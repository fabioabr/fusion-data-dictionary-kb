---
id: DOC-OTHER-PVO-ProfileTypeSectionPVO
doc_type: system-doc
title: "ProfileTypeSectionPVO — PVO Cross-Module"
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
  - ProfileTypeSectionPVO
  - profiletypesectionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProfileTypeSectionPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Profile Type Section. Acessa as tabelas: HRT_PROFILE_TYPES_TL, HRT_PROFILE_TYP_SECTIONS_TL, HRT_PROFILE_TYP_SECTIONS_VL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmProfileSetupAM.ProfileTypeSectionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 27 | 3 | 2 | 4 | 15% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_profile_types_tl|HRT_PROFILE_TYPES_TL]] — 4 atributos
- [[hrt_profile_typ_sections_tl|HRT_PROFILE_TYP_SECTIONS_TL]] — 3 atributos
- [[hrt_profile_typ_sections_vl|HRT_PROFILE_TYP_SECTIONS_VL]] — 20 atributos (2 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[hrt_profile_types_tl|HRT_PROFILE_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId2 | BUSINESS_GROUP_ID | — | — |
| 2 | Language1 | LANGUAGE | — | — |
| 3 | ProfileTypeId1 | PROFILE_TYPE_ID | — | — |
| 4 | ProfileTypeName | DESCRIPTION | — | — |

### [[hrt_profile_typ_sections_tl|HRT_PROFILE_TYP_SECTIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 2 | Language | LANGUAGE | — | — |
| 3 | SectionId1 | SECTION_ID | — | — |

### [[hrt_profile_typ_sections_vl|HRT_PROFILE_TYP_SECTIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApprovalRequiredFlag | APPROVAL_REQUIRED_FLAG | — | — |
| 2 | BusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 3 | ContentTypeId | CONTENT_TYPE_ID | — | — |
| 4 | ContentTypeRelationId | CONTENT_TYPE_RELATION_ID | — | — |
| 5 | CreatedBy | CREATED_BY | — | — |
| 6 | CreationDate | CREATION_DATE | — | — |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ModuleId | MODULE_ID | — | — |
| 11 | Name | NAME | — | ✅ |
| 12 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | ParentSectionId | PARENT_SECTION_ID | — | — |
| 14 | ProfileTypeId | PROFILE_TYPE_ID | — | — |
| 15 | QualifierSetId1 | QUALIFIER_SET_ID1 | — | — |
| 16 | QualifierSetId2 | QUALIFIER_SET_ID2 | — | — |
| 17 | SectionContext | SECTION_CONTEXT | — | — |
| 18 | SectionDescription | DESCRIPTION | — | — |
| 19 | SectionId | SECTION_ID | 🔑 | ✅ |
| 20 | SectionItemReqdFlag | SECTION_ITEM_REQD_FLAG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
