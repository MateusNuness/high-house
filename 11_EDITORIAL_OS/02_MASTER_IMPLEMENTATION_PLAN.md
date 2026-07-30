# MASTER_IMPLEMENTATION_PLAN

## 1. Visão Geral
Este documento atua como o **Guia Mestre de Implementação** do *Editorial Operating System (EOS)* da High House. 

**Objetivo:** Sistematizar a injeção do DNA da marca (Estratégia, Fundação e MVP Visual) na arquitetura vazia dos agentes e na infraestrutura do sistema.

**Estado Atual:** O projeto possui a arquitetura de diretórios (`11_EDITORIAL_OS/`) e a infraestrutura de agentes (12 papéis) definidas e lincadas, porém estas "cascas" carecem do contexto profundo da marca, tornando-as operacionais no nível técnico, mas perigosas no nível de identidade.

**Por que a implementação será incremental?**
Para garantir rastreabilidade. Injetar todo o contexto simultaneamente impediria testes isolados e auditorias. Cada alteração (ex: atualizar o *Brand Guardian*) deve ser feita, documentada, validada contra o documento-mãe (ex: `brand-essence.md`), e comitada no Git antes da próxima.

**Por que nenhuma etapa poderá ser pulada?**
O pipeline do EOS é estritamente sequencial. Se o *Designer Agent* for implementado antes do *Design System*, o sistema quebra. Se o *Curator Agent* for implementado sem o limite de fontes, todo o material gerado nas etapas seguintes será lixo genérico de IA.

---

## 2. Estado Atual

**O que já existe (Validado e Completo):**
- Arquitetura de pastas (`11_EDITORIAL_OS/`).
- Pipeline sequencial de 12 agentes mapeado (`README.md`).
- Estrutura da Tríade de Auditoria definida (`review-engine.md`).
- Arquitetura do Motor de Memória e papéis de salvamento isolados (`memory-schema.md`).

**O que está incompleto (Falta Injeção de Contexto):**
- Os *System Prompts* de todos os agentes (`personas.md`) não contêm as restrições da marca.
- O template de experimentos não engloba as 4 Hipóteses Oficiais do Ciclo 1.

**O que está incorreto / desatualizado:**
- O módulo de curadoria (`curation-guidelines.md`) referencia fontes e cores obsoletas (*DM Serif Display*, *Dourado Envelhecido*) em vez das regras vigentes no MVP Visual (*Space Grotesk*, *Preto Profundo*, *Terracota*).

**O que ainda precisa ser criado (Inexistente):**
- O **Design System Base** (Tokens, CSS Variables, Templates HTML, Escalas) na pasta `design_system/` para abastecer o *Coder Agent* e auditar o *Vision Agent*.

---

## 3. Backlog Mestre

| ID | Título | Descrição e Justificativa | Prioridade | Dependências | Arquivos Afetados | Agentes | Dificuldade | Esforço | Risco | Critério de Aceite | DoD |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **EOS-001** | Correção Visual Curadoria | Substituir referências obsoletas (*DM Serif*, *Dourado*) pelo MVP Visual atual (*Space Grotesk*, *Terracota/Lilás*) no documento de curadoria. (Justificativa: Evita rejeições falso-positivas). | P0 (Máxima) | Nenhuma | `modules/curation-guidelines.md` | Curator | Baixa | 1h | Baixo | Regras do arquivo conferem 100% com `identidade-visual-minima-viavel.md`. | Revisado, comitado. |
| **EOS-002** | Design System: Tokens CSS | Criar `tokens.css` com cores, tipografia (Inter/Space Grotesk) e grid. (Justificativa: Base material para o Coder Agent). | P0 (Máxima) | Nenhuma | `design_system/tokens.css` | Coder, Vision | Média | 3h | Alto | Tokens mapeados corretamente a partir do MVP. | Arquivo criado e testado. |
| **EOS-003** | Design System: Templates HTML | Criar `carrossel-base.html` utilizando tokens. (Justificativa: Evita que a IA recrie layouts quebrados do zero). | P0 (Máxima) | EOS-002 | `design_system/templates/...` | Coder, Vision | Média | 3h | Médio | HTML responsivo e aderente ao grid de 10% de margem. | Arquivo criado e renderizável. |
| **EOS-004** | Injeção: Brand Guardian | Inserir os 5 Core Values, a essência e o Modelo de Camadas no prompt do Guardião. (Justificativa: Ele é a barreira final contra diluição). | P1 (Alta) | Nenhuma | `agents/personas.md` | Brand Guardian | Alta | 2h | Alto | O agente possui o checklist de reprovação embasado nos valores. | Atualizado, comitado. |
| **EOS-005** | Injeção: Editorial e Estratégia | Inserir a estrutura de "Capítulos" (Manifesto, Universo, etc) e a "Ausência do Tempo" no Editorial Agent. | P1 (Alta) | Nenhuma | `agents/personas.md` | Editorial | Alta | 2h | Médio | O agente sabe produzir narrativas alinhadas à estratégia do Ciclo 1. | Atualizado, comitado. |
| **EOS-006** | Injeção: Regras Visuais MVP | Inserir paleta, regra de "1 acento" e "espaço em branco" no Art Director e Designer. | P1 (Alta) | EOS-002 | `agents/personas.md` | Art Director, Designer | Média | 2h | Médio | Agentes impedem hiper-saturação. | Atualizado, comitado. |
| **EOS-007** | Injeção: Regra Fotográfica | Atualizar o Image Agent com a preferência de Tipografia brutalista > Foto Real > Foto IA. | P2 (Média) | Nenhuma | `agents/personas.md` | Image | Baixa | 1h | Baixo | Agente prioriza HTML/CSS antes de gerar imagens via IA. | Atualizado, comitado. |
| **EOS-008** | Injeção: Hipóteses Metrics/Critic | Adicionar as 4 Hipóteses Oficiais do Ciclo 1 e proporções (40% Design, 30% Ritual) ao Critic e Metrics Agent. | P2 (Média) | Nenhuma | `agents/personas.md` | Critic, Metrics | Média | 2h | Baixo | Auditoria bate com os KPIs definidos pela Gestão. | Atualizado, comitado. |
| **EOS-009** | Injeção: Regra de Pesquisa | Adicionar restrição (Fontes Originais > Reddit > Proibição de Pinterest) no Research Agent. | P3 (Baixa) | Nenhuma | `agents/personas.md` | Research | Baixa | 1h | Baixo | Limita entrada de clichês no topo do funil. | Atualizado, comitado. |

---

## 4. Roadmap (Fases de Implementação)

- **Fase 1: O Desbloqueio e a Fundação Visual**
  - **Objetivos:** Corrigir erros de legado visual. Fornecer ferramentas (CSS/HTML) para a IA desenhar.
  - **Tarefas:** EOS-001, EOS-002, EOS-003.
- **Fase 2: O Escudo e a Narrativa**
  - **Objetivos:** Injetar identidade no Brand Guardian e estratégia de Capítulos no Editorial Agent. Blinda o sistema estrategicamente.
  - **Tarefas:** EOS-004, EOS-005.
- **Fase 3: A Direção de Arte e a Execução**
  - **Objetivos:** Fazer com que o Art Director e o Designer saibam usar o MVP Visual e o Image Agent saiba quando NÃO usar IA.
  - **Tarefas:** EOS-006, EOS-007.
- **Fase 4: O Fechamento Metodológico**
  - **Objetivos:** Garantir que o começo (Research) pesquise no lugar certo e o fim (Metrics/Critic) avalie a hipótese certa.
  - **Tarefas:** EOS-008, EOS-009.
- **Fase 5: Auditoria Final e Code Review**
  - **Objetivos:** Rodar o primeiro pipeline teste (Pipeline Dry-Run).

---

## 5. Ordem de Implementação

A ordem (Fase 1 ➔ Fase 5) é inegociável. 
- *Fase 1 antes da Fase 3:* O *Designer Agent* (Fase 3) não pode ser atualizado com instruções de uso de um *Design System* que ainda não foi fisicamente criado na Fase 1.
- *Fase 2 antes da Fase 4:* A proteção geral da marca (*Brand Guardian*) é mais crítica e abrangente que a restrição de fontes de um post (*Research*). O Guardião deve estar pronto antes para barrar qualquer erro não previsto nas outras atualizações.

---

## 6. Árvore de Dependências

```text
Sistema Operacional EOS
│
├── Coder Agent & Vision Agent
│   └── Dependem do Design System (Fase 1)
│       └── Depende do MVP Visual (06_IDENTIDADE_VISUAL)
│
├── Brand Guardian Agent & Editorial Agent
│   └── Dependem de Brand Context Injected (Fase 2)
│       └── Depende dos Core Values e Essência (01_FUNDACAO_DA_MARCA)
│
├── Art Director Agent & Designer Agent
│   └── Dependem de Visual Rules Injected (Fase 3)
│       └── Dependem da Finalização do Design System e MVP Visual
│
└── Critic Agent & Metrics Agent
    └── Dependem de Hipóteses Definidas (Fase 4)
        └── Dependem do Protocolo de Experimentação (03_ESTRATEGIA)
```

---

## 7. Critérios de Qualidade (Q-Gates)

Nenhuma tarefa pode ser migrada para "Concluída" sem:
1. **Rastreabilidade Absoluta:** O commit do Git deve referenciar o ID da tarefa (ex: `feat: [EOS-002] implementa tokens.css`).
2. **Aderência à Documentação-Fonte:** A alteração precisa ser uma cópia da lógica já documentada na raiz do projeto (Nada inventado).
3. **Isolamento de Alterações:** Um commit de alteração do *Editorial Agent* não pode alterar linhas do *Coder Agent*.

---

## 8. Estratégia de Testes

- **Testes de Fase 1 (Design System):** Renderizar o arquivo `.html` criado no navegador. Verificar se as cores hex e o grid estão perfeitamente responsivos e aderentes. Reprovação: Fontes erradas ou aspecto não-editorial.
- **Testes de Fase 2, 3 e 4 (Agents Update):** Teste de "Sanity Check" via Git Diff. A auditoria verificará se as palavras-chave ("Ausência do Tempo", "Space Grotesk") estão firmemente injetadas no arquivo `personas.md`.
- **Validação:** Um *Dry-Run* será executado onde se simula um input do usuário e confere-se se o Brand Guardian bloqueia adequadamente uma ideia clichê injetada de propósito.

---

## 9. Estratégia de Rollback

**Reversibilidade Padrão:** Toda modificação ocorrerá sob versionamento do Git.
- Caso uma tarefa de injeção polua ou quebre o arquivo `personas.md`, a ação é: `git restore 11_EDITORIAL_OS/agents/personas.md` e reavaliação.
- Nenhum `git push` será forçado (`-f`). A nuvem conterá apenas etapas concluídas e validadas pela regra de qualidade.
- Backup estático: A versão atual vazia (mas funcional) de `personas.md` servirá de âncora de segurança.

---

## 10. Checklist de Execução Padrão

*Para cada Tarefa do Backlog Mestre (EOS-00X), este roteiro deve ser cumprido rigorosamente:*

- [ ] Revisão do escopo da Tarefa no Documento Mestre.
- [ ] Leitura prévia do Documento-Fonte (ex: `valores-e-principios.md`).
- [ ] Modificação exclusiva dos arquivos listados na tarefa.
- [ ] Revisão autônoma das modificações (Verificação de erros e aderência).
- [ ] Atualização do status no Registro de Progresso (Seção 11) para "Em revisão".
- [ ] Aprovação do Líder/Usuário.
- [ ] Commit semântico descrevendo a alteração e o ID da tarefa.
- [ ] Status alterado para "Concluído" na Seção 11.
- [ ] Liberação para início da próxima tarefa.

---

## 11. Registro de Progresso

| Tarefa | Agente / Módulo | Status | Responsável | Hash do Commit (Futuro) |
|---|---|---|---|---|
| EOS-001 | Curator Agent | Não iniciado | - | - |
| EOS-002 | Design System (CSS) | Não iniciado | - | - |
| EOS-003 | Design System (HTML) | Não iniciado | - | - |
| EOS-004 | Brand Guardian | Não iniciado | - | - |
| EOS-005 | Editorial Agent | Não iniciado | - | - |
| EOS-006 | Art Director & Designer | Não iniciado | - | - |
| EOS-007 | Image Agent | Não iniciado | - | - |
| EOS-008 | Critic & Metrics Agent | Não iniciado | - | - |
| EOS-009 | Research Agent | Não iniciado | - | - |

---

## 12. Regras de Implementação

1. **Nunca implementar mais de uma Fase ou Tarefa por vez.** O trabalho é estritamente atômico.
2. **Nunca modificar múltiplos módulos sem justificativa.** Se a tarefa é alterar o *Brand Guardian*, apenas a respectiva seção em `personas.md` será tocada.
3. **Nunca alterar prompts sem revisar as dependências.** Ver Seção 6 sempre que houver dúvida sobre impacto.
4. **Sempre atualizar este MASTER_IMPLEMENTATION_PLAN.md antes de fechar a tarefa.** A Seção 11 é o painel de controle absoluto.
5. **Sempre aguardar autorização humana (Usuário) entre o status "Em revisão" e "Concluído".** Nenhum push será feito sem aprovação.
6. **O Código não é inventado.** Tudo o que o EOS souber virá impreterivelmente das pastas raízes `01` a `10`.
