---
id: DOC-OTHER-PVO-ProjectAssetLinePVO
doc_type: system-doc
title: "ProjectAssetLinePVO — PVO Cross-Module"
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
  - ProjectAssetLinePVO
  - projectassetlinepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectAssetLinePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Asset Line. Acessa as tabelas: FUN_ALL_BUSINESS_UNITS_V, PJC_PRJ_ASSET_LNS_ALL, PJF_PROJECTS_ALL_B.

**Caminho:** `FscmTopModelAM.PjcCapitalAM.ProjectAssetLinePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 49 | 3 | 1 | 16 | 33% |

---

## 🔗 Tabelas Relacionadas

- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 1 atributos
- [[pjc_prj_asset_lns_all|PJC_PRJ_ASSET_LNS_ALL]] — 46 atributos (1 PKs, 16 BICC)
- [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]] — 2 atributos

---

## ⚙️ Atributos

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitPEOBusinessUnitId | BU_ID | — | — |

### [[pjc_prj_asset_lns_all|PJC_PRJ_ASSET_LNS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectAssetLineId | PROJECT_ASSET_LINE_ID | 🔑 | ✅ |
| 2 | ProjectAssetLinePEOAmortizeFlag | AMORTIZE_FLAG | — | — |
| 3 | ProjectAssetLinePEOApDistributionLineNumber | AP_DISTRIBUTION_LINE_NUMBER | — | — |
| 4 | ProjectAssetLinePEOAssetCategoryId | ASSET_CATEGORY_ID | — | — |
| 5 | ProjectAssetLinePEOAssetCostCcid | ASSET_COST_CCID | — | — |
| 6 | ProjectAssetLinePEOCapitalEventId | CAPITAL_EVENT_ID | — | — |
| 7 | ProjectAssetLinePEOCipCcid | CIP_CCID | — | — |
| 8 | ProjectAssetLinePEOCreatedBy | CREATED_BY | — | ✅ |
| 9 | ProjectAssetLinePEOCreationDate | CREATION_DATE | — | ✅ |
| 10 | ProjectAssetLinePEOCurrentAssetCost | CURRENT_ASSET_COST | — | ✅ |
| 11 | ProjectAssetLinePEODescription | DESCRIPTION | — | ✅ |
| 12 | ProjectAssetLinePEOFaPeriodName | FA_PERIOD_NAME | — | ✅ |
| 13 | ProjectAssetLinePEOGlDate | GL_DATE | — | — |
| 14 | ProjectAssetLinePEOInvoiceCreatedBy | INVOICE_CREATED_BY | — | — |
| 15 | ProjectAssetLinePEOInvoiceDate | INVOICE_DATE | — | — |
| 16 | ProjectAssetLinePEOInvoiceDistributionId | INVOICE_DISTRIBUTION_ID | — | — |
| 17 | ProjectAssetLinePEOInvoiceId | INVOICE_ID | — | — |
| 18 | ProjectAssetLinePEOInvoiceLineNumber | INVOICE_LINE_NUMBER | — | — |
| 19 | ProjectAssetLinePEOInvoiceNumber | INVOICE_NUMBER | — | — |
| 20 | ProjectAssetLinePEOInvoiceUpdatedBy | INVOICE_UPDATED_BY | — | — |
| 21 | ProjectAssetLinePEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 22 | ProjectAssetLinePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 23 | ProjectAssetLinePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 24 | ProjectAssetLinePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 25 | ProjectAssetLinePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 26 | ProjectAssetLinePEOLineType | LINE_TYPE | — | ✅ |
| 27 | ProjectAssetLinePEONewMasterFlag | NEW_MASTER_FLAG | — | — |
| 28 | ProjectAssetLinePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 29 | ProjectAssetLinePEOOrgId | ORG_ID | — | — |
| 30 | ProjectAssetLinePEOOriginalAssetCost | ORIGINAL_ASSET_COST | — | ✅ |
| 31 | ProjectAssetLinePEOOriginalAssetId | ORIGINAL_ASSET_ID | — | — |
| 32 | ProjectAssetLinePEOPayablesBatchName | PAYABLES_BATCH_NAME | — | — |
| 33 | ProjectAssetLinePEOPoNumber | PO_NUMBER | — | — |
| 34 | ProjectAssetLinePEOPoVendorId | PO_VENDOR_ID | — | — |
| 35 | ProjectAssetLinePEOProjectAssetId | PROJECT_ASSET_ID | — | ✅ |
| 36 | ProjectAssetLinePEOProjectAssetLineDetailId | PROJECT_ASSET_LINE_DETAIL_ID | — | — |
| 37 | ProjectAssetLinePEOProjectId | PROJECT_ID | — | — |
| 38 | ProjectAssetLinePEORequestId | REQUEST_ID | — | — |
| 39 | ProjectAssetLinePEORetAdjustmentTxnId | RET_ADJUSTMENT_TXN_ID | — | ✅ |
| 40 | ProjectAssetLinePEORetirementCostType | RETIREMENT_COST_TYPE | — | ✅ |
| 41 | ProjectAssetLinePEORevFromProjAssetLineId | REV_FROM_PROJ_ASSET_LINE_ID | — | — |
| 42 | ProjectAssetLinePEORevProjAssetLineId | REV_PROJ_ASSET_LINE_ID | — | ✅ |
| 43 | ProjectAssetLinePEOTaskId | TASK_ID | — | — |
| 44 | ProjectAssetLinePEOTransferRejectionReason | TRANSFER_REJECTION_REASON | — | ✅ |
| 45 | ProjectAssetLinePEOTransferStatusCode | TRANSFER_STATUS_CODE | — | ✅ |
| 46 | ProjectAssetLinePEOVendorNumber | VENDOR_NUMBER | — | — |

### [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectBasePEOProjectId | PROJECT_ID | — | — |
| 2 | ProjectBasePEOProjfuncCurrencyCode | PROJFUNC_CURRENCY_CODE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
