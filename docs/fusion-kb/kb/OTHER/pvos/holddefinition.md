---
id: DOC-OTHER-PVO-HoldDefinition
doc_type: system-doc
title: "HoldDefinition — PVO Cross-Module"
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
  - HoldDefinition
  - holddefinition
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# HoldDefinition

## 📌 Visão Geral

View Object para extração BICC de dados de Hold Definition. Acessa as tabelas: DOO_HOLD_CODES_B, DOO_HOLD_CODES_TL.

**Caminho:** `FscmTopModelAM.DooTopAM.HoldDefinition`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 25 | 2 | 1 | 9 | 36% |

---

## 🔗 Tabelas Relacionadas

- [[doo_hold_codes_b|DOO_HOLD_CODES_B]] — 14 atributos (1 PKs, 9 BICC)
- [[doo_hold_codes_tl|DOO_HOLD_CODES_TL]] — 11 atributos

---

## ⚙️ Atributos

### [[doo_hold_codes_b|DOO_HOLD_CODES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HoldCreatedBy | CREATED_BY | — | ✅ |
| 2 | HoldCreationDate | CREATION_DATE | — | ✅ |
| 3 | HoldEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 4 | HoldEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 5 | HoldGeneralHoldFlag | GENERAL_HOLD_FLAG | — | — |
| 6 | HoldHoldCode | HOLD_CODE | — | ✅ |
| 7 | HoldHoldCodeId | HOLD_CODE_ID | 🔑 | ✅ |
| 8 | HoldLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | HoldLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | HoldLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | HoldObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | HoldOrchestrationApplicationId | ORCHESTRATION_APPLICATION_ID | — | ✅ |
| 13 | HoldSetId | SET_ID | — | — |
| 14 | HoldSystemFlag | SYSTEM_FLAG | — | — |

### [[doo_hold_codes_tl|DOO_HOLD_CODES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HoldTranslationCreatedBy | CREATED_BY | — | — |
| 2 | HoldTranslationCreationDate | CREATION_DATE | — | — |
| 3 | HoldTranslationHoldCodeId | HOLD_CODE_ID | — | — |
| 4 | HoldTranslationHoldDescription | HOLD_DESCRIPTION | — | — |
| 5 | HoldTranslationHoldName | HOLD_NAME | — | — |
| 6 | HoldTranslationLanguage | LANGUAGE | — | — |
| 7 | HoldTranslationLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 8 | HoldTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | HoldTranslationLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | HoldTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | HoldTranslationSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
