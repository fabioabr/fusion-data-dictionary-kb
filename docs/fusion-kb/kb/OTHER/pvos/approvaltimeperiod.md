---
id: DOC-OTHER-PVO-ApprovalTimePeriod
doc_type: system-doc
title: "ApprovalTimePeriod — PVO Cross-Module"
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
  - ApprovalTimePeriod
  - approvaltimeperiod
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ApprovalTimePeriod

## 📌 Visão Geral

View Object para extração BICC de dados de Approval Time Period. Acessa as tabelas: HWM_RP_TM_PERIODS_B, HWM_RP_TM_PERIODS_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.TimePeriodsAM.ApprovalTimePeriod`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 36 | 2 | 1 | 18 | 50% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_rp_tm_periods_b|HWM_RP_TM_PERIODS_B]] — 25 atributos (1 PKs, 15 BICC)
- [[hwm_rp_tm_periods_tl|HWM_RP_TM_PERIODS_TL]] — 11 atributos (3 BICC)

---

## ⚙️ Atributos

### [[hwm_rp_tm_periods_b|HWM_RP_TM_PERIODS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RepeatingTimePeriodPEOAccrualUsage | ACCRUAL_USAGE | — | — |
| 2 | RepeatingTimePeriodPEOApprovalUsage | APPROVAL_USAGE | — | — |
| 3 | RepeatingTimePeriodPEOBalanceUsage | BALANCE_USAGE | — | — |
| 4 | RepeatingTimePeriodPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | RepeatingTimePeriodPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | RepeatingTimePeriodPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 7 | RepeatingTimePeriodPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | RepeatingTimePeriodPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | RepeatingTimePeriodPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | RepeatingTimePeriodPEOModuleId | MODULE_ID | — | — |
| 11 | RepeatingTimePeriodPEOMonthType | MONTH_TYPE | — | ✅ |
| 12 | RepeatingTimePeriodPEOMultiple | MULTIPLE | — | ✅ |
| 13 | RepeatingTimePeriodPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | RepeatingTimePeriodPEOOneOrMany | ONE_OR_MANY | — | ✅ |
| 15 | RepeatingTimePeriodPEOOvertimeUsage | OVERTIME_USAGE | — | — |
| 16 | RepeatingTimePeriodPEOPeriodCd | PERIOD_CD | — | ✅ |
| 17 | RepeatingTimePeriodPEOPeriodClass | PERIOD_CLASS | — | ✅ |
| 18 | RepeatingTimePeriodPEOPeriodLength | PERIOD_LENGTH | — | ✅ |
| 19 | RepeatingTimePeriodPEOPeriodStartDate | PERIOD_START_DATE | — | ✅ |
| 20 | RepeatingTimePeriodPEOPeriodType | PERIOD_TYPE | — | — |
| 21 | RepeatingTimePeriodPEOReferenceDate | REFERENCE_DATE | — | ✅ |
| 22 | RepeatingTimePeriodPEORepeatingTmPeriodId | REPEATING_TM_PERIOD_ID | 🔑 | ✅ |
| 23 | RepeatingTimePeriodPEORuleUsage | RULE_USAGE | — | — |
| 24 | RepeatingTimePeriodPEOTimeEntryUsage | TIME_ENTRY_USAGE | — | — |
| 25 | RepeatingTimePeriodPEOWeekType | WEEK_TYPE | — | ✅ |

### [[hwm_rp_tm_periods_tl|HWM_RP_TM_PERIODS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RepeatingTimePeriodTlPEOCreatedBy | CREATED_BY | — | — |
| 2 | RepeatingTimePeriodTlPEOCreationDate | CREATION_DATE | — | — |
| 3 | RepeatingTimePeriodTlPEODescription | DESCRIPTION | — | ✅ |
| 4 | RepeatingTimePeriodTlPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 5 | RepeatingTimePeriodTlPEOLanguage | LANGUAGE | — | — |
| 6 | RepeatingTimePeriodTlPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | RepeatingTimePeriodTlPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | RepeatingTimePeriodTlPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | RepeatingTimePeriodTlPEOName | NAME | — | ✅ |
| 10 | RepeatingTimePeriodTlPEORepeatingTmPeriodId | REPEATING_TM_PERIOD_ID | — | — |
| 11 | RepeatingTimePeriodTlPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
