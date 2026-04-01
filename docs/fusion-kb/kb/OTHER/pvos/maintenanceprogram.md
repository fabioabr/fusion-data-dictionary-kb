---
id: DOC-OTHER-PVO-MaintenanceProgram
doc_type: system-doc
title: "MaintenanceProgram — PVO Cross-Module"
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
  - MaintenanceProgram
  - maintenanceprogram
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MaintenanceProgram

## 📌 Visão Geral

View Object para extração BICC de dados de Maintenance Program. Acessa as tabelas: MNT_PROGRAMS_B, MNT_PROGRAMS_TL.

**Caminho:** `FscmTopModelAM.MaintProgramAM.MaintenanceProgram`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 77 | 2 | 1 | 15 | 19% |

---

## 🔗 Tabelas Relacionadas

- [[mnt_programs_b|MNT_PROGRAMS_B]] — 72 atributos (1 PKs, 12 BICC)
- [[mnt_programs_tl|MNT_PROGRAMS_TL]] — 5 atributos (3 BICC)

---

## ⚙️ Atributos

### [[mnt_programs_b|MNT_PROGRAMS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MaintenanceProgramBasePEOActiveEndDate | ACTIVE_END_DATE | — | ✅ |
| 2 | MaintenanceProgramBasePEOActiveStartDate | ACTIVE_START_DATE | — | ✅ |
| 3 | MaintenanceProgramBasePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 4 | MaintenanceProgramBasePEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 5 | MaintenanceProgramBasePEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 6 | MaintenanceProgramBasePEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 7 | MaintenanceProgramBasePEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 8 | MaintenanceProgramBasePEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 9 | MaintenanceProgramBasePEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 10 | MaintenanceProgramBasePEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 11 | MaintenanceProgramBasePEOAttributeChar16 | ATTRIBUTE_CHAR16 | — | — |
| 12 | MaintenanceProgramBasePEOAttributeChar17 | ATTRIBUTE_CHAR17 | — | — |
| 13 | MaintenanceProgramBasePEOAttributeChar18 | ATTRIBUTE_CHAR18 | — | — |
| 14 | MaintenanceProgramBasePEOAttributeChar19 | ATTRIBUTE_CHAR19 | — | — |
| 15 | MaintenanceProgramBasePEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 16 | MaintenanceProgramBasePEOAttributeChar20 | ATTRIBUTE_CHAR20 | — | — |
| 17 | MaintenanceProgramBasePEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 18 | MaintenanceProgramBasePEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 19 | MaintenanceProgramBasePEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 20 | MaintenanceProgramBasePEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 21 | MaintenanceProgramBasePEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 22 | MaintenanceProgramBasePEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 23 | MaintenanceProgramBasePEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 24 | MaintenanceProgramBasePEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 25 | MaintenanceProgramBasePEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 26 | MaintenanceProgramBasePEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 27 | MaintenanceProgramBasePEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 28 | MaintenanceProgramBasePEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 29 | MaintenanceProgramBasePEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 30 | MaintenanceProgramBasePEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 31 | MaintenanceProgramBasePEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 32 | MaintenanceProgramBasePEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 33 | MaintenanceProgramBasePEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 34 | MaintenanceProgramBasePEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 35 | MaintenanceProgramBasePEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 36 | MaintenanceProgramBasePEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 37 | MaintenanceProgramBasePEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 38 | MaintenanceProgramBasePEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 39 | MaintenanceProgramBasePEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 40 | MaintenanceProgramBasePEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 41 | MaintenanceProgramBasePEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 42 | MaintenanceProgramBasePEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 43 | MaintenanceProgramBasePEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 44 | MaintenanceProgramBasePEOCreatedBy | CREATED_BY | — | — |
| 45 | MaintenanceProgramBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 46 | MaintenanceProgramBasePEOForecastWindowInDays | FORECAST_WINDOW_IN_DAYS | — | — |
| 47 | MaintenanceProgramBasePEOGlobalAssetsFlag | GLOBAL_ASSETS_FLAG | — | — |
| 48 | MaintenanceProgramBasePEOInProcessFlag | IN_PROCESS_FLAG | — | — |
| 49 | MaintenanceProgramBasePEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 50 | MaintenanceProgramBasePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 51 | MaintenanceProgramBasePEOLastForecastDate | LAST_FORECAST_DATE | — | ✅ |
| 52 | MaintenanceProgramBasePEOLastForecastGenRequestId | LAST_FORECAST_GEN_REQUEST_ID | — | — |
| 53 | MaintenanceProgramBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 54 | MaintenanceProgramBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 55 | MaintenanceProgramBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 56 | MaintenanceProgramBasePEOLastWoGenRequestId | LAST_WO_GEN_REQUEST_ID | — | — |
| 57 | MaintenanceProgramBasePEOModifiedFlag | MODIFIED_FLAG | — | ✅ |
| 58 | MaintenanceProgramBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 59 | MaintenanceProgramBasePEOOrganizationId | ORGANIZATION_ID | — | — |
| 60 | MaintenanceProgramBasePEOProgramCode | PROGRAM_CODE | — | ✅ |
| 61 | MaintenanceProgramBasePEOProgramId | PROGRAM_ID | 🔑 | ✅ |
| 62 | MaintenanceProgramBasePEOProgramReference | PROGRAM_REFERENCE | — | — |
| 63 | MaintenanceProgramBasePEOProgramSubTypeCode | PROGRAM_SUB_TYPE_CODE | — | — |
| 64 | MaintenanceProgramBasePEOProgramTypeCode | PROGRAM_TYPE_CODE | — | — |
| 65 | MaintenanceProgramBasePEORequestId | REQUEST_ID | — | — |
| 66 | MaintenanceProgramBasePEOReviewComments | REVIEW_COMMENTS | — | ✅ |
| 67 | MaintenanceProgramBasePEOReviewDate | REVIEW_DATE | — | ✅ |
| 68 | MaintenanceProgramBasePEOReviewedBy | REVIEWED_BY | — | ✅ |
| 69 | MaintenanceProgramBasePEOSuppressMergeCode | SUPPRESS_MERGE_CODE | — | ✅ |
| 70 | MaintenanceProgramBasePEOWorkOrderStartTime | WORK_ORDER_START_TIME | — | — |
| 71 | MaintenanceProgramBasePEOWorkOrderTimezoneCode | WORK_ORDER_TIMEZONE_CODE | — | — |
| 72 | MaintenanceProgramBasePEOWorkOrderWindowInDays | WORK_ORDER_WINDOW_IN_DAYS | — | — |

### [[mnt_programs_tl|MNT_PROGRAMS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MaintenanceProgramTLPEOLanguage | LANGUAGE | — | ✅ |
| 2 | MaintenanceProgramTLPEOProgramDescription | PROGRAM_DESCRIPTION | — | ✅ |
| 3 | MaintenanceProgramTLPEOProgramId | PROGRAM_ID | — | — |
| 4 | MaintenanceProgramTLPEOProgramName | PROGRAM_NAME | — | ✅ |
| 5 | MaintenanceProgramTLPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
