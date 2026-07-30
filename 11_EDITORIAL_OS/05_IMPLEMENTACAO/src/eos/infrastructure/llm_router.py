"""
LLM Provider Abstraction & Routing.
Allows routing to different models depending on the agent's role (e.g., DeepSeek for reasoning, OpenAI for fast tasks).
"""
import os
from enum import Enum
from langchain_core.language_models import BaseChatModel

# We would import actual Langchain Chat classes here, but for MVP we mock it.
# from langchain_openai import ChatOpenAI
# from langchain_community.chat_models import ChatDeepSeek

class AgentRole(str, Enum):
    CREATIVE = "creative"
    VALIDATOR = "validator"
    REASONING = "reasoning"
    RESEARCH = "research"

class ModelRouter:
    """
    Factory to return the correct LangChain LLM instance based on the agent's required capabilities.
    """
    @staticmethod
    def get_model_for_role(role: AgentRole) -> BaseChatModel:
        """
        Returns a configured LLM for the given role.
        In this MVP, we return a mock or a generic model setup.
        """
        # Mocking the LLM instantiation for the MVP
        class MockLLM(BaseChatModel):
            def _generate(self, messages, stop=None, run_manager=None, **kwargs):
                from langchain_core.messages import AIMessage
                from langchain_core.outputs import ChatResult, ChatGeneration
                
                msg = AIMessage(content=f"[Mocked LLM Response for {role}]")
                return ChatResult(generations=[ChatGeneration(message=msg)])
            
            @property
            def _llm_type(self) -> str:
                return "mock_llm"
        
        return MockLLM()
