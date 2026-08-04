import json
from langchain_core.messages import SystemMessage, HumanMessage
from eos.domain.contracts.creative_direction import CreativeDirection
from eos.domain.contracts.visual_proposal import VisualProposal
from eos.infrastructure.llm_router import AgentRole
from eos.infrastructure.context_loader import MarkdownContextLoader
from eos.infrastructure.structured_llm_adapter import StructuredLLMAdapter

class DesignerAgent:
    """
    Designer Agent do EOS (EOS-006).
    Recebe a CreativeDirection enriquecida (do Art Director) e gera um 
    VisualProposal (Blueprint) ditando grids, hierarquia e proporções espaciais.
    """
    
    def __init__(self):
        # Carrega o contexto dedicado de 04_AGENT_CONTEXTS/designer_context.md
        self.system_prompt = MarkdownContextLoader.load("Designer Agent")
        # Roteia para o modelo
        self.adapter = StructuredLLMAdapter(AgentRole.CREATIVE)
        
    def run(self, direction: CreativeDirection) -> VisualProposal:
        """
        Gera a estrutura visual/blueprint baseada na direção criativa.
        """
        human_msg = f"""
        Core Concept: {direction.core_concept}
        Aesthetic Mood: {direction.aesthetic_mood}
        References: {', '.join(direction.references)}
        
        Sua tarefa é traduzir isso em matemática espacial e regras rígidas (Blueprint).
        Retorne estritamente um JSON correspondente ao contrato VisualProposal.
        """
        
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=human_msg)
        ]
        
        fallback = VisualProposal(
            grid_structure="Asymmetric grid with heavy negative space",
            visual_elements=["High contrast text blocks", "Monochrome borders"],
            color_palette=["#000000", "#F5F5F5"],
            typography_spec="Space Grotesk 8xl for headlines, Inter for body",
            generation_prompt="High contrast black and white abstract texture",
            implementation_notes="Ensure 10vw padding on left side. Horror ao preenchimento."
        )
        
        return self.adapter.invoke(messages, VisualProposal, fallback)
