---
id: DOC-OTHER-PVO-ProjectTranslationExtractPVO
doc_type: system-doc
title: "ProjectTranslationExtractPVO — PVO Cross-Module"
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
  - ProjectTranslationExtractPVO
  - projecttranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Translation Extract. Acessa as tabelas: PJF_PROJECTS_ALL_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.ProjectTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 2 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_projects_all_tl|PJF_PROJECTS_ALL_TL]] — 12 atributos (2 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[pjf_projects_all_tl|PJF_PROJECTS_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | ProjectTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | ProjectTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | ProjectTranslationPEOExecutionCustomerName | EXECUTION_CUSTOMER_NAME | — | ✅ |
| 5 | ProjectTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | ProjectTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ProjectTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | ProjectTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ProjectTranslationPEOName | NAME | — | ✅ |
| 10 | ProjectTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | ProjectTranslationPEOProjectId | PROJECT_ID | 🔑 | ✅ |
| 12 | ProjectTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
