---
id: DOC-HCM-PVO-ProfileTypeSectionPropertyPVO
doc_type: system-doc
title: "ProfileTypeSectionPropertyPVO — PVO Human Capital Management"
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
  - ProfileTypeSectionPropertyPVO
  - profiletypesectionpropertypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProfileTypeSectionPropertyPVO

## 📌 Visão Geral

Disponibiliza propriedades de seções de tipos de perfil com traduções. Controla a configuração granular de campos e comportamentos por seção de perfil.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmProfileSetupAM.ProfileTypeSectionPropertyPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 30 | 2 | 2 | 4 | 13% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_profile_tp_sc_prp_b|HRT_PROFILE_TP_SC_PRP_B]] — 19 atributos (2 PKs, 3 BICC)
- [[hrt_profile_tp_sc_prp_tl|HRT_PROFILE_TP_SC_PRP_TL]] — 11 atributos (1 BICC)

---

## ⚙️ Atributos

### [[hrt_profile_tp_sc_prp_b|HRT_PROFILE_TP_SC_PRP_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProfileTypeSectionPropertyBPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | ProfileTypeSectionPropertyBPEOColumnName | COLUMN_NAME | — | — |
| 3 | ProfileTypeSectionPropertyBPEOCreatedBy | CREATED_BY | — | — |
| 4 | ProfileTypeSectionPropertyBPEOCreationDate | CREATION_DATE | — | — |
| 5 | ProfileTypeSectionPropertyBPEODefaultValue | DEFAULT_VALUE | — | — |
| 6 | ProfileTypeSectionPropertyBPEODisplayFlag | DISPLAY_FLAG | — | — |
| 7 | ProfileTypeSectionPropertyBPEOFieldName | FIELD_NAME | — | — |
| 8 | ProfileTypeSectionPropertyBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | ProfileTypeSectionPropertyBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | ProfileTypeSectionPropertyBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | ProfileTypeSectionPropertyBPEOModuleId | MODULE_ID | — | — |
| 12 | ProfileTypeSectionPropertyBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | ProfileTypeSectionPropertyBPEOPropertySource | PROPERTY_SOURCE | — | — |
| 14 | ProfileTypeSectionPropertyBPEORequiredFlag | REQUIRED_FLAG | — | — |
| 15 | ProfileTypeSectionPropertyBPEOSearchFlag | SEARCH_FLAG | — | — |
| 16 | ProfileTypeSectionPropertyBPEOSectionId | SECTION_ID | — | — |
| 17 | ProfileTypeSectionPropertyBPEOSectionPropId | SECTION_PROP_ID | 🔑 | ✅ |
| 18 | ProfileTypeSectionPropertyBPEOValueSetName | VALUE_SET_NAME | — | — |
| 19 | ProfileTypeSectionPropertyBPEOViewAttrbName | VIEW_ATTRB_NAME | — | — |

### [[hrt_profile_tp_sc_prp_tl|HRT_PROFILE_TP_SC_PRP_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProfileTypeSectionPropertyTrPEOAttributeLabel | ATTRIBUTE_LABEL | — | — |
| 2 | ProfileTypeSectionPropertyTrPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | ProfileTypeSectionPropertyTrPEOCreatedBy | CREATED_BY | — | — |
| 4 | ProfileTypeSectionPropertyTrPEOCreationDate | CREATION_DATE | — | — |
| 5 | ProfileTypeSectionPropertyTrPEOLanguage | LANGUAGE | — | — |
| 6 | ProfileTypeSectionPropertyTrPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ProfileTypeSectionPropertyTrPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | ProfileTypeSectionPropertyTrPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ProfileTypeSectionPropertyTrPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | ProfileTypeSectionPropertyTrPEOSectionPropId | SECTION_PROP_ID | — | — |
| 11 | SourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
