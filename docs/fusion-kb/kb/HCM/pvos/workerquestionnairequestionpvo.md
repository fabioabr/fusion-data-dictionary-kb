---
id: DOC-HCM-PVO-WorkerQuestionnaireQuestionPVO
doc_type: system-doc
title: "WorkerQuestionnaireQuestionPVO — PVO Human Capital Management"
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
  - WorkerQuestionnaireQuestionPVO
  - workerquestionnairequestionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WorkerQuestionnaireQuestionPVO

## 📌 Visão Geral

Disponibiliza perguntas de questionários atribuídos a colaboradores com seções e respostas. Suporta avaliações e pesquisas direcionadas a trabalhadores específicos.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.QuestionnaireAM.WorkerQuestionnaireQuestionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 149 | 10 | 2 | 11 | 7% |

---

## 🔗 Tabelas Relacionadas

- [[hrq_qstnr_participants|HRQ_QSTNR_PARTICIPANTS]] — 11 atributos
- [[hrq_qstnr_questions|HRQ_QSTNR_QUESTIONS]] — 17 atributos (2 BICC)
- [[hrq_qstnr_sections_b|HRQ_QSTNR_SECTIONS_B]] — 17 atributos (2 PKs, 3 BICC)
- [[hrq_qstnr_sections_tl|HRQ_QSTNR_SECTIONS_TL]] — 13 atributos (1 BICC)
- [[hrq_qstn_answers_b|HRQ_QSTN_ANSWERS_B]] — 3 atributos
- [[hrq_qstn_answers_tl|HRQ_QSTN_ANSWERS_TL]] — 5 atributos
- [[hrq_questionnaires_b|HRQ_QUESTIONNAIRES_B]] — 20 atributos
- [[hrq_questionnaires_tl|HRQ_QUESTIONNAIRES_TL]] — 7 atributos
- [[hrq_questions_b|HRQ_QUESTIONS_B]] — 38 atributos (3 BICC)
- [[hrq_questions_tl|HRQ_QUESTIONS_TL]] — 18 atributos (2 BICC)

---

## ⚙️ Atributos

### [[hrq_qstnr_participants|HRQ_QSTNR_PARTICIPANTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QuestionnaireBPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 2 | QuestionnaireParticipantPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | QuestionnaireParticipantPEOParticipantId | PARTICIPANT_ID | — | — |
| 4 | QuestionnaireParticipantPEOParticipantType | PARTICIPANT_TYPE | — | — |
| 5 | QuestionnaireParticipantPEOQstnrParticipantId | QSTNR_PARTICIPANT_ID | — | — |
| 6 | QuestionnaireParticipantPEOQuestionnaireId | QUESTIONNAIRE_ID | — | — |
| 7 | QuestionnaireParticipantPEOStatus | STATUS | — | — |
| 8 | QuestionnaireParticipantPEOSubjectCode | SUBJECT_CODE | — | — |
| 9 | QuestionnaireParticipantPEOSubjectId | SUBJECT_ID | — | — |
| 10 | QuestionnaireParticipantPEOSubmittedDateTime | SUBMITTED_DATE_TIME | — | — |
| 11 | QuestionnaireParticipantPEOSubscriberId | SUBSCRIBER_ID | — | — |

### [[hrq_qstnr_questions|HRQ_QSTNR_QUESTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QuestionnaireQuestionPEOAdhocQstn | ADHOC_QSTN | — | — |
| 2 | QuestionnaireQuestionPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
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
| 13 | QuestionnaireQuestionPEOQstnrQuestionId | QSTNR_QUESTION_ID | — | — |
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
| 1 | QuestionSectionTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | QuestionSectionTranslationPEOLanguage | LANGUAGE | — | — |
| 3 | QuestionSectionTranslationPEOName | NAME | — | — |
| 4 | QuestionSectionTranslationPEOQstnrSectionId | QSTNR_SECTION_ID | — | — |
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

### [[hrq_questionnaires_b|HRQ_QUESTIONNAIRES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QuestionnaireBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | QuestionnaireBPEOCategoryId | CATEGORY_ID | — | — |
| 3 | QuestionnaireBPEOInUse | IN_USE | — | — |
| 4 | QuestionnaireBPEOLatestVersion | LATEST_VERSION | — | — |
| 5 | QuestionnaireBPEOOwner | OWNER | — | — |
| 6 | QuestionnaireBPEOPageLayout | PAGE_LAYOUT | — | — |
| 7 | QuestionnaireBPEOPrivacyFlag | PRIVACY_FLAG | — | — |
| 8 | QuestionnaireBPEOQstnrTemplateId | QSTNR_TEMPLATE_ID | — | — |
| 9 | QuestionnaireBPEOQstnrVersionNum | QSTNR_VERSION_NUM | — | — |
| 10 | QuestionnaireBPEOQstnsPerPage | QSTNS_PER_PAGE | — | — |
| 11 | QuestionnaireBPEOQuestionnaireCode | QUESTIONNAIRE_CODE | — | — |
| 12 | QuestionnaireBPEOQuestionnaireId | QUESTIONNAIRE_ID | — | — |
| 13 | QuestionnaireBPEOSectionOrder | SECTION_ORDER | — | — |
| 14 | QuestionnaireBPEOSectionPresentation | SECTION_PRESENTATION | — | — |
| 15 | QuestionnaireBPEOStatus | STATUS | — | — |
| 16 | QuestionnaireBPEOSubscriberId | SUBSCRIBER_ID | — | — |
| 17 | QuestionnaireBPEOTemplateFlag | TEMPLATE_FLAG | — | — |
| 18 | QuestionnaireBPEOUpdateAllowed | UPDATE_ALLOWED | — | — |
| 19 | QuestionnaireBPEOVersionDescription | VERSION_DESCRIPTION | — | — |
| 20 | QuestionnaireParticipantPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |

### [[hrq_questionnaires_tl|HRQ_QUESTIONNAIRES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QuestionnaireTLPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | QuestionnaireTLPEOIntroText | INTRO_TEXT | — | — |
| 3 | QuestionnaireTLPEOLanguage | LANGUAGE | — | — |
| 4 | QuestionnaireTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 5 | QuestionnaireTLPEOName | NAME | — | — |
| 6 | QuestionnaireTLPEOQstnrVersionNum | QSTNR_VERSION_NUM | — | — |
| 7 | QuestionnaireTLPEOQuestionnaireId | QUESTIONNAIRE_ID | — | — |

### [[hrq_questions_b|HRQ_QUESTIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConditionQuestionBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ConditionQuestionBPEOQstnVersionNum | QSTN_VERSION_NUM | — | — |
| 3 | ConditionQuestionBPEOQuestionCode | QUESTION_CODE | — | — |
| 4 | ConditionQuestionBPEOQuestionId | QUESTION_ID | — | — |
| 5 | QuestionBPEOAdhocFlag | ADHOC_FLAG | — | — |
| 6 | QuestionBPEOAttachmentAllowed | ATTACHMENT_ALLOWED | — | — |
| 7 | QuestionBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 8 | QuestionBPEOCategoryId | CATEGORY_ID | — | — |
| 9 | QuestionBPEOClassificationCode | CLASSIFICATION_CODE | — | — |
| 10 | QuestionBPEOConditionAnswerId | CONDITION_ANSWER_ID | — | — |
| 11 | QuestionBPEOConditionDisplay | CONDITION_DISPLAY | — | — |
| 12 | QuestionBPEOConditionQstnVersionNum | CONDITION_QSTN_VERSION_NUM | — | — |
| 13 | QuestionBPEOConditionQuestionId | CONDITION_QUESTION_ID | — | — |
| 14 | QuestionBPEOCreatedBy | CREATED_BY | — | — |
| 15 | QuestionBPEOCreationDate | CREATION_DATE | — | — |
| 16 | QuestionBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | QuestionBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 18 | QuestionBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 19 | QuestionBPEOLatestVersion | LATEST_VERSION | — | — |
| 20 | QuestionBPEOMaxLength | MAX_LENGTH | — | — |
| 21 | QuestionBPEOMaxSelections | MAX_SELECTIONS | — | — |
| 22 | QuestionBPEOMinLength | MIN_LENGTH | — | — |
| 23 | QuestionBPEOMinSelections | MIN_SELECTIONS | — | — |
| 24 | QuestionBPEOModuleId | MODULE_ID | — | — |
| 25 | QuestionBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 26 | QuestionBPEOOverrideDescFlag | OVERRIDE_DESC_FLAG | — | — |
| 27 | QuestionBPEOOwner | OWNER | — | — |
| 28 | QuestionBPEOPrivacyFlag | PRIVACY_FLAG | — | — |
| 29 | QuestionBPEOQstnVersionNum | QSTN_VERSION_NUM | — | — |
| 30 | QuestionBPEOQuestionCode | QUESTION_CODE | — | — |
| 31 | QuestionBPEOQuestionId | QUESTION_ID | — | ✅ |
| 32 | QuestionBPEOQuestionType | QUESTION_TYPE | — | ✅ |
| 33 | QuestionBPEORatingModelId | RATING_MODEL_ID | — | — |
| 34 | QuestionBPEOResponseTypeId | RESPONSE_TYPE_ID | — | — |
| 35 | QuestionBPEOStatus | STATUS | — | — |
| 36 | QuestionBPEOSubscriberId | SUBSCRIBER_ID | — | — |
| 37 | QuestionBPEOUpdateAllowed | UPDATE_ALLOWED | — | — |
| 38 | QuestionBPEOVersionDescription | VERSION_DESCRIPTION | — | — |

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
| 12 | QuestionnaireTranslationPEOCreatedBy | CREATED_BY | — | — |
| 13 | QuestionnaireTranslationPEOCreationDate | CREATION_DATE | — | — |
| 14 | QuestionnaireTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | QuestionnaireTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | QuestionnaireTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 17 | QuestionnaireTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | QuestionnaireTranslationPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
