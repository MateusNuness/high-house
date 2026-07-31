import json
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
    
    def __init__(self):
        # Carrega o contexto dedicado de 04_AGENT_CONTEXTS/art_director_context.md
        self.system_prompt = MarkdownContextLoader.load("Art Director Agent")
        # Roteia para o modelo (usa o mesmo nível do Designer/Creation)
        self.llm = ModelRouter.get_model_for_role(AgentRole.CREATIVE)
        
    def run(self, direction: CreativeDirection) -> CreativeDirection:
        """
        Analisa a intenção editorial e define as restrições visuais.
        """
        human_msg = f"""
        Core Concept: {direction.core_concept}
        Editorial Intent: {direction.editorial_intent}
        
        Sua tarefa é expandir esta direção definindo o `aesthetic_mood` (técnica visual, 
        iluminação, paleta de acentos, materialidade tátil) e as `references` ideais 
        para este conceito, retornando o objeto JSON atualizado.
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
                # Mantém as definições editoriais originais caso o LLM omita
                if "core_concept" not in data or not data["core_concept"]:
                    data["core_concept"] = direction.core_concept
                if "editorial_intent" not in data or not data["editorial_intent"]:
                    data["editorial_intent"] = direction.editorial_intent
                return CreativeDirection(**data)
            elif isinstance(response, dict):
                return CreativeDirection(**response)
        except Exception:
            pass
            
        # Fallback Fail-safe (padrão de segurança do sistema)
        return CreativeDirection(
            core_concept=direction.core_concept,
            editorial_intent=direction.editorial_intent,
            aesthetic_mood="Luz dura, textura de concreto e preto absoluto. Sem acentos vibrantes.",
            references=direction.references if direction.references else ["Fotografia documental preto e branco, brutalismo paulista"]
        )
