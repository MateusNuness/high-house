# High House — Editorial Operating System (EOS)

O **Editorial Operating System (EOS)** é a camada de inteligência autônoma da High House, estruturada não como um mero gerador de imagens ou textos, mas como uma **agência autônoma baseada na construção sequencial de marca a longo prazo**.

## 🏗️ O Pipeline de 12 Agentes

Todo o fluxo de conteúdo obedece estritamente a este pipeline, impedindo que o Design se inicie antes da Narrativa e que a Publicação ocorra sem o crivo da Marca.

1. **Briefing** (Gatilho)
2. ⬇️ **Research Agent** (Pesquisa repertório)
3. ⬇️ **Curator Agent** (Seleciona e filtra anti-patterns)
4. ⬇️ **Editorial Agent** (Cria a narrativa do capítulo)
5. ⬇️ **Art Director Agent** (Define direção criativa e visual)
6. ⬇️ **Designer Agent** (Estrutura a hierarquia do layout)
7. ⬇️ **Image Agent** (Decide técnica: Foto Real vs IA vs HTML)
8. ⬇️ **Coder Agent** (Implementa HTML/CSS/SVG)
9. ⬇️ **Vision Agent** [Auditoria 1/3] (Renderiza e avalia layout/técnica)
10. ⬇️ **Critic Agent** [Auditoria 2/3] (Avalia originalidade frente ao mercado)
11. ⬇️ **Brand Guardian Agent** [Auditoria 3/3] (Juiz supremo da identidade da marca)
12. ⬇️ **Memory Agent** (Arquiva o processo concluído para a perpetuidade)
13. ⬇️ **Metrics Agent** (Injeta os resultados e hipóteses no motor empírico)
14. **Publish**

## 📂 Arquitetura do Sistema
- `agents/`: System Prompts dos 12 agentes do Pipeline.
- `memory/`: Gerenciado pelo *Memory Agent*, registra o histórico contínuo para evitar contradições.
- `modules/`: Regras de negócio, contendo a Tríade de Auditoria e Curadoria.
- `design_system/`: Repositório de HTML/CSS para consumo do *Coder Agent*.
- `experiments/`: Gerenciado pelo *Metrics Agent*, formaliza os testes.
- `logs_and_docs/`: Rastro documental ativo de loops de revisão e vetos.
