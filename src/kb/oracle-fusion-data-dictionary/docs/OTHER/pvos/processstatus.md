---
id: DOC-OTHER-PVO-ProcessStatus
doc_type: system-doc
title: "ProcessStatus — PVO Cross-Module"
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
  - ProcessStatus
  - processstatus
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProcessStatus

## 📌 Visão Geral

View Object para extração BICC de dados de Process Status. Acessa as tabelas: DOO_STATUSES_B, DOO_STATUSES_TL.

**Caminho:** `FscmTopModelAM.DooTopAM.ProcessStatus`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 2 | 2 | 6 | 50% |

---

## 🔗 Tabelas Relacionadas

- [[doo_statuses_b|DOO_STATUSES_B]] — 8 atributos (1 PKs, 4 BICC)
- [[doo_statuses_tl|DOO_STATUSES_TL]] — 4 atributos (1 PKs, 2 BICC)

---

## ⚙️ Atributos

### [[doo_statuses_b|DOO_STATUSES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | StatusCreatedBy | CREATED_BY | — | — |
| 2 | StatusCreationDate | CREATION_DATE | — | ✅ |
| 3 | StatusId | STATUS_ID | 🔑 | ✅ |
| 4 | StatusLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | StatusLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | StatusLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | StatusSeededFlag | SEEDED_FLAG | — | — |
| 8 | StatusStatusCode | STATUS_CODE | — | ✅ |

### [[doo_statuses_tl|DOO_STATUSES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | StatusTranslationDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | StatusTranslationLanguage | LANGUAGE | 🔑 | ✅ |
| 3 | StatusTranslationSourceLang | SOURCE_LANG | — | — |
| 4 | StatusTranslationStatusId | STATUS_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
