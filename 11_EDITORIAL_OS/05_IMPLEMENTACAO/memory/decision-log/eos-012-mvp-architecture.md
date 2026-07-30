# Decision Log: EOS-012 — MVP Architecture Provisioning

**Date:** 2026-07-30  
**Context:** Inicialização física do motor de IA (`05_IMPLEMENTACAO`) do Editorial OS.  
**Status:** Approved by Architecture Gate.

## Arquitetura Aprovada

Para garantir escalabilidade com dezenas de agentes simultâneos (LangGraph), optou-se por adotar **Domain-Driven Design (DDD)** simplificado (src-layout) em vez de um script monolítico ou de pastas planas.

1. **Gerenciamento de Dependências:** `Poetry` (pyproject.toml) para garantir deterministicamente as versões (LangChain, LangGraph, Pydantic, Structlog).
2. **Separação de Preocupações:**
   - `domain/`: Contém APENAS as tipagens (Pydantic, TypedDict). Onde o estado do grafo (`GlobalState`) e as entradas/saídas dos agentes são estritamente controladas.
   - `application/`: Onde o `LangGraph` orquestra. Ele roteia informações baseado nas validações do domínio.
   - `infrastructure/`: Abstrações (Banco SQLite para Checkpoints, Roteamento de LLMs).
3. **Observabilidade:** Uso de `structlog` desde o Dia 1 para gerar logs JSON compatíveis com tracing.

## Escopo do MVP (Fase 1 Mínima)

Implementado no primeiro commit:
- Estrutura de pastas `src/eos/...`
- `.env.example` e `.gitignore`
- `state.py` (TypedDict e Reducers básicos do LangGraph)
- `orchestrator.py` (Um DAG mínimo com 1 *Dummy Agent*)
- `dummy_agent.py` (Contrato de teste)
- `memory.py` (Wrapper básico do SqliteSaver)
- `telemetry.py` (Setup do Structlog)
- `llm_router.py` (Fábrica mockada de LLMs baseada em *Role*)

## Itens Explicitamente Adiados

Para evitar engenharia excessiva prematura, os seguintes itens não foram implementados nesta fase:
1. **Os 12 Agentes Reais:** Nenhum prompt oficial da marca foi codificado ainda. O `Dummy Agent` apenas valida se o Node transita estado.
2. **Roteamento Real Multi-LLM:** O `ModelRouter` retorna um mock no MVP, postergando chamadas pagas à OpenAI/DeepSeek até a infraestrutura transitar estado com sucesso.
3. **Persistência SQL Completa:** O SqliteSaver está configurado em teoria, mas o fluxo de Human-in-the-loop complexo foi postergado.
4. **Vetorização/RAG:** A leitura da marca será feita inicialmente lendo os Markdowns crus do disco.

## Regra de Ouro Firmada
*"O código Python nunca toma decisões criativas ou de marca; ele apenas roteia o que está aprovado nos documentos oficiais."*
