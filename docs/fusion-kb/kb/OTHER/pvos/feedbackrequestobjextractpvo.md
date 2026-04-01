---
id: DOC-OTHER-PVO-FeedbackRequestObjExtractPVO
doc_type: system-doc
title: "FeedbackRequestObjExtractPVO — PVO Cross-Module"
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
  - FeedbackRequestObjExtractPVO
  - feedbackrequestobjextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FeedbackRequestObjExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Feedback Request Obj Extract. Acessa as tabelas: HRA_FEEDBACK_REQUEST_OBJECTS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.PerformanceBiccExtractAM.FeedbackRequestObjExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 1 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hra_feedback_request_objects|HRA_FEEDBACK_REQUEST_OBJECTS]] — 13 atributos (1 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[hra_feedback_request_objects|HRA_FEEDBACK_REQUEST_OBJECTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FeedbackRequestObjPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 2 | FeedbackRequestObjPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | FeedbackRequestObjPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | FeedbackRequestObjPEOFeedbackReqId | FEEDBACK_REQ_ID | — | ✅ |
| 5 | FeedbackRequestObjPEOFeedbackReqObjId | FEEDBACK_REQ_OBJ_ID | 🔑 | ✅ |
| 6 | FeedbackRequestObjPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | FeedbackRequestObjPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | FeedbackRequestObjPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | FeedbackRequestObjPEOObjectId | OBJECT_ID | — | ✅ |
| 10 | FeedbackRequestObjPEOObjectReferenceDescription | OBJECT_REFERENCE_DESCRIPTION | — | ✅ |
| 11 | FeedbackRequestObjPEOObjectReferenceName | OBJECT_REFERENCE_NAME | — | ✅ |
| 12 | FeedbackRequestObjPEOObjectType | OBJECT_TYPE | — | ✅ |
| 13 | FeedbackRequestObjPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
