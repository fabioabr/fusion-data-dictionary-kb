---
id: DOC-OTHER-PVO-PeriodStatusPVO
doc_type: system-doc
title: "PeriodStatusPVO — PVO Cross-Module"
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
  - PeriodStatusPVO
  - periodstatuspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PeriodStatusPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Period Status. Acessa as tabelas: CST_PERIOD_STATUSES, GL_PERIODS, GL_PERIOD_SETS.

**Caminho:** `FscmTopModelAM.CstPeriodStatusAM.PeriodStatusPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 92 | 3 | 3 | 18 | 20% |

---

## 🔗 Tabelas Relacionadas

- [[cst_period_statuses|CST_PERIOD_STATUSES]] — 16 atributos (3 PKs, 16 BICC)
- [[gl_periods|GL_PERIODS]] — 60 atributos (1 BICC)
- [[gl_period_sets|GL_PERIOD_SETS]] — 16 atributos (1 BICC)

---

## ⚙️ Atributos

### [[cst_period_statuses|CST_PERIOD_STATUSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostBookId | COST_BOOK_ID | 🔑 | ✅ |
| 2 | CostOrgId | COST_ORG_ID | 🔑 | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | EndDate | END_DATE | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | PeriodName | PERIOD_NAME | 🔑 | ✅ |
| 11 | PeriodNum | PERIOD_NUM | — | ✅ |
| 12 | PeriodSetName | PERIOD_SET_NAME | — | ✅ |
| 13 | PeriodType | PERIOD_TYPE | — | ✅ |
| 14 | PeriodYear | PERIOD_YEAR | — | ✅ |
| 15 | StartDate | START_DATE | — | ✅ |
| 16 | StatusCode | STATUS_CODE | — | ✅ |

### [[gl_periods|GL_PERIODS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlPeriodsAdjustmentPeriodFlag | ADJUSTMENT_PERIOD_FLAG | — | — |
| 2 | GlPeriodsAttribute1 | ATTRIBUTE1 | — | — |
| 3 | GlPeriodsAttribute2 | ATTRIBUTE2 | — | — |
| 4 | GlPeriodsAttribute3 | ATTRIBUTE3 | — | — |
| 5 | GlPeriodsAttribute4 | ATTRIBUTE4 | — | — |
| 6 | GlPeriodsAttribute5 | ATTRIBUTE5 | — | — |
| 7 | GlPeriodsAttribute6 | ATTRIBUTE6 | — | — |
| 8 | GlPeriodsAttribute7 | ATTRIBUTE7 | — | — |
| 9 | GlPeriodsAttribute8 | ATTRIBUTE8 | — | — |
| 10 | GlPeriodsAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 11 | GlPeriodsConfirmationStatus | CONFIRMATION_STATUS | — | — |
| 12 | GlPeriodsCreatedBy1 | CREATED_BY | — | — |
| 13 | GlPeriodsCreationDate1 | CREATION_DATE | — | — |
| 14 | GlPeriodsDescription | DESCRIPTION | — | — |
| 15 | GlPeriodsEndDate1 | END_DATE | — | — |
| 16 | GlPeriodsEnteredPeriodName | ENTERED_PERIOD_NAME | — | — |
| 17 | GlPeriodsGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 18 | GlPeriodsGlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | — |
| 19 | GlPeriodsGlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | — |
| 20 | GlPeriodsGlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | — |
| 21 | GlPeriodsGlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | — |
| 22 | GlPeriodsGlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | — |
| 23 | GlPeriodsGlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | — |
| 24 | GlPeriodsGlobalAttribute16 | GLOBAL_ATTRIBUTE16 | — | — |
| 25 | GlPeriodsGlobalAttribute17 | GLOBAL_ATTRIBUTE17 | — | — |
| 26 | GlPeriodsGlobalAttribute18 | GLOBAL_ATTRIBUTE18 | — | — |
| 27 | GlPeriodsGlobalAttribute19 | GLOBAL_ATTRIBUTE19 | — | — |
| 28 | GlPeriodsGlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | — |
| 29 | GlPeriodsGlobalAttribute20 | GLOBAL_ATTRIBUTE20 | — | — |
| 30 | GlPeriodsGlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | — |
| 31 | GlPeriodsGlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | — |
| 32 | GlPeriodsGlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | — |
| 33 | GlPeriodsGlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | — |
| 34 | GlPeriodsGlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | — |
| 35 | GlPeriodsGlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | — |
| 36 | GlPeriodsGlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | — |
| 37 | GlPeriodsGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 38 | GlPeriodsGlobalAttributeDate1 | GLOBAL_ATTRIBUTE_DATE1 | — | — |
| 39 | GlPeriodsGlobalAttributeDate2 | GLOBAL_ATTRIBUTE_DATE2 | — | — |
| 40 | GlPeriodsGlobalAttributeDate3 | GLOBAL_ATTRIBUTE_DATE3 | — | — |
| 41 | GlPeriodsGlobalAttributeDate4 | GLOBAL_ATTRIBUTE_DATE4 | — | — |
| 42 | GlPeriodsGlobalAttributeDate5 | GLOBAL_ATTRIBUTE_DATE5 | — | — |
| 43 | GlPeriodsGlobalAttributeNumber1 | GLOBAL_ATTRIBUTE_NUMBER1 | — | — |
| 44 | GlPeriodsGlobalAttributeNumber2 | GLOBAL_ATTRIBUTE_NUMBER2 | — | — |
| 45 | GlPeriodsGlobalAttributeNumber3 | GLOBAL_ATTRIBUTE_NUMBER3 | — | — |
| 46 | GlPeriodsGlobalAttributeNumber4 | GLOBAL_ATTRIBUTE_NUMBER4 | — | — |
| 47 | GlPeriodsGlobalAttributeNumber5 | GLOBAL_ATTRIBUTE_NUMBER5 | — | — |
| 48 | GlPeriodsLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 49 | GlPeriodsLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 50 | GlPeriodsLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 51 | GlPeriodsObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 52 | GlPeriodsPeriodName1 | PERIOD_NAME | — | — |
| 53 | GlPeriodsPeriodNum1 | PERIOD_NUM | — | — |
| 54 | GlPeriodsPeriodSetName1 | PERIOD_SET_NAME | — | — |
| 55 | GlPeriodsPeriodType1 | PERIOD_TYPE | — | — |
| 56 | GlPeriodsPeriodYear1 | PERIOD_YEAR | — | — |
| 57 | GlPeriodsQuarterNum | QUARTER_NUM | — | — |
| 58 | GlPeriodsQuarterStartDate | QUARTER_START_DATE | — | — |
| 59 | GlPeriodsStartDate1 | START_DATE | — | — |
| 60 | GlPeriodsYearStartDate | YEAR_START_DATE | — | — |

### [[gl_period_sets|GL_PERIOD_SETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlPeriodSetsAttribute1 | ATTRIBUTE1 | — | — |
| 2 | GlPeriodSetsAttribute2 | ATTRIBUTE2 | — | — |
| 3 | GlPeriodSetsAttribute3 | ATTRIBUTE3 | — | — |
| 4 | GlPeriodSetsAttribute4 | ATTRIBUTE4 | — | — |
| 5 | GlPeriodSetsAttribute5 | ATTRIBUTE5 | — | — |
| 6 | GlPeriodSetsAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 7 | GlPeriodSetsCreatedBy1 | CREATED_BY | — | — |
| 8 | GlPeriodSetsCreationDate1 | CREATION_DATE | — | — |
| 9 | GlPeriodSetsDescription | DESCRIPTION | — | — |
| 10 | GlPeriodSetsLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 11 | GlPeriodSetsLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 12 | GlPeriodSetsLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 13 | GlPeriodSetsObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 14 | GlPeriodSetsPeriodSetId | PERIOD_SET_ID | — | — |
| 15 | GlPeriodSetsPeriodSetName1 | PERIOD_SET_NAME | — | — |
| 16 | GlPeriodSetsSecurityFlag | SECURITY_FLAG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
