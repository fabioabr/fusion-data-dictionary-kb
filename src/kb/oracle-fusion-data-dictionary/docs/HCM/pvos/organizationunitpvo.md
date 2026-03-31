---
id: DOC-HCM-PVO-OrganizationUnitPVO
doc_type: system-doc
title: "OrganizationUnitPVO — PVO Human Capital Management"
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
  - OrganizationUnitPVO
  - organizationunitpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# OrganizationUnitPVO

## 📌 Visão Geral

Extrai unidades organizacionais com informações complementares e traduções por vigência temporal. Base para construção da hierarquia departamental e análise de estrutura organizacional.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.OrganizationAM.OrganizationUnitPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 39 | 3 | 1 | 12 | 31% |

---

## 🔗 Tabelas Relacionadas

- [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]] — 18 atributos (1 PKs, 11 BICC)
- [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]] — 8 atributos
- [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]] — 13 atributos (1 BICC)

---

## ⚙️ Atributos

### [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | OrganizationId | ORGANIZATION_ID | 🔑 | ✅ |
| 4 | OrganizationUnitPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 5 | OrganizationUnitPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 6 | OrganizationUnitPEOCostAllocationKeyflexId | COST_ALLOCATION_KEYFLEX_ID | — | — |
| 7 | OrganizationUnitPEOCreatedBy | CREATED_BY | — | ✅ |
| 8 | OrganizationUnitPEOCreationDate | CREATION_DATE | — | ✅ |
| 9 | OrganizationUnitPEOEstablishmentId | ESTABLISHMENT_ID | — | — |
| 10 | OrganizationUnitPEOInternalAddressLine | INTERNAL_ADDRESS_LINE | — | ✅ |
| 11 | OrganizationUnitPEOInternalExternalFlag | INTERNAL_EXTERNAL_FLAG | — | — |
| 12 | OrganizationUnitPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | OrganizationUnitPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | OrganizationUnitPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | OrganizationUnitPEOLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 16 | OrganizationUnitPEOLocationId | LOCATION_ID | — | ✅ |
| 17 | OrganizationUnitPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | OrganizationUnitPEOOrganizationUnitPEOType | TYPE | — | ✅ |

### [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrgInfoBUPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | OrgInfoBUPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | OrgInfoBUPEOOrgInformation1 | ORG_INFORMATION1 | — | — |
| 4 | OrgInfoBUPEOOrgInformationId | ORG_INFORMATION_ID | — | — |
| 5 | OrgInfoOrgManagerPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 6 | OrgInfoOrgManagerPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 7 | OrgInfoOrgManagerPEOOrgInformation2 | ORG_INFORMATION2 | — | — |
| 8 | OrgInfoOrgManagerPEOOrgInformationId | ORG_INFORMATION_ID | — | — |

### [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrganizationUnitTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | OrganizationUnitTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | OrganizationUnitTranslationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 4 | OrganizationUnitTranslationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 5 | OrganizationUnitTranslationPEOLanguage | LANGUAGE | — | — |
| 6 | OrganizationUnitTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | OrganizationUnitTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | OrganizationUnitTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | OrganizationUnitTranslationPEOName | NAME | — | ✅ |
| 10 | OrganizationUnitTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | OrganizationUnitTranslationPEOOrganizationId | ORGANIZATION_ID | — | — |
| 12 | OrganizationUnitTranslationPEOSourceLang | SOURCE_LANG | — | — |
| 13 | OrganizationUnitTranslationPEOTitle | TITLE | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
