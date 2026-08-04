"""
LLM Provider Abstraction & Routing.
Allows routing to different models depending on the agent's role (e.g., DeepSeek for reasoning, OpenAI for fast tasks).
"""
import os
import sys

# Guard against broken PyTorch DLL on Windows when importing transformers via langchain_core
if "transformers" not in sys.modules:
    try:
        import transformers  # type: ignore # noqa
    except Exception:
        sys.modules["transformers"] = None

from enum import Enum
from langchain_core.language_models import BaseChatModel

# We would import actual Langchain Chat classes here, but for MVP we mock it.
from langchain_openai import ChatOpenAI

class AgentRole(str, Enum):
    CREATIVE = "creative"
    VALIDATOR = "validator"
    REASONING = "reasoning"
    RESEARCH = "research"
    EDITORIAL = "editorial"
    IMAGE = "image"
    CODER = "coder"
    VISION = "vision"
    BRAND_GUARDIAN = "brand_guardian"


class ModelRouter:
    """
    Factory to return the correct LangChain LLM instance based on the agent's required capabilities.
    Configurado para a API da DeepSeek.
    """
    @staticmethod
    def get_model_for_role(role: AgentRole) -> BaseChatModel:
        """
        Retorna o modelo adequado. Para a DeepSeek, usamos o ChatOpenAI apontando para a base_url deles.
        """
        api_key = os.environ.get("DEEPSEEK_API_KEY")
        if not api_key:
            raise ValueError("A variável de ambiente 'DEEPSEEK_API_KEY' não está configurada.")
            
        # Para validação e código pesados, deepseek-reasoner pode ser melhor, 
        # mas para o MVP usaremos deepseek-chat por ter melhor suporte genérico a JSON/tool calls na interface da OpenAI.
        model_name = "deepseek-chat"
        
        return ChatOpenAI(
            model=model_name,
            api_key=api_key,
            base_url="https://api.deepseek.com/v1",
            max_tokens=2048,
            temperature=0.7 if role in (AgentRole.CREATIVE, AgentRole.EDITORIAL, AgentRole.IMAGE) else 0.1
        )
