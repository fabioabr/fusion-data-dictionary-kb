---
id: DOC-PO-140
doc_type: system-doc
title: "PO_ORIG_LINE_LOCATIONS_ALL_V — Localizacoes de Linha Originais (View)"
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
  - PO_ORIG_LINE_LOCATIONS_ALL_V
  - po_orig_line_locations_all_v
  - po-orig-line-locations-all-v
  - po-orig
  - localizacoes-de-linha-originais-(vi
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_ORIG_LINE_LOCATIONS_ALL_V

## 📌 Visão Geral

View com **schedules originais** de PO antes de alteracoes, para comparacao e auditoria.

> [!note] Sufixo _V
> O sufixo `_V` indica que este objeto e uma **view**, projetada para simplificar consultas.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Auditoria:** Comparacao original vs atual.
- **Controle de alteracoes:** Mudancas em datas e quantidades.
- **Compliance:** Evidencia do planejamento original.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LINE_LOCATION_ID | NUMBER(18) | NOT NULL | PK | ID do schedule | — | 🟡 80% |
| 2 | PO_HEADER_ID | NUMBER(18) | NOT NULL | FK | Cabecalho | [[po_headers_all]] | 🟢 90% |
| 3 | PO_LINE_ID | NUMBER(18) | NOT NULL | FK | Linha | [[po_lines_all]] | 🟢 90% |
| 4 | ORIGINAL_QUANTITY | NUMBER | NULL | Quantidade | Quantidade original | — | 🟡 75% |
| 5 | ORIGINAL_NEED_BY_DATE | DATE | NULL | Data | Data original | — | 🟡 75% |
| 6 | ORIGINAL_PROMISED_DATE | DATE | NULL | Data | Data prometida original | — | 🟡 75% |
| 7 | SHIP_TO_LOCATION_ID | NUMBER(18) | NULL | FK | Local original | [[hr_locations]] | 🟢 85% |
| 8 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[po_headers_all]] — via `PO_HEADER_ID` (PO original da view de shipments)
- [[po_lines_all]] — via `PO_LINE_ID` (linha original do PO na view de shipments)

### Tabelas-filha (FK de saída)
- Nenhuma FK de saida identificada

---

## 📎 Uso Típico

### Comparacao original vs atual
```sql
SELECT o.LINE_LOCATION_ID, o.ORIGINAL_QUANTITY, l.QUANTITY AS CURRENT_QTY
FROM   PO_ORIG_LINE_LOCATIONS_ALL_V o
JOIN   PO_LINE_LOCATIONS_ALL l ON o.LINE_LOCATION_ID = l.LINE_LOCATION_ID
WHERE  o.PO_HEADER_ID = :p_po_header_id;
```

---

## 🔒 Observações

- View derivada de tabelas de arquivo/historico.
- Util para relatorios de aderencia ao planejamento.

---

## 🔗 PVOs Relacionados

### [[agreementpricebreakpvo|AgreementPriceBreakPVO]] (PO · BICC: 1/122)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCRUE_ON_RECEIPT_FLAG | OriginalLineLocationAccrueOnReceiptFlag | — |
| ALLOW_SUBSTITUTE_RECEIPTS_FLAG | OriginalLineLocationAllowSubstituteReceiptsFlag | — |
| AMOUNT | OriginalLineLocationAmount | — |
| ASSESSABLE_VALUE | OriginalLineLocationAssessableValue | — |
| ATTRIBUTE_CATEGORY | OriginalLineLocationAttributeCategory | — |
| BID_PAYMENT_ID | OriginalLineLocationBidPaymentId | — |
| CALCULATE_TAX_FLAG | OriginalLineLocationCalculateTaxFlag | — |
| CANCEL_DATE | OriginalLineLocationCancelDate | — |
| CANCEL_FLAG | OriginalLineLocationCancelFlag | — |
| CANCEL_REASON | OriginalLineLocationCancelReason | — |
| CANCELLED_BY | OriginalLineLocationCancelledBy | — |
| CARRIER_ID | OriginalLineLocationCarrierId | — |
| CHANGE_PROMISED_DATE_REASON | OriginalLineLocationChangePromisedDateReason | — |
| CO_AMOUNT_CANCELLED | OriginalLineLocationCoAmountCancelled | — |
| CO_QUANTITY_CANCELLED | OriginalLineLocationCoQuantityCancelled | — |
| CONSIGNED_FLAG | OriginalLineLocationConsignedFlag | — |
| COUNTRY_OF_ORIGIN_CODE | OriginalLineLocationCountryOfOriginCode | — |
| CREATED_BY | OriginalLineLocationCreatedBy | — |
| CREATION_DATE | OriginalLineLocationCreationDate | — |
| DAYS_EARLY_RECEIPT_ALLOWED | OriginalLineLocationDaysEarlyReceiptAllowed | — |
| DAYS_LATE_RECEIPT_ALLOWED | OriginalLineLocationDaysLateReceiptAllowed | — |
| DESCRIPTION | OriginalLineLocationDescription | — |
| DESTINATION_TYPE_CODE | OriginalLineLocationDestinationTypeCode | — |
| DROP_SHIP_FLAG | OriginalLineLocationDropShipFlag | — |
| ENCUMBER_NOW | OriginalLineLocationEncumberNow | — |
| ENCUMBERED_DATE | OriginalLineLocationEncumberedDate | — |
| ENCUMBERED_FLAG | OriginalLineLocationEncumberedFlag | — |
| END_DATE | OriginalLineLocationEndDate | — |
| ENFORCE_SHIP_TO_LOCATION_CODE | OriginalLineLocationEnforceShipToLocationCode | — |
| ENTITY_CO_DISPOSITION | OriginalLineLocationEntityCoDisposition | — |
| ESTIMATED_TAX_AMOUNT | OriginalLineLocationEstimatedTaxAmount | — |
| EXTERNAL_CHANGE_FLAG | OriginalLineLocationExternalChangeFlag | — |
| FIRM_DATE | OriginalLineLocationFirmDate | — |
| FIRM_STATUS_LOOKUP_CODE | OriginalLineLocationFirmStatusLookupCode | — |
| FOB_LOOKUP_CODE | OriginalLineLocationFobLookupCode | — |
| FREIGHT_TERMS_LOOKUP_CODE | OriginalLineLocationFreightTermsLookupCode | — |
| FROM_CO_SEQ | OriginalLineLocationFromCoSeq | — |
| FROM_HEADER_ID | OriginalLineLocationFromHeaderId | — |
| FROM_LINE_ID | OriginalLineLocationFromLineId | — |
| FROM_LINE_LOCATION_ID | OriginalLineLocationFromLineLocationId | — |
| GLOBAL_ATTRIBUTE_CATEGORY | OriginalLineLocationGlobalAttributeCategory | — |
| GOVERNMENT_CONTEXT | OriginalLineLocationGovernmentContext | — |
| GROUP_NAME | OriginalLineLocationGroupName | — |
| INPUT_TAX_CLASSIFICATION_CODE | OriginalLineLocationInputTaxClassificationCode | — |
| INSPECTION_REQUIRED_FLAG | OriginalLineLocationInspectionRequiredFlag | — |
| INVOICE_CLOSE_TOLERANCE | OriginalLineLocationInvoiceCloseTolerance | — |
| JOB_DEFINITION_NAME | OriginalLineLocationJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | OriginalLineLocationJobDefinitionPackage | — |
| LAST_ACCEPT_DATE | OriginalLineLocationLastAcceptDate | — |
| LAST_UPDATE_DATE | OriginalLineLocationLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OriginalLineLocationLastUpdateLogin | — |
| LAST_UPDATED_BY | OriginalLineLocationLastUpdatedBy | — |
| LEAD_TIME | OriginalLineLocationLeadTime | — |
| LEAD_TIME_UNIT | OriginalLineLocationLeadTimeUnit | — |
| LINE_INTENDED_USE | OriginalLineLocationLineIntendedUse | — |
| LINE_INTENDED_USE_ID | OriginalLineLocationLineIntendedUseId | — |
| LINE_LOCATION_ID | OriginalLineLocationLineLocationId | — |
| MANUAL_PRICE_CHANGE_FLAG | OriginalLineLocationManualPriceChangeFlag | — |
| MATCH_OPTION | OriginalLineLocationMatchOption | — |
| MATCHING_BASIS | OriginalLineLocationMatchingBasis | — |
| NEED_BY_DATE | OriginalLineLocationNeedByDate | — |
| NOTE_TO_RECEIVER | OriginalLineLocationNoteToReceiver | — |
| OBJECT_VERSION_NUMBER | OriginalLineLocationObjectVersionNumber | — |
| OUTSOURCED_ASSEMBLY | OriginalLineLocationOutsourcedAssembly | — |
| PAYMENT_TYPE | OriginalLineLocationPaymentType | — |
| PJC_CONTEXT_CATEGORY | OriginalLineLocationPjcContextCategory | — |
| PO_HEADER_ID | OriginalLineLocationPoHeaderId | — |
| PO_LINE_ID | OriginalLineLocationPoLineId | — |
| PO_TRADING_ORGANIZATION_ID | OriginalLineLocationPoTradingOrganizationId | — |
| PRC_BU_ID | OriginalLineLocationPrcBuId | — |
| PREFERRED_GRADE | OriginalLineLocationPreferredGrade | — |
| PRICE_DISCOUNT | OriginalLineLocationPriceDiscount | — |
| PRICE_OVERRIDE | OriginalLineLocationPriceOverride | — |
| PRODUCT_CATEGORY | OriginalLineLocationProductCategory | — |
| PRODUCT_FISC_CLASS_ID | OriginalLineLocationProductFiscClassId | — |
| PRODUCT_FISC_CLASSIFICATION | OriginalLineLocationProductFiscClassification | — |
| PRODUCT_TYPE | OriginalLineLocationProductType | — |
| PROGRAM_APP_NAME | OriginalLineLocationProgramAppName | — |
| PROGRAM_NAME | OriginalLineLocationProgramName | — |
| PROMISED_DATE | OriginalLineLocationPromisedDate | — |
| PROMISED_SHIP_DATE | OriginalLineLocationPromisedShipDate | — |
| QTY_RCV_EXCEPTION_CODE | OriginalLineLocationQtyRcvExceptionCode | — |
| QTY_RCV_TOLERANCE | OriginalLineLocationQtyRcvTolerance | — |
| QUANTITY | OriginalLineLocationQuantity | — |
| REASON_FOR_CHANGE | OriginalLineLocationReasonForChange | — |
| RECEIPT_DAYS_EXCEPTION_CODE | OriginalLineLocationReceiptDaysExceptionCode | — |
| RECEIPT_REQUIRED_FLAG | OriginalLineLocationReceiptRequiredFlag | — |
| RECEIVE_CLOSE_TOLERANCE | OriginalLineLocationReceiveCloseTolerance | — |
| RECEIVING_ROUTING_ID | OriginalLineLocationReceivingRoutingId | — |
| REJECTED_BY | OriginalLineLocationRejectedBy | — |
| REJECTED_BY_ROLE | OriginalLineLocationRejectedByRole | — |
| REJECTED_REASON | OriginalLineLocationRejectedReason | — |
| REQ_BU_ID | OriginalLineLocationReqBuId | — |
| REQUEST_ID | OriginalLineLocationRequestId | — |
| RETROACTIVE_DATE | OriginalLineLocationRetroactiveDate | — |
| SALES_ORDER_UPDATE_DATE | OriginalLineLocationSalesOrderUpdateDate | — |
| SECONDARY_QUANTITY | OriginalLineLocationSecondaryQuantity | — |
| SECONDARY_UOM_CODE | OriginalLineLocationSecondaryUomCode | — |
| SFO_AGREEMENT_LINE_NUMBER | OriginalLineLocationSfoAgreementLineNumber | — |
| SFO_AGREEMENT_NUMBER | OriginalLineLocationSfoAgreementNumber | — |
| SFO_PTR_ID | OriginalLineLocationSfoPtrId | — |
| SHIP_TO_LOCATION_ID | OriginalLineLocationShipToLocationId | — |
| SHIP_TO_ORGANIZATION_ID | OriginalLineLocationShipToOrganizationId | — |
| SHIPMENT_NUM | OriginalLineLocationShipmentNum | — |
| SHIPMENT_TYPE | OriginalLineLocationShipmentType | — |
| SOURCE_SHIPMENT_ID | OriginalLineLocationSourceShipmentId | — |
| START_DATE | OriginalLineLocationStartDate | — |
| SUPPLIER_ORDER_LINE_NUMBER | OriginalLineLocationSupplierOrderLineNumber | — |
| TAX_CODE_ID | OriginalLineLocationTaxCodeId | — |
| TAX_NAME | OriginalLineLocationTaxName | — |
| TAX_USER_OVERRIDE_FLAG | OriginalLineLocationTaxUserOverrideFlag | — |
| TAXABLE_FLAG | OriginalLineLocationTaxableFlag | — |
| TERMS_ID | OriginalLineLocationTermsId | — |
| TO_CO_SEQ | OriginalLineLocationToCoSeq | — |
| TRANSACTION_FLOW_HEADER_ID | OriginalLineLocationTransactionFlowHeaderId | — |
| TRX_BUSINESS_CATEGORY | OriginalLineLocationTrxBusinessCategory | — |
| UNENCUMBERED_QUANTITY | OriginalLineLocationUnencumberedQuantity | — |
| UNIT_OF_MEASURE_CLASS | OriginalLineLocationUnitOfMeasureClass | — |
| UOM_CODE | OriginalLineLocationUomCode | — |
| USER_DEFINED_FISC_CLASS | OriginalLineLocationUserDefinedFiscClass | — |
| VALUE_BASIS | OriginalLineLocationValueBasis | — |
| VMI_FLAG | OriginalLineLocationVmiFlag | — |

### [[standarddistributionpvo|StandardDistributionPVO]] (PO · BICC: 1/122)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCRUE_ON_RECEIPT_FLAG | OriginalLineLocationAccrueOnReceiptFlag | — |
| ALLOW_SUBSTITUTE_RECEIPTS_FLAG | OriginalLineLocationAllowSubstituteReceiptsFlag | — |
| AMOUNT | OriginalLineLocationAmount | — |
| ASSESSABLE_VALUE | OriginalLineLocationAssessableValue | — |
| ATTRIBUTE_CATEGORY | OriginalLineLocationAttributeCategory | — |
| BID_PAYMENT_ID | OriginalLineLocationBidPaymentId | — |
| CALCULATE_TAX_FLAG | OriginalLineLocationCalculateTaxFlag | — |
| CANCEL_DATE | OriginalLineLocationCancelDate | — |
| CANCEL_FLAG | OriginalLineLocationCancelFlag | — |
| CANCEL_REASON | OriginalLineLocationCancelReason | — |
| CANCELLED_BY | OriginalLineLocationCancelledBy | — |
| CARRIER_ID | OriginalLineLocationCarrierId | — |
| CHANGE_PROMISED_DATE_REASON | OriginalLineLocationChangePromisedDateReason | — |
| CO_AMOUNT_CANCELLED | OriginalLineLocationCoAmountCancelled | — |
| CO_QUANTITY_CANCELLED | OriginalLineLocationCoQuantityCancelled | — |
| CONSIGNED_FLAG | OriginalLineLocationConsignedFlag | — |
| COUNTRY_OF_ORIGIN_CODE | OriginalLineLocationCountryOfOriginCode | — |
| CREATED_BY | OriginalLineLocationCreatedBy | — |
| CREATION_DATE | OriginalLineLocationCreationDate | — |
| DAYS_EARLY_RECEIPT_ALLOWED | OriginalLineLocationDaysEarlyReceiptAllowed | — |
| DAYS_LATE_RECEIPT_ALLOWED | OriginalLineLocationDaysLateReceiptAllowed | — |
| DESCRIPTION | OriginalLineLocationDescription | — |
| DESTINATION_TYPE_CODE | OriginalLineLocationDestinationTypeCode | — |
| DROP_SHIP_FLAG | OriginalLineLocationDropShipFlag | — |
| ENCUMBER_NOW | OriginalLineLocationEncumberNow | — |
| ENCUMBERED_DATE | OriginalLineLocationEncumberedDate | — |
| ENCUMBERED_FLAG | OriginalLineLocationEncumberedFlag | — |
| END_DATE | OriginalLineLocationEndDate | — |
| ENFORCE_SHIP_TO_LOCATION_CODE | OriginalLineLocationEnforceShipToLocationCode | — |
| ENTITY_CO_DISPOSITION | OriginalLineLocationEntityCoDisposition | — |
| ESTIMATED_TAX_AMOUNT | OriginalLineLocationEstimatedTaxAmount | — |
| EXTERNAL_CHANGE_FLAG | OriginalLineLocationExternalChangeFlag | — |
| FIRM_DATE | OriginalLineLocationFirmDate | — |
| FIRM_STATUS_LOOKUP_CODE | OriginalLineLocationFirmStatusLookupCode | — |
| FOB_LOOKUP_CODE | OriginalLineLocationFobLookupCode | — |
| FREIGHT_TERMS_LOOKUP_CODE | OriginalLineLocationFreightTermsLookupCode | — |
| FROM_CO_SEQ | OriginalLineLocationFromCoSeq | — |
| FROM_HEADER_ID | OriginalLineLocationFromHeaderId | — |
| FROM_LINE_ID | OriginalLineLocationFromLineId | — |
| FROM_LINE_LOCATION_ID | OriginalLineLocationFromLineLocationId | — |
| GLOBAL_ATTRIBUTE_CATEGORY | OriginalLineLocationGlobalAttributeCategory | — |
| GOVERNMENT_CONTEXT | OriginalLineLocationGovernmentContext | — |
| GROUP_NAME | OriginalLineLocationGroupName | — |
| INPUT_TAX_CLASSIFICATION_CODE | OriginalLineLocationInputTaxClassificationCode | — |
| INSPECTION_REQUIRED_FLAG | OriginalLineLocationInspectionRequiredFlag | — |
| INVOICE_CLOSE_TOLERANCE | OriginalLineLocationInvoiceCloseTolerance | — |
| JOB_DEFINITION_NAME | OriginalLineLocationJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | OriginalLineLocationJobDefinitionPackage | — |
| LAST_ACCEPT_DATE | OriginalLineLocationLastAcceptDate | — |
| LAST_UPDATE_DATE | OriginalLineLocationLastUpdateDate | — |
| LAST_UPDATE_LOGIN | OriginalLineLocationLastUpdateLogin | — |
| LAST_UPDATED_BY | OriginalLineLocationLastUpdatedBy | — |
| LEAD_TIME | OriginalLineLocationLeadTime | — |
| LEAD_TIME_UNIT | OriginalLineLocationLeadTimeUnit | — |
| LINE_INTENDED_USE | OriginalLineLocationLineIntendedUse | — |
| LINE_INTENDED_USE_ID | OriginalLineLocationLineIntendedUseId | — |
| LINE_LOCATION_ID | OriginalLineLocationLineLocationId1 | — |
| MANUAL_PRICE_CHANGE_FLAG | OriginalLineLocationManualPriceChangeFlag | — |
| MATCH_OPTION | OriginalLineLocationMatchOption | — |
| MATCHING_BASIS | OriginalLineLocationMatchingBasis | — |
| NEED_BY_DATE | OriginalLineLocationNeedByDate | — |
| NOTE_TO_RECEIVER | OriginalLineLocationNoteToReceiver | — |
| OBJECT_VERSION_NUMBER | OriginalLineLocationObjectVersionNumber | — |
| OUTSOURCED_ASSEMBLY | OriginalLineLocationOutsourcedAssembly | — |
| PAYMENT_TYPE | OriginalLineLocationPaymentType | — |
| PJC_CONTEXT_CATEGORY | OriginalLineLocationPjcContextCategory | — |
| PO_HEADER_ID | OriginalLineLocationPoHeaderId | — |
| PO_LINE_ID | OriginalLineLocationPoLineId | — |
| PO_TRADING_ORGANIZATION_ID | OriginalLineLocationPoTradingOrganizationId | — |
| PRC_BU_ID | OriginalLineLocationPrcBuId | — |
| PREFERRED_GRADE | OriginalLineLocationPreferredGrade | — |
| PRICE_DISCOUNT | OriginalLineLocationPriceDiscount | — |
| PRICE_OVERRIDE | OriginalLineLocationPriceOverride | — |
| PRODUCT_CATEGORY | OriginalLineLocationProductCategory | — |
| PRODUCT_FISC_CLASS_ID | OriginalLineLocationProductFiscClassId | — |
| PRODUCT_FISC_CLASSIFICATION | OriginalLineLocationProductFiscClassification | — |
| PRODUCT_TYPE | OriginalLineLocationProductType | — |
| PROGRAM_APP_NAME | OriginalLineLocationProgramAppName | — |
| PROGRAM_NAME | OriginalLineLocationProgramName | — |
| PROMISED_DATE | OriginalLineLocationPromisedDate | — |
| PROMISED_SHIP_DATE | OriginalLineLocationPromisedShipDate | ✅ |
| QTY_RCV_EXCEPTION_CODE | OriginalLineLocationQtyRcvExceptionCode | — |
| QTY_RCV_TOLERANCE | OriginalLineLocationQtyRcvTolerance | — |
| QUANTITY | OriginalLineLocationQuantity | — |
| REASON_FOR_CHANGE | OriginalLineLocationReasonForChange | — |
| RECEIPT_DAYS_EXCEPTION_CODE | OriginalLineLocationReceiptDaysExceptionCode | — |
| RECEIPT_REQUIRED_FLAG | OriginalLineLocationReceiptRequiredFlag | — |
| RECEIVE_CLOSE_TOLERANCE | OriginalLineLocationReceiveCloseTolerance | — |
| RECEIVING_ROUTING_ID | OriginalLineLocationReceivingRoutingId | — |
| REJECTED_BY | OriginalLineLocationRejectedBy | — |
| REJECTED_BY_ROLE | OriginalLineLocationRejectedByRole | — |
| REJECTED_REASON | OriginalLineLocationRejectedReason | — |
| REQ_BU_ID | OriginalLineLocationReqBuId | — |
| REQUEST_ID | OriginalLineLocationRequestId | — |
| RETROACTIVE_DATE | OriginalLineLocationRetroactiveDate | — |
| SALES_ORDER_UPDATE_DATE | OriginalLineLocationSalesOrderUpdateDate | — |
| SECONDARY_QUANTITY | OriginalLineLocationSecondaryQuantity | — |
| SECONDARY_UOM_CODE | OriginalLineLocationSecondaryUomCode | — |
| SFO_AGREEMENT_LINE_NUMBER | OriginalLineLocationSfoAgreementLineNumber | — |
| SFO_AGREEMENT_NUMBER | OriginalLineLocationSfoAgreementNumber | — |
| SFO_PTR_ID | OriginalLineLocationSfoPtrId | — |
| SHIP_TO_LOCATION_ID | OriginalLineLocationShipToLocationId | — |
| SHIP_TO_ORGANIZATION_ID | OriginalLineLocationShipToOrganizationId | — |
| SHIPMENT_NUM | OriginalLineLocationShipmentNum | — |
| SHIPMENT_TYPE | OriginalLineLocationShipmentType | — |
| SOURCE_SHIPMENT_ID | OriginalLineLocationSourceShipmentId | — |
| START_DATE | OriginalLineLocationStartDate | — |
| SUPPLIER_ORDER_LINE_NUMBER | OriginalLineLocationSupplierOrderLineNumber | — |
| TAX_CODE_ID | OriginalLineLocationTaxCodeId | — |
| TAX_NAME | OriginalLineLocationTaxName | — |
| TAX_USER_OVERRIDE_FLAG | OriginalLineLocationTaxUserOverrideFlag | — |
| TAXABLE_FLAG | OriginalLineLocationTaxableFlag | — |
| TERMS_ID | OriginalLineLocationTermsId | — |
| TO_CO_SEQ | OriginalLineLocationToCoSeq | — |
| TRANSACTION_FLOW_HEADER_ID | OriginalLineLocationTransactionFlowHeaderId | — |
| TRX_BUSINESS_CATEGORY | OriginalLineLocationTrxBusinessCategory | — |
| UNENCUMBERED_QUANTITY | OriginalLineLocationUnencumberedQuantity | — |
| UNIT_OF_MEASURE_CLASS | OriginalLineLocationUnitOfMeasureClass | — |
| UOM_CODE | OriginalLineLocationUomCode | — |
| USER_DEFINED_FISC_CLASS | OriginalLineLocationUserDefinedFiscClass | — |
| VALUE_BASIS | OriginalLineLocationValueBasis | — |
| VMI_FLAG | OriginalLineLocationVmiFlag | — |

### [[standardshipmentpvo|StandardShipmentPVO]] (PO · BICC: 1/122)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCRUE_ON_RECEIPT_FLAG | OriginalLineLocationAccrueOnReceiptFlag | — |
| ALLOW_SUBSTITUTE_RECEIPTS_FLAG | OriginalLineLocationAllowSubstituteReceiptsFlag | — |
| AMOUNT | OriginalLineLocationAmount | — |
| ASSESSABLE_VALUE | OriginalLineLocationAssessableValue | — |
| ATTRIBUTE_CATEGORY | OriginalLineLocationAttributeCategory | — |
| BID_PAYMENT_ID | OriginalLineLocationBidPaymentId | — |
| CALCULATE_TAX_FLAG | OriginalLineLocationCalculateTaxFlag | — |
| CANCEL_DATE | OriginalLineLocationCancelDate | — |
| CANCEL_FLAG | OriginalLineLocationCancelFlag | — |
| CANCEL_REASON | OriginalLineLocationCancelReason | — |
| CANCELLED_BY | OriginalLineLocationCancelledBy | — |
| CARRIER_ID | OriginalLineLocationCarrierId | — |
| CHANGE_PROMISED_DATE_REASON | OriginalLineLocationChangePromisedDateReason | — |
| CO_AMOUNT_CANCELLED | OriginalLineLocationCoAmountCancelled | — |
| CO_QUANTITY_CANCELLED | OriginalLineLocationCoQuantityCancelled | — |
| CONSIGNED_FLAG | OriginalLineLocationConsignedFlag | — |
| COUNTRY_OF_ORIGIN_CODE | OriginalLineLocationCountryOfOriginCode | — |
| CREATED_BY | OriginalLineLocationCreatedBy | — |
| CREATION_DATE | OriginalLineLocationCreationDate | — |
| DAYS_EARLY_RECEIPT_ALLOWED | OriginalLineLocationDaysEarlyReceiptAllowed | — |
| DAYS_LATE_RECEIPT_ALLOWED | OriginalLineLocationDaysLateReceiptAllowed | — |
| DESCRIPTION | OriginalLineLocationDescription | — |
| DESTINATION_TYPE_CODE | OriginalLineLocationDestinationTypeCode | — |
| DROP_SHIP_FLAG | OriginalLineLocationDropShipFlag | — |
| ENCUMBER_NOW | OriginalLineLocationEncumberNow | — |
| ENCUMBERED_DATE | OriginalLineLocationEncumberedDate | — |
| ENCUMBERED_FLAG | OriginalLineLocationEncumberedFlag | — |
| END_DATE | OriginalLineLocationEndDate | — |
| ENFORCE_SHIP_TO_LOCATION_CODE | OriginalLineLocationEnforceShipToLocationCode | — |
| ENTITY_CO_DISPOSITION | OriginalLineLocationEntityCoDisposition | — |
| ESTIMATED_TAX_AMOUNT | OriginalLineLocationEstimatedTaxAmount | — |
| EXTERNAL_CHANGE_FLAG | OriginalLineLocationExternalChangeFlag | — |
| FIRM_DATE | OriginalLineLocationFirmDate | — |
| FIRM_STATUS_LOOKUP_CODE | OriginalLineLocationFirmStatusLookupCode | — |
| FOB_LOOKUP_CODE | OriginalLineLocationFobLookupCode | — |
| FREIGHT_TERMS_LOOKUP_CODE | OriginalLineLocationFreightTermsLookupCode | — |
| FROM_CO_SEQ | OriginalLineLocationFromCoSeq | — |
| FROM_HEADER_ID | OriginalLineLocationFromHeaderId | — |
| FROM_LINE_ID | OriginalLineLocationFromLineId | — |
| FROM_LINE_LOCATION_ID | OriginalLineLocationFromLineLocationId | — |
| GLOBAL_ATTRIBUTE_CATEGORY | OriginalLineLocationGlobalAttributeCategory | — |
| GOVERNMENT_CONTEXT | OriginalLineLocationGovernmentContext | — |
| GROUP_NAME | OriginalLineLocationGroupName | — |
| INPUT_TAX_CLASSIFICATION_CODE | OriginalLineLocationInputTaxClassificationCode | — |
| INSPECTION_REQUIRED_FLAG | OriginalLineLocationInspectionRequiredFlag | — |
| INVOICE_CLOSE_TOLERANCE | OriginalLineLocationInvoiceCloseTolerance | — |
| JOB_DEFINITION_NAME | OriginalLineLocationJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | OriginalLineLocationJobDefinitionPackage | — |
| LAST_ACCEPT_DATE | OriginalLineLocationLastAcceptDate | — |
| LAST_UPDATE_DATE | OriginalLineLocationLastUpdateDate | — |
| LAST_UPDATE_LOGIN | OriginalLineLocationLastUpdateLogin | — |
| LAST_UPDATED_BY | OriginalLineLocationLastUpdatedBy | — |
| LEAD_TIME | OriginalLineLocationLeadTime | — |
| LEAD_TIME_UNIT | OriginalLineLocationLeadTimeUnit | — |
| LINE_INTENDED_USE | OriginalLineLocationLineIntendedUse | — |
| LINE_INTENDED_USE_ID | OriginalLineLocationLineIntendedUseId | — |
| LINE_LOCATION_ID | OriginalLineLocationLineLocationId | — |
| MANUAL_PRICE_CHANGE_FLAG | OriginalLineLocationManualPriceChangeFlag | — |
| MATCH_OPTION | OriginalLineLocationMatchOption | — |
| MATCHING_BASIS | OriginalLineLocationMatchingBasis | — |
| NEED_BY_DATE | OriginalLineLocationNeedByDate | — |
| NOTE_TO_RECEIVER | OriginalLineLocationNoteToReceiver | — |
| OBJECT_VERSION_NUMBER | OriginalLineLocationObjectVersionNumber | — |
| OUTSOURCED_ASSEMBLY | OriginalLineLocationOutsourcedAssembly | — |
| PAYMENT_TYPE | OriginalLineLocationPaymentType | — |
| PJC_CONTEXT_CATEGORY | OriginalLineLocationPjcContextCategory | — |
| PO_HEADER_ID | OriginalLineLocationPoHeaderId | — |
| PO_LINE_ID | OriginalLineLocationPoLineId | — |
| PO_TRADING_ORGANIZATION_ID | OriginalLineLocationPoTradingOrganizationId | — |
| PRC_BU_ID | OriginalLineLocationPrcBuId | — |
| PREFERRED_GRADE | OriginalLineLocationPreferredGrade | — |
| PRICE_DISCOUNT | OriginalLineLocationPriceDiscount | — |
| PRICE_OVERRIDE | OriginalLineLocationPriceOverride | — |
| PRODUCT_CATEGORY | OriginalLineLocationProductCategory | — |
| PRODUCT_FISC_CLASS_ID | OriginalLineLocationProductFiscClassId | — |
| PRODUCT_FISC_CLASSIFICATION | OriginalLineLocationProductFiscClassification | — |
| PRODUCT_TYPE | OriginalLineLocationProductType | — |
| PROGRAM_APP_NAME | OriginalLineLocationProgramAppName | — |
| PROGRAM_NAME | OriginalLineLocationProgramName | — |
| PROMISED_DATE | OriginalLineLocationPromisedDate | — |
| PROMISED_SHIP_DATE | OriginalLineLocationPromisedShipDate | ✅ |
| QTY_RCV_EXCEPTION_CODE | OriginalLineLocationQtyRcvExceptionCode | — |
| QTY_RCV_TOLERANCE | OriginalLineLocationQtyRcvTolerance | — |
| QUANTITY | OriginalLineLocationQuantity | — |
| REASON_FOR_CHANGE | OriginalLineLocationReasonForChange | — |
| RECEIPT_DAYS_EXCEPTION_CODE | OriginalLineLocationReceiptDaysExceptionCode | — |
| RECEIPT_REQUIRED_FLAG | OriginalLineLocationReceiptRequiredFlag | — |
| RECEIVE_CLOSE_TOLERANCE | OriginalLineLocationReceiveCloseTolerance | — |
| RECEIVING_ROUTING_ID | OriginalLineLocationReceivingRoutingId | — |
| REJECTED_BY | OriginalLineLocationRejectedBy | — |
| REJECTED_BY_ROLE | OriginalLineLocationRejectedByRole | — |
| REJECTED_REASON | OriginalLineLocationRejectedReason | — |
| REQ_BU_ID | OriginalLineLocationReqBuId | — |
| REQUEST_ID | OriginalLineLocationRequestId | — |
| RETROACTIVE_DATE | OriginalLineLocationRetroactiveDate | — |
| SALES_ORDER_UPDATE_DATE | OriginalLineLocationSalesOrderUpdateDate | — |
| SECONDARY_QUANTITY | OriginalLineLocationSecondaryQuantity | — |
| SECONDARY_UOM_CODE | OriginalLineLocationSecondaryUomCode | — |
| SFO_AGREEMENT_LINE_NUMBER | OriginalLineLocationSfoAgreementLineNumber | — |
| SFO_AGREEMENT_NUMBER | OriginalLineLocationSfoAgreementNumber | — |
| SFO_PTR_ID | OriginalLineLocationSfoPtrId | — |
| SHIP_TO_LOCATION_ID | OriginalLineLocationShipToLocationId | — |
| SHIP_TO_ORGANIZATION_ID | OriginalLineLocationShipToOrganizationId | — |
| SHIPMENT_NUM | OriginalLineLocationShipmentNum | — |
| SHIPMENT_TYPE | OriginalLineLocationShipmentType | — |
| SOURCE_SHIPMENT_ID | OriginalLineLocationSourceShipmentId | — |
| START_DATE | OriginalLineLocationStartDate | — |
| SUPPLIER_ORDER_LINE_NUMBER | OriginalLineLocationSupplierOrderLineNumber | — |
| TAX_CODE_ID | OriginalLineLocationTaxCodeId | — |
| TAX_NAME | OriginalLineLocationTaxName | — |
| TAX_USER_OVERRIDE_FLAG | OriginalLineLocationTaxUserOverrideFlag | — |
| TAXABLE_FLAG | OriginalLineLocationTaxableFlag | — |
| TERMS_ID | OriginalLineLocationTermsId | — |
| TO_CO_SEQ | OriginalLineLocationToCoSeq | — |
| TRANSACTION_FLOW_HEADER_ID | OriginalLineLocationTransactionFlowHeaderId | — |
| TRX_BUSINESS_CATEGORY | OriginalLineLocationTrxBusinessCategory | — |
| UNENCUMBERED_QUANTITY | OriginalLineLocationUnencumberedQuantity | — |
| UNIT_OF_MEASURE_CLASS | OriginalLineLocationUnitOfMeasureClass | — |
| UOM_CODE | OriginalLineLocationUomCode | — |
| USER_DEFINED_FISC_CLASS | OriginalLineLocationUserDefinedFiscClass | — |
| VALUE_BASIS | OriginalLineLocationValueBasis | — |
| VMI_FLAG | OriginalLineLocationVmiFlag | — |

---

## 📚 Referências

- [Oracle Docs — PO_ORIG_LINE_LOCATIONS_ALL_V](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
