---
id: DOC-OTHER-PVO-AwardFundingSourcePVO
doc_type: system-doc
title: "AwardFundingSourcePVO — PVO Cross-Module"
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
  - AwardFundingSourcePVO
  - awardfundingsourcepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AwardFundingSourcePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Award Funding Source. Acessa as tabelas: GMS_AWARD_FUNDING_SOURCES_B, GMS_FUNDING_SOURCES_B, GMS_FUNDING_SOURCES_TL (+5).

**Caminho:** `FscmTopModelAM.GmsAwardAM.AwardFundingSourcePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 40 | 8 | 4 | 23 | 57% |

---

## 🔗 Tabelas Relacionadas

- [[gms_award_funding_sources_b|GMS_AWARD_FUNDING_SOURCES_B]] — 12 atributos (1 PKs, 12 BICC)
- [[gms_funding_sources_b|GMS_FUNDING_SOURCES_B]] — 4 atributos (2 BICC)
- [[gms_funding_sources_tl|GMS_FUNDING_SOURCES_TL]] — 4 atributos (1 BICC)
- [[gms_lookups|GMS_LOOKUPS]] — 3 atributos (1 BICC)
- [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]] — 5 atributos (1 BICC)
- [[hr_org_unit_classifications_f|HR_ORG_UNIT_CLASSIFICATIONS_F]] — 4 atributos (1 BICC)
- [[hz_parties|HZ_PARTIES]] — 3 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 5 atributos (3 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[gms_award_funding_sources_b|GMS_AWARD_FUNDING_SOURCES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardFundingSourcePEOApprovalDate | APPROVAL_DATE | — | ✅ |
| 2 | AwardFundingSourcePEOApprovalPersonId | APPROVAL_PERSON_ID | — | ✅ |
| 3 | AwardFundingSourcePEOAwardId | AWARD_ID | — | ✅ |
| 4 | AwardFundingSourcePEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | AwardFundingSourcePEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | AwardFundingSourcePEOFundingSourceId | FUNDING_SOURCE_ID | — | ✅ |
| 7 | AwardFundingSourcePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | AwardFundingSourcePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | AwardFundingSourcePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | AwardFundingSourcePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | AwardFundingSourcePEORequiredBySponsor | REQUIRED_BY_SPONSOR | — | ✅ |
| 12 | Id | ID | 🔑 | ✅ |

### [[gms_funding_sources_b|GMS_FUNDING_SOURCES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FundingSourceAllPEOFundingSourceId | FUNDING_SOURCE_ID | — | ✅ |
| 2 | FundingSourceAllPEOFundingSourceNumber | FUNDING_SOURCE_NUMBER | — | ✅ |
| 3 | FundingSourceBasePEOEndDateActive | END_DATE_ACTIVE | — | — |
| 4 | FundingSourceBasePEOStartDateActive | START_DATE_ACTIVE | — | — |

### [[gms_funding_sources_tl|GMS_FUNDING_SOURCES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FundingSourceTranslationPEODescription | DESCRIPTION | — | ✅ |
| 2 | FundingSourceTranslationPEOFundingSourceId | FUNDING_SOURCE_ID | — | — |
| 3 | FundingSourceTranslationPEOFundingSourceName | FUNDING_SOURCE_NAME | — | — |
| 4 | FundingSourceTranslationPEOLanguage | LANGUAGE | — | — |

### [[gms_lookups|GMS_LOOKUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FSLookupPEOLookupCode | LOOKUP_CODE | — | — |
| 2 | FSLookupPEOLookupType | LOOKUP_TYPE | — | — |
| 3 | FundingSourceAllPEOFundingSourceType | MEANING | — | ✅ |

### [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrgUnitTranslationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | OrgUnitTranslationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | OrgUnitTranslationPEOLanguage | LANGUAGE | — | — |
| 4 | OrgUnitTranslationPEOOrganizationId | ORGANIZATION_ID | — | — |
| 5 | OrganizationUnitTranslationPEOName | NAME | — | — |

### [[hr_org_unit_classifications_f|HR_ORG_UNIT_CLASSIFICATIONS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrgUnitClassificationPEOClassificationId | ORG_UNIT_CLASSIFICATION_ID | — | — |
| 2 | OrgUnitClassificationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | OrgUnitClassificationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | OrgUnitClassificationPEOStatus | STATUS | — | — |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyId | PARTY_ID | — | — |
| 2 | PartyPEOPartyName | PARTY_NAME | — | — |
| 3 | PartyPEOStatus | STATUS | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonNameDPEODisplayName | DISPLAY_NAME | — | ✅ |
| 2 | PersonNameDPEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 3 | PersonNameDPEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 4 | PersonNameDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 5 | PersonNameDPEOPersonNameId | PERSON_NAME_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
