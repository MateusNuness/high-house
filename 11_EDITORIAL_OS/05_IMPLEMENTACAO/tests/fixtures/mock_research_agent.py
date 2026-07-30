from eos.domain.contracts.editorial_brief import EditorialBrief
from eos.domain.contracts.research_report import ResearchReport

class MockResearchAgent:
    """
    Fallback agent that returns a hardcoded ResearchReport for testing purposes without hitting any API.
    """
    
    def run(self, brief: EditorialBrief) -> ResearchReport:
        return ResearchReport(
            sources=["http://mock-source-1.com", "http://mock-source-2.com"],
            cultural_hypotheses=[
                f"Mocked hypothesis based on {brief.topic}",
                "Another cultural hypothesis linking to underground movements"
            ],
            key_findings=[
                "Finding 1: Xarpi represents marginal history.",
                "Finding 2: The aesthetics are deeply tied to the city's architecture."
            ],
            confidence_score=0.95
        )
