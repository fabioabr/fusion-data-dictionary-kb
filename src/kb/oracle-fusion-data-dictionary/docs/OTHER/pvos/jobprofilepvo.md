---
id: DOC-OTHER-PVO-JobProfilePVO
doc_type: system-doc
title: "JobProfilePVO — PVO Cross-Module"
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
  - JobProfilePVO
  - jobprofilepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# JobProfilePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Job Profile. Acessa as tabelas: HRT_PROFILES_B, HRT_PROFILES_TL, HRT_PROFILE_RELATIONS (+2).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmProfileCoreAM.JobProfilePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 65 | 5 | 1 | 8 | 12% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_profiles_b|HRT_PROFILES_B]] — 15 atributos (1 PKs, 2 BICC)
- [[hrt_profiles_tl|HRT_PROFILES_TL]] — 12 atributos (2 BICC)
- [[hrt_profile_relations|HRT_PROFILE_RELATIONS]] — 13 atributos (2 BICC)
- [[hrt_relation_config_b|HRT_RELATION_CONFIG_B]] — 14 atributos (1 BICC)
- [[hrt_relation_config_tl|HRT_RELATION_CONFIG_TL]] — 11 atributos (1 BICC)

---

## ⚙️ Atributos

### [[hrt_profiles_b|HRT_PROFILES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProfileBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ProfileBPEOCreatedBy | CREATED_BY | — | — |
| 3 | ProfileBPEOCreationDate | CREATION_DATE | — | — |
| 4 | ProfileBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ProfileBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | ProfileBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | ProfileBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | ProfileBPEOOwnerPersonId | OWNER_PERSON_ID | — | — |
| 9 | ProfileBPEOPartyId | PARTY_ID | — | — |
| 10 | ProfileBPEOPersonId | PERSON_ID | — | — |
| 11 | ProfileBPEOProfileCode | PROFILE_CODE | — | — |
| 12 | ProfileBPEOProfileId | PROFILE_ID | 🔑 | ✅ |
| 13 | ProfileBPEOProfileTypeId | PROFILE_TYPE_ID | — | — |
| 14 | ProfileBPEOProfileUsageCode | PROFILE_USAGE_CODE | — | — |
| 15 | ProfileBPEOReviewRequiredFlag | REVIEW_REQD_FLAG | — | — |

### [[hrt_profiles_tl|HRT_PROFILES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProfileTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ProfileTranslationPEOCreatedBy | CREATED_BY | — | — |
| 3 | ProfileTranslationPEOCreationDate | CREATION_DATE | — | — |
| 4 | ProfileTranslationPEODescription | DESCRIPTION | — | ✅ |
| 5 | ProfileTranslationPEOLanguage | LANGUAGE | — | — |
| 6 | ProfileTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ProfileTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | ProfileTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ProfileTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | ProfileTranslationPEOProfileId | PROFILE_ID | — | — |
| 11 | ProfileTranslationPEOSourceLang | SOURCE_LANG | — | — |
| 12 | ProfileTranslationPEOSummary | SUMMARY | — | — |

### [[hrt_profile_relations|HRT_PROFILE_RELATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProfileRelationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ProfileRelationPEOCreatedBy | CREATED_BY | — | — |
| 3 | ProfileRelationPEOCreationDate | CREATION_DATE | — | — |
| 4 | ProfileRelationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ProfileRelationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | ProfileRelationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | ProfileRelationPEOObjectEffEndDate | OBJECT_EFF_END_DATE | — | — |
| 8 | ProfileRelationPEOObjectEffStartDate | OBJECT_EFF_START_DATE | — | — |
| 9 | ProfileRelationPEOObjectId | OBJECT_ID | — | ✅ |
| 10 | ProfileRelationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | ProfileRelationPEOProfileId | PROFILE_ID | — | — |
| 12 | ProfileRelationPEOProfileRelationId | PROFILE_RELATION_ID | — | — |
| 13 | ProfileRelationPEORelationId | RELATION_ID | — | — |

### [[hrt_relation_config_b|HRT_RELATION_CONFIG_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RelationConfigBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | RelationConfigBPEOCreatedBy | CREATED_BY | — | — |
| 3 | RelationConfigBPEOCreationDate | CREATION_DATE | — | — |
| 4 | RelationConfigBPEOEnabledFlag | ENABLED_FLAG | — | — |
| 5 | RelationConfigBPEOKeyTableName | KEY_TABLE_NAME | — | — |
| 6 | RelationConfigBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | RelationConfigBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | RelationConfigBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | RelationConfigBPEOModuleId | MODULE_ID | — | — |
| 10 | RelationConfigBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | RelationConfigBPEORelationCode | RELATION_CODE | — | — |
| 12 | RelationConfigBPEORelationId | RELATION_ID | — | — |
| 13 | RelationConfigBPEORelationSeqNumber | RELATION_SEQ_NUMBER | — | — |
| 14 | RelationConfigBPEORelationTypeCode | RELATION_TYPE_CODE | — | — |

### [[hrt_relation_config_tl|HRT_RELATION_CONFIG_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RelationConfigTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | RelationConfigTranslationPEOCreatedBy | CREATED_BY | — | — |
| 3 | RelationConfigTranslationPEOCreationDate | CREATION_DATE | — | — |
| 4 | RelationConfigTranslationPEODescription | DESCRIPTION | — | — |
| 5 | RelationConfigTranslationPEOLanguage | LANGUAGE | — | — |
| 6 | RelationConfigTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | RelationConfigTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | RelationConfigTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | RelationConfigTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | RelationConfigTranslationPEORelationId | RELATION_ID | — | — |
| 11 | RelationConfigTranslationPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
