---
id: DOC-OTHER-PVO-CstTransactionTypesExtractPVO
doc_type: system-doc
title: "CstTransactionTypesExtractPVO — PVO Cross-Module"
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
  - CstTransactionTypesExtractPVO
  - csttransactiontypesextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstTransactionTypesExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Transaction Types Extract. Acessa as tabelas: CST_TXN_SOURCE_ACTIONS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstTransactionTypesExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 43 | 1 | 2 | 43 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_txn_source_actions|CST_TXN_SOURCE_ACTIONS]] — 43 atributos (2 PKs, 43 BICC)

---

## ⚙️ Atributos

### [[cst_txn_source_actions|CST_TXN_SOURCE_ACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstTransactionTypesPEOAcqCostParentFlag | ACQ_COST_PARENT_FLAG | — | ✅ |
| 2 | CstTransactionTypesPEOAdditionalProcessingCode | ADDITIONAL_PROCESSING_CODE | — | ✅ |
| 3 | CstTransactionTypesPEOBaseTxnActionId | BASE_TXN_ACTION_ID | 🔑 | ✅ |
| 4 | CstTransactionTypesPEOBaseTxnSourceTypeId | BASE_TXN_SOURCE_TYPE_ID | 🔑 | ✅ |
| 5 | CstTransactionTypesPEOCheckQtySignFlag | CHECK_QTY_SIGN_FLAG | — | ✅ |
| 6 | CstTransactionTypesPEOCheckWithSfoFlag | CHECK_WITH_SFO_FLAG | — | ✅ |
| 7 | CstTransactionTypesPEOCogsRecognitionFlag | COGS_RECOGNITION_FLAG | — | ✅ |
| 8 | CstTransactionTypesPEOCompareVuStrLevel | COMPARE_VU_STR_LEVEL | — | ✅ |
| 9 | CstTransactionTypesPEOConsignedTfrToInvIndicator | CONSIGNED_TFR_TO_INV_INDICATOR | — | ✅ |
| 10 | CstTransactionTypesPEOCostPreprocessingFlag | COST_PREPROCESSING_FLAG | — | ✅ |
| 11 | CstTransactionTypesPEOCostTransactionType | COST_TRANSACTION_TYPE | — | ✅ |
| 12 | CstTransactionTypesPEOCreateIssueTxnAction | CREATE_ISSUE_TXN_ACTION | — | ✅ |
| 13 | CstTransactionTypesPEOCreateIssueTxnSourceType | CREATE_ISSUE_TXN_SOURCE_TYPE | — | ✅ |
| 14 | CstTransactionTypesPEOCreateReceiptTxnAction | CREATE_RECEIPT_TXN_ACTION | — | ✅ |
| 15 | CstTransactionTypesPEOCreateReceiptTxnSourceType | CREATE_RECEIPT_TXN_SOURCE_TYPE | — | ✅ |
| 16 | CstTransactionTypesPEOCreateTxnFlag | CREATE_TXN_FLAG | — | ✅ |
| 17 | CstTransactionTypesPEOCreatedBy | CREATED_BY | — | ✅ |
| 18 | CstTransactionTypesPEOCreationDate | CREATION_DATE | — | ✅ |
| 19 | CstTransactionTypesPEODirectInterfaceCostFlag | DIRECT_INTERFACE_COST_FLAG | — | ✅ |
| 20 | CstTransactionTypesPEOEndDate | END_DATE | — | ✅ |
| 21 | CstTransactionTypesPEOExternalTxnType | EXTERNAL_TXN_TYPE | — | ✅ |
| 22 | CstTransactionTypesPEOGpFwdFlowInvOrgType | GP_FWD_FLOW_INV_ORG_TYPE | — | ✅ |
| 23 | CstTransactionTypesPEOGpFwdFlowRcvParent | GP_FWD_FLOW_RCV_PARENT | — | ✅ |
| 24 | CstTransactionTypesPEOGpMapToXferGroup | GP_MAP_TO_XFER_GROUP | — | ✅ |
| 25 | CstTransactionTypesPEOGpXferGroup | GP_XFER_GROUP | — | ✅ |
| 26 | CstTransactionTypesPEOInactiveFlag | INACTIVE_FLAG | — | ✅ |
| 27 | CstTransactionTypesPEOIntransitFlag | INTRANSIT_FLAG | — | ✅ |
| 28 | CstTransactionTypesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 29 | CstTransactionTypesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 30 | CstTransactionTypesPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 31 | CstTransactionTypesPEOLeEnabledFlag | LE_ENABLED_FLAG | — | ✅ |
| 32 | CstTransactionTypesPEOLogicalAcqCostFlag | LOGICAL_ACQ_COST_FLAG | — | ✅ |
| 33 | CstTransactionTypesPEOLogicalFlag | LOGICAL_FLAG | — | ✅ |
| 34 | CstTransactionTypesPEOMiscInterfaceCostFlag | MISC_INTERFACE_COST_FLAG | — | ✅ |
| 35 | CstTransactionTypesPEOPhysicalAcqCostFlag | PHYSICAL_ACQ_COST_FLAG | — | ✅ |
| 36 | CstTransactionTypesPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 37 | CstTransactionTypesPEOSfoAcqCostFlag | SFO_ACQ_COST_FLAG | — | ✅ |
| 38 | CstTransactionTypesPEOSfoEventCostInterfaceFlag | SFO_EVENT_COST_INTERFACE_FLAG | — | ✅ |
| 39 | CstTransactionTypesPEOSingleLegTransferSign | SINGLE_LEG_TRANSFER_SIGN | — | ✅ |
| 40 | CstTransactionTypesPEOStartDate | START_DATE | — | ✅ |
| 41 | CstTransactionTypesPEOTransactionFlowType | TRANSACTION_FLOW_TYPE | — | ✅ |
| 42 | CstTransactionTypesPEOTransferShipRcptCoeval | TRANSFER_SHIP_RCPT_COEVAL | — | ✅ |
| 43 | CstTransactionTypesPEOWipCostFlag | WIP_COST_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
