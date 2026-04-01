---
id: DOC-OTHER-PVO-ExpenseReportHistoryPVO
doc_type: system-doc
title: "ExpenseReportHistoryPVO — PVO Cross-Module"
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
  - ExpenseReportHistoryPVO
  - expensereporthistorypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ExpenseReportHistoryPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Expense Report History. Acessa as tabelas: EXM_EXPENSE_REPORTS, EXM_EXP_REP_PROCESSING, PER_ALL_PEOPLE_F (+3).

**Caminho:** `FscmTopModelAM.FinExmEntrySharedAM.ExpenseReportHistoryPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 107 | 6 | 1 | 17 | 16% |

---

## 🔗 Tabelas Relacionadas

- [[exm_expense_reports|EXM_EXPENSE_REPORTS]] — 54 atributos (1 BICC)
- [[exm_exp_rep_processing|EXM_EXP_REP_PROCESSING]] — 21 atributos (1 PKs, 13 BICC)
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 5 atributos
- [[per_email_addresses|PER_EMAIL_ADDRESSES]] — 2 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 15 atributos (3 BICC)
- [[per_users|PER_USERS]] — 10 atributos

---

## ⚙️ Atributos

### [[exm_expense_reports|EXM_EXPENSE_REPORTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenseReportPEOApplyCashAdvFlag | APPLY_CASH_ADV_FLAG | — | — |
| 2 | ExpenseReportPEOAssignmentId | ASSIGNMENT_ID | — | — |
| 3 | ExpenseReportPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 4 | ExpenseReportPEOAuditCode | AUDIT_CODE | — | — |
| 5 | ExpenseReportPEOAuditReturnReasonCode1 | AUDIT_RETURN_REASON_CODE | — | — |
| 6 | ExpenseReportPEOAwtGroupId | AWT_GROUP_ID | — | — |
| 7 | ExpenseReportPEOBothpayFlag | BOTHPAY_FLAG | — | — |
| 8 | ExpenseReportPEOCashExpensePaidDate | CASH_EXPENSE_PAID_DATE | — | — |
| 9 | ExpenseReportPEOCreatedBy1 | CREATED_BY | — | — |
| 10 | ExpenseReportPEOCreationDate1 | CREATION_DATE | — | — |
| 11 | ExpenseReportPEOCurrentApproverId | CURRENT_APPROVER_ID | — | — |
| 12 | ExpenseReportPEOExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 13 | ExpenseReportPEOExpRepProcessingId1 | EXP_REP_PROCESSING_ID | — | — |
| 14 | ExpenseReportPEOExpenseReportDate | EXPENSE_REPORT_DATE | — | — |
| 15 | ExpenseReportPEOExpenseReportId | EXPENSE_REPORT_ID | — | — |
| 16 | ExpenseReportPEOExpenseReportNum | EXPENSE_REPORT_NUM | — | — |
| 17 | ExpenseReportPEOExpenseReportTotal | EXPENSE_REPORT_TOTAL | — | — |
| 18 | ExpenseReportPEOExpenseStatusCode1 | EXPENSE_STATUS_CODE | — | — |
| 19 | ExpenseReportPEOExpenseStatusDate | EXPENSE_STATUS_DATE | — | — |
| 20 | ExpenseReportPEOExportRejectCode1 | EXPORT_REJECT_CODE | — | — |
| 21 | ExpenseReportPEOExportRequestId1 | EXPORT_REQUEST_ID | — | — |
| 22 | ExpenseReportPEOFinalApprovalDate | FINAL_APPROVAL_DATE | — | — |
| 23 | ExpenseReportPEOHoldingExpenseReportId1 | HOLDING_EXPENSE_REPORT_ID | — | — |
| 24 | ExpenseReportPEOImagedReceiptsReceivedDate | IMAGED_RECEIPTS_RECEIVED_DATE | — | — |
| 25 | ExpenseReportPEOImagedReceiptsStatusCode1 | IMAGED_RECEIPTS_STATUS_CODE | — | — |
| 26 | ExpenseReportPEOLastAuditBy | LAST_AUDIT_BY | — | — |
| 27 | ExpenseReportPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | — |
| 28 | ExpenseReportPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 29 | ExpenseReportPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 30 | ExpenseReportPEOMissingImagesReason | MISSING_IMAGES_REASON | — | — |
| 31 | ExpenseReportPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 32 | ExpenseReportPEOOrgId | ORG_ID | — | — |
| 33 | ExpenseReportPEOOverdueRcptCorrelationId | OVERDUE_RCPT_CORRELATION_ID | — | — |
| 34 | ExpenseReportPEOOverrideApproverId | OVERRIDE_APPROVER_ID | — | — |
| 35 | ExpenseReportPEOParentExpenseReportId | PARENT_EXPENSE_REPORT_ID | — | — |
| 36 | ExpenseReportPEOPaymentHoldCorrelationId | PAYMENT_HOLD_CORRELATION_ID | — | — |
| 37 | ExpenseReportPEOPaymentMethodCode | PAYMENT_METHOD_CODE | — | — |
| 38 | ExpenseReportPEOPersonId | PERSON_ID | — | — |
| 39 | ExpenseReportPEOPreparerId | PREPARER_ID | — | — |
| 40 | ExpenseReportPEOPurpose | PURPOSE | — | — |
| 41 | ExpenseReportPEOReceiptsFilingNumber | RECEIPTS_FILING_NUMBER | — | — |
| 42 | ExpenseReportPEOReceiptsReceivedDate | RECEIPTS_RECEIVED_DATE | — | — |
| 43 | ExpenseReportPEOReceiptsStatusCode1 | RECEIPTS_STATUS_CODE | — | — |
| 44 | ExpenseReportPEOReimbursementCurrencyCode | REIMBURSEMENT_CURRENCY_CODE | — | — |
| 45 | ExpenseReportPEOReportCreationMethodCode | REPORT_CREATION_METHOD_CODE | — | — |
| 46 | ExpenseReportPEOReportSubmitDate | REPORT_SUBMIT_DATE | — | — |
| 47 | ExpenseReportPEOShortpayTypeCode | SHORTPAY_TYPE_CODE | — | — |
| 48 | ExpenseReportPEOTripId | TRIP_ID | — | — |
| 49 | ExpenseReportPEOUnappliedAdvancesJust | UNAPPLIED_ADVANCES_JUST | — | — |
| 50 | ExpenseReportPEOUnappliedCashAdvReason | UNAPPLIED_CASH_ADV_REASON | — | — |
| 51 | ExpenseReportPEOWorkflowCorrelationId | WORKFLOW_CORRELATION_ID | — | — |
| 52 | HoldingExpenseReportPEOExpenseReportId | EXPENSE_REPORT_ID | — | — |
| 53 | HoldingExpenseReportPEOExpenseReportNum | EXPENSE_REPORT_NUM | — | ✅ |
| 54 | HoldingExpenseReportPEOHoldingExpenseReportId | HOLDING_EXPENSE_REPORT_ID | — | — |

### [[exm_exp_rep_processing|EXM_EXP_REP_PROCESSING]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExmExpRepProcessingApprovalLevel | APPROVAL_LEVEL | — | ✅ |
| 2 | ExmExpRepProcessingAuditCode | AUDIT_CODE | — | ✅ |
| 3 | ExmExpRepProcessingAuditReturnReasonCode | AUDIT_RETURN_REASON_CODE | — | — |
| 4 | ExmExpRepProcessingCreatedBy | CREATED_BY | — | ✅ |
| 5 | ExmExpRepProcessingCreationDate | CREATION_DATE | — | ✅ |
| 6 | ExmExpRepProcessingEvent | EVENT | — | ✅ |
| 7 | ExmExpRepProcessingEventDate | EVENT_DATE | — | ✅ |
| 8 | ExmExpRepProcessingEventPerformerId | EVENT_PERFORMER_ID | — | — |
| 9 | ExmExpRepProcessingExpRepProcessingId | EXP_REP_PROCESSING_ID | 🔑 | ✅ |
| 10 | ExmExpRepProcessingExpenseReportId | EXPENSE_REPORT_ID | — | — |
| 11 | ExmExpRepProcessingExpenseStatusCode | EXPENSE_STATUS_CODE | — | ✅ |
| 12 | ExmExpRepProcessingExportRejectCode | EXPORT_REJECT_CODE | — | ✅ |
| 13 | ExmExpRepProcessingExportRequestId | EXPORT_REQUEST_ID | — | ✅ |
| 14 | ExmExpRepProcessingHoldingExpenseReportId | HOLDING_EXPENSE_REPORT_ID | — | ✅ |
| 15 | ExmExpRepProcessingImagedReceiptsStatusCode | IMAGED_RECEIPTS_STATUS_CODE | — | — |
| 16 | ExmExpRepProcessingLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | ExmExpRepProcessingLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 18 | ExmExpRepProcessingLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 19 | ExmExpRepProcessingNoteId | NOTE_ID | — | — |
| 20 | ExmExpRepProcessingObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 21 | ExmExpRepProcessingReceiptsStatusCode | RECEIPTS_STATUS_CODE | — | — |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PerformerPersonDetailsEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | PerformerPersonDetailsEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | PerformerPersonDetailsPersonId | PERSON_ID | — | — |
| 4 | PerformerPersonDetailsPersonNumber | PERSON_NUMBER | — | — |
| 5 | PerformerPersonDetailsPrimaryEmailId | PRIMARY_EMAIL_ID | — | — |

### [[per_email_addresses|PER_EMAIL_ADDRESSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PerformerPersonEmailEmailAddress | EMAIL_ADDRESS | — | — |
| 2 | PerformerPersonEmailEmailAddressId | EMAIL_ADDRESS_ID | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpRepPrcPerCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | ExpRepPrcPerCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | ExpRepPrcPerCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | ExpRepPrcPerCreatedByPersonId | PERSON_ID | — | — |
| 5 | ExpRepPrcPerCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | ExpRepPrcPerUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 7 | ExpRepPrcPerUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | ExpRepPrcPerUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | ExpRepPrcPerUpdatedByPersonId | PERSON_ID | — | — |
| 10 | ExpRepPrcPerUpdatedByPersonNameId | PERSON_NAME_ID | — | — |
| 11 | ExpRepPrcPerformerEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 12 | ExpRepPrcPerformerEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 13 | ExpRepPrcPerformerListName | LIST_NAME | — | ✅ |
| 14 | ExpRepPrcPerformerPersonId | PERSON_ID | — | — |
| 15 | ExpRepPrcPerformerPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpRepPrcCreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | ExpRepPrcCreatedByPersonId | PERSON_ID | — | — |
| 3 | ExpRepPrcCreatedByUserGuid | USER_GUID | — | — |
| 4 | ExpRepPrcCreatedByUserId | USER_ID | — | — |
| 5 | ExpRepPrcCreatedByUsername | USERNAME | — | — |
| 6 | ExpRepPrcUpdatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | ExpRepPrcUpdatedByPersonId | PERSON_ID | — | — |
| 8 | ExpRepPrcUpdatedByUserGuid | USER_GUID | — | — |
| 9 | ExpRepPrcUpdatedByUserId | USER_ID | — | — |
| 10 | ExpRepPrcUpdatedByUsername | USERNAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
