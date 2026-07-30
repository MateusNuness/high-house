"""
Dummy Agent Contracts for MVP validation.
"""
from pydantic import BaseModel, Field

class DummyAgentInput(BaseModel):
    """Input contract for the Dummy Agent."""
    raw_text: str = Field(..., description="The raw text to be processed.")
    context_id: str = Field(..., description="The ID of the current context/collection.")

class DummyAgentOutput(BaseModel):
    """Output contract for the Dummy Agent."""
    processed_text: str = Field(..., description="The processed text.")
    confidence_score: float = Field(..., description="Confidence score of the processing.")
    status: str = Field(..., description="Status of the operation (e.g., 'SUCCESS', 'FAILED').")
