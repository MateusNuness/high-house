from typing import TypedDict, Optional
from .contracts import (
    EditorialBrief,
    ResearchReport,
    CreativeDirection,
    VisualProposal,
    BrandAuditReport,
    PublicationPackage,
    ImageAsset,
    RenderedCode,
    VisionAuditReport
)

class GlobalState(TypedDict):
    execution_id: str
    thread_id: str
    current_phase: str
    current_agent: str
    audit_log: list[str]
    audit_events: list[dict]
    errors: list[str]
    revision_count: int  # Contador de loops Designer ↔ Guardian (workflow, não domínio)
    previous_posters: list[dict]
    
    # Artifacts as separated states
    brief: Optional[EditorialBrief]
    research: Optional[ResearchReport]
    direction: Optional[CreativeDirection]
    proposal: Optional[VisualProposal]
    audit: Optional[BrandAuditReport]
    image_asset: Optional[ImageAsset]
    rendered_code: Optional[RenderedCode]
    vision_audit: Optional[VisionAuditReport]
    vision_revision_count: int
    package: Optional[PublicationPackage]

