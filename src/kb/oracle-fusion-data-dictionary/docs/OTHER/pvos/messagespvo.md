---
id: DOC-OTHER-PVO-MessagesPVO
doc_type: system-doc
title: "MessagesPVO — PVO Cross-Module"
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
  - MessagesPVO
  - messagespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MessagesPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Messages. Acessa as tabelas: FND_MESSAGES_B, FND_MESSAGES_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.AnalyticsExtractServiceAM.MessagesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 33 | 2 | 5 | 33 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_messages_b|FND_MESSAGES_B]] — 15 atributos (15 BICC)
- [[fnd_messages_tl|FND_MESSAGES_TL]] — 18 atributos (5 PKs, 18 BICC)

---

## ⚙️ Atributos

### [[fnd_messages_b|FND_MESSAGES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApplicationId1 | APPLICATION_ID | — | ✅ |
| 2 | ChangeSinceLastRefresh | CHANGE_SINCE_LAST_REFRESH | — | ✅ |
| 3 | Context | CONTEXT | — | ✅ |
| 4 | CreatedBy1 | CREATED_BY | — | ✅ |
| 5 | CreationDate1 | CREATION_DATE | — | ✅ |
| 6 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy1 | LAST_UPDATED_BY | — | ✅ |
| 9 | LoggableAlertable | LOGGABLE_ALERTABLE | — | ✅ |
| 10 | MessageCategory | MESSAGE_CATEGORY | — | ✅ |
| 11 | MessageName1 | MESSAGE_NAME | — | ✅ |
| 12 | MessageNumber | MESSAGE_NUMBER | — | ✅ |
| 13 | MessageSeverity | MESSAGE_SEVERITY | — | ✅ |
| 14 | ModuleId | MODULE_ID | — | ✅ |
| 15 | Type | TYPE | — | ✅ |

### [[fnd_messages_tl|FND_MESSAGES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApplicationId | APPLICATION_ID | 🔑 | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | EnterpriseId | ENTERPRISE_ID | 🔑 | ✅ |
| 5 | Language | LANGUAGE | 🔑 | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | MessageAdminAction | MESSAGE_ADMIN_ACTION | — | ✅ |
| 10 | MessageAdminDetails | MESSAGE_ADMIN_DETAILS | — | ✅ |
| 11 | MessageCause | MESSAGE_CAUSE | — | ✅ |
| 12 | MessageName | MESSAGE_NAME | 🔑 | ✅ |
| 13 | MessageText | MESSAGE_TEXT | — | ✅ |
| 14 | MessageUserAction | MESSAGE_USER_ACTION | — | ✅ |
| 15 | MessageUserDetails | MESSAGE_USER_DETAILS | — | ✅ |
| 16 | SandboxId | SANDBOX_ID | 🔑 | ✅ |
| 17 | SeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 18 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
