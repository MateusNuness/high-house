from pydantic import BaseModel

class EditorialBrief(BaseModel):
    topic: str
    objective: str
    audience: str
    cultural_context: str
    constraints: list[str]
    source_reference: str
    created_by: str
