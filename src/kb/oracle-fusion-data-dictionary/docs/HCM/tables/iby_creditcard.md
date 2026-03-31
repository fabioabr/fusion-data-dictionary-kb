---
id: DOC-HCM-509
doc_type: system-doc
title: "IBY_CREDITCARD — (título a preencher)"
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
  - IBY_CREDITCARD
  - iby_creditcard
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# IBY_CREDITCARD

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ACCTTYPEID | — | — | — | — | — | — |
| 2 | ADDRESSID | — | — | — | — | — | — |
| 3 | BILLING_ADDR_POSTAL_CODE | — | — | — | — | — | — |
| 4 | BILL_ADDR_TERRITORY_CODE | — | — | — | — | — | — |
| 5 | CARD_ISSUER_CODE | — | — | — | — | — | — |
| 6 | CARD_MASK_SETTING | — | — | — | — | — | — |
| 7 | CARD_OWNER_ID | — | — | — | — | — | — |
| 8 | CARD_PURPOSE | — | — | — | — | — | — |
| 9 | CARD_UNMASK_LENGTH | — | — | — | — | — | — |
| 10 | CCNUMBER | — | — | — | — | — | — |
| 11 | CC_ISSUER_RANGE_ID | — | — | — | — | — | — |
| 12 | CC_NUMBER_HASH1 | — | — | — | — | — | — |
| 13 | CC_NUMBER_HASH2 | — | — | — | — | — | — |
| 14 | CC_NUMBER_LENGTH | — | — | — | — | — | — |
| 15 | CC_NUM_SEC_SEGMENT_ID | — | — | — | — | — | — |
| 16 | CHNAME | — | — | — | — | — | — |
| 17 | CREATED_BY | — | — | — | — | — | — |
| 18 | CREATION_DATE | — | — | — | — | — | — |
| 19 | DESCRIPTION | — | — | — | — | — | — |
| 20 | ENCRYPTED | — | — | — | — | — | — |
| 21 | END_DATE | — | — | — | — | — | — |
| 22 | EXPIRYDATE | — | — | — | — | — | — |
| 23 | EXPIRY_SEC_SEGMENT_ID | — | — | — | — | — | — |
| 24 | FINAME | — | — | — | — | — | — |
| 25 | INFORMATION_ONLY_FLAG | — | — | — | — | — | — |
| 26 | INSTRBUF | — | — | — | — | — | — |
| 27 | INSTRID | — | — | — | — | — | — |
| 28 | INSTRNAME | — | — | — | — | — | — |
| 29 | INSTRUMENT_TYPE | — | — | — | — | — | — |
| 30 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 31 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 32 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 33 | MASKED_CC_NUMBER | — | — | — | — | — | — |
| 34 | OBJECT_VERSION_NUMBER | — | — | — | — | — | — |
| 35 | PROGRAM_APPLICATION_ID | — | — | — | — | — | — |
| 36 | PROGRAM_ID | — | — | — | — | — | — |
| 37 | PROGRAM_UPDATE_DATE | — | — | — | — | — | — |
| 38 | PURCHASECARD_FLAG | — | — | — | — | — | — |
| 39 | PURCHASECARD_SUBTYPE | — | — | — | — | — | — |
| 40 | REQUEST_ID | — | — | — | — | — | — |
| 41 | SECURITY_GROUP_ID | — | — | — | — | — | — |
| 42 | SEC_SUBKEY_ID | — | — | — | — | — | — |
| 43 | SINGLE_USE_FLAG | — | — | — | — | — | — |
| 44 | START_DATE | — | — | — | — | — | — |
| 45 | SUBTYPE | — | — | — | — | — | — |
| 46 | UPGRADE_ADDRESSID | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[accountcreditcard|AccountCreditCard]] (AR · BICC: 11/46)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTTYPEID | CreditCardAccttypeid | — |
| ADDRESSID | CreditCardAddressid | — |
| BILL_ADDR_TERRITORY_CODE | CreditCardBillAddrTerritoryCode | — |
| BILLING_ADDR_POSTAL_CODE | CreditCardBillingAddrPostalCode | — |
| CARD_ISSUER_CODE | CreditCardCardIssuerCode | ✅ |
| CARD_MASK_SETTING | CreditCardCardMaskSetting | — |
| CARD_OWNER_ID | CreditCardCardOwnerId | — |
| CARD_PURPOSE | CreditCardCardPurpose | ✅ |
| CARD_UNMASK_LENGTH | CreditCardCardUnmaskLength | — |
| CC_ISSUER_RANGE_ID | CreditCardCcIssuerRangeId | — |
| CC_NUM_SEC_SEGMENT_ID | CreditCardCcNumSecSegmentId | — |
| CC_NUMBER_HASH1 | CreditCardCcNumberHash1 | — |
| CC_NUMBER_HASH2 | CreditCardCcNumberHash2 | — |
| CC_NUMBER_LENGTH | CreditCardCcNumberLength | — |
| CCNUMBER | CreditCardCcnumber | — |
| CHNAME | CreditCardChname | ✅ |
| CREATED_BY | CreditCardCreatedBy | — |
| CREATION_DATE | CreditCardCreationDate | — |
| DESCRIPTION | CreditCardDescription | ✅ |
| ENCRYPTED | CreditCardEncrypted | — |
| END_DATE | CreditCardEndDate | ✅ |
| EXPIRY_SEC_SEGMENT_ID | CreditCardExpirySecSegmentId | — |
| EXPIRYDATE | CreditCardExpirydate | ✅ |
| FINAME | CreditCardFiname | ✅ |
| INFORMATION_ONLY_FLAG | CreditCardInformationOnlyFlag | — |
| INSTRBUF | CreditCardInstrbuf | — |
| INSTRID | CreditCardInstrid | — |
| INSTRNAME | CreditCardInstrname | — |
| INSTRUMENT_TYPE | CreditCardInstrumentType | — |
| LAST_UPDATE_DATE | CreditCardLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CreditCardLastUpdateLogin | — |
| LAST_UPDATED_BY | CreditCardLastUpdatedBy | — |
| MASKED_CC_NUMBER | CreditCardMaskedCcNumber | ✅ |
| OBJECT_VERSION_NUMBER | CreditCardObjectVersionNumber | — |
| PROGRAM_APPLICATION_ID | CreditCardProgramApplicationId | — |
| PROGRAM_ID | CreditCardProgramId | — |
| PROGRAM_UPDATE_DATE | CreditCardProgramUpdateDate | — |
| PURCHASECARD_FLAG | CreditCardPurchasecardFlag | ✅ |
| PURCHASECARD_SUBTYPE | CreditCardPurchasecardSubtype | — |
| REQUEST_ID | CreditCardRequestId | — |
| SEC_SUBKEY_ID | CreditCardSecSubkeyId | — |
| SECURITY_GROUP_ID | CreditCardSecurityGroupId | — |
| SINGLE_USE_FLAG | CreditCardSingleUseFlag | — |
| START_DATE | CreditCardStartDate | ✅ |
| SUBTYPE | CreditCardSubtype | — |
| UPGRADE_ADDRESSID | CreditCardUpgradeAddressid | — |

### [[sitecreditcard|SiteCreditCard]] (AR · BICC: 11/46)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTTYPEID | CreditCardAccttypeid | — |
| ADDRESSID | CreditCardAddressid | — |
| BILL_ADDR_TERRITORY_CODE | CreditCardBillAddrTerritoryCode | — |
| BILLING_ADDR_POSTAL_CODE | CreditCardBillingAddrPostalCode | — |
| CARD_ISSUER_CODE | CreditCardCardIssuerCode | ✅ |
| CARD_MASK_SETTING | CreditCardCardMaskSetting | — |
| CARD_OWNER_ID | CreditCardCardOwnerId | — |
| CARD_PURPOSE | CreditCardCardPurpose | ✅ |
| CARD_UNMASK_LENGTH | CreditCardCardUnmaskLength | — |
| CC_ISSUER_RANGE_ID | CreditCardCcIssuerRangeId | — |
| CC_NUM_SEC_SEGMENT_ID | CreditCardCcNumSecSegmentId | — |
| CC_NUMBER_HASH1 | CreditCardCcNumberHash1 | — |
| CC_NUMBER_HASH2 | CreditCardCcNumberHash2 | — |
| CC_NUMBER_LENGTH | CreditCardCcNumberLength | — |
| CCNUMBER | CreditCardCcnumber | — |
| CHNAME | CreditCardChname | ✅ |
| CREATED_BY | CreditCardCreatedBy | — |
| CREATION_DATE | CreditCardCreationDate | — |
| DESCRIPTION | CreditCardDescription | ✅ |
| ENCRYPTED | CreditCardEncrypted | — |
| END_DATE | CreditCardEndDate | ✅ |
| EXPIRY_SEC_SEGMENT_ID | CreditCardExpirySecSegmentId | — |
| EXPIRYDATE | CreditCardExpirydate | ✅ |
| FINAME | CreditCardFiname | ✅ |
| INFORMATION_ONLY_FLAG | CreditCardInformationOnlyFlag | — |
| INSTRBUF | CreditCardInstrbuf | — |
| INSTRID | CreditCardInstrid | — |
| INSTRNAME | CreditCardInstrname | — |
| INSTRUMENT_TYPE | CreditCardInstrumentType | — |
| LAST_UPDATE_DATE | CreditCardLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CreditCardLastUpdateLogin | — |
| LAST_UPDATED_BY | CreditCardLastUpdatedBy | — |
| MASKED_CC_NUMBER | CreditCardMaskedCcNumber | ✅ |
| OBJECT_VERSION_NUMBER | CreditCardObjectVersionNumber | — |
| PROGRAM_APPLICATION_ID | CreditCardProgramApplicationId | — |
| PROGRAM_ID | CreditCardProgramId | — |
| PROGRAM_UPDATE_DATE | CreditCardProgramUpdateDate | — |
| PURCHASECARD_FLAG | CreditCardPurchasecardFlag | ✅ |
| PURCHASECARD_SUBTYPE | CreditCardPurchasecardSubtype | — |
| REQUEST_ID | CreditCardRequestId | — |
| SEC_SUBKEY_ID | CreditCardSecSubkeyId | — |
| SECURITY_GROUP_ID | CreditCardSecurityGroupId | — |
| SINGLE_USE_FLAG | CreditCardSingleUseFlag | — |
| START_DATE | CreditCardStartDate | ✅ |
| SUBTYPE | CreditCardSubtype | — |
| UPGRADE_ADDRESSID | CreditCardUpgradeAddressid | — |
