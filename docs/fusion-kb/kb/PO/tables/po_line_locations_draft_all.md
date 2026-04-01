---
id: DOC-PO-135
doc_type: system-doc
title: "PO_LINE_LOCATIONS_DRAFT_ALL — Schedules de Entrega em Rascunho"
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
  - PO_LINE_LOCATIONS_DRAFT_ALL
  - po_line_locations_draft_all
  - po-line-locations-draft-all
  - po-line
  - schedules-de-entrega-em-rascunho
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_LINE_LOCATIONS_DRAFT_ALL

## 📌 Visão Geral

Armazena os **schedules de POs em rascunho**. Estrutura espelha `PO_LINE_LOCATIONS_ALL`.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` e necessario para consultas por organizacao especifica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Edicao:** Schedules de POs em elaboracao.
- **Amendments:** Alteracoes de schedules durante emendas.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LINE_LOCATION_ID | NUMBER(18) | NOT NULL | PK | ID do schedule | — | 🟢 95% |
| 2 | DRAFT_ID | NUMBER(18) | NOT NULL | PK | ID do draft | [[po_headers_draft_all]] | 🟢 95% |
| 3 | PO_HEADER_ID | NUMBER(18) | NOT NULL | FK | Cabecalho | [[po_headers_draft_all]] | 🟢 95% |
| 4 | PO_LINE_ID | NUMBER(18) | NOT NULL | FK | Linha | [[po_lines_draft_all]] | 🟢 95% |
| 5 | SHIPMENT_NUM | NUMBER | NOT NULL | Identificacao | Numero | — | 🟢 100% |
| 6 | QUANTITY | NUMBER | NULL | Quantidade | Quantidade | — | 🟢 100% |
| 7 | NEED_BY_DATE | DATE | NULL | Data | Data de necessidade | — | 🟢 100% |
| 8 | SHIP_TO_LOCATION_ID | NUMBER(18) | NULL | FK | Local de entrega | [[hr_locations]] | 🟢 100% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[po_headers_draft_all]] — via `PO_HEADER_ID`/`DRAFT_ID` (rascunho de PO do shipment draft)
- [[po_lines_draft_all]] — via `PO_LINE_ID` (linha draft à qual o shipment draft pertence)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Schedules de um draft
```sql
SELECT LINE_LOCATION_ID, SHIPMENT_NUM, QUANTITY, NEED_BY_DATE
FROM   PO_LINE_LOCATIONS_DRAFT_ALL
WHERE  PO_HEADER_ID = :p_header_id AND DRAFT_ID = :p_draft_id;
```

---

## 🔒 Observações

- Dados migram para `PO_LINE_LOCATIONS_ALL` apos aprovacao.

---

## 🔗 PVOs Relacionados

### [[draftpurchaseorderdistributionpvo|DraftPurchaseOrderDistributionPVO]] (PO · BICC: 38/268)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCRUE_ON_RECEIPT_FLAG | DraftShipmentAccrueOnReceiptFlag | ✅ |
| ACCRUE_ON_RECEIPT_FLAG | FromDraftShipmentAccrueOnReceiptFlag | — |
| ALLOW_SUBSTITUTE_RECEIPTS_FLAG | DraftShipmentAllowSubstituteReceiptsFlag | ✅ |
| ALLOW_SUBSTITUTE_RECEIPTS_FLAG | FromDraftShipmentAllowSubstituteReceiptsFlag | — |
| AMOUNT | DraftShipmentAmount | — |
| AMOUNT | FromDraftShipmentAmount | — |
| ASSESSABLE_VALUE | DraftShipmentAssessableValue | — |
| ASSESSABLE_VALUE | FromDraftShipmentAssessableValue | — |
| BACK_TO_BACK_FLAG | DraftShipmentBackToBackFlag | ✅ |
| BID_PAYMENT_ID | DraftShipmentBidPaymentId | — |
| BID_PAYMENT_ID | FromDraftShipmentBidPaymentId | — |
| CALCULATE_TAX_FLAG | DraftShipmentCalculateTaxFlag | — |
| CALCULATE_TAX_FLAG | FromDraftShipmentCalculateTaxFlag | — |
| CANCEL_BACKING_REQ_FLAG | DraftShipmentCancelBackingReqFlag | — |
| CANCEL_BACKING_REQ_FLAG | FromDraftShipmentCancelBackingReqFlag | — |
| CANCEL_BUDGET_DATE | DraftShipmentCancelBudgetDate | — |
| CANCEL_BUDGET_DATE | FromDraftShipmentCancelBudgetDate | — |
| CANCEL_DATE | DraftShipmentCancelDate | — |
| CANCEL_DATE | FromDraftShipmentCancelDate | — |
| CANCEL_FLAG | DraftShipmentCancelFlag | — |
| CANCEL_FLAG | FromDraftShipmentCancelFlag | — |
| CANCEL_REASON | DraftShipmentCancelReason | — |
| CANCEL_REASON | FromDraftShipmentCancelReason | — |
| CANCELLED_BY | DraftShipmentCancelledBy | — |
| CANCELLED_BY | FromDraftShipmentCancelledBy | — |
| CARRIER_ID | DraftShipmentCarrierId | — |
| CARRIER_ID | FromDraftShipmentCarrierId | — |
| CHANGE_ACCEPTED_FLAG | DraftShipmentChangeAcceptedFlag | — |
| CHANGE_ACCEPTED_FLAG | FromDraftShipmentChangeAcceptedFlag | — |
| CHANGE_PROMISED_DATE_REASON | DraftShipmentChangePromisedDateReason | — |
| CHANGE_PROMISED_DATE_REASON | FromDraftShipmentChangePromisedDateReason | — |
| CO_AMOUNT_CANCELLED | DraftShipmentCoAmountCancelled | — |
| CO_AMOUNT_CANCELLED | FromDraftShipmentCoAmountCancelled | — |
| CO_QUANTITY_CANCELLED | DraftShipmentCoQuantityCancelled | — |
| CO_QUANTITY_CANCELLED | FromDraftShipmentCoQuantityCancelled | — |
| CONSIGNED_FLAG | DraftShipmentConsignedFlag | — |
| CONSIGNED_FLAG | FromDraftShipmentConsignedFlag | — |
| COUNTRY_OF_ORIGIN_CODE | DraftShipmentCountryOfOriginCode | ✅ |
| COUNTRY_OF_ORIGIN_CODE | FromDraftShipmentCountryOfOriginCode | — |
| CREATED_BY | DraftShipmentCreatedBy | — |
| CREATED_BY | FromDraftShipmentCreatedBy | — |
| CREATION_DATE | DraftShipmentCreationDate | — |
| CREATION_DATE | FromDraftShipmentCreationDate | — |
| CUSTOMER_ITEM | DraftShipmentCustomerItem | — |
| CUSTOMER_ITEM_DESC | DraftShipmentCustomerItemDesc | — |
| CUSTOMER_PO_LINE_NUMBER | DraftShipmentCustomerPoLineNumber | — |
| CUSTOMER_PO_NUMBER | DraftShipmentCustomerPoNumber | — |
| CUSTOMER_PO_SCHEDULE_NUMBER | DraftShipmentCustomerPoScheduleNumber | — |
| DAYS_EARLY_RECEIPT_ALLOWED | DraftShipmentDaysEarlyReceiptAllowed | — |
| DAYS_EARLY_RECEIPT_ALLOWED | FromDraftShipmentDaysEarlyReceiptAllowed | — |
| DAYS_LATE_RECEIPT_ALLOWED | DraftShipmentDaysLateReceiptAllowed | ✅ |
| DAYS_LATE_RECEIPT_ALLOWED | FromDraftShipmentDaysLateReceiptAllowed | — |
| DESCRIPTION | DraftShipmentDescription | — |
| DESCRIPTION | FromDraftShipmentDescription | — |
| DESTINATION_TYPE_CODE | DraftShipmentDestinationTypeCode | ✅ |
| DESTINATION_TYPE_CODE | FromDraftShipmentDestinationTypeCode | — |
| DROP_SHIP_FLAG | DraftShipmentDropShipFlag | — |
| DROP_SHIP_FLAG | FromDraftShipmentDropShipFlag | — |
| ENCUMBER_NOW | DraftShipmentEncumberNow | — |
| ENCUMBER_NOW | FromDraftShipmentEncumberNow | — |
| ENCUMBERED_DATE | DraftShipmentEncumberedDate | — |
| ENCUMBERED_DATE | FromDraftShipmentEncumberedDate | — |
| ENCUMBERED_FLAG | DraftShipmentEncumberedFlag | — |
| ENCUMBERED_FLAG | FromDraftShipmentEncumberedFlag | — |
| END_DATE | DraftShipmentEndDate | — |
| END_DATE | FromDraftShipmentEndDate | — |
| ENFORCE_SHIP_TO_LOCATION_CODE | DraftShipmentEnforceShipToLocationCode | ✅ |
| ENFORCE_SHIP_TO_LOCATION_CODE | FromDraftShipmentEnforceShipToLocationCode | — |
| ENTITY_CHANGE_TYPE_CODE | DraftShipmentEntityChangeTypeCode | — |
| ENTITY_CHANGE_TYPE_CODE | FromDraftShipmentEntityChangeTypeCode | — |
| ESTIMATED_TAX_AMOUNT | DraftShipmentEstimatedTaxAmount | — |
| ESTIMATED_TAX_AMOUNT | FromDraftShipmentEstimatedTaxAmount | — |
| EXTERNAL_CHANGE_FLAG | DraftShipmentExternalChangeFlag | — |
| EXTERNAL_CHANGE_FLAG | FromDraftShipmentExternalChangeFlag | — |
| FIRM_DATE | DraftShipmentFirmDate | — |
| FIRM_DATE | FromDraftShipmentFirmDate | — |
| FIRM_STATUS_LOOKUP_CODE | DraftShipmentFirmStatusLookupCode | — |
| FIRM_STATUS_LOOKUP_CODE | FromDraftShipmentFirmStatusLookupCode | — |
| FOB_LOOKUP_CODE | DraftShipmentFobLookupCode | — |
| FOB_LOOKUP_CODE | FromDraftShipmentFobLookupCode | — |
| FREIGHT_TERMS_LOOKUP_CODE | DraftShipmentFreightTermsLookupCode | — |
| FREIGHT_TERMS_LOOKUP_CODE | FromDraftShipmentFreightTermsLookupCode | — |
| FROM_HEADER_ID | DraftShipmentFromHeaderId | — |
| FROM_HEADER_ID | FromDraftShipmentFromHeaderId | — |
| FROM_LINE_ID | DraftShipmentFromLineId | — |
| FROM_LINE_ID | FromDraftShipmentFromLineId | — |
| FROM_LINE_LOCATION_ID | DraftShipmentFromLineLocationId | — |
| FROM_LINE_LOCATION_ID | FromDraftShipmentFromLineLocationId | — |
| FUNDS_STATUS | DraftShipmentFundsStatus | ✅ |
| FUNDS_STATUS | FromDraftShipmentFundsStatus | — |
| GOVERNMENT_CONTEXT | DraftShipmentGovernmentContext | — |
| GOVERNMENT_CONTEXT | FromDraftShipmentGovernmentContext | — |
| GROUP_NAME | DraftShipmentGroupName | — |
| GROUP_NAME | FromDraftShipmentGroupName | — |
| INPUT_TAX_CLASSIFICATION_CODE | DraftShipmentInputTaxClassificationCode | ✅ |
| INPUT_TAX_CLASSIFICATION_CODE | FromDraftShipmentInputTaxClassificationCode | — |
| INSPECTION_REQUIRED_FLAG | DraftShipmentInspectionRequiredFlag | — |
| INSPECTION_REQUIRED_FLAG | FromDraftShipmentInspectionRequiredFlag | — |
| INVOICE_CLOSE_TOLERANCE | DraftShipmentInvoiceCloseTolerance | — |
| INVOICE_CLOSE_TOLERANCE | FromDraftShipmentInvoiceCloseTolerance | — |
| JOB_DEFINITION_NAME | DraftShipmentJobDefinitionName | — |
| JOB_DEFINITION_NAME | FromDraftShipmentJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | DraftShipmentJobDefinitionPackage | — |
| JOB_DEFINITION_PACKAGE | FromDraftShipmentJobDefinitionPackage | — |
| LAST_ACCEPT_DATE | DraftShipmentLastAcceptDate | ✅ |
| LAST_ACCEPT_DATE | FromDraftShipmentLastAcceptDate | — |
| LAST_UPDATE_DATE | DraftShipmentLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | FromDraftShipmentLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DraftShipmentLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | FromDraftShipmentLastUpdateLogin | — |
| LAST_UPDATED_BY | DraftShipmentLastUpdatedBy | — |
| LAST_UPDATED_BY | FromDraftShipmentLastUpdatedBy | — |
| LEAD_TIME | DraftShipmentLeadTime | — |
| LEAD_TIME | FromDraftShipmentLeadTime | — |
| LEAD_TIME_UNIT | DraftShipmentLeadTimeUnit | — |
| LEAD_TIME_UNIT | FromDraftShipmentLeadTimeUnit | — |
| LINE_INTENDED_USE | DraftShipmentLineIntendedUse | ✅ |
| LINE_INTENDED_USE | FromDraftShipmentLineIntendedUse | — |
| LINE_LOCATION_ID | DraftShipmentLineLocationId | ✅ |
| LINE_LOCATION_ID | FromDraftShipmentLineLocationId | — |
| MANUAL_PRICE_CHANGE_FLAG | DraftShipmentManualPriceChangeFlag | — |
| MANUAL_PRICE_CHANGE_FLAG | FromDraftShipmentManualPriceChangeFlag | — |
| MATCH_OPTION | DraftShipmentMatchOption | — |
| MATCH_OPTION | FromDraftShipmentMatchOption | — |
| MATCHING_BASIS | DraftShipmentMatchingBasis | — |
| MATCHING_BASIS | FromDraftShipmentMatchingBasis | — |
| MODE_OF_TRANSPORT | DraftShipmentModeOfTransport | ✅ |
| MODE_OF_TRANSPORT | FromDraftShipmentModeOfTransport | — |
| NEED_BY_DATE | DraftShipmentNeedByDate | ✅ |
| NEED_BY_DATE | FromDraftShipmentNeedByDate | — |
| NOTE_TO_RECEIVER | DraftShipmentNoteToReceiver | — |
| NOTE_TO_RECEIVER | FromDraftShipmentNoteToReceiver | — |
| OBJECT_VERSION_NUMBER | DraftShipmentObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | FromDraftShipmentObjectVersionNumber | — |
| OUTSOURCED_ASSEMBLY | DraftShipmentOutsourcedAssembly | — |
| OUTSOURCED_ASSEMBLY | FromDraftShipmentOutsourcedAssembly | — |
| PAYMENT_TYPE | DraftShipmentPaymentType | — |
| PAYMENT_TYPE | FromDraftShipmentPaymentType | — |
| PJC_CONTEXT_CATEGORY | DraftShipmentPjcContextCategory | — |
| PJC_CONTEXT_CATEGORY | FromDraftShipmentPjcContextCategory | — |
| PO_HEADER_ID | DraftShipmentPoHeaderId | — |
| PO_HEADER_ID | FromDraftShipmentPoHeaderId | — |
| PO_LINE_ID | DraftShipmentPoLineId | — |
| PO_LINE_ID | FromDraftShipmentPoLineId | — |
| PO_TRADING_ORGANIZATION_ID | DrafShipmentPoTradingOrganizationId | — |
| PO_TRADING_ORGANIZATION_ID | DraftShipmentPoTradingOrganizationId | — |
| PO_TRADING_ORGANIZATION_ID | FromDrafShipmentPoTradingOrganizationId | — |
| PO_TRADING_ORGANIZATION_ID | FromDraftShipmentPoTradingOrganizationId | — |
| PRC_BU_ID | DraftShipmentPrcBuId | — |
| PRC_BU_ID | FromDraftShipmentPrcBuId | — |
| PREFERRED_GRADE | DraftShipmentPreferredGrade | — |
| PREFERRED_GRADE | FromDraftShipmentPreferredGrade | — |
| PRICE_DISCOUNT | DraftShipmentPriceDiscount | — |
| PRICE_DISCOUNT | FromDraftShipmentPriceDiscount | — |
| PRICE_OVERRIDE | DraftShipmentPriceOverride | ✅ |
| PRICE_OVERRIDE | FromDraftShipmentPriceOverride | — |
| PRODUCT_CATEGORY | DraftShipmentProductCategory | ✅ |
| PRODUCT_CATEGORY | FromDraftShipmentProductCategory | — |
| PRODUCT_FISC_CLASSIFICATION | DraftShipmentProductFiscClassification | ✅ |
| PRODUCT_FISC_CLASSIFICATION | FromDraftShipmentProductFiscClassification | — |
| PRODUCT_TYPE | DraftShipmentProductType | ✅ |
| PRODUCT_TYPE | FromDraftShipmentProductType | — |
| PROGRAM_APP_NAME | DraftShipmentProgramAppName | — |
| PROGRAM_APP_NAME | FromDraftShipmentProgramAppName | — |
| PROGRAM_NAME | DraftShipmentProgramName | — |
| PROGRAM_NAME | FromDraftShipmentProgramName | — |
| PROMISED_DATE | DraftShipmentPromisedDate | ✅ |
| PROMISED_DATE | FromDraftShipmentPromisedDate | — |
| PROMISED_SHIP_DATE | DraftShipmentPromisedShipDate | ✅ |
| QTY_RCV_EXCEPTION_CODE | DraftShipmentQtyRcvExceptionCode | ✅ |
| QTY_RCV_EXCEPTION_CODE | FromDraftShipmentQtyRcvExceptionCode | — |
| QTY_RCV_TOLERANCE | DraftShipmentQtyRcvTolerance | — |
| QTY_RCV_TOLERANCE | FromDraftShipmentQtyRcvTolerance | — |
| QUANTITY | DraftShipmentQuantity | ✅ |
| QUANTITY | FromDraftShipmentQuantity | — |
| REASON_FOR_CHANGE | DraftShipmentReasonForChange | ✅ |
| REASON_FOR_CHANGE | FromDraftShipmentReasonForChange | — |
| RECEIPT_DAYS_EXCEPTION_CODE | DraftShipmentReceiptDaysExceptionCode | ✅ |
| RECEIPT_DAYS_EXCEPTION_CODE | FromDraftShipmentReceiptDaysExceptionCode | — |
| RECEIPT_REQUIRED_FLAG | DraftShipmentReceiptRequiredFlag | — |
| RECEIPT_REQUIRED_FLAG | FromDraftShipmentReceiptRequiredFlag | — |
| RECEIVE_CLOSE_TOLERANCE | DraftShipmentReceiveCloseTolerance | — |
| RECEIVE_CLOSE_TOLERANCE | FromDraftShipmentReceiveCloseTolerance | — |
| RECEIVING_ROUTING_ID | DraftShipmentReceivingRoutingId | — |
| RECEIVING_ROUTING_ID | FromDraftShipmentReceivingRoutingId | — |
| REJECTED_BY | DraftShipmentRejectedBy | — |
| REJECTED_BY | FromDraftShipmentRejectedBy | — |
| REJECTED_BY_ROLE | DraftShipmentRejectedByRole | — |
| REJECTED_BY_ROLE | FromDraftShipmentRejectedByRole | — |
| REJECTED_REASON | DraftShipmentRejectedReason | — |
| REJECTED_REASON | FromDraftShipmentRejectedReason | — |
| REQ_BU_ID | DraftShipmentReqBuId | — |
| REQ_BU_ID | FromDraftShipmentReqBuId | — |
| REQUEST_ID | DraftShipmentRequestId | — |
| REQUEST_ID | FromDraftShipmentRequestId | — |
| REQUESTED_SHIP_DATE | DraftShipmentRequestedShipDate | ✅ |
| RETROACTIVE_DATE | DraftShipmentRetroactiveDate | — |
| RETROACTIVE_DATE | FromDraftShipmentRetroactiveDate | — |
| SALES_ORDER_LINE_NUMBER | DraftShipmentSalesOrderLineNumber | — |
| SALES_ORDER_NUMBER | DraftShipmentSalesOrderNumber | ✅ |
| SALES_ORDER_SCHEDULE_NUMBER | DraftShipmentSalesOrderScheduleNumber | — |
| SALES_ORDER_UPDATE_DATE | DraftShipmentSalesOrderUpdateDate | — |
| SALES_ORDER_UPDATE_DATE | FromDraftShipmentSalesOrderUpdateDate | — |
| SECONDARY_QUANTITY | DraftShipmentSecondaryQuantity | — |
| SECONDARY_QUANTITY | FromDraftShipmentSecondaryQuantity | — |
| SECONDARY_UOM_CODE | DraftShipmentSecondaryUomCode | — |
| SECONDARY_UOM_CODE | FromDraftShipmentSecondaryUomCode | — |
| SERVICE_LEVEL | DraftShipmentServiceLevel | ✅ |
| SERVICE_LEVEL | FromDraftShipmentServiceLevel | — |
| SFO_AGREEMENT_LINE_NUMBER | DrafShipmentSfoAgreementLineNumber | — |
| SFO_AGREEMENT_LINE_NUMBER | DraftShipmentSfoAgreementLineNumber | — |
| SFO_AGREEMENT_LINE_NUMBER | FromDrafShipmentSfoAgreementLineNumber | — |
| SFO_AGREEMENT_LINE_NUMBER | FromDraftShipmentSfoAgreementLineNumber | — |
| SFO_AGREEMENT_NUMBER | DrafShipmentSfoAgreementNumber | ✅ |
| SFO_AGREEMENT_NUMBER | DraftShipmentSfoAgreementNumber | — |
| SFO_AGREEMENT_NUMBER | FromDrafShipmentSfoAgreementNumber | — |
| SFO_AGREEMENT_NUMBER | FromDraftShipmentSfoAgreementNumber | — |
| SFO_PTR_ID | DrafShipmentSfoPtrId | — |
| SFO_PTR_ID | DraftShipmentSfoPtrId | — |
| SFO_PTR_ID | FromDrafShipmentSfoPtrId | — |
| SFO_PTR_ID | FromDraftShipmentSfoPtrId | — |
| SHIP_TO_CUST_CONTACT_ID | DraftShipmentShipToCustContactId | — |
| SHIP_TO_CUST_ID | DraftShipmentShipToCustId | — |
| SHIP_TO_CUST_LOCATION_ID | DraftShipmentShipToCustLocationId | ✅ |
| SHIP_TO_LOCATION_ID | DraftShipmentShipToLocationId | ✅ |
| SHIP_TO_LOCATION_ID | FromDraftShipmentShipToLocationId | — |
| SHIP_TO_ORGANIZATION_ID | DraftShipmentShipToOrganizationId | — |
| SHIP_TO_ORGANIZATION_ID | FromDraftShipmentShipToOrganizationId | — |
| SHIPMENT_NUM | DraftShipmentShipmentNum | ✅ |
| SHIPMENT_NUM | FromDraftShipmentShipmentNum | — |
| SHIPMENT_TYPE | DraftShipmentShipmentType | — |
| SHIPMENT_TYPE | FromDraftShipmentShipmentType | — |
| SHIPPING_UOM_CODE | DraftShipmentShippingUomCode | ✅ |
| SHIPPING_UOM_QUANTITY | DraftShipmentUomQuantity | — |
| SOURCE_SHIPMENT_ID | DraftShipmentSourceShipmentId | — |
| SOURCE_SHIPMENT_ID | FromDraftShipmentSourceShipmentId | — |
| START_DATE | DraftShipmentStartDate | — |
| START_DATE | FromDraftShipmentStartDate | — |
| SUPPLIER_ORDER_LINE_NUMBER | DraftShipmentSupplierOrderLineNumber | ✅ |
| SUPPLIER_ORDER_LINE_NUMBER | FromDraftShipmentSupplierOrderLineNumber | — |
| TAX_ATTRIBUTE_UPDATE_CODE | DraftShipmentTaxAttributeUpdateCode | — |
| TAX_ATTRIBUTE_UPDATE_CODE | FromDraftShipmentTaxAttributeUpdateCode | — |
| TAX_CODE_ID | DraftShipmentTaxCodeId | — |
| TAX_CODE_ID | FromDraftShipmentTaxCodeId | — |
| TAX_NAME | DraftShipmentTaxName | — |
| TAX_NAME | FromDraftShipmentTaxName | — |
| TAX_USER_OVERRIDE_FLAG | DraftShipmentTaxUserOverrideFlag | — |
| TAX_USER_OVERRIDE_FLAG | FromDraftShipmentTaxUserOverrideFlag | — |
| TAXABLE_FLAG | DraftShipmentTaxableFlag | — |
| TAXABLE_FLAG | FromDraftShipmentTaxableFlag | — |
| TERMS_ID | DraftShipmentTermsId | — |
| TERMS_ID | FromDraftShipmentTermsId | — |
| TRANSACTION_FLOW_HEADER_ID | DraftShipmentTransactionFlowHeaderId | — |
| TRANSACTION_FLOW_HEADER_ID | FromDraftShipmentTransactionFlowHeaderId | — |
| TRX_BUSINESS_CATEGORY | DraftShipmentTrxBusinessCategory | ✅ |
| TRX_BUSINESS_CATEGORY | FromDraftShipmentTrxBusinessCategory | — |
| UNENCUMBERED_QUANTITY | DraftShipmentUnencumberedQuantity | — |
| UNENCUMBERED_QUANTITY | FromDraftShipmentUnencumberedQuantity | — |
| UNIT_OF_MEASURE_CLASS | DraftShipmentUnitOfMeasureClass | — |
| UNIT_OF_MEASURE_CLASS | FromDraftShipmentUnitOfMeasureClass | — |
| UOM_CODE | DraftShipmentUomCode | ✅ |
| UOM_CODE | FromDraftShipmentUomCode | — |
| USER_DEFINED_FISC_CLASS | DraftShipmentUserDefinedFiscClass | ✅ |
| USER_DEFINED_FISC_CLASS | FromDraftShipmentUserDefinedFiscClass | — |
| VALUE_BASIS | DraftShipmentValueBasis | — |
| VALUE_BASIS | FromDraftShipmentValueBasis | — |
| VMI_FLAG | DraftShipmentVmiFlag | — |
| VMI_FLAG | FromDraftShipmentVmiFlag | — |

### [[draftpurchaseorderdistributionrefpvo|DraftPurchaseOrderDistributionRefPVO]] (PO · BICC: 3/268)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCRUE_ON_RECEIPT_FLAG | DraftShipmentAccrueOnReceiptFlag | — |
| ACCRUE_ON_RECEIPT_FLAG | FromDraftShipmentAccrueOnReceiptFlag | — |
| ALLOW_SUBSTITUTE_RECEIPTS_FLAG | DraftShipmentAllowSubstituteReceiptsFlag | — |
| ALLOW_SUBSTITUTE_RECEIPTS_FLAG | FromDraftShipmentAllowSubstituteReceiptsFlag | — |
| AMOUNT | DraftShipmentAmount | — |
| AMOUNT | FromDraftShipmentAmount | — |
| ASSESSABLE_VALUE | DraftShipmentAssessableValue | — |
| ASSESSABLE_VALUE | FromDraftShipmentAssessableValue | — |
| BACK_TO_BACK_FLAG | DraftShipmentBackToBackFlag | — |
| BID_PAYMENT_ID | DraftShipmentBidPaymentId | — |
| BID_PAYMENT_ID | FromDraftShipmentBidPaymentId | — |
| CALCULATE_TAX_FLAG | DraftShipmentCalculateTaxFlag | — |
| CALCULATE_TAX_FLAG | FromDraftShipmentCalculateTaxFlag | — |
| CANCEL_BACKING_REQ_FLAG | DraftShipmentCancelBackingReqFlag | — |
| CANCEL_BACKING_REQ_FLAG | FromDraftShipmentCancelBackingReqFlag | — |
| CANCEL_BUDGET_DATE | DraftShipmentCancelBudgetDate | — |
| CANCEL_BUDGET_DATE | FromDraftShipmentCancelBudgetDate | — |
| CANCEL_DATE | DraftShipmentCancelDate | — |
| CANCEL_DATE | FromDraftShipmentCancelDate | — |
| CANCEL_FLAG | DraftShipmentCancelFlag | — |
| CANCEL_FLAG | FromDraftShipmentCancelFlag | — |
| CANCEL_REASON | DraftShipmentCancelReason | — |
| CANCEL_REASON | FromDraftShipmentCancelReason | — |
| CANCELLED_BY | DraftShipmentCancelledBy | — |
| CANCELLED_BY | FromDraftShipmentCancelledBy | — |
| CARRIER_ID | DraftShipmentCarrierId | — |
| CARRIER_ID | FromDraftShipmentCarrierId | — |
| CHANGE_ACCEPTED_FLAG | DraftShipmentChangeAcceptedFlag | — |
| CHANGE_ACCEPTED_FLAG | FromDraftShipmentChangeAcceptedFlag | — |
| CHANGE_PROMISED_DATE_REASON | DraftShipmentChangePromisedDateReason | — |
| CHANGE_PROMISED_DATE_REASON | FromDraftShipmentChangePromisedDateReason | — |
| CO_AMOUNT_CANCELLED | DraftShipmentCoAmountCancelled | — |
| CO_AMOUNT_CANCELLED | FromDraftShipmentCoAmountCancelled | — |
| CO_QUANTITY_CANCELLED | DraftShipmentCoQuantityCancelled | — |
| CO_QUANTITY_CANCELLED | FromDraftShipmentCoQuantityCancelled | — |
| CONSIGNED_FLAG | DraftShipmentConsignedFlag | — |
| CONSIGNED_FLAG | FromDraftShipmentConsignedFlag | — |
| COUNTRY_OF_ORIGIN_CODE | DraftShipmentCountryOfOriginCode | — |
| COUNTRY_OF_ORIGIN_CODE | FromDraftShipmentCountryOfOriginCode | — |
| CREATED_BY | DraftShipmentCreatedBy | — |
| CREATED_BY | FromDraftShipmentCreatedBy | — |
| CREATION_DATE | DraftShipmentCreationDate | — |
| CREATION_DATE | FromDraftShipmentCreationDate | — |
| CUSTOMER_ITEM | DraftShipmentCustomerItem | — |
| CUSTOMER_ITEM_DESC | DraftShipmentCustomerItemDesc | — |
| CUSTOMER_PO_LINE_NUMBER | DraftShipmentCustomerPoLineNumber | — |
| CUSTOMER_PO_NUMBER | DraftShipmentCustomerPoNumber | — |
| CUSTOMER_PO_SCHEDULE_NUMBER | DraftShipmentCustomerPoScheduleNumber | — |
| DAYS_EARLY_RECEIPT_ALLOWED | DraftShipmentDaysEarlyReceiptAllowed | — |
| DAYS_EARLY_RECEIPT_ALLOWED | FromDraftShipmentDaysEarlyReceiptAllowed | — |
| DAYS_LATE_RECEIPT_ALLOWED | DraftShipmentDaysLateReceiptAllowed | — |
| DAYS_LATE_RECEIPT_ALLOWED | FromDraftShipmentDaysLateReceiptAllowed | — |
| DESCRIPTION | DraftShipmentDescription | — |
| DESCRIPTION | FromDraftShipmentDescription | — |
| DESTINATION_TYPE_CODE | DraftShipmentDestinationTypeCode | — |
| DESTINATION_TYPE_CODE | FromDraftShipmentDestinationTypeCode | — |
| DROP_SHIP_FLAG | DraftShipmentDropShipFlag | — |
| DROP_SHIP_FLAG | FromDraftShipmentDropShipFlag | — |
| ENCUMBER_NOW | DraftShipmentEncumberNow | — |
| ENCUMBER_NOW | FromDraftShipmentEncumberNow | — |
| ENCUMBERED_DATE | DraftShipmentEncumberedDate | — |
| ENCUMBERED_DATE | FromDraftShipmentEncumberedDate | — |
| ENCUMBERED_FLAG | DraftShipmentEncumberedFlag | — |
| ENCUMBERED_FLAG | FromDraftShipmentEncumberedFlag | — |
| END_DATE | DraftShipmentEndDate | — |
| END_DATE | FromDraftShipmentEndDate | — |
| ENFORCE_SHIP_TO_LOCATION_CODE | DraftShipmentEnforceShipToLocationCode | — |
| ENFORCE_SHIP_TO_LOCATION_CODE | FromDraftShipmentEnforceShipToLocationCode | — |
| ENTITY_CHANGE_TYPE_CODE | DraftShipmentEntityChangeTypeCode | — |
| ENTITY_CHANGE_TYPE_CODE | FromDraftShipmentEntityChangeTypeCode | — |
| ESTIMATED_TAX_AMOUNT | DraftShipmentEstimatedTaxAmount | — |
| ESTIMATED_TAX_AMOUNT | FromDraftShipmentEstimatedTaxAmount | — |
| EXTERNAL_CHANGE_FLAG | DraftShipmentExternalChangeFlag | — |
| EXTERNAL_CHANGE_FLAG | FromDraftShipmentExternalChangeFlag | — |
| FIRM_DATE | DraftShipmentFirmDate | — |
| FIRM_DATE | FromDraftShipmentFirmDate | — |
| FIRM_STATUS_LOOKUP_CODE | DraftShipmentFirmStatusLookupCode | — |
| FIRM_STATUS_LOOKUP_CODE | FromDraftShipmentFirmStatusLookupCode | — |
| FOB_LOOKUP_CODE | DraftShipmentFobLookupCode | — |
| FOB_LOOKUP_CODE | FromDraftShipmentFobLookupCode | — |
| FREIGHT_TERMS_LOOKUP_CODE | DraftShipmentFreightTermsLookupCode | — |
| FREIGHT_TERMS_LOOKUP_CODE | FromDraftShipmentFreightTermsLookupCode | — |
| FROM_HEADER_ID | DraftShipmentFromHeaderId | — |
| FROM_HEADER_ID | FromDraftShipmentFromHeaderId | — |
| FROM_LINE_ID | DraftShipmentFromLineId | — |
| FROM_LINE_ID | FromDraftShipmentFromLineId | — |
| FROM_LINE_LOCATION_ID | DraftShipmentFromLineLocationId | — |
| FROM_LINE_LOCATION_ID | FromDraftShipmentFromLineLocationId | — |
| FUNDS_STATUS | DraftShipmentFundsStatus | — |
| FUNDS_STATUS | FromDraftShipmentFundsStatus | — |
| GOVERNMENT_CONTEXT | DraftShipmentGovernmentContext | — |
| GOVERNMENT_CONTEXT | FromDraftShipmentGovernmentContext | — |
| GROUP_NAME | DraftShipmentGroupName | — |
| GROUP_NAME | FromDraftShipmentGroupName | — |
| INPUT_TAX_CLASSIFICATION_CODE | DraftShipmentInputTaxClassificationCode | — |
| INPUT_TAX_CLASSIFICATION_CODE | FromDraftShipmentInputTaxClassificationCode | — |
| INSPECTION_REQUIRED_FLAG | DraftShipmentInspectionRequiredFlag | — |
| INSPECTION_REQUIRED_FLAG | FromDraftShipmentInspectionRequiredFlag | — |
| INVOICE_CLOSE_TOLERANCE | DraftShipmentInvoiceCloseTolerance | — |
| INVOICE_CLOSE_TOLERANCE | FromDraftShipmentInvoiceCloseTolerance | — |
| JOB_DEFINITION_NAME | DraftShipmentJobDefinitionName | — |
| JOB_DEFINITION_NAME | FromDraftShipmentJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | DraftShipmentJobDefinitionPackage | — |
| JOB_DEFINITION_PACKAGE | FromDraftShipmentJobDefinitionPackage | — |
| LAST_ACCEPT_DATE | DraftShipmentLastAcceptDate | — |
| LAST_ACCEPT_DATE | FromDraftShipmentLastAcceptDate | — |
| LAST_UPDATE_DATE | DraftShipmentLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | FromDraftShipmentLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DraftShipmentLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | FromDraftShipmentLastUpdateLogin | — |
| LAST_UPDATED_BY | DraftShipmentLastUpdatedBy | — |
| LAST_UPDATED_BY | FromDraftShipmentLastUpdatedBy | — |
| LEAD_TIME | DraftShipmentLeadTime | — |
| LEAD_TIME | FromDraftShipmentLeadTime | — |
| LEAD_TIME_UNIT | DraftShipmentLeadTimeUnit | — |
| LEAD_TIME_UNIT | FromDraftShipmentLeadTimeUnit | — |
| LINE_INTENDED_USE | DraftShipmentLineIntendedUse | — |
| LINE_INTENDED_USE | FromDraftShipmentLineIntendedUse | — |
| LINE_LOCATION_ID | DraftShipmentLineLocationId | — |
| LINE_LOCATION_ID | FromDraftShipmentLineLocationId | — |
| MANUAL_PRICE_CHANGE_FLAG | DraftShipmentManualPriceChangeFlag | — |
| MANUAL_PRICE_CHANGE_FLAG | FromDraftShipmentManualPriceChangeFlag | — |
| MATCH_OPTION | DraftShipmentMatchOption | — |
| MATCH_OPTION | FromDraftShipmentMatchOption | — |
| MATCHING_BASIS | DraftShipmentMatchingBasis | — |
| MATCHING_BASIS | FromDraftShipmentMatchingBasis | — |
| MODE_OF_TRANSPORT | DraftShipmentModeOfTransport | — |
| MODE_OF_TRANSPORT | FromDraftShipmentModeOfTransport | — |
| NEED_BY_DATE | DraftShipmentNeedByDate | — |
| NEED_BY_DATE | FromDraftShipmentNeedByDate | — |
| NOTE_TO_RECEIVER | DraftShipmentNoteToReceiver | — |
| NOTE_TO_RECEIVER | FromDraftShipmentNoteToReceiver | — |
| OBJECT_VERSION_NUMBER | DraftShipmentObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | FromDraftShipmentObjectVersionNumber | — |
| OUTSOURCED_ASSEMBLY | DraftShipmentOutsourcedAssembly | — |
| OUTSOURCED_ASSEMBLY | FromDraftShipmentOutsourcedAssembly | — |
| PAYMENT_TYPE | DraftShipmentPaymentType | — |
| PAYMENT_TYPE | FromDraftShipmentPaymentType | — |
| PJC_CONTEXT_CATEGORY | DraftShipmentPjcContextCategory | — |
| PJC_CONTEXT_CATEGORY | FromDraftShipmentPjcContextCategory | — |
| PO_HEADER_ID | DraftShipmentPoHeaderId | — |
| PO_HEADER_ID | FromDraftShipmentPoHeaderId | — |
| PO_LINE_ID | DraftShipmentPoLineId | — |
| PO_LINE_ID | FromDraftShipmentPoLineId | — |
| PO_TRADING_ORGANIZATION_ID | DrafShipmentPoTradingOrganizationId | — |
| PO_TRADING_ORGANIZATION_ID | DraftShipmentPoTradingOrganizationId | — |
| PO_TRADING_ORGANIZATION_ID | FromDrafShipmentPoTradingOrganizationId | — |
| PO_TRADING_ORGANIZATION_ID | FromDraftShipmentPoTradingOrganizationId | — |
| PRC_BU_ID | DraftShipmentPrcBuId | — |
| PRC_BU_ID | FromDraftShipmentPrcBuId | — |
| PREFERRED_GRADE | DraftShipmentPreferredGrade | — |
| PREFERRED_GRADE | FromDraftShipmentPreferredGrade | — |
| PRICE_DISCOUNT | DraftShipmentPriceDiscount | — |
| PRICE_DISCOUNT | FromDraftShipmentPriceDiscount | — |
| PRICE_OVERRIDE | DraftShipmentPriceOverride | — |
| PRICE_OVERRIDE | FromDraftShipmentPriceOverride | — |
| PRODUCT_CATEGORY | DraftShipmentProductCategory | — |
| PRODUCT_CATEGORY | FromDraftShipmentProductCategory | — |
| PRODUCT_FISC_CLASSIFICATION | DraftShipmentProductFiscClassification | — |
| PRODUCT_FISC_CLASSIFICATION | FromDraftShipmentProductFiscClassification | — |
| PRODUCT_TYPE | DraftShipmentProductType | — |
| PRODUCT_TYPE | FromDraftShipmentProductType | — |
| PROGRAM_APP_NAME | DraftShipmentProgramAppName | — |
| PROGRAM_APP_NAME | FromDraftShipmentProgramAppName | — |
| PROGRAM_NAME | DraftShipmentProgramName | — |
| PROGRAM_NAME | FromDraftShipmentProgramName | — |
| PROMISED_DATE | DraftShipmentPromisedDate | — |
| PROMISED_DATE | FromDraftShipmentPromisedDate | — |
| PROMISED_SHIP_DATE | DraftShipmentPromisedShipDate | — |
| QTY_RCV_EXCEPTION_CODE | DraftShipmentQtyRcvExceptionCode | — |
| QTY_RCV_EXCEPTION_CODE | FromDraftShipmentQtyRcvExceptionCode | — |
| QTY_RCV_TOLERANCE | DraftShipmentQtyRcvTolerance | — |
| QTY_RCV_TOLERANCE | FromDraftShipmentQtyRcvTolerance | — |
| QUANTITY | DraftShipmentQuantity | — |
| QUANTITY | FromDraftShipmentQuantity | — |
| REASON_FOR_CHANGE | DraftShipmentReasonForChange | — |
| REASON_FOR_CHANGE | FromDraftShipmentReasonForChange | — |
| RECEIPT_DAYS_EXCEPTION_CODE | DraftShipmentReceiptDaysExceptionCode | — |
| RECEIPT_DAYS_EXCEPTION_CODE | FromDraftShipmentReceiptDaysExceptionCode | — |
| RECEIPT_REQUIRED_FLAG | DraftShipmentReceiptRequiredFlag | — |
| RECEIPT_REQUIRED_FLAG | FromDraftShipmentReceiptRequiredFlag | — |
| RECEIVE_CLOSE_TOLERANCE | DraftShipmentReceiveCloseTolerance | — |
| RECEIVE_CLOSE_TOLERANCE | FromDraftShipmentReceiveCloseTolerance | — |
| RECEIVING_ROUTING_ID | DraftShipmentReceivingRoutingId | — |
| RECEIVING_ROUTING_ID | FromDraftShipmentReceivingRoutingId | — |
| REJECTED_BY | DraftShipmentRejectedBy | — |
| REJECTED_BY | FromDraftShipmentRejectedBy | — |
| REJECTED_BY_ROLE | DraftShipmentRejectedByRole | — |
| REJECTED_BY_ROLE | FromDraftShipmentRejectedByRole | — |
| REJECTED_REASON | DraftShipmentRejectedReason | — |
| REJECTED_REASON | FromDraftShipmentRejectedReason | — |
| REQ_BU_ID | DraftShipmentReqBuId | — |
| REQ_BU_ID | FromDraftShipmentReqBuId | — |
| REQUEST_ID | DraftShipmentRequestId | — |
| REQUEST_ID | FromDraftShipmentRequestId | — |
| REQUESTED_SHIP_DATE | DraftShipmentRequestedShipDate | — |
| RETROACTIVE_DATE | DraftShipmentRetroactiveDate | — |
| RETROACTIVE_DATE | FromDraftShipmentRetroactiveDate | — |
| SALES_ORDER_LINE_NUMBER | DraftShipmentSalesOrderLineNumber | — |
| SALES_ORDER_NUMBER | DraftShipmentSalesOrderNumber | — |
| SALES_ORDER_SCHEDULE_NUMBER | DraftShipmentSalesOrderScheduleNumber | — |
| SALES_ORDER_UPDATE_DATE | DraftShipmentSalesOrderUpdateDate | — |
| SALES_ORDER_UPDATE_DATE | FromDraftShipmentSalesOrderUpdateDate | — |
| SECONDARY_QUANTITY | DraftShipmentSecondaryQuantity | — |
| SECONDARY_QUANTITY | FromDraftShipmentSecondaryQuantity | — |
| SECONDARY_UOM_CODE | DraftShipmentSecondaryUomCode | — |
| SECONDARY_UOM_CODE | FromDraftShipmentSecondaryUomCode | — |
| SERVICE_LEVEL | DraftShipmentServiceLevel | — |
| SERVICE_LEVEL | FromDraftShipmentServiceLevel | — |
| SFO_AGREEMENT_LINE_NUMBER | DrafShipmentSfoAgreementLineNumber | — |
| SFO_AGREEMENT_LINE_NUMBER | DraftShipmentSfoAgreementLineNumber | — |
| SFO_AGREEMENT_LINE_NUMBER | FromDrafShipmentSfoAgreementLineNumber | — |
| SFO_AGREEMENT_LINE_NUMBER | FromDraftShipmentSfoAgreementLineNumber | — |
| SFO_AGREEMENT_NUMBER | DrafShipmentSfoAgreementNumber | — |
| SFO_AGREEMENT_NUMBER | DraftShipmentSfoAgreementNumber | — |
| SFO_AGREEMENT_NUMBER | FromDrafShipmentSfoAgreementNumber | — |
| SFO_AGREEMENT_NUMBER | FromDraftShipmentSfoAgreementNumber | — |
| SFO_PTR_ID | DrafShipmentSfoPtrId | — |
| SFO_PTR_ID | DraftShipmentSfoPtrId | — |
| SFO_PTR_ID | FromDrafShipmentSfoPtrId | — |
| SFO_PTR_ID | FromDraftShipmentSfoPtrId | — |
| SHIP_TO_CUST_CONTACT_ID | DraftShipmentShipToCustContactId | — |
| SHIP_TO_CUST_ID | DraftShipmentShipToCustId | — |
| SHIP_TO_CUST_LOCATION_ID | DraftShipmentShipToCustLocationId | — |
| SHIP_TO_LOCATION_ID | DraftShipmentShipToLocationId | — |
| SHIP_TO_LOCATION_ID | FromDraftShipmentShipToLocationId | — |
| SHIP_TO_ORGANIZATION_ID | DraftShipmentShipToOrganizationId | — |
| SHIP_TO_ORGANIZATION_ID | FromDraftShipmentShipToOrganizationId | — |
| SHIPMENT_NUM | DraftShipmentShipmentNum | ✅ |
| SHIPMENT_NUM | FromDraftShipmentShipmentNum | — |
| SHIPMENT_TYPE | DraftShipmentShipmentType | — |
| SHIPMENT_TYPE | FromDraftShipmentShipmentType | — |
| SHIPPING_UOM_CODE | DraftShipmentShippingUomCode | — |
| SHIPPING_UOM_QUANTITY | DraftShipmentUomQuantity | — |
| SOURCE_SHIPMENT_ID | DraftShipmentSourceShipmentId | — |
| SOURCE_SHIPMENT_ID | FromDraftShipmentSourceShipmentId | — |
| START_DATE | DraftShipmentStartDate | — |
| START_DATE | FromDraftShipmentStartDate | — |
| SUPPLIER_ORDER_LINE_NUMBER | DraftShipmentSupplierOrderLineNumber | — |
| SUPPLIER_ORDER_LINE_NUMBER | FromDraftShipmentSupplierOrderLineNumber | — |
| TAX_ATTRIBUTE_UPDATE_CODE | DraftShipmentTaxAttributeUpdateCode | — |
| TAX_ATTRIBUTE_UPDATE_CODE | FromDraftShipmentTaxAttributeUpdateCode | — |
| TAX_CODE_ID | DraftShipmentTaxCodeId | — |
| TAX_CODE_ID | FromDraftShipmentTaxCodeId | — |
| TAX_NAME | DraftShipmentTaxName | — |
| TAX_NAME | FromDraftShipmentTaxName | — |
| TAX_USER_OVERRIDE_FLAG | DraftShipmentTaxUserOverrideFlag | — |
| TAX_USER_OVERRIDE_FLAG | FromDraftShipmentTaxUserOverrideFlag | — |
| TAXABLE_FLAG | DraftShipmentTaxableFlag | — |
| TAXABLE_FLAG | FromDraftShipmentTaxableFlag | — |
| TERMS_ID | DraftShipmentTermsId | — |
| TERMS_ID | FromDraftShipmentTermsId | — |
| TRANSACTION_FLOW_HEADER_ID | DraftShipmentTransactionFlowHeaderId | — |
| TRANSACTION_FLOW_HEADER_ID | FromDraftShipmentTransactionFlowHeaderId | — |
| TRX_BUSINESS_CATEGORY | DraftShipmentTrxBusinessCategory | — |
| TRX_BUSINESS_CATEGORY | FromDraftShipmentTrxBusinessCategory | — |
| UNENCUMBERED_QUANTITY | DraftShipmentUnencumberedQuantity | — |
| UNENCUMBERED_QUANTITY | FromDraftShipmentUnencumberedQuantity | — |
| UNIT_OF_MEASURE_CLASS | DraftShipmentUnitOfMeasureClass | — |
| UNIT_OF_MEASURE_CLASS | FromDraftShipmentUnitOfMeasureClass | — |
| UOM_CODE | DraftShipmentUomCode | — |
| UOM_CODE | FromDraftShipmentUomCode | — |
| USER_DEFINED_FISC_CLASS | DraftShipmentUserDefinedFiscClass | — |
| USER_DEFINED_FISC_CLASS | FromDraftShipmentUserDefinedFiscClass | — |
| VALUE_BASIS | DraftShipmentValueBasis | — |
| VALUE_BASIS | FromDraftShipmentValueBasis | — |
| VMI_FLAG | DraftShipmentVmiFlag | — |
| VMI_FLAG | FromDraftShipmentVmiFlag | — |

### [[draftpurchasingdocumentlinelocationextractpvo|DraftPurchasingDocumentLineLocationExtractPVO]] (PO · BICC: 140/142)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCRUE_ON_RECEIPT_FLAG | AccrueOnReceiptFlag | ✅ |
| ALLOW_SUBSTITUTE_RECEIPTS_FLAG | AllowSubstituteReceiptsFlag | ✅ |
| AMOUNT | Amount | ✅ |
| ASSESSABLE_VALUE | AssessableValue | ✅ |
| BACK_TO_BACK_FLAG | BackToBackFlag | ✅ |
| BID_PAYMENT_ID | BidPaymentId | ✅ |
| CALCULATE_TAX_FLAG | CalculateTaxFlag | ✅ |
| CANCEL_BACKING_REQ_FLAG | CancelBackingReqFlag | ✅ |
| CANCEL_BUDGET_DATE | CancelBudgetDate | ✅ |
| CANCEL_DATE | CancelDate | ✅ |
| CANCEL_FLAG | CancelFlag | ✅ |
| CANCEL_REASON | CancelReason | ✅ |
| CANCELLED_BY | CancelledBy | ✅ |
| CARRIER_ID | CarrierId | ✅ |
| CHANGE_ACCEPTED_FLAG | ChangeAcceptedFlag | ✅ |
| CHANGE_PROMISED_DATE_REASON | ChangePromisedDateReason | ✅ |
| CO_AMOUNT_CANCELLED | CoAmountCancelled | ✅ |
| CO_QUANTITY_CANCELLED | CoQuantityCancelled | ✅ |
| CONSIGNED_FLAG | ConsignedFlag | ✅ |
| COUNTRY_OF_ORIGIN_CODE | CountryOfOriginCode | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| CUSTOMER_ITEM | CustomerItem | ✅ |
| CUSTOMER_ITEM_DESC | CustomerItemDesc | ✅ |
| CUSTOMER_PO_LINE_NUMBER | CustomerPoLineNumber | ✅ |
| CUSTOMER_PO_NUMBER | CustomerPoNumber | ✅ |
| CUSTOMER_PO_SCHEDULE_NUMBER | CustomerPoScheduleNumber | ✅ |
| DAYS_EARLY_RECEIPT_ALLOWED | DaysEarlyReceiptAllowed | ✅ |
| DAYS_LATE_RECEIPT_ALLOWED | DaysLateReceiptAllowed | ✅ |
| DESCRIPTION | Description | ✅ |
| DESTINATION_TYPE_CODE | DestinationTypeCode | ✅ |
| DROP_SHIP_FLAG | DropShipFlag | ✅ |
| ENCUMBERED_DATE | EncumberedDate | ✅ |
| ENCUMBERED_FLAG | EncumberedFlag | ✅ |
| END_DATE | EndDate | ✅ |
| ENFORCE_SHIP_TO_LOCATION_CODE | EnforceShipToLocationCode | ✅ |
| ENTITY_CHANGE_TYPE_CODE | EntityChangeTypeCode | ✅ |
| EXTERNAL_CHANGE_FLAG | ExternalChangeFlag | ✅ |
| FINAL_DISCHARGE_LOCATION_ID | FinalDischargeLocationId | — |
| FIRM_DATE | FirmDate | ✅ |
| FIRM_STATUS_LOOKUP_CODE | FirmStatusLookupCode | ✅ |
| FOB_LOOKUP_CODE | FobLookupCode | ✅ |
| FREIGHT_TERMS_LOOKUP_CODE | FreightTermsLookupCode | ✅ |
| FROM_HEADER_ID | FromHeaderId | ✅ |
| FROM_LINE_ID | FromLineId | ✅ |
| FROM_LINE_LOCATION_ID | FromLineLocationId | ✅ |
| FUNDS_STATUS | FundsStatus | ✅ |
| INPUT_TAX_CLASSIFICATION_CODE | InputTaxClassificationCode | ✅ |
| INSPECTION_REQUIRED_FLAG | InspectionRequiredFlag | ✅ |
| INVOICE_CLOSE_TOLERANCE | InvoiceCloseTolerance | ✅ |
| JOB_DEFINITION_NAME | JobDefinitionName | ✅ |
| JOB_DEFINITION_PACKAGE | JobDefinitionPackage | ✅ |
| LAST_ACCEPT_DATE | LastAcceptDate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LEAD_TIME | LeadTime | ✅ |
| LEAD_TIME_UNIT | LeadTimeUnit | ✅ |
| LINE_INTENDED_USE | LineIntendedUse | ✅ |
| LINE_INTENDED_USE_ID | LineIntendedUseId | ✅ |
| LINE_LOCATION_ID | LineLocationId | ✅ |
| MANUAL_PRICE_CHANGE_FLAG | ManualPriceChangeFlag | ✅ |
| MATCH_OPTION | MatchOption | ✅ |
| MATCHING_BASIS | MatchingBasis | ✅ |
| MODE_OF_TRANSPORT | ModeOfTransport | ✅ |
| NEED_BY_DATE | NeedByDate | ✅ |
| NOTE_TO_RECEIVER | NoteToReceiver | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| ORIGINAL_SHIPMENT_ID | OriginalShipmentId | ✅ |
| OUTSOURCED_ASSEMBLY | OutsourcedAssembly | ✅ |
| PAYMENT_TYPE | PaymentType | ✅ |
| PJC_CONTEXT_CATEGORY | PjcContextCategory | ✅ |
| PO_HEADER_ID | PoHeaderId | ✅ |
| PO_LINE_ID | PoLineId | ✅ |
| PO_TRADING_ORGANIZATION_ID | PoTradingOrganizationId | ✅ |
| PRC_BU_ID | PrcBuId | ✅ |
| PREFERRED_GRADE | PreferredGrade | ✅ |
| PRICE_DISCOUNT | PriceDiscount | ✅ |
| PRICE_OVERRIDE | PriceOverride | ✅ |
| PRODUCT_CATEGORY | ProductCategory | ✅ |
| PRODUCT_FISC_CLASS_ID | ProductFiscClassId | ✅ |
| PRODUCT_FISC_CLASSIFICATION | ProductFiscClassification | ✅ |
| PRODUCT_TYPE | ProductType | ✅ |
| PROGRAM_APP_NAME | ProgramAppName | ✅ |
| PROGRAM_NAME | ProgramName | ✅ |
| PROMISED_DATE | PromisedDate | ✅ |
| PROMISED_SHIP_DATE | PromisedShipDate | ✅ |
| QTY_RCV_EXCEPTION_CODE | QtyRcvExceptionCode | ✅ |
| QTY_RCV_TOLERANCE | QtyRcvTolerance | ✅ |
| QUANTITY | Quantity | ✅ |
| REASON_FOR_CHANGE | ReasonForChange | ✅ |
| RECEIPT_DAYS_EXCEPTION_CODE | ReceiptDaysExceptionCode | ✅ |
| RECEIPT_REQUIRED_FLAG | ReceiptRequiredFlag | ✅ |
| RECEIVE_CLOSE_TOLERANCE | ReceiveCloseTolerance | ✅ |
| RECEIVING_ROUTING_ID | ReceivingRoutingId | ✅ |
| REJECTED_BY | RejectedBy | ✅ |
| REJECTED_BY_ROLE | RejectedByRole | ✅ |
| REJECTED_REASON | RejectedReason | ✅ |
| REQ_BU_ID | ReqBuId | ✅ |
| REQUEST_ID | RequestId | ✅ |
| REQUESTED_SHIP_DATE | RequestedShipDate | ✅ |
| RETAINAGE_RATE | RetainageRate | ✅ |
| RETROACTIVE_DATE | RetroactiveDate | ✅ |
| SALES_ORDER_LINE_NUMBER | SalesOrderLineNumber | ✅ |
| SALES_ORDER_NUMBER | SalesOrderNumber | ✅ |
| SALES_ORDER_SCHEDULE_NUMBER | SalesOrderScheduleNumber | ✅ |
| SALES_ORDER_UPDATE_DATE | SalesOrderUpdateDate | ✅ |
| SECONDARY_QUANTITY | SecondaryQuantity | ✅ |
| SECONDARY_UOM_CODE | SecondaryUomCode | ✅ |
| SERVICE_LEVEL | ServiceLevel | ✅ |
| SFO_AGREEMENT_LINE_NUMBER | SfoAgreementLineNumber | ✅ |
| SFO_AGREEMENT_NUMBER | SfoAgreementNumber | ✅ |
| SFO_PTR_ID | SfoPtrId | ✅ |
| SHIP_TO_CUST_CONTACT_ID | ShipToCustContactId | ✅ |
| SHIP_TO_CUST_ID | ShipToCustId | ✅ |
| SHIP_TO_CUST_LOCATION_ID | ShipToCustLocationId | ✅ |
| SHIP_TO_LOCATION_ID | ShipToLocationId | ✅ |
| SHIP_TO_ORGANIZATION_ID | ShipToOrganizationId | ✅ |
| SHIPMENT_NUM | ShipmentNum | ✅ |
| SHIPMENT_TYPE | ShipmentType | ✅ |
| SHIPPING_UOM_CODE | ShippingUomCode | ✅ |
| SHIPPING_UOM_QUANTITY | ShippingUomQuantity | ✅ |
| SOURCE_SHIPMENT_ID | SourceShipmentId | ✅ |
| START_DATE | StartDate | ✅ |
| SUPPLIER_ORDER_LINE_NUMBER | SupplierOrderLineNumber | ✅ |
| TAX_ATTRIBUTE_UPDATE_CODE | TaxAttributeUpdateCode | ✅ |
| TAX_CODE_ID | TaxCodeId | ✅ |
| TAX_NAME | TaxName | ✅ |
| TAX_USER_OVERRIDE_FLAG | TaxUserOverrideFlag | ✅ |
| TAXABLE_FLAG | TaxableFlag | ✅ |
| TERMS_ID | TermsId | ✅ |
| TRANSACTION_FLOW_HEADER_ID | TransactionFlowHeaderId | — |
| TRX_BUSINESS_CATEGORY | TrxBusinessCategory | ✅ |
| UNENCUMBERED_QUANTITY | UnencumberedQuantity | ✅ |
| UNIT_OF_MEASURE_CLASS | UnitOfMeasureClass | ✅ |
| UOM_CODE | UomCode | ✅ |
| USER_DEFINED_FISC_CLASS | UserDefinedFiscClass | ✅ |
| VALUE_BASIS | ValueBasis | ✅ |
| VMI_FLAG | VmiFlag | ✅ |
| WORK_ORDER_ID | WorkOrderId | ✅ |
| WORK_ORDER_NUMBER | WorkOrderNumber | ✅ |
| WORK_ORDER_OPERATION_SEQ | WorkOrderOperationSeq | ✅ |

### [[draftpurchasingdocumentlinelocationpvo|DraftPurchasingDocumentLineLocationPVO]] (PO · BICC: 40/139)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCRUE_ON_RECEIPT_FLAG | DrafShipmentAccrueOnReceiptFlag | ✅ |
| ALLOW_SUBSTITUTE_RECEIPTS_FLAG | DrafShipmentAllowSubstituteReceiptsFlag | ✅ |
| AMOUNT | DrafShipmentAmount | — |
| ASSESSABLE_VALUE | DrafShipmentAssessableValue | — |
| BACK_TO_BACK_FLAG | DrafShipmentBackToBackFlag | ✅ |
| BID_PAYMENT_ID | DrafShipmentBidPaymentId | — |
| CALCULATE_TAX_FLAG | DrafShipmentCalculateTaxFlag | — |
| CANCEL_BACKING_REQ_FLAG | DrafShipmentCancelBackingReqFlag | — |
| CANCEL_BUDGET_DATE | DrafShipmentCancelBudgetDate | — |
| CANCEL_DATE | DrafShipmentCancelDate | — |
| CANCEL_FLAG | DrafShipmentCancelFlag | — |
| CANCEL_REASON | DrafShipmentCancelReason | — |
| CANCELLED_BY | DrafShipmentCancelledBy | — |
| CARRIER_ID | DrafShipmentCarrierId | — |
| CHANGE_ACCEPTED_FLAG | DrafShipmentChangeAcceptedFlag | — |
| CHANGE_PROMISED_DATE_REASON | DrafShipmentChangePromisedDateReason | — |
| CO_AMOUNT_CANCELLED | DrafShipmentCoAmountCancelled | — |
| CO_QUANTITY_CANCELLED | DrafShipmentCoQuantityCancelled | — |
| CONSIGNED_FLAG | DrafShipmentConsignedFlag | — |
| COUNTRY_OF_ORIGIN_CODE | DrafShipmentCountryOfOriginCode | ✅ |
| CREATED_BY | DrafShipmentCreatedBy | — |
| CREATION_DATE | DrafShipmentCreationDate | — |
| CUSTOMER_ITEM | DrafShipmentCustomerItem | — |
| CUSTOMER_ITEM_DESC | DrafShipmentCustomerItemDesc | — |
| CUSTOMER_PO_LINE_NUMBER | DrafShipmentCustomerPoLineNumber | — |
| CUSTOMER_PO_NUMBER | DrafShipmentCustomerPoNumber | — |
| CUSTOMER_PO_SCHEDULE_NUMBER | DrafShipmentCustomerPoScheduleNumber | — |
| DAYS_EARLY_RECEIPT_ALLOWED | DrafShipmentDaysEarlyReceiptAllowed | — |
| DAYS_LATE_RECEIPT_ALLOWED | DrafShipmentDaysLateReceiptAllowed | ✅ |
| DESCRIPTION | DrafShipmentDescription | — |
| DESTINATION_TYPE_CODE | DrafShipmentDestinationTypeCode | ✅ |
| DROP_SHIP_FLAG | DrafShipmentDropShipFlag | — |
| ENCUMBER_NOW | DrafShipmentEncumberNow | — |
| ENCUMBERED_DATE | DrafShipmentEncumberedDate | — |
| ENCUMBERED_FLAG | DrafShipmentEncumberedFlag | — |
| END_DATE | DrafShipmentEndDate | ✅ |
| ENFORCE_SHIP_TO_LOCATION_CODE | DrafShipmentEnforceShipToLocationCode | ✅ |
| ENTITY_CHANGE_TYPE_CODE | DrafShipmentEntityChangeTypeCode | — |
| ESTIMATED_TAX_AMOUNT | DrafShipmentEstimatedTaxAmount | — |
| EXTERNAL_CHANGE_FLAG | DrafShipmentExternalChangeFlag | — |
| FIRM_DATE | DrafShipmentFirmDate | — |
| FIRM_STATUS_LOOKUP_CODE | DrafShipmentFirmStatusLookupCode | — |
| FOB_LOOKUP_CODE | DrafShipmentFobLookupCode | — |
| FREIGHT_TERMS_LOOKUP_CODE | DrafShipmentFreightTermsLookupCode | — |
| FROM_HEADER_ID | DrafShipmentFromHeaderId | — |
| FROM_LINE_ID | DrafShipmentFromLineId | — |
| FROM_LINE_LOCATION_ID | DrafShipmentFromLineLocationId | — |
| FUNDS_STATUS | DrafShipmentFundsStatus | ✅ |
| GOVERNMENT_CONTEXT | DrafShipmentGovernmentContext | — |
| GROUP_NAME | DrafShipmentGroupName | — |
| INPUT_TAX_CLASSIFICATION_CODE | DrafShipmentInputTaxClassificationCode | ✅ |
| INSPECTION_REQUIRED_FLAG | DrafShipmentInspectionRequiredFlag | — |
| INVOICE_CLOSE_TOLERANCE | DrafShipmentInvoiceCloseTolerance | — |
| JOB_DEFINITION_NAME | DrafShipmentJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | DrafShipmentJobDefinitionPackage | — |
| LAST_ACCEPT_DATE | DrafShipmentLastAcceptDate | ✅ |
| LAST_UPDATE_DATE | DrafShipmentLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DrafShipmentLastUpdateLogin | — |
| LAST_UPDATED_BY | DrafShipmentLastUpdatedBy | — |
| LEAD_TIME | DrafShipmentLeadTime | — |
| LEAD_TIME_UNIT | DrafShipmentLeadTimeUnit | — |
| LINE_INTENDED_USE | DrafShipmentLineIntendedUse | ✅ |
| LINE_LOCATION_ID | LineLocationId | ✅ |
| MANUAL_PRICE_CHANGE_FLAG | DrafShipmentManualPriceChangeFlag | — |
| MATCH_OPTION | DrafShipmentMatchOption | — |
| MATCHING_BASIS | DrafShipmentMatchingBasis | — |
| MODE_OF_TRANSPORT | DrafShipmentModeOfTransport | ✅ |
| NEED_BY_DATE | DrafShipmentNeedByDate | ✅ |
| NOTE_TO_RECEIVER | DrafShipmentNoteToReceiver | — |
| OBJECT_VERSION_NUMBER | DrafShipmentObjectVersionNumber | — |
| OUTSOURCED_ASSEMBLY | DrafShipmentOutsourcedAssembly | — |
| PAYMENT_TYPE | DrafShipmentPaymentType | — |
| PJC_CONTEXT_CATEGORY | DrafShipmentPjcContextCategory | — |
| PO_HEADER_ID | DrafShipmentPoHeaderId | — |
| PO_LINE_ID | DrafShipmentPoLineId | — |
| PO_TRADING_ORGANIZATION_ID | DrafShipmentPoTradingOrganizationId | — |
| PRC_BU_ID | DrafShipmentPrcBuId | — |
| PREFERRED_GRADE | DrafShipmentPreferredGrade | — |
| PRICE_DISCOUNT | DrafShipmentPriceDiscount | ✅ |
| PRICE_OVERRIDE | DrafShipmentPriceOverride | ✅ |
| PRODUCT_CATEGORY | DrafShipmentProductCategory | ✅ |
| PRODUCT_FISC_CLASSIFICATION | DrafShipmentProductFiscClassification | ✅ |
| PRODUCT_TYPE | DrafShipmentProductType | ✅ |
| PROGRAM_APP_NAME | DrafShipmentProgramAppName | — |
| PROGRAM_NAME | DrafShipmentProgramName | — |
| PROMISED_DATE | DrafShipmentPromisedDate | ✅ |
| PROMISED_SHIP_DATE | DrafShipmentPromisedShipDate | ✅ |
| QTY_RCV_EXCEPTION_CODE | DrafShipmentQtyRcvExceptionCode | ✅ |
| QTY_RCV_TOLERANCE | DrafShipmentQtyRcvTolerance | — |
| QUANTITY | DrafShipmentQuantity | ✅ |
| REASON_FOR_CHANGE | DrafShipmentReasonForChange | ✅ |
| RECEIPT_DAYS_EXCEPTION_CODE | DrafShipmentReceiptDaysExceptionCode | ✅ |
| RECEIPT_REQUIRED_FLAG | DrafShipmentReceiptRequiredFlag | — |
| RECEIVE_CLOSE_TOLERANCE | DrafShipmentReceiveCloseTolerance | — |
| RECEIVING_ROUTING_ID | DrafShipmentReceivingRoutingId | — |
| REJECTED_BY | DrafShipmentRejectedBy | — |
| REJECTED_BY_ROLE | DrafShipmentRejectedByRole | — |
| REJECTED_REASON | DrafShipmentRejectedReason | — |
| REQ_BU_ID | DrafShipmentReqBuId | — |
| REQUEST_ID | DrafShipmentRequestId | — |
| REQUESTED_SHIP_DATE | DrafShipmentRequestedShipDate | ✅ |
| RETAINAGE_RATE | DrafShipmentRetainageRate | — |
| RETROACTIVE_DATE | DrafShipmentRetroactiveDate | — |
| SALES_ORDER_LINE_NUMBER | DrafShipmentSalesOrderLineNumber | — |
| SALES_ORDER_NUMBER | DrafShipmentSalesOrderNumber | ✅ |
| SALES_ORDER_SCHEDULE_NUMBER | DrafShipmentSalesOrderScheduleNumber | — |
| SALES_ORDER_UPDATE_DATE | DrafShipmentSalesOrderUpdateDate | — |
| SECONDARY_QUANTITY | DrafShipmentSecondaryQuantity | — |
| SECONDARY_UOM_CODE | DrafShipmentSecondaryUomCode | — |
| SERVICE_LEVEL | DrafShipmentServiceLevel | ✅ |
| SFO_AGREEMENT_LINE_NUMBER | DrafShipmentSfoAgreementLineNumber | — |
| SFO_AGREEMENT_NUMBER | DrafShipmentSfoAgreementNumber | ✅ |
| SFO_PTR_ID | DrafShipmentSfoPtrId | — |
| SHIP_TO_CUST_CONTACT_ID | DrafShipmentShipToCustContactId | — |
| SHIP_TO_CUST_ID | DrafShipmentShipToCustId | — |
| SHIP_TO_CUST_LOCATION_ID | DrafShipmentShipToCustLocationId | ✅ |
| SHIP_TO_LOCATION_ID | DrafShipmentShipToLocationId | ✅ |
| SHIP_TO_ORGANIZATION_ID | DrafShipmentShipToOrganizationId | — |
| SHIPMENT_NUM | DrafShipmentShipmentNum | ✅ |
| SHIPMENT_TYPE | DrafShipmentShipmentType | — |
| SHIPPING_UOM_CODE | DrafShipmentShippingUomCode | ✅ |
| SHIPPING_UOM_QUANTITY | DrafShipmentShippingUomQuantity | — |
| SOURCE_SHIPMENT_ID | DrafShipmentSourceShipmentId | — |
| START_DATE | DrafShipmentStartDate | ✅ |
| SUPPLIER_ORDER_LINE_NUMBER | DrafShipmentSupplierOrderLineNumber | ✅ |
| TAX_ATTRIBUTE_UPDATE_CODE | DrafShipmentTaxAttributeUpdateCode | — |
| TAX_CODE_ID | DrafShipmentTaxCodeId | — |
| TAX_NAME | DrafShipmentTaxName | — |
| TAX_USER_OVERRIDE_FLAG | DrafShipmentTaxUserOverrideFlag | — |
| TAXABLE_FLAG | DrafShipmentTaxableFlag | — |
| TERMS_ID | DrafShipmentTermsId | — |
| TRANSACTION_FLOW_HEADER_ID | DrafShipmentTransactionFlowHeaderId | — |
| TRX_BUSINESS_CATEGORY | DrafShipmentTrxBusinessCategory | ✅ |
| UNENCUMBERED_QUANTITY | DrafShipmentUnencumberedQuantity | — |
| UNIT_OF_MEASURE_CLASS | DrafShipmentUnitOfMeasureClass | — |
| UOM_CODE | DrafShipmentUomCode | ✅ |
| USER_DEFINED_FISC_CLASS | DrafShipmentUserDefinedFiscClass | ✅ |
| VALUE_BASIS | DrafShipmentValueBasis | — |
| VMI_FLAG | DrafShipmentVmiFlag | — |

---

## 📚 Referências

- [Oracle Docs — PO_LINE_LOCATIONS_DRAFT_ALL](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
