# High House — Marca, Cultura & Espaço Físico

> **Princípio Central:** *A High House deve começar pequena o suficiente para ser possível, mas ser construída com uma visão grande o suficiente para um dia se tornar um lugar.*

---

## 📌 Visão Geral do Projeto

A **High House** é uma marca contemporânea de lifestyle, cultura urbana e convivência originada em Niterói (RJ). O projeto combina moda (streetwear), artigos de design & headshop, arte, música e cultura canábica desmistificada, tendo como destino final a criação de um **espaço físico imersivo** em Niterói.

- **Frase Emocional de Comunidade:** *"Vamos na High hoje?"*
- **Estratégia de Expansão:** Identidade e raízes locais em Niterói (RJ), com distribuição e engajamento de alcance nacional via e-commerce e ecossistema digital.
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
│   └── estrategia-conteudo-ciclo-1.md         # Plano tático do Ciclo 1 (50 ideias + 1º post)
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
├── 08_ESPACO_FISICO/           # Conceito arquitetônico, áreas e dinâmica do espaço
│   ├── conceito-do-espaco.md   # Diretrizes arquitetônicas do espaço em Niterói
│   ├── experiencia.md          # Jornada do cliente e atmosfera imersiva
│   ├── areas.md                # Zoneamento do espaço (Lounge, Retail, Bar/Café)
│   └── programacao.md          # Eventos, workshops e ativações culturais
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
   - Define o universo editorial inicial, 3 pilares temáticos, banco com 50 ideias de posts e o roteiro estruturado do primeiro conteúdo para o Instagram.
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
| **11** | Espaço Físico High House | ⏳ Pendente | Escolha de imóvel em Niterói (RJ), projeto arquitetônico, licenças e abertura. |

---

## 🔒 Decisões Estratégicas Consolidadas

1. **Raiz Local (Niterói) + Alcance Nacional (E-Commerce):** A marca fixa sua identidade física em Niterói (RJ), mas constrói sua base comunitária e de vendas em escala nacional via meios digitais.
2. **Acessibilidade Cultural:** A marca recusa a postura de elitismo esnobe. Embora ofereça produtos com alto padrão de design, a linguagem e o ambiente mantêm portas abertas a diferentes perfis.
3. **Cultura Canábica Elegante e Inclusiva:** Abordagem desmistificada e contemporânea da cannabis, evitando clichês visuais estéreis e acolhendo consumidores e não consumidores.
4. **Crescimento Responsável (*Bootstrapping*):** Proibição estrita de contração de dívidas irresponsáveis. Cada etapa deve gerar caixa para financiar o passo seguinte.
5. **Espaço Físico como Destino Final:** O produto de vestuário e headshop é o veículo de conexão inicial; o espaço físico imersivo é o objetivo supremo do projeto.

---

## ❓ Questões em Aberto & Próximas Implementações

As seguintes frentes operacionais e táticas estão atualmente sob análise para deliberação nos próximos ciclos:

1. **Definição do Produto do Drop 0:** Seleção entre camiseta institucional premium, boné em sarja pesada ou acessório exclusivo de headshop.
2. **Modelo de Produção & Fornecedores:** Validação entre confecção própria local em Niterói/RJ vs. modelo *Private Label* parceiro com estamparia em silkscreen.
3. **Plataforma E-Commerce Inicial:** Escolha tecnológica entre Shopify ou Nuvemshop para o lançamento do Drop 0.
4. **Métricas de Corte para Avanço de Fase:** Estabelecimento dos volumes mínimos de salvamentos e compartilhamentos no Instagram necessários para autorizar a produção física do Drop 0.
5. **Localização Física em Niterói:** Estudo preliminar de viabilidade de bairros em Niterói (Icaraí, Centro ou São Francisco) quanto a fluxo, zoneamento e custo de ocupação.

---

## 🎯 Próximos Passos Imediatos

1. ~~Mapear repertório e formulção de hipóteses de mercado~~ ✅
2. ~~Diagnosticar recursos, restrições e perfil do fundador~~ ✅
3. ~~Definir matriz de priorização de oportunidades de negócio~~ ✅
4. ~~Estruturar plano de validação de baixo contato (5 fases)~~ ✅
5. ~~Construir sistema de coleções editoriais (Revistas)~~ ✅
6. ~~Desenvolver Identidade Visual Mínima Viável (MVP Visual)~~ ✅
7. ~~Elaborar Protocolo de Experimentação de Conteúdo~~ ✅
8. ~~Desenhar Estratégia de Conteúdo do Ciclo 1 (50 ideias + 1º post)~~ ✅
9. **Executar o Ciclo 1 do Laboratório de Conteúdo:** Produzir as 10 primeiras lâminas visuais no Figma/Canva e publicar no Instagram.
10. **Avaliar Métricas Qualitativas:** Analisar taxa de retenção, salvamentos e comentários para validar a persona antes de encomendar a produção do Drop 0.

---

*Documentação oficial atualizada em Julho de 2026 — Estrutura completa consolidada para a Fase 2 (Validação e Descoberta de Público).*
