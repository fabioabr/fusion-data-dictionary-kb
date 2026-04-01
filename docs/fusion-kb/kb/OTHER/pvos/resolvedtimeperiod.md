---
id: DOC-OTHER-PVO-ResolvedTimePeriod
doc_type: system-doc
title: "ResolvedTimePeriod — PVO Cross-Module"
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
  - ResolvedTimePeriod
  - resolvedtimeperiod
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ResolvedTimePeriod

## 📌 Visão Geral

View Object para extração BICC de dados de Resolved Time Period. Acessa as tabelas: HWM_RP_TM_PERIODS_B, HWM_RP_TM_PERIODS_TL, HWM_RP_TM_RESOLVED.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.TimePeriodsAM.ResolvedTimePeriod`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 47 | 3 | 1 | 34 | 72% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_rp_tm_periods_b|HWM_RP_TM_PERIODS_B]] — 25 atributos (20 BICC)
- [[hwm_rp_tm_periods_tl|HWM_RP_TM_PERIODS_TL]] — 11 atributos (3 BICC)
- [[hwm_rp_tm_resolved|HWM_RP_TM_RESOLVED]] — 11 atributos (1 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[hwm_rp_tm_periods_b|HWM_RP_TM_PERIODS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RepeatingTimePeriodPEOAccrualUsage | ACCRUAL_USAGE | — | ✅ |
| 2 | RepeatingTimePeriodPEOApprovalUsage | APPROVAL_USAGE | — | ✅ |
| 3 | RepeatingTimePeriodPEOBalanceUsage | BALANCE_USAGE | — | ✅ |
| 4 | RepeatingTimePeriodPEOCreatedBy1 | CREATED_BY | — | ✅ |
| 5 | RepeatingTimePeriodPEOCreationDate1 | CREATION_DATE | — | ✅ |
| 6 | RepeatingTimePeriodPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 7 | RepeatingTimePeriodPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | RepeatingTimePeriodPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | ✅ |
| 9 | RepeatingTimePeriodPEOModuleId | MODULE_ID | — | — |
| 10 | RepeatingTimePeriodPEOMonthType | MONTH_TYPE | — | ✅ |
| 11 | RepeatingTimePeriodPEOMultiple | MULTIPLE | — | ✅ |
| 12 | RepeatingTimePeriodPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 13 | RepeatingTimePeriodPEOOneOrMany | ONE_OR_MANY | — | ✅ |
| 14 | RepeatingTimePeriodPEOOvertimeUsage | OVERTIME_USAGE | — | ✅ |
| 15 | RepeatingTimePeriodPEOPeriodCd | PERIOD_CD | — | ✅ |
| 16 | RepeatingTimePeriodPEOPeriodClass | PERIOD_CLASS | — | ✅ |
| 17 | RepeatingTimePeriodPEOPeriodLength | PERIOD_LENGTH | — | ✅ |
| 18 | RepeatingTimePeriodPEOPeriodStartDate | PERIOD_START_DATE | — | ✅ |
| 19 | RepeatingTimePeriodPEOPeriodType | PERIOD_TYPE | — | — |
| 20 | RepeatingTimePeriodPEOReferenceDate | REFERENCE_DATE | — | ✅ |
| 21 | RepeatingTimePeriodPEORepeatingTmPeriodId1 | REPEATING_TM_PERIOD_ID | — | — |
| 22 | RepeatingTimePeriodPEORuleUsage | RULE_USAGE | — | ✅ |
| 23 | RepeatingTimePeriodPEOTimeEntryUsage | TIME_ENTRY_USAGE | — | ✅ |
| 24 | RepeatingTimePeriodPEOWeekType | WEEK_TYPE | — | ✅ |
| 25 | RepeatingTimePeriodPEOnterpriseId1 | ENTERPRISE_ID | — | — |

### [[hwm_rp_tm_periods_tl|HWM_RP_TM_PERIODS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RepeatingTimePeriodTranslationPEOCreatedBy1 | CREATED_BY | — | — |
| 2 | RepeatingTimePeriodTranslationPEOCreationDate1 | CREATION_DATE | — | — |
| 3 | RepeatingTimePeriodTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | RepeatingTimePeriodTranslationPEOEnterpriseId1 | ENTERPRISE_ID | — | — |
| 5 | RepeatingTimePeriodTranslationPEOLanguage | LANGUAGE | — | — |
| 6 | RepeatingTimePeriodTranslationPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 7 | RepeatingTimePeriodTranslationPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 8 | RepeatingTimePeriodTranslationPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 9 | RepeatingTimePeriodTranslationPEOName | NAME | — | ✅ |
| 10 | RepeatingTimePeriodTranslationPEORepeatingTmPeriodId1 | REPEATING_TM_PERIOD_ID | — | — |
| 11 | RepeatingTimePeriodTranslationPEOSourceLang | SOURCE_LANG | — | — |

### [[hwm_rp_tm_resolved|HWM_RP_TM_RESOLVED]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | EndDate | END_DATE | — | ✅ |
| 4 | EnterpriseId | ENTERPRISE_ID | — | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | RepeatingTmPeriodId | REPEATING_TM_PERIOD_ID | — | ✅ |
| 10 | ResolvedTmPeriodId | RESOLVED_TM_PERIOD_ID | 🔑 | ✅ |
| 11 | StartDate | START_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
