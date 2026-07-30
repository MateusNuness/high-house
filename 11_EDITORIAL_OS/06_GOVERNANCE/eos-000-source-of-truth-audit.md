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

## Hierarquia de Fonte de Verdade

Em caso de conflito, a autoridade segue a seguinte prioridade estrutural:
1. Brand Foundation (Raiz 01 a 10)
2. Source of Truth Audit (EOS-000)
3. Design System Specification (03.1)
4. Agent Specifications (04)
5. Experimentações Visuais (05)

Isso evita que referências externas ou sugestões aleatórias da IA sobrescrevam o DNA da marca.

## Decisões congeladas

Após a execução da auditoria **EOS-000**, as seguintes âncoras tornam-se inegociáveis para a construção da especificação (03.1 e 04) e implementação:

- **Sistema Tipográfico:**
  - **Display / Headlines:** Space Grotesk
  - **Body / Text:** Inter
- **Paleta Oficial:**
  - **Primárias:** Preto Profundo, Off-White Quente (fundos e textos base).
  - **Acentos:** Terracota Suave, Lilás Denso.
  - **Regra de Acento:** Cada composição deve possuir no máximo um elemento cromático de destaque. O acento deve reforçar hierarquia, nunca competir com a mensagem.
  - **Cores exploratórias:** Verde Água Apagado, Areia Escura (Uso permitido apenas em experimentações aprovadas).
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
    - Estética industrial fria
    - Aparência de software experimental
    - Interfaces desconfortáveis
- **Anti-patterns (Rejeitar terminantemente):**
  - Luxo tradicional / Estética premium dourada.
  - Clichês canábicos (folhas literais, fumaça excessiva, estilo stoner).
  - Vibe hiper-corporativa ou marketing invasivo.
  - Aglomeração de informações (medo do vazio).

## EOS-000.1 — Validação Humana

**Status:** Approved
**Responsável:** Matheus
**Data:** 2026-07-30

**Decisões aprovadas:**
- `[x]` Tipografia
- `[x]` Paleta Oficial e Regra de Acentos
- `[x]` Direção visual e Definição do Minimalismo Brutalista
- `[x]` Anti-patterns

**Pendências (Próximos passos após aprovação):**
- `[ ]` Definir escala tipográfica (no 03.1)
- `[ ]` Definir tokens (no 03.1)
- `[ ]` Definir componentes (no 03.1)

*Nota técnica: Estas definições deverão agora alimentar naturalmente o documento `03.1_DESIGN_SYSTEM_SPECIFICATION.md`.*
