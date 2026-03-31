---
id: DOC-OTHER-PVO-ChangeStatusesTranslationExtractPVO
doc_type: system-doc
title: "ChangeStatusesTranslationExtractPVO — PVO Cross-Module"
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
  - ChangeStatusesTranslationExtractPVO
  - changestatusestranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ChangeStatusesTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Change Statuses Translation Extract. Acessa as tabelas: EGO_CHANGE_STATUSES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.EgoBiccExtractAM.ChangeStatusesTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 2 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ego_change_statuses_tl|EGO_CHANGE_STATUSES_TL]] — 12 atributos (2 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[ego_change_statuses_tl|EGO_CHANGE_STATUSES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EgoChangeStatusesTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | EgoChangeStatusesTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | EgoChangeStatusesTLPEODescription | DESCRIPTION | — | ✅ |
| 4 | EgoChangeStatusesTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | EgoChangeStatusesTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | EgoChangeStatusesTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | EgoChangeStatusesTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | EgoChangeStatusesTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | EgoChangeStatusesTLPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 10 | EgoChangeStatusesTLPEOSourceLang | SOURCE_LANG | — | ✅ |
| 11 | EgoChangeStatusesTLPEOStatusCode | STATUS_CODE | 🔑 | ✅ |
| 12 | EgoChangeStatusesTLPEOStatusName | STATUS_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
