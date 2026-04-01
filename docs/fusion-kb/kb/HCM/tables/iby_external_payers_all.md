---
id: DOC-HCM-512
doc_type: system-doc
title: "IBY_EXTERNAL_PAYERS_ALL — (título a preencher)"
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
  - IBY_EXTERNAL_PAYERS_ALL
  - iby_external_payers_all
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# IBY_EXTERNAL_PAYERS_ALL

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ACCT_SITE_USE_ID | — | — | — | — | — | — |
| 2 | BANK_CHARGE_BEARER_CODE | — | — | — | — | — | — |
| 3 | CREATED_BY | — | — | — | — | — | — |
| 4 | CREATION_DATE | — | — | — | — | — | — |
| 5 | CUST_ACCOUNT_ID | — | — | — | — | — | — |
| 6 | DEBIT_ADVICE_DELIVERY_METHOD | — | — | — | — | — | — |
| 7 | DEBIT_ADVICE_EMAIL | — | — | — | — | — | — |
| 8 | DEBIT_ADVICE_FAX | — | — | — | — | — | — |
| 9 | DIRDEB_INSTRUCTION_CODE | — | — | — | — | — | — |
| 10 | EXT_PAYER_ID | — | — | — | — | — | — |
| 11 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 12 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 13 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 14 | LOCALINSTR | — | — | — | — | — | — |
| 15 | OBJECT_VERSION_NUMBER | — | — | — | — | — | — |
| 16 | ORG_ID | — | — | — | — | — | — |
| 17 | ORG_TYPE | — | — | — | — | — | — |
| 18 | PARTY_ID | — | — | — | — | — | — |
| 19 | PAYMENT_FUNCTION | — | — | — | — | — | — |
| 20 | PURPOSE_CODE | — | — | — | — | — | — |
| 21 | SERVICE_LEVEL | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[accountbankaccount|AccountBankAccount]] (AR · BICC: 6/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCT_SITE_USE_ID | PayersAcctSiteUseId | — |
| BANK_CHARGE_BEARER_CODE | PayersBankChargeBearerCode | ✅ |
| CREATED_BY | PayersCreatedBy | — |
| CREATION_DATE | PayersCreationDate | — |
| CUST_ACCOUNT_ID | PayersCustAccountId | — |
| DEBIT_ADVICE_DELIVERY_METHOD | PayersDebitAdviceDeliveryMethod | — |
| DEBIT_ADVICE_EMAIL | PayersDebitAdviceEmail | — |
| DEBIT_ADVICE_FAX | PayersDebitAdviceFax | — |
| DIRDEB_INSTRUCTION_CODE | PayersDirdebInstructionCode | ✅ |
| EXT_PAYER_ID | PayersExtPayerId | — |
| LAST_UPDATE_DATE | PayersLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PayersLastUpdateLogin | — |
| LAST_UPDATED_BY | PayersLastUpdatedBy | — |
| LOCALINSTR | PayersLocalinstr | ✅ |
| OBJECT_VERSION_NUMBER | PayersObjectVersionNumber | — |
| ORG_ID | PayersOrgId | — |
| ORG_TYPE | PayersOrgType | — |
| PARTY_ID | PayersPartyId | — |
| PAYMENT_FUNCTION | PayersPaymentFunction | — |
| PURPOSE_CODE | PayersPurposeCode | ✅ |
| SERVICE_LEVEL | PayersServiceLevel | ✅ |

### [[accountcreditcard|AccountCreditCard]] (AR · BICC: 1/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCT_SITE_USE_ID | PayersAcctSiteUseId | — |
| BANK_CHARGE_BEARER_CODE | PayersBankChargeBearerCode | — |
| CREATED_BY | PayersCreatedBy | — |
| CREATION_DATE | PayersCreationDate | — |
| CUST_ACCOUNT_ID | PayersCustAccountId | — |
| DEBIT_ADVICE_DELIVERY_METHOD | PayersDebitAdviceDeliveryMethod | — |
| DEBIT_ADVICE_EMAIL | PayersDebitAdviceEmail | — |
| DEBIT_ADVICE_FAX | PayersDebitAdviceFax | — |
| DIRDEB_INSTRUCTION_CODE | PayersDirdebInstructionCode | — |
| EXT_PAYER_ID | PayersExtPayerId | — |
| LAST_UPDATE_DATE | PayersLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PayersLastUpdateLogin | — |
| LAST_UPDATED_BY | PayersLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | PayersObjectVersionNumber | — |
| ORG_ID | PayersOrgId | — |
| ORG_TYPE | PayersOrgType | — |
| PARTY_ID | PayersPartyId | — |
| PAYMENT_FUNCTION | PayersPaymentFunction | — |

### [[accountpaymentnotification|AccountPaymentNotification]] (AR · BICC: 5/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCT_SITE_USE_ID | PayersAcctSiteUseId | — |
| BANK_CHARGE_BEARER_CODE | PayersBankChargeBearerCode | — |
| CREATED_BY | PayersCreatedBy | — |
| CREATION_DATE | PayersCreationDate | — |
| CUST_ACCOUNT_ID | PayersCustAccountId | — |
| DEBIT_ADVICE_DELIVERY_METHOD | PayersDebitAdviceDeliveryMethod | ✅ |
| DEBIT_ADVICE_EMAIL | PayersDebitAdviceEmail | ✅ |
| DEBIT_ADVICE_FAX | PayersDebitAdviceFax | ✅ |
| DIRDEB_INSTRUCTION_CODE | PayersDirdebInstructionCode | — |
| EXT_PAYER_ID | ExtPayerId | ✅ |
| LAST_UPDATE_DATE | PayersLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PayersLastUpdateLogin | — |
| LAST_UPDATED_BY | PayersLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | PayersObjectVersionNumber | — |
| ORG_ID | PayersOrgId | — |
| ORG_TYPE | PayersOrgType | — |
| PARTY_ID | PayersPartyId | — |
| PAYMENT_FUNCTION | PayersPaymentFunction | — |

### [[sitebankaccount|SiteBankAccount]] (AR · BICC: 6/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCT_SITE_USE_ID | PayersAcctSiteUseId | — |
| BANK_CHARGE_BEARER_CODE | PayersBankChargeBearerCode | ✅ |
| CREATED_BY | PayersCreatedBy | — |
| CREATION_DATE | PayersCreationDate | — |
| CUST_ACCOUNT_ID | PayersCustAccountId | — |
| DEBIT_ADVICE_DELIVERY_METHOD | PayersDebitAdviceDeliveryMethod | — |
| DEBIT_ADVICE_EMAIL | PayersDebitAdviceEmail | — |
| DEBIT_ADVICE_FAX | PayersDebitAdviceFax | — |
| DIRDEB_INSTRUCTION_CODE | PayersDirdebInstructionCode | ✅ |
| EXT_PAYER_ID | PayersExtPayerId | — |
| LAST_UPDATE_DATE | PayersLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PayersLastUpdateLogin | — |
| LAST_UPDATED_BY | PayersLastUpdatedBy | — |
| LOCALINSTR | PayersLocalinstr | ✅ |
| OBJECT_VERSION_NUMBER | PayersObjectVersionNumber | — |
| ORG_ID | PayersOrgId | — |
| ORG_TYPE | PayersOrgType | — |
| PARTY_ID | PayersPartyId | — |
| PAYMENT_FUNCTION | PayersPaymentFunction | — |
| PURPOSE_CODE | PayersPurposeCode | ✅ |
| SERVICE_LEVEL | PayersServiceLevel | ✅ |

### [[sitecreditcard|SiteCreditCard]] (AR · BICC: 1/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCT_SITE_USE_ID | PayersAcctSiteUseId | — |
| BANK_CHARGE_BEARER_CODE | PayersBankChargeBearerCode | — |
| CREATED_BY | PayersCreatedBy | — |
| CREATION_DATE | PayersCreationDate | — |
| CUST_ACCOUNT_ID | PayersCustAccountId | — |
| DEBIT_ADVICE_DELIVERY_METHOD | PayersDebitAdviceDeliveryMethod | — |
| DEBIT_ADVICE_EMAIL | PayersDebitAdviceEmail | — |
| DEBIT_ADVICE_FAX | PayersDebitAdviceFax | — |
| DIRDEB_INSTRUCTION_CODE | PayersDirdebInstructionCode | — |
| EXT_PAYER_ID | PayersExtPayerId | — |
| LAST_UPDATE_DATE | PayersLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PayersLastUpdateLogin | — |
| LAST_UPDATED_BY | PayersLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | PayersObjectVersionNumber | — |
| ORG_ID | PayersOrgId | — |
| ORG_TYPE | PayersOrgType | — |
| PARTY_ID | PayersPartyId | — |
| PAYMENT_FUNCTION | PayersPaymentFunction | — |

### [[sitepaymentnotification|SitePaymentNotification]] (AR · BICC: 5/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCT_SITE_USE_ID | PayersAcctSiteUseId | — |
| BANK_CHARGE_BEARER_CODE | PayersBankChargeBearerCode | — |
| CREATED_BY | PayersCreatedBy | — |
| CREATION_DATE | PayersCreationDate | — |
| CUST_ACCOUNT_ID | PayersCustAccountId | — |
| DEBIT_ADVICE_DELIVERY_METHOD | PayersDebitAdviceDeliveryMethod | ✅ |
| DEBIT_ADVICE_EMAIL | PayersDebitAdviceEmail | ✅ |
| DEBIT_ADVICE_FAX | PayersDebitAdviceFax | ✅ |
| DIRDEB_INSTRUCTION_CODE | PayersDirdebInstructionCode | — |
| EXT_PAYER_ID | ExtPayerId | ✅ |
| LAST_UPDATE_DATE | PayersLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PayersLastUpdateLogin | — |
| LAST_UPDATED_BY | PayersLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | PayersObjectVersionNumber | — |
| ORG_ID | PayersOrgId | — |
| ORG_TYPE | PayersOrgType | — |
| PARTY_ID | PayersPartyId | — |
| PAYMENT_FUNCTION | PayersPaymentFunction | — |
