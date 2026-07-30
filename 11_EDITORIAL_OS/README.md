# High House — Editorial Operating System (EOS)

O **Editorial Operating System (EOS)** é a camada de inteligência autônoma da High House. Ele atua como um sistema operacional editorial projetado para criar, curar, documentar e evoluir todo o ecossistema de conteúdo da marca.

Diferente de gerar prompts isolados, o EOS opera como uma **agência autônoma**, orquestrando pesquisa, conceituação, design, documentação e uma rigorosa crítica automática.

## 🏗️ Arquitetura do Sistema

O sistema é dividido em diretórios funcionais que representam seus módulos e instâncias de agentes:

- `agents/`: Contém os "System Prompts" e personas de cada agente (Editor-Chefe, Diretor Criativo, Pesquisador, etc.).
- `memory/`: O coração do EOS. Armazena o registro permanente das narrativas, decisões e hipóteses validadas. A IA consulta isso **antes** de criar algo novo.
- `modules/`: Regras de negócio, fluxos de curadoria e o *Review Engine* (Crítica Automática).
- `design_system/`: Repositório de tokens (HTML, CSS, SVG) para renderização de peças de conteúdo e layouts editoriais (evitando o "aspecto Canva").
- `experiments/`: Templates e logs de hipóteses de conteúdo, métricas esperadas e resultados empíricos.
- `logs_and_docs/`: Documentação passiva autogerada (o "porquê" de cada decisão ser tomada).

## 🚀 Fluxo de Trabalho (Workflow)

1. **Gatilho:** Uma nova necessidade de coleção/capítulo é iniciada.
2. **Pesquisa & Memória:** O *Pesquisador* vasculha referências e o `memory/` garante a não contradição com decisões anteriores.
3. **Criação Sequencial:** *Editor-Chefe* estrutura a narrativa ➔ *Diretor Criativo* define a linguagem ➔ *Diretor de Arte* codifica o visual.
4. **Crítica Automática (Review Engine):** O conteúdo passa pela aprovação unânime de todos os agentes especialistas em `modules/review-engine.md`. Reprovações entram em loop de refação.
5. **Aprovação & Documentação:** A peça final é versionada via Git, o relatório de justificativas é salvo em `logs_and_docs/`, e as hipóteses atualizadas em `experiments/`.

---

> **Diretriz Máxima:** Qualidade sobrepõe a velocidade. O EOS recusa conteúdo genérico, estéril, ou que não fortaleça ativamente os princípios arquiteturais da High House estabelecidos na fundação da marca.
