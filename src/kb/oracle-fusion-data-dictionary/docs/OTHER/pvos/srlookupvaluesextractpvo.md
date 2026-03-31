---
id: DOC-OTHER-PVO-SrLookupValuesExtractPVO
doc_type: system-doc
title: "SrLookupValuesExtractPVO — PVO Cross-Module"
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
  - SrLookupValuesExtractPVO
  - srlookupvaluesextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SrLookupValuesExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Sr Lookup Values Extract. Acessa as tabelas: MSC_SR_LOOKUP_VALUES_B, MSC_SR_LOOKUP_VALUES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DooBiccExtractAM.SrLookupValuesExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 23 | 2 | 6 | 23 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[msc_sr_lookup_values_b|MSC_SR_LOOKUP_VALUES_B]] — 11 atributos (2 PKs, 11 BICC)
- [[msc_sr_lookup_values_tl|MSC_SR_LOOKUP_VALUES_TL]] — 12 atributos (4 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[msc_sr_lookup_values_b|MSC_SR_LOOKUP_VALUES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SrLookupValuesBaseCreatedBy | CREATED_BY | — | ✅ |
| 2 | SrLookupValuesBaseCreationDate | CREATION_DATE | — | ✅ |
| 3 | SrLookupValuesBaseEnabledFlag | ENABLED_FLAG | — | ✅ |
| 4 | SrLookupValuesBaseEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 5 | SrLookupValuesBaseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | SrLookupValuesBaseLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | SrLookupValuesBaseLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | SrLookupValuesBaseLookupCode | LOOKUP_CODE | 🔑 | ✅ |
| 9 | SrLookupValuesBaseLookupType | LOOKUP_TYPE | 🔑 | ✅ |
| 10 | SrLookupValuesBaseRefreshNumber | REFRESH_NUMBER | — | ✅ |
| 11 | SrLookupValuesBaseStartDateActive | START_DATE_ACTIVE | — | ✅ |

### [[msc_sr_lookup_values_tl|MSC_SR_LOOKUP_VALUES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SrLookupValueTranslationCreatedBy | CREATED_BY | — | ✅ |
| 2 | SrLookupValueTranslationCreationDate | CREATION_DATE | — | ✅ |
| 3 | SrLookupValueTranslationDescription | DESCRIPTION | — | ✅ |
| 4 | SrLookupValueTranslationLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | SrLookupValueTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | SrLookupValueTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | SrLookupValueTranslationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | SrLookupValueTranslationLookupCode | LOOKUP_CODE | 🔑 | ✅ |
| 9 | SrLookupValueTranslationLookupType | LOOKUP_TYPE | 🔑 | ✅ |
| 10 | SrLookupValueTranslationMeaning | MEANING | — | ✅ |
| 11 | SrLookupValueTranslationRefreshNumber | REFRESH_NUMBER | — | ✅ |
| 12 | SrLookupValueTranslationSourceLang | SOURCE_LANG | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
