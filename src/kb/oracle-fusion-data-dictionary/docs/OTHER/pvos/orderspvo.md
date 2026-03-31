---
id: DOC-OTHER-PVO-OrdersPVO
doc_type: system-doc
title: "OrdersPVO — PVO Cross-Module"
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
  - OrdersPVO
  - orderspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# OrdersPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Orders. Acessa as tabelas: MSC_ANALYTIC_FACT_ORD_V.

**Caminho:** `FscmTopModelAM.MscAnalyticsTopAM.OrdersPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 127 | 1 | 2 | 108 | 85% |

---

## 🔗 Tabelas Relacionadas

- [[msc_analytic_fact_ord_v|MSC_ANALYTIC_FACT_ORD_V]] — 127 atributos (2 PKs, 108 BICC)

---

## ⚙️ Atributos

### [[msc_analytic_fact_ord_v|MSC_ANALYTIC_FACT_ORD_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BasePlanId | BASE_PLAN_ID | — | — |
| 2 | OrderId | ORDER_ID | 🔑 | ✅ |
| 3 | OrdersPEOAction | ACTION | — | ✅ |
| 4 | OrdersPEOActualStartDate | ACTUAL_START_DATE | — | ✅ |
| 5 | OrdersPEOArrivalSetName | ARRIVAL_SET_NAME | — | ✅ |
| 6 | OrdersPEOBucketType | BUCKET_TYPE | — | ✅ |
| 7 | OrdersPEOBuyerManagedTrans | BUYER_MANAGED_TRANSPORTATION | — | ✅ |
| 8 | OrdersPEOClearToBldCompAvblty | CLEAR_TO_BLD_COMP_AVBLTY | — | ✅ |
| 9 | OrdersPEOClearToBuild | CLEAR_TO_BUILD | — | ✅ |
| 10 | OrdersPEOClearToBuildHorizon | CLEAR_TO_BUILD_HORIZON | — | ✅ |
| 11 | OrdersPEOCompressionDays | COMPRESSION_DAYS | — | ✅ |
| 12 | OrdersPEOCustomerId | CUSTOMER_ID | — | ✅ |
| 13 | OrdersPEOCustomerSiteId | CUSTOMER_SITE_ID | — | ✅ |
| 14 | OrdersPEODaysLate | DAYS_LATE | — | ✅ |
| 15 | OrdersPEODaysPastDue | DAYS_PAST_DUE | — | ✅ |
| 16 | OrdersPEODemandClass | DEMAND_CLASS | — | ✅ |
| 17 | OrdersPEODemandPriority | DEMAND_PRIORITY | — | — |
| 18 | OrdersPEODestinationType | DESTINATION_TYPE | — | ✅ |
| 19 | OrdersPEOEndDemandValue | END_DEMAND_VALUE | — | ✅ |
| 20 | OrdersPEOExpenseTransfer | EXPENSE_TRANSFER | — | ✅ |
| 21 | OrdersPEOExpirationDate | EXPIRATION_DATE | — | ✅ |
| 22 | OrdersPEOFirmDate | FIRM_DATE | — | ✅ |
| 23 | OrdersPEOFirmQuantity | FIRM_QUANTITY | — | ✅ |
| 24 | OrdersPEOFirmStatus | FIRM_STATUS | — | ✅ |
| 25 | OrdersPEOFulfillmentLine | FULFILLMENT_LINE | — | ✅ |
| 26 | OrdersPEOGlobalAttributeNumber11 | GLOBAL_ATTRIBUTE_NUMBER11 | — | — |
| 27 | OrdersPEOGlobalAttributeNumber12 | GLOBAL_ATTRIBUTE_NUMBER12 | — | — |
| 28 | OrdersPEOGlobalAttributeNumber13 | GLOBAL_ATTRIBUTE_NUMBER13 | — | — |
| 29 | OrdersPEOGlobalAttributeNumber14 | GLOBAL_ATTRIBUTE_NUMBER14 | — | — |
| 30 | OrdersPEOGlobalAttributeNumber15 | GLOBAL_ATTRIBUTE_NUMBER15 | — | — |
| 31 | OrdersPEOGlobalAttributeNumber16 | GLOBAL_ATTRIBUTE_NUMBER16 | — | — |
| 32 | OrdersPEOGlobalAttributeNumber17 | GLOBAL_ATTRIBUTE_NUMBER17 | — | — |
| 33 | OrdersPEOGlobalAttributeNumber18 | GLOBAL_ATTRIBUTE_NUMBER18 | — | — |
| 34 | OrdersPEOGlobalAttributeNumber19 | GLOBAL_ATTRIBUTE_NUMBER19 | — | — |
| 35 | OrdersPEOGlobalAttributeNumber20 | GLOBAL_ATTRIBUTE_NUMBER20 | — | — |
| 36 | OrdersPEOGlobalAttributeNumber21 | GLOBAL_ATTRIBUTE_NUMBER21 | — | — |
| 37 | OrdersPEOGlobalAttributeNumber22 | GLOBAL_ATTRIBUTE_NUMBER22 | — | — |
| 38 | OrdersPEOGlobalAttributeNumber23 | GLOBAL_ATTRIBUTE_NUMBER23 | — | — |
| 39 | OrdersPEOGlobalAttributeNumber24 | GLOBAL_ATTRIBUTE_NUMBER24 | — | — |
| 40 | OrdersPEOGlobalAttributeNumber25 | GLOBAL_ATTRIBUTE_NUMBER25 | — | — |
| 41 | OrdersPEOGlobalAttributeNumber26 | GLOBAL_ATTRIBUTE_NUMBER26 | — | — |
| 42 | OrdersPEOImplementDate | IMPLEMENT_DATE | — | ✅ |
| 43 | OrdersPEOImplementDockDate | IMPLEMENT_DOCK_DATE | — | ✅ |
| 44 | OrdersPEOImplementFirm | IMPLEMENT_FIRM | — | ✅ |
| 45 | OrdersPEOImplementItemStrucName | IMPLEMENT_ITEM_STRUCTURE_NAME | — | ✅ |
| 46 | OrdersPEOImplementOrderType | IMPLEMENT_ORDER_TYPE | — | ✅ |
| 47 | OrdersPEOImplementQuantity | IMPLEMENT_QUANTITY | — | ✅ |
| 48 | OrdersPEOImplementShipDate | IMPLEMENT_SHIP_DATE | — | ✅ |
| 49 | OrdersPEOImplementShippingMethod | IMPLEMENT_SHIPPING_METHOD | — | ✅ |
| 50 | OrdersPEOImplementSourceOrg | IMPLEMENT_SOURCE_ORGANIZATION | — | ✅ |
| 51 | OrdersPEOImplementStatus | IMPLEMENT_STATUS | — | ✅ |
| 52 | OrdersPEOImplementSupplier | IMPLEMENT_SUPPLIER | — | ✅ |
| 53 | OrdersPEOImplementSupplierSite | IMPLEMENT_SUPPLIER_SITE | — | ✅ |
| 54 | OrdersPEOImplementWorkDefinitionName | IMPLEMENT_WORK_DEFINITION_NAME | — | ✅ |
| 55 | OrdersPEOImplementWorkOrderSubtype | IMPLEMENT_WORK_ORDER_SUBTYPE | — | ✅ |
| 56 | OrdersPEOImplementedQuantity | IMPLEMENTED_QUANTITY | — | ✅ |
| 57 | OrdersPEOImplementedSupplyQuantity | IMPLEMENTED_SUPPLY_QUANTITY | — | ✅ |
| 58 | OrdersPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 59 | OrdersPEOItemStructureName | ITEM_STRUCTURE_NAME | — | ✅ |
| 60 | OrdersPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 61 | OrdersPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 62 | OrdersPEOLatestAcceptableDate | LATEST_ACCEPTABLE_DATE | — | ✅ |
| 63 | OrdersPEOLineNumber | LINE_NUMBER | — | ✅ |
| 64 | OrdersPEOLot | LOT | — | ✅ |
| 65 | OrdersPEOMaterialAvlblDate | MATERIAL_AVLBL_DATE | — | ✅ |
| 66 | OrdersPEONeedByDate | NEED_BY_DATE | — | ✅ |
| 67 | OrdersPEONettableSupQtyOverride | NETTABLE_SUP_QTY_OVERRIDE | — | ✅ |
| 68 | OrdersPEOOldDockDate | OLD_DOCK_DATE | — | ✅ |
| 69 | OrdersPEOOldDueDate | OLD_DUE_DATE | — | ✅ |
| 70 | OrdersPEOOrderDate | ORDER_DATE | — | ✅ |
| 71 | OrdersPEOOrderDateType | ORDER_DATE_TYPE | — | ✅ |
| 72 | OrdersPEOOrderNumber | ORDER_NUMBER | — | ✅ |
| 73 | OrdersPEOOrderQuantity | ORDER_QUANTITY | — | ✅ |
| 74 | OrdersPEOOrderType | ORDER_TYPE | — | ✅ |
| 75 | OrdersPEOOrderTypeText | ORDER_TYPE_TEXT | — | ✅ |
| 76 | OrdersPEOOrderValue | ORDER_VALUE | — | ✅ |
| 77 | OrdersPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 78 | OrdersPEOOriginalItem | ORIGINAL_ITEM | — | ✅ |
| 79 | OrdersPEOOriginalItemQuantity | ORIGINAL_ITEM_QUANTITY | — | ✅ |
| 80 | OrdersPEOOriginalNeedByDate | ORIGINAL_NEED_BY_DATE | — | ✅ |
| 81 | OrdersPEOOriginalOrderQuantity | ORIGINAL_ORDER_QUANTITY | — | ✅ |
| 82 | OrdersPEOOverrideDemandPriority | OVERRIDE_DEMAND_PRIORITY | — | — |
| 83 | OrdersPEOPlannedArrivalDate | PLANNED_ARRIVAL_DATE | — | ✅ |
| 84 | OrdersPEOPlannedOrderType | PLANNED_ORDER_TYPE | — | ✅ |
| 85 | OrdersPEOProductFamily | PRODUCT_FAMILY | — | ✅ |
| 86 | OrdersPEOPromisedArrivalDate | PROMISED_ARRIVAL_DATE | — | ✅ |
| 87 | OrdersPEOPromisedShipDate | PROMISED_SHIP_DATE | — | ✅ |
| 88 | OrdersPEOQuantityByDueDate | QUANTITY_BY_DUE_DATE | — | ✅ |
| 89 | OrdersPEOQuantitySatisfiedByDueDate | QUANTITY_SATISFIED_BY_DUE_DATE | — | ✅ |
| 90 | OrdersPEOReadyToBuildPercentage | READY_TO_BUILD_PERCENTAGE | — | ✅ |
| 91 | OrdersPEORecommendationType | RECOMMENDATION_TYPE | — | ✅ |
| 92 | OrdersPEOReleaseErrors | RELEASE_ERRORS | — | ✅ |
| 93 | OrdersPEOReleaseStatus | RELEASE_STATUS | — | ✅ |
| 94 | OrdersPEORequestedArrivalDate | REQUESTED_ARRIVAL_DATE | — | ✅ |
| 95 | OrdersPEORequestedShipDate | REQUESTED_SHIP_DATE | — | ✅ |
| 96 | OrdersPEORescheduleDays | RESCHEDULE_DAYS | — | ✅ |
| 97 | OrdersPEORescheduled | RESCHEDULED | — | ✅ |
| 98 | OrdersPEOReservedQuantity | RESERVED_QUANTITY | — | ✅ |
| 99 | OrdersPEORevisedDemandDate | REVISED_DEMAND_DATE | — | ✅ |
| 100 | OrdersPEORevisedDemandPriority | REVISED_DEMAND_PRIORITY | — | ✅ |
| 101 | OrdersPEOScheduleArrivalDate | SCHEDULE_ARRIVAL_DATE | — | ✅ |
| 102 | OrdersPEOScheduleName | SCHEDULE_NAME | — | ✅ |
| 103 | OrdersPEOScheduleShipDate | SCHEDULE_SHIP_DATE | — | ✅ |
| 104 | OrdersPEOSegmentName | SEGMENT_NAME | — | ✅ |
| 105 | OrdersPEOShipTo | SHIP_TO | — | ✅ |
| 106 | OrdersPEOShipmentSetName | SHIPMENT_SET_NAME | — | ✅ |
| 107 | OrdersPEOShippingMethod | SHIPPING_METHOD | — | ✅ |
| 108 | OrdersPEOSourceOrderPriority | SOURCE_ORDER_PRIORITY | — | ✅ |
| 109 | OrdersPEOSourceOrganization | SOURCE_ORGANIZATION | — | ✅ |
| 110 | OrdersPEOStartQuantity | START_QUANTITY | — | ✅ |
| 111 | OrdersPEOSubinventory | SUBINVENTORY | — | ✅ |
| 112 | OrdersPEOSuggestedDockDate | SUGGESTED_DOCK_DATE | — | ✅ |
| 113 | OrdersPEOSuggestedDueDate | SUGGESTED_DUE_DATE | — | ✅ |
| 114 | OrdersPEOSuggestedOrderDate | SUGGESTED_ORDER_DATE | — | ✅ |
| 115 | OrdersPEOSuggestedShipDate | SUGGESTED_SHIP_DATE | — | ✅ |
| 116 | OrdersPEOSuggestedStartDate | SUGGESTED_START_DATE | — | ✅ |
| 117 | OrdersPEOSupplierId | SUPPLIER_ID | — | ✅ |
| 118 | OrdersPEOSupplierSiteId | SUPPLIER_SITE_ID | — | ✅ |
| 119 | OrdersPEOTransitLeadTime | TRANSIT_LEAD_TIME | — | ✅ |
| 120 | OrdersPEOUnitNumber | UNIT_NUMBER | — | ✅ |
| 121 | OrdersPEOUnmetDemandQuantity | UNMET_DEMAND_QUANTITY | — | ✅ |
| 122 | OrdersPEOUom | UOM | — | ✅ |
| 123 | OrdersPEOUsingAssembly | USING_ASSEMBLY | — | ✅ |
| 124 | OrdersPEOWorkDefinitionName | WORK_DEFINITION_NAME | — | ✅ |
| 125 | OrdersPEOWorkOrderStatus | WORK_ORDER_STATUS | — | ✅ |
| 126 | OrdersPEOZone | ZONE | — | ✅ |
| 127 | PlanId | PLAN_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
