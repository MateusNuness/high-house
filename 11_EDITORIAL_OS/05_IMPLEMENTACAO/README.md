# High House — Editorial OS Implementation (Runtime)

> **Documento Operacional:** Arquitetura do Runtime Python, Estrutura de Código, Padrões de Injeção de Contexto e Execução de Testes do Editorial Operating System (EOS).

---

## 1. Visão Geral

A pasta `05_IMPLEMENTACAO` é a camada de execução de software (Runtime) do Editorial OS. Desenvolvida em **Python 3.12+**, integrando **LangChain**, **LangGraph** e **Pydantic**, esta camada é responsável por instanciar a rede de 12 agentes cognitivos da High House.

O código foi desenhado seguindo princípios de **Domain-Driven Design (DDD)** e a diretiva inegociável de **Single Source of Truth (SSOT / DRY)**: nenhuma regra de negócio, prompt ou contrato é duplicado no código. O runtime lê a documentação normativa de `11_EDITORIAL_OS` para alimentar a inteligência.

---

## 2. Arquitetura do Pacote (`src/eos`)

```text
05_IMPLEMENTACAO/
├── pyproject.toml              # Dependências e configurações da aplicação
├── README.md                   # Esta documentação técnica
├── src/
│   └── eos/
│       ├── domain/             # Contratos estritos de entrada/saída (Pydantic)
│       │   ├── state.py        # GlobalState (TypedDict do LangGraph)
│       │   └── contracts/
│       │       ├── base.py             # AuditStatus Enum
│       │       ├── editorial_brief.py
│       │       ├── research_report.py
│       │       ├── creative_direction.py
│       │       ├── visual_proposal.py
│       │       ├── brand_audit_report.py
│       │       └── publication_package.py
│       │
│       ├── application/        # Inteligência e Agentes Cognitivos
│       │   ├── agents/
│       │   │   ├── research_agent.py
│       │   │   ├── editorial_agent.py
│       │   │   ├── brand_guardian_agent.py  # EOS-004 — Primeiro agente de JULGAMENTO
│       │   │   └── memory_agent.py
│       │   └── workflows/
│       │       ├── editorial_creation.py   # DAG LangGraph com routing condicional
│       │       └── guardian_policy.py      # GuardianDecisionPolicy (routing pós-auditoria)
│       │
│       └── infrastructure/     # Abstrações de LLM, Carregadores e Persistência
│           ├── context_loader.py  # MarkdownContextLoader (SSOT Parser + contextos dedicados)
│           ├── llm_router.py      # ModelRouter & AgentRole mapping
│           ├── llm_provider.py    # Provedor e suporte a providers externos
│           ├── memory.py          # Gerenciador de checkpoints/memória
│           └── telemetry.py       # Observabilidade e rastreabilidade
│
└── tests/                      # Suite de Testes Automatizados
    ├── agents/                 # Testes de aderência cultural e lógica dos agentes
    │   ├── test_research_agent.py
    │   ├── test_editorial_agent.py
    │   └── test_brand_guardian_agent.py  # 7 testes: contrato, anti-patterns, fail-secure
    ├── fixtures/               # Fallbacks, mocks e fixtures JSON
    │   ├── dummy_agent.py
    │   ├── mock_research_agent.py
    │   ├── mock_editorial_agent.py
    │   ├── mock_brand_guardian_agent.py  # Mock determinístico baseado em fixtures
    │   ├── approved_visual.json         # Fixture: proposta underground autêntica
    │   ├── rejected_visual.json         # Fixture: proposta SaaS / anti-pattern
    │   └── needs_revision.json          # Fixture: proposta com materialidade insuficiente
    ├── infrastructure/
    └── workflows/
        ├── test_editorial_workflow.py   # Testes E2E + 5 testes de GuardianDecisionPolicy
        └── test_persistence.py
```

---

## 3. Padrões de Engenharia do Runtime

### 3.1 Carregamento Dinâmico de Contexto (SSOT)
O `MarkdownContextLoader` suporta duas fontes de contexto com prioridade:

1. **Contexto dedicado** (`04_AGENT_CONTEXTS/<slug>_context.md`) — preferencial
2. **Documento monolítico** (`04_AGENT_SPECIFICATIONS.md`) — fallback

```python
from eos.infrastructure.context_loader import MarkdownContextLoader

# Carrega contexto dedicado (brand_guardian_context.md existe)
system_prompt = MarkdownContextLoader.load("Brand Guardian Agent")

# Carrega do documento monolítico (não tem arquivo dedicado)
system_prompt = MarkdownContextLoader.load("Research Agent")
```

### 3.2 Roteamento de Modelos (`ModelRouter`)
Os agentes não acoplam dependências diretas a provedores de LLM específicos (OpenAI, DeepSeek, Anthropic). O papel (`AgentRole`) determina o roteamento adequado:

```python
from eos.infrastructure.llm_router import ModelRouter, AgentRole

llm = ModelRouter.get_model_for_role(AgentRole.VALIDATOR)  # Brand Guardian
llm = ModelRouter.get_model_for_role(AgentRole.RESEARCH)    # Research Agent
```

### 3.3 Contratos de Dados Estruturados (`Pydantic`)
Todo fluxo entre nós do LangGraph obedece estritamente aos modelos em `src/eos/domain/contracts/`, impedindo que chaves arbitrárias fluam pelo sistema:
- `EditorialBrief` → `ResearchReport` (EOS-009)
- `ResearchReport` → `CreativeDirection` (EOS-005)
- `VisualProposal` + `CreativeDirection` → `BrandAuditReport` (EOS-004)

### 3.4 GuardianDecisionPolicy (Separação Domínio ↔ Workflow)
O Brand Guardian apenas **julga**. Quem decide o **fluxo** é a `GuardianDecisionPolicy`:

```python
from eos.application.workflows.guardian_policy import GuardianDecisionPolicy

# APPROVED → human_approval
# REJECTED (revisão < 3) → designer (loop)
# REJECTED (revisão >= 3) → human_approval (escalonamento)
# HUMAN_REVIEW_REQUIRED → human_approval
next_node = GuardianDecisionPolicy.route(state)
```

---

## 4. Status de Implementação e Infraestrutura

### 4.1 Infraestrutura Abstrata & Runtime (Fase 1.5)

| Módulo | Tarefa | Status | Artefato | Validação |
|---|---|---|---|---|
| **State Schema Architecture** | EOS-012.1 | **Concluído** | `src/eos/domain/state.py` | TypedDicts globais (`GlobalState`) |
| **LLM Provider Abstraction** | EOS-012.2 | **Concluído** | `src/eos/infrastructure/llm_provider.py` & `llm_router.py` | Desacoplamento e roteamento por `AgentRole` |
| **LangGraph Orchestrator** | EOS-012.3 | **Concluído** | `src/eos/application/workflows/editorial_creation.py` | DAG com routing condicional pós-Guardian |
| **Checkpoints & Persistence** | EOS-012.4 | **Concluído** | `src/eos/infrastructure/checkpoints.py` & `memory.py` | Interrupção, salvamento e retomada de estado |
| **Memory Agent Context** | EOS-010 | **Concluído** | `src/eos/application/agents/memory_agent.py` | Rastreabilidade e log de eventos/decisões |

### 4.2 Agentes Cognitivos (Fases 2 e 3)

| Agente | Tarefa | Status | Contrato I/O | Loader SSOT | Fallback Mock |
|---|---|---|---|---|---|
| **Research Agent** | EOS-009 | **Concluído** | `EditorialBrief` → `ResearchReport` | ✅ Monolítico | `MockResearchAgent` |
| **Curator Agent** | EOS-001 | **Concluído** | `ResearchReport` → `CuratedReport` | ✅ Monolítico | — |
| **Memory Agent** | EOS-014 | **Concluído** | Runtime Persistent Memory | ✅ Monolítico | — |
| **Editorial Agent** | EOS-005 | **Concluído** | `ResearchReport` → `CreativeDirection` | ✅ Monolítico | `MockEditorialAgent` |
| **Brand Guardian** | EOS-004 | **Concluído** | `Brief+Research+Direction+Proposal` → `BrandAuditReport` | ✅ Dedicado | `MockBrandGuardianAgent` |

### 4.3 Workflow LangGraph (Routing Condicional)

O workflow evoluiu de linear para condicional com a implementação do Brand Guardian:

```
Research → Editorial → Designer → Brand Guardian → [Decision Policy]
                                                        │
                                                        ├── APPROVED → Human Review → END
                                                        ├── HUMAN_REVIEW_REQUIRED → Human Review → END
                                                        ├── APPROVED_WITH_CHANGES (rev < 3) → Designer (loop)
                                                        ├── REJECTED (rev < 3) → Designer (loop)
                                                        └── Any (rev >= 3) → Human Review → END
```

### 4.4 Acumulador Sequencial e Continuidade Narrativa
O `CollectionOrchestrator` implementa o recurso de Acumulação Sequencial:
- Pôsteres gerados numa mesma coleção alimentam um histórico (`previous_posters`).
- O `EditorialWorkflow` injeta esse contexto no `EditorialAgent`.
- A direção criativa avança mantendo coerência visual e textual entre os elementos da coleção.

---

## 5. Guia de Execução e Testes

### 5.1 Configuração do Ambiente
```powershell
# Ativar o ambiente virtual e definir PYTHONPATH
$env:PYTHONPATH="src"
```

### 5.2 Executando a Suite de Testes
```powershell
# Executar todos os testes
pytest -v

# Testes do Brand Guardian (EOS-004)
pytest tests/agents/test_brand_guardian_agent.py -v

# Testes de Workflow com routing condicional
pytest tests/workflows/test_editorial_workflow.py -v

# Suite completa
pytest tests/ -v
```

### 5.3 Modos de Execução (API vs Mock)
- **Modo Sandbox / CI:** `MockBrandGuardianAgent` em `tests/fixtures/` carrega fixtures JSON determinísticas (`approved_visual.json`, `rejected_visual.json`, `needs_revision.json`).
- **Modo Produção:** O `BrandGuardianAgent` carrega o contexto dedicado de `04_AGENT_CONTEXTS/brand_guardian_context.md` e conecta ao `ModelRouter` para inferência real via DeepSeek/LLM configurado.

---

*Última atualização: Implementação da Continuidade Narrativa (Sequential Accumulator) para geração coesa de pôsteres em coleções.*
