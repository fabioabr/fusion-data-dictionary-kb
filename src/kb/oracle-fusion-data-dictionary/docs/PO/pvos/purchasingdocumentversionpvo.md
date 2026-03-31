---
id: DOC-PO-PVO-PurchasingDocumentVersionPVO
doc_type: system-doc
title: "PurchasingDocumentVersionPVO — PVO Purchasing"
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
  - PurchasingDocumentVersionPVO
  - purchasingdocumentversionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PurchasingDocumentVersionPVO

## 📌 Visão Geral

Disponibiliza versões de documentos de compra para consulta, incluindo dados de arquivo e rascunho. Permite comparar versões anteriores e entender a evolução de cada pedido ao longo do tempo.

**Caminho:** `FscmTopModelAM.PrcPoPublicViewAM.PurchasingDocumentVersionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 626 | 5 | 8 | 84 | 13% |

---

## 🔗 Tabelas Relacionadas

- [[po_doc_style_headers|PO_DOC_STYLE_HEADERS]] — 18 atributos (1 PKs, 2 BICC)
- [[po_headers_all|PO_HEADERS_ALL]] — 352 atributos (3 PKs, 32 BICC)
- [[po_headers_archive_all|PO_HEADERS_ARCHIVE_ALL]] — 108 atributos (2 PKs, 16 BICC)
- [[po_headers_draft_all|PO_HEADERS_DRAFT_ALL]] — 105 atributos (1 PKs, 9 BICC)
- [[po_versions|PO_VERSIONS]] — 43 atributos (1 PKs, 25 BICC)

---

## ⚙️ Atributos

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
| 16 | DocStyleStyleId | STYLE_ID | 🔑 | ✅ |
| 17 | DocStyleStyleName | STYLE_NAME | — | — |
| 18 | DocStyleStyleType | STYLE_TYPE | — | — |

### [[po_headers_all|PO_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FromDraftHeaderAcceptanceDueDate | ACCEPTANCE_DUE_DATE | — | — |
| 2 | FromDraftHeaderAcceptanceRequiredFlag | ACCEPTANCE_REQUIRED_FLAG | — | — |
| 3 | FromDraftHeaderAcceptanceWithinDays | ACCEPTANCE_WITHIN_DAYS | — | — |
| 4 | FromDraftHeaderAgentId | AGENT_ID | — | — |
| 5 | FromDraftHeaderAmountLimit | AMOUNT_LIMIT | — | — |
| 6 | FromDraftHeaderAmountReleased | AMOUNT_RELEASED | — | — |
| 7 | FromDraftHeaderApprovedDate | APPROVED_DATE | — | — |
| 8 | FromDraftHeaderApprovedFlag | APPROVED_FLAG | — | — |
| 9 | FromDraftHeaderAutoSourcingFlag | AUTO_SOURCING_FLAG | — | — |
| 10 | FromDraftHeaderBillToLocationId | BILL_TO_LOCATION_ID | — | — |
| 11 | FromDraftHeaderBilltoBuId | BILLTO_BU_ID | — | ✅ |
| 12 | FromDraftHeaderBlanketTotalAmount | BLANKET_TOTAL_AMOUNT | — | — |
| 13 | FromDraftHeaderCancelFlag | CANCEL_FLAG | — | — |
| 14 | FromDraftHeaderCarrierId | CARRIER_ID | — | — |
| 15 | FromDraftHeaderCatAdminAuthEnabledFlag | CAT_ADMIN_AUTH_ENABLED_FLAG | — | — |
| 16 | FromDraftHeaderCbcAccountingDate | CBC_ACCOUNTING_DATE | — | — |
| 17 | FromDraftHeaderChangeRequestedBy | CHANGE_REQUESTED_BY | — | — |
| 18 | FromDraftHeaderChangeSummary | CHANGE_SUMMARY | — | — |
| 19 | FromDraftHeaderClosedDate | CLOSED_DATE | — | — |
| 20 | FromDraftHeaderComments | COMMENTS | — | — |
| 21 | FromDraftHeaderConfirmingOrderFlag | CONFIRMING_ORDER_FLAG | — | — |
| 22 | FromDraftHeaderConsignedConsumptionFlag | CONSIGNED_CONSUMPTION_FLAG | — | — |
| 23 | FromDraftHeaderConsumeReqDemandFlag | CONSUME_REQ_DEMAND_FLAG | — | — |
| 24 | FromDraftHeaderContermsArticlesUpdDate | CONTERMS_ARTICLES_UPD_DATE | — | — |
| 25 | FromDraftHeaderContermsDelivUpdDate | CONTERMS_DELIV_UPD_DATE | — | — |
| 26 | FromDraftHeaderContermsExistFlag | CONTERMS_EXIST_FLAG | — | — |
| 27 | FromDraftHeaderCpaReference | CPA_REFERENCE | — | — |
| 28 | FromDraftHeaderCreatedBy | CREATED_BY | — | — |
| 29 | FromDraftHeaderCreatedLanguage | CREATED_LANGUAGE | — | — |
| 30 | FromDraftHeaderCreationDate | CREATION_DATE | — | — |
| 31 | FromDraftHeaderCurrencyCode | CURRENCY_CODE | — | — |
| 32 | FromDraftHeaderCurrentVersionId | CURRENT_VERSION_ID | — | — |
| 33 | FromDraftHeaderDefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | — |
| 34 | FromDraftHeaderDocumentCreationMethod | DOCUMENT_CREATION_METHOD | — | — |
| 35 | FromDraftHeaderDocumentStatus | DOCUMENT_STATUS | — | — |
| 36 | FromDraftHeaderEdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 37 | FromDraftHeaderEdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 38 | FromDraftHeaderEmailAddress | EMAIL_ADDRESS | — | — |
| 39 | FromDraftHeaderEnabledFlag | ENABLED_FLAG | — | — |
| 40 | FromDraftHeaderEncumbranceRequiredFlag | ENCUMBRANCE_REQUIRED_FLAG | — | — |
| 41 | FromDraftHeaderEndDate | END_DATE | — | — |
| 42 | FromDraftHeaderFax | FAX | — | — |
| 43 | FromDraftHeaderFirmDate | FIRM_DATE | — | — |
| 44 | FromDraftHeaderFirmStatusLookupCode | FIRM_STATUS_LOOKUP_CODE | — | — |
| 45 | FromDraftHeaderFobLookupCode | FOB_LOOKUP_CODE | — | — |
| 46 | FromDraftHeaderFreightTermsLookupCode | FREIGHT_TERMS_LOOKUP_CODE | — | — |
| 47 | FromDraftHeaderFromHeaderId | FROM_HEADER_ID | — | — |
| 48 | FromDraftHeaderFromTypeLookupCode | FROM_TYPE_LOOKUP_CODE | — | — |
| 49 | FromDraftHeaderFrozenFlag | FROZEN_FLAG | — | — |
| 50 | FromDraftHeaderFundsStatus | FUNDS_STATUS | — | ✅ |
| 51 | FromDraftHeaderGenerateOrdersAutomatic | GENERATE_ORDERS_AUTOMATIC | — | — |
| 52 | FromDraftHeaderGovernmentContext | GOVERNMENT_CONTEXT | — | — |
| 53 | FromDraftHeaderGroupRequisitionLines | GROUP_REQUISITION_LINES | — | — |
| 54 | FromDraftHeaderGroupRequisitions | GROUP_REQUISITIONS | — | — |
| 55 | FromDraftHeaderInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | — |
| 56 | FromDraftHeaderJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 57 | FromDraftHeaderJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 58 | FromDraftHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 59 | FromDraftHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 60 | FromDraftHeaderLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 61 | FromDraftHeaderLastUpdatedProgram | LAST_UPDATED_PROGRAM | — | — |
| 62 | FromDraftHeaderMinReleaseAmount | MIN_RELEASE_AMOUNT | — | — |
| 63 | FromDraftHeaderModeOfTransport | MODE_OF_TRANSPORT | — | ✅ |
| 64 | FromDraftHeaderNoteToAuthorizer | NOTE_TO_AUTHORIZER | — | — |
| 65 | FromDraftHeaderNoteToReceiver | NOTE_TO_RECEIVER | — | — |
| 66 | FromDraftHeaderNoteToVendor | NOTE_TO_VENDOR | — | — |
| 67 | FromDraftHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 68 | FromDraftHeaderOrchestrationOrderFlag | ORCHESTRATION_ORDER_FLAG | — | ✅ |
| 69 | FromDraftHeaderPayOnCode | PAY_ON_CODE | — | — |
| 70 | FromDraftHeaderPcardId | PCARD_ID | — | — |
| 71 | FromDraftHeaderPendingSignatureFlag | PENDING_SIGNATURE_FLAG | — | — |
| 72 | FromDraftHeaderPoHeaderId | PO_HEADER_ID | 🔑 | ✅ |
| 73 | FromDraftHeaderPrcBuId | PRC_BU_ID | — | — |
| 74 | FromDraftHeaderPriceUpdateTolerance | PRICE_UPDATE_TOLERANCE | — | — |
| 75 | FromDraftHeaderProgramAppName | PROGRAM_APP_NAME | — | — |
| 76 | FromDraftHeaderProgramName | PROGRAM_NAME | — | — |
| 77 | FromDraftHeaderRate | RATE | — | — |
| 78 | FromDraftHeaderRateDate | RATE_DATE | — | — |
| 79 | FromDraftHeaderRateType | RATE_TYPE | — | — |
| 80 | FromDraftHeaderReferenceNum | REFERENCE_NUM | — | — |
| 81 | FromDraftHeaderReleaseMethod | RELEASE_METHOD | — | — |
| 82 | FromDraftHeaderReqBuId | REQ_BU_ID | — | — |
| 83 | FromDraftHeaderRequestId | REQUEST_ID | — | — |
| 84 | FromDraftHeaderRetroPriceApplyUpdatesFlag | RETRO_PRICE_APPLY_UPDATES_FLAG | — | — |
| 85 | FromDraftHeaderRetroPriceCommUpdatesFlag | RETRO_PRICE_COMM_UPDATES_FLAG | — | — |
| 86 | FromDraftHeaderReviewAutogeneratedReleases | REVIEW_AUTOGENERATED_RELEASES | — | — |
| 87 | FromDraftHeaderRevisedDate | REVISED_DATE | — | — |
| 88 | FromDraftHeaderRevisionNum | REVISION_NUM | — | — |
| 89 | FromDraftHeaderSegment1 | SEGMENT1 | — | — |
| 90 | FromDraftHeaderSegment2 | SEGMENT2 | — | — |
| 91 | FromDraftHeaderSegment3 | SEGMENT3 | — | — |
| 92 | FromDraftHeaderSegment4 | SEGMENT4 | — | — |
| 93 | FromDraftHeaderSegment5 | SEGMENT5 | — | — |
| 94 | FromDraftHeaderServiceLevel | SERVICE_LEVEL | — | ✅ |
| 95 | FromDraftHeaderShipToLocationId | SHIP_TO_LOCATION_ID | — | — |
| 96 | FromDraftHeaderShippingControl | SHIPPING_CONTROL | — | — |
| 97 | FromDraftHeaderSoldtoLeId | SOLDTO_LE_ID | — | ✅ |
| 98 | FromDraftHeaderStartDate | START_DATE | — | — |
| 99 | FromDraftHeaderStyleId | STYLE_ID | — | — |
| 100 | FromDraftHeaderSubmitApprovalAutomatic | SUBMIT_APPROVAL_AUTOMATIC | — | — |
| 101 | FromDraftHeaderSubmitDate | SUBMIT_DATE | — | — |
| 102 | FromDraftHeaderSummaryFlag | SUMMARY_FLAG | — | — |
| 103 | FromDraftHeaderSupplierNotifMethod | SUPPLIER_NOTIF_METHOD | — | — |
| 104 | FromDraftHeaderTaxAttributeUpdateCode | TAX_ATTRIBUTE_UPDATE_CODE | — | — |
| 105 | FromDraftHeaderTaxDocumentSubtype | TAX_DOCUMENT_SUBTYPE | — | — |
| 106 | FromDraftHeaderTermsId | TERMS_ID | — | — |
| 107 | FromDraftHeaderTypeLookupCode | TYPE_LOOKUP_CODE | — | — |
| 108 | FromDraftHeaderUpdateSourcingRulesFlag | UPDATE_SOURCING_RULES_FLAG | — | — |
| 109 | FromDraftHeaderUseNeedByDate | USE_NEED_BY_DATE | — | — |
| 110 | FromDraftHeaderUseShipTo | USE_SHIP_TO | — | — |
| 111 | FromDraftHeaderVendorContactId | VENDOR_CONTACT_ID | — | — |
| 112 | FromDraftHeaderVendorId | VENDOR_ID | — | — |
| 113 | FromDraftHeaderVendorOrderNum | VENDOR_ORDER_NUM | — | — |
| 114 | FromDraftHeaderVendorSiteId | VENDOR_SITE_ID | — | — |
| 115 | FromDraftHeaderXmlChangeSendDate | XML_CHANGE_SEND_DATE | — | — |
| 116 | FromDraftHeaderXmlFlag | XML_FLAG | — | — |
| 117 | FromDraftHeaderXmlSendDate | XML_SEND_DATE | — | — |
| 118 | FromPoHeaderAcceptanceDueDate | ACCEPTANCE_DUE_DATE | — | — |
| 119 | FromPoHeaderAcceptanceRequiredFlag | ACCEPTANCE_REQUIRED_FLAG | — | — |
| 120 | FromPoHeaderAcceptanceWithinDays | ACCEPTANCE_WITHIN_DAYS | — | — |
| 121 | FromPoHeaderAgentId | AGENT_ID | — | — |
| 122 | FromPoHeaderAmountLimit | AMOUNT_LIMIT | — | — |
| 123 | FromPoHeaderAmountReleased | AMOUNT_RELEASED | — | — |
| 124 | FromPoHeaderApprovedDate | APPROVED_DATE | — | — |
| 125 | FromPoHeaderApprovedFlag | APPROVED_FLAG | — | — |
| 126 | FromPoHeaderAutoSourcingFlag | AUTO_SOURCING_FLAG | — | — |
| 127 | FromPoHeaderBillToLocationId | BILL_TO_LOCATION_ID | — | — |
| 128 | FromPoHeaderBilltoBuId | BILLTO_BU_ID | — | ✅ |
| 129 | FromPoHeaderBlanketTotalAmount | BLANKET_TOTAL_AMOUNT | — | — |
| 130 | FromPoHeaderCancelFlag | CANCEL_FLAG | — | — |
| 131 | FromPoHeaderCarrierId | CARRIER_ID | — | — |
| 132 | FromPoHeaderCatAdminAuthEnabledFlag | CAT_ADMIN_AUTH_ENABLED_FLAG | — | — |
| 133 | FromPoHeaderCbcAccountingDate | CBC_ACCOUNTING_DATE | — | — |
| 134 | FromPoHeaderChangeRequestedBy | CHANGE_REQUESTED_BY | — | — |
| 135 | FromPoHeaderChangeSummary | CHANGE_SUMMARY | — | — |
| 136 | FromPoHeaderClosedDate | CLOSED_DATE | — | — |
| 137 | FromPoHeaderComments | COMMENTS | — | — |
| 138 | FromPoHeaderConfirmingOrderFlag | CONFIRMING_ORDER_FLAG | — | — |
| 139 | FromPoHeaderConsignedConsumptionFlag | CONSIGNED_CONSUMPTION_FLAG | — | — |
| 140 | FromPoHeaderConsumeReqDemandFlag | CONSUME_REQ_DEMAND_FLAG | — | — |
| 141 | FromPoHeaderContermsArticlesUpdDate | CONTERMS_ARTICLES_UPD_DATE | — | — |
| 142 | FromPoHeaderContermsDelivUpdDate | CONTERMS_DELIV_UPD_DATE | — | — |
| 143 | FromPoHeaderContermsExistFlag | CONTERMS_EXIST_FLAG | — | — |
| 144 | FromPoHeaderCpaReference | CPA_REFERENCE | — | — |
| 145 | FromPoHeaderCreatedBy | CREATED_BY | — | — |
| 146 | FromPoHeaderCreatedLanguage | CREATED_LANGUAGE | — | — |
| 147 | FromPoHeaderCreationDate | CREATION_DATE | — | — |
| 148 | FromPoHeaderCurrencyCode | CURRENCY_CODE | — | — |
| 149 | FromPoHeaderCurrentVersionId | CURRENT_VERSION_ID | — | — |
| 150 | FromPoHeaderDefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | — |
| 151 | FromPoHeaderDocumentCreationMethod | DOCUMENT_CREATION_METHOD | — | — |
| 152 | FromPoHeaderDocumentStatus | DOCUMENT_STATUS | — | — |
| 153 | FromPoHeaderEdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 154 | FromPoHeaderEdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 155 | FromPoHeaderEmailAddress | EMAIL_ADDRESS | — | — |
| 156 | FromPoHeaderEnabledFlag | ENABLED_FLAG | — | — |
| 157 | FromPoHeaderEncumbranceRequiredFlag | ENCUMBRANCE_REQUIRED_FLAG | — | — |
| 158 | FromPoHeaderEndDate | END_DATE | — | — |
| 159 | FromPoHeaderFax | FAX | — | — |
| 160 | FromPoHeaderFirmDate | FIRM_DATE | — | — |
| 161 | FromPoHeaderFirmStatusLookupCode | FIRM_STATUS_LOOKUP_CODE | — | — |
| 162 | FromPoHeaderFobLookupCode | FOB_LOOKUP_CODE | — | — |
| 163 | FromPoHeaderFreightTermsLookupCode | FREIGHT_TERMS_LOOKUP_CODE | — | — |
| 164 | FromPoHeaderFromHeaderId | FROM_HEADER_ID | — | — |
| 165 | FromPoHeaderFromTypeLookupCode | FROM_TYPE_LOOKUP_CODE | — | — |
| 166 | FromPoHeaderFrozenFlag | FROZEN_FLAG | — | — |
| 167 | FromPoHeaderFundsStatus | FUNDS_STATUS | — | ✅ |
| 168 | FromPoHeaderGenerateOrdersAutomatic | GENERATE_ORDERS_AUTOMATIC | — | — |
| 169 | FromPoHeaderGovernmentContext | GOVERNMENT_CONTEXT | — | — |
| 170 | FromPoHeaderGroupRequisitionLines | GROUP_REQUISITION_LINES | — | — |
| 171 | FromPoHeaderGroupRequisitions | GROUP_REQUISITIONS | — | — |
| 172 | FromPoHeaderInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | — |
| 173 | FromPoHeaderJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 174 | FromPoHeaderJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 175 | FromPoHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 176 | FromPoHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 177 | FromPoHeaderLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 178 | FromPoHeaderLastUpdatedProgram | LAST_UPDATED_PROGRAM | — | — |
| 179 | FromPoHeaderMinReleaseAmount | MIN_RELEASE_AMOUNT | — | — |
| 180 | FromPoHeaderModeOfTransport | MODE_OF_TRANSPORT | — | ✅ |
| 181 | FromPoHeaderNoteToAuthorizer | NOTE_TO_AUTHORIZER | — | — |
| 182 | FromPoHeaderNoteToReceiver | NOTE_TO_RECEIVER | — | — |
| 183 | FromPoHeaderNoteToVendor | NOTE_TO_VENDOR | — | — |
| 184 | FromPoHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 185 | FromPoHeaderOrchestrationOrderFlag | ORCHESTRATION_ORDER_FLAG | — | ✅ |
| 186 | FromPoHeaderPayOnCode | PAY_ON_CODE | — | — |
| 187 | FromPoHeaderPcardId | PCARD_ID | — | — |
| 188 | FromPoHeaderPendingSignatureFlag | PENDING_SIGNATURE_FLAG | — | — |
| 189 | FromPoHeaderPoHeaderId | PO_HEADER_ID | 🔑 | ✅ |
| 190 | FromPoHeaderPrcBuId | PRC_BU_ID | — | — |
| 191 | FromPoHeaderPriceUpdateTolerance | PRICE_UPDATE_TOLERANCE | — | — |
| 192 | FromPoHeaderProgramAppName | PROGRAM_APP_NAME | — | — |
| 193 | FromPoHeaderProgramName | PROGRAM_NAME | — | — |
| 194 | FromPoHeaderRate | RATE | — | — |
| 195 | FromPoHeaderRateDate | RATE_DATE | — | — |
| 196 | FromPoHeaderRateType | RATE_TYPE | — | — |
| 197 | FromPoHeaderReferenceNum | REFERENCE_NUM | — | — |
| 198 | FromPoHeaderReleaseMethod | RELEASE_METHOD | — | — |
| 199 | FromPoHeaderReqBuId | REQ_BU_ID | — | — |
| 200 | FromPoHeaderRequestId | REQUEST_ID | — | — |
| 201 | FromPoHeaderRetroPriceApplyUpdatesFlag | RETRO_PRICE_APPLY_UPDATES_FLAG | — | — |
| 202 | FromPoHeaderRetroPriceCommUpdatesFlag | RETRO_PRICE_COMM_UPDATES_FLAG | — | — |
| 203 | FromPoHeaderReviewAutogeneratedReleases | REVIEW_AUTOGENERATED_RELEASES | — | — |
| 204 | FromPoHeaderRevisedDate | REVISED_DATE | — | — |
| 205 | FromPoHeaderRevisionNum | REVISION_NUM | — | — |
| 206 | FromPoHeaderSegment1 | SEGMENT1 | — | — |
| 207 | FromPoHeaderSegment2 | SEGMENT2 | — | — |
| 208 | FromPoHeaderSegment3 | SEGMENT3 | — | — |
| 209 | FromPoHeaderSegment4 | SEGMENT4 | — | — |
| 210 | FromPoHeaderSegment5 | SEGMENT5 | — | — |
| 211 | FromPoHeaderServiceLevel | SERVICE_LEVEL | — | ✅ |
| 212 | FromPoHeaderShipToLocationId | SHIP_TO_LOCATION_ID | — | — |
| 213 | FromPoHeaderShippingControl | SHIPPING_CONTROL | — | — |
| 214 | FromPoHeaderSoldtoLeId | SOLDTO_LE_ID | — | ✅ |
| 215 | FromPoHeaderStartDate | START_DATE | — | — |
| 216 | FromPoHeaderStyleId | STYLE_ID | — | — |
| 217 | FromPoHeaderSubmitApprovalAutomatic | SUBMIT_APPROVAL_AUTOMATIC | — | — |
| 218 | FromPoHeaderSubmitDate | SUBMIT_DATE | — | — |
| 219 | FromPoHeaderSummaryFlag | SUMMARY_FLAG | — | — |
| 220 | FromPoHeaderSupplierNotifMethod | SUPPLIER_NOTIF_METHOD | — | — |
| 221 | FromPoHeaderTaxAttributeUpdateCode | TAX_ATTRIBUTE_UPDATE_CODE | — | — |
| 222 | FromPoHeaderTaxDocumentSubtype | TAX_DOCUMENT_SUBTYPE | — | — |
| 223 | FromPoHeaderTermsId | TERMS_ID | — | — |
| 224 | FromPoHeaderTypeLookupCode | TYPE_LOOKUP_CODE | — | — |
| 225 | FromPoHeaderUpdateSourcingRulesFlag | UPDATE_SOURCING_RULES_FLAG | — | — |
| 226 | FromPoHeaderUseNeedByDate | USE_NEED_BY_DATE | — | — |
| 227 | FromPoHeaderUseShipTo | USE_SHIP_TO | — | — |
| 228 | FromPoHeaderVendorContactId | VENDOR_CONTACT_ID | — | — |
| 229 | FromPoHeaderVendorId | VENDOR_ID | — | — |
| 230 | FromPoHeaderVendorOrderNum | VENDOR_ORDER_NUM | — | — |
| 231 | FromPoHeaderVendorSiteId | VENDOR_SITE_ID | — | — |
| 232 | FromPoHeaderXmlChangeSendDate | XML_CHANGE_SEND_DATE | — | — |
| 233 | FromPoHeaderXmlFlag | XML_FLAG | — | — |
| 234 | FromPoHeaderXmlSendDate | XML_SEND_DATE | — | — |
| 235 | PoHeaderAcceptanceDueDate | ACCEPTANCE_DUE_DATE | — | — |
| 236 | PoHeaderAcceptanceRequiredFlag | ACCEPTANCE_REQUIRED_FLAG | — | — |
| 237 | PoHeaderAcceptanceWithinDays | ACCEPTANCE_WITHIN_DAYS | — | — |
| 238 | PoHeaderAgentId | AGENT_ID | — | ✅ |
| 239 | PoHeaderAmountLimit | AMOUNT_LIMIT | — | — |
| 240 | PoHeaderAmountReleased | AMOUNT_RELEASED | — | — |
| 241 | PoHeaderApprovedDate | APPROVED_DATE | — | — |
| 242 | PoHeaderApprovedFlag | APPROVED_FLAG | — | — |
| 243 | PoHeaderAutoSourcingFlag | AUTO_SOURCING_FLAG | — | — |
| 244 | PoHeaderBillToLocationId | BILL_TO_LOCATION_ID | — | — |
| 245 | PoHeaderBilltoBuId | BILLTO_BU_ID | — | ✅ |
| 246 | PoHeaderBlanketTotalAmount | BLANKET_TOTAL_AMOUNT | — | — |
| 247 | PoHeaderBuyerManagedTransportFlag | BUYER_MANAGED_TRANSPORT_FLAG | — | ✅ |
| 248 | PoHeaderCancelFlag | CANCEL_FLAG | — | — |
| 249 | PoHeaderCarrierId | CARRIER_ID | — | — |
| 250 | PoHeaderCatAdminAuthEnabledFlag | CAT_ADMIN_AUTH_ENABLED_FLAG | — | — |
| 251 | PoHeaderCbcAccountingDate | CBC_ACCOUNTING_DATE | — | — |
| 252 | PoHeaderChangeRequestedBy | CHANGE_REQUESTED_BY | — | — |
| 253 | PoHeaderChangeSummary | CHANGE_SUMMARY | — | — |
| 254 | PoHeaderClosedDate | CLOSED_DATE | — | — |
| 255 | PoHeaderComments | COMMENTS | — | — |
| 256 | PoHeaderConfirmingOrderFlag | CONFIRMING_ORDER_FLAG | — | — |
| 257 | PoHeaderConsignedConsumptionFlag | CONSIGNED_CONSUMPTION_FLAG | — | — |
| 258 | PoHeaderConsumeReqDemandFlag | CONSUME_REQ_DEMAND_FLAG | — | — |
| 259 | PoHeaderContermsArticlesUpdDate | CONTERMS_ARTICLES_UPD_DATE | — | — |
| 260 | PoHeaderContermsDelivUpdDate | CONTERMS_DELIV_UPD_DATE | — | — |
| 261 | PoHeaderContermsExistFlag | CONTERMS_EXIST_FLAG | — | — |
| 262 | PoHeaderCpaReference | CPA_REFERENCE | — | — |
| 263 | PoHeaderCreatedBy | CREATED_BY | — | — |
| 264 | PoHeaderCreatedLanguage | CREATED_LANGUAGE | — | — |
| 265 | PoHeaderCreationDate | CREATION_DATE | — | — |
| 266 | PoHeaderCurrencyCode | CURRENCY_CODE | — | — |
| 267 | PoHeaderCurrentVersionId | CURRENT_VERSION_ID | — | — |
| 268 | PoHeaderDefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | — |
| 269 | PoHeaderDocumentCreationMethod | DOCUMENT_CREATION_METHOD | — | — |
| 270 | PoHeaderDocumentStatus | DOCUMENT_STATUS | — | — |
| 271 | PoHeaderEdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 272 | PoHeaderEdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 273 | PoHeaderEmailAddress | EMAIL_ADDRESS | — | — |
| 274 | PoHeaderEnabledFlag | ENABLED_FLAG | — | — |
| 275 | PoHeaderEncumbranceRequiredFlag | ENCUMBRANCE_REQUIRED_FLAG | — | — |
| 276 | PoHeaderEndDate | END_DATE | — | — |
| 277 | PoHeaderFax | FAX | — | — |
| 278 | PoHeaderFirmDate | FIRM_DATE | — | — |
| 279 | PoHeaderFirmStatusLookupCode | FIRM_STATUS_LOOKUP_CODE | — | — |
| 280 | PoHeaderFobLookupCode | FOB_LOOKUP_CODE | — | — |
| 281 | PoHeaderFreightTermsLookupCode | FREIGHT_TERMS_LOOKUP_CODE | — | — |
| 282 | PoHeaderFromHeaderId | FROM_HEADER_ID | — | — |
| 283 | PoHeaderFromTypeLookupCode | FROM_TYPE_LOOKUP_CODE | — | — |
| 284 | PoHeaderFrozenFlag | FROZEN_FLAG | — | — |
| 285 | PoHeaderFundsStatus | FUNDS_STATUS | — | ✅ |
| 286 | PoHeaderGenerateOrdersAutomatic | GENERATE_ORDERS_AUTOMATIC | — | — |
| 287 | PoHeaderGovernmentContext | GOVERNMENT_CONTEXT | — | — |
| 288 | PoHeaderGroupRequisitionLines | GROUP_REQUISITION_LINES | — | — |
| 289 | PoHeaderGroupRequisitions | GROUP_REQUISITIONS | — | — |
| 290 | PoHeaderInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | — |
| 291 | PoHeaderJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 292 | PoHeaderJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 293 | PoHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 294 | PoHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 295 | PoHeaderLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 296 | PoHeaderLastUpdatedProgram | LAST_UPDATED_PROGRAM | — | — |
| 297 | PoHeaderMinReleaseAmount | MIN_RELEASE_AMOUNT | — | — |
| 298 | PoHeaderModeOfTransport | MODE_OF_TRANSPORT | — | ✅ |
| 299 | PoHeaderNoteToAuthorizer | NOTE_TO_AUTHORIZER | — | — |
| 300 | PoHeaderNoteToReceiver | NOTE_TO_RECEIVER | — | — |
| 301 | PoHeaderNoteToVendor | NOTE_TO_VENDOR | — | — |
| 302 | PoHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 303 | PoHeaderOrchestrationOrderFlag | ORCHESTRATION_ORDER_FLAG | — | ✅ |
| 304 | PoHeaderPayOnCode | PAY_ON_CODE | — | — |
| 305 | PoHeaderPcardId | PCARD_ID | — | — |
| 306 | PoHeaderPendingSignatureFlag | PENDING_SIGNATURE_FLAG | — | — |
| 307 | PoHeaderPoHeaderId | PO_HEADER_ID | 🔑 | ✅ |
| 308 | PoHeaderPrcBuId | PRC_BU_ID | — | ✅ |
| 309 | PoHeaderPriceUpdateTolerance | PRICE_UPDATE_TOLERANCE | — | — |
| 310 | PoHeaderProgramAppName | PROGRAM_APP_NAME | — | — |
| 311 | PoHeaderProgramName | PROGRAM_NAME | — | — |
| 312 | PoHeaderRate | RATE | — | — |
| 313 | PoHeaderRateDate | RATE_DATE | — | — |
| 314 | PoHeaderRateType | RATE_TYPE | — | — |
| 315 | PoHeaderReferenceNum | REFERENCE_NUM | — | — |
| 316 | PoHeaderReleaseMethod | RELEASE_METHOD | — | — |
| 317 | PoHeaderReqBuId | REQ_BU_ID | — | ✅ |
| 318 | PoHeaderRequestId | REQUEST_ID | — | — |
| 319 | PoHeaderRetroPriceApplyUpdatesFlag | RETRO_PRICE_APPLY_UPDATES_FLAG | — | — |
| 320 | PoHeaderRetroPriceCommUpdatesFlag | RETRO_PRICE_COMM_UPDATES_FLAG | — | — |
| 321 | PoHeaderReviewAutogeneratedReleases | REVIEW_AUTOGENERATED_RELEASES | — | — |
| 322 | PoHeaderRevisedDate | REVISED_DATE | — | — |
| 323 | PoHeaderRevisionNum | REVISION_NUM | — | — |
| 324 | PoHeaderSegment1 | SEGMENT1 | — | ✅ |
| 325 | PoHeaderSegment2 | SEGMENT2 | — | — |
| 326 | PoHeaderSegment3 | SEGMENT3 | — | — |
| 327 | PoHeaderSegment4 | SEGMENT4 | — | — |
| 328 | PoHeaderSegment5 | SEGMENT5 | — | — |
| 329 | PoHeaderServiceLevel | SERVICE_LEVEL | — | ✅ |
| 330 | PoHeaderShipToLocationId | SHIP_TO_LOCATION_ID | — | — |
| 331 | PoHeaderShippingControl | SHIPPING_CONTROL | — | — |
| 332 | PoHeaderSoldtoLeId | SOLDTO_LE_ID | — | ✅ |
| 333 | PoHeaderStartDate | START_DATE | — | — |
| 334 | PoHeaderStyleId | STYLE_ID | — | — |
| 335 | PoHeaderSubmitApprovalAutomatic | SUBMIT_APPROVAL_AUTOMATIC | — | — |
| 336 | PoHeaderSubmitDate | SUBMIT_DATE | — | — |
| 337 | PoHeaderSummaryFlag | SUMMARY_FLAG | — | — |
| 338 | PoHeaderSupplierNotifMethod | SUPPLIER_NOTIF_METHOD | — | — |
| 339 | PoHeaderTaxAttributeUpdateCode | TAX_ATTRIBUTE_UPDATE_CODE | — | — |
| 340 | PoHeaderTaxDocumentSubtype | TAX_DOCUMENT_SUBTYPE | — | — |
| 341 | PoHeaderTermsId | TERMS_ID | — | — |
| 342 | PoHeaderTypeLookupCode | TYPE_LOOKUP_CODE | — | ✅ |
| 343 | PoHeaderUpdateSourcingRulesFlag | UPDATE_SOURCING_RULES_FLAG | — | — |
| 344 | PoHeaderUseNeedByDate | USE_NEED_BY_DATE | — | — |
| 345 | PoHeaderUseShipTo | USE_SHIP_TO | — | — |
| 346 | PoHeaderVendorContactId | VENDOR_CONTACT_ID | — | — |
| 347 | PoHeaderVendorId | VENDOR_ID | — | ✅ |
| 348 | PoHeaderVendorOrderNum | VENDOR_ORDER_NUM | — | — |
| 349 | PoHeaderVendorSiteId | VENDOR_SITE_ID | — | ✅ |
| 350 | PoHeaderXmlChangeSendDate | XML_CHANGE_SEND_DATE | — | — |
| 351 | PoHeaderXmlFlag | XML_FLAG | — | — |
| 352 | PoHeaderXmlSendDate | XML_SEND_DATE | — | — |

### [[po_headers_archive_all|PO_HEADERS_ARCHIVE_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ArchivedPOHeaderAcceptanceDueDate | ACCEPTANCE_DUE_DATE | — | — |
| 2 | ArchivedPOHeaderAcceptanceRequiredFlag | ACCEPTANCE_REQUIRED_FLAG | — | — |
| 3 | ArchivedPOHeaderAgentId | AGENT_ID | — | — |
| 4 | ArchivedPOHeaderAgingOnsetPoint | AGING_ONSET_POINT | — | ✅ |
| 5 | ArchivedPOHeaderAgingPeriodDays | AGING_PERIOD_DAYS | — | ✅ |
| 6 | ArchivedPOHeaderAmountLimit | AMOUNT_LIMIT | — | — |
| 7 | ArchivedPOHeaderAutoSourcingFlag | AUTO_SOURCING_FLAG | — | — |
| 8 | ArchivedPOHeaderBillToLocationId | BILL_TO_LOCATION_ID | — | — |
| 9 | ArchivedPOHeaderBillingCycleClosingDate | BILLING_CYCLE_CLOSING_DATE | — | ✅ |
| 10 | ArchivedPOHeaderBilltoBuId | BILLTO_BU_ID | — | ✅ |
| 11 | ArchivedPOHeaderBlanketTotalAmount | BLANKET_TOTAL_AMOUNT | — | — |
| 12 | ArchivedPOHeaderBuyerManagedTransportFlag | BUYER_MANAGED_TRANSPORT_FLAG | — | — |
| 13 | ArchivedPOHeaderCancelFlag | CANCEL_FLAG | — | — |
| 14 | ArchivedPOHeaderCarrierId | CARRIER_ID | — | — |
| 15 | ArchivedPOHeaderCbcAccountingDate | CBC_ACCOUNTING_DATE | — | — |
| 16 | ArchivedPOHeaderChangeRequestedBy | CHANGE_REQUESTED_BY | — | — |
| 17 | ArchivedPOHeaderChangeSummary | CHANGE_SUMMARY | — | — |
| 18 | ArchivedPOHeaderComments | COMMENTS | — | ✅ |
| 19 | ArchivedPOHeaderConfirmingOrderFlag | CONFIRMING_ORDER_FLAG | — | — |
| 20 | ArchivedPOHeaderConsignedConsumptionFlag | CONSIGNED_CONSUMPTION_FLAG | — | — |
| 21 | ArchivedPOHeaderConsumeReqDemandFlag | CONSUME_REQ_DEMAND_FLAG | — | — |
| 22 | ArchivedPOHeaderConsumptionAdviceFrequency | CONSUMPTION_ADVICE_FREQUENCY | — | ✅ |
| 23 | ArchivedPOHeaderConsumptionAdviceSummary | CONSUMPTION_ADVICE_SUMMARY | — | ✅ |
| 24 | ArchivedPOHeaderContermsArticlesUpdDate | CONTERMS_ARTICLES_UPD_DATE | — | — |
| 25 | ArchivedPOHeaderContermsDelivUpdDate | CONTERMS_DELIV_UPD_DATE | — | — |
| 26 | ArchivedPOHeaderContermsExistFlag | CONTERMS_EXIST_FLAG | — | — |
| 27 | ArchivedPOHeaderCpaReference | CPA_REFERENCE | — | — |
| 28 | ArchivedPOHeaderCreatedBy | CREATED_BY | — | — |
| 29 | ArchivedPOHeaderCreatedLanguage | CREATED_LANGUAGE | — | — |
| 30 | ArchivedPOHeaderCreationDate | CREATION_DATE | — | — |
| 31 | ArchivedPOHeaderCurrencyCode | CURRENCY_CODE | — | — |
| 32 | ArchivedPOHeaderDefaultConsignmentLineFlag | DEFAULT_CONSIGNMENT_LINE_FLAG | — | ✅ |
| 33 | ArchivedPOHeaderDefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | — |
| 34 | ArchivedPOHeaderDocumentCreationMethod | DOCUMENT_CREATION_METHOD | — | — |
| 35 | ArchivedPOHeaderEmailAddress | EMAIL_ADDRESS | — | — |
| 36 | ArchivedPOHeaderEnabledFlag | ENABLED_FLAG | — | — |
| 37 | ArchivedPOHeaderEncumbranceRequiredFlag | ENCUMBRANCE_REQUIRED_FLAG | — | — |
| 38 | ArchivedPOHeaderEndDate | END_DATE | — | — |
| 39 | ArchivedPOHeaderEntityCoDisposition | ENTITY_CO_DISPOSITION | — | — |
| 40 | ArchivedPOHeaderFax | FAX | — | — |
| 41 | ArchivedPOHeaderFirmDate | FIRM_DATE | — | — |
| 42 | ArchivedPOHeaderFirmStatusLookupCode | FIRM_STATUS_LOOKUP_CODE | — | — |
| 43 | ArchivedPOHeaderFobLookupCode | FOB_LOOKUP_CODE | — | — |
| 44 | ArchivedPOHeaderFreightTermsLookupCode | FREIGHT_TERMS_LOOKUP_CODE | — | — |
| 45 | ArchivedPOHeaderFromCoSeq | FROM_CO_SEQ | 🔑 | ✅ |
| 46 | ArchivedPOHeaderFromHeaderId | FROM_HEADER_ID | — | — |
| 47 | ArchivedPOHeaderFromTypeLookupCode | FROM_TYPE_LOOKUP_CODE | — | — |
| 48 | ArchivedPOHeaderGenerateOrdersAutomatic | GENERATE_ORDERS_AUTOMATIC | — | — |
| 49 | ArchivedPOHeaderGovernmentContext | GOVERNMENT_CONTEXT | — | — |
| 50 | ArchivedPOHeaderGroupRequisitionLines | GROUP_REQUISITION_LINES | — | — |
| 51 | ArchivedPOHeaderGroupRequisitions | GROUP_REQUISITIONS | — | — |
| 52 | ArchivedPOHeaderInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | — |
| 53 | ArchivedPOHeaderJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 54 | ArchivedPOHeaderJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 55 | ArchivedPOHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 56 | ArchivedPOHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 57 | ArchivedPOHeaderLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 58 | ArchivedPOHeaderMinReleaseAmount | MIN_RELEASE_AMOUNT | — | — |
| 59 | ArchivedPOHeaderModeOfTransport | MODE_OF_TRANSPORT | — | ✅ |
| 60 | ArchivedPOHeaderNoteToAuthorizer | NOTE_TO_AUTHORIZER | — | — |
| 61 | ArchivedPOHeaderNoteToReceiver | NOTE_TO_RECEIVER | — | — |
| 62 | ArchivedPOHeaderNoteToVendor | NOTE_TO_VENDOR | — | — |
| 63 | ArchivedPOHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 64 | ArchivedPOHeaderOrchestrationOrderFlag | ORCHESTRATION_ORDER_FLAG | — | ✅ |
| 65 | ArchivedPOHeaderPayOnCode | PAY_ON_CODE | — | — |
| 66 | ArchivedPOHeaderPayOnUseFlag | PAY_ON_USE_FLAG | — | ✅ |
| 67 | ArchivedPOHeaderPcardId | PCARD_ID | — | — |
| 68 | ArchivedPOHeaderPendingSignatureFlag | PENDING_SIGNATURE_FLAG | — | — |
| 69 | ArchivedPOHeaderPoHeaderId | PO_HEADER_ID | 🔑 | ✅ |
| 70 | ArchivedPOHeaderPrcBuId | PRC_BU_ID | — | — |
| 71 | ArchivedPOHeaderPriceUpdateTolerance | PRICE_UPDATE_TOLERANCE | — | — |
| 72 | ArchivedPOHeaderProgramAppName | PROGRAM_APP_NAME | — | — |
| 73 | ArchivedPOHeaderProgramName | PROGRAM_NAME | — | — |
| 74 | ArchivedPOHeaderRate | RATE | — | — |
| 75 | ArchivedPOHeaderRateDate | RATE_DATE | — | — |
| 76 | ArchivedPOHeaderRateType | RATE_TYPE | — | — |
| 77 | ArchivedPOHeaderReferenceNum | REFERENCE_NUM | — | — |
| 78 | ArchivedPOHeaderReqBuId | REQ_BU_ID | — | — |
| 79 | ArchivedPOHeaderRequestId | REQUEST_ID | — | — |
| 80 | ArchivedPOHeaderRetroPriceApplyUpdatesFlag | RETRO_PRICE_APPLY_UPDATES_FLAG | — | — |
| 81 | ArchivedPOHeaderRetroPriceCommUpdatesFlag | RETRO_PRICE_COMM_UPDATES_FLAG | — | — |
| 82 | ArchivedPOHeaderSegment1 | SEGMENT1 | — | — |
| 83 | ArchivedPOHeaderSegment2 | SEGMENT2 | — | — |
| 84 | ArchivedPOHeaderSegment3 | SEGMENT3 | — | — |
| 85 | ArchivedPOHeaderSegment4 | SEGMENT4 | — | — |
| 86 | ArchivedPOHeaderSegment5 | SEGMENT5 | — | — |
| 87 | ArchivedPOHeaderServiceLevel | SERVICE_LEVEL | — | ✅ |
| 88 | ArchivedPOHeaderShipToLocationId | SHIP_TO_LOCATION_ID | — | — |
| 89 | ArchivedPOHeaderShippingControl | SHIPPING_CONTROL | — | — |
| 90 | ArchivedPOHeaderSoldtoLeId | SOLDTO_LE_ID | — | ✅ |
| 91 | ArchivedPOHeaderStartDate | START_DATE | — | — |
| 92 | ArchivedPOHeaderStyleId | STYLE_ID | — | — |
| 93 | ArchivedPOHeaderSubmitApprovalAutomatic | SUBMIT_APPROVAL_AUTOMATIC | — | — |
| 94 | ArchivedPOHeaderSubmitDate | SUBMIT_DATE | — | — |
| 95 | ArchivedPOHeaderSummaryFlag | SUMMARY_FLAG | — | — |
| 96 | ArchivedPOHeaderSupplierNotifMethod | SUPPLIER_NOTIF_METHOD | — | — |
| 97 | ArchivedPOHeaderTaxDocumentSubtype | TAX_DOCUMENT_SUBTYPE | — | — |
| 98 | ArchivedPOHeaderTermsId | TERMS_ID | — | — |
| 99 | ArchivedPOHeaderToCoSeq | TO_CO_SEQ | — | — |
| 100 | ArchivedPOHeaderTypeLookupCode | TYPE_LOOKUP_CODE | — | — |
| 101 | ArchivedPOHeaderUpdateSourcingRulesFlag | UPDATE_SOURCING_RULES_FLAG | — | — |
| 102 | ArchivedPOHeaderUseNeedByDate | USE_NEED_BY_DATE | — | — |
| 103 | ArchivedPOHeaderUseShipTo | USE_SHIP_TO | — | — |
| 104 | ArchivedPOHeaderVendorContactId | VENDOR_CONTACT_ID | — | — |
| 105 | ArchivedPOHeaderVendorId | VENDOR_ID | — | — |
| 106 | ArchivedPOHeaderVendorOrderNum | VENDOR_ORDER_NUM | — | — |
| 107 | ArchivedPOHeaderVendorSiteId | VENDOR_SITE_ID | — | — |
| 108 | ArchivedPOHeaderXmlFlag | XML_FLAG | — | — |

### [[po_headers_draft_all|PO_HEADERS_DRAFT_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DraftHeaderAcceptanceDueDate | ACCEPTANCE_DUE_DATE | — | — |
| 2 | DraftHeaderAcceptanceRequiredFlag | ACCEPTANCE_REQUIRED_FLAG | — | — |
| 3 | DraftHeaderAcceptanceWithinDays | ACCEPTANCE_WITHIN_DAYS | — | — |
| 4 | DraftHeaderAgentId | AGENT_ID | — | — |
| 5 | DraftHeaderAmountLimit | AMOUNT_LIMIT | — | — |
| 6 | DraftHeaderAutoSourcingFlag | AUTO_SOURCING_FLAG | — | — |
| 7 | DraftHeaderBillToLocationId | BILL_TO_LOCATION_ID | — | — |
| 8 | DraftHeaderBilltoBuId | BILLTO_BU_ID | — | ✅ |
| 9 | DraftHeaderBlanketTotalAmount | BLANKET_TOTAL_AMOUNT | — | — |
| 10 | DraftHeaderBuyerManagedTransportFlag | BUYER_MANAGED_TRANSPORT_FLAG | — | ✅ |
| 11 | DraftHeaderCancelFlag | CANCEL_FLAG | — | — |
| 12 | DraftHeaderCarrierId | CARRIER_ID | — | — |
| 13 | DraftHeaderCbcAccountingDate | CBC_ACCOUNTING_DATE | — | — |
| 14 | DraftHeaderChangeAcceptedFlag | CHANGE_ACCEPTED_FLAG | — | — |
| 15 | DraftHeaderChangeRequestedBy | CHANGE_REQUESTED_BY | — | — |
| 16 | DraftHeaderChangeSummary | CHANGE_SUMMARY | — | — |
| 17 | DraftHeaderComments | COMMENTS | — | — |
| 18 | DraftHeaderConfirmingOrderFlag | CONFIRMING_ORDER_FLAG | — | — |
| 19 | DraftHeaderConsignedConsumptionFlag | CONSIGNED_CONSUMPTION_FLAG | — | — |
| 20 | DraftHeaderConsumeReqDemandFlag | CONSUME_REQ_DEMAND_FLAG | — | — |
| 21 | DraftHeaderContermsArticlesUpdDate | CONTERMS_ARTICLES_UPD_DATE | — | — |
| 22 | DraftHeaderContermsDelivUpdDate | CONTERMS_DELIV_UPD_DATE | — | — |
| 23 | DraftHeaderContermsExistFlag | CONTERMS_EXIST_FLAG | — | — |
| 24 | DraftHeaderCpaReference | CPA_REFERENCE | — | — |
| 25 | DraftHeaderCreatedBy | CREATED_BY | — | — |
| 26 | DraftHeaderCreatedLanguage | CREATED_LANGUAGE | — | — |
| 27 | DraftHeaderCreationDate | CREATION_DATE | — | — |
| 28 | DraftHeaderCurrencyCode | CURRENCY_CODE | — | — |
| 29 | DraftHeaderDefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | — |
| 30 | DraftHeaderDocumentCreationMethod | DOCUMENT_CREATION_METHOD | — | — |
| 31 | DraftHeaderEmailAddress | EMAIL_ADDRESS | — | — |
| 32 | DraftHeaderEnabledFlag | ENABLED_FLAG | — | — |
| 33 | DraftHeaderEncumbranceRequiredFlag | ENCUMBRANCE_REQUIRED_FLAG | — | — |
| 34 | DraftHeaderEndDate | END_DATE | — | — |
| 35 | DraftHeaderEntityChangeTypeCode | ENTITY_CHANGE_TYPE_CODE | — | — |
| 36 | DraftHeaderExternalChangeFlag | EXTERNAL_CHANGE_FLAG | — | — |
| 37 | DraftHeaderFax | FAX | — | — |
| 38 | DraftHeaderFirmDate | FIRM_DATE | — | — |
| 39 | DraftHeaderFirmStatusLookupCode | FIRM_STATUS_LOOKUP_CODE | — | — |
| 40 | DraftHeaderFobLookupCode | FOB_LOOKUP_CODE | — | — |
| 41 | DraftHeaderFreightTermsLookupCode | FREIGHT_TERMS_LOOKUP_CODE | — | — |
| 42 | DraftHeaderFromHeaderId | FROM_HEADER_ID | — | — |
| 43 | DraftHeaderFromTypeLookupCode | FROM_TYPE_LOOKUP_CODE | — | — |
| 44 | DraftHeaderFundsStatus | FUNDS_STATUS | — | ✅ |
| 45 | DraftHeaderGenerateOrdersAutomatic | GENERATE_ORDERS_AUTOMATIC | — | — |
| 46 | DraftHeaderGovernmentContext | GOVERNMENT_CONTEXT | — | — |
| 47 | DraftHeaderGroupRequisitionLines | GROUP_REQUISITION_LINES | — | — |
| 48 | DraftHeaderGroupRequisitions | GROUP_REQUISITIONS | — | — |
| 49 | DraftHeaderInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | — |
| 50 | DraftHeaderJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 51 | DraftHeaderJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 52 | DraftHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 53 | DraftHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 54 | DraftHeaderLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 55 | DraftHeaderMinReleaseAmount | MIN_RELEASE_AMOUNT | — | — |
| 56 | DraftHeaderModeOfTransport | MODE_OF_TRANSPORT | — | ✅ |
| 57 | DraftHeaderNoteToAuthorizer | NOTE_TO_AUTHORIZER | — | — |
| 58 | DraftHeaderNoteToReceiver | NOTE_TO_RECEIVER | — | — |
| 59 | DraftHeaderNoteToVendor | NOTE_TO_VENDOR | — | — |
| 60 | DraftHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 61 | DraftHeaderOrchestrationOrderFlag | ORCHESTRATION_ORDER_FLAG | — | ✅ |
| 62 | DraftHeaderPayOnCode | PAY_ON_CODE | — | — |
| 63 | DraftHeaderPcardId | PCARD_ID | — | — |
| 64 | DraftHeaderPendingSignatureFlag | PENDING_SIGNATURE_FLAG | — | — |
| 65 | DraftHeaderPoHeaderId | PO_HEADER_ID | 🔑 | ✅ |
| 66 | DraftHeaderPrcBuId | PRC_BU_ID | — | — |
| 67 | DraftHeaderPriceUpdateTolerance | PRICE_UPDATE_TOLERANCE | — | — |
| 68 | DraftHeaderProgramAppName | PROGRAM_APP_NAME | — | — |
| 69 | DraftHeaderProgramName | PROGRAM_NAME | — | — |
| 70 | DraftHeaderRate | RATE | — | — |
| 71 | DraftHeaderRateDate | RATE_DATE | — | — |
| 72 | DraftHeaderRateType | RATE_TYPE | — | — |
| 73 | DraftHeaderReasonForChange | REASON_FOR_CHANGE | — | — |
| 74 | DraftHeaderReferenceNum | REFERENCE_NUM | — | — |
| 75 | DraftHeaderReqBuId | REQ_BU_ID | — | — |
| 76 | DraftHeaderRequestId | REQUEST_ID | — | — |
| 77 | DraftHeaderRetroPriceApplyUpdatesFlag | RETRO_PRICE_APPLY_UPDATES_FLAG | — | — |
| 78 | DraftHeaderRetroPriceCommUpdatesFlag | RETRO_PRICE_COMM_UPDATES_FLAG | — | — |
| 79 | DraftHeaderSegment1 | SEGMENT1 | — | — |
| 80 | DraftHeaderSegment2 | SEGMENT2 | — | — |
| 81 | DraftHeaderSegment3 | SEGMENT3 | — | — |
| 82 | DraftHeaderSegment4 | SEGMENT4 | — | — |
| 83 | DraftHeaderSegment5 | SEGMENT5 | — | — |
| 84 | DraftHeaderServiceLevel | SERVICE_LEVEL | — | ✅ |
| 85 | DraftHeaderShipToLocationId | SHIP_TO_LOCATION_ID | — | — |
| 86 | DraftHeaderShippingControl | SHIPPING_CONTROL | — | — |
| 87 | DraftHeaderSoldtoLeId | SOLDTO_LE_ID | — | ✅ |
| 88 | DraftHeaderStartDate | START_DATE | — | — |
| 89 | DraftHeaderStyleId | STYLE_ID | — | — |
| 90 | DraftHeaderSubmitApprovalAutomatic | SUBMIT_APPROVAL_AUTOMATIC | — | — |
| 91 | DraftHeaderSubmitDate | SUBMIT_DATE | — | — |
| 92 | DraftHeaderSummaryFlag | SUMMARY_FLAG | — | — |
| 93 | DraftHeaderSupplierNotifMethod | SUPPLIER_NOTIF_METHOD | — | — |
| 94 | DraftHeaderTaxAttributeUpdateCode | TAX_ATTRIBUTE_UPDATE_CODE | — | — |
| 95 | DraftHeaderTaxDocumentSubtype | TAX_DOCUMENT_SUBTYPE | — | — |
| 96 | DraftHeaderTermsId | TERMS_ID | — | — |
| 97 | DraftHeaderTypeLookupCode | TYPE_LOOKUP_CODE | — | — |
| 98 | DraftHeaderUpdateSourcingRulesFlag | UPDATE_SOURCING_RULES_FLAG | — | — |
| 99 | DraftHeaderUseNeedByDate | USE_NEED_BY_DATE | — | — |
| 100 | DraftHeaderUseShipTo | USE_SHIP_TO | — | — |
| 101 | DraftHeaderVendorContactId | VENDOR_CONTACT_ID | — | — |
| 102 | DraftHeaderVendorId | VENDOR_ID | — | — |
| 103 | DraftHeaderVendorOrderNum | VENDOR_ORDER_NUM | — | — |
| 104 | DraftHeaderVendorSiteId | VENDOR_SITE_ID | — | — |
| 105 | DraftHeaderXmlFlag | XML_FLAG | — | — |

### [[po_versions|PO_VERSIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PurchasingDocumentVersionAcceptedDate | ACCEPTED_DATE | — | ✅ |
| 2 | PurchasingDocumentVersionApprovedDate | APPROVED_DATE | — | ✅ |
| 3 | PurchasingDocumentVersionCancelBackingReqFlag | CANCEL_BACKING_REQ_FLAG | — | — |
| 4 | PurchasingDocumentVersionCancelDocFlag | CANCEL_DOC_FLAG | — | ✅ |
| 5 | PurchasingDocumentVersionChangeOrderDesc | CHANGE_ORDER_DESC | — | ✅ |
| 6 | PurchasingDocumentVersionChangeOrderStatus | CHANGE_ORDER_STATUS | — | ✅ |
| 7 | PurchasingDocumentVersionChangeOrderType | CHANGE_ORDER_TYPE | — | ✅ |
| 8 | PurchasingDocumentVersionChecklistId | CHECKLIST_ID | — | — |
| 9 | PurchasingDocumentVersionCoCanceledByRole | CO_CANCELED_BY_ROLE | — | — |
| 10 | PurchasingDocumentVersionCoCanceledByUserId | CO_CANCELED_BY_USER_ID | — | — |
| 11 | PurchasingDocumentVersionCoCanceledFlag | CO_CANCELED_FLAG | — | ✅ |
| 12 | PurchasingDocumentVersionCoNum | CO_NUM | — | ✅ |
| 13 | PurchasingDocumentVersionCoSequence | CO_SEQUENCE | — | ✅ |
| 14 | PurchasingDocumentVersionCommunicatedDate | COMMUNICATED_DATE | — | ✅ |
| 15 | PurchasingDocumentVersionCommunicatedToSupplier | COMMUNICATED_TO_SUPPLIER | — | — |
| 16 | PurchasingDocumentVersionCreatedBy | CREATED_BY | — | ✅ |
| 17 | PurchasingDocumentVersionCreatedByProgramName | CREATED_BY_PROGRAM_NAME | — | ✅ |
| 18 | PurchasingDocumentVersionCreationDate | CREATION_DATE | — | ✅ |
| 19 | PurchasingDocumentVersionDocumentDate | DOCUMENT_DATE | — | — |
| 20 | PurchasingDocumentVersionExternalSystemFlag | EXTERNAL_SYSTEM_FLAG | — | — |
| 21 | PurchasingDocumentVersionFundsStatus | FUNDS_STATUS | — | ✅ |
| 22 | PurchasingDocumentVersionJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 23 | PurchasingDocumentVersionJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 24 | PurchasingDocumentVersionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 25 | PurchasingDocumentVersionLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 26 | PurchasingDocumentVersionLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 27 | PurchasingDocumentVersionModifiedFlag | MODIFIED_FLAG | — | — |
| 28 | PurchasingDocumentVersionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 29 | PurchasingDocumentVersionOnlineReportId | ONLINE_REPORT_ID | — | — |
| 30 | PurchasingDocumentVersionOriginatorId | ORIGINATOR_ID | — | ✅ |
| 31 | PurchasingDocumentVersionOriginatorRole | ORIGINATOR_ROLE | — | ✅ |
| 32 | PurchasingDocumentVersionPendingResponseRole | PENDING_RESPONSE_ROLE | — | — |
| 33 | PurchasingDocumentVersionPoHeaderId | PO_HEADER_ID | — | ✅ |
| 34 | PurchasingDocumentVersionProcessedDate | PROCESSED_DATE | — | ✅ |
| 35 | PurchasingDocumentVersionProgramAppName | PROGRAM_APP_NAME | — | — |
| 36 | PurchasingDocumentVersionProgramName | PROGRAM_NAME | — | — |
| 37 | PurchasingDocumentVersionRejectedFlag | REJECTED_FLAG | — | ✅ |
| 38 | PurchasingDocumentVersionRequestDate | REQUEST_DATE | — | — |
| 39 | PurchasingDocumentVersionRequestId | REQUEST_ID | — | — |
| 40 | PurchasingDocumentVersionRevisionNum | REVISION_NUM | — | ✅ |
| 41 | PurchasingDocumentVersionSubmittedDate | SUBMITTED_DATE | — | ✅ |
| 42 | PurchasingDocumentVersionWithdrawnFlag | WITHDRAWN_FLAG | — | ✅ |
| 43 | VersionId | VERSION_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
