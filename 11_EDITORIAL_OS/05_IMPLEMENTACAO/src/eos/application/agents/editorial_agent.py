import json
from langchain_core.messages import SystemMessage, HumanMessage
from eos.domain.contracts.research_report import ResearchReport
from eos.domain.contracts.creative_direction import CreativeDirection
from eos.infrastructure.llm_router import ModelRouter, AgentRole
from eos.infrastructure.context_loader import MarkdownContextLoader

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
        self.llm = ModelRouter.get_model_for_role(AgentRole.EDITORIAL)
        
    def run(self, report: ResearchReport) -> CreativeDirection:
        """
        Executa a síntese editorial com base no relatório de pesquisa e retorna a direção criativa estruturada.
        """
        human_msg = f"""
        Research Sources: {', '.join(report.sources) if report.sources else 'None'}
        Cultural Hypotheses: {'; '.join(report.cultural_hypotheses) if report.cultural_hypotheses else 'None'}
        Key Findings: {'; '.join(report.key_findings) if report.key_findings else 'None'}
        Confidence Score: {report.confidence_score}
        """
        
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=human_msg)
        ]
        
        response = self.llm.invoke(messages)
        
        try:
            if hasattr(response, 'content') and "{" in response.content:
                content = response.content
                json_str = content[content.find("{"):content.rfind("}")+1]
                data = json.loads(json_str)
                return CreativeDirection(**data)
            elif isinstance(response, dict):
                return CreativeDirection(**response)
            elif isinstance(response, CreativeDirection):
                return response
        except Exception:
            pass
            
        # Fallback de segurança para mock/desenvolvimento ou LLM genérico
        primary_finding = report.key_findings[0] if report.key_findings else "Expressão urbana underground"
        return CreativeDirection(
            core_concept=f"Intervenção e sofisticação silenciosa: {primary_finding}",
            editorial_intent="Narrativa madura e autoral, observando a tensão urbana sem retórica apelativa de marketing.",
            aesthetic_mood="Caos organizado com textura brutalista e tipografia contida.",
            references=report.sources if report.sources else ["https://highhouse.estudio/editorial-manifesto"]
        )
