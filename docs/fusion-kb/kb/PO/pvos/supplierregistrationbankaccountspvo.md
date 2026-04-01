---
id: DOC-PO-PVO-SupplierRegistrationBankAccountsPVO
doc_type: system-doc
title: "SupplierRegistrationBankAccountsPVO — PVO Purchasing"
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
  - SupplierRegistrationBankAccountsPVO
  - supplierregistrationbankaccountspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplierRegistrationBankAccountsPVO

## 📌 Visão Geral

Extrai as contas bancárias informadas durante o registro de novos fornecedores. Permite validação antecipada de dados bancários no processo de homologação e onboarding.

**Caminho:** `FscmTopModelAM.PrcPozPublicViewAM.SupplierRegistrationBankAccountsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 30 | 1 | 1 | 21 | 70% |

---

## 🔗 Tabelas Relacionadas

- [[poz_bi_supp_reg_bank_account_v|POZ_BI_SUPP_REG_BANK_ACCOUNT_V]] — 30 atributos (1 PKs, 21 BICC)

---

## ⚙️ Atributos

### [[poz_bi_supp_reg_bank_account_v|POZ_BI_SUPP_REG_BANK_ACCOUNT_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SecondaryAccountReference | SECONDARYACCOUNTREFERENCE | — | — |
| 2 | SupplierRegBankAccountAccountrequestid | ACCOUNTREQUESTID | — | — |
| 3 | SupplierRegBankAccountAccountsuffix | ACCOUNTSUFFIX | — | ✅ |
| 4 | SupplierRegBankAccountAgencylocationcode | AGENCYLOCATIONCODE | — | ✅ |
| 5 | SupplierRegBankAccountBank | BANK | — | ✅ |
| 6 | SupplierRegBankAccountBankaccountname | BANKACCOUNTNAME | — | ✅ |
| 7 | SupplierRegBankAccountBankaccountnamealt | BANKACCOUNTNAMEALT | — | ✅ |
| 8 | SupplierRegBankAccountBankaccountnum | BANKACCOUNTNUM | — | ✅ |
| 9 | SupplierRegBankAccountBankaccounttype | BANKACCOUNTTYPE | — | ✅ |
| 10 | SupplierRegBankAccountBankid | BANKID | — | — |
| 11 | SupplierRegBankAccountBanknumber | BANKNUMBER | — | ✅ |
| 12 | SupplierRegBankAccountBranch | BRANCH | — | ✅ |
| 13 | SupplierRegBankAccountBranchid | BRANCHID | — | — |
| 14 | SupplierRegBankAccountBranchnumber | BRANCHNUMBER | — | ✅ |
| 15 | SupplierRegBankAccountCheckdigits | CHECKDIGITS | — | ✅ |
| 16 | SupplierRegBankAccountCountry | COUNTRY | — | ✅ |
| 17 | SupplierRegBankAccountCountrycode | COUNTRYCODE | — | — |
| 18 | SupplierRegBankAccountCreatedby | CREATEDBY | — | ✅ |
| 19 | SupplierRegBankAccountCreationdate | CREATIONDATE | — | ✅ |
| 20 | SupplierRegBankAccountCurrency | CURRENCY | — | ✅ |
| 21 | SupplierRegBankAccountCurrencycode | CURRENCYCODE | — | — |
| 22 | SupplierRegBankAccountDescription | DESCRIPTION | — | ✅ |
| 23 | SupplierRegBankAccountIban | IBAN | — | ✅ |
| 24 | SupplierRegBankAccountLastupdatedate | LASTUPDATEDATE | — | ✅ |
| 25 | SupplierRegBankAccountLastupdatedby | LASTUPDATEDBY | — | ✅ |
| 26 | SupplierRegBankAccountLastupdatelogin | LASTUPDATELOGIN | — | — |
| 27 | SupplierRegBankAccountNote | NOTE | — | ✅ |
| 28 | SupplierRegBankAccountObjectversionnumber | OBJECTVERSIONNUMBER | — | — |
| 29 | SupplierRegBankAccountSupplierregid | SUPPLIERREGID | — | — |
| 30 | Tempextbankacctid | TEMPEXTBANKACCTID | 🔑 | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
