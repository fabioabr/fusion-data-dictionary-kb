---
id: DOC-HCM-PVO-ContactPersonDisabilityPVO
doc_type: system-doc
title: "ContactPersonDisabilityPVO — PVO Human Capital Management"
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
  - ContactPersonDisabilityPVO
  - contactpersondisabilitypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ContactPersonDisabilityPVO

## 📌 Visão Geral

Registra deficiencias de contatos/dependentes com organizacao e vigencia. Suporta compliance de acessibilidade e gestao de beneficios especiais.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.PersonAM.ContactPersonDisabilityPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 46 | 5 | 3 | 33 | 72% |

---

## 🔗 Tabelas Relacionadas

- [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]] — 3 atributos (1 BICC)
- [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]] — 5 atributos (3 BICC)
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 3 atributos (1 BICC)
- [[per_contact_relships_f|PER_CONTACT_RELSHIPS_F]] — 4 atributos (1 BICC)
- [[per_disabilities_f|PER_DISABILITIES_F]] — 31 atributos (3 PKs, 27 BICC)

---

## ⚙️ Atributos

### [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrganizationUnitPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | OrganizationUnitPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | OrganizationUnitPEOOrganizationId | ORGANIZATION_ID | — | — |

### [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrganizationUnitTranslationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | OrganizationUnitTranslationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | OrganizationUnitTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 4 | OrganizationUnitTranslationPEOName | NAME | — | ✅ |
| 5 | OrganizationUnitTranslationPEOOrganizationId | ORGANIZATION_ID | — | — |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContactPersonDetailsPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | ContactPersonDetailsPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | ContactPersonDetailsPEOPersonId | PERSON_ID | — | — |

### [[per_contact_relships_f|PER_CONTACT_RELSHIPS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContactRelshipsPEOContactRelationshipId | CONTACT_RELATIONSHIP_ID | — | — |
| 2 | ContactRelshipsPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | ContactRelshipsPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | ContactRelshipsPEOPersonId | PERSON_ID | — | — |

### [[per_disabilities_f|PER_DISABILITIES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DisabilityId | DISABILITY_ID | 🔑 | ✅ |
| 2 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 3 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 4 | PersonDisabilityPEOAccommodationRequest | ACCOMMODATION_REQUEST | — | — |
| 5 | PersonDisabilityPEOAssessmentDueDate | ASSESSMENT_DUE_DATE | — | ✅ |
| 6 | PersonDisabilityPEOAssignmentId | ASSIGNMENT_ID | — | ✅ |
| 7 | PersonDisabilityPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 8 | PersonDisabilityPEOCategory | CATEGORY | — | ✅ |
| 9 | PersonDisabilityPEOCreatedBy | CREATED_BY | — | ✅ |
| 10 | PersonDisabilityPEOCreationDate | CREATION_DATE | — | ✅ |
| 11 | PersonDisabilityPEODegree | DEGREE | — | ✅ |
| 12 | PersonDisabilityPEODescription | DESCRIPTION | — | ✅ |
| 13 | PersonDisabilityPEODisabilityCode | DISABILITY_CODE | — | ✅ |
| 14 | PersonDisabilityPEODisclosureDate | DISCLOSURE_DATE | — | — |
| 15 | PersonDisabilityPEOIncidentId | INCIDENT_ID | — | ✅ |
| 16 | PersonDisabilityPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | PersonDisabilityPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 18 | PersonDisabilityPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 19 | PersonDisabilityPEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 20 | PersonDisabilityPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 21 | PersonDisabilityPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 22 | PersonDisabilityPEOPersonId | PERSON_ID | — | ✅ |
| 23 | PersonDisabilityPEOPreRegistrationJob | PRE_REGISTRATION_JOB | — | ✅ |
| 24 | PersonDisabilityPEOQuotaFte | QUOTA_FTE | — | ✅ |
| 25 | PersonDisabilityPEOReason | REASON | — | ✅ |
| 26 | PersonDisabilityPEORegistrationDate | REGISTRATION_DATE | — | ✅ |
| 27 | PersonDisabilityPEORegistrationExpDate | REGISTRATION_EXP_DATE | — | ✅ |
| 28 | PersonDisabilityPEORegistrationId | REGISTRATION_ID | — | ✅ |
| 29 | PersonDisabilityPEOSelfDisclosedType | SELF_DISCLOSED_TYPE | — | — |
| 30 | PersonDisabilityPEOStatus | STATUS | — | ✅ |
| 31 | PersonDisabilityPEOWorkRestriction | WORK_RESTRICTION | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
