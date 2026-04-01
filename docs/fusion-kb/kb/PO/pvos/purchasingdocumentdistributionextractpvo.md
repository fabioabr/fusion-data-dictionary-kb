---
id: DOC-PO-PVO-PurchasingDocumentDistributionExtractPVO
doc_type: system-doc
title: "PurchasingDocumentDistributionExtractPVO — PVO Purchasing"
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
  - PurchasingDocumentDistributionExtractPVO
  - purchasingdocumentdistributionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PurchasingDocumentDistributionExtractPVO

## 📌 Visão Geral

Extrai as distribuições contábeis de ordens de compra para carga BICC, mapeando cada linha a centros de custo, contas e projetos. Essencial para apropriação de despesas e controle orçamentário.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PoBiccExtractAM.PurchasingDocumentDistributionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 64 | 1 | 1 | 63 | 98% |

---

## 🔗 Tabelas Relacionadas

- [[po_distributions_all|PO_DISTRIBUTIONS_ALL]] — 64 atributos (1 PKs, 63 BICC)

---

## ⚙️ Atributos

### [[po_distributions_all|PO_DISTRIBUTIONS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccrualAccountId | ACCRUAL_ACCOUNT_ID | — | ✅ |
| 2 | AccrueOnReceiptFlag | ACCRUE_ON_RECEIPT_FLAG | — | ✅ |
| 3 | AccruedFlag | ACCRUED_FLAG | — | ✅ |
| 4 | AmountBilled | AMOUNT_BILLED | — | ✅ |
| 5 | AmountCancelled | AMOUNT_CANCELLED | — | ✅ |
| 6 | AmountDelivered | AMOUNT_DELIVERED | — | ✅ |
| 7 | AmountOrdered | AMOUNT_ORDERED | — | ✅ |
| 8 | BudgetDate | BUDGET_DATE | — | ✅ |
| 9 | CodeCombinationId | CODE_COMBINATION_ID | — | ✅ |
| 10 | ConsignmentQuantity | CONSIGNMENT_QUANTITY | — | ✅ |
| 11 | CreatedBy | CREATED_BY | — | ✅ |
| 12 | CreationDate | CREATION_DATE | — | ✅ |
| 13 | DeliverToCustContactId | DELIVER_TO_CUST_CONTACT_ID | — | ✅ |
| 14 | DeliverToCustId | DELIVER_TO_CUST_ID | — | ✅ |
| 15 | DeliverToCustLocationId | DELIVER_TO_CUST_LOCATION_ID | — | ✅ |
| 16 | DeliverToLocationId | DELIVER_TO_LOCATION_ID | — | ✅ |
| 17 | DeliverToPersonId | DELIVER_TO_PERSON_ID | — | ✅ |
| 18 | DestChargeAccountId | DEST_CHARGE_ACCOUNT_ID | — | ✅ |
| 19 | DestVarianceAccountId | DEST_VARIANCE_ACCOUNT_ID | — | ✅ |
| 20 | DestinationOrganizationId | DESTINATION_ORGANIZATION_ID | — | ✅ |
| 21 | DestinationSubinventory | DESTINATION_SUBINVENTORY | — | ✅ |
| 22 | DestinationTypeCode | DESTINATION_TYPE_CODE | — | ✅ |
| 23 | DistIntendedUse | DIST_INTENDED_USE | — | — |
| 24 | DistributionNum | DISTRIBUTION_NUM | — | ✅ |
| 25 | FundsStatus | FUNDS_STATUS | — | ✅ |
| 26 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 27 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 28 | LineLocationId | LINE_LOCATION_ID | — | ✅ |
| 29 | NonrecoverableInclusiveTax | NONRECOVERABLE_INCLUSIVE_TAX | — | ✅ |
| 30 | NonrecoverableTax | NONRECOVERABLE_TAX | — | ✅ |
| 31 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 32 | OriginalDistributionId | ORIGINAL_DISTRIBUTION_ID | — | ✅ |
| 33 | PJC_CONTEXT_CATEGORY | PJC_CONTEXT_CATEGORY | — | ✅ |
| 34 | PJC_EXPENDITURE_TYPE_ID | PJC_EXPENDITURE_TYPE_ID | — | ✅ |
| 35 | PJC_ORGANIZATION_ID | PJC_ORGANIZATION_ID | — | ✅ |
| 36 | PJC_PROJECT_ID | PJC_PROJECT_ID | — | ✅ |
| 37 | PJC_TASK_ID | PJC_TASK_ID | — | ✅ |
| 38 | PoDistributionId | PO_DISTRIBUTION_ID | 🔑 | ✅ |
| 39 | PoHeaderId | PO_HEADER_ID | — | ✅ |
| 40 | PoLineId | PO_LINE_ID | — | ✅ |
| 41 | QuantityBilled | QUANTITY_BILLED | — | ✅ |
| 42 | QuantityCancelled | QUANTITY_CANCELLED | — | ✅ |
| 43 | QuantityDelivered | QUANTITY_DELIVERED | — | ✅ |
| 44 | QuantityOrdered | QUANTITY_ORDERED | — | ✅ |
| 45 | Rate | RATE | — | ✅ |
| 46 | RateDate | RATE_DATE | — | ✅ |
| 47 | RecoverableInclusiveTax | RECOVERABLE_INCLUSIVE_TAX | — | ✅ |
| 48 | RecoverableTax | RECOVERABLE_TAX | — | ✅ |
| 49 | RecoveryRate | RECOVERY_RATE | — | ✅ |
| 50 | ReqBuId | REQ_BU_ID | — | ✅ |
| 51 | ReqDistributionId | REQ_DISTRIBUTION_ID | — | ✅ |
| 52 | ReqHeaderReferenceNum | REQ_HEADER_REFERENCE_NUM | — | ✅ |
| 53 | ReqLineReferenceNum | REQ_LINE_REFERENCE_NUM | — | ✅ |
| 54 | RetainageReleasedAmount | RETAINAGE_RELEASED_AMOUNT | — | ✅ |
| 55 | RetainageWithheldAmount | RETAINAGE_WITHHELD_AMOUNT | — | ✅ |
| 56 | SetOfBooksId | SET_OF_BOOKS_ID | — | ✅ |
| 57 | ShippingUomQtyCanceled | SHIPPING_UOM_QUANTITY_CANCELED | — | ✅ |
| 58 | ShippingUomQtyDelivered | SHIPPING_UOM_QTY_DELIVERED | — | ✅ |
| 59 | ShippingUomQuantity | SHIPPING_UOM_QUANTITY | — | ✅ |
| 60 | TaxAttributeUpdateCode | TAX_ATTRIBUTE_UPDATE_CODE | — | ✅ |
| 61 | TaxExclusiveAmount | TAX_EXCLUSIVE_AMOUNT | — | ✅ |
| 62 | TaxRecoveryOverrideFlag | TAX_RECOVERY_OVERRIDE_FLAG | — | ✅ |
| 63 | UnencumberedAmount | UNENCUMBERED_AMOUNT | — | ✅ |
| 64 | VarianceAccountId | VARIANCE_ACCOUNT_ID | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
