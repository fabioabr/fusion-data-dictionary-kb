---
id: DOC-PO-146
doc_type: system-doc
title: "RCV_SHIPMENT_HEADERS — Cabecalhos de Recebimento"
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
  - RCV_SHIPMENT_HEADERS
  - rcv_shipment_headers
  - rcv-shipment-headers
  - rcv-shipment
  - cabecalhos-de-recebimento
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# RCV_SHIPMENT_HEADERS

## 📌 Visão Geral

Armazena os **cabecalhos de recebimento (shipment headers)**. Cada registro representa um recebimento fisico de mercadorias contra POs.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Recebimento:** Entrada de materiais no estoque.
- **Rastreamento logistico:** Shipments, ASNs e transportadoras.
- **3-way matching:** Base para matching PO x Recebimento x Fatura.
- **Relatorios de receiving:** Volumes e lead times.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | SHIPMENT_HEADER_ID | NUMBER(18) | NOT NULL | PK | ID do recebimento | — | 🟢 100% |
| 2 | RECEIPT_NUM | VARCHAR2(30) | NULL | Identificacao | Numero do recebimento | — | 🟢 100% |
| 3 | VENDOR_ID | NUMBER(18) | NULL | FK | Fornecedor | [[poz_suppliers]] | 🟢 100% |
| 4 | VENDOR_SITE_ID | NUMBER(18) | NULL | FK | Site | [[poz_supplier_sites_all_m]] | 🟢 95% |
| 5 | SHIP_TO_ORG_ID | NUMBER(18) | NULL | FK | Org de destino | [[hr_all_organization_units_f]] | 🟢 95% |
| 6 | RECEIPT_SOURCE_CODE | VARCHAR2(25) | NULL | Classificacao | VENDOR, INTERNAL, CUSTOMER | — | 🟢 95% |
| 7 | SHIPMENT_NUM | VARCHAR2(30) | NULL | Identificacao | Numero do shipment (ASN) | — | 🟢 90% |
| 8 | FREIGHT_CARRIER_CODE | VARCHAR2(25) | NULL | Logistica | Transportadora | — | 🟢 85% |
| 9 | BILL_OF_LADING | VARCHAR2(25) | NULL | Logistica | Conhecimento de embarque | — | 🟢 85% |
| 10 | SHIPPED_DATE | DATE | NULL | Data | Data de envio | — | 🟢 90% |
| 11 | EXPECTED_RECEIPT_DATE | DATE | NULL | Data | Data esperada | — | 🟢 90% |
| 12 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 13 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 14 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 15 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_suppliers]] — via `VENDOR_ID` (fornecedor do recebimento)
- [[poz_supplier_sites_all_m]] — via `VENDOR_SITE_ID` (site do fornecedor no recebimento)
- [[hr_all_organization_units_f]] — via `SHIP_TO_ORG_ID` (organizacao destino do recebimento)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Recebimentos de um fornecedor
```sql
SELECT SHIPMENT_HEADER_ID, RECEIPT_NUM, SHIPPED_DATE, CREATION_DATE
FROM   RCV_SHIPMENT_HEADERS
WHERE  VENDOR_ID = :p_vendor_id
ORDER BY CREATION_DATE DESC;
```


---

## 🔒 Observações

- O `RECEIPT_SOURCE_CODE` identifica VENDOR, INTERNAL ou CUSTOMER.
- O `RECEIPT_NUM` e gerado automaticamente.
- ASNs criam o header antes da chegada fisica.
- Cada header pode ter multiplas linhas.

---

## 📚 Referências

- [Oracle Docs — RCV_SHIPMENT_HEADERS](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/rcvshipmentheaders-10274.html)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
