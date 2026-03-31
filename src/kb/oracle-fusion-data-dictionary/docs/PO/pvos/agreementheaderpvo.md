---
id: DOC-PO-PVO-AgreementHeaderPVO
doc_type: system-doc
title: "AgreementHeaderPVO — PVO Purchasing"
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
  - AgreementHeaderPVO
  - agreementheaderpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AgreementHeaderPVO

## 📌 Visão Geral

Extrai os cabeçalhos de contratos e acordos de compra (Blanket e Contract Purchase Agreements), incluindo fornecedor, valores-limite, vigência, moeda e status de aprovação. Permite gestão centralizada de contratos, monitoramento de consumo versus valor acordado e compliance com termos negociados.

**Caminho:** `FscmTopModelAM.PrcPoPublicViewAM.AgreementHeaderPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 457 | 8 | 1 | 59 | 13% |

---

## 🔗 Tabelas Relacionadas

- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 21 atributos
- [[hz_parties|HZ_PARTIES]] — 16 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 23 atributos
- [[po_action_history|PO_ACTION_HISTORY]] — 16 atributos
- [[po_headers_all|PO_HEADERS_ALL]] — 260 atributos (1 PKs, 57 BICC)
- [[po_system_parameters_all|PO_SYSTEM_PARAMETERS_ALL]] — 71 atributos (1 BICC)
- [[po_versions_init_sequence_v|PO_VERSIONS_INIT_SEQUENCE_V]] — 42 atributos (1 BICC)
- [[zx_fc_document_fiscal_v|ZX_FC_DOCUMENT_FISCAL_V]] — 8 atributos

---

## ⚙️ Atributos

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BillToBUBusinessUnitId | BU_ID | — | — |
| 2 | BillToBUCreatedBy | CREATED_BY | — | — |
| 3 | BillToBUCreationDate | CREATION_DATE | — | — |
| 4 | BillToBUDateFrom | DATE_FROM | — | — |
| 5 | BillToBUDateTo | DATE_TO | — | — |
| 6 | BillToBUDefaultCurrencyCode | DEFAULT_CURRENCY_CODE | — | — |
| 7 | BillToBUDefaultSetId | DEFAULT_SET_ID | — | — |
| 8 | BillToBUEnabledForHrFlag | ENABLED_FOR_HR_FLAG | — | — |
| 9 | BillToBUEnterpriseId | BUSINESS_GROUP_ID | — | — |
| 10 | BillToBUFinancialsBusinessUnitId | FIN_BUSINESS_UNIT_ID | — | — |
| 11 | BillToBULastUpdateDate | LAST_UPDATE_DATE | — | — |
| 12 | BillToBULastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | BillToBULastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | BillToBULegalEntityId | LEGAL_ENTITY_ID | — | — |
| 15 | BillToBULocationId | LOCATION_ID | — | — |
| 16 | BillToBUManagerId | MANAGER_ID | — | — |
| 17 | BillToBUName | BU_NAME | — | — |
| 18 | BillToBUPrimaryLedgerId | PRIMARY_LEDGER_ID | — | — |
| 19 | BillToBUProfitCenterFlag | PROFIT_CENTER_FLAG | — | — |
| 20 | BillToBUShortCode | SHORT_CODE | — | — |
| 21 | BillToBUStatus | STATUS | — | — |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DocumentCancelledByPartyAddress1 | ADDRESS1 | — | — |
| 2 | DocumentCancelledByPartyAddress2 | ADDRESS2 | — | — |
| 3 | DocumentCancelledByPartyAddress3 | ADDRESS3 | — | — |
| 4 | DocumentCancelledByPartyAddress4 | ADDRESS4 | — | — |
| 5 | DocumentCancelledByPartyCity | CITY | — | — |
| 6 | DocumentCancelledByPartyCountry | COUNTRY | — | — |
| 7 | DocumentCancelledByPartyCounty | COUNTY | — | — |
| 8 | DocumentCancelledByPartyPartyId | PARTY_ID | — | — |
| 9 | DocumentCancelledByPartyPartyName | PARTY_NAME | — | — |
| 10 | DocumentCancelledByPartyPartyNumber | PARTY_NUMBER | — | — |
| 11 | DocumentCancelledByPartyPostalCode | POSTAL_CODE | — | — |
| 12 | DocumentCancelledByPartyPreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | — |
| 13 | DocumentCancelledByPartyPreferredName | PREFERRED_NAME | — | — |
| 14 | DocumentCancelledByPartyProvince | PROVINCE | — | — |
| 15 | DocumentCancelledByPartyState | STATE | — | — |
| 16 | DocumentCancelledByPartyStatus | STATUS | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DocumentCancelledByPersonDisplayName | DISPLAY_NAME | — | — |
| 2 | DocumentCancelledByPersonEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | DocumentCancelledByPersonEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | DocumentCancelledByPersonFirstName | FIRST_NAME | — | — |
| 5 | DocumentCancelledByPersonFullName | FULL_NAME | — | — |
| 6 | DocumentCancelledByPersonHonors | HONORS | — | — |
| 7 | DocumentCancelledByPersonKnownAs | KNOWN_AS | — | — |
| 8 | DocumentCancelledByPersonLastName | LAST_NAME | — | — |
| 9 | DocumentCancelledByPersonListName | LIST_NAME | — | — |
| 10 | DocumentCancelledByPersonMiddleNames | MIDDLE_NAMES | — | — |
| 11 | DocumentCancelledByPersonMilitaryRank | MILITARY_RANK | — | — |
| 12 | DocumentCancelledByPersonNameType | NAME_TYPE | — | — |
| 13 | DocumentCancelledByPersonPersonNameId | PERSON_NAME_ID | — | — |
| 14 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 15 | EffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 16 | EffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 17 | EffectiveStartDate1 | EFFECTIVE_START_DATE | — | — |
| 18 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 19 | OverridingApproverDisplayName | DISPLAY_NAME | — | — |
| 20 | OverridingApproverListName | LIST_NAME | — | — |
| 21 | OverridingApproverPersonNameId | PERSON_NAME_ID | — | — |
| 22 | PersonNameId | PERSON_NAME_ID | — | — |
| 23 | PurchasingDocumentHeaderLastUpdatedByName | DISPLAY_NAME | — | — |

### [[po_action_history|PO_ACTION_HISTORY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DocumentCancelActionActionCode | ACTION_CODE | — | — |
| 2 | DocumentCancelActionActionDate | ACTION_DATE | — | — |
| 3 | DocumentCancelActionActionLevel | ACTION_LEVEL | — | — |
| 4 | DocumentCancelActionIdentificationKey | IDENTIFICATION_KEY | — | — |
| 5 | DocumentCancelActionNote | NOTE | — | — |
| 6 | DocumentCancelActionObjectId | OBJECT_ID | — | — |
| 7 | DocumentCancelActionObjectRevisionNum | OBJECT_REVISION_NUM | — | — |
| 8 | DocumentCancelActionObjectSubTypeCode | OBJECT_SUB_TYPE_CODE | — | — |
| 9 | DocumentCancelActionObjectTypeCode | OBJECT_TYPE_CODE | — | — |
| 10 | DocumentCancelActionOfflineCode | OFFLINE_CODE | — | — |
| 11 | DocumentCancelActionPerformerId | PERFORMER_ID | — | — |
| 12 | DocumentCancelActionPoVersionId | PO_VERSION_ID | — | — |
| 13 | DocumentCancelActionProgramDate | PROGRAM_DATE | — | — |
| 14 | DocumentCancelActionRoleCode | ROLE_CODE | — | — |
| 15 | DocumentCancelActionSequenceNum | SEQUENCE_NUM | — | — |
| 16 | DocumentCancelActionSupplierAccessibleFlag | SUPPLIER_ACCESSIBLE_FLAG | — | — |

### [[po_headers_all|PO_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FromPurchaseOrderAcceptanceDueDate | ACCEPTANCE_DUE_DATE | — | — |
| 2 | FromPurchaseOrderAcceptanceRequiredFlag | ACCEPTANCE_REQUIRED_FLAG | — | — |
| 3 | FromPurchaseOrderAcceptanceWithinDays | ACCEPTANCE_WITHIN_DAYS | — | — |
| 4 | FromPurchaseOrderAgentId | AGENT_ID | — | — |
| 5 | FromPurchaseOrderAmountLimit | AMOUNT_LIMIT | — | — |
| 6 | FromPurchaseOrderAmountReleased | AMOUNT_RELEASED | — | — |
| 7 | FromPurchaseOrderApprovedDate | APPROVED_DATE | — | — |
| 8 | FromPurchaseOrderApprovedFlag | APPROVED_FLAG | — | — |
| 9 | FromPurchaseOrderAutoSourcingFlag | AUTO_SOURCING_FLAG | — | — |
| 10 | FromPurchaseOrderBillToLocationId | BILL_TO_LOCATION_ID | — | — |
| 11 | FromPurchaseOrderBilltoBuId | BILLTO_BU_ID | — | — |
| 12 | FromPurchaseOrderBlanketTotalAmount | BLANKET_TOTAL_AMOUNT | — | — |
| 13 | FromPurchaseOrderBudgetControlEnabledFlag | BUDGET_CONTROL_ENABLED_FLAG | — | — |
| 14 | FromPurchaseOrderCancelFlag | CANCEL_FLAG | — | — |
| 15 | FromPurchaseOrderCarrierId | CARRIER_ID | — | — |
| 16 | FromPurchaseOrderCatAdminAuthEnabledFlag | CAT_ADMIN_AUTH_ENABLED_FLAG | — | — |
| 17 | FromPurchaseOrderCbcAccountingDate | CBC_ACCOUNTING_DATE | — | — |
| 18 | FromPurchaseOrderChangeRequestedBy | CHANGE_REQUESTED_BY | — | — |
| 19 | FromPurchaseOrderChangeSummary | CHANGE_SUMMARY | — | — |
| 20 | FromPurchaseOrderClosedDate | CLOSED_DATE | — | — |
| 21 | FromPurchaseOrderComments | COMMENTS | — | — |
| 22 | FromPurchaseOrderConfirmingOrderFlag | CONFIRMING_ORDER_FLAG | — | — |
| 23 | FromPurchaseOrderConsignedConsumptionFlag | CONSIGNED_CONSUMPTION_FLAG | — | — |
| 24 | FromPurchaseOrderConsumeReqDemandFlag | CONSUME_REQ_DEMAND_FLAG | — | — |
| 25 | FromPurchaseOrderContermsArticlesUpdDate | CONTERMS_ARTICLES_UPD_DATE | — | — |
| 26 | FromPurchaseOrderContermsDelivUpdDate | CONTERMS_DELIV_UPD_DATE | — | — |
| 27 | FromPurchaseOrderContermsExistFlag | CONTERMS_EXIST_FLAG | — | — |
| 28 | FromPurchaseOrderCpaReference | CPA_REFERENCE | — | — |
| 29 | FromPurchaseOrderCreatedLanguage | CREATED_LANGUAGE | — | — |
| 30 | FromPurchaseOrderCurrencyCode | CURRENCY_CODE | — | — |
| 31 | FromPurchaseOrderCurrentVersionId | CURRENT_VERSION_ID | — | — |
| 32 | FromPurchaseOrderDefaultPoTradeOrgId | DEFAULT_PO_TRADE_ORG_ID | — | — |
| 33 | FromPurchaseOrderDefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | — |
| 34 | FromPurchaseOrderDocumentCreationMethod | DOCUMENT_CREATION_METHOD | — | — |
| 35 | FromPurchaseOrderDocumentStatus | DOCUMENT_STATUS | — | — |
| 36 | FromPurchaseOrderEdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 37 | FromPurchaseOrderEdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 38 | FromPurchaseOrderEmailAddress | EMAIL_ADDRESS | — | — |
| 39 | FromPurchaseOrderEnabledFlag | ENABLED_FLAG | — | — |
| 40 | FromPurchaseOrderEncumbranceRequiredFlag | ENCUMBRANCE_REQUIRED_FLAG | — | — |
| 41 | FromPurchaseOrderEndDate | END_DATE | — | — |
| 42 | FromPurchaseOrderFax | FAX | — | — |
| 43 | FromPurchaseOrderFirmDate | FIRM_DATE | — | — |
| 44 | FromPurchaseOrderFirmStatusLookupCode | FIRM_STATUS_LOOKUP_CODE | — | — |
| 45 | FromPurchaseOrderFobLookupCode | FOB_LOOKUP_CODE | — | — |
| 46 | FromPurchaseOrderFreightTermsLookupCode | FREIGHT_TERMS_LOOKUP_CODE | — | — |
| 47 | FromPurchaseOrderFromHeaderId | FROM_HEADER_ID | — | — |
| 48 | FromPurchaseOrderFromTypeLookupCode | FROM_TYPE_LOOKUP_CODE | — | — |
| 49 | FromPurchaseOrderFrozenFlag | FROZEN_FLAG | — | — |
| 50 | FromPurchaseOrderFundsStatus | FUNDS_STATUS | — | — |
| 51 | FromPurchaseOrderGenerateOrdersAutomatic | GENERATE_ORDERS_AUTOMATIC | — | — |
| 52 | FromPurchaseOrderGovernmentContext | GOVERNMENT_CONTEXT | — | — |
| 53 | FromPurchaseOrderGroupRequisitionLines | GROUP_REQUISITION_LINES | — | — |
| 54 | FromPurchaseOrderGroupRequisitions | GROUP_REQUISITIONS | — | — |
| 55 | FromPurchaseOrderInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | — |
| 56 | FromPurchaseOrderJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 57 | FromPurchaseOrderJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 58 | FromPurchaseOrderLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 59 | FromPurchaseOrderLastUpdatedProgram | LAST_UPDATED_PROGRAM | — | — |
| 60 | FromPurchaseOrderMinReleaseAmount | MIN_RELEASE_AMOUNT | — | — |
| 61 | FromPurchaseOrderModeOfTransport | MODE_OF_TRANSPORT | — | — |
| 62 | FromPurchaseOrderNoteToAuthorizer | NOTE_TO_AUTHORIZER | — | — |
| 63 | FromPurchaseOrderNoteToReceiver | NOTE_TO_RECEIVER | — | — |
| 64 | FromPurchaseOrderNoteToVendor | NOTE_TO_VENDOR | — | — |
| 65 | FromPurchaseOrderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 66 | FromPurchaseOrderOrchestrationOrderFlag | ORCHESTRATION_ORDER_FLAG | — | — |
| 67 | FromPurchaseOrderPayOnCode | PAY_ON_CODE | — | — |
| 68 | FromPurchaseOrderPcardId | PCARD_ID | — | — |
| 69 | FromPurchaseOrderPendingSignatureFlag | PENDING_SIGNATURE_FLAG | — | — |
| 70 | FromPurchaseOrderPoHeaderId | PO_HEADER_ID | — | — |
| 71 | FromPurchaseOrderPrcBuId | PRC_BU_ID | — | — |
| 72 | FromPurchaseOrderPriceUpdateTolerance | PRICE_UPDATE_TOLERANCE | — | — |
| 73 | FromPurchaseOrderProgramAppName | PROGRAM_APP_NAME | — | — |
| 74 | FromPurchaseOrderProgramName | PROGRAM_NAME | — | — |
| 75 | FromPurchaseOrderRate | RATE | — | — |
| 76 | FromPurchaseOrderRateDate | RATE_DATE | — | — |
| 77 | FromPurchaseOrderRateType | RATE_TYPE | — | — |
| 78 | FromPurchaseOrderReferenceNum | REFERENCE_NUM | — | — |
| 79 | FromPurchaseOrderReleaseMethod | RELEASE_METHOD | — | — |
| 80 | FromPurchaseOrderReqBuId | REQ_BU_ID | — | — |
| 81 | FromPurchaseOrderRequestId | REQUEST_ID | — | — |
| 82 | FromPurchaseOrderRetroPriceApplyUpdatesFlag | RETRO_PRICE_APPLY_UPDATES_FLAG | — | — |
| 83 | FromPurchaseOrderRetroPriceCommUpdatesFlag | RETRO_PRICE_COMM_UPDATES_FLAG | — | — |
| 84 | FromPurchaseOrderReviewAutogeneratedReleases | REVIEW_AUTOGENERATED_RELEASES | — | — |
| 85 | FromPurchaseOrderRevisedDate | REVISED_DATE | — | — |
| 86 | FromPurchaseOrderRevisionNum | REVISION_NUM | — | — |
| 87 | FromPurchaseOrderSegment1 | SEGMENT1 | — | — |
| 88 | FromPurchaseOrderSegment2 | SEGMENT2 | — | — |
| 89 | FromPurchaseOrderSegment3 | SEGMENT3 | — | — |
| 90 | FromPurchaseOrderSegment4 | SEGMENT4 | — | — |
| 91 | FromPurchaseOrderSegment5 | SEGMENT5 | — | — |
| 92 | FromPurchaseOrderServiceLevel | SERVICE_LEVEL | — | — |
| 93 | FromPurchaseOrderShipToLocationId | SHIP_TO_LOCATION_ID | — | — |
| 94 | FromPurchaseOrderShippingControl | SHIPPING_CONTROL | — | — |
| 95 | FromPurchaseOrderSoldtoLeId | SOLDTO_LE_ID | — | — |
| 96 | FromPurchaseOrderStartDate | START_DATE | — | — |
| 97 | FromPurchaseOrderStyleId | STYLE_ID | — | — |
| 98 | FromPurchaseOrderSubmitApprovalAutomatic | SUBMIT_APPROVAL_AUTOMATIC | — | — |
| 99 | FromPurchaseOrderSubmitDate | SUBMIT_DATE | — | — |
| 100 | FromPurchaseOrderSummaryFlag | SUMMARY_FLAG | — | — |
| 101 | FromPurchaseOrderSupplierNotifMethod | SUPPLIER_NOTIF_METHOD | — | — |
| 102 | FromPurchaseOrderTaxAttributeUpdateCode | TAX_ATTRIBUTE_UPDATE_CODE | — | — |
| 103 | FromPurchaseOrderTaxDocumentSubtype | TAX_DOCUMENT_SUBTYPE | — | — |
| 104 | FromPurchaseOrderTermsId | TERMS_ID | — | — |
| 105 | FromPurchaseOrderTypeLookupCode | TYPE_LOOKUP_CODE | — | — |
| 106 | FromPurchaseOrderUpdateSourcingRulesFlag | UPDATE_SOURCING_RULES_FLAG | — | — |
| 107 | FromPurchaseOrderUseNeedByDate | USE_NEED_BY_DATE | — | — |
| 108 | FromPurchaseOrderUseShipTo | USE_SHIP_TO | — | — |
| 109 | FromPurchaseOrderVendorContactId | VENDOR_CONTACT_ID | — | — |
| 110 | FromPurchaseOrderVendorId | VENDOR_ID | — | — |
| 111 | FromPurchaseOrderVendorOrderNum | VENDOR_ORDER_NUM | — | — |
| 112 | FromPurchaseOrderVendorSiteId | VENDOR_SITE_ID | — | — |
| 113 | FromPurchaseOrderXmlChangeSendDate | XML_CHANGE_SEND_DATE | — | — |
| 114 | FromPurchaseOrderXmlFlag | XML_FLAG | — | — |
| 115 | FromPurchaseOrderXmlSendDate | XML_SEND_DATE | — | — |
| 116 | OverridingApproverId | OVERRIDING_APPROVER_ID | — | — |
| 117 | PoHeaderId | PO_HEADER_ID | 🔑 | ✅ |
| 118 | PurchasingDocumentHeaderAcceptanceDueDate | ACCEPTANCE_DUE_DATE | — | ✅ |
| 119 | PurchasingDocumentHeaderAcceptanceRequiredFlag | ACCEPTANCE_REQUIRED_FLAG | — | ✅ |
| 120 | PurchasingDocumentHeaderAcceptanceWithinDays | ACCEPTANCE_WITHIN_DAYS | — | — |
| 121 | PurchasingDocumentHeaderAdditionalContactEmailAddress | ALT_CONTACT_EMAIL_ADDRESS | — | — |
| 122 | PurchasingDocumentHeaderAgentId | AGENT_ID | — | ✅ |
| 123 | PurchasingDocumentHeaderAgingOnsetPoint | AGING_ONSET_POINT | — | ✅ |
| 124 | PurchasingDocumentHeaderAgingPeriodDays | AGING_PERIOD_DAYS | — | ✅ |
| 125 | PurchasingDocumentHeaderAmountLimit | AMOUNT_LIMIT | — | ✅ |
| 126 | PurchasingDocumentHeaderAmountReleased | AMOUNT_RELEASED | — | ✅ |
| 127 | PurchasingDocumentHeaderApprovedDate | APPROVED_DATE | — | — |
| 128 | PurchasingDocumentHeaderApprovedFlag | APPROVED_FLAG | — | — |
| 129 | PurchasingDocumentHeaderAutoSourcingFlag | AUTO_SOURCING_FLAG | — | — |
| 130 | PurchasingDocumentHeaderBccEmailAddress | BCC_EMAIL_ADDRESS | — | — |
| 131 | PurchasingDocumentHeaderBillToLocationId | BILL_TO_LOCATION_ID | — | — |
| 132 | PurchasingDocumentHeaderBillingCycleClosingDate | BILLING_CYCLE_CLOSING_DATE | — | ✅ |
| 133 | PurchasingDocumentHeaderBilltoBuId | BILLTO_BU_ID | — | — |
| 134 | PurchasingDocumentHeaderBlanketTotalAmount | BLANKET_TOTAL_AMOUNT | — | ✅ |
| 135 | PurchasingDocumentHeaderBudgetControlEnabledFlag | BUDGET_CONTROL_ENABLED_FLAG | — | — |
| 136 | PurchasingDocumentHeaderBuyerManagedTransportFlag | BUYER_MANAGED_TRANSPORT_FLAG | — | ✅ |
| 137 | PurchasingDocumentHeaderCancelFlag | CANCEL_FLAG | — | — |
| 138 | PurchasingDocumentHeaderCarrierId | CARRIER_ID | — | — |
| 139 | PurchasingDocumentHeaderCatAdminAuthEnabledFlag | CAT_ADMIN_AUTH_ENABLED_FLAG | — | — |
| 140 | PurchasingDocumentHeaderCbcAccountingDate | CBC_ACCOUNTING_DATE | — | — |
| 141 | PurchasingDocumentHeaderCcEmailAddress | CC_EMAIL_ADDRESS | — | — |
| 142 | PurchasingDocumentHeaderChangeRequestedBy | CHANGE_REQUESTED_BY | — | — |
| 143 | PurchasingDocumentHeaderChangeSummary | CHANGE_SUMMARY | — | — |
| 144 | PurchasingDocumentHeaderChecklistId | CHECKLIST_ID | — | — |
| 145 | PurchasingDocumentHeaderClosedDate | CLOSED_DATE | — | — |
| 146 | PurchasingDocumentHeaderComments | COMMENTS | — | ✅ |
| 147 | PurchasingDocumentHeaderConfirmingOrderFlag | CONFIRMING_ORDER_FLAG | — | ✅ |
| 148 | PurchasingDocumentHeaderConsignedConsumptionFlag | CONSIGNED_CONSUMPTION_FLAG | — | — |
| 149 | PurchasingDocumentHeaderConsumeReqDemandFlag | CONSUME_REQ_DEMAND_FLAG | — | — |
| 150 | PurchasingDocumentHeaderConsumptionAdviceFrequency | CONSUMPTION_ADVICE_FREQUENCY | — | ✅ |
| 151 | PurchasingDocumentHeaderConsumptionAdviceSummary | CONSUMPTION_ADVICE_SUMMARY | — | ✅ |
| 152 | PurchasingDocumentHeaderContermsArticlesUpdDate | CONTERMS_ARTICLES_UPD_DATE | — | — |
| 153 | PurchasingDocumentHeaderContermsDelivUpdDate | CONTERMS_DELIV_UPD_DATE | — | — |
| 154 | PurchasingDocumentHeaderContermsExistFlag | CONTERMS_EXIST_FLAG | — | — |
| 155 | PurchasingDocumentHeaderCpaReference | CPA_REFERENCE | — | — |
| 156 | PurchasingDocumentHeaderCreatedBy | CREATED_BY | — | ✅ |
| 157 | PurchasingDocumentHeaderCreatedLanguage | CREATED_LANGUAGE | — | — |
| 158 | PurchasingDocumentHeaderCreationDate | CREATION_DATE | — | ✅ |
| 159 | PurchasingDocumentHeaderCurrencyCode | CURRENCY_CODE | — | ✅ |
| 160 | PurchasingDocumentHeaderCurrentVersionId | CURRENT_VERSION_ID | — | — |
| 161 | PurchasingDocumentHeaderDefaultConsignmentLineFlag | DEFAULT_CONSIGNMENT_LINE_FLAG | — | — |
| 162 | PurchasingDocumentHeaderDefaultPoTradeOrgId | DEFAULT_PO_TRADE_ORG_ID | — | — |
| 163 | PurchasingDocumentHeaderDefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | — |
| 164 | PurchasingDocumentHeaderDisableAutosourcingFlag | DISABLE_AUTOSOURCING_FLAG | — | — |
| 165 | PurchasingDocumentHeaderDocumentCreationMethod | DOCUMENT_CREATION_METHOD | — | — |
| 166 | PurchasingDocumentHeaderDocumentStatus | DOCUMENT_STATUS | — | ✅ |
| 167 | PurchasingDocumentHeaderEdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 168 | PurchasingDocumentHeaderEdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 169 | PurchasingDocumentHeaderEmailAddress | EMAIL_ADDRESS | — | — |
| 170 | PurchasingDocumentHeaderEnabledFlag | ENABLED_FLAG | — | — |
| 171 | PurchasingDocumentHeaderEncumbranceRequiredFlag | ENCUMBRANCE_REQUIRED_FLAG | — | — |
| 172 | PurchasingDocumentHeaderEndDate | END_DATE | — | ✅ |
| 173 | PurchasingDocumentHeaderFax | FAX | — | — |
| 174 | PurchasingDocumentHeaderFirmDate | FIRM_DATE | — | — |
| 175 | PurchasingDocumentHeaderFirmStatusLookupCode | FIRM_STATUS_LOOKUP_CODE | — | — |
| 176 | PurchasingDocumentHeaderFobLookupCode | FOB_LOOKUP_CODE | — | — |
| 177 | PurchasingDocumentHeaderFreightTermsLookupCode | FREIGHT_TERMS_LOOKUP_CODE | — | — |
| 178 | PurchasingDocumentHeaderFromHeaderId | FROM_HEADER_ID | — | — |
| 179 | PurchasingDocumentHeaderFromTypeLookupCode | FROM_TYPE_LOOKUP_CODE | — | — |
| 180 | PurchasingDocumentHeaderFrozenFlag | FROZEN_FLAG | — | — |
| 181 | PurchasingDocumentHeaderFundsStatus | FUNDS_STATUS | — | — |
| 182 | PurchasingDocumentHeaderGenerateOrdersAutomatic | GENERATE_ORDERS_AUTOMATIC | — | ✅ |
| 183 | PurchasingDocumentHeaderGenerateOrdersAutomaticContract | GENERATE_ORDERS_AUTOMATIC | — | ✅ |
| 184 | PurchasingDocumentHeaderGovernmentContext | GOVERNMENT_CONTEXT | — | — |
| 185 | PurchasingDocumentHeaderGroupRequisitionLines | GROUP_REQUISITION_LINES | — | ✅ |
| 186 | PurchasingDocumentHeaderGroupRequisitionLinesContract | GROUP_REQUISITION_LINES | — | ✅ |
| 187 | PurchasingDocumentHeaderGroupRequisitions | GROUP_REQUISITIONS | — | ✅ |
| 188 | PurchasingDocumentHeaderGroupRequisitionsContract | GROUP_REQUISITIONS | — | ✅ |
| 189 | PurchasingDocumentHeaderInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | ✅ |
| 190 | PurchasingDocumentHeaderJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 191 | PurchasingDocumentHeaderJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 192 | PurchasingDocumentHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 193 | PurchasingDocumentHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 194 | PurchasingDocumentHeaderLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 195 | PurchasingDocumentHeaderLastUpdatedProgram | LAST_UPDATED_PROGRAM | — | — |
| 196 | PurchasingDocumentHeaderMasterContractId | MASTER_CONTRACT_ID | — | ✅ |
| 197 | PurchasingDocumentHeaderMinReleaseAmount | MIN_RELEASE_AMOUNT | — | ✅ |
| 198 | PurchasingDocumentHeaderModeOfTransport | MODE_OF_TRANSPORT | — | ✅ |
| 199 | PurchasingDocumentHeaderNoteToAuthorizer | NOTE_TO_AUTHORIZER | — | — |
| 200 | PurchasingDocumentHeaderNoteToReceiver | NOTE_TO_RECEIVER | — | ✅ |
| 201 | PurchasingDocumentHeaderNoteToVendor | NOTE_TO_VENDOR | — | ✅ |
| 202 | PurchasingDocumentHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 203 | PurchasingDocumentHeaderOrchestrationOrderFlag | ORCHESTRATION_ORDER_FLAG | — | — |
| 204 | PurchasingDocumentHeaderPayOnCode | PAY_ON_CODE | — | ✅ |
| 205 | PurchasingDocumentHeaderPayOnUseFlag | PAY_ON_USE_FLAG | — | ✅ |
| 206 | PurchasingDocumentHeaderPcardId | PCARD_ID | — | — |
| 207 | PurchasingDocumentHeaderPendingSignatureFlag | PENDING_SIGNATURE_FLAG | — | — |
| 208 | PurchasingDocumentHeaderPrcBuId | PRC_BU_ID | — | ✅ |
| 209 | PurchasingDocumentHeaderPriceUpdateTolerance | PRICE_UPDATE_TOLERANCE | — | — |
| 210 | PurchasingDocumentHeaderProgramAppName | PROGRAM_APP_NAME | — | — |
| 211 | PurchasingDocumentHeaderProgramName | PROGRAM_NAME | — | — |
| 212 | PurchasingDocumentHeaderRate | RATE | — | ✅ |
| 213 | PurchasingDocumentHeaderRateDate | RATE_DATE | — | ✅ |
| 214 | PurchasingDocumentHeaderRateType | RATE_TYPE | — | ✅ |
| 215 | PurchasingDocumentHeaderReferenceNum | REFERENCE_NUM | — | — |
| 216 | PurchasingDocumentHeaderReleaseMethod | RELEASE_METHOD | — | — |
| 217 | PurchasingDocumentHeaderReqBuId | REQ_BU_ID | — | ✅ |
| 218 | PurchasingDocumentHeaderRequestId | REQUEST_ID | — | — |
| 219 | PurchasingDocumentHeaderRetroPriceApplyUpdatesFlag | RETRO_PRICE_APPLY_UPDATES_FLAG | — | ✅ |
| 220 | PurchasingDocumentHeaderRetroPriceCommUpdatesFlag | RETRO_PRICE_COMM_UPDATES_FLAG | — | ✅ |
| 221 | PurchasingDocumentHeaderReviewAutogeneratedReleases | REVIEW_AUTOGENERATED_RELEASES | — | — |
| 222 | PurchasingDocumentHeaderRevisedDate | REVISED_DATE | — | — |
| 223 | PurchasingDocumentHeaderRevisionNum | REVISION_NUM | — | — |
| 224 | PurchasingDocumentHeaderSegment1 | SEGMENT1 | — | ✅ |
| 225 | PurchasingDocumentHeaderSegment2 | SEGMENT2 | — | — |
| 226 | PurchasingDocumentHeaderSegment3 | SEGMENT3 | — | — |
| 227 | PurchasingDocumentHeaderSegment4 | SEGMENT4 | — | — |
| 228 | PurchasingDocumentHeaderSegment5 | SEGMENT5 | — | — |
| 229 | PurchasingDocumentHeaderServiceLevel | SERVICE_LEVEL | — | ✅ |
| 230 | PurchasingDocumentHeaderShipToLocationId | SHIP_TO_LOCATION_ID | — | — |
| 231 | PurchasingDocumentHeaderShippingControl | SHIPPING_CONTROL | — | — |
| 232 | PurchasingDocumentHeaderSkipElectronicCommFlag | SKIP_ELECTRONIC_COMM_FLAG | — | — |
| 233 | PurchasingDocumentHeaderSoldtoLeId | SOLDTO_LE_ID | — | — |
| 234 | PurchasingDocumentHeaderSourcingPriority | SOURCING_PRIORITY | — | — |
| 235 | PurchasingDocumentHeaderSpecialHandlingTypeCode | SPECIAL_HANDLING_TYPE_CODE | — | — |
| 236 | PurchasingDocumentHeaderStartDate | START_DATE | — | ✅ |
| 237 | PurchasingDocumentHeaderStyleId | STYLE_ID | — | — |
| 238 | PurchasingDocumentHeaderSubmitApprovalAutomatic | SUBMIT_APPROVAL_AUTOMATIC | — | ✅ |
| 239 | PurchasingDocumentHeaderSubmitApprovalAutomaticContract | SUBMIT_APPROVAL_AUTOMATIC | — | ✅ |
| 240 | PurchasingDocumentHeaderSubmitDate | SUBMIT_DATE | — | — |
| 241 | PurchasingDocumentHeaderSummaryFlag | SUMMARY_FLAG | — | — |
| 242 | PurchasingDocumentHeaderSupplierNotifMethod | SUPPLIER_NOTIF_METHOD | — | ✅ |
| 243 | PurchasingDocumentHeaderTaxAttributeUpdateCode | TAX_ATTRIBUTE_UPDATE_CODE | — | — |
| 244 | PurchasingDocumentHeaderTaxDocumentSubtype | TAX_DOCUMENT_SUBTYPE | — | — |
| 245 | PurchasingDocumentHeaderTermsId | TERMS_ID | — | — |
| 246 | PurchasingDocumentHeaderTypeLookupCode | TYPE_LOOKUP_CODE | — | ✅ |
| 247 | PurchasingDocumentHeaderUpdateSourcingRulesFlag | UPDATE_SOURCING_RULES_FLAG | — | — |
| 248 | PurchasingDocumentHeaderUseNeedByDate | USE_NEED_BY_DATE | — | ✅ |
| 249 | PurchasingDocumentHeaderUseNeedByDateContract | USE_NEED_BY_DATE | — | ✅ |
| 250 | PurchasingDocumentHeaderUseSalesOrderNumberFlag | USE_SALES_ORDER_NUMBER_FLAG | — | ✅ |
| 251 | PurchasingDocumentHeaderUseShipTo | USE_SHIP_TO | — | ✅ |
| 252 | PurchasingDocumentHeaderUseShipToContract | USE_SHIP_TO | — | ✅ |
| 253 | PurchasingDocumentHeaderVendorAgreementNum | VENDOR_ORDER_NUM | — | — |
| 254 | PurchasingDocumentHeaderVendorContactId | VENDOR_CONTACT_ID | — | — |
| 255 | PurchasingDocumentHeaderVendorId | VENDOR_ID | — | ✅ |
| 256 | PurchasingDocumentHeaderVendorOrderNum | VENDOR_ORDER_NUM | — | ✅ |
| 257 | PurchasingDocumentHeaderVendorSiteId | VENDOR_SITE_ID | — | ✅ |
| 258 | PurchasingDocumentHeaderXmlChangeSendDate | XML_CHANGE_SEND_DATE | — | — |
| 259 | PurchasingDocumentHeaderXmlFlag | XML_FLAG | — | — |
| 260 | PurchasingDocumentHeaderXmlSendDate | XML_SEND_DATE | — | — |

### [[po_system_parameters_all|PO_SYSTEM_PARAMETERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | POSystemParametersAllowItemDescUpdateFlag | ALLOW_ITEM_DESC_UPDATE_FLAG | — | — |
| 2 | POSystemParametersAllowRetroPricing | ALLOW_RETRO_PRICING | — | — |
| 3 | POSystemParametersBestPriceVisibleBlind | BEST_PRICE_VISIBLE_BLIND | — | — |
| 4 | POSystemParametersCarrierId | CARRIER_ID | — | — |
| 5 | POSystemParametersCatAdminAuthoringAcceptance | CAT_ADMIN_AUTHORING_ACCEPTANCE | — | — |
| 6 | POSystemParametersCollabSecurityProfileId | COLLAB_SECURITY_PROFILE_ID | — | — |
| 7 | POSystemParametersCreateDebitMemoFlag | CREATE_DEBIT_MEMO_FLAG | — | — |
| 8 | POSystemParametersCreatedBy | CREATED_BY | — | — |
| 9 | POSystemParametersCreationDate | CREATION_DATE | — | — |
| 10 | POSystemParametersCurrencyCode | CURRENCY_CODE | — | — |
| 11 | POSystemParametersDefaultPromiseDate | DEFAULT_PROMISE_DATE | — | — |
| 12 | POSystemParametersDefaultRateType | DEFAULT_RATE_TYPE | — | — |
| 13 | POSystemParametersDoctypeId | DOCTYPE_ID | — | — |
| 14 | POSystemParametersEmailAttachmentFilename | EMAIL_ATTACHMENT_FILENAME | — | — |
| 15 | POSystemParametersEnforceBuyerAuthorityFlag | ENFORCE_BUYER_AUTHORITY_FLAG | — | — |
| 16 | POSystemParametersEnforceMinBidPrice | ENFORCE_MIN_BID_PRICE | — | — |
| 17 | POSystemParametersEnforceVendorHoldFlag | ENFORCE_VENDOR_HOLD_FLAG | — | — |
| 18 | POSystemParametersFobLookupCode | FOB_LOOKUP_CODE | — | — |
| 19 | POSystemParametersFreightTermsLookupCode | FREIGHT_TERMS_LOOKUP_CODE | — | — |
| 20 | POSystemParametersGroupRequisitionLines | GROUP_REQUISITION_LINES | — | — |
| 21 | POSystemParametersGroupRequisitions | GROUP_REQUISITIONS | — | — |
| 22 | POSystemParametersHdrAttrDefaultMaxScore | HDR_ATTR_DEFAULT_MAX_SCORE | — | — |
| 23 | POSystemParametersHdrAttrDispScoreCriteria | HDR_ATTR_DISP_SCORE_CRITERIA | — | — |
| 24 | POSystemParametersHdrAttrEnableWeights | HDR_ATTR_ENABLE_WEIGHTS | — | — |
| 25 | POSystemParametersInspectionRequiredFlag | INSPECTION_REQUIRED_FLAG | — | — |
| 26 | POSystemParametersInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | — |
| 27 | POSystemParametersInvoiceCloseCode | INVOICE_CLOSE_CODE | — | — |
| 28 | POSystemParametersInvoiceCloseTolerance | INVOICE_CLOSE_TOLERANCE | — | — |
| 29 | POSystemParametersLanguageCode | LANGUAGE_CODE | — | — |
| 30 | POSystemParametersLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 31 | POSystemParametersLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 32 | POSystemParametersLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 33 | POSystemParametersLineTypeId | LINE_TYPE_ID | — | — |
| 34 | POSystemParametersManualReceiptNumType | MANUAL_RECEIPT_NUM_TYPE | — | — |
| 35 | POSystemParametersManualReqNumType | MANUAL_REQ_NUM_TYPE | — | — |
| 36 | POSystemParametersMatchOption | MATCH_OPTION | — | — |
| 37 | POSystemParametersMaxAttachmentSize | MAX_ATTACHMENT_SIZE | — | — |
| 38 | POSystemParametersMinReleaseAmount | MIN_RELEASE_AMOUNT | — | — |
| 39 | POSystemParametersModeOfTransport | MODE_OF_TRANSPORT | — | — |
| 40 | POSystemParametersNextApproverLookupCode | NEXT_APPROVER_LOOKUP_CODE | — | — |
| 41 | POSystemParametersNextNegotiationNumber | NEXT_NEGOTIATION_NUMBER | — | — |
| 42 | POSystemParametersObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 43 | POSystemParametersPrcBuId | PRC_BU_ID | — | — |
| 44 | POSystemParametersPriceBreakLookupCode | PRICE_BREAK_LOOKUP_CODE | — | — |
| 45 | POSystemParametersPriceChangeAmount | PRICE_CHANGE_AMOUNT | — | — |
| 46 | POSystemParametersRankIndicator | RANK_INDICATOR | — | — |
| 47 | POSystemParametersRankVisibleBlind | RANK_VISIBLE_BLIND | — | — |
| 48 | POSystemParametersReceiveCloseCode | RECEIVE_CLOSE_CODE | — | — |
| 49 | POSystemParametersReceiveCloseTolerance | RECEIVE_CLOSE_TOLERANCE | — | — |
| 50 | POSystemParametersReceivingFlag | RECEIVING_FLAG | — | — |
| 51 | POSystemParametersRfqOnlySiteFlag | RFQ_ONLY_SITE_FLAG | — | — |
| 52 | POSystemParametersServiceLevel | SERVICE_LEVEL | — | — |
| 53 | POSystemParametersStyleId | STYLE_ID | — | — |
| 54 | POSystemParametersSupplierAuthoringAcceptance | SUPPLIER_AUTHORING_ACCEPTANCE | — | — |
| 55 | POSystemParametersSupplierHistoryDuration | SUPPLIER_HISTORY_DURATION | — | — |
| 56 | POSystemParametersTaxFromItemFlag | TAX_FROM_ITEM_FLAG | — | — |
| 57 | POSystemParametersTaxFromShipToLocFlag | TAX_FROM_SHIP_TO_LOC_FLAG | — | — |
| 58 | POSystemParametersTaxFromSystemFlag | TAX_FROM_SYSTEM_FLAG | — | — |
| 59 | POSystemParametersTaxFromVendorFlag | TAX_FROM_VENDOR_FLAG | — | — |
| 60 | POSystemParametersTaxFromVendorSiteFlag | TAX_FROM_VENDOR_SITE_FLAG | — | — |
| 61 | POSystemParametersTaxHierItem | TAX_HIER_ITEM | — | — |
| 62 | POSystemParametersTaxHierShipToLoc | TAX_HIER_SHIP_TO_LOC | — | — |
| 63 | POSystemParametersTaxHierSystem | TAX_HIER_SYSTEM | — | — |
| 64 | POSystemParametersTaxHierVendor | TAX_HIER_VENDOR | — | — |
| 65 | POSystemParametersTaxHierVendorSite | TAX_HIER_VENDOR_SITE | — | — |
| 66 | POSystemParametersTaxableFlag | TAXABLE_FLAG | — | — |
| 67 | POSystemParametersTermsId | TERMS_ID | — | — |
| 68 | POSystemParametersUseNeedByDate | USE_NEED_BY_DATE | — | — |
| 69 | POSystemParametersUseShipTo | USE_SHIP_TO | — | — |
| 70 | POSystemParametersUserDefinedReceiptNumCode | USER_DEFINED_RECEIPT_NUM_CODE | — | — |
| 71 | POSystemParametersUserDefinedReqNumCode | USER_DEFINED_REQ_NUM_CODE | — | — |

### [[po_versions_init_sequence_v|PO_VERSIONS_INIT_SEQUENCE_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PurchaseOrderVersionAcceptedDate | ACCEPTED_DATE | — | — |
| 2 | PurchaseOrderVersionApprovedDate | APPROVED_DATE | — | — |
| 3 | PurchaseOrderVersionCancelBackingReqFlag | CANCEL_BACKING_REQ_FLAG | — | — |
| 4 | PurchaseOrderVersionCancelDocFlag | CANCEL_DOC_FLAG | — | — |
| 5 | PurchaseOrderVersionChangeOrderDesc | CHANGE_ORDER_DESC | — | — |
| 6 | PurchaseOrderVersionChangeOrderStatus | CHANGE_ORDER_STATUS | — | — |
| 7 | PurchaseOrderVersionChangeOrderType | CHANGE_ORDER_TYPE | — | — |
| 8 | PurchaseOrderVersionCoCanceledByRole | CO_CANCELED_BY_ROLE | — | — |
| 9 | PurchaseOrderVersionCoCanceledByUserId | CO_CANCELED_BY_USER_ID | — | — |
| 10 | PurchaseOrderVersionCoCanceledFlag | CO_CANCELED_FLAG | — | — |
| 11 | PurchaseOrderVersionCoNum | CO_NUM | — | — |
| 12 | PurchaseOrderVersionCoSequence | CO_SEQUENCE | — | — |
| 13 | PurchaseOrderVersionCommunicatedDate | COMMUNICATED_DATE | — | — |
| 14 | PurchaseOrderVersionCommunicatedToSupplier | COMMUNICATED_TO_SUPPLIER | — | — |
| 15 | PurchaseOrderVersionCreatedBy | CREATED_BY | — | — |
| 16 | PurchaseOrderVersionCreatedByProgramName | CREATED_BY_PROGRAM_NAME | — | — |
| 17 | PurchaseOrderVersionCreationDate | CREATION_DATE | — | — |
| 18 | PurchaseOrderVersionDocumentDate | DOCUMENT_DATE | — | — |
| 19 | PurchaseOrderVersionExternalSystemFlag | EXTERNAL_SYSTEM_FLAG | — | — |
| 20 | PurchaseOrderVersionFundsStatus | FUNDS_STATUS | — | — |
| 21 | PurchaseOrderVersionJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 22 | PurchaseOrderVersionJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 23 | PurchaseOrderVersionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 24 | PurchaseOrderVersionLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 25 | PurchaseOrderVersionLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 26 | PurchaseOrderVersionModifiedFlag | MODIFIED_FLAG | — | — |
| 27 | PurchaseOrderVersionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 28 | PurchaseOrderVersionOnlineReportId | ONLINE_REPORT_ID | — | — |
| 29 | PurchaseOrderVersionOriginatorId | ORIGINATOR_ID | — | — |
| 30 | PurchaseOrderVersionOriginatorRole | ORIGINATOR_ROLE | — | — |
| 31 | PurchaseOrderVersionPendingResponseRole | PENDING_RESPONSE_ROLE | — | — |
| 32 | PurchaseOrderVersionPoHeaderId | PO_HEADER_ID | — | — |
| 33 | PurchaseOrderVersionProcessedDate | PROCESSED_DATE | — | — |
| 34 | PurchaseOrderVersionProgramAppName | PROGRAM_APP_NAME | — | — |
| 35 | PurchaseOrderVersionProgramName | PROGRAM_NAME | — | — |
| 36 | PurchaseOrderVersionRejectedFlag | REJECTED_FLAG | — | — |
| 37 | PurchaseOrderVersionRequestDate | REQUEST_DATE | — | — |
| 38 | PurchaseOrderVersionRequestId | REQUEST_ID | — | — |
| 39 | PurchaseOrderVersionRevisionNum | REVISION_NUM | — | — |
| 40 | PurchaseOrderVersionSubmittedDate | SUBMITTED_DATE | — | — |
| 41 | PurchaseOrderVersionVersionId | VERSION_ID | — | — |
| 42 | PurchaseOrderVersionWithdrawnFlag | WITHDRAWN_FLAG | — | — |

### [[zx_fc_document_fiscal_v|ZX_FC_DOCUMENT_FISCAL_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DocFisClassificationClassificationCode | CLASSIFICATION_CODE | — | — |
| 2 | DocFisClassificationClassificationId | CLASSIFICATION_ID | — | — |
| 3 | DocFisClassificationClassificationName | CLASSIFICATION_NAME | — | — |
| 4 | DocFisClassificationConcatClassifCode | CONCAT_CLASSIF_CODE | — | — |
| 5 | DocFisClassificationConcatClassifName | CONCAT_CLASSIF_NAME | — | — |
| 6 | DocFisClassificationCountryCode | COUNTRY_CODE | — | — |
| 7 | DocFisClassificationEffectiveFrom | EFFECTIVE_FROM | — | — |
| 8 | DocFisClassificationEffectiveTo | EFFECTIVE_TO | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
