---
id: DOC-GL-PVO-PersonAbsPlnSummaryEntPVO
doc_type: system-doc
title: "PersonAbsPlnSummaryEntPVO — PVO General Ledger"
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
  - PersonAbsPlnSummaryEntPVO
  - personabsplnsummaryentpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PersonAbsPlnSummaryEntPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Person Abs Pln Summary Ent. Acessa as tabelas: ANC_PER_ABS_PLN_SUMM_ENT, PER_ALL_PEOPLE_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.GlobalAbsencesAM.PersonAbsPlnSummaryEntPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 28 | 2 | 1 | 13 | 46% |

---

## 🔗 Tabelas Relacionadas

- [[anc_per_abs_pln_summ_ent|ANC_PER_ABS_PLN_SUMM_ENT]] — 25 atributos (1 PKs, 12 BICC)
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 3 atributos (1 BICC)

---

## ⚙️ Atributos

### [[anc_per_abs_pln_summ_ent|ANC_PER_ABS_PLN_SUMM_ENT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActivityCd | ACTIVITY_CD | — | ✅ |
| 2 | CalcDate | CALC_DATE | — | ✅ |
| 3 | CaseId | CASE_ID | — | — |
| 4 | CreatedBy | CREATED_BY | — | — |
| 5 | CreationDate | CREATION_DATE | — | — |
| 6 | EndDatetime | END_DATETIME | — | ✅ |
| 7 | EnterpriseId | ENTERPRISE_ID | — | — |
| 8 | EntitlementDate | ENTITLEMENT_DATE | — | — |
| 9 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | OvrrdRsnCd | OVRRD_RSN_CD | — | ✅ |
| 14 | PayFactor | PAY_FACTOR | — | ✅ |
| 15 | PerAbsPlnSummEntryId | PER_ABS_PLN_SUMM_ENTRY_ID | 🔑 | ✅ |
| 16 | PerAbsTypeEntryId | PER_ABS_TYPE_ENTRY_ID | — | — |
| 17 | PerAbsenceEntryId | PER_ABSENCE_ENTRY_ID | — | — |
| 18 | PersonId | PERSON_ID | — | — |
| 19 | PlanId | PLAN_ID | — | — |
| 20 | PlanPeriodStartDate | PLAN_PERIOD_START_DATE | — | ✅ |
| 21 | QualificationDate | QUALIFICATION_DATE | — | ✅ |
| 22 | Source | SOURCE | — | ✅ |
| 23 | StartDatetime | START_DATETIME | — | ✅ |
| 24 | Units | UNITS | — | ✅ |
| 25 | Uom | UOM | — | — |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | PersonId1 | PERSON_ID | — | — |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
