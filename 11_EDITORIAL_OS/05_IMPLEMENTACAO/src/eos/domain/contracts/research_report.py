from pydantic import BaseModel

class ResearchReport(BaseModel):
    research_question: str
    methodology: str
    sources: list[str]
    cultural_hypotheses: list[str]
    key_findings: list[str]
    cultural_relevance: str
    limitations: str
    confidence_score: float
