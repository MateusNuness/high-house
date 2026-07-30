from langgraph.checkpoint.base import BaseCheckpointSaver
from langgraph.checkpoint.memory import MemorySaver

def get_checkpointer() -> BaseCheckpointSaver:
    """
    Returns the checkpointer instance for the LangGraph workflow.
    Currently uses MemorySaver, but provides an abstraction layer
    to easily swap to SqliteSaver or a Persistent Database in the future.
    """
    return MemorySaver()
