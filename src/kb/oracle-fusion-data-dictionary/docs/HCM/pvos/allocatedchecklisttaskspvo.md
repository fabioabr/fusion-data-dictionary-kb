---
id: DOC-HCM-PVO-AllocatedChecklistTasksPVO
doc_type: system-doc
title: "AllocatedChecklistTasksPVO — PVO Human Capital Management"
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
  - AllocatedChecklistTasksPVO
  - allocatedchecklisttaskspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AllocatedChecklistTasksPVO

## 📌 Visão Geral

Detalha tarefas individuais de checklists alocados, incluindo predecessoras e questionarios. Permite acompanhamento granular do progresso de cada tarefa.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.ChecklistAM.AllocatedChecklistTasksPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 493 | 12 | 1 | 110 | 22% |

---

## 🔗 Tabelas Relacionadas

- [[hrq_questionnaires_tl|HRQ_QUESTIONNAIRES_TL]] — 5 atributos (1 BICC)
- [[hr_document_types_tl|HR_DOCUMENT_TYPES_TL]] — 3 atributos (1 BICC)
- [[per_allocated_checklists|PER_ALLOCATED_CHECKLISTS]] — 119 atributos (18 BICC)
- [[per_allocated_checklists_tl|PER_ALLOCATED_CHECKLISTS_TL]] — 17 atributos (4 BICC)
- [[per_allocated_tasks|PER_ALLOCATED_TASKS]] — 173 atributos (1 PKs, 48 BICC)
- [[per_allocated_tasks_tl|PER_ALLOCATED_TASKS_TL]] — 21 atributos (6 BICC)
- [[per_alloc_chklst_contacts|PER_ALLOC_CHKLST_CONTACTS]] — 15 atributos (5 BICC)
- [[per_alloc_chklst_contents|PER_ALLOC_CHKLST_CONTENTS]] — 78 atributos (12 BICC)
- [[per_alloc_task_notifs|PER_ALLOC_TASK_NOTIFS]] — 52 atributos (12 BICC)
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 4 atributos (1 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 4 atributos (1 BICC)
- [[per_users|PER_USERS]] — 2 atributos (1 BICC)

---

## ⚙️ Atributos

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

### [[per_allocated_checklists|PER_ALLOCATED_CHECKLISTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AllocatedChecklistsPEOActionDate | ACTION_DATE | — | ✅ |
| 2 | AllocatedChecklistsPEOAllocatedChecklistId | ALLOCATED_CHECKLIST_ID | — | ✅ |
| 3 | AllocatedChecklistsPEOAllocationDate | ALLOCATION_DATE | — | ✅ |
| 4 | AllocatedChecklistsPEOAllocationDetails | ALLOCATION_DETAILS | — | ✅ |
| 5 | AllocatedChecklistsPEOAssignmentId | ASSIGNMENT_ID | — | — |
| 6 | AllocatedChecklistsPEOAttribute1 | ATTRIBUTE1 | — | — |
| 7 | AllocatedChecklistsPEOAttribute10 | ATTRIBUTE10 | — | — |
| 8 | AllocatedChecklistsPEOAttribute11 | ATTRIBUTE11 | — | — |
| 9 | AllocatedChecklistsPEOAttribute12 | ATTRIBUTE12 | — | — |
| 10 | AllocatedChecklistsPEOAttribute13 | ATTRIBUTE13 | — | — |
| 11 | AllocatedChecklistsPEOAttribute14 | ATTRIBUTE14 | — | — |
| 12 | AllocatedChecklistsPEOAttribute15 | ATTRIBUTE15 | — | — |
| 13 | AllocatedChecklistsPEOAttribute16 | ATTRIBUTE16 | — | — |
| 14 | AllocatedChecklistsPEOAttribute17 | ATTRIBUTE17 | — | — |
| 15 | AllocatedChecklistsPEOAttribute18 | ATTRIBUTE18 | — | — |
| 16 | AllocatedChecklistsPEOAttribute19 | ATTRIBUTE19 | — | — |
| 17 | AllocatedChecklistsPEOAttribute2 | ATTRIBUTE2 | — | — |
| 18 | AllocatedChecklistsPEOAttribute20 | ATTRIBUTE20 | — | — |
| 19 | AllocatedChecklistsPEOAttribute21 | ATTRIBUTE21 | — | — |
| 20 | AllocatedChecklistsPEOAttribute22 | ATTRIBUTE22 | — | — |
| 21 | AllocatedChecklistsPEOAttribute23 | ATTRIBUTE23 | — | — |
| 22 | AllocatedChecklistsPEOAttribute24 | ATTRIBUTE24 | — | — |
| 23 | AllocatedChecklistsPEOAttribute25 | ATTRIBUTE25 | — | — |
| 24 | AllocatedChecklistsPEOAttribute26 | ATTRIBUTE26 | — | — |
| 25 | AllocatedChecklistsPEOAttribute27 | ATTRIBUTE27 | — | — |
| 26 | AllocatedChecklistsPEOAttribute28 | ATTRIBUTE28 | — | — |
| 27 | AllocatedChecklistsPEOAttribute29 | ATTRIBUTE29 | — | — |
| 28 | AllocatedChecklistsPEOAttribute3 | ATTRIBUTE3 | — | — |
| 29 | AllocatedChecklistsPEOAttribute30 | ATTRIBUTE30 | — | — |
| 30 | AllocatedChecklistsPEOAttribute4 | ATTRIBUTE4 | — | — |
| 31 | AllocatedChecklistsPEOAttribute5 | ATTRIBUTE5 | — | — |
| 32 | AllocatedChecklistsPEOAttribute6 | ATTRIBUTE6 | — | — |
| 33 | AllocatedChecklistsPEOAttribute7 | ATTRIBUTE7 | — | — |
| 34 | AllocatedChecklistsPEOAttribute8 | ATTRIBUTE8 | — | — |
| 35 | AllocatedChecklistsPEOAttribute9 | ATTRIBUTE9 | — | — |
| 36 | AllocatedChecklistsPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 37 | AllocatedChecklistsPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 38 | AllocatedChecklistsPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 39 | AllocatedChecklistsPEOAttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 40 | AllocatedChecklistsPEOAttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 41 | AllocatedChecklistsPEOAttributeDate13 | ATTRIBUTE_DATE13 | — | — |
| 42 | AllocatedChecklistsPEOAttributeDate14 | ATTRIBUTE_DATE14 | — | — |
| 43 | AllocatedChecklistsPEOAttributeDate15 | ATTRIBUTE_DATE15 | — | — |
| 44 | AllocatedChecklistsPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 45 | AllocatedChecklistsPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 46 | AllocatedChecklistsPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 47 | AllocatedChecklistsPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 48 | AllocatedChecklistsPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 49 | AllocatedChecklistsPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 50 | AllocatedChecklistsPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 51 | AllocatedChecklistsPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 52 | AllocatedChecklistsPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 53 | AllocatedChecklistsPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 54 | AllocatedChecklistsPEOAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 55 | AllocatedChecklistsPEOAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 56 | AllocatedChecklistsPEOAttributeNumber13 | ATTRIBUTE_NUMBER13 | — | — |
| 57 | AllocatedChecklistsPEOAttributeNumber14 | ATTRIBUTE_NUMBER14 | — | — |
| 58 | AllocatedChecklistsPEOAttributeNumber15 | ATTRIBUTE_NUMBER15 | — | — |
| 59 | AllocatedChecklistsPEOAttributeNumber16 | ATTRIBUTE_NUMBER16 | — | — |
| 60 | AllocatedChecklistsPEOAttributeNumber17 | ATTRIBUTE_NUMBER17 | — | — |
| 61 | AllocatedChecklistsPEOAttributeNumber18 | ATTRIBUTE_NUMBER18 | — | — |
| 62 | AllocatedChecklistsPEOAttributeNumber19 | ATTRIBUTE_NUMBER19 | — | — |
| 63 | AllocatedChecklistsPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 64 | AllocatedChecklistsPEOAttributeNumber20 | ATTRIBUTE_NUMBER20 | — | — |
| 65 | AllocatedChecklistsPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 66 | AllocatedChecklistsPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 67 | AllocatedChecklistsPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 68 | AllocatedChecklistsPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 69 | AllocatedChecklistsPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 70 | AllocatedChecklistsPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 71 | AllocatedChecklistsPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 72 | AllocatedChecklistsPEOChecklistCategory | CHECKLIST_CATEGORY | — | ✅ |
| 73 | AllocatedChecklistsPEOChecklistId | CHECKLIST_ID | — | ✅ |
| 74 | AllocatedChecklistsPEOChecklistInstance | CHECKLIST_INSTANCE | — | ✅ |
| 75 | AllocatedChecklistsPEOChecklistStatus | CHECKLIST_STATUS | — | ✅ |
| 76 | AllocatedChecklistsPEOCompletedOn | COMPLETED_ON | — | ✅ |
| 77 | AllocatedChecklistsPEOCompletionDate | COMPLETION_DATE | — | ✅ |
| 78 | AllocatedChecklistsPEOCompletionOffsetDays | COMPLETION_OFFSET_DAYS | — | ✅ |
| 79 | AllocatedChecklistsPEOCreatedBy | CREATED_BY | — | ✅ |
| 80 | AllocatedChecklistsPEOCreationDate | CREATION_DATE | — | ✅ |
| 81 | AllocatedChecklistsPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 82 | AllocatedChecklistsPEOEventDate | EVENT_DATE | — | ✅ |
| 83 | AllocatedChecklistsPEOInformation1 | INFORMATION1 | — | — |
| 84 | AllocatedChecklistsPEOInformation10 | INFORMATION10 | — | — |
| 85 | AllocatedChecklistsPEOInformation11 | INFORMATION11 | — | — |
| 86 | AllocatedChecklistsPEOInformation12 | INFORMATION12 | — | — |
| 87 | AllocatedChecklistsPEOInformation13 | INFORMATION13 | — | — |
| 88 | AllocatedChecklistsPEOInformation14 | INFORMATION14 | — | — |
| 89 | AllocatedChecklistsPEOInformation15 | INFORMATION15 | — | — |
| 90 | AllocatedChecklistsPEOInformation16 | INFORMATION16 | — | — |
| 91 | AllocatedChecklistsPEOInformation17 | INFORMATION17 | — | — |
| 92 | AllocatedChecklistsPEOInformation18 | INFORMATION18 | — | — |
| 93 | AllocatedChecklistsPEOInformation19 | INFORMATION19 | — | — |
| 94 | AllocatedChecklistsPEOInformation2 | INFORMATION2 | — | — |
| 95 | AllocatedChecklistsPEOInformation20 | INFORMATION20 | — | — |
| 96 | AllocatedChecklistsPEOInformation21 | INFORMATION21 | — | — |
| 97 | AllocatedChecklistsPEOInformation22 | INFORMATION22 | — | — |
| 98 | AllocatedChecklistsPEOInformation23 | INFORMATION23 | — | — |
| 99 | AllocatedChecklistsPEOInformation24 | INFORMATION24 | — | — |
| 100 | AllocatedChecklistsPEOInformation25 | INFORMATION25 | — | — |
| 101 | AllocatedChecklistsPEOInformation26 | INFORMATION26 | — | — |
| 102 | AllocatedChecklistsPEOInformation27 | INFORMATION27 | — | — |
| 103 | AllocatedChecklistsPEOInformation28 | INFORMATION28 | — | — |
| 104 | AllocatedChecklistsPEOInformation29 | INFORMATION29 | — | — |
| 105 | AllocatedChecklistsPEOInformation3 | INFORMATION3 | — | — |
| 106 | AllocatedChecklistsPEOInformation30 | INFORMATION30 | — | — |
| 107 | AllocatedChecklistsPEOInformation4 | INFORMATION4 | — | — |
| 108 | AllocatedChecklistsPEOInformation5 | INFORMATION5 | — | — |
| 109 | AllocatedChecklistsPEOInformation6 | INFORMATION6 | — | — |
| 110 | AllocatedChecklistsPEOInformation7 | INFORMATION7 | — | — |
| 111 | AllocatedChecklistsPEOInformation8 | INFORMATION8 | — | — |
| 112 | AllocatedChecklistsPEOInformation9 | INFORMATION9 | — | — |
| 113 | AllocatedChecklistsPEOInformationCategory | INFORMATION_CATEGORY | — | — |
| 114 | AllocatedChecklistsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 115 | AllocatedChecklistsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 116 | AllocatedChecklistsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 117 | AllocatedChecklistsPEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 118 | AllocatedChecklistsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 119 | AllocatedChecklistsPEOPersonId | PERSON_ID | — | — |

### [[per_allocated_checklists_tl|PER_ALLOCATED_CHECKLISTS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AllocatedChecklistranslationAllocatedChecklistId | ALLOCATED_CHECKLIST_ID | — | — |
| 2 | AllocatedChecklistranslationBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | AllocatedChecklistranslationChecklistDetails | CHECKLIST_DETAILS | — | — |
| 4 | AllocatedChecklistranslationChecklistName | CHECKLIST_NAME | — | — |
| 5 | AllocatedChecklistranslationCreatedBy | CREATED_BY | — | — |
| 6 | AllocatedChecklistranslationCreationDate1 | CREATION_DATE | — | — |
| 7 | AllocatedChecklistranslationDescription | DESCRIPTION | — | — |
| 8 | AllocatedChecklistranslationLanguage | LANGUAGE | — | — |
| 9 | AllocatedChecklistranslationLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 10 | AllocatedChecklistranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | AllocatedChecklistranslationLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | AllocatedChecklistranslationMessageText | MESSAGE_TEXT | — | ✅ |
| 13 | AllocatedChecklistranslationMessageTitle | MESSAGE_TITLE | — | ✅ |
| 14 | AllocatedChecklistranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | AllocatedChecklistranslationSourceLang | SOURCE_LANG | — | — |
| 16 | AllocatedChecklistsPEOChecklistName | CHECKLIST_NAME | — | ✅ |
| 17 | AllocatedChecklistsPEODescription | DESCRIPTION | — | ✅ |

### [[per_allocated_tasks|PER_ALLOCATED_TASKS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AllocatedChecklistTasksPEOAbsAllocatedChecklistId | ABS_ALLOCATED_CHECKLIST_ID | — | — |
| 2 | AllocatedChecklistTasksPEOActionType | ACTION_TYPE | — | ✅ |
| 3 | AllocatedChecklistTasksPEOActualEndDate | ACTUAL_END_DATE | — | ✅ |
| 4 | AllocatedChecklistTasksPEOActualStartDate | ACTUAL_START_DATE | — | ✅ |
| 5 | AllocatedChecklistTasksPEOAllocatedChecklistId | ALLOCATED_CHECKLIST_ID | — | ✅ |
| 6 | AllocatedChecklistTasksPEOAttribute1 | ATTRIBUTE1 | — | — |
| 7 | AllocatedChecklistTasksPEOAttribute10 | ATTRIBUTE10 | — | — |
| 8 | AllocatedChecklistTasksPEOAttribute11 | ATTRIBUTE11 | — | — |
| 9 | AllocatedChecklistTasksPEOAttribute12 | ATTRIBUTE12 | — | — |
| 10 | AllocatedChecklistTasksPEOAttribute13 | ATTRIBUTE13 | — | — |
| 11 | AllocatedChecklistTasksPEOAttribute14 | ATTRIBUTE14 | — | — |
| 12 | AllocatedChecklistTasksPEOAttribute15 | ATTRIBUTE15 | — | — |
| 13 | AllocatedChecklistTasksPEOAttribute16 | ATTRIBUTE16 | — | — |
| 14 | AllocatedChecklistTasksPEOAttribute17 | ATTRIBUTE17 | — | — |
| 15 | AllocatedChecklistTasksPEOAttribute18 | ATTRIBUTE18 | — | — |
| 16 | AllocatedChecklistTasksPEOAttribute19 | ATTRIBUTE19 | — | — |
| 17 | AllocatedChecklistTasksPEOAttribute2 | ATTRIBUTE2 | — | — |
| 18 | AllocatedChecklistTasksPEOAttribute20 | ATTRIBUTE20 | — | — |
| 19 | AllocatedChecklistTasksPEOAttribute21 | ATTRIBUTE21 | — | — |
| 20 | AllocatedChecklistTasksPEOAttribute22 | ATTRIBUTE22 | — | — |
| 21 | AllocatedChecklistTasksPEOAttribute23 | ATTRIBUTE23 | — | — |
| 22 | AllocatedChecklistTasksPEOAttribute24 | ATTRIBUTE24 | — | — |
| 23 | AllocatedChecklistTasksPEOAttribute25 | ATTRIBUTE25 | — | — |
| 24 | AllocatedChecklistTasksPEOAttribute26 | ATTRIBUTE26 | — | — |
| 25 | AllocatedChecklistTasksPEOAttribute27 | ATTRIBUTE27 | — | — |
| 26 | AllocatedChecklistTasksPEOAttribute28 | ATTRIBUTE28 | — | — |
| 27 | AllocatedChecklistTasksPEOAttribute29 | ATTRIBUTE29 | — | — |
| 28 | AllocatedChecklistTasksPEOAttribute3 | ATTRIBUTE3 | — | — |
| 29 | AllocatedChecklistTasksPEOAttribute30 | ATTRIBUTE30 | — | — |
| 30 | AllocatedChecklistTasksPEOAttribute4 | ATTRIBUTE4 | — | — |
| 31 | AllocatedChecklistTasksPEOAttribute5 | ATTRIBUTE5 | — | — |
| 32 | AllocatedChecklistTasksPEOAttribute6 | ATTRIBUTE6 | — | — |
| 33 | AllocatedChecklistTasksPEOAttribute7 | ATTRIBUTE7 | — | — |
| 34 | AllocatedChecklistTasksPEOAttribute8 | ATTRIBUTE8 | — | — |
| 35 | AllocatedChecklistTasksPEOAttribute9 | ATTRIBUTE9 | — | — |
| 36 | AllocatedChecklistTasksPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 37 | AllocatedChecklistTasksPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 38 | AllocatedChecklistTasksPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 39 | AllocatedChecklistTasksPEOAttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 40 | AllocatedChecklistTasksPEOAttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 41 | AllocatedChecklistTasksPEOAttributeDate13 | ATTRIBUTE_DATE13 | — | — |
| 42 | AllocatedChecklistTasksPEOAttributeDate14 | ATTRIBUTE_DATE14 | — | — |
| 43 | AllocatedChecklistTasksPEOAttributeDate15 | ATTRIBUTE_DATE15 | — | — |
| 44 | AllocatedChecklistTasksPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 45 | AllocatedChecklistTasksPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 46 | AllocatedChecklistTasksPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 47 | AllocatedChecklistTasksPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 48 | AllocatedChecklistTasksPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 49 | AllocatedChecklistTasksPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 50 | AllocatedChecklistTasksPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 51 | AllocatedChecklistTasksPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 52 | AllocatedChecklistTasksPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 53 | AllocatedChecklistTasksPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 54 | AllocatedChecklistTasksPEOAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 55 | AllocatedChecklistTasksPEOAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 56 | AllocatedChecklistTasksPEOAttributeNumber13 | ATTRIBUTE_NUMBER13 | — | — |
| 57 | AllocatedChecklistTasksPEOAttributeNumber14 | ATTRIBUTE_NUMBER14 | — | — |
| 58 | AllocatedChecklistTasksPEOAttributeNumber15 | ATTRIBUTE_NUMBER15 | — | — |
| 59 | AllocatedChecklistTasksPEOAttributeNumber16 | ATTRIBUTE_NUMBER16 | — | — |
| 60 | AllocatedChecklistTasksPEOAttributeNumber17 | ATTRIBUTE_NUMBER17 | — | — |
| 61 | AllocatedChecklistTasksPEOAttributeNumber18 | ATTRIBUTE_NUMBER18 | — | — |
| 62 | AllocatedChecklistTasksPEOAttributeNumber19 | ATTRIBUTE_NUMBER19 | — | — |
| 63 | AllocatedChecklistTasksPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 64 | AllocatedChecklistTasksPEOAttributeNumber20 | ATTRIBUTE_NUMBER20 | — | — |
| 65 | AllocatedChecklistTasksPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 66 | AllocatedChecklistTasksPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 67 | AllocatedChecklistTasksPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 68 | AllocatedChecklistTasksPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 69 | AllocatedChecklistTasksPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 70 | AllocatedChecklistTasksPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 71 | AllocatedChecklistTasksPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 72 | AllocatedChecklistTasksPEOCompletedBy | COMPLETED_BY | — | — |
| 73 | AllocatedChecklistTasksPEOCompletionDate | COMPLETION_DATE | — | — |
| 74 | AllocatedChecklistTasksPEOContactDetails | CONTACT_DETAILS | — | ✅ |
| 75 | AllocatedChecklistTasksPEOCreatedBy | CREATED_BY | — | ✅ |
| 76 | AllocatedChecklistTasksPEOCreationDate | CREATION_DATE | — | ✅ |
| 77 | AllocatedChecklistTasksPEODefAllocationDate | DEF_ALLOCATION_DATE | — | ✅ |
| 78 | AllocatedChecklistTasksPEODefaultPerfRespType | DEFAULT_PERF_RESP_TYPE | — | ✅ |
| 79 | AllocatedChecklistTasksPEODependentOnTasks | DEPENDENT_ON_TASKS | — | ✅ |
| 80 | AllocatedChecklistTasksPEODetailAllocChecklistId | DETAIL_ALLOC_CHECKLIST_ID | — | — |
| 81 | AllocatedChecklistTasksPEODetailChecklistId | DETAIL_CHECKLIST_ID | — | — |
| 82 | AllocatedChecklistTasksPEODocumentEntityId | DOCUMENT_ENTITY_ID | — | — |
| 83 | AllocatedChecklistTasksPEODocumentTypeId | DOCUMENT_TYPE_ID | — | ✅ |
| 84 | AllocatedChecklistTasksPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 85 | AllocatedChecklistTasksPEOEsignType | ESIGN_TYPE | — | ✅ |
| 86 | AllocatedChecklistTasksPEOExpiryDays | EXPIRY_DAYS | — | ✅ |
| 87 | AllocatedChecklistTasksPEOFlexContextCode | FLEX_CONTEXT_CODE | — | — |
| 88 | AllocatedChecklistTasksPEOGenerateAtomFeed | GENERATE_ATOM_FEED | — | — |
| 89 | AllocatedChecklistTasksPEOInformation1 | INFORMATION1 | — | — |
| 90 | AllocatedChecklistTasksPEOInformation10 | INFORMATION10 | — | — |
| 91 | AllocatedChecklistTasksPEOInformation11 | INFORMATION11 | — | — |
| 92 | AllocatedChecklistTasksPEOInformation12 | INFORMATION12 | — | — |
| 93 | AllocatedChecklistTasksPEOInformation13 | INFORMATION13 | — | — |
| 94 | AllocatedChecklistTasksPEOInformation14 | INFORMATION14 | — | — |
| 95 | AllocatedChecklistTasksPEOInformation15 | INFORMATION15 | — | — |
| 96 | AllocatedChecklistTasksPEOInformation16 | INFORMATION16 | — | — |
| 97 | AllocatedChecklistTasksPEOInformation17 | INFORMATION17 | — | — |
| 98 | AllocatedChecklistTasksPEOInformation18 | INFORMATION18 | — | — |
| 99 | AllocatedChecklistTasksPEOInformation19 | INFORMATION19 | — | — |
| 100 | AllocatedChecklistTasksPEOInformation2 | INFORMATION2 | — | — |
| 101 | AllocatedChecklistTasksPEOInformation20 | INFORMATION20 | — | — |
| 102 | AllocatedChecklistTasksPEOInformation21 | INFORMATION21 | — | — |
| 103 | AllocatedChecklistTasksPEOInformation22 | INFORMATION22 | — | — |
| 104 | AllocatedChecklistTasksPEOInformation23 | INFORMATION23 | — | — |
| 105 | AllocatedChecklistTasksPEOInformation24 | INFORMATION24 | — | — |
| 106 | AllocatedChecklistTasksPEOInformation25 | INFORMATION25 | — | — |
| 107 | AllocatedChecklistTasksPEOInformation26 | INFORMATION26 | — | — |
| 108 | AllocatedChecklistTasksPEOInformation27 | INFORMATION27 | — | — |
| 109 | AllocatedChecklistTasksPEOInformation28 | INFORMATION28 | — | — |
| 110 | AllocatedChecklistTasksPEOInformation29 | INFORMATION29 | — | — |
| 111 | AllocatedChecklistTasksPEOInformation3 | INFORMATION3 | — | — |
| 112 | AllocatedChecklistTasksPEOInformation30 | INFORMATION30 | — | — |
| 113 | AllocatedChecklistTasksPEOInformation4 | INFORMATION4 | — | — |
| 114 | AllocatedChecklistTasksPEOInformation5 | INFORMATION5 | — | — |
| 115 | AllocatedChecklistTasksPEOInformation6 | INFORMATION6 | — | — |
| 116 | AllocatedChecklistTasksPEOInformation7 | INFORMATION7 | — | — |
| 117 | AllocatedChecklistTasksPEOInformation8 | INFORMATION8 | — | — |
| 118 | AllocatedChecklistTasksPEOInformation9 | INFORMATION9 | — | — |
| 119 | AllocatedChecklistTasksPEOInformationCategory | INFORMATION_CATEGORY | — | — |
| 120 | AllocatedChecklistTasksPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 121 | AllocatedChecklistTasksPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 122 | AllocatedChecklistTasksPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 123 | AllocatedChecklistTasksPEOMandatoryFlag | MANDATORY_FLAG | — | ✅ |
| 124 | AllocatedChecklistTasksPEOMeetingOffset | MEETING_OFFSET | — | ✅ |
| 125 | AllocatedChecklistTasksPEOMeetingTime | MEETING_TIME | — | ✅ |
| 126 | AllocatedChecklistTasksPEONextReminderDate | NEXT_REMINDER_DATE | — | — |
| 127 | AllocatedChecklistTasksPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 128 | AllocatedChecklistTasksPEOOwnerRespType | OWNER_RESP_TYPE | — | ✅ |
| 129 | AllocatedChecklistTasksPEOOwnerRespTypeUsers | OWNER_RESP_TYPE_USERS | — | — |
| 130 | AllocatedChecklistTasksPEOPerformerOrigSysId | PERFORMER_ORIG_SYS_ID | — | ✅ |
| 131 | AllocatedChecklistTasksPEOPerformerOrigSystem | PERFORMER_ORIG_SYSTEM | — | — |
| 132 | AllocatedChecklistTasksPEOProcessingMode | PROCESSING_MODE | — | — |
| 133 | AllocatedChecklistTasksPEOQuestionnaireId | QUESTIONNAIRE_ID | — | ✅ |
| 134 | AllocatedChecklistTasksPEOReassignedBy | REASSIGNED_BY | — | — |
| 135 | AllocatedChecklistTasksPEOReassignedDate | REASSIGNED_DATE | — | — |
| 136 | AllocatedChecklistTasksPEOReminderCount | REMINDER_COUNT | — | — |
| 137 | AllocatedChecklistTasksPEOReminderDuration | REMINDER_DURATION | — | ✅ |
| 138 | AllocatedChecklistTasksPEOReminderRecurrence | REMINDER_RECURRENCE | — | ✅ |
| 139 | AllocatedChecklistTasksPEOReminderRelativeTo | REMINDER_RELATIVE_TO | — | ✅ |
| 140 | AllocatedChecklistTasksPEOReminderTemplateId | REMINDER_TEMPLATE_ID | — | — |
| 141 | AllocatedChecklistTasksPEOReopenDate | REOPEN_DATE | — | ✅ |
| 142 | AllocatedChecklistTasksPEOReopenedBy | REOPENED_BY | — | ✅ |
| 143 | AllocatedChecklistTasksPEOReportPath | REPORT_PATH | — | ✅ |
| 144 | AllocatedChecklistTasksPEORespPerformerAvailability | RESP_PERFORMER_AVAILABILITY | — | ✅ |
| 145 | AllocatedChecklistTasksPEOResponsibilityType | RESPONSIBILITY_TYPE | — | ✅ |
| 146 | AllocatedChecklistTasksPEOResponsibilityTypeGuid | RESPONSIBILITY_TYPE_GUID | — | — |
| 147 | AllocatedChecklistTasksPEOSignDate | SIGN_DATE | — | ✅ |
| 148 | AllocatedChecklistTasksPEOSignDocument | SIGN_DOCUMENT | — | ✅ |
| 149 | AllocatedChecklistTasksPEOSignTemplate | SIGN_TEMPLATE | — | ✅ |
| 150 | AllocatedChecklistTasksPEOSignerEmail | SIGNER_EMAIL | — | ✅ |
| 151 | AllocatedChecklistTasksPEOSignerName | SIGNER_NAME | — | ✅ |
| 152 | AllocatedChecklistTasksPEOStatus | STATUS | — | ✅ |
| 153 | AllocatedChecklistTasksPEOTargetDuration | TARGET_DURATION | — | ✅ |
| 154 | AllocatedChecklistTasksPEOTargetDurationUom | TARGET_DURATION_UOM | — | ✅ |
| 155 | AllocatedChecklistTasksPEOTargetEndDate | TARGET_END_DATE | — | ✅ |
| 156 | AllocatedChecklistTasksPEOTargetStartDate | TARGET_START_DATE | — | ✅ |
| 157 | AllocatedChecklistTasksPEOTaskActionCode | TASK_ACTION_CODE | — | ✅ |
| 158 | AllocatedChecklistTasksPEOTaskActionId | TASK_ACTION_ID | — | ✅ |
| 159 | AllocatedChecklistTasksPEOTaskComments | TASK_COMMENTS | — | ✅ |
| 160 | AllocatedChecklistTasksPEOTaskConfiguration | TASK_CONFIGURATION | — | ✅ |
| 161 | AllocatedChecklistTasksPEOTaskDelayDuration | TASK_DELAY_DURATION | — | ✅ |
| 162 | AllocatedChecklistTasksPEOTaskDelayDurationUom | TASK_DELAY_DURATION_UOM | — | ✅ |
| 163 | AllocatedChecklistTasksPEOTaskFeature1 | TASK_FEATURE1 | — | — |
| 164 | AllocatedChecklistTasksPEOTaskInChecklistId | TASK_IN_CHECKLIST_ID | — | — |
| 165 | AllocatedChecklistTasksPEOTaskInitiator | TASK_INITIATOR | — | — |
| 166 | AllocatedChecklistTasksPEOTaskInitiatorPersonId | TASK_INITIATOR_PERSON_ID | — | — |
| 167 | AllocatedChecklistTasksPEOTaskOwnerPersonId | TASK_OWNER_PERSON_ID | — | ✅ |
| 168 | AllocatedChecklistTasksPEOTaskOwnerUsername | TASK_OWNER_USERNAME | — | — |
| 169 | AllocatedChecklistTasksPEOTaskOwners | TASK_OWNERS | — | — |
| 170 | AllocatedChecklistTasksPEOTaskPercentageComplete | TASK_PERCENTAGE_COMPLETE | — | — |
| 171 | AllocatedChecklistTasksPEOTaskPerformers | TASK_PERFORMERS | — | — |
| 172 | AllocatedChecklistTasksPEOTaskSequence | TASK_SEQUENCE | — | — |
| 173 | AllocatedTaskId | ALLOCATED_TASK_ID | 🔑 | ✅ |

### [[per_allocated_tasks_tl|PER_ALLOCATED_TASKS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AllocateChecklistTaskTemplat1AllocatedTaskId1 | ALLOCATED_TASK_ID | — | — |
| 2 | AllocateChecklistTaskTemplat1Language | LANGUAGE | — | — |
| 3 | AllocateChecklistTaskTemplat1PredecessorTaskName | TASK_NAME | — | ✅ |
| 4 | AllocateChecklistTaskTemplatActionUrl | ACTION_URL | — | — |
| 5 | AllocateChecklistTaskTemplatAllocatedTaskId | ALLOCATED_TASK_ID | — | — |
| 6 | AllocateChecklistTaskTemplatBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 7 | AllocateChecklistTaskTemplatCreatedBy | CREATED_BY | — | — |
| 8 | AllocateChecklistTaskTemplatCreationDate | CREATION_DATE | — | — |
| 9 | AllocateChecklistTaskTemplatDescription | DESCRIPTION | — | — |
| 10 | AllocateChecklistTaskTemplatLanguage | LANGUAGE | — | — |
| 11 | AllocateChecklistTaskTemplatLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 12 | AllocateChecklistTaskTemplatLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | AllocateChecklistTaskTemplatLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | AllocateChecklistTaskTemplatMeetingLocation | MEETING_LOCATION | — | ✅ |
| 15 | AllocateChecklistTaskTemplatObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | AllocateChecklistTaskTemplatSourceLang | SOURCE_LANG | — | — |
| 17 | AllocateChecklistTaskTemplatTaskDetails | TASK_DETAILS | — | ✅ |
| 18 | AllocateChecklistTaskTemplatTaskName | TASK_NAME | — | — |
| 19 | AllocatedChecklistTasksPEOActionUrl | ACTION_URL | — | ✅ |
| 20 | AllocatedChecklistTasksPEODescription | DESCRIPTION | — | ✅ |
| 21 | AllocatedChecklistTasksPEOTaskName | TASK_NAME | — | ✅ |

### [[per_alloc_chklst_contacts|PER_ALLOC_CHKLST_CONTACTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AllocatedChecklistContactsPEAdhocUserGuid | ADHOC_USER_GUID | — | ✅ |
| 2 | AllocatedChecklistContactsPEAllocChklstContactId | ALLOC_CHKLST_CONTACT_ID | — | — |
| 3 | AllocatedChecklistContactsPEAllocatedChecklistId | ALLOCATED_CHECKLIST_ID | — | — |
| 4 | AllocatedChecklistContactsPEChecklistContactId | CHECKLIST_CONTACT_ID | — | — |
| 5 | AllocatedChecklistContactsPEContactTitleCode | CONTACT_TITLE_CODE | — | ✅ |
| 6 | AllocatedChecklistContactsPEContactType | CONTACT_TYPE | — | ✅ |
| 7 | AllocatedChecklistContactsPECreatedBy | CREATED_BY | — | — |
| 8 | AllocatedChecklistContactsPECreationDate | CREATION_DATE | — | — |
| 9 | AllocatedChecklistContactsPECustomContact | CUSTOM_CONTACT | — | ✅ |
| 10 | AllocatedChecklistContactsPEEnterpriseId | ENTERPRISE_ID | — | — |
| 11 | AllocatedChecklistContactsPELastUpdateDate | LAST_UPDATE_DATE | — | — |
| 12 | AllocatedChecklistContactsPELastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | AllocatedChecklistContactsPELastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | AllocatedChecklistContactsPEObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | AllocatedChecklistContactsPEResponsibilityType | RESPONSIBILITY_TYPE | — | ✅ |

### [[per_alloc_chklst_contents|PER_ALLOC_CHKLST_CONTENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AllocatedChecklistContentsPE1AllocChklstContentId | ALLOC_CHKLST_CONTENT_ID | — | — |
| 2 | AllocatedChecklistContentsPE1AllocatedChecklistId | ALLOCATED_CHECKLIST_ID | — | — |
| 3 | AllocatedChecklistContentsPE1ChecklistContentId | CHECKLIST_CONTENT_ID | — | — |
| 4 | AllocatedChecklistContentsPE1ChkContentDefnId | CHK_CONTENT_DEFN_ID | — | — |
| 5 | AllocatedChecklistContentsPE1ContentType | CONTENT_TYPE | — | ✅ |
| 6 | AllocatedChecklistContentsPE1CreatedBy | CREATED_BY | — | — |
| 7 | AllocatedChecklistContentsPE1CreationDate | CREATION_DATE | — | — |
| 8 | AllocatedChecklistContentsPE1EnterpriseId | ENTERPRISE_ID | — | — |
| 9 | AllocatedChecklistContentsPE1LastUpdateDate | LAST_UPDATE_DATE | — | — |
| 10 | AllocatedChecklistContentsPE1LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | AllocatedChecklistContentsPE1LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | AllocatedChecklistContentsPE1ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | AllocatedChecklistContentsPE1Sequence | SEQUENCE | — | ✅ |
| 14 | AllocatedChecklistContentsPE2AllocChklstContentId | ALLOC_CHKLST_CONTENT_ID | — | — |
| 15 | AllocatedChecklistContentsPE2AllocatedChecklistId | ALLOCATED_CHECKLIST_ID | — | — |
| 16 | AllocatedChecklistContentsPE2ChecklistContentId | CHECKLIST_CONTENT_ID | — | — |
| 17 | AllocatedChecklistContentsPE2ChkContentDefnId | CHK_CONTENT_DEFN_ID | — | — |
| 18 | AllocatedChecklistContentsPE2ContentType | CONTENT_TYPE | — | ✅ |
| 19 | AllocatedChecklistContentsPE2CreatedBy | CREATED_BY | — | — |
| 20 | AllocatedChecklistContentsPE2CreationDate | CREATION_DATE | — | — |
| 21 | AllocatedChecklistContentsPE2EnterpriseId | ENTERPRISE_ID | — | — |
| 22 | AllocatedChecklistContentsPE2LastUpdateDate | LAST_UPDATE_DATE | — | — |
| 23 | AllocatedChecklistContentsPE2LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 24 | AllocatedChecklistContentsPE2LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 25 | AllocatedChecklistContentsPE2ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 26 | AllocatedChecklistContentsPE2Sequence | SEQUENCE | — | ✅ |
| 27 | AllocatedChecklistContentsPE3AllocChklstContentId | ALLOC_CHKLST_CONTENT_ID | — | — |
| 28 | AllocatedChecklistContentsPE3AllocatedChecklistId | ALLOCATED_CHECKLIST_ID | — | — |
| 29 | AllocatedChecklistContentsPE3ChecklistContentId | CHECKLIST_CONTENT_ID | — | — |
| 30 | AllocatedChecklistContentsPE3ChkContentDefnId | CHK_CONTENT_DEFN_ID | — | — |
| 31 | AllocatedChecklistContentsPE3ContentType | CONTENT_TYPE | — | ✅ |
| 32 | AllocatedChecklistContentsPE3CreatedBy | CREATED_BY | — | — |
| 33 | AllocatedChecklistContentsPE3CreationDate | CREATION_DATE | — | — |
| 34 | AllocatedChecklistContentsPE3EnterpriseId | ENTERPRISE_ID | — | — |
| 35 | AllocatedChecklistContentsPE3LastUpdateDate | LAST_UPDATE_DATE | — | — |
| 36 | AllocatedChecklistContentsPE3LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 37 | AllocatedChecklistContentsPE3LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 38 | AllocatedChecklistContentsPE3ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 39 | AllocatedChecklistContentsPE3Sequence | SEQUENCE | — | ✅ |
| 40 | AllocatedChecklistContentsPE4AllocChklstContentId | ALLOC_CHKLST_CONTENT_ID | — | — |
| 41 | AllocatedChecklistContentsPE4AllocatedChecklistId | ALLOCATED_CHECKLIST_ID | — | — |
| 42 | AllocatedChecklistContentsPE4ChecklistContentId | CHECKLIST_CONTENT_ID | — | — |
| 43 | AllocatedChecklistContentsPE4ChkContentDefnId | CHK_CONTENT_DEFN_ID | — | — |
| 44 | AllocatedChecklistContentsPE4ContentType | CONTENT_TYPE | — | ✅ |
| 45 | AllocatedChecklistContentsPE4CreatedBy | CREATED_BY | — | — |
| 46 | AllocatedChecklistContentsPE4CreationDate | CREATION_DATE | — | — |
| 47 | AllocatedChecklistContentsPE4EnterpriseId | ENTERPRISE_ID | — | — |
| 48 | AllocatedChecklistContentsPE4LastUpdateDate | LAST_UPDATE_DATE | — | — |
| 49 | AllocatedChecklistContentsPE4LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 50 | AllocatedChecklistContentsPE4LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 51 | AllocatedChecklistContentsPE4ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 52 | AllocatedChecklistContentsPE4Sequence | SEQUENCE | — | ✅ |
| 53 | AllocatedChecklistContentsPE5AllocChklstContentId | ALLOC_CHKLST_CONTENT_ID | — | — |
| 54 | AllocatedChecklistContentsPE5AllocatedChecklistId | ALLOCATED_CHECKLIST_ID | — | — |
| 55 | AllocatedChecklistContentsPE5ChecklistContentId | CHECKLIST_CONTENT_ID | — | — |
| 56 | AllocatedChecklistContentsPE5ChkContentDefnId | CHK_CONTENT_DEFN_ID | — | — |
| 57 | AllocatedChecklistContentsPE5ContentType | CONTENT_TYPE | — | ✅ |
| 58 | AllocatedChecklistContentsPE5CreatedBy | CREATED_BY | — | — |
| 59 | AllocatedChecklistContentsPE5CreationDate | CREATION_DATE | — | — |
| 60 | AllocatedChecklistContentsPE5EnterpriseId | ENTERPRISE_ID | — | — |
| 61 | AllocatedChecklistContentsPE5LastUpdateDate | LAST_UPDATE_DATE | — | — |
| 62 | AllocatedChecklistContentsPE5LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 63 | AllocatedChecklistContentsPE5LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 64 | AllocatedChecklistContentsPE5ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 65 | AllocatedChecklistContentsPE5Sequence | SEQUENCE | — | ✅ |
| 66 | AllocatedChecklistContentsPEAllocChklstContentId | ALLOC_CHKLST_CONTENT_ID | — | — |
| 67 | AllocatedChecklistContentsPEAllocatedChecklistId | ALLOCATED_CHECKLIST_ID | — | — |
| 68 | AllocatedChecklistContentsPEChecklistContentId | CHECKLIST_CONTENT_ID | — | — |
| 69 | AllocatedChecklistContentsPEChkContentDefnId | CHK_CONTENT_DEFN_ID | — | — |
| 70 | AllocatedChecklistContentsPEContentType | CONTENT_TYPE | — | ✅ |
| 71 | AllocatedChecklistContentsPECreatedBy | CREATED_BY | — | — |
| 72 | AllocatedChecklistContentsPECreationDate | CREATION_DATE | — | — |
| 73 | AllocatedChecklistContentsPEEnterpriseId | ENTERPRISE_ID | — | — |
| 74 | AllocatedChecklistContentsPELastUpdateDate | LAST_UPDATE_DATE | — | — |
| 75 | AllocatedChecklistContentsPELastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 76 | AllocatedChecklistContentsPELastUpdatedBy | LAST_UPDATED_BY | — | — |
| 77 | AllocatedChecklistContentsPEObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 78 | AllocatedChecklistContentsPESequence | SEQUENCE | — | ✅ |

### [[per_alloc_task_notifs|PER_ALLOC_TASK_NOTIFS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AllocatedTaskNotificationPEO1AllocTaskNotificationId | ALLOC_TASK_NOTIFICATION_ID | — | — |
| 2 | AllocatedTaskNotificationPEO1AllocatedTaskId | ALLOCATED_TASK_ID | — | — |
| 3 | AllocatedTaskNotificationPEO1CreatedBy | CREATED_BY | — | — |
| 4 | AllocatedTaskNotificationPEO1CreationDate | CREATION_DATE | — | — |
| 5 | AllocatedTaskNotificationPEO1EnterpriseId | ENTERPRISE_ID | — | — |
| 6 | AllocatedTaskNotificationPEO1LastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | AllocatedTaskNotificationPEO1LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | AllocatedTaskNotificationPEO1LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | AllocatedTaskNotificationPEO1NotifyOwner | NOTIFY_OWNER | — | ✅ |
| 10 | AllocatedTaskNotificationPEO1NotifyPerformer | NOTIFY_PERFORMER | — | ✅ |
| 11 | AllocatedTaskNotificationPEO1ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | AllocatedTaskNotificationPEO1TaskEvent | TASK_EVENT | — | ✅ |
| 13 | AllocatedTaskNotificationPEO1TaskNotificationId | TASK_NOTIFICATION_ID | — | — |
| 14 | AllocatedTaskNotificationPEO2AllocTaskNotificationId | ALLOC_TASK_NOTIFICATION_ID | — | — |
| 15 | AllocatedTaskNotificationPEO2AllocatedTaskId | ALLOCATED_TASK_ID | — | — |
| 16 | AllocatedTaskNotificationPEO2CreatedBy | CREATED_BY | — | — |
| 17 | AllocatedTaskNotificationPEO2CreationDate | CREATION_DATE | — | — |
| 18 | AllocatedTaskNotificationPEO2EnterpriseId | ENTERPRISE_ID | — | — |
| 19 | AllocatedTaskNotificationPEO2LastUpdateDate | LAST_UPDATE_DATE | — | — |
| 20 | AllocatedTaskNotificationPEO2LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 21 | AllocatedTaskNotificationPEO2LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 22 | AllocatedTaskNotificationPEO2NotifyOwner | NOTIFY_OWNER | — | ✅ |
| 23 | AllocatedTaskNotificationPEO2NotifyPerformer | NOTIFY_PERFORMER | — | ✅ |
| 24 | AllocatedTaskNotificationPEO2ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 25 | AllocatedTaskNotificationPEO2TaskEvent | TASK_EVENT | — | ✅ |
| 26 | AllocatedTaskNotificationPEO2TaskNotificationId | TASK_NOTIFICATION_ID | — | — |
| 27 | AllocatedTaskNotificationPEO3AllocTaskNotificationId | ALLOC_TASK_NOTIFICATION_ID | — | — |
| 28 | AllocatedTaskNotificationPEO3AllocatedTaskId | ALLOCATED_TASK_ID | — | — |
| 29 | AllocatedTaskNotificationPEO3CreatedBy | CREATED_BY | — | — |
| 30 | AllocatedTaskNotificationPEO3CreationDate | CREATION_DATE | — | — |
| 31 | AllocatedTaskNotificationPEO3EnterpriseId | ENTERPRISE_ID | — | — |
| 32 | AllocatedTaskNotificationPEO3LastUpdateDate | LAST_UPDATE_DATE | — | — |
| 33 | AllocatedTaskNotificationPEO3LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 34 | AllocatedTaskNotificationPEO3LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 35 | AllocatedTaskNotificationPEO3NotifyOwner | NOTIFY_OWNER | — | ✅ |
| 36 | AllocatedTaskNotificationPEO3NotifyPerformer | NOTIFY_PERFORMER | — | ✅ |
| 37 | AllocatedTaskNotificationPEO3ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 38 | AllocatedTaskNotificationPEO3TaskEvent | TASK_EVENT | — | ✅ |
| 39 | AllocatedTaskNotificationPEO3TaskNotificationId | TASK_NOTIFICATION_ID | — | — |
| 40 | AllocatedTaskNotificationPEOAllocTaskNotificationId | ALLOC_TASK_NOTIFICATION_ID | — | — |
| 41 | AllocatedTaskNotificationPEOAllocatedTaskId | ALLOCATED_TASK_ID | — | — |
| 42 | AllocatedTaskNotificationPEOCreatedBy | CREATED_BY | — | — |
| 43 | AllocatedTaskNotificationPEOCreationDate | CREATION_DATE | — | — |
| 44 | AllocatedTaskNotificationPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 45 | AllocatedTaskNotificationPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 46 | AllocatedTaskNotificationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 47 | AllocatedTaskNotificationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 48 | AllocatedTaskNotificationPEONotifyOwner | NOTIFY_OWNER | — | ✅ |
| 49 | AllocatedTaskNotificationPEONotifyPerformer | NOTIFY_PERFORMER | — | ✅ |
| 50 | AllocatedTaskNotificationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 51 | AllocatedTaskNotificationPEOTaskEvent | TASK_EVENT | — | ✅ |
| 52 | AllocatedTaskNotificationPEOTaskNotificationId | TASK_NOTIFICATION_ID | — | — |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonDetailsPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | PersonDetailsPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | PersonDetailsPEOPersonId | PERSON_ID | — | — |
| 4 | PersonDetailsPEOPersonNumber | PERSON_NUMBER | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | PersonNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | PersonNamePEOFullName | FULL_NAME | — | ✅ |
| 4 | PersonNamePEOPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UsersPEOAllocatedContactAdhocUsername | USERNAME | — | ✅ |
| 2 | UsersPEOUserId | USER_ID | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
