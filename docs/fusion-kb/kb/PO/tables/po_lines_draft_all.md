---
id: DOC-PO-133
doc_type: system-doc
title: "PO_LINES_DRAFT_ALL — Linhas de PO em Rascunho"
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
  - PO_LINES_DRAFT_ALL
  - po_lines_draft_all
  - po-lines-draft-all
  - po-lines
  - linhas-de-po-em-rascunho
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_LINES_DRAFT_ALL

## 📌 Visão Geral

Armazena as **linhas de POs em fase de rascunho**. Estrutura espelha `PO_LINES_ALL`.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` e necessario para consultas por organizacao especifica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Edicao:** Linhas de POs em elaboracao.
- **Amendments:** Linhas alteradas durante emendas.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PO_LINE_ID | NUMBER(18) | NOT NULL | PK | ID da linha | — | 🟢 95% |
| 2 | DRAFT_ID | NUMBER(18) | NOT NULL | PK | ID do draft | [[po_headers_draft_all]] | 🟢 95% |
| 3 | PO_HEADER_ID | NUMBER(18) | NOT NULL | FK | Cabecalho | [[po_headers_draft_all]] | 🟢 95% |
| 4 | LINE_NUM | NUMBER | NOT NULL | Identificacao | Numero | — | 🟢 100% |
| 5 | ITEM_DESCRIPTION | VARCHAR2(240) | NULL | Descritivo | Descricao | — | 🟢 100% |
| 6 | UNIT_PRICE | NUMBER | NULL | Financeiro | Preco | — | 🟢 100% |
| 7 | QUANTITY | NUMBER | NULL | Quantidade | Quantidade | — | 🟢 100% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[po_headers_draft_all]] — via `PO_HEADER_ID`/`DRAFT_ID` (rascunho de PO ao qual a linha draft pertence)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Linhas de um draft
```sql
SELECT PO_LINE_ID, LINE_NUM, ITEM_DESCRIPTION, UNIT_PRICE, QUANTITY
FROM   PO_LINES_DRAFT_ALL
WHERE  PO_HEADER_ID = :p_header_id AND DRAFT_ID = :p_draft_id;
```

---

## 🔒 Observações

- Dados migram para `PO_LINES_ALL` apos aprovacao.
- Estrutura espelha `PO_LINES_ALL`.

---

## 🔗 PVOs Relacionados

### [[draftpurchaseorderdistributionpvo|DraftPurchaseOrderDistributionPVO]] (PO · BICC: 20/318)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGING_PERIOD_DAYS | DraftLineAgingPeriodDays | — |
| ALLOW_DESCRIPTION_UPDATE_FLAG | DraftLineAllowDescriptionUpdateFlag | — |
| ALLOW_DESCRIPTION_UPDATE_FLAG | FromDraftLineAllowDescriptionUpdateFlag | — |
| ALLOW_DESCRIPTION_UPDATE_FLAG | FromDraftShipmentLineAllowDescriptionUpdateFlag | — |
| ALLOW_PRICE_OVERRIDE_FLAG | DraftLineAllowPriceOverrideFlag | — |
| ALLOW_PRICE_OVERRIDE_FLAG | FromDraftLineAllowPriceOverrideFlag | — |
| ALLOW_PRICE_OVERRIDE_FLAG | FromDraftShipmentLineAllowPriceOverrideFlag | — |
| AMOUNT | DraftLineAmount | — |
| AMOUNT | FromDraftLineAmount | — |
| AMOUNT | FromDraftShipmentLineAmount | — |
| AUCTION_DISPLAY_NUMBER | DraftLineAuctionDisplayNumber | — |
| AUCTION_DISPLAY_NUMBER | FromDraftLineAuctionDisplayNumber | — |
| AUCTION_DISPLAY_NUMBER | FromDraftShipmentLineAuctionDisplayNumber | — |
| AUCTION_HEADER_ID | DraftLineAuctionHeaderId | — |
| AUCTION_HEADER_ID | FromDraftLineAuctionHeaderId | — |
| AUCTION_HEADER_ID | FromDraftShipmentLineAuctionHeaderId | — |
| AUCTION_LINE_NUMBER | DraftLineAuctionLineNumber | — |
| AUCTION_LINE_NUMBER | FromDraftLineAuctionLineNumber | — |
| AUCTION_LINE_NUMBER | FromDraftShipmentLineAuctionLineNumber | — |
| BASE_QTY | DraftLineBaseQty | — |
| BASE_QTY | FromDraftLineBaseQty | — |
| BASE_QTY | FromDraftShipmentLineBaseQty | — |
| BASE_UNIT_PRICE | DraftLineBaseUnitPrice | — |
| BASE_UNIT_PRICE | FromDraftLineBaseUnitPrice | — |
| BASE_UNIT_PRICE | FromDraftShipmentLineBaseUnitPrice | — |
| BASE_UOM | DraftLineBaseUom | — |
| BASE_UOM | FromDraftLineBaseUom | — |
| BASE_UOM | FromDraftShipmentLineBaseUom | — |
| BID_LINE_NUMBER | DraftLineBidLineNumber | — |
| BID_LINE_NUMBER | FromDraftLineBidLineNumber | — |
| BID_LINE_NUMBER | FromDraftShipmentLineBidLineNumber | — |
| BID_NUMBER | DraftLineBidNumber | — |
| BID_NUMBER | FromDraftLineBidNumber | — |
| BID_NUMBER | FromDraftShipmentLineBidNumber | — |
| CANCEL_DATE | DraftLineCancelDate | — |
| CANCEL_DATE | FromDraftLineCancelDate | — |
| CANCEL_DATE | FromDraftShipmentLineCancelDate | — |
| CANCEL_FLAG | DraftLineCancelFlag | — |
| CANCEL_FLAG | FromDraftLineCancelFlag | — |
| CANCEL_FLAG | FromDraftShipmentLineCancelFlag | — |
| CANCEL_REASON | DraftLineCancelReason | — |
| CANCEL_REASON | FromDraftLineCancelReason | — |
| CANCEL_REASON | FromDraftShipmentLineCancelReason | — |
| CANCELLED_BY | DraftLineCancelledBy | — |
| CANCELLED_BY | FromDraftLineCancelledBy | — |
| CANCELLED_BY | FromDraftShipmentLineCancelledBy | — |
| CAPITAL_EXPENSE_FLAG | DraftLineCapitalExpenseFlag | — |
| CAPITAL_EXPENSE_FLAG | FromDraftLineCapitalExpenseFlag | — |
| CAPITAL_EXPENSE_FLAG | FromDraftShipmentLineCapitalExpenseFlag | — |
| CATEGORY_ID | DraftLineCategoryId | — |
| CATEGORY_ID | FromDraftLineCategoryId | — |
| CATEGORY_ID | FromDraftShipmentLineCategoryId | — |
| CHANGE_ACCEPTED_FLAG | DraftLineChangeAcceptedFlag | — |
| CHANGE_ACCEPTED_FLAG | FromDraftLineChangeAcceptedFlag | — |
| CHANGE_ACCEPTED_FLAG | FromDraftShipmentLineChangeAcceptedFlag | — |
| CO_AMOUNT_CANCELLED | DraftLineCoAmountCancelled | — |
| CO_AMOUNT_CANCELLED | FromDraftLineCoAmountCancelled | — |
| CO_AMOUNT_CANCELLED | FromDraftShipmentLineCoAmountCancelled | — |
| CO_QUANTITY_CANCELLED | DraftLineCoQuantityCancelled | — |
| CO_QUANTITY_CANCELLED | FromDraftLineCoQuantityCancelled | — |
| CO_QUANTITY_CANCELLED | FromDraftShipmentLineCoQuantityCancelled | — |
| COMMITTED_AMOUNT | DraftLineCommittedAmount | — |
| COMMITTED_AMOUNT | FromDraftLineCommittedAmount | — |
| COMMITTED_AMOUNT | FromDraftShipmentLineCommittedAmount | — |
| CONSIGNMENT_LINE_FLAG | DraftLineConsignmentLineFlag | ✅ |
| CONTRACT_ID | DraftLineContractId | — |
| CONTRACT_ID | FromDraftLineContractId | — |
| CONTRACT_ID | FromDraftShipmentLineContractId | — |
| CONTRACTOR_FIRST_NAME | DraftLineContractorFirstName | — |
| CONTRACTOR_FIRST_NAME | FromDraftLineContractorFirstName | — |
| CONTRACTOR_FIRST_NAME | FromDraftShipmentLineContractorFirstName | — |
| CONTRACTOR_LAST_NAME | DraftLineContractorLastName | — |
| CONTRACTOR_LAST_NAME | FromDraftLineContractorLastName | — |
| CONTRACTOR_LAST_NAME | FromDraftShipmentLineContractorLastName | — |
| CREATED_BY | DraftLineCreatedBy | — |
| CREATED_BY | FromDraftLineCreatedBy | — |
| CREATED_BY | FromDraftShipmentLineCreatedBy | — |
| CREATION_DATE | DraftLineCreationDate | — |
| CREATION_DATE | FromDraftLineCreationDate | — |
| CREATION_DATE | FromDraftShipmentLineCreationDate | — |
| ENTITY_CHANGE_TYPE_CODE | DraftLineEntityChangeTypeCode | — |
| ENTITY_CHANGE_TYPE_CODE | FromDraftLineEntityChangeTypeCode | — |
| ENTITY_CHANGE_TYPE_CODE | FromDraftShipmentLineEntityChangeTypeCode | — |
| EXPIRATION_DATE | DraftLineExpirationDate | — |
| EXPIRATION_DATE | FromDraftLineExpirationDate | — |
| EXPIRATION_DATE | FromDraftShipmentLineExpirationDate | — |
| EXTERNAL_CHANGE_FLAG | DraftLineExternalChangeFlag | — |
| EXTERNAL_CHANGE_FLAG | FromDraftLineExternalChangeFlag | — |
| EXTERNAL_CHANGE_FLAG | FromDraftShipmentLineExternalChangeFlag | — |
| FIRM_DATE | DraftLineFirmDate | — |
| FIRM_DATE | FromDraftLineFirmDate | — |
| FIRM_DATE | FromDraftShipmentLineFirmDate | — |
| FIRM_STATUS_LOOKUP_CODE | DraftLineFirmStatusLookupCode | — |
| FIRM_STATUS_LOOKUP_CODE | FromDraftLineFirmStatusLookupCode | — |
| FIRM_STATUS_LOOKUP_CODE | FromDraftShipmentLineFirmStatusLookupCode | — |
| FROM_HEADER_ID | DraftLineFromHeaderId | — |
| FROM_HEADER_ID | FromDraftLineFromHeaderId | — |
| FROM_HEADER_ID | FromDraftShipmentLineFromHeaderId | — |
| FROM_LINE_ID | DraftLineFromLineId | — |
| FROM_LINE_ID | FromDraftLineFromLineId | — |
| FROM_LINE_ID | FromDraftShipmentLineFromLineId | — |
| FROM_LINE_LOCATION_ID | DraftLineFromLineLocationId | — |
| FROM_LINE_LOCATION_ID | FromDraftLineFromLineLocationId | — |
| FROM_LINE_LOCATION_ID | FromDraftShipmentLineFromLineLocationId | — |
| FUNDS_STATUS | DraftLineFundsStatus | ✅ |
| FUNDS_STATUS | FromDraftLineFundsStatus | — |
| FUNDS_STATUS | FromDraftShipmentLineFundsStatus | — |
| GOVERNMENT_CONTEXT | DraftLineGovernmentContext | — |
| GOVERNMENT_CONTEXT | FromDraftLineGovernmentContext | — |
| GOVERNMENT_CONTEXT | FromDraftShipmentLineGovernmentContext | — |
| HAZARD_CLASS_ID | DraftLineHazardClassId | — |
| HAZARD_CLASS_ID | FromDraftLineHazardClassId | — |
| HAZARD_CLASS_ID | FromDraftShipmentLineHazardClassId | — |
| ITEM_DESCRIPTION | DraftLineItemDescription | ✅ |
| ITEM_DESCRIPTION | FromDraftLineItemDescription | — |
| ITEM_DESCRIPTION | FromDraftShipmentLineItemDescription | — |
| ITEM_ID | DraftLineItemId | ✅ |
| ITEM_ID | FromDraftLineItemId | — |
| ITEM_ID | FromDraftShipmentLineItemId | — |
| ITEM_REVISION | DraftLineItemRevision | ✅ |
| ITEM_REVISION | FromDraftLineItemRevision | — |
| ITEM_REVISION | FromDraftShipmentLineItemRevision | — |
| JOB_DEFINITION_NAME | DraftLineJobDefinitionName | — |
| JOB_DEFINITION_NAME | FromDraftLineJobDefinitionName | — |
| JOB_DEFINITION_NAME | FromDraftShipmentLineJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | DraftLineJobDefinitionPackage | — |
| JOB_DEFINITION_PACKAGE | FromDraftLineJobDefinitionPackage | — |
| JOB_DEFINITION_PACKAGE | FromDraftShipmentLineJobDefinitionPackage | — |
| JOB_ID | DraftLineJobId | — |
| JOB_ID | FromDraftLineJobId | — |
| JOB_ID | FromDraftShipmentLineJobId | — |
| LAST_UPDATE_DATE | DraftLineLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | FromDraftLineLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | FromDraftShipmentLineLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DraftLineLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | FromDraftLineLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | FromDraftShipmentLineLastUpdateLogin | — |
| LAST_UPDATED_BY | DraftLineLastUpdatedBy | — |
| LAST_UPDATED_BY | FromDraftLineLastUpdatedBy | — |
| LAST_UPDATED_BY | FromDraftShipmentLineLastUpdatedBy | — |
| LINE_NUM | DraftLineLineNum | ✅ |
| LINE_NUM | FromDraftLineLineNum | — |
| LINE_NUM | FromDraftShipmentLineLineNum | — |
| LINE_REFERENCE_NUM | DraftLineLineReferenceNum | — |
| LINE_REFERENCE_NUM | FromDraftLineLineReferenceNum | — |
| LINE_REFERENCE_NUM | FromDraftShipmentLineLineReferenceNum | — |
| LINE_TYPE_ID | DraftLineLineTypeId | — |
| LINE_TYPE_ID | FromDraftLineLineTypeId | — |
| LINE_TYPE_ID | FromDraftShipmentLineLineTypeId | — |
| LIST_PRICE_PER_UNIT | DraftLineListPricePerUnit | — |
| LIST_PRICE_PER_UNIT | FromDraftLineListPricePerUnit | — |
| LIST_PRICE_PER_UNIT | FromDraftShipmentLineListPricePerUnit | — |
| MANUAL_PRICE_CHANGE_FLAG | DraftLineManualPriceChangeFlag | — |
| MANUAL_PRICE_CHANGE_FLAG | FromDraftLineManualPriceChangeFlag | — |
| MANUAL_PRICE_CHANGE_FLAG | FromDraftShipmentLineManualPriceChangeFlag | — |
| MARKET_PRICE | DraftLineMarketPrice | — |
| MARKET_PRICE | FromDraftLineMarketPrice | — |
| MARKET_PRICE | FromDraftShipmentLineMarketPrice | — |
| MATCHING_BASIS | DraftLineMatchingBasis | — |
| MATCHING_BASIS | FromDraftLineMatchingBasis | — |
| MATCHING_BASIS | FromDraftShipmentLineMatchingBasis | — |
| MAX_RETAINAGE_AMOUNT | DraftLineMaxRetainageAmount | — |
| MAX_RETAINAGE_AMOUNT | FromDraftLineMaxRetainageAmount | — |
| MAX_RETAINAGE_AMOUNT | FromDraftShipmentLineMaxRetainageAmount | — |
| MIN_RELEASE_AMOUNT | DraftLineMinReleaseAmount | ✅ |
| MIN_RELEASE_AMOUNT | FromDraftLineMinReleaseAmount | — |
| MIN_RELEASE_AMOUNT | FromDraftShipmentLineMinReleaseAmount | — |
| NEGOTIATED_BY_PREPARER_FLAG | DraftLineNegotiatedByPreparerFlag | ✅ |
| NEGOTIATED_BY_PREPARER_FLAG | FromDraftLineNegotiatedByPreparerFlag | — |
| NEGOTIATED_BY_PREPARER_FLAG | FromDraftShipmentLineNegotiatedByPreparerFlag | — |
| NOT_TO_EXCEED_PRICE | DraftLineNotToExceedPrice | — |
| NOT_TO_EXCEED_PRICE | FromDraftLineNotToExceedPrice | — |
| NOT_TO_EXCEED_PRICE | FromDraftShipmentLineNotToExceedPrice | — |
| NOTE_TO_VENDOR | DraftLineNoteToVendor | ✅ |
| NOTE_TO_VENDOR | FromDraftLineNoteToVendor | — |
| NOTE_TO_VENDOR | FromDraftShipmentLineNoteToVendor | — |
| OBJECT_VERSION_NUMBER | DraftLineObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | FromDraftLineObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | FromDraftShipmentLineObjectVersionNumber | — |
| OKE_CONTRACT_HEADER_ID | DraftLineOkeContractHeaderId | — |
| OKE_CONTRACT_HEADER_ID | FromDraftLineOkeContractHeaderId | — |
| OKE_CONTRACT_HEADER_ID | FromDraftShipmentLineOkeContractHeaderId | — |
| OKE_CONTRACT_VERSION_ID | DraftLineOkeContractVersionId | — |
| OKE_CONTRACT_VERSION_ID | FromDraftLineOkeContractVersionId | — |
| OKE_CONTRACT_VERSION_ID | FromDraftShipmentLineOkeContractVersionId | — |
| ORDER_TYPE_LOOKUP_CODE | DraftLineOrderTypeLookupCode | — |
| ORDER_TYPE_LOOKUP_CODE | FromDraftLineOrderTypeLookupCode | — |
| ORDER_TYPE_LOOKUP_CODE | FromDraftShipmentLineOrderTypeLookupCode | — |
| ORIGINAL_INTERFACE_LINE_ID | DraftLineOriginalInterfaceLineId | — |
| ORIGINAL_INTERFACE_LINE_ID | FromDraftLineOriginalInterfaceLineId | — |
| ORIGINAL_INTERFACE_LINE_ID | FromDraftShipmentLineOriginalInterfaceLineId | — |
| OVER_TOLERANCE_ERROR_FLAG | DraftLineOverToleranceErrorFlag | — |
| OVER_TOLERANCE_ERROR_FLAG | FromDraftLineOverToleranceErrorFlag | — |
| OVER_TOLERANCE_ERROR_FLAG | FromDraftShipmentLineOverToleranceErrorFlag | — |
| PJC_CONTEXT_CATEGORY | DraftLinePjcContextCategory | — |
| PJC_CONTEXT_CATEGORY | FromDraftLinePjcContextCategory | — |
| PJC_CONTEXT_CATEGORY | FromDraftShipmentLinePjcContextCategory | — |
| PO_HEADER_ID | DraftLinePoHeaderId | — |
| PO_HEADER_ID | FromDraftLinePoHeaderId | — |
| PO_HEADER_ID | FromDraftShipmentLinePoHeaderId | — |
| PO_LINE_ID | DraftLinePoLineId | ✅ |
| PO_LINE_ID | FromDraftLinePoLineId | — |
| PO_LINE_ID | FromDraftShipmentLinePoLineId | — |
| PRC_BU_ID | DraftLinePrcBuId | — |
| PRC_BU_ID | FromDraftLinePrcBuId | — |
| PRC_BU_ID | FromDraftShipmentLinePrcBuId | — |
| PREFERRED_GRADE | DraftLinePreferredGrade | — |
| PREFERRED_GRADE | FromDraftLinePreferredGrade | — |
| PREFERRED_GRADE | FromDraftShipmentLinePreferredGrade | — |
| PRICE_BREAK_LOOKUP_CODE | DraftLinePriceBreakLookupCode | — |
| PRICE_BREAK_LOOKUP_CODE | FromDraftLinePriceBreakLookupCode | — |
| PRICE_BREAK_LOOKUP_CODE | FromDraftShipmentLinePriceBreakLookupCode | — |
| PRICE_TYPE_LOOKUP_CODE | DraftLinePriceTypeLookupCode | — |
| PRICE_TYPE_LOOKUP_CODE | FromDraftLinePriceTypeLookupCode | — |
| PRICE_TYPE_LOOKUP_CODE | FromDraftShipmentLinePriceTypeLookupCode | — |
| PROGRAM_APP_NAME | DraftLineProgramAppName | — |
| PROGRAM_APP_NAME | FromDraftLineProgramAppName | — |
| PROGRAM_APP_NAME | FromDraftShipmentLineProgramAppName | — |
| PROGRAM_NAME | DraftLineProgramName | — |
| PROGRAM_NAME | FromDraftLineProgramName | — |
| PROGRAM_NAME | FromDraftShipmentLineProgramName | — |
| PROGRESS_PAYMENT_RATE | DraftLineProgressPaymentRate | — |
| PROGRESS_PAYMENT_RATE | FromDraftLineProgressPaymentRate | — |
| PROGRESS_PAYMENT_RATE | FromDraftShipmentLineProgressPaymentRate | — |
| PURCHASE_BASIS | DraftLinePurchaseBasis | ✅ |
| PURCHASE_BASIS | FromDraftLinePurchaseBasis | — |
| PURCHASE_BASIS | FromDraftShipmentLinePurchaseBasis | — |
| QC_GRADE | DraftLineQcGrade | — |
| QC_GRADE | FromDraftLineQcGrade | — |
| QC_GRADE | FromDraftShipmentLineQcGrade | — |
| QTY_RCV_TOLERANCE | DraftLineQtyRcvTolerance | — |
| QTY_RCV_TOLERANCE | FromDraftLineQtyRcvTolerance | — |
| QTY_RCV_TOLERANCE | FromDraftShipmentLineQtyRcvTolerance | — |
| QUANTITY | DraftLineQuantity | ✅ |
| QUANTITY | FromDraftLineQuantity | — |
| QUANTITY | FromDraftShipmentLineQuantity | — |
| QUANTITY_COMMITTED | DraftLineQuantityCommitted | — |
| QUANTITY_COMMITTED | FromDraftLineQuantityCommitted | — |
| QUANTITY_COMMITTED | FromDraftShipmentLineQuantityCommitted | — |
| REASON_FOR_CHANGE | DraftLineReasonForChange | ✅ |
| REASON_FOR_CHANGE | FromDraftLineReasonForChange | — |
| REASON_FOR_CHANGE | FromDraftShipmentLineReasonForChange | — |
| RECOUPMENT_RATE | DraftLineRecoupmentRate | — |
| RECOUPMENT_RATE | FromDraftLineRecoupmentRate | — |
| RECOUPMENT_RATE | FromDraftShipmentLineRecoupmentRate | — |
| REFERENCE_NUM | DraftLineReferenceNum | — |
| REFERENCE_NUM | FromDraftLineReferenceNum | — |
| REJECTED_BY | DraftLineRejectedBy | — |
| REJECTED_BY | FromDraftLineRejectedBy | — |
| REJECTED_BY | FromDraftShipmentLineRejectedBy | — |
| REJECTED_BY_ROLE | DraftLineRejectedByRole | — |
| REJECTED_BY_ROLE | FromDraftLineRejectedByRole | — |
| REJECTED_BY_ROLE | FromDraftShipmentLineRejectedByRole | — |
| REJECTED_REASON | DraftLineRejectedReason | — |
| REJECTED_REASON | FromDraftLineRejectedReason | — |
| REJECTED_REASON | FromDraftShipmentLineRejectedReason | — |
| REQ_BU_ID | DraftLineReqBuId | — |
| REQ_BU_ID | FromDraftLineReqBuId | — |
| REQ_BU_ID | FromDraftShipmentLineReqBuId | — |
| REQUEST_ID | DraftLineRequestId | — |
| REQUEST_ID | FromDraftLineRequestId | — |
| REQUEST_ID | FromDraftShipmentLineRequestId | — |
| RETAINAGE_RATE | DraftLineRetainageRate | — |
| RETAINAGE_RATE | FromDraftLineRetainageRate | — |
| RETAINAGE_RATE | FromDraftShipmentLineRetainageRate | — |
| RETROACTIVE_DATE | DraftLineRetroactiveDate | — |
| RETROACTIVE_DATE | FromDraftLineRetroactiveDate | — |
| RETROACTIVE_DATE | FromDraftShipmentLineRetroactiveDate | — |
| SECONDARY_QUANTITY | DraftLineSecondaryQuantity | — |
| SECONDARY_QUANTITY | FromDraftLineSecondaryQuantity | — |
| SECONDARY_QUANTITY | FromDraftShipmentLineSecondaryQuantity | — |
| SECONDARY_UOM_CODE | DraftLineSecondaryUomCode | — |
| SECONDARY_UOM_CODE | FromDraftLineSecondaryUomCode | — |
| SECONDARY_UOM_CODE | FromDraftShipmentLineSecondaryUomCode | — |
| SHIPPING_UOM_CODE | DraftLineShippingUomCode | ✅ |
| SHIPPING_UOM_QUANTITY | DraftLineShippingUomQuantity | — |
| SOURCE_DOC_REV_NUM | DraftLineSourceDocRevNum | — |
| SOURCE_DOC_REV_NUM | FromDraftLineSourceDocRevNum | — |
| SOURCE_DOC_REV_NUM | FromDraftShipmentLineSourceDocRevNum | — |
| START_DATE | DraftLineStartDate | — |
| START_DATE | FromDraftLineStartDate | — |
| START_DATE | FromDraftShipmentLineStartDate | — |
| SUPPLIER_PART_AUXID | DraftLineSupplierPartAuxid | — |
| SUPPLIER_PART_AUXID | FromDraftLineSupplierPartAuxid | — |
| SUPPLIER_PART_AUXID | FromDraftShipmentLineSupplierPartAuxid | — |
| SUPPLIER_REF_NUMBER | DraftLineSupplierRefNumber | — |
| SUPPLIER_REF_NUMBER | FromDraftLineSupplierRefNumber | — |
| SUPPLIER_REF_NUMBER | FromDraftShipmentLineSupplierRefNumber | — |
| TAX_ATTRIBUTE_UPDATE_CODE | DraftLineTaxAttributeUpdateCode | — |
| TAX_ATTRIBUTE_UPDATE_CODE | FromDraftLineTaxAttributeUpdateCode | — |
| TAX_ATTRIBUTE_UPDATE_CODE | FromDraftShipmentLineTaxAttributeUpdateCode | — |
| TAX_CODE_ID | DraftLineTaxCodeId | — |
| TAX_CODE_ID | FromDraftLineTaxCodeId | — |
| TAX_CODE_ID | FromDraftShipmentLineTaxCodeId | — |
| TAX_NAME | DraftLineTaxName | — |
| TAX_NAME | FromDraftLineTaxName | — |
| TAX_NAME | FromDraftShipmentLineTaxName | — |
| TAXABLE_FLAG | DraftLineTaxableFlag | — |
| TAXABLE_FLAG | FromDraftLineTaxableFlag | — |
| TAXABLE_FLAG | FromDraftShipmentLineTaxableFlag | — |
| TYPE_1099 | DraftLineType1099 | — |
| TYPE_1099 | FromDraftLineType1099 | — |
| TYPE_1099 | FromDraftShipmentLineType1099 | — |
| UN_NUMBER_ID | DraftLineUnNumberId | — |
| UN_NUMBER_ID | FromDraftLineUnNumberId | — |
| UN_NUMBER_ID | FromDraftShipmentLineUnNumberId | — |
| UNIT_PRICE | DraftLineUnitPrice | ✅ |
| UNIT_PRICE | FromDraftLineUnitPrice | — |
| UNIT_PRICE | FromDraftShipmentLineUnitPrice | — |
| UNORDERED_FLAG | DraftLineUnorderedFlag | — |
| UNORDERED_FLAG | FromDraftLineUnorderedFlag | — |
| UNORDERED_FLAG | FromDraftShipmentLineUnorderedFlag | — |
| UOM_CODE | DraftLineUomCode | ✅ |
| UOM_CODE | FromDraftLineUomCode | — |
| UOM_CODE | FromDraftShipmentLineUomCode | — |
| VENDOR_PRODUCT_NUM | DraftLineVendorProductNum | ✅ |
| VENDOR_PRODUCT_NUM | FromDraftLineVendorProductNum | — |
| VENDOR_PRODUCT_NUM | FromDraftShipmentLineVendorProductNum | — |

### [[draftpurchaseorderdistributionrefpvo|DraftPurchaseOrderDistributionRefPVO]] (PO · BICC: 3/318)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGING_PERIOD_DAYS | DraftLineAgingPeriodDays | — |
| ALLOW_DESCRIPTION_UPDATE_FLAG | DraftLineAllowDescriptionUpdateFlag | — |
| ALLOW_DESCRIPTION_UPDATE_FLAG | FromDraftLineAllowDescriptionUpdateFlag | — |
| ALLOW_DESCRIPTION_UPDATE_FLAG | FromDraftShipmentLineAllowDescriptionUpdateFlag | — |
| ALLOW_PRICE_OVERRIDE_FLAG | DraftLineAllowPriceOverrideFlag | — |
| ALLOW_PRICE_OVERRIDE_FLAG | FromDraftLineAllowPriceOverrideFlag | — |
| ALLOW_PRICE_OVERRIDE_FLAG | FromDraftShipmentLineAllowPriceOverrideFlag | — |
| AMOUNT | DraftLineAmount | — |
| AMOUNT | FromDraftLineAmount | — |
| AMOUNT | FromDraftShipmentLineAmount | — |
| AUCTION_DISPLAY_NUMBER | DraftLineAuctionDisplayNumber | — |
| AUCTION_DISPLAY_NUMBER | FromDraftLineAuctionDisplayNumber | — |
| AUCTION_DISPLAY_NUMBER | FromDraftShipmentLineAuctionDisplayNumber | — |
| AUCTION_HEADER_ID | DraftLineAuctionHeaderId | — |
| AUCTION_HEADER_ID | FromDraftLineAuctionHeaderId | — |
| AUCTION_HEADER_ID | FromDraftShipmentLineAuctionHeaderId | — |
| AUCTION_LINE_NUMBER | DraftLineAuctionLineNumber | — |
| AUCTION_LINE_NUMBER | FromDraftLineAuctionLineNumber | — |
| AUCTION_LINE_NUMBER | FromDraftShipmentLineAuctionLineNumber | — |
| BASE_QTY | DraftLineBaseQty | — |
| BASE_QTY | FromDraftLineBaseQty | — |
| BASE_QTY | FromDraftShipmentLineBaseQty | — |
| BASE_UNIT_PRICE | DraftLineBaseUnitPrice | — |
| BASE_UNIT_PRICE | FromDraftLineBaseUnitPrice | — |
| BASE_UNIT_PRICE | FromDraftShipmentLineBaseUnitPrice | — |
| BASE_UOM | DraftLineBaseUom | — |
| BASE_UOM | FromDraftLineBaseUom | — |
| BASE_UOM | FromDraftShipmentLineBaseUom | — |
| BID_LINE_NUMBER | DraftLineBidLineNumber | — |
| BID_LINE_NUMBER | FromDraftLineBidLineNumber | — |
| BID_LINE_NUMBER | FromDraftShipmentLineBidLineNumber | — |
| BID_NUMBER | DraftLineBidNumber | — |
| BID_NUMBER | FromDraftLineBidNumber | — |
| BID_NUMBER | FromDraftShipmentLineBidNumber | — |
| CANCEL_DATE | DraftLineCancelDate | — |
| CANCEL_DATE | FromDraftLineCancelDate | — |
| CANCEL_DATE | FromDraftShipmentLineCancelDate | — |
| CANCEL_FLAG | DraftLineCancelFlag | — |
| CANCEL_FLAG | FromDraftLineCancelFlag | — |
| CANCEL_FLAG | FromDraftShipmentLineCancelFlag | — |
| CANCEL_REASON | DraftLineCancelReason | — |
| CANCEL_REASON | FromDraftLineCancelReason | — |
| CANCEL_REASON | FromDraftShipmentLineCancelReason | — |
| CANCELLED_BY | DraftLineCancelledBy | — |
| CANCELLED_BY | FromDraftLineCancelledBy | — |
| CANCELLED_BY | FromDraftShipmentLineCancelledBy | — |
| CAPITAL_EXPENSE_FLAG | DraftLineCapitalExpenseFlag | — |
| CAPITAL_EXPENSE_FLAG | FromDraftLineCapitalExpenseFlag | — |
| CAPITAL_EXPENSE_FLAG | FromDraftShipmentLineCapitalExpenseFlag | — |
| CATEGORY_ID | DraftLineCategoryId | — |
| CATEGORY_ID | FromDraftLineCategoryId | — |
| CATEGORY_ID | FromDraftShipmentLineCategoryId | — |
| CHANGE_ACCEPTED_FLAG | DraftLineChangeAcceptedFlag | — |
| CHANGE_ACCEPTED_FLAG | FromDraftLineChangeAcceptedFlag | — |
| CHANGE_ACCEPTED_FLAG | FromDraftShipmentLineChangeAcceptedFlag | — |
| CO_AMOUNT_CANCELLED | DraftLineCoAmountCancelled | — |
| CO_AMOUNT_CANCELLED | FromDraftLineCoAmountCancelled | — |
| CO_AMOUNT_CANCELLED | FromDraftShipmentLineCoAmountCancelled | — |
| CO_QUANTITY_CANCELLED | DraftLineCoQuantityCancelled | — |
| CO_QUANTITY_CANCELLED | FromDraftLineCoQuantityCancelled | — |
| CO_QUANTITY_CANCELLED | FromDraftShipmentLineCoQuantityCancelled | — |
| COMMITTED_AMOUNT | DraftLineCommittedAmount | — |
| COMMITTED_AMOUNT | FromDraftLineCommittedAmount | — |
| COMMITTED_AMOUNT | FromDraftShipmentLineCommittedAmount | — |
| CONSIGNMENT_LINE_FLAG | DraftLineConsignmentLineFlag | — |
| CONTRACT_ID | DraftLineContractId | — |
| CONTRACT_ID | FromDraftLineContractId | — |
| CONTRACT_ID | FromDraftShipmentLineContractId | — |
| CONTRACTOR_FIRST_NAME | DraftLineContractorFirstName | — |
| CONTRACTOR_FIRST_NAME | FromDraftLineContractorFirstName | — |
| CONTRACTOR_FIRST_NAME | FromDraftShipmentLineContractorFirstName | — |
| CONTRACTOR_LAST_NAME | DraftLineContractorLastName | — |
| CONTRACTOR_LAST_NAME | FromDraftLineContractorLastName | — |
| CONTRACTOR_LAST_NAME | FromDraftShipmentLineContractorLastName | — |
| CREATED_BY | DraftLineCreatedBy | — |
| CREATED_BY | FromDraftLineCreatedBy | — |
| CREATED_BY | FromDraftShipmentLineCreatedBy | — |
| CREATION_DATE | DraftLineCreationDate | — |
| CREATION_DATE | FromDraftLineCreationDate | — |
| CREATION_DATE | FromDraftShipmentLineCreationDate | — |
| ENTITY_CHANGE_TYPE_CODE | DraftLineEntityChangeTypeCode | — |
| ENTITY_CHANGE_TYPE_CODE | FromDraftLineEntityChangeTypeCode | — |
| ENTITY_CHANGE_TYPE_CODE | FromDraftShipmentLineEntityChangeTypeCode | — |
| EXPIRATION_DATE | DraftLineExpirationDate | — |
| EXPIRATION_DATE | FromDraftLineExpirationDate | — |
| EXPIRATION_DATE | FromDraftShipmentLineExpirationDate | — |
| EXTERNAL_CHANGE_FLAG | DraftLineExternalChangeFlag | — |
| EXTERNAL_CHANGE_FLAG | FromDraftLineExternalChangeFlag | — |
| EXTERNAL_CHANGE_FLAG | FromDraftShipmentLineExternalChangeFlag | — |
| FIRM_DATE | DraftLineFirmDate | — |
| FIRM_DATE | FromDraftLineFirmDate | — |
| FIRM_DATE | FromDraftShipmentLineFirmDate | — |
| FIRM_STATUS_LOOKUP_CODE | DraftLineFirmStatusLookupCode | — |
| FIRM_STATUS_LOOKUP_CODE | FromDraftLineFirmStatusLookupCode | — |
| FIRM_STATUS_LOOKUP_CODE | FromDraftShipmentLineFirmStatusLookupCode | — |
| FROM_HEADER_ID | DraftLineFromHeaderId | — |
| FROM_HEADER_ID | FromDraftLineFromHeaderId | — |
| FROM_HEADER_ID | FromDraftShipmentLineFromHeaderId | — |
| FROM_LINE_ID | DraftLineFromLineId | — |
| FROM_LINE_ID | FromDraftLineFromLineId | — |
| FROM_LINE_ID | FromDraftShipmentLineFromLineId | — |
| FROM_LINE_LOCATION_ID | DraftLineFromLineLocationId | — |
| FROM_LINE_LOCATION_ID | FromDraftLineFromLineLocationId | — |
| FROM_LINE_LOCATION_ID | FromDraftShipmentLineFromLineLocationId | — |
| FUNDS_STATUS | DraftLineFundsStatus | — |
| FUNDS_STATUS | FromDraftLineFundsStatus | — |
| FUNDS_STATUS | FromDraftShipmentLineFundsStatus | — |
| GOVERNMENT_CONTEXT | DraftLineGovernmentContext | — |
| GOVERNMENT_CONTEXT | FromDraftLineGovernmentContext | — |
| GOVERNMENT_CONTEXT | FromDraftShipmentLineGovernmentContext | — |
| HAZARD_CLASS_ID | DraftLineHazardClassId | — |
| HAZARD_CLASS_ID | FromDraftLineHazardClassId | — |
| HAZARD_CLASS_ID | FromDraftShipmentLineHazardClassId | — |
| ITEM_DESCRIPTION | DraftLineItemDescription | — |
| ITEM_DESCRIPTION | FromDraftLineItemDescription | — |
| ITEM_DESCRIPTION | FromDraftShipmentLineItemDescription | — |
| ITEM_ID | DraftLineItemId | — |
| ITEM_ID | FromDraftLineItemId | — |
| ITEM_ID | FromDraftShipmentLineItemId | — |
| ITEM_REVISION | DraftLineItemRevision | — |
| ITEM_REVISION | FromDraftLineItemRevision | — |
| ITEM_REVISION | FromDraftShipmentLineItemRevision | — |
| JOB_DEFINITION_NAME | DraftLineJobDefinitionName | — |
| JOB_DEFINITION_NAME | FromDraftLineJobDefinitionName | — |
| JOB_DEFINITION_NAME | FromDraftShipmentLineJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | DraftLineJobDefinitionPackage | — |
| JOB_DEFINITION_PACKAGE | FromDraftLineJobDefinitionPackage | — |
| JOB_DEFINITION_PACKAGE | FromDraftShipmentLineJobDefinitionPackage | — |
| JOB_ID | DraftLineJobId | — |
| JOB_ID | FromDraftLineJobId | — |
| JOB_ID | FromDraftShipmentLineJobId | — |
| LAST_UPDATE_DATE | DraftLineLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | FromDraftLineLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | FromDraftShipmentLineLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DraftLineLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | FromDraftLineLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | FromDraftShipmentLineLastUpdateLogin | — |
| LAST_UPDATED_BY | DraftLineLastUpdatedBy | — |
| LAST_UPDATED_BY | FromDraftLineLastUpdatedBy | — |
| LAST_UPDATED_BY | FromDraftShipmentLineLastUpdatedBy | — |
| LINE_NUM | DraftLineLineNum | — |
| LINE_NUM | FromDraftLineLineNum | — |
| LINE_NUM | FromDraftShipmentLineLineNum | — |
| LINE_REFERENCE_NUM | DraftLineLineReferenceNum | — |
| LINE_REFERENCE_NUM | FromDraftLineLineReferenceNum | — |
| LINE_REFERENCE_NUM | FromDraftShipmentLineLineReferenceNum | — |
| LINE_TYPE_ID | DraftLineLineTypeId | — |
| LINE_TYPE_ID | FromDraftLineLineTypeId | — |
| LINE_TYPE_ID | FromDraftShipmentLineLineTypeId | — |
| LIST_PRICE_PER_UNIT | DraftLineListPricePerUnit | — |
| LIST_PRICE_PER_UNIT | FromDraftLineListPricePerUnit | — |
| LIST_PRICE_PER_UNIT | FromDraftShipmentLineListPricePerUnit | — |
| MANUAL_PRICE_CHANGE_FLAG | DraftLineManualPriceChangeFlag | — |
| MANUAL_PRICE_CHANGE_FLAG | FromDraftLineManualPriceChangeFlag | — |
| MANUAL_PRICE_CHANGE_FLAG | FromDraftShipmentLineManualPriceChangeFlag | — |
| MARKET_PRICE | DraftLineMarketPrice | — |
| MARKET_PRICE | FromDraftLineMarketPrice | — |
| MARKET_PRICE | FromDraftShipmentLineMarketPrice | — |
| MATCHING_BASIS | DraftLineMatchingBasis | — |
| MATCHING_BASIS | FromDraftLineMatchingBasis | — |
| MATCHING_BASIS | FromDraftShipmentLineMatchingBasis | — |
| MAX_RETAINAGE_AMOUNT | DraftLineMaxRetainageAmount | — |
| MAX_RETAINAGE_AMOUNT | FromDraftLineMaxRetainageAmount | — |
| MAX_RETAINAGE_AMOUNT | FromDraftShipmentLineMaxRetainageAmount | — |
| MIN_RELEASE_AMOUNT | DraftLineMinReleaseAmount | — |
| MIN_RELEASE_AMOUNT | FromDraftLineMinReleaseAmount | — |
| MIN_RELEASE_AMOUNT | FromDraftShipmentLineMinReleaseAmount | — |
| NEGOTIATED_BY_PREPARER_FLAG | DraftLineNegotiatedByPreparerFlag | — |
| NEGOTIATED_BY_PREPARER_FLAG | FromDraftLineNegotiatedByPreparerFlag | — |
| NEGOTIATED_BY_PREPARER_FLAG | FromDraftShipmentLineNegotiatedByPreparerFlag | — |
| NOT_TO_EXCEED_PRICE | DraftLineNotToExceedPrice | — |
| NOT_TO_EXCEED_PRICE | FromDraftLineNotToExceedPrice | — |
| NOT_TO_EXCEED_PRICE | FromDraftShipmentLineNotToExceedPrice | — |
| NOTE_TO_VENDOR | DraftLineNoteToVendor | — |
| NOTE_TO_VENDOR | FromDraftLineNoteToVendor | — |
| NOTE_TO_VENDOR | FromDraftShipmentLineNoteToVendor | — |
| OBJECT_VERSION_NUMBER | DraftLineObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | FromDraftLineObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | FromDraftShipmentLineObjectVersionNumber | — |
| OKE_CONTRACT_HEADER_ID | DraftLineOkeContractHeaderId | — |
| OKE_CONTRACT_HEADER_ID | FromDraftLineOkeContractHeaderId | — |
| OKE_CONTRACT_HEADER_ID | FromDraftShipmentLineOkeContractHeaderId | — |
| OKE_CONTRACT_VERSION_ID | DraftLineOkeContractVersionId | — |
| OKE_CONTRACT_VERSION_ID | FromDraftLineOkeContractVersionId | — |
| OKE_CONTRACT_VERSION_ID | FromDraftShipmentLineOkeContractVersionId | — |
| ORDER_TYPE_LOOKUP_CODE | DraftLineOrderTypeLookupCode | — |
| ORDER_TYPE_LOOKUP_CODE | FromDraftLineOrderTypeLookupCode | — |
| ORDER_TYPE_LOOKUP_CODE | FromDraftShipmentLineOrderTypeLookupCode | — |
| ORIGINAL_INTERFACE_LINE_ID | DraftLineOriginalInterfaceLineId | — |
| ORIGINAL_INTERFACE_LINE_ID | FromDraftLineOriginalInterfaceLineId | — |
| ORIGINAL_INTERFACE_LINE_ID | FromDraftShipmentLineOriginalInterfaceLineId | — |
| OVER_TOLERANCE_ERROR_FLAG | DraftLineOverToleranceErrorFlag | — |
| OVER_TOLERANCE_ERROR_FLAG | FromDraftLineOverToleranceErrorFlag | — |
| OVER_TOLERANCE_ERROR_FLAG | FromDraftShipmentLineOverToleranceErrorFlag | — |
| PJC_CONTEXT_CATEGORY | DraftLinePjcContextCategory | — |
| PJC_CONTEXT_CATEGORY | FromDraftLinePjcContextCategory | — |
| PJC_CONTEXT_CATEGORY | FromDraftShipmentLinePjcContextCategory | — |
| PO_HEADER_ID | DraftLinePoHeaderId | — |
| PO_HEADER_ID | FromDraftLinePoHeaderId | — |
| PO_HEADER_ID | FromDraftShipmentLinePoHeaderId | — |
| PO_LINE_ID | DraftLinePoLineId | — |
| PO_LINE_ID | FromDraftLinePoLineId | — |
| PO_LINE_ID | FromDraftShipmentLinePoLineId | — |
| PRC_BU_ID | DraftLinePrcBuId | — |
| PRC_BU_ID | FromDraftLinePrcBuId | — |
| PRC_BU_ID | FromDraftShipmentLinePrcBuId | — |
| PREFERRED_GRADE | DraftLinePreferredGrade | — |
| PREFERRED_GRADE | FromDraftLinePreferredGrade | — |
| PREFERRED_GRADE | FromDraftShipmentLinePreferredGrade | — |
| PRICE_BREAK_LOOKUP_CODE | DraftLinePriceBreakLookupCode | — |
| PRICE_BREAK_LOOKUP_CODE | FromDraftLinePriceBreakLookupCode | — |
| PRICE_BREAK_LOOKUP_CODE | FromDraftShipmentLinePriceBreakLookupCode | — |
| PRICE_TYPE_LOOKUP_CODE | DraftLinePriceTypeLookupCode | — |
| PRICE_TYPE_LOOKUP_CODE | FromDraftLinePriceTypeLookupCode | — |
| PRICE_TYPE_LOOKUP_CODE | FromDraftShipmentLinePriceTypeLookupCode | — |
| PROGRAM_APP_NAME | DraftLineProgramAppName | — |
| PROGRAM_APP_NAME | FromDraftLineProgramAppName | — |
| PROGRAM_APP_NAME | FromDraftShipmentLineProgramAppName | — |
| PROGRAM_NAME | DraftLineProgramName | — |
| PROGRAM_NAME | FromDraftLineProgramName | — |
| PROGRAM_NAME | FromDraftShipmentLineProgramName | — |
| PROGRESS_PAYMENT_RATE | DraftLineProgressPaymentRate | — |
| PROGRESS_PAYMENT_RATE | FromDraftLineProgressPaymentRate | — |
| PROGRESS_PAYMENT_RATE | FromDraftShipmentLineProgressPaymentRate | — |
| PURCHASE_BASIS | DraftLinePurchaseBasis | — |
| PURCHASE_BASIS | FromDraftLinePurchaseBasis | — |
| PURCHASE_BASIS | FromDraftShipmentLinePurchaseBasis | — |
| QC_GRADE | DraftLineQcGrade | — |
| QC_GRADE | FromDraftLineQcGrade | — |
| QC_GRADE | FromDraftShipmentLineQcGrade | — |
| QTY_RCV_TOLERANCE | DraftLineQtyRcvTolerance | — |
| QTY_RCV_TOLERANCE | FromDraftLineQtyRcvTolerance | — |
| QTY_RCV_TOLERANCE | FromDraftShipmentLineQtyRcvTolerance | — |
| QUANTITY | DraftLineQuantity | — |
| QUANTITY | FromDraftLineQuantity | — |
| QUANTITY | FromDraftShipmentLineQuantity | — |
| QUANTITY_COMMITTED | DraftLineQuantityCommitted | — |
| QUANTITY_COMMITTED | FromDraftLineQuantityCommitted | — |
| QUANTITY_COMMITTED | FromDraftShipmentLineQuantityCommitted | — |
| REASON_FOR_CHANGE | DraftLineReasonForChange | — |
| REASON_FOR_CHANGE | FromDraftLineReasonForChange | — |
| REASON_FOR_CHANGE | FromDraftShipmentLineReasonForChange | — |
| RECOUPMENT_RATE | DraftLineRecoupmentRate | — |
| RECOUPMENT_RATE | FromDraftLineRecoupmentRate | — |
| RECOUPMENT_RATE | FromDraftShipmentLineRecoupmentRate | — |
| REFERENCE_NUM | DraftLineReferenceNum | — |
| REFERENCE_NUM | FromDraftLineReferenceNum | — |
| REJECTED_BY | DraftLineRejectedBy | — |
| REJECTED_BY | FromDraftLineRejectedBy | — |
| REJECTED_BY | FromDraftShipmentLineRejectedBy | — |
| REJECTED_BY_ROLE | DraftLineRejectedByRole | — |
| REJECTED_BY_ROLE | FromDraftLineRejectedByRole | — |
| REJECTED_BY_ROLE | FromDraftShipmentLineRejectedByRole | — |
| REJECTED_REASON | DraftLineRejectedReason | — |
| REJECTED_REASON | FromDraftLineRejectedReason | — |
| REJECTED_REASON | FromDraftShipmentLineRejectedReason | — |
| REQ_BU_ID | DraftLineReqBuId | — |
| REQ_BU_ID | FromDraftLineReqBuId | — |
| REQ_BU_ID | FromDraftShipmentLineReqBuId | — |
| REQUEST_ID | DraftLineRequestId | — |
| REQUEST_ID | FromDraftLineRequestId | — |
| REQUEST_ID | FromDraftShipmentLineRequestId | — |
| RETAINAGE_RATE | DraftLineRetainageRate | — |
| RETAINAGE_RATE | FromDraftLineRetainageRate | — |
| RETAINAGE_RATE | FromDraftShipmentLineRetainageRate | — |
| RETROACTIVE_DATE | DraftLineRetroactiveDate | — |
| RETROACTIVE_DATE | FromDraftLineRetroactiveDate | — |
| RETROACTIVE_DATE | FromDraftShipmentLineRetroactiveDate | — |
| SECONDARY_QUANTITY | DraftLineSecondaryQuantity | — |
| SECONDARY_QUANTITY | FromDraftLineSecondaryQuantity | — |
| SECONDARY_QUANTITY | FromDraftShipmentLineSecondaryQuantity | — |
| SECONDARY_UOM_CODE | DraftLineSecondaryUomCode | — |
| SECONDARY_UOM_CODE | FromDraftLineSecondaryUomCode | — |
| SECONDARY_UOM_CODE | FromDraftShipmentLineSecondaryUomCode | — |
| SHIPPING_UOM_CODE | DraftLineShippingUomCode | — |
| SHIPPING_UOM_QUANTITY | DraftLineShippingUomQuantity | — |
| SOURCE_DOC_REV_NUM | DraftLineSourceDocRevNum | — |
| SOURCE_DOC_REV_NUM | FromDraftLineSourceDocRevNum | — |
| SOURCE_DOC_REV_NUM | FromDraftShipmentLineSourceDocRevNum | — |
| START_DATE | DraftLineStartDate | — |
| START_DATE | FromDraftLineStartDate | — |
| START_DATE | FromDraftShipmentLineStartDate | — |
| SUPPLIER_PART_AUXID | DraftLineSupplierPartAuxid | — |
| SUPPLIER_PART_AUXID | FromDraftLineSupplierPartAuxid | — |
| SUPPLIER_PART_AUXID | FromDraftShipmentLineSupplierPartAuxid | — |
| SUPPLIER_REF_NUMBER | DraftLineSupplierRefNumber | — |
| SUPPLIER_REF_NUMBER | FromDraftLineSupplierRefNumber | — |
| SUPPLIER_REF_NUMBER | FromDraftShipmentLineSupplierRefNumber | — |
| TAX_ATTRIBUTE_UPDATE_CODE | DraftLineTaxAttributeUpdateCode | — |
| TAX_ATTRIBUTE_UPDATE_CODE | FromDraftLineTaxAttributeUpdateCode | — |
| TAX_ATTRIBUTE_UPDATE_CODE | FromDraftShipmentLineTaxAttributeUpdateCode | — |
| TAX_CODE_ID | DraftLineTaxCodeId | — |
| TAX_CODE_ID | FromDraftLineTaxCodeId | — |
| TAX_CODE_ID | FromDraftShipmentLineTaxCodeId | — |
| TAX_NAME | DraftLineTaxName | — |
| TAX_NAME | FromDraftLineTaxName | — |
| TAX_NAME | FromDraftShipmentLineTaxName | — |
| TAXABLE_FLAG | DraftLineTaxableFlag | — |
| TAXABLE_FLAG | FromDraftLineTaxableFlag | — |
| TAXABLE_FLAG | FromDraftShipmentLineTaxableFlag | — |
| TYPE_1099 | DraftLineType1099 | — |
| TYPE_1099 | FromDraftLineType1099 | — |
| TYPE_1099 | FromDraftShipmentLineType1099 | — |
| UN_NUMBER_ID | DraftLineUnNumberId | — |
| UN_NUMBER_ID | FromDraftLineUnNumberId | — |
| UN_NUMBER_ID | FromDraftShipmentLineUnNumberId | — |
| UNIT_PRICE | DraftLineUnitPrice | — |
| UNIT_PRICE | FromDraftLineUnitPrice | — |
| UNIT_PRICE | FromDraftShipmentLineUnitPrice | — |
| UNORDERED_FLAG | DraftLineUnorderedFlag | — |
| UNORDERED_FLAG | FromDraftLineUnorderedFlag | — |
| UNORDERED_FLAG | FromDraftShipmentLineUnorderedFlag | — |
| UOM_CODE | DraftLineUomCode | — |
| UOM_CODE | FromDraftLineUomCode | — |
| UOM_CODE | FromDraftShipmentLineUomCode | — |
| VENDOR_PRODUCT_NUM | DraftLineVendorProductNum | — |
| VENDOR_PRODUCT_NUM | FromDraftLineVendorProductNum | — |
| VENDOR_PRODUCT_NUM | FromDraftShipmentLineVendorProductNum | — |

### [[draftpurchasingdocumentlineextractpvo|DraftPurchasingDocumentLineExtractPVO]] (PO · BICC: 113/118)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGING_PERIOD_DAYS | AgingPeriodDays | ✅ |
| ALLOW_DESCRIPTION_UPDATE_FLAG | AllowDescriptionUpdateFlag | ✅ |
| ALLOW_PRICE_OVERRIDE_FLAG | AllowPriceOverrideFlag | ✅ |
| AMOUNT | Amount | ✅ |
| AUCTION_DISPLAY_NUMBER | AuctionDisplayNumber | ✅ |
| AUCTION_HEADER_ID | AuctionHeaderId | ✅ |
| AUCTION_LINE_NUMBER | AuctionLineNumber | ✅ |
| BASE_MODEL_ID | BaseModelId | ✅ |
| BASE_MODEL_PRICE | BaseModelPrice | ✅ |
| BASE_QTY | BaseQty | ✅ |
| BASE_UNIT_PRICE | BaseUnitPrice | ✅ |
| BASE_UOM | BaseUom | ✅ |
| BID_LINE_NUMBER | BidLineNumber | ✅ |
| BID_NUMBER | BidNumber | ✅ |
| CANCEL_DATE | CancelDate | ✅ |
| CANCEL_FLAG | CancelFlag | ✅ |
| CANCEL_REASON | CancelReason | ✅ |
| CANCELLED_BY | CancelledBy | ✅ |
| CAPITAL_EXPENSE_FLAG | CapitalExpenseFlag | ✅ |
| CATEGORY_ID | CategoryId | ✅ |
| CHANGE_ACCEPTED_FLAG | ChangeAcceptedFlag | ✅ |
| CO_AMOUNT_CANCELLED | CoAmountCancelled | ✅ |
| CO_QUANTITY_CANCELLED | CoQuantityCancelled | ✅ |
| COMMITTED_AMOUNT | CommittedAmount | ✅ |
| CONFIGURED_ITEM_FLAG | ConfiguredItemFlag | ✅ |
| CONSIGNMENT_LINE_FLAG | ConsignmentLineFlag | ✅ |
| CONTRACT_ID | ContractId | ✅ |
| CONTRACTOR_FIRST_NAME | ContractorFirstName | ✅ |
| CONTRACTOR_LAST_NAME | ContractorLastName | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| ENTITY_CHANGE_TYPE_CODE | EntityChangeTypeCode | ✅ |
| EXPIRATION_DATE | ExpirationDate | ✅ |
| EXTERNAL_CHANGE_FLAG | ExternalChangeFlag | ✅ |
| FROM_HEADER_ID | FromHeaderId | ✅ |
| FROM_LINE_ID | FromLineId | ✅ |
| FROM_LINE_LOCATION_ID | FromLineLocationId | ✅ |
| FUNDS_STATUS | FundsStatus | ✅ |
| HAZARD_CLASS_ID | HazardClassId | ✅ |
| ITEM_DESCRIPTION | ItemDescription | ✅ |
| ITEM_ID | ItemId | ✅ |
| ITEM_REVISION | ItemRevision | ✅ |
| JOB_DEFINITION_NAME | JobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | JobDefinitionPackage | — |
| JOB_ID | JobId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LINE_NUM | LineNum | ✅ |
| LINE_REFERENCE_NUM | LineReferenceNum | ✅ |
| LINE_START_DATE | LineStartDate | — |
| LINE_TYPE_ID | LineTypeId | ✅ |
| LIST_PRICE_PER_UNIT | ListPricePerUnit | ✅ |
| MANUAL_PRICE_CHANGE_FLAG | ManualPriceChangeFlag | ✅ |
| MANUFACTURER | Manufacturer | ✅ |
| MANUFACTURER_PART_NUM | ManufacturerPartNum | ✅ |
| MARKET_PRICE | MarketPrice | ✅ |
| MATCHING_BASIS | MatchingBasis | ✅ |
| MAX_RETAINAGE_AMOUNT | MaxRetainageAmount | ✅ |
| MIN_RELEASE_AMOUNT | MinReleaseAmount | ✅ |
| NEGOTIATED_BY_PREPARER_FLAG | NegotiatedByPreparerFlag | ✅ |
| NOT_TO_EXCEED_PRICE | NotToExceedPrice | ✅ |
| NOTE_TO_VENDOR | NoteToVendor | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| OKE_CONTRACT_HEADER_ID | OkeContractHeaderId | ✅ |
| OKE_CONTRACT_VERSION_ID | OkeContractVersionId | ✅ |
| OPTIONS_PRICE | OptionsPrice | ✅ |
| ORDER_TYPE_LOOKUP_CODE | OrderTypeLookupCode | ✅ |
| ORIGINAL_INTERFACE_LINE_ID | OriginalInterfaceLineId | ✅ |
| OVER_TOLERANCE_ERROR_FLAG | OverToleranceErrorFlag | ✅ |
| PARENT_ITEM_ID | ParentItemId | ✅ |
| PJC_CONTEXT_CATEGORY | PjcContextCategory | ✅ |
| PO_HEADER_ID | PoHeaderId | ✅ |
| PO_LINE_ID | PoLineId | ✅ |
| PRC_BU_ID | PrcBuId | ✅ |
| PREFERRED_GRADE | PreferredGrade | — |
| PRICE_BREAK_LOOKUP_CODE | PriceBreakLookupCode | ✅ |
| PRICE_TYPE_LOOKUP_CODE | PriceTypeLookupCode | ✅ |
| PROGRAM_APP_NAME | ProgramAppName | ✅ |
| PROGRAM_NAME | ProgramName | ✅ |
| PROGRESS_PAYMENT_RATE | ProgressPaymentRate | — |
| PURCHASE_BASIS | PurchaseBasis | ✅ |
| QC_GRADE | QcGrade | ✅ |
| QTY_RCV_TOLERANCE | QtyRcvTolerance | ✅ |
| QUANTITY | Quantity | ✅ |
| QUANTITY_COMMITTED | QuantityCommitted | ✅ |
| REASON_FOR_CHANGE | ReasonForChange | ✅ |
| RECOUPMENT_RATE | RecoupmentRate | ✅ |
| REJECTED_BY | RejectedBy | ✅ |
| REJECTED_BY_ROLE | RejectedByRole | ✅ |
| REJECTED_REASON | RejectedReason | ✅ |
| REQ_BU_ID | ReqBuId | ✅ |
| REQUEST_ID | RequestId | ✅ |
| RETAINAGE_RATE | RetainageRate | ✅ |
| RETROACTIVE_DATE | RetroactiveDate | ✅ |
| SECONDARY_QUANTITY | SecondaryQuantity | ✅ |
| SECONDARY_UOM_CODE | SecondaryUomCode | ✅ |
| SHIPPING_UOM_CODE | ShippingUomCode | ✅ |
| SHIPPING_UOM_QUANTITY | ShippingUomQuantity | ✅ |
| SOURCE_DOC_REV_NUM | SourceDocRevNum | ✅ |
| START_DATE | StartDate | ✅ |
| SUPPLIER_PARENT_ITEM | SupplierParentItem | ✅ |
| SUPPLIER_PART_AUXID | SupplierPartAuxid | ✅ |
| SUPPLIER_REF_NUMBER | SupplierRefNumber | ✅ |
| SUPPLIER_TOP_MODEL | SupplierTopModel | ✅ |
| TAX_ATTRIBUTE_UPDATE_CODE | TaxAttributeUpdateCode | ✅ |
| TAX_CODE_ID | TaxCodeId | ✅ |
| TAX_EXCLUSIVE_PRICE | TaxExclusivePrice | ✅ |
| TAX_NAME | TaxName | ✅ |
| TAXABLE_FLAG | TaxableFlag | ✅ |
| TOP_MODEL_ID | TopModelId | ✅ |
| TYPE_1099 | Type1099 | ✅ |
| UN_NUMBER_ID | UnNumberId | ✅ |
| UNIT_PRICE | UnitPrice | ✅ |
| UNORDERED_FLAG | UnorderedFlag | ✅ |
| UOM_CODE | UomCode | ✅ |
| VENDOR_PRODUCT_NUM | VendorProductNum | ✅ |
| WORK_ORDER_PRODUCT | WorkOrderProduct | ✅ |

### [[draftpurchasingdocumentlinelocationpvo|DraftPurchasingDocumentLineLocationPVO]] (PO · BICC: 19/214)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGING_PERIOD_DAYS | DraftLineAgingPeriodDays | — |
| ALLOW_DESCRIPTION_UPDATE_FLAG | DraftLineAllowDescriptionUpdateFlag | — |
| ALLOW_DESCRIPTION_UPDATE_FLAG | FromDraftLineAllowDescriptionUpdateFlag | — |
| ALLOW_PRICE_OVERRIDE_FLAG | DraftLineAllowPriceOverrideFlag | — |
| ALLOW_PRICE_OVERRIDE_FLAG | FromDraftLineAllowPriceOverrideFlag | — |
| AMOUNT | DraftLineAmount | — |
| AMOUNT | FromDraftLineAmount | — |
| AUCTION_DISPLAY_NUMBER | DraftLineAuctionDisplayNumber | — |
| AUCTION_DISPLAY_NUMBER | FromDraftLineAuctionDisplayNumber | — |
| AUCTION_HEADER_ID | DraftLineAuctionHeaderId | — |
| AUCTION_HEADER_ID | FromDraftLineAuctionHeaderId | — |
| AUCTION_LINE_NUMBER | DraftLineAuctionLineNumber | — |
| AUCTION_LINE_NUMBER | FromDraftLineAuctionLineNumber | — |
| BASE_QTY | DraftLineBaseQty | — |
| BASE_QTY | FromDraftLineBaseQty | — |
| BASE_UNIT_PRICE | DraftLineBaseUnitPrice | — |
| BASE_UNIT_PRICE | FromDraftLineBaseUnitPrice | — |
| BASE_UOM | DraftLineBaseUom | — |
| BASE_UOM | FromDraftLineBaseUom | — |
| BID_LINE_NUMBER | DraftLineBidLineNumber | — |
| BID_LINE_NUMBER | FromDraftLineBidLineNumber | — |
| BID_NUMBER | DraftLineBidNumber | — |
| BID_NUMBER | FromDraftLineBidNumber | — |
| CANCEL_DATE | DraftLineCancelDate | — |
| CANCEL_DATE | FromDraftLineCancelDate | — |
| CANCEL_FLAG | DraftLineCancelFlag | — |
| CANCEL_FLAG | FromDraftLineCancelFlag | — |
| CANCEL_REASON | DraftLineCancelReason | — |
| CANCEL_REASON | FromDraftLineCancelReason | — |
| CANCELLED_BY | DraftLineCancelledBy | — |
| CANCELLED_BY | FromDraftLineCancelledBy | — |
| CAPITAL_EXPENSE_FLAG | DraftLineCapitalExpenseFlag | — |
| CAPITAL_EXPENSE_FLAG | FromDraftLineCapitalExpenseFlag | — |
| CATEGORY_ID | DraftLineCategoryId | — |
| CATEGORY_ID | FromDraftLineCategoryId | — |
| CHANGE_ACCEPTED_FLAG | DraftLineChangeAcceptedFlag | — |
| CHANGE_ACCEPTED_FLAG | FromDraftLineChangeAcceptedFlag | — |
| CO_AMOUNT_CANCELLED | DraftLineCoAmountCancelled | — |
| CO_AMOUNT_CANCELLED | FromDraftLineCoAmountCancelled | — |
| CO_QUANTITY_CANCELLED | DraftLineCoQuantityCancelled | — |
| CO_QUANTITY_CANCELLED | FromDraftLineCoQuantityCancelled | — |
| COMMITTED_AMOUNT | DraftLineCommittedAmount | — |
| COMMITTED_AMOUNT | FromDraftLineCommittedAmount | — |
| CONSIGNMENT_LINE_FLAG | DraftLineConsignmentLineFlag | ✅ |
| CONTRACT_ID | DraftLineContractId | — |
| CONTRACT_ID | FromDraftLineContractId | — |
| CONTRACTOR_FIRST_NAME | DraftLineContractorFirstName | — |
| CONTRACTOR_FIRST_NAME | FromDraftLineContractorFirstName | — |
| CONTRACTOR_LAST_NAME | DraftLineContractorLastName | — |
| CONTRACTOR_LAST_NAME | FromDraftLineContractorLastName | — |
| CREATED_BY | DraftLineCreatedBy | — |
| CREATED_BY | FromDraftLineCreatedBy | — |
| CREATION_DATE | DraftLineCreationDate | — |
| CREATION_DATE | FromDraftLineCreationDate | — |
| ENTITY_CHANGE_TYPE_CODE | DraftLineEntityChangeTypeCode | — |
| ENTITY_CHANGE_TYPE_CODE | FromDraftLineEntityChangeTypeCode | — |
| EXPIRATION_DATE | DraftLineExpirationDate | — |
| EXPIRATION_DATE | FromDraftLineExpirationDate | — |
| EXTERNAL_CHANGE_FLAG | DraftLineExternalChangeFlag | — |
| EXTERNAL_CHANGE_FLAG | FromDraftLineExternalChangeFlag | — |
| FIRM_DATE | DraftLineFirmDate | — |
| FIRM_DATE | FromDraftLineFirmDate | — |
| FIRM_STATUS_LOOKUP_CODE | DraftLineFirmStatusLookupCode | — |
| FIRM_STATUS_LOOKUP_CODE | FromDraftLineFirmStatusLookupCode | — |
| FROM_HEADER_ID | DraftLineFromHeaderId | — |
| FROM_HEADER_ID | FromDraftLineFromHeaderId | — |
| FROM_LINE_ID | DraftLineFromLineId | — |
| FROM_LINE_ID | FromDraftLineFromLineId | — |
| FROM_LINE_LOCATION_ID | DraftLineFromLineLocationId | — |
| FROM_LINE_LOCATION_ID | FromDraftLineFromLineLocationId | — |
| FUNDS_STATUS | DraftLineFundsStatus | ✅ |
| FUNDS_STATUS | FromDraftLineFundsStatus | — |
| GOVERNMENT_CONTEXT | DraftLineGovernmentContext | — |
| GOVERNMENT_CONTEXT | FromDraftLineGovernmentContext | — |
| HAZARD_CLASS_ID | DraftLineHazardClassId | — |
| HAZARD_CLASS_ID | FromDraftLineHazardClassId | — |
| ITEM_DESCRIPTION | DraftLineItemDescription | ✅ |
| ITEM_DESCRIPTION | FromDraftLineItemDescription | — |
| ITEM_ID | DraftLineItemId | ✅ |
| ITEM_ID | FromDraftLineItemId | — |
| ITEM_REVISION | DraftLineItemRevision | ✅ |
| ITEM_REVISION | FromDraftLineItemRevision | — |
| JOB_DEFINITION_NAME | DraftLineJobDefinitionName | — |
| JOB_DEFINITION_NAME | FromDraftLineJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | DraftLineJobDefinitionPackage | — |
| JOB_DEFINITION_PACKAGE | FromDraftLineJobDefinitionPackage | — |
| JOB_ID | DraftLineJobId | — |
| JOB_ID | FromDraftLineJobId | — |
| LAST_UPDATE_DATE | DraftLineLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | FromDraftLineLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DraftLineLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | FromDraftLineLastUpdateLogin | — |
| LAST_UPDATED_BY | DraftLineLastUpdatedBy | — |
| LAST_UPDATED_BY | FromDraftLineLastUpdatedBy | — |
| LINE_NUM | DraftLineLineNum | ✅ |
| LINE_NUM | FromDraftLineLineNum | — |
| LINE_REFERENCE_NUM | DraftLineLineReferenceNum | — |
| LINE_REFERENCE_NUM | FromDraftLineLineReferenceNum | — |
| LINE_START_DATE | DraftLineLineStartDate | — |
| LINE_TYPE_ID | DraftLineLineTypeId | — |
| LINE_TYPE_ID | FromDraftLineLineTypeId | — |
| LIST_PRICE_PER_UNIT | DraftLineListPricePerUnit | — |
| LIST_PRICE_PER_UNIT | FromDraftLineListPricePerUnit | — |
| MANUAL_PRICE_CHANGE_FLAG | DraftLineManualPriceChangeFlag | — |
| MANUAL_PRICE_CHANGE_FLAG | FromDraftLineManualPriceChangeFlag | — |
| MARKET_PRICE | DraftLineMarketPrice | — |
| MARKET_PRICE | FromDraftLineMarketPrice | — |
| MATCHING_BASIS | DraftLineMatchingBasis | — |
| MATCHING_BASIS | FromDraftLineMatchingBasis | — |
| MAX_RETAINAGE_AMOUNT | DraftLineMaxRetainageAmount | — |
| MAX_RETAINAGE_AMOUNT | FromDraftLineMaxRetainageAmount | — |
| MIN_RELEASE_AMOUNT | DraftLineMinReleaseAmount | ✅ |
| MIN_RELEASE_AMOUNT | FromDraftLineMinReleaseAmount | — |
| NEGOTIATED_BY_PREPARER_FLAG | DraftLineNegotiatedByPreparerFlag | ✅ |
| NEGOTIATED_BY_PREPARER_FLAG | FromDraftLineNegotiatedByPreparerFlag | — |
| NOT_TO_EXCEED_PRICE | DraftLineNotToExceedPrice | — |
| NOT_TO_EXCEED_PRICE | FromDraftLineNotToExceedPrice | — |
| NOTE_TO_VENDOR | DraftLineNoteToVendor | ✅ |
| NOTE_TO_VENDOR | FromDraftLineNoteToVendor | — |
| OBJECT_VERSION_NUMBER | DraftLineObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | FromDraftLineObjectVersionNumber | — |
| OKE_CONTRACT_HEADER_ID | DraftLineOkeContractHeaderId | — |
| OKE_CONTRACT_HEADER_ID | FromDraftLineOkeContractHeaderId | — |
| OKE_CONTRACT_VERSION_ID | DraftLineOkeContractVersionId | — |
| OKE_CONTRACT_VERSION_ID | FromDraftLineOkeContractVersionId | — |
| ORDER_TYPE_LOOKUP_CODE | DraftLineOrderTypeLookupCode | — |
| ORDER_TYPE_LOOKUP_CODE | FromDraftLineOrderTypeLookupCode | — |
| ORIGINAL_INTERFACE_LINE_ID | DraftLineOriginalInterfaceLineId | — |
| ORIGINAL_INTERFACE_LINE_ID | FromDraftLineOriginalInterfaceLineId | — |
| OVER_TOLERANCE_ERROR_FLAG | DraftLineOverToleranceErrorFlag | — |
| OVER_TOLERANCE_ERROR_FLAG | FromDraftLineOverToleranceErrorFlag | — |
| PJC_CONTEXT_CATEGORY | DraftLinePjcContextCategory | — |
| PJC_CONTEXT_CATEGORY | FromDraftLinePjcContextCategory | — |
| PO_HEADER_ID | DraftLinePoHeaderId | — |
| PO_HEADER_ID | FromDraftLinePoHeaderId | — |
| PO_LINE_ID | DraftLinePoLineId | ✅ |
| PO_LINE_ID | FromDraftLinePoLineId | — |
| PRC_BU_ID | DraftLinePrcBuId | — |
| PRC_BU_ID | FromDraftLinePrcBuId | — |
| PREFERRED_GRADE | DraftLinePreferredGrade | — |
| PREFERRED_GRADE | FromDraftLinePreferredGrade | — |
| PRICE_BREAK_LOOKUP_CODE | DraftLinePriceBreakLookupCode | — |
| PRICE_BREAK_LOOKUP_CODE | FromDraftLinePriceBreakLookupCode | — |
| PRICE_TYPE_LOOKUP_CODE | DraftLinePriceTypeLookupCode | — |
| PRICE_TYPE_LOOKUP_CODE | FromDraftLinePriceTypeLookupCode | — |
| PROGRAM_APP_NAME | DraftLineProgramAppName | — |
| PROGRAM_APP_NAME | FromDraftLineProgramAppName | — |
| PROGRAM_NAME | DraftLineProgramName | — |
| PROGRAM_NAME | FromDraftLineProgramName | — |
| PROGRESS_PAYMENT_RATE | DraftLineProgressPaymentRate | — |
| PROGRESS_PAYMENT_RATE | FromDraftLineProgressPaymentRate | — |
| PURCHASE_BASIS | DraftLinePurchaseBasis | ✅ |
| PURCHASE_BASIS | FromDraftLinePurchaseBasis | — |
| QC_GRADE | DraftLineQcGrade | — |
| QC_GRADE | FromDraftLineQcGrade | — |
| QTY_RCV_TOLERANCE | DraftLineQtyRcvTolerance | — |
| QTY_RCV_TOLERANCE | FromDraftLineQtyRcvTolerance | — |
| QUANTITY | DraftLineQuantity | ✅ |
| QUANTITY | FromDraftLineQuantity | — |
| QUANTITY_COMMITTED | DraftLineQuantityCommitted | — |
| QUANTITY_COMMITTED | FromDraftLineQuantityCommitted | — |
| REASON_FOR_CHANGE | DraftLineReasonForChange | ✅ |
| REASON_FOR_CHANGE | FromDraftLineReasonForChange | — |
| RECOUPMENT_RATE | DraftLineRecoupmentRate | — |
| RECOUPMENT_RATE | FromDraftLineRecoupmentRate | — |
| REFERENCE_NUM | DraftLineReferenceNum | — |
| REFERENCE_NUM | FromDraftLineReferenceNum | — |
| REJECTED_BY | DraftLineRejectedBy | — |
| REJECTED_BY | FromDraftLineRejectedBy | — |
| REJECTED_BY_ROLE | DraftLineRejectedByRole | — |
| REJECTED_BY_ROLE | FromDraftLineRejectedByRole | — |
| REJECTED_REASON | DraftLineRejectedReason | — |
| REJECTED_REASON | FromDraftLineRejectedReason | — |
| REQ_BU_ID | DraftLineReqBuId | — |
| REQ_BU_ID | FromDraftLineReqBuId | — |
| REQUEST_ID | DraftLineRequestId | — |
| REQUEST_ID | FromDraftLineRequestId | — |
| RETAINAGE_RATE | FromDraftLineRetainageRate | — |
| RETROACTIVE_DATE | DraftLineRetroactiveDate | — |
| RETROACTIVE_DATE | FromDraftLineRetroactiveDate | — |
| SECONDARY_QUANTITY | DraftLineSecondaryQuantity | — |
| SECONDARY_QUANTITY | FromDraftLineSecondaryQuantity | — |
| SECONDARY_UOM_CODE | DraftLineSecondaryUomCode | — |
| SECONDARY_UOM_CODE | FromDraftLineSecondaryUomCode | — |
| SHIPPING_UOM_CODE | DraftLineShippingUomCode | ✅ |
| SHIPPING_UOM_QUANTITY | DraftLineShippingUomQuantity | — |
| SOURCE_DOC_REV_NUM | DraftLineSourceDocRevNum | — |
| SOURCE_DOC_REV_NUM | FromDraftLineSourceDocRevNum | — |
| START_DATE | DraftLineStartDate | — |
| START_DATE | FromDraftLineStartDate | — |
| SUPPLIER_PART_AUXID | DraftLineSupplierPartAuxid | — |
| SUPPLIER_PART_AUXID | FromDraftLineSupplierPartAuxid | — |
| SUPPLIER_REF_NUMBER | DraftLineSupplierRefNumber | — |
| SUPPLIER_REF_NUMBER | FromDraftLineSupplierRefNumber | — |
| TAX_ATTRIBUTE_UPDATE_CODE | DraftLineTaxAttributeUpdateCode | — |
| TAX_ATTRIBUTE_UPDATE_CODE | FromDraftLineTaxAttributeUpdateCode | — |
| TAX_CODE_ID | DraftLineTaxCodeId | — |
| TAX_CODE_ID | FromDraftLineTaxCodeId | — |
| TAX_NAME | DraftLineTaxName | — |
| TAX_NAME | FromDraftLineTaxName | — |
| TAXABLE_FLAG | DraftLineTaxableFlag | — |
| TAXABLE_FLAG | FromDraftLineTaxableFlag | — |
| TYPE_1099 | DraftLineType1099 | — |
| TYPE_1099 | FromDraftLineType1099 | — |
| UN_NUMBER_ID | DraftLineUnNumberId | — |
| UN_NUMBER_ID | FromDraftLineUnNumberId | — |
| UNIT_PRICE | DraftLineUnitPrice | ✅ |
| UNIT_PRICE | FromDraftLineUnitPrice | — |
| UNORDERED_FLAG | DraftLineUnorderedFlag | — |
| UNORDERED_FLAG | FromDraftLineUnorderedFlag | — |
| UOM_CODE | DraftLineUomCode | ✅ |
| UOM_CODE | FromDraftLineUomCode | — |
| VENDOR_PRODUCT_NUM | DraftLineVendorProductNum | ✅ |
| VENDOR_PRODUCT_NUM | FromDraftLineVendorProductNum | — |

### [[draftpurchasingdocumentlinepvo|DraftPurchasingDocumentLinePVO]] (PO · BICC: 17/112)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGING_PERIOD_DAYS | DraftLineAgingPeriodDays | — |
| ALLOW_DESCRIPTION_UPDATE_FLAG | DraftLineAllowDescriptionUpdateFlag | — |
| ALLOW_PRICE_OVERRIDE_FLAG | DraftLineAllowPriceOverrideFlag | — |
| AMOUNT | DraftLineAmount | — |
| AUCTION_DISPLAY_NUMBER | DraftLineAuctionDisplayNumber | — |
| AUCTION_HEADER_ID | DraftLineAuctionHeaderId | — |
| AUCTION_LINE_NUMBER | DraftLineAuctionLineNumber | — |
| BASE_QTY | DraftLineBaseQty | — |
| BASE_UNIT_PRICE | DraftLineBaseUnitPrice | — |
| BASE_UOM | DraftLineBaseUom | — |
| BID_LINE_NUMBER | DraftLineBidLineNumber | — |
| BID_NUMBER | DraftLineBidNumber | — |
| CANCEL_DATE | DraftLineCancelDate | — |
| CANCEL_FLAG | DraftLineCancelFlag | — |
| CANCEL_REASON | DraftLineCancelReason | — |
| CANCELLED_BY | DraftLineCancelledBy | — |
| CAPITAL_EXPENSE_FLAG | DraftLineCapitalExpenseFlag | — |
| CATEGORY_ID | DraftLineCategoryId | — |
| CHANGE_ACCEPTED_FLAG | DraftLineChangeAcceptedFlag | — |
| CO_AMOUNT_CANCELLED | DraftLineCoAmountCancelled | — |
| CO_QUANTITY_CANCELLED | DraftLineCoQuantityCancelled | — |
| COMMITTED_AMOUNT | DraftLineCommittedAmount | — |
| CONSIGNMENT_LINE_FLAG | DraftLineConsignmentLineFlag | ✅ |
| CONTRACT_ID | DraftLineContractId | — |
| CONTRACTOR_FIRST_NAME | DraftLineContractorFirstName | — |
| CONTRACTOR_LAST_NAME | DraftLineContractorLastName | — |
| CREATED_BY | DraftLineCreatedBy | — |
| CREATION_DATE | DraftLineCreationDate | — |
| ENTITY_CHANGE_TYPE_CODE | DraftLineEntityChangeTypeCode | — |
| EXPIRATION_DATE | DraftLineExpirationDate | — |
| EXTERNAL_CHANGE_FLAG | DraftLineExternalChangeFlag | — |
| FIRM_DATE | DraftLineFirmDate | — |
| FIRM_STATUS_LOOKUP_CODE | DraftLineFirmStatusLookupCode | — |
| FROM_HEADER_ID | DraftLineFromHeaderId | — |
| FROM_LINE_ID | DraftLineFromLineId | — |
| FROM_LINE_LOCATION_ID | DraftLineFromLineLocationId | — |
| FUNDS_STATUS | DraftLineFundsStatus | ✅ |
| GOVERNMENT_CONTEXT | DraftLineGovernmentContext | — |
| HAZARD_CLASS_ID | DraftLineHazardClassId | — |
| ITEM_DESCRIPTION | DraftLineItemDescription | ✅ |
| ITEM_ID | DraftLineItemId | ✅ |
| ITEM_REVISION | DraftLineItemRevision | ✅ |
| JOB_DEFINITION_NAME | DraftLineJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | DraftLineJobDefinitionPackage | — |
| JOB_ID | DraftLineJobId | — |
| LAST_UPDATE_DATE | DraftLineLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DraftLineLastUpdateLogin | — |
| LAST_UPDATED_BY | DraftLineLastUpdatedBy | — |
| LINE_NUM | DraftLineLineNum | ✅ |
| LINE_REFERENCE_NUM | DraftLineLineReferenceNum | — |
| LINE_START_DATE | DraftLineLineStartDate | — |
| LINE_TYPE_ID | DraftLineLineTypeId | — |
| LIST_PRICE_PER_UNIT | DraftLineListPricePerUnit | — |
| MANUAL_PRICE_CHANGE_FLAG | DraftLineManualPriceChangeFlag | — |
| MARKET_PRICE | DraftLineMarketPrice | — |
| MATCHING_BASIS | DraftLineMatchingBasis | — |
| MAX_RETAINAGE_AMOUNT | DraftLineMaxRetainageAmount | — |
| MIN_RELEASE_AMOUNT | DraftLineMinReleaseAmount | ✅ |
| NEGOTIATED_BY_PREPARER_FLAG | DraftLineNegotiatedByPreparerFlag | ✅ |
| NOT_TO_EXCEED_PRICE | DraftLineNotToExceedPrice | — |
| NOTE_TO_VENDOR | DraftLineNoteToVendor | ✅ |
| OBJECT_VERSION_NUMBER | DraftLineObjectVersionNumber | — |
| OKE_CONTRACT_HEADER_ID | DraftLineOkeContractHeaderId | — |
| OKE_CONTRACT_VERSION_ID | DraftLineOkeContractVersionId | — |
| ORDER_TYPE_LOOKUP_CODE | DraftLineOrderTypeLookupCode | — |
| ORIGINAL_INTERFACE_LINE_ID | DraftLineOriginalInterfaceLineId | — |
| OVER_TOLERANCE_ERROR_FLAG | DraftLineOverToleranceErrorFlag | — |
| PJC_CONTEXT_CATEGORY | DraftLinePjcContextCategory | — |
| PO_HEADER_ID | DraftLinePoHeaderId | — |
| PO_LINE_ID | PoLineId | ✅ |
| PRC_BU_ID | DraftLinePrcBuId | — |
| PREFERRED_GRADE | DraftLinePreferredGrade | — |
| PRICE_BREAK_LOOKUP_CODE | DraftLinePriceBreakLookupCode | — |
| PRICE_TYPE_LOOKUP_CODE | DraftLinePriceTypeLookupCode | — |
| PROGRAM_APP_NAME | DraftLineProgramAppName | — |
| PROGRAM_NAME | DraftLineProgramName | — |
| PROGRESS_PAYMENT_RATE | DraftLineProgressPaymentRate | — |
| PURCHASE_BASIS | DraftLinePurchaseBasis | — |
| QC_GRADE | DraftLineQcGrade | — |
| QTY_RCV_TOLERANCE | DraftLineQtyRcvTolerance | — |
| QUANTITY | DraftLineQuantity | ✅ |
| QUANTITY_COMMITTED | DraftLineQuantityCommitted | — |
| REASON_FOR_CHANGE | DraftLineReasonForChange | ✅ |
| RECOUPMENT_RATE | DraftLineRecoupmentRate | — |
| REFERENCE_NUM | DraftLineReferenceNum | — |
| REJECTED_BY | DraftLineRejectedBy | — |
| REJECTED_BY_ROLE | DraftLineRejectedByRole | — |
| REJECTED_REASON | DraftLineRejectedReason | — |
| REQ_BU_ID | DraftLineReqBuId | — |
| REQUEST_ID | DraftLineRequestId | — |
| REQUEST_ID | PurchasingDocumentLineRequestId | — |
| REQUEST_ID | RequestId | — |
| RETAINAGE_RATE | DraftLineRetainageRate | — |
| RETROACTIVE_DATE | DraftLineRetroactiveDate | — |
| SECONDARY_QUANTITY | DraftLineSecondaryQuantity | — |
| SECONDARY_UOM_CODE | DraftLineSecondaryUomCode | — |
| SHIPPING_UOM_CODE | DraftLineShippingUomCode | ✅ |
| SHIPPING_UOM_QUANTITY | DraftLineShippingUomQuantity | — |
| SOURCE_DOC_REV_NUM | DraftLineSourceDocRevNum | — |
| START_DATE | DraftLineStartDate | — |
| SUPPLIER_PART_AUXID | DraftLineSupplierPartAuxid | — |
| SUPPLIER_REF_NUMBER | DraftLineSupplierRefNumber | — |
| TAX_ATTRIBUTE_UPDATE_CODE | DraftLineTaxAttributeUpdateCode | — |
| TAX_CODE_ID | DraftLineTaxCodeId | — |
| TAX_NAME | DraftLineTaxName | — |
| TAXABLE_FLAG | DraftLineTaxableFlag | — |
| TYPE_1099 | DraftLineType1099 | — |
| UN_NUMBER_ID | DraftLineUnNumberId | — |
| UNIT_PRICE | DraftLineUnitPrice | ✅ |
| UNORDERED_FLAG | DraftLineUnorderedFlag | — |
| UOM_CODE | DraftLineUomCode | ✅ |
| VENDOR_PRODUCT_NUM | DraftLineVendorProductNum | ✅ |

---

## 📚 Referências

- [Oracle Docs — PO_LINES_DRAFT_ALL](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
