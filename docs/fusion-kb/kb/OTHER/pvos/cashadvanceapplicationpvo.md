---
id: DOC-OTHER-PVO-CashAdvanceApplicationPVO
doc_type: system-doc
title: "CashAdvanceApplicationPVO — PVO Cross-Module"
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
  - CashAdvanceApplicationPVO
  - cashadvanceapplicationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CashAdvanceApplicationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cash Advance Application. Acessa as tabelas: EXM_CASH_ADVANCES, EXM_CASH_ADV_APPLICATIONS, EXM_TRIPS (+4).

**Caminho:** `FscmTopModelAM.FinExmEntrySharedAM.CashAdvanceApplicationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 104 | 7 | 1 | 33 | 32% |

---

## 🔗 Tabelas Relacionadas

- [[exm_cash_advances|EXM_CASH_ADVANCES]] — 34 atributos (18 BICC)
- [[exm_cash_adv_applications|EXM_CASH_ADV_APPLICATIONS]] — 15 atributos (1 PKs, 9 BICC)
- [[exm_trips|EXM_TRIPS]] — 2 atributos (1 BICC)
- [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]] — 4 atributos
- [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]] — 4 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 25 atributos (5 BICC)
- [[per_users|PER_USERS]] — 20 atributos

---

## ⚙️ Atributos

### [[exm_cash_advances|EXM_CASH_ADVANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CashAdvancePEOAdjustedAmount | ADJUSTED_AMOUNT | — | ✅ |
| 2 | CashAdvancePEOAmount | AMOUNT | — | ✅ |
| 3 | CashAdvancePEOApprovalCorrelationId | APPROVAL_CORRELATION_ID | — | — |
| 4 | CashAdvancePEOAssignmentId | ASSIGNMENT_ID | — | — |
| 5 | CashAdvancePEOAuditReturnReasonCode | AUDIT_RETURN_REASON_CODE | — | — |
| 6 | CashAdvancePEOCashAdvanceId | CASH_ADVANCE_ID | — | — |
| 7 | CashAdvancePEOCashAdvanceNumber | CASH_ADVANCE_NUMBER | — | ✅ |
| 8 | CashAdvancePEOCashAdvanceType | CASH_ADVANCE_TYPE | — | ✅ |
| 9 | CashAdvancePEOCreatedBy | CREATED_BY | — | ✅ |
| 10 | CashAdvancePEOCreationDate | CREATION_DATE | — | ✅ |
| 11 | CashAdvancePEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 12 | CashAdvancePEOExchangeRate | EXCHANGE_RATE | — | — |
| 13 | CashAdvancePEOExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 14 | CashAdvancePEOExportRejectCode | EXPORT_REJECT_CODE | — | — |
| 15 | CashAdvancePEOLastAuditedBy | LAST_AUDITED_BY | — | — |
| 16 | CashAdvancePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | CashAdvancePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 18 | CashAdvancePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 19 | CashAdvancePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | CashAdvancePEOOrgId | ORG_ID | — | — |
| 21 | CashAdvancePEOOverdueCorrelationId | OVERDUE_CORRELATION_ID | — | — |
| 22 | CashAdvancePEOPaymentAmount | PAYMENT_AMOUNT | — | ✅ |
| 23 | CashAdvancePEOPaymentCurrencyCode | PAYMENT_CURRENCY_CODE | — | ✅ |
| 24 | CashAdvancePEOPaymentMethodCode | PAYMENT_METHOD_CODE | — | — |
| 25 | CashAdvancePEOPersonId | PERSON_ID | — | — |
| 26 | CashAdvancePEOPurpose | PURPOSE | — | ✅ |
| 27 | CashAdvancePEORequestId | REQUEST_ID | — | — |
| 28 | CashAdvancePEOSettlementDate | SETTLEMENT_DATE | — | ✅ |
| 29 | CashAdvancePEOStatusCode | STATUS_CODE | — | ✅ |
| 30 | CashAdvancePEOSubmittedDate | SUBMITTED_DATE | — | ✅ |
| 31 | CashAdvancePEOTripEndDate | TRIP_END_DATE | — | ✅ |
| 32 | CashAdvancePEOTripId | TRIP_ID | — | — |
| 33 | CashAdvancePEOTripStartDate | TRIP_START_DATE | — | ✅ |
| 34 | CashAdvancePEOUnappliedAmount | UNAPPLIED_AMOUNT | — | ✅ |

### [[exm_cash_adv_applications|EXM_CASH_ADV_APPLICATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CashAdvanceApplEOAmount | AMOUNT | — | ✅ |
| 2 | CashAdvanceApplEOAppliedDate | APPLIED_DATE | — | ✅ |
| 3 | CashAdvanceApplEOCashAdvAppId | CASH_ADV_APP_ID | 🔑 | ✅ |
| 4 | CashAdvanceApplEOCashAdvanceId | CASH_ADVANCE_ID | — | ✅ |
| 5 | CashAdvanceApplEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | CashAdvanceApplEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | CashAdvanceApplEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 8 | CashAdvanceApplEOExchangeRate | EXCHANGE_RATE | — | — |
| 9 | CashAdvanceApplEOExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 10 | CashAdvanceApplEOExpenseReportId | EXPENSE_REPORT_ID | — | — |
| 11 | CashAdvanceApplEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | CashAdvanceApplEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | CashAdvanceApplEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | CashAdvanceApplEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | CashAdvanceApplEORequestId | REQUEST_ID | — | — |

### [[exm_trips|EXM_TRIPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TripPEOTripId | TRIP_ID | — | — |
| 2 | TripPEOTripName | TRIP_NAME | — | ✅ |

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

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CashAdvPEOLastAuditedEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | CashAdvPEOLastAuditedEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | CashAdvPEOLastAuditedPersonId1 | PERSON_ID | — | — |
| 4 | CashAdvPEOLastAuditedPersonNameId | PERSON_NAME_ID | — | — |
| 5 | CashAdvPersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 6 | CashAdvPersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 7 | CashAdvPersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 8 | CashAdvPersonCreatedByPersonId | PERSON_ID | — | — |
| 9 | CashAdvPersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 10 | CashAdvPersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 11 | CashAdvPersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 12 | CashAdvPersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 13 | CashAdvPersonUpdatedByPersonId | PERSON_ID | — | — |
| 14 | CashAdvPersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |
| 15 | CashAdvancePEOLastAuditedByDisplayName | DISPLAY_NAME | — | ✅ |
| 16 | PersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 17 | PersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 18 | PersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 19 | PersonCreatedByPersonId | PERSON_ID | — | — |
| 20 | PersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 21 | PersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 22 | PersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 23 | PersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 24 | PersonUpdatedByPersonId | PERSON_ID | — | — |
| 25 | PersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CashAdvCreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | CashAdvCreatedByPersonId | PERSON_ID | — | — |
| 3 | CashAdvCreatedByUserGuid | USER_GUID | — | — |
| 4 | CashAdvCreatedByUserId | USER_ID | — | — |
| 5 | CashAdvCreatedByUsername | USERNAME | — | — |
| 6 | CashAdvUserUpdatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | CashAdvUserUpdatedByPersonId | PERSON_ID | — | — |
| 8 | CashAdvUserUpdatedByUserGuid | USER_GUID | — | — |
| 9 | CashAdvUserUpdatedByUserId | USER_ID | — | — |
| 10 | CashAdvUserUpdatedByUsername | USERNAME | — | — |
| 11 | CreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | CreatedByPersonId | PERSON_ID | — | — |
| 13 | CreatedByUserGuid | USER_GUID | — | — |
| 14 | CreatedByUserId | USER_ID | — | — |
| 15 | CreatedByUsername | USERNAME | — | — |
| 16 | UserUpdatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | UserUpdatedByPersonId | PERSON_ID | — | — |
| 18 | UserUpdatedByUserGuid | USER_GUID | — | — |
| 19 | UserUpdatedByUserId | USER_ID | — | — |
| 20 | UserUpdatedByUsername | USERNAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
