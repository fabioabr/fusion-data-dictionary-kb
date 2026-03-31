---
id: DOC-OTHER-PVO-CashAdvancePVO
doc_type: system-doc
title: "CashAdvancePVO — PVO Cross-Module"
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
  - CashAdvancePVO
  - cashadvancepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CashAdvancePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cash Advance. Acessa as tabelas: EXM_CASH_ADVANCES, EXM_TRIPS, HR_ALL_ORGANIZATION_UNITS_F (+3).

**Caminho:** `FscmTopModelAM.FinExmEntrySharedAM.CashAdvancePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 69 | 6 | 1 | 23 | 33% |

---

## 🔗 Tabelas Relacionadas

- [[exm_cash_advances|EXM_CASH_ADVANCES]] — 34 atributos (1 PKs, 19 BICC)
- [[exm_trips|EXM_TRIPS]] — 2 atributos (1 BICC)
- [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]] — 4 atributos
- [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]] — 4 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 15 atributos (3 BICC)
- [[per_users|PER_USERS]] — 10 atributos

---

## ⚙️ Atributos

### [[exm_cash_advances|EXM_CASH_ADVANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdjustedAmount | ADJUSTED_AMOUNT | — | ✅ |
| 2 | Amount | AMOUNT | — | ✅ |
| 3 | ApprovalCorrelationId | APPROVAL_CORRELATION_ID | — | — |
| 4 | AssignmentId | ASSIGNMENT_ID | — | — |
| 5 | AuditReturnReasonCode | AUDIT_RETURN_REASON_CODE | — | — |
| 6 | CashAdvanceId | CASH_ADVANCE_ID | 🔑 | ✅ |
| 7 | CashAdvanceNumber | CASH_ADVANCE_NUMBER | — | ✅ |
| 8 | CashAdvancePurpose | PURPOSE | — | ✅ |
| 9 | CashAdvanceStatus | STATUS_CODE | — | ✅ |
| 10 | CashAdvanceType | CASH_ADVANCE_TYPE | — | ✅ |
| 11 | CreatedBy | CREATED_BY | — | ✅ |
| 12 | CreationDate | CREATION_DATE | — | ✅ |
| 13 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 14 | ExchangeRate | EXCHANGE_RATE | — | — |
| 15 | ExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 16 | ExportRejectCode | EXPORT_REJECT_CODE | — | — |
| 17 | LastAuditedBy | LAST_AUDITED_BY | — | — |
| 18 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 19 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 20 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 21 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 22 | OrgId | ORG_ID | — | — |
| 23 | OverdueCorrelationId | OVERDUE_CORRELATION_ID | — | — |
| 24 | PaymentAmount | PAYMENT_AMOUNT | — | ✅ |
| 25 | PaymentCurrencyCode | PAYMENT_CURRENCY_CODE | — | ✅ |
| 26 | PaymentMethodCode | PAYMENT_METHOD_CODE | — | — |
| 27 | PersonId | PERSON_ID | — | — |
| 28 | RequestId | REQUEST_ID | — | — |
| 29 | SettlementDate | SETTLEMENT_DATE | — | ✅ |
| 30 | SubmittedDate | SUBMITTED_DATE | — | ✅ |
| 31 | TripEndDate | TRIP_END_DATE | — | ✅ |
| 32 | TripId | TRIP_ID | — | — |
| 33 | TripStartDate | TRIP_START_DATE | — | ✅ |
| 34 | UnappliedAmount | UNAPPLIED_AMOUNT | — | ✅ |

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
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | LastAuditedByDisplayName | DISPLAY_NAME | — | ✅ |
| 3 | LastAuditedByPersonId1 | PERSON_ID | — | — |
| 4 | LastAuditedByPersonNameId | PERSON_NAME_ID | — | — |
| 5 | LastAuditedEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 6 | PersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 7 | PersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | PersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | PersonCreatedByPersonId | PERSON_ID | — | — |
| 10 | PersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 11 | PersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 12 | PersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 13 | PersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 14 | PersonUpdatedByPersonId | PERSON_ID | — | — |
| 15 | PersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | CreatedByPersonId | PERSON_ID | — | — |
| 3 | CreatedByUserGuid | USER_GUID | — | — |
| 4 | CreatedByUserId | USER_ID | — | — |
| 5 | CreatedByUsername | USERNAME | — | — |
| 6 | UserUpdatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | UserUpdatedByPersonId | PERSON_ID | — | — |
| 8 | UserUpdatedByUserGuid | USER_GUID | — | — |
| 9 | UserUpdatedByUserId | USER_ID | — | — |
| 10 | UserUpdatedByUsername | USERNAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
