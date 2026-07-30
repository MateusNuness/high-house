"""
Memory Layer for LangGraph Checkpoints.
Uses SqliteSaver for operational memory (State Persistence).
"""
import sqlite3
from langgraph.checkpoint.sqlite import SqliteSaver

def get_checkpointer(db_path: str = "eos_checkpoints.sqlite3"):
    """
    Returns a configured SqliteSaver for LangGraph.
    Note: In production, the connection must be managed properly (e.g., via context manager).
    """
    conn = sqlite3.connect(db_path, check_same_thread=False)
    # The checkpointer needs to be used within a context manager where graph is executed.
    # Return the raw connection and saver wrapper helper
    return SqliteSaver(conn)

class MarkdownContextLoader:
    """
    Utility to load standard operating procedures (SOPs) from the brand's foundation.
    """
    @staticmethod
    def load_agent_spec(agent_name: str) -> str:
        """
        Mock implementation. In the future, this will read 04_AGENT_SPECIFICATIONS.md
        and parse out the specific rules for the given agent.
        """
        return f"Loaded markdown spec for {agent_name} (Mocked)"
