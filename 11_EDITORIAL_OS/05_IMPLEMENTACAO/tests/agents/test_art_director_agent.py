import pytest
from unittest.mock import patch, MagicMock
from eos.application.agents.art_director_agent import ArtDirectorAgent
from eos.domain.contracts.creative_direction import CreativeDirection

def _make_base_direction():
    return CreativeDirection(
        core_concept="Urban tension and decay",
        editorial_intent="A sophisticated critique of modern isolation",
        aesthetic_mood="",
        references=[]
    )

@patch("eos.application.agents.art_director_agent.ModelRouter.get_model_for_role")
def test_art_director_context_loading(mock_get_model):
    """Testa se o agente carrega o contexto do Art Director corretamente."""
    mock_llm = MagicMock()
    mock_get_model.return_value = mock_llm
    
    agent = ArtDirectorAgent()
    assert "Art Director Agent" in agent.system_prompt
    assert "Restrição de Acento" in agent.system_prompt

@patch("eos.application.agents.art_director_agent.ModelRouter.get_model_for_role")
def test_art_director_contract_output(mock_get_model):
    """Testa se o agente retorna o contrato esperado (CreativeDirection enriquecida)."""
    mock_llm = MagicMock()
    mock_llm.with_structured_output.return_value = mock_llm
    mock_llm.invoke.return_value = CreativeDirection(
        core_concept="Urban tension", 
        editorial_intent="Critique", 
        aesthetic_mood="Dark and brutal", 
        references=["Brutalism"]
    )
    mock_get_model.return_value = mock_llm
    
    agent = ArtDirectorAgent()
    base_direction = _make_base_direction()
    result = agent.run(base_direction)
    
    assert isinstance(result, CreativeDirection)
    assert result.aesthetic_mood == "Dark and brutal"
    assert "Brutalism" in result.references

@patch("eos.application.agents.art_director_agent.ModelRouter.get_model_for_role")
def test_art_director_fail_secure(mock_get_model):
    """Testa se o agente cai no fallback determinístico em caso de falha."""
    mock_llm = MagicMock()
    mock_llm.with_structured_output.return_value = mock_llm
    # Simulando um erro
    mock_llm.invoke.side_effect = Exception("Parsing error")
    mock_get_model.return_value = mock_llm
    
    agent = ArtDirectorAgent()
    base_direction = _make_base_direction()
    result = agent.run(base_direction)
    
    assert isinstance(result, CreativeDirection)
    assert "Luz dura" in result.aesthetic_mood
    assert result.core_concept == "Urban tension and decay"  # Preserva os dados originais
