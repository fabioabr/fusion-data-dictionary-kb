---
id: DOC-OTHER-PVO-FundingSourceTranslationExtractPVO
doc_type: system-doc
title: "FundingSourceTranslationExtractPVO — PVO Cross-Module"
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
  - FundingSourceTranslationExtractPVO
  - fundingsourcetranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FundingSourceTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Funding Source Translation Extract. Acessa as tabelas: GMS_FUNDING_SOURCES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.GmsBiccExtractAM.FundingSourceTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gms_funding_sources_tl|GMS_FUNDING_SOURCES_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[gms_funding_sources_tl|GMS_FUNDING_SOURCES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FundingSourceTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | FundingSourceTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | FundingSourceTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | FundingSourceTranslationPEOFundingSourceId | FUNDING_SOURCE_ID | 🔑 | ✅ |
| 5 | FundingSourceTranslationPEOFundingSourceName | FUNDING_SOURCE_NAME | — | ✅ |
| 6 | FundingSourceTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 7 | FundingSourceTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | FundingSourceTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | FundingSourceTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | FundingSourceTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | FundingSourceTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
