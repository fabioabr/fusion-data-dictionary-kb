---
id: DOC-PO-PVO-RequisitionDistributionRefPVO
doc_type: system-doc
title: "RequisitionDistributionRefPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - RequisitionDistributionRefPVO
  - requisitiondistributionrefpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RequisitionDistributionRefPVO

## 📌 Visão Geral

Extrai referências de distribuição de requisições, vinculando alocações a documentos-fonte e projetos. Suporta rastreabilidade completa da cadeia de aprovação e comprometimento de gastos.

**Caminho:** `FscmTopModelAM.PrcPorPublicViewAM.RequisitionDistributionRefPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 1423 | 30 | 1 | 71 | 5% |

---

## 🔗 Tabelas Relacionadas

- [[egp_categories_vl|EGP_CATEGORIES_VL]] — 7 atributos (1 BICC)
- [[egp_system_items_vl|EGP_SYSTEM_ITEMS_VL]] — 6 atributos
- [[fnd_territories_vl|FND_TERRITORIES_VL]] — 2 atributos
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 21 atributos (2 BICC)
- [[hr_locations_all_f_vl|HR_LOCATIONS_ALL_F_VL]] — 4 atributos (1 BICC)
- [[inv_units_of_measure_vl|INV_UNITS_OF_MEASURE_VL]] — 68 atributos (4 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 20 atributos (5 BICC)
- [[per_users|PER_USERS]] — 6 atributos
- [[pon_auction_headers_all|PON_AUCTION_HEADERS_ALL]] — 211 atributos (2 BICC)
- [[pon_auction_item_prices_all|PON_AUCTION_ITEM_PRICES_ALL]] — 93 atributos (1 BICC)
- [[pon_bid_item_prices|PON_BID_ITEM_PRICES]] — 78 atributos (1 BICC)
- [[por_line_locations_sum_v|POR_LINE_LOCATIONS_SUM_V]] — 10 atributos (1 BICC)
- [[por_requisition_headers_all|POR_REQUISITION_HEADERS_ALL]] — 43 atributos (9 BICC)
- [[por_requisition_lines_all|POR_REQUISITION_LINES_ALL]] — 260 atributos (21 BICC)
- [[por_req_distributions_all|POR_REQ_DISTRIBUTIONS_ALL]] — 58 atributos (1 PKs, 12 BICC)
- [[po_action_history|PO_ACTION_HISTORY]] — 7 atributos (2 BICC)
- [[po_hazard_classes_vl|PO_HAZARD_CLASSES_VL]] — 6 atributos
- [[po_headers_all|PO_HEADERS_ALL]] — 232 atributos (4 BICC)
- [[po_lines_all|PO_LINES_ALL]] — 204 atributos (2 BICC)
- [[po_un_numbers_vl|PO_UN_NUMBERS_VL]] — 12 atributos (1 BICC)
- [[po_versions_init_sequence_v|PO_VERSIONS_INIT_SEQUENCE_V]] — 41 atributos (2 BICC)
- [[zx_fc_business_categories_v|ZX_FC_BUSINESS_CATEGORIES_V]] — 8 atributos
- [[zx_fc_document_fiscal_v|ZX_FC_DOCUMENT_FISCAL_V]] — 3 atributos
- [[zx_fc_intended_use_v|ZX_FC_INTENDED_USE_V]] — 2 atributos
- [[zx_fc_product_categories_v|ZX_FC_PRODUCT_CATEGORIES_V]] — 3 atributos
- [[zx_fc_product_fiscal_v|ZX_FC_PRODUCT_FISCAL_V]] — 6 atributos
- [[zx_fc_user_defined_v|ZX_FC_USER_DEFINED_V]] — 3 atributos
- [[zx_input_classifications_v|ZX_INPUT_CLASSIFICATIONS_V]] — 3 atributos
- [[zx_product_types_v|ZX_PRODUCT_TYPES_V]] — 2 atributos
- [[zx_registrations|ZX_REGISTRATIONS]] — 4 atributos

---

## ⚙️ Atributos

### [[egp_categories_vl|EGP_CATEGORIES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CategoryCategoryId | CATEGORY_ID | — | — |
| 2 | CategoryCategoryName | CATEGORY_NAME | — | ✅ |
| 3 | CategoryDescription | DESCRIPTION | — | — |
| 4 | CategoryEnabledFlag | ENABLED_FLAG | — | — |
| 5 | CategoryJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 6 | CategoryJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 7 | CategoryStructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | — |

### [[egp_system_items_vl|EGP_SYSTEM_ITEMS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 2 | ItemInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | — |
| 3 | ItemItemNumber | ITEM_NUMBER | — | — |
| 4 | ItemItemType | ITEM_TYPE | — | — |
| 5 | ItemOrganizationId | ORGANIZATION_ID | — | — |
| 6 | ItemPrimaryUomCode | PRIMARY_UOM_CODE | — | — |

### [[fnd_territories_vl|FND_TERRITORIES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TerritoryPEOTerritoryCode | TERRITORY_CODE | — | — |
| 2 | TerritoryPEOTerritoryShortName | TERRITORY_SHORT_NAME | — | — |

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitId | BU_ID | — | — |
| 2 | CreatedBy | CREATED_BY | — | — |
| 3 | CreationDate | CREATION_DATE | — | — |
| 4 | DateFrom | DATE_FROM | — | — |
| 5 | DateTo | DATE_TO | — | — |
| 6 | DefaultCurrencyCode | DEFAULT_CURRENCY_CODE | — | — |
| 7 | DefaultSetId | DEFAULT_SET_ID | — | — |
| 8 | EnabledForHrFlag | ENABLED_FOR_HR_FLAG | — | — |
| 9 | EnterpriseId | BUSINESS_GROUP_ID | — | — |
| 10 | FinancialsBusinessUnitId | FIN_BUSINESS_UNIT_ID | — | — |
| 11 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | LegalEntityId | LEGAL_ENTITY_ID | — | — |
| 15 | LocationId | LOCATION_ID | — | — |
| 16 | ManagerId | MANAGER_ID | — | — |
| 17 | Name | BU_NAME | — | ✅ |
| 18 | ProfitCenterFlag | PROFIT_CENTER_FLAG | — | — |
| 19 | ReqBUPrimaryLedgerId | PRIMARY_LEDGER_ID | — | — |
| 20 | ShortCode | SHORT_CODE | — | — |
| 21 | Status | STATUS | — | — |

### [[hr_locations_all_f_vl|HR_LOCATIONS_ALL_F_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FinalDischargeLocationEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | FinalDischargeLocationEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | FinalDischargeLocationLocationCode | LOCATION_CODE | — | — |
| 4 | FinalDischargeLocationLocationId | LOCATION_ID | — | — |

### [[inv_units_of_measure_vl|INV_UNITS_OF_MEASURE_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SecondaryUnitOfMeasureAttribute1 | ATTRIBUTE1 | — | — |
| 2 | SecondaryUnitOfMeasureAttribute10 | ATTRIBUTE10 | — | — |
| 3 | SecondaryUnitOfMeasureAttribute11 | ATTRIBUTE11 | — | — |
| 4 | SecondaryUnitOfMeasureAttribute12 | ATTRIBUTE12 | — | — |
| 5 | SecondaryUnitOfMeasureAttribute13 | ATTRIBUTE13 | — | — |
| 6 | SecondaryUnitOfMeasureAttribute14 | ATTRIBUTE14 | — | — |
| 7 | SecondaryUnitOfMeasureAttribute15 | ATTRIBUTE15 | — | — |
| 8 | SecondaryUnitOfMeasureAttribute2 | ATTRIBUTE2 | — | — |
| 9 | SecondaryUnitOfMeasureAttribute3 | ATTRIBUTE3 | — | — |
| 10 | SecondaryUnitOfMeasureAttribute4 | ATTRIBUTE4 | — | — |
| 11 | SecondaryUnitOfMeasureAttribute5 | ATTRIBUTE5 | — | — |
| 12 | SecondaryUnitOfMeasureAttribute6 | ATTRIBUTE6 | — | — |
| 13 | SecondaryUnitOfMeasureAttribute7 | ATTRIBUTE7 | — | — |
| 14 | SecondaryUnitOfMeasureAttribute8 | ATTRIBUTE8 | — | — |
| 15 | SecondaryUnitOfMeasureAttribute9 | ATTRIBUTE9 | — | — |
| 16 | SecondaryUnitOfMeasureAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 17 | SecondaryUnitOfMeasureBaseUomFlag | BASE_UOM_FLAG | — | — |
| 18 | SecondaryUnitOfMeasureCreatedBy | CREATED_BY | — | — |
| 19 | SecondaryUnitOfMeasureCreationDate | CREATION_DATE | — | — |
| 20 | SecondaryUnitOfMeasureDescription | DESCRIPTION | — | — |
| 21 | SecondaryUnitOfMeasureDisableDate | DISABLE_DATE | — | — |
| 22 | SecondaryUnitOfMeasureJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 23 | SecondaryUnitOfMeasureJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 24 | SecondaryUnitOfMeasureLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 25 | SecondaryUnitOfMeasureLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 26 | SecondaryUnitOfMeasureLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 27 | SecondaryUnitOfMeasureObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 28 | SecondaryUnitOfMeasureRequestId | REQUEST_ID | — | — |
| 29 | SecondaryUnitOfMeasureStandardPackFlag | STANDARD_PACK_FLAG | — | — |
| 30 | SecondaryUnitOfMeasureUnitOfMeasure | UNIT_OF_MEASURE | — | — |
| 31 | SecondaryUnitOfMeasureUomClass | UOM_CLASS | — | — |
| 32 | SecondaryUnitOfMeasureUomCode | UOM_CODE | — | — |
| 33 | SecondaryUnitOfMeasureUomPluralDesc | UOM_PLURAL_DESC | — | — |
| 34 | SecondaryUnitOfMeasureUomReciprocalDesc | UOM_RECIPROCAL_DESC | — | — |
| 35 | UnitOfMeasureAttribute1 | ATTRIBUTE1 | — | — |
| 36 | UnitOfMeasureAttribute10 | ATTRIBUTE10 | — | — |
| 37 | UnitOfMeasureAttribute11 | ATTRIBUTE11 | — | — |
| 38 | UnitOfMeasureAttribute12 | ATTRIBUTE12 | — | — |
| 39 | UnitOfMeasureAttribute13 | ATTRIBUTE13 | — | — |
| 40 | UnitOfMeasureAttribute14 | ATTRIBUTE14 | — | — |
| 41 | UnitOfMeasureAttribute15 | ATTRIBUTE15 | — | — |
| 42 | UnitOfMeasureAttribute2 | ATTRIBUTE2 | — | — |
| 43 | UnitOfMeasureAttribute3 | ATTRIBUTE3 | — | — |
| 44 | UnitOfMeasureAttribute4 | ATTRIBUTE4 | — | — |
| 45 | UnitOfMeasureAttribute5 | ATTRIBUTE5 | — | — |
| 46 | UnitOfMeasureAttribute6 | ATTRIBUTE6 | — | — |
| 47 | UnitOfMeasureAttribute7 | ATTRIBUTE7 | — | — |
| 48 | UnitOfMeasureAttribute8 | ATTRIBUTE8 | — | — |
| 49 | UnitOfMeasureAttribute9 | ATTRIBUTE9 | — | — |
| 50 | UnitOfMeasureAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 51 | UnitOfMeasureBaseUomFlag | BASE_UOM_FLAG | — | — |
| 52 | UnitOfMeasureCreatedBy | CREATED_BY | — | — |
| 53 | UnitOfMeasureCreationDate | CREATION_DATE | — | — |
| 54 | UnitOfMeasureDescription | DESCRIPTION | — | ✅ |
| 55 | UnitOfMeasureDisableDate | DISABLE_DATE | — | — |
| 56 | UnitOfMeasureJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 57 | UnitOfMeasureJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 58 | UnitOfMeasureLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 59 | UnitOfMeasureLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 60 | UnitOfMeasureLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 61 | UnitOfMeasureObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 62 | UnitOfMeasureRequestId | REQUEST_ID | — | — |
| 63 | UnitOfMeasureStandardPackFlag | STANDARD_PACK_FLAG | — | — |
| 64 | UnitOfMeasureUnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |
| 65 | UnitOfMeasureUomClass | UOM_CLASS | — | — |
| 66 | UnitOfMeasureUomCode | UOM_CODE | — | — |
| 67 | UnitOfMeasureUomPluralDesc | UOM_PLURAL_DESC | — | — |
| 68 | UnitOfMeasureUomReciprocalDesc | UOM_RECIPROCAL_DESC | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | EffectiveEndDate2 | EFFECTIVE_END_DATE | — | — |
| 3 | EffectiveEndDate3 | EFFECTIVE_END_DATE | — | — |
| 4 | EffectiveEndDate4 | EFFECTIVE_END_DATE | — | — |
| 5 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 6 | EffectiveStartDate2 | EFFECTIVE_START_DATE | — | ✅ |
| 7 | EffectiveStartDate3 | EFFECTIVE_START_DATE | — | ✅ |
| 8 | EffectiveStartDate4 | EFFECTIVE_START_DATE | — | ✅ |
| 9 | PersonNameDisplayNameReqDistLastUpdatedBy | DISPLAY_NAME | — | — |
| 10 | PersonNameDisplayNameReqHeaderLastUpdatedBy | DISPLAY_NAME | — | — |
| 11 | PersonNameDisplayNameReqLineLastUpdatedBy | DISPLAY_NAME | — | — |
| 12 | PersonNameId | PERSON_NAME_ID | — | — |
| 13 | PersonNameId1 | PERSON_NAME_ID | — | — |
| 14 | PersonNameId2 | PERSON_NAME_ID | — | — |
| 15 | PersonNameId3 | PERSON_NAME_ID | — | — |
| 16 | PersonNameSuggestedBuyerEffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 17 | PersonNameSuggestedBuyerEffectiveStartDate1 | EFFECTIVE_START_DATE | — | — |
| 18 | PersonNameSuggestedBuyerListName | LIST_NAME | — | — |
| 19 | PersonNameSuggestedBuyerPersonNameId1 | PERSON_NAME_ID | — | — |
| 20 | RequisitionHeaderCanceledBy | LIST_NAME | — | ✅ |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserId | USER_ID | — | — |
| 2 | UserId1 | USER_ID | — | — |
| 3 | UserId2 | USER_ID | — | — |
| 4 | UserUsernameReqDistLastUpdatedBy | USERNAME | — | — |
| 5 | UserUsernameReqHeaderLastUpdatedBy | USERNAME | — | — |
| 6 | UserUsernameReqLineLastUpdatedBy | USERNAME | — | — |

### [[pon_auction_headers_all|PON_AUCTION_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NegotiationHeaderAbstractDetails | ABSTRACT_DETAILS | — | — |
| 2 | NegotiationHeaderAbstractStatus | ABSTRACT_STATUS | — | — |
| 3 | NegotiationHeaderAdvanceNegotiableFlag | ADVANCE_NEGOTIABLE_FLAG | — | — |
| 4 | NegotiationHeaderAllowOtherBidCurrencyFlag | ALLOW_OTHER_BID_CURRENCY_FLAG | — | — |
| 5 | NegotiationHeaderAmendmentDescription | AMENDMENT_DESCRIPTION | — | — |
| 6 | NegotiationHeaderAmendmentNumber | AMENDMENT_NUMBER | — | — |
| 7 | NegotiationHeaderApprovalStatus | NEG_APPROVAL_STATUS | — | — |
| 8 | NegotiationHeaderAttributeLineNumber | ATTRIBUTE_LINE_NUMBER | — | — |
| 9 | NegotiationHeaderAttributesExist | ATTRIBUTES_EXIST | — | — |
| 10 | NegotiationHeaderAuctionHeaderId | AUCTION_HEADER_ID | — | — |
| 11 | NegotiationHeaderAuctionHeaderIdOrigAmend | AUCTION_HEADER_ID_ORIG_AMEND | — | — |
| 12 | NegotiationHeaderAuctionHeaderIdOrigRound | AUCTION_HEADER_ID_ORIG_ROUND | — | — |
| 13 | NegotiationHeaderAuctionHeaderIdPrevAmend | AUCTION_HEADER_ID_PREV_AMEND | — | — |
| 14 | NegotiationHeaderAuctionHeaderIdPrevRound | AUCTION_HEADER_ID_PREV_ROUND | — | — |
| 15 | NegotiationHeaderAuctionOriginationCode | AUCTION_ORIGINATION_CODE | — | — |
| 16 | NegotiationHeaderAuctionRoundNumber | AUCTION_ROUND_NUMBER | — | — |
| 17 | NegotiationHeaderAuctionStatus | AUCTION_STATUS | — | — |
| 18 | NegotiationHeaderAuctionTitle | AUCTION_TITLE | — | — |
| 19 | NegotiationHeaderAutoExtendAllLinesFlag | AUTO_EXTEND_ALL_LINES_FLAG | — | — |
| 20 | NegotiationHeaderAutoExtendDuration | AUTO_EXTEND_DURATION | — | — |
| 21 | NegotiationHeaderAutoExtendEnabledFlag | AUTO_EXTEND_ENABLED_FLAG | — | — |
| 22 | NegotiationHeaderAutoExtendFlag | AUTO_EXTEND_FLAG | — | — |
| 23 | NegotiationHeaderAutoExtendMinTriggerRank | AUTO_EXTEND_MIN_TRIGGER_RANK | — | — |
| 24 | NegotiationHeaderAutoExtendNumber | AUTO_EXTEND_NUMBER | — | — |
| 25 | NegotiationHeaderAutoExtendTypeFlag | AUTO_EXTEND_TYPE_FLAG | — | — |
| 26 | NegotiationHeaderAutoextendChangedFlag | AUTOEXTEND_CHANGED_FLAG | — | — |
| 27 | NegotiationHeaderAwardApprAmeTransId | AWARD_APPR_AME_TRANS_ID | — | — |
| 28 | NegotiationHeaderAwardApprAmeTransPrevId | AWARD_APPR_AME_TRANS_PREV_ID | — | — |
| 29 | NegotiationHeaderAwardApprAmeTxnDate | AWARD_APPR_AME_TXN_DATE | — | — |
| 30 | NegotiationHeaderAwardApprovalFlag | AWARD_APPROVAL_FLAG | — | — |
| 31 | NegotiationHeaderAwardApprovalStatus | AWARD_APPROVAL_STATUS | — | — |
| 32 | NegotiationHeaderAwardByDate | AWARD_BY_DATE | — | — |
| 33 | NegotiationHeaderAwardCompleteDate | AWARD_COMPLETE_DATE | — | — |
| 34 | NegotiationHeaderAwardDate | AWARD_DATE | — | — |
| 35 | NegotiationHeaderAwardMode | AWARD_MODE | — | — |
| 36 | NegotiationHeaderAwardStatus | AWARD_STATUS | — | — |
| 37 | NegotiationHeaderBidDecrementMethod | BID_DECREMENT_METHOD | — | — |
| 38 | NegotiationHeaderBidFrequencyCode | BID_FREQUENCY_CODE | — | — |
| 39 | NegotiationHeaderBidListType | BID_LIST_TYPE | — | — |
| 40 | NegotiationHeaderBidRanking | BID_RANKING | — | — |
| 41 | NegotiationHeaderBidScopeCode | BID_SCOPE_CODE | — | — |
| 42 | NegotiationHeaderBidVisibilityCode | BID_VISIBILITY_CODE | — | — |
| 43 | NegotiationHeaderCancelDate | CANCEL_DATE | — | — |
| 44 | NegotiationHeaderCarrierId | CARRIER_ID | — | — |
| 45 | NegotiationHeaderCloseBiddingDate | CLOSE_BIDDING_DATE | — | — |
| 46 | NegotiationHeaderCompleteFlag | COMPLETE_FLAG | — | — |
| 47 | NegotiationHeaderContermsArticlesUpdDate | CONTERMS_ARTICLES_UPD_DATE | — | — |
| 48 | NegotiationHeaderContermsDelivUpdDate | CONTERMS_DELIV_UPD_DATE | — | — |
| 49 | NegotiationHeaderContermsExistFlag | CONTERMS_EXIST_FLAG | — | — |
| 50 | NegotiationHeaderContractTemplateId | CONTRACT_TEMPLATE_ID | — | — |
| 51 | NegotiationHeaderContractType | CONTRACT_TYPE | — | — |
| 52 | NegotiationHeaderCreatedBy | CREATED_BY | — | — |
| 53 | NegotiationHeaderCreationDate | CREATION_DATE | — | — |
| 54 | NegotiationHeaderCreationDateOrigAmend | CREATION_DATE_ORIG_AMEND | — | — |
| 55 | NegotiationHeaderCurrencyCode | CURRENCY_CODE | — | — |
| 56 | NegotiationHeaderDescription | DESCRIPTION | — | — |
| 57 | NegotiationHeaderDisplayBestPriceBlindFlag | DISPLAY_BEST_PRICE_BLIND_FLAG | — | — |
| 58 | NegotiationHeaderDoctypeId | DOCTYPE_ID | — | — |
| 59 | NegotiationHeaderDocumentNumber | DOCUMENT_NUMBER | — | ✅ |
| 60 | NegotiationHeaderDraftLocked | DRAFT_LOCKED | — | — |
| 61 | NegotiationHeaderDraftLockedDate | DRAFT_LOCKED_DATE | — | — |
| 62 | NegotiationHeaderDraftUnlockedDate | DRAFT_UNLOCKED_DATE | — | — |
| 63 | NegotiationHeaderEnforcePrevrndBidPriceFlag | ENFORCE_PREVRND_BID_PRICE_FLAG | — | — |
| 64 | NegotiationHeaderEventId | EVENT_ID | — | — |
| 65 | NegotiationHeaderEventTitle | EVENT_TITLE | — | — |
| 66 | NegotiationHeaderExtAttribute1 | EXT_ATTRIBUTE1 | — | — |
| 67 | NegotiationHeaderExtAttribute10 | EXT_ATTRIBUTE10 | — | — |
| 68 | NegotiationHeaderExtAttribute11 | EXT_ATTRIBUTE11 | — | — |
| 69 | NegotiationHeaderExtAttribute12 | EXT_ATTRIBUTE12 | — | — |
| 70 | NegotiationHeaderExtAttribute13 | EXT_ATTRIBUTE13 | — | — |
| 71 | NegotiationHeaderExtAttribute14 | EXT_ATTRIBUTE14 | — | — |
| 72 | NegotiationHeaderExtAttribute15 | EXT_ATTRIBUTE15 | — | — |
| 73 | NegotiationHeaderExtAttribute2 | EXT_ATTRIBUTE2 | — | — |
| 74 | NegotiationHeaderExtAttribute3 | EXT_ATTRIBUTE3 | — | — |
| 75 | NegotiationHeaderExtAttribute4 | EXT_ATTRIBUTE4 | — | — |
| 76 | NegotiationHeaderExtAttribute5 | EXT_ATTRIBUTE5 | — | — |
| 77 | NegotiationHeaderExtAttribute6 | EXT_ATTRIBUTE6 | — | — |
| 78 | NegotiationHeaderExtAttribute7 | EXT_ATTRIBUTE7 | — | — |
| 79 | NegotiationHeaderExtAttribute8 | EXT_ATTRIBUTE8 | — | — |
| 80 | NegotiationHeaderExtAttribute9 | EXT_ATTRIBUTE9 | — | — |
| 81 | NegotiationHeaderExtAttributeCategory | EXT_ATTRIBUTE_CATEGORY | — | — |
| 82 | NegotiationHeaderFirstLineCloseDate | FIRST_LINE_CLOSE_DATE | — | — |
| 83 | NegotiationHeaderFobCode | FOB_CODE | — | — |
| 84 | NegotiationHeaderFreightTermsCode | FREIGHT_TERMS_CODE | — | — |
| 85 | NegotiationHeaderFullQuantityBidCode | FULL_QUANTITY_BID_CODE | — | — |
| 86 | NegotiationHeaderGlobalTemplateFlag | GLOBAL_TEMPLATE_FLAG | — | — |
| 87 | NegotiationHeaderGroupEnabledFlag | GROUP_ENABLED_FLAG | — | — |
| 88 | NegotiationHeaderHasHdrAttrFlag | HAS_HDR_ATTR_FLAG | — | — |
| 89 | NegotiationHeaderHasItemsFlag | HAS_ITEMS_FLAG | — | — |
| 90 | NegotiationHeaderHasPeForAllItems | HAS_PE_FOR_ALL_ITEMS | — | — |
| 91 | NegotiationHeaderHasPriceElements | HAS_PRICE_ELEMENTS | — | — |
| 92 | NegotiationHeaderHasScoringTeamsFlag | HAS_SCORING_TEAMS_FLAG | — | — |
| 93 | NegotiationHeaderHdrAttrDisplayScore | HDR_ATTR_DISPLAY_SCORE | — | — |
| 94 | NegotiationHeaderHdrAttrEnableWeights | HDR_ATTR_ENABLE_WEIGHTS | — | — |
| 95 | NegotiationHeaderHdrAttrMaximumScore | HDR_ATTR_MAXIMUM_SCORE | — | — |
| 96 | NegotiationHeaderHdrAttributeEnabledFlag | HDR_ATTRIBUTE_ENABLED_FLAG | — | — |
| 97 | NegotiationHeaderImportFileName | IMPORT_FILE_NAME | — | — |
| 98 | NegotiationHeaderIncludePdfInExternalPage | INCLUDE_PDF_IN_EXTERNAL_PAGE | — | — |
| 99 | NegotiationHeaderIntAttribute1 | INT_ATTRIBUTE1 | — | — |
| 100 | NegotiationHeaderIntAttribute10 | INT_ATTRIBUTE10 | — | — |
| 101 | NegotiationHeaderIntAttribute11 | INT_ATTRIBUTE11 | — | — |
| 102 | NegotiationHeaderIntAttribute12 | INT_ATTRIBUTE12 | — | — |
| 103 | NegotiationHeaderIntAttribute13 | INT_ATTRIBUTE13 | — | — |
| 104 | NegotiationHeaderIntAttribute14 | INT_ATTRIBUTE14 | — | — |
| 105 | NegotiationHeaderIntAttribute15 | INT_ATTRIBUTE15 | — | — |
| 106 | NegotiationHeaderIntAttribute2 | INT_ATTRIBUTE2 | — | — |
| 107 | NegotiationHeaderIntAttribute3 | INT_ATTRIBUTE3 | — | — |
| 108 | NegotiationHeaderIntAttribute4 | INT_ATTRIBUTE4 | — | — |
| 109 | NegotiationHeaderIntAttribute5 | INT_ATTRIBUTE5 | — | — |
| 110 | NegotiationHeaderIntAttribute6 | INT_ATTRIBUTE6 | — | — |
| 111 | NegotiationHeaderIntAttribute7 | INT_ATTRIBUTE7 | — | — |
| 112 | NegotiationHeaderIntAttribute8 | INT_ATTRIBUTE8 | — | — |
| 113 | NegotiationHeaderIntAttribute9 | INT_ATTRIBUTE9 | — | — |
| 114 | NegotiationHeaderIntAttributeCategory | INT_ATTRIBUTE_CATEGORY | — | — |
| 115 | NegotiationHeaderIsPaused | IS_PAUSED | — | — |
| 116 | NegotiationHeaderIsTemplateFlag | IS_TEMPLATE_FLAG | — | — |
| 117 | NegotiationHeaderLanguageCode | LANGUAGE_CODE | — | — |
| 118 | NegotiationHeaderLargeNegEnabledFlag | LARGE_NEG_ENABLED_FLAG | — | — |
| 119 | NegotiationHeaderLastLineNumber | LAST_LINE_NUMBER | — | — |
| 120 | NegotiationHeaderLastPauseDate | LAST_PAUSE_DATE | — | — |
| 121 | NegotiationHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 122 | NegotiationHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 123 | NegotiationHeaderLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 124 | NegotiationHeaderLineAttributeEnabledFlag | LINE_ATTRIBUTE_ENABLED_FLAG | — | — |
| 125 | NegotiationHeaderLineMasEnabledFlag | LINE_MAS_ENABLED_FLAG | — | — |
| 126 | NegotiationHeaderLotEnabledFlag | LOT_ENABLED_FLAG | — | — |
| 127 | NegotiationHeaderMaxBidColorSequenceId | MAX_BID_COLOR_SEQUENCE_ID | — | — |
| 128 | NegotiationHeaderMaxDocumentLineNum | MAX_DOCUMENT_LINE_NUM | — | — |
| 129 | NegotiationHeaderMaxInternalLineNum | MAX_INTERNAL_LINE_NUM | — | — |
| 130 | NegotiationHeaderMaxRetainageNegotiableFlag | MAX_RETAINAGE_NEGOTIABLE_FLAG | — | — |
| 131 | NegotiationHeaderMinBidChangeType | MIN_BID_CHANGE_TYPE | — | — |
| 132 | NegotiationHeaderMinBidDecrement | MIN_BID_DECREMENT | — | — |
| 133 | NegotiationHeaderNegTeamEnabledFlag | NEG_TEAM_ENABLED_FLAG | — | — |
| 134 | NegotiationHeaderNumberOfBids | NUMBER_OF_BIDS | — | — |
| 135 | NegotiationHeaderNumberOfExtensions | NUMBER_OF_EXTENSIONS | — | — |
| 136 | NegotiationHeaderNumberOfLines | NUMBER_OF_LINES | — | — |
| 137 | NegotiationHeaderNumberPriceDecimals | NUMBER_PRICE_DECIMALS | — | — |
| 138 | NegotiationHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 139 | NegotiationHeaderOpenAuctionNowFlag | OPEN_AUCTION_NOW_FLAG | — | — |
| 140 | NegotiationHeaderOpenBiddingDate | OPEN_BIDDING_DATE | — | — |
| 141 | NegotiationHeaderOriginalCloseBiddingDate | ORIGINAL_CLOSE_BIDDING_DATE | — | — |
| 142 | NegotiationHeaderOutcomeStatus | OUTCOME_STATUS | — | — |
| 143 | NegotiationHeaderPauseRemarks | PAUSE_REMARKS | — | — |
| 144 | NegotiationHeaderPaymentTermsId | PAYMENT_TERMS_ID | — | — |
| 145 | NegotiationHeaderPersonId | PERSON_ID | — | — |
| 146 | NegotiationHeaderPfTypeAllowed | PF_TYPE_ALLOWED | — | — |
| 147 | NegotiationHeaderPoAgreedAmount | PO_AGREED_AMOUNT | — | — |
| 148 | NegotiationHeaderPoEndDate | PO_END_DATE | — | — |
| 149 | NegotiationHeaderPoMinRelAmount | PO_MIN_REL_AMOUNT | — | — |
| 150 | NegotiationHeaderPoStartDate | PO_START_DATE | — | — |
| 151 | NegotiationHeaderPoStyleId | PO_STYLE_ID | — | — |
| 152 | NegotiationHeaderPowerBiddingEnabledFlag | POWER_BIDDING_ENABLED_FLAG | — | — |
| 153 | NegotiationHeaderPrcBuId | PRC_BU_ID | — | — |
| 154 | NegotiationHeaderPriceDrivenAuctionFlag | PRICE_DRIVEN_AUCTION_FLAG | — | — |
| 155 | NegotiationHeaderPriceElementEnabledFlag | PRICE_ELEMENT_ENABLED_FLAG | — | — |
| 156 | NegotiationHeaderPriceTiersIndicator | PRICE_TIERS_INDICATOR | — | — |
| 157 | NegotiationHeaderProgramAppName | PROGRAM_APP_NAME | — | — |
| 158 | NegotiationHeaderProgramName | PROGRAM_NAME | — | — |
| 159 | NegotiationHeaderProgressPaymentType | PROGRESS_PAYMENT_TYPE | — | — |
| 160 | NegotiationHeaderProgressPymtNegotiableFlag | PROGRESS_PYMT_NEGOTIABLE_FLAG | — | — |
| 161 | NegotiationHeaderProjectId | PROJECT_ID | — | — |
| 162 | NegotiationHeaderProxyBiddingEnabledFlag | PROXY_BIDDING_ENABLED_FLAG | — | — |
| 163 | NegotiationHeaderPublishAuctionNowFlag | PUBLISH_AUCTION_NOW_FLAG | — | — |
| 164 | NegotiationHeaderPublishDate | PUBLISH_DATE | — | — |
| 165 | NegotiationHeaderPublishDateOrigAmend | PUBLISH_DATE_ORIG_AMEND | — | — |
| 166 | NegotiationHeaderPublishRatesToBiddersFlag | PUBLISH_RATES_TO_BIDDERS_FLAG | — | — |
| 167 | NegotiationHeaderQtyPriceTiersEnabledFlag | QTY_PRICE_TIERS_ENABLED_FLAG | — | — |
| 168 | NegotiationHeaderRankIndicator | RANK_INDICATOR | — | — |
| 169 | NegotiationHeaderRateDate | RATE_DATE | — | — |
| 170 | NegotiationHeaderRateType | RATE_TYPE | — | — |
| 171 | NegotiationHeaderRecoupmentNegotiableFlag | RECOUPMENT_NEGOTIABLE_FLAG | — | — |
| 172 | NegotiationHeaderReminderDate | REMINDER_DATE | — | — |
| 173 | NegotiationHeaderRequestDate | REQUEST_DATE | — | — |
| 174 | NegotiationHeaderRequestId | REQUEST_ID | — | — |
| 175 | NegotiationHeaderRequestedBy | REQUESTED_BY | — | — |
| 176 | NegotiationHeaderRetainageNegotiableFlag | RETAINAGE_NEGOTIABLE_FLAG | — | — |
| 177 | NegotiationHeaderRfiLineEnabledFlag | RFI_LINE_ENABLED_FLAG | — | — |
| 178 | NegotiationHeaderScoringLockDate | SCORING_LOCK_DATE | — | — |
| 179 | NegotiationHeaderSealedActualUnlockDate | SEALED_ACTUAL_UNLOCK_DATE | — | — |
| 180 | NegotiationHeaderSealedActualUnsealDate | SEALED_ACTUAL_UNSEAL_DATE | — | — |
| 181 | NegotiationHeaderSealedAuctionStatus | SEALED_AUCTION_STATUS | — | — |
| 182 | NegotiationHeaderShareAwardDecision | SHARE_AWARD_DECISION | — | — |
| 183 | NegotiationHeaderShowBidderNotes | SHOW_BIDDER_NOTES | — | — |
| 184 | NegotiationHeaderShowBidderScores | SHOW_BIDDER_SCORES | — | — |
| 185 | NegotiationHeaderSourceDocId | SOURCE_DOC_ID | — | — |
| 186 | NegotiationHeaderSourceDocLineMsg | SOURCE_DOC_LINE_MSG | — | — |
| 187 | NegotiationHeaderSourceDocMsg | SOURCE_DOC_MSG | — | — |
| 188 | NegotiationHeaderSourceDocMsgApp | SOURCE_DOC_MSG_APP | — | — |
| 189 | NegotiationHeaderSourceDocNumber | SOURCE_DOC_NUMBER | — | — |
| 190 | NegotiationHeaderSourceReqsFlag | SOURCE_REQS_FLAG | — | — |
| 191 | NegotiationHeaderStaggeredClosingInterval | STAGGERED_CLOSING_INTERVAL | — | — |
| 192 | NegotiationHeaderStyleId | STYLE_ID | — | — |
| 193 | NegotiationHeaderSupplierEnterablePymtFlag | SUPPLIER_ENTERABLE_PYMT_FLAG | — | — |
| 194 | NegotiationHeaderSupplierViewType | SUPPLIER_VIEW_TYPE | — | — |
| 195 | NegotiationHeaderTeamScoringEnabledFlag | TEAM_SCORING_ENABLED_FLAG | — | — |
| 196 | NegotiationHeaderTechnicalActualUnlockDate | TECHNICAL_ACTUAL_UNLOCK_DATE | — | — |
| 197 | NegotiationHeaderTechnicalActualUnsealDate | TECHNICAL_ACTUAL_UNSEAL_DATE | — | — |
| 198 | NegotiationHeaderTechnicalEvaluationStatus | TECHNICAL_EVALUATION_STATUS | — | — |
| 199 | NegotiationHeaderTechnicalLockStatus | TECHNICAL_LOCK_STATUS | — | — |
| 200 | NegotiationHeaderTemplateId | TEMPLATE_ID | — | — |
| 201 | NegotiationHeaderTemplateScope | TEMPLATE_SCOPE | — | — |
| 202 | NegotiationHeaderTemplateStatus | TEMPLATE_STATUS | — | — |
| 203 | NegotiationHeaderTwoPartFlag | TWO_PART_FLAG | — | — |
| 204 | NegotiationHeaderVersionNum | VERSION_NUM | — | — |
| 205 | NegotiationHeaderViewByDate | VIEW_BY_DATE | — | — |
| 206 | NegotiationHeaderWfApprovalItemKey | WF_APPROVAL_ITEM_KEY | — | — |
| 207 | NegotiationHeaderWfAwardApprovalItemKey | WF_AWARD_APPROVAL_ITEM_KEY | — | — |
| 208 | NegotiationHeaderWfItemKey | WF_ITEM_KEY | — | — |
| 209 | NegotiationHeaderWfPoncomplCurrentRound | WF_PONCOMPL_CURRENT_ROUND | — | — |
| 210 | NegotiationHeaderWfPoncomplItemKey | WF_PONCOMPL_ITEM_KEY | — | — |
| 211 | NegotiationHeaderWfRoleName | WF_ROLE_NAME | — | — |

### [[pon_auction_item_prices_all|PON_AUCTION_ITEM_PRICES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NegotiationLineAdditionalJobDetails | ADDITIONAL_JOB_DETAILS | — | — |
| 2 | NegotiationLineAdvanceAmount | ADVANCE_AMOUNT | — | — |
| 3 | NegotiationLineAllocationStatus | ALLOCATION_STATUS | — | — |
| 4 | NegotiationLineAuctionHeaderId | AUCTION_HEADER_ID | — | — |
| 5 | NegotiationLineAwardMode | AWARD_MODE | — | — |
| 6 | NegotiationLineAwardStatus | AWARD_STATUS | — | — |
| 7 | NegotiationLineAwardedQuantity | AWARDED_QUANTITY | — | — |
| 8 | NegotiationLineBestBidBidCurrencyCode | BEST_BID_BID_CURRENCY_CODE | — | — |
| 9 | NegotiationLineBestBidBidCurrencyPrice | BEST_BID_BID_CURRENCY_PRICE | — | — |
| 10 | NegotiationLineBestBidBidNumber | BEST_BID_BID_NUMBER | — | — |
| 11 | NegotiationLineBestBidBidPrice | BEST_BID_BID_PRICE | — | — |
| 12 | NegotiationLineBestBidCurrencyCode | BEST_BID_CURRENCY_CODE | — | — |
| 13 | NegotiationLineBestBidCurrencyPrice | BEST_BID_CURRENCY_PRICE | — | — |
| 14 | NegotiationLineBestBidFirstBidPrice | BEST_BID_FIRST_BID_PRICE | — | — |
| 15 | NegotiationLineBestBidNumber | BEST_BID_NUMBER | — | — |
| 16 | NegotiationLineBestBidPrice | BEST_BID_PRICE | — | — |
| 17 | NegotiationLineBestBidPromisedDate | BEST_BID_PROMISED_DATE | — | — |
| 18 | NegotiationLineBestBidProxyLimitPrice | BEST_BID_PROXY_LIMIT_PRICE | — | — |
| 19 | NegotiationLineBestBidQuantity | BEST_BID_QUANTITY | — | — |
| 20 | NegotiationLineBestBidScore | BEST_BID_SCORE | — | — |
| 21 | NegotiationLineBidStartPrice | BID_START_PRICE | — | — |
| 22 | NegotiationLineCategoryId | CATEGORY_ID | — | — |
| 23 | NegotiationLineCloseBiddingDate | CLOSE_BIDDING_DATE | — | — |
| 24 | NegotiationLineCreatedBy | CREATED_BY | — | — |
| 25 | NegotiationLineCreationDate | CREATION_DATE | — | — |
| 26 | NegotiationLineCurrentPrice | CURRENT_PRICE | — | — |
| 27 | NegotiationLineDifferentialResponseType | DIFFERENTIAL_RESPONSE_TYPE | — | — |
| 28 | NegotiationLineDispLineNumber | DISP_LINE_NUMBER | — | — |
| 29 | NegotiationLineDisplayTargetPriceFlag | DISPLAY_TARGET_PRICE_FLAG | — | — |
| 30 | NegotiationLineDocumentDispLineNumber | DOCUMENT_DISP_LINE_NUMBER | — | — |
| 31 | NegotiationLineGroupType | GROUP_TYPE | — | — |
| 32 | NegotiationLineHasAttributesFlag | HAS_ATTRIBUTES_FLAG | — | — |
| 33 | NegotiationLineHasBuyerPfsFlag | HAS_BUYER_PFS_FLAG | — | — |
| 34 | NegotiationLineHasPaymentsFlag | HAS_PAYMENTS_FLAG | — | — |
| 35 | NegotiationLineHasPriceDifferentialsFlag | HAS_PRICE_DIFFERENTIALS_FLAG | — | — |
| 36 | NegotiationLineHasPriceElementsFlag | HAS_PRICE_ELEMENTS_FLAG | — | — |
| 37 | NegotiationLineHasQuantityTiers | HAS_QUANTITY_TIERS | — | — |
| 38 | NegotiationLineHasShipmentsFlag | HAS_SHIPMENTS_FLAG | — | — |
| 39 | NegotiationLineItemDescription | ITEM_DESCRIPTION | — | — |
| 40 | NegotiationLineItemId | ITEM_ID | — | — |
| 41 | NegotiationLineItemRevision | ITEM_REVISION | — | — |
| 42 | NegotiationLineJobId | JOB_ID | — | — |
| 43 | NegotiationLineLastAmendmentUpdate | LAST_AMENDMENT_UPDATE | — | — |
| 44 | NegotiationLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 45 | NegotiationLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 46 | NegotiationLineLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 47 | NegotiationLineLineNumber | LINE_NUMBER | — | — |
| 48 | NegotiationLineLineOriginationCode | LINE_ORIGINATION_CODE | — | — |
| 49 | NegotiationLineLineTypeId | LINE_TYPE_ID | — | — |
| 50 | NegotiationLineMaxRetainageAmount | MAX_RETAINAGE_AMOUNT | — | — |
| 51 | NegotiationLineMaxSubLineSequenceNumber | MAX_SUB_LINE_SEQUENCE_NUMBER | — | — |
| 52 | NegotiationLineModifiedDate | MODIFIED_DATE | — | — |
| 53 | NegotiationLineModifiedFlag | MODIFIED_FLAG | — | — |
| 54 | NegotiationLineNeedByDate | NEED_BY_DATE | — | — |
| 55 | NegotiationLineNoAward | NO_AWARD | — | — |
| 56 | NegotiationLineNoteToBidders | NOTE_TO_BIDDERS | — | — |
| 57 | NegotiationLineNumberOfBids | NUMBER_OF_BIDS | — | — |
| 58 | NegotiationLineNumberOfExtensions | NUMBER_OF_EXTENSIONS | — | — |
| 59 | NegotiationLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 60 | NegotiationLineOrderTypeLookupCode | ORDER_TYPE_LOOKUP_CODE | — | — |
| 61 | NegotiationLineParentLineNumber | PARENT_LINE_NUMBER | — | — |
| 62 | NegotiationLinePoAgreedAmount | PO_AGREED_AMOUNT | — | — |
| 63 | NegotiationLinePoMinRelAmount | PO_MIN_REL_AMOUNT | — | — |
| 64 | NegotiationLinePrcBuId | PRC_BU_ID | — | — |
| 65 | NegotiationLinePriceBreakNegFlag | PRICE_BREAK_NEG_FLAG | — | — |
| 66 | NegotiationLinePriceBreakType | PRICE_BREAK_TYPE | — | — |
| 67 | NegotiationLinePriceDiffShipmentNumber | PRICE_DIFF_SHIPMENT_NUMBER | — | — |
| 68 | NegotiationLinePriceDisabledFlag | PRICE_DISABLED_FLAG | — | — |
| 69 | NegotiationLineProgressPymtRatePercent | PROGRESS_PYMT_RATE_PERCENT | — | — |
| 70 | NegotiationLineProjectAwardId | PROJECT_AWARD_ID | — | — |
| 71 | NegotiationLineProjectExpOrganizationId | PROJECT_EXP_ORGANIZATION_ID | — | — |
| 72 | NegotiationLineProjectExpenditureItemDate | PROJECT_EXPENDITURE_ITEM_DATE | — | — |
| 73 | NegotiationLineProjectExpenditureType | PROJECT_EXPENDITURE_TYPE | — | — |
| 74 | NegotiationLineProjectId | PROJECT_ID | — | — |
| 75 | NegotiationLineProjectTaskId | PROJECT_TASK_ID | — | — |
| 76 | NegotiationLinePurchaseBasis | PURCHASE_BASIS | — | — |
| 77 | NegotiationLineQuantity | QUANTITY | — | — |
| 78 | NegotiationLineQuantityDisabledFlag | QUANTITY_DISABLED_FLAG | — | — |
| 79 | NegotiationLineRecoupmentRatePercent | RECOUPMENT_RATE_PERCENT | — | — |
| 80 | NegotiationLineReqBuId | REQ_BU_ID | — | — |
| 81 | NegotiationLineRequisitionNumber | REQUISITION_NUMBER | — | — |
| 82 | NegotiationLineRetainageRatePercent | RETAINAGE_RATE_PERCENT | — | — |
| 83 | NegotiationLineShipToLocationId | SHIP_TO_LOCATION_ID | — | — |
| 84 | NegotiationLineSourceDocId | SOURCE_DOC_ID | — | — |
| 85 | NegotiationLineSourceDocNumber | SOURCE_DOC_NUMBER | — | — |
| 86 | NegotiationLineSourceLineId | SOURCE_LINE_ID | — | — |
| 87 | NegotiationLineSourceLineNumber | SOURCE_LINE_NUMBER | — | — |
| 88 | NegotiationLineSubLineSequenceNumber | SUB_LINE_SEQUENCE_NUMBER | — | — |
| 89 | NegotiationLineTargetPrice | TARGET_PRICE | — | — |
| 90 | NegotiationLineUnitDisplayTargetFlag | UNIT_DISPLAY_TARGET_FLAG | — | — |
| 91 | NegotiationLineUnitTargetPrice | UNIT_TARGET_PRICE | — | — |
| 92 | NegotiationLineUomCode | UOM_CODE | — | — |
| 93 | NegotiationLineWorkApproverUserId | WORK_APPROVER_USER_ID | — | — |

### [[pon_bid_item_prices|PON_BID_ITEM_PRICES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NegotiationResponseLineAdvanceAmount | ADVANCE_AMOUNT | — | — |
| 2 | NegotiationResponseLineAuctionHeaderId | AUCTION_HEADER_ID | — | — |
| 3 | NegotiationResponseLineAwardDate | AWARD_DATE | — | — |
| 4 | NegotiationResponseLineAwardPrice | AWARD_PRICE | — | — |
| 5 | NegotiationResponseLineAwardQuantity | AWARD_QUANTITY | — | — |
| 6 | NegotiationResponseLineAwardShipmentNumber | AWARD_SHIPMENT_NUMBER | — | — |
| 7 | NegotiationResponseLineAwardStatus | AWARD_STATUS | — | — |
| 8 | NegotiationResponseLineBatchId | BATCH_ID | — | — |
| 9 | NegotiationResponseLineBidCurrAdvanceAmount | BID_CURR_ADVANCE_AMOUNT | — | — |
| 10 | NegotiationResponseLineBidCurrMaxRetainageAmt | BID_CURR_MAX_RETAINAGE_AMT | — | — |
| 11 | NegotiationResponseLineBidCurrencyLimitPrice | BID_CURRENCY_LIMIT_PRICE | — | — |
| 12 | NegotiationResponseLineBidCurrencyPrice | BID_CURRENCY_PRICE | — | — |
| 13 | NegotiationResponseLineBidCurrencyTransPrice | BID_CURRENCY_TRANS_PRICE | — | — |
| 14 | NegotiationResponseLineBidCurrencyUnitPrice | BID_CURRENCY_UNIT_PRICE | — | — |
| 15 | NegotiationResponseLineBidNumber | BID_NUMBER | — | — |
| 16 | NegotiationResponseLineBidStartPrice | BID_START_PRICE | — | — |
| 17 | NegotiationResponseLineCancelledLimitPrice | CANCELLED_LIMIT_PRICE | — | — |
| 18 | NegotiationResponseLineCopyPriceForProxyFlag | COPY_PRICE_FOR_PROXY_FLAG | — | — |
| 19 | NegotiationResponseLineCreatedBy | CREATED_BY | — | — |
| 20 | NegotiationResponseLineCreationDate | CREATION_DATE | — | — |
| 21 | NegotiationResponseLineDisplayPriceFactorsFlag | DISPLAY_PRICE_FACTORS_FLAG | — | — |
| 22 | NegotiationResponseLineFirstBidPrice | FIRST_BID_PRICE | — | — |
| 23 | NegotiationResponseLineFixedAmountComponent | FIXED_AMOUNT_COMPONENT | — | — |
| 24 | NegotiationResponseLineGroupAmount | GROUP_AMOUNT | — | — |
| 25 | NegotiationResponseLineHasAttributesFlag | HAS_ATTRIBUTES_FLAG | — | — |
| 26 | NegotiationResponseLineHasBidFlag | HAS_BID_FLAG | — | — |
| 27 | NegotiationResponseLineHasBidPaymentsFlag | HAS_BID_PAYMENTS_FLAG | — | — |
| 28 | NegotiationResponseLineHasPriceDifferentialsFlag | HAS_PRICE_DIFFERENTIALS_FLAG | — | — |
| 29 | NegotiationResponseLineHasQuantityTiers | HAS_QUANTITY_TIERS | — | — |
| 30 | NegotiationResponseLineHasShipmentsFlag | HAS_SHIPMENTS_FLAG | — | — |
| 31 | NegotiationResponseLineInterfaceLineId | INTERFACE_LINE_ID | — | — |
| 32 | NegotiationResponseLineIsChangedLineFlag | IS_CHANGED_LINE_FLAG | — | — |
| 33 | NegotiationResponseLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 34 | NegotiationResponseLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 35 | NegotiationResponseLineLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 36 | NegotiationResponseLineLineNumber | LINE_NUMBER | — | — |
| 37 | NegotiationResponseLineMaxRetainageAmount | MAX_RETAINAGE_AMOUNT | — | — |
| 38 | NegotiationResponseLineNoteToAuctionOwner | NOTE_TO_AUCTION_OWNER | — | — |
| 39 | NegotiationResponseLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 40 | NegotiationResponseLineOldBidCurrAdvanceAmount | OLD_BID_CURR_ADVANCE_AMOUNT | — | — |
| 41 | NegotiationResponseLineOldBidCurrMaxRetainageAmt | OLD_BID_CURR_MAX_RETAINAGE_AMT | — | — |
| 42 | NegotiationResponseLineOldBidCurrencyLimitPrice | OLD_BID_CURRENCY_LIMIT_PRICE | — | — |
| 43 | NegotiationResponseLineOldBidCurrencyPrice | OLD_BID_CURRENCY_PRICE | — | — |
| 44 | NegotiationResponseLineOldBidCurrencyUnitPrice | OLD_BID_CURRENCY_UNIT_PRICE | — | — |
| 45 | NegotiationResponseLineOldNoOfPayments | OLD_NO_OF_PAYMENTS | — | — |
| 46 | NegotiationResponseLineOldNoteToAuctionOwner | OLD_NOTE_TO_AUCTION_OWNER | — | — |
| 47 | NegotiationResponseLineOldPoBidMinRelAmount | OLD_PO_BID_MIN_REL_AMOUNT | — | — |
| 48 | NegotiationResponseLineOldPrice | OLD_PRICE | — | — |
| 49 | NegotiationResponseLineOldProgressPymtRatePercent | OLD_PROGRESS_PYMT_RATE_PERCENT | — | — |
| 50 | NegotiationResponseLineOldPromisedDate | OLD_PROMISED_DATE | — | — |
| 51 | NegotiationResponseLineOldPublishDate | OLD_PUBLISH_DATE | — | — |
| 52 | NegotiationResponseLineOldQuantity | OLD_QUANTITY | — | — |
| 53 | NegotiationResponseLineOldRecoupmentRatePercent | OLD_RECOUPMENT_RATE_PERCENT | — | — |
| 54 | NegotiationResponseLineOldRetainageRatePercent | OLD_RETAINAGE_RATE_PERCENT | — | — |
| 55 | NegotiationResponseLinePerUnitPriceComponent | PER_UNIT_PRICE_COMPONENT | — | — |
| 56 | NegotiationResponseLinePoBidMinRelAmount | PO_BID_MIN_REL_AMOUNT | — | — |
| 57 | NegotiationResponseLinePoMinRelAmount | PO_MIN_REL_AMOUNT | — | — |
| 58 | NegotiationResponseLinePrice | PRICE | — | — |
| 59 | NegotiationResponseLinePriceBreakType | PRICE_BREAK_TYPE | — | — |
| 60 | NegotiationResponseLinePriceDiffShipmentNumber | PRICE_DIFF_SHIPMENT_NUMBER | — | — |
| 61 | NegotiationResponseLineProgramAppName | PROGRAM_APP_NAME | — | — |
| 62 | NegotiationResponseLineProgramName | PROGRAM_NAME | — | — |
| 63 | NegotiationResponseLineProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 64 | NegotiationResponseLineProgressPymtRatePercent | PROGRESS_PYMT_RATE_PERCENT | — | — |
| 65 | NegotiationResponseLinePromisedDate | PROMISED_DATE | — | — |
| 66 | NegotiationResponseLineProxyBidFlag | PROXY_BID_FLAG | — | — |
| 67 | NegotiationResponseLineProxyBidLimitPrice | PROXY_BID_LIMIT_PRICE | — | — |
| 68 | NegotiationResponseLinePublishDate | PUBLISH_DATE | — | — |
| 69 | NegotiationResponseLineQuantity | QUANTITY | — | — |
| 70 | NegotiationResponseLineRank | RANK | — | — |
| 71 | NegotiationResponseLineRecoupmentRatePercent | RECOUPMENT_RATE_PERCENT | — | — |
| 72 | NegotiationResponseLineRequestId | REQUEST_ID | — | — |
| 73 | NegotiationResponseLineRetainageRatePercent | RETAINAGE_RATE_PERCENT | — | — |
| 74 | NegotiationResponseLineTotalWeightedScore | TOTAL_WEIGHTED_SCORE | — | — |
| 75 | NegotiationResponseLineTriggerBidNumber | TRIGGER_BID_NUMBER | — | — |
| 76 | NegotiationResponseLineUnitPrice | UNIT_PRICE | — | — |
| 77 | NegotiationResponseLineWorksheetName | WORKSHEET_NAME | — | — |
| 78 | NegotiationResponseLineWorksheetSequenceNumber | WORKSHEET_SEQUENCE_NUMBER | — | — |

### [[por_line_locations_sum_v|POR_LINE_LOCATIONS_SUM_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PurchasingShipmentSummaryAllPoSchCanceledFlag | ALL_PO_SCH_CANCELED_FLAG | — | — |
| 2 | PurchasingShipmentSummaryAllPoSchFulfilledFlag | ALL_PO_SCH_FULFILLED_FLAG | — | — |
| 3 | PurchasingShipmentSummaryAnyPoSchFfPastDueFlag | ANY_PO_SCH_FF_PAST_DUE_FLAG | — | — |
| 4 | PurchasingShipmentSummaryMaxPoSchFulfilledDate | MAX_PO_SCH_FULFILLED_DATE | — | — |
| 5 | PurchasingShipmentSummaryMaxPoSchLastUpdateDate | MAX_PO_SCH_LAST_UPDATE_DATE | — | ✅ |
| 6 | PurchasingShipmentSummaryMinPoSchNeedByDate | MIN_PO_SCH_NEED_BY_DATE | — | — |
| 7 | PurchasingShipmentSummaryMinPoSchPromisedDate | MIN_PO_SCH_PROMISED_DATE | — | — |
| 8 | PurchasingShipmentSummaryRequisitionLineId | REQUISITION_LINE_ID | — | — |
| 9 | PurchasingShipmentSummarySumPoSchAmountReceived | SUM_PO_SCH_AMOUNT_RECEIVED | — | — |
| 10 | PurchasingShipmentSummarySumPoSchQuantityReceived | SUM_PO_SCH_QUANTITY_RECEIVED | — | — |

### [[por_requisition_headers_all|POR_REQUISITION_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RequisitionHeaderActiveRequisitionFlag | ACTIVE_REQUISITION_FLAG | — | — |
| 2 | RequisitionHeaderApprovedDate | APPROVED_DATE | — | ✅ |
| 3 | RequisitionHeaderBudgetControlEnabledFlag | BUDGET_CONTROL_ENABLED_FLAG | — | — |
| 4 | RequisitionHeaderChangePendingFlag | CHANGE_PENDING_FLAG | — | — |
| 5 | RequisitionHeaderCreatedBy | CREATED_BY | — | — |
| 6 | RequisitionHeaderCreationDate | CREATION_DATE | — | — |
| 7 | RequisitionHeaderDescription | DESCRIPTION | — | ✅ |
| 8 | RequisitionHeaderDocumentStatus | DOCUMENT_STATUS | — | ✅ |
| 9 | RequisitionHeaderEmergencyPoNumber | EMERGENCY_PO_NUMBER | — | — |
| 10 | RequisitionHeaderEmergencyReqFlag | EMERGENCY_REQ_FLAG | — | — |
| 11 | RequisitionHeaderExternallyManagedFlag | EXTERNALLY_MANAGED_FLAG | — | — |
| 12 | RequisitionHeaderFundsChkFailWarnFlag | FUNDS_CHK_FAIL_WARN_FLAG | — | — |
| 13 | RequisitionHeaderFundsStatus | FUNDS_STATUS | — | ✅ |
| 14 | RequisitionHeaderHasActionRequiredLines | HAS_ACTION_REQUIRED_LINES | — | — |
| 15 | RequisitionHeaderHasCanceledLines | HAS_CANCELED_LINES | — | — |
| 16 | RequisitionHeaderHasIncompleteLines | HAS_INCOMPLETE_LINES | — | — |
| 17 | RequisitionHeaderHasPendingApprLines | HAS_PENDING_APPR_LINES | — | — |
| 18 | RequisitionHeaderHasRejectedLines | HAS_REJECTED_LINES | — | — |
| 19 | RequisitionHeaderHasReturnedLines | HAS_RETURNED_LINES | — | — |
| 20 | RequisitionHeaderHasWithdrawnLines | HAS_WITHDRAWN_LINES | — | — |
| 21 | RequisitionHeaderInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | ✅ |
| 22 | RequisitionHeaderInterfaceSourceLineId | INTERFACE_SOURCE_LINE_ID | — | — |
| 23 | RequisitionHeaderInternalTransferReqFlag | INTERNAL_TRANSFER_REQ_FLAG | — | ✅ |
| 24 | RequisitionHeaderJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 25 | RequisitionHeaderJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 26 | RequisitionHeaderJustification | JUSTIFICATION | — | ✅ |
| 27 | RequisitionHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 28 | RequisitionHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 29 | RequisitionHeaderLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 30 | RequisitionHeaderLifeCycleStatus | LIFECYCLE_STATUS | — | — |
| 31 | RequisitionHeaderLineGroup | LINE_GROUP | — | — |
| 32 | RequisitionHeaderLockedByBuyerFlag | LOCKED_BY_BUYER_FLAG | — | — |
| 33 | RequisitionHeaderModifyingApproverId | MODIFYING_APPROVER_ID | — | — |
| 34 | RequisitionHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 35 | RequisitionHeaderPcardId | PCARD_ID | — | — |
| 36 | RequisitionHeaderPrcBuId | PRC_BU_ID | — | — |
| 37 | RequisitionHeaderPreparerId | PREPARER_ID | — | — |
| 38 | RequisitionHeaderReqBuId | REQ_BU_ID | — | — |
| 39 | RequisitionHeaderRequestId | REQUEST_ID | — | — |
| 40 | RequisitionHeaderRequisitionHeaderId | REQUISITION_HEADER_ID | — | — |
| 41 | RequisitionHeaderRequisitionNumber | REQUISITION_NUMBER | — | ✅ |
| 42 | RequisitionHeaderSoldtoLeId | SOLDTO_LE_ID | — | — |
| 43 | RequisitionHeaderSubmissionDate | SUBMISSION_DATE | — | — |

### [[por_requisition_lines_all|POR_REQUISITION_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ModifiedByBuyerFlag | MODIFIED_BY_BUYER_FLAG | — | — |
| 2 | RequisitionLineActionRequiredCode | ACTION_REQUIRED_CODE | — | — |
| 3 | RequisitionLineAmount | AMOUNT | — | — |
| 4 | RequisitionLineApprovedDate | LAST_APPROVAL_DATE | — | — |
| 5 | RequisitionLineAssessableValue | ASSESSABLE_VALUE | — | — |
| 6 | RequisitionLineAssignedBuyerId | ASSIGNED_BUYER_ID | — | — |
| 7 | RequisitionLineAtSourcingFlag | AT_SOURCING_FLAG | — | — |
| 8 | RequisitionLineAuctionDisplayNumber | AUCTION_DISPLAY_NUMBER | — | — |
| 9 | RequisitionLineAuctionHeaderId | AUCTION_HEADER_ID | — | — |
| 10 | RequisitionLineAuctionLineNumber | AUCTION_LINE_NUMBER | — | — |
| 11 | RequisitionLineBackToBackFlag | BACK_TO_BACK_FLAG | — | — |
| 12 | RequisitionLineBidLineNumber | BID_LINE_NUMBER | — | — |
| 13 | RequisitionLineBidNumber | BID_NUMBER | — | — |
| 14 | RequisitionLineBpaPriceUserOverrideFlag | BPA_PRICE_USER_OVERRIDE_FLAG | — | — |
| 15 | RequisitionLineBuyerProcessingFlag | BUYER_PROCESSING_FLAG | — | — |
| 16 | RequisitionLineCancelDate | CANCEL_DATE | — | ✅ |
| 17 | RequisitionLineCancelReason | CANCEL_REASON | — | ✅ |
| 18 | RequisitionLineCarrierId | CARRIER_ID | — | — |
| 19 | RequisitionLineCategoryId | CATEGORY_ID | — | — |
| 20 | RequisitionLineContentPrcBuId | CONTENT_PRC_BU_ID | — | — |
| 21 | RequisitionLineCreatedBy | CREATED_BY | — | — |
| 22 | RequisitionLineCreationDate | CREATION_DATE | — | — |
| 23 | RequisitionLineCurrencyAmount | CURRENCY_AMOUNT | — | — |
| 24 | RequisitionLineCurrencyCode | CURRENCY_CODE | — | ✅ |
| 25 | RequisitionLineCurrencyUnitPrice | CURRENCY_UNIT_PRICE | — | — |
| 26 | RequisitionLineCustomerItem | CUSTOMER_ITEM | — | — |
| 27 | RequisitionLineCustomerItemDesc | CUSTOMER_ITEM_DESC | — | — |
| 28 | RequisitionLineCustomerPoLineNumber | CUSTOMER_PO_LINE_NUMBER | — | — |
| 29 | RequisitionLineCustomerPoNumber | CUSTOMER_PO_NUMBER | — | — |
| 30 | RequisitionLineCustomerPoScheduleNumber | CUSTOMER_PO_SCHEDULE_NUMBER | — | — |
| 31 | RequisitionLineDaysEarlyReceiptAllowed | DAYS_EARLY_RECEIPT_ALLOWED | — | — |
| 32 | RequisitionLineDaysLateReceiptAllowed | DAYS_LATE_RECEIPT_ALLOWED | — | — |
| 33 | RequisitionLineDefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | — |
| 34 | RequisitionLineDeliverToCustContactId | DELIVER_TO_CUST_CONTACT_ID | — | — |
| 35 | RequisitionLineDeliverToCustId | DELIVER_TO_CUST_ID | — | — |
| 36 | RequisitionLineDeliverToCustLocationId | DELIVER_TO_CUST_LOCATION_ID | — | — |
| 37 | RequisitionLineDeliverToLocationId | DELIVER_TO_LOCATION_ID | — | — |
| 38 | RequisitionLineDestinationOrganizationId | DESTINATION_ORGANIZATION_ID | — | — |
| 39 | RequisitionLineDestinationSubinventory | DESTINATION_SUBINVENTORY | — | — |
| 40 | RequisitionLineDestinationTypeCode | DESTINATION_TYPE_CODE | — | ✅ |
| 41 | RequisitionLineDocumentSubType | DOCUMENT_SUB_TYPE | — | — |
| 42 | RequisitionLineFinalDischargeLocationId | FINAL_DISCHARGE_LOCATION_ID | — | — |
| 43 | RequisitionLineFirstPtyRegId | FIRST_PTY_REG_ID | — | — |
| 44 | RequisitionLineFundsStatus | FUNDS_STATUS | — | ✅ |
| 45 | RequisitionLineHazardClassId | HAZARD_CLASS_ID | — | — |
| 46 | RequisitionLineInfoTemplateTouchedFlag | INFO_TEMPLATE_TOUCHED_FLAG | — | — |
| 47 | RequisitionLineItemDescription | ITEM_DESCRIPTION | — | ✅ |
| 48 | RequisitionLineItemId | ITEM_ID | — | — |
| 49 | RequisitionLineItemRevision | ITEM_REVISION | — | — |
| 50 | RequisitionLineItemSource | ITEM_SOURCE | — | — |
| 51 | RequisitionLineItemUserOverrideFlag | ITEM_USER_OVERRIDE_FLAG | — | — |
| 52 | RequisitionLineJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 53 | RequisitionLineJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 54 | RequisitionLineLastApprovalDate | LAST_APPROVAL_DATE | — | — |
| 55 | RequisitionLineLastSubmittedDate | LAST_SUBMITTED_DATE | — | — |
| 56 | RequisitionLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 57 | RequisitionLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 58 | RequisitionLineLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 59 | RequisitionLineLifeCycleStatus | LIFECYCLE_STATUS | — | — |
| 60 | RequisitionLineLineGroup | LINE_GROUP | — | — |
| 61 | RequisitionLineLineIntendedUse | LINE_INTENDED_USE | — | — |
| 62 | RequisitionLineLineNumber | LINE_NUMBER | — | ✅ |
| 63 | RequisitionLineLineStatus | LINE_STATUS | — | ✅ |
| 64 | RequisitionLineLineTypeId | LINE_TYPE_ID | — | — |
| 65 | RequisitionLineManufacturerName | MANUFACTURER_NAME | — | ✅ |
| 66 | RequisitionLineManufacturerPartNumber | MANUFACTURER_PART_NUMBER | — | ✅ |
| 67 | RequisitionLineMatchingBasis | MATCHING_BASIS | — | — |
| 68 | RequisitionLineModeOfTransport | MODE_OF_TRANSPORT | — | — |
| 69 | RequisitionLineModifiedByBuyerId | MODIFIED_BY_BUYER_ID | — | — |
| 70 | RequisitionLineNeedByDate | NEED_BY_DATE | — | — |
| 71 | RequisitionLineNegotiatedByPreparerFlag | NEGOTIATED_BY_PREPARER_FLAG | — | — |
| 72 | RequisitionLineNegotiationRequiredFlag | NEGOTIATION_REQUIRED_FLAG | — | — |
| 73 | RequisitionLineNewSupplierFlag | NEW_SUPPLIER_FLAG | — | — |
| 74 | RequisitionLineNoteToBuyer | NOTE_TO_BUYER | — | — |
| 75 | RequisitionLineNoteToReceiver | NOTE_TO_RECEIVER | — | — |
| 76 | RequisitionLineNoteToSupplier | NOTE_TO_SUPPLIER | — | ✅ |
| 77 | RequisitionLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 78 | RequisitionLineOnRfqFlag | ON_RFQ_FLAG | — | — |
| 79 | RequisitionLineOneTimeLocationFlag | ONE_TIME_LOCATION_FLAG | — | ✅ |
| 80 | RequisitionLineOrderTypeLookupCode | ORDER_TYPE_LOOKUP_CODE | — | — |
| 81 | RequisitionLineOriginalApprovalDate | ORIGINAL_APPROVAL_DATE | — | — |
| 82 | RequisitionLineOriginalSubmittedDate | ORIGINAL_SUBMITTED_DATE | — | — |
| 83 | RequisitionLineParentIdAmount | AMOUNT | — | — |
| 84 | RequisitionLineParentIdAssessableValue | ASSESSABLE_VALUE | — | — |
| 85 | RequisitionLineParentIdAssignedBuyerId | ASSIGNED_BUYER_ID | — | — |
| 86 | RequisitionLineParentIdAtSourcingFlag | AT_SOURCING_FLAG | — | — |
| 87 | RequisitionLineParentIdAuctionDisplayNumber | AUCTION_DISPLAY_NUMBER | — | — |
| 88 | RequisitionLineParentIdAuctionHeaderId | AUCTION_HEADER_ID | — | — |
| 89 | RequisitionLineParentIdAuctionLineNumber | AUCTION_LINE_NUMBER | — | — |
| 90 | RequisitionLineParentIdBidLineNumber | BID_LINE_NUMBER | — | — |
| 91 | RequisitionLineParentIdBidNumber | BID_NUMBER | — | — |
| 92 | RequisitionLineParentIdBpaPriceUserOverrideFlag | BPA_PRICE_USER_OVERRIDE_FLAG | — | — |
| 93 | RequisitionLineParentIdCancelDate | CANCEL_DATE | — | — |
| 94 | RequisitionLineParentIdCancelReason | CANCEL_REASON | — | — |
| 95 | RequisitionLineParentIdCategoryId | CATEGORY_ID | — | — |
| 96 | RequisitionLineParentIdContentPrcBuId | CONTENT_PRC_BU_ID | — | — |
| 97 | RequisitionLineParentIdCreatedBy | CREATED_BY | — | — |
| 98 | RequisitionLineParentIdCreationDate | CREATION_DATE | — | — |
| 99 | RequisitionLineParentIdCurrencyAmount | CURRENCY_AMOUNT | — | — |
| 100 | RequisitionLineParentIdCurrencyCode | CURRENCY_CODE | — | — |
| 101 | RequisitionLineParentIdCurrencyUnitPrice | CURRENCY_UNIT_PRICE | — | — |
| 102 | RequisitionLineParentIdDefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | — |
| 103 | RequisitionLineParentIdDeliverToLocationId | DELIVER_TO_LOCATION_ID | — | — |
| 104 | RequisitionLineParentIdDestinationOrganizationId | DESTINATION_ORGANIZATION_ID | — | — |
| 105 | RequisitionLineParentIdDestinationSubinventory | DESTINATION_SUBINVENTORY | — | — |
| 106 | RequisitionLineParentIdDestinationTypeCode | DESTINATION_TYPE_CODE | — | — |
| 107 | RequisitionLineParentIdDocumentSubType | DOCUMENT_SUB_TYPE | — | — |
| 108 | RequisitionLineParentIdHazardClassId | HAZARD_CLASS_ID | — | — |
| 109 | RequisitionLineParentIdInfoTemplateTouchedFlag | INFO_TEMPLATE_TOUCHED_FLAG | — | — |
| 110 | RequisitionLineParentIdItemDescription | ITEM_DESCRIPTION | — | — |
| 111 | RequisitionLineParentIdItemId | ITEM_ID | — | — |
| 112 | RequisitionLineParentIdItemRevision | ITEM_REVISION | — | — |
| 113 | RequisitionLineParentIdItemSource | ITEM_SOURCE | — | — |
| 114 | RequisitionLineParentIdItemUserOverrideFlag | ITEM_USER_OVERRIDE_FLAG | — | — |
| 115 | RequisitionLineParentIdJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 116 | RequisitionLineParentIdJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 117 | RequisitionLineParentIdLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 118 | RequisitionLineParentIdLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 119 | RequisitionLineParentIdLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 120 | RequisitionLineParentIdLineIntendedUse | LINE_INTENDED_USE | — | — |
| 121 | RequisitionLineParentIdLineNumber | LINE_NUMBER | — | — |
| 122 | RequisitionLineParentIdLineTypeId | LINE_TYPE_ID | — | — |
| 123 | RequisitionLineParentIdManufacturerName | MANUFACTURER_NAME | — | — |
| 124 | RequisitionLineParentIdManufacturerPartNumber | MANUFACTURER_PART_NUMBER | — | — |
| 125 | RequisitionLineParentIdMatchingBasis | MATCHING_BASIS | — | — |
| 126 | RequisitionLineParentIdModifiedByBuyerId | MODIFIED_BY_BUYER_ID | — | — |
| 127 | RequisitionLineParentIdNeedByDate | NEED_BY_DATE | — | — |
| 128 | RequisitionLineParentIdNegotiatedByPreparerFlag | NEGOTIATED_BY_PREPARER_FLAG | — | — |
| 129 | RequisitionLineParentIdNegotiationRequiredFlag | NEGOTIATION_REQUIRED_FLAG | — | — |
| 130 | RequisitionLineParentIdNewSupplierFlag | NEW_SUPPLIER_FLAG | — | — |
| 131 | RequisitionLineParentIdNoteToBuyer | NOTE_TO_BUYER | — | — |
| 132 | RequisitionLineParentIdNoteToReceiver | NOTE_TO_RECEIVER | — | — |
| 133 | RequisitionLineParentIdNoteToSupplier | NOTE_TO_SUPPLIER | — | — |
| 134 | RequisitionLineParentIdObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 135 | RequisitionLineParentIdOnRfqFlag | ON_RFQ_FLAG | — | — |
| 136 | RequisitionLineParentIdOneTimeLocationFlag | ONE_TIME_LOCATION_FLAG | — | — |
| 137 | RequisitionLineParentIdOrderTypeLookupCode | ORDER_TYPE_LOOKUP_CODE | — | — |
| 138 | RequisitionLineParentIdParentReqLineId | PARENT_REQ_LINE_ID | — | — |
| 139 | RequisitionLineParentIdPcardFlag | PCARD_FLAG | — | — |
| 140 | RequisitionLineParentIdPrcBuId | PRC_BU_ID | — | — |
| 141 | RequisitionLineParentIdProductCategory | PRODUCT_CATEGORY | — | — |
| 142 | RequisitionLineParentIdProductFiscClassification | PRODUCT_FISC_CLASSIFICATION | — | — |
| 143 | RequisitionLineParentIdProductType | PRODUCT_TYPE | — | — |
| 144 | RequisitionLineParentIdPublicListId | PUBLIC_LIST_ID | — | — |
| 145 | RequisitionLineParentIdPunchoutCatalogId | PUNCHOUT_CATALOG_ID | — | — |
| 146 | RequisitionLineParentIdPurchaseBasis | PURCHASE_BASIS | — | — |
| 147 | RequisitionLineParentIdQuantity | QUANTITY | — | — |
| 148 | RequisitionLineParentIdQuantityCancelled | QUANTITY_CANCELLED | — | — |
| 149 | RequisitionLineParentIdQuantityDelivered | QUANTITY_DELIVERED | — | — |
| 150 | RequisitionLineParentIdQuantityReceived | QUANTITY_RECEIVED | — | — |
| 151 | RequisitionLineParentIdRate | RATE | — | — |
| 152 | RequisitionLineParentIdRateDate | RATE_DATE | — | — |
| 153 | RequisitionLineParentIdRateType | RATE_TYPE | — | — |
| 154 | RequisitionLineParentIdReqBuId | REQ_BU_ID | — | — |
| 155 | RequisitionLineParentIdReqsInPoolFlag | REQS_IN_POOL_FLAG | — | — |
| 156 | RequisitionLineParentIdReqtopoAutomationFailed | REQTOPO_AUTOMATION_FAILED | — | — |
| 157 | RequisitionLineParentIdRequestId | REQUEST_ID | — | — |
| 158 | RequisitionLineParentIdRequesterId | REQUESTER_ID | — | — |
| 159 | RequisitionLineParentIdRequisitionHeaderId | REQUISITION_HEADER_ID | — | — |
| 160 | RequisitionLineParentIdRequisitionLineId | REQUISITION_LINE_ID | — | — |
| 161 | RequisitionLineParentIdSecondaryQuantity | SECONDARY_QUANTITY | — | — |
| 162 | RequisitionLineParentIdSecondaryQuantityCancelled | SECONDARY_QUANTITY_CANCELLED | — | — |
| 163 | RequisitionLineParentIdSecondaryQuantityReceived | SECONDARY_QUANTITY_RECEIVED | — | — |
| 164 | RequisitionLineParentIdSecondaryUomCode | SECONDARY_UOM_CODE | — | — |
| 165 | RequisitionLineParentIdSmartFormId | SMART_FORM_ID | — | — |
| 166 | RequisitionLineParentIdSourceDocHeaderId | SOURCE_DOC_HEADER_ID | — | — |
| 167 | RequisitionLineParentIdSourceDocLineId | SOURCE_DOC_LINE_ID | — | — |
| 168 | RequisitionLineParentIdSourceDocumentType | SOURCE_DOCUMENT_TYPE | — | — |
| 169 | RequisitionLineParentIdSuggestedBuyerId | SUGGESTED_BUYER_ID | — | — |
| 170 | RequisitionLineParentIdSuggestedSupplierItemNumber | SUGGESTED_SUPPLIER_ITEM_NUMBER | — | — |
| 171 | RequisitionLineParentIdSuggestedVendorContact | SUGGESTED_VENDOR_CONTACT | — | — |
| 172 | RequisitionLineParentIdSuggestedVendorContactEmail | SUGGESTED_VENDOR_CONTACT_EMAIL | — | — |
| 173 | RequisitionLineParentIdSuggestedVendorContactFax | SUGGESTED_VENDOR_CONTACT_FAX | — | — |
| 174 | RequisitionLineParentIdSuggestedVendorContactPhone | SUGGESTED_VENDOR_CONTACT_PHONE | — | — |
| 175 | RequisitionLineParentIdSuggestedVendorName | SUGGESTED_VENDOR_NAME | — | — |
| 176 | RequisitionLineParentIdSuggestedVendorSite | SUGGESTED_VENDOR_SITE | — | — |
| 177 | RequisitionLineParentIdSupplierDuns | SUPPLIER_DUNS | — | — |
| 178 | RequisitionLineParentIdSupplierRefNumber | SUPPLIER_REF_NUMBER | — | — |
| 179 | RequisitionLineParentIdTaxAttrUserOverrideFlag | TAX_ATTR_USER_OVERRIDE_FLAG | — | — |
| 180 | RequisitionLineParentIdTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | — |
| 181 | RequisitionLineParentIdTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | — |
| 182 | RequisitionLineParentIdUnNumberId | UN_NUMBER_ID | — | — |
| 183 | RequisitionLineParentIdUnitPrice | UNIT_PRICE | — | — |
| 184 | RequisitionLineParentIdUnspscCode | UNSPSC_CODE | — | — |
| 185 | RequisitionLineParentIdUomCode | UOM_CODE | — | — |
| 186 | RequisitionLineParentIdUrgentFlag | URGENT_FLAG | — | — |
| 187 | RequisitionLineParentIdUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |
| 188 | RequisitionLineParentIdVendorContactId | VENDOR_CONTACT_ID | — | — |
| 189 | RequisitionLineParentIdVendorId | VENDOR_ID | — | — |
| 190 | RequisitionLineParentIdVendorSiteId | VENDOR_SITE_ID | — | — |
| 191 | RequisitionLineParentReqLineId | PARENT_REQ_LINE_ID | — | — |
| 192 | RequisitionLinePcardFlag | PCARD_FLAG | — | — |
| 193 | RequisitionLinePoHeaderId | PO_HEADER_ID | — | — |
| 194 | RequisitionLinePoLineId | PO_LINE_ID | — | — |
| 195 | RequisitionLinePrcBuId | PRC_BU_ID | — | — |
| 196 | RequisitionLineProductCategory | PRODUCT_CATEGORY | — | — |
| 197 | RequisitionLineProductFiscClassification | PRODUCT_FISC_CLASSIFICATION | — | — |
| 198 | RequisitionLineProductType | PRODUCT_TYPE | — | — |
| 199 | RequisitionLinePublicListId | PUBLIC_LIST_ID | — | — |
| 200 | RequisitionLinePunchoutCatalogId | PUNCHOUT_CATALOG_ID | — | — |
| 201 | RequisitionLinePurchaseBasis | PURCHASE_BASIS | — | — |
| 202 | RequisitionLineQtyRcvTolerance | QTY_RCV_TOLERANCE | — | — |
| 203 | RequisitionLineQuantity | QUANTITY | — | — |
| 204 | RequisitionLineQuantityCancelled | QUANTITY_CANCELLED | — | — |
| 205 | RequisitionLineQuantityDelivered | QUANTITY_DELIVERED | — | — |
| 206 | RequisitionLineQuantityReceived | QUANTITY_RECEIVED | — | — |
| 207 | RequisitionLineRate | RATE | — | — |
| 208 | RequisitionLineRateDate | RATE_DATE | — | — |
| 209 | RequisitionLineRateType | RATE_TYPE | — | — |
| 210 | RequisitionLineReqBuId | REQ_BU_ID | — | — |
| 211 | RequisitionLineReqsInPoolFlag | REQS_IN_POOL_FLAG | — | — |
| 212 | RequisitionLineReqtopoAutoFailedReason | REQTOPO_AUTO_FAILED_REASON | — | — |
| 213 | RequisitionLineReqtopoAutomationFailed | REQTOPO_AUTOMATION_FAILED | — | — |
| 214 | RequisitionLineRequestId | REQUEST_ID | — | — |
| 215 | RequisitionLineRequestedShipDate | REQUESTED_SHIP_DATE | — | — |
| 216 | RequisitionLineRequesterId | REQUESTER_ID | — | — |
| 217 | RequisitionLineRequisitionHeaderId | REQUISITION_HEADER_ID | — | — |
| 218 | RequisitionLineRequisitionLineId | REQUISITION_LINE_ID | — | — |
| 219 | RequisitionLineReturnReason | RETURN_REASON | — | — |
| 220 | RequisitionLineSalesOrderLineNumber | SALES_ORDER_LINE_NUMBER | — | — |
| 221 | RequisitionLineSalesOrderNumber | SALES_ORDER_NUMBER | — | — |
| 222 | RequisitionLineSalesOrderScheduleNumber | SALES_ORDER_SCHEDULE_NUMBER | — | — |
| 223 | RequisitionLineSecondaryQuantity | SECONDARY_QUANTITY | — | — |
| 224 | RequisitionLineSecondaryQuantityCancelled | SECONDARY_QUANTITY_CANCELLED | — | — |
| 225 | RequisitionLineSecondaryQuantityReceived | SECONDARY_QUANTITY_RECEIVED | — | — |
| 226 | RequisitionLineSecondaryUomCode | SECONDARY_UOM_CODE | — | — |
| 227 | RequisitionLineServiceLevel | SERVICE_LEVEL | — | — |
| 228 | RequisitionLineShipToCustContactId | SHIP_TO_CUST_CONTACT_ID | — | — |
| 229 | RequisitionLineShipToCustId | SHIP_TO_CUST_ID | — | — |
| 230 | RequisitionLineShipToCustLocationId | SHIP_TO_CUST_LOCATION_ID | — | — |
| 231 | RequisitionLineSmartFormId | SMART_FORM_ID | — | — |
| 232 | RequisitionLineSourceDocHeaderId | SOURCE_DOC_HEADER_ID | — | — |
| 233 | RequisitionLineSourceDocLineId | SOURCE_DOC_LINE_ID | — | — |
| 234 | RequisitionLineSourceDocumentType | SOURCE_DOCUMENT_TYPE | — | ✅ |
| 235 | RequisitionLineSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | — |
| 236 | RequisitionLineSourceSubinventory | SOURCE_SUBINVENTORY | — | — |
| 237 | RequisitionLineSourceTypeCode | SOURCE_TYPE_CODE | — | ✅ |
| 238 | RequisitionLineSuggestedBuyerId | SUGGESTED_BUYER_ID | — | — |
| 239 | RequisitionLineSuggestedSupplierItemNumber | SUGGESTED_SUPPLIER_ITEM_NUMBER | — | — |
| 240 | RequisitionLineSuggestedVendorContact | SUGGESTED_VENDOR_CONTACT | — | ✅ |
| 241 | RequisitionLineSuggestedVendorContactEmail | SUGGESTED_VENDOR_CONTACT_EMAIL | — | — |
| 242 | RequisitionLineSuggestedVendorContactFax | SUGGESTED_VENDOR_CONTACT_FAX | — | — |
| 243 | RequisitionLineSuggestedVendorContactPhone | SUGGESTED_VENDOR_CONTACT_PHONE | — | — |
| 244 | RequisitionLineSuggestedVendorName | SUGGESTED_VENDOR_NAME | — | ✅ |
| 245 | RequisitionLineSuggestedVendorSite | SUGGESTED_VENDOR_SITE | — | ✅ |
| 246 | RequisitionLineSupplierDuns | SUPPLIER_DUNS | — | — |
| 247 | RequisitionLineSupplierRefNumber | SUPPLIER_REF_NUMBER | — | — |
| 248 | RequisitionLineTaxAttrUserOverrideFlag | TAX_ATTR_USER_OVERRIDE_FLAG | — | — |
| 249 | RequisitionLineTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | — |
| 250 | RequisitionLineThirdPtyRegId | THIRD_PTY_REG_ID | — | — |
| 251 | RequisitionLineTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | — |
| 252 | RequisitionLineUnNumberId | UN_NUMBER_ID | — | — |
| 253 | RequisitionLineUnitPrice | UNIT_PRICE | — | ✅ |
| 254 | RequisitionLineUnspscCode | UNSPSC_CODE | — | — |
| 255 | RequisitionLineUomCode | UOM_CODE | — | ✅ |
| 256 | RequisitionLineUrgentFlag | URGENT_FLAG | — | — |
| 257 | RequisitionLineUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |
| 258 | RequisitionLineVendorContactId | VENDOR_CONTACT_ID | — | — |
| 259 | RequisitionLineVendorId | VENDOR_ID | — | — |
| 260 | RequisitionLineVendorSiteId | VENDOR_SITE_ID | — | — |

### [[por_req_distributions_all|POR_REQ_DISTRIBUTIONS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DistributionId | DISTRIBUTION_ID | 🔑 | ✅ |
| 2 | RequisitionDistributionAccountUserOverrideFlag | ACCOUNT_USER_OVERRIDE_FLAG | — | — |
| 3 | RequisitionDistributionAccrualAccountId | ACCRUAL_ACCOUNT_ID | — | — |
| 4 | RequisitionDistributionBudgetDate | BUDGET_DATE | — | ✅ |
| 5 | RequisitionDistributionCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 6 | RequisitionDistributionCreatedBy | CREATED_BY | — | — |
| 7 | RequisitionDistributionCreationDate | CREATION_DATE | — | — |
| 8 | RequisitionDistributionDistributionAmount | DISTRIBUTION_AMOUNT | — | — |
| 9 | RequisitionDistributionDistributionCurrencyAmount | DISTRIBUTION_CURRENCY_AMOUNT | — | ✅ |
| 10 | RequisitionDistributionDistributionNumber | DISTRIBUTION_NUMBER | — | ✅ |
| 11 | RequisitionDistributionDistributionQuantity | DISTRIBUTION_QUANTITY | — | ✅ |
| 12 | RequisitionDistributionFundsStatus | FUNDS_STATUS | — | ✅ |
| 13 | RequisitionDistributionJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 14 | RequisitionDistributionJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 15 | RequisitionDistributionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | RequisitionDistributionLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 17 | RequisitionDistributionLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 18 | RequisitionDistributionNonrecoverableTax | NONRECOVERABLE_TAX | — | ✅ |
| 19 | RequisitionDistributionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | RequisitionDistributionPJC_BILLABLE_FLAG | PJC_BILLABLE_FLAG | — | — |
| 21 | RequisitionDistributionPJC_CAPITALIZABLE_FLAG | PJC_CAPITALIZABLE_FLAG | — | ✅ |
| 22 | RequisitionDistributionPJC_CONTEXT_CATEGORY | PJC_CONTEXT_CATEGORY | — | — |
| 23 | RequisitionDistributionPJC_CONTRACT_ID | PJC_CONTRACT_ID | — | — |
| 24 | RequisitionDistributionPJC_CONTRACT_LINE_ID | PJC_CONTRACT_LINE_ID | — | — |
| 25 | RequisitionDistributionPJC_EXPENDITURE_ITEM_DATE | PJC_EXPENDITURE_ITEM_DATE | — | ✅ |
| 26 | RequisitionDistributionPJC_EXPENDITURE_TYPE_ID | PJC_EXPENDITURE_TYPE_ID | — | — |
| 27 | RequisitionDistributionPJC_FUNDING_ALLOCATION_ID | PJC_FUNDING_ALLOCATION_ID | — | — |
| 28 | RequisitionDistributionPJC_ORGANIZATION_ID | PJC_ORGANIZATION_ID | — | — |
| 29 | RequisitionDistributionPJC_PROJECT_ID | PJC_PROJECT_ID | — | — |
| 30 | RequisitionDistributionPJC_RESERVED_ATTRIBUTE1 | PJC_RESERVED_ATTRIBUTE1 | — | — |
| 31 | RequisitionDistributionPJC_RESERVED_ATTRIBUTE10 | PJC_RESERVED_ATTRIBUTE10 | — | — |
| 32 | RequisitionDistributionPJC_RESERVED_ATTRIBUTE2 | PJC_RESERVED_ATTRIBUTE2 | — | — |
| 33 | RequisitionDistributionPJC_RESERVED_ATTRIBUTE3 | PJC_RESERVED_ATTRIBUTE3 | — | — |
| 34 | RequisitionDistributionPJC_RESERVED_ATTRIBUTE4 | PJC_RESERVED_ATTRIBUTE4 | — | — |
| 35 | RequisitionDistributionPJC_RESERVED_ATTRIBUTE5 | PJC_RESERVED_ATTRIBUTE5 | — | — |
| 36 | RequisitionDistributionPJC_RESERVED_ATTRIBUTE6 | PJC_RESERVED_ATTRIBUTE6 | — | — |
| 37 | RequisitionDistributionPJC_RESERVED_ATTRIBUTE7 | PJC_RESERVED_ATTRIBUTE7 | — | — |
| 38 | RequisitionDistributionPJC_RESERVED_ATTRIBUTE8 | PJC_RESERVED_ATTRIBUTE8 | — | — |
| 39 | RequisitionDistributionPJC_RESERVED_ATTRIBUTE9 | PJC_RESERVED_ATTRIBUTE9 | — | — |
| 40 | RequisitionDistributionPJC_TASK_ID | PJC_TASK_ID | — | — |
| 41 | RequisitionDistributionPJC_USER_DEF_ATTRIBUTE1 | PJC_USER_DEF_ATTRIBUTE1 | — | — |
| 42 | RequisitionDistributionPJC_USER_DEF_ATTRIBUTE10 | PJC_USER_DEF_ATTRIBUTE10 | — | — |
| 43 | RequisitionDistributionPJC_USER_DEF_ATTRIBUTE2 | PJC_USER_DEF_ATTRIBUTE2 | — | — |
| 44 | RequisitionDistributionPJC_USER_DEF_ATTRIBUTE3 | PJC_USER_DEF_ATTRIBUTE3 | — | — |
| 45 | RequisitionDistributionPJC_USER_DEF_ATTRIBUTE4 | PJC_USER_DEF_ATTRIBUTE4 | — | — |
| 46 | RequisitionDistributionPJC_USER_DEF_ATTRIBUTE5 | PJC_USER_DEF_ATTRIBUTE5 | — | — |
| 47 | RequisitionDistributionPJC_USER_DEF_ATTRIBUTE6 | PJC_USER_DEF_ATTRIBUTE6 | — | — |
| 48 | RequisitionDistributionPJC_USER_DEF_ATTRIBUTE7 | PJC_USER_DEF_ATTRIBUTE7 | — | — |
| 49 | RequisitionDistributionPJC_USER_DEF_ATTRIBUTE8 | PJC_USER_DEF_ATTRIBUTE8 | — | — |
| 50 | RequisitionDistributionPJC_USER_DEF_ATTRIBUTE9 | PJC_USER_DEF_ATTRIBUTE9 | — | — |
| 51 | RequisitionDistributionPJC_WORK_TYPE_ID | PJC_WORK_TYPE_ID | — | — |
| 52 | RequisitionDistributionPercent | PERCENT | — | ✅ |
| 53 | RequisitionDistributionPrimaryLedgerId | PRIMARY_LEDGER_ID | — | — |
| 54 | RequisitionDistributionRecoverableTax | RECOVERABLE_TAX | — | ✅ |
| 55 | RequisitionDistributionReqBuId | REQ_BU_ID | — | — |
| 56 | RequisitionDistributionRequestId | REQUEST_ID | — | — |
| 57 | RequisitionDistributionRequisitionLineId | REQUISITION_LINE_ID | — | — |
| 58 | RequisitionDistributionVarianceAccountId | VARIANCE_ACCOUNT_ID | — | — |

### [[po_action_history|PO_ACTION_HISTORY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PurchasingDocumentActionHistActionCode | ACTION_CODE | — | — |
| 2 | PurchasingDocumentActionHistObjectId | OBJECT_ID | — | — |
| 3 | PurchasingDocumentActionHistObjectSubTypeCode | OBJECT_SUB_TYPE_CODE | — | — |
| 4 | PurchasingDocumentActionHistObjectTypeCode | OBJECT_TYPE_CODE | — | — |
| 5 | PurchasingDocumentActionHistSequenceNum | SEQUENCE_NUM | — | — |
| 6 | RequisitionHeaderCanceledDate | ACTION_DATE | — | ✅ |
| 7 | RequisitionHeaderCanceledReason | NOTE | — | ✅ |

### [[po_hazard_classes_vl|PO_HAZARD_CLASSES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PurchasingHazardClassDescription | DESCRIPTION | — | — |
| 2 | PurchasingHazardClassHazardClass | HAZARD_CLASS | — | — |
| 3 | PurchasingHazardClassHazardClassCode | HAZARD_CLASS_CODE | — | — |
| 4 | PurchasingHazardClassHazardClassId | HAZARD_CLASS_ID | — | — |
| 5 | PurchasingHazardClassInactiveDate | INACTIVE_DATE | — | — |
| 6 | PurchasingHazardClassObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[po_headers_all|PO_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PurchasingDocHdrSourceHdrAcceptanceDueDate | ACCEPTANCE_DUE_DATE | — | — |
| 2 | PurchasingDocHdrSourceHdrAcceptanceRequiredFlag | ACCEPTANCE_REQUIRED_FLAG | — | — |
| 3 | PurchasingDocHdrSourceHdrAcceptanceWithinDays | ACCEPTANCE_WITHIN_DAYS | — | — |
| 4 | PurchasingDocHdrSourceHdrAgentId | AGENT_ID | — | — |
| 5 | PurchasingDocHdrSourceHdrAmountLimit | AMOUNT_LIMIT | — | — |
| 6 | PurchasingDocHdrSourceHdrAmountReleased | AMOUNT_RELEASED | — | — |
| 7 | PurchasingDocHdrSourceHdrApprovedDate | APPROVED_DATE | — | — |
| 8 | PurchasingDocHdrSourceHdrApprovedFlag | APPROVED_FLAG | — | — |
| 9 | PurchasingDocHdrSourceHdrAutoSourcingFlag | AUTO_SOURCING_FLAG | — | — |
| 10 | PurchasingDocHdrSourceHdrBillToLocationId | BILL_TO_LOCATION_ID | — | — |
| 11 | PurchasingDocHdrSourceHdrBilltoBuId | BILLTO_BU_ID | — | — |
| 12 | PurchasingDocHdrSourceHdrBlanketTotalAmount | BLANKET_TOTAL_AMOUNT | — | — |
| 13 | PurchasingDocHdrSourceHdrCancelFlag | CANCEL_FLAG | — | — |
| 14 | PurchasingDocHdrSourceHdrCarrierId | CARRIER_ID | — | — |
| 15 | PurchasingDocHdrSourceHdrCatAdminAuthEnabledFlag | CAT_ADMIN_AUTH_ENABLED_FLAG | — | — |
| 16 | PurchasingDocHdrSourceHdrCbcAccountingDate | CBC_ACCOUNTING_DATE | — | — |
| 17 | PurchasingDocHdrSourceHdrChangeRequestedBy | CHANGE_REQUESTED_BY | — | — |
| 18 | PurchasingDocHdrSourceHdrChangeSummary | CHANGE_SUMMARY | — | — |
| 19 | PurchasingDocHdrSourceHdrClosedDate | CLOSED_DATE | — | — |
| 20 | PurchasingDocHdrSourceHdrComments | COMMENTS | — | — |
| 21 | PurchasingDocHdrSourceHdrConfirmingOrderFlag | CONFIRMING_ORDER_FLAG | — | — |
| 22 | PurchasingDocHdrSourceHdrConsignedConsumptionFlag | CONSIGNED_CONSUMPTION_FLAG | — | — |
| 23 | PurchasingDocHdrSourceHdrConsumeReqDemandFlag | CONSUME_REQ_DEMAND_FLAG | — | — |
| 24 | PurchasingDocHdrSourceHdrContermsArticlesUpdDate | CONTERMS_ARTICLES_UPD_DATE | — | — |
| 25 | PurchasingDocHdrSourceHdrContermsDelivUpdDate | CONTERMS_DELIV_UPD_DATE | — | — |
| 26 | PurchasingDocHdrSourceHdrContermsExistFlag | CONTERMS_EXIST_FLAG | — | — |
| 27 | PurchasingDocHdrSourceHdrCpaReference | CPA_REFERENCE | — | — |
| 28 | PurchasingDocHdrSourceHdrCreatedBy | CREATED_BY | — | — |
| 29 | PurchasingDocHdrSourceHdrCreatedLanguage | CREATED_LANGUAGE | — | — |
| 30 | PurchasingDocHdrSourceHdrCreationDate | CREATION_DATE | — | — |
| 31 | PurchasingDocHdrSourceHdrCurrencyCode | CURRENCY_CODE | — | — |
| 32 | PurchasingDocHdrSourceHdrCurrentVersionId | CURRENT_VERSION_ID | — | — |
| 33 | PurchasingDocHdrSourceHdrDefaultPoTradeOrgId | DEFAULT_PO_TRADE_ORG_ID | — | — |
| 34 | PurchasingDocHdrSourceHdrDefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | — |
| 35 | PurchasingDocHdrSourceHdrDocumentCreationMethod | DOCUMENT_CREATION_METHOD | — | — |
| 36 | PurchasingDocHdrSourceHdrDocumentStatus | DOCUMENT_STATUS | — | — |
| 37 | PurchasingDocHdrSourceHdrEdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 38 | PurchasingDocHdrSourceHdrEdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 39 | PurchasingDocHdrSourceHdrEmailAddress | EMAIL_ADDRESS | — | — |
| 40 | PurchasingDocHdrSourceHdrEnabledFlag | ENABLED_FLAG | — | — |
| 41 | PurchasingDocHdrSourceHdrEncumbranceRequiredFlag | ENCUMBRANCE_REQUIRED_FLAG | — | — |
| 42 | PurchasingDocHdrSourceHdrEndDate | END_DATE | — | — |
| 43 | PurchasingDocHdrSourceHdrFax | FAX | — | — |
| 44 | PurchasingDocHdrSourceHdrFirmDate | FIRM_DATE | — | — |
| 45 | PurchasingDocHdrSourceHdrFirmStatusLookupCode | FIRM_STATUS_LOOKUP_CODE | — | — |
| 46 | PurchasingDocHdrSourceHdrFobLookupCode | FOB_LOOKUP_CODE | — | — |
| 47 | PurchasingDocHdrSourceHdrFreightTermsLookupCode | FREIGHT_TERMS_LOOKUP_CODE | — | — |
| 48 | PurchasingDocHdrSourceHdrFromHeaderId | FROM_HEADER_ID | — | — |
| 49 | PurchasingDocHdrSourceHdrFromTypeLookupCode | FROM_TYPE_LOOKUP_CODE | — | — |
| 50 | PurchasingDocHdrSourceHdrFrozenFlag | FROZEN_FLAG | — | — |
| 51 | PurchasingDocHdrSourceHdrFundsStatus | FUNDS_STATUS | — | — |
| 52 | PurchasingDocHdrSourceHdrGenerateOrdersAutomatic | GENERATE_ORDERS_AUTOMATIC | — | — |
| 53 | PurchasingDocHdrSourceHdrGovernmentContext | GOVERNMENT_CONTEXT | — | — |
| 54 | PurchasingDocHdrSourceHdrGroupRequisitionLines | GROUP_REQUISITION_LINES | — | — |
| 55 | PurchasingDocHdrSourceHdrGroupRequisitions | GROUP_REQUISITIONS | — | — |
| 56 | PurchasingDocHdrSourceHdrInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | — |
| 57 | PurchasingDocHdrSourceHdrJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 58 | PurchasingDocHdrSourceHdrJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 59 | PurchasingDocHdrSourceHdrLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 60 | PurchasingDocHdrSourceHdrLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 61 | PurchasingDocHdrSourceHdrLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 62 | PurchasingDocHdrSourceHdrLastUpdatedProgram | LAST_UPDATED_PROGRAM | — | — |
| 63 | PurchasingDocHdrSourceHdrMinReleaseAmount | MIN_RELEASE_AMOUNT | — | — |
| 64 | PurchasingDocHdrSourceHdrNoteToAuthorizer | NOTE_TO_AUTHORIZER | — | — |
| 65 | PurchasingDocHdrSourceHdrNoteToReceiver | NOTE_TO_RECEIVER | — | — |
| 66 | PurchasingDocHdrSourceHdrNoteToVendor | NOTE_TO_VENDOR | — | — |
| 67 | PurchasingDocHdrSourceHdrObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 68 | PurchasingDocHdrSourceHdrOrchestrationOrderFlag | ORCHESTRATION_ORDER_FLAG | — | — |
| 69 | PurchasingDocHdrSourceHdrPayOnCode | PAY_ON_CODE | — | — |
| 70 | PurchasingDocHdrSourceHdrPcardId | PCARD_ID | — | — |
| 71 | PurchasingDocHdrSourceHdrPendingSignatureFlag | PENDING_SIGNATURE_FLAG | — | — |
| 72 | PurchasingDocHdrSourceHdrPoHeaderId | PO_HEADER_ID | — | — |
| 73 | PurchasingDocHdrSourceHdrPrcBuId | PRC_BU_ID | — | — |
| 74 | PurchasingDocHdrSourceHdrPriceUpdateTolerance | PRICE_UPDATE_TOLERANCE | — | — |
| 75 | PurchasingDocHdrSourceHdrProgramAppName | PROGRAM_APP_NAME | — | — |
| 76 | PurchasingDocHdrSourceHdrProgramName | PROGRAM_NAME | — | — |
| 77 | PurchasingDocHdrSourceHdrRate | RATE | — | — |
| 78 | PurchasingDocHdrSourceHdrRateDate | RATE_DATE | — | — |
| 79 | PurchasingDocHdrSourceHdrRateType | RATE_TYPE | — | — |
| 80 | PurchasingDocHdrSourceHdrReferenceNum | REFERENCE_NUM | — | — |
| 81 | PurchasingDocHdrSourceHdrReleaseMethod | RELEASE_METHOD | — | — |
| 82 | PurchasingDocHdrSourceHdrReqBuId | REQ_BU_ID | — | — |
| 83 | PurchasingDocHdrSourceHdrRequestId | REQUEST_ID | — | — |
| 84 | PurchasingDocHdrSourceHdrRetroPriceApplyUpdatesFlag | RETRO_PRICE_APPLY_UPDATES_FLAG | — | — |
| 85 | PurchasingDocHdrSourceHdrRetroPriceCommUpdatesFlag | RETRO_PRICE_COMM_UPDATES_FLAG | — | — |
| 86 | PurchasingDocHdrSourceHdrReviewAutogeneratedReleases | REVIEW_AUTOGENERATED_RELEASES | — | — |
| 87 | PurchasingDocHdrSourceHdrRevisedDate | REVISED_DATE | — | — |
| 88 | PurchasingDocHdrSourceHdrRevisionNum | REVISION_NUM | — | — |
| 89 | PurchasingDocHdrSourceHdrSegment1 | SEGMENT1 | — | ✅ |
| 90 | PurchasingDocHdrSourceHdrSegment2 | SEGMENT2 | — | — |
| 91 | PurchasingDocHdrSourceHdrSegment3 | SEGMENT3 | — | — |
| 92 | PurchasingDocHdrSourceHdrSegment4 | SEGMENT4 | — | — |
| 93 | PurchasingDocHdrSourceHdrSegment5 | SEGMENT5 | — | — |
| 94 | PurchasingDocHdrSourceHdrShipToLocationId | SHIP_TO_LOCATION_ID | — | — |
| 95 | PurchasingDocHdrSourceHdrShippingControl | SHIPPING_CONTROL | — | — |
| 96 | PurchasingDocHdrSourceHdrSoldtoLeId | SOLDTO_LE_ID | — | — |
| 97 | PurchasingDocHdrSourceHdrStartDate | START_DATE | — | — |
| 98 | PurchasingDocHdrSourceHdrStyleId | STYLE_ID | — | — |
| 99 | PurchasingDocHdrSourceHdrSubmitApprovalAutomatic | SUBMIT_APPROVAL_AUTOMATIC | — | — |
| 100 | PurchasingDocHdrSourceHdrSubmitDate | SUBMIT_DATE | — | — |
| 101 | PurchasingDocHdrSourceHdrSummaryFlag | SUMMARY_FLAG | — | — |
| 102 | PurchasingDocHdrSourceHdrSupplierNotifMethod | SUPPLIER_NOTIF_METHOD | — | — |
| 103 | PurchasingDocHdrSourceHdrTaxAttributeUpdateCode | TAX_ATTRIBUTE_UPDATE_CODE | — | — |
| 104 | PurchasingDocHdrSourceHdrTaxDocumentSubtype | TAX_DOCUMENT_SUBTYPE | — | — |
| 105 | PurchasingDocHdrSourceHdrTermsId | TERMS_ID | — | — |
| 106 | PurchasingDocHdrSourceHdrTypeLookupCode | TYPE_LOOKUP_CODE | — | — |
| 107 | PurchasingDocHdrSourceHdrUpdateSourcingRulesFlag | UPDATE_SOURCING_RULES_FLAG | — | — |
| 108 | PurchasingDocHdrSourceHdrUseNeedByDate | USE_NEED_BY_DATE | — | — |
| 109 | PurchasingDocHdrSourceHdrUseShipTo | USE_SHIP_TO | — | — |
| 110 | PurchasingDocHdrSourceHdrVendorContactId | VENDOR_CONTACT_ID | — | — |
| 111 | PurchasingDocHdrSourceHdrVendorId | VENDOR_ID | — | — |
| 112 | PurchasingDocHdrSourceHdrVendorOrderNum | VENDOR_ORDER_NUM | — | — |
| 113 | PurchasingDocHdrSourceHdrVendorSiteId | VENDOR_SITE_ID | — | — |
| 114 | PurchasingDocHdrSourceHdrXmlChangeSendDate | XML_CHANGE_SEND_DATE | — | — |
| 115 | PurchasingDocHdrSourceHdrXmlFlag | XML_FLAG | — | — |
| 116 | PurchasingDocHdrSourceHdrXmlSendDate | XML_SEND_DATE | — | — |
| 117 | PurchasingDocumentHeaderAcceptanceDueDate | ACCEPTANCE_DUE_DATE | — | — |
| 118 | PurchasingDocumentHeaderAcceptanceRequiredFlag | ACCEPTANCE_REQUIRED_FLAG | — | — |
| 119 | PurchasingDocumentHeaderAcceptanceWithinDays | ACCEPTANCE_WITHIN_DAYS | — | — |
| 120 | PurchasingDocumentHeaderAgentId | AGENT_ID | — | — |
| 121 | PurchasingDocumentHeaderAmountLimit | AMOUNT_LIMIT | — | — |
| 122 | PurchasingDocumentHeaderAmountReleased | AMOUNT_RELEASED | — | — |
| 123 | PurchasingDocumentHeaderApprovedDate | APPROVED_DATE | — | — |
| 124 | PurchasingDocumentHeaderApprovedFlag | APPROVED_FLAG | — | — |
| 125 | PurchasingDocumentHeaderAutoSourcingFlag | AUTO_SOURCING_FLAG | — | — |
| 126 | PurchasingDocumentHeaderBillToLocationId | BILL_TO_LOCATION_ID | — | — |
| 127 | PurchasingDocumentHeaderBilltoBuId | BILLTO_BU_ID | — | — |
| 128 | PurchasingDocumentHeaderBlanketTotalAmount | BLANKET_TOTAL_AMOUNT | — | — |
| 129 | PurchasingDocumentHeaderCancelFlag | CANCEL_FLAG | — | — |
| 130 | PurchasingDocumentHeaderCarrierId | CARRIER_ID | — | — |
| 131 | PurchasingDocumentHeaderCatAdminAuthEnabledFlag | CAT_ADMIN_AUTH_ENABLED_FLAG | — | — |
| 132 | PurchasingDocumentHeaderCbcAccountingDate | CBC_ACCOUNTING_DATE | — | — |
| 133 | PurchasingDocumentHeaderChangeRequestedBy | CHANGE_REQUESTED_BY | — | — |
| 134 | PurchasingDocumentHeaderChangeSummary | CHANGE_SUMMARY | — | — |
| 135 | PurchasingDocumentHeaderClosedDate | CLOSED_DATE | — | — |
| 136 | PurchasingDocumentHeaderComments | COMMENTS | — | — |
| 137 | PurchasingDocumentHeaderConfirmingOrderFlag | CONFIRMING_ORDER_FLAG | — | — |
| 138 | PurchasingDocumentHeaderConsignedConsumptionFlag | CONSIGNED_CONSUMPTION_FLAG | — | — |
| 139 | PurchasingDocumentHeaderConsumeReqDemandFlag | CONSUME_REQ_DEMAND_FLAG | — | — |
| 140 | PurchasingDocumentHeaderContermsArticlesUpdDate | CONTERMS_ARTICLES_UPD_DATE | — | — |
| 141 | PurchasingDocumentHeaderContermsDelivUpdDate | CONTERMS_DELIV_UPD_DATE | — | — |
| 142 | PurchasingDocumentHeaderContermsExistFlag | CONTERMS_EXIST_FLAG | — | — |
| 143 | PurchasingDocumentHeaderCpaReference | CPA_REFERENCE | — | — |
| 144 | PurchasingDocumentHeaderCreatedBy | CREATED_BY | — | — |
| 145 | PurchasingDocumentHeaderCreatedLanguage | CREATED_LANGUAGE | — | — |
| 146 | PurchasingDocumentHeaderCreationDate | CREATION_DATE | — | — |
| 147 | PurchasingDocumentHeaderCurrencyCode | CURRENCY_CODE | — | — |
| 148 | PurchasingDocumentHeaderCurrentVersionId | CURRENT_VERSION_ID | — | — |
| 149 | PurchasingDocumentHeaderDefaultPoTradeOrgId | DEFAULT_PO_TRADE_ORG_ID | — | — |
| 150 | PurchasingDocumentHeaderDefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | — |
| 151 | PurchasingDocumentHeaderDocumentCreationMethod | DOCUMENT_CREATION_METHOD | — | — |
| 152 | PurchasingDocumentHeaderDocumentStatus | DOCUMENT_STATUS | — | — |
| 153 | PurchasingDocumentHeaderEdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 154 | PurchasingDocumentHeaderEdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 155 | PurchasingDocumentHeaderEmailAddress | EMAIL_ADDRESS | — | — |
| 156 | PurchasingDocumentHeaderEnabledFlag | ENABLED_FLAG | — | — |
| 157 | PurchasingDocumentHeaderEncumbranceRequiredFlag | ENCUMBRANCE_REQUIRED_FLAG | — | — |
| 158 | PurchasingDocumentHeaderEndDate | END_DATE | — | — |
| 159 | PurchasingDocumentHeaderFax | FAX | — | — |
| 160 | PurchasingDocumentHeaderFirmDate | FIRM_DATE | — | — |
| 161 | PurchasingDocumentHeaderFirmStatusLookupCode | FIRM_STATUS_LOOKUP_CODE | — | — |
| 162 | PurchasingDocumentHeaderFobLookupCode | FOB_LOOKUP_CODE | — | — |
| 163 | PurchasingDocumentHeaderFreightTermsLookupCode | FREIGHT_TERMS_LOOKUP_CODE | — | — |
| 164 | PurchasingDocumentHeaderFromHeaderId | FROM_HEADER_ID | — | — |
| 165 | PurchasingDocumentHeaderFromTypeLookupCode | FROM_TYPE_LOOKUP_CODE | — | — |
| 166 | PurchasingDocumentHeaderFrozenFlag | FROZEN_FLAG | — | — |
| 167 | PurchasingDocumentHeaderFundsStatus | FUNDS_STATUS | — | — |
| 168 | PurchasingDocumentHeaderGenerateOrdersAutomatic | GENERATE_ORDERS_AUTOMATIC | — | — |
| 169 | PurchasingDocumentHeaderGovernmentContext | GOVERNMENT_CONTEXT | — | — |
| 170 | PurchasingDocumentHeaderGroupRequisitionLines | GROUP_REQUISITION_LINES | — | — |
| 171 | PurchasingDocumentHeaderGroupRequisitions | GROUP_REQUISITIONS | — | — |
| 172 | PurchasingDocumentHeaderInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | — |
| 173 | PurchasingDocumentHeaderJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 174 | PurchasingDocumentHeaderJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 175 | PurchasingDocumentHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 176 | PurchasingDocumentHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 177 | PurchasingDocumentHeaderLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 178 | PurchasingDocumentHeaderLastUpdatedProgram | LAST_UPDATED_PROGRAM | — | — |
| 179 | PurchasingDocumentHeaderMinReleaseAmount | MIN_RELEASE_AMOUNT | — | — |
| 180 | PurchasingDocumentHeaderNoteToAuthorizer | NOTE_TO_AUTHORIZER | — | — |
| 181 | PurchasingDocumentHeaderNoteToReceiver | NOTE_TO_RECEIVER | — | — |
| 182 | PurchasingDocumentHeaderNoteToVendor | NOTE_TO_VENDOR | — | — |
| 183 | PurchasingDocumentHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 184 | PurchasingDocumentHeaderOrchestrationOrderFlag | ORCHESTRATION_ORDER_FLAG | — | — |
| 185 | PurchasingDocumentHeaderPayOnCode | PAY_ON_CODE | — | — |
| 186 | PurchasingDocumentHeaderPcardId | PCARD_ID | — | — |
| 187 | PurchasingDocumentHeaderPendingSignatureFlag | PENDING_SIGNATURE_FLAG | — | — |
| 188 | PurchasingDocumentHeaderPoHeaderId | PO_HEADER_ID | — | — |
| 189 | PurchasingDocumentHeaderPrcBuId | PRC_BU_ID | — | — |
| 190 | PurchasingDocumentHeaderPriceUpdateTolerance | PRICE_UPDATE_TOLERANCE | — | — |
| 191 | PurchasingDocumentHeaderProgramAppName | PROGRAM_APP_NAME | — | — |
| 192 | PurchasingDocumentHeaderProgramName | PROGRAM_NAME | — | — |
| 193 | PurchasingDocumentHeaderRate | RATE | — | — |
| 194 | PurchasingDocumentHeaderRateDate | RATE_DATE | — | — |
| 195 | PurchasingDocumentHeaderRateType | RATE_TYPE | — | — |
| 196 | PurchasingDocumentHeaderReferenceNum | REFERENCE_NUM | — | — |
| 197 | PurchasingDocumentHeaderReleaseMethod | RELEASE_METHOD | — | — |
| 198 | PurchasingDocumentHeaderReqBuId | REQ_BU_ID | — | — |
| 199 | PurchasingDocumentHeaderRequestId | REQUEST_ID | — | — |
| 200 | PurchasingDocumentHeaderRetroPriceApplyUpdatesFlag | RETRO_PRICE_APPLY_UPDATES_FLAG | — | — |
| 201 | PurchasingDocumentHeaderRetroPriceCommUpdatesFlag | RETRO_PRICE_COMM_UPDATES_FLAG | — | — |
| 202 | PurchasingDocumentHeaderReviewAutogeneratedReleases | REVIEW_AUTOGENERATED_RELEASES | — | — |
| 203 | PurchasingDocumentHeaderRevisedDate | REVISED_DATE | — | — |
| 204 | PurchasingDocumentHeaderRevisionNum | REVISION_NUM | — | — |
| 205 | PurchasingDocumentHeaderSegment1 | SEGMENT1 | — | ✅ |
| 206 | PurchasingDocumentHeaderSegment2 | SEGMENT2 | — | — |
| 207 | PurchasingDocumentHeaderSegment3 | SEGMENT3 | — | — |
| 208 | PurchasingDocumentHeaderSegment4 | SEGMENT4 | — | — |
| 209 | PurchasingDocumentHeaderSegment5 | SEGMENT5 | — | — |
| 210 | PurchasingDocumentHeaderShipToLocationId | SHIP_TO_LOCATION_ID | — | — |
| 211 | PurchasingDocumentHeaderShippingControl | SHIPPING_CONTROL | — | — |
| 212 | PurchasingDocumentHeaderSoldtoLeId | SOLDTO_LE_ID | — | — |
| 213 | PurchasingDocumentHeaderStartDate | START_DATE | — | — |
| 214 | PurchasingDocumentHeaderStyleId | STYLE_ID | — | — |
| 215 | PurchasingDocumentHeaderSubmitApprovalAutomatic | SUBMIT_APPROVAL_AUTOMATIC | — | — |
| 216 | PurchasingDocumentHeaderSubmitDate | SUBMIT_DATE | — | — |
| 217 | PurchasingDocumentHeaderSummaryFlag | SUMMARY_FLAG | — | — |
| 218 | PurchasingDocumentHeaderSupplierNotifMethod | SUPPLIER_NOTIF_METHOD | — | — |
| 219 | PurchasingDocumentHeaderTaxAttributeUpdateCode | TAX_ATTRIBUTE_UPDATE_CODE | — | — |
| 220 | PurchasingDocumentHeaderTaxDocumentSubtype | TAX_DOCUMENT_SUBTYPE | — | — |
| 221 | PurchasingDocumentHeaderTermsId | TERMS_ID | — | — |
| 222 | PurchasingDocumentHeaderTypeLookupCode | TYPE_LOOKUP_CODE | — | — |
| 223 | PurchasingDocumentHeaderUpdateSourcingRulesFlag | UPDATE_SOURCING_RULES_FLAG | — | — |
| 224 | PurchasingDocumentHeaderUseNeedByDate | USE_NEED_BY_DATE | — | — |
| 225 | PurchasingDocumentHeaderUseShipTo | USE_SHIP_TO | — | — |
| 226 | PurchasingDocumentHeaderVendorContactId | VENDOR_CONTACT_ID | — | — |
| 227 | PurchasingDocumentHeaderVendorId | VENDOR_ID | — | — |
| 228 | PurchasingDocumentHeaderVendorOrderNum | VENDOR_ORDER_NUM | — | — |
| 229 | PurchasingDocumentHeaderVendorSiteId | VENDOR_SITE_ID | — | — |
| 230 | PurchasingDocumentHeaderXmlChangeSendDate | XML_CHANGE_SEND_DATE | — | — |
| 231 | PurchasingDocumentHeaderXmlFlag | XML_FLAG | — | — |
| 232 | PurchasingDocumentHeaderXmlSendDate | XML_SEND_DATE | — | — |

### [[po_lines_all|PO_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PurchasingDocLineSourceLineAllowDescriptionUpdateFlag | ALLOW_DESCRIPTION_UPDATE_FLAG | — | — |
| 2 | PurchasingDocLineSourceLineAllowPriceOverrideFlag | ALLOW_PRICE_OVERRIDE_FLAG | — | — |
| 3 | PurchasingDocLineSourceLineAmount | AMOUNT | — | — |
| 4 | PurchasingDocLineSourceLineAmountReleased | AMOUNT_RELEASED | — | — |
| 5 | PurchasingDocLineSourceLineAuctionDisplayNumber | AUCTION_DISPLAY_NUMBER | — | — |
| 6 | PurchasingDocLineSourceLineAuctionHeaderId | AUCTION_HEADER_ID | — | — |
| 7 | PurchasingDocLineSourceLineAuctionLineNumber | AUCTION_LINE_NUMBER | — | — |
| 8 | PurchasingDocLineSourceLineBaseQty | BASE_QTY | — | — |
| 9 | PurchasingDocLineSourceLineBaseUnitPrice | BASE_UNIT_PRICE | — | — |
| 10 | PurchasingDocLineSourceLineBaseUom | BASE_UOM | — | — |
| 11 | PurchasingDocLineSourceLineBidLineNumber | BID_LINE_NUMBER | — | — |
| 12 | PurchasingDocLineSourceLineBidNumber | BID_NUMBER | — | — |
| 13 | PurchasingDocLineSourceLineCancelDate | CANCEL_DATE | — | — |
| 14 | PurchasingDocLineSourceLineCancelFlag | CANCEL_FLAG | — | — |
| 15 | PurchasingDocLineSourceLineCancelReason | CANCEL_REASON | — | — |
| 16 | PurchasingDocLineSourceLineCancelledBy | CANCELLED_BY | — | — |
| 17 | PurchasingDocLineSourceLineCapitalExpenseFlag | CAPITAL_EXPENSE_FLAG | — | — |
| 18 | PurchasingDocLineSourceLineClosedBy | CLOSED_BY | — | — |
| 19 | PurchasingDocLineSourceLineClosedDate | CLOSED_DATE | — | — |
| 20 | PurchasingDocLineSourceLineClosedReason | CLOSED_REASON | — | — |
| 21 | PurchasingDocLineSourceLineCommittedAmount | COMMITTED_AMOUNT | — | — |
| 22 | PurchasingDocLineSourceLineContractId | CONTRACT_ID | — | — |
| 23 | PurchasingDocLineSourceLineContractorFirstName | CONTRACTOR_FIRST_NAME | — | — |
| 24 | PurchasingDocLineSourceLineContractorLastName | CONTRACTOR_LAST_NAME | — | — |
| 25 | PurchasingDocLineSourceLineCreatedBy | CREATED_BY | — | — |
| 26 | PurchasingDocLineSourceLineCreationDate | CREATION_DATE | — | — |
| 27 | PurchasingDocLineSourceLineExpirationDate | EXPIRATION_DATE | — | — |
| 28 | PurchasingDocLineSourceLineFirmDate | FIRM_DATE | — | — |
| 29 | PurchasingDocLineSourceLineFirmStatusLookupCode | FIRM_STATUS_LOOKUP_CODE | — | — |
| 30 | PurchasingDocLineSourceLineFromHeaderId | FROM_HEADER_ID | — | — |
| 31 | PurchasingDocLineSourceLineFromLineId | FROM_LINE_ID | — | — |
| 32 | PurchasingDocLineSourceLineFromLineLocationId | FROM_LINE_LOCATION_ID | — | — |
| 33 | PurchasingDocLineSourceLineFundsStatus | FUNDS_STATUS | — | — |
| 34 | PurchasingDocLineSourceLineGovernmentContext | GOVERNMENT_CONTEXT | — | — |
| 35 | PurchasingDocLineSourceLineHazardClassId | HAZARD_CLASS_ID | — | — |
| 36 | PurchasingDocLineSourceLineItemDescription | ITEM_DESCRIPTION | — | — |
| 37 | PurchasingDocLineSourceLineItemId | ITEM_ID | — | — |
| 38 | PurchasingDocLineSourceLineItemRevision | ITEM_REVISION | — | — |
| 39 | PurchasingDocLineSourceLineJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 40 | PurchasingDocLineSourceLineJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 41 | PurchasingDocLineSourceLineJobId | JOB_ID | — | — |
| 42 | PurchasingDocLineSourceLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 43 | PurchasingDocLineSourceLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 44 | PurchasingDocLineSourceLineLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 45 | PurchasingDocLineSourceLineLastUpdatedProgram | LAST_UPDATED_PROGRAM | — | — |
| 46 | PurchasingDocLineSourceLineLineNum | LINE_NUM | — | — |
| 47 | PurchasingDocLineSourceLineLineReferenceNum | LINE_REFERENCE_NUM | — | — |
| 48 | PurchasingDocLineSourceLineLineStatus | LINE_STATUS | — | — |
| 49 | PurchasingDocLineSourceLineLineTypeId | LINE_TYPE_ID | — | — |
| 50 | PurchasingDocLineSourceLineListPricePerUnit | LIST_PRICE_PER_UNIT | — | — |
| 51 | PurchasingDocLineSourceLineManualPriceChangeFlag | MANUAL_PRICE_CHANGE_FLAG | — | — |
| 52 | PurchasingDocLineSourceLineMarketPrice | MARKET_PRICE | — | — |
| 53 | PurchasingDocLineSourceLineMatchingBasis | MATCHING_BASIS | — | — |
| 54 | PurchasingDocLineSourceLineMaxRetainageAmount | MAX_RETAINAGE_AMOUNT | — | — |
| 55 | PurchasingDocLineSourceLineMinReleaseAmount | MIN_RELEASE_AMOUNT | — | — |
| 56 | PurchasingDocLineSourceLineNegotiatedByPreparerFlag | NEGOTIATED_BY_PREPARER_FLAG | — | — |
| 57 | PurchasingDocLineSourceLineNotToExceedPrice | NOT_TO_EXCEED_PRICE | — | — |
| 58 | PurchasingDocLineSourceLineNoteToVendor | NOTE_TO_VENDOR | — | — |
| 59 | PurchasingDocLineSourceLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 60 | PurchasingDocLineSourceLineOkeContractHeaderId | OKE_CONTRACT_HEADER_ID | — | — |
| 61 | PurchasingDocLineSourceLineOkeContractVersionId | OKE_CONTRACT_VERSION_ID | — | — |
| 62 | PurchasingDocLineSourceLineOrderTypeLookupCode | ORDER_TYPE_LOOKUP_CODE | — | — |
| 63 | PurchasingDocLineSourceLineOverToleranceErrorFlag | OVER_TOLERANCE_ERROR_FLAG | — | — |
| 64 | PurchasingDocLineSourceLinePJC_CONTEXT_CATEGORY | PJC_CONTEXT_CATEGORY | — | — |
| 65 | PurchasingDocLineSourceLinePoHeaderId | PO_HEADER_ID | — | — |
| 66 | PurchasingDocLineSourceLinePoLineId | PO_LINE_ID | — | — |
| 67 | PurchasingDocLineSourceLinePrcBuId | PRC_BU_ID | — | — |
| 68 | PurchasingDocLineSourceLinePreferredGrade | PREFERRED_GRADE | — | — |
| 69 | PurchasingDocLineSourceLinePriceBreakLookupCode | PRICE_BREAK_LOOKUP_CODE | — | — |
| 70 | PurchasingDocLineSourceLinePriceTypeLookupCode | PRICE_TYPE_LOOKUP_CODE | — | — |
| 71 | PurchasingDocLineSourceLineProgramAppName | PROGRAM_APP_NAME | — | — |
| 72 | PurchasingDocLineSourceLineProgramName | PROGRAM_NAME | — | — |
| 73 | PurchasingDocLineSourceLineProgressPaymentRate | PROGRESS_PAYMENT_RATE | — | — |
| 74 | PurchasingDocLineSourceLinePurchaseBasis | PURCHASE_BASIS | — | — |
| 75 | PurchasingDocLineSourceLineQcGrade | QC_GRADE | — | — |
| 76 | PurchasingDocLineSourceLineQtyRcvTolerance | QTY_RCV_TOLERANCE | — | — |
| 77 | PurchasingDocLineSourceLineQuantity | QUANTITY | — | — |
| 78 | PurchasingDocLineSourceLineQuantityCommitted | QUANTITY_COMMITTED | — | — |
| 79 | PurchasingDocLineSourceLineRecoupmentRate | RECOUPMENT_RATE | — | — |
| 80 | PurchasingDocLineSourceLineReferenceNum | REFERENCE_NUM | — | — |
| 81 | PurchasingDocLineSourceLineReqBuId | REQ_BU_ID | — | — |
| 82 | PurchasingDocLineSourceLineRequestId | REQUEST_ID | — | — |
| 83 | PurchasingDocLineSourceLineRetainageRate | RETAINAGE_RATE | — | — |
| 84 | PurchasingDocLineSourceLineRetroactiveDate | RETROACTIVE_DATE | — | — |
| 85 | PurchasingDocLineSourceLineSecondaryQuantity | SECONDARY_QUANTITY | — | — |
| 86 | PurchasingDocLineSourceLineSecondaryUomCode | SECONDARY_UOM_CODE | — | — |
| 87 | PurchasingDocLineSourceLineSourceDocRevNum | SOURCE_DOC_REV_NUM | — | — |
| 88 | PurchasingDocLineSourceLineStartDate | START_DATE | — | — |
| 89 | PurchasingDocLineSourceLineSupplierPartAuxid | SUPPLIER_PART_AUXID | — | — |
| 90 | PurchasingDocLineSourceLineSupplierRefNumber | SUPPLIER_REF_NUMBER | — | — |
| 91 | PurchasingDocLineSourceLineSvcAmountNotifSent | SVC_AMOUNT_NOTIF_SENT | — | — |
| 92 | PurchasingDocLineSourceLineSvcCompletionNotifSent | SVC_COMPLETION_NOTIF_SENT | — | — |
| 93 | PurchasingDocLineSourceLineTaxAttributeUpdateCode | TAX_ATTRIBUTE_UPDATE_CODE | — | — |
| 94 | PurchasingDocLineSourceLineTaxCodeId | TAX_CODE_ID | — | — |
| 95 | PurchasingDocLineSourceLineTaxName | TAX_NAME | — | — |
| 96 | PurchasingDocLineSourceLineTaxableFlag | TAXABLE_FLAG | — | — |
| 97 | PurchasingDocLineSourceLineType1099 | TYPE_1099 | — | — |
| 98 | PurchasingDocLineSourceLineUnNumberId | UN_NUMBER_ID | — | — |
| 99 | PurchasingDocLineSourceLineUnitPrice | UNIT_PRICE | — | — |
| 100 | PurchasingDocLineSourceLineUnorderedFlag | UNORDERED_FLAG | — | — |
| 101 | PurchasingDocLineSourceLineUomCode | UOM_CODE | — | — |
| 102 | PurchasingDocLineSourceLineVendorProductNum | VENDOR_PRODUCT_NUM | — | — |
| 103 | PurchasingDocumentLineAllowDescriptionUpdateFlag | ALLOW_DESCRIPTION_UPDATE_FLAG | — | — |
| 104 | PurchasingDocumentLineAllowPriceOverrideFlag | ALLOW_PRICE_OVERRIDE_FLAG | — | — |
| 105 | PurchasingDocumentLineAmount | AMOUNT | — | — |
| 106 | PurchasingDocumentLineAuctionDisplayNumber | AUCTION_DISPLAY_NUMBER | — | — |
| 107 | PurchasingDocumentLineAuctionHeaderId | AUCTION_HEADER_ID | — | — |
| 108 | PurchasingDocumentLineAuctionLineNumber | AUCTION_LINE_NUMBER | — | — |
| 109 | PurchasingDocumentLineBaseQty | BASE_QTY | — | — |
| 110 | PurchasingDocumentLineBaseUnitPrice | BASE_UNIT_PRICE | — | — |
| 111 | PurchasingDocumentLineBaseUom | BASE_UOM | — | — |
| 112 | PurchasingDocumentLineBidLineNumber | BID_LINE_NUMBER | — | — |
| 113 | PurchasingDocumentLineBidNumber | BID_NUMBER | — | — |
| 114 | PurchasingDocumentLineCancelDate | CANCEL_DATE | — | — |
| 115 | PurchasingDocumentLineCancelFlag | CANCEL_FLAG | — | — |
| 116 | PurchasingDocumentLineCancelReason | CANCEL_REASON | — | — |
| 117 | PurchasingDocumentLineCancelledBy | CANCELLED_BY | — | — |
| 118 | PurchasingDocumentLineCapitalExpenseFlag | CAPITAL_EXPENSE_FLAG | — | — |
| 119 | PurchasingDocumentLineCategoryId | CATEGORY_ID | — | — |
| 120 | PurchasingDocumentLineClosedBy | CLOSED_BY | — | — |
| 121 | PurchasingDocumentLineClosedDate | CLOSED_DATE | — | — |
| 122 | PurchasingDocumentLineClosedReason | CLOSED_REASON | — | — |
| 123 | PurchasingDocumentLineCommittedAmount | COMMITTED_AMOUNT | — | — |
| 124 | PurchasingDocumentLineConsignmentLineFlag | CONSIGNMENT_LINE_FLAG | — | — |
| 125 | PurchasingDocumentLineContractId | CONTRACT_ID | — | — |
| 126 | PurchasingDocumentLineContractorFirstName | CONTRACTOR_FIRST_NAME | — | — |
| 127 | PurchasingDocumentLineContractorLastName | CONTRACTOR_LAST_NAME | — | — |
| 128 | PurchasingDocumentLineCreatedBy | CREATED_BY | — | — |
| 129 | PurchasingDocumentLineCreationDate | CREATION_DATE | — | — |
| 130 | PurchasingDocumentLineExpirationDate | EXPIRATION_DATE | — | — |
| 131 | PurchasingDocumentLineFirmDate | FIRM_DATE | — | — |
| 132 | PurchasingDocumentLineFirmStatusLookupCode | FIRM_STATUS_LOOKUP_CODE | — | — |
| 133 | PurchasingDocumentLineFromHeaderId | FROM_HEADER_ID | — | — |
| 134 | PurchasingDocumentLineFromLineId | FROM_LINE_ID | — | — |
| 135 | PurchasingDocumentLineFromLineLocationId | FROM_LINE_LOCATION_ID | — | — |
| 136 | PurchasingDocumentLineFundsStatus | FUNDS_STATUS | — | — |
| 137 | PurchasingDocumentLineGovernmentContext | GOVERNMENT_CONTEXT | — | — |
| 138 | PurchasingDocumentLineHazardClassId | HAZARD_CLASS_ID | — | — |
| 139 | PurchasingDocumentLineItemDescription | ITEM_DESCRIPTION | — | — |
| 140 | PurchasingDocumentLineItemId | ITEM_ID | — | — |
| 141 | PurchasingDocumentLineItemRevision | ITEM_REVISION | — | — |
| 142 | PurchasingDocumentLineJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 143 | PurchasingDocumentLineJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 144 | PurchasingDocumentLineJobId | JOB_ID | — | — |
| 145 | PurchasingDocumentLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 146 | PurchasingDocumentLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 147 | PurchasingDocumentLineLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 148 | PurchasingDocumentLineLastUpdatedProgram | LAST_UPDATED_PROGRAM | — | — |
| 149 | PurchasingDocumentLineLineNum | LINE_NUM | — | — |
| 150 | PurchasingDocumentLineLineReferenceNum | LINE_REFERENCE_NUM | — | — |
| 151 | PurchasingDocumentLineLineStatus | LINE_STATUS | — | — |
| 152 | PurchasingDocumentLineLineTypeId | LINE_TYPE_ID | — | — |
| 153 | PurchasingDocumentLineListPricePerUnit | LIST_PRICE_PER_UNIT | — | — |
| 154 | PurchasingDocumentLineManualPriceChangeFlag | MANUAL_PRICE_CHANGE_FLAG | — | — |
| 155 | PurchasingDocumentLineMarketPrice | MARKET_PRICE | — | — |
| 156 | PurchasingDocumentLineMatchingBasis | MATCHING_BASIS | — | — |
| 157 | PurchasingDocumentLineMaxRetainageAmount | MAX_RETAINAGE_AMOUNT | — | — |
| 158 | PurchasingDocumentLineMinReleaseAmount | MIN_RELEASE_AMOUNT | — | — |
| 159 | PurchasingDocumentLineNegotiatedByPreparerFlag | NEGOTIATED_BY_PREPARER_FLAG | — | — |
| 160 | PurchasingDocumentLineNotToExceedPrice | NOT_TO_EXCEED_PRICE | — | — |
| 161 | PurchasingDocumentLineNoteToVendor | NOTE_TO_VENDOR | — | — |
| 162 | PurchasingDocumentLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 163 | PurchasingDocumentLineOkeContractHeaderId | OKE_CONTRACT_HEADER_ID | — | — |
| 164 | PurchasingDocumentLineOkeContractVersionId | OKE_CONTRACT_VERSION_ID | — | — |
| 165 | PurchasingDocumentLineOrderTypeLookupCode | ORDER_TYPE_LOOKUP_CODE | — | — |
| 166 | PurchasingDocumentLineOverToleranceErrorFlag | OVER_TOLERANCE_ERROR_FLAG | — | — |
| 167 | PurchasingDocumentLinePJC_CONTEXT_CATEGORY | PJC_CONTEXT_CATEGORY | — | — |
| 168 | PurchasingDocumentLinePoHeaderId | PO_HEADER_ID | — | — |
| 169 | PurchasingDocumentLinePoLineId | PO_LINE_ID | — | — |
| 170 | PurchasingDocumentLinePrcBuId | PRC_BU_ID | — | — |
| 171 | PurchasingDocumentLinePreferredGrade | PREFERRED_GRADE | — | — |
| 172 | PurchasingDocumentLinePriceBreakLookupCode | PRICE_BREAK_LOOKUP_CODE | — | — |
| 173 | PurchasingDocumentLinePriceTypeLookupCode | PRICE_TYPE_LOOKUP_CODE | — | — |
| 174 | PurchasingDocumentLineProgramAppName | PROGRAM_APP_NAME | — | — |
| 175 | PurchasingDocumentLineProgramName | PROGRAM_NAME | — | — |
| 176 | PurchasingDocumentLineProgressPaymentRate | PROGRESS_PAYMENT_RATE | — | — |
| 177 | PurchasingDocumentLinePurchaseBasis | PURCHASE_BASIS | — | — |
| 178 | PurchasingDocumentLineQcGrade | QC_GRADE | — | — |
| 179 | PurchasingDocumentLineQtyRcvTolerance | QTY_RCV_TOLERANCE | — | — |
| 180 | PurchasingDocumentLineQuantity | QUANTITY | — | — |
| 181 | PurchasingDocumentLineQuantityCommitted | QUANTITY_COMMITTED | — | — |
| 182 | PurchasingDocumentLineRecoupmentRate | RECOUPMENT_RATE | — | — |
| 183 | PurchasingDocumentLineReferenceNum | REFERENCE_NUM | — | — |
| 184 | PurchasingDocumentLineReqBuId | REQ_BU_ID | — | — |
| 185 | PurchasingDocumentLineRequestId | REQUEST_ID | — | — |
| 186 | PurchasingDocumentLineRetainageRate | RETAINAGE_RATE | — | — |
| 187 | PurchasingDocumentLineRetroactiveDate | RETROACTIVE_DATE | — | — |
| 188 | PurchasingDocumentLineSecondaryQuantity | SECONDARY_QUANTITY | — | — |
| 189 | PurchasingDocumentLineSecondaryUomCode | SECONDARY_UOM_CODE | — | — |
| 190 | PurchasingDocumentLineStartDate | START_DATE | — | — |
| 191 | PurchasingDocumentLineSupplierPartAuxid | SUPPLIER_PART_AUXID | — | — |
| 192 | PurchasingDocumentLineSupplierRefNumber | SUPPLIER_REF_NUMBER | — | — |
| 193 | PurchasingDocumentLineSvcAmountNotifSent | SVC_AMOUNT_NOTIF_SENT | — | — |
| 194 | PurchasingDocumentLineSvcCompletionNotifSent | SVC_COMPLETION_NOTIF_SENT | — | — |
| 195 | PurchasingDocumentLineTaxAttributeUpdateCode | TAX_ATTRIBUTE_UPDATE_CODE | — | — |
| 196 | PurchasingDocumentLineTaxCodeId | TAX_CODE_ID | — | — |
| 197 | PurchasingDocumentLineTaxName | TAX_NAME | — | — |
| 198 | PurchasingDocumentLineTaxableFlag | TAXABLE_FLAG | — | — |
| 199 | PurchasingDocumentLineType1099 | TYPE_1099 | — | — |
| 200 | PurchasingDocumentLineUnNumberId | UN_NUMBER_ID | — | — |
| 201 | PurchasingDocumentLineUnitPrice | UNIT_PRICE | — | — |
| 202 | PurchasingDocumentLineUnorderedFlag | UNORDERED_FLAG | — | — |
| 203 | PurchasingDocumentLineUomCode | UOM_CODE | — | — |
| 204 | PurchasingDocumentLineVendorProductNum | VENDOR_PRODUCT_NUM | — | — |

### [[po_un_numbers_vl|PO_UN_NUMBERS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PurchasingUnNumberCreatedBy | CREATED_BY | — | — |
| 2 | PurchasingUnNumberCreationDate | CREATION_DATE | — | — |
| 3 | PurchasingUnNumberDescription | DESCRIPTION | — | — |
| 4 | PurchasingUnNumberHazardClassId | HAZARD_CLASS_ID | — | — |
| 5 | PurchasingUnNumberInactiveDate | INACTIVE_DATE | — | — |
| 6 | PurchasingUnNumberLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | PurchasingUnNumberLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | PurchasingUnNumberLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | PurchasingUnNumberObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | PurchasingUnNumberUnNumber | UN_NUMBER | — | — |
| 11 | PurchasingUnNumberUnNumberCode | UN_NUMBER_CODE | — | — |
| 12 | PurchasingUnNumberUnNumberId | UN_NUMBER_ID | — | — |

### [[po_versions_init_sequence_v|PO_VERSIONS_INIT_SEQUENCE_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PurchasingDocumentVersionAcceptedDate | ACCEPTED_DATE | — | — |
| 2 | PurchasingDocumentVersionCancelBackingReqFlag | CANCEL_BACKING_REQ_FLAG | — | — |
| 3 | PurchasingDocumentVersionCancelDocFlag | CANCEL_DOC_FLAG | — | — |
| 4 | PurchasingDocumentVersionChangeOrderDesc | CHANGE_ORDER_DESC | — | — |
| 5 | PurchasingDocumentVersionChangeOrderStatus | CHANGE_ORDER_STATUS | — | — |
| 6 | PurchasingDocumentVersionChangeOrderType | CHANGE_ORDER_TYPE | — | — |
| 7 | PurchasingDocumentVersionCoCanceledByRole | CO_CANCELED_BY_ROLE | — | — |
| 8 | PurchasingDocumentVersionCoCanceledByUserId | CO_CANCELED_BY_USER_ID | — | — |
| 9 | PurchasingDocumentVersionCoCanceledFlag | CO_CANCELED_FLAG | — | — |
| 10 | PurchasingDocumentVersionCoNum | CO_NUM | — | — |
| 11 | PurchasingDocumentVersionCoSequence | CO_SEQUENCE | — | — |
| 12 | PurchasingDocumentVersionCommunicatedDate | COMMUNICATED_DATE | — | — |
| 13 | PurchasingDocumentVersionCommunicatedToSupplier | COMMUNICATED_TO_SUPPLIER | — | — |
| 14 | PurchasingDocumentVersionCreatedBy | CREATED_BY | — | — |
| 15 | PurchasingDocumentVersionCreatedByProgramName | CREATED_BY_PROGRAM_NAME | — | — |
| 16 | PurchasingDocumentVersionCreationDate | CREATION_DATE | — | — |
| 17 | PurchasingDocumentVersionDocumentDate | DOCUMENT_DATE | — | — |
| 18 | PurchasingDocumentVersionExternalSystemFlag | EXTERNAL_SYSTEM_FLAG | — | — |
| 19 | PurchasingDocumentVersionFundsStatus | FUNDS_STATUS | — | — |
| 20 | PurchasingDocumentVersionJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 21 | PurchasingDocumentVersionJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 22 | PurchasingDocumentVersionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 23 | PurchasingDocumentVersionLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 24 | PurchasingDocumentVersionLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 25 | PurchasingDocumentVersionModifiedFlag | MODIFIED_FLAG | — | — |
| 26 | PurchasingDocumentVersionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 27 | PurchasingDocumentVersionOnlineReportId | ONLINE_REPORT_ID | — | — |
| 28 | PurchasingDocumentVersionOriginatorId | ORIGINATOR_ID | — | — |
| 29 | PurchasingDocumentVersionOriginatorRole | ORIGINATOR_ROLE | — | — |
| 30 | PurchasingDocumentVersionPendingResponseRole | PENDING_RESPONSE_ROLE | — | — |
| 31 | PurchasingDocumentVersionPoHeaderId | PO_HEADER_ID | — | — |
| 32 | PurchasingDocumentVersionProcessedDate | PROCESSED_DATE | — | ✅ |
| 33 | PurchasingDocumentVersionProgramAppName | PROGRAM_APP_NAME | — | — |
| 34 | PurchasingDocumentVersionProgramName | PROGRAM_NAME | — | — |
| 35 | PurchasingDocumentVersionRejectedFlag | REJECTED_FLAG | — | — |
| 36 | PurchasingDocumentVersionRequestDate | REQUEST_DATE | — | — |
| 37 | PurchasingDocumentVersionRequestId | REQUEST_ID | — | — |
| 38 | PurchasingDocumentVersionRevisionNum | REVISION_NUM | — | — |
| 39 | PurchasingDocumentVersionSubmittedDate | SUBMITTED_DATE | — | — |
| 40 | PurchasingDocumentVersionVersionId | VERSION_ID | — | — |
| 41 | PurchasingDocumentVersionWithdrawnFlag | WITHDRAWN_FLAG | — | — |

### [[zx_fc_business_categories_v|ZX_FC_BUSINESS_CATEGORIES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionBizCategoriesApplicationId | APPLICATION_ID | — | — |
| 2 | TransactionBizCategoriesClassificationCode | CLASSIFICATION_CODE | — | — |
| 3 | TransactionBizCategoriesClassificationId | CLASSIFICATION_ID | — | — |
| 4 | TransactionBizCategoriesClassificationName | CLASSIFICATION_NAME | — | — |
| 5 | TransactionBizCategoriesConcatClassifCode | CONCAT_CLASSIF_CODE | — | — |
| 6 | TransactionBizCategoriesEntityCode | ENTITY_CODE | — | — |
| 7 | TransactionBizCategoriesEventClassCode | EVENT_CLASS_CODE | — | — |
| 8 | TransactionBizCategoriesTaxEvntClsCode | TAX_EVNT_CLS_CODE | — | — |

### [[zx_fc_document_fiscal_v|ZX_FC_DOCUMENT_FISCAL_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DocFisClassificationClassificationCode | CLASSIFICATION_CODE | — | — |
| 2 | DocFisClassificationClassificationId | CLASSIFICATION_ID | — | — |
| 3 | DocFisClassificationClassificationName | CLASSIFICATION_NAME | — | — |

### [[zx_fc_intended_use_v|ZX_FC_INTENDED_USE_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LineIntendedUseClassificationId | CLASSIFICATION_ID | — | — |
| 2 | LineIntendedUseName | NAME | — | — |

### [[zx_fc_product_categories_v|ZX_FC_PRODUCT_CATEGORIES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProductCategoriesClassificationCode | CLASSIFICATION_CODE | — | — |
| 2 | ProductCategoriesClassificationName | CLASSIFICATION_NAME | — | — |
| 3 | ProductCategoriesConcatLeafName | CONCAT_LEAF_NAME | — | — |

### [[zx_fc_product_fiscal_v|ZX_FC_PRODUCT_FISCAL_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProductFiscClassificationsCategoryId | CATEGORY_ID | — | — |
| 2 | ProductFiscClassificationsCategorySetId | CATEGORY_SET_ID | — | — |
| 3 | ProductFiscClassificationsClassificationCode | CLASSIFICATION_CODE | — | — |
| 4 | ProductFiscClassificationsClassificationName | CLASSIFICATION_NAME | — | — |
| 5 | ProductFiscClassificationsCountryCode | COUNTRY_CODE | — | — |
| 6 | ProductFiscClassificationsStructureId | STRUCTURE_ID | — | — |

### [[zx_fc_user_defined_v|ZX_FC_USER_DEFINED_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserDefinedFiscClassClassificationCode | CLASSIFICATION_CODE | — | — |
| 2 | UserDefinedFiscClassClassificationName | CLASSIFICATION_NAME | — | — |
| 3 | UserDefinedFiscClassCountryCode | COUNTRY_CODE | — | — |

### [[zx_input_classifications_v|ZX_INPUT_CLASSIFICATIONS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InputTaxClassificationsLookupCode | LOOKUP_CODE | — | — |
| 2 | InputTaxClassificationsMeaning | MEANING | — | — |
| 3 | InputTaxClassificationsSetId | SET_ID | — | — |

### [[zx_product_types_v|ZX_PRODUCT_TYPES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProductTypesClassificationCode | CLASSIFICATION_CODE | — | — |
| 2 | ProductTypesClassificationName | CLASSIFICATION_NAME | — | — |

### [[zx_registrations|ZX_REGISTRATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FirstTaxRegRegistrationId | REGISTRATION_ID | — | — |
| 2 | FirstTaxRegRegistrationNumber | REGISTRATION_NUMBER | — | — |
| 3 | ThirdTaxRegRegistrationId | REGISTRATION_ID | — | — |
| 4 | ThirdTaxRegRegistrationNumber | REGISTRATION_NUMBER | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
