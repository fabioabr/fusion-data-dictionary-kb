---
id: DOC-OTHER-PVO-StructureTypesPVO
doc_type: system-doc
title: "StructureTypesPVO — PVO Cross-Module"
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
  - StructureTypesPVO
  - structuretypespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# StructureTypesPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Structure Types. Acessa as tabelas: EGP_STRUCTURE_TYPES_B, EGP_STRUCTURE_TYPES_TL.

**Caminho:** `FscmTopModelAM.EgpStructuresPublicModelAM.StructureTypesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 24 | 2 | 1 | 9 | 38% |

---

## 🔗 Tabelas Relacionadas

- [[egp_structure_types_b|EGP_STRUCTURE_TYPES_B]] — 13 atributos (1 PKs, 5 BICC)
- [[egp_structure_types_tl|EGP_STRUCTURE_TYPES_TL]] — 11 atributos (4 BICC)

---

## ⚙️ Atributos

### [[egp_structure_types_b|EGP_STRUCTURE_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | StructureTypeId | STRUCTURE_TYPE_ID | 🔑 | ✅ |
| 2 | StructureTypesBasePEOApplicationId | APPLICATION_ID | — | — |
| 3 | StructureTypesBasePEOCompItmSeqInc | COMP_ITM_SEQ_INC | — | — |
| 4 | StructureTypesBasePEOCreatedBy | CREATED_BY | — | — |
| 5 | StructureTypesBasePEOCreationDate | CREATION_DATE | — | — |
| 6 | StructureTypesBasePEODefWipSupForCompFlag | DEF_WIP_SUP_FOR_COMP_FLAG | — | — |
| 7 | StructureTypesBasePEODisableDate | DISABLE_DATE | — | ✅ |
| 8 | StructureTypesBasePEOEffectiveDate | EFFECTIVE_DATE | — | ✅ |
| 9 | StructureTypesBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | StructureTypesBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | StructureTypesBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | StructureTypesBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | StructureTypesBasePEOStructureTypeName | STRUCTURE_TYPE_NAME | — | ✅ |

### [[egp_structure_types_tl|EGP_STRUCTURE_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | StructureTypesTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | StructureTypesTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | StructureTypesTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | StructureTypesTranslationPEODisplayName | DISPLAY_NAME | — | ✅ |
| 5 | StructureTypesTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 6 | StructureTypesTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | StructureTypesTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | StructureTypesTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | StructureTypesTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | StructureTypesTranslationPEOSourceLang | SOURCE_LANG | — | — |
| 11 | StructureTypesTranslationPEOStructureTypeId | STRUCTURE_TYPE_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
