---
id: DOC-HCM-PVO-MessagesTLPVO
doc_type: system-doc
title: "MessagesTLPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
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

Disponibiliza traduções de mensagens do sistema (FND_MESSAGES) por aplicação e idioma. Utilizado para internacionalização de alertas, notificações e mensagens padronizadas do Oracle Fusion.

**Caminho:** `FscmTopModelAM.AnalyticsServiceAM.MessagesTLPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 18 | 1 | 5 | 7 | 39% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_messages_tl|FND_MESSAGES_TL]] — 18 atributos (5 PKs, 7 BICC)

---

## ⚙️ Atributos

### [[fnd_messages_tl|FND_MESSAGES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApplicationId | APPLICATION_ID | 🔑 | ✅ |
| 2 | CreatedBy | CREATED_BY | — | — |
| 3 | CreationDate | CREATION_DATE | — | — |
| 4 | EnterpriseId | ENTERPRISE_ID | 🔑 | ✅ |
| 5 | Language | LANGUAGE | 🔑 | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | MessageAdminAction | MESSAGE_ADMIN_ACTION | — | — |
| 10 | MessageAdminDetails | MESSAGE_ADMIN_DETAILS | — | — |
| 11 | MessageCause | MESSAGE_CAUSE | — | — |
| 12 | MessageName | MESSAGE_NAME | 🔑 | ✅ |
| 13 | MessageText | MESSAGE_TEXT | — | ✅ |
| 14 | MessageUserAction | MESSAGE_USER_ACTION | — | — |
| 15 | MessageUserDetails | MESSAGE_USER_DETAILS | — | — |
| 16 | SandboxId | SANDBOX_ID | 🔑 | ✅ |
| 17 | SeedDataSource | SEED_DATA_SOURCE | — | — |
| 18 | SourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
