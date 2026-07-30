from pydantic import BaseModel

class ResearchReport(BaseModel):
    sources: list[str]
    cultural_hypotheses: list[str]
    key_findings: list[str]
    confidence_score: float
