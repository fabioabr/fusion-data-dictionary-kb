---
id: DOC-PO-PVO-QualAreaQuestionPVO
doc_type: system-doc
title: "QualAreaQuestionPVO — PVO Purchasing"
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
  - QualAreaQuestionPVO
  - qualareaquestionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QualAreaQuestionPVO

## 📌 Visão Geral

Extrai as perguntas associadas a áreas de qualificação de fornecedores, vinculando critérios de avaliação a dimensões de homologação. Permite análise de cobertura e profundidade por área temática.

**Caminho:** `FscmTopModelAM.PrcPoqPublicViewAM.QualAreaQuestionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 240 | 5 | 2 | 237 | 99% |

---

## 🔗 Tabelas Relacionadas

- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 124 atributos (124 BICC)
- [[poq_qual_areas_vl|POQ_QUAL_AREAS_VL]] — 24 atributos (23 BICC)
- [[poq_qual_area_questions|POQ_QUAL_AREA_QUESTIONS]] — 12 atributos (1 PKs, 12 BICC)
- [[poq_questions_vl|POQ_QUESTIONS_VL]] — 77 atributos (1 PKs, 75 BICC)
- [[poq_question_structure_v|POQ_QUESTION_STRUCTURE_V]] — 3 atributos (3 BICC)

---

## ⚙️ Atributos

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OwnerAttribute1 | ATTRIBUTE1 | — | ✅ |
| 2 | OwnerAttribute10 | ATTRIBUTE10 | — | ✅ |
| 3 | OwnerAttribute11 | ATTRIBUTE11 | — | ✅ |
| 4 | OwnerAttribute12 | ATTRIBUTE12 | — | ✅ |
| 5 | OwnerAttribute13 | ATTRIBUTE13 | — | ✅ |
| 6 | OwnerAttribute14 | ATTRIBUTE14 | — | ✅ |
| 7 | OwnerAttribute15 | ATTRIBUTE15 | — | ✅ |
| 8 | OwnerAttribute16 | ATTRIBUTE16 | — | ✅ |
| 9 | OwnerAttribute17 | ATTRIBUTE17 | — | ✅ |
| 10 | OwnerAttribute18 | ATTRIBUTE18 | — | ✅ |
| 11 | OwnerAttribute19 | ATTRIBUTE19 | — | ✅ |
| 12 | OwnerAttribute2 | ATTRIBUTE2 | — | ✅ |
| 13 | OwnerAttribute20 | ATTRIBUTE20 | — | ✅ |
| 14 | OwnerAttribute21 | ATTRIBUTE21 | — | ✅ |
| 15 | OwnerAttribute22 | ATTRIBUTE22 | — | ✅ |
| 16 | OwnerAttribute23 | ATTRIBUTE23 | — | ✅ |
| 17 | OwnerAttribute24 | ATTRIBUTE24 | — | ✅ |
| 18 | OwnerAttribute25 | ATTRIBUTE25 | — | ✅ |
| 19 | OwnerAttribute26 | ATTRIBUTE26 | — | ✅ |
| 20 | OwnerAttribute27 | ATTRIBUTE27 | — | ✅ |
| 21 | OwnerAttribute28 | ATTRIBUTE28 | — | ✅ |
| 22 | OwnerAttribute29 | ATTRIBUTE29 | — | ✅ |
| 23 | OwnerAttribute3 | ATTRIBUTE3 | — | ✅ |
| 24 | OwnerAttribute30 | ATTRIBUTE30 | — | ✅ |
| 25 | OwnerAttribute4 | ATTRIBUTE4 | — | ✅ |
| 26 | OwnerAttribute5 | ATTRIBUTE5 | — | ✅ |
| 27 | OwnerAttribute6 | ATTRIBUTE6 | — | ✅ |
| 28 | OwnerAttribute7 | ATTRIBUTE7 | — | ✅ |
| 29 | OwnerAttribute8 | ATTRIBUTE8 | — | ✅ |
| 30 | OwnerAttribute9 | ATTRIBUTE9 | — | ✅ |
| 31 | OwnerAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 32 | OwnerAttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 33 | OwnerAttributeDate10 | ATTRIBUTE_DATE10 | — | ✅ |
| 34 | OwnerAttributeDate11 | ATTRIBUTE_DATE11 | — | ✅ |
| 35 | OwnerAttributeDate12 | ATTRIBUTE_DATE12 | — | ✅ |
| 36 | OwnerAttributeDate13 | ATTRIBUTE_DATE13 | — | ✅ |
| 37 | OwnerAttributeDate14 | ATTRIBUTE_DATE14 | — | ✅ |
| 38 | OwnerAttributeDate15 | ATTRIBUTE_DATE15 | — | ✅ |
| 39 | OwnerAttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 40 | OwnerAttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 41 | OwnerAttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 42 | OwnerAttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 43 | OwnerAttributeDate6 | ATTRIBUTE_DATE6 | — | ✅ |
| 44 | OwnerAttributeDate7 | ATTRIBUTE_DATE7 | — | ✅ |
| 45 | OwnerAttributeDate8 | ATTRIBUTE_DATE8 | — | ✅ |
| 46 | OwnerAttributeDate9 | ATTRIBUTE_DATE9 | — | ✅ |
| 47 | OwnerAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 48 | OwnerAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 49 | OwnerAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | ✅ |
| 50 | OwnerAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | ✅ |
| 51 | OwnerAttributeNumber13 | ATTRIBUTE_NUMBER13 | — | ✅ |
| 52 | OwnerAttributeNumber14 | ATTRIBUTE_NUMBER14 | — | ✅ |
| 53 | OwnerAttributeNumber15 | ATTRIBUTE_NUMBER15 | — | ✅ |
| 54 | OwnerAttributeNumber16 | ATTRIBUTE_NUMBER16 | — | ✅ |
| 55 | OwnerAttributeNumber17 | ATTRIBUTE_NUMBER17 | — | ✅ |
| 56 | OwnerAttributeNumber18 | ATTRIBUTE_NUMBER18 | — | ✅ |
| 57 | OwnerAttributeNumber19 | ATTRIBUTE_NUMBER19 | — | ✅ |
| 58 | OwnerAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 59 | OwnerAttributeNumber20 | ATTRIBUTE_NUMBER20 | — | ✅ |
| 60 | OwnerAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 61 | OwnerAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 62 | OwnerAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 63 | OwnerAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 64 | OwnerAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 65 | OwnerAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 66 | OwnerAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 67 | OwnerBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 68 | OwnerCreatedBy | CREATED_BY | — | ✅ |
| 69 | OwnerCreationDate | CREATION_DATE | — | ✅ |
| 70 | OwnerDisplayName | DISPLAY_NAME | — | ✅ |
| 71 | OwnerEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 72 | OwnerEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 73 | OwnerFirstName | FIRST_NAME | — | ✅ |
| 74 | OwnerFullName | FULL_NAME | — | ✅ |
| 75 | OwnerHonors | HONORS | — | ✅ |
| 76 | OwnerKnownAs | KNOWN_AS | — | ✅ |
| 77 | OwnerLastName | LAST_NAME | — | ✅ |
| 78 | OwnerLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 79 | OwnerLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 80 | OwnerLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 81 | OwnerLegislationCode | LEGISLATION_CODE | — | ✅ |
| 82 | OwnerListName | LIST_NAME | — | ✅ |
| 83 | OwnerMiddleNames | MIDDLE_NAMES | — | ✅ |
| 84 | OwnerMilitaryRank | MILITARY_RANK | — | ✅ |
| 85 | OwnerNamInformation1 | NAM_INFORMATION1 | — | ✅ |
| 86 | OwnerNamInformation10 | NAM_INFORMATION10 | — | ✅ |
| 87 | OwnerNamInformation11 | NAM_INFORMATION11 | — | ✅ |
| 88 | OwnerNamInformation12 | NAM_INFORMATION12 | — | ✅ |
| 89 | OwnerNamInformation13 | NAM_INFORMATION13 | — | ✅ |
| 90 | OwnerNamInformation14 | NAM_INFORMATION14 | — | ✅ |
| 91 | OwnerNamInformation15 | NAM_INFORMATION15 | — | ✅ |
| 92 | OwnerNamInformation16 | NAM_INFORMATION16 | — | ✅ |
| 93 | OwnerNamInformation17 | NAM_INFORMATION17 | — | ✅ |
| 94 | OwnerNamInformation18 | NAM_INFORMATION18 | — | ✅ |
| 95 | OwnerNamInformation19 | NAM_INFORMATION19 | — | ✅ |
| 96 | OwnerNamInformation2 | NAM_INFORMATION2 | — | ✅ |
| 97 | OwnerNamInformation20 | NAM_INFORMATION20 | — | ✅ |
| 98 | OwnerNamInformation21 | NAM_INFORMATION21 | — | ✅ |
| 99 | OwnerNamInformation22 | NAM_INFORMATION22 | — | ✅ |
| 100 | OwnerNamInformation23 | NAM_INFORMATION23 | — | ✅ |
| 101 | OwnerNamInformation24 | NAM_INFORMATION24 | — | ✅ |
| 102 | OwnerNamInformation25 | NAM_INFORMATION25 | — | ✅ |
| 103 | OwnerNamInformation26 | NAM_INFORMATION26 | — | ✅ |
| 104 | OwnerNamInformation27 | NAM_INFORMATION27 | — | ✅ |
| 105 | OwnerNamInformation28 | NAM_INFORMATION28 | — | ✅ |
| 106 | OwnerNamInformation29 | NAM_INFORMATION29 | — | ✅ |
| 107 | OwnerNamInformation3 | NAM_INFORMATION3 | — | ✅ |
| 108 | OwnerNamInformation30 | NAM_INFORMATION30 | — | ✅ |
| 109 | OwnerNamInformation4 | NAM_INFORMATION4 | — | ✅ |
| 110 | OwnerNamInformation5 | NAM_INFORMATION5 | — | ✅ |
| 111 | OwnerNamInformation6 | NAM_INFORMATION6 | — | ✅ |
| 112 | OwnerNamInformation7 | NAM_INFORMATION7 | — | ✅ |
| 113 | OwnerNamInformation8 | NAM_INFORMATION8 | — | ✅ |
| 114 | OwnerNamInformation9 | NAM_INFORMATION9 | — | ✅ |
| 115 | OwnerNamInformationCategory | NAM_INFORMATION_CATEGORY | — | ✅ |
| 116 | OwnerNameType | NAME_TYPE | — | ✅ |
| 117 | OwnerObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 118 | OwnerOrderName | ORDER_NAME | — | ✅ |
| 119 | OwnerPersonId | PERSON_ID | — | ✅ |
| 120 | OwnerPersonNameId | PERSON_NAME_ID | — | ✅ |
| 121 | OwnerPreNameAdjunct | PRE_NAME_ADJUNCT | — | ✅ |
| 122 | OwnerPreviousLastName | PREVIOUS_LAST_NAME | — | ✅ |
| 123 | OwnerSuffix | SUFFIX | — | ✅ |
| 124 | OwnerTitle | TITLE | — | ✅ |

### [[poq_qual_areas_vl|POQ_QUAL_AREAS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QualAreaActivationDate | ACTIVATION_DATE | — | ✅ |
| 2 | QualAreaCreatedBy | CREATED_BY | — | ✅ |
| 3 | QualAreaCreationDate | CREATION_DATE | — | ✅ |
| 4 | QualAreaExpirationReminderPeriod | EXPIRATION_REMINDER_PERIOD | — | ✅ |
| 5 | QualAreaExpirationReminderType | EXPIRATION_REMINDER_TYPE | — | ✅ |
| 6 | QualAreaGlobalFlag | GLOBAL_FLAG | — | ✅ |
| 7 | QualAreaInformationOnlyFlag | INFORMATION_ONLY_FLAG | — | ✅ |
| 8 | QualAreaLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | QualAreaLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | QualAreaLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | QualAreaLatestRevisionFlag | LATEST_REVISION_FLAG | — | ✅ |
| 12 | QualAreaObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | QualAreaOriginalQualAreaId | ORIGINAL_QUAL_AREA_ID | — | ✅ |
| 14 | QualAreaOwnerId1 | OWNER_ID | — | ✅ |
| 15 | QualAreaPrcBuId | PRC_BU_ID | — | ✅ |
| 16 | QualAreaQualAreaDescription | QUAL_AREA_DESCRIPTION | — | ✅ |
| 17 | QualAreaQualAreaId | QUAL_AREA_ID | — | ✅ |
| 18 | QualAreaQualAreaLevel | QUAL_AREA_LEVEL | — | ✅ |
| 19 | QualAreaQualAreaName | QUAL_AREA_NAME | — | ✅ |
| 20 | QualAreaQualAreaStatus | QUAL_AREA_STATUS | — | ✅ |
| 21 | QualAreaRevisionNumber | REVISION_NUMBER | — | ✅ |
| 22 | QualAreaStdsOrgCode | STDS_ORG_CODE | — | ✅ |
| 23 | QualAreaSubjectCode | SUBJECT_CODE | — | ✅ |
| 24 | QualAreaUsageCode | QUAL_AREA_USAGE_CODE | — | — |

### [[poq_qual_area_questions|POQ_QUAL_AREA_QUESTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QualAreaQuestionCreatedBy | CREATED_BY | — | ✅ |
| 2 | QualAreaQuestionCreationDate | CREATION_DATE | — | ✅ |
| 3 | QualAreaQuestionDisplaySequence | DISPLAY_SEQUENCE | — | ✅ |
| 4 | QualAreaQuestionId | QUAL_AREA_QUESTION_ID | 🔑 | ✅ |
| 5 | QualAreaQuestionKnockoutScore | KNOCKOUT_SCORE | — | ✅ |
| 6 | QualAreaQuestionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | QualAreaQuestionLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | QualAreaQuestionLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | QualAreaQuestionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | QualAreaQuestionQualAreaId | QUAL_AREA_ID | — | ✅ |
| 11 | QualAreaQuestionQuestionId | QUESTION_ID | — | ✅ |
| 12 | QualAreaQuestionWeight | WEIGHT | — | ✅ |

### [[poq_questions_vl|POQ_QUESTIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChildQuestionActivationDate | ACTIVATION_DATE | — | ✅ |
| 2 | ChildQuestionAllowRespCommentFlag | ALLOW_RESP_COMMENT_FLAG | — | ✅ |
| 3 | ChildQuestionAttachmentAllowedCode | ATTACHMENT_ALLOWED_CODE | — | ✅ |
| 4 | ChildQuestionCreatedBy | CREATED_BY | — | ✅ |
| 5 | ChildQuestionCreationDate | CREATION_DATE | — | ✅ |
| 6 | ChildQuestionCreationSource | CREATION_SOURCE | — | — |
| 7 | ChildQuestionCriticalQuestionFlag | CRITICAL_QUESTION_FLAG | — | ✅ |
| 8 | ChildQuestionDisplayPreferredRespFlag | DISPLAY_PREFERRED_RESP_FLAG | — | ✅ |
| 9 | ChildQuestionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | ChildQuestionLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | ChildQuestionLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | ChildQuestionLatestRevisionFlag | LATEST_REVISION_FLAG | — | ✅ |
| 13 | ChildQuestionMaximumScore | MAXIMUM_SCORE | — | ✅ |
| 14 | ChildQuestionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 15 | ChildQuestionOriginalQuestionId | ORIGINAL_QUESTION_ID | — | ✅ |
| 16 | ChildQuestionOwnerId | OWNER_ID | — | ✅ |
| 17 | ChildQuestionPreferredResponseDate | PREFERRED_RESPONSE_DATE | — | ✅ |
| 18 | ChildQuestionPreferredResponseDatetime | PREFERRED_RESPONSE_DATETIME | — | ✅ |
| 19 | ChildQuestionPreferredResponseNumber | PREFERRED_RESPONSE_NUMBER | — | ✅ |
| 20 | ChildQuestionPreferredResponseText | PREFERRED_RESPONSE_TEXT | — | ✅ |
| 21 | ChildQuestionQuestionHint | QUESTION_HINT | — | ✅ |
| 22 | ChildQuestionQuestionId | QUESTION_ID | 🔑 | ✅ |
| 23 | ChildQuestionQuestionLevel | QUESTION_LEVEL | — | ✅ |
| 24 | ChildQuestionQuestionName | QUESTION_NAME | — | ✅ |
| 25 | ChildQuestionQuestionStatus | QUESTION_STATUS | — | ✅ |
| 26 | ChildQuestionQuestionText | QUESTION_TEXT | — | ✅ |
| 27 | ChildQuestionQuestionType | QUESTION_TYPE | — | ✅ |
| 28 | ChildQuestionResponderType | RESPONDER_TYPE | — | ✅ |
| 29 | ChildQuestionResponseRequiredFlag | RESPONSE_REQUIRED_FLAG | — | ✅ |
| 30 | ChildQuestionResponseType | RESPONSE_TYPE | — | ✅ |
| 31 | ChildQuestionRevisionNumber | REVISION_NUMBER | — | ✅ |
| 32 | ChildQuestionScoreForNoResponse | SCORE_FOR_NO_RESPONSE | — | ✅ |
| 33 | ChildQuestionScoringApproach | SCORING_APPROACH | — | ✅ |
| 34 | ChildQuestionScoringMethod | SCORING_METHOD | — | ✅ |
| 35 | ChildQuestionStdsOrgCode | STDS_ORG_CODE | — | ✅ |
| 36 | ChildQuestionSubjectCode | SUBJECT_CODE | — | ✅ |
| 37 | ChildQuestionSupplierAttributeCode | SUPPLIER_ATTRIBUTE_CODE | — | ✅ |
| 38 | ChildQuestionSupplierAttributeFlag | SUPPLIER_ATTRIBUTE_FLAG | — | ✅ |
| 39 | CreationSource | CREATION_SOURCE | — | — |
| 40 | QuestionActivationDate | ACTIVATION_DATE | — | ✅ |
| 41 | QuestionAllowRespCommentFlag | ALLOW_RESP_COMMENT_FLAG | — | ✅ |
| 42 | QuestionAttachmentAllowedCode | ATTACHMENT_ALLOWED_CODE | — | ✅ |
| 43 | QuestionCreatedBy | CREATED_BY | — | ✅ |
| 44 | QuestionCreationDate | CREATION_DATE | — | ✅ |
| 45 | QuestionCriticalQuestionFlag | CRITICAL_QUESTION_FLAG | — | ✅ |
| 46 | QuestionDisplayPreferredRespFlag | DISPLAY_PREFERRED_RESP_FLAG | — | ✅ |
| 47 | QuestionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 48 | QuestionLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 49 | QuestionLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 50 | QuestionLatestRevisionFlag | LATEST_REVISION_FLAG | — | ✅ |
| 51 | QuestionMaximumScore | MAXIMUM_SCORE | — | ✅ |
| 52 | QuestionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 53 | QuestionOriginalQuestionId | ORIGINAL_QUESTION_ID | — | ✅ |
| 54 | QuestionOwnerId | OWNER_ID | — | ✅ |
| 55 | QuestionPreferredResponseDate | PREFERRED_RESPONSE_DATE | — | ✅ |
| 56 | QuestionPreferredResponseDatetime | PREFERRED_RESPONSE_DATETIME | — | ✅ |
| 57 | QuestionPreferredResponseNumber | PREFERRED_RESPONSE_NUMBER | — | ✅ |
| 58 | QuestionPreferredResponseText | PREFERRED_RESPONSE_TEXT | — | ✅ |
| 59 | QuestionQuestionHint | QUESTION_HINT | — | ✅ |
| 60 | QuestionQuestionId | QUESTION_ID | — | ✅ |
| 61 | QuestionQuestionLevel | QUESTION_LEVEL | — | ✅ |
| 62 | QuestionQuestionName | QUESTION_NAME | — | ✅ |
| 63 | QuestionQuestionStatus | QUESTION_STATUS | — | ✅ |
| 64 | QuestionQuestionText | QUESTION_TEXT | — | ✅ |
| 65 | QuestionQuestionType | QUESTION_TYPE | — | ✅ |
| 66 | QuestionResponderType | RESPONDER_TYPE | — | ✅ |
| 67 | QuestionResponseRequiredFlag | RESPONSE_REQUIRED_FLAG | — | ✅ |
| 68 | QuestionResponseType | RESPONSE_TYPE | — | ✅ |
| 69 | QuestionRevisionNumber | REVISION_NUMBER | — | ✅ |
| 70 | QuestionScoreForNoResponse | SCORE_FOR_NO_RESPONSE | — | ✅ |
| 71 | QuestionScoringApproach | SCORING_APPROACH | — | ✅ |
| 72 | QuestionScoringMethod | SCORING_METHOD | — | ✅ |
| 73 | QuestionStdsOrgCode | STDS_ORG_CODE | — | ✅ |
| 74 | QuestionSubjectCode | SUBJECT_CODE | — | ✅ |
| 75 | QuestionSupplierAttributeCode | SUPPLIER_ATTRIBUTE_CODE | — | ✅ |
| 76 | QuestionSupplierAttributeFlag | SUPPLIER_ATTRIBUTE_FLAG | — | ✅ |
| 77 | QuestionSurveyFlag | QUESTION_SURVEY_FLAG | — | ✅ |

### [[poq_question_structure_v|POQ_QUESTION_STRUCTURE_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QuestionStructureBranchLevel | BRANCH_LEVEL | — | ✅ |
| 2 | QuestionStructureQuestionId | QUESTION_ID | — | ✅ |
| 3 | QuestionStructureRootQuestionId | ROOT_QUESTION_ID | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
