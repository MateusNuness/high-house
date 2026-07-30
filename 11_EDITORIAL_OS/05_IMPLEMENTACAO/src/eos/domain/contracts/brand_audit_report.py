from pydantic import BaseModel
from .base import AuditStatus

class BrandAuditReport(BaseModel):
    status: AuditStatus
    evaluated_rules: list[str]
    violations: list[str]
    severity: str
    justification: str
    audit_context: str
    recommendations: list[str]
