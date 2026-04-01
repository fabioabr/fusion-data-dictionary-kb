---
id: DOC-OTHER-PVO-SubledgerMappingSetExtractPVO
doc_type: system-doc
title: "SubledgerMappingSetExtractPVO — PVO Cross-Module"
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
  - SubledgerMappingSetExtractPVO
  - subledgermappingsetextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SubledgerMappingSetExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Subledger Mapping Set Extract. Acessa as tabelas: XLA_MAPPING_SETS_B, XLA_MAPPING_SETS_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.XlaBiccExtractAM.SubledgerMappingSetExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 30 | 2 | 3 | 30 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[xla_mapping_sets_b|XLA_MAPPING_SETS_B]] — 17 atributos (3 PKs, 17 BICC)
- [[xla_mapping_sets_tl|XLA_MAPPING_SETS_TL]] — 13 atributos (13 BICC)

---

## ⚙️ Atributos

### [[xla_mapping_sets_b|XLA_MAPPING_SETS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MappingSetBAmbContextCode | AMB_CONTEXT_CODE | 🔑 | ✅ |
| 2 | MappingSetBApplicationId | APPLICATION_ID | 🔑 | ✅ |
| 3 | MappingSetBCreatedBy | CREATED_BY | — | ✅ |
| 4 | MappingSetBCreationDate | CREATION_DATE | — | ✅ |
| 5 | MappingSetBEnabledFlag | ENABLED_FLAG | — | ✅ |
| 6 | MappingSetBFlexfieldAssignModeCode | FLEXFIELD_ASSIGN_MODE_CODE | — | ✅ |
| 7 | MappingSetBFlexfieldSegmentCode | FLEXFIELD_SEGMENT_CODE | — | ✅ |
| 8 | MappingSetBLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | MappingSetBLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | MappingSetBLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | MappingSetBMappingSetCode | MAPPING_SET_CODE | 🔑 | ✅ |
| 12 | MappingSetBMappingSetId | MAPPING_SET_ID | — | ✅ |
| 13 | MappingSetBNumInputs | NUM_INPUTS | — | ✅ |
| 14 | MappingSetBObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 15 | MappingSetBOwnerCode | OWNER_CODE | — | ✅ |
| 16 | MappingSetBUpdatedFlag | UPDATED_FLAG | — | ✅ |
| 17 | MappingSetBUserLanguage | LANGUAGE | — | ✅ |

### [[xla_mapping_sets_tl|XLA_MAPPING_SETS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MappingSetTLAmbContextCode | AMB_CONTEXT_CODE | — | ✅ |
| 2 | MappingSetTLApplicationId | APPLICATION_ID | — | ✅ |
| 3 | MappingSetTLCreatedBy | CREATED_BY | — | ✅ |
| 4 | MappingSetTLCreationDate | CREATION_DATE | — | ✅ |
| 5 | MappingSetTLDescription | DESCRIPTION | — | ✅ |
| 6 | MappingSetTLLanguage | LANGUAGE | — | ✅ |
| 7 | MappingSetTLLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | MappingSetTLLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | MappingSetTLLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | MappingSetTLMappingSetCode | MAPPING_SET_CODE | — | ✅ |
| 11 | MappingSetTLName | NAME | — | ✅ |
| 12 | MappingSetTLObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | MappingSetTLSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
