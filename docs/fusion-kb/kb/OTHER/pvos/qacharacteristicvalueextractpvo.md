---
id: DOC-OTHER-PVO-QaCharacteristicValueExtractPVO
doc_type: system-doc
title: "QaCharacteristicValueExtractPVO — PVO Cross-Module"
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
  - QaCharacteristicValueExtractPVO
  - qacharacteristicvalueextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QaCharacteristicValueExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Qa Characteristic Value Extract. Acessa as tabelas: QA_CS_VALUES_B, QA_CS_VALUES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.QaBiccExtractAM.QaCharacteristicValueExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 17 | 2 | 2 | 17 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[qa_cs_values_b|QA_CS_VALUES_B]] — 7 atributos (7 BICC)
- [[qa_cs_values_tl|QA_CS_VALUES_TL]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[qa_cs_values_b|QA_CS_VALUES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CharacteristicValueBasePEOCharacteristicId | CHARACTERISTIC_ID | — | ✅ |
| 2 | CharacteristicValueBasePEOCsValueCode | CS_VALUE_CODE | — | ✅ |
| 3 | CharacteristicValueBasePEOCsValueId | CS_VALUE_ID | — | ✅ |
| 4 | CharacteristicValueBasePEODisplaySequence | DISPLAY_SEQUENCE | — | ✅ |
| 5 | CharacteristicValueBasePEOEnabledFlag | ENABLED_FLAG | — | ✅ |
| 6 | CharacteristicValueBasePEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 7 | CharacteristicValueBasePEOStartDateActive | START_DATE_ACTIVE | — | ✅ |

### [[qa_cs_values_tl|QA_CS_VALUES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CharacteristicValueTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | CharacteristicValueTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | CharacteristicValueTLPEOCsValueId | CS_VALUE_ID | 🔑 | ✅ |
| 4 | CharacteristicValueTLPEODescription | DESCRIPTION | — | ✅ |
| 5 | CharacteristicValueTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | CharacteristicValueTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | CharacteristicValueTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | CharacteristicValueTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | CharacteristicValueTLPEOName | NAME | — | ✅ |
| 10 | CharacteristicValueTLPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
