---
id: DOC-OTHER-PVO-ProjectResourcePVO
doc_type: system-doc
title: "ProjectResourcePVO — PVO Cross-Module"
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
  - ProjectResourcePVO
  - projectresourcepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectResourcePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Resource. Acessa as tabelas: HCM_LOOKUPS, PER_LDAP_REQUESTS, PJF_PROJECTS_ALL_B (+2).

**Caminho:** `FscmTopModelAM.PjtPrjResourceAM.ProjectResourcePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 52 | 5 | 1 | 31 | 60% |

---

## 🔗 Tabelas Relacionadas

- [[hcm_lookups|HCM_LOOKUPS]] — 3 atributos (1 BICC)
- [[per_ldap_requests|PER_LDAP_REQUESTS]] — 3 atributos
- [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]] — 4 atributos (1 BICC)
- [[pjt_prj_enterprise_resource_b|PJT_PRJ_ENTERPRISE_RESOURCE_B]] — 1 atributos
- [[pjt_project_resource|PJT_PROJECT_RESOURCE]] — 41 atributos (1 PKs, 29 BICC)

---

## ⚙️ Atributos

### [[hcm_lookups|HCM_LOOKUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LookupCode | LOOKUP_CODE | — | — |
| 2 | LookupType | LOOKUP_TYPE | — | — |
| 3 | SecurityAssignmentStatus | MEANING | — | ✅ |

### [[per_ldap_requests|PER_LDAP_REQUESTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LdapRequestId | LDAP_REQUEST_ID | — | — |
| 2 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 3 | RequestStatus | REQUEST_STATUS | — | — |

### [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CarryingOutOrganizationId | CARRYING_OUT_ORGANIZATION_ID | — | — |
| 2 | HoursPerDay | HOURS_PER_DAY | — | ✅ |
| 3 | OrgId | ORG_ID | — | — |
| 4 | ProjectId1 | PROJECT_ID | — | — |

### [[pjt_prj_enterprise_resource_b|PJT_PRJ_ENTERPRISE_RESOURCE_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MgrResourceId | RESOURCE_ID | — | — |

### [[pjt_project_resource|PJT_PROJECT_RESOURCE]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Allocation | ALLOCATION | — | ✅ |
| 2 | AssignmentStatusCode | ASSIGNMENT_STATUS_CODE | — | — |
| 3 | AssignmentType | ASSIGNMENT_TYPE | — | ✅ |
| 4 | BillablePercent | BILLABLE_PERCENT | — | ✅ |
| 5 | BillablePercentReasonCode | BILLABLE_PERCENT_REASON_CODE | — | ✅ |
| 6 | CreatedBy | CREATED_BY | — | ✅ |
| 7 | CreationDate | CREATION_DATE | — | ✅ |
| 8 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 9 | EndDateActive | END_DATE_ACTIVE | — | ✅ |
| 10 | ExpenseAmount | EXPENSE_AMOUNT | — | ✅ |
| 11 | HoursPerDay1 | HOURS_PER_DAY | — | ✅ |
| 12 | HoursPerDay2 | HOURS_PER_DAY2 | — | ✅ |
| 13 | HoursPerDay3 | HOURS_PER_DAY3 | — | ✅ |
| 14 | HoursPerDay4 | HOURS_PER_DAY4 | — | ✅ |
| 15 | HoursPerDay5 | HOURS_PER_DAY5 | — | ✅ |
| 16 | HoursPerDay6 | HOURS_PER_DAY6 | — | ✅ |
| 17 | HoursPerDay7 | HOURS_PER_DAY7 | — | ✅ |
| 18 | HoursPerInterval | HOURS_PER_INTERVAL | — | ✅ |
| 19 | LaborBillRate | LABOR_BILL_RATE | — | ✅ |
| 20 | LaborCostRate | LABOR_COST_RATE | — | ✅ |
| 21 | LaborEffort | LABOR_EFFORT | — | ✅ |
| 22 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 23 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 24 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 25 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 26 | PartyId | PARTY_ID | — | — |
| 27 | PersonId | PERSON_ID | — | — |
| 28 | ProjResourceId | PROJ_RESOURCE_ID | 🔑 | ✅ |
| 29 | ProjectId | PROJECT_ID | — | — |
| 30 | ProjectResourcePEOHoursPerDay | HOURS_PER_DAY | — | ✅ |
| 31 | ProjectResourceRequestId | PROJECT_RESOURCE_REQUEST_ID | — | — |
| 32 | ProjectRoleId | PROJECT_ROLE_ID | — | — |
| 33 | Rate | RATE | — | — |
| 34 | ResourceId | RESOURCE_ID | — | — |
| 35 | ResourceRequestId | RESOURCE_REQUEST_ID | — | — |
| 36 | ScheduleId | SCHEDULE_ID | — | — |
| 37 | StartDateActive | START_DATE_ACTIVE | — | ✅ |
| 38 | TrackTimeFlag | TRACK_TIME_FLAG | — | ✅ |
| 39 | UnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |
| 40 | UpRequestId | UP_REQUEST_ID | — | ✅ |
| 41 | UseProjCalendarHourFlag | USE_PROJ_CALENDAR_HOUR_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
