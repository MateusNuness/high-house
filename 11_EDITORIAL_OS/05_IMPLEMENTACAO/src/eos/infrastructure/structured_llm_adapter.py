from typing import TypeVar, Type
from pydantic import BaseModel
from langchain_core.messages import SystemMessage, HumanMessage
from eos.infrastructure.llm_router import ModelRouter, AgentRole

T = TypeVar('T', bound=BaseModel)

class StructuredLLMAdapter:
    """
    Adapter para padronizar as chamadas ao LLM com estruturação de dados.
    Abstrai o boilerplate do LangChain, try/except e o parse Pydantic.
    """
    def __init__(self, role: AgentRole):
        self.llm = ModelRouter.get_model_for_role(role)
        
    def invoke(self, system_prompt: str, human_prompt: str, schema: Type[T], fallback_obj: T) -> T:
        """
        Invoca o LLM exigindo uma resposta estruturada de acordo com o schema.
        Em caso de falha (de rede, parse, etc), retorna fail-secure com o fallback_obj.
        """
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=human_prompt)
        ]
        structured_llm = self.llm.with_structured_output(schema)
        
        try:
            response = structured_llm.invoke(messages)
            if isinstance(response, schema):
                return response
            elif isinstance(response, dict):
                return schema(**response)
        except Exception:
            pass
            
        return fallback_obj
