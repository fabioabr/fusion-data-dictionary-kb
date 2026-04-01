---
id: DOC-OTHER-PVO-TimeEntryMessagePVO
doc_type: system-doc
title: "TimeEntryMessagePVO — PVO Cross-Module"
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
  - TimeEntryMessagePVO
  - timeentrymessagepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TimeEntryMessagePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Time Entry Message. Acessa as tabelas: HWM_TE_MESSAGES_V.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.TimeRepositoryAM.TimeEntryMessagePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 3 | 11 | 85% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_te_messages_v|HWM_TE_MESSAGES_V]] — 13 atributos (3 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[hwm_te_messages_v|HWM_TE_MESSAGES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimeEntryMessagePEOApplicationId | APPLICATION_ID | 🔑 | ✅ |
| 2 | TimeEntryMessagePEOApplicationShortName | APPLICATION_SHORT_NAME | — | ✅ |
| 3 | TimeEntryMessagePEOContext | CONTEXT | — | — |
| 4 | TimeEntryMessagePEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | TimeEntryMessagePEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | TimeEntryMessagePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | TimeEntryMessagePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | TimeEntryMessagePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | TimeEntryMessagePEOMessageLevel | MESSAGE_LEVEL | 🔑 | ✅ |
| 10 | TimeEntryMessagePEOMessageName | MESSAGE_NAME | 🔑 | ✅ |
| 11 | TimeEntryMessagePEOMessageNumber | MESSAGE_NUMBER | — | ✅ |
| 12 | TimeEntryMessagePEOMessageText | MESSAGE_TEXT | — | ✅ |
| 13 | TimeEntryMessagePEOMessageUserDetails | MESSAGE_USER_DETAILS | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
