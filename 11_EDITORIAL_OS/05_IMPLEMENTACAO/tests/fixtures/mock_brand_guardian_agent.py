import json
from pathlib import Path
from eos.domain.contracts.visual_proposal import VisualProposal
from eos.domain.contracts.creative_direction import CreativeDirection
from eos.domain.contracts.editorial_brief import EditorialBrief
from eos.domain.contracts.research_report import ResearchReport
from eos.domain.contracts.brand_audit_report import BrandAuditReport
from eos.domain.contracts.base import AuditStatus


class MockBrandGuardianAgent:
    """
    Mock determinístico do Brand Guardian para testes de integração e CI.
    
    Em vez de utilizar lógica baseada em keywords (frágil), carrega fixtures JSON
    pré-definidas que representam cenários de auditoria completos e determinísticos.
    
    Uso:
        mock = MockBrandGuardianAgent(scenario="approved")
        report = mock.audit(proposal, direction)
    """
    
    FIXTURES_DIR = Path(__file__).parent
    
    SCENARIO_MAP = {
        "approved": "approved_visual.json",
        "rejected": "rejected_visual.json",
        "needs_revision": "needs_revision.json",
    }
    
    def __init__(self, scenario: str = "approved"):
        """
        Inicializa o mock com um cenário de fixture.
        
        Args:
            scenario: "approved", "rejected", ou "needs_revision"
        """
        if scenario not in self.SCENARIO_MAP:
            raise ValueError(
                f"Cenário '{scenario}' inválido. "
                f"Opções: {list(self.SCENARIO_MAP.keys())}"
            )
        self._scenario = scenario
        self._fixture = self._load_fixture(scenario)
    
    def _load_fixture(self, scenario: str) -> dict:
        """Carrega a fixture JSON do cenário."""
        fixture_path = self.FIXTURES_DIR / self.SCENARIO_MAP[scenario]
        with open(fixture_path, "r", encoding="utf-8") as f:
            return json.load(f)
    
    def audit(
        self,
        proposal: VisualProposal,
        direction: CreativeDirection,
        brief: EditorialBrief | None = None,
        research: ResearchReport | None = None
    ) -> BrandAuditReport:
        """
        Retorna um BrandAuditReport determinístico baseado na fixture carregada.
        Os parâmetros de input são aceitos para manter a interface idêntica ao
        BrandGuardianAgent real, mas são ignorados no mock.
        """
        return BrandAuditReport(
            status=AuditStatus(self._fixture["status"]),
            evaluated_rules=self._fixture["evaluated_rules"],
            violations=self._fixture["violations"],
            severity=self._fixture["severity"],
            justification=self._fixture["justification"],
            audit_context=self._fixture["audit_context"],
            recommendations=self._fixture["recommendations"]
        )
