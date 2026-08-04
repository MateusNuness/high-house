from typing import Protocol, Any
from eos.domain.contracts.editorial_brief import EditorialBrief
from eos.domain.contracts.research_report import ResearchReport
from eos.domain.contracts.creative_direction import CreativeDirection
from eos.domain.contracts.visual_proposal import VisualProposal
from eos.domain.contracts.brand_audit_report import BrandAuditReport

class IResearchAgent(Protocol):
    def run(self, brief: EditorialBrief) -> ResearchReport:
        ...

class IEditorialAgent(Protocol):
    def run(self, report: ResearchReport) -> CreativeDirection:
        ...

class IArtDirectorAgent(Protocol):
    def run(self, direction: CreativeDirection) -> CreativeDirection:
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

class IMemoryAgent(Protocol):
    def log_event(self, event_type: str, details: dict[str, Any]) -> None:
        ...
    
    def save_decision(self, agent_id: str, context: str, data: dict[str, Any]) -> None:
        ...
