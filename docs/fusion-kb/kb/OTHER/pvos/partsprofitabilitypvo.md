---
id: DOC-OTHER-PVO-PartsProfitabilityPVO
doc_type: system-doc
title: "PartsProfitabilityPVO — PVO Cross-Module"
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
  - PartsProfitabilityPVO
  - partsprofitabilitypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PartsProfitabilityPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Parts Profitability. Acessa as tabelas: HZ_PARTY_SITES, QP_CHARGE_DEFINITIONS_VL, QP_PRICE_ELEMENTS_VL (+6).

**Caminho:** `FscmTopModelAM.PartsAnalyticsAM.PartsProfitabilityPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 247 | 9 | 1 | 31 | 13% |

---

## 🔗 Tabelas Relacionadas

- [[hz_party_sites|HZ_PARTY_SITES]] — 34 atributos (1 BICC)
- [[qp_charge_definitions_vl|QP_CHARGE_DEFINITIONS_VL]] — 22 atributos (2 BICC)
- [[qp_price_elements_vl|QP_PRICE_ELEMENTS_VL]] — 14 atributos (2 BICC)
- [[qp_pricing_strategies_vl|QP_PRICING_STRATEGIES_VL]] — 20 atributos (2 BICC)
- [[rcl_parts_req_lines|RCL_PARTS_REQ_LINES]] — 22 atributos (10 BICC)
- [[rcl_pricing_headers|RCL_PRICING_HEADERS]] — 19 atributos (4 BICC)
- [[rcl_service_charges|RCL_SERVICE_CHARGES]] — 28 atributos (3 BICC)
- [[rcl_service_charge_components|RCL_SERVICE_CHARGE_COMPONENTS]] — 35 atributos (1 PKs, 5 BICC)
- [[svc_service_requests|SVC_SERVICE_REQUESTS]] — 53 atributos (2 BICC)

---

## ⚙️ Atributos

### [[hz_party_sites|HZ_PARTY_SITES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartySitePEOActualContentSource | ACTUAL_CONTENT_SOURCE | — | — |
| 2 | PartySitePEOAddressee | ADDRESSEE | — | — |
| 3 | PartySitePEOComments | COMMENTS | — | — |
| 4 | PartySitePEOCorpCurrencyCode | CORP_CURRENCY_CODE | — | — |
| 5 | PartySitePEOCreatedBy | CREATED_BY | — | — |
| 6 | PartySitePEOCreatedByModule | CREATED_BY_MODULE | — | — |
| 7 | PartySitePEOCreationDate | CREATION_DATE | — | — |
| 8 | PartySitePEOCurcyConvRateType | CURCY_CONV_RATE_TYPE | — | — |
| 9 | PartySitePEOCurrencyCode | CURRENCY_CODE | — | — |
| 10 | PartySitePEODunsNumberC | DUNS_NUMBER_C | — | — |
| 11 | PartySitePEOEndDateActive | END_DATE_ACTIVE | — | — |
| 12 | PartySitePEOGlobalLocationNumber | GLOBAL_LOCATION_NUMBER | — | — |
| 13 | PartySitePEOIdentifyingAddressFlag | IDENTIFYING_ADDRESS_FLAG | — | — |
| 14 | PartySitePEOLanguage | PARTY_SITE_LANGUAGE | — | — |
| 15 | PartySitePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | PartySitePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 17 | PartySitePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 18 | PartySitePEOLocationId | LOCATION_ID | — | — |
| 19 | PartySitePEOMailstop | MAILSTOP | — | — |
| 20 | PartySitePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 21 | PartySitePEOOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 22 | PartySitePEOOverallPrimaryFlag | OVERALL_PRIMARY_FLAG | — | — |
| 23 | PartySitePEOPartyId | PARTY_ID | — | — |
| 24 | PartySitePEOPartyNameDba | PARTY_NAME_DBA | — | — |
| 25 | PartySitePEOPartyNameDivision | PARTY_NAME_DIVISION | — | — |
| 26 | PartySitePEOPartyNameLegal | PARTY_NAME_LEGAL | — | — |
| 27 | PartySitePEOPartySiteId | PARTY_SITE_ID | — | — |
| 28 | PartySitePEOPartySiteName | PARTY_SITE_NAME | — | — |
| 29 | PartySitePEOPartySiteNumber | PARTY_SITE_NUMBER | — | — |
| 30 | PartySitePEOPartySiteType | PARTY_SITE_TYPE | — | — |
| 31 | PartySitePEOPartyUsageCode | PARTY_USAGE_CODE | — | — |
| 32 | PartySitePEORelationshipId | RELATIONSHIP_ID | — | — |
| 33 | PartySitePEOStartDateActive | START_DATE_ACTIVE | — | — |
| 34 | PartySitePEOStatus | STATUS | — | — |

### [[qp_charge_definitions_vl|QP_CHARGE_DEFINITIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChargeDefinitionPEOActiveFlag | ACTIVE_FLAG | — | — |
| 2 | ChargeDefinitionPEOAppliesToCode | APPLIES_TO_CODE | — | — |
| 3 | ChargeDefinitionPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 4 | ChargeDefinitionPEOCalculateMarginFlag | CALCULATE_MARGIN_FLAG | — | — |
| 5 | ChargeDefinitionPEOChargeDefinitionCode1 | CHARGE_DEFINITION_CODE | — | — |
| 6 | ChargeDefinitionPEOChargeDefinitionId | CHARGE_DEFINITION_ID | — | — |
| 7 | ChargeDefinitionPEOChargeDefinitionId1 | CHARGE_DEFINITION_ID | — | — |
| 8 | ChargeDefinitionPEOChargeSubtypeCode1 | CHARGE_SUBTYPE_CODE | — | — |
| 9 | ChargeDefinitionPEOChargeTypeCode1 | CHARGE_TYPE_CODE | — | — |
| 10 | ChargeDefinitionPEOCreatedBy5 | CREATED_BY | — | — |
| 11 | ChargeDefinitionPEOCreationDate5 | CREATION_DATE | — | — |
| 12 | ChargeDefinitionPEODescription | DESCRIPTION | — | — |
| 13 | ChargeDefinitionPEOLastUpdateDate5 | LAST_UPDATE_DATE | — | ✅ |
| 14 | ChargeDefinitionPEOLastUpdateLogin5 | LAST_UPDATE_LOGIN | — | — |
| 15 | ChargeDefinitionPEOLastUpdatedBy5 | LAST_UPDATED_BY | — | — |
| 16 | ChargeDefinitionPEOName | NAME | — | ✅ |
| 17 | ChargeDefinitionPEOObjectVersionNumber5 | OBJECT_VERSION_NUMBER | — | — |
| 18 | ChargeDefinitionPEOPricePeriodicityUomClass | PRICE_PERIODICITY_UOM_CLASS | — | — |
| 19 | ChargeDefinitionPEOPriceTypeCode1 | PRICE_TYPE_CODE | — | — |
| 20 | ChargeDefinitionPEORefundableFlag | REFUNDABLE_FLAG | — | — |
| 21 | ChargeDefinitionPEOSetupEnabledFlag | SETUP_ENABLED_FLAG | — | — |
| 22 | ChargeDefinitionPEOUsageUomClass | USAGE_UOM_CLASS | — | — |

### [[qp_price_elements_vl|QP_PRICE_ELEMENTS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PriceElementPEOActiveFlag | ACTIVE_FLAG | — | — |
| 2 | PriceElementPEOCreatedBy | CREATED_BY | — | — |
| 3 | PriceElementPEOCreationDate | CREATION_DATE | — | — |
| 4 | PriceElementPEOElementCode | ELEMENT_CODE | — | — |
| 5 | PriceElementPEOElementTypeCode | ELEMENT_TYPE_CODE | — | — |
| 6 | PriceElementPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | PriceElementPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | PriceElementPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | PriceElementPEOName | NAME | — | ✅ |
| 10 | PriceElementPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | PriceElementPEOPriceElementId | PRICE_ELEMENT_ID | — | — |
| 12 | PriceElementPEOPriceElementId1 | PRICE_ELEMENT_ID | — | — |
| 13 | PriceElementPEOPricingGuidelineEnabledFlag | PRICING_GUIDELINE_ENABLED_FLAG | — | — |
| 14 | PriceElementPEOSeededFlag | SEEDED_FLAG | — | — |

### [[qp_pricing_strategies_vl|QP_PRICING_STRATEGIES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PricingStrategyPEOAllowCurrencyOverrideFlag | ALLOW_CURRENCY_OVERRIDE_FLAG | — | — |
| 2 | PricingStrategyPEOAllowPriceListOverrideFlag | ALLOW_PRICE_LIST_OVERRIDE_FLAG | — | — |
| 3 | PricingStrategyPEOAttributeCategory1 | ATTRIBUTE_CATEGORY | — | — |
| 4 | PricingStrategyPEOCreatedBy6 | CREATED_BY | — | — |
| 5 | PricingStrategyPEOCreationDate6 | CREATION_DATE | — | — |
| 6 | PricingStrategyPEODefaultCurrencyCode | DEFAULT_CURRENCY_CODE | — | — |
| 7 | PricingStrategyPEODefaultGlConvTypeCode | DEFAULT_GL_CONV_TYPE_CODE | — | — |
| 8 | PricingStrategyPEODescription1 | DESCRIPTION | — | — |
| 9 | PricingStrategyPEOEndDate | END_DATE | — | — |
| 10 | PricingStrategyPEOLastUpdateDate6 | LAST_UPDATE_DATE | — | ✅ |
| 11 | PricingStrategyPEOLastUpdateLogin6 | LAST_UPDATE_LOGIN | — | — |
| 12 | PricingStrategyPEOLastUpdatedBy6 | LAST_UPDATED_BY | — | — |
| 13 | PricingStrategyPEOName1 | NAME | — | ✅ |
| 14 | PricingStrategyPEOObjectVersionNumber6 | OBJECT_VERSION_NUMBER | — | — |
| 15 | PricingStrategyPEOObjectiveCode | OBJECTIVE_CODE | — | — |
| 16 | PricingStrategyPEOOrgId1 | ORG_ID | — | — |
| 17 | PricingStrategyPEOPricingStrategyId1 | PRICING_STRATEGY_ID | — | — |
| 18 | PricingStrategyPEOPricingStrategyId2 | PRICING_STRATEGY_ID | — | — |
| 19 | PricingStrategyPEOStartDate | START_DATE | — | — |
| 20 | PricingStrategyPEOStatusCode | STATUS_CODE | — | — |

### [[rcl_parts_req_lines|RCL_PARTS_REQ_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartsReqLinesPEOCreatedBy2 | CREATED_BY | — | — |
| 2 | PartsReqLinesPEOCreationDate2 | CREATION_DATE | — | — |
| 3 | PartsReqLinesPEODestinationOrganizationId | DESTINATION_ORGANIZATION_ID | — | — |
| 4 | PartsReqLinesPEODestinationSubinventory | DESTINATION_SUBINVENTORY | — | ✅ |
| 5 | PartsReqLinesPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 6 | PartsReqLinesPEOLastUpdateDate2 | LAST_UPDATE_DATE | — | ✅ |
| 7 | PartsReqLinesPEOLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 8 | PartsReqLinesPEOLastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 9 | PartsReqLinesPEONeedByDate | NEED_BY_DATE | — | ✅ |
| 10 | PartsReqLinesPEOObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 11 | PartsReqLinesPEOParentEntityCode1 | PARENT_ENTITY_CODE | — | ✅ |
| 12 | PartsReqLinesPEOParentEntityId1 | PARENT_ENTITY_ID | — | ✅ |
| 13 | PartsReqLinesPEOQuantity | QUANTITY | — | ✅ |
| 14 | PartsReqLinesPEORequirementHeaderId | REQUIREMENT_HEADER_ID | — | — |
| 15 | PartsReqLinesPEORequirementLineId | REQUIREMENT_LINE_ID | — | ✅ |
| 16 | PartsReqLinesPEOReturnReasonCode | RETURN_REASON_CODE | — | — |
| 17 | PartsReqLinesPEORevision | REVISION | — | ✅ |
| 18 | PartsReqLinesPEOServiceActivityId | SERVICE_ACTIVITY_ID | — | — |
| 19 | PartsReqLinesPEOShipToAddressType | SHIP_TO_ADDRESS_TYPE | — | ✅ |
| 20 | PartsReqLinesPEOShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 21 | PartsReqLinesPEOShipToLocationId | SHIP_TO_LOCATION_ID | — | — |
| 22 | PartsReqLinesPEOUomCode | UOM_CODE | — | ✅ |

### [[rcl_pricing_headers|RCL_PRICING_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PricingHeadersPEOAppliedCurrencyCode | APPLIED_CURRENCY_CODE | — | ✅ |
| 2 | PricingHeadersPEOCreatedBy3 | CREATED_BY | — | — |
| 3 | PricingHeadersPEOCreationDate3 | CREATION_DATE | — | — |
| 4 | PricingHeadersPEOLastUpdateDate3 | LAST_UPDATE_DATE | — | ✅ |
| 5 | PricingHeadersPEOLastUpdateLogin3 | LAST_UPDATE_LOGIN | — | — |
| 6 | PricingHeadersPEOLastUpdatedBy3 | LAST_UPDATED_BY | — | — |
| 7 | PricingHeadersPEOObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 8 | PricingHeadersPEOOrgId | ORG_ID | — | — |
| 9 | PricingHeadersPEOPricedOn | PRICED_ON | — | — |
| 10 | PricingHeadersPEOPricingSegmentCode | PRICING_SEGMENT_CODE | — | ✅ |
| 11 | PricingHeadersPEOPricingSegmentExplanation | PRICING_SEGMENT_EXPLANATION | — | — |
| 12 | PricingHeadersPEOPricingStrategyExplanation | PRICING_STRATEGY_EXPLANATION | — | — |
| 13 | PricingHeadersPEOPricingStrategyId | PRICING_STRATEGY_ID | — | — |
| 14 | PricingHeadersPEORclPricingHeaderId | RCL_PRICING_HEADER_ID | — | ✅ |
| 15 | PricingHeadersPEOSegmentExplanationMsgName | SEGMENT_EXPLANATION_MSG_NAME | — | — |
| 16 | PricingHeadersPEOSoldToPartyId | SOLD_TO_PARTY_ID | — | — |
| 17 | PricingHeadersPEOSourceId | SOURCE_ID | — | — |
| 18 | PricingHeadersPEOSourceType | SOURCE_TYPE | — | — |
| 19 | PricingHeadersPEOStrategyExplanationMsgName | STRATEGY_EXPLANATION_MSG_NAME | — | — |

### [[rcl_service_charges|RCL_SERVICE_CHARGES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ServiceChargesPEOAvgUnitSellingPrice | AVG_UNIT_SELLING_PRICE | — | — |
| 2 | ServiceChargesPEOCanAdjustFlag | CAN_ADJUST_FLAG | — | — |
| 3 | ServiceChargesPEOChargeAppliesTo | CHARGE_APPLIES_TO | — | — |
| 4 | ServiceChargesPEOChargeCurrencyCode1 | CHARGE_CURRENCY_CODE | — | — |
| 5 | ServiceChargesPEOChargeDefinitionCode | CHARGE_DEFINITION_CODE | — | — |
| 6 | ServiceChargesPEOChargeSubtypeCode | CHARGE_SUBTYPE_CODE | — | — |
| 7 | ServiceChargesPEOChargeTypeCode | CHARGE_TYPE_CODE | — | — |
| 8 | ServiceChargesPEOCreatedBy1 | CREATED_BY | — | — |
| 9 | ServiceChargesPEOCreationDate1 | CREATION_DATE | — | — |
| 10 | ServiceChargesPEODeltaType1 | DELTA_TYPE | — | — |
| 11 | ServiceChargesPEOGsaUnitPrice | GSA_UNIT_PRICE | — | — |
| 12 | ServiceChargesPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 13 | ServiceChargesPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 14 | ServiceChargesPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 15 | ServiceChargesPEOModifiedFlag1 | MODIFIED_FLAG | — | — |
| 16 | ServiceChargesPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 17 | ServiceChargesPEOParentEntityCode | PARENT_ENTITY_CODE | — | ✅ |
| 18 | ServiceChargesPEOParentEntityId | PARENT_ENTITY_ID | — | ✅ |
| 19 | ServiceChargesPEOPricePeriodicityCode | PRICE_PERIODICITY_CODE | — | — |
| 20 | ServiceChargesPEOPriceTypeCode | PRICE_TYPE_CODE | — | — |
| 21 | ServiceChargesPEOPricedQuantity | PRICED_QUANTITY | — | — |
| 22 | ServiceChargesPEOPricedQuantityUomCode | PRICED_QUANTITY_UOM_CODE | — | — |
| 23 | ServiceChargesPEOPrimaryFlag | PRIMARY_FLAG | — | — |
| 24 | ServiceChargesPEOReferenceOrderChargeId | REFERENCE_ORDER_CHARGE_ID | — | — |
| 25 | ServiceChargesPEORollupFlag1 | ROLLUP_FLAG | — | — |
| 26 | ServiceChargesPEOSequenceNumber1 | SEQUENCE_NUMBER | — | — |
| 27 | ServiceChargesPEOServiceChargeId1 | SERVICE_CHARGE_ID | — | — |
| 28 | ServiceChargesPEOSourceChargeId1 | SOURCE_CHARGE_ID | — | — |

### [[rcl_service_charge_components|RCL_SERVICE_CHARGE_COMPONENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ServiceChargeComponentsPEOChargeCurrDurationExtAmt | CHARGE_CURR_DURATION_EXT_AMT | — | — |
| 2 | ServiceChargeComponentsPEOChargeCurrencyCode | CHARGE_CURRENCY_CODE | — | — |
| 3 | ServiceChargeComponentsPEOChargeCurrencyExtAmount | CHARGE_CURRENCY_EXT_AMOUNT | — | — |
| 4 | ServiceChargeComponentsPEOChargeCurrencyUnitPrice | CHARGE_CURRENCY_UNIT_PRICE | — | — |
| 5 | ServiceChargeComponentsPEOCoverageProductId | COVERAGE_PRODUCT_ID | — | — |
| 6 | ServiceChargeComponentsPEOCreatedBy | CREATED_BY | — | — |
| 7 | ServiceChargeComponentsPEOCreationDate | CREATION_DATE | — | — |
| 8 | ServiceChargeComponentsPEODeltaType | DELTA_TYPE | — | — |
| 9 | ServiceChargeComponentsPEOExplanation | EXPLANATION | — | — |
| 10 | ServiceChargeComponentsPEOExplanationMessageName | EXPLANATION_MESSAGE_NAME | — | — |
| 11 | ServiceChargeComponentsPEOHeaderCurrDurationExtAmt | HEADER_CURR_DURATION_EXT_AMT | — | — |
| 12 | ServiceChargeComponentsPEOHeaderCurrencyCode | HEADER_CURRENCY_CODE | — | — |
| 13 | ServiceChargeComponentsPEOHeaderCurrencyExtAmount | HEADER_CURRENCY_EXT_AMOUNT | — | ✅ |
| 14 | ServiceChargeComponentsPEOHeaderCurrencyUnitPrice | HEADER_CURRENCY_UNIT_PRICE | — | ✅ |
| 15 | ServiceChargeComponentsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | ServiceChargeComponentsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 17 | ServiceChargeComponentsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 18 | ServiceChargeComponentsPEOModifiedFlag | MODIFIED_FLAG | — | — |
| 19 | ServiceChargeComponentsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | ServiceChargeComponentsPEOParentChargeComponentId | PARENT_CHARGE_COMPONENT_ID | — | — |
| 21 | ServiceChargeComponentsPEOPercentOfComparisonElement | PERCENT_OF_COMPARISON_ELEMENT | — | — |
| 22 | ServiceChargeComponentsPEOPriceElementCode | PRICE_ELEMENT_CODE | — | ✅ |
| 23 | ServiceChargeComponentsPEOPriceElementUsageCode | PRICE_ELEMENT_USAGE_CODE | — | — |
| 24 | ServiceChargeComponentsPEOPricingSourceId | PRICING_SOURCE_ID | — | — |
| 25 | ServiceChargeComponentsPEOPricingSourceTypeCode | PRICING_SOURCE_TYPE_CODE | — | — |
| 26 | ServiceChargeComponentsPEOReferenceSrvChargeCompId | REFERENCE_SRV_CHARGE_COMP_ID | — | — |
| 27 | ServiceChargeComponentsPEORollupFlag | ROLLUP_FLAG | — | — |
| 28 | ServiceChargeComponentsPEOSequenceNumber | SEQUENCE_NUMBER | — | — |
| 29 | ServiceChargeComponentsPEOServiceChargeComponentId | SERVICE_CHARGE_COMPONENT_ID | 🔑 | ✅ |
| 30 | ServiceChargeComponentsPEOServiceChargeId | SERVICE_CHARGE_ID | — | — |
| 31 | ServiceChargeComponentsPEOSourceChargeComponentId | SOURCE_CHARGE_COMPONENT_ID | — | — |
| 32 | ServiceChargeComponentsPEOSourceChargeId | SOURCE_CHARGE_ID | — | — |
| 33 | ServiceChargeComponentsPEOSourceMpaId | SOURCE_MPA_ID | — | — |
| 34 | ServiceChargeComponentsPEOSourceParentChargeCompId | SOURCE_PARENT_CHARGE_COMP_ID | — | — |
| 35 | ServiceChargeComponentsPEOTaxIncludedFlag | TAX_INCLUDED_FLAG | — | — |

### [[svc_service_requests|SVC_SERVICE_REQUESTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ServiceRequestUnsecuredPEOAccountPartyId | ACCOUNT_PARTY_ID | — | — |
| 2 | ServiceRequestUnsecuredPEOAssetId | ASSET_ID | — | — |
| 3 | ServiceRequestUnsecuredPEOAssigneeResourceId | ASSIGNEE_RESOURCE_ID | — | — |
| 4 | ServiceRequestUnsecuredPEOBUOrgId | BU_ORG_ID | — | — |
| 5 | ServiceRequestUnsecuredPEOCatalogId | CATALOG_ID | — | — |
| 6 | ServiceRequestUnsecuredPEOCategoryId | CATEGORY_ID | — | — |
| 7 | ServiceRequestUnsecuredPEOChannelTypeCd | CHANNEL_TYPE_CD | — | — |
| 8 | ServiceRequestUnsecuredPEOClosedDate | CLOSED_DATE | — | — |
| 9 | ServiceRequestUnsecuredPEOCorpCurrencyCode | CORP_CURRENCY_CODE | — | — |
| 10 | ServiceRequestUnsecuredPEOCreatedBy4 | CREATED_BY | — | — |
| 11 | ServiceRequestUnsecuredPEOCreatedByPartyId | CREATED_BY_PARTY_ID | — | — |
| 12 | ServiceRequestUnsecuredPEOCreationDate4 | CREATION_DATE | — | — |
| 13 | ServiceRequestUnsecuredPEOCriticalFlag | CRITICAL_FLAG | — | — |
| 14 | ServiceRequestUnsecuredPEOCurcyConvRateType | CURCY_CONV_RATE_TYPE | — | — |
| 15 | ServiceRequestUnsecuredPEOCurrencyCode | CURRENCY_CODE | — | — |
| 16 | ServiceRequestUnsecuredPEODeletedFlag | DELETED_FLAG | — | — |
| 17 | ServiceRequestUnsecuredPEOIBAssetId | IB_ASSET_ID | — | — |
| 18 | ServiceRequestUnsecuredPEOInternalPriorityCd | INTERNAL_PRIORITY_CD | — | — |
| 19 | ServiceRequestUnsecuredPEOInventoryItemId1 | INVENTORY_ITEM_ID | — | — |
| 20 | ServiceRequestUnsecuredPEOInventoryOrgId | INVENTORY_ORG_ID | — | — |
| 21 | ServiceRequestUnsecuredPEOLanguageCd | LANGUAGE_CD | — | — |
| 22 | ServiceRequestUnsecuredPEOLastReopenDate | LAST_REOPEN_DATE | — | — |
| 23 | ServiceRequestUnsecuredPEOLastResolvedDate | LAST_RESOLVED_DATE | — | — |
| 24 | ServiceRequestUnsecuredPEOLastUpdateDate4 | LAST_UPDATE_DATE | — | ✅ |
| 25 | ServiceRequestUnsecuredPEOLastUpdateLogin4 | LAST_UPDATE_LOGIN | — | — |
| 26 | ServiceRequestUnsecuredPEOLastUpdatedBy4 | LAST_UPDATED_BY | — | — |
| 27 | ServiceRequestUnsecuredPEOObjectVersionNumber4 | OBJECT_VERSION_NUMBER | — | — |
| 28 | ServiceRequestUnsecuredPEOOpenDate | OPEN_DATE | — | — |
| 29 | ServiceRequestUnsecuredPEOOriginalSystemReference | ORIGINAL_SYSTEM_REFERENCE | — | — |
| 30 | ServiceRequestUnsecuredPEOOwnerTypeCd | OWNER_TYPE_CD | — | — |
| 31 | ServiceRequestUnsecuredPEOPartnerAccountPartyId | PARTNER_ACCOUNT_PARTY_ID | — | — |
| 32 | ServiceRequestUnsecuredPEOPrimaryContactPartyId | PRIMARY_CONTACT_PARTY_ID | — | — |
| 33 | ServiceRequestUnsecuredPEOProblemCd | PROBLEM_CD | — | — |
| 34 | ServiceRequestUnsecuredPEOProblemDesc | PROBLEM_DESC | — | — |
| 35 | ServiceRequestUnsecuredPEOProdGroupId | PROD_GROUP_ID | — | — |
| 36 | ServiceRequestUnsecuredPEOQueueId | QUEUE_ID | — | — |
| 37 | ServiceRequestUnsecuredPEOReportedByPartyId | REPORTED_BY_PARTY_ID | — | — |
| 38 | ServiceRequestUnsecuredPEOResolutionCd | RESOLUTION_CD | — | — |
| 39 | ServiceRequestUnsecuredPEOResolveDescription | RESOLVE_DESC | — | — |
| 40 | ServiceRequestUnsecuredPEOResolveOutcomeCd | RESOLVE_OUTCOME_CD | — | — |
| 41 | ServiceRequestUnsecuredPEOResolvedBy | RESOLVED_BY | — | — |
| 42 | ServiceRequestUnsecuredPEOSeverityCd | SEVERITY_CD | — | — |
| 43 | ServiceRequestUnsecuredPEOSourceCd | SOURCE_CD | — | — |
| 44 | ServiceRequestUnsecuredPEOSrCreatedBy | SR_CREATED_BY | — | — |
| 45 | ServiceRequestUnsecuredPEOSrId | SR_ID | — | — |
| 46 | ServiceRequestUnsecuredPEOSrLastUpdateDate | SR_LAST_UPDATE_DATE | — | ✅ |
| 47 | ServiceRequestUnsecuredPEOSrLastUpdateLogin | SR_LAST_UPDATE_LOGIN | — | — |
| 48 | ServiceRequestUnsecuredPEOSrLastUpdatedBy | SR_LAST_UPDATED_BY | — | — |
| 49 | ServiceRequestUnsecuredPEOSrNumber | SR_NUMBER | — | — |
| 50 | ServiceRequestUnsecuredPEOStatusCd | STATUS_CD | — | — |
| 51 | ServiceRequestUnsecuredPEOStatusTypeCd | STATUS_TYPE_CD | — | — |
| 52 | ServiceRequestUnsecuredPEOStripeCd | STRIPE_CD | — | — |
| 53 | ServiceRequestUnsecuredPEOTitle | TITLE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
