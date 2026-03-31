---
id: DOC-OTHER-PVO-GrantsBusinessUnitPVO
doc_type: system-doc
title: "GrantsBusinessUnitPVO — PVO Cross-Module"
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
  - GrantsBusinessUnitPVO
  - grantsbusinessunitpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GrantsBusinessUnitPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Grants Business Unit. Acessa as tabelas: FND_SETID_SETS_VL, GL_LEDGERS, GMS_BUSINESS_UNITS (+16).

**Caminho:** `FscmTopModelAM.GmsSetupAM.GrantsBusinessUnitPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 103 | 19 | 1 | 27 | 26% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_setid_sets_vl|FND_SETID_SETS_VL]] — 3 atributos (1 BICC)
- [[gl_ledgers|GL_LEDGERS]] — 3 atributos (1 BICC)
- [[gms_business_units|GMS_BUSINESS_UNITS]] — 21 atributos (1 PKs, 5 BICC)
- [[gms_institutions_b|GMS_INSTITUTIONS_B]] — 1 atributos
- [[gms_institutions_tl|GMS_INSTITUTIONS_TL]] — 3 atributos (1 BICC)
- [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]] — 7 atributos (2 BICC)
- [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]] — 9 atributos (1 BICC)
- [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]] — 10 atributos (2 BICC)
- [[hr_org_unit_classifications_f|HR_ORG_UNIT_CLASSIFICATIONS_F]] — 4 atributos (1 BICC)
- [[okc_contract_types_b|OKC_CONTRACT_TYPES_B]] — 2 atributos
- [[okc_contract_types_tl|OKC_CONTRACT_TYPES_TL]] — 4 atributos (1 BICC)
- [[per_location_details_f|PER_LOCATION_DETAILS_F]] — 4 atributos (1 BICC)
- [[per_location_details_f_tl|PER_LOCATION_DETAILS_F_TL]] — 5 atributos (1 BICC)
- [[per_person_names_f|PER_PERSON_NAMES_F]] — 5 atributos (2 BICC)
- [[pjb_billing_methods_tl|PJB_BILLING_METHODS_TL]] — 6 atributos (2 BICC)
- [[pjb_invoice_formats|PJB_INVOICE_FORMATS]] — 6 atributos (3 BICC)
- [[pjf_billing_cycles_tl|PJF_BILLING_CYCLES_TL]] — 4 atributos (1 BICC)
- [[pjf_ind_rate_sch_tl|PJF_IND_RATE_SCH_TL]] — 3 atributos (1 BICC)
- [[xle_entity_profiles|XLE_ENTITY_PROFILES]] — 3 atributos (1 BICC)

---

## ⚙️ Atributos

### [[fnd_setid_sets_vl|FND_SETID_SETS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SetIdSetPEOSetCode | SET_CODE | — | — |
| 2 | SetIdSetPEOSetId | SET_ID | — | — |
| 3 | SetIdSetPEOSetName | SET_NAME | — | ✅ |

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlLedgersLedgerId | LEDGER_ID | — | — |
| 2 | GlLedgersName1 | NAME | — | ✅ |
| 3 | GlLedgersObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[gms_business_units|GMS_BUSINESS_UNITS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BuId | BU_ID | 🔑 | ✅ |
| 2 | GrantsBusinessUnitPEOBillingCycleId | BILLING_CYCLE_ID | — | — |
| 3 | GrantsBusinessUnitPEOContractTypeId | CONTRACT_TYPE_ID | — | — |
| 4 | GrantsBusinessUnitPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | GrantsBusinessUnitPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | GrantsBusinessUnitPEODayToClose | DAY_TO_CLOSE | — | ✅ |
| 7 | GrantsBusinessUnitPEOEventFormatId | EVENT_FORMAT_ID | — | — |
| 8 | GrantsBusinessUnitPEOIndRateSchId | IND_RATE_SCH_ID | — | — |
| 9 | GrantsBusinessUnitPEOInstitutionId | INSTITUTION_ID | — | — |
| 10 | GrantsBusinessUnitPEOInvoiceMethodId | INVOICE_METHOD_ID | — | — |
| 11 | GrantsBusinessUnitPEOLaborFormatId | LABOR_FORMAT_ID | — | — |
| 12 | GrantsBusinessUnitPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | GrantsBusinessUnitPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | GrantsBusinessUnitPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | GrantsBusinessUnitPEONonLaborFormatId | NON_LABOR_FORMAT_ID | — | — |
| 16 | GrantsBusinessUnitPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | GrantsBusinessUnitPEOOnTrackPctTo | ON_TRACK_PCT_TO | — | — |
| 18 | GrantsBusinessUnitPEOOtValueUsedInGraph | OT_VALUE_USED_IN_GRAPH | — | — |
| 19 | GrantsBusinessUnitPEORevenueMethodId | REVENUE_METHOD_ID | — | — |
| 20 | GrantsBusinessUnitPEOUnderSpendPctTo | UNDER_SPEND_PCT_TO | — | — |
| 21 | GrantsBusinessUnitPEOUsValueUsedInGraph | US_VALUE_USED_IN_GRAPH | — | — |

### [[gms_institutions_b|GMS_INSTITUTIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InstitutionPEOInstitutionId | INSTITUTION_ID | — | — |

### [[gms_institutions_tl|GMS_INSTITUTIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InstitutionPEOInstitutionName | INSTITUTION_NAME | — | ✅ |
| 2 | InstitutionTranslationPEOInstitutionId | INSTITUTION_ID | — | — |
| 3 | InstitutionTranslationPEOLanguage | LANGUAGE | — | — |

### [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitId | ORGANIZATION_ID | — | — |
| 2 | BusinessUnitPEODateFrom | EFFECTIVE_START_DATE | — | ✅ |
| 3 | BusinessUnitPEODateTo | EFFECTIVE_END_DATE | — | ✅ |
| 4 | FinancialsBusinessUnitPEOBusinessUnitId1 | ORGANIZATION_ID | — | — |
| 5 | LocationId | LOCATION_ID | — | — |
| 6 | OrganizationUnitPEO1EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 7 | OrganizationUnitPEO1EffectiveStartDate | EFFECTIVE_START_DATE | — | — |

### [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DefaultCurrencyCode | ORG_INFORMATION8 | — | ✅ |
| 2 | DefaultSetId | ORG_INFORMATION4 | — | — |
| 3 | FinancialsBusinessUnitId | ORG_INFORMATION7 | — | — |
| 4 | LegalEntityId | ORG_INFORMATION2 | — | — |
| 5 | ManagerId | ORG_INFORMATION1 | — | — |
| 6 | OrganizationInformationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 7 | OrganizationInformationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 8 | OrganizationInformationPEOOrgInformationId | ORG_INFORMATION_ID | — | — |
| 9 | PrimaryLedgerId | ORG_INFORMATION3 | — | — |

### [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitPEOName | NAME | — | ✅ |
| 2 | FinancialsBusinessUnitPEOName | NAME | — | ✅ |
| 3 | OrganizationUnitTranslationP1EffectiveEndDate6 | EFFECTIVE_END_DATE | — | — |
| 4 | OrganizationUnitTranslationP1EffectiveStartDate6 | EFFECTIVE_START_DATE | — | — |
| 5 | OrganizationUnitTranslationP1Language | LANGUAGE | — | — |
| 6 | OrganizationUnitTranslationP1OrganizationId | ORGANIZATION_ID | — | — |
| 7 | OrganizationUnitTranslationPEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | OrganizationUnitTranslationPEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | OrganizationUnitTranslationPLanguage | LANGUAGE | — | — |
| 10 | OrganizationUnitTranslationPOrganizationId | ORGANIZATION_ID | — | — |

### [[hr_org_unit_classifications_f|HR_ORG_UNIT_CLASSIFICATIONS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrgUnitClassificationPEOEffectiveEndDate4 | EFFECTIVE_END_DATE | — | — |
| 2 | OrgUnitClassificationPEOEffectiveStartDate4 | EFFECTIVE_START_DATE | — | — |
| 3 | OrgUnitClassificationPEOOrgUnitClassificationId | ORG_UNIT_CLASSIFICATION_ID | — | — |
| 4 | Status | STATUS | — | ✅ |

### [[okc_contract_types_b|OKC_CONTRACT_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractTypePEOContractTypeId | CONTRACT_TYPE_ID | — | — |
| 2 | ContractTypePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[okc_contract_types_tl|OKC_CONTRACT_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractTypePEOName | NAME | — | ✅ |
| 2 | ContractTypeTranslationPEOContractTypeId | CONTRACT_TYPE_ID | — | — |
| 3 | ContractTypeTranslationPEOLanguage | LANGUAGE | — | — |
| 4 | ContractTypeTranslationPEOObjectVersionNumber4 | OBJECT_VERSION_NUMBER | — | — |

### [[per_location_details_f|PER_LOCATION_DETAILS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LocationDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | LocationDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | LocationDPEOLocationId | LOCATION_ID | — | — |
| 4 | LocationDetailsBasePEOLocationDetailsId | LOCATION_DETAILS_ID | — | — |

### [[per_location_details_f_tl|PER_LOCATION_DETAILS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LocationDPEOLocationName | LOCATION_NAME | — | ✅ |
| 2 | LocationDetailsTranslationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | LocationDetailsTranslationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | LocationDetailsTranslationPEOLanguage | LANGUAGE | — | — |
| 5 | LocationDetailsTranslationPEOLocationDetailsId | LOCATION_DETAILS_ID | — | — |

### [[per_person_names_f|PER_PERSON_NAMES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonNameDPEODisplayName | DISPLAY_NAME | — | ✅ |
| 2 | PersonNameDPEOEffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 3 | PersonNameDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | PersonNameDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 5 | PersonNameDPEOPersonNameId | PERSON_NAME_ID | — | — |

### [[pjb_billing_methods_tl|PJB_BILLING_METHODS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvoiceMethodPEOBillMethodId | BILL_METHOD_ID | — | — |
| 2 | InvoiceMethodPEOBillMethodName | BILL_METHOD_NAME | — | ✅ |
| 3 | InvoiceMethodTLPEOLanguage | LANGUAGE | — | — |
| 4 | RevenueMethodPEOBillMethodId | BILL_METHOD_ID | — | — |
| 5 | RevenueMethodPEOBillMethodName | BILL_METHOD_NAME | — | ✅ |
| 6 | RevenueMethodTLPEOLanguage | LANGUAGE | — | — |

### [[pjb_invoice_formats|PJB_INVOICE_FORMATS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventFormatPEOInvoiceFormatId | INVOICE_FORMAT_ID | — | — |
| 2 | EventFormatPEOName | NAME | — | ✅ |
| 3 | LaborFormatPEOInvoiceFormatId | INVOICE_FORMAT_ID | — | — |
| 4 | LaborFormatPEOName | NAME | — | ✅ |
| 5 | NonLaborFormatPEOInvoiceFormatId | INVOICE_FORMAT_ID | — | — |
| 6 | NonLaborFormatPEOName | NAME | — | ✅ |

### [[pjf_billing_cycles_tl|PJF_BILLING_CYCLES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BillingCycleId | BILLING_CYCLE_ID | — | — |
| 2 | BillingCycleName | BILLING_CYCLE_NAME | — | ✅ |
| 3 | BillingCycleTLPEOLanguage | LANGUAGE | — | — |
| 4 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[pjf_ind_rate_sch_tl|PJF_IND_RATE_SCH_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BurdenScheduleTLPEOLanguage | LANGUAGE | — | — |
| 2 | PjfIndRateSchVlIndRateSchId | IND_RATE_SCH_ID | — | — |
| 3 | PjfIndRateSchVlIndSchName | IND_SCH_NAME | — | ✅ |

### [[xle_entity_profiles|XLE_ENTITY_PROFILES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DefaultLegalEntityName | NAME | — | ✅ |
| 2 | XleEntityProfilesLegalEntityId1 | LEGAL_ENTITY_ID | — | — |
| 3 | XleEntityProfilesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
