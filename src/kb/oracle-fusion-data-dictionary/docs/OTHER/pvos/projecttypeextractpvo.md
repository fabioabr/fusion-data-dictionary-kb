---
id: DOC-OTHER-PVO-ProjectTypeExtractPVO
doc_type: system-doc
title: "ProjectTypeExtractPVO — PVO Cross-Module"
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
  - ProjectTypeExtractPVO
  - projecttypeextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectTypeExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Type Extract. Acessa as tabelas: PJF_PROJECT_TYPES_B, PJF_PROJECT_TYPES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.ProjectTypeExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 55 | 2 | 1 | 44 | 80% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_project_types_b|PJF_PROJECT_TYPES_B]] — 44 atributos (1 PKs, 33 BICC)
- [[pjf_project_types_tl|PJF_PROJECT_TYPES_TL]] — 11 atributos (11 BICC)

---

## ⚙️ Atributos

### [[pjf_project_types_b|PJF_PROJECT_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectTypeBasePEOAssetAllocationMethod | ASSET_ALLOCATION_METHOD | — | ✅ |
| 2 | ProjectTypeBasePEOAttribute1 | ATTRIBUTE1 | — | — |
| 3 | ProjectTypeBasePEOAttribute10 | ATTRIBUTE10 | — | — |
| 4 | ProjectTypeBasePEOAttribute2 | ATTRIBUTE2 | — | — |
| 5 | ProjectTypeBasePEOAttribute3 | ATTRIBUTE3 | — | — |
| 6 | ProjectTypeBasePEOAttribute4 | ATTRIBUTE4 | — | — |
| 7 | ProjectTypeBasePEOAttribute5 | ATTRIBUTE5 | — | — |
| 8 | ProjectTypeBasePEOAttribute6 | ATTRIBUTE6 | — | — |
| 9 | ProjectTypeBasePEOAttribute7 | ATTRIBUTE7 | — | — |
| 10 | ProjectTypeBasePEOAttribute8 | ATTRIBUTE8 | — | — |
| 11 | ProjectTypeBasePEOAttribute9 | ATTRIBUTE9 | — | — |
| 12 | ProjectTypeBasePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 13 | ProjectTypeBasePEOBurdenAccountFlag | BURDEN_ACCOUNT_FLAG | — | ✅ |
| 14 | ProjectTypeBasePEOBurdenAmtDisplayMethod | BURDEN_AMT_DISPLAY_METHOD | — | ✅ |
| 15 | ProjectTypeBasePEOBurdenCostFlag | BURDEN_COST_FLAG | — | ✅ |
| 16 | ProjectTypeBasePEOBurdenCostJournalFlag | BURDEN_COST_JOURNAL_FLAG | — | ✅ |
| 17 | ProjectTypeBasePEOBurdenSumDestProjectId | BURDEN_SUM_DEST_PROJECT_ID | — | ✅ |
| 18 | ProjectTypeBasePEOBurdenSumDestTaskId | BURDEN_SUM_DEST_TASK_ID | — | ✅ |
| 19 | ProjectTypeBasePEOCapitalCostTypeCode | CAPITAL_COST_TYPE_CODE | — | ✅ |
| 20 | ProjectTypeBasePEOCapitalEventProcessing | CAPITAL_EVENT_PROCESSING | — | ✅ |
| 21 | ProjectTypeBasePEOCintRateSchId | CINT_RATE_SCH_ID | — | ✅ |
| 22 | ProjectTypeBasePEOCintSchOverrideFlag | CINT_SCH_OVERRIDE_FLAG | — | ✅ |
| 23 | ProjectTypeBasePEOCipGroupingMethodCode | CIP_GROUPING_METHOD_CODE | — | ✅ |
| 24 | ProjectTypeBasePEOCostIndRateSchId | COST_IND_RATE_SCH_ID | — | ✅ |
| 25 | ProjectTypeBasePEOCostSchOverrideFlag | COST_SCH_OVERRIDE_FLAG | — | ✅ |
| 26 | ProjectTypeBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 27 | ProjectTypeBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 28 | ProjectTypeBasePEOEnableBillingFlag | ENABLE_BILLING_FLAG | — | ✅ |
| 29 | ProjectTypeBasePEOEnableCapitalizationFlag | ENABLE_CAPITALIZATION_FLAG | — | ✅ |
| 30 | ProjectTypeBasePEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 31 | ProjectTypeBasePEOInterfaceAssetCostCode | INTERFACE_ASSET_COST_CODE | — | ✅ |
| 32 | ProjectTypeBasePEOInterfaceCompleteAssetFlag | INTERFACE_COMPLETE_ASSET_FLAG | — | ✅ |
| 33 | ProjectTypeBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 34 | ProjectTypeBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 35 | ProjectTypeBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 36 | ProjectTypeBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 37 | ProjectTypeBasePEOOverrideAssetAssignmentFlag | OVERRIDE_ASSET_ASSIGNMENT_FLAG | — | ✅ |
| 38 | ProjectTypeBasePEOProjectTypeId | PROJECT_TYPE_ID | 🔑 | ✅ |
| 39 | ProjectTypeBasePEOSetId | SET_ID | — | ✅ |
| 40 | ProjectTypeBasePEOSponsoredFlag | SPONSORED_FLAG | — | ✅ |
| 41 | ProjectTypeBasePEOStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 42 | ProjectTypeBasePEOTotalBurdenedJournalFlag | TOTAL_BURDENED_JOURNAL_FLAG | — | ✅ |
| 43 | ProjectTypeBasePEOVendorInvoiceGroupingCode | VENDOR_INVOICE_GROUPING_CODE | — | ✅ |
| 44 | ProjectTypeBasePEOWorkTypeId | WORK_TYPE_ID | — | ✅ |

### [[pjf_project_types_tl|PJF_PROJECT_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectTypeTransLangPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | ProjectTypeTransLangPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | ProjectTypeTransLangPEODescription | DESCRIPTION | — | ✅ |
| 4 | ProjectTypeTransLangPEOLanguage | LANGUAGE | — | ✅ |
| 5 | ProjectTypeTransLangPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ProjectTypeTransLangPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | ProjectTypeTransLangPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ProjectTypeTransLangPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | ProjectTypeTransLangPEOProjectType | PROJECT_TYPE | — | ✅ |
| 10 | ProjectTypeTransLangPEOProjectTypeId | PROJECT_TYPE_ID | — | ✅ |
| 11 | ProjectTypeTransLangPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
