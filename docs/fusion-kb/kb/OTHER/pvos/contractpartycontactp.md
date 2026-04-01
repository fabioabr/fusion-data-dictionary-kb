---
id: DOC-OTHER-PVO-ContractPartyContactP
doc_type: system-doc
title: "ContractPartyContactP — PVO Cross-Module"
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
  - ContractPartyContactP
  - contractpartycontactp
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ContractPartyContactP

## 📌 Visão Geral

View Object para extração BICC de dados de Contract Party Contact P. Acessa as tabelas: HR_ALL_ORGANIZATION_UNITS_F_VL, HZ_PARTIES, OKC_CONTACTS (+1).

**Caminho:** `FscmTopModelAM.ContractsCoreAM.ContractPartyContactP`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 130 | 4 | 2 | 24 | 18% |

---

## 🔗 Tabelas Relacionadas

- [[hr_all_organization_units_f_vl|HR_ALL_ORGANIZATION_UNITS_F_VL]] — 5 atributos (1 BICC)
- [[hz_parties|HZ_PARTIES]] — 7 atributos
- [[okc_contacts|OKC_CONTACTS]] — 20 atributos (1 PKs, 20 BICC)
- [[okc_k_headers_all_b|OKC_K_HEADERS_ALL_B]] — 98 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[hr_all_organization_units_f_vl|HR_ALL_ORGANIZATION_UNITS_F_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrganizationUnitEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | OrganizationUnitEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | OrganizationUnitName | NAME | — | — |
| 4 | OrganizationUnitObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 5 | OrganizationUnitOrganizationId | ORGANIZATION_ID | — | — |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyPartyId | PARTY_ID | — | — |
| 2 | PartyPartyName | PARTY_NAME | — | — |
| 3 | RelPartyEmailAddress | EMAIL_ADDRESS | — | — |
| 4 | RelPartyId | PARTY_ID | — | — |
| 5 | RelPartyName | PARTY_NAME | — | — |
| 6 | RelPartyObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | ResPartyEmailAddress | EMAIL_ADDRESS | — | — |

### [[okc_contacts|OKC_CONTACTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractPartyContactContactSequence | CONTACT_SEQUENCE | — | ✅ |
| 2 | ContractPartyContactCplId | CPL_ID | — | ✅ |
| 3 | ContractPartyContactCreatedBy | CREATED_BY | — | ✅ |
| 4 | ContractPartyContactCreationDate | CREATION_DATE | — | ✅ |
| 5 | ContractPartyContactCroCode | CRO_CODE | — | ✅ |
| 6 | ContractPartyContactDnzChrId | DNZ_CHR_ID | — | ✅ |
| 7 | ContractPartyContactEndDate | END_DATE | — | ✅ |
| 8 | ContractPartyContactId | ID | 🔑 | ✅ |
| 9 | ContractPartyContactJtotObject1Code | JTOT_OBJECT1_CODE | — | ✅ |
| 10 | ContractPartyContactLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | ContractPartyContactLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | ContractPartyContactLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | ContractPartyContactMajorVersion | MAJOR_VERSION | — | ✅ |
| 14 | ContractPartyContactObject1Id1 | OBJECT1_ID1 | — | ✅ |
| 15 | ContractPartyContactObject1Id2 | OBJECT1_ID2 | — | ✅ |
| 16 | ContractPartyContactObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 17 | ContractPartyContactOwnerYn | OWNER_YN | — | ✅ |
| 18 | ContractPartyContactSignerYn | SIGNER_YN | — | ✅ |
| 19 | ContractPartyContactStartDate | START_DATE | — | ✅ |
| 20 | ContractPartyContactVersionType | VERSION_TYPE | — | ✅ |

### [[okc_k_headers_all_b|OKC_K_HEADERS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractHeaderAcctRuleId | ACCT_RULE_ID | — | — |
| 2 | ContractHeaderAgreedAmount | AGREED_AMOUNT | — | — |
| 3 | ContractHeaderAmendmentEffectiveDate | AMENDMENT_EFFECTIVE_DATE | — | — |
| 4 | ContractHeaderApTermsId | AP_TERMS_ID | — | — |
| 5 | ContractHeaderArInterfaceYn | AR_INTERFACE_YN | — | — |
| 6 | ContractHeaderAutoReleaseInvoice | AUTO_RELEASE_INVOICE | — | — |
| 7 | ContractHeaderBaseContractYn | BASE_CONTRACT_YN | — | — |
| 8 | ContractHeaderBillSequence | BILL_SEQUENCE | — | — |
| 9 | ContractHeaderBillToAcctId | BILL_TO_ACCT_ID | — | — |
| 10 | ContractHeaderBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 11 | ContractHeaderBilledAtSource | BILLED_AT_SOURCE | — | — |
| 12 | ContractHeaderBilltoLocationId | BILLTO_LOCATION_ID | — | — |
| 13 | ContractHeaderBuyOrSell | BUY_OR_SELL | — | — |
| 14 | ContractHeaderCancelledAmount | CANCELLED_AMOUNT | — | — |
| 15 | ContractHeaderCarrierId | CARRIER_ID | — | — |
| 16 | ContractHeaderCommitmentId | COMMITMENT_ID | — | — |
| 17 | ContractHeaderContractNumber | CONTRACT_NUMBER | — | — |
| 18 | ContractHeaderContractNumberModifier | CONTRACT_NUMBER_MODIFIER | — | — |
| 19 | ContractHeaderContractTypeId | CONTRACT_TYPE_ID | — | — |
| 20 | ContractHeaderContributionPercent | CONTRIBUTION_PERCENT | — | — |
| 21 | ContractHeaderCreatedBy | CREATED_BY | — | — |
| 22 | ContractHeaderCreationDate | CREATION_DATE | — | — |
| 23 | ContractHeaderCurrencyCode | CURRENCY_CODE | — | — |
| 24 | ContractHeaderCustPoNumber | CUST_PO_NUMBER | — | — |
| 25 | ContractHeaderCustPoNumberReqYn | CUST_PO_NUMBER_REQ_YN | — | — |
| 26 | ContractHeaderDateApproved | DATE_APPROVED | — | — |
| 27 | ContractHeaderDateNotified | DATE_NOTIFIED | — | — |
| 28 | ContractHeaderDateSigned | DATE_SIGNED | — | — |
| 29 | ContractHeaderDateTerminated | DATE_TERMINATED | — | — |
| 30 | ContractHeaderDatetimeCancelled | DATETIME_CANCELLED | — | — |
| 31 | ContractHeaderEndDate | END_DATE | — | — |
| 32 | ContractHeaderEstimatedAmount | ESTIMATED_AMOUNT | — | — |
| 33 | ContractHeaderExemptCertificateNumber | EXEMPT_CERTIFICATE_NUMBER | — | — |
| 34 | ContractHeaderExemptReasonCode | EXEMPT_REASON_CODE | — | — |
| 35 | ContractHeaderFob | FOB | — | — |
| 36 | ContractHeaderFreightTerms | FREIGHT_TERMS | — | — |
| 37 | ContractHeaderHoldBilling | HOLD_BILLING | — | — |
| 38 | ContractHeaderHoldReasonCode | HOLD_REASON_CODE | — | — |
| 39 | ContractHeaderHoldUntilDate | HOLD_UNTIL_DATE | — | — |
| 40 | ContractHeaderId | ID | — | — |
| 41 | ContractHeaderInvConvRateDate | INV_CONV_RATE_DATE | — | — |
| 42 | ContractHeaderInvConvRateDateType | INV_CONV_RATE_DATE_TYPE | — | — |
| 43 | ContractHeaderInvConvRateType | INV_CONV_RATE_TYPE | — | — |
| 44 | ContractHeaderInvOrganizationId | INV_ORGANIZATION_ID | — | — |
| 45 | ContractHeaderInvPrintProfile | INV_PRINT_PROFILE | — | — |
| 46 | ContractHeaderInvRuleId | INV_RULE_ID | — | — |
| 47 | ContractHeaderInvTrxTypeId | INV_TRX_TYPE_ID | — | — |
| 48 | ContractHeaderLastRevRecogDate | LAST_REV_RECOG_DATE | — | — |
| 49 | ContractHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 50 | ContractHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 51 | ContractHeaderLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 52 | ContractHeaderLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 53 | ContractHeaderLineAutonumberEnabledFlag | LINE_AUTONUMBER_ENABLED_FLAG | — | — |
| 54 | ContractHeaderMajorVersion | MAJOR_VERSION | 🔑 | ✅ |
| 55 | ContractHeaderNetInvoiceFlag | NET_INVOICE_FLAG | — | — |
| 56 | ContractHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 57 | ContractHeaderOrderId | ORDER_ID | — | — |
| 58 | ContractHeaderOrderNumber | ORDER_NUMBER | — | — |
| 59 | ContractHeaderOrgId | ORG_ID | — | — |
| 60 | ContractHeaderOrigSystemId1 | ORIG_SYSTEM_ID1 | — | — |
| 61 | ContractHeaderOrigSystemReference1 | ORIG_SYSTEM_REFERENCE1 | — | — |
| 62 | ContractHeaderOrigSystemSourceCode | ORIG_SYSTEM_SOURCE_CODE | — | — |
| 63 | ContractHeaderOutputTaxClassificationCode | OUTPUT_TAX_CLASSIFICATION_CODE | — | — |
| 64 | ContractHeaderOverallRiskCode | OVERALL_RISK_CODE | — | — |
| 65 | ContractHeaderOwningOrgId | OWNING_ORG_ID | — | — |
| 66 | ContractHeaderPaymentInstructionType | PAYMENT_INSTRUCTION_TYPE | — | — |
| 67 | ContractHeaderPaymentTermId | PAYMENT_TERM_ID | — | — |
| 68 | ContractHeaderPaymentType | PAYMENT_TYPE | — | — |
| 69 | ContractHeaderPriceListId | PRICE_LIST_ID | — | — |
| 70 | ContractHeaderPrimaryEntPartyId | PRIMARY_ENT_PARTY_ID | — | — |
| 71 | ContractHeaderProgramAppName | PROGRAM_APP_NAME | — | — |
| 72 | ContractHeaderProgramName | PROGRAM_NAME | — | — |
| 73 | ContractHeaderQclId | QCL_ID | — | — |
| 74 | ContractHeaderRecvInvOrgId | RECV_INV_ORG_ID | — | — |
| 75 | ContractHeaderRequestId | REQUEST_ID | — | — |
| 76 | ContractHeaderRevConvRateType | REV_CONV_RATE_TYPE | — | — |
| 77 | ContractHeaderShipInvOrgId | SHIP_INV_ORG_ID | — | — |
| 78 | ContractHeaderShipToAcctId | SHIP_TO_ACCT_ID | — | — |
| 79 | ContractHeaderShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 80 | ContractHeaderShiptoLocationId | SHIPTO_LOCATION_ID | — | — |
| 81 | ContractHeaderSoldToAcctId | SOLD_TO_ACCT_ID | — | — |
| 82 | ContractHeaderSoldToSiteId | SOLD_TO_SITE_ID | — | — |
| 83 | ContractHeaderStartDate | START_DATE | — | — |
| 84 | ContractHeaderStateTransitionFlowName | STATE_TRANSITION_FLOW_NAME | — | — |
| 85 | ContractHeaderStateTransitionFlowState | STATE_TRANSITION_FLOW_STATE | — | — |
| 86 | ContractHeaderStsCode | STS_CODE | — | — |
| 87 | ContractHeaderSummaryTrxYn | SUMMARY_TRX_YN | — | — |
| 88 | ContractHeaderSupplierId | SUPPLIER_ID | — | — |
| 89 | ContractHeaderSupplierSiteId | SUPPLIER_SITE_ID | — | — |
| 90 | ContractHeaderTaskId | TASK_ID | — | — |
| 91 | ContractHeaderTaxAmount | TAX_AMOUNT | — | — |
| 92 | ContractHeaderTaxExemptionControl | TAX_EXEMPTION_CONTROL | — | — |
| 93 | ContractHeaderTemplateUsed | TEMPLATE_USED | — | — |
| 94 | ContractHeaderTemplateYn | TEMPLATE_YN | — | — |
| 95 | ContractHeaderTermCancelSource | TERM_CANCEL_SOURCE | — | — |
| 96 | ContractHeaderTrnCode | TRN_CODE | — | — |
| 97 | ContractHeaderUserStatusCode | USER_STATUS_CODE | — | — |
| 98 | ContractHeaderVersionType | VERSION_TYPE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
