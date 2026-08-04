from eos.domain.contracts.visual_proposal import VisualProposal
from eos.domain.contracts.image_asset import ImageAsset

class MockImageAgent:
    def run(self, proposal: VisualProposal) -> ImageAsset:
        return ImageAsset(
            image_url="https://images.unsplash.com/mock-street-texture.jpg",
            generation_prompt_used="shot on 35mm film, concrete texture, harsh flash",
            alt_text="Mock de textura urbana para testes do pipeline",
            metadata={"mocked": True}
        )
