---
id: DOC-PO-140
doc_type: system-doc
title: "PO_ORIG_LINE_LOCATIONS_ALL_V — Localizacoes de Linha Originais (View)"
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
  - PO_ORIG_LINE_LOCATIONS_ALL_V
  - po_orig_line_locations_all_v
  - po-orig-line-locations-all-v
  - po-orig
  - localizacoes-de-linha-originais-(vi
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_ORIG_LINE_LOCATIONS_ALL_V

## 📌 Visão Geral

View com **schedules originais** de PO antes de alteracoes, para comparacao e auditoria.

> [!note] Sufixo _V
> O sufixo `_V` indica que este objeto e uma **view**, projetada para simplificar consultas.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Auditoria:** Comparacao original vs atual.
- **Controle de alteracoes:** Mudancas em datas e quantidades.
- **Compliance:** Evidencia do planejamento original.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LINE_LOCATION_ID | NUMBER(18) | NOT NULL | PK | ID do schedule | — | 🟡 80% |
| 2 | PO_HEADER_ID | NUMBER(18) | NOT NULL | FK | Cabecalho | [[po_headers_all]] | 🟢 90% |
| 3 | PO_LINE_ID | NUMBER(18) | NOT NULL | FK | Linha | [[po_lines_all]] | 🟢 90% |
| 4 | ORIGINAL_QUANTITY | NUMBER | NULL | Quantidade | Quantidade original | — | 🟡 75% |
| 5 | ORIGINAL_NEED_BY_DATE | DATE | NULL | Data | Data original | — | 🟡 75% |
| 6 | ORIGINAL_PROMISED_DATE | DATE | NULL | Data | Data prometida original | — | 🟡 75% |
| 7 | SHIP_TO_LOCATION_ID | NUMBER(18) | NULL | FK | Local original | [[hr_locations]] | 🟢 85% |
| 8 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[po_headers_all]] — via `PO_HEADER_ID` (PO original da view de shipments)
- [[po_lines_all]] — via `PO_LINE_ID` (linha original do PO na view de shipments)

### Tabelas-filha (FK de saída)
- Nenhuma FK de saida identificada

---

## 📎 Uso Típico

### Comparacao original vs atual
```sql
SELECT o.LINE_LOCATION_ID, o.ORIGINAL_QUANTITY, l.QUANTITY AS CURRENT_QTY
FROM   PO_ORIG_LINE_LOCATIONS_ALL_V o
JOIN   PO_LINE_LOCATIONS_ALL l ON o.LINE_LOCATION_ID = l.LINE_LOCATION_ID
WHERE  o.PO_HEADER_ID = :p_po_header_id;
```


---

## 🔒 Observações

- View derivada de tabelas de arquivo/historico.
- Util para relatorios de aderencia ao planejamento.

---

## 📚 Referências

- [Oracle Docs — PO_ORIG_LINE_LOCATIONS_ALL_V](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
