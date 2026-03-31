---
id: DOC-PO-PVO-NegotiationIotSupplierTransactionExtractPVO
doc_type: system-doc
title: "NegotiationIotSupplierTransactionExtractPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - NegotiationIotSupplierTransactionExtractPVO
  - negotiationiotsuppliertransactionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# NegotiationIotSupplierTransactionExtractPVO

## 📌 Visão Geral

Extrai transações de fornecedores via canais digitais em negociações, capturando interações automatizadas e dados de integração. Suporta análise de adoção de canais digitais no processo de sourcing.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PonBiccExtractAM.NegotiationIotSupplierTransactionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 28 | 1 | 1 | 24 | 86% |

---

## 🔗 Tabelas Relacionadas

- [[pon_iot_supp_trans_ext|PON_IOT_SUPP_TRANS_EXT]] — 28 atributos (1 PKs, 24 BICC)

---

## ⚙️ Atributos

### [[pon_iot_supp_trans_ext|PON_IOT_SUPP_TRANS_EXT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BidHeaderId | BID_HEADER_ID | — | ✅ |
| 2 | BidLineId | BID_LINE_ID | — | ✅ |
| 3 | CategoryDescription | CATEGORY_DESCRIPTION | — | ✅ |
| 4 | CategoryId | CATEGORY_ID | — | ✅ |
| 5 | CategoryName | CATEGORY_NAME | — | ✅ |
| 6 | CreatedBy | CREATED_BY | — | — |
| 7 | CreationDate | CREATION_DATE | — | ✅ |
| 8 | HeaderId | HEADER_ID | — | ✅ |
| 9 | Item | ITEM | — | ✅ |
| 10 | ItemId | ITEM_ID | — | ✅ |
| 11 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | LineDescription | LINE_DESCRIPTION | — | ✅ |
| 15 | LineId | LINE_ID | — | ✅ |
| 16 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | ProjectId | PROJECT_ID | — | ✅ |
| 18 | RecordTimestamp | RECORD_TIMESTAMP | — | ✅ |
| 19 | Source | SOURCE | — | ✅ |
| 20 | SupplierAndSiteId | SUPPLIER_AND_SITE_ID | — | ✅ |
| 21 | SupplierId | SUPPLIER_ID | — | ✅ |
| 22 | SupplierScenario1 | SUPPLIER_SCENARIO1 | — | ✅ |
| 23 | SupplierScenario2 | SUPPLIER_SCENARIO2 | — | ✅ |
| 24 | SupplierScenario3 | SUPPLIER_SCENARIO3 | — | ✅ |
| 25 | SupplierScenario4 | SUPPLIER_SCENARIO4 | — | ✅ |
| 26 | SupplierScenario5 | SUPPLIER_SCENARIO5 | — | ✅ |
| 27 | SupplierSiteId | SUPPLIER_SITE_ID | — | ✅ |
| 28 | SupplierTransactionId | SUPPLIER_TRANSACTION_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
