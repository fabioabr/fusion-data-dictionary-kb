---
id: DOC-OTHER-PVO-InterfaceFiscalDocumentP1
doc_type: system-doc
title: "InterfaceFiscalDocumentP1 — PVO Cross-Module"
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
  - InterfaceFiscalDocumentP1
  - interfacefiscaldocumentp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InterfaceFiscalDocumentP1

## 📌 Visão Geral

View Object para extração BICC de dados de Interface Fiscal Document P1. Acessa as tabelas: CMF_FD_CHARGES_INT, CMF_FD_CHARGE_ASSOCS_INT, CMF_FD_HEADERS_INT (+23).

**Caminho:** `FscmTopModelAM.FiscalDocumentInterfaceAM.InterfaceFiscalDocumentP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 1388 | 26 | 1 | 75 | 5% |

---

## 🔗 Tabelas Relacionadas

- [[cmf_fd_charges_int|CMF_FD_CHARGES_INT]] — 24 atributos
- [[cmf_fd_charge_assocs_int|CMF_FD_CHARGE_ASSOCS_INT]] — 20 atributos
- [[cmf_fd_headers_int|CMF_FD_HEADERS_INT]] — 100 atributos (1 PKs, 25 BICC)
- [[cmf_fd_inv_org_int_otbi_v|CMF_FD_INV_ORG_INT_OTBI_V]] — 5 atributos
- [[cmf_fd_in_convert_cfops_v|CMF_FD_IN_CONVERT_CFOPS_V]] — 2 atributos (1 BICC)
- [[cmf_fd_legal_procs_int|CMF_FD_LEGAL_PROCS_INT]] — 18 atributos (5 BICC)
- [[cmf_fd_lines_int|CMF_FD_LINES_INT]] — 49 atributos (20 BICC)
- [[cmf_fd_loc_info_int_otbi_v|CMF_FD_LOC_INFO_INT_OTBI_V]] — 80 atributos
- [[cmf_fd_out_origin_cfops_v|CMF_FD_OUT_ORIGIN_CFOPS_V]] — 2 atributos (1 BICC)
- [[cmf_fd_references_int|CMF_FD_REFERENCES_INT]] — 26 atributos (11 BICC)
- [[cmf_fiscal_doc_assoctns_vl|CMF_FISCAL_DOC_ASSOCTNS_VL]] — 16 atributos
- [[cmf_fiscal_operation_types|CMF_FISCAL_OPERATION_TYPES]] — 14 atributos
- [[cmf_fiscal_proc_options|CMF_FISCAL_PROC_OPTIONS]] — 54 atributos
- [[cmf_fiscal_ref_options|CMF_FISCAL_REF_OPTIONS]] — 19 atributos
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 21 atributos
- [[inv_units_of_measure_vl|INV_UNITS_OF_MEASURE_VL]] — 20 atributos (1 BICC)
- [[jg_fscl_hdrs_atrb_int|JG_FSCL_HDRS_ATRB_INT]] — 69 atributos
- [[jg_fscl_hdr_dtls_atrb_int|JG_FSCL_HDR_DTLS_ATRB_INT]] — 23 atributos
- [[jg_fscl_lines_atrb_int|JG_FSCL_LINES_ATRB_INT]] — 48 atributos
- [[jg_fscl_ln_dtls_atrb_int|JG_FSCL_LN_DTLS_ATRB_INT]] — 31 atributos
- [[jg_fscl_tax_lines_int|JG_FSCL_TAX_LINES_INT]] — 40 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 377 atributos (8 BICC)
- [[per_users|PER_USERS]] — 308 atributos
- [[zx_fc_intended_use_v|ZX_FC_INTENDED_USE_V]] — 6 atributos (1 BICC)
- [[zx_fc_product_categories_v|ZX_FC_PRODUCT_CATEGORIES_V]] — 8 atributos (1 BICC)
- [[zx_fc_product_fiscal_v|ZX_FC_PRODUCT_FISCAL_V]] — 8 atributos (1 BICC)

---

## ⚙️ Atributos

### [[cmf_fd_charges_int|CMF_FD_CHARGES_INT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FDInterfaceChargesPEOAllocationBasis | ALLOCATION_BASIS | — | — |
| 2 | FDInterfaceChargesPEOAllocationUom | ALLOCATION_UOM | — | — |
| 3 | FDInterfaceChargesPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 4 | FDInterfaceChargesPEOBasis | BASIS | — | — |
| 5 | FDInterfaceChargesPEOChargeAmount | CHARGE_AMOUNT | — | — |
| 6 | FDInterfaceChargesPEOChargeCode | CHARGE_CODE | — | — |
| 7 | FDInterfaceChargesPEOChargeId | CHARGE_ID | — | — |
| 8 | FDInterfaceChargesPEOChargeLineId | CHARGE_LINE_ID | — | — |
| 9 | FDInterfaceChargesPEOChargeLineStatus | CHARGE_LINE_STATUS | — | — |
| 10 | FDInterfaceChargesPEOCreatedBy2 | CREATED_BY | — | — |
| 11 | FDInterfaceChargesPEOCreationDate2 | CREATION_DATE | — | — |
| 12 | FDInterfaceChargesPEODocumentHeaderId3 | DOCUMENT_HEADER_ID | — | — |
| 13 | FDInterfaceChargesPEOExternalSystemRefId2 | EXTERNAL_SYSTEM_REF_ID | — | — |
| 14 | FDInterfaceChargesPEOExternalSystemReference2 | EXTERNAL_SYSTEM_REFERENCE | — | — |
| 15 | FDInterfaceChargesPEOJobDefinitionName2 | JOB_DEFINITION_NAME | — | — |
| 16 | FDInterfaceChargesPEOJobDefinitionPackage2 | JOB_DEFINITION_PACKAGE | — | — |
| 17 | FDInterfaceChargesPEOLandedCostCharge | LANDED_COST_CHARGE | — | — |
| 18 | FDInterfaceChargesPEOLastUpdateDate2 | LAST_UPDATE_DATE | — | — |
| 19 | FDInterfaceChargesPEOLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 20 | FDInterfaceChargesPEOLastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 21 | FDInterfaceChargesPEOLineNumber1 | LINE_NUMBER | — | — |
| 22 | FDInterfaceChargesPEOObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 23 | FDInterfaceChargesPEOPercentage | PERCENTAGE | — | — |
| 24 | FDInterfaceChargesPEORequestId2 | REQUEST_ID | — | — |

### [[cmf_fd_charge_assocs_int|CMF_FD_CHARGE_ASSOCS_INT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FDIntChargeAssocPEOAllocatedAmount | ALLOCATED_AMOUNT | — | — |
| 2 | FDIntChargeAssocPEOAllocationBaseValue | ALLOCATION_BASE_VALUE | — | — |
| 3 | FDIntChargeAssocPEOAllocationPercentage | ALLOCATION_PERCENTAGE | — | — |
| 4 | FDIntChargeAssocPEOAttributeCategory1 | ATTRIBUTE_CATEGORY | — | — |
| 5 | FDIntChargeAssocPEOChargeAssociationId | CHARGE_ASSOCIATION_ID | — | — |
| 6 | FDIntChargeAssocPEOChargeLineId1 | CHARGE_LINE_ID | — | — |
| 7 | FDIntChargeAssocPEOCreatedBy3 | CREATED_BY | — | — |
| 8 | FDIntChargeAssocPEOCreationDate3 | CREATION_DATE | — | — |
| 9 | FDIntChargeAssocPEODocumentLineId1 | DOCUMENT_LINE_ID | — | — |
| 10 | FDIntChargeAssocPEOExternalSystemRefId3 | EXTERNAL_SYSTEM_REF_ID | — | — |
| 11 | FDIntChargeAssocPEOExternalSystemReference3 | EXTERNAL_SYSTEM_REFERENCE | — | — |
| 12 | FDIntChargeAssocPEOJobDefinitionName3 | JOB_DEFINITION_NAME | — | — |
| 13 | FDIntChargeAssocPEOJobDefinitionPackage3 | JOB_DEFINITION_PACKAGE | — | — |
| 14 | FDIntChargeAssocPEOLastUpdateDate3 | LAST_UPDATE_DATE | — | — |
| 15 | FDIntChargeAssocPEOLastUpdateLogin3 | LAST_UPDATE_LOGIN | — | — |
| 16 | FDIntChargeAssocPEOLastUpdatedBy3 | LAST_UPDATED_BY | — | — |
| 17 | FDIntChargeAssocPEOObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 18 | FDIntChargeAssocPEORefDocumentHeaderId1 | REF_DOCUMENT_HEADER_ID | — | — |
| 19 | FDIntChargeAssocPEORequestId3 | REQUEST_ID | — | — |
| 20 | FDIntChargeAssocPEOVariablePercentage | VARIABLE_PERCENTAGE | — | — |

### [[cmf_fd_headers_int|CMF_FD_HEADERS_INT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FDInterfaceHeadersPEOAccessKeyNumber | ACCESS_KEY_NUMBER | — | ✅ |
| 2 | FDInterfaceHeadersPEOAcknowledgedDate | ACKNOWLEDGED_DATE | — | ✅ |
| 3 | FDInterfaceHeadersPEOApprovedStatus | APPROVED_STATUS | — | — |
| 4 | FDInterfaceHeadersPEOBillToBuId | BILL_TO_BU_ID | — | — |
| 5 | FDInterfaceHeadersPEOChargeAllocationStatus | CHARGE_ALLOCATION_STATUS | — | — |
| 6 | FDInterfaceHeadersPEOCountryCode | COUNTRY_CODE | — | ✅ |
| 7 | FDInterfaceHeadersPEOCreatedBy | CREATED_BY | — | — |
| 8 | FDInterfaceHeadersPEOCreationDate | CREATION_DATE | — | ✅ |
| 9 | FDInterfaceHeadersPEOCurrency | CURRENCY | — | ✅ |
| 10 | FDInterfaceHeadersPEODiscountAmount | DISCOUNT_AMOUNT | — | ✅ |
| 11 | FDInterfaceHeadersPEODocumentHeaderId | DOCUMENT_HEADER_ID | — | ✅ |
| 12 | FDInterfaceHeadersPEODocumentNumber | DOCUMENT_NUMBER | — | ✅ |
| 13 | FDInterfaceHeadersPEODocumentStatus | DOCUMENT_STATUS | — | ✅ |
| 14 | FDInterfaceHeadersPEODocumentType | DOCUMENT_TYPE | — | ✅ |
| 15 | FDInterfaceHeadersPEOExternalSystemRefId | EXTERNAL_SYSTEM_REF_ID | — | — |
| 16 | FDInterfaceHeadersPEOExternalSystemReference | EXTERNAL_SYSTEM_REFERENCE | — | — |
| 17 | FDInterfaceHeadersPEOFiscalDocAssoctnsId | FISCAL_DOC_ASSOCTNS_ID | — | — |
| 18 | FDInterfaceHeadersPEOFiscalProcOptionsId | FISCAL_PROC_OPTIONS_ID | — | — |
| 19 | FDInterfaceHeadersPEOFreightAmount | FREIGHT_AMOUNT | — | ✅ |
| 20 | FDInterfaceHeadersPEOImportingStatus | IMPORTING_STATUS | — | — |
| 21 | FDInterfaceHeadersPEOInsuranceAmount | INSURANCE_AMOUNT | — | ✅ |
| 22 | FDInterfaceHeadersPEOIssueDate | ISSUE_DATE | — | ✅ |
| 23 | FDInterfaceHeadersPEOIssuerAddress | ISSUER_ADDRESS | — | — |
| 24 | FDInterfaceHeadersPEOIssuerAddressCityCode | ISSUER_ADDRESS_CITY_CODE | — | — |
| 25 | FDInterfaceHeadersPEOIssuerAddressCityName | ISSUER_ADDRESS_CITY_NAME | — | — |
| 26 | FDInterfaceHeadersPEOIssuerAddressComplement | ISSUER_ADDRESS_COMPLEMENT | — | — |
| 27 | FDInterfaceHeadersPEOIssuerAddressNumber | ISSUER_ADDRESS_NUMBER | — | — |
| 28 | FDInterfaceHeadersPEOIssuerAddressState | ISSUER_ADDRESS_STATE | — | — |
| 29 | FDInterfaceHeadersPEOIssuerAddressZipCode | ISSUER_ADDRESS_ZIP_CODE | — | — |
| 30 | FDInterfaceHeadersPEOIssuerLocationId | ISSUER_LOCATION_ID | — | — |
| 31 | FDInterfaceHeadersPEOIssuerName | ISSUER_NAME | — | — |
| 32 | FDInterfaceHeadersPEOIssuerPartyId | ISSUER_PARTY_ID | — | — |
| 33 | FDInterfaceHeadersPEOIssuerPartySiteId | ISSUER_PARTY_SITE_ID | — | — |
| 34 | FDInterfaceHeadersPEOIssuerPartyType | ISSUER_PARTY_TYPE | — | — |
| 35 | FDInterfaceHeadersPEOIssuerTaxId | ISSUER_TAX_ID | — | — |
| 36 | FDInterfaceHeadersPEOIssuerTaxpayerId | ISSUER_TAXPAYER_ID | — | — |
| 37 | FDInterfaceHeadersPEOIssuingPurpose | ISSUING_PURPOSE | — | ✅ |
| 38 | FDInterfaceHeadersPEOItemLineTotal | ITEM_LINE_TOTAL | — | ✅ |
| 39 | FDInterfaceHeadersPEOJgStatus | JG_STATUS | — | — |
| 40 | FDInterfaceHeadersPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 41 | FDInterfaceHeadersPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 42 | FDInterfaceHeadersPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 43 | FDInterfaceHeadersPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 44 | FDInterfaceHeadersPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 45 | FDInterfaceHeadersPEOModel | MODEL | — | ✅ |
| 46 | FDInterfaceHeadersPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 47 | FDInterfaceHeadersPEOOperationType | OPERATION_TYPE | — | ✅ |
| 48 | FDInterfaceHeadersPEOOtherExpensesAmount | OTHER_EXPENSES_AMOUNT | — | ✅ |
| 49 | FDInterfaceHeadersPEOReceiverAddress | RECEIVER_ADDRESS | — | — |
| 50 | FDInterfaceHeadersPEOReceiverAddressCityCode | RECEIVER_ADDRESS_CITY_CODE | — | — |
| 51 | FDInterfaceHeadersPEOReceiverAddressCityName | RECEIVER_ADDRESS_CITY_NAME | — | — |
| 52 | FDInterfaceHeadersPEOReceiverAddressComplement | RECEIVER_ADDRESS_COMPLEMENT | — | — |
| 53 | FDInterfaceHeadersPEOReceiverAddressNumber | RECEIVER_ADDRESS_NUMBER | — | — |
| 54 | FDInterfaceHeadersPEOReceiverAddressState | RECEIVER_ADDRESS_STATE | — | — |
| 55 | FDInterfaceHeadersPEOReceiverAddressZipCode | RECEIVER_ADDRESS_ZIP_CODE | — | — |
| 56 | FDInterfaceHeadersPEOReceiverLocationId | RECEIVER_LOCATION_ID | — | — |
| 57 | FDInterfaceHeadersPEOReceiverName | RECEIVER_NAME | — | — |
| 58 | FDInterfaceHeadersPEOReceiverPartyId | RECEIVER_PARTY_ID | — | — |
| 59 | FDInterfaceHeadersPEOReceiverPartySiteId | RECEIVER_PARTY_SITE_ID | — | — |
| 60 | FDInterfaceHeadersPEOReceiverPartyType | RECEIVER_PARTY_TYPE | — | — |
| 61 | FDInterfaceHeadersPEOReceiverTaxId | RECEIVER_TAX_ID | — | — |
| 62 | FDInterfaceHeadersPEOReceiverTaxpayerId | RECEIVER_TAXPAYER_ID | — | — |
| 63 | FDInterfaceHeadersPEOReferencedStatus | REFERENCED_STATUS | — | — |
| 64 | FDInterfaceHeadersPEORequestId | REQUEST_ID | — | — |
| 65 | FDInterfaceHeadersPEOSeries | SERIES | — | ✅ |
| 66 | FDInterfaceHeadersPEOShipFromAddrComplement | SHIP_FROM_ADDR_COMPLEMENT | — | — |
| 67 | FDInterfaceHeadersPEOShipFromAddress | SHIP_FROM_ADDRESS | — | — |
| 68 | FDInterfaceHeadersPEOShipFromAddressCityCode | SHIP_FROM_ADDRESS_CITY_CODE | — | — |
| 69 | FDInterfaceHeadersPEOShipFromAddressCityName | SHIP_FROM_ADDRESS_CITY_NAME | — | — |
| 70 | FDInterfaceHeadersPEOShipFromAddressNumber | SHIP_FROM_ADDRESS_NUMBER | — | — |
| 71 | FDInterfaceHeadersPEOShipFromAddressState | SHIP_FROM_ADDRESS_STATE | — | — |
| 72 | FDInterfaceHeadersPEOShipFromAddressZipCode | SHIP_FROM_ADDRESS_ZIP_CODE | — | — |
| 73 | FDInterfaceHeadersPEOShipFromPartyType | SHIP_FROM_PARTY_TYPE | — | — |
| 74 | FDInterfaceHeadersPEOShipToAddress | SHIP_TO_ADDRESS | — | — |
| 75 | FDInterfaceHeadersPEOShipToAddressCityCode | SHIP_TO_ADDRESS_CITY_CODE | — | — |
| 76 | FDInterfaceHeadersPEOShipToAddressCityName | SHIP_TO_ADDRESS_CITY_NAME | — | — |
| 77 | FDInterfaceHeadersPEOShipToAddressComplement | SHIP_TO_ADDRESS_COMPLEMENT | — | — |
| 78 | FDInterfaceHeadersPEOShipToAddressNumber | SHIP_TO_ADDRESS_NUMBER | — | — |
| 79 | FDInterfaceHeadersPEOShipToAddressState | SHIP_TO_ADDRESS_STATE | — | — |
| 80 | FDInterfaceHeadersPEOShipToAddressZipCode | SHIP_TO_ADDRESS_ZIP_CODE | — | — |
| 81 | FDInterfaceHeadersPEOShipfromLocationId | SHIPFROM_LOCATION_ID | — | — |
| 82 | FDInterfaceHeadersPEOShipfromPartyId | SHIPFROM_PARTY_ID | — | — |
| 83 | FDInterfaceHeadersPEOShipfromPartySiteId | SHIPFROM_PARTY_SITE_ID | — | — |
| 84 | FDInterfaceHeadersPEOShipfromTaxId | SHIPFROM_TAX_ID | — | — |
| 85 | FDInterfaceHeadersPEOShipfromTaxpayerId | SHIPFROM_TAXPAYER_ID | — | — |
| 86 | FDInterfaceHeadersPEOShiptoLocationId | SHIPTO_LOCATION_ID | — | — |
| 87 | FDInterfaceHeadersPEOShiptoPartyId | SHIPTO_PARTY_ID | — | — |
| 88 | FDInterfaceHeadersPEOShiptoPartySiteId | SHIPTO_PARTY_SITE_ID | — | — |
| 89 | FDInterfaceHeadersPEOShiptoTaxId | SHIPTO_TAX_ID | — | — |
| 90 | FDInterfaceHeadersPEOShiptoTaxpayerId | SHIPTO_TAXPAYER_ID | — | — |
| 91 | FDInterfaceHeadersPEOSoldToLeId | SOLD_TO_LE_ID | — | — |
| 92 | FDInterfaceHeadersPEOSourceDocCurrencyCode | SOURCE_DOC_CURRENCY_CODE | — | ✅ |
| 93 | FDInterfaceHeadersPEOSourceDocumentType | SOURCE_DOCUMENT_TYPE | — | ✅ |
| 94 | FDInterfaceHeadersPEOSubseries | SUBSERIES | — | ✅ |
| 95 | FDInterfaceHeadersPEOTaxCalculationStatus | TAX_CALCULATION_STATUS | — | — |
| 96 | FDInterfaceHeadersPEOTotalAmount | TOTAL_AMOUNT | — | ✅ |
| 97 | FDInterfaceHeadersPEOUsageAuthorization | USAGE_AUTHORIZATION | — | — |
| 98 | FDInterfaceHeadersPEOValidationStatus | VALIDATION_STATUS | — | — |
| 99 | FDInterfaceHeadersPEOZxStatus | ZX_STATUS | — | — |
| 100 | FdHeadersIntId | FD_HEADERS_INT_ID | 🔑 | ✅ |

### [[cmf_fd_inv_org_int_otbi_v|CMF_FD_INV_ORG_INT_OTBI_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FDInterfaceInvOrgPEODestInventoryOrgId | DEST_INVENTORY_ORG_ID | — | — |
| 2 | FDInterfaceInvOrgPEOFdHeadersIntId5 | FD_HEADERS_INT_ID | — | — |
| 3 | FDInterfaceInvOrgPEOFdLinesIntId1 | FD_LINES_INT_ID | — | — |
| 4 | FDInterfaceInvOrgPEOSourceDocumentType2 | SOURCE_DOCUMENT_TYPE | — | — |
| 5 | FDInterfaceInvOrgPEOSrcInventoryOrgId | SRC_INVENTORY_ORG_ID | — | — |

### [[cmf_fd_in_convert_cfops_v|CMF_FD_IN_CONVERT_CFOPS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocInBoundCFOPPEOClassificationCode2 | CLASSIFICATION_CODE | — | — |
| 2 | FiscalDocInBoundCFOPPEOClassificationName2 | CLASSIFICATION_NAME | — | ✅ |

### [[cmf_fd_legal_procs_int|CMF_FD_LEGAL_PROCS_INT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FDInterfaceLegalprocessPEOCreatedBy5 | CREATED_BY | — | — |
| 2 | FDInterfaceLegalprocessPEOCreationDate5 | CREATION_DATE | — | ✅ |
| 3 | FDInterfaceLegalprocessPEODocumentHeaderId5 | DOCUMENT_HEADER_ID | — | — |
| 4 | FDInterfaceLegalprocessPEODocumentLegalDocAssocId | DOCUMENT_LEGAL_DOC_ASSOC_ID | — | — |
| 5 | FDInterfaceLegalprocessPEOExternalSystemRefId5 | EXTERNAL_SYSTEM_REF_ID | — | — |
| 6 | FDInterfaceLegalprocessPEOExternalSystemReference5 | EXTERNAL_SYSTEM_REFERENCE | — | — |
| 7 | FDInterfaceLegalprocessPEOFdHeadersIntId4 | FD_HEADERS_INT_ID | — | — |
| 8 | FDInterfaceLegalprocessPEOFdLegalProcsIntId | FD_LEGAL_PROCS_INT_ID | — | — |
| 9 | FDInterfaceLegalprocessPEOJobDefinitionName5 | JOB_DEFINITION_NAME | — | — |
| 10 | FDInterfaceLegalprocessPEOJobDefinitionPackage5 | JOB_DEFINITION_PACKAGE | — | — |
| 11 | FDInterfaceLegalprocessPEOLastUpdateDate5 | LAST_UPDATE_DATE | — | ✅ |
| 12 | FDInterfaceLegalprocessPEOLastUpdateLogin5 | LAST_UPDATE_LOGIN | — | — |
| 13 | FDInterfaceLegalprocessPEOLastUpdatedBy5 | LAST_UPDATED_BY | — | — |
| 14 | FDInterfaceLegalprocessPEOLegalProcActIdentifier | LEGAL_PROC_ACT_IDENTIFIER | — | ✅ |
| 15 | FDInterfaceLegalprocessPEOLegalProcProceedingOrig | LEGAL_PROC_PROCEEDING_ORIG | — | ✅ |
| 16 | FDInterfaceLegalprocessPEOObjectVersionNumber5 | OBJECT_VERSION_NUMBER | — | — |
| 17 | FDInterfaceLegalprocessPEORequestId5 | REQUEST_ID | — | — |
| 18 | FDInterfaceLegalprocessPEOValidationStatus3 | VALIDATION_STATUS | — | ✅ |

### [[cmf_fd_lines_int|CMF_FD_LINES_INT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FDInterfaceLinesPEOCfop | CFOP | — | — |
| 2 | FDInterfaceLinesPEOChargesAmount | CHARGES_AMOUNT | — | ✅ |
| 3 | FDInterfaceLinesPEOCreatedBy1 | CREATED_BY | — | — |
| 4 | FDInterfaceLinesPEOCreationDate1 | CREATION_DATE | — | ✅ |
| 5 | FDInterfaceLinesPEODiscountLineAmount | DISCOUNT_LINE_AMOUNT | — | ✅ |
| 6 | FDInterfaceLinesPEODocumentHeaderId2 | DOCUMENT_HEADER_ID | — | — |
| 7 | FDInterfaceLinesPEODocumentLineId | DOCUMENT_LINE_ID | — | — |
| 8 | FDInterfaceLinesPEOExternalSystemRefId1 | EXTERNAL_SYSTEM_REF_ID | — | — |
| 9 | FDInterfaceLinesPEOExternalSystemReference1 | EXTERNAL_SYSTEM_REFERENCE | — | — |
| 10 | FDInterfaceLinesPEOFdConvertedCfop | FD_CONVERTED_CFOP | — | — |
| 11 | FDInterfaceLinesPEOFdHeadersIntId2 | FD_HEADERS_INT_ID | — | — |
| 12 | FDInterfaceLinesPEOFdLinesIntId | FD_LINES_INT_ID | — | — |
| 13 | FDInterfaceLinesPEOFiscalClassification | FISCAL_CLASSIFICATION | — | — |
| 14 | FDInterfaceLinesPEOFreightLineAmount | FREIGHT_LINE_AMOUNT | — | ✅ |
| 15 | FDInterfaceLinesPEOFreightModal | FREIGHT_MODAL | — | ✅ |
| 16 | FDInterfaceLinesPEOInsuranceLineAmount | INSURANCE_LINE_AMOUNT | — | ✅ |
| 17 | FDInterfaceLinesPEOIntendedUse | INTENDED_USE | — | — |
| 18 | FDInterfaceLinesPEOItemCode | ITEM_CODE | — | ✅ |
| 19 | FDInterfaceLinesPEOItemDescription | ITEM_DESCRIPTION | — | ✅ |
| 20 | FDInterfaceLinesPEOItemId | ITEM_ID | — | — |
| 21 | FDInterfaceLinesPEOJobDefinitionName1 | JOB_DEFINITION_NAME | — | — |
| 22 | FDInterfaceLinesPEOJobDefinitionPackage1 | JOB_DEFINITION_PACKAGE | — | — |
| 23 | FDInterfaceLinesPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 24 | FDInterfaceLinesPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 25 | FDInterfaceLinesPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 26 | FDInterfaceLinesPEOLineAmount | LINE_AMOUNT | — | ✅ |
| 27 | FDInterfaceLinesPEOLineNumber | LINE_NUMBER | — | ✅ |
| 28 | FDInterfaceLinesPEOLineType | LINE_TYPE | — | ✅ |
| 29 | FDInterfaceLinesPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 30 | FDInterfaceLinesPEOOtherExpensesLineAmount | OTHER_EXPENSES_LINE_AMOUNT | — | ✅ |
| 31 | FDInterfaceLinesPEOProductCategory | PRODUCT_CATEGORY | — | — |
| 32 | FDInterfaceLinesPEOProductFiscalClassifId | PRODUCT_FISCAL_CLASSIF_ID | — | — |
| 33 | FDInterfaceLinesPEOQuantity | QUANTITY | — | ✅ |
| 34 | FDInterfaceLinesPEORefDocumentHeaderId | REF_DOCUMENT_HEADER_ID | — | — |
| 35 | FDInterfaceLinesPEORefDocumentLineId | REF_DOCUMENT_LINE_ID | — | — |
| 36 | FDInterfaceLinesPEORefFdDocumentType | REF_FD_DOCUMENT_TYPE | — | — |
| 37 | FDInterfaceLinesPEOReqBuId | REQ_BU_ID | — | — |
| 38 | FDInterfaceLinesPEORequestId1 | REQUEST_ID | — | — |
| 39 | FDInterfaceLinesPEOSourceCurrencyCode | SOURCE_CURRENCY_CODE | — | ✅ |
| 40 | FDInterfaceLinesPEOSourceDocBuId | SOURCE_DOC_BU_ID | — | — |
| 41 | FDInterfaceLinesPEOSourceDocHeaderId | SOURCE_DOC_HEADER_ID | — | — |
| 42 | FDInterfaceLinesPEOSourceDocLineId | SOURCE_DOC_LINE_ID | — | — |
| 43 | FDInterfaceLinesPEOSourceDocScheduleId | SOURCE_DOC_SCHEDULE_ID | — | — |
| 44 | FDInterfaceLinesPEOSourceDocumentLine | SOURCE_DOCUMENT_LINE | — | ✅ |
| 45 | FDInterfaceLinesPEOSourceDocumentNumber | SOURCE_DOCUMENT_NUMBER | — | ✅ |
| 46 | FDInterfaceLinesPEOSourceDocumentType1 | SOURCE_DOCUMENT_TYPE | — | ✅ |
| 47 | FDInterfaceLinesPEOUnitOfMeasure | UNIT_OF_MEASURE | — | — |
| 48 | FDInterfaceLinesPEOUnitPrice | UNIT_PRICE | — | ✅ |
| 49 | FDInterfaceLinesPEOValidationStatus1 | VALIDATION_STATUS | — | ✅ |

### [[cmf_fd_loc_info_int_otbi_v|CMF_FD_LOC_INFO_INT_OTBI_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FDInterfaceLocInfoPEODocumentHeaderId1 | DOCUMENT_HEADER_ID | — | — |
| 2 | FDInterfaceLocInfoPEODocumentNumber1 | DOCUMENT_NUMBER | — | — |
| 3 | FDInterfaceLocInfoPEOFdHeadersIntId1 | FD_HEADERS_INT_ID | — | — |
| 4 | FDInterfaceLocInfoPEOFiscalProcOptionsId1 | FISCAL_PROC_OPTIONS_ID | — | — |
| 5 | FDInterfaceLocInfoPEOIssuerCustomerFormTaxNum | ISSUER_CUSTOMER_FORM_TAX_NUM | — | — |
| 6 | FDInterfaceLocInfoPEOIssuerCustomerLocationId | ISSUER_CUSTOMER_LOCATION_ID | — | — |
| 7 | FDInterfaceLocInfoPEOIssuerCustomerPartyId | ISSUER_CUSTOMER_PARTY_ID | — | — |
| 8 | FDInterfaceLocInfoPEOIssuerCustomerPartySiteId | ISSUER_CUSTOMER_PARTY_SITE_ID | — | — |
| 9 | FDInterfaceLocInfoPEOIssuerCustomerTaxId | ISSUER_CUSTOMER_TAX_ID | — | — |
| 10 | FDInterfaceLocInfoPEOIssuerCustomerTaxpayerId | ISSUER_CUSTOMER_TAXPAYER_ID | — | — |
| 11 | FDInterfaceLocInfoPEOIssuerLeFormTaxNumber | ISSUER_LE_FORM_TAX_NUMBER | — | — |
| 12 | FDInterfaceLocInfoPEOIssuerLeId | ISSUER_LE_ID | — | — |
| 13 | FDInterfaceLocInfoPEOIssuerLeLocationId | ISSUER_LE_LOCATION_ID | — | — |
| 14 | FDInterfaceLocInfoPEOIssuerLeSiteId | ISSUER_LE_SITE_ID | — | — |
| 15 | FDInterfaceLocInfoPEOIssuerLeTaxId | ISSUER_LE_TAX_ID | — | — |
| 16 | FDInterfaceLocInfoPEOIssuerLeTaxpayerId | ISSUER_LE_TAXPAYER_ID | — | — |
| 17 | FDInterfaceLocInfoPEOIssuerSupplierFormTaxNum | ISSUER_SUPPLIER_FORM_TAX_NUM | — | — |
| 18 | FDInterfaceLocInfoPEOIssuerSupplierLocationId | ISSUER_SUPPLIER_LOCATION_ID | — | — |
| 19 | FDInterfaceLocInfoPEOIssuerSupplierPartyId | ISSUER_SUPPLIER_PARTY_ID | — | — |
| 20 | FDInterfaceLocInfoPEOIssuerSupplierPartySiteId | ISSUER_SUPPLIER_PARTY_SITE_ID | — | — |
| 21 | FDInterfaceLocInfoPEOIssuerSupplierTaxId | ISSUER_SUPPLIER_TAX_ID | — | — |
| 22 | FDInterfaceLocInfoPEOIssuerSupplierTaxpayerId | ISSUER_SUPPLIER_TAXPAYER_ID | — | — |
| 23 | FDInterfaceLocInfoPEOIssuerType | ISSUER_TYPE | — | — |
| 24 | FDInterfaceLocInfoPEOReceiverCustPartySiteId | RECEIVER_CUST_PARTY_SITE_ID | — | — |
| 25 | FDInterfaceLocInfoPEOReceiverCustomerFormTaxNum | RECEIVER_CUSTOMER_FORM_TAX_NUM | — | — |
| 26 | FDInterfaceLocInfoPEOReceiverCustomerLocationId | RECEIVER_CUSTOMER_LOCATION_ID | — | — |
| 27 | FDInterfaceLocInfoPEOReceiverCustomerPartyId | RECEIVER_CUSTOMER_PARTY_ID | — | — |
| 28 | FDInterfaceLocInfoPEOReceiverCustomerTaxId | RECEIVER_CUSTOMER_TAX_ID | — | — |
| 29 | FDInterfaceLocInfoPEOReceiverCustomerTaxpayerId | RECEIVER_CUSTOMER_TAXPAYER_ID | — | — |
| 30 | FDInterfaceLocInfoPEOReceiverLeFormTaxNumber | RECEIVER_LE_FORM_TAX_NUMBER | — | — |
| 31 | FDInterfaceLocInfoPEOReceiverLeLocationId | RECEIVER_LE_LOCATION_ID | — | — |
| 32 | FDInterfaceLocInfoPEOReceiverLePartyId | RECEIVER_LE_PARTY_ID | — | — |
| 33 | FDInterfaceLocInfoPEOReceiverLePartySiteId | RECEIVER_LE_PARTY_SITE_ID | — | — |
| 34 | FDInterfaceLocInfoPEOReceiverLeTaxId | RECEIVER_LE_TAX_ID | — | — |
| 35 | FDInterfaceLocInfoPEOReceiverLeTaxpayerId | RECEIVER_LE_TAXPAYER_ID | — | — |
| 36 | FDInterfaceLocInfoPEOReceiverSuppPartySiteId | RECEIVER_SUPP_PARTY_SITE_ID | — | — |
| 37 | FDInterfaceLocInfoPEOReceiverSupplierFormTaxNum | RECEIVER_SUPPLIER_FORM_TAX_NUM | — | — |
| 38 | FDInterfaceLocInfoPEOReceiverSupplierLocationId | RECEIVER_SUPPLIER_LOCATION_ID | — | — |
| 39 | FDInterfaceLocInfoPEOReceiverSupplierPartyId | RECEIVER_SUPPLIER_PARTY_ID | — | — |
| 40 | FDInterfaceLocInfoPEOReceiverSupplierTaxId | RECEIVER_SUPPLIER_TAX_ID | — | — |
| 41 | FDInterfaceLocInfoPEOReceiverSupplierTaxpayerId | RECEIVER_SUPPLIER_TAXPAYER_ID | — | — |
| 42 | FDInterfaceLocInfoPEOReceiverType | RECEIVER_TYPE | — | — |
| 43 | FDInterfaceLocInfoPEOShipfromCustPartySiteId | SHIPFROM_CUST_PARTY_SITE_ID | — | — |
| 44 | FDInterfaceLocInfoPEOShipfromCustomerFormTaxNum | SHIPFROM_CUSTOMER_FORM_TAX_NUM | — | — |
| 45 | FDInterfaceLocInfoPEOShipfromCustomerLocationId | SHIPFROM_CUSTOMER_LOCATION_ID | — | — |
| 46 | FDInterfaceLocInfoPEOShipfromCustomerPartyId | SHIPFROM_CUSTOMER_PARTY_ID | — | — |
| 47 | FDInterfaceLocInfoPEOShipfromCustomerTaxId | SHIPFROM_CUSTOMER_TAX_ID | — | — |
| 48 | FDInterfaceLocInfoPEOShipfromCustomerTaxpayerId | SHIPFROM_CUSTOMER_TAXPAYER_ID | — | — |
| 49 | FDInterfaceLocInfoPEOShipfromLeFormTaxNumber | SHIPFROM_LE_FORM_TAX_NUMBER | — | — |
| 50 | FDInterfaceLocInfoPEOShipfromLeLocationId | SHIPFROM_LE_LOCATION_ID | — | — |
| 51 | FDInterfaceLocInfoPEOShipfromLePartyId | SHIPFROM_LE_PARTY_ID | — | — |
| 52 | FDInterfaceLocInfoPEOShipfromLePartySiteId | SHIPFROM_LE_PARTY_SITE_ID | — | — |
| 53 | FDInterfaceLocInfoPEOShipfromLeTaxId | SHIPFROM_LE_TAX_ID | — | — |
| 54 | FDInterfaceLocInfoPEOShipfromLeTaxpayerId | SHIPFROM_LE_TAXPAYER_ID | — | — |
| 55 | FDInterfaceLocInfoPEOShipfromSuppPartySiteId | SHIPFROM_SUPP_PARTY_SITE_ID | — | — |
| 56 | FDInterfaceLocInfoPEOShipfromSupplierFormTaxNum | SHIPFROM_SUPPLIER_FORM_TAX_NUM | — | — |
| 57 | FDInterfaceLocInfoPEOShipfromSupplierLocationId | SHIPFROM_SUPPLIER_LOCATION_ID | — | — |
| 58 | FDInterfaceLocInfoPEOShipfromSupplierPartyId | SHIPFROM_SUPPLIER_PARTY_ID | — | — |
| 59 | FDInterfaceLocInfoPEOShipfromSupplierTaxId | SHIPFROM_SUPPLIER_TAX_ID | — | — |
| 60 | FDInterfaceLocInfoPEOShipfromSupplierTaxpayerId | SHIPFROM_SUPPLIER_TAXPAYER_ID | — | — |
| 61 | FDInterfaceLocInfoPEOShipfromType | SHIPFROM_TYPE | — | — |
| 62 | FDInterfaceLocInfoPEOShiptoCustPartySiteId | SHIPTO_CUST_PARTY_SITE_ID | — | — |
| 63 | FDInterfaceLocInfoPEOShiptoCustomerFormTaxNum | SHIPTO_CUSTOMER_FORM_TAX_NUM | — | — |
| 64 | FDInterfaceLocInfoPEOShiptoCustomerLocationId | SHIPTO_CUSTOMER_LOCATION_ID | — | — |
| 65 | FDInterfaceLocInfoPEOShiptoCustomerPartyId | SHIPTO_CUSTOMER_PARTY_ID | — | — |
| 66 | FDInterfaceLocInfoPEOShiptoCustomerTaxId | SHIPTO_CUSTOMER_TAX_ID | — | — |
| 67 | FDInterfaceLocInfoPEOShiptoCustomerTaxpayerId | SHIPTO_CUSTOMER_TAXPAYER_ID | — | — |
| 68 | FDInterfaceLocInfoPEOShiptoLeFormTaxNumber | SHIPTO_LE_FORM_TAX_NUMBER | — | — |
| 69 | FDInterfaceLocInfoPEOShiptoLeLocationId | SHIPTO_LE_LOCATION_ID | — | — |
| 70 | FDInterfaceLocInfoPEOShiptoLePartyId | SHIPTO_LE_PARTY_ID | — | — |
| 71 | FDInterfaceLocInfoPEOShiptoLePartySiteId | SHIPTO_LE_PARTY_SITE_ID | — | — |
| 72 | FDInterfaceLocInfoPEOShiptoLeTaxId | SHIPTO_LE_TAX_ID | — | — |
| 73 | FDInterfaceLocInfoPEOShiptoLeTaxpayerId | SHIPTO_LE_TAXPAYER_ID | — | — |
| 74 | FDInterfaceLocInfoPEOShiptoSuppPartySiteId | SHIPTO_SUPP_PARTY_SITE_ID | — | — |
| 75 | FDInterfaceLocInfoPEOShiptoSupplierFormTaxNum | SHIPTO_SUPPLIER_FORM_TAX_NUM | — | — |
| 76 | FDInterfaceLocInfoPEOShiptoSupplierLocationId | SHIPTO_SUPPLIER_LOCATION_ID | — | — |
| 77 | FDInterfaceLocInfoPEOShiptoSupplierPartyId | SHIPTO_SUPPLIER_PARTY_ID | — | — |
| 78 | FDInterfaceLocInfoPEOShiptoSupplierTaxId | SHIPTO_SUPPLIER_TAX_ID | — | — |
| 79 | FDInterfaceLocInfoPEOShiptoSupplierTaxpayerId | SHIPTO_SUPPLIER_TAXPAYER_ID | — | — |
| 80 | FDInterfaceLocInfoPEOShiptoType | SHIPTO_TYPE | — | — |

### [[cmf_fd_out_origin_cfops_v|CMF_FD_OUT_ORIGIN_CFOPS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocOutBoundCFOPPEOClassificationCode3 | CLASSIFICATION_CODE | — | — |
| 2 | FiscalDocOutBoundCFOPPEOClassificationName3 | CLASSIFICATION_NAME | — | ✅ |

### [[cmf_fd_references_int|CMF_FD_REFERENCES_INT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FDInterfaceReferencesPEOCreatedBy4 | CREATED_BY | — | — |
| 2 | FDInterfaceReferencesPEOCreationDate4 | CREATION_DATE | — | ✅ |
| 3 | FDInterfaceReferencesPEODocumentHeaderId4 | DOCUMENT_HEADER_ID | — | — |
| 4 | FDInterfaceReferencesPEODocumentRefAttrId | DOCUMENT_REF_ATTR_ID | — | — |
| 5 | FDInterfaceReferencesPEOExternalSystemRefId4 | EXTERNAL_SYSTEM_REF_ID | — | — |
| 6 | FDInterfaceReferencesPEOExternalSystemReference4 | EXTERNAL_SYSTEM_REFERENCE | — | — |
| 7 | FDInterfaceReferencesPEOFdHeadersIntId3 | FD_HEADERS_INT_ID | — | — |
| 8 | FDInterfaceReferencesPEOFdReferencesIntId | FD_REFERENCES_INT_ID | — | — |
| 9 | FDInterfaceReferencesPEOJobDefinitionName4 | JOB_DEFINITION_NAME | — | — |
| 10 | FDInterfaceReferencesPEOJobDefinitionPackage4 | JOB_DEFINITION_PACKAGE | — | — |
| 11 | FDInterfaceReferencesPEOLastUpdateDate4 | LAST_UPDATE_DATE | — | ✅ |
| 12 | FDInterfaceReferencesPEOLastUpdateLogin4 | LAST_UPDATE_LOGIN | — | — |
| 13 | FDInterfaceReferencesPEOLastUpdatedBy4 | LAST_UPDATED_BY | — | — |
| 14 | FDInterfaceReferencesPEOObjectVersionNumber4 | OBJECT_VERSION_NUMBER | — | — |
| 15 | FDInterfaceReferencesPEORefAccessKeyNumber | REF_ACCESS_KEY_NUMBER | — | ✅ |
| 16 | FDInterfaceReferencesPEORefDocumentHeaderId2 | REF_DOCUMENT_HEADER_ID | — | — |
| 17 | FDInterfaceReferencesPEORefDocumentNumber | REF_DOCUMENT_NUMBER | — | ✅ |
| 18 | FDInterfaceReferencesPEORefFdDocumentType1 | REF_FD_DOCUMENT_TYPE | — | ✅ |
| 19 | FDInterfaceReferencesPEORefIssueDate | REF_ISSUE_DATE | — | ✅ |
| 20 | FDInterfaceReferencesPEORefIssuerId | REF_ISSUER_ID | — | — |
| 21 | FDInterfaceReferencesPEORefIssuerState | REF_ISSUER_STATE | — | ✅ |
| 22 | FDInterfaceReferencesPEORefIssuerTaxpayerId | REF_ISSUER_TAXPAYER_ID | — | ✅ |
| 23 | FDInterfaceReferencesPEORefModel | REF_MODEL | — | ✅ |
| 24 | FDInterfaceReferencesPEORefSeries | REF_SERIES | — | ✅ |
| 25 | FDInterfaceReferencesPEORequestId4 | REQUEST_ID | — | — |
| 26 | FDInterfaceReferencesPEOValidationStatus2 | VALIDATION_STATUS | — | ✅ |

### [[cmf_fiscal_doc_assoctns_vl|CMF_FISCAL_DOC_ASSOCTNS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocAssoctnsPEOActiveFlag | ACTIVE_FLAG | — | — |
| 2 | FiscalDocAssoctnsPEOAssociationCode | ASSOCIATION_CODE | — | — |
| 3 | FiscalDocAssoctnsPEOCountryCode1 | COUNTRY_CODE | — | — |
| 4 | FiscalDocAssoctnsPEOCreatedBy6 | CREATED_BY | — | — |
| 5 | FiscalDocAssoctnsPEOCreationDate6 | CREATION_DATE | — | — |
| 6 | FiscalDocAssoctnsPEODescription | DESCRIPTION | — | — |
| 7 | FiscalDocAssoctnsPEOEndDate | END_DATE | — | — |
| 8 | FiscalDocAssoctnsPEOFiscalDocAssoctnsId1 | FISCAL_DOC_ASSOCTNS_ID | — | — |
| 9 | FiscalDocAssoctnsPEOFiscalProcOptionsId2 | FISCAL_PROC_OPTIONS_ID | — | — |
| 10 | FiscalDocAssoctnsPEOLastUpdateDate6 | LAST_UPDATE_DATE | — | — |
| 11 | FiscalDocAssoctnsPEOLastUpdateLogin6 | LAST_UPDATE_LOGIN | — | — |
| 12 | FiscalDocAssoctnsPEOLastUpdatedBy6 | LAST_UPDATED_BY | — | — |
| 13 | FiscalDocAssoctnsPEOName | NAME | — | — |
| 14 | FiscalDocAssoctnsPEOObjectVersionNumber6 | OBJECT_VERSION_NUMBER | — | — |
| 15 | FiscalDocAssoctnsPEOSeedFlag | SEED_FLAG | — | — |
| 16 | FiscalDocAssoctnsPEOStartDate | START_DATE | — | — |

### [[cmf_fiscal_operation_types|CMF_FISCAL_OPERATION_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FDOperationsTypePEOActiveFlag1 | ACTIVE_FLAG | — | — |
| 2 | FDOperationsTypePEOCreatedBy7 | CREATED_BY | — | — |
| 3 | FDOperationsTypePEOCreationDate7 | CREATION_DATE | — | — |
| 4 | FDOperationsTypePEOEndDate1 | END_DATE | — | — |
| 5 | FDOperationsTypePEOFiscalDocAssoctnsId2 | FISCAL_DOC_ASSOCTNS_ID | — | — |
| 6 | FDOperationsTypePEOFiscalOperationCode | FISCAL_OPERATION_CODE | — | — |
| 7 | FDOperationsTypePEOFiscalOperationTypeId | FISCAL_OPERATION_TYPE_ID | — | — |
| 8 | FDOperationsTypePEOLastUpdateDate7 | LAST_UPDATE_DATE | — | — |
| 9 | FDOperationsTypePEOLastUpdateLogin7 | LAST_UPDATE_LOGIN | — | — |
| 10 | FDOperationsTypePEOLastUpdatedBy7 | LAST_UPDATED_BY | — | — |
| 11 | FDOperationsTypePEOObjectVersionNumber7 | OBJECT_VERSION_NUMBER | — | — |
| 12 | FDOperationsTypePEOPaymentFlag | PAYMENT_FLAG | — | — |
| 13 | FDOperationsTypePEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 14 | FDOperationsTypePEOStartDate1 | START_DATE | — | — |

### [[cmf_fiscal_proc_options|CMF_FISCAL_PROC_OPTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalProcOptionsPEOAdditionalMatchRule | ADDITIONAL_MATCH_RULE | — | — |
| 2 | FiscalProcOptionsPEOChangeDocStatusFlag | CHANGE_DOC_STATUS_FLAG | — | — |
| 3 | FiscalProcOptionsPEOChargeAllocation1Flag | CHARGE_ALLOCATION_1_FLAG | — | — |
| 4 | FiscalProcOptionsPEOChargeAllocationFlag | CHARGE_ALLOCATION_FLAG | — | — |
| 5 | FiscalProcOptionsPEOChargesDistributionFlag | CHARGES_DISTRIBUTION_FLAG | — | — |
| 6 | FiscalProcOptionsPEOComplementaryFlag | COMPLEMENTARY_FLAG | — | — |
| 7 | FiscalProcOptionsPEOComplementaryLineType | COMPLEMENTARY_LINE_TYPE | — | — |
| 8 | FiscalProcOptionsPEOCostDistribution | COST_DISTRIBUTION | — | — |
| 9 | FiscalProcOptionsPEOCountryCode2 | COUNTRY_CODE | — | — |
| 10 | FiscalProcOptionsPEOCreatedBy8 | CREATED_BY | — | — |
| 11 | FiscalProcOptionsPEOCreationDate8 | CREATION_DATE | — | — |
| 12 | FiscalProcOptionsPEODeleteAllowedFlag | DELETE_ALLOWED_FLAG | — | — |
| 13 | FiscalProcOptionsPEODocumentTypeCode | DOCUMENT_TYPE_CODE | — | — |
| 14 | FiscalProcOptionsPEOElectronicModel | ELECTRONIC_MODEL | — | — |
| 15 | FiscalProcOptionsPEOEndDate2 | END_DATE | — | — |
| 16 | FiscalProcOptionsPEOFdCurrencyCode | FD_CURRENCY_CODE | — | — |
| 17 | FiscalProcOptionsPEOFdHeaderLineRelationship | FD_HEADER_LINE_RELATIONSHIP | — | — |
| 18 | FiscalProcOptionsPEOFdUsage | FD_USAGE | — | — |
| 19 | FiscalProcOptionsPEOFiscalAttributesFlag | FISCAL_ATTRIBUTES_FLAG | — | — |
| 20 | FiscalProcOptionsPEOFiscalProcOptionsId3 | FISCAL_PROC_OPTIONS_ID | — | — |
| 21 | FiscalProcOptionsPEOHoldMgmtFlag | HOLD_MGMT_FLAG | — | — |
| 22 | FiscalProcOptionsPEOIfaceApFlag | IFACE_AP_FLAG | — | — |
| 23 | FiscalProcOptionsPEOIfaceCstFlag | IFACE_CST_FLAG | — | — |
| 24 | FiscalProcOptionsPEOIfaceRcvFlag | IFACE_RCV_FLAG | — | — |
| 25 | FiscalProcOptionsPEOInformativeCharges | INFORMATIVE_CHARGES | — | — |
| 26 | FiscalProcOptionsPEOIssuerType1 | ISSUER_TYPE | — | — |
| 27 | FiscalProcOptionsPEOLastUpdateDate8 | LAST_UPDATE_DATE | — | — |
| 28 | FiscalProcOptionsPEOLastUpdateLogin8 | LAST_UPDATE_LOGIN | — | — |
| 29 | FiscalProcOptionsPEOLastUpdatedBy8 | LAST_UPDATED_BY | — | — |
| 30 | FiscalProcOptionsPEOLegalProcessesFlag | LEGAL_PROCESSES_FLAG | — | — |
| 31 | FiscalProcOptionsPEOLineSrcDocTypeCode | LINE_SRC_DOC_TYPE_CODE | — | — |
| 32 | FiscalProcOptionsPEOManualPrQttyEntryFlag | MANUAL_PR_QTTY_ENTRY_FLAG | — | — |
| 33 | FiscalProcOptionsPEOMatchRefPrepaymentFlag | MATCH_REF_PREPAYMENT_FLAG | — | — |
| 34 | FiscalProcOptionsPEOObjectVersionNumber8 | OBJECT_VERSION_NUMBER | — | — |
| 35 | FiscalProcOptionsPEOOperationType1 | OPERATION_TYPE | — | — |
| 36 | FiscalProcOptionsPEOParentProcessOptId | PARENT_PROCESS_OPT_ID | — | — |
| 37 | FiscalProcOptionsPEOPayablesDocTypeCode | PAYABLES_DOC_TYPE_CODE | — | — |
| 38 | FiscalProcOptionsPEOPhysicalRecptByOrderFd | PHYSICAL_RECPT_BY_ORDER_FD | — | — |
| 39 | FiscalProcOptionsPEOProcessCode | PROCESS_CODE | — | — |
| 40 | FiscalProcOptionsPEOProcessOptionCode | PROCESS_OPTION_CODE | — | — |
| 41 | FiscalProcOptionsPEOReceiverType1 | RECEIVER_TYPE | — | — |
| 42 | FiscalProcOptionsPEOReferenceAllowedFlag | REFERENCE_ALLOWED_FLAG | — | — |
| 43 | FiscalProcOptionsPEOSeedDataSource1 | SEED_DATA_SOURCE | — | — |
| 44 | FiscalProcOptionsPEOSeriesReq | SERIES_REQ | — | — |
| 45 | FiscalProcOptionsPEOShipFromType | SHIP_FROM_TYPE | — | — |
| 46 | FiscalProcOptionsPEOShipToType | SHIP_TO_TYPE | — | — |
| 47 | FiscalProcOptionsPEOSourceDocumentTypeCode | SOURCE_DOCUMENT_TYPE_CODE | — | — |
| 48 | FiscalProcOptionsPEOSrcDocCurrencyCode | SRC_DOC_CURRENCY_CODE | — | — |
| 49 | FiscalProcOptionsPEOStartDate2 | START_DATE | — | — |
| 50 | FiscalProcOptionsPEOSubSeriesReq | SUB_SERIES_REQ | — | — |
| 51 | FiscalProcOptionsPEOTaxCalculationFlag | TAX_CALCULATION_FLAG | — | — |
| 52 | FiscalProcOptionsPEOUpdateRefPhysicalReceipt | UPDATE_REF_PHYSICAL_RECEIPT | — | — |
| 53 | FiscalProcOptionsPEOValidateRefDocFlag | VALIDATE_REF_DOC_FLAG | — | — |
| 54 | FiscalProcOptionsPEOValidationFlag | VALIDATION_FLAG | — | — |

### [[cmf_fiscal_ref_options|CMF_FISCAL_REF_OPTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FDReferenceOptionPEOCopyRefFdTaxDeterminant | COPY_REF_FD_TAX_DETERMINANT | — | — |
| 2 | FDReferenceOptionPEOCreatedBy9 | CREATED_BY | — | — |
| 3 | FDReferenceOptionPEOCreationDate9 | CREATION_DATE | — | — |
| 4 | FDReferenceOptionPEOEndDate3 | END_DATE | — | — |
| 5 | FDReferenceOptionPEOFiscalProcOptionsId4 | FISCAL_PROC_OPTIONS_ID | — | — |
| 6 | FDReferenceOptionPEOFiscalRefOptionId | FISCAL_REF_OPTION_ID | — | — |
| 7 | FDReferenceOptionPEOLastUpdateDate9 | LAST_UPDATE_DATE | — | — |
| 8 | FDReferenceOptionPEOLastUpdateLogin9 | LAST_UPDATE_LOGIN | — | — |
| 9 | FDReferenceOptionPEOLastUpdatedBy9 | LAST_UPDATED_BY | — | — |
| 10 | FDReferenceOptionPEOObjectVersionNumber9 | OBJECT_VERSION_NUMBER | — | — |
| 11 | FDReferenceOptionPEORefEligibleStatus | REF_ELIGIBLE_STATUS | — | — |
| 12 | FDReferenceOptionPEORefFdIssuerType | REF_FD_ISSUER_TYPE | — | — |
| 13 | FDReferenceOptionPEORefFdProduct | REF_FD_PRODUCT | — | — |
| 14 | FDReferenceOptionPEORefProcessOptionCodes | REF_PROCESS_OPTION_CODES | — | — |
| 15 | FDReferenceOptionPEORefRelationship | REF_RELATIONSHIP | — | — |
| 16 | FDReferenceOptionPEORefRequired | REF_REQUIRED | — | — |
| 17 | FDReferenceOptionPEOReferencedEligibleStatus | REFERENCED_ELIGIBLE_STATUS | — | — |
| 18 | FDReferenceOptionPEOSeedDataSource2 | SEED_DATA_SOURCE | — | — |
| 19 | FDReferenceOptionPEOStartDate3 | START_DATE | — | — |

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitPEOBusinessUnitId | BU_ID | — | — |
| 2 | BusinessUnitPEOCreatedBy10 | CREATED_BY | — | — |
| 3 | BusinessUnitPEOCreationDate10 | CREATION_DATE | — | — |
| 4 | BusinessUnitPEODateFrom | DATE_FROM | — | — |
| 5 | BusinessUnitPEODateTo | DATE_TO | — | — |
| 6 | BusinessUnitPEODefaultCurrencyCode | DEFAULT_CURRENCY_CODE | — | — |
| 7 | BusinessUnitPEODefaultSetId | DEFAULT_SET_ID | — | — |
| 8 | BusinessUnitPEOEnabledForHrFlag | ENABLED_FOR_HR_FLAG | — | — |
| 9 | BusinessUnitPEOEnterpriseId | BUSINESS_GROUP_ID | — | — |
| 10 | BusinessUnitPEOFinancialsBusinessUnitId | FIN_BUSINESS_UNIT_ID | — | — |
| 11 | BusinessUnitPEOLastUpdateDate10 | LAST_UPDATE_DATE | — | — |
| 12 | BusinessUnitPEOLastUpdateLogin10 | LAST_UPDATE_LOGIN | — | — |
| 13 | BusinessUnitPEOLastUpdatedBy10 | LAST_UPDATED_BY | — | — |
| 14 | BusinessUnitPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 15 | BusinessUnitPEOLocationId | LOCATION_ID | — | — |
| 16 | BusinessUnitPEOManagerId | MANAGER_ID | — | — |
| 17 | BusinessUnitPEOName1 | BU_NAME | — | — |
| 18 | BusinessUnitPEOPrimaryLedgerId | PRIMARY_LEDGER_ID | — | — |
| 19 | BusinessUnitPEOProfitCenterFlag | PROFIT_CENTER_FLAG | — | — |
| 20 | BusinessUnitPEOShortCode | SHORT_CODE | — | — |
| 21 | BusinessUnitPEOStatus | STATUS | — | — |

### [[inv_units_of_measure_vl|INV_UNITS_OF_MEASURE_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UnitOfMeasurePEOBaseUomFlag | BASE_UOM_FLAG | — | — |
| 2 | UnitOfMeasurePEOCreatedBy8 | CREATED_BY | — | — |
| 3 | UnitOfMeasurePEOCreationDate8 | CREATION_DATE | — | — |
| 4 | UnitOfMeasurePEODescription | DESCRIPTION | — | — |
| 5 | UnitOfMeasurePEODisableDate | DISABLE_DATE | — | — |
| 6 | UnitOfMeasurePEOHasGeneratedCode | HAS_GENERATED_CODE | — | — |
| 7 | UnitOfMeasurePEOJobDefinitionName8 | JOB_DEFINITION_NAME | — | — |
| 8 | UnitOfMeasurePEOJobDefinitionPackage8 | JOB_DEFINITION_PACKAGE | — | — |
| 9 | UnitOfMeasurePEOLastUpdateDate8 | LAST_UPDATE_DATE | — | — |
| 10 | UnitOfMeasurePEOLastUpdateLogin8 | LAST_UPDATE_LOGIN | — | — |
| 11 | UnitOfMeasurePEOLastUpdatedBy8 | LAST_UPDATED_BY | — | — |
| 12 | UnitOfMeasurePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | UnitOfMeasurePEORequestId8 | REQUEST_ID | — | — |
| 14 | UnitOfMeasurePEOStandardPackFlag | STANDARD_PACK_FLAG | — | — |
| 15 | UnitOfMeasurePEOUnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |
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
| 5 | FiscalDocHeaderIntrEOContainerIdentifier | CONTAINER_IDENTIFIER | — | — |
| 6 | FiscalDocHeaderIntrEOContingencyType | CONTINGENCY_TYPE | — | — |
| 7 | FiscalDocHeaderIntrEOCreatedBy | CREATED_BY | — | — |
| 8 | FiscalDocHeaderIntrEOCreationDate | CREATION_DATE | — | — |
| 9 | FiscalDocHeaderIntrEODocNature | DOC_NATURE | — | — |
| 10 | FiscalDocHeaderIntrEODocNum | DOC_NUM | — | — |
| 11 | FiscalDocHeaderIntrEOEntityCode | ENTITY_CODE | — | — |
| 12 | FiscalDocHeaderIntrEOEventClassCode | EVENT_CLASS_CODE | — | — |
| 13 | FiscalDocHeaderIntrEOFerryIdentification | FERRY_IDENTIFICATION | — | — |
| 14 | FiscalDocHeaderIntrEOFiscalDocDate | FISCAL_DOC_DATE | — | — |
| 15 | FiscalDocHeaderIntrEOFiscalDocKey | FISCAL_DOC_KEY | — | — |
| 16 | FiscalDocHeaderIntrEOFreightType | FREIGHT_TYPE | — | — |
| 17 | FiscalDocHeaderIntrEOGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 18 | FiscalDocHeaderIntrEOGlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | — |
| 19 | FiscalDocHeaderIntrEOGlobalAttributeNumber1 | GLOBAL_ATTRIBUTE_NUMBER1 | — | — |
| 20 | FiscalDocHeaderIntrEOGlobalAttributeNumber2 | GLOBAL_ATTRIBUTE_NUMBER2 | — | — |
| 21 | FiscalDocHeaderIntrEOGlobalAttributeNumber3 | GLOBAL_ATTRIBUTE_NUMBER3 | — | — |
| 22 | FiscalDocHeaderIntrEOGlobalAttributeNumber4 | GLOBAL_ATTRIBUTE_NUMBER4 | — | — |
| 23 | FiscalDocHeaderIntrEOGlobalAttributeNumber5 | GLOBAL_ATTRIBUTE_NUMBER5 | — | — |
| 24 | FiscalDocHeaderIntrEOGoodsBrandCarried | GOODS_BRAND_CARRIED | — | — |
| 25 | FiscalDocHeaderIntrEOGoodsTypeCarried | GOODS_TYPE_CARRIED | — | — |
| 26 | FiscalDocHeaderIntrEOGrossWeight | GROSS_WEIGHT | — | — |
| 27 | FiscalDocHeaderIntrEOIndustryType | INDUSTRY_TYPE | — | — |
| 28 | FiscalDocHeaderIntrEOInterfaceHdrId | INTERFACE_HDR_ID | — | — |
| 29 | FiscalDocHeaderIntrEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 30 | FiscalDocHeaderIntrEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 31 | FiscalDocHeaderIntrEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 32 | FiscalDocHeaderIntrEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 33 | FiscalDocHeaderIntrEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 34 | FiscalDocHeaderIntrEOLegalEntityIdentifier | LEGAL_ENTITY_IDENTIFIER | — | — |
| 35 | FiscalDocHeaderIntrEOLegalRepUnitName | LEGAL_REP_UNIT_NAME | — | — |
| 36 | FiscalDocHeaderIntrEOLoadRequestId | LOAD_REQUEST_ID | — | — |
| 37 | FiscalDocHeaderIntrEOMatIssueRecptDate | MAT_ISSUE_RECPT_DATE | — | — |
| 38 | FiscalDocHeaderIntrEOMatIssueRecptHour | MAT_ISSUE_RECPT_HOUR | — | — |
| 39 | FiscalDocHeaderIntrEONetWeight | NET_WEIGHT | — | — |
| 40 | FiscalDocHeaderIntrEOOrgId | ORG_ID | — | — |
| 41 | FiscalDocHeaderIntrEOPaymentOption | PAYMENT_OPTION | — | — |
| 42 | FiscalDocHeaderIntrEOPurchaseContract | PURCHASE_CONTRACT | — | — |
| 43 | FiscalDocHeaderIntrEOQuantityCarried | QUANTITY_CARRIED | — | — |
| 44 | FiscalDocHeaderIntrEORefComplementaryFdFlag | REF_COMPLEMENTARY_FD_FLAG | — | — |
| 45 | FiscalDocHeaderIntrEORefDocIssuerStateCode | REF_DOC_ISSUER_STATE_CODE | — | — |
| 46 | FiscalDocHeaderIntrEORefDocNum | REF_DOC_NUM | — | — |
| 47 | FiscalDocHeaderIntrEORefFiscalDocDate | REF_FISCAL_DOC_DATE | — | — |
| 48 | FiscalDocHeaderIntrEORefFiscalDocKey | REF_FISCAL_DOC_KEY | — | — |
| 49 | FiscalDocHeaderIntrEORefIssuerTaxpayerId | REF_ISSUER_TAXPAYER_ID | — | — |
| 50 | FiscalDocHeaderIntrEORefModel | REF_MODEL | — | — |
| 51 | FiscalDocHeaderIntrEORefRuralFlag | REF_RURAL_FLAG | — | — |
| 52 | FiscalDocHeaderIntrEORefSeries | REF_SERIES | — | — |
| 53 | FiscalDocHeaderIntrEORequestId | REQUEST_ID | — | — |
| 54 | FiscalDocHeaderIntrEOSealNumber | SEAL_NUMBER | — | — |
| 55 | FiscalDocHeaderIntrEOSeries | SERIES | — | — |
| 56 | FiscalDocHeaderIntrEOServiceSeries | SERVICE_SERIES | — | — |
| 57 | FiscalDocHeaderIntrEOServiceSituation | SERVICE_SITUATION | — | — |
| 58 | FiscalDocHeaderIntrEOServiceTaxPaidFlag | SERVICE_TAX_PAID_FLAG | — | — |
| 59 | FiscalDocHeaderIntrEOTaxAuthDocNumber | TAX_AUTH_DOC_NUMBER | — | — |
| 60 | FiscalDocHeaderIntrEOTaxSettlementDate | TAX_SETTLEMENT_DATE | — | — |
| 61 | FiscalDocHeaderIntrEOTempServiceType | TEMP_SERVICE_TYPE | — | — |
| 62 | FiscalDocHeaderIntrEOTrxFdTypeDeterminant | TRX_FD_TYPE_DETERMINANT | — | — |
| 63 | FiscalDocHeaderIntrEOTrxNumber | TRX_NUMBER | — | — |
| 64 | FiscalDocHeaderIntrEOVendorId | VENDOR_ID | — | — |
| 65 | FiscalDocHeaderIntrEOVendorName | VENDOR_NAME | — | — |
| 66 | FiscalDocHeaderIntrEOVendorNum | VENDOR_NUM | — | — |
| 67 | FiscalDocHeaderIntrEOWagonIdentification | WAGON_IDENTIFICATION | — | — |
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
| 7 | FiscalDocHeaderDetailIntrEOGlobalAttribute31 | GLOBAL_ATTRIBUTE3 | — | — |
| 8 | FiscalDocHeaderDetailIntrEOGlobalAttribute41 | GLOBAL_ATTRIBUTE4 | — | — |
| 9 | FiscalDocHeaderDetailIntrEOGlobalAttribute71 | GLOBAL_ATTRIBUTE7 | — | — |
| 10 | FiscalDocHeaderDetailIntrEOGlobalAttributeNumber21 | GLOBAL_ATTRIBUTE_NUMBER2 | — | — |
| 11 | FiscalDocHeaderDetailIntrEOGlobalAttributeNumber32 | GLOBAL_ATTRIBUTE_NUMBER3 | — | — |
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
| 7 | FiscalDocLineIntrEOGlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | — |
| 8 | FiscalDocLineIntrEOGlobalAttribute11 | GLOBAL_ATTRIBUTE1 | — | — |
| 9 | FiscalDocLineIntrEOGlobalAttribute111 | GLOBAL_ATTRIBUTE11 | — | — |
| 10 | FiscalDocLineIntrEOGlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | — |
| 11 | FiscalDocLineIntrEOGlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | — |
| 12 | FiscalDocLineIntrEOGlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | — |
| 13 | FiscalDocLineIntrEOGlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | — |
| 14 | FiscalDocLineIntrEOGlobalAttribute16 | GLOBAL_ATTRIBUTE16 | — | — |
| 15 | FiscalDocLineIntrEOGlobalAttribute17 | GLOBAL_ATTRIBUTE17 | — | — |
| 16 | FiscalDocLineIntrEOGlobalAttribute18 | GLOBAL_ATTRIBUTE18 | — | — |
| 17 | FiscalDocLineIntrEOGlobalAttribute19 | GLOBAL_ATTRIBUTE19 | — | — |
| 18 | FiscalDocLineIntrEOGlobalAttribute20 | GLOBAL_ATTRIBUTE20 | — | — |
| 19 | FiscalDocLineIntrEOGlobalAttribute21 | GLOBAL_ATTRIBUTE2 | — | — |
| 20 | FiscalDocLineIntrEOGlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | — |
| 21 | FiscalDocLineIntrEOGlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | — |
| 22 | FiscalDocLineIntrEOGlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | — |
| 23 | FiscalDocLineIntrEOGlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | — |
| 24 | FiscalDocLineIntrEOGlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | — |
| 25 | FiscalDocLineIntrEOGlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | — |
| 26 | FiscalDocLineIntrEOGlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | — |
| 27 | FiscalDocLineIntrEOGlobalAttributeNumber10 | GLOBAL_ATTRIBUTE_NUMBER10 | — | — |
| 28 | FiscalDocLineIntrEOGlobalAttributeNumber11 | GLOBAL_ATTRIBUTE_NUMBER11 | — | — |
| 29 | FiscalDocLineIntrEOGlobalAttributeNumber12 | GLOBAL_ATTRIBUTE_NUMBER12 | — | — |
| 30 | FiscalDocLineIntrEOGlobalAttributeNumber31 | GLOBAL_ATTRIBUTE_NUMBER3 | — | — |
| 31 | FiscalDocLineIntrEOGlobalAttributeNumber7 | GLOBAL_ATTRIBUTE_NUMBER7 | — | — |
| 32 | FiscalDocLineIntrEOGlobalAttributeNumber8 | GLOBAL_ATTRIBUTE_NUMBER8 | — | — |
| 33 | FiscalDocLineIntrEOGlobalAttributeNumber9 | GLOBAL_ATTRIBUTE_NUMBER9 | — | — |
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
| 45 | FiscalDocLineIntrEOServiceSituation1 | SERVICE_SITUATION | — | — |
| 46 | FiscalDocLineIntrEOTrxLevelType | TRX_LEVEL_TYPE | — | — |
| 47 | FiscalDocLineIntrEOTrxLineNumber | TRX_LINE_NUMBER | — | — |
| 48 | FiscalDocLineIntrEOTrxNumber1 | TRX_NUMBER | — | — |

### [[jg_fscl_ln_dtls_atrb_int|JG_FSCL_LN_DTLS_ATRB_INT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocLineDetailIntrEOAppShortName6 | APP_SHORT_NAME | — | — |
| 2 | FiscalDocLineDetailIntrEOBuName5 | BU_NAME | — | — |
| 3 | FiscalDocLineDetailIntrEOCreatedBy6 | CREATED_BY | — | — |
| 4 | FiscalDocLineDetailIntrEOCreationDate6 | CREATION_DATE | — | — |
| 5 | FiscalDocLineDetailIntrEOEntityCode6 | ENTITY_CODE | — | — |
| 6 | FiscalDocLineDetailIntrEOEventClassCode6 | EVENT_CLASS_CODE | — | — |
| 7 | FiscalDocLineDetailIntrEOGlobalAttribute110 | GLOBAL_ATTRIBUTE1 | — | — |
| 8 | FiscalDocLineDetailIntrEOGlobalAttribute22 | GLOBAL_ATTRIBUTE2 | — | — |
| 9 | FiscalDocLineDetailIntrEOGlobalAttribute32 | GLOBAL_ATTRIBUTE3 | — | — |
| 10 | FiscalDocLineDetailIntrEOGlobalAttribute42 | GLOBAL_ATTRIBUTE4 | — | — |
| 11 | FiscalDocLineDetailIntrEOGlobalAttribute51 | GLOBAL_ATTRIBUTE5 | — | — |
| 12 | FiscalDocLineDetailIntrEOGlobalAttribute61 | GLOBAL_ATTRIBUTE6 | — | — |
| 13 | FiscalDocLineDetailIntrEOGlobalAttributeDate1 | GLOBAL_ATTRIBUTE_DATE1 | — | — |
| 14 | FiscalDocLineDetailIntrEOGlobalAttributeDate2 | GLOBAL_ATTRIBUTE_DATE2 | — | — |
| 15 | FiscalDocLineDetailIntrEOGlobalAttributeDate3 | GLOBAL_ATTRIBUTE_DATE3 | — | — |
| 16 | FiscalDocLineDetailIntrEOGlobalAttributeNumber13 | GLOBAL_ATTRIBUTE_NUMBER1 | — | — |
| 17 | FiscalDocLineDetailIntrEOGlobalAttributeNumber22 | GLOBAL_ATTRIBUTE_NUMBER2 | — | — |
| 18 | FiscalDocLineDetailIntrEOInterfaceHdrId6 | INTERFACE_HDR_ID | — | — |
| 19 | FiscalDocLineDetailIntrEOInterfaceLineDetailId | INTERFACE_LINE_DETAIL_ID | — | — |
| 20 | FiscalDocLineDetailIntrEOInterfaceLineId3 | INTERFACE_LINE_ID | — | — |
| 21 | FiscalDocLineDetailIntrEOJobDefinitionName6 | JOB_DEFINITION_NAME | — | — |
| 22 | FiscalDocLineDetailIntrEOJobDefinitionPackage6 | JOB_DEFINITION_PACKAGE | — | — |
| 23 | FiscalDocLineDetailIntrEOLastUpdateDate6 | LAST_UPDATE_DATE | — | — |
| 24 | FiscalDocLineDetailIntrEOLastUpdateLogin6 | LAST_UPDATE_LOGIN | — | — |
| 25 | FiscalDocLineDetailIntrEOLastUpdatedBy6 | LAST_UPDATED_BY | — | — |
| 26 | FiscalDocLineDetailIntrEOLoadRequestId6 | LOAD_REQUEST_ID | — | — |
| 27 | FiscalDocLineDetailIntrEOOrgId5 | ORG_ID | — | — |
| 28 | FiscalDocLineDetailIntrEORequestId6 | REQUEST_ID | — | — |
| 29 | FiscalDocLineDetailIntrEOTrxLevelType3 | TRX_LEVEL_TYPE | — | — |
| 30 | FiscalDocLineDetailIntrEOTrxLineDetailNumber | TRX_LINE_DETAIL_NUMBER | — | — |
| 31 | FiscalDocLineDetailIntrEOTrxLineNumber3 | TRX_LINE_NUMBER | — | — |

### [[jg_fscl_tax_lines_int|JG_FSCL_TAX_LINES_INT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocTaxLineIntrEOAppShortName2 | APP_SHORT_NAME | — | — |
| 2 | FiscalDocTaxLineIntrEOCityCode | CITY_CODE | — | — |
| 3 | FiscalDocTaxLineIntrEOCreatedBy2 | CREATED_BY | — | — |
| 4 | FiscalDocTaxLineIntrEOCreationDate2 | CREATION_DATE | — | — |
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
| 15 | FiscalDocTaxLineIntrEOLastUpdateDate2 | LAST_UPDATE_DATE | — | — |
| 16 | FiscalDocTaxLineIntrEOLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 17 | FiscalDocTaxLineIntrEOLastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 18 | FiscalDocTaxLineIntrEOLoadRequestId2 | LOAD_REQUEST_ID | — | — |
| 19 | FiscalDocTaxLineIntrEOQuantity | QUANTITY | — | — |
| 20 | FiscalDocTaxLineIntrEOReportingTypeCode | REPORTING_TYPE_CODE | — | — |
| 21 | FiscalDocTaxLineIntrEORequestId2 | REQUEST_ID | — | — |
| 22 | FiscalDocTaxLineIntrEOServiceItemCode | SERVICE_ITEM_CODE | — | — |
| 23 | FiscalDocTaxLineIntrEOTax | TAX | — | — |
| 24 | FiscalDocTaxLineIntrEOTaxAmt | TAX_AMT | — | — |
| 25 | FiscalDocTaxLineIntrEOTaxAmtIncludedFlag | TAX_AMT_INCLUDED_FLAG | — | — |
| 26 | FiscalDocTaxLineIntrEOTaxLineNumber | TAX_LINE_NUMBER | — | — |
| 27 | FiscalDocTaxLineIntrEOTaxRate | TAX_RATE | — | — |
| 28 | FiscalDocTaxLineIntrEOTaxRateCode | TAX_RATE_CODE | — | — |
| 29 | FiscalDocTaxLineIntrEOTaxRegimeCode | TAX_REGIME_CODE | — | — |
| 30 | FiscalDocTaxLineIntrEOTaxSituationCode | TAX_SITUATION_CODE | — | — |
| 31 | FiscalDocTaxLineIntrEOTaxStatusCode | TAX_STATUS_CODE | — | — |
| 32 | FiscalDocTaxLineIntrEOTaxableAmt | TAXABLE_AMT | — | — |
| 33 | FiscalDocTaxLineIntrEOTaxableAmtDetermCode | TAXABLE_AMT_DETERM_CODE | — | — |
| 34 | FiscalDocTaxLineIntrEOTaxableBasisPercPayerOpr | TAXABLE_BASIS_PERC_PAYER_OPR | — | — |
| 35 | FiscalDocTaxLineIntrEOTaxableBasisReductionPerc | TAXABLE_BASIS_REDUCTION_PERC | — | — |
| 36 | FiscalDocTaxLineIntrEOTrxLevelType1 | TRX_LEVEL_TYPE | — | — |
| 37 | FiscalDocTaxLineIntrEOTrxLineNumber1 | TRX_LINE_NUMBER | — | — |
| 38 | FiscalDocTaxLineIntrEOTrxNumber2 | TRX_NUMBER | — | — |
| 39 | FiscalDocTaxLineIntrEOUomCode | UOM_CODE | — | — |
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
| 8 | FDHdrsIntCreatedByPersonNameFullName | FULL_NAME | — | — |
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
| 35 | FDHdrsIntLastUpdtdByPersonNaFullName1 | FULL_NAME | — | — |
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
| 55 | FDLineIntCreatedByPNBusinessGroupId6 | BUSINESS_GROUP_ID | — | — |
| 56 | FDLineIntCreatedByPNCreatedBy6 | CREATED_BY | — | — |
| 57 | FDLineIntCreatedByPNCreationDate6 | CREATION_DATE | — | — |
| 58 | FDLineIntCreatedByPNDisplayName2 | DISPLAY_NAME | — | — |
| 59 | FDLineIntCreatedByPNEffectiveEndDate2 | EFFECTIVE_END_DATE | — | — |
| 60 | FDLineIntCreatedByPNEffectiveStartDate2 | EFFECTIVE_START_DATE | — | — |
| 61 | FDLineIntCreatedByPNFirstName2 | FIRST_NAME | — | — |
| 62 | FDLineIntCreatedByPNFullName2 | FULL_NAME | — | — |
| 63 | FDLineIntCreatedByPNHonors2 | HONORS | — | — |
| 64 | FDLineIntCreatedByPNKnownAs2 | KNOWN_AS | — | — |
| 65 | FDLineIntCreatedByPNLastName2 | LAST_NAME | — | — |
| 66 | FDLineIntCreatedByPNLastUpdateDate6 | LAST_UPDATE_DATE | — | — |
| 67 | FDLineIntCreatedByPNLastUpdateLogin6 | LAST_UPDATE_LOGIN | — | — |
| 68 | FDLineIntCreatedByPNLastUpdatedBy6 | LAST_UPDATED_BY | — | — |
| 69 | FDLineIntCreatedByPNLegislationCode2 | LEGISLATION_CODE | — | — |
| 70 | FDLineIntCreatedByPNListName2 | LIST_NAME | — | — |
| 71 | FDLineIntCreatedByPNMiddleNames2 | MIDDLE_NAMES | — | — |
| 72 | FDLineIntCreatedByPNMilitaryRank2 | MILITARY_RANK | — | — |
| 73 | FDLineIntCreatedByPNNameType2 | NAME_TYPE | — | — |
| 74 | FDLineIntCreatedByPNObjectVersionNumber6 | OBJECT_VERSION_NUMBER | — | — |
| 75 | FDLineIntCreatedByPNOrderName2 | ORDER_NAME | — | — |
| 76 | FDLineIntCreatedByPNPersonId6 | PERSON_ID | — | — |
| 77 | FDLineIntCreatedByPNPersonNameId2 | PERSON_NAME_ID | — | — |
| 78 | FDLineIntCreatedByPNPreNameAdjunct2 | PRE_NAME_ADJUNCT | — | — |
| 79 | FDLineIntCreatedByPNPreviousLastName2 | PREVIOUS_LAST_NAME | — | — |
| 80 | FDLineIntCreatedByPNSuffix2 | SUFFIX | — | — |
| 81 | FDLineIntCreatedByPNTitle2 | TITLE | — | — |
| 82 | FDLineIntLastUpdtdByPNBusinessGroupId7 | BUSINESS_GROUP_ID | — | — |
| 83 | FDLineIntLastUpdtdByPNCreatedBy7 | CREATED_BY | — | — |
| 84 | FDLineIntLastUpdtdByPNCreationDate7 | CREATION_DATE | — | — |
| 85 | FDLineIntLastUpdtdByPNDisplayName3 | DISPLAY_NAME | — | — |
| 86 | FDLineIntLastUpdtdByPNEffectiveEndDate3 | EFFECTIVE_END_DATE | — | — |
| 87 | FDLineIntLastUpdtdByPNEffectiveStartDate3 | EFFECTIVE_START_DATE | — | — |
| 88 | FDLineIntLastUpdtdByPNFirstName3 | FIRST_NAME | — | — |
| 89 | FDLineIntLastUpdtdByPNFullName3 | FULL_NAME | — | — |
| 90 | FDLineIntLastUpdtdByPNHonors3 | HONORS | — | — |
| 91 | FDLineIntLastUpdtdByPNKnownAs3 | KNOWN_AS | — | — |
| 92 | FDLineIntLastUpdtdByPNLastName3 | LAST_NAME | — | — |
| 93 | FDLineIntLastUpdtdByPNLastUpdateDate7 | LAST_UPDATE_DATE | — | — |
| 94 | FDLineIntLastUpdtdByPNLastUpdateLogin7 | LAST_UPDATE_LOGIN | — | — |
| 95 | FDLineIntLastUpdtdByPNLastUpdatedBy7 | LAST_UPDATED_BY | — | — |
| 96 | FDLineIntLastUpdtdByPNLegislationCode3 | LEGISLATION_CODE | — | — |
| 97 | FDLineIntLastUpdtdByPNListName3 | LIST_NAME | — | — |
| 98 | FDLineIntLastUpdtdByPNMiddleNames3 | MIDDLE_NAMES | — | — |
| 99 | FDLineIntLastUpdtdByPNMilitaryRank3 | MILITARY_RANK | — | — |
| 100 | FDLineIntLastUpdtdByPNNameType3 | NAME_TYPE | — | — |
| 101 | FDLineIntLastUpdtdByPNObjectVersionNumber7 | OBJECT_VERSION_NUMBER | — | — |
| 102 | FDLineIntLastUpdtdByPNOrderName3 | ORDER_NAME | — | — |
| 103 | FDLineIntLastUpdtdByPNPersonId7 | PERSON_ID | — | — |
| 104 | FDLineIntLastUpdtdByPNPersonNameId3 | PERSON_NAME_ID | — | — |
| 105 | FDLineIntLastUpdtdByPNPreNameAdjunct3 | PRE_NAME_ADJUNCT | — | — |
| 106 | FDLineIntLastUpdtdByPNPreviousLastName3 | PREVIOUS_LAST_NAME | — | — |
| 107 | FDLineIntLastUpdtdByPNSuffix3 | SUFFIX | — | — |
| 108 | FDLineIntLastUpdtdByPNTitle3 | TITLE | — | — |
| 109 | IntHdrCreatedByPersonNameDPEBusinessGroupId8 | BUSINESS_GROUP_ID | — | — |
| 110 | IntHdrCreatedByPersonNameDPECreatedBy8 | CREATED_BY | — | — |
| 111 | IntHdrCreatedByPersonNameDPECreationDate8 | CREATION_DATE | — | — |
| 112 | IntHdrCreatedByPersonNameDPEDisplayName | DISPLAY_NAME | — | — |
| 113 | IntHdrCreatedByPersonNameDPEEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 114 | IntHdrCreatedByPersonNameDPEEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 115 | IntHdrCreatedByPersonNameDPEFirstName | FIRST_NAME | — | — |
| 116 | IntHdrCreatedByPersonNameDPEFullName | FULL_NAME | — | ✅ |
| 117 | IntHdrCreatedByPersonNameDPEHonors | HONORS | — | — |
| 118 | IntHdrCreatedByPersonNameDPEKnownAs | KNOWN_AS | — | — |
| 119 | IntHdrCreatedByPersonNameDPELastName | LAST_NAME | — | — |
| 120 | IntHdrCreatedByPersonNameDPELastUpdateDate8 | LAST_UPDATE_DATE | — | — |
| 121 | IntHdrCreatedByPersonNameDPELastUpdateLogin8 | LAST_UPDATE_LOGIN | — | — |
| 122 | IntHdrCreatedByPersonNameDPELastUpdatedBy8 | LAST_UPDATED_BY | — | — |
| 123 | IntHdrCreatedByPersonNameDPELegislationCode | LEGISLATION_CODE | — | — |
| 124 | IntHdrCreatedByPersonNameDPEListName | LIST_NAME | — | — |
| 125 | IntHdrCreatedByPersonNameDPEMiddleNames | MIDDLE_NAMES | — | — |
| 126 | IntHdrCreatedByPersonNameDPEMilitaryRank | MILITARY_RANK | — | — |
| 127 | IntHdrCreatedByPersonNameDPENameType | NAME_TYPE | — | — |
| 128 | IntHdrCreatedByPersonNameDPEObjectVersionNumber8 | OBJECT_VERSION_NUMBER | — | — |
| 129 | IntHdrCreatedByPersonNameDPEOrderName | ORDER_NAME | — | — |
| 130 | IntHdrCreatedByPersonNameDPEPersonId8 | PERSON_ID | — | — |
| 131 | IntHdrCreatedByPersonNameDPEPersonNameId | PERSON_NAME_ID | — | — |
| 132 | IntHdrCreatedByPersonNameDPEPreNameAdjunct | PRE_NAME_ADJUNCT | — | — |
| 133 | IntHdrCreatedByPersonNameDPEPreviousLastName | PREVIOUS_LAST_NAME | — | — |
| 134 | IntHdrCreatedByPersonNameDPESuffix | SUFFIX | — | — |
| 135 | IntHdrCreatedByPersonNameDPETitle | TITLE | — | — |
| 136 | IntHdrLUpdtdByPersonNameDPEOBusinessGroupId9 | BUSINESS_GROUP_ID | — | — |
| 137 | IntHdrLUpdtdByPersonNameDPEOCreatedBy9 | CREATED_BY | — | — |
| 138 | IntHdrLUpdtdByPersonNameDPEOCreationDate9 | CREATION_DATE | — | — |
| 139 | IntHdrLUpdtdByPersonNameDPEODisplayName1 | DISPLAY_NAME | — | — |
| 140 | IntHdrLUpdtdByPersonNameDPEOEffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 141 | IntHdrLUpdtdByPersonNameDPEOEffectiveStartDate1 | EFFECTIVE_START_DATE | — | — |
| 142 | IntHdrLUpdtdByPersonNameDPEOFirstName1 | FIRST_NAME | — | — |
| 143 | IntHdrLUpdtdByPersonNameDPEOFullName1 | FULL_NAME | — | ✅ |
| 144 | IntHdrLUpdtdByPersonNameDPEOHonors1 | HONORS | — | — |
| 145 | IntHdrLUpdtdByPersonNameDPEOKnownAs1 | KNOWN_AS | — | — |
| 146 | IntHdrLUpdtdByPersonNameDPEOLastName1 | LAST_NAME | — | — |
| 147 | IntHdrLUpdtdByPersonNameDPEOLastUpdateDate9 | LAST_UPDATE_DATE | — | — |
| 148 | IntHdrLUpdtdByPersonNameDPEOLastUpdateLogin9 | LAST_UPDATE_LOGIN | — | — |
| 149 | IntHdrLUpdtdByPersonNameDPEOLastUpdatedBy9 | LAST_UPDATED_BY | — | — |
| 150 | IntHdrLUpdtdByPersonNameDPEOLegislationCode1 | LEGISLATION_CODE | — | — |
| 151 | IntHdrLUpdtdByPersonNameDPEOListName1 | LIST_NAME | — | — |
| 152 | IntHdrLUpdtdByPersonNameDPEOMiddleNames1 | MIDDLE_NAMES | — | — |
| 153 | IntHdrLUpdtdByPersonNameDPEOMilitaryRank1 | MILITARY_RANK | — | — |
| 154 | IntHdrLUpdtdByPersonNameDPEONameType1 | NAME_TYPE | — | — |
| 155 | IntHdrLUpdtdByPersonNameDPEOObjectVersionNumber9 | OBJECT_VERSION_NUMBER | — | — |
| 156 | IntHdrLUpdtdByPersonNameDPEOOrderName1 | ORDER_NAME | — | — |
| 157 | IntHdrLUpdtdByPersonNameDPEOPersonId9 | PERSON_ID | — | — |
| 158 | IntHdrLUpdtdByPersonNameDPEOPersonNameId1 | PERSON_NAME_ID | — | — |
| 159 | IntHdrLUpdtdByPersonNameDPEOPreNameAdjunct1 | PRE_NAME_ADJUNCT | — | — |
| 160 | IntHdrLUpdtdByPersonNameDPEOPreviousLastName1 | PREVIOUS_LAST_NAME | — | — |
| 161 | IntHdrLUpdtdByPersonNameDPEOSuffix1 | SUFFIX | — | — |
| 162 | IntHdrLUpdtdByPersonNameDPEOTitle1 | TITLE | — | — |
| 163 | IntLegProcCreatedByPersonNamBusinessGroupId12 | BUSINESS_GROUP_ID | — | — |
| 164 | IntLegProcCreatedByPersonNamCreatedBy12 | CREATED_BY | — | — |
| 165 | IntLegProcCreatedByPersonNamCreationDate12 | CREATION_DATE | — | — |
| 166 | IntLegProcCreatedByPersonNamDisplayName4 | DISPLAY_NAME | — | — |
| 167 | IntLegProcCreatedByPersonNamEffectiveEndDate4 | EFFECTIVE_END_DATE | — | — |
| 168 | IntLegProcCreatedByPersonNamEffectiveStartDate4 | EFFECTIVE_START_DATE | — | — |
| 169 | IntLegProcCreatedByPersonNamFirstName4 | FIRST_NAME | — | — |
| 170 | IntLegProcCreatedByPersonNamFullName4 | FULL_NAME | — | ✅ |
| 171 | IntLegProcCreatedByPersonNamHonors4 | HONORS | — | — |
| 172 | IntLegProcCreatedByPersonNamKnownAs4 | KNOWN_AS | — | — |
| 173 | IntLegProcCreatedByPersonNamLastName4 | LAST_NAME | — | — |
| 174 | IntLegProcCreatedByPersonNamLastUpdateDate12 | LAST_UPDATE_DATE | — | — |
| 175 | IntLegProcCreatedByPersonNamLastUpdateLogin12 | LAST_UPDATE_LOGIN | — | — |
| 176 | IntLegProcCreatedByPersonNamLastUpdatedBy12 | LAST_UPDATED_BY | — | — |
| 177 | IntLegProcCreatedByPersonNamLegislationCode4 | LEGISLATION_CODE | — | — |
| 178 | IntLegProcCreatedByPersonNamListName4 | LIST_NAME | — | — |
| 179 | IntLegProcCreatedByPersonNamMiddleNames4 | MIDDLE_NAMES | — | — |
| 180 | IntLegProcCreatedByPersonNamMilitaryRank4 | MILITARY_RANK | — | — |
| 181 | IntLegProcCreatedByPersonNamNameType4 | NAME_TYPE | — | — |
| 182 | IntLegProcCreatedByPersonNamObjectVersionNumber12 | OBJECT_VERSION_NUMBER | — | — |
| 183 | IntLegProcCreatedByPersonNamOrderName4 | ORDER_NAME | — | — |
| 184 | IntLegProcCreatedByPersonNamPersonId12 | PERSON_ID | — | — |
| 185 | IntLegProcCreatedByPersonNamPersonNameId4 | PERSON_NAME_ID | — | — |
| 186 | IntLegProcCreatedByPersonNamPreNameAdjunct4 | PRE_NAME_ADJUNCT | — | — |
| 187 | IntLegProcCreatedByPersonNamPreviousLastName4 | PREVIOUS_LAST_NAME | — | — |
| 188 | IntLegProcCreatedByPersonNamSuffix4 | SUFFIX | — | — |
| 189 | IntLegProcCreatedByPersonNamTitle4 | TITLE | — | — |
| 190 | IntLegProcLUpdtdByPersonNameBusinessGroupId13 | BUSINESS_GROUP_ID | — | — |
| 191 | IntLegProcLUpdtdByPersonNameCreatedBy13 | CREATED_BY | — | — |
| 192 | IntLegProcLUpdtdByPersonNameCreationDate13 | CREATION_DATE | — | — |
| 193 | IntLegProcLUpdtdByPersonNameDisplayName5 | DISPLAY_NAME | — | — |
| 194 | IntLegProcLUpdtdByPersonNameEffectiveEndDate5 | EFFECTIVE_END_DATE | — | — |
| 195 | IntLegProcLUpdtdByPersonNameEffectiveStartDate5 | EFFECTIVE_START_DATE | — | — |
| 196 | IntLegProcLUpdtdByPersonNameFirstName5 | FIRST_NAME | — | — |
| 197 | IntLegProcLUpdtdByPersonNameFullName5 | FULL_NAME | — | ✅ |
| 198 | IntLegProcLUpdtdByPersonNameHonors5 | HONORS | — | — |
| 199 | IntLegProcLUpdtdByPersonNameKnownAs5 | KNOWN_AS | — | — |
| 200 | IntLegProcLUpdtdByPersonNameLastName5 | LAST_NAME | — | — |
| 201 | IntLegProcLUpdtdByPersonNameLastUpdateDate13 | LAST_UPDATE_DATE | — | — |
| 202 | IntLegProcLUpdtdByPersonNameLastUpdateLogin13 | LAST_UPDATE_LOGIN | — | — |
| 203 | IntLegProcLUpdtdByPersonNameLastUpdatedBy13 | LAST_UPDATED_BY | — | — |
| 204 | IntLegProcLUpdtdByPersonNameLegislationCode5 | LEGISLATION_CODE | — | — |
| 205 | IntLegProcLUpdtdByPersonNameListName5 | LIST_NAME | — | — |
| 206 | IntLegProcLUpdtdByPersonNameMiddleNames5 | MIDDLE_NAMES | — | — |
| 207 | IntLegProcLUpdtdByPersonNameMilitaryRank5 | MILITARY_RANK | — | — |
| 208 | IntLegProcLUpdtdByPersonNameNameType5 | NAME_TYPE | — | — |
| 209 | IntLegProcLUpdtdByPersonNameObjectVersionNumber13 | OBJECT_VERSION_NUMBER | — | — |
| 210 | IntLegProcLUpdtdByPersonNameOrderName5 | ORDER_NAME | — | — |
| 211 | IntLegProcLUpdtdByPersonNamePersonId13 | PERSON_ID | — | — |
| 212 | IntLegProcLUpdtdByPersonNamePersonNameId5 | PERSON_NAME_ID | — | — |
| 213 | IntLegProcLUpdtdByPersonNamePreNameAdjunct5 | PRE_NAME_ADJUNCT | — | — |
| 214 | IntLegProcLUpdtdByPersonNamePreviousLastName5 | PREVIOUS_LAST_NAME | — | — |
| 215 | IntLegProcLUpdtdByPersonNameSuffix5 | SUFFIX | — | — |
| 216 | IntLegProcLUpdtdByPersonNameTitle5 | TITLE | — | — |
| 217 | IntLinesCreatedByPersonNameDBusinessGroupId10 | BUSINESS_GROUP_ID | — | — |
| 218 | IntLinesCreatedByPersonNameDCreatedBy10 | CREATED_BY | — | — |
| 219 | IntLinesCreatedByPersonNameDCreationDate10 | CREATION_DATE | — | — |
| 220 | IntLinesCreatedByPersonNameDDisplayName2 | DISPLAY_NAME | — | — |
| 221 | IntLinesCreatedByPersonNameDEffectiveEndDate2 | EFFECTIVE_END_DATE | — | — |
| 222 | IntLinesCreatedByPersonNameDEffectiveStartDate2 | EFFECTIVE_START_DATE | — | — |
| 223 | IntLinesCreatedByPersonNameDFirstName2 | FIRST_NAME | — | — |
| 224 | IntLinesCreatedByPersonNameDFullName2 | FULL_NAME | — | ✅ |
| 225 | IntLinesCreatedByPersonNameDHonors2 | HONORS | — | — |
| 226 | IntLinesCreatedByPersonNameDKnownAs2 | KNOWN_AS | — | — |
| 227 | IntLinesCreatedByPersonNameDLastName2 | LAST_NAME | — | — |
| 228 | IntLinesCreatedByPersonNameDLastUpdateDate10 | LAST_UPDATE_DATE | — | — |
| 229 | IntLinesCreatedByPersonNameDLastUpdateLogin10 | LAST_UPDATE_LOGIN | — | — |
| 230 | IntLinesCreatedByPersonNameDLastUpdatedBy10 | LAST_UPDATED_BY | — | — |
| 231 | IntLinesCreatedByPersonNameDLegislationCode2 | LEGISLATION_CODE | — | — |
| 232 | IntLinesCreatedByPersonNameDListName2 | LIST_NAME | — | — |
| 233 | IntLinesCreatedByPersonNameDMiddleNames2 | MIDDLE_NAMES | — | — |
| 234 | IntLinesCreatedByPersonNameDMilitaryRank2 | MILITARY_RANK | — | — |
| 235 | IntLinesCreatedByPersonNameDNameType2 | NAME_TYPE | — | — |
| 236 | IntLinesCreatedByPersonNameDObjectVersionNumber10 | OBJECT_VERSION_NUMBER | — | — |
| 237 | IntLinesCreatedByPersonNameDOrderName2 | ORDER_NAME | — | — |
| 238 | IntLinesCreatedByPersonNameDPersonId10 | PERSON_ID | — | — |
| 239 | IntLinesCreatedByPersonNameDPersonNameId2 | PERSON_NAME_ID | — | — |
| 240 | IntLinesCreatedByPersonNameDPreNameAdjunct2 | PRE_NAME_ADJUNCT | — | — |
| 241 | IntLinesCreatedByPersonNameDPreviousLastName2 | PREVIOUS_LAST_NAME | — | — |
| 242 | IntLinesCreatedByPersonNameDSuffix2 | SUFFIX | — | — |
| 243 | IntLinesCreatedByPersonNameDTitle2 | TITLE | — | — |
| 244 | IntLinesLUpdtdByPersonNameDPBusinessGroupId11 | BUSINESS_GROUP_ID | — | — |
| 245 | IntLinesLUpdtdByPersonNameDPCreatedBy11 | CREATED_BY | — | — |
| 246 | IntLinesLUpdtdByPersonNameDPCreationDate11 | CREATION_DATE | — | — |
| 247 | IntLinesLUpdtdByPersonNameDPDisplayName3 | DISPLAY_NAME | — | — |
| 248 | IntLinesLUpdtdByPersonNameDPEffectiveEndDate3 | EFFECTIVE_END_DATE | — | — |
| 249 | IntLinesLUpdtdByPersonNameDPEffectiveStartDate3 | EFFECTIVE_START_DATE | — | — |
| 250 | IntLinesLUpdtdByPersonNameDPFirstName3 | FIRST_NAME | — | — |
| 251 | IntLinesLUpdtdByPersonNameDPFullName3 | FULL_NAME | — | ✅ |
| 252 | IntLinesLUpdtdByPersonNameDPHonors3 | HONORS | — | — |
| 253 | IntLinesLUpdtdByPersonNameDPKnownAs3 | KNOWN_AS | — | — |
| 254 | IntLinesLUpdtdByPersonNameDPLastName3 | LAST_NAME | — | — |
| 255 | IntLinesLUpdtdByPersonNameDPLastUpdateDate11 | LAST_UPDATE_DATE | — | — |
| 256 | IntLinesLUpdtdByPersonNameDPLastUpdateLogin11 | LAST_UPDATE_LOGIN | — | — |
| 257 | IntLinesLUpdtdByPersonNameDPLastUpdatedBy11 | LAST_UPDATED_BY | — | — |
| 258 | IntLinesLUpdtdByPersonNameDPLegislationCode3 | LEGISLATION_CODE | — | — |
| 259 | IntLinesLUpdtdByPersonNameDPListName3 | LIST_NAME | — | — |
| 260 | IntLinesLUpdtdByPersonNameDPMiddleNames3 | MIDDLE_NAMES | — | — |
| 261 | IntLinesLUpdtdByPersonNameDPMilitaryRank3 | MILITARY_RANK | — | — |
| 262 | IntLinesLUpdtdByPersonNameDPNameType3 | NAME_TYPE | — | — |
| 263 | IntLinesLUpdtdByPersonNameDPObjectVersionNumber11 | OBJECT_VERSION_NUMBER | — | — |
| 264 | IntLinesLUpdtdByPersonNameDPOrderName3 | ORDER_NAME | — | — |
| 265 | IntLinesLUpdtdByPersonNameDPPersonId11 | PERSON_ID | — | — |
| 266 | IntLinesLUpdtdByPersonNameDPPersonNameId3 | PERSON_NAME_ID | — | — |
| 267 | IntLinesLUpdtdByPersonNameDPPreNameAdjunct3 | PRE_NAME_ADJUNCT | — | — |
| 268 | IntLinesLUpdtdByPersonNameDPPreviousLastName3 | PREVIOUS_LAST_NAME | — | — |
| 269 | IntLinesLUpdtdByPersonNameDPSuffix3 | SUFFIX | — | — |
| 270 | IntLinesLUpdtdByPersonNameDPTitle3 | TITLE | — | — |
| 271 | IntRefCreatedByPersonNameDPEBusinessGroupId14 | BUSINESS_GROUP_ID | — | — |
| 272 | IntRefCreatedByPersonNameDPECreatedBy14 | CREATED_BY | — | — |
| 273 | IntRefCreatedByPersonNameDPECreationDate14 | CREATION_DATE | — | — |
| 274 | IntRefCreatedByPersonNameDPEDisplayName6 | DISPLAY_NAME | — | — |
| 275 | IntRefCreatedByPersonNameDPEEffectiveEndDate6 | EFFECTIVE_END_DATE | — | — |
| 276 | IntRefCreatedByPersonNameDPEEffectiveStartDate6 | EFFECTIVE_START_DATE | — | — |
| 277 | IntRefCreatedByPersonNameDPEFirstName6 | FIRST_NAME | — | — |
| 278 | IntRefCreatedByPersonNameDPEFullName6 | FULL_NAME | — | ✅ |
| 279 | IntRefCreatedByPersonNameDPEHonors6 | HONORS | — | — |
| 280 | IntRefCreatedByPersonNameDPEKnownAs6 | KNOWN_AS | — | — |
| 281 | IntRefCreatedByPersonNameDPELastName6 | LAST_NAME | — | — |
| 282 | IntRefCreatedByPersonNameDPELastUpdateDate14 | LAST_UPDATE_DATE | — | — |
| 283 | IntRefCreatedByPersonNameDPELastUpdateLogin14 | LAST_UPDATE_LOGIN | — | — |
| 284 | IntRefCreatedByPersonNameDPELastUpdatedBy14 | LAST_UPDATED_BY | — | — |
| 285 | IntRefCreatedByPersonNameDPELegislationCode6 | LEGISLATION_CODE | — | — |
| 286 | IntRefCreatedByPersonNameDPEListName6 | LIST_NAME | — | — |
| 287 | IntRefCreatedByPersonNameDPEMiddleNames6 | MIDDLE_NAMES | — | — |
| 288 | IntRefCreatedByPersonNameDPEMilitaryRank6 | MILITARY_RANK | — | — |
| 289 | IntRefCreatedByPersonNameDPENameType6 | NAME_TYPE | — | — |
| 290 | IntRefCreatedByPersonNameDPEObjectVersionNumber14 | OBJECT_VERSION_NUMBER | — | — |
| 291 | IntRefCreatedByPersonNameDPEOrderName6 | ORDER_NAME | — | — |
| 292 | IntRefCreatedByPersonNameDPEPersonId14 | PERSON_ID | — | — |
| 293 | IntRefCreatedByPersonNameDPEPersonNameId6 | PERSON_NAME_ID | — | — |
| 294 | IntRefCreatedByPersonNameDPEPreNameAdjunct6 | PRE_NAME_ADJUNCT | — | — |
| 295 | IntRefCreatedByPersonNameDPEPreviousLastName6 | PREVIOUS_LAST_NAME | — | — |
| 296 | IntRefCreatedByPersonNameDPESuffix6 | SUFFIX | — | — |
| 297 | IntRefCreatedByPersonNameDPETitle6 | TITLE | — | — |
| 298 | IntRefLUpdtdByPersonNameDPEOBusinessGroupId15 | BUSINESS_GROUP_ID | — | — |
| 299 | IntRefLUpdtdByPersonNameDPEOCreatedBy15 | CREATED_BY | — | — |
| 300 | IntRefLUpdtdByPersonNameDPEOCreationDate15 | CREATION_DATE | — | — |
| 301 | IntRefLUpdtdByPersonNameDPEODisplayName7 | DISPLAY_NAME | — | — |
| 302 | IntRefLUpdtdByPersonNameDPEOEffectiveEndDate7 | EFFECTIVE_END_DATE | — | — |
| 303 | IntRefLUpdtdByPersonNameDPEOEffectiveStartDate7 | EFFECTIVE_START_DATE | — | — |
| 304 | IntRefLUpdtdByPersonNameDPEOFirstName7 | FIRST_NAME | — | — |
| 305 | IntRefLUpdtdByPersonNameDPEOFullName7 | FULL_NAME | — | ✅ |
| 306 | IntRefLUpdtdByPersonNameDPEOHonors7 | HONORS | — | — |
| 307 | IntRefLUpdtdByPersonNameDPEOKnownAs7 | KNOWN_AS | — | — |
| 308 | IntRefLUpdtdByPersonNameDPEOLastName7 | LAST_NAME | — | — |
| 309 | IntRefLUpdtdByPersonNameDPEOLastUpdateDate15 | LAST_UPDATE_DATE | — | — |
| 310 | IntRefLUpdtdByPersonNameDPEOLastUpdateLogin15 | LAST_UPDATE_LOGIN | — | — |
| 311 | IntRefLUpdtdByPersonNameDPEOLastUpdatedBy15 | LAST_UPDATED_BY | — | — |
| 312 | IntRefLUpdtdByPersonNameDPEOLegislationCode7 | LEGISLATION_CODE | — | — |
| 313 | IntRefLUpdtdByPersonNameDPEOListName7 | LIST_NAME | — | — |
| 314 | IntRefLUpdtdByPersonNameDPEOMiddleNames7 | MIDDLE_NAMES | — | — |
| 315 | IntRefLUpdtdByPersonNameDPEOMilitaryRank7 | MILITARY_RANK | — | — |
| 316 | IntRefLUpdtdByPersonNameDPEONameType7 | NAME_TYPE | — | — |
| 317 | IntRefLUpdtdByPersonNameDPEOObjectVersionNumber15 | OBJECT_VERSION_NUMBER | — | — |
| 318 | IntRefLUpdtdByPersonNameDPEOOrderName7 | ORDER_NAME | — | — |
| 319 | IntRefLUpdtdByPersonNameDPEOPersonId15 | PERSON_ID | — | — |
| 320 | IntRefLUpdtdByPersonNameDPEOPersonNameId7 | PERSON_NAME_ID | — | — |
| 321 | IntRefLUpdtdByPersonNameDPEOPreNameAdjunct7 | PRE_NAME_ADJUNCT | — | — |
| 322 | IntRefLUpdtdByPersonNameDPEOPreviousLastName7 | PREVIOUS_LAST_NAME | — | — |
| 323 | IntRefLUpdtdByPersonNameDPEOSuffix7 | SUFFIX | — | — |
| 324 | IntRefLUpdtdByPersonNameDPEOTitle7 | TITLE | — | — |
| 325 | TaxLineIntrCreatedByPersonNaBusinessGroupId2 | BUSINESS_GROUP_ID | — | — |
| 326 | TaxLineIntrCreatedByPersonNaCreatedBy2 | CREATED_BY | — | — |
| 327 | TaxLineIntrCreatedByPersonNaCreationDate2 | CREATION_DATE | — | — |
| 328 | TaxLineIntrCreatedByPersonNaDisplayName | DISPLAY_NAME | — | — |
| 329 | TaxLineIntrCreatedByPersonNaEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 330 | TaxLineIntrCreatedByPersonNaEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 331 | TaxLineIntrCreatedByPersonNaFirstName | FIRST_NAME | — | — |
| 332 | TaxLineIntrCreatedByPersonNaFullName | FULL_NAME | — | — |
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
| 359 | TaxLineIntrLastUpdtdByPersonFullName1 | FULL_NAME | — | — |
| 360 | TaxLineIntrLastUpdtdByPersonHonors1 | HONORS | — | — |
| 361 | TaxLineIntrLastUpdtdByPersonKnownAs1 | KNOWN_AS | — | — |
| 362 | TaxLineIntrLastUpdtdByPersonLastName1 | LAST_NAME | — | — |
| 363 | TaxLineIntrLastUpdtdByPersonLastUpdateDate3 | LAST_UPDATE_DATE | — | — |
| 364 | TaxLineIntrLastUpdtdByPersonLastUpdateLogin3 | LAST_UPDATE_LOGIN | — | — |
| 365 | TaxLineIntrLastUpdtdByPersonLegislationCode1 | LEGISLATION_CODE | — | — |
| 366 | TaxLineIntrLastUpdtdByPersonListName1 | LIST_NAME | — | — |
| 367 | TaxLineIntrLastUpdtdByPersonMiddleNames1 | MIDDLE_NAMES | — | — |
| 368 | TaxLineIntrLastUpdtdByPersonMilitaryRank1 | MILITARY_RANK | — | — |
| 369 | TaxLineIntrLastUpdtdByPersonNameType1 | NAME_TYPE | — | — |
| 370 | TaxLineIntrLastUpdtdByPersonObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 371 | TaxLineIntrLastUpdtdByPersonOrderName1 | ORDER_NAME | — | — |
| 372 | TaxLineIntrLastUpdtdByPersonPersonId3 | PERSON_ID | — | — |
| 373 | TaxLineIntrLastUpdtdByPersonPersonNameId1 | PERSON_NAME_ID | — | — |
| 374 | TaxLineIntrLastUpdtdByPersonPreNameAdjunct1 | PRE_NAME_ADJUNCT | — | — |
| 375 | TaxLineIntrLastUpdtdByPersonPreviousLastName1 | PREVIOUS_LAST_NAME | — | — |
| 376 | TaxLineIntrLastUpdtdByPersonSuffix1 | SUFFIX | — | — |
| 377 | TaxLineIntrLastUpdtdByPersonTitle1 | TITLE | — | — |

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
| 45 | FDLineIntrEOToCreatedByUserPActiveFlag2 | ACTIVE_FLAG | — | — |
| 46 | FDLineIntrEOToCreatedByUserPBusinessGroupId2 | BUSINESS_GROUP_ID | — | — |
| 47 | FDLineIntrEOToCreatedByUserPCreatedBy2 | CREATED_BY | — | — |
| 48 | FDLineIntrEOToCreatedByUserPCreationDate2 | CREATION_DATE | — | — |
| 49 | FDLineIntrEOToCreatedByUserPCredentialsEmailSent2 | CREDENTIALS_EMAIL_SENT | — | — |
| 50 | FDLineIntrEOToCreatedByUserPEndDate2 | END_DATE | — | — |
| 51 | FDLineIntrEOToCreatedByUserPExternalId2 | EXTERNAL_ID | — | — |
| 52 | FDLineIntrEOToCreatedByUserPHrTerminated2 | HR_TERMINATED | — | — |
| 53 | FDLineIntrEOToCreatedByUserPLastUpdateDate2 | LAST_UPDATE_DATE | — | — |
| 54 | FDLineIntrEOToCreatedByUserPLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 55 | FDLineIntrEOToCreatedByUserPLastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 56 | FDLineIntrEOToCreatedByUserPMultitenancyUsername2 | MULTITENANCY_USERNAME | — | — |
| 57 | FDLineIntrEOToCreatedByUserPObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 58 | FDLineIntrEOToCreatedByUserPPartyId2 | PARTY_ID | — | — |
| 59 | FDLineIntrEOToCreatedByUserPPersonId2 | PERSON_ID | — | — |
| 60 | FDLineIntrEOToCreatedByUserPStartDate2 | START_DATE | — | — |
| 61 | FDLineIntrEOToCreatedByUserPSuspended2 | SUSPENDED | — | — |
| 62 | FDLineIntrEOToCreatedByUserPUserDataChecksum2 | USER_DATA_CHECKSUM | — | — |
| 63 | FDLineIntrEOToCreatedByUserPUserDistinguishedName2 | USER_DISTINGUISHED_NAME | — | — |
| 64 | FDLineIntrEOToCreatedByUserPUserGuid2 | USER_GUID | — | — |
| 65 | FDLineIntrEOToCreatedByUserPUserId2 | USER_ID | — | — |
| 66 | FDLineIntrEOToCreatedByUserPUsername2 | USERNAME | — | — |
| 67 | FDLineIntrToLastUpdtdByUserPActiveFlag3 | ACTIVE_FLAG | — | — |
| 68 | FDLineIntrToLastUpdtdByUserPBusinessGroupId3 | BUSINESS_GROUP_ID | — | — |
| 69 | FDLineIntrToLastUpdtdByUserPCreatedBy3 | CREATED_BY | — | — |
| 70 | FDLineIntrToLastUpdtdByUserPCreationDate3 | CREATION_DATE | — | — |
| 71 | FDLineIntrToLastUpdtdByUserPCredentialsEmailSent3 | CREDENTIALS_EMAIL_SENT | — | — |
| 72 | FDLineIntrToLastUpdtdByUserPEndDate3 | END_DATE | — | — |
| 73 | FDLineIntrToLastUpdtdByUserPExternalId3 | EXTERNAL_ID | — | — |
| 74 | FDLineIntrToLastUpdtdByUserPHrTerminated3 | HR_TERMINATED | — | — |
| 75 | FDLineIntrToLastUpdtdByUserPLastUpdateDate3 | LAST_UPDATE_DATE | — | — |
| 76 | FDLineIntrToLastUpdtdByUserPLastUpdateLogin3 | LAST_UPDATE_LOGIN | — | — |
| 77 | FDLineIntrToLastUpdtdByUserPLastUpdatedBy3 | LAST_UPDATED_BY | — | — |
| 78 | FDLineIntrToLastUpdtdByUserPMultitenancyUsername3 | MULTITENANCY_USERNAME | — | — |
| 79 | FDLineIntrToLastUpdtdByUserPObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 80 | FDLineIntrToLastUpdtdByUserPPartyId3 | PARTY_ID | — | — |
| 81 | FDLineIntrToLastUpdtdByUserPPersonId3 | PERSON_ID | — | — |
| 82 | FDLineIntrToLastUpdtdByUserPStartDate3 | START_DATE | — | — |
| 83 | FDLineIntrToLastUpdtdByUserPSuspended3 | SUSPENDED | — | — |
| 84 | FDLineIntrToLastUpdtdByUserPUserDataChecksum3 | USER_DATA_CHECKSUM | — | — |
| 85 | FDLineIntrToLastUpdtdByUserPUserDistinguishedName3 | USER_DISTINGUISHED_NAME | — | — |
| 86 | FDLineIntrToLastUpdtdByUserPUserGuid3 | USER_GUID | — | — |
| 87 | FDLineIntrToLastUpdtdByUserPUserId3 | USER_ID | — | — |
| 88 | FDLineIntrToLastUpdtdByUserPUsername3 | USERNAME | — | — |
| 89 | IntHdrsCreatedByUserPEOActiveFlag | ACTIVE_FLAG | — | — |
| 90 | IntHdrsCreatedByUserPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 91 | IntHdrsCreatedByUserPEOCreatedBy | CREATED_BY | — | — |
| 92 | IntHdrsCreatedByUserPEOCreationDate | CREATION_DATE | — | — |
| 93 | IntHdrsCreatedByUserPEOCredentialsEmailSent | CREDENTIALS_EMAIL_SENT | — | — |
| 94 | IntHdrsCreatedByUserPEOEndDate | END_DATE | — | — |
| 95 | IntHdrsCreatedByUserPEOExternalId | EXTERNAL_ID | — | — |
| 96 | IntHdrsCreatedByUserPEOHrTerminated | HR_TERMINATED | — | — |
| 97 | IntHdrsCreatedByUserPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 98 | IntHdrsCreatedByUserPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 99 | IntHdrsCreatedByUserPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 100 | IntHdrsCreatedByUserPEOMultitenancyUsername | MULTITENANCY_USERNAME | — | — |
| 101 | IntHdrsCreatedByUserPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 102 | IntHdrsCreatedByUserPEOPartyId | PARTY_ID | — | — |
| 103 | IntHdrsCreatedByUserPEOPersonId | PERSON_ID | — | — |
| 104 | IntHdrsCreatedByUserPEOStartDate | START_DATE | — | — |
| 105 | IntHdrsCreatedByUserPEOSuspended | SUSPENDED | — | — |
| 106 | IntHdrsCreatedByUserPEOUserDataChecksum | USER_DATA_CHECKSUM | — | — |
| 107 | IntHdrsCreatedByUserPEOUserDistinguishedName | USER_DISTINGUISHED_NAME | — | — |
| 108 | IntHdrsCreatedByUserPEOUserGuid | USER_GUID | — | — |
| 109 | IntHdrsCreatedByUserPEOUserId | USER_ID | — | — |
| 110 | IntHdrsCreatedByUserPEOUsername | USERNAME | — | — |
| 111 | IntHdrsLUpdtdByUserPEOActiveFlag1 | ACTIVE_FLAG | — | — |
| 112 | IntHdrsLUpdtdByUserPEOBusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 113 | IntHdrsLUpdtdByUserPEOCreatedBy1 | CREATED_BY | — | — |
| 114 | IntHdrsLUpdtdByUserPEOCreationDate1 | CREATION_DATE | — | — |
| 115 | IntHdrsLUpdtdByUserPEOCredentialsEmailSent1 | CREDENTIALS_EMAIL_SENT | — | — |
| 116 | IntHdrsLUpdtdByUserPEOEndDate1 | END_DATE | — | — |
| 117 | IntHdrsLUpdtdByUserPEOExternalId1 | EXTERNAL_ID | — | — |
| 118 | IntHdrsLUpdtdByUserPEOHrTerminated1 | HR_TERMINATED | — | — |
| 119 | IntHdrsLUpdtdByUserPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | — |
| 120 | IntHdrsLUpdtdByUserPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 121 | IntHdrsLUpdtdByUserPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 122 | IntHdrsLUpdtdByUserPEOMultitenancyUsername1 | MULTITENANCY_USERNAME | — | — |
| 123 | IntHdrsLUpdtdByUserPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 124 | IntHdrsLUpdtdByUserPEOPartyId1 | PARTY_ID | — | — |
| 125 | IntHdrsLUpdtdByUserPEOPersonId1 | PERSON_ID | — | — |
| 126 | IntHdrsLUpdtdByUserPEOStartDate1 | START_DATE | — | — |
| 127 | IntHdrsLUpdtdByUserPEOSuspended1 | SUSPENDED | — | — |
| 128 | IntHdrsLUpdtdByUserPEOUserDataChecksum1 | USER_DATA_CHECKSUM | — | — |
| 129 | IntHdrsLUpdtdByUserPEOUserDistinguishedName1 | USER_DISTINGUISHED_NAME | — | — |
| 130 | IntHdrsLUpdtdByUserPEOUserGuid1 | USER_GUID | — | — |
| 131 | IntHdrsLUpdtdByUserPEOUserId1 | USER_ID | — | — |
| 132 | IntHdrsLUpdtdByUserPEOUsername1 | USERNAME | — | — |
| 133 | IntLegalProcCreatedByUserPEOActiveFlag4 | ACTIVE_FLAG | — | — |
| 134 | IntLegalProcCreatedByUserPEOBusinessGroupId4 | BUSINESS_GROUP_ID | — | — |
| 135 | IntLegalProcCreatedByUserPEOCreatedBy4 | CREATED_BY | — | — |
| 136 | IntLegalProcCreatedByUserPEOCreationDate4 | CREATION_DATE | — | — |
| 137 | IntLegalProcCreatedByUserPEOCredentialsEmailSent4 | CREDENTIALS_EMAIL_SENT | — | — |
| 138 | IntLegalProcCreatedByUserPEOEndDate4 | END_DATE | — | — |
| 139 | IntLegalProcCreatedByUserPEOExternalId4 | EXTERNAL_ID | — | — |
| 140 | IntLegalProcCreatedByUserPEOHrTerminated4 | HR_TERMINATED | — | — |
| 141 | IntLegalProcCreatedByUserPEOLastUpdateDate4 | LAST_UPDATE_DATE | — | — |
| 142 | IntLegalProcCreatedByUserPEOLastUpdateLogin4 | LAST_UPDATE_LOGIN | — | — |
| 143 | IntLegalProcCreatedByUserPEOLastUpdatedBy4 | LAST_UPDATED_BY | — | — |
| 144 | IntLegalProcCreatedByUserPEOMultitenancyUsername4 | MULTITENANCY_USERNAME | — | — |
| 145 | IntLegalProcCreatedByUserPEOObjectVersionNumber4 | OBJECT_VERSION_NUMBER | — | — |
| 146 | IntLegalProcCreatedByUserPEOPartyId4 | PARTY_ID | — | — |
| 147 | IntLegalProcCreatedByUserPEOPersonId4 | PERSON_ID | — | — |
| 148 | IntLegalProcCreatedByUserPEOStartDate4 | START_DATE | — | — |
| 149 | IntLegalProcCreatedByUserPEOSuspended4 | SUSPENDED | — | — |
| 150 | IntLegalProcCreatedByUserPEOUserDataChecksum4 | USER_DATA_CHECKSUM | — | — |
| 151 | IntLegalProcCreatedByUserPEOUserDistinguishedName4 | USER_DISTINGUISHED_NAME | — | — |
| 152 | IntLegalProcCreatedByUserPEOUserGuid4 | USER_GUID | — | — |
| 153 | IntLegalProcCreatedByUserPEOUserId4 | USER_ID | — | — |
| 154 | IntLegalProcCreatedByUserPEOUsername4 | USERNAME | — | — |
| 155 | IntLegalProcLUpdtdByUserPEOActiveFlag5 | ACTIVE_FLAG | — | — |
| 156 | IntLegalProcLUpdtdByUserPEOBusinessGroupId5 | BUSINESS_GROUP_ID | — | — |
| 157 | IntLegalProcLUpdtdByUserPEOCreatedBy5 | CREATED_BY | — | — |
| 158 | IntLegalProcLUpdtdByUserPEOCreationDate5 | CREATION_DATE | — | — |
| 159 | IntLegalProcLUpdtdByUserPEOCredentialsEmailSent5 | CREDENTIALS_EMAIL_SENT | — | — |
| 160 | IntLegalProcLUpdtdByUserPEOEndDate5 | END_DATE | — | — |
| 161 | IntLegalProcLUpdtdByUserPEOExternalId5 | EXTERNAL_ID | — | — |
| 162 | IntLegalProcLUpdtdByUserPEOHrTerminated5 | HR_TERMINATED | — | — |
| 163 | IntLegalProcLUpdtdByUserPEOLastUpdateDate5 | LAST_UPDATE_DATE | — | — |
| 164 | IntLegalProcLUpdtdByUserPEOLastUpdateLogin5 | LAST_UPDATE_LOGIN | — | — |
| 165 | IntLegalProcLUpdtdByUserPEOLastUpdatedBy5 | LAST_UPDATED_BY | — | — |
| 166 | IntLegalProcLUpdtdByUserPEOMultitenancyUsername5 | MULTITENANCY_USERNAME | — | — |
| 167 | IntLegalProcLUpdtdByUserPEOObjectVersionNumber5 | OBJECT_VERSION_NUMBER | — | — |
| 168 | IntLegalProcLUpdtdByUserPEOPartyId5 | PARTY_ID | — | — |
| 169 | IntLegalProcLUpdtdByUserPEOPersonId5 | PERSON_ID | — | — |
| 170 | IntLegalProcLUpdtdByUserPEOStartDate5 | START_DATE | — | — |
| 171 | IntLegalProcLUpdtdByUserPEOSuspended5 | SUSPENDED | — | — |
| 172 | IntLegalProcLUpdtdByUserPEOUserDataChecksum5 | USER_DATA_CHECKSUM | — | — |
| 173 | IntLegalProcLUpdtdByUserPEOUserDistinguishedName5 | USER_DISTINGUISHED_NAME | — | — |
| 174 | IntLegalProcLUpdtdByUserPEOUserGuid5 | USER_GUID | — | — |
| 175 | IntLegalProcLUpdtdByUserPEOUserId5 | USER_ID | — | — |
| 176 | IntLegalProcLUpdtdByUserPEOUsername5 | USERNAME | — | — |
| 177 | IntLinesCreatedByUserPEOActiveFlag2 | ACTIVE_FLAG | — | — |
| 178 | IntLinesCreatedByUserPEOBusinessGroupId2 | BUSINESS_GROUP_ID | — | — |
| 179 | IntLinesCreatedByUserPEOCreatedBy2 | CREATED_BY | — | — |
| 180 | IntLinesCreatedByUserPEOCreationDate2 | CREATION_DATE | — | — |
| 181 | IntLinesCreatedByUserPEOCredentialsEmailSent2 | CREDENTIALS_EMAIL_SENT | — | — |
| 182 | IntLinesCreatedByUserPEOEndDate2 | END_DATE | — | — |
| 183 | IntLinesCreatedByUserPEOExternalId2 | EXTERNAL_ID | — | — |
| 184 | IntLinesCreatedByUserPEOHrTerminated2 | HR_TERMINATED | — | — |
| 185 | IntLinesCreatedByUserPEOLastUpdateDate2 | LAST_UPDATE_DATE | — | — |
| 186 | IntLinesCreatedByUserPEOLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 187 | IntLinesCreatedByUserPEOLastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 188 | IntLinesCreatedByUserPEOMultitenancyUsername2 | MULTITENANCY_USERNAME | — | — |
| 189 | IntLinesCreatedByUserPEOObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 190 | IntLinesCreatedByUserPEOPartyId2 | PARTY_ID | — | — |
| 191 | IntLinesCreatedByUserPEOPersonId2 | PERSON_ID | — | — |
| 192 | IntLinesCreatedByUserPEOStartDate2 | START_DATE | — | — |
| 193 | IntLinesCreatedByUserPEOSuspended2 | SUSPENDED | — | — |
| 194 | IntLinesCreatedByUserPEOUserDataChecksum2 | USER_DATA_CHECKSUM | — | — |
| 195 | IntLinesCreatedByUserPEOUserDistinguishedName2 | USER_DISTINGUISHED_NAME | — | — |
| 196 | IntLinesCreatedByUserPEOUserGuid2 | USER_GUID | — | — |
| 197 | IntLinesCreatedByUserPEOUserId2 | USER_ID | — | — |
| 198 | IntLinesCreatedByUserPEOUsername2 | USERNAME | — | — |
| 199 | IntLinesLUpdtdByUserPEOActiveFlag3 | ACTIVE_FLAG | — | — |
| 200 | IntLinesLUpdtdByUserPEOBusinessGroupId3 | BUSINESS_GROUP_ID | — | — |
| 201 | IntLinesLUpdtdByUserPEOCreatedBy3 | CREATED_BY | — | — |
| 202 | IntLinesLUpdtdByUserPEOCreationDate3 | CREATION_DATE | — | — |
| 203 | IntLinesLUpdtdByUserPEOCredentialsEmailSent3 | CREDENTIALS_EMAIL_SENT | — | — |
| 204 | IntLinesLUpdtdByUserPEOEndDate3 | END_DATE | — | — |
| 205 | IntLinesLUpdtdByUserPEOExternalId3 | EXTERNAL_ID | — | — |
| 206 | IntLinesLUpdtdByUserPEOHrTerminated3 | HR_TERMINATED | — | — |
| 207 | IntLinesLUpdtdByUserPEOLastUpdateDate3 | LAST_UPDATE_DATE | — | — |
| 208 | IntLinesLUpdtdByUserPEOLastUpdateLogin3 | LAST_UPDATE_LOGIN | — | — |
| 209 | IntLinesLUpdtdByUserPEOLastUpdatedBy3 | LAST_UPDATED_BY | — | — |
| 210 | IntLinesLUpdtdByUserPEOMultitenancyUsername3 | MULTITENANCY_USERNAME | — | — |
| 211 | IntLinesLUpdtdByUserPEOObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 212 | IntLinesLUpdtdByUserPEOPartyId3 | PARTY_ID | — | — |
| 213 | IntLinesLUpdtdByUserPEOPersonId3 | PERSON_ID | — | — |
| 214 | IntLinesLUpdtdByUserPEOStartDate3 | START_DATE | — | — |
| 215 | IntLinesLUpdtdByUserPEOSuspended3 | SUSPENDED | — | — |
| 216 | IntLinesLUpdtdByUserPEOUserDataChecksum3 | USER_DATA_CHECKSUM | — | — |
| 217 | IntLinesLUpdtdByUserPEOUserDistinguishedName3 | USER_DISTINGUISHED_NAME | — | — |
| 218 | IntLinesLUpdtdByUserPEOUserGuid3 | USER_GUID | — | — |
| 219 | IntLinesLUpdtdByUserPEOUserId3 | USER_ID | — | — |
| 220 | IntLinesLUpdtdByUserPEOUsername3 | USERNAME | — | — |
| 221 | IntRefCreatedByUserPEOActiveFlag6 | ACTIVE_FLAG | — | — |
| 222 | IntRefCreatedByUserPEOBusinessGroupId6 | BUSINESS_GROUP_ID | — | — |
| 223 | IntRefCreatedByUserPEOCreatedBy6 | CREATED_BY | — | — |
| 224 | IntRefCreatedByUserPEOCreationDate6 | CREATION_DATE | — | — |
| 225 | IntRefCreatedByUserPEOCredentialsEmailSent6 | CREDENTIALS_EMAIL_SENT | — | — |
| 226 | IntRefCreatedByUserPEOEndDate6 | END_DATE | — | — |
| 227 | IntRefCreatedByUserPEOExternalId6 | EXTERNAL_ID | — | — |
| 228 | IntRefCreatedByUserPEOHrTerminated6 | HR_TERMINATED | — | — |
| 229 | IntRefCreatedByUserPEOLastUpdateDate6 | LAST_UPDATE_DATE | — | — |
| 230 | IntRefCreatedByUserPEOLastUpdateLogin6 | LAST_UPDATE_LOGIN | — | — |
| 231 | IntRefCreatedByUserPEOLastUpdatedBy6 | LAST_UPDATED_BY | — | — |
| 232 | IntRefCreatedByUserPEOMultitenancyUsername6 | MULTITENANCY_USERNAME | — | — |
| 233 | IntRefCreatedByUserPEOObjectVersionNumber6 | OBJECT_VERSION_NUMBER | — | — |
| 234 | IntRefCreatedByUserPEOPartyId6 | PARTY_ID | — | — |
| 235 | IntRefCreatedByUserPEOPersonId6 | PERSON_ID | — | — |
| 236 | IntRefCreatedByUserPEOStartDate6 | START_DATE | — | — |
| 237 | IntRefCreatedByUserPEOSuspended6 | SUSPENDED | — | — |
| 238 | IntRefCreatedByUserPEOUserDataChecksum6 | USER_DATA_CHECKSUM | — | — |
| 239 | IntRefCreatedByUserPEOUserDistinguishedName6 | USER_DISTINGUISHED_NAME | — | — |
| 240 | IntRefCreatedByUserPEOUserGuid6 | USER_GUID | — | — |
| 241 | IntRefCreatedByUserPEOUserId6 | USER_ID | — | — |
| 242 | IntRefCreatedByUserPEOUsername6 | USERNAME | — | — |
| 243 | IntRefLUpdtdByUserPEOActiveFlag7 | ACTIVE_FLAG | — | — |
| 244 | IntRefLUpdtdByUserPEOBusinessGroupId7 | BUSINESS_GROUP_ID | — | — |
| 245 | IntRefLUpdtdByUserPEOCreatedBy7 | CREATED_BY | — | — |
| 246 | IntRefLUpdtdByUserPEOCreationDate7 | CREATION_DATE | — | — |
| 247 | IntRefLUpdtdByUserPEOCredentialsEmailSent7 | CREDENTIALS_EMAIL_SENT | — | — |
| 248 | IntRefLUpdtdByUserPEOEndDate7 | END_DATE | — | — |
| 249 | IntRefLUpdtdByUserPEOExternalId7 | EXTERNAL_ID | — | — |
| 250 | IntRefLUpdtdByUserPEOHrTerminated7 | HR_TERMINATED | — | — |
| 251 | IntRefLUpdtdByUserPEOLastUpdateDate7 | LAST_UPDATE_DATE | — | — |
| 252 | IntRefLUpdtdByUserPEOLastUpdateLogin7 | LAST_UPDATE_LOGIN | — | — |
| 253 | IntRefLUpdtdByUserPEOLastUpdatedBy7 | LAST_UPDATED_BY | — | — |
| 254 | IntRefLUpdtdByUserPEOMultitenancyUsername7 | MULTITENANCY_USERNAME | — | — |
| 255 | IntRefLUpdtdByUserPEOObjectVersionNumber7 | OBJECT_VERSION_NUMBER | — | — |
| 256 | IntRefLUpdtdByUserPEOPartyId7 | PARTY_ID | — | — |
| 257 | IntRefLUpdtdByUserPEOPersonId7 | PERSON_ID | — | — |
| 258 | IntRefLUpdtdByUserPEOStartDate7 | START_DATE | — | — |
| 259 | IntRefLUpdtdByUserPEOSuspended7 | SUSPENDED | — | — |
| 260 | IntRefLUpdtdByUserPEOUserDataChecksum7 | USER_DATA_CHECKSUM | — | — |
| 261 | IntRefLUpdtdByUserPEOUserDistinguishedName7 | USER_DISTINGUISHED_NAME | — | — |
| 262 | IntRefLUpdtdByUserPEOUserGuid7 | USER_GUID | — | — |
| 263 | IntRefLUpdtdByUserPEOUserId7 | USER_ID | — | — |
| 264 | IntRefLUpdtdByUserPEOUsername7 | USERNAME | — | — |
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
| 6 | LineIntendedUsePEOName | NAME | — | ✅ |

### [[zx_fc_product_categories_v|ZX_FC_PRODUCT_CATEGORIES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProductCategoriesPEOClassificationCode | CLASSIFICATION_CODE | — | — |
| 2 | ProductCategoriesPEOClassificationId1 | CLASSIFICATION_ID | — | — |
| 3 | ProductCategoriesPEOClassificationName | CLASSIFICATION_NAME | — | ✅ |
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
| 4 | ProductFiscClassificationsPE1ClassificationName1 | CLASSIFICATION_NAME | — | ✅ |
| 5 | ProductFiscClassificationsPE1CountryCode2 | COUNTRY_CODE | — | — |
| 6 | ProductFiscClassificationsPE1EffectiveTo2 | EFFECTIVE_TO | — | — |
| 7 | ProductFiscClassificationsPE1StructureId | STRUCTURE_ID | — | — |
| 8 | ProductFiscClassificationsPE1StructureName | STRUCTURE_NAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
