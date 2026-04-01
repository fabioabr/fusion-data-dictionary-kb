---
id: DOC-OTHER-PVO-EgoChangeTypesPVO
doc_type: system-doc
title: "EgoChangeTypesPVO — PVO Cross-Module"
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
  - EgoChangeTypesPVO
  - egochangetypespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EgoChangeTypesPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Ego Change Types. Acessa as tabelas: EGO_CHANGE_TYPES_B, EGO_CHANGE_TYPES_TL.

**Caminho:** `FscmTopModelAM.ChangeTypesAM.EgoChangeTypesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 50 | 2 | 2 | 15 | 30% |

---

## 🔗 Tabelas Relacionadas

- [[ego_change_types_b|EGO_CHANGE_TYPES_B]] — 27 atributos (1 PKs, 7 BICC)
- [[ego_change_types_tl|EGO_CHANGE_TYPES_TL]] — 23 atributos (1 PKs, 8 BICC)

---

## ⚙️ Atributos

### [[ego_change_types_b|EGO_CHANGE_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChangeTypeId | CHANGE_TYPE_ID | 🔑 | ✅ |
| 2 | EgoChangeTypesBasePEOApplicationId | APPLICATION_ID | — | — |
| 3 | EgoChangeTypesBasePEOAutoNumberingMethod | AUTO_NUMBERING_METHOD | — | — |
| 4 | EgoChangeTypesBasePEOBaseChangeMgmtTypeCode | BASE_CHANGE_MGMT_TYPE_CODE | — | ✅ |
| 5 | EgoChangeTypesBasePEOChangeMgmtTypeCode | CHANGE_MGMT_TYPE_CODE | — | — |
| 6 | EgoChangeTypesBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 7 | EgoChangeTypesBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | EgoChangeTypesBasePEODefaultAssigneeFromRoleId | DEFAULT_ASSIGNEE_FROM_ROLE_ID | — | — |
| 9 | EgoChangeTypesBasePEODefaultAssigneeId | DEFAULT_ASSIGNEE_ID | — | — |
| 10 | EgoChangeTypesBasePEODefaultAssigneeType | DEFAULT_ASSIGNEE_TYPE | — | — |
| 11 | EgoChangeTypesBasePEODisableDate | DISABLE_DATE | — | — |
| 12 | EgoChangeTypesBasePEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 13 | EgoChangeTypesBasePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 14 | EgoChangeTypesBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | EgoChangeTypesBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | EgoChangeTypesBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 17 | EgoChangeTypesBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | EgoChangeTypesBasePEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 19 | EgoChangeTypesBasePEOProgramName | PROGRAM_NAME | — | — |
| 20 | EgoChangeTypesBasePEORequestId | REQUEST_ID | — | — |
| 21 | EgoChangeTypesBasePEOSeededFlag | SEEDED_FLAG | — | — |
| 22 | EgoChangeTypesBasePEOStartDate | START_DATE | — | — |
| 23 | EgoChangeTypesBasePEOSubjectInternalName | SUBJECT_INTERNAL_NAME | — | — |
| 24 | EgoChangeTypesBasePEOTypeClassification | TYPE_CLASSIFICATION | — | — |
| 25 | EgoChangeTypesBasePEOTypeInternalName | TYPE_INTERNAL_NAME | — | — |
| 26 | EgoChangeTypesBasePEOXmlDataSourceCode | XML_DATA_SOURCE_CODE | — | — |
| 27 | EgoChangeTypesTransPEOCopiedFrom | COPIED_FROM | — | ✅ |

### [[ego_change_types_tl|EGO_CHANGE_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EgoChangeTypesTLPEOChangeTypeId | CHANGE_TYPE_ID | — | — |
| 2 | EgoChangeTypesTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | EgoChangeTypesTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | EgoChangeTypesTLPEODescription | DESCRIPTION | — | ✅ |
| 5 | EgoChangeTypesTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | EgoChangeTypesTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | EgoChangeTypesTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | EgoChangeTypesTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | EgoChangeTypesTLPEOSourceLang | SOURCE_LANG | — | ✅ |
| 10 | EgoChangeTypesTLPEOTabText | TAB_TEXT | — | — |
| 11 | EgoChangeTypesTLPEOTypeName | TYPE_NAME | — | ✅ |
| 12 | EgoChangeTypesTransPEOChangeTypeId | CHANGE_TYPE_ID | — | — |
| 13 | EgoChangeTypesTransPEOCreatedBy | CREATED_BY | — | — |
| 14 | EgoChangeTypesTransPEOCreationDate | CREATION_DATE | — | — |
| 15 | EgoChangeTypesTransPEODescription | DESCRIPTION | — | — |
| 16 | EgoChangeTypesTransPEOLanguage | LANGUAGE | — | — |
| 17 | EgoChangeTypesTransPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 18 | EgoChangeTypesTransPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 19 | EgoChangeTypesTransPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 20 | EgoChangeTypesTransPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 21 | EgoChangeTypesTransPEOSourceLang | SOURCE_LANG | — | — |
| 22 | EgoChangeTypesTransPEOTabText | TAB_TEXT | — | — |
| 23 | EgoChangeTypesTransPEOTypeName | TYPE_NAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
