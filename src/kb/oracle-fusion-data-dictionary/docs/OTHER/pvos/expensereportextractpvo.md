---
id: DOC-OTHER-PVO-ExpenseReportExtractPVO
doc_type: system-doc
title: "ExpenseReportExtractPVO — PVO Cross-Module"
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
  - ExpenseReportExtractPVO
  - expensereportextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ExpenseReportExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Expense Report Extract. Acessa as tabelas: EXM_EXPENSE_REPORTS.

**Caminho:** `FscmTopModelAM.FinExtractAM.ExmBiccExtractAM.ExpenseReportExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 79 | 1 | 1 | 23 | 29% |

---

## 🔗 Tabelas Relacionadas

- [[exm_expense_reports|EXM_EXPENSE_REPORTS]] — 79 atributos (1 PKs, 23 BICC)

---

## ⚙️ Atributos

### [[exm_expense_reports|EXM_EXPENSE_REPORTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenseReportApplyCashAdvFlag | APPLY_CASH_ADV_FLAG | — | — |
| 2 | ExpenseReportAssignmentId | ASSIGNMENT_ID | — | ✅ |
| 3 | ExpenseReportAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 4 | ExpenseReportAttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 5 | ExpenseReportAttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 6 | ExpenseReportAttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 7 | ExpenseReportAttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 8 | ExpenseReportAttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 9 | ExpenseReportAttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 10 | ExpenseReportAttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 11 | ExpenseReportAttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 12 | ExpenseReportAttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 13 | ExpenseReportAttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 14 | ExpenseReportAttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 15 | ExpenseReportAttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 16 | ExpenseReportAttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 17 | ExpenseReportAttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 18 | ExpenseReportAttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 19 | ExpenseReportAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 20 | ExpenseReportAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 21 | ExpenseReportAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 22 | ExpenseReportAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 23 | ExpenseReportAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 24 | ExpenseReportAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 25 | ExpenseReportAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 26 | ExpenseReportAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 27 | ExpenseReportAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 28 | ExpenseReportAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 29 | ExpenseReportAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 30 | ExpenseReportAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 31 | ExpenseReportAuditCode | AUDIT_CODE | — | — |
| 32 | ExpenseReportAuditPriorMgrStatusCode | AUDIT_PRIOR_MGR_STATUS_CODE | — | — |
| 33 | ExpenseReportAuditReturnReasonCode | AUDIT_RETURN_REASON_CODE | — | — |
| 34 | ExpenseReportAwtGroupId | AWT_GROUP_ID | — | — |
| 35 | ExpenseReportBothpayFlag | BOTHPAY_FLAG | — | — |
| 36 | ExpenseReportCashExpensePaidDate | CASH_EXPENSE_PAID_DATE | — | — |
| 37 | ExpenseReportCreatedBy | CREATED_BY | — | — |
| 38 | ExpenseReportCreationDate | CREATION_DATE | — | ✅ |
| 39 | ExpenseReportCreationMethodCode | REPORT_CREATION_METHOD_CODE | — | ✅ |
| 40 | ExpenseReportCurrentApproverId | CURRENT_APPROVER_ID | — | — |
| 41 | ExpenseReportDate | EXPENSE_REPORT_DATE | — | ✅ |
| 42 | ExpenseReportExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 43 | ExpenseReportExpRepProcessingId | EXP_REP_PROCESSING_ID | — | — |
| 44 | ExpenseReportExpenseStatusCode | EXPENSE_STATUS_CODE | — | ✅ |
| 45 | ExpenseReportExpenseStatusDate | EXPENSE_STATUS_DATE | — | ✅ |
| 46 | ExpenseReportExportRejectCode | EXPORT_REJECT_CODE | — | ✅ |
| 47 | ExpenseReportExportRequestId | EXPORT_REQUEST_ID | — | — |
| 48 | ExpenseReportFinalApprovalDate | FINAL_APPROVAL_DATE | — | — |
| 49 | ExpenseReportHoldingExpenseReportId | HOLDING_EXPENSE_REPORT_ID | — | — |
| 50 | ExpenseReportId | EXPENSE_REPORT_ID | 🔑 | ✅ |
| 51 | ExpenseReportImagedReceiptsReceivedDate | IMAGED_RECEIPTS_RECEIVED_DATE | — | ✅ |
| 52 | ExpenseReportImagedReceiptsStatusCode | IMAGED_RECEIPTS_STATUS_CODE | — | ✅ |
| 53 | ExpenseReportLastAuditBy | LAST_AUDIT_BY | — | — |
| 54 | ExpenseReportLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 55 | ExpenseReportLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 56 | ExpenseReportLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 57 | ExpenseReportMissingImagesReason | MISSING_IMAGES_REASON | — | — |
| 58 | ExpenseReportNum | EXPENSE_REPORT_NUM | — | ✅ |
| 59 | ExpenseReportObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 60 | ExpenseReportOrgId | ORG_ID | — | ✅ |
| 61 | ExpenseReportOverdueRcptCorrelationId | OVERDUE_RCPT_CORRELATION_ID | — | — |
| 62 | ExpenseReportOverrideApproverId | OVERRIDE_APPROVER_ID | — | — |
| 63 | ExpenseReportParentExpenseReportId | PARENT_EXPENSE_REPORT_ID | — | ✅ |
| 64 | ExpenseReportPaymentHoldCorrelationId | PAYMENT_HOLD_CORRELATION_ID | — | — |
| 65 | ExpenseReportPaymentMethodCode | PAYMENT_METHOD_CODE | — | ✅ |
| 66 | ExpenseReportPersonId | PERSON_ID | — | ✅ |
| 67 | ExpenseReportPreparerId | PREPARER_ID | — | — |
| 68 | ExpenseReportPurpose | PURPOSE | — | ✅ |
| 69 | ExpenseReportReceiptsFilingNumber | RECEIPTS_FILING_NUMBER | — | — |
| 70 | ExpenseReportReceiptsReceivedDate | RECEIPTS_RECEIVED_DATE | — | ✅ |
| 71 | ExpenseReportReceiptsStatusCode | RECEIPTS_STATUS_CODE | — | ✅ |
| 72 | ExpenseReportReimbursementCurrencyCode | REIMBURSEMENT_CURRENCY_CODE | — | ✅ |
| 73 | ExpenseReportShortpayTypeCode | SHORTPAY_TYPE_CODE | — | — |
| 74 | ExpenseReportSubmitDate | REPORT_SUBMIT_DATE | — | ✅ |
| 75 | ExpenseReportTotal | EXPENSE_REPORT_TOTAL | — | ✅ |
| 76 | ExpenseReportTripId | TRIP_ID | — | — |
| 77 | ExpenseReportUnappliedAdvancesJust | UNAPPLIED_ADVANCES_JUST | — | — |
| 78 | ExpenseReportUnappliedCashAdvReason | UNAPPLIED_CASH_ADV_REASON | — | — |
| 79 | ExpenseReportWorkflowCorrelationId | WORKFLOW_CORRELATION_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
