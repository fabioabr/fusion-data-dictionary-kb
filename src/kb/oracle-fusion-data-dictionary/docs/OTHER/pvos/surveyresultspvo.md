---
id: DOC-OTHER-PVO-SurveyResultsPVO
doc_type: system-doc
title: "SurveyResultsPVO — PVO Cross-Module"
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
  - SurveyResultsPVO
  - surveyresultspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SurveyResultsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Survey Results. Acessa as tabelas: GRC_SURVEY_RESULT_V, GRC_SUV_PARTICIPANT, GRC_SUV_QUESTION_ODR_OTBI_V (+13).

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.SurveyResultsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 255 | 16 | 5 | 50 | 20% |

---

## 🔗 Tabelas Relacionadas

- [[grc_survey_result_v|GRC_SURVEY_RESULT_V]] — 73 atributos (3 PKs, 19 BICC)
- [[grc_suv_participant|GRC_SUV_PARTICIPANT]] — 16 atributos (2 BICC)
- [[grc_suv_question_odr_otbi_v|GRC_SUV_QUESTION_ODR_OTBI_V]] — 17 atributos
- [[grc_suv_question_tl|GRC_SUV_QUESTION_TL]] — 9 atributos (2 BICC)
- [[grc_suv_q_choice_tl|GRC_SUV_Q_CHOICE_TL]] — 10 atributos (1 PKs, 3 BICC)
- [[grc_suv_q_choice_vl|GRC_SUV_Q_CHOICE_VL]] — 20 atributos (2 BICC)
- [[grc_suv_response|GRC_SUV_RESPONSE]] — 11 atributos (1 PKs, 5 BICC)
- [[grc_suv_resp_comments|GRC_SUV_RESP_COMMENTS]] — 10 atributos (1 BICC)
- [[grc_suv_survey_tl|GRC_SUV_SURVEY_TL]] — 11 atributos (3 BICC)
- [[grc_suv_template_b|GRC_SUV_TEMPLATE_B]] — 23 atributos (5 BICC)
- [[grc_suv_template_tl|GRC_SUV_TEMPLATE_TL]] — 4 atributos (1 BICC)
- [[gtg_sc_frc_access_v|GTG_SC_FRC_ACCESS_V]] — 3 atributos
- [[gtg_survey_comp_otbi_v|GTG_SURVEY_COMP_OTBI_V]] — 5 atributos (2 BICC)
- [[per_email_addresses|PER_EMAIL_ADDRESSES]] — 3 atributos (1 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 20 atributos (4 BICC)
- [[per_users|PER_USERS]] — 20 atributos

---

## ⚙️ Atributos

### [[grc_survey_result_v|GRC_SURVEY_RESULT_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SurveyBasePEOChoiceChoiceId | CHOICE_CHOICE_ID | 🔑 | ✅ |
| 2 | SurveyBasePEOChoiceCreatedBy | CHOICE_CREATED_BY | — | — |
| 3 | SurveyBasePEOChoiceCreationDate | CHOICE_CREATION_DATE | — | — |
| 4 | SurveyBasePEOChoiceLastUpdateDate | CHOICE_LAST_UPDATE_DATE | — | ✅ |
| 5 | SurveyBasePEOChoiceLastUpdateLogin | CHOICE_LAST_UPDATE_LOGIN | — | — |
| 6 | SurveyBasePEOChoiceLastUpdatedBy | CHOICE_LAST_UPDATED_BY | — | — |
| 7 | SurveyBasePEOChoiceObjectVersionNumber | CHOICE_OBJECT_VERSION_NUMBER | — | — |
| 8 | SurveyBasePEOChoiceSeeded | CHOICE_SEEDED | — | — |
| 9 | SurveyBasePEOPartiCompletedDate | PARTI_COMPLETED_DATE | — | — |
| 10 | SurveyBasePEOPartiCreatedBy | PARTI_CREATED_BY | — | — |
| 11 | SurveyBasePEOPartiCreationDate | PARTI_CREATION_DATE | — | — |
| 12 | SurveyBasePEOPartiEntityId | PARTI_ENTITY_ID | — | ✅ |
| 13 | SurveyBasePEOPartiEntityTypeCode | PARTI_ENTITY_TYPE_CODE | — | — |
| 14 | SurveyBasePEOPartiLastStateCode | PARTI_LAST_STATE_CODE | — | — |
| 15 | SurveyBasePEOPartiLastUpdateDate | PARTI_LAST_UPDATE_DATE | — | ✅ |
| 16 | SurveyBasePEOPartiLastUpdateLogin | PARTI_LAST_UPDATE_LOGIN | — | — |
| 17 | SurveyBasePEOPartiLastUpdatedBy | PARTI_LAST_UPDATED_BY | — | — |
| 18 | SurveyBasePEOPartiParticipantId | PARTI_PARTICIPANT_ID | 🔑 | ✅ |
| 19 | SurveyBasePEOPartiStartDate | PARTI_START_DATE | — | — |
| 20 | SurveyBasePEOPartiStateCode | PARTI_STATE_CODE | — | — |
| 21 | SurveyBasePEOPartiStateDate | PARTI_STATE_DATE | — | — |
| 22 | SurveyBasePEOPartiSurveyId | PARTI_SURVEY_ID | — | — |
| 23 | SurveyBasePEOPartiUserId | PARTI_USER_ID | — | ✅ |
| 24 | SurveyBasePEOQtQuestionFormatTypeCode | QT_QUESTION_FORMAT_TYPE_CODE | — | — |
| 25 | SurveyBasePEOQuestionAddCommentBox | QUESTION_ADD_COMMENT_BOX | — | — |
| 26 | SurveyBasePEOQuestionApproveCompleteDate | QUESTION_APPROVE_COMPLETE_DATE | — | — |
| 27 | SurveyBasePEOQuestionCreatedBy | QUESTION_CREATED_BY | — | — |
| 28 | SurveyBasePEOQuestionCreationDate | QUESTION_CREATION_DATE | — | — |
| 29 | SurveyBasePEOQuestionDisplayCode | QUESTION_DISPLAY_CODE | — | — |
| 30 | SurveyBasePEOQuestionEffectiveSequence | QUESTION_EFFECTIVE_SEQUENCE | — | — |
| 31 | SurveyBasePEOQuestionLastStateCode | QUESTION_LAST_STATE_CODE | — | — |
| 32 | SurveyBasePEOQuestionLastUpdateDate | QUESTION_LAST_UPDATE_DATE | — | ✅ |
| 33 | SurveyBasePEOQuestionLastUpdateLogin | QUESTION_LAST_UPDATE_LOGIN | — | — |
| 34 | SurveyBasePEOQuestionLastUpdatedBy | QUESTION_LAST_UPDATED_BY | — | — |
| 35 | SurveyBasePEOQuestionObjectVersionNumber | QUESTION_OBJECT_VERSION_NUMBER | — | — |
| 36 | SurveyBasePEOQuestionQuestionId | QUESTION_QUESTION_ID | 🔑 | ✅ |
| 37 | SurveyBasePEOQuestionQuestionTypeCode | QUESTION_QUESTION_TYPE_CODE | — | — |
| 38 | SurveyBasePEOQuestionRangeOfScale | QUESTION_RANGE_OF_SCALE | — | — |
| 39 | SurveyBasePEOQuestionReviewStartDate | QUESTION_REVIEW_START_DATE | — | — |
| 40 | SurveyBasePEOQuestionRevisionDate | QUESTION_REVISION_DATE | — | — |
| 41 | SurveyBasePEOQuestionRevisionNumber | QUESTION_REVISION_NUMBER | — | — |
| 42 | SurveyBasePEOQuestionSeeded | QUESTION_SEEDED | — | — |
| 43 | SurveyBasePEOQuestionStateCode | QUESTION_STATE_CODE | — | — |
| 44 | SurveyBasePEOQuestionStateDate | QUESTION_STATE_DATE | — | — |
| 45 | SurveyBasePEOQuestionStatus | QUESTION_STATUS | — | — |
| 46 | SurveyBasePEOQuestionTotalToAllocate | QUESTION_TOTAL_TO_ALLOCATE | — | — |
| 47 | SurveyBasePEOSurveyApproveCompleteDate | SURVEY_APPROVE_COMPLETE_DATE | — | — |
| 48 | SurveyBasePEOSurveyAssessmentId | SURVEY_ASSESSMENT_ID | — | — |
| 49 | SurveyBasePEOSurveyCreatedBy | SURVEY_CREATED_BY | — | ✅ |
| 50 | SurveyBasePEOSurveyCreationDate | SURVEY_CREATION_DATE | — | ✅ |
| 51 | SurveyBasePEOSurveyDueDate | SURVEY_DUE_DATE | — | ✅ |
| 52 | SurveyBasePEOSurveyEffectiveSequence | SURVEY_EFFECTIVE_SEQUENCE | — | — |
| 53 | SurveyBasePEOSurveyEndDate | SURVEY_END_DATE | — | ✅ |
| 54 | SurveyBasePEOSurveyEntityId | SURVEY_ENTITY_ID | — | ✅ |
| 55 | SurveyBasePEOSurveyEntityTypeCode | SURVEY_ENTITY_TYPE_CODE | — | — |
| 56 | SurveyBasePEOSurveyLastStateCode | SURVEY_LAST_STATE_CODE | — | — |
| 57 | SurveyBasePEOSurveyLastUpdateDate | SURVEY_LAST_UPDATE_DATE | — | ✅ |
| 58 | SurveyBasePEOSurveyLastUpdateLogin | SURVEY_LAST_UPDATE_LOGIN | — | — |
| 59 | SurveyBasePEOSurveyLastUpdatedBy | SURVEY_LAST_UPDATED_BY | — | ✅ |
| 60 | SurveyBasePEOSurveyObjectVersionNumber | SURVEY_OBJECT_VERSION_NUMBER | — | — |
| 61 | SurveyBasePEOSurveyOrigin | SURVEY_ORIGIN | — | — |
| 62 | SurveyBasePEOSurveyReviewStartDate | SURVEY_REVIEW_START_DATE | — | — |
| 63 | SurveyBasePEOSurveyRevisionDate | SURVEY_REVISION_DATE | — | — |
| 64 | SurveyBasePEOSurveyRevisionNumber | SURVEY_REVISION_NUMBER | — | — |
| 65 | SurveyBasePEOSurveyStartDate | SURVEY_START_DATE | — | ✅ |
| 66 | SurveyBasePEOSurveyStateCode | SURVEY_STATE_CODE | — | ✅ |
| 67 | SurveyBasePEOSurveyStateDate | SURVEY_STATE_DATE | — | — |
| 68 | SurveyBasePEOSurveyStatus | SURVEY_STATUS | — | ✅ |
| 69 | SurveyBasePEOSurveySurveyId | SURVEY_SURVEY_ID | — | ✅ |
| 70 | SurveyBasePEOSurveyTemplateId | SURVEY_TEMPLATE_ID | — | — |
| 71 | SurveyBasePEOTempMandatoryFlag | TEMP_MANDATORY_FLAG | — | — |
| 72 | SurveyBasePEOTempPagebreakId | TEMP_PAGEBREAK_ID | — | — |
| 73 | SurveyBasePEOTempQuestionSequence | TEMP_QUESTION_SEQUENCE | — | — |

### [[grc_suv_participant|GRC_SUV_PARTICIPANT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | StateDate | STATE_DATE | — | — |
| 2 | SurveyParticipantPEOCompletedBy | COMPLETED_BY | — | — |
| 3 | SurveyParticipantPEOCompltdDt | COMPLETED_DATE | — | ✅ |
| 4 | SurveyParticipantPEOCreatedBy | CREATED_BY | — | — |
| 5 | SurveyParticipantPEOCreationDt | CREATION_DATE | — | — |
| 6 | SurveyParticipantPEOEntTypCd | ENTITY_TYPE_CODE | — | — |
| 7 | SurveyParticipantPEOEntityId | ENTITY_ID | — | — |
| 8 | SurveyParticipantPEOLstStCd | LAST_STATE_CODE | — | — |
| 9 | SurveyParticipantPEOLstUpdtDt | LAST_UPDATE_DATE | — | — |
| 10 | SurveyParticipantPEOLstUpdtLgn | LAST_UPDATE_LOGIN | — | — |
| 11 | SurveyParticipantPEOLstUpdtdBy | LAST_UPDATED_BY | — | — |
| 12 | SurveyParticipantPEOPrtcpntId | PARTICIPANT_ID | — | — |
| 13 | SurveyParticipantPEOStartDate | START_DATE | — | — |
| 14 | SurveyParticipantPEOStateCd | STATE_CODE | — | ✅ |
| 15 | SurveyParticipantPEOSurveyId | SURVEY_ID | — | — |
| 16 | SurveyParticipantPEOUserId | USER_ID | — | — |

### [[grc_suv_question_odr_otbi_v|GRC_SUV_QUESTION_ODR_OTBI_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SurveyQuestionOrderPEOActualDbQSequence | ACTUAL_DB_Q_SEQUENCE | — | — |
| 2 | SurveyQuestionOrderPEOCalculatedQSequence | CALCULATED_Q_SEQUENCE | — | — |
| 3 | SurveyQuestionOrderPEOCreatedBy | CREATED_BY | — | — |
| 4 | SurveyQuestionOrderPEOCreationDate | CREATION_DATE | — | — |
| 5 | SurveyQuestionOrderPEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 6 | SurveyQuestionOrderPEOIsActive | IS_ACTIVE | — | — |
| 7 | SurveyQuestionOrderPEOIsSeeded | IS_SEEDED | — | — |
| 8 | SurveyQuestionOrderPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 9 | SurveyQuestionOrderPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | SurveyQuestionOrderPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | SurveyQuestionOrderPEOMandatoryFlag | MANDATORY_FLAG | — | — |
| 12 | SurveyQuestionOrderPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | SurveyQuestionOrderPEOPagebreakId | PAGEBREAK_ID | — | — |
| 14 | SurveyQuestionOrderPEOQuestionId | QUESTION_ID | — | — |
| 15 | SurveyQuestionOrderPEORevisionDate | REVISION_DATE | — | — |
| 16 | SurveyQuestionOrderPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 17 | SurveyQuestionOrderPEOTemplateId | TEMPLATE_ID | — | — |

### [[grc_suv_question_tl|GRC_SUV_QUESTION_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SurveyQuestionsTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | SurveyQuestionsTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | SurveyQuestionsTranslationPEOLanguage | LANGUAGE | — | — |
| 4 | SurveyQuestionsTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | SurveyQuestionsTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | SurveyQuestionsTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | SurveyQuestionsTranslationPEOQuestionId | QUESTION_ID | — | — |
| 8 | SurveyQuestionsTranslationPEOQuestionText | QUESTION_TEXT | — | ✅ |
| 9 | SurveyQuestionsTranslationPEOSourceLang | SOURCE_LANG | — | — |

### [[grc_suv_q_choice_tl|GRC_SUV_Q_CHOICE_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SurveyQChoiceTranslationPEOChoiceId | CHOICE_ID | 🔑 | ✅ |
| 2 | SurveyQChoiceTranslationPEOCreatedBy | CREATED_BY | — | — |
| 3 | SurveyQChoiceTranslationPEOCreationDate | CREATION_DATE | — | — |
| 4 | SurveyQChoiceTranslationPEOLanguage | LANGUAGE | — | — |
| 5 | SurveyQChoiceTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | SurveyQChoiceTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | SurveyQChoiceTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | SurveyQChoiceTranslationPEOName | NAME | — | ✅ |
| 9 | SurveyQChoiceTranslationPEOQuestionId | QUESTION_ID | — | — |
| 10 | SurveyQChoiceTranslationPEOSourceLang | SOURCE_LANG | — | — |

### [[grc_suv_q_choice_vl|GRC_SUV_Q_CHOICE_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SurveyQChoicePEOChoiceId | CHOICE_ID | — | — |
| 2 | SurveyQChoicePEOChoiceOther | CHOICE_OTHER | — | ✅ |
| 3 | SurveyQChoicePEOCreatedBy | CREATED_BY | — | — |
| 4 | SurveyQChoicePEOCreationDate | CREATION_DATE | — | — |
| 5 | SurveyQChoicePEOEffSeq | EFFECTIVE_SEQUENCE | — | — |
| 6 | SurveyQChoicePEOIsActive | IS_ACTIVE | — | — |
| 7 | SurveyQChoicePEOIsSeeded | IS_SEEDED | — | — |
| 8 | SurveyQChoicePEOLanguage | LANGUAGE | — | — |
| 9 | SurveyQChoicePEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 10 | SurveyQChoicePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | SurveyQChoicePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | SurveyQChoicePEOName | NAME | — | ✅ |
| 13 | SurveyQChoicePEOObjVrsnNum | OBJECT_VERSION_NUMBER | — | — |
| 14 | SurveyQChoicePEOOrdinal | ORDINAL | — | — |
| 15 | SurveyQChoicePEOQuestionId | QUESTION_ID | — | — |
| 16 | SurveyQChoicePEORvsnDate | REVISION_DATE | — | — |
| 17 | SurveyQChoicePEORvsnNumber | REVISION_NUMBER | — | — |
| 18 | SurveyQChoicePEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 19 | SurveyQChoicePEOSeeded | SEEDED | — | — |
| 20 | SurveyQChoicePEOSourceLang | SOURCE_LANG | — | — |

### [[grc_suv_response|GRC_SUV_RESPONSE]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SurveyResponsePEOChoiceId | CHOICE_ID | — | ✅ |
| 2 | SurveyResponsePEOChoiceNumber | CHOICE_NUMBER | — | ✅ |
| 3 | SurveyResponsePEOChoiceText | CHOICE_TEXT | — | ✅ |
| 4 | SurveyResponsePEOCreatedBy | CREATED_BY | — | — |
| 5 | SurveyResponsePEOCreationDate | CREATION_DATE | — | — |
| 6 | SurveyResponsePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | SurveyResponsePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | SurveyResponsePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | SurveyResponsePEOParticipantId | PARTICIPANT_ID | 🔑 | ✅ |
| 10 | SurveyResponsePEOQuestionId | QUESTION_ID | — | — |
| 11 | SurveyResponsePEORevisionDate | REVISION_DATE | — | — |

### [[grc_suv_resp_comments|GRC_SUV_RESP_COMMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SurveyRespCommentsPEOCreatedBy | CREATED_BY | — | — |
| 2 | SurveyRespCommentsPEOCreationDate | CREATION_DATE | — | — |
| 3 | SurveyRespCommentsPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 4 | SurveyRespCommentsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 5 | SurveyRespCommentsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 6 | SurveyRespCommentsPEOParticipantId | PARTICIPANT_ID | — | — |
| 7 | SurveyRespCommentsPEOQuestionId | QUESTION_ID | — | — |
| 8 | SurveyRespCommentsPEOResponseComment | RESPONSE_COMMENT | — | ✅ |
| 9 | SurveyRespCommentsPEORevisionDate | REVISION_DATE | — | — |
| 10 | SurveyRespCommentsPEOSurveyResponseComment | SURVEY_RESPONSE_COMMENT | — | — |

### [[grc_suv_survey_tl|GRC_SUV_SURVEY_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SurveyTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | SurveyTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | SurveyTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | SurveyTranslationPEODtlDescr | DETAILED_DESCRIPTION | — | — |
| 5 | SurveyTranslationPEOLanguage | LANGUAGE | — | — |
| 6 | SurveyTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | SurveyTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | SurveyTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | SurveyTranslationPEOName | NAME | — | ✅ |
| 10 | SurveyTranslationPEOSourceLang | SOURCE_LANG | — | — |
| 11 | SurveyTranslationPEOSurveyId | SURVEY_ID | — | — |

### [[grc_suv_template_b|GRC_SUV_TEMPLATE_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SurveyTemplatePEOApproveCompleteDate | APPROVE_COMPLETE_DATE | — | — |
| 2 | SurveyTemplatePEOApprovedBy | APPROVED_BY | — | ✅ |
| 3 | SurveyTemplatePEOApprovedDate | APPROVED_DATE | — | ✅ |
| 4 | SurveyTemplatePEOCreatedBy | CREATED_BY | — | — |
| 5 | SurveyTemplatePEOCreationDate | CREATION_DATE | — | — |
| 6 | SurveyTemplatePEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 7 | SurveyTemplatePEOLastStateCode | LAST_STATE_CODE | — | — |
| 8 | SurveyTemplatePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | SurveyTemplatePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | SurveyTemplatePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | SurveyTemplatePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | SurveyTemplatePEOReviewStartDate | REVIEW_START_DATE | — | — |
| 13 | SurveyTemplatePEOReviewedBy | REVIEWED_BY | — | ✅ |
| 14 | SurveyTemplatePEOReviewedDate | REVIEWED_DATE | — | ✅ |
| 15 | SurveyTemplatePEORevisionDate | REVISION_DATE | — | — |
| 16 | SurveyTemplatePEORevisionNumber | REVISION_NUMBER | — | — |
| 17 | SurveyTemplatePEORevisionSubmittedBy | REVISION_SUBMITTED_BY | — | — |
| 18 | SurveyTemplatePEOSeeded | SEEDED | — | — |
| 19 | SurveyTemplatePEOStateCode | STATE_CODE | — | — |
| 20 | SurveyTemplatePEOStateDate | STATE_DATE | — | — |
| 21 | SurveyTemplatePEOStatus | STATUS | — | — |
| 22 | SurveyTemplatePEOSurveyType | SURVEY_TYPE | — | — |
| 23 | SurveyTemplatePEOTemplateId | TEMPLATE_ID | — | — |

### [[grc_suv_template_tl|GRC_SUV_TEMPLATE_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SurveyTempTransPEODescription | DESCRIPTION | — | — |
| 2 | SurveyTempTransPEOLanguage | LANGUAGE | — | — |
| 3 | SurveyTempTransPEOName | NAME | — | ✅ |
| 4 | SurveyTempTransPEOTemplateId | TEMPLATE_ID | — | — |

### [[gtg_sc_frc_access_v|GTG_SC_FRC_ACCESS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FRCSecurityPEOSecurableId | SECURABLE_ID | — | — |
| 2 | FRCSecurityPEOSecurableType | SECURABLE_TYPE | — | — |
| 3 | FRCSecurityPEOUserId | USER_ID | — | — |

### [[gtg_survey_comp_otbi_v|GTG_SURVEY_COMP_OTBI_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SurveyComponentPEOCompName | COMPONENT_NAME | — | ✅ |
| 2 | SurveyComponentPEOCompType | COMPONENT_TYPE | — | ✅ |
| 3 | SurveyComponentPEOEntTypCd | ENTITY_TYPE_CODE | — | — |
| 4 | SurveyComponentPEOEntityId | ENTITY_ID | — | — |
| 5 | SurveyComponentPEOSurveyId | SURVEY_ID | — | — |

### [[per_email_addresses|PER_EMAIL_ADDRESSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EmailAddressPEOEmailAddress | EMAIL_ADDRESS | — | ✅ |
| 2 | EmailAddressPEOEmailAddressId | EMAIL_ADDRESS_ID | — | — |
| 3 | EmailAddressPEOEmailType | EMAIL_TYPE | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SrvyPersonApprovedByDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | SrvyPersonApprovedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | SrvyPersonApprovedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | SrvyPersonApprovedByPersonId | PERSON_ID | — | — |
| 5 | SrvyPersonApprovedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | SrvyPersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 7 | SrvyPersonCreatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | SrvyPersonCreatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | SrvyPersonCreatedByPersonId | PERSON_ID | — | — |
| 10 | SrvyPersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 11 | SrvyPersonReviewedByDisplayName | DISPLAY_NAME | — | ✅ |
| 12 | SrvyPersonReviewedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 13 | SrvyPersonReviewedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 14 | SrvyPersonReviewedByPersonId | PERSON_ID | — | — |
| 15 | SrvyPersonReviewedByPersonNameId | PERSON_NAME_ID | — | — |
| 16 | SrvyPersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 17 | SrvyPersonUpdatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 18 | SrvyPersonUpdatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 19 | SrvyPersonUpdatedByPersonId | PERSON_ID | — | — |
| 20 | SrvyPersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SrvyApprovedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | SrvyApprovedByPersonId | PERSON_ID | — | — |
| 3 | SrvyApprovedByUserGuid | USER_GUID | — | — |
| 4 | SrvyApprovedByUserId | USER_ID | — | — |
| 5 | SrvyApprovedByUsername | USERNAME | — | — |
| 6 | SrvyCreatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | SrvyCreatedByPersonId | PERSON_ID | — | — |
| 8 | SrvyCreatedByUserGuid | USER_GUID | — | — |
| 9 | SrvyCreatedByUserId | USER_ID | — | — |
| 10 | SrvyCreatedByUsername | USERNAME | — | — |
| 11 | SrvyReviewedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | SrvyReviewedByPersonId | PERSON_ID | — | — |
| 13 | SrvyReviewedByUserGuid | USER_GUID | — | — |
| 14 | SrvyReviewedByUserId | USER_ID | — | — |
| 15 | SrvyReviewedByUsername | USERNAME | — | — |
| 16 | SrvyUpdatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | SrvyUpdatedByPersonId | PERSON_ID | — | — |
| 18 | SrvyUpdatedByUserGuid | USER_GUID | — | — |
| 19 | SrvyUpdatedByUserId | USER_ID | — | — |
| 20 | SrvyUpdatedByUsername | USERNAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
