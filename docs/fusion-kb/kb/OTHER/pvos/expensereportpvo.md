---
id: DOC-OTHER-PVO-ExpenseReportPVO
doc_type: system-doc
title: "ExpenseReportPVO — PVO Cross-Module"
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
  - ExpenseReportPVO
  - expensereportpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ExpenseReportPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Expense Report. Acessa as tabelas: EXM_EXPENSE_REPORTS, FUN_BU_PERF_V, GL_LEDGERS (+5).

**Caminho:** `FscmTopModelAM.FinExmEntrySharedAM.ExpenseReportPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 301 | 8 | 1 | 31 | 10% |

---

## 🔗 Tabelas Relacionadas

- [[exm_expense_reports|EXM_EXPENSE_REPORTS]] — 116 atributos (1 PKs, 24 BICC)
- [[fun_bu_perf_v|FUN_BU_PERF_V]] — 1 atributos
- [[gl_ledgers|GL_LEDGERS]] — 86 atributos (1 BICC)
- [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]] — 4 atributos
- [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]] — 4 atributos
- [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]] — 8 atributos (1 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 72 atributos (5 BICC)
- [[per_users|PER_USERS]] — 10 atributos

---

## ⚙️ Atributos

### [[exm_expense_reports|EXM_EXPENSE_REPORTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApplyCashAdvFlag | APPLY_CASH_ADV_FLAG | — | — |
| 2 | AssignmentId | ASSIGNMENT_ID | — | — |
| 3 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 4 | AttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 5 | AttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 6 | AttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 7 | AttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 8 | AttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 9 | AttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 10 | AttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 11 | AttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 12 | AttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 13 | AttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 14 | AttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 15 | AttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 16 | AttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 17 | AttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 18 | AttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 19 | AuditCode | AUDIT_CODE | — | ✅ |
| 20 | AuditReturnReasonCode | AUDIT_RETURN_REASON_CODE | — | ✅ |
| 21 | AwtGroupId | AWT_GROUP_ID | — | — |
| 22 | BothpayFlag | BOTHPAY_FLAG | — | — |
| 23 | CashExpensePaidDate | CASH_EXPENSE_PAID_DATE | — | ✅ |
| 24 | CreatedBy | CREATED_BY | — | ✅ |
| 25 | CreationDate | CREATION_DATE | — | ✅ |
| 26 | CurrentApproverId | CURRENT_APPROVER_ID | — | — |
| 27 | ExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 28 | ExpRepProcessingId | EXP_REP_PROCESSING_ID | — | — |
| 29 | ExpenseReportDate | EXPENSE_REPORT_DATE | — | ✅ |
| 30 | ExpenseReportId | EXPENSE_REPORT_ID | 🔑 | ✅ |
| 31 | ExpenseReportNum | EXPENSE_REPORT_NUM | — | ✅ |
| 32 | ExpenseReportTotal | EXPENSE_REPORT_TOTAL | — | ✅ |
| 33 | ExpenseStatusCode | EXPENSE_STATUS_CODE | — | ✅ |
| 34 | ExpenseStatusDate | EXPENSE_STATUS_DATE | — | — |
| 35 | ExportRejectCode | EXPORT_REJECT_CODE | — | — |
| 36 | ExportRequestId | EXPORT_REQUEST_ID | — | — |
| 37 | FinalApprovalDate | FINAL_APPROVAL_DATE | — | ✅ |
| 38 | FullReportCMC | REPORT_CREATION_METHOD_CODE | — | — |
| 39 | HoldingExpenseReportId | HOLDING_EXPENSE_REPORT_ID | — | — |
| 40 | ImagedReceiptsReceivedDate | IMAGED_RECEIPTS_RECEIVED_DATE | — | — |
| 41 | ImagedReceiptsStatusCode | IMAGED_RECEIPTS_STATUS_CODE | — | ✅ |
| 42 | LastAuditBy | LAST_AUDIT_BY | — | — |
| 43 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 44 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 45 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 46 | MissingImagesReason | MISSING_IMAGES_REASON | — | — |
| 47 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 48 | OrgId | ORG_ID | — | — |
| 49 | OverdueRcptCorrelationId | OVERDUE_RCPT_CORRELATION_ID | — | — |
| 50 | OverrideApproverId | OVERRIDE_APPROVER_ID | — | — |
| 51 | ParentExpReportApplyCashAdvFlag | APPLY_CASH_ADV_FLAG | — | — |
| 52 | ParentExpReportAssignmentId | ASSIGNMENT_ID | — | — |
| 53 | ParentExpReportAuditCode | AUDIT_CODE | — | — |
| 54 | ParentExpReportAuditReturnReasonCode | AUDIT_RETURN_REASON_CODE | — | — |
| 55 | ParentExpReportAwtGroupId | AWT_GROUP_ID | — | — |
| 56 | ParentExpReportBothpayFlag | BOTHPAY_FLAG | — | — |
| 57 | ParentExpReportCashExpensePaidDate | CASH_EXPENSE_PAID_DATE | — | — |
| 58 | ParentExpReportCreatedBy | CREATED_BY | — | — |
| 59 | ParentExpReportCreationDate | CREATION_DATE | — | — |
| 60 | ParentExpReportCurrentApproverId | CURRENT_APPROVER_ID | — | — |
| 61 | ParentExpReportExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 62 | ParentExpReportExpRepProcessingId | EXP_REP_PROCESSING_ID | — | — |
| 63 | ParentExpReportExpenseReportDate | EXPENSE_REPORT_DATE | — | — |
| 64 | ParentExpReportExpenseReportId | EXPENSE_REPORT_ID | — | — |
| 65 | ParentExpReportExpenseReportNum | EXPENSE_REPORT_NUM | — | ✅ |
| 66 | ParentExpReportExpenseReportTotal | EXPENSE_REPORT_TOTAL | — | — |
| 67 | ParentExpReportExpenseStatusCode | EXPENSE_STATUS_CODE | — | — |
| 68 | ParentExpReportExpenseStatusDate | EXPENSE_STATUS_DATE | — | — |
| 69 | ParentExpReportExportRejectCode | EXPORT_REJECT_CODE | — | — |
| 70 | ParentExpReportExportRequestId | EXPORT_REQUEST_ID | — | — |
| 71 | ParentExpReportFinalApprovalDate | FINAL_APPROVAL_DATE | — | — |
| 72 | ParentExpReportHoldingExpenseReportId | HOLDING_EXPENSE_REPORT_ID | — | — |
| 73 | ParentExpReportImagedReceiptsReceivedDate | IMAGED_RECEIPTS_RECEIVED_DATE | — | — |
| 74 | ParentExpReportImagedReceiptsStatusCode | IMAGED_RECEIPTS_STATUS_CODE | — | — |
| 75 | ParentExpReportLastAuditBy | LAST_AUDIT_BY | — | — |
| 76 | ParentExpReportLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 77 | ParentExpReportLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 78 | ParentExpReportLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 79 | ParentExpReportMissingImagesReason | MISSING_IMAGES_REASON | — | — |
| 80 | ParentExpReportObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 81 | ParentExpReportOrgId | ORG_ID | — | — |
| 82 | ParentExpReportOverdueRcptCorrelationId | OVERDUE_RCPT_CORRELATION_ID | — | — |
| 83 | ParentExpReportOverrideApproverId | OVERRIDE_APPROVER_ID | — | — |
| 84 | ParentExpReportParentExpenseReportId | PARENT_EXPENSE_REPORT_ID | — | — |
| 85 | ParentExpReportPaymentHoldCorrelationId | PAYMENT_HOLD_CORRELATION_ID | — | — |
| 86 | ParentExpReportPaymentMethodCode | PAYMENT_METHOD_CODE | — | — |
| 87 | ParentExpReportPersonId | PERSON_ID | — | — |
| 88 | ParentExpReportPreparerId | PREPARER_ID | — | — |
| 89 | ParentExpReportPurpose | PURPOSE | — | — |
| 90 | ParentExpReportReceiptsFilingNumber | RECEIPTS_FILING_NUMBER | — | — |
| 91 | ParentExpReportReceiptsReceivedDate | RECEIPTS_RECEIVED_DATE | — | — |
| 92 | ParentExpReportReceiptsStatusCode | RECEIPTS_STATUS_CODE | — | — |
| 93 | ParentExpReportReimbursementCurrencyCode | REIMBURSEMENT_CURRENCY_CODE | — | — |
| 94 | ParentExpReportReportCreationMethodCode | REPORT_CREATION_METHOD_CODE | — | — |
| 95 | ParentExpReportReportSubmitDate | REPORT_SUBMIT_DATE | — | — |
| 96 | ParentExpReportShortpayTypeCode | SHORTPAY_TYPE_CODE | — | — |
| 97 | ParentExpReportTripId | TRIP_ID | — | — |
| 98 | ParentExpReportUnappliedAdvancesJust | UNAPPLIED_ADVANCES_JUST | — | — |
| 99 | ParentExpReportUnappliedCashAdvReason | UNAPPLIED_CASH_ADV_REASON | — | — |
| 100 | ParentExpReportWorkflowCorrelationId | WORKFLOW_CORRELATION_ID | — | — |
| 101 | ParentExpenseReportId | PARENT_EXPENSE_REPORT_ID | — | — |
| 102 | PaymentHoldCorrelationId | PAYMENT_HOLD_CORRELATION_ID | — | — |
| 103 | PaymentMethodCode | PAYMENT_METHOD_CODE | — | ✅ |
| 104 | PersonId | PERSON_ID | — | — |
| 105 | PreparerId | PREPARER_ID | — | — |
| 106 | Purpose | PURPOSE | — | ✅ |
| 107 | ReceiptsFilingNumber | RECEIPTS_FILING_NUMBER | — | ✅ |
| 108 | ReceiptsReceivedDate | RECEIPTS_RECEIVED_DATE | — | ✅ |
| 109 | ReceiptsStatusCode | RECEIPTS_STATUS_CODE | — | ✅ |
| 110 | ReimbursementCurrencyCode | REIMBURSEMENT_CURRENCY_CODE | — | ✅ |
| 111 | ReportSubmitDate | REPORT_SUBMIT_DATE | — | ✅ |
| 112 | ShortpayTypeCode | SHORTPAY_TYPE_CODE | — | ✅ |
| 113 | TripId | TRIP_ID | — | — |
| 114 | UnappliedAdvancesJust | UNAPPLIED_ADVANCES_JUST | — | — |
| 115 | UnappliedCashAdvReason | UNAPPLIED_CASH_ADV_REASON | — | — |
| 116 | WorkflowCorrelationId | WORKFLOW_CORRELATION_ID | — | — |

### [[fun_bu_perf_v|FUN_BU_PERF_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BUBusinessUnitId | BU_ID | — | — |

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlLedgersAccountedPeriodType | ACCOUNTED_PERIOD_TYPE | — | — |
| 2 | GlLedgersAlcLedgerTypeCode | ALC_LEDGER_TYPE_CODE | — | — |
| 3 | GlLedgersAllowIntercompanyPostFlag | ALLOW_INTERCOMPANY_POST_FLAG | — | — |
| 4 | GlLedgersApDocSequencingOptionFlag | AP_DOC_SEQUENCING_OPTION_FLAG | — | — |
| 5 | GlLedgersArDocSequencingOptionFlag | AR_DOC_SEQUENCING_OPTION_FLAG | — | — |
| 6 | GlLedgersAutomateSecJrnlRevFlag | AUTOMATE_SEC_JRNL_REV_FLAG | — | — |
| 7 | GlLedgersAutomaticallyCreatedFlag | AUTOMATICALLY_CREATED_FLAG | — | — |
| 8 | GlLedgersAutorevAfterOpenPrdFlag | AUTOREV_AFTER_OPEN_PRD_FLAG | — | — |
| 9 | GlLedgersBalSegColumnName | BAL_SEG_COLUMN_NAME | — | — |
| 10 | GlLedgersBalSegValueOptionCode | BAL_SEG_VALUE_OPTION_CODE | — | — |
| 11 | GlLedgersBalSegValueSetId | BAL_SEG_VALUE_SET_ID | — | — |
| 12 | GlLedgersBudgetPeriodAvgRateType | BUDGET_PERIOD_AVG_RATE_TYPE | — | — |
| 13 | GlLedgersBudgetPeriodEndRateType | BUDGET_PERIOD_END_RATE_TYPE | — | — |
| 14 | GlLedgersChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 15 | GlLedgersCompleteFlag | COMPLETE_FLAG | — | — |
| 16 | GlLedgersCompletionStatusCode | COMPLETION_STATUS_CODE | — | — |
| 17 | GlLedgersConfigurationId | CONFIGURATION_ID | — | — |
| 18 | GlLedgersConsolidationLedgerFlag | CONSOLIDATION_LEDGER_FLAG | — | — |
| 19 | GlLedgersCreateJeFlag | CREATE_JE_FLAG | — | — |
| 20 | GlLedgersCreatedBy | CREATED_BY | — | — |
| 21 | GlLedgersCreationDate | CREATION_DATE | — | — |
| 22 | GlLedgersCriteriaSetId | CRITERIA_SET_ID | — | — |
| 23 | GlLedgersCumTransCodeCombinationId | CUM_TRANS_CODE_COMBINATION_ID | — | — |
| 24 | GlLedgersCurrencyCode | CURRENCY_CODE | — | — |
| 25 | GlLedgersDailyTranslationRateType | DAILY_TRANSLATION_RATE_TYPE | — | — |
| 26 | GlLedgersDescription | DESCRIPTION | — | — |
| 27 | GlLedgersEnableAutomaticTaxFlag | ENABLE_AUTOMATIC_TAX_FLAG | — | — |
| 28 | GlLedgersEnableAverageBalancesFlag | ENABLE_AVERAGE_BALANCES_FLAG | — | — |
| 29 | GlLedgersEnableBudgetaryControlFlag | ENABLE_BUDGETARY_CONTROL_FLAG | — | — |
| 30 | GlLedgersEnableJeApprovalFlag | ENABLE_JE_APPROVAL_FLAG | — | — |
| 31 | GlLedgersEnableReconciliationFlag | ENABLE_RECONCILIATION_FLAG | — | — |
| 32 | GlLedgersEnableRevalSsTrackFlag | ENABLE_REVAL_SS_TRACK_FLAG | — | — |
| 33 | GlLedgersEnableSecondaryTrackFlag | ENABLE_SECONDARY_TRACK_FLAG | — | — |
| 34 | GlLedgersEnfSeqDateCorrelationCode | ENF_SEQ_DATE_CORRELATION_CODE | — | — |
| 35 | GlLedgersFirstLedgerPeriodName | FIRST_LEDGER_PERIOD_NAME | — | — |
| 36 | GlLedgersFutureEnterablePeriodsLimit | FUTURE_ENTERABLE_PERIODS_LIMIT | — | — |
| 37 | GlLedgersImplicitAccessSetId | IMPLICIT_ACCESS_SET_ID | — | — |
| 38 | GlLedgersImplicitLedgerSetId | IMPLICIT_LEDGER_SET_ID | — | — |
| 39 | GlLedgersIntercoGainLossCcid | INTERCO_GAIN_LOSS_CCID | — | — |
| 40 | GlLedgersJrnlsGroupByDateFlag | JRNLS_GROUP_BY_DATE_FLAG | — | — |
| 41 | GlLedgersLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 42 | GlLedgersLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 43 | GlLedgersLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 44 | GlLedgersLatestEncumbranceYear | LATEST_ENCUMBRANCE_YEAR | — | — |
| 45 | GlLedgersLatestOpenedPeriodName | LATEST_OPENED_PERIOD_NAME | — | — |
| 46 | GlLedgersLeLedgerTypeCode | LE_LEDGER_TYPE_CODE | — | — |
| 47 | GlLedgersLedgerAttributes | LEDGER_ATTRIBUTES | — | — |
| 48 | GlLedgersLedgerCategoryCode | LEDGER_CATEGORY_CODE | — | — |
| 49 | GlLedgersLedgerId | LEDGER_ID | — | — |
| 50 | GlLedgersMgtSegColumnName | MGT_SEG_COLUMN_NAME | — | — |
| 51 | GlLedgersMgtSegValueOptionCode | MGT_SEG_VALUE_OPTION_CODE | — | — |
| 52 | GlLedgersMgtSegValueSetId | MGT_SEG_VALUE_SET_ID | — | — |
| 53 | GlLedgersName | NAME | — | — |
| 54 | GlLedgersNetClosingBalFlag | NET_CLOSING_BAL_FLAG | — | — |
| 55 | GlLedgersNetIncomeCodeCombinationId | NET_INCOME_CODE_COMBINATION_ID | — | — |
| 56 | GlLedgersObjectTypeCode | OBJECT_TYPE_CODE | — | — |
| 57 | GlLedgersObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 58 | GlLedgersPeriodAverageRateType | PERIOD_AVERAGE_RATE_TYPE | — | — |
| 59 | GlLedgersPeriodEndRateType | PERIOD_END_RATE_TYPE | — | — |
| 60 | GlLedgersPeriodSetName | PERIOD_SET_NAME | — | — |
| 61 | GlLedgersPopUpStatAccountFlag | POP_UP_STAT_ACCOUNT_FLAG | — | — |
| 62 | GlLedgersPriorPrdNotificationFlag | PRIOR_PRD_NOTIFICATION_FLAG | — | — |
| 63 | GlLedgersRequireBudgetJournalsFlag | REQUIRE_BUDGET_JOURNALS_FLAG | — | — |
| 64 | GlLedgersResEncumbCodeCombinationId | RES_ENCUMB_CODE_COMBINATION_ID | — | — |
| 65 | GlLedgersRetEarnCodeCombinationId | RET_EARN_CODE_COMBINATION_ID | — | — |
| 66 | GlLedgersRevalFromPriLgrCurr | REVAL_FROM_PRI_LGR_CURR | — | — |
| 67 | GlLedgersRoundingCodeCombinationId | ROUNDING_CODE_COMBINATION_ID | — | — |
| 68 | GlLedgersSequencingModeCode | SEQUENCING_MODE_CODE | — | — |
| 69 | GlLedgersShortName | SHORT_NAME | — | — |
| 70 | GlLedgersSlaAccountingMethodCode | SLA_ACCOUNTING_METHOD_CODE | — | — |
| 71 | GlLedgersSlaAccountingMethodType | SLA_ACCOUNTING_METHOD_TYPE | — | — |
| 72 | GlLedgersSlaBalByLedgerCurrFlag | SLA_BAL_BY_LEDGER_CURR_FLAG | — | — |
| 73 | GlLedgersSlaDescriptionLanguage | SLA_DESCRIPTION_LANGUAGE | — | — |
| 74 | GlLedgersSlaEnteredCurBalSusCcid | SLA_ENTERED_CUR_BAL_SUS_CCID | — | — |
| 75 | GlLedgersSlaLedgerCashBasisFlag | SLA_LEDGER_CASH_BASIS_FLAG | — | — |
| 76 | GlLedgersSlaLedgerCurBalSusCcid | SLA_LEDGER_CUR_BAL_SUS_CCID | — | — |
| 77 | GlLedgersSlaSequencingFlag | SLA_SEQUENCING_FLAG | — | — |
| 78 | GlLedgersSuspenseAllowedFlag | SUSPENSE_ALLOWED_FLAG | — | — |
| 79 | GlLedgersThresholdAmount | THRESHOLD_AMOUNT | — | — |
| 80 | GlLedgersTrackRoundingImbalanceFlag | TRACK_ROUNDING_IMBALANCE_FLAG | — | — |
| 81 | GlLedgersTransactionCalendarId | TRANSACTION_CALENDAR_ID | — | — |
| 82 | GlLedgersTranslateEodFlag | TRANSLATE_EOD_FLAG | — | — |
| 83 | GlLedgersTranslateQatdFlag | TRANSLATE_QATD_FLAG | — | — |
| 84 | GlLedgersTranslateYatdFlag | TRANSLATE_YATD_FLAG | — | — |
| 85 | GlLedgersUssglOptionCode | USSGL_OPTION_CODE | — | — |
| 86 | GlLedgersValidateJournalRefDate | VALIDATE_JOURNAL_REF_DATE | — | — |

### [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrganizationEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | OrganizationEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | OrganizationLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 4 | OrganizationOrganizationId | ORGANIZATION_ID | — | — |

### [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BUPrimaryLedgerId | ORG_INFORMATION3 | — | — |
| 2 | OrgInfoEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | OrgInfoEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | OrgInfoOrgInformationId | ORG_INFORMATION_ID | — | — |

### [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentAssignmentId | ASSIGNMENT_ID | — | — |
| 2 | AssignmentEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | AssignmentEffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | — |
| 4 | AssignmentEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 5 | AssignmentEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 6 | AssignmentExpenseCheckAddress | EXPENSE_CHECK_ADDRESS | — | ✅ |
| 7 | AssignmentLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 8 | AssignmentPersonId | PERSON_ID | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpHdrPreparerNameDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | ExpHdrPreparerNameEffEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | ExpHdrPreparerNameEffStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | ExpHdrPreparerNamePersonNameId | PERSON_NAME_ID | — | — |
| 5 | PersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 6 | PersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 7 | PersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 8 | PersonCreatedByPersonId | PERSON_ID | — | — |
| 9 | PersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 10 | PersonNamePEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 11 | PersonNamePEOCreatedBy1 | CREATED_BY | — | — |
| 12 | PersonNamePEOCreationDate1 | CREATION_DATE | — | — |
| 13 | PersonNamePEODisplayName | DISPLAY_NAME | — | ✅ |
| 14 | PersonNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 15 | PersonNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 16 | PersonNamePEOFirstName | FIRST_NAME | — | — |
| 17 | PersonNamePEOFullName | FULL_NAME | — | — |
| 18 | PersonNamePEOHonors | HONORS | — | — |
| 19 | PersonNamePEOKnownAs | KNOWN_AS | — | — |
| 20 | PersonNamePEOLastName | LAST_NAME | — | — |
| 21 | PersonNamePEOLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 22 | PersonNamePEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 23 | PersonNamePEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 24 | PersonNamePEOLegislationCode | LEGISLATION_CODE | — | — |
| 25 | PersonNamePEOListName | LIST_NAME | — | — |
| 26 | PersonNamePEOMiddleNames | MIDDLE_NAMES | — | — |
| 27 | PersonNamePEOMilitaryRank | MILITARY_RANK | — | — |
| 28 | PersonNamePEONamInformation1 | NAM_INFORMATION1 | — | — |
| 29 | PersonNamePEONamInformation10 | NAM_INFORMATION10 | — | — |
| 30 | PersonNamePEONamInformation11 | NAM_INFORMATION11 | — | — |
| 31 | PersonNamePEONamInformation12 | NAM_INFORMATION12 | — | — |
| 32 | PersonNamePEONamInformation13 | NAM_INFORMATION13 | — | — |
| 33 | PersonNamePEONamInformation14 | NAM_INFORMATION14 | — | — |
| 34 | PersonNamePEONamInformation15 | NAM_INFORMATION15 | — | — |
| 35 | PersonNamePEONamInformation16 | NAM_INFORMATION16 | — | — |
| 36 | PersonNamePEONamInformation17 | NAM_INFORMATION17 | — | — |
| 37 | PersonNamePEONamInformation18 | NAM_INFORMATION18 | — | — |
| 38 | PersonNamePEONamInformation19 | NAM_INFORMATION19 | — | — |
| 39 | PersonNamePEONamInformation2 | NAM_INFORMATION2 | — | — |
| 40 | PersonNamePEONamInformation20 | NAM_INFORMATION20 | — | — |
| 41 | PersonNamePEONamInformation21 | NAM_INFORMATION21 | — | — |
| 42 | PersonNamePEONamInformation22 | NAM_INFORMATION22 | — | — |
| 43 | PersonNamePEONamInformation23 | NAM_INFORMATION23 | — | — |
| 44 | PersonNamePEONamInformation24 | NAM_INFORMATION24 | — | — |
| 45 | PersonNamePEONamInformation25 | NAM_INFORMATION25 | — | — |
| 46 | PersonNamePEONamInformation26 | NAM_INFORMATION26 | — | — |
| 47 | PersonNamePEONamInformation27 | NAM_INFORMATION27 | — | — |
| 48 | PersonNamePEONamInformation28 | NAM_INFORMATION28 | — | — |
| 49 | PersonNamePEONamInformation29 | NAM_INFORMATION29 | — | — |
| 50 | PersonNamePEONamInformation3 | NAM_INFORMATION3 | — | — |
| 51 | PersonNamePEONamInformation30 | NAM_INFORMATION30 | — | — |
| 52 | PersonNamePEONamInformation4 | NAM_INFORMATION4 | — | — |
| 53 | PersonNamePEONamInformation5 | NAM_INFORMATION5 | — | — |
| 54 | PersonNamePEONamInformation6 | NAM_INFORMATION6 | — | — |
| 55 | PersonNamePEONamInformation7 | NAM_INFORMATION7 | — | — |
| 56 | PersonNamePEONamInformation8 | NAM_INFORMATION8 | — | — |
| 57 | PersonNamePEONamInformation9 | NAM_INFORMATION9 | — | — |
| 58 | PersonNamePEONamInformationCategory | NAM_INFORMATION_CATEGORY | — | — |
| 59 | PersonNamePEONameType | NAME_TYPE | — | — |
| 60 | PersonNamePEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 61 | PersonNamePEOOrderName | ORDER_NAME | — | — |
| 62 | PersonNamePEOPersonId1 | PERSON_ID | — | — |
| 63 | PersonNamePEOPersonNameId | PERSON_NAME_ID | — | — |
| 64 | PersonNamePEOPreNameAdjunct | PRE_NAME_ADJUNCT | — | — |
| 65 | PersonNamePEOPreviousLastName | PREVIOUS_LAST_NAME | — | — |
| 66 | PersonNamePEOSuffix | SUFFIX | — | — |
| 67 | PersonNamePEOTitle | TITLE | — | — |
| 68 | PersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 69 | PersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 70 | PersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 71 | PersonUpdatedByPersonId | PERSON_ID | — | — |
| 72 | PersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserCreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | UserCreatedByPersonId | PERSON_ID | — | — |
| 3 | UserCreatedByUserGuid | USER_GUID | — | — |
| 4 | UserCreatedByUserId | USER_ID | — | — |
| 5 | UserCreatedByUsername | USERNAME | — | — |
| 6 | UserUpdatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | UserUpdatedByPersonId | PERSON_ID | — | — |
| 8 | UserUpdatedByUserGuid | USER_GUID | — | — |
| 9 | UserUpdatedByUserId | USER_ID | — | — |
| 10 | UserUpdatedByUsername | USERNAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
