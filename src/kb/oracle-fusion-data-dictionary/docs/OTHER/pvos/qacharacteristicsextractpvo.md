---
id: DOC-OTHER-PVO-QaCharacteristicsExtractPVO
doc_type: system-doc
title: "QaCharacteristicsExtractPVO — PVO Cross-Module"
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
  - QaCharacteristicsExtractPVO
  - qacharacteristicsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QaCharacteristicsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Qa Characteristics Extract. Acessa as tabelas: QA_CHARACTERISTICS_B, QA_CHARACTERISTICS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.QaBiccExtractAM.QaCharacteristicsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 32 | 2 | 2 | 31 | 97% |

---

## 🔗 Tabelas Relacionadas

- [[qa_characteristics_b|QA_CHARACTERISTICS_B]] — 22 atributos (21 BICC)
- [[qa_characteristics_tl|QA_CHARACTERISTICS_TL]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[qa_characteristics_b|QA_CHARACTERISTICS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AiSuggestion | AI_SUGGESTION | — | — |
| 2 | CharacteristicBaseRptPEOAttributeGroupMaximum | ATTRIBUTE_GROUP_MAXIMUM | — | ✅ |
| 3 | CharacteristicBaseRptPEOAttributeGroupMinimum | ATTRIBUTE_GROUP_MINIMUM | — | ✅ |
| 4 | CharacteristicBaseRptPEOAttributeGroupTarget | ATTRIBUTE_GROUP_TARGET | — | ✅ |
| 5 | CharacteristicBaseRptPEOAttributeMaximum | ATTRIBUTE_MAXIMUM | — | ✅ |
| 6 | CharacteristicBaseRptPEOAttributeMaximumDate | ATTRIBUTE_MAXIMUM_DATE | — | ✅ |
| 7 | CharacteristicBaseRptPEOAttributeMinimum | ATTRIBUTE_MINIMUM | — | ✅ |
| 8 | CharacteristicBaseRptPEOAttributeMinimumDate | ATTRIBUTE_MINIMUM_DATE | — | ✅ |
| 9 | CharacteristicBaseRptPEOAttributeTarget | ATTRIBUTE_TARGET | — | ✅ |
| 10 | CharacteristicBaseRptPEOCharacteristicId | CHARACTERISTIC_ID | — | ✅ |
| 11 | CharacteristicBaseRptPEOCharacteristicType | CHARACTERISTIC_TYPE | — | ✅ |
| 12 | CharacteristicBaseRptPEOContextType | CONTEXT_TYPE | — | ✅ |
| 13 | CharacteristicBaseRptPEODataType | DATA_TYPE | — | ✅ |
| 14 | CharacteristicBaseRptPEODecimalPrecision | DECIMAL_PRECISION | — | ✅ |
| 15 | CharacteristicBaseRptPEODefaultValue | DEFAULT_VALUE | — | ✅ |
| 16 | CharacteristicBaseRptPEOEnabledFlag | ENABLED_FLAG | — | ✅ |
| 17 | CharacteristicBaseRptPEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 18 | CharacteristicBaseRptPEOItemClassId | ITEM_CLASS_ID | — | ✅ |
| 19 | CharacteristicBaseRptPEOStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 20 | CharacteristicBaseRptPEOTargetValueDate | TARGET_VALUE_DATE | — | ✅ |
| 21 | CharacteristicBaseRptPEOUomCode | UOM_CODE | — | ✅ |
| 22 | CharacteristicBaseRptPEOValueSetId | VALUE_SET_ID | — | ✅ |

### [[qa_characteristics_tl|QA_CHARACTERISTICS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QaCharacteristicRptTLPEOCharacteristicId | CHARACTERISTIC_ID | 🔑 | ✅ |
| 2 | QaCharacteristicRptTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | QaCharacteristicRptTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | QaCharacteristicRptTLPEODescription | DESCRIPTION | — | ✅ |
| 5 | QaCharacteristicRptTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | QaCharacteristicRptTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | QaCharacteristicRptTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | QaCharacteristicRptTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | QaCharacteristicRptTLPEOName | NAME | — | ✅ |
| 10 | QaCharacteristicRptTLPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
