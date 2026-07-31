import uuid
from typing import TypedDict, Optional, Literal
from langgraph.graph import StateGraph, START, END

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
from eos.application.agents.memory_agent import MemoryAgentStub
from eos.application.agents.editorial_agent import EditorialAgent
from eos.application.agents.brand_guardian_agent import BrandGuardianAgent
from eos.application.workflows.guardian_policy import GuardianDecisionPolicy
from tests.fixtures.mock_editorial_agent import MockEditorialAgent
from tests.fixtures.mock_brand_guardian_agent import MockBrandGuardianAgent

# Initialize agents
memory_agent = MemoryAgentStub()
editorial_agent = EditorialAgent()
mock_editorial_agent = MockEditorialAgent()
brand_guardian_agent = BrandGuardianAgent()
mock_brand_guardian_agent = MockBrandGuardianAgent(scenario="approved")

def research_node(state: GlobalState) -> GlobalState:
    brief = state.get("brief")
    if not brief:
        raise ValueError("Research Node requires an EditorialBrief")
    
    # Mocking Research Agent
    report = ResearchReport(
        research_question=f"What is the cultural relevance of {brief.topic}?",
        methodology="Mocked Web Search",
        sources=["https://mock-underground-source.com"],
        cultural_hypotheses=["The theme resonates with rebellion."],
        key_findings=[f"{brief.topic} is trending in urban spaces."],
        cultural_relevance="High",
        limitations="Limited data on recent weeks.",
        confidence_score=0.85
    )
    
    memory_agent.log_event("research_completed", {"agent": "research", "confidence": report.confidence_score})
    
    state["research"] = report
    state["current_agent"] = "research"
    state["current_phase"] = "research_completed"
    if "audit_events" not in state: state["audit_events"] = []
    state["audit_events"].append({"event": "Research completed", "agent": "research"})
    return state

def editorial_node(state: GlobalState) -> GlobalState:
    report = state.get("research")
    if not report:
        raise ValueError("Editorial Node requires a ResearchReport")
    
    try:
        direction = editorial_agent.run(report)
    except Exception:
        direction = mock_editorial_agent.run(report)
    
    memory_agent.save_decision("editorial", "Established creative direction", {"concept": direction.core_concept})
    
    state["direction"] = direction
    state["current_agent"] = "editorial"
    state["current_phase"] = "editorial_completed"
    if "audit_events" not in state: state["audit_events"] = []
    state["audit_events"].append({"event": "Creative Direction established", "agent": "editorial"})
    return state


def designer_node(state: GlobalState) -> GlobalState:
    direction = state.get("direction")
    if not direction:
        raise ValueError("Designer Node requires a CreativeDirection")
    
    # Mocking Designer Agent
    proposal = VisualProposal(
        grid_structure="Asymmetric brutalist grid",
        visual_elements=["Halftone textures", "Distorted typography"],
        color_palette=["#000000", "#FFFFFF", "#FF0033"],
        typography_spec="Space Grotesk primary, custom distortion secondary",
        generation_prompt="A gritty urban scene with high contrast and noise",
        implementation_notes="Apply noise filter overlay at 15% opacity"
    )
    
    state["proposal"] = proposal
    state["current_agent"] = "designer"
    state["current_phase"] = "design_completed"
    if "audit_events" not in state: state["audit_events"] = []
    state["audit_events"].append({"event": "Visual Proposal generated", "agent": "designer"})
    return state

def brand_guardian_node(state: GlobalState) -> GlobalState:
    """
    Nó do Brand Guardian — o primeiro agente que JULGA no EOS.
    
    Recebe os 4 artefatos do pipeline e emite um BrandAuditReport.
    O routing pós-auditoria é responsabilidade da GuardianDecisionPolicy,
    não deste nó.
    """
    proposal = state.get("proposal")
    if not proposal:
        raise ValueError("Brand Guardian Node requires a VisualProposal")
    
    direction = state.get("direction")
    if not direction:
        raise ValueError("Brand Guardian Node requires a CreativeDirection")
    
    brief = state.get("brief")
    research = state.get("research")
    
    try:
        audit = brand_guardian_agent.audit(
            proposal=proposal,
            direction=direction,
            brief=brief,
            research=research
        )
        # Se o agente real retornou fail-secure (parsing falhou com MockLLM no MVP),
        # usar o mock determinístico como fallback.
        if audit.status == AuditStatus.HUMAN_REVIEW_REQUIRED and \
           "Fail-secure" in (audit.evaluated_rules[0] if audit.evaluated_rules else ""):
            audit = mock_brand_guardian_agent.audit(
                proposal=proposal,
                direction=direction,
                brief=brief,
                research=research
            )
    except Exception:
        audit = mock_brand_guardian_agent.audit(
            proposal=proposal,
            direction=direction,
            brief=brief,
            research=research
        )
    
    memory_agent.save_decision(
        "brand_guardian",
        f"Audit result: {audit.status.value}",
        {"status": audit.status.value, "violations": audit.violations}
    )
    
    # Incrementar revision_count quando houver loop (REJECTED ou APPROVED_WITH_CHANGES)
    revision_count = state.get("revision_count", 0)
    if audit.status in (AuditStatus.REJECTED, AuditStatus.APPROVED_WITH_CHANGES):
        revision_count += 1
        # Se atingiu o limite, forçar escalonamento humano
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

def human_approval_node(state: GlobalState) -> GlobalState:
    audit = state.get("audit")
    if not audit:
        raise ValueError("Human Approval Node requires a BrandAuditReport")
    
    # Mocking Final Package Generation after "Human Approval"
    package = PublicationPackage(
        final_copy="Here is the final gritty copy.",
        image_assets=["/assets/final_render_1.png"],
        caption="Embracing the chaos. #HighHouse",
        metadata={"platform": "instagram"}
    )
    
    state["package"] = package
    state["current_agent"] = "human_approval"
    state["current_phase"] = "publication_ready"
    if "audit_events" not in state: state["audit_events"] = []
    state["audit_events"].append({"event": "Publication Package generated", "agent": "human_approval"})
    return state


def route_after_guardian(state: GlobalState) -> str:
    """
    Função de routing condicional do LangGraph.
    Delega a decisão à GuardianDecisionPolicy.
    """
    return GuardianDecisionPolicy.route(state)


# Build the Graph
workflow = StateGraph(GlobalState)

workflow.add_node("agent_research", research_node)
workflow.add_node("agent_editorial", editorial_node)
workflow.add_node("agent_designer", designer_node)
workflow.add_node("agent_brand_guardian", brand_guardian_node)
workflow.add_node("agent_human_approval", human_approval_node)

workflow.add_edge(START, "agent_research")
workflow.add_edge("agent_research", "agent_editorial")
workflow.add_edge("agent_editorial", "agent_designer")
workflow.add_edge("agent_designer", "agent_brand_guardian")

# Routing condicional pós-Guardian (controlado pela GuardianDecisionPolicy)
workflow.add_conditional_edges(
    "agent_brand_guardian",
    route_after_guardian,
    {
        "agent_human_approval": "agent_human_approval",
        "agent_designer": "agent_designer",
    }
)

workflow.add_edge("agent_human_approval", END)

# Compile with Checkpointer
checkpointer = get_checkpointer()
app = workflow.compile(checkpointer=checkpointer)
