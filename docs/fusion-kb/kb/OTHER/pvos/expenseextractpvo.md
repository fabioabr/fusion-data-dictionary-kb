---
id: DOC-OTHER-PVO-ExpenseExtractPVO
doc_type: system-doc
title: "ExpenseExtractPVO — PVO Cross-Module"
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
  - ExpenseExtractPVO
  - expenseextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ExpenseExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Expense Extract. Acessa as tabelas: EXM_EXPENSES.

**Caminho:** `FscmTopModelAM.FinExtractAM.ExmBiccExtractAM.ExpenseExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 117 | 1 | 1 | 39 | 33% |

---

## 🔗 Tabelas Relacionadas

- [[exm_expenses|EXM_EXPENSES]] — 117 atributos (1 PKs, 39 BICC)

---

## ⚙️ Atributos

### [[exm_expenses|EXM_EXPENSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenseAllocationReason | ALLOCATION_REASON | — | — |
| 2 | ExpenseAllocationSplitCode | ALLOCATION_SPLIT_CODE | — | — |
| 3 | ExpenseAssignmentId | ASSIGNMENT_ID | — | ✅ |
| 4 | ExpenseAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 5 | ExpenseAttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 6 | ExpenseAttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 7 | ExpenseAttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 8 | ExpenseAttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 9 | ExpenseAttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 10 | ExpenseAttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 11 | ExpenseAttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 12 | ExpenseAttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 13 | ExpenseAttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 14 | ExpenseAttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 15 | ExpenseAttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 16 | ExpenseAttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 17 | ExpenseAttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 18 | ExpenseAttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 19 | ExpenseAttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 20 | ExpenseAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 21 | ExpenseAttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 22 | ExpenseAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 23 | ExpenseAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 24 | ExpenseAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 25 | ExpenseAttributeDatetime1 | ATTRIBUTE_DATETIME1 | — | — |
| 26 | ExpenseAttributeDatetime2 | ATTRIBUTE_DATETIME2 | — | — |
| 27 | ExpenseAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 28 | ExpenseAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 29 | ExpenseAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 30 | ExpenseAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 31 | ExpenseAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 32 | ExpenseAuditAdjustmentReason | AUDIT_ADJUSTMENT_REASON | — | ✅ |
| 33 | ExpenseAuditAdjustmentReasonCode | AUDIT_ADJUSTMENT_REASON_CODE | — | ✅ |
| 34 | ExpenseAvgMileageRate | AVG_MILEAGE_RATE | — | — |
| 35 | ExpenseAwtGroupId | AWT_GROUP_ID | — | — |
| 36 | ExpenseCardId | CARD_ID | — | ✅ |
| 37 | ExpenseCategoryCode | EXPENSE_CATEGORY_CODE | — | — |
| 38 | ExpenseCcPrepaidInvoiceId | CC_PREPAID_INVOICE_ID | — | — |
| 39 | ExpenseCcPrepaidRequestId | CC_PREPAID_REQUEST_ID | — | — |
| 40 | ExpenseCheckoutDate | CHECKOUT_DATE | — | — |
| 41 | ExpenseCountryOfSupply | COUNTRY_OF_SUPPLY | — | — |
| 42 | ExpenseCreatedBy | CREATED_BY | — | — |
| 43 | ExpenseCreationDate | CREATION_DATE | — | ✅ |
| 44 | ExpenseCreationMethodCode | EXPENSE_CREATION_METHOD_CODE | — | — |
| 45 | ExpenseCreditCardTrxnId | CREDIT_CARD_TRXN_ID | — | ✅ |
| 46 | ExpenseDailyDistance | DAILY_DISTANCE | — | — |
| 47 | ExpenseDepartureLocationId | DEPARTURE_LOCATION_ID | — | — |
| 48 | ExpenseDescription | DESCRIPTION | — | ✅ |
| 49 | ExpenseDestinationFrom | DESTINATION_FROM | — | — |
| 50 | ExpenseDestinationTo | DESTINATION_TO | — | — |
| 51 | ExpenseDistanceUnitCode | DISTANCE_UNIT_CODE | — | — |
| 52 | ExpenseEmpDefaultCostCenter | EMP_DEFAULT_COST_CENTER | — | ✅ |
| 53 | ExpenseEndDate | END_DATE | — | ✅ |
| 54 | ExpenseExchangeRate | EXCHANGE_RATE | — | ✅ |
| 55 | ExpenseFlightNumber | FLIGHT_NUMBER | — | — |
| 56 | ExpenseFuelType | FUEL_TYPE | — | — |
| 57 | ExpenseFuncCurrencyAmount | FUNC_CURRENCY_AMOUNT | — | ✅ |
| 58 | ExpenseId | EXPENSE_ID | 🔑 | ✅ |
| 59 | ExpenseImgReceiptRequiredFlag | IMG_RECEIPT_REQUIRED_FLAG | — | — |
| 60 | ExpenseInactiveEmpProcessId | INACTIVE_EMP_PROCESS_ID | — | — |
| 61 | ExpenseItemizationParentExpenseId | ITEMIZATION_PARENT_EXPENSE_ID | — | ✅ |
| 62 | ExpenseJustification | JUSTIFICATION | — | ✅ |
| 63 | ExpenseJustificationRequiredFlag | JUSTIFICATION_REQUIRED_FLAG | — | ✅ |
| 64 | ExpenseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 65 | ExpenseLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 66 | ExpenseLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 67 | ExpenseLicensePlateNumber | LICENSE_PLATE_NUMBER | — | — |
| 68 | ExpenseLocation | LOCATION | — | ✅ |
| 69 | ExpenseLocationId | LOCATION_ID | — | ✅ |
| 70 | ExpenseMerchantDocumentNumber | MERCHANT_DOCUMENT_NUMBER | — | — |
| 71 | ExpenseMerchantName | MERCHANT_NAME | — | — |
| 72 | ExpenseMerchantReference | MERCHANT_REFERENCE | — | — |
| 73 | ExpenseMerchantTaxRegNumber | MERCHANT_TAX_REG_NUMBER | — | — |
| 74 | ExpenseMerchantTaxpayerId | MERCHANT_TAXPAYER_ID | — | — |
| 75 | ExpenseMileageRateAdjustedFlag | MILEAGE_RATE_ADJUSTED_FLAG | — | — |
| 76 | ExpenseNumberOfAttendees | NUMBER_OF_ATTENDEES | — | — |
| 77 | ExpenseNumberPeople | NUMBER_PEOPLE | — | — |
| 78 | ExpenseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 79 | ExpenseOrgId | ORG_ID | — | ✅ |
| 80 | ExpenseOrigExchangeRate | ORIG_EXCHANGE_RATE | — | — |
| 81 | ExpenseOrigExpenseTypeId | ORIG_EXPENSE_TYPE_ID | — | — |
| 82 | ExpenseOrigReceiptAmount | ORIG_RECEIPT_AMOUNT | — | — |
| 83 | ExpenseOrigReimbursableAmount | ORIG_REIMBURSABLE_AMOUNT | — | ✅ |
| 84 | ExpensePassengerAmount | PASSENGER_AMOUNT | — | — |
| 85 | ExpensePassengerRateType | PASSENGER_RATE_TYPE | — | — |
| 86 | ExpensePersonId | PERSON_ID | — | ✅ |
| 87 | ExpensePersonalReceiptAmount | PERSONAL_RECEIPT_AMOUNT | — | ✅ |
| 88 | ExpensePolicyShortpayFlag | POLICY_SHORTPAY_FLAG | — | — |
| 89 | ExpensePolicyViolatedFlag | POLICY_VIOLATED_FLAG | — | — |
| 90 | ExpensePreparerId | PREPARER_ID | — | ✅ |
| 91 | ExpenseRangeHigh | RANGE_HIGH | — | — |
| 92 | ExpenseRangeLow | RANGE_LOW | — | — |
| 93 | ExpenseRatePerPassenger | RATE_PER_PASSENGER | — | — |
| 94 | ExpenseReceiptAmount | RECEIPT_AMOUNT | — | ✅ |
| 95 | ExpenseReceiptCurrencyCode | RECEIPT_CURRENCY_CODE | — | ✅ |
| 96 | ExpenseReceiptMissingDecReqFlag | RECEIPT_MISSING_DEC_REQ_FLAG | — | — |
| 97 | ExpenseReceiptMissingFlag | RECEIPT_MISSING_FLAG | — | ✅ |
| 98 | ExpenseReceiptRequiredFlag | RECEIPT_REQUIRED_FLAG | — | ✅ |
| 99 | ExpenseReceiptVerifiedFlag | RECEIPT_VERIFIED_FLAG | — | ✅ |
| 100 | ExpenseReimbursableAmount | REIMBURSABLE_AMOUNT | — | ✅ |
| 101 | ExpenseReimbursementCurrencyCode | REIMBURSEMENT_CURRENCY_CODE | — | ✅ |
| 102 | ExpenseReportId | EXPENSE_REPORT_ID | — | ✅ |
| 103 | ExpenseSequenceNum | SEQUENCE_NUM | — | — |
| 104 | ExpenseSource | EXPENSE_SOURCE | — | ✅ |
| 105 | ExpenseStartDate | START_DATE | — | ✅ |
| 106 | ExpenseTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | ✅ |
| 107 | ExpenseTemplateId | EXPENSE_TEMPLATE_ID | — | ✅ |
| 108 | ExpenseTicketClassCode | TICKET_CLASS_CODE | — | — |
| 109 | ExpenseTicketNumber | TICKET_NUMBER | — | — |
| 110 | ExpenseTravelType | TRAVEL_TYPE | — | — |
| 111 | ExpenseTripDistance | TRIP_DISTANCE | — | — |
| 112 | ExpenseTrxnAvailableDate | TRXN_AVAILABLE_DATE | — | — |
| 113 | ExpenseTypeCategoryCode | EXPENSE_TYPE_CATEGORY_CODE | — | ✅ |
| 114 | ExpenseTypeId | EXPENSE_TYPE_ID | — | ✅ |
| 115 | ExpenseUomDays | UOM_DAYS | — | — |
| 116 | ExpenseVehicleCategoryCode | VEHICLE_CATEGORY_CODE | — | — |
| 117 | ExpenseVehicleType | VEHICLE_TYPE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
