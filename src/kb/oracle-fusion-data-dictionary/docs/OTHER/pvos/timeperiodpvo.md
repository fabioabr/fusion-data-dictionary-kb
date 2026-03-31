---
id: DOC-OTHER-PVO-TimePeriodPVO
doc_type: system-doc
title: "TimePeriodPVO — PVO Cross-Module"
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
  - TimePeriodPVO
  - timeperiodpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TimePeriodPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Time Period. Acessa as tabelas: PAY_TIME_PERIODS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmPayCoreAM.TimePeriodPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 32 | 1 | 1 | 28 | 88% |

---

## 🔗 Tabelas Relacionadas

- [[pay_time_periods|PAY_TIME_PERIODS]] — 32 atributos (1 PKs, 28 BICC)

---

## ⚙️ Atributos

### [[pay_time_periods|PAY_TIME_PERIODS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProcessSubDate | PROCESS_SUB_DATE | — | ✅ |
| 2 | TimePeriodId | TIME_PERIOD_ID | 🔑 | ✅ |
| 3 | TimePeriodPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | TimePeriodPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | TimePeriodPEOCutOffDate | CUT_OFF_DATE | — | ✅ |
| 6 | TimePeriodPEODefaultPaydate | DEFAULT_PAYDATE | — | ✅ |
| 7 | TimePeriodPEODescription | DESCRIPTION | — | ✅ |
| 8 | TimePeriodPEOEndDate | END_DATE | — | ✅ |
| 9 | TimePeriodPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | TimePeriodPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | TimePeriodPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | TimePeriodPEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 13 | TimePeriodPEOLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | ✅ |
| 14 | TimePeriodPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | TimePeriodPEOPayrollId | PAYROLL_ID | — | ✅ |
| 16 | TimePeriodPEOPayslipViewDate | PAYSLIP_VIEW_DATE | — | ✅ |
| 17 | TimePeriodPEOPeriodCategory | PERIOD_CATEGORY | — | ✅ |
| 18 | TimePeriodPEOPeriodName | PERIOD_NAME | — | ✅ |
| 19 | TimePeriodPEOPeriodNum | PERIOD_NUM | — | ✅ |
| 20 | TimePeriodPEOPeriodSetName | PERIOD_SET_NAME | — | ✅ |
| 21 | TimePeriodPEOPeriodType | PERIOD_TYPE | — | ✅ |
| 22 | TimePeriodPEOPeriodYear | PERIOD_YEAR | — | ✅ |
| 23 | TimePeriodPEOProcPeriodType | PROC_PERIOD_TYPE | — | ✅ |
| 24 | TimePeriodPEOQuarterNum | QUARTER_NUM | — | — |
| 25 | TimePeriodPEOQuickpayDisplayNumber | QUICKPAY_DISPLAY_NUMBER | — | — |
| 26 | TimePeriodPEORegularEarnDate | REGULAR_EARN_DATE | — | ✅ |
| 27 | TimePeriodPEORegularProcessDate | REGULAR_PROCESS_DATE | — | ✅ |
| 28 | TimePeriodPEORunDisplayNumber | RUN_DISPLAY_NUMBER | — | ✅ |
| 29 | TimePeriodPEOStartDate | START_DATE | — | ✅ |
| 30 | TimePeriodPEOStatus | STATUS | — | ✅ |
| 31 | TimePeriodPEOTimeDefinitionId | TIME_DEFINITION_ID | — | ✅ |
| 32 | TimePeriodPEOYearNumber | YEAR_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
