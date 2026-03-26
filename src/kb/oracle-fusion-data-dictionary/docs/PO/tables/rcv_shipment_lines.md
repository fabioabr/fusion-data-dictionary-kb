---
id: DOC-PO-147
doc_type: system-doc
title: "RCV_SHIPMENT_LINES — Linhas de Recebimento"
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
  - RCV_SHIPMENT_LINES
  - rcv_shipment_lines
  - rcv-shipment-lines
  - rcv-shipment
  - linhas-de-recebimento
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# RCV_SHIPMENT_LINES

## 📌 Visão Geral

Armazena as **linhas de recebimento**. Cada linha vincula um item recebido a uma linha de PO especifica.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Detalhamento:** Itens recebidos com quantidade e PO de referencia.
- **Matching:** Base para 3-way match.
- **Estoque:** Entrada de materiais.
- **Inspecao:** Itens pendentes de inspecao (4-way).

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | SHIPMENT_LINE_ID | NUMBER(18) | NOT NULL | PK | ID da linha | — | 🟢 100% |
| 2 | SHIPMENT_HEADER_ID | NUMBER(18) | NOT NULL | FK | Cabecalho | [[rcv_shipment_headers]] | 🟢 100% |
| 3 | LINE_NUM | NUMBER | NOT NULL | Identificacao | Numero | — | 🟢 100% |
| 4 | PO_HEADER_ID | NUMBER(18) | NULL | FK | PO de referencia | [[po_headers_all]] | 🟢 100% |
| 5 | PO_LINE_ID | NUMBER(18) | NULL | FK | Linha do PO | [[po_lines_all]] | 🟢 100% |
| 6 | PO_LINE_LOCATION_ID | NUMBER(18) | NULL | FK | Schedule | [[po_line_locations_all]] | 🟢 100% |
| 7 | PO_DISTRIBUTION_ID | NUMBER(18) | NULL | FK | Distribuicao | [[po_distributions_all]] | 🟢 95% |
| 8 | ITEM_ID | NUMBER(18) | NULL | FK | Item | [[egp_system_items_b]] | 🟢 100% |
| 9 | ITEM_DESCRIPTION | VARCHAR2(240) | NULL | Descritivo | Descricao do item | — | 🟢 100% |
| 10 | QUANTITY_SHIPPED | NUMBER | NULL | Quantidade | Quantidade enviada | — | 🟢 100% |
| 11 | QUANTITY_RECEIVED | NUMBER | NULL | Quantidade | Quantidade recebida | — | 🟢 100% |
| 12 | UNIT_OF_MEASURE | VARCHAR2(25) | NULL | Classificacao | UoM | — | 🟢 100% |
| 13 | CATEGORY_ID | NUMBER(18) | NULL | FK | Categoria | [[egp_categories_b]] | 🟢 90% |
| 14 | VENDOR_ID | NUMBER(18) | NULL | FK | Fornecedor | [[poz_suppliers]] | 🟢 95% |
| 15 | TO_ORGANIZATION_ID | NUMBER(18) | NULL | FK | Org destino | [[hr_all_organization_units_f]] | 🟢 95% |
| 16 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 17 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 18 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 19 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[rcv_shipment_headers]] — via `SHIPMENT_HEADER_ID` (cabecalho do recebimento)
- [[po_headers_all]] — via `PO_HEADER_ID` (pedido de compra do recebimento)
- [[po_lines_all]] — via `PO_LINE_ID` (linha do pedido de compra recebido)
- [[po_line_locations_all]] — via `PO_LINE_LOCATION_ID` (local de entrega do pedido recebido)
- [[po_distributions_all]] — via `PO_DISTRIBUTION_ID` (distribuicao contabil do pedido recebido)
- [[egp_system_items_b]] — via `ITEM_ID` (item recebido no recebimento)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Linhas recebidas de um PO
```sql
SELECT SHIPMENT_LINE_ID, LINE_NUM, ITEM_DESCRIPTION,
       QUANTITY_SHIPPED, QUANTITY_RECEIVED
FROM   RCV_SHIPMENT_LINES
WHERE  PO_HEADER_ID = :p_po_header_id
ORDER BY LINE_NUM;
```


---

## 🔒 Observações

- Cada linha vincula item recebido a um schedule (LINE_LOCATION_ID).
- A `QUANTITY_RECEIVED` atualiza `PO_LINE_LOCATIONS_ALL`.
- Recebimentos parciais: multiplas transacoes por linha.

---

## 📚 Referências

- [Oracle Docs — RCV_SHIPMENT_LINES](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/rcvshipmentlines-10275.html)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
