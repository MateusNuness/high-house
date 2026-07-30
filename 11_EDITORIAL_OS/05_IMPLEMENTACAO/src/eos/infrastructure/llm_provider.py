import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

def get_llm(role: str) -> ChatOpenAI:
    """
    Returns the appropriate LLM instance based on the agent's role.
    This acts as the LLM Router for the EOS architecture.
    """
    base_url = os.environ.get("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
    api_key = os.environ.get("DEEPSEEK_API_KEY", "")
    
    pro_model = os.environ.get("DEFAULT_REASONING_MODEL", "deepseek-v4-pro")
    flash_model = os.environ.get("FAST_MODEL", "deepseek-v4-flash")
    
    # Roles that require high reasoning effort
    reasoning_roles = [
        "research",
        "editorial",
        "art_director",
        "critic",
        "brand_guardian"
    ]
    
    if role in reasoning_roles:
        # Use deepseek-v4-pro with thinking mode and high reasoning effort
        return ChatOpenAI(
            model=pro_model,
            api_key=api_key,
            base_url=base_url,
            model_kwargs={"reasoning_effort": "high"}
        )
    else:
        # Default to flash model for fast/validation tasks
        return ChatOpenAI(
            model=flash_model,
            api_key=api_key,
            base_url=base_url
        )
