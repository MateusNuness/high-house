from langchain_core.messages import SystemMessage, HumanMessage
from eos.domain.contracts.editorial_brief import EditorialBrief
from eos.domain.contracts.research_report import ResearchReport
from eos.infrastructure.llm_router import ModelRouter, AgentRole
from eos.infrastructure.context_loader import MarkdownContextLoader
import json

class ResearchAgent:
    """
    Agente de Pesquisa do EOS.
    Responsável por investigar profundamente temas culturais com base em um EditorialBrief.
    """
    
    def __init__(self):
        # Carrega o contexto (System Prompt) direto da especificação mestre
        self.system_prompt = MarkdownContextLoader.load("Research Agent")
        # Roteia para o modelo de pesquisa (ex: DeepSeek)
        self.llm = ModelRouter.get_model_for_role(AgentRole.RESEARCH)
        
    def run(self, brief: EditorialBrief) -> ResearchReport:
        """
        Executa a pesquisa com base no brief e retorna o relatório estruturado.
        """
        # Em uma implementação real do LangChain com suporte a structured output:
        # structured_llm = self.llm.with_structured_output(ResearchReport)
        
        # Como estamos simulando/iniciando, construímos a mensagem.
        human_msg = f"""
        Topic: {brief.topic}
        Objective: {brief.objective}
        Constraints: {', '.join(brief.constraints) if brief.constraints else 'None'}
        """
        
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=human_msg)
        ]
        
        # Chamada ao modelo (no MVP, pode retornar um mock string ou um dict json formatado)
        response = self.llm.invoke(messages)
        
        # Para compatibilidade com o mock do llm_router que retorna strings simples, 
        # ou caso o llm suporte structured output. 
        # Aqui, vamos assumir que o LLM retorna JSON no nosso setup real,
        # Mas como temos o MockLLM no router agora, fazemos um fallback caso falhe.
        
        try:
            # Em um cenário real com structured output, a resposta já seria o BaseModel,
            # ou um JSON que podemos fazer parse.
            if hasattr(response, 'content') and "{" in response.content:
                # Tenta parsear o JSON se vier em texto
                content = response.content
                # Simples extract de json:
                json_str = content[content.find("{"):content.rfind("}")+1]
                data = json.loads(json_str)
                return ResearchReport(**data)
            elif isinstance(response, dict):
                return ResearchReport(**response)
            elif isinstance(response, ResearchReport):
                return response
        except Exception:
            pass
            
        # Fallback de segurança caso a resposta não seja parseável ou seja o Mock string
        return ResearchReport(
            sources=["Falha no parser ou mock"],
            cultural_hypotheses=["O agente não retornou JSON válido"],
            key_findings=["Verificar implementação do Structured Output no LLM", str(response.content) if hasattr(response, 'content') else str(response)],
            confidence_score=0.0
        )
