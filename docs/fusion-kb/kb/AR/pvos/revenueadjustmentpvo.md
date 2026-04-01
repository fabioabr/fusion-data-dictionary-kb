---
id: DOC-AR-PVO-RevenueAdjustmentPVO
doc_type: system-doc
title: "RevenueAdjustmentPVO — PVO Accounts Receivable"
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
  - RevenueAdjustmentPVO
  - revenueadjustmentpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RevenueAdjustmentPVO

## 📌 Visão Geral

Extrai os ajustes de reconhecimento de receita em transações de Contas a Receber, com motivo, valor, status e período. Permite controlar reclassificações de receita, diferimentos e acelerações conforme normas contábeis.

**Caminho:** `FscmTopModelAM.FinArTopPublicModelAM.RevenueAdjustmentPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 71 | 8 | 1 | 20 | 28% |

---

## 🔗 Tabelas Relacionadas

- [[ar_revenue_adjustments_all|AR_REVENUE_ADJUSTMENTS_ALL]] — 35 atributos (1 PKs, 15 BICC)
- [[egp_categories_vl|EGP_CATEGORIES_VL]] — 2 atributos (1 BICC)
- [[egp_system_items_vl|EGP_SYSTEM_ITEMS_VL]] — 4 atributos (2 BICC)
- [[fun_bu_perf_v|FUN_BU_PERF_V]] — 2 atributos
- [[hr_all_organization_units_f_vl|HR_ALL_ORGANIZATION_UNITS_F_VL]] — 8 atributos (2 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos
- [[per_users|PER_USERS]] — 8 atributos
- [[ra_customer_trx_all|RA_CUSTOMER_TRX_ALL]] — 2 atributos

---

## ⚙️ Atributos

### [[ar_revenue_adjustments_all|AR_REVENUE_ADJUSTMENTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RevenueAdjustmentAmount | AMOUNT | — | ✅ |
| 2 | RevenueAdjustmentAmountMode | AMOUNT_MODE | — | ✅ |
| 3 | RevenueAdjustmentApplicationDate | APPLICATION_DATE | — | ✅ |
| 4 | RevenueAdjustmentComments | COMMENTS | — | ✅ |
| 5 | RevenueAdjustmentCreatedBy | CREATED_BY | — | ✅ |
| 6 | RevenueAdjustmentCreationDate | CREATION_DATE | — | ✅ |
| 7 | RevenueAdjustmentCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 8 | RevenueAdjustmentFromCategoryId | FROM_CATEGORY_ID | — | — |
| 9 | RevenueAdjustmentFromCustTrxLineId | FROM_CUST_TRX_LINE_ID | — | — |
| 10 | RevenueAdjustmentFromInventoryItemId | FROM_INVENTORY_ITEM_ID | — | — |
| 11 | RevenueAdjustmentFromResourceSalesrepId | FROM_RESOURCE_SALESREP_ID | — | — |
| 12 | RevenueAdjustmentFromSalesgroupId | FROM_SALESGROUP_ID | — | — |
| 13 | RevenueAdjustmentGlDate | GL_DATE | — | ✅ |
| 14 | RevenueAdjustmentId | REVENUE_ADJUSTMENT_ID | 🔑 | ✅ |
| 15 | RevenueAdjustmentLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | RevenueAdjustmentLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 17 | RevenueAdjustmentLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 18 | RevenueAdjustmentLineSelectionMode | LINE_SELECTION_MODE | — | — |
| 19 | RevenueAdjustmentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | RevenueAdjustmentOrgId | ORG_ID | — | — |
| 21 | RevenueAdjustmentPercent | PERCENT | — | ✅ |
| 22 | RevenueAdjustmentProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 23 | RevenueAdjustmentProgramId | PROGRAM_ID | — | — |
| 24 | RevenueAdjustmentProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 25 | RevenueAdjustmentReasonCode | REASON_CODE | — | ✅ |
| 26 | RevenueAdjustmentRequestId | REQUEST_ID | — | — |
| 27 | RevenueAdjustmentRevenueAdjustmentNumber | REVENUE_ADJUSTMENT_NUMBER | — | ✅ |
| 28 | RevenueAdjustmentSalesCreditType | SALES_CREDIT_TYPE | — | ✅ |
| 29 | RevenueAdjustmentStatus | STATUS | — | — |
| 30 | RevenueAdjustmentToCategoryId | TO_CATEGORY_ID | — | — |
| 31 | RevenueAdjustmentToCustTrxLineId | TO_CUST_TRX_LINE_ID | — | — |
| 32 | RevenueAdjustmentToInventoryItemId | TO_INVENTORY_ITEM_ID | — | — |
| 33 | RevenueAdjustmentToResourceSalesrepId | TO_RESOURCE_SALESREP_ID | — | — |
| 34 | RevenueAdjustmentToSalesgroupId | TO_SALESGROUP_ID | — | — |
| 35 | RevenueAdjustmentType | TYPE | — | ✅ |

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
| 2 | BusinessUnitName | BU_NAME | — | — |

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
| 6 | PersonUpdatedByDisplayName | DISPLAY_NAME | — | — |
| 7 | PersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | PersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | PersonUpdatedByPersonId | PERSON_ID | — | — |
| 10 | PersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserCreatedByPersonId | PERSON_ID | — | — |
| 2 | UserCreatedByUserGuid | USER_GUID | — | — |
| 3 | UserCreatedByUserId | USER_ID | — | — |
| 4 | UserCreatedByUsername | USERNAME | — | — |
| 5 | UserUpdatedByPersonId | PERSON_ID | — | — |
| 6 | UserUpdatedByUserGuid | USER_GUID | — | — |
| 7 | UserUpdatedByUserId | USER_ID | — | — |
| 8 | UserUpdatedByUsername | USERNAME | — | — |

### [[ra_customer_trx_all|RA_CUSTOMER_TRX_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionHeaderCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 2 | TransactionHeaderSetOfBooksId | SET_OF_BOOKS_ID | — | — |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
