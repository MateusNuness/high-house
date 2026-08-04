from eos.domain.contracts.visual_proposal import VisualProposal
from eos.domain.contracts.rendered_code import RenderedCode

class MockCoderAgent:
    def run(self, proposal: VisualProposal) -> RenderedCode:
        return RenderedCode(
            html_content="""
            <article class="hh-container hh-grid">
                <h1 class="hh-title-brutalist">Caos Organizado</h1>
                <p class="hh-body-text">O peso e a textura urbana importam.</p>
            </article>
            """,
            css_tokens_used=["hh-container", "hh-grid", "hh-title-brutalist", "hh-body-text"],
            notes="Mocked output based on visual proposal."
        )
