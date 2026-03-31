---
id: DOC-OTHER-PVO-FundingSourceTranslationPVO
doc_type: system-doc
title: "FundingSourceTranslationPVO — PVO Cross-Module"
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
  - FundingSourceTranslationPVO
  - fundingsourcetranslationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FundingSourceTranslationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Funding Source Translation. Acessa as tabelas: GMS_FUNDING_SOURCES_TL.

**Caminho:** `FscmTopModelAM.GmsSetupAM.FundingSourceTranslationPVO`

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
| 1 | FundingSourceId | FUNDING_SOURCE_ID | 🔑 | ✅ |
| 2 | FundingSourceTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | FundingSourceTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | FundingSourceTranslationPEODescription | DESCRIPTION | — | ✅ |
| 5 | FundingSourceTranslationPEOFundingSourceName | FUNDING_SOURCE_NAME | — | ✅ |
| 6 | FundingSourceTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | FundingSourceTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | FundingSourceTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | FundingSourceTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | FundingSourceTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |
| 11 | Language | LANGUAGE | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
