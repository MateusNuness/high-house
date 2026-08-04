from eos.domain.contracts.rendered_code import RenderedCode
from eos.domain.contracts.vision_audit_report import VisionAuditReport, TechnicalAudit, AestheticAudit
from eos.domain.contracts.base import AuditStatus

class MockVisionAgent:
    def __init__(self, scenario: str = "approved"):
        self.scenario = scenario

    def audit(self, rendered_code: RenderedCode) -> VisionAuditReport:
        if self.scenario == "approved":
            return VisionAuditReport(
                technical_audit=TechnicalAudit(has_layout_break=False, has_overflow=False, details="OK"),
                aesthetic_audit=AestheticAudit(passes_vibe_check=True, details="Aura mantida"),
                final_status=AuditStatus.APPROVED,
                justification="Visual validado."
            )
        else:
            return VisionAuditReport(
                technical_audit=TechnicalAudit(has_layout_break=True, has_overflow=False, details="Texto vazando"),
                aesthetic_audit=AestheticAudit(passes_vibe_check=False, details="Parece genérico"),
                final_status=AuditStatus.REJECTED,
                justification="Reprovado na auditoria dupla.",
                failure_coordinates="body > article > h1"
            )
