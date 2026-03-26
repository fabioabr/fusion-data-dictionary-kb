---
id: DOC-PO-135
doc_type: system-doc
title: "PO_LINE_LOCATIONS_DRAFT_ALL — Schedules de Entrega em Rascunho"
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
  - PO_LINE_LOCATIONS_DRAFT_ALL
  - po_line_locations_draft_all
  - po-line-locations-draft-all
  - po-line
  - schedules-de-entrega-em-rascunho
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_LINE_LOCATIONS_DRAFT_ALL

## 📌 Visão Geral

Armazena os **schedules de POs em rascunho**. Estrutura espelha `PO_LINE_LOCATIONS_ALL`.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` e necessario para consultas por organizacao especifica.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Edicao:** Schedules de POs em elaboracao.
- **Amendments:** Alteracoes de schedules durante emendas.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LINE_LOCATION_ID | NUMBER(18) | NOT NULL | PK | ID do schedule | — | 🟢 95% |
| 2 | DRAFT_ID | NUMBER(18) | NOT NULL | PK | ID do draft | [[po_headers_draft_all]] | 🟢 95% |
| 3 | PO_HEADER_ID | NUMBER(18) | NOT NULL | FK | Cabecalho | [[po_headers_draft_all]] | 🟢 95% |
| 4 | PO_LINE_ID | NUMBER(18) | NOT NULL | FK | Linha | [[po_lines_draft_all]] | 🟢 95% |
| 5 | SHIPMENT_NUM | NUMBER | NOT NULL | Identificacao | Numero | — | 🟢 100% |
| 6 | QUANTITY | NUMBER | NULL | Quantidade | Quantidade | — | 🟢 100% |
| 7 | NEED_BY_DATE | DATE | NULL | Data | Data de necessidade | — | 🟢 100% |
| 8 | SHIP_TO_LOCATION_ID | NUMBER(18) | NULL | FK | Local de entrega | [[hr_locations]] | 🟢 100% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[po_headers_draft_all]] — via `PO_HEADER_ID`/`DRAFT_ID` (rascunho de PO do shipment draft)
- [[po_lines_draft_all]] — via `PO_LINE_ID` (linha draft à qual o shipment draft pertence)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Schedules de um draft
```sql
SELECT LINE_LOCATION_ID, SHIPMENT_NUM, QUANTITY, NEED_BY_DATE
FROM   PO_LINE_LOCATIONS_DRAFT_ALL
WHERE  PO_HEADER_ID = :p_header_id AND DRAFT_ID = :p_draft_id;
```


---

## 🔒 Observações

- Dados migram para `PO_LINE_LOCATIONS_ALL` apos aprovacao.

---

## 📚 Referências

- [Oracle Docs — PO_LINE_LOCATIONS_DRAFT_ALL](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
