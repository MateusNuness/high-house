from eos.domain.contracts.visual_proposal import VisualProposal
from eos.domain.contracts.image_asset import ImageAsset
from eos.infrastructure.llm_router import ModelRouter, AgentRole
from eos.infrastructure.context_loader import MarkdownContextLoader
from langchain_core.messages import SystemMessage, HumanMessage

import json

class ImageAgent:
    """
    Agente responsável por injetar a lente fotográfica "Analógica Documental"
    na Proposta Visual e orquestrar a geração/busca da imagem de fundo (Camada 1).
    """

    def __init__(self):
        self.system_prompt = MarkdownContextLoader.load("Image Agent")
        self.llm = ModelRouter.get_model_for_role(AgentRole.IMAGE)
        
    def run(self, proposal: VisualProposal) -> ImageAsset:
        human_msg = f"""
        Visual Proposal Abstract Prompt:
        {proposal.generation_prompt}
        
        Converta essa ideia em um prompt de Fotografia Analógica estrito conforme as suas regras.
        Retorne um JSON estrito correspondente ao contrato ImageAsset contendo 'image_url', 'generation_prompt_used', 'alt_text' e 'metadata'.
        Use 'https://images.unsplash.com/photo-1616422285623-146698dc96a5?q=80&w=1080&auto=format&fit=crop' como image_url provisória.
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
                return ImageAsset(**data)
            elif isinstance(response, dict):
                return ImageAsset(**response)
        except Exception:
            pass
            
        return ImageAsset(
            image_url="https://images.unsplash.com/photo-1616422285623-146698dc96a5?q=80&w=1080&auto=format&fit=crop",
            generation_prompt_used=f"Refined Analog Prompt based on: {proposal.generation_prompt}",
            alt_text="Textura urbana fotográfica com granulação analógica",
            metadata={"engine": "fallback", "style": "analog"}
        )
