---
id: DOC-OTHER-PVO-ClaimHeaderExtractPVO
doc_type: system-doc
title: "ClaimHeaderExtractPVO — PVO Cross-Module"
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
  - ClaimHeaderExtractPVO
  - claimheaderextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ClaimHeaderExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Claim Header Extract. Acessa as tabelas: CJM_CLAIMS_ALL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CjmBiccExtractAM.ClaimHeaderExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 159 | 1 | 1 | 159 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cjm_claims_all|CJM_CLAIMS_ALL]] — 159 atributos (1 PKs, 159 BICC)

---

## ⚙️ Atributos

### [[cjm_claims_all|CJM_CLAIMS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AcctdAmount | ACCTD_AMOUNT | — | ✅ |
| 2 | AcctdAmountAdjusted | ACCTD_AMOUNT_ADJUSTED | — | ✅ |
| 3 | AcctdAmountRemaining | ACCTD_AMOUNT_REMAINING | — | ✅ |
| 4 | AcctdAmountSettled | ACCTD_AMOUNT_SETTLED | — | ✅ |
| 5 | Amount | AMOUNT | — | ✅ |
| 6 | AmountAdjusted | AMOUNT_ADJUSTED | — | ✅ |
| 7 | AmountApplied | AMOUNT_APPLIED | — | ✅ |
| 8 | AmountIncludesTaxFlag | AMOUNT_INCLUDES_TAX_FLAG | — | ✅ |
| 9 | AmountRemaining | AMOUNT_REMAINING | — | ✅ |
| 10 | AmountSettled | AMOUNT_SETTLED | — | ✅ |
| 11 | AppliedPaymentScheduleId | APPLIED_PAYMENT_SCHEDULE_ID | — | ✅ |
| 12 | AttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 13 | AttributeChar1 | ATTRIBUTE_CHAR1 | — | ✅ |
| 14 | AttributeChar10 | ATTRIBUTE_CHAR10 | — | ✅ |
| 15 | AttributeChar11 | ATTRIBUTE_CHAR11 | — | ✅ |
| 16 | AttributeChar12 | ATTRIBUTE_CHAR12 | — | ✅ |
| 17 | AttributeChar13 | ATTRIBUTE_CHAR13 | — | ✅ |
| 18 | AttributeChar14 | ATTRIBUTE_CHAR14 | — | ✅ |
| 19 | AttributeChar15 | ATTRIBUTE_CHAR15 | — | ✅ |
| 20 | AttributeChar16 | ATTRIBUTE_CHAR16 | — | ✅ |
| 21 | AttributeChar17 | ATTRIBUTE_CHAR17 | — | ✅ |
| 22 | AttributeChar18 | ATTRIBUTE_CHAR18 | — | ✅ |
| 23 | AttributeChar19 | ATTRIBUTE_CHAR19 | — | ✅ |
| 24 | AttributeChar2 | ATTRIBUTE_CHAR2 | — | ✅ |
| 25 | AttributeChar20 | ATTRIBUTE_CHAR20 | — | ✅ |
| 26 | AttributeChar3 | ATTRIBUTE_CHAR3 | — | ✅ |
| 27 | AttributeChar4 | ATTRIBUTE_CHAR4 | — | ✅ |
| 28 | AttributeChar5 | ATTRIBUTE_CHAR5 | — | ✅ |
| 29 | AttributeChar6 | ATTRIBUTE_CHAR6 | — | ✅ |
| 30 | AttributeChar7 | ATTRIBUTE_CHAR7 | — | ✅ |
| 31 | AttributeChar8 | ATTRIBUTE_CHAR8 | — | ✅ |
| 32 | AttributeChar9 | ATTRIBUTE_CHAR9 | — | ✅ |
| 33 | AttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 34 | AttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 35 | AttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 36 | AttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 37 | AttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 38 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 39 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 40 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 41 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 42 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 43 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 44 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 45 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 46 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 47 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 48 | AttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 49 | AttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 50 | AttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 51 | AttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 52 | AttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 53 | BillToAddressId | BILL_TO_ADDRESS_ID | — | ✅ |
| 54 | BillToContactId | BILL_TO_CONTACT_ID | — | ✅ |
| 55 | BillToCustomerId | BILL_TO_CUSTOMER_ID | — | ✅ |
| 56 | BillToSiteUseId | BILL_TO_SITE_USE_ID | — | ✅ |
| 57 | BuId | BU_ID | — | ✅ |
| 58 | ClaimClassCode | CLAIM_CLASS_CODE | — | ✅ |
| 59 | ClaimComments | CLAIM_COMMENTS | — | ✅ |
| 60 | ClaimDate | CLAIM_DATE | — | ✅ |
| 61 | ClaimForCode | CLAIM_FOR_CODE | — | ✅ |
| 62 | ClaimId | CLAIM_ID | 🔑 | ✅ |
| 63 | ClaimNumber | CLAIM_NUMBER | — | ✅ |
| 64 | ClaimSourceCode | CLAIM_SOURCE_CODE | — | ✅ |
| 65 | ClaimTypeId | CLAIM_TYPE_ID | — | ✅ |
| 66 | CreatedBy | CREATED_BY | — | ✅ |
| 67 | CreationDate | CREATION_DATE | — | ✅ |
| 68 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 69 | CustomerAttributeCategory | CUSTOMER_ATTRIBUTE_CATEGORY | — | ✅ |
| 70 | CustomerAttributeChar1 | CUSTOMER_ATTRIBUTE_CHAR1 | — | ✅ |
| 71 | CustomerAttributeChar10 | CUSTOMER_ATTRIBUTE_CHAR10 | — | ✅ |
| 72 | CustomerAttributeChar11 | CUSTOMER_ATTRIBUTE_CHAR11 | — | ✅ |
| 73 | CustomerAttributeChar12 | CUSTOMER_ATTRIBUTE_CHAR12 | — | ✅ |
| 74 | CustomerAttributeChar13 | CUSTOMER_ATTRIBUTE_CHAR13 | — | ✅ |
| 75 | CustomerAttributeChar14 | CUSTOMER_ATTRIBUTE_CHAR14 | — | ✅ |
| 76 | CustomerAttributeChar15 | CUSTOMER_ATTRIBUTE_CHAR15 | — | ✅ |
| 77 | CustomerAttributeChar16 | CUSTOMER_ATTRIBUTE_CHAR16 | — | ✅ |
| 78 | CustomerAttributeChar17 | CUSTOMER_ATTRIBUTE_CHAR17 | — | ✅ |
| 79 | CustomerAttributeChar18 | CUSTOMER_ATTRIBUTE_CHAR18 | — | ✅ |
| 80 | CustomerAttributeChar19 | CUSTOMER_ATTRIBUTE_CHAR19 | — | ✅ |
| 81 | CustomerAttributeChar2 | CUSTOMER_ATTRIBUTE_CHAR2 | — | ✅ |
| 82 | CustomerAttributeChar20 | CUSTOMER_ATTRIBUTE_CHAR20 | — | ✅ |
| 83 | CustomerAttributeChar3 | CUSTOMER_ATTRIBUTE_CHAR3 | — | ✅ |
| 84 | CustomerAttributeChar4 | CUSTOMER_ATTRIBUTE_CHAR4 | — | ✅ |
| 85 | CustomerAttributeChar5 | CUSTOMER_ATTRIBUTE_CHAR5 | — | ✅ |
| 86 | CustomerAttributeChar6 | CUSTOMER_ATTRIBUTE_CHAR6 | — | ✅ |
| 87 | CustomerAttributeChar7 | CUSTOMER_ATTRIBUTE_CHAR7 | — | ✅ |
| 88 | CustomerAttributeChar8 | CUSTOMER_ATTRIBUTE_CHAR8 | — | ✅ |
| 89 | CustomerAttributeChar9 | CUSTOMER_ATTRIBUTE_CHAR9 | — | ✅ |
| 90 | CustomerAttributeDate1 | CUSTOMER_ATTRIBUTE_DATE1 | — | ✅ |
| 91 | CustomerAttributeDate2 | CUSTOMER_ATTRIBUTE_DATE2 | — | ✅ |
| 92 | CustomerAttributeDate3 | CUSTOMER_ATTRIBUTE_DATE3 | — | ✅ |
| 93 | CustomerAttributeDate4 | CUSTOMER_ATTRIBUTE_DATE4 | — | ✅ |
| 94 | CustomerAttributeDate5 | CUSTOMER_ATTRIBUTE_DATE5 | — | ✅ |
| 95 | CustomerAttributeNumber1 | CUSTOMER_ATTRIBUTE_NUMBER1 | — | ✅ |
| 96 | CustomerAttributeNumber10 | CUSTOMER_ATTRIBUTE_NUMBER10 | — | ✅ |
| 97 | CustomerAttributeNumber2 | CUSTOMER_ATTRIBUTE_NUMBER2 | — | ✅ |
| 98 | CustomerAttributeNumber3 | CUSTOMER_ATTRIBUTE_NUMBER3 | — | ✅ |
| 99 | CustomerAttributeNumber4 | CUSTOMER_ATTRIBUTE_NUMBER4 | — | ✅ |
| 100 | CustomerAttributeNumber5 | CUSTOMER_ATTRIBUTE_NUMBER5 | — | ✅ |
| 101 | CustomerAttributeNumber6 | CUSTOMER_ATTRIBUTE_NUMBER6 | — | ✅ |
| 102 | CustomerAttributeNumber7 | CUSTOMER_ATTRIBUTE_NUMBER7 | — | ✅ |
| 103 | CustomerAttributeNumber8 | CUSTOMER_ATTRIBUTE_NUMBER8 | — | ✅ |
| 104 | CustomerAttributeNumber9 | CUSTOMER_ATTRIBUTE_NUMBER9 | — | ✅ |
| 105 | CustomerAttributeTimestamp1 | CUSTOMER_ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 106 | CustomerAttributeTimestamp2 | CUSTOMER_ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 107 | CustomerAttributeTimestamp3 | CUSTOMER_ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 108 | CustomerAttributeTimestamp4 | CUSTOMER_ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 109 | CustomerAttributeTimestamp5 | CUSTOMER_ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 110 | CustomerReason | CUSTOMER_REASON | — | ✅ |
| 111 | CustomerRefDate | CUSTOMER_REF_DATE | — | ✅ |
| 112 | CustomerRefNumber | CUSTOMER_REF_NUMBER | — | ✅ |
| 113 | ExchangeRate | EXCHANGE_RATE | — | ✅ |
| 114 | ExchangeRateDate | EXCHANGE_RATE_DATE | — | ✅ |
| 115 | ExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 116 | GlDate | GL_DATE | — | ✅ |
| 117 | GroupClaimId | GROUP_CLAIM_ID | — | ✅ |
| 118 | InvoiceBuId | INVOICE_BU_ID | — | ✅ |
| 119 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 120 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 121 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 122 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 123 | LegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 124 | MassSettlementNumber | MASS_SETTLEMENT_NUMBER | — | ✅ |
| 125 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 126 | OriginalClaimDate | ORIGINAL_CLAIM_DATE | — | ✅ |
| 127 | OwnerId | OWNER_ID | — | ✅ |
| 128 | PrimaryResourceSalesrepId | PRIMARY_RESOURCE_SALESREP_ID | — | ✅ |
| 129 | ProgramHeaderId | PROGRAM_HEADER_ID | — | ✅ |
| 130 | ReasonCodeId | REASON_CODE_ID | — | ✅ |
| 131 | ReceiptBuId | RECEIPT_BU_ID | — | ✅ |
| 132 | ReceiptId | RECEIPT_ID | — | ✅ |
| 133 | ReceiptNumber | RECEIPT_NUMBER | — | ✅ |
| 134 | ReceivableApplicationId | RECEIVABLE_APPLICATION_ID | — | ✅ |
| 135 | ReceivablesTrxId | RECEIVABLES_TRX_ID | — | ✅ |
| 136 | RequestId | REQUEST_ID | — | ✅ |
| 137 | ResolvedDate | RESOLVED_DATE | — | ✅ |
| 138 | RootClaimId | ROOT_CLAIM_ID | — | ✅ |
| 139 | SettledBy | SETTLED_BY | — | ✅ |
| 140 | SettledDate | SETTLED_DATE | — | ✅ |
| 141 | ShipToPartyAddressId | SHIP_TO_PARTY_ADDRESS_ID | — | ✅ |
| 142 | ShipToPartyContactId | SHIP_TO_PARTY_CONTACT_ID | — | ✅ |
| 143 | ShipToPartyId | SHIP_TO_PARTY_ID | — | ✅ |
| 144 | ShipToPartySiteUseId | SHIP_TO_PARTY_SITE_USE_ID | — | ✅ |
| 145 | SourceMapId | SOURCE_MAP_ID | — | ✅ |
| 146 | SourceObjectClass | SOURCE_OBJECT_CLASS | — | ✅ |
| 147 | SourceObjectDate | SOURCE_OBJECT_DATE | — | ✅ |
| 148 | SourceObjectId | SOURCE_OBJECT_ID | — | ✅ |
| 149 | SourceObjectNumber | SOURCE_OBJECT_NUMBER | — | ✅ |
| 150 | SourceObjectTypeId | SOURCE_OBJECT_TYPE_ID | — | ✅ |
| 151 | SplitDate | SPLIT_DATE | — | ✅ |
| 152 | SplitFromClaimId | SPLIT_FROM_CLAIM_ID | — | ✅ |
| 153 | StatusCode | STATUS_CODE | — | ✅ |
| 154 | TaxAmount | TAX_AMOUNT | — | ✅ |
| 155 | UserStatusId | USER_STATUS_ID | — | ✅ |
| 156 | VendorId | VENDOR_ID | — | ✅ |
| 157 | VendorSiteId | VENDOR_SITE_ID | — | ✅ |
| 158 | WoReceivablesActivityId | WO_RECEIVABLES_ACTIVITY_ID | — | ✅ |
| 159 | WriteOffFlag | WRITE_OFF_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
