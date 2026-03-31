---
id: DOC-OTHER-PVO-ChangeTypesExtractPVO
doc_type: system-doc
title: "ChangeTypesExtractPVO — PVO Cross-Module"
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
  - ChangeTypesExtractPVO
  - changetypesextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ChangeTypesExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Change Types Extract. Acessa as tabelas: EGO_CHANGE_TYPES_B, EGO_CHANGE_TYPES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.EgoBiccExtractAM.ChangeTypesExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 30 | 2 | 1 | 26 | 87% |

---

## 🔗 Tabelas Relacionadas

- [[ego_change_types_b|EGO_CHANGE_TYPES_B]] — 26 atributos (1 PKs, 26 BICC)
- [[ego_change_types_tl|EGO_CHANGE_TYPES_TL]] — 4 atributos

---

## ⚙️ Atributos

### [[ego_change_types_b|EGO_CHANGE_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EgoChangeTypesBasePEOApplicationId | APPLICATION_ID | — | ✅ |
| 2 | EgoChangeTypesBasePEOAutoCompleteOnCancelFlag | AUTO_COMPLETE_ON_CANCEL_FLAG | — | ✅ |
| 3 | EgoChangeTypesBasePEOAutoNumberingMethod | AUTO_NUMBERING_METHOD | — | ✅ |
| 4 | EgoChangeTypesBasePEOBaseChangeMgmtTypeCode | BASE_CHANGE_MGMT_TYPE_CODE | — | ✅ |
| 5 | EgoChangeTypesBasePEOChangeTypeId | CHANGE_TYPE_ID | 🔑 | ✅ |
| 6 | EgoChangeTypesBasePEOCopiedFrom | COPIED_FROM | — | ✅ |
| 7 | EgoChangeTypesBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 8 | EgoChangeTypesBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 9 | EgoChangeTypesBasePEODefaultAssigneeFromRoleId | DEFAULT_ASSIGNEE_FROM_ROLE_ID | — | ✅ |
| 10 | EgoChangeTypesBasePEODefaultAssigneeId | DEFAULT_ASSIGNEE_ID | — | ✅ |
| 11 | EgoChangeTypesBasePEODefaultAssigneeType | DEFAULT_ASSIGNEE_TYPE | — | ✅ |
| 12 | EgoChangeTypesBasePEODisableDate | DISABLE_DATE | — | ✅ |
| 13 | EgoChangeTypesBasePEOEffectiveImmediatelyFlag | EFFECTIVE_IMMEDIATELY_FLAG | — | ✅ |
| 14 | EgoChangeTypesBasePEOEffectivityIncrementDays | EFFECTIVITY_INCREMENT_DAYS | — | ✅ |
| 15 | EgoChangeTypesBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | EgoChangeTypesBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 17 | EgoChangeTypesBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 18 | EgoChangeTypesBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 19 | EgoChangeTypesBasePEOPriorityCode | PRIORITY_CODE | — | ✅ |
| 20 | EgoChangeTypesBasePEORequestId | REQUEST_ID | — | ✅ |
| 21 | EgoChangeTypesBasePEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 22 | EgoChangeTypesBasePEOSeededFlag | SEEDED_FLAG | — | ✅ |
| 23 | EgoChangeTypesBasePEOStartDate | START_DATE | — | ✅ |
| 24 | EgoChangeTypesBasePEOSubjectInternalName | SUBJECT_INTERNAL_NAME | — | ✅ |
| 25 | EgoChangeTypesBasePEOTypeClassification | TYPE_CLASSIFICATION | — | ✅ |
| 26 | EgoChangeTypesBasePEOTypeInternalName | TYPE_INTERNAL_NAME | — | ✅ |

### [[ego_change_types_tl|EGO_CHANGE_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EgoChangeTypesTLPEOChangeTypeId | CHANGE_TYPE_ID | — | — |
| 2 | EgoChangeTypesTLPEODescription | DESCRIPTION | — | — |
| 3 | EgoChangeTypesTLPEOLanguage | LANGUAGE | — | — |
| 4 | EgoChangeTypesTLPEOTypeName | TYPE_NAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
