---
id: DOC-OTHER-PVO-SubledgerMappingSetInputExtractPVO
doc_type: system-doc
title: "SubledgerMappingSetInputExtractPVO — PVO Cross-Module"
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
  - SubledgerMappingSetInputExtractPVO
  - subledgermappingsetinputextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SubledgerMappingSetInputExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Subledger Mapping Set Input Extract. Acessa as tabelas: XLA_MAPPING_SET_INPUTS.

**Caminho:** `FscmTopModelAM.FinExtractAM.XlaBiccExtractAM.SubledgerMappingSetInputExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 18 | 1 | 1 | 18 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[xla_mapping_set_inputs|XLA_MAPPING_SET_INPUTS]] — 18 atributos (1 PKs, 18 BICC)

---

## ⚙️ Atributos

### [[xla_mapping_set_inputs|XLA_MAPPING_SET_INPUTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MappingSetInputAmbContextCode | AMB_CONTEXT_CODE | — | ✅ |
| 2 | MappingSetInputApplicationId | APPLICATION_ID | — | ✅ |
| 3 | MappingSetInputCreatedBy | CREATED_BY | — | ✅ |
| 4 | MappingSetInputCreationDate | CREATION_DATE | — | ✅ |
| 5 | MappingSetInputFlexSegment | FLEX_SEGMENT | — | ✅ |
| 6 | MappingSetInputInputSeq | INPUT_SEQ | — | ✅ |
| 7 | MappingSetInputLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | MappingSetInputLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | MappingSetInputLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | MappingSetInputLookupType | LOOKUP_TYPE | — | ✅ |
| 11 | MappingSetInputMappingSetCode | MAPPING_SET_CODE | — | ✅ |
| 12 | MappingSetInputMappingSetInputId | MAPPING_SET_INPUT_ID | 🔑 | ✅ |
| 13 | MappingSetInputObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | MappingSetInputSourceApplicationId | SOURCE_APPLICATION_ID | — | ✅ |
| 15 | MappingSetInputSourceCode | SOURCE_CODE | — | ✅ |
| 16 | MappingSetInputSourceTypeCode | SOURCE_TYPE_CODE | — | ✅ |
| 17 | MappingSetInputValueSetId | VALUE_SET_ID | — | ✅ |
| 18 | MappingSetInputViewApplicationId | VIEW_APPLICATION_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
