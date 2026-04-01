---
id: DOC-OTHER-PVO-ExpenseAttendeePVO
doc_type: system-doc
title: "ExpenseAttendeePVO — PVO Cross-Module"
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
  - ExpenseAttendeePVO
  - expenseattendeepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ExpenseAttendeePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Expense Attendee. Acessa as tabelas: EXM_CREDIT_CARD_TRXNS, EXM_EXPENSES, EXM_EXPENSE_ATTENDEES (+10).

**Caminho:** `FscmTopModelAM.FinExmEntrySharedAM.ExpenseAttendeePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 462 | 13 | 1 | 72 | 16% |

---

## 🔗 Tabelas Relacionadas

- [[exm_credit_card_trxns|EXM_CREDIT_CARD_TRXNS]] — 2 atributos (1 BICC)
- [[exm_expenses|EXM_EXPENSES]] — 90 atributos (39 BICC)
- [[exm_expense_attendees|EXM_EXPENSE_ATTENDEES]] — 19 atributos (1 PKs, 2 BICC)
- [[exm_expense_reports|EXM_EXPENSE_REPORTS]] — 53 atributos (21 BICC)
- [[exm_expense_templates|EXM_EXPENSE_TEMPLATES]] — 21 atributos (1 BICC)
- [[exm_expense_types|EXM_EXPENSE_TYPES]] — 27 atributos (1 BICC)
- [[fun_bu_perf_v|FUN_BU_PERF_V]] — 11 atributos
- [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]] — 18 atributos
- [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]] — 16 atributos
- [[hz_parties|HZ_PARTIES]] — 4 atributos
- [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]] — 109 atributos (1 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 62 atributos (6 BICC)
- [[per_users|PER_USERS]] — 30 atributos

---

## ⚙️ Atributos

### [[exm_credit_card_trxns|EXM_CREDIT_CARD_TRXNS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpCreditCardTrxCreditCardTrxnId | CREDIT_CARD_TRXN_ID | — | — |
| 2 | ExpCreditCardTrxReferenceNumber | REFERENCE_NUMBER | — | ✅ |

### [[exm_expenses|EXM_EXPENSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpAllocationReason | ALLOCATION_REASON | — | — |
| 2 | ExpAllocationSplitCode | ALLOCATION_SPLIT_CODE | — | — |
| 3 | ExpAssignmentId | ASSIGNMENT_ID | — | — |
| 4 | ExpAttributeCategory1 | ATTRIBUTE_CATEGORY | — | — |
| 5 | ExpAuditAdjustmentReason | AUDIT_ADJUSTMENT_REASON | — | — |
| 6 | ExpAuditAdjustmentReasonCode | AUDIT_ADJUSTMENT_REASON_CODE | — | ✅ |
| 7 | ExpAvgMileageRate | AVG_MILEAGE_RATE | — | ✅ |
| 8 | ExpAwtGroupId | AWT_GROUP_ID | — | — |
| 9 | ExpCardId | CARD_ID | — | — |
| 10 | ExpCcPrepaidInvoiceId | CC_PREPAID_INVOICE_ID | — | — |
| 11 | ExpCcPrepaidRequestId | CC_PREPAID_REQUEST_ID | — | — |
| 12 | ExpCheckoutDate | CHECKOUT_DATE | — | — |
| 13 | ExpCountryOfSupply | COUNTRY_OF_SUPPLY | — | — |
| 14 | ExpCreatedBy | CREATED_BY | — | ✅ |
| 15 | ExpCreationDate | CREATION_DATE | — | ✅ |
| 16 | ExpCreditCardTrxnId | CREDIT_CARD_TRXN_ID | — | — |
| 17 | ExpDailyDistance | DAILY_DISTANCE | — | ✅ |
| 18 | ExpDepartureLocationId | DEPARTURE_LOCATION_ID | — | — |
| 19 | ExpDescription | DESCRIPTION | — | ✅ |
| 20 | ExpDestinationFrom | DESTINATION_FROM | — | ✅ |
| 21 | ExpDestinationTo | DESTINATION_TO | — | ✅ |
| 22 | ExpDistanceUnitCode | DISTANCE_UNIT_CODE | — | ✅ |
| 23 | ExpEmpDefaultCostCenter | EMP_DEFAULT_COST_CENTER | — | — |
| 24 | ExpEndDate | END_DATE | — | ✅ |
| 25 | ExpExchangeRate | EXCHANGE_RATE | — | — |
| 26 | ExpExpenseCategoryCode | EXPENSE_CATEGORY_CODE | — | ✅ |
| 27 | ExpExpenseReportId | EXPENSE_REPORT_ID | — | ✅ |
| 28 | ExpExpenseSource | EXPENSE_SOURCE | — | ✅ |
| 29 | ExpExpenseTemplateId | EXPENSE_TEMPLATE_ID | — | — |
| 30 | ExpExpenseTypeCategoryCode | EXPENSE_TYPE_CATEGORY_CODE | — | ✅ |
| 31 | ExpExpenseTypeId | EXPENSE_TYPE_ID | — | — |
| 32 | ExpFlightNumber | FLIGHT_NUMBER | — | ✅ |
| 33 | ExpFuelType | FUEL_TYPE | — | ✅ |
| 34 | ExpFuncCurrencyAmount | FUNC_CURRENCY_AMOUNT | — | — |
| 35 | ExpImgReceiptRequiredFlag | IMG_RECEIPT_REQUIRED_FLAG | — | — |
| 36 | ExpInactiveEmpProcessId | INACTIVE_EMP_PROCESS_ID | — | — |
| 37 | ExpItemizationParentExpenseId | ITEMIZATION_PARENT_EXPENSE_ID | — | — |
| 38 | ExpJustification | JUSTIFICATION | — | ✅ |
| 39 | ExpJustificationRequiredFlag | JUSTIFICATION_REQUIRED_FLAG | — | ✅ |
| 40 | ExpLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 41 | ExpLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 42 | ExpLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 43 | ExpLicensePlateNumber | LICENSE_PLATE_NUMBER | — | — |
| 44 | ExpLocation | LOCATION | — | ✅ |
| 45 | ExpLocationId | LOCATION_ID | — | — |
| 46 | ExpMerchantDocumentNumber | MERCHANT_DOCUMENT_NUMBER | — | ✅ |
| 47 | ExpMerchantName | MERCHANT_NAME | — | ✅ |
| 48 | ExpMerchantReference | MERCHANT_REFERENCE | — | — |
| 49 | ExpMerchantTaxRegNumber | MERCHANT_TAX_REG_NUMBER | — | — |
| 50 | ExpMerchantTaxpayerId | MERCHANT_TAXPAYER_ID | — | — |
| 51 | ExpMileageRateAdjustedFlag | MILEAGE_RATE_ADJUSTED_FLAG | — | — |
| 52 | ExpNumberOfAttendees | NUMBER_OF_ATTENDEES | — | ✅ |
| 53 | ExpNumberPeople | NUMBER_PEOPLE | — | — |
| 54 | ExpObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 55 | ExpOrgId | ORG_ID | — | — |
| 56 | ExpOrigExchangeRate | ORIG_EXCHANGE_RATE | — | — |
| 57 | ExpOrigExpenseTypeId | ORIG_EXPENSE_TYPE_ID | — | — |
| 58 | ExpOrigReceiptAmount | ORIG_RECEIPT_AMOUNT | — | — |
| 59 | ExpOrigReimbursableAmount | ORIG_REIMBURSABLE_AMOUNT | — | — |
| 60 | ExpPassengerAmount | PASSENGER_AMOUNT | — | — |
| 61 | ExpPassengerRateType | PASSENGER_RATE_TYPE | — | — |
| 62 | ExpPersonId | PERSON_ID | — | — |
| 63 | ExpPersonalReceiptAmount | PERSONAL_RECEIPT_AMOUNT | — | — |
| 64 | ExpPolicyShortpayFlag | POLICY_SHORTPAY_FLAG | — | ✅ |
| 65 | ExpPolicyViolatedFlag | POLICY_VIOLATED_FLAG | — | ✅ |
| 66 | ExpPreparerId | PREPARER_ID | — | — |
| 67 | ExpRangeHigh | RANGE_HIGH | — | — |
| 68 | ExpRangeLow | RANGE_LOW | — | — |
| 69 | ExpRatePerPassenger | RATE_PER_PASSENGER | — | — |
| 70 | ExpReceiptAmount | RECEIPT_AMOUNT | — | — |
| 71 | ExpReceiptCurrencyCode | RECEIPT_CURRENCY_CODE | — | ✅ |
| 72 | ExpReceiptMissingDecReqFlag | RECEIPT_MISSING_DEC_REQ_FLAG | — | — |
| 73 | ExpReceiptMissingFlag | RECEIPT_MISSING_FLAG | — | ✅ |
| 74 | ExpReceiptRequiredFlag | RECEIPT_REQUIRED_FLAG | — | ✅ |
| 75 | ExpReceiptVerifiedFlag | RECEIPT_VERIFIED_FLAG | — | ✅ |
| 76 | ExpReimbursableAmount | REIMBURSABLE_AMOUNT | — | — |
| 77 | ExpReimbursementCurrencyCode | REIMBURSEMENT_CURRENCY_CODE | — | — |
| 78 | ExpSequenceNum | SEQUENCE_NUM | — | — |
| 79 | ExpStartDate | START_DATE | — | ✅ |
| 80 | ExpTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | ✅ |
| 81 | ExpTicketClassCode | TICKET_CLASS_CODE | — | ✅ |
| 82 | ExpTicketNumber | TICKET_NUMBER | — | ✅ |
| 83 | ExpTravelType | TRAVEL_TYPE | — | ✅ |
| 84 | ExpTripDistance | TRIP_DISTANCE | — | ✅ |
| 85 | ExpTrxnAvailableDate | TRXN_AVAILABLE_DATE | — | — |
| 86 | ExpUomDays | UOM_DAYS | — | — |
| 87 | ExpVehicleCategoryCode | VEHICLE_CATEGORY_CODE | — | ✅ |
| 88 | ExpVehicleType | VEHICLE_TYPE | — | ✅ |
| 89 | ExpenseId | EXPENSE_ID | — | ✅ |
| 90 | FullExpExpenseCMC | EXPENSE_CREATION_METHOD_CODE | — | — |

### [[exm_expense_attendees|EXM_EXPENSE_ATTENDEES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenseAttendeeAttendeeAmount | AMOUNT | — | ✅ |
| 2 | ExpenseAttendeeAttendeeCreatedBy | CREATED_BY | — | — |
| 3 | ExpenseAttendeeAttendeeCreationDate | CREATION_DATE | — | — |
| 4 | ExpenseAttendeeAttendeeLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 5 | ExpenseAttendeeAttendeePartyId | ATTENDEE_PARTY_ID | — | — |
| 6 | ExpenseAttendeeAttendeeType | ATTENDEE_TYPE | — | — |
| 7 | ExpenseAttendeeAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 8 | ExpenseAttendeeEmployeeIndicator | EMPLOYEE_FLAG | — | — |
| 9 | ExpenseAttendeeEmployerAddress | EMPLOYER_ADDRESS | — | — |
| 10 | ExpenseAttendeeEmployerName | EMPLOYER_NAME | — | — |
| 11 | ExpenseAttendeeEmployerPartyId | EMPLOYER_PARTY_ID | — | — |
| 12 | ExpenseAttendeeExpenseAttendeeId | EXPENSE_ATTENDEE_ID | 🔑 | ✅ |
| 13 | ExpenseAttendeeExpenseId | EXPENSE_ID | — | — |
| 14 | ExpenseAttendeeJobTitle | TITLE | — | — |
| 15 | ExpenseAttendeeLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | ExpenseAttendeeLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 17 | ExpenseAttendeeName | NAME | — | — |
| 18 | ExpenseAttendeeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 19 | ExpenseAttendeeTaxIdentifier | TAX_IDENTIFIER | — | — |

### [[exm_expense_reports|EXM_EXPENSE_REPORTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpHdrApplyCashAdvFlag | APPLY_CASH_ADV_FLAG | — | — |
| 2 | ExpHdrAssignmentId | ASSIGNMENT_ID | — | — |
| 3 | ExpHdrAttributeCategory2 | ATTRIBUTE_CATEGORY | — | — |
| 4 | ExpHdrAuditCode | AUDIT_CODE | — | ✅ |
| 5 | ExpHdrAuditReturnReasonCode | AUDIT_RETURN_REASON_CODE | — | ✅ |
| 6 | ExpHdrAwtGroupId | AWT_GROUP_ID | — | — |
| 7 | ExpHdrBothpayFlag | BOTHPAY_FLAG | — | — |
| 8 | ExpHdrCashExpensePaidDate | CASH_EXPENSE_PAID_DATE | — | ✅ |
| 9 | ExpHdrCreatedBy | CREATED_BY | — | ✅ |
| 10 | ExpHdrCreationDate | CREATION_DATE | — | ✅ |
| 11 | ExpHdrCurrentApproverId | CURRENT_APPROVER_ID | — | — |
| 12 | ExpHdrExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 13 | ExpHdrExpRepProcessingId | EXP_REP_PROCESSING_ID | — | — |
| 14 | ExpHdrExpenseReportDate | EXPENSE_REPORT_DATE | — | ✅ |
| 15 | ExpHdrExpenseReportId | EXPENSE_REPORT_ID | — | — |
| 16 | ExpHdrExpenseReportNum | EXPENSE_REPORT_NUM | — | ✅ |
| 17 | ExpHdrExpenseReportTotal | EXPENSE_REPORT_TOTAL | — | — |
| 18 | ExpHdrExpenseStatusCode | EXPENSE_STATUS_CODE | — | ✅ |
| 19 | ExpHdrExpenseStatusDate | EXPENSE_STATUS_DATE | — | — |
| 20 | ExpHdrExportRejectCode | EXPORT_REJECT_CODE | — | — |
| 21 | ExpHdrExportRequestId | EXPORT_REQUEST_ID | — | — |
| 22 | ExpHdrFinalApprovalDate | FINAL_APPROVAL_DATE | — | ✅ |
| 23 | ExpHdrHoldingExpenseReportId | HOLDING_EXPENSE_REPORT_ID | — | — |
| 24 | ExpHdrImagedReceiptsReceivedDate | IMAGED_RECEIPTS_RECEIVED_DATE | — | — |
| 25 | ExpHdrImagedReceiptsStatusCode | IMAGED_RECEIPTS_STATUS_CODE | — | ✅ |
| 26 | ExpHdrLastAuditBy | LAST_AUDIT_BY | — | — |
| 27 | ExpHdrLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 28 | ExpHdrLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 29 | ExpHdrLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 30 | ExpHdrMissingImagesReason | MISSING_IMAGES_REASON | — | — |
| 31 | ExpHdrObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 32 | ExpHdrOrgId | ORG_ID | — | — |
| 33 | ExpHdrOverdueRcptCorrelationId | OVERDUE_RCPT_CORRELATION_ID | — | — |
| 34 | ExpHdrOverrideApproverId | OVERRIDE_APPROVER_ID | — | — |
| 35 | ExpHdrParentExpenseReportId | PARENT_EXPENSE_REPORT_ID | — | — |
| 36 | ExpHdrPaymentHoldCorrelationId | PAYMENT_HOLD_CORRELATION_ID | — | — |
| 37 | ExpHdrPaymentMethodCode | PAYMENT_METHOD_CODE | — | ✅ |
| 38 | ExpHdrPersonId | PERSON_ID | — | — |
| 39 | ExpHdrPreparerId | PREPARER_ID | — | — |
| 40 | ExpHdrPrntExpenseReportId | EXPENSE_REPORT_ID | — | — |
| 41 | ExpHdrPrntExpenseReportNum | EXPENSE_REPORT_NUM | — | ✅ |
| 42 | ExpHdrPurpose | PURPOSE | — | ✅ |
| 43 | ExpHdrReceiptsFilingNumber | RECEIPTS_FILING_NUMBER | — | ✅ |
| 44 | ExpHdrReceiptsReceivedDate | RECEIPTS_RECEIVED_DATE | — | ✅ |
| 45 | ExpHdrReceiptsStatusCode | RECEIPTS_STATUS_CODE | — | ✅ |
| 46 | ExpHdrReimbursementCurrencyCode | REIMBURSEMENT_CURRENCY_CODE | — | ✅ |
| 47 | ExpHdrReportSubmitDate | REPORT_SUBMIT_DATE | — | ✅ |
| 48 | ExpHdrShortpayTypeCode | SHORTPAY_TYPE_CODE | — | ✅ |
| 49 | ExpHdrTripId | TRIP_ID | — | — |
| 50 | ExpHdrUnappliedAdvancesJust | UNAPPLIED_ADVANCES_JUST | — | — |
| 51 | ExpHdrUnappliedCashAdvReason | UNAPPLIED_CASH_ADV_REASON | — | — |
| 52 | ExpHdrWorkflowCorrelationId | WORKFLOW_CORRELATION_ID | — | — |
| 53 | FullExpHdrReportCMC | REPORT_CREATION_METHOD_CODE | — | — |

### [[exm_expense_templates|EXM_EXPENSE_TEMPLATES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenseTemplatePEOAllowRcptMissingFlag | ALLOW_RCPT_MISSING_FLAG | — | — |
| 2 | ExpenseTemplatePEOCashReceiptReqFlag | CASH_RECEIPT_REQ_FLAG | — | — |
| 3 | ExpenseTemplatePEOCashReceiptReqLimit | CASH_RECEIPT_REQ_LIMIT | — | — |
| 4 | ExpenseTemplatePEOCcReceiptReqFlag | CC_RECEIPT_REQ_FLAG | — | — |
| 5 | ExpenseTemplatePEOCcReceiptReqLimit | CC_RECEIPT_REQ_LIMIT | — | — |
| 6 | ExpenseTemplatePEOCreatedBy | CREATED_BY | — | — |
| 7 | ExpenseTemplatePEOCreationDate | CREATION_DATE | — | — |
| 8 | ExpenseTemplatePEODescription | DESCRIPTION | — | — |
| 9 | ExpenseTemplatePEODfltCcExpTypeId | DFLT_CC_EXP_TYPE_ID | — | — |
| 10 | ExpenseTemplatePEODispRcptViolationFlag | DISP_RCPT_VIOLATION_FLAG | — | — |
| 11 | ExpenseTemplatePEOEnableCcMappingFlag | ENABLE_CC_MAPPING_FLAG | — | — |
| 12 | ExpenseTemplatePEOExpenseTemplateId | EXPENSE_TEMPLATE_ID | — | — |
| 13 | ExpenseTemplatePEOInactiveDate | INACTIVE_DATE | — | — |
| 14 | ExpenseTemplatePEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 15 | ExpenseTemplatePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | ExpenseTemplatePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 17 | ExpenseTemplatePEOName | NAME | — | ✅ |
| 18 | ExpenseTemplatePEONegativeRcptReqFlag | NEGATIVE_RCPT_REQ_FLAG | — | — |
| 19 | ExpenseTemplatePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | ExpenseTemplatePEOOrgId | ORG_ID | — | — |
| 21 | ExpenseTemplatePEOStartDate | START_DATE | — | — |

### [[exm_expense_types|EXM_EXPENSE_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenseTypePEOCategoryCode | CATEGORY_CODE | — | — |
| 2 | ExpenseTypePEOCcReceiptRequiredFlag | CC_RECEIPT_REQUIRED_FLAG | — | — |
| 3 | ExpenseTypePEOCcReceiptThreshold | CC_RECEIPT_THRESHOLD | — | — |
| 4 | ExpenseTypePEOCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 5 | ExpenseTypePEOCreatedBy | CREATED_BY | — | — |
| 6 | ExpenseTypePEOCreationDate | CREATION_DATE | — | — |
| 7 | ExpenseTypePEODefaultProjExpendType | DEFAULT_PROJ_EXPEND_TYPE | — | — |
| 8 | ExpenseTypePEODescription | DESCRIPTION | — | — |
| 9 | ExpenseTypePEODispRcptViolationFlag | DISP_RCPT_VIOLATION_FLAG | — | — |
| 10 | ExpenseTypePEOEnableProjectsFlag | ENABLE_PROJECTS_FLAG | — | — |
| 11 | ExpenseTypePEOEndDate | END_DATE | — | — |
| 12 | ExpenseTypePEOExpenseTemplateId | EXPENSE_TEMPLATE_ID | — | — |
| 13 | ExpenseTypePEOExpenseTypeId | EXPENSE_TYPE_ID | — | — |
| 14 | ExpenseTypePEOItemizationBehaviourCode | ITEMIZATION_BEHAVIOUR_CODE | — | — |
| 15 | ExpenseTypePEOItemizationOnlyFlag | ITEMIZATION_ONLY_FLAG | — | — |
| 16 | ExpenseTypePEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 17 | ExpenseTypePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 18 | ExpenseTypePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 19 | ExpenseTypePEOName | NAME | — | ✅ |
| 20 | ExpenseTypePEONegativeRcptReqCode | NEGATIVE_RCPT_REQ_CODE | — | — |
| 21 | ExpenseTypePEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 22 | ExpenseTypePEOOrgId1 | ORG_ID | — | — |
| 23 | ExpenseTypePEORcptRequiredProjFlag | RCPT_REQUIRED_PROJ_FLAG | — | — |
| 24 | ExpenseTypePEOReceiptRequiredFlag | RECEIPT_REQUIRED_FLAG | — | — |
| 25 | ExpenseTypePEOReceiptThreshold | RECEIPT_THRESHOLD | — | — |
| 26 | ExpenseTypePEOStartDate | START_DATE | — | — |
| 27 | ExpenseTypePEOTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | — |

### [[fun_bu_perf_v|FUN_BU_PERF_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitId | BU_ID | — | — |
| 2 | BusinessUnitPEOCreatedBy | CREATED_BY | — | — |
| 3 | BusinessUnitPEOCreationDate | CREATION_DATE | — | — |
| 4 | BusinessUnitPEODateFrom | DATE_FROM | — | — |
| 5 | BusinessUnitPEODateTo | DATE_TO | — | — |
| 6 | BusinessUnitPEOEnterpriseId | BUSINESS_GROUP_ID | — | — |
| 7 | BusinessUnitPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 8 | BusinessUnitPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | BusinessUnitPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | BusinessUnitPEOName | BU_NAME | — | — |
| 11 | BusinessUnitPEOStatus | STATUS | — | — |

### [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrganizationActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 2 | OrganizationBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | OrganizationCostAllocationKeyflexId | COST_ALLOCATION_KEYFLEX_ID | — | — |
| 4 | OrganizationCreatedBy | CREATED_BY | — | — |
| 5 | OrganizationCreationDate | CREATION_DATE | — | — |
| 6 | OrganizationEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 7 | OrganizationEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 8 | OrganizationEstablishmentId | ESTABLISHMENT_ID | — | — |
| 9 | OrganizationInternalAddressLine | INTERNAL_ADDRESS_LINE | — | — |
| 10 | OrganizationInternalExternalFlag | INTERNAL_EXTERNAL_FLAG | — | — |
| 11 | OrganizationLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 12 | OrganizationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | OrganizationLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | OrganizationLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 15 | OrganizationLocationId | LOCATION_ID | — | — |
| 16 | OrganizationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | OrganizationOrganizationId | ORGANIZATION_ID | — | — |
| 18 | OrganizationType | TYPE | — | — |

### [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BUPrimaryLedgerId | ORG_INFORMATION3 | — | — |
| 2 | OOrganizationInformationPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 3 | OOrganizationInformationPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 4 | OrgInfoEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 5 | OrgInfoEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 6 | OrgInfoOrgInformationId | ORG_INFORMATION_ID | — | — |
| 7 | OrganizationInformationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 8 | OrganizationInformationPEOCreatedBy | CREATED_BY | — | — |
| 9 | OrganizationInformationPEOCreationDate | CREATION_DATE | — | — |
| 10 | OrganizationInformationPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 11 | OrganizationInformationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | OrganizationInformationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | OrganizationInformationPEOLegislationCode | LEGISLATION_CODE | — | — |
| 14 | OrganizationInformationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | OrganizationInformationPEOOrgInformationContext | ORG_INFORMATION_CONTEXT | — | — |
| 16 | OrganizationInformationPEOOrganizationId | ORGANIZATION_ID | — | — |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenseAttendeePartyPartyId | PARTY_ID | — | — |
| 2 | ExpenseAttendeePartyPartyName | PARTY_NAME | — | — |
| 3 | ExpenseEmployerPartyPartyId | PARTY_ID | — | — |
| 4 | ExpenseEmployerPartyPartyName | PARTY_NAME | — | — |

### [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentActionCode | ACTION_CODE | — | — |
| 2 | AssignmentActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 3 | AssignmentAllowAsgOverrideFlag | ALLOW_ASG_OVERRIDE_FLAG | — | — |
| 4 | AssignmentApplicantRank | APPLICANT_RANK | — | — |
| 5 | AssignmentAssignmentId | ASSIGNMENT_ID | — | — |
| 6 | AssignmentAssignmentType | ASSIGNMENT_TYPE | — | — |
| 7 | AssignmentAutoEndFlag | AUTO_END_FLAG | — | — |
| 8 | AssignmentBargainingUnitCode | BARGAINING_UNIT_CODE | — | — |
| 9 | AssignmentBillingTitle | BILLING_TITLE | — | — |
| 10 | AssignmentBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 11 | AssignmentBusinessUnitId | BUSINESS_UNIT_ID | — | — |
| 12 | AssignmentCagrGradeDefId | CAGR_GRADE_DEF_ID | — | — |
| 13 | AssignmentCagrIdFlexNum | CAGR_ID_FLEX_NUM | — | — |
| 14 | AssignmentCollectiveAgreementId | COLLECTIVE_AGREEMENT_ID | — | — |
| 15 | AssignmentContractId | CONTRACT_ID | — | — |
| 16 | AssignmentCreatedBy | CREATED_BY | — | — |
| 17 | AssignmentCreationDate | CREATION_DATE | — | — |
| 18 | AssignmentDateProbationEnd | DATE_PROBATION_END | — | — |
| 19 | AssignmentDefaultCodeCombId | DEFAULT_CODE_COMB_ID | — | — |
| 20 | AssignmentDutiesType | DUTIES_TYPE | — | — |
| 21 | AssignmentEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 22 | AssignmentEffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | — |
| 23 | AssignmentEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 24 | AssignmentEmployeeCategory | EMPLOYEE_CATEGORY | — | — |
| 25 | AssignmentEmploymentCategory | EMPLOYMENT_CATEGORY | — | — |
| 26 | AssignmentEstablishmentId | ESTABLISHMENT_ID | — | — |
| 27 | AssignmentExpenseCheckAddress | EXPENSE_CHECK_ADDRESS | — | ✅ |
| 28 | AssignmentFreezeStartDate | FREEZE_START_DATE | — | — |
| 29 | AssignmentFreezeUntilDate | FREEZE_UNTIL_DATE | — | — |
| 30 | AssignmentFrequency | FREQUENCY | — | — |
| 31 | AssignmentFullPartTime | FULL_PART_TIME | — | — |
| 32 | AssignmentGradeId | GRADE_ID | — | — |
| 33 | AssignmentGradeLadderPgmId | GRADE_LADDER_PGM_ID | — | — |
| 34 | AssignmentHourlySalariedCode | HOURLY_SALARIED_CODE | — | — |
| 35 | AssignmentIdFlexNum | ID_FLEX_NUM | — | — |
| 36 | AssignmentInternalBuilding | INTERNAL_BUILDING | — | — |
| 37 | AssignmentInternalFloor | INTERNAL_FLOOR | — | — |
| 38 | AssignmentInternalLocation | INTERNAL_LOCATION | — | — |
| 39 | AssignmentInternalMailstop | INTERNAL_MAILSTOP | — | — |
| 40 | AssignmentInternalOfficeNumber | INTERNAL_OFFICE_NUMBER | — | — |
| 41 | AssignmentJobId | JOB_ID | — | — |
| 42 | AssignmentJobPostSourceName | JOB_POST_SOURCE_NAME | — | — |
| 43 | AssignmentLabourUnionMemberFlag | LABOUR_UNION_MEMBER_FLAG | — | — |
| 44 | AssignmentLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 45 | AssignmentLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 46 | AssignmentLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 47 | AssignmentLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 48 | AssignmentLegislationCode | LEGISLATION_CODE | — | — |
| 49 | AssignmentLinkageType | LINKAGE_TYPE | — | — |
| 50 | AssignmentLocationId | LOCATION_ID | — | — |
| 51 | AssignmentManagerFlag | MANAGER_FLAG | — | — |
| 52 | AssignmentName | ASSIGNMENT_NAME | — | — |
| 53 | AssignmentNormalHours | NORMAL_HOURS | — | — |
| 54 | AssignmentNoticePeriod | NOTICE_PERIOD | — | — |
| 55 | AssignmentNoticePeriodUom | NOTICE_PERIOD_UOM | — | — |
| 56 | AssignmentNumber | ASSIGNMENT_NUMBER | — | — |
| 57 | AssignmentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 58 | AssignmentOrganizationId | ORGANIZATION_ID | — | — |
| 59 | AssignmentParentAssignmentId | PARENT_ASSIGNMENT_ID | — | — |
| 60 | AssignmentPeopleGroupId | PEOPLE_GROUP_ID | — | — |
| 61 | AssignmentPeriodOfServiceId | PERIOD_OF_SERVICE_ID | — | — |
| 62 | AssignmentPermanentTemporaryFlag | PERMANENT_TEMPORARY_FLAG | — | — |
| 63 | AssignmentPersonId | PERSON_ID | — | — |
| 64 | AssignmentPersonReferredById | PERSON_REFERRED_BY_ID | — | — |
| 65 | AssignmentPersonTypeId | PERSON_TYPE_ID | — | — |
| 66 | AssignmentPoHeaderId | PO_HEADER_ID | — | — |
| 67 | AssignmentPoLineId | PO_LINE_ID | — | — |
| 68 | AssignmentPositionId | POSITION_ID | — | — |
| 69 | AssignmentPositionOverrideFlag | POSITION_OVERRIDE_FLAG | — | — |
| 70 | AssignmentPostingContentId | POSTING_CONTENT_ID | — | — |
| 71 | AssignmentPrimaryAssignmentFlag | PRIMARY_ASSIGNMENT_FLAG | — | — |
| 72 | AssignmentPrimaryFlag | PRIMARY_FLAG | — | — |
| 73 | AssignmentPrimaryWorkRelationFlag | PRIMARY_WORK_RELATION_FLAG | — | — |
| 74 | AssignmentPrimaryWorkTermsFlag | PRIMARY_WORK_TERMS_FLAG | — | — |
| 75 | AssignmentProbationPeriod | PROBATION_PERIOD | — | — |
| 76 | AssignmentProbationUnit | PROBATION_UNIT | — | — |
| 77 | AssignmentProjectTitle | PROJECT_TITLE | — | — |
| 78 | AssignmentProjectedAssignmentEnd | PROJECTED_ASSIGNMENT_END | — | — |
| 79 | AssignmentProjectedStartDate | PROJECTED_START_DATE | — | — |
| 80 | AssignmentProposedWorkerType | PROPOSED_WORKER_TYPE | — | — |
| 81 | AssignmentReasonCode | REASON_CODE | — | — |
| 82 | AssignmentRecordCreator | RECORD_CREATOR | — | — |
| 83 | AssignmentRecruiterId | RECRUITER_ID | — | — |
| 84 | AssignmentRecruitmentActivityId | RECRUITMENT_ACTIVITY_ID | — | — |
| 85 | AssignmentRetirementAge | RETIREMENT_AGE | — | — |
| 86 | AssignmentRetirementDate | RETIREMENT_DATE | — | — |
| 87 | AssignmentSalReviewPeriod | SAL_REVIEW_PERIOD | — | — |
| 88 | AssignmentSalReviewPeriodFrequency | SAL_REVIEW_PERIOD_FREQUENCY | — | — |
| 89 | AssignmentSequence | ASSIGNMENT_SEQUENCE | — | — |
| 90 | AssignmentSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 91 | AssignmentSoftCodingKeyflexId | SOFT_CODING_KEYFLEX_ID | — | — |
| 92 | AssignmentSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | — |
| 93 | AssignmentSourceType | SOURCE_TYPE | — | — |
| 94 | AssignmentSpecialCeilingStepId | SPECIAL_CEILING_STEP_ID | — | — |
| 95 | AssignmentStatusType | ASSIGNMENT_STATUS_TYPE | — | — |
| 96 | AssignmentStatusTypeId | ASSIGNMENT_STATUS_TYPE_ID | — | — |
| 97 | AssignmentStepEntryDate | STEP_ENTRY_DATE | — | — |
| 98 | AssignmentSystemPersonType | SYSTEM_PERSON_TYPE | — | — |
| 99 | AssignmentTaxAddressId | TAX_ADDRESS_ID | — | — |
| 100 | AssignmentTimeNormalFinish | TIME_NORMAL_FINISH | — | — |
| 101 | AssignmentTimeNormalStart | TIME_NORMAL_START | — | — |
| 102 | AssignmentVacancyId | VACANCY_ID | — | — |
| 103 | AssignmentVendorAssignmentNumber | VENDOR_ASSIGNMENT_NUMBER | — | — |
| 104 | AssignmentVendorEmployeeNumber | VENDOR_EMPLOYEE_NUMBER | — | — |
| 105 | AssignmentVendorId | VENDOR_ID | — | — |
| 106 | AssignmentVendorSiteId | VENDOR_SITE_ID | — | — |
| 107 | AssignmentWorkAtHome | WORK_AT_HOME | — | — |
| 108 | AssignmentWorkTermsAssignmentId | WORK_TERMS_ASSIGNMENT_ID | — | — |
| 109 | ExpAssignmentEffectiveStartDate | EFFECTIVE_START_DATE | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpAttPerCreatedByDisplayName | DISPLAY_NAME | — | — |
| 2 | ExpAttPerCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | ExpAttPerCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | ExpAttPerCreatedByPersonId | PERSON_ID | — | — |
| 5 | ExpAttPerCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | ExpAttPerUpdatedByDisplayName | DISPLAY_NAME | — | — |
| 7 | ExpAttPerUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | ExpAttPerUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | ExpAttPerUpdatedByPersonId | PERSON_ID | — | — |
| 10 | ExpAttPerUpdatedByPersonNameId | PERSON_NAME_ID | — | — |
| 11 | ExpHdrPersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 12 | ExpHdrPersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 13 | ExpHdrPersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 14 | ExpHdrPersonUpdatedByPersonId | PERSON_ID | — | — |
| 15 | ExpHdrPersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |
| 16 | ExpHdrPreparerNameDisplayName | DISPLAY_NAME | — | ✅ |
| 17 | ExpHdrPreparerNameEffEndDate | EFFECTIVE_END_DATE | — | — |
| 18 | ExpHdrPreparerNameEffStartDate | EFFECTIVE_START_DATE | — | — |
| 19 | ExpHdrPreparerNamePersonNameId | PERSON_NAME_ID | — | — |
| 20 | ExpPersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 21 | ExpPersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 22 | ExpPersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 23 | ExpPersonUpdatedByPersonId | PERSON_ID | — | — |
| 24 | ExpPersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |
| 25 | ExpPersoncreatedByPersonId | PERSON_ID | — | — |
| 26 | ExpenHdrPersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 27 | ExpenHdrPersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 28 | ExpenHdrPersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 29 | ExpenHdrPersonCreatedByPersonId | PERSON_ID | — | — |
| 30 | ExpenHdrPersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 31 | ExpenPersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 32 | ExpenPersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 33 | ExpenPersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 34 | ExpenPersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 35 | PersonNamePEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 36 | PersonNamePEOCreatedBy1 | CREATED_BY | — | — |
| 37 | PersonNamePEOCreationDate1 | CREATION_DATE | — | — |
| 38 | PersonNamePEODisplayName | DISPLAY_NAME | — | ✅ |
| 39 | PersonNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 40 | PersonNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 41 | PersonNamePEOFirstName | FIRST_NAME | — | — |
| 42 | PersonNamePEOFullName | FULL_NAME | — | — |
| 43 | PersonNamePEOHonors | HONORS | — | — |
| 44 | PersonNamePEOKnownAs | KNOWN_AS | — | — |
| 45 | PersonNamePEOLastName | LAST_NAME | — | — |
| 46 | PersonNamePEOLastUpdateDate1 | LAST_UPDATE_DATE | — | — |
| 47 | PersonNamePEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 48 | PersonNamePEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 49 | PersonNamePEOLegislationCode | LEGISLATION_CODE | — | — |
| 50 | PersonNamePEOListName | LIST_NAME | — | — |
| 51 | PersonNamePEOMiddleNames | MIDDLE_NAMES | — | — |
| 52 | PersonNamePEOMilitaryRank | MILITARY_RANK | — | — |
| 53 | PersonNamePEONamInformationCategory | NAM_INFORMATION_CATEGORY | — | — |
| 54 | PersonNamePEONameType | NAME_TYPE | — | — |
| 55 | PersonNamePEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 56 | PersonNamePEOOrderName | ORDER_NAME | — | — |
| 57 | PersonNamePEOPersonId1 | PERSON_ID | — | — |
| 58 | PersonNamePEOPersonNameId | PERSON_NAME_ID | — | — |
| 59 | PersonNamePEOPreNameAdjunct | PRE_NAME_ADJUNCT | — | — |
| 60 | PersonNamePEOPreviousLastName | PREVIOUS_LAST_NAME | — | — |
| 61 | PersonNamePEOSuffix | SUFFIX | — | — |
| 62 | PersonNamePEOTitle | TITLE | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpAttendeeCreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | ExpAttendeeCreatedByPersonId | PERSON_ID | — | — |
| 3 | ExpAttendeeCreatedByUserGuid | USER_GUID | — | — |
| 4 | ExpAttendeeCreatedByUserId | USER_ID | — | — |
| 5 | ExpAttendeeCreatedByUsername | USERNAME | — | — |
| 6 | ExpAttendeeUpdatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | ExpAttendeeUpdatedByPersonId | PERSON_ID | — | — |
| 8 | ExpAttendeeUpdatedByUserGuid | USER_GUID | — | — |
| 9 | ExpAttendeeUpdatedByUserId | USER_ID | — | — |
| 10 | ExpAttendeeUpdatedByUsername | USERNAME | — | — |
| 11 | ExpHdrUserUpdatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | ExpHdrUserUpdatedByPersonId | PERSON_ID | — | — |
| 13 | ExpHdrUserUpdatedByUserGuid | USER_GUID | — | — |
| 14 | ExpHdrUserUpdatedByUserId | USER_ID | — | — |
| 15 | ExpHdrUserUpdatedByUsername | USERNAME | — | — |
| 16 | ExpUserUpdatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | ExpUserUpdatedByPersonId | PERSON_ID | — | — |
| 18 | ExpUserUpdatedByUserGuid | USER_GUID | — | — |
| 19 | ExpUserUpdatedByUserId | USER_ID | — | — |
| 20 | ExpUserUpdatedByUsername | USERNAME | — | — |
| 21 | ExpenCreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 22 | ExpenCreatedByPersonId | PERSON_ID | — | — |
| 23 | ExpenCreatedByUserGuid | USER_GUID | — | — |
| 24 | ExpenCreatedByUserId | USER_ID | — | — |
| 25 | ExpenCreatedByUsername | USERNAME | — | — |
| 26 | ExpenHdrCreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 27 | ExpenHdrCreatedByPersonId | PERSON_ID | — | — |
| 28 | ExpenHdrCreatedByUserGuid | USER_GUID | — | — |
| 29 | ExpenHdrCreatedByUserId | USER_ID | — | — |
| 30 | ExpenHdrCreatedByUsername | USERNAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
