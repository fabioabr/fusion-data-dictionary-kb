---
id: DOC-OTHER-PVO-BillCalendarPVO
doc_type: system-doc
title: "BillCalendarPVO — PVO Cross-Module"
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
  - BillCalendarPVO
  - billcalendarpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BillCalendarPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Bill Calendar. Acessa as tabelas: BEN_BILL_CALENDAR, BEN_BILL_CYCLE.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmBenefitsAM.BillCalendarPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 108 | 2 | 1 | 21 | 19% |

---

## 🔗 Tabelas Relacionadas

- [[ben_bill_calendar|BEN_BILL_CALENDAR]] — 57 atributos (12 BICC)
- [[ben_bill_cycle|BEN_BILL_CYCLE]] — 51 atributos (1 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[ben_bill_calendar|BEN_BILL_CALENDAR]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BbcAttribute1 | BBC_ATTRIBUTE1 | — | — |
| 2 | BbcAttribute10 | BBC_ATTRIBUTE10 | — | — |
| 3 | BbcAttribute2 | BBC_ATTRIBUTE2 | — | — |
| 4 | BbcAttribute3 | BBC_ATTRIBUTE3 | — | — |
| 5 | BbcAttribute4 | BBC_ATTRIBUTE4 | — | — |
| 6 | BbcAttribute5 | BBC_ATTRIBUTE5 | — | — |
| 7 | BbcAttribute6 | BBC_ATTRIBUTE6 | — | — |
| 8 | BbcAttribute7 | BBC_ATTRIBUTE7 | — | — |
| 9 | BbcAttribute8 | BBC_ATTRIBUTE8 | — | — |
| 10 | BbcAttribute9 | BBC_ATTRIBUTE9 | — | — |
| 11 | BbcAttributeCategory | BBC_ATTRIBUTE_CATEGORY | — | — |
| 12 | BbcAttributeDate1 | BBC_ATTRIBUTE_DATE1 | — | — |
| 13 | BbcAttributeDate2 | BBC_ATTRIBUTE_DATE2 | — | — |
| 14 | BbcAttributeDate3 | BBC_ATTRIBUTE_DATE3 | — | — |
| 15 | BbcAttributeDate4 | BBC_ATTRIBUTE_DATE4 | — | — |
| 16 | BbcAttributeDate5 | BBC_ATTRIBUTE_DATE5 | — | — |
| 17 | BbcAttributeNumber1 | BBC_ATTRIBUTE_NUMBER1 | — | — |
| 18 | BbcAttributeNumber2 | BBC_ATTRIBUTE_NUMBER2 | — | — |
| 19 | BbcAttributeNumber3 | BBC_ATTRIBUTE_NUMBER3 | — | — |
| 20 | BbcAttributeNumber4 | BBC_ATTRIBUTE_NUMBER4 | — | — |
| 21 | BbcAttributeNumber5 | BBC_ATTRIBUTE_NUMBER5 | — | — |
| 22 | BillCalId | BILL_CAL_ID | — | ✅ |
| 23 | BillCalSource | BILL_CAL_SOURCE | — | ✅ |
| 24 | BillCalcRun | BILL_CALC_RUN | — | ✅ |
| 25 | BillCalendarPEOBillCycleId | BILL_CYCLE_ID | — | — |
| 26 | BillYear | BILL_YEAR | — | ✅ |
| 27 | BillingDate | BILLING_DATE | — | ✅ |
| 28 | BusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 29 | Comments | COMMENTS | — | ✅ |
| 30 | ConfigChar1 | CONFIG_CHAR_1 | — | — |
| 31 | ConfigChar2 | CONFIG_CHAR_2 | — | — |
| 32 | ConfigChar3 | CONFIG_CHAR_3 | — | — |
| 33 | ConfigChar4 | CONFIG_CHAR_4 | — | — |
| 34 | ConfigChar5 | CONFIG_CHAR_5 | — | — |
| 35 | ConfigDate1 | CONFIG_DATE_1 | — | — |
| 36 | ConfigDate2 | CONFIG_DATE_2 | — | — |
| 37 | ConfigDate3 | CONFIG_DATE_3 | — | — |
| 38 | ConfigDate4 | CONFIG_DATE_4 | — | — |
| 39 | ConfigDate5 | CONFIG_DATE_5 | — | — |
| 40 | ConfigNum1 | CONFIG_NUM_1 | — | — |
| 41 | ConfigNum2 | CONFIG_NUM_2 | — | — |
| 42 | ConfigNum3 | CONFIG_NUM_3 | — | — |
| 43 | ConfigNum4 | CONFIG_NUM_4 | — | — |
| 44 | ConfigNum5 | CONFIG_NUM_5 | — | — |
| 45 | CreatedBy | CREATED_BY | — | — |
| 46 | CreationDate | CREATION_DATE | — | — |
| 47 | EndDate | END_DATE | — | ✅ |
| 48 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 49 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 50 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 51 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 52 | PayTimePeriodId | PAY_TIME_PERIOD_ID | — | — |
| 53 | PayrollId | PAYROLL_ID | — | — |
| 54 | PeriodName | PERIOD_NAME | — | ✅ |
| 55 | PymntDueDt | PYMNT_DUE_DT | — | ✅ |
| 56 | PymntOverdueDt | PYMNT_OVERDUE_DT | — | ✅ |
| 57 | StartDate | START_DATE | — | ✅ |

### [[ben_bill_cycle|BEN_BILL_CYCLE]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BclAttribute1 | BCL_ATTRIBUTE1 | — | — |
| 2 | BclAttribute10 | BCL_ATTRIBUTE10 | — | — |
| 3 | BclAttribute2 | BCL_ATTRIBUTE2 | — | — |
| 4 | BclAttribute3 | BCL_ATTRIBUTE3 | — | — |
| 5 | BclAttribute4 | BCL_ATTRIBUTE4 | — | — |
| 6 | BclAttribute5 | BCL_ATTRIBUTE5 | — | — |
| 7 | BclAttribute6 | BCL_ATTRIBUTE6 | — | — |
| 8 | BclAttribute7 | BCL_ATTRIBUTE7 | — | — |
| 9 | BclAttribute8 | BCL_ATTRIBUTE8 | — | — |
| 10 | BclAttribute9 | BCL_ATTRIBUTE9 | — | — |
| 11 | BclAttributeCategory | BCL_ATTRIBUTE_CATEGORY | — | — |
| 12 | BclAttributeDate1 | BCL_ATTRIBUTE_DATE1 | — | — |
| 13 | BclAttributeDate2 | BCL_ATTRIBUTE_DATE2 | — | — |
| 14 | BclAttributeDate3 | BCL_ATTRIBUTE_DATE3 | — | — |
| 15 | BclAttributeDate4 | BCL_ATTRIBUTE_DATE4 | — | — |
| 16 | BclAttributeDate5 | BCL_ATTRIBUTE_DATE5 | — | — |
| 17 | BclAttributeNumber1 | BCL_ATTRIBUTE_NUMBER1 | — | — |
| 18 | BclAttributeNumber2 | BCL_ATTRIBUTE_NUMBER2 | — | — |
| 19 | BclAttributeNumber3 | BCL_ATTRIBUTE_NUMBER3 | — | — |
| 20 | BclAttributeNumber4 | BCL_ATTRIBUTE_NUMBER4 | — | — |
| 21 | BclAttributeNumber5 | BCL_ATTRIBUTE_NUMBER5 | — | — |
| 22 | BillCyclePEOBillCycleId | BILL_CYCLE_ID | 🔑 | ✅ |
| 23 | BillFreq | BILL_FREQ | — | ✅ |
| 24 | BillingDay | BILLING_DAY | — | ✅ |
| 25 | BusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 26 | ConfigChar11 | CONFIG_CHAR_1 | — | — |
| 27 | ConfigChar21 | CONFIG_CHAR_2 | — | — |
| 28 | ConfigChar31 | CONFIG_CHAR_3 | — | — |
| 29 | ConfigChar41 | CONFIG_CHAR_4 | — | — |
| 30 | ConfigChar51 | CONFIG_CHAR_5 | — | — |
| 31 | ConfigDate11 | CONFIG_DATE_1 | — | — |
| 32 | ConfigDate21 | CONFIG_DATE_2 | — | — |
| 33 | ConfigDate31 | CONFIG_DATE_3 | — | — |
| 34 | ConfigDate41 | CONFIG_DATE_4 | — | — |
| 35 | ConfigDate51 | CONFIG_DATE_5 | — | — |
| 36 | ConfigNum11 | CONFIG_NUM_1 | — | — |
| 37 | ConfigNum21 | CONFIG_NUM_2 | — | — |
| 38 | ConfigNum31 | CONFIG_NUM_3 | — | — |
| 39 | ConfigNum41 | CONFIG_NUM_4 | — | — |
| 40 | ConfigNum51 | CONFIG_NUM_5 | — | — |
| 41 | CreatedBy1 | CREATED_BY | — | — |
| 42 | CreationDate1 | CREATION_DATE | — | — |
| 43 | DaysOverdue | DAYS_OVERDUE | — | ✅ |
| 44 | Description | DESCRIPTION | — | ✅ |
| 45 | DueDay | DUE_DAY | — | ✅ |
| 46 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 47 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 48 | LastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 49 | Name | NAME | — | ✅ |
| 50 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 51 | Type | TYPE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
