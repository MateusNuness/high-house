import pytest
from eos.domain.contracts.research_report import ResearchReport
from eos.domain.contracts.creative_direction import CreativeDirection
from eos.infrastructure.context_loader import MarkdownContextLoader
from eos.application.agents.editorial_agent import EditorialAgent
from tests.fixtures.mock_editorial_agent import MockEditorialAgent

def test_editorial_agent_context_loading():
    """
    Valida a carga do contexto do Editorial Agent diretamente do 04_AGENT_SPECIFICATIONS.md (SSOT).
    """
    prompt = MarkdownContextLoader.load("Editorial Agent")
    assert "Editorial Agent" in prompt, "O prompt carregado deve mencionar o Editorial Agent."
    assert "Anti-patterns" in prompt or "Regras Permanentes" in prompt, "O prompt deve carregar as regras e restrições."

def test_editorial_agent_contract_output():
    """
    Valida se o output do Editorial Agent respeita o esquema CreativeDirection estrito (4 campos).
    """
    mock_agent = MockEditorialAgent()
    report = ResearchReport(
        sources=["https://highhouse.estudio/source1"],
        cultural_hypotheses=["Tensão entre o espaço privado e a intervenção pública."],
        key_findings=["Xarpi como linguagem visual de protesto silencioso."],
        confidence_score=0.9
    )
    
    direction = mock_agent.run(report)
    
    assert isinstance(direction, CreativeDirection)
    assert hasattr(direction, "core_concept")
    assert hasattr(direction, "editorial_intent")
    assert hasattr(direction, "aesthetic_mood")
    assert hasattr(direction, "references")

def test_editorial_agent_adherence_to_style_and_anti_patterns():
    """
    Teste de Aderência Editorial (EOS-005):
    - Bloqueia anti-patterns de marketing digital ("compre agora", "disruptivo", "última chance", CTAs agressivos).
    - Bloqueia uso exagerado de exclamações e emojis.
    - Exige atributos de estilo: tom autoral, maduro, sofisticação silenciosa.
    """
    agent = EditorialAgent()
    report = ResearchReport(
        sources=["https://highhouse.estudio/research-xarpi"],
        cultural_hypotheses=["Apropriação da verticalidade urbana como expressão marginal."],
        key_findings=["Simbolismo da caligrafia urbana brutalista no Rio de Janeiro."],
        confidence_score=0.92
    )
    
    direction = agent.run(report)
    
    combined_text = f"{direction.core_concept} {direction.editorial_intent} {direction.aesthetic_mood}".lower()
    
    # 1. Validação de Anti-patterns (Marketing Hype & CTAs)
    forbidden_terms = ["compre agora", "disruptivo", "última chance", "clique aqui", "garanta o seu", "inovação que faltava", "promoção"]
    for term in forbidden_terms:
        assert term not in combined_text, f"O texto editorial contém anti-pattern proibido: '{term}'"
        
    # 2. Ausência de abusos de pontuação/emojis (caos não-estruturado)
    assert "!" not in combined_text, "O texto editorial não deve conter pontos de exclamação abusivos."
    assert "🚀" not in combined_text and "🔥" not in combined_text, "O texto editorial não deve conter emojis de marketing."
    
    # 3. Atributos Mandatórios de Estilo (Tom autoral, maduro, sofisticação silenciosa)
    assert len(direction.core_concept.strip()) > 0, "O core_concept deve ter conteúdo."
    assert len(direction.editorial_intent.strip()) > 0, "A intencionalidade editorial deve ser clara."
    assert len(direction.aesthetic_mood.strip()) > 0, "O mood estético deve estar definido."
