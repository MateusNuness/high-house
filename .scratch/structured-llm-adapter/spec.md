Status: ready-for-agent

## Problem Statement
Atualmente, os agentes de domínio do Editorial OS são módulos rasos (shallow modules) que misturam lógica de negócios (tradução de conceitos para prompts) com o boilerplate pesado de infraestrutura (tratamento de erros, fail-safes dinâmicos, roteamento do LangChain e parsing de objetos Pydantic via `isinstance`). Isso dilui a localidade (locality) do código: se precisarmos alterar como o sistema lida com falhas da API do LLM, teríamos que modificar a lógica repetitiva espalhada em 8 agentes diferentes.

## Solution
A solução é criar um "deep module" na camada de infraestrutura chamado `StructuredLLMAdapter`. Ele irá abstrair toda a complexidade de execução de modelos estruturados, englobando o try/except, a chamada ao `with_structured_output` e o parse seguro. Os agentes manterão apenas a responsabilidade semântica (criar os prompts), passarão o esquema (Schema) esperado e o objeto Pydantic estático de fallback para o adaptador via instanciação interna.

## User Stories
1. As a system architect, I want the LangChain and structured output boilerplate abstracted away into a single adapter, so that the agents are easier to read and maintain.
2. As a system architect, I want error handling and fail-safes to be centralized, so that a change in our LLM error-recovery strategy only needs to be implemented once.
3. As a developer, I want to define agents purely by their prompts and Pydantic schemas, so that I don't have to write repetitive parsing and type-checking logic for every new agent.
4. As a developer, I want agents to pass a pre-instantiated static fallback object to the adapter, so that mypy type hints are preserved cleanly without needing complex callback functions.
5. As a maintainer, I want the adapter to live in the `infrastructure/` directory, so that the `application/` layer remains decoupled from the specific details of LangChain and network I/O.

## Implementation Decisions
- **Módulo a ser criado**: `src/eos/infrastructure/structured_llm_adapter.py`. Conterá a classe `StructuredLLMAdapter`.
- **Interface do Adaptador**:
  - `__init__(self, role: AgentRole)`: Inicializa pegando o LLM correto via `ModelRouter`.
  - `invoke(self, messages: list, schema: Type[T], fallback_obj: T) -> T`: Invoca o LLM, faz o parse e captura exceções, retornando o `fallback_obj` em caso de erro (fail-secure).
- **Módulos a serem modificados**:
  - Os agentes: `art_director_agent.py`, `brand_guardian_agent.py`, `coder_agent.py`, `designer_agent.py`, `editorial_agent.py`, `image_agent.py`, `research_agent.py`, `vision_agent.py`.
- **Interações Específicas**: Os agentes instanciarão o adaptador internamente nos seus construtores (ex: `self.adapter = StructuredLLMAdapter(AgentRole.CODER)`) em vez de obterem a instância do LLM bruta. A execução do LLM debaixo do capô muda de `self.llm.with_structured_output(Schema).invoke(...)` para `self.adapter.invoke(messages, Schema, fallback)`.

## Testing Decisions
- O teste não usará novas costuras (seams) isoladas ou testes unitários triviais. A regra de ouro é "menos seams possível, usando sempre a mais alta".
- O teste será feito na costura mais alta existente: a execução do pipeline completo (via orquestrador LangGraph / `EditorialWorkflow` ou `CollectionOrchestrator`).
- Se a coleção conseguir ser gerada de ponta a ponta sem quebras, e todos os agentes gerarem os artefatos Pydantic corretos na máquina de estados, a refatoração será considerada validada, pois demonstra que o adaptador está passando adiante os estados corretamente e falhando silenciosamente com o objeto estático conforme planejado.

## Out of Scope
- Aprofundamento do `EditorialWorkflow` (o Orquestrador). Esta revisão arquitetural identificou a extração dos Graph Nodes declarativos como o próximo passo (Candidato 2 da nossa análise), mas ele será tratado num ciclo (ou ticket) separado.
- Modificações na lógica de negócios, tuning nos prompts dos agentes ou alteração nos objetos de fallback retornados.
- O `MemoryAgent` está fora de escopo pois não invoca o LLM diretamente no estágio atual.

## Further Notes
O vocabulário no `CONTEXT.md` já foi atualizado em tempo real com o termo `StructuredLLMAdapter` durante a nossa sessão interativa para consolidar essa decisão arquitetural na linguagem ubíqua do projeto.
