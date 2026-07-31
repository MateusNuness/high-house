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
│       │   └── contracts/
│       │       ├── base.py
│       │       ├── editorial_brief.py
│       │       ├── research_report.py
│       │       ├── creative_direction.py
│       │       ├── visual_proposal.py
│       │       ├── brand_audit_report.py
│       │       └── publication_package.py
│       │
│       ├── application/        # Inteligência e Agentes Cognitivos
│       │   └── agents/
│       │       ├── research_agent.py
│       │       └── memory_agent.py
│       │
│       └── infrastructure/     # Abstrações de LLM, Carregadores e Persistência
│           ├── context_loader.py  # MarkdownContextLoader (SSOT Parser)
│           ├── llm_router.py      # ModelRouter & AgentRole mapping
│           ├── llm_provider.py    # Provedor e suporte a providers externos
│           ├── memory.py          # Gerenciador de checkpoints/memória
│           └── telemetry.py       # Observabilidade e rastreabilidade
│
└── tests/                      # Suite de Testes Automatizados
    ├── agents/                 # Testes de aderência cultural e lógica dos agentes
    │   └── test_research_agent.py
    ├── fixtures/               # Fallbacks e mocks de agentes sem consumo de API
    │   ├── dummy_agent.py
    │   └── mock_research_agent.py
    ├── infrastructure/
    └── workflows/
```

---

## 3. Padrões de Engenharia do Runtime

### 3.1 Carregamento Dinâmico de Contexto (SSOT)
Para garantir que o código **não carregue responsabilidade documental**, o `MarkdownContextLoader` realiza o parseamento dinâmico em tempo de execução diretamente de `11_EDITORIAL_OS/04_AGENT_SPECIFICATIONS.md`:

```python
from eos.infrastructure.context_loader import MarkdownContextLoader

# O agente solicita seu contexto via nome de papel, sem conhecer caminhos de arquivo
system_prompt = MarkdownContextLoader.load("Research Agent")
```

### 3.2 Roteamento de Modelos (`ModelRouter`)
Os agentes não acoplam dependências diretas a provedores de LLM específicos (OpenAI, DeepSeek, Anthropic). O papel (`AgentRole`) determina o roteamento adequado:

```python
from eos.infrastructure.llm_router import ModelRouter, AgentRole

llm = ModelRouter.get_model_for_role(AgentRole.RESEARCH)
```

### 3.3 Contratos de Dados Estruturados (`Pydantic`)
Todo fluxo entre nós do LangGraph ou agentes individuais obedece estritamente aos modelos em `src/eos/domain/contracts/`, impedindo que chaves arbitrárias fluam pelo sistema:
- `EditorialBrief` ➔ `ResearchReport` (`EOS-009`)

---

## 4. Status de Implementação e Infraestrutura

### 4.1 Infraestrutura Abstrata & Runtime (Fase 1.5)

| Módulo | Tarefa | Status | Artefato | Validação |
|---|---|---|---|---|
| **State Schema Architecture** | EOS-012.1 | **Concluído** | `src/eos/domain/state.py` | TypedDicts globais (`GlobalState`) |
| **LLM Provider Abstraction** | EOS-012.2 | **Concluído** | `src/eos/infrastructure/llm_provider.py` & `llm_router.py` | Desacoplamento e roteamento por `AgentRole` |
| **LangGraph Orchestrator** | EOS-012.3 | **Concluído** | `src/eos/application/workflows/editorial_creation.py` | DAG com nós, arestas e ponto de interrupção (HIL) |
| **Checkpoints & Persistence** | EOS-012.4 | **Concluído** | `src/eos/infrastructure/checkpoints.py` & `memory.py` | Interrupção, salvamento e retomada de estado via `test_persistence.py` |
| **Memory Agent Context** | EOS-010 | **Concluído** | `src/eos/application/agents/memory_agent.py` | Rastreabilidade e log de eventos/decisões |

### 4.2 Agentes Cognitivos (Fases 1 e 2)

| Agente | Tarefa | Status | Contrato I/O | Loader SSOT | Fallback Mock |
|---|---|---|---|---|---|
| **Research Agent** | EOS-009 | **Concluído** | `EditorialBrief` ➔ `ResearchReport` | ✅ Ativo | `MockResearchAgent` |
| **Curator Agent** | EOS-001 | **Concluído** | `ResearchReport` ➔ `CuratedReport` | ✅ Ativo | — |
| **Memory Agent** | EOS-014 | **Concluído** | Runtime Persistent Memory | ✅ Ativo | — |
| **Editorial Agent** | EOS-005 | **Concluído** | `ResearchReport` ➔ `CreativeDirection` | ✅ Ativo | `MockEditorialAgent` |
| **Brand Guardian** | EOS-004 | *Planejado* | — | — | — |

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
pytest

# Executar especificamente os testes de aderência cultural do Research Agent
pytest tests/agents/test_research_agent.py
```

### 5.3 Modos de Execução (API vs Mock)
- **Modo Sandbox / CI:** Utilize a classe `MockResearchAgent` em `tests/fixtures/mock_research_agent.py` para validar fluxos do LangGraph sem necessidade de chaves de API ou conexões de rede.
- **Modo Produção:** O `ResearchAgent` em `src/eos/application/agents/research_agent.py` carrega o contexto do documento oficial e conecta ao `ModelRouter` para inferência real via DeepSeek / LLM configurado.
