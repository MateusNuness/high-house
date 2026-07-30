# 01_SYSTEM_ARCHITECTURE.md

> **High House — Editorial Operating System (EOS)**  
> **Tipo:** Documento Mestre de Arquitetura do Sistema  
> **Status:** Ativo / Fonte da Verdade Arquitetural  
> **Versão:** 2.1  

---

## 1. Filosofia

- **Patrimônio sobre Conteúdo:** A High House não publica posts isolados; constrói repertório, autoridade e patrimônio intelectual.
- **Coleções Editoriais:** Todo o conteúdo é organizado em coleções com narrativa contínua entre capítulos, onde cada publicação fortalece a anterior.
- **Estado de Presença:** A essência da marca se apoia na desaceleração, no estado de flow, na imersão profunda e no ritual urbano sofisticado.
- **Antítese do Clichê:** Rejeição absoluta a templates genéricos ("Visual Canva"), linguagem de startup ("Thread 10 passos") e apologia estilizada superficial ("Clichês Canábicos Neon").

---

## 2. Arquitetura

- **Princípio de Baixo Acoplamento e Alta Coesão:** Agentes operam de forma isolada, conhecendo apenas os contratos de entrada e saída (APIs internas), sem dependência de código interno de outros agentes.
- **Fonte Única da Verdade (SSOT):** Nenhuma decisão é tomada por intuição ou preenchida com conhecimento genérico de IA; todas as regras derivam exclusivamente da documentação oficial da marca (`01_FUNDACAO`, `03_ESTRATEGIA`, `04_IDENTIDADE`, `06_IDENTIDADE_VISUAL`).
- **Arquitetura Determinística:** Contextos idênticos produzem direcionamentos e decisões consistentes, limitando a aleatoriedade da IA apenas onde a criatividade é requerida.
- **Portões de Arquitetura (Architecture Gates / DoA):** Uma fase do pipeline só avança para a seguinte se atender rigorosamente à *Definition of Architecture* estabelecida.

---

## 3. Domínios

O sistema é segregado em 10 domínios arquiteturais atômicos:

1. **Conhecimento (Knowledge Domain):** Extração, investigação de mercado e prospecção de repertório cultural.
2. **Curadoria (Curation Domain):** Filtragem severa, eliminação de ruídos e separação de anti-patterns.
3. **Narrativa (Editorial Domain):** Enredo, mensagem central, intenção emocional e estrutura de capítulos.
4. **Direção Criativa (Creative Direction Domain):** Definição da atmosfera visual, linguagem de luz, texturas e ritmo.
5. **Design (Layout Domain):** Estruturação da hierarquia visual, tipografia e grides no Design System.
6. **Produção Visual (Visual Production Domain):** Decisão estratégica do meio (Fotografia Real vs IA vs HTML Brutalista).
7. **Implementação (Implementation Domain):** Codificação de artefatos reproduzíveis em HTML/CSS/SVG.
8. **Auditoria (Audit Domain):** Tríade de inspeção técnica (Vision), mercadológica (Critic) e de essência (Brand Guardian).
9. **Memória (Memory Domain):** Consolidação contínua do Knowledge Graph, Decision Log e histórico narrativo.
10. **Inteligência (Metrics Domain):** Acompanhamento empírico e validação de hipóteses pós-publicação.

---

## 4. Pipeline

O pipeline de execução segue uma cascata determinística sequencial composta por 12 agentes e 4 fases de ciclo de vida:

```text
[Briefing]
   │
   ▼ (Fase 1: Pesquisa & Estratégia)
1. Research Agent ➔ 2. Curator Agent ➔ 3. Editorial Agent
   │
   ▼ (Fase 2: Direção & Execução Criativa)
4. Art Director Agent ➔ 5. Designer Agent ➔ 6. Image Agent ➔ 7. Coder Agent
   │
   ▼ (Fase 3: Tríade de Auditoria)
8. Vision Agent (Técnica) ➔ 9. Critic Agent (Mercado) ➔ 10. Brand Guardian Agent (Essência)
   │
   ▼ (Fase 4: Fechamento & Memória)
11. Memory Agent ➔ 12. Metrics Agent ➔ [Publish]
```

### Regras de Recuperação de Erros e Loops:
- **Vision Agent (Falha Técnica):** Retorna o artefato ao `Coder Agent` ou `Designer Agent` (Máximo: 3 revisões).
- **Critic Agent (Falha Estratégica):** Retorna ao `Art Director Agent` ou `Curator Agent` (Máximo: 2 revisões).
- **Brand Guardian Agent (Falha de Essência):** Retorna ao `Editorial Agent` (Máximo: 2 revisões).
- **Kill Thread:** Excedido o limite de loops, a execução é interrompida (`BLOCKED`), registrando o erro no *Decision Log* e solicitando intervenção humana.

---

## 5. Comunicação

- **Zero Chat Aberto:** Os agentes não se comunicam via texto livre desestruturado.
- **Contratos de Dados Estruturados:** Toda transmissão de contexto entre agentes é feita obrigatoriamente através de payloads JSON/YAML estritamente tipados.
- **Contrato Exemplo (`Research Agent` ➔ `Curator Agent`):**

```yaml
research_package:
  topic: "string"
  objective: "string"
  primary_sources: ["url_or_ref"]
  secondary_sources: ["url_or_ref"]
  rejected_sources: [{"source": "string", "reason": "string"}]
  insights: ["string"]
  suggested_hypotheses: ["string"]
  confidence_score: 0.00
```

---

## 6. Estados

O ciclo de vida de qualquer coleção ou capítulo obedece a uma máquina de estados finita:

```text
Draft
  │
  ▼
Research ➔ Curated ➔ Editorial Approved ➔ Creative Direction
  │
  ▼
Designed ➔ Implemented ➔ Rendered
  │
  ▼
Under Review (Vision / Critic / Guardian)
  │
  ▼
Approved ➔ Ready To Publish ➔ Published ➔ Monitoring ➔ Archived
```

---

## 7. Memória (alto nível)

A memória permanente do EOS é segregada por responsabilidades e níveis de acesso restritos:

| Tipo de Memória | Função | Escrita (Write) | Leitura (Read) |
|---|---|---|---|
| **Brand Memory** | Núcleo imutável (Essência, Valores, Posicionamento). | Apenas Humano | Todos os Agentes |
| **Collection Memory** | Histórico cronológico e enredos das coleções já lançadas. | Memory Agent | Research, Editorial |
| **Knowledge Graph** | Rede não-linear de conceitos, conexões e referências acumuladas. | Memory Agent | Research, Curator |
| **Decision Log** | Registro de justificativas e alternativas descartadas. | Memory Agent | Todos os Agentes |
| **Experiment Memory** | Hipóteses formuladas vs KPIs reais observados. | Metrics Agent | Editorial, Critic |
| **Visual Memory** | Design System vivo, tokens CSS e templates visuais. | Coder / Memory | Art Director, Vision |

---

## 8. MCPs (alto nível)

Uso estratégico e justificado dos Model Context Protocols (MCPs) gratuitos e open-source:

- **Filesystem MCP:** Leitura e escrita no sistema de arquivos local (`memory/`, `design_system/`, `logs_and_docs/`).
- **Fetch / Browser MCP:** Investigação de fontes originais de cultura, arquitetura e mercado para o Research Agent.
- **Playwright MCP:** Renderização e captura de screenshots de alta resolução dos templates HTML/CSS para análise automatizada de layout pelo Vision Agent.
- **Sequential Thinking MCP:** Decomposição lógica em múltiplas etapas de raciocínio para o Editorial Agent estruturar narrativas complexas.

---

## 9. Segurança

- **Blindagem de Identidade:** O `Brand Guardian Agent` possui poder de veto absoluto e atua como a barreira inviolável contra a diluição da marca ou postagens genéricas.
- **Proteção de Dados e Chaves:** Garantia de que segredos, chaves de API (`DEEPSEEK_API_KEY`) e arquivos locais sensíveis permanecem protegidos por `.gitignore` e pelo arquivo `.env`.
- **Isolamento de Estado:** Agentes operantes não possuem autoridade para alterar a *Brand Memory* sem intervenção e aprovação do fundador.

---

## 10. Escalabilidade

- **Crescimento Não-Linear:** O *Knowledge Graph* permite que a marca expanda repertório conectando conceitos antigos a novas coleções sem perda de contexto histórico.
- **Reutilização de Design Tokens:** O Design System modularizado permite que o `Coder Agent` e o `Designer Agent` gerem dezenas de formatos (stories, carrosséis, portfólio) mantendo 100% de consistência.
- **Evolução de Agentes:** Agentes podem ter seus System Prompts atualizados ou refinados sem a necessidade de reestruturar a arquitetura do pipeline ou o banco de dados de memória.

---

## 11. Arquitetura de Memória

### Objetivo
O Editorial Operating System assume que modelos de linguagem possuem memória limitada e volátil. Portanto, o sistema **não depende** da memória interna do modelo. Todo conhecimento permanente deve existir em arquivos versionados e estruturados. A memória pertence ao sistema, nunca ao modelo de IA.

### Princípios
Toda memória deve ser:
- Persistente
- Versionável
- Auditável
- Consultável
- Reutilizável
- Independente do modelo utilizado

Nenhuma decisão importante poderá existir apenas dentro da conversa.

### Categorias de Memória

1. **Memória Estratégica:** Conhecimento permanente sobre a marca (Fundação, Valores, Posicionamento, Manifesto, Identidade). Mudanças são extremamente raras e exigem autorização humana.
2. **Memória Editorial:** Conhecimento produzido durante as coleções (Capítulos, Narrativas, Hipóteses, Insights). Atualização frequente a cada ciclo.
3. **Memória Operacional:** Informações utilizadas durante a execução do pipeline (Status, Logs, Estados, Execuções, Histórico). Não influencia diretamente a identidade.
4. **Memória Experimental:** Resultados de experimentos (Hipótese, Métricas, Conclusão, Aprendizados, Decisão final).

---

## 12. Knowledge Graph

O sistema interpreta toda informação como uma rede de conhecimento interconectada, nunca como documentos isolados. Cada documento representa um nó; cada referência representa uma conexão.

```text
Manifesto
      │
      ├──────────────┐
      │              │
Valores        Identidade
      │              │
      ├──────┐       │
      │      │       │
Coleção 1    Coleção 2
      │
      ├────────────┐
      │            │
Capítulo 1    Capítulo 2
```

O objetivo do grafo é impedir duplicação de conhecimento e permitir navegação semântica.

### Relações Suportadas
Uma informação poderá estabelecer as seguintes pontes relacionais:
- `depende_de`
- `referencia`
- `contradiz`
- `substitui`
- `expande`
- `inspira`
- `valida`
- `invalida`

---

## 13. Arquitetura de Comunicação

Todo fluxo entre módulos ocorre estritamente através de contratos serializáveis (YAML ou JSON). Nunca através de linguagem livre.

```text
Domínio ➔ Contrato ➔ Validação ➔ Próximo Domínio
```

Os contratos funcionam como portas lógicas de entrada e saída. Se o payload falhar na validação do schema, o próximo domínio é bloqueado imediatamente.

---

## 14. Arquitetura de MCPs

Os MCPs (Model Context Protocols) representam capacidades externas e atuam como adaptadores. Eles não pertencem ao núcleo do EOS.

```text
EOS ➔ MCP (Adaptador) ➔ Ferramenta Externa
```

### MCPs Obrigatórios (Núcleo)
- **Filesystem:** Leitura, escrita, memória e versionamento local.
- **Playwright:** Renderização, screenshots, inspeção visual e auditoria de interface.
- **Browser / Fetch:** Pesquisa, documentação, referências e validação externa.
- **Sequential Thinking:** Raciocínio complexo, planejamento e decomposição lógica.

### MCPs Opcionais (Extensões)
- GitHub
- Banco Vetorial
- Google Drive
- Notion
- Cloud Storage

Nenhum MCP opcional é necessário para o funcionamento do núcleo do EOS.

---

## 15. Independência do Modelo

O EOS foi projetado de forma neutra para **nunca depender de um único modelo de IA**. O sistema deverá funcionar de maneira agnóstica com:
- OpenAI (GPT-4, GPT-5)
- Anthropic (Claude 3.5, Claude 3.7)
- Google (Gemini 2.5, Gemini 2.0, Gemini 3.1)
- DeepSeek
- Antigravity / Modelos futuros

Toda a inteligência e regra de negócio pertencem à arquitetura e ao repositório, jamais aos pesos de um modelo específico.

---

## 16. Encerramento da Arquitetura

Este documento define **apenas a arquitetura mestre do sistema**. Ele não define implementação direta de código ou prompts.

A implementação oficial encontra-se estritamente desdobrada em:
1. `MASTER_IMPLEMENTATION_PLAN.md`
2. `DESIGN_SYSTEM_SPECIFICATION.md`
3. `AGENT_SPECIFICATIONS.md`

Qualquer alteração arquitetural futura deverá ser refletida neste documento antes de ser replicada nos documentos de implementação.

---

## 17. Referências

Toda a arquitetura do EOS se ancora estritamente nos seguintes documentos oficiais do projeto High House:

- **01_FUNDACAO_DA_MARCA:** `brand-foundation.md`, `brand-essence.md`, `valores-e-principios.md`
- **03_ESTRATEGIA:** `posicionamento.md`, `proposta-de-valor.md`, `primeiro-sistema-de-conteudo.md`, `estrategia-conteudo-ciclo-1.md`, `protocolo-de-experimentacao.md`
- **04_IDENTIDADE_DA_MARCA:** `personalidade.md`, `voz-e-linguagem.md`, `principios-de-comunicacao.md`
- **05_DIRECAO_CRIATIVA:** `universos-visuais.md`, `materiais-e-texturas.md`
- **06_IDENTIDADE_VISUAL:** `identidade-visual-minima-viavel.md`, `brand-guidelines.md`
- **00_GESTAO_DO_PROJETO:** `ROADMAP.md`, `recursos-e-restricoes-do-fundador.md`