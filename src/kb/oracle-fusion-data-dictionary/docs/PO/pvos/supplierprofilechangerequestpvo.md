---
id: DOC-PO-PVO-SupplierProfileChangeRequestPVO
doc_type: system-doc
title: "SupplierProfileChangeRequestPVO — PVO Purchasing"
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
  - SupplierProfileChangeRequestPVO
  - supplierprofilechangerequestpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplierProfileChangeRequestPVO

## 📌 Visão Geral

Extrai as solicitações de alteração de perfil de fornecedores, incluindo campos modificados, solicitante, justificativa e status. Permite rastreabilidade de mudanças cadastrais e compliance.

**Caminho:** `FscmTopModelAM.PrcPozPublicViewAM.SupplierProfileChangeRequestPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 61 | 4 | 1 | 16 | 26% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_lookups|FND_LOOKUPS]] — 10 atributos (2 BICC)
- [[hz_parties|HZ_PARTIES]] — 7 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 9 atributos
- [[poz_supp_requests|POZ_SUPP_REQUESTS]] — 35 atributos (1 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[fnd_lookups|FND_LOOKUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RequestSourceLookupPEODescription | DESCRIPTION | — | — |
| 2 | RequestSourceLookupPEOEnabledFlag | ENABLED_FLAG | — | — |
| 3 | RequestSourceLookupPEOLookupCode | LOOKUP_CODE | — | — |
| 4 | RequestSourceLookupPEOLookupType | LOOKUP_TYPE | — | — |
| 5 | RequestSourceLookupPEOMeaning | MEANING | — | ✅ |
| 6 | RequestStatusLookupPEODescription | DESCRIPTION | — | — |
| 7 | RequestStatusLookupPEOEnabledFlag | ENABLED_FLAG | — | — |
| 8 | RequestStatusLookupPEOLookupCode | LOOKUP_CODE | — | — |
| 9 | RequestStatusLookupPEOLookupType | LOOKUP_TYPE | — | — |
| 10 | RequestStatusLookupPEOMeaning | MEANING | — | ✅ |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RequestedByPartyPEOPartyId | PARTY_ID | — | — |
| 2 | RequestedByPartyPEOPartyName | PARTY_NAME | — | — |
| 3 | RequestedByPartyPEOPartyNumber | PARTY_NUMBER | — | — |
| 4 | RequestedByPartyPEOPartyType | PARTY_TYPE | — | — |
| 5 | RequestedByPartyPEOPersonFirstName | PERSON_FIRST_NAME | — | — |
| 6 | RequestedByPartyPEOPersonLastName | PERSON_LAST_NAME | — | — |
| 7 | RequestedByPartyPEOStatus | STATUS | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RequestedByPersonNamePEODisplayName | DISPLAY_NAME | — | — |
| 2 | RequestedByPersonNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | RequestedByPersonNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | RequestedByPersonNamePEOFirstName | FIRST_NAME | — | — |
| 5 | RequestedByPersonNamePEOFullName | FULL_NAME | — | — |
| 6 | RequestedByPersonNamePEOLastName | LAST_NAME | — | — |
| 7 | RequestedByPersonNamePEOListName | LIST_NAME | — | — |
| 8 | RequestedByPersonNamePEOPersonId | PERSON_ID | — | — |
| 9 | RequestedByPersonNamePEOPersonNameId | PERSON_NAME_ID | — | — |

### [[poz_supp_requests|POZ_SUPP_REQUESTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChangeRequestPEOActionByPartyId | ACTION_BY_PARTY_ID | — | — |
| 2 | ChangeRequestPEOActionByPersonId | ACTION_BY_PERSON_ID | — | — |
| 3 | ChangeRequestPEOActionDate | ACTION_DATE | — | — |
| 4 | ChangeRequestPEOActionReason | ACTION_REASON | — | — |
| 5 | ChangeRequestPEOApprovalInstanceId | APPROVAL_INSTANCE_ID | — | — |
| 6 | ChangeRequestPEOBcNotApplicableNewFlag | BC_NOT_APPLICABLE_NEW_FLAG | — | — |
| 7 | ChangeRequestPEOBcNotApplicableOldFlag | BC_NOT_APPLICABLE_OLD_FLAG | — | — |
| 8 | ChangeRequestPEOChangeDescription | CHANGE_DESCRIPTION | — | ✅ |
| 9 | ChangeRequestPEOChangeReqNumber | CHANGE_REQ_NUMBER | — | ✅ |
| 10 | ChangeRequestPEOChangeReqSubmissionDate | CHANGE_REQ_SUBMISSION_DATE | — | ✅ |
| 11 | ChangeRequestPEOChangedAddressesFlag | CHANGED_ADDRESSES_FLAG | — | ✅ |
| 12 | ChangeRequestPEOChangedBankAccountsFlag | CHANGED_BANK_ACCOUNTS_FLAG | — | ✅ |
| 13 | ChangeRequestPEOChangedBusClassDetailsFlag | CHANGED_BUS_CLASS_DETAILS_FLAG | — | ✅ |
| 14 | ChangeRequestPEOChangedContactsFlag | CHANGED_CONTACTS_FLAG | — | ✅ |
| 15 | ChangeRequestPEOChangedOrgDetailsFlag | CHANGED_ORG_DETAILS_FLAG | — | ✅ |
| 16 | ChangeRequestPEOChangedPaymentMethodFlag | CHANGED_PAYMENT_METHOD_FLAG | — | ✅ |
| 17 | ChangeRequestPEOChangedProdServFlag | CHANGED_PROD_SERV_FLAG | — | ✅ |
| 18 | ChangeRequestPEOChangedSitesFlag | CHANGED_SITES_FLAG | — | ✅ |
| 19 | ChangeRequestPEOChangedTaxDetailsFlag | CHANGED_TAX_DETAILS_FLAG | — | ✅ |
| 20 | ChangeRequestPEOChangedUserAccountFlag | CHANGED_USER_ACCOUNT_FLAG | — | ✅ |
| 21 | ChangeRequestPEOCreatedBy | CREATED_BY | — | — |
| 22 | ChangeRequestPEOCreationDate | CREATION_DATE | — | — |
| 23 | ChangeRequestPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 24 | ChangeRequestPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 25 | ChangeRequestPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 26 | ChangeRequestPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 27 | ChangeRequestPEORequestByPartyId | REQUEST_BY_PARTY_ID | — | — |
| 28 | ChangeRequestPEORequestByPersonId | REQUEST_BY_PERSON_ID | — | — |
| 29 | ChangeRequestPEORequestSourceCode | REQUEST_SOURCE_CODE | — | — |
| 30 | ChangeRequestPEORequestStatusCode | REQUEST_STATUS_CODE | — | — |
| 31 | ChangeRequestPEOResubmissionNum | RESUBMISSION_NUM | — | — |
| 32 | ChangeRequestPEOSourceDocumentNumber | SOURCE_DOCUMENT_NUMBER | — | — |
| 33 | ChangeRequestPEOSourcingBatchId | SOURCING_BATCH_ID | — | — |
| 34 | ChangeRequestPEOSuppRequestId | SUPP_REQUEST_ID | 🔑 | ✅ |
| 35 | ChangeRequestPEOVendorId | VENDOR_ID | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
