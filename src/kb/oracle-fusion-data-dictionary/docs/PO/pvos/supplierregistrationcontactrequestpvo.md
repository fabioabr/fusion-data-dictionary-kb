---
id: DOC-PO-PVO-SupplierRegistrationContactRequestPVO
doc_type: system-doc
title: "SupplierRegistrationContactRequestPVO — PVO Purchasing"
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
  - SupplierRegistrationContactRequestPVO
  - supplierregistrationcontactrequestpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplierRegistrationContactRequestPVO

## 📌 Visão Geral

Extrai os contatos informados durante o registro de novos fornecedores, incluindo nome, e-mail e telefone. Facilita comunicação e acompanhamento do processo de cadastramento.

**Caminho:** `FscmTopModelAM.PrcPozPublicViewAM.SupplierRegistrationContactRequestPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 37 | 1 | 1 | 20 | 54% |

---

## 🔗 Tabelas Relacionadas

- [[poz_contact_requests|POZ_CONTACT_REQUESTS]] — 37 atributos (1 PKs, 20 BICC)

---

## ⚙️ Atributos

### [[poz_contact_requests|POZ_CONTACT_REQUESTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContactRequestId | CONTACT_REQUEST_ID | 🔑 | ✅ |
| 2 | SupplierRegContactRequestAdministrativeContact | ADMINISTRATIVE_CONTACT | — | ✅ |
| 3 | SupplierRegContactRequestApprovalInstanceId | APPROVAL_INSTANCE_ID | — | — |
| 4 | SupplierRegContactRequestChangeRequestNumber | CHANGE_REQUEST_NUMBER | — | — |
| 5 | SupplierRegContactRequestChangeSource | CHANGE_SOURCE | — | — |
| 6 | SupplierRegContactRequestContactPartyId | CONTACT_PARTY_ID | — | — |
| 7 | SupplierRegContactRequestContactTitle | CONTACT_TITLE | — | ✅ |
| 8 | SupplierRegContactRequestCreateUserAccount | CREATE_USER_ACCOUNT | — | ✅ |
| 9 | SupplierRegContactRequestCreatedBy | CREATED_BY | — | — |
| 10 | SupplierRegContactRequestCreationDate | CREATION_DATE | — | — |
| 11 | SupplierRegContactRequestEmailAddress | EMAIL_ADDRESS | — | ✅ |
| 12 | SupplierRegContactRequestFaxAreaCode | FAX_AREA_CODE | — | ✅ |
| 13 | SupplierRegContactRequestFaxCountryCode | FAX_COUNTRY_CODE | — | ✅ |
| 14 | SupplierRegContactRequestFaxNumber | FAX_NUMBER | — | ✅ |
| 15 | SupplierRegContactRequestFirstName | FIRST_NAME | — | ✅ |
| 16 | SupplierRegContactRequestHasBackingDoc | HAS_BACKING_DOC | — | — |
| 17 | SupplierRegContactRequestJobTitle | JOB_TITLE | — | ✅ |
| 18 | SupplierRegContactRequestLastName | LAST_NAME | — | ✅ |
| 19 | SupplierRegContactRequestLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 20 | SupplierRegContactRequestLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 21 | SupplierRegContactRequestLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 22 | SupplierRegContactRequestMappingId | MAPPING_ID | — | — |
| 23 | SupplierRegContactRequestMiddleName | MIDDLE_NAME | — | ✅ |
| 24 | SupplierRegContactRequestMobileAreaCode | MOBILE_AREA_CODE | — | ✅ |
| 25 | SupplierRegContactRequestMobileCountryCode | MOBILE_COUNTRY_CODE | — | ✅ |
| 26 | SupplierRegContactRequestMobileNumber | MOBILE_NUMBER | — | ✅ |
| 27 | SupplierRegContactRequestNotes | NOTES | — | — |
| 28 | SupplierRegContactRequestObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 29 | SupplierRegContactRequestPhoneAreaCode | PHONE_AREA_CODE | — | ✅ |
| 30 | SupplierRegContactRequestPhoneCountryCode | PHONE_COUNTRY_CODE | — | ✅ |
| 31 | SupplierRegContactRequestPhoneExtension | PHONE_EXTENSION | — | ✅ |
| 32 | SupplierRegContactRequestPhoneNumber | PHONE_NUMBER | — | ✅ |
| 33 | SupplierRegContactRequestPrimaryAdminContact | PRIMARY_ADMIN_CONTACT | — | — |
| 34 | SupplierRegContactRequestRequestStatus | REQUEST_STATUS | — | — |
| 35 | SupplierRegContactRequestRequestType | REQUEST_TYPE | — | — |
| 36 | SupplierRegContactRequestRequestedEndDate | REQUESTED_END_DATE | — | — |
| 37 | SupplierRegContactRequestRequestedStartDate | REQUESTED_START_DATE | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
