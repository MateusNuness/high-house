from eos.domain.contracts.visual_proposal import VisualProposal
from eos.domain.contracts.image_asset import ImageAsset
from eos.infrastructure.llm_router import ModelRouter, AgentRole
from eos.infrastructure.context_loader import MarkdownContextLoader
from langchain_core.messages import SystemMessage, HumanMessage

class ImageAgent:
    """
    Agente responsável por injetar a lente fotográfica "Analógica Documental"
    na Proposta Visual e orquestrar a geração/busca da imagem de fundo (Camada 1).
    """

    def __init__(self):
        self.system_prompt = MarkdownContextLoader.load("Image Agent")
        # Usamos o LLM primário para "traduzir" o generation_prompt do Designer 
        # para a lente analógica bruta da High House antes de enviar pro Midjourney/DALL-E.
        self.llm = ModelRouter.get_model_for_role(AgentRole.IMAGE)
        
    def run(self, proposal: VisualProposal) -> ImageAsset:
        human_msg = f"""
        Visual Proposal Abstract Prompt:
        {proposal.generation_prompt}
        
        Converta essa ideia em um prompt de Fotografia Analógica estrito conforme as suas regras.
        """
        
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=human_msg)
        ]
        
        # Simula o LLM refinando o prompt e, em seguida, uma API de imagem retornando a URL.
        # Em produção real, este agente bate na API do DALL-E/Midjourney.
        refined_prompt_response = self.llm.invoke(messages)
        
        # Placeholder estático para desenvolvimento
        return ImageAsset(
            image_url="https://images.unsplash.com/photo-1616422285623-146698dc96a5?q=80&w=1080&auto=format&fit=crop",
            generation_prompt_used=f"Refined Analog Prompt based on: {proposal.generation_prompt}",
            alt_text="Textura urbana fotográfica com granulação analógica",
            metadata={"engine": "simulated", "style": "analog"}
        )
