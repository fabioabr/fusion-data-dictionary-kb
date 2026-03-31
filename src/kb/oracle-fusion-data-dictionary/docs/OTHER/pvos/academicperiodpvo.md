---
id: DOC-OTHER-PVO-AcademicPeriodPVO
doc_type: system-doc
title: "AcademicPeriodPVO — PVO Cross-Module"
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
  - AcademicPeriodPVO
  - academicperiodpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AcademicPeriodPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Academic Period. Acessa as tabelas: HER_ACADEMIC_PERIOD_VL, HER_ACAD_PRD_TP_VL, HEY_CALENDAR_ITEM_VL.

**Caminho:** `FscmTopModelAM.StudentEnrollmentAM.AcademicPeriodPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 132 | 3 | 1 | 11 | 8% |

---

## 🔗 Tabelas Relacionadas

- [[her_academic_period_vl|HER_ACADEMIC_PERIOD_VL]] — 67 atributos (1 PKs, 8 BICC)
- [[her_acad_prd_tp_vl|HER_ACAD_PRD_TP_VL]] — 61 atributos (3 BICC)
- [[hey_calendar_item_vl|HEY_CALENDAR_ITEM_VL]] — 4 atributos

---

## ⚙️ Atributos

### [[her_academic_period_vl|HER_ACADEMIC_PERIOD_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AcademicPeriodPEOAcademicPeriodEndDt | ACADEMIC_PERIOD_END_DT | — | ✅ |
| 2 | AcademicPeriodPEOAcademicPeriodId | ACADEMIC_PERIOD_ID | 🔑 | ✅ |
| 3 | AcademicPeriodPEOAcademicPeriodStartDt | ACADEMIC_PERIOD_START_DT | — | ✅ |
| 4 | AcademicPeriodPEOAcademicPeriodTypeId | ACADEMIC_PERIOD_TYPE_ID | — | ✅ |
| 5 | AcademicPeriodPEOAttribute1 | ATTRIBUTE1 | — | — |
| 6 | AcademicPeriodPEOAttribute10 | ATTRIBUTE10 | — | — |
| 7 | AcademicPeriodPEOAttribute11 | ATTRIBUTE11 | — | — |
| 8 | AcademicPeriodPEOAttribute12 | ATTRIBUTE12 | — | — |
| 9 | AcademicPeriodPEOAttribute13 | ATTRIBUTE13 | — | — |
| 10 | AcademicPeriodPEOAttribute14 | ATTRIBUTE14 | — | — |
| 11 | AcademicPeriodPEOAttribute15 | ATTRIBUTE15 | — | — |
| 12 | AcademicPeriodPEOAttribute16 | ATTRIBUTE16 | — | — |
| 13 | AcademicPeriodPEOAttribute17 | ATTRIBUTE17 | — | — |
| 14 | AcademicPeriodPEOAttribute18 | ATTRIBUTE18 | — | — |
| 15 | AcademicPeriodPEOAttribute19 | ATTRIBUTE19 | — | — |
| 16 | AcademicPeriodPEOAttribute2 | ATTRIBUTE2 | — | — |
| 17 | AcademicPeriodPEOAttribute20 | ATTRIBUTE20 | — | — |
| 18 | AcademicPeriodPEOAttribute3 | ATTRIBUTE3 | — | — |
| 19 | AcademicPeriodPEOAttribute4 | ATTRIBUTE4 | — | — |
| 20 | AcademicPeriodPEOAttribute5 | ATTRIBUTE5 | — | — |
| 21 | AcademicPeriodPEOAttribute6 | ATTRIBUTE6 | — | — |
| 22 | AcademicPeriodPEOAttribute7 | ATTRIBUTE7 | — | — |
| 23 | AcademicPeriodPEOAttribute8 | ATTRIBUTE8 | — | — |
| 24 | AcademicPeriodPEOAttribute9 | ATTRIBUTE9 | — | — |
| 25 | AcademicPeriodPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 26 | AcademicPeriodPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 27 | AcademicPeriodPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 28 | AcademicPeriodPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 29 | AcademicPeriodPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 30 | AcademicPeriodPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 31 | AcademicPeriodPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 32 | AcademicPeriodPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 33 | AcademicPeriodPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 34 | AcademicPeriodPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 35 | AcademicPeriodPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 36 | AcademicPeriodPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 37 | AcademicPeriodPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 38 | AcademicPeriodPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 39 | AcademicPeriodPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 40 | AcademicPeriodPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 41 | AcademicPeriodPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 42 | AcademicPeriodPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 43 | AcademicPeriodPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 44 | AcademicPeriodPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 45 | AcademicPeriodPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 46 | AcademicPeriodPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 47 | AcademicPeriodPEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 48 | AcademicPeriodPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 49 | AcademicPeriodPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 50 | AcademicPeriodPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 51 | AcademicPeriodPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 52 | AcademicPeriodPEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 53 | AcademicPeriodPEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 54 | AcademicPeriodPEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 55 | AcademicPeriodPEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 56 | AcademicPeriodPEOCalId | CAL_ID | — | — |
| 57 | AcademicPeriodPEOCalendarDateFlag | CALENDAR_DATE_FLAG | — | — |
| 58 | AcademicPeriodPEOCreatedBy | CREATED_BY | — | — |
| 59 | AcademicPeriodPEOCreationDate | CREATION_DATE | — | — |
| 60 | AcademicPeriodPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 61 | AcademicPeriodPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 62 | AcademicPeriodPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 63 | AcademicPeriodPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 64 | AcademicPeriodPEOPeriodCategoryCode | PERIOD_CATEGORY_CODE | — | — |
| 65 | AcademicPeriodPEOPeriodName | PERIOD_NAME | — | ✅ |
| 66 | AcademicPeriodPEOSetId | SET_ID | — | ✅ |
| 67 | AcademicPeriodPEOSystemGeneratedFlag | SYSTEM_GENERATED_FLAG | — | ✅ |

### [[her_acad_prd_tp_vl|HER_ACAD_PRD_TP_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AcademicPeriodTypePEOAcademicPeriodTypeId1 | ACADEMIC_PERIOD_TYPE_ID | — | — |
| 2 | AcademicPeriodTypePEOAttribute101 | ATTRIBUTE10 | — | — |
| 3 | AcademicPeriodTypePEOAttribute110 | ATTRIBUTE1 | — | — |
| 4 | AcademicPeriodTypePEOAttribute111 | ATTRIBUTE11 | — | — |
| 5 | AcademicPeriodTypePEOAttribute121 | ATTRIBUTE12 | — | — |
| 6 | AcademicPeriodTypePEOAttribute131 | ATTRIBUTE13 | — | — |
| 7 | AcademicPeriodTypePEOAttribute141 | ATTRIBUTE14 | — | — |
| 8 | AcademicPeriodTypePEOAttribute151 | ATTRIBUTE15 | — | — |
| 9 | AcademicPeriodTypePEOAttribute161 | ATTRIBUTE16 | — | — |
| 10 | AcademicPeriodTypePEOAttribute171 | ATTRIBUTE17 | — | — |
| 11 | AcademicPeriodTypePEOAttribute181 | ATTRIBUTE18 | — | — |
| 12 | AcademicPeriodTypePEOAttribute191 | ATTRIBUTE19 | — | — |
| 13 | AcademicPeriodTypePEOAttribute201 | ATTRIBUTE20 | — | — |
| 14 | AcademicPeriodTypePEOAttribute21 | ATTRIBUTE2 | — | — |
| 15 | AcademicPeriodTypePEOAttribute31 | ATTRIBUTE3 | — | — |
| 16 | AcademicPeriodTypePEOAttribute41 | ATTRIBUTE4 | — | — |
| 17 | AcademicPeriodTypePEOAttribute51 | ATTRIBUTE5 | — | — |
| 18 | AcademicPeriodTypePEOAttribute61 | ATTRIBUTE6 | — | — |
| 19 | AcademicPeriodTypePEOAttribute71 | ATTRIBUTE7 | — | — |
| 20 | AcademicPeriodTypePEOAttribute81 | ATTRIBUTE8 | — | — |
| 21 | AcademicPeriodTypePEOAttribute91 | ATTRIBUTE9 | — | — |
| 22 | AcademicPeriodTypePEOAttributeCategory1 | ATTRIBUTE_CATEGORY | — | — |
| 23 | AcademicPeriodTypePEOAttributeDate101 | ATTRIBUTE_DATE10 | — | — |
| 24 | AcademicPeriodTypePEOAttributeDate11 | ATTRIBUTE_DATE1 | — | — |
| 25 | AcademicPeriodTypePEOAttributeDate21 | ATTRIBUTE_DATE2 | — | — |
| 26 | AcademicPeriodTypePEOAttributeDate31 | ATTRIBUTE_DATE3 | — | — |
| 27 | AcademicPeriodTypePEOAttributeDate41 | ATTRIBUTE_DATE4 | — | — |
| 28 | AcademicPeriodTypePEOAttributeDate51 | ATTRIBUTE_DATE5 | — | — |
| 29 | AcademicPeriodTypePEOAttributeDate61 | ATTRIBUTE_DATE6 | — | — |
| 30 | AcademicPeriodTypePEOAttributeDate71 | ATTRIBUTE_DATE7 | — | — |
| 31 | AcademicPeriodTypePEOAttributeDate81 | ATTRIBUTE_DATE8 | — | — |
| 32 | AcademicPeriodTypePEOAttributeDate91 | ATTRIBUTE_DATE9 | — | — |
| 33 | AcademicPeriodTypePEOAttributeNumber101 | ATTRIBUTE_NUMBER10 | — | — |
| 34 | AcademicPeriodTypePEOAttributeNumber11 | ATTRIBUTE_NUMBER1 | — | — |
| 35 | AcademicPeriodTypePEOAttributeNumber21 | ATTRIBUTE_NUMBER2 | — | — |
| 36 | AcademicPeriodTypePEOAttributeNumber31 | ATTRIBUTE_NUMBER3 | — | — |
| 37 | AcademicPeriodTypePEOAttributeNumber41 | ATTRIBUTE_NUMBER4 | — | — |
| 38 | AcademicPeriodTypePEOAttributeNumber51 | ATTRIBUTE_NUMBER5 | — | — |
| 39 | AcademicPeriodTypePEOAttributeNumber61 | ATTRIBUTE_NUMBER6 | — | — |
| 40 | AcademicPeriodTypePEOAttributeNumber71 | ATTRIBUTE_NUMBER7 | — | — |
| 41 | AcademicPeriodTypePEOAttributeNumber81 | ATTRIBUTE_NUMBER8 | — | — |
| 42 | AcademicPeriodTypePEOAttributeNumber91 | ATTRIBUTE_NUMBER9 | — | — |
| 43 | AcademicPeriodTypePEOAttributeTimestamp101 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 44 | AcademicPeriodTypePEOAttributeTimestamp11 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 45 | AcademicPeriodTypePEOAttributeTimestamp21 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 46 | AcademicPeriodTypePEOAttributeTimestamp31 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 47 | AcademicPeriodTypePEOAttributeTimestamp41 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 48 | AcademicPeriodTypePEOAttributeTimestamp51 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 49 | AcademicPeriodTypePEOAttributeTimestamp61 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 50 | AcademicPeriodTypePEOAttributeTimestamp71 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 51 | AcademicPeriodTypePEOAttributeTimestamp81 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 52 | AcademicPeriodTypePEOAttributeTimestamp91 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 53 | AcademicPeriodTypePEOCreatedBy1 | CREATED_BY | — | — |
| 54 | AcademicPeriodTypePEOCreationDate1 | CREATION_DATE | — | — |
| 55 | AcademicPeriodTypePEOLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 56 | AcademicPeriodTypePEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 57 | AcademicPeriodTypePEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 58 | AcademicPeriodTypePEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 59 | AcademicPeriodTypePEOPeriodCategoryCode | PERIOD_CATEGORY_CODE | — | ✅ |
| 60 | AcademicPeriodTypePEOSetId1 | SET_ID | — | — |
| 61 | AcademicPeriodTypePEOTypeName | TYPE_NAME | — | ✅ |

### [[hey_calendar_item_vl|HEY_CALENDAR_ITEM_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CalendarItemPEOCalendarItemId | CALENDAR_ITEM_ID | — | — |
| 2 | CalendarItemPEOEndDate | END_DATE | — | — |
| 3 | CalendarItemPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 4 | CalendarItemPEOStartDate | START_DATE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
