---
id: DOC-OTHER-PVO-ContractClausesP
doc_type: system-doc
title: "ContractClausesP — PVO Cross-Module"
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
  - ContractClausesP
  - contractclausesp
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ContractClausesP

## 📌 Visão Geral

View Object para extração BICC de dados de Contract Clauses P. Acessa as tabelas: OKC_ARTICLES_ALL, OKC_ARTICLE_VERSIONS, OKC_K_ARTICLES_B (+1).

**Caminho:** `FscmTopModelAM.ContractsCoreAM.ContractClausesP`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 201 | 4 | 1 | 199 | 99% |

---

## 🔗 Tabelas Relacionadas

- [[okc_articles_all|OKC_ARTICLES_ALL]] — 26 atributos (26 BICC)
- [[okc_article_versions|OKC_ARTICLE_VERSIONS]] — 41 atributos (39 BICC)
- [[okc_k_articles_b|OKC_K_ARTICLES_B]] — 38 atributos (1 PKs, 38 BICC)
- [[okc_k_headers_all_b|OKC_K_HEADERS_ALL_B]] — 96 atributos (96 BICC)

---

## ⚙️ Atributos

### [[okc_articles_all|OKC_ARTICLES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ClausesArticleId | ARTICLE_ID | — | ✅ |
| 2 | ClausesArticleIntent | ARTICLE_INTENT | — | ✅ |
| 3 | ClausesArticleLanguage | ARTICLE_LANGUAGE | — | ✅ |
| 4 | ClausesArticleNumber | ARTICLE_NUMBER | — | ✅ |
| 5 | ClausesArticleTitle | ARTICLE_TITLE | — | ✅ |
| 6 | ClausesArticleType | ARTICLE_TYPE | — | ✅ |
| 7 | ClausesCreatedBy | CREATED_BY | — | ✅ |
| 8 | ClausesCreationDate | CREATION_DATE | — | ✅ |
| 9 | ClausesLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | ClausesLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | ClausesLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | ClausesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | ClausesOrgId | ORG_ID | — | ✅ |
| 14 | ClausesOrigSystemReferenceCode | ORIG_SYSTEM_REFERENCE_CODE | — | ✅ |
| 15 | ClausesOrigSystemReferenceId1 | ORIG_SYSTEM_REFERENCE_ID1 | — | ✅ |
| 16 | ClausesOrigSystemReferenceId2 | ORIG_SYSTEM_REFERENCE_ID2 | — | ✅ |
| 17 | ClausesProgramAppName | PROGRAM_APP_NAME | — | ✅ |
| 18 | ClausesProgramName | PROGRAM_NAME | — | ✅ |
| 19 | ClausesRequestId | REQUEST_ID | — | ✅ |
| 20 | ClausesStandardYn | STANDARD_YN | — | ✅ |
| 21 | ContractLibraryClauseArticleId | ARTICLE_ID | — | ✅ |
| 22 | ContractLibraryClauseArticleNumber | ARTICLE_NUMBER | — | ✅ |
| 23 | ContractLibraryClauseArticleTitle | ARTICLE_TITLE | — | ✅ |
| 24 | RefArticleContractLibClauseArticleId | ARTICLE_ID | — | ✅ |
| 25 | RefArticleContractLibClauseArticleNumber | ARTICLE_NUMBER | — | ✅ |
| 26 | RefArticleContractLibClauseArticleTitle | ARTICLE_TITLE | — | ✅ |

### [[okc_article_versions|OKC_ARTICLE_VERSIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ClausesVersionsAdditionalInstructions | ADDITIONAL_INSTRUCTIONS | — | ✅ |
| 2 | ClausesVersionsAdoptionType | ADOPTION_TYPE | — | ✅ |
| 3 | ClausesVersionsArticleDescription | ARTICLE_DESCRIPTION | — | ✅ |
| 4 | ClausesVersionsArticleId | ARTICLE_ID | — | ✅ |
| 5 | ClausesVersionsArticleLanguage | ARTICLE_LANGUAGE | — | ✅ |
| 6 | ClausesVersionsArticleStatus | ARTICLE_STATUS | — | ✅ |
| 7 | ClausesVersionsArticleText | ARTICLE_TEXT | — | — |
| 8 | ClausesVersionsArticleTextInWord | ARTICLE_TEXT_IN_WORD | — | — |
| 9 | ClausesVersionsArticleVersionId | ARTICLE_VERSION_ID | — | ✅ |
| 10 | ClausesVersionsArticleVersionNumber | ARTICLE_VERSION_NUMBER | — | ✅ |
| 11 | ClausesVersionsCreatedBy | CREATED_BY | — | ✅ |
| 12 | ClausesVersionsCreationDate | CREATION_DATE | — | ✅ |
| 13 | ClausesVersionsDateApproved | DATE_APPROVED | — | ✅ |
| 14 | ClausesVersionsDatePublished | DATE_PUBLISHED | — | ✅ |
| 15 | ClausesVersionsDefaultSection | DEFAULT_SECTION | — | ✅ |
| 16 | ClausesVersionsDisplayName | DISPLAY_NAME | — | ✅ |
| 17 | ClausesVersionsEditedInWord | EDITED_IN_WORD | — | ✅ |
| 18 | ClausesVersionsEndDate | END_DATE | — | ✅ |
| 19 | ClausesVersionsGlobalYn | GLOBAL_YN | — | ✅ |
| 20 | ClausesVersionsInsertByReference | INSERT_BY_REFERENCE | — | ✅ |
| 21 | ClausesVersionsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 22 | ClausesVersionsLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 23 | ClausesVersionsLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 24 | ClausesVersionsLockText | LOCK_TEXT | — | ✅ |
| 25 | ClausesVersionsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 26 | ClausesVersionsOrigSystemReferenceCode | ORIG_SYSTEM_REFERENCE_CODE | — | ✅ |
| 27 | ClausesVersionsOrigSystemReferenceId1 | ORIG_SYSTEM_REFERENCE_ID1 | — | ✅ |
| 28 | ClausesVersionsOrigSystemReferenceId2 | ORIG_SYSTEM_REFERENCE_ID2 | — | ✅ |
| 29 | ClausesVersionsProgramAppName | PROGRAM_APP_NAME | — | ✅ |
| 30 | ClausesVersionsProgramName | PROGRAM_NAME | — | ✅ |
| 31 | ClausesVersionsProvisionYn | PROVISION_YN | — | ✅ |
| 32 | ClausesVersionsReferenceSource | REFERENCE_SOURCE | — | ✅ |
| 33 | ClausesVersionsReferenceText | REFERENCE_TEXT | — | ✅ |
| 34 | ClausesVersionsRequestId | REQUEST_ID | — | ✅ |
| 35 | ClausesVersionsSavRelease | SAV_RELEASE | — | ✅ |
| 36 | ClausesVersionsSectionId | SECTION_ID | — | ✅ |
| 37 | ClausesVersionsStartDate | START_DATE | — | ✅ |
| 38 | ClausesVersionsStdArticleVersionId | STD_ARTICLE_VERSION_ID | — | ✅ |
| 39 | ClausesVersionsTaskId | TASK_ID | — | ✅ |
| 40 | ClausesVersionsTranslatedYn | TRANSLATED_YN | — | ✅ |
| 41 | ClausesVersionsVariationDescription | VARIATION_DESCRIPTION | — | ✅ |

### [[okc_k_articles_b|OKC_K_ARTICLES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractClauseAmendmentDescription | AMENDMENT_DESCRIPTION | — | ✅ |
| 2 | ContractClauseAmendmentOperationCode | AMENDMENT_OPERATION_CODE | — | ✅ |
| 3 | ContractClauseArticleVersionId | ARTICLE_VERSION_ID | — | ✅ |
| 4 | ContractClauseChangeNonstdYn | CHANGE_NONSTD_YN | — | ✅ |
| 5 | ContractClauseConditional | CONDITIONAL | — | ✅ |
| 6 | ContractClauseCreatedBy | CREATED_BY | — | ✅ |
| 7 | ContractClauseCreationDate | CREATION_DATE | — | ✅ |
| 8 | ContractClauseDisabled | DISABLED | — | ✅ |
| 9 | ContractClauseDisplaySequence | DISPLAY_SEQUENCE | — | ✅ |
| 10 | ContractClauseDocumentId | DOCUMENT_ID | — | ✅ |
| 11 | ContractClauseDocumentType | DOCUMENT_TYPE | — | ✅ |
| 12 | ContractClauseFulltextYn | FULLTEXT_YN | — | ✅ |
| 13 | ContractClauseId | ID | 🔑 | ✅ |
| 14 | ContractClauseLabel | LABEL | — | ✅ |
| 15 | ContractClauseLastAmendedBy | LAST_AMENDED_BY | — | ✅ |
| 16 | ContractClauseLastAmendmentDate | LAST_AMENDMENT_DATE | — | ✅ |
| 17 | ContractClauseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 18 | ContractClauseLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 19 | ContractClauseLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 20 | ContractClauseMajorVersion | MAJOR_VERSION | — | ✅ |
| 21 | ContractClauseMandatoryYn | MANDATORY_YN | — | ✅ |
| 22 | ContractClauseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 23 | ContractClauseOldId | OLD_ID | — | ✅ |
| 24 | ContractClauseOrigArticleId | ORIG_ARTICLE_ID | — | ✅ |
| 25 | ContractClauseOrigSystemReferenceCode | ORIG_SYSTEM_REFERENCE_CODE | — | ✅ |
| 26 | ContractClauseOrigSystemReferenceId1 | ORIG_SYSTEM_REFERENCE_ID1 | — | ✅ |
| 27 | ContractClauseOrigSystemReferenceId2 | ORIG_SYSTEM_REFERENCE_ID2 | — | ✅ |
| 28 | ContractClausePrintTextYn | PRINT_TEXT_YN | — | ✅ |
| 29 | ContractClauseRefArticleId | REF_ARTICLE_ID | — | ✅ |
| 30 | ContractClauseRefArticleVersionId | REF_ARTICLE_VERSION_ID | — | ✅ |
| 31 | ContractClauseSavSaeId | SAV_SAE_ID | — | ✅ |
| 32 | ContractClauseScnId | SCN_ID | — | ✅ |
| 33 | ContractClauseSecurityGroupId | SECURITY_GROUP_ID | — | ✅ |
| 34 | ContractClauseSkipNumbering | SKIP_NUMBERING | — | ✅ |
| 35 | ContractClauseSourceFlag | SOURCE_FLAG | — | ✅ |
| 36 | ContractClauseSummaryAmendOperationCode | SUMMARY_AMEND_OPERATION_CODE | — | ✅ |
| 37 | ContractClauseSuppressClauseTitlePrint | SUPPRESS_CLAUSE_TITLE_PRINT | — | ✅ |
| 38 | ContractClauseVersionType | VERSION_TYPE | — | ✅ |

### [[okc_k_headers_all_b|OKC_K_HEADERS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractHeaderAcctRuleId | ACCT_RULE_ID | — | ✅ |
| 2 | ContractHeaderAgreedAmount | AGREED_AMOUNT | — | ✅ |
| 3 | ContractHeaderAmendmentEffectiveDate | AMENDMENT_EFFECTIVE_DATE | — | ✅ |
| 4 | ContractHeaderApTermsId | AP_TERMS_ID | — | ✅ |
| 5 | ContractHeaderArInterfaceYn | AR_INTERFACE_YN | — | ✅ |
| 6 | ContractHeaderAutoReleaseInvoice | AUTO_RELEASE_INVOICE | — | ✅ |
| 7 | ContractHeaderBillSequence | BILL_SEQUENCE | — | ✅ |
| 8 | ContractHeaderBillToAcctId | BILL_TO_ACCT_ID | — | ✅ |
| 9 | ContractHeaderBillToSiteUseId | BILL_TO_SITE_USE_ID | — | ✅ |
| 10 | ContractHeaderBilledAtSource | BILLED_AT_SOURCE | — | ✅ |
| 11 | ContractHeaderBilltoLocationId | BILLTO_LOCATION_ID | — | ✅ |
| 12 | ContractHeaderBuyOrSell | BUY_OR_SELL | — | ✅ |
| 13 | ContractHeaderCancelledAmount | CANCELLED_AMOUNT | — | ✅ |
| 14 | ContractHeaderCommitmentId | COMMITMENT_ID | — | ✅ |
| 15 | ContractHeaderContractNumber | CONTRACT_NUMBER | — | ✅ |
| 16 | ContractHeaderContractNumberModifier | CONTRACT_NUMBER_MODIFIER | — | ✅ |
| 17 | ContractHeaderContractTypeId | CONTRACT_TYPE_ID | — | ✅ |
| 18 | ContractHeaderContributionPercent | CONTRIBUTION_PERCENT | — | ✅ |
| 19 | ContractHeaderCreatedBy | CREATED_BY | — | ✅ |
| 20 | ContractHeaderCreationDate | CREATION_DATE | — | ✅ |
| 21 | ContractHeaderCurrencyCode | CURRENCY_CODE | — | ✅ |
| 22 | ContractHeaderCustPoNumber | CUST_PO_NUMBER | — | ✅ |
| 23 | ContractHeaderCustPoNumberReqYn | CUST_PO_NUMBER_REQ_YN | — | ✅ |
| 24 | ContractHeaderDateApproved | DATE_APPROVED | — | ✅ |
| 25 | ContractHeaderDateNotified | DATE_NOTIFIED | — | ✅ |
| 26 | ContractHeaderDateSigned | DATE_SIGNED | — | ✅ |
| 27 | ContractHeaderDateTerminated | DATE_TERMINATED | — | ✅ |
| 28 | ContractHeaderDatetimeCancelled | DATETIME_CANCELLED | — | ✅ |
| 29 | ContractHeaderEndDate | END_DATE | — | ✅ |
| 30 | ContractHeaderEstimatedAmount | ESTIMATED_AMOUNT | — | ✅ |
| 31 | ContractHeaderExemptCertificateNumber | EXEMPT_CERTIFICATE_NUMBER | — | ✅ |
| 32 | ContractHeaderExemptReasonCode | EXEMPT_REASON_CODE | — | ✅ |
| 33 | ContractHeaderFob | FOB | — | ✅ |
| 34 | ContractHeaderFreightTerms | FREIGHT_TERMS | — | ✅ |
| 35 | ContractHeaderHoldBilling | HOLD_BILLING | — | ✅ |
| 36 | ContractHeaderHoldReasonCode | HOLD_REASON_CODE | — | ✅ |
| 37 | ContractHeaderHoldUntilDate | HOLD_UNTIL_DATE | — | ✅ |
| 38 | ContractHeaderId | ID | — | ✅ |
| 39 | ContractHeaderInvConvRateDate | INV_CONV_RATE_DATE | — | ✅ |
| 40 | ContractHeaderInvConvRateDateType | INV_CONV_RATE_DATE_TYPE | — | ✅ |
| 41 | ContractHeaderInvConvRateType | INV_CONV_RATE_TYPE | — | ✅ |
| 42 | ContractHeaderInvOrganizationId | INV_ORGANIZATION_ID | — | ✅ |
| 43 | ContractHeaderInvPrintProfile | INV_PRINT_PROFILE | — | ✅ |
| 44 | ContractHeaderInvRuleId | INV_RULE_ID | — | ✅ |
| 45 | ContractHeaderInvTrxTypeId | INV_TRX_TYPE_ID | — | ✅ |
| 46 | ContractHeaderLastRevRecogDate | LAST_REV_RECOG_DATE | — | ✅ |
| 47 | ContractHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 48 | ContractHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 49 | ContractHeaderLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 50 | ContractHeaderLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 51 | ContractHeaderLineAutonumberEnabledFlag | LINE_AUTONUMBER_ENABLED_FLAG | — | ✅ |
| 52 | ContractHeaderMajorVersion | MAJOR_VERSION | — | ✅ |
| 53 | ContractHeaderNetInvoiceFlag | NET_INVOICE_FLAG | — | ✅ |
| 54 | ContractHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 55 | ContractHeaderOrderId | ORDER_ID | — | ✅ |
| 56 | ContractHeaderOrderNumber | ORDER_NUMBER | — | ✅ |
| 57 | ContractHeaderOrgId | ORG_ID | — | ✅ |
| 58 | ContractHeaderOrigSystemId1 | ORIG_SYSTEM_ID1 | — | ✅ |
| 59 | ContractHeaderOrigSystemReference1 | ORIG_SYSTEM_REFERENCE1 | — | ✅ |
| 60 | ContractHeaderOrigSystemSourceCode | ORIG_SYSTEM_SOURCE_CODE | — | ✅ |
| 61 | ContractHeaderOutputTaxClassificationCode | OUTPUT_TAX_CLASSIFICATION_CODE | — | ✅ |
| 62 | ContractHeaderOverallRiskCode | OVERALL_RISK_CODE | — | ✅ |
| 63 | ContractHeaderOwningOrgId | OWNING_ORG_ID | — | ✅ |
| 64 | ContractHeaderPaymentInstructionType | PAYMENT_INSTRUCTION_TYPE | — | ✅ |
| 65 | ContractHeaderPaymentTermId | PAYMENT_TERM_ID | — | ✅ |
| 66 | ContractHeaderPaymentType | PAYMENT_TYPE | — | ✅ |
| 67 | ContractHeaderPriceListId | PRICE_LIST_ID | — | ✅ |
| 68 | ContractHeaderPrimaryEntPartyId | PRIMARY_ENT_PARTY_ID | — | ✅ |
| 69 | ContractHeaderProgramAppName | PROGRAM_APP_NAME | — | ✅ |
| 70 | ContractHeaderProgramName | PROGRAM_NAME | — | ✅ |
| 71 | ContractHeaderQclId | QCL_ID | — | ✅ |
| 72 | ContractHeaderRecvInvOrgId | RECV_INV_ORG_ID | — | ✅ |
| 73 | ContractHeaderRequestId | REQUEST_ID | — | ✅ |
| 74 | ContractHeaderRevConvRateType | REV_CONV_RATE_TYPE | — | ✅ |
| 75 | ContractHeaderShipInvOrgId | SHIP_INV_ORG_ID | — | ✅ |
| 76 | ContractHeaderShipToAcctId | SHIP_TO_ACCT_ID | — | ✅ |
| 77 | ContractHeaderShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | ✅ |
| 78 | ContractHeaderShiptoLocationId | SHIPTO_LOCATION_ID | — | ✅ |
| 79 | ContractHeaderSoldToAcctId | SOLD_TO_ACCT_ID | — | ✅ |
| 80 | ContractHeaderSoldToSiteId | SOLD_TO_SITE_ID | — | ✅ |
| 81 | ContractHeaderStartDate | START_DATE | — | ✅ |
| 82 | ContractHeaderStateTransitionFlowName | STATE_TRANSITION_FLOW_NAME | — | ✅ |
| 83 | ContractHeaderStateTransitionFlowState | STATE_TRANSITION_FLOW_STATE | — | ✅ |
| 84 | ContractHeaderStsCode | STS_CODE | — | ✅ |
| 85 | ContractHeaderSummaryTrxYn | SUMMARY_TRX_YN | — | ✅ |
| 86 | ContractHeaderSupplierId | SUPPLIER_ID | — | ✅ |
| 87 | ContractHeaderSupplierSiteId | SUPPLIER_SITE_ID | — | ✅ |
| 88 | ContractHeaderTaskId | TASK_ID | — | ✅ |
| 89 | ContractHeaderTaxAmount | TAX_AMOUNT | — | ✅ |
| 90 | ContractHeaderTaxExemptionControl | TAX_EXEMPTION_CONTROL | — | ✅ |
| 91 | ContractHeaderTemplateUsed | TEMPLATE_USED | — | ✅ |
| 92 | ContractHeaderTemplateYn | TEMPLATE_YN | — | ✅ |
| 93 | ContractHeaderTermCancelSource | TERM_CANCEL_SOURCE | — | ✅ |
| 94 | ContractHeaderTrnCode | TRN_CODE | — | ✅ |
| 95 | ContractHeaderUserStatusCode | USER_STATUS_CODE | — | ✅ |
| 96 | ContractHeaderVersionType | VERSION_TYPE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
