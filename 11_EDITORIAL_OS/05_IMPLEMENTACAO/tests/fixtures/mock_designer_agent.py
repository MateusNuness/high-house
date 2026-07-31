from eos.domain.contracts.creative_direction import CreativeDirection
from eos.domain.contracts.visual_proposal import VisualProposal

class MockDesignerAgent:
    def run(self, direction: CreativeDirection) -> VisualProposal:
        return VisualProposal(
            grid_structure="Asymmetric brutalist grid",
            visual_elements=["Halftone textures", "Distorted typography"],
            color_palette=["#000000", "#FFFFFF", "#FF0033"],
            typography_spec="Space Grotesk primary, custom distortion secondary",
            generation_prompt="A gritty urban scene with high contrast and noise",
            implementation_notes="Apply noise filter overlay at 15% opacity"
        )
