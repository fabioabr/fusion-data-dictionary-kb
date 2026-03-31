---
id: DOC-OTHER-PVO-StatusExtractPVO
doc_type: system-doc
title: "StatusExtractPVO — PVO Cross-Module"
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
  - StatusExtractPVO
  - statusextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# StatusExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Status Extract. Acessa as tabelas: DOO_STATUSES_B, DOO_STATUSES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DooBiccExtractAM.StatusExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 2 | 3 | 20 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[doo_statuses_b|DOO_STATUSES_B]] — 10 atributos (1 PKs, 10 BICC)
- [[doo_statuses_tl|DOO_STATUSES_TL]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[doo_statuses_b|DOO_STATUSES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | StatusCreatedBy | CREATED_BY | — | ✅ |
| 2 | StatusCreationDate | CREATION_DATE | — | ✅ |
| 3 | StatusLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | StatusLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 5 | StatusLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 6 | StatusObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 7 | StatusOrchestrationApplicationId | ORCHESTRATION_APPLICATION_ID | — | ✅ |
| 8 | StatusSeededFlag | SEEDED_FLAG | — | ✅ |
| 9 | StatusStatusCode | STATUS_CODE | — | ✅ |
| 10 | StatusStatusId | STATUS_ID | 🔑 | ✅ |

### [[doo_statuses_tl|DOO_STATUSES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | StatusTranslationCreatedBy | CREATED_BY | — | ✅ |
| 2 | StatusTranslationCreationDate | CREATION_DATE | — | ✅ |
| 3 | StatusTranslationDisplayName | DISPLAY_NAME | — | ✅ |
| 4 | StatusTranslationLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | StatusTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | StatusTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | StatusTranslationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | StatusTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | StatusTranslationSourceLang | SOURCE_LANG | — | ✅ |
| 10 | StatusTranslationStatusId | STATUS_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
