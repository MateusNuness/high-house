# Template de Experimentos (Motor de Aprendizado)

Todo conteúdo gerado pelo EOS é, na verdade, um **Experimento**. A High House se guia por dados empíricos aliados à alta direção de arte. 

Sempre que a Criação formular um novo Capítulo de conteúdo, este arquivo de log deve ser gerado e salvo em `experiments/`.

## Estrutura do Documento de Experimento

```markdown
# Experimento: [Nome do Experimento - Ex: Tipografia vs Foto IA]
**Data de Criação:** [Data]
**Coleção/Capítulo:** [ID da Narrativa Associada]
**Agente Líder:** [Agente que propôs]

### 1. A Hipótese (Por que estamos fazendo isso?)
- *[Exemplo: Acreditamos que layouts puramente tipográficos (HTML/CSS) com frases introspectivas gerarão 2x mais "Salvamentos" do que imagens hiper-realistas geradas por IA, por soarem mais enigmáticos.]*

### 2. A Métrica de Sucesso (KPI Primário)
- *[Exemplo: Volume de Salvamentos (Saves) e Compartilhamentos nos Stories (Shares).]*
- *Métricas secundárias: Tempo de retenção na leitura.*

### 3. Execução Técnica (Como vamos testar?)
- *[Exemplo: Post formato Carrossel 5 páginas. Cores: Preto Profundo e Dourado. Fonte: DM Serif. Sem imagens.*]

### 4. Resultado Observado (Preenchido pós-publicação)
- *[ ] Aguardando dados.*
- *Engajamento atingido:* 
- *Taxa de conversão do objetivo:*

### 5. Aprendizado / Insights
- *[O que aprendemos com isso? Devemos repetir? Entra para os Anti-Patterns ou para as Decisões Estratégicas?]*
```

## Como o EOS utiliza isso?
Quando o campo 4 e 5 são preenchidos através de análise de métricas pós-publicação, o sistema automaticamente aciona o *Editor-Chefe* para atualizar o arquivo genérico de `aprendizados-empiricos.md` no `Memory Engine`. O ciclo se fecha, tornando a High House mais inteligente e autônoma a cada postagem.
