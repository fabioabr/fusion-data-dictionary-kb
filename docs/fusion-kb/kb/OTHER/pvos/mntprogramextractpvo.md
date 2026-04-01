---
id: DOC-OTHER-PVO-MntProgramExtractPVO
doc_type: system-doc
title: "MntProgramExtractPVO — PVO Cross-Module"
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
  - MntProgramExtractPVO
  - mntprogramextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MntProgramExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Mnt Program Extract. Acessa as tabelas: MNT_PROGRAMS_B, MNT_PROGRAMS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.MntBiccExtractAM.MntProgramExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 73 | 2 | 3 | 73 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[mnt_programs_b|MNT_PROGRAMS_B]] — 62 atributos (1 PKs, 62 BICC)
- [[mnt_programs_tl|MNT_PROGRAMS_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[mnt_programs_b|MNT_PROGRAMS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActiveEndDate | ACTIVE_END_DATE | — | ✅ |
| 2 | ActiveStartDate | ACTIVE_START_DATE | — | ✅ |
| 3 | AttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 4 | AttributeChar1 | ATTRIBUTE_CHAR1 | — | ✅ |
| 5 | AttributeChar10 | ATTRIBUTE_CHAR10 | — | ✅ |
| 6 | AttributeChar11 | ATTRIBUTE_CHAR11 | — | ✅ |
| 7 | AttributeChar12 | ATTRIBUTE_CHAR12 | — | ✅ |
| 8 | AttributeChar13 | ATTRIBUTE_CHAR13 | — | ✅ |
| 9 | AttributeChar14 | ATTRIBUTE_CHAR14 | — | ✅ |
| 10 | AttributeChar15 | ATTRIBUTE_CHAR15 | — | ✅ |
| 11 | AttributeChar16 | ATTRIBUTE_CHAR16 | — | ✅ |
| 12 | AttributeChar17 | ATTRIBUTE_CHAR17 | — | ✅ |
| 13 | AttributeChar18 | ATTRIBUTE_CHAR18 | — | ✅ |
| 14 | AttributeChar19 | ATTRIBUTE_CHAR19 | — | ✅ |
| 15 | AttributeChar2 | ATTRIBUTE_CHAR2 | — | ✅ |
| 16 | AttributeChar20 | ATTRIBUTE_CHAR20 | — | ✅ |
| 17 | AttributeChar3 | ATTRIBUTE_CHAR3 | — | ✅ |
| 18 | AttributeChar4 | ATTRIBUTE_CHAR4 | — | ✅ |
| 19 | AttributeChar5 | ATTRIBUTE_CHAR5 | — | ✅ |
| 20 | AttributeChar6 | ATTRIBUTE_CHAR6 | — | ✅ |
| 21 | AttributeChar7 | ATTRIBUTE_CHAR7 | — | ✅ |
| 22 | AttributeChar8 | ATTRIBUTE_CHAR8 | — | ✅ |
| 23 | AttributeChar9 | ATTRIBUTE_CHAR9 | — | ✅ |
| 24 | AttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 25 | AttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 26 | AttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 27 | AttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 28 | AttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 29 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 30 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 31 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 32 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 33 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 34 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 35 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 36 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 37 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 38 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 39 | AttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 40 | AttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 41 | AttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 42 | AttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 43 | AttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 44 | CreatedBy | CREATED_BY | — | ✅ |
| 45 | CreationDate | CREATION_DATE | — | ✅ |
| 46 | InProcessFlag | IN_PROCESS_FLAG | — | ✅ |
| 47 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 48 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 49 | LastForecastDate | LAST_FORECAST_DATE | — | ✅ |
| 50 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 51 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 52 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 53 | ModifiedFlag | MODIFIED_FLAG | — | ✅ |
| 54 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 55 | OrganizationId | ORGANIZATION_ID | — | ✅ |
| 56 | ProgramCode | PROGRAM_CODE | — | ✅ |
| 57 | ProgramId | PROGRAM_ID | 🔑 | ✅ |
| 58 | RequestId | REQUEST_ID | — | ✅ |
| 59 | ReviewComments | REVIEW_COMMENTS | — | ✅ |
| 60 | ReviewDate | REVIEW_DATE | — | ✅ |
| 61 | ReviewedBy | REVIEWED_BY | — | ✅ |
| 62 | SuppressMergeCode | SUPPRESS_MERGE_CODE | — | ✅ |

### [[mnt_programs_tl|MNT_PROGRAMS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MaintenanceProgramTranslatio1CreatedBy | CREATED_BY | — | ✅ |
| 2 | MaintenanceProgramTranslatio1CreationDate | CREATION_DATE | — | ✅ |
| 3 | MaintenanceProgramTranslatio1Language | LANGUAGE | 🔑 | ✅ |
| 4 | MaintenanceProgramTranslatio1LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | MaintenanceProgramTranslatio1LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | MaintenanceProgramTranslatio1LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | MaintenanceProgramTranslatio1ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | MaintenanceProgramTranslatio1ProgramDescription | PROGRAM_DESCRIPTION | — | ✅ |
| 9 | MaintenanceProgramTranslatio1ProgramId | PROGRAM_ID | 🔑 | ✅ |
| 10 | MaintenanceProgramTranslatio1ProgramName | PROGRAM_NAME | — | ✅ |
| 11 | MaintenanceProgramTranslatio1SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
