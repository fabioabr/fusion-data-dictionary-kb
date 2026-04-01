---
id: DOC-OTHER-PVO-FundingSourcePVO
doc_type: system-doc
title: "FundingSourcePVO — PVO Cross-Module"
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
  - FundingSourcePVO
  - fundingsourcepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FundingSourcePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Funding Source. Acessa as tabelas: GMS_FUNDING_SOURCES_B, GMS_FUNDING_SOURCES_TL, GMS_LOOKUPS (+3).

**Caminho:** `FscmTopModelAM.GmsSetupAM.FundingSourcePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 31 | 6 | 1 | 7 | 23% |

---

## 🔗 Tabelas Relacionadas

- [[gms_funding_sources_b|GMS_FUNDING_SOURCES_B]] — 12 atributos (1 PKs, 3 BICC)
- [[gms_funding_sources_tl|GMS_FUNDING_SOURCES_TL]] — 4 atributos (1 BICC)
- [[gms_lookups|GMS_LOOKUPS]] — 3 atributos (1 BICC)
- [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]] — 5 atributos (1 BICC)
- [[hr_org_unit_classifications_f|HR_ORG_UNIT_CLASSIFICATIONS_F]] — 4 atributos (1 BICC)
- [[hz_parties|HZ_PARTIES]] — 3 atributos

---

## ⚙️ Atributos

### [[gms_funding_sources_b|GMS_FUNDING_SOURCES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FundingSourceAllPEOCreatedBy | CREATED_BY | — | — |
| 2 | FundingSourceAllPEOCreationDate | CREATION_DATE | — | — |
| 3 | FundingSourceAllPEOFundingSourceNumber | FUNDING_SOURCE_NUMBER | — | ✅ |
| 4 | FundingSourceAllPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | FundingSourceAllPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | FundingSourceAllPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | FundingSourceAllPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | FundingSourceAllPEOSourceId | SOURCE_ID | — | — |
| 9 | FundingSourceAllPEOType | TYPE | — | — |
| 10 | FundingSourceBasePEOEndDateActive | END_DATE_ACTIVE | — | — |
| 11 | FundingSourceBasePEOStartDateActive | START_DATE_ACTIVE | — | — |
| 12 | FundingSourceId | FUNDING_SOURCE_ID | 🔑 | ✅ |

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
| 1 | FundingSourceAllPEOFundingSourceType | MEANING | — | ✅ |
| 2 | GmsLookupPEOLookupCode | LOOKUP_CODE | — | — |
| 3 | GmsLookupPEOLookupType | LOOKUP_TYPE | — | — |

### [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FundingSourceAllPEOOrganizationId | ORGANIZATION_ID | — | — |
| 2 | OrgEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | OrgEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | OrganizationPEOName | NAME | — | — |
| 5 | OrganizationUnitTranslationPEOLanguage | LANGUAGE | — | — |

### [[hr_org_unit_classifications_f|HR_ORG_UNIT_CLASSIFICATIONS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FundingSourceAllPEOOrgStatus | STATUS | — | — |
| 2 | OrgUnitClassificationId | ORG_UNIT_CLASSIFICATION_ID | — | — |
| 3 | OrgUnitClassificationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 4 | OrgUnitClassificationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FundingSourceAllPEOPartyId | PARTY_ID | — | — |
| 2 | FundingSourceAllPEOSponsorStatus | STATUS | — | — |
| 3 | PartyName | PARTY_NAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
