---
id: DOC-PO-133
doc_type: system-doc
title: "PO_LINES_DRAFT_ALL — Linhas de PO em Rascunho"
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
  - PO_LINES_DRAFT_ALL
  - po_lines_draft_all
  - po-lines-draft-all
  - po-lines
  - linhas-de-po-em-rascunho
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_LINES_DRAFT_ALL

## 📌 Visão Geral

Armazena as **linhas de POs em fase de rascunho**. Estrutura espelha `PO_LINES_ALL`.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` e necessario para consultas por organizacao especifica.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Edicao:** Linhas de POs em elaboracao.
- **Amendments:** Linhas alteradas durante emendas.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PO_LINE_ID | NUMBER(18) | NOT NULL | PK | ID da linha | — | 🟢 95% |
| 2 | DRAFT_ID | NUMBER(18) | NOT NULL | PK | ID do draft | [[po_headers_draft_all]] | 🟢 95% |
| 3 | PO_HEADER_ID | NUMBER(18) | NOT NULL | FK | Cabecalho | [[po_headers_draft_all]] | 🟢 95% |
| 4 | LINE_NUM | NUMBER | NOT NULL | Identificacao | Numero | — | 🟢 100% |
| 5 | ITEM_DESCRIPTION | VARCHAR2(240) | NULL | Descritivo | Descricao | — | 🟢 100% |
| 6 | UNIT_PRICE | NUMBER | NULL | Financeiro | Preco | — | 🟢 100% |
| 7 | QUANTITY | NUMBER | NULL | Quantidade | Quantidade | — | 🟢 100% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[po_headers_draft_all]] — via `PO_HEADER_ID`/`DRAFT_ID` (rascunho de PO ao qual a linha draft pertence)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Linhas de um draft
```sql
SELECT PO_LINE_ID, LINE_NUM, ITEM_DESCRIPTION, UNIT_PRICE, QUANTITY
FROM   PO_LINES_DRAFT_ALL
WHERE  PO_HEADER_ID = :p_header_id AND DRAFT_ID = :p_draft_id;
```


---

## 🔒 Observações

- Dados migram para `PO_LINES_ALL` apos aprovacao.
- Estrutura espelha `PO_LINES_ALL`.

---

## 📚 Referências

- [Oracle Docs — PO_LINES_DRAFT_ALL](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
