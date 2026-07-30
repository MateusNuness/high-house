# Memory Engine (Esquema de Memória Permanente)

O motor de memória garante a linearidade do sistema, servindo como o sistema nervoso de longo prazo da marca.

## 🗂️ Os Mantenedores da Memória

No Pipeline V2 do EOS, **outros agentes não tocam diretamente na gravação da memória**. Essa responsabilidade é isolada:

### 1. The Memory Agent (Arquivista de Narrativas)
Sempre que uma peça supera o `Brand Guardian` e é aprovada, o **Memory Agent** entra em ação e atualiza de forma autônoma os seguintes arquivos:
- `colecoes-anteriores.md`: Insere um resumo executivo de como a peça estendeu a história, para que o capítulo seguinte conheça o capítulo passado.
- `decisoes-estrategicas.md`: Registra se alguma escolha conceitual nova foi tomada e deve virar regra.
- `logs_and_docs/`: Versiona um sumário com todas as hipóteses testadas e referências que foram eliminadas na jornada de aprovação.

### 2. The Metrics Agent (Analista Empírico)
Atua com os dados matemáticos da operação e resultados da comunidade, alimentando:
- `experiments/`: Preenche a performance no template de experimento.
- `aprendizados-empiricos.md`: Isola fatos absolutos gerados pelas métricas (ex: "Peças que não focaram no produto principal tiveram 50% mais compartilhamentos"). 

O `Research Agent` e o `Editorial Agent` sempre realizarão a **leitura** obrigatória dessa memória na fase inicial do próximo pipeline, garantindo a evolução contínua (A = B = C).
