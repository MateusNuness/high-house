"""
State definition for the EOS LangGraph.
"""
from typing import TypedDict, Annotated, List, Optional
import operator

# Reducers for LangGraph state
def add_messages(left: List[dict], right: List[dict]) -> List[dict]:
    """Reducer to append new messages to the existing list."""
    return left + right

def add_audit_logs(left: List[str], right: List[str]) -> List[str]:
    """Reducer to append audit logs."""
    return left + right

class EOSGlobalState(TypedDict):
    """
    The global state flowing through the Editorial OS.
    This state is strictly transient and only holds data for the current execution.
    It does not hold rules, brand essence, or system prompts.
    """
    collection_id: str
    current_phase: str
    
    # Internal agent messages
    messages: Annotated[List[dict], add_messages]
    
    # Accumulated audit logs (e.g., from Brand Guardian or Critic)
    audit_logs: Annotated[List[str], add_audit_logs]
    
    # Final generated artifact (e.g., HTML, Markdown, or JSON)
    final_artifact: Optional[str]
    
    # Approval flag for human-in-the-loop or final gate
    is_approved: bool
