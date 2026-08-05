from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class PosterSummary:
    topic: str
    caption: str
    aesthetic_mood: str
    core_concept: str

class CollectionHistory:
    """
    Encapsula o estado e o histórico de pôsteres gerados em uma coleção.
    Responsável por formatar os contextos para garantir continuidade narrativa
    e contraste estético.
    """
    def __init__(self):
        self.posters: List[PosterSummary] = []
        
    def add_poster(self, topic: str, caption: str, aesthetic_mood: str, core_concept: str):
        self.posters.append(PosterSummary(topic, caption, aesthetic_mood, core_concept))

    def get_narrative_context(self) -> str:
        if not self.posters:
            return ""
        
        history_context = "\nContexto Narrativo Anterior da Coleção (Pôsteres já gerados):\n"
        for i, p in enumerate(self.posters):
            history_context += f"Pôster {i+1} - Tópico: {p.topic}\n"
            history_context += f"Caption: {p.caption}\n"
            history_context += f"Core Concept: {p.core_concept}\n\n"
        history_context += "Instrução: Considere o contexto narrativo acima para garantir continuidade. A caption deste novo pôster deve soar como o próximo capítulo ou continuação natural, mantendo coesão e progressão em relação aos pôsteres anteriores."
        
        return history_context

    def get_contrast_context(self) -> str:
        if not self.posters:
            return ""
        
        contrast_context = "\nHistórico Visual da Coleção (Pôsteres já gerados):\n"
        for i, p in enumerate(self.posters):
            contrast_context += f"Pôster {i+1} - Tópico: {p.topic}\n"
            contrast_context += f"Aesthetic Mood: {p.aesthetic_mood}\n\n"
        contrast_context += "Instrução: Analise o 'Aesthetic Mood' dos pôsteres anteriores e crie uma nova atmosfera visual que garanta **contraste deliberado** (ex: se o anterior foi clean/minimalista, este pode ser mais brutalista, ruidoso ou com luz mais dramática). O objetivo é não repetir a mesma estética consecutivamente."
        
        return contrast_context
        
    def to_list(self) -> List[Dict[str, Any]]:
        return [
            {
                "topic": p.topic,
                "caption": p.caption,
                "aesthetic_mood": p.aesthetic_mood,
                "core_concept": p.core_concept
            }
            for p in self.posters
        ]

    @classmethod
    def from_list(cls, poster_dicts: List[Dict[str, Any]]):
        history = cls()
        for p in poster_dicts:
            history.add_poster(
                topic=p.get("topic", ""),
                caption=p.get("caption", ""),
                aesthetic_mood=p.get("aesthetic_mood", ""),
                core_concept=p.get("core_concept", "")
            )
        return history
