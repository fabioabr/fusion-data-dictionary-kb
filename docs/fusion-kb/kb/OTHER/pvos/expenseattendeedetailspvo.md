---
id: DOC-OTHER-PVO-ExpenseAttendeeDetailsPVO
doc_type: system-doc
title: "ExpenseAttendeeDetailsPVO — PVO Cross-Module"
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
  - ExpenseAttendeeDetailsPVO
  - expenseattendeedetailspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ExpenseAttendeeDetailsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Expense Attendee Details. Acessa as tabelas: EXM_EXPENSES, EXM_EXPENSE_ATTENDEES, EXM_EXPENSE_REPORTS (+2).

**Caminho:** `FscmTopModelAM.FinExmEntrySharedAM.ExpenseAttendeeDetailsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 41 | 5 | 1 | 14 | 34% |

---

## 🔗 Tabelas Relacionadas

- [[exm_expenses|EXM_EXPENSES]] — 1 atributos
- [[exm_expense_attendees|EXM_EXPENSE_ATTENDEES]] — 19 atributos (1 PKs, 12 BICC)
- [[exm_expense_reports|EXM_EXPENSE_REPORTS]] — 1 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos (2 BICC)
- [[per_users|PER_USERS]] — 10 atributos

---

## ⚙️ Atributos

### [[exm_expenses|EXM_EXPENSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpExpenseId | EXPENSE_ID | — | — |

### [[exm_expense_attendees|EXM_EXPENSE_ATTENDEES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenseAttendeePEOAmount | AMOUNT | — | — |
| 2 | ExpenseAttendeePEOAttendeePartyId | ATTENDEE_PARTY_ID | — | — |
| 3 | ExpenseAttendeePEOAttendeeType | ATTENDEE_TYPE | — | ✅ |
| 4 | ExpenseAttendeePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 5 | ExpenseAttendeePEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | ExpenseAttendeePEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | ExpenseAttendeePEOEmployeeFlag | EMPLOYEE_FLAG | — | ✅ |
| 8 | ExpenseAttendeePEOEmployerAddress | EMPLOYER_ADDRESS | — | ✅ |
| 9 | ExpenseAttendeePEOEmployerName | EMPLOYER_NAME | — | ✅ |
| 10 | ExpenseAttendeePEOEmployerPartyId | EMPLOYER_PARTY_ID | — | — |
| 11 | ExpenseAttendeePEOExpenseAttendeeId | EXPENSE_ATTENDEE_ID | 🔑 | ✅ |
| 12 | ExpenseAttendeePEOExpenseId | EXPENSE_ID | — | — |
| 13 | ExpenseAttendeePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | ExpenseAttendeePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | ExpenseAttendeePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | ExpenseAttendeePEOName | NAME | — | ✅ |
| 17 | ExpenseAttendeePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | ExpenseAttendeePEOTaxIdentifier | TAX_IDENTIFIER | — | ✅ |
| 19 | ExpenseAttendeePEOTitle | TITLE | — | ✅ |

### [[exm_expense_reports|EXM_EXPENSE_REPORTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpHdrExpenseReportId | EXPENSE_REPORT_ID | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpAttPerCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | ExpAttPerCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | ExpAttPerCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | ExpAttPerCreatedByPersonId | PERSON_ID | — | — |
| 5 | ExpAttPerCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | ExpAttPerUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 7 | ExpAttPerUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | ExpAttPerUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | ExpAttPerUpdatedByPersonId | PERSON_ID | — | — |
| 10 | ExpAttPerUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

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

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
