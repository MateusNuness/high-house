from pydantic import BaseModel
from typing import List

class RenderedCode(BaseModel):
    html_content: str
    css_tokens_used: List[str]
    notes: str = ""
