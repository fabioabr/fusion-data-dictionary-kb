---
id: DOC-OTHER-PVO-SponsorAgreementsPVO
doc_type: system-doc
title: "SponsorAgreementsPVO — PVO Cross-Module"
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
  - SponsorAgreementsPVO
  - sponsoragreementspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SponsorAgreementsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Sponsor Agreements. Acessa as tabelas: FUN_ALL_BUSINESS_UNITS_V, HES_SPONSOR_AGREEMENTS_ALL_VL.

**Caminho:** `FscmTopModelAM.HedHesSharedCustAccountAM.SponsorAgreementsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 97 | 2 | 1 | 16 | 16% |

---

## 🔗 Tabelas Relacionadas

- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 21 atributos (2 BICC)
- [[hes_sponsor_agreements_all_vl|HES_SPONSOR_AGREEMENTS_ALL_VL]] — 76 atributos (1 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitPEOBuName | BU_NAME | — | ✅ |
| 2 | BusinessUnitPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | BusinessUnitPEOBusinessUnitPEOBuId | BU_ID | — | — |
| 4 | BusinessUnitPEOCreatedBy | CREATED_BY | — | — |
| 5 | BusinessUnitPEOCreationDate | CREATION_DATE | — | — |
| 6 | BusinessUnitPEODateFrom | DATE_FROM | — | — |
| 7 | BusinessUnitPEODateTo | DATE_TO | — | — |
| 8 | BusinessUnitPEODefaultCurrencyCode | DEFAULT_CURRENCY_CODE | — | — |
| 9 | BusinessUnitPEODefaultSetId | DEFAULT_SET_ID | — | — |
| 10 | BusinessUnitPEOEnabledForHrFlag | ENABLED_FOR_HR_FLAG | — | — |
| 11 | BusinessUnitPEOFinBusinessUnitId | FIN_BUSINESS_UNIT_ID | — | — |
| 12 | BusinessUnitPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | BusinessUnitPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | BusinessUnitPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | BusinessUnitPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 16 | BusinessUnitPEOLocationId | LOCATION_ID | — | — |
| 17 | BusinessUnitPEOManagerId | MANAGER_ID | — | — |
| 18 | BusinessUnitPEOPrimaryLedgerId | PRIMARY_LEDGER_ID | — | — |
| 19 | BusinessUnitPEOProfitCenterFlag | PROFIT_CENTER_FLAG | — | — |
| 20 | BusinessUnitPEOShortCode | SHORT_CODE | — | — |
| 21 | BusinessUnitPEOStatus | STATUS | — | — |

### [[hes_sponsor_agreements_all_vl|HES_SPONSOR_AGREEMENTS_ALL_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SponsorAgreementsPEOAgreementLongDescription | AGREEMENT_LONG_DESCRIPTION | — | ✅ |
| 2 | SponsorAgreementsPEOAgreementPriority | AGREEMENT_PRIORITY | — | ✅ |
| 3 | SponsorAgreementsPEOAgreementShortDescription | AGREEMENT_SHORT_DESCRIPTION | — | ✅ |
| 4 | SponsorAgreementsPEOAgreementStatusCode | AGREEMENT_STATUS_CODE | — | ✅ |
| 5 | SponsorAgreementsPEOAgreementTypeCode | AGREEMENT_TYPE_CODE | — | — |
| 6 | SponsorAgreementsPEOAttribute1 | ATTRIBUTE1 | — | — |
| 7 | SponsorAgreementsPEOAttribute10 | ATTRIBUTE10 | — | — |
| 8 | SponsorAgreementsPEOAttribute11 | ATTRIBUTE11 | — | — |
| 9 | SponsorAgreementsPEOAttribute12 | ATTRIBUTE12 | — | — |
| 10 | SponsorAgreementsPEOAttribute13 | ATTRIBUTE13 | — | — |
| 11 | SponsorAgreementsPEOAttribute14 | ATTRIBUTE14 | — | — |
| 12 | SponsorAgreementsPEOAttribute15 | ATTRIBUTE15 | — | — |
| 13 | SponsorAgreementsPEOAttribute16 | ATTRIBUTE16 | — | — |
| 14 | SponsorAgreementsPEOAttribute17 | ATTRIBUTE17 | — | — |
| 15 | SponsorAgreementsPEOAttribute18 | ATTRIBUTE18 | — | — |
| 16 | SponsorAgreementsPEOAttribute19 | ATTRIBUTE19 | — | — |
| 17 | SponsorAgreementsPEOAttribute2 | ATTRIBUTE2 | — | — |
| 18 | SponsorAgreementsPEOAttribute20 | ATTRIBUTE20 | — | — |
| 19 | SponsorAgreementsPEOAttribute3 | ATTRIBUTE3 | — | — |
| 20 | SponsorAgreementsPEOAttribute4 | ATTRIBUTE4 | — | — |
| 21 | SponsorAgreementsPEOAttribute5 | ATTRIBUTE5 | — | — |
| 22 | SponsorAgreementsPEOAttribute6 | ATTRIBUTE6 | — | — |
| 23 | SponsorAgreementsPEOAttribute7 | ATTRIBUTE7 | — | — |
| 24 | SponsorAgreementsPEOAttribute8 | ATTRIBUTE8 | — | — |
| 25 | SponsorAgreementsPEOAttribute9 | ATTRIBUTE9 | — | — |
| 26 | SponsorAgreementsPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 27 | SponsorAgreementsPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 28 | SponsorAgreementsPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 29 | SponsorAgreementsPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 30 | SponsorAgreementsPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 31 | SponsorAgreementsPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 32 | SponsorAgreementsPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 33 | SponsorAgreementsPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 34 | SponsorAgreementsPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 35 | SponsorAgreementsPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 36 | SponsorAgreementsPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 37 | SponsorAgreementsPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 38 | SponsorAgreementsPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 39 | SponsorAgreementsPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 40 | SponsorAgreementsPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 41 | SponsorAgreementsPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 42 | SponsorAgreementsPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 43 | SponsorAgreementsPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 44 | SponsorAgreementsPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 45 | SponsorAgreementsPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 46 | SponsorAgreementsPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 47 | SponsorAgreementsPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 48 | SponsorAgreementsPEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 49 | SponsorAgreementsPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 50 | SponsorAgreementsPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 51 | SponsorAgreementsPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 52 | SponsorAgreementsPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 53 | SponsorAgreementsPEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 54 | SponsorAgreementsPEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 55 | SponsorAgreementsPEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 56 | SponsorAgreementsPEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 57 | SponsorAgreementsPEOContactTypeCode | CONTACT_TYPE_CODE | — | ✅ |
| 58 | SponsorAgreementsPEOCreatedBy | CREATED_BY | — | — |
| 59 | SponsorAgreementsPEOCreationDate | CREATION_DATE | — | — |
| 60 | SponsorAgreementsPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 61 | SponsorAgreementsPEOCurriculumId | CURRICULUM_ID | — | — |
| 62 | SponsorAgreementsPEOCustomerAccountId | CUSTOMER_ACCOUNT_ID | — | — |
| 63 | SponsorAgreementsPEOEndReportingPeriodId | END_REPORTING_PERIOD_ID | — | — |
| 64 | SponsorAgreementsPEOEnforceMaximumFlag | ENFORCE_MAXIMUM_FLAG | — | ✅ |
| 65 | SponsorAgreementsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 66 | SponsorAgreementsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 67 | SponsorAgreementsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 68 | SponsorAgreementsPEOMaximumAmountContract | MAXIMUM_AMOUNT_CONTRACT | — | ✅ |
| 69 | SponsorAgreementsPEOMaximumAmountStudent | MAXIMUM_AMOUNT_STUDENT | — | ✅ |
| 70 | SponsorAgreementsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 71 | SponsorAgreementsPEOOrgId | ORG_ID | — | ✅ |
| 72 | SponsorAgreementsPEOServiceImpactId | SERVICE_IMPACT_ID | — | ✅ |
| 73 | SponsorAgreementsPEOSponsorAgreementId | SPONSOR_AGREEMENT_ID | 🔑 | ✅ |
| 74 | SponsorAgreementsPEOSponsorAgreementName | SPONSOR_AGREEMENT_NAME | — | ✅ |
| 75 | SponsorAgreementsPEOSponsorPartyId | SPONSOR_PARTY_ID | — | — |
| 76 | SponsorAgreementsPEOStartReportingPeriodId | START_REPORTING_PERIOD_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
