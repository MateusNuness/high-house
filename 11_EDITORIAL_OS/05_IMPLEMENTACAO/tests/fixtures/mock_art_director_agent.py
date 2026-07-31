from eos.domain.contracts.creative_direction import CreativeDirection

class MockArtDirectorAgent:
    def run(self, direction: CreativeDirection) -> CreativeDirection:
        return CreativeDirection(
            core_concept=direction.core_concept,
            editorial_intent=direction.editorial_intent,
            aesthetic_mood="Luz dura, textura de concreto e contraste absoluto.",
            references=["Mock Photographer", "Mock Architect"]
        )
