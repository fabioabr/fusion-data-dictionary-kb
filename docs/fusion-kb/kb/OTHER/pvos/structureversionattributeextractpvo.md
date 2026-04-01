---
id: DOC-OTHER-PVO-StructureVersionAttributeExtractPVO
doc_type: system-doc
title: "StructureVersionAttributeExtractPVO — PVO Cross-Module"
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
  - StructureVersionAttributeExtractPVO
  - structureversionattributeextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# StructureVersionAttributeExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Structure Version Attribute Extract. Acessa as tabelas: PJF_PROJ_ELEM_VER_STRUCT.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.StructureVersionAttributeExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 30 | 1 | 1 | 30 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_proj_elem_ver_struct|PJF_PROJ_ELEM_VER_STRUCT]] — 30 atributos (1 PKs, 30 BICC)

---

## ⚙️ Atributos

### [[pjf_proj_elem_ver_struct|PJF_PROJ_ELEM_VER_STRUCT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | StructureVersionConcRequestId | CONC_REQUEST_ID | — | ✅ |
| 2 | StructureVersionCreatedBy | CREATED_BY | — | ✅ |
| 3 | StructureVersionCreationDate | CREATION_DATE | — | ✅ |
| 4 | StructureVersionDescription | DESCRIPTION | — | ✅ |
| 5 | StructureVersionElementVersionId | ELEMENT_VERSION_ID | — | ✅ |
| 6 | StructureVersionJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 7 | StructureVersionJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 8 | StructureVersionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | StructureVersionLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | StructureVersionLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | StructureVersionLockStatusCode | LOCK_STATUS_CODE | — | ✅ |
| 12 | StructureVersionLockedByPersonId | LOCKED_BY_PERSON_ID | — | ✅ |
| 13 | StructureVersionLockedDate | LOCKED_DATE | — | ✅ |
| 14 | StructureVersionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 15 | StructureVersionPevStructureId | PEV_STRUCTURE_ID | 🔑 | ✅ |
| 16 | StructureVersionPmSourceCode | PM_SOURCE_CODE | — | ✅ |
| 17 | StructureVersionPmSourceReference | PM_SOURCE_REFERENCE | — | ✅ |
| 18 | StructureVersionPrbsChangeFlag | PRBS_CHANGE_FLAG | — | ✅ |
| 19 | StructureVersionProcessCode | PROCESS_CODE | — | ✅ |
| 20 | StructureVersionProcessUpdateWbsFlag | PROCESS_UPDATE_WBS_FLAG | — | ✅ |
| 21 | StructureVersionProgramAppName | PROGRAM_APP_NAME | — | ✅ |
| 22 | StructureVersionProgramName | PROGRAM_NAME | — | ✅ |
| 23 | StructureVersionProjElementId | PROJ_ELEMENT_ID | — | ✅ |
| 24 | StructureVersionProjPlanUpdatedFlag | PROJ_PLAN_UPDATED_FLAG | — | ✅ |
| 25 | StructureVersionProjectId | PROJECT_ID | — | ✅ |
| 26 | StructureVersionRequestId | REQUEST_ID | — | ✅ |
| 27 | StructureVersionStatusCode | STATUS_CODE | — | ✅ |
| 28 | StructureVersionTreeFlatteningFlag | TREE_FLATTENING_FLAG | — | ✅ |
| 29 | StructureVersionVersionName | VERSION_NAME | — | ✅ |
| 30 | StructureVersionVersionNumber | VERSION_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
