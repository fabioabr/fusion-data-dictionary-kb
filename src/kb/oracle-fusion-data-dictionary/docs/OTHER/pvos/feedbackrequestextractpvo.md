---
id: DOC-OTHER-PVO-FeedbackRequestExtractPVO
doc_type: system-doc
title: "FeedbackRequestExtractPVO — PVO Cross-Module"
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
  - FeedbackRequestExtractPVO
  - feedbackrequestextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FeedbackRequestExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Feedback Request Extract. Acessa as tabelas: HRA_FEEDBACK_REQUEST.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.PerformanceBiccExtractAM.FeedbackRequestExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 17 | 1 | 2 | 17 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hra_feedback_request|HRA_FEEDBACK_REQUEST]] — 17 atributos (2 PKs, 17 BICC)

---

## ⚙️ Atributos

### [[hra_feedback_request|HRA_FEEDBACK_REQUEST]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | DueDate | DUE_DATE | — | ✅ |
| 5 | DueDateAlertSent | DUE_DATE_ALERT_SENT | — | ✅ |
| 6 | FeedbackReqId | FEEDBACK_REQ_ID | 🔑 | ✅ |
| 7 | FeedbackReqTmplId | FEEDBACK_REQ_TMPL_ID | — | ✅ |
| 8 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | MessageText | MESSAGE_TEXT | — | ✅ |
| 12 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | ParticipantPersonId | PARTICIPANT_PERSON_ID | — | ✅ |
| 14 | RequestedByPersonId | REQUESTED_BY_PERSON_ID | — | ✅ |
| 15 | RequestedForPersonId | REQUESTED_FOR_PERSON_ID | — | ✅ |
| 16 | ShareWithMgrFlag | SHARE_WITH_MGR_FLAG | — | ✅ |
| 17 | ShareWithWkrFlag | SHARE_WITH_WKR_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
