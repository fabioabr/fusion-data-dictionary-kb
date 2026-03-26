---
id: DOC-PO-134
doc_type: system-doc
title: "PO_LINE_LOCATIONS_ALL — Schedules de Entrega de PO"
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
  - PO_LINE_LOCATIONS_ALL
  - po_line_locations_all
  - po-line-locations-all
  - po-line
  - schedules-de-entrega-de-po
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_LINE_LOCATIONS_ALL

## 📌 Visão Geral

Armazena os **schedules de entrega** (line locations/shipments) das linhas de PO. Cada schedule define entrega com data, local, quantidade e informacoes de matching.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` e necessario para consultas por organizacao especifica.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Planejamento de entregas:** Datas e locais por linha.
- **Receiving:** Base para recebimento de mercadorias.
- **Invoice matching:** Regras de 2/3/4-way match.
- **Controle de quantidade:** Tolerancias de recebimento e faturamento.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LINE_LOCATION_ID | NUMBER(18) | NOT NULL | PK | ID do schedule | — | 🟢 100% |
| 2 | PO_HEADER_ID | NUMBER(18) | NOT NULL | FK | Cabecalho | [[po_headers_all]] | 🟢 100% |
| 3 | PO_LINE_ID | NUMBER(18) | NOT NULL | FK | Linha | [[po_lines_all]] | 🟢 100% |
| 4 | SHIPMENT_NUM | NUMBER | NOT NULL | Identificacao | Numero do shipment | — | 🟢 100% |
| 5 | QUANTITY | NUMBER | NULL | Quantidade | Quantidade a entregar | — | 🟢 100% |
| 6 | QUANTITY_RECEIVED | NUMBER | NULL | Quantidade | Quantidade recebida | — | 🟢 100% |
| 7 | QUANTITY_BILLED | NUMBER | NULL | Quantidade | Quantidade faturada | — | 🟢 100% |
| 8 | QUANTITY_CANCELLED | NUMBER | NULL | Quantidade | Quantidade cancelada | — | 🟢 100% |
| 9 | NEED_BY_DATE | DATE | NULL | Data | Data de necessidade | — | 🟢 100% |
| 10 | PROMISED_DATE | DATE | NULL | Data | Data prometida | — | 🟢 95% |
| 11 | SHIP_TO_LOCATION_ID | NUMBER(18) | NULL | FK | Local de entrega | [[hr_locations]] | 🟢 100% |
| 12 | MATCH_OPTION | VARCHAR2(25) | NULL | Classificacao | P (PO) ou R (Receipt) | — | 🟢 95% |
| 13 | RECEIPT_REQUIRED_FLAG | VARCHAR2(1) | NULL | Flag | Requer recebimento (3-way) | — | 🟢 90% |
| 14 | INSPECTION_REQUIRED_FLAG | VARCHAR2(1) | NULL | Flag | Requer inspecao (4-way) | — | 🟢 90% |
| 15 | CANCEL_FLAG | VARCHAR2(1) | NULL | Flag | Cancelado | — | 🟢 95% |
| 16 | CLOSED_CODE | VARCHAR2(25) | NULL | Status | Status de fechamento | — | 🟢 100% |
| 17 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit | [[hr_all_organization_units_f]] | 🟢 100% |
| 18 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 19 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 20 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 21 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[po_headers_all]] — via `PO_HEADER_ID` (pedido de compra do shipment)
- [[po_lines_all]] — via `PO_LINE_ID` (linha do PO à qual o shipment pertence)
- [[hr_locations]] — via `SHIP_TO_LOCATION_ID` (local de entrega do shipment)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Schedules de um PO
```sql
SELECT LINE_LOCATION_ID, SHIPMENT_NUM, QUANTITY, QUANTITY_RECEIVED,
       NEED_BY_DATE, SHIP_TO_LOCATION_ID
FROM   PO_LINE_LOCATIONS_ALL
WHERE  PO_HEADER_ID = :p_po_header_id
  AND  NVL(CANCEL_FLAG,'N') = 'N';
```


---

## 🔒 Observações

- `MATCH_OPTION`: P = 2-way (PO), R = 3-way (Receipt).
- `RECEIPT_REQUIRED_FLAG = 'Y'` exige recebimento antes do pagamento.
- `INSPECTION_REQUIRED_FLAG = 'Y'` adiciona 4-way match.
- Filtrar por `ORG_ID` em consultas multi-org.

---

## 📚 Referências

- [Oracle Docs — PO_LINE_LOCATIONS_ALL](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/polinelocationsall-10204.html)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
