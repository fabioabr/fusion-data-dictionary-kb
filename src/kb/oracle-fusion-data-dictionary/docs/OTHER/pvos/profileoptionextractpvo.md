---
id: DOC-OTHER-PVO-ProfileOptionExtractPVO
doc_type: system-doc
title: "ProfileOptionExtractPVO — PVO Cross-Module"
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
  - ProfileOptionExtractPVO
  - profileoptionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProfileOptionExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Profile Option Extract. Acessa as tabelas: FND_PROFILE_OPTIONS_B.

**Caminho:** `FscmTopModelAM.FinExtractAM.AnalyticsExtractServiceAM.ProfileOptionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 1 | 2 | 16 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_profile_options_b|FND_PROFILE_OPTIONS_B]] — 16 atributos (2 PKs, 16 BICC)

---

## ⚙️ Atributos

### [[fnd_profile_options_b|FND_PROFILE_OPTIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApplicationId | APPLICATION_ID | 🔑 | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | EndDateActive | END_DATE_ACTIVE | — | ✅ |
| 5 | HierarchyName | HIERARCHY_NAME | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ModuleId | MODULE_ID | — | ✅ |
| 10 | ProfileOptionId | PROFILE_OPTION_ID | 🔑 | ✅ |
| 11 | ProfileOptionName | PROFILE_OPTION_NAME | — | ✅ |
| 12 | SeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 13 | SqlValidation | SQL_VALIDATION | — | ✅ |
| 14 | StartDateActive | START_DATE_ACTIVE | — | ✅ |
| 15 | UserEnabledFlag | USER_ENABLED_FLAG | — | ✅ |
| 16 | UserUpdateableFlag | USER_UPDATEABLE_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
