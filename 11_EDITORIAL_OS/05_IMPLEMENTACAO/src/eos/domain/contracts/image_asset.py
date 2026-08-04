from typing import Dict, Any, Optional
from pydantic import BaseModel, Field

class ImageAsset(BaseModel):
    """
    Representa a Imagem/Textura Base (Camada 1) gerada pelo Image Agent (EOS-007).
    """
    image_url: str = Field(..., description="Caminho local ou URL da imagem gerada.")
    generation_prompt_used: str = Field(..., description="O prompt analógico injetado para a geração.")
    alt_text: str = Field(..., description="Texto alternativo focado em acessibilidade.")
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Dados extras (engine, seed, etc).")
