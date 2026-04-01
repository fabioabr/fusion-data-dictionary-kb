---
id: DOC-PO-PVO-InitiativePVO
doc_type: system-doc
title: "InitiativePVO — PVO Purchasing"
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
  - InitiativePVO
  - initiativepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InitiativePVO

## 📌 Visão Geral

Extrai as iniciativas de qualificação de fornecedores, incluindo nome, responsável, datas e critérios. Permite gestão de campanhas de qualificação e acompanhamento de resultados por programa.

**Caminho:** `FscmTopModelAM.PrcPoqPublicViewAM.InitiativePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 205 | 2 | 1 | 204 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 124 atributos (124 BICC)
- [[poq_initiatives|POQ_INITIATIVES]] — 81 atributos (1 PKs, 80 BICC)

---

## ⚙️ Atributos

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CanceledByAttribute1 | ATTRIBUTE1 | — | ✅ |
| 2 | CanceledByAttribute10 | ATTRIBUTE10 | — | ✅ |
| 3 | CanceledByAttribute11 | ATTRIBUTE11 | — | ✅ |
| 4 | CanceledByAttribute12 | ATTRIBUTE12 | — | ✅ |
| 5 | CanceledByAttribute13 | ATTRIBUTE13 | — | ✅ |
| 6 | CanceledByAttribute14 | ATTRIBUTE14 | — | ✅ |
| 7 | CanceledByAttribute15 | ATTRIBUTE15 | — | ✅ |
| 8 | CanceledByAttribute16 | ATTRIBUTE16 | — | ✅ |
| 9 | CanceledByAttribute17 | ATTRIBUTE17 | — | ✅ |
| 10 | CanceledByAttribute18 | ATTRIBUTE18 | — | ✅ |
| 11 | CanceledByAttribute19 | ATTRIBUTE19 | — | ✅ |
| 12 | CanceledByAttribute2 | ATTRIBUTE2 | — | ✅ |
| 13 | CanceledByAttribute20 | ATTRIBUTE20 | — | ✅ |
| 14 | CanceledByAttribute21 | ATTRIBUTE21 | — | ✅ |
| 15 | CanceledByAttribute22 | ATTRIBUTE22 | — | ✅ |
| 16 | CanceledByAttribute23 | ATTRIBUTE23 | — | ✅ |
| 17 | CanceledByAttribute24 | ATTRIBUTE24 | — | ✅ |
| 18 | CanceledByAttribute25 | ATTRIBUTE25 | — | ✅ |
| 19 | CanceledByAttribute26 | ATTRIBUTE26 | — | ✅ |
| 20 | CanceledByAttribute27 | ATTRIBUTE27 | — | ✅ |
| 21 | CanceledByAttribute28 | ATTRIBUTE28 | — | ✅ |
| 22 | CanceledByAttribute29 | ATTRIBUTE29 | — | ✅ |
| 23 | CanceledByAttribute3 | ATTRIBUTE3 | — | ✅ |
| 24 | CanceledByAttribute30 | ATTRIBUTE30 | — | ✅ |
| 25 | CanceledByAttribute4 | ATTRIBUTE4 | — | ✅ |
| 26 | CanceledByAttribute5 | ATTRIBUTE5 | — | ✅ |
| 27 | CanceledByAttribute6 | ATTRIBUTE6 | — | ✅ |
| 28 | CanceledByAttribute7 | ATTRIBUTE7 | — | ✅ |
| 29 | CanceledByAttribute8 | ATTRIBUTE8 | — | ✅ |
| 30 | CanceledByAttribute9 | ATTRIBUTE9 | — | ✅ |
| 31 | CanceledByAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 32 | CanceledByAttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 33 | CanceledByAttributeDate10 | ATTRIBUTE_DATE10 | — | ✅ |
| 34 | CanceledByAttributeDate11 | ATTRIBUTE_DATE11 | — | ✅ |
| 35 | CanceledByAttributeDate12 | ATTRIBUTE_DATE12 | — | ✅ |
| 36 | CanceledByAttributeDate13 | ATTRIBUTE_DATE13 | — | ✅ |
| 37 | CanceledByAttributeDate14 | ATTRIBUTE_DATE14 | — | ✅ |
| 38 | CanceledByAttributeDate15 | ATTRIBUTE_DATE15 | — | ✅ |
| 39 | CanceledByAttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 40 | CanceledByAttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 41 | CanceledByAttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 42 | CanceledByAttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 43 | CanceledByAttributeDate6 | ATTRIBUTE_DATE6 | — | ✅ |
| 44 | CanceledByAttributeDate7 | ATTRIBUTE_DATE7 | — | ✅ |
| 45 | CanceledByAttributeDate8 | ATTRIBUTE_DATE8 | — | ✅ |
| 46 | CanceledByAttributeDate9 | ATTRIBUTE_DATE9 | — | ✅ |
| 47 | CanceledByAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 48 | CanceledByAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 49 | CanceledByAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | ✅ |
| 50 | CanceledByAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | ✅ |
| 51 | CanceledByAttributeNumber13 | ATTRIBUTE_NUMBER13 | — | ✅ |
| 52 | CanceledByAttributeNumber14 | ATTRIBUTE_NUMBER14 | — | ✅ |
| 53 | CanceledByAttributeNumber15 | ATTRIBUTE_NUMBER15 | — | ✅ |
| 54 | CanceledByAttributeNumber16 | ATTRIBUTE_NUMBER16 | — | ✅ |
| 55 | CanceledByAttributeNumber17 | ATTRIBUTE_NUMBER17 | — | ✅ |
| 56 | CanceledByAttributeNumber18 | ATTRIBUTE_NUMBER18 | — | ✅ |
| 57 | CanceledByAttributeNumber19 | ATTRIBUTE_NUMBER19 | — | ✅ |
| 58 | CanceledByAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 59 | CanceledByAttributeNumber20 | ATTRIBUTE_NUMBER20 | — | ✅ |
| 60 | CanceledByAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 61 | CanceledByAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 62 | CanceledByAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 63 | CanceledByAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 64 | CanceledByAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 65 | CanceledByAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 66 | CanceledByAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 67 | CanceledByBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 68 | CanceledByCreatedBy | CREATED_BY | — | ✅ |
| 69 | CanceledByCreationDate | CREATION_DATE | — | ✅ |
| 70 | CanceledByDisplayName | DISPLAY_NAME | — | ✅ |
| 71 | CanceledByEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 72 | CanceledByEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 73 | CanceledByFirstName | FIRST_NAME | — | ✅ |
| 74 | CanceledByFullName | FULL_NAME | — | ✅ |
| 75 | CanceledByHonors | HONORS | — | ✅ |
| 76 | CanceledByKnownAs | KNOWN_AS | — | ✅ |
| 77 | CanceledByLastName | LAST_NAME | — | ✅ |
| 78 | CanceledByLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 79 | CanceledByLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 80 | CanceledByLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 81 | CanceledByLegislationCode | LEGISLATION_CODE | — | ✅ |
| 82 | CanceledByListName | LIST_NAME | — | ✅ |
| 83 | CanceledByMiddleNames | MIDDLE_NAMES | — | ✅ |
| 84 | CanceledByMilitaryRank | MILITARY_RANK | — | ✅ |
| 85 | CanceledByNamInformation1 | NAM_INFORMATION1 | — | ✅ |
| 86 | CanceledByNamInformation10 | NAM_INFORMATION10 | — | ✅ |
| 87 | CanceledByNamInformation11 | NAM_INFORMATION11 | — | ✅ |
| 88 | CanceledByNamInformation12 | NAM_INFORMATION12 | — | ✅ |
| 89 | CanceledByNamInformation13 | NAM_INFORMATION13 | — | ✅ |
| 90 | CanceledByNamInformation14 | NAM_INFORMATION14 | — | ✅ |
| 91 | CanceledByNamInformation15 | NAM_INFORMATION15 | — | ✅ |
| 92 | CanceledByNamInformation16 | NAM_INFORMATION16 | — | ✅ |
| 93 | CanceledByNamInformation17 | NAM_INFORMATION17 | — | ✅ |
| 94 | CanceledByNamInformation18 | NAM_INFORMATION18 | — | ✅ |
| 95 | CanceledByNamInformation19 | NAM_INFORMATION19 | — | ✅ |
| 96 | CanceledByNamInformation2 | NAM_INFORMATION2 | — | ✅ |
| 97 | CanceledByNamInformation20 | NAM_INFORMATION20 | — | ✅ |
| 98 | CanceledByNamInformation21 | NAM_INFORMATION21 | — | ✅ |
| 99 | CanceledByNamInformation22 | NAM_INFORMATION22 | — | ✅ |
| 100 | CanceledByNamInformation23 | NAM_INFORMATION23 | — | ✅ |
| 101 | CanceledByNamInformation24 | NAM_INFORMATION24 | — | ✅ |
| 102 | CanceledByNamInformation25 | NAM_INFORMATION25 | — | ✅ |
| 103 | CanceledByNamInformation26 | NAM_INFORMATION26 | — | ✅ |
| 104 | CanceledByNamInformation27 | NAM_INFORMATION27 | — | ✅ |
| 105 | CanceledByNamInformation28 | NAM_INFORMATION28 | — | ✅ |
| 106 | CanceledByNamInformation29 | NAM_INFORMATION29 | — | ✅ |
| 107 | CanceledByNamInformation3 | NAM_INFORMATION3 | — | ✅ |
| 108 | CanceledByNamInformation30 | NAM_INFORMATION30 | — | ✅ |
| 109 | CanceledByNamInformation4 | NAM_INFORMATION4 | — | ✅ |
| 110 | CanceledByNamInformation5 | NAM_INFORMATION5 | — | ✅ |
| 111 | CanceledByNamInformation6 | NAM_INFORMATION6 | — | ✅ |
| 112 | CanceledByNamInformation7 | NAM_INFORMATION7 | — | ✅ |
| 113 | CanceledByNamInformation8 | NAM_INFORMATION8 | — | ✅ |
| 114 | CanceledByNamInformation9 | NAM_INFORMATION9 | — | ✅ |
| 115 | CanceledByNamInformationCategory | NAM_INFORMATION_CATEGORY | — | ✅ |
| 116 | CanceledByNameType | NAME_TYPE | — | ✅ |
| 117 | CanceledByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 118 | CanceledByOrderName | ORDER_NAME | — | ✅ |
| 119 | CanceledByPersonId | PERSON_ID | — | ✅ |
| 120 | CanceledByPersonNameId | PERSON_NAME_ID | — | ✅ |
| 121 | CanceledByPreNameAdjunct | PRE_NAME_ADJUNCT | — | ✅ |
| 122 | CanceledByPreviousLastName | PREVIOUS_LAST_NAME | — | ✅ |
| 123 | CanceledBySuffix | SUFFIX | — | ✅ |
| 124 | CanceledByTitle | TITLE | — | ✅ |

### [[poq_initiatives|POQ_INITIATIVES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InitiativeAssessmentEvalDueDate | ASSESSMENT_EVAL_DUE_DATE | — | ✅ |
| 2 | InitiativeAssessmentOwnerId | ASSESSMENT_OWNER_ID | — | ✅ |
| 3 | InitiativeAttribute1 | ATTRIBUTE1 | — | ✅ |
| 4 | InitiativeAttribute10 | ATTRIBUTE10 | — | ✅ |
| 5 | InitiativeAttribute11 | ATTRIBUTE11 | — | ✅ |
| 6 | InitiativeAttribute12 | ATTRIBUTE12 | — | ✅ |
| 7 | InitiativeAttribute13 | ATTRIBUTE13 | — | ✅ |
| 8 | InitiativeAttribute14 | ATTRIBUTE14 | — | ✅ |
| 9 | InitiativeAttribute15 | ATTRIBUTE15 | — | ✅ |
| 10 | InitiativeAttribute16 | ATTRIBUTE16 | — | ✅ |
| 11 | InitiativeAttribute17 | ATTRIBUTE17 | — | ✅ |
| 12 | InitiativeAttribute18 | ATTRIBUTE18 | — | ✅ |
| 13 | InitiativeAttribute19 | ATTRIBUTE19 | — | ✅ |
| 14 | InitiativeAttribute2 | ATTRIBUTE2 | — | ✅ |
| 15 | InitiativeAttribute20 | ATTRIBUTE20 | — | ✅ |
| 16 | InitiativeAttribute3 | ATTRIBUTE3 | — | ✅ |
| 17 | InitiativeAttribute4 | ATTRIBUTE4 | — | ✅ |
| 18 | InitiativeAttribute5 | ATTRIBUTE5 | — | ✅ |
| 19 | InitiativeAttribute6 | ATTRIBUTE6 | — | ✅ |
| 20 | InitiativeAttribute7 | ATTRIBUTE7 | — | ✅ |
| 21 | InitiativeAttribute8 | ATTRIBUTE8 | — | ✅ |
| 22 | InitiativeAttribute9 | ATTRIBUTE9 | — | ✅ |
| 23 | InitiativeAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 24 | InitiativeAttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 25 | InitiativeAttributeDate10 | ATTRIBUTE_DATE10 | — | ✅ |
| 26 | InitiativeAttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 27 | InitiativeAttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 28 | InitiativeAttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 29 | InitiativeAttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 30 | InitiativeAttributeDate6 | ATTRIBUTE_DATE6 | — | ✅ |
| 31 | InitiativeAttributeDate7 | ATTRIBUTE_DATE7 | — | ✅ |
| 32 | InitiativeAttributeDate8 | ATTRIBUTE_DATE8 | — | ✅ |
| 33 | InitiativeAttributeDate9 | ATTRIBUTE_DATE9 | — | ✅ |
| 34 | InitiativeAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 35 | InitiativeAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 36 | InitiativeAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 37 | InitiativeAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 38 | InitiativeAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 39 | InitiativeAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 40 | InitiativeAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 41 | InitiativeAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 42 | InitiativeAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 43 | InitiativeAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 44 | InitiativeAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 45 | InitiativeAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | ✅ |
| 46 | InitiativeAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 47 | InitiativeAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 48 | InitiativeAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 49 | InitiativeAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 50 | InitiativeAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | ✅ |
| 51 | InitiativeAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | ✅ |
| 52 | InitiativeAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | ✅ |
| 53 | InitiativeAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | ✅ |
| 54 | InitiativeAutoAcceptResponsesFlag | AUTO_ACCEPT_RESPONSES_FLAG | — | ✅ |
| 55 | InitiativeAutoPopulateResponsesFlag | AUTO_POPULATE_RESPONSES_FLAG | — | ✅ |
| 56 | InitiativeCanceledBy | CANCELED_BY | — | ✅ |
| 57 | InitiativeCanceledDate | CANCELED_DATE | — | ✅ |
| 58 | InitiativeCanceledReasonCode | CANCELED_REASON_CODE | — | ✅ |
| 59 | InitiativeCompletedDate | COMPLETED_DATE | — | ✅ |
| 60 | InitiativeCreatedBy | CREATED_BY | — | ✅ |
| 61 | InitiativeCreationDate | CREATION_DATE | — | ✅ |
| 62 | InitiativeCreationSource | CREATION_SOURCE | — | ✅ |
| 63 | InitiativeDescription | DESCRIPTION | — | ✅ |
| 64 | InitiativeId | INITIATIVE_ID | 🔑 | ✅ |
| 65 | InitiativeInitiativeNumber | INITIATIVE_NUMBER | — | ✅ |
| 66 | InitiativeInternalNote | INTERNAL_NOTE | — | ✅ |
| 67 | InitiativeLastOverdueReminderDate | LAST_OVERDUE_REMINDER_DATE | — | ✅ |
| 68 | InitiativeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 69 | InitiativeLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 70 | InitiativeLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 71 | InitiativeLaunchDate | LAUNCH_DATE | — | ✅ |
| 72 | InitiativeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 73 | InitiativeOwnerId | OWNER_ID | — | ✅ |
| 74 | InitiativePrcBuId | PRC_BU_ID | — | ✅ |
| 75 | InitiativeQualModelId | QUAL_MODEL_ID | — | ✅ |
| 76 | InitiativeReuseActiveQualFlag | REUSE_ACTIVE_QUAL_FLAG | — | ✅ |
| 77 | InitiativeStatus | STATUS | — | ✅ |
| 78 | InitiativeSurveyFlag | INITIATIVE_SURVEY_FLAG | — | ✅ |
| 79 | InitiativeTitle | TITLE | — | ✅ |
| 80 | InitiativeType | TYPE | — | ✅ |
| 81 | InitiativeUsageCode | INITIATIVE_USAGE_CODE | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
