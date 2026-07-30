import pytest
from pydantic import ValidationError

from eos.domain.contracts import (
    EditorialBrief,
    BrandAuditReport,
    AuditStatus
)
from eos.application.workflows.editorial_creation import app

def test_workflow_end_to_end():
    """Test the complete execution of the LangGraph workflow with mocked nodes."""
    
    initial_brief = EditorialBrief(
        topic="Xarpi Carioca",
        objective="Highlight the subversive nature of Xarpi",
        audience="Underground culture enthusiasts",
        cultural_context="Rio de Janeiro urban scene",
        constraints=["Do not romanticize vandalism excessively", "Keep it authentic"],
        source_reference="Internal research",
        created_by="Human Director"
    )
    
    initial_state = {
        "execution_id": "test-execution-001",
        "current_phase": "started",
        "audit_log": ["Workflow started"],
        "brief": initial_brief,
        "research": None,
        "direction": None,
        "proposal": None,
        "audit": None,
        "package": None
    }
    
    # Run the graph
    final_state = app.invoke(initial_state)
    
    # Assertions
    assert final_state["current_phase"] == "publication_ready"
    assert final_state["research"] is not None
    assert final_state["direction"] is not None
    assert final_state["proposal"] is not None
    assert final_state["audit"] is not None
    assert final_state["package"] is not None
    
    # Check if specific mocked values are present
    assert final_state["research"].confidence_score == 0.85
    assert final_state["direction"].desired_emotion == "Tension and awe"
    assert final_state["audit"].status == AuditStatus.APPROVED
    assert "Publication Package generated" in final_state["audit_log"]


def test_invalid_contract_fails():
    """Test that creating an invalid Pydantic model raises ValidationError."""
    
    # Missing required fields
    with pytest.raises(ValidationError):
        EditorialBrief(topic="Only topic")
        
    # Invalid Enum status
    with pytest.raises(ValidationError):
        BrandAuditReport(
            status="INVALID_STATUS", # Should be from AuditStatus Enum
            evaluated_rules=["Rule 1"],
            violations=[],
            severity="High",
            justification="Because.",
            audit_context="Testing",
            recommendations=[]
        )
