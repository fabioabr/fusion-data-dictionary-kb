---
id: DOC-OTHER-PVO-AssetInvoiceExtractPVO
doc_type: system-doc
title: "AssetInvoiceExtractPVO — PVO Cross-Module"
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
  - AssetInvoiceExtractPVO
  - assetinvoiceextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AssetInvoiceExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Asset Invoice Extract. Acessa as tabelas: FA_ASSET_INVOICES.

**Caminho:** `FscmTopModelAM.FinExtractAM.FaBiccExtractAM.AssetInvoiceExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 120 | 1 | 1 | 63 | 52% |

---

## 🔗 Tabelas Relacionadas

- [[fa_asset_invoices|FA_ASSET_INVOICES]] — 120 atributos (1 PKs, 63 BICC)

---

## ⚙️ Atributos

### [[fa_asset_invoices|FA_ASSET_INVOICES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssetInvoiceApDistributionLineNumber | AP_DISTRIBUTION_LINE_NUMBER | — | ✅ |
| 2 | AssetInvoiceAssetId | ASSET_ID | — | ✅ |
| 3 | AssetInvoiceAssetInvoiceId | ASSET_INVOICE_ID | — | ✅ |
| 4 | AssetInvoiceAttribute1 | ATTRIBUTE1 | — | — |
| 5 | AssetInvoiceAttribute10 | ATTRIBUTE10 | — | — |
| 6 | AssetInvoiceAttribute11 | ATTRIBUTE11 | — | — |
| 7 | AssetInvoiceAttribute12 | ATTRIBUTE12 | — | — |
| 8 | AssetInvoiceAttribute13 | ATTRIBUTE13 | — | — |
| 9 | AssetInvoiceAttribute14 | ATTRIBUTE14 | — | — |
| 10 | AssetInvoiceAttribute15 | ATTRIBUTE15 | — | — |
| 11 | AssetInvoiceAttribute2 | ATTRIBUTE2 | — | — |
| 12 | AssetInvoiceAttribute3 | ATTRIBUTE3 | — | — |
| 13 | AssetInvoiceAttribute4 | ATTRIBUTE4 | — | — |
| 14 | AssetInvoiceAttribute5 | ATTRIBUTE5 | — | — |
| 15 | AssetInvoiceAttribute6 | ATTRIBUTE6 | — | — |
| 16 | AssetInvoiceAttribute7 | ATTRIBUTE7 | — | — |
| 17 | AssetInvoiceAttribute8 | ATTRIBUTE8 | — | — |
| 18 | AssetInvoiceAttribute9 | ATTRIBUTE9 | — | — |
| 19 | AssetInvoiceAttributeCategoryCode | ATTRIBUTE_CATEGORY_CODE | — | — |
| 20 | AssetInvoiceAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 21 | AssetInvoiceAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 22 | AssetInvoiceAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 23 | AssetInvoiceAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 24 | AssetInvoiceAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 25 | AssetInvoiceAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 26 | AssetInvoiceAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 27 | AssetInvoiceAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 28 | AssetInvoiceAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 29 | AssetInvoiceAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 30 | AssetInvoiceBookTypeCode | BOOK_TYPE_CODE | — | ✅ |
| 31 | AssetInvoiceCorpSourceLineId | CORP_SOURCE_LINE_ID | — | ✅ |
| 32 | AssetInvoiceCreateBatchDate | CREATE_BATCH_DATE | — | ✅ |
| 33 | AssetInvoiceCreateBatchId | CREATE_BATCH_ID | — | ✅ |
| 34 | AssetInvoiceCreatedBy | CREATED_BY | — | ✅ |
| 35 | AssetInvoiceCreationDate | CREATION_DATE | — | ✅ |
| 36 | AssetInvoiceDateEffective | DATE_EFFECTIVE | — | ✅ |
| 37 | AssetInvoiceDateIneffective | DATE_INEFFECTIVE | — | ✅ |
| 38 | AssetInvoiceDeletedFlag | DELETED_FLAG | — | ✅ |
| 39 | AssetInvoiceDepreciateInGroupFlag | DEPRECIATE_IN_GROUP_FLAG | — | ✅ |
| 40 | AssetInvoiceDescription | DESCRIPTION | — | ✅ |
| 41 | AssetInvoiceExpenditureOrganizationId | EXPENDITURE_ORGANIZATION_ID | — | ✅ |
| 42 | AssetInvoiceExpenditureTypeId | EXPENDITURE_TYPE_ID | — | ✅ |
| 43 | AssetInvoiceFeederSystemName | FEEDER_SYSTEM_NAME | — | ✅ |
| 44 | AssetInvoiceFixedAssetsCost | FIXED_ASSETS_COST | — | ✅ |
| 45 | AssetInvoiceGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 46 | AssetInvoiceGlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | — |
| 47 | AssetInvoiceGlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | — |
| 48 | AssetInvoiceGlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | — |
| 49 | AssetInvoiceGlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | — |
| 50 | AssetInvoiceGlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | — |
| 51 | AssetInvoiceGlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | — |
| 52 | AssetInvoiceGlobalAttribute16 | GLOBAL_ATTRIBUTE16 | — | — |
| 53 | AssetInvoiceGlobalAttribute17 | GLOBAL_ATTRIBUTE17 | — | — |
| 54 | AssetInvoiceGlobalAttribute18 | GLOBAL_ATTRIBUTE18 | — | — |
| 55 | AssetInvoiceGlobalAttribute19 | GLOBAL_ATTRIBUTE19 | — | — |
| 56 | AssetInvoiceGlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | — |
| 57 | AssetInvoiceGlobalAttribute20 | GLOBAL_ATTRIBUTE20 | — | — |
| 58 | AssetInvoiceGlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | — |
| 59 | AssetInvoiceGlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | — |
| 60 | AssetInvoiceGlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | — |
| 61 | AssetInvoiceGlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | — |
| 62 | AssetInvoiceGlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | — |
| 63 | AssetInvoiceGlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | — |
| 64 | AssetInvoiceGlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | — |
| 65 | AssetInvoiceGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 66 | AssetInvoiceGlobalAttributeDate1 | GLOBAL_ATTRIBUTE_DATE1 | — | — |
| 67 | AssetInvoiceGlobalAttributeDate2 | GLOBAL_ATTRIBUTE_DATE2 | — | — |
| 68 | AssetInvoiceGlobalAttributeDate3 | GLOBAL_ATTRIBUTE_DATE3 | — | — |
| 69 | AssetInvoiceGlobalAttributeDate4 | GLOBAL_ATTRIBUTE_DATE4 | — | — |
| 70 | AssetInvoiceGlobalAttributeDate5 | GLOBAL_ATTRIBUTE_DATE5 | — | — |
| 71 | AssetInvoiceGlobalAttributeNumber1 | GLOBAL_ATTRIBUTE_NUMBER1 | — | — |
| 72 | AssetInvoiceGlobalAttributeNumber2 | GLOBAL_ATTRIBUTE_NUMBER2 | — | — |
| 73 | AssetInvoiceGlobalAttributeNumber3 | GLOBAL_ATTRIBUTE_NUMBER3 | — | — |
| 74 | AssetInvoiceGlobalAttributeNumber4 | GLOBAL_ATTRIBUTE_NUMBER4 | — | — |
| 75 | AssetInvoiceGlobalAttributeNumber5 | GLOBAL_ATTRIBUTE_NUMBER5 | — | — |
| 76 | AssetInvoiceInvoiceDate | INVOICE_DATE | — | ✅ |
| 77 | AssetInvoiceInvoiceDistributionId | INVOICE_DISTRIBUTION_ID | — | ✅ |
| 78 | AssetInvoiceInvoiceId | INVOICE_ID | — | ✅ |
| 79 | AssetInvoiceInvoiceLineDescription | INVOICE_LINE_DESCRIPTION | — | ✅ |
| 80 | AssetInvoiceInvoiceLineNumber | INVOICE_LINE_NUMBER | — | ✅ |
| 81 | AssetInvoiceInvoiceLineType | INVOICE_LINE_TYPE | — | ✅ |
| 82 | AssetInvoiceInvoiceNumber | INVOICE_NUMBER | — | ✅ |
| 83 | AssetInvoiceInvoicePaymentId | INVOICE_PAYMENT_ID | — | ✅ |
| 84 | AssetInvoiceInvoicePaymentNumber | INVOICE_PAYMENT_NUMBER | — | ✅ |
| 85 | AssetInvoiceInvoiceTransactionIdIn | INVOICE_TRANSACTION_ID_IN | — | ✅ |
| 86 | AssetInvoiceInvoiceTransactionIdOut | INVOICE_TRANSACTION_ID_OUT | — | ✅ |
| 87 | AssetInvoiceInvoiceVoucherNumber | INVOICE_VOUCHER_NUMBER | — | ✅ |
| 88 | AssetInvoiceLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 89 | AssetInvoiceLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 90 | AssetInvoiceLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 91 | AssetInvoiceLineTypeLookupCode | LINE_TYPE_LOOKUP_CODE | — | ✅ |
| 92 | AssetInvoiceMaterialIndicatorFlag | MATERIAL_INDICATOR_FLAG | — | ✅ |
| 93 | AssetInvoiceMergeParentMassAdditionsId | MERGE_PARENT_MASS_ADDITIONS_ID | — | ✅ |
| 94 | AssetInvoiceMergedCode | MERGED_CODE | — | ✅ |
| 95 | AssetInvoiceObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 96 | AssetInvoiceParentMassAdditionId | PARENT_MASS_ADDITION_ID | — | ✅ |
| 97 | AssetInvoicePayablesBatchName | PAYABLES_BATCH_NAME | — | ✅ |
| 98 | AssetInvoicePayablesCodeCombinationId | PAYABLES_CODE_COMBINATION_ID | — | ✅ |
| 99 | AssetInvoicePayablesCost | PAYABLES_COST | — | ✅ |
| 100 | AssetInvoicePayablesUnits | PAYABLES_UNITS | — | ✅ |
| 101 | AssetInvoicePoDistributionId | PO_DISTRIBUTION_ID | — | ✅ |
| 102 | AssetInvoicePoNumber | PO_NUMBER | — | ✅ |
| 103 | AssetInvoicePoVendorId | PO_VENDOR_ID | — | ✅ |
| 104 | AssetInvoicePostBatchId | POST_BATCH_ID | — | ✅ |
| 105 | AssetInvoicePriorSourceLineId | PRIOR_SOURCE_LINE_ID | — | ✅ |
| 106 | AssetInvoiceProjectAssetLineId | PROJECT_ASSET_LINE_ID | — | ✅ |
| 107 | AssetInvoiceProjectId | PROJECT_ID | — | ✅ |
| 108 | AssetInvoiceProjectNumber | PROJECT_NUMBER | — | ✅ |
| 109 | AssetInvoiceProjectOrganizationId | PROJECT_ORGANIZATION_ID | — | ✅ |
| 110 | AssetInvoiceProjectTaskNumber | PROJECT_TASK_NUMBER | — | ✅ |
| 111 | AssetInvoiceProjectTxnDocEntryId | PROJECT_TXN_DOC_ENTRY_ID | — | ✅ |
| 112 | AssetInvoiceSourceLineId | SOURCE_LINE_ID | 🔑 | ✅ |
| 113 | AssetInvoiceSplitCode | SPLIT_CODE | — | ✅ |
| 114 | AssetInvoiceSplitMergedCode | SPLIT_MERGED_CODE | — | ✅ |
| 115 | AssetInvoiceSplitParentMassAdditionsId | SPLIT_PARENT_MASS_ADDITIONS_ID | — | ✅ |
| 116 | AssetInvoiceTaskId | TASK_ID | — | ✅ |
| 117 | AssetInvoiceTaskOrganizationId | TASK_ORGANIZATION_ID | — | ✅ |
| 118 | AssetInvoiceUnrevaluedCost | UNREVALUED_COST | — | ✅ |
| 119 | AssetInvoiceVendorName | VENDOR_NAME | — | ✅ |
| 120 | AssetInvoiceVendorNumber | VENDOR_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
