from pydantic import BaseModel
from typing import Optional
from eos.domain.contracts.base import AuditStatus

class TechnicalAudit(BaseModel):
    has_layout_break: bool
    has_overflow: bool
    details: str

class AestheticAudit(BaseModel):
    passes_vibe_check: bool
    details: str

class VisionAuditReport(BaseModel):
    technical_audit: TechnicalAudit
    aesthetic_audit: AestheticAudit
    final_status: AuditStatus
    justification: str
    failure_coordinates: Optional[str] = None
