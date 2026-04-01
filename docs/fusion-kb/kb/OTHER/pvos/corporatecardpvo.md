---
id: DOC-OTHER-PVO-CorporateCardPVO
doc_type: system-doc
title: "CorporateCardPVO — PVO Cross-Module"
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
  - CorporateCardPVO
  - corporatecardpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CorporateCardPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Corporate Card. Acessa as tabelas: EXM_CARDS, EXM_CARD_PROGRAMS, EXM_CC_COMPANY_ACCOUNTS (+2).

**Caminho:** `FscmTopModelAM.FinExmEntrySharedAM.CorporateCardPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 68 | 5 | 1 | 16 | 24% |

---

## 🔗 Tabelas Relacionadas

- [[exm_cards|EXM_CARDS]] — 42 atributos (1 PKs, 12 BICC)
- [[exm_card_programs|EXM_CARD_PROGRAMS]] — 3 atributos (1 BICC)
- [[exm_cc_company_accounts|EXM_CC_COMPANY_ACCOUNTS]] — 3 atributos (1 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos (2 BICC)
- [[per_users|PER_USERS]] — 10 atributos

---

## ⚙️ Atributos

### [[exm_cards|EXM_CARDS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CardPEOAccountCategoryCode | ACCOUNT_CATEGORY_CODE | — | — |
| 2 | CardPEOAccountTypeCode | ACCOUNT_TYPE_CODE | — | — |
| 3 | CardPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 4 | CardPEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 5 | CardPEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 6 | CardPEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 7 | CardPEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 8 | CardPEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 9 | CardPEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 10 | CardPEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 11 | CardPEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 12 | CardPEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 13 | CardPEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 14 | CardPEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 15 | CardPEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 16 | CardPEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 17 | CardPEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 18 | CardPEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 19 | CardPEOCardExpirationDate | CARD_EXPIRATION_DATE | — | ✅ |
| 20 | CardPEOCardId | CARD_ID | 🔑 | ✅ |
| 21 | CardPEOCardNumber | CARD_NUMBER | — | ✅ |
| 22 | CardPEOCardProgramId | CARD_PROGRAM_ID | — | — |
| 23 | CardPEOCardReferenceId | CARD_REFERENCE_ID | — | — |
| 24 | CardPEOCardStatusCode | CARD_STATUS_CODE | — | ✅ |
| 25 | CardPEOCardmemberName | CARDMEMBER_NAME | — | ✅ |
| 26 | CardPEOCompanyAccountId | COMPANY_ACCOUNT_ID | — | — |
| 27 | CardPEOCreatedBy | CREATED_BY | — | ✅ |
| 28 | CardPEOCreationDate | CREATION_DATE | — | ✅ |
| 29 | CardPEODescription | DESCRIPTION | — | ✅ |
| 30 | CardPEOInactiveDate | INACTIVE_DATE | — | ✅ |
| 31 | CardPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 32 | CardPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 33 | CardPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 34 | CardPEOLocationId | LOCATION_ID | — | — |
| 35 | CardPEOMaxPeriodAmount | MAX_PERIOD_AMOUNT | — | — |
| 36 | CardPEOMothersMaidenName | MOTHERS_MAIDEN_NAME | — | — |
| 37 | CardPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 38 | CardPEOPersonId | PERSON_ID | — | — |
| 39 | CardPEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 40 | CardPEOProgramName | PROGRAM_NAME | — | ✅ |
| 41 | CardPEORequestId | REQUEST_ID | — | — |
| 42 | CardPEOTrxLimitAmount | TRX_LIMIT_AMOUNT | — | — |

### [[exm_card_programs|EXM_CARD_PROGRAMS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CardProgramPEOCardProgramId | CARD_PROGRAM_ID | — | — |
| 2 | CardProgramPEOCardProgramName | CARD_PROGRAM_NAME | — | ✅ |
| 3 | CardProgramPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[exm_cc_company_accounts|EXM_CC_COMPANY_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CardCompanyAccountPEOCcCompanyAccountId | CC_COMPANY_ACCOUNT_ID | — | — |
| 2 | CardCompanyAccountPEOCompanyAccountName | COMPANY_ACCOUNT_NAME | — | ✅ |
| 3 | CardCompanyAccountPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | PersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | PersonCreatedByPersonId | PERSON_ID | — | — |
| 5 | PersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | PersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 7 | PersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | PersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | PersonUpdatedByPersonId | PERSON_ID | — | — |
| 10 | PersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserCreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | UserCreatedByPersonId | PERSON_ID | — | — |
| 3 | UserCreatedByUserGuid | USER_GUID | — | — |
| 4 | UserCreatedByUserId | USER_ID | — | — |
| 5 | UserCreatedByUsername | USERNAME | — | — |
| 6 | UserUpdatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | UserUpdatedByPersonId | PERSON_ID | — | — |
| 8 | UserUpdatedByUserGuid | USER_GUID | — | — |
| 9 | UserUpdatedByUserId | USER_ID | — | — |
| 10 | UserUpdatedByUsername | USERNAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
