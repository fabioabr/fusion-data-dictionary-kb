---
id: DOC-OTHER-PVO-InventoryTransactionDetailExtractPVO
doc_type: system-doc
title: "InventoryTransactionDetailExtractPVO — PVO Cross-Module"
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
  - InventoryTransactionDetailExtractPVO
  - inventorytransactiondetailextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InventoryTransactionDetailExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Inventory Transaction Detail Extract. Acessa as tabelas: INV_MATERIAL_TXNS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.InvBiccExtractAM.InventoryTransactionDetailExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 282 | 1 | 1 | 210 | 74% |

---

## 🔗 Tabelas Relacionadas

- [[inv_material_txns|INV_MATERIAL_TXNS]] — 282 atributos (1 PKs, 210 BICC)

---

## ⚙️ Atributos

### [[inv_material_txns|INV_MATERIAL_TXNS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InventoryTransactionPEOAcctPeriodId | ACCT_PERIOD_ID | — | ✅ |
| 2 | InventoryTransactionPEOActualCost | ACTUAL_COST | — | ✅ |
| 3 | InventoryTransactionPEOAgingExpirationDate | AGING_EXPIRATION_DATE | — | ✅ |
| 4 | InventoryTransactionPEOAgingOnsetDate | AGING_ONSET_DATE | — | ✅ |
| 5 | InventoryTransactionPEOAssemblySerialNumber | ASSEMBLY_SERIAL_NUMBER | — | ✅ |
| 6 | InventoryTransactionPEOAssessableValue | ASSESSABLE_VALUE | — | ✅ |
| 7 | InventoryTransactionPEOAttribute1 | ATTRIBUTE1 | — | — |
| 8 | InventoryTransactionPEOAttribute10 | ATTRIBUTE10 | — | — |
| 9 | InventoryTransactionPEOAttribute11 | ATTRIBUTE11 | — | — |
| 10 | InventoryTransactionPEOAttribute12 | ATTRIBUTE12 | — | — |
| 11 | InventoryTransactionPEOAttribute13 | ATTRIBUTE13 | — | — |
| 12 | InventoryTransactionPEOAttribute14 | ATTRIBUTE14 | — | — |
| 13 | InventoryTransactionPEOAttribute15 | ATTRIBUTE15 | — | — |
| 14 | InventoryTransactionPEOAttribute16 | ATTRIBUTE16 | — | — |
| 15 | InventoryTransactionPEOAttribute17 | ATTRIBUTE17 | — | — |
| 16 | InventoryTransactionPEOAttribute18 | ATTRIBUTE18 | — | — |
| 17 | InventoryTransactionPEOAttribute19 | ATTRIBUTE19 | — | — |
| 18 | InventoryTransactionPEOAttribute2 | ATTRIBUTE2 | — | — |
| 19 | InventoryTransactionPEOAttribute20 | ATTRIBUTE20 | — | — |
| 20 | InventoryTransactionPEOAttribute3 | ATTRIBUTE3 | — | — |
| 21 | InventoryTransactionPEOAttribute4 | ATTRIBUTE4 | — | — |
| 22 | InventoryTransactionPEOAttribute5 | ATTRIBUTE5 | — | — |
| 23 | InventoryTransactionPEOAttribute6 | ATTRIBUTE6 | — | — |
| 24 | InventoryTransactionPEOAttribute7 | ATTRIBUTE7 | — | — |
| 25 | InventoryTransactionPEOAttribute8 | ATTRIBUTE8 | — | — |
| 26 | InventoryTransactionPEOAttribute9 | ATTRIBUTE9 | — | — |
| 27 | InventoryTransactionPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 28 | InventoryTransactionPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 29 | InventoryTransactionPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 30 | InventoryTransactionPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 31 | InventoryTransactionPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 32 | InventoryTransactionPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 33 | InventoryTransactionPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 34 | InventoryTransactionPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 35 | InventoryTransactionPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 36 | InventoryTransactionPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 37 | InventoryTransactionPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 38 | InventoryTransactionPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 39 | InventoryTransactionPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 40 | InventoryTransactionPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 41 | InventoryTransactionPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 42 | InventoryTransactionPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 43 | InventoryTransactionPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 44 | InventoryTransactionPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 45 | InventoryTransactionPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 46 | InventoryTransactionPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 47 | InventoryTransactionPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 48 | InventoryTransactionPEOBuildBreakToUom | BUILD_BREAK_TO_UOM | — | ✅ |
| 49 | InventoryTransactionPEOCategoryId | CATEGORY_ID | — | ✅ |
| 50 | InventoryTransactionPEOCogsRecognitionPercent | COGS_RECOGNITION_PERCENT | — | ✅ |
| 51 | InventoryTransactionPEOCommonBomSeqId | COMMON_BOM_SEQ_ID | — | ✅ |
| 52 | InventoryTransactionPEOCommonRoutingSeqId | COMMON_ROUTING_SEQ_ID | — | ✅ |
| 53 | InventoryTransactionPEOCompletionTransactionId | COMPLETION_TRANSACTION_ID | — | ✅ |
| 54 | InventoryTransactionPEOConsErrorActionCode | CONS_ERROR_ACTION_CODE | — | ✅ |
| 55 | InventoryTransactionPEOConsErrorTypeCode | CONS_ERROR_TYPE_CODE | — | ✅ |
| 56 | InventoryTransactionPEOConsignmentSourceTxnId | CONSIGNMENT_SOURCE_TXN_ID | — | ✅ |
| 57 | InventoryTransactionPEOConsumptionLineId | CONSUMPTION_LINE_ID | — | ✅ |
| 58 | InventoryTransactionPEOConsumptionUnitPrice | CONSUMPTION_UNIT_PRICE | — | ✅ |
| 59 | InventoryTransactionPEOContentLpnId | CONTENT_LPN_ID | — | ✅ |
| 60 | InventoryTransactionPEOCostCategoryId | COST_CATEGORY_ID | — | ✅ |
| 61 | InventoryTransactionPEOCostGroupId | COST_GROUP_ID | — | ✅ |
| 62 | InventoryTransactionPEOCostTypeId | COST_TYPE_ID | — | ✅ |
| 63 | InventoryTransactionPEOCostUpdateId | COST_UPDATE_ID | — | ✅ |
| 64 | InventoryTransactionPEOCostedFlag | COSTED_FLAG | — | ✅ |
| 65 | InventoryTransactionPEOCountryOfOriginCode | COUNTRY_OF_ORIGIN_CODE | — | ✅ |
| 66 | InventoryTransactionPEOCreatedBy | CREATED_BY | — | ✅ |
| 67 | InventoryTransactionPEOCreationDate | CREATION_DATE | — | ✅ |
| 68 | InventoryTransactionPEOCseInterfaceStatusCode | CSE_INTERFACE_STATUS_CODE | — | ✅ |
| 69 | InventoryTransactionPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 70 | InventoryTransactionPEOCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | ✅ |
| 71 | InventoryTransactionPEOCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | ✅ |
| 72 | InventoryTransactionPEOCurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | ✅ |
| 73 | InventoryTransactionPEOCycleCountId | CYCLE_COUNT_ID | — | ✅ |
| 74 | InventoryTransactionPEODefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | ✅ |
| 75 | InventoryTransactionPEODepartmentCode | DEPARTMENT_CODE | — | ✅ |
| 76 | InventoryTransactionPEODepartmentId | DEPARTMENT_ID | — | ✅ |
| 77 | InventoryTransactionPEODepreciableFlag | DEPRECIABLE_FLAG | — | ✅ |
| 78 | InventoryTransactionPEODistributionAccountId | DISTRIBUTION_ACCOUNT_ID | — | ✅ |
| 79 | InventoryTransactionPEODocumentSubType | DOCUMENT_SUB_TYPE | — | ✅ |
| 80 | InventoryTransactionPEOERecordId | E_RECORD_ID | — | ✅ |
| 81 | InventoryTransactionPEOEmployeeCode | EMPLOYEE_CODE | — | ✅ |
| 82 | InventoryTransactionPEOEncumbranceAccount | ENCUMBRANCE_ACCOUNT | — | ✅ |
| 83 | InventoryTransactionPEOEncumbranceAmount | ENCUMBRANCE_AMOUNT | — | ✅ |
| 84 | InventoryTransactionPEOErrorCode | ERROR_CODE | — | ✅ |
| 85 | InventoryTransactionPEOErrorConsHeaderId | ERROR_CONS_HEADER_ID | — | ✅ |
| 86 | InventoryTransactionPEOErrorExplanation | ERROR_EXPLANATION | — | ✅ |
| 87 | InventoryTransactionPEOExemptCertificateNumber | EXEMPT_CERTIFICATE_NUMBER | — | ✅ |
| 88 | InventoryTransactionPEOExemptReasonCode | EXEMPT_REASON_CODE | — | ✅ |
| 89 | InventoryTransactionPEOExpenseAccountId | EXPENSE_ACCOUNT_ID | — | ✅ |
| 90 | InventoryTransactionPEOExternalSysTxnReference | EXTERNAL_SYS_TXN_REFERENCE | — | ✅ |
| 91 | InventoryTransactionPEOExternalSystemPackingUnit | EXTERNAL_SYSTEM_PACKING_UNIT | — | ✅ |
| 92 | InventoryTransactionPEOFinalCompletionFlag | FINAL_COMPLETION_FLAG | — | ✅ |
| 93 | InventoryTransactionPEOFinalDischargeLocationId | FINAL_DISCHARGE_LOCATION_ID | — | ✅ |
| 94 | InventoryTransactionPEOFirstPtyRegId | FIRST_PTY_REG_ID | — | ✅ |
| 95 | InventoryTransactionPEOFlowSchedule | FLOW_SCHEDULE | — | ✅ |
| 96 | InventoryTransactionPEOFobPoint | FOB_POINT | — | ✅ |
| 97 | InventoryTransactionPEOFreightCode | FREIGHT_CODE | — | ✅ |
| 98 | InventoryTransactionPEOFromGradeCode | FROM_GRADE_CODE | — | ✅ |
| 99 | InventoryTransactionPEOFromProjectId | FROM_PROJECT_ID | — | ✅ |
| 100 | InventoryTransactionPEOFromTaskId | FROM_TASK_ID | — | ✅ |
| 101 | InventoryTransactionPEOIntendedUseClassifId | INTENDED_USE_CLASSIF_ID | — | ✅ |
| 102 | InventoryTransactionPEOIntercompanyCost | INTERCOMPANY_COST | — | ✅ |
| 103 | InventoryTransactionPEOIntercompanyCurrencyCode | INTERCOMPANY_CURRENCY_CODE | — | ✅ |
| 104 | InventoryTransactionPEOIntercompanyPricingOption | INTERCOMPANY_PRICING_OPTION | — | ✅ |
| 105 | InventoryTransactionPEOIntransitAccount | INTRANSIT_ACCOUNT | — | ✅ |
| 106 | InventoryTransactionPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 107 | InventoryTransactionPEOInvoicedFlag | INVOICED_FLAG | — | ✅ |
| 108 | InventoryTransactionPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 109 | InventoryTransactionPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 110 | InventoryTransactionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 111 | InventoryTransactionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 112 | InventoryTransactionPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 113 | InventoryTransactionPEOLicensePlateNumber | LICENSE_PLATE_NUMBER | — | ✅ |
| 114 | InventoryTransactionPEOLocationType | LOCATION_TYPE | — | ✅ |
| 115 | InventoryTransactionPEOLocatorId | LOCATOR_ID | — | ✅ |
| 116 | InventoryTransactionPEOLogicalTransaction | LOGICAL_TRANSACTION | — | ✅ |
| 117 | InventoryTransactionPEOLogicalTransactionsCreated | LOGICAL_TRANSACTIONS_CREATED | — | ✅ |
| 118 | InventoryTransactionPEOLogicalTrxTypeCode | LOGICAL_TRX_TYPE_CODE | — | ✅ |
| 119 | InventoryTransactionPEOLpnId | LPN_ID | — | ✅ |
| 120 | InventoryTransactionPEOManualReceiptExpense | MANUAL_RECEIPT_EXPENSE | — | ✅ |
| 121 | InventoryTransactionPEOMasterScheduleUpdateCode | MASTER_SCHEDULE_UPDATE_CODE | — | ✅ |
| 122 | InventoryTransactionPEOMaterialAccount | MATERIAL_ACCOUNT | — | ✅ |
| 123 | InventoryTransactionPEOMaterialOverheadAccount | MATERIAL_OVERHEAD_ACCOUNT | — | ✅ |
| 124 | InventoryTransactionPEOMoveOrderLineId | MOVE_ORDER_LINE_ID | — | ✅ |
| 125 | InventoryTransactionPEOMoveTransactionId | MOVE_TRANSACTION_ID | — | ✅ |
| 126 | InventoryTransactionPEOMovementId | MOVEMENT_ID | — | ✅ |
| 127 | InventoryTransactionPEOMvtStatStatus | MVT_STAT_STATUS | — | ✅ |
| 128 | InventoryTransactionPEONewCost | NEW_COST | — | ✅ |
| 129 | InventoryTransactionPEONumberOfContainers | NUMBER_OF_CONTAINERS | — | ✅ |
| 130 | InventoryTransactionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 131 | InventoryTransactionPEOOperationSeqNum | OPERATION_SEQ_NUM | — | ✅ |
| 132 | InventoryTransactionPEOOperationSeqNumberId | OPERATION_SEQ_NUMBER_ID | — | ✅ |
| 133 | InventoryTransactionPEOOperationTransactionId | OPERATION_TRANSACTION_ID | — | ✅ |
| 134 | InventoryTransactionPEOOpmCostedFlag | OPM_COSTED_FLAG | — | ✅ |
| 135 | InventoryTransactionPEOOrgCostGroupId | ORG_COST_GROUP_ID | — | ✅ |
| 136 | InventoryTransactionPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 137 | InventoryTransactionPEOOrganizationType | ORGANIZATION_TYPE | — | ✅ |
| 138 | InventoryTransactionPEOOrigLocatorId | ORIG_LOCATOR_ID | — | ✅ |
| 139 | InventoryTransactionPEOOrigLotNumber | ORIG_LOT_NUMBER | — | ✅ |
| 140 | InventoryTransactionPEOOrigSubinventoryCode | ORIG_SUBINVENTORY_CODE | — | ✅ |
| 141 | InventoryTransactionPEOOrigTransactionQuantity | ORIG_TRANSACTION_QUANTITY | — | ✅ |
| 142 | InventoryTransactionPEOOriginalShipmentTxnId | ORIGINAL_SHIPMENT_TXN_ID | — | ✅ |
| 143 | InventoryTransactionPEOOriginalTransactionTempId | ORIGINAL_TRANSACTION_TEMP_ID | — | ✅ |
| 144 | InventoryTransactionPEOOutsideProcessingAccount | OUTSIDE_PROCESSING_ACCOUNT | — | ✅ |
| 145 | InventoryTransactionPEOOvercompletionPrimaryQty | OVERCOMPLETION_PRIMARY_QTY | — | ✅ |
| 146 | InventoryTransactionPEOOvercompletionTransactionId | OVERCOMPLETION_TRANSACTION_ID | — | ✅ |
| 147 | InventoryTransactionPEOOvercompletionTransactionQty | OVERCOMPLETION_TRANSACTION_QTY | — | ✅ |
| 148 | InventoryTransactionPEOOverheadAccount | OVERHEAD_ACCOUNT | — | ✅ |
| 149 | InventoryTransactionPEOOwnershipChangeTxnId | OWNERSHIP_CHANGE_TXN_ID | — | ✅ |
| 150 | InventoryTransactionPEOOwningOrganizationId | OWNING_ORGANIZATION_ID | — | ✅ |
| 151 | InventoryTransactionPEOOwningTpType | OWNING_TP_TYPE | — | ✅ |
| 152 | InventoryTransactionPEOParentTransactionId | PARENT_TRANSACTION_ID | — | ✅ |
| 153 | InventoryTransactionPEOPercentageChange | PERCENTAGE_CHANGE | — | ✅ |
| 154 | InventoryTransactionPEOPeriodicPrimaryQuantity | PERIODIC_PRIMARY_QUANTITY | — | ✅ |
| 155 | InventoryTransactionPEOPhysicalAdjustmentId | PHYSICAL_ADJUSTMENT_ID | — | ✅ |
| 156 | InventoryTransactionPEOPickRuleId | PICK_RULE_ID | — | ✅ |
| 157 | InventoryTransactionPEOPickSlipDate | PICK_SLIP_DATE | — | ✅ |
| 158 | InventoryTransactionPEOPickSlipLineNumber | PICK_SLIP_LINE_NUMBER | — | ✅ |
| 159 | InventoryTransactionPEOPickSlipNumber | PICK_SLIP_NUMBER | — | ✅ |
| 160 | InventoryTransactionPEOPickStrategyId | PICK_STRATEGY_ID | — | ✅ |
| 161 | InventoryTransactionPEOPickingLineId | PICKING_LINE_ID | — | ✅ |
| 162 | InventoryTransactionPEOPjcBillableFlag | PJC_BILLABLE_FLAG | — | — |
| 163 | InventoryTransactionPEOPjcCapitalizableFlag | PJC_CAPITALIZABLE_FLAG | — | — |
| 164 | InventoryTransactionPEOPjcContextCategory | PJC_CONTEXT_CATEGORY | — | — |
| 165 | InventoryTransactionPEOPjcContractId | PJC_CONTRACT_ID | — | — |
| 166 | InventoryTransactionPEOPjcContractLineId | PJC_CONTRACT_LINE_ID | — | — |
| 167 | InventoryTransactionPEOPjcExpenditureItemDate | PJC_EXPENDITURE_ITEM_DATE | — | — |
| 168 | InventoryTransactionPEOPjcExpenditureTypeId | PJC_EXPENDITURE_TYPE_ID | — | — |
| 169 | InventoryTransactionPEOPjcFundingAllocationId | PJC_FUNDING_ALLOCATION_ID | — | — |
| 170 | InventoryTransactionPEOPjcOrganizationId | PJC_ORGANIZATION_ID | — | ✅ |
| 171 | InventoryTransactionPEOPjcProjectId | PJC_PROJECT_ID | — | — |
| 172 | InventoryTransactionPEOPjcReservedAttribute1 | PJC_RESERVED_ATTRIBUTE1 | — | — |
| 173 | InventoryTransactionPEOPjcReservedAttribute10 | PJC_RESERVED_ATTRIBUTE10 | — | — |
| 174 | InventoryTransactionPEOPjcReservedAttribute2 | PJC_RESERVED_ATTRIBUTE2 | — | — |
| 175 | InventoryTransactionPEOPjcReservedAttribute3 | PJC_RESERVED_ATTRIBUTE3 | — | — |
| 176 | InventoryTransactionPEOPjcReservedAttribute4 | PJC_RESERVED_ATTRIBUTE4 | — | — |
| 177 | InventoryTransactionPEOPjcReservedAttribute5 | PJC_RESERVED_ATTRIBUTE5 | — | — |
| 178 | InventoryTransactionPEOPjcReservedAttribute6 | PJC_RESERVED_ATTRIBUTE6 | — | — |
| 179 | InventoryTransactionPEOPjcReservedAttribute7 | PJC_RESERVED_ATTRIBUTE7 | — | — |
| 180 | InventoryTransactionPEOPjcReservedAttribute8 | PJC_RESERVED_ATTRIBUTE8 | — | — |
| 181 | InventoryTransactionPEOPjcReservedAttribute9 | PJC_RESERVED_ATTRIBUTE9 | — | — |
| 182 | InventoryTransactionPEOPjcTaskId | PJC_TASK_ID | — | — |
| 183 | InventoryTransactionPEOPjcUserDefAttribute1 | PJC_USER_DEF_ATTRIBUTE1 | — | — |
| 184 | InventoryTransactionPEOPjcUserDefAttribute10 | PJC_USER_DEF_ATTRIBUTE10 | — | — |
| 185 | InventoryTransactionPEOPjcUserDefAttribute2 | PJC_USER_DEF_ATTRIBUTE2 | — | — |
| 186 | InventoryTransactionPEOPjcUserDefAttribute3 | PJC_USER_DEF_ATTRIBUTE3 | — | — |
| 187 | InventoryTransactionPEOPjcUserDefAttribute4 | PJC_USER_DEF_ATTRIBUTE4 | — | — |
| 188 | InventoryTransactionPEOPjcUserDefAttribute5 | PJC_USER_DEF_ATTRIBUTE5 | — | — |
| 189 | InventoryTransactionPEOPjcUserDefAttribute6 | PJC_USER_DEF_ATTRIBUTE6 | — | — |
| 190 | InventoryTransactionPEOPjcUserDefAttribute7 | PJC_USER_DEF_ATTRIBUTE7 | — | — |
| 191 | InventoryTransactionPEOPjcUserDefAttribute8 | PJC_USER_DEF_ATTRIBUTE8 | — | — |
| 192 | InventoryTransactionPEOPjcUserDefAttribute9 | PJC_USER_DEF_ATTRIBUTE9 | — | — |
| 193 | InventoryTransactionPEOPjcWorkTypeId | PJC_WORK_TYPE_ID | — | — |
| 194 | InventoryTransactionPEOPlanningOrganizationId | PLANNING_ORGANIZATION_ID | — | ✅ |
| 195 | InventoryTransactionPEOPlanningTpType | PLANNING_TP_TYPE | — | ✅ |
| 196 | InventoryTransactionPEOPmCostCollected | PM_COST_COLLECTED | — | ✅ |
| 197 | InventoryTransactionPEOPmCostCollectorGroupId | PM_COST_COLLECTOR_GROUP_ID | — | ✅ |
| 198 | InventoryTransactionPEOPrimaryQuantity | PRIMARY_QUANTITY | — | ✅ |
| 199 | InventoryTransactionPEOPriorCost | PRIOR_COST | — | ✅ |
| 200 | InventoryTransactionPEOPriorCostedQuantity | PRIOR_COSTED_QUANTITY | — | ✅ |
| 201 | InventoryTransactionPEOProductCategory | PRODUCT_CATEGORY | — | ✅ |
| 202 | InventoryTransactionPEOProductType | PRODUCT_TYPE | — | ✅ |
| 203 | InventoryTransactionPEOProjectId | PROJECT_ID | — | ✅ |
| 204 | InventoryTransactionPEOPutAwayRuleId | PUT_AWAY_RULE_ID | — | ✅ |
| 205 | InventoryTransactionPEOPutAwayStrategyId | PUT_AWAY_STRATEGY_ID | — | ✅ |
| 206 | InventoryTransactionPEOQaCollectionId | QA_COLLECTION_ID | — | ✅ |
| 207 | InventoryTransactionPEOQuantityAdjusted | QUANTITY_ADJUSTED | — | ✅ |
| 208 | InventoryTransactionPEORcvTransactionId | RCV_TRANSACTION_ID | — | ✅ |
| 209 | InventoryTransactionPEOReasonId | REASON_ID | — | ✅ |
| 210 | InventoryTransactionPEOReceivingDocument | RECEIVING_DOCUMENT | — | ✅ |
| 211 | InventoryTransactionPEORepetitiveLineId | REPETITIVE_LINE_ID | — | ✅ |
| 212 | InventoryTransactionPEORequestId | REQUEST_ID | — | ✅ |
| 213 | InventoryTransactionPEOReservationId | RESERVATION_ID | — | ✅ |
| 214 | InventoryTransactionPEOResourceAccount | RESOURCE_ACCOUNT | — | ✅ |
| 215 | InventoryTransactionPEORevision | REVISION | — | ✅ |
| 216 | InventoryTransactionPEORmaLineId | RMA_LINE_ID | — | ✅ |
| 217 | InventoryTransactionPEOSecondaryTransactionQuantity | SECONDARY_TRANSACTION_QUANTITY | — | ✅ |
| 218 | InventoryTransactionPEOSecondaryUomCode | SECONDARY_UOM_CODE | — | ✅ |
| 219 | InventoryTransactionPEOShipFromLocationId | SHIP_FROM_LOCATION_ID | — | ✅ |
| 220 | InventoryTransactionPEOShipToLocationId | SHIP_TO_LOCATION_ID | — | ✅ |
| 221 | InventoryTransactionPEOShipmentCosted | SHIPMENT_COSTED | — | ✅ |
| 222 | InventoryTransactionPEOShipmentNumber | SHIPMENT_NUMBER | — | ✅ |
| 223 | InventoryTransactionPEOShortageProcessCode | SHORTAGE_PROCESS_CODE | — | ✅ |
| 224 | InventoryTransactionPEOSoIssueAccountType | SO_ISSUE_ACCOUNT_TYPE | — | ✅ |
| 225 | InventoryTransactionPEOSourceCode | SOURCE_CODE | — | ✅ |
| 226 | InventoryTransactionPEOSourceLineId | SOURCE_LINE_ID | — | ✅ |
| 227 | InventoryTransactionPEOSubinventoryCode | SUBINVENTORY_CODE | — | ✅ |
| 228 | InventoryTransactionPEOTaskGroupId | TASK_GROUP_ID | — | ✅ |
| 229 | InventoryTransactionPEOTaskId | TASK_ID | — | ✅ |
| 230 | InventoryTransactionPEOTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | ✅ |
| 231 | InventoryTransactionPEOTaxInvoiceDate | TAX_INVOICE_DATE | — | ✅ |
| 232 | InventoryTransactionPEOTaxInvoiceNumber | TAX_INVOICE_NUMBER | — | ✅ |
| 233 | InventoryTransactionPEOThirdPtyRegId | THIRD_PTY_REG_ID | — | ✅ |
| 234 | InventoryTransactionPEOToGradeCode | TO_GRADE_CODE | — | ✅ |
| 235 | InventoryTransactionPEOToProjectId | TO_PROJECT_ID | — | ✅ |
| 236 | InventoryTransactionPEOToTaskId | TO_TASK_ID | — | ✅ |
| 237 | InventoryTransactionPEOTransactionActionId | TRANSACTION_ACTION_ID | — | ✅ |
| 238 | InventoryTransactionPEOTransactionBatchId | TRANSACTION_BATCH_ID | — | ✅ |
| 239 | InventoryTransactionPEOTransactionBatchSeq | TRANSACTION_BATCH_SEQ | — | ✅ |
| 240 | InventoryTransactionPEOTransactionCost | TRANSACTION_COST | — | ✅ |
| 241 | InventoryTransactionPEOTransactionDate | TRANSACTION_DATE | — | ✅ |
| 242 | InventoryTransactionPEOTransactionGroupId | TRANSACTION_GROUP_ID | — | ✅ |
| 243 | InventoryTransactionPEOTransactionId | TRANSACTION_ID | 🔑 | ✅ |
| 244 | InventoryTransactionPEOTransactionInterfaceId | TRANSACTION_INTERFACE_ID | — | ✅ |
| 245 | InventoryTransactionPEOTransactionMode | TRANSACTION_MODE | — | ✅ |
| 246 | InventoryTransactionPEOTransactionQuantity | TRANSACTION_QUANTITY | — | ✅ |
| 247 | InventoryTransactionPEOTransactionReference | TRANSACTION_REFERENCE | — | ✅ |
| 248 | InventoryTransactionPEOTransactionSetId | TRANSACTION_SET_ID | — | ✅ |
| 249 | InventoryTransactionPEOTransactionSourceId | TRANSACTION_SOURCE_ID | — | ✅ |
| 250 | InventoryTransactionPEOTransactionSourceName | TRANSACTION_SOURCE_NAME | — | ✅ |
| 251 | InventoryTransactionPEOTransactionSourceTypeId | TRANSACTION_SOURCE_TYPE_ID | — | ✅ |
| 252 | InventoryTransactionPEOTransactionTypeId | TRANSACTION_TYPE_ID | — | ✅ |
| 253 | InventoryTransactionPEOTransactionUom | TRANSACTION_UOM | — | ✅ |
| 254 | InventoryTransactionPEOTransferCost | TRANSFER_COST | — | ✅ |
| 255 | InventoryTransactionPEOTransferCostDistAccount | TRANSFER_COST_DIST_ACCOUNT | — | ✅ |
| 256 | InventoryTransactionPEOTransferCostGroupId | TRANSFER_COST_GROUP_ID | — | ✅ |
| 257 | InventoryTransactionPEOTransferLocatorId | TRANSFER_LOCATOR_ID | — | ✅ |
| 258 | InventoryTransactionPEOTransferLpnId | TRANSFER_LPN_ID | — | ✅ |
| 259 | InventoryTransactionPEOTransferOrganizationId | TRANSFER_ORGANIZATION_ID | — | ✅ |
| 260 | InventoryTransactionPEOTransferOrganizationType | TRANSFER_ORGANIZATION_TYPE | — | ✅ |
| 261 | InventoryTransactionPEOTransferOwningTpType | TRANSFER_OWNING_TP_TYPE | — | ✅ |
| 262 | InventoryTransactionPEOTransferPercentage | TRANSFER_PERCENTAGE | — | ✅ |
| 263 | InventoryTransactionPEOTransferPlanningTpType | TRANSFER_PLANNING_TP_TYPE | — | ✅ |
| 264 | InventoryTransactionPEOTransferPrice | TRANSFER_PRICE | — | ✅ |
| 265 | InventoryTransactionPEOTransferPriorCostedQuantity | TRANSFER_PRIOR_COSTED_QUANTITY | — | ✅ |
| 266 | InventoryTransactionPEOTransferSubinventory | TRANSFER_SUBINVENTORY | — | ✅ |
| 267 | InventoryTransactionPEOTransferTransactionId | TRANSFER_TRANSACTION_ID | — | ✅ |
| 268 | InventoryTransactionPEOTransportationCost | TRANSPORTATION_COST | — | ✅ |
| 269 | InventoryTransactionPEOTransportationDistAccount | TRANSPORTATION_DIST_ACCOUNT | — | ✅ |
| 270 | InventoryTransactionPEOTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | ✅ |
| 271 | InventoryTransactionPEOTrxFlowHeaderId | TRX_FLOW_HEADER_ID | — | ✅ |
| 272 | InventoryTransactionPEOTrxSourceDeliveryId | TRX_SOURCE_DELIVERY_ID | — | ✅ |
| 273 | InventoryTransactionPEOTrxSourceLineId | TRX_SOURCE_LINE_ID | — | ✅ |
| 274 | InventoryTransactionPEOUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | ✅ |
| 275 | InventoryTransactionPEOUssglTransactionCode | USSGL_TRANSACTION_CODE | — | ✅ |
| 276 | InventoryTransactionPEOValueChange | VALUE_CHANGE | — | ✅ |
| 277 | InventoryTransactionPEOVarianceAmount | VARIANCE_AMOUNT | — | ✅ |
| 278 | InventoryTransactionPEOVendorLotNumber | VENDOR_LOT_NUMBER | — | ✅ |
| 279 | InventoryTransactionPEOWaybillAirbill | WAYBILL_AIRBILL | — | ✅ |
| 280 | InventoryTransactionPEOWipSupplyType | WIP_SUPPLY_TYPE | — | ✅ |
| 281 | InventoryTransactionPEOXfrOwningOrganizationId | XFR_OWNING_ORGANIZATION_ID | — | ✅ |
| 282 | InventoryTransactionPEOXfrPlanningOrganizationId | XFR_PLANNING_ORGANIZATION_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
