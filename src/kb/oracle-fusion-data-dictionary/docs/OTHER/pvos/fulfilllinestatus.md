---
id: DOC-OTHER-PVO-FulfillLineStatus
doc_type: system-doc
title: "FulfillLineStatus — PVO Cross-Module"
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
  - FulfillLineStatus
  - fulfilllinestatus
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FulfillLineStatus

## 📌 Visão Geral

View Object para extração BICC de dados de Fulfill Line Status. Acessa as tabelas: DOO_LINE_STATUSES, DOO_STATUSES_B, DOO_STATUSES_TL.

**Caminho:** `FscmTopModelAM.DooTopAM.FulfillLineStatus`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 3 | 2 | 12 | 57% |

---

## 🔗 Tabelas Relacionadas

- [[doo_line_statuses|DOO_LINE_STATUSES]] — 10 atributos (1 PKs, 6 BICC)
- [[doo_statuses_b|DOO_STATUSES_B]] — 1 atributos
- [[doo_statuses_tl|DOO_STATUSES_TL]] — 10 atributos (1 PKs, 6 BICC)

---

## ⚙️ Atributos

### [[doo_line_statuses|DOO_LINE_STATUSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FulfillLineStatusCreatedBy | CREATED_BY | — | ✅ |
| 2 | FulfillLineStatusCreationDate | CREATION_DATE | — | ✅ |
| 3 | FulfillLineStatusDefaultFlag | DEFAULT_FLAG | — | — |
| 4 | FulfillLineStatusLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | FulfillLineStatusLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | FulfillLineStatusLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | FulfillLineStatusObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | FulfillLineStatusOrchestrationApplicationId | ORCHESTRATION_APPLICATION_ID | — | — |
| 9 | FulfillLineStatusStatusCode | STATUS_CODE | — | ✅ |
| 10 | LineStatusId | LINE_STATUS_ID | 🔑 | ✅ |

### [[doo_statuses_b|DOO_STATUSES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | StatusStatusId | STATUS_ID | — | — |

### [[doo_statuses_tl|DOO_STATUSES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | StatusTranslationCreatedBy | CREATED_BY | — | ✅ |
| 2 | StatusTranslationCreationDate | CREATION_DATE | — | ✅ |
| 3 | StatusTranslationDisplayName | DISPLAY_NAME | — | ✅ |
| 4 | StatusTranslationLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | StatusTranslationLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 6 | StatusTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | StatusTranslationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | StatusTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | StatusTranslationSourceLang | SOURCE_LANG | — | ✅ |
| 10 | StatusTranslationStatusId | STATUS_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
