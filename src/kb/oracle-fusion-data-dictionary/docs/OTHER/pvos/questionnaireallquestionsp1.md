---
id: DOC-OTHER-PVO-QuestionnaireAllQuestionsP1
doc_type: system-doc
title: "QuestionnaireAllQuestionsP1 — PVO Cross-Module"
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
  - QuestionnaireAllQuestionsP1
  - questionnaireallquestionsp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QuestionnaireAllQuestionsP1

## 📌 Visão Geral

View Object para extração BICC de dados de Questionnaire All Questions P1. Acessa as tabelas: HRQ_QSTNR_QUESTIONS, HRQ_QSTNR_SECTIONS_B, HRQ_QSTNR_SECTIONS_TL (+5).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.QuestionnaireLibraryAM.QuestionnaireAllQuestionsP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 132 | 8 | 3 | 30 | 23% |

---

## 🔗 Tabelas Relacionadas

- [[hrq_qstnr_questions|HRQ_QSTNR_QUESTIONS]] — 12 atributos (4 BICC)
- [[hrq_qstnr_sections_b|HRQ_QSTNR_SECTIONS_B]] — 11 atributos (3 BICC)
- [[hrq_qstnr_sections_tl|HRQ_QSTNR_SECTIONS_TL]] — 7 atributos (3 BICC)
- [[hrq_qstn_answers_b|HRQ_QSTN_ANSWERS_B]] — 23 atributos (4 BICC)
- [[hrq_qstn_answers_tl|HRQ_QSTN_ANSWERS_TL]] — 19 atributos (5 BICC)
- [[hrq_questionnaires_b|HRQ_QUESTIONNAIRES_B]] — 4 atributos (3 PKs, 3 BICC)
- [[hrq_questions_b|HRQ_QUESTIONS_B]] — 43 atributos (7 BICC)
- [[hrq_questions_tl|HRQ_QUESTIONS_TL]] — 13 atributos (1 BICC)

---

## ⚙️ Atributos

### [[hrq_qstnr_questions|HRQ_QSTNR_QUESTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QuestionnaireQuestionPEOAdhocQstn | ADHOC_QSTN | — | — |
| 2 | QuestionnaireQuestionPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | QuestionnaireQuestionPEOLockQuestionFlag | LOCK_QUESTION_FLAG | — | — |
| 4 | QuestionnaireQuestionPEOMandatory | MANDATORY | — | ✅ |
| 5 | QuestionnaireQuestionPEOMaxPossibleScore | MAX_POSSIBLE_SCORE | — | — |
| 6 | QuestionnaireQuestionPEOMaxThresholdScore | MAX_THRESHOLD_SCORE | — | ✅ |
| 7 | QuestionnaireQuestionPEOMinThresholdScore | MIN_THRESHOLD_SCORE | — | ✅ |
| 8 | QuestionnaireQuestionPEOQstnVersionNum | QSTN_VERSION_NUM | — | — |
| 9 | QuestionnaireQuestionPEOQstnrQuestionId | QSTNR_QUESTION_ID | — | — |
| 10 | QuestionnaireQuestionPEOQuestionId | QUESTION_ID | — | — |
| 11 | QuestionnaireQuestionPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 12 | QuestionnaireQuestionPEOSeqNum | SEQ_NUM | — | ✅ |

### [[hrq_qstnr_sections_b|HRQ_QSTNR_SECTIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QuestionnaireSectionBPEOAllowAdhoc | ALLOW_ADHOC | — | — |
| 2 | QuestionnaireSectionBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | QuestionnaireSectionBPEOMandatory | MANDATORY | — | ✅ |
| 4 | QuestionnaireSectionBPEOModuleId | MODULE_ID | — | — |
| 5 | QuestionnaireSectionBPEONewPage | NEW_PAGE | — | — |
| 6 | QuestionnaireSectionBPEOQstnrSectionId | QSTNR_SECTION_ID | — | — |
| 7 | QuestionnaireSectionBPEOQstnrVersionNum | QSTNR_VERSION_NUM | — | — |
| 8 | QuestionnaireSectionBPEOQuestionOrder | QUESTION_ORDER | — | ✅ |
| 9 | QuestionnaireSectionBPEOQuestionnaireId | QUESTIONNAIRE_ID | — | — |
| 10 | QuestionnaireSectionBPEOResponseOrder | RESPONSE_ORDER | — | — |
| 11 | QuestionnaireSectionBPEOSectionSeqNum | SECTION_SEQ_NUM | — | ✅ |

### [[hrq_qstnr_sections_tl|HRQ_QSTNR_SECTIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QstnrSectionTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | QstnrSectionTranslationPEODescription | DESCRIPTION | — | ✅ |
| 3 | QstnrSectionTranslationPEOIntroText | INTRO_TEXT | — | ✅ |
| 4 | QstnrSectionTranslationPEOLanguage | LANGUAGE | — | — |
| 5 | QstnrSectionTranslationPEOName | NAME | — | ✅ |
| 6 | QstnrSectionTranslationPEOQstnrSectionId | QSTNR_SECTION_ID | — | — |
| 7 | QstnrSectionTranslationPEOSourceLang | SOURCE_LANG | — | — |

### [[hrq_qstn_answers_b|HRQ_QSTN_ANSWERS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AnswerCode | ANSWER_CODE | — | — |
| 2 | ConditionQstnAnswerBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | ConditionQstnAnswerBPEOQstnAnswerId | QSTN_ANSWER_ID | — | — |
| 4 | QuestionAnswerBPEOAddlQstnrId | ADDL_QSTNR_ID | — | — |
| 5 | QuestionAnswerBPEOAddlQstnrVersionNum | ADDL_QSTNR_VERSION_NUM | — | — |
| 6 | QuestionAnswerBPEOAnswerCode | ANSWER_CODE | — | — |
| 7 | QuestionAnswerBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 8 | QuestionAnswerBPEOCorrectFlag | CORRECT_FLAG | — | — |
| 9 | QuestionAnswerBPEOCreatedBy | CREATED_BY | — | — |
| 10 | QuestionAnswerBPEOCreationDate | CREATION_DATE | — | — |
| 11 | QuestionAnswerBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | QuestionAnswerBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | QuestionAnswerBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | QuestionAnswerBPEOModuleId | MODULE_ID | — | — |
| 15 | QuestionAnswerBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | QuestionAnswerBPEOQstnAnswerId | QSTN_ANSWER_ID | — | ✅ |
| 17 | QuestionAnswerBPEOQstnVersionNum | QSTN_VERSION_NUM | — | — |
| 18 | QuestionAnswerBPEOQuestionId | QUESTION_ID | — | — |
| 19 | QuestionAnswerBPEORatingLevelId | RATING_LEVEL_ID | — | — |
| 20 | QuestionAnswerBPEOScore | SCORE | — | ✅ |
| 21 | QuestionAnswerBPEOScoreWeight | SCORE_WEIGHT | — | — |
| 22 | QuestionAnswerBPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 23 | QuestionAnswerBPEOSeqNum | SEQ_NUM | — | ✅ |

### [[hrq_qstn_answers_tl|HRQ_QSTN_ANSWERS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConditionQstnAnswerTLPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ConditionQstnAnswerTLPEOLanguage | LANGUAGE | — | — |
| 3 | ConditionQstnAnswerTLPEOLongText | LONG_TEXT | — | — |
| 4 | ConditionQstnAnswerTLPEOQstnAnswerId | QSTN_ANSWER_ID | — | — |
| 5 | ConditionQstnAnswerTLPEOShortText | SHORT_TEXT | — | — |
| 6 | QuestionAnswerTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 7 | QuestionAnswerTranslationPEOCreatedBy | CREATED_BY | — | — |
| 8 | QuestionAnswerTranslationPEOCreationDate | CREATION_DATE | — | — |
| 9 | QuestionAnswerTranslationPEOLanguage | LANGUAGE | — | — |
| 10 | QuestionAnswerTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | QuestionAnswerTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | QuestionAnswerTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | QuestionAnswerTranslationPEOLongText | LONG_TEXT | — | ✅ |
| 14 | QuestionAnswerTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | QuestionAnswerTranslationPEOQstnAnswerId | QSTN_ANSWER_ID | — | ✅ |
| 16 | QuestionAnswerTranslationPEOResponseFeedback | RESPONSE_FEEDBACK | — | ✅ |
| 17 | QuestionAnswerTranslationPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 18 | QuestionAnswerTranslationPEOShortText | SHORT_TEXT | — | ✅ |
| 19 | QuestionAnswerTranslationPEOSourceLang | SOURCE_LANG | — | — |

### [[hrq_questionnaires_b|HRQ_QUESTIONNAIRES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QuestionnaireBPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | QuestionnaireBPEOLatestVersion | LATEST_VERSION | — | — |
| 3 | QuestionnaireBPEOQstnrVersionNum | QSTNR_VERSION_NUM | 🔑 | ✅ |
| 4 | QuestionnaireBPEOQuestionnaireId | QUESTIONNAIRE_ID | 🔑 | ✅ |

### [[hrq_questions_b|HRQ_QUESTIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConditionQuestionBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ConditionQuestionBPEOQstnVersionNum | QSTN_VERSION_NUM | — | — |
| 3 | ConditionQuestionBPEOQuestionCode | QUESTION_CODE | — | — |
| 4 | ConditionQuestionBPEOQuestionId | QUESTION_ID | — | — |
| 5 | QuestionBPEOAdhocFlag | ADHOC_FLAG | — | — |
| 6 | QuestionBPEOAllJobFamiliesFlag | ALL_JOB_FAMILIES_FLAG | — | — |
| 7 | QuestionBPEOAllJobFunctionsFlag | ALL_JOB_FUNCTIONS_FLAG | — | — |
| 8 | QuestionBPEOAllLocationsFlag | ALL_LOCATIONS_FLAG | — | — |
| 9 | QuestionBPEOAllOrganizationsFlag | ALL_ORGANIZATIONS_FLAG | — | — |
| 10 | QuestionBPEOAttachmentAllowed | ATTACHMENT_ALLOWED | — | — |
| 11 | QuestionBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 12 | QuestionBPEOCandidateCode | CANDIDATE_CODE | — | — |
| 13 | QuestionBPEOCategoryId | CATEGORY_ID | — | — |
| 14 | QuestionBPEOClassificationCode | CLASSIFICATION_CODE | — | ✅ |
| 15 | QuestionBPEOConditionAnswerId | CONDITION_ANSWER_ID | — | — |
| 16 | QuestionBPEOConditionDisplay | CONDITION_DISPLAY | — | — |
| 17 | QuestionBPEOConditionQstnVersionNum | CONDITION_QSTN_VERSION_NUM | — | — |
| 18 | QuestionBPEOConditionQuestionId | CONDITION_QUESTION_ID | — | — |
| 19 | QuestionBPEOLatestVersion | LATEST_VERSION | — | — |
| 20 | QuestionBPEOMaxLength | MAX_LENGTH | — | — |
| 21 | QuestionBPEOMaxPossibleScore | MAX_POSSIBLE_SCORE | — | — |
| 22 | QuestionBPEOMaxSelections | MAX_SELECTIONS | — | — |
| 23 | QuestionBPEOMaxThresholdScore | MAX_THRESHOLD_SCORE | — | ✅ |
| 24 | QuestionBPEOMinLength | MIN_LENGTH | — | — |
| 25 | QuestionBPEOMinSelections | MIN_SELECTIONS | — | — |
| 26 | QuestionBPEOMinThresholdScore | MIN_THRESHOLD_SCORE | — | ✅ |
| 27 | QuestionBPEOModuleId | MODULE_ID | — | — |
| 28 | QuestionBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 29 | QuestionBPEOOverrideDescFlag | OVERRIDE_DESC_FLAG | — | — |
| 30 | QuestionBPEOOwner | OWNER | — | — |
| 31 | QuestionBPEOPrivacyFlag | PRIVACY_FLAG | — | — |
| 32 | QuestionBPEOQstnVersionNum | QSTN_VERSION_NUM | — | ✅ |
| 33 | QuestionBPEOQuestionCode | QUESTION_CODE | — | — |
| 34 | QuestionBPEOQuestionId | QUESTION_ID | — | ✅ |
| 35 | QuestionBPEOQuestionType | QUESTION_TYPE | — | ✅ |
| 36 | QuestionBPEORatingModelId | RATING_MODEL_ID | — | — |
| 37 | QuestionBPEOResponseTypeId | RESPONSE_TYPE_ID | — | — |
| 38 | QuestionBPEOScoredFlag | SCORED_FLAG | — | — |
| 39 | QuestionBPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 40 | QuestionBPEOStatus | STATUS | — | ✅ |
| 41 | QuestionBPEOSubscriberId | SUBSCRIBER_ID | — | — |
| 42 | QuestionBPEOUpdateAllowed | UPDATE_ALLOWED | — | — |
| 43 | QuestionBPEOVersionDescription | VERSION_DESCRIPTION | — | — |

### [[hrq_questions_tl|HRQ_QUESTIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConditionQuestionTLPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ConditionQuestionTLPEOLanguage | LANGUAGE | — | — |
| 3 | ConditionQuestionTLPEOQstnVersionNum | QSTN_VERSION_NUM | — | — |
| 4 | ConditionQuestionTLPEOQuestionId | QUESTION_ID | — | — |
| 5 | ConditionQuestionTLPEOQuestionText | QUESTION_TEXT | — | — |
| 6 | QuestionTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 7 | QuestionTranslationPEOInstructionsText | INSTRUCTIONS_TEXT | — | — |
| 8 | QuestionTranslationPEOLanguage | LANGUAGE | — | — |
| 9 | QuestionTranslationPEOQstnVersionNum | QSTN_VERSION_NUM | — | — |
| 10 | QuestionTranslationPEOQuestionId | QUESTION_ID | — | — |
| 11 | QuestionTranslationPEOQuestionText | QUESTION_TEXT | — | ✅ |
| 12 | QuestionTranslationPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 13 | QuestionTranslationPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
