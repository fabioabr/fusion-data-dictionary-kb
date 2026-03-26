---
id: DOC-PO-129
doc_type: system-doc
title: "PO_HEADERS_ALL — Cabecalhos de Ordens de Compra"
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
  - PO_HEADERS_ALL
  - po_headers_all
  - po-headers-all
  - po-headers
  - cabecalhos-de-ordens-de-compra
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_HEADERS_ALL

## 📌 Visão Geral

Tabela principal que armazena os **cabecalhos de ordens de compra** (Purchase Orders), Blanket Purchase Agreements (BPAs), Contract Purchase Agreements (CPAs) e Planned POs. Tabela-mae da hierarquia PO Header - Lines - Schedules - Distributions.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` e necessario para consultas por organizacao especifica.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Ordens de compra:** Registro de todos os POs.
- **Agreements:** BPA e CPA.
- **Workflow de aprovacao:** Ciclo de vida (draft - aprovado - fechado).
- **Spend management:** Analise de gastos e compliance.
- **Integracao AP:** Referencia para matching de faturas.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PO_HEADER_ID | NUMBER(18) | NOT NULL | PK | ID unico | — | 🟢 100% |
| 2 | SEGMENT1 | VARCHAR2(20) | NOT NULL | Identificacao | Numero do PO | — | 🟢 100% |
| 3 | TYPE_LOOKUP_CODE | VARCHAR2(25) | NOT NULL | Classificacao | STANDARD, BLANKET, CONTRACT, PLANNED | — | 🟢 100% |
| 4 | VENDOR_ID | NUMBER(18) | NULL | FK | Fornecedor | [[poz_suppliers]] | 🟢 100% |
| 5 | VENDOR_SITE_ID | NUMBER(18) | NULL | FK | Site | [[poz_supplier_sites_all_m]] | 🟢 100% |
| 6 | AGENT_ID | NUMBER(18) | NULL | FK | Comprador | [[po_agents_v]] | 🟢 100% |
| 7 | CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Moeda | [[fnd_currencies]] | 🟢 100% |
| 8 | AUTHORIZATION_STATUS | VARCHAR2(25) | NULL | Status | INCOMPLETE, APPROVED, etc. | — | 🟢 100% |
| 9 | APPROVED_FLAG | VARCHAR2(1) | NULL | Flag | Aprovado (Y/N) | — | 🟢 100% |
| 10 | APPROVED_DATE | DATE | NULL | Data | Data de aprovacao | — | 🟢 95% |
| 11 | REVISION_NUM | NUMBER | NULL | Versionamento | Revisao atual | — | 🟢 100% |
| 12 | CANCEL_FLAG | VARCHAR2(1) | NULL | Flag | Cancelado (Y/N) | — | 🟢 95% |
| 13 | CLOSED_CODE | VARCHAR2(25) | NULL | Status | OPEN/CLOSED/FINALLY CLOSED | — | 🟢 100% |
| 14 | FROZEN_FLAG | VARCHAR2(1) | NULL | Flag | Congelado | — | 🟢 90% |
| 15 | BILL_TO_LOCATION_ID | NUMBER(18) | NULL | FK | Local de faturamento | [[hr_locations]] | 🟢 90% |
| 16 | SHIP_TO_LOCATION_ID | NUMBER(18) | NULL | FK | Local de entrega | [[hr_locations]] | 🟢 90% |
| 17 | TERMS_ID | NUMBER(18) | NULL | FK | Condicao de pagamento | [[ap_terms_b]] | 🟢 90% |
| 18 | STYLE_ID | NUMBER(18) | NULL | FK | Estilo de documento | [[po_doc_style_headers]] | 🟢 85% |
| 19 | AMOUNT_LIMIT | NUMBER | NULL | Financeiro | Limite de valor (BPA/CPA) | — | 🟢 90% |
| 20 | START_DATE | DATE | NULL | Data | Inicio (agreements) | — | 🟢 90% |
| 21 | END_DATE | DATE | NULL | Data | Termino (agreements) | — | 🟢 90% |
| 22 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit | [[hr_all_organization_units_f]] | 🟢 100% |
| 23 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 24 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 25 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 26 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_suppliers]] — via `VENDOR_ID` (fornecedor do pedido de compra)
- [[poz_supplier_sites_all_m]] — via `VENDOR_SITE_ID` (site do fornecedor no pedido de compra)
- [[po_agents_v]] — via `AGENT_ID` (comprador responsável pelo pedido de compra)
- [[fnd_currencies]] — via `CURRENCY_CODE` (moeda do pedido de compra)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit do pedido de compra)
- [[po_doc_style_headers]] — via `STYLE_ID` (estilo de documento do pedido de compra)
- [[ap_terms_b]] — via `TERMS_ID` (condição de pagamento do pedido de compra)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### POs aprovados de um fornecedor
```sql
SELECT PO_HEADER_ID, SEGMENT1, TYPE_LOOKUP_CODE, APPROVED_DATE
FROM   PO_HEADERS_ALL
WHERE  VENDOR_ID = :p_vendor_id
  AND  AUTHORIZATION_STATUS = 'APPROVED'
  AND  ORG_ID = :p_org_id;
```

### Agreements ativos
```sql
SELECT PO_HEADER_ID, SEGMENT1, TYPE_LOOKUP_CODE, START_DATE, END_DATE
FROM   PO_HEADERS_ALL
WHERE  TYPE_LOOKUP_CODE IN ('BLANKET','CONTRACT')
  AND  CLOSED_CODE = 'OPEN'
  AND  (END_DATE IS NULL OR END_DATE > SYSDATE);
```


---

## 🔒 Observações

- Tabela mais importante do modulo PO.
- O `TYPE_LOOKUP_CODE` define STANDARD, BLANKET, CONTRACT, PLANNED.
- O `REVISION_NUM` incrementa a cada alteracao aprovada.
- Filtrar por `ORG_ID` em consultas multi-org.

---

## 📚 Referências

- [Oracle Docs — PO_HEADERS_ALL](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/poheadersall-10196.html)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
