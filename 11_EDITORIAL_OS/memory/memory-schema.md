# Memory Engine (Esquema de Memória Permanente)

O motor de memória (`Memory Engine`) garante que a High House possua um fio condutor ao longo do tempo. Agentes de IA são proibidos de gerar conteúdos novos sem ler o estado atual da memória.

## 🗂️ Estrutura de Registros

A memória é composta por arquivos textuais versionados que atuam como base de contexto longo (Long-Term Context).

### 1. `colecoes-anteriores.md`
- **O que armazena:** Resumo narrativo, tema central e diretrizes visuais de cada coleção já publicada.
- **Objetivo:** Impedir que o *Editor-Chefe* repita temas, clichês ou fure a continuidade cronológica.

### 2. `decisoes-estrategicas.md`
- **O que armazena:** Escolhas definitivas da marca (ex: "Não utilizaremos logotipos gigantes", "Optamos por fotografias reais para a Coleção 2").
- **Objetivo:** Garantir a obediência cega aos vetores da marca pela inteligência artificial.

### 3. `anti-patterns.md` (Integrado à Memória)
- **O que armazena:** O que a High House **não é**. O que ela já testou e reprovou. (ex: estética startup SaaS, visual derivativo do Canva).
- **Objetivo:** Refinar a curadoria. A IA deve auditar seu próprio trabalho cruzando com os anti-patterns.

### 4. `aprendizados-empiricos.md`
- **O que armazena:** Resultados oriundos do `experiments/`. Ex: "Textos curtos retiveram 30% a mais que textões", "HTML renderizado em Preto e Dourado converteu mais salvamentos do que fotos geradas por IA".
- **Objetivo:** A evolução autônoma e paramétrica do estilo da marca.

## ⚙️ Regra de Atualização (Auto-Update)

1. Quando um *Capítulo* ou *Coleção* é aprovado e publicado, um agente deve resumir os dados e injetá-los no `colecoes-anteriores.md`.
2. Após análise de métricas, os insights e taxas de conversão/engajamento entram em `aprendizados-empiricos.md`.
3. O histórico não deve ser apagado, apenas adicionado em formato `Append-Only` (Logs sequenciais), permitindo a rastreabilidade temporal.
