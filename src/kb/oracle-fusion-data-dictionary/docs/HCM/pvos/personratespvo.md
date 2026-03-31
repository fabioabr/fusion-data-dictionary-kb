---
id: DOC-HCM-PVO-PersonRatesPVO
doc_type: system-doc
title: "PersonRatesPVO — PVO Human Capital Management"
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
  - PersonRatesPVO
  - personratespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PersonRatesPVO

## 📌 Visão Geral

Extrai as taxas de compensação dos colaboradores no ciclo de Compensation Workbench, com componentes e taxas de câmbio. Suporta cálculos de remuneração total em múltiplas moedas.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.CompensationAM.PersonRatesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 45 | 2 | 2 | 45 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cmp_cwb_person_rates|CMP_CWB_PERSON_RATES]] — 41 atributos (2 PKs, 41 BICC)
- [[cmp_cwb_xchg|CMP_CWB_XCHG]] — 4 atributos (4 BICC)

---

## ⚙️ Atributos

### [[cmp_cwb_person_rates|CMP_CWB_PERSON_RATES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonEventId | PERSON_EVENT_ID | 🔑 | ✅ |
| 2 | PersonRatesPEOAssignmentId | ASSIGNMENT_ID | — | ✅ |
| 3 | PersonRatesPEOCompPostedDate | COMP_POSTED_DATE | — | ✅ |
| 4 | PersonRatesPEOCompPostingDate | COMP_POSTING_DATE | — | ✅ |
| 5 | PersonRatesPEOComponentId | COMPONENT_ID | 🔑 | ✅ |
| 6 | PersonRatesPEOCreatedBy | CREATED_BY | — | ✅ |
| 7 | PersonRatesPEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | PersonRatesPEOCurrency | CURRENCY | — | ✅ |
| 9 | PersonRatesPEOEligFlag | ELIG_FLAG | — | ✅ |
| 10 | PersonRatesPEOEligOverrideDate | ELIG_OVERRIDE_DATE | — | ✅ |
| 11 | PersonRatesPEOEligOverridePersonId | ELIG_OVERRIDE_PERSON_ID | — | ✅ |
| 12 | PersonRatesPEOEligSalVal | ELIG_SAL_VAL | — | ✅ |
| 13 | PersonRatesPEOEmpBdgtMaxVal | EMP_BDGT_MAX_VAL | — | ✅ |
| 14 | PersonRatesPEOEmpBdgtMinVal | EMP_BDGT_MIN_VAL | — | ✅ |
| 15 | PersonRatesPEOEmpBdgtVal | EMP_BDGT_VAL | — | ✅ |
| 16 | PersonRatesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | PersonRatesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 18 | PersonRatesPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 19 | PersonRatesPEOMisc1Val | MISC1_VAL | — | ✅ |
| 20 | PersonRatesPEOMisc2Val | MISC2_VAL | — | ✅ |
| 21 | PersonRatesPEOMisc3Val | MISC3_VAL | — | ✅ |
| 22 | PersonRatesPEOMisc4Val | MISC4_VAL | — | ✅ |
| 23 | PersonRatesPEOMisc5Val | MISC5_VAL | — | ✅ |
| 24 | PersonRatesPEOMisc6Val | MISC6_VAL | — | ✅ |
| 25 | PersonRatesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 26 | PersonRatesPEOPeriodId | PERIOD_ID | — | ✅ |
| 27 | PersonRatesPEOPersonId | PERSON_ID | — | ✅ |
| 28 | PersonRatesPEOPlanId | PLAN_ID | — | ✅ |
| 29 | PersonRatesPEOPriorCycleEffectiveDate | PRIOR_WS_VAL_DATE | — | ✅ |
| 30 | PersonRatesPEOPriorEligSalVal | PRIOR_ELIG_SAL_VAL | — | ✅ |
| 31 | PersonRatesPEOPriorWsVal | PRIOR_WS_VAL | — | ✅ |
| 32 | PersonRatesPEOPriorWsValDate | PRIOR_WS_VAL_DATE | — | ✅ |
| 33 | PersonRatesPEORecMaxVal | REC_MAX_VAL | — | ✅ |
| 34 | PersonRatesPEORecMinVal | REC_MIN_VAL | — | ✅ |
| 35 | PersonRatesPEORecVal | REC_VAL | — | ✅ |
| 36 | PersonRatesPEOWsMaxVal | WS_MAX_VAL | — | ✅ |
| 37 | PersonRatesPEOWsMinVal | WS_MIN_VAL | — | ✅ |
| 38 | PersonRatesPEOWsVal | WS_VAL | — | ✅ |
| 39 | PersonRatesPEOWsValLastUpdBy | WS_VAL_LAST_UPD_BY | — | ✅ |
| 40 | PersonRatesPEOWsValLastUpdDate | WS_VAL_LAST_UPD_DATE | — | ✅ |
| 41 | PersonRatesPEOWsValOrigUpdBy | WS_VAL_ORIG_UPD_BY | — | ✅ |

### [[cmp_cwb_xchg|CMP_CWB_XCHG]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExchangeRatePEOCurrency | CURRENCY | — | ✅ |
| 2 | ExchangeRatePEOPeriodId | PERIOD_ID | — | ✅ |
| 3 | ExchangeRatePEOPlanId | PLAN_ID | — | ✅ |
| 4 | ExchangeRatePEOXchgRate | XCHG_RATE | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
