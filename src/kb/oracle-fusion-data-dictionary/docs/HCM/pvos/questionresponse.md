---
id: DOC-HCM-PVO-QuestionResponse
doc_type: system-doc
title: "QuestionResponse — PVO Human Capital Management"
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
  - QuestionResponse
  - questionresponse
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QuestionResponse

## 📌 Visão Geral

Disponibiliza respostas individuais a perguntas para carga BICC. Contém texto, lista de respostas e tipo de resposta para análise de questionários.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.QuestionnaireBiccExtractAM.QuestionResponse`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 17 | 1 | 1 | 17 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hrq_qstn_responses|HRQ_QSTN_RESPONSES]] — 17 atributos (1 PKs, 17 BICC)

---

## ⚙️ Atributos

### [[hrq_qstn_responses|HRQ_QSTN_RESPONSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AnswerClob | ANSWER_CLOB | — | ✅ |
| 2 | AnswerList | ANSWER_LIST | — | ✅ |
| 3 | AnswerText | ANSWER_TEXT | — | ✅ |
| 4 | BusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 5 | ChoiceList | CHOICE_LIST | — | ✅ |
| 6 | CreatedBy | CREATED_BY | — | ✅ |
| 7 | CreationDate | CREATION_DATE | — | ✅ |
| 8 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | QstnAnswerId | QSTN_ANSWER_ID | — | ✅ |
| 13 | QstnResponseId | QSTN_RESPONSE_ID | 🔑 | ✅ |
| 14 | QstnrQuestionId | QSTNR_QUESTION_ID | — | ✅ |
| 15 | QstnrResponseId | QSTNR_RESPONSE_ID | — | ✅ |
| 16 | Score | SCORE | — | ✅ |
| 17 | SubQuestionId | SUB_QUESTION_ID | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
