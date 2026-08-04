import json
from typing import Any
from langchain_core.messages import SystemMessage, HumanMessage
from eos.domain.contracts.creative_direction import CreativeDirection
from eos.infrastructure.llm_router import ModelRouter, AgentRole
from eos.infrastructure.context_loader import MarkdownContextLoader

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
        self.llm = ModelRouter.get_model_for_role(AgentRole.CREATIVE)
        
    def run(self, direction: CreativeDirection, previous_posters: list[dict[str, Any]] | None = None) -> CreativeDirection:
        """
        Analisa a intenção editorial e define as restrições visuais, buscando contraste estético.
        """
        contrast_context = ""
        if previous_posters:
            contrast_context = "\nHistórico Visual da Coleção (Pôsteres já gerados):\n"
            for i, p in enumerate(previous_posters):
                contrast_context += f"Pôster {i+1} - Tópico: {p.get('topic')}\n"
                contrast_context += f"Aesthetic Mood: {p.get('aesthetic_mood')}\n\n"
            contrast_context += "Instrução: Analise o 'Aesthetic Mood' dos pôsteres anteriores e crie uma nova atmosfera visual que garanta **contraste deliberado** (ex: se o anterior foi clean/minimalista, este pode ser mais brutalista, ruidoso ou com luz mais dramática). O objetivo é não repetir a mesma estética consecutivamente."

        human_msg = (
            f"Core Concept: {direction.core_concept}\n"
            f"Editorial Intent: {direction.editorial_intent}\n\n"
            f"Sua tarefa é expandir esta direção definindo o `aesthetic_mood` (técnica visual,\n"
            f"iluminação, paleta de acentos, materialidade tátil) e as `references` ideais\n"
            f"para este conceito, retornando o objeto JSON atualizado.\n"
            f"{contrast_context}"
        )
        
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=human_msg)
        ]
        
        structured_llm = self.llm.with_structured_output(CreativeDirection)
        
        try:
            response = structured_llm.invoke(messages)
            
            if isinstance(response, CreativeDirection):
                data = response.model_dump()
            elif isinstance(response, dict):
                data = response
            else:
                raise ValueError("Unexpected response type")
                
            # Mantém as definições editoriais originais caso o LLM omita
            if "core_concept" not in data or not data["core_concept"]:
                data["core_concept"] = direction.core_concept
            if "editorial_intent" not in data or not data["editorial_intent"]:
                data["editorial_intent"] = direction.editorial_intent
            return CreativeDirection(**data)
        except Exception:
            pass
            
        # Fallback Fail-safe (padrão de segurança do sistema)
        return CreativeDirection(
            core_concept=direction.core_concept,
            editorial_intent=direction.editorial_intent,
            aesthetic_mood="Luz dura, textura de concreto e preto absoluto. Sem acentos vibrantes.",
            references=direction.references if direction.references else ["Fotografia documental preto e branco, brutalismo paulista"]
        )
