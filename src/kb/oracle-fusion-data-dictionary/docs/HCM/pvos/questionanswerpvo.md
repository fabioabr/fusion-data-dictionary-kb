---
id: DOC-HCM-PVO-QuestionAnswerPVO
doc_type: system-doc
title: "QuestionAnswerPVO — PVO Human Capital Management"
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
  - QuestionAnswerPVO
  - questionanswerpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QuestionAnswerPVO

## 📌 Visão Geral

Extrai respostas de perguntas em questionários com pontuação e sequência. Suporta análise de resultados de avaliações, pesquisas e questionários de RH.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.QuestionnaireLibraryAM.QuestionAnswerPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 43 | 4 | 2 | 12 | 28% |

---

## 🔗 Tabelas Relacionadas

- [[hrq_qstn_answers_b|HRQ_QSTN_ANSWERS_B]] — 20 atributos (2 PKs, 5 BICC)
- [[hrq_qstn_answers_tl|HRQ_QSTN_ANSWERS_TL]] — 14 atributos (7 BICC)
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
| 5 | QuestionAnswerBPEOCorrectFlag | CORRECT_FLAG | — | — |
| 6 | QuestionAnswerBPEOCreatedBy | CREATED_BY | — | — |
| 7 | QuestionAnswerBPEOCreationDate | CREATION_DATE | — | — |
| 8 | QuestionAnswerBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | QuestionAnswerBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | QuestionAnswerBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | QuestionAnswerBPEOModuleId | MODULE_ID | — | — |
| 12 | QuestionAnswerBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | QuestionAnswerBPEOQstnAnswerId | QSTN_ANSWER_ID | 🔑 | ✅ |
| 14 | QuestionAnswerBPEOQstnVersionNum | QSTN_VERSION_NUM | — | — |
| 15 | QuestionAnswerBPEOQuestionId | QUESTION_ID | — | — |
| 16 | QuestionAnswerBPEORatingLevelId | RATING_LEVEL_ID | — | — |
| 17 | QuestionAnswerBPEOScore | SCORE | — | ✅ |
| 18 | QuestionAnswerBPEOScoreWeight | SCORE_WEIGHT | — | — |
| 19 | QuestionAnswerBPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 20 | QuestionAnswerBPEOSeqNum | SEQ_NUM | — | ✅ |

### [[hrq_qstn_answers_tl|HRQ_QSTN_ANSWERS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QuestionAnswerTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 2 | QuestionAnswerTranslationPEOCreatedBy | CREATED_BY | — | — |
| 3 | QuestionAnswerTranslationPEOCreationDate | CREATION_DATE | — | — |
| 4 | QuestionAnswerTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 5 | QuestionAnswerTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | QuestionAnswerTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | QuestionAnswerTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | QuestionAnswerTranslationPEOLongText | LONG_TEXT | — | ✅ |
| 9 | QuestionAnswerTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | QuestionAnswerTranslationPEOQstnAnswerId | QSTN_ANSWER_ID | — | ✅ |
| 11 | QuestionAnswerTranslationPEOResponseFeedback | RESPONSE_FEEDBACK | — | ✅ |
| 12 | QuestionAnswerTranslationPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 13 | QuestionAnswerTranslationPEOShortText | SHORT_TEXT | — | ✅ |
| 14 | QuestionAnswerTranslationPEOSourceLang | SOURCE_LANG | — | — |

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

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
