from pydantic import BaseModel

class PublicationPackage(BaseModel):
    final_copy: str
    image_assets: list[str]
    caption: str
    metadata: dict
