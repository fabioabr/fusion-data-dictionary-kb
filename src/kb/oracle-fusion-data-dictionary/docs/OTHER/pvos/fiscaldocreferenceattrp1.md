---
id: DOC-OTHER-PVO-FiscalDocReferenceAttrP1
doc_type: system-doc
title: "FiscalDocReferenceAttrP1 — PVO Cross-Module"
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
  - FiscalDocReferenceAttrP1
  - fiscaldocreferenceattrp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FiscalDocReferenceAttrP1

## 📌 Visão Geral

View Object para extração BICC de dados de Fiscal Doc Reference Attr P1. Acessa as tabelas: CMF_FD_LOC_INFO_PERSIST_OTBI_V, CMF_FISCAL_DOC_HEADERS, CMF_FISCAL_DOC_REF_ATTRIBUTES (+5).

**Caminho:** `FscmTopModelAM.FiscalDocumentAM.FiscalDocReferenceAttrP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 618 | 8 | 1 | 13 | 2% |

---

## 🔗 Tabelas Relacionadas

- [[cmf_fd_loc_info_persist_otbi_v|CMF_FD_LOC_INFO_PERSIST_OTBI_V]] — 79 atributos
- [[cmf_fiscal_doc_headers|CMF_FISCAL_DOC_HEADERS]] — 123 atributos (10 BICC)
- [[cmf_fiscal_doc_ref_attributes|CMF_FISCAL_DOC_REF_ATTRIBUTES]] — 28 atributos (1 PKs, 1 BICC)
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 21 atributos
- [[jg_fscl_hdrs_atrb_ext_all|JG_FSCL_HDRS_ATRB_EXT_ALL]] — 55 atributos
- [[jg_fscl_hdr_dtls_atrb_ext_all|JG_FSCL_HDR_DTLS_ATRB_EXT_ALL]] — 18 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 162 atributos (2 BICC)
- [[per_users|PER_USERS]] — 132 atributos

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
| 1 | DHIdFiscalDocHeadersPEOAccessKeyNumber1 | ACCESS_KEY_NUMBER | — | — |
| 2 | DHIdFiscalDocHeadersPEOAcknowledgedDate1 | ACKNOWLEDGED_DATE | — | — |
| 3 | DHIdFiscalDocHeadersPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 4 | DHIdFiscalDocHeadersPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 5 | DHIdFiscalDocHeadersPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 6 | DHIdFiscalDocHeadersPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 7 | DHIdFiscalDocHeadersPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 8 | DHIdFiscalDocHeadersPEOBillToBusinessUnitId1 | BILL_TO_BUSINESS_UNIT_ID | — | — |
| 9 | DHIdFiscalDocHeadersPEOChargeAllocationStatus1 | CHARGE_ALLOCATION_STATUS | — | — |
| 10 | DHIdFiscalDocHeadersPEOCmrInterfacedFlag1 | CMR_INTERFACED_FLAG | — | — |
| 11 | DHIdFiscalDocHeadersPEOConversionRate1 | CONVERSION_RATE | — | — |
| 12 | DHIdFiscalDocHeadersPEOConverstionType1 | CONVERSTION_TYPE | — | — |
| 13 | DHIdFiscalDocHeadersPEOCountryCode1 | COUNTRY_CODE | — | — |
| 14 | DHIdFiscalDocHeadersPEOCreatedBy9 | CREATED_BY | — | — |
| 15 | DHIdFiscalDocHeadersPEOCreationDate9 | CREATION_DATE | — | — |
| 16 | DHIdFiscalDocHeadersPEOCurrency1 | CURRENCY | — | — |
| 17 | DHIdFiscalDocHeadersPEODocumentHeaderId3 | DOCUMENT_HEADER_ID | — | — |
| 18 | DHIdFiscalDocHeadersPEODocumentNumber2 | DOCUMENT_NUMBER | — | — |
| 19 | DHIdFiscalDocHeadersPEODocumentStatus1 | DOCUMENT_STATUS | — | — |
| 20 | DHIdFiscalDocHeadersPEODocumentType1 | DOCUMENT_TYPE | — | — |
| 21 | DHIdFiscalDocHeadersPEOExternalSystemRefId2 | EXTERNAL_SYSTEM_REF_ID | — | — |
| 22 | DHIdFiscalDocHeadersPEOExternalSystemReference2 | EXTERNAL_SYSTEM_REFERENCE | — | — |
| 23 | DHIdFiscalDocHeadersPEOFiscalDocAssoctnsId1 | FISCAL_DOC_ASSOCTNS_ID | — | — |
| 24 | DHIdFiscalDocHeadersPEOFiscalProcOptionsId2 | FISCAL_PROC_OPTIONS_ID | — | — |
| 25 | DHIdFiscalDocHeadersPEOInterfacedFlag1 | INTERFACED_FLAG | — | — |
| 26 | DHIdFiscalDocHeadersPEOInvoiceInterfacedFlag1 | INVOICE_INTERFACED_FLAG | — | — |
| 27 | DHIdFiscalDocHeadersPEOIssueDate1 | ISSUE_DATE | — | — |
| 28 | DHIdFiscalDocHeadersPEOIssuerLocationId1 | ISSUER_LOCATION_ID | — | — |
| 29 | DHIdFiscalDocHeadersPEOIssuerPartyId1 | ISSUER_PARTY_ID | — | — |
| 30 | DHIdFiscalDocHeadersPEOIssuerPartySiteId1 | ISSUER_PARTY_SITE_ID | — | — |
| 31 | DHIdFiscalDocHeadersPEOIssuerTaxId1 | ISSUER_TAX_ID | — | — |
| 32 | DHIdFiscalDocHeadersPEOItemLineAmount1 | ITEM_LINE_AMOUNT | — | — |
| 33 | DHIdFiscalDocHeadersPEOJobDefinitionName4 | JOB_DEFINITION_NAME | — | — |
| 34 | DHIdFiscalDocHeadersPEOJobDefinitionPackage4 | JOB_DEFINITION_PACKAGE | — | — |
| 35 | DHIdFiscalDocHeadersPEOLastUpdateDate9 | LAST_UPDATE_DATE | — | — |
| 36 | DHIdFiscalDocHeadersPEOLastUpdateLogin9 | LAST_UPDATE_LOGIN | — | — |
| 37 | DHIdFiscalDocHeadersPEOLastUpdatedBy9 | LAST_UPDATED_BY | — | — |
| 38 | DHIdFiscalDocHeadersPEOModel1 | MODEL | — | — |
| 39 | DHIdFiscalDocHeadersPEOObjectVersionNumber8 | OBJECT_VERSION_NUMBER | — | — |
| 40 | DHIdFiscalDocHeadersPEOOperationType1 | OPERATION_TYPE | — | — |
| 41 | DHIdFiscalDocHeadersPEOParentDocumentHeaderId1 | PARENT_DOCUMENT_HEADER_ID | — | — |
| 42 | DHIdFiscalDocHeadersPEOReason1 | REASON | — | — |
| 43 | DHIdFiscalDocHeadersPEOReceiverLocationId1 | RECEIVER_LOCATION_ID | — | — |
| 44 | DHIdFiscalDocHeadersPEOReceiverPartyId1 | RECEIVER_PARTY_ID | — | — |
| 45 | DHIdFiscalDocHeadersPEOReceiverPartySiteId1 | RECEIVER_PARTY_SITE_ID | — | — |
| 46 | DHIdFiscalDocHeadersPEOReceiverTaxId1 | RECEIVER_TAX_ID | — | — |
| 47 | DHIdFiscalDocHeadersPEOReferencedStatus1 | REFERENCED_STATUS | — | — |
| 48 | DHIdFiscalDocHeadersPEORequestId4 | REQUEST_ID | — | — |
| 49 | DHIdFiscalDocHeadersPEOSchedulesAllocatedFlag1 | SCHEDULES_ALLOCATED_FLAG | — | — |
| 50 | DHIdFiscalDocHeadersPEOSeries2 | SERIES | — | — |
| 51 | DHIdFiscalDocHeadersPEOShipfromLocationId1 | SHIPFROM_LOCATION_ID | — | — |
| 52 | DHIdFiscalDocHeadersPEOShipfromPartyId1 | SHIPFROM_PARTY_ID | — | — |
| 53 | DHIdFiscalDocHeadersPEOShipfromPartySiteId1 | SHIPFROM_PARTY_SITE_ID | — | — |
| 54 | DHIdFiscalDocHeadersPEOShipfromTaxId1 | SHIPFROM_TAX_ID | — | — |
| 55 | DHIdFiscalDocHeadersPEOShiptoLocationId1 | SHIPTO_LOCATION_ID | — | — |
| 56 | DHIdFiscalDocHeadersPEOShiptoPartyId1 | SHIPTO_PARTY_ID | — | — |
| 57 | DHIdFiscalDocHeadersPEOShiptoPartySiteId1 | SHIPTO_PARTY_SITE_ID | — | — |
| 58 | DHIdFiscalDocHeadersPEOShiptoTaxId1 | SHIPTO_TAX_ID | — | — |
| 59 | DHIdFiscalDocHeadersPEOSoldToLegalEntityId1 | SOLD_TO_LEGAL_ENTITY_ID | — | — |
| 60 | DHIdFiscalDocHeadersPEOSourceDocumentType2 | SOURCE_DOCUMENT_TYPE | — | — |
| 61 | DHIdFiscalDocHeadersPEOSubseries1 | SUBSERIES | — | — |
| 62 | DHIdFiscalDocHeadersPEOTaxCalculationStatus1 | TAX_CALCULATION_STATUS | — | — |
| 63 | DHIdFiscalDocHeadersPEOTotalAmount1 | TOTAL_AMOUNT | — | — |
| 64 | DHIdFiscalDocHeadersPEOValidationStatus1 | VALIDATION_STATUS | — | — |
| 65 | RDHIdFiscalDocHeadersPEOAccessKeyNumber | ACCESS_KEY_NUMBER | — | ✅ |
| 66 | RDHIdFiscalDocHeadersPEOAcknowledgedDate | ACKNOWLEDGED_DATE | — | — |
| 67 | RDHIdFiscalDocHeadersPEOBillToBusinessUnitId | BILL_TO_BUSINESS_UNIT_ID | — | — |
| 68 | RDHIdFiscalDocHeadersPEOChargeAllocationStatus | CHARGE_ALLOCATION_STATUS | — | — |
| 69 | RDHIdFiscalDocHeadersPEOCmrInterfacedFlag | CMR_INTERFACED_FLAG | — | — |
| 70 | RDHIdFiscalDocHeadersPEOConversionRate | CONVERSION_RATE | — | — |
| 71 | RDHIdFiscalDocHeadersPEOConverstionType | CONVERSTION_TYPE | — | — |
| 72 | RDHIdFiscalDocHeadersPEOCountryCode | COUNTRY_CODE | — | — |
| 73 | RDHIdFiscalDocHeadersPEOCreatedBy1 | CREATED_BY | — | — |
| 74 | RDHIdFiscalDocHeadersPEOCreationDate1 | CREATION_DATE | — | ✅ |
| 75 | RDHIdFiscalDocHeadersPEOCurrency | CURRENCY | — | — |
| 76 | RDHIdFiscalDocHeadersPEODocumentHeaderId1 | DOCUMENT_HEADER_ID | — | — |
| 77 | RDHIdFiscalDocHeadersPEODocumentNumber | DOCUMENT_NUMBER | — | ✅ |
| 78 | RDHIdFiscalDocHeadersPEODocumentStatus | DOCUMENT_STATUS | — | — |
| 79 | RDHIdFiscalDocHeadersPEODocumentType | DOCUMENT_TYPE | — | ✅ |
| 80 | RDHIdFiscalDocHeadersPEOExternalSystemRefId1 | EXTERNAL_SYSTEM_REF_ID | — | — |
| 81 | RDHIdFiscalDocHeadersPEOExternalSystemReference1 | EXTERNAL_SYSTEM_REFERENCE | — | — |
| 82 | RDHIdFiscalDocHeadersPEOFiscalDocAssoctnsId | FISCAL_DOC_ASSOCTNS_ID | — | — |
| 83 | RDHIdFiscalDocHeadersPEOFiscalProcOptionsId | FISCAL_PROC_OPTIONS_ID | — | — |
| 84 | RDHIdFiscalDocHeadersPEOInterfacedFlag | INTERFACED_FLAG | — | — |
| 85 | RDHIdFiscalDocHeadersPEOInvoiceInterfacedFlag | INVOICE_INTERFACED_FLAG | — | — |
| 86 | RDHIdFiscalDocHeadersPEOIssueDate | ISSUE_DATE | — | ✅ |
| 87 | RDHIdFiscalDocHeadersPEOIssuerLocationId | ISSUER_LOCATION_ID | — | — |
| 88 | RDHIdFiscalDocHeadersPEOIssuerPartyId | ISSUER_PARTY_ID | — | — |
| 89 | RDHIdFiscalDocHeadersPEOIssuerPartySiteId | ISSUER_PARTY_SITE_ID | — | — |
| 90 | RDHIdFiscalDocHeadersPEOIssuerTaxId | ISSUER_TAX_ID | — | — |
| 91 | RDHIdFiscalDocHeadersPEOItemLineAmount | ITEM_LINE_AMOUNT | — | — |
| 92 | RDHIdFiscalDocHeadersPEOJobDefinitionName1 | JOB_DEFINITION_NAME | — | — |
| 93 | RDHIdFiscalDocHeadersPEOJobDefinitionPackage1 | JOB_DEFINITION_PACKAGE | — | — |
| 94 | RDHIdFiscalDocHeadersPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 95 | RDHIdFiscalDocHeadersPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 96 | RDHIdFiscalDocHeadersPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 97 | RDHIdFiscalDocHeadersPEOModel | MODEL | — | ✅ |
| 98 | RDHIdFiscalDocHeadersPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 99 | RDHIdFiscalDocHeadersPEOOperationType | OPERATION_TYPE | — | — |
| 100 | RDHIdFiscalDocHeadersPEOParentDocumentHeaderId | PARENT_DOCUMENT_HEADER_ID | — | — |
| 101 | RDHIdFiscalDocHeadersPEOReason | REASON | — | — |
| 102 | RDHIdFiscalDocHeadersPEOReceiverLocationId | RECEIVER_LOCATION_ID | — | — |
| 103 | RDHIdFiscalDocHeadersPEOReceiverPartyId | RECEIVER_PARTY_ID | — | — |
| 104 | RDHIdFiscalDocHeadersPEOReceiverPartySiteId | RECEIVER_PARTY_SITE_ID | — | — |
| 105 | RDHIdFiscalDocHeadersPEOReceiverTaxId | RECEIVER_TAX_ID | — | — |
| 106 | RDHIdFiscalDocHeadersPEOReferencedStatus | REFERENCED_STATUS | — | — |
| 107 | RDHIdFiscalDocHeadersPEORequestId1 | REQUEST_ID | — | — |
| 108 | RDHIdFiscalDocHeadersPEOSchedulesAllocatedFlag | SCHEDULES_ALLOCATED_FLAG | — | — |
| 109 | RDHIdFiscalDocHeadersPEOSeries | SERIES | — | ✅ |
| 110 | RDHIdFiscalDocHeadersPEOShipfromLocationId | SHIPFROM_LOCATION_ID | — | — |
| 111 | RDHIdFiscalDocHeadersPEOShipfromPartyId | SHIPFROM_PARTY_ID | — | — |
| 112 | RDHIdFiscalDocHeadersPEOShipfromPartySiteId | SHIPFROM_PARTY_SITE_ID | — | — |
| 113 | RDHIdFiscalDocHeadersPEOShipfromTaxId | SHIPFROM_TAX_ID | — | — |
| 114 | RDHIdFiscalDocHeadersPEOShiptoLocationId | SHIPTO_LOCATION_ID | — | — |
| 115 | RDHIdFiscalDocHeadersPEOShiptoPartyId | SHIPTO_PARTY_ID | — | — |
| 116 | RDHIdFiscalDocHeadersPEOShiptoPartySiteId | SHIPTO_PARTY_SITE_ID | — | — |
| 117 | RDHIdFiscalDocHeadersPEOShiptoTaxId | SHIPTO_TAX_ID | — | — |
| 118 | RDHIdFiscalDocHeadersPEOSoldToLegalEntityId | SOLD_TO_LEGAL_ENTITY_ID | — | — |
| 119 | RDHIdFiscalDocHeadersPEOSourceDocumentType1 | SOURCE_DOCUMENT_TYPE | — | ✅ |
| 120 | RDHIdFiscalDocHeadersPEOSubseries | SUBSERIES | — | ✅ |
| 121 | RDHIdFiscalDocHeadersPEOTaxCalculationStatus | TAX_CALCULATION_STATUS | — | — |
| 122 | RDHIdFiscalDocHeadersPEOTotalAmount | TOTAL_AMOUNT | — | — |
| 123 | RDHIdFiscalDocHeadersPEOValidationStatus | VALIDATION_STATUS | — | — |

### [[cmf_fiscal_doc_ref_attributes|CMF_FISCAL_DOC_REF_ATTRIBUTES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FdRefAttributeId | FD_REF_ATTRIBUTE_ID | 🔑 | ✅ |
| 2 | FiscalDocReferenceAttrPEOCreatedBy | CREATED_BY | — | — |
| 3 | FiscalDocReferenceAttrPEOCreationDate | CREATION_DATE | — | — |
| 4 | FiscalDocReferenceAttrPEODocumentHeaderId | DOCUMENT_HEADER_ID | — | — |
| 5 | FiscalDocReferenceAttrPEODocumentLineId | DOCUMENT_LINE_ID | — | — |
| 6 | FiscalDocReferenceAttrPEOExternalSystemRefId | EXTERNAL_SYSTEM_REF_ID | — | — |
| 7 | FiscalDocReferenceAttrPEOExternalSystemReference | EXTERNAL_SYSTEM_REFERENCE | — | — |
| 8 | FiscalDocReferenceAttrPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 9 | FiscalDocReferenceAttrPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 10 | FiscalDocReferenceAttrPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 11 | FiscalDocReferenceAttrPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | FiscalDocReferenceAttrPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | FiscalDocReferenceAttrPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | FiscalDocReferenceAttrPEORefAccessKeyNbr | REF_ACCESS_KEY_NBR | — | — |
| 15 | FiscalDocReferenceAttrPEORefDocumentHeaderId | REF_DOCUMENT_HEADER_ID | — | — |
| 16 | FiscalDocReferenceAttrPEORefDocumentLineId | REF_DOCUMENT_LINE_ID | — | — |
| 17 | FiscalDocReferenceAttrPEORefFdDocumentType | REF_FD_DOCUMENT_TYPE | — | — |
| 18 | FiscalDocReferenceAttrPEORefFdIssuerDate | REF_FD_ISSUER_DATE | — | — |
| 19 | FiscalDocReferenceAttrPEORefFdIssuerId | REF_FD_ISSUER_ID | — | — |
| 20 | FiscalDocReferenceAttrPEORefFdIssuerState | REF_FD_ISSUER_STATE | — | — |
| 21 | FiscalDocReferenceAttrPEORefFdModel | REF_FD_MODEL | — | — |
| 22 | FiscalDocReferenceAttrPEORefFdNumber | REF_FD_NUMBER | — | — |
| 23 | FiscalDocReferenceAttrPEORefFdSeries | REF_FD_SERIES | — | — |
| 24 | FiscalDocReferenceAttrPEORefFdSource | REF_FD_SOURCE | — | — |
| 25 | FiscalDocReferenceAttrPEORefFdSubseries | REF_FD_SUBSERIES | — | — |
| 26 | FiscalDocReferenceAttrPEORefFdTaxPayerId | REF_FD_TAX_PAYER_ID | — | — |
| 27 | FiscalDocReferenceAttrPEORequestId | REQUEST_ID | — | — |
| 28 | FiscalDocReferenceAttrPEOSourceDocumentType | SOURCE_DOCUMENT_TYPE | — | — |

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

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedByPersonNameDPEOBusinessGroupId2 | BUSINESS_GROUP_ID | — | — |
| 2 | CreatedByPersonNameDPEOCreatedBy7 | CREATED_BY | — | — |
| 3 | CreatedByPersonNameDPEOCreationDate7 | CREATION_DATE | — | — |
| 4 | CreatedByPersonNameDPEODisplayName | DISPLAY_NAME | — | — |
| 5 | CreatedByPersonNameDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 6 | CreatedByPersonNameDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 7 | CreatedByPersonNameDPEOFirstName | FIRST_NAME | — | — |
| 8 | CreatedByPersonNameDPEOFullName | FULL_NAME | — | — |
| 9 | CreatedByPersonNameDPEOHonors | HONORS | — | — |
| 10 | CreatedByPersonNameDPEOKnownAs | KNOWN_AS | — | — |
| 11 | CreatedByPersonNameDPEOLastName | LAST_NAME | — | — |
| 12 | CreatedByPersonNameDPEOLastUpdateDate7 | LAST_UPDATE_DATE | — | — |
| 13 | CreatedByPersonNameDPEOLastUpdateLogin7 | LAST_UPDATE_LOGIN | — | — |
| 14 | CreatedByPersonNameDPEOLastUpdatedBy7 | LAST_UPDATED_BY | — | — |
| 15 | CreatedByPersonNameDPEOLegislationCode | LEGISLATION_CODE | — | — |
| 16 | CreatedByPersonNameDPEOListName | LIST_NAME | — | — |
| 17 | CreatedByPersonNameDPEOMiddleNames | MIDDLE_NAMES | — | — |
| 18 | CreatedByPersonNameDPEOMilitaryRank | MILITARY_RANK | — | — |
| 19 | CreatedByPersonNameDPEONameType | NAME_TYPE | — | — |
| 20 | CreatedByPersonNameDPEOObjectVersionNumber6 | OBJECT_VERSION_NUMBER | — | — |
| 21 | CreatedByPersonNameDPEOOrderName | ORDER_NAME | — | — |
| 22 | CreatedByPersonNameDPEOPersonId2 | PERSON_ID | — | — |
| 23 | CreatedByPersonNameDPEOPersonNameId | PERSON_NAME_ID | — | — |
| 24 | CreatedByPersonNameDPEOPreNameAdjunct | PRE_NAME_ADJUNCT | — | — |
| 25 | CreatedByPersonNameDPEOPreviousLastName | PREVIOUS_LAST_NAME | — | — |
| 26 | CreatedByPersonNameDPEOSuffix | SUFFIX | — | — |
| 27 | CreatedByPersonNameDPEOTitle | TITLE | — | — |
| 28 | LastUpdatedByPersonNameDPEO1_1BusinessGroupId3 | BUSINESS_GROUP_ID | — | — |
| 29 | LastUpdatedByPersonNameDPEO1_1CreatedBy8 | CREATED_BY | — | — |
| 30 | LastUpdatedByPersonNameDPEO1_1CreationDate8 | CREATION_DATE | — | — |
| 31 | LastUpdatedByPersonNameDPEO1_1DisplayName1 | DISPLAY_NAME | — | — |
| 32 | LastUpdatedByPersonNameDPEO1_1EffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 33 | LastUpdatedByPersonNameDPEO1_1EffectiveStartDate1 | EFFECTIVE_START_DATE | — | — |
| 34 | LastUpdatedByPersonNameDPEO1_1FirstName1 | FIRST_NAME | — | — |
| 35 | LastUpdatedByPersonNameDPEO1_1FullName1 | FULL_NAME | — | — |
| 36 | LastUpdatedByPersonNameDPEO1_1Honors1 | HONORS | — | — |
| 37 | LastUpdatedByPersonNameDPEO1_1KnownAs1 | KNOWN_AS | — | — |
| 38 | LastUpdatedByPersonNameDPEO1_1LastName1 | LAST_NAME | — | — |
| 39 | LastUpdatedByPersonNameDPEO1_1LastUpdateDate8 | LAST_UPDATE_DATE | — | — |
| 40 | LastUpdatedByPersonNameDPEO1_1LastUpdateLogin8 | LAST_UPDATE_LOGIN | — | — |
| 41 | LastUpdatedByPersonNameDPEO1_1LastUpdatedBy8 | LAST_UPDATED_BY | — | — |
| 42 | LastUpdatedByPersonNameDPEO1_1LegislationCode1 | LEGISLATION_CODE | — | — |
| 43 | LastUpdatedByPersonNameDPEO1_1ListName1 | LIST_NAME | — | — |
| 44 | LastUpdatedByPersonNameDPEO1_1MiddleNames1 | MIDDLE_NAMES | — | — |
| 45 | LastUpdatedByPersonNameDPEO1_1MilitaryRank1 | MILITARY_RANK | — | — |
| 46 | LastUpdatedByPersonNameDPEO1_1NameType1 | NAME_TYPE | — | — |
| 47 | LastUpdatedByPersonNameDPEO1_1ObjectVersionNumber7 | OBJECT_VERSION_NUMBER | — | — |
| 48 | LastUpdatedByPersonNameDPEO1_1OrderName1 | ORDER_NAME | — | — |
| 49 | LastUpdatedByPersonNameDPEO1_1PersonId3 | PERSON_ID | — | — |
| 50 | LastUpdatedByPersonNameDPEO1_1PersonNameId1 | PERSON_NAME_ID | — | — |
| 51 | LastUpdatedByPersonNameDPEO1_1PreNameAdjunct1 | PRE_NAME_ADJUNCT | — | — |
| 52 | LastUpdatedByPersonNameDPEO1_1PreviousLastName1 | PREVIOUS_LAST_NAME | — | — |
| 53 | LastUpdatedByPersonNameDPEO1_1Suffix1 | SUFFIX | — | — |
| 54 | LastUpdatedByPersonNameDPEO1_1Title1 | TITLE | — | — |
| 55 | RDCreatedByPersonNameDPEOBusinessGroupId2 | BUSINESS_GROUP_ID | — | — |
| 56 | RDCreatedByPersonNameDPEOCreatedBy2 | CREATED_BY | — | — |
| 57 | RDCreatedByPersonNameDPEOCreationDate2 | CREATION_DATE | — | — |
| 58 | RDCreatedByPersonNameDPEODisplayName | DISPLAY_NAME | — | — |
| 59 | RDCreatedByPersonNameDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 60 | RDCreatedByPersonNameDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 61 | RDCreatedByPersonNameDPEOFirstName | FIRST_NAME | — | — |
| 62 | RDCreatedByPersonNameDPEOFullName | FULL_NAME | — | ✅ |
| 63 | RDCreatedByPersonNameDPEOHonors | HONORS | — | — |
| 64 | RDCreatedByPersonNameDPEOKnownAs | KNOWN_AS | — | — |
| 65 | RDCreatedByPersonNameDPEOLastName | LAST_NAME | — | — |
| 66 | RDCreatedByPersonNameDPEOLastUpdateDate2 | LAST_UPDATE_DATE | — | — |
| 67 | RDCreatedByPersonNameDPEOLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 68 | RDCreatedByPersonNameDPEOLastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 69 | RDCreatedByPersonNameDPEOLegislationCode | LEGISLATION_CODE | — | — |
| 70 | RDCreatedByPersonNameDPEOListName | LIST_NAME | — | — |
| 71 | RDCreatedByPersonNameDPEOMiddleNames | MIDDLE_NAMES | — | — |
| 72 | RDCreatedByPersonNameDPEOMilitaryRank | MILITARY_RANK | — | — |
| 73 | RDCreatedByPersonNameDPEONameType | NAME_TYPE | — | — |
| 74 | RDCreatedByPersonNameDPEOObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 75 | RDCreatedByPersonNameDPEOOrderName | ORDER_NAME | — | — |
| 76 | RDCreatedByPersonNameDPEOPersonId2 | PERSON_ID | — | — |
| 77 | RDCreatedByPersonNameDPEOPersonNameId | PERSON_NAME_ID | — | — |
| 78 | RDCreatedByPersonNameDPEOPreNameAdjunct | PRE_NAME_ADJUNCT | — | — |
| 79 | RDCreatedByPersonNameDPEOPreviousLastName | PREVIOUS_LAST_NAME | — | — |
| 80 | RDCreatedByPersonNameDPEOSuffix | SUFFIX | — | — |
| 81 | RDCreatedByPersonNameDPEOTitle | TITLE | — | — |
| 82 | RDLastUpdtdByPersonNameDPEOBusinessGroupId3 | BUSINESS_GROUP_ID | — | — |
| 83 | RDLastUpdtdByPersonNameDPEOCreatedBy3 | CREATED_BY | — | — |
| 84 | RDLastUpdtdByPersonNameDPEOCreationDate3 | CREATION_DATE | — | — |
| 85 | RDLastUpdtdByPersonNameDPEODisplayName1 | DISPLAY_NAME | — | — |
| 86 | RDLastUpdtdByPersonNameDPEOEffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 87 | RDLastUpdtdByPersonNameDPEOEffectiveStartDate1 | EFFECTIVE_START_DATE | — | — |
| 88 | RDLastUpdtdByPersonNameDPEOFirstName1 | FIRST_NAME | — | — |
| 89 | RDLastUpdtdByPersonNameDPEOFullName1 | FULL_NAME | — | ✅ |
| 90 | RDLastUpdtdByPersonNameDPEOHonors1 | HONORS | — | — |
| 91 | RDLastUpdtdByPersonNameDPEOKnownAs1 | KNOWN_AS | — | — |
| 92 | RDLastUpdtdByPersonNameDPEOLastName1 | LAST_NAME | — | — |
| 93 | RDLastUpdtdByPersonNameDPEOLastUpdateDate3 | LAST_UPDATE_DATE | — | — |
| 94 | RDLastUpdtdByPersonNameDPEOLastUpdateLogin3 | LAST_UPDATE_LOGIN | — | — |
| 95 | RDLastUpdtdByPersonNameDPEOLastUpdatedBy3 | LAST_UPDATED_BY | — | — |
| 96 | RDLastUpdtdByPersonNameDPEOLegislationCode1 | LEGISLATION_CODE | — | — |
| 97 | RDLastUpdtdByPersonNameDPEOListName1 | LIST_NAME | — | — |
| 98 | RDLastUpdtdByPersonNameDPEOMiddleNames1 | MIDDLE_NAMES | — | — |
| 99 | RDLastUpdtdByPersonNameDPEOMilitaryRank1 | MILITARY_RANK | — | — |
| 100 | RDLastUpdtdByPersonNameDPEONameType1 | NAME_TYPE | — | — |
| 101 | RDLastUpdtdByPersonNameDPEOObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 102 | RDLastUpdtdByPersonNameDPEOOrderName1 | ORDER_NAME | — | — |
| 103 | RDLastUpdtdByPersonNameDPEOPersonId3 | PERSON_ID | — | — |
| 104 | RDLastUpdtdByPersonNameDPEOPersonNameId1 | PERSON_NAME_ID | — | — |
| 105 | RDLastUpdtdByPersonNameDPEOPreNameAdjunct1 | PRE_NAME_ADJUNCT | — | — |
| 106 | RDLastUpdtdByPersonNameDPEOPreviousLastName1 | PREVIOUS_LAST_NAME | — | — |
| 107 | RDLastUpdtdByPersonNameDPEOSuffix1 | SUFFIX | — | — |
| 108 | RDLastUpdtdByPersonNameDPEOTitle1 | TITLE | — | — |
| 109 | RefAttrCreatedByPersonNameDPBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 110 | RefAttrCreatedByPersonNameDPCreatedBy | CREATED_BY | — | — |
| 111 | RefAttrCreatedByPersonNameDPCreationDate | CREATION_DATE | — | — |
| 112 | RefAttrCreatedByPersonNameDPDisplayName | DISPLAY_NAME | — | — |
| 113 | RefAttrCreatedByPersonNameDPEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 114 | RefAttrCreatedByPersonNameDPEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 115 | RefAttrCreatedByPersonNameDPFirstName | FIRST_NAME | — | — |
| 116 | RefAttrCreatedByPersonNameDPFullName | FULL_NAME | — | — |
| 117 | RefAttrCreatedByPersonNameDPHonors | HONORS | — | — |
| 118 | RefAttrCreatedByPersonNameDPKnownAs | KNOWN_AS | — | — |
| 119 | RefAttrCreatedByPersonNameDPLastName | LAST_NAME | — | — |
| 120 | RefAttrCreatedByPersonNameDPLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 121 | RefAttrCreatedByPersonNameDPLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 122 | RefAttrCreatedByPersonNameDPLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 123 | RefAttrCreatedByPersonNameDPLegislationCode | LEGISLATION_CODE | — | — |
| 124 | RefAttrCreatedByPersonNameDPListName | LIST_NAME | — | — |
| 125 | RefAttrCreatedByPersonNameDPMiddleNames | MIDDLE_NAMES | — | — |
| 126 | RefAttrCreatedByPersonNameDPMilitaryRank | MILITARY_RANK | — | — |
| 127 | RefAttrCreatedByPersonNameDPNameType | NAME_TYPE | — | — |
| 128 | RefAttrCreatedByPersonNameDPObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 129 | RefAttrCreatedByPersonNameDPOrderName | ORDER_NAME | — | — |
| 130 | RefAttrCreatedByPersonNameDPPersonId | PERSON_ID | — | — |
| 131 | RefAttrCreatedByPersonNameDPPersonNameId | PERSON_NAME_ID | — | — |
| 132 | RefAttrCreatedByPersonNameDPPreNameAdjunct | PRE_NAME_ADJUNCT | — | — |
| 133 | RefAttrCreatedByPersonNameDPPreviousLastName | PREVIOUS_LAST_NAME | — | — |
| 134 | RefAttrCreatedByPersonNameDPSuffix | SUFFIX | — | — |
| 135 | RefAttrCreatedByPersonNameDPTitle | TITLE | — | — |
| 136 | RefLUpdatedByPersonNameDPEOBusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 137 | RefLUpdatedByPersonNameDPEOCreatedBy1 | CREATED_BY | — | — |
| 138 | RefLUpdatedByPersonNameDPEOCreationDate1 | CREATION_DATE | — | — |
| 139 | RefLUpdatedByPersonNameDPEODisplayName1 | DISPLAY_NAME | — | — |
| 140 | RefLUpdatedByPersonNameDPEOEffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 141 | RefLUpdatedByPersonNameDPEOEffectiveStartDate1 | EFFECTIVE_START_DATE | — | — |
| 142 | RefLUpdatedByPersonNameDPEOFirstName1 | FIRST_NAME | — | — |
| 143 | RefLUpdatedByPersonNameDPEOFullName1 | FULL_NAME | — | — |
| 144 | RefLUpdatedByPersonNameDPEOHonors1 | HONORS | — | — |
| 145 | RefLUpdatedByPersonNameDPEOKnownAs1 | KNOWN_AS | — | — |
| 146 | RefLUpdatedByPersonNameDPEOLastName1 | LAST_NAME | — | — |
| 147 | RefLUpdatedByPersonNameDPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | — |
| 148 | RefLUpdatedByPersonNameDPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 149 | RefLUpdatedByPersonNameDPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 150 | RefLUpdatedByPersonNameDPEOLegislationCode1 | LEGISLATION_CODE | — | — |
| 151 | RefLUpdatedByPersonNameDPEOListName1 | LIST_NAME | — | — |
| 152 | RefLUpdatedByPersonNameDPEOMiddleNames1 | MIDDLE_NAMES | — | — |
| 153 | RefLUpdatedByPersonNameDPEOMilitaryRank1 | MILITARY_RANK | — | — |
| 154 | RefLUpdatedByPersonNameDPEONameType1 | NAME_TYPE | — | — |
| 155 | RefLUpdatedByPersonNameDPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 156 | RefLUpdatedByPersonNameDPEOOrderName1 | ORDER_NAME | — | — |
| 157 | RefLUpdatedByPersonNameDPEOPersonId1 | PERSON_ID | — | — |
| 158 | RefLUpdatedByPersonNameDPEOPersonNameId1 | PERSON_NAME_ID | — | — |
| 159 | RefLUpdatedByPersonNameDPEOPreNameAdjunct1 | PRE_NAME_ADJUNCT | — | — |
| 160 | RefLUpdatedByPersonNameDPEOPreviousLastName1 | PREVIOUS_LAST_NAME | — | — |
| 161 | RefLUpdatedByPersonNameDPEOSuffix1 | SUFFIX | — | — |
| 162 | RefLUpdatedByPersonNameDPEOTitle1 | TITLE | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedByUserPEOActiveFlag | ACTIVE_FLAG | — | — |
| 2 | CreatedByUserPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | CreatedByUserPEOCreatedBy5 | CREATED_BY | — | — |
| 4 | CreatedByUserPEOCreationDate5 | CREATION_DATE | — | — |
| 5 | CreatedByUserPEOCredentialsEmailSent | CREDENTIALS_EMAIL_SENT | — | — |
| 6 | CreatedByUserPEOEndDate | END_DATE | — | — |
| 7 | CreatedByUserPEOExternalId | EXTERNAL_ID | — | — |
| 8 | CreatedByUserPEOHrTerminated | HR_TERMINATED | — | — |
| 9 | CreatedByUserPEOLastUpdateDate5 | LAST_UPDATE_DATE | — | — |
| 10 | CreatedByUserPEOLastUpdateLogin5 | LAST_UPDATE_LOGIN | — | — |
| 11 | CreatedByUserPEOLastUpdatedBy5 | LAST_UPDATED_BY | — | — |
| 12 | CreatedByUserPEOMultitenancyUsername | MULTITENANCY_USERNAME | — | — |
| 13 | CreatedByUserPEOObjectVersionNumber4 | OBJECT_VERSION_NUMBER | — | — |
| 14 | CreatedByUserPEOPartyId | PARTY_ID | — | — |
| 15 | CreatedByUserPEOPersonId | PERSON_ID | — | — |
| 16 | CreatedByUserPEOStartDate | START_DATE | — | — |
| 17 | CreatedByUserPEOSuspended | SUSPENDED | — | — |
| 18 | CreatedByUserPEOUserDataChecksum | USER_DATA_CHECKSUM | — | — |
| 19 | CreatedByUserPEOUserDistinguishedName | USER_DISTINGUISHED_NAME | — | — |
| 20 | CreatedByUserPEOUserGuid | USER_GUID | — | — |
| 21 | CreatedByUserPEOUserId | USER_ID | — | — |
| 22 | CreatedByUserPEOUsername | USERNAME | — | — |
| 23 | LastUpdatedByUserPEO1_1ActiveFlag1 | ACTIVE_FLAG | — | — |
| 24 | LastUpdatedByUserPEO1_1BusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 25 | LastUpdatedByUserPEO1_1CreatedBy6 | CREATED_BY | — | — |
| 26 | LastUpdatedByUserPEO1_1CreationDate6 | CREATION_DATE | — | — |
| 27 | LastUpdatedByUserPEO1_1CredentialsEmailSent1 | CREDENTIALS_EMAIL_SENT | — | — |
| 28 | LastUpdatedByUserPEO1_1EndDate1 | END_DATE | — | — |
| 29 | LastUpdatedByUserPEO1_1ExternalId1 | EXTERNAL_ID | — | — |
| 30 | LastUpdatedByUserPEO1_1HrTerminated1 | HR_TERMINATED | — | — |
| 31 | LastUpdatedByUserPEO1_1LastUpdateDate6 | LAST_UPDATE_DATE | — | — |
| 32 | LastUpdatedByUserPEO1_1LastUpdateLogin6 | LAST_UPDATE_LOGIN | — | — |
| 33 | LastUpdatedByUserPEO1_1LastUpdatedBy6 | LAST_UPDATED_BY | — | — |
| 34 | LastUpdatedByUserPEO1_1MultitenancyUsername1 | MULTITENANCY_USERNAME | — | — |
| 35 | LastUpdatedByUserPEO1_1ObjectVersionNumber5 | OBJECT_VERSION_NUMBER | — | — |
| 36 | LastUpdatedByUserPEO1_1PartyId1 | PARTY_ID | — | — |
| 37 | LastUpdatedByUserPEO1_1PersonId1 | PERSON_ID | — | — |
| 38 | LastUpdatedByUserPEO1_1StartDate1 | START_DATE | — | — |
| 39 | LastUpdatedByUserPEO1_1Suspended1 | SUSPENDED | — | — |
| 40 | LastUpdatedByUserPEO1_1UserDataChecksum1 | USER_DATA_CHECKSUM | — | — |
| 41 | LastUpdatedByUserPEO1_1UserDistinguishedName1 | USER_DISTINGUISHED_NAME | — | — |
| 42 | LastUpdatedByUserPEO1_1UserGuid1 | USER_GUID | — | — |
| 43 | LastUpdatedByUserPEO1_1UserId1 | USER_ID | — | — |
| 44 | LastUpdatedByUserPEO1_1Username1 | USERNAME | — | — |
| 45 | RefAttrCreatedByUserPEOActiveFlag | ACTIVE_FLAG | — | — |
| 46 | RefAttrCreatedByUserPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 47 | RefAttrCreatedByUserPEOCreatedBy1 | CREATED_BY | — | — |
| 48 | RefAttrCreatedByUserPEOCreationDate1 | CREATION_DATE | — | — |
| 49 | RefAttrCreatedByUserPEOCredentialsEmailSent | CREDENTIALS_EMAIL_SENT | — | — |
| 50 | RefAttrCreatedByUserPEOEndDate | END_DATE | — | — |
| 51 | RefAttrCreatedByUserPEOExternalId | EXTERNAL_ID | — | — |
| 52 | RefAttrCreatedByUserPEOHrTerminated | HR_TERMINATED | — | — |
| 53 | RefAttrCreatedByUserPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | — |
| 54 | RefAttrCreatedByUserPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 55 | RefAttrCreatedByUserPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 56 | RefAttrCreatedByUserPEOMultitenancyUsername | MULTITENANCY_USERNAME | — | — |
| 57 | RefAttrCreatedByUserPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 58 | RefAttrCreatedByUserPEOPartyId | PARTY_ID | — | — |
| 59 | RefAttrCreatedByUserPEOPersonId | PERSON_ID | — | — |
| 60 | RefAttrCreatedByUserPEOStartDate | START_DATE | — | — |
| 61 | RefAttrCreatedByUserPEOSuspended | SUSPENDED | — | — |
| 62 | RefAttrCreatedByUserPEOUserDataChecksum | USER_DATA_CHECKSUM | — | — |
| 63 | RefAttrCreatedByUserPEOUserDistinguishedName | USER_DISTINGUISHED_NAME | — | — |
| 64 | RefAttrCreatedByUserPEOUserGuid | USER_GUID | — | — |
| 65 | RefAttrCreatedByUserPEOUserId | USER_ID | — | — |
| 66 | RefAttrCreatedByUserPEOUsername | USERNAME | — | — |
| 67 | RefAttrLastUpdateByUserPEOActiveFlag1 | ACTIVE_FLAG | — | — |
| 68 | RefAttrLastUpdateByUserPEOBusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 69 | RefAttrLastUpdateByUserPEOCreatedBy2 | CREATED_BY | — | — |
| 70 | RefAttrLastUpdateByUserPEOCreationDate2 | CREATION_DATE | — | — |
| 71 | RefAttrLastUpdateByUserPEOCredentialsEmailSent1 | CREDENTIALS_EMAIL_SENT | — | — |
| 72 | RefAttrLastUpdateByUserPEOEndDate1 | END_DATE | — | — |
| 73 | RefAttrLastUpdateByUserPEOExternalId1 | EXTERNAL_ID | — | — |
| 74 | RefAttrLastUpdateByUserPEOHrTerminated1 | HR_TERMINATED | — | — |
| 75 | RefAttrLastUpdateByUserPEOLastUpdateDate2 | LAST_UPDATE_DATE | — | — |
| 76 | RefAttrLastUpdateByUserPEOLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 77 | RefAttrLastUpdateByUserPEOLastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 78 | RefAttrLastUpdateByUserPEOMultitenancyUsername1 | MULTITENANCY_USERNAME | — | — |
| 79 | RefAttrLastUpdateByUserPEOObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 80 | RefAttrLastUpdateByUserPEOPartyId1 | PARTY_ID | — | — |
| 81 | RefAttrLastUpdateByUserPEOPersonId1 | PERSON_ID | — | — |
| 82 | RefAttrLastUpdateByUserPEOStartDate1 | START_DATE | — | — |
| 83 | RefAttrLastUpdateByUserPEOSuspended1 | SUSPENDED | — | — |
| 84 | RefAttrLastUpdateByUserPEOUserDataChecksum1 | USER_DATA_CHECKSUM | — | — |
| 85 | RefAttrLastUpdateByUserPEOUserDistinguishedName1 | USER_DISTINGUISHED_NAME | — | — |
| 86 | RefAttrLastUpdateByUserPEOUserGuid1 | USER_GUID | — | — |
| 87 | RefAttrLastUpdateByUserPEOUserId1 | USER_ID | — | — |
| 88 | RefAttrLastUpdateByUserPEOUsername1 | USERNAME | — | — |
| 89 | RefDocCreatedByUserPEOActiveFlag | ACTIVE_FLAG | — | — |
| 90 | RefDocCreatedByUserPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 91 | RefDocCreatedByUserPEOCreatedBy | CREATED_BY | — | — |
| 92 | RefDocCreatedByUserPEOCreationDate | CREATION_DATE | — | — |
| 93 | RefDocCreatedByUserPEOCredentialsEmailSent | CREDENTIALS_EMAIL_SENT | — | — |
| 94 | RefDocCreatedByUserPEOEndDate | END_DATE | — | — |
| 95 | RefDocCreatedByUserPEOExternalId | EXTERNAL_ID | — | — |
| 96 | RefDocCreatedByUserPEOHrTerminated | HR_TERMINATED | — | — |
| 97 | RefDocCreatedByUserPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 98 | RefDocCreatedByUserPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 99 | RefDocCreatedByUserPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 100 | RefDocCreatedByUserPEOMultitenancyUsername | MULTITENANCY_USERNAME | — | — |
| 101 | RefDocCreatedByUserPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 102 | RefDocCreatedByUserPEOPartyId | PARTY_ID | — | — |
| 103 | RefDocCreatedByUserPEOPersonId | PERSON_ID | — | — |
| 104 | RefDocCreatedByUserPEOStartDate | START_DATE | — | — |
| 105 | RefDocCreatedByUserPEOSuspended | SUSPENDED | — | — |
| 106 | RefDocCreatedByUserPEOUserDataChecksum | USER_DATA_CHECKSUM | — | — |
| 107 | RefDocCreatedByUserPEOUserDistinguishedName | USER_DISTINGUISHED_NAME | — | — |
| 108 | RefDocCreatedByUserPEOUserGuid | USER_GUID | — | — |
| 109 | RefDocCreatedByUserPEOUserId | USER_ID | — | — |
| 110 | RefDocCreatedByUserPEOUsername | USERNAME | — | — |
| 111 | RefDocLastUpdtdByUserPEOActiveFlag1 | ACTIVE_FLAG | — | — |
| 112 | RefDocLastUpdtdByUserPEOBusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 113 | RefDocLastUpdtdByUserPEOCreatedBy1 | CREATED_BY | — | — |
| 114 | RefDocLastUpdtdByUserPEOCreationDate1 | CREATION_DATE | — | — |
| 115 | RefDocLastUpdtdByUserPEOCredentialsEmailSent1 | CREDENTIALS_EMAIL_SENT | — | — |
| 116 | RefDocLastUpdtdByUserPEOEndDate1 | END_DATE | — | — |
| 117 | RefDocLastUpdtdByUserPEOExternalId1 | EXTERNAL_ID | — | — |
| 118 | RefDocLastUpdtdByUserPEOHrTerminated1 | HR_TERMINATED | — | — |
| 119 | RefDocLastUpdtdByUserPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | — |
| 120 | RefDocLastUpdtdByUserPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 121 | RefDocLastUpdtdByUserPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 122 | RefDocLastUpdtdByUserPEOMultitenancyUsername1 | MULTITENANCY_USERNAME | — | — |
| 123 | RefDocLastUpdtdByUserPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 124 | RefDocLastUpdtdByUserPEOPartyId1 | PARTY_ID | — | — |
| 125 | RefDocLastUpdtdByUserPEOPersonId1 | PERSON_ID | — | — |
| 126 | RefDocLastUpdtdByUserPEOStartDate1 | START_DATE | — | — |
| 127 | RefDocLastUpdtdByUserPEOSuspended1 | SUSPENDED | — | — |
| 128 | RefDocLastUpdtdByUserPEOUserDataChecksum1 | USER_DATA_CHECKSUM | — | — |
| 129 | RefDocLastUpdtdByUserPEOUserDistinguishedName1 | USER_DISTINGUISHED_NAME | — | — |
| 130 | RefDocLastUpdtdByUserPEOUserGuid1 | USER_GUID | — | — |
| 131 | RefDocLastUpdtdByUserPEOUserId1 | USER_ID | — | — |
| 132 | RefDocLastUpdtdByUserPEOUsername1 | USERNAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
