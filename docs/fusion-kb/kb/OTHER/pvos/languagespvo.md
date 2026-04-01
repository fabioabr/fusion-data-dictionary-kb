---
id: DOC-OTHER-PVO-LanguagesPVO
doc_type: system-doc
title: "LanguagesPVO — PVO Cross-Module"
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
  - LanguagesPVO
  - languagespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LanguagesPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Languages. Acessa as tabelas: FND_LANGUAGES_B, FND_LANGUAGES_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.AnalyticsExtractServiceAM.LanguagesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 19 | 2 | 1 | 19 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_languages_b|FND_LANGUAGES_B]] — 15 atributos (1 PKs, 15 BICC)
- [[fnd_languages_tl|FND_LANGUAGES_TL]] — 4 atributos (4 BICC)

---

## ⚙️ Atributos

### [[fnd_languages_b|FND_LANGUAGES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | InstalledFlag | INSTALLED_FLAG | — | ✅ |
| 4 | IsoLanguage | ISO_LANGUAGE | — | ✅ |
| 5 | IsoLanguage3 | ISO_LANGUAGE_3 | — | ✅ |
| 6 | IsoTerritory | ISO_TERRITORY | — | ✅ |
| 7 | LanguageCode | LANGUAGE_CODE | 🔑 | ✅ |
| 8 | LanguageId | LANGUAGE_ID | — | ✅ |
| 9 | LanguageTag | LANGUAGE_TAG | — | ✅ |
| 10 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | NlsCodeset | NLS_CODESET | — | ✅ |
| 14 | NlsLanguage | NLS_LANGUAGE | — | ✅ |
| 15 | NlsTerritory | NLS_TERRITORY | — | ✅ |

### [[fnd_languages_tl|FND_LANGUAGES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Description | DESCRIPTION | — | ✅ |
| 2 | Language | LANGUAGE | — | ✅ |
| 3 | LanguageCode1 | LANGUAGE_CODE | — | ✅ |
| 4 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
