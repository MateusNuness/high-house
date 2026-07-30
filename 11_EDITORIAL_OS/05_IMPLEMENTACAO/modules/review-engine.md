# Review Engine (A Tríade de Auditoria)

O **Review Engine** não é mais um comitê genérico. Ele é uma esteira final rígida composta por três instâncias de auditoria sucessivas. A peça deve superar as três barreiras para ser publicada.

## 🔄 A Tríade de Auditoria

### Passo 1: Auditoria Estética & Funcional
**Responsável:** `Vision Agent`
- Analisa a renderização em tela, screenshots e HTML gerado via *Playwright*.
- **Critérios:**
  - A hierarquia visual está legível?
  - O contraste e os espaçamentos respeitam o grid do Design System?
  - Existem erros técnicos ou acessibilidade falha?
- **Se falhar:** A peça retorna imediatamente para o `Designer Agent` ou `Coder Agent`.

### Passo 2: Auditoria Estratégica & Competitiva
**Responsável:** `Critic Agent`
- Analisa o impacto semântico e a força da peça.
- **Critérios:**
  - A peça parece derivada e facilmente confundida com uma postagem de outra marca (startup, lojinha, influencer)?
  - Há presença de "Anti-Patterns" ou clichês não percebidos anteriormente?
- **Se falhar:** A peça retorna para o `Curator Agent` ou `Art Director Agent` para repensar o impacto e textura.

### Passo 3: Auditoria de Identidade e Essência
**Responsável:** `Brand Guardian Agent`
- Analisa a sobrevivência da peça no longo prazo e alinhamento central.
- **Critérios:**
  - A peça reforça ou dilui a marca?
  - Essa postagem faz sentido como continuação orgânica do capítulo passado?
  - O tom de voz e o rigor de fundação foram mantidos?
- **Se falhar:** Interrupção total. O projeto retorna ao `Editorial Agent` para reformular o *porquê* da postagem existir.

## ❌ Feedback Loop
Cada rejeição produz um relatório de log na pasta `logs_and_docs/`. Um agente nunca aprova por cansaço; se a peça voltar 10 vezes, ela será consertada 10 vezes, mantendo o princípio de **Qualidade acima de Velocidade**.
