---
id: DOC-OTHER-PVO-ReceivingInboundShipmentHeaderExtractPVO
doc_type: system-doc
title: "ReceivingInboundShipmentHeaderExtractPVO — PVO Cross-Module"
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
  - ReceivingInboundShipmentHeaderExtractPVO
  - receivinginboundshipmentheaderextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReceivingInboundShipmentHeaderExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Receiving Inbound Shipment Header Extract. Acessa as tabelas: RCV_SHIPMENT_HEADERS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.RcvBiccExtractAM.ReceivingInboundShipmentHeaderExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 118 | 1 | 1 | 78 | 66% |

---

## 🔗 Tabelas Relacionadas

- [[rcv_shipment_headers|RCV_SHIPMENT_HEADERS]] — 118 atributos (1 PKs, 78 BICC)

---

## ⚙️ Atributos

### [[rcv_shipment_headers|RCV_SHIPMENT_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AsnType | ASN_TYPE | — | ✅ |
| 2 | Attribute1 | ATTRIBUTE1 | — | — |
| 3 | Attribute10 | ATTRIBUTE10 | — | — |
| 4 | Attribute11 | ATTRIBUTE11 | — | — |
| 5 | Attribute12 | ATTRIBUTE12 | — | — |
| 6 | Attribute13 | ATTRIBUTE13 | — | — |
| 7 | Attribute14 | ATTRIBUTE14 | — | — |
| 8 | Attribute15 | ATTRIBUTE15 | — | — |
| 9 | Attribute16 | ATTRIBUTE16 | — | — |
| 10 | Attribute17 | ATTRIBUTE17 | — | — |
| 11 | Attribute18 | ATTRIBUTE18 | — | — |
| 12 | Attribute19 | ATTRIBUTE19 | — | — |
| 13 | Attribute2 | ATTRIBUTE2 | — | — |
| 14 | Attribute20 | ATTRIBUTE20 | — | — |
| 15 | Attribute3 | ATTRIBUTE3 | — | — |
| 16 | Attribute4 | ATTRIBUTE4 | — | — |
| 17 | Attribute5 | ATTRIBUTE5 | — | — |
| 18 | Attribute6 | ATTRIBUTE6 | — | — |
| 19 | Attribute7 | ATTRIBUTE7 | — | — |
| 20 | Attribute8 | ATTRIBUTE8 | — | — |
| 21 | Attribute9 | ATTRIBUTE9 | — | — |
| 22 | AttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 23 | AttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 24 | AttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 25 | AttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 26 | AttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 27 | AttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 28 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 29 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 30 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 31 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 32 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 33 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 34 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 35 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 36 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 37 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 38 | AttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 39 | AttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 40 | AttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 41 | AttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 42 | AttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 43 | BillOfLading | BILL_OF_LADING | — | ✅ |
| 44 | CarrierEquipment | CARRIER_EQUIPMENT | — | ✅ |
| 45 | CarrierMethod | CARRIER_METHOD | — | ✅ |
| 46 | Comments | COMMENTS | — | ✅ |
| 47 | ConversionDate | CONVERSION_DATE | — | ✅ |
| 48 | ConversionRate | CONVERSION_RATE | — | ✅ |
| 49 | ConversionRateType | CONVERSION_RATE_TYPE | — | ✅ |
| 50 | CreatedBy | CREATED_BY | — | ✅ |
| 51 | CreationDate | CREATION_DATE | — | ✅ |
| 52 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 53 | CustomerId | CUSTOMER_ID | — | ✅ |
| 54 | CustomerSiteId | CUSTOMER_SITE_ID | — | ✅ |
| 55 | EdiControlNum | EDI_CONTROL_NUM | — | ✅ |
| 56 | EmployeeId | EMPLOYEE_ID | — | ✅ |
| 57 | ExpectedReceiptDate | EXPECTED_RECEIPT_DATE | — | ✅ |
| 58 | FreightAmount | FREIGHT_AMOUNT | — | ✅ |
| 59 | FreightBillNumber | FREIGHT_BILL_NUMBER | — | ✅ |
| 60 | FreightCarrierId | FREIGHT_CARRIER_ID | — | ✅ |
| 61 | FreightTerms | FREIGHT_TERMS | — | ✅ |
| 62 | GovernmentContext | GOVERNMENT_CONTEXT | — | ✅ |
| 63 | GrossWeight | GROSS_WEIGHT | — | ✅ |
| 64 | GrossWeightUomCode | GROSS_WEIGHT_UOM_CODE | — | ✅ |
| 65 | HazardClass | HAZARD_CLASS | — | ✅ |
| 66 | HazardCode | HAZARD_CODE | — | ✅ |
| 67 | HazardDescription | HAZARD_DESCRIPTION | — | ✅ |
| 68 | HeaderInterfaceId | HEADER_INTERFACE_ID | — | ✅ |
| 69 | InvoiceAmount | INVOICE_AMOUNT | — | ✅ |
| 70 | InvoiceDate | INVOICE_DATE | — | ✅ |
| 71 | InvoiceNum | INVOICE_NUM | — | ✅ |
| 72 | InvoiceStatusCode | INVOICE_STATUS_CODE | — | ✅ |
| 73 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 74 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 75 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 76 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 77 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 78 | LspFlag | LSP_FLAG | — | ✅ |
| 79 | NetWeight | NET_WEIGHT | — | ✅ |
| 80 | NetWeightUomCode | NET_WEIGHT_UOM_CODE | — | ✅ |
| 81 | NoticeCreationDate | NOTICE_CREATION_DATE | — | ✅ |
| 82 | NumOfContainers | NUM_OF_CONTAINERS | — | ✅ |
| 83 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 84 | OrganizationId | ORGANIZATION_ID | — | ✅ |
| 85 | PackagingCode | PACKAGING_CODE | — | ✅ |
| 86 | PackingSlip | PACKING_SLIP | — | ✅ |
| 87 | PaymentTermsId | PAYMENT_TERMS_ID | — | ✅ |
| 88 | RaDocCreationDate | RA_DOC_CREATION_DATE | — | ✅ |
| 89 | RaDocLastUpdateDate | RA_DOC_LAST_UPDATE_DATE | — | ✅ |
| 90 | RaDocRevisionDate | RA_DOC_REVISION_DATE | — | ✅ |
| 91 | RaDocRevisionNumber | RA_DOC_REVISION_NUMBER | — | ✅ |
| 92 | RaDocumentCode | RA_DOCUMENT_CODE | — | ✅ |
| 93 | RaDocumentNumber | RA_DOCUMENT_NUMBER | — | ✅ |
| 94 | RaDooSourceSystemId | RA_DOO_SOURCE_SYSTEM_ID | — | ✅ |
| 95 | RaNoteToReceiver | RA_NOTE_TO_RECEIVER | — | ✅ |
| 96 | RaOrigSystemRef | RA_ORIG_SYSTEM_REF | — | ✅ |
| 97 | RaOutsourcerContactId | RA_OUTSOURCER_CONTACT_ID | — | ✅ |
| 98 | RaOutsourcerPartyId | RA_OUTSOURCER_PARTY_ID | — | ✅ |
| 99 | ReceiptAdviceNumber | RECEIPT_ADVICE_NUMBER | — | ✅ |
| 100 | ReceiptNum | RECEIPT_NUM | — | ✅ |
| 101 | ReceiptSourceCode | RECEIPT_SOURCE_CODE | — | ✅ |
| 102 | RemitToSiteId | REMIT_TO_SITE_ID | — | ✅ |
| 103 | RequestId | REQUEST_ID | — | ✅ |
| 104 | RmaBuId | RMA_BU_ID | — | ✅ |
| 105 | ShipFromLocationId | SHIP_FROM_LOCATION_ID | — | ✅ |
| 106 | ShipToLocationId | SHIP_TO_LOCATION_ID | — | ✅ |
| 107 | ShipToOrgId | SHIP_TO_ORG_ID | — | ✅ |
| 108 | ShipmentHeaderId | SHIPMENT_HEADER_ID | 🔑 | ✅ |
| 109 | ShipmentNum | SHIPMENT_NUM | — | ✅ |
| 110 | ShippedDate | SHIPPED_DATE | — | ✅ |
| 111 | SpecialHandlingCode | SPECIAL_HANDLING_CODE | — | ✅ |
| 112 | TarWeight | TAR_WEIGHT | — | ✅ |
| 113 | TarWeightUomCode | TAR_WEIGHT_UOM_CODE | — | ✅ |
| 114 | TaxAmount | TAX_AMOUNT | — | ✅ |
| 115 | TaxName | TAX_NAME | — | ✅ |
| 116 | VendorId | VENDOR_ID | — | ✅ |
| 117 | VendorSiteId | VENDOR_SITE_ID | — | ✅ |
| 118 | WaybillAirbillNum | WAYBILL_AIRBILL_NUM | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
