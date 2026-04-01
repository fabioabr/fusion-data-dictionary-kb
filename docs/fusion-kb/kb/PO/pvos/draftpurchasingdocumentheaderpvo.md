---
id: DOC-PO-PVO-DraftPurchasingDocumentHeaderPVO
doc_type: system-doc
title: "DraftPurchasingDocumentHeaderPVO — PVO Purchasing"
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
  - DraftPurchasingDocumentHeaderPVO
  - draftpurchasingdocumentheaderpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DraftPurchasingDocumentHeaderPVO

## 📌 Visão Geral

Disponibiliza cabeçalhos de rascunhos de documentos de compra para consulta operacional, com dados de fornecedor, estilo e vínculo com documentos ativos. Suporta acompanhamento de pedidos em fase de preparação.

**Caminho:** `FscmTopModelAM.PrcPoPublicViewAM.DraftPurchasingDocumentHeaderPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 542 | 5 | 1 | 52 | 10% |

---

## 🔗 Tabelas Relacionadas

- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 6 atributos
- [[po_doc_style_headers|PO_DOC_STYLE_HEADERS]] — 18 atributos (1 BICC)
- [[po_headers_all|PO_HEADERS_ALL]] — 364 atributos (20 BICC)
- [[po_headers_draft_all|PO_HEADERS_DRAFT_ALL]] — 118 atributos (1 PKs, 25 BICC)
- [[po_versions_unprocessed_v|PO_VERSIONS_UNPROCESSED_V]] — 36 atributos (6 BICC)

---

## ⚙️ Atributos

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 4 | OverridingApproverDisplayName | DISPLAY_NAME | — | — |
| 5 | OverridingApproverListName | LIST_NAME | — | — |
| 6 | PersonNameId | PERSON_NAME_ID | — | — |

### [[po_doc_style_headers|PO_DOC_STYLE_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DocStyleAdvancesFlag | ADVANCES_FLAG | — | — |
| 2 | DocStyleContractFinancingFlag | CONTRACT_FINANCING_FLAG | — | — |
| 3 | DocStyleCreatedBy | CREATED_BY | — | — |
| 4 | DocStyleCreationDate | CREATION_DATE | — | — |
| 5 | DocStyleLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | DocStyleLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | DocStyleLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | DocStyleLineTypeAllowed | LINE_TYPE_ALLOWED | — | — |
| 9 | DocStyleObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | DocStylePriceBreaksFlag | PRICE_BREAKS_FLAG | — | — |
| 11 | DocStylePriceDifferentialsFlag | PRICE_DIFFERENTIALS_FLAG | — | — |
| 12 | DocStyleProgressPaymentFlag | PROGRESS_PAYMENT_FLAG | — | — |
| 13 | DocStyleRetainageFlag | RETAINAGE_FLAG | — | — |
| 14 | DocStyleStatus | STATUS | — | — |
| 15 | DocStyleStyleDescription | STYLE_DESCRIPTION | — | — |
| 16 | DocStyleStyleId | STYLE_ID | — | — |
| 17 | DocStyleStyleName | STYLE_NAME | — | — |
| 18 | DocStyleStyleType | STYLE_TYPE | — | — |

### [[po_headers_all|PO_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FromPOHeaderAcceptanceDueDate | ACCEPTANCE_DUE_DATE | — | — |
| 2 | FromPOHeaderAcceptanceRequiredFlag | ACCEPTANCE_REQUIRED_FLAG | — | — |
| 3 | FromPOHeaderAcceptanceWithinDays | ACCEPTANCE_WITHIN_DAYS | — | — |
| 4 | FromPOHeaderAgentId | AGENT_ID | — | — |
| 5 | FromPOHeaderAmountLimit | AMOUNT_LIMIT | — | — |
| 6 | FromPOHeaderAmountReleased | AMOUNT_RELEASED | — | — |
| 7 | FromPOHeaderApprovedDate | APPROVED_DATE | — | — |
| 8 | FromPOHeaderApprovedFlag | APPROVED_FLAG | — | — |
| 9 | FromPOHeaderAutoSourcingFlag | AUTO_SOURCING_FLAG | — | — |
| 10 | FromPOHeaderBillToLocationId | BILL_TO_LOCATION_ID | — | — |
| 11 | FromPOHeaderBilltoBuId | BILLTO_BU_ID | — | — |
| 12 | FromPOHeaderBlanketTotalAmount | BLANKET_TOTAL_AMOUNT | — | — |
| 13 | FromPOHeaderBudgetControlEnabledFlag | BUDGET_CONTROL_ENABLED_FLAG | — | — |
| 14 | FromPOHeaderCancelFlag | CANCEL_FLAG | — | — |
| 15 | FromPOHeaderCarrierId | CARRIER_ID | — | — |
| 16 | FromPOHeaderCatAdminAuthEnabledFlag | CAT_ADMIN_AUTH_ENABLED_FLAG | — | — |
| 17 | FromPOHeaderCbcAccountingDate | CBC_ACCOUNTING_DATE | — | — |
| 18 | FromPOHeaderChangeRequestedBy | CHANGE_REQUESTED_BY | — | — |
| 19 | FromPOHeaderChangeSummary | CHANGE_SUMMARY | — | — |
| 20 | FromPOHeaderClosedDate | CLOSED_DATE | — | — |
| 21 | FromPOHeaderComments | COMMENTS | — | — |
| 22 | FromPOHeaderConfirmingOrderFlag | CONFIRMING_ORDER_FLAG | — | — |
| 23 | FromPOHeaderConsignedConsumptionFlag | CONSIGNED_CONSUMPTION_FLAG | — | — |
| 24 | FromPOHeaderConsumeReqDemandFlag | CONSUME_REQ_DEMAND_FLAG | — | — |
| 25 | FromPOHeaderContermsArticlesUpdDate | CONTERMS_ARTICLES_UPD_DATE | — | — |
| 26 | FromPOHeaderContermsDelivUpdDate | CONTERMS_DELIV_UPD_DATE | — | — |
| 27 | FromPOHeaderContermsExistFlag | CONTERMS_EXIST_FLAG | — | — |
| 28 | FromPOHeaderCpaReference | CPA_REFERENCE | — | — |
| 29 | FromPOHeaderCreatedBy | CREATED_BY | — | — |
| 30 | FromPOHeaderCreatedLanguage | CREATED_LANGUAGE | — | — |
| 31 | FromPOHeaderCreationDate | CREATION_DATE | — | — |
| 32 | FromPOHeaderCurrencyCode | CURRENCY_CODE | — | — |
| 33 | FromPOHeaderCurrentVersionId | CURRENT_VERSION_ID | — | — |
| 34 | FromPOHeaderDefaultPoTradeOrgId | DEFAULT_PO_TRADE_ORG_ID | — | — |
| 35 | FromPOHeaderDefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | — |
| 36 | FromPOHeaderDocumentCreationMethod | DOCUMENT_CREATION_METHOD | — | — |
| 37 | FromPOHeaderDocumentStatus | DOCUMENT_STATUS | — | — |
| 38 | FromPOHeaderEdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 39 | FromPOHeaderEdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 40 | FromPOHeaderEmailAddress | EMAIL_ADDRESS | — | — |
| 41 | FromPOHeaderEnabledFlag | ENABLED_FLAG | — | — |
| 42 | FromPOHeaderEncumbranceRequiredFlag | ENCUMBRANCE_REQUIRED_FLAG | — | — |
| 43 | FromPOHeaderEndDate | END_DATE | — | — |
| 44 | FromPOHeaderFax | FAX | — | — |
| 45 | FromPOHeaderFirmDate | FIRM_DATE | — | — |
| 46 | FromPOHeaderFirmStatusLookupCode | FIRM_STATUS_LOOKUP_CODE | — | — |
| 47 | FromPOHeaderFobLookupCode | FOB_LOOKUP_CODE | — | — |
| 48 | FromPOHeaderFreightTermsLookupCode | FREIGHT_TERMS_LOOKUP_CODE | — | — |
| 49 | FromPOHeaderFromHeaderId | FROM_HEADER_ID | — | — |
| 50 | FromPOHeaderFromTypeLookupCode | FROM_TYPE_LOOKUP_CODE | — | — |
| 51 | FromPOHeaderFrozenFlag | FROZEN_FLAG | — | — |
| 52 | FromPOHeaderFundsStatus | FUNDS_STATUS | — | — |
| 53 | FromPOHeaderGenerateOrdersAutomatic | GENERATE_ORDERS_AUTOMATIC | — | — |
| 54 | FromPOHeaderGovernmentContext | GOVERNMENT_CONTEXT | — | — |
| 55 | FromPOHeaderGroupRequisitionLines | GROUP_REQUISITION_LINES | — | — |
| 56 | FromPOHeaderGroupRequisitions | GROUP_REQUISITIONS | — | — |
| 57 | FromPOHeaderInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | — |
| 58 | FromPOHeaderJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 59 | FromPOHeaderJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 60 | FromPOHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 61 | FromPOHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 62 | FromPOHeaderLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 63 | FromPOHeaderLastUpdatedProgram | LAST_UPDATED_PROGRAM | — | — |
| 64 | FromPOHeaderMinReleaseAmount | MIN_RELEASE_AMOUNT | — | — |
| 65 | FromPOHeaderModeOfTransport | MODE_OF_TRANSPORT | — | — |
| 66 | FromPOHeaderNoteToAuthorizer | NOTE_TO_AUTHORIZER | — | — |
| 67 | FromPOHeaderNoteToReceiver | NOTE_TO_RECEIVER | — | — |
| 68 | FromPOHeaderNoteToVendor | NOTE_TO_VENDOR | — | — |
| 69 | FromPOHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 70 | FromPOHeaderOrchestrationOrderFlag | ORCHESTRATION_ORDER_FLAG | — | — |
| 71 | FromPOHeaderPayOnCode | PAY_ON_CODE | — | — |
| 72 | FromPOHeaderPcardId | PCARD_ID | — | — |
| 73 | FromPOHeaderPendingSignatureFlag | PENDING_SIGNATURE_FLAG | — | — |
| 74 | FromPOHeaderPoHeaderId | PO_HEADER_ID | — | — |
| 75 | FromPOHeaderPrcBuId | PRC_BU_ID | — | — |
| 76 | FromPOHeaderPriceUpdateTolerance | PRICE_UPDATE_TOLERANCE | — | — |
| 77 | FromPOHeaderProgramAppName | PROGRAM_APP_NAME | — | — |
| 78 | FromPOHeaderProgramName | PROGRAM_NAME | — | — |
| 79 | FromPOHeaderRate | RATE | — | — |
| 80 | FromPOHeaderRateDate | RATE_DATE | — | — |
| 81 | FromPOHeaderRateType | RATE_TYPE | — | — |
| 82 | FromPOHeaderReferenceNum | REFERENCE_NUM | — | — |
| 83 | FromPOHeaderReleaseMethod | RELEASE_METHOD | — | — |
| 84 | FromPOHeaderReqBuId | REQ_BU_ID | — | — |
| 85 | FromPOHeaderRequestId | REQUEST_ID | — | — |
| 86 | FromPOHeaderRetroPriceApplyUpdatesFlag | RETRO_PRICE_APPLY_UPDATES_FLAG | — | — |
| 87 | FromPOHeaderRetroPriceCommUpdatesFlag | RETRO_PRICE_COMM_UPDATES_FLAG | — | — |
| 88 | FromPOHeaderReviewAutogeneratedReleases | REVIEW_AUTOGENERATED_RELEASES | — | — |
| 89 | FromPOHeaderRevisedDate | REVISED_DATE | — | — |
| 90 | FromPOHeaderRevisionNum | REVISION_NUM | — | — |
| 91 | FromPOHeaderSegment1 | SEGMENT1 | — | — |
| 92 | FromPOHeaderSegment2 | SEGMENT2 | — | — |
| 93 | FromPOHeaderSegment3 | SEGMENT3 | — | — |
| 94 | FromPOHeaderSegment4 | SEGMENT4 | — | — |
| 95 | FromPOHeaderSegment5 | SEGMENT5 | — | — |
| 96 | FromPOHeaderServiceLevel | SERVICE_LEVEL | — | — |
| 97 | FromPOHeaderShipToLocationId | SHIP_TO_LOCATION_ID | — | — |
| 98 | FromPOHeaderShippingControl | SHIPPING_CONTROL | — | — |
| 99 | FromPOHeaderSoldtoLeId | SOLDTO_LE_ID | — | — |
| 100 | FromPOHeaderStartDate | START_DATE | — | — |
| 101 | FromPOHeaderStyleId | STYLE_ID | — | — |
| 102 | FromPOHeaderSubmitApprovalAutomatic | SUBMIT_APPROVAL_AUTOMATIC | — | — |
| 103 | FromPOHeaderSubmitDate | SUBMIT_DATE | — | — |
| 104 | FromPOHeaderSummaryFlag | SUMMARY_FLAG | — | — |
| 105 | FromPOHeaderSupplierNotifMethod | SUPPLIER_NOTIF_METHOD | — | — |
| 106 | FromPOHeaderTaxAttributeUpdateCode | TAX_ATTRIBUTE_UPDATE_CODE | — | — |
| 107 | FromPOHeaderTaxDocumentSubtype | TAX_DOCUMENT_SUBTYPE | — | — |
| 108 | FromPOHeaderTermsId | TERMS_ID | — | — |
| 109 | FromPOHeaderTypeLookupCode | TYPE_LOOKUP_CODE | — | — |
| 110 | FromPOHeaderUpdateSourcingRulesFlag | UPDATE_SOURCING_RULES_FLAG | — | — |
| 111 | FromPOHeaderUseNeedByDate | USE_NEED_BY_DATE | — | — |
| 112 | FromPOHeaderUseShipTo | USE_SHIP_TO | — | — |
| 113 | FromPOHeaderVendorContactId | VENDOR_CONTACT_ID | — | — |
| 114 | FromPOHeaderVendorId | VENDOR_ID | — | — |
| 115 | FromPOHeaderVendorOrderNum | VENDOR_ORDER_NUM | — | — |
| 116 | FromPOHeaderVendorSiteId | VENDOR_SITE_ID | — | — |
| 117 | FromPOHeaderXmlChangeSendDate | XML_CHANGE_SEND_DATE | — | — |
| 118 | FromPOHeaderXmlFlag | XML_FLAG | — | — |
| 119 | FromPOHeaderXmlSendDate | XML_SEND_DATE | — | — |
| 120 | FromQuotationHeaderAcceptanceDueDate | ACCEPTANCE_DUE_DATE | — | — |
| 121 | FromQuotationHeaderAcceptanceRequiredFlag | ACCEPTANCE_REQUIRED_FLAG | — | — |
| 122 | FromQuotationHeaderAcceptanceWithinDays | ACCEPTANCE_WITHIN_DAYS | — | — |
| 123 | FromQuotationHeaderAgentId | AGENT_ID | — | — |
| 124 | FromQuotationHeaderAmountLimit | AMOUNT_LIMIT | — | — |
| 125 | FromQuotationHeaderAmountReleased | AMOUNT_RELEASED | — | — |
| 126 | FromQuotationHeaderApprovedDate | APPROVED_DATE | — | — |
| 127 | FromQuotationHeaderApprovedFlag | APPROVED_FLAG | — | — |
| 128 | FromQuotationHeaderAutoSourcingFlag | AUTO_SOURCING_FLAG | — | — |
| 129 | FromQuotationHeaderBillToLocationId | BILL_TO_LOCATION_ID | — | — |
| 130 | FromQuotationHeaderBilltoBuId | BILLTO_BU_ID | — | — |
| 131 | FromQuotationHeaderBlanketTotalAmount | BLANKET_TOTAL_AMOUNT | — | — |
| 132 | FromQuotationHeaderCancelFlag | CANCEL_FLAG | — | — |
| 133 | FromQuotationHeaderCarrierId | CARRIER_ID | — | — |
| 134 | FromQuotationHeaderCatAdminAuthEnabledFlag | CAT_ADMIN_AUTH_ENABLED_FLAG | — | — |
| 135 | FromQuotationHeaderCbcAccountingDate | CBC_ACCOUNTING_DATE | — | — |
| 136 | FromQuotationHeaderChangeRequestedBy | CHANGE_REQUESTED_BY | — | — |
| 137 | FromQuotationHeaderChangeSummary | CHANGE_SUMMARY | — | — |
| 138 | FromQuotationHeaderClosedDate | CLOSED_DATE | — | — |
| 139 | FromQuotationHeaderComments | COMMENTS | — | — |
| 140 | FromQuotationHeaderConfirmingOrderFlag | CONFIRMING_ORDER_FLAG | — | — |
| 141 | FromQuotationHeaderConsignedConsumptionFlag | CONSIGNED_CONSUMPTION_FLAG | — | — |
| 142 | FromQuotationHeaderConsumeReqDemandFlag | CONSUME_REQ_DEMAND_FLAG | — | — |
| 143 | FromQuotationHeaderContermsArticlesUpdDate | CONTERMS_ARTICLES_UPD_DATE | — | — |
| 144 | FromQuotationHeaderContermsDelivUpdDate | CONTERMS_DELIV_UPD_DATE | — | — |
| 145 | FromQuotationHeaderContermsExistFlag | CONTERMS_EXIST_FLAG | — | — |
| 146 | FromQuotationHeaderCpaReference | CPA_REFERENCE | — | — |
| 147 | FromQuotationHeaderCreatedBy | CREATED_BY | — | — |
| 148 | FromQuotationHeaderCreatedLanguage | CREATED_LANGUAGE | — | — |
| 149 | FromQuotationHeaderCreationDate | CREATION_DATE | — | — |
| 150 | FromQuotationHeaderCurrencyCode | CURRENCY_CODE | — | — |
| 151 | FromQuotationHeaderCurrentVersionId | CURRENT_VERSION_ID | — | — |
| 152 | FromQuotationHeaderDefaultPoTradeOrgId | DEFAULT_PO_TRADE_ORG_ID | — | — |
| 153 | FromQuotationHeaderDefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | — |
| 154 | FromQuotationHeaderDocumentCreationMethod | DOCUMENT_CREATION_METHOD | — | — |
| 155 | FromQuotationHeaderDocumentStatus | DOCUMENT_STATUS | — | — |
| 156 | FromQuotationHeaderEdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 157 | FromQuotationHeaderEdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 158 | FromQuotationHeaderEmailAddress | EMAIL_ADDRESS | — | — |
| 159 | FromQuotationHeaderEnabledFlag | ENABLED_FLAG | — | — |
| 160 | FromQuotationHeaderEncumbranceRequiredFlag | ENCUMBRANCE_REQUIRED_FLAG | — | — |
| 161 | FromQuotationHeaderEndDate | END_DATE | — | — |
| 162 | FromQuotationHeaderFax | FAX | — | — |
| 163 | FromQuotationHeaderFirmDate | FIRM_DATE | — | — |
| 164 | FromQuotationHeaderFirmStatusLookupCode | FIRM_STATUS_LOOKUP_CODE | — | — |
| 165 | FromQuotationHeaderFobLookupCode | FOB_LOOKUP_CODE | — | — |
| 166 | FromQuotationHeaderFreightTermsLookupCode | FREIGHT_TERMS_LOOKUP_CODE | — | — |
| 167 | FromQuotationHeaderFromHeaderId | FROM_HEADER_ID | — | — |
| 168 | FromQuotationHeaderFromTypeLookupCode | FROM_TYPE_LOOKUP_CODE | — | — |
| 169 | FromQuotationHeaderFrozenFlag | FROZEN_FLAG | — | — |
| 170 | FromQuotationHeaderGenerateOrdersAutomatic | GENERATE_ORDERS_AUTOMATIC | — | — |
| 171 | FromQuotationHeaderGovernmentContext | GOVERNMENT_CONTEXT | — | — |
| 172 | FromQuotationHeaderGroupRequisitionLines | GROUP_REQUISITION_LINES | — | — |
| 173 | FromQuotationHeaderGroupRequisitions | GROUP_REQUISITIONS | — | — |
| 174 | FromQuotationHeaderInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | — |
| 175 | FromQuotationHeaderJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 176 | FromQuotationHeaderJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 177 | FromQuotationHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 178 | FromQuotationHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 179 | FromQuotationHeaderLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 180 | FromQuotationHeaderLastUpdatedProgram | LAST_UPDATED_PROGRAM | — | — |
| 181 | FromQuotationHeaderMinReleaseAmount | MIN_RELEASE_AMOUNT | — | — |
| 182 | FromQuotationHeaderModeOfTransport | MODE_OF_TRANSPORT | — | — |
| 183 | FromQuotationHeaderNoteToAuthorizer | NOTE_TO_AUTHORIZER | — | — |
| 184 | FromQuotationHeaderNoteToReceiver | NOTE_TO_RECEIVER | — | — |
| 185 | FromQuotationHeaderNoteToVendor | NOTE_TO_VENDOR | — | — |
| 186 | FromQuotationHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 187 | FromQuotationHeaderOrchestrationOrderFlag | ORCHESTRATION_ORDER_FLAG | — | — |
| 188 | FromQuotationHeaderPayOnCode | PAY_ON_CODE | — | — |
| 189 | FromQuotationHeaderPcardId | PCARD_ID | — | — |
| 190 | FromQuotationHeaderPendingSignatureFlag | PENDING_SIGNATURE_FLAG | — | — |
| 191 | FromQuotationHeaderPoHeaderId | PO_HEADER_ID | — | — |
| 192 | FromQuotationHeaderPrcBuId | PRC_BU_ID | — | — |
| 193 | FromQuotationHeaderPriceUpdateTolerance | PRICE_UPDATE_TOLERANCE | — | — |
| 194 | FromQuotationHeaderProgramAppName | PROGRAM_APP_NAME | — | — |
| 195 | FromQuotationHeaderProgramName | PROGRAM_NAME | — | — |
| 196 | FromQuotationHeaderRate | RATE | — | — |
| 197 | FromQuotationHeaderRateDate | RATE_DATE | — | — |
| 198 | FromQuotationHeaderRateType | RATE_TYPE | — | — |
| 199 | FromQuotationHeaderReferenceNum | REFERENCE_NUM | — | — |
| 200 | FromQuotationHeaderReleaseMethod | RELEASE_METHOD | — | — |
| 201 | FromQuotationHeaderReqBuId | REQ_BU_ID | — | — |
| 202 | FromQuotationHeaderRequestId | REQUEST_ID | — | — |
| 203 | FromQuotationHeaderRetroPriceApplyUpdatesFlag | RETRO_PRICE_APPLY_UPDATES_FLAG | — | — |
| 204 | FromQuotationHeaderRetroPriceCommUpdatesFlag | RETRO_PRICE_COMM_UPDATES_FLAG | — | — |
| 205 | FromQuotationHeaderReviewAutogeneratedReleases | REVIEW_AUTOGENERATED_RELEASES | — | — |
| 206 | FromQuotationHeaderRevisedDate | REVISED_DATE | — | — |
| 207 | FromQuotationHeaderRevisionNum | REVISION_NUM | — | — |
| 208 | FromQuotationHeaderSegment1 | SEGMENT1 | — | — |
| 209 | FromQuotationHeaderSegment2 | SEGMENT2 | — | — |
| 210 | FromQuotationHeaderSegment3 | SEGMENT3 | — | — |
| 211 | FromQuotationHeaderSegment4 | SEGMENT4 | — | — |
| 212 | FromQuotationHeaderSegment5 | SEGMENT5 | — | — |
| 213 | FromQuotationHeaderServiceLevel | SERVICE_LEVEL | — | — |
| 214 | FromQuotationHeaderShipToLocationId | SHIP_TO_LOCATION_ID | — | — |
| 215 | FromQuotationHeaderShippingControl | SHIPPING_CONTROL | — | — |
| 216 | FromQuotationHeaderSoldtoLeId | SOLDTO_LE_ID | — | — |
| 217 | FromQuotationHeaderStartDate | START_DATE | — | — |
| 218 | FromQuotationHeaderStyleId | STYLE_ID | — | — |
| 219 | FromQuotationHeaderSubmitApprovalAutomatic | SUBMIT_APPROVAL_AUTOMATIC | — | — |
| 220 | FromQuotationHeaderSubmitDate | SUBMIT_DATE | — | — |
| 221 | FromQuotationHeaderSummaryFlag | SUMMARY_FLAG | — | — |
| 222 | FromQuotationHeaderSupplierNotifMethod | SUPPLIER_NOTIF_METHOD | — | — |
| 223 | FromQuotationHeaderTaxAttributeUpdateCode | TAX_ATTRIBUTE_UPDATE_CODE | — | — |
| 224 | FromQuotationHeaderTaxDocumentSubtype | TAX_DOCUMENT_SUBTYPE | — | — |
| 225 | FromQuotationHeaderTermsId | TERMS_ID | — | — |
| 226 | FromQuotationHeaderTypeLookupCode | TYPE_LOOKUP_CODE | — | — |
| 227 | FromQuotationHeaderUpdateSourcingRulesFlag | UPDATE_SOURCING_RULES_FLAG | — | — |
| 228 | FromQuotationHeaderUseNeedByDate | USE_NEED_BY_DATE | — | — |
| 229 | FromQuotationHeaderUseShipTo | USE_SHIP_TO | — | — |
| 230 | FromQuotationHeaderVendorContactId | VENDOR_CONTACT_ID | — | — |
| 231 | FromQuotationHeaderVendorId | VENDOR_ID | — | — |
| 232 | FromQuotationHeaderVendorOrderNum | VENDOR_ORDER_NUM | — | — |
| 233 | FromQuotationHeaderVendorSiteId | VENDOR_SITE_ID | — | — |
| 234 | FromQuotationHeaderXmlChangeSendDate | XML_CHANGE_SEND_DATE | — | — |
| 235 | FromQuotationHeaderXmlFlag | XML_FLAG | — | — |
| 236 | FromQuotationHeaderXmlSendDate | XML_SEND_DATE | — | — |
| 237 | PurchasingDocumentHeaderAcceptanceDueDate | ACCEPTANCE_DUE_DATE | — | — |
| 238 | PurchasingDocumentHeaderAcceptanceRequiredFlag | ACCEPTANCE_REQUIRED_FLAG | — | ✅ |
| 239 | PurchasingDocumentHeaderAcceptanceWithinDays | ACCEPTANCE_WITHIN_DAYS | — | — |
| 240 | PurchasingDocumentHeaderAdditionalContactEmailAddress | ALT_CONTACT_EMAIL_ADDRESS | — | — |
| 241 | PurchasingDocumentHeaderAgentId | AGENT_ID | — | ✅ |
| 242 | PurchasingDocumentHeaderAgingOnsetPoint | AGING_ONSET_POINT | — | — |
| 243 | PurchasingDocumentHeaderAgingPeriodDays | AGING_PERIOD_DAYS | — | — |
| 244 | PurchasingDocumentHeaderAmountLimit | AMOUNT_LIMIT | — | ✅ |
| 245 | PurchasingDocumentHeaderAmountReleased | AMOUNT_RELEASED | — | — |
| 246 | PurchasingDocumentHeaderApprovedDate | APPROVED_DATE | — | — |
| 247 | PurchasingDocumentHeaderApprovedFlag | APPROVED_FLAG | — | — |
| 248 | PurchasingDocumentHeaderAutoSourcingFlag | AUTO_SOURCING_FLAG | — | — |
| 249 | PurchasingDocumentHeaderBillToLocationId | BILL_TO_LOCATION_ID | — | — |
| 250 | PurchasingDocumentHeaderBillingCycleClosingDate | BILLING_CYCLE_CLOSING_DATE | — | — |
| 251 | PurchasingDocumentHeaderBilltoBuId | BILLTO_BU_ID | — | — |
| 252 | PurchasingDocumentHeaderBlanketTotalAmount | BLANKET_TOTAL_AMOUNT | — | ✅ |
| 253 | PurchasingDocumentHeaderBudgetControlEnabledFlag | BUDGET_CONTROL_ENABLED_FLAG | — | — |
| 254 | PurchasingDocumentHeaderCancelFlag | CANCEL_FLAG | — | — |
| 255 | PurchasingDocumentHeaderCarrierId | CARRIER_ID | — | — |
| 256 | PurchasingDocumentHeaderCatAdminAuthEnabledFlag | CAT_ADMIN_AUTH_ENABLED_FLAG | — | — |
| 257 | PurchasingDocumentHeaderCbcAccountingDate | CBC_ACCOUNTING_DATE | — | — |
| 258 | PurchasingDocumentHeaderChangeRequestedBy | CHANGE_REQUESTED_BY | — | — |
| 259 | PurchasingDocumentHeaderChangeSummary | CHANGE_SUMMARY | — | — |
| 260 | PurchasingDocumentHeaderClosedDate | CLOSED_DATE | — | — |
| 261 | PurchasingDocumentHeaderComments | COMMENTS | — | ✅ |
| 262 | PurchasingDocumentHeaderConfirmingOrderFlag | CONFIRMING_ORDER_FLAG | — | ✅ |
| 263 | PurchasingDocumentHeaderConsignedConsumptionFlag | CONSIGNED_CONSUMPTION_FLAG | — | — |
| 264 | PurchasingDocumentHeaderConsumeReqDemandFlag | CONSUME_REQ_DEMAND_FLAG | — | — |
| 265 | PurchasingDocumentHeaderConsumptionAdviceFrequency | CONSUMPTION_ADVICE_FREQUENCY | — | — |
| 266 | PurchasingDocumentHeaderConsumptionAdviceSummary | CONSUMPTION_ADVICE_SUMMARY | — | — |
| 267 | PurchasingDocumentHeaderContermsArticlesUpdDate | CONTERMS_ARTICLES_UPD_DATE | — | — |
| 268 | PurchasingDocumentHeaderContermsDelivUpdDate | CONTERMS_DELIV_UPD_DATE | — | — |
| 269 | PurchasingDocumentHeaderContermsExistFlag | CONTERMS_EXIST_FLAG | — | — |
| 270 | PurchasingDocumentHeaderCpaReference | CPA_REFERENCE | — | — |
| 271 | PurchasingDocumentHeaderCreatedBy | CREATED_BY | — | — |
| 272 | PurchasingDocumentHeaderCreatedLanguage | CREATED_LANGUAGE | — | — |
| 273 | PurchasingDocumentHeaderCreationDate | CREATION_DATE | — | — |
| 274 | PurchasingDocumentHeaderCurrencyCode | CURRENCY_CODE | — | ✅ |
| 275 | PurchasingDocumentHeaderCurrentVersionId | CURRENT_VERSION_ID | — | — |
| 276 | PurchasingDocumentHeaderDefaultConsignmentLineFlag | DEFAULT_CONSIGNMENT_LINE_FLAG | — | — |
| 277 | PurchasingDocumentHeaderDefaultPoTradeOrgId | DEFAULT_PO_TRADE_ORG_ID | — | — |
| 278 | PurchasingDocumentHeaderDefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | ✅ |
| 279 | PurchasingDocumentHeaderDocumentCreationMethod | DOCUMENT_CREATION_METHOD | — | — |
| 280 | PurchasingDocumentHeaderDocumentStatus | DOCUMENT_STATUS | — | ✅ |
| 281 | PurchasingDocumentHeaderEdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 282 | PurchasingDocumentHeaderEdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 283 | PurchasingDocumentHeaderEmailAddress | EMAIL_ADDRESS | — | — |
| 284 | PurchasingDocumentHeaderEnabledFlag | ENABLED_FLAG | — | — |
| 285 | PurchasingDocumentHeaderEncumbranceRequiredFlag | ENCUMBRANCE_REQUIRED_FLAG | — | — |
| 286 | PurchasingDocumentHeaderEndDate | END_DATE | — | ✅ |
| 287 | PurchasingDocumentHeaderFax | FAX | — | — |
| 288 | PurchasingDocumentHeaderFirmDate | FIRM_DATE | — | — |
| 289 | PurchasingDocumentHeaderFirmStatusLookupCode | FIRM_STATUS_LOOKUP_CODE | — | — |
| 290 | PurchasingDocumentHeaderFobLookupCode | FOB_LOOKUP_CODE | — | — |
| 291 | PurchasingDocumentHeaderFreightTermsLookupCode | FREIGHT_TERMS_LOOKUP_CODE | — | — |
| 292 | PurchasingDocumentHeaderFromHeaderId | FROM_HEADER_ID | — | — |
| 293 | PurchasingDocumentHeaderFromTypeLookupCode | FROM_TYPE_LOOKUP_CODE | — | — |
| 294 | PurchasingDocumentHeaderFrozenFlag | FROZEN_FLAG | — | ✅ |
| 295 | PurchasingDocumentHeaderFundsStatus | FUNDS_STATUS | — | — |
| 296 | PurchasingDocumentHeaderGenerateOrdersAutomatic | GENERATE_ORDERS_AUTOMATIC | — | — |
| 297 | PurchasingDocumentHeaderGovernmentContext | GOVERNMENT_CONTEXT | — | — |
| 298 | PurchasingDocumentHeaderGroupRequisitionLines | GROUP_REQUISITION_LINES | — | — |
| 299 | PurchasingDocumentHeaderGroupRequisitions | GROUP_REQUISITIONS | — | — |
| 300 | PurchasingDocumentHeaderInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | ✅ |
| 301 | PurchasingDocumentHeaderJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 302 | PurchasingDocumentHeaderJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 303 | PurchasingDocumentHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 304 | PurchasingDocumentHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 305 | PurchasingDocumentHeaderLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 306 | PurchasingDocumentHeaderLastUpdatedProgram | LAST_UPDATED_PROGRAM | — | — |
| 307 | PurchasingDocumentHeaderMinReleaseAmount | MIN_RELEASE_AMOUNT | — | — |
| 308 | PurchasingDocumentHeaderModeOfTransport | MODE_OF_TRANSPORT | — | — |
| 309 | PurchasingDocumentHeaderNoteToAuthorizer | NOTE_TO_AUTHORIZER | — | — |
| 310 | PurchasingDocumentHeaderNoteToReceiver | NOTE_TO_RECEIVER | — | ✅ |
| 311 | PurchasingDocumentHeaderNoteToVendor | NOTE_TO_VENDOR | — | ✅ |
| 312 | PurchasingDocumentHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 313 | PurchasingDocumentHeaderOrchestrationOrderFlag | ORCHESTRATION_ORDER_FLAG | — | — |
| 314 | PurchasingDocumentHeaderPayOnCode | PAY_ON_CODE | — | — |
| 315 | PurchasingDocumentHeaderPayOnUseFlag | PAY_ON_USE_FLAG | — | — |
| 316 | PurchasingDocumentHeaderPcardId | PCARD_ID | — | — |
| 317 | PurchasingDocumentHeaderPendingSignatureFlag | PENDING_SIGNATURE_FLAG | — | — |
| 318 | PurchasingDocumentHeaderPoHeaderId | PO_HEADER_ID | — | ✅ |
| 319 | PurchasingDocumentHeaderPrcBuId | PRC_BU_ID | — | — |
| 320 | PurchasingDocumentHeaderPriceUpdateTolerance | PRICE_UPDATE_TOLERANCE | — | — |
| 321 | PurchasingDocumentHeaderProgramAppName | PROGRAM_APP_NAME | — | — |
| 322 | PurchasingDocumentHeaderProgramName | PROGRAM_NAME | — | — |
| 323 | PurchasingDocumentHeaderRate | RATE | — | — |
| 324 | PurchasingDocumentHeaderRateDate | RATE_DATE | — | — |
| 325 | PurchasingDocumentHeaderRateType | RATE_TYPE | — | — |
| 326 | PurchasingDocumentHeaderReferenceNum | REFERENCE_NUM | — | — |
| 327 | PurchasingDocumentHeaderReleaseMethod | RELEASE_METHOD | — | — |
| 328 | PurchasingDocumentHeaderReqBuId | REQ_BU_ID | — | — |
| 329 | PurchasingDocumentHeaderRequestId | REQUEST_ID | — | — |
| 330 | PurchasingDocumentHeaderRetroPriceApplyUpdatesFlag | RETRO_PRICE_APPLY_UPDATES_FLAG | — | — |
| 331 | PurchasingDocumentHeaderRetroPriceCommUpdatesFlag | RETRO_PRICE_COMM_UPDATES_FLAG | — | — |
| 332 | PurchasingDocumentHeaderReviewAutogeneratedReleases | REVIEW_AUTOGENERATED_RELEASES | — | — |
| 333 | PurchasingDocumentHeaderRevisedDate | REVISED_DATE | — | — |
| 334 | PurchasingDocumentHeaderRevisionNum | REVISION_NUM | — | — |
| 335 | PurchasingDocumentHeaderSegment1 | SEGMENT1 | — | — |
| 336 | PurchasingDocumentHeaderSegment2 | SEGMENT2 | — | — |
| 337 | PurchasingDocumentHeaderSegment3 | SEGMENT3 | — | — |
| 338 | PurchasingDocumentHeaderSegment4 | SEGMENT4 | — | — |
| 339 | PurchasingDocumentHeaderSegment5 | SEGMENT5 | — | — |
| 340 | PurchasingDocumentHeaderServiceLevel | SERVICE_LEVEL | — | — |
| 341 | PurchasingDocumentHeaderShipToLocationId | SHIP_TO_LOCATION_ID | — | — |
| 342 | PurchasingDocumentHeaderShippingControl | SHIPPING_CONTROL | — | — |
| 343 | PurchasingDocumentHeaderSoldtoLeId | SOLDTO_LE_ID | — | — |
| 344 | PurchasingDocumentHeaderSourcingPriority | SOURCING_PRIORITY | — | — |
| 345 | PurchasingDocumentHeaderStartDate | START_DATE | — | ✅ |
| 346 | PurchasingDocumentHeaderStyleId | STYLE_ID | — | — |
| 347 | PurchasingDocumentHeaderSubmitApprovalAutomatic | SUBMIT_APPROVAL_AUTOMATIC | — | — |
| 348 | PurchasingDocumentHeaderSubmitDate | SUBMIT_DATE | — | — |
| 349 | PurchasingDocumentHeaderSummaryFlag | SUMMARY_FLAG | — | — |
| 350 | PurchasingDocumentHeaderSupplierNotifMethod | SUPPLIER_NOTIF_METHOD | — | — |
| 351 | PurchasingDocumentHeaderTaxAttributeUpdateCode | TAX_ATTRIBUTE_UPDATE_CODE | — | — |
| 352 | PurchasingDocumentHeaderTaxDocumentSubtype | TAX_DOCUMENT_SUBTYPE | — | — |
| 353 | PurchasingDocumentHeaderTermsId | TERMS_ID | — | — |
| 354 | PurchasingDocumentHeaderTypeLookupCode | TYPE_LOOKUP_CODE | — | — |
| 355 | PurchasingDocumentHeaderUpdateSourcingRulesFlag | UPDATE_SOURCING_RULES_FLAG | — | — |
| 356 | PurchasingDocumentHeaderUseNeedByDate | USE_NEED_BY_DATE | — | — |
| 357 | PurchasingDocumentHeaderUseShipTo | USE_SHIP_TO | — | — |
| 358 | PurchasingDocumentHeaderVendorContactId | VENDOR_CONTACT_ID | — | — |
| 359 | PurchasingDocumentHeaderVendorId | VENDOR_ID | — | — |
| 360 | PurchasingDocumentHeaderVendorOrderNum | VENDOR_ORDER_NUM | — | — |
| 361 | PurchasingDocumentHeaderVendorSiteId | VENDOR_SITE_ID | — | ✅ |
| 362 | PurchasingDocumentHeaderXmlChangeSendDate | XML_CHANGE_SEND_DATE | — | — |
| 363 | PurchasingDocumentHeaderXmlFlag | XML_FLAG | — | — |
| 364 | PurchasingDocumentHeaderXmlSendDate | XML_SEND_DATE | — | — |

### [[po_headers_draft_all|PO_HEADERS_DRAFT_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DraftHeaderAcceptanceDueDate | ACCEPTANCE_DUE_DATE | — | — |
| 2 | DraftHeaderAcceptanceRequiredFlag | ACCEPTANCE_REQUIRED_FLAG | — | ✅ |
| 3 | DraftHeaderAcceptanceWithinDays | ACCEPTANCE_WITHIN_DAYS | — | — |
| 4 | DraftHeaderAdditionalContactEmailAddress | ALT_CONTACT_EMAIL_ADDRESS | — | — |
| 5 | DraftHeaderAgentId | AGENT_ID | — | ✅ |
| 6 | DraftHeaderAgingOnsetPoint | AGING_ONSET_POINT | — | — |
| 7 | DraftHeaderAgingPeriodDays | AGING_PERIOD_DAYS | — | — |
| 8 | DraftHeaderAmountLimit | AMOUNT_LIMIT | — | ✅ |
| 9 | DraftHeaderAutoSourcingFlag | AUTO_SOURCING_FLAG | — | — |
| 10 | DraftHeaderBillToLocationId | BILL_TO_LOCATION_ID | — | — |
| 11 | DraftHeaderBillingCycleClosingDate | BILLING_CYCLE_CLOSING_DATE | — | — |
| 12 | DraftHeaderBilltoBuId | BILLTO_BU_ID | — | — |
| 13 | DraftHeaderBlanketTotalAmount | BLANKET_TOTAL_AMOUNT | — | ✅ |
| 14 | DraftHeaderBudgetControlEnabledFlag | BUDGET_CONTROL_ENABLED_FLAG | — | ✅ |
| 15 | DraftHeaderBuyerManagedTransportFlag | BUYER_MANAGED_TRANSPORT_FLAG | — | ✅ |
| 16 | DraftHeaderCancelFlag | CANCEL_FLAG | — | — |
| 17 | DraftHeaderCarrierId | CARRIER_ID | — | — |
| 18 | DraftHeaderCbcAccountingDate | CBC_ACCOUNTING_DATE | — | — |
| 19 | DraftHeaderChangeAcceptedFlag | CHANGE_ACCEPTED_FLAG | — | — |
| 20 | DraftHeaderChangeRequestedBy | CHANGE_REQUESTED_BY | — | — |
| 21 | DraftHeaderChangeSummary | CHANGE_SUMMARY | — | — |
| 22 | DraftHeaderChecklistId | CHECKLIST_ID | — | — |
| 23 | DraftHeaderComments | COMMENTS | — | ✅ |
| 24 | DraftHeaderConfirmingOrderFlag | CONFIRMING_ORDER_FLAG | — | ✅ |
| 25 | DraftHeaderConsignedConsumptionFlag | CONSIGNED_CONSUMPTION_FLAG | — | — |
| 26 | DraftHeaderConsumeReqDemandFlag | CONSUME_REQ_DEMAND_FLAG | — | — |
| 27 | DraftHeaderConsumptionAdviceFrequency | CONSUMPTION_ADVICE_FREQUENCY | — | — |
| 28 | DraftHeaderConsumptionAdviceSummary | CONSUMPTION_ADVICE_SUMMARY | — | — |
| 29 | DraftHeaderContermsArticlesUpdDate | CONTERMS_ARTICLES_UPD_DATE | — | — |
| 30 | DraftHeaderContermsDelivUpdDate | CONTERMS_DELIV_UPD_DATE | — | — |
| 31 | DraftHeaderContermsExistFlag | CONTERMS_EXIST_FLAG | — | — |
| 32 | DraftHeaderCpaReference | CPA_REFERENCE | — | — |
| 33 | DraftHeaderCreatedBy | CREATED_BY | — | — |
| 34 | DraftHeaderCreatedLanguage | CREATED_LANGUAGE | — | — |
| 35 | DraftHeaderCreationDate | CREATION_DATE | — | ✅ |
| 36 | DraftHeaderCurrencyCode | CURRENCY_CODE | — | ✅ |
| 37 | DraftHeaderDefaultConsignmentLineFlag | DEFAULT_CONSIGNMENT_LINE_FLAG | — | — |
| 38 | DraftHeaderDefaultPoTradeOrgId | DEFAULT_PO_TRADE_ORG_ID | — | — |
| 39 | DraftHeaderDefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | ✅ |
| 40 | DraftHeaderDocumentCreationMethod | DOCUMENT_CREATION_METHOD | — | — |
| 41 | DraftHeaderEmailAddress | EMAIL_ADDRESS | — | — |
| 42 | DraftHeaderEnabledFlag | ENABLED_FLAG | — | — |
| 43 | DraftHeaderEncumbranceRequiredFlag | ENCUMBRANCE_REQUIRED_FLAG | — | — |
| 44 | DraftHeaderEndDate | END_DATE | — | ✅ |
| 45 | DraftHeaderEntityChangeTypeCode | ENTITY_CHANGE_TYPE_CODE | — | — |
| 46 | DraftHeaderExternalChangeFlag | EXTERNAL_CHANGE_FLAG | — | — |
| 47 | DraftHeaderFax | FAX | — | — |
| 48 | DraftHeaderFirmDate | FIRM_DATE | — | — |
| 49 | DraftHeaderFirmStatusLookupCode | FIRM_STATUS_LOOKUP_CODE | — | — |
| 50 | DraftHeaderFobLookupCode | FOB_LOOKUP_CODE | — | — |
| 51 | DraftHeaderFreightTermsLookupCode | FREIGHT_TERMS_LOOKUP_CODE | — | — |
| 52 | DraftHeaderFromHeaderId | FROM_HEADER_ID | — | — |
| 53 | DraftHeaderFromTypeLookupCode | FROM_TYPE_LOOKUP_CODE | — | — |
| 54 | DraftHeaderFundsStatus | FUNDS_STATUS | — | ✅ |
| 55 | DraftHeaderGenerateOrdersAutomatic | GENERATE_ORDERS_AUTOMATIC | — | — |
| 56 | DraftHeaderGovernmentContext | GOVERNMENT_CONTEXT | — | — |
| 57 | DraftHeaderGroupRequisitionLines | GROUP_REQUISITION_LINES | — | — |
| 58 | DraftHeaderGroupRequisitions | GROUP_REQUISITIONS | — | — |
| 59 | DraftHeaderInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | — |
| 60 | DraftHeaderJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 61 | DraftHeaderJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 62 | DraftHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 63 | DraftHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 64 | DraftHeaderLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 65 | DraftHeaderMinReleaseAmount | MIN_RELEASE_AMOUNT | — | ✅ |
| 66 | DraftHeaderModeOfTransport | MODE_OF_TRANSPORT | — | ✅ |
| 67 | DraftHeaderNoteToAuthorizer | NOTE_TO_AUTHORIZER | — | — |
| 68 | DraftHeaderNoteToReceiver | NOTE_TO_RECEIVER | — | ✅ |
| 69 | DraftHeaderNoteToVendor | NOTE_TO_VENDOR | — | ✅ |
| 70 | DraftHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 71 | DraftHeaderOrchestrationOrderFlag | ORCHESTRATION_ORDER_FLAG | — | — |
| 72 | DraftHeaderPayOnCode | PAY_ON_CODE | — | — |
| 73 | DraftHeaderPayOnUseFlag | PAY_ON_USE_FLAG | — | — |
| 74 | DraftHeaderPcardId | PCARD_ID | — | — |
| 75 | DraftHeaderPendingSignatureFlag | PENDING_SIGNATURE_FLAG | — | — |
| 76 | DraftHeaderPrcBuId | PRC_BU_ID | — | — |
| 77 | DraftHeaderPriceUpdateTolerance | PRICE_UPDATE_TOLERANCE | — | — |
| 78 | DraftHeaderProgramAppName | PROGRAM_APP_NAME | — | — |
| 79 | DraftHeaderProgramName | PROGRAM_NAME | — | — |
| 80 | DraftHeaderRate | RATE | — | — |
| 81 | DraftHeaderRateDate | RATE_DATE | — | — |
| 82 | DraftHeaderRateType | RATE_TYPE | — | — |
| 83 | DraftHeaderReasonForChange | REASON_FOR_CHANGE | — | — |
| 84 | DraftHeaderReferenceNum | REFERENCE_NUM | — | — |
| 85 | DraftHeaderReqBuId | REQ_BU_ID | — | — |
| 86 | DraftHeaderRequestId | REQUEST_ID | — | — |
| 87 | DraftHeaderRetroPriceApplyUpdatesFlag | RETRO_PRICE_APPLY_UPDATES_FLAG | — | — |
| 88 | DraftHeaderRetroPriceCommUpdatesFlag | RETRO_PRICE_COMM_UPDATES_FLAG | — | — |
| 89 | DraftHeaderSegment1 | SEGMENT1 | — | ✅ |
| 90 | DraftHeaderSegment2 | SEGMENT2 | — | — |
| 91 | DraftHeaderSegment3 | SEGMENT3 | — | — |
| 92 | DraftHeaderSegment4 | SEGMENT4 | — | — |
| 93 | DraftHeaderSegment5 | SEGMENT5 | — | — |
| 94 | DraftHeaderServiceLevel | SERVICE_LEVEL | — | ✅ |
| 95 | DraftHeaderShipToLocationId | SHIP_TO_LOCATION_ID | — | — |
| 96 | DraftHeaderShippingControl | SHIPPING_CONTROL | — | — |
| 97 | DraftHeaderSoldtoLeId | SOLDTO_LE_ID | — | — |
| 98 | DraftHeaderSourcingPriority | SOURCING_PRIORITY | — | — |
| 99 | DraftHeaderStartDate | START_DATE | — | ✅ |
| 100 | DraftHeaderStyleId | STYLE_ID | — | — |
| 101 | DraftHeaderSubmitApprovalAutomatic | SUBMIT_APPROVAL_AUTOMATIC | — | — |
| 102 | DraftHeaderSubmitDate | SUBMIT_DATE | — | — |
| 103 | DraftHeaderSummaryFlag | SUMMARY_FLAG | — | — |
| 104 | DraftHeaderSupplierNotifMethod | SUPPLIER_NOTIF_METHOD | — | ✅ |
| 105 | DraftHeaderTaxAttributeUpdateCode | TAX_ATTRIBUTE_UPDATE_CODE | — | — |
| 106 | DraftHeaderTaxDocumentSubtype | TAX_DOCUMENT_SUBTYPE | — | — |
| 107 | DraftHeaderTermsId | TERMS_ID | — | — |
| 108 | DraftHeaderTypeLookupCode | TYPE_LOOKUP_CODE | — | ✅ |
| 109 | DraftHeaderUpdateSourcingRulesFlag | UPDATE_SOURCING_RULES_FLAG | — | — |
| 110 | DraftHeaderUseNeedByDate | USE_NEED_BY_DATE | — | — |
| 111 | DraftHeaderUseShipTo | USE_SHIP_TO | — | — |
| 112 | DraftHeaderVendorContactId | VENDOR_CONTACT_ID | — | — |
| 113 | DraftHeaderVendorId | VENDOR_ID | — | — |
| 114 | DraftHeaderVendorOrderNum | VENDOR_ORDER_NUM | — | — |
| 115 | DraftHeaderVendorSiteId | VENDOR_SITE_ID | — | ✅ |
| 116 | DraftHeaderXmlFlag | XML_FLAG | — | — |
| 117 | OverridingApproverId | OVERRIDING_APPROVER_ID | — | — |
| 118 | PoHeaderId | PO_HEADER_ID | 🔑 | ✅ |

### [[po_versions_unprocessed_v|PO_VERSIONS_UNPROCESSED_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExternalSystemFlag | EXTERNAL_SYSTEM_FLAG | — | — |
| 2 | PoVersionAcceptedDate | ACCEPTED_DATE | — | — |
| 3 | PoVersionApprovedDate | APPROVED_DATE | — | — |
| 4 | PoVersionCancelBackingReqFlag | CANCEL_BACKING_REQ_FLAG | — | — |
| 5 | PoVersionCancelDocFlag | CANCEL_DOC_FLAG | — | — |
| 6 | PoVersionChangeOrderDesc | CHANGE_ORDER_DESC | — | ✅ |
| 7 | PoVersionChangeOrderStatus | CHANGE_ORDER_STATUS | — | ✅ |
| 8 | PoVersionChangeOrderType | CHANGE_ORDER_TYPE | — | — |
| 9 | PoVersionCoCanceledByRole | CO_CANCELED_BY_ROLE | — | — |
| 10 | PoVersionCoCanceledByUserId | CO_CANCELED_BY_USER_ID | — | — |
| 11 | PoVersionCoCanceledFlag | CO_CANCELED_FLAG | — | ✅ |
| 12 | PoVersionCoNum | CO_NUM | — | ✅ |
| 13 | PoVersionCoSequence | CO_SEQUENCE | — | — |
| 14 | PoVersionCommunicatedDate | COMMUNICATED_DATE | — | — |
| 15 | PoVersionCommunicatedToSupplier | COMMUNICATED_TO_SUPPLIER | — | — |
| 16 | PoVersionCreationDate | CREATION_DATE | — | — |
| 17 | PoVersionDocumentDate | DOCUMENT_DATE | — | — |
| 18 | PoVersionFundsStatus | FUNDS_STATUS | — | — |
| 19 | PoVersionJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 20 | PoVersionJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 21 | PoVersionModifiedFlag | MODIFIED_FLAG | — | — |
| 22 | PoVersionOnlineReportId | ONLINE_REPORT_ID | — | — |
| 23 | PoVersionOriginatorId | ORIGINATOR_ID | — | — |
| 24 | PoVersionOriginatorRole | ORIGINATOR_ROLE | — | — |
| 25 | PoVersionPendingResponseRole | PENDING_RESPONSE_ROLE | — | — |
| 26 | PoVersionPoHeaderId | PO_HEADER_ID | — | — |
| 27 | PoVersionProcessedDate | PROCESSED_DATE | — | — |
| 28 | PoVersionProgramAppName | PROGRAM_APP_NAME | — | — |
| 29 | PoVersionProgramName | PROGRAM_NAME | — | — |
| 30 | PoVersionRejectedFlag | REJECTED_FLAG | — | ✅ |
| 31 | PoVersionRequestDate | REQUEST_DATE | — | — |
| 32 | PoVersionRequestId | REQUEST_ID | — | — |
| 33 | PoVersionRevisionNum | REVISION_NUM | — | — |
| 34 | PoVersionSubmittedDate | SUBMITTED_DATE | — | — |
| 35 | PoVersionVersionId | VERSION_ID | — | — |
| 36 | PoVersionWithdrawnFlag | WITHDRAWN_FLAG | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
