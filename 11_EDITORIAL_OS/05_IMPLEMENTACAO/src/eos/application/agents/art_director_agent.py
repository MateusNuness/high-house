import json
from typing import Any
from eos.domain.contracts.creative_direction import CreativeDirection
from eos.infrastructure.llm_router import AgentRole
from eos.infrastructure.context_loader import MarkdownContextLoader
from eos.infrastructure.structured_llm_adapter import StructuredLLMAdapter
from eos.domain.collection_history import CollectionHistory

class ArtDirectorAgent:
    """
    Art Director Agent do EOS (EOS-006).
    Recebe a CreativeDirection básica do Editorial Agent e a enriquece com as 
    restrições poéticas, materialidade dominante e técnica visual (Atmosfera Estética).
    """
    
    def __init__(self) -> None:
        # Carrega o contexto dedicado de 04_AGENT_CONTEXTS/art_director_context.md
        self.system_prompt = MarkdownContextLoader.load("Art Director Agent")
        # Roteia para o modelo (usa o mesmo nível do Designer/Creation)
        self.adapter = StructuredLLMAdapter(AgentRole.CREATIVE)
        
    def run(self, direction: CreativeDirection, history: CollectionHistory | None = None) -> CreativeDirection:
        """
        Analisa a intenção editorial e define as restrições visuais, buscando contraste estético.
        """
        contrast_context = ""
        if history:
            contrast_context = history.get_contrast_context()

        human_msg = (
            f"Core Concept: {direction.core_concept}\n"
            f"Editorial Intent: {direction.editorial_intent}\n\n"
            f"Sua tarefa é expandir esta direção definindo o `aesthetic_mood` (técnica visual,\n"
            f"iluminação, paleta de acentos, materialidade tátil) e as `references` ideais\n"
            f"para este conceito, retornando o objeto JSON atualizado.\n"
            f"{contrast_context}"
        )
        
        fallback = CreativeDirection(
            core_concept=direction.core_concept,
            editorial_intent=direction.editorial_intent,
            aesthetic_mood="Luz dura, textura de concreto e preto absoluto. Sem acentos vibrantes.",
            references=direction.references if direction.references else ["Fotografia documental preto e branco, brutalismo paulista"]
        )
        
        response = self.adapter.invoke(self.system_prompt, human_msg, CreativeDirection, fallback)
        
        # Mantém as definições editoriais originais caso o LLM omita
        if not response.core_concept:
            response.core_concept = direction.core_concept
        if not response.editorial_intent:
            response.editorial_intent = direction.editorial_intent
            
        return response
