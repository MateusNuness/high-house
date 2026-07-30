from pydantic import BaseModel

class CreativeDirection(BaseModel):
    core_concept: str
    editorial_intent: str
    desired_emotion: str
    aesthetic_mood: str
    cultural_reference: str
    strategic_alignment: str
    references: list[str]
