---
id: DOC-PO-141
doc_type: system-doc
title: "PO_SYSTEM_PARAMETERS_ALL — Parametros de Sistema do Modulo PO"
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
  - parametros
  - configuracao
  - setup
aliases:
  - PO_SYSTEM_PARAMETERS_ALL
  - po_system_parameters_all
  - po-system-parameters-all
  - po-system
  - parametros-de-sistema-do-modulo-po
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_SYSTEM_PARAMETERS_ALL

## 📌 Visão Geral

Armazena os **parametros de configuracao do modulo Procurement** por business unit: numeracao, matching, accrual, aprovacao automatica.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` e necessario para consultas por organizacao especifica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Configuracao:** Parametros que controlam o comportamento.
- **Defaults:** Valores padrao para POs.
- **Matching rules:** Regras padrao por BU.
- **Aprovacao:** Controle de aprovacao automatica.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ORG_ID | NUMBER(18) | NOT NULL | PK | Business unit | [[hr_all_organization_units_f]] | 🟢 100% |
| 2 | RECEIVE_CLOSE_TOLERANCE | NUMBER | NULL | Configuracao | Tolerancia de fechamento por recebimento (%) | — | 🟢 90% |
| 3 | INVOICE_CLOSE_TOLERANCE | NUMBER | NULL | Configuracao | Tolerancia de fechamento por faturamento (%) | — | 🟢 90% |
| 4 | ACCRUE_ON_RECEIPT_FLAG | VARCHAR2(1) | NULL | Flag | Accrual no recebimento (Y/N) | — | 🟢 90% |
| 5 | DEFAULT_RATE_TYPE | VARCHAR2(30) | NULL | Financeiro | Tipo de taxa padrao | — | 🟡 80% |
| 6 | ENFORCE_BUYER_NAME_FLAG | VARCHAR2(1) | NULL | Flag | Obriga comprador | — | 🟡 75% |
| 7 | APPROVAL_REQUIRED_FLAG | VARCHAR2(1) | NULL | Flag | Aprovacao obrigatoria | — | 🟡 80% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit dos parâmetros de sistema de compras)

### Tabelas-filha (FK de saída)
- Nenhuma FK de saida identificada

---

## 📎 Uso Típico

### Parametros de uma BU
```sql
SELECT ORG_ID, RECEIVE_CLOSE_TOLERANCE, INVOICE_CLOSE_TOLERANCE,
       ACCRUE_ON_RECEIPT_FLAG
FROM   PO_SYSTEM_PARAMETERS_ALL
WHERE  ORG_ID = :p_org_id;
```

---

## 🔒 Observações

- Uma linha por business unit.
- Alteracoes impactam todo o modulo na BU.
- Tolerancias controlam fechamento automatico de PO.
- Flag `ACCRUE_ON_RECEIPT_FLAG` define accrual no recebimento ou pagamento.

---

## 🔗 PVOs Relacionados

### [[agreementheaderpvo|AgreementHeaderPVO]] (PO · BICC: 1/71)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_ITEM_DESC_UPDATE_FLAG | POSystemParametersAllowItemDescUpdateFlag | — |
| ALLOW_RETRO_PRICING | POSystemParametersAllowRetroPricing | — |
| BEST_PRICE_VISIBLE_BLIND | POSystemParametersBestPriceVisibleBlind | — |
| CARRIER_ID | POSystemParametersCarrierId | — |
| CAT_ADMIN_AUTHORING_ACCEPTANCE | POSystemParametersCatAdminAuthoringAcceptance | — |
| COLLAB_SECURITY_PROFILE_ID | POSystemParametersCollabSecurityProfileId | — |
| CREATE_DEBIT_MEMO_FLAG | POSystemParametersCreateDebitMemoFlag | — |
| CREATED_BY | POSystemParametersCreatedBy | — |
| CREATION_DATE | POSystemParametersCreationDate | — |
| CURRENCY_CODE | POSystemParametersCurrencyCode | — |
| DEFAULT_PROMISE_DATE | POSystemParametersDefaultPromiseDate | — |
| DEFAULT_RATE_TYPE | POSystemParametersDefaultRateType | — |
| DOCTYPE_ID | POSystemParametersDoctypeId | — |
| EMAIL_ATTACHMENT_FILENAME | POSystemParametersEmailAttachmentFilename | — |
| ENFORCE_BUYER_AUTHORITY_FLAG | POSystemParametersEnforceBuyerAuthorityFlag | — |
| ENFORCE_MIN_BID_PRICE | POSystemParametersEnforceMinBidPrice | — |
| ENFORCE_VENDOR_HOLD_FLAG | POSystemParametersEnforceVendorHoldFlag | — |
| FOB_LOOKUP_CODE | POSystemParametersFobLookupCode | — |
| FREIGHT_TERMS_LOOKUP_CODE | POSystemParametersFreightTermsLookupCode | — |
| GROUP_REQUISITION_LINES | POSystemParametersGroupRequisitionLines | — |
| GROUP_REQUISITIONS | POSystemParametersGroupRequisitions | — |
| HDR_ATTR_DEFAULT_MAX_SCORE | POSystemParametersHdrAttrDefaultMaxScore | — |
| HDR_ATTR_DISP_SCORE_CRITERIA | POSystemParametersHdrAttrDispScoreCriteria | — |
| HDR_ATTR_ENABLE_WEIGHTS | POSystemParametersHdrAttrEnableWeights | — |
| INSPECTION_REQUIRED_FLAG | POSystemParametersInspectionRequiredFlag | — |
| INVENTORY_ORGANIZATION_ID | POSystemParametersInventoryOrganizationId | — |
| INVOICE_CLOSE_CODE | POSystemParametersInvoiceCloseCode | — |
| INVOICE_CLOSE_TOLERANCE | POSystemParametersInvoiceCloseTolerance | — |
| LANGUAGE_CODE | POSystemParametersLanguageCode | — |
| LAST_UPDATE_DATE | POSystemParametersLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | POSystemParametersLastUpdateLogin | — |
| LAST_UPDATED_BY | POSystemParametersLastUpdatedBy | — |
| LINE_TYPE_ID | POSystemParametersLineTypeId | — |
| MANUAL_RECEIPT_NUM_TYPE | POSystemParametersManualReceiptNumType | — |
| MANUAL_REQ_NUM_TYPE | POSystemParametersManualReqNumType | — |
| MATCH_OPTION | POSystemParametersMatchOption | — |
| MAX_ATTACHMENT_SIZE | POSystemParametersMaxAttachmentSize | — |
| MIN_RELEASE_AMOUNT | POSystemParametersMinReleaseAmount | — |
| MODE_OF_TRANSPORT | POSystemParametersModeOfTransport | — |
| NEXT_APPROVER_LOOKUP_CODE | POSystemParametersNextApproverLookupCode | — |
| NEXT_NEGOTIATION_NUMBER | POSystemParametersNextNegotiationNumber | — |
| OBJECT_VERSION_NUMBER | POSystemParametersObjectVersionNumber | — |
| PRC_BU_ID | POSystemParametersPrcBuId | — |
| PRICE_BREAK_LOOKUP_CODE | POSystemParametersPriceBreakLookupCode | — |
| PRICE_CHANGE_AMOUNT | POSystemParametersPriceChangeAmount | — |
| RANK_INDICATOR | POSystemParametersRankIndicator | — |
| RANK_VISIBLE_BLIND | POSystemParametersRankVisibleBlind | — |
| RECEIVE_CLOSE_CODE | POSystemParametersReceiveCloseCode | — |
| RECEIVE_CLOSE_TOLERANCE | POSystemParametersReceiveCloseTolerance | — |
| RECEIVING_FLAG | POSystemParametersReceivingFlag | — |
| RFQ_ONLY_SITE_FLAG | POSystemParametersRfqOnlySiteFlag | — |
| SERVICE_LEVEL | POSystemParametersServiceLevel | — |
| STYLE_ID | POSystemParametersStyleId | — |
| SUPPLIER_AUTHORING_ACCEPTANCE | POSystemParametersSupplierAuthoringAcceptance | — |
| SUPPLIER_HISTORY_DURATION | POSystemParametersSupplierHistoryDuration | — |
| TAX_FROM_ITEM_FLAG | POSystemParametersTaxFromItemFlag | — |
| TAX_FROM_SHIP_TO_LOC_FLAG | POSystemParametersTaxFromShipToLocFlag | — |
| TAX_FROM_SYSTEM_FLAG | POSystemParametersTaxFromSystemFlag | — |
| TAX_FROM_VENDOR_FLAG | POSystemParametersTaxFromVendorFlag | — |
| TAX_FROM_VENDOR_SITE_FLAG | POSystemParametersTaxFromVendorSiteFlag | — |
| TAX_HIER_ITEM | POSystemParametersTaxHierItem | — |
| TAX_HIER_SHIP_TO_LOC | POSystemParametersTaxHierShipToLoc | — |
| TAX_HIER_SYSTEM | POSystemParametersTaxHierSystem | — |
| TAX_HIER_VENDOR | POSystemParametersTaxHierVendor | — |
| TAX_HIER_VENDOR_SITE | POSystemParametersTaxHierVendorSite | — |
| TAXABLE_FLAG | POSystemParametersTaxableFlag | — |
| TERMS_ID | POSystemParametersTermsId | — |
| USE_NEED_BY_DATE | POSystemParametersUseNeedByDate | — |
| USE_SHIP_TO | POSystemParametersUseShipTo | — |
| USER_DEFINED_RECEIPT_NUM_CODE | POSystemParametersUserDefinedReceiptNumCode | — |
| USER_DEFINED_REQ_NUM_CODE | POSystemParametersUserDefinedReqNumCode | — |

### [[agreementlinepvo|AgreementLinePVO]] (PO · BICC: 1/71)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_ITEM_DESC_UPDATE_FLAG | POSystemParametersAllowItemDescUpdateFlag | — |
| ALLOW_RETRO_PRICING | POSystemParametersAllowRetroPricing | — |
| BEST_PRICE_VISIBLE_BLIND | POSystemParametersBestPriceVisibleBlind | — |
| CARRIER_ID | POSystemParametersCarrierId | — |
| CAT_ADMIN_AUTHORING_ACCEPTANCE | POSystemParametersCatAdminAuthoringAcceptance | — |
| COLLAB_SECURITY_PROFILE_ID | POSystemParametersCollabSecurityProfileId | — |
| CREATE_DEBIT_MEMO_FLAG | POSystemParametersCreateDebitMemoFlag | — |
| CREATED_BY | POSystemParametersCreatedBy | — |
| CREATION_DATE | POSystemParametersCreationDate | — |
| CURRENCY_CODE | POSystemParametersCurrencyCode | — |
| DEFAULT_PROMISE_DATE | POSystemParametersDefaultPromiseDate | — |
| DEFAULT_RATE_TYPE | POSystemParametersDefaultRateType | — |
| DOCTYPE_ID | POSystemParametersDoctypeId | — |
| EMAIL_ATTACHMENT_FILENAME | POSystemParametersEmailAttachmentFilename | — |
| ENFORCE_BUYER_AUTHORITY_FLAG | POSystemParametersEnforceBuyerAuthorityFlag | — |
| ENFORCE_MIN_BID_PRICE | POSystemParametersEnforceMinBidPrice | — |
| ENFORCE_VENDOR_HOLD_FLAG | POSystemParametersEnforceVendorHoldFlag | — |
| FOB_LOOKUP_CODE | POSystemParametersFobLookupCode | — |
| FREIGHT_TERMS_LOOKUP_CODE | POSystemParametersFreightTermsLookupCode | — |
| GROUP_REQUISITION_LINES | POSystemParametersGroupRequisitionLines | — |
| GROUP_REQUISITIONS | POSystemParametersGroupRequisitions | — |
| HDR_ATTR_DEFAULT_MAX_SCORE | POSystemParametersHdrAttrDefaultMaxScore | — |
| HDR_ATTR_DISP_SCORE_CRITERIA | POSystemParametersHdrAttrDispScoreCriteria | — |
| HDR_ATTR_ENABLE_WEIGHTS | POSystemParametersHdrAttrEnableWeights | — |
| INSPECTION_REQUIRED_FLAG | POSystemParametersInspectionRequiredFlag | — |
| INVENTORY_ORGANIZATION_ID | POSystemParametersInventoryOrganizationId | — |
| INVOICE_CLOSE_CODE | POSystemParametersInvoiceCloseCode | — |
| INVOICE_CLOSE_TOLERANCE | POSystemParametersInvoiceCloseTolerance | — |
| LANGUAGE_CODE | POSystemParametersLanguageCode | — |
| LAST_UPDATE_DATE | POSystemParametersLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | POSystemParametersLastUpdateLogin | — |
| LAST_UPDATED_BY | POSystemParametersLastUpdatedBy | — |
| LINE_TYPE_ID | POSystemParametersLineTypeId | — |
| MANUAL_RECEIPT_NUM_TYPE | POSystemParametersManualReceiptNumType | — |
| MANUAL_REQ_NUM_TYPE | POSystemParametersManualReqNumType | — |
| MATCH_OPTION | POSystemParametersMatchOption | — |
| MAX_ATTACHMENT_SIZE | POSystemParametersMaxAttachmentSize | — |
| MIN_RELEASE_AMOUNT | POSystemParametersMinReleaseAmount | — |
| MODE_OF_TRANSPORT | POSystemParametersModeOfTransport | — |
| NEXT_APPROVER_LOOKUP_CODE | POSystemParametersNextApproverLookupCode | — |
| NEXT_NEGOTIATION_NUMBER | POSystemParametersNextNegotiationNumber | — |
| OBJECT_VERSION_NUMBER | POSystemParametersObjectVersionNumber | — |
| PRC_BU_ID | POSystemParametersPrcBuId | — |
| PRICE_BREAK_LOOKUP_CODE | POSystemParametersPriceBreakLookupCode | — |
| PRICE_CHANGE_AMOUNT | POSystemParametersPriceChangeAmount | — |
| RANK_INDICATOR | POSystemParametersRankIndicator | — |
| RANK_VISIBLE_BLIND | POSystemParametersRankVisibleBlind | — |
| RECEIVE_CLOSE_CODE | POSystemParametersReceiveCloseCode | — |
| RECEIVE_CLOSE_TOLERANCE | POSystemParametersReceiveCloseTolerance | — |
| RECEIVING_FLAG | POSystemParametersReceivingFlag | — |
| RFQ_ONLY_SITE_FLAG | POSystemParametersRfqOnlySiteFlag | — |
| SERVICE_LEVEL | POSystemParametersServiceLevel | — |
| STYLE_ID | POSystemParametersStyleId | — |
| SUPPLIER_AUTHORING_ACCEPTANCE | POSystemParametersSupplierAuthoringAcceptance | — |
| SUPPLIER_HISTORY_DURATION | POSystemParametersSupplierHistoryDuration | — |
| TAX_FROM_ITEM_FLAG | POSystemParametersTaxFromItemFlag | — |
| TAX_FROM_SHIP_TO_LOC_FLAG | POSystemParametersTaxFromShipToLocFlag | — |
| TAX_FROM_SYSTEM_FLAG | POSystemParametersTaxFromSystemFlag | — |
| TAX_FROM_VENDOR_FLAG | POSystemParametersTaxFromVendorFlag | — |
| TAX_FROM_VENDOR_SITE_FLAG | POSystemParametersTaxFromVendorSiteFlag | — |
| TAX_HIER_ITEM | POSystemParametersTaxHierItem | — |
| TAX_HIER_SHIP_TO_LOC | POSystemParametersTaxHierShipToLoc | — |
| TAX_HIER_SYSTEM | POSystemParametersTaxHierSystem | — |
| TAX_HIER_VENDOR | POSystemParametersTaxHierVendor | — |
| TAX_HIER_VENDOR_SITE | POSystemParametersTaxHierVendorSite | — |
| TAXABLE_FLAG | POSystemParametersTaxableFlag | — |
| TERMS_ID | POSystemParametersTermsId | — |
| USE_NEED_BY_DATE | POSystemParametersUseNeedByDate | — |
| USE_SHIP_TO | POSystemParametersUseShipTo | — |
| USER_DEFINED_RECEIPT_NUM_CODE | POSystemParametersUserDefinedReceiptNumCode | — |
| USER_DEFINED_REQ_NUM_CODE | POSystemParametersUserDefinedReqNumCode | — |

### [[agreementpricebreakpvo|AgreementPriceBreakPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_ITEM_DESC_UPDATE_FLAG | POSystemParametersAllowItemDescUpdateFlag | — |
| ALLOW_RETRO_PRICING | POSystemParametersAllowRetroPricing | — |
| BEST_PRICE_VISIBLE_BLIND | POSystemParametersBestPriceVisibleBlind | — |
| CARRIER_ID | POSystemParametersCarrierId | — |
| CAT_ADMIN_AUTHORING_ACCEPTANCE | POSystemParametersCatAdminAuthoringAcceptance | — |
| COLLAB_SECURITY_PROFILE_ID | POSystemParametersCollabSecurityProfileId | — |
| CREATE_DEBIT_MEMO_FLAG | POSystemParametersCreateDebitMemoFlag | — |
| CURRENCY_CODE | POSystemParametersCurrencyCode | — |
| DEFAULT_PROMISE_DATE | POSystemParametersDefaultPromiseDate | — |
| DEFAULT_RATE_TYPE | POSystemParametersDefaultRateType | — |
| DOCTYPE_ID | POSystemParametersDoctypeId | — |
| EMAIL_ATTACHMENT_FILENAME | POSystemParametersEmailAttachmentFilename | — |
| ENFORCE_BUYER_AUTHORITY_FLAG | POSystemParametersEnforceBuyerAuthorityFlag | — |
| ENFORCE_MIN_BID_PRICE | POSystemParametersEnforceMinBidPrice | — |
| ENFORCE_VENDOR_HOLD_FLAG | POSystemParametersEnforceVendorHoldFlag | — |
| FOB_LOOKUP_CODE | POSystemParametersFobLookupCode | — |
| FREIGHT_TERMS_LOOKUP_CODE | POSystemParametersFreightTermsLookupCode | — |
| GROUP_REQUISITION_LINES | POSystemParametersGroupRequisitionLines | — |
| GROUP_REQUISITIONS | POSystemParametersGroupRequisitions | — |
| HDR_ATTR_DEFAULT_MAX_SCORE | POSystemParametersHdrAttrDefaultMaxScore | — |
| HDR_ATTR_DISP_SCORE_CRITERIA | POSystemParametersHdrAttrDispScoreCriteria | — |
| HDR_ATTR_ENABLE_WEIGHTS | POSystemParametersHdrAttrEnableWeights | — |
| INSPECTION_REQUIRED_FLAG | POSystemParametersInspectionRequiredFlag | — |
| INVENTORY_ORGANIZATION_ID | POSystemParametersInventoryOrganizationId | — |
| INVOICE_CLOSE_CODE | POSystemParametersInvoiceCloseCode | — |
| INVOICE_CLOSE_TOLERANCE | POSystemParametersInvoiceCloseTolerance | — |
| LANGUAGE_CODE | POSystemParametersLanguageCode | — |
| LINE_TYPE_ID | POSystemParametersLineTypeId | — |
| MANUAL_RECEIPT_NUM_TYPE | POSystemParametersManualReceiptNumType | — |
| MANUAL_REQ_NUM_TYPE | POSystemParametersManualReqNumType | — |
| MATCH_OPTION | POSystemParametersMatchOption | — |
| MAX_ATTACHMENT_SIZE | POSystemParametersMaxAttachmentSize | — |
| MIN_RELEASE_AMOUNT | POSystemParametersMinReleaseAmount | — |
| MODE_OF_TRANSPORT | POSystemParametersModeOfTransport | — |
| NEXT_APPROVER_LOOKUP_CODE | POSystemParametersNextApproverLookupCode | — |
| NEXT_NEGOTIATION_NUMBER | POSystemParametersNextNegotiationNumber | — |
| PRC_BU_ID | POSystemParametersPrcBuId | — |
| PRICE_BREAK_LOOKUP_CODE | POSystemParametersPriceBreakLookupCode | — |
| PRICE_CHANGE_AMOUNT | POSystemParametersPriceChangeAmount | — |
| RANK_INDICATOR | POSystemParametersRankIndicator | — |
| RANK_VISIBLE_BLIND | POSystemParametersRankVisibleBlind | — |
| RECEIVE_CLOSE_CODE | POSystemParametersReceiveCloseCode | — |
| RECEIVE_CLOSE_TOLERANCE | POSystemParametersReceiveCloseTolerance | — |
| RECEIVING_FLAG | POSystemParametersReceivingFlag | — |
| RFQ_ONLY_SITE_FLAG | POSystemParametersRfqOnlySiteFlag | — |
| SERVICE_LEVEL | POSystemParametersServiceLevel | — |
| STYLE_ID | POSystemParametersStyleId | — |
| SUPPLIER_AUTHORING_ACCEPTANCE | POSystemParametersSupplierAuthoringAcceptance | — |
| SUPPLIER_HISTORY_DURATION | POSystemParametersSupplierHistoryDuration | — |
| TAX_FROM_ITEM_FLAG | POSystemParametersTaxFromItemFlag | — |
| TAX_FROM_SHIP_TO_LOC_FLAG | POSystemParametersTaxFromShipToLocFlag | — |
| TAX_FROM_SYSTEM_FLAG | POSystemParametersTaxFromSystemFlag | — |
| TAX_FROM_VENDOR_FLAG | POSystemParametersTaxFromVendorFlag | — |
| TAX_FROM_VENDOR_SITE_FLAG | POSystemParametersTaxFromVendorSiteFlag | — |
| TAX_HIER_ITEM | POSystemParametersTaxHierItem | — |
| TAX_HIER_SHIP_TO_LOC | POSystemParametersTaxHierShipToLoc | — |
| TAX_HIER_SYSTEM | POSystemParametersTaxHierSystem | — |
| TAX_HIER_VENDOR | POSystemParametersTaxHierVendor | — |
| TAX_HIER_VENDOR_SITE | POSystemParametersTaxHierVendorSite | — |
| TAXABLE_FLAG | POSystemParametersTaxableFlag | — |
| TERMS_ID | POSystemParametersTermsId | — |
| USE_NEED_BY_DATE | POSystemParametersUseNeedByDate | — |
| USE_SHIP_TO | POSystemParametersUseShipTo | — |
| USER_DEFINED_RECEIPT_NUM_CODE | POSystemParametersUserDefinedReceiptNumCode | — |
| USER_DEFINED_REQ_NUM_CODE | POSystemParametersUserDefinedReqNumCode | — |

### [[awardednegotiationresponselinepvo|AwardedNegotiationResponseLinePVO]] (PO · BICC: 1/106)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGING_ONSET_POINT | AgingOnsetPoint | — |
| AGING_PERIOD_DAYS | AgingPeriodDays | — |
| ALLOW_ITEM_DESC_UPDATE_FLAG | AllowItemDescUpdateFlag | — |
| ALLOW_MANUL_PRICE_UPDATE_ORDER | AllowManulPriceUpdateOrder | — |
| ALLOW_RETRO_PRICING | AllowRetroPricing | — |
| AWARD_APPROVAL_ENABLED_FLAG | AwardApprovalEnabledFlag | — |
| BEST_PRICE_VISIBLE_BLIND | BestPriceVisibleBlind | — |
| BUYER_MANAGED_TRANSPORT_FLAG | BuyerManagedTransportFlag | — |
| CARRIER_ID | CarrierId | — |
| CAT_ADMIN_AUTHORING_ACCEPTANCE | CatAdminAuthoringAcceptance | — |
| COLLAB_SECURITY_PROFILE_ID | CollabSecurityProfileId | — |
| CONSUMPTION_ADVICE_FREQUENCY | ConsumptionAdviceFrequency | — |
| CONSUMPTION_ADVICE_SUMMARY | ConsumptionAdviceSummary | — |
| CREATE_DEBIT_MEMO_FLAG | CreateDebitMemoFlag | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| CURRENCY_CODE | CurrencyCode | — |
| DEFAULT_BUYER_ID | DefaultBuyerId | — |
| DEFAULT_PROMISE_DATE | DefaultPromiseDate | — |
| DEFAULT_RATE_TYPE | DefaultRateType | — |
| DOCTYPE_ID | DoctypeId | — |
| EMAIL_ATTACHMENT_FILENAME | EmailAttachmentFilename | — |
| ENFORCE_BUYER_AUTHORITY_FLAG | EnforceBuyerAuthorityFlag | — |
| ENFORCE_MIN_BID_PRICE | EnforceMinBidPrice | — |
| ENFORCE_VENDOR_HOLD_FLAG | EnforceVendorHoldFlag | — |
| FOB_LOOKUP_CODE | FobLookupCode | — |
| FREIGHT_TERMS_LOOKUP_CODE | FreightTermsLookupCode | — |
| GEN_ORDER_FOR_NEG_REQS_FLAG | GenOrderForNegReqsFlag | — |
| GLOBAL_ATTRIBUTE1 | GlobalAttribute1 | — |
| GLOBAL_ATTRIBUTE10 | GlobalAttribute10 | — |
| GLOBAL_ATTRIBUTE11 | GlobalAttribute11 | — |
| GLOBAL_ATTRIBUTE12 | GlobalAttribute12 | — |
| GLOBAL_ATTRIBUTE13 | GlobalAttribute13 | — |
| GLOBAL_ATTRIBUTE14 | GlobalAttribute14 | — |
| GLOBAL_ATTRIBUTE15 | GlobalAttribute15 | — |
| GLOBAL_ATTRIBUTE16 | GlobalAttribute16 | — |
| GLOBAL_ATTRIBUTE17 | GlobalAttribute17 | — |
| GLOBAL_ATTRIBUTE18 | GlobalAttribute18 | — |
| GLOBAL_ATTRIBUTE19 | GlobalAttribute19 | — |
| GLOBAL_ATTRIBUTE2 | GlobalAttribute2 | — |
| GLOBAL_ATTRIBUTE20 | GlobalAttribute20 | — |
| GLOBAL_ATTRIBUTE3 | GlobalAttribute3 | — |
| GLOBAL_ATTRIBUTE4 | GlobalAttribute4 | — |
| GLOBAL_ATTRIBUTE5 | GlobalAttribute5 | — |
| GLOBAL_ATTRIBUTE6 | GlobalAttribute6 | — |
| GLOBAL_ATTRIBUTE7 | GlobalAttribute7 | — |
| GLOBAL_ATTRIBUTE8 | GlobalAttribute8 | — |
| GLOBAL_ATTRIBUTE9 | GlobalAttribute9 | — |
| GLOBAL_ATTRIBUTE_CATEGORY | GlobalAttributeCategory | — |
| GROUP_REQUISITION_LINES | GroupRequisitionLines | — |
| GROUP_REQUISITIONS | GroupRequisitions | — |
| HDR_ATTR_DEFAULT_MAX_SCORE | HdrAttrDefaultMaxScore | — |
| HDR_ATTR_DISP_SCORE_CRITERIA | HdrAttrDispScoreCriteria | — |
| HDR_ATTR_ENABLE_WEIGHTS | HdrAttrEnableWeights | — |
| INSPECTION_REQUIRED_FLAG | InspectionRequiredFlag | — |
| INVENTORY_ORGANIZATION_ID | InventoryOrganizationId | — |
| INVENTORY_ORGANIZATION_ID | InventoryOrganizationId1 | — |
| INVOICE_CLOSE_CODE | InvoiceCloseCode | — |
| INVOICE_CLOSE_TOLERANCE | InvoiceCloseTolerance | — |
| LANGUAGE_CODE | LanguageCode | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| LINE_TYPE_ID | LineTypeId | — |
| MANUAL_RECEIPT_NUM_TYPE | ManualReceiptNumType | — |
| MANUAL_REQ_NUM_TYPE | ManualReqNumType | — |
| MATCH_OPTION | MatchOption | — |
| MAX_ATTACHMENT_SIZE | MaxAttachmentSize | — |
| MIN_RELEASE_AMOUNT | MinReleaseAmount | — |
| MODE_OF_TRANSPORT | ModeOfTransport1 | — |
| NEG_APPROVAL_ENABLED_FLAG | NegApprovalEnabledFlag | — |
| NEXT_APPROVER_LOOKUP_CODE | NextApproverLookupCode | — |
| NEXT_NEGOTIATION_NUMBER | NextNegotiationNumber | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PRC_BU_ID | PrcBuId | — |
| PRC_BU_ID | PrcBuId1 | — |
| PRICE_BREAK_LOOKUP_CODE | PriceBreakLookupCode | — |
| PRICE_CHANGE_AMOUNT | PriceChangeAmount | — |
| RANK_INDICATOR | RankIndicator | — |
| RANK_VISIBLE_BLIND | RankVisibleBlind | — |
| RECEIVE_CLOSE_CODE | ReceiveCloseCode | — |
| RECEIVE_CLOSE_TOLERANCE | ReceiveCloseTolerance | — |
| RECEIVING_FLAG | ReceivingFlag | — |
| RFQ_ONLY_SITE_FLAG | RfqOnlySiteFlag | — |
| SERVICE_LEVEL | ServiceLevel1 | — |
| STYLE_ID | StyleId | — |
| SUPPLIER_AUTHORING_ACCEPTANCE | SupplierAuthoringAcceptance | — |
| SUPPLIER_HISTORY_DURATION | SupplierHistoryDuration | — |
| SYSTEM_CONFIGURED_FLAG | SystemConfiguredFlag | — |
| TAX_FROM_ITEM_FLAG | TaxFromItemFlag | — |
| TAX_FROM_SHIP_TO_LOC_FLAG | TaxFromShipToLocFlag | — |
| TAX_FROM_SYSTEM_FLAG | TaxFromSystemFlag | — |
| TAX_FROM_VENDOR_FLAG | TaxFromVendorFlag | — |
| TAX_FROM_VENDOR_SITE_FLAG | TaxFromVendorSiteFlag | — |
| TAX_HIER_ITEM | TaxHierItem | — |
| TAX_HIER_SHIP_TO_LOC | TaxHierShipToLoc | — |
| TAX_HIER_SYSTEM | TaxHierSystem | — |
| TAX_HIER_VENDOR | TaxHierVendor | — |
| TAX_HIER_VENDOR_SITE | TaxHierVendorSite | — |
| TAXABLE_FLAG | TaxableFlag | — |
| TERMS_ID | TermsId | — |
| USE_NEED_BY_DATE | UseNeedByDate | — |
| USE_SALES_ORDER_NUMBER_FLAG | UseSalesOrderNumberFlag | — |
| USE_SHIP_TO | UseShipTo | — |
| USER_DEFINED_RECEIPT_NUM_CODE | UserDefinedReceiptNumCode | — |
| USER_DEFINED_REQ_NUM_CODE | UserDefinedReqNumCode | — |

### [[draftpurchaseorderdistributionpvo|DraftPurchaseOrderDistributionPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| INVENTORY_ORGANIZATION_ID | POSystemParametersInventoryOrganizationId | — |
| PRC_BU_ID | POSystemParametersPrcBuId | — |

### [[draftpurchaseorderdistributionrefpvo|DraftPurchaseOrderDistributionRefPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| INVENTORY_ORGANIZATION_ID | POSystemParametersInventoryOrganizationId | — |
| PRC_BU_ID | POSystemParametersPrcBuId | — |

### [[draftpurchasingdocumentlinelocationpvo|DraftPurchasingDocumentLineLocationPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| INVENTORY_ORGANIZATION_ID | POSystemParametersInventoryOrganizationId | — |
| PRC_BU_ID | POSystemParametersPrcBuId | — |

### [[draftpurchasingdocumentlinepvo|DraftPurchasingDocumentLinePVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| INVENTORY_ORGANIZATION_ID | POSystemParametersInventoryOrganizationId | — |
| PRC_BU_ID | POSystemParametersPrcBuId | — |

### [[invoicelinepvo|InvoiceLinePVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| INVENTORY_ORGANIZATION_ID | PurchasingSystemParameterInventoryOrgId | — |
| PRC_BU_ID | PurchasingSystemParameterPrcBuId | — |

### [[negdocumentnegotiationlinepvo|NegDocumentNegotiationLinePVO]] (PO · BICC: 1/106)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGING_ONSET_POINT | AgingOnsetPoint | — |
| AGING_PERIOD_DAYS | AgingPeriodDays | — |
| ALLOW_ITEM_DESC_UPDATE_FLAG | AllowItemDescUpdateFlag | — |
| ALLOW_MANUL_PRICE_UPDATE_ORDER | AllowManulPriceUpdateOrder | — |
| ALLOW_RETRO_PRICING | AllowRetroPricing | — |
| AWARD_APPROVAL_ENABLED_FLAG | AwardApprovalEnabledFlag | — |
| BEST_PRICE_VISIBLE_BLIND | BestPriceVisibleBlind | — |
| BUYER_MANAGED_TRANSPORT_FLAG | BuyerManagedTransportFlag | — |
| CARRIER_ID | CarrierId | — |
| CAT_ADMIN_AUTHORING_ACCEPTANCE | CatAdminAuthoringAcceptance | — |
| COLLAB_SECURITY_PROFILE_ID | CollabSecurityProfileId | — |
| CONSUMPTION_ADVICE_FREQUENCY | ConsumptionAdviceFrequency | — |
| CONSUMPTION_ADVICE_SUMMARY | ConsumptionAdviceSummary | — |
| CREATE_DEBIT_MEMO_FLAG | CreateDebitMemoFlag | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| CURRENCY_CODE | CurrencyCode | — |
| DEFAULT_BUYER_ID | DefaultBuyerId | — |
| DEFAULT_PROMISE_DATE | DefaultPromiseDate | — |
| DEFAULT_RATE_TYPE | DefaultRateType | — |
| DOCTYPE_ID | DoctypeId | — |
| EMAIL_ATTACHMENT_FILENAME | EmailAttachmentFilename | — |
| ENFORCE_BUYER_AUTHORITY_FLAG | EnforceBuyerAuthorityFlag | — |
| ENFORCE_MIN_BID_PRICE | EnforceMinBidPrice | — |
| ENFORCE_VENDOR_HOLD_FLAG | EnforceVendorHoldFlag | — |
| FOB_LOOKUP_CODE | FobLookupCode | — |
| FREIGHT_TERMS_LOOKUP_CODE | FreightTermsLookupCode | — |
| GEN_ORDER_FOR_NEG_REQS_FLAG | GenOrderForNegReqsFlag | — |
| GLOBAL_ATTRIBUTE1 | GlobalAttribute1 | — |
| GLOBAL_ATTRIBUTE10 | GlobalAttribute10 | — |
| GLOBAL_ATTRIBUTE11 | GlobalAttribute11 | — |
| GLOBAL_ATTRIBUTE12 | GlobalAttribute12 | — |
| GLOBAL_ATTRIBUTE13 | GlobalAttribute13 | — |
| GLOBAL_ATTRIBUTE14 | GlobalAttribute14 | — |
| GLOBAL_ATTRIBUTE15 | GlobalAttribute15 | — |
| GLOBAL_ATTRIBUTE16 | GlobalAttribute16 | — |
| GLOBAL_ATTRIBUTE17 | GlobalAttribute17 | — |
| GLOBAL_ATTRIBUTE18 | GlobalAttribute18 | — |
| GLOBAL_ATTRIBUTE19 | GlobalAttribute19 | — |
| GLOBAL_ATTRIBUTE2 | GlobalAttribute2 | — |
| GLOBAL_ATTRIBUTE20 | GlobalAttribute20 | — |
| GLOBAL_ATTRIBUTE3 | GlobalAttribute3 | — |
| GLOBAL_ATTRIBUTE4 | GlobalAttribute4 | — |
| GLOBAL_ATTRIBUTE5 | GlobalAttribute5 | — |
| GLOBAL_ATTRIBUTE6 | GlobalAttribute6 | — |
| GLOBAL_ATTRIBUTE7 | GlobalAttribute7 | — |
| GLOBAL_ATTRIBUTE8 | GlobalAttribute8 | — |
| GLOBAL_ATTRIBUTE9 | GlobalAttribute9 | — |
| GLOBAL_ATTRIBUTE_CATEGORY | GlobalAttributeCategory | — |
| GROUP_REQUISITION_LINES | GroupRequisitionLines | — |
| GROUP_REQUISITIONS | GroupRequisitions | — |
| HDR_ATTR_DEFAULT_MAX_SCORE | HdrAttrDefaultMaxScore | — |
| HDR_ATTR_DISP_SCORE_CRITERIA | HdrAttrDispScoreCriteria | — |
| HDR_ATTR_ENABLE_WEIGHTS | HdrAttrEnableWeights | — |
| INSPECTION_REQUIRED_FLAG | InspectionRequiredFlag | — |
| INVENTORY_ORGANIZATION_ID | InventoryOrganizationId | — |
| INVENTORY_ORGANIZATION_ID | InventoryOrganizationId1 | — |
| INVOICE_CLOSE_CODE | InvoiceCloseCode | — |
| INVOICE_CLOSE_TOLERANCE | InvoiceCloseTolerance | — |
| LANGUAGE_CODE | LanguageCode | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| LINE_TYPE_ID | LineTypeId | — |
| MANUAL_RECEIPT_NUM_TYPE | ManualReceiptNumType | — |
| MANUAL_REQ_NUM_TYPE | ManualReqNumType | — |
| MATCH_OPTION | MatchOption | — |
| MAX_ATTACHMENT_SIZE | MaxAttachmentSize | — |
| MIN_RELEASE_AMOUNT | MinReleaseAmount | — |
| MODE_OF_TRANSPORT | ModeOfTransport | — |
| NEG_APPROVAL_ENABLED_FLAG | NegApprovalEnabledFlag | — |
| NEXT_APPROVER_LOOKUP_CODE | NextApproverLookupCode | — |
| NEXT_NEGOTIATION_NUMBER | NextNegotiationNumber | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber2 | — |
| PRC_BU_ID | PrcBuId | — |
| PRC_BU_ID | PrcBuId1 | — |
| PRICE_BREAK_LOOKUP_CODE | PriceBreakLookupCode | — |
| PRICE_CHANGE_AMOUNT | PriceChangeAmount | — |
| RANK_INDICATOR | RankIndicator | — |
| RANK_VISIBLE_BLIND | RankVisibleBlind | — |
| RECEIVE_CLOSE_CODE | ReceiveCloseCode | — |
| RECEIVE_CLOSE_TOLERANCE | ReceiveCloseTolerance | — |
| RECEIVING_FLAG | ReceivingFlag | — |
| RFQ_ONLY_SITE_FLAG | RfqOnlySiteFlag | — |
| SERVICE_LEVEL | ServiceLevel | — |
| STYLE_ID | StyleId | — |
| SUPPLIER_AUTHORING_ACCEPTANCE | SupplierAuthoringAcceptance | — |
| SUPPLIER_HISTORY_DURATION | SupplierHistoryDuration | — |
| SYSTEM_CONFIGURED_FLAG | SystemConfiguredFlag | — |
| TAX_FROM_ITEM_FLAG | TaxFromItemFlag | — |
| TAX_FROM_SHIP_TO_LOC_FLAG | TaxFromShipToLocFlag | — |
| TAX_FROM_SYSTEM_FLAG | TaxFromSystemFlag | — |
| TAX_FROM_VENDOR_FLAG | TaxFromVendorFlag | — |
| TAX_FROM_VENDOR_SITE_FLAG | TaxFromVendorSiteFlag | — |
| TAX_HIER_ITEM | TaxHierItem | — |
| TAX_HIER_SHIP_TO_LOC | TaxHierShipToLoc | — |
| TAX_HIER_SYSTEM | TaxHierSystem | — |
| TAX_HIER_VENDOR | TaxHierVendor | — |
| TAX_HIER_VENDOR_SITE | TaxHierVendorSite | — |
| TAXABLE_FLAG | TaxableFlag | — |
| TERMS_ID | TermsId | — |
| USE_NEED_BY_DATE | UseNeedByDate | — |
| USE_SALES_ORDER_NUMBER_FLAG | UseSalesOrderNumberFlag | — |
| USE_SHIP_TO | UseShipTo | — |
| USER_DEFINED_RECEIPT_NUM_CODE | UserDefinedReceiptNumCode | — |
| USER_DEFINED_REQ_NUM_CODE | UserDefinedReqNumCode | — |

### [[negotiationresponsepurchaseorderlinepvo|NegotiationResponsePurchaseOrderLinePVO]] (PO · BICC: 1/104)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGING_ONSET_POINT | AgingOnsetPoint | — |
| AGING_PERIOD_DAYS | AgingPeriodDays | — |
| ALLOW_ITEM_DESC_UPDATE_FLAG | AllowItemDescUpdateFlag | — |
| ALLOW_MANUL_PRICE_UPDATE_ORDER | AllowManulPriceUpdateOrder | — |
| ALLOW_RETRO_PRICING | AllowRetroPricing | — |
| AWARD_APPROVAL_ENABLED_FLAG | AwardApprovalEnabledFlag | — |
| BEST_PRICE_VISIBLE_BLIND | BestPriceVisibleBlind | — |
| BUYER_MANAGED_TRANSPORT_FLAG | BuyerManagedTransportFlag | — |
| CARRIER_ID | CarrierId | — |
| CAT_ADMIN_AUTHORING_ACCEPTANCE | CatAdminAuthoringAcceptance | — |
| COLLAB_SECURITY_PROFILE_ID | CollabSecurityProfileId | — |
| CONSUMPTION_ADVICE_FREQUENCY | ConsumptionAdviceFrequency | — |
| CONSUMPTION_ADVICE_SUMMARY | ConsumptionAdviceSummary | — |
| CREATE_DEBIT_MEMO_FLAG | CreateDebitMemoFlag | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| CURRENCY_CODE | CurrencyCode | — |
| DEFAULT_BUYER_ID | DefaultBuyerId | — |
| DEFAULT_PROMISE_DATE | DefaultPromiseDate | — |
| DEFAULT_RATE_TYPE | DefaultRateType | — |
| DOCTYPE_ID | DoctypeId | — |
| EMAIL_ATTACHMENT_FILENAME | EmailAttachmentFilename | — |
| ENFORCE_BUYER_AUTHORITY_FLAG | EnforceBuyerAuthorityFlag | — |
| ENFORCE_MIN_BID_PRICE | EnforceMinBidPrice | — |
| ENFORCE_VENDOR_HOLD_FLAG | EnforceVendorHoldFlag | — |
| FOB_LOOKUP_CODE | FobLookupCode | — |
| FREIGHT_TERMS_LOOKUP_CODE | FreightTermsLookupCode | — |
| GEN_ORDER_FOR_NEG_REQS_FLAG | GenOrderForNegReqsFlag | — |
| GLOBAL_ATTRIBUTE1 | GlobalAttribute1 | — |
| GLOBAL_ATTRIBUTE10 | GlobalAttribute10 | — |
| GLOBAL_ATTRIBUTE11 | GlobalAttribute11 | — |
| GLOBAL_ATTRIBUTE12 | GlobalAttribute12 | — |
| GLOBAL_ATTRIBUTE13 | GlobalAttribute13 | — |
| GLOBAL_ATTRIBUTE14 | GlobalAttribute14 | — |
| GLOBAL_ATTRIBUTE15 | GlobalAttribute15 | — |
| GLOBAL_ATTRIBUTE16 | GlobalAttribute16 | — |
| GLOBAL_ATTRIBUTE17 | GlobalAttribute17 | — |
| GLOBAL_ATTRIBUTE18 | GlobalAttribute18 | — |
| GLOBAL_ATTRIBUTE19 | GlobalAttribute19 | — |
| GLOBAL_ATTRIBUTE2 | GlobalAttribute2 | — |
| GLOBAL_ATTRIBUTE20 | GlobalAttribute20 | — |
| GLOBAL_ATTRIBUTE3 | GlobalAttribute3 | — |
| GLOBAL_ATTRIBUTE4 | GlobalAttribute4 | — |
| GLOBAL_ATTRIBUTE5 | GlobalAttribute5 | — |
| GLOBAL_ATTRIBUTE6 | GlobalAttribute6 | — |
| GLOBAL_ATTRIBUTE7 | GlobalAttribute7 | — |
| GLOBAL_ATTRIBUTE8 | GlobalAttribute8 | — |
| GLOBAL_ATTRIBUTE9 | GlobalAttribute9 | — |
| GLOBAL_ATTRIBUTE_CATEGORY | GlobalAttributeCategory | — |
| GROUP_REQUISITION_LINES | GroupRequisitionLines | — |
| GROUP_REQUISITIONS | GroupRequisitions | — |
| HDR_ATTR_DEFAULT_MAX_SCORE | HdrAttrDefaultMaxScore | — |
| HDR_ATTR_DISP_SCORE_CRITERIA | HdrAttrDispScoreCriteria | — |
| HDR_ATTR_ENABLE_WEIGHTS | HdrAttrEnableWeights | — |
| INSPECTION_REQUIRED_FLAG | InspectionRequiredFlag | — |
| INVENTORY_ORGANIZATION_ID | InventoryOrganizationId | — |
| INVOICE_CLOSE_CODE | InvoiceCloseCode | — |
| INVOICE_CLOSE_TOLERANCE | InvoiceCloseTolerance | — |
| LANGUAGE_CODE | LanguageCode | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| LINE_TYPE_ID | LineTypeId | — |
| MANUAL_RECEIPT_NUM_TYPE | ManualReceiptNumType | — |
| MANUAL_REQ_NUM_TYPE | ManualReqNumType | — |
| MATCH_OPTION | MatchOption | — |
| MAX_ATTACHMENT_SIZE | MaxAttachmentSize | — |
| MIN_RELEASE_AMOUNT | MinReleaseAmount | — |
| MODE_OF_TRANSPORT | ModeOfTransport | — |
| NEG_APPROVAL_ENABLED_FLAG | NegApprovalEnabledFlag | — |
| NEXT_APPROVER_LOOKUP_CODE | NextApproverLookupCode | — |
| NEXT_NEGOTIATION_NUMBER | NextNegotiationNumber | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber2 | — |
| PRC_BU_ID | PrcBuId | — |
| PRICE_BREAK_LOOKUP_CODE | PriceBreakLookupCode | — |
| PRICE_CHANGE_AMOUNT | PriceChangeAmount | — |
| RANK_INDICATOR | RankIndicator | — |
| RANK_VISIBLE_BLIND | RankVisibleBlind | — |
| RECEIVE_CLOSE_CODE | ReceiveCloseCode | — |
| RECEIVE_CLOSE_TOLERANCE | ReceiveCloseTolerance | — |
| RECEIVING_FLAG | ReceivingFlag | — |
| RFQ_ONLY_SITE_FLAG | RfqOnlySiteFlag | — |
| SERVICE_LEVEL | ServiceLevel | — |
| STYLE_ID | StyleId | — |
| SUPPLIER_AUTHORING_ACCEPTANCE | SupplierAuthoringAcceptance | — |
| SUPPLIER_HISTORY_DURATION | SupplierHistoryDuration | — |
| SYSTEM_CONFIGURED_FLAG | SystemConfiguredFlag | — |
| TAX_FROM_ITEM_FLAG | TaxFromItemFlag | — |
| TAX_FROM_SHIP_TO_LOC_FLAG | TaxFromShipToLocFlag | — |
| TAX_FROM_SYSTEM_FLAG | TaxFromSystemFlag | — |
| TAX_FROM_VENDOR_FLAG | TaxFromVendorFlag | — |
| TAX_FROM_VENDOR_SITE_FLAG | TaxFromVendorSiteFlag | — |
| TAX_HIER_ITEM | TaxHierItem | — |
| TAX_HIER_SHIP_TO_LOC | TaxHierShipToLoc | — |
| TAX_HIER_SYSTEM | TaxHierSystem | — |
| TAX_HIER_VENDOR | TaxHierVendor | — |
| TAX_HIER_VENDOR_SITE | TaxHierVendorSite | — |
| TAXABLE_FLAG | TaxableFlag | — |
| TERMS_ID | TermsId | — |
| USE_NEED_BY_DATE | UseNeedByDate | — |
| USE_SALES_ORDER_NUMBER_FLAG | UseSalesOrderNumberFlag | — |
| USE_SHIP_TO | UseShipTo | — |
| USER_DEFINED_RECEIPT_NUM_CODE | UserDefinedReceiptNumCode | — |
| USER_DEFINED_REQ_NUM_CODE | UserDefinedReqNumCode | — |

### [[negotiationresponserequirementandattributepvo|NegotiationResponseRequirementAndAttributePVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGING_ONSET_POINT | AgingOnsetPoint | — |
| AGING_PERIOD_DAYS | AgingPeriodDays | — |
| ALLOW_ITEM_DESC_UPDATE_FLAG | AllowItemDescUpdateFlag | — |
| ALLOW_MANUL_PRICE_UPDATE_ORDER | AllowManulPriceUpdateOrder | — |
| ALLOW_RETRO_PRICING | AllowRetroPricing | — |
| AWARD_APPROVAL_ENABLED_FLAG | AwardApprovalEnabledFlag | — |
| BEST_PRICE_VISIBLE_BLIND | BestPriceVisibleBlind | — |
| BUYER_MANAGED_TRANSPORT_FLAG | BuyerManagedTransportFlag | — |
| CARRIER_ID | CarrierId | — |
| CAT_ADMIN_AUTHORING_ACCEPTANCE | CatAdminAuthoringAcceptance | — |
| COLLAB_SECURITY_PROFILE_ID | CollabSecurityProfileId | — |
| CONSUMPTION_ADVICE_FREQUENCY | ConsumptionAdviceFrequency | — |
| CONSUMPTION_ADVICE_SUMMARY | ConsumptionAdviceSummary | — |
| CREATE_DEBIT_MEMO_FLAG | CreateDebitMemoFlag | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| CURRENCY_CODE | CurrencyCode | — |
| DEFAULT_BUYER_ID | DefaultBuyerId | — |
| DEFAULT_PROMISE_DATE | DefaultPromiseDate | — |
| DEFAULT_RATE_TYPE | DefaultRateType | — |
| DOCTYPE_ID | DoctypeId | — |
| EMAIL_ATTACHMENT_FILENAME | EmailAttachmentFilename | — |
| ENFORCE_BUYER_AUTHORITY_FLAG | EnforceBuyerAuthorityFlag | — |
| ENFORCE_MIN_BID_PRICE | EnforceMinBidPrice | — |
| ENFORCE_VENDOR_HOLD_FLAG | EnforceVendorHoldFlag | — |
| FOB_LOOKUP_CODE | FobLookupCode | — |
| FREIGHT_TERMS_LOOKUP_CODE | FreightTermsLookupCode | — |
| GEN_ORDER_FOR_NEG_REQS_FLAG | GenOrderForNegReqsFlag | — |
| GLOBAL_ATTRIBUTE1 | GlobalAttribute1 | — |
| GLOBAL_ATTRIBUTE10 | GlobalAttribute10 | — |
| GLOBAL_ATTRIBUTE11 | GlobalAttribute11 | — |
| GLOBAL_ATTRIBUTE12 | GlobalAttribute12 | — |
| GLOBAL_ATTRIBUTE13 | GlobalAttribute13 | — |
| GLOBAL_ATTRIBUTE14 | GlobalAttribute14 | — |
| GLOBAL_ATTRIBUTE15 | GlobalAttribute15 | — |
| GLOBAL_ATTRIBUTE16 | GlobalAttribute16 | — |
| GLOBAL_ATTRIBUTE17 | GlobalAttribute17 | — |
| GLOBAL_ATTRIBUTE18 | GlobalAttribute18 | — |
| GLOBAL_ATTRIBUTE19 | GlobalAttribute19 | — |
| GLOBAL_ATTRIBUTE2 | GlobalAttribute2 | — |
| GLOBAL_ATTRIBUTE20 | GlobalAttribute20 | — |
| GLOBAL_ATTRIBUTE3 | GlobalAttribute3 | — |
| GLOBAL_ATTRIBUTE4 | GlobalAttribute4 | — |
| GLOBAL_ATTRIBUTE5 | GlobalAttribute5 | — |
| GLOBAL_ATTRIBUTE6 | GlobalAttribute6 | — |
| GLOBAL_ATTRIBUTE7 | GlobalAttribute7 | — |
| GLOBAL_ATTRIBUTE8 | GlobalAttribute8 | — |
| GLOBAL_ATTRIBUTE9 | GlobalAttribute9 | — |
| GLOBAL_ATTRIBUTE_CATEGORY | GlobalAttributeCategory | — |
| GROUP_REQUISITION_LINES | GroupRequisitionLines | — |
| GROUP_REQUISITIONS | GroupRequisitions | — |
| HDR_ATTR_DEFAULT_MAX_SCORE | HdrAttrDefaultMaxScore | — |
| HDR_ATTR_DISP_SCORE_CRITERIA | HdrAttrDispScoreCriteria | — |
| HDR_ATTR_ENABLE_WEIGHTS | HdrAttrEnableWeights | — |
| INSPECTION_REQUIRED_FLAG | InspectionRequiredFlag | — |
| INVENTORY_ORGANIZATION_ID | InventoryOrganizationId | — |
| INVOICE_CLOSE_CODE | InvoiceCloseCode | — |
| INVOICE_CLOSE_TOLERANCE | InvoiceCloseTolerance | — |
| LANGUAGE_CODE | LanguageCode | — |
| LAST_UPDATE_DATE | LastUpdateDate | — |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| LINE_TYPE_ID | LineTypeId | — |
| MANUAL_RECEIPT_NUM_TYPE | ManualReceiptNumType | — |
| MANUAL_REQ_NUM_TYPE | ManualReqNumType | — |
| MATCH_OPTION | MatchOption | — |
| MAX_ATTACHMENT_SIZE | MaxAttachmentSize | — |
| MIN_RELEASE_AMOUNT | MinReleaseAmount | — |
| MODE_OF_TRANSPORT | ModeOfTransport1 | — |
| NEG_APPROVAL_ENABLED_FLAG | NegApprovalEnabledFlag | — |
| NEXT_APPROVER_LOOKUP_CODE | NextApproverLookupCode | — |
| NEXT_NEGOTIATION_NUMBER | NextNegotiationNumber | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber2 | — |
| PRC_BU_ID | PrcBuId | — |
| PRICE_BREAK_LOOKUP_CODE | PriceBreakLookupCode | — |
| PRICE_CHANGE_AMOUNT | PriceChangeAmount | — |
| RANK_INDICATOR | RankIndicator | — |
| RANK_VISIBLE_BLIND | RankVisibleBlind | — |
| RECEIVE_CLOSE_CODE | ReceiveCloseCode | — |
| RECEIVE_CLOSE_TOLERANCE | ReceiveCloseTolerance | — |
| RECEIVING_FLAG | ReceivingFlag | — |
| RFQ_ONLY_SITE_FLAG | RfqOnlySiteFlag | — |
| SERVICE_LEVEL | ServiceLevel1 | — |
| STYLE_ID | StyleId | — |
| SUPPLIER_AUTHORING_ACCEPTANCE | SupplierAuthoringAcceptance | — |
| SUPPLIER_HISTORY_DURATION | SupplierHistoryDuration | — |
| SYSTEM_CONFIGURED_FLAG | SystemConfiguredFlag | — |
| TAX_FROM_ITEM_FLAG | TaxFromItemFlag | — |
| TAX_FROM_SHIP_TO_LOC_FLAG | TaxFromShipToLocFlag | — |
| TAX_FROM_SYSTEM_FLAG | TaxFromSystemFlag | — |
| TAX_FROM_VENDOR_FLAG | TaxFromVendorFlag | — |
| TAX_FROM_VENDOR_SITE_FLAG | TaxFromVendorSiteFlag | — |
| TAX_HIER_ITEM | TaxHierItem | — |
| TAX_HIER_SHIP_TO_LOC | TaxHierShipToLoc | — |
| TAX_HIER_SYSTEM | TaxHierSystem | — |
| TAX_HIER_VENDOR | TaxHierVendor | — |
| TAX_HIER_VENDOR_SITE | TaxHierVendorSite | — |
| TAXABLE_FLAG | TaxableFlag | — |
| TERMS_ID | TermsId | — |
| USE_NEED_BY_DATE | UseNeedByDate | — |
| USE_SALES_ORDER_NUMBER_FLAG | UseSalesOrderNumberFlag | — |
| USE_SHIP_TO | UseShipTo | — |
| USER_DEFINED_RECEIPT_NUM_CODE | UserDefinedReceiptNumCode | — |
| USER_DEFINED_REQ_NUM_CODE | UserDefinedReqNumCode | — |

### [[purchasingdocumentheaderextractpvo|PurchasingDocumentHeaderExtractPVO]] (PO · BICC: 38/38)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_ITEM_DESC_UPDATE_FLAG | AllowItemDescUpdateFlag | ✅ |
| ALLOW_MANUL_PRICE_UPDATE_ORDER | AllowManulPriceUpdateOrder | ✅ |
| ALLOW_RETRO_PRICING | AllowRetroPricing | ✅ |
| AWARD_APPROVAL_ENABLED_FLAG | AwardApprovalEnabledFlag | ✅ |
| BYPASS_APPROVAL_FLAG | BypassApprovalFlag | ✅ |
| CAT_ADMIN_AUTHORING_ACCEPTANCE | CatAdminAuthoringAcceptance | ✅ |
| CURRENCY_CODE | CurrencyCode1 | ✅ |
| DEFAULT_BUYER_ID | DefaultBuyerId | ✅ |
| DEFAULT_PROMISE_DATE | DefaultPromiseDate | ✅ |
| DEFAULT_RATE_TYPE | DefaultRateType | ✅ |
| DOCTYPE_ID | DoctypeId | ✅ |
| EMAIL_ATTACHMENT_FILENAME | EmailAttachmentFilename | ✅ |
| ENFORCE_MIN_BID_PRICE | EnforceMinBidPrice | ✅ |
| ENFORCE_VENDOR_HOLD_FLAG | EnforceVendorHoldFlag | ✅ |
| GEN_ORDER_FOR_NEG_REQS_FLAG | GenOrderForNegReqsFlag | ✅ |
| INVENTORY_ORGANIZATION_ID | InventoryOrganizationId | ✅ |
| INVOICE_CLOSE_TOLERANCE | InvoiceCloseTolerance | ✅ |
| LANGUAGE_CODE | LanguageCode | ✅ |
| LINE_TYPE_ID | LineTypeId | ✅ |
| MANUAL_RECEIPT_NUM_TYPE | ManualReceiptNumType | ✅ |
| MATCH_OPTION | MatchOption | ✅ |
| MAX_ATTACHMENT_SIZE | MaxAttachmentSize | ✅ |
| MODE_OF_TRANSPORT | ModeOfTransport1 | ✅ |
| NEG_APPROVAL_ENABLED_FLAG | NegApprovalEnabledFlag | ✅ |
| PRC_BU_ID | ProcurementOptionsPrcBuId | ✅ |
| PRICE_BREAK_LOOKUP_CODE | PriceBreakLookupCode | ✅ |
| PRICE_CHANGE_AMOUNT | PriceChangeAmount | ✅ |
| RECEIVE_CLOSE_CODE | ReceiveCloseCode | ✅ |
| RECEIVE_CLOSE_TOLERANCE | ReceiveCloseTolerance | ✅ |
| RECEIVING_FLAG | ReceivingFlag | ✅ |
| SERVICE_LEVEL | ServiceLevel1 | ✅ |
| SOURCING_SUPP_ELIGIBILITY_FLAG | SourcingSuppEligibilityFlag | ✅ |
| STYLE_ID | StyleId1 | ✅ |
| SUPPLIER_AUTHORING_ACCEPTANCE | SupplierAuthoringAcceptance | ✅ |
| TERMS_ID | TermsId1 | ✅ |
| USE_SHIP_TO_FOR_GROUP_REQS | UseShipToForGroupReqs1 | ✅ |
| USER_DEFINED_RECEIPT_NUM_CODE | UserDefinedReceiptNumCode | ✅ |
| USER_DEFINED_REQ_NUM_CODE | UserDefinedReqNumCode | ✅ |

### [[purchasingdocumentlinepvo|PurchasingDocumentLinePVO]] (PO · BICC: 1/71)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_ITEM_DESC_UPDATE_FLAG | POSystemParametersAllowItemDescUpdateFlag | — |
| ALLOW_RETRO_PRICING | POSystemParametersAllowRetroPricing | — |
| BEST_PRICE_VISIBLE_BLIND | POSystemParametersBestPriceVisibleBlind | — |
| CARRIER_ID | POSystemParametersCarrierId | — |
| CAT_ADMIN_AUTHORING_ACCEPTANCE | POSystemParametersCatAdminAuthoringAcceptance | — |
| COLLAB_SECURITY_PROFILE_ID | POSystemParametersCollabSecurityProfileId | — |
| CREATE_DEBIT_MEMO_FLAG | POSystemParametersCreateDebitMemoFlag | — |
| CREATED_BY | POSystemParametersCreatedBy | — |
| CREATION_DATE | POSystemParametersCreationDate | — |
| CURRENCY_CODE | POSystemParametersCurrencyCode | — |
| DEFAULT_PROMISE_DATE | POSystemParametersDefaultPromiseDate | — |
| DEFAULT_RATE_TYPE | POSystemParametersDefaultRateType | — |
| DOCTYPE_ID | POSystemParametersDoctypeId | — |
| EMAIL_ATTACHMENT_FILENAME | POSystemParametersEmailAttachmentFilename | — |
| ENFORCE_BUYER_AUTHORITY_FLAG | POSystemParametersEnforceBuyerAuthorityFlag | — |
| ENFORCE_MIN_BID_PRICE | POSystemParametersEnforceMinBidPrice | — |
| ENFORCE_VENDOR_HOLD_FLAG | POSystemParametersEnforceVendorHoldFlag | — |
| FOB_LOOKUP_CODE | POSystemParametersFobLookupCode | — |
| FREIGHT_TERMS_LOOKUP_CODE | POSystemParametersFreightTermsLookupCode | — |
| GROUP_REQUISITION_LINES | POSystemParametersGroupRequisitionLines | — |
| GROUP_REQUISITIONS | POSystemParametersGroupRequisitions | — |
| HDR_ATTR_DEFAULT_MAX_SCORE | POSystemParametersHdrAttrDefaultMaxScore | — |
| HDR_ATTR_DISP_SCORE_CRITERIA | POSystemParametersHdrAttrDispScoreCriteria | — |
| HDR_ATTR_ENABLE_WEIGHTS | POSystemParametersHdrAttrEnableWeights | — |
| INSPECTION_REQUIRED_FLAG | POSystemParametersInspectionRequiredFlag | — |
| INVENTORY_ORGANIZATION_ID | POSystemParametersInventoryOrganizationId | — |
| INVOICE_CLOSE_CODE | POSystemParametersInvoiceCloseCode | — |
| INVOICE_CLOSE_TOLERANCE | POSystemParametersInvoiceCloseTolerance | — |
| LANGUAGE_CODE | POSystemParametersLanguageCode | — |
| LAST_UPDATE_DATE | POSystemParametersLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | POSystemParametersLastUpdateLogin | — |
| LAST_UPDATED_BY | POSystemParametersLastUpdatedBy | — |
| LINE_TYPE_ID | POSystemParametersLineTypeId | — |
| MANUAL_RECEIPT_NUM_TYPE | POSystemParametersManualReceiptNumType | — |
| MANUAL_REQ_NUM_TYPE | POSystemParametersManualReqNumType | — |
| MATCH_OPTION | POSystemParametersMatchOption | — |
| MAX_ATTACHMENT_SIZE | POSystemParametersMaxAttachmentSize | — |
| MIN_RELEASE_AMOUNT | POSystemParametersMinReleaseAmount | — |
| MODE_OF_TRANSPORT | POSystemParametersModeOfTransport | — |
| NEXT_APPROVER_LOOKUP_CODE | POSystemParametersNextApproverLookupCode | — |
| NEXT_NEGOTIATION_NUMBER | POSystemParametersNextNegotiationNumber | — |
| OBJECT_VERSION_NUMBER | POSystemParametersObjectVersionNumber | — |
| PRC_BU_ID | POSystemParametersPrcBuId | — |
| PRICE_BREAK_LOOKUP_CODE | POSystemParametersPriceBreakLookupCode | — |
| PRICE_CHANGE_AMOUNT | POSystemParametersPriceChangeAmount | — |
| RANK_INDICATOR | POSystemParametersRankIndicator | — |
| RANK_VISIBLE_BLIND | POSystemParametersRankVisibleBlind | — |
| RECEIVE_CLOSE_CODE | POSystemParametersReceiveCloseCode | — |
| RECEIVE_CLOSE_TOLERANCE | POSystemParametersReceiveCloseTolerance | — |
| RECEIVING_FLAG | POSystemParametersReceivingFlag | — |
| RFQ_ONLY_SITE_FLAG | POSystemParametersRfqOnlySiteFlag | — |
| SERVICE_LEVEL | POSystemParametersServiceLevel | — |
| STYLE_ID | POSystemParametersStyleId | — |
| SUPPLIER_AUTHORING_ACCEPTANCE | POSystemParametersSupplierAuthoringAcceptance | — |
| SUPPLIER_HISTORY_DURATION | POSystemParametersSupplierHistoryDuration | — |
| TAX_FROM_ITEM_FLAG | POSystemParametersTaxFromItemFlag | — |
| TAX_FROM_SHIP_TO_LOC_FLAG | POSystemParametersTaxFromShipToLocFlag | — |
| TAX_FROM_SYSTEM_FLAG | POSystemParametersTaxFromSystemFlag | — |
| TAX_FROM_VENDOR_FLAG | POSystemParametersTaxFromVendorFlag | — |
| TAX_FROM_VENDOR_SITE_FLAG | POSystemParametersTaxFromVendorSiteFlag | — |
| TAX_HIER_ITEM | POSystemParametersTaxHierItem | — |
| TAX_HIER_SHIP_TO_LOC | POSystemParametersTaxHierShipToLoc | — |
| TAX_HIER_SYSTEM | POSystemParametersTaxHierSystem | — |
| TAX_HIER_VENDOR | POSystemParametersTaxHierVendor | — |
| TAX_HIER_VENDOR_SITE | POSystemParametersTaxHierVendorSite | — |
| TAXABLE_FLAG | POSystemParametersTaxableFlag | — |
| TERMS_ID | POSystemParametersTermsId | — |
| USE_NEED_BY_DATE | POSystemParametersUseNeedByDate | — |
| USE_SHIP_TO | POSystemParametersUseShipTo | — |
| USER_DEFINED_RECEIPT_NUM_CODE | POSystemParametersUserDefinedReceiptNumCode | — |
| USER_DEFINED_REQ_NUM_CODE | POSystemParametersUserDefinedReqNumCode | — |

### [[purchasingsystemparameterextractpvo|PurchasingSystemParameterExtractPVO]] (PO · BICC: 75/75)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGING_ONSET_POINT | AgingOnsetPoint | ✅ |
| AGING_PERIOD_DAYS | AgingPeriodDays | ✅ |
| ALLOW_ITEM_DESC_UPDATE_FLAG | AllowItemDescUpdateFlag | ✅ |
| ALLOW_MANUL_PRICE_UPDATE_ORDER | AllowManulPriceUpdateOrder | ✅ |
| ALLOW_RETRO_PRICING | AllowRetroPricing | ✅ |
| AWARD_APPROVAL_ENABLED_FLAG | AwardApprovalEnabledFlag | ✅ |
| BUYER_MANAGED_TRANSPORT_FLAG | BuyerManagedTransportFlag | ✅ |
| BYPASS_APPROVAL_FLAG | BypassApprovalFlag | ✅ |
| CARRIER_ID | CarrierId | ✅ |
| CAT_ADMIN_AUTHORING_ACCEPTANCE | CatAdminAuthoringAcceptance | ✅ |
| COMMUNICATE_CO_FLAG | CommunicateCoFlag | ✅ |
| COMMUNICATE_PA_FLAG | CommunicatePaFlag | ✅ |
| CONSUMPTION_ADVICE_FREQUENCY | ConsumptionAdviceFrequency | ✅ |
| CONSUMPTION_ADVICE_SUMMARY | ConsumptionAdviceSummary | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| CURRENCY_CODE | CurrencyCode | ✅ |
| DEFAULT_BUYER_ID | DefaultBuyerId | ✅ |
| DEFAULT_PROMISE_DATE | DefaultPromiseDate | ✅ |
| DEFAULT_RATE_TYPE | DefaultRateType | ✅ |
| DOCTYPE_ID | DoctypeId | ✅ |
| EMAIL_ATTACHMENT_FILENAME | EmailAttachmentFilename | ✅ |
| ENFORCE_MIN_BID_PRICE | EnforceMinBidPrice | ✅ |
| ENFORCE_VENDOR_HOLD_FLAG | EnforceVendorHoldFlag | ✅ |
| FOB_LOOKUP_CODE | FobLookupCode | ✅ |
| FREIGHT_TERMS_LOOKUP_CODE | FreightTermsLookupCode | ✅ |
| GEN_ORDER_FOR_NEG_REQS_FLAG | GenOrderForNegReqsFlag | ✅ |
| GENERATE_ORDERS_AUTOMATIC | GenerateOrdersAutomatic | ✅ |
| GROUP_REQUISITION_LINES | GroupRequisitionLines | ✅ |
| GROUP_REQUISITIONS | GroupRequisitions | ✅ |
| INVENTORY_ORGANIZATION_ID | InventoryOrganizationId | ✅ |
| INVOICE_CLOSE_TOLERANCE | InvoiceCloseTolerance | ✅ |
| LANGUAGE_CODE | LanguageCode | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LINE_TYPE_ID | LineTypeId | ✅ |
| MANUAL_RECEIPT_NUM_TYPE | ManualReceiptNumType | ✅ |
| MANUAL_REQ_NUM_TYPE | ManualReqNumType | ✅ |
| MATCH_OPTION | MatchOption | ✅ |
| MAX_ATTACHMENT_SIZE | MaxAttachmentSize | ✅ |
| MIN_RELEASE_AMOUNT | MinReleaseAmount | ✅ |
| MODE_OF_TRANSPORT | ModeOfTransport | ✅ |
| NEG_APPROVAL_ENABLED_FLAG | NegApprovalEnabledFlag | ✅ |
| NEXT_APPROVER_LOOKUP_CODE | NextApproverLookupCode | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| PRC_BU_ID | PrcBuId | ✅ |
| PRICE_BREAK_LOOKUP_CODE | PriceBreakLookupCode | ✅ |
| PRICE_CHANGE_AMOUNT | PriceChangeAmount | ✅ |
| RECEIVE_CLOSE_CODE | ReceiveCloseCode | ✅ |
| RECEIVE_CLOSE_TOLERANCE | ReceiveCloseTolerance | ✅ |
| RECEIVING_FLAG | ReceivingFlag | ✅ |
| RFQ_ONLY_SITE_FLAG | RfqOnlySiteFlag | ✅ |
| SERVICE_LEVEL | ServiceLevel | ✅ |
| SOURCING_SUPP_ELIGIBILITY_FLAG | SourcingSuppEligibilityFlag | ✅ |
| STYLE_ID | StyleId | ✅ |
| SUBMIT_APPROVAL_AUTOMATIC | SubmitApprovalAutomatic | ✅ |
| SUPPLIER_AUTHORING_ACCEPTANCE | SupplierAuthoringAcceptance | ✅ |
| TAX_FROM_ITEM_FLAG | TaxFromItemFlag | ✅ |
| TAX_FROM_SHIP_TO_LOC_FLAG | TaxFromShipToLocFlag | ✅ |
| TAX_FROM_SYSTEM_FLAG | TaxFromSystemFlag | ✅ |
| TAX_FROM_VENDOR_FLAG | TaxFromVendorFlag | ✅ |
| TAX_FROM_VENDOR_SITE_FLAG | TaxFromVendorSiteFlag | ✅ |
| TAX_HIER_ITEM | TaxHierItem | ✅ |
| TAX_HIER_SHIP_TO_LOC | TaxHierShipToLoc | ✅ |
| TAX_HIER_SYSTEM | TaxHierSystem | ✅ |
| TAX_HIER_VENDOR | TaxHierVendor | ✅ |
| TAX_HIER_VENDOR_SITE | TaxHierVendorSite | ✅ |
| TERMS_ID | TermsId | ✅ |
| USE_NEED_BY_DATE | UseNeedByDate | ✅ |
| USE_SALES_ORDER_NUMBER_FLAG | UseSalesOrderNumberFlag | ✅ |
| USE_SHIP_TO | UseShipTo | ✅ |
| USE_SHIP_TO_FOR_GROUP_REQS | UseShipToForGroupReqs | ✅ |
| USER_DEFINED_RECEIPT_NUM_CODE | UserDefinedReceiptNumCode | ✅ |
| USER_DEFINED_REQ_NUM_CODE | UserDefinedReqNumCode | ✅ |

### [[sourcingrequirementandattributepvo|SourcingRequirementAndAttributePVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGING_ONSET_POINT | AgingOnsetPoint | — |
| AGING_PERIOD_DAYS | AgingPeriodDays | — |
| ALLOW_ITEM_DESC_UPDATE_FLAG | AllowItemDescUpdateFlag | — |
| ALLOW_MANUL_PRICE_UPDATE_ORDER | AllowManulPriceUpdateOrder | — |
| ALLOW_RETRO_PRICING | AllowRetroPricing | — |
| AWARD_APPROVAL_ENABLED_FLAG | AwardApprovalEnabledFlag | — |
| BEST_PRICE_VISIBLE_BLIND | BestPriceVisibleBlind | — |
| BUYER_MANAGED_TRANSPORT_FLAG | BuyerManagedTransportFlag | — |
| CARRIER_ID | CarrierId | — |
| CAT_ADMIN_AUTHORING_ACCEPTANCE | CatAdminAuthoringAcceptance | — |
| COLLAB_SECURITY_PROFILE_ID | CollabSecurityProfileId | — |
| CONSUMPTION_ADVICE_FREQUENCY | ConsumptionAdviceFrequency | — |
| CONSUMPTION_ADVICE_SUMMARY | ConsumptionAdviceSummary | — |
| CREATE_DEBIT_MEMO_FLAG | CreateDebitMemoFlag | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| CURRENCY_CODE | CurrencyCode | — |
| DEFAULT_BUYER_ID | DefaultBuyerId | — |
| DEFAULT_PROMISE_DATE | DefaultPromiseDate | — |
| DEFAULT_RATE_TYPE | DefaultRateType | — |
| DOCTYPE_ID | DoctypeId | — |
| EMAIL_ATTACHMENT_FILENAME | EmailAttachmentFilename | — |
| ENFORCE_BUYER_AUTHORITY_FLAG | EnforceBuyerAuthorityFlag | — |
| ENFORCE_MIN_BID_PRICE | EnforceMinBidPrice | — |
| ENFORCE_VENDOR_HOLD_FLAG | EnforceVendorHoldFlag | — |
| FOB_LOOKUP_CODE | FobLookupCode | — |
| FREIGHT_TERMS_LOOKUP_CODE | FreightTermsLookupCode | — |
| GEN_ORDER_FOR_NEG_REQS_FLAG | GenOrderForNegReqsFlag | — |
| GLOBAL_ATTRIBUTE1 | GlobalAttribute1 | — |
| GLOBAL_ATTRIBUTE10 | GlobalAttribute10 | — |
| GLOBAL_ATTRIBUTE11 | GlobalAttribute11 | — |
| GLOBAL_ATTRIBUTE12 | GlobalAttribute12 | — |
| GLOBAL_ATTRIBUTE13 | GlobalAttribute13 | — |
| GLOBAL_ATTRIBUTE14 | GlobalAttribute14 | — |
| GLOBAL_ATTRIBUTE15 | GlobalAttribute15 | — |
| GLOBAL_ATTRIBUTE16 | GlobalAttribute16 | — |
| GLOBAL_ATTRIBUTE17 | GlobalAttribute17 | — |
| GLOBAL_ATTRIBUTE18 | GlobalAttribute18 | — |
| GLOBAL_ATTRIBUTE19 | GlobalAttribute19 | — |
| GLOBAL_ATTRIBUTE2 | GlobalAttribute2 | — |
| GLOBAL_ATTRIBUTE20 | GlobalAttribute20 | — |
| GLOBAL_ATTRIBUTE3 | GlobalAttribute3 | — |
| GLOBAL_ATTRIBUTE4 | GlobalAttribute4 | — |
| GLOBAL_ATTRIBUTE5 | GlobalAttribute5 | — |
| GLOBAL_ATTRIBUTE6 | GlobalAttribute6 | — |
| GLOBAL_ATTRIBUTE7 | GlobalAttribute7 | — |
| GLOBAL_ATTRIBUTE8 | GlobalAttribute8 | — |
| GLOBAL_ATTRIBUTE9 | GlobalAttribute9 | — |
| GLOBAL_ATTRIBUTE_CATEGORY | GlobalAttributeCategory | — |
| GROUP_REQUISITION_LINES | GroupRequisitionLines | — |
| GROUP_REQUISITIONS | GroupRequisitions | — |
| HDR_ATTR_DEFAULT_MAX_SCORE | HdrAttrDefaultMaxScore | — |
| HDR_ATTR_DISP_SCORE_CRITERIA | HdrAttrDispScoreCriteria | — |
| HDR_ATTR_ENABLE_WEIGHTS | HdrAttrEnableWeights | — |
| INSPECTION_REQUIRED_FLAG | InspectionRequiredFlag | — |
| INVENTORY_ORGANIZATION_ID | InventoryOrganizationId | — |
| INVOICE_CLOSE_CODE | InvoiceCloseCode | — |
| INVOICE_CLOSE_TOLERANCE | InvoiceCloseTolerance | — |
| LANGUAGE_CODE | LanguageCode | — |
| LAST_UPDATE_DATE | LastUpdateDate | — |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| LINE_TYPE_ID | LineTypeId | — |
| MANUAL_RECEIPT_NUM_TYPE | ManualReceiptNumType | — |
| MANUAL_REQ_NUM_TYPE | ManualReqNumType | — |
| MATCH_OPTION | MatchOption | — |
| MAX_ATTACHMENT_SIZE | MaxAttachmentSize | — |
| MIN_RELEASE_AMOUNT | MinReleaseAmount | — |
| MODE_OF_TRANSPORT | ModeOfTransport | — |
| NEG_APPROVAL_ENABLED_FLAG | NegApprovalEnabledFlag | — |
| NEXT_APPROVER_LOOKUP_CODE | NextApproverLookupCode | — |
| NEXT_NEGOTIATION_NUMBER | NextNegotiationNumber | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PRC_BU_ID | PrcBuId | — |
| PRICE_BREAK_LOOKUP_CODE | PriceBreakLookupCode | — |
| PRICE_CHANGE_AMOUNT | PriceChangeAmount | — |
| RANK_INDICATOR | RankIndicator | — |
| RANK_VISIBLE_BLIND | RankVisibleBlind | — |
| RECEIVE_CLOSE_CODE | ReceiveCloseCode | — |
| RECEIVE_CLOSE_TOLERANCE | ReceiveCloseTolerance | — |
| RECEIVING_FLAG | ReceivingFlag | — |
| RFQ_ONLY_SITE_FLAG | RfqOnlySiteFlag | — |
| SERVICE_LEVEL | ServiceLevel | — |
| STYLE_ID | StyleId | — |
| SUPPLIER_AUTHORING_ACCEPTANCE | SupplierAuthoringAcceptance | — |
| SUPPLIER_HISTORY_DURATION | SupplierHistoryDuration | — |
| SYSTEM_CONFIGURED_FLAG | SystemConfiguredFlag | — |
| TAX_FROM_ITEM_FLAG | TaxFromItemFlag | — |
| TAX_FROM_SHIP_TO_LOC_FLAG | TaxFromShipToLocFlag | — |
| TAX_FROM_SYSTEM_FLAG | TaxFromSystemFlag | — |
| TAX_FROM_VENDOR_FLAG | TaxFromVendorFlag | — |
| TAX_FROM_VENDOR_SITE_FLAG | TaxFromVendorSiteFlag | — |
| TAX_HIER_ITEM | TaxHierItem | — |
| TAX_HIER_SHIP_TO_LOC | TaxHierShipToLoc | — |
| TAX_HIER_SYSTEM | TaxHierSystem | — |
| TAX_HIER_VENDOR | TaxHierVendor | — |
| TAX_HIER_VENDOR_SITE | TaxHierVendorSite | — |
| TAXABLE_FLAG | TaxableFlag | — |
| TERMS_ID | TermsId | — |
| USE_NEED_BY_DATE | UseNeedByDate | — |
| USE_SALES_ORDER_NUMBER_FLAG | UseSalesOrderNumberFlag | — |
| USE_SHIP_TO | UseShipTo | — |
| USER_DEFINED_RECEIPT_NUM_CODE | UserDefinedReceiptNumCode | — |
| USER_DEFINED_REQ_NUM_CODE | UserDefinedReqNumCode | — |

### [[standarddistributionpvo|StandardDistributionPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_ITEM_DESC_UPDATE_FLAG | PurchasingSystemParameterAllowItemDescUpdateFlag | — |
| ALLOW_RETRO_PRICING | PurchasingSystemParameterAllowRetroPricing | — |
| BEST_PRICE_VISIBLE_BLIND | PurchasingSystemParameterBestPriceVisibleBlind | — |
| CARRIER_ID | PurchasingSystemParameterCarrierId | — |
| CAT_ADMIN_AUTHORING_ACCEPTANCE | PurchasingSystemParameterCatAdminAuthoringAcceptance | — |
| COLLAB_SECURITY_PROFILE_ID | PurchasingSystemParameterCollabSecurityProfileId | — |
| CREATE_DEBIT_MEMO_FLAG | PurchasingSystemParameterCreateDebitMemoFlag | — |
| CURRENCY_CODE | PurchasingSystemParameterCurrencyCode | — |
| DEFAULT_PROMISE_DATE | PurchasingSystemParameterDefaultPromiseDate | — |
| DEFAULT_RATE_TYPE | PurchasingSystemParameterDefaultRateType | — |
| DOCTYPE_ID | PurchasingSystemParameterDoctypeId | — |
| EMAIL_ATTACHMENT_FILENAME | PurchasingSystemParameterEmailAttachmentFilename | — |
| ENFORCE_BUYER_AUTHORITY_FLAG | PurchasingSystemParameterEnforceBuyerAuthorityFlag | — |
| ENFORCE_MIN_BID_PRICE | PurchasingSystemParameterEnforceMinBidPrice | — |
| ENFORCE_VENDOR_HOLD_FLAG | PurchasingSystemParameterEnforceVendorHoldFlag | — |
| FOB_LOOKUP_CODE | PurchasingSystemParameterFobLookupCode | — |
| FREIGHT_TERMS_LOOKUP_CODE | PurchasingSystemParameterFreightTermsLookupCode | — |
| GROUP_REQUISITION_LINES | PurchasingSystemParameterGroupRequisitionLines | — |
| GROUP_REQUISITIONS | PurchasingSystemParameterGroupRequisitions | — |
| HDR_ATTR_DEFAULT_MAX_SCORE | PurchasingSystemParameterHdrAttrDefaultMaxScore | — |
| HDR_ATTR_DISP_SCORE_CRITERIA | PurchasingSystemParameterHdrAttrDispScoreCriteria | — |
| HDR_ATTR_ENABLE_WEIGHTS | PurchasingSystemParameterHdrAttrEnableWeights | — |
| INSPECTION_REQUIRED_FLAG | PurchasingSystemParameterInspectionRequiredFlag | — |
| INVENTORY_ORGANIZATION_ID | PurchasingSystemParameterInventoryOrganizationId | — |
| INVOICE_CLOSE_CODE | PurchasingSystemParameterInvoiceCloseCode | — |
| INVOICE_CLOSE_TOLERANCE | PurchasingSystemParameterInvoiceCloseTolerance | — |
| LANGUAGE_CODE | PurchasingSystemParameterLanguageCode | — |
| LINE_TYPE_ID | PurchasingSystemParameterLineTypeId | — |
| MANUAL_RECEIPT_NUM_TYPE | PurchasingSystemParameterManualReceiptNumType | — |
| MANUAL_REQ_NUM_TYPE | PurchasingSystemParameterManualReqNumType | — |
| MATCH_OPTION | PurchasingSystemParameterMatchOption | — |
| MAX_ATTACHMENT_SIZE | PurchasingSystemParameterMaxAttachmentSize | — |
| MIN_RELEASE_AMOUNT | PurchasingSystemParameterMinReleaseAmount | — |
| MODE_OF_TRANSPORT | PurchasingSystemParameterModeOfTransport | — |
| NEXT_APPROVER_LOOKUP_CODE | PurchasingSystemParameterNextApproverLookupCode | — |
| NEXT_NEGOTIATION_NUMBER | PurchasingSystemParameterNextNegotiationNumber | — |
| OBJECT_VERSION_NUMBER | PurchasingSystemParameterObjectVersionNumber | — |
| PRC_BU_ID | PurchasingSystemParameterPrcBuId | — |
| PRICE_BREAK_LOOKUP_CODE | PurchasingSystemParameterPriceBreakLookupCode | — |
| PRICE_CHANGE_AMOUNT | PurchasingSystemParameterPriceChangeAmount | — |
| RANK_INDICATOR | PurchasingSystemParameterRankIndicator | — |
| RANK_VISIBLE_BLIND | PurchasingSystemParameterRankVisibleBlind | — |
| RECEIVE_CLOSE_CODE | PurchasingSystemParameterReceiveCloseCode | — |
| RECEIVE_CLOSE_TOLERANCE | PurchasingSystemParameterReceiveCloseTolerance | — |
| RECEIVING_FLAG | PurchasingSystemParameterReceivingFlag | — |
| RFQ_ONLY_SITE_FLAG | PurchasingSystemParameterRfqOnlySiteFlag | — |
| SERVICE_LEVEL | PurchasingSystemParameterServiceLevel | — |
| STYLE_ID | PurchasingSystemParameterStyleId | — |
| SUPPLIER_AUTHORING_ACCEPTANCE | PurchasingSystemParameterSupplierAuthoringAcceptance | — |
| SUPPLIER_HISTORY_DURATION | PurchasingSystemParameterSupplierHistoryDuration | — |
| TAX_FROM_ITEM_FLAG | PurchasingSystemParameterTaxFromItemFlag | — |
| TAX_FROM_SHIP_TO_LOC_FLAG | PurchasingSystemParameterTaxFromShipToLocFlag | — |
| TAX_FROM_SYSTEM_FLAG | PurchasingSystemParameterTaxFromSystemFlag | — |
| TAX_FROM_VENDOR_FLAG | PurchasingSystemParameterTaxFromVendorFlag | — |
| TAX_FROM_VENDOR_SITE_FLAG | PurchasingSystemParameterTaxFromVendorSiteFlag | — |
| TAX_HIER_ITEM | PurchasingSystemParameterTaxHierItem | — |
| TAX_HIER_SHIP_TO_LOC | PurchasingSystemParameterTaxHierShipToLoc | — |
| TAX_HIER_SYSTEM | PurchasingSystemParameterTaxHierSystem | — |
| TAX_HIER_VENDOR | PurchasingSystemParameterTaxHierVendor | — |
| TAX_HIER_VENDOR_SITE | PurchasingSystemParameterTaxHierVendorSite | — |
| TAXABLE_FLAG | PurchasingSystemParameterTaxableFlag | — |
| TERMS_ID | PurchasingSystemParameterTermsId | — |
| USE_NEED_BY_DATE | PurchasingSystemParameterUseNeedByDate | — |
| USE_SHIP_TO | PurchasingSystemParameterUseShipTo | — |
| USER_DEFINED_RECEIPT_NUM_CODE | PurchasingSystemParameterUserDefinedReceiptNumCode | — |
| USER_DEFINED_REQ_NUM_CODE | PurchasingSystemParameterUserDefinedReqNumCode | — |

### [[standardheaderpvo|StandardHeaderPVO]] (PO · BICC: 1/71)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_ITEM_DESC_UPDATE_FLAG | POSystemParametersAllowItemDescUpdateFlag | — |
| ALLOW_RETRO_PRICING | POSystemParametersAllowRetroPricing | — |
| BEST_PRICE_VISIBLE_BLIND | POSystemParametersBestPriceVisibleBlind | — |
| CARRIER_ID | POSystemParametersCarrierId | — |
| CAT_ADMIN_AUTHORING_ACCEPTANCE | POSystemParametersCatAdminAuthoringAcceptance | — |
| COLLAB_SECURITY_PROFILE_ID | POSystemParametersCollabSecurityProfileId | — |
| CREATE_DEBIT_MEMO_FLAG | POSystemParametersCreateDebitMemoFlag | — |
| CREATED_BY | POSystemParametersCreatedBy | — |
| CREATION_DATE | POSystemParametersCreationDate | — |
| CURRENCY_CODE | POSystemParametersCurrencyCode | — |
| DEFAULT_PROMISE_DATE | POSystemParametersDefaultPromiseDate | — |
| DEFAULT_RATE_TYPE | POSystemParametersDefaultRateType | — |
| DOCTYPE_ID | POSystemParametersDoctypeId | — |
| EMAIL_ATTACHMENT_FILENAME | POSystemParametersEmailAttachmentFilename | — |
| ENFORCE_BUYER_AUTHORITY_FLAG | POSystemParametersEnforceBuyerAuthorityFlag | — |
| ENFORCE_MIN_BID_PRICE | POSystemParametersEnforceMinBidPrice | — |
| ENFORCE_VENDOR_HOLD_FLAG | POSystemParametersEnforceVendorHoldFlag | — |
| FOB_LOOKUP_CODE | POSystemParametersFobLookupCode | — |
| FREIGHT_TERMS_LOOKUP_CODE | POSystemParametersFreightTermsLookupCode | — |
| GROUP_REQUISITION_LINES | POSystemParametersGroupRequisitionLines | — |
| GROUP_REQUISITIONS | POSystemParametersGroupRequisitions | — |
| HDR_ATTR_DEFAULT_MAX_SCORE | POSystemParametersHdrAttrDefaultMaxScore | — |
| HDR_ATTR_DISP_SCORE_CRITERIA | POSystemParametersHdrAttrDispScoreCriteria | — |
| HDR_ATTR_ENABLE_WEIGHTS | POSystemParametersHdrAttrEnableWeights | — |
| INSPECTION_REQUIRED_FLAG | POSystemParametersInspectionRequiredFlag | — |
| INVENTORY_ORGANIZATION_ID | POSystemParametersInventoryOrganizationId | — |
| INVOICE_CLOSE_CODE | POSystemParametersInvoiceCloseCode | — |
| INVOICE_CLOSE_TOLERANCE | POSystemParametersInvoiceCloseTolerance | — |
| LANGUAGE_CODE | POSystemParametersLanguageCode | — |
| LAST_UPDATE_DATE | POSystemParametersLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | POSystemParametersLastUpdateLogin | — |
| LAST_UPDATED_BY | POSystemParametersLastUpdatedBy | — |
| LINE_TYPE_ID | POSystemParametersLineTypeId | — |
| MANUAL_RECEIPT_NUM_TYPE | POSystemParametersManualReceiptNumType | — |
| MANUAL_REQ_NUM_TYPE | POSystemParametersManualReqNumType | — |
| MATCH_OPTION | POSystemParametersMatchOption | — |
| MAX_ATTACHMENT_SIZE | POSystemParametersMaxAttachmentSize | — |
| MIN_RELEASE_AMOUNT | POSystemParametersMinReleaseAmount | — |
| MODE_OF_TRANSPORT | POSystemParametersModeOfTransport | — |
| NEXT_APPROVER_LOOKUP_CODE | POSystemParametersNextApproverLookupCode | — |
| NEXT_NEGOTIATION_NUMBER | POSystemParametersNextNegotiationNumber | — |
| OBJECT_VERSION_NUMBER | POSystemParametersObjectVersionNumber | — |
| PRC_BU_ID | POSystemParametersPrcBuId | — |
| PRICE_BREAK_LOOKUP_CODE | POSystemParametersPriceBreakLookupCode | — |
| PRICE_CHANGE_AMOUNT | POSystemParametersPriceChangeAmount | — |
| RANK_INDICATOR | POSystemParametersRankIndicator | — |
| RANK_VISIBLE_BLIND | POSystemParametersRankVisibleBlind | — |
| RECEIVE_CLOSE_CODE | POSystemParametersReceiveCloseCode | — |
| RECEIVE_CLOSE_TOLERANCE | POSystemParametersReceiveCloseTolerance | — |
| RECEIVING_FLAG | POSystemParametersReceivingFlag | — |
| RFQ_ONLY_SITE_FLAG | POSystemParametersRfqOnlySiteFlag | — |
| SERVICE_LEVEL | POSystemParametersServiceLevel | — |
| STYLE_ID | POSystemParametersStyleId | — |
| SUPPLIER_AUTHORING_ACCEPTANCE | POSystemParametersSupplierAuthoringAcceptance | — |
| SUPPLIER_HISTORY_DURATION | POSystemParametersSupplierHistoryDuration | — |
| TAX_FROM_ITEM_FLAG | POSystemParametersTaxFromItemFlag | — |
| TAX_FROM_SHIP_TO_LOC_FLAG | POSystemParametersTaxFromShipToLocFlag | — |
| TAX_FROM_SYSTEM_FLAG | POSystemParametersTaxFromSystemFlag | — |
| TAX_FROM_VENDOR_FLAG | POSystemParametersTaxFromVendorFlag | — |
| TAX_FROM_VENDOR_SITE_FLAG | POSystemParametersTaxFromVendorSiteFlag | — |
| TAX_HIER_ITEM | POSystemParametersTaxHierItem | — |
| TAX_HIER_SHIP_TO_LOC | POSystemParametersTaxHierShipToLoc | — |
| TAX_HIER_SYSTEM | POSystemParametersTaxHierSystem | — |
| TAX_HIER_VENDOR | POSystemParametersTaxHierVendor | — |
| TAX_HIER_VENDOR_SITE | POSystemParametersTaxHierVendorSite | — |
| TAXABLE_FLAG | POSystemParametersTaxableFlag | — |
| TERMS_ID | POSystemParametersTermsId | — |
| USE_NEED_BY_DATE | POSystemParametersUseNeedByDate | — |
| USE_SHIP_TO | POSystemParametersUseShipTo | — |
| USER_DEFINED_RECEIPT_NUM_CODE | POSystemParametersUserDefinedReceiptNumCode | — |
| USER_DEFINED_REQ_NUM_CODE | POSystemParametersUserDefinedReqNumCode | — |

### [[standardlinepvo|StandardLinePVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_ITEM_DESC_UPDATE_FLAG | POSystemParametersAllowItemDescUpdateFlag | — |
| ALLOW_RETRO_PRICING | POSystemParametersAllowRetroPricing | — |
| BEST_PRICE_VISIBLE_BLIND | POSystemParametersBestPriceVisibleBlind | — |
| CARRIER_ID | POSystemParametersCarrierId | — |
| CAT_ADMIN_AUTHORING_ACCEPTANCE | POSystemParametersCatAdminAuthoringAcceptance | — |
| COLLAB_SECURITY_PROFILE_ID | POSystemParametersCollabSecurityProfileId | — |
| CREATE_DEBIT_MEMO_FLAG | POSystemParametersCreateDebitMemoFlag | — |
| CREATED_BY | POSystemParametersCreatedBy | — |
| CREATION_DATE | POSystemParametersCreationDate | — |
| CURRENCY_CODE | POSystemParametersCurrencyCode | — |
| DEFAULT_PROMISE_DATE | POSystemParametersDefaultPromiseDate | — |
| DEFAULT_RATE_TYPE | POSystemParametersDefaultRateType | — |
| DOCTYPE_ID | POSystemParametersDoctypeId | — |
| EMAIL_ATTACHMENT_FILENAME | POSystemParametersEmailAttachmentFilename | — |
| ENFORCE_BUYER_AUTHORITY_FLAG | POSystemParametersEnforceBuyerAuthorityFlag | — |
| ENFORCE_MIN_BID_PRICE | POSystemParametersEnforceMinBidPrice | — |
| ENFORCE_VENDOR_HOLD_FLAG | POSystemParametersEnforceVendorHoldFlag | — |
| FOB_LOOKUP_CODE | POSystemParametersFobLookupCode | — |
| FREIGHT_TERMS_LOOKUP_CODE | POSystemParametersFreightTermsLookupCode | — |
| GROUP_REQUISITION_LINES | POSystemParametersGroupRequisitionLines | — |
| GROUP_REQUISITIONS | POSystemParametersGroupRequisitions | — |
| HDR_ATTR_DEFAULT_MAX_SCORE | POSystemParametersHdrAttrDefaultMaxScore | — |
| HDR_ATTR_DISP_SCORE_CRITERIA | POSystemParametersHdrAttrDispScoreCriteria | — |
| HDR_ATTR_ENABLE_WEIGHTS | POSystemParametersHdrAttrEnableWeights | — |
| INSPECTION_REQUIRED_FLAG | POSystemParametersInspectionRequiredFlag | — |
| INVENTORY_ORGANIZATION_ID | POSystemParametersInventoryOrganizationId | — |
| INVOICE_CLOSE_CODE | POSystemParametersInvoiceCloseCode | — |
| INVOICE_CLOSE_TOLERANCE | POSystemParametersInvoiceCloseTolerance | — |
| LANGUAGE_CODE | POSystemParametersLanguageCode | — |
| LAST_UPDATE_DATE | POSystemParametersLastUpdateDate | — |
| LAST_UPDATE_LOGIN | POSystemParametersLastUpdateLogin | — |
| LAST_UPDATED_BY | POSystemParametersLastUpdatedBy | — |
| LINE_TYPE_ID | POSystemParametersLineTypeId | — |
| MANUAL_RECEIPT_NUM_TYPE | POSystemParametersManualReceiptNumType | — |
| MANUAL_REQ_NUM_TYPE | POSystemParametersManualReqNumType | — |
| MATCH_OPTION | POSystemParametersMatchOption | — |
| MAX_ATTACHMENT_SIZE | POSystemParametersMaxAttachmentSize | — |
| MIN_RELEASE_AMOUNT | POSystemParametersMinReleaseAmount | — |
| MODE_OF_TRANSPORT | POSystemParametersModeOfTransport | — |
| NEXT_APPROVER_LOOKUP_CODE | POSystemParametersNextApproverLookupCode | — |
| NEXT_NEGOTIATION_NUMBER | POSystemParametersNextNegotiationNumber | — |
| OBJECT_VERSION_NUMBER | POSystemParametersObjectVersionNumber | — |
| PRC_BU_ID | POSystemParametersPrcBuId | — |
| PRICE_BREAK_LOOKUP_CODE | POSystemParametersPriceBreakLookupCode | — |
| PRICE_CHANGE_AMOUNT | POSystemParametersPriceChangeAmount | — |
| RANK_INDICATOR | POSystemParametersRankIndicator | — |
| RANK_VISIBLE_BLIND | POSystemParametersRankVisibleBlind | — |
| RECEIVE_CLOSE_CODE | POSystemParametersReceiveCloseCode | — |
| RECEIVE_CLOSE_TOLERANCE | POSystemParametersReceiveCloseTolerance | — |
| RECEIVING_FLAG | POSystemParametersReceivingFlag | — |
| RFQ_ONLY_SITE_FLAG | POSystemParametersRfqOnlySiteFlag | — |
| SERVICE_LEVEL | POSystemParametersServiceLevel | — |
| STYLE_ID | POSystemParametersStyleId | — |
| SUPPLIER_AUTHORING_ACCEPTANCE | POSystemParametersSupplierAuthoringAcceptance | — |
| SUPPLIER_HISTORY_DURATION | POSystemParametersSupplierHistoryDuration | — |
| TAX_FROM_ITEM_FLAG | POSystemParametersTaxFromItemFlag | — |
| TAX_FROM_SHIP_TO_LOC_FLAG | POSystemParametersTaxFromShipToLocFlag | — |
| TAX_FROM_SYSTEM_FLAG | POSystemParametersTaxFromSystemFlag | — |
| TAX_FROM_VENDOR_FLAG | POSystemParametersTaxFromVendorFlag | — |
| TAX_FROM_VENDOR_SITE_FLAG | POSystemParametersTaxFromVendorSiteFlag | — |
| TAX_HIER_ITEM | POSystemParametersTaxHierItem | — |
| TAX_HIER_SHIP_TO_LOC | POSystemParametersTaxHierShipToLoc | — |
| TAX_HIER_SYSTEM | POSystemParametersTaxHierSystem | — |
| TAX_HIER_VENDOR | POSystemParametersTaxHierVendor | — |
| TAX_HIER_VENDOR_SITE | POSystemParametersTaxHierVendorSite | — |
| TAXABLE_FLAG | POSystemParametersTaxableFlag | — |
| TERMS_ID | POSystemParametersTermsId | — |
| USE_NEED_BY_DATE | POSystemParametersUseNeedByDate | — |
| USE_SHIP_TO | POSystemParametersUseShipTo | — |
| USER_DEFINED_RECEIPT_NUM_CODE | POSystemParametersUserDefinedReceiptNumCode | — |
| USER_DEFINED_REQ_NUM_CODE | POSystemParametersUserDefinedReqNumCode | — |

### [[standardshipmentpvo|StandardShipmentPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_ITEM_DESC_UPDATE_FLAG | POSystemParametersAllowItemDescUpdateFlag | — |
| ALLOW_RETRO_PRICING | POSystemParametersAllowRetroPricing | — |
| BEST_PRICE_VISIBLE_BLIND | POSystemParametersBestPriceVisibleBlind | — |
| CARRIER_ID | POSystemParametersCarrierId | — |
| CAT_ADMIN_AUTHORING_ACCEPTANCE | POSystemParametersCatAdminAuthoringAcceptance | — |
| COLLAB_SECURITY_PROFILE_ID | POSystemParametersCollabSecurityProfileId | — |
| CREATE_DEBIT_MEMO_FLAG | POSystemParametersCreateDebitMemoFlag | — |
| CURRENCY_CODE | POSystemParametersCurrencyCode | — |
| DEFAULT_PROMISE_DATE | POSystemParametersDefaultPromiseDate | — |
| DEFAULT_RATE_TYPE | POSystemParametersDefaultRateType | — |
| DOCTYPE_ID | POSystemParametersDoctypeId | — |
| EMAIL_ATTACHMENT_FILENAME | POSystemParametersEmailAttachmentFilename | — |
| ENFORCE_BUYER_AUTHORITY_FLAG | POSystemParametersEnforceBuyerAuthorityFlag | — |
| ENFORCE_MIN_BID_PRICE | POSystemParametersEnforceMinBidPrice | — |
| ENFORCE_VENDOR_HOLD_FLAG | POSystemParametersEnforceVendorHoldFlag | — |
| FOB_LOOKUP_CODE | POSystemParametersFobLookupCode | — |
| FREIGHT_TERMS_LOOKUP_CODE | POSystemParametersFreightTermsLookupCode | — |
| GROUP_REQUISITION_LINES | POSystemParametersGroupRequisitionLines | — |
| GROUP_REQUISITIONS | POSystemParametersGroupRequisitions | — |
| HDR_ATTR_DEFAULT_MAX_SCORE | POSystemParametersHdrAttrDefaultMaxScore | — |
| HDR_ATTR_DISP_SCORE_CRITERIA | POSystemParametersHdrAttrDispScoreCriteria | — |
| HDR_ATTR_ENABLE_WEIGHTS | POSystemParametersHdrAttrEnableWeights | — |
| INSPECTION_REQUIRED_FLAG | POSystemParametersInspectionRequiredFlag | — |
| INVENTORY_ORGANIZATION_ID | POSystemParametersInventoryOrganizationId | — |
| INVOICE_CLOSE_CODE | POSystemParametersInvoiceCloseCode | — |
| INVOICE_CLOSE_TOLERANCE | POSystemParametersInvoiceCloseTolerance | — |
| LANGUAGE_CODE | POSystemParametersLanguageCode | — |
| LINE_TYPE_ID | POSystemParametersLineTypeId | — |
| MANUAL_RECEIPT_NUM_TYPE | POSystemParametersManualReceiptNumType | — |
| MANUAL_REQ_NUM_TYPE | POSystemParametersManualReqNumType | — |
| MATCH_OPTION | POSystemParametersMatchOption | — |
| MAX_ATTACHMENT_SIZE | POSystemParametersMaxAttachmentSize | — |
| MIN_RELEASE_AMOUNT | POSystemParametersMinReleaseAmount | — |
| MODE_OF_TRANSPORT | POSystemParametersModeOfTransport | — |
| NEXT_APPROVER_LOOKUP_CODE | POSystemParametersNextApproverLookupCode | — |
| NEXT_NEGOTIATION_NUMBER | POSystemParametersNextNegotiationNumber | — |
| PRC_BU_ID | POSystemParametersPrcBuId | — |
| PRICE_BREAK_LOOKUP_CODE | POSystemParametersPriceBreakLookupCode | — |
| PRICE_CHANGE_AMOUNT | POSystemParametersPriceChangeAmount | — |
| RANK_INDICATOR | POSystemParametersRankIndicator | — |
| RANK_VISIBLE_BLIND | POSystemParametersRankVisibleBlind | — |
| RECEIVE_CLOSE_CODE | POSystemParametersReceiveCloseCode | — |
| RECEIVE_CLOSE_TOLERANCE | POSystemParametersReceiveCloseTolerance | — |
| RECEIVING_FLAG | POSystemParametersReceivingFlag | — |
| RFQ_ONLY_SITE_FLAG | POSystemParametersRfqOnlySiteFlag | — |
| SERVICE_LEVEL | POSystemParametersServiceLevel | — |
| STYLE_ID | POSystemParametersStyleId | — |
| SUPPLIER_AUTHORING_ACCEPTANCE | POSystemParametersSupplierAuthoringAcceptance | — |
| SUPPLIER_HISTORY_DURATION | POSystemParametersSupplierHistoryDuration | — |
| TAX_FROM_ITEM_FLAG | POSystemParametersTaxFromItemFlag | — |
| TAX_FROM_SHIP_TO_LOC_FLAG | POSystemParametersTaxFromShipToLocFlag | — |
| TAX_FROM_SYSTEM_FLAG | POSystemParametersTaxFromSystemFlag | — |
| TAX_FROM_VENDOR_FLAG | POSystemParametersTaxFromVendorFlag | — |
| TAX_FROM_VENDOR_SITE_FLAG | POSystemParametersTaxFromVendorSiteFlag | — |
| TAX_HIER_ITEM | POSystemParametersTaxHierItem | — |
| TAX_HIER_SHIP_TO_LOC | POSystemParametersTaxHierShipToLoc | — |
| TAX_HIER_SYSTEM | POSystemParametersTaxHierSystem | — |
| TAX_HIER_VENDOR | POSystemParametersTaxHierVendor | — |
| TAX_HIER_VENDOR_SITE | POSystemParametersTaxHierVendorSite | — |
| TAXABLE_FLAG | POSystemParametersTaxableFlag | — |
| TERMS_ID | POSystemParametersTermsId | — |
| USE_NEED_BY_DATE | POSystemParametersUseNeedByDate | — |
| USE_SHIP_TO | POSystemParametersUseShipTo | — |
| USER_DEFINED_RECEIPT_NUM_CODE | POSystemParametersUserDefinedReceiptNumCode | — |
| USER_DEFINED_REQ_NUM_CODE | POSystemParametersUserDefinedReqNumCode | — |

### [[unlockednegotiationresponselinepvo|UnlockedNegotiationResponseLinePVO]] (PO · BICC: 1/106)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGING_ONSET_POINT | AgingOnsetPoint | — |
| AGING_PERIOD_DAYS | AgingPeriodDays | — |
| ALLOW_ITEM_DESC_UPDATE_FLAG | AllowItemDescUpdateFlag | — |
| ALLOW_MANUL_PRICE_UPDATE_ORDER | AllowManulPriceUpdateOrder | — |
| ALLOW_RETRO_PRICING | AllowRetroPricing | — |
| AWARD_APPROVAL_ENABLED_FLAG | AwardApprovalEnabledFlag | — |
| BEST_PRICE_VISIBLE_BLIND | BestPriceVisibleBlind | — |
| BUYER_MANAGED_TRANSPORT_FLAG | BuyerManagedTransportFlag | — |
| CARRIER_ID | CarrierId | — |
| CAT_ADMIN_AUTHORING_ACCEPTANCE | CatAdminAuthoringAcceptance | — |
| COLLAB_SECURITY_PROFILE_ID | CollabSecurityProfileId | — |
| CONSUMPTION_ADVICE_FREQUENCY | ConsumptionAdviceFrequency | — |
| CONSUMPTION_ADVICE_SUMMARY | ConsumptionAdviceSummary | — |
| CREATE_DEBIT_MEMO_FLAG | CreateDebitMemoFlag | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| CURRENCY_CODE | CurrencyCode | — |
| DEFAULT_BUYER_ID | DefaultBuyerId | — |
| DEFAULT_PROMISE_DATE | DefaultPromiseDate | — |
| DEFAULT_RATE_TYPE | DefaultRateType | — |
| DOCTYPE_ID | DoctypeId | — |
| EMAIL_ATTACHMENT_FILENAME | EmailAttachmentFilename | — |
| ENFORCE_BUYER_AUTHORITY_FLAG | EnforceBuyerAuthorityFlag | — |
| ENFORCE_MIN_BID_PRICE | EnforceMinBidPrice | — |
| ENFORCE_VENDOR_HOLD_FLAG | EnforceVendorHoldFlag | — |
| FOB_LOOKUP_CODE | FobLookupCode | — |
| FREIGHT_TERMS_LOOKUP_CODE | FreightTermsLookupCode | — |
| GEN_ORDER_FOR_NEG_REQS_FLAG | GenOrderForNegReqsFlag | — |
| GLOBAL_ATTRIBUTE1 | GlobalAttribute1 | — |
| GLOBAL_ATTRIBUTE10 | GlobalAttribute10 | — |
| GLOBAL_ATTRIBUTE11 | GlobalAttribute11 | — |
| GLOBAL_ATTRIBUTE12 | GlobalAttribute12 | — |
| GLOBAL_ATTRIBUTE13 | GlobalAttribute13 | — |
| GLOBAL_ATTRIBUTE14 | GlobalAttribute14 | — |
| GLOBAL_ATTRIBUTE15 | GlobalAttribute15 | — |
| GLOBAL_ATTRIBUTE16 | GlobalAttribute16 | — |
| GLOBAL_ATTRIBUTE17 | GlobalAttribute17 | — |
| GLOBAL_ATTRIBUTE18 | GlobalAttribute18 | — |
| GLOBAL_ATTRIBUTE19 | GlobalAttribute19 | — |
| GLOBAL_ATTRIBUTE2 | GlobalAttribute2 | — |
| GLOBAL_ATTRIBUTE20 | GlobalAttribute20 | — |
| GLOBAL_ATTRIBUTE3 | GlobalAttribute3 | — |
| GLOBAL_ATTRIBUTE4 | GlobalAttribute4 | — |
| GLOBAL_ATTRIBUTE5 | GlobalAttribute5 | — |
| GLOBAL_ATTRIBUTE6 | GlobalAttribute6 | — |
| GLOBAL_ATTRIBUTE7 | GlobalAttribute7 | — |
| GLOBAL_ATTRIBUTE8 | GlobalAttribute8 | — |
| GLOBAL_ATTRIBUTE9 | GlobalAttribute9 | — |
| GLOBAL_ATTRIBUTE_CATEGORY | GlobalAttributeCategory | — |
| GROUP_REQUISITION_LINES | GroupRequisitionLines | — |
| GROUP_REQUISITIONS | GroupRequisitions | — |
| HDR_ATTR_DEFAULT_MAX_SCORE | HdrAttrDefaultMaxScore | — |
| HDR_ATTR_DISP_SCORE_CRITERIA | HdrAttrDispScoreCriteria | — |
| HDR_ATTR_ENABLE_WEIGHTS | HdrAttrEnableWeights | — |
| INSPECTION_REQUIRED_FLAG | InspectionRequiredFlag | — |
| INVENTORY_ORGANIZATION_ID | InventoryOrganizationId | — |
| INVENTORY_ORGANIZATION_ID | InventoryOrganizationId1 | — |
| INVOICE_CLOSE_CODE | InvoiceCloseCode | — |
| INVOICE_CLOSE_TOLERANCE | InvoiceCloseTolerance | — |
| LANGUAGE_CODE | LanguageCode | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| LINE_TYPE_ID | LineTypeId | — |
| MANUAL_RECEIPT_NUM_TYPE | ManualReceiptNumType | — |
| MANUAL_REQ_NUM_TYPE | ManualReqNumType | — |
| MATCH_OPTION | MatchOption | — |
| MAX_ATTACHMENT_SIZE | MaxAttachmentSize | — |
| MIN_RELEASE_AMOUNT | MinReleaseAmount | — |
| MODE_OF_TRANSPORT | ModeOfTransport1 | — |
| NEG_APPROVAL_ENABLED_FLAG | NegApprovalEnabledFlag | — |
| NEXT_APPROVER_LOOKUP_CODE | NextApproverLookupCode | — |
| NEXT_NEGOTIATION_NUMBER | NextNegotiationNumber | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PRC_BU_ID | PrcBuId | — |
| PRC_BU_ID | PrcBuId1 | — |
| PRICE_BREAK_LOOKUP_CODE | PriceBreakLookupCode | — |
| PRICE_CHANGE_AMOUNT | PriceChangeAmount | — |
| RANK_INDICATOR | RankIndicator | — |
| RANK_VISIBLE_BLIND | RankVisibleBlind | — |
| RECEIVE_CLOSE_CODE | ReceiveCloseCode | — |
| RECEIVE_CLOSE_TOLERANCE | ReceiveCloseTolerance | — |
| RECEIVING_FLAG | ReceivingFlag | — |
| RFQ_ONLY_SITE_FLAG | RfqOnlySiteFlag | — |
| SERVICE_LEVEL | ServiceLevel1 | — |
| STYLE_ID | StyleId | — |
| SUPPLIER_AUTHORING_ACCEPTANCE | SupplierAuthoringAcceptance | — |
| SUPPLIER_HISTORY_DURATION | SupplierHistoryDuration | — |
| SYSTEM_CONFIGURED_FLAG | SystemConfiguredFlag | — |
| TAX_FROM_ITEM_FLAG | TaxFromItemFlag | — |
| TAX_FROM_SHIP_TO_LOC_FLAG | TaxFromShipToLocFlag | — |
| TAX_FROM_SYSTEM_FLAG | TaxFromSystemFlag | — |
| TAX_FROM_VENDOR_FLAG | TaxFromVendorFlag | — |
| TAX_FROM_VENDOR_SITE_FLAG | TaxFromVendorSiteFlag | — |
| TAX_HIER_ITEM | TaxHierItem | — |
| TAX_HIER_SHIP_TO_LOC | TaxHierShipToLoc | — |
| TAX_HIER_SYSTEM | TaxHierSystem | — |
| TAX_HIER_VENDOR | TaxHierVendor | — |
| TAX_HIER_VENDOR_SITE | TaxHierVendorSite | — |
| TAXABLE_FLAG | TaxableFlag | — |
| TERMS_ID | TermsId | — |
| USE_NEED_BY_DATE | UseNeedByDate | — |
| USE_SALES_ORDER_NUMBER_FLAG | UseSalesOrderNumberFlag | — |
| USE_SHIP_TO | UseShipTo | — |
| USER_DEFINED_RECEIPT_NUM_CODE | UserDefinedReceiptNumCode | — |
| USER_DEFINED_REQ_NUM_CODE | UserDefinedReqNumCode | — |

---

## 📚 Referências

- [Oracle Docs — PO_SYSTEM_PARAMETERS_ALL](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/posystemparametersall-10213.html)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
