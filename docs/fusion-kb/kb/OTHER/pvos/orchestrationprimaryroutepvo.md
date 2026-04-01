---
id: DOC-OTHER-PVO-OrchestrationPrimaryRoutePVO
doc_type: system-doc
title: "OrchestrationPrimaryRoutePVO — PVO Cross-Module"
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
  - OrchestrationPrimaryRoutePVO
  - orchestrationprimaryroutepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# OrchestrationPrimaryRoutePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Orchestration Primary Route. Acessa as tabelas: FOS_AGREEMENT_FTR_F, FOS_AGREEMENT_PTR_F, FUN_ALL_BUSINESS_UNITS_V.

**Caminho:** `FscmTopModelAM.FosOrchestrationProcessAM.OrchestrationPrimaryRoutePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 70 | 3 | 4 | 70 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fos_agreement_ftr_f|FOS_AGREEMENT_FTR_F]] — 44 atributos (1 PKs, 44 BICC)
- [[fos_agreement_ptr_f|FOS_AGREEMENT_PTR_F]] — 18 atributos (3 PKs, 18 BICC)
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 8 atributos (8 BICC)

---

## ⚙️ Atributos

### [[fos_agreement_ftr_f|FOS_AGREEMENT_FTR_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AgreementFTRPEOAgreementFtrId | AGREEMENT_FTR_ID | 🔑 | ✅ |
| 2 | AgreementFTRPEOAgreementId | AGREEMENT_ID | — | ✅ |
| 3 | AgreementFTRPEOAgreementPtrId | AGREEMENT_PTR_ID | — | ✅ |
| 4 | AgreementFTRPEOBuyingDefaultTxtCountry | BUYING_DEFAULT_TXT_COUNTRY | — | ✅ |
| 5 | AgreementFTRPEOBuyingDocumentSubType | BUYING_DOCUMENT_SUB_TYPE | — | ✅ |
| 6 | AgreementFTRPEOBuyingFirstPtyRegId | BUYING_FIRST_PTY_REG_ID | — | ✅ |
| 7 | AgreementFTRPEOBuyingIntendedUse | BUYING_INTENDED_USE | — | ✅ |
| 8 | AgreementFTRPEOBuyingProductCategory | BUYING_PRODUCT_CATEGORY | — | ✅ |
| 9 | AgreementFTRPEOBuyingProductFiscClsf | BUYING_PRODUCT_FISC_CLSF | — | ✅ |
| 10 | AgreementFTRPEOBuyingThirdPtyRegId | BUYING_THIRD_PTY_REG_ID | — | ✅ |
| 11 | AgreementFTRPEOBuyingTrxBusinessCategory | BUYING_TRX_BUSINESS_CATEGORY | — | ✅ |
| 12 | AgreementFTRPEOBuyingUserDefinedFiscCls | BUYING_USER_DEFINED_FISC_CLS | — | ✅ |
| 13 | AgreementFTRPEOCreatedBy | CREATED_BY | — | ✅ |
| 14 | AgreementFTRPEOCreationDate | CREATION_DATE | — | ✅ |
| 15 | AgreementFTRPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 16 | AgreementFTRPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 17 | AgreementFTRPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 18 | AgreementFTRPEOFromBuId | FROM_BU_ID | — | ✅ |
| 19 | AgreementFTRPEOFromTradeOrg | FROM_TRADE_ORG | — | ✅ |
| 20 | AgreementFTRPEOIncotermLocation | INCOTERM_LOCATION | — | ✅ |
| 21 | AgreementFTRPEOIncoterms | INCOTERMS | — | ✅ |
| 22 | AgreementFTRPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 23 | AgreementFTRPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 24 | AgreementFTRPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 25 | AgreementFTRPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 26 | AgreementFTRPEOOcFwdEventDefId | OC_FWD_EVENT_DEF_ID | — | ✅ |
| 27 | AgreementFTRPEOOcRetEventDefId | OC_RET_EVENT_DEF_ID | — | ✅ |
| 28 | AgreementFTRPEOPaymentTermId | PAYMENT_TERM_ID | — | ✅ |
| 29 | AgreementFTRPEOPricingId | PRICING_ID | — | ✅ |
| 30 | AgreementFTRPEOReceivablesCreditMemoType | RECEIVABLES_CREDIT_MEMO_TYPE | — | ✅ |
| 31 | AgreementFTRPEOReceivablesInvoiceType | RECEIVABLES_INVOICE_TYPE | — | ✅ |
| 32 | AgreementFTRPEOSellingDefaultTxtCountry | SELLING_DEFAULT_TXT_COUNTRY | — | ✅ |
| 33 | AgreementFTRPEOSellingDocumentSubType | SELLING_DOCUMENT_SUB_TYPE | — | ✅ |
| 34 | AgreementFTRPEOSellingFirstPtyRegId | SELLING_FIRST_PTY_REG_ID | — | ✅ |
| 35 | AgreementFTRPEOSellingIntendedUse | SELLING_INTENDED_USE | — | ✅ |
| 36 | AgreementFTRPEOSellingProductCategory | SELLING_PRODUCT_CATEGORY | — | ✅ |
| 37 | AgreementFTRPEOSellingProductFiscClsf | SELLING_PRODUCT_FISC_CLSF | — | ✅ |
| 38 | AgreementFTRPEOSellingThirdPtyRegId | SELLING_THIRD_PTY_REG_ID | — | ✅ |
| 39 | AgreementFTRPEOSellingTrxBusinessCategory | SELLING_TRX_BUSINESS_CATEGORY | — | ✅ |
| 40 | AgreementFTRPEOSellingUserDefinedFiscCls | SELLING_USER_DEFINED_FISC_CLS | — | ✅ |
| 41 | AgreementFTRPEOSequenceNumber | SEQUENCE_NUMBER | — | ✅ |
| 42 | AgreementFTRPEOTaRuleSetId | TA_RULE_SET_ID | — | ✅ |
| 43 | AgreementFTRPEOToBuId | TO_BU_ID | — | ✅ |
| 44 | AgreementFTRPEOToTradeOrg | TO_TRADE_ORG | — | ✅ |

### [[fos_agreement_ptr_f|FOS_AGREEMENT_PTR_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AgreementPTRPEOAgreementId | AGREEMENT_ID | — | ✅ |
| 2 | AgreementPTRPEOAgreementPtrId | AGREEMENT_PTR_ID | 🔑 | ✅ |
| 3 | AgreementPTRPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | AgreementPTRPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | AgreementPTRPEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 6 | AgreementPTRPEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 7 | AgreementPTRPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 8 | AgreementPTRPEOFromBuId | FROM_BU_ID | — | ✅ |
| 9 | AgreementPTRPEOFromLeId | FROM_LE_ID | — | ✅ |
| 10 | AgreementPTRPEOFromTradeOrganizationId | FROM_TRADE_ORGANIZATION_ID | — | ✅ |
| 11 | AgreementPTRPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | AgreementPTRPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | AgreementPTRPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | AgreementPTRPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 15 | AgreementPTRPEOPtrNumber | PTR_NUMBER | — | ✅ |
| 16 | AgreementPTRPEOToBuId | TO_BU_ID | — | ✅ |
| 17 | AgreementPTRPEOToLeId | TO_LE_ID | — | ✅ |
| 18 | AgreementPTRPEOToTradeOrganizationId | TO_TRADE_ORGANIZATION_ID | — | ✅ |

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitPEOFtrBuyingBuId | BU_ID | — | ✅ |
| 2 | BusinessUnitPEOFtrBuyingBuName | BU_NAME | — | ✅ |
| 3 | BusinessUnitPEOFtrSellingBuId | BU_ID | — | ✅ |
| 4 | BusinessUnitPEOFtrSellingBuName | BU_NAME | — | ✅ |
| 5 | BusinessUnitPEOPtrBuyingBuId | BU_ID | — | ✅ |
| 6 | BusinessUnitPEOPtrBuyingBuName | BU_NAME | — | ✅ |
| 7 | BusinessUnitPEOPtrSellingBuId | BU_ID | — | ✅ |
| 8 | BusinessUnitPEOPtrSellingBuName | BU_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
