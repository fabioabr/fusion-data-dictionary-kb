---
id: DOC-HCM-PVO-OrganizationRefPVO
doc_type: system-doc
title: "OrganizationRefPVO — PVO Human Capital Management"
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
  - OrganizationRefPVO
  - organizationrefpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# OrganizationRefPVO

## 📌 Visão Geral

Disponibiliza referência de organizações com classificações, status e legislação aplicável. Utilizado como dimensão de lookup para enriquecimento de dados organizacionais em relatórios.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.OrganizationAM.OrganizationRefPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 46 | 3 | 6 | 13 | 28% |

---

## 🔗 Tabelas Relacionadas

- [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]] — 18 atributos (3 PKs, 4 BICC)
- [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]] — 12 atributos (3 BICC)
- [[hr_org_unit_classifications_f|HR_ORG_UNIT_CLASSIFICATIONS_F]] — 16 atributos (3 PKs, 6 BICC)

---

## ⚙️ Atributos

### [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrganizationUnitPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 2 | OrganizationUnitPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | OrganizationUnitPEOCostAllocationKeyflexId | COST_ALLOCATION_KEYFLEX_ID | — | — |
| 4 | OrganizationUnitPEOCreatedBy | CREATED_BY | — | — |
| 5 | OrganizationUnitPEOCreationDate | CREATION_DATE | — | — |
| 6 | OrganizationUnitPEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 7 | OrganizationUnitPEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 8 | OrganizationUnitPEOEstablishmentId | ESTABLISHMENT_ID | — | — |
| 9 | OrganizationUnitPEOInternalAddressLine | INTERNAL_ADDRESS_LINE | — | — |
| 10 | OrganizationUnitPEOInternalExternalFlag | INTERNAL_EXTERNAL_FLAG | — | — |
| 11 | OrganizationUnitPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | OrganizationUnitPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | OrganizationUnitPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | OrganizationUnitPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 15 | OrganizationUnitPEOLocationId | LOCATION_ID | — | — |
| 16 | OrganizationUnitPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | OrganizationUnitPEOOrganizationId | ORGANIZATION_ID | 🔑 | ✅ |
| 18 | OrganizationUnitPEOOrganizationUnitPEOType | TYPE | — | — |

### [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrganizationUnitTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | OrganizationUnitTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | OrganizationUnitTranslationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 4 | OrganizationUnitTranslationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 5 | OrganizationUnitTranslationPEOLanguage | LANGUAGE | — | — |
| 6 | OrganizationUnitTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | OrganizationUnitTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | OrganizationUnitTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | OrganizationUnitTranslationPEOName | NAME | — | ✅ |
| 10 | OrganizationUnitTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | OrganizationUnitTranslationPEOOrganizationId | ORGANIZATION_ID | — | — |
| 12 | OrganizationUnitTranslationPEOSourceLang | SOURCE_LANG | — | — |

### [[hr_org_unit_classifications_f|HR_ORG_UNIT_CLASSIFICATIONS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 3 | OrgUnitClassificationId | ORG_UNIT_CLASSIFICATION_ID | 🔑 | ✅ |
| 4 | OrgUnitClassificationPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 5 | OrgUnitClassificationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 6 | OrgUnitClassificationPEOClassificationCode | CLASSIFICATION_CODE | — | — |
| 7 | OrgUnitClassificationPEOCreatedBy | CREATED_BY | — | — |
| 8 | OrgUnitClassificationPEOCreationDate | CREATION_DATE | — | — |
| 9 | OrgUnitClassificationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | OrgUnitClassificationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | OrgUnitClassificationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | OrgUnitClassificationPEOLegislationCode | LEGISLATION_CODE | — | — |
| 13 | OrgUnitClassificationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | OrgUnitClassificationPEOOrganizationId | ORGANIZATION_ID | — | — |
| 15 | OrgUnitClassificationPEOSetId | SET_ID | — | ✅ |
| 16 | OrgUnitClassificationPEOStatus | STATUS | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
