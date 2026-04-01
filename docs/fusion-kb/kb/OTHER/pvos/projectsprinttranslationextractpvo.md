---
id: DOC-OTHER-PVO-ProjectSprintTranslationExtractPVO
doc_type: system-doc
title: "ProjectSprintTranslationExtractPVO — PVO Cross-Module"
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
  - ProjectSprintTranslationExtractPVO
  - projectsprinttranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectSprintTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Sprint Translation Extract. Acessa as tabelas: PJT_SPRINT_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjtBiccExtractAM.ProjectSprintTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjt_sprint_tl|PJT_SPRINT_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[pjt_sprint_tl|PJT_SPRINT_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjtSprintTranslationEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | PjtSprintTranslationEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | PjtSprintTranslationEOLanguage | LANGUAGE | 🔑 | ✅ |
| 4 | PjtSprintTranslationEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | PjtSprintTranslationEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | PjtSprintTranslationEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | PjtSprintTranslationEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | PjtSprintTranslationEOSourceLang | SOURCE_LANG | — | ✅ |
| 9 | PjtSprintTranslationEOSprintDesc | SPRINT_DESC | — | ✅ |
| 10 | PjtSprintTranslationEOSprintId | SPRINT_ID | 🔑 | ✅ |
| 11 | PjtSprintTranslationEOSprintName | SPRINT_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
