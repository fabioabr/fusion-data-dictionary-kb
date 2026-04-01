---
id: DOC-PO-146
doc_type: system-doc
title: "RCV_SHIPMENT_HEADERS — Cabecalhos de Recebimento"
system: Oracle Fusion Cloud ERP
module: Procurement
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - procurement
  - data-dictionary
  - purchase-orders
  - po-transactions
  - compras
aliases:
  - RCV_SHIPMENT_HEADERS
  - rcv_shipment_headers
  - rcv-shipment-headers
  - rcv-shipment
  - cabecalhos-de-recebimento
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# RCV_SHIPMENT_HEADERS

## 📌 Visão Geral

Armazena os **cabecalhos de recebimento (shipment headers)**. Cada registro representa um recebimento fisico de mercadorias contra POs.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Recebimento:** Entrada de materiais no estoque.
- **Rastreamento logistico:** Shipments, ASNs e transportadoras.
- **3-way matching:** Base para matching PO x Recebimento x Fatura.
- **Relatorios de receiving:** Volumes e lead times.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | SHIPMENT_HEADER_ID | NUMBER(18) | NOT NULL | PK | ID do recebimento | — | 🟢 100% |
| 2 | RECEIPT_NUM | VARCHAR2(30) | NULL | Identificacao | Numero do recebimento | — | 🟢 100% |
| 3 | VENDOR_ID | NUMBER(18) | NULL | FK | Fornecedor | [[poz_suppliers]] | 🟢 100% |
| 4 | VENDOR_SITE_ID | NUMBER(18) | NULL | FK | Site | [[poz_supplier_sites_all_m]] | 🟢 95% |
| 5 | SHIP_TO_ORG_ID | NUMBER(18) | NULL | FK | Org de destino | [[hr_all_organization_units_f]] | 🟢 95% |
| 6 | RECEIPT_SOURCE_CODE | VARCHAR2(25) | NULL | Classificacao | VENDOR, INTERNAL, CUSTOMER | — | 🟢 95% |
| 7 | SHIPMENT_NUM | VARCHAR2(30) | NULL | Identificacao | Numero do shipment (ASN) | — | 🟢 90% |
| 8 | FREIGHT_CARRIER_CODE | VARCHAR2(25) | NULL | Logistica | Transportadora | — | 🟢 85% |
| 9 | BILL_OF_LADING | VARCHAR2(25) | NULL | Logistica | Conhecimento de embarque | — | 🟢 85% |
| 10 | SHIPPED_DATE | DATE | NULL | Data | Data de envio | — | 🟢 90% |
| 11 | EXPECTED_RECEIPT_DATE | DATE | NULL | Data | Data esperada | — | 🟢 90% |
| 12 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 13 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 14 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 15 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_suppliers]] — via `VENDOR_ID` (fornecedor do recebimento)
- [[poz_supplier_sites_all_m]] — via `VENDOR_SITE_ID` (site do fornecedor no recebimento)
- [[hr_all_organization_units_f]] — via `SHIP_TO_ORG_ID` (organizacao destino do recebimento)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Recebimentos de um fornecedor
```sql
SELECT SHIPMENT_HEADER_ID, RECEIPT_NUM, SHIPPED_DATE, CREATION_DATE
FROM   RCV_SHIPMENT_HEADERS
WHERE  VENDOR_ID = :p_vendor_id
ORDER BY CREATION_DATE DESC;
```

---

## 🔒 Observações

- O `RECEIPT_SOURCE_CODE` identifica VENDOR, INTERNAL ou CUSTOMER.
- O `RECEIPT_NUM` e gerado automaticamente.
- ASNs criam o header antes da chegada fisica.
- Cada header pode ter multiplas linhas.

---

## 🔗 PVOs Relacionados

### [[costaccountingtransactionspvo|CostAccountingTransactionsPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| FREIGHT_CARRIER_ID | ReceivingShipmentReceiptHeaderPEOFreightCarrierId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| SHIP_FROM_LOCATION_ID | ReceivingShipmentReceiptHeaderPEOShipFromLocationId | — |
| SHIPMENT_HEADER_ID | ReceivingShipmentReceiptHeaderPEOShipmentHeaderId | — |
| WAYBILL_AIRBILL_NUM | RcvShipmentHeadersWaybillAirbillNum | — |

### [[costaccountingtransactionsrefpvo|CostAccountingTransactionsRefPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| FREIGHT_CARRIER_ID | ReceivingShipmentReceiptHeaderPEOFreightCarrierId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| SHIP_FROM_LOCATION_ID | ReceivingShipmentReceiptHeaderPEOShipFromLocationId | — |
| SHIPMENT_HEADER_ID | ReceivingShipmentReceiptHeaderPEOShipmentHeaderId | — |
| WAYBILL_AIRBILL_NUM | RcvShipmentHeadersWaybillAirbillNum | — |

### [[fiscaldocheadersp|FiscalDocHeadersP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPROVAL_STATUS | RcvShipmentHeadersApprovalStatus | — |
| ASN_STATUS | RcvShipmentHeadersAsnStatus | — |
| ASN_TYPE | RcvShipmentHeadersAsnType | — |
| BILL_OF_LADING | RcvShipmentHeadersBillOfLading | — |
| CARRIER_EQUIPMENT | RcvShipmentHeadersCarrierEquipment | — |
| CARRIER_METHOD | RcvShipmentHeadersCarrierMethod | — |
| COMMENTS | RcvShipmentHeadersComments | — |
| CONVERSION_DATE | RcvShipmentHeadersConversionDate | — |
| CONVERSION_RATE | RcvShipmentHeadersConversionRate | — |
| CONVERSION_RATE_TYPE | RcvShipmentHeadersConversionRateType | — |
| CREATED_BY | RcvShipmentHeadersCreatedBy | — |
| CREATION_DATE | RcvShipmentHeadersCreationDate | — |
| CURRENCY_CODE | RcvShipmentHeadersCurrencyCode | — |
| CUSTOMER_ID | RcvShipmentHeadersCustomerId | — |
| CUSTOMER_SITE_ID | RcvShipmentHeadersCustomerSiteId | — |
| EDI_CONTROL_NUM | RcvShipmentHeadersEdiControlNum | — |
| EMPLOYEE_ID | RcvShipmentHeadersEmployeeId | — |
| EXPECTED_RECEIPT_DATE | RcvShipmentHeadersExpectedReceiptDate | — |
| FREIGHT_AMOUNT | RcvShipmentHeadersFreightAmount | — |
| FREIGHT_BILL_NUMBER | RcvShipmentHeadersFreightBillNumber | — |
| FREIGHT_CARRIER_ID | RcvShipmentHeadersFreightCarrierId | — |
| FREIGHT_TERMS | RcvShipmentHeadersFreightTerms | — |
| GOVERNMENT_CONTEXT | RcvShipmentHeadersGovernmentContext | — |
| GROSS_WEIGHT | RcvShipmentHeadersGrossWeight | — |
| GROSS_WEIGHT_UOM_CODE | RcvShipmentHeadersGrossWeightUomCode | — |
| HAZARD_CLASS | RcvShipmentHeadersHazardClass | — |
| HAZARD_CODE | RcvShipmentHeadersHazardCode | — |
| HAZARD_DESCRIPTION | RcvShipmentHeadersHazardDescription | — |
| HEADER_INTERFACE_ID | RcvShipmentHeadersHeaderInterfaceId | — |
| INVOICE_AMOUNT | RcvShipmentHeadersInvoiceAmount | — |
| INVOICE_DATE | RcvShipmentHeadersInvoiceDate | — |
| INVOICE_NUM | RcvShipmentHeadersInvoiceNum | — |
| INVOICE_STATUS_CODE | RcvShipmentHeadersInvoiceStatusCode | — |
| JOB_DEFINITION_NAME | RcvShipmentHeadersJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | RcvShipmentHeadersJobDefinitionPackage | — |
| LAST_UPDATE_DATE | RcvShipmentHeadersLastUpdateDate | — |
| LAST_UPDATE_LOGIN | RcvShipmentHeadersLastUpdateLogin | — |
| LAST_UPDATED_BY | RcvShipmentHeadersLastUpdatedBy | — |
| LSP_FLAG | RcvShipmentHeadersLspFlag | — |
| NET_WEIGHT | RcvShipmentHeadersNetWeight | — |
| NET_WEIGHT_UOM_CODE | RcvShipmentHeadersNetWeightUomCode | — |
| NOTICE_CREATION_DATE | RcvShipmentHeadersNoticeCreationDate | — |
| NUM_OF_CONTAINERS | RcvShipmentHeadersNumOfContainers | — |
| OBJECT_VERSION_NUMBER | RcvShipmentHeadersObjectVersionNumber | — |
| ORGANIZATION_ID | RcvShipmentHeadersOrganizationId | — |
| PACKAGING_CODE | RcvShipmentHeadersPackagingCode | — |
| PACKING_SLIP | RcvShipmentHeadersPackingSlip | — |
| PAYMENT_TERMS_ID | RcvShipmentHeadersPaymentTermsId | — |
| PERFORMANCE_PERIOD_FROM | RcvShipmentHeadersPerformancePeriodFrom | — |
| PERFORMANCE_PERIOD_TO | RcvShipmentHeadersPerformancePeriodTo | — |
| RA_DOC_CREATION_DATE | RcvShipmentHeadersRaDocCreationDate | — |
| RA_DOC_LAST_UPDATE_DATE | RcvShipmentHeadersRaDocLastUpdateDate | — |
| RA_DOC_REVISION_DATE | RcvShipmentHeadersRaDocRevisionDate | — |
| RA_DOC_REVISION_NUMBER | RcvShipmentHeadersRaDocRevisionNumber | — |
| RA_DOCUMENT_CODE | RcvShipmentHeadersRaDocumentCode | — |
| RA_DOCUMENT_NUMBER | RcvShipmentHeadersRaDocumentNumber | — |
| RA_DOO_SOURCE_SYSTEM_ID | RcvShipmentHeadersRaDooSourceSystemId | — |
| RA_NOTE_TO_RECEIVER | RcvShipmentHeadersRaNoteToReceiver | — |
| RA_ORIG_SYSTEM_REF | RcvShipmentHeadersRaOrigSystemRef | — |
| RA_OUTSOURCER_CONTACT_ID | RcvShipmentHeadersRaOutsourcerContactId | — |
| RA_OUTSOURCER_PARTY_ID | RcvShipmentHeadersRaOutsourcerPartyId | — |
| RECEIPT_ADVICE_NUMBER | RcvShipmentHeadersReceiptAdviceNumber | — |
| RECEIPT_NUM | RcvShipmentHeadersReceiptNum | — |
| RECEIPT_SOURCE_CODE | RcvShipmentHeadersReceiptSourceCode | — |
| REMIT_TO_SITE_ID | RcvShipmentHeadersRemitToSiteId | — |
| REQUEST_DATE | RcvShipmentHeadersRequestDate | — |
| REQUEST_ID | RcvShipmentHeadersRequestId | — |
| RMA_BU_ID | RcvShipmentHeadersRmaBuId | — |
| SHIP_FROM_LOCATION_ID | RcvShipmentHeadersShipFromLocationId | — |
| SHIP_TO_LOCATION_ID | RcvShipmentHeadersShipToLocationId | — |
| SHIP_TO_ORG_ID | RcvShipmentHeadersShipToOrgId | — |
| SHIPMENT_HEADER_ID | RcvShipmentHeadersShipmentHeaderId | — |
| SHIPMENT_HEADER_ID | RcvShipmentHeadersShipmentHeaderId1 | — |
| SHIPMENT_NUM | RcvShipmentHeadersShipmentNum | — |
| SHIPPED_DATE | RcvShipmentHeadersShippedDate | — |
| SPECIAL_HANDLING_CODE | RcvShipmentHeadersSpecialHandlingCode | — |
| TAR_WEIGHT | RcvShipmentHeadersTarWeight | — |
| TAR_WEIGHT_UOM_CODE | RcvShipmentHeadersTarWeightUomCode | — |
| TAX_AMOUNT | RcvShipmentHeadersTaxAmount | — |
| TAX_NAME | RcvShipmentHeadersTaxName | — |
| VENDOR_ID | RcvShipmentHeadersVendorId | — |
| VENDOR_SITE_ID | RcvShipmentHeadersVendorSiteId | — |
| WAYBILL_AIRBILL_NUM | RcvShipmentHeadersWaybillAirbillNum | — |

### [[fiscaldocholdsp|FiscalDocHoldsP]] (OTHER · BICC: 1/84)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPROVAL_STATUS | RcvShipmentHeadersApprovalStatus | — |
| ASN_STATUS | RcvShipmentHeadersAsnStatus | — |
| ASN_TYPE | RcvShipmentHeadersAsnType | — |
| BILL_OF_LADING | RcvShipmentHeadersBillOfLading | — |
| CARRIER_EQUIPMENT | RcvShipmentHeadersCarrierEquipment | — |
| CARRIER_METHOD | RcvShipmentHeadersCarrierMethod | — |
| COMMENTS | RcvShipmentHeadersComments1 | — |
| CONVERSION_DATE | RcvShipmentHeadersConversionDate | — |
| CONVERSION_RATE | RcvShipmentHeadersConversionRate | — |
| CONVERSION_RATE_TYPE | RcvShipmentHeadersConversionRateType | — |
| CREATED_BY | RcvShipmentHeadersCreatedBy4 | — |
| CREATION_DATE | RcvShipmentHeadersCreationDate4 | — |
| CURRENCY_CODE | RcvShipmentHeadersCurrencyCode1 | — |
| CUSTOMER_ID | RcvShipmentHeadersCustomerId | — |
| CUSTOMER_SITE_ID | RcvShipmentHeadersCustomerSiteId | — |
| EDI_CONTROL_NUM | RcvShipmentHeadersEdiControlNum | — |
| EMPLOYEE_ID | RcvShipmentHeadersEmployeeId | — |
| EXPECTED_RECEIPT_DATE | RcvShipmentHeadersExpectedReceiptDate | — |
| FREIGHT_AMOUNT | RcvShipmentHeadersFreightAmount | — |
| FREIGHT_BILL_NUMBER | RcvShipmentHeadersFreightBillNumber | — |
| FREIGHT_CARRIER_ID | RcvShipmentHeadersFreightCarrierId | — |
| FREIGHT_TERMS | RcvShipmentHeadersFreightTerms | — |
| GOVERNMENT_CONTEXT | RcvShipmentHeadersGovernmentContext3 | — |
| GROSS_WEIGHT | RcvShipmentHeadersGrossWeight | — |
| GROSS_WEIGHT_UOM_CODE | RcvShipmentHeadersGrossWeightUomCode | — |
| HAZARD_CLASS | RcvShipmentHeadersHazardClass | — |
| HAZARD_CODE | RcvShipmentHeadersHazardCode | — |
| HAZARD_DESCRIPTION | RcvShipmentHeadersHazardDescription | — |
| HEADER_INTERFACE_ID | RcvShipmentHeadersHeaderInterfaceId | — |
| INVOICE_AMOUNT | RcvShipmentHeadersInvoiceAmount | — |
| INVOICE_DATE | RcvShipmentHeadersInvoiceDate | — |
| INVOICE_NUM | RcvShipmentHeadersInvoiceNum | — |
| INVOICE_STATUS_CODE | RcvShipmentHeadersInvoiceStatusCode | — |
| JOB_DEFINITION_NAME | RcvShipmentHeadersJobDefinitionName4 | — |
| JOB_DEFINITION_PACKAGE | RcvShipmentHeadersJobDefinitionPackage4 | — |
| LAST_UPDATE_DATE | RcvShipmentHeadersLastUpdateDate4 | — |
| LAST_UPDATE_LOGIN | RcvShipmentHeadersLastUpdateLogin4 | — |
| LAST_UPDATED_BY | RcvShipmentHeadersLastUpdatedBy4 | — |
| LSP_FLAG | RcvShipmentHeadersLspFlag | — |
| NET_WEIGHT | RcvShipmentHeadersNetWeight | — |
| NET_WEIGHT_UOM_CODE | RcvShipmentHeadersNetWeightUomCode | — |
| NOTICE_CREATION_DATE | RcvShipmentHeadersNoticeCreationDate | — |
| NUM_OF_CONTAINERS | RcvShipmentHeadersNumOfContainers | — |
| OBJECT_VERSION_NUMBER | RcvShipmentHeadersObjectVersionNumber7 | — |
| OBJECT_VERSION_NUMBER | RcvShipmentHeadersObjectVersionNumber8 | — |
| ORGANIZATION_ID | RcvShipmentHeadersOrganizationId | — |
| PACKAGING_CODE | RcvShipmentHeadersPackagingCode | — |
| PACKING_SLIP | RcvShipmentHeadersPackingSlip | — |
| PAYMENT_TERMS_ID | RcvShipmentHeadersPaymentTermsId | — |
| PERFORMANCE_PERIOD_FROM | RcvShipmentHeadersPerformancePeriodFrom | — |
| PERFORMANCE_PERIOD_TO | RcvShipmentHeadersPerformancePeriodTo | — |
| RA_DOC_CREATION_DATE | RcvShipmentHeadersRaDocCreationDate | — |
| RA_DOC_LAST_UPDATE_DATE | RcvShipmentHeadersRaDocLastUpdateDate | — |
| RA_DOC_REVISION_DATE | RcvShipmentHeadersRaDocRevisionDate | — |
| RA_DOC_REVISION_NUMBER | RcvShipmentHeadersRaDocRevisionNumber | — |
| RA_DOCUMENT_CODE | RcvShipmentHeadersRaDocumentCode | — |
| RA_DOCUMENT_NUMBER | RcvShipmentHeadersRaDocumentNumber | — |
| RA_DOO_SOURCE_SYSTEM_ID | RcvShipmentHeadersRaDooSourceSystemId | — |
| RA_NOTE_TO_RECEIVER | RcvShipmentHeadersRaNoteToReceiver | — |
| RA_ORIG_SYSTEM_REF | RcvShipmentHeadersRaOrigSystemRef | — |
| RA_OUTSOURCER_CONTACT_ID | RcvShipmentHeadersRaOutsourcerContactId | — |
| RA_OUTSOURCER_PARTY_ID | RcvShipmentHeadersRaOutsourcerPartyId | — |
| RECEIPT_ADVICE_NUMBER | RcvShipmentHeadersReceiptAdviceNumber | — |
| RECEIPT_NUM | RcvShipmentHeadersReceiptNum | ✅ |
| RECEIPT_SOURCE_CODE | RcvShipmentHeadersReceiptSourceCode | — |
| REMIT_TO_SITE_ID | RcvShipmentHeadersRemitToSiteId | — |
| REQUEST_DATE | RcvShipmentHeadersRequestDate | — |
| REQUEST_ID | RcvShipmentHeadersRequestId4 | — |
| RMA_BU_ID | RcvShipmentHeadersRmaBuId | — |
| SHIP_FROM_LOCATION_ID | RcvShipmentHeadersShipFromLocationId | — |
| SHIP_TO_LOCATION_ID | RcvShipmentHeadersShipToLocationId2 | — |
| SHIP_TO_ORG_ID | RcvShipmentHeadersShipToOrgId | — |
| SHIPMENT_HEADER_ID | RcvShipmentHeadersShipmentHeaderId | — |
| SHIPMENT_HEADER_ID | RcvShipmentHeadersShipmentHeaderId1 | — |
| SHIPMENT_NUM | RcvShipmentHeadersShipmentNum1 | — |
| SHIPPED_DATE | RcvShipmentHeadersShippedDate | — |
| SPECIAL_HANDLING_CODE | RcvShipmentHeadersSpecialHandlingCode | — |
| TAR_WEIGHT | RcvShipmentHeadersTarWeight | — |
| TAR_WEIGHT_UOM_CODE | RcvShipmentHeadersTarWeightUomCode | — |
| TAX_AMOUNT | RcvShipmentHeadersTaxAmount | — |
| TAX_NAME | RcvShipmentHeadersTaxName2 | — |
| VENDOR_ID | RcvShipmentHeadersVendorId1 | — |
| VENDOR_SITE_ID | RcvShipmentHeadersVendorSiteId1 | — |
| WAYBILL_AIRBILL_NUM | RcvShipmentHeadersWaybillAirbillNum | — |

### [[fiscaldocumentchargeassocp|FiscalDocumentChargeAssocP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPROVAL_STATUS | RcvShipmentHeadersApprovalStatus | — |
| ASN_STATUS | RcvShipmentHeadersAsnStatus | — |
| ASN_TYPE | RcvShipmentHeadersAsnType | — |
| BILL_OF_LADING | RcvShipmentHeadersBillOfLading | — |
| CARRIER_EQUIPMENT | RcvShipmentHeadersCarrierEquipment | — |
| CARRIER_METHOD | RcvShipmentHeadersCarrierMethod | — |
| COMMENTS | RcvShipmentHeadersComments | — |
| CONVERSION_DATE | RcvShipmentHeadersConversionDate | — |
| CONVERSION_RATE | RcvShipmentHeadersConversionRate | — |
| CONVERSION_RATE_TYPE | RcvShipmentHeadersConversionRateType | — |
| CREATED_BY | RcvShipmentHeadersCreatedBy | — |
| CREATION_DATE | RcvShipmentHeadersCreationDate | — |
| CURRENCY_CODE | RcvShipmentHeadersCurrencyCode | — |
| CUSTOMER_ID | RcvShipmentHeadersCustomerId | — |
| CUSTOMER_SITE_ID | RcvShipmentHeadersCustomerSiteId | — |
| EDI_CONTROL_NUM | RcvShipmentHeadersEdiControlNum | — |
| EMPLOYEE_ID | RcvShipmentHeadersEmployeeId | — |
| EXPECTED_RECEIPT_DATE | RcvShipmentHeadersExpectedReceiptDate | — |
| FREIGHT_AMOUNT | RcvShipmentHeadersFreightAmount | — |
| FREIGHT_BILL_NUMBER | RcvShipmentHeadersFreightBillNumber | — |
| FREIGHT_CARRIER_ID | RcvShipmentHeadersFreightCarrierId | — |
| FREIGHT_TERMS | RcvShipmentHeadersFreightTerms | — |
| GOVERNMENT_CONTEXT | RcvShipmentHeadersGovernmentContext | — |
| GROSS_WEIGHT | RcvShipmentHeadersGrossWeight | — |
| GROSS_WEIGHT_UOM_CODE | RcvShipmentHeadersGrossWeightUomCode | — |
| HAZARD_CLASS | RcvShipmentHeadersHazardClass | — |
| HAZARD_CODE | RcvShipmentHeadersHazardCode | — |
| HAZARD_DESCRIPTION | RcvShipmentHeadersHazardDescription | — |
| HEADER_INTERFACE_ID | RcvShipmentHeadersHeaderInterfaceId | — |
| INVOICE_AMOUNT | RcvShipmentHeadersInvoiceAmount | — |
| INVOICE_DATE | RcvShipmentHeadersInvoiceDate | — |
| INVOICE_NUM | RcvShipmentHeadersInvoiceNum | — |
| INVOICE_STATUS_CODE | RcvShipmentHeadersInvoiceStatusCode | — |
| JOB_DEFINITION_NAME | RcvShipmentHeadersJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | RcvShipmentHeadersJobDefinitionPackage | — |
| LAST_UPDATE_DATE | RcvShipmentHeadersLastUpdateDate | — |
| LAST_UPDATE_LOGIN | RcvShipmentHeadersLastUpdateLogin | — |
| LAST_UPDATED_BY | RcvShipmentHeadersLastUpdatedBy | — |
| LSP_FLAG | RcvShipmentHeadersLspFlag | — |
| NET_WEIGHT | RcvShipmentHeadersNetWeight | — |
| NET_WEIGHT_UOM_CODE | RcvShipmentHeadersNetWeightUomCode | — |
| NOTICE_CREATION_DATE | RcvShipmentHeadersNoticeCreationDate | — |
| NUM_OF_CONTAINERS | RcvShipmentHeadersNumOfContainers | — |
| OBJECT_VERSION_NUMBER | RcvShipmentHeadersObjectVersionNumber | — |
| ORGANIZATION_ID | RcvShipmentHeadersOrganizationId | — |
| PACKAGING_CODE | RcvShipmentHeadersPackagingCode | — |
| PACKING_SLIP | RcvShipmentHeadersPackingSlip | — |
| PAYMENT_TERMS_ID | RcvShipmentHeadersPaymentTermsId | — |
| PERFORMANCE_PERIOD_FROM | RcvShipmentHeadersPerformancePeriodFrom | — |
| PERFORMANCE_PERIOD_TO | RcvShipmentHeadersPerformancePeriodTo | — |
| RA_DOC_CREATION_DATE | RcvShipmentHeadersRaDocCreationDate | — |
| RA_DOC_LAST_UPDATE_DATE | RcvShipmentHeadersRaDocLastUpdateDate | — |
| RA_DOC_REVISION_DATE | RcvShipmentHeadersRaDocRevisionDate | — |
| RA_DOC_REVISION_NUMBER | RcvShipmentHeadersRaDocRevisionNumber | — |
| RA_DOCUMENT_CODE | RcvShipmentHeadersRaDocumentCode | — |
| RA_DOCUMENT_NUMBER | RcvShipmentHeadersRaDocumentNumber | — |
| RA_DOO_SOURCE_SYSTEM_ID | RcvShipmentHeadersRaDooSourceSystemId | — |
| RA_NOTE_TO_RECEIVER | RcvShipmentHeadersRaNoteToReceiver | — |
| RA_ORIG_SYSTEM_REF | RcvShipmentHeadersRaOrigSystemRef | — |
| RA_OUTSOURCER_CONTACT_ID | RcvShipmentHeadersRaOutsourcerContactId | — |
| RA_OUTSOURCER_PARTY_ID | RcvShipmentHeadersRaOutsourcerPartyId | — |
| RECEIPT_ADVICE_NUMBER | RcvShipmentHeadersReceiptAdviceNumber | — |
| RECEIPT_NUM | RcvShipmentHeadersReceiptNum | — |
| RECEIPT_SOURCE_CODE | RcvShipmentHeadersReceiptSourceCode | — |
| REMIT_TO_SITE_ID | RcvShipmentHeadersRemitToSiteId | — |
| REQUEST_DATE | RcvShipmentHeadersRequestDate | — |
| REQUEST_ID | RcvShipmentHeadersRequestId | — |
| RMA_BU_ID | RcvShipmentHeadersRmaBuId | — |
| SHIP_FROM_LOCATION_ID | RcvShipmentHeadersShipFromLocationId | — |
| SHIP_TO_LOCATION_ID | RcvShipmentHeadersShipToLocationId | — |
| SHIP_TO_ORG_ID | RcvShipmentHeadersShipToOrgId | — |
| SHIPMENT_HEADER_ID | RcvShipmentHeadersShipmentHeaderId | — |
| SHIPMENT_NUM | RcvShipmentHeadersShipmentNum | — |
| SHIPPED_DATE | RcvShipmentHeadersShippedDate | — |
| SPECIAL_HANDLING_CODE | RcvShipmentHeadersSpecialHandlingCode | — |
| TAR_WEIGHT | RcvShipmentHeadersTarWeight | — |
| TAR_WEIGHT_UOM_CODE | RcvShipmentHeadersTarWeightUomCode | — |
| TAX_AMOUNT | RcvShipmentHeadersTaxAmount | — |
| TAX_NAME | RcvShipmentHeadersTaxName | — |
| VENDOR_ID | RcvShipmentHeadersVendorId | — |
| VENDOR_SITE_ID | RcvShipmentHeadersVendorSiteId | — |
| WAYBILL_AIRBILL_NUM | RcvShipmentHeadersWaybillAirbillNum | — |

### [[fiscaldocumentlinesp|FiscalDocumentLinesP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPROVAL_STATUS | RcvShipmentHeadersApprovalStatus | — |
| ASN_STATUS | RcvShipmentHeadersAsnStatus | — |
| ASN_TYPE | RcvShipmentHeadersAsnType | — |
| BILL_OF_LADING | RcvShipmentHeadersBillOfLading | — |
| CARRIER_EQUIPMENT | RcvShipmentHeadersCarrierEquipment | — |
| CARRIER_METHOD | RcvShipmentHeadersCarrierMethod | — |
| COMMENTS | RcvShipmentHeadersComments | — |
| CONVERSION_DATE | RcvShipmentHeadersConversionDate | — |
| CONVERSION_RATE | RcvShipmentHeadersConversionRate | — |
| CONVERSION_RATE_TYPE | RcvShipmentHeadersConversionRateType | — |
| CREATED_BY | RcvShipmentHeadersCreatedBy | — |
| CREATION_DATE | RcvShipmentHeadersCreationDate | — |
| CURRENCY_CODE | RcvShipmentHeadersCurrencyCode | — |
| CUSTOMER_ID | RcvShipmentHeadersCustomerId | — |
| CUSTOMER_SITE_ID | RcvShipmentHeadersCustomerSiteId | — |
| EDI_CONTROL_NUM | RcvShipmentHeadersEdiControlNum | — |
| EMPLOYEE_ID | RcvShipmentHeadersEmployeeId | — |
| EXPECTED_RECEIPT_DATE | RcvShipmentHeadersExpectedReceiptDate | — |
| FREIGHT_AMOUNT | RcvShipmentHeadersFreightAmount | — |
| FREIGHT_BILL_NUMBER | RcvShipmentHeadersFreightBillNumber | — |
| FREIGHT_CARRIER_ID | RcvShipmentHeadersFreightCarrierId | — |
| FREIGHT_TERMS | RcvShipmentHeadersFreightTerms | — |
| GOVERNMENT_CONTEXT | RcvShipmentHeadersGovernmentContext | — |
| GROSS_WEIGHT | RcvShipmentHeadersGrossWeight | — |
| GROSS_WEIGHT_UOM_CODE | RcvShipmentHeadersGrossWeightUomCode | — |
| HAZARD_CLASS | RcvShipmentHeadersHazardClass | — |
| HAZARD_CODE | RcvShipmentHeadersHazardCode | — |
| HAZARD_DESCRIPTION | RcvShipmentHeadersHazardDescription | — |
| HEADER_INTERFACE_ID | RcvShipmentHeadersHeaderInterfaceId | — |
| INVOICE_AMOUNT | RcvShipmentHeadersInvoiceAmount | — |
| INVOICE_DATE | RcvShipmentHeadersInvoiceDate | — |
| INVOICE_NUM | RcvShipmentHeadersInvoiceNum | — |
| INVOICE_STATUS_CODE | RcvShipmentHeadersInvoiceStatusCode | — |
| JOB_DEFINITION_NAME | RcvShipmentHeadersJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | RcvShipmentHeadersJobDefinitionPackage | — |
| LAST_UPDATE_DATE | RcvShipmentHeadersLastUpdateDate | — |
| LAST_UPDATE_LOGIN | RcvShipmentHeadersLastUpdateLogin | — |
| LAST_UPDATED_BY | RcvShipmentHeadersLastUpdatedBy | — |
| LSP_FLAG | RcvShipmentHeadersLspFlag | — |
| NET_WEIGHT | RcvShipmentHeadersNetWeight | — |
| NET_WEIGHT_UOM_CODE | RcvShipmentHeadersNetWeightUomCode | — |
| NOTICE_CREATION_DATE | RcvShipmentHeadersNoticeCreationDate | — |
| NUM_OF_CONTAINERS | RcvShipmentHeadersNumOfContainers | — |
| OBJECT_VERSION_NUMBER | RcvShipmentHeadersObjectVersionNumber | — |
| ORGANIZATION_ID | RcvShipmentHeadersOrganizationId | — |
| PACKAGING_CODE | RcvShipmentHeadersPackagingCode | — |
| PACKING_SLIP | RcvShipmentHeadersPackingSlip | — |
| PAYMENT_TERMS_ID | RcvShipmentHeadersPaymentTermsId | — |
| PERFORMANCE_PERIOD_FROM | RcvShipmentHeadersPerformancePeriodFrom | — |
| PERFORMANCE_PERIOD_TO | RcvShipmentHeadersPerformancePeriodTo | — |
| RA_DOC_CREATION_DATE | RcvShipmentHeadersRaDocCreationDate | — |
| RA_DOC_LAST_UPDATE_DATE | RcvShipmentHeadersRaDocLastUpdateDate | — |
| RA_DOC_REVISION_DATE | RcvShipmentHeadersRaDocRevisionDate | — |
| RA_DOC_REVISION_NUMBER | RcvShipmentHeadersRaDocRevisionNumber | — |
| RA_DOCUMENT_CODE | RcvShipmentHeadersRaDocumentCode | — |
| RA_DOCUMENT_NUMBER | RcvShipmentHeadersRaDocumentNumber | — |
| RA_DOO_SOURCE_SYSTEM_ID | RcvShipmentHeadersRaDooSourceSystemId | — |
| RA_NOTE_TO_RECEIVER | RcvShipmentHeadersRaNoteToReceiver | — |
| RA_ORIG_SYSTEM_REF | RcvShipmentHeadersRaOrigSystemRef | — |
| RA_OUTSOURCER_CONTACT_ID | RcvShipmentHeadersRaOutsourcerContactId | — |
| RA_OUTSOURCER_PARTY_ID | RcvShipmentHeadersRaOutsourcerPartyId | — |
| RECEIPT_ADVICE_NUMBER | RcvShipmentHeadersReceiptAdviceNumber | — |
| RECEIPT_NUM | RcvShipmentHeadersReceiptNum | — |
| RECEIPT_SOURCE_CODE | RcvShipmentHeadersReceiptSourceCode | — |
| REMIT_TO_SITE_ID | RcvShipmentHeadersRemitToSiteId | — |
| REQUEST_DATE | RcvShipmentHeadersRequestDate | — |
| REQUEST_ID | RcvShipmentHeadersRequestId | — |
| RMA_BU_ID | RcvShipmentHeadersRmaBuId | — |
| SHIP_FROM_LOCATION_ID | RcvShipmentHeadersShipFromLocationId | — |
| SHIP_TO_LOCATION_ID | RcvShipmentHeadersShipToLocationId | — |
| SHIP_TO_ORG_ID | RcvShipmentHeadersShipToOrgId | — |
| SHIPMENT_HEADER_ID | RcvShipmentHeadersShipmentHeaderId | — |
| SHIPMENT_HEADER_ID | RcvShipmentHeadersShipmentHeaderId1 | — |
| SHIPMENT_NUM | RcvShipmentHeadersShipmentNum | — |
| SHIPPED_DATE | RcvShipmentHeadersShippedDate | — |
| SPECIAL_HANDLING_CODE | RcvShipmentHeadersSpecialHandlingCode | — |
| TAR_WEIGHT | RcvShipmentHeadersTarWeight | — |
| TAR_WEIGHT_UOM_CODE | RcvShipmentHeadersTarWeightUomCode | — |
| TAX_AMOUNT | RcvShipmentHeadersTaxAmount | — |
| TAX_NAME | RcvShipmentHeadersTaxName | — |
| VENDOR_ID | RcvShipmentHeadersVendorId | — |
| VENDOR_SITE_ID | RcvShipmentHeadersVendorSiteId | — |
| WAYBILL_AIRBILL_NUM | RcvShipmentHeadersWaybillAirbillNum | — |

### [[fiscaldocumentrcvchargeallocsp|FiscalDocumentRcvChargeAllocsP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPROVAL_STATUS | RcvShipmentHeadersApprovalStatus | — |
| ASN_STATUS | RcvShipmentHeadersAsnStatus | — |
| ASN_TYPE | RcvShipmentHeadersAsnType | — |
| BILL_OF_LADING | RcvShipmentHeadersBillOfLading | — |
| CARRIER_EQUIPMENT | RcvShipmentHeadersCarrierEquipment | — |
| CARRIER_METHOD | RcvShipmentHeadersCarrierMethod | — |
| COMMENTS | RcvShipmentHeadersComments | — |
| CONVERSION_DATE | RcvShipmentHeadersConversionDate | — |
| CONVERSION_RATE | RcvShipmentHeadersConversionRate | — |
| CONVERSION_RATE_TYPE | RcvShipmentHeadersConversionRateType | — |
| CREATED_BY | RcvShipmentHeadersCreatedBy | — |
| CREATION_DATE | RcvShipmentHeadersCreationDate | — |
| CURRENCY_CODE | RcvShipmentHeadersCurrencyCode | — |
| CUSTOMER_ID | RcvShipmentHeadersCustomerId | — |
| CUSTOMER_SITE_ID | RcvShipmentHeadersCustomerSiteId | — |
| EDI_CONTROL_NUM | RcvShipmentHeadersEdiControlNum | — |
| EMPLOYEE_ID | RcvShipmentHeadersEmployeeId | — |
| EXPECTED_RECEIPT_DATE | RcvShipmentHeadersExpectedReceiptDate | — |
| FREIGHT_AMOUNT | RcvShipmentHeadersFreightAmount | — |
| FREIGHT_BILL_NUMBER | RcvShipmentHeadersFreightBillNumber | — |
| FREIGHT_CARRIER_ID | RcvShipmentHeadersFreightCarrierId | — |
| FREIGHT_TERMS | RcvShipmentHeadersFreightTerms | — |
| GOVERNMENT_CONTEXT | RcvShipmentHeadersGovernmentContext | — |
| GROSS_WEIGHT | RcvShipmentHeadersGrossWeight | — |
| GROSS_WEIGHT_UOM_CODE | RcvShipmentHeadersGrossWeightUomCode | — |
| HAZARD_CLASS | RcvShipmentHeadersHazardClass | — |
| HAZARD_CODE | RcvShipmentHeadersHazardCode | — |
| HAZARD_DESCRIPTION | RcvShipmentHeadersHazardDescription | — |
| HEADER_INTERFACE_ID | RcvShipmentHeadersHeaderInterfaceId | — |
| INVOICE_AMOUNT | RcvShipmentHeadersInvoiceAmount | — |
| INVOICE_DATE | RcvShipmentHeadersInvoiceDate | — |
| INVOICE_NUM | RcvShipmentHeadersInvoiceNum | — |
| INVOICE_STATUS_CODE | RcvShipmentHeadersInvoiceStatusCode | — |
| JOB_DEFINITION_NAME | RcvShipmentHeadersJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | RcvShipmentHeadersJobDefinitionPackage | — |
| LAST_UPDATE_DATE | RcvShipmentHeadersLastUpdateDate | — |
| LAST_UPDATE_LOGIN | RcvShipmentHeadersLastUpdateLogin | — |
| LAST_UPDATED_BY | RcvShipmentHeadersLastUpdatedBy | — |
| LSP_FLAG | RcvShipmentHeadersLspFlag | — |
| NET_WEIGHT | RcvShipmentHeadersNetWeight | — |
| NET_WEIGHT_UOM_CODE | RcvShipmentHeadersNetWeightUomCode | — |
| NOTICE_CREATION_DATE | RcvShipmentHeadersNoticeCreationDate | — |
| NUM_OF_CONTAINERS | RcvShipmentHeadersNumOfContainers | — |
| OBJECT_VERSION_NUMBER | RcvShipmentHeadersObjectVersionNumber | — |
| ORGANIZATION_ID | RcvShipmentHeadersOrganizationId | — |
| PACKAGING_CODE | RcvShipmentHeadersPackagingCode | — |
| PACKING_SLIP | RcvShipmentHeadersPackingSlip | — |
| PAYMENT_TERMS_ID | RcvShipmentHeadersPaymentTermsId | — |
| PERFORMANCE_PERIOD_FROM | RcvShipmentHeadersPerformancePeriodFrom | — |
| PERFORMANCE_PERIOD_TO | RcvShipmentHeadersPerformancePeriodTo | — |
| RA_DOC_CREATION_DATE | RcvShipmentHeadersRaDocCreationDate | — |
| RA_DOC_LAST_UPDATE_DATE | RcvShipmentHeadersRaDocLastUpdateDate | — |
| RA_DOC_REVISION_DATE | RcvShipmentHeadersRaDocRevisionDate | — |
| RA_DOC_REVISION_NUMBER | RcvShipmentHeadersRaDocRevisionNumber | — |
| RA_DOCUMENT_CODE | RcvShipmentHeadersRaDocumentCode | — |
| RA_DOCUMENT_NUMBER | RcvShipmentHeadersRaDocumentNumber | — |
| RA_DOO_SOURCE_SYSTEM_ID | RcvShipmentHeadersRaDooSourceSystemId | — |
| RA_NOTE_TO_RECEIVER | RcvShipmentHeadersRaNoteToReceiver | — |
| RA_ORIG_SYSTEM_REF | RcvShipmentHeadersRaOrigSystemRef | — |
| RA_OUTSOURCER_CONTACT_ID | RcvShipmentHeadersRaOutsourcerContactId | — |
| RA_OUTSOURCER_PARTY_ID | RcvShipmentHeadersRaOutsourcerPartyId | — |
| RECEIPT_ADVICE_NUMBER | RcvShipmentHeadersReceiptAdviceNumber | — |
| RECEIPT_NUM | RcvShipmentHeadersReceiptNum | — |
| RECEIPT_SOURCE_CODE | RcvShipmentHeadersReceiptSourceCode | — |
| REMIT_TO_SITE_ID | RcvShipmentHeadersRemitToSiteId | — |
| REQUEST_DATE | RcvShipmentHeadersRequestDate | — |
| REQUEST_ID | RcvShipmentHeadersRequestId | — |
| RMA_BU_ID | RcvShipmentHeadersRmaBuId | — |
| SHIP_FROM_LOCATION_ID | RcvShipmentHeadersShipFromLocationId | — |
| SHIP_TO_LOCATION_ID | RcvShipmentHeadersShipToLocationId | — |
| SHIP_TO_ORG_ID | RcvShipmentHeadersShipToOrgId | — |
| SHIPMENT_HEADER_ID | RcvShipmentHeadersShipmentHeaderId | — |
| SHIPMENT_NUM | RcvShipmentHeadersShipmentNum | — |
| SHIPPED_DATE | RcvShipmentHeadersShippedDate | — |
| SPECIAL_HANDLING_CODE | RcvShipmentHeadersSpecialHandlingCode | — |
| TAR_WEIGHT | RcvShipmentHeadersTarWeight | — |
| TAR_WEIGHT_UOM_CODE | RcvShipmentHeadersTarWeightUomCode | — |
| TAX_AMOUNT | RcvShipmentHeadersTaxAmount | — |
| TAX_NAME | RcvShipmentHeadersTaxName | — |
| VENDOR_ID | RcvShipmentHeadersVendorId | — |
| VENDOR_SITE_ID | RcvShipmentHeadersVendorSiteId | — |
| WAYBILL_AIRBILL_NUM | RcvShipmentHeadersWaybillAirbillNum | — |

### [[fiscaldocumentschedulesp|FiscalDocumentSchedulesP]] (OTHER · BICC: 1/164)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPROVAL_STATUS | RcvShipmentHeaders1ApprovalStatus | — |
| APPROVAL_STATUS | RcvShipmentHeadersApprovalStatus | — |
| ASN_STATUS | RcvShipmentHeaders1AsnStatus | — |
| ASN_STATUS | RcvShipmentHeadersAsnStatus | — |
| ASN_TYPE | RcvShipmentHeaders1AsnType | — |
| ASN_TYPE | RcvShipmentHeadersAsnType | — |
| BILL_OF_LADING | RcvShipmentHeaders1BillOfLading | — |
| BILL_OF_LADING | RcvShipmentHeadersBillOfLading | — |
| CARRIER_EQUIPMENT | RcvShipmentHeaders1CarrierEquipment | — |
| CARRIER_EQUIPMENT | RcvShipmentHeadersCarrierEquipment | — |
| CARRIER_METHOD | RcvShipmentHeaders1CarrierMethod | — |
| CARRIER_METHOD | RcvShipmentHeadersCarrierMethod | — |
| COMMENTS | RcvShipmentHeaders1Comments | — |
| COMMENTS | RcvShipmentHeadersComments1 | — |
| CONVERSION_DATE | RcvShipmentHeaders1ConversionDate | — |
| CONVERSION_DATE | RcvShipmentHeadersConversionDate | — |
| CONVERSION_RATE | RcvShipmentHeaders1ConversionRate | — |
| CONVERSION_RATE | RcvShipmentHeadersConversionRate | — |
| CONVERSION_RATE_TYPE | RcvShipmentHeaders1ConversionRateType | — |
| CONVERSION_RATE_TYPE | RcvShipmentHeadersConversionRateType | — |
| CREATED_BY | RcvShipmentHeaders1CreatedBy | — |
| CREATED_BY | RcvShipmentHeadersCreatedBy4 | — |
| CREATION_DATE | RcvShipmentHeaders1CreationDate | — |
| CREATION_DATE | RcvShipmentHeadersCreationDate4 | — |
| CURRENCY_CODE | RcvShipmentHeaders1CurrencyCode | — |
| CURRENCY_CODE | RcvShipmentHeadersCurrencyCode1 | — |
| CUSTOMER_ID | RcvShipmentHeaders1CustomerId | — |
| CUSTOMER_ID | RcvShipmentHeadersCustomerId | — |
| CUSTOMER_SITE_ID | RcvShipmentHeaders1CustomerSiteId | — |
| CUSTOMER_SITE_ID | RcvShipmentHeadersCustomerSiteId | — |
| EDI_CONTROL_NUM | RcvShipmentHeaders1EdiControlNum | — |
| EDI_CONTROL_NUM | RcvShipmentHeadersEdiControlNum | — |
| EMPLOYEE_ID | RcvShipmentHeaders1EmployeeId | — |
| EMPLOYEE_ID | RcvShipmentHeadersEmployeeId | — |
| EXPECTED_RECEIPT_DATE | RcvShipmentHeaders1ExpectedReceiptDate | — |
| EXPECTED_RECEIPT_DATE | RcvShipmentHeadersExpectedReceiptDate | — |
| FREIGHT_AMOUNT | RcvShipmentHeaders1FreightAmount | — |
| FREIGHT_AMOUNT | RcvShipmentHeadersFreightAmount | — |
| FREIGHT_BILL_NUMBER | RcvShipmentHeaders1FreightBillNumber | — |
| FREIGHT_BILL_NUMBER | RcvShipmentHeadersFreightBillNumber | — |
| FREIGHT_CARRIER_ID | RcvShipmentHeaders1FreightCarrierId | — |
| FREIGHT_CARRIER_ID | RcvShipmentHeadersFreightCarrierId | — |
| FREIGHT_TERMS | RcvShipmentHeaders1FreightTerms | — |
| FREIGHT_TERMS | RcvShipmentHeadersFreightTerms | — |
| GOVERNMENT_CONTEXT | RcvShipmentHeaders1GovernmentContext | — |
| GOVERNMENT_CONTEXT | RcvShipmentHeadersGovernmentContext3 | — |
| GROSS_WEIGHT | RcvShipmentHeaders1GrossWeight | — |
| GROSS_WEIGHT | RcvShipmentHeadersGrossWeight | — |
| GROSS_WEIGHT_UOM_CODE | RcvShipmentHeaders1GrossWeightUomCode | — |
| GROSS_WEIGHT_UOM_CODE | RcvShipmentHeadersGrossWeightUomCode | — |
| HAZARD_CLASS | RcvShipmentHeaders1HazardClass | — |
| HAZARD_CLASS | RcvShipmentHeadersHazardClass | — |
| HAZARD_CODE | RcvShipmentHeaders1HazardCode | — |
| HAZARD_CODE | RcvShipmentHeadersHazardCode | — |
| HAZARD_DESCRIPTION | RcvShipmentHeaders1HazardDescription | — |
| HAZARD_DESCRIPTION | RcvShipmentHeadersHazardDescription | — |
| HEADER_INTERFACE_ID | RcvShipmentHeaders1HeaderInterfaceId | — |
| HEADER_INTERFACE_ID | RcvShipmentHeadersHeaderInterfaceId | — |
| INVOICE_AMOUNT | RcvShipmentHeaders1InvoiceAmount | — |
| INVOICE_AMOUNT | RcvShipmentHeadersInvoiceAmount | — |
| INVOICE_DATE | RcvShipmentHeaders1InvoiceDate | — |
| INVOICE_DATE | RcvShipmentHeadersInvoiceDate | — |
| INVOICE_NUM | RcvShipmentHeaders1InvoiceNum | — |
| INVOICE_NUM | RcvShipmentHeadersInvoiceNum | — |
| INVOICE_STATUS_CODE | RcvShipmentHeaders1InvoiceStatusCode | — |
| INVOICE_STATUS_CODE | RcvShipmentHeadersInvoiceStatusCode | — |
| JOB_DEFINITION_NAME | RcvShipmentHeaders1JobDefinitionName | — |
| JOB_DEFINITION_NAME | RcvShipmentHeadersJobDefinitionName3 | — |
| JOB_DEFINITION_PACKAGE | RcvShipmentHeaders1JobDefinitionPackage | — |
| JOB_DEFINITION_PACKAGE | RcvShipmentHeadersJobDefinitionPackage3 | — |
| LAST_UPDATE_DATE | RcvShipmentHeaders1LastUpdateDate | — |
| LAST_UPDATE_DATE | RcvShipmentHeadersLastUpdateDate4 | — |
| LAST_UPDATE_LOGIN | RcvShipmentHeaders1LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | RcvShipmentHeadersLastUpdateLogin4 | — |
| LAST_UPDATED_BY | RcvShipmentHeaders1LastUpdatedBy | — |
| LAST_UPDATED_BY | RcvShipmentHeadersLastUpdatedBy4 | — |
| LSP_FLAG | RcvShipmentHeaders1LspFlag | — |
| LSP_FLAG | RcvShipmentHeadersLspFlag | — |
| NET_WEIGHT | RcvShipmentHeaders1NetWeight | — |
| NET_WEIGHT | RcvShipmentHeadersNetWeight | — |
| NET_WEIGHT_UOM_CODE | RcvShipmentHeaders1NetWeightUomCode | — |
| NET_WEIGHT_UOM_CODE | RcvShipmentHeadersNetWeightUomCode | — |
| NOTICE_CREATION_DATE | RcvShipmentHeaders1NoticeCreationDate | — |
| NOTICE_CREATION_DATE | RcvShipmentHeadersNoticeCreationDate | — |
| NUM_OF_CONTAINERS | RcvShipmentHeaders1NumOfContainers | — |
| NUM_OF_CONTAINERS | RcvShipmentHeadersNumOfContainers | — |
| OBJECT_VERSION_NUMBER | RcvShipmentHeaders1ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | RcvShipmentHeadersObjectVersionNumber4 | — |
| ORGANIZATION_ID | RcvShipmentHeaders1OrganizationId | — |
| ORGANIZATION_ID | RcvShipmentHeadersOrganizationId | — |
| PACKAGING_CODE | RcvShipmentHeaders1PackagingCode | — |
| PACKAGING_CODE | RcvShipmentHeadersPackagingCode | — |
| PACKING_SLIP | RcvShipmentHeaders1PackingSlip | — |
| PACKING_SLIP | RcvShipmentHeadersPackingSlip | — |
| PAYMENT_TERMS_ID | RcvShipmentHeaders1PaymentTermsId | — |
| PAYMENT_TERMS_ID | RcvShipmentHeadersPaymentTermsId | — |
| PERFORMANCE_PERIOD_FROM | RcvShipmentHeaders1PerformancePeriodFrom | — |
| PERFORMANCE_PERIOD_FROM | RcvShipmentHeadersPerformancePeriodFrom | — |
| PERFORMANCE_PERIOD_TO | RcvShipmentHeaders1PerformancePeriodTo | — |
| PERFORMANCE_PERIOD_TO | RcvShipmentHeadersPerformancePeriodTo | — |
| RA_DOC_CREATION_DATE | RcvShipmentHeaders1RaDocCreationDate | — |
| RA_DOC_CREATION_DATE | RcvShipmentHeadersRaDocCreationDate | — |
| RA_DOC_LAST_UPDATE_DATE | RcvShipmentHeaders1RaDocLastUpdateDate | — |
| RA_DOC_LAST_UPDATE_DATE | RcvShipmentHeadersRaDocLastUpdateDate | — |
| RA_DOC_REVISION_DATE | RcvShipmentHeaders1RaDocRevisionDate | — |
| RA_DOC_REVISION_DATE | RcvShipmentHeadersRaDocRevisionDate | — |
| RA_DOC_REVISION_NUMBER | RcvShipmentHeaders1RaDocRevisionNumber | — |
| RA_DOC_REVISION_NUMBER | RcvShipmentHeadersRaDocRevisionNumber | — |
| RA_DOCUMENT_CODE | RcvShipmentHeaders1RaDocumentCode | — |
| RA_DOCUMENT_CODE | RcvShipmentHeadersRaDocumentCode | — |
| RA_DOCUMENT_NUMBER | RcvShipmentHeaders1RaDocumentNumber | — |
| RA_DOCUMENT_NUMBER | RcvShipmentHeadersRaDocumentNumber | — |
| RA_DOO_SOURCE_SYSTEM_ID | RcvShipmentHeaders1RaDooSourceSystemId | — |
| RA_DOO_SOURCE_SYSTEM_ID | RcvShipmentHeadersRaDooSourceSystemId | — |
| RA_NOTE_TO_RECEIVER | RcvShipmentHeaders1RaNoteToReceiver | — |
| RA_NOTE_TO_RECEIVER | RcvShipmentHeadersRaNoteToReceiver | — |
| RA_ORIG_SYSTEM_REF | RcvShipmentHeaders1RaOrigSystemRef | — |
| RA_ORIG_SYSTEM_REF | RcvShipmentHeadersRaOrigSystemRef | — |
| RA_OUTSOURCER_CONTACT_ID | RcvShipmentHeaders1RaOutsourcerContactId | — |
| RA_OUTSOURCER_CONTACT_ID | RcvShipmentHeadersRaOutsourcerContactId | — |
| RA_OUTSOURCER_PARTY_ID | RcvShipmentHeaders1RaOutsourcerPartyId | — |
| RA_OUTSOURCER_PARTY_ID | RcvShipmentHeadersRaOutsourcerPartyId | — |
| RECEIPT_ADVICE_NUMBER | RcvShipmentHeaders1ReceiptAdviceNumber | — |
| RECEIPT_ADVICE_NUMBER | RcvShipmentHeadersReceiptAdviceNumber | — |
| RECEIPT_NUM | RcvShipmentHeaders1ReceiptNum | — |
| RECEIPT_NUM | RcvShipmentHeadersReceiptNum1 | ✅ |
| RECEIPT_SOURCE_CODE | RcvShipmentHeaders1ReceiptSourceCode | — |
| RECEIPT_SOURCE_CODE | RcvShipmentHeadersReceiptSourceCode | — |
| REMIT_TO_SITE_ID | RcvShipmentHeaders1RemitToSiteId | — |
| REMIT_TO_SITE_ID | RcvShipmentHeadersRemitToSiteId | — |
| REQUEST_DATE | RcvShipmentHeaders1RequestDate | — |
| REQUEST_DATE | RcvShipmentHeadersRequestDate | — |
| REQUEST_ID | RcvShipmentHeaders1RequestId | — |
| REQUEST_ID | RcvShipmentHeadersRequestId3 | — |
| RMA_BU_ID | RcvShipmentHeaders1RmaBuId | — |
| RMA_BU_ID | RcvShipmentHeadersRmaBuId | — |
| SHIP_FROM_LOCATION_ID | RcvShipmentHeaders1ShipFromLocationId | — |
| SHIP_FROM_LOCATION_ID | RcvShipmentHeadersShipFromLocationId | — |
| SHIP_TO_LOCATION_ID | RcvShipmentHeaders1ShipToLocationId | — |
| SHIP_TO_LOCATION_ID | RcvShipmentHeadersShipToLocationId2 | — |
| SHIP_TO_ORG_ID | RcvShipmentHeaders1ShipToOrgId | — |
| SHIP_TO_ORG_ID | RcvShipmentHeadersShipToOrgId | — |
| SHIPMENT_HEADER_ID | RcvShipmentHeaders1ShipmentHeaderId | — |
| SHIPMENT_HEADER_ID | RcvShipmentHeadersShipmentHeaderId1 | — |
| SHIPMENT_NUM | RcvShipmentHeaders1ShipmentNum | — |
| SHIPMENT_NUM | RcvShipmentHeadersShipmentNum1 | — |
| SHIPPED_DATE | RcvShipmentHeaders1ShippedDate | — |
| SHIPPED_DATE | RcvShipmentHeadersShippedDate | — |
| SPECIAL_HANDLING_CODE | RcvShipmentHeaders1SpecialHandlingCode | — |
| SPECIAL_HANDLING_CODE | RcvShipmentHeadersSpecialHandlingCode | — |
| TAR_WEIGHT | RcvShipmentHeaders1TarWeight | — |
| TAR_WEIGHT | RcvShipmentHeadersTarWeight | — |
| TAR_WEIGHT_UOM_CODE | RcvShipmentHeaders1TarWeightUomCode | — |
| TAR_WEIGHT_UOM_CODE | RcvShipmentHeadersTarWeightUomCode | — |
| TAX_AMOUNT | RcvShipmentHeaders1TaxAmount | — |
| TAX_AMOUNT | RcvShipmentHeadersTaxAmount | — |
| TAX_NAME | RcvShipmentHeaders1TaxName | — |
| TAX_NAME | RcvShipmentHeadersTaxName2 | — |
| VENDOR_ID | RcvShipmentHeaders1VendorId | — |
| VENDOR_ID | RcvShipmentHeadersVendorId1 | — |
| VENDOR_SITE_ID | RcvShipmentHeaders1VendorSiteId | — |
| VENDOR_SITE_ID | RcvShipmentHeadersVendorSiteId1 | — |
| WAYBILL_AIRBILL_NUM | RcvShipmentHeaders1WaybillAirbillNum | — |
| WAYBILL_AIRBILL_NUM | RcvShipmentHeadersWaybillAirbillNum | — |

### [[inventorytransactiondetailpvo|InventoryTransactionDetailPVO]] (OTHER · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | RCVSHIPHPEOObjectVersionNumber3 | — |
| RA_DOCUMENT_NUMBER | RaDocumentNumber | ✅ |
| SHIPMENT_HEADER_ID | ShipmentHeaderId | — |

### [[invoiceheaderholdspvo|InvoiceHeaderHoldsPVO]] (AP · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LAST_UPDATE_DATE | RcvShipHeaderInvHoldLastUpdateDate | — |
| OBJECT_VERSION_NUMBER | RcvShipHeaderInvHoldObjectVersionNumber | — |
| RA_DOC_LAST_UPDATE_DATE | RcvShipHeaderInvHoldRaDocLastUpdateDate | — |
| RECEIPT_NUM | RcvShipHeaderInvHoldReceiptNum | ✅ |
| SHIPMENT_HEADER_ID | RcvShipHeaderInvHoldShipmentHeaderId | — |

### [[invoiceholdpvo|InvoiceHoldPVO]] (AP · BICC: 3/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LAST_UPDATE_DATE | RcvShipHeaderInvHoldLastUpdateDate | ✅ |
| OBJECT_VERSION_NUMBER | RcvShipHeaderInvHoldObjectVersionNumber | — |
| RA_DOC_LAST_UPDATE_DATE | RcvShipHeaderInvHoldRaDocLastUpdateDate | ✅ |
| RECEIPT_NUM | RcvShipHeaderInvHoldReceiptNum | ✅ |
| SHIPMENT_HEADER_ID | RcvShipHeaderInvHoldShipmentHeaderId | — |

### [[invoiceholdpvoactiveholds|InvoiceHoldPVOActiveHolds]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LAST_UPDATE_DATE | RcvShipHeaderInvHoldLastUpdateDate | — |
| OBJECT_VERSION_NUMBER | RcvShipHeaderInvHoldObjectVersionNumber | — |
| RA_DOC_LAST_UPDATE_DATE | RcvShipHeaderInvHoldRaDocLastUpdateDate | — |
| RECEIPT_NUM | RcvShipHeaderInvHoldReceiptNum | — |
| SHIPMENT_HEADER_ID | RcvShipHeaderInvHoldShipmentHeaderId | — |

### [[invoicelineholdspvo|InvoiceLineHoldsPVO]] (AP · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LAST_UPDATE_DATE | RcvShipHeaderInvHoldLastUpdateDate | — |
| OBJECT_VERSION_NUMBER | RcvShipHeaderInvHoldObjectVersionNumber | — |
| RA_DOC_LAST_UPDATE_DATE | RcvShipHeaderInvHoldRaDocLastUpdateDate | — |
| RECEIPT_NUM | RcvShipHeaderInvHoldReceiptNum | ✅ |
| SHIPMENT_HEADER_ID | RcvShipHeaderInvHoldShipmentHeaderId | — |

### [[invoicelinepvo|InvoiceLinePVO]] (AP · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| RECEIPT_NUM | RcvShipHeaderInvLineReceiptNum | ✅ |
| SHIPMENT_HEADER_ID | RcvShipHeaderInvLineShipmentHeaderId | — |

### [[landedcostpvo|LandedCostPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPROVAL_STATUS | ReceivingShipmentReceiptHeaderPEOApprovalStatus | — |
| ASN_STATUS | ReceivingShipmentReceiptHeaderPEOAsnStatus | — |
| ASN_TYPE | ReceivingShipmentReceiptHeaderPEOAsnType | — |
| ATTRIBUTE1 | ReceivingShipmentReceiptHeaderPEOAttribute110 | — |
| ATTRIBUTE10 | ReceivingShipmentReceiptHeaderPEOAttribute102 | — |
| ATTRIBUTE11 | ReceivingShipmentReceiptHeaderPEOAttribute112 | — |
| ATTRIBUTE12 | ReceivingShipmentReceiptHeaderPEOAttribute122 | — |
| ATTRIBUTE13 | ReceivingShipmentReceiptHeaderPEOAttribute132 | — |
| ATTRIBUTE14 | ReceivingShipmentReceiptHeaderPEOAttribute142 | — |
| ATTRIBUTE15 | ReceivingShipmentReceiptHeaderPEOAttribute152 | — |
| ATTRIBUTE16 | ReceivingShipmentReceiptHeaderPEOAttribute162 | — |
| ATTRIBUTE17 | ReceivingShipmentReceiptHeaderPEOAttribute171 | — |
| ATTRIBUTE18 | ReceivingShipmentReceiptHeaderPEOAttribute181 | — |
| ATTRIBUTE19 | ReceivingShipmentReceiptHeaderPEOAttribute191 | — |
| ATTRIBUTE2 | ReceivingShipmentReceiptHeaderPEOAttribute22 | — |
| ATTRIBUTE20 | ReceivingShipmentReceiptHeaderPEOAttribute201 | — |
| ATTRIBUTE3 | ReceivingShipmentReceiptHeaderPEOAttribute32 | — |
| ATTRIBUTE4 | ReceivingShipmentReceiptHeaderPEOAttribute42 | — |
| ATTRIBUTE5 | ReceivingShipmentReceiptHeaderPEOAttribute52 | — |
| ATTRIBUTE6 | ReceivingShipmentReceiptHeaderPEOAttribute62 | — |
| ATTRIBUTE7 | ReceivingShipmentReceiptHeaderPEOAttribute72 | — |
| ATTRIBUTE8 | ReceivingShipmentReceiptHeaderPEOAttribute82 | — |
| ATTRIBUTE9 | ReceivingShipmentReceiptHeaderPEOAttribute92 | — |
| ATTRIBUTE_CATEGORY | ReceivingShipmentReceiptHeaderPEOAttributeCategory2 | — |
| ATTRIBUTE_DATE1 | ReceivingShipmentReceiptHeaderPEOAttributeDate11 | — |
| ATTRIBUTE_DATE2 | ReceivingShipmentReceiptHeaderPEOAttributeDate21 | — |
| ATTRIBUTE_DATE3 | ReceivingShipmentReceiptHeaderPEOAttributeDate31 | — |
| ATTRIBUTE_DATE4 | ReceivingShipmentReceiptHeaderPEOAttributeDate41 | — |
| ATTRIBUTE_DATE5 | ReceivingShipmentReceiptHeaderPEOAttributeDate51 | — |
| ATTRIBUTE_NUMBER1 | ReceivingShipmentReceiptHeaderPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER10 | ReceivingShipmentReceiptHeaderPEOAttributeNumber101 | — |
| ATTRIBUTE_NUMBER2 | ReceivingShipmentReceiptHeaderPEOAttributeNumber21 | — |
| ATTRIBUTE_NUMBER3 | ReceivingShipmentReceiptHeaderPEOAttributeNumber31 | — |
| ATTRIBUTE_NUMBER4 | ReceivingShipmentReceiptHeaderPEOAttributeNumber41 | — |
| ATTRIBUTE_NUMBER5 | ReceivingShipmentReceiptHeaderPEOAttributeNumber51 | — |
| ATTRIBUTE_NUMBER6 | ReceivingShipmentReceiptHeaderPEOAttributeNumber61 | — |
| ATTRIBUTE_NUMBER7 | ReceivingShipmentReceiptHeaderPEOAttributeNumber71 | — |
| ATTRIBUTE_NUMBER8 | ReceivingShipmentReceiptHeaderPEOAttributeNumber81 | — |
| ATTRIBUTE_NUMBER9 | ReceivingShipmentReceiptHeaderPEOAttributeNumber91 | — |
| ATTRIBUTE_TIMESTAMP1 | ReceivingShipmentReceiptHeaderPEOAttributeTimestamp11 | — |
| ATTRIBUTE_TIMESTAMP2 | ReceivingShipmentReceiptHeaderPEOAttributeTimestamp21 | — |
| ATTRIBUTE_TIMESTAMP3 | ReceivingShipmentReceiptHeaderPEOAttributeTimestamp31 | — |
| ATTRIBUTE_TIMESTAMP4 | ReceivingShipmentReceiptHeaderPEOAttributeTimestamp41 | — |
| ATTRIBUTE_TIMESTAMP5 | ReceivingShipmentReceiptHeaderPEOAttributeTimestamp51 | — |
| BILL_OF_LADING | ReceivingShipmentReceiptHeaderPEOBillOfLading | — |
| CARRIER_EQUIPMENT | ReceivingShipmentReceiptHeaderPEOCarrierEquipment | — |
| CARRIER_METHOD | ReceivingShipmentReceiptHeaderPEOCarrierMethod | — |
| COMMENTS | ReceivingShipmentReceiptHeaderPEOComments1 | — |
| CONVERSION_DATE | ReceivingShipmentReceiptHeaderPEOConversionDate | — |
| CONVERSION_RATE | ReceivingShipmentReceiptHeaderPEOConversionRate | — |
| CONVERSION_RATE_TYPE | ReceivingShipmentReceiptHeaderPEOConversionRateType | — |
| CREATED_BY | ReceivingShipmentReceiptHeaderPEOCreatedBy3 | — |
| CREATION_DATE | ReceivingShipmentReceiptHeaderPEOCreationDate3 | — |
| CURRENCY_CODE | ReceivingShipmentReceiptHeaderPEOCurrencyCode1 | — |
| CUSTOMER_ID | ReceivingShipmentReceiptHeaderPEOCustomerId1 | — |
| CUSTOMER_SITE_ID | ReceivingShipmentReceiptHeaderPEOCustomerSiteId1 | — |
| EDI_CONTROL_NUM | ReceivingShipmentReceiptHeaderPEOEdiControlNum | — |
| EMPLOYEE_ID | ReceivingShipmentReceiptHeaderPEOEmployeeId1 | — |
| EXPECTED_RECEIPT_DATE | ReceivingShipmentReceiptHeaderPEOExpectedReceiptDate | — |
| FREIGHT_AMOUNT | ReceivingShipmentReceiptHeaderPEOFreightAmount | — |
| FREIGHT_BILL_NUMBER | ReceivingShipmentReceiptHeaderPEOFreightBillNumber | — |
| FREIGHT_CARRIER_ID | ReceivingShipmentReceiptHeaderPEOFreightCarrierId | — |
| FREIGHT_TERMS | ReceivingShipmentReceiptHeaderPEOFreightTerms | — |
| GOVERNMENT_CONTEXT | ReceivingShipmentReceiptHeaderPEOGovernmentContext | — |
| GROSS_WEIGHT | ReceivingShipmentReceiptHeaderPEOGrossWeight | — |
| HAZARD_CLASS | ReceivingShipmentReceiptHeaderPEOHazardClass | — |
| HAZARD_CODE | ReceivingShipmentReceiptHeaderPEOHazardCode | — |
| HAZARD_DESCRIPTION | ReceivingShipmentReceiptHeaderPEOHazardDescription | — |
| HEADER_INTERFACE_ID | ReceivingShipmentReceiptHeaderPEOHeaderInterfaceId | — |
| INVOICE_AMOUNT | ReceivingShipmentReceiptHeaderPEOInvoiceAmount | — |
| INVOICE_DATE | ReceivingShipmentReceiptHeaderPEOInvoiceDate | — |
| INVOICE_NUM | ReceivingShipmentReceiptHeaderPEOInvoiceNum | — |
| INVOICE_STATUS_CODE | ReceivingShipmentReceiptHeaderPEOInvoiceStatusCode1 | — |
| JOB_DEFINITION_NAME | ReceivingShipmentReceiptHeaderPEOJobDefinitionName2 | — |
| JOB_DEFINITION_PACKAGE | ReceivingShipmentReceiptHeaderPEOJobDefinitionPackage2 | — |
| LAST_UPDATE_DATE | ReceivingShipmentReceiptHeaderPEOLastUpdateDate3 | — |
| LAST_UPDATE_LOGIN | ReceivingShipmentReceiptHeaderPEOLastUpdateLogin3 | — |
| LAST_UPDATED_BY | ReceivingShipmentReceiptHeaderPEOLastUpdatedBy3 | — |
| LSP_FLAG | ReceivingShipmentReceiptHeaderPEOLspFlag | — |
| NET_WEIGHT | ReceivingShipmentReceiptHeaderPEONetWeight | — |
| NET_WEIGHT_UOM_CODE | ReceivingShipmentReceiptHeaderPEONetWeightUomCode | — |
| NOTICE_CREATION_DATE | ReceivingShipmentReceiptHeaderPEONoticeCreationDate | — |
| NUM_OF_CONTAINERS | ReceivingShipmentReceiptHeaderPEONumOfContainers | — |
| OBJECT_VERSION_NUMBER | ReceivingShipmentReceiptHeaderPEOObjectVersionNumber1 | — |
| ORGANIZATION_ID | ReceivingShipmentReceiptHeaderPEOOrganizationId1 | — |
| PACKAGING_CODE | ReceivingShipmentReceiptHeaderPEOPackagingCode | — |
| PACKING_SLIP | ReceivingShipmentReceiptHeaderPEOPackingSlip | — |
| PAYMENT_TERMS_ID | ReceivingShipmentReceiptHeaderPEOPaymentTermsId | — |
| PERFORMANCE_PERIOD_FROM | ReceivingShipmentReceiptHeaderPEOPerformancePeriodFrom | — |
| PERFORMANCE_PERIOD_TO | ReceivingShipmentReceiptHeaderPEOPerformancePeriodTo | — |
| RA_DOC_CREATION_DATE | ReceivingShipmentReceiptHeaderPEORaDocCreationDate | — |
| RA_DOC_LAST_UPDATE_DATE | ReceivingShipmentReceiptHeaderPEORaDocLastUpdateDate | — |
| RA_DOC_REVISION_DATE | ReceivingShipmentReceiptHeaderPEORaDocRevisionDate | — |
| RA_DOC_REVISION_NUMBER | ReceivingShipmentReceiptHeaderPEORaDocRevisionNumber | — |
| RA_DOCUMENT_CODE | ReceivingShipmentReceiptHeaderPEORaDocumentCode | — |
| RA_DOCUMENT_NUMBER | ReceivingShipmentReceiptHeaderPEORaDocumentNumber | — |
| RA_DOO_SOURCE_SYSTEM_ID | ReceivingShipmentReceiptHeaderPEORaDooSourceSystemId | — |
| RA_NOTE_TO_RECEIVER | ReceivingShipmentReceiptHeaderPEORaNoteToReceiver | — |
| RA_ORIG_SYSTEM_REF | ReceivingShipmentReceiptHeaderPEORaOrigSystemRef | — |
| RA_OUTSOURCER_CONTACT_ID | ReceivingShipmentReceiptHeaderPEORaOutsourcerContactId | — |
| RA_OUTSOURCER_PARTY_ID | ReceivingShipmentReceiptHeaderPEORaOutsourcerPartyId | — |
| RECEIPT_ADVICE_NUMBER | ReceivingShipmentReceiptHeaderPEOReceiptAdviceNumber | — |
| RECEIPT_NUM | ReceivingShipmentReceiptHeaderPEOReceiptNum | — |
| RECEIPT_SOURCE_CODE | ReceivingShipmentReceiptHeaderPEOReceiptSourceCode | — |
| REMIT_TO_SITE_ID | ReceivingShipmentReceiptHeaderPEORemitToSiteId | — |
| REQUEST_DATE | ReceivingShipmentReceiptHeaderPEORequestDate | — |
| REQUEST_ID | ReceivingShipmentReceiptHeaderPEORequestId2 | — |
| RMA_BU_ID | ReceivingShipmentReceiptHeaderPEORmaBuId | — |
| SHIP_FROM_LOCATION_ID | ReceivingShipmentReceiptHeaderPEOShipFromLocationId2 | — |
| SHIP_TO_LOCATION_ID | ShipToLocationId | — |
| SHIP_TO_ORG_ID | ReceivingShipmentReceiptHeaderPEOShipToOrgId | — |
| SHIPMENT_HEADER_ID | ReceivingShipmentReceiptHeaderPEOShipmentHeaderId1 | — |
| SHIPMENT_NUM | ReceivingShipmentReceiptHeaderPEOShipmentNum | — |
| SHIPPED_DATE | ReceivingShipmentReceiptHeaderPEOShippedDate | — |
| SPECIAL_HANDLING_CODE | ReceivingShipmentReceiptHeaderPEOSpecialHandlingCode | — |
| TAR_WEIGHT | ReceivingShipmentReceiptHeaderPEOTarWeight | — |
| TAR_WEIGHT_UOM_CODE | ReceivingShipmentReceiptHeaderPEOTarWeightUomCode | — |
| TAX_AMOUNT | ReceivingShipmentReceiptHeaderPEOTaxAmount | — |
| TAX_NAME | ReceivingShipmentReceiptHeaderPEOTaxName | — |
| VENDOR_ID | ReceivingShipmentReceiptHeaderPEOVendorId1 | — |
| VENDOR_SITE_ID | ReceivingShipmentReceiptHeaderPEOVendorSiteId1 | — |
| WAYBILL_AIRBILL_NUM | ReceivingShipmentReceiptHeaderPEOWaybillAirbillNum | — |

### [[maintenancewooperationspvo|MaintenanceWOOperationsPVO]] (OTHER · BICC: 1/123)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPROVAL_STATUS | RcvShipmentHeadersApprovalStatus1 | — |
| ASN_STATUS | RcvShipmentHeadersAsnStatus | — |
| ASN_TYPE | RcvShipmentHeadersAsnType | — |
| ATTRIBUTE1 | RcvShipmentHeadersAttribute116 | — |
| ATTRIBUTE10 | RcvShipmentHeadersAttribute104 | — |
| ATTRIBUTE11 | RcvShipmentHeadersAttribute117 | — |
| ATTRIBUTE12 | RcvShipmentHeadersAttribute124 | — |
| ATTRIBUTE13 | RcvShipmentHeadersAttribute134 | — |
| ATTRIBUTE14 | RcvShipmentHeadersAttribute144 | — |
| ATTRIBUTE15 | RcvShipmentHeadersAttribute154 | — |
| ATTRIBUTE16 | RcvShipmentHeadersAttribute164 | — |
| ATTRIBUTE17 | RcvShipmentHeadersAttribute174 | — |
| ATTRIBUTE18 | RcvShipmentHeadersAttribute184 | — |
| ATTRIBUTE19 | RcvShipmentHeadersAttribute194 | — |
| ATTRIBUTE2 | RcvShipmentHeadersAttribute24 | — |
| ATTRIBUTE20 | RcvShipmentHeadersAttribute204 | — |
| ATTRIBUTE3 | RcvShipmentHeadersAttribute34 | — |
| ATTRIBUTE4 | RcvShipmentHeadersAttribute44 | — |
| ATTRIBUTE5 | RcvShipmentHeadersAttribute54 | — |
| ATTRIBUTE6 | RcvShipmentHeadersAttribute64 | — |
| ATTRIBUTE7 | RcvShipmentHeadersAttribute74 | — |
| ATTRIBUTE8 | RcvShipmentHeadersAttribute84 | — |
| ATTRIBUTE9 | RcvShipmentHeadersAttribute94 | — |
| ATTRIBUTE_CATEGORY | RcvShipmentHeadersAttributeCategory4 | — |
| ATTRIBUTE_DATE1 | RcvShipmentHeadersAttributeDate14 | — |
| ATTRIBUTE_DATE2 | RcvShipmentHeadersAttributeDate24 | — |
| ATTRIBUTE_DATE3 | RcvShipmentHeadersAttributeDate34 | — |
| ATTRIBUTE_DATE4 | RcvShipmentHeadersAttributeDate44 | — |
| ATTRIBUTE_DATE5 | RcvShipmentHeadersAttributeDate54 | — |
| ATTRIBUTE_NUMBER1 | RcvShipmentHeadersAttributeNumber14 | — |
| ATTRIBUTE_NUMBER10 | RcvShipmentHeadersAttributeNumber104 | — |
| ATTRIBUTE_NUMBER2 | RcvShipmentHeadersAttributeNumber24 | — |
| ATTRIBUTE_NUMBER3 | RcvShipmentHeadersAttributeNumber34 | — |
| ATTRIBUTE_NUMBER4 | RcvShipmentHeadersAttributeNumber44 | — |
| ATTRIBUTE_NUMBER5 | RcvShipmentHeadersAttributeNumber54 | — |
| ATTRIBUTE_NUMBER6 | RcvShipmentHeadersAttributeNumber64 | — |
| ATTRIBUTE_NUMBER7 | RcvShipmentHeadersAttributeNumber74 | — |
| ATTRIBUTE_NUMBER8 | RcvShipmentHeadersAttributeNumber84 | — |
| ATTRIBUTE_NUMBER9 | RcvShipmentHeadersAttributeNumber94 | — |
| ATTRIBUTE_TIMESTAMP1 | RcvShipmentHeadersAttributeTimestamp14 | — |
| ATTRIBUTE_TIMESTAMP2 | RcvShipmentHeadersAttributeTimestamp24 | — |
| ATTRIBUTE_TIMESTAMP3 | RcvShipmentHeadersAttributeTimestamp34 | — |
| ATTRIBUTE_TIMESTAMP4 | RcvShipmentHeadersAttributeTimestamp44 | — |
| ATTRIBUTE_TIMESTAMP5 | RcvShipmentHeadersAttributeTimestamp54 | — |
| BILL_OF_LADING | RcvShipmentHeadersBillOfLading | — |
| CARRIER_EQUIPMENT | RcvShipmentHeadersCarrierEquipment | — |
| CARRIER_METHOD | RcvShipmentHeadersCarrierMethod | — |
| COMMENTS | RcvShipmentHeadersComments2 | — |
| CONVERSION_DATE | RcvShipmentHeadersConversionDate | — |
| CONVERSION_RATE | RcvShipmentHeadersConversionRate | — |
| CONVERSION_RATE_TYPE | RcvShipmentHeadersConversionRateType | — |
| CREATED_BY | RcvShipmentHeadersCreatedBy4 | — |
| CREATION_DATE | RcvShipmentHeadersCreationDate4 | — |
| CURRENCY_CODE | RcvShipmentHeadersCurrencyCode1 | — |
| CUSTOMER_ID | RcvShipmentHeadersCustomerId1 | — |
| CUSTOMER_SITE_ID | RcvShipmentHeadersCustomerSiteId1 | — |
| EDI_CONTROL_NUM | RcvShipmentHeadersEdiControlNum | — |
| EMPLOYEE_ID | RcvShipmentHeadersEmployeeId1 | — |
| EXPECTED_RECEIPT_DATE | RcvShipmentHeadersExpectedReceiptDate | — |
| FREIGHT_AMOUNT | RcvShipmentHeadersFreightAmount | — |
| FREIGHT_BILL_NUMBER | RcvShipmentHeadersFreightBillNumber | — |
| FREIGHT_CARRIER_ID | RcvShipmentHeadersFreightCarrierId | — |
| FREIGHT_TERMS | RcvShipmentHeadersFreightTerms | — |
| GOVERNMENT_CONTEXT | RcvShipmentHeadersGovernmentContext4 | — |
| GROSS_WEIGHT | RcvShipmentHeadersGrossWeight | — |
| GROSS_WEIGHT_UOM_CODE | RcvShipmentHeadersGrossWeightUomCode | — |
| HAZARD_CLASS | RcvShipmentHeadersHazardClass | — |
| HAZARD_CODE | RcvShipmentHeadersHazardCode | — |
| HAZARD_DESCRIPTION | RcvShipmentHeadersHazardDescription | — |
| HEADER_INTERFACE_ID | RcvShipmentHeadersHeaderInterfaceId | — |
| INVOICE_AMOUNT | RcvShipmentHeadersInvoiceAmount | — |
| INVOICE_DATE | RcvShipmentHeadersInvoiceDate | — |
| INVOICE_NUM | RcvShipmentHeadersInvoiceNum | — |
| INVOICE_STATUS_CODE | RcvShipmentHeadersInvoiceStatusCode1 | — |
| JOB_DEFINITION_NAME | RcvShipmentHeadersJobDefinitionName4 | — |
| JOB_DEFINITION_PACKAGE | RcvShipmentHeadersJobDefinitionPackage4 | — |
| LAST_UPDATE_DATE | RcvShipmentHeadersLastUpdateDate4 | — |
| LAST_UPDATE_LOGIN | RcvShipmentHeadersLastUpdateLogin4 | — |
| LAST_UPDATED_BY | RcvShipmentHeadersLastUpdatedBy4 | — |
| LSP_FLAG | RcvShipmentHeadersLspFlag | — |
| NET_WEIGHT | RcvShipmentHeadersNetWeight | — |
| NET_WEIGHT_UOM_CODE | RcvShipmentHeadersNetWeightUomCode | — |
| NOTICE_CREATION_DATE | RcvShipmentHeadersNoticeCreationDate | — |
| NUM_OF_CONTAINERS | RcvShipmentHeadersNumOfContainers | — |
| OBJECT_VERSION_NUMBER | RcvShipmentHeadersObjectVersionNumber4 | — |
| ORGANIZATION_ID | RcvShipmentHeadersOrganizationId | — |
| PACKAGING_CODE | RcvShipmentHeadersPackagingCode | — |
| PACKING_SLIP | RcvShipmentHeadersPackingSlip1 | — |
| PAYMENT_TERMS_ID | RcvShipmentHeadersPaymentTermsId | — |
| PERFORMANCE_PERIOD_FROM | RcvShipmentHeadersPerformancePeriodFrom | — |
| PERFORMANCE_PERIOD_TO | RcvShipmentHeadersPerformancePeriodTo | — |
| RA_DOC_CREATION_DATE | RcvShipmentHeadersRaDocCreationDate | — |
| RA_DOC_LAST_UPDATE_DATE | RcvShipmentHeadersRaDocLastUpdateDate | — |
| RA_DOC_REVISION_DATE | RcvShipmentHeadersRaDocRevisionDate | — |
| RA_DOC_REVISION_NUMBER | RcvShipmentHeadersRaDocRevisionNumber | — |
| RA_DOCUMENT_CODE | RcvShipmentHeadersRaDocumentCode | — |
| RA_DOCUMENT_NUMBER | RcvShipmentHeadersRaDocumentNumber | — |
| RA_DOO_SOURCE_SYSTEM_ID | RcvShipmentHeadersRaDooSourceSystemId | — |
| RA_NOTE_TO_RECEIVER | RcvShipmentHeadersRaNoteToReceiver1 | — |
| RA_ORIG_SYSTEM_REF | RcvShipmentHeadersRaOrigSystemRef | — |
| RA_OUTSOURCER_CONTACT_ID | RcvShipmentHeadersRaOutsourcerContactId | — |
| RA_OUTSOURCER_PARTY_ID | RcvShipmentHeadersRaOutsourcerPartyId | — |
| RECEIPT_ADVICE_NUMBER | RcvShipmentHeadersReceiptAdviceNumber | — |
| RECEIPT_NUM | RcvShipmentHeadersReceiptNum | ✅ |
| RECEIPT_SOURCE_CODE | RcvShipmentHeadersReceiptSourceCode | — |
| REMIT_TO_SITE_ID | RcvShipmentHeadersRemitToSiteId | — |
| REQUEST_DATE | RcvShipmentHeadersRequestDate | — |
| REQUEST_ID | RcvShipmentHeadersRequestId4 | — |
| RMA_BU_ID | RcvShipmentHeadersRmaBuId | — |
| SHIP_FROM_LOCATION_ID | RcvShipmentHeadersShipFromLocationId1 | — |
| SHIP_TO_LOCATION_ID | RcvShipmentHeadersShipToLocationId3 | — |
| SHIP_TO_ORG_ID | RcvShipmentHeadersShipToOrgId | — |
| SHIPMENT_HEADER_ID | RcvShipmentHeadersShipmentHeaderId1 | — |
| SHIPMENT_NUM | RcvShipmentHeadersShipmentNum1 | — |
| SHIPPED_DATE | RcvShipmentHeadersShippedDate | — |
| SPECIAL_HANDLING_CODE | RcvShipmentHeadersSpecialHandlingCode | — |
| TAR_WEIGHT | RcvShipmentHeadersTarWeight | — |
| TAR_WEIGHT_UOM_CODE | RcvShipmentHeadersTarWeightUomCode | — |
| TAX_AMOUNT | RcvShipmentHeadersTaxAmount1 | — |
| TAX_NAME | RcvShipmentHeadersTaxName3 | — |
| VENDOR_ID | RcvShipmentHeadersVendorId1 | — |
| VENDOR_SITE_ID | RcvShipmentHeadersVendorSiteId1 | — |
| WAYBILL_AIRBILL_NUM | RcvShipmentHeadersWaybillAirbillNum | — |

### [[maintenancewoprocurementreceiptpvo|MaintenanceWOProcurementReceiptPVO]] (OTHER · BICC: 6/82)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPROVAL_STATUS | RcvShipmentReceiptHeaderPEOApprovalStatus | — |
| ASN_STATUS | RcvShipmentReceiptHeaderPEOAsnStatus | — |
| ASN_TYPE | RcvShipmentReceiptHeaderPEOAsnType | — |
| BILL_OF_LADING | RcvShipmentReceiptHeaderPEOBillOfLading | — |
| CARRIER_EQUIPMENT | RcvShipmentReceiptHeaderPEOCarrierEquipment | — |
| CARRIER_METHOD | RcvShipmentReceiptHeaderPEOCarrierMethod | — |
| COMMENTS | RcvShipmentReceiptHeaderPEOComments | — |
| CONVERSION_DATE | RcvShipmentReceiptHeaderPEOConversionDate | — |
| CONVERSION_RATE | RcvShipmentReceiptHeaderPEOConversionRate | — |
| CONVERSION_RATE_TYPE | RcvShipmentReceiptHeaderPEOConversionRateType | — |
| CREATED_BY | RcvShipmentReceiptHeaderPEOCreatedBy | — |
| CREATION_DATE | RcvShipmentReceiptHeaderPEOCreationDate | ✅ |
| CURRENCY_CODE | RcvShipmentReceiptHeaderPEOCurrencyCode | — |
| CUSTOMER_ID | RcvShipmentReceiptHeaderPEOCustomerId | — |
| CUSTOMER_SITE_ID | RcvShipmentReceiptHeaderPEOCustomerSiteId | — |
| EDI_CONTROL_NUM | RcvShipmentReceiptHeaderPEOEdiControlNum | — |
| EMPLOYEE_ID | RcvShipmentReceiptHeaderPEOEmployeeId | — |
| EXPECTED_RECEIPT_DATE | RcvShipmentReceiptHeaderPEOExpectedReceiptDate | — |
| FREIGHT_AMOUNT | RcvShipmentReceiptHeaderPEOFreightAmount | — |
| FREIGHT_BILL_NUMBER | RcvShipmentReceiptHeaderPEOFreightBillNumber | — |
| FREIGHT_CARRIER_ID | RcvShipmentReceiptHeaderPEOFreightCarrierId | — |
| FREIGHT_TERMS | RcvShipmentReceiptHeaderPEOFreightTerms | — |
| GOVERNMENT_CONTEXT | RcvShipmentReceiptHeaderPEOGovernmentContext | — |
| GROSS_WEIGHT | RcvShipmentReceiptHeaderPEOGrossWeight | — |
| GROSS_WEIGHT_UOM_CODE | RcvShipmentReceiptHeaderPEOGrossWeightUomCode | — |
| HAZARD_CLASS | RcvShipmentReceiptHeaderPEOHazardClass | — |
| HAZARD_CODE | RcvShipmentReceiptHeaderPEOHazardCode | — |
| HAZARD_DESCRIPTION | RcvShipmentReceiptHeaderPEOHazardDescription | — |
| HEADER_INTERFACE_ID | RcvShipmentReceiptHeaderPEOHeaderInterfaceId | — |
| INVOICE_AMOUNT | RcvShipmentReceiptHeaderPEOInvoiceAmount | — |
| INVOICE_DATE | RcvShipmentReceiptHeaderPEOInvoiceDate | — |
| INVOICE_NUM | RcvShipmentReceiptHeaderPEOInvoiceNum | — |
| INVOICE_STATUS_CODE | RcvShipmentReceiptHeaderPEOInvoiceStatusCode | — |
| JOB_DEFINITION_NAME | RcvShipmentReceiptHeaderPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | RcvShipmentReceiptHeaderPEOJobDefinitionPackage | — |
| LAST_UPDATE_DATE | RcvShipmentReceiptHeaderPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RcvShipmentReceiptHeaderPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | RcvShipmentReceiptHeaderPEOLastUpdatedBy | — |
| LSP_FLAG | RcvShipmentReceiptHeaderPEOLspFlag | — |
| NET_WEIGHT | RcvShipmentReceiptHeaderPEONetWeight | — |
| NET_WEIGHT_UOM_CODE | RcvShipmentReceiptHeaderPEONetWeightUomCode | — |
| NOTICE_CREATION_DATE | RcvShipmentReceiptHeaderPEONoticeCreationDate | — |
| NUM_OF_CONTAINERS | RcvShipmentReceiptHeaderPEONumOfContainers | — |
| OBJECT_VERSION_NUMBER | RcvShipmentReceiptHeaderPEOObjectVersionNumber | — |
| ORGANIZATION_ID | RcvShipmentReceiptHeaderPEOOrganizationId | — |
| PACKAGING_CODE | RcvShipmentReceiptHeaderPEOPackagingCode | — |
| PACKING_SLIP | RcvShipmentReceiptHeaderPEOPackingSlip | — |
| PAYMENT_TERMS_ID | RcvShipmentReceiptHeaderPEOPaymentTermsId | — |
| PERFORMANCE_PERIOD_FROM | RcvShipmentReceiptHeaderPEOPerformancePeriodFrom | — |
| PERFORMANCE_PERIOD_TO | RcvShipmentReceiptHeaderPEOPerformancePeriodTo | — |
| RA_DOC_CREATION_DATE | RcvShipmentReceiptHeaderPEORaDocCreationDate | — |
| RA_DOC_LAST_UPDATE_DATE | RcvShipmentReceiptHeaderPEORaDocLastUpdateDate | ✅ |
| RA_DOC_REVISION_DATE | RcvShipmentReceiptHeaderPEORaDocRevisionDate | — |
| RA_DOC_REVISION_NUMBER | RcvShipmentReceiptHeaderPEORaDocRevisionNumber | — |
| RA_DOCUMENT_CODE | RcvShipmentReceiptHeaderPEORaDocumentCode | — |
| RA_DOCUMENT_NUMBER | RcvShipmentReceiptHeaderPEORaDocumentNumber | — |
| RA_DOO_SOURCE_SYSTEM_ID | RcvShipmentReceiptHeaderPEORaDooSourceSystemId | — |
| RA_NOTE_TO_RECEIVER | RcvShipmentReceiptHeaderPEORaNoteToReceiver | — |
| RA_ORIG_SYSTEM_REF | RcvShipmentReceiptHeaderPEORaOrigSystemRef | — |
| RA_OUTSOURCER_CONTACT_ID | RcvShipmentReceiptHeaderPEORaOutsourcerContactId | — |
| RA_OUTSOURCER_PARTY_ID | RcvShipmentReceiptHeaderPEORaOutsourcerPartyId | — |
| RECEIPT_ADVICE_NUMBER | RcvShipmentReceiptHeaderPEOReceiptAdviceNumber | — |
| RECEIPT_NUM | RcvShipmentReceiptHeaderPEOReceiptNum | ✅ |
| RECEIPT_SOURCE_CODE | RcvShipmentReceiptHeaderPEOReceiptSourceCode | — |
| REMIT_TO_SITE_ID | RcvShipmentReceiptHeaderPEORemitToSiteId | — |
| REQUEST_DATE | RcvShipmentReceiptHeaderPEORequestDate | — |
| REQUEST_ID | RcvShipmentReceiptHeaderPEORequestId | — |
| RMA_BU_ID | RcvShipmentReceiptHeaderPEORmaBuId | — |
| SHIP_FROM_LOCATION_ID | RcvShipmentReceiptHeaderPEOShipFromLocationId | — |
| SHIP_TO_LOCATION_ID | RcvShipmentReceiptHeaderPEOShipToLocationId | — |
| SHIP_TO_ORG_ID | RcvShipmentReceiptHeaderPEOShipToOrgId | — |
| SHIPMENT_HEADER_ID | RcvShipmentReceiptHeaderPEOShipmentHeaderId | ✅ |
| SHIPMENT_NUM | RcvShipmentReceiptHeaderPEOShipmentNum | ✅ |
| SHIPPED_DATE | RcvShipmentReceiptHeaderPEOShippedDate | — |
| SPECIAL_HANDLING_CODE | RcvShipmentReceiptHeaderPEOSpecialHandlingCode | — |
| TAR_WEIGHT | RcvShipmentReceiptHeaderPEOTarWeight | — |
| TAR_WEIGHT_UOM_CODE | RcvShipmentReceiptHeaderPEOTarWeightUomCode | — |
| TAX_AMOUNT | RcvShipmentReceiptHeaderPEOTaxAmount | — |
| TAX_NAME | RcvShipmentReceiptHeaderPEOTaxName | — |
| VENDOR_ID | RcvShipmentReceiptHeaderPEOVendorId | — |
| VENDOR_SITE_ID | RcvShipmentReceiptHeaderPEOVendorSiteId | — |
| WAYBILL_AIRBILL_NUM | RcvShipmentReceiptHeaderPEOWaybillAirbillNum | — |

### [[prepaymentappliationdistributionpvo|PrepaymentAppliationDistributionPVO]] (AP · BICC: 4/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LAST_UPDATE_DATE | RcvShipHeaderInvDistLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | RcvShipHeaderInvLineLastUpdateDate | ✅ |
| RA_DOC_LAST_UPDATE_DATE | RcvShipHeaderInvDistRaDocLastUpdateDate | ✅ |
| RA_DOC_LAST_UPDATE_DATE | RcvShipHeaderInvLineRaDocLastUpdateDate | ✅ |
| SHIPMENT_HEADER_ID | RcvShipHeaderInvDistShipmentHeaderId | — |
| SHIPMENT_HEADER_ID | RcvShipHeaderInvLineShipmentHeaderId | — |

### [[receiptaccountingtxnp1|ReceiptAccountingTxnP1]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPROVAL_STATUS | RcvShipmentHeadersApprovalStatus1 | — |
| ASN_STATUS | RcvShipmentHeadersAsnStatus | — |
| ASN_TYPE | RcvShipmentHeadersAsnType | — |
| ATTRIBUTE1 | RcvShipmentHeadersAttribute120 | — |
| ATTRIBUTE10 | RcvShipmentHeadersAttribute106 | — |
| ATTRIBUTE11 | RcvShipmentHeadersAttribute1110 | — |
| ATTRIBUTE12 | RcvShipmentHeadersAttribute126 | — |
| ATTRIBUTE13 | RcvShipmentHeadersAttribute136 | — |
| ATTRIBUTE14 | RcvShipmentHeadersAttribute146 | — |
| ATTRIBUTE15 | RcvShipmentHeadersAttribute156 | — |
| ATTRIBUTE16 | RcvShipmentHeadersAttribute166 | — |
| ATTRIBUTE17 | RcvShipmentHeadersAttribute176 | — |
| ATTRIBUTE18 | RcvShipmentHeadersAttribute186 | — |
| ATTRIBUTE19 | RcvShipmentHeadersAttribute196 | — |
| ATTRIBUTE2 | RcvShipmentHeadersAttribute26 | — |
| ATTRIBUTE20 | RcvShipmentHeadersAttribute206 | — |
| ATTRIBUTE3 | RcvShipmentHeadersAttribute36 | — |
| ATTRIBUTE4 | RcvShipmentHeadersAttribute46 | — |
| ATTRIBUTE5 | RcvShipmentHeadersAttribute56 | — |
| ATTRIBUTE6 | RcvShipmentHeadersAttribute66 | — |
| ATTRIBUTE7 | RcvShipmentHeadersAttribute76 | — |
| ATTRIBUTE8 | RcvShipmentHeadersAttribute86 | — |
| ATTRIBUTE9 | RcvShipmentHeadersAttribute96 | — |
| ATTRIBUTE_CATEGORY | RcvShipmentHeadersAttributeCategory6 | — |
| ATTRIBUTE_DATE1 | RcvShipmentHeadersAttributeDate16 | — |
| ATTRIBUTE_DATE2 | RcvShipmentHeadersAttributeDate26 | — |
| ATTRIBUTE_DATE3 | RcvShipmentHeadersAttributeDate36 | — |
| ATTRIBUTE_DATE4 | RcvShipmentHeadersAttributeDate46 | — |
| ATTRIBUTE_DATE5 | RcvShipmentHeadersAttributeDate56 | — |
| ATTRIBUTE_NUMBER1 | RcvShipmentHeadersAttributeNumber16 | — |
| ATTRIBUTE_NUMBER10 | RcvShipmentHeadersAttributeNumber106 | — |
| ATTRIBUTE_NUMBER2 | RcvShipmentHeadersAttributeNumber26 | — |
| ATTRIBUTE_NUMBER3 | RcvShipmentHeadersAttributeNumber36 | — |
| ATTRIBUTE_NUMBER4 | RcvShipmentHeadersAttributeNumber46 | — |
| ATTRIBUTE_NUMBER5 | RcvShipmentHeadersAttributeNumber56 | — |
| ATTRIBUTE_NUMBER6 | RcvShipmentHeadersAttributeNumber66 | — |
| ATTRIBUTE_NUMBER7 | RcvShipmentHeadersAttributeNumber76 | — |
| ATTRIBUTE_NUMBER8 | RcvShipmentHeadersAttributeNumber86 | — |
| ATTRIBUTE_NUMBER9 | RcvShipmentHeadersAttributeNumber96 | — |
| ATTRIBUTE_TIMESTAMP1 | RcvShipmentHeadersAttributeTimestamp16 | — |
| ATTRIBUTE_TIMESTAMP2 | RcvShipmentHeadersAttributeTimestamp26 | — |
| ATTRIBUTE_TIMESTAMP3 | RcvShipmentHeadersAttributeTimestamp36 | — |
| ATTRIBUTE_TIMESTAMP4 | RcvShipmentHeadersAttributeTimestamp46 | — |
| ATTRIBUTE_TIMESTAMP5 | RcvShipmentHeadersAttributeTimestamp56 | — |
| BILL_OF_LADING | RcvShipmentHeadersBillOfLading | — |
| CARRIER_EQUIPMENT | RcvShipmentHeadersCarrierEquipment | — |
| CARRIER_METHOD | RcvShipmentHeadersCarrierMethod | — |
| COMMENTS | RcvShipmentHeadersComments3 | — |
| CONVERSION_DATE | RcvShipmentHeadersConversionDate | — |
| CONVERSION_RATE | RcvShipmentHeadersConversionRate | — |
| CONVERSION_RATE_TYPE | RcvShipmentHeadersConversionRateType | — |
| CREATED_BY | RcvShipmentHeadersCreatedBy9 | — |
| CREATION_DATE | RcvShipmentHeadersCreationDate9 | — |
| CURRENCY_CODE | RcvShipmentHeadersCurrencyCode5 | — |
| CUSTOMER_ID | RcvShipmentHeadersCustomerId2 | — |
| CUSTOMER_SITE_ID | RcvShipmentHeadersCustomerSiteId2 | — |
| EDI_CONTROL_NUM | RcvShipmentHeadersEdiControlNum | — |
| EMPLOYEE_ID | RcvShipmentHeadersEmployeeId2 | — |
| EXPECTED_RECEIPT_DATE | RcvShipmentHeadersExpectedReceiptDate | — |
| FREIGHT_AMOUNT | RcvShipmentHeadersFreightAmount | — |
| FREIGHT_BILL_NUMBER | RcvShipmentHeadersFreightBillNumber | — |
| FREIGHT_CARRIER_ID | RcvShipmentHeadersFreightCarrierId | — |
| FREIGHT_TERMS | RcvShipmentHeadersFreightTerms | — |
| GOVERNMENT_CONTEXT | RcvShipmentHeadersGovernmentContext5 | — |
| GROSS_WEIGHT | RcvShipmentHeadersGrossWeight | — |
| GROSS_WEIGHT_UOM_CODE | RcvShipmentHeadersGrossWeightUomCode | — |
| HAZARD_CLASS | RcvShipmentHeadersHazardClass | — |
| HAZARD_CODE | RcvShipmentHeadersHazardCode | — |
| HAZARD_DESCRIPTION | RcvShipmentHeadersHazardDescription | — |
| HEADER_INTERFACE_ID | RcvShipmentHeadersHeaderInterfaceId | — |
| INVOICE_AMOUNT | RcvShipmentHeadersInvoiceAmount | — |
| INVOICE_DATE | RcvShipmentHeadersInvoiceDate | — |
| INVOICE_NUM | RcvShipmentHeadersInvoiceNum | — |
| INVOICE_STATUS_CODE | RcvShipmentHeadersInvoiceStatusCode2 | — |
| JOB_DEFINITION_NAME | RcvShipmentHeadersJobDefinitionName9 | — |
| JOB_DEFINITION_PACKAGE | RcvShipmentHeadersJobDefinitionPackage9 | — |
| LAST_UPDATE_DATE | RcvShipmentHeadersLastUpdateDate9 | — |
| LAST_UPDATE_LOGIN | RcvShipmentHeadersLastUpdateLogin9 | — |
| LAST_UPDATED_BY | RcvShipmentHeadersLastUpdatedBy9 | — |
| LSP_FLAG | RcvShipmentHeadersLspFlag | — |
| NET_WEIGHT | RcvShipmentHeadersNetWeight | — |
| NET_WEIGHT_UOM_CODE | RcvShipmentHeadersNetWeightUomCode | — |
| NOTICE_CREATION_DATE | RcvShipmentHeadersNoticeCreationDate | — |
| NUM_OF_CONTAINERS | RcvShipmentHeadersNumOfContainers | — |
| OBJECT_VERSION_NUMBER | RcvShipmentHeadersObjectVersionNumber6 | — |
| ORGANIZATION_ID | RcvShipmentHeadersOrganizationId1 | — |
| PACKAGING_CODE | RcvShipmentHeadersPackagingCode | — |
| PACKING_SLIP | RcvShipmentHeadersPackingSlip1 | — |
| PAYMENT_TERMS_ID | RcvShipmentHeadersPaymentTermsId | — |
| PERFORMANCE_PERIOD_FROM | RcvShipmentHeadersPerformancePeriodFrom | — |
| PERFORMANCE_PERIOD_TO | RcvShipmentHeadersPerformancePeriodTo | — |
| RA_DOC_CREATION_DATE | RcvShipmentHeadersRaDocCreationDate | — |
| RA_DOC_LAST_UPDATE_DATE | RcvShipmentHeadersRaDocLastUpdateDate | — |
| RA_DOC_REVISION_DATE | RcvShipmentHeadersRaDocRevisionDate | — |
| RA_DOC_REVISION_NUMBER | RcvShipmentHeadersRaDocRevisionNumber | — |
| RA_DOCUMENT_CODE | RcvShipmentHeadersRaDocumentCode | — |
| RA_DOCUMENT_NUMBER | RcvShipmentHeadersRaDocumentNumber | — |
| RA_DOO_SOURCE_SYSTEM_ID | RcvShipmentHeadersRaDooSourceSystemId | — |
| RA_NOTE_TO_RECEIVER | RcvShipmentHeadersRaNoteToReceiver1 | — |
| RA_ORIG_SYSTEM_REF | RcvShipmentHeadersRaOrigSystemRef | — |
| RA_OUTSOURCER_CONTACT_ID | RcvShipmentHeadersRaOutsourcerContactId | — |
| RA_OUTSOURCER_PARTY_ID | RcvShipmentHeadersRaOutsourcerPartyId | — |
| RECEIPT_ADVICE_NUMBER | RcvShipmentHeadersReceiptAdviceNumber | — |
| RECEIPT_NUM | RcvShipmentHeadersReceiptNum | — |
| RECEIPT_SOURCE_CODE | RcvShipmentHeadersReceiptSourceCode | — |
| REMIT_TO_SITE_ID | RcvShipmentHeadersRemitToSiteId | — |
| REQUEST_DATE | RcvShipmentHeadersRequestDate | — |
| REQUEST_ID | RcvShipmentHeadersRequestId9 | — |
| RMA_BU_ID | RcvShipmentHeadersRmaBuId | — |
| SHIP_FROM_LOCATION_ID | RcvShipmentHeadersShipFromLocationId2 | — |
| SHIP_TO_LOCATION_ID | RcvShipmentHeadersShipToLocationId3 | — |
| SHIP_TO_ORG_ID | RcvShipmentHeadersShipToOrgId | — |
| SHIPMENT_HEADER_ID | RcvShipmentHeadersShipmentHeaderId2 | — |
| SHIPMENT_NUM | RcvShipmentHeadersShipmentNum1 | — |
| SHIPPED_DATE | RcvShipmentHeadersShippedDate | — |
| SPECIAL_HANDLING_CODE | RcvShipmentHeadersSpecialHandlingCode | — |
| TAR_WEIGHT | RcvShipmentHeadersTarWeight | — |
| TAR_WEIGHT_UOM_CODE | RcvShipmentHeadersTarWeightUomCode | — |
| TAX_AMOUNT | RcvShipmentHeadersTaxAmount1 | — |
| TAX_NAME | RcvShipmentHeadersTaxName3 | — |
| VENDOR_ID | RcvShipmentHeadersVendorId3 | — |
| VENDOR_SITE_ID | RcvShipmentHeadersVendorSiteId3 | — |
| WAYBILL_AIRBILL_NUM | RcvShipmentHeadersWaybillAirbillNum | — |

### [[receiptaccountingtxnrefpvo|ReceiptAccountingTxnRefPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPROVAL_STATUS | RcvShipmentHeadersApprovalStatus1 | — |
| ASN_STATUS | RcvShipmentHeadersAsnStatus | — |
| ASN_TYPE | RcvShipmentHeadersAsnType | — |
| ATTRIBUTE1 | RcvShipmentHeadersAttribute120 | — |
| ATTRIBUTE10 | RcvShipmentHeadersAttribute106 | — |
| ATTRIBUTE11 | RcvShipmentHeadersAttribute1110 | — |
| ATTRIBUTE12 | RcvShipmentHeadersAttribute126 | — |
| ATTRIBUTE13 | RcvShipmentHeadersAttribute136 | — |
| ATTRIBUTE14 | RcvShipmentHeadersAttribute146 | — |
| ATTRIBUTE15 | RcvShipmentHeadersAttribute156 | — |
| ATTRIBUTE16 | RcvShipmentHeadersAttribute166 | — |
| ATTRIBUTE17 | RcvShipmentHeadersAttribute176 | — |
| ATTRIBUTE18 | RcvShipmentHeadersAttribute186 | — |
| ATTRIBUTE19 | RcvShipmentHeadersAttribute196 | — |
| ATTRIBUTE2 | RcvShipmentHeadersAttribute26 | — |
| ATTRIBUTE20 | RcvShipmentHeadersAttribute206 | — |
| ATTRIBUTE3 | RcvShipmentHeadersAttribute36 | — |
| ATTRIBUTE4 | RcvShipmentHeadersAttribute46 | — |
| ATTRIBUTE5 | RcvShipmentHeadersAttribute56 | — |
| ATTRIBUTE6 | RcvShipmentHeadersAttribute66 | — |
| ATTRIBUTE7 | RcvShipmentHeadersAttribute76 | — |
| ATTRIBUTE8 | RcvShipmentHeadersAttribute86 | — |
| ATTRIBUTE9 | RcvShipmentHeadersAttribute96 | — |
| ATTRIBUTE_CATEGORY | RcvShipmentHeadersAttributeCategory6 | — |
| ATTRIBUTE_DATE1 | RcvShipmentHeadersAttributeDate16 | — |
| ATTRIBUTE_DATE2 | RcvShipmentHeadersAttributeDate26 | — |
| ATTRIBUTE_DATE3 | RcvShipmentHeadersAttributeDate36 | — |
| ATTRIBUTE_DATE4 | RcvShipmentHeadersAttributeDate46 | — |
| ATTRIBUTE_DATE5 | RcvShipmentHeadersAttributeDate56 | — |
| ATTRIBUTE_NUMBER1 | RcvShipmentHeadersAttributeNumber16 | — |
| ATTRIBUTE_NUMBER10 | RcvShipmentHeadersAttributeNumber106 | — |
| ATTRIBUTE_NUMBER2 | RcvShipmentHeadersAttributeNumber26 | — |
| ATTRIBUTE_NUMBER3 | RcvShipmentHeadersAttributeNumber36 | — |
| ATTRIBUTE_NUMBER4 | RcvShipmentHeadersAttributeNumber46 | — |
| ATTRIBUTE_NUMBER5 | RcvShipmentHeadersAttributeNumber56 | — |
| ATTRIBUTE_NUMBER6 | RcvShipmentHeadersAttributeNumber66 | — |
| ATTRIBUTE_NUMBER7 | RcvShipmentHeadersAttributeNumber76 | — |
| ATTRIBUTE_NUMBER8 | RcvShipmentHeadersAttributeNumber86 | — |
| ATTRIBUTE_NUMBER9 | RcvShipmentHeadersAttributeNumber96 | — |
| ATTRIBUTE_TIMESTAMP1 | RcvShipmentHeadersAttributeTimestamp16 | — |
| ATTRIBUTE_TIMESTAMP2 | RcvShipmentHeadersAttributeTimestamp26 | — |
| ATTRIBUTE_TIMESTAMP3 | RcvShipmentHeadersAttributeTimestamp36 | — |
| ATTRIBUTE_TIMESTAMP4 | RcvShipmentHeadersAttributeTimestamp46 | — |
| ATTRIBUTE_TIMESTAMP5 | RcvShipmentHeadersAttributeTimestamp56 | — |
| BILL_OF_LADING | RcvShipmentHeadersBillOfLading | — |
| CARRIER_EQUIPMENT | RcvShipmentHeadersCarrierEquipment | — |
| CARRIER_METHOD | RcvShipmentHeadersCarrierMethod | — |
| COMMENTS | RcvShipmentHeadersComments3 | — |
| CONVERSION_DATE | RcvShipmentHeadersConversionDate | — |
| CONVERSION_RATE | RcvShipmentHeadersConversionRate | — |
| CONVERSION_RATE_TYPE | RcvShipmentHeadersConversionRateType | — |
| CREATED_BY | RcvShipmentHeadersCreatedBy9 | — |
| CREATION_DATE | RcvShipmentHeadersCreationDate9 | — |
| CURRENCY_CODE | RcvShipmentHeadersCurrencyCode5 | — |
| CUSTOMER_ID | RcvShipmentHeadersCustomerId2 | — |
| CUSTOMER_SITE_ID | RcvShipmentHeadersCustomerSiteId2 | — |
| EDI_CONTROL_NUM | RcvShipmentHeadersEdiControlNum | — |
| EMPLOYEE_ID | RcvShipmentHeadersEmployeeId2 | — |
| EXPECTED_RECEIPT_DATE | RcvShipmentHeadersExpectedReceiptDate | — |
| FREIGHT_AMOUNT | RcvShipmentHeadersFreightAmount | — |
| FREIGHT_BILL_NUMBER | RcvShipmentHeadersFreightBillNumber | — |
| FREIGHT_CARRIER_ID | RcvShipmentHeadersFreightCarrierId | — |
| FREIGHT_TERMS | RcvShipmentHeadersFreightTerms | — |
| GOVERNMENT_CONTEXT | RcvShipmentHeadersGovernmentContext5 | — |
| GROSS_WEIGHT | RcvShipmentHeadersGrossWeight | — |
| GROSS_WEIGHT_UOM_CODE | RcvShipmentHeadersGrossWeightUomCode | — |
| HAZARD_CLASS | RcvShipmentHeadersHazardClass | — |
| HAZARD_CODE | RcvShipmentHeadersHazardCode | — |
| HAZARD_DESCRIPTION | RcvShipmentHeadersHazardDescription | — |
| HEADER_INTERFACE_ID | RcvShipmentHeadersHeaderInterfaceId | — |
| INVOICE_AMOUNT | RcvShipmentHeadersInvoiceAmount | — |
| INVOICE_DATE | RcvShipmentHeadersInvoiceDate | — |
| INVOICE_NUM | RcvShipmentHeadersInvoiceNum | — |
| INVOICE_STATUS_CODE | RcvShipmentHeadersInvoiceStatusCode2 | — |
| JOB_DEFINITION_NAME | RcvShipmentHeadersJobDefinitionName9 | — |
| JOB_DEFINITION_PACKAGE | RcvShipmentHeadersJobDefinitionPackage9 | — |
| LAST_UPDATE_DATE | RcvShipmentHeadersLastUpdateDate9 | — |
| LAST_UPDATE_LOGIN | RcvShipmentHeadersLastUpdateLogin9 | — |
| LAST_UPDATED_BY | RcvShipmentHeadersLastUpdatedBy9 | — |
| LSP_FLAG | RcvShipmentHeadersLspFlag | — |
| NET_WEIGHT | RcvShipmentHeadersNetWeight | — |
| NET_WEIGHT_UOM_CODE | RcvShipmentHeadersNetWeightUomCode | — |
| NOTICE_CREATION_DATE | RcvShipmentHeadersNoticeCreationDate | — |
| NUM_OF_CONTAINERS | RcvShipmentHeadersNumOfContainers | — |
| OBJECT_VERSION_NUMBER | RcvShipmentHeadersObjectVersionNumber6 | — |
| ORGANIZATION_ID | RcvShipmentHeadersOrganizationId1 | — |
| PACKAGING_CODE | RcvShipmentHeadersPackagingCode | — |
| PACKING_SLIP | RcvShipmentHeadersPackingSlip1 | — |
| PAYMENT_TERMS_ID | RcvShipmentHeadersPaymentTermsId | — |
| PERFORMANCE_PERIOD_FROM | RcvShipmentHeadersPerformancePeriodFrom | — |
| PERFORMANCE_PERIOD_TO | RcvShipmentHeadersPerformancePeriodTo | — |
| RA_DOC_CREATION_DATE | RcvShipmentHeadersRaDocCreationDate | — |
| RA_DOC_LAST_UPDATE_DATE | RcvShipmentHeadersRaDocLastUpdateDate | — |
| RA_DOC_REVISION_DATE | RcvShipmentHeadersRaDocRevisionDate | — |
| RA_DOC_REVISION_NUMBER | RcvShipmentHeadersRaDocRevisionNumber | — |
| RA_DOCUMENT_CODE | RcvShipmentHeadersRaDocumentCode | — |
| RA_DOCUMENT_NUMBER | RcvShipmentHeadersRaDocumentNumber | — |
| RA_DOO_SOURCE_SYSTEM_ID | RcvShipmentHeadersRaDooSourceSystemId | — |
| RA_NOTE_TO_RECEIVER | RcvShipmentHeadersRaNoteToReceiver1 | — |
| RA_ORIG_SYSTEM_REF | RcvShipmentHeadersRaOrigSystemRef | — |
| RA_OUTSOURCER_CONTACT_ID | RcvShipmentHeadersRaOutsourcerContactId | — |
| RA_OUTSOURCER_PARTY_ID | RcvShipmentHeadersRaOutsourcerPartyId | — |
| RECEIPT_ADVICE_NUMBER | RcvShipmentHeadersReceiptAdviceNumber | — |
| RECEIPT_NUM | RcvShipmentHeadersReceiptNum | — |
| RECEIPT_SOURCE_CODE | RcvShipmentHeadersReceiptSourceCode | — |
| REMIT_TO_SITE_ID | RcvShipmentHeadersRemitToSiteId | — |
| REQUEST_DATE | RcvShipmentHeadersRequestDate | — |
| REQUEST_ID | RcvShipmentHeadersRequestId9 | — |
| RMA_BU_ID | RcvShipmentHeadersRmaBuId | — |
| SHIP_FROM_LOCATION_ID | RcvShipmentHeadersShipFromLocationId2 | — |
| SHIP_TO_LOCATION_ID | RcvShipmentHeadersShipToLocationId3 | — |
| SHIP_TO_ORG_ID | RcvShipmentHeadersShipToOrgId | — |
| SHIPMENT_HEADER_ID | RcvShipmentHeadersShipmentHeaderId2 | — |
| SHIPMENT_NUM | RcvShipmentHeadersShipmentNum1 | — |
| SHIPPED_DATE | RcvShipmentHeadersShippedDate | — |
| SPECIAL_HANDLING_CODE | RcvShipmentHeadersSpecialHandlingCode | — |
| TAR_WEIGHT | RcvShipmentHeadersTarWeight | — |
| TAR_WEIGHT_UOM_CODE | RcvShipmentHeadersTarWeightUomCode | — |
| TAX_AMOUNT | RcvShipmentHeadersTaxAmount1 | — |
| TAX_NAME | RcvShipmentHeadersTaxName3 | — |
| VENDOR_ID | RcvShipmentHeadersVendorId3 | — |
| VENDOR_SITE_ID | RcvShipmentHeadersVendorSiteId3 | — |
| WAYBILL_AIRBILL_NUM | RcvShipmentHeadersWaybillAirbillNum | — |

### [[receivinginboundshipmentheaderextractpvo|ReceivingInboundShipmentHeaderExtractPVO]] (OTHER · BICC: 78/118)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASN_TYPE | AsnType | ✅ |
| ATTRIBUTE1 | Attribute1 | — |
| ATTRIBUTE10 | Attribute10 | — |
| ATTRIBUTE11 | Attribute11 | — |
| ATTRIBUTE12 | Attribute12 | — |
| ATTRIBUTE13 | Attribute13 | — |
| ATTRIBUTE14 | Attribute14 | — |
| ATTRIBUTE15 | Attribute15 | — |
| ATTRIBUTE16 | Attribute16 | — |
| ATTRIBUTE17 | Attribute17 | — |
| ATTRIBUTE18 | Attribute18 | — |
| ATTRIBUTE19 | Attribute19 | — |
| ATTRIBUTE2 | Attribute2 | — |
| ATTRIBUTE20 | Attribute20 | — |
| ATTRIBUTE3 | Attribute3 | — |
| ATTRIBUTE4 | Attribute4 | — |
| ATTRIBUTE5 | Attribute5 | — |
| ATTRIBUTE6 | Attribute6 | — |
| ATTRIBUTE7 | Attribute7 | — |
| ATTRIBUTE8 | Attribute8 | — |
| ATTRIBUTE9 | Attribute9 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory | ✅ |
| ATTRIBUTE_DATE1 | AttributeDate1 | — |
| ATTRIBUTE_DATE2 | AttributeDate2 | — |
| ATTRIBUTE_DATE3 | AttributeDate3 | — |
| ATTRIBUTE_DATE4 | AttributeDate4 | — |
| ATTRIBUTE_DATE5 | AttributeDate5 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber10 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber2 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber9 | — |
| ATTRIBUTE_TIMESTAMP1 | AttributeTimestamp1 | — |
| ATTRIBUTE_TIMESTAMP2 | AttributeTimestamp2 | — |
| ATTRIBUTE_TIMESTAMP3 | AttributeTimestamp3 | — |
| ATTRIBUTE_TIMESTAMP4 | AttributeTimestamp4 | — |
| ATTRIBUTE_TIMESTAMP5 | AttributeTimestamp5 | — |
| BILL_OF_LADING | BillOfLading | ✅ |
| CARRIER_EQUIPMENT | CarrierEquipment | ✅ |
| CARRIER_METHOD | CarrierMethod | ✅ |
| COMMENTS | Comments | ✅ |
| CONVERSION_DATE | ConversionDate | ✅ |
| CONVERSION_RATE | ConversionRate | ✅ |
| CONVERSION_RATE_TYPE | ConversionRateType | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| CURRENCY_CODE | CurrencyCode | ✅ |
| CUSTOMER_ID | CustomerId | ✅ |
| CUSTOMER_SITE_ID | CustomerSiteId | ✅ |
| EDI_CONTROL_NUM | EdiControlNum | ✅ |
| EMPLOYEE_ID | EmployeeId | ✅ |
| EXPECTED_RECEIPT_DATE | ExpectedReceiptDate | ✅ |
| FREIGHT_AMOUNT | FreightAmount | ✅ |
| FREIGHT_BILL_NUMBER | FreightBillNumber | ✅ |
| FREIGHT_CARRIER_ID | FreightCarrierId | ✅ |
| FREIGHT_TERMS | FreightTerms | ✅ |
| GOVERNMENT_CONTEXT | GovernmentContext | ✅ |
| GROSS_WEIGHT | GrossWeight | ✅ |
| GROSS_WEIGHT_UOM_CODE | GrossWeightUomCode | ✅ |
| HAZARD_CLASS | HazardClass | ✅ |
| HAZARD_CODE | HazardCode | ✅ |
| HAZARD_DESCRIPTION | HazardDescription | ✅ |
| HEADER_INTERFACE_ID | HeaderInterfaceId | ✅ |
| INVOICE_AMOUNT | InvoiceAmount | ✅ |
| INVOICE_DATE | InvoiceDate | ✅ |
| INVOICE_NUM | InvoiceNum | ✅ |
| INVOICE_STATUS_CODE | InvoiceStatusCode | ✅ |
| JOB_DEFINITION_NAME | JobDefinitionName | ✅ |
| JOB_DEFINITION_PACKAGE | JobDefinitionPackage | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LSP_FLAG | LspFlag | ✅ |
| NET_WEIGHT | NetWeight | ✅ |
| NET_WEIGHT_UOM_CODE | NetWeightUomCode | ✅ |
| NOTICE_CREATION_DATE | NoticeCreationDate | ✅ |
| NUM_OF_CONTAINERS | NumOfContainers | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| ORGANIZATION_ID | OrganizationId | ✅ |
| PACKAGING_CODE | PackagingCode | ✅ |
| PACKING_SLIP | PackingSlip | ✅ |
| PAYMENT_TERMS_ID | PaymentTermsId | ✅ |
| RA_DOC_CREATION_DATE | RaDocCreationDate | ✅ |
| RA_DOC_LAST_UPDATE_DATE | RaDocLastUpdateDate | ✅ |
| RA_DOC_REVISION_DATE | RaDocRevisionDate | ✅ |
| RA_DOC_REVISION_NUMBER | RaDocRevisionNumber | ✅ |
| RA_DOCUMENT_CODE | RaDocumentCode | ✅ |
| RA_DOCUMENT_NUMBER | RaDocumentNumber | ✅ |
| RA_DOO_SOURCE_SYSTEM_ID | RaDooSourceSystemId | ✅ |
| RA_NOTE_TO_RECEIVER | RaNoteToReceiver | ✅ |
| RA_ORIG_SYSTEM_REF | RaOrigSystemRef | ✅ |
| RA_OUTSOURCER_CONTACT_ID | RaOutsourcerContactId | ✅ |
| RA_OUTSOURCER_PARTY_ID | RaOutsourcerPartyId | ✅ |
| RECEIPT_ADVICE_NUMBER | ReceiptAdviceNumber | ✅ |
| RECEIPT_NUM | ReceiptNum | ✅ |
| RECEIPT_SOURCE_CODE | ReceiptSourceCode | ✅ |
| REMIT_TO_SITE_ID | RemitToSiteId | ✅ |
| REQUEST_ID | RequestId | ✅ |
| RMA_BU_ID | RmaBuId | ✅ |
| SHIP_FROM_LOCATION_ID | ShipFromLocationId | ✅ |
| SHIP_TO_LOCATION_ID | ShipToLocationId | ✅ |
| SHIP_TO_ORG_ID | ShipToOrgId | ✅ |
| SHIPMENT_HEADER_ID | ShipmentHeaderId | ✅ |
| SHIPMENT_NUM | ShipmentNum | ✅ |
| SHIPPED_DATE | ShippedDate | ✅ |
| SPECIAL_HANDLING_CODE | SpecialHandlingCode | ✅ |
| TAR_WEIGHT | TarWeight | ✅ |
| TAR_WEIGHT_UOM_CODE | TarWeightUomCode | ✅ |
| TAX_AMOUNT | TaxAmount | ✅ |
| TAX_NAME | TaxName | ✅ |
| VENDOR_ID | VendorId | ✅ |
| VENDOR_SITE_ID | VendorSiteId | ✅ |
| WAYBILL_AIRBILL_NUM | WaybillAirbillNum | ✅ |

### [[receivingintransitshipmentspvo|ReceivingIntransitShipmentsPVO]] (AR · BICC: 11/81)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPROVAL_STATUS | RcvShipmentHeadersPEOApprovalStatus | — |
| ASN_STATUS | RcvShipmentHeadersPEOAsnStatus | — |
| ASN_TYPE | RcvShipmentHeadersPEOAsnType | — |
| ATTRIBUTE_CATEGORY | RcvShipmentHeadersPEOAttributeCategory | — |
| BILL_OF_LADING | RcvShipmentHeadersPEOBillOfLading | ✅ |
| CARRIER_EQUIPMENT | RcvShipmentHeadersPEOCarrierEquipment | — |
| CARRIER_METHOD | RcvShipmentHeadersPEOCarrierMethod | — |
| COMMENTS | RcvShipmentHeadersPEOComments | — |
| CONVERSION_DATE | RcvShipmentHeadersPEOConversionDate | — |
| CONVERSION_RATE | RcvShipmentHeadersPEOConversionRate | — |
| CONVERSION_RATE_TYPE | RcvShipmentHeadersPEOConversionRateType | — |
| CREATED_BY | RcvShipmentHeadersPEOCreatedBy | — |
| CREATION_DATE | RcvShipmentHeadersPEOCreationDate | — |
| CURRENCY_CODE | RcvShipmentHeadersPEOCurrencyCode | — |
| CUSTOMER_ID | RcvShipmentHeadersPEOCustomerId | — |
| CUSTOMER_SITE_ID | RcvShipmentHeadersPEOCustomerSiteId | — |
| EDI_CONTROL_NUM | RcvShipmentHeadersPEOEdiControlNum | — |
| EMPLOYEE_ID | RcvShipmentHeadersPEOEmployeeId | — |
| EXPECTED_RECEIPT_DATE | RcvShipmentHeadersPEOExpectedReceiptDate | ✅ |
| FREIGHT_AMOUNT | RcvShipmentHeadersPEOFreightAmount | — |
| FREIGHT_BILL_NUMBER | RcvShipmentHeadersPEOFreightBillNumber | — |
| FREIGHT_CARRIER_ID | RcvShipmentHeadersPEOFreightCarrierId | — |
| FREIGHT_TERMS | RcvShipmentHeadersPEOFreightTerms | — |
| GOVERNMENT_CONTEXT | RcvShipmentHeadersPEOGovernmentContext | — |
| GROSS_WEIGHT | RcvShipmentHeadersPEOGrossWeight | — |
| GROSS_WEIGHT_UOM_CODE | RcvShipmentHeadersPEOGrossWeightUomCode | — |
| HAZARD_CLASS | RcvShipmentHeadersPEOHazardClass | ✅ |
| HAZARD_CODE | RcvShipmentHeadersPEOHazardCode | — |
| HAZARD_DESCRIPTION | RcvShipmentHeadersPEOHazardDescription | — |
| INVOICE_AMOUNT | RcvShipmentHeadersPEOInvoiceAmount | — |
| INVOICE_DATE | RcvShipmentHeadersPEOInvoiceDate | — |
| INVOICE_NUM | RcvShipmentHeadersPEOInvoiceNum | — |
| INVOICE_STATUS_CODE | RcvShipmentHeadersPEOInvoiceStatusCode | ✅ |
| JOB_DEFINITION_NAME | RcvShipmentHeadersPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | RcvShipmentHeadersPEOJobDefinitionPackage | — |
| LAST_UPDATE_DATE | RcvShipmentHeadersPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RcvShipmentHeadersPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | RcvShipmentHeadersPEOLastUpdatedBy | — |
| LSP_FLAG | RcvShipmentHeadersPEOLspFlag | — |
| NET_WEIGHT | RcvShipmentHeadersPEONetWeight | — |
| NET_WEIGHT_UOM_CODE | RcvShipmentHeadersPEONetWeightUomCode | — |
| NOTICE_CREATION_DATE | RcvShipmentHeadersPEONoticeCreationDate | — |
| NUM_OF_CONTAINERS | RcvShipmentHeadersPEONumOfContainers | — |
| OBJECT_VERSION_NUMBER | RcvShipmentHeadersPEOObjectVersionNumber | — |
| ORGANIZATION_ID | RcvShipmentHeadersPEOOrganizationId | — |
| PACKAGING_CODE | RcvShipmentHeadersPEOPackagingCode | — |
| PACKING_SLIP | RcvShipmentHeadersPEOPackingSlip | — |
| PAYMENT_TERMS_ID | RcvShipmentHeadersPEOPaymentTermsId | — |
| PERFORMANCE_PERIOD_FROM | RcvShipmentHeadersPEOPerformancePeriodFrom | — |
| PERFORMANCE_PERIOD_TO | RcvShipmentHeadersPEOPerformancePeriodTo | — |
| RA_DOC_CREATION_DATE | RcvShipmentHeadersPEORaDocCreationDate | — |
| RA_DOC_LAST_UPDATE_DATE | RcvShipmentHeadersPEORaDocLastUpdateDate | ✅ |
| RA_DOC_REVISION_DATE | RcvShipmentHeadersPEORaDocRevisionDate | — |
| RA_DOC_REVISION_NUMBER | RcvShipmentHeadersPEORaDocRevisionNumber | — |
| RA_DOCUMENT_CODE | RcvShipmentHeadersPEORaDocumentCode | — |
| RA_DOCUMENT_NUMBER | RcvShipmentHeadersPEORaDocumentNumber | — |
| RA_DOO_SOURCE_SYSTEM_ID | RcvShipmentHeadersPEORaDooSourceSystemId | — |
| RA_NOTE_TO_RECEIVER | RcvShipmentHeadersPEORaNoteToReceiver | — |
| RA_OUTSOURCER_CONTACT_ID | RcvShipmentHeadersPEORaOutsourcerContactId | — |
| RA_OUTSOURCER_PARTY_ID | RcvShipmentHeadersPEORaOutsourcerPartyId | — |
| RECEIPT_ADVICE_NUMBER | RcvShipmentHeadersPEOReceiptAdviceNumber | — |
| RECEIPT_NUM | RcvShipmentHeadersPEOReceiptNum | ✅ |
| RECEIPT_SOURCE_CODE | RcvShipmentHeadersPEOReceiptSourceCode | ✅ |
| REMIT_TO_SITE_ID | RcvShipmentHeadersPEORemitToSiteId | — |
| REQUEST_DATE | RcvShipmentHeadersPEORequestDate | — |
| REQUEST_ID | RcvShipmentHeadersPEORequestId | — |
| RMA_BU_ID | RcvShipmentHeadersPEORmaBuId | — |
| SHIP_FROM_LOCATION_ID | RcvShipmentHeadersPEOShipFromLocationId | — |
| SHIP_TO_LOCATION_ID | RcvShipmentHeadersPEOShipToLocationId | — |
| SHIP_TO_ORG_ID | RcvShipmentHeadersPEOShipToOrgId | — |
| SHIPMENT_HEADER_ID | RcvShipmentHeadersPEOShipmentHeaderId | — |
| SHIPMENT_NUM | RcvShipmentHeadersPEOShipmentNum | ✅ |
| SHIPPED_DATE | RcvShipmentHeadersPEOShippedDate | ✅ |
| SPECIAL_HANDLING_CODE | RcvShipmentHeadersPEOSpecialHandlingCode | — |
| TAR_WEIGHT | RcvShipmentHeadersPEOTarWeight | — |
| TAR_WEIGHT_UOM_CODE | RcvShipmentHeadersPEOTarWeightUomCode | — |
| TAX_AMOUNT | RcvShipmentHeadersPEOTaxAmount | — |
| TAX_NAME | RcvShipmentHeadersPEOTaxName | — |
| VENDOR_ID | RcvShipmentHeadersPEOVendorId | — |
| VENDOR_SITE_ID | RcvShipmentHeadersPEOVendorSiteId | — |
| WAYBILL_AIRBILL_NUM | RcvShipmentHeadersPEOWaybillAirbillNum | ✅ |

### [[receivingreceiptp2ptransactionpvo|ReceivingReceiptP2PTransactionPVO]] (AR · BICC: 6/123)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPROVAL_STATUS | RcvShipmentHeadersPEOApprovalStatus | — |
| ASN_STATUS | RcvShipmentHeadersPEOAsnStatus | — |
| ASN_TYPE | RcvShipmentHeadersPEOAsnType | — |
| ATTRIBUTE1 | RcvShipmentHeadersPEOAttribute1 | — |
| ATTRIBUTE10 | RcvShipmentHeadersPEOAttribute10 | — |
| ATTRIBUTE11 | RcvShipmentHeadersPEOAttribute11 | — |
| ATTRIBUTE12 | RcvShipmentHeadersPEOAttribute12 | — |
| ATTRIBUTE13 | RcvShipmentHeadersPEOAttribute13 | — |
| ATTRIBUTE14 | RcvShipmentHeadersPEOAttribute14 | — |
| ATTRIBUTE15 | RcvShipmentHeadersPEOAttribute15 | — |
| ATTRIBUTE16 | RcvShipmentHeadersPEOAttribute16 | — |
| ATTRIBUTE17 | RcvShipmentHeadersPEOAttribute17 | — |
| ATTRIBUTE18 | RcvShipmentHeadersPEOAttribute18 | — |
| ATTRIBUTE19 | RcvShipmentHeadersPEOAttribute19 | — |
| ATTRIBUTE2 | RcvShipmentHeadersPEOAttribute2 | — |
| ATTRIBUTE20 | RcvShipmentHeadersPEOAttribute20 | — |
| ATTRIBUTE3 | RcvShipmentHeadersPEOAttribute3 | — |
| ATTRIBUTE4 | RcvShipmentHeadersPEOAttribute4 | — |
| ATTRIBUTE5 | RcvShipmentHeadersPEOAttribute5 | — |
| ATTRIBUTE6 | RcvShipmentHeadersPEOAttribute6 | — |
| ATTRIBUTE7 | RcvShipmentHeadersPEOAttribute7 | — |
| ATTRIBUTE8 | RcvShipmentHeadersPEOAttribute8 | — |
| ATTRIBUTE9 | RcvShipmentHeadersPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | RcvShipmentHeadersPEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | RcvShipmentHeadersPEOAttributeDate1 | — |
| ATTRIBUTE_DATE2 | RcvShipmentHeadersPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | RcvShipmentHeadersPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | RcvShipmentHeadersPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | RcvShipmentHeadersPEOAttributeDate5 | — |
| ATTRIBUTE_NUMBER1 | RcvShipmentHeadersPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | RcvShipmentHeadersPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER2 | RcvShipmentHeadersPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER3 | RcvShipmentHeadersPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | RcvShipmentHeadersPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | RcvShipmentHeadersPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | RcvShipmentHeadersPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | RcvShipmentHeadersPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | RcvShipmentHeadersPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | RcvShipmentHeadersPEOAttributeNumber9 | — |
| ATTRIBUTE_TIMESTAMP1 | RcvShipmentHeadersPEOAttributeTimestamp1 | — |
| ATTRIBUTE_TIMESTAMP2 | RcvShipmentHeadersPEOAttributeTimestamp2 | — |
| ATTRIBUTE_TIMESTAMP3 | RcvShipmentHeadersPEOAttributeTimestamp3 | — |
| ATTRIBUTE_TIMESTAMP4 | RcvShipmentHeadersPEOAttributeTimestamp4 | — |
| ATTRIBUTE_TIMESTAMP5 | RcvShipmentHeadersPEOAttributeTimestamp5 | — |
| BILL_OF_LADING | RcvShipmentHeadersPEOBillOfLading | ✅ |
| CARRIER_EQUIPMENT | RcvShipmentHeadersPEOCarrierEquipment | — |
| CARRIER_METHOD | RcvShipmentHeadersPEOCarrierMethod | — |
| COMMENTS | RcvShipmentHeadersPEOComments | — |
| CONVERSION_DATE | RcvShipmentHeadersPEOConversionDate | — |
| CONVERSION_RATE | RcvShipmentHeadersPEOConversionRate | — |
| CONVERSION_RATE_TYPE | RcvShipmentHeadersPEOConversionRateType | — |
| CREATED_BY | RcvShipmentHeadersPEOCreatedBy | — |
| CREATION_DATE | RcvShipmentHeadersPEOCreationDate | ✅ |
| CURRENCY_CODE | RcvShipmentHeadersPEOCurrencyCode | — |
| CUSTOMER_ID | RcvShipmentHeadersPEOCustomerId | — |
| CUSTOMER_SITE_ID | RcvShipmentHeadersPEOCustomerSiteId | — |
| EDI_CONTROL_NUM | RcvShipmentHeadersPEOEdiControlNum | — |
| EMPLOYEE_ID | RcvShipmentHeadersPEOEmployeeId | — |
| EXPECTED_RECEIPT_DATE | RcvShipmentHeadersPEOExpectedReceiptDate | — |
| FREIGHT_AMOUNT | RcvShipmentHeadersPEOFreightAmount | — |
| FREIGHT_BILL_NUMBER | RcvShipmentHeadersPEOFreightBillNumber | — |
| FREIGHT_CARRIER_ID | RcvShipmentHeadersPEOFreightCarrierId | — |
| FREIGHT_TERMS | RcvShipmentHeadersPEOFreightTerms | — |
| GOVERNMENT_CONTEXT | RcvShipmentHeadersPEOGovernmentContext | — |
| GROSS_WEIGHT | RcvShipmentHeadersPEOGrossWeight | — |
| GROSS_WEIGHT_UOM_CODE | RcvShipmentHeadersPEOGrossWeightUomCode | — |
| HAZARD_CLASS | RcvShipmentHeadersPEOHazardClass | — |
| HAZARD_CODE | RcvShipmentHeadersPEOHazardCode | — |
| HAZARD_DESCRIPTION | RcvShipmentHeadersPEOHazardDescription | — |
| HEADER_INTERFACE_ID | RcvShipmentHeadersPEOHeaderInterfaceId | — |
| INVOICE_AMOUNT | RcvShipmentHeadersPEOInvoiceAmount | — |
| INVOICE_DATE | RcvShipmentHeadersPEOInvoiceDate | — |
| INVOICE_NUM | RcvShipmentHeadersPEOInvoiceNum | — |
| INVOICE_STATUS_CODE | RcvShipmentHeadersPEOInvoiceStatusCode | — |
| JOB_DEFINITION_NAME | RcvShipmentHeadersPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | RcvShipmentHeadersPEOJobDefinitionPackage | — |
| LAST_UPDATE_DATE | RcvShipmentHeadersPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | RcvShipmentHeadersPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | RcvShipmentHeadersPEOLastUpdatedBy | — |
| LSP_FLAG | RcvShipmentHeadersPEOLspFlag | — |
| NET_WEIGHT | RcvShipmentHeadersPEONetWeight | — |
| NET_WEIGHT_UOM_CODE | RcvShipmentHeadersPEONetWeightUomCode | — |
| NOTICE_CREATION_DATE | RcvShipmentHeadersPEONoticeCreationDate | — |
| NUM_OF_CONTAINERS | RcvShipmentHeadersPEONumOfContainers | — |
| OBJECT_VERSION_NUMBER | RcvShipmentHeadersPEOObjectVersionNumber | — |
| ORGANIZATION_ID | RcvShipmentHeadersPEOOrganizationId | — |
| PACKAGING_CODE | RcvShipmentHeadersPEOPackagingCode | — |
| PACKING_SLIP | RcvShipmentHeadersPEOPackingSlip | — |
| PAYMENT_TERMS_ID | RcvShipmentHeadersPEOPaymentTermsId | — |
| PERFORMANCE_PERIOD_FROM | RcvShipmentHeadersPEOPerformancePeriodFrom | — |
| PERFORMANCE_PERIOD_TO | RcvShipmentHeadersPEOPerformancePeriodTo | — |
| RA_DOC_CREATION_DATE | RcvShipmentHeadersPEORaDocCreationDate | — |
| RA_DOC_LAST_UPDATE_DATE | RcvShipmentHeadersPEORaDocLastUpdateDate | — |
| RA_DOC_REVISION_DATE | RcvShipmentHeadersPEORaDocRevisionDate | — |
| RA_DOC_REVISION_NUMBER | RcvShipmentHeadersPEORaDocRevisionNumber | — |
| RA_DOCUMENT_CODE | RcvShipmentHeadersPEORaDocumentCode | — |
| RA_DOCUMENT_NUMBER | RcvShipmentHeadersPEORaDocumentNumber | — |
| RA_DOO_SOURCE_SYSTEM_ID | RcvShipmentHeadersPEORaDooSourceSystemId | — |
| RA_NOTE_TO_RECEIVER | RcvShipmentHeadersPEORaNoteToReceiver | — |
| RA_ORIG_SYSTEM_REF | RcvShipmentHeadersPEORaOrigSystemRef | — |
| RA_OUTSOURCER_CONTACT_ID | RcvShipmentHeadersPEORaOutsourcerContactId | — |
| RA_OUTSOURCER_PARTY_ID | RcvShipmentHeadersPEORaOutsourcerPartyId | — |
| RECEIPT_ADVICE_NUMBER | RcvShipmentHeadersPEOReceiptAdviceNumber | — |
| RECEIPT_NUM | RcvShipmentHeadersPEOReceiptNum | ✅ |
| RECEIPT_SOURCE_CODE | RcvShipmentHeadersPEOReceiptSourceCode | — |
| REMIT_TO_SITE_ID | RcvShipmentHeadersPEORemitToSiteId | — |
| REQUEST_DATE | RcvShipmentHeadersPEORequestDate | — |
| REQUEST_ID | RcvShipmentHeadersPEORequestId | — |
| RMA_BU_ID | RcvShipmentHeadersPEORmaBuId | — |
| SHIP_FROM_LOCATION_ID | RcvShipmentHeadersPEOShipFromLocationId | — |
| SHIP_TO_LOCATION_ID | RcvShipmentHeadersPEOShipToLocationId | — |
| SHIP_TO_ORG_ID | RcvShipmentHeadersPEOShipToOrgId | — |
| SHIPMENT_HEADER_ID | RcvShipmentHeadersPEOShipmentHeaderId | — |
| SHIPMENT_NUM | RcvShipmentHeadersPEOShipmentNum | ✅ |
| SHIPPED_DATE | RcvShipmentHeadersPEOShippedDate | ✅ |
| SPECIAL_HANDLING_CODE | RcvShipmentHeadersPEOSpecialHandlingCode | — |
| TAR_WEIGHT | RcvShipmentHeadersPEOTarWeight | — |
| TAR_WEIGHT_UOM_CODE | RcvShipmentHeadersPEOTarWeightUomCode | — |
| TAX_AMOUNT | RcvShipmentHeadersPEOTaxAmount | — |
| TAX_NAME | RcvShipmentHeadersPEOTaxName | — |
| VENDOR_ID | RcvShipmentHeadersPEOVendorId | — |
| VENDOR_SITE_ID | RcvShipmentHeadersPEOVendorSiteId | — |
| WAYBILL_AIRBILL_NUM | RcvShipmentHeadersPEOWaybillAirbillNum | ✅ |

### [[receivingreceiptspvo|ReceivingReceiptsPVO]] (AR · BICC: 15/81)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPROVAL_STATUS | RcvShipmentHeadersPEOApprovalStatus | — |
| ASN_STATUS | RcvShipmentHeadersPEOAsnStatus | — |
| ASN_TYPE | RcvShipmentHeadersPEOAsnType | — |
| ATTRIBUTE_CATEGORY | RcvShipmentHeadersPEOAttributeCategory | — |
| BILL_OF_LADING | RcvShipmentHeadersPEOBillOfLading | ✅ |
| CARRIER_EQUIPMENT | RcvShipmentHeadersPEOCarrierEquipment | — |
| CARRIER_METHOD | RcvShipmentHeadersPEOCarrierMethod | — |
| COMMENTS | RcvShipmentHeadersPEOComments | ✅ |
| CONVERSION_DATE | RcvShipmentHeadersPEOConversionDate | — |
| CONVERSION_RATE | RcvShipmentHeadersPEOConversionRate | — |
| CONVERSION_RATE_TYPE | RcvShipmentHeadersPEOConversionRateType | — |
| CREATED_BY | RcvShipmentHeadersPEOCreatedBy | — |
| CREATION_DATE | RcvShipmentHeadersPEOCreationDate | ✅ |
| CURRENCY_CODE | RcvShipmentHeadersPEOCurrencyCode | — |
| CUSTOMER_ID | RcvShipmentHeadersPEOCustomerId | — |
| CUSTOMER_SITE_ID | RcvShipmentHeadersPEOCustomerSiteId | — |
| EDI_CONTROL_NUM | RcvShipmentHeadersPEOEdiControlNum | — |
| EMPLOYEE_ID | RcvShipmentHeadersPEOEmployeeId | — |
| EXPECTED_RECEIPT_DATE | RcvShipmentHeadersPEOExpectedReceiptDate | — |
| FREIGHT_AMOUNT | RcvShipmentHeadersPEOFreightAmount | — |
| FREIGHT_BILL_NUMBER | RcvShipmentHeadersPEOFreightBillNumber | — |
| FREIGHT_CARRIER_ID | RcvShipmentHeadersPEOFreightCarrierId | — |
| FREIGHT_TERMS | RcvShipmentHeadersPEOFreightTerms | — |
| GOVERNMENT_CONTEXT | RcvShipmentHeadersPEOGovernmentContext | — |
| GROSS_WEIGHT | RcvShipmentHeadersPEOGrossWeight | — |
| GROSS_WEIGHT_UOM_CODE | RcvShipmentHeadersPEOGrossWeightUomCode | — |
| HAZARD_CLASS | RcvShipmentHeadersPEOHazardClass | — |
| HAZARD_CODE | RcvShipmentHeadersPEOHazardCode | — |
| HAZARD_DESCRIPTION | RcvShipmentHeadersPEOHazardDescription | — |
| INVOICE_AMOUNT | RcvShipmentHeadersPEOInvoiceAmount | — |
| INVOICE_DATE | RcvShipmentHeadersPEOInvoiceDate | — |
| INVOICE_NUM | RcvShipmentHeadersPEOInvoiceNum | — |
| INVOICE_STATUS_CODE | RcvShipmentHeadersPEOInvoiceStatusCode | — |
| JOB_DEFINITION_NAME | RcvShipmentHeadersPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | RcvShipmentHeadersPEOJobDefinitionPackage | — |
| LAST_UPDATE_DATE | RcvShipmentHeadersPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RcvShipmentHeadersPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | RcvShipmentHeadersPEOLastUpdatedBy | — |
| LSP_FLAG | RcvShipmentHeadersPEOLspFlag | — |
| NET_WEIGHT | RcvShipmentHeadersPEONetWeight | ✅ |
| NET_WEIGHT_UOM_CODE | RcvShipmentHeadersPEONetWeightUomCode | ✅ |
| NOTICE_CREATION_DATE | RcvShipmentHeadersPEONoticeCreationDate | — |
| NUM_OF_CONTAINERS | RcvShipmentHeadersPEONumOfContainers | — |
| OBJECT_VERSION_NUMBER | RcvShipmentHeadersPEOObjectVersionNumber | — |
| ORGANIZATION_ID | RcvShipmentHeadersPEOOrganizationId | — |
| PACKAGING_CODE | RcvShipmentHeadersPEOPackagingCode | — |
| PACKING_SLIP | RcvShipmentHeadersPEOPackingSlip | ✅ |
| PAYMENT_TERMS_ID | RcvShipmentHeadersPEOPaymentTermsId | — |
| PERFORMANCE_PERIOD_FROM | RcvShipmentHeadersPEOPerformancePeriodFrom | — |
| PERFORMANCE_PERIOD_TO | RcvShipmentHeadersPEOPerformancePeriodTo | — |
| RA_DOC_CREATION_DATE | RcvShipmentHeadersPEORaDocCreationDate | — |
| RA_DOC_LAST_UPDATE_DATE | RcvShipmentHeadersPEORaDocLastUpdateDate | ✅ |
| RA_DOC_REVISION_DATE | RcvShipmentHeadersPEORaDocRevisionDate | — |
| RA_DOC_REVISION_NUMBER | RcvShipmentHeadersPEORaDocRevisionNumber | — |
| RA_DOCUMENT_CODE | RcvShipmentHeadersPEORaDocumentCode | — |
| RA_DOCUMENT_NUMBER | RcvShipmentHeadersPEORaDocumentNumber | — |
| RA_DOO_SOURCE_SYSTEM_ID | RcvShipmentHeadersPEORaDooSourceSystemId | — |
| RA_NOTE_TO_RECEIVER | RcvShipmentHeadersPEORaNoteToReceiver | — |
| RA_OUTSOURCER_CONTACT_ID | RcvShipmentHeadersPEORaOutsourcerContactId | — |
| RA_OUTSOURCER_PARTY_ID | RcvShipmentHeadersPEORaOutsourcerPartyId | — |
| RECEIPT_ADVICE_NUMBER | RcvShipmentHeadersPEOReceiptAdviceNumber | — |
| RECEIPT_NUM | RcvShipmentHeadersPEOReceiptNum | ✅ |
| RECEIPT_SOURCE_CODE | RcvShipmentHeadersPEOReceiptSourceCode | — |
| REMIT_TO_SITE_ID | RcvShipmentHeadersPEORemitToSiteId | — |
| REQUEST_DATE | RcvShipmentHeadersPEORequestDate | — |
| REQUEST_ID | RcvShipmentHeadersPEORequestId | — |
| RMA_BU_ID | RcvShipmentHeadersPEORmaBuId | — |
| SHIP_FROM_LOCATION_ID | RcvShipmentHeadersPEOShipFromLocationId | — |
| SHIP_TO_LOCATION_ID | RcvShipmentHeadersPEOShipToLocationId | — |
| SHIP_TO_ORG_ID | RcvShipmentHeadersPEOShipToOrgId | — |
| SHIPMENT_HEADER_ID | RcvShipmentHeadersPEOShipmentHeaderId | ✅ |
| SHIPMENT_NUM | RcvShipmentHeadersPEOShipmentNum | ✅ |
| SHIPPED_DATE | RcvShipmentHeadersPEOShippedDate | ✅ |
| SPECIAL_HANDLING_CODE | RcvShipmentHeadersPEOSpecialHandlingCode | — |
| TAR_WEIGHT | RcvShipmentHeadersPEOTarWeight | ✅ |
| TAR_WEIGHT_UOM_CODE | RcvShipmentHeadersPEOTarWeightUomCode | ✅ |
| TAX_AMOUNT | RcvShipmentHeadersPEOTaxAmount | — |
| TAX_NAME | RcvShipmentHeadersPEOTaxName | — |
| VENDOR_ID | RcvShipmentHeadersPEOVendorId | — |
| VENDOR_SITE_ID | RcvShipmentHeadersPEOVendorSiteId | — |
| WAYBILL_AIRBILL_NUM | RcvShipmentHeadersPEOWaybillAirbillNum | ✅ |

### [[receivingreceiptsrefpvo|ReceivingReceiptsRefPVO]] (AR · BICC: 11/81)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPROVAL_STATUS | RcvShipmentHeadersPEOApprovalStatus | — |
| ASN_STATUS | RcvShipmentHeadersPEOAsnStatus | — |
| ASN_TYPE | RcvShipmentHeadersPEOAsnType | — |
| ATTRIBUTE_CATEGORY | RcvShipmentHeadersPEOAttributeCategory | — |
| BILL_OF_LADING | RcvShipmentHeadersPEOBillOfLading | ✅ |
| CARRIER_EQUIPMENT | RcvShipmentHeadersPEOCarrierEquipment | — |
| CARRIER_METHOD | RcvShipmentHeadersPEOCarrierMethod | — |
| COMMENTS | RcvShipmentHeadersPEOComments | ✅ |
| CONVERSION_DATE | RcvShipmentHeadersPEOConversionDate | — |
| CONVERSION_RATE | RcvShipmentHeadersPEOConversionRate | — |
| CONVERSION_RATE_TYPE | RcvShipmentHeadersPEOConversionRateType | — |
| CREATED_BY | RcvShipmentHeadersPEOCreatedBy | — |
| CREATION_DATE | RcvShipmentHeadersPEOCreationDate | ✅ |
| CURRENCY_CODE | RcvShipmentHeadersPEOCurrencyCode | — |
| CUSTOMER_ID | RcvShipmentHeadersPEOCustomerId | — |
| CUSTOMER_SITE_ID | RcvShipmentHeadersPEOCustomerSiteId | — |
| EDI_CONTROL_NUM | RcvShipmentHeadersPEOEdiControlNum | — |
| EMPLOYEE_ID | RcvShipmentHeadersPEOEmployeeId | — |
| EXPECTED_RECEIPT_DATE | RcvShipmentHeadersPEOExpectedReceiptDate | — |
| FREIGHT_AMOUNT | RcvShipmentHeadersPEOFreightAmount | — |
| FREIGHT_BILL_NUMBER | RcvShipmentHeadersPEOFreightBillNumber | — |
| FREIGHT_CARRIER_ID | RcvShipmentHeadersPEOFreightCarrierId | — |
| FREIGHT_TERMS | RcvShipmentHeadersPEOFreightTerms | — |
| GOVERNMENT_CONTEXT | RcvShipmentHeadersPEOGovernmentContext | — |
| GROSS_WEIGHT | RcvShipmentHeadersPEOGrossWeight | — |
| GROSS_WEIGHT_UOM_CODE | RcvShipmentHeadersPEOGrossWeightUomCode | — |
| HAZARD_CLASS | RcvShipmentHeadersPEOHazardClass | — |
| HAZARD_CODE | RcvShipmentHeadersPEOHazardCode | — |
| HAZARD_DESCRIPTION | RcvShipmentHeadersPEOHazardDescription | — |
| INVOICE_AMOUNT | RcvShipmentHeadersPEOInvoiceAmount | — |
| INVOICE_DATE | RcvShipmentHeadersPEOInvoiceDate | — |
| INVOICE_NUM | RcvShipmentHeadersPEOInvoiceNum | — |
| INVOICE_STATUS_CODE | RcvShipmentHeadersPEOInvoiceStatusCode | — |
| JOB_DEFINITION_NAME | RcvShipmentHeadersPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | RcvShipmentHeadersPEOJobDefinitionPackage | — |
| LAST_UPDATE_DATE | RcvShipmentHeadersPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RcvShipmentHeadersPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | RcvShipmentHeadersPEOLastUpdatedBy | — |
| LSP_FLAG | RcvShipmentHeadersPEOLspFlag | — |
| NET_WEIGHT | RcvShipmentHeadersPEONetWeight | — |
| NET_WEIGHT_UOM_CODE | RcvShipmentHeadersPEONetWeightUomCode | — |
| NOTICE_CREATION_DATE | RcvShipmentHeadersPEONoticeCreationDate | — |
| NUM_OF_CONTAINERS | RcvShipmentHeadersPEONumOfContainers | — |
| OBJECT_VERSION_NUMBER | RcvShipmentHeadersPEOObjectVersionNumber | — |
| ORGANIZATION_ID | RcvShipmentHeadersPEOOrganizationId | — |
| PACKAGING_CODE | RcvShipmentHeadersPEOPackagingCode | — |
| PACKING_SLIP | RcvShipmentHeadersPEOPackingSlip | ✅ |
| PAYMENT_TERMS_ID | RcvShipmentHeadersPEOPaymentTermsId | — |
| PERFORMANCE_PERIOD_FROM | RcvShipmentHeadersPEOPerformancePeriodFrom | — |
| PERFORMANCE_PERIOD_TO | RcvShipmentHeadersPEOPerformancePeriodTo | — |
| RA_DOC_CREATION_DATE | RcvShipmentHeadersPEORaDocCreationDate | — |
| RA_DOC_LAST_UPDATE_DATE | RcvShipmentHeadersPEORaDocLastUpdateDate | ✅ |
| RA_DOC_REVISION_DATE | RcvShipmentHeadersPEORaDocRevisionDate | — |
| RA_DOC_REVISION_NUMBER | RcvShipmentHeadersPEORaDocRevisionNumber | — |
| RA_DOCUMENT_CODE | RcvShipmentHeadersPEORaDocumentCode | — |
| RA_DOCUMENT_NUMBER | RcvShipmentHeadersPEORaDocumentNumber | — |
| RA_DOO_SOURCE_SYSTEM_ID | RcvShipmentHeadersPEORaDooSourceSystemId | — |
| RA_NOTE_TO_RECEIVER | RcvShipmentHeadersPEORaNoteToReceiver | — |
| RA_OUTSOURCER_CONTACT_ID | RcvShipmentHeadersPEORaOutsourcerContactId | — |
| RA_OUTSOURCER_PARTY_ID | RcvShipmentHeadersPEORaOutsourcerPartyId | — |
| RECEIPT_ADVICE_NUMBER | RcvShipmentHeadersPEOReceiptAdviceNumber | — |
| RECEIPT_NUM | RcvShipmentHeadersPEOReceiptNum | ✅ |
| RECEIPT_SOURCE_CODE | RcvShipmentHeadersPEOReceiptSourceCode | — |
| REMIT_TO_SITE_ID | RcvShipmentHeadersPEORemitToSiteId | — |
| REQUEST_DATE | RcvShipmentHeadersPEORequestDate | — |
| REQUEST_ID | RcvShipmentHeadersPEORequestId | — |
| RMA_BU_ID | RcvShipmentHeadersPEORmaBuId | — |
| SHIP_FROM_LOCATION_ID | RcvShipmentHeadersPEOShipFromLocationId | — |
| SHIP_TO_LOCATION_ID | RcvShipmentHeadersPEOShipToLocationId | — |
| SHIP_TO_ORG_ID | RcvShipmentHeadersPEOShipToOrgId | — |
| SHIPMENT_HEADER_ID | RcvShipmentHeadersPEOShipmentHeaderId | ✅ |
| SHIPMENT_NUM | RcvShipmentHeadersPEOShipmentNum | ✅ |
| SHIPPED_DATE | RcvShipmentHeadersPEOShippedDate | ✅ |
| SPECIAL_HANDLING_CODE | RcvShipmentHeadersPEOSpecialHandlingCode | — |
| TAR_WEIGHT | RcvShipmentHeadersPEOTarWeight | — |
| TAR_WEIGHT_UOM_CODE | RcvShipmentHeadersPEOTarWeightUomCode | — |
| TAX_AMOUNT | RcvShipmentHeadersPEOTaxAmount | — |
| TAX_NAME | RcvShipmentHeadersPEOTaxName | — |
| VENDOR_ID | RcvShipmentHeadersPEOVendorId | — |
| VENDOR_SITE_ID | RcvShipmentHeadersPEOVendorSiteId | — |
| WAYBILL_AIRBILL_NUM | RcvShipmentHeadersPEOWaybillAirbillNum | ✅ |

### [[receivingreceipttransactionextractpvo|ReceivingReceiptTransactionExtractPVO]] (OTHER · BICC: 76/76)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASN_TYPE | RcvngShpmntReceiptHdrPEOAsnType | ✅ |
| ATTRIBUTE_CATEGORY | RcvngShpmntReceiptHdrPEOAttributeCategory | ✅ |
| BILL_OF_LADING | RcvngShpmntReceiptHdrPEOBillOfLading | ✅ |
| CARRIER_EQUIPMENT | RcvngShpmntReceiptHdrPEOCarrierEquipment | ✅ |
| CARRIER_METHOD | RcvngShpmntReceiptHdrPEOCarrierMethod | ✅ |
| COMMENTS | RcvngShpmntReceiptHdrPEOComments | ✅ |
| CONVERSION_DATE | RcvngShpmntReceiptHdrPEOConversionDate | ✅ |
| CONVERSION_RATE | RcvngShpmntReceiptHdrPEOConversionRate | ✅ |
| CONVERSION_RATE_TYPE | RcvngShpmntReceiptHdrPEOConversionRateType | ✅ |
| CREATED_BY | RcvngShpmntReceiptHdrPEOCreatedBy | ✅ |
| CREATION_DATE | RcvngShpmntReceiptHdrPEOCreationDate | ✅ |
| CURRENCY_CODE | RcvngShpmntReceiptHdrPEOCurrencyCode | ✅ |
| CUSTOMER_ID | RcvngShpmntReceiptHdrPEOCustomerId | ✅ |
| CUSTOMER_SITE_ID | RcvngShpmntReceiptHdrPEOCustomerSiteId | ✅ |
| EDI_CONTROL_NUM | RcvngShpmntReceiptHdrPEOEdiControlNum | ✅ |
| EMPLOYEE_ID | RcvngShpmntReceiptHdrPEOEmployeeId | ✅ |
| EXPECTED_RECEIPT_DATE | RcvngShpmntReceiptHdrPEOExpectedReceiptDate | ✅ |
| FREIGHT_AMOUNT | RcvngShpmntReceiptHdrPEOFreightAmount | ✅ |
| FREIGHT_BILL_NUMBER | RcvngShpmntReceiptHdrPEOFreightBillNumber | ✅ |
| FREIGHT_CARRIER_ID | RcvngShpmntReceiptHdrPEOFreightCarrierId | ✅ |
| FREIGHT_TERMS | RcvngShpmntReceiptHdrPEOFreightTerms | ✅ |
| GOVERNMENT_CONTEXT | RcvngShpmntReceiptHdrPEOGovernmentContext | ✅ |
| GROSS_WEIGHT | RcvngShpmntReceiptHdrPEOGrossWeight | ✅ |
| GROSS_WEIGHT_UOM_CODE | RcvngShpmntReceiptHdrPEOGrossWeightUomCode | ✅ |
| HAZARD_CLASS | RcvngShpmntReceiptHdrPEOHazardClass | ✅ |
| HAZARD_CODE | RcvngShpmntReceiptHdrPEOHazardCode | ✅ |
| HAZARD_DESCRIPTION | RcvngShpmntReceiptHdrPEOHazardDescription | ✅ |
| INVOICE_AMOUNT | RcvngShpmntReceiptHdrPEOInvoiceAmount | ✅ |
| INVOICE_DATE | RcvngShpmntReceiptHdrPEOInvoiceDate | ✅ |
| INVOICE_NUM | RcvngShpmntReceiptHdrPEOInvoiceNum | ✅ |
| INVOICE_STATUS_CODE | RcvngShpmntReceiptHdrPEOInvoiceStatusCode | ✅ |
| JOB_DEFINITION_NAME | RcvngShpmntReceiptHdrPEOJobDefinitionName | ✅ |
| JOB_DEFINITION_PACKAGE | RcvngShpmntReceiptHdrPEOJobDefinitionPackage | ✅ |
| LAST_UPDATE_DATE | RcvngShpmntReceiptHdrPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RcvngShpmntReceiptHdrPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | RcvngShpmntReceiptHdrPEOLastUpdatedBy | ✅ |
| LSP_FLAG | RcvngShpmntReceiptHdrPEOLspFlag | ✅ |
| NET_WEIGHT | RcvngShpmntReceiptHdrPEONetWeight | ✅ |
| NET_WEIGHT_UOM_CODE | RcvngShpmntReceiptHdrPEONetWeightUomCode | ✅ |
| NOTICE_CREATION_DATE | RcvngShpmntReceiptHdrPEONoticeCreationDate | ✅ |
| NUM_OF_CONTAINERS | RcvngShpmntReceiptHdrPEONumOfContainers | ✅ |
| OBJECT_VERSION_NUMBER | RcvngShpmntReceiptHdrPEOObjectVersionNumber | ✅ |
| ORGANIZATION_ID | RcvngShpmntReceiptHdrPEOOrganizationId | ✅ |
| PACKAGING_CODE | RcvngShpmntReceiptHdrPEOPackagingCode | ✅ |
| PACKING_SLIP | RcvngShpmntReceiptHdrPEOPackingSlip | ✅ |
| PAYMENT_TERMS_ID | RcvngShpmntReceiptHdrPEOPaymentTermsId | ✅ |
| RA_DOC_CREATION_DATE | RcvngShpmntReceiptHdrPEORaDocCreationDate | ✅ |
| RA_DOC_LAST_UPDATE_DATE | RcvngShpmntReceiptHdrPEORaDocLastUpdateDate | ✅ |
| RA_DOC_REVISION_DATE | RcvngShpmntReceiptHdrPEORaDocRevisionDate | ✅ |
| RA_DOC_REVISION_NUMBER | RcvngShpmntReceiptHdrPEORaDocRevisionNumber | ✅ |
| RA_DOCUMENT_CODE | RcvngShpmntReceiptHdrPEORaDocumentCode | ✅ |
| RA_DOCUMENT_NUMBER | RcvngShpmntReceiptHdrPEORaDocumentNumber | ✅ |
| RA_DOO_SOURCE_SYSTEM_ID | RcvngShpmntReceiptHdrPEORaDooSourceSystemId | ✅ |
| RA_NOTE_TO_RECEIVER | RcvngShpmntReceiptHdrPEORaNoteToReceiver | ✅ |
| RA_OUTSOURCER_CONTACT_ID | RcvngShpmntReceiptHdrPEORaOutsourcerContactId | ✅ |
| RA_OUTSOURCER_PARTY_ID | RcvngShpmntReceiptHdrPEORaOutsourcerPartyId | ✅ |
| RECEIPT_ADVICE_NUMBER | RcvngShpmntReceiptHdrPEOReceiptAdviceNumber | ✅ |
| RECEIPT_NUM | RcvngShpmntReceiptHdrPEOReceiptNum | ✅ |
| RECEIPT_SOURCE_CODE | RcvngShpmntReceiptHdrPEOReceiptSourceCode | ✅ |
| REMIT_TO_SITE_ID | RcvngShpmntReceiptHdrPEORemitToSiteId | ✅ |
| REQUEST_ID | RcvngShpmntReceiptHdrPEORequestId | ✅ |
| RMA_BU_ID | RcvngShpmntReceiptHdrPEORmaBuId | ✅ |
| SHIP_FROM_LOCATION_ID | RcvngShpmntReceiptHdrPEOShipFromLocationId | ✅ |
| SHIP_TO_LOCATION_ID | RcvngShpmntReceiptHdrPEOShipToLocationId | ✅ |
| SHIP_TO_ORG_ID | RcvngShpmntReceiptHdrPEOShipToOrgId | ✅ |
| SHIPMENT_HEADER_ID | RcvngShpmntReceiptHdrPEOShipmentHeaderId | ✅ |
| SHIPMENT_NUM | RcvngShpmntReceiptHdrPEOShipmentNum | ✅ |
| SHIPPED_DATE | RcvngShpmntReceiptHdrPEOShippedDate | ✅ |
| SPECIAL_HANDLING_CODE | RcvngShpmntReceiptHdrPEOSpecialHandlingCode | ✅ |
| TAR_WEIGHT | RcvngShpmntReceiptHdrPEOTarWeight | ✅ |
| TAR_WEIGHT_UOM_CODE | RcvngShpmntReceiptHdrPEOTarWeightUomCode | ✅ |
| TAX_AMOUNT | RcvngShpmntReceiptHdrPEOTaxAmount | ✅ |
| TAX_NAME | RcvngShpmntReceiptHdrPEOTaxName | ✅ |
| VENDOR_ID | RcvngShpmntReceiptHdrPEOVendorId | ✅ |
| VENDOR_SITE_ID | RcvngShpmntReceiptHdrPEOVendorSiteId | ✅ |
| WAYBILL_AIRBILL_NUM | RcvngShpmntReceiptHdrPEOWaybillAirbillNum | ✅ |

### [[receivingreceipttransactionpvo|ReceivingReceiptTransactionPVO]] (AR · BICC: 15/81)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPROVAL_STATUS | RcvShipmentHeadersPEOApprovalStatus | — |
| ASN_STATUS | RcvShipmentHeadersPEOAsnStatus | — |
| ASN_TYPE | RcvShipmentHeadersPEOAsnType | — |
| ATTRIBUTE_CATEGORY | RcvShipmentHeadersPEOAttributeCategory | — |
| BILL_OF_LADING | RcvShipmentHeadersPEOBillOfLading | ✅ |
| CARRIER_EQUIPMENT | RcvShipmentHeadersPEOCarrierEquipment | — |
| CARRIER_METHOD | RcvShipmentHeadersPEOCarrierMethod | — |
| COMMENTS | RcvShipmentHeadersPEOComments | — |
| CONVERSION_DATE | RcvShipmentHeadersPEOConversionDate | — |
| CONVERSION_RATE | RcvShipmentHeadersPEOConversionRate | — |
| CONVERSION_RATE_TYPE | RcvShipmentHeadersPEOConversionRateType | — |
| CREATED_BY | RcvShipmentHeadersPEOCreatedBy | — |
| CREATION_DATE | RcvShipmentHeadersPEOCreationDate | ✅ |
| CURRENCY_CODE | RcvShipmentHeadersPEOCurrencyCode | — |
| CUSTOMER_ID | RcvShipmentHeadersPEOCustomerId | — |
| CUSTOMER_SITE_ID | RcvShipmentHeadersPEOCustomerSiteId | — |
| EDI_CONTROL_NUM | RcvShipmentHeadersPEOEdiControlNum | — |
| EMPLOYEE_ID | RcvShipmentHeadersPEOEmployeeId | — |
| EXPECTED_RECEIPT_DATE | RcvShipmentHeadersPEOExpectedReceiptDate | — |
| FREIGHT_AMOUNT | RcvShipmentHeadersPEOFreightAmount | — |
| FREIGHT_BILL_NUMBER | RcvShipmentHeadersPEOFreightBillNumber | — |
| FREIGHT_CARRIER_ID | RcvShipmentHeadersPEOFreightCarrierId | — |
| FREIGHT_TERMS | RcvShipmentHeadersPEOFreightTerms | — |
| GOVERNMENT_CONTEXT | RcvShipmentHeadersPEOGovernmentContext | — |
| GROSS_WEIGHT | RcvShipmentHeadersPEOGrossWeight | — |
| GROSS_WEIGHT_UOM_CODE | RcvShipmentHeadersPEOGrossWeightUomCode | — |
| HAZARD_CLASS | RcvShipmentHeadersPEOHazardClass | — |
| HAZARD_CODE | RcvShipmentHeadersPEOHazardCode | — |
| HAZARD_DESCRIPTION | RcvShipmentHeadersPEOHazardDescription | — |
| INVOICE_AMOUNT | RcvShipmentHeadersPEOInvoiceAmount | — |
| INVOICE_DATE | RcvShipmentHeadersPEOInvoiceDate | — |
| INVOICE_NUM | RcvShipmentHeadersPEOInvoiceNum | — |
| INVOICE_STATUS_CODE | RcvShipmentHeadersPEOInvoiceStatusCode | — |
| JOB_DEFINITION_NAME | RcvShipmentHeadersPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | RcvShipmentHeadersPEOJobDefinitionPackage | — |
| LAST_UPDATE_DATE | RcvShipmentHeadersPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RcvShipmentHeadersPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | RcvShipmentHeadersPEOLastUpdatedBy | — |
| LSP_FLAG | RcvShipmentHeadersPEOLspFlag | — |
| NET_WEIGHT | RcvShipmentHeadersPEONetWeight | ✅ |
| NET_WEIGHT_UOM_CODE | RcvShipmentHeadersPEONetWeightUomCode | ✅ |
| NOTICE_CREATION_DATE | RcvShipmentHeadersPEONoticeCreationDate | — |
| NUM_OF_CONTAINERS | RcvShipmentHeadersPEONumOfContainers | — |
| OBJECT_VERSION_NUMBER | RcvShipmentHeadersPEOObjectVersionNumber | — |
| ORGANIZATION_ID | RcvShipmentHeadersPEOOrganizationId | — |
| PACKAGING_CODE | RcvShipmentHeadersPEOPackagingCode | — |
| PACKING_SLIP | RcvShipmentHeadersPEOPackingSlip | — |
| PAYMENT_TERMS_ID | RcvShipmentHeadersPEOPaymentTermsId | — |
| PERFORMANCE_PERIOD_FROM | RcvShipmentHeadersPEOPerformancePeriodFrom | — |
| PERFORMANCE_PERIOD_TO | RcvShipmentHeadersPEOPerformancePeriodTo | — |
| RA_DOC_CREATION_DATE | RcvShipmentHeadersPEORaDocCreationDate | — |
| RA_DOC_LAST_UPDATE_DATE | RcvShipmentHeadersPEORaDocLastUpdateDate | ✅ |
| RA_DOC_REVISION_DATE | RcvShipmentHeadersPEORaDocRevisionDate | — |
| RA_DOC_REVISION_NUMBER | RcvShipmentHeadersPEORaDocRevisionNumber | — |
| RA_DOCUMENT_CODE | RcvShipmentHeadersPEORaDocumentCode | — |
| RA_DOCUMENT_NUMBER | RcvShipmentHeadersPEORaDocumentNumber | — |
| RA_DOO_SOURCE_SYSTEM_ID | RcvShipmentHeadersPEORaDooSourceSystemId | — |
| RA_NOTE_TO_RECEIVER | RcvShipmentHeadersPEORaNoteToReceiver | ✅ |
| RA_OUTSOURCER_CONTACT_ID | RcvShipmentHeadersPEORaOutsourcerContactId | — |
| RA_OUTSOURCER_PARTY_ID | RcvShipmentHeadersPEORaOutsourcerPartyId | — |
| RECEIPT_ADVICE_NUMBER | RcvShipmentHeadersPEOReceiptAdviceNumber | — |
| RECEIPT_NUM | RcvShipmentHeadersPEOReceiptNum | ✅ |
| RECEIPT_SOURCE_CODE | RcvShipmentHeadersPEOReceiptSourceCode | ✅ |
| REMIT_TO_SITE_ID | RcvShipmentHeadersPEORemitToSiteId | — |
| REQUEST_DATE | RcvShipmentHeadersPEORequestDate | — |
| REQUEST_ID | RcvShipmentHeadersPEORequestId | — |
| RMA_BU_ID | RcvShipmentHeadersPEORmaBuId | — |
| SHIP_FROM_LOCATION_ID | RcvShipmentHeadersPEOShipFromLocationId | — |
| SHIP_TO_LOCATION_ID | RcvShipmentHeadersPEOShipToLocationId | — |
| SHIP_TO_ORG_ID | RcvShipmentHeadersPEOShipToOrgId | — |
| SHIPMENT_HEADER_ID | RcvShipmentHeadersPEOShipmentHeaderId | ✅ |
| SHIPMENT_NUM | RcvShipmentHeadersPEOShipmentNum | ✅ |
| SHIPPED_DATE | RcvShipmentHeadersPEOShippedDate | ✅ |
| SPECIAL_HANDLING_CODE | RcvShipmentHeadersPEOSpecialHandlingCode | — |
| TAR_WEIGHT | RcvShipmentHeadersPEOTarWeight | ✅ |
| TAR_WEIGHT_UOM_CODE | RcvShipmentHeadersPEOTarWeightUomCode | ✅ |
| TAX_AMOUNT | RcvShipmentHeadersPEOTaxAmount | — |
| TAX_NAME | RcvShipmentHeadersPEOTaxName | — |
| VENDOR_ID | RcvShipmentHeadersPEOVendorId | — |
| VENDOR_SITE_ID | RcvShipmentHeadersPEOVendorSiteId | — |
| WAYBILL_AIRBILL_NUM | RcvShipmentHeadersPEOWaybillAirbillNum | ✅ |

### [[receivingreceipttransactionrefpvo|ReceivingReceiptTransactionRefPVO]] (AR · BICC: 11/81)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPROVAL_STATUS | RcvShipmentHeadersPEOApprovalStatus | — |
| ASN_STATUS | RcvShipmentHeadersPEOAsnStatus | — |
| ASN_TYPE | RcvShipmentHeadersPEOAsnType | — |
| ATTRIBUTE_CATEGORY | RcvShipmentHeadersPEOAttributeCategory | — |
| BILL_OF_LADING | RcvShipmentHeadersPEOBillOfLading | ✅ |
| CARRIER_EQUIPMENT | RcvShipmentHeadersPEOCarrierEquipment | — |
| CARRIER_METHOD | RcvShipmentHeadersPEOCarrierMethod | — |
| COMMENTS | RcvShipmentHeadersPEOComments | — |
| CONVERSION_DATE | RcvShipmentHeadersPEOConversionDate | — |
| CONVERSION_RATE | RcvShipmentHeadersPEOConversionRate | — |
| CONVERSION_RATE_TYPE | RcvShipmentHeadersPEOConversionRateType | — |
| CREATED_BY | RcvShipmentHeadersPEOCreatedBy | — |
| CREATION_DATE | RcvShipmentHeadersPEOCreationDate | ✅ |
| CURRENCY_CODE | RcvShipmentHeadersPEOCurrencyCode | — |
| CUSTOMER_ID | RcvShipmentHeadersPEOCustomerId | — |
| CUSTOMER_SITE_ID | RcvShipmentHeadersPEOCustomerSiteId | — |
| EDI_CONTROL_NUM | RcvShipmentHeadersPEOEdiControlNum | — |
| EMPLOYEE_ID | RcvShipmentHeadersPEOEmployeeId | — |
| EXPECTED_RECEIPT_DATE | RcvShipmentHeadersPEOExpectedReceiptDate | — |
| FREIGHT_AMOUNT | RcvShipmentHeadersPEOFreightAmount | — |
| FREIGHT_BILL_NUMBER | RcvShipmentHeadersPEOFreightBillNumber | — |
| FREIGHT_CARRIER_ID | RcvShipmentHeadersPEOFreightCarrierId | — |
| FREIGHT_TERMS | RcvShipmentHeadersPEOFreightTerms | — |
| GOVERNMENT_CONTEXT | RcvShipmentHeadersPEOGovernmentContext | — |
| GROSS_WEIGHT | RcvShipmentHeadersPEOGrossWeight | — |
| GROSS_WEIGHT_UOM_CODE | RcvShipmentHeadersPEOGrossWeightUomCode | — |
| HAZARD_CLASS | RcvShipmentHeadersPEOHazardClass | — |
| HAZARD_CODE | RcvShipmentHeadersPEOHazardCode | — |
| HAZARD_DESCRIPTION | RcvShipmentHeadersPEOHazardDescription | — |
| INVOICE_AMOUNT | RcvShipmentHeadersPEOInvoiceAmount | — |
| INVOICE_DATE | RcvShipmentHeadersPEOInvoiceDate | — |
| INVOICE_NUM | RcvShipmentHeadersPEOInvoiceNum | — |
| INVOICE_STATUS_CODE | RcvShipmentHeadersPEOInvoiceStatusCode | — |
| JOB_DEFINITION_NAME | RcvShipmentHeadersPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | RcvShipmentHeadersPEOJobDefinitionPackage | — |
| LAST_UPDATE_DATE | RcvShipmentHeadersPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RcvShipmentHeadersPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | RcvShipmentHeadersPEOLastUpdatedBy | — |
| LSP_FLAG | RcvShipmentHeadersPEOLspFlag | — |
| NET_WEIGHT | RcvShipmentHeadersPEONetWeight | — |
| NET_WEIGHT_UOM_CODE | RcvShipmentHeadersPEONetWeightUomCode | — |
| NOTICE_CREATION_DATE | RcvShipmentHeadersPEONoticeCreationDate | — |
| NUM_OF_CONTAINERS | RcvShipmentHeadersPEONumOfContainers | — |
| OBJECT_VERSION_NUMBER | RcvShipmentHeadersPEOObjectVersionNumber | — |
| ORGANIZATION_ID | RcvShipmentHeadersPEOOrganizationId | — |
| PACKAGING_CODE | RcvShipmentHeadersPEOPackagingCode | — |
| PACKING_SLIP | RcvShipmentHeadersPEOPackingSlip | — |
| PAYMENT_TERMS_ID | RcvShipmentHeadersPEOPaymentTermsId | — |
| PERFORMANCE_PERIOD_FROM | RcvShipmentHeadersPEOPerformancePeriodFrom | — |
| PERFORMANCE_PERIOD_TO | RcvShipmentHeadersPEOPerformancePeriodTo | — |
| RA_DOC_CREATION_DATE | RcvShipmentHeadersPEORaDocCreationDate | — |
| RA_DOC_LAST_UPDATE_DATE | RcvShipmentHeadersPEORaDocLastUpdateDate | ✅ |
| RA_DOC_REVISION_DATE | RcvShipmentHeadersPEORaDocRevisionDate | — |
| RA_DOC_REVISION_NUMBER | RcvShipmentHeadersPEORaDocRevisionNumber | — |
| RA_DOCUMENT_CODE | RcvShipmentHeadersPEORaDocumentCode | — |
| RA_DOCUMENT_NUMBER | RcvShipmentHeadersPEORaDocumentNumber | — |
| RA_DOO_SOURCE_SYSTEM_ID | RcvShipmentHeadersPEORaDooSourceSystemId | — |
| RA_NOTE_TO_RECEIVER | RcvShipmentHeadersPEORaNoteToReceiver | ✅ |
| RA_OUTSOURCER_CONTACT_ID | RcvShipmentHeadersPEORaOutsourcerContactId | — |
| RA_OUTSOURCER_PARTY_ID | RcvShipmentHeadersPEORaOutsourcerPartyId | — |
| RECEIPT_ADVICE_NUMBER | RcvShipmentHeadersPEOReceiptAdviceNumber | — |
| RECEIPT_NUM | RcvShipmentHeadersPEOReceiptNum | ✅ |
| RECEIPT_SOURCE_CODE | RcvShipmentHeadersPEOReceiptSourceCode | ✅ |
| REMIT_TO_SITE_ID | RcvShipmentHeadersPEORemitToSiteId | — |
| REQUEST_DATE | RcvShipmentHeadersPEORequestDate | — |
| REQUEST_ID | RcvShipmentHeadersPEORequestId | — |
| RMA_BU_ID | RcvShipmentHeadersPEORmaBuId | — |
| SHIP_FROM_LOCATION_ID | RcvShipmentHeadersPEOShipFromLocationId | — |
| SHIP_TO_LOCATION_ID | RcvShipmentHeadersPEOShipToLocationId | — |
| SHIP_TO_ORG_ID | RcvShipmentHeadersPEOShipToOrgId | — |
| SHIPMENT_HEADER_ID | RcvShipmentHeadersPEOShipmentHeaderId | ✅ |
| SHIPMENT_NUM | RcvShipmentHeadersPEOShipmentNum | ✅ |
| SHIPPED_DATE | RcvShipmentHeadersPEOShippedDate | ✅ |
| SPECIAL_HANDLING_CODE | RcvShipmentHeadersPEOSpecialHandlingCode | — |
| TAR_WEIGHT | RcvShipmentHeadersPEOTarWeight | — |
| TAR_WEIGHT_UOM_CODE | RcvShipmentHeadersPEOTarWeightUomCode | — |
| TAX_AMOUNT | RcvShipmentHeadersPEOTaxAmount | — |
| TAX_NAME | RcvShipmentHeadersPEOTaxName | — |
| VENDOR_ID | RcvShipmentHeadersPEOVendorId | — |
| VENDOR_SITE_ID | RcvShipmentHeadersPEOVendorSiteId | — |
| WAYBILL_AIRBILL_NUM | RcvShipmentHeadersPEOWaybillAirbillNum | ✅ |

### [[wooperationspvo|WOOperationsPVO]] (OTHER · BICC: 28/123)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPROVAL_STATUS | RcvShipmentHeadersApprovalStatus1 | — |
| ASN_STATUS | RcvShipmentHeadersAsnStatus | — |
| ASN_TYPE | RcvShipmentHeadersAsnType | — |
| ATTRIBUTE1 | RcvShipmentHeadersAttribute116 | — |
| ATTRIBUTE10 | RcvShipmentHeadersAttribute104 | — |
| ATTRIBUTE11 | RcvShipmentHeadersAttribute117 | — |
| ATTRIBUTE12 | RcvShipmentHeadersAttribute124 | — |
| ATTRIBUTE13 | RcvShipmentHeadersAttribute134 | — |
| ATTRIBUTE14 | RcvShipmentHeadersAttribute144 | — |
| ATTRIBUTE15 | RcvShipmentHeadersAttribute154 | — |
| ATTRIBUTE16 | RcvShipmentHeadersAttribute164 | — |
| ATTRIBUTE17 | RcvShipmentHeadersAttribute174 | — |
| ATTRIBUTE18 | RcvShipmentHeadersAttribute184 | — |
| ATTRIBUTE19 | RcvShipmentHeadersAttribute194 | — |
| ATTRIBUTE2 | RcvShipmentHeadersAttribute24 | — |
| ATTRIBUTE20 | RcvShipmentHeadersAttribute204 | — |
| ATTRIBUTE3 | RcvShipmentHeadersAttribute34 | — |
| ATTRIBUTE4 | RcvShipmentHeadersAttribute44 | — |
| ATTRIBUTE5 | RcvShipmentHeadersAttribute54 | — |
| ATTRIBUTE6 | RcvShipmentHeadersAttribute64 | — |
| ATTRIBUTE7 | RcvShipmentHeadersAttribute74 | — |
| ATTRIBUTE8 | RcvShipmentHeadersAttribute84 | — |
| ATTRIBUTE9 | RcvShipmentHeadersAttribute94 | — |
| ATTRIBUTE_CATEGORY | RcvShipmentHeadersAttributeCategory4 | — |
| ATTRIBUTE_DATE1 | RcvShipmentHeadersAttributeDate14 | — |
| ATTRIBUTE_DATE2 | RcvShipmentHeadersAttributeDate24 | — |
| ATTRIBUTE_DATE3 | RcvShipmentHeadersAttributeDate34 | — |
| ATTRIBUTE_DATE4 | RcvShipmentHeadersAttributeDate44 | — |
| ATTRIBUTE_DATE5 | RcvShipmentHeadersAttributeDate54 | — |
| ATTRIBUTE_NUMBER1 | RcvShipmentHeadersAttributeNumber14 | — |
| ATTRIBUTE_NUMBER10 | RcvShipmentHeadersAttributeNumber104 | — |
| ATTRIBUTE_NUMBER2 | RcvShipmentHeadersAttributeNumber24 | — |
| ATTRIBUTE_NUMBER3 | RcvShipmentHeadersAttributeNumber34 | — |
| ATTRIBUTE_NUMBER4 | RcvShipmentHeadersAttributeNumber44 | — |
| ATTRIBUTE_NUMBER5 | RcvShipmentHeadersAttributeNumber54 | — |
| ATTRIBUTE_NUMBER6 | RcvShipmentHeadersAttributeNumber64 | — |
| ATTRIBUTE_NUMBER7 | RcvShipmentHeadersAttributeNumber74 | — |
| ATTRIBUTE_NUMBER8 | RcvShipmentHeadersAttributeNumber84 | — |
| ATTRIBUTE_NUMBER9 | RcvShipmentHeadersAttributeNumber94 | — |
| ATTRIBUTE_TIMESTAMP1 | RcvShipmentHeadersAttributeTimestamp14 | — |
| ATTRIBUTE_TIMESTAMP2 | RcvShipmentHeadersAttributeTimestamp24 | — |
| ATTRIBUTE_TIMESTAMP3 | RcvShipmentHeadersAttributeTimestamp34 | — |
| ATTRIBUTE_TIMESTAMP4 | RcvShipmentHeadersAttributeTimestamp44 | — |
| ATTRIBUTE_TIMESTAMP5 | RcvShipmentHeadersAttributeTimestamp54 | — |
| BILL_OF_LADING | RcvShipmentHeadersBillOfLading | — |
| CARRIER_EQUIPMENT | RcvShipmentHeadersCarrierEquipment | — |
| CARRIER_METHOD | RcvShipmentHeadersCarrierMethod | — |
| COMMENTS | RcvShipmentHeadersComments2 | — |
| CONVERSION_DATE | RcvShipmentHeadersConversionDate | ✅ |
| CONVERSION_RATE | RcvShipmentHeadersConversionRate | — |
| CONVERSION_RATE_TYPE | RcvShipmentHeadersConversionRateType | — |
| CREATED_BY | RcvShipmentHeadersCreatedBy4 | — |
| CREATION_DATE | RcvShipmentHeadersCreationDate4 | — |
| CURRENCY_CODE | RcvShipmentHeadersCurrencyCode1 | — |
| CUSTOMER_ID | RcvShipmentHeadersCustomerId1 | ✅ |
| CUSTOMER_SITE_ID | RcvShipmentHeadersCustomerSiteId1 | ✅ |
| EDI_CONTROL_NUM | RcvShipmentHeadersEdiControlNum | — |
| EMPLOYEE_ID | RcvShipmentHeadersEmployeeId1 | ✅ |
| EXPECTED_RECEIPT_DATE | RcvShipmentHeadersExpectedReceiptDate | ✅ |
| FREIGHT_AMOUNT | RcvShipmentHeadersFreightAmount | — |
| FREIGHT_BILL_NUMBER | RcvShipmentHeadersFreightBillNumber | — |
| FREIGHT_CARRIER_ID | RcvShipmentHeadersFreightCarrierId | ✅ |
| FREIGHT_TERMS | RcvShipmentHeadersFreightTerms | — |
| GOVERNMENT_CONTEXT | RcvShipmentHeadersGovernmentContext4 | — |
| GROSS_WEIGHT | RcvShipmentHeadersGrossWeight | — |
| GROSS_WEIGHT_UOM_CODE | RcvShipmentHeadersGrossWeightUomCode | — |
| HAZARD_CLASS | RcvShipmentHeadersHazardClass | — |
| HAZARD_CODE | RcvShipmentHeadersHazardCode | — |
| HAZARD_DESCRIPTION | RcvShipmentHeadersHazardDescription | — |
| HEADER_INTERFACE_ID | RcvShipmentHeadersHeaderInterfaceId | ✅ |
| INVOICE_AMOUNT | RcvShipmentHeadersInvoiceAmount | — |
| INVOICE_DATE | RcvShipmentHeadersInvoiceDate | ✅ |
| INVOICE_NUM | RcvShipmentHeadersInvoiceNum | — |
| INVOICE_STATUS_CODE | RcvShipmentHeadersInvoiceStatusCode1 | — |
| JOB_DEFINITION_NAME | RcvShipmentHeadersJobDefinitionName4 | — |
| JOB_DEFINITION_PACKAGE | RcvShipmentHeadersJobDefinitionPackage4 | — |
| LAST_UPDATE_DATE | RcvShipmentHeadersLastUpdateDate4 | ✅ |
| LAST_UPDATE_LOGIN | RcvShipmentHeadersLastUpdateLogin4 | — |
| LAST_UPDATED_BY | RcvShipmentHeadersLastUpdatedBy4 | — |
| LSP_FLAG | RcvShipmentHeadersLspFlag | — |
| NET_WEIGHT | RcvShipmentHeadersNetWeight | — |
| NET_WEIGHT_UOM_CODE | RcvShipmentHeadersNetWeightUomCode | — |
| NOTICE_CREATION_DATE | RcvShipmentHeadersNoticeCreationDate | ✅ |
| NUM_OF_CONTAINERS | RcvShipmentHeadersNumOfContainers | — |
| OBJECT_VERSION_NUMBER | RcvShipmentHeadersObjectVersionNumber4 | — |
| ORGANIZATION_ID | RcvShipmentHeadersOrganizationId | — |
| PACKAGING_CODE | RcvShipmentHeadersPackagingCode | — |
| PACKING_SLIP | RcvShipmentHeadersPackingSlip1 | — |
| PAYMENT_TERMS_ID | RcvShipmentHeadersPaymentTermsId | — |
| PERFORMANCE_PERIOD_FROM | RcvShipmentHeadersPerformancePeriodFrom | — |
| PERFORMANCE_PERIOD_TO | RcvShipmentHeadersPerformancePeriodTo | — |
| RA_DOC_CREATION_DATE | RcvShipmentHeadersRaDocCreationDate | ✅ |
| RA_DOC_LAST_UPDATE_DATE | RcvShipmentHeadersRaDocLastUpdateDate | ✅ |
| RA_DOC_REVISION_DATE | RcvShipmentHeadersRaDocRevisionDate | ✅ |
| RA_DOC_REVISION_NUMBER | RcvShipmentHeadersRaDocRevisionNumber | — |
| RA_DOCUMENT_CODE | RcvShipmentHeadersRaDocumentCode | — |
| RA_DOCUMENT_NUMBER | RcvShipmentHeadersRaDocumentNumber | — |
| RA_DOO_SOURCE_SYSTEM_ID | RcvShipmentHeadersRaDooSourceSystemId | ✅ |
| RA_NOTE_TO_RECEIVER | RcvShipmentHeadersRaNoteToReceiver1 | — |
| RA_ORIG_SYSTEM_REF | RcvShipmentHeadersRaOrigSystemRef | — |
| RA_OUTSOURCER_CONTACT_ID | RcvShipmentHeadersRaOutsourcerContactId | ✅ |
| RA_OUTSOURCER_PARTY_ID | RcvShipmentHeadersRaOutsourcerPartyId | ✅ |
| RECEIPT_ADVICE_NUMBER | RcvShipmentHeadersReceiptAdviceNumber | — |
| RECEIPT_NUM | RcvShipmentHeadersReceiptNum | ✅ |
| RECEIPT_SOURCE_CODE | RcvShipmentHeadersReceiptSourceCode | — |
| REMIT_TO_SITE_ID | RcvShipmentHeadersRemitToSiteId | ✅ |
| REQUEST_DATE | RcvShipmentHeadersRequestDate | ✅ |
| REQUEST_ID | RcvShipmentHeadersRequestId4 | ✅ |
| RMA_BU_ID | RcvShipmentHeadersRmaBuId | ✅ |
| SHIP_FROM_LOCATION_ID | RcvShipmentHeadersShipFromLocationId1 | ✅ |
| SHIP_TO_LOCATION_ID | RcvShipmentHeadersShipToLocationId3 | ✅ |
| SHIP_TO_ORG_ID | RcvShipmentHeadersShipToOrgId | ✅ |
| SHIPMENT_HEADER_ID | RcvShipmentHeadersShipmentHeaderId1 | ✅ |
| SHIPMENT_NUM | RcvShipmentHeadersShipmentNum1 | — |
| SHIPPED_DATE | RcvShipmentHeadersShippedDate | ✅ |
| SPECIAL_HANDLING_CODE | RcvShipmentHeadersSpecialHandlingCode | — |
| TAR_WEIGHT | RcvShipmentHeadersTarWeight | — |
| TAR_WEIGHT_UOM_CODE | RcvShipmentHeadersTarWeightUomCode | — |
| TAX_AMOUNT | RcvShipmentHeadersTaxAmount1 | — |
| TAX_NAME | RcvShipmentHeadersTaxName3 | — |
| VENDOR_ID | RcvShipmentHeadersVendorId1 | ✅ |
| VENDOR_SITE_ID | RcvShipmentHeadersVendorSiteId1 | ✅ |
| WAYBILL_AIRBILL_NUM | RcvShipmentHeadersWaybillAirbillNum | — |

### [[wooperationsrefpvo|WOOperationsRefPVO]] (OTHER · BICC: 31/123)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPROVAL_STATUS | RcvShipmentHeadersApprovalStatus1 | — |
| ASN_STATUS | RcvShipmentHeadersAsnStatus | — |
| ASN_TYPE | RcvShipmentHeadersAsnType | — |
| ATTRIBUTE1 | RcvShipmentHeadersAttribute116 | — |
| ATTRIBUTE10 | RcvShipmentHeadersAttribute104 | — |
| ATTRIBUTE11 | RcvShipmentHeadersAttribute117 | — |
| ATTRIBUTE12 | RcvShipmentHeadersAttribute124 | — |
| ATTRIBUTE13 | RcvShipmentHeadersAttribute134 | — |
| ATTRIBUTE14 | RcvShipmentHeadersAttribute144 | — |
| ATTRIBUTE15 | RcvShipmentHeadersAttribute154 | — |
| ATTRIBUTE16 | RcvShipmentHeadersAttribute164 | — |
| ATTRIBUTE17 | RcvShipmentHeadersAttribute174 | — |
| ATTRIBUTE18 | RcvShipmentHeadersAttribute184 | — |
| ATTRIBUTE19 | RcvShipmentHeadersAttribute194 | — |
| ATTRIBUTE2 | RcvShipmentHeadersAttribute24 | — |
| ATTRIBUTE20 | RcvShipmentHeadersAttribute204 | — |
| ATTRIBUTE3 | RcvShipmentHeadersAttribute34 | — |
| ATTRIBUTE4 | RcvShipmentHeadersAttribute44 | — |
| ATTRIBUTE5 | RcvShipmentHeadersAttribute54 | — |
| ATTRIBUTE6 | RcvShipmentHeadersAttribute64 | — |
| ATTRIBUTE7 | RcvShipmentHeadersAttribute74 | — |
| ATTRIBUTE8 | RcvShipmentHeadersAttribute84 | — |
| ATTRIBUTE9 | RcvShipmentHeadersAttribute94 | — |
| ATTRIBUTE_CATEGORY | RcvShipmentHeadersAttributeCategory4 | — |
| ATTRIBUTE_DATE1 | RcvShipmentHeadersAttributeDate14 | — |
| ATTRIBUTE_DATE2 | RcvShipmentHeadersAttributeDate24 | — |
| ATTRIBUTE_DATE3 | RcvShipmentHeadersAttributeDate34 | — |
| ATTRIBUTE_DATE4 | RcvShipmentHeadersAttributeDate44 | — |
| ATTRIBUTE_DATE5 | RcvShipmentHeadersAttributeDate54 | — |
| ATTRIBUTE_NUMBER1 | RcvShipmentHeadersAttributeNumber14 | — |
| ATTRIBUTE_NUMBER10 | RcvShipmentHeadersAttributeNumber104 | — |
| ATTRIBUTE_NUMBER2 | RcvShipmentHeadersAttributeNumber24 | — |
| ATTRIBUTE_NUMBER3 | RcvShipmentHeadersAttributeNumber34 | — |
| ATTRIBUTE_NUMBER4 | RcvShipmentHeadersAttributeNumber44 | — |
| ATTRIBUTE_NUMBER5 | RcvShipmentHeadersAttributeNumber54 | — |
| ATTRIBUTE_NUMBER6 | RcvShipmentHeadersAttributeNumber64 | — |
| ATTRIBUTE_NUMBER7 | RcvShipmentHeadersAttributeNumber74 | — |
| ATTRIBUTE_NUMBER8 | RcvShipmentHeadersAttributeNumber84 | — |
| ATTRIBUTE_NUMBER9 | RcvShipmentHeadersAttributeNumber94 | — |
| ATTRIBUTE_TIMESTAMP1 | RcvShipmentHeadersAttributeTimestamp14 | — |
| ATTRIBUTE_TIMESTAMP2 | RcvShipmentHeadersAttributeTimestamp24 | — |
| ATTRIBUTE_TIMESTAMP3 | RcvShipmentHeadersAttributeTimestamp34 | — |
| ATTRIBUTE_TIMESTAMP4 | RcvShipmentHeadersAttributeTimestamp44 | — |
| ATTRIBUTE_TIMESTAMP5 | RcvShipmentHeadersAttributeTimestamp54 | — |
| BILL_OF_LADING | RcvShipmentHeadersBillOfLading | — |
| CARRIER_EQUIPMENT | RcvShipmentHeadersCarrierEquipment | — |
| CARRIER_METHOD | RcvShipmentHeadersCarrierMethod | — |
| COMMENTS | RcvShipmentHeadersComments2 | — |
| CONVERSION_DATE | RcvShipmentHeadersConversionDate | ✅ |
| CONVERSION_RATE | RcvShipmentHeadersConversionRate | — |
| CONVERSION_RATE_TYPE | RcvShipmentHeadersConversionRateType | — |
| CREATED_BY | RcvShipmentHeadersCreatedBy4 | — |
| CREATION_DATE | RcvShipmentHeadersCreationDate4 | ✅ |
| CURRENCY_CODE | RcvShipmentHeadersCurrencyCode1 | — |
| CUSTOMER_ID | RcvShipmentHeadersCustomerId1 | ✅ |
| CUSTOMER_SITE_ID | RcvShipmentHeadersCustomerSiteId1 | ✅ |
| EDI_CONTROL_NUM | RcvShipmentHeadersEdiControlNum | — |
| EMPLOYEE_ID | RcvShipmentHeadersEmployeeId1 | ✅ |
| EXPECTED_RECEIPT_DATE | RcvShipmentHeadersExpectedReceiptDate | ✅ |
| FREIGHT_AMOUNT | RcvShipmentHeadersFreightAmount | — |
| FREIGHT_BILL_NUMBER | RcvShipmentHeadersFreightBillNumber | — |
| FREIGHT_CARRIER_ID | RcvShipmentHeadersFreightCarrierId | ✅ |
| FREIGHT_TERMS | RcvShipmentHeadersFreightTerms | — |
| GOVERNMENT_CONTEXT | RcvShipmentHeadersGovernmentContext4 | — |
| GROSS_WEIGHT | RcvShipmentHeadersGrossWeight | — |
| GROSS_WEIGHT_UOM_CODE | RcvShipmentHeadersGrossWeightUomCode | — |
| HAZARD_CLASS | RcvShipmentHeadersHazardClass | — |
| HAZARD_CODE | RcvShipmentHeadersHazardCode | — |
| HAZARD_DESCRIPTION | RcvShipmentHeadersHazardDescription | — |
| HEADER_INTERFACE_ID | RcvShipmentHeadersHeaderInterfaceId | ✅ |
| INVOICE_AMOUNT | RcvShipmentHeadersInvoiceAmount | — |
| INVOICE_DATE | RcvShipmentHeadersInvoiceDate | ✅ |
| INVOICE_NUM | RcvShipmentHeadersInvoiceNum | — |
| INVOICE_STATUS_CODE | RcvShipmentHeadersInvoiceStatusCode1 | — |
| JOB_DEFINITION_NAME | RcvShipmentHeadersJobDefinitionName4 | — |
| JOB_DEFINITION_PACKAGE | RcvShipmentHeadersJobDefinitionPackage4 | — |
| LAST_UPDATE_DATE | RcvShipmentHeadersLastUpdateDate4 | ✅ |
| LAST_UPDATE_LOGIN | RcvShipmentHeadersLastUpdateLogin4 | — |
| LAST_UPDATED_BY | RcvShipmentHeadersLastUpdatedBy4 | — |
| LSP_FLAG | RcvShipmentHeadersLspFlag | — |
| NET_WEIGHT | RcvShipmentHeadersNetWeight | — |
| NET_WEIGHT_UOM_CODE | RcvShipmentHeadersNetWeightUomCode | — |
| NOTICE_CREATION_DATE | RcvShipmentHeadersNoticeCreationDate | ✅ |
| NUM_OF_CONTAINERS | RcvShipmentHeadersNumOfContainers | — |
| OBJECT_VERSION_NUMBER | RcvShipmentHeadersObjectVersionNumber4 | — |
| ORGANIZATION_ID | RcvShipmentHeadersOrganizationId | ✅ |
| PACKAGING_CODE | RcvShipmentHeadersPackagingCode | — |
| PACKING_SLIP | RcvShipmentHeadersPackingSlip1 | — |
| PAYMENT_TERMS_ID | RcvShipmentHeadersPaymentTermsId | ✅ |
| PERFORMANCE_PERIOD_FROM | RcvShipmentHeadersPerformancePeriodFrom | — |
| PERFORMANCE_PERIOD_TO | RcvShipmentHeadersPerformancePeriodTo | — |
| RA_DOC_CREATION_DATE | RcvShipmentHeadersRaDocCreationDate | ✅ |
| RA_DOC_LAST_UPDATE_DATE | RcvShipmentHeadersRaDocLastUpdateDate | ✅ |
| RA_DOC_REVISION_DATE | RcvShipmentHeadersRaDocRevisionDate | ✅ |
| RA_DOC_REVISION_NUMBER | RcvShipmentHeadersRaDocRevisionNumber | — |
| RA_DOCUMENT_CODE | RcvShipmentHeadersRaDocumentCode | — |
| RA_DOCUMENT_NUMBER | RcvShipmentHeadersRaDocumentNumber | — |
| RA_DOO_SOURCE_SYSTEM_ID | RcvShipmentHeadersRaDooSourceSystemId | ✅ |
| RA_NOTE_TO_RECEIVER | RcvShipmentHeadersRaNoteToReceiver1 | — |
| RA_ORIG_SYSTEM_REF | RcvShipmentHeadersRaOrigSystemRef | — |
| RA_OUTSOURCER_CONTACT_ID | RcvShipmentHeadersRaOutsourcerContactId | ✅ |
| RA_OUTSOURCER_PARTY_ID | RcvShipmentHeadersRaOutsourcerPartyId | ✅ |
| RECEIPT_ADVICE_NUMBER | RcvShipmentHeadersReceiptAdviceNumber | — |
| RECEIPT_NUM | RcvShipmentHeadersReceiptNum | ✅ |
| RECEIPT_SOURCE_CODE | RcvShipmentHeadersReceiptSourceCode | — |
| REMIT_TO_SITE_ID | RcvShipmentHeadersRemitToSiteId | ✅ |
| REQUEST_DATE | RcvShipmentHeadersRequestDate | ✅ |
| REQUEST_ID | RcvShipmentHeadersRequestId4 | ✅ |
| RMA_BU_ID | RcvShipmentHeadersRmaBuId | ✅ |
| SHIP_FROM_LOCATION_ID | RcvShipmentHeadersShipFromLocationId1 | ✅ |
| SHIP_TO_LOCATION_ID | RcvShipmentHeadersShipToLocationId3 | ✅ |
| SHIP_TO_ORG_ID | RcvShipmentHeadersShipToOrgId | ✅ |
| SHIPMENT_HEADER_ID | RcvShipmentHeadersShipmentHeaderId1 | ✅ |
| SHIPMENT_NUM | RcvShipmentHeadersShipmentNum1 | — |
| SHIPPED_DATE | RcvShipmentHeadersShippedDate | ✅ |
| SPECIAL_HANDLING_CODE | RcvShipmentHeadersSpecialHandlingCode | — |
| TAR_WEIGHT | RcvShipmentHeadersTarWeight | — |
| TAR_WEIGHT_UOM_CODE | RcvShipmentHeadersTarWeightUomCode | — |
| TAX_AMOUNT | RcvShipmentHeadersTaxAmount1 | — |
| TAX_NAME | RcvShipmentHeadersTaxName3 | — |
| VENDOR_ID | RcvShipmentHeadersVendorId1 | ✅ |
| VENDOR_SITE_ID | RcvShipmentHeadersVendorSiteId1 | ✅ |
| WAYBILL_AIRBILL_NUM | RcvShipmentHeadersWaybillAirbillNum | — |

### [[woprocurementreceiptpvo|WOProcurementReceiptPVO]] (OTHER · BICC: 8/82)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPROVAL_STATUS | RcvShipmentReceiptHeaderPEOApprovalStatus | — |
| ASN_STATUS | RcvShipmentReceiptHeaderPEOAsnStatus | — |
| ASN_TYPE | RcvShipmentReceiptHeaderPEOAsnType | — |
| BILL_OF_LADING | RcvShipmentReceiptHeaderPEOBillOfLading | — |
| CARRIER_EQUIPMENT | RcvShipmentReceiptHeaderPEOCarrierEquipment | — |
| CARRIER_METHOD | RcvShipmentReceiptHeaderPEOCarrierMethod | — |
| COMMENTS | RcvShipmentReceiptHeaderPEOComments | — |
| CONVERSION_DATE | RcvShipmentReceiptHeaderPEOConversionDate | — |
| CONVERSION_RATE | RcvShipmentReceiptHeaderPEOConversionRate | — |
| CONVERSION_RATE_TYPE | RcvShipmentReceiptHeaderPEOConversionRateType | — |
| CREATED_BY | RcvShipmentReceiptHeaderPEOCreatedBy | ✅ |
| CREATION_DATE | RcvShipmentReceiptHeaderPEOCreationDate | ✅ |
| CURRENCY_CODE | RcvShipmentReceiptHeaderPEOCurrencyCode | — |
| CUSTOMER_ID | RcvShipmentReceiptHeaderPEOCustomerId | — |
| CUSTOMER_SITE_ID | RcvShipmentReceiptHeaderPEOCustomerSiteId | — |
| EDI_CONTROL_NUM | RcvShipmentReceiptHeaderPEOEdiControlNum | — |
| EMPLOYEE_ID | RcvShipmentReceiptHeaderPEOEmployeeId | — |
| EXPECTED_RECEIPT_DATE | RcvShipmentReceiptHeaderPEOExpectedReceiptDate | — |
| FREIGHT_AMOUNT | RcvShipmentReceiptHeaderPEOFreightAmount | — |
| FREIGHT_BILL_NUMBER | RcvShipmentReceiptHeaderPEOFreightBillNumber | — |
| FREIGHT_CARRIER_ID | RcvShipmentReceiptHeaderPEOFreightCarrierId | — |
| FREIGHT_TERMS | RcvShipmentReceiptHeaderPEOFreightTerms | — |
| GOVERNMENT_CONTEXT | RcvShipmentReceiptHeaderPEOGovernmentContext | — |
| GROSS_WEIGHT | RcvShipmentReceiptHeaderPEOGrossWeight | — |
| GROSS_WEIGHT_UOM_CODE | RcvShipmentReceiptHeaderPEOGrossWeightUomCode | — |
| HAZARD_CLASS | RcvShipmentReceiptHeaderPEOHazardClass | — |
| HAZARD_CODE | RcvShipmentReceiptHeaderPEOHazardCode | — |
| HAZARD_DESCRIPTION | RcvShipmentReceiptHeaderPEOHazardDescription | — |
| HEADER_INTERFACE_ID | RcvShipmentReceiptHeaderPEOHeaderInterfaceId | — |
| INVOICE_AMOUNT | RcvShipmentReceiptHeaderPEOInvoiceAmount | — |
| INVOICE_DATE | RcvShipmentReceiptHeaderPEOInvoiceDate | — |
| INVOICE_NUM | RcvShipmentReceiptHeaderPEOInvoiceNum | — |
| INVOICE_STATUS_CODE | RcvShipmentReceiptHeaderPEOInvoiceStatusCode | — |
| JOB_DEFINITION_NAME | RcvShipmentReceiptHeaderPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | RcvShipmentReceiptHeaderPEOJobDefinitionPackage | — |
| LAST_UPDATE_DATE | RcvShipmentReceiptHeaderPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RcvShipmentReceiptHeaderPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | RcvShipmentReceiptHeaderPEOLastUpdatedBy | ✅ |
| LSP_FLAG | RcvShipmentReceiptHeaderPEOLspFlag | — |
| NET_WEIGHT | RcvShipmentReceiptHeaderPEONetWeight | — |
| NET_WEIGHT_UOM_CODE | RcvShipmentReceiptHeaderPEONetWeightUomCode | — |
| NOTICE_CREATION_DATE | RcvShipmentReceiptHeaderPEONoticeCreationDate | — |
| NUM_OF_CONTAINERS | RcvShipmentReceiptHeaderPEONumOfContainers | — |
| OBJECT_VERSION_NUMBER | RcvShipmentReceiptHeaderPEOObjectVersionNumber | — |
| ORGANIZATION_ID | RcvShipmentReceiptHeaderPEOOrganizationId | — |
| PACKAGING_CODE | RcvShipmentReceiptHeaderPEOPackagingCode | — |
| PACKING_SLIP | RcvShipmentReceiptHeaderPEOPackingSlip | — |
| PAYMENT_TERMS_ID | RcvShipmentReceiptHeaderPEOPaymentTermsId | — |
| PERFORMANCE_PERIOD_FROM | RcvShipmentReceiptHeaderPEOPerformancePeriodFrom | — |
| PERFORMANCE_PERIOD_TO | RcvShipmentReceiptHeaderPEOPerformancePeriodTo | — |
| RA_DOC_CREATION_DATE | RcvShipmentReceiptHeaderPEORaDocCreationDate | — |
| RA_DOC_LAST_UPDATE_DATE | RcvShipmentReceiptHeaderPEORaDocLastUpdateDate | ✅ |
| RA_DOC_REVISION_DATE | RcvShipmentReceiptHeaderPEORaDocRevisionDate | — |
| RA_DOC_REVISION_NUMBER | RcvShipmentReceiptHeaderPEORaDocRevisionNumber | — |
| RA_DOCUMENT_CODE | RcvShipmentReceiptHeaderPEORaDocumentCode | — |
| RA_DOCUMENT_NUMBER | RcvShipmentReceiptHeaderPEORaDocumentNumber | — |
| RA_DOO_SOURCE_SYSTEM_ID | RcvShipmentReceiptHeaderPEORaDooSourceSystemId | — |
| RA_NOTE_TO_RECEIVER | RcvShipmentReceiptHeaderPEORaNoteToReceiver | — |
| RA_ORIG_SYSTEM_REF | RcvShipmentReceiptHeaderPEORaOrigSystemRef | — |
| RA_OUTSOURCER_CONTACT_ID | RcvShipmentReceiptHeaderPEORaOutsourcerContactId | — |
| RA_OUTSOURCER_PARTY_ID | RcvShipmentReceiptHeaderPEORaOutsourcerPartyId | — |
| RECEIPT_ADVICE_NUMBER | RcvShipmentReceiptHeaderPEOReceiptAdviceNumber | — |
| RECEIPT_NUM | RcvShipmentReceiptHeaderPEOReceiptNum | ✅ |
| RECEIPT_SOURCE_CODE | RcvShipmentReceiptHeaderPEOReceiptSourceCode | — |
| REMIT_TO_SITE_ID | RcvShipmentReceiptHeaderPEORemitToSiteId | — |
| REQUEST_DATE | RcvShipmentReceiptHeaderPEORequestDate | — |
| REQUEST_ID | RcvShipmentReceiptHeaderPEORequestId | — |
| RMA_BU_ID | RcvShipmentReceiptHeaderPEORmaBuId | — |
| SHIP_FROM_LOCATION_ID | RcvShipmentReceiptHeaderPEOShipFromLocationId | — |
| SHIP_TO_LOCATION_ID | RcvShipmentReceiptHeaderPEOShipToLocationId | — |
| SHIP_TO_ORG_ID | RcvShipmentReceiptHeaderPEOShipToOrgId | — |
| SHIPMENT_HEADER_ID | RcvShipmentReceiptHeaderPEOShipmentHeaderId | ✅ |
| SHIPMENT_NUM | RcvShipmentReceiptHeaderPEOShipmentNum | ✅ |
| SHIPPED_DATE | RcvShipmentReceiptHeaderPEOShippedDate | — |
| SPECIAL_HANDLING_CODE | RcvShipmentReceiptHeaderPEOSpecialHandlingCode | — |
| TAR_WEIGHT | RcvShipmentReceiptHeaderPEOTarWeight | — |
| TAR_WEIGHT_UOM_CODE | RcvShipmentReceiptHeaderPEOTarWeightUomCode | — |
| TAX_AMOUNT | RcvShipmentReceiptHeaderPEOTaxAmount | — |
| TAX_NAME | RcvShipmentReceiptHeaderPEOTaxName | — |
| VENDOR_ID | RcvShipmentReceiptHeaderPEOVendorId | — |
| VENDOR_SITE_ID | RcvShipmentReceiptHeaderPEOVendorSiteId | — |
| WAYBILL_AIRBILL_NUM | RcvShipmentReceiptHeaderPEOWaybillAirbillNum | — |

---

## 📚 Referências

- [Oracle Docs — RCV_SHIPMENT_HEADERS](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/rcvshipmentheaders-10274.html)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
