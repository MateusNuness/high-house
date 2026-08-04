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
        structured_llm = self.llm.with_structured_output(ResearchReport)
        
        human_msg = f"""
        Topic: {brief.topic}
        Objective: {brief.objective}
        Constraints: {', '.join(brief.constraints) if brief.constraints else 'None'}
        """
        
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=human_msg)
        ]
        
        try:
            response = structured_llm.invoke(messages)
            if isinstance(response, ResearchReport):
                return response
            elif isinstance(response, dict):
                return ResearchReport(**response)
        except Exception as e:
            pass
            
        # Fallback de segurança caso a resposta não seja parseável
        return ResearchReport(
            sources=["Falha no parser ou mock"],
            cultural_hypotheses=["O agente não retornou JSON válido"],
            key_findings=["Verificar implementação do Structured Output no LLM"],
            confidence_score=0.0
        )
