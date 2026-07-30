"""
LangGraph Orchestrator MVP.
This module validates the DAG architecture, state transition, and checkpointing
using a dummy agent. It does not contain real High House logic.
"""
from langgraph.graph import StateGraph, START, END
from eos.domain.state import EOSGlobalState
from eos.infrastructure.telemetry import get_logger

logger = get_logger("orchestrator")

def dummy_node(state: EOSGlobalState) -> dict:
    """
    A dummy node representing an agent to test the architecture plumbing.
    """
    logger.info("Executing dummy node", current_phase=state.get("current_phase"))
    
    # Simulate processing and state update
    new_message = {"role": "agent", "content": "Dummy processing completed."}
    
    return {
        "messages": [new_message],
        "is_approved": True,
        "final_artifact": "[MOCKED ARTIFACT]"
    }

def create_mvp_graph():
    """
    Builds and compiles the minimal LangGraph to prove the infrastructure works.
    """
    # Initialize the graph with our strongly typed state
    workflow = StateGraph(EOSGlobalState)
    
    # Add nodes
    workflow.add_node("dummy_agent", dummy_node)
    
    # Define edges (The DAG)
    workflow.add_edge(START, "dummy_agent")
    workflow.add_edge("dummy_agent", END)
    
    # Compile the graph
    # Note: Checkpointer is passed during execution or compilation depending on usage.
    return workflow.compile()
