---
id: DOC-OTHER-PVO-SponsorPVO
doc_type: system-doc
title: "SponsorPVO — PVO Cross-Module"
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
  - SponsorPVO
  - sponsorpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SponsorPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Sponsor. Acessa as tabelas: GMS_SPONSORS_VL, HZ_CUST_ACCOUNTS, HZ_PARTIES (+1).

**Caminho:** `FscmTopModelAM.GmsSetupAM.SponsorPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 65 | 4 | 1 | 65 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gms_sponsors_vl|GMS_SPONSORS_VL]] — 18 atributos (1 PKs, 18 BICC)
- [[hz_cust_accounts|HZ_CUST_ACCOUNTS]] — 6 atributos (6 BICC)
- [[hz_parties|HZ_PARTIES]] — 39 atributos (39 BICC)
- [[pjf_ind_rate_sch_vl|PJF_IND_RATE_SCH_VL]] — 2 atributos (2 BICC)

---

## ⚙️ Atributos

### [[gms_sponsors_vl|GMS_SPONSORS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BillToSponsorPEOBillToSponsor | BILL_TO_SPONSOR | — | ✅ |
| 2 | BillToSponsorPEOSponsorId1 | SPONSOR_ID | — | ✅ |
| 3 | RelatedSponsorAcctId | RELATED_SPONSOR_ACCT_ID | — | ✅ |
| 4 | SponsorId | SPONSOR_ID | 🔑 | ✅ |
| 5 | SponsorPEOBillToSponsor | BILL_TO_SPONSOR | — | ✅ |
| 6 | SponsorPEOComments | COMMENTS | — | ✅ |
| 7 | SponsorPEOCreatedBy | CREATED_BY | — | ✅ |
| 8 | SponsorPEOCreationDate | CREATION_DATE | — | ✅ |
| 9 | SponsorPEOFederalFlag | FEDERAL_FLAG | — | ✅ |
| 10 | SponsorPEOIndRateSchId | IND_RATE_SCH_ID | — | ✅ |
| 11 | SponsorPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | SponsorPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | SponsorPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | SponsorPEOLocFlag | LOC_FLAG | — | ✅ |
| 15 | SponsorPEOLocNumber | LOC_NUMBER | — | ✅ |
| 16 | SponsorPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 17 | SponsorPEOPartyId | PARTY_ID | — | ✅ |
| 18 | SponsorPEOSponsorAcctId | SPONSOR_ACCT_ID | — | ✅ |

### [[hz_cust_accounts|HZ_CUST_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustomerAccountPEOAccountName | ACCOUNT_NAME | — | ✅ |
| 2 | CustomerAccountPEOAccountNumber | ACCOUNT_NUMBER | — | ✅ |
| 3 | CustomerAccountPEOCustAccountId | CUST_ACCOUNT_ID | — | ✅ |
| 4 | RelatedCustomerAccountPEOAccountName | ACCOUNT_NAME | — | ✅ |
| 5 | RelatedCustomerAccountPEOAccountNumber | ACCOUNT_NUMBER | — | ✅ |
| 6 | RelatedCustomerAccountPEOCustAccountId | CUST_ACCOUNT_ID | — | ✅ |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BillToPartyPEOPartyId | PARTY_ID | — | ✅ |
| 2 | BillToPartyPEOPartyName | PARTY_NAME | — | ✅ |
| 3 | BillToPartyPEOPartyNumber | PARTY_NUMBER | — | ✅ |
| 4 | PartyPEOAddress1 | ADDRESS1 | — | ✅ |
| 5 | PartyPEOAddress2 | ADDRESS2 | — | ✅ |
| 6 | PartyPEOAddress3 | ADDRESS3 | — | ✅ |
| 7 | PartyPEOAddress4 | ADDRESS4 | — | ✅ |
| 8 | PartyPEOCity | CITY | — | ✅ |
| 9 | PartyPEOCountry | COUNTRY | — | ✅ |
| 10 | PartyPEOCounty | COUNTY | — | ✅ |
| 11 | PartyPEOEmailAddress | EMAIL_ADDRESS | — | ✅ |
| 12 | PartyPEOPartyId | PARTY_ID | — | ✅ |
| 13 | PartyPEOPartyName | PARTY_NAME | — | ✅ |
| 14 | PartyPEOPartyNumber | PARTY_NUMBER | — | ✅ |
| 15 | PartyPEOPostalCode | POSTAL_CODE | — | ✅ |
| 16 | PartyPEOPreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | ✅ |
| 17 | PartyPEOPrimaryPhoneAreaCode | PRIMARY_PHONE_AREA_CODE | — | ✅ |
| 18 | PartyPEOPrimaryPhoneCountryCode | PRIMARY_PHONE_COUNTRY_CODE | — | ✅ |
| 19 | PartyPEOPrimaryPhoneExtension | PRIMARY_PHONE_EXTENSION | — | ✅ |
| 20 | PartyPEOPrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | ✅ |
| 21 | PartyPEOState | STATE | — | ✅ |
| 22 | PartyPEOStatus | STATUS | — | ✅ |
| 23 | PartyPEOUrl | URL | — | ✅ |
| 24 | PartyPrimaryContactAddress1 | ADDRESS1 | — | ✅ |
| 25 | PartyPrimaryContactAddress2 | ADDRESS2 | — | ✅ |
| 26 | PartyPrimaryContactAddress3 | ADDRESS3 | — | ✅ |
| 27 | PartyPrimaryContactAddress4 | ADDRESS4 | — | ✅ |
| 28 | PartyPrimaryContactCity | CITY | — | ✅ |
| 29 | PartyPrimaryContactCountry | COUNTRY | — | ✅ |
| 30 | PartyPrimaryContactCounty | COUNTY | — | ✅ |
| 31 | PartyPrimaryContactEmailAddress | EMAIL_ADDRESS | — | ✅ |
| 32 | PartyPrimaryContactPartyId | PARTY_ID | — | ✅ |
| 33 | PartyPrimaryContactPartyName | PARTY_NAME | — | ✅ |
| 34 | PartyPrimaryContactPostalCode | POSTAL_CODE | — | ✅ |
| 35 | PartyPrimaryContactPrimaryPhoneAreaCode | PRIMARY_PHONE_AREA_CODE | — | ✅ |
| 36 | PartyPrimaryContactPrimaryPhoneCountryCode | PRIMARY_PHONE_COUNTRY_CODE | — | ✅ |
| 37 | PartyPrimaryContactPrimaryPhoneExtension | PRIMARY_PHONE_EXTENSION | — | ✅ |
| 38 | PartyPrimaryContactPrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | ✅ |
| 39 | PartyPrimaryContactState | STATE | — | ✅ |

### [[pjf_ind_rate_sch_vl|PJF_IND_RATE_SCH_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BurdenSchedulePEOIndRateSchId | IND_RATE_SCH_ID | — | ✅ |
| 2 | BurdenSchedulePEOIndSchName | IND_SCH_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
