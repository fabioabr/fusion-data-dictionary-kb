---
id: DOC-PO-PVO-RequisitionQstnrInterviewViewAllPVO
doc_type: system-doc
title: "RequisitionQstnrInterviewViewAllPVO — PVO Purchasing"
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
  - RequisitionQstnrInterviewViewAllPVO
  - requisitionqstnrinterviewviewallpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RequisitionQstnrInterviewViewAllPVO

## 📌 Visão Geral

Extrai questionários de entrevista associados a requisições de contratação, utilizados na avaliação de candidatos durante o processo seletivo. Suporta estruturação e consistência das entrevistas.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecHiringRequisitionAM.RequisitionQstnrInterviewViewAllPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 48 | 7 | 3 | 14 | 29% |

---

## 🔗 Tabelas Relacionadas

- [[hrq_categories_b|HRQ_CATEGORIES_B]] — 2 atributos
- [[hrq_categories_tl|HRQ_CATEGORIES_TL]] — 4 atributos (1 BICC)
- [[hrq_questionnaires_b|HRQ_QUESTIONNAIRES_B]] — 13 atributos (4 BICC)
- [[hrq_questionnaires_tl|HRQ_QUESTIONNAIRES_TL]] — 7 atributos (3 BICC)
- [[irc_im_req_qstnrs|IRC_IM_REQ_QSTNRS]] — 10 atributos (3 PKs, 4 BICC)
- [[irc_requisitions_b|IRC_REQUISITIONS_B]] — 2 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos (2 BICC)

---

## ⚙️ Atributos

### [[hrq_categories_b|HRQ_CATEGORIES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CategoryBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | CategoryBPEOCategoryId | CATEGORY_ID | — | — |

### [[hrq_categories_tl|HRQ_CATEGORIES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CategoryTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | CategoryTranslationPEOCategoryId | CATEGORY_ID | — | — |
| 3 | CategoryTranslationPEOLanguage | LANGUAGE | — | — |
| 4 | CategoryTranslationPEOName | NAME | — | ✅ |

### [[hrq_questionnaires_b|HRQ_QUESTIONNAIRES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QuestionnaireBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | QuestionnaireBPEOCategoryId | CATEGORY_ID | — | — |
| 3 | QuestionnaireBPEOCreatedBy | CREATED_BY | — | — |
| 4 | QuestionnaireBPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | QuestionnaireBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | QuestionnaireBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | QuestionnaireBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | QuestionnaireBPEOMaxPossibleScore | MAX_POSSIBLE_SCORE | — | — |
| 9 | QuestionnaireBPEOOwner | OWNER | — | ✅ |
| 10 | QuestionnaireBPEOQstnrVersionNum | QSTNR_VERSION_NUM | — | — |
| 11 | QuestionnaireBPEOQuestionnaireCode | QUESTIONNAIRE_CODE | — | ✅ |
| 12 | QuestionnaireBPEOQuestionnaireId | QUESTIONNAIRE_ID | — | — |
| 13 | QuestionnaireBPEOStatus | STATUS | — | — |

### [[hrq_questionnaires_tl|HRQ_QUESTIONNAIRES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QuestionnaireTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | QuestionnaireTranslationPEODescription | DESCRIPTION | — | ✅ |
| 3 | QuestionnaireTranslationPEOIntroText | INTRO_TEXT | — | ✅ |
| 4 | QuestionnaireTranslationPEOLanguage | LANGUAGE | — | — |
| 5 | QuestionnaireTranslationPEOName | NAME | — | ✅ |
| 6 | QuestionnaireTranslationPEOQstnrVersionNum | QSTNR_VERSION_NUM | — | — |
| 7 | QuestionnaireTranslationPEOQuestionnaireId | QUESTIONNAIRE_ID | — | — |

### [[irc_im_req_qstnrs|IRC_IM_REQ_QSTNRS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | CreationDate | CREATION_DATE | — | — |
| 3 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 5 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 6 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | QstnrTypeCode | QSTNR_TYPE_CODE | — | — |
| 8 | QstnrVersionNum | QSTNR_VERSION_NUM | 🔑 | ✅ |
| 9 | QuestionnaireId | QUESTIONNAIRE_ID | 🔑 | ✅ |
| 10 | RequisitionId | REQUISITION_ID | 🔑 | ✅ |

### [[irc_requisitions_b|IRC_REQUISITIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RequisitionBPEOReqUsageCode | REQ_USAGE_CODE | — | — |
| 2 | RequisitionBPEORequisitionId | REQUISITION_ID | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonNamePEODisplayName | DISPLAY_NAME | — | ✅ |
| 2 | PersonNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | PersonNamePEOFirstName | FIRST_NAME | — | — |
| 5 | PersonNamePEOFullName | FULL_NAME | — | — |
| 6 | PersonNamePEOLastName | LAST_NAME | — | — |
| 7 | PersonNamePEOListName | LIST_NAME | — | — |
| 8 | PersonNamePEOMiddleNames | MIDDLE_NAMES | — | — |
| 9 | PersonNamePEOPersonId | PERSON_ID | — | — |
| 10 | PersonNamePEOPersonNameId | PERSON_NAME_ID | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
