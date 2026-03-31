---
id: DOC-OTHER-PVO-FosFinancialTradeRelationExtractPVO
doc_type: system-doc
title: "FosFinancialTradeRelationExtractPVO — PVO Cross-Module"
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
  - FosFinancialTradeRelationExtractPVO
  - fosfinancialtraderelationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FosFinancialTradeRelationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fos Financial Trade Relation Extract. Acessa as tabelas: FOS_AGREEMENT_FTR_F.

**Caminho:** `FscmTopModelAM.ScmExtractAM.FosBiccExtractAM.FosFinancialTradeRelationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 79 | 1 | 3 | 79 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fos_agreement_ftr_f|FOS_AGREEMENT_FTR_F]] — 79 atributos (3 PKs, 79 BICC)

---

## ⚙️ Atributos

### [[fos_agreement_ftr_f|FOS_AGREEMENT_FTR_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FinancialTradeRelationPEOAgreementFtrId | AGREEMENT_FTR_ID | 🔑 | ✅ |
| 2 | FinancialTradeRelationPEOAgreementId | AGREEMENT_ID | — | ✅ |
| 3 | FinancialTradeRelationPEOAgreementPtrId | AGREEMENT_PTR_ID | — | ✅ |
| 4 | FinancialTradeRelationPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 5 | FinancialTradeRelationPEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | ✅ |
| 6 | FinancialTradeRelationPEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | ✅ |
| 7 | FinancialTradeRelationPEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | ✅ |
| 8 | FinancialTradeRelationPEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | ✅ |
| 9 | FinancialTradeRelationPEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | ✅ |
| 10 | FinancialTradeRelationPEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | ✅ |
| 11 | FinancialTradeRelationPEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | ✅ |
| 12 | FinancialTradeRelationPEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | ✅ |
| 13 | FinancialTradeRelationPEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | ✅ |
| 14 | FinancialTradeRelationPEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | ✅ |
| 15 | FinancialTradeRelationPEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | ✅ |
| 16 | FinancialTradeRelationPEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | ✅ |
| 17 | FinancialTradeRelationPEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | ✅ |
| 18 | FinancialTradeRelationPEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | ✅ |
| 19 | FinancialTradeRelationPEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | ✅ |
| 20 | FinancialTradeRelationPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 21 | FinancialTradeRelationPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 22 | FinancialTradeRelationPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 23 | FinancialTradeRelationPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 24 | FinancialTradeRelationPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 25 | FinancialTradeRelationPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 26 | FinancialTradeRelationPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 27 | FinancialTradeRelationPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 28 | FinancialTradeRelationPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 29 | FinancialTradeRelationPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 30 | FinancialTradeRelationPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 31 | FinancialTradeRelationPEOBsrId | BSR_ID | — | ✅ |
| 32 | FinancialTradeRelationPEOBuyingCrmDocCategoryCode | BUYING_CRM_DOC_CATEGORY_CODE | — | ✅ |
| 33 | FinancialTradeRelationPEOBuyingDefaultTxtCountry | BUYING_DEFAULT_TXT_COUNTRY | — | ✅ |
| 34 | FinancialTradeRelationPEOBuyingDocCategoryCode | BUYING_DOC_CATEGORY_CODE | — | ✅ |
| 35 | FinancialTradeRelationPEOBuyingDocumentSubType | BUYING_DOCUMENT_SUB_TYPE | — | ✅ |
| 36 | FinancialTradeRelationPEOBuyingFirstPtyRegId | BUYING_FIRST_PTY_REG_ID | — | ✅ |
| 37 | FinancialTradeRelationPEOBuyingIntendedUse | BUYING_INTENDED_USE | — | ✅ |
| 38 | FinancialTradeRelationPEOBuyingProductCategory | BUYING_PRODUCT_CATEGORY | — | ✅ |
| 39 | FinancialTradeRelationPEOBuyingProductFiscClsf | BUYING_PRODUCT_FISC_CLSF | — | ✅ |
| 40 | FinancialTradeRelationPEOBuyingThirdPtyRegId | BUYING_THIRD_PTY_REG_ID | — | ✅ |
| 41 | FinancialTradeRelationPEOBuyingTrxBusinessCategory | BUYING_TRX_BUSINESS_CATEGORY | — | ✅ |
| 42 | FinancialTradeRelationPEOBuyingUserDefinedFiscCls | BUYING_USER_DEFINED_FISC_CLS | — | ✅ |
| 43 | FinancialTradeRelationPEOChargeAccountCcid | CHARGE_ACCOUNT_CCID | — | ✅ |
| 44 | FinancialTradeRelationPEOCreatedBy | CREATED_BY | — | ✅ |
| 45 | FinancialTradeRelationPEOCreationDate | CREATION_DATE | — | ✅ |
| 46 | FinancialTradeRelationPEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 47 | FinancialTradeRelationPEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 48 | FinancialTradeRelationPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 49 | FinancialTradeRelationPEOFromBuId | FROM_BU_ID | — | ✅ |
| 50 | FinancialTradeRelationPEOFromTradeOrg | FROM_TRADE_ORG | — | ✅ |
| 51 | FinancialTradeRelationPEOIncotermLocation | INCOTERM_LOCATION | — | ✅ |
| 52 | FinancialTradeRelationPEOIncoterms | INCOTERMS | — | ✅ |
| 53 | FinancialTradeRelationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 54 | FinancialTradeRelationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 55 | FinancialTradeRelationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 56 | FinancialTradeRelationPEOLogicalReceiptHoldFlag | LOGICAL_RECEIPT_HOLD_FLAG | — | ✅ |
| 57 | FinancialTradeRelationPEOLogicalShipHoldFlag | LOGICAL_SHIP_HOLD_FLAG | — | ✅ |
| 58 | FinancialTradeRelationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 59 | FinancialTradeRelationPEOOcForwardTimeLag | OC_FORWARD_TIME_LAG | — | ✅ |
| 60 | FinancialTradeRelationPEOOcFwdEventDefId | OC_FWD_EVENT_DEF_ID | — | ✅ |
| 61 | FinancialTradeRelationPEOOcRetEventDefId | OC_RET_EVENT_DEF_ID | — | ✅ |
| 62 | FinancialTradeRelationPEOOcReturnTimeLag | OC_RETURN_TIME_LAG | — | ✅ |
| 63 | FinancialTradeRelationPEOPaymentTermId | PAYMENT_TERM_ID | — | ✅ |
| 64 | FinancialTradeRelationPEOPricingId | PRICING_ID | — | ✅ |
| 65 | FinancialTradeRelationPEOReceivablesCreditMemoType | RECEIVABLES_CREDIT_MEMO_TYPE | — | ✅ |
| 66 | FinancialTradeRelationPEOReceivablesInvoiceType | RECEIVABLES_INVOICE_TYPE | — | ✅ |
| 67 | FinancialTradeRelationPEOSellingDefaultTxtCountry | SELLING_DEFAULT_TXT_COUNTRY | — | ✅ |
| 68 | FinancialTradeRelationPEOSellingDocumentSubType | SELLING_DOCUMENT_SUB_TYPE | — | ✅ |
| 69 | FinancialTradeRelationPEOSellingFirstPtyRegId | SELLING_FIRST_PTY_REG_ID | — | ✅ |
| 70 | FinancialTradeRelationPEOSellingIntendedUse | SELLING_INTENDED_USE | — | ✅ |
| 71 | FinancialTradeRelationPEOSellingProductCategory | SELLING_PRODUCT_CATEGORY | — | ✅ |
| 72 | FinancialTradeRelationPEOSellingProductFiscClsf | SELLING_PRODUCT_FISC_CLSF | — | ✅ |
| 73 | FinancialTradeRelationPEOSellingThirdPtyRegId | SELLING_THIRD_PTY_REG_ID | — | ✅ |
| 74 | FinancialTradeRelationPEOSellingTrxBusinessCategory | SELLING_TRX_BUSINESS_CATEGORY | — | ✅ |
| 75 | FinancialTradeRelationPEOSellingUserDefinedFiscCls | SELLING_USER_DEFINED_FISC_CLS | — | ✅ |
| 76 | FinancialTradeRelationPEOSequenceNumber | SEQUENCE_NUMBER | — | ✅ |
| 77 | FinancialTradeRelationPEOTaRuleSetId | TA_RULE_SET_ID | — | ✅ |
| 78 | FinancialTradeRelationPEOToBuId | TO_BU_ID | — | ✅ |
| 79 | FinancialTradeRelationPEOToTradeOrg | TO_TRADE_ORG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
