# Editorial Operating System (EOS)

Sistema principal responsável pela orquestração, auditoria e geração dos artefatos da High House.

## Language

**Collection (Coleção/Revista)**:
Um agrupamento narrativo de Pôsteres lançados em sequência. Funciona como uma "edição de revista", com um fio condutor (Manifesto, Banco de Perguntas, etc) orquestrado como um lote (batch).
_Avoid_: Campanha isolada, série de posts

**CollectionBrief**:
O contrato de dados (payload) que define uma Coleção inteira. Contém uma lista de `EditorialBrief` individuais (os Capítulos/Pôsteres) que serão processados pelo orquestrador.

**Poster**:
Uma imagem estática de formato fixo (1080×1350px, portrait 4:5) gerada a partir da renderização de um layout web (HTML/CSS + Fotografia) para publicação direta no feed do Instagram.
_Avoid_: Imagem, post, banner, página web

**Renderer**:
O componente de infraestrutura responsável por compilar artefatos web (HTML/CSS + assets) e convertê-los em uma imagem estática (Poster) usando um navegador headless.
