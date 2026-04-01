---
id: DOC-PO-PVO-DraftPurchasingDocumentDistributionExtractPVO
doc_type: system-doc
title: "DraftPurchasingDocumentDistributionExtractPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - DraftPurchasingDocumentDistributionExtractPVO
  - draftpurchasingdocumentdistributionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DraftPurchasingDocumentDistributionExtractPVO

## 📌 Visão Geral

Extrai as distribuições contábeis de rascunhos de documentos de compra para carga BICC. Permite análise de comprometimento orçamentário em pedidos ainda não submetidos.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PoBiccExtractAM.DraftPurchasingDocumentDistributionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 69 | 1 | 1 | 68 | 99% |

---

## 🔗 Tabelas Relacionadas

- [[po_distributions_draft_all|PO_DISTRIBUTIONS_DRAFT_ALL]] — 69 atributos (1 PKs, 68 BICC)

---

## ⚙️ Atributos

### [[po_distributions_draft_all|PO_DISTRIBUTIONS_DRAFT_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccrualAccountId | ACCRUAL_ACCOUNT_ID | — | ✅ |
| 2 | AccrueOnReceiptFlag | ACCRUE_ON_RECEIPT_FLAG | — | ✅ |
| 3 | AccruedFlag | ACCRUED_FLAG | — | ✅ |
| 4 | AmountOrdered | AMOUNT_ORDERED | — | ✅ |
| 5 | BudgetDate | BUDGET_DATE | — | ✅ |
| 6 | ChangeAcceptedFlag | CHANGE_ACCEPTED_FLAG | — | ✅ |
| 7 | CoAmountCancelled | CO_AMOUNT_CANCELLED | — | ✅ |
| 8 | CoQuantityCancelled | CO_QUANTITY_CANCELLED | — | ✅ |
| 9 | CodeCombinationId | CODE_COMBINATION_ID | — | ✅ |
| 10 | CreatedBy | CREATED_BY | — | ✅ |
| 11 | CreationDate | CREATION_DATE | — | ✅ |
| 12 | DeliverToCustContactId | DELIVER_TO_CUST_CONTACT_ID | — | ✅ |
| 13 | DeliverToCustId | DELIVER_TO_CUST_ID | — | ✅ |
| 14 | DeliverToCustLocationId | DELIVER_TO_CUST_LOCATION_ID | — | ✅ |
| 15 | DeliverToLocationId | DELIVER_TO_LOCATION_ID | — | ✅ |
| 16 | DeliverToPersonId | DELIVER_TO_PERSON_ID | — | ✅ |
| 17 | DestChargeAccountId | DEST_CHARGE_ACCOUNT_ID | — | ✅ |
| 18 | DestVarianceAccountId | DEST_VARIANCE_ACCOUNT_ID | — | ✅ |
| 19 | DestinationContext | DESTINATION_CONTEXT | — | ✅ |
| 20 | DestinationOrganizationId | DESTINATION_ORGANIZATION_ID | — | ✅ |
| 21 | DestinationSubinventory | DESTINATION_SUBINVENTORY | — | ✅ |
| 22 | DestinationTypeCode | DESTINATION_TYPE_CODE | — | ✅ |
| 23 | DistIntendedUse | DIST_INTENDED_USE | — | — |
| 24 | DistributionNum | DISTRIBUTION_NUM | — | ✅ |
| 25 | EntityChangeTypeCode | ENTITY_CHANGE_TYPE_CODE | — | ✅ |
| 26 | ExternalChangeFlag | EXTERNAL_CHANGE_FLAG | — | ✅ |
| 27 | FundsStatus | FUNDS_STATUS | — | ✅ |
| 28 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 29 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 30 | KanbanCardId | KANBAN_CARD_ID | — | ✅ |
| 31 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 32 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 33 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 34 | LineLocationId | LINE_LOCATION_ID | — | ✅ |
| 35 | NonrecoverableInclusiveTax | NONRECOVERABLE_INCLUSIVE_TAX | — | ✅ |
| 36 | NonrecoverableTax | NONRECOVERABLE_TAX | — | ✅ |
| 37 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 38 | OriginalDistributionId | ORIGINAL_DISTRIBUTION_ID | — | ✅ |
| 39 | PjcContextCategory | PJC_CONTEXT_CATEGORY | — | ✅ |
| 40 | PjcExpenditureTypeId | PJC_EXPENDITURE_TYPE_ID | — | ✅ |
| 41 | PjcOrganizationId | PJC_ORGANIZATION_ID | — | ✅ |
| 42 | PjcProjectId | PJC_PROJECT_ID | — | ✅ |
| 43 | PjcTaskId | PJC_TASK_ID | — | ✅ |
| 44 | PoDistributionId | PO_DISTRIBUTION_ID | 🔑 | ✅ |
| 45 | PoHeaderId | PO_HEADER_ID | — | ✅ |
| 46 | PoLineId | PO_LINE_ID | — | ✅ |
| 47 | PrcBuId | PRC_BU_ID | — | ✅ |
| 48 | ProgramAppName | PROGRAM_APP_NAME | — | ✅ |
| 49 | ProgramName | PROGRAM_NAME | — | ✅ |
| 50 | QuantityOrdered | QUANTITY_ORDERED | — | ✅ |
| 51 | Rate | RATE | — | ✅ |
| 52 | RateDate | RATE_DATE | — | ✅ |
| 53 | ReasonForChange | REASON_FOR_CHANGE | — | ✅ |
| 54 | RecoverableInclusiveTax | RECOVERABLE_INCLUSIVE_TAX | — | ✅ |
| 55 | RecoverableTax | RECOVERABLE_TAX | — | ✅ |
| 56 | RecoveryRate | RECOVERY_RATE | — | ✅ |
| 57 | ReqBuId | REQ_BU_ID | — | ✅ |
| 58 | ReqDistributionId | REQ_DISTRIBUTION_ID | — | ✅ |
| 59 | ReqHeaderReferenceNum | REQ_HEADER_REFERENCE_NUM | — | ✅ |
| 60 | ReqLineReferenceNum | REQ_LINE_REFERENCE_NUM | — | ✅ |
| 61 | RequestId | REQUEST_ID | — | ✅ |
| 62 | SetOfBooksId | SET_OF_BOOKS_ID | — | ✅ |
| 63 | ShippingUomQuantity | SHIPPING_UOM_QUANTITY | — | ✅ |
| 64 | TaxAttributeUpdateCode | TAX_ATTRIBUTE_UPDATE_CODE | — | ✅ |
| 65 | TaxExclusiveAmount | TAX_EXCLUSIVE_AMOUNT | — | ✅ |
| 66 | TaxRecoveryOverrideFlag | TAX_RECOVERY_OVERRIDE_FLAG | — | ✅ |
| 67 | UnencumberedAmount | UNENCUMBERED_AMOUNT | — | ✅ |
| 68 | UserPoChrgAcctChgFlag | USER_PO_CHRG_ACCT_CHG_FLAG | — | ✅ |
| 69 | VarianceAccountId | VARIANCE_ACCOUNT_ID | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
