---
id: DOC-OTHER-PVO-LegalDocumentAssocP1
doc_type: system-doc
title: "LegalDocumentAssocP1 — PVO Cross-Module"
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
  - LegalDocumentAssocP1
  - legaldocumentassocp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LegalDocumentAssocP1

## 📌 Visão Geral

View Object para extração BICC de dados de Legal Document Assoc P1. Acessa as tabelas: CMF_FD_LOC_INFO_PERSIST_OTBI_V, CMF_FISCAL_DOC_HEADERS, CMF_LEGAL_DOC_ASSOCIATIONS (+6).

**Caminho:** `FscmTopModelAM.FiscalDocumentAM.LegalDocumentAssocP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 515 | 9 | 1 | 7 | 1% |

---

## 🔗 Tabelas Relacionadas

- [[cmf_fd_loc_info_persist_otbi_v|CMF_FD_LOC_INFO_PERSIST_OTBI_V]] — 79 atributos
- [[cmf_fiscal_doc_headers|CMF_FISCAL_DOC_HEADERS]] — 59 atributos
- [[cmf_legal_doc_associations|CMF_LEGAL_DOC_ASSOCIATIONS]] — 15 atributos (1 PKs, 5 BICC)
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 21 atributos
- [[jg_fscl_hdrs_atrb_ext_all|JG_FSCL_HDRS_ATRB_EXT_ALL]] — 55 atributos
- [[jg_fscl_hdr_dtls_atrb_ext_all|JG_FSCL_HDR_DTLS_ATRB_EXT_ALL]] — 18 atributos
- [[jg_fscl_tax_lines_all|JG_FSCL_TAX_LINES_ALL]] — 72 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 108 atributos (2 BICC)
- [[per_users|PER_USERS]] — 88 atributos

---

## ⚙️ Atributos

### [[cmf_fd_loc_info_persist_otbi_v|CMF_FD_LOC_INFO_PERSIST_OTBI_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocLocInfoPersistPEODocumentHeaderId2 | DOCUMENT_HEADER_ID | — | — |
| 2 | FiscalDocLocInfoPersistPEODocumentNumber1 | DOCUMENT_NUMBER | — | — |
| 3 | FiscalDocLocInfoPersistPEOFiscalProcOptionsId1 | FISCAL_PROC_OPTIONS_ID | — | — |
| 4 | FiscalDocLocInfoPersistPEOIssuerCustomerFormTaxNum | ISSUER_CUSTOMER_FORM_TAX_NUM | — | — |
| 5 | FiscalDocLocInfoPersistPEOIssuerCustomerLocationId | ISSUER_CUSTOMER_LOCATION_ID | — | — |
| 6 | FiscalDocLocInfoPersistPEOIssuerCustomerPartyId | ISSUER_CUSTOMER_PARTY_ID | — | — |
| 7 | FiscalDocLocInfoPersistPEOIssuerCustomerPartySiteId | ISSUER_CUSTOMER_PARTY_SITE_ID | — | — |
| 8 | FiscalDocLocInfoPersistPEOIssuerCustomerTaxId | ISSUER_CUSTOMER_TAX_ID | — | — |
| 9 | FiscalDocLocInfoPersistPEOIssuerCustomerTaxpayerId | ISSUER_CUSTOMER_TAXPAYER_ID | — | — |
| 10 | FiscalDocLocInfoPersistPEOIssuerLeFormTaxNumber | ISSUER_LE_FORM_TAX_NUMBER | — | — |
| 11 | FiscalDocLocInfoPersistPEOIssuerLeId | ISSUER_LE_ID | — | — |
| 12 | FiscalDocLocInfoPersistPEOIssuerLeLocationId | ISSUER_LE_LOCATION_ID | — | — |
| 13 | FiscalDocLocInfoPersistPEOIssuerLeSiteId | ISSUER_LE_SITE_ID | — | — |
| 14 | FiscalDocLocInfoPersistPEOIssuerLeTaxId | ISSUER_LE_TAX_ID | — | — |
| 15 | FiscalDocLocInfoPersistPEOIssuerLeTaxpayerId | ISSUER_LE_TAXPAYER_ID | — | — |
| 16 | FiscalDocLocInfoPersistPEOIssuerSupplierFormTaxNum | ISSUER_SUPPLIER_FORM_TAX_NUM | — | — |
| 17 | FiscalDocLocInfoPersistPEOIssuerSupplierLocationId | ISSUER_SUPPLIER_LOCATION_ID | — | — |
| 18 | FiscalDocLocInfoPersistPEOIssuerSupplierPartyId | ISSUER_SUPPLIER_PARTY_ID | — | — |
| 19 | FiscalDocLocInfoPersistPEOIssuerSupplierPartySiteId | ISSUER_SUPPLIER_PARTY_SITE_ID | — | — |
| 20 | FiscalDocLocInfoPersistPEOIssuerSupplierTaxId | ISSUER_SUPPLIER_TAX_ID | — | — |
| 21 | FiscalDocLocInfoPersistPEOIssuerSupplierTaxpayerId | ISSUER_SUPPLIER_TAXPAYER_ID | — | — |
| 22 | FiscalDocLocInfoPersistPEOIssuerType | ISSUER_TYPE | — | — |
| 23 | FiscalDocLocInfoPersistPEOReceiverCustPartySiteId | RECEIVER_CUST_PARTY_SITE_ID | — | — |
| 24 | FiscalDocLocInfoPersistPEOReceiverCustomerFormTaxNum | RECEIVER_CUSTOMER_FORM_TAX_NUM | — | — |
| 25 | FiscalDocLocInfoPersistPEOReceiverCustomerLocationId | RECEIVER_CUSTOMER_LOCATION_ID | — | — |
| 26 | FiscalDocLocInfoPersistPEOReceiverCustomerPartyId | RECEIVER_CUSTOMER_PARTY_ID | — | — |
| 27 | FiscalDocLocInfoPersistPEOReceiverCustomerTaxId | RECEIVER_CUSTOMER_TAX_ID | — | — |
| 28 | FiscalDocLocInfoPersistPEOReceiverCustomerTaxpayerId | RECEIVER_CUSTOMER_TAXPAYER_ID | — | — |
| 29 | FiscalDocLocInfoPersistPEOReceiverLeFormTaxNumber | RECEIVER_LE_FORM_TAX_NUMBER | — | — |
| 30 | FiscalDocLocInfoPersistPEOReceiverLeLocationId | RECEIVER_LE_LOCATION_ID | — | — |
| 31 | FiscalDocLocInfoPersistPEOReceiverLePartyId | RECEIVER_LE_PARTY_ID | — | — |
| 32 | FiscalDocLocInfoPersistPEOReceiverLePartySiteId | RECEIVER_LE_PARTY_SITE_ID | — | — |
| 33 | FiscalDocLocInfoPersistPEOReceiverLeTaxId | RECEIVER_LE_TAX_ID | — | — |
| 34 | FiscalDocLocInfoPersistPEOReceiverLeTaxpayerId | RECEIVER_LE_TAXPAYER_ID | — | — |
| 35 | FiscalDocLocInfoPersistPEOReceiverSuppPartySiteId | RECEIVER_SUPP_PARTY_SITE_ID | — | — |
| 36 | FiscalDocLocInfoPersistPEOReceiverSupplierFormTaxNum | RECEIVER_SUPPLIER_FORM_TAX_NUM | — | — |
| 37 | FiscalDocLocInfoPersistPEOReceiverSupplierLocationId | RECEIVER_SUPPLIER_LOCATION_ID | — | — |
| 38 | FiscalDocLocInfoPersistPEOReceiverSupplierPartyId | RECEIVER_SUPPLIER_PARTY_ID | — | — |
| 39 | FiscalDocLocInfoPersistPEOReceiverSupplierTaxId | RECEIVER_SUPPLIER_TAX_ID | — | — |
| 40 | FiscalDocLocInfoPersistPEOReceiverSupplierTaxpayerId | RECEIVER_SUPPLIER_TAXPAYER_ID | — | — |
| 41 | FiscalDocLocInfoPersistPEOReceiverType | RECEIVER_TYPE | — | — |
| 42 | FiscalDocLocInfoPersistPEOShipfromCustPartySiteId | SHIPFROM_CUST_PARTY_SITE_ID | — | — |
| 43 | FiscalDocLocInfoPersistPEOShipfromCustomerFormTaxNum | SHIPFROM_CUSTOMER_FORM_TAX_NUM | — | — |
| 44 | FiscalDocLocInfoPersistPEOShipfromCustomerLocationId | SHIPFROM_CUSTOMER_LOCATION_ID | — | — |
| 45 | FiscalDocLocInfoPersistPEOShipfromCustomerPartyId | SHIPFROM_CUSTOMER_PARTY_ID | — | — |
| 46 | FiscalDocLocInfoPersistPEOShipfromCustomerTaxId | SHIPFROM_CUSTOMER_TAX_ID | — | — |
| 47 | FiscalDocLocInfoPersistPEOShipfromCustomerTaxpayerId | SHIPFROM_CUSTOMER_TAXPAYER_ID | — | — |
| 48 | FiscalDocLocInfoPersistPEOShipfromLeFormTaxNumber | SHIPFROM_LE_FORM_TAX_NUMBER | — | — |
| 49 | FiscalDocLocInfoPersistPEOShipfromLeLocationId | SHIPFROM_LE_LOCATION_ID | — | — |
| 50 | FiscalDocLocInfoPersistPEOShipfromLePartyId | SHIPFROM_LE_PARTY_ID | — | — |
| 51 | FiscalDocLocInfoPersistPEOShipfromLePartySiteId | SHIPFROM_LE_PARTY_SITE_ID | — | — |
| 52 | FiscalDocLocInfoPersistPEOShipfromLeTaxId | SHIPFROM_LE_TAX_ID | — | — |
| 53 | FiscalDocLocInfoPersistPEOShipfromLeTaxpayerId | SHIPFROM_LE_TAXPAYER_ID | — | — |
| 54 | FiscalDocLocInfoPersistPEOShipfromSuppPartySiteId | SHIPFROM_SUPP_PARTY_SITE_ID | — | — |
| 55 | FiscalDocLocInfoPersistPEOShipfromSupplierFormTaxNum | SHIPFROM_SUPPLIER_FORM_TAX_NUM | — | — |
| 56 | FiscalDocLocInfoPersistPEOShipfromSupplierLocationId | SHIPFROM_SUPPLIER_LOCATION_ID | — | — |
| 57 | FiscalDocLocInfoPersistPEOShipfromSupplierPartyId | SHIPFROM_SUPPLIER_PARTY_ID | — | — |
| 58 | FiscalDocLocInfoPersistPEOShipfromSupplierTaxId | SHIPFROM_SUPPLIER_TAX_ID | — | — |
| 59 | FiscalDocLocInfoPersistPEOShipfromSupplierTaxpayerId | SHIPFROM_SUPPLIER_TAXPAYER_ID | — | — |
| 60 | FiscalDocLocInfoPersistPEOShipfromType | SHIPFROM_TYPE | — | — |
| 61 | FiscalDocLocInfoPersistPEOShiptoCustPartySiteId | SHIPTO_CUST_PARTY_SITE_ID | — | — |
| 62 | FiscalDocLocInfoPersistPEOShiptoCustomerFormTaxNum | SHIPTO_CUSTOMER_FORM_TAX_NUM | — | — |
| 63 | FiscalDocLocInfoPersistPEOShiptoCustomerLocationId | SHIPTO_CUSTOMER_LOCATION_ID | — | — |
| 64 | FiscalDocLocInfoPersistPEOShiptoCustomerPartyId | SHIPTO_CUSTOMER_PARTY_ID | — | — |
| 65 | FiscalDocLocInfoPersistPEOShiptoCustomerTaxId | SHIPTO_CUSTOMER_TAX_ID | — | — |
| 66 | FiscalDocLocInfoPersistPEOShiptoCustomerTaxpayerId | SHIPTO_CUSTOMER_TAXPAYER_ID | — | — |
| 67 | FiscalDocLocInfoPersistPEOShiptoLeFormTaxNumber | SHIPTO_LE_FORM_TAX_NUMBER | — | — |
| 68 | FiscalDocLocInfoPersistPEOShiptoLeLocationId | SHIPTO_LE_LOCATION_ID | — | — |
| 69 | FiscalDocLocInfoPersistPEOShiptoLePartyId | SHIPTO_LE_PARTY_ID | — | — |
| 70 | FiscalDocLocInfoPersistPEOShiptoLePartySiteId | SHIPTO_LE_PARTY_SITE_ID | — | — |
| 71 | FiscalDocLocInfoPersistPEOShiptoLeTaxId | SHIPTO_LE_TAX_ID | — | — |
| 72 | FiscalDocLocInfoPersistPEOShiptoLeTaxpayerId | SHIPTO_LE_TAXPAYER_ID | — | — |
| 73 | FiscalDocLocInfoPersistPEOShiptoSuppPartySiteId | SHIPTO_SUPP_PARTY_SITE_ID | — | — |
| 74 | FiscalDocLocInfoPersistPEOShiptoSupplierFormTaxNum | SHIPTO_SUPPLIER_FORM_TAX_NUM | — | — |
| 75 | FiscalDocLocInfoPersistPEOShiptoSupplierLocationId | SHIPTO_SUPPLIER_LOCATION_ID | — | — |
| 76 | FiscalDocLocInfoPersistPEOShiptoSupplierPartyId | SHIPTO_SUPPLIER_PARTY_ID | — | — |
| 77 | FiscalDocLocInfoPersistPEOShiptoSupplierTaxId | SHIPTO_SUPPLIER_TAX_ID | — | — |
| 78 | FiscalDocLocInfoPersistPEOShiptoSupplierTaxpayerId | SHIPTO_SUPPLIER_TAXPAYER_ID | — | — |
| 79 | FiscalDocLocInfoPersistPEOShiptoType | SHIPTO_TYPE | — | — |

### [[cmf_fiscal_doc_headers|CMF_FISCAL_DOC_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocHeadersPEOAccessKeyNumber | ACCESS_KEY_NUMBER | — | — |
| 2 | FiscalDocHeadersPEOAcknowledgedDate | ACKNOWLEDGED_DATE | — | — |
| 3 | FiscalDocHeadersPEOBillToBusinessUnitId | BILL_TO_BUSINESS_UNIT_ID | — | — |
| 4 | FiscalDocHeadersPEOChargeAllocationStatus | CHARGE_ALLOCATION_STATUS | — | — |
| 5 | FiscalDocHeadersPEOCmrInterfacedFlag | CMR_INTERFACED_FLAG | — | — |
| 6 | FiscalDocHeadersPEOConversionRate | CONVERSION_RATE | — | — |
| 7 | FiscalDocHeadersPEOConverstionType | CONVERSTION_TYPE | — | — |
| 8 | FiscalDocHeadersPEOCountryCode | COUNTRY_CODE | — | — |
| 9 | FiscalDocHeadersPEOCreatedBy1 | CREATED_BY | — | — |
| 10 | FiscalDocHeadersPEOCreationDate1 | CREATION_DATE | — | — |
| 11 | FiscalDocHeadersPEOCurrency | CURRENCY | — | — |
| 12 | FiscalDocHeadersPEODocumentHeaderId1 | DOCUMENT_HEADER_ID | — | — |
| 13 | FiscalDocHeadersPEODocumentNumber | DOCUMENT_NUMBER | — | — |
| 14 | FiscalDocHeadersPEODocumentStatus | DOCUMENT_STATUS | — | — |
| 15 | FiscalDocHeadersPEODocumentType | DOCUMENT_TYPE | — | — |
| 16 | FiscalDocHeadersPEOExternalSystemRefId1 | EXTERNAL_SYSTEM_REF_ID | — | — |
| 17 | FiscalDocHeadersPEOExternalSystemReference1 | EXTERNAL_SYSTEM_REFERENCE | — | — |
| 18 | FiscalDocHeadersPEOFiscalDocAssoctnsId | FISCAL_DOC_ASSOCTNS_ID | — | — |
| 19 | FiscalDocHeadersPEOFiscalProcOptionsId | FISCAL_PROC_OPTIONS_ID | — | — |
| 20 | FiscalDocHeadersPEOInterfacedFlag | INTERFACED_FLAG | — | — |
| 21 | FiscalDocHeadersPEOInvoiceInterfacedFlag | INVOICE_INTERFACED_FLAG | — | — |
| 22 | FiscalDocHeadersPEOIssueDate | ISSUE_DATE | — | — |
| 23 | FiscalDocHeadersPEOIssuerLocationId | ISSUER_LOCATION_ID | — | — |
| 24 | FiscalDocHeadersPEOIssuerPartyId | ISSUER_PARTY_ID | — | — |
| 25 | FiscalDocHeadersPEOIssuerPartySiteId | ISSUER_PARTY_SITE_ID | — | — |
| 26 | FiscalDocHeadersPEOIssuerTaxId | ISSUER_TAX_ID | — | — |
| 27 | FiscalDocHeadersPEOItemLineAmount | ITEM_LINE_AMOUNT | — | — |
| 28 | FiscalDocHeadersPEOJobDefinitionName1 | JOB_DEFINITION_NAME | — | — |
| 29 | FiscalDocHeadersPEOJobDefinitionPackage1 | JOB_DEFINITION_PACKAGE | — | — |
| 30 | FiscalDocHeadersPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | — |
| 31 | FiscalDocHeadersPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 32 | FiscalDocHeadersPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 33 | FiscalDocHeadersPEOModel | MODEL | — | — |
| 34 | FiscalDocHeadersPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 35 | FiscalDocHeadersPEOOperationType | OPERATION_TYPE | — | — |
| 36 | FiscalDocHeadersPEOParentDocumentHeaderId | PARENT_DOCUMENT_HEADER_ID | — | — |
| 37 | FiscalDocHeadersPEOReason | REASON | — | — |
| 38 | FiscalDocHeadersPEOReceiverLocationId | RECEIVER_LOCATION_ID | — | — |
| 39 | FiscalDocHeadersPEOReceiverPartyId | RECEIVER_PARTY_ID | — | — |
| 40 | FiscalDocHeadersPEOReceiverPartySiteId | RECEIVER_PARTY_SITE_ID | — | — |
| 41 | FiscalDocHeadersPEOReceiverTaxId | RECEIVER_TAX_ID | — | — |
| 42 | FiscalDocHeadersPEOReferencedStatus | REFERENCED_STATUS | — | — |
| 43 | FiscalDocHeadersPEORequestId1 | REQUEST_ID | — | — |
| 44 | FiscalDocHeadersPEOSchedulesAllocatedFlag | SCHEDULES_ALLOCATED_FLAG | — | — |
| 45 | FiscalDocHeadersPEOSeries | SERIES | — | — |
| 46 | FiscalDocHeadersPEOShipfromLocationId | SHIPFROM_LOCATION_ID | — | — |
| 47 | FiscalDocHeadersPEOShipfromPartyId | SHIPFROM_PARTY_ID | — | — |
| 48 | FiscalDocHeadersPEOShipfromPartySiteId | SHIPFROM_PARTY_SITE_ID | — | — |
| 49 | FiscalDocHeadersPEOShipfromTaxId | SHIPFROM_TAX_ID | — | — |
| 50 | FiscalDocHeadersPEOShiptoLocationId | SHIPTO_LOCATION_ID | — | — |
| 51 | FiscalDocHeadersPEOShiptoPartyId | SHIPTO_PARTY_ID | — | — |
| 52 | FiscalDocHeadersPEOShiptoPartySiteId | SHIPTO_PARTY_SITE_ID | — | — |
| 53 | FiscalDocHeadersPEOShiptoTaxId | SHIPTO_TAX_ID | — | — |
| 54 | FiscalDocHeadersPEOSoldToLegalEntityId | SOLD_TO_LEGAL_ENTITY_ID | — | — |
| 55 | FiscalDocHeadersPEOSourceDocumentType | SOURCE_DOCUMENT_TYPE | — | — |
| 56 | FiscalDocHeadersPEOSubseries | SUBSERIES | — | — |
| 57 | FiscalDocHeadersPEOTaxCalculationStatus | TAX_CALCULATION_STATUS | — | — |
| 58 | FiscalDocHeadersPEOTotalAmount | TOTAL_AMOUNT | — | — |
| 59 | FiscalDocHeadersPEOValidationStatus | VALIDATION_STATUS | — | — |

### [[cmf_legal_doc_associations|CMF_LEGAL_DOC_ASSOCIATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LawsuitId | LAWSUIT_ID | 🔑 | ✅ |
| 2 | LegalDocumentAssocPEOConcessionActId | CONCESSION_ACT_ID | — | ✅ |
| 3 | LegalDocumentAssocPEOCreatedBy | CREATED_BY | — | — |
| 4 | LegalDocumentAssocPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | LegalDocumentAssocPEODocumentHeaderId | DOCUMENT_HEADER_ID | — | — |
| 6 | LegalDocumentAssocPEOExternalSystemRefId | EXTERNAL_SYSTEM_REF_ID | — | — |
| 7 | LegalDocumentAssocPEOExternalSystemReference | EXTERNAL_SYSTEM_REFERENCE | — | — |
| 8 | LegalDocumentAssocPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 9 | LegalDocumentAssocPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 10 | LegalDocumentAssocPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | LegalDocumentAssocPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | LegalDocumentAssocPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | LegalDocumentAssocPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | LegalDocumentAssocPEOOriginOrProceeding | ORIGIN_OR_PROCEEDING | — | ✅ |
| 15 | LegalDocumentAssocPEORequestId | REQUEST_ID | — | — |

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitPEOBusinessUnitId | BU_ID | — | — |
| 2 | BusinessUnitPEOCreatedBy4 | CREATED_BY | — | — |
| 3 | BusinessUnitPEOCreationDate4 | CREATION_DATE | — | — |
| 4 | BusinessUnitPEODateFrom | DATE_FROM | — | — |
| 5 | BusinessUnitPEODateTo | DATE_TO | — | — |
| 6 | BusinessUnitPEODefaultCurrencyCode | DEFAULT_CURRENCY_CODE | — | — |
| 7 | BusinessUnitPEODefaultSetId | DEFAULT_SET_ID | — | — |
| 8 | BusinessUnitPEOEnabledForHrFlag | ENABLED_FOR_HR_FLAG | — | — |
| 9 | BusinessUnitPEOEnterpriseId | BUSINESS_GROUP_ID | — | — |
| 10 | BusinessUnitPEOFinancialsBusinessUnitId | FIN_BUSINESS_UNIT_ID | — | — |
| 11 | BusinessUnitPEOLastUpdateDate4 | LAST_UPDATE_DATE | — | — |
| 12 | BusinessUnitPEOLastUpdateLogin4 | LAST_UPDATE_LOGIN | — | — |
| 13 | BusinessUnitPEOLastUpdatedBy4 | LAST_UPDATED_BY | — | — |
| 14 | BusinessUnitPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 15 | BusinessUnitPEOLocationId | LOCATION_ID | — | — |
| 16 | BusinessUnitPEOManagerId | MANAGER_ID | — | — |
| 17 | BusinessUnitPEOName | BU_NAME | — | — |
| 18 | BusinessUnitPEOPrimaryLedgerId | PRIMARY_LEDGER_ID | — | — |
| 19 | BusinessUnitPEOProfitCenterFlag | PROFIT_CENTER_FLAG | — | — |
| 20 | BusinessUnitPEOShortCode | SHORT_CODE | — | — |
| 21 | BusinessUnitPEOStatus | STATUS | — | — |

### [[jg_fscl_hdrs_atrb_ext_all|JG_FSCL_HDRS_ATRB_EXT_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocHeaderExtnEOApplicationId | APPLICATION_ID | — | — |
| 2 | FiscalDocHeaderExtnEOCommitmentStatementIdent | COMMITMENT_STATEMENT_IDENT | — | — |
| 3 | FiscalDocHeaderExtnEOContainerIdentifier | CONTAINER_IDENTIFIER | — | — |
| 4 | FiscalDocHeaderExtnEOContingencyType | CONTINGENCY_TYPE | — | — |
| 5 | FiscalDocHeaderExtnEOCreatedBy2 | CREATED_BY | — | — |
| 6 | FiscalDocHeaderExtnEOCreationDate2 | CREATION_DATE | — | — |
| 7 | FiscalDocHeaderExtnEODocExtHdrId | DOC_EXT_HDR_ID | — | — |
| 8 | FiscalDocHeaderExtnEODocNature | DOC_NATURE | — | — |
| 9 | FiscalDocHeaderExtnEOEntityCode | ENTITY_CODE | — | — |
| 10 | FiscalDocHeaderExtnEOEventClassCode | EVENT_CLASS_CODE | — | — |
| 11 | FiscalDocHeaderExtnEOFerryIdentification | FERRY_IDENTIFICATION | — | — |
| 12 | FiscalDocHeaderExtnEOFiscalDocDate | FISCAL_DOC_DATE | — | — |
| 13 | FiscalDocHeaderExtnEOFreightPartySiteId | FREIGHT_PARTY_SITE_ID | — | — |
| 14 | FiscalDocHeaderExtnEOFreightType | FREIGHT_TYPE | — | — |
| 15 | FiscalDocHeaderExtnEOGoodsBrandCarried | GOODS_BRAND_CARRIED | — | — |
| 16 | FiscalDocHeaderExtnEOGoodsTypeCarried | GOODS_TYPE_CARRIED | — | — |
| 17 | FiscalDocHeaderExtnEOGrossWeight | GROSS_WEIGHT | — | — |
| 18 | FiscalDocHeaderExtnEOIndustryType | INDUSTRY_TYPE | — | — |
| 19 | FiscalDocHeaderExtnEOJobDefinitionName2 | JOB_DEFINITION_NAME | — | — |
| 20 | FiscalDocHeaderExtnEOJobDefinitionPackage2 | JOB_DEFINITION_PACKAGE | — | — |
| 21 | FiscalDocHeaderExtnEOLastUpdateDate2 | LAST_UPDATE_DATE | — | — |
| 22 | FiscalDocHeaderExtnEOLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 23 | FiscalDocHeaderExtnEOLastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 24 | FiscalDocHeaderExtnEOLegalReportingUnitId | LEGAL_REPORTING_UNIT_ID | — | — |
| 25 | FiscalDocHeaderExtnEOMatIssueRecptDate | MAT_ISSUE_RECPT_DATE | — | — |
| 26 | FiscalDocHeaderExtnEOMatIssueRecptHour | MAT_ISSUE_RECPT_HOUR | — | — |
| 27 | FiscalDocHeaderExtnEONetWeight | NET_WEIGHT | — | — |
| 28 | FiscalDocHeaderExtnEOObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 29 | FiscalDocHeaderExtnEOOrgId | ORG_ID | — | — |
| 30 | FiscalDocHeaderExtnEOPaymentOption | PAYMENT_OPTION | — | — |
| 31 | FiscalDocHeaderExtnEOPurchaseContract | PURCHASE_CONTRACT | — | — |
| 32 | FiscalDocHeaderExtnEOQuantityCarried | QUANTITY_CARRIED | — | — |
| 33 | FiscalDocHeaderExtnEORefComplementaryFdFlag | REF_COMPLEMENTARY_FD_FLAG | — | — |
| 34 | FiscalDocHeaderExtnEORefDocIssuerStateCode | REF_DOC_ISSUER_STATE_CODE | — | — |
| 35 | FiscalDocHeaderExtnEORefDocNum | REF_DOC_NUM | — | — |
| 36 | FiscalDocHeaderExtnEORefFiscalDocDate | REF_FISCAL_DOC_DATE | — | — |
| 37 | FiscalDocHeaderExtnEORefFiscalDocKey | REF_FISCAL_DOC_KEY | — | — |
| 38 | FiscalDocHeaderExtnEORefIssuerTaxpayerId | REF_ISSUER_TAXPAYER_ID | — | — |
| 39 | FiscalDocHeaderExtnEORefModel | REF_MODEL | — | — |
| 40 | FiscalDocHeaderExtnEORefRuralFlag | REF_RURAL_FLAG | — | — |
| 41 | FiscalDocHeaderExtnEORefSeries | REF_SERIES | — | — |
| 42 | FiscalDocHeaderExtnEORequestId2 | REQUEST_ID | — | — |
| 43 | FiscalDocHeaderExtnEOSealNumber | SEAL_NUMBER | — | — |
| 44 | FiscalDocHeaderExtnEOSeries1 | SERIES | — | — |
| 45 | FiscalDocHeaderExtnEOServiceSeries | SERVICE_SERIES | — | — |
| 46 | FiscalDocHeaderExtnEOServiceSituation | SERVICE_SITUATION | — | — |
| 47 | FiscalDocHeaderExtnEOServiceTaxPaidFlag | SERVICE_TAX_PAID_FLAG | — | — |
| 48 | FiscalDocHeaderExtnEOServiceType | SERVICE_TYPE | — | — |
| 49 | FiscalDocHeaderExtnEOTaxSettlementDate | TAX_SETTLEMENT_DATE | — | — |
| 50 | FiscalDocHeaderExtnEOTrxFdTypeDeterminant | TRX_FD_TYPE_DETERMINANT | — | — |
| 51 | FiscalDocHeaderExtnEOTrxId | TRX_ID | — | — |
| 52 | FiscalDocHeaderExtnEOTrxNumber | TRX_NUMBER | — | — |
| 53 | FiscalDocHeaderExtnEOWagonIdentification | WAGON_IDENTIFICATION | — | — |
| 54 | FiscalDocHeaderExtnEOWhtSocialIntgProgAmt | WHT_SOCIAL_INTG_PROG_AMT | — | — |
| 55 | FiscalDocHeaderExtnEOWhtSsFinancingAmt | WHT_SS_FINANCING_AMT | — | — |

### [[jg_fscl_hdr_dtls_atrb_ext_all|JG_FSCL_HDR_DTLS_ATRB_EXT_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocHeaderDetailExtnEOApplicationId1 | APPLICATION_ID | — | — |
| 2 | FiscalDocHeaderDetailExtnEOCreatedBy3 | CREATED_BY | — | — |
| 3 | FiscalDocHeaderDetailExtnEOCreationDate3 | CREATION_DATE | — | — |
| 4 | FiscalDocHeaderDetailExtnEODocExtHdrId1 | DOC_EXT_HDR_ID | — | — |
| 5 | FiscalDocHeaderDetailExtnEOEntityCode1 | ENTITY_CODE | — | — |
| 6 | FiscalDocHeaderDetailExtnEOEventClassCode1 | EVENT_CLASS_CODE | — | — |
| 7 | FiscalDocHeaderDetailExtnEOHdrAtrbExtDtlId | HDR_ATRB_EXT_DTL_ID | — | — |
| 8 | FiscalDocHeaderDetailExtnEOJobDefinitionName3 | JOB_DEFINITION_NAME | — | — |
| 9 | FiscalDocHeaderDetailExtnEOJobDefinitionPackage3 | JOB_DEFINITION_PACKAGE | — | — |
| 10 | FiscalDocHeaderDetailExtnEOLastUpdateDate3 | LAST_UPDATE_DATE | — | — |
| 11 | FiscalDocHeaderDetailExtnEOLastUpdateLogin3 | LAST_UPDATE_LOGIN | — | — |
| 12 | FiscalDocHeaderDetailExtnEOLastUpdatedBy3 | LAST_UPDATED_BY | — | — |
| 13 | FiscalDocHeaderDetailExtnEOObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 14 | FiscalDocHeaderDetailExtnEOOrgId1 | ORG_ID | — | — |
| 15 | FiscalDocHeaderDetailExtnEORecordType | RECORD_TYPE | — | — |
| 16 | FiscalDocHeaderDetailExtnEORequestId3 | REQUEST_ID | — | — |
| 17 | FiscalDocHeaderDetailExtnEOTaxRelatedLegalMessageFlag | TAX_RELATED_LEGAL_MESSAGE_FLAG | — | — |
| 18 | FiscalDocHeaderDetailExtnEOTrxId1 | TRX_ID | — | — |

### [[jg_fscl_tax_lines_all|JG_FSCL_TAX_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocTaxLineEOAdjustedTaxLineId | ADJUSTED_TAX_LINE_ID | — | — |
| 2 | FiscalDocTaxLineEOApplicationId | APPLICATION_ID | — | — |
| 3 | FiscalDocTaxLineEOCalTaxAmt | CAL_TAX_AMT | — | — |
| 4 | FiscalDocTaxLineEOCalTaxAmtTaxCurr | CAL_TAX_AMT_TAX_CURR | — | — |
| 5 | FiscalDocTaxLineEOCityCode | CITY_CODE | — | — |
| 6 | FiscalDocTaxLineEOContentOwnerId | CONTENT_OWNER_ID | — | — |
| 7 | FiscalDocTaxLineEOCreatedBy | CREATED_BY | — | — |
| 8 | FiscalDocTaxLineEOCreationDate | CREATION_DATE | — | — |
| 9 | FiscalDocTaxLineEOEntityCode | ENTITY_CODE | — | — |
| 10 | FiscalDocTaxLineEOEventClassCode | EVENT_CLASS_CODE | — | — |
| 11 | FiscalDocTaxLineEOExemptCertificateNumber | EXEMPT_CERTIFICATE_NUMBER | — | — |
| 12 | FiscalDocTaxLineEOExemptReasonCode | EXEMPT_REASON_CODE | — | — |
| 13 | FiscalDocTaxLineEOInterfaceEntityCode | INTERFACE_ENTITY_CODE | — | — |
| 14 | FiscalDocTaxLineEOInterfaceTaxLineId | INTERFACE_TAX_LINE_ID | — | — |
| 15 | FiscalDocTaxLineEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 16 | FiscalDocTaxLineEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 17 | FiscalDocTaxLineEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 18 | FiscalDocTaxLineEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 19 | FiscalDocTaxLineEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 20 | FiscalDocTaxLineEOMainTrxLineId | MAIN_TRX_LINE_ID | — | — |
| 21 | FiscalDocTaxLineEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 22 | FiscalDocTaxLineEOOrgId | ORG_ID | — | — |
| 23 | FiscalDocTaxLineEOOrigSelfAssessedFlag | ORIG_SELF_ASSESSED_FLAG | — | — |
| 24 | FiscalDocTaxLineEOOrigTaxAmtIncludedFlag | ORIG_TAX_AMT_INCLUDED_FLAG | — | — |
| 25 | FiscalDocTaxLineEOOrigTaxJurisdictionCode | ORIG_TAX_JURISDICTION_CODE | — | — |
| 26 | FiscalDocTaxLineEOOrigTaxJurisdictionId | ORIG_TAX_JURISDICTION_ID | — | — |
| 27 | FiscalDocTaxLineEOOrigTaxRate | ORIG_TAX_RATE | — | — |
| 28 | FiscalDocTaxLineEOOrigTaxRateCode | ORIG_TAX_RATE_CODE | — | — |
| 29 | FiscalDocTaxLineEOOrigTaxRateId | ORIG_TAX_RATE_ID | — | — |
| 30 | FiscalDocTaxLineEOOrigTaxStatusCode | ORIG_TAX_STATUS_CODE | — | — |
| 31 | FiscalDocTaxLineEOOrigTaxStatusId | ORIG_TAX_STATUS_ID | — | — |
| 32 | FiscalDocTaxLineEOQuantity | QUANTITY | — | — |
| 33 | FiscalDocTaxLineEOReferenceDocLineAmt | REFERENCE_DOC_LINE_AMT | — | — |
| 34 | FiscalDocTaxLineEOReferenceDocUnitPrice | REFERENCE_DOC_UNIT_PRICE | — | — |
| 35 | FiscalDocTaxLineEOReportingTypeCode | REPORTING_TYPE_CODE | — | — |
| 36 | FiscalDocTaxLineEORequestId | REQUEST_ID | — | — |
| 37 | FiscalDocTaxLineEOSelfAssessedFlag | SELF_ASSESSED_FLAG | — | — |
| 38 | FiscalDocTaxLineEOServiceItemCode | SERVICE_ITEM_CODE | — | — |
| 39 | FiscalDocTaxLineEOTax | TAX | — | — |
| 40 | FiscalDocTaxLineEOTaxAmt | TAX_AMT | — | — |
| 41 | FiscalDocTaxLineEOTaxAmtIncludedFlag | TAX_AMT_INCLUDED_FLAG | — | — |
| 42 | FiscalDocTaxLineEOTaxAmtTaxCurr | TAX_AMT_TAX_CURR | — | — |
| 43 | FiscalDocTaxLineEOTaxCreditAmount | TAX_CREDIT_AMOUNT | — | — |
| 44 | FiscalDocTaxLineEOTaxExceptionId | TAX_EXCEPTION_ID | — | — |
| 45 | FiscalDocTaxLineEOTaxExemptionId | TAX_EXEMPTION_ID | — | — |
| 46 | FiscalDocTaxLineEOTaxHoldCode | TAX_HOLD_CODE | — | — |
| 47 | FiscalDocTaxLineEOTaxId | TAX_ID | — | — |
| 48 | FiscalDocTaxLineEOTaxJurisdictionCode | TAX_JURISDICTION_CODE | — | — |
| 49 | FiscalDocTaxLineEOTaxJurisdictionId | TAX_JURISDICTION_ID | — | — |
| 50 | FiscalDocTaxLineEOTaxLineId | TAX_LINE_ID | — | — |
| 51 | FiscalDocTaxLineEOTaxLineNumber | TAX_LINE_NUMBER | — | — |
| 52 | FiscalDocTaxLineEOTaxLineSourceCode | TAX_LINE_SOURCE_CODE | — | — |
| 53 | FiscalDocTaxLineEOTaxOnlyLineFlag | TAX_ONLY_LINE_FLAG | — | — |
| 54 | FiscalDocTaxLineEOTaxRate | TAX_RATE | — | — |
| 55 | FiscalDocTaxLineEOTaxRateCode | TAX_RATE_CODE | — | — |
| 56 | FiscalDocTaxLineEOTaxRateId | TAX_RATE_ID | — | — |
| 57 | FiscalDocTaxLineEOTaxRegimeCode | TAX_REGIME_CODE | — | — |
| 58 | FiscalDocTaxLineEOTaxRegimeId | TAX_REGIME_ID | — | — |
| 59 | FiscalDocTaxLineEOTaxSituationCode | TAX_SITUATION_CODE | — | — |
| 60 | FiscalDocTaxLineEOTaxStatusCode | TAX_STATUS_CODE | — | — |
| 61 | FiscalDocTaxLineEOTaxStatusId | TAX_STATUS_ID | — | — |
| 62 | FiscalDocTaxLineEOTaxableAmt | TAXABLE_AMT | — | — |
| 63 | FiscalDocTaxLineEOTaxableAmtDetermCode | TAXABLE_AMT_DETERM_CODE | — | — |
| 64 | FiscalDocTaxLineEOTaxableBasisPercPayerOpr | TAXABLE_BASIS_PERC_PAYER_OPR | — | — |
| 65 | FiscalDocTaxLineEOTaxableBasisReductionPerc | TAXABLE_BASIS_REDUCTION_PERC | — | — |
| 66 | FiscalDocTaxLineEOTrxId | TRX_ID | — | — |
| 67 | FiscalDocTaxLineEOTrxLevelType | TRX_LEVEL_TYPE | — | — |
| 68 | FiscalDocTaxLineEOTrxLineId | TRX_LINE_ID | — | — |
| 69 | FiscalDocTaxLineEOUomCode | UOM_CODE | — | — |
| 70 | FiscalDocTaxLineEOUserEnteredTaxAmt | USER_ENTERED_TAX_AMT | — | — |
| 71 | FiscalDocTaxLineEOUserEnteredTaxAmtTaxCurr | USER_ENTERED_TAX_AMT_TAX_CURR | — | — |
| 72 | FiscalDocTaxLineEOValueAddedMarginPerc | VALUE_ADDED_MARGIN_PERC | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FdhCreatedByPersonNameDPEOBusinessGroupId6 | BUSINESS_GROUP_ID | — | — |
| 2 | FdhCreatedByPersonNameDPEOCreatedBy11 | CREATED_BY | — | — |
| 3 | FdhCreatedByPersonNameDPEOCreationDate11 | CREATION_DATE | — | — |
| 4 | FdhCreatedByPersonNameDPEODisplayName2 | DISPLAY_NAME | — | — |
| 5 | FdhCreatedByPersonNameDPEOEffectiveEndDate2 | EFFECTIVE_END_DATE | — | — |
| 6 | FdhCreatedByPersonNameDPEOEffectiveStartDate2 | EFFECTIVE_START_DATE | — | — |
| 7 | FdhCreatedByPersonNameDPEOFirstName2 | FIRST_NAME | — | — |
| 8 | FdhCreatedByPersonNameDPEOFullName2 | FULL_NAME | — | — |
| 9 | FdhCreatedByPersonNameDPEOHonors2 | HONORS | — | — |
| 10 | FdhCreatedByPersonNameDPEOKnownAs2 | KNOWN_AS | — | — |
| 11 | FdhCreatedByPersonNameDPEOLastName2 | LAST_NAME | — | — |
| 12 | FdhCreatedByPersonNameDPEOLastUpdateDate11 | LAST_UPDATE_DATE | — | — |
| 13 | FdhCreatedByPersonNameDPEOLastUpdateLogin11 | LAST_UPDATE_LOGIN | — | — |
| 14 | FdhCreatedByPersonNameDPEOLastUpdatedBy11 | LAST_UPDATED_BY | — | — |
| 15 | FdhCreatedByPersonNameDPEOLegislationCode2 | LEGISLATION_CODE | — | — |
| 16 | FdhCreatedByPersonNameDPEOListName2 | LIST_NAME | — | — |
| 17 | FdhCreatedByPersonNameDPEOMiddleNames2 | MIDDLE_NAMES | — | — |
| 18 | FdhCreatedByPersonNameDPEOMilitaryRank2 | MILITARY_RANK | — | — |
| 19 | FdhCreatedByPersonNameDPEONameType2 | NAME_TYPE | — | — |
| 20 | FdhCreatedByPersonNameDPEOObjectVersionNumber10 | OBJECT_VERSION_NUMBER | — | — |
| 21 | FdhCreatedByPersonNameDPEOOrderName2 | ORDER_NAME | — | — |
| 22 | FdhCreatedByPersonNameDPEOPersonId6 | PERSON_ID | — | — |
| 23 | FdhCreatedByPersonNameDPEOPersonNameId2 | PERSON_NAME_ID | — | — |
| 24 | FdhCreatedByPersonNameDPEOPreNameAdjunct2 | PRE_NAME_ADJUNCT | — | — |
| 25 | FdhCreatedByPersonNameDPEOPreviousLastName2 | PREVIOUS_LAST_NAME | — | — |
| 26 | FdhCreatedByPersonNameDPEOSuffix2 | SUFFIX | — | — |
| 27 | FdhCreatedByPersonNameDPEOTitle2 | TITLE | — | — |
| 28 | FdhUpdatedByPersonNameDPEO1_1BusinessGroupId7 | BUSINESS_GROUP_ID | — | — |
| 29 | FdhUpdatedByPersonNameDPEO1_1CreatedBy12 | CREATED_BY | — | — |
| 30 | FdhUpdatedByPersonNameDPEO1_1CreationDate12 | CREATION_DATE | — | — |
| 31 | FdhUpdatedByPersonNameDPEO1_1DisplayName3 | DISPLAY_NAME | — | — |
| 32 | FdhUpdatedByPersonNameDPEO1_1EffectiveEndDate3 | EFFECTIVE_END_DATE | — | — |
| 33 | FdhUpdatedByPersonNameDPEO1_1EffectiveStartDate3 | EFFECTIVE_START_DATE | — | — |
| 34 | FdhUpdatedByPersonNameDPEO1_1FirstName3 | FIRST_NAME | — | — |
| 35 | FdhUpdatedByPersonNameDPEO1_1FullName3 | FULL_NAME | — | — |
| 36 | FdhUpdatedByPersonNameDPEO1_1Honors3 | HONORS | — | — |
| 37 | FdhUpdatedByPersonNameDPEO1_1KnownAs3 | KNOWN_AS | — | — |
| 38 | FdhUpdatedByPersonNameDPEO1_1LastName3 | LAST_NAME | — | — |
| 39 | FdhUpdatedByPersonNameDPEO1_1LastUpdateDate12 | LAST_UPDATE_DATE | — | — |
| 40 | FdhUpdatedByPersonNameDPEO1_1LastUpdateLogin12 | LAST_UPDATE_LOGIN | — | — |
| 41 | FdhUpdatedByPersonNameDPEO1_1LastUpdatedBy12 | LAST_UPDATED_BY | — | — |
| 42 | FdhUpdatedByPersonNameDPEO1_1LegislationCode3 | LEGISLATION_CODE | — | — |
| 43 | FdhUpdatedByPersonNameDPEO1_1ListName3 | LIST_NAME | — | — |
| 44 | FdhUpdatedByPersonNameDPEO1_1MiddleNames3 | MIDDLE_NAMES | — | — |
| 45 | FdhUpdatedByPersonNameDPEO1_1MilitaryRank3 | MILITARY_RANK | — | — |
| 46 | FdhUpdatedByPersonNameDPEO1_1NameType3 | NAME_TYPE | — | — |
| 47 | FdhUpdatedByPersonNameDPEO1_1ObjectVersionNumber11 | OBJECT_VERSION_NUMBER | — | — |
| 48 | FdhUpdatedByPersonNameDPEO1_1OrderName3 | ORDER_NAME | — | — |
| 49 | FdhUpdatedByPersonNameDPEO1_1PersonId7 | PERSON_ID | — | — |
| 50 | FdhUpdatedByPersonNameDPEO1_1PersonNameId3 | PERSON_NAME_ID | — | — |
| 51 | FdhUpdatedByPersonNameDPEO1_1PreNameAdjunct3 | PRE_NAME_ADJUNCT | — | — |
| 52 | FdhUpdatedByPersonNameDPEO1_1PreviousLastName3 | PREVIOUS_LAST_NAME | — | — |
| 53 | FdhUpdatedByPersonNameDPEO1_1Suffix3 | SUFFIX | — | — |
| 54 | FdhUpdatedByPersonNameDPEO1_1Title3 | TITLE | — | — |
| 55 | LeCreatedByPersonNameDPEOBusinessGroupId4 | BUSINESS_GROUP_ID | — | — |
| 56 | LeCreatedByPersonNameDPEOCreatedBy9 | CREATED_BY | — | — |
| 57 | LeCreatedByPersonNameDPEOCreationDate9 | CREATION_DATE | — | — |
| 58 | LeCreatedByPersonNameDPEODisplayName | DISPLAY_NAME | — | — |
| 59 | LeCreatedByPersonNameDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 60 | LeCreatedByPersonNameDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 61 | LeCreatedByPersonNameDPEOFirstName | FIRST_NAME | — | — |
| 62 | LeCreatedByPersonNameDPEOFullName | FULL_NAME | — | ✅ |
| 63 | LeCreatedByPersonNameDPEOHonors | HONORS | — | — |
| 64 | LeCreatedByPersonNameDPEOKnownAs | KNOWN_AS | — | — |
| 65 | LeCreatedByPersonNameDPEOLastName | LAST_NAME | — | — |
| 66 | LeCreatedByPersonNameDPEOLastUpdateDate9 | LAST_UPDATE_DATE | — | — |
| 67 | LeCreatedByPersonNameDPEOLastUpdateLogin9 | LAST_UPDATE_LOGIN | — | — |
| 68 | LeCreatedByPersonNameDPEOLastUpdatedBy9 | LAST_UPDATED_BY | — | — |
| 69 | LeCreatedByPersonNameDPEOLegislationCode | LEGISLATION_CODE | — | — |
| 70 | LeCreatedByPersonNameDPEOListName | LIST_NAME | — | — |
| 71 | LeCreatedByPersonNameDPEOMiddleNames | MIDDLE_NAMES | — | — |
| 72 | LeCreatedByPersonNameDPEOMilitaryRank | MILITARY_RANK | — | — |
| 73 | LeCreatedByPersonNameDPEONameType | NAME_TYPE | — | — |
| 74 | LeCreatedByPersonNameDPEOObjectVersionNumber8 | OBJECT_VERSION_NUMBER | — | — |
| 75 | LeCreatedByPersonNameDPEOOrderName | ORDER_NAME | — | — |
| 76 | LeCreatedByPersonNameDPEOPersonId4 | PERSON_ID | — | — |
| 77 | LeCreatedByPersonNameDPEOPersonNameId | PERSON_NAME_ID | — | — |
| 78 | LeCreatedByPersonNameDPEOPreNameAdjunct | PRE_NAME_ADJUNCT | — | — |
| 79 | LeCreatedByPersonNameDPEOPreviousLastName | PREVIOUS_LAST_NAME | — | — |
| 80 | LeCreatedByPersonNameDPEOSuffix | SUFFIX | — | — |
| 81 | LeCreatedByPersonNameDPEOTitle | TITLE | — | — |
| 82 | LeUpdatedByPersonNameDPEO1_1BusinessGroupId5 | BUSINESS_GROUP_ID | — | — |
| 83 | LeUpdatedByPersonNameDPEO1_1CreatedBy10 | CREATED_BY | — | — |
| 84 | LeUpdatedByPersonNameDPEO1_1CreationDate10 | CREATION_DATE | — | — |
| 85 | LeUpdatedByPersonNameDPEO1_1DisplayName1 | DISPLAY_NAME | — | — |
| 86 | LeUpdatedByPersonNameDPEO1_1EffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 87 | LeUpdatedByPersonNameDPEO1_1EffectiveStartDate1 | EFFECTIVE_START_DATE | — | — |
| 88 | LeUpdatedByPersonNameDPEO1_1FirstName1 | FIRST_NAME | — | — |
| 89 | LeUpdatedByPersonNameDPEO1_1FullName1 | FULL_NAME | — | ✅ |
| 90 | LeUpdatedByPersonNameDPEO1_1Honors1 | HONORS | — | — |
| 91 | LeUpdatedByPersonNameDPEO1_1KnownAs1 | KNOWN_AS | — | — |
| 92 | LeUpdatedByPersonNameDPEO1_1LastName1 | LAST_NAME | — | — |
| 93 | LeUpdatedByPersonNameDPEO1_1LastUpdateDate10 | LAST_UPDATE_DATE | — | — |
| 94 | LeUpdatedByPersonNameDPEO1_1LastUpdateLogin10 | LAST_UPDATE_LOGIN | — | — |
| 95 | LeUpdatedByPersonNameDPEO1_1LastUpdatedBy10 | LAST_UPDATED_BY | — | — |
| 96 | LeUpdatedByPersonNameDPEO1_1LegislationCode1 | LEGISLATION_CODE | — | — |
| 97 | LeUpdatedByPersonNameDPEO1_1ListName1 | LIST_NAME | — | — |
| 98 | LeUpdatedByPersonNameDPEO1_1MiddleNames1 | MIDDLE_NAMES | — | — |
| 99 | LeUpdatedByPersonNameDPEO1_1MilitaryRank1 | MILITARY_RANK | — | — |
| 100 | LeUpdatedByPersonNameDPEO1_1NameType1 | NAME_TYPE | — | — |
| 101 | LeUpdatedByPersonNameDPEO1_1ObjectVersionNumber9 | OBJECT_VERSION_NUMBER | — | — |
| 102 | LeUpdatedByPersonNameDPEO1_1OrderName1 | ORDER_NAME | — | — |
| 103 | LeUpdatedByPersonNameDPEO1_1PersonId5 | PERSON_ID | — | — |
| 104 | LeUpdatedByPersonNameDPEO1_1PersonNameId1 | PERSON_NAME_ID | — | — |
| 105 | LeUpdatedByPersonNameDPEO1_1PreNameAdjunct1 | PRE_NAME_ADJUNCT | — | — |
| 106 | LeUpdatedByPersonNameDPEO1_1PreviousLastName1 | PREVIOUS_LAST_NAME | — | — |
| 107 | LeUpdatedByPersonNameDPEO1_1Suffix1 | SUFFIX | — | — |
| 108 | LeUpdatedByPersonNameDPEO1_1Title1 | TITLE | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FdhCreatedByUserPEOActiveFlag2 | ACTIVE_FLAG | — | — |
| 2 | FdhCreatedByUserPEOBusinessGroupId2 | BUSINESS_GROUP_ID | — | — |
| 3 | FdhCreatedByUserPEOCreatedBy7 | CREATED_BY | — | — |
| 4 | FdhCreatedByUserPEOCreationDate7 | CREATION_DATE | — | — |
| 5 | FdhCreatedByUserPEOCredentialsEmailSent2 | CREDENTIALS_EMAIL_SENT | — | — |
| 6 | FdhCreatedByUserPEOEndDate2 | END_DATE | — | — |
| 7 | FdhCreatedByUserPEOExternalId2 | EXTERNAL_ID | — | — |
| 8 | FdhCreatedByUserPEOHrTerminated2 | HR_TERMINATED | — | — |
| 9 | FdhCreatedByUserPEOLastUpdateDate7 | LAST_UPDATE_DATE | — | — |
| 10 | FdhCreatedByUserPEOLastUpdateLogin7 | LAST_UPDATE_LOGIN | — | — |
| 11 | FdhCreatedByUserPEOLastUpdatedBy7 | LAST_UPDATED_BY | — | — |
| 12 | FdhCreatedByUserPEOMultitenancyUsername2 | MULTITENANCY_USERNAME | — | — |
| 13 | FdhCreatedByUserPEOObjectVersionNumber6 | OBJECT_VERSION_NUMBER | — | — |
| 14 | FdhCreatedByUserPEOPartyId2 | PARTY_ID | — | — |
| 15 | FdhCreatedByUserPEOPersonId2 | PERSON_ID | — | — |
| 16 | FdhCreatedByUserPEOStartDate2 | START_DATE | — | — |
| 17 | FdhCreatedByUserPEOSuspended2 | SUSPENDED | — | — |
| 18 | FdhCreatedByUserPEOUserDataChecksum2 | USER_DATA_CHECKSUM | — | — |
| 19 | FdhCreatedByUserPEOUserDistinguishedName2 | USER_DISTINGUISHED_NAME | — | — |
| 20 | FdhCreatedByUserPEOUserGuid2 | USER_GUID | — | — |
| 21 | FdhCreatedByUserPEOUserId2 | USER_ID | — | — |
| 22 | FdhCreatedByUserPEOUsername2 | USERNAME | — | — |
| 23 | FdhUpdatedByUserPEO1_1ActiveFlag3 | ACTIVE_FLAG | — | — |
| 24 | FdhUpdatedByUserPEO1_1BusinessGroupId3 | BUSINESS_GROUP_ID | — | — |
| 25 | FdhUpdatedByUserPEO1_1CreatedBy8 | CREATED_BY | — | — |
| 26 | FdhUpdatedByUserPEO1_1CreationDate8 | CREATION_DATE | — | — |
| 27 | FdhUpdatedByUserPEO1_1CredentialsEmailSent3 | CREDENTIALS_EMAIL_SENT | — | — |
| 28 | FdhUpdatedByUserPEO1_1EndDate3 | END_DATE | — | — |
| 29 | FdhUpdatedByUserPEO1_1ExternalId3 | EXTERNAL_ID | — | — |
| 30 | FdhUpdatedByUserPEO1_1HrTerminated3 | HR_TERMINATED | — | — |
| 31 | FdhUpdatedByUserPEO1_1LastUpdateDate8 | LAST_UPDATE_DATE | — | — |
| 32 | FdhUpdatedByUserPEO1_1LastUpdateLogin8 | LAST_UPDATE_LOGIN | — | — |
| 33 | FdhUpdatedByUserPEO1_1LastUpdatedBy8 | LAST_UPDATED_BY | — | — |
| 34 | FdhUpdatedByUserPEO1_1MultitenancyUsername3 | MULTITENANCY_USERNAME | — | — |
| 35 | FdhUpdatedByUserPEO1_1ObjectVersionNumber7 | OBJECT_VERSION_NUMBER | — | — |
| 36 | FdhUpdatedByUserPEO1_1PartyId3 | PARTY_ID | — | — |
| 37 | FdhUpdatedByUserPEO1_1PersonId3 | PERSON_ID | — | — |
| 38 | FdhUpdatedByUserPEO1_1StartDate3 | START_DATE | — | — |
| 39 | FdhUpdatedByUserPEO1_1Suspended3 | SUSPENDED | — | — |
| 40 | FdhUpdatedByUserPEO1_1UserDataChecksum3 | USER_DATA_CHECKSUM | — | — |
| 41 | FdhUpdatedByUserPEO1_1UserDistinguishedName3 | USER_DISTINGUISHED_NAME | — | — |
| 42 | FdhUpdatedByUserPEO1_1UserGuid3 | USER_GUID | — | — |
| 43 | FdhUpdatedByUserPEO1_1UserId3 | USER_ID | — | — |
| 44 | FdhUpdatedByUserPEO1_1Username3 | USERNAME | — | — |
| 45 | LeCreatedByUserPEOActiveFlag | ACTIVE_FLAG | — | — |
| 46 | LeCreatedByUserPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 47 | LeCreatedByUserPEOCreatedBy5 | CREATED_BY | — | — |
| 48 | LeCreatedByUserPEOCreationDate5 | CREATION_DATE | — | — |
| 49 | LeCreatedByUserPEOCredentialsEmailSent | CREDENTIALS_EMAIL_SENT | — | — |
| 50 | LeCreatedByUserPEOEndDate | END_DATE | — | — |
| 51 | LeCreatedByUserPEOExternalId | EXTERNAL_ID | — | — |
| 52 | LeCreatedByUserPEOHrTerminated | HR_TERMINATED | — | — |
| 53 | LeCreatedByUserPEOLastUpdateDate5 | LAST_UPDATE_DATE | — | — |
| 54 | LeCreatedByUserPEOLastUpdateLogin5 | LAST_UPDATE_LOGIN | — | — |
| 55 | LeCreatedByUserPEOLastUpdatedBy5 | LAST_UPDATED_BY | — | — |
| 56 | LeCreatedByUserPEOMultitenancyUsername | MULTITENANCY_USERNAME | — | — |
| 57 | LeCreatedByUserPEOObjectVersionNumber4 | OBJECT_VERSION_NUMBER | — | — |
| 58 | LeCreatedByUserPEOPartyId | PARTY_ID | — | — |
| 59 | LeCreatedByUserPEOPersonId | PERSON_ID | — | — |
| 60 | LeCreatedByUserPEOStartDate | START_DATE | — | — |
| 61 | LeCreatedByUserPEOSuspended | SUSPENDED | — | — |
| 62 | LeCreatedByUserPEOUserDataChecksum | USER_DATA_CHECKSUM | — | — |
| 63 | LeCreatedByUserPEOUserDistinguishedName | USER_DISTINGUISHED_NAME | — | — |
| 64 | LeCreatedByUserPEOUserGuid | USER_GUID | — | — |
| 65 | LeCreatedByUserPEOUserId | USER_ID | — | — |
| 66 | LeCreatedByUserPEOUsername | USERNAME | — | — |
| 67 | LeUpdatedByUserPEO1_1ActiveFlag1 | ACTIVE_FLAG | — | — |
| 68 | LeUpdatedByUserPEO1_1BusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 69 | LeUpdatedByUserPEO1_1CreatedBy6 | CREATED_BY | — | — |
| 70 | LeUpdatedByUserPEO1_1CreationDate6 | CREATION_DATE | — | — |
| 71 | LeUpdatedByUserPEO1_1CredentialsEmailSent1 | CREDENTIALS_EMAIL_SENT | — | — |
| 72 | LeUpdatedByUserPEO1_1EndDate1 | END_DATE | — | — |
| 73 | LeUpdatedByUserPEO1_1ExternalId1 | EXTERNAL_ID | — | — |
| 74 | LeUpdatedByUserPEO1_1HrTerminated1 | HR_TERMINATED | — | — |
| 75 | LeUpdatedByUserPEO1_1LastUpdateDate6 | LAST_UPDATE_DATE | — | — |
| 76 | LeUpdatedByUserPEO1_1LastUpdateLogin6 | LAST_UPDATE_LOGIN | — | — |
| 77 | LeUpdatedByUserPEO1_1LastUpdatedBy6 | LAST_UPDATED_BY | — | — |
| 78 | LeUpdatedByUserPEO1_1MultitenancyUsername1 | MULTITENANCY_USERNAME | — | — |
| 79 | LeUpdatedByUserPEO1_1ObjectVersionNumber5 | OBJECT_VERSION_NUMBER | — | — |
| 80 | LeUpdatedByUserPEO1_1PartyId1 | PARTY_ID | — | — |
| 81 | LeUpdatedByUserPEO1_1PersonId1 | PERSON_ID | — | — |
| 82 | LeUpdatedByUserPEO1_1StartDate1 | START_DATE | — | — |
| 83 | LeUpdatedByUserPEO1_1Suspended1 | SUSPENDED | — | — |
| 84 | LeUpdatedByUserPEO1_1UserDataChecksum1 | USER_DATA_CHECKSUM | — | — |
| 85 | LeUpdatedByUserPEO1_1UserDistinguishedName1 | USER_DISTINGUISHED_NAME | — | — |
| 86 | LeUpdatedByUserPEO1_1UserGuid1 | USER_GUID | — | — |
| 87 | LeUpdatedByUserPEO1_1UserId1 | USER_ID | — | — |
| 88 | LeUpdatedByUserPEO1_1Username1 | USERNAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
