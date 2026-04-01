---
id: DOC-OTHER-PVO-CandidateSelectProcessPVO
doc_type: system-doc
title: "CandidateSelectProcessPVO — PVO Cross-Module"
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
  - CandidateSelectProcessPVO
  - candidateselectprocesspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CandidateSelectProcessPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Candidate Select Process. Acessa as tabelas: IRC_LC_SETTING_ITEMS, IRC_PROCESSES_B, IRC_PROCESSES_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecProcessLifecycleAM.CandidateSelectProcessPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 30 | 3 | 3 | 14 | 47% |

---

## 🔗 Tabelas Relacionadas

- [[irc_lc_setting_items|IRC_LC_SETTING_ITEMS]] — 3 atributos (1 BICC)
- [[irc_processes_b|IRC_PROCESSES_B]] — 15 atributos (1 PKs, 8 BICC)
- [[irc_processes_tl|IRC_PROCESSES_TL]] — 12 atributos (2 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[irc_lc_setting_items|IRC_LC_SETTING_ITEMS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProcessTypeSettingItemPEOItemKeyName | ITEM_KEY_NAME | — | — |
| 2 | ProcessTypeSettingItemPEOSettingItemId | SETTING_ITEM_ID | — | — |
| 3 | ProcessTypeSettingItemPEOStringValue | STRING_VALUE | — | ✅ |

### [[irc_processes_b|IRC_PROCESSES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Code | CODE | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | IsActiveFlag | IS_ACTIVE_FLAG | — | — |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ModuleId | MODULE_ID | — | — |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | PhaseId | PHASE_ID | — | — |
| 11 | ProcessId | PROCESS_ID | 🔑 | ✅ |
| 12 | SeedDataSource | SEED_DATA_SOURCE | — | — |
| 13 | StatusCode | STATUS_CODE | — | ✅ |
| 14 | TypeCode | TYPE_CODE | — | ✅ |
| 15 | UsageCode | USAGE_CODE | — | — |

### [[irc_processes_tl|IRC_PROCESSES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy1 | CREATED_BY | — | — |
| 2 | CreationDate1 | CREATION_DATE | — | — |
| 3 | Description | DESCRIPTION | — | ✅ |
| 4 | Language1 | LANGUAGE | 🔑 | ✅ |
| 5 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 7 | LastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 8 | Name | NAME | — | ✅ |
| 9 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 10 | ProcessId1 | PROCESS_ID | 🔑 | ✅ |
| 11 | SeedDataSource1 | SEED_DATA_SOURCE | — | — |
| 12 | SourceLang1 | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
