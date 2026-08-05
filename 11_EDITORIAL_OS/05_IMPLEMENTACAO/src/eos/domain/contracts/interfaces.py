from typing import Protocol, Any
from eos.domain.contracts.editorial_brief import EditorialBrief
from eos.domain.contracts.research_report import ResearchReport
from eos.domain.contracts.creative_direction import CreativeDirection
from eos.domain.contracts.visual_proposal import VisualProposal
from eos.domain.contracts.brand_audit_report import BrandAuditReport
from eos.domain.contracts.image_asset import ImageAsset
from eos.domain.contracts.rendered_code import RenderedCode
from eos.domain.contracts.vision_audit_report import VisionAuditReport
from eos.domain.collection_history import CollectionHistory

class ICoderAgent(Protocol):
    def run(
        self, 
        proposal: VisualProposal, 
        brief: EditorialBrief, 
        direction: CreativeDirection, 
        image: ImageAsset | None = None
    ) -> RenderedCode:
        ...

class IVisionAgent(Protocol):
    def audit(self, rendered_code: RenderedCode) -> VisionAuditReport:
        ...

class IResearchAgent(Protocol):
    def run(self, brief: EditorialBrief) -> ResearchReport:
        ...

class IEditorialAgent(Protocol):
    def run(self, report: ResearchReport, history: CollectionHistory | None = None) -> CreativeDirection:
        ...

class IArtDirectorAgent(Protocol):
    def run(self, direction: CreativeDirection, history: CollectionHistory | None = None) -> CreativeDirection:
        ...

class IDesignerAgent(Protocol):
    def run(self, direction: CreativeDirection) -> VisualProposal:
        ...

class IBrandGuardianAgent(Protocol):
    def audit(
        self,
        proposal: VisualProposal,
        direction: CreativeDirection,
        brief: EditorialBrief,
        research: ResearchReport
    ) -> BrandAuditReport:
        ...

class IImageAgent(Protocol):
    def run(self, proposal: VisualProposal) -> ImageAsset:
        ...

class IMemoryAgent(Protocol):
    def log_event(self, event_type: str, details: dict[str, Any]) -> None:
        ...
    
    def save_decision(self, agent_id: str, context: str, data: dict[str, Any]) -> None:
        ...
