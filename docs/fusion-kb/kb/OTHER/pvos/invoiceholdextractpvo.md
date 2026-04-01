---
id: DOC-OTHER-PVO-InvoiceHoldExtractPVO
doc_type: system-doc
title: "InvoiceHoldExtractPVO — PVO Cross-Module"
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
  - InvoiceHoldExtractPVO
  - invoiceholdextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InvoiceHoldExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Invoice Hold Extract. Acessa as tabelas: AP_HOLDS_ALL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ApBiccExtractAM.InvoiceHoldExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 39 | 1 | 1 | 23 | 59% |

---

## 🔗 Tabelas Relacionadas

- [[ap_holds_all|AP_HOLDS_ALL]] — 39 atributos (1 PKs, 23 BICC)

---

## ⚙️ Atributos

### [[ap_holds_all|AP_HOLDS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApHoldsAllAttribute1 | ATTRIBUTE1 | — | — |
| 2 | ApHoldsAllAttribute10 | ATTRIBUTE10 | — | — |
| 3 | ApHoldsAllAttribute11 | ATTRIBUTE11 | — | — |
| 4 | ApHoldsAllAttribute12 | ATTRIBUTE12 | — | — |
| 5 | ApHoldsAllAttribute13 | ATTRIBUTE13 | — | — |
| 6 | ApHoldsAllAttribute14 | ATTRIBUTE14 | — | — |
| 7 | ApHoldsAllAttribute15 | ATTRIBUTE15 | — | — |
| 8 | ApHoldsAllAttribute2 | ATTRIBUTE2 | — | — |
| 9 | ApHoldsAllAttribute3 | ATTRIBUTE3 | — | — |
| 10 | ApHoldsAllAttribute4 | ATTRIBUTE4 | — | — |
| 11 | ApHoldsAllAttribute5 | ATTRIBUTE5 | — | — |
| 12 | ApHoldsAllAttribute6 | ATTRIBUTE6 | — | — |
| 13 | ApHoldsAllAttribute7 | ATTRIBUTE7 | — | — |
| 14 | ApHoldsAllAttribute8 | ATTRIBUTE8 | — | — |
| 15 | ApHoldsAllAttribute9 | ATTRIBUTE9 | — | — |
| 16 | ApHoldsAllAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 17 | ApHoldsAllConsumptionAdviceLineId | CONSUMPTION_ADVICE_LINE_ID | — | ✅ |
| 18 | ApHoldsAllCreatedBy | CREATED_BY | — | ✅ |
| 19 | ApHoldsAllCreationDate | CREATION_DATE | — | ✅ |
| 20 | ApHoldsAllHeldBy | HELD_BY | — | ✅ |
| 21 | ApHoldsAllHoldDate | HOLD_DATE | — | ✅ |
| 22 | ApHoldsAllHoldDetails | HOLD_DETAILS | — | ✅ |
| 23 | ApHoldsAllHoldId | HOLD_ID | 🔑 | ✅ |
| 24 | ApHoldsAllHoldLookupCode | HOLD_LOOKUP_CODE | — | ✅ |
| 25 | ApHoldsAllHoldReason | HOLD_REASON | — | ✅ |
| 26 | ApHoldsAllInvoiceId | INVOICE_ID | — | ✅ |
| 27 | ApHoldsAllLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 28 | ApHoldsAllLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 29 | ApHoldsAllLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 30 | ApHoldsAllLineLocationId | LINE_LOCATION_ID | — | ✅ |
| 31 | ApHoldsAllLineNumber | LINE_NUMBER | — | ✅ |
| 32 | ApHoldsAllObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 33 | ApHoldsAllOrgId | ORG_ID | — | ✅ |
| 34 | ApHoldsAllRcvTransactionId | RCV_TRANSACTION_ID | — | ✅ |
| 35 | ApHoldsAllReleaseLookupCode | RELEASE_LOOKUP_CODE | — | ✅ |
| 36 | ApHoldsAllReleaseReason | RELEASE_REASON | — | ✅ |
| 37 | ApHoldsAllResponsibilityId | RESPONSIBILITY_ID | — | ✅ |
| 38 | ApHoldsAllStatusFlag | STATUS_FLAG | — | ✅ |
| 39 | ApHoldsAllWfStatus | WF_STATUS | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
