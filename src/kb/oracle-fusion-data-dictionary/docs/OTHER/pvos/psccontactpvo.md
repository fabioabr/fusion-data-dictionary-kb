---
id: DOC-OTHER-PVO-PSCContactPVO
doc_type: system-doc
title: "PSCContactPVO — PVO Cross-Module"
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
  - PSCContactPVO
  - psccontactpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PSCContactPVO

## 📌 Visão Geral

View Object para extração BICC de dados de PSCContact. Acessa as tabelas: PSC_COM_CONTACT_TYPE_TL, PSC_LNP_CONTACT_LIST.

**Caminho:** `FscmTopModelAM.PscPermitsReportingAM.PSCContactPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 48 | 2 | 1 | 31 | 65% |

---

## 🔗 Tabelas Relacionadas

- [[psc_com_contact_type_tl|PSC_COM_CONTACT_TYPE_TL]] — 11 atributos (1 BICC)
- [[psc_lnp_contact_list|PSC_LNP_CONTACT_LIST]] — 37 atributos (1 PKs, 30 BICC)

---

## ⚙️ Atributos

### [[psc_com_contact_type_tl|PSC_COM_CONTACT_TYPE_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContactTypeTLPEOAgencyId | AGENCY_ID | — | — |
| 2 | ContactTypeTLPEOContactType | CONTACT_TYPE | — | — |
| 3 | ContactTypeTLPEOCreatedBy | CREATED_BY | — | — |
| 4 | ContactTypeTLPEOCreationDate | CREATION_DATE | — | — |
| 5 | ContactTypeTLPEODescription | DESCRIPTION | — | ✅ |
| 6 | ContactTypeTLPEOLanguage | LANGUAGE | — | — |
| 7 | ContactTypeTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 8 | ContactTypeTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ContactTypeTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ContactTypeTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | ContactTypeTLPEOSourceLang | SOURCE_LANG | — | — |

### [[psc_lnp_contact_list|PSC_LNP_CONTACT_LIST]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContactPEOAddress1 | ADDRESS1 | — | ✅ |
| 2 | ContactPEOAddress2 | ADDRESS2 | — | ✅ |
| 3 | ContactPEOAddress3 | ADDRESS3 | — | ✅ |
| 4 | ContactPEOAddress4 | ADDRESS4 | — | ✅ |
| 5 | ContactPEOAgencyId | AGENCY_ID | — | — |
| 6 | ContactPEOCity | CITY | — | ✅ |
| 7 | ContactPEOContactBizPartyId | CONTACT_BIZ_PARTY_ID | — | — |
| 8 | ContactPEOContactKey | CONTACT_KEY | 🔑 | ✅ |
| 9 | ContactPEOContactPartyId | CONTACT_PARTY_ID | — | — |
| 10 | ContactPEOContactType | CONTACT_TYPE | — | ✅ |
| 11 | ContactPEOCountry | COUNTRY | — | ✅ |
| 12 | ContactPEOCounty | COUNTY | — | ✅ |
| 13 | ContactPEOCreatedBy | CREATED_BY | — | ✅ |
| 14 | ContactPEOCreationDate | CREATION_DATE | — | ✅ |
| 15 | ContactPEODateOfBirth | DATE_OF_BIRTH | — | ✅ |
| 16 | ContactPEOEmailAddress1 | EMAIL_ADDRESS1 | — | ✅ |
| 17 | ContactPEOGender | GENDER | — | ✅ |
| 18 | ContactPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 19 | ContactPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 20 | ContactPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 21 | ContactPEOLnpRecordId | LNP_RECORD_ID | — | — |
| 22 | ContactPEOLnpRecordKey | LNP_RECORD_KEY | — | — |
| 23 | ContactPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 24 | ContactPEOOrganizationName | ORGANIZATION_NAME | — | ✅ |
| 25 | ContactPEOPersonFirstName | PERSON_FIRST_NAME | — | ✅ |
| 26 | ContactPEOPersonLastName | PERSON_LAST_NAME | — | ✅ |
| 27 | ContactPEOPersonMiddleName | PERSON_MIDDLE_NAME | — | ✅ |
| 28 | ContactPEOPersonName | PERSON_NAME | — | ✅ |
| 29 | ContactPEOPersonNameSuffix | PERSON_NAME_SUFFIX | — | ✅ |
| 30 | ContactPEOPersonPreNameAdjunct | PERSON_PRE_NAME_ADJUNCT | — | ✅ |
| 31 | ContactPEOPersonTitle | PERSON_TITLE | — | ✅ |
| 32 | ContactPEOPhoneNumber | PHONE_NUMBER | — | ✅ |
| 33 | ContactPEOPostalCode | POSTAL_CODE | — | ✅ |
| 34 | ContactPEOPostalPlus4Code | POSTAL_PLUS4_CODE | — | ✅ |
| 35 | ContactPEOPrimaryFlag | PRIMARY_FLAG | — | ✅ |
| 36 | ContactPEOProvince | PROVINCE | — | ✅ |
| 37 | ContactPEOState | STATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
