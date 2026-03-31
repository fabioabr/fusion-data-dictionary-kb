---
id: DOC-AP-PVO-ChecklistTaskTemplatePVO
doc_type: system-doc
title: "ChecklistTaskTemplatePVO — PVO Accounts Payable"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ap
  - data-dictionary
  - pvo
  - bicc
aliases:
  - ChecklistTaskTemplatePVO
  - checklisttasktemplatepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ChecklistTaskTemplatePVO

## 📌 Visão Geral

Extrai os templates de tarefas de checklists de RH, incluindo dependências, notificações, perfis de elegibilidade, documentos e questionários vinculados. Serve como base para padronizar e automatizar processos recorrentes de onboarding, transferências e desligamentos.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.ChecklistAM.ChecklistTaskTemplatePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 561 | 16 | 1 | 158 | 28% |

---

## 🔗 Tabelas Relacionadas

- [[ben_eligy_prfl|BEN_ELIGY_PRFL]] — 4 atributos (2 BICC)
- [[hrq_questionnaires_tl|HRQ_QUESTIONNAIRES_TL]] — 5 atributos (1 BICC)
- [[hr_document_types_tl|HR_DOCUMENT_TYPES_TL]] — 3 atributos (1 BICC)
- [[per_actions_b|PER_ACTIONS_B]] — 4 atributos
- [[per_actions_tl|PER_ACTIONS_TL]] — 3 atributos (1 BICC)
- [[per_checklists_b|PER_CHECKLISTS_B]] — 18 atributos (16 BICC)
- [[per_checklists_tl|PER_CHECKLISTS_TL]] — 7 atributos (5 BICC)
- [[per_checklist_contacts|PER_CHECKLIST_CONTACTS]] — 14 atributos (5 BICC)
- [[per_checklist_contents|PER_CHECKLIST_CONTENTS]] — 72 atributos (12 BICC)
- [[per_chk_content_defns_b|PER_CHK_CONTENT_DEFNS_B]] — 132 atributos (60 BICC)
- [[per_chk_content_defns_tl|PER_CHK_CONTENT_DEFNS_TL]] — 78 atributos (12 BICC)
- [[per_tasks_in_checklist_b|PER_TASKS_IN_CHECKLIST_B]] — 136 atributos (1 PKs, 23 BICC)
- [[per_tasks_in_checklist_tl|PER_TASKS_IN_CHECKLIST_TL]] — 17 atributos (5 BICC)
- [[per_task_dependencies|PER_TASK_DEPENDENCIES]] — 12 atributos (2 BICC)
- [[per_task_notifications|PER_TASK_NOTIFICATIONS]] — 52 atributos (12 BICC)
- [[per_users|PER_USERS]] — 4 atributos (1 BICC)

---

## ⚙️ Atributos

### [[ben_eligy_prfl|BEN_ELIGY_PRFL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EligibilityProfilePEO1EligyPrflId | ELIGY_PRFL_ID | — | — |
| 2 | EligibilityProfilePEO1Name | NAME | — | ✅ |
| 3 | EligibilityProfilePEOEligyPrflId | ELIGY_PRFL_ID | — | — |
| 4 | EligibilityProfilePEOName | NAME | — | ✅ |

### [[hrq_questionnaires_tl|HRQ_QUESTIONNAIRES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QuestionnaireTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | QuestionnaireTranslationPEOLanguage | LANGUAGE | — | — |
| 3 | QuestionnaireTranslationPEOName | NAME | — | ✅ |
| 4 | QuestionnaireTranslationPEOQstnrVersionNum | QSTNR_VERSION_NUM | — | — |
| 5 | QuestionnaireTranslationPEOQuestionnaireId | QUESTIONNAIRE_ID | — | — |

### [[hr_document_types_tl|HR_DOCUMENT_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DocumentTypesTranslationPEODocumentType | DOCUMENT_TYPE | — | ✅ |
| 2 | DocumentTypesTranslationPEODocumentTypeId | DOCUMENT_TYPE_ID | — | — |
| 3 | DocumentTypesTranslationPEOLanguage | LANGUAGE | — | — |

### [[per_actions_b|PER_ACTIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionsPEOActionCode | ACTION_CODE | — | — |
| 2 | ActionsPEOActionId | ACTION_ID | — | — |
| 3 | ActionsPEOActionTypeCode | ACTION_TYPE_CODE | — | — |
| 4 | ActionsPEOActionTypeId | ACTION_TYPE_ID | — | — |

### [[per_actions_tl|PER_ACTIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionTranslationPEOActionId | ACTION_ID | — | — |
| 2 | ActionTranslationPEOLanguage | LANGUAGE | — | — |
| 3 | ActionTranslationPEOPEOActionName | ACTION_NAME | — | ✅ |

### [[per_checklists_b|PER_CHECKLISTS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChecklistTemplatePEOActiveInactiveFlag | ACTIVE_INACTIVE_FLAG | — | ✅ |
| 2 | ChecklistTemplatePEOAllocatedOn | ALLOCATED_ON | — | ✅ |
| 3 | ChecklistTemplatePEOChecklistCategory | CHECKLIST_CATEGORY | — | ✅ |
| 4 | ChecklistTemplatePEOChecklistCode | CHECKLIST_CODE | — | ✅ |
| 5 | ChecklistTemplatePEOChecklistId | CHECKLIST_ID | — | — |
| 6 | ChecklistTemplatePEOCompletedOn | COMPLETED_ON | — | ✅ |
| 7 | ChecklistTemplatePEOCompletionOffsetDays | COMPLETION_OFFSET_DAYS | — | ✅ |
| 8 | ChecklistTemplatePEOCreatedBy | CREATED_BY | — | ✅ |
| 9 | ChecklistTemplatePEOCreationDate | CREATION_DATE | — | ✅ |
| 10 | ChecklistTemplatePEODateFrom | DATE_FROM | — | ✅ |
| 11 | ChecklistTemplatePEODateTo | DATE_TO | — | ✅ |
| 12 | ChecklistTemplatePEOEligibilityProfileId | ELIGIBILITY_PROFILE_ID | — | ✅ |
| 13 | ChecklistTemplatePEOEventReasonId | EVENT_REASON_ID | — | — |
| 14 | ChecklistTemplatePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | ChecklistTemplatePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 16 | ChecklistTemplatePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 17 | ChecklistTemplatePEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 18 | ChecklistTemplatePEOOffsetDays | OFFSET_DAYS | — | ✅ |

### [[per_checklists_tl|PER_CHECKLISTS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChecklistTemplateTranslationPEOChecklistDetails | CHECKLIST_DETAILS | — | ✅ |
| 2 | ChecklistTemplateTranslationPEOChecklistId | CHECKLIST_ID | — | — |
| 3 | ChecklistTemplateTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | ChecklistTemplateTranslationPEOLanguage | LANGUAGE | — | — |
| 5 | ChecklistTemplateTranslationPEOMessageText | MESSAGE_TEXT | — | ✅ |
| 6 | ChecklistTemplateTranslationPEOMessageTitle | MESSAGE_TITLE | — | ✅ |
| 7 | ChecklistTemplateTranslationPEOName | NAME | — | ✅ |

### [[per_checklist_contacts|PER_CHECKLIST_CONTACTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChecklistContactsPEOAdhocUserGuid | ADHOC_USER_GUID | — | ✅ |
| 2 | ChecklistContactsPEOChecklistContactId | CHECKLIST_CONTACT_ID | — | — |
| 3 | ChecklistContactsPEOChecklistId | CHECKLIST_ID | — | — |
| 4 | ChecklistContactsPEOContactTitleCode | CONTACT_TITLE_CODE | — | ✅ |
| 5 | ChecklistContactsPEOContactType | CONTACT_TYPE | — | ✅ |
| 6 | ChecklistContactsPEOCreatedBy | CREATED_BY | — | — |
| 7 | ChecklistContactsPEOCreationDate | CREATION_DATE | — | — |
| 8 | ChecklistContactsPEOCustomContact | CUSTOM_CONTACT | — | ✅ |
| 9 | ChecklistContactsPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 10 | ChecklistContactsPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 11 | ChecklistContactsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | ChecklistContactsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | ChecklistContactsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | ChecklistContactsPEOResponsibilityType | RESPONSIBILITY_TYPE | — | ✅ |

### [[per_checklist_contents|PER_CHECKLIST_CONTENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChecklistContentsPEO1ChecklistContentId | CHECKLIST_CONTENT_ID | — | — |
| 2 | ChecklistContentsPEO1ChecklistId | CHECKLIST_ID | — | — |
| 3 | ChecklistContentsPEO1ChkContentDefnId | CHK_CONTENT_DEFN_ID | — | — |
| 4 | ChecklistContentsPEO1ContentType | CONTENT_TYPE | — | ✅ |
| 5 | ChecklistContentsPEO1CreatedBy | CREATED_BY | — | — |
| 6 | ChecklistContentsPEO1CreationDate | CREATION_DATE | — | — |
| 7 | ChecklistContentsPEO1EnterpriseId | ENTERPRISE_ID | — | — |
| 8 | ChecklistContentsPEO1LastUpdateDate | LAST_UPDATE_DATE | — | — |
| 9 | ChecklistContentsPEO1LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | ChecklistContentsPEO1LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | ChecklistContentsPEO1ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | ChecklistContentsPEO1Sequence | SEQUENCE | — | ✅ |
| 13 | ChecklistContentsPEO2ChecklistContentId | CHECKLIST_CONTENT_ID | — | — |
| 14 | ChecklistContentsPEO2ChecklistId | CHECKLIST_ID | — | — |
| 15 | ChecklistContentsPEO2ChkContentDefnId | CHK_CONTENT_DEFN_ID | — | — |
| 16 | ChecklistContentsPEO2ContentType | CONTENT_TYPE | — | ✅ |
| 17 | ChecklistContentsPEO2CreatedBy | CREATED_BY | — | — |
| 18 | ChecklistContentsPEO2CreationDate | CREATION_DATE | — | — |
| 19 | ChecklistContentsPEO2EnterpriseId | ENTERPRISE_ID | — | — |
| 20 | ChecklistContentsPEO2LastUpdateDate | LAST_UPDATE_DATE | — | — |
| 21 | ChecklistContentsPEO2LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 22 | ChecklistContentsPEO2LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 23 | ChecklistContentsPEO2ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 24 | ChecklistContentsPEO2Sequence | SEQUENCE | — | ✅ |
| 25 | ChecklistContentsPEO3ChecklistContentId | CHECKLIST_CONTENT_ID | — | — |
| 26 | ChecklistContentsPEO3ChecklistId | CHECKLIST_ID | — | — |
| 27 | ChecklistContentsPEO3ChkContentDefnId | CHK_CONTENT_DEFN_ID | — | — |
| 28 | ChecklistContentsPEO3ContentType | CONTENT_TYPE | — | ✅ |
| 29 | ChecklistContentsPEO3CreatedBy | CREATED_BY | — | — |
| 30 | ChecklistContentsPEO3CreationDate | CREATION_DATE | — | — |
| 31 | ChecklistContentsPEO3EnterpriseId | ENTERPRISE_ID | — | — |
| 32 | ChecklistContentsPEO3LastUpdateDate | LAST_UPDATE_DATE | — | — |
| 33 | ChecklistContentsPEO3LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 34 | ChecklistContentsPEO3LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 35 | ChecklistContentsPEO3ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 36 | ChecklistContentsPEO3Sequence | SEQUENCE | — | ✅ |
| 37 | ChecklistContentsPEO4ChecklistContentId | CHECKLIST_CONTENT_ID | — | — |
| 38 | ChecklistContentsPEO4ChecklistId | CHECKLIST_ID | — | — |
| 39 | ChecklistContentsPEO4ChkContentDefnId | CHK_CONTENT_DEFN_ID | — | — |
| 40 | ChecklistContentsPEO4ContentType | CONTENT_TYPE | — | ✅ |
| 41 | ChecklistContentsPEO4CreatedBy | CREATED_BY | — | — |
| 42 | ChecklistContentsPEO4CreationDate | CREATION_DATE | — | — |
| 43 | ChecklistContentsPEO4EnterpriseId | ENTERPRISE_ID | — | — |
| 44 | ChecklistContentsPEO4LastUpdateDate | LAST_UPDATE_DATE | — | — |
| 45 | ChecklistContentsPEO4LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 46 | ChecklistContentsPEO4LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 47 | ChecklistContentsPEO4ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 48 | ChecklistContentsPEO4Sequence | SEQUENCE | — | ✅ |
| 49 | ChecklistContentsPEO5ChecklistContentId | CHECKLIST_CONTENT_ID | — | — |
| 50 | ChecklistContentsPEO5ChecklistId | CHECKLIST_ID | — | — |
| 51 | ChecklistContentsPEO5ChkContentDefnId | CHK_CONTENT_DEFN_ID | — | — |
| 52 | ChecklistContentsPEO5ContentType | CONTENT_TYPE | — | ✅ |
| 53 | ChecklistContentsPEO5CreatedBy | CREATED_BY | — | — |
| 54 | ChecklistContentsPEO5CreationDate | CREATION_DATE | — | — |
| 55 | ChecklistContentsPEO5EnterpriseId | ENTERPRISE_ID | — | — |
| 56 | ChecklistContentsPEO5LastUpdateDate | LAST_UPDATE_DATE | — | — |
| 57 | ChecklistContentsPEO5LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 58 | ChecklistContentsPEO5LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 59 | ChecklistContentsPEO5ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 60 | ChecklistContentsPEO5Sequence | SEQUENCE | — | ✅ |
| 61 | ChecklistContentsPEOChecklistContentId | CHECKLIST_CONTENT_ID | — | — |
| 62 | ChecklistContentsPEOChecklistId | CHECKLIST_ID | — | — |
| 63 | ChecklistContentsPEOChkContentDefnId | CHK_CONTENT_DEFN_ID | — | — |
| 64 | ChecklistContentsPEOContentType | CONTENT_TYPE | — | ✅ |
| 65 | ChecklistContentsPEOCreatedBy | CREATED_BY | — | — |
| 66 | ChecklistContentsPEOCreationDate | CREATION_DATE | — | — |
| 67 | ChecklistContentsPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 68 | ChecklistContentsPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 69 | ChecklistContentsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 70 | ChecklistContentsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 71 | ChecklistContentsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 72 | ChecklistContentsPEOSequence | SEQUENCE | — | ✅ |

### [[per_chk_content_defns_b|PER_CHK_CONTENT_DEFNS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChecklistContentDefnPEO1ChkContentDefnId | CHK_CONTENT_DEFN_ID | — | — |
| 2 | ChecklistContentDefnPEO1ContentCategory | CONTENT_CATEGORY | — | ✅ |
| 3 | ChecklistContentDefnPEO1ContentDefnCode | CONTENT_DEFN_CODE | — | — |
| 4 | ChecklistContentDefnPEO1ContentSubtype | CONTENT_SUBTYPE | — | ✅ |
| 5 | ChecklistContentDefnPEO1ContentType | CONTENT_TYPE | — | — |
| 6 | ChecklistContentDefnPEO1ContentUrl | CONTENT_URL | — | ✅ |
| 7 | ChecklistContentDefnPEO1CreatedBy | CREATED_BY | — | — |
| 8 | ChecklistContentDefnPEO1CreationDate | CREATION_DATE | — | — |
| 9 | ChecklistContentDefnPEO1EmbeddedContent | EMBEDDED_CONTENT | — | — |
| 10 | ChecklistContentDefnPEO1EmbeddedContentType | EMBEDDED_CONTENT_TYPE | — | — |
| 11 | ChecklistContentDefnPEO1EnterpriseId | ENTERPRISE_ID | — | — |
| 12 | ChecklistContentDefnPEO1EventDate | EVENT_DATE | — | ✅ |
| 13 | ChecklistContentDefnPEO1EventLocation | EVENT_LOCATION | — | ✅ |
| 14 | ChecklistContentDefnPEO1EventOffset | EVENT_OFFSET | — | ✅ |
| 15 | ChecklistContentDefnPEO1EventTime | EVENT_TIME | — | ✅ |
| 16 | ChecklistContentDefnPEO1HtmlContent | HTML_CONTENT | — | ✅ |
| 17 | ChecklistContentDefnPEO1ImageUrl | IMAGE_URL | — | ✅ |
| 18 | ChecklistContentDefnPEO1LastUpdateDate | LAST_UPDATE_DATE | — | — |
| 19 | ChecklistContentDefnPEO1LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 20 | ChecklistContentDefnPEO1LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 21 | ChecklistContentDefnPEO1ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 22 | ChecklistContentDefnPEO1Status | STATUS | — | ✅ |
| 23 | ChecklistContentDefnPEO2ChkContentDefnId | CHK_CONTENT_DEFN_ID | — | — |
| 24 | ChecklistContentDefnPEO2ContentCategory | CONTENT_CATEGORY | — | ✅ |
| 25 | ChecklistContentDefnPEO2ContentDefnCode | CONTENT_DEFN_CODE | — | — |
| 26 | ChecklistContentDefnPEO2ContentSubtype | CONTENT_SUBTYPE | — | ✅ |
| 27 | ChecklistContentDefnPEO2ContentType | CONTENT_TYPE | — | — |
| 28 | ChecklistContentDefnPEO2ContentUrl | CONTENT_URL | — | ✅ |
| 29 | ChecklistContentDefnPEO2CreatedBy | CREATED_BY | — | — |
| 30 | ChecklistContentDefnPEO2CreationDate | CREATION_DATE | — | — |
| 31 | ChecklistContentDefnPEO2EmbeddedContent | EMBEDDED_CONTENT | — | — |
| 32 | ChecklistContentDefnPEO2EmbeddedContentType | EMBEDDED_CONTENT_TYPE | — | — |
| 33 | ChecklistContentDefnPEO2EnterpriseId | ENTERPRISE_ID | — | — |
| 34 | ChecklistContentDefnPEO2EventDate | EVENT_DATE | — | ✅ |
| 35 | ChecklistContentDefnPEO2EventLocation | EVENT_LOCATION | — | ✅ |
| 36 | ChecklistContentDefnPEO2EventOffset | EVENT_OFFSET | — | ✅ |
| 37 | ChecklistContentDefnPEO2EventTime | EVENT_TIME | — | ✅ |
| 38 | ChecklistContentDefnPEO2HtmlContent | HTML_CONTENT | — | ✅ |
| 39 | ChecklistContentDefnPEO2ImageUrl | IMAGE_URL | — | ✅ |
| 40 | ChecklistContentDefnPEO2LastUpdateDate | LAST_UPDATE_DATE | — | — |
| 41 | ChecklistContentDefnPEO2LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 42 | ChecklistContentDefnPEO2LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 43 | ChecklistContentDefnPEO2ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 44 | ChecklistContentDefnPEO2Status | STATUS | — | ✅ |
| 45 | ChecklistContentDefnPEO3ChkContentDefnId | CHK_CONTENT_DEFN_ID | — | — |
| 46 | ChecklistContentDefnPEO3ContentCategory | CONTENT_CATEGORY | — | ✅ |
| 47 | ChecklistContentDefnPEO3ContentDefnCode | CONTENT_DEFN_CODE | — | — |
| 48 | ChecklistContentDefnPEO3ContentSubtype | CONTENT_SUBTYPE | — | ✅ |
| 49 | ChecklistContentDefnPEO3ContentType | CONTENT_TYPE | — | — |
| 50 | ChecklistContentDefnPEO3ContentUrl | CONTENT_URL | — | ✅ |
| 51 | ChecklistContentDefnPEO3CreatedBy | CREATED_BY | — | — |
| 52 | ChecklistContentDefnPEO3CreationDate | CREATION_DATE | — | — |
| 53 | ChecklistContentDefnPEO3EmbeddedContent | EMBEDDED_CONTENT | — | — |
| 54 | ChecklistContentDefnPEO3EmbeddedContentType | EMBEDDED_CONTENT_TYPE | — | — |
| 55 | ChecklistContentDefnPEO3EnterpriseId | ENTERPRISE_ID | — | — |
| 56 | ChecklistContentDefnPEO3EventDate | EVENT_DATE | — | ✅ |
| 57 | ChecklistContentDefnPEO3EventLocation | EVENT_LOCATION | — | ✅ |
| 58 | ChecklistContentDefnPEO3EventOffset | EVENT_OFFSET | — | ✅ |
| 59 | ChecklistContentDefnPEO3EventTime | EVENT_TIME | — | ✅ |
| 60 | ChecklistContentDefnPEO3HtmlContent | HTML_CONTENT | — | ✅ |
| 61 | ChecklistContentDefnPEO3ImageUrl | IMAGE_URL | — | ✅ |
| 62 | ChecklistContentDefnPEO3LastUpdateDate | LAST_UPDATE_DATE | — | — |
| 63 | ChecklistContentDefnPEO3LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 64 | ChecklistContentDefnPEO3LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 65 | ChecklistContentDefnPEO3ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 66 | ChecklistContentDefnPEO3Status | STATUS | — | ✅ |
| 67 | ChecklistContentDefnPEO4ChkContentDefnId | CHK_CONTENT_DEFN_ID | — | — |
| 68 | ChecklistContentDefnPEO4ContentCategory | CONTENT_CATEGORY | — | ✅ |
| 69 | ChecklistContentDefnPEO4ContentDefnCode | CONTENT_DEFN_CODE | — | — |
| 70 | ChecklistContentDefnPEO4ContentSubtype | CONTENT_SUBTYPE | — | ✅ |
| 71 | ChecklistContentDefnPEO4ContentType | CONTENT_TYPE | — | — |
| 72 | ChecklistContentDefnPEO4ContentUrl | CONTENT_URL | — | ✅ |
| 73 | ChecklistContentDefnPEO4CreatedBy | CREATED_BY | — | — |
| 74 | ChecklistContentDefnPEO4CreationDate | CREATION_DATE | — | — |
| 75 | ChecklistContentDefnPEO4EmbeddedContent | EMBEDDED_CONTENT | — | — |
| 76 | ChecklistContentDefnPEO4EmbeddedContentType | EMBEDDED_CONTENT_TYPE | — | — |
| 77 | ChecklistContentDefnPEO4EnterpriseId | ENTERPRISE_ID | — | — |
| 78 | ChecklistContentDefnPEO4EventDate | EVENT_DATE | — | ✅ |
| 79 | ChecklistContentDefnPEO4EventLocation | EVENT_LOCATION | — | ✅ |
| 80 | ChecklistContentDefnPEO4EventOffset | EVENT_OFFSET | — | ✅ |
| 81 | ChecklistContentDefnPEO4EventTime | EVENT_TIME | — | ✅ |
| 82 | ChecklistContentDefnPEO4HtmlContent | HTML_CONTENT | — | ✅ |
| 83 | ChecklistContentDefnPEO4ImageUrl | IMAGE_URL | — | ✅ |
| 84 | ChecklistContentDefnPEO4LastUpdateDate | LAST_UPDATE_DATE | — | — |
| 85 | ChecklistContentDefnPEO4LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 86 | ChecklistContentDefnPEO4LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 87 | ChecklistContentDefnPEO4ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 88 | ChecklistContentDefnPEO4Status | STATUS | — | ✅ |
| 89 | ChecklistContentDefnPEO5ChkContentDefnId | CHK_CONTENT_DEFN_ID | — | — |
| 90 | ChecklistContentDefnPEO5ContentCategory | CONTENT_CATEGORY | — | ✅ |
| 91 | ChecklistContentDefnPEO5ContentDefnCode | CONTENT_DEFN_CODE | — | — |
| 92 | ChecklistContentDefnPEO5ContentSubtype | CONTENT_SUBTYPE | — | ✅ |
| 93 | ChecklistContentDefnPEO5ContentType | CONTENT_TYPE | — | — |
| 94 | ChecklistContentDefnPEO5ContentUrl | CONTENT_URL | — | ✅ |
| 95 | ChecklistContentDefnPEO5CreatedBy | CREATED_BY | — | — |
| 96 | ChecklistContentDefnPEO5CreationDate | CREATION_DATE | — | — |
| 97 | ChecklistContentDefnPEO5EmbeddedContent | EMBEDDED_CONTENT | — | — |
| 98 | ChecklistContentDefnPEO5EmbeddedContentType | EMBEDDED_CONTENT_TYPE | — | — |
| 99 | ChecklistContentDefnPEO5EnterpriseId | ENTERPRISE_ID | — | — |
| 100 | ChecklistContentDefnPEO5EventDate | EVENT_DATE | — | ✅ |
| 101 | ChecklistContentDefnPEO5EventLocation | EVENT_LOCATION | — | ✅ |
| 102 | ChecklistContentDefnPEO5EventOffset | EVENT_OFFSET | — | ✅ |
| 103 | ChecklistContentDefnPEO5EventTime | EVENT_TIME | — | ✅ |
| 104 | ChecklistContentDefnPEO5HtmlContent | HTML_CONTENT | — | ✅ |
| 105 | ChecklistContentDefnPEO5ImageUrl | IMAGE_URL | — | ✅ |
| 106 | ChecklistContentDefnPEO5LastUpdateDate | LAST_UPDATE_DATE | — | — |
| 107 | ChecklistContentDefnPEO5LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 108 | ChecklistContentDefnPEO5LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 109 | ChecklistContentDefnPEO5ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 110 | ChecklistContentDefnPEO5Status | STATUS | — | ✅ |
| 111 | ChecklistContentDefnPEOChkContentDefnId | CHK_CONTENT_DEFN_ID | — | — |
| 112 | ChecklistContentDefnPEOContentCategory | CONTENT_CATEGORY | — | ✅ |
| 113 | ChecklistContentDefnPEOContentDefnCode | CONTENT_DEFN_CODE | — | — |
| 114 | ChecklistContentDefnPEOContentSubtype | CONTENT_SUBTYPE | — | ✅ |
| 115 | ChecklistContentDefnPEOContentType | CONTENT_TYPE | — | — |
| 116 | ChecklistContentDefnPEOContentUrl | CONTENT_URL | — | ✅ |
| 117 | ChecklistContentDefnPEOCreatedBy | CREATED_BY | — | — |
| 118 | ChecklistContentDefnPEOCreationDate | CREATION_DATE | — | — |
| 119 | ChecklistContentDefnPEOEmbeddedContent | EMBEDDED_CONTENT | — | — |
| 120 | ChecklistContentDefnPEOEmbeddedContentType | EMBEDDED_CONTENT_TYPE | — | — |
| 121 | ChecklistContentDefnPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 122 | ChecklistContentDefnPEOEventDate | EVENT_DATE | — | ✅ |
| 123 | ChecklistContentDefnPEOEventLocation | EVENT_LOCATION | — | ✅ |
| 124 | ChecklistContentDefnPEOEventOffset | EVENT_OFFSET | — | ✅ |
| 125 | ChecklistContentDefnPEOEventTime | EVENT_TIME | — | ✅ |
| 126 | ChecklistContentDefnPEOHtmlContent | HTML_CONTENT | — | ✅ |
| 127 | ChecklistContentDefnPEOImageUrl | IMAGE_URL | — | ✅ |
| 128 | ChecklistContentDefnPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 129 | ChecklistContentDefnPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 130 | ChecklistContentDefnPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 131 | ChecklistContentDefnPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 132 | ChecklistContentDefnPEOStatus | STATUS | — | ✅ |

### [[per_chk_content_defns_tl|PER_CHK_CONTENT_DEFNS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChecklistContentDefnTranslat1ChkContentDefnId | CHK_CONTENT_DEFN_ID | — | — |
| 2 | ChecklistContentDefnTranslat1ContentDetails | CONTENT_DETAILS | — | — |
| 3 | ChecklistContentDefnTranslat1CreatedBy | CREATED_BY | — | — |
| 4 | ChecklistContentDefnTranslat1CreationDate | CREATION_DATE | — | — |
| 5 | ChecklistContentDefnTranslat1Description | DESCRIPTION | — | ✅ |
| 6 | ChecklistContentDefnTranslat1EnterpriseId | ENTERPRISE_ID | — | — |
| 7 | ChecklistContentDefnTranslat1Language | LANGUAGE | — | — |
| 8 | ChecklistContentDefnTranslat1LastUpdateDate | LAST_UPDATE_DATE | — | — |
| 9 | ChecklistContentDefnTranslat1LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | ChecklistContentDefnTranslat1LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | ChecklistContentDefnTranslat1ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | ChecklistContentDefnTranslat1SourceLang | SOURCE_LANG | — | — |
| 13 | ChecklistContentDefnTranslat1Title | TITLE | — | ✅ |
| 14 | ChecklistContentDefnTranslat2ChkContentDefnId | CHK_CONTENT_DEFN_ID | — | — |
| 15 | ChecklistContentDefnTranslat2ContentDetails | CONTENT_DETAILS | — | — |
| 16 | ChecklistContentDefnTranslat2CreatedBy | CREATED_BY | — | — |
| 17 | ChecklistContentDefnTranslat2CreationDate | CREATION_DATE | — | — |
| 18 | ChecklistContentDefnTranslat2Description | DESCRIPTION | — | ✅ |
| 19 | ChecklistContentDefnTranslat2EnterpriseId | ENTERPRISE_ID | — | — |
| 20 | ChecklistContentDefnTranslat2Language | LANGUAGE | — | — |
| 21 | ChecklistContentDefnTranslat2LastUpdateDate | LAST_UPDATE_DATE | — | — |
| 22 | ChecklistContentDefnTranslat2LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 23 | ChecklistContentDefnTranslat2LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 24 | ChecklistContentDefnTranslat2ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 25 | ChecklistContentDefnTranslat2SourceLang | SOURCE_LANG | — | — |
| 26 | ChecklistContentDefnTranslat2Title | TITLE | — | ✅ |
| 27 | ChecklistContentDefnTranslat3ChkContentDefnId | CHK_CONTENT_DEFN_ID | — | — |
| 28 | ChecklistContentDefnTranslat3ContentDetails | CONTENT_DETAILS | — | — |
| 29 | ChecklistContentDefnTranslat3CreatedBy | CREATED_BY | — | — |
| 30 | ChecklistContentDefnTranslat3CreationDate | CREATION_DATE | — | — |
| 31 | ChecklistContentDefnTranslat3Description | DESCRIPTION | — | ✅ |
| 32 | ChecklistContentDefnTranslat3EnterpriseId | ENTERPRISE_ID | — | — |
| 33 | ChecklistContentDefnTranslat3Language | LANGUAGE | — | — |
| 34 | ChecklistContentDefnTranslat3LastUpdateDate | LAST_UPDATE_DATE | — | — |
| 35 | ChecklistContentDefnTranslat3LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 36 | ChecklistContentDefnTranslat3LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 37 | ChecklistContentDefnTranslat3ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 38 | ChecklistContentDefnTranslat3SourceLang | SOURCE_LANG | — | — |
| 39 | ChecklistContentDefnTranslat3Title | TITLE | — | ✅ |
| 40 | ChecklistContentDefnTranslat4ChkContentDefnId | CHK_CONTENT_DEFN_ID | — | — |
| 41 | ChecklistContentDefnTranslat4ContentDetails | CONTENT_DETAILS | — | — |
| 42 | ChecklistContentDefnTranslat4CreatedBy | CREATED_BY | — | — |
| 43 | ChecklistContentDefnTranslat4CreationDate | CREATION_DATE | — | — |
| 44 | ChecklistContentDefnTranslat4Description | DESCRIPTION | — | ✅ |
| 45 | ChecklistContentDefnTranslat4EnterpriseId | ENTERPRISE_ID | — | — |
| 46 | ChecklistContentDefnTranslat4Language | LANGUAGE | — | — |
| 47 | ChecklistContentDefnTranslat4LastUpdateDate | LAST_UPDATE_DATE | — | — |
| 48 | ChecklistContentDefnTranslat4LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 49 | ChecklistContentDefnTranslat4LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 50 | ChecklistContentDefnTranslat4ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 51 | ChecklistContentDefnTranslat4SourceLang | SOURCE_LANG | — | — |
| 52 | ChecklistContentDefnTranslat4Title | TITLE | — | ✅ |
| 53 | ChecklistContentDefnTranslat5ChkContentDefnId | CHK_CONTENT_DEFN_ID | — | — |
| 54 | ChecklistContentDefnTranslat5ContentDetails | CONTENT_DETAILS | — | — |
| 55 | ChecklistContentDefnTranslat5CreatedBy | CREATED_BY | — | — |
| 56 | ChecklistContentDefnTranslat5CreationDate | CREATION_DATE | — | — |
| 57 | ChecklistContentDefnTranslat5Description | DESCRIPTION | — | ✅ |
| 58 | ChecklistContentDefnTranslat5EnterpriseId | ENTERPRISE_ID | — | — |
| 59 | ChecklistContentDefnTranslat5Language | LANGUAGE | — | — |
| 60 | ChecklistContentDefnTranslat5LastUpdateDate | LAST_UPDATE_DATE | — | — |
| 61 | ChecklistContentDefnTranslat5LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 62 | ChecklistContentDefnTranslat5LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 63 | ChecklistContentDefnTranslat5ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 64 | ChecklistContentDefnTranslat5SourceLang | SOURCE_LANG | — | — |
| 65 | ChecklistContentDefnTranslat5Title | TITLE | — | ✅ |
| 66 | ChecklistContentDefnTranslatChkContentDefnId | CHK_CONTENT_DEFN_ID | — | — |
| 67 | ChecklistContentDefnTranslatContentDetails | CONTENT_DETAILS | — | — |
| 68 | ChecklistContentDefnTranslatCreatedBy | CREATED_BY | — | — |
| 69 | ChecklistContentDefnTranslatCreationDate | CREATION_DATE | — | — |
| 70 | ChecklistContentDefnTranslatDescription | DESCRIPTION | — | ✅ |
| 71 | ChecklistContentDefnTranslatEnterpriseId | ENTERPRISE_ID | — | — |
| 72 | ChecklistContentDefnTranslatLanguage | LANGUAGE | — | — |
| 73 | ChecklistContentDefnTranslatLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 74 | ChecklistContentDefnTranslatLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 75 | ChecklistContentDefnTranslatLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 76 | ChecklistContentDefnTranslatObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 77 | ChecklistContentDefnTranslatSourceLang | SOURCE_LANG | — | — |
| 78 | ChecklistContentDefnTranslatTitle | TITLE | — | ✅ |

### [[per_tasks_in_checklist_b|PER_TASKS_IN_CHECKLIST_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChecklistTaskTemplatePEOActionType | ACTION_TYPE | — | ✅ |
| 2 | ChecklistTaskTemplatePEOActiveInactiveFlag | ACTIVE_INACTIVE_FLAG | — | ✅ |
| 3 | ChecklistTaskTemplatePEOAllowAllcTaskCreate | ALLOW_ALLC_TASK_CREATE | — | — |
| 4 | ChecklistTaskTemplatePEOAllowAllcTaskDelete | ALLOW_ALLC_TASK_DELETE | — | — |
| 5 | ChecklistTaskTemplatePEOAllowAllcTaskUpdate | ALLOW_ALLC_TASK_UPDATE | — | — |
| 6 | ChecklistTaskTemplatePEOAmeAttributeIdentifier | AME_ATTRIBUTE_IDENTIFIER | — | — |
| 7 | ChecklistTaskTemplatePEOAttribute1 | ATTRIBUTE1 | — | — |
| 8 | ChecklistTaskTemplatePEOAttribute10 | ATTRIBUTE10 | — | — |
| 9 | ChecklistTaskTemplatePEOAttribute11 | ATTRIBUTE11 | — | — |
| 10 | ChecklistTaskTemplatePEOAttribute12 | ATTRIBUTE12 | — | — |
| 11 | ChecklistTaskTemplatePEOAttribute13 | ATTRIBUTE13 | — | — |
| 12 | ChecklistTaskTemplatePEOAttribute14 | ATTRIBUTE14 | — | — |
| 13 | ChecklistTaskTemplatePEOAttribute15 | ATTRIBUTE15 | — | — |
| 14 | ChecklistTaskTemplatePEOAttribute16 | ATTRIBUTE16 | — | — |
| 15 | ChecklistTaskTemplatePEOAttribute17 | ATTRIBUTE17 | — | — |
| 16 | ChecklistTaskTemplatePEOAttribute18 | ATTRIBUTE18 | — | — |
| 17 | ChecklistTaskTemplatePEOAttribute19 | ATTRIBUTE19 | — | — |
| 18 | ChecklistTaskTemplatePEOAttribute2 | ATTRIBUTE2 | — | — |
| 19 | ChecklistTaskTemplatePEOAttribute20 | ATTRIBUTE20 | — | — |
| 20 | ChecklistTaskTemplatePEOAttribute21 | ATTRIBUTE21 | — | — |
| 21 | ChecklistTaskTemplatePEOAttribute22 | ATTRIBUTE22 | — | — |
| 22 | ChecklistTaskTemplatePEOAttribute23 | ATTRIBUTE23 | — | — |
| 23 | ChecklistTaskTemplatePEOAttribute24 | ATTRIBUTE24 | — | — |
| 24 | ChecklistTaskTemplatePEOAttribute25 | ATTRIBUTE25 | — | — |
| 25 | ChecklistTaskTemplatePEOAttribute26 | ATTRIBUTE26 | — | — |
| 26 | ChecklistTaskTemplatePEOAttribute27 | ATTRIBUTE27 | — | — |
| 27 | ChecklistTaskTemplatePEOAttribute28 | ATTRIBUTE28 | — | — |
| 28 | ChecklistTaskTemplatePEOAttribute29 | ATTRIBUTE29 | — | — |
| 29 | ChecklistTaskTemplatePEOAttribute3 | ATTRIBUTE3 | — | — |
| 30 | ChecklistTaskTemplatePEOAttribute30 | ATTRIBUTE30 | — | — |
| 31 | ChecklistTaskTemplatePEOAttribute4 | ATTRIBUTE4 | — | — |
| 32 | ChecklistTaskTemplatePEOAttribute5 | ATTRIBUTE5 | — | — |
| 33 | ChecklistTaskTemplatePEOAttribute6 | ATTRIBUTE6 | — | — |
| 34 | ChecklistTaskTemplatePEOAttribute7 | ATTRIBUTE7 | — | — |
| 35 | ChecklistTaskTemplatePEOAttribute8 | ATTRIBUTE8 | — | — |
| 36 | ChecklistTaskTemplatePEOAttribute9 | ATTRIBUTE9 | — | — |
| 37 | ChecklistTaskTemplatePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 38 | ChecklistTaskTemplatePEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 39 | ChecklistTaskTemplatePEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 40 | ChecklistTaskTemplatePEOAttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 41 | ChecklistTaskTemplatePEOAttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 42 | ChecklistTaskTemplatePEOAttributeDate13 | ATTRIBUTE_DATE13 | — | — |
| 43 | ChecklistTaskTemplatePEOAttributeDate14 | ATTRIBUTE_DATE14 | — | — |
| 44 | ChecklistTaskTemplatePEOAttributeDate15 | ATTRIBUTE_DATE15 | — | — |
| 45 | ChecklistTaskTemplatePEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 46 | ChecklistTaskTemplatePEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 47 | ChecklistTaskTemplatePEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 48 | ChecklistTaskTemplatePEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 49 | ChecklistTaskTemplatePEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 50 | ChecklistTaskTemplatePEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 51 | ChecklistTaskTemplatePEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 52 | ChecklistTaskTemplatePEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 53 | ChecklistTaskTemplatePEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 54 | ChecklistTaskTemplatePEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 55 | ChecklistTaskTemplatePEOAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 56 | ChecklistTaskTemplatePEOAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 57 | ChecklistTaskTemplatePEOAttributeNumber13 | ATTRIBUTE_NUMBER13 | — | — |
| 58 | ChecklistTaskTemplatePEOAttributeNumber14 | ATTRIBUTE_NUMBER14 | — | — |
| 59 | ChecklistTaskTemplatePEOAttributeNumber15 | ATTRIBUTE_NUMBER15 | — | — |
| 60 | ChecklistTaskTemplatePEOAttributeNumber16 | ATTRIBUTE_NUMBER16 | — | — |
| 61 | ChecklistTaskTemplatePEOAttributeNumber17 | ATTRIBUTE_NUMBER17 | — | — |
| 62 | ChecklistTaskTemplatePEOAttributeNumber18 | ATTRIBUTE_NUMBER18 | — | — |
| 63 | ChecklistTaskTemplatePEOAttributeNumber19 | ATTRIBUTE_NUMBER19 | — | — |
| 64 | ChecklistTaskTemplatePEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 65 | ChecklistTaskTemplatePEOAttributeNumber20 | ATTRIBUTE_NUMBER20 | — | — |
| 66 | ChecklistTaskTemplatePEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 67 | ChecklistTaskTemplatePEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 68 | ChecklistTaskTemplatePEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 69 | ChecklistTaskTemplatePEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 70 | ChecklistTaskTemplatePEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 71 | ChecklistTaskTemplatePEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 72 | ChecklistTaskTemplatePEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 73 | ChecklistTaskTemplatePEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 74 | ChecklistTaskTemplatePEOChecklistId | CHECKLIST_ID | — | ✅ |
| 75 | ChecklistTaskTemplatePEOCreatedBy | CREATED_BY | — | ✅ |
| 76 | ChecklistTaskTemplatePEOCreationDate | CREATION_DATE | — | ✅ |
| 77 | ChecklistTaskTemplatePEODocumentTypeId | DOCUMENT_TYPE_ID | — | ✅ |
| 78 | ChecklistTaskTemplatePEOEligibilityObjectId | ELIGIBILITY_OBJECT_ID | — | — |
| 79 | ChecklistTaskTemplatePEOEligibilityProfileId | ELIGIBILITY_PROFILE_ID | — | ✅ |
| 80 | ChecklistTaskTemplatePEOEsignType | ESIGN_TYPE | — | ✅ |
| 81 | ChecklistTaskTemplatePEOExpiryAfterDays | EXPIRY_AFTER_DAYS | — | — |
| 82 | ChecklistTaskTemplatePEOGenerateAtomFeed | GENERATE_ATOM_FEED | — | — |
| 83 | ChecklistTaskTemplatePEOInformation1 | INFORMATION1 | — | — |
| 84 | ChecklistTaskTemplatePEOInformation10 | INFORMATION10 | — | — |
| 85 | ChecklistTaskTemplatePEOInformation11 | INFORMATION11 | — | — |
| 86 | ChecklistTaskTemplatePEOInformation12 | INFORMATION12 | — | — |
| 87 | ChecklistTaskTemplatePEOInformation13 | INFORMATION13 | — | — |
| 88 | ChecklistTaskTemplatePEOInformation14 | INFORMATION14 | — | — |
| 89 | ChecklistTaskTemplatePEOInformation15 | INFORMATION15 | — | — |
| 90 | ChecklistTaskTemplatePEOInformation16 | INFORMATION16 | — | — |
| 91 | ChecklistTaskTemplatePEOInformation17 | INFORMATION17 | — | — |
| 92 | ChecklistTaskTemplatePEOInformation18 | INFORMATION18 | — | — |
| 93 | ChecklistTaskTemplatePEOInformation19 | INFORMATION19 | — | — |
| 94 | ChecklistTaskTemplatePEOInformation2 | INFORMATION2 | — | — |
| 95 | ChecklistTaskTemplatePEOInformation20 | INFORMATION20 | — | — |
| 96 | ChecklistTaskTemplatePEOInformation21 | INFORMATION21 | — | — |
| 97 | ChecklistTaskTemplatePEOInformation22 | INFORMATION22 | — | — |
| 98 | ChecklistTaskTemplatePEOInformation23 | INFORMATION23 | — | — |
| 99 | ChecklistTaskTemplatePEOInformation24 | INFORMATION24 | — | — |
| 100 | ChecklistTaskTemplatePEOInformation25 | INFORMATION25 | — | — |
| 101 | ChecklistTaskTemplatePEOInformation26 | INFORMATION26 | — | — |
| 102 | ChecklistTaskTemplatePEOInformation27 | INFORMATION27 | — | — |
| 103 | ChecklistTaskTemplatePEOInformation28 | INFORMATION28 | — | — |
| 104 | ChecklistTaskTemplatePEOInformation29 | INFORMATION29 | — | — |
| 105 | ChecklistTaskTemplatePEOInformation3 | INFORMATION3 | — | — |
| 106 | ChecklistTaskTemplatePEOInformation30 | INFORMATION30 | — | — |
| 107 | ChecklistTaskTemplatePEOInformation4 | INFORMATION4 | — | — |
| 108 | ChecklistTaskTemplatePEOInformation5 | INFORMATION5 | — | — |
| 109 | ChecklistTaskTemplatePEOInformation6 | INFORMATION6 | — | — |
| 110 | ChecklistTaskTemplatePEOInformation7 | INFORMATION7 | — | — |
| 111 | ChecklistTaskTemplatePEOInformation8 | INFORMATION8 | — | — |
| 112 | ChecklistTaskTemplatePEOInformation9 | INFORMATION9 | — | — |
| 113 | ChecklistTaskTemplatePEOInformationCategory | INFORMATION_CATEGORY | — | — |
| 114 | ChecklistTaskTemplatePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 115 | ChecklistTaskTemplatePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 116 | ChecklistTaskTemplatePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 117 | ChecklistTaskTemplatePEOMandatoryFlag | MANDATORY_FLAG | — | ✅ |
| 118 | ChecklistTaskTemplatePEOMeetingTime | MEETING_TIME | — | — |
| 119 | ChecklistTaskTemplatePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 120 | ChecklistTaskTemplatePEOOwnerRespType | OWNER_RESP_TYPE | — | — |
| 121 | ChecklistTaskTemplatePEOQuestionnaireId | QUESTIONNAIRE_ID | — | ✅ |
| 122 | ChecklistTaskTemplatePEOReminderRecurrence | REMINDER_RECURRENCE | — | — |
| 123 | ChecklistTaskTemplatePEOReminderRelativeTo | REMINDER_RELATIVE_TO | — | — |
| 124 | ChecklistTaskTemplatePEOReportPath | REPORT_PATH | — | ✅ |
| 125 | ChecklistTaskTemplatePEOResponsibilityType | RESPONSIBILITY_TYPE | — | ✅ |
| 126 | ChecklistTaskTemplatePEOSignTemplate | SIGN_TEMPLATE | — | ✅ |
| 127 | ChecklistTaskTemplatePEOTargetDuration | TARGET_DURATION | — | ✅ |
| 128 | ChecklistTaskTemplatePEOTargetDurationUom | TARGET_DURATION_UOM | — | ✅ |
| 129 | ChecklistTaskTemplatePEOTaskActionCode | TASK_ACTION_CODE | — | — |
| 130 | ChecklistTaskTemplatePEOTaskCategory | TASK_CATEGORY | — | ✅ |
| 131 | ChecklistTaskTemplatePEOTaskConfiguration | TASK_CONFIGURATION | — | — |
| 132 | ChecklistTaskTemplatePEOTaskDelayDuration | TASK_DELAY_DURATION | — | ✅ |
| 133 | ChecklistTaskTemplatePEOTaskDelayDurationUom | TASK_DELAY_DURATION_UOM | — | ✅ |
| 134 | ChecklistTaskTemplatePEOTaskInChecklistCode | TASK_IN_CHECKLIST_CODE | — | ✅ |
| 135 | ChecklistTaskTemplatePEOTaskSequence | TASK_SEQUENCE | — | — |
| 136 | TaskInChecklistId | TASK_IN_CHECKLIST_ID | 🔑 | ✅ |

### [[per_tasks_in_checklist_tl|PER_TASKS_IN_CHECKLIST_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChecklistTaskTemplateTransla1ChecklistTaskName | CHECKLIST_TASK_NAME | — | ✅ |
| 2 | ChecklistTaskTemplateTransla1Language | LANGUAGE | — | — |
| 3 | ChecklistTaskTemplateTransla1TaskInChecklistId1 | TASK_IN_CHECKLIST_ID | — | — |
| 4 | ChecklistTaskTemplateTranslationPEOActionUrl | ACTION_URL | — | ✅ |
| 5 | ChecklistTaskTemplateTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 6 | ChecklistTaskTemplateTranslationPEOChecklistTaskName | CHECKLIST_TASK_NAME | — | ✅ |
| 7 | ChecklistTaskTemplateTranslationPEOCreatedBy | CREATED_BY | — | — |
| 8 | ChecklistTaskTemplateTranslationPEOCreationDate | CREATION_DATE | — | — |
| 9 | ChecklistTaskTemplateTranslationPEODescription | DESCRIPTION | — | ✅ |
| 10 | ChecklistTaskTemplateTranslationPEOLanguage | LANGUAGE | — | — |
| 11 | ChecklistTaskTemplateTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | ChecklistTaskTemplateTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | ChecklistTaskTemplateTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | ChecklistTaskTemplateTranslationPEOMeetingLocation | MEETING_LOCATION | — | — |
| 15 | ChecklistTaskTemplateTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | ChecklistTaskTemplateTranslationPEOSourceLang | SOURCE_LANG | — | — |
| 17 | ChecklistTaskTemplateTranslationPEOTaskInChecklistId | TASK_IN_CHECKLIST_ID | — | — |

### [[per_task_dependencies|PER_TASK_DEPENDENCIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChecklistTaskDependenciesPEOChecklistTaskDependenciesPEOTaskDependencyId | TASK_DEPENDENCY_ID | — | — |
| 2 | ChecklistTaskDependenciesPEOCreatedBy | CREATED_BY | — | — |
| 3 | ChecklistTaskDependenciesPEOCreationDate | CREATION_DATE | — | — |
| 4 | ChecklistTaskDependenciesPEODependencyType | DEPENDENCY_TYPE | — | ✅ |
| 5 | ChecklistTaskDependenciesPEODependentTaskInChecklistId | DEPENDENT_TASK_IN_CHECKLIST_ID | — | ✅ |
| 6 | ChecklistTaskDependenciesPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 7 | ChecklistTaskDependenciesPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 8 | ChecklistTaskDependenciesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ChecklistTaskDependenciesPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ChecklistTaskDependenciesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | ChecklistTaskDependenciesPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 12 | ChecklistTaskDependenciesPEOTaskInChecklistId | TASK_IN_CHECKLIST_ID | — | — |

### [[per_task_notifications|PER_TASK_NOTIFICATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChecklistTaskNotificationPEO1CreatedBy | CREATED_BY | — | — |
| 2 | ChecklistTaskNotificationPEO1CreationDate | CREATION_DATE | — | — |
| 3 | ChecklistTaskNotificationPEO1EnterpriseId | ENTERPRISE_ID | — | — |
| 4 | ChecklistTaskNotificationPEO1LastUpdateDate | LAST_UPDATE_DATE | — | — |
| 5 | ChecklistTaskNotificationPEO1LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | ChecklistTaskNotificationPEO1LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | ChecklistTaskNotificationPEO1NotifyOwner | NOTIFY_OWNER | — | ✅ |
| 8 | ChecklistTaskNotificationPEO1NotifyPerformer | NOTIFY_PERFORMER | — | ✅ |
| 9 | ChecklistTaskNotificationPEO1ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | ChecklistTaskNotificationPEO1SeedDataSource | SEED_DATA_SOURCE | — | — |
| 11 | ChecklistTaskNotificationPEO1TaskEvent | TASK_EVENT | — | ✅ |
| 12 | ChecklistTaskNotificationPEO1TaskInChecklistId | TASK_IN_CHECKLIST_ID | — | — |
| 13 | ChecklistTaskNotificationPEO1TaskNotificationId | TASK_NOTIFICATION_ID | — | — |
| 14 | ChecklistTaskNotificationPEO2CreatedBy | CREATED_BY | — | — |
| 15 | ChecklistTaskNotificationPEO2CreationDate | CREATION_DATE | — | — |
| 16 | ChecklistTaskNotificationPEO2EnterpriseId | ENTERPRISE_ID | — | — |
| 17 | ChecklistTaskNotificationPEO2LastUpdateDate | LAST_UPDATE_DATE | — | — |
| 18 | ChecklistTaskNotificationPEO2LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 19 | ChecklistTaskNotificationPEO2LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 20 | ChecklistTaskNotificationPEO2NotifyOwner | NOTIFY_OWNER | — | ✅ |
| 21 | ChecklistTaskNotificationPEO2NotifyPerformer | NOTIFY_PERFORMER | — | ✅ |
| 22 | ChecklistTaskNotificationPEO2ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 23 | ChecklistTaskNotificationPEO2SeedDataSource | SEED_DATA_SOURCE | — | — |
| 24 | ChecklistTaskNotificationPEO2TaskEvent | TASK_EVENT | — | ✅ |
| 25 | ChecklistTaskNotificationPEO2TaskInChecklistId | TASK_IN_CHECKLIST_ID | — | — |
| 26 | ChecklistTaskNotificationPEO2TaskNotificationId | TASK_NOTIFICATION_ID | — | — |
| 27 | ChecklistTaskNotificationPEO3CreatedBy | CREATED_BY | — | — |
| 28 | ChecklistTaskNotificationPEO3CreationDate | CREATION_DATE | — | — |
| 29 | ChecklistTaskNotificationPEO3EnterpriseId | ENTERPRISE_ID | — | — |
| 30 | ChecklistTaskNotificationPEO3LastUpdateDate | LAST_UPDATE_DATE | — | — |
| 31 | ChecklistTaskNotificationPEO3LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 32 | ChecklistTaskNotificationPEO3LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 33 | ChecklistTaskNotificationPEO3NotifyOwner | NOTIFY_OWNER | — | ✅ |
| 34 | ChecklistTaskNotificationPEO3NotifyPerformer | NOTIFY_PERFORMER | — | ✅ |
| 35 | ChecklistTaskNotificationPEO3ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 36 | ChecklistTaskNotificationPEO3SeedDataSource | SEED_DATA_SOURCE | — | — |
| 37 | ChecklistTaskNotificationPEO3TaskEvent | TASK_EVENT | — | ✅ |
| 38 | ChecklistTaskNotificationPEO3TaskInChecklistId | TASK_IN_CHECKLIST_ID | — | — |
| 39 | ChecklistTaskNotificationPEO3TaskNotificationId | TASK_NOTIFICATION_ID | — | — |
| 40 | ChecklistTaskNotificationPEOCreatedBy | CREATED_BY | — | — |
| 41 | ChecklistTaskNotificationPEOCreationDate | CREATION_DATE | — | — |
| 42 | ChecklistTaskNotificationPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 43 | ChecklistTaskNotificationPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 44 | ChecklistTaskNotificationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 45 | ChecklistTaskNotificationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 46 | ChecklistTaskNotificationPEONotifyOwner | NOTIFY_OWNER | — | ✅ |
| 47 | ChecklistTaskNotificationPEONotifyPerformer | NOTIFY_PERFORMER | — | ✅ |
| 48 | ChecklistTaskNotificationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 49 | ChecklistTaskNotificationPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 50 | ChecklistTaskNotificationPEOTaskEvent | TASK_EVENT | — | ✅ |
| 51 | ChecklistTaskNotificationPEOTaskInChecklistId | TASK_IN_CHECKLIST_ID | — | — |
| 52 | ChecklistTaskNotificationPEOTaskNotificationId | TASK_NOTIFICATION_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UsersPEO1ChecklistTaskAdhocUsername | USERNAME | — | — |
| 2 | UsersPEO1UserId | USER_ID | — | — |
| 3 | UsersPEOAdhocUserUserName | USERNAME | — | ✅ |
| 4 | UsersPEOUserId | USER_ID | — | — |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
