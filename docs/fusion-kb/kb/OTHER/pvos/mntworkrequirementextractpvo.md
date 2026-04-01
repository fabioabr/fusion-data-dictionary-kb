---
id: DOC-OTHER-PVO-MntWorkRequirementExtractPVO
doc_type: system-doc
title: "MntWorkRequirementExtractPVO — PVO Cross-Module"
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
  - MntWorkRequirementExtractPVO
  - mntworkrequirementextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MntWorkRequirementExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Mnt Work Requirement Extract. Acessa as tabelas: MNT_WORK_REQUIREMENTS_B, MNT_WORK_REQUIREMENTS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.MntBiccExtractAM.MntWorkRequirementExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 39 | 2 | 3 | 39 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[mnt_work_requirements_b|MNT_WORK_REQUIREMENTS_B]] — 29 atributos (1 PKs, 29 BICC)
- [[mnt_work_requirements_tl|MNT_WORK_REQUIREMENTS_TL]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[mnt_work_requirements_b|MNT_WORK_REQUIREMENTS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActiveEndDate | ACTIVE_END_DATE | — | ✅ |
| 2 | ActiveStartDate | ACTIVE_START_DATE | — | ✅ |
| 3 | AssetId | ASSET_ID | — | ✅ |
| 4 | CalendarBasedFlag | CALENDAR_BASED_FLAG | — | ✅ |
| 5 | ConditionBasedFlag | CONDITION_BASED_FLAG | — | ✅ |
| 6 | CreatedBy | CREATED_BY | — | ✅ |
| 7 | CreationDate | CREATION_DATE | — | ✅ |
| 8 | ForecastUsingCycleFlag | FORECAST_USING_CYCLE_FLAG | — | ✅ |
| 9 | IntervalsInTheCycle | INTERVALS_IN_THE_CYCLE | — | ✅ |
| 10 | ItemId | ITEM_ID | — | ✅ |
| 11 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 12 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 13 | LastForecastDate | LAST_FORECAST_DATE | — | ✅ |
| 14 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 16 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 17 | MeterBasedFlag | METER_BASED_FLAG | — | ✅ |
| 18 | ModifiedFlag | MODIFIED_FLAG | — | ✅ |
| 19 | NextWorkOrderOnlyFlag | NEXT_WORK_ORDER_ONLY_FLAG | — | ✅ |
| 20 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 21 | OrganizationId | ORGANIZATION_ID | — | ✅ |
| 22 | ProgramId | PROGRAM_ID | — | ✅ |
| 23 | RequestId | REQUEST_ID | — | ✅ |
| 24 | RequirementId | REQUIREMENT_ID | 🔑 | ✅ |
| 25 | RequirementTypeCode | REQUIREMENT_TYPE_CODE | — | ✅ |
| 26 | SchedulePatternId | SCHEDULE_PATTERN_ID | — | ✅ |
| 27 | StatusCode | STATUS_CODE | — | ✅ |
| 28 | SuppressMergeCode | SUPPRESS_MERGE_CODE | — | ✅ |
| 29 | SuppressMergeOverrideFlag | SUPPRESS_MERGE_OVERRIDE_FLAG | — | ✅ |

### [[mnt_work_requirements_tl|MNT_WORK_REQUIREMENTS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MntWorkRequirementTranslatio1CreatedBy | CREATED_BY | — | ✅ |
| 2 | MntWorkRequirementTranslatio1CreationDate | CREATION_DATE | — | ✅ |
| 3 | MntWorkRequirementTranslatio1Language | LANGUAGE | 🔑 | ✅ |
| 4 | MntWorkRequirementTranslatio1LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | MntWorkRequirementTranslatio1LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | MntWorkRequirementTranslatio1LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | MntWorkRequirementTranslatio1ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | MntWorkRequirementTranslatio1RequirementId | REQUIREMENT_ID | 🔑 | ✅ |
| 9 | MntWorkRequirementTranslatio1RequirementName | REQUIREMENT_NAME | — | ✅ |
| 10 | MntWorkRequirementTranslatio1SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
