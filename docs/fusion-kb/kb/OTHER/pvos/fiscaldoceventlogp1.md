---
id: DOC-OTHER-PVO-FiscalDocEventLogP1
doc_type: system-doc
title: "FiscalDocEventLogP1 — PVO Cross-Module"
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
  - FiscalDocEventLogP1
  - fiscaldoceventlogp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FiscalDocEventLogP1

## 📌 Visão Geral

View Object para extração BICC de dados de Fiscal Doc Event Log P1. Acessa as tabelas: CMF_FD_LOC_INFO_PERSIST_OTBI_V, CMF_FISCAL_DOC_EVENT_LOG, CMF_FISCAL_DOC_HEADERS (+5).

**Caminho:** `FscmTopModelAM.FiscalDocumentAM.FiscalDocEventLogP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 448 | 8 | 2 | 9 | 2% |

---

## 🔗 Tabelas Relacionadas

- [[cmf_fd_loc_info_persist_otbi_v|CMF_FD_LOC_INFO_PERSIST_OTBI_V]] — 79 atributos
- [[cmf_fiscal_doc_event_log|CMF_FISCAL_DOC_EVENT_LOG]] — 20 atributos (1 PKs, 8 BICC)
- [[cmf_fiscal_doc_headers|CMF_FISCAL_DOC_HEADERS]] — 59 atributos
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 21 atributos
- [[jg_fscl_hdrs_atrb_ext_all|JG_FSCL_HDRS_ATRB_EXT_ALL]] — 55 atributos
- [[jg_fscl_hdr_dtls_atrb_ext_all|JG_FSCL_HDR_DTLS_ATRB_EXT_ALL]] — 18 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 108 atributos (1 PKs, 1 BICC)
- [[per_users|PER_USERS]] — 88 atributos

---

## ⚙️ Atributos

### [[cmf_fd_loc_info_persist_otbi_v|CMF_FD_LOC_INFO_PERSIST_OTBI_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalDocLocInfoPersistPEODocumentHeaderId1 | DOCUMENT_HEADER_ID | — | — |
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

### [[cmf_fiscal_doc_event_log|CMF_FISCAL_DOC_EVENT_LOG]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventLogIdentifier | EVENT_LOG_IDENTIFIER | 🔑 | ✅ |
| 2 | FiscalDocEventLogPEOAccessKey | ACCESS_KEY | — | — |
| 3 | FiscalDocEventLogPEOCountry | COUNTRY | — | — |
| 4 | FiscalDocEventLogPEOCreatedBy | CREATED_BY | — | — |
| 5 | FiscalDocEventLogPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | FiscalDocEventLogPEOEventAction | EVENT_ACTION | — | ✅ |
| 7 | FiscalDocEventLogPEOEventCode | EVENT_CODE | — | ✅ |
| 8 | FiscalDocEventLogPEOEventDate | EVENT_DATE | — | ✅ |
| 9 | FiscalDocEventLogPEOEventName | EVENT_NAME | — | ✅ |
| 10 | FiscalDocEventLogPEOEventStatus | EVENT_STATUS | — | ✅ |
| 11 | FiscalDocEventLogPEOFdHeaderIdentifier | FD_HEADER_IDENTIFIER | — | — |
| 12 | FiscalDocEventLogPEOFdLineIdentifier | FD_LINE_IDENTIFIER | — | — |
| 13 | FiscalDocEventLogPEOFdScheduleIdentifier | FD_SCHEDULE_IDENTIFIER | — | — |
| 14 | FiscalDocEventLogPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | FiscalDocEventLogPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | FiscalDocEventLogPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 17 | FiscalDocEventLogPEOParentEventLogIdentifier | PARENT_EVENT_LOG_IDENTIFIER | — | — |
| 18 | FiscalDocEventLogPEOProcessingDate | PROCESSING_DATE | — | — |
| 19 | FiscalDocEventLogPEOState | STATE | — | — |
| 20 | FiscalDocEventLogPEOTaxpayerid | TAXPAYERID | — | — |

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
| 12 | FiscalDocHeadersPEODocumentHeaderId | DOCUMENT_HEADER_ID | — | — |
| 13 | FiscalDocHeadersPEODocumentNumber | DOCUMENT_NUMBER | — | — |
| 14 | FiscalDocHeadersPEODocumentStatus | DOCUMENT_STATUS | — | — |
| 15 | FiscalDocHeadersPEODocumentType | DOCUMENT_TYPE | — | — |
| 16 | FiscalDocHeadersPEOExternalSystemRefId | EXTERNAL_SYSTEM_REF_ID | — | — |
| 17 | FiscalDocHeadersPEOExternalSystemReference | EXTERNAL_SYSTEM_REFERENCE | — | — |
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
| 28 | FiscalDocHeadersPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 29 | FiscalDocHeadersPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 30 | FiscalDocHeadersPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | — |
| 31 | FiscalDocHeadersPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 32 | FiscalDocHeadersPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 33 | FiscalDocHeadersPEOModel | MODEL | — | — |
| 34 | FiscalDocHeadersPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 35 | FiscalDocHeadersPEOOperationType | OPERATION_TYPE | — | — |
| 36 | FiscalDocHeadersPEOParentDocumentHeaderId | PARENT_DOCUMENT_HEADER_ID | — | — |
| 37 | FiscalDocHeadersPEOReason | REASON | — | — |
| 38 | FiscalDocHeadersPEOReceiverLocationId | RECEIVER_LOCATION_ID | — | — |
| 39 | FiscalDocHeadersPEOReceiverPartyId | RECEIVER_PARTY_ID | — | — |
| 40 | FiscalDocHeadersPEOReceiverPartySiteId | RECEIVER_PARTY_SITE_ID | — | — |
| 41 | FiscalDocHeadersPEOReceiverTaxId | RECEIVER_TAX_ID | — | — |
| 42 | FiscalDocHeadersPEOReferencedStatus | REFERENCED_STATUS | — | — |
| 43 | FiscalDocHeadersPEORequestId | REQUEST_ID | — | — |
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
| 19 | FiscalDocHeaderExtnEOJobDefinitionName1 | JOB_DEFINITION_NAME | — | — |
| 20 | FiscalDocHeaderExtnEOJobDefinitionPackage1 | JOB_DEFINITION_PACKAGE | — | — |
| 21 | FiscalDocHeaderExtnEOLastUpdateDate2 | LAST_UPDATE_DATE | — | — |
| 22 | FiscalDocHeaderExtnEOLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 23 | FiscalDocHeaderExtnEOLastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 24 | FiscalDocHeaderExtnEOLegalReportingUnitId | LEGAL_REPORTING_UNIT_ID | — | — |
| 25 | FiscalDocHeaderExtnEOMatIssueRecptDate | MAT_ISSUE_RECPT_DATE | — | — |
| 26 | FiscalDocHeaderExtnEOMatIssueRecptHour | MAT_ISSUE_RECPT_HOUR | — | — |
| 27 | FiscalDocHeaderExtnEONetWeight | NET_WEIGHT | — | — |
| 28 | FiscalDocHeaderExtnEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
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
| 42 | FiscalDocHeaderExtnEORequestId1 | REQUEST_ID | — | — |
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
| 8 | FiscalDocHeaderDetailExtnEOJobDefinitionName2 | JOB_DEFINITION_NAME | — | — |
| 9 | FiscalDocHeaderDetailExtnEOJobDefinitionPackage2 | JOB_DEFINITION_PACKAGE | — | — |
| 10 | FiscalDocHeaderDetailExtnEOLastUpdateDate3 | LAST_UPDATE_DATE | — | — |
| 11 | FiscalDocHeaderDetailExtnEOLastUpdateLogin3 | LAST_UPDATE_LOGIN | — | — |
| 12 | FiscalDocHeaderDetailExtnEOLastUpdatedBy3 | LAST_UPDATED_BY | — | — |
| 13 | FiscalDocHeaderDetailExtnEOObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 14 | FiscalDocHeaderDetailExtnEOOrgId1 | ORG_ID | — | — |
| 15 | FiscalDocHeaderDetailExtnEORecordType | RECORD_TYPE | — | — |
| 16 | FiscalDocHeaderDetailExtnEORequestId2 | REQUEST_ID | — | — |
| 17 | FiscalDocHeaderDetailExtnEOTaxRelatedLegalMessageFlag | TAX_RELATED_LEGAL_MESSAGE_FLAG | — | — |
| 18 | FiscalDocHeaderDetailExtnEOTrxId1 | TRX_ID | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FDEventCreatedByPersonNameDPBusinessGroupId3 | BUSINESS_GROUP_ID | — | — |
| 2 | FDEventCreatedByPersonNameDPCreatedBy8 | CREATED_BY | — | — |
| 3 | FDEventCreatedByPersonNameDPCreationDate8 | CREATION_DATE | — | — |
| 4 | FDEventCreatedByPersonNameDPDisplayName | DISPLAY_NAME | — | — |
| 5 | FDEventCreatedByPersonNameDPEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 6 | FDEventCreatedByPersonNameDPEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 7 | FDEventCreatedByPersonNameDPFirstName | FIRST_NAME | — | — |
| 8 | FDEventCreatedByPersonNameDPFullName | FULL_NAME | — | — |
| 9 | FDEventCreatedByPersonNameDPHonors | HONORS | — | — |
| 10 | FDEventCreatedByPersonNameDPKnownAs | KNOWN_AS | — | — |
| 11 | FDEventCreatedByPersonNameDPLastName | LAST_NAME | — | — |
| 12 | FDEventCreatedByPersonNameDPLastUpdateDate8 | LAST_UPDATE_DATE | — | — |
| 13 | FDEventCreatedByPersonNameDPLastUpdateLogin8 | LAST_UPDATE_LOGIN | — | — |
| 14 | FDEventCreatedByPersonNameDPLastUpdatedBy8 | LAST_UPDATED_BY | — | — |
| 15 | FDEventCreatedByPersonNameDPLegislationCode | LEGISLATION_CODE | — | — |
| 16 | FDEventCreatedByPersonNameDPListName | LIST_NAME | — | — |
| 17 | FDEventCreatedByPersonNameDPMiddleNames | MIDDLE_NAMES | — | — |
| 18 | FDEventCreatedByPersonNameDPMilitaryRank | MILITARY_RANK | — | — |
| 19 | FDEventCreatedByPersonNameDPNameType | NAME_TYPE | — | — |
| 20 | FDEventCreatedByPersonNameDPObjectVersionNumber6 | OBJECT_VERSION_NUMBER | — | — |
| 21 | FDEventCreatedByPersonNameDPOrderName | ORDER_NAME | — | — |
| 22 | FDEventCreatedByPersonNameDPPersonId3 | PERSON_ID | — | — |
| 23 | FDEventCreatedByPersonNameDPPersonNameId | PERSON_NAME_ID | — | — |
| 24 | FDEventCreatedByPersonNameDPPreNameAdjunct | PRE_NAME_ADJUNCT | — | — |
| 25 | FDEventCreatedByPersonNameDPPreviousLastName | PREVIOUS_LAST_NAME | — | — |
| 26 | FDEventCreatedByPersonNameDPSuffix | SUFFIX | — | — |
| 27 | FDEventCreatedByPersonNameDPTitle | TITLE | — | — |
| 28 | FDEventLUpdatedByPersonNameDBusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 29 | FDEventLUpdatedByPersonNameDCreatedBy1 | CREATED_BY | — | — |
| 30 | FDEventLUpdatedByPersonNameDCreationDate1 | CREATION_DATE | — | — |
| 31 | FDEventLUpdatedByPersonNameDDisplayName | DISPLAY_NAME | — | — |
| 32 | FDEventLUpdatedByPersonNameDEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 33 | FDEventLUpdatedByPersonNameDEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 34 | FDEventLUpdatedByPersonNameDFirstName | FIRST_NAME | — | — |
| 35 | FDEventLUpdatedByPersonNameDFullName | FULL_NAME | 🔑 | ✅ |
| 36 | FDEventLUpdatedByPersonNameDHonors | HONORS | — | — |
| 37 | FDEventLUpdatedByPersonNameDKnownAs | KNOWN_AS | — | — |
| 38 | FDEventLUpdatedByPersonNameDLastName | LAST_NAME | — | — |
| 39 | FDEventLUpdatedByPersonNameDLastUpdateDate1 | LAST_UPDATE_DATE | — | — |
| 40 | FDEventLUpdatedByPersonNameDLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 41 | FDEventLUpdatedByPersonNameDLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 42 | FDEventLUpdatedByPersonNameDLegislationCode | LEGISLATION_CODE | — | — |
| 43 | FDEventLUpdatedByPersonNameDListName | LIST_NAME | — | — |
| 44 | FDEventLUpdatedByPersonNameDMiddleNames | MIDDLE_NAMES | — | — |
| 45 | FDEventLUpdatedByPersonNameDMilitaryRank | MILITARY_RANK | — | — |
| 46 | FDEventLUpdatedByPersonNameDNameType | NAME_TYPE | — | — |
| 47 | FDEventLUpdatedByPersonNameDObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 48 | FDEventLUpdatedByPersonNameDOrderName | ORDER_NAME | — | — |
| 49 | FDEventLUpdatedByPersonNameDPersonId1 | PERSON_ID | — | — |
| 50 | FDEventLUpdatedByPersonNameDPersonNameId | PERSON_NAME_ID | — | — |
| 51 | FDEventLUpdatedByPersonNameDPreNameAdjunct | PRE_NAME_ADJUNCT | — | — |
| 52 | FDEventLUpdatedByPersonNameDPreviousLastName | PREVIOUS_LAST_NAME | — | — |
| 53 | FDEventLUpdatedByPersonNameDSuffix | SUFFIX | — | — |
| 54 | FDEventLUpdatedByPersonNameDTitle | TITLE | — | — |
| 55 | FDHdrCreatedByPersonNameDPEOBusinessGroupId4 | BUSINESS_GROUP_ID | — | — |
| 56 | FDHdrCreatedByPersonNameDPEOCreatedBy9 | CREATED_BY | — | — |
| 57 | FDHdrCreatedByPersonNameDPEOCreationDate9 | CREATION_DATE | — | — |
| 58 | FDHdrCreatedByPersonNameDPEODisplayName1 | DISPLAY_NAME | — | — |
| 59 | FDHdrCreatedByPersonNameDPEOEffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 60 | FDHdrCreatedByPersonNameDPEOEffectiveStartDate1 | EFFECTIVE_START_DATE | — | — |
| 61 | FDHdrCreatedByPersonNameDPEOFirstName1 | FIRST_NAME | — | — |
| 62 | FDHdrCreatedByPersonNameDPEOFullName1 | FULL_NAME | — | — |
| 63 | FDHdrCreatedByPersonNameDPEOHonors1 | HONORS | — | — |
| 64 | FDHdrCreatedByPersonNameDPEOKnownAs1 | KNOWN_AS | — | — |
| 65 | FDHdrCreatedByPersonNameDPEOLastName1 | LAST_NAME | — | — |
| 66 | FDHdrCreatedByPersonNameDPEOLastUpdateDate9 | LAST_UPDATE_DATE | — | — |
| 67 | FDHdrCreatedByPersonNameDPEOLastUpdateLogin9 | LAST_UPDATE_LOGIN | — | — |
| 68 | FDHdrCreatedByPersonNameDPEOLastUpdatedBy9 | LAST_UPDATED_BY | — | — |
| 69 | FDHdrCreatedByPersonNameDPEOLegislationCode1 | LEGISLATION_CODE | — | — |
| 70 | FDHdrCreatedByPersonNameDPEOListName1 | LIST_NAME | — | — |
| 71 | FDHdrCreatedByPersonNameDPEOMiddleNames1 | MIDDLE_NAMES | — | — |
| 72 | FDHdrCreatedByPersonNameDPEOMilitaryRank1 | MILITARY_RANK | — | — |
| 73 | FDHdrCreatedByPersonNameDPEONameType1 | NAME_TYPE | — | — |
| 74 | FDHdrCreatedByPersonNameDPEOObjectVersionNumber7 | OBJECT_VERSION_NUMBER | — | — |
| 75 | FDHdrCreatedByPersonNameDPEOOrderName1 | ORDER_NAME | — | — |
| 76 | FDHdrCreatedByPersonNameDPEOPersonId4 | PERSON_ID | — | — |
| 77 | FDHdrCreatedByPersonNameDPEOPersonNameId1 | PERSON_NAME_ID | — | — |
| 78 | FDHdrCreatedByPersonNameDPEOPreNameAdjunct1 | PRE_NAME_ADJUNCT | — | — |
| 79 | FDHdrCreatedByPersonNameDPEOPreviousLastName1 | PREVIOUS_LAST_NAME | — | — |
| 80 | FDHdrCreatedByPersonNameDPEOSuffix1 | SUFFIX | — | — |
| 81 | FDHdrCreatedByPersonNameDPEOTitle1 | TITLE | — | — |
| 82 | FDHdrUpdatedByPersonNameDPEOBusinessGroupId5 | BUSINESS_GROUP_ID | — | — |
| 83 | FDHdrUpdatedByPersonNameDPEOCreatedBy10 | CREATED_BY | — | — |
| 84 | FDHdrUpdatedByPersonNameDPEOCreationDate10 | CREATION_DATE | — | — |
| 85 | FDHdrUpdatedByPersonNameDPEODisplayName2 | DISPLAY_NAME | — | — |
| 86 | FDHdrUpdatedByPersonNameDPEOEffectiveEndDate2 | EFFECTIVE_END_DATE | — | — |
| 87 | FDHdrUpdatedByPersonNameDPEOEffectiveStartDate2 | EFFECTIVE_START_DATE | — | — |
| 88 | FDHdrUpdatedByPersonNameDPEOFirstName2 | FIRST_NAME | — | — |
| 89 | FDHdrUpdatedByPersonNameDPEOFullName2 | FULL_NAME | — | — |
| 90 | FDHdrUpdatedByPersonNameDPEOHonors2 | HONORS | — | — |
| 91 | FDHdrUpdatedByPersonNameDPEOKnownAs2 | KNOWN_AS | — | — |
| 92 | FDHdrUpdatedByPersonNameDPEOLastName2 | LAST_NAME | — | — |
| 93 | FDHdrUpdatedByPersonNameDPEOLastUpdateDate10 | LAST_UPDATE_DATE | — | — |
| 94 | FDHdrUpdatedByPersonNameDPEOLastUpdateLogin10 | LAST_UPDATE_LOGIN | — | — |
| 95 | FDHdrUpdatedByPersonNameDPEOLastUpdatedBy10 | LAST_UPDATED_BY | — | — |
| 96 | FDHdrUpdatedByPersonNameDPEOLegislationCode2 | LEGISLATION_CODE | — | — |
| 97 | FDHdrUpdatedByPersonNameDPEOListName2 | LIST_NAME | — | — |
| 98 | FDHdrUpdatedByPersonNameDPEOMiddleNames2 | MIDDLE_NAMES | — | — |
| 99 | FDHdrUpdatedByPersonNameDPEOMilitaryRank2 | MILITARY_RANK | — | — |
| 100 | FDHdrUpdatedByPersonNameDPEONameType2 | NAME_TYPE | — | — |
| 101 | FDHdrUpdatedByPersonNameDPEOObjectVersionNumber8 | OBJECT_VERSION_NUMBER | — | — |
| 102 | FDHdrUpdatedByPersonNameDPEOOrderName2 | ORDER_NAME | — | — |
| 103 | FDHdrUpdatedByPersonNameDPEOPersonId5 | PERSON_ID | — | — |
| 104 | FDHdrUpdatedByPersonNameDPEOPersonNameId2 | PERSON_NAME_ID | — | — |
| 105 | FDHdrUpdatedByPersonNameDPEOPreNameAdjunct2 | PRE_NAME_ADJUNCT | — | — |
| 106 | FDHdrUpdatedByPersonNameDPEOPreviousLastName2 | PREVIOUS_LAST_NAME | — | — |
| 107 | FDHdrUpdatedByPersonNameDPEOSuffix2 | SUFFIX | — | — |
| 108 | FDHdrUpdatedByPersonNameDPEOTitle2 | TITLE | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FDEventCreatedByUserPEOActiveFlag | ACTIVE_FLAG | — | — |
| 2 | FDEventCreatedByUserPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | FDEventCreatedByUserPEOCreatedBy5 | CREATED_BY | — | — |
| 4 | FDEventCreatedByUserPEOCreationDate5 | CREATION_DATE | — | — |
| 5 | FDEventCreatedByUserPEOCredentialsEmailSent | CREDENTIALS_EMAIL_SENT | — | — |
| 6 | FDEventCreatedByUserPEOEndDate | END_DATE | — | — |
| 7 | FDEventCreatedByUserPEOExternalId | EXTERNAL_ID | — | — |
| 8 | FDEventCreatedByUserPEOHrTerminated | HR_TERMINATED | — | — |
| 9 | FDEventCreatedByUserPEOLastUpdateDate5 | LAST_UPDATE_DATE | — | — |
| 10 | FDEventCreatedByUserPEOLastUpdateLogin5 | LAST_UPDATE_LOGIN | — | — |
| 11 | FDEventCreatedByUserPEOLastUpdatedBy5 | LAST_UPDATED_BY | — | — |
| 12 | FDEventCreatedByUserPEOMultitenancyUsername | MULTITENANCY_USERNAME | — | — |
| 13 | FDEventCreatedByUserPEOObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 14 | FDEventCreatedByUserPEOPartyId | PARTY_ID | — | — |
| 15 | FDEventCreatedByUserPEOPersonId | PERSON_ID | — | — |
| 16 | FDEventCreatedByUserPEOStartDate | START_DATE | — | — |
| 17 | FDEventCreatedByUserPEOSuspended | SUSPENDED | — | — |
| 18 | FDEventCreatedByUserPEOUserDataChecksum | USER_DATA_CHECKSUM | — | — |
| 19 | FDEventCreatedByUserPEOUserDistinguishedName | USER_DISTINGUISHED_NAME | — | — |
| 20 | FDEventCreatedByUserPEOUserGuid | USER_GUID | — | — |
| 21 | FDEventCreatedByUserPEOUserId | USER_ID | — | — |
| 22 | FDEventCreatedByUserPEOUsername | USERNAME | — | — |
| 23 | FDEventLastUpdatedByUserPEOActiveFlag | ACTIVE_FLAG | — | — |
| 24 | FDEventLastUpdatedByUserPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 25 | FDEventLastUpdatedByUserPEOCreatedBy | CREATED_BY | — | — |
| 26 | FDEventLastUpdatedByUserPEOCreationDate | CREATION_DATE | — | — |
| 27 | FDEventLastUpdatedByUserPEOCredentialsEmailSent | CREDENTIALS_EMAIL_SENT | — | — |
| 28 | FDEventLastUpdatedByUserPEOEndDate | END_DATE | — | — |
| 29 | FDEventLastUpdatedByUserPEOExternalId | EXTERNAL_ID | — | — |
| 30 | FDEventLastUpdatedByUserPEOHrTerminated | HR_TERMINATED | — | — |
| 31 | FDEventLastUpdatedByUserPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 32 | FDEventLastUpdatedByUserPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 33 | FDEventLastUpdatedByUserPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 34 | FDEventLastUpdatedByUserPEOMultitenancyUsername | MULTITENANCY_USERNAME | — | — |
| 35 | FDEventLastUpdatedByUserPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 36 | FDEventLastUpdatedByUserPEOPartyId | PARTY_ID | — | — |
| 37 | FDEventLastUpdatedByUserPEOPersonId | PERSON_ID | — | — |
| 38 | FDEventLastUpdatedByUserPEOStartDate | START_DATE | — | — |
| 39 | FDEventLastUpdatedByUserPEOSuspended | SUSPENDED | — | — |
| 40 | FDEventLastUpdatedByUserPEOUserDataChecksum | USER_DATA_CHECKSUM | — | — |
| 41 | FDEventLastUpdatedByUserPEOUserDistinguishedName | USER_DISTINGUISHED_NAME | — | — |
| 42 | FDEventLastUpdatedByUserPEOUserGuid | USER_GUID | — | — |
| 43 | FDEventLastUpdatedByUserPEOUserId | USER_ID | — | — |
| 44 | FDEventLastUpdatedByUserPEOUsername | USERNAME | — | — |
| 45 | FDHdrCreatedByUserPEO1_1ActiveFlag1 | ACTIVE_FLAG | — | — |
| 46 | FDHdrCreatedByUserPEO1_1BusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 47 | FDHdrCreatedByUserPEO1_1CreatedBy6 | CREATED_BY | — | — |
| 48 | FDHdrCreatedByUserPEO1_1CreationDate6 | CREATION_DATE | — | — |
| 49 | FDHdrCreatedByUserPEO1_1CredentialsEmailSent1 | CREDENTIALS_EMAIL_SENT | — | — |
| 50 | FDHdrCreatedByUserPEO1_1EndDate1 | END_DATE | — | — |
| 51 | FDHdrCreatedByUserPEO1_1ExternalId1 | EXTERNAL_ID | — | — |
| 52 | FDHdrCreatedByUserPEO1_1HrTerminated1 | HR_TERMINATED | — | — |
| 53 | FDHdrCreatedByUserPEO1_1LastUpdateDate6 | LAST_UPDATE_DATE | — | — |
| 54 | FDHdrCreatedByUserPEO1_1LastUpdateLogin6 | LAST_UPDATE_LOGIN | — | — |
| 55 | FDHdrCreatedByUserPEO1_1LastUpdatedBy6 | LAST_UPDATED_BY | — | — |
| 56 | FDHdrCreatedByUserPEO1_1MultitenancyUsername1 | MULTITENANCY_USERNAME | — | — |
| 57 | FDHdrCreatedByUserPEO1_1ObjectVersionNumber4 | OBJECT_VERSION_NUMBER | — | — |
| 58 | FDHdrCreatedByUserPEO1_1PartyId1 | PARTY_ID | — | — |
| 59 | FDHdrCreatedByUserPEO1_1PersonId1 | PERSON_ID | — | — |
| 60 | FDHdrCreatedByUserPEO1_1StartDate1 | START_DATE | — | — |
| 61 | FDHdrCreatedByUserPEO1_1Suspended1 | SUSPENDED | — | — |
| 62 | FDHdrCreatedByUserPEO1_1UserDataChecksum1 | USER_DATA_CHECKSUM | — | — |
| 63 | FDHdrCreatedByUserPEO1_1UserDistinguishedName1 | USER_DISTINGUISHED_NAME | — | — |
| 64 | FDHdrCreatedByUserPEO1_1UserGuid1 | USER_GUID | — | — |
| 65 | FDHdrCreatedByUserPEO1_1UserId1 | USER_ID | — | — |
| 66 | FDHdrCreatedByUserPEO1_1Username1 | USERNAME | — | — |
| 67 | FDHdrUpdatedByUserPEOActiveFlag2 | ACTIVE_FLAG | — | — |
| 68 | FDHdrUpdatedByUserPEOBusinessGroupId2 | BUSINESS_GROUP_ID | — | — |
| 69 | FDHdrUpdatedByUserPEOCreatedBy7 | CREATED_BY | — | — |
| 70 | FDHdrUpdatedByUserPEOCreationDate7 | CREATION_DATE | — | — |
| 71 | FDHdrUpdatedByUserPEOCredentialsEmailSent2 | CREDENTIALS_EMAIL_SENT | — | — |
| 72 | FDHdrUpdatedByUserPEOEndDate2 | END_DATE | — | — |
| 73 | FDHdrUpdatedByUserPEOExternalId2 | EXTERNAL_ID | — | — |
| 74 | FDHdrUpdatedByUserPEOHrTerminated2 | HR_TERMINATED | — | — |
| 75 | FDHdrUpdatedByUserPEOLastUpdateDate7 | LAST_UPDATE_DATE | — | — |
| 76 | FDHdrUpdatedByUserPEOLastUpdateLogin7 | LAST_UPDATE_LOGIN | — | — |
| 77 | FDHdrUpdatedByUserPEOLastUpdatedBy7 | LAST_UPDATED_BY | — | — |
| 78 | FDHdrUpdatedByUserPEOMultitenancyUsername2 | MULTITENANCY_USERNAME | — | — |
| 79 | FDHdrUpdatedByUserPEOObjectVersionNumber5 | OBJECT_VERSION_NUMBER | — | — |
| 80 | FDHdrUpdatedByUserPEOPartyId2 | PARTY_ID | — | — |
| 81 | FDHdrUpdatedByUserPEOPersonId2 | PERSON_ID | — | — |
| 82 | FDHdrUpdatedByUserPEOStartDate2 | START_DATE | — | — |
| 83 | FDHdrUpdatedByUserPEOSuspended2 | SUSPENDED | — | — |
| 84 | FDHdrUpdatedByUserPEOUserDataChecksum2 | USER_DATA_CHECKSUM | — | — |
| 85 | FDHdrUpdatedByUserPEOUserDistinguishedName2 | USER_DISTINGUISHED_NAME | — | — |
| 86 | FDHdrUpdatedByUserPEOUserGuid2 | USER_GUID | — | — |
| 87 | FDHdrUpdatedByUserPEOUserId2 | USER_ID | — | — |
| 88 | FDHdrUpdatedByUserPEOUsername2 | USERNAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
