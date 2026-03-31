---
id: DOC-OTHER-PVO-FiscalPeriodExtractPVO
doc_type: system-doc
title: "FiscalPeriodExtractPVO — PVO Cross-Module"
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
  - FiscalPeriodExtractPVO
  - fiscalperiodextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FiscalPeriodExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fiscal Period Extract. Acessa as tabelas: GL_PERIODS, GL_PERIOD_SETS.

**Caminho:** `FscmTopModelAM.FinExtractAM.GlBiccExtractAM.FiscalPeriodExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 73 | 2 | 2 | 20 | 27% |

---

## 🔗 Tabelas Relacionadas

- [[gl_periods|GL_PERIODS]] — 70 atributos (2 PKs, 20 BICC)
- [[gl_period_sets|GL_PERIOD_SETS]] — 3 atributos

---

## ⚙️ Atributos

### [[gl_periods|GL_PERIODS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PeriodAdjustmentPeriodFlag | ADJUSTMENT_PERIOD_FLAG | — | ✅ |
| 2 | PeriodAttribute1 | ATTRIBUTE1 | — | — |
| 3 | PeriodAttribute2 | ATTRIBUTE2 | — | — |
| 4 | PeriodAttribute3 | ATTRIBUTE3 | — | — |
| 5 | PeriodAttribute4 | ATTRIBUTE4 | — | — |
| 6 | PeriodAttribute5 | ATTRIBUTE5 | — | — |
| 7 | PeriodAttribute6 | ATTRIBUTE6 | — | — |
| 8 | PeriodAttribute7 | ATTRIBUTE7 | — | — |
| 9 | PeriodAttribute8 | ATTRIBUTE8 | — | — |
| 10 | PeriodAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 11 | PeriodAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 12 | PeriodAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 13 | PeriodAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 14 | PeriodAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 15 | PeriodAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 16 | PeriodAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 17 | PeriodAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 18 | PeriodAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 19 | PeriodAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 20 | PeriodAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 21 | PeriodConfirmationStatus | CONFIRMATION_STATUS | — | ✅ |
| 22 | PeriodCreatedBy | CREATED_BY | — | ✅ |
| 23 | PeriodCreationDate | CREATION_DATE | — | ✅ |
| 24 | PeriodDescription | DESCRIPTION | — | ✅ |
| 25 | PeriodEndDate | END_DATE | — | ✅ |
| 26 | PeriodEnteredPeriodName | ENTERED_PERIOD_NAME | — | ✅ |
| 27 | PeriodGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 28 | PeriodGlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | — |
| 29 | PeriodGlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | — |
| 30 | PeriodGlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | — |
| 31 | PeriodGlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | — |
| 32 | PeriodGlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | — |
| 33 | PeriodGlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | — |
| 34 | PeriodGlobalAttribute16 | GLOBAL_ATTRIBUTE16 | — | — |
| 35 | PeriodGlobalAttribute17 | GLOBAL_ATTRIBUTE17 | — | — |
| 36 | PeriodGlobalAttribute18 | GLOBAL_ATTRIBUTE18 | — | — |
| 37 | PeriodGlobalAttribute19 | GLOBAL_ATTRIBUTE19 | — | — |
| 38 | PeriodGlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | — |
| 39 | PeriodGlobalAttribute20 | GLOBAL_ATTRIBUTE20 | — | — |
| 40 | PeriodGlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | — |
| 41 | PeriodGlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | — |
| 42 | PeriodGlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | — |
| 43 | PeriodGlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | — |
| 44 | PeriodGlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | — |
| 45 | PeriodGlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | — |
| 46 | PeriodGlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | — |
| 47 | PeriodGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 48 | PeriodGlobalAttributeDate1 | GLOBAL_ATTRIBUTE_DATE1 | — | — |
| 49 | PeriodGlobalAttributeDate2 | GLOBAL_ATTRIBUTE_DATE2 | — | — |
| 50 | PeriodGlobalAttributeDate3 | GLOBAL_ATTRIBUTE_DATE3 | — | — |
| 51 | PeriodGlobalAttributeDate4 | GLOBAL_ATTRIBUTE_DATE4 | — | — |
| 52 | PeriodGlobalAttributeDate5 | GLOBAL_ATTRIBUTE_DATE5 | — | — |
| 53 | PeriodGlobalAttributeNumber1 | GLOBAL_ATTRIBUTE_NUMBER1 | — | — |
| 54 | PeriodGlobalAttributeNumber2 | GLOBAL_ATTRIBUTE_NUMBER2 | — | — |
| 55 | PeriodGlobalAttributeNumber3 | GLOBAL_ATTRIBUTE_NUMBER3 | — | — |
| 56 | PeriodGlobalAttributeNumber4 | GLOBAL_ATTRIBUTE_NUMBER4 | — | — |
| 57 | PeriodGlobalAttributeNumber5 | GLOBAL_ATTRIBUTE_NUMBER5 | — | — |
| 58 | PeriodLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 59 | PeriodLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 60 | PeriodLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 61 | PeriodObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 62 | PeriodPeriodName | PERIOD_NAME | 🔑 | ✅ |
| 63 | PeriodPeriodNum | PERIOD_NUM | — | ✅ |
| 64 | PeriodPeriodSetName | PERIOD_SET_NAME | 🔑 | ✅ |
| 65 | PeriodPeriodType | PERIOD_TYPE | — | ✅ |
| 66 | PeriodPeriodYear | PERIOD_YEAR | — | ✅ |
| 67 | PeriodQuarterNum | QUARTER_NUM | — | ✅ |
| 68 | PeriodQuarterStartDate | QUARTER_START_DATE | — | ✅ |
| 69 | PeriodStartDate | START_DATE | — | ✅ |
| 70 | PeriodYearStartDate | YEAR_START_DATE | — | ✅ |

### [[gl_period_sets|GL_PERIOD_SETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccountingCalendarDescription | DESCRIPTION | — | — |
| 2 | AccountingCalendarPeriodSetName | PERIOD_SET_NAME | — | — |
| 3 | AccountingCalendarSecurityFlag | SECURITY_FLAG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
