from pydantic import BaseModel

class CreativeDirection(BaseModel):
    core_concept: str
    editorial_intent: str
    aesthetic_mood: str
    references: list[str]
    suggested_caption: str = ""

