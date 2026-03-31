---
id: DOC-OTHER-PVO-ProjectSetExtractPVO
doc_type: system-doc
title: "ProjectSetExtractPVO — PVO Cross-Module"
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
  - ProjectSetExtractPVO
  - projectsetextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectSetExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Set Extract. Acessa as tabelas: PJF_PROJECT_SETS_B, PJF_PROJECT_SETS_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.ProjectSetExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 38 | 2 | 1 | 22 | 58% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_project_sets_b|PJF_PROJECT_SETS_B]] — 27 atributos (1 PKs, 11 BICC)
- [[pjf_project_sets_tl|PJF_PROJECT_SETS_TL]] — 11 atributos (11 BICC)

---

## ⚙️ Atributos

### [[pjf_project_sets_b|PJF_PROJECT_SETS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectSetBasePEOAttribute1 | ATTRIBUTE1 | — | — |
| 2 | ProjectSetBasePEOAttribute10 | ATTRIBUTE10 | — | — |
| 3 | ProjectSetBasePEOAttribute11 | ATTRIBUTE11 | — | — |
| 4 | ProjectSetBasePEOAttribute12 | ATTRIBUTE12 | — | — |
| 5 | ProjectSetBasePEOAttribute13 | ATTRIBUTE13 | — | — |
| 6 | ProjectSetBasePEOAttribute14 | ATTRIBUTE14 | — | — |
| 7 | ProjectSetBasePEOAttribute15 | ATTRIBUTE15 | — | — |
| 8 | ProjectSetBasePEOAttribute2 | ATTRIBUTE2 | — | — |
| 9 | ProjectSetBasePEOAttribute3 | ATTRIBUTE3 | — | — |
| 10 | ProjectSetBasePEOAttribute4 | ATTRIBUTE4 | — | — |
| 11 | ProjectSetBasePEOAttribute5 | ATTRIBUTE5 | — | — |
| 12 | ProjectSetBasePEOAttribute6 | ATTRIBUTE6 | — | — |
| 13 | ProjectSetBasePEOAttribute7 | ATTRIBUTE7 | — | — |
| 14 | ProjectSetBasePEOAttribute8 | ATTRIBUTE8 | — | — |
| 15 | ProjectSetBasePEOAttribute9 | ATTRIBUTE9 | — | — |
| 16 | ProjectSetBasePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 17 | ProjectSetBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 18 | ProjectSetBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 19 | ProjectSetBasePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 20 | ProjectSetBasePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 21 | ProjectSetBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 22 | ProjectSetBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 23 | ProjectSetBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 24 | ProjectSetBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 25 | ProjectSetBasePEOPartyId | PARTY_ID | — | ✅ |
| 26 | ProjectSetBasePEOProjectSetId | PROJECT_SET_ID | 🔑 | ✅ |
| 27 | ProjectSetBasePEOSharedFlag | SHARED_FLAG | — | ✅ |

### [[pjf_project_sets_tl|PJF_PROJECT_SETS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectSetTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | ProjectSetTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | ProjectSetTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | ProjectSetTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 5 | ProjectSetTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ProjectSetTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | ProjectSetTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ProjectSetTranslationPEOName | NAME | — | ✅ |
| 9 | ProjectSetTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | ProjectSetTranslationPEOProjectSetId | PROJECT_SET_ID | — | ✅ |
| 11 | ProjectSetTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
