---
id: DOC-PO-148
doc_type: system-doc
title: "RCV_TRANSACTIONS — Transacoes de Recebimento"
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
  - recebimento
  - receiving
  - rcv
aliases:
  - RCV_TRANSACTIONS
  - rcv_transactions
  - rcv-transactions
  - rcv-transactions
  - transacoes-de-recebimento
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# RCV_TRANSACTIONS

## 📌 Visão Geral

Armazena as **transacoes detalhadas de recebimento**. Cada registro e uma transacao individual — recebimento, devolucao, entrega, correcao, inspecao — com quantidade, data e informacoes contabeis.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Recebimento (RECEIVE):** Entrada fisica de mercadorias.
- **Entrega (DELIVER):** Transferencia para destino final.
- **Devolucao (RETURN TO VENDOR):** Devolucao ao fornecedor.
- **Inspecao (ACCEPT/REJECT):** Registro de qualidade.
- **Matching AP:** Base para 3-way/4-way match.
- **Contabilizacao:** Accrual no recebimento.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TRANSACTION_ID | NUMBER(18) | NOT NULL | PK | ID da transacao | — | 🟢 100% |
| 2 | TRANSACTION_TYPE | VARCHAR2(25) | NOT NULL | Classificacao | RECEIVE, DELIVER, RETURN, CORRECT, ACCEPT, REJECT | — | 🟢 100% |
| 3 | TRANSACTION_DATE | DATE | NOT NULL | Data | Data da transacao | — | 🟢 100% |
| 4 | QUANTITY | NUMBER | NOT NULL | Quantidade | Quantidade | — | 🟢 100% |
| 5 | UNIT_OF_MEASURE | VARCHAR2(25) | NULL | Classificacao | UoM | — | 🟢 100% |
| 6 | SHIPMENT_HEADER_ID | NUMBER(18) | NOT NULL | FK | Cabecalho | [[rcv_shipment_headers]] | 🟢 100% |
| 7 | SHIPMENT_LINE_ID | NUMBER(18) | NOT NULL | FK | Linha | [[rcv_shipment_lines]] | 🟢 100% |
| 8 | PO_HEADER_ID | NUMBER(18) | NULL | FK | PO | [[po_headers_all]] | 🟢 100% |
| 9 | PO_LINE_ID | NUMBER(18) | NULL | FK | Linha PO | [[po_lines_all]] | 🟢 100% |
| 10 | PO_LINE_LOCATION_ID | NUMBER(18) | NULL | FK | Schedule | [[po_line_locations_all]] | 🟢 100% |
| 11 | PO_DISTRIBUTION_ID | NUMBER(18) | NULL | FK | Distribuicao | [[po_distributions_all]] | 🟢 100% |
| 12 | PARENT_TRANSACTION_ID | NUMBER(18) | NULL | FK | Transacao pai | [[rcv_transactions]] | 🟢 95% |
| 13 | DESTINATION_TYPE_CODE | VARCHAR2(25) | NULL | Classificacao | INVENTORY, EXPENSE, SHOP FLOOR | — | 🟢 95% |
| 14 | ORGANIZATION_ID | NUMBER(18) | NULL | FK | Organizacao | [[hr_all_organization_units_f]] | 🟢 100% |
| 15 | SUBINVENTORY | VARCHAR2(10) | NULL | Estoque | Sub-inventario | — | 🟢 90% |
| 16 | INSPECTION_STATUS_CODE | VARCHAR2(25) | NULL | Classificacao | ACCEPTED, REJECTED, NOT INSPECTED | — | 🟢 90% |
| 17 | CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Moeda | — | 🟢 90% |
| 18 | CURRENCY_CONVERSION_RATE | NUMBER | NULL | Financeiro | Taxa de cambio | — | 🟢 85% |
| 19 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 20 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 21 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 22 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[rcv_shipment_headers]] — via `SHIPMENT_HEADER_ID` (cabecalho do recebimento da transacao)
- [[rcv_shipment_lines]] — via `SHIPMENT_LINE_ID` (linha do recebimento da transacao)
- [[po_headers_all]] — via `PO_HEADER_ID` (pedido de compra da transacao de recebimento)
- [[po_lines_all]] — via `PO_LINE_ID` (linha do pedido na transacao de recebimento)
- [[po_line_locations_all]] — via `PO_LINE_LOCATION_ID` (local de entrega na transacao de recebimento)
- [[po_distributions_all]] — via `PO_DISTRIBUTION_ID` (distribuicao contabil na transacao de recebimento)
- [[rcv_transactions]] — via `PARENT_TRANSACTION_ID` (auto-referencia)
- [[hr_all_organization_units_f]] — via `ORGANIZATION_ID` (organizacao da transacao de recebimento)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Transacoes de um recebimento
```sql
SELECT TRANSACTION_ID, TRANSACTION_TYPE, TRANSACTION_DATE,
       QUANTITY, DESTINATION_TYPE_CODE
FROM   RCV_TRANSACTIONS
WHERE  SHIPMENT_HEADER_ID = :p_shipment_header_id
ORDER BY TRANSACTION_ID;
```

### Recebimentos contra um PO
```sql
SELECT rt.TRANSACTION_ID, rt.TRANSACTION_TYPE, rt.QUANTITY,
       rt.TRANSACTION_DATE, rsl.ITEM_DESCRIPTION
FROM   RCV_TRANSACTIONS rt
JOIN   RCV_SHIPMENT_LINES rsl ON rt.SHIPMENT_LINE_ID = rsl.SHIPMENT_LINE_ID
WHERE  rt.PO_HEADER_ID = :p_po_header_id
  AND  rt.TRANSACTION_TYPE = 'RECEIVE';
```


---

## 🔒 Observações

- Fluxo tipico: RECEIVE - DELIVER ou RECEIVE - ACCEPT/REJECT - DELIVER.
- O `PARENT_TRANSACTION_ID` vincula transacoes derivadas.
- Transacoes CORRECT permitem ajustar quantidades retroativamente.
- O `DESTINATION_TYPE_CODE` controla destino: INVENTORY, EXPENSE, SHOP FLOOR.
- Tabela de alto volume; indexar por `PO_HEADER_ID`, `SHIPMENT_HEADER_ID`.

---

## 📚 Referências

- [Oracle Docs — RCV_TRANSACTIONS](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/rcvtransactions-10276.html)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
