---
id: DOC-PO-PVO-SubmissionQstnrsViewAllPVO
doc_type: system-doc
title: "SubmissionQstnrsViewAllPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - SubmissionQstnrsViewAllPVO
  - submissionqstnrsviewallpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SubmissionQstnrsViewAllPVO

## 📌 Visão Geral

Extrai visão consolidada de todos os questionários de submissão associados a requisições e ofertas de contratação. Permite análise completa de instrumentos de avaliação utilizados no processo seletivo.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecHiringRequisitionAM.SubmissionQstnrsViewAllPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 5 | 3 | 7 | 32% |

---

## 🔗 Tabelas Relacionadas

- [[hrq_questionnaires_b|HRQ_QUESTIONNAIRES_B]] — 4 atributos (1 BICC)
- [[irc_im_req_qstnrs|IRC_IM_REQ_QSTNRS]] — 10 atributos (3 PKs, 4 BICC)
- [[irc_offers|IRC_OFFERS]] — 1 atributos
- [[irc_requisitions_b|IRC_REQUISITIONS_B]] — 1 atributos
- [[irc_submissions|IRC_SUBMISSIONS]] — 6 atributos (2 BICC)

---

## ⚙️ Atributos

### [[hrq_questionnaires_b|HRQ_QUESTIONNAIRES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QuestionnaireBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | QuestionnaireBPEOMaxPossibleScore | MAX_POSSIBLE_SCORE | — | ✅ |
| 3 | QuestionnaireBPEOQstnrVersionNum | QSTNR_VERSION_NUM | — | — |
| 4 | QuestionnaireBPEOQuestionnaireId | QUESTIONNAIRE_ID | — | — |

### [[irc_im_req_qstnrs|IRC_IM_REQ_QSTNRS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QstnrVersionNum | QSTNR_VERSION_NUM | 🔑 | ✅ |
| 2 | QuestionnaireId | QUESTIONNAIRE_ID | 🔑 | ✅ |
| 3 | RequisitionId | REQUISITION_ID | 🔑 | ✅ |
| 4 | RequisitionQstnrPEOCreatedBy | CREATED_BY | — | — |
| 5 | RequisitionQstnrPEOCreationDate | CREATION_DATE | — | — |
| 6 | RequisitionQstnrPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | RequisitionQstnrPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | RequisitionQstnrPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | RequisitionQstnrPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | RequisitionQstnrPEOQstnrTypeCode | QSTNR_TYPE_CODE | — | — |

### [[irc_offers|IRC_OFFERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OffersPEOOfferId | OFFER_ID | — | — |

### [[irc_requisitions_b|IRC_REQUISITIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RequisitionBPEORequisitionId | REQUISITION_ID | — | — |

### [[irc_submissions|IRC_SUBMISSIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreationDate | CREATION_DATE | — | — |
| 2 | SubmissionPEOInternalFlag | INTERNAL_FLAG | — | — |
| 3 | SubmissionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 4 | SubmissionPEOPersonId | PERSON_ID | — | — |
| 5 | SubmissionPEOQstnrScore | QSTNR_SCORE | — | ✅ |
| 6 | SubmissionPEOSubmissionId | SUBMISSION_ID | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
