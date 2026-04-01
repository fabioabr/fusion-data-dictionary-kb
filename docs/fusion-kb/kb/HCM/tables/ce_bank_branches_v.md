---
id: DOC-HCM-067
doc_type: system-doc
title: "CE_BANK_BRANCHES_V — (título a preencher)"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - human-capital-management
  - data-dictionary
aliases:
  - CE_BANK_BRANCHES_V
  - ce_bank_branches_v
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# CE_BANK_BRANCHES_V

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ADDRESS_LINE1 | — | — | — | — | — | — |
| 2 | ADDRESS_LINE2 | — | — | — | — | — | — |
| 3 | ADDRESS_LINE3 | — | — | — | — | — | — |
| 4 | ADDRESS_LINE4 | — | — | — | — | — | — |
| 5 | BANK_BRANCH_NAME | — | — | — | — | — | — |
| 6 | BANK_BRANCH_NAME_ALT | — | — | — | — | — | — |
| 7 | BANK_BRANCH_TYPE | — | — | — | — | — | — |
| 8 | BANK_CODE | — | — | — | — | — | — |
| 9 | BANK_HOME_COUNTRY | — | — | — | — | — | — |
| 10 | BANK_INSTITUTION_TYPE | — | — | — | — | — | — |
| 11 | BANK_NAME | — | — | — | — | — | — |
| 12 | BANK_NAME_ALT | — | — | — | — | — | — |
| 13 | BANK_NUMBER | — | — | — | — | — | — |
| 14 | BANK_PARTY_ID | — | — | — | — | — | — |
| 15 | BRANCH_NUMBER | — | — | — | — | — | — |
| 16 | BRANCH_PARTY_ID | — | — | — | — | — | — |
| 17 | CITY | — | — | — | — | — | — |
| 18 | COUNTRY | — | — | — | — | — | — |
| 19 | COUNTRY_NAME | — | — | — | — | — | — |
| 20 | DESCRIPTION | — | — | — | — | — | — |
| 21 | EDI_ID_NUMBER | — | — | — | — | — | — |
| 22 | EDI_LOCATION | — | — | — | — | — | — |
| 23 | EFT_SWIFT_CODE | — | — | — | — | — | — |
| 24 | EFT_USER_NUMBER | — | — | — | — | — | — |
| 25 | END_DATE | — | — | — | — | — | — |
| 26 | PK_ID | — | — | — | — | — | — |
| 27 | PROVINCE | — | — | — | — | — | — |
| 28 | RFC | — | — | — | — | — | — |
| 29 | ROW_ID | — | — | — | — | — | — |
| 30 | SHORT_BANK_NAME | — | — | — | — | — | — |
| 31 | START_DATE | — | — | — | — | — | — |
| 32 | STATE | — | — | — | — | — | — |
| 33 | ZIP | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[bankaccountpvo|BankAccountPVO]] (OTHER · BICC: 1/33)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDRESS_LINE1 | BankBranchAddressLine1 | — |
| ADDRESS_LINE2 | BankBranchAddressLine2 | — |
| ADDRESS_LINE3 | BankBranchAddressLine3 | — |
| ADDRESS_LINE4 | BankBranchAddressLine4 | — |
| BANK_BRANCH_NAME | BankBranchBankBranchName | ✅ |
| BANK_BRANCH_NAME_ALT | BankBranchBankBranchNameAlt | — |
| BANK_BRANCH_TYPE | BankBranchBankBranchType | — |
| BANK_CODE | BankBranchBankCode | — |
| BANK_HOME_COUNTRY | BankBranchBankHomeCountry | — |
| BANK_INSTITUTION_TYPE | BankBranchBankInstitutionType | — |
| BANK_NAME | BankBranchBankName | — |
| BANK_NAME_ALT | BankBranchBankNameAlt | — |
| BANK_NUMBER | BankBranchBankNumber | — |
| BANK_PARTY_ID | BankBranchBankPartyId | — |
| BRANCH_NUMBER | BankBranchBranchNumber | — |
| BRANCH_PARTY_ID | BankBranchBranchPartyId | — |
| CITY | BankBranchCity | — |
| COUNTRY | BankBranchCountry | — |
| COUNTRY_NAME | BankBranchCountryName | — |
| DESCRIPTION | BankBranchDescription | — |
| EDI_ID_NUMBER | BankBranchEdiIdNumber | — |
| EDI_LOCATION | BankBranchEdiLocation | — |
| EFT_SWIFT_CODE | BankBranchEftSwiftCode | — |
| EFT_USER_NUMBER | BankBranchEftUserNumber | — |
| END_DATE | BankBranchEndDate | — |
| PK_ID | BankBranchPkId | — |
| PROVINCE | BankBranchProvince | — |
| RFC | BankBranchRfc | — |
| ROW_ID | BankBranchRowId | — |
| SHORT_BANK_NAME | BankBranchShortBankName | — |
| START_DATE | BankBranchStartDate | — |
| STATE | BankBranchState | — |
| ZIP | BankBranchZip | — |

### [[miscreceiptdistributionpvo|MiscReceiptDistributionPVO]] (AR · BICC: 1/132)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDRESS_LINE1 | CustomerBankBranchAddressLine1 | — |
| ADDRESS_LINE1 | IssuerBankBranchAddressLine1 | — |
| ADDRESS_LINE1 | OldCustomerBankBranchAddressLine1 | — |
| ADDRESS_LINE1 | OldIssuerBankBranchAddressLine1 | — |
| ADDRESS_LINE2 | CustomerBankBranchAddressLine2 | — |
| ADDRESS_LINE2 | IssuerBankBranchAddressLine2 | — |
| ADDRESS_LINE2 | OldCustomerBankBranchAddressLine2 | — |
| ADDRESS_LINE2 | OldIssuerBankBranchAddressLine2 | — |
| ADDRESS_LINE3 | CustomerBankBranchAddressLine3 | — |
| ADDRESS_LINE3 | IssuerBankBranchAddressLine3 | — |
| ADDRESS_LINE3 | OldCustomerBankBranchAddressLine3 | — |
| ADDRESS_LINE3 | OldIssuerBankBranchAddressLine3 | — |
| ADDRESS_LINE4 | CustomerBankBranchAddressLine4 | — |
| ADDRESS_LINE4 | IssuerBankBranchAddressLine4 | — |
| ADDRESS_LINE4 | OldCustomerBankBranchAddressLine4 | — |
| ADDRESS_LINE4 | OldIssuerBankBranchAddressLine4 | — |
| BANK_BRANCH_NAME | CustomerBankBranchBankBranchName | ✅ |
| BANK_BRANCH_NAME | IssuerBankBranchBankBranchName | — |
| BANK_BRANCH_NAME | OldCustomerBankBranchBankBranchName | — |
| BANK_BRANCH_NAME | OldIssuerBankBranchBankBranchName | — |
| BANK_BRANCH_NAME_ALT | CustomerBankBranchBankBranchNameAlt | — |
| BANK_BRANCH_NAME_ALT | IssuerBankBranchBankBranchNameAlt | — |
| BANK_BRANCH_NAME_ALT | OldCustomerBankBranchBankBranchNameAlt | — |
| BANK_BRANCH_NAME_ALT | OldIssuerBankBranchBankBranchNameAlt | — |
| BANK_BRANCH_TYPE | CustomerBankBranchBankBranchType | — |
| BANK_BRANCH_TYPE | IssuerBankBranchBankBranchType | — |
| BANK_BRANCH_TYPE | OldCustomerBankBranchBankBranchType | — |
| BANK_BRANCH_TYPE | OldIssuerBankBranchBankBranchType | — |
| BANK_CODE | CustomerBankBranchBankCode | — |
| BANK_CODE | IssuerBankBranchBankCode | — |
| BANK_CODE | OldCustomerBankBranchBankCode | — |
| BANK_CODE | OldIssuerBankBranchBankCode | — |
| BANK_HOME_COUNTRY | CustomerBankBranchBankHomeCountry | — |
| BANK_HOME_COUNTRY | IssuerBankBranchBankHomeCountry | — |
| BANK_HOME_COUNTRY | OldCustomerBankBranchBankHomeCountry | — |
| BANK_HOME_COUNTRY | OldIssuerBankBranchBankHomeCountry | — |
| BANK_INSTITUTION_TYPE | CustomerBankBranchBankInstitutionType | — |
| BANK_INSTITUTION_TYPE | IssuerBankBranchBankInstitutionType | — |
| BANK_INSTITUTION_TYPE | OldCustomerBankBranchBankInstitutionType | — |
| BANK_INSTITUTION_TYPE | OldIssuerBankBranchBankInstitutionType | — |
| BANK_NAME | CustomerBankBranchBankName | — |
| BANK_NAME | IssuerBankBranchBankName | — |
| BANK_NAME | OldCustomerBankBranchBankName | — |
| BANK_NAME | OldIssuerBankBranchBankName | — |
| BANK_NAME_ALT | CustomerBankBranchBankNameAlt | — |
| BANK_NAME_ALT | IssuerBankBranchBankNameAlt | — |
| BANK_NAME_ALT | OldCustomerBankBranchBankNameAlt | — |
| BANK_NAME_ALT | OldIssuerBankBranchBankNameAlt | — |
| BANK_NUMBER | CustomerBankBranchBankNumber | — |
| BANK_NUMBER | IssuerBankBranchBankNumber | — |
| BANK_NUMBER | OldCustomerBankBranchBankNumber | — |
| BANK_NUMBER | OldIssuerBankBranchBankNumber | — |
| BANK_PARTY_ID | CustomerBankBranchBankPartyId | — |
| BANK_PARTY_ID | IssuerBankBranchBankPartyId | — |
| BANK_PARTY_ID | OldCustomerBankBranchBankPartyId | — |
| BANK_PARTY_ID | OldIssuerBankBranchBankPartyId | — |
| BRANCH_NUMBER | CustomerBankBranchBranchNumber | — |
| BRANCH_NUMBER | IssuerBankBranchBranchNumber | — |
| BRANCH_NUMBER | OldCustomerBankBranchBranchNumber | — |
| BRANCH_NUMBER | OldIssuerBankBranchBranchNumber | — |
| BRANCH_PARTY_ID | CustomerBankBranchBranchPartyId | — |
| BRANCH_PARTY_ID | IssuerBankBranchBranchPartyId | — |
| BRANCH_PARTY_ID | OldCustomerBankBranchBranchPartyId | — |
| BRANCH_PARTY_ID | OldIssuerBankBranchBranchPartyId | — |
| CITY | CustomerBankBranchCity | — |
| CITY | IssuerBankBranchCity | — |
| CITY | OldCustomerBankBranchCity | — |
| CITY | OldIssuerBankBranchCity | — |
| COUNTRY | CustomerBankBranchCountry | — |
| COUNTRY | IssuerBankBranchCountry | — |
| COUNTRY | OldCustomerBankBranchCountry | — |
| COUNTRY | OldIssuerBankBranchCountry | — |
| COUNTRY_NAME | CustomerBankBranchCountryName | — |
| COUNTRY_NAME | IssuerBankBranchCountryName | — |
| COUNTRY_NAME | OldCustomerBankBranchCountryName | — |
| COUNTRY_NAME | OldIssuerBankBranchCountryName | — |
| DESCRIPTION | CustomerBankBranchDescription | — |
| DESCRIPTION | IssuerBankBranchDescription | — |
| DESCRIPTION | OldCustomerBankBranchDescription | — |
| DESCRIPTION | OldIssuerBankBranchDescription | — |
| EDI_ID_NUMBER | CustomerBankBranchEdiIdNumber | — |
| EDI_ID_NUMBER | IssuerBankBranchEdiIdNumber | — |
| EDI_ID_NUMBER | OldCustomerBankBranchEdiIdNumber | — |
| EDI_ID_NUMBER | OldIssuerBankBranchEdiIdNumber | — |
| EDI_LOCATION | CustomerBankBranchEdiLocation | — |
| EDI_LOCATION | IssuerBankBranchEdiLocation | — |
| EDI_LOCATION | OldCustomerBankBranchEdiLocation | — |
| EDI_LOCATION | OldIssuerBankBranchEdiLocation | — |
| EFT_SWIFT_CODE | CustomerBankBranchEftSwiftCode | — |
| EFT_SWIFT_CODE | IssuerBankBranchEftSwiftCode | — |
| EFT_SWIFT_CODE | OldCustomerBankBranchEftSwiftCode | — |
| EFT_SWIFT_CODE | OldIssuerBankBranchEftSwiftCode | — |
| EFT_USER_NUMBER | CustomerBankBranchEftUserNumber | — |
| EFT_USER_NUMBER | IssuerBankBranchEftUserNumber | — |
| EFT_USER_NUMBER | OldCustomerBankBranchEftUserNumber | — |
| EFT_USER_NUMBER | OldIssuerBankBranchEftUserNumber | — |
| END_DATE | CustomerBankBranchEndDate | — |
| END_DATE | IssuerBankBranchEndDate | — |
| END_DATE | OldCustomerBankBranchEndDate | — |
| END_DATE | OldIssuerBankBranchEndDate | — |
| PK_ID | CustomerBankBranchPkId | — |
| PK_ID | IssuerBankBranchPkId | — |
| PK_ID | OldCustomerBankBranchPkId | — |
| PK_ID | OldIssuerBankBranchPkId | — |
| PROVINCE | CustomerBankBranchProvince | — |
| PROVINCE | IssuerBankBranchProvince | — |
| PROVINCE | OldCustomerBankBranchProvince | — |
| PROVINCE | OldIssuerBankBranchProvince | — |
| RFC | CustomerBankBranchRfc | — |
| RFC | IssuerBankBranchRfc | — |
| RFC | OldCustomerBankBranchRfc | — |
| RFC | OldIssuerBankBranchRfc | — |
| ROW_ID | CustomerBankBranchRowId | — |
| ROW_ID | IssuerBankBranchRowId | — |
| ROW_ID | OldCustomerBankBranchRowId | — |
| ROW_ID | OldIssuerBankBranchRowId | — |
| SHORT_BANK_NAME | CustomerBankBranchShortBankName | — |
| SHORT_BANK_NAME | IssuerBankBranchShortBankName | — |
| SHORT_BANK_NAME | OldCustomerBankBranchShortBankName | — |
| SHORT_BANK_NAME | OldIssuerBankBranchShortBankName | — |
| START_DATE | CustomerBankBranchStartDate | — |
| START_DATE | IssuerBankBranchStartDate | — |
| START_DATE | OldCustomerBankBranchStartDate | — |
| START_DATE | OldIssuerBankBranchStartDate | — |
| STATE | CustomerBankBranchState | — |
| STATE | IssuerBankBranchState | — |
| STATE | OldCustomerBankBranchState | — |
| STATE | OldIssuerBankBranchState | — |
| ZIP | CustomerBankBranchZip | — |
| ZIP | IssuerBankBranchZip | — |
| ZIP | OldCustomerBankBranchZip | — |
| ZIP | OldIssuerBankBranchZip | — |

### [[receiptapplicationdistributionpvo|ReceiptApplicationDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDRESS_LINE1 | CustomerBankBranchAddressLine1 | — |
| ADDRESS_LINE1 | IssuerBankBranchAddressLine1 | — |
| ADDRESS_LINE1 | OldCustomerBankBranchAddressLine1 | — |
| ADDRESS_LINE1 | OldIssuerBankBranchAddressLine1 | — |
| ADDRESS_LINE2 | CustomerBankBranchAddressLine2 | — |
| ADDRESS_LINE2 | IssuerBankBranchAddressLine2 | — |
| ADDRESS_LINE2 | OldCustomerBankBranchAddressLine2 | — |
| ADDRESS_LINE2 | OldIssuerBankBranchAddressLine2 | — |
| ADDRESS_LINE3 | CustomerBankBranchAddressLine3 | — |
| ADDRESS_LINE3 | IssuerBankBranchAddressLine3 | — |
| ADDRESS_LINE3 | OldCustomerBankBranchAddressLine3 | — |
| ADDRESS_LINE3 | OldIssuerBankBranchAddressLine3 | — |
| ADDRESS_LINE4 | CustomerBankBranchAddressLine4 | — |
| ADDRESS_LINE4 | IssuerBankBranchAddressLine4 | — |
| ADDRESS_LINE4 | OldCustomerBankBranchAddressLine4 | — |
| ADDRESS_LINE4 | OldIssuerBankBranchAddressLine4 | — |
| BANK_BRANCH_NAME | CustomerBankBranchBankBranchName | — |
| BANK_BRANCH_NAME | IssuerBankBranchBankBranchName | — |
| BANK_BRANCH_NAME | OldCustomerBankBranchBankBranchName | — |
| BANK_BRANCH_NAME | OldIssuerBankBranchBankBranchName | — |
| BANK_BRANCH_NAME_ALT | CustomerBankBranchBankBranchNameAlt | — |
| BANK_BRANCH_NAME_ALT | IssuerBankBranchBankBranchNameAlt | — |
| BANK_BRANCH_NAME_ALT | OldCustomerBankBranchBankBranchNameAlt | — |
| BANK_BRANCH_NAME_ALT | OldIssuerBankBranchBankBranchNameAlt | — |
| BANK_BRANCH_TYPE | CustomerBankBranchBankBranchType | — |
| BANK_BRANCH_TYPE | IssuerBankBranchBankBranchType | — |
| BANK_BRANCH_TYPE | OldCustomerBankBranchBankBranchType | — |
| BANK_BRANCH_TYPE | OldIssuerBankBranchBankBranchType | — |
| BANK_CODE | CustomerBankBranchBankCode | — |
| BANK_CODE | IssuerBankBranchBankCode | — |
| BANK_CODE | OldCustomerBankBranchBankCode | — |
| BANK_CODE | OldIssuerBankBranchBankCode | — |
| BANK_HOME_COUNTRY | CustomerBankBranchBankHomeCountry | — |
| BANK_HOME_COUNTRY | IssuerBankBranchBankHomeCountry | — |
| BANK_HOME_COUNTRY | OldCustomerBankBranchBankHomeCountry | — |
| BANK_HOME_COUNTRY | OldIssuerBankBranchBankHomeCountry | — |
| BANK_INSTITUTION_TYPE | CustomerBankBranchBankInstitutionType | — |
| BANK_INSTITUTION_TYPE | IssuerBankBranchBankInstitutionType | — |
| BANK_INSTITUTION_TYPE | OldCustomerBankBranchBankInstitutionType | — |
| BANK_INSTITUTION_TYPE | OldIssuerBankBranchBankInstitutionType | — |
| BANK_NAME | CustomerBankBranchBankName | — |
| BANK_NAME | IssuerBankBranchBankName | — |
| BANK_NAME | OldCustomerBankBranchBankName | — |
| BANK_NAME | OldIssuerBankBranchBankName | — |
| BANK_NAME_ALT | CustomerBankBranchBankNameAlt | — |
| BANK_NAME_ALT | IssuerBankBranchBankNameAlt | — |
| BANK_NAME_ALT | OldCustomerBankBranchBankNameAlt | — |
| BANK_NAME_ALT | OldIssuerBankBranchBankNameAlt | — |
| BANK_NUMBER | CustomerBankBranchBankNumber | — |
| BANK_NUMBER | IssuerBankBranchBankNumber | — |
| BANK_NUMBER | OldCustomerBankBranchBankNumber | — |
| BANK_NUMBER | OldIssuerBankBranchBankNumber | — |
| BANK_PARTY_ID | CustomerBankBranchBankPartyId | — |
| BANK_PARTY_ID | IssuerBankBranchBankPartyId | — |
| BANK_PARTY_ID | OldCustomerBankBranchBankPartyId | — |
| BANK_PARTY_ID | OldIssuerBankBranchBankPartyId | — |
| BRANCH_NUMBER | CustomerBankBranchBranchNumber | — |
| BRANCH_NUMBER | IssuerBankBranchBranchNumber | — |
| BRANCH_NUMBER | OldCustomerBankBranchBranchNumber | — |
| BRANCH_NUMBER | OldIssuerBankBranchBranchNumber | — |
| BRANCH_PARTY_ID | CustomerBankBranchBranchPartyId | — |
| BRANCH_PARTY_ID | IssuerBankBranchBranchPartyId | — |
| BRANCH_PARTY_ID | OldCustomerBankBranchBranchPartyId | — |
| BRANCH_PARTY_ID | OldIssuerBankBranchBranchPartyId | — |
| CITY | CustomerBankBranchCity | — |
| CITY | IssuerBankBranchCity | — |
| CITY | OldCustomerBankBranchCity | — |
| CITY | OldIssuerBankBranchCity | — |
| COUNTRY | CustomerBankBranchCountry | — |
| COUNTRY | IssuerBankBranchCountry | — |
| COUNTRY | OldCustomerBankBranchCountry | — |
| COUNTRY | OldIssuerBankBranchCountry | — |
| COUNTRY_NAME | CustomerBankBranchCountryName | — |
| COUNTRY_NAME | IssuerBankBranchCountryName | — |
| COUNTRY_NAME | OldCustomerBankBranchCountryName | — |
| COUNTRY_NAME | OldIssuerBankBranchCountryName | — |
| DESCRIPTION | CustomerBankBranchDescription | — |
| DESCRIPTION | IssuerBankBranchDescription | — |
| DESCRIPTION | OldCustomerBankBranchDescription | — |
| DESCRIPTION | OldIssuerBankBranchDescription | — |
| EDI_ID_NUMBER | CustomerBankBranchEdiIdNumber | — |
| EDI_ID_NUMBER | IssuerBankBranchEdiIdNumber | — |
| EDI_ID_NUMBER | OldCustomerBankBranchEdiIdNumber | — |
| EDI_ID_NUMBER | OldIssuerBankBranchEdiIdNumber | — |
| EDI_LOCATION | CustomerBankBranchEdiLocation | — |
| EDI_LOCATION | IssuerBankBranchEdiLocation | — |
| EDI_LOCATION | OldCustomerBankBranchEdiLocation | — |
| EDI_LOCATION | OldIssuerBankBranchEdiLocation | — |
| EFT_SWIFT_CODE | CustomerBankBranchEftSwiftCode | — |
| EFT_SWIFT_CODE | IssuerBankBranchEftSwiftCode | — |
| EFT_SWIFT_CODE | OldCustomerBankBranchEftSwiftCode | — |
| EFT_SWIFT_CODE | OldIssuerBankBranchEftSwiftCode | — |
| EFT_USER_NUMBER | CustomerBankBranchEftUserNumber | — |
| EFT_USER_NUMBER | IssuerBankBranchEftUserNumber | — |
| EFT_USER_NUMBER | OldCustomerBankBranchEftUserNumber | — |
| EFT_USER_NUMBER | OldIssuerBankBranchEftUserNumber | — |
| END_DATE | CustomerBankBranchEndDate | — |
| END_DATE | IssuerBankBranchEndDate | — |
| END_DATE | OldCustomerBankBranchEndDate | — |
| END_DATE | OldIssuerBankBranchEndDate | — |
| PK_ID | CustomerBankBranchPkId | — |
| PK_ID | IssuerBankBranchPkId | — |
| PK_ID | OldCustomerBankBranchPkId | — |
| PK_ID | OldIssuerBankBranchPkId | — |
| PROVINCE | CustomerBankBranchProvince | — |
| PROVINCE | IssuerBankBranchProvince | — |
| PROVINCE | OldCustomerBankBranchProvince | — |
| PROVINCE | OldIssuerBankBranchProvince | — |
| RFC | CustomerBankBranchRfc | — |
| RFC | IssuerBankBranchRfc | — |
| RFC | OldCustomerBankBranchRfc | — |
| RFC | OldIssuerBankBranchRfc | — |
| ROW_ID | CustomerBankBranchRowId | — |
| ROW_ID | IssuerBankBranchRowId | — |
| ROW_ID | OldCustomerBankBranchRowId | — |
| ROW_ID | OldIssuerBankBranchRowId | — |
| SHORT_BANK_NAME | CustomerBankBranchShortBankName | — |
| SHORT_BANK_NAME | IssuerBankBranchShortBankName | — |
| SHORT_BANK_NAME | OldCustomerBankBranchShortBankName | — |
| SHORT_BANK_NAME | OldIssuerBankBranchShortBankName | — |
| START_DATE | CustomerBankBranchStartDate | — |
| START_DATE | IssuerBankBranchStartDate | — |
| START_DATE | OldCustomerBankBranchStartDate | — |
| START_DATE | OldIssuerBankBranchStartDate | — |
| STATE | CustomerBankBranchState | — |
| STATE | IssuerBankBranchState | — |
| STATE | OldCustomerBankBranchState | — |
| STATE | OldIssuerBankBranchState | — |
| ZIP | CustomerBankBranchZip | — |
| ZIP | IssuerBankBranchZip | — |
| ZIP | OldCustomerBankBranchZip | — |
| ZIP | OldIssuerBankBranchZip | — |

### [[receiptapplicationdistributionvc|ReceiptApplicationDistributionVC]] (AR · BICC: 1/132)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDRESS_LINE1 | CustomerBankBranchAddressLine1 | — |
| ADDRESS_LINE1 | IssuerBankBranchAddressLine1 | — |
| ADDRESS_LINE1 | OldCustomerBankBranchAddressLine1 | — |
| ADDRESS_LINE1 | OldIssuerBankBranchAddressLine1 | — |
| ADDRESS_LINE2 | CustomerBankBranchAddressLine2 | — |
| ADDRESS_LINE2 | IssuerBankBranchAddressLine2 | — |
| ADDRESS_LINE2 | OldCustomerBankBranchAddressLine2 | — |
| ADDRESS_LINE2 | OldIssuerBankBranchAddressLine2 | — |
| ADDRESS_LINE3 | CustomerBankBranchAddressLine3 | — |
| ADDRESS_LINE3 | IssuerBankBranchAddressLine3 | — |
| ADDRESS_LINE3 | OldCustomerBankBranchAddressLine3 | — |
| ADDRESS_LINE3 | OldIssuerBankBranchAddressLine3 | — |
| ADDRESS_LINE4 | CustomerBankBranchAddressLine4 | — |
| ADDRESS_LINE4 | IssuerBankBranchAddressLine4 | — |
| ADDRESS_LINE4 | OldCustomerBankBranchAddressLine4 | — |
| ADDRESS_LINE4 | OldIssuerBankBranchAddressLine4 | — |
| BANK_BRANCH_NAME | CustomerBankBranchBankBranchName | ✅ |
| BANK_BRANCH_NAME | IssuerBankBranchBankBranchName | — |
| BANK_BRANCH_NAME | OldCustomerBankBranchBankBranchName | — |
| BANK_BRANCH_NAME | OldIssuerBankBranchBankBranchName | — |
| BANK_BRANCH_NAME_ALT | CustomerBankBranchBankBranchNameAlt | — |
| BANK_BRANCH_NAME_ALT | IssuerBankBranchBankBranchNameAlt | — |
| BANK_BRANCH_NAME_ALT | OldCustomerBankBranchBankBranchNameAlt | — |
| BANK_BRANCH_NAME_ALT | OldIssuerBankBranchBankBranchNameAlt | — |
| BANK_BRANCH_TYPE | CustomerBankBranchBankBranchType | — |
| BANK_BRANCH_TYPE | IssuerBankBranchBankBranchType | — |
| BANK_BRANCH_TYPE | OldCustomerBankBranchBankBranchType | — |
| BANK_BRANCH_TYPE | OldIssuerBankBranchBankBranchType | — |
| BANK_CODE | CustomerBankBranchBankCode | — |
| BANK_CODE | IssuerBankBranchBankCode | — |
| BANK_CODE | OldCustomerBankBranchBankCode | — |
| BANK_CODE | OldIssuerBankBranchBankCode | — |
| BANK_HOME_COUNTRY | CustomerBankBranchBankHomeCountry | — |
| BANK_HOME_COUNTRY | IssuerBankBranchBankHomeCountry | — |
| BANK_HOME_COUNTRY | OldCustomerBankBranchBankHomeCountry | — |
| BANK_HOME_COUNTRY | OldIssuerBankBranchBankHomeCountry | — |
| BANK_INSTITUTION_TYPE | CustomerBankBranchBankInstitutionType | — |
| BANK_INSTITUTION_TYPE | IssuerBankBranchBankInstitutionType | — |
| BANK_INSTITUTION_TYPE | OldCustomerBankBranchBankInstitutionType | — |
| BANK_INSTITUTION_TYPE | OldIssuerBankBranchBankInstitutionType | — |
| BANK_NAME | CustomerBankBranchBankName | — |
| BANK_NAME | IssuerBankBranchBankName | — |
| BANK_NAME | OldCustomerBankBranchBankName | — |
| BANK_NAME | OldIssuerBankBranchBankName | — |
| BANK_NAME_ALT | CustomerBankBranchBankNameAlt | — |
| BANK_NAME_ALT | IssuerBankBranchBankNameAlt | — |
| BANK_NAME_ALT | OldCustomerBankBranchBankNameAlt | — |
| BANK_NAME_ALT | OldIssuerBankBranchBankNameAlt | — |
| BANK_NUMBER | CustomerBankBranchBankNumber | — |
| BANK_NUMBER | IssuerBankBranchBankNumber | — |
| BANK_NUMBER | OldCustomerBankBranchBankNumber | — |
| BANK_NUMBER | OldIssuerBankBranchBankNumber | — |
| BANK_PARTY_ID | CustomerBankBranchBankPartyId | — |
| BANK_PARTY_ID | IssuerBankBranchBankPartyId | — |
| BANK_PARTY_ID | OldCustomerBankBranchBankPartyId | — |
| BANK_PARTY_ID | OldIssuerBankBranchBankPartyId | — |
| BRANCH_NUMBER | CustomerBankBranchBranchNumber | — |
| BRANCH_NUMBER | IssuerBankBranchBranchNumber | — |
| BRANCH_NUMBER | OldCustomerBankBranchBranchNumber | — |
| BRANCH_NUMBER | OldIssuerBankBranchBranchNumber | — |
| BRANCH_PARTY_ID | CustomerBankBranchBranchPartyId | — |
| BRANCH_PARTY_ID | IssuerBankBranchBranchPartyId | — |
| BRANCH_PARTY_ID | OldCustomerBankBranchBranchPartyId | — |
| BRANCH_PARTY_ID | OldIssuerBankBranchBranchPartyId | — |
| CITY | CustomerBankBranchCity | — |
| CITY | IssuerBankBranchCity | — |
| CITY | OldCustomerBankBranchCity | — |
| CITY | OldIssuerBankBranchCity | — |
| COUNTRY | CustomerBankBranchCountry | — |
| COUNTRY | IssuerBankBranchCountry | — |
| COUNTRY | OldCustomerBankBranchCountry | — |
| COUNTRY | OldIssuerBankBranchCountry | — |
| COUNTRY_NAME | CustomerBankBranchCountryName | — |
| COUNTRY_NAME | IssuerBankBranchCountryName | — |
| COUNTRY_NAME | OldCustomerBankBranchCountryName | — |
| COUNTRY_NAME | OldIssuerBankBranchCountryName | — |
| DESCRIPTION | CustomerBankBranchDescription | — |
| DESCRIPTION | IssuerBankBranchDescription | — |
| DESCRIPTION | OldCustomerBankBranchDescription | — |
| DESCRIPTION | OldIssuerBankBranchDescription | — |
| EDI_ID_NUMBER | CustomerBankBranchEdiIdNumber | — |
| EDI_ID_NUMBER | IssuerBankBranchEdiIdNumber | — |
| EDI_ID_NUMBER | OldCustomerBankBranchEdiIdNumber | — |
| EDI_ID_NUMBER | OldIssuerBankBranchEdiIdNumber | — |
| EDI_LOCATION | CustomerBankBranchEdiLocation | — |
| EDI_LOCATION | IssuerBankBranchEdiLocation | — |
| EDI_LOCATION | OldCustomerBankBranchEdiLocation | — |
| EDI_LOCATION | OldIssuerBankBranchEdiLocation | — |
| EFT_SWIFT_CODE | CustomerBankBranchEftSwiftCode | — |
| EFT_SWIFT_CODE | IssuerBankBranchEftSwiftCode | — |
| EFT_SWIFT_CODE | OldCustomerBankBranchEftSwiftCode | — |
| EFT_SWIFT_CODE | OldIssuerBankBranchEftSwiftCode | — |
| EFT_USER_NUMBER | CustomerBankBranchEftUserNumber | — |
| EFT_USER_NUMBER | IssuerBankBranchEftUserNumber | — |
| EFT_USER_NUMBER | OldCustomerBankBranchEftUserNumber | — |
| EFT_USER_NUMBER | OldIssuerBankBranchEftUserNumber | — |
| END_DATE | CustomerBankBranchEndDate | — |
| END_DATE | IssuerBankBranchEndDate | — |
| END_DATE | OldCustomerBankBranchEndDate | — |
| END_DATE | OldIssuerBankBranchEndDate | — |
| PK_ID | CustomerBankBranchPkId | — |
| PK_ID | IssuerBankBranchPkId | — |
| PK_ID | OldCustomerBankBranchPkId | — |
| PK_ID | OldIssuerBankBranchPkId | — |
| PROVINCE | CustomerBankBranchProvince | — |
| PROVINCE | IssuerBankBranchProvince | — |
| PROVINCE | OldCustomerBankBranchProvince | — |
| PROVINCE | OldIssuerBankBranchProvince | — |
| RFC | CustomerBankBranchRfc | — |
| RFC | IssuerBankBranchRfc | — |
| RFC | OldCustomerBankBranchRfc | — |
| RFC | OldIssuerBankBranchRfc | — |
| ROW_ID | CustomerBankBranchRowId | — |
| ROW_ID | IssuerBankBranchRowId | — |
| ROW_ID | OldCustomerBankBranchRowId | — |
| ROW_ID | OldIssuerBankBranchRowId | — |
| SHORT_BANK_NAME | CustomerBankBranchShortBankName | — |
| SHORT_BANK_NAME | IssuerBankBranchShortBankName | — |
| SHORT_BANK_NAME | OldCustomerBankBranchShortBankName | — |
| SHORT_BANK_NAME | OldIssuerBankBranchShortBankName | — |
| START_DATE | CustomerBankBranchStartDate | — |
| START_DATE | IssuerBankBranchStartDate | — |
| START_DATE | OldCustomerBankBranchStartDate | — |
| START_DATE | OldIssuerBankBranchStartDate | — |
| STATE | CustomerBankBranchState | — |
| STATE | IssuerBankBranchState | — |
| STATE | OldCustomerBankBranchState | — |
| STATE | OldIssuerBankBranchState | — |
| ZIP | CustomerBankBranchZip | — |
| ZIP | IssuerBankBranchZip | — |
| ZIP | OldCustomerBankBranchZip | — |
| ZIP | OldIssuerBankBranchZip | — |

### [[receiptapplicationpvo|ReceiptApplicationPVO]] (AR · BICC: 1/33)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDRESS_LINE1 | BankBranchAddressLine1 | — |
| ADDRESS_LINE2 | BankBranchAddressLine2 | — |
| ADDRESS_LINE3 | BankBranchAddressLine3 | — |
| ADDRESS_LINE4 | BankBranchAddressLine4 | — |
| BANK_BRANCH_NAME | BankBranchBankBranchName | ✅ |
| BANK_BRANCH_NAME_ALT | BankBranchBankBranchNameAlt | — |
| BANK_BRANCH_TYPE | BankBranchBankBranchType | — |
| BANK_CODE | BankBranchBankCode | — |
| BANK_HOME_COUNTRY | BankBranchBankHomeCountry | — |
| BANK_INSTITUTION_TYPE | BankBranchBankInstitutionType | — |
| BANK_NAME | BankBranchBankName | — |
| BANK_NAME_ALT | BankBranchBankNameAlt | — |
| BANK_NUMBER | BankBranchBankNumber | — |
| BANK_PARTY_ID | BankBranchBankPartyId | — |
| BRANCH_NUMBER | BankBranchBranchNumber | — |
| BRANCH_PARTY_ID | BankBranchBranchPartyId | — |
| CITY | BankBranchCity | — |
| COUNTRY | BankBranchCountry | — |
| COUNTRY_NAME | BankBranchCountryName | — |
| DESCRIPTION | BankBranchDescription | — |
| EDI_ID_NUMBER | BankBranchEdiIdNumber | — |
| EDI_LOCATION | BankBranchEdiLocation | — |
| EFT_SWIFT_CODE | BankBranchEftSwiftCode | — |
| EFT_USER_NUMBER | BankBranchEftUserNumber | — |
| END_DATE | BankBranchEndDate | — |
| PK_ID | BankBranchPkId | — |
| PROVINCE | BankBranchProvince | — |
| RFC | BankBranchRfc | — |
| ROW_ID | BankBranchRowId | — |
| SHORT_BANK_NAME | BankBranchShortBankName | — |
| START_DATE | BankBranchStartDate | — |
| STATE | BankBranchState | — |
| ZIP | BankBranchZip | — |

### [[receiptheaderpvo|ReceiptHeaderPVO]] (AR · BICC: 1/132)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDRESS_LINE1 | CustomerBankBranchAddressLine1 | — |
| ADDRESS_LINE1 | IssuerBankBranchAddressLine1 | — |
| ADDRESS_LINE1 | OldCustomerBankBranchAddressLine1 | — |
| ADDRESS_LINE1 | OldIssuerBankBranchAddressLine1 | — |
| ADDRESS_LINE2 | CustomerBankBranchAddressLine2 | — |
| ADDRESS_LINE2 | IssuerBankBranchAddressLine2 | — |
| ADDRESS_LINE2 | OldCustomerBankBranchAddressLine2 | — |
| ADDRESS_LINE2 | OldIssuerBankBranchAddressLine2 | — |
| ADDRESS_LINE3 | CustomerBankBranchAddressLine3 | — |
| ADDRESS_LINE3 | IssuerBankBranchAddressLine3 | — |
| ADDRESS_LINE3 | OldCustomerBankBranchAddressLine3 | — |
| ADDRESS_LINE3 | OldIssuerBankBranchAddressLine3 | — |
| ADDRESS_LINE4 | CustomerBankBranchAddressLine4 | — |
| ADDRESS_LINE4 | IssuerBankBranchAddressLine4 | — |
| ADDRESS_LINE4 | OldCustomerBankBranchAddressLine4 | — |
| ADDRESS_LINE4 | OldIssuerBankBranchAddressLine4 | — |
| BANK_BRANCH_NAME | CustomerBankBranchBankBranchName | ✅ |
| BANK_BRANCH_NAME | IssuerBankBranchBankBranchName | — |
| BANK_BRANCH_NAME | OldCustomerBankBranchBankBranchName | — |
| BANK_BRANCH_NAME | OldIssuerBankBranchBankBranchName | — |
| BANK_BRANCH_NAME_ALT | CustomerBankBranchBankBranchNameAlt | — |
| BANK_BRANCH_NAME_ALT | IssuerBankBranchBankBranchNameAlt | — |
| BANK_BRANCH_NAME_ALT | OldCustomerBankBranchBankBranchNameAlt | — |
| BANK_BRANCH_NAME_ALT | OldIssuerBankBranchBankBranchNameAlt | — |
| BANK_BRANCH_TYPE | CustomerBankBranchBankBranchType | — |
| BANK_BRANCH_TYPE | IssuerBankBranchBankBranchType | — |
| BANK_BRANCH_TYPE | OldCustomerBankBranchBankBranchType | — |
| BANK_BRANCH_TYPE | OldIssuerBankBranchBankBranchType | — |
| BANK_CODE | CustomerBankBranchBankCode | — |
| BANK_CODE | IssuerBankBranchBankCode | — |
| BANK_CODE | OldCustomerBankBranchBankCode | — |
| BANK_CODE | OldIssuerBankBranchBankCode | — |
| BANK_HOME_COUNTRY | CustomerBankBranchBankHomeCountry | — |
| BANK_HOME_COUNTRY | IssuerBankBranchBankHomeCountry | — |
| BANK_HOME_COUNTRY | OldCustomerBankBranchBankHomeCountry | — |
| BANK_HOME_COUNTRY | OldIssuerBankBranchBankHomeCountry | — |
| BANK_INSTITUTION_TYPE | CustomerBankBranchBankInstitutionType | — |
| BANK_INSTITUTION_TYPE | IssuerBankBranchBankInstitutionType | — |
| BANK_INSTITUTION_TYPE | OldCustomerBankBranchBankInstitutionType | — |
| BANK_INSTITUTION_TYPE | OldIssuerBankBranchBankInstitutionType | — |
| BANK_NAME | CustomerBankBranchBankName | — |
| BANK_NAME | IssuerBankBranchBankName | — |
| BANK_NAME | OldCustomerBankBranchBankName | — |
| BANK_NAME | OldIssuerBankBranchBankName | — |
| BANK_NAME_ALT | CustomerBankBranchBankNameAlt | — |
| BANK_NAME_ALT | IssuerBankBranchBankNameAlt | — |
| BANK_NAME_ALT | OldCustomerBankBranchBankNameAlt | — |
| BANK_NAME_ALT | OldIssuerBankBranchBankNameAlt | — |
| BANK_NUMBER | CustomerBankBranchBankNumber | — |
| BANK_NUMBER | IssuerBankBranchBankNumber | — |
| BANK_NUMBER | OldCustomerBankBranchBankNumber | — |
| BANK_NUMBER | OldIssuerBankBranchBankNumber | — |
| BANK_PARTY_ID | CustomerBankBranchBankPartyId | — |
| BANK_PARTY_ID | IssuerBankBranchBankPartyId | — |
| BANK_PARTY_ID | OldCustomerBankBranchBankPartyId | — |
| BANK_PARTY_ID | OldIssuerBankBranchBankPartyId | — |
| BRANCH_NUMBER | CustomerBankBranchBranchNumber | — |
| BRANCH_NUMBER | IssuerBankBranchBranchNumber | — |
| BRANCH_NUMBER | OldCustomerBankBranchBranchNumber | — |
| BRANCH_NUMBER | OldIssuerBankBranchBranchNumber | — |
| BRANCH_PARTY_ID | CustomerBankBranchBranchPartyId | — |
| BRANCH_PARTY_ID | IssuerBankBranchBranchPartyId | — |
| BRANCH_PARTY_ID | OldCustomerBankBranchBranchPartyId | — |
| BRANCH_PARTY_ID | OldIssuerBankBranchBranchPartyId | — |
| CITY | CustomerBankBranchCity | — |
| CITY | IssuerBankBranchCity | — |
| CITY | OldCustomerBankBranchCity | — |
| CITY | OldIssuerBankBranchCity | — |
| COUNTRY | CustomerBankBranchCountry | — |
| COUNTRY | IssuerBankBranchCountry | — |
| COUNTRY | OldCustomerBankBranchCountry | — |
| COUNTRY | OldIssuerBankBranchCountry | — |
| COUNTRY_NAME | CustomerBankBranchCountryName | — |
| COUNTRY_NAME | IssuerBankBranchCountryName | — |
| COUNTRY_NAME | OldCustomerBankBranchCountryName | — |
| COUNTRY_NAME | OldIssuerBankBranchCountryName | — |
| DESCRIPTION | CustomerBankBranchDescription | — |
| DESCRIPTION | IssuerBankBranchDescription | — |
| DESCRIPTION | OldCustomerBankBranchDescription | — |
| DESCRIPTION | OldIssuerBankBranchDescription | — |
| EDI_ID_NUMBER | CustomerBankBranchEdiIdNumber | — |
| EDI_ID_NUMBER | IssuerBankBranchEdiIdNumber | — |
| EDI_ID_NUMBER | OldCustomerBankBranchEdiIdNumber | — |
| EDI_ID_NUMBER | OldIssuerBankBranchEdiIdNumber | — |
| EDI_LOCATION | CustomerBankBranchEdiLocation | — |
| EDI_LOCATION | IssuerBankBranchEdiLocation | — |
| EDI_LOCATION | OldCustomerBankBranchEdiLocation | — |
| EDI_LOCATION | OldIssuerBankBranchEdiLocation | — |
| EFT_SWIFT_CODE | CustomerBankBranchEftSwiftCode | — |
| EFT_SWIFT_CODE | IssuerBankBranchEftSwiftCode | — |
| EFT_SWIFT_CODE | OldCustomerBankBranchEftSwiftCode | — |
| EFT_SWIFT_CODE | OldIssuerBankBranchEftSwiftCode | — |
| EFT_USER_NUMBER | CustomerBankBranchEftUserNumber | — |
| EFT_USER_NUMBER | IssuerBankBranchEftUserNumber | — |
| EFT_USER_NUMBER | OldCustomerBankBranchEftUserNumber | — |
| EFT_USER_NUMBER | OldIssuerBankBranchEftUserNumber | — |
| END_DATE | CustomerBankBranchEndDate | — |
| END_DATE | IssuerBankBranchEndDate | — |
| END_DATE | OldCustomerBankBranchEndDate | — |
| END_DATE | OldIssuerBankBranchEndDate | — |
| PK_ID | CustomerBankBranchPkId | — |
| PK_ID | IssuerBankBranchPkId | — |
| PK_ID | OldCustomerBankBranchPkId | — |
| PK_ID | OldIssuerBankBranchPkId | — |
| PROVINCE | CustomerBankBranchProvince | — |
| PROVINCE | IssuerBankBranchProvince | — |
| PROVINCE | OldCustomerBankBranchProvince | — |
| PROVINCE | OldIssuerBankBranchProvince | — |
| RFC | CustomerBankBranchRfc | — |
| RFC | IssuerBankBranchRfc | — |
| RFC | OldCustomerBankBranchRfc | — |
| RFC | OldIssuerBankBranchRfc | — |
| ROW_ID | CustomerBankBranchRowId | — |
| ROW_ID | IssuerBankBranchRowId | — |
| ROW_ID | OldCustomerBankBranchRowId | — |
| ROW_ID | OldIssuerBankBranchRowId | — |
| SHORT_BANK_NAME | CustomerBankBranchShortBankName | — |
| SHORT_BANK_NAME | IssuerBankBranchShortBankName | — |
| SHORT_BANK_NAME | OldCustomerBankBranchShortBankName | — |
| SHORT_BANK_NAME | OldIssuerBankBranchShortBankName | — |
| START_DATE | CustomerBankBranchStartDate | — |
| START_DATE | IssuerBankBranchStartDate | — |
| START_DATE | OldCustomerBankBranchStartDate | — |
| START_DATE | OldIssuerBankBranchStartDate | — |
| STATE | CustomerBankBranchState | — |
| STATE | IssuerBankBranchState | — |
| STATE | OldCustomerBankBranchState | — |
| STATE | OldIssuerBankBranchState | — |
| ZIP | CustomerBankBranchZip | — |
| ZIP | IssuerBankBranchZip | — |
| ZIP | OldCustomerBankBranchZip | — |
| ZIP | OldIssuerBankBranchZip | — |
