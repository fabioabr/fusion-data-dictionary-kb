---
id: DOC-PO-131
doc_type: system-doc
title: "PO_HEADERS_DRAFT_ALL — Cabecalhos de PO em Rascunho"
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
  - purchase-orders
  - po-transactions
  - compras
aliases:
  - PO_HEADERS_DRAFT_ALL
  - po_headers_draft_all
  - po-headers-draft-all
  - po-headers
  - cabecalhos-de-po-em-rascunho
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_HEADERS_DRAFT_ALL

## 📌 Visão Geral

Armazena os **cabecalhos de POs em fase de rascunho**. POs sendo criados ou editados antes da submissao.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` e necessario para consultas por organizacao especifica.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Edicao:** POs em elaboracao.
- **Amendments:** Alteracoes antes da re-submissao.
- **Validacao:** Verificacao antes da aprovacao.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PO_HEADER_ID | NUMBER(18) | NOT NULL | PK | ID do cabecalho | — | 🟢 95% |
| 2 | DRAFT_ID | NUMBER(18) | NOT NULL | PK | ID do rascunho | — | 🟢 95% |
| 3 | SEGMENT1 | VARCHAR2(20) | NULL | Identificacao | Numero do PO | — | 🟢 100% |
| 4 | TYPE_LOOKUP_CODE | VARCHAR2(25) | NULL | Classificacao | Tipo | — | 🟢 100% |
| 5 | VENDOR_ID | NUMBER(18) | NULL | FK | Fornecedor | [[poz_suppliers]] | 🟢 100% |
| 6 | AGENT_ID | NUMBER(18) | NULL | FK | Comprador | [[po_agents_v]] | 🟢 95% |
| 7 | CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Moeda | — | 🟢 100% |
| 8 | DRAFT_STATUS | VARCHAR2(25) | NULL | Status | Status do draft | — | 🟢 90% |
| 9 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit | [[hr_all_organization_units_f]] | 🟢 100% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_suppliers]] — via `VENDOR_ID` (fornecedor do rascunho de pedido de compra)
- [[po_agents_v]] — via `AGENT_ID` (comprador do rascunho de pedido de compra)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit do rascunho de pedido de compra)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Drafts em edicao
```sql
SELECT PO_HEADER_ID, DRAFT_ID, SEGMENT1, DRAFT_STATUS
FROM   PO_HEADERS_DRAFT_ALL
WHERE  ORG_ID = :p_org_id AND DRAFT_STATUS = 'DRAFT';
```


---

## 🔒 Observações

- PK composta: `PO_HEADER_ID` + `DRAFT_ID`.
- Dados migram para `PO_HEADERS_ALL` apos aprovacao.
- Drafts abandonados devem ser purgados periodicamente.

---

## 📚 Referências

- [Oracle Docs — PO_HEADERS_DRAFT_ALL](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
