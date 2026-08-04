import json
from langchain_core.messages import SystemMessage, HumanMessage
from eos.domain.contracts.visual_proposal import VisualProposal
from eos.domain.contracts.creative_direction import CreativeDirection
from eos.domain.contracts.editorial_brief import EditorialBrief
from eos.domain.contracts.research_report import ResearchReport
from eos.domain.contracts.brand_audit_report import BrandAuditReport
from eos.domain.contracts.base import AuditStatus
from eos.infrastructure.llm_router import ModelRouter, AgentRole
from eos.infrastructure.context_loader import MarkdownContextLoader


class BrandGuardianAgent:
    """
    Brand Guardian Agent do EOS (EOS-004).
    
    O primeiro agente do EOS que JULGA em vez de PRODUZIR.
    Atua como o "sistema imunológico" da marca, auditando
    a coerência entre intenção (Brief + Direction) e execução (Proposal)
    contra a constituição inegociável da High House.
    
    Princípio fail-secure: em caso de qualquer falha (timeout, parsing,
    exceção), o Guardian NUNCA aprova. Retorna HUMAN_REVIEW_REQUIRED.
    """
    
    def __init__(self):
        # Carrega o contexto dedicado de 04_AGENT_CONTEXTS/brand_guardian_context.md
        self.system_prompt = MarkdownContextLoader.load("Brand Guardian Agent")
        # Roteia para o modelo do papel VALIDATOR
        self.llm = ModelRouter.get_model_for_role(AgentRole.VALIDATOR)
        
    def audit(
        self,
        proposal: VisualProposal,
        direction: CreativeDirection,
        brief: EditorialBrief | None = None,
        research: ResearchReport | None = None
    ) -> BrandAuditReport:
        """
        Executa a auditoria de marca contra os artefatos produzidos pelo pipeline.
        
        Recebe os 4 artefatos do pipeline (brief e research são opcionais para 
        compatibilidade com fases onde ainda não existem) e retorna um BrandAuditReport
        estrito em Pydantic.
        
        Fail-secure: Qualquer exceção retorna HUMAN_REVIEW_REQUIRED.
        Nunca APPROVED por default.
        """
        human_msg = self._build_audit_message(proposal, direction, brief, research)
        
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=human_msg)
        ]
        
        structured_llm = self.llm.with_structured_output(BrandAuditReport)
        
        try:
            response = structured_llm.invoke(messages)
            return self._parse_response(response)
        except Exception:
            # Fail-secure: qualquer falha → HUMAN_REVIEW_REQUIRED
            return self._fail_secure_report(
                context="Falha na execução do LLM ou parsing da resposta"
            )
    
    def _build_audit_message(
        self,
        proposal: VisualProposal,
        direction: CreativeDirection,
        brief: EditorialBrief | None = None,
        research: ResearchReport | None = None
    ) -> str:
        """Constrói a mensagem de auditoria com todos os artefatos disponíveis."""
        sections = []
        
        if brief:
            sections.append(
                f"--- EDITORIAL BRIEF ---\n"
                f"Topic: {brief.topic}\n"
                f"Objective: {brief.objective}\n"
                f"Audience: {brief.audience}\n"
                f"Cultural Context: {brief.cultural_context}\n"
                f"Constraints: {', '.join(brief.constraints)}"
            )
        
        if research:
            sections.append(
                f"--- RESEARCH REPORT ---\n"
                f"Sources: {', '.join(research.sources)}\n"
                f"Cultural Hypotheses: {'; '.join(research.cultural_hypotheses)}\n"
                f"Key Findings: {'; '.join(research.key_findings)}\n"
                f"Confidence: {research.confidence_score}"
            )
        
        sections.append(
            f"--- CREATIVE DIRECTION ---\n"
            f"Core Concept: {direction.core_concept}\n"
            f"Editorial Intent: {direction.editorial_intent}\n"
            f"Aesthetic Mood: {direction.aesthetic_mood}\n"
            f"References: {', '.join(direction.references)}"
        )
        
        sections.append(
            f"--- VISUAL PROPOSAL (UNDER AUDIT) ---\n"
            f"Grid Structure: {proposal.grid_structure}\n"
            f"Visual Elements: {', '.join(proposal.visual_elements)}\n"
            f"Color Palette: {', '.join(proposal.color_palette)}\n"
            f"Typography Spec: {proposal.typography_spec}\n"
            f"Generation Prompt: {proposal.generation_prompt}\n"
            f"Implementation Notes: {proposal.implementation_notes}"
        )
        
        return "\n\n".join(sections)
    
    def _parse_response(self, response) -> BrandAuditReport:
        """
        Parseia a resposta do LLM em BrandAuditReport.
        Fail-secure: se o parsing falhar, retorna HUMAN_REVIEW_REQUIRED.
        """
        try:
            if isinstance(response, BrandAuditReport):
                return response
            elif isinstance(response, dict):
                return BrandAuditReport(**response)
        except Exception:
            pass
        
        # Fail-secure: parsing falhou → HUMAN_REVIEW_REQUIRED
        return self._fail_secure_report(
            context="Resposta do LLM não pôde ser parseada em BrandAuditReport válido"
        )
    
    @staticmethod
    def _fail_secure_report(context: str) -> BrandAuditReport:
        """
        Retorno fail-secure. Nunca APPROVED.
        Em caso de qualquer falha, emite HUMAN_REVIEW_REQUIRED.
        """
        return BrandAuditReport(
            status=AuditStatus.HUMAN_REVIEW_REQUIRED,
            evaluated_rules=["Fail-secure acionado"],
            violations=["Auditoria inconclusiva por falha técnica"],
            severity="Critical",
            justification=(
                "O Brand Guardian não conseguiu completar a auditoria devido a uma "
                "falha técnica. Conforme o princípio fail-secure (04_AGENT_SPECIFICATIONS §3.1, §14), "
                "em caso de dúvida ou falha, o agente aciona HUMAN_REVIEW_REQUIRED."
            ),
            audit_context=context,
            recommendations=["Revisão humana obrigatória antes de prosseguir."]
        )
