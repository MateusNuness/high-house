# Editorial Operating System (EOS)

Sistema principal responsável pela orquestração, auditoria e geração dos artefatos da High House.

## Language

**Collection (Coleção/Revista)**:
Um agrupamento narrativo lançado em sequência. Funciona como uma "edição de revista", composta por múltiplos Capítulos.
_Avoid_: Campanha isolada, série de posts

**Chapter (Capítulo)**:
Um bloco temático dentro de uma Coleção (ex: "O Manifesto"). Representa a intenção narrativa principal (descrita no `EditorialBrief`) e é desdobrado em múltiplos Pôsteres (1:N) para publicação sequencial.

**CollectionBrief**:
O contrato de dados (payload) que define uma Coleção inteira. Contém uma lista de `EditorialBriefs` (os Capítulos).

**Poster**:
Uma unidade final de publicação. Uma imagem estática de formato fixo (1080×1350px, portrait 4:5) gerada a partir da renderização de um layout web (HTML/CSS + Fotografia) acompanhada de sua legenda. Vários Pôsteres formam um Capítulo.
_Avoid_: Imagem, post, banner, página web

**Renderer**:
O componente de infraestrutura responsável por compilar artefatos web (HTML/CSS + assets) e convertê-los em uma imagem estática (Poster) usando um navegador headless.

**StructuredLLMAdapter**:
Um adaptador de infraestrutura (deep module) responsável por isolar a execução de LLMs, encapsulando o boilerplate do LangChain, conversão para objetos Pydantic (`with_structured_output`), tratamento de erros e execução do fail-safe fallback. Os Agentes delegam a execução do LLM a ele.

**CollectionHistory**:
Objeto de domínio (deep module) responsável por encapsular o estado acumulado de pôsteres gerados em uma Coleção. Ele abstrai a formatação do contexto narrativo e de contraste estético para os agentes.
_Avoid_: previous_posters, history_list, state list
