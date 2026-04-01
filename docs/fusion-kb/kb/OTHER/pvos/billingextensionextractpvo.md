---
id: DOC-OTHER-PVO-BillingExtensionExtractPVO
doc_type: system-doc
title: "BillingExtensionExtractPVO — PVO Cross-Module"
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
  - BillingExtensionExtractPVO
  - billingextensionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BillingExtensionExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Billing Extension Extract. Acessa as tabelas: PJB_BILLING_EXTENSIONS.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjbBiccExtractAM.BillingExtensionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 40 | 1 | 1 | 24 | 60% |

---

## 🔗 Tabelas Relacionadas

- [[pjb_billing_extensions|PJB_BILLING_EXTENSIONS]] — 40 atributos (1 PKs, 24 BICC)

---

## ⚙️ Atributos

### [[pjb_billing_extensions|PJB_BILLING_EXTENSIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BillingExtensionPEOAfterDraftCreationFlag | AFTER_DRAFT_CREATION_FLAG | — | ✅ |
| 2 | BillingExtensionPEOAmtReqdFlag | AMT_REQD_FLAG | — | ✅ |
| 3 | BillingExtensionPEOAttribute1 | ATTRIBUTE1 | — | — |
| 4 | BillingExtensionPEOAttribute10 | ATTRIBUTE10 | — | — |
| 5 | BillingExtensionPEOAttribute11 | ATTRIBUTE11 | — | — |
| 6 | BillingExtensionPEOAttribute12 | ATTRIBUTE12 | — | — |
| 7 | BillingExtensionPEOAttribute13 | ATTRIBUTE13 | — | — |
| 8 | BillingExtensionPEOAttribute14 | ATTRIBUTE14 | — | — |
| 9 | BillingExtensionPEOAttribute15 | ATTRIBUTE15 | — | — |
| 10 | BillingExtensionPEOAttribute2 | ATTRIBUTE2 | — | — |
| 11 | BillingExtensionPEOAttribute3 | ATTRIBUTE3 | — | — |
| 12 | BillingExtensionPEOAttribute4 | ATTRIBUTE4 | — | — |
| 13 | BillingExtensionPEOAttribute5 | ATTRIBUTE5 | — | — |
| 14 | BillingExtensionPEOAttribute6 | ATTRIBUTE6 | — | — |
| 15 | BillingExtensionPEOAttribute7 | ATTRIBUTE7 | — | — |
| 16 | BillingExtensionPEOAttribute8 | ATTRIBUTE8 | — | — |
| 17 | BillingExtensionPEOAttribute9 | ATTRIBUTE9 | — | — |
| 18 | BillingExtensionPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 19 | BillingExtensionPEOBeforeDeletionFlag | BEFORE_DELETION_FLAG | — | ✅ |
| 20 | BillingExtensionPEOBeforePreProcessFlag | BEFORE_PRE_PROCESS_FLAG | — | ✅ |
| 21 | BillingExtensionPEOBillingExtensionId | BILLING_EXTENSION_ID | 🔑 | ✅ |
| 22 | BillingExtensionPEOBillingExtensionName | BILLING_EXTENSION_NAME | — | ✅ |
| 23 | BillingExtensionPEOCallingProcess | CALLING_PROCESS | — | ✅ |
| 24 | BillingExtensionPEOCreatedBy | CREATED_BY | — | ✅ |
| 25 | BillingExtensionPEOCreationDate | CREATION_DATE | — | ✅ |
| 26 | BillingExtensionPEODefaultCostPlanTypeId | DEFAULT_COST_PLAN_TYPE_ID | — | ✅ |
| 27 | BillingExtensionPEODefaultEventDescription | DEFAULT_EVENT_DESCRIPTION | — | ✅ |
| 28 | BillingExtensionPEODefaultEventTypeId | DEFAULT_EVENT_TYPE_ID | — | ✅ |
| 29 | BillingExtensionPEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 30 | BillingExtensionPEOExtensionDesc | EXTENSION_DESC | — | ✅ |
| 31 | BillingExtensionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 32 | BillingExtensionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 33 | BillingExtensionPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 34 | BillingExtensionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 35 | BillingExtensionPEOPercentageReqdFlag | PERCENTAGE_REQD_FLAG | — | ✅ |
| 36 | BillingExtensionPEOPredefinedFlag | PREDEFINED_FLAG | — | ✅ |
| 37 | BillingExtensionPEOProcedureName | PROCEDURE_NAME | — | ✅ |
| 38 | BillingExtensionPEOProcessingOrder | PROCESSING_ORDER | — | ✅ |
| 39 | BillingExtensionPEOStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 40 | BillingExtensionPEOTrxIndependentFlag | TRX_INDEPENDENT_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
