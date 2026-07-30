from typing import Any

class MemoryAgentStub:
    """
    Stub for the Memory Agent (EOS-010).
    Current responsibility in this phase:
    - Register events
    - Save decision logs
    - Prepare future interfaces for Knowledge Graph and Experiment Memory
    """
    def __init__(self):
        self.events_log: list[dict[str, Any]] = []
        self.decision_logs: list[dict[str, Any]] = []
        
    def log_event(self, event_type: str, details: dict[str, Any]) -> None:
        """Register an event in the memory layer."""
        self.events_log.append({
            "type": event_type,
            "details": details
        })
        
    def save_decision(self, agent_role: str, decision: str, context: dict[str, Any]) -> None:
        """Save a decision log."""
        self.decision_logs.append({
            "agent_role": agent_role,
            "decision": decision,
            "context": context
        })
