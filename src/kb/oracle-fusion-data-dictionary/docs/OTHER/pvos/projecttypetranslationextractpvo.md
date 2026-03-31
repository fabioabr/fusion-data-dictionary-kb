---
id: DOC-OTHER-PVO-ProjectTypeTranslationExtractPVO
doc_type: system-doc
title: "ProjectTypeTranslationExtractPVO — PVO Cross-Module"
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
  - ProjectTypeTranslationExtractPVO
  - projecttypetranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectTypeTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Type Translation Extract. Acessa as tabelas: PJF_PROJECT_TYPES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.ProjectTypeTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_project_types_tl|PJF_PROJECT_TYPES_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[pjf_project_types_tl|PJF_PROJECT_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectTypeTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | ProjectTypeTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | ProjectTypeTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | ProjectTypeTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | ProjectTypeTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ProjectTypeTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | ProjectTypeTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ProjectTypeTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | ProjectTypeTranslationPEOProjectType | PROJECT_TYPE | — | ✅ |
| 10 | ProjectTypeTranslationPEOProjectTypeId | PROJECT_TYPE_ID | 🔑 | ✅ |
| 11 | ProjectTypeTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
