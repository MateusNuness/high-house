from typing import TypedDict, Optional
from .contracts import (
    EditorialBrief,
    ResearchReport,
    CreativeDirection,
    VisualProposal,
    BrandAuditReport,
    PublicationPackage
)

class GlobalState(TypedDict):
    execution_id: str
    thread_id: str
    current_phase: str
    current_agent: str
    audit_log: list[str]
    audit_events: list[dict]
    errors: list[str]
    
    # Artifacts as separated states
    brief: Optional[EditorialBrief]
    research: Optional[ResearchReport]
    direction: Optional[CreativeDirection]
    proposal: Optional[VisualProposal]
    audit: Optional[BrandAuditReport]
    package: Optional[PublicationPackage]
