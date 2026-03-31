---
id: DOC-OTHER-PVO-FDInterfaceExceptionsP1
doc_type: system-doc
title: "FDInterfaceExceptionsP1 — PVO Cross-Module"
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
  - FDInterfaceExceptionsP1
  - fdinterfaceexceptionsp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FDInterfaceExceptionsP1

## 📌 Visão Geral

View Object para extração BICC de dados de FDInterface Exceptions P1. Acessa as tabelas: CMF_FD_EXCEPTIONS_INT, CMF_FD_HEADERS_INT, CMF_FD_INV_ORG_INT_OTBI_V (+18).

**Caminho:** `FscmTopModelAM.FiscalDocumentInterfaceAM.FDInterfaceExceptionsP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 1259 | 21 | 1 | 129 | 10% |

---

## 🔗 Tabelas Relacionadas

- [[cmf_fd_exceptions_int|CMF_FD_EXCEPTIONS_INT]] — 17 atributos (1 PKs, 5 BICC)
- [[cmf_fd_headers_int|CMF_FD_HEADERS_INT]] — 100 atributos (2 BICC)
- [[cmf_fd_inv_org_int_otbi_v|CMF_FD_INV_ORG_INT_OTBI_V]] — 5 atributos
- [[cmf_fd_in_convert_cfops_v|CMF_FD_IN_CONVERT_CFOPS_V]] — 2 atributos
- [[cmf_fd_legal_procs_int|CMF_FD_LEGAL_PROCS_INT]] — 18 atributos (1 BICC)
- [[cmf_fd_lines_int|CMF_FD_LINES_INT]] — 49 atributos (2 BICC)
- [[cmf_fd_loc_info_int_otbi_v|CMF_FD_LOC_INFO_INT_OTBI_V]] — 80 atributos (12 BICC)
- [[cmf_fd_out_origin_cfops_v|CMF_FD_OUT_ORIGIN_CFOPS_V]] — 2 atributos
- [[cmf_fd_references_int|CMF_FD_REFERENCES_INT]] — 26 atributos (1 BICC)
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 21 atributos
- [[inv_units_of_measure_vl|INV_UNITS_OF_MEASURE_VL]] — 20 atributos
- [[jg_fscl_hdrs_atrb_int|JG_FSCL_HDRS_ATRB_INT]] — 69 atributos (43 BICC)
- [[jg_fscl_hdr_dtls_atrb_int|JG_FSCL_HDR_DTLS_ATRB_INT]] — 23 atributos (5 BICC)
- [[jg_fscl_lines_atrb_int|JG_FSCL_LINES_ATRB_INT]] — 48 atributos (29 BICC)
- [[jg_fscl_ln_dtls_atrb_int|JG_FSCL_LN_DTLS_ATRB_INT]] — 31 atributos (12 BICC)
- [[jg_fscl_tax_lines_int|JG_FSCL_TAX_LINES_INT]] — 40 atributos (13 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 378 atributos (4 BICC)
- [[per_users|PER_USERS]] — 308 atributos
- [[zx_fc_intended_use_v|ZX_FC_INTENDED_USE_V]] — 6 atributos
- [[zx_fc_product_categories_v|ZX_FC_PRODUCT_CATEGORIES_V]] — 8 atributos
- [[zx_fc_product_fiscal_v|ZX_FC_PRODUCT_FISCAL_V]] — 8 atributos

---

## ⚙️ Atributos

### [[cmf_fd_exceptions_int|CMF_FD_EXCEPTIONS_INT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExceptionId | EXCEPTION_ID | 🔑 | ✅ |
| 2 | FDInterfaceExceptionsPEOCreatedBy | CREATED_BY | — | — |
| 3 | FDInterfaceExceptionsPEOCreationDate | CREATION_DATE | — | — |
| 4 | FDInterfaceExceptionsPEOErrorCode | ERROR_CODE | — | ✅ |
| 5 | FDInterfaceExceptionsPEOErrorDescr | ERROR_DESCR | — | ✅ |
| 6 | FDInterfaceExceptionsPEOExceptionCode | EXCEPTION_CODE | — | ✅ |
| 7 | FDInterfaceExceptionsPEOExternalSystemRefId | EXTERNAL_SYSTEM_REF_ID | — | — |
| 8 | FDInterfaceExceptionsPEOExternalSystemReference | EXTERNAL_SYSTEM_REFERENCE | — | — |
| 9 | FDInterfaceExceptionsPEOFdHeadersIntId | FD_HEADERS_INT_ID | — | — |
| 10 | FDInterfaceExceptionsPEOInterfaceEntityId | INTERFACE_ENTITY_ID | — | — |
| 11 | FDInterfaceExceptionsPEOInterfaceEntityType | INTERFACE_ENTITY_TYPE | — | ✅ |
| 12 | FDInterfaceExceptionsPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 13 | FDInterfaceExceptionsPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 14 | FDInterfaceExceptionsPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 15 | FDInterfaceExceptionsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | FDInterfaceExceptionsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 17 | FDInterfaceExceptionsPEORequestId | REQUEST_ID | — | — |

### [[cmf_fd_headers_int|CMF_FD_HEADERS_INT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FDInterfaceHeadersPEOAccessKeyNumber | ACCESS_KEY_NUMBER | — | — |
| 2 | FDInterfaceHeadersPEOAcknowledgedDate | ACKNOWLEDGED_DATE | — | — |
| 3 | FDInterfaceHeadersPEOApprovedStatus | APPROVED_STATUS | — | — |
| 4 | FDInterfaceHeadersPEOBillToBuId | BILL_TO_BU_ID | — | — |
| 5 | FDInterfaceHeadersPEOChargeAllocationStatus | CHARGE_ALLOCATION_STATUS | — | — |
| 6 | FDInterfaceHeadersPEOCountryCode | COUNTRY_CODE | — | — |
| 7 | FDInterfaceHeadersPEOCreatedBy1 | CREATED_BY | — | — |
| 8 | FDInterfaceHeadersPEOCreationDate1 | CREATION_DATE | — | — |
| 9 | FDInterfaceHeadersPEOCurrency | CURRENCY | — | — |
| 10 | FDInterfaceHeadersPEODiscountAmount | DISCOUNT_AMOUNT | — | — |
| 11 | FDInterfaceHeadersPEODocumentHeaderId1 | DOCUMENT_HEADER_ID | — | ✅ |
| 12 | FDInterfaceHeadersPEODocumentNumber1 | DOCUMENT_NUMBER | — | ✅ |
| 13 | FDInterfaceHeadersPEODocumentStatus | DOCUMENT_STATUS | — | — |
| 14 | FDInterfaceHeadersPEODocumentType | DOCUMENT_TYPE | — | — |
| 15 | FDInterfaceHeadersPEOExternalSystemRefId1 | EXTERNAL_SYSTEM_REF_ID | — | — |
| 16 | FDInterfaceHeadersPEOExternalSystemReference1 | EXTERNAL_SYSTEM_REFERENCE | — | — |
| 17 | FDInterfaceHeadersPEOFdHeadersIntId2 | FD_HEADERS_INT_ID | — | — |
| 18 | FDInterfaceHeadersPEOFiscalDocAssoctnsId | FISCAL_DOC_ASSOCTNS_ID | — | — |
| 19 | FDInterfaceHeadersPEOFiscalProcOptionsId1 | FISCAL_PROC_OPTIONS_ID | — | — |
| 20 | FDInterfaceHeadersPEOFreightAmount | FREIGHT_AMOUNT | — | — |
| 21 | FDInterfaceHeadersPEOImportingStatus | IMPORTING_STATUS | — | — |
| 22 | FDInterfaceHeadersPEOInsuranceAmount | INSURANCE_AMOUNT | — | — |
| 23 | FDInterfaceHeadersPEOIssueDate | ISSUE_DATE | — | — |
| 24 | FDInterfaceHeadersPEOIssuerAddress | ISSUER_ADDRESS | — | — |
| 25 | FDInterfaceHeadersPEOIssuerAddressCityCode | ISSUER_ADDRESS_CITY_CODE | — | — |
| 26 | FDInterfaceHeadersPEOIssuerAddressCityName | ISSUER_ADDRESS_CITY_NAME | — | — |
| 27 | FDInterfaceHeadersPEOIssuerAddressComplement | ISSUER_ADDRESS_COMPLEMENT | — | — |
| 28 | FDInterfaceHeadersPEOIssuerAddressNumber | ISSUER_ADDRESS_NUMBER | — | — |
| 29 | FDInterfaceHeadersPEOIssuerAddressState | ISSUER_ADDRESS_STATE | — | — |
| 30 | FDInterfaceHeadersPEOIssuerAddressZipCode | ISSUER_ADDRESS_ZIP_CODE | — | — |
| 31 | FDInterfaceHeadersPEOIssuerLocationId | ISSUER_LOCATION_ID | — | — |
| 32 | FDInterfaceHeadersPEOIssuerName | ISSUER_NAME | — | — |
| 33 | FDInterfaceHeadersPEOIssuerPartyId | ISSUER_PARTY_ID | — | — |
| 34 | FDInterfaceHeadersPEOIssuerPartySiteId | ISSUER_PARTY_SITE_ID | — | — |
| 35 | FDInterfaceHeadersPEOIssuerPartyType | ISSUER_PARTY_TYPE | — | — |
| 36 | FDInterfaceHeadersPEOIssuerTaxId | ISSUER_TAX_ID | — | — |
| 37 | FDInterfaceHeadersPEOIssuerTaxpayerId | ISSUER_TAXPAYER_ID | — | — |
| 38 | FDInterfaceHeadersPEOIssuingPurpose | ISSUING_PURPOSE | — | — |
| 39 | FDInterfaceHeadersPEOItemLineTotal | ITEM_LINE_TOTAL | — | — |
| 40 | FDInterfaceHeadersPEOJgStatus | JG_STATUS | — | — |
| 41 | FDInterfaceHeadersPEOJobDefinitionName1 | JOB_DEFINITION_NAME | — | — |
| 42 | FDInterfaceHeadersPEOJobDefinitionPackage1 | JOB_DEFINITION_PACKAGE | — | — |
| 43 | FDInterfaceHeadersPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | — |
| 44 | FDInterfaceHeadersPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 45 | FDInterfaceHeadersPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 46 | FDInterfaceHeadersPEOModel | MODEL | — | — |
| 47 | FDInterfaceHeadersPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 48 | FDInterfaceHeadersPEOOperationType | OPERATION_TYPE | — | — |
| 49 | FDInterfaceHeadersPEOOtherExpensesAmount | OTHER_EXPENSES_AMOUNT | — | — |
| 50 | FDInterfaceHeadersPEOReceiverAddress | RECEIVER_ADDRESS | — | — |
| 51 | FDInterfaceHeadersPEOReceiverAddressCityCode | RECEIVER_ADDRESS_CITY_CODE | — | — |
| 52 | FDInterfaceHeadersPEOReceiverAddressCityName | RECEIVER_ADDRESS_CITY_NAME | — | — |
| 53 | FDInterfaceHeadersPEOReceiverAddressComplement | RECEIVER_ADDRESS_COMPLEMENT | — | — |
| 54 | FDInterfaceHeadersPEOReceiverAddressNumber | RECEIVER_ADDRESS_NUMBER | — | — |
| 55 | FDInterfaceHeadersPEOReceiverAddressState | RECEIVER_ADDRESS_STATE | — | — |
| 56 | FDInterfaceHeadersPEOReceiverAddressZipCode | RECEIVER_ADDRESS_ZIP_CODE | — | — |
| 57 | FDInterfaceHeadersPEOReceiverLocationId | RECEIVER_LOCATION_ID | — | — |
| 58 | FDInterfaceHeadersPEOReceiverName | RECEIVER_NAME | — | — |
| 59 | FDInterfaceHeadersPEOReceiverPartyId | RECEIVER_PARTY_ID | — | — |
| 60 | FDInterfaceHeadersPEOReceiverPartySiteId | RECEIVER_PARTY_SITE_ID | — | — |
| 61 | FDInterfaceHeadersPEOReceiverPartyType | RECEIVER_PARTY_TYPE | — | — |
| 62 | FDInterfaceHeadersPEOReceiverTaxId | RECEIVER_TAX_ID | — | — |
| 63 | FDInterfaceHeadersPEOReceiverTaxpayerId | RECEIVER_TAXPAYER_ID | — | — |
| 64 | FDInterfaceHeadersPEOReferencedStatus | REFERENCED_STATUS | — | — |
| 65 | FDInterfaceHeadersPEORequestId1 | REQUEST_ID | — | — |
| 66 | FDInterfaceHeadersPEOSeries | SERIES | — | — |
| 67 | FDInterfaceHeadersPEOShipFromAddrComplement | SHIP_FROM_ADDR_COMPLEMENT | — | — |
| 68 | FDInterfaceHeadersPEOShipFromAddress | SHIP_FROM_ADDRESS | — | — |
| 69 | FDInterfaceHeadersPEOShipFromAddressCityCode | SHIP_FROM_ADDRESS_CITY_CODE | — | — |
| 70 | FDInterfaceHeadersPEOShipFromAddressCityName | SHIP_FROM_ADDRESS_CITY_NAME | — | — |
| 71 | FDInterfaceHeadersPEOShipFromAddressNumber | SHIP_FROM_ADDRESS_NUMBER | — | — |
| 72 | FDInterfaceHeadersPEOShipFromAddressState | SHIP_FROM_ADDRESS_STATE | — | — |
| 73 | FDInterfaceHeadersPEOShipFromAddressZipCode | SHIP_FROM_ADDRESS_ZIP_CODE | — | — |
| 74 | FDInterfaceHeadersPEOShipFromPartyType | SHIP_FROM_PARTY_TYPE | — | — |
| 75 | FDInterfaceHeadersPEOShipToAddress | SHIP_TO_ADDRESS | — | — |
| 76 | FDInterfaceHeadersPEOShipToAddressCityCode | SHIP_TO_ADDRESS_CITY_CODE | — | — |
| 77 | FDInterfaceHeadersPEOShipToAddressCityName | SHIP_TO_ADDRESS_CITY_NAME | — | — |
| 78 | FDInterfaceHeadersPEOShipToAddressComplement | SHIP_TO_ADDRESS_COMPLEMENT | — | — |
| 79 | FDInterfaceHeadersPEOShipToAddressNumber | SHIP_TO_ADDRESS_NUMBER | — | — |
| 80 | FDInterfaceHeadersPEOShipToAddressState | SHIP_TO_ADDRESS_STATE | — | — |
| 81 | FDInterfaceHeadersPEOShipToAddressZipCode | SHIP_TO_ADDRESS_ZIP_CODE | — | — |
| 82 | FDInterfaceHeadersPEOShipfromLocationId | SHIPFROM_LOCATION_ID | — | — |
| 83 | FDInterfaceHeadersPEOShipfromPartyId | SHIPFROM_PARTY_ID | — | — |
| 84 | FDInterfaceHeadersPEOShipfromPartySiteId | SHIPFROM_PARTY_SITE_ID | — | — |
| 85 | FDInterfaceHeadersPEOShipfromTaxId | SHIPFROM_TAX_ID | — | — |
| 86 | FDInterfaceHeadersPEOShipfromTaxpayerId | SHIPFROM_TAXPAYER_ID | — | — |
| 87 | FDInterfaceHeadersPEOShiptoLocationId | SHIPTO_LOCATION_ID | — | — |
| 88 | FDInterfaceHeadersPEOShiptoPartyId | SHIPTO_PARTY_ID | — | — |
| 89 | FDInterfaceHeadersPEOShiptoPartySiteId | SHIPTO_PARTY_SITE_ID | — | — |
| 90 | FDInterfaceHeadersPEOShiptoTaxId | SHIPTO_TAX_ID | — | — |
| 91 | FDInterfaceHeadersPEOShiptoTaxpayerId | SHIPTO_TAXPAYER_ID | — | — |
| 92 | FDInterfaceHeadersPEOSoldToLeId | SOLD_TO_LE_ID | — | — |
| 93 | FDInterfaceHeadersPEOSourceDocCurrencyCode | SOURCE_DOC_CURRENCY_CODE | — | — |
| 94 | FDInterfaceHeadersPEOSourceDocumentType | SOURCE_DOCUMENT_TYPE | — | — |
| 95 | FDInterfaceHeadersPEOSubseries | SUBSERIES | — | — |
| 96 | FDInterfaceHeadersPEOTaxCalculationStatus | TAX_CALCULATION_STATUS | — | — |
| 97 | FDInterfaceHeadersPEOTotalAmount | TOTAL_AMOUNT | — | — |
| 98 | FDInterfaceHeadersPEOUsageAuthorization | USAGE_AUTHORIZATION | — | — |
| 99 | FDInterfaceHeadersPEOValidationStatus | VALIDATION_STATUS | — | — |
| 100 | FDInterfaceHeadersPEOZxStatus | ZX_STATUS | — | — |

### [[cmf_fd_inv_org_int_otbi_v|CMF_FD_INV_ORG_INT_OTBI_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FDInterfaceInvOrgPEODestInventoryOrgId | DEST_INVENTORY_ORG_ID | — | — |
| 2 | FDInterfaceInvOrgPEOFdHeadersIntId6 | FD_HEADERS_INT_ID | — | — |
| 3 | FDInterfaceInvOrgPEOFdLinesIntId1 | FD_LINES_INT_ID | — | — |
| 4 | FDInterfaceInvOrgPEOSourceDocumentType2 | SOURCE_DOCUMENT_TYPE | — | — |
| 5 | FDInterfaceInvOrgPEOSrcInventoryOrgId | SRC_INVENTORY_ORG_ID | — | — |

### [[cmf_fd_in_convert_cfops_v|CMF_FD_IN_CONVERT_CFOPS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocInBoundCFOPPEOClassificationCode2 | CLASSIFICATION_CODE | — | — |
| 2 | FiscalDocInBoundCFOPPEOClassificationName2 | CLASSIFICATION_NAME | — | — |

### [[cmf_fd_legal_procs_int|CMF_FD_LEGAL_PROCS_INT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FDInterfaceLegalprocessPEOCreatedBy3 | CREATED_BY | — | — |
| 2 | FDInterfaceLegalprocessPEOCreationDate3 | CREATION_DATE | — | — |
| 3 | FDInterfaceLegalprocessPEODocumentHeaderId3 | DOCUMENT_HEADER_ID | — | ✅ |
| 4 | FDInterfaceLegalprocessPEODocumentLegalDocAssocId | DOCUMENT_LEGAL_DOC_ASSOC_ID | — | — |
| 5 | FDInterfaceLegalprocessPEOExternalSystemRefId3 | EXTERNAL_SYSTEM_REF_ID | — | — |
| 6 | FDInterfaceLegalprocessPEOExternalSystemReference3 | EXTERNAL_SYSTEM_REFERENCE | — | — |
| 7 | FDInterfaceLegalprocessPEOFdHeadersIntId4 | FD_HEADERS_INT_ID | — | — |
| 8 | FDInterfaceLegalprocessPEOFdLegalProcsIntId | FD_LEGAL_PROCS_INT_ID | — | — |
| 9 | FDInterfaceLegalprocessPEOJobDefinitionName3 | JOB_DEFINITION_NAME | — | — |
| 10 | FDInterfaceLegalprocessPEOJobDefinitionPackage3 | JOB_DEFINITION_PACKAGE | — | — |
| 11 | FDInterfaceLegalprocessPEOLastUpdateDate3 | LAST_UPDATE_DATE | — | — |
| 12 | FDInterfaceLegalprocessPEOLastUpdateLogin3 | LAST_UPDATE_LOGIN | — | — |
| 13 | FDInterfaceLegalprocessPEOLastUpdatedBy3 | LAST_UPDATED_BY | — | — |
| 14 | FDInterfaceLegalprocessPEOLegalProcActIdentifier | LEGAL_PROC_ACT_IDENTIFIER | — | — |
| 15 | FDInterfaceLegalprocessPEOLegalProcProceedingOrig | LEGAL_PROC_PROCEEDING_ORIG | — | — |
| 16 | FDInterfaceLegalprocessPEOObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 17 | FDInterfaceLegalprocessPEORequestId3 | REQUEST_ID | — | — |
| 18 | FDInterfaceLegalprocessPEOValidationStatus2 | VALIDATION_STATUS | — | — |

### [[cmf_fd_lines_int|CMF_FD_LINES_INT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FDInterfaceLinesPEOCfop | CFOP | — | — |
| 2 | FDInterfaceLinesPEOChargesAmount | CHARGES_AMOUNT | — | — |
| 3 | FDInterfaceLinesPEOCreatedBy2 | CREATED_BY | — | — |
| 4 | FDInterfaceLinesPEOCreationDate2 | CREATION_DATE | — | — |
| 5 | FDInterfaceLinesPEODiscountLineAmount | DISCOUNT_LINE_AMOUNT | — | — |
| 6 | FDInterfaceLinesPEODocumentHeaderId2 | DOCUMENT_HEADER_ID | — | — |
| 7 | FDInterfaceLinesPEODocumentLineId | DOCUMENT_LINE_ID | — | — |
| 8 | FDInterfaceLinesPEOExternalSystemRefId2 | EXTERNAL_SYSTEM_REF_ID | — | — |
| 9 | FDInterfaceLinesPEOExternalSystemReference2 | EXTERNAL_SYSTEM_REFERENCE | — | — |
| 10 | FDInterfaceLinesPEOFdConvertedCfop | FD_CONVERTED_CFOP | — | — |
| 11 | FDInterfaceLinesPEOFdHeadersIntId3 | FD_HEADERS_INT_ID | — | — |
| 12 | FDInterfaceLinesPEOFdLinesIntId | FD_LINES_INT_ID | — | ✅ |
| 13 | FDInterfaceLinesPEOFiscalClassification | FISCAL_CLASSIFICATION | — | — |
| 14 | FDInterfaceLinesPEOFreightLineAmount | FREIGHT_LINE_AMOUNT | — | — |
| 15 | FDInterfaceLinesPEOFreightModal | FREIGHT_MODAL | — | — |
| 16 | FDInterfaceLinesPEOInsuranceLineAmount | INSURANCE_LINE_AMOUNT | — | — |
| 17 | FDInterfaceLinesPEOIntendedUse | INTENDED_USE | — | — |
| 18 | FDInterfaceLinesPEOItemCode | ITEM_CODE | — | — |
| 19 | FDInterfaceLinesPEOItemDescription | ITEM_DESCRIPTION | — | — |
| 20 | FDInterfaceLinesPEOItemId | ITEM_ID | — | — |
| 21 | FDInterfaceLinesPEOJobDefinitionName2 | JOB_DEFINITION_NAME | — | — |
| 22 | FDInterfaceLinesPEOJobDefinitionPackage2 | JOB_DEFINITION_PACKAGE | — | — |
| 23 | FDInterfaceLinesPEOLastUpdateDate2 | LAST_UPDATE_DATE | — | — |
| 24 | FDInterfaceLinesPEOLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 25 | FDInterfaceLinesPEOLastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 26 | FDInterfaceLinesPEOLineAmount | LINE_AMOUNT | — | — |
| 27 | FDInterfaceLinesPEOLineNumber | LINE_NUMBER | — | ✅ |
| 28 | FDInterfaceLinesPEOLineType | LINE_TYPE | — | — |
| 29 | FDInterfaceLinesPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 30 | FDInterfaceLinesPEOOtherExpensesLineAmount | OTHER_EXPENSES_LINE_AMOUNT | — | — |
| 31 | FDInterfaceLinesPEOProductCategory | PRODUCT_CATEGORY | — | — |
| 32 | FDInterfaceLinesPEOProductFiscalClassifId | PRODUCT_FISCAL_CLASSIF_ID | — | — |
| 33 | FDInterfaceLinesPEOQuantity | QUANTITY | — | — |
| 34 | FDInterfaceLinesPEORefDocumentHeaderId | REF_DOCUMENT_HEADER_ID | — | — |
| 35 | FDInterfaceLinesPEORefDocumentLineId | REF_DOCUMENT_LINE_ID | — | — |
| 36 | FDInterfaceLinesPEORefFdDocumentType | REF_FD_DOCUMENT_TYPE | — | — |
| 37 | FDInterfaceLinesPEOReqBuId | REQ_BU_ID | — | — |
| 38 | FDInterfaceLinesPEORequestId2 | REQUEST_ID | — | — |
| 39 | FDInterfaceLinesPEOSourceCurrencyCode | SOURCE_CURRENCY_CODE | — | — |
| 40 | FDInterfaceLinesPEOSourceDocBuId | SOURCE_DOC_BU_ID | — | — |
| 41 | FDInterfaceLinesPEOSourceDocHeaderId | SOURCE_DOC_HEADER_ID | — | — |
| 42 | FDInterfaceLinesPEOSourceDocLineId | SOURCE_DOC_LINE_ID | — | — |
| 43 | FDInterfaceLinesPEOSourceDocScheduleId | SOURCE_DOC_SCHEDULE_ID | — | — |
| 44 | FDInterfaceLinesPEOSourceDocumentLine | SOURCE_DOCUMENT_LINE | — | — |
| 45 | FDInterfaceLinesPEOSourceDocumentNumber | SOURCE_DOCUMENT_NUMBER | — | — |
| 46 | FDInterfaceLinesPEOSourceDocumentType1 | SOURCE_DOCUMENT_TYPE | — | — |
| 47 | FDInterfaceLinesPEOUnitOfMeasure | UNIT_OF_MEASURE | — | — |
| 48 | FDInterfaceLinesPEOUnitPrice | UNIT_PRICE | — | — |
| 49 | FDInterfaceLinesPEOValidationStatus1 | VALIDATION_STATUS | — | — |

### [[cmf_fd_loc_info_int_otbi_v|CMF_FD_LOC_INFO_INT_OTBI_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FDInterfaceLocInfoPEODocumentHeaderId | DOCUMENT_HEADER_ID | — | — |
| 2 | FDInterfaceLocInfoPEODocumentNumber | DOCUMENT_NUMBER | — | — |
| 3 | FDInterfaceLocInfoPEOFdHeadersIntId1 | FD_HEADERS_INT_ID | — | — |
| 4 | FDInterfaceLocInfoPEOFiscalProcOptionsId | FISCAL_PROC_OPTIONS_ID | — | — |
| 5 | FDInterfaceLocInfoPEOIssuerCustomerFormTaxNum | ISSUER_CUSTOMER_FORM_TAX_NUM | — | — |
| 6 | FDInterfaceLocInfoPEOIssuerCustomerLocationId | ISSUER_CUSTOMER_LOCATION_ID | — | — |
| 7 | FDInterfaceLocInfoPEOIssuerCustomerPartyId | ISSUER_CUSTOMER_PARTY_ID | — | — |
| 8 | FDInterfaceLocInfoPEOIssuerCustomerPartySiteId | ISSUER_CUSTOMER_PARTY_SITE_ID | — | — |
| 9 | FDInterfaceLocInfoPEOIssuerCustomerTaxId | ISSUER_CUSTOMER_TAX_ID | — | — |
| 10 | FDInterfaceLocInfoPEOIssuerCustomerTaxpayerId | ISSUER_CUSTOMER_TAXPAYER_ID | — | ✅ |
| 11 | FDInterfaceLocInfoPEOIssuerLeFormTaxNumber | ISSUER_LE_FORM_TAX_NUMBER | — | — |
| 12 | FDInterfaceLocInfoPEOIssuerLeId | ISSUER_LE_ID | — | — |
| 13 | FDInterfaceLocInfoPEOIssuerLeLocationId | ISSUER_LE_LOCATION_ID | — | — |
| 14 | FDInterfaceLocInfoPEOIssuerLeSiteId | ISSUER_LE_SITE_ID | — | — |
| 15 | FDInterfaceLocInfoPEOIssuerLeTaxId | ISSUER_LE_TAX_ID | — | — |
| 16 | FDInterfaceLocInfoPEOIssuerLeTaxpayerId | ISSUER_LE_TAXPAYER_ID | — | ✅ |
| 17 | FDInterfaceLocInfoPEOIssuerSupplierFormTaxNum | ISSUER_SUPPLIER_FORM_TAX_NUM | — | — |
| 18 | FDInterfaceLocInfoPEOIssuerSupplierLocationId | ISSUER_SUPPLIER_LOCATION_ID | — | — |
| 19 | FDInterfaceLocInfoPEOIssuerSupplierPartyId | ISSUER_SUPPLIER_PARTY_ID | — | — |
| 20 | FDInterfaceLocInfoPEOIssuerSupplierPartySiteId | ISSUER_SUPPLIER_PARTY_SITE_ID | — | — |
| 21 | FDInterfaceLocInfoPEOIssuerSupplierTaxId | ISSUER_SUPPLIER_TAX_ID | — | — |
| 22 | FDInterfaceLocInfoPEOIssuerSupplierTaxpayerId | ISSUER_SUPPLIER_TAXPAYER_ID | — | ✅ |
| 23 | FDInterfaceLocInfoPEOIssuerType | ISSUER_TYPE | — | — |
| 24 | FDInterfaceLocInfoPEOReceiverCustPartySiteId | RECEIVER_CUST_PARTY_SITE_ID | — | — |
| 25 | FDInterfaceLocInfoPEOReceiverCustomerFormTaxNum | RECEIVER_CUSTOMER_FORM_TAX_NUM | — | — |
| 26 | FDInterfaceLocInfoPEOReceiverCustomerLocationId | RECEIVER_CUSTOMER_LOCATION_ID | — | — |
| 27 | FDInterfaceLocInfoPEOReceiverCustomerPartyId | RECEIVER_CUSTOMER_PARTY_ID | — | — |
| 28 | FDInterfaceLocInfoPEOReceiverCustomerTaxId | RECEIVER_CUSTOMER_TAX_ID | — | — |
| 29 | FDInterfaceLocInfoPEOReceiverCustomerTaxpayerId | RECEIVER_CUSTOMER_TAXPAYER_ID | — | ✅ |
| 30 | FDInterfaceLocInfoPEOReceiverLeFormTaxNumber | RECEIVER_LE_FORM_TAX_NUMBER | — | — |
| 31 | FDInterfaceLocInfoPEOReceiverLeLocationId | RECEIVER_LE_LOCATION_ID | — | — |
| 32 | FDInterfaceLocInfoPEOReceiverLePartyId | RECEIVER_LE_PARTY_ID | — | — |
| 33 | FDInterfaceLocInfoPEOReceiverLePartySiteId | RECEIVER_LE_PARTY_SITE_ID | — | — |
| 34 | FDInterfaceLocInfoPEOReceiverLeTaxId | RECEIVER_LE_TAX_ID | — | — |
| 35 | FDInterfaceLocInfoPEOReceiverLeTaxpayerId | RECEIVER_LE_TAXPAYER_ID | — | ✅ |
| 36 | FDInterfaceLocInfoPEOReceiverSuppPartySiteId | RECEIVER_SUPP_PARTY_SITE_ID | — | — |
| 37 | FDInterfaceLocInfoPEOReceiverSupplierFormTaxNum | RECEIVER_SUPPLIER_FORM_TAX_NUM | — | — |
| 38 | FDInterfaceLocInfoPEOReceiverSupplierLocationId | RECEIVER_SUPPLIER_LOCATION_ID | — | — |
| 39 | FDInterfaceLocInfoPEOReceiverSupplierPartyId | RECEIVER_SUPPLIER_PARTY_ID | — | — |
| 40 | FDInterfaceLocInfoPEOReceiverSupplierTaxId | RECEIVER_SUPPLIER_TAX_ID | — | — |
| 41 | FDInterfaceLocInfoPEOReceiverSupplierTaxpayerId | RECEIVER_SUPPLIER_TAXPAYER_ID | — | ✅ |
| 42 | FDInterfaceLocInfoPEOReceiverType | RECEIVER_TYPE | — | — |
| 43 | FDInterfaceLocInfoPEOShipfromCustPartySiteId | SHIPFROM_CUST_PARTY_SITE_ID | — | — |
| 44 | FDInterfaceLocInfoPEOShipfromCustomerFormTaxNum | SHIPFROM_CUSTOMER_FORM_TAX_NUM | — | — |
| 45 | FDInterfaceLocInfoPEOShipfromCustomerLocationId | SHIPFROM_CUSTOMER_LOCATION_ID | — | — |
| 46 | FDInterfaceLocInfoPEOShipfromCustomerPartyId | SHIPFROM_CUSTOMER_PARTY_ID | — | — |
| 47 | FDInterfaceLocInfoPEOShipfromCustomerTaxId | SHIPFROM_CUSTOMER_TAX_ID | — | — |
| 48 | FDInterfaceLocInfoPEOShipfromCustomerTaxpayerId | SHIPFROM_CUSTOMER_TAXPAYER_ID | — | ✅ |
| 49 | FDInterfaceLocInfoPEOShipfromLeFormTaxNumber | SHIPFROM_LE_FORM_TAX_NUMBER | — | — |
| 50 | FDInterfaceLocInfoPEOShipfromLeLocationId | SHIPFROM_LE_LOCATION_ID | — | — |
| 51 | FDInterfaceLocInfoPEOShipfromLePartyId | SHIPFROM_LE_PARTY_ID | — | — |
| 52 | FDInterfaceLocInfoPEOShipfromLePartySiteId | SHIPFROM_LE_PARTY_SITE_ID | — | — |
| 53 | FDInterfaceLocInfoPEOShipfromLeTaxId | SHIPFROM_LE_TAX_ID | — | — |
| 54 | FDInterfaceLocInfoPEOShipfromLeTaxpayerId | SHIPFROM_LE_TAXPAYER_ID | — | ✅ |
| 55 | FDInterfaceLocInfoPEOShipfromSuppPartySiteId | SHIPFROM_SUPP_PARTY_SITE_ID | — | — |
| 56 | FDInterfaceLocInfoPEOShipfromSupplierFormTaxNum | SHIPFROM_SUPPLIER_FORM_TAX_NUM | — | — |
| 57 | FDInterfaceLocInfoPEOShipfromSupplierLocationId | SHIPFROM_SUPPLIER_LOCATION_ID | — | — |
| 58 | FDInterfaceLocInfoPEOShipfromSupplierPartyId | SHIPFROM_SUPPLIER_PARTY_ID | — | — |
| 59 | FDInterfaceLocInfoPEOShipfromSupplierTaxId | SHIPFROM_SUPPLIER_TAX_ID | — | — |
| 60 | FDInterfaceLocInfoPEOShipfromSupplierTaxpayerId | SHIPFROM_SUPPLIER_TAXPAYER_ID | — | ✅ |
| 61 | FDInterfaceLocInfoPEOShipfromType | SHIPFROM_TYPE | — | — |
| 62 | FDInterfaceLocInfoPEOShiptoCustPartySiteId | SHIPTO_CUST_PARTY_SITE_ID | — | — |
| 63 | FDInterfaceLocInfoPEOShiptoCustomerFormTaxNum | SHIPTO_CUSTOMER_FORM_TAX_NUM | — | — |
| 64 | FDInterfaceLocInfoPEOShiptoCustomerLocationId | SHIPTO_CUSTOMER_LOCATION_ID | — | — |
| 65 | FDInterfaceLocInfoPEOShiptoCustomerPartyId | SHIPTO_CUSTOMER_PARTY_ID | — | — |
| 66 | FDInterfaceLocInfoPEOShiptoCustomerTaxId | SHIPTO_CUSTOMER_TAX_ID | — | — |
| 67 | FDInterfaceLocInfoPEOShiptoCustomerTaxpayerId | SHIPTO_CUSTOMER_TAXPAYER_ID | — | ✅ |
| 68 | FDInterfaceLocInfoPEOShiptoLeFormTaxNumber | SHIPTO_LE_FORM_TAX_NUMBER | — | — |
| 69 | FDInterfaceLocInfoPEOShiptoLeLocationId | SHIPTO_LE_LOCATION_ID | — | — |
| 70 | FDInterfaceLocInfoPEOShiptoLePartyId | SHIPTO_LE_PARTY_ID | — | — |
| 71 | FDInterfaceLocInfoPEOShiptoLePartySiteId | SHIPTO_LE_PARTY_SITE_ID | — | — |
| 72 | FDInterfaceLocInfoPEOShiptoLeTaxId | SHIPTO_LE_TAX_ID | — | — |
| 73 | FDInterfaceLocInfoPEOShiptoLeTaxpayerId | SHIPTO_LE_TAXPAYER_ID | — | ✅ |
| 74 | FDInterfaceLocInfoPEOShiptoSuppPartySiteId | SHIPTO_SUPP_PARTY_SITE_ID | — | — |
| 75 | FDInterfaceLocInfoPEOShiptoSupplierFormTaxNum | SHIPTO_SUPPLIER_FORM_TAX_NUM | — | — |
| 76 | FDInterfaceLocInfoPEOShiptoSupplierLocationId | SHIPTO_SUPPLIER_LOCATION_ID | — | — |
| 77 | FDInterfaceLocInfoPEOShiptoSupplierPartyId | SHIPTO_SUPPLIER_PARTY_ID | — | — |
| 78 | FDInterfaceLocInfoPEOShiptoSupplierTaxId | SHIPTO_SUPPLIER_TAX_ID | — | — |
| 79 | FDInterfaceLocInfoPEOShiptoSupplierTaxpayerId | SHIPTO_SUPPLIER_TAXPAYER_ID | — | ✅ |
| 80 | FDInterfaceLocInfoPEOShiptoType | SHIPTO_TYPE | — | — |

### [[cmf_fd_out_origin_cfops_v|CMF_FD_OUT_ORIGIN_CFOPS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocOutBoundCFOPPEOClassificationCode3 | CLASSIFICATION_CODE | — | — |
| 2 | FiscalDocOutBoundCFOPPEOClassificationName3 | CLASSIFICATION_NAME | — | — |

### [[cmf_fd_references_int|CMF_FD_REFERENCES_INT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FDInterfaceReferencesPEOCreatedBy4 | CREATED_BY | — | — |
| 2 | FDInterfaceReferencesPEOCreationDate4 | CREATION_DATE | — | — |
| 3 | FDInterfaceReferencesPEODocumentHeaderId4 | DOCUMENT_HEADER_ID | — | ✅ |
| 4 | FDInterfaceReferencesPEODocumentRefAttrId | DOCUMENT_REF_ATTR_ID | — | — |
| 5 | FDInterfaceReferencesPEOExternalSystemRefId4 | EXTERNAL_SYSTEM_REF_ID | — | — |
| 6 | FDInterfaceReferencesPEOExternalSystemReference4 | EXTERNAL_SYSTEM_REFERENCE | — | — |
| 7 | FDInterfaceReferencesPEOFdHeadersIntId5 | FD_HEADERS_INT_ID | — | — |
| 8 | FDInterfaceReferencesPEOFdReferencesIntId | FD_REFERENCES_INT_ID | — | — |
| 9 | FDInterfaceReferencesPEOJobDefinitionName4 | JOB_DEFINITION_NAME | — | — |
| 10 | FDInterfaceReferencesPEOJobDefinitionPackage4 | JOB_DEFINITION_PACKAGE | — | — |
| 11 | FDInterfaceReferencesPEOLastUpdateDate4 | LAST_UPDATE_DATE | — | — |
| 12 | FDInterfaceReferencesPEOLastUpdateLogin4 | LAST_UPDATE_LOGIN | — | — |
| 13 | FDInterfaceReferencesPEOLastUpdatedBy4 | LAST_UPDATED_BY | — | — |
| 14 | FDInterfaceReferencesPEOObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 15 | FDInterfaceReferencesPEORefAccessKeyNumber | REF_ACCESS_KEY_NUMBER | — | — |
| 16 | FDInterfaceReferencesPEORefDocumentHeaderId1 | REF_DOCUMENT_HEADER_ID | — | — |
| 17 | FDInterfaceReferencesPEORefDocumentNumber | REF_DOCUMENT_NUMBER | — | — |
| 18 | FDInterfaceReferencesPEORefFdDocumentType1 | REF_FD_DOCUMENT_TYPE | — | — |
| 19 | FDInterfaceReferencesPEORefIssueDate | REF_ISSUE_DATE | — | — |
| 20 | FDInterfaceReferencesPEORefIssuerId | REF_ISSUER_ID | — | — |
| 21 | FDInterfaceReferencesPEORefIssuerState | REF_ISSUER_STATE | — | — |
| 22 | FDInterfaceReferencesPEORefIssuerTaxpayerId | REF_ISSUER_TAXPAYER_ID | — | — |
| 23 | FDInterfaceReferencesPEORefModel | REF_MODEL | — | — |
| 24 | FDInterfaceReferencesPEORefSeries | REF_SERIES | — | — |
| 25 | FDInterfaceReferencesPEORequestId4 | REQUEST_ID | — | — |
| 26 | FDInterfaceReferencesPEOValidationStatus3 | VALIDATION_STATUS | — | — |

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitPEOBusinessUnitId | BU_ID | — | — |
| 2 | BusinessUnitPEOCreatedBy5 | CREATED_BY | — | — |
| 3 | BusinessUnitPEOCreationDate5 | CREATION_DATE | — | — |
| 4 | BusinessUnitPEODateFrom | DATE_FROM | — | — |
| 5 | BusinessUnitPEODateTo | DATE_TO | — | — |
| 6 | BusinessUnitPEODefaultCurrencyCode | DEFAULT_CURRENCY_CODE | — | — |
| 7 | BusinessUnitPEODefaultSetId | DEFAULT_SET_ID | — | — |
| 8 | BusinessUnitPEOEnabledForHrFlag | ENABLED_FOR_HR_FLAG | — | — |
| 9 | BusinessUnitPEOEnterpriseId | BUSINESS_GROUP_ID | — | — |
| 10 | BusinessUnitPEOFinancialsBusinessUnitId | FIN_BUSINESS_UNIT_ID | — | — |
| 11 | BusinessUnitPEOLastUpdateDate5 | LAST_UPDATE_DATE | — | — |
| 12 | BusinessUnitPEOLastUpdateLogin5 | LAST_UPDATE_LOGIN | — | — |
| 13 | BusinessUnitPEOLastUpdatedBy5 | LAST_UPDATED_BY | — | — |
| 14 | BusinessUnitPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 15 | BusinessUnitPEOLocationId | LOCATION_ID | — | — |
| 16 | BusinessUnitPEOManagerId | MANAGER_ID | — | — |
| 17 | BusinessUnitPEOName | BU_NAME | — | — |
| 18 | BusinessUnitPEOPrimaryLedgerId | PRIMARY_LEDGER_ID | — | — |
| 19 | BusinessUnitPEOProfitCenterFlag | PROFIT_CENTER_FLAG | — | — |
| 20 | BusinessUnitPEOShortCode | SHORT_CODE | — | — |
| 21 | BusinessUnitPEOStatus | STATUS | — | — |

### [[inv_units_of_measure_vl|INV_UNITS_OF_MEASURE_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UnitOfMeasurePEOBaseUomFlag | BASE_UOM_FLAG | — | — |
| 2 | UnitOfMeasurePEOCreatedBy5 | CREATED_BY | — | — |
| 3 | UnitOfMeasurePEOCreationDate5 | CREATION_DATE | — | — |
| 4 | UnitOfMeasurePEODescription | DESCRIPTION | — | — |
| 5 | UnitOfMeasurePEODisableDate | DISABLE_DATE | — | — |
| 6 | UnitOfMeasurePEOHasGeneratedCode | HAS_GENERATED_CODE | — | — |
| 7 | UnitOfMeasurePEOJobDefinitionName5 | JOB_DEFINITION_NAME | — | — |
| 8 | UnitOfMeasurePEOJobDefinitionPackage5 | JOB_DEFINITION_PACKAGE | — | — |
| 9 | UnitOfMeasurePEOLastUpdateDate5 | LAST_UPDATE_DATE | — | — |
| 10 | UnitOfMeasurePEOLastUpdateLogin5 | LAST_UPDATE_LOGIN | — | — |
| 11 | UnitOfMeasurePEOLastUpdatedBy5 | LAST_UPDATED_BY | — | — |
| 12 | UnitOfMeasurePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | UnitOfMeasurePEORequestId5 | REQUEST_ID | — | — |
| 14 | UnitOfMeasurePEOStandardPackFlag | STANDARD_PACK_FLAG | — | — |
| 15 | UnitOfMeasurePEOUnitOfMeasure | UNIT_OF_MEASURE | — | — |
| 16 | UnitOfMeasurePEOUnitOfMeasureId | UNIT_OF_MEASURE_ID | — | — |
| 17 | UnitOfMeasurePEOUomClass | UOM_CLASS | — | — |
| 18 | UnitOfMeasurePEOUomCode1 | UOM_CODE | — | — |
| 19 | UnitOfMeasurePEOUomPluralDesc | UOM_PLURAL_DESC | — | — |
| 20 | UnitOfMeasurePEOUomReciprocalDesc | UOM_RECIPROCAL_DESC | — | — |

### [[jg_fscl_hdrs_atrb_int|JG_FSCL_HDRS_ATRB_INT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocHeaderIntrEOAppShortName | APP_SHORT_NAME | — | — |
| 2 | FiscalDocHeaderIntrEOBatchName | BATCH_NAME | — | — |
| 3 | FiscalDocHeaderIntrEOBuName | BU_NAME | — | — |
| 4 | FiscalDocHeaderIntrEOCommitmentStatementIdent | COMMITMENT_STATEMENT_IDENT | — | — |
| 5 | FiscalDocHeaderIntrEOContainerIdentifier | CONTAINER_IDENTIFIER | — | ✅ |
| 6 | FiscalDocHeaderIntrEOContingencyType | CONTINGENCY_TYPE | — | ✅ |
| 7 | FiscalDocHeaderIntrEOCreatedBy | CREATED_BY | — | — |
| 8 | FiscalDocHeaderIntrEOCreationDate | CREATION_DATE | — | ✅ |
| 9 | FiscalDocHeaderIntrEODocNature | DOC_NATURE | — | ✅ |
| 10 | FiscalDocHeaderIntrEODocNum | DOC_NUM | — | — |
| 11 | FiscalDocHeaderIntrEOEntityCode | ENTITY_CODE | — | — |
| 12 | FiscalDocHeaderIntrEOEventClassCode | EVENT_CLASS_CODE | — | — |
| 13 | FiscalDocHeaderIntrEOFerryIdentification | FERRY_IDENTIFICATION | — | ✅ |
| 14 | FiscalDocHeaderIntrEOFiscalDocDate | FISCAL_DOC_DATE | — | ✅ |
| 15 | FiscalDocHeaderIntrEOFiscalDocKey | FISCAL_DOC_KEY | — | — |
| 16 | FiscalDocHeaderIntrEOFreightType | FREIGHT_TYPE | — | ✅ |
| 17 | FiscalDocHeaderIntrEOGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | ✅ |
| 18 | FiscalDocHeaderIntrEOGlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | ✅ |
| 19 | FiscalDocHeaderIntrEOGlobalAttributeNumber1 | GLOBAL_ATTRIBUTE_NUMBER1 | — | ✅ |
| 20 | FiscalDocHeaderIntrEOGlobalAttributeNumber2 | GLOBAL_ATTRIBUTE_NUMBER2 | — | ✅ |
| 21 | FiscalDocHeaderIntrEOGlobalAttributeNumber3 | GLOBAL_ATTRIBUTE_NUMBER3 | — | ✅ |
| 22 | FiscalDocHeaderIntrEOGlobalAttributeNumber4 | GLOBAL_ATTRIBUTE_NUMBER4 | — | ✅ |
| 23 | FiscalDocHeaderIntrEOGlobalAttributeNumber5 | GLOBAL_ATTRIBUTE_NUMBER5 | — | ✅ |
| 24 | FiscalDocHeaderIntrEOGoodsBrandCarried | GOODS_BRAND_CARRIED | — | ✅ |
| 25 | FiscalDocHeaderIntrEOGoodsTypeCarried | GOODS_TYPE_CARRIED | — | ✅ |
| 26 | FiscalDocHeaderIntrEOGrossWeight | GROSS_WEIGHT | — | ✅ |
| 27 | FiscalDocHeaderIntrEOIndustryType | INDUSTRY_TYPE | — | ✅ |
| 28 | FiscalDocHeaderIntrEOInterfaceHdrId | INTERFACE_HDR_ID | — | — |
| 29 | FiscalDocHeaderIntrEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 30 | FiscalDocHeaderIntrEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 31 | FiscalDocHeaderIntrEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 32 | FiscalDocHeaderIntrEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 33 | FiscalDocHeaderIntrEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 34 | FiscalDocHeaderIntrEOLegalEntityIdentifier | LEGAL_ENTITY_IDENTIFIER | — | — |
| 35 | FiscalDocHeaderIntrEOLegalRepUnitName | LEGAL_REP_UNIT_NAME | — | — |
| 36 | FiscalDocHeaderIntrEOLoadRequestId | LOAD_REQUEST_ID | — | — |
| 37 | FiscalDocHeaderIntrEOMatIssueRecptDate | MAT_ISSUE_RECPT_DATE | — | ✅ |
| 38 | FiscalDocHeaderIntrEOMatIssueRecptHour | MAT_ISSUE_RECPT_HOUR | — | ✅ |
| 39 | FiscalDocHeaderIntrEONetWeight | NET_WEIGHT | — | ✅ |
| 40 | FiscalDocHeaderIntrEOOrgId | ORG_ID | — | — |
| 41 | FiscalDocHeaderIntrEOPaymentOption | PAYMENT_OPTION | — | ✅ |
| 42 | FiscalDocHeaderIntrEOPurchaseContract | PURCHASE_CONTRACT | — | ✅ |
| 43 | FiscalDocHeaderIntrEOQuantityCarried | QUANTITY_CARRIED | — | ✅ |
| 44 | FiscalDocHeaderIntrEORefComplementaryFdFlag | REF_COMPLEMENTARY_FD_FLAG | — | ✅ |
| 45 | FiscalDocHeaderIntrEORefDocIssuerStateCode | REF_DOC_ISSUER_STATE_CODE | — | ✅ |
| 46 | FiscalDocHeaderIntrEORefDocNum | REF_DOC_NUM | — | ✅ |
| 47 | FiscalDocHeaderIntrEORefFiscalDocDate | REF_FISCAL_DOC_DATE | — | ✅ |
| 48 | FiscalDocHeaderIntrEORefFiscalDocKey | REF_FISCAL_DOC_KEY | — | ✅ |
| 49 | FiscalDocHeaderIntrEORefIssuerTaxpayerId | REF_ISSUER_TAXPAYER_ID | — | ✅ |
| 50 | FiscalDocHeaderIntrEORefModel | REF_MODEL | — | ✅ |
| 51 | FiscalDocHeaderIntrEORefRuralFlag | REF_RURAL_FLAG | — | ✅ |
| 52 | FiscalDocHeaderIntrEORefSeries | REF_SERIES | — | ✅ |
| 53 | FiscalDocHeaderIntrEORequestId | REQUEST_ID | — | — |
| 54 | FiscalDocHeaderIntrEOSealNumber | SEAL_NUMBER | — | ✅ |
| 55 | FiscalDocHeaderIntrEOSeries | SERIES | — | ✅ |
| 56 | FiscalDocHeaderIntrEOServiceSeries | SERVICE_SERIES | — | ✅ |
| 57 | FiscalDocHeaderIntrEOServiceSituation | SERVICE_SITUATION | — | ✅ |
| 58 | FiscalDocHeaderIntrEOServiceTaxPaidFlag | SERVICE_TAX_PAID_FLAG | — | ✅ |
| 59 | FiscalDocHeaderIntrEOTaxAuthDocNumber | TAX_AUTH_DOC_NUMBER | — | — |
| 60 | FiscalDocHeaderIntrEOTaxSettlementDate | TAX_SETTLEMENT_DATE | — | ✅ |
| 61 | FiscalDocHeaderIntrEOTempServiceType | TEMP_SERVICE_TYPE | — | — |
| 62 | FiscalDocHeaderIntrEOTrxFdTypeDeterminant | TRX_FD_TYPE_DETERMINANT | — | ✅ |
| 63 | FiscalDocHeaderIntrEOTrxNumber | TRX_NUMBER | — | ✅ |
| 64 | FiscalDocHeaderIntrEOVendorId | VENDOR_ID | — | — |
| 65 | FiscalDocHeaderIntrEOVendorName | VENDOR_NAME | — | — |
| 66 | FiscalDocHeaderIntrEOVendorNum | VENDOR_NUM | — | — |
| 67 | FiscalDocHeaderIntrEOWagonIdentification | WAGON_IDENTIFICATION | — | ✅ |
| 68 | FiscalDocHeaderIntrEOWhtSocialIntgProgAmt | WHT_SOCIAL_INTG_PROG_AMT | — | — |
| 69 | FiscalDocHeaderIntrEOWhtSsFinancingAmt | WHT_SS_FINANCING_AMT | — | — |

### [[jg_fscl_hdr_dtls_atrb_int|JG_FSCL_HDR_DTLS_ATRB_INT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocHeaderDetailIntrEOAppShortName3 | APP_SHORT_NAME | — | — |
| 2 | FiscalDocHeaderDetailIntrEOBuName2 | BU_NAME | — | — |
| 3 | FiscalDocHeaderDetailIntrEOCreatedBy3 | CREATED_BY | — | — |
| 4 | FiscalDocHeaderDetailIntrEOCreationDate3 | CREATION_DATE | — | — |
| 5 | FiscalDocHeaderDetailIntrEOEntityCode3 | ENTITY_CODE | — | — |
| 6 | FiscalDocHeaderDetailIntrEOEventClassCode3 | EVENT_CLASS_CODE | — | — |
| 7 | FiscalDocHeaderDetailIntrEOGlobalAttribute31 | GLOBAL_ATTRIBUTE3 | — | ✅ |
| 8 | FiscalDocHeaderDetailIntrEOGlobalAttribute41 | GLOBAL_ATTRIBUTE4 | — | ✅ |
| 9 | FiscalDocHeaderDetailIntrEOGlobalAttribute71 | GLOBAL_ATTRIBUTE7 | — | ✅ |
| 10 | FiscalDocHeaderDetailIntrEOGlobalAttributeNumber21 | GLOBAL_ATTRIBUTE_NUMBER2 | — | ✅ |
| 11 | FiscalDocHeaderDetailIntrEOGlobalAttributeNumber32 | GLOBAL_ATTRIBUTE_NUMBER3 | — | ✅ |
| 12 | FiscalDocHeaderDetailIntrEOHdrAtrbDtlIntId | HDR_ATRB_DTL_INT_ID | — | — |
| 13 | FiscalDocHeaderDetailIntrEOInterfaceHdrId3 | INTERFACE_HDR_ID | — | — |
| 14 | FiscalDocHeaderDetailIntrEOJobDefinitionName3 | JOB_DEFINITION_NAME | — | — |
| 15 | FiscalDocHeaderDetailIntrEOJobDefinitionPackage3 | JOB_DEFINITION_PACKAGE | — | — |
| 16 | FiscalDocHeaderDetailIntrEOLastUpdateDate3 | LAST_UPDATE_DATE | — | — |
| 17 | FiscalDocHeaderDetailIntrEOLastUpdateLogin3 | LAST_UPDATE_LOGIN | — | — |
| 18 | FiscalDocHeaderDetailIntrEOLastUpdatedBy3 | LAST_UPDATED_BY | — | — |
| 19 | FiscalDocHeaderDetailIntrEOLoadRequestId3 | LOAD_REQUEST_ID | — | — |
| 20 | FiscalDocHeaderDetailIntrEOOrgId2 | ORG_ID | — | — |
| 21 | FiscalDocHeaderDetailIntrEORecordType | RECORD_TYPE | — | — |
| 22 | FiscalDocHeaderDetailIntrEORequestId3 | REQUEST_ID | — | — |
| 23 | FiscalDocHeaderDetailIntrEOTrxNumber3 | TRX_NUMBER | — | — |

### [[jg_fscl_lines_atrb_int|JG_FSCL_LINES_ATRB_INT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocLineIntrEOAppShortName1 | APP_SHORT_NAME | — | — |
| 2 | FiscalDocLineIntrEOBuName1 | BU_NAME | — | — |
| 3 | FiscalDocLineIntrEOCreatedBy1 | CREATED_BY | — | — |
| 4 | FiscalDocLineIntrEOCreationDate1 | CREATION_DATE | — | — |
| 5 | FiscalDocLineIntrEOEntityCode1 | ENTITY_CODE | — | — |
| 6 | FiscalDocLineIntrEOEventClassCode1 | EVENT_CLASS_CODE | — | — |
| 7 | FiscalDocLineIntrEOGlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | ✅ |
| 8 | FiscalDocLineIntrEOGlobalAttribute11 | GLOBAL_ATTRIBUTE1 | — | ✅ |
| 9 | FiscalDocLineIntrEOGlobalAttribute111 | GLOBAL_ATTRIBUTE11 | — | ✅ |
| 10 | FiscalDocLineIntrEOGlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | ✅ |
| 11 | FiscalDocLineIntrEOGlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | ✅ |
| 12 | FiscalDocLineIntrEOGlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | ✅ |
| 13 | FiscalDocLineIntrEOGlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | ✅ |
| 14 | FiscalDocLineIntrEOGlobalAttribute16 | GLOBAL_ATTRIBUTE16 | — | ✅ |
| 15 | FiscalDocLineIntrEOGlobalAttribute17 | GLOBAL_ATTRIBUTE17 | — | ✅ |
| 16 | FiscalDocLineIntrEOGlobalAttribute18 | GLOBAL_ATTRIBUTE18 | — | ✅ |
| 17 | FiscalDocLineIntrEOGlobalAttribute19 | GLOBAL_ATTRIBUTE19 | — | ✅ |
| 18 | FiscalDocLineIntrEOGlobalAttribute20 | GLOBAL_ATTRIBUTE20 | — | ✅ |
| 19 | FiscalDocLineIntrEOGlobalAttribute21 | GLOBAL_ATTRIBUTE2 | — | ✅ |
| 20 | FiscalDocLineIntrEOGlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | ✅ |
| 21 | FiscalDocLineIntrEOGlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | ✅ |
| 22 | FiscalDocLineIntrEOGlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | ✅ |
| 23 | FiscalDocLineIntrEOGlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | ✅ |
| 24 | FiscalDocLineIntrEOGlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | ✅ |
| 25 | FiscalDocLineIntrEOGlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | ✅ |
| 26 | FiscalDocLineIntrEOGlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | ✅ |
| 27 | FiscalDocLineIntrEOGlobalAttributeNumber10 | GLOBAL_ATTRIBUTE_NUMBER10 | — | ✅ |
| 28 | FiscalDocLineIntrEOGlobalAttributeNumber11 | GLOBAL_ATTRIBUTE_NUMBER11 | — | ✅ |
| 29 | FiscalDocLineIntrEOGlobalAttributeNumber12 | GLOBAL_ATTRIBUTE_NUMBER12 | — | ✅ |
| 30 | FiscalDocLineIntrEOGlobalAttributeNumber31 | GLOBAL_ATTRIBUTE_NUMBER3 | — | ✅ |
| 31 | FiscalDocLineIntrEOGlobalAttributeNumber7 | GLOBAL_ATTRIBUTE_NUMBER7 | — | ✅ |
| 32 | FiscalDocLineIntrEOGlobalAttributeNumber8 | GLOBAL_ATTRIBUTE_NUMBER8 | — | ✅ |
| 33 | FiscalDocLineIntrEOGlobalAttributeNumber9 | GLOBAL_ATTRIBUTE_NUMBER9 | — | ✅ |
| 34 | FiscalDocLineIntrEOInterfaceHdrId1 | INTERFACE_HDR_ID | — | — |
| 35 | FiscalDocLineIntrEOInterfaceLineId | INTERFACE_LINE_ID | — | — |
| 36 | FiscalDocLineIntrEOItemSerialNumber | ITEM_SERIAL_NUMBER | — | — |
| 37 | FiscalDocLineIntrEOJobDefinitionName1 | JOB_DEFINITION_NAME | — | — |
| 38 | FiscalDocLineIntrEOJobDefinitionPackage1 | JOB_DEFINITION_PACKAGE | — | — |
| 39 | FiscalDocLineIntrEOLastUpdateDate1 | LAST_UPDATE_DATE | — | — |
| 40 | FiscalDocLineIntrEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 41 | FiscalDocLineIntrEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 42 | FiscalDocLineIntrEOLoadRequestId1 | LOAD_REQUEST_ID | — | — |
| 43 | FiscalDocLineIntrEOOrgId1 | ORG_ID | — | — |
| 44 | FiscalDocLineIntrEORequestId1 | REQUEST_ID | — | — |
| 45 | FiscalDocLineIntrEOServiceSituation1 | SERVICE_SITUATION | — | ✅ |
| 46 | FiscalDocLineIntrEOTrxLevelType | TRX_LEVEL_TYPE | — | ✅ |
| 47 | FiscalDocLineIntrEOTrxLineNumber | TRX_LINE_NUMBER | — | — |
| 48 | FiscalDocLineIntrEOTrxNumber1 | TRX_NUMBER | — | — |

### [[jg_fscl_ln_dtls_atrb_int|JG_FSCL_LN_DTLS_ATRB_INT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocLineDetailIntrEOAppShortName4 | APP_SHORT_NAME | — | — |
| 2 | FiscalDocLineDetailIntrEOBuName3 | BU_NAME | — | — |
| 3 | FiscalDocLineDetailIntrEOCreatedBy4 | CREATED_BY | — | — |
| 4 | FiscalDocLineDetailIntrEOCreationDate4 | CREATION_DATE | — | — |
| 5 | FiscalDocLineDetailIntrEOEntityCode4 | ENTITY_CODE | — | — |
| 6 | FiscalDocLineDetailIntrEOEventClassCode4 | EVENT_CLASS_CODE | — | — |
| 7 | FiscalDocLineDetailIntrEOGlobalAttribute110 | GLOBAL_ATTRIBUTE1 | — | ✅ |
| 8 | FiscalDocLineDetailIntrEOGlobalAttribute22 | GLOBAL_ATTRIBUTE2 | — | ✅ |
| 9 | FiscalDocLineDetailIntrEOGlobalAttribute32 | GLOBAL_ATTRIBUTE3 | — | ✅ |
| 10 | FiscalDocLineDetailIntrEOGlobalAttribute42 | GLOBAL_ATTRIBUTE4 | — | ✅ |
| 11 | FiscalDocLineDetailIntrEOGlobalAttribute51 | GLOBAL_ATTRIBUTE5 | — | ✅ |
| 12 | FiscalDocLineDetailIntrEOGlobalAttribute61 | GLOBAL_ATTRIBUTE6 | — | ✅ |
| 13 | FiscalDocLineDetailIntrEOGlobalAttributeDate1 | GLOBAL_ATTRIBUTE_DATE1 | — | ✅ |
| 14 | FiscalDocLineDetailIntrEOGlobalAttributeDate2 | GLOBAL_ATTRIBUTE_DATE2 | — | ✅ |
| 15 | FiscalDocLineDetailIntrEOGlobalAttributeDate3 | GLOBAL_ATTRIBUTE_DATE3 | — | ✅ |
| 16 | FiscalDocLineDetailIntrEOGlobalAttributeNumber13 | GLOBAL_ATTRIBUTE_NUMBER1 | — | ✅ |
| 17 | FiscalDocLineDetailIntrEOGlobalAttributeNumber22 | GLOBAL_ATTRIBUTE_NUMBER2 | — | ✅ |
| 18 | FiscalDocLineDetailIntrEOInterfaceHdrId4 | INTERFACE_HDR_ID | — | — |
| 19 | FiscalDocLineDetailIntrEOInterfaceLineDetailId | INTERFACE_LINE_DETAIL_ID | — | — |
| 20 | FiscalDocLineDetailIntrEOInterfaceLineId2 | INTERFACE_LINE_ID | — | — |
| 21 | FiscalDocLineDetailIntrEOJobDefinitionName4 | JOB_DEFINITION_NAME | — | — |
| 22 | FiscalDocLineDetailIntrEOJobDefinitionPackage4 | JOB_DEFINITION_PACKAGE | — | — |
| 23 | FiscalDocLineDetailIntrEOLastUpdateDate4 | LAST_UPDATE_DATE | — | — |
| 24 | FiscalDocLineDetailIntrEOLastUpdateLogin4 | LAST_UPDATE_LOGIN | — | — |
| 25 | FiscalDocLineDetailIntrEOLastUpdatedBy4 | LAST_UPDATED_BY | — | — |
| 26 | FiscalDocLineDetailIntrEOLoadRequestId4 | LOAD_REQUEST_ID | — | — |
| 27 | FiscalDocLineDetailIntrEOOrgId3 | ORG_ID | — | — |
| 28 | FiscalDocLineDetailIntrEORequestId4 | REQUEST_ID | — | — |
| 29 | FiscalDocLineDetailIntrEOTrxLevelType2 | TRX_LEVEL_TYPE | — | ✅ |
| 30 | FiscalDocLineDetailIntrEOTrxLineDetailNumber | TRX_LINE_DETAIL_NUMBER | — | — |
| 31 | FiscalDocLineDetailIntrEOTrxLineNumber2 | TRX_LINE_NUMBER | — | — |

### [[jg_fscl_tax_lines_int|JG_FSCL_TAX_LINES_INT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocTaxLineIntrEOAppShortName2 | APP_SHORT_NAME | — | — |
| 2 | FiscalDocTaxLineIntrEOCityCode | CITY_CODE | — | — |
| 3 | FiscalDocTaxLineIntrEOCreatedBy2 | CREATED_BY | — | — |
| 4 | FiscalDocTaxLineIntrEOCreationDate2 | CREATION_DATE | — | ✅ |
| 5 | FiscalDocTaxLineIntrEOEntityCode2 | ENTITY_CODE | — | — |
| 6 | FiscalDocTaxLineIntrEOEventClassCode2 | EVENT_CLASS_CODE | — | — |
| 7 | FiscalDocTaxLineIntrEOExemptCertificateNumber | EXEMPT_CERTIFICATE_NUMBER | — | — |
| 8 | FiscalDocTaxLineIntrEOExemptReasonCode | EXEMPT_REASON_CODE | — | — |
| 9 | FiscalDocTaxLineIntrEOInterfaceEntityCode | INTERFACE_ENTITY_CODE | — | — |
| 10 | FiscalDocTaxLineIntrEOInterfaceHdrId2 | INTERFACE_HDR_ID | — | — |
| 11 | FiscalDocTaxLineIntrEOInterfaceLineId1 | INTERFACE_LINE_ID | — | — |
| 12 | FiscalDocTaxLineIntrEOInterfaceTaxLineId | INTERFACE_TAX_LINE_ID | — | — |
| 13 | FiscalDocTaxLineIntrEOJobDefinitionName2 | JOB_DEFINITION_NAME | — | — |
| 14 | FiscalDocTaxLineIntrEOJobDefinitionPackage2 | JOB_DEFINITION_PACKAGE | — | — |
| 15 | FiscalDocTaxLineIntrEOLastUpdateDate2 | LAST_UPDATE_DATE | — | ✅ |
| 16 | FiscalDocTaxLineIntrEOLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 17 | FiscalDocTaxLineIntrEOLastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 18 | FiscalDocTaxLineIntrEOLoadRequestId2 | LOAD_REQUEST_ID | — | — |
| 19 | FiscalDocTaxLineIntrEOQuantity | QUANTITY | — | ✅ |
| 20 | FiscalDocTaxLineIntrEOReportingTypeCode | REPORTING_TYPE_CODE | — | ✅ |
| 21 | FiscalDocTaxLineIntrEORequestId2 | REQUEST_ID | — | — |
| 22 | FiscalDocTaxLineIntrEOServiceItemCode | SERVICE_ITEM_CODE | — | — |
| 23 | FiscalDocTaxLineIntrEOTax | TAX | — | ✅ |
| 24 | FiscalDocTaxLineIntrEOTaxAmt | TAX_AMT | — | — |
| 25 | FiscalDocTaxLineIntrEOTaxAmtIncludedFlag | TAX_AMT_INCLUDED_FLAG | — | ✅ |
| 26 | FiscalDocTaxLineIntrEOTaxLineNumber | TAX_LINE_NUMBER | — | ✅ |
| 27 | FiscalDocTaxLineIntrEOTaxRate | TAX_RATE | — | ✅ |
| 28 | FiscalDocTaxLineIntrEOTaxRateCode | TAX_RATE_CODE | — | ✅ |
| 29 | FiscalDocTaxLineIntrEOTaxRegimeCode | TAX_REGIME_CODE | — | ✅ |
| 30 | FiscalDocTaxLineIntrEOTaxSituationCode | TAX_SITUATION_CODE | — | — |
| 31 | FiscalDocTaxLineIntrEOTaxStatusCode | TAX_STATUS_CODE | — | ✅ |
| 32 | FiscalDocTaxLineIntrEOTaxableAmt | TAXABLE_AMT | — | ✅ |
| 33 | FiscalDocTaxLineIntrEOTaxableAmtDetermCode | TAXABLE_AMT_DETERM_CODE | — | — |
| 34 | FiscalDocTaxLineIntrEOTaxableBasisPercPayerOpr | TAXABLE_BASIS_PERC_PAYER_OPR | — | — |
| 35 | FiscalDocTaxLineIntrEOTaxableBasisReductionPerc | TAXABLE_BASIS_REDUCTION_PERC | — | — |
| 36 | FiscalDocTaxLineIntrEOTrxLevelType1 | TRX_LEVEL_TYPE | — | — |
| 37 | FiscalDocTaxLineIntrEOTrxLineNumber1 | TRX_LINE_NUMBER | — | — |
| 38 | FiscalDocTaxLineIntrEOTrxNumber2 | TRX_NUMBER | — | — |
| 39 | FiscalDocTaxLineIntrEOUomCode | UOM_CODE | — | ✅ |
| 40 | FiscalDocTaxLineIntrEOValueAddedMarginPerc | VALUE_ADDED_MARGIN_PERC | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FDHdrsIntCreatedByPersonNameBusinessGroupId4 | BUSINESS_GROUP_ID | — | — |
| 2 | FDHdrsIntCreatedByPersonNameCreatedBy4 | CREATED_BY | — | — |
| 3 | FDHdrsIntCreatedByPersonNameCreationDate4 | CREATION_DATE | — | — |
| 4 | FDHdrsIntCreatedByPersonNameDisplayName | DISPLAY_NAME | — | — |
| 5 | FDHdrsIntCreatedByPersonNameEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 6 | FDHdrsIntCreatedByPersonNameEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 7 | FDHdrsIntCreatedByPersonNameFirstName | FIRST_NAME | — | — |
| 8 | FDHdrsIntCreatedByPersonNameFullName | FULL_NAME | — | ✅ |
| 9 | FDHdrsIntCreatedByPersonNameHonors | HONORS | — | — |
| 10 | FDHdrsIntCreatedByPersonNameKnownAs | KNOWN_AS | — | — |
| 11 | FDHdrsIntCreatedByPersonNameLastName | LAST_NAME | — | — |
| 12 | FDHdrsIntCreatedByPersonNameLastUpdateDate4 | LAST_UPDATE_DATE | — | — |
| 13 | FDHdrsIntCreatedByPersonNameLastUpdateLogin4 | LAST_UPDATE_LOGIN | — | — |
| 14 | FDHdrsIntCreatedByPersonNameLastUpdatedBy4 | LAST_UPDATED_BY | — | — |
| 15 | FDHdrsIntCreatedByPersonNameLegislationCode | LEGISLATION_CODE | — | — |
| 16 | FDHdrsIntCreatedByPersonNameListName | LIST_NAME | — | — |
| 17 | FDHdrsIntCreatedByPersonNameMiddleNames | MIDDLE_NAMES | — | — |
| 18 | FDHdrsIntCreatedByPersonNameMilitaryRank | MILITARY_RANK | — | — |
| 19 | FDHdrsIntCreatedByPersonNameNameType | NAME_TYPE | — | — |
| 20 | FDHdrsIntCreatedByPersonNameObjectVersionNumber4 | OBJECT_VERSION_NUMBER | — | — |
| 21 | FDHdrsIntCreatedByPersonNameOrderName | ORDER_NAME | — | — |
| 22 | FDHdrsIntCreatedByPersonNamePersonId4 | PERSON_ID | — | — |
| 23 | FDHdrsIntCreatedByPersonNamePersonNameId | PERSON_NAME_ID | — | — |
| 24 | FDHdrsIntCreatedByPersonNamePreNameAdjunct | PRE_NAME_ADJUNCT | — | — |
| 25 | FDHdrsIntCreatedByPersonNamePreviousLastName | PREVIOUS_LAST_NAME | — | — |
| 26 | FDHdrsIntCreatedByPersonNameSuffix | SUFFIX | — | — |
| 27 | FDHdrsIntCreatedByPersonNameTitle | TITLE | — | — |
| 28 | FDHdrsIntLastUpdtdByPersonNaBusinessGroupId5 | BUSINESS_GROUP_ID | — | — |
| 29 | FDHdrsIntLastUpdtdByPersonNaCreatedBy5 | CREATED_BY | — | — |
| 30 | FDHdrsIntLastUpdtdByPersonNaCreationDate5 | CREATION_DATE | — | — |
| 31 | FDHdrsIntLastUpdtdByPersonNaDisplayName1 | DISPLAY_NAME | — | — |
| 32 | FDHdrsIntLastUpdtdByPersonNaEffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 33 | FDHdrsIntLastUpdtdByPersonNaEffectiveStartDate1 | EFFECTIVE_START_DATE | — | — |
| 34 | FDHdrsIntLastUpdtdByPersonNaFirstName1 | FIRST_NAME | — | — |
| 35 | FDHdrsIntLastUpdtdByPersonNaFullName1 | FULL_NAME | — | ✅ |
| 36 | FDHdrsIntLastUpdtdByPersonNaHonors1 | HONORS | — | — |
| 37 | FDHdrsIntLastUpdtdByPersonNaKnownAs1 | KNOWN_AS | — | — |
| 38 | FDHdrsIntLastUpdtdByPersonNaLastName1 | LAST_NAME | — | — |
| 39 | FDHdrsIntLastUpdtdByPersonNaLastUpdateDate5 | LAST_UPDATE_DATE | — | — |
| 40 | FDHdrsIntLastUpdtdByPersonNaLastUpdateLogin5 | LAST_UPDATE_LOGIN | — | — |
| 41 | FDHdrsIntLastUpdtdByPersonNaLastUpdatedBy5 | LAST_UPDATED_BY | — | — |
| 42 | FDHdrsIntLastUpdtdByPersonNaLegislationCode1 | LEGISLATION_CODE | — | — |
| 43 | FDHdrsIntLastUpdtdByPersonNaListName1 | LIST_NAME | — | — |
| 44 | FDHdrsIntLastUpdtdByPersonNaMiddleNames1 | MIDDLE_NAMES | — | — |
| 45 | FDHdrsIntLastUpdtdByPersonNaMilitaryRank1 | MILITARY_RANK | — | — |
| 46 | FDHdrsIntLastUpdtdByPersonNaNameType1 | NAME_TYPE | — | — |
| 47 | FDHdrsIntLastUpdtdByPersonNaObjectVersionNumber5 | OBJECT_VERSION_NUMBER | — | — |
| 48 | FDHdrsIntLastUpdtdByPersonNaOrderName1 | ORDER_NAME | — | — |
| 49 | FDHdrsIntLastUpdtdByPersonNaPersonId5 | PERSON_ID | — | — |
| 50 | FDHdrsIntLastUpdtdByPersonNaPersonNameId1 | PERSON_NAME_ID | — | — |
| 51 | FDHdrsIntLastUpdtdByPersonNaPreNameAdjunct1 | PRE_NAME_ADJUNCT | — | — |
| 52 | FDHdrsIntLastUpdtdByPersonNaPreviousLastName1 | PREVIOUS_LAST_NAME | — | — |
| 53 | FDHdrsIntLastUpdtdByPersonNaSuffix1 | SUFFIX | — | — |
| 54 | FDHdrsIntLastUpdtdByPersonNaTitle1 | TITLE | — | — |
| 55 | FDIntHdrsCreatedByPersonNameBusinessGroupId8 | BUSINESS_GROUP_ID | — | — |
| 56 | FDIntHdrsCreatedByPersonNameCreatedBy8 | CREATED_BY | — | — |
| 57 | FDIntHdrsCreatedByPersonNameCreationDate8 | CREATION_DATE | — | — |
| 58 | FDIntHdrsCreatedByPersonNameDisplayName | DISPLAY_NAME | — | — |
| 59 | FDIntHdrsCreatedByPersonNameEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 60 | FDIntHdrsCreatedByPersonNameEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 61 | FDIntHdrsCreatedByPersonNameFirstName | FIRST_NAME | — | — |
| 62 | FDIntHdrsCreatedByPersonNameFullName | FULL_NAME | — | — |
| 63 | FDIntHdrsCreatedByPersonNameHonors | HONORS | — | — |
| 64 | FDIntHdrsCreatedByPersonNameKnownAs | KNOWN_AS | — | — |
| 65 | FDIntHdrsCreatedByPersonNameLastName | LAST_NAME | — | — |
| 66 | FDIntHdrsCreatedByPersonNameLastUpdateDate8 | LAST_UPDATE_DATE | — | — |
| 67 | FDIntHdrsCreatedByPersonNameLastUpdateLogin8 | LAST_UPDATE_LOGIN | — | — |
| 68 | FDIntHdrsCreatedByPersonNameLastUpdatedBy8 | LAST_UPDATED_BY | — | — |
| 69 | FDIntHdrsCreatedByPersonNameLegislationCode | LEGISLATION_CODE | — | — |
| 70 | FDIntHdrsCreatedByPersonNameListName | LIST_NAME | — | — |
| 71 | FDIntHdrsCreatedByPersonNameMiddleNames | MIDDLE_NAMES | — | — |
| 72 | FDIntHdrsCreatedByPersonNameMilitaryRank | MILITARY_RANK | — | — |
| 73 | FDIntHdrsCreatedByPersonNameNameType | NAME_TYPE | — | — |
| 74 | FDIntHdrsCreatedByPersonNameObjectVersionNumber8 | OBJECT_VERSION_NUMBER | — | — |
| 75 | FDIntHdrsCreatedByPersonNameOrderName | ORDER_NAME | — | — |
| 76 | FDIntHdrsCreatedByPersonNamePersonId8 | PERSON_ID | — | — |
| 77 | FDIntHdrsCreatedByPersonNamePersonNameId | PERSON_NAME_ID | — | — |
| 78 | FDIntHdrsCreatedByPersonNamePreNameAdjunct | PRE_NAME_ADJUNCT | — | — |
| 79 | FDIntHdrsCreatedByPersonNamePreviousLastName | PREVIOUS_LAST_NAME | — | — |
| 80 | FDIntHdrsCreatedByPersonNameSuffix | SUFFIX | — | — |
| 81 | FDIntHdrsCreatedByPersonNameTitle | TITLE | — | — |
| 82 | FDIntHdrsLUpdtdByPersonNameDBusinessGroupId9 | BUSINESS_GROUP_ID | — | — |
| 83 | FDIntHdrsLUpdtdByPersonNameDCreatedBy9 | CREATED_BY | — | — |
| 84 | FDIntHdrsLUpdtdByPersonNameDCreationDate9 | CREATION_DATE | — | — |
| 85 | FDIntHdrsLUpdtdByPersonNameDDisplayName1 | DISPLAY_NAME | — | — |
| 86 | FDIntHdrsLUpdtdByPersonNameDEffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 87 | FDIntHdrsLUpdtdByPersonNameDEffectiveStartDate1 | EFFECTIVE_START_DATE | — | — |
| 88 | FDIntHdrsLUpdtdByPersonNameDFirstName1 | FIRST_NAME | — | — |
| 89 | FDIntHdrsLUpdtdByPersonNameDFullName1 | FULL_NAME | — | — |
| 90 | FDIntHdrsLUpdtdByPersonNameDHonors1 | HONORS | — | — |
| 91 | FDIntHdrsLUpdtdByPersonNameDKnownAs1 | KNOWN_AS | — | — |
| 92 | FDIntHdrsLUpdtdByPersonNameDLastName1 | LAST_NAME | — | — |
| 93 | FDIntHdrsLUpdtdByPersonNameDLastUpdateDate9 | LAST_UPDATE_DATE | — | — |
| 94 | FDIntHdrsLUpdtdByPersonNameDLastUpdateLogin9 | LAST_UPDATE_LOGIN | — | — |
| 95 | FDIntHdrsLUpdtdByPersonNameDLastUpdatedBy9 | LAST_UPDATED_BY | — | — |
| 96 | FDIntHdrsLUpdtdByPersonNameDLegislationCode1 | LEGISLATION_CODE | — | — |
| 97 | FDIntHdrsLUpdtdByPersonNameDListName1 | LIST_NAME | — | — |
| 98 | FDIntHdrsLUpdtdByPersonNameDMiddleNames1 | MIDDLE_NAMES | — | — |
| 99 | FDIntHdrsLUpdtdByPersonNameDMilitaryRank1 | MILITARY_RANK | — | — |
| 100 | FDIntHdrsLUpdtdByPersonNameDNameType1 | NAME_TYPE | — | — |
| 101 | FDIntHdrsLUpdtdByPersonNameDObjectVersionNumber9 | OBJECT_VERSION_NUMBER | — | — |
| 102 | FDIntHdrsLUpdtdByPersonNameDOrderName1 | ORDER_NAME | — | — |
| 103 | FDIntHdrsLUpdtdByPersonNameDPersonId9 | PERSON_ID | — | — |
| 104 | FDIntHdrsLUpdtdByPersonNameDPersonNameId1 | PERSON_NAME_ID | — | — |
| 105 | FDIntHdrsLUpdtdByPersonNameDPreNameAdjunct1 | PRE_NAME_ADJUNCT | — | — |
| 106 | FDIntHdrsLUpdtdByPersonNameDPreviousLastName1 | PREVIOUS_LAST_NAME | — | — |
| 107 | FDIntHdrsLUpdtdByPersonNameDSuffix1 | SUFFIX | — | — |
| 108 | FDIntHdrsLUpdtdByPersonNameDTitle1 | TITLE | — | — |
| 109 | FDIntLinesCreatedByPersonNamBusinessGroupId12 | BUSINESS_GROUP_ID | — | — |
| 110 | FDIntLinesCreatedByPersonNamCreatedBy12 | CREATED_BY | — | — |
| 111 | FDIntLinesCreatedByPersonNamCreationDate12 | CREATION_DATE | — | — |
| 112 | FDIntLinesCreatedByPersonNamDisplayName4 | DISPLAY_NAME | — | — |
| 113 | FDIntLinesCreatedByPersonNamEffectiveEndDate4 | EFFECTIVE_END_DATE | — | — |
| 114 | FDIntLinesCreatedByPersonNamEffectiveStartDate4 | EFFECTIVE_START_DATE | — | — |
| 115 | FDIntLinesCreatedByPersonNamFirstName4 | FIRST_NAME | — | — |
| 116 | FDIntLinesCreatedByPersonNamFullName4 | FULL_NAME | — | — |
| 117 | FDIntLinesCreatedByPersonNamHonors4 | HONORS | — | — |
| 118 | FDIntLinesCreatedByPersonNamKnownAs4 | KNOWN_AS | — | — |
| 119 | FDIntLinesCreatedByPersonNamLastName4 | LAST_NAME | — | — |
| 120 | FDIntLinesCreatedByPersonNamLastUpdateDate12 | LAST_UPDATE_DATE | — | — |
| 121 | FDIntLinesCreatedByPersonNamLastUpdateLogin12 | LAST_UPDATE_LOGIN | — | — |
| 122 | FDIntLinesCreatedByPersonNamLastUpdatedBy12 | LAST_UPDATED_BY | — | — |
| 123 | FDIntLinesCreatedByPersonNamLegislationCode4 | LEGISLATION_CODE | — | — |
| 124 | FDIntLinesCreatedByPersonNamListName4 | LIST_NAME | — | — |
| 125 | FDIntLinesCreatedByPersonNamMiddleNames4 | MIDDLE_NAMES | — | — |
| 126 | FDIntLinesCreatedByPersonNamMilitaryRank4 | MILITARY_RANK | — | — |
| 127 | FDIntLinesCreatedByPersonNamNameType4 | NAME_TYPE | — | — |
| 128 | FDIntLinesCreatedByPersonNamObjectVersionNumber12 | OBJECT_VERSION_NUMBER | — | — |
| 129 | FDIntLinesCreatedByPersonNamOrderName4 | ORDER_NAME | — | — |
| 130 | FDIntLinesCreatedByPersonNamPersonId12 | PERSON_ID | — | — |
| 131 | FDIntLinesCreatedByPersonNamPersonNameId4 | PERSON_NAME_ID | — | — |
| 132 | FDIntLinesCreatedByPersonNamPreNameAdjunct4 | PRE_NAME_ADJUNCT | — | — |
| 133 | FDIntLinesCreatedByPersonNamPreviousLastName4 | PREVIOUS_LAST_NAME | — | — |
| 134 | FDIntLinesCreatedByPersonNamSuffix4 | SUFFIX | — | — |
| 135 | FDIntLinesCreatedByPersonNamTitle4 | TITLE | — | — |
| 136 | FDIntLinesLUpdtdByPersonNameBusinessGroupId13 | BUSINESS_GROUP_ID | — | — |
| 137 | FDIntLinesLUpdtdByPersonNameBusinessGroupId14 | BUSINESS_GROUP_ID | — | — |
| 138 | FDIntLinesLUpdtdByPersonNameCreatedBy13 | CREATED_BY | — | — |
| 139 | FDIntLinesLUpdtdByPersonNameCreatedBy14 | CREATED_BY | — | — |
| 140 | FDIntLinesLUpdtdByPersonNameCreationDate13 | CREATION_DATE | — | — |
| 141 | FDIntLinesLUpdtdByPersonNameCreationDate14 | CREATION_DATE | — | — |
| 142 | FDIntLinesLUpdtdByPersonNameDisplayName5 | DISPLAY_NAME | — | — |
| 143 | FDIntLinesLUpdtdByPersonNameDisplayName6 | DISPLAY_NAME | — | — |
| 144 | FDIntLinesLUpdtdByPersonNameEffectiveEndDate5 | EFFECTIVE_END_DATE | — | — |
| 145 | FDIntLinesLUpdtdByPersonNameEffectiveEndDate6 | EFFECTIVE_END_DATE | — | — |
| 146 | FDIntLinesLUpdtdByPersonNameEffectiveStartDate5 | EFFECTIVE_START_DATE | — | — |
| 147 | FDIntLinesLUpdtdByPersonNameEffectiveStartDate6 | EFFECTIVE_START_DATE | — | — |
| 148 | FDIntLinesLUpdtdByPersonNameFirstName5 | FIRST_NAME | — | — |
| 149 | FDIntLinesLUpdtdByPersonNameFirstName6 | FIRST_NAME | — | — |
| 150 | FDIntLinesLUpdtdByPersonNameFullName5 | FULL_NAME | — | — |
| 151 | FDIntLinesLUpdtdByPersonNameFullName6 | FULL_NAME | — | — |
| 152 | FDIntLinesLUpdtdByPersonNameHonors5 | HONORS | — | — |
| 153 | FDIntLinesLUpdtdByPersonNameHonors6 | HONORS | — | — |
| 154 | FDIntLinesLUpdtdByPersonNameKnownAs5 | KNOWN_AS | — | — |
| 155 | FDIntLinesLUpdtdByPersonNameKnownAs6 | KNOWN_AS | — | — |
| 156 | FDIntLinesLUpdtdByPersonNameLastName5 | LAST_NAME | — | — |
| 157 | FDIntLinesLUpdtdByPersonNameLastName6 | LAST_NAME | — | — |
| 158 | FDIntLinesLUpdtdByPersonNameLastUpdateDate13 | LAST_UPDATE_DATE | — | — |
| 159 | FDIntLinesLUpdtdByPersonNameLastUpdateDate14 | LAST_UPDATE_DATE | — | — |
| 160 | FDIntLinesLUpdtdByPersonNameLastUpdateLogin13 | LAST_UPDATE_LOGIN | — | — |
| 161 | FDIntLinesLUpdtdByPersonNameLastUpdateLogin14 | LAST_UPDATE_LOGIN | — | — |
| 162 | FDIntLinesLUpdtdByPersonNameLastUpdatedBy13 | LAST_UPDATED_BY | — | — |
| 163 | FDIntLinesLUpdtdByPersonNameLastUpdatedBy14 | LAST_UPDATED_BY | — | — |
| 164 | FDIntLinesLUpdtdByPersonNameLegislationCode5 | LEGISLATION_CODE | — | — |
| 165 | FDIntLinesLUpdtdByPersonNameLegislationCode6 | LEGISLATION_CODE | — | — |
| 166 | FDIntLinesLUpdtdByPersonNameListName5 | LIST_NAME | — | — |
| 167 | FDIntLinesLUpdtdByPersonNameListName6 | LIST_NAME | — | — |
| 168 | FDIntLinesLUpdtdByPersonNameMiddleNames5 | MIDDLE_NAMES | — | — |
| 169 | FDIntLinesLUpdtdByPersonNameMiddleNames6 | MIDDLE_NAMES | — | — |
| 170 | FDIntLinesLUpdtdByPersonNameMilitaryRank5 | MILITARY_RANK | — | — |
| 171 | FDIntLinesLUpdtdByPersonNameMilitaryRank6 | MILITARY_RANK | — | — |
| 172 | FDIntLinesLUpdtdByPersonNameNameType5 | NAME_TYPE | — | — |
| 173 | FDIntLinesLUpdtdByPersonNameNameType6 | NAME_TYPE | — | — |
| 174 | FDIntLinesLUpdtdByPersonNameObjectVersionNumber13 | OBJECT_VERSION_NUMBER | — | — |
| 175 | FDIntLinesLUpdtdByPersonNameObjectVersionNumber14 | OBJECT_VERSION_NUMBER | — | — |
| 176 | FDIntLinesLUpdtdByPersonNameOrderName5 | ORDER_NAME | — | — |
| 177 | FDIntLinesLUpdtdByPersonNameOrderName6 | ORDER_NAME | — | — |
| 178 | FDIntLinesLUpdtdByPersonNamePersonId13 | PERSON_ID | — | — |
| 179 | FDIntLinesLUpdtdByPersonNamePersonId14 | PERSON_ID | — | — |
| 180 | FDIntLinesLUpdtdByPersonNamePersonNameId5 | PERSON_NAME_ID | — | — |
| 181 | FDIntLinesLUpdtdByPersonNamePersonNameId6 | PERSON_NAME_ID | — | — |
| 182 | FDIntLinesLUpdtdByPersonNamePreNameAdjunct5 | PRE_NAME_ADJUNCT | — | — |
| 183 | FDIntLinesLUpdtdByPersonNamePreNameAdjunct6 | PRE_NAME_ADJUNCT | — | — |
| 184 | FDIntLinesLUpdtdByPersonNamePreviousLastName5 | PREVIOUS_LAST_NAME | — | — |
| 185 | FDIntLinesLUpdtdByPersonNamePreviousLastName6 | PREVIOUS_LAST_NAME | — | — |
| 186 | FDIntLinesLUpdtdByPersonNameSuffix5 | SUFFIX | — | — |
| 187 | FDIntLinesLUpdtdByPersonNameSuffix6 | SUFFIX | — | — |
| 188 | FDIntLinesLUpdtdByPersonNameTitle5 | TITLE | — | — |
| 189 | FDIntLinesLUpdtdByPersonNameTitle6 | TITLE | — | — |
| 190 | FDIntRefLUpdtdByPersonNameDBusinessGroupId15 | BUSINESS_GROUP_ID | — | — |
| 191 | FDIntRefLUpdtdByPersonNameDCreatedBy15 | CREATED_BY | — | — |
| 192 | FDIntRefLUpdtdByPersonNameDCreationDate15 | CREATION_DATE | — | — |
| 193 | FDIntRefLUpdtdByPersonNameDDisplayName7 | DISPLAY_NAME | — | — |
| 194 | FDIntRefLUpdtdByPersonNameDEffectiveEndDate7 | EFFECTIVE_END_DATE | — | — |
| 195 | FDIntRefLUpdtdByPersonNameDEffectiveStartDate7 | EFFECTIVE_START_DATE | — | — |
| 196 | FDIntRefLUpdtdByPersonNameDFirstName7 | FIRST_NAME | — | — |
| 197 | FDIntRefLUpdtdByPersonNameDFullName7 | FULL_NAME | — | — |
| 198 | FDIntRefLUpdtdByPersonNameDHonors7 | HONORS | — | — |
| 199 | FDIntRefLUpdtdByPersonNameDKnownAs7 | KNOWN_AS | — | — |
| 200 | FDIntRefLUpdtdByPersonNameDLastName7 | LAST_NAME | — | — |
| 201 | FDIntRefLUpdtdByPersonNameDLastUpdateDate15 | LAST_UPDATE_DATE | — | — |
| 202 | FDIntRefLUpdtdByPersonNameDLastUpdateLogin15 | LAST_UPDATE_LOGIN | — | — |
| 203 | FDIntRefLUpdtdByPersonNameDLastUpdatedBy15 | LAST_UPDATED_BY | — | — |
| 204 | FDIntRefLUpdtdByPersonNameDLegislationCode7 | LEGISLATION_CODE | — | — |
| 205 | FDIntRefLUpdtdByPersonNameDListName7 | LIST_NAME | — | — |
| 206 | FDIntRefLUpdtdByPersonNameDMiddleNames7 | MIDDLE_NAMES | — | — |
| 207 | FDIntRefLUpdtdByPersonNameDMilitaryRank7 | MILITARY_RANK | — | — |
| 208 | FDIntRefLUpdtdByPersonNameDNameType7 | NAME_TYPE | — | — |
| 209 | FDIntRefLUpdtdByPersonNameDObjectVersionNumber15 | OBJECT_VERSION_NUMBER | — | — |
| 210 | FDIntRefLUpdtdByPersonNameDOrderName7 | ORDER_NAME | — | — |
| 211 | FDIntRefLUpdtdByPersonNameDPersonId15 | PERSON_ID | — | — |
| 212 | FDIntRefLUpdtdByPersonNameDPersonNameId7 | PERSON_NAME_ID | — | — |
| 213 | FDIntRefLUpdtdByPersonNameDPreNameAdjunct7 | PRE_NAME_ADJUNCT | — | — |
| 214 | FDIntRefLUpdtdByPersonNameDPreviousLastName7 | PREVIOUS_LAST_NAME | — | — |
| 215 | FDIntRefLUpdtdByPersonNameDSuffix7 | SUFFIX | — | — |
| 216 | FDIntRefLUpdtdByPersonNameDTitle7 | TITLE | — | — |
| 217 | FDLegalProcCreatedByPersonNaBusinessGroupId10 | BUSINESS_GROUP_ID | — | — |
| 218 | FDLegalProcCreatedByPersonNaCreatedBy10 | CREATED_BY | — | — |
| 219 | FDLegalProcCreatedByPersonNaCreationDate10 | CREATION_DATE | — | — |
| 220 | FDLegalProcCreatedByPersonNaDisplayName2 | DISPLAY_NAME | — | — |
| 221 | FDLegalProcCreatedByPersonNaEffectiveEndDate2 | EFFECTIVE_END_DATE | — | — |
| 222 | FDLegalProcCreatedByPersonNaEffectiveStartDate2 | EFFECTIVE_START_DATE | — | — |
| 223 | FDLegalProcCreatedByPersonNaFirstName2 | FIRST_NAME | — | — |
| 224 | FDLegalProcCreatedByPersonNaFullName2 | FULL_NAME | — | — |
| 225 | FDLegalProcCreatedByPersonNaHonors2 | HONORS | — | — |
| 226 | FDLegalProcCreatedByPersonNaKnownAs2 | KNOWN_AS | — | — |
| 227 | FDLegalProcCreatedByPersonNaLastName2 | LAST_NAME | — | — |
| 228 | FDLegalProcCreatedByPersonNaLastUpdateDate10 | LAST_UPDATE_DATE | — | — |
| 229 | FDLegalProcCreatedByPersonNaLastUpdateLogin10 | LAST_UPDATE_LOGIN | — | — |
| 230 | FDLegalProcCreatedByPersonNaLastUpdatedBy10 | LAST_UPDATED_BY | — | — |
| 231 | FDLegalProcCreatedByPersonNaLegislationCode2 | LEGISLATION_CODE | — | — |
| 232 | FDLegalProcCreatedByPersonNaListName2 | LIST_NAME | — | — |
| 233 | FDLegalProcCreatedByPersonNaMiddleNames2 | MIDDLE_NAMES | — | — |
| 234 | FDLegalProcCreatedByPersonNaMilitaryRank2 | MILITARY_RANK | — | — |
| 235 | FDLegalProcCreatedByPersonNaNameType2 | NAME_TYPE | — | — |
| 236 | FDLegalProcCreatedByPersonNaObjectVersionNumber10 | OBJECT_VERSION_NUMBER | — | — |
| 237 | FDLegalProcCreatedByPersonNaOrderName2 | ORDER_NAME | — | — |
| 238 | FDLegalProcCreatedByPersonNaPersonId10 | PERSON_ID | — | — |
| 239 | FDLegalProcCreatedByPersonNaPersonNameId2 | PERSON_NAME_ID | — | — |
| 240 | FDLegalProcCreatedByPersonNaPreNameAdjunct2 | PRE_NAME_ADJUNCT | — | — |
| 241 | FDLegalProcCreatedByPersonNaPreviousLastName2 | PREVIOUS_LAST_NAME | — | — |
| 242 | FDLegalProcCreatedByPersonNaSuffix2 | SUFFIX | — | — |
| 243 | FDLegalProcCreatedByPersonNaTitle2 | TITLE | — | — |
| 244 | FDLegalProcLUpdatedByPersonNBusinessGroupId11 | BUSINESS_GROUP_ID | — | — |
| 245 | FDLegalProcLUpdatedByPersonNCreatedBy11 | CREATED_BY | — | — |
| 246 | FDLegalProcLUpdatedByPersonNCreationDate11 | CREATION_DATE | — | — |
| 247 | FDLegalProcLUpdatedByPersonNDisplayName3 | DISPLAY_NAME | — | — |
| 248 | FDLegalProcLUpdatedByPersonNEffectiveEndDate3 | EFFECTIVE_END_DATE | — | — |
| 249 | FDLegalProcLUpdatedByPersonNEffectiveStartDate3 | EFFECTIVE_START_DATE | — | — |
| 250 | FDLegalProcLUpdatedByPersonNFirstName3 | FIRST_NAME | — | — |
| 251 | FDLegalProcLUpdatedByPersonNFullName3 | FULL_NAME | — | — |
| 252 | FDLegalProcLUpdatedByPersonNHonors3 | HONORS | — | — |
| 253 | FDLegalProcLUpdatedByPersonNKnownAs3 | KNOWN_AS | — | — |
| 254 | FDLegalProcLUpdatedByPersonNLastName3 | LAST_NAME | — | — |
| 255 | FDLegalProcLUpdatedByPersonNLastUpdateDate11 | LAST_UPDATE_DATE | — | — |
| 256 | FDLegalProcLUpdatedByPersonNLastUpdateLogin11 | LAST_UPDATE_LOGIN | — | — |
| 257 | FDLegalProcLUpdatedByPersonNLastUpdatedBy11 | LAST_UPDATED_BY | — | — |
| 258 | FDLegalProcLUpdatedByPersonNLegislationCode3 | LEGISLATION_CODE | — | — |
| 259 | FDLegalProcLUpdatedByPersonNListName3 | LIST_NAME | — | — |
| 260 | FDLegalProcLUpdatedByPersonNMiddleNames3 | MIDDLE_NAMES | — | — |
| 261 | FDLegalProcLUpdatedByPersonNMilitaryRank3 | MILITARY_RANK | — | — |
| 262 | FDLegalProcLUpdatedByPersonNNameType3 | NAME_TYPE | — | — |
| 263 | FDLegalProcLUpdatedByPersonNObjectVersionNumber11 | OBJECT_VERSION_NUMBER | — | — |
| 264 | FDLegalProcLUpdatedByPersonNOrderName3 | ORDER_NAME | — | — |
| 265 | FDLegalProcLUpdatedByPersonNPersonId11 | PERSON_ID | — | — |
| 266 | FDLegalProcLUpdatedByPersonNPersonNameId3 | PERSON_NAME_ID | — | — |
| 267 | FDLegalProcLUpdatedByPersonNPreNameAdjunct3 | PRE_NAME_ADJUNCT | — | — |
| 268 | FDLegalProcLUpdatedByPersonNPreviousLastName3 | PREVIOUS_LAST_NAME | — | — |
| 269 | FDLegalProcLUpdatedByPersonNSuffix3 | SUFFIX | — | — |
| 270 | FDLegalProcLUpdatedByPersonNTitle3 | TITLE | — | — |
| 271 | FDLineIntCreatedByPNBusinessGroupId6 | BUSINESS_GROUP_ID | — | — |
| 272 | FDLineIntCreatedByPNCreatedBy6 | CREATED_BY | — | — |
| 273 | FDLineIntCreatedByPNCreationDate6 | CREATION_DATE | — | — |
| 274 | FDLineIntCreatedByPNDisplayName2 | DISPLAY_NAME | — | — |
| 275 | FDLineIntCreatedByPNEffectiveEndDate2 | EFFECTIVE_END_DATE | — | — |
| 276 | FDLineIntCreatedByPNEffectiveStartDate2 | EFFECTIVE_START_DATE | — | — |
| 277 | FDLineIntCreatedByPNFirstName2 | FIRST_NAME | — | — |
| 278 | FDLineIntCreatedByPNFullName2 | FULL_NAME | — | — |
| 279 | FDLineIntCreatedByPNHonors2 | HONORS | — | — |
| 280 | FDLineIntCreatedByPNKnownAs2 | KNOWN_AS | — | — |
| 281 | FDLineIntCreatedByPNLastName2 | LAST_NAME | — | — |
| 282 | FDLineIntCreatedByPNLastUpdateDate6 | LAST_UPDATE_DATE | — | — |
| 283 | FDLineIntCreatedByPNLastUpdateLogin6 | LAST_UPDATE_LOGIN | — | — |
| 284 | FDLineIntCreatedByPNLastUpdatedBy6 | LAST_UPDATED_BY | — | — |
| 285 | FDLineIntCreatedByPNLegislationCode2 | LEGISLATION_CODE | — | — |
| 286 | FDLineIntCreatedByPNListName2 | LIST_NAME | — | — |
| 287 | FDLineIntCreatedByPNMiddleNames2 | MIDDLE_NAMES | — | — |
| 288 | FDLineIntCreatedByPNMilitaryRank2 | MILITARY_RANK | — | — |
| 289 | FDLineIntCreatedByPNNameType2 | NAME_TYPE | — | — |
| 290 | FDLineIntCreatedByPNObjectVersionNumber6 | OBJECT_VERSION_NUMBER | — | — |
| 291 | FDLineIntCreatedByPNOrderName2 | ORDER_NAME | — | — |
| 292 | FDLineIntCreatedByPNPersonId6 | PERSON_ID | — | — |
| 293 | FDLineIntCreatedByPNPersonNameId2 | PERSON_NAME_ID | — | — |
| 294 | FDLineIntCreatedByPNPreNameAdjunct2 | PRE_NAME_ADJUNCT | — | — |
| 295 | FDLineIntCreatedByPNPreviousLastName2 | PREVIOUS_LAST_NAME | — | — |
| 296 | FDLineIntCreatedByPNSuffix2 | SUFFIX | — | — |
| 297 | FDLineIntCreatedByPNTitle2 | TITLE | — | — |
| 298 | FDLineIntLastUpdtdByPNBusinessGroupId7 | BUSINESS_GROUP_ID | — | — |
| 299 | FDLineIntLastUpdtdByPNCreatedBy7 | CREATED_BY | — | — |
| 300 | FDLineIntLastUpdtdByPNCreationDate7 | CREATION_DATE | — | — |
| 301 | FDLineIntLastUpdtdByPNDisplayName3 | DISPLAY_NAME | — | — |
| 302 | FDLineIntLastUpdtdByPNEffectiveEndDate3 | EFFECTIVE_END_DATE | — | — |
| 303 | FDLineIntLastUpdtdByPNEffectiveStartDate3 | EFFECTIVE_START_DATE | — | — |
| 304 | FDLineIntLastUpdtdByPNFirstName3 | FIRST_NAME | — | — |
| 305 | FDLineIntLastUpdtdByPNFullName3 | FULL_NAME | — | — |
| 306 | FDLineIntLastUpdtdByPNHonors3 | HONORS | — | — |
| 307 | FDLineIntLastUpdtdByPNKnownAs3 | KNOWN_AS | — | — |
| 308 | FDLineIntLastUpdtdByPNLastName3 | LAST_NAME | — | — |
| 309 | FDLineIntLastUpdtdByPNLastUpdateDate7 | LAST_UPDATE_DATE | — | — |
| 310 | FDLineIntLastUpdtdByPNLastUpdateLogin7 | LAST_UPDATE_LOGIN | — | — |
| 311 | FDLineIntLastUpdtdByPNLastUpdatedBy7 | LAST_UPDATED_BY | — | — |
| 312 | FDLineIntLastUpdtdByPNLegislationCode3 | LEGISLATION_CODE | — | — |
| 313 | FDLineIntLastUpdtdByPNListName3 | LIST_NAME | — | — |
| 314 | FDLineIntLastUpdtdByPNMiddleNames3 | MIDDLE_NAMES | — | — |
| 315 | FDLineIntLastUpdtdByPNMilitaryRank3 | MILITARY_RANK | — | — |
| 316 | FDLineIntLastUpdtdByPNNameType3 | NAME_TYPE | — | — |
| 317 | FDLineIntLastUpdtdByPNObjectVersionNumber7 | OBJECT_VERSION_NUMBER | — | — |
| 318 | FDLineIntLastUpdtdByPNOrderName3 | ORDER_NAME | — | — |
| 319 | FDLineIntLastUpdtdByPNPersonId7 | PERSON_ID | — | — |
| 320 | FDLineIntLastUpdtdByPNPersonNameId3 | PERSON_NAME_ID | — | — |
| 321 | FDLineIntLastUpdtdByPNPreNameAdjunct3 | PRE_NAME_ADJUNCT | — | — |
| 322 | FDLineIntLastUpdtdByPNPreviousLastName3 | PREVIOUS_LAST_NAME | — | — |
| 323 | FDLineIntLastUpdtdByPNSuffix3 | SUFFIX | — | — |
| 324 | FDLineIntLastUpdtdByPNTitle3 | TITLE | — | — |
| 325 | TaxLineIntrCreatedByPersonNaBusinessGroupId2 | BUSINESS_GROUP_ID | — | — |
| 326 | TaxLineIntrCreatedByPersonNaCreatedBy2 | CREATED_BY | — | — |
| 327 | TaxLineIntrCreatedByPersonNaCreationDate2 | CREATION_DATE | — | — |
| 328 | TaxLineIntrCreatedByPersonNaDisplayName | DISPLAY_NAME | — | — |
| 329 | TaxLineIntrCreatedByPersonNaEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 330 | TaxLineIntrCreatedByPersonNaEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 331 | TaxLineIntrCreatedByPersonNaFirstName | FIRST_NAME | — | — |
| 332 | TaxLineIntrCreatedByPersonNaFullName | FULL_NAME | — | ✅ |
| 333 | TaxLineIntrCreatedByPersonNaHonors | HONORS | — | — |
| 334 | TaxLineIntrCreatedByPersonNaKnownAs | KNOWN_AS | — | — |
| 335 | TaxLineIntrCreatedByPersonNaLastName | LAST_NAME | — | — |
| 336 | TaxLineIntrCreatedByPersonNaLastUpdateDate2 | LAST_UPDATE_DATE | — | — |
| 337 | TaxLineIntrCreatedByPersonNaLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 338 | TaxLineIntrCreatedByPersonNaLastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 339 | TaxLineIntrCreatedByPersonNaLegislationCode | LEGISLATION_CODE | — | — |
| 340 | TaxLineIntrCreatedByPersonNaListName | LIST_NAME | — | — |
| 341 | TaxLineIntrCreatedByPersonNaMiddleNames | MIDDLE_NAMES | — | — |
| 342 | TaxLineIntrCreatedByPersonNaMilitaryRank | MILITARY_RANK | — | — |
| 343 | TaxLineIntrCreatedByPersonNaNameType | NAME_TYPE | — | — |
| 344 | TaxLineIntrCreatedByPersonNaObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 345 | TaxLineIntrCreatedByPersonNaOrderName | ORDER_NAME | — | — |
| 346 | TaxLineIntrCreatedByPersonNaPersonId2 | PERSON_ID | — | — |
| 347 | TaxLineIntrCreatedByPersonNaPersonNameId | PERSON_NAME_ID | — | — |
| 348 | TaxLineIntrCreatedByPersonNaPreNameAdjunct | PRE_NAME_ADJUNCT | — | — |
| 349 | TaxLineIntrCreatedByPersonNaPreviousLastName | PREVIOUS_LAST_NAME | — | — |
| 350 | TaxLineIntrCreatedByPersonNaSuffix | SUFFIX | — | — |
| 351 | TaxLineIntrCreatedByPersonNaTitle | TITLE | — | — |
| 352 | TaxLineIntrLastUpdtdByPersonBusinessGroupId3 | BUSINESS_GROUP_ID | — | — |
| 353 | TaxLineIntrLastUpdtdByPersonCreatedBy3 | CREATED_BY | — | — |
| 354 | TaxLineIntrLastUpdtdByPersonCreationDate3 | CREATION_DATE | — | — |
| 355 | TaxLineIntrLastUpdtdByPersonDisplayName1 | DISPLAY_NAME | — | — |
| 356 | TaxLineIntrLastUpdtdByPersonEffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 357 | TaxLineIntrLastUpdtdByPersonEffectiveStartDate1 | EFFECTIVE_START_DATE | — | — |
| 358 | TaxLineIntrLastUpdtdByPersonFirstName1 | FIRST_NAME | — | — |
| 359 | TaxLineIntrLastUpdtdByPersonFullName1 | FULL_NAME | — | ✅ |
| 360 | TaxLineIntrLastUpdtdByPersonHonors1 | HONORS | — | — |
| 361 | TaxLineIntrLastUpdtdByPersonKnownAs1 | KNOWN_AS | — | — |
| 362 | TaxLineIntrLastUpdtdByPersonLastName1 | LAST_NAME | — | — |
| 363 | TaxLineIntrLastUpdtdByPersonLastUpdateDate3 | LAST_UPDATE_DATE | — | — |
| 364 | TaxLineIntrLastUpdtdByPersonLastUpdateLogin3 | LAST_UPDATE_LOGIN | — | — |
| 365 | TaxLineIntrLastUpdtdByPersonLastUpdatedBy3 | LAST_UPDATED_BY | — | — |
| 366 | TaxLineIntrLastUpdtdByPersonLegislationCode1 | LEGISLATION_CODE | — | — |
| 367 | TaxLineIntrLastUpdtdByPersonListName1 | LIST_NAME | — | — |
| 368 | TaxLineIntrLastUpdtdByPersonMiddleNames1 | MIDDLE_NAMES | — | — |
| 369 | TaxLineIntrLastUpdtdByPersonMilitaryRank1 | MILITARY_RANK | — | — |
| 370 | TaxLineIntrLastUpdtdByPersonNameType1 | NAME_TYPE | — | — |
| 371 | TaxLineIntrLastUpdtdByPersonObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 372 | TaxLineIntrLastUpdtdByPersonOrderName1 | ORDER_NAME | — | — |
| 373 | TaxLineIntrLastUpdtdByPersonPersonId3 | PERSON_ID | — | — |
| 374 | TaxLineIntrLastUpdtdByPersonPersonNameId1 | PERSON_NAME_ID | — | — |
| 375 | TaxLineIntrLastUpdtdByPersonPreNameAdjunct1 | PRE_NAME_ADJUNCT | — | — |
| 376 | TaxLineIntrLastUpdtdByPersonPreviousLastName1 | PREVIOUS_LAST_NAME | — | — |
| 377 | TaxLineIntrLastUpdtdByPersonSuffix1 | SUFFIX | — | — |
| 378 | TaxLineIntrLastUpdtdByPersonTitle1 | TITLE | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FDHeaderIntrEOCreatedByUserPActiveFlag | ACTIVE_FLAG | — | — |
| 2 | FDHeaderIntrEOCreatedByUserPBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | FDHeaderIntrEOCreatedByUserPCreatedBy | CREATED_BY | — | — |
| 4 | FDHeaderIntrEOCreatedByUserPCreationDate | CREATION_DATE | — | — |
| 5 | FDHeaderIntrEOCreatedByUserPCredentialsEmailSent | CREDENTIALS_EMAIL_SENT | — | — |
| 6 | FDHeaderIntrEOCreatedByUserPEndDate | END_DATE | — | — |
| 7 | FDHeaderIntrEOCreatedByUserPExternalId | EXTERNAL_ID | — | — |
| 8 | FDHeaderIntrEOCreatedByUserPHrTerminated | HR_TERMINATED | — | — |
| 9 | FDHeaderIntrEOCreatedByUserPLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 10 | FDHeaderIntrEOCreatedByUserPLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | FDHeaderIntrEOCreatedByUserPLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | FDHeaderIntrEOCreatedByUserPMultitenancyUsername | MULTITENANCY_USERNAME | — | — |
| 13 | FDHeaderIntrEOCreatedByUserPObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | FDHeaderIntrEOCreatedByUserPPartyId | PARTY_ID | — | — |
| 15 | FDHeaderIntrEOCreatedByUserPPersonId | PERSON_ID | — | — |
| 16 | FDHeaderIntrEOCreatedByUserPStartDate | START_DATE | — | — |
| 17 | FDHeaderIntrEOCreatedByUserPSuspended | SUSPENDED | — | — |
| 18 | FDHeaderIntrEOCreatedByUserPUserDataChecksum | USER_DATA_CHECKSUM | — | — |
| 19 | FDHeaderIntrEOCreatedByUserPUserDistinguishedName | USER_DISTINGUISHED_NAME | — | — |
| 20 | FDHeaderIntrEOCreatedByUserPUserGuid | USER_GUID | — | — |
| 21 | FDHeaderIntrEOCreatedByUserPUserId | USER_ID | — | — |
| 22 | FDHeaderIntrEOCreatedByUserPUsername | USERNAME | — | — |
| 23 | FDHeaderIntrLastUpdtdByUserPActiveFlag1 | ACTIVE_FLAG | — | — |
| 24 | FDHeaderIntrLastUpdtdByUserPBusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 25 | FDHeaderIntrLastUpdtdByUserPCreatedBy1 | CREATED_BY | — | — |
| 26 | FDHeaderIntrLastUpdtdByUserPCreationDate1 | CREATION_DATE | — | — |
| 27 | FDHeaderIntrLastUpdtdByUserPCredentialsEmailSent1 | CREDENTIALS_EMAIL_SENT | — | — |
| 28 | FDHeaderIntrLastUpdtdByUserPEndDate1 | END_DATE | — | — |
| 29 | FDHeaderIntrLastUpdtdByUserPExternalId1 | EXTERNAL_ID | — | — |
| 30 | FDHeaderIntrLastUpdtdByUserPHrTerminated1 | HR_TERMINATED | — | — |
| 31 | FDHeaderIntrLastUpdtdByUserPLastUpdateDate1 | LAST_UPDATE_DATE | — | — |
| 32 | FDHeaderIntrLastUpdtdByUserPLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 33 | FDHeaderIntrLastUpdtdByUserPLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 34 | FDHeaderIntrLastUpdtdByUserPMultitenancyUsername1 | MULTITENANCY_USERNAME | — | — |
| 35 | FDHeaderIntrLastUpdtdByUserPObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 36 | FDHeaderIntrLastUpdtdByUserPPartyId1 | PARTY_ID | — | — |
| 37 | FDHeaderIntrLastUpdtdByUserPPersonId1 | PERSON_ID | — | — |
| 38 | FDHeaderIntrLastUpdtdByUserPStartDate1 | START_DATE | — | — |
| 39 | FDHeaderIntrLastUpdtdByUserPSuspended1 | SUSPENDED | — | — |
| 40 | FDHeaderIntrLastUpdtdByUserPUserDataChecksum1 | USER_DATA_CHECKSUM | — | — |
| 41 | FDHeaderIntrLastUpdtdByUserPUserDistinguishedName1 | USER_DISTINGUISHED_NAME | — | — |
| 42 | FDHeaderIntrLastUpdtdByUserPUserGuid1 | USER_GUID | — | — |
| 43 | FDHeaderIntrLastUpdtdByUserPUserId1 | USER_ID | — | — |
| 44 | FDHeaderIntrLastUpdtdByUserPUsername1 | USERNAME | — | — |
| 45 | FDIntHeadersCreatedByUserPEOActiveFlag | ACTIVE_FLAG | — | — |
| 46 | FDIntHeadersCreatedByUserPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 47 | FDIntHeadersCreatedByUserPEOCreatedBy | CREATED_BY | — | — |
| 48 | FDIntHeadersCreatedByUserPEOCreationDate | CREATION_DATE | — | — |
| 49 | FDIntHeadersCreatedByUserPEOCredentialsEmailSent | CREDENTIALS_EMAIL_SENT | — | — |
| 50 | FDIntHeadersCreatedByUserPEOEndDate | END_DATE | — | — |
| 51 | FDIntHeadersCreatedByUserPEOExternalId | EXTERNAL_ID | — | — |
| 52 | FDIntHeadersCreatedByUserPEOHrTerminated | HR_TERMINATED | — | — |
| 53 | FDIntHeadersCreatedByUserPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 54 | FDIntHeadersCreatedByUserPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 55 | FDIntHeadersCreatedByUserPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 56 | FDIntHeadersCreatedByUserPEOMultitenancyUsername | MULTITENANCY_USERNAME | — | — |
| 57 | FDIntHeadersCreatedByUserPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 58 | FDIntHeadersCreatedByUserPEOPartyId | PARTY_ID | — | — |
| 59 | FDIntHeadersCreatedByUserPEOPersonId | PERSON_ID | — | — |
| 60 | FDIntHeadersCreatedByUserPEOStartDate | START_DATE | — | — |
| 61 | FDIntHeadersCreatedByUserPEOSuspended | SUSPENDED | — | — |
| 62 | FDIntHeadersCreatedByUserPEOUserDataChecksum | USER_DATA_CHECKSUM | — | — |
| 63 | FDIntHeadersCreatedByUserPEOUserDistinguishedName | USER_DISTINGUISHED_NAME | — | — |
| 64 | FDIntHeadersCreatedByUserPEOUserGuid | USER_GUID | — | — |
| 65 | FDIntHeadersCreatedByUserPEOUserId | USER_ID | — | — |
| 66 | FDIntHeadersCreatedByUserPEOUsername | USERNAME | — | — |
| 67 | FDIntHeadersLUpdatedByUserPEActiveFlag1 | ACTIVE_FLAG | — | — |
| 68 | FDIntHeadersLUpdatedByUserPEBusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 69 | FDIntHeadersLUpdatedByUserPECreatedBy1 | CREATED_BY | — | — |
| 70 | FDIntHeadersLUpdatedByUserPECreationDate1 | CREATION_DATE | — | — |
| 71 | FDIntHeadersLUpdatedByUserPECredentialsEmailSent1 | CREDENTIALS_EMAIL_SENT | — | — |
| 72 | FDIntHeadersLUpdatedByUserPEEndDate1 | END_DATE | — | — |
| 73 | FDIntHeadersLUpdatedByUserPEExternalId1 | EXTERNAL_ID | — | — |
| 74 | FDIntHeadersLUpdatedByUserPEHrTerminated1 | HR_TERMINATED | — | — |
| 75 | FDIntHeadersLUpdatedByUserPELastUpdateDate1 | LAST_UPDATE_DATE | — | — |
| 76 | FDIntHeadersLUpdatedByUserPELastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 77 | FDIntHeadersLUpdatedByUserPELastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 78 | FDIntHeadersLUpdatedByUserPEMultitenancyUsername1 | MULTITENANCY_USERNAME | — | — |
| 79 | FDIntHeadersLUpdatedByUserPEObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 80 | FDIntHeadersLUpdatedByUserPEPartyId1 | PARTY_ID | — | — |
| 81 | FDIntHeadersLUpdatedByUserPEPersonId1 | PERSON_ID | — | — |
| 82 | FDIntHeadersLUpdatedByUserPEStartDate1 | START_DATE | — | — |
| 83 | FDIntHeadersLUpdatedByUserPESuspended1 | SUSPENDED | — | — |
| 84 | FDIntHeadersLUpdatedByUserPEUserDataChecksum1 | USER_DATA_CHECKSUM | — | — |
| 85 | FDIntHeadersLUpdatedByUserPEUserDistinguishedName1 | USER_DISTINGUISHED_NAME | — | — |
| 86 | FDIntHeadersLUpdatedByUserPEUserGuid1 | USER_GUID | — | — |
| 87 | FDIntHeadersLUpdatedByUserPEUserId1 | USER_ID | — | — |
| 88 | FDIntHeadersLUpdatedByUserPEUsername1 | USERNAME | — | — |
| 89 | FDIntLegalProcCreatedByUserPActiveFlag2 | ACTIVE_FLAG | — | — |
| 90 | FDIntLegalProcCreatedByUserPBusinessGroupId2 | BUSINESS_GROUP_ID | — | — |
| 91 | FDIntLegalProcCreatedByUserPCreatedBy2 | CREATED_BY | — | — |
| 92 | FDIntLegalProcCreatedByUserPCreationDate2 | CREATION_DATE | — | — |
| 93 | FDIntLegalProcCreatedByUserPCredentialsEmailSent2 | CREDENTIALS_EMAIL_SENT | — | — |
| 94 | FDIntLegalProcCreatedByUserPEndDate2 | END_DATE | — | — |
| 95 | FDIntLegalProcCreatedByUserPExternalId2 | EXTERNAL_ID | — | — |
| 96 | FDIntLegalProcCreatedByUserPHrTerminated2 | HR_TERMINATED | — | — |
| 97 | FDIntLegalProcCreatedByUserPLastUpdateDate2 | LAST_UPDATE_DATE | — | — |
| 98 | FDIntLegalProcCreatedByUserPLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 99 | FDIntLegalProcCreatedByUserPLastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 100 | FDIntLegalProcCreatedByUserPMultitenancyUsername2 | MULTITENANCY_USERNAME | — | — |
| 101 | FDIntLegalProcCreatedByUserPObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 102 | FDIntLegalProcCreatedByUserPPartyId2 | PARTY_ID | — | — |
| 103 | FDIntLegalProcCreatedByUserPPersonId2 | PERSON_ID | — | — |
| 104 | FDIntLegalProcCreatedByUserPStartDate2 | START_DATE | — | — |
| 105 | FDIntLegalProcCreatedByUserPSuspended2 | SUSPENDED | — | — |
| 106 | FDIntLegalProcCreatedByUserPUserDataChecksum2 | USER_DATA_CHECKSUM | — | — |
| 107 | FDIntLegalProcCreatedByUserPUserDistinguishedName2 | USER_DISTINGUISHED_NAME | — | — |
| 108 | FDIntLegalProcCreatedByUserPUserGuid2 | USER_GUID | — | — |
| 109 | FDIntLegalProcCreatedByUserPUserId2 | USER_ID | — | — |
| 110 | FDIntLegalProcCreatedByUserPUsername2 | USERNAME | — | — |
| 111 | FDIntLegalProcLUpdatedByUserActiveFlag3 | ACTIVE_FLAG | — | — |
| 112 | FDIntLegalProcLUpdatedByUserBusinessGroupId3 | BUSINESS_GROUP_ID | — | — |
| 113 | FDIntLegalProcLUpdatedByUserCreatedBy3 | CREATED_BY | — | — |
| 114 | FDIntLegalProcLUpdatedByUserCreationDate3 | CREATION_DATE | — | — |
| 115 | FDIntLegalProcLUpdatedByUserCredentialsEmailSent3 | CREDENTIALS_EMAIL_SENT | — | — |
| 116 | FDIntLegalProcLUpdatedByUserEndDate3 | END_DATE | — | — |
| 117 | FDIntLegalProcLUpdatedByUserExternalId3 | EXTERNAL_ID | — | — |
| 118 | FDIntLegalProcLUpdatedByUserHrTerminated3 | HR_TERMINATED | — | — |
| 119 | FDIntLegalProcLUpdatedByUserLastUpdateDate3 | LAST_UPDATE_DATE | — | — |
| 120 | FDIntLegalProcLUpdatedByUserLastUpdateLogin3 | LAST_UPDATE_LOGIN | — | — |
| 121 | FDIntLegalProcLUpdatedByUserLastUpdatedBy3 | LAST_UPDATED_BY | — | — |
| 122 | FDIntLegalProcLUpdatedByUserMultitenancyUsername3 | MULTITENANCY_USERNAME | — | — |
| 123 | FDIntLegalProcLUpdatedByUserObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 124 | FDIntLegalProcLUpdatedByUserPartyId3 | PARTY_ID | — | — |
| 125 | FDIntLegalProcLUpdatedByUserPersonId3 | PERSON_ID | — | — |
| 126 | FDIntLegalProcLUpdatedByUserStartDate3 | START_DATE | — | — |
| 127 | FDIntLegalProcLUpdatedByUserSuspended3 | SUSPENDED | — | — |
| 128 | FDIntLegalProcLUpdatedByUserUserDataChecksum3 | USER_DATA_CHECKSUM | — | — |
| 129 | FDIntLegalProcLUpdatedByUserUserDistinguishedName3 | USER_DISTINGUISHED_NAME | — | — |
| 130 | FDIntLegalProcLUpdatedByUserUserGuid3 | USER_GUID | — | — |
| 131 | FDIntLegalProcLUpdatedByUserUserId3 | USER_ID | — | — |
| 132 | FDIntLegalProcLUpdatedByUserUsername3 | USERNAME | — | — |
| 133 | FDIntLinesCreatedByUserPEOActiveFlag4 | ACTIVE_FLAG | — | — |
| 134 | FDIntLinesCreatedByUserPEOBusinessGroupId4 | BUSINESS_GROUP_ID | — | — |
| 135 | FDIntLinesCreatedByUserPEOCreatedBy4 | CREATED_BY | — | — |
| 136 | FDIntLinesCreatedByUserPEOCreationDate4 | CREATION_DATE | — | — |
| 137 | FDIntLinesCreatedByUserPEOCredentialsEmailSent4 | CREDENTIALS_EMAIL_SENT | — | — |
| 138 | FDIntLinesCreatedByUserPEOEndDate4 | END_DATE | — | — |
| 139 | FDIntLinesCreatedByUserPEOExternalId4 | EXTERNAL_ID | — | — |
| 140 | FDIntLinesCreatedByUserPEOHrTerminated4 | HR_TERMINATED | — | — |
| 141 | FDIntLinesCreatedByUserPEOLastUpdateDate4 | LAST_UPDATE_DATE | — | — |
| 142 | FDIntLinesCreatedByUserPEOLastUpdateLogin4 | LAST_UPDATE_LOGIN | — | — |
| 143 | FDIntLinesCreatedByUserPEOLastUpdatedBy4 | LAST_UPDATED_BY | — | — |
| 144 | FDIntLinesCreatedByUserPEOMultitenancyUsername4 | MULTITENANCY_USERNAME | — | — |
| 145 | FDIntLinesCreatedByUserPEOObjectVersionNumber4 | OBJECT_VERSION_NUMBER | — | — |
| 146 | FDIntLinesCreatedByUserPEOPartyId4 | PARTY_ID | — | — |
| 147 | FDIntLinesCreatedByUserPEOPersonId4 | PERSON_ID | — | — |
| 148 | FDIntLinesCreatedByUserPEOStartDate4 | START_DATE | — | — |
| 149 | FDIntLinesCreatedByUserPEOSuspended4 | SUSPENDED | — | — |
| 150 | FDIntLinesCreatedByUserPEOUserDataChecksum4 | USER_DATA_CHECKSUM | — | — |
| 151 | FDIntLinesCreatedByUserPEOUserDistinguishedName4 | USER_DISTINGUISHED_NAME | — | — |
| 152 | FDIntLinesCreatedByUserPEOUserGuid4 | USER_GUID | — | — |
| 153 | FDIntLinesCreatedByUserPEOUserId4 | USER_ID | — | — |
| 154 | FDIntLinesCreatedByUserPEOUsername4 | USERNAME | — | — |
| 155 | FDIntLinesLUpdatedByUserPEOActiveFlag5 | ACTIVE_FLAG | — | — |
| 156 | FDIntLinesLUpdatedByUserPEOBusinessGroupId5 | BUSINESS_GROUP_ID | — | — |
| 157 | FDIntLinesLUpdatedByUserPEOCreatedBy5 | CREATED_BY | — | — |
| 158 | FDIntLinesLUpdatedByUserPEOCreationDate5 | CREATION_DATE | — | — |
| 159 | FDIntLinesLUpdatedByUserPEOCredentialsEmailSent5 | CREDENTIALS_EMAIL_SENT | — | — |
| 160 | FDIntLinesLUpdatedByUserPEOEndDate5 | END_DATE | — | — |
| 161 | FDIntLinesLUpdatedByUserPEOExternalId5 | EXTERNAL_ID | — | — |
| 162 | FDIntLinesLUpdatedByUserPEOHrTerminated5 | HR_TERMINATED | — | — |
| 163 | FDIntLinesLUpdatedByUserPEOLastUpdateDate5 | LAST_UPDATE_DATE | — | — |
| 164 | FDIntLinesLUpdatedByUserPEOLastUpdateLogin5 | LAST_UPDATE_LOGIN | — | — |
| 165 | FDIntLinesLUpdatedByUserPEOLastUpdatedBy5 | LAST_UPDATED_BY | — | — |
| 166 | FDIntLinesLUpdatedByUserPEOMultitenancyUsername5 | MULTITENANCY_USERNAME | — | — |
| 167 | FDIntLinesLUpdatedByUserPEOObjectVersionNumber5 | OBJECT_VERSION_NUMBER | — | — |
| 168 | FDIntLinesLUpdatedByUserPEOPartyId5 | PARTY_ID | — | — |
| 169 | FDIntLinesLUpdatedByUserPEOPersonId5 | PERSON_ID | — | — |
| 170 | FDIntLinesLUpdatedByUserPEOStartDate5 | START_DATE | — | — |
| 171 | FDIntLinesLUpdatedByUserPEOSuspended5 | SUSPENDED | — | — |
| 172 | FDIntLinesLUpdatedByUserPEOUserDataChecksum5 | USER_DATA_CHECKSUM | — | — |
| 173 | FDIntLinesLUpdatedByUserPEOUserDistinguishedName5 | USER_DISTINGUISHED_NAME | — | — |
| 174 | FDIntLinesLUpdatedByUserPEOUserGuid5 | USER_GUID | — | — |
| 175 | FDIntLinesLUpdatedByUserPEOUserId5 | USER_ID | — | — |
| 176 | FDIntLinesLUpdatedByUserPEOUsername5 | USERNAME | — | — |
| 177 | FDIntRefCreatedByUserPEOActiveFlag6 | ACTIVE_FLAG | — | — |
| 178 | FDIntRefCreatedByUserPEOBusinessGroupId6 | BUSINESS_GROUP_ID | — | — |
| 179 | FDIntRefCreatedByUserPEOCreatedBy6 | CREATED_BY | — | — |
| 180 | FDIntRefCreatedByUserPEOCreationDate6 | CREATION_DATE | — | — |
| 181 | FDIntRefCreatedByUserPEOCredentialsEmailSent6 | CREDENTIALS_EMAIL_SENT | — | — |
| 182 | FDIntRefCreatedByUserPEOEndDate6 | END_DATE | — | — |
| 183 | FDIntRefCreatedByUserPEOExternalId6 | EXTERNAL_ID | — | — |
| 184 | FDIntRefCreatedByUserPEOHrTerminated6 | HR_TERMINATED | — | — |
| 185 | FDIntRefCreatedByUserPEOLastUpdateDate6 | LAST_UPDATE_DATE | — | — |
| 186 | FDIntRefCreatedByUserPEOLastUpdateLogin6 | LAST_UPDATE_LOGIN | — | — |
| 187 | FDIntRefCreatedByUserPEOLastUpdatedBy6 | LAST_UPDATED_BY | — | — |
| 188 | FDIntRefCreatedByUserPEOMultitenancyUsername6 | MULTITENANCY_USERNAME | — | — |
| 189 | FDIntRefCreatedByUserPEOObjectVersionNumber6 | OBJECT_VERSION_NUMBER | — | — |
| 190 | FDIntRefCreatedByUserPEOPartyId6 | PARTY_ID | — | — |
| 191 | FDIntRefCreatedByUserPEOPersonId6 | PERSON_ID | — | — |
| 192 | FDIntRefCreatedByUserPEOStartDate6 | START_DATE | — | — |
| 193 | FDIntRefCreatedByUserPEOSuspended6 | SUSPENDED | — | — |
| 194 | FDIntRefCreatedByUserPEOUserDataChecksum6 | USER_DATA_CHECKSUM | — | — |
| 195 | FDIntRefCreatedByUserPEOUserDistinguishedName6 | USER_DISTINGUISHED_NAME | — | — |
| 196 | FDIntRefCreatedByUserPEOUserGuid6 | USER_GUID | — | — |
| 197 | FDIntRefCreatedByUserPEOUserId6 | USER_ID | — | — |
| 198 | FDIntRefCreatedByUserPEOUsername6 | USERNAME | — | — |
| 199 | FDIntRefLUpdatedByUserPEOActiveFlag7 | ACTIVE_FLAG | — | — |
| 200 | FDIntRefLUpdatedByUserPEOBusinessGroupId7 | BUSINESS_GROUP_ID | — | — |
| 201 | FDIntRefLUpdatedByUserPEOCreatedBy7 | CREATED_BY | — | — |
| 202 | FDIntRefLUpdatedByUserPEOCreationDate7 | CREATION_DATE | — | — |
| 203 | FDIntRefLUpdatedByUserPEOCredentialsEmailSent7 | CREDENTIALS_EMAIL_SENT | — | — |
| 204 | FDIntRefLUpdatedByUserPEOEndDate7 | END_DATE | — | — |
| 205 | FDIntRefLUpdatedByUserPEOExternalId7 | EXTERNAL_ID | — | — |
| 206 | FDIntRefLUpdatedByUserPEOHrTerminated7 | HR_TERMINATED | — | — |
| 207 | FDIntRefLUpdatedByUserPEOLastUpdateDate7 | LAST_UPDATE_DATE | — | — |
| 208 | FDIntRefLUpdatedByUserPEOLastUpdateLogin7 | LAST_UPDATE_LOGIN | — | — |
| 209 | FDIntRefLUpdatedByUserPEOLastUpdatedBy7 | LAST_UPDATED_BY | — | — |
| 210 | FDIntRefLUpdatedByUserPEOMultitenancyUsername7 | MULTITENANCY_USERNAME | — | — |
| 211 | FDIntRefLUpdatedByUserPEOObjectVersionNumber7 | OBJECT_VERSION_NUMBER | — | — |
| 212 | FDIntRefLUpdatedByUserPEOPartyId7 | PARTY_ID | — | — |
| 213 | FDIntRefLUpdatedByUserPEOPersonId7 | PERSON_ID | — | — |
| 214 | FDIntRefLUpdatedByUserPEOStartDate7 | START_DATE | — | — |
| 215 | FDIntRefLUpdatedByUserPEOSuspended7 | SUSPENDED | — | — |
| 216 | FDIntRefLUpdatedByUserPEOUserDataChecksum7 | USER_DATA_CHECKSUM | — | — |
| 217 | FDIntRefLUpdatedByUserPEOUserDistinguishedName7 | USER_DISTINGUISHED_NAME | — | — |
| 218 | FDIntRefLUpdatedByUserPEOUserGuid7 | USER_GUID | — | — |
| 219 | FDIntRefLUpdatedByUserPEOUserId7 | USER_ID | — | — |
| 220 | FDIntRefLUpdatedByUserPEOUsername7 | USERNAME | — | — |
| 221 | FDLineIntrEOToCreatedByUserPActiveFlag2 | ACTIVE_FLAG | — | — |
| 222 | FDLineIntrEOToCreatedByUserPBusinessGroupId2 | BUSINESS_GROUP_ID | — | — |
| 223 | FDLineIntrEOToCreatedByUserPCreatedBy2 | CREATED_BY | — | — |
| 224 | FDLineIntrEOToCreatedByUserPCreationDate2 | CREATION_DATE | — | — |
| 225 | FDLineIntrEOToCreatedByUserPCredentialsEmailSent2 | CREDENTIALS_EMAIL_SENT | — | — |
| 226 | FDLineIntrEOToCreatedByUserPEndDate2 | END_DATE | — | — |
| 227 | FDLineIntrEOToCreatedByUserPExternalId2 | EXTERNAL_ID | — | — |
| 228 | FDLineIntrEOToCreatedByUserPHrTerminated2 | HR_TERMINATED | — | — |
| 229 | FDLineIntrEOToCreatedByUserPLastUpdateDate2 | LAST_UPDATE_DATE | — | — |
| 230 | FDLineIntrEOToCreatedByUserPLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 231 | FDLineIntrEOToCreatedByUserPLastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 232 | FDLineIntrEOToCreatedByUserPMultitenancyUsername2 | MULTITENANCY_USERNAME | — | — |
| 233 | FDLineIntrEOToCreatedByUserPObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 234 | FDLineIntrEOToCreatedByUserPPartyId2 | PARTY_ID | — | — |
| 235 | FDLineIntrEOToCreatedByUserPPersonId2 | PERSON_ID | — | — |
| 236 | FDLineIntrEOToCreatedByUserPStartDate2 | START_DATE | — | — |
| 237 | FDLineIntrEOToCreatedByUserPSuspended2 | SUSPENDED | — | — |
| 238 | FDLineIntrEOToCreatedByUserPUserDataChecksum2 | USER_DATA_CHECKSUM | — | — |
| 239 | FDLineIntrEOToCreatedByUserPUserDistinguishedName2 | USER_DISTINGUISHED_NAME | — | — |
| 240 | FDLineIntrEOToCreatedByUserPUserGuid2 | USER_GUID | — | — |
| 241 | FDLineIntrEOToCreatedByUserPUserId2 | USER_ID | — | — |
| 242 | FDLineIntrEOToCreatedByUserPUsername2 | USERNAME | — | — |
| 243 | FDLineIntrToLastUpdtdByUserPActiveFlag3 | ACTIVE_FLAG | — | — |
| 244 | FDLineIntrToLastUpdtdByUserPBusinessGroupId3 | BUSINESS_GROUP_ID | — | — |
| 245 | FDLineIntrToLastUpdtdByUserPCreatedBy3 | CREATED_BY | — | — |
| 246 | FDLineIntrToLastUpdtdByUserPCreationDate3 | CREATION_DATE | — | — |
| 247 | FDLineIntrToLastUpdtdByUserPCredentialsEmailSent3 | CREDENTIALS_EMAIL_SENT | — | — |
| 248 | FDLineIntrToLastUpdtdByUserPEndDate3 | END_DATE | — | — |
| 249 | FDLineIntrToLastUpdtdByUserPExternalId3 | EXTERNAL_ID | — | — |
| 250 | FDLineIntrToLastUpdtdByUserPHrTerminated3 | HR_TERMINATED | — | — |
| 251 | FDLineIntrToLastUpdtdByUserPLastUpdateDate3 | LAST_UPDATE_DATE | — | — |
| 252 | FDLineIntrToLastUpdtdByUserPLastUpdateLogin3 | LAST_UPDATE_LOGIN | — | — |
| 253 | FDLineIntrToLastUpdtdByUserPLastUpdatedBy3 | LAST_UPDATED_BY | — | — |
| 254 | FDLineIntrToLastUpdtdByUserPMultitenancyUsername3 | MULTITENANCY_USERNAME | — | — |
| 255 | FDLineIntrToLastUpdtdByUserPObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 256 | FDLineIntrToLastUpdtdByUserPPartyId3 | PARTY_ID | — | — |
| 257 | FDLineIntrToLastUpdtdByUserPPersonId3 | PERSON_ID | — | — |
| 258 | FDLineIntrToLastUpdtdByUserPStartDate3 | START_DATE | — | — |
| 259 | FDLineIntrToLastUpdtdByUserPSuspended3 | SUSPENDED | — | — |
| 260 | FDLineIntrToLastUpdtdByUserPUserDataChecksum3 | USER_DATA_CHECKSUM | — | — |
| 261 | FDLineIntrToLastUpdtdByUserPUserDistinguishedName3 | USER_DISTINGUISHED_NAME | — | — |
| 262 | FDLineIntrToLastUpdtdByUserPUserGuid3 | USER_GUID | — | — |
| 263 | FDLineIntrToLastUpdtdByUserPUserId3 | USER_ID | — | — |
| 264 | FDLineIntrToLastUpdtdByUserPUsername3 | USERNAME | — | — |
| 265 | TaxLineIntrEOCreatedByUserPEActiveFlag | ACTIVE_FLAG | — | — |
| 266 | TaxLineIntrEOCreatedByUserPEBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 267 | TaxLineIntrEOCreatedByUserPECreatedBy | CREATED_BY | — | — |
| 268 | TaxLineIntrEOCreatedByUserPECreationDate | CREATION_DATE | — | — |
| 269 | TaxLineIntrEOCreatedByUserPECredentialsEmailSent | CREDENTIALS_EMAIL_SENT | — | — |
| 270 | TaxLineIntrEOCreatedByUserPEEndDate | END_DATE | — | — |
| 271 | TaxLineIntrEOCreatedByUserPEExternalId | EXTERNAL_ID | — | — |
| 272 | TaxLineIntrEOCreatedByUserPEHrTerminated | HR_TERMINATED | — | — |
| 273 | TaxLineIntrEOCreatedByUserPELastUpdateDate | LAST_UPDATE_DATE | — | — |
| 274 | TaxLineIntrEOCreatedByUserPELastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 275 | TaxLineIntrEOCreatedByUserPELastUpdatedBy | LAST_UPDATED_BY | — | — |
| 276 | TaxLineIntrEOCreatedByUserPEMultitenancyUsername | MULTITENANCY_USERNAME | — | — |
| 277 | TaxLineIntrEOCreatedByUserPEObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 278 | TaxLineIntrEOCreatedByUserPEPartyId | PARTY_ID | — | — |
| 279 | TaxLineIntrEOCreatedByUserPEPersonId | PERSON_ID | — | — |
| 280 | TaxLineIntrEOCreatedByUserPEStartDate | START_DATE | — | — |
| 281 | TaxLineIntrEOCreatedByUserPESuspended | SUSPENDED | — | — |
| 282 | TaxLineIntrEOCreatedByUserPEUserDataChecksum | USER_DATA_CHECKSUM | — | — |
| 283 | TaxLineIntrEOCreatedByUserPEUserDistinguishedName | USER_DISTINGUISHED_NAME | — | — |
| 284 | TaxLineIntrEOCreatedByUserPEUserGuid | USER_GUID | — | — |
| 285 | TaxLineIntrEOCreatedByUserPEUserId | USER_ID | — | — |
| 286 | TaxLineIntrEOCreatedByUserPEUsername | USERNAME | — | — |
| 287 | TaxLineIntrEOLastUpdtdByUserActiveFlag1 | ACTIVE_FLAG | — | — |
| 288 | TaxLineIntrEOLastUpdtdByUserBusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 289 | TaxLineIntrEOLastUpdtdByUserCreatedBy1 | CREATED_BY | — | — |
| 290 | TaxLineIntrEOLastUpdtdByUserCreationDate1 | CREATION_DATE | — | — |
| 291 | TaxLineIntrEOLastUpdtdByUserCredentialsEmailSent1 | CREDENTIALS_EMAIL_SENT | — | — |
| 292 | TaxLineIntrEOLastUpdtdByUserEndDate1 | END_DATE | — | — |
| 293 | TaxLineIntrEOLastUpdtdByUserExternalId1 | EXTERNAL_ID | — | — |
| 294 | TaxLineIntrEOLastUpdtdByUserHrTerminated1 | HR_TERMINATED | — | — |
| 295 | TaxLineIntrEOLastUpdtdByUserLastUpdateDate1 | LAST_UPDATE_DATE | — | — |
| 296 | TaxLineIntrEOLastUpdtdByUserLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 297 | TaxLineIntrEOLastUpdtdByUserLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 298 | TaxLineIntrEOLastUpdtdByUserMultitenancyUsername1 | MULTITENANCY_USERNAME | — | — |
| 299 | TaxLineIntrEOLastUpdtdByUserObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 300 | TaxLineIntrEOLastUpdtdByUserPartyId1 | PARTY_ID | — | — |
| 301 | TaxLineIntrEOLastUpdtdByUserPersonId1 | PERSON_ID | — | — |
| 302 | TaxLineIntrEOLastUpdtdByUserStartDate1 | START_DATE | — | — |
| 303 | TaxLineIntrEOLastUpdtdByUserSuspended1 | SUSPENDED | — | — |
| 304 | TaxLineIntrEOLastUpdtdByUserUserDataChecksum1 | USER_DATA_CHECKSUM | — | — |
| 305 | TaxLineIntrEOLastUpdtdByUserUserDistinguishedName1 | USER_DISTINGUISHED_NAME | — | — |
| 306 | TaxLineIntrEOLastUpdtdByUserUserGuid1 | USER_GUID | — | — |
| 307 | TaxLineIntrEOLastUpdtdByUserUserId1 | USER_ID | — | — |
| 308 | TaxLineIntrEOLastUpdtdByUserUsername1 | USERNAME | — | — |

### [[zx_fc_intended_use_v|ZX_FC_INTENDED_USE_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LineIntendedUsePEOClassificationId | CLASSIFICATION_ID | — | — |
| 2 | LineIntendedUsePEOCode | CODE | — | — |
| 3 | LineIntendedUsePEOCountryCode | COUNTRY_CODE | — | — |
| 4 | LineIntendedUsePEOEffectiveFrom | EFFECTIVE_FROM | — | — |
| 5 | LineIntendedUsePEOEffectiveTo | EFFECTIVE_TO | — | — |
| 6 | LineIntendedUsePEOName | NAME | — | — |

### [[zx_fc_product_categories_v|ZX_FC_PRODUCT_CATEGORIES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProductCategoriesPEOClassificationCode | CLASSIFICATION_CODE | — | — |
| 2 | ProductCategoriesPEOClassificationId1 | CLASSIFICATION_ID | — | — |
| 3 | ProductCategoriesPEOClassificationName | CLASSIFICATION_NAME | — | — |
| 4 | ProductCategoriesPEOConcatLeafCode | CONCAT_LEAF_CODE | — | — |
| 5 | ProductCategoriesPEOConcatLeafName | CONCAT_LEAF_NAME | — | — |
| 6 | ProductCategoriesPEOCountryCode1 | COUNTRY_CODE | — | — |
| 7 | ProductCategoriesPEOEffectiveFrom1 | EFFECTIVE_FROM | — | — |
| 8 | ProductCategoriesPEOEffectiveTo1 | EFFECTIVE_TO | — | — |

### [[zx_fc_product_fiscal_v|ZX_FC_PRODUCT_FISCAL_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProductFiscClassificationsPE1CategoryId | CATEGORY_ID | — | — |
| 2 | ProductFiscClassificationsPE1CategorySetId | CATEGORY_SET_ID | — | — |
| 3 | ProductFiscClassificationsPE1ClassificationCode1 | CLASSIFICATION_CODE | — | — |
| 4 | ProductFiscClassificationsPE1ClassificationName1 | CLASSIFICATION_NAME | — | — |
| 5 | ProductFiscClassificationsPE1CountryCode2 | COUNTRY_CODE | — | — |
| 6 | ProductFiscClassificationsPE1EffectiveTo2 | EFFECTIVE_TO | — | — |
| 7 | ProductFiscClassificationsPE1StructureId | STRUCTURE_ID | — | — |
| 8 | ProductFiscClassificationsPE1StructureName | STRUCTURE_NAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
