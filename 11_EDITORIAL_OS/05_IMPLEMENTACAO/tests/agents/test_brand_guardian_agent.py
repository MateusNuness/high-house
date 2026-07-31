import json
import pytest
from pathlib import Path

from eos.domain.contracts.visual_proposal import VisualProposal
from eos.domain.contracts.creative_direction import CreativeDirection
from eos.domain.contracts.editorial_brief import EditorialBrief
from eos.domain.contracts.research_report import ResearchReport
from eos.domain.contracts.brand_audit_report import BrandAuditReport
from eos.domain.contracts.base import AuditStatus
from eos.infrastructure.context_loader import MarkdownContextLoader
from eos.application.agents.brand_guardian_agent import BrandGuardianAgent
from tests.fixtures.mock_brand_guardian_agent import MockBrandGuardianAgent


FIXTURES_DIR = Path(__file__).parent.parent / "fixtures"


def _load_fixture(name: str) -> dict:
    """Carrega uma fixture JSON."""
    with open(FIXTURES_DIR / name, "r", encoding="utf-8") as f:
        return json.load(f)


def _proposal_from_fixture(fixture: dict) -> VisualProposal:
    """Cria uma VisualProposal a partir de uma fixture."""
    return VisualProposal(**fixture["proposal"])


def _direction_from_fixture(fixture: dict) -> CreativeDirection:
    """Cria uma CreativeDirection a partir de uma fixture."""
    return CreativeDirection(**fixture["direction"])


# ─────────────────────────────────────────────────────────────────
# 1. Teste de Carregamento de Contexto (SSOT)
# ─────────────────────────────────────────────────────────────────

def test_guardian_context_loading():
    """
    Valida a carga do contexto dedicado do Brand Guardian
    a partir de 04_AGENT_CONTEXTS/brand_guardian_context.md.
    """
    prompt = MarkdownContextLoader.load("Brand Guardian Agent")
    
    # Deve conter elementos-chave do contexto dedicado
    assert "Brand Guardian" in prompt, \
        "O prompt carregado deve mencionar o Brand Guardian."
    assert "Anti-patterns" in prompt or "Rejeição" in prompt or "REJECTED" in prompt, \
        "O prompt deve carregar critérios de rejeição."
    assert "Regras Permanentes" in prompt or "fail-secure" in prompt, \
        "O prompt deve carregar as regras permanentes e fail-secure."
    assert "APPROVED" in prompt and "REJECTED" in prompt, \
        "O prompt deve definir os possíveis status de auditoria."


# ─────────────────────────────────────────────────────────────────
# 2. Teste de Rejeição: Estética SaaS (Anti-pattern §23.1)
# ─────────────────────────────────────────────────────────────────

def test_guardian_rejects_saas_aesthetic():
    """
    Entrada: VisualProposal com estética SaaS (rounded cards, cores pastéis, Nunito Sans).
    Esperado: REJECTED com violations citando §23.1.
    
    Usa fixture determinística rejected_visual.json.
    """
    mock = MockBrandGuardianAgent(scenario="rejected")
    fixture = _load_fixture("rejected_visual.json")
    
    proposal = _proposal_from_fixture(fixture)
    direction = _direction_from_fixture(fixture)
    
    report = mock.audit(proposal, direction)
    
    assert isinstance(report, BrandAuditReport)
    assert report.status == AuditStatus.REJECTED
    assert len(report.violations) > 0, "Deve listar violações específicas."
    assert any("§23.1" in v or "SaaS" in v for v in report.violations), \
        "Deve citar a regra §23.1 (Estética SaaS) nas violações."
    assert report.severity in ("High", "Critical"), \
        "Violação SaaS deve ter severidade High ou Critical."
    assert len(report.recommendations) > 0, \
        "Deve incluir recomendações de correção."


# ─────────────────────────────────────────────────────────────────
# 3. Teste de Aprovação: Estética Underground Autêntica
# ─────────────────────────────────────────────────────────────────

def test_guardian_approves_authentic_underground():
    """
    Entrada: VisualProposal com grafite, xerox, tipografia experimental, alto contraste.
    Esperado: APPROVED sem violações.
    
    Usa fixture determinística approved_visual.json.
    """
    mock = MockBrandGuardianAgent(scenario="approved")
    fixture = _load_fixture("approved_visual.json")
    
    proposal = _proposal_from_fixture(fixture)
    direction = _direction_from_fixture(fixture)
    
    report = mock.audit(proposal, direction)
    
    assert isinstance(report, BrandAuditReport)
    assert report.status == AuditStatus.APPROVED
    assert len(report.violations) == 0, "APPROVED não deve ter violações."
    assert report.severity == "None", "APPROVED deve ter severidade None."
    assert len(report.recommendations) == 0, "APPROVED não deve ter recomendações."


# ─────────────────────────────────────────────────────────────────
# 4. Teste de Rejeição: Cannabis Caricata (Anti-pattern §23.2)
# ─────────────────────────────────────────────────────────────────

def test_guardian_rejects_cannabis_caricature():
    """
    Entrada: VisualProposal com folha verde neon, cultura canábica caricata.
    Esperado: REJECTED.
    
    Usa o mock com cenário "rejected" — a fixture inclui violações de §23.2.
    Para testar especificamente cannabis, criamos a proposta manualmente e 
    verificamos que o mock retorna REJECTED.
    """
    mock = MockBrandGuardianAgent(scenario="rejected")
    
    # Proposta canábica caricata
    proposal = VisualProposal(
        grid_structure="Centered layout with cannabis leaf border",
        visual_elements=["Cartoon marijuana leaf", "Neon green smoke", "Rastafari pattern"],
        color_palette=["#00FF00", "#FFD700", "#FF0000"],
        typography_spec="Comic Sans with leaf decorations",
        generation_prompt="A psychedelic weed-themed poster with green neon glowing leaves",
        implementation_notes="Use glowing green border-shadow on all elements"
    )
    
    direction = CreativeDirection(
        core_concept="Celebração da cultura 420 com estética stoner clássica",
        editorial_intent="Marketing direto de produtos canábicos com apelo visual forte",
        aesthetic_mood="Reggae colorido com folhas de maconha e alienígenas verdes",
        references=["https://generic-headshop-template.com"]
    )
    
    report = mock.audit(proposal, direction)
    
    assert isinstance(report, BrandAuditReport)
    assert report.status == AuditStatus.REJECTED
    assert len(report.violations) > 0


# ─────────────────────────────────────────────────────────────────
# 5. Teste de Contrato de Output (Validação Pydantic)
# ─────────────────────────────────────────────────────────────────

def test_guardian_contract_output():
    """
    Valida que o output do Brand Guardian respeita o schema BrandAuditReport estrito.
    Todos os campos devem estar presentes e tipados corretamente.
    Status deve ser um AuditStatus Enum, nunca string.
    """
    mock = MockBrandGuardianAgent(scenario="approved")
    fixture = _load_fixture("approved_visual.json")
    
    proposal = _proposal_from_fixture(fixture)
    direction = _direction_from_fixture(fixture)
    
    report = mock.audit(proposal, direction)
    
    # Verificação de tipo
    assert isinstance(report, BrandAuditReport)
    
    # Verificação de todos os campos obrigatórios
    assert hasattr(report, "status")
    assert hasattr(report, "evaluated_rules")
    assert hasattr(report, "violations")
    assert hasattr(report, "severity")
    assert hasattr(report, "justification")
    assert hasattr(report, "audit_context")
    assert hasattr(report, "recommendations")
    
    # Status DEVE ser Enum, nunca string
    assert isinstance(report.status, AuditStatus), \
        f"status deve ser AuditStatus Enum, não {type(report.status)}"
    
    # Campos de lista devem ser listas
    assert isinstance(report.evaluated_rules, list)
    assert isinstance(report.violations, list)
    assert isinstance(report.recommendations, list)
    
    # Campos de string devem ser strings não-vazias
    assert isinstance(report.severity, str) and len(report.severity) > 0
    assert isinstance(report.justification, str) and len(report.justification) > 0
    assert isinstance(report.audit_context, str) and len(report.audit_context) > 0


# ─────────────────────────────────────────────────────────────────
# 6. Teste de Fail-Secure (Princípio Inegociável)
# ─────────────────────────────────────────────────────────────────

def test_guardian_fail_secure():
    """
    Verifica que o BrandGuardianAgent NUNCA retorna APPROVED por default
    quando ocorre uma falha (parsing, timeout, exceção).
    
    Testa o método _fail_secure_report diretamente.
    """
    agent = BrandGuardianAgent()
    
    # Simula falha chamando o fail-secure diretamente
    report = agent._fail_secure_report(context="Teste de fail-secure")
    
    assert isinstance(report, BrandAuditReport)
    assert report.status == AuditStatus.HUMAN_REVIEW_REQUIRED, \
        "Fail-secure DEVE retornar HUMAN_REVIEW_REQUIRED, nunca APPROVED."
    assert report.severity == "Critical", \
        "Fail-secure deve ter severidade Critical."
    assert len(report.violations) > 0, \
        "Fail-secure deve registrar a falha como violação."
    assert "fail-secure" in report.justification.lower() or "falha" in report.justification.lower(), \
        "A justificativa deve mencionar o fail-secure ou a falha."


# ─────────────────────────────────────────────────────────────────
# 7. Teste de APPROVED_WITH_CHANGES (Revisão necessária)
# ─────────────────────────────────────────────────────────────────

def test_guardian_needs_revision():
    """
    Entrada: VisualProposal com conceito correto mas materialidade insuficiente.
    Esperado: APPROVED_WITH_CHANGES com recomendações acionáveis.
    
    Usa fixture determinística needs_revision.json.
    """
    mock = MockBrandGuardianAgent(scenario="needs_revision")
    fixture = _load_fixture("needs_revision.json")
    
    proposal = _proposal_from_fixture(fixture)
    direction = _direction_from_fixture(fixture)
    
    report = mock.audit(proposal, direction)
    
    assert isinstance(report, BrandAuditReport)
    assert report.status == AuditStatus.APPROVED_WITH_CHANGES
    assert len(report.violations) > 0, "APPROVED_WITH_CHANGES deve listar problemas."
    assert len(report.recommendations) > 0, "APPROVED_WITH_CHANGES deve ter recomendações acionáveis."
    assert report.severity in ("Low", "Medium"), \
        "Revisão menor deve ter severidade Low ou Medium."
