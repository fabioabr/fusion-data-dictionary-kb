---
id: DOC-OTHER-PVO-DemandClass
doc_type: system-doc
title: "DemandClass — PVO Cross-Module"
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
  - DemandClass
  - demandclass
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DemandClass

## 📌 Visão Geral

View Object para extração BICC de dados de Demand Class. Acessa as tabelas: MSC_SR_LOOKUP_VALUES_TL.

**Caminho:** `FscmTopModelAM.MscAnalyticsTopAM.DemandClass`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 3 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[msc_sr_lookup_values_tl|MSC_SR_LOOKUP_VALUES_TL]] — 12 atributos (3 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[msc_sr_lookup_values_tl|MSC_SR_LOOKUP_VALUES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Language | LANGUAGE | 🔑 | ✅ |
| 2 | LookupCode | LOOKUP_CODE | 🔑 | ✅ |
| 3 | LookupType | LOOKUP_TYPE | 🔑 | ✅ |
| 4 | SrLookupValueTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | SrLookupValueTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | SrLookupValueTranslationPEODescription | DESCRIPTION | — | ✅ |
| 7 | SrLookupValueTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | SrLookupValueTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | SrLookupValueTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | SrLookupValueTranslationPEOMeaning | MEANING | — | ✅ |
| 11 | SrLookupValueTranslationPEORefreshNumber | REFRESH_NUMBER | — | ✅ |
| 12 | SrLookupValueTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
