---
id: DOC-OTHER-PVO-InventoryOrgParametersPVO
doc_type: system-doc
title: "InventoryOrgParametersPVO — PVO Cross-Module"
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
  - InventoryOrgParametersPVO
  - inventoryorgparameterspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InventoryOrgParametersPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Inventory Org Parameters. Acessa as tabelas: INV_ORG_PARAMETERS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.ScmRcsBiccExtractAM.InventoryOrgParametersPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 64 | 1 | 1 | 64 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[inv_org_parameters|INV_ORG_PARAMETERS]] — 64 atributos (1 PKs, 64 BICC)

---

## ⚙️ Atributos

### [[inv_org_parameters|INV_ORG_PARAMETERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrganizationId | ORGANIZATION_ID | 🔑 | ✅ |
| 2 | OrganizationParameterPEOAllocateSerialFlag | ALLOCATE_SERIAL_FLAG | — | ✅ |
| 3 | OrganizationParameterPEOAllowDifferentStatus | ALLOW_DIFFERENT_STATUS | — | ✅ |
| 4 | OrganizationParameterPEOAllowNegOnhandCcTxns | ALLOW_NEG_ONHAND_CC_TXNS | — | ✅ |
| 5 | OrganizationParameterPEOAutoDelAllocFlag | AUTO_DEL_ALLOC_FLAG | — | ✅ |
| 6 | OrganizationParameterPEOAutoLotAlphaPrefix | AUTO_LOT_ALPHA_PREFIX | — | ✅ |
| 7 | OrganizationParameterPEOAutoSerialAlphaPrefix | AUTO_SERIAL_ALPHA_PREFIX | — | ✅ |
| 8 | OrganizationParameterPEOBusinessUnitId | BUSINESS_UNIT_ID | — | ✅ |
| 9 | OrganizationParameterPEOChildLotAlphaPrefix | CHILD_LOT_ALPHA_PREFIX | — | ✅ |
| 10 | OrganizationParameterPEOChildLotNumberLength | CHILD_LOT_NUMBER_LENGTH | — | ✅ |
| 11 | OrganizationParameterPEOChildLotValidationFlag | CHILD_LOT_VALIDATION_FLAG | — | ✅ |
| 12 | OrganizationParameterPEOChildLotZeroPaddingFlag | CHILD_LOT_ZERO_PADDING_FLAG | — | ✅ |
| 13 | OrganizationParameterPEOContractMfgFlag | CONTRACT_MFG_FLAG | — | ✅ |
| 14 | OrganizationParameterPEOCopyLotAttributeFlag | COPY_LOT_ATTRIBUTE_FLAG | — | ✅ |
| 15 | OrganizationParameterPEOCreateLotUomConversion | CREATE_LOT_UOM_CONVERSION | — | ✅ |
| 16 | OrganizationParameterPEOCreatedBy | CREATED_BY | — | ✅ |
| 17 | OrganizationParameterPEOCreationDate | CREATION_DATE | — | ✅ |
| 18 | OrganizationParameterPEODefaultLocatorOrderValue | DEFAULT_LOCATOR_ORDER_VALUE | — | ✅ |
| 19 | OrganizationParameterPEODefaultPickingRuleId | DEFAULT_PICKING_RULE_ID | — | ✅ |
| 20 | OrganizationParameterPEODefaultSubinvOrderValue | DEFAULT_SUBINV_ORDER_VALUE | — | ✅ |
| 21 | OrganizationParameterPEODistributedOrganizationFlag | DISTRIBUTED_ORGANIZATION_FLAG | — | ✅ |
| 22 | OrganizationParameterPEOEnforceLocatorAlisUnqFlag | ENFORCE_LOCATOR_ALIS_UNQ_FLAG | — | ✅ |
| 23 | OrganizationParameterPEOFifoOrigRcptDateFlag | FIFO_ORIG_RCPT_DATE_FLAG | — | ✅ |
| 24 | OrganizationParameterPEOFillKillMoveOrderFlag | FILL_KILL_MOVE_ORDER_FLAG | — | ✅ |
| 25 | OrganizationParameterPEOInventoryFlag | INVENTORY_FLAG | — | ✅ |
| 26 | OrganizationParameterPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 27 | OrganizationParameterPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 28 | OrganizationParameterPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 29 | OrganizationParameterPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 30 | OrganizationParameterPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 31 | OrganizationParameterPEOLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 32 | OrganizationParameterPEOLotNumberGeneration | LOT_NUMBER_GENERATION | — | ✅ |
| 33 | OrganizationParameterPEOLotNumberLength | LOT_NUMBER_LENGTH | — | ✅ |
| 34 | OrganizationParameterPEOLotNumberUniqueness | LOT_NUMBER_UNIQUENESS | — | ✅ |
| 35 | OrganizationParameterPEOLotNumberZeroPadding | LOT_NUMBER_ZERO_PADDING | — | ✅ |
| 36 | OrganizationParameterPEOLpnPrefix | LPN_PREFIX | — | ✅ |
| 37 | OrganizationParameterPEOLpnStartingNumber | LPN_STARTING_NUMBER | — | ✅ |
| 38 | OrganizationParameterPEOLpnSuffix | LPN_SUFFIX | — | ✅ |
| 39 | OrganizationParameterPEOMasterOrganizationId | MASTER_ORGANIZATION_ID | — | ✅ |
| 40 | OrganizationParameterPEOMfgPlantFlag | MFG_PLANT_FLAG | — | ✅ |
| 41 | OrganizationParameterPEOMoPickConfirmRequired | MO_PICK_CONFIRM_REQUIRED | — | ✅ |
| 42 | OrganizationParameterPEONegativeInvReceiptCode | NEGATIVE_INV_RECEIPT_CODE | — | ✅ |
| 43 | OrganizationParameterPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 44 | OrganizationParameterPEOOrganizationCode | ORGANIZATION_CODE | — | ✅ |
| 45 | OrganizationParameterPEOOvpkTransferOrdersEnabled | OVPK_TRANSFER_ORDERS_ENABLED | — | ✅ |
| 46 | OrganizationParameterPEOParentChildGenerationFlag | PARENT_CHILD_GENERATION_FLAG | — | ✅ |
| 47 | OrganizationParameterPEOPickSlipBatchSize | PICK_SLIP_BATCH_SIZE | — | ✅ |
| 48 | OrganizationParameterPEOPurchasingByRevision | PURCHASING_BY_REVISION | — | ✅ |
| 49 | OrganizationParameterPEOReplnshMoveOrderGrouping | REPLNSH_MOVE_ORDER_GROUPING | — | ✅ |
| 50 | OrganizationParameterPEORequestId | REQUEST_ID | — | ✅ |
| 51 | OrganizationParameterPEORoundReorderQtyFlag | ROUND_REORDER_QTY_FLAG | — | ✅ |
| 52 | OrganizationParameterPEOScheduleId | SCHEDULE_ID | — | ✅ |
| 53 | OrganizationParameterPEOSerialNumberGeneration | SERIAL_NUMBER_GENERATION | — | ✅ |
| 54 | OrganizationParameterPEOSerialNumberType | SERIAL_NUMBER_TYPE | — | ✅ |
| 55 | OrganizationParameterPEOSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | ✅ |
| 56 | OrganizationParameterPEOSourceSubinventory | SOURCE_SUBINVENTORY | — | ✅ |
| 57 | OrganizationParameterPEOSourceType | SOURCE_TYPE | — | ✅ |
| 58 | OrganizationParameterPEOStartAutoSerialNumber | START_AUTO_SERIAL_NUMBER | — | ✅ |
| 59 | OrganizationParameterPEOStartingRevision | STARTING_REVISION | — | ✅ |
| 60 | OrganizationParameterPEOStockLocatorControlCode | STOCK_LOCATOR_CONTROL_CODE | — | ✅ |
| 61 | OrganizationParameterPEOSupplierId | SUPPLIER_ID | — | ✅ |
| 62 | OrganizationParameterPEOSupplierSiteId | SUPPLIER_SITE_ID | — | ✅ |
| 63 | OrganizationParameterPEOTotalLpnLength | TOTAL_LPN_LENGTH | — | ✅ |
| 64 | OrganizationParameterPEOUcc128SuffixFlag | UCC_128_SUFFIX_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
