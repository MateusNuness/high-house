import os
from unittest.mock import patch
from eos.infrastructure.llm_provider import get_llm

@patch.dict(os.environ, {
    "DEEPSEEK_API_KEY": "test-key",
    "DEEPSEEK_BASE_URL": "https://api.deepseek.com",
    "DEFAULT_REASONING_MODEL": "deepseek-v4-pro",
    "FAST_MODEL": "deepseek-v4-flash"
})
def test_llm_router_research_role():
    """Test that the research role uses the reasoning model."""
    llm = get_llm(role="research")
    
    assert llm.model_name == "deepseek-v4-pro"
    assert getattr(llm, "model_kwargs", {}).get("reasoning_effort") == "high"


@patch.dict(os.environ, {
    "DEEPSEEK_API_KEY": "test-key",
    "DEEPSEEK_BASE_URL": "https://api.deepseek.com",
    "DEFAULT_REASONING_MODEL": "deepseek-v4-pro",
    "FAST_MODEL": "deepseek-v4-flash"
})
def test_llm_router_fast_validation_role():
    """Test that the fast_validation role uses the fast model."""
    llm = get_llm(role="fast_validation")
    
    assert llm.model_name == "deepseek-v4-flash"
    assert getattr(llm, "model_kwargs", {}).get("reasoning_effort") is None
