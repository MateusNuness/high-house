from typing import TypedDict, Optional, Literal, cast
from langgraph.graph import StateGraph, START, END
from langgraph.graph.state import CompiledStateGraph

from eos.domain.contracts import (
    EditorialBrief,
    ResearchReport,
    CreativeDirection,
    VisualProposal,
    BrandAuditReport,
    PublicationPackage,
    AuditStatus
)
from eos.domain.state import GlobalState
from eos.infrastructure.checkpoints import get_checkpointer
from eos.application.workflows.guardian_policy import GuardianDecisionPolicy
from eos.domain.contracts.interfaces import (
    IResearchAgent,
    IEditorialAgent,
    IArtDirectorAgent,
    IDesignerAgent,
    IBrandGuardianAgent,
    IMemoryAgent,
    ICoderAgent,
    IVisionAgent,
    IImageAgent
)

class EditorialWorkflow:
    """
    Class-based Workflow para a Criação Editorial do High House EOS.
    Utiliza Injeção de Dependência para receber os agentes, garantindo que
    os nós atuem apenas como Thin Adapters sem lógicas de domínio ou fallbacks.
    """

    def __init__(
        self,
        research_agent: IResearchAgent,
        editorial_agent: IEditorialAgent,
        art_director_agent: IArtDirectorAgent,
        designer_agent: IDesignerAgent,
        brand_guardian_agent: IBrandGuardianAgent,
        memory_agent: IMemoryAgent,
        coder_agent: ICoderAgent,
        vision_agent: IVisionAgent,
        image_agent: IImageAgent
    ):
        self.research_agent = research_agent
        self.editorial_agent = editorial_agent
        self.art_director_agent = art_director_agent
        self.designer_agent = designer_agent
        self.brand_guardian_agent = brand_guardian_agent
        self.memory_agent = memory_agent
        self.coder_agent = coder_agent
        self.vision_agent = vision_agent
        self.image_agent = image_agent

    def _research_node(self, state: GlobalState) -> GlobalState:
        brief = state.get("brief")
        if not brief:
            raise ValueError("Research Node requires an EditorialBrief")
        
        report = self.research_agent.run(brief)
        
        self.memory_agent.log_event("research_completed", {"agent": "research", "confidence": report.confidence_score})
        
        state["research"] = report
        state["current_agent"] = "research"
        state["current_phase"] = "research_completed"
        if "audit_events" not in state: state["audit_events"] = []
        state["audit_events"].append({"event": "Research completed", "agent": "research"})
        return state

    def _editorial_node(self, state: GlobalState) -> GlobalState:
        report = state.get("research")
        if not report:
            raise ValueError("Editorial Node requires a ResearchReport")
        
        direction = self.editorial_agent.run(report)
        
        self.memory_agent.save_decision("editorial", "Established creative direction", {"concept": direction.core_concept})
        
        state["direction"] = direction
        state["current_agent"] = "editorial"
        state["current_phase"] = "editorial_completed"
        if "audit_events" not in state: state["audit_events"] = []
        state["audit_events"].append({"event": "Creative Direction established", "agent": "editorial"})
        return state

    def _art_director_node(self, state: GlobalState) -> GlobalState:
        direction = state.get("direction")
        if not direction:
            raise ValueError("Art Director Node requires a CreativeDirection")
        
        direction = self.art_director_agent.run(direction)
            
        self.memory_agent.save_decision("art_director", "Enriched creative direction with aesthetic mood", {"mood": direction.aesthetic_mood})
        
        state["direction"] = direction
        state["current_agent"] = "art_director"
        state["current_phase"] = "art_direction_completed"
        if "audit_events" not in state: state["audit_events"] = []
        state["audit_events"].append({"event": "Aesthetic mood defined", "agent": "art_director"})
        return state

    def _designer_node(self, state: GlobalState) -> GlobalState:
        direction = state.get("direction")
        if not direction:
            raise ValueError("Designer Node requires a CreativeDirection")
        
        proposal = self.designer_agent.run(direction)
        
        self.memory_agent.save_decision("designer", "Generated Design Blueprint", {"grid": proposal.grid_structure})
        
        state["proposal"] = proposal
        state["current_agent"] = "designer"
        state["current_phase"] = "design_completed"
        if "audit_events" not in state: state["audit_events"] = []
        state["audit_events"].append({"event": "Visual Proposal generated", "agent": "designer"})
        return state

    def _brand_guardian_node(self, state: GlobalState) -> GlobalState:
        proposal = state.get("proposal")
        if not proposal:
            raise ValueError("Brand Guardian Node requires a VisualProposal")
        
        direction = state.get("direction")
        if not direction:
            raise ValueError("Brand Guardian Node requires a CreativeDirection")
        
        brief = state.get("brief")
        research = state.get("research")
        
        # Tipando os parâmetros que podem ser None (para fins de type hinting), 
        # assumindo que chegar neste estágio implica que existem, mas garantimos no assert.
        assert brief is not None
        assert research is not None

        audit = self.brand_guardian_agent.audit(
            proposal=proposal,
            direction=direction,
            brief=brief,
            research=research
        )
        
        self.memory_agent.save_decision(
            "brand_guardian",
            f"Audit result: {audit.status.value}",
            {"status": audit.status.value, "violations": audit.violations}
        )
        
        revision_count = state.get("revision_count", 0)
        if audit.status in (AuditStatus.REJECTED, AuditStatus.APPROVED_WITH_CHANGES):
            revision_count += 1
            if revision_count >= GuardianDecisionPolicy.MAX_REVISIONS:
                audit = BrandAuditReport(
                    status=AuditStatus.HUMAN_REVIEW_REQUIRED,
                    evaluated_rules=audit.evaluated_rules,
                    violations=audit.violations,
                    severity="Critical",
                    justification=(
                        f"Limite de {GuardianDecisionPolicy.MAX_REVISIONS} revisões atingido. "
                        f"Escalonando para revisão humana. Última justificativa: {audit.justification}"
                    ),
                    audit_context=f"Escalonamento automático após {revision_count} revisões",
                    recommendations=audit.recommendations + [
                        "Intervenção humana obrigatória — limite de revisões automáticas atingido."
                    ]
                )
        
        state["audit"] = audit
        state["revision_count"] = revision_count
        state["current_agent"] = "brand_guardian"
        state["current_phase"] = "audit_completed"
        if "audit_events" not in state: state["audit_events"] = []
        state["audit_events"].append({
            "event": f"Brand Audit completed: {audit.status.value}",
            "agent": "brand_guardian",
            "revision": revision_count
        })
        return state

    def _image_node(self, state: GlobalState) -> GlobalState:
        proposal = state.get("proposal")
        if not proposal:
            raise ValueError("Image Node requires a VisualProposal")
        
        image_asset = self.image_agent.run(proposal)
        
        self.memory_agent.log_event("image_generated", {"agent": "image_agent", "url": image_asset.image_url})
        
        state["image_asset"] = image_asset
        state["current_agent"] = "image"
        state["current_phase"] = "image_generation_completed"
        if "audit_events" not in state: state["audit_events"] = []
        state["audit_events"].append({"event": "Base Image generated", "agent": "image_agent"})
        return state

    def _coder_node(self, state: GlobalState) -> GlobalState:
        proposal = state.get("proposal")
        if not proposal:
            raise ValueError("Coder Node requires a VisualProposal")
        
        rendered_code = self.coder_agent.run(proposal)
        
        self.memory_agent.log_event("coding_completed", {"agent": "coder"})
        
        state["rendered_code"] = rendered_code
        state["current_agent"] = "coder"
        state["current_phase"] = "coding_completed"
        if "audit_events" not in state: state["audit_events"] = []
        state["audit_events"].append({"event": "Code generated", "agent": "coder"})
        return state

    def _vision_node(self, state: GlobalState) -> GlobalState:
        rendered_code = state.get("rendered_code")
        if not rendered_code:
            raise ValueError("Vision Node requires RenderedCode")
        
        audit = self.vision_agent.audit(rendered_code)
        
        self.memory_agent.log_event(
            "vision_audit", 
            {"status": audit.final_status.value, "details": audit.technical_audit.details}
        )
        
        vision_revision_count = state.get("vision_revision_count", 0)
        if audit.final_status == AuditStatus.REJECTED:
            vision_revision_count += 1
            if vision_revision_count >= GuardianDecisionPolicy.MAX_REVISIONS:
                audit.final_status = AuditStatus.HUMAN_REVIEW_REQUIRED
                audit.justification = "Vision max revisions reached. Escalating to human."
        
        state["vision_audit"] = audit
        state["vision_revision_count"] = vision_revision_count
        state["current_agent"] = "vision"
        state["current_phase"] = "vision_audit_completed"
        if "audit_events" not in state: state["audit_events"] = []
        state["audit_events"].append({"event": f"Vision Audit: {audit.final_status.value}", "agent": "vision"})
        return state

    def _human_approval_node(self, state: GlobalState) -> GlobalState:
        audit = state.get("audit")
        if not audit:
            raise ValueError("Human Approval Node requires a BrandAuditReport")
        
        direction = state.get("direction")
        image_asset = state.get("image_asset")
        
        caption = direction.suggested_caption if direction and hasattr(direction, "suggested_caption") else "High House."
        image_url = image_asset.image_url if image_asset else ""
        
        package = PublicationPackage(
            final_copy=caption,
            image_assets=[image_url] if image_url else [],
            caption=caption,
            metadata={"platform": "instagram"}
        )
        
        state["package"] = package
        state["current_agent"] = "human_approval"
        state["current_phase"] = "publication_ready"
        if "audit_events" not in state: state["audit_events"] = []
        state["audit_events"].append({"event": "Publication Package generated", "agent": "human_approval"})
        return state

    def _route_after_guardian(self, state: GlobalState) -> str:
        return GuardianDecisionPolicy.route(state)

    def _route_after_vision(self, state: GlobalState) -> str:
        audit = state.get("vision_audit")
        if not audit:
            return "agent_human_approval"
        if audit.final_status == AuditStatus.APPROVED:
            return "agent_human_approval"
        elif audit.final_status == AuditStatus.HUMAN_REVIEW_REQUIRED:
            return "agent_human_approval"
        else:
            return "agent_coder"

    def build_app(self) -> CompiledStateGraph:
        workflow = StateGraph(GlobalState)

        workflow.add_node("agent_research", self._research_node)
        workflow.add_node("agent_editorial", self._editorial_node)
        workflow.add_node("agent_art_director", self._art_director_node)
        workflow.add_node("agent_designer", self._designer_node)
        workflow.add_node("agent_brand_guardian", self._brand_guardian_node)
        workflow.add_node("agent_image", self._image_node)
        workflow.add_node("agent_coder", self._coder_node)
        workflow.add_node("agent_vision", self._vision_node)
        workflow.add_node("agent_human_approval", self._human_approval_node)

        workflow.add_edge(START, "agent_research")
        workflow.add_edge("agent_research", "agent_editorial")
        workflow.add_edge("agent_editorial", "agent_art_director")
        workflow.add_edge("agent_art_director", "agent_designer")
        workflow.add_edge("agent_designer", "agent_brand_guardian")

        workflow.add_conditional_edges(
            "agent_brand_guardian",
            self._route_after_guardian,
            {
                "agent_human_approval": "agent_human_approval",
                "agent_designer": "agent_designer",
                "agent_image": "agent_image",
            }
        )
        
        workflow.add_edge("agent_image", "agent_coder")
        workflow.add_edge("agent_coder", "agent_vision")
        
        workflow.add_conditional_edges(
            "agent_vision",
            self._route_after_vision,
            {
                "agent_human_approval": "agent_human_approval",
                "agent_coder": "agent_coder",
            }
        )
        
        workflow.add_edge("agent_human_approval", END)

        checkpointer = get_checkpointer()
        return workflow.compile(checkpointer=checkpointer)
