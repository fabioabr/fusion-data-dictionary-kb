---
id: DOC-HCM-PVO-FeedbackRequestObjExtractPVO
doc_type: system-doc
title: "FeedbackRequestObjExtractPVO — PVO Human Capital Management"
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

Extrai objetos vinculados a solicitações de feedback de desempenho. Suporta rastreabilidade de sobre quem ou o que o feedback foi solicitado.

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

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
