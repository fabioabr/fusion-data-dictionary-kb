---
id: DOC-OTHER-PVO-SurveyRespCommentsPVO
doc_type: system-doc
title: "SurveyRespCommentsPVO — PVO Cross-Module"
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
  - SurveyRespCommentsPVO
  - surveyrespcommentspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SurveyRespCommentsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Survey Resp Comments. Acessa as tabelas: GRC_SUV_RESP_COMMENTS.

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.SurveyRespCommentsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 2 | 4 | 44% |

---

## 🔗 Tabelas Relacionadas

- [[grc_suv_resp_comments|GRC_SUV_RESP_COMMENTS]] — 9 atributos (2 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[grc_suv_resp_comments|GRC_SUV_RESP_COMMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SurveyRespCommentsPEOCreatedBy | CREATED_BY | — | — |
| 2 | SurveyRespCommentsPEOCreationDate | CREATION_DATE | — | — |
| 3 | SurveyRespCommentsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | SurveyRespCommentsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 5 | SurveyRespCommentsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 6 | SurveyRespCommentsPEOParticipantId | PARTICIPANT_ID | 🔑 | ✅ |
| 7 | SurveyRespCommentsPEOQuestionId | QUESTION_ID | 🔑 | ✅ |
| 8 | SurveyRespCommentsPEOResponseComment | RESPONSE_COMMENT | — | ✅ |
| 9 | SurveyRespCommentsPEORevisionDate | REVISION_DATE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
