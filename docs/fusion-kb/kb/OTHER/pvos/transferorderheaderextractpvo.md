---
id: DOC-OTHER-PVO-TransferOrderHeaderExtractPVO
doc_type: system-doc
title: "TransferOrderHeaderExtractPVO — PVO Cross-Module"
system: Oracle Fusion Cloud ERP
module: Cross-Module
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - other
  - data-dictionary
  - pvo
  - bicc
aliases:
  - TransferOrderHeaderExtractPVO
  - transferorderheaderextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TransferOrderHeaderExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Transfer Order Header Extract. Acessa as tabelas: INV_TRANSFER_ORDER_HEADERS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.InvBiccExtractAM.TransferOrderHeaderExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 1 | 14 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[inv_transfer_order_headers|INV_TRANSFER_ORDER_HEADERS]] — 14 atributos (1 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[inv_transfer_order_headers|INV_TRANSFER_ORDER_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TOHeaderPEOBudgetControlEnabledFlag | BUDGET_CONTROL_ENABLED_FLAG | — | ✅ |
| 2 | TOHeaderPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | TOHeaderPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | TOHeaderPEODescription | DESCRIPTION | — | ✅ |
| 5 | TOHeaderPEOFulfillOrchestrationRequired | FULFILL_ORCHESTRATION_REQUIRED | — | ✅ |
| 6 | TOHeaderPEOHeaderId | HEADER_ID | 🔑 | ✅ |
| 7 | TOHeaderPEOHeaderNumber | HEADER_NUMBER | — | ✅ |
| 8 | TOHeaderPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | TOHeaderPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | TOHeaderPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | TOHeaderPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | TOHeaderPEOOrderedDate | ORDERED_DATE | — | ✅ |
| 13 | TOHeaderPEOReqBuId | REQ_BU_ID | — | ✅ |
| 14 | TOHeaderPEOSourceTypeLookup | SOURCE_TYPE_LOOKUP | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
