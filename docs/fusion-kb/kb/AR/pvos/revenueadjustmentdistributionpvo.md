---
id: DOC-AR-PVO-RevenueAdjustmentDistributionPVO
doc_type: system-doc
title: "RevenueAdjustmentDistributionPVO — PVO Accounts Receivable"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ar
  - data-dictionary
  - pvo
  - bicc
aliases:
  - RevenueAdjustmentDistributionPVO
  - revenueadjustmentdistributionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RevenueAdjustmentDistributionPVO

## 📌 Visão Geral

Extrai as distribuições contábeis dos ajustes de receita, detalhando o impacto por conta do GL, item e organização. Fundamental para auditoria do reconhecimento de receita e conformidade com ASC 606/IFRS 15.

**Caminho:** `FscmTopModelAM.FinArTopPublicModelAM.RevenueAdjustmentDistributionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 112 | 9 | 1 | 34 | 30% |

---

## 🔗 Tabelas Relacionadas

- [[ar_revenue_adjustments_all|AR_REVENUE_ADJUSTMENTS_ALL]] — 35 atributos (14 BICC)
- [[egp_categories_vl|EGP_CATEGORIES_VL]] — 2 atributos (1 BICC)
- [[egp_system_items_vl|EGP_SYSTEM_ITEMS_VL]] — 4 atributos (2 BICC)
- [[fun_bu_perf_v|FUN_BU_PERF_V]] — 1 atributos
- [[gl_ledgers|GL_LEDGERS]] — 2 atributos
- [[hr_all_organization_units_f_vl|HR_ALL_ORGANIZATION_UNITS_F_VL]] — 8 atributos (2 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos (1 BICC)
- [[per_users|PER_USERS]] — 10 atributos
- [[ra_cust_trx_line_gl_dist_all|RA_CUST_TRX_LINE_GL_DIST_ALL]] — 40 atributos (1 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[ar_revenue_adjustments_all|AR_REVENUE_ADJUSTMENTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RevAdjustmentAmount | AMOUNT | — | — |
| 2 | RevAdjustmentAmountMode | AMOUNT_MODE | — | ✅ |
| 3 | RevAdjustmentApplicationDate | APPLICATION_DATE | — | ✅ |
| 4 | RevAdjustmentComments | COMMENTS | — | ✅ |
| 5 | RevAdjustmentCreatedBy | CREATED_BY | — | ✅ |
| 6 | RevAdjustmentCreationDate | CREATION_DATE | — | ✅ |
| 7 | RevAdjustmentCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 8 | RevAdjustmentFromCategoryId | FROM_CATEGORY_ID | — | — |
| 9 | RevAdjustmentFromCustTrxLineId | FROM_CUST_TRX_LINE_ID | — | — |
| 10 | RevAdjustmentFromInventoryItemId | FROM_INVENTORY_ITEM_ID | — | — |
| 11 | RevAdjustmentFromResourceSalesrepId | FROM_RESOURCE_SALESREP_ID | — | — |
| 12 | RevAdjustmentFromSalesgroupId | FROM_SALESGROUP_ID | — | — |
| 13 | RevAdjustmentGlDate | GL_DATE | — | ✅ |
| 14 | RevAdjustmentLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | RevAdjustmentLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | RevAdjustmentLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 17 | RevAdjustmentLineSelectionMode | LINE_SELECTION_MODE | — | — |
| 18 | RevAdjustmentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 19 | RevAdjustmentOrgId | ORG_ID | — | — |
| 20 | RevAdjustmentPercent | PERCENT | — | ✅ |
| 21 | RevAdjustmentProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 22 | RevAdjustmentProgramId | PROGRAM_ID | — | — |
| 23 | RevAdjustmentProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 24 | RevAdjustmentReasonCode | REASON_CODE | — | ✅ |
| 25 | RevAdjustmentRequestId | REQUEST_ID | — | — |
| 26 | RevAdjustmentRevenueAdjustmentId | REVENUE_ADJUSTMENT_ID | — | ✅ |
| 27 | RevAdjustmentRevenueAdjustmentNumber | REVENUE_ADJUSTMENT_NUMBER | — | ✅ |
| 28 | RevAdjustmentSalesCreditType | SALES_CREDIT_TYPE | — | ✅ |
| 29 | RevAdjustmentStatus | STATUS | — | — |
| 30 | RevAdjustmentToCategoryId | TO_CATEGORY_ID | — | — |
| 31 | RevAdjustmentToCustTrxLineId | TO_CUST_TRX_LINE_ID | — | — |
| 32 | RevAdjustmentToInventoryItemId | TO_INVENTORY_ITEM_ID | — | — |
| 33 | RevAdjustmentToResourceSalesrepId | TO_RESOURCE_SALESREP_ID | — | — |
| 34 | RevAdjustmentToSalesgroupId | TO_SALESGROUP_ID | — | — |
| 35 | RevAdjustmentType | TYPE | — | ✅ |

### [[egp_categories_vl|EGP_CATEGORIES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CategoryCategoryId | CATEGORY_ID | — | — |
| 2 | CategoryCategoryName | CATEGORY_NAME | — | ✅ |

### [[egp_system_items_vl|EGP_SYSTEM_ITEMS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemDescription | DESCRIPTION | — | ✅ |
| 2 | ItemInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 3 | ItemItemNumber | ITEM_NUMBER | — | ✅ |
| 4 | ItemOrganizationId | ORGANIZATION_ID | — | — |

### [[fun_bu_perf_v|FUN_BU_PERF_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitBusinessUnitId | BU_ID | — | — |

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LedgersChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 2 | LedgersLedgerId | LEDGER_ID | — | — |

### [[hr_all_organization_units_f_vl|HR_ALL_ORGANIZATION_UNITS_F_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrgUnitFrmSalesGrpEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | OrgUnitFrmSalesGrpEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | OrgUnitFrmSalesGrpName | NAME | — | ✅ |
| 4 | OrgUnitFrmSalesGrpOrganizationId | ORGANIZATION_ID | — | — |
| 5 | OrgUnitToSalesGrpEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 6 | OrgUnitToSalesGrpEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 7 | OrgUnitToSalesGrpName | NAME | — | ✅ |
| 8 | OrgUnitToSalesGrpOrganizationId | ORGANIZATION_ID | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonCreatedByDisplayName | DISPLAY_NAME | — | — |
| 2 | PersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | PersonCreatedByPersonId | PERSON_ID | — | — |
| 5 | PersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | PersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 7 | PersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | PersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | PersonUpdatedByPersonId | PERSON_ID | — | — |
| 10 | PersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 3 | UserCreatedByPersonId | PERSON_ID | — | — |
| 4 | UserCreatedByUserGuid | USER_GUID | — | — |
| 5 | UserCreatedByUserId | USER_ID | — | — |
| 6 | UserCreatedByUsername | USERNAME | — | — |
| 7 | UserUpdatedByPersonId | PERSON_ID | — | — |
| 8 | UserUpdatedByUserGuid | USER_GUID | — | — |
| 9 | UserUpdatedByUserId | USER_ID | — | — |
| 10 | UserUpdatedByUsername | USERNAME | — | — |

### [[ra_cust_trx_line_gl_dist_all|RA_CUST_TRX_LINE_GL_DIST_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustTrxLineGlDistId | CUST_TRX_LINE_GL_DIST_ID | 🔑 | ✅ |
| 2 | TrxDistributionAccountClass | ACCOUNT_CLASS | — | — |
| 3 | TrxDistributionAccountSetFlag | ACCOUNT_SET_FLAG | — | — |
| 4 | TrxDistributionAcctdAmount | ACCTD_AMOUNT | — | ✅ |
| 5 | TrxDistributionAmount | AMOUNT | — | ✅ |
| 6 | TrxDistributionCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 7 | TrxDistributionCollectedTaxCcid | COLLECTED_TAX_CCID | — | — |
| 8 | TrxDistributionCollectedTaxConcatSeg | COLLECTED_TAX_CONCAT_SEG | — | ✅ |
| 9 | TrxDistributionComments | COMMENTS | — | ✅ |
| 10 | TrxDistributionConcatenatedSegments | CONCATENATED_SEGMENTS | — | ✅ |
| 11 | TrxDistributionCreatedBy | CREATED_BY | — | — |
| 12 | TrxDistributionCreationDate | CREATION_DATE | — | — |
| 13 | TrxDistributionCustTrxLineSalesrepId | CUST_TRX_LINE_SALESREP_ID | — | — |
| 14 | TrxDistributionCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 15 | TrxDistributionCustomerTrxLineId | CUSTOMER_TRX_LINE_ID | — | — |
| 16 | TrxDistributionEventId | EVENT_ID | — | ✅ |
| 17 | TrxDistributionGlDate | GL_DATE | — | ✅ |
| 18 | TrxDistributionGlPostedDate | GL_POSTED_DATE | — | ✅ |
| 19 | TrxDistributionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 20 | TrxDistributionLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 21 | TrxDistributionLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 22 | TrxDistributionLatestRecFlag | LATEST_REC_FLAG | — | ✅ |
| 23 | TrxDistributionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 24 | TrxDistributionOrgId | ORG_ID | — | — |
| 25 | TrxDistributionOriginalGlDate | ORIGINAL_GL_DATE | — | ✅ |
| 26 | TrxDistributionPercent | PERCENT | — | ✅ |
| 27 | TrxDistributionPostRequestId | POST_REQUEST_ID | — | — |
| 28 | TrxDistributionPostingControlId | POSTING_CONTROL_ID | — | ✅ |
| 29 | TrxDistributionProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 30 | TrxDistributionProgramId | PROGRAM_ID | — | — |
| 31 | TrxDistributionProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 32 | TrxDistributionRaPostLoopNumber | RA_POST_LOOP_NUMBER | — | — |
| 33 | TrxDistributionRecOffsetFlag | REC_OFFSET_FLAG | — | — |
| 34 | TrxDistributionRequestId | REQUEST_ID | — | — |
| 35 | TrxDistributionRevAdjClassTemp | REV_ADJ_CLASS_TEMP | — | — |
| 36 | TrxDistributionRevenueAdjustmentId | REVENUE_ADJUSTMENT_ID | — | — |
| 37 | TrxDistributionRoundingCorrectionFlag | ROUNDING_CORRECTION_FLAG | — | — |
| 38 | TrxDistributionSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 39 | TrxDistributionTransferToCosting | TRANSFER_TO_COSTING | — | — |
| 40 | TrxDistributionUserGeneratedFlag | USER_GENERATED_FLAG | — | — |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
