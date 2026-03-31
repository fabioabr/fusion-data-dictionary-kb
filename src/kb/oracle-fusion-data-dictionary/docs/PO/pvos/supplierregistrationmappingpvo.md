---
id: DOC-PO-PVO-SupplierRegistrationMappingPVO
doc_type: system-doc
title: "SupplierRegistrationMappingPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - SupplierRegistrationMappingPVO
  - supplierregistrationmappingpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplierRegistrationMappingPVO

## 📌 Visão Geral

Extrai o mapeamento entre solicitações de registro e fornecedores efetivados, rastreando a conversão de prospects em fornecedores ativos. Permite análise de funil de cadastramento e taxa de conversão.

**Caminho:** `FscmTopModelAM.PrcPozPublicViewAM.SupplierRegistrationMappingPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 70 | 5 | 2 | 26 | 37% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_territories_vl|FND_TERRITORIES_VL]] — 2 atributos (1 BICC)
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 2 atributos (1 BICC)
- [[poz_supplier_mappings|POZ_SUPPLIER_MAPPINGS]] — 2 atributos (1 PKs, 1 BICC)
- [[poz_supplier_registrations|POZ_SUPPLIER_REGISTRATIONS]] — 61 atributos (1 PKs, 22 BICC)
- [[poz_sup_reg_pii|POZ_SUP_REG_PII]] — 3 atributos (1 BICC)

---

## ⚙️ Atributos

### [[fnd_territories_vl|FND_TERRITORIES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TerritoryTerritoryCode | TERRITORY_CODE | — | — |
| 2 | TerritoryTerritoryShortName | TERRITORY_SHORT_NAME | — | ✅ |

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BUBusinessUnitId | BU_ID | — | — |
| 2 | BUName | BU_NAME | — | ✅ |

### [[poz_supplier_mappings|POZ_SUPPLIER_MAPPINGS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SuppMapMappingId | MAPPING_ID | 🔑 | ✅ |
| 2 | SuppMapSupplierRegId | SUPPLIER_REG_ID | — | — |

### [[poz_supplier_registrations|POZ_SUPPLIER_REGISTRATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DeniedPartyFlag | DENIED_PARTY_FLAG | — | — |
| 2 | RejectComments | REJECT_COMMENTS | — | ✅ |
| 3 | RejectReasonCode | REJECT_REASON_CODE | — | ✅ |
| 4 | SupplierRegId | SUPPLIER_REG_ID | 🔑 | ✅ |
| 5 | SupplierRegistrationAddressLine1 | ADDRESS_LINE1 | — | — |
| 6 | SupplierRegistrationAddressLine2 | ADDRESS_LINE2 | — | — |
| 7 | SupplierRegistrationAddressLine3 | ADDRESS_LINE3 | — | — |
| 8 | SupplierRegistrationAddressLine4 | ADDRESS_LINE4 | — | — |
| 9 | SupplierRegistrationAddressNickname | ADDRESS_NICKNAME | — | — |
| 10 | SupplierRegistrationApprovalInstanceId | APPROVAL_INSTANCE_ID | — | — |
| 11 | SupplierRegistrationApprovedDate | APPROVED_DATE | — | ✅ |
| 12 | SupplierRegistrationBcNotApplicableFlag | BC_NOT_APPLICABLE_FLAG | — | — |
| 13 | SupplierRegistrationBusinessRelationshipCode | BUSINESS_RELATIONSHIP_CODE | — | ✅ |
| 14 | SupplierRegistrationCity | CITY | — | — |
| 15 | SupplierRegistrationCorporateWebsite | CORPORATE_WEBSITE | — | ✅ |
| 16 | SupplierRegistrationCountry | COUNTRY | — | — |
| 17 | SupplierRegistrationCounty | COUNTY | — | — |
| 18 | SupplierRegistrationCreatedBy | CREATED_BY | — | — |
| 19 | SupplierRegistrationCreationDate | CREATION_DATE | — | — |
| 20 | SupplierRegistrationDunsNumber | DUNS_NUMBER | — | ✅ |
| 21 | SupplierRegistrationIncomeTaxIdFlag | INCOME_TAX_ID_FLAG | — | — |
| 22 | SupplierRegistrationJustification | JUSTIFICATION | — | ✅ |
| 23 | SupplierRegistrationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 24 | SupplierRegistrationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 25 | SupplierRegistrationLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 26 | SupplierRegistrationNoteFromSupplier | NOTE_FROM_SUPPLIER | — | — |
| 27 | SupplierRegistrationNoteToApprover | NOTE_TO_APPROVER | — | ✅ |
| 28 | SupplierRegistrationNoteToSupplier | NOTE_TO_SUPPLIER | — | — |
| 29 | SupplierRegistrationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 30 | SupplierRegistrationOrganizationType | ORGANIZATION_TYPE | — | ✅ |
| 31 | SupplierRegistrationPostalCode | POSTAL_CODE | — | — |
| 32 | SupplierRegistrationPrcBuId | PRC_BU_ID | — | — |
| 33 | SupplierRegistrationProvince | PROVINCE | — | — |
| 34 | SupplierRegistrationRegKey | REG_KEY | — | — |
| 35 | SupplierRegistrationRegistrationStatus | REGISTRATION_STATUS | — | ✅ |
| 36 | SupplierRegistrationRegistrationType | REGISTRATION_TYPE | — | ✅ |
| 37 | SupplierRegistrationRejectionCode | REJECTION_CODE | — | — |
| 38 | SupplierRegistrationReqToResubmitReason | REQ_TO_RESUBMIT_REASON | — | — |
| 39 | SupplierRegistrationRequestNumber | REQUEST_NUMBER | — | ✅ |
| 40 | SupplierRegistrationRequestReasonCode | REQUEST_REASON_CODE | — | ✅ |
| 41 | SupplierRegistrationRequestedDate | REQUESTED_DATE | — | ✅ |
| 42 | SupplierRegistrationRequesterEmailAddress | REQUESTER_EMAIL_ADDRESS | — | ✅ |
| 43 | SupplierRegistrationRequesterFirstName | REQUESTER_FIRST_NAME | — | ✅ |
| 44 | SupplierRegistrationRequesterLanguage | REQUESTER_LANGUAGE | — | — |
| 45 | SupplierRegistrationRequesterLastName | REQUESTER_LAST_NAME | — | ✅ |
| 46 | SupplierRegistrationRequesterPersonId | REQUESTER_PERSON_ID | — | — |
| 47 | SupplierRegistrationResubmissionNum | RESUBMISSION_NUM | — | — |
| 48 | SupplierRegistrationState | STATE | — | — |
| 49 | SupplierRegistrationSupplierCreationStatus | SUPPLIER_CREATION_STATUS | — | ✅ |
| 50 | SupplierRegistrationSupplierName | SUPPLIER_NAME | — | ✅ |
| 51 | SupplierRegistrationSupplierNumber | SUPPLIER_NUMBER | — | — |
| 52 | SupplierRegistrationTaxRegCountryCode | TAX_REG_COUNTRY_CODE | — | — |
| 53 | SupplierRegistrationTaxRegNumberFlag | TAX_REG_NUMBER_FLAG | — | — |
| 54 | SupplierRegistrationTaxRegType | TAX_REG_TYPE | — | — |
| 55 | SupplierRegistrationTaxRegistrationNumber | TAX_REGISTRATION_NUMBER | — | — |
| 56 | SupplierRegistrationTaxpayerId | TAXPAYER_ID | — | — |
| 57 | SupplierRegistrationUrlValidationParam | URL_VALIDATION_PARAM | — | — |
| 58 | SupplierRegistrationUserRegId | USER_REG_ID | — | — |
| 59 | SupplierRegistrationVendorId | VENDOR_ID | — | — |
| 60 | SupplierRegistrationVendorPartyId | VENDOR_PARTY_ID | — | — |
| 61 | SupplierRegistrationVendorTypeLookupCode | VENDOR_TYPE_LOOKUP_CODE | — | ✅ |

### [[poz_sup_reg_pii|POZ_SUP_REG_PII]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SuppRegPiiIncomeTaxId | INCOME_TAX_ID | — | ✅ |
| 2 | SuppRegPiiSupplierRegId1 | SUPPLIER_REG_ID | — | — |
| 3 | SuppRegPiiTaxRegistrationNumber | TAX_REGISTRATION_NUMBER | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
