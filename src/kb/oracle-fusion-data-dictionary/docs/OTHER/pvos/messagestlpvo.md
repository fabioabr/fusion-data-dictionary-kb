---
id: DOC-OTHER-PVO-MessagesTLPVO
doc_type: system-doc
title: "MessagesTLPVO — PVO Cross-Module"
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
  - MessagesTLPVO
  - messagestlpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MessagesTLPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Messages TL. Acessa as tabelas: FND_MESSAGES_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.AnalyticsExtractServiceAM.MessagesTLPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 18 | 1 | 0 | 18 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_messages_tl|FND_MESSAGES_TL]] — 18 atributos (18 BICC)

---

## ⚙️ Atributos

### [[fnd_messages_tl|FND_MESSAGES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApplicationId | APPLICATION_ID | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | EnterpriseId | ENTERPRISE_ID | — | ✅ |
| 5 | Language | LANGUAGE | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | MessageAdminAction | MESSAGE_ADMIN_ACTION | — | ✅ |
| 10 | MessageAdminDetails | MESSAGE_ADMIN_DETAILS | — | ✅ |
| 11 | MessageCause | MESSAGE_CAUSE | — | ✅ |
| 12 | MessageName | MESSAGE_NAME | — | ✅ |
| 13 | MessageText | MESSAGE_TEXT | — | ✅ |
| 14 | MessageUserAction | MESSAGE_USER_ACTION | — | ✅ |
| 15 | MessageUserDetails | MESSAGE_USER_DETAILS | — | ✅ |
| 16 | SandboxId | SANDBOX_ID | — | ✅ |
| 17 | SeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 18 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
