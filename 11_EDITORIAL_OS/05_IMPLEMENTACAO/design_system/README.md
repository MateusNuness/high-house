# High House — Design System Base

Este diretório contém a camada fundamental de primitivas visuais (Tokens) do Editorial Operating System (EOS), conforme ditado pela tarefa **EOS-002**.

## Propósito
Garantir que toda a materialização visual gerada por futuros agentes (Designer, Coder) siga estritamente as restrições da documentação mestre, operando sob uma única fonte da verdade (SSOT).

## Organização e Convenções
Todo o ecossistema visual é governado por um único arquivo centralizado:
- `tokens.css`: Contém **apenas** Custom Properties no `:root`. Nenhuma classe CSS (`.btn`, `.card`) é declarada aqui. 

As convenções de nomenclatura seguem um padrão funcional (ex: `--color-base-black`, `--font-primary`, `--spacing-massive`) e nunca referenciam contextos específicos de uso, garantindo reutilização semântica e escalabilidade.

## Single Source of Truth (SSOT)
Este Design System Base possui apenas um "norte" cognitivo:
👉 **[03.1_DESIGN_SYSTEM_SPECIFICATION.md](../../03.1_DESIGN_SYSTEM_SPECIFICATION.md)**

### Regra de Ouro da Implementação
- Os tokens contidos neste diretório são a **única fonte** que deverá ser utilizada pelos componentes HTML no futuro.
- É estritamente **proibido** utilizar valores hardcoded (ex: `margin: 10px`, `color: #0E0F12`) diretamente no código dos templates e componentes (EOS-003). Qualquer medida ou cor deve obrigatoriamente chamar a variável CSS declarada aqui.
- Nenhuma variável de acento (cor), sombra ou border-radius curvo foi inserida aqui porque não estavam explícitos no documento 03.1. Toda expansão futura de tokens deve primeiro passar pela documentação 03.1.
