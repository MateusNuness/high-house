from pydantic import BaseModel
from typing import List
from .editorial_brief import EditorialBrief

class CollectionBrief(BaseModel):
    """
    O contrato de dados que define uma Coleção inteira.
    Contém uma lista de capítulos (EditorialBrief) que serão processados em lote.
    """
    collection_id: str
    name: str
    description: str
    chapters: List[EditorialBrief]
