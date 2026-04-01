---
id: DOC-OTHER-PVO-StructureHeaderPVO
doc_type: system-doc
title: "StructureHeaderPVO — PVO Cross-Module"
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
  - StructureHeaderPVO
  - structureheaderpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# StructureHeaderPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Structure Header. Acessa as tabelas: EGP_STRUCTURES_B, EGP_STRUCTURE_NAMES_VL.

**Caminho:** `FscmTopModelAM.EgpStructuresPublicModelAM.StructureHeaderPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 50 | 2 | 1 | 7 | 14% |

---

## 🔗 Tabelas Relacionadas

- [[egp_structures_b|EGP_STRUCTURES_B]] — 29 atributos (1 PKs, 6 BICC)
- [[egp_structure_names_vl|EGP_STRUCTURE_NAMES_VL]] — 21 atributos (1 BICC)

---

## ⚙️ Atributos

### [[egp_structures_b|EGP_STRUCTURES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BillSequenceId | BILL_SEQUENCE_ID | 🔑 | ✅ |
| 2 | StructureHeaderPEOAlternateBomDesignator | ALTERNATE_BOM_DESIGNATOR | — | ✅ |
| 3 | StructureHeaderPEOChangeId | CHANGE_ID | — | — |
| 4 | StructureHeaderPEOChangeLineId | CHANGE_LINE_ID | — | — |
| 5 | StructureHeaderPEOCommonAssemblyItemId | COMMON_ASSEMBLY_ITEM_ID | — | — |
| 6 | StructureHeaderPEOCommonBillSequenceId | COMMON_BILL_SEQUENCE_ID | — | — |
| 7 | StructureHeaderPEOCommonOrganizationId | COMMON_ORGANIZATION_ID | — | — |
| 8 | StructureHeaderPEOCreatedBy | CREATED_BY | — | — |
| 9 | StructureHeaderPEOCreationDate | CREATION_DATE | — | — |
| 10 | StructureHeaderPEOEffectivityControl | EFFECTIVITY_CONTROL | — | ✅ |
| 11 | StructureHeaderPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 12 | StructureHeaderPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 13 | StructureHeaderPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | StructureHeaderPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | StructureHeaderPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 16 | StructureHeaderPEOObjName | OBJ_NAME | — | ✅ |
| 17 | StructureHeaderPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | StructureHeaderPEOOriginalSystemReference | ORIGINAL_SYSTEM_REFERENCE | — | — |
| 19 | StructureHeaderPEOPk1Value | PK1_VALUE | — | — |
| 20 | StructureHeaderPEOPk2Value | PK2_VALUE | — | — |
| 21 | StructureHeaderPEOPk3Value | PK3_VALUE | — | — |
| 22 | StructureHeaderPEOPk4Value | PK4_VALUE | — | — |
| 23 | StructureHeaderPEOPk5Value | PK5_VALUE | — | — |
| 24 | StructureHeaderPEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 25 | StructureHeaderPEOProgramName | PROGRAM_NAME | — | — |
| 26 | StructureHeaderPEORequestId | REQUEST_ID | — | — |
| 27 | StructureHeaderPEOSourceBillSequenceId | SOURCE_BILL_SEQUENCE_ID | — | — |
| 28 | StructureHeaderPEOSpecificAssemblyComment | SPECIFIC_ASSEMBLY_COMMENT | — | ✅ |
| 29 | StructureHeaderPEOStructureTypeId | STRUCTURE_TYPE_ID | — | — |

### [[egp_structure_names_vl|EGP_STRUCTURE_NAMES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | StructureNamePEOAlternateDesignatorCode | ALTERNATE_DESIGNATOR_CODE | — | — |
| 2 | StructureNamePEOAlternateDesignatorId | ALTERNATE_DESIGNATOR_ID | — | — |
| 3 | StructureNamePEOApplicationId | APPLICATION_ID | — | — |
| 4 | StructureNamePEOCreatedBy | CREATED_BY | — | — |
| 5 | StructureNamePEOCreationDate | CREATION_DATE | — | — |
| 6 | StructureNamePEODescription | DESCRIPTION | — | — |
| 7 | StructureNamePEODisableDate | DISABLE_DATE | — | — |
| 8 | StructureNamePEODisplayName | DISPLAY_NAME | — | — |
| 9 | StructureNamePEOEffectiveDate | EFFECTIVE_DATE | — | — |
| 10 | StructureNamePEOLanguage | LANGUAGE | — | — |
| 11 | StructureNamePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | StructureNamePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | StructureNamePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | StructureNamePEOLifecycleValidationFlag | LIFECYCLE_VALIDATION_FLAG | — | — |
| 15 | StructureNamePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | StructureNamePEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 17 | StructureNamePEOProgramName | PROGRAM_NAME | — | — |
| 18 | StructureNamePEORequestId | REQUEST_ID | — | — |
| 19 | StructureNamePEOSourceLang | SOURCE_LANG | — | — |
| 20 | StructureNamePEOStructureTypeId | STRUCTURE_TYPE_ID | — | — |
| 21 | StructureNamePEOUsePrimaryForExplFlag | USE_PRIMARY_FOR_EXPL_FLAG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
