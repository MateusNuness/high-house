# 04_AGENT_SPECIFICATIONS.md

> Projeto: High House
> Documento: Agent Specifications
> Versão: 1.1
> Status: Architecture Draft
>
> Este documento mapeia a matriz de agentes (EOS), detalhando o contrato cognitivo, responsabilidade, autoridade, e limites de cada inteligência artificial no sistema.

---

## 1. Visão Geral

Este documento detalha os 12 agentes do EOS. Cada agente possui responsabilidades e autoridades específicas, operando em conjunto para o sistema final. Os agentes não são apenas prompts; eles são componentes de um sistema operando dentro da constituição da marca.

### 1.1 Hierarquia de Agentes (Arquitetura Cognitiva)

Os agentes estão organizados em domínios para facilitar a orquestração estruturada (visando LangGraph):

```text
EOS
│
├── Conhecimento
│   ├── Research
│   └── Curator
│
├── Estratégia
│   ├── Editorial
│   ├── Brand Guardian
│   └── Metrics
│
├── Criação
│   ├── Art Director
│   ├── Designer
│   ├── Image
│   └── Coder
│
├── Validação
│   ├── Critic
│   └── Vision
│
└── Memória
    └── Memory
```

### 1.2 Ordem de Preenchimento (Roadmap)

Para garantir a construção correta das defesas do sistema e propagação das regras, as especificações devem ser preenchidas na seguinte ordem de dependência:

1. **Brand Guardian:** O "sistema imunológico". Define o que passa, o que bloqueia e o que é High House.
2. **Memory Agent:** Todos dependem dele. Define como as decisões são registradas e como o conhecimento retorna.
3. **Art Director:** Traduz as regras estéticas da especificação (03.1).
4. **Designer:** Recebe as regras visuais estruturadas pelo Art Director.
5. **Editorial:** Recebe estratégia e voz.
6. **Research / Curator:** Alimentam o sistema.
7. **Coder / Vision / Image:** Executam as orientações anteriores.
8. **Critic / Metrics:** Fecham o ciclo validando resultados e alimentando hipóteses empíricas.

---

## 2. Template Oficial de Agente

Cada agente deve ser especificado estritamente utilizando a seguinte estrutura de contrato:

```markdown
## 1. Propósito
Por que este agente existe.

## 2. Papel no EOS
Onde ele se encaixa no pipeline.

## 3. Responsabilidade
O que ele decide.

## 4. Não Responsabilidade
O que ele nunca decide.

## 5. Autoridade
Quais decisões pertencem exclusivamente a ele.

## 6. Input Contract
Recebe:
- contexto
- memória
- documentos
- estado atual

## 7. Output Contract
Entrega:
- decisão
- artefato
- recomendação
- memória

## 8. Processo Cognitivo
Como deve raciocinar.

## 9. Ferramentas
Quais ferramentas pode usar.

## 10. MCPs
Integrações externas.

## 11. Regras Permanentes
Restrições imutáveis.

## 12. Anti-patterns
O que deve rejeitar.

## 13. Critérios de Qualidade
Como validar a própria saída.

## 14. Falhas e Recuperação
O que acontece quando falhar.

## 15. Memória Gerada
O que deve salvar.
```

---

## 3. Especificações dos Agentes

### 3.1 Brand Guardian Agent
*(A preencher conforme Template Oficial)*

### 3.2 Memory Agent
*(A preencher conforme Template Oficial)*

### 3.3 Art Director Agent
*(A preencher conforme Template Oficial)*

### 3.4 Designer Agent
*(A preencher conforme Template Oficial)*

### 3.5 Editorial Agent
*(A preencher conforme Template Oficial)*

### 3.6 Research Agent
*(A preencher conforme Template Oficial)*

### 3.7 Curator Agent
*(A preencher conforme Template Oficial)*

### 3.8 Coder Agent
*(A preencher conforme Template Oficial)*

### 3.9 Vision Agent
*(A preencher conforme Template Oficial)*

### 3.10 Image Agent
*(A preencher conforme Template Oficial)*

### 3.11 Critic Agent
*(A preencher conforme Template Oficial)*

### 3.12 Metrics Agent
*(A preencher conforme Template Oficial)*
