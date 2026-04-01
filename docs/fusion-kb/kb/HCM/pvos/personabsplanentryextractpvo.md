---
id: DOC-HCM-PVO-PersonAbsPlanEntryExtractPVO
doc_type: system-doc
title: "PersonAbsPlanEntryExtractPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - PersonAbsPlanEntryExtractPVO
  - personabsplanentryextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PersonAbsPlanEntryExtractPVO

## 📌 Visão Geral

Extrai as inscrições de colaboradores em planos de ausência, com unidades, fator de pagamento e vínculo ao plano. Suporta análise de elegibilidade e consumo de licenças e afastamentos.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.HcmGblAbsencesBiccExtractAM.PersonAbsPlanEntryExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 30 | 1 | 1 | 29 | 97% |

---

## 🔗 Tabelas Relacionadas

- [[anc_per_abs_plan_entries|ANC_PER_ABS_PLAN_ENTRIES]] — 30 atributos (1 PKs, 29 BICC)

---

## ⚙️ Atributos

### [[anc_per_abs_plan_entries|ANC_PER_ABS_PLAN_ENTRIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbsUnits | ABS_UNITS | — | ✅ |
| 2 | AbsencePayFactor | ABSENCE_PAY_FACTOR | — | ✅ |
| 3 | AbsencePlanId | ABSENCE_PLAN_ID | — | ✅ |
| 4 | AssignmentId | ASSIGNMENT_ID | — | ✅ |
| 5 | CreatedBy | CREATED_BY | — | ✅ |
| 6 | CreationDate | CREATION_DATE | — | ✅ |
| 7 | EndDate | END_DATE | — | ✅ |
| 8 | EndDatetime | END_DATETIME | — | ✅ |
| 9 | EndTime | END_TIME | — | ✅ |
| 10 | EnterpriseId | ENTERPRISE_ID | — | ✅ |
| 11 | EntitlementDate | ENTITLEMENT_DATE | — | ✅ |
| 12 | HeaderId | HEADER_ID | — | ✅ |
| 13 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 15 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 17 | PerAbsPlanEntryId | PER_ABS_PLAN_ENTRY_ID | 🔑 | ✅ |
| 18 | PerAbsPlnSummEntryId | PER_ABS_PLN_SUMM_ENTRY_ID | — | ✅ |
| 19 | PerAbsTypeEntryId | PER_ABS_TYPE_ENTRY_ID | — | ✅ |
| 20 | PerAbsenceEntryId | PER_ABSENCE_ENTRY_ID | — | ✅ |
| 21 | PerAccrualEntryDtlId | PER_ACCRUAL_ENTRY_DTL_ID | — | — |
| 22 | PersonId | PERSON_ID | — | ✅ |
| 23 | QualificationDate | QUALIFICATION_DATE | — | ✅ |
| 24 | RateDefinitionId | RATE_DEFINITION_ID | — | ✅ |
| 25 | ScheduledUnits | SCHEDULED_UNITS | — | ✅ |
| 26 | StartDate | START_DATE | — | ✅ |
| 27 | StartDatetime | START_DATETIME | — | ✅ |
| 28 | StartTime | START_TIME | — | ✅ |
| 29 | TmRecId | TM_REC_ID | — | ✅ |
| 30 | Uom | UOM | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
