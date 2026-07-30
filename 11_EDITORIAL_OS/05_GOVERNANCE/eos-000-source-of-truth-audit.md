# EOS-000 — Source of Truth Audit

## Objetivo
Validar que os documentos raiz (01 a 10) não possuem conflitos que prejudiquem a implementação do EOS (Editorial Operating System) e congelar as decisões fundamentais antes da criação das especificações de design e dos contratos dos agentes.

## Documentos auditados
- `01_FUNDACAO_DA_MARCA/brand-essence.md`
- `03_ESTRATEGIA/protocolo-de-experimentacao.md`
- `04_IDENTIDADE_DA_MARCA/voz-e-linguagem.md`
- `06_IDENTIDADE_VISUAL/identidade-visual-minima-viavel.md`
- `06_IDENTIDADE_VISUAL/brand-guidelines.md`

## Matriz de decisão

| Tema | Fonte oficial | Status |
|---|---|---|
| Essência da marca | `01_FUNDACAO_DA_MARCA/brand-essence.md` | OK |
| Valores | `01_FUNDACAO_DA_MARCA/brand-essence.md` | OK |
| Posicionamento e Frase Emocional | `01_FUNDACAO_DA_MARCA/brand-essence.md` | OK |
| Tom de voz e Linguagem | `04_IDENTIDADE_DA_MARCA/voz-e-linguagem.md` | OK |
| Tipografia | `06_IDENTIDADE_VISUAL/identidade-visual-minima-viavel.md` | Resolvido (conflitos de legado) |
| Paleta de cores | `06_IDENTIDADE_VISUAL/identidade-visual-minima-viavel.md` | Resolvido (conflitos de legado) |

## Conflitos encontrados

### Conflito 1: Tipografia
- **Ocorrência:** O documento `06_IDENTIDADE_VISUAL/identidade-visual-minima-viavel.md` define `Space Grotesk` (títulos) e `Inter` (corpo). Porém, documentos mais antigos como o `03_ESTRATEGIA/protocolo-de-experimentacao.md` e artefatos de código base (`apresentacao-v2`) citam `DM Serif Display`.
- **Decisão:** `Space Grotesk` e `Inter` permanecem como tipografias oficiais absolutas.
- **Motivo:** O documento do MVP Visual (06) é a aprovação mais recente para a direção contemporânea da marca. `DM Serif Display` transmite uma aura vintage/clássica que foi abandonada.

### Conflito 2: Paleta de Cores e Atmosfera
- **Ocorrência:** Diretrizes de curadoria antigas e arquivos em `03_ESTRATEGIA` carregam referências à cor `Dourado`, remetendo a "luxo tradicional".
- **Decisão:** Fica abolida a estética de "luxo dourado". A paleta oficial aprovada no MVP Visual passa a ser: Preto Profundo, Off-White Quente, Terracota Suave, Lilás Denso, Verde Água Apagado, Areia Escura.
- **Motivo:** A estética de luxo afasta a sensação de ambiente cultural e acolhedor (a "ausência do tempo"). A marca exige brutalismo contido e não um premium artificial.

## Decisões congeladas

Após a execução da auditoria **EOS-000**, as seguintes âncoras tornam-se inegociáveis para a construção da especificação (03.1 e 04) e implementação:

- **Fontes primárias (Tipografia):** Space Grotesk (Títulos) / Inter (Corpo).
- **Paleta Oficial:**
  - **Primárias:** Preto Profundo, Off-White Quente (fundos e textos base).
  - **Acentos:** Terracota Suave, Lilás Denso (usar 1 acento por peça).
  - **Secundárias experimentais:** Verde Água Apagado, Areia Escura.
- **Direção de Arte / Identidade:** Editorial contemporâneo e Minimalismo Brutalista.
  - **Minimalismo brutalista High House Significa:**
    - Estruturas simples
    - Hierarquia forte
    - Materiais honestos
    - Espaço negativo
    - Ausência de decoração desnecessária
  - **Minimalismo brutalista High House NÃO Significa:**
    - Agressividade visual
    - Caos
    - Excesso tipográfico
    - Bauhaus literal ou brutalismo web dos anos 2000
- **Anti-patterns (Rejeitar terminantemente):**
  - Luxo tradicional / Estética premium dourada.
  - Clichês canábicos (folhas literais, fumaça excessiva, estilo stoner).
  - Vibe hiper-corporativa ou marketing invasivo.
  - Aglomeração de informações (medo do vazio).

## EOS-000.1 — Validação Humana

**Decisões aprovadas:**
- `[x]` Tipografia
- `[x]` Paleta Oficial e Regra de Acentos
- `[x]` Direção visual e Definição do Minimalismo Brutalista
- `[x]` Anti-patterns

**Pendências (Próximos passos após aprovação):**
- `[ ]` Definir escala tipográfica (no 03.1)
- `[ ]` Definir tokens (no 03.1)
- `[ ]` Definir componentes (no 03.1)

*Nota técnica: Estas definições deverão agora alimentar naturalmente o documento `03.1_DESIGN_SYSTEM_SPECIFICATION.md` apenas APÓS o Humano preencher as aprovações acima com `[x]`.*
