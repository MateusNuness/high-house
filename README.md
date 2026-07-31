# High House — Cultura, Convivência & Design

> **Princípio Central:** *A High House deve começar pequena o suficiente para ser possível, mas ser construída com uma visão grande o suficiente para um dia se tornar um lugar.*

---

## 📌 Visão Geral do Projeto

A **High House** é uma marca contemporânea de lifestyle, cultura urbana e convivência. O projeto combina moda (streetwear), artigos de design & headshop, arte, música e cultura canábica desmistificada, tendo como destino final de longo prazo a criação de um **espaço físico imersivo**.

- **Frase Emocional de Comunidade:** *"Vamos na High hoje?"*
- **Território de Marca:** A identidade pública da High House é definida por **cultura, estética e valores** — não por geografia. A origem do projeto (Niterói, RJ) é parte da história de fundo, revelada organicamente para quem mergulha mais fundo na marca.
- **Estratégia de Expansão:** Construção digital-first com alcance nacional via Instagram e e-commerce, sem filtro geográfico na comunicação pública.
- **Fase Atual do Projeto:** **Fase 2 — Validação e Descoberta de Público** (Laboratório de Conteúdo & Experimentação).
- **Modelo de Financiamento:** *Bootstrapping* sustentável por etapas, sem endividamento, em que cada fase financia a seguinte.

---

## ✍️ Convenção de Escrita da Documentação (Regra de Governança)

Este repositório funciona como a **documentação oficial de arquitetura, estratégia e operação do projeto**. É proibido o uso de linguagem informal, instrucional, aconselhamentos ou diálogos típicos de assistentes de IA (ex: *"você deve"*, *"faça isso"*, *"recomendo que"*). Em vez de orientar ações futuras, a documentação **registra rigorosamente o que foi decidido, testado e estruturado**.

Para manter o rigor técnico e institucional, os documentos do repositório adotam quatro perspectivas normativas:

1. **Documentos Estratégicos:** Escrita institucional e objetiva. Utilizados para registrar decisões, hipóteses de mercado, objetivos e diretrizes diretivas (*ex: "A estratégia prioriza...", "O objetivo é..."*). Proibido o uso de 1ª e 2ª pessoas.
2. **Documentos Operacionais:** Manuais técnicos, fluxos de trabalho, checklists e protocolos de experimentação (*ex: "Procedimento", "Entrada", "Saída", "Métrica de Sucesso"*). Estrutura técnica impessoal, sem frases imperativas.
3. **Documentos da Marca:** Empregam a 1ª pessoa do plural (*"nós"*) **exclusivamente** quando expressam a voz direta da marca em manifestos, valores e declarações de posicionamento público.
4. **Documentos do Fundador:** Empregam a 1ª pessoa do singular (*"eu"*) **exclusivamente** para registrar diagnósticos de capacidade, restrições pessoais, orçamento e alocação de tempo do fundador.

---

## 🗂️ Estrutura e Arquitetura do Repositório

Abaixo está a arquitetura completa da documentação e diretórios do projeto:

```
HIGH HOUSE/
│
├── 00_GESTAO_DO_PROJETO/       # Governança operacional, roadmap, decisões e diagnósticos
│   ├── README.md               # Visão geral da gestão do projeto
│   ├── ROADMAP.md              # Mapeamento detalhado das 11 fases do projeto
│   ├── DECISOES.md             # Registro de decisões consolidadas
│   ├── QUESTOES_EM_ABERTO.md   # Mapeamento de pendências e hipóteses não resolvidas
│   └── recursos-e-restricoes-do-fundador.md # Diagnóstico de recursos e limites do fundador
│
├── 01_FUNDACAO_DA_MARCA/       # Propósito, essência e pilares éticos/culturais
│   ├── brand-foundation.md     # Fundação estratégica da marca
│   ├── brand-essence.md        # Essência e promessa central
│   └── valores-e-principios.md # Código de conduta e princípios não negociáveis
│
├── 02_PESQUISA/                # Estudos de repertório, mercado e cultura urbana
│   ├── mercado/                # Hipóteses e análises de mercado (hipoteses-de-mercado.md)
│   ├── concorrentes/           # Mapeamento de concorrência direta e indireta [Em Construção]
│   ├── publico/                # Pesquisas demográficas e comportamentais [Em Construção]
│   ├── cannabis/               # Estudos de cultura canábica e regulamentação [Em Construção]
│   ├── cultura/                # Referências de música, arte e lifestyle [Em Construção]
│   └── moda/                   # Tendências de streetwear e confecção [Em Construção]
│
├── 03_ESTRATEGIA/              # Posicionamento, validação e sistemas de conteúdo
│   ├── posicionamento.md       # Matriz de posicionamento de mercado
│   ├── proposta-de-valor.md    # Arquitetura da proposta de valor
│   ├── publico.md              # Definição preliminar de personas
│   ├── modelo-de-negocio.md    # Estrutura lean inicial
│   ├── plano-de-validacao-de-baixo-contato.md # Estratégia de validação introspectiva (5 fases)
│   ├── primeiro-sistema-de-conteudo.md        # Transição para coleções editoriais (Revistas)
│   ├── protocolo-de-experimentacao.md         # Motor de testes com hipóteses e métricas
│   └── estrategia-conteudo-ciclo-1.md         # Plano tático do Ciclo 1 (Banco de Perguntas + Coleção 001)
│
├── 04_IDENTIDADE_DA_MARCA/     # Personalidade, voz, linguagem e comunicação
│   ├── personalidade.md        # Arquetipia e traços de personalidade da marca
│   ├── voz-e-linguagem.md      # Tom de voz, vocabulário e proibições de linguagem
│   └── principios-de-comunicacao.md # Diretrizes de engajamento e diálogo público
│
├── 05_DIRECAO_CRIATIVA/        # Universos visuais, texturas e referências estéticas
│   ├── universos-visuais.md    # Pilares visuais da marca
│   ├── materiais-e-texturas.md # Diretrizes de materiais têxteis e físicos
│   ├── moodboards/             # Coleção de painéis semânticos [Em Construção]
│   └── referencias/            # Acervo visual de inspiração [Em Construção]
│
├── 06_IDENTIDADE_VISUAL/       # Naming, logo, tipografia, cores e MVP visual
│   ├── brand-guidelines.md     # Diretrizes gerais de marca
│   ├── identidade-visual-minima-viavel.md # Kit visual provisório (Cores, Fontes, Grid)
│   ├── logo/                   # Variações e especificações do logotipo [Em Construção]
│   ├── tipografia/             # Famílias tipográficas oficiais [Em Construção]
│   └── cores/                  # Códigos de cor e regras de aplicação [Em Construção]
│
├── 07_PRODUTOS/                # Linhas de vestuário, headshop e coleções
│   ├── roupas/                 # Modelagens, fichas técnicas de vestuário [Em Construção]
│   ├── headshop/               # Artigos de utilidade e acessórios canábicos [Em Construção]
│   ├── acessorios/             # Pins, bags, bonés e itens de lifestyle [Em Construção]
│   └── colecoes/               # Planejamento de drops e coleções capsule [Em Construção]
│
├── 08_ESPACO_FISICO/           # Visão exploratória de longo prazo (nada definido)
│   ├── conceito-do-espaco.md   # Possibilidades: Café, Bar, Galeria, Studio, Boutique
│   ├── experiencia.md          # Jornada do visitante e dinâmica dia/noite
│   ├── areas.md                # Ideias de áreas (tudo depende de oportunidade)
│   └── programacao.md          # Ideias de programação cultural
│
├── 09_NEGOCIO/                 # Sustentabilidade financeira, receitas e viabilidade
│   ├── modelo-de-negocio.md    # Estrutura financeira resumida
│   ├── clientes.md             # Segmentação financeira de clientes
│   ├── receitas.md             # Fontes de receita projetadas
│   ├── custos.md               # Estrutura de custos fixos e variáveis
│   ├── viabilidade.md          # Análise de viabilidade econômico-financeira
│   └── oportunidades-concretas-e-priorizacao.md # Matriz de priorização de 6 oportunidades
│
├── 10_REFERENCIAS/             # Acervo de pesquisa, livros, marcas e mídias
│   ├── artigos/                # Leituras e artigos de referência [Em Construção]
│   ├── imagens/                # Banco de imagens de referência [Em Construção]
│   ├── livros/                 # Bibliografia de apoio [Em Construção]
│   ├── marcas/                 # Benchmarks de marcas nacionais e globais [Em Construção]
│   └── videos/                 # Material audiovisual de inspiração [Em Construção]
│
├── 11_EDITORIAL_OS/            # Sistema Operacional Editorial autônomo baseado em IA
│   ├── 01_SYSTEM_ARCHITECTURE.md              # Filosofia, pipeline de orquestração e domínios do sistema
│   ├── 02_MASTER_IMPLEMENTATION_PLAN.md       # Roadmap tático estruturado por Fases de Execução
│   ├── 03_BRAND_DESIGN_FOUNDATION.md          # O propósito estético, valores e DNA não-negociável
│   ├── 03.1_DESIGN_SYSTEM_SPECIFICATION.md    # Regras matemáticas, cores, tipografia (Manual de Direção de Arte)
│   ├── 03.2_AGENT_RUNTIME_SPECIFICATION.md    # Mecânica de execução, grafos, state schema e checkpoints
│   ├── 04_AGENT_SPECIFICATIONS.md             # Contratos cognitivos, limites e responsabilidades dos 12 Agentes
│   ├── 04_AGENT_CONTEXTS/                     # Contextos operacionais dedicados por agente (Brand Guardian, etc.)
│   │   └── brand_guardian_context.md          # Contexto do Brand Guardian com critérios APPROVE/REJECT/HUMAN_REVIEW
│   ├── 04.1_AGENT_OPERATIONAL_CONTRACTS.md    # Contratos Pydantic de I/O
│   ├── 04.2_COGNITIVE_WORKFLOWS.md            # Modelo mental e fluxos cognitivos
│   ├── 05_IMPLEMENTACAO/                      # Onde a orquestração e os testes vivem (código real)
│   │   ├── agents/                            # Prompts, contextos e funções de cada um dos 12 agentes
│   │   ├── design_system/                     # HTML/CSS base para renderização (Design System tokenizado)
│   │   ├── memory/                            # Logs de decisões de design, logs empíricos e grafos de memória
│   │   └── runtime/                           # Lógica do LangGraph, estado e LLM Provider Abstraction
│   ├── 06_GOVERNANCE/                         # Documentos de auditoria humana, validação da Fonte de Verdade
│   │   ├── 00_BRAND_DIRECTION_CHANGE_PROPOSAL.md # Proposta de evolução estética e cultural
│   │   └── eos-000-source-of-truth-audit.md   # Auditoria da Fonte de Verdade
│   └── README.md                              # Regras fundamentais de arquitetura para a camada de Inteligência
│
├── apresentacao/               # Brand Deck Conceitual V1 (HTML/CSS responsivo)
├── apresentacao-v2/            # Caderno de Projeto V2 (HTML/CSS editorial responsivo)
├── index.html                  # Portal Hub de entrada para navegação das apresentações
└── README.md                   # Documentação oficial mestre do repositório
```

---

## 🌐 Apresentações de Marca & Portal Web

O repositório conta com uma infraestrutura web em HTML5/CSS3 estilizada para apresentação da marca a parceiros, investidores e comunidade:

### 1. Hub Portal (`index.html`)
- **Descrição:** Página de entrada com estética sóbria e escura (`#0e0e0e`), servindo de menu principal para acessar as versões da apresentação.
- **Localização:** [`index.html`](file:///c:/Users/user/Documents/High%20House/index.html)

### 2. Caderno de Projeto — V2 (`apresentacao-v2/`)
- **Descrição:** Apresentação narrativa em formato editorial/journal (*Brand Deck de Construção*). Transmite transparência sobre o processo, o que foi descoberto nas pesquisas e as perguntas ainda em aberto.
- **Estética:** Tipografia *DM Serif Display* + *Inter*, detalhes em dourado envelhecido (`#c8a96e`), layout editorial responsivo com navegação lateral por seções.
- **Estrutura:** Abertura → O que é → Por que existe → O que já descobrimos → O que ainda não sabemos → O caminho → Referências a estudar → Onde estamos.
- **Localização:** [`apresentacao-v2/index.html`](file:///c:/Users/user/Documents/High%20House/apresentacao-v2/index.html)

### 3. Brand Deck Conceitual — V1 (`apresentacao/`)
- **Descrição:** Apresentação conceitual síntese do objetivo final da marca.
- **Estrutura:** Abertura → O que é → O que defende → Para onde vai → O que faz primeiro → Onde está agora → Convite.
- **Localização:** [`apresentacao/index.html`](file:///c:/Users/user/Documents/High%20House/apresentacao/index.html)

### 🚀 Publicação Automática no GitHub Pages
O repositório está configurado para servir as apresentações via GitHub Pages. Os endpoints públicos ativos são:
- **Portal de Navegação:** `https://mateusnuness.github.io/high-house/`
- **Caderno de Projeto (V2):** `https://mateusnuness.github.io/high-house/apresentacao-v2/`
- **Brand Deck Conceitual (V1):** `https://mateusnuness.github.io/high-house/apresentacao/`

---

## 📄 Detalhamento dos Documentos Estratégicos Recentes

1. **Estratégia de Conteúdo (Ciclo 1):** [`03_ESTRATEGIA/estrategia-conteudo-ciclo-1.md`](file:///c:/Users/user/Documents/High%20House/03_ESTRATEGIA/estrategia-conteudo-ciclo-1.md)
   - Define o universo editorial inicial, pilares temáticos, o Banco de Perguntas e o roteiro estruturado da primeira Coleção (Revista) para o Instagram.
2. **Protocolo de Experimentação e Aprendizado:** [`03_ESTRATEGIA/protocolo-de-experimentacao.md`](file:///c:/Users/user/Documents/High%20House/03_ESTRATEGIA/protocolo-de-experimentacao.md)
   - Motor de validação com 4 hipóteses práticas de engajamento, métricas primárias (salvamentos/compartilhamentos) e restrição de custo zero (R$ 0).
3. **Identidade Visual Mínima Viável (MVP Visual):** [`06_IDENTIDADE_VISUAL/identidade-visual-minima-viavel.md`](file:///c:/Users/user/Documents/High%20House/06_IDENTIDADE_VISUAL/identidade-visual-minima-viavel.md)
   - Kit provisório contendo paleta cromática (`Off-black`, `Preto Profundo`, `Creme Warm`, `Dourado Envelhecido`), fontes (*DM Serif Display*, *Inter*, *DM Mono*), regras de composição e assinatura visual.
4. **Plano de Validação de Baixo Contato:** [`03_ESTRATEGIA/plano-de-validacao-de-baixo-contato.md`](file:///c:/Users/user/Documents/High%20House/03_ESTRATEGIA/plano-de-validacao-de-baixo-contato.md)
   - Metodologia de validação adaptada ao perfil introspectivo do fundador, organizada em 5 fases progressivas e 5 experimentos assíncronos.
5. **Primeiro Sistema de Conteúdo (Coleções Editoriais):** [`03_ESTRATEGIA/primeiro-sistema-de-conteudo.md`](file:///c:/Users/user/Documents/High%20House/03_ESTRATEGIA/primeiro-sistema-de-conteudo.md)
   - Substituição da lógica de posts soltos pelo lançamento de "Revistas/Coleções Editoriais", alinhadas ao princípio de criar experiências imersivas.
6. **Oportunidades Concretas e Priorização:** [`09_NEGOCIO/oportunidades-concretas-e-priorizacao.md`](file:///c:/Users/user/Documents/High%20House/09_NEGOCIO/oportunidades-concretas-e-priorizacao.md)
   - Avaliação de 6 caminhos de negócio por 8 critérios objetivos, recomendando a sequência: *Conteúdo → Drop 0 Vestuário → Headshop Curada → Espaço Físico*.
7. **Recursos e Restrições do Fundador:** [`00_GESTAO_DO_PROJETO/recursos-e-restricoes-do-fundador.md`](file:///c:/Users/user/Documents/High%20House/00_GESTAO_DO_PROJETO/recursos-e-restricoes-do-fundador.md)
   - Mapeamento pragmático das limitações de capital, tempo e energia, estabelecendo regras de blindagem financeira e execução simplificada.

---

## 🚦 Roadmap e Estágio do Projeto (11 Etapas)

| Etapa | Nome da Etapa | Status | Descrição Resumida |
| :--- | :--- | :---: | :--- |
| **01** | Fundação da Marca | ✅ Concluído | Definição da essência, princípios éticos, razão de existir e manifesto. |
| **02** | Pesquisa e Repertório | ✅ Concluído | Mapeamento de mercado, referências de streetwear, headshop e cultura urbana. |
| **03** | Estratégia de Marca | 🔄 Em Andamento | Posicionamento, proposta de valor e definição de personas iniciais. |
| **04** | Modelo de Negócio Inicial | 🔄 Em Andamento | Estruturação de canais digitais, precificação lean e margens brutas. |
| **05** | Direção Criativa | 🔄 Em Andamento | Definição de universos visuais, texturas e linguagem estética. |
| **06** | Identidade Visual | 🔄 Em Andamento | MVP Visual concluído; logo definitivo e brandbook completo em desenvolvimento. |
| **07** | Validação de Mercado (Conteúdo) | 🔄 Em Andamento | Execução do Laboratório de Conteúdo (Ciclo 1) no Instagram sem investimento financeiro. |
| **08** | Desenvolvimento de Produtos (Drop 0) | ⏳ Pendente | Criação e confecção das primeiras peças (camiseta/acessório) pós-validação de audiência. |
| **09** | Operação e Crescimento | ⏳ Pendente | Lançamento do e-commerce oficial, logística nacional e retenção de comunidade. |
| **10** | Acúmulo de Capital | ⏳ Pendente | Formação de reserva financeira dedicada exclusivamente à viabilização da sede física. |
| **11** | Espaço Físico High House | ⏳ Pendente | Seleção de imóvel, projeto arquitetônico, licenças e abertura (localização a ser definida com base na comunidade consolidada). |

---

## 🔒 Decisões Estratégicas Consolidadas

1. **Identidade Territorial em Camadas (Cultura First):** A comunicação pública da marca lidera com cultura, estética e valores — sem filtro geográfico. A origem (Niterói, RJ) é revelada progressivamente como elemento de autenticidade para quem acompanha a marca de perto, e o espaço físico é comunicado apenas quando a comunidade nacional já estiver consolidada. *(Decisão de Julho/2026 — ver modelo de camadas abaixo.)*
2. **Acessibilidade Cultural:** A marca recusa a postura de elitismo esnobe. Embora ofereça produtos com alto padrão de design, a linguagem e o ambiente mantêm portas abertas a diferentes perfis.
3. **Cultura Canábica Elegante e Inclusiva:** Abordagem desmistificada e contemporânea da cannabis, evitando clichês visuais estéreis e acolhendo consumidores e não consumidores.
4. **Crescimento Responsável (*Bootstrapping*):** Proibição estrita de contração de dívidas irresponsáveis. Cada etapa deve gerar caixa para financiar o passo seguinte.
5. **Espaço Físico como Destino Final:** O produto de vestuário e headshop é o veículo de conexão inicial; o espaço físico imersivo é o objetivo supremo do projeto. **Nenhum formato está definido** — as possibilidades em exploração incluem café, bar, galeria de arte com apoio a artistas locais, estúdio musical (High House Studio) e boutique/headshop, em qualquer combinação que a oportunidade concreta permitir. Documentação exploratória em [`08_ESPACO_FISICO/`](file:///c:/Users/user/Documents/High%20House/08_ESPACO_FISICO/).

### 🗺️ Modelo de Camadas de Identidade Territorial

A identidade geográfica da marca opera em quatro camadas progressivas de profundidade, calibradas para maximizar a identificação do público nacional na fase digital sem ocultar a origem autêntica do projeto:

| Camada | Nível | O que aparece | Onde aparece |
| :---: | :--- | :--- | :--- |
| **1** | Vitrine (1º contato) | Lifestyle, estética, cultura, música e valores universais | Feed do Instagram, conteúdo público, anúncios |
| **2** | Bastidor (quem acompanha) | Atmosfera visual urbana/litorânea sem nomear cidade | Stories, making-of, referências visuais |
| **3** | Origem (quem mergulha) | *"Nascida em Niterói"* como fato de autenticidade | Bio, manifesto, About, documentação interna |
| **4** | Destino (longo prazo) | Anúncio do espaço físico em Niterói | Comunicado à comunidade consolidada |

> **Princípio Operacional:** Na Fase 2 (digital-first), a comunicação pública opera exclusivamente nas Camadas 1 e 2. A Camada 3 é acessível a quem busca, mas não é projetada como mensagem principal. A Camada 4 permanece reservada até a viabilização financeira e comunitária do espaço físico.

---

## ❓ Questões em Aberto & Próximas Implementações

As seguintes frentes operacionais e táticas estão atualmente sob análise para deliberação nos próximos ciclos:

1. **Definição do Produto do Drop 0:** Seleção entre camiseta institucional premium, boné em sarja pesada ou acessório exclusivo de headshop.
2. **Modelo de Produção & Fornecedores:** Validação entre confecção própria local vs. modelo *Private Label* parceiro com estamparia em silkscreen.
3. **Plataforma E-Commerce Inicial:** Escolha tecnológica entre Shopify ou Nuvemshop para o lançamento do Drop 0.
4. **Métricas de Corte para Avanço de Fase:** Estabelecimento dos volumes mínimos de salvamentos e compartilhamentos no Instagram necessários para autorizar a produção física do Drop 0.
5. **Localização do Espaço Físico (Longo Prazo):** Estudo preliminar de viabilidade adiado para após a consolidação da comunidade digital nacional — a escolha da cidade/bairro será informada pelo perfil geográfico da base de clientes real.

---

## 🎯 Foco Atual e Próximos Passos

> **Prioridade Imediata (Julho/2026):** Definir o que criar e postar — a primeira coleção editorial no Instagram. A definição do produto físico (Drop 0) acontece somente após a validação de linguagem e audiência no conteúdo digital.

### Etapas Concluídas
1. ~~Mapear repertório e formulação de hipóteses de mercado~~ ✅
2. ~~Diagnosticar recursos, restrições e perfil do fundador~~ ✅
3. ~~Definir matriz de priorização de oportunidades de negócio~~ ✅
4. ~~Estruturar plano de validação de baixo contato (5 fases)~~ ✅
5. ~~Construir sistema de coleções editoriais (Revistas)~~ ✅
6. ~~Desenvolver Identidade Visual Mínima Viável (MVP Visual)~~ ✅
7. ~~Elaborar Protocolo de Experimentação de Conteúdo~~ ✅
8. ~~Desenhar Estratégia de Conteúdo do Ciclo 1 (Banco de Perguntas + Coleção 001)~~ ✅

### Próximos Passos Ativos
9. **Produzir a Coleção 001:** Selecionar as perguntas exploratórias, definir os capítulos da primeira Revista Editorial e produzir as lâminas visuais no Figma.
10. **Publicar e testar no Instagram:** Rodar o Ciclo 1 do Laboratório de Conteúdo e coletar dados reais de engajamento.
11. **Avaliar métricas qualitativas:** Analisar salvamentos, compartilhamentos e comentários para validar a persona e a linguagem visual.
12. **Definir o produto (Drop 0):** Somente após validação — selecionar o formato do primeiro produto físico com base nos dados de audiência.

---

*Documentação oficial atualizada em Julho de 2026 — Fase 2 (Validação e Descoberta de Público). Foco imediato: criação da primeira coleção editorial para o Instagram. Sistema Operacional Editorial: Fase 3 (Governança) concluída — Brand Guardian Agent (EOS-004) implementado com routing condicional LangGraph e fail-secure.*
