---
id: DOC-GL-PVO-ActionsPVO
doc_type: system-doc
title: "ActionsPVO — PVO General Ledger"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - gl
  - data-dictionary
  - pvo
  - bicc
aliases:
  - ActionsPVO
  - actionspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ActionsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Actions. Acessa as tabelas: PER_ACTIONS_B, PER_ACTIONS_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.ActionAM.ActionsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 36 | 2 | 2 | 22 | 61% |

---

## 🔗 Tabelas Relacionadas

- [[per_actions_b|PER_ACTIONS_B]] — 23 atributos (1 PKs, 18 BICC)
- [[per_actions_tl|PER_ACTIONS_TL]] — 13 atributos (1 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[per_actions_b|PER_ACTIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionId | ACTION_ID | 🔑 | ✅ |
| 2 | ActionsPEOActInformation1 | ACT_INFORMATION1 | — | ✅ |
| 3 | ActionsPEOActInformation2 | ACT_INFORMATION2 | — | ✅ |
| 4 | ActionsPEOActionCode | ACTION_CODE | — | ✅ |
| 5 | ActionsPEOActionTypeCode | ACTION_TYPE_CODE | — | ✅ |
| 6 | ActionsPEOActionTypeId | ACTION_TYPE_ID | — | ✅ |
| 7 | ActionsPEOAllRoles | ALL_ROLES | — | ✅ |
| 8 | ActionsPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 9 | ActionsPEOCountry | COUNTRY | — | ✅ |
| 10 | ActionsPEOCreatedBy | CREATED_BY | — | ✅ |
| 11 | ActionsPEOCreationDate | CREATION_DATE | — | ✅ |
| 12 | ActionsPEODfltAsgStatusTypeId | DFLT_ASG_STATUS_TYPE_ID | — | ✅ |
| 13 | ActionsPEOEndDate | END_DATE | — | ✅ |
| 14 | ActionsPEOIsSystemAction | IS_SYSTEM_ACTION | — | ✅ |
| 15 | ActionsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | ActionsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 17 | ActionsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 18 | ActionsPEOModuleId | MODULE_ID | — | — |
| 19 | ActionsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | ActionsPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 21 | ActionsPEOSguid | SGUID | — | — |
| 22 | ActionsPEOStartDate | START_DATE | — | ✅ |
| 23 | ActionsPEOUsedInContract | USED_IN_CONTRACT | — | ✅ |

### [[per_actions_tl|PER_ACTIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionTranslationPEOActionId | ACTION_ID | — | — |
| 2 | ActionTranslationPEOActionName | ACTION_NAME | — | ✅ |
| 3 | ActionTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 4 | ActionTranslationPEOCreatedBy | CREATED_BY | — | — |
| 5 | ActionTranslationPEOCreationDate | CREATION_DATE | — | — |
| 6 | ActionTranslationPEODescription | DESCRIPTION | — | ✅ |
| 7 | ActionTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 8 | ActionTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | ActionTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | ActionTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | ActionTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | ActionTranslationPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 13 | ActionTranslationPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
