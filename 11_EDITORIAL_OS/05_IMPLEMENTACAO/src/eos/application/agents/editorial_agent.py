import json
from langchain_core.messages import SystemMessage, HumanMessage
from eos.domain.contracts.research_report import ResearchReport
from eos.domain.contracts.creative_direction import CreativeDirection
from eos.infrastructure.llm_router import AgentRole
from eos.infrastructure.context_loader import MarkdownContextLoader
from eos.infrastructure.structured_llm_adapter import StructuredLLMAdapter

class EditorialAgent:
    """
    Agente Editorial do EOS (EOS-005).
    Responsável por transformar o ResearchReport numa Direção Criativa (CreativeDirection)
    sofisticada, autoral e com o tom de voz da High House.
    """
    
    def __init__(self):
        # Carrega o contexto (System Prompt) direto da especificação mestre (04_AGENT_SPECIFICATIONS.md)
        self.system_prompt = MarkdownContextLoader.load("Editorial Agent")
        # Roteia para o modelo do papel EDITORIAL
        self.adapter = StructuredLLMAdapter(AgentRole.EDITORIAL)
        
    def run(self, report: ResearchReport, previous_posters: list[dict] | None = None) -> CreativeDirection:
        """
        Executa a síntese editorial com base no relatório de pesquisa e retorna a direção criativa estruturada.
        """
        history_context = ""
        if previous_posters:
            history_context = "\nContexto Narrativo Anterior da Coleção (Pôsteres já gerados):\n"
            for i, p in enumerate(previous_posters):
                history_context += f"Pôster {i+1} - Tópico: {p.get('topic')}\n"
                history_context += f"Caption: {p.get('caption')}\n"
                history_context += f"Core Concept: {p.get('core_concept')}\n\n"
            history_context += "Instrução: Considere o contexto narrativo acima para garantir continuidade. A caption deste novo pôster deve soar como o próximo capítulo ou continuação natural, mantendo coesão e progressão em relação aos pôsteres anteriores."

        human_msg = f"""
        Research Sources: {', '.join(report.sources) if report.sources else 'None'}
        Cultural Hypotheses: {'; '.join(report.cultural_hypotheses) if report.cultural_hypotheses else 'None'}
        Key Findings: {'; '.join(report.key_findings) if report.key_findings else 'None'}
        Confidence Score: {report.confidence_score}
        {history_context}
        """
        
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=human_msg)
        ]
        
        primary_finding = report.key_findings[0] if report.key_findings else "Expressão urbana underground"
        fallback = CreativeDirection(
            core_concept=f"Intervenção e sofisticação silenciosa: {primary_finding}",
            editorial_intent="Narrativa madura e autoral, observando a tensão urbana sem retórica apelativa de marketing.",
            aesthetic_mood="Caos organizado com textura brutalista e tipografia contida.",
            references=report.sources if report.sources else ["https://highhouse.estudio/editorial-manifesto"]
        )
        
        return self.adapter.invoke(messages, CreativeDirection, fallback)
