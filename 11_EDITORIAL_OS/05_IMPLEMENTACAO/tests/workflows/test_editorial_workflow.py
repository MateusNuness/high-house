import pytest
from pydantic import ValidationError

from eos.domain.contracts import (
    EditorialBrief,
    BrandAuditReport,
    AuditStatus
)
from eos.domain.state import GlobalState
from eos.application.workflows.guardian_policy import GuardianDecisionPolicy


def _make_initial_state() -> dict:
    """Cria o estado inicial padrão para os testes de workflow."""
    initial_brief = EditorialBrief(
        topic="Xarpi Carioca",
        objective="Highlight the subversive nature of Xarpi",
        audience="Underground culture enthusiasts",
        cultural_context="Rio de Janeiro urban scene",
        constraints=["Do not romanticize vandalism excessively", "Keep it authentic"],
        source_reference="Internal research",
        created_by="Human Director"
    )
    
    return {
        "execution_id": "test-execution-001",
        "current_phase": "started",
        "current_agent": "",
        "audit_log": ["Workflow started"],
        "audit_events": [],
        "errors": [],
        "revision_count": 0,
        "brief": initial_brief,
        "research": None,
        "direction": None,
        "proposal": None,
        "audit": None,
        "package": None
    }


def test_workflow_end_to_end():
    """Test the complete execution of the LangGraph workflow with mocked nodes."""
    from eos.application.workflows.editorial_creation import app
    
    initial_state = _make_initial_state()
    config = {"configurable": {"thread_id": "test-thread-001"}}
    
    # Run the graph
    final_state = app.invoke(initial_state, config=config)
    
    # Assertions
    assert final_state["current_phase"] == "publication_ready"
    assert final_state["research"] is not None
    assert final_state["direction"] is not None
    assert final_state["proposal"] is not None
    assert final_state["audit"] is not None
    assert final_state["package"] is not None
    
    # Check if specific mocked values are present
    assert final_state["research"].confidence_score == 0.85
    assert len(final_state["direction"].core_concept) > 0
    assert len(final_state["direction"].aesthetic_mood) > 0  # Preenchido pelo Art Director
    assert final_state["audit"].status == AuditStatus.APPROVED
    assert len(final_state.get("audit_events", [])) > 0


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


def test_guardian_policy_approved_routes_to_human():
    """Verifica que APPROVED roteia para human_approval."""
    audit = BrandAuditReport(
        status=AuditStatus.APPROVED,
        evaluated_rules=["Test rule"],
        violations=[],
        severity="None",
        justification="All good.",
        audit_context="Test",
        recommendations=[]
    )
    
    state = _make_initial_state()
    state["audit"] = audit
    
    next_node = GuardianDecisionPolicy.route(state)
    assert next_node == "agent_human_approval"


def test_guardian_policy_rejected_routes_to_designer():
    """Verifica que REJECTED (com revisões restantes) roteia para designer."""
    audit = BrandAuditReport(
        status=AuditStatus.REJECTED,
        evaluated_rules=["Test rule"],
        violations=["SaaS detected"],
        severity="Critical",
        justification="SaaS aesthetic.",
        audit_context="Test",
        recommendations=["Fix it."]
    )
    
    state = _make_initial_state()
    state["audit"] = audit
    state["revision_count"] = 1  # Abaixo do limite (3)
    
    next_node = GuardianDecisionPolicy.route(state)
    assert next_node == "agent_designer"


def test_guardian_policy_max_revisions_escalates_to_human():
    """Verifica que após MAX_REVISIONS loops, qualquer status roteia para human."""
    audit = BrandAuditReport(
        status=AuditStatus.REJECTED,
        evaluated_rules=["Test rule"],
        violations=["Persistent issue"],
        severity="Critical",
        justification="Still wrong after 3 attempts.",
        audit_context="Test",
        recommendations=["Human help needed."]
    )
    
    state = _make_initial_state()
    state["audit"] = audit
    state["revision_count"] = 3  # Atingiu o limite
    
    next_node = GuardianDecisionPolicy.route(state)
    assert next_node == "agent_human_approval"


def test_guardian_policy_human_review_required_routes_to_human():
    """Verifica que HUMAN_REVIEW_REQUIRED sempre roteia para human."""
    audit = BrandAuditReport(
        status=AuditStatus.HUMAN_REVIEW_REQUIRED,
        evaluated_rules=["Fail-secure"],
        violations=["Technical failure"],
        severity="Critical",
        justification="Fail-secure triggered.",
        audit_context="Test",
        recommendations=["Manual review needed."]
    )
    
    state = _make_initial_state()
    state["audit"] = audit
    state["revision_count"] = 0
    
    next_node = GuardianDecisionPolicy.route(state)
    assert next_node == "agent_human_approval"


def test_guardian_policy_approved_with_changes_routes_to_designer():
    """Verifica que APPROVED_WITH_CHANGES roteia para designer quando há revisões restantes."""
    audit = BrandAuditReport(
        status=AuditStatus.APPROVED_WITH_CHANGES,
        evaluated_rules=["Test rule"],
        violations=["Minor texture issue"],
        severity="Medium",
        justification="Almost there.",
        audit_context="Test",
        recommendations=["Add texture."]
    )
    
    state = _make_initial_state()
    state["audit"] = audit
    state["revision_count"] = 0
    
    next_node = GuardianDecisionPolicy.route(state)
    assert next_node == "agent_designer"
