---
id: DOC-OTHER-PVO-ProjectStatusTranslationExtractPVO
doc_type: system-doc
title: "ProjectStatusTranslationExtractPVO — PVO Cross-Module"
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
  - ProjectStatusTranslationExtractPVO
  - projectstatustranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectStatusTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Status Translation Extract. Acessa as tabelas: PJF_PROJECT_STATUSES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.ProjectStatusTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_project_statuses_tl|PJF_PROJECT_STATUSES_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[pjf_project_statuses_tl|PJF_PROJECT_STATUSES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectStatusTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | ProjectStatusTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | ProjectStatusTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | ProjectStatusTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | ProjectStatusTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ProjectStatusTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | ProjectStatusTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ProjectStatusTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | ProjectStatusTranslationPEOProjectStatusCode | PROJECT_STATUS_CODE | 🔑 | ✅ |
| 10 | ProjectStatusTranslationPEOProjectStatusName | PROJECT_STATUS_NAME | — | ✅ |
| 11 | ProjectStatusTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
