---
id: DOC-OTHER-PVO-ProjectSetTranslationExtractPVO
doc_type: system-doc
title: "ProjectSetTranslationExtractPVO — PVO Cross-Module"
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
  - ProjectSetTranslationExtractPVO
  - projectsettranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectSetTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Set Translation Extract. Acessa as tabelas: PJF_PROJECT_SETS_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.ProjectSetTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_project_sets_tl|PJF_PROJECT_SETS_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[pjf_project_sets_tl|PJF_PROJECT_SETS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectSetTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | ProjectSetTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | ProjectSetTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | ProjectSetTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | ProjectSetTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ProjectSetTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | ProjectSetTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ProjectSetTranslationPEOName | NAME | — | ✅ |
| 9 | ProjectSetTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | ProjectSetTranslationPEOProjectSetId | PROJECT_SET_ID | 🔑 | ✅ |
| 11 | ProjectSetTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
