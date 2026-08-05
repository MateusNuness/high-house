from eos.domain.contracts.editorial_brief import EditorialBrief
from eos.domain.contracts.research_report import ResearchReport
from eos.infrastructure.llm_router import AgentRole
from eos.infrastructure.context_loader import MarkdownContextLoader
from eos.infrastructure.structured_llm_adapter import StructuredLLMAdapter
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
        self.adapter = StructuredLLMAdapter(AgentRole.RESEARCH)
        
    def run(self, brief: EditorialBrief) -> ResearchReport:
        """
        Executa a pesquisa com base no brief e retorna o relatório estruturado.
        """
        human_msg = f"""
        Topic: {brief.topic}
        Objective: {brief.objective}
        Constraints: {', '.join(brief.constraints) if brief.constraints else 'None'}
        """
        
        fallback = ResearchReport(
            sources=["Falha no parser ou mock"],
            cultural_hypotheses=["O agente não retornou JSON válido"],
            key_findings=["Verificar implementação do Structured Output no LLM"],
            confidence_score=0.0
        )
        
        return self.adapter.invoke(self.system_prompt, human_msg, ResearchReport, fallback)
