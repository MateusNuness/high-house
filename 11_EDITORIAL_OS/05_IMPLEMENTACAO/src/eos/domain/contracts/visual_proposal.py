from pydantic import BaseModel

class VisualProposal(BaseModel):
    grid_structure: str
    visual_elements: list[str]
    color_palette: list[str]
    typography_spec: str
    generation_prompt: str
    implementation_notes: str
