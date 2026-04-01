---
id: DOC-HCM-PVO-CandidatePVO
doc_type: system-doc
title: "CandidatePVO — PVO Human Capital Management"
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
  - CandidatePVO
  - candidatepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CandidatePVO

## 📌 Visão Geral

View Object principal de candidatos com perfil, rastreamento de busca e ultima interacao. Base para gestao completa do ciclo de vida do candidato.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecCandidatesAM.CandidatePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 101 | 7 | 1 | 67 | 66% |

---

## 🔗 Tabelas Relacionadas

- [[irc_candidates|IRC_CANDIDATES]] — 35 atributos (1 PKs, 29 BICC)
- [[irc_candidate_search_tracking|IRC_CANDIDATE_SEARCH_TRACKING]] — 2 atributos (1 BICC)
- [[irc_cand_last_interaction_v|IRC_CAND_LAST_INTERACTION_V]] — 2 atributos
- [[irc_cand_profile_usages_m|IRC_CAND_PROFILE_USAGES_M]] — 17 atributos (1 BICC)
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 8 atributos (2 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 23 atributos (20 BICC)
- [[per_person_type_usages_m|PER_PERSON_TYPE_USAGES_M]] — 14 atributos (14 BICC)

---

## ⚙️ Atributos

### [[irc_candidates|IRC_CANDIDATES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AddedByFlowCode | ADDED_BY_FLOW_CODE | — | ✅ |
| 2 | AvailabilityDate | AVAILABILITY_DATE | — | ✅ |
| 3 | CandLastModifiedDate | CAND_LAST_MODIFIED_DATE | — | ✅ |
| 4 | CandPEOOptInMktEmailsDate | OPT_IN_MKT_EMAILS_DATE | — | ✅ |
| 5 | CandPEOOptInMktEmailsFlag | OPT_IN_MKT_EMAILS_FLAG | — | ✅ |
| 6 | CandPrefLanguageCode | CAND_PREF_LANGUAGE_CODE | — | ✅ |
| 7 | CandidateNumber | CANDIDATE_NUMBER | — | ✅ |
| 8 | CandidatePEOCandEmailId | CAND_EMAIL_ID | — | — |
| 9 | CandidatePEOCandPhoneId | CAND_PHONE_ID | — | — |
| 10 | CandidatePEODeletedByUser | DELETED_BY_USER | — | ✅ |
| 11 | CandidatePEODeletionDate | DELETION_DATE | — | ✅ |
| 12 | CandidatePEODeletionQualifier | DELETION_QUALIFIER | — | ✅ |
| 13 | CandidatePEOEmailPreferredFlag | EMAIL_PREFERRED_FLAG | — | ✅ |
| 14 | CandidatePEOEmailVerifiedFlag | EMAIL_VERIFIED_FLAG | — | ✅ |
| 15 | CandidatePEOMergedFlag | MERGED_FLAG | — | ✅ |
| 16 | CandidatePEOPhonePreferredFlag | PHONE_PREFERRED_FLAG | — | ✅ |
| 17 | CandidatePEOPhoneVerifiedFlag | PHONE_VERIFIED_FLAG | — | ✅ |
| 18 | CandidatePEOPotentialDuplicateFlag | POTENTIAL_DUPLICATE_FLAG | — | ✅ |
| 19 | CandidatePEOVisibleToCandidateFlag | VISIBLE_TO_CANDIDATE_FLAG | — | ✅ |
| 20 | ConfirmedFlag | CONFIRMED_FLAG | — | ✅ |
| 21 | CreatedBy | CREATED_BY | — | ✅ |
| 22 | CreationDate | CREATION_DATE | — | ✅ |
| 23 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 24 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 25 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 26 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 27 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 28 | ObjectStatus | OBJECT_STATUS | — | ✅ |
| 29 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 30 | PersonId | PERSON_ID | 🔑 | ✅ |
| 31 | PrefPhoneCntTypeCode | PREF_PHONE_CNT_TYPE_CODE | — | ✅ |
| 32 | ProfileId1 | PROFILE_ID | — | — |
| 33 | RequestId | REQUEST_ID | — | — |
| 34 | SearchDate | SEARCH_DATE | — | ✅ |
| 35 | VisibleToCandidateFlag | VISIBLE_TO_CANDIDATE_FLAG | — | ✅ |

### [[irc_candidate_search_tracking|IRC_CANDIDATE_SEARCH_TRACKING]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SearchTrackingPEOCandidateId | CANDIDATE_ID | — | — |
| 2 | SearchTrackingPEOLastRetrievedDate | LAST_RETRIEVED_DATE | — | ✅ |

### [[irc_cand_last_interaction_v|IRC_CAND_LAST_INTERACTION_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CandLastInteractionInteractionId | INTERACTION_ID | — | — |
| 2 | CandLastInteractionPEOInteractionDate | INTERACTION_DATE | — | — |

### [[irc_cand_profile_usages_m|IRC_CAND_PROFILE_USAGES_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CandProfileUsageId | CAND_PROFILE_USAGE_ID | — | — |
| 2 | CreatedBy1 | CREATED_BY | — | — |
| 3 | CreationDate1 | CREATION_DATE | — | — |
| 4 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 5 | EffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | — |
| 6 | EffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 7 | EffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 8 | JobDefinitionName1 | JOB_DEFINITION_NAME | — | — |
| 9 | JobDefinitionPackage1 | JOB_DEFINITION_PACKAGE | — | — |
| 10 | LastUpdateDate1 | LAST_UPDATE_DATE | — | — |
| 11 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 12 | LastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 13 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 14 | PersonId1 | PERSON_ID | — | — |
| 15 | ProfileId | PROFILE_ID | — | ✅ |
| 16 | ProfileType | PROFILE_TYPE | — | — |
| 17 | RequestId1 | REQUEST_ID | — | — |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DeletedByPersonDetailsPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | DeletedByPersonDetailsPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | DeletedByPersonDetailsPEOPersonId | PERSON_ID | — | — |
| 4 | DeletedByPersonDetailsPEOPersonNumber | PERSON_NUMBER | — | ✅ |
| 5 | PersonDetailsPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 6 | PersonDetailsPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 7 | PersonDetailsPEOPersonId | PERSON_ID | — | — |
| 8 | PersonDetailsPEOPersonNumber | PERSON_NUMBER | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DeletedByPersonNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | DeletedByPersonNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | DeletedByPersonNamePEOFirstName | FIRST_NAME | — | ✅ |
| 4 | DeletedByPersonNamePEOFullName | FULL_NAME | — | ✅ |
| 5 | DeletedByPersonNamePEOLastName | LAST_NAME | — | ✅ |
| 6 | DeletedByPersonNamePEOPersonNameId | PERSON_NAME_ID | — | — |
| 7 | PersonNamePEOCreatedBy | CREATED_BY | — | ✅ |
| 8 | PersonNamePEOCreationDate | CREATION_DATE | — | ✅ |
| 9 | PersonNamePEODisplayName | DISPLAY_NAME | — | ✅ |
| 10 | PersonNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 11 | PersonNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 12 | PersonNamePEOFirstName | FIRST_NAME | — | ✅ |
| 13 | PersonNamePEOFullName | FULL_NAME | — | ✅ |
| 14 | PersonNamePEOLastName | LAST_NAME | — | ✅ |
| 15 | PersonNamePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | PersonNamePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 17 | PersonNamePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 18 | PersonNamePEOMiddleNames | MIDDLE_NAMES | — | ✅ |
| 19 | PersonNamePEONameType | NAME_TYPE | — | ✅ |
| 20 | PersonNamePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 21 | PersonNamePEOPersonNameId | PERSON_NAME_ID | — | ✅ |
| 22 | PersonNamePEOSuffix | SUFFIX | — | ✅ |
| 23 | PersonNamePEOTitle | TITLE | — | ✅ |

### [[per_person_type_usages_m|PER_PERSON_TYPE_USAGES_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonTypeUsagesPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | PersonTypeUsagesPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | PersonTypeUsagesPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 4 | PersonTypeUsagesPEOEffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | ✅ |
| 5 | PersonTypeUsagesPEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | ✅ |
| 6 | PersonTypeUsagesPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 7 | PersonTypeUsagesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | PersonTypeUsagesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | PersonTypeUsagesPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | PersonTypeUsagesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | PersonTypeUsagesPEOPersonId | PERSON_ID | — | ✅ |
| 12 | PersonTypeUsagesPEOPersonTypeId | PERSON_TYPE_ID | — | ✅ |
| 13 | PersonTypeUsagesPEOPersonTypeUsageId | PERSON_TYPE_USAGE_ID | — | ✅ |
| 14 | PersonTypeUsagesPEOSystemPersonType | SYSTEM_PERSON_TYPE | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
