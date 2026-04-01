---
id: DOC-OTHER-PVO-QuestionnaireQuestionResponseListPVO
doc_type: system-doc
title: "QuestionnaireQuestionResponseListPVO — PVO Cross-Module"
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
  - QuestionnaireQuestionResponseListPVO
  - questionnairequestionresponselistpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QuestionnaireQuestionResponseListPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Questionnaire Question Response List. Acessa as tabelas: HRQ_QSTN_ANSWERS_B, HRQ_QSTN_ANSWERS_TL, HRQ_QUESTIONNAIRES_B (+1).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.QuestionnaireAM.QuestionnaireQuestionResponseListPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 4 | 5 | 7 | 32% |

---

## 🔗 Tabelas Relacionadas

- [[hrq_qstn_answers_b|HRQ_QSTN_ANSWERS_B]] — 8 atributos (2 PKs, 2 BICC)
- [[hrq_qstn_answers_tl|HRQ_QSTN_ANSWERS_TL]] — 5 atributos (3 PKs, 5 BICC)
- [[hrq_questionnaires_b|HRQ_QUESTIONNAIRES_B]] — 4 atributos
- [[hrq_questionnaires_tl|HRQ_QUESTIONNAIRES_TL]] — 5 atributos

---

## ⚙️ Atributos

### [[hrq_qstn_answers_b|HRQ_QSTN_ANSWERS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AnswerCode | ANSWER_CODE | — | — |
| 2 | QuestionAnswerBPEOAddlQstnrId | ADDL_QSTNR_ID | — | — |
| 3 | QuestionAnswerBPEOAddlQstnrVersionNum | ADDL_QSTNR_VERSION_NUM | — | — |
| 4 | QuestionAnswerBPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 5 | QuestionAnswerBPEOQstnAnswerId | QSTN_ANSWER_ID | 🔑 | ✅ |
| 6 | QuestionAnswerBPEOQuestionId | QUESTION_ID | — | — |
| 7 | QuestionAnswerBPEORatingLevelId | RATING_LEVEL_ID | — | — |
| 8 | QuestionAnswerBPEOSeqNum | SEQ_NUM | — | — |

### [[hrq_qstn_answers_tl|HRQ_QSTN_ANSWERS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QuestionAnswerTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | QuestionAnswerTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 3 | QuestionAnswerTranslationPEOLongText | LONG_TEXT | — | ✅ |
| 4 | QuestionAnswerTranslationPEOQstnAnswerId | QSTN_ANSWER_ID | 🔑 | ✅ |
| 5 | QuestionAnswerTranslationPEOShortText | SHORT_TEXT | — | ✅ |

### [[hrq_questionnaires_b|HRQ_QUESTIONNAIRES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdditionalQuestionnaireBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | AdditionalQuestionnaireBPEOQstnrVersionNum | QSTNR_VERSION_NUM | — | — |
| 3 | AdditionalQuestionnaireBPEOQuestionnaireCode | QUESTIONNAIRE_CODE | — | — |
| 4 | AdditionalQuestionnaireBPEOQuestionnaireId | QUESTIONNAIRE_ID | — | — |

### [[hrq_questionnaires_tl|HRQ_QUESTIONNAIRES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdditionalQuestionnaireTLPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | AdditionalQuestionnaireTLPEOLanguage | LANGUAGE | — | — |
| 3 | AdditionalQuestionnaireTLPEOName | NAME | — | — |
| 4 | AdditionalQuestionnaireTLPEOQstnrVersionNum | QSTNR_VERSION_NUM | — | — |
| 5 | AdditionalQuestionnaireTLPEOQuestionnaireId | QUESTIONNAIRE_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
