---
id: DOC-PO-109
doc_type: system-doc
title: "PO_AGENTS_V — Compradores (Agentes de Compras)"
system: Oracle Fusion Cloud ERP
module: Procurement
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - procurement
  - data-dictionary
  - compradores
  - buyers
  - agents
aliases:
  - PO_AGENTS_V
  - po_agents_v
  - po-agents-v
  - po-agents
  - compradores-(agentes-de-compras)
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_AGENTS_V

## 📌 Visão Geral

View que expoe os **compradores (agents)** cadastrados no modulo Procurement. Consolida informacoes de funcionarios habilitados como compradores, com limites de autorizacao e categorias atribuidas.

> [!note] Sufixo _V
> O sufixo `_V` indica que este objeto e uma **view**, projetada para simplificar consultas.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Identificacao:** Lista de funcionarios autorizados a criar/aprovar POs.
- **Validacao de limites:** Verificacao de limites de autorizacao.
- **Atribuicao de POs:** Associacao automatica a ordens de compra.
- **Relatorios de produtividade:** Volume de compras por comprador.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | AGENT_ID | NUMBER(18) | NOT NULL | PK | ID do comprador | — | 🟢 95% |
| 2 | AGENT_NAME | VARCHAR2(360) | NULL | Dados | Nome do comprador | — | 🟢 95% |
| 3 | BUYER_CODE | VARCHAR2(30) | NULL | Identificacao | Codigo do comprador | — | 🟡 75% |
| 4 | PERSON_ID | NUMBER(18) | NULL | FK | Funcionario HCM | [[per_all_people_f]] | 🟢 90% |
| 5 | START_DATE_ACTIVE | DATE | NULL | Data | Inicio da atividade | — | 🟢 85% |
| 6 | END_DATE_ACTIVE | DATE | NULL | Data | Termino da atividade | — | 🟢 85% |
| 7 | AUTHORIZATION_LIMIT | NUMBER | NULL | Financeiro | Limite monetario | — | 🟡 80% |
| 8 | CATEGORY_ID | NUMBER(18) | NULL | FK | Categoria atribuida | [[egp_categories_b]] | 🟡 70% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa física que atua como comprador)
- [[egp_categories_b]] — via `CATEGORY_ID` (categoria padrão do comprador)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Compradores ativos
```sql
SELECT AGENT_ID, AGENT_NAME, AUTHORIZATION_LIMIT
FROM   PO_AGENTS_V
WHERE  (END_DATE_ACTIVE IS NULL OR END_DATE_ACTIVE > SYSDATE);
```

---

## 🔒 Observações

- O `AGENT_ID` e referenciado em `PO_HEADERS_ALL`.
- View sem indices proprios.
- Limites combinados com regras de aprovacao para controle de alcada.

---

## 🔗 PVOs Relacionados

### [[allbuyerpvo|AllBuyerPVO]] (PO · BICC: 1/1)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGENT_ID | AgentId | ✅ |

### [[poagentpvo|PoAgentPVO]] (PO · BICC: 1/1)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGENT_ID | AgentId | ✅ |

---

## 📚 Referências

- [Oracle Docs — PO_AGENTS_V](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
