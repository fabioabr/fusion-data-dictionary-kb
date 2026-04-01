---
id: DOC-PO-PVO-PurchasingAgreementNotificationControlPVO
doc_type: system-doc
title: "PurchasingAgreementNotificationControlPVO — PVO Purchasing"
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
  - PurchasingAgreementNotificationControlPVO
  - purchasingagreementnotificationcontrolpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PurchasingAgreementNotificationControlPVO

## 📌 Visão Geral

Disponibiliza controles de notificação de contratos para consulta operacional, permitindo verificar alertas configurados (vencimento, consumo, renovação) para cada acordo de compra.

**Caminho:** `FscmTopModelAM.PrcPoPublicViewAM.PurchasingAgreementNotificationControlPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 179 | 2 | 1 | 13 | 7% |

---

## 🔗 Tabelas Relacionadas

- [[po_headers_all|PO_HEADERS_ALL]] — 111 atributos (2 BICC)
- [[po_notification_controls|PO_NOTIFICATION_CONTROLS]] — 68 atributos (1 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[po_headers_all|PO_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PurchasingAgreementAcceptanceDueDate | ACCEPTANCE_DUE_DATE | — | — |
| 2 | PurchasingAgreementAcceptanceRequiredFlag | ACCEPTANCE_REQUIRED_FLAG | — | — |
| 3 | PurchasingAgreementAcceptanceWithinDays | ACCEPTANCE_WITHIN_DAYS | — | — |
| 4 | PurchasingAgreementAgentId | AGENT_ID | — | — |
| 5 | PurchasingAgreementAmountLimit | AMOUNT_LIMIT | — | — |
| 6 | PurchasingAgreementAmountReleased | AMOUNT_RELEASED | — | — |
| 7 | PurchasingAgreementApprovedDate | APPROVED_DATE | — | — |
| 8 | PurchasingAgreementApprovedFlag | APPROVED_FLAG | — | — |
| 9 | PurchasingAgreementAutoSourcingFlag | AUTO_SOURCING_FLAG | — | — |
| 10 | PurchasingAgreementBillToLocationId | BILL_TO_LOCATION_ID | — | — |
| 11 | PurchasingAgreementBlanketTotalAmount | BLANKET_TOTAL_AMOUNT | — | — |
| 12 | PurchasingAgreementCancelFlag | CANCEL_FLAG | — | — |
| 13 | PurchasingAgreementCarrierId | CARRIER_ID | — | — |
| 14 | PurchasingAgreementCatAdminAuthEnabledFlag | CAT_ADMIN_AUTH_ENABLED_FLAG | — | — |
| 15 | PurchasingAgreementCbcAccountingDate | CBC_ACCOUNTING_DATE | — | — |
| 16 | PurchasingAgreementChangeRequestedBy | CHANGE_REQUESTED_BY | — | — |
| 17 | PurchasingAgreementChangeSummary | CHANGE_SUMMARY | — | — |
| 18 | PurchasingAgreementClosedDate | CLOSED_DATE | — | — |
| 19 | PurchasingAgreementComments | COMMENTS | — | — |
| 20 | PurchasingAgreementConfirmingOrderFlag | CONFIRMING_ORDER_FLAG | — | — |
| 21 | PurchasingAgreementConsignedConsumptionFlag | CONSIGNED_CONSUMPTION_FLAG | — | — |
| 22 | PurchasingAgreementConsumeReqDemandFlag | CONSUME_REQ_DEMAND_FLAG | — | — |
| 23 | PurchasingAgreementContermsArticlesUpdDate | CONTERMS_ARTICLES_UPD_DATE | — | — |
| 24 | PurchasingAgreementContermsDelivUpdDate | CONTERMS_DELIV_UPD_DATE | — | — |
| 25 | PurchasingAgreementContermsExistFlag | CONTERMS_EXIST_FLAG | — | — |
| 26 | PurchasingAgreementCpaReference | CPA_REFERENCE | — | — |
| 27 | PurchasingAgreementCreatedBy | CREATED_BY | — | — |
| 28 | PurchasingAgreementCreatedLanguage | CREATED_LANGUAGE | — | — |
| 29 | PurchasingAgreementCreationDate | CREATION_DATE | — | — |
| 30 | PurchasingAgreementCurrencyCode | CURRENCY_CODE | — | — |
| 31 | PurchasingAgreementCurrentVersionId | CURRENT_VERSION_ID | — | — |
| 32 | PurchasingAgreementDefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | — |
| 33 | PurchasingAgreementDocumentCreationMethod | DOCUMENT_CREATION_METHOD | — | — |
| 34 | PurchasingAgreementDocumentStatus | DOCUMENT_STATUS | — | — |
| 35 | PurchasingAgreementEdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 36 | PurchasingAgreementEdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 37 | PurchasingAgreementEmailAddress | EMAIL_ADDRESS | — | — |
| 38 | PurchasingAgreementEnabledFlag | ENABLED_FLAG | — | — |
| 39 | PurchasingAgreementEncumbranceRequiredFlag | ENCUMBRANCE_REQUIRED_FLAG | — | — |
| 40 | PurchasingAgreementEndDate | END_DATE | — | — |
| 41 | PurchasingAgreementFax | FAX | — | — |
| 42 | PurchasingAgreementFirmDate | FIRM_DATE | — | — |
| 43 | PurchasingAgreementFirmStatusLookupCode | FIRM_STATUS_LOOKUP_CODE | — | — |
| 44 | PurchasingAgreementFobLookupCode | FOB_LOOKUP_CODE | — | — |
| 45 | PurchasingAgreementFreightTermsLookupCode | FREIGHT_TERMS_LOOKUP_CODE | — | — |
| 46 | PurchasingAgreementFromHeaderId | FROM_HEADER_ID | — | — |
| 47 | PurchasingAgreementFromTypeLookupCode | FROM_TYPE_LOOKUP_CODE | — | — |
| 48 | PurchasingAgreementFrozenFlag | FROZEN_FLAG | — | — |
| 49 | PurchasingAgreementGenerateOrdersAutomatic | GENERATE_ORDERS_AUTOMATIC | — | — |
| 50 | PurchasingAgreementGovernmentContext | GOVERNMENT_CONTEXT | — | — |
| 51 | PurchasingAgreementGroupRequisitionLines | GROUP_REQUISITION_LINES | — | — |
| 52 | PurchasingAgreementGroupRequisitions | GROUP_REQUISITIONS | — | — |
| 53 | PurchasingAgreementInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | — |
| 54 | PurchasingAgreementJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 55 | PurchasingAgreementJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 56 | PurchasingAgreementLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 57 | PurchasingAgreementLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 58 | PurchasingAgreementLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 59 | PurchasingAgreementLastUpdatedProgram | LAST_UPDATED_PROGRAM | — | — |
| 60 | PurchasingAgreementMinReleaseAmount | MIN_RELEASE_AMOUNT | — | — |
| 61 | PurchasingAgreementNoteToAuthorizer | NOTE_TO_AUTHORIZER | — | — |
| 62 | PurchasingAgreementNoteToReceiver | NOTE_TO_RECEIVER | — | — |
| 63 | PurchasingAgreementNoteToVendor | NOTE_TO_VENDOR | — | — |
| 64 | PurchasingAgreementObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 65 | PurchasingAgreementPayOnCode | PAY_ON_CODE | — | — |
| 66 | PurchasingAgreementPcardId | PCARD_ID | — | — |
| 67 | PurchasingAgreementPendingSignatureFlag | PENDING_SIGNATURE_FLAG | — | — |
| 68 | PurchasingAgreementPoHeaderId | PO_HEADER_ID | — | — |
| 69 | PurchasingAgreementPrcBuId | PRC_BU_ID | — | — |
| 70 | PurchasingAgreementPriceUpdateTolerance | PRICE_UPDATE_TOLERANCE | — | — |
| 71 | PurchasingAgreementProgramAppName | PROGRAM_APP_NAME | — | — |
| 72 | PurchasingAgreementProgramName | PROGRAM_NAME | — | — |
| 73 | PurchasingAgreementRate | RATE | — | — |
| 74 | PurchasingAgreementRateDate | RATE_DATE | — | — |
| 75 | PurchasingAgreementRateType | RATE_TYPE | — | — |
| 76 | PurchasingAgreementReferenceNum | REFERENCE_NUM | — | — |
| 77 | PurchasingAgreementReleaseMethod | RELEASE_METHOD | — | — |
| 78 | PurchasingAgreementReqBuId | REQ_BU_ID | — | — |
| 79 | PurchasingAgreementRequestId | REQUEST_ID | — | — |
| 80 | PurchasingAgreementRetroPriceApplyUpdatesFlag | RETRO_PRICE_APPLY_UPDATES_FLAG | — | — |
| 81 | PurchasingAgreementRetroPriceCommUpdatesFlag | RETRO_PRICE_COMM_UPDATES_FLAG | — | — |
| 82 | PurchasingAgreementReviewAutogeneratedReleases | REVIEW_AUTOGENERATED_RELEASES | — | — |
| 83 | PurchasingAgreementRevisedDate | REVISED_DATE | — | — |
| 84 | PurchasingAgreementRevisionNum | REVISION_NUM | — | — |
| 85 | PurchasingAgreementSegment1 | SEGMENT1 | — | — |
| 86 | PurchasingAgreementSegment2 | SEGMENT2 | — | — |
| 87 | PurchasingAgreementSegment3 | SEGMENT3 | — | — |
| 88 | PurchasingAgreementSegment4 | SEGMENT4 | — | — |
| 89 | PurchasingAgreementSegment5 | SEGMENT5 | — | — |
| 90 | PurchasingAgreementShipToLocationId | SHIP_TO_LOCATION_ID | — | — |
| 91 | PurchasingAgreementShippingControl | SHIPPING_CONTROL | — | — |
| 92 | PurchasingAgreementStartDate | START_DATE | — | — |
| 93 | PurchasingAgreementStyleId | STYLE_ID | — | — |
| 94 | PurchasingAgreementSubmitApprovalAutomatic | SUBMIT_APPROVAL_AUTOMATIC | — | — |
| 95 | PurchasingAgreementSubmitDate | SUBMIT_DATE | — | — |
| 96 | PurchasingAgreementSummaryFlag | SUMMARY_FLAG | — | — |
| 97 | PurchasingAgreementSupplierNotifMethod | SUPPLIER_NOTIF_METHOD | — | — |
| 98 | PurchasingAgreementTaxAttributeUpdateCode | TAX_ATTRIBUTE_UPDATE_CODE | — | — |
| 99 | PurchasingAgreementTaxDocumentSubtype | TAX_DOCUMENT_SUBTYPE | — | — |
| 100 | PurchasingAgreementTermsId | TERMS_ID | — | — |
| 101 | PurchasingAgreementTypeLookupCode | TYPE_LOOKUP_CODE | — | ✅ |
| 102 | PurchasingAgreementUpdateSourcingRulesFlag | UPDATE_SOURCING_RULES_FLAG | — | — |
| 103 | PurchasingAgreementUseNeedByDate | USE_NEED_BY_DATE | — | — |
| 104 | PurchasingAgreementUseShipTo | USE_SHIP_TO | — | — |
| 105 | PurchasingAgreementVendorContactId | VENDOR_CONTACT_ID | — | — |
| 106 | PurchasingAgreementVendorId | VENDOR_ID | — | — |
| 107 | PurchasingAgreementVendorOrderNum | VENDOR_ORDER_NUM | — | — |
| 108 | PurchasingAgreementVendorSiteId | VENDOR_SITE_ID | — | — |
| 109 | PurchasingAgreementXmlChangeSendDate | XML_CHANGE_SEND_DATE | — | — |
| 110 | PurchasingAgreementXmlFlag | XML_FLAG | — | — |
| 111 | PurchasingAgreementXmlSendDate | XML_SEND_DATE | — | — |

### [[po_notification_controls|PO_NOTIFICATION_CONTROLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AgreementNotificationControlAttribute1 | ATTRIBUTE1 | — | — |
| 2 | AgreementNotificationControlAttribute10 | ATTRIBUTE10 | — | — |
| 3 | AgreementNotificationControlAttribute11 | ATTRIBUTE11 | — | — |
| 4 | AgreementNotificationControlAttribute12 | ATTRIBUTE12 | — | — |
| 5 | AgreementNotificationControlAttribute13 | ATTRIBUTE13 | — | — |
| 6 | AgreementNotificationControlAttribute14 | ATTRIBUTE14 | — | — |
| 7 | AgreementNotificationControlAttribute15 | ATTRIBUTE15 | — | — |
| 8 | AgreementNotificationControlAttribute16 | ATTRIBUTE16 | — | — |
| 9 | AgreementNotificationControlAttribute17 | ATTRIBUTE17 | — | — |
| 10 | AgreementNotificationControlAttribute18 | ATTRIBUTE18 | — | — |
| 11 | AgreementNotificationControlAttribute19 | ATTRIBUTE19 | — | — |
| 12 | AgreementNotificationControlAttribute2 | ATTRIBUTE2 | — | — |
| 13 | AgreementNotificationControlAttribute20 | ATTRIBUTE20 | — | — |
| 14 | AgreementNotificationControlAttribute3 | ATTRIBUTE3 | — | — |
| 15 | AgreementNotificationControlAttribute4 | ATTRIBUTE4 | — | — |
| 16 | AgreementNotificationControlAttribute5 | ATTRIBUTE5 | — | — |
| 17 | AgreementNotificationControlAttribute6 | ATTRIBUTE6 | — | — |
| 18 | AgreementNotificationControlAttribute7 | ATTRIBUTE7 | — | — |
| 19 | AgreementNotificationControlAttribute8 | ATTRIBUTE8 | — | — |
| 20 | AgreementNotificationControlAttribute9 | ATTRIBUTE9 | — | — |
| 21 | AgreementNotificationControlAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 22 | AgreementNotificationControlAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 23 | AgreementNotificationControlAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 24 | AgreementNotificationControlAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 25 | AgreementNotificationControlAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 26 | AgreementNotificationControlAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 27 | AgreementNotificationControlAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 28 | AgreementNotificationControlAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 29 | AgreementNotificationControlAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 30 | AgreementNotificationControlAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 31 | AgreementNotificationControlAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 32 | AgreementNotificationControlAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 33 | AgreementNotificationControlAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 34 | AgreementNotificationControlAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 35 | AgreementNotificationControlAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 36 | AgreementNotificationControlAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 37 | AgreementNotificationControlAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 38 | AgreementNotificationControlAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 39 | AgreementNotificationControlAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 40 | AgreementNotificationControlAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 41 | AgreementNotificationControlAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 42 | AgreementNotificationControlAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 43 | AgreementNotificationControlAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 44 | AgreementNotificationControlAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 45 | AgreementNotificationControlAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 46 | AgreementNotificationControlAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 47 | AgreementNotificationControlAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 48 | AgreementNotificationControlAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 49 | AgreementNotificationControlAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 50 | AgreementNotificationControlAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 51 | AgreementNotificationControlAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 52 | AgreementNotificationControlCreatedBy | CREATED_BY | — | — |
| 53 | AgreementNotificationControlCreationDate | CREATION_DATE | — | — |
| 54 | AgreementNotificationControlEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 55 | AgreementNotificationControlEndDateActiveContract | END_DATE_ACTIVE | — | ✅ |
| 56 | AgreementNotificationControlLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 57 | AgreementNotificationControlLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 58 | AgreementNotificationControlLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 59 | AgreementNotificationControlNotificationAmount | NOTIFICATION_AMOUNT | — | ✅ |
| 60 | AgreementNotificationControlNotificationConditionCode | NOTIFICATION_CONDITION_CODE | — | ✅ |
| 61 | AgreementNotificationControlNotificationConditionCodeContract | NOTIFICATION_CONDITION_CODE | — | ✅ |
| 62 | AgreementNotificationControlNotificationId | NOTIFICATION_ID | 🔑 | ✅ |
| 63 | AgreementNotificationControlNotificationQtyPercentage | NOTIFICATION_QTY_PERCENTAGE | — | ✅ |
| 64 | AgreementNotificationControlNotificationQtyPercentageContract | NOTIFICATION_QTY_PERCENTAGE | — | ✅ |
| 65 | AgreementNotificationControlObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 66 | AgreementNotificationControlPoHeaderId | PO_HEADER_ID | — | — |
| 67 | AgreementNotificationControlStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 68 | AgreementNotificationControlStartDateActiveContract | START_DATE_ACTIVE | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
