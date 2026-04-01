---
id: DOC-OTHER-PVO-AwardHeaderPVO
doc_type: system-doc
title: "AwardHeaderPVO — PVO Cross-Module"
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
  - AwardHeaderPVO
  - awardheaderpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AwardHeaderPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Award Header. Acessa as tabelas: GMS_AWARD_HEADERS_B, GMS_AWARD_HEADERS_TL, GMS_AWARD_TEMPLATES_VL (+8).

**Caminho:** `FscmTopModelAM.GmsAwardAM.AwardHeaderPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 92 | 11 | 1 | 81 | 88% |

---

## 🔗 Tabelas Relacionadas

- [[gms_award_headers_b|GMS_AWARD_HEADERS_B]] — 44 atributos (1 PKs, 44 BICC)
- [[gms_award_headers_tl|GMS_AWARD_HEADERS_TL]] — 13 atributos (13 BICC)
- [[gms_award_templates_vl|GMS_AWARD_TEMPLATES_VL]] — 3 atributos (3 BICC)
- [[gms_cost_share_awards_v|GMS_COST_SHARE_AWARDS_V]] — 1 atributos (1 BICC)
- [[gms_organizations_all_v|GMS_ORGANIZATIONS_ALL_V]] — 2 atributos (2 BICC)
- [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]] — 7 atributos (3 BICC)
- [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]] — 10 atributos (3 BICC)
- [[hz_parties|HZ_PARTIES]] — 2 atributos (2 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 5 atributos (5 BICC)
- [[pjf_ind_rate_sch_vl|PJF_IND_RATE_SCH_VL]] — 2 atributos (2 BICC)
- [[xle_entity_profiles|XLE_ENTITY_PROFILES]] — 3 atributos (3 BICC)

---

## ⚙️ Atributos

### [[gms_award_headers_b|GMS_AWARD_HEADERS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardHeaderBasePEOAwardOwningOrgId | AWARD_OWNING_ORG_ID | — | ✅ |
| 2 | AwardHeaderBasePEOAwardPurposeCode1 | AWARD_PURPOSE_CODE | — | ✅ |
| 3 | AwardHeaderBasePEOAwardType1 | AWARD_TYPE | — | ✅ |
| 4 | AwardHeaderBasePEOBusinessUnitId | BUSINESS_UNIT_ID | — | ✅ |
| 5 | AwardHeaderBasePEOCfdaNumber | CFDA_NUMBER | — | ✅ |
| 6 | AwardHeaderBasePEOCloseDate | CLOSE_DATE | — | ✅ |
| 7 | AwardHeaderBasePEOCoiApprovalDate | COI_APPROVAL_DATE | — | ✅ |
| 8 | AwardHeaderBasePEOCoiInstPolicyCompliant | COI_INST_POLICY_COMPLIANT | — | ✅ |
| 9 | AwardHeaderBasePEOCoiReviewCompleted | COI_REVIEW_COMPLETED | — | ✅ |
| 10 | AwardHeaderBasePEOCostIndSchFixedDate | COST_IND_SCH_FIXED_DATE | — | ✅ |
| 11 | AwardHeaderBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 12 | AwardHeaderBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 13 | AwardHeaderBasePEOExpandedAuthFlag | EXPANDED_AUTH_FLAG | — | ✅ |
| 14 | AwardHeaderBasePEOFtAmount | FT_AMOUNT | — | ✅ |
| 15 | AwardHeaderBasePEOFtFromDate | FT_FROM_DATE | — | ✅ |
| 16 | AwardHeaderBasePEOFtIsFederal | FT_IS_FEDERAL | — | ✅ |
| 17 | AwardHeaderBasePEOFtPrimarySponsor | FT_PRIMARY_SPONSOR | — | ✅ |
| 18 | AwardHeaderBasePEOFtToDate | FT_TO_DATE | — | ✅ |
| 19 | AwardHeaderBasePEOIdcScheduleId | IDC_SCHEDULE_ID | — | ✅ |
| 20 | AwardHeaderBasePEOIfsApprovalDate | IFS_APPROVAL_DATE | — | ✅ |
| 21 | AwardHeaderBasePEOIfsApproverId | IFS_APPROVER_ID | — | ✅ |
| 22 | AwardHeaderBasePEOIfsSponsorApprovalReqFlag | IFS_SPONSOR_APPROVAL_REQ_FLAG | — | ✅ |
| 23 | AwardHeaderBasePEOInstitutionId | INSTITUTION_ID | — | ✅ |
| 24 | AwardHeaderBasePEOIsIntellPropReported | IS_INTELL_PROP_REPORTED | — | ✅ |
| 25 | AwardHeaderBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 26 | AwardHeaderBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 27 | AwardHeaderBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 28 | AwardHeaderBasePEOLastValidated | LAST_VALIDATED | — | ✅ |
| 29 | AwardHeaderBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 30 | AwardHeaderBasePEOPreAwardDate | PRE_AWARD_DATE | — | ✅ |
| 31 | AwardHeaderBasePEOPreAwardSpendingAllowed | PRE_AWARD_SPENDING_ALLOWED | — | ✅ |
| 32 | AwardHeaderBasePEOPrevAwardAbr | PREV_AWARD_ABR | — | ✅ |
| 33 | AwardHeaderBasePEOPrevAwardBu | PREV_AWARD_BU | — | ✅ |
| 34 | AwardHeaderBasePEOPrevAwardId | PREV_AWARD_ID | — | ✅ |
| 35 | AwardHeaderBasePEOPrevAwardRenewalInprg | PREV_AWARD_RENEWAL_INPRG | — | ✅ |
| 36 | AwardHeaderBasePEOPrincipalInvestigatorId | PRINCIPAL_INVESTIGATOR_ID | — | ✅ |
| 37 | AwardHeaderBasePEOProposalId | PROPOSAL_ID | — | ✅ |
| 38 | AwardHeaderBasePEOSourceAwardId | SOURCE_AWARD_ID | — | ✅ |
| 39 | AwardHeaderBasePEOSourceTemplateId | SOURCE_TEMPLATE_ID | — | ✅ |
| 40 | AwardHeaderBasePEOSponsorAwardNumber | SPONSOR_AWARD_NUMBER | — | ✅ |
| 41 | AwardHeaderBasePEOSponsorId | SPONSOR_ID | — | ✅ |
| 42 | AwardHeaderBasePEOTemplateFlag | TEMPLATE_FLAG | — | ✅ |
| 43 | AwardHeaderBasePEOValidateStatus | VALIDATE_STATUS | — | ✅ |
| 44 | Id | ID | 🔑 | ✅ |

### [[gms_award_headers_tl|GMS_AWARD_HEADERS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardHeaderTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | AwardHeaderTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | AwardHeaderTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | AwardHeaderTranslationPEOFtRefAwardName | FT_REF_AWARD_NAME | — | ✅ |
| 5 | AwardHeaderTranslationPEOId1 | ID | — | ✅ |
| 6 | AwardHeaderTranslationPEOIntellPropDesc | INTELL_PROP_DESC | — | ✅ |
| 7 | AwardHeaderTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 8 | AwardHeaderTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | AwardHeaderTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | AwardHeaderTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | AwardHeaderTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | AwardHeaderTranslationPEOPreAwardGsf | PRE_AWARD_GSF | — | ✅ |
| 13 | AwardHeaderTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

### [[gms_award_templates_vl|GMS_AWARD_TEMPLATES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardTemplatesPEOTemplateId | TEMPLATE_ID | — | ✅ |
| 2 | AwardTemplatesPEOTemplateName | TEMPLATE_NAME | — | ✅ |
| 3 | AwardTemplatesPEOTemplateSource | TEMPLATE_SOURCE | — | ✅ |

### [[gms_cost_share_awards_v|GMS_COST_SHARE_AWARDS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GmsCostShareAwardPEOAwardId | AWARD_ID | — | ✅ |

### [[gms_organizations_all_v|GMS_ORGANIZATIONS_ALL_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardOwningOrganizationPEOName | NAME | — | ✅ |
| 2 | AwardOwningOrganizationPEOOrganizationId | ORGANIZATION_ID | — | ✅ |

### [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitPEOBusinessUnitId | ORGANIZATION_ID | — | ✅ |
| 2 | BusinessUnitPEODefaultCurrencyCode | ORG_INFORMATION_NUMBER8 | — | ✅ |
| 3 | BusinessUnitPEOLegalEntityId | ORG_INFORMATION2 | — | ✅ |
| 4 | OrganizationInformationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 5 | OrganizationInformationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 6 | OrganizationInformationPEOOrgInformationId | ORG_INFORMATION_ID | — | — |
| 7 | OrganizationInformationPEOOrganizationId | ORGANIZATION_ID | — | — |

### [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitPEOName | NAME | — | ✅ |
| 2 | OrganizationUnitTranslationP1EffectiveEndDate2 | EFFECTIVE_END_DATE | — | — |
| 3 | OrganizationUnitTranslationP1EffectiveStartDate2 | EFFECTIVE_START_DATE | — | — |
| 4 | OrganizationUnitTranslationP1Language1 | LANGUAGE | — | — |
| 5 | OrganizationUnitTranslationPEffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 6 | OrganizationUnitTranslationPEffectiveStartDate1 | EFFECTIVE_START_DATE | — | — |
| 7 | OrganizationUnitTranslationPLanguage | LANGUAGE | — | — |
| 8 | OrganizationUnitTranslationPOrganizationId1 | ORGANIZATION_ID | — | — |
| 9 | PrevAwardBusinessUnitId | ORGANIZATION_ID | — | ✅ |
| 10 | PrevAwardBusinessUnitName | NAME | — | ✅ |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyPEOPartyId | PARTY_ID | — | ✅ |
| 2 | PartyPEOPartyName | PARTY_NAME | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonNameDPEODisplayName | DISPLAY_NAME | — | ✅ |
| 2 | PersonNameDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 3 | PersonNameDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | PersonNameDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 5 | PersonNameDPEOPersonNameId | PERSON_NAME_ID | — | ✅ |

### [[pjf_ind_rate_sch_vl|PJF_IND_RATE_SCH_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BurdenSchedulePEOIndRateSchId | IND_RATE_SCH_ID | — | ✅ |
| 2 | BurdenSchedulePEOIndSchName | IND_SCH_NAME | — | ✅ |

### [[xle_entity_profiles|XLE_ENTITY_PROFILES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | XleEntityProfilesLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 2 | XleEntityProfilesName | NAME | — | ✅ |
| 3 | XleEntityProfilesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
