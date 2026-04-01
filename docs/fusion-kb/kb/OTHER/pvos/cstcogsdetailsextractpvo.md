---
id: DOC-OTHER-PVO-CstCogsDetailsExtractPVO
doc_type: system-doc
title: "CstCogsDetailsExtractPVO — PVO Cross-Module"
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
  - CstCogsDetailsExtractPVO
  - cstcogsdetailsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstCogsDetailsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Cogs Details Extract. Acessa as tabelas: CST_COGS_DETAILS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstCogsDetailsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 48 | 1 | 1 | 48 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_cogs_details|CST_COGS_DETAILS]] — 48 atributos (1 PKs, 48 BICC)

---

## ⚙️ Atributos

### [[cst_cogs_details|CST_COGS_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstCogsDetailsPEOAccountedFlag | ACCOUNTED_FLAG | — | ✅ |
| 2 | CstCogsDetailsPEOAccountingLineType | ACCOUNTING_LINE_TYPE | — | ✅ |
| 3 | CstCogsDetailsPEOAgreementNumber | AGREEMENT_NUMBER | — | ✅ |
| 4 | CstCogsDetailsPEOBaseCurrencyCode | BASE_CURRENCY_CODE | — | ✅ |
| 5 | CstCogsDetailsPEOBaseTxnActionId | BASE_TXN_ACTION_ID | — | ✅ |
| 6 | CstCogsDetailsPEOBaseTxnSourceTypeId | BASE_TXN_SOURCE_TYPE_ID | — | ✅ |
| 7 | CstCogsDetailsPEOBaseTxnTypeId | BASE_TXN_TYPE_ID | — | ✅ |
| 8 | CstCogsDetailsPEOCogsAccountId | COGS_ACCOUNT_ID | — | ✅ |
| 9 | CstCogsDetailsPEOCogsAmount | COGS_AMOUNT | — | ✅ |
| 10 | CstCogsDetailsPEOCogsDetailId | COGS_DETAIL_ID | 🔑 | ✅ |
| 11 | CstCogsDetailsPEOCogsType | COGS_TYPE | — | ✅ |
| 12 | CstCogsDetailsPEOConfigInventoryItemId | CONFIG_INVENTORY_ITEM_ID | — | ✅ |
| 13 | CstCogsDetailsPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 14 | CstCogsDetailsPEOCostElementId | COST_ELEMENT_ID | — | ✅ |
| 15 | CstCogsDetailsPEOCostElementType | COST_ELEMENT_TYPE | — | ✅ |
| 16 | CstCogsDetailsPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 17 | CstCogsDetailsPEOCostTransactionUom | COST_TRANSACTION_UOM | — | ✅ |
| 18 | CstCogsDetailsPEOCreatedBy | CREATED_BY | — | ✅ |
| 19 | CstCogsDetailsPEOCreationDate | CREATION_DATE | — | ✅ |
| 20 | CstCogsDetailsPEOCtDooFullfillLineId | CT_DOO_FULLFILL_LINE_ID | — | ✅ |
| 21 | CstCogsDetailsPEOCustomerId | CUSTOMER_ID | — | ✅ |
| 22 | CstCogsDetailsPEODcogsAmount | DCOGS_AMOUNT | — | ✅ |
| 23 | CstCogsDetailsPEODistributionId | DISTRIBUTION_ID | — | ✅ |
| 24 | CstCogsDetailsPEODistributionLineId | DISTRIBUTION_LINE_ID | — | ✅ |
| 25 | CstCogsDetailsPEODooFullfillLineId | DOO_FULLFILL_LINE_ID | — | ✅ |
| 26 | CstCogsDetailsPEODooOrderNumber | DOO_ORDER_NUMBER | — | ✅ |
| 27 | CstCogsDetailsPEODooOrderType | DOO_ORDER_TYPE | — | ✅ |
| 28 | CstCogsDetailsPEOEventId | EVENT_ID | — | ✅ |
| 29 | CstCogsDetailsPEOFlowInstanceId | FLOW_INSTANCE_ID | — | ✅ |
| 30 | CstCogsDetailsPEOGlDate | GL_DATE | — | ✅ |
| 31 | CstCogsDetailsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 32 | CstCogsDetailsPEOInventoryOrgId | INVENTORY_ORG_ID | — | ✅ |
| 33 | CstCogsDetailsPEOItemOrganizationId | ITEM_ORGANIZATION_ID | — | ✅ |
| 34 | CstCogsDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 35 | CstCogsDetailsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 36 | CstCogsDetailsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 37 | CstCogsDetailsPEOLayerQuantity | LAYER_QUANTITY | — | ✅ |
| 38 | CstCogsDetailsPEOLedgerId | LEDGER_ID | — | ✅ |
| 39 | CstCogsDetailsPEOLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 40 | CstCogsDetailsPEOMarginCalcFlag | MARGIN_CALC_FLAG | — | ✅ |
| 41 | CstCogsDetailsPEOProfitCenterBuId | PROFIT_CENTER_BU_ID | — | ✅ |
| 42 | CstCogsDetailsPEORootInventoryItemId | ROOT_INVENTORY_ITEM_ID | — | ✅ |
| 43 | CstCogsDetailsPEOShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | ✅ |
| 44 | CstCogsDetailsPEOSourceDocNo | SOURCE_DOC_NO | — | ✅ |
| 45 | CstCogsDetailsPEOSourceDocType | SOURCE_DOC_TYPE | — | ✅ |
| 46 | CstCogsDetailsPEOSuccessorBuId | SUCCESSOR_BU_ID | — | ✅ |
| 47 | CstCogsDetailsPEOSuccessorInvOrgId | SUCCESSOR_INV_ORG_ID | — | ✅ |
| 48 | CstCogsDetailsPEOTxnInventoryItemId | TXN_INVENTORY_ITEM_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
