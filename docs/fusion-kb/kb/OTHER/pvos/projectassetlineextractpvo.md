---
id: DOC-OTHER-PVO-ProjectAssetLineExtractPVO
doc_type: system-doc
title: "ProjectAssetLineExtractPVO — PVO Cross-Module"
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
  - ProjectAssetLineExtractPVO
  - projectassetlineextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectAssetLineExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Asset Line Extract. Acessa as tabelas: PJC_PRJ_ASSET_LNS_ALL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjcBiccExtractAM.ProjectAssetLineExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 46 | 1 | 1 | 46 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjc_prj_asset_lns_all|PJC_PRJ_ASSET_LNS_ALL]] — 46 atributos (1 PKs, 46 BICC)

---

## ⚙️ Atributos

### [[pjc_prj_asset_lns_all|PJC_PRJ_ASSET_LNS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjcPrjAssetLnsAllAmortizeFlag | AMORTIZE_FLAG | — | ✅ |
| 2 | PjcPrjAssetLnsAllApDistributionLineNumber | AP_DISTRIBUTION_LINE_NUMBER | — | ✅ |
| 3 | PjcPrjAssetLnsAllAssetCategoryId | ASSET_CATEGORY_ID | — | ✅ |
| 4 | PjcPrjAssetLnsAllAssetCostCcid | ASSET_COST_CCID | — | ✅ |
| 5 | PjcPrjAssetLnsAllCapitalEventId | CAPITAL_EVENT_ID | — | ✅ |
| 6 | PjcPrjAssetLnsAllCipCcid | CIP_CCID | — | ✅ |
| 7 | PjcPrjAssetLnsAllCreatedBy | CREATED_BY | — | ✅ |
| 8 | PjcPrjAssetLnsAllCreationDate | CREATION_DATE | — | ✅ |
| 9 | PjcPrjAssetLnsAllCurrentAssetCost | CURRENT_ASSET_COST | — | ✅ |
| 10 | PjcPrjAssetLnsAllDescription | DESCRIPTION | — | ✅ |
| 11 | PjcPrjAssetLnsAllFaPeriodName | FA_PERIOD_NAME | — | ✅ |
| 12 | PjcPrjAssetLnsAllGlDate | GL_DATE | — | ✅ |
| 13 | PjcPrjAssetLnsAllInvoiceCreatedBy | INVOICE_CREATED_BY | — | ✅ |
| 14 | PjcPrjAssetLnsAllInvoiceDate | INVOICE_DATE | — | ✅ |
| 15 | PjcPrjAssetLnsAllInvoiceDistributionId | INVOICE_DISTRIBUTION_ID | — | ✅ |
| 16 | PjcPrjAssetLnsAllInvoiceId | INVOICE_ID | — | ✅ |
| 17 | PjcPrjAssetLnsAllInvoiceLineNumber | INVOICE_LINE_NUMBER | — | ✅ |
| 18 | PjcPrjAssetLnsAllInvoiceNumber | INVOICE_NUMBER | — | ✅ |
| 19 | PjcPrjAssetLnsAllInvoiceUpdatedBy | INVOICE_UPDATED_BY | — | ✅ |
| 20 | PjcPrjAssetLnsAllJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 21 | PjcPrjAssetLnsAllJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 22 | PjcPrjAssetLnsAllLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 23 | PjcPrjAssetLnsAllLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 24 | PjcPrjAssetLnsAllLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 25 | PjcPrjAssetLnsAllLineType | LINE_TYPE | — | ✅ |
| 26 | PjcPrjAssetLnsAllNewMasterFlag | NEW_MASTER_FLAG | — | ✅ |
| 27 | PjcPrjAssetLnsAllObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 28 | PjcPrjAssetLnsAllOrgId | ORG_ID | — | ✅ |
| 29 | PjcPrjAssetLnsAllOriginalAssetCost | ORIGINAL_ASSET_COST | — | ✅ |
| 30 | PjcPrjAssetLnsAllOriginalAssetId | ORIGINAL_ASSET_ID | — | ✅ |
| 31 | PjcPrjAssetLnsAllPayablesBatchName | PAYABLES_BATCH_NAME | — | ✅ |
| 32 | PjcPrjAssetLnsAllPoNumber | PO_NUMBER | — | ✅ |
| 33 | PjcPrjAssetLnsAllPoVendorId | PO_VENDOR_ID | — | ✅ |
| 34 | PjcPrjAssetLnsAllProjectAssetId | PROJECT_ASSET_ID | — | ✅ |
| 35 | PjcPrjAssetLnsAllProjectAssetLineDetailId | PROJECT_ASSET_LINE_DETAIL_ID | — | ✅ |
| 36 | PjcPrjAssetLnsAllProjectAssetLineId | PROJECT_ASSET_LINE_ID | 🔑 | ✅ |
| 37 | PjcPrjAssetLnsAllProjectId | PROJECT_ID | — | ✅ |
| 38 | PjcPrjAssetLnsAllRequestId | REQUEST_ID | — | ✅ |
| 39 | PjcPrjAssetLnsAllRetAdjustmentTxnId | RET_ADJUSTMENT_TXN_ID | — | ✅ |
| 40 | PjcPrjAssetLnsAllRetirementCostType | RETIREMENT_COST_TYPE | — | ✅ |
| 41 | PjcPrjAssetLnsAllRevFromProjAssetLineId | REV_FROM_PROJ_ASSET_LINE_ID | — | ✅ |
| 42 | PjcPrjAssetLnsAllRevProjAssetLineId | REV_PROJ_ASSET_LINE_ID | — | ✅ |
| 43 | PjcPrjAssetLnsAllTaskId | TASK_ID | — | ✅ |
| 44 | PjcPrjAssetLnsAllTransferRejectionReason | TRANSFER_REJECTION_REASON | — | ✅ |
| 45 | PjcPrjAssetLnsAllTransferStatusCode | TRANSFER_STATUS_CODE | — | ✅ |
| 46 | PjcPrjAssetLnsAllVendorNumber | VENDOR_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
