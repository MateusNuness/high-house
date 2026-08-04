import pytest
from unittest.mock import patch, MagicMock
from eos.application.agents.designer_agent import DesignerAgent
from eos.domain.contracts.creative_direction import CreativeDirection
from eos.domain.contracts.visual_proposal import VisualProposal

def _make_direction():
    return CreativeDirection(
        core_concept="Urban tension",
        editorial_intent="Critique",
        aesthetic_mood="Dark and brutal, concrete texture",
        references=["Brutalism"]
    )

@patch("eos.application.agents.designer_agent.ModelRouter.get_model_for_role")
def test_designer_context_loading(mock_get_model):
    """Testa se o agente carrega o contexto do Designer corretamente."""
    mock_llm = MagicMock()
    mock_get_model.return_value = mock_llm
    
    agent = DesignerAgent()
    assert "Designer Agent" in agent.system_prompt
    assert "Contraste Extremo" in agent.system_prompt
    assert "Horror ao Preenchimento" in agent.system_prompt

@patch("eos.application.agents.designer_agent.ModelRouter.get_model_for_role")
def test_designer_contract_output(mock_get_model):
    """Testa se o agente retorna o contrato esperado (VisualProposal)."""
    mock_llm = MagicMock()
    mock_llm.with_structured_output.return_value = mock_llm
    mock_llm.invoke.return_value = VisualProposal(
        grid_structure="Heavy asymmetric grid",
        visual_elements=["Block quotes"],
        color_palette=["#000000", "#FFFFFF"],
        typography_spec="Space Grotesk primary",
        generation_prompt="None",
        implementation_notes="Use extreme padding"
    )
    mock_get_model.return_value = mock_llm
    
    agent = DesignerAgent()
    result = agent.run(_make_direction())
    
    assert isinstance(result, VisualProposal)
    assert result.grid_structure == "Heavy asymmetric grid"
    assert "Space Grotesk" in result.typography_spec

@patch("eos.application.agents.designer_agent.ModelRouter.get_model_for_role")
def test_designer_fail_secure(mock_get_model):
    """Testa se o agente cai no fallback determinístico em caso de falha de parsing."""
    mock_llm = MagicMock()
    mock_llm.with_structured_output.return_value = mock_llm
    mock_llm.invoke.side_effect = Exception("Parsing Error")
    mock_get_model.return_value = mock_llm
    
    agent = DesignerAgent()
    result = agent.run(_make_direction())
    
    assert isinstance(result, VisualProposal)
    assert "Asymmetric grid with heavy negative space" in result.grid_structure
