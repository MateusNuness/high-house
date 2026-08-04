import json
from langchain_core.messages import SystemMessage, HumanMessage
from eos.domain.contracts.visual_proposal import VisualProposal
from eos.domain.contracts.rendered_code import RenderedCode
from eos.infrastructure.llm_router import ModelRouter, AgentRole
from eos.infrastructure.context_loader import MarkdownContextLoader

class CoderAgent:
    """
    Agente Coder do EOS (EOS-011).
    Responsável por transformar a Proposta Visual em código HTML estrito,
    utilizando apenas o tokens.css e obedecendo o purismo editorial.
    """
    
    def __init__(self):
        self.system_prompt = MarkdownContextLoader.load("Coder Agent")
        self.llm = ModelRouter.get_model_for_role(AgentRole.CODER)
        
    def run(self, proposal: VisualProposal) -> RenderedCode:
        human_msg = f"""
        Visual Proposal:
        {proposal.grid_structure}
        
        Constraints: No inline CSS, no frameworks. Use ONLY tokens.css abstractions.
        """
        
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=human_msg)
        ]
        
        # Simulamos a extração de código (a lógica de parsing pode ser mais robusta)
        response = self.llm.invoke(messages)
        
        # Fallback de segurança temporário (até plugar um parser mais complexo)
        return RenderedCode(
            html_content="<article class='high-article'><h1>Title</h1></article>",
            css_tokens_used=["high-article"],
            notes="Basic markup generated."
        )
