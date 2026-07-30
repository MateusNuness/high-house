import pytest
from langgraph.graph import StateGraph, START, END
from eos.domain.contracts import EditorialBrief
from eos.application.workflows.editorial_creation import workflow
from eos.infrastructure.checkpoints import get_checkpointer

def test_workflow_persistence_pause_resume():
    """Test that the workflow can be paused and resumed using checkpoints."""
    
    # Compile with an interrupt before the designer agent
    checkpointer = get_checkpointer()
    test_app = workflow.compile(
        checkpointer=checkpointer,
        interrupt_before=["agent_designer"]
    )
    
    thread_id = "test-thread-persistence-002"
    config = {"configurable": {"thread_id": thread_id}}
    
    initial_brief = EditorialBrief(
        topic="Xarpi Carioca Persistence",
        objective="Test persistence",
        audience="Developers",
        cultural_context="Tech scene",
        constraints=["None"],
        source_reference="Internal test",
        created_by="Pytest"
    )
    
    initial_state = {
        "execution_id": "exec-pers-002",
        "thread_id": thread_id,
        "current_phase": "started",
        "current_agent": "system",
        "audit_log": [],
        "audit_events": [],
        "errors": [],
        "brief": initial_brief,
        "research": None,
        "direction": None,
        "proposal": None,
        "audit": None,
        "package": None
    }
    
    # Run graph until it hits the interrupt
    test_app.invoke(initial_state, config=config)
    
    # Verify the state is paused at the interrupt point (after editorial, before designer)
    saved_state = test_app.get_state(config)
    
    assert saved_state is not None
    assert saved_state.next == ('agent_designer',)
    assert saved_state.values["current_phase"] == "editorial_completed"
    assert saved_state.values["direction"] is not None
    assert saved_state.values["proposal"] is None
    
    # Resume workflow by passing None
    test_app.invoke(None, config=config)
    
    # Verify it completed
    final_saved_state = test_app.get_state(config)
    assert final_saved_state.next == ()
    assert final_saved_state.values["current_phase"] == "publication_ready"
    assert final_saved_state.values["proposal"] is not None
    assert final_saved_state.values["package"] is not None
