---
id: DOC-OTHER-PVO-QuestionnaireQuestionPVO
doc_type: system-doc
title: "QuestionnaireQuestionPVO — PVO Cross-Module"
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
  - QuestionnaireQuestionPVO
  - questionnairequestionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QuestionnaireQuestionPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Questionnaire Question. Acessa as tabelas: HRQ_EVAL_PTCPNT_QUESTIONS_V, HRQ_QSTNR_QUESTIONS, HRQ_QSTNR_SECTIONS_B (+5).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.QuestionnaireAM.QuestionnaireQuestionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 121 | 8 | 18 | 30 | 25% |

---

## 🔗 Tabelas Relacionadas

- [[hrq_eval_ptcpnt_questions_v|HRQ_EVAL_PTCPNT_QUESTIONS_V]] — 12 atributos (4 PKs, 4 BICC)
- [[hrq_qstnr_questions|HRQ_QSTNR_QUESTIONS]] — 17 atributos (2 PKs, 5 BICC)
- [[hrq_qstnr_sections_b|HRQ_QSTNR_SECTIONS_B]] — 17 atributos (2 PKs, 3 BICC)
- [[hrq_qstnr_sections_tl|HRQ_QSTNR_SECTIONS_TL]] — 13 atributos (3 PKs, 4 BICC)
- [[hrq_qstn_answers_b|HRQ_QSTN_ANSWERS_B]] — 3 atributos
- [[hrq_qstn_answers_tl|HRQ_QSTN_ANSWERS_TL]] — 5 atributos
- [[hrq_questions_b|HRQ_QUESTIONS_B]] — 37 atributos (3 PKs, 8 BICC)
- [[hrq_questions_tl|HRQ_QUESTIONS_TL]] — 17 atributos (4 PKs, 6 BICC)

---

## ⚙️ Atributos

### [[hrq_eval_ptcpnt_questions_v|HRQ_EVAL_PTCPNT_QUESTIONS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EvalParticipantQuestionPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | EvalParticipantQuestionPEOEvalRoleId | EVAL_ROLE_ID | — | — |
| 3 | EvalParticipantQuestionPEOEvalSectionId | EVAL_SECTION_ID | — | — |
| 4 | EvalParticipantQuestionPEOParticipantId | PARTICIPANT_ID | 🔑 | ✅ |
| 5 | EvalParticipantQuestionPEOParticipantType | PARTICIPANT_TYPE | — | — |
| 6 | EvalParticipantQuestionPEOPtcpntPersonId | PTCPNT_PERSON_ID | — | — |
| 7 | EvalParticipantQuestionPEOQstnrQuestionId | QSTNR_QUESTION_ID | 🔑 | ✅ |
| 8 | EvalParticipantQuestionPEOQstnrSectionId | QSTNR_SECTION_ID | — | — |
| 9 | EvalParticipantQuestionPEOQuestionnaireId | QUESTIONNAIRE_ID | — | — |
| 10 | EvalParticipantQuestionPEOSubjectCode | SUBJECT_CODE | — | — |
| 11 | EvalParticipantQuestionPEOSubjectId | SUBJECT_ID | 🔑 | ✅ |
| 12 | EvalParticipantQuestionPEOSubscriberId | SUBSCRIBER_ID | — | — |

### [[hrq_qstnr_questions|HRQ_QSTNR_QUESTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QuestionnaireQuestionPEOAdhocQstn | ADHOC_QSTN | — | ✅ |
| 2 | QuestionnaireQuestionPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 3 | QuestionnaireQuestionPEOCreatedBy | CREATED_BY | — | — |
| 4 | QuestionnaireQuestionPEOCreationDate | CREATION_DATE | — | — |
| 5 | QuestionnaireQuestionPEOKeepWithPrev | KEEP_WITH_PREV | — | — |
| 6 | QuestionnaireQuestionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | QuestionnaireQuestionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | QuestionnaireQuestionPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | QuestionnaireQuestionPEOMandatory | MANDATORY | — | ✅ |
| 10 | QuestionnaireQuestionPEOModuleId | MODULE_ID | — | — |
| 11 | QuestionnaireQuestionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | QuestionnaireQuestionPEOQstnVersionNum | QSTN_VERSION_NUM | — | — |
| 13 | QuestionnaireQuestionPEOQstnrQuestionId | QSTNR_QUESTION_ID | 🔑 | ✅ |
| 14 | QuestionnaireQuestionPEOQstnrSectionId | QSTNR_SECTION_ID | — | — |
| 15 | QuestionnaireQuestionPEOQuestionId | QUESTION_ID | — | — |
| 16 | QuestionnaireQuestionPEOResponseTypeId | RESPONSE_TYPE_ID | — | — |
| 17 | QuestionnaireQuestionPEOSeqNum | SEQ_NUM | — | — |

### [[hrq_qstnr_sections_b|HRQ_QSTNR_SECTIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QuestionnaireSectionBPEOAllowAdhoc | ALLOW_ADHOC | — | — |
| 2 | QuestionnaireSectionBPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 3 | QuestionnaireSectionBPEOCreatedBy | CREATED_BY | — | — |
| 4 | QuestionnaireSectionBPEOCreationDate | CREATION_DATE | — | — |
| 5 | QuestionnaireSectionBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | QuestionnaireSectionBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | QuestionnaireSectionBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | QuestionnaireSectionBPEOMandatory | MANDATORY | — | — |
| 9 | QuestionnaireSectionBPEOModuleId | MODULE_ID | — | — |
| 10 | QuestionnaireSectionBPEONewPage | NEW_PAGE | — | — |
| 11 | QuestionnaireSectionBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | QuestionnaireSectionBPEOQstnrSectionId | QSTNR_SECTION_ID | 🔑 | ✅ |
| 13 | QuestionnaireSectionBPEOQstnrVersionNum | QSTNR_VERSION_NUM | — | — |
| 14 | QuestionnaireSectionBPEOQuestionOrder | QUESTION_ORDER | — | — |
| 15 | QuestionnaireSectionBPEOQuestionnaireId | QUESTIONNAIRE_ID | — | — |
| 16 | QuestionnaireSectionBPEOResponseOrder | RESPONSE_ORDER | — | — |
| 17 | QuestionnaireSectionBPEOSectionSeqNum | SECTION_SEQ_NUM | — | — |

### [[hrq_qstnr_sections_tl|HRQ_QSTNR_SECTIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QuestionSectionTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | QuestionSectionTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 3 | QuestionSectionTranslationPEOName | NAME | — | — |
| 4 | QuestionSectionTranslationPEOQstnrSectionId | QSTNR_SECTION_ID | 🔑 | ✅ |
| 5 | QuestionnaireSectionTranslationPEOCreatedBy | CREATED_BY | — | — |
| 6 | QuestionnaireSectionTranslationPEOCreationDate | CREATION_DATE | — | — |
| 7 | QuestionnaireSectionTranslationPEODescription | DESCRIPTION | — | — |
| 8 | QuestionnaireSectionTranslationPEOIntroText | INTRO_TEXT | — | — |
| 9 | QuestionnaireSectionTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | QuestionnaireSectionTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | QuestionnaireSectionTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | QuestionnaireSectionTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | QuestionnaireSectionTranslationPEOSourceLang | SOURCE_LANG | — | — |

### [[hrq_qstn_answers_b|HRQ_QSTN_ANSWERS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AnswerCode | ANSWER_CODE | — | — |
| 2 | ConditionQstnAnswerBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | ConditionQstnAnswerBPEOQstnAnswerId | QSTN_ANSWER_ID | — | — |

### [[hrq_qstn_answers_tl|HRQ_QSTN_ANSWERS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConditionQstnAnswerTLPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ConditionQstnAnswerTLPEOLanguage | LANGUAGE | — | — |
| 3 | ConditionQstnAnswerTLPEOLongText | LONG_TEXT | — | — |
| 4 | ConditionQstnAnswerTLPEOQstnAnswerId | QSTN_ANSWER_ID | — | — |
| 5 | ConditionQstnAnswerTLPEOShortText | SHORT_TEXT | — | — |

### [[hrq_questions_b|HRQ_QUESTIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConditionQuestionBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ConditionQuestionBPEOQstnVersionNum | QSTN_VERSION_NUM | — | — |
| 3 | ConditionQuestionBPEOQuestionCode | QUESTION_CODE | — | — |
| 4 | ConditionQuestionBPEOQuestionId | QUESTION_ID | — | — |
| 5 | QuestionBPEOAdhocFlag | ADHOC_FLAG | — | — |
| 6 | QuestionBPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 7 | QuestionBPEOCategoryId | CATEGORY_ID | — | — |
| 8 | QuestionBPEOConditionAnswerId | CONDITION_ANSWER_ID | — | — |
| 9 | QuestionBPEOConditionDisplay | CONDITION_DISPLAY | — | — |
| 10 | QuestionBPEOConditionQstnVersionNum | CONDITION_QSTN_VERSION_NUM | — | — |
| 11 | QuestionBPEOConditionQuestionId | CONDITION_QUESTION_ID | — | — |
| 12 | QuestionBPEOOwner | OWNER | — | ✅ |
| 13 | QuestionBPEOPrivacyFlag | PRIVACY_FLAG | — | ✅ |
| 14 | QuestionBPEOQstnVersionNum | QSTN_VERSION_NUM | 🔑 | ✅ |
| 15 | QuestionBPEOQuestionId | QUESTION_ID | 🔑 | ✅ |
| 16 | QuestionBPEOQuestionType | QUESTION_TYPE | — | ✅ |
| 17 | QuestionBPEORatingModelId | RATING_MODEL_ID | — | — |
| 18 | QuestionBPEOStatus | STATUS | — | ✅ |
| 19 | QuestionBPEOSubscriberId | SUBSCRIBER_ID | — | — |
| 20 | QuestionnaireBPEOAttachmentAllowed | ATTACHMENT_ALLOWED | — | — |
| 21 | QuestionnaireBPEOCreatedBy | CREATED_BY | — | — |
| 22 | QuestionnaireBPEOCreationDate | CREATION_DATE | — | — |
| 23 | QuestionnaireBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 24 | QuestionnaireBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 25 | QuestionnaireBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 26 | QuestionnaireBPEOLatestVersion | LATEST_VERSION | — | — |
| 27 | QuestionnaireBPEOMaxLength | MAX_LENGTH | — | — |
| 28 | QuestionnaireBPEOMaxSelections | MAX_SELECTIONS | — | — |
| 29 | QuestionnaireBPEOMinLength | MIN_LENGTH | — | — |
| 30 | QuestionnaireBPEOMinSelections | MIN_SELECTIONS | — | — |
| 31 | QuestionnaireBPEOModuleId | MODULE_ID | — | — |
| 32 | QuestionnaireBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 33 | QuestionnaireBPEOOverrideDescFlag | OVERRIDE_DESC_FLAG | — | — |
| 34 | QuestionnaireBPEOQuestionCode | QUESTION_CODE | — | — |
| 35 | QuestionnaireBPEOResponseTypeId | RESPONSE_TYPE_ID | — | — |
| 36 | QuestionnaireBPEOUpdateAllowed | UPDATE_ALLOWED | — | — |
| 37 | QuestionnaireBPEOVersionDescription | VERSION_DESCRIPTION | — | — |

### [[hrq_questions_tl|HRQ_QUESTIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConditionQuestionTLPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ConditionQuestionTLPEOLanguage | LANGUAGE | — | — |
| 3 | ConditionQuestionTLPEOQstnVersionNum | QSTN_VERSION_NUM | — | — |
| 4 | ConditionQuestionTLPEOQuestionId | QUESTION_ID | — | — |
| 5 | ConditionQuestionTLPEOQuestionText | QUESTION_TEXT | — | — |
| 6 | QuestionTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 7 | QuestionTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 8 | QuestionTranslationPEOQstnVersionNum | QSTN_VERSION_NUM | 🔑 | ✅ |
| 9 | QuestionTranslationPEOQuestionId | QUESTION_ID | 🔑 | ✅ |
| 10 | QuestionTranslationPEOQuestionText | QUESTION_TEXT | — | ✅ |
| 11 | QuestionnaireTranslationPEOCreatedBy | CREATED_BY | — | — |
| 12 | QuestionnaireTranslationPEOCreationDate | CREATION_DATE | — | — |
| 13 | QuestionnaireTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | QuestionnaireTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | QuestionnaireTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 16 | QuestionnaireTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | QuestionnaireTranslationPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
