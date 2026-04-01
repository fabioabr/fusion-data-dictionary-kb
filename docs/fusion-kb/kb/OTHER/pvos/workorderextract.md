---
id: DOC-OTHER-PVO-WorkOrderExtract
doc_type: system-doc
title: "WorkOrderExtract — PVO Cross-Module"
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
  - WorkOrderExtract
  - workorderextract
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WorkOrderExtract

## 📌 Visão Geral

View Object para extração BICC de dados de Work Order Extract. Acessa as tabelas: MNT_WORK_ORDERS_EXT.

**Caminho:** `FscmTopModelAM.MaintProgramAM.WorkOrderExtract`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 68 | 1 | 1 | 3 | 4% |

---

## 🔗 Tabelas Relacionadas

- [[mnt_work_orders_ext|MNT_WORK_ORDERS_EXT]] — 68 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[mnt_work_orders_ext|MNT_WORK_ORDERS_EXT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActualCompletionDate | ACTUAL_COMPLETION_DATE | — | — |
| 2 | ActualStartDate | ACTUAL_START_DATE | — | — |
| 3 | AssetFailureFlag | ASSET_FAILURE_FLAG | — | — |
| 4 | AssetId | ASSET_ID | — | — |
| 5 | AssetNumber | ASSET_NUMBER | — | — |
| 6 | AssetTbf | ASSET_TBF | — | — |
| 7 | AssetUbf | ASSET_UBF | — | — |
| 8 | CanceledDate | CANCELED_DATE | — | — |
| 9 | CanceledReason | CANCELED_REASON | — | — |
| 10 | ClosedDate | CLOSED_DATE | — | — |
| 11 | CreatedBy | CREATED_BY | — | — |
| 12 | CreationDate | CREATION_DATE | — | — |
| 13 | DailyUtilizationRate | DAILY_UTILIZATION_RATE | — | — |
| 14 | DataRowId | DATA_ROW_ID | 🔑 | ✅ |
| 15 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 16 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 17 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 18 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 19 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 20 | MaterialItemId | MATERIAL_ITEM_ID | — | — |
| 21 | MaterialItemNumber | MATERIAL_ITEM_NUMBER | — | — |
| 22 | MaterialQuantity | MATERIAL_QUANTITY | — | — |
| 23 | MaterialSeqNumber | MATERIAL_SEQ_NUMBER | — | — |
| 24 | MaterialTtf | MATERIAL_TTF | — | — |
| 25 | MaterialUomCode | MATERIAL_UOM_CODE | — | — |
| 26 | MaterialUtf | MATERIAL_UTF | — | — |
| 27 | MeterDefinitionId | METER_DEFINITION_ID | — | — |
| 28 | MeterId | METER_ID | — | — |
| 29 | MeterName | METER_NAME | — | — |
| 30 | MeterUomCode | METER_UOM_CODE | — | — |
| 31 | MntForecastId | MNT_FORECAST_ID | — | — |
| 32 | NetValue | NET_VALUE | — | — |
| 33 | OrganizationCode | ORGANIZATION_CODE | — | — |
| 34 | OrganizationId | ORGANIZATION_ID | — | ✅ |
| 35 | PartFailureFlag | PART_FAILURE_FLAG | — | — |
| 36 | PlannedCompletionDate | PLANNED_COMPLETION_DATE | — | — |
| 37 | PlannedStartDate | PLANNED_START_DATE | — | — |
| 38 | ProgramCode | PROGRAM_CODE | — | — |
| 39 | ProgramId | PROGRAM_ID | — | — |
| 40 | ProgramName | PROGRAM_NAME | — | — |
| 41 | ReadingDate | READING_DATE | — | — |
| 42 | ReadingValue | READING_VALUE | — | — |
| 43 | ReleasedDate | RELEASED_DATE | — | — |
| 44 | RequestId | REQUEST_ID | — | — |
| 45 | RequirementId | REQUIREMENT_ID | — | — |
| 46 | RequirementName | REQUIREMENT_NAME | — | — |
| 47 | RunId | RUN_ID | — | — |
| 48 | UnplannedWoFlag | UNPLANNED_WO_FLAG | — | — |
| 49 | WoItemId | WO_ITEM_ID | — | — |
| 50 | WoItemNumber | WO_ITEM_NUMBER | — | — |
| 51 | WoOperationId | WO_OPERATION_ID | — | — |
| 52 | WoOperationMaterialId | WO_OPERATION_MATERIAL_ID | — | — |
| 53 | WoOperationName | WO_OPERATION_NAME | — | — |
| 54 | WoOperationSeqNumber | WO_OPERATION_SEQ_NUMBER | — | — |
| 55 | WorkCenterCode | WORK_CENTER_CODE | — | — |
| 56 | WorkCenterId | WORK_CENTER_ID | — | — |
| 57 | WorkCenterName | WORK_CENTER_NAME | — | — |
| 58 | WorkDefinitionCode | WORK_DEFINITION_CODE | — | — |
| 59 | WorkDefinitionId | WORK_DEFINITION_ID | — | — |
| 60 | WorkDefinitionName | WORK_DEFINITION_NAME | — | — |
| 61 | WorkDefinitionVersionId | WORK_DEFINITION_VERSION_ID | — | — |
| 62 | WorkOrderCost | WORK_ORDER_COST | — | — |
| 63 | WorkOrderId | WORK_ORDER_ID | — | — |
| 64 | WorkOrderNumber | WORK_ORDER_NUMBER | — | — |
| 65 | WorkOrderOvn | WORK_ORDER_OVN | — | — |
| 66 | WorkOrderStatusId | WORK_ORDER_STATUS_ID | — | — |
| 67 | WorkOrderSubType | WORK_ORDER_SUB_TYPE | — | — |
| 68 | WorkOrderType | WORK_ORDER_TYPE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
