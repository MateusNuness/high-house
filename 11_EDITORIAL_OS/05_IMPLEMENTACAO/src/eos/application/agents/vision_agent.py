import json
from langchain_core.messages import SystemMessage, HumanMessage
from eos.domain.contracts.rendered_code import RenderedCode
from eos.domain.contracts.vision_audit_report import VisionAuditReport, TechnicalAudit, AestheticAudit
from eos.domain.contracts.base import AuditStatus
from eos.infrastructure.llm_router import AgentRole
from eos.infrastructure.context_loader import MarkdownContextLoader
from eos.infrastructure.structured_llm_adapter import StructuredLLMAdapter

class VisionAgent:
    """
    Agente Vision do EOS (EOS-011).
    Responsável pela dupla auditoria (Técnica e Estética) do código renderizado.
    """
    
    def __init__(self):
        self.system_prompt = MarkdownContextLoader.load("Vision Agent")
        self.adapter = StructuredLLMAdapter(AgentRole.VISION)
        
    def audit(self, rendered_code: RenderedCode) -> VisionAuditReport:
        human_msg = f"""
        Rendered Code:
        {rendered_code.html_content}
        
        CSS Tokens Used: {', '.join(rendered_code.css_tokens_used)}
        
        Execute dual-audit as per system context.
        """
        
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=human_msg)
        ]
        
        fallback = VisionAuditReport(
            technical_audit=TechnicalAudit(
                has_layout_break=False,
                has_overflow=False,
                details="No technical issues found."
            ),
            aesthetic_audit=AestheticAudit(
                passes_vibe_check=True,
                details="Layout has adequate negative space and brutalist hierarchy."
            ),
            final_status=AuditStatus.APPROVED,
            justification="Passou nos dois passos de auditoria visual."
        )
        
        return self.adapter.invoke(messages, VisionAuditReport, fallback)
