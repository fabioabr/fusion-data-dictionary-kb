---
id: DOC-GL-PVO-AbsPerPlanEnrollmentPVO
doc_type: system-doc
title: "AbsPerPlanEnrollmentPVO — PVO General Ledger"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - gl
  - data-dictionary
  - pvo
  - bicc
aliases:
  - AbsPerPlanEnrollmentPVO
  - absperplanenrollmentpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AbsPerPlanEnrollmentPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Abs Per Plan Enrollment. Acessa as tabelas: ANC_PER_PLAN_ENROLLMENT.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.GlobalAbsencesAM.AbsPerPlanEnrollmentPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 25 | 1 | 1 | 5 | 20% |

---

## 🔗 Tabelas Relacionadas

- [[anc_per_plan_enrollment|ANC_PER_PLAN_ENROLLMENT]] — 25 atributos (1 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[anc_per_plan_enrollment|ANC_PER_PLAN_ENROLLMENT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CeilingAmt | CEILING_AMT | — | — |
| 2 | CreatedBy | CREATED_BY | — | — |
| 3 | CreationDate | CREATION_DATE | — | — |
| 4 | EnrtEndDt | ENRT_END_DT | — | ✅ |
| 5 | EnrtStDt | ENRT_ST_DT | — | ✅ |
| 6 | EnterpriseId | ENTERPRISE_ID | — | — |
| 7 | LastAccrualRun | LAST_ACCRUAL_RUN | — | ✅ |
| 8 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | OperationType | OPERATION_TYPE | — | — |
| 13 | PayrollMappingId | PAYROLL_MAPPING_ID | — | — |
| 14 | PayrollStatus | PAYROLL_STATUS | — | — |
| 15 | PerEventId | PER_EVENT_ID | — | — |
| 16 | PerPlanEnrtId | PER_PLAN_ENRT_ID | 🔑 | ✅ |
| 17 | PersonId | PERSON_ID | — | — |
| 18 | PlanId | PLAN_ID | — | — |
| 19 | PrdOfSvcId | PRD_OF_SVC_ID | — | — |
| 20 | RecipientAlias | RECIPIENT_ALIAS | — | — |
| 21 | SourceEnrtId | SOURCE_ENRT_ID | — | — |
| 22 | Status | STATUS | — | — |
| 23 | WaitPeriodDurUnits | WAIT_PERIOD_DUR_UNITS | — | — |
| 24 | WaitPeriodDurUom | WAIT_PERIOD_DUR_UOM | — | — |
| 25 | WorkTermAsgId | WORK_TERM_ASG_ID | — | — |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
