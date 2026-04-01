---
id: DOC-OTHER-PVO-AwardHeaderViewPVO
doc_type: system-doc
title: "AwardHeaderViewPVO — PVO Cross-Module"
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
  - AwardHeaderViewPVO
  - awardheaderviewpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AwardHeaderViewPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Award Header View. Acessa as tabelas: GMS_AWARD_HEADERS_VL, GMS_AWARD_TEMPLATES_VL, GMS_COST_SHARE_AWARDS_V (+7).

**Caminho:** `FscmTopModelAM.GmsAwardAM.AwardHeaderViewPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 80 | 10 | 1 | 39 | 49% |

---

## 🔗 Tabelas Relacionadas

- [[gms_award_headers_vl|GMS_AWARD_HEADERS_VL]] — 46 atributos (1 PKs, 31 BICC)
- [[gms_award_templates_vl|GMS_AWARD_TEMPLATES_VL]] — 2 atributos (1 BICC)
- [[gms_cost_share_awards_v|GMS_COST_SHARE_AWARDS_V]] — 1 atributos
- [[gms_organizations_all_v|GMS_ORGANIZATIONS_ALL_V]] — 2 atributos (1 BICC)
- [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]] — 7 atributos
- [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]] — 10 atributos (2 BICC)
- [[hz_parties|HZ_PARTIES]] — 2 atributos (1 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 5 atributos (1 BICC)
- [[pjf_ind_rate_sch_vl|PJF_IND_RATE_SCH_VL]] — 2 atributos (1 BICC)
- [[xle_entity_profiles|XLE_ENTITY_PROFILES]] — 3 atributos (1 BICC)

---

## ⚙️ Atributos

### [[gms_award_headers_vl|GMS_AWARD_HEADERS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardHeaderPEOAwardOwningOrgId | AWARD_OWNING_ORG_ID | — | — |
| 2 | AwardHeaderPEOAwardPurposeCode1 | AWARD_PURPOSE_CODE | — | ✅ |
| 3 | AwardHeaderPEOAwardType1 | AWARD_TYPE | — | ✅ |
| 4 | AwardHeaderPEOBusinessUnitId | BUSINESS_UNIT_ID | — | — |
| 5 | AwardHeaderPEOCloseDate | CLOSE_DATE | — | ✅ |
| 6 | AwardHeaderPEOCoiApprovalDate | COI_APPROVAL_DATE | — | ✅ |
| 7 | AwardHeaderPEOCoiInstPolicyCompliant | COI_INST_POLICY_COMPLIANT | — | ✅ |
| 8 | AwardHeaderPEOCoiReviewCompleted | COI_REVIEW_COMPLETED | — | ✅ |
| 9 | AwardHeaderPEOCostIndSchFixedDate | COST_IND_SCH_FIXED_DATE | — | ✅ |
| 10 | AwardHeaderPEOCreatedBy | CREATED_BY | — | ✅ |
| 11 | AwardHeaderPEOCreationDate | CREATION_DATE | — | ✅ |
| 12 | AwardHeaderPEODescription | DESCRIPTION | — | ✅ |
| 13 | AwardHeaderPEOExpandedAuthFlag | EXPANDED_AUTH_FLAG | — | ✅ |
| 14 | AwardHeaderPEOFtAmount | FT_AMOUNT | — | ✅ |
| 15 | AwardHeaderPEOFtFromDate | FT_FROM_DATE | — | ✅ |
| 16 | AwardHeaderPEOFtIsFederal | FT_IS_FEDERAL | — | ✅ |
| 17 | AwardHeaderPEOFtPrimarySponsor | FT_PRIMARY_SPONSOR | — | — |
| 18 | AwardHeaderPEOFtRefAwardName | FT_REF_AWARD_NAME | — | ✅ |
| 19 | AwardHeaderPEOFtToDate | FT_TO_DATE | — | ✅ |
| 20 | AwardHeaderPEOIdcScheduleId | IDC_SCHEDULE_ID | — | — |
| 21 | AwardHeaderPEOIfsApprovalDate | IFS_APPROVAL_DATE | — | ✅ |
| 22 | AwardHeaderPEOIfsApproverId | IFS_APPROVER_ID | — | — |
| 23 | AwardHeaderPEOIfsSponsorApprovalReqFlag | IFS_SPONSOR_APPROVAL_REQ_FLAG | — | ✅ |
| 24 | AwardHeaderPEOInstitutionId | INSTITUTION_ID | — | — |
| 25 | AwardHeaderPEOIntellPropDesc | INTELL_PROP_DESC | — | ✅ |
| 26 | AwardHeaderPEOIsIntellPropReported | IS_INTELL_PROP_REPORTED | — | ✅ |
| 27 | AwardHeaderPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 28 | AwardHeaderPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 29 | AwardHeaderPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 30 | AwardHeaderPEOLastValidated | LAST_VALIDATED | — | — |
| 31 | AwardHeaderPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 32 | AwardHeaderPEOPreAwardDate | PRE_AWARD_DATE | — | ✅ |
| 33 | AwardHeaderPEOPreAwardGsf | PRE_AWARD_GSF | — | ✅ |
| 34 | AwardHeaderPEOPreAwardSpendingAllowed | PRE_AWARD_SPENDING_ALLOWED | — | ✅ |
| 35 | AwardHeaderPEOPrevAwardAbr | PREV_AWARD_ABR | — | ✅ |
| 36 | AwardHeaderPEOPrevAwardBu | PREV_AWARD_BU | — | — |
| 37 | AwardHeaderPEOPrevAwardId | PREV_AWARD_ID | — | — |
| 38 | AwardHeaderPEOPrevAwardRenewalInprg | PREV_AWARD_RENEWAL_INPRG | — | ✅ |
| 39 | AwardHeaderPEOProposalId | PROPOSAL_ID | — | — |
| 40 | AwardHeaderPEOSourceAwardId | SOURCE_AWARD_ID | — | — |
| 41 | AwardHeaderPEOSourceTemplateId | SOURCE_TEMPLATE_ID | — | — |
| 42 | AwardHeaderPEOSponsorAwardNumber | SPONSOR_AWARD_NUMBER | — | ✅ |
| 43 | AwardHeaderPEOSponsorId | SPONSOR_ID | — | — |
| 44 | AwardHeaderPEOTemplateFlag | TEMPLATE_FLAG | — | ✅ |
| 45 | AwardHeaderPEOValidateStatus | VALIDATE_STATUS | — | ✅ |
| 46 | Id | ID | 🔑 | ✅ |

### [[gms_award_templates_vl|GMS_AWARD_TEMPLATES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardTemplatesPEOTemplateId | TEMPLATE_ID | — | — |
| 2 | AwardTemplatesPEOTemplateName | TEMPLATE_NAME | — | ✅ |

### [[gms_cost_share_awards_v|GMS_COST_SHARE_AWARDS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GmsCostShareAwardPEOAwardId | AWARD_ID | — | — |

### [[gms_organizations_all_v|GMS_ORGANIZATIONS_ALL_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardOwningOrganizationPEOName | NAME | — | ✅ |
| 2 | AwardOwningOrganizationPEOOrganizationId | ORGANIZATION_ID | — | — |

### [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitPEOBusinessUnitId | ORGANIZATION_ID | — | — |
| 2 | BusinessUnitPEODefaultCurrencyCode | ORG_INFORMATION8 | — | — |
| 3 | BusinessUnitPEOLegalEntityId | ORG_INFORMATION2 | — | — |
| 4 | OrganizationInformationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 5 | OrganizationInformationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 6 | OrganizationInformationPEOOrgInformationId | ORG_INFORMATION_ID | — | — |
| 7 | OrganizationInformationPEOOrganizationId | ORGANIZATION_ID | — | — |

### [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitPEOName | NAME | — | ✅ |
| 2 | OrganizationUnitTranslationPEOEffectiveEndDate2 | EFFECTIVE_END_DATE | — | — |
| 3 | OrganizationUnitTranslationPEOEffectiveStartDate2 | EFFECTIVE_START_DATE | — | — |
| 4 | OrganizationUnitTranslationPEOLanguage1 | LANGUAGE | — | — |
| 5 | OrganizationUnitTranslationPEffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 6 | OrganizationUnitTranslationPEffectiveStartDate1 | EFFECTIVE_START_DATE | — | — |
| 7 | OrganizationUnitTranslationPLanguage | LANGUAGE | — | — |
| 8 | OrganizationUnitTranslationPOrganizationId1 | ORGANIZATION_ID | — | — |
| 9 | PrevAwardBusinessUnitId | ORGANIZATION_ID | — | — |
| 10 | PrevAwardBusinessUnitName | NAME | — | ✅ |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyPEOPartyId | PARTY_ID | — | — |
| 2 | PartyPEOPartyName | PARTY_NAME | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonNameDPEODisplayName | DISPLAY_NAME | — | — |
| 2 | PersonNameDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonNameDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | PersonNameDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 5 | PersonNameDPEOPersonNameId | PERSON_NAME_ID | — | — |

### [[pjf_ind_rate_sch_vl|PJF_IND_RATE_SCH_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BurdenSchedulePEOIndRateSchId | IND_RATE_SCH_ID | — | — |
| 2 | BurdenSchedulePEOIndSchName | IND_SCH_NAME | — | ✅ |

### [[xle_entity_profiles|XLE_ENTITY_PROFILES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | XleEntityProfilesLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 2 | XleEntityProfilesName | NAME | — | ✅ |
| 3 | XleEntityProfilesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
