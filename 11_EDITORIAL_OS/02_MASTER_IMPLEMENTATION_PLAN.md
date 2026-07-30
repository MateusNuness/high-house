# 02_MASTER_IMPLEMENTATION_PLAN.md

## 1. Propósito
Este documento atua como o **Guia Mestre de Implementação** do *Editorial Operating System (EOS)* da High House. 

Sua função é orquestrar a construção do sistema garantindo que a implementação obedeça estritamente à documentação fundacional (01, 03, 03.1 e 04). O MASTER apenas orquestra; a verdadeira fonte de regras reside nos documentos de especificação e de fundação da marca.

## 2. Relação com Arquitetura
Uma informação deve existir em apenas um local. Nunca duplicar conhecimento.

A hierarquia da verdade do EOS segue o fluxo:
**Fundação (01-10)** ➔ **Design System Specification (03.1)** ➔ **Agent Specifications (04)** ➔ **Implementação (05)**

Se uma regra da marca ou do design mudar, ela deve ser atualizada na sua fonte, não neste plano.

## 3. Estado Inicial da Implementação
A implementação parte das seguintes premissas e do seguinte estado de arte:
- A arquitetura lógica do projeto está definida e provisionada (pastas e documentos raiz).
- O macro do Editorial OS está estruturado (01 a 05).
- Agentes possuem contratos e especificações vazias ou iniciais, aguardando injeção de contexto.
- O motor de memória possui esquema inicial.
- O Design System ainda não está materializado em código (CSS/HTML).

## 4. Estratégia de Implementação Incremental
Para garantir rastreabilidade, injetar todo o contexto simultaneamente impediria testes isolados e auditorias. Cada alteração deve ser feita, documentada e validada contra o documento-mãe aplicável e comitada no Git antes da próxima.

Nenhuma etapa do pipeline pode ser pulada. (ex: IA sem Design System = criatividade sem restrição). O sistema quebra se as premissas não forem seguidas em ordem cronológica.

## 5. Backlog Mestre

### EOS-000 — Auditoria de Fonte de Verdade
- **Objetivo:** Validar documentos raiz (01 a 10) como fontes oficiais e resolver contradições antes de escrever qualquer código.
- **Justificativa:** Código nasce da documentação. Se existirem inconsistências na Fundação ou Estratégia, o EOS herdará essas falhas.
- **Artefato gerado:** `05_GOVERNANCE/eos-000-source-of-truth-audit.md`
- **Validação:** Não existem conflitos entre Fundação, Estratégia, Identidade Visual e Design System.
- **Memória gerada:** `05_IMPLEMENTACAO/memory/decision-log/eos-000-audit.md`

### EOS-001 — Atualização do Curator Agent
- **Objetivo:** Atualizar regras de curadoria do Curator Agent conforme as diretrizes oficiais de Identidade e Estratégia.
- **Artefato gerado:** `05_IMPLEMENTACAO/modules/curation-guidelines.md` e `04_AGENT_SPECIFICATIONS.md` (Curator).
- **Validação:** Regras do arquivo conferem 100% com a identidade atual.
- **Memória gerada:** `05_IMPLEMENTACAO/memory/decision-log/eos-001-curator.md`

### EOS-002 — Implementação do Design System Base (Tokens)
- **Objetivo:** Criar `tokens.css` mapeando tipografia primária/secundária, cores, grids e espaçamentos estritamente de acordo com `03.1_DESIGN_SYSTEM_SPECIFICATION.md`.
- **Artefato gerado:** `05_IMPLEMENTACAO/design_system/tokens.css`
- **Validação:** Browser render test demonstrando o mapeamento correto dos tokens sem inferir design.
- **Memória gerada:** `05_IMPLEMENTACAO/memory/decision-log/design-system-v1.md`

### EOS-003 — Implementação do Design System Base (Templates HTML)
- **Objetivo:** Criar componentes base (ex: `carrossel-base.html`) utilizando `tokens.css` de acordo com os princípios do `03.1_DESIGN_SYSTEM_SPECIFICATION.md`.
- **Artefato gerado:** `05_IMPLEMENTACAO/design_system/templates/...`
- **Validação:** HTML responsivo renderizando os tokens corretamente e respeitando regras estéticas fundamentais.
- **Memória gerada:** `05_IMPLEMENTACAO/memory/decision-log/html-templates-v1.md`

### EOS-004 — Injeção de Contexto: Brand Guardian
- **Objetivo:** Atualizar contrato cognitivo do Brand Guardian Agent conforme `04_AGENT_SPECIFICATIONS.md` e fundação da marca.
- **Artefato gerado:** Checklist de aprovação/reprovação dentro do respectivo Agente.
- **Validação:** Agente corretamente configurado na especificação e pronto para proteger a essência.
- **Memória gerada:** `05_IMPLEMENTACAO/memory/decision-log/eos-004-guardian.md`

### EOS-005 — Injeção de Contexto: Editorial e Estratégia
- **Objetivo:** Atualizar o contrato do Editorial Agent com a estratégia de marca e tom de voz conforme documentação raiz.
- **Artefato gerado:** Atualização no `04_AGENT_SPECIFICATIONS.md` (Editorial).
- **Validação:** Agente sabe reproduzir as narrativas alinhadas à estratégia atual.
- **Memória gerada:** `05_IMPLEMENTACAO/memory/decision-log/eos-005-editorial.md`

### EOS-006 — Injeção de Contexto: Art Director e Designer
- **Objetivo:** Injetar regras visuais oficiais no Art Director e Designer Agent conforme `03.1_DESIGN_SYSTEM_SPECIFICATION.md`.
- **Artefato gerado:** Atualização no `04_AGENT_SPECIFICATIONS.md` (Art Director e Designer).
- **Validação:** Agentes não produzem hyper-saturação e seguem os 24 pontos da RFC.
- **Memória gerada:** `05_IMPLEMENTACAO/memory/decision-log/eos-006-design.md`

### EOS-007 — Injeção de Contexto: Image Agent
- **Objetivo:** Injetar a estratégia fotográfica e hierarquia de criação de imagens conforme especificações.
- **Artefato gerado:** Atualização no `04_AGENT_SPECIFICATIONS.md` (Image).
- **Validação:** Image agent prefere soluções de markup antes de forçar geração de IA.
- **Memória gerada:** `05_IMPLEMENTACAO/memory/decision-log/eos-007-image.md`

### EOS-008 — Injeção de Contexto: Critic e Metrics Agent
- **Objetivo:** Atualizar hipóteses oficiais de teste para o Critic e Metrics Agent.
- **Artefato gerado:** Atualização no `04_AGENT_SPECIFICATIONS.md` (Critic, Metrics).
- **Validação:** KPIs e critérios de auditoria estão lincados com a meta do ciclo atual.
- **Memória gerada:** `05_IMPLEMENTACAO/memory/decision-log/eos-008-metrics.md`

### EOS-009 — Injeção de Contexto: Research Agent
- **Objetivo:** Adicionar restrições de pesquisa e limites de fontes no Research Agent conforme especificações.
- **Artefato gerado:** Atualização no `04_AGENT_SPECIFICATIONS.md` (Research).
- **Validação:** Entradas são filtradas para garantir qualidade antes da criação.
- **Memória gerada:** `05_IMPLEMENTACAO/memory/decision-log/eos-009-research.md`

---

## 6. Roadmap (Fases de Implementação)
- **Fase 0: A Validação da Verdade**
  - **Objetivos:** Confirmar coerência nas fontes raiz de documentação.
  - **Tarefas:** EOS-000.
- **Fase 1: O Desbloqueio e a Fundação Visual**
  - **Objetivos:** Fornecer ferramentas (CSS/HTML) para a IA desenhar, baseando-se estritamente na documentação estética.
  - **Tarefas:** EOS-001, EOS-002, EOS-003.
- **Fase 2: O Escudo e a Narrativa**
  - **Objetivos:** Injetar identidade no Brand Guardian e estratégia no Editorial Agent. Blinda o sistema estrategicamente.
  - **Tarefas:** EOS-004, EOS-005.
- **Fase 3: A Direção de Arte e a Execução**
  - **Objetivos:** Garantir que o Art Director e o Designer saibam usar o Design System (Fase 1).
  - **Tarefas:** EOS-006, EOS-007.
- **Fase 4: O Fechamento Metodológico**
  - **Objetivos:** Garantir que o começo (Research) e o fim (Metrics/Critic) possuam o escopo correto do ciclo.
  - **Tarefas:** EOS-008, EOS-009.
- **Fase 5: Auditoria Final e Code Review**
  - **Objetivos:** Rodar o primeiro pipeline teste (Pipeline Dry-Run).

---

## 7. Dependências
- **A ordem (Fase 0 ➔ Fase 5) é inegociável.**
- **Fase 1 DEVE ocorrer antes da Fase 3:** IA sem Design System implementado gera criatividade sem restrição estrutural (comporta-se como um compiler livre).
- **Fase 2 DEVE ocorrer antes da Fase 4:** A proteção do Guardian é crítica para barrar alucinações antes de aprofundar restrições de pesquisas e métricas.

---

## 8. Quality Gates
Nenhuma tarefa pode ser migrada para "Concluída" sem:
1. **Rastreabilidade Absoluta:** Todo commit deve referenciar sua respectiva Tarefa Mestre.
2. **Aderência à Fonte de Verdade:** Nenhuma regra ou valor de design é "imaginado" aqui. Tudo deve emanar dos arquivos `01` a `10`, além de `03.1` e `04`.
3. **Artefatos Materializados:** Os artefatos tangíveis (códigos, guidelines) e a Memória Log devem estar gerados e persistidos em seus locais corretos.

---

## 9. Estratégia de Testes
- **Testes Visuais:** (Render tests em browsers) para as saídas da Fase 1, atestando tokens.
- **Sanity Checks de Revisão:** Avaliação de Diff (Git) para injeção de contexto nos agentes vs as Specifications.
- **Teste de Integração (Dry-Run):** Execução teste de todo o pipeline, assegurando que o Guardião reprove devidamente e que o Coder entregue o esperado.

---

## 10. Rollback
- A reversibilidade padrão é feita através do versionamento **Git**.
- Módulos, prompts ou documentos corrompidos durante uma injeção sofrem `git restore` imediato.
- Nenhum push forçado (`-f`) é aceito sem deliberação técnica.

---

## 11. Registro de Progresso

| Tarefa | Status | Responsável | Hash do Commit (Futuro) |
|---|---|---|---|
| EOS-000 | Em revisão | - | - |
| EOS-001 | Não iniciado | - | - |
| EOS-002 | Não iniciado | - | - |
| EOS-003 | Não iniciado | - | - |
| EOS-004 | Não iniciado | - | - |
| EOS-005 | Não iniciado | - | - |
| EOS-006 | Não iniciado | - | - |
| EOS-007 | Não iniciado | - | - |
| EOS-008 | Não iniciado | - | - |
| EOS-009 | Não iniciado | - | - |

---

## 12. Regras Operacionais
1. **Atomicidade:** Nunca implementar mais de uma Fase ou Tarefa simultaneamente.
2. **Isolamento:** Nunca modificar múltiplos agentes ou módulos estruturais sem justificativa ligada estritamente à tarefa atual.
3. **Fidelidade ao DNA:** Sempre basear-se estritamente nas documentações de Fundação e nas Especificações de Design/Agentes. O MASTER apenas delega; a IA consulta a fonte antes de alterar qualquer contrato.
4. **Atualização Contínua:** Sempre atualizar este documento (MASTER_IMPLEMENTATION_PLAN.md) refletindo a finalização de uma tarefa (Seção 11).
