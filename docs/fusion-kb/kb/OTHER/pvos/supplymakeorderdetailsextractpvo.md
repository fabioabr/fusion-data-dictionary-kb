---
id: DOC-OTHER-PVO-SupplyMakeOrderDetailsExtractPVO
doc_type: system-doc
title: "SupplyMakeOrderDetailsExtractPVO — PVO Cross-Module"
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
  - SupplyMakeOrderDetailsExtractPVO
  - supplymakeorderdetailsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplyMakeOrderDetailsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Supply Make Order Details Extract. Acessa as tabelas: DOS_SUPPLY_MAKE_ORDER_DTLS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DosBiccExtractAM.SupplyMakeOrderDetailsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 46 | 1 | 1 | 46 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[dos_supply_make_order_dtls|DOS_SUPPLY_MAKE_ORDER_DTLS]] — 46 atributos (1 PKs, 46 BICC)

---

## ⚙️ Atributos

### [[dos_supply_make_order_dtls|DOS_SUPPLY_MAKE_ORDER_DTLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DosMakeOrderDetailsPEOAccountingClassCode | ACCOUNTING_CLASS_CODE | — | ✅ |
| 2 | DosMakeOrderDetailsPEOAllowExplosionFlag | ALLOW_EXPLOSION_FLAG | — | ✅ |
| 3 | DosMakeOrderDetailsPEOAltBomDesignator | ALT_BOM_DESIGNATOR | — | ✅ |
| 4 | DosMakeOrderDetailsPEOAltRoutingDesignator | ALT_ROUTING_DESIGNATOR | — | ✅ |
| 5 | DosMakeOrderDetailsPEOBomRevisionDate | BOM_REVISION_DATE | — | ✅ |
| 6 | DosMakeOrderDetailsPEOBuildSequence | BUILD_SEQUENCE | — | ✅ |
| 7 | DosMakeOrderDetailsPEOChangeSupplyOperation | CHANGE_SUPPLY_OPERATION | — | ✅ |
| 8 | DosMakeOrderDetailsPEOChargeAcctId | CHARGE_ACCT_ID | — | ✅ |
| 9 | DosMakeOrderDetailsPEOCreatedBy | CREATED_BY | — | ✅ |
| 10 | DosMakeOrderDetailsPEOCreationDate | CREATION_DATE | — | ✅ |
| 11 | DosMakeOrderDetailsPEODeliverToSubinventory | DELIVER_TO_SUBINVENTORY | — | ✅ |
| 12 | DosMakeOrderDetailsPEODemandClass | DEMAND_CLASS | — | ✅ |
| 13 | DosMakeOrderDetailsPEOExecSystemComplLoctrCode | EXEC_SYSTEM_COMPL_LOCTR_CODE | — | ✅ |
| 14 | DosMakeOrderDetailsPEOFirmPlannedFlag | FIRM_PLANNED_FLAG | — | ✅ |
| 15 | DosMakeOrderDetailsPEOGroupId | GROUP_ID | — | ✅ |
| 16 | DosMakeOrderDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | DosMakeOrderDetailsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 18 | DosMakeOrderDetailsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 19 | DosMakeOrderDetailsPEOLoadType | LOAD_TYPE | — | ✅ |
| 20 | DosMakeOrderDetailsPEONeedByDate | NEED_BY_DATE | — | ✅ |
| 21 | DosMakeOrderDetailsPEONetQuantity | NET_QUANTITY | — | ✅ |
| 22 | DosMakeOrderDetailsPEONetQuantityUomCode | NET_QUANTITY_UOM_CODE | — | ✅ |
| 23 | DosMakeOrderDetailsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 24 | DosMakeOrderDetailsPEOPrimaryDocQuantity | PRIMARY_DOC_QUANTITY | — | ✅ |
| 25 | DosMakeOrderDetailsPEOPrimaryDocQuantityUom | PRIMARY_DOC_QUANTITY_UOM | — | ✅ |
| 26 | DosMakeOrderDetailsPEORoutingRevisionDate | ROUTING_REVISION_DATE | — | ✅ |
| 27 | DosMakeOrderDetailsPEOScheduleGrpId | SCHEDULE_GRP_ID | — | ✅ |
| 28 | DosMakeOrderDetailsPEOSchedulingMethod | SCHEDULING_METHOD | — | ✅ |
| 29 | DosMakeOrderDetailsPEOSourceSystemId | SOURCE_SYSTEM_ID | — | ✅ |
| 30 | DosMakeOrderDetailsPEOSourceSystemType | SOURCE_SYSTEM_TYPE | — | ✅ |
| 31 | DosMakeOrderDetailsPEOSupplyMakeDetailsId | SUPPLY_MAKE_DETAILS_ID | 🔑 | ✅ |
| 32 | DosMakeOrderDetailsPEOTrackingLineId | TRACKING_LINE_ID | — | ✅ |
| 33 | DosMakeOrderDetailsPEOWipQty | WIP_QTY | — | ✅ |
| 34 | DosMakeOrderDetailsPEOWorkDefinitionAsOfDate | WORK_DEFINITION_AS_OF_DATE | — | ✅ |
| 35 | DosMakeOrderDetailsPEOWorkDefinitionId | WORK_DEFINITION_ID | — | ✅ |
| 36 | DosMakeOrderDetailsPEOWorkDefinitionName | WORK_DEFINITION_NAME | — | ✅ |
| 37 | DosMakeOrderDetailsPEOWorkMethodCode | WORK_METHOD_CODE | — | ✅ |
| 38 | DosMakeOrderDetailsPEOWorkOrderCompletionDate | WORK_ORDER_COMPLETION_DATE | — | ✅ |
| 39 | DosMakeOrderDetailsPEOWorkOrderDescription | WORK_ORDER_DESCRIPTION | — | ✅ |
| 40 | DosMakeOrderDetailsPEOWorkOrderId | WORK_ORDER_ID | — | ✅ |
| 41 | DosMakeOrderDetailsPEOWorkOrderNumber | WORK_ORDER_NUMBER | — | ✅ |
| 42 | DosMakeOrderDetailsPEOWorkOrderStartDate | WORK_ORDER_START_DATE | — | ✅ |
| 43 | DosMakeOrderDetailsPEOWorkOrderStatusId | WORK_ORDER_STATUS_ID | — | ✅ |
| 44 | DosMakeOrderDetailsPEOWorkOrderSubType | WORK_ORDER_SUB_TYPE | — | ✅ |
| 45 | DosMakeOrderDetailsPEOWorkOrderType | WORK_ORDER_TYPE | — | ✅ |
| 46 | DosMakeOrderDetailsPEOWorkProcessName | WORK_PROCESS_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
