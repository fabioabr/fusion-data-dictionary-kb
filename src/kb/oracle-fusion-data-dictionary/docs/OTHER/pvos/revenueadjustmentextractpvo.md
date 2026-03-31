---
id: DOC-OTHER-PVO-RevenueAdjustmentExtractPVO
doc_type: system-doc
title: "RevenueAdjustmentExtractPVO — PVO Cross-Module"
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
  - RevenueAdjustmentExtractPVO
  - revenueadjustmentextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RevenueAdjustmentExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Revenue Adjustment Extract. Acessa as tabelas: AR_REVENUE_ADJUSTMENTS_ALL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ArBiccExtractAM.RevenueAdjustmentExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 51 | 1 | 1 | 35 | 69% |

---

## 🔗 Tabelas Relacionadas

- [[ar_revenue_adjustments_all|AR_REVENUE_ADJUSTMENTS_ALL]] — 51 atributos (1 PKs, 35 BICC)

---

## ⚙️ Atributos

### [[ar_revenue_adjustments_all|AR_REVENUE_ADJUSTMENTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ArRevenueAdjustmentAmount | AMOUNT | — | ✅ |
| 2 | ArRevenueAdjustmentAmountMode | AMOUNT_MODE | — | ✅ |
| 3 | ArRevenueAdjustmentApplicationDate | APPLICATION_DATE | — | ✅ |
| 4 | ArRevenueAdjustmentAttribute1 | ATTRIBUTE1 | — | — |
| 5 | ArRevenueAdjustmentAttribute10 | ATTRIBUTE10 | — | — |
| 6 | ArRevenueAdjustmentAttribute11 | ATTRIBUTE11 | — | — |
| 7 | ArRevenueAdjustmentAttribute12 | ATTRIBUTE12 | — | — |
| 8 | ArRevenueAdjustmentAttribute13 | ATTRIBUTE13 | — | — |
| 9 | ArRevenueAdjustmentAttribute14 | ATTRIBUTE14 | — | — |
| 10 | ArRevenueAdjustmentAttribute15 | ATTRIBUTE15 | — | — |
| 11 | ArRevenueAdjustmentAttribute2 | ATTRIBUTE2 | — | — |
| 12 | ArRevenueAdjustmentAttribute3 | ATTRIBUTE3 | — | — |
| 13 | ArRevenueAdjustmentAttribute4 | ATTRIBUTE4 | — | — |
| 14 | ArRevenueAdjustmentAttribute5 | ATTRIBUTE5 | — | — |
| 15 | ArRevenueAdjustmentAttribute6 | ATTRIBUTE6 | — | — |
| 16 | ArRevenueAdjustmentAttribute7 | ATTRIBUTE7 | — | — |
| 17 | ArRevenueAdjustmentAttribute8 | ATTRIBUTE8 | — | — |
| 18 | ArRevenueAdjustmentAttribute9 | ATTRIBUTE9 | — | — |
| 19 | ArRevenueAdjustmentAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 20 | ArRevenueAdjustmentComments | COMMENTS | — | ✅ |
| 21 | ArRevenueAdjustmentCreatedBy | CREATED_BY | — | ✅ |
| 22 | ArRevenueAdjustmentCreationDate | CREATION_DATE | — | ✅ |
| 23 | ArRevenueAdjustmentCustomerTrxId | CUSTOMER_TRX_ID | — | ✅ |
| 24 | ArRevenueAdjustmentFromCategoryId | FROM_CATEGORY_ID | — | ✅ |
| 25 | ArRevenueAdjustmentFromCustTrxLineId | FROM_CUST_TRX_LINE_ID | — | ✅ |
| 26 | ArRevenueAdjustmentFromInventoryItemId | FROM_INVENTORY_ITEM_ID | — | ✅ |
| 27 | ArRevenueAdjustmentFromResourceSalesrepId | FROM_RESOURCE_SALESREP_ID | — | ✅ |
| 28 | ArRevenueAdjustmentFromSalesgroupId | FROM_SALESGROUP_ID | — | ✅ |
| 29 | ArRevenueAdjustmentGlDate | GL_DATE | — | ✅ |
| 30 | ArRevenueAdjustmentLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 31 | ArRevenueAdjustmentLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 32 | ArRevenueAdjustmentLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 33 | ArRevenueAdjustmentLineSelectionMode | LINE_SELECTION_MODE | — | ✅ |
| 34 | ArRevenueAdjustmentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 35 | ArRevenueAdjustmentOrgId | ORG_ID | — | ✅ |
| 36 | ArRevenueAdjustmentPercent | PERCENT | — | ✅ |
| 37 | ArRevenueAdjustmentProgramApplicationId | PROGRAM_APPLICATION_ID | — | ✅ |
| 38 | ArRevenueAdjustmentProgramId | PROGRAM_ID | — | ✅ |
| 39 | ArRevenueAdjustmentProgramUpdateDate | PROGRAM_UPDATE_DATE | — | ✅ |
| 40 | ArRevenueAdjustmentReasonCode | REASON_CODE | — | ✅ |
| 41 | ArRevenueAdjustmentRequestId | REQUEST_ID | — | ✅ |
| 42 | ArRevenueAdjustmentRevenueAdjustmentId | REVENUE_ADJUSTMENT_ID | 🔑 | ✅ |
| 43 | ArRevenueAdjustmentRevenueAdjustmentNumber | REVENUE_ADJUSTMENT_NUMBER | — | ✅ |
| 44 | ArRevenueAdjustmentSalesCreditType | SALES_CREDIT_TYPE | — | ✅ |
| 45 | ArRevenueAdjustmentStatus | STATUS | — | ✅ |
| 46 | ArRevenueAdjustmentToCategoryId | TO_CATEGORY_ID | — | ✅ |
| 47 | ArRevenueAdjustmentToCustTrxLineId | TO_CUST_TRX_LINE_ID | — | ✅ |
| 48 | ArRevenueAdjustmentToInventoryItemId | TO_INVENTORY_ITEM_ID | — | ✅ |
| 49 | ArRevenueAdjustmentToResourceSalesrepId | TO_RESOURCE_SALESREP_ID | — | ✅ |
| 50 | ArRevenueAdjustmentToSalesgroupId | TO_SALESGROUP_ID | — | ✅ |
| 51 | ArRevenueAdjustmentType | TYPE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
