from eos.domain.contracts.research_report import ResearchReport
from eos.domain.contracts.creative_direction import CreativeDirection

class MockEditorialAgent:
    """
    Agente Mock Editorial para testes de integração e execução offline/CI sem dependência de LLM ao vivo.
    """
    
    def run(self, report: ResearchReport) -> CreativeDirection:
        topic_summary = report.key_findings[0] if report.key_findings else "Intervenção urbana"
        return CreativeDirection(
            core_concept=f"Arquitetura da resistência urbana: {topic_summary}",
            editorial_intent="Documentação observadora e autoral sobre a apropriação dos espaços urbanos, com tom contido e silenciosa sofisticação.",
            aesthetic_mood="Caos organizado, tipografia estruturada sob grid brutalista e paleta monocromática de alta tensão.",
            references=report.sources if report.sources else ["https://highhouse.estudio/references/01"]
        )
