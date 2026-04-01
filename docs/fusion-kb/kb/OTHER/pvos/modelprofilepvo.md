---
id: DOC-OTHER-PVO-ModelProfilePVO
doc_type: system-doc
title: "ModelProfilePVO — PVO Cross-Module"
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
  - ModelProfilePVO
  - modelprofilepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ModelProfilePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Model Profile. Acessa as tabelas: HRT_PROFILES_B, HRT_PROFILES_TL, HRT_PROFILE_RELATIONS (+1).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmProfileCoreAM.ModelProfilePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 40 | 4 | 3 | 35 | 88% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_profiles_b|HRT_PROFILES_B]] — 15 atributos (1 PKs, 14 BICC)
- [[hrt_profiles_tl|HRT_PROFILES_TL]] — 7 atributos (3 BICC)
- [[hrt_profile_relations|HRT_PROFILE_RELATIONS]] — 8 atributos (1 PKs, 8 BICC)
- [[hrt_profile_types_b|HRT_PROFILE_TYPES_B]] — 10 atributos (1 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[hrt_profiles_b|HRT_PROFILES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 5 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 6 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 7 | ProfileBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 8 | ProfileBPEOOwnerPersonId | OWNER_PERSON_ID | — | ✅ |
| 9 | ProfileBPEOPartyId | PARTY_ID | — | ✅ |
| 10 | ProfileBPEOPersonId | PERSON_ID | — | ✅ |
| 11 | ProfileBPEOProfileCode | PROFILE_CODE | — | ✅ |
| 12 | ProfileBPEOProfileId | PROFILE_ID | 🔑 | ✅ |
| 13 | ProfileBPEOProfileTypeId | PROFILE_TYPE_ID | — | ✅ |
| 14 | ProfileBPEOProfileUsageCode | PROFILE_USAGE_CODE | — | ✅ |
| 15 | ProfileBPEOReviewRequiredFlag | REVIEW_REQD_FLAG | — | — |

### [[hrt_profiles_tl|HRT_PROFILES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Language | LANGUAGE | — | — |
| 2 | ProfileTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | ProfileTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | ProfileTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ProfileTranslationPEOProfileId | PROFILE_ID | — | — |
| 6 | ProfileTranslationPEOSummary | SUMMARY | — | ✅ |
| 7 | SourceLang | SOURCE_LANG | — | — |

### [[hrt_profile_relations|HRT_PROFILE_RELATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProfileRelationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 2 | ProfileRelationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 3 | ProfileRelationPEOObjectEffEndDate | OBJECT_EFF_END_DATE | — | ✅ |
| 4 | ProfileRelationPEOObjectEffStartDate | OBJECT_EFF_START_DATE | — | ✅ |
| 5 | ProfileRelationPEOObjectId | OBJECT_ID | — | ✅ |
| 6 | ProfileRelationPEOProfileId | PROFILE_ID | — | ✅ |
| 7 | ProfileRelationPEOProfileRelationId | PROFILE_RELATION_ID | 🔑 | ✅ |
| 8 | ProfileRelationPEORelationId | RELATION_ID | — | ✅ |

### [[hrt_profile_types_b|HRT_PROFILE_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProfileTypeBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 2 | ProfileTypeBPEODateFrom | DATE_FROM | — | ✅ |
| 3 | ProfileTypeBPEODateTo | DATE_TO | — | ✅ |
| 4 | ProfileTypeBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ProfileTypeBPEOModuleId | MODULE_ID | — | ✅ |
| 6 | ProfileTypeBPEOPidApprovalFlag | PID_APPROVAL_FLAG | — | ✅ |
| 7 | ProfileTypeBPEOProfileStatusCode | PROFILE_STATUS_CODE | — | ✅ |
| 8 | ProfileTypeBPEOProfileTypeCode | PROFILE_TYPE_CODE | — | ✅ |
| 9 | ProfileTypeBPEOProfileTypeId | PROFILE_TYPE_ID | 🔑 | ✅ |
| 10 | ProfileTypeBPEOProfileUsageCode | PROFILE_USAGE_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
