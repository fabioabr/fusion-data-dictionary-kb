---
id: DOC-AP-PVO-AllocatedChecklistsPVO
doc_type: system-doc
title: "AllocatedChecklistsPVO — PVO Accounts Payable"
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
  - AllocatedChecklistsPVO
  - allocatedchecklistspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AllocatedChecklistsPVO

## 📌 Visão Geral

Extrai os checklists alocados a colaboradores em processos de RH (onboarding, offboarding, transferências), incluindo contatos, conteúdos e responsáveis. Permite acompanhar o progresso de atividades obrigatórias em transições de pessoal e garantir conformidade nos processos de gestão de pessoas.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.ChecklistAM.AllocatedChecklistsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 253 | 7 | 1 | 42 | 17% |

---

## 🔗 Tabelas Relacionadas

- [[per_allocated_checklists|PER_ALLOCATED_CHECKLISTS]] — 133 atributos (1 PKs, 18 BICC)
- [[per_allocated_checklists_tl|PER_ALLOCATED_CHECKLISTS_TL]] — 17 atributos (4 BICC)
- [[per_alloc_chklst_contacts|PER_ALLOC_CHKLST_CONTACTS]] — 15 atributos (5 BICC)
- [[per_alloc_chklst_contents|PER_ALLOC_CHKLST_CONTENTS]] — 78 atributos (12 BICC)
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 4 atributos (1 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 4 atributos (1 BICC)
- [[per_users|PER_USERS]] — 2 atributos (1 BICC)

---

## ⚙️ Atributos

### [[per_allocated_checklists|PER_ALLOCATED_CHECKLISTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AllocatedChecklistId | ALLOCATED_CHECKLIST_ID | 🔑 | ✅ |
| 2 | AllocatedChecklistsPEOActionDate | ACTION_DATE | — | ✅ |
| 3 | AllocatedChecklistsPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 4 | AllocatedChecklistsPEOAllocationDate | ALLOCATION_DATE | — | ✅ |
| 5 | AllocatedChecklistsPEOAllocationDetails | ALLOCATION_DETAILS | — | ✅ |
| 6 | AllocatedChecklistsPEOAllocationNotifiedFlag | ALLOCATION_NOTIFIED_FLAG | — | — |
| 7 | AllocatedChecklistsPEOAssignmentId | ASSIGNMENT_ID | — | — |
| 8 | AllocatedChecklistsPEOAttribute1 | ATTRIBUTE1 | — | — |
| 9 | AllocatedChecklistsPEOAttribute10 | ATTRIBUTE10 | — | — |
| 10 | AllocatedChecklistsPEOAttribute11 | ATTRIBUTE11 | — | — |
| 11 | AllocatedChecklistsPEOAttribute12 | ATTRIBUTE12 | — | — |
| 12 | AllocatedChecklistsPEOAttribute13 | ATTRIBUTE13 | — | — |
| 13 | AllocatedChecklistsPEOAttribute14 | ATTRIBUTE14 | — | — |
| 14 | AllocatedChecklistsPEOAttribute15 | ATTRIBUTE15 | — | — |
| 15 | AllocatedChecklistsPEOAttribute16 | ATTRIBUTE16 | — | — |
| 16 | AllocatedChecklistsPEOAttribute17 | ATTRIBUTE17 | — | — |
| 17 | AllocatedChecklistsPEOAttribute18 | ATTRIBUTE18 | — | — |
| 18 | AllocatedChecklistsPEOAttribute19 | ATTRIBUTE19 | — | — |
| 19 | AllocatedChecklistsPEOAttribute2 | ATTRIBUTE2 | — | — |
| 20 | AllocatedChecklistsPEOAttribute20 | ATTRIBUTE20 | — | — |
| 21 | AllocatedChecklistsPEOAttribute21 | ATTRIBUTE21 | — | — |
| 22 | AllocatedChecklistsPEOAttribute22 | ATTRIBUTE22 | — | — |
| 23 | AllocatedChecklistsPEOAttribute23 | ATTRIBUTE23 | — | — |
| 24 | AllocatedChecklistsPEOAttribute24 | ATTRIBUTE24 | — | — |
| 25 | AllocatedChecklistsPEOAttribute25 | ATTRIBUTE25 | — | — |
| 26 | AllocatedChecklistsPEOAttribute26 | ATTRIBUTE26 | — | — |
| 27 | AllocatedChecklistsPEOAttribute27 | ATTRIBUTE27 | — | — |
| 28 | AllocatedChecklistsPEOAttribute28 | ATTRIBUTE28 | — | — |
| 29 | AllocatedChecklistsPEOAttribute29 | ATTRIBUTE29 | — | — |
| 30 | AllocatedChecklistsPEOAttribute3 | ATTRIBUTE3 | — | — |
| 31 | AllocatedChecklistsPEOAttribute30 | ATTRIBUTE30 | — | — |
| 32 | AllocatedChecklistsPEOAttribute4 | ATTRIBUTE4 | — | — |
| 33 | AllocatedChecklistsPEOAttribute5 | ATTRIBUTE5 | — | — |
| 34 | AllocatedChecklistsPEOAttribute6 | ATTRIBUTE6 | — | — |
| 35 | AllocatedChecklistsPEOAttribute7 | ATTRIBUTE7 | — | — |
| 36 | AllocatedChecklistsPEOAttribute8 | ATTRIBUTE8 | — | — |
| 37 | AllocatedChecklistsPEOAttribute9 | ATTRIBUTE9 | — | — |
| 38 | AllocatedChecklistsPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 39 | AllocatedChecklistsPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 40 | AllocatedChecklistsPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 41 | AllocatedChecklistsPEOAttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 42 | AllocatedChecklistsPEOAttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 43 | AllocatedChecklistsPEOAttributeDate13 | ATTRIBUTE_DATE13 | — | — |
| 44 | AllocatedChecklistsPEOAttributeDate14 | ATTRIBUTE_DATE14 | — | — |
| 45 | AllocatedChecklistsPEOAttributeDate15 | ATTRIBUTE_DATE15 | — | — |
| 46 | AllocatedChecklistsPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 47 | AllocatedChecklistsPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 48 | AllocatedChecklistsPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 49 | AllocatedChecklistsPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 50 | AllocatedChecklistsPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 51 | AllocatedChecklistsPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 52 | AllocatedChecklistsPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 53 | AllocatedChecklistsPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 54 | AllocatedChecklistsPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 55 | AllocatedChecklistsPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 56 | AllocatedChecklistsPEOAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 57 | AllocatedChecklistsPEOAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 58 | AllocatedChecklistsPEOAttributeNumber13 | ATTRIBUTE_NUMBER13 | — | — |
| 59 | AllocatedChecklistsPEOAttributeNumber14 | ATTRIBUTE_NUMBER14 | — | — |
| 60 | AllocatedChecklistsPEOAttributeNumber15 | ATTRIBUTE_NUMBER15 | — | — |
| 61 | AllocatedChecklistsPEOAttributeNumber16 | ATTRIBUTE_NUMBER16 | — | — |
| 62 | AllocatedChecklistsPEOAttributeNumber17 | ATTRIBUTE_NUMBER17 | — | — |
| 63 | AllocatedChecklistsPEOAttributeNumber18 | ATTRIBUTE_NUMBER18 | — | — |
| 64 | AllocatedChecklistsPEOAttributeNumber19 | ATTRIBUTE_NUMBER19 | — | — |
| 65 | AllocatedChecklistsPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 66 | AllocatedChecklistsPEOAttributeNumber20 | ATTRIBUTE_NUMBER20 | — | — |
| 67 | AllocatedChecklistsPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 68 | AllocatedChecklistsPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 69 | AllocatedChecklistsPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 70 | AllocatedChecklistsPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 71 | AllocatedChecklistsPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 72 | AllocatedChecklistsPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 73 | AllocatedChecklistsPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 74 | AllocatedChecklistsPEOBackgroundImageUrl | BACKGROUND_IMAGE_URL | — | — |
| 75 | AllocatedChecklistsPEOBackgroundThumbnailUrl | BACKGROUND_THUMBNAIL_URL | — | — |
| 76 | AllocatedChecklistsPEOChecklistActionId | CHECKLIST_ACTION_ID | — | — |
| 77 | AllocatedChecklistsPEOChecklistActionOccurrenceId | CHECKLIST_ACTION_OCCURRENCE_ID | — | — |
| 78 | AllocatedChecklistsPEOChecklistCategory | CHECKLIST_CATEGORY | — | ✅ |
| 79 | AllocatedChecklistsPEOChecklistId | CHECKLIST_ID | — | ✅ |
| 80 | AllocatedChecklistsPEOChecklistInstance | CHECKLIST_INSTANCE | — | ✅ |
| 81 | AllocatedChecklistsPEOChecklistStatus | CHECKLIST_STATUS | — | ✅ |
| 82 | AllocatedChecklistsPEOCombinedTaskTemplateId | COMBINED_TASK_TEMPLATE_ID | — | — |
| 83 | AllocatedChecklistsPEOCompletedOn | COMPLETED_ON | — | ✅ |
| 84 | AllocatedChecklistsPEOCompletionDate | COMPLETION_DATE | — | ✅ |
| 85 | AllocatedChecklistsPEOCompletionOffsetDays | COMPLETION_OFFSET_DAYS | — | ✅ |
| 86 | AllocatedChecklistsPEOCreatedBy | CREATED_BY | — | ✅ |
| 87 | AllocatedChecklistsPEOCreationDate | CREATION_DATE | — | ✅ |
| 88 | AllocatedChecklistsPEODefCompletionDate | DEF_COMPLETION_DATE | — | — |
| 89 | AllocatedChecklistsPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 90 | AllocatedChecklistsPEOEventDate | EVENT_DATE | — | ✅ |
| 91 | AllocatedChecklistsPEOInformation1 | INFORMATION1 | — | — |
| 92 | AllocatedChecklistsPEOInformation10 | INFORMATION10 | — | — |
| 93 | AllocatedChecklistsPEOInformation11 | INFORMATION11 | — | — |
| 94 | AllocatedChecklistsPEOInformation12 | INFORMATION12 | — | — |
| 95 | AllocatedChecklistsPEOInformation13 | INFORMATION13 | — | — |
| 96 | AllocatedChecklistsPEOInformation14 | INFORMATION14 | — | — |
| 97 | AllocatedChecklistsPEOInformation15 | INFORMATION15 | — | — |
| 98 | AllocatedChecklistsPEOInformation16 | INFORMATION16 | — | — |
| 99 | AllocatedChecklistsPEOInformation17 | INFORMATION17 | — | — |
| 100 | AllocatedChecklistsPEOInformation18 | INFORMATION18 | — | — |
| 101 | AllocatedChecklistsPEOInformation19 | INFORMATION19 | — | — |
| 102 | AllocatedChecklistsPEOInformation2 | INFORMATION2 | — | — |
| 103 | AllocatedChecklistsPEOInformation20 | INFORMATION20 | — | — |
| 104 | AllocatedChecklistsPEOInformation21 | INFORMATION21 | — | — |
| 105 | AllocatedChecklistsPEOInformation22 | INFORMATION22 | — | — |
| 106 | AllocatedChecklistsPEOInformation23 | INFORMATION23 | — | — |
| 107 | AllocatedChecklistsPEOInformation24 | INFORMATION24 | — | — |
| 108 | AllocatedChecklistsPEOInformation25 | INFORMATION25 | — | — |
| 109 | AllocatedChecklistsPEOInformation26 | INFORMATION26 | — | — |
| 110 | AllocatedChecklistsPEOInformation27 | INFORMATION27 | — | — |
| 111 | AllocatedChecklistsPEOInformation28 | INFORMATION28 | — | — |
| 112 | AllocatedChecklistsPEOInformation29 | INFORMATION29 | — | — |
| 113 | AllocatedChecklistsPEOInformation3 | INFORMATION3 | — | — |
| 114 | AllocatedChecklistsPEOInformation30 | INFORMATION30 | — | — |
| 115 | AllocatedChecklistsPEOInformation4 | INFORMATION4 | — | — |
| 116 | AllocatedChecklistsPEOInformation5 | INFORMATION5 | — | — |
| 117 | AllocatedChecklistsPEOInformation6 | INFORMATION6 | — | — |
| 118 | AllocatedChecklistsPEOInformation7 | INFORMATION7 | — | — |
| 119 | AllocatedChecklistsPEOInformation8 | INFORMATION8 | — | — |
| 120 | AllocatedChecklistsPEOInformation9 | INFORMATION9 | — | — |
| 121 | AllocatedChecklistsPEOInformationCategory | INFORMATION_CATEGORY | — | — |
| 122 | AllocatedChecklistsPEOInitiatorPersonId | INITIATOR_PERSON_ID | — | — |
| 123 | AllocatedChecklistsPEOInitiatorUser | INITIATOR_USER | — | — |
| 124 | AllocatedChecklistsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 125 | AllocatedChecklistsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 126 | AllocatedChecklistsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 127 | AllocatedChecklistsPEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 128 | AllocatedChecklistsPEOObjectId | OBJECT_ID | — | — |
| 129 | AllocatedChecklistsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 130 | AllocatedChecklistsPEOPeriodOfServiceId | PERIOD_OF_SERVICE_ID | — | — |
| 131 | AllocatedChecklistsPEOPersonId | PERSON_ID | — | — |
| 132 | AllocatedChecklistsPEOProcessingMode | PROCESSING_MODE | — | — |
| 133 | AllocatedChecklistsPEOSelfAssignedFlag | SELF_ASSIGNED_FLAG | — | — |

### [[per_allocated_checklists_tl|PER_ALLOCATED_CHECKLISTS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AllocatedChecklistranslationAllocatedChecklistId | ALLOCATED_CHECKLIST_ID | — | — |
| 2 | AllocatedChecklistranslationBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | AllocatedChecklistranslationChecklistDetails | CHECKLIST_DETAILS | — | — |
| 4 | AllocatedChecklistranslationChecklistName | CHECKLIST_NAME | — | — |
| 5 | AllocatedChecklistranslationCreatedBy | CREATED_BY | — | — |
| 6 | AllocatedChecklistranslationCreationDate | CREATION_DATE | — | — |
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
| 67 | AllocatedChecklistContentsPEChecklistContentId | CHECKLIST_CONTENT_ID | — | — |
| 68 | AllocatedChecklistContentsPEOAllocatedChecklistId | ALLOCATED_CHECKLIST_ID | — | — |
| 69 | AllocatedChecklistContentsPEOChkContentDefnId | CHK_CONTENT_DEFN_ID | — | — |
| 70 | AllocatedChecklistContentsPEOContentType | CONTENT_TYPE | — | ✅ |
| 71 | AllocatedChecklistContentsPEOCreatedBy | CREATED_BY | — | — |
| 72 | AllocatedChecklistContentsPEOCreationDate | CREATION_DATE | — | — |
| 73 | AllocatedChecklistContentsPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 74 | AllocatedChecklistContentsPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 75 | AllocatedChecklistContentsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 76 | AllocatedChecklistContentsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 77 | AllocatedChecklistContentsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 78 | AllocatedChecklistContentsPEOSequence | SEQUENCE | — | ✅ |

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

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
