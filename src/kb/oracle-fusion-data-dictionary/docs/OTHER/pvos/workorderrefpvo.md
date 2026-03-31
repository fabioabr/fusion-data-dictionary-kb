---
id: DOC-OTHER-PVO-WorkOrderRefPVO
doc_type: system-doc
title: "WorkOrderRefPVO — PVO Cross-Module"
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
  - WorkOrderRefPVO
  - workorderrefpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WorkOrderRefPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Work Order Ref. Acessa as tabelas: CSE_ASSETS_B, CSE_CONDITION_EVENT_CODES_B, CSE_W_CONTRACTS (+12).

**Caminho:** `FscmTopModelAM.WorkOrderAM.WorkOrderRefPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 556 | 15 | 1 | 125 | 22% |

---

## 🔗 Tabelas Relacionadas

- [[cse_assets_b|CSE_ASSETS_B]] — 4 atributos
- [[cse_condition_event_codes_b|CSE_CONDITION_EVENT_CODES_B]] — 2 atributos
- [[cse_w_contracts|CSE_W_CONTRACTS]] — 6 atributos
- [[cse_w_coverages_b|CSE_W_COVERAGES_B]] — 6 atributos
- [[cse_w_coverages_tl|CSE_W_COVERAGES_TL]] — 3 atributos
- [[hz_parties|HZ_PARTIES]] — 77 atributos (13 BICC)
- [[inv_item_locations|INV_ITEM_LOCATIONS]] — 95 atributos
- [[poz_suppliers|POZ_SUPPLIERS]] — 110 atributos (15 BICC)
- [[poz_suppliers_v|POZ_SUPPLIERS_V]] — 2 atributos
- [[po_headers_all|PO_HEADERS_ALL]] — 146 atributos (41 BICC)
- [[wie_work_orders_b|WIE_WORK_ORDERS_B]] — 71 atributos (1 PKs, 50 BICC)
- [[wie_work_orders_tl|WIE_WORK_ORDERS_TL]] — 10 atributos (5 BICC)
- [[wie_wo_assets|WIE_WO_ASSETS]] — 4 atributos
- [[wie_wo_product_lots|WIE_WO_PRODUCT_LOTS]] — 15 atributos
- [[wis_work_methods_vl|WIS_WORK_METHODS_VL]] — 5 atributos (1 BICC)

---

## ⚙️ Atributos

### [[cse_assets_b|CSE_ASSETS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssetPEOAssetId | ASSET_ID | — | — |
| 2 | AssetPEOAssetNumber | ASSET_NUMBER | — | — |
| 3 | AssetPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 4 | AssetPEOSerialNumber | SERIAL_NUMBER | — | — |

### [[cse_condition_event_codes_b|CSE_CONDITION_EVENT_CODES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConditionEventCodeAnalyticsPEOConditionEventCode | CONDITION_EVENT_CODE | — | — |
| 2 | ConditionEventCodeAnalyticsPEOConditionEventCodeId | CONDITION_EVENT_CODE_ID | — | — |

### [[cse_w_contracts|CSE_W_CONTRACTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WarrantyContractPEOCalculatedExpirationDate | CALCULATED_EXPIRATION_DATE | — | — |
| 2 | WarrantyContractPEOContractEndDate | CONTRACT_END_DATE | — | — |
| 3 | WarrantyContractPEOContractId | CONTRACT_ID | — | — |
| 4 | WarrantyContractPEOContractNumber | CONTRACT_NUMBER | — | — |
| 5 | WarrantyContractPEOContractStartDate | CONTRACT_START_DATE | — | — |
| 6 | WarrantyContractPEOExternalReferenceNumber | EXTERNAL_REFERENCE_NUMBER | — | — |

### [[cse_w_coverages_b|CSE_W_COVERAGES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WarrantyCoverageBPEOAuthorizationRequiredFlag | AUTHORIZATION_REQUIRED_FLAG | — | — |
| 2 | WarrantyCoverageBPEOCoverageId | COVERAGE_ID | — | — |
| 3 | WarrantyCoverageBPEOInternalRepairAllowedFlag | INTERNAL_REPAIR_ALLOWED_FLAG | — | — |
| 4 | WarrantyCoverageBPEOLaborReimbursementFlag | LABOR_REIMBURSEMENT_FLAG | — | — |
| 5 | WarrantyCoverageBPEOPartsReimbursementFlag | PARTS_REIMBURSEMENT_FLAG | — | — |
| 6 | WarrantyCoverageBPEOPartsReturnRequiredFlag | PARTS_RETURN_REQUIRED_FLAG | — | — |

### [[cse_w_coverages_tl|CSE_W_COVERAGES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WarrantyCoverageTLPEOCoverageId | COVERAGE_ID | — | — |
| 2 | WarrantyCoverageTLPEOCoverageName | COVERAGE_NAME | — | — |
| 3 | WarrantyCoverageTLPEOLanguage | LANGUAGE | — | — |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyPEOCategoryCode | CATEGORY_CODE | — | — |
| 2 | PartyPEOCeoName | CEO_NAME | — | — |
| 3 | PartyPEOCertReasonCode | CERT_REASON_CODE | — | — |
| 4 | PartyPEOCertificationLevel | CERTIFICATION_LEVEL | — | — |
| 5 | PartyPEOCity | CITY | — | — |
| 6 | PartyPEOComments1 | COMMENTS | — | — |
| 7 | PartyPEOCountry | COUNTRY | — | — |
| 8 | PartyPEOCounty | COUNTY | — | — |
| 9 | PartyPEOCreatedBy2 | CREATED_BY | — | — |
| 10 | PartyPEOCreatedByModule | CREATED_BY_MODULE | — | — |
| 11 | PartyPEOCreationDate2 | CREATION_DATE | — | ✅ |
| 12 | PartyPEOCurrFyPotentialRevenue | CURR_FY_POTENTIAL_REVENUE | — | — |
| 13 | PartyPEODateOfBirth | DATE_OF_BIRTH | — | — |
| 14 | PartyPEODunsNumberC | DUNS_NUMBER_C | — | — |
| 15 | PartyPEOEmailAddress1 | EMAIL_ADDRESS | — | — |
| 16 | PartyPEOEmployeesTotal | EMPLOYEES_TOTAL | — | — |
| 17 | PartyPEOFiscalYearendMonth | FISCAL_YEAREND_MONTH | — | — |
| 18 | PartyPEOGender | GENDER | — | — |
| 19 | PartyPEOGroupType | GROUP_TYPE | — | — |
| 20 | PartyPEOGsaIndicatorFlag | GSA_INDICATOR_FLAG | — | — |
| 21 | PartyPEOHomeCountry | HOME_COUNTRY | — | — |
| 22 | PartyPEOHqBranchInd | HQ_BRANCH_IND | — | — |
| 23 | PartyPEOIdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | ✅ |
| 24 | PartyPEOIdenAddrPartySiteId | IDEN_ADDR_PARTY_SITE_ID | — | ✅ |
| 25 | PartyPEOInternalFlag | INTERNAL_FLAG | — | — |
| 26 | PartyPEOJgzzFiscalCode | JGZZ_FISCAL_CODE | — | — |
| 27 | PartyPEOLanguageName | LANGUAGE_NAME | — | — |
| 28 | PartyPEOLastUpdateDate2 | LAST_UPDATE_DATE | — | ✅ |
| 29 | PartyPEOLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 30 | PartyPEOLastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 31 | PartyPEOMaritalStatus | MARITAL_STATUS | — | — |
| 32 | PartyPEOMissionStatement | MISSION_STATEMENT | — | — |
| 33 | PartyPEONextFyPotentialRevenue | NEXT_FY_POTENTIAL_REVENUE | — | — |
| 34 | PartyPEOObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 35 | PartyPEOOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 36 | PartyPEOPartyId1 | PARTY_ID | — | ✅ |
| 37 | PartyPEOPartyName | PARTY_NAME | — | ✅ |
| 38 | PartyPEOPartyNumber | PARTY_NUMBER | — | ✅ |
| 39 | PartyPEOPartyType | PARTY_TYPE | — | — |
| 40 | PartyPEOPartyUniqueName | PARTY_UNIQUE_NAME | — | — |
| 41 | PartyPEOPersonAcademicTitle | PERSON_ACADEMIC_TITLE | — | — |
| 42 | PartyPEOPersonFirstName | PERSON_FIRST_NAME | — | — |
| 43 | PartyPEOPersonLastName | PERSON_LAST_NAME | — | — |
| 44 | PartyPEOPersonLastNamePrefix | PERSON_LAST_NAME_PREFIX | — | — |
| 45 | PartyPEOPersonMiddleName | PERSON_MIDDLE_NAME | — | — |
| 46 | PartyPEOPersonNameSuffix | PERSON_NAME_SUFFIX | — | — |
| 47 | PartyPEOPersonPreNameAdjunct | PERSON_PRE_NAME_ADJUNCT | — | — |
| 48 | PartyPEOPersonPreviousLastName | PERSON_PREVIOUS_LAST_NAME | — | — |
| 49 | PartyPEOPersonSecondLastName | PERSON_SECOND_LAST_NAME | — | — |
| 50 | PartyPEOPersonTitle | PERSON_TITLE | — | — |
| 51 | PartyPEOPostalCode | POSTAL_CODE | — | — |
| 52 | PartyPEOPrefFunctionalCurrency | PREF_FUNCTIONAL_CURRENCY | — | — |
| 53 | PartyPEOPreferredContactMethod | PREFERRED_CONTACT_METHOD | — | — |
| 54 | PartyPEOPreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | ✅ |
| 55 | PartyPEOPreferredName | PREFERRED_NAME | — | — |
| 56 | PartyPEOPreferredNameId | PREFERRED_NAME_ID | — | ✅ |
| 57 | PartyPEOPrimaryEmailContactPtId | PRIMARY_EMAIL_CONTACT_PT_ID | — | ✅ |
| 58 | PartyPEOPrimaryPhoneAreaCode | PRIMARY_PHONE_AREA_CODE | — | — |
| 59 | PartyPEOPrimaryPhoneContactPtId | PRIMARY_PHONE_CONTACT_PT_ID | — | ✅ |
| 60 | PartyPEOPrimaryPhoneCountryCode | PRIMARY_PHONE_COUNTRY_CODE | — | — |
| 61 | PartyPEOPrimaryPhoneExtension | PRIMARY_PHONE_EXTENSION | — | — |
| 62 | PartyPEOPrimaryPhoneLineType | PRIMARY_PHONE_LINE_TYPE | — | — |
| 63 | PartyPEOPrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | — |
| 64 | PartyPEOPrimaryPhonePurpose | PRIMARY_PHONE_PURPOSE | — | — |
| 65 | PartyPEOPrimaryUrlContactPtId | PRIMARY_URL_CONTACT_PT_ID | — | ✅ |
| 66 | PartyPEOProvince | PROVINCE | — | — |
| 67 | PartyPEOSalutation | SALUTATION | — | — |
| 68 | PartyPEOSicCode | SIC_CODE | — | — |
| 69 | PartyPEOSicCodeType | SIC_CODE_TYPE | — | — |
| 70 | PartyPEOState | STATE | — | — |
| 71 | PartyPEOStatus | STATUS | — | — |
| 72 | PartyPEOThirdPartyFlag | THIRD_PARTY_FLAG | — | — |
| 73 | PartyPEOTradingPartnerIdentifier | TRADING_PARTNER_IDENTIFIER | — | — |
| 74 | PartyPEOUrl | URL | — | — |
| 75 | PartyPEOUserGuid | USER_GUID | — | ✅ |
| 76 | PartyPEOValidatedFlag | VALIDATED_FLAG | — | — |
| 77 | PartyPEOYearEstablished | YEAR_ESTABLISHED | — | — |

### [[inv_item_locations|INV_ITEM_LOCATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InventoryLocatorPEOAlias | ALIAS | — | — |
| 2 | InventoryLocatorPEOAttribute1 | ATTRIBUTE1 | — | — |
| 3 | InventoryLocatorPEOAttribute10 | ATTRIBUTE10 | — | — |
| 4 | InventoryLocatorPEOAttribute11 | ATTRIBUTE11 | — | — |
| 5 | InventoryLocatorPEOAttribute12 | ATTRIBUTE12 | — | — |
| 6 | InventoryLocatorPEOAttribute13 | ATTRIBUTE13 | — | — |
| 7 | InventoryLocatorPEOAttribute14 | ATTRIBUTE14 | — | — |
| 8 | InventoryLocatorPEOAttribute15 | ATTRIBUTE15 | — | — |
| 9 | InventoryLocatorPEOAttribute2 | ATTRIBUTE2 | — | — |
| 10 | InventoryLocatorPEOAttribute3 | ATTRIBUTE3 | — | — |
| 11 | InventoryLocatorPEOAttribute4 | ATTRIBUTE4 | — | — |
| 12 | InventoryLocatorPEOAttribute5 | ATTRIBUTE5 | — | — |
| 13 | InventoryLocatorPEOAttribute6 | ATTRIBUTE6 | — | — |
| 14 | InventoryLocatorPEOAttribute7 | ATTRIBUTE7 | — | — |
| 15 | InventoryLocatorPEOAttribute8 | ATTRIBUTE8 | — | — |
| 16 | InventoryLocatorPEOAttribute9 | ATTRIBUTE9 | — | — |
| 17 | InventoryLocatorPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 18 | InventoryLocatorPEOAvailabilityType | AVAILABILITY_TYPE | — | — |
| 19 | InventoryLocatorPEOAvailableCubicArea | AVAILABLE_CUBIC_AREA | — | — |
| 20 | InventoryLocatorPEOAvailableWeight | AVAILABLE_WEIGHT | — | — |
| 21 | InventoryLocatorPEOCreatedBy | CREATED_BY | — | — |
| 22 | InventoryLocatorPEOCreationDate | CREATION_DATE | — | — |
| 23 | InventoryLocatorPEOCurrentCubicArea | CURRENT_CUBIC_AREA | — | — |
| 24 | InventoryLocatorPEOCurrentWeight | CURRENT_WEIGHT | — | — |
| 25 | InventoryLocatorPEODepreciableFlag | DEPRECIABLE_FLAG | — | — |
| 26 | InventoryLocatorPEODescription | DESCRIPTION | — | — |
| 27 | InventoryLocatorPEODimensionUomCode | DIMENSION_UOM_CODE | — | — |
| 28 | InventoryLocatorPEODisableDate | DISABLE_DATE | — | — |
| 29 | InventoryLocatorPEODroppingOrder | DROPPING_ORDER | — | — |
| 30 | InventoryLocatorPEOEmptyFlag | EMPTY_FLAG | — | — |
| 31 | InventoryLocatorPEOEnabledFlag | ENABLED_FLAG | — | — |
| 32 | InventoryLocatorPEOEndDateActive | END_DATE_ACTIVE | — | — |
| 33 | InventoryLocatorPEOInventoryAtpCode | INVENTORY_ATP_CODE | — | — |
| 34 | InventoryLocatorPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 35 | InventoryLocatorPEOInventoryLocationId | INVENTORY_LOCATION_ID | — | — |
| 36 | InventoryLocatorPEOInventoryLocationType | INVENTORY_LOCATION_TYPE | — | — |
| 37 | InventoryLocatorPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 38 | InventoryLocatorPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 39 | InventoryLocatorPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 40 | InventoryLocatorPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 41 | InventoryLocatorPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 42 | InventoryLocatorPEOLocationAvailableUnits | LOCATION_AVAILABLE_UNITS | — | — |
| 43 | InventoryLocatorPEOLocationCurrentUnits | LOCATION_CURRENT_UNITS | — | — |
| 44 | InventoryLocatorPEOLocationHeight | LOCATION_HEIGHT | — | — |
| 45 | InventoryLocatorPEOLocationLength | LOCATION_LENGTH | — | — |
| 46 | InventoryLocatorPEOLocationMaximumUnits | LOCATION_MAXIMUM_UNITS | — | — |
| 47 | InventoryLocatorPEOLocationSuggestedUnits | LOCATION_SUGGESTED_UNITS | — | — |
| 48 | InventoryLocatorPEOLocationWeightUomCode | LOCATION_WEIGHT_UOM_CODE | — | — |
| 49 | InventoryLocatorPEOLocationWidth | LOCATION_WIDTH | — | — |
| 50 | InventoryLocatorPEOLocatorStatus | LOCATOR_STATUS | — | — |
| 51 | InventoryLocatorPEOMaxCubicArea | MAX_CUBIC_AREA | — | — |
| 52 | InventoryLocatorPEOMaxWeight | MAX_WEIGHT | — | — |
| 53 | InventoryLocatorPEOMixedItemsFlag | MIXED_ITEMS_FLAG | — | — |
| 54 | InventoryLocatorPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 55 | InventoryLocatorPEOOrganizationId | ORGANIZATION_ID | — | — |
| 56 | InventoryLocatorPEOPhysicalLocationCode | PHYSICAL_LOCATION_CODE | — | — |
| 57 | InventoryLocatorPEOPhysicalLocationId | PHYSICAL_LOCATION_ID | — | — |
| 58 | InventoryLocatorPEOPickUomCode | PICK_UOM_CODE | — | — |
| 59 | InventoryLocatorPEOPickingOrder | PICKING_ORDER | — | — |
| 60 | InventoryLocatorPEOProjectId | PROJECT_ID | — | — |
| 61 | InventoryLocatorPEORequestId | REQUEST_ID | — | — |
| 62 | InventoryLocatorPEOReservableType | RESERVABLE_TYPE | — | — |
| 63 | InventoryLocatorPEOSegment1 | SEGMENT1 | — | — |
| 64 | InventoryLocatorPEOSegment10 | SEGMENT10 | — | — |
| 65 | InventoryLocatorPEOSegment11 | SEGMENT11 | — | — |
| 66 | InventoryLocatorPEOSegment12 | SEGMENT12 | — | — |
| 67 | InventoryLocatorPEOSegment13 | SEGMENT13 | — | — |
| 68 | InventoryLocatorPEOSegment14 | SEGMENT14 | — | — |
| 69 | InventoryLocatorPEOSegment15 | SEGMENT15 | — | — |
| 70 | InventoryLocatorPEOSegment16 | SEGMENT16 | — | — |
| 71 | InventoryLocatorPEOSegment17 | SEGMENT17 | — | — |
| 72 | InventoryLocatorPEOSegment18 | SEGMENT18 | — | — |
| 73 | InventoryLocatorPEOSegment19 | SEGMENT19 | — | — |
| 74 | InventoryLocatorPEOSegment2 | SEGMENT2 | — | — |
| 75 | InventoryLocatorPEOSegment20 | SEGMENT20 | — | — |
| 76 | InventoryLocatorPEOSegment3 | SEGMENT3 | — | — |
| 77 | InventoryLocatorPEOSegment4 | SEGMENT4 | — | — |
| 78 | InventoryLocatorPEOSegment5 | SEGMENT5 | — | — |
| 79 | InventoryLocatorPEOSegment6 | SEGMENT6 | — | — |
| 80 | InventoryLocatorPEOSegment7 | SEGMENT7 | — | — |
| 81 | InventoryLocatorPEOSegment8 | SEGMENT8 | — | — |
| 82 | InventoryLocatorPEOSegment9 | SEGMENT9 | — | — |
| 83 | InventoryLocatorPEOStartDateActive | START_DATE_ACTIVE | — | — |
| 84 | InventoryLocatorPEOStatusId | STATUS_ID | — | — |
| 85 | InventoryLocatorPEOStructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | — |
| 86 | InventoryLocatorPEOSubinventoryCode | SUBINVENTORY_CODE | — | — |
| 87 | InventoryLocatorPEOSubinventoryId | SUBINVENTORY_ID | — | — |
| 88 | InventoryLocatorPEOSuggestedCubicArea | SUGGESTED_CUBIC_AREA | — | — |
| 89 | InventoryLocatorPEOSuggestedWeight | SUGGESTED_WEIGHT | — | — |
| 90 | InventoryLocatorPEOSummaryFlag | SUMMARY_FLAG | — | — |
| 91 | InventoryLocatorPEOTaskId | TASK_ID | — | — |
| 92 | InventoryLocatorPEOVolumeUomCode | VOLUME_UOM_CODE | — | — |
| 93 | InventoryLocatorPEOXCoordinate | X_COORDINATE | — | — |
| 94 | InventoryLocatorPEOYCoordinate | Y_COORDINATE | — | — |
| 95 | InventoryLocatorPEOZCoordinate | Z_COORDINATE | — | — |

### [[poz_suppliers|POZ_SUPPLIERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SupplierPEOAutoTaxCalcFlag | AUTO_TAX_CALC_FLAG | — | — |
| 2 | SupplierPEOAutoTaxCalcOverride | AUTO_TAX_CALC_OVERRIDE | — | — |
| 3 | SupplierPEOAwtGroupId | AWT_GROUP_ID | — | ✅ |
| 4 | SupplierPEOBankChargeBearer | BANK_CHARGE_BEARER | — | — |
| 5 | SupplierPEOBcNotApplicableFlag | BC_NOT_APPLICABLE_FLAG | — | — |
| 6 | SupplierPEOBusinessRelationship | BUSINESS_RELATIONSHIP | — | — |
| 7 | SupplierPEOChangeReqNumber | CHANGE_REQ_NUMBER | — | — |
| 8 | SupplierPEOCorporateWebsite | CORPORATE_WEBSITE | — | — |
| 9 | SupplierPEOCreatedBy1 | CREATED_BY | — | — |
| 10 | SupplierPEOCreationDate1 | CREATION_DATE | — | ✅ |
| 11 | SupplierPEOCreationSource | CREATION_SOURCE | — | — |
| 12 | SupplierPEOCustomerNum | CUSTOMER_NUM | — | — |
| 13 | SupplierPEOEmployeeId | EMPLOYEE_ID | — | ✅ |
| 14 | SupplierPEOEnabledFlag1 | ENABLED_FLAG | — | — |
| 15 | SupplierPEOEndDateActive | END_DATE_ACTIVE | — | — |
| 16 | SupplierPEOFederalReportableFlag | FEDERAL_REPORTABLE_FLAG | — | — |
| 17 | SupplierPEOGlobalAttribute101 | GLOBAL_ATTRIBUTE10 | — | — |
| 18 | SupplierPEOGlobalAttribute110 | GLOBAL_ATTRIBUTE1 | — | — |
| 19 | SupplierPEOGlobalAttribute111 | GLOBAL_ATTRIBUTE11 | — | — |
| 20 | SupplierPEOGlobalAttribute121 | GLOBAL_ATTRIBUTE12 | — | — |
| 21 | SupplierPEOGlobalAttribute131 | GLOBAL_ATTRIBUTE13 | — | — |
| 22 | SupplierPEOGlobalAttribute141 | GLOBAL_ATTRIBUTE14 | — | — |
| 23 | SupplierPEOGlobalAttribute151 | GLOBAL_ATTRIBUTE15 | — | — |
| 24 | SupplierPEOGlobalAttribute161 | GLOBAL_ATTRIBUTE16 | — | — |
| 25 | SupplierPEOGlobalAttribute171 | GLOBAL_ATTRIBUTE17 | — | — |
| 26 | SupplierPEOGlobalAttribute181 | GLOBAL_ATTRIBUTE18 | — | — |
| 27 | SupplierPEOGlobalAttribute191 | GLOBAL_ATTRIBUTE19 | — | — |
| 28 | SupplierPEOGlobalAttribute201 | GLOBAL_ATTRIBUTE20 | — | — |
| 29 | SupplierPEOGlobalAttribute21 | GLOBAL_ATTRIBUTE2 | — | — |
| 30 | SupplierPEOGlobalAttribute31 | GLOBAL_ATTRIBUTE3 | — | — |
| 31 | SupplierPEOGlobalAttribute41 | GLOBAL_ATTRIBUTE4 | — | — |
| 32 | SupplierPEOGlobalAttribute51 | GLOBAL_ATTRIBUTE5 | — | — |
| 33 | SupplierPEOGlobalAttribute61 | GLOBAL_ATTRIBUTE6 | — | — |
| 34 | SupplierPEOGlobalAttribute71 | GLOBAL_ATTRIBUTE7 | — | — |
| 35 | SupplierPEOGlobalAttribute81 | GLOBAL_ATTRIBUTE8 | — | — |
| 36 | SupplierPEOGlobalAttribute91 | GLOBAL_ATTRIBUTE9 | — | — |
| 37 | SupplierPEOGlobalAttributeCategory1 | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 38 | SupplierPEOGlobalAttributeDate1 | GLOBAL_ATTRIBUTE_DATE1 | — | — |
| 39 | SupplierPEOGlobalAttributeDate10 | GLOBAL_ATTRIBUTE_DATE10 | — | — |
| 40 | SupplierPEOGlobalAttributeDate2 | GLOBAL_ATTRIBUTE_DATE2 | — | — |
| 41 | SupplierPEOGlobalAttributeDate3 | GLOBAL_ATTRIBUTE_DATE3 | — | — |
| 42 | SupplierPEOGlobalAttributeDate4 | GLOBAL_ATTRIBUTE_DATE4 | — | — |
| 43 | SupplierPEOGlobalAttributeDate5 | GLOBAL_ATTRIBUTE_DATE5 | — | — |
| 44 | SupplierPEOGlobalAttributeDate6 | GLOBAL_ATTRIBUTE_DATE6 | — | — |
| 45 | SupplierPEOGlobalAttributeDate7 | GLOBAL_ATTRIBUTE_DATE7 | — | — |
| 46 | SupplierPEOGlobalAttributeDate8 | GLOBAL_ATTRIBUTE_DATE8 | — | — |
| 47 | SupplierPEOGlobalAttributeDate9 | GLOBAL_ATTRIBUTE_DATE9 | — | — |
| 48 | SupplierPEOGlobalAttributeNumber1 | GLOBAL_ATTRIBUTE_NUMBER1 | — | — |
| 49 | SupplierPEOGlobalAttributeNumber10 | GLOBAL_ATTRIBUTE_NUMBER10 | — | — |
| 50 | SupplierPEOGlobalAttributeNumber2 | GLOBAL_ATTRIBUTE_NUMBER2 | — | — |
| 51 | SupplierPEOGlobalAttributeNumber3 | GLOBAL_ATTRIBUTE_NUMBER3 | — | — |
| 52 | SupplierPEOGlobalAttributeNumber4 | GLOBAL_ATTRIBUTE_NUMBER4 | — | — |
| 53 | SupplierPEOGlobalAttributeNumber5 | GLOBAL_ATTRIBUTE_NUMBER5 | — | — |
| 54 | SupplierPEOGlobalAttributeNumber6 | GLOBAL_ATTRIBUTE_NUMBER6 | — | — |
| 55 | SupplierPEOGlobalAttributeNumber7 | GLOBAL_ATTRIBUTE_NUMBER7 | — | — |
| 56 | SupplierPEOGlobalAttributeNumber8 | GLOBAL_ATTRIBUTE_NUMBER8 | — | — |
| 57 | SupplierPEOGlobalAttributeNumber9 | GLOBAL_ATTRIBUTE_NUMBER9 | — | — |
| 58 | SupplierPEOGlobalAttributeTimestamp1 | GLOBAL_ATTRIBUTE_TIMESTAMP1 | — | — |
| 59 | SupplierPEOGlobalAttributeTimestamp10 | GLOBAL_ATTRIBUTE_TIMESTAMP10 | — | — |
| 60 | SupplierPEOGlobalAttributeTimestamp2 | GLOBAL_ATTRIBUTE_TIMESTAMP2 | — | — |
| 61 | SupplierPEOGlobalAttributeTimestamp3 | GLOBAL_ATTRIBUTE_TIMESTAMP3 | — | — |
| 62 | SupplierPEOGlobalAttributeTimestamp4 | GLOBAL_ATTRIBUTE_TIMESTAMP4 | — | — |
| 63 | SupplierPEOGlobalAttributeTimestamp5 | GLOBAL_ATTRIBUTE_TIMESTAMP5 | — | — |
| 64 | SupplierPEOGlobalAttributeTimestamp6 | GLOBAL_ATTRIBUTE_TIMESTAMP6 | — | — |
| 65 | SupplierPEOGlobalAttributeTimestamp7 | GLOBAL_ATTRIBUTE_TIMESTAMP7 | — | — |
| 66 | SupplierPEOGlobalAttributeTimestamp8 | GLOBAL_ATTRIBUTE_TIMESTAMP8 | — | — |
| 67 | SupplierPEOGlobalAttributeTimestamp9 | GLOBAL_ATTRIBUTE_TIMESTAMP9 | — | — |
| 68 | SupplierPEOIncomeTaxIdFlag | INCOME_TAX_ID_FLAG | — | — |
| 69 | SupplierPEOJobDefinitionName1 | JOB_DEFINITION_NAME | — | — |
| 70 | SupplierPEOJobDefinitionPackage1 | JOB_DEFINITION_PACKAGE | — | — |
| 71 | SupplierPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 72 | SupplierPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 73 | SupplierPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 74 | SupplierPEOMinOrderAmount | MIN_ORDER_AMOUNT | — | ✅ |
| 75 | SupplierPEOMinorityGroupLookupCode | MINORITY_GROUP_LOOKUP_CODE | — | — |
| 76 | SupplierPEONameControl | NAME_CONTROL | — | — |
| 77 | SupplierPEONiNumber | NI_NUMBER | — | — |
| 78 | SupplierPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 79 | SupplierPEOOffsetTaxFlag | OFFSET_TAX_FLAG | — | — |
| 80 | SupplierPEOOffsetVatCode | OFFSET_VAT_CODE | — | — |
| 81 | SupplierPEOOneTimeFlag | ONE_TIME_FLAG | — | — |
| 82 | SupplierPEOOrganizationTypeLookupCode | ORGANIZATION_TYPE_LOOKUP_CODE | — | — |
| 83 | SupplierPEOParentPartyId | PARENT_PARTY_ID | — | ✅ |
| 84 | SupplierPEOParentVendorId | PARENT_VENDOR_ID | — | ✅ |
| 85 | SupplierPEOPartyId | PARTY_ID | — | ✅ |
| 86 | SupplierPEOProgramApplicationId | PROGRAM_APPLICATION_ID | — | ✅ |
| 87 | SupplierPEOProgramId | PROGRAM_ID | — | ✅ |
| 88 | SupplierPEOProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 89 | SupplierPEORequestId1 | REQUEST_ID | — | ✅ |
| 90 | SupplierPEOSegment11 | SEGMENT1 | — | — |
| 91 | SupplierPEOSetOfBooksId | SET_OF_BOOKS_ID | — | ✅ |
| 92 | SupplierPEOSmallBusinessFlag | SMALL_BUSINESS_FLAG | — | — |
| 93 | SupplierPEOSpendAuthJustification | SPEND_AUTH_JUSTIFICATION | — | — |
| 94 | SupplierPEOSpendAuthReviewStatus | SPEND_AUTH_REVIEW_STATUS | — | — |
| 95 | SupplierPEOStandardIndustryClass | STANDARD_INDUSTRY_CLASS | — | — |
| 96 | SupplierPEOStartDateActive | START_DATE_ACTIVE | — | — |
| 97 | SupplierPEOStateReportableFlag | STATE_REPORTABLE_FLAG | — | — |
| 98 | SupplierPEOSummaryFlag1 | SUMMARY_FLAG | — | — |
| 99 | SupplierPEOSupplierLockedFlag | SUPPLIER_LOCKED_FLAG | — | — |
| 100 | SupplierPEOTaxReportingName | TAX_REPORTING_NAME | — | — |
| 101 | SupplierPEOTaxVerificationDate | TAX_VERIFICATION_DATE | — | ✅ |
| 102 | SupplierPEOTaxpayerCountry | TAXPAYER_COUNTRY | — | — |
| 103 | SupplierPEOType1099 | TYPE_1099 | — | — |
| 104 | SupplierPEOVatCode | VAT_CODE | — | — |
| 105 | SupplierPEOVatRegistrationNum | VAT_REGISTRATION_NUM | — | — |
| 106 | SupplierPEOVendorId1 | VENDOR_ID | — | ✅ |
| 107 | SupplierPEOVendorTypeLookupCode | VENDOR_TYPE_LOOKUP_CODE | — | — |
| 108 | SupplierPEOWithholdingStartDate | WITHHOLDING_START_DATE | — | ✅ |
| 109 | SupplierPEOWithholdingStatusLookupCode | WITHHOLDING_STATUS_LOOKUP_CODE | — | — |
| 110 | SupplierPEOWomenOwnedFlag | WOMEN_OWNED_FLAG | — | — |

### [[poz_suppliers_v|POZ_SUPPLIERS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WarrantySupplierViewPEOVendorId | VENDOR_ID | — | — |
| 2 | WarrantySupplierViewPEOVendorName | VENDOR_NAME | — | — |

### [[po_headers_all|PO_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PurchasingDocumentHeaderPEOAutoSourcingFlag | AUTO_SOURCING_FLAG | — | — |
| 2 | PurchasingDocumentHeaderPEOBillToLocationId | BILL_TO_LOCATION_ID | — | ✅ |
| 3 | PurchasingDocumentHeaderPEOBillingCycleClosingDate | BILLING_CYCLE_CLOSING_DATE | — | ✅ |
| 4 | PurchasingDocumentHeaderPEOBilltoBuId | BILLTO_BU_ID | — | ✅ |
| 5 | PurchasingDocumentHeaderPEOBlanketTotalAmount | BLANKET_TOTAL_AMOUNT | — | ✅ |
| 6 | PurchasingDocumentHeaderPEOBudgetControlEnabledFlag | BUDGET_CONTROL_ENABLED_FLAG | — | — |
| 7 | PurchasingDocumentHeaderPEOBuyerManagedTransportFlag | BUYER_MANAGED_TRANSPORT_FLAG | — | — |
| 8 | PurchasingDocumentHeaderPEOCancelFlag | CANCEL_FLAG | — | — |
| 9 | PurchasingDocumentHeaderPEOCarrierId | CARRIER_ID | — | ✅ |
| 10 | PurchasingDocumentHeaderPEOCatAdminAuthEnabledFlag | CAT_ADMIN_AUTH_ENABLED_FLAG | — | — |
| 11 | PurchasingDocumentHeaderPEOCbcAccountingDate | CBC_ACCOUNTING_DATE | — | ✅ |
| 12 | PurchasingDocumentHeaderPEOChangeRequestedBy | CHANGE_REQUESTED_BY | — | — |
| 13 | PurchasingDocumentHeaderPEOChangeSummary | CHANGE_SUMMARY | — | — |
| 14 | PurchasingDocumentHeaderPEOClosedDate | CLOSED_DATE | — | ✅ |
| 15 | PurchasingDocumentHeaderPEOClosedDateTime | CLOSED_DATE | — | — |
| 16 | PurchasingDocumentHeaderPEOComments | COMMENTS | — | — |
| 17 | PurchasingDocumentHeaderPEOConfirmingOrderFlag | CONFIRMING_ORDER_FLAG | — | — |
| 18 | PurchasingDocumentHeaderPEOConsignedConsumptionFlag | CONSIGNED_CONSUMPTION_FLAG | — | — |
| 19 | PurchasingDocumentHeaderPEOConsumeReqDemandFlag | CONSUME_REQ_DEMAND_FLAG | — | — |
| 20 | PurchasingDocumentHeaderPEOConsumptionAdviceFrequency | CONSUMPTION_ADVICE_FREQUENCY | — | — |
| 21 | PurchasingDocumentHeaderPEOConsumptionAdviceSummary | CONSUMPTION_ADVICE_SUMMARY | — | — |
| 22 | PurchasingDocumentHeaderPEOContermsArticlesUpdDate | CONTERMS_ARTICLES_UPD_DATE | — | ✅ |
| 23 | PurchasingDocumentHeaderPEOContermsDelivUpdDate | CONTERMS_DELIV_UPD_DATE | — | ✅ |
| 24 | PurchasingDocumentHeaderPEOContermsExistFlag | CONTERMS_EXIST_FLAG | — | — |
| 25 | PurchasingDocumentHeaderPEOCpaReference | CPA_REFERENCE | — | — |
| 26 | PurchasingDocumentHeaderPEOCreatedBy | CREATED_BY | — | — |
| 27 | PurchasingDocumentHeaderPEOCreatedLanguage | CREATED_LANGUAGE | — | — |
| 28 | PurchasingDocumentHeaderPEOCreationDate | CREATION_DATE | — | ✅ |
| 29 | PurchasingDocumentHeaderPEOCurrencyCode | CURRENCY_CODE | — | — |
| 30 | PurchasingDocumentHeaderPEOCurrentVersionId | CURRENT_VERSION_ID | — | ✅ |
| 31 | PurchasingDocumentHeaderPEODefaultConsignmentLineFlag | DEFAULT_CONSIGNMENT_LINE_FLAG | — | — |
| 32 | PurchasingDocumentHeaderPEODefaultPoTradeOrgId | DEFAULT_PO_TRADE_ORG_ID | — | ✅ |
| 33 | PurchasingDocumentHeaderPEODefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | — |
| 34 | PurchasingDocumentHeaderPEODisableAutosourcingFlag | DISABLE_AUTOSOURCING_FLAG | — | — |
| 35 | PurchasingDocumentHeaderPEODocumentCreationMethod | DOCUMENT_CREATION_METHOD | — | — |
| 36 | PurchasingDocumentHeaderPEODocumentStatus | DOCUMENT_STATUS | — | — |
| 37 | PurchasingDocumentHeaderPEOEdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 38 | PurchasingDocumentHeaderPEOEdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 39 | PurchasingDocumentHeaderPEOEmailAddress | EMAIL_ADDRESS | — | — |
| 40 | PurchasingDocumentHeaderPEOEnabledFlag | ENABLED_FLAG | — | — |
| 41 | PurchasingDocumentHeaderPEOEncumbranceRequiredFlag | ENCUMBRANCE_REQUIRED_FLAG | — | — |
| 42 | PurchasingDocumentHeaderPEOEndDate | END_DATE | — | ✅ |
| 43 | PurchasingDocumentHeaderPEOFax | FAX | — | — |
| 44 | PurchasingDocumentHeaderPEOFirmDate | FIRM_DATE | — | ✅ |
| 45 | PurchasingDocumentHeaderPEOFirmStatusLookupCode | FIRM_STATUS_LOOKUP_CODE | — | — |
| 46 | PurchasingDocumentHeaderPEOFirstPtyRegId | FIRST_PTY_REG_ID | — | ✅ |
| 47 | PurchasingDocumentHeaderPEOFobLookupCode | FOB_LOOKUP_CODE | — | — |
| 48 | PurchasingDocumentHeaderPEOFreightTermsLookupCode | FREIGHT_TERMS_LOOKUP_CODE | — | — |
| 49 | PurchasingDocumentHeaderPEOFromHeaderId | FROM_HEADER_ID | — | ✅ |
| 50 | PurchasingDocumentHeaderPEOFromTypeLookupCode | FROM_TYPE_LOOKUP_CODE | — | — |
| 51 | PurchasingDocumentHeaderPEOFrozenFlag | FROZEN_FLAG | — | — |
| 52 | PurchasingDocumentHeaderPEOFundsStatus | FUNDS_STATUS | — | — |
| 53 | PurchasingDocumentHeaderPEOGenerateOrdersAutomatic | GENERATE_ORDERS_AUTOMATIC | — | — |
| 54 | PurchasingDocumentHeaderPEOGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 55 | PurchasingDocumentHeaderPEOGlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | — |
| 56 | PurchasingDocumentHeaderPEOGlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | — |
| 57 | PurchasingDocumentHeaderPEOGlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | — |
| 58 | PurchasingDocumentHeaderPEOGlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | — |
| 59 | PurchasingDocumentHeaderPEOGlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | — |
| 60 | PurchasingDocumentHeaderPEOGlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | — |
| 61 | PurchasingDocumentHeaderPEOGlobalAttribute16 | GLOBAL_ATTRIBUTE16 | — | — |
| 62 | PurchasingDocumentHeaderPEOGlobalAttribute17 | GLOBAL_ATTRIBUTE17 | — | — |
| 63 | PurchasingDocumentHeaderPEOGlobalAttribute18 | GLOBAL_ATTRIBUTE18 | — | — |
| 64 | PurchasingDocumentHeaderPEOGlobalAttribute19 | GLOBAL_ATTRIBUTE19 | — | — |
| 65 | PurchasingDocumentHeaderPEOGlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | — |
| 66 | PurchasingDocumentHeaderPEOGlobalAttribute20 | GLOBAL_ATTRIBUTE20 | — | — |
| 67 | PurchasingDocumentHeaderPEOGlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | — |
| 68 | PurchasingDocumentHeaderPEOGlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | — |
| 69 | PurchasingDocumentHeaderPEOGlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | — |
| 70 | PurchasingDocumentHeaderPEOGlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | — |
| 71 | PurchasingDocumentHeaderPEOGlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | — |
| 72 | PurchasingDocumentHeaderPEOGlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | — |
| 73 | PurchasingDocumentHeaderPEOGlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | — |
| 74 | PurchasingDocumentHeaderPEOGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 75 | PurchasingDocumentHeaderPEOGovernmentContext | GOVERNMENT_CONTEXT | — | — |
| 76 | PurchasingDocumentHeaderPEOGroupRequisitionLines | GROUP_REQUISITION_LINES | — | — |
| 77 | PurchasingDocumentHeaderPEOGroupRequisitions | GROUP_REQUISITIONS | — | — |
| 78 | PurchasingDocumentHeaderPEOInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | — |
| 79 | PurchasingDocumentHeaderPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 80 | PurchasingDocumentHeaderPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 81 | PurchasingDocumentHeaderPEOLastBilledDate | LAST_BILLED_DATE | — | ✅ |
| 82 | PurchasingDocumentHeaderPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 83 | PurchasingDocumentHeaderPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 84 | PurchasingDocumentHeaderPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 85 | PurchasingDocumentHeaderPEOLastUpdatedProgram | LAST_UPDATED_PROGRAM | — | — |
| 86 | PurchasingDocumentHeaderPEOMergeRequestId | MERGE_REQUEST_ID | — | ✅ |
| 87 | PurchasingDocumentHeaderPEOMinReleaseAmount | MIN_RELEASE_AMOUNT | — | — |
| 88 | PurchasingDocumentHeaderPEOModeOfTransport | MODE_OF_TRANSPORT | — | — |
| 89 | PurchasingDocumentHeaderPEONoteToAuthorizer | NOTE_TO_AUTHORIZER | — | — |
| 90 | PurchasingDocumentHeaderPEONoteToReceiver | NOTE_TO_RECEIVER | — | — |
| 91 | PurchasingDocumentHeaderPEONoteToVendor | NOTE_TO_VENDOR | — | — |
| 92 | PurchasingDocumentHeaderPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 93 | PurchasingDocumentHeaderPEOOrchestrationOrderFlag | ORCHESTRATION_ORDER_FLAG | — | — |
| 94 | PurchasingDocumentHeaderPEOPayOnCode | PAY_ON_CODE | — | — |
| 95 | PurchasingDocumentHeaderPEOPayOnUseFlag | PAY_ON_USE_FLAG | — | — |
| 96 | PurchasingDocumentHeaderPEOPcardId | PCARD_ID | — | ✅ |
| 97 | PurchasingDocumentHeaderPEOPendingSignatureFlag | PENDING_SIGNATURE_FLAG | — | — |
| 98 | PurchasingDocumentHeaderPEOPoHeaderId | PO_HEADER_ID | — | ✅ |
| 99 | PurchasingDocumentHeaderPEOPrcBuId | PRC_BU_ID | — | ✅ |
| 100 | PurchasingDocumentHeaderPEOPriceUpdateTolerance | PRICE_UPDATE_TOLERANCE | — | — |
| 101 | PurchasingDocumentHeaderPEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 102 | PurchasingDocumentHeaderPEOProgramName | PROGRAM_NAME | — | — |
| 103 | PurchasingDocumentHeaderPEOPunchoutSourcingOnlyFlag | PUNCHOUT_SOURCING_ONLY_FLAG | — | — |
| 104 | PurchasingDocumentHeaderPEORate | RATE | — | — |
| 105 | PurchasingDocumentHeaderPEORateDate | RATE_DATE | — | ✅ |
| 106 | PurchasingDocumentHeaderPEORateType | RATE_TYPE | — | — |
| 107 | PurchasingDocumentHeaderPEOReferenceNum | REFERENCE_NUM | — | — |
| 108 | PurchasingDocumentHeaderPEOReleaseMethod | RELEASE_METHOD | — | — |
| 109 | PurchasingDocumentHeaderPEOReqBuId | REQ_BU_ID | — | ✅ |
| 110 | PurchasingDocumentHeaderPEORequestId | REQUEST_ID | — | ✅ |
| 111 | PurchasingDocumentHeaderPEORetroPriceApplyUpdatesFlag | RETRO_PRICE_APPLY_UPDATES_FLAG | — | — |
| 112 | PurchasingDocumentHeaderPEORetroPriceCommUpdatesFlag | RETRO_PRICE_COMM_UPDATES_FLAG | — | — |
| 113 | PurchasingDocumentHeaderPEOReviewAutogeneratedReleases | REVIEW_AUTOGENERATED_RELEASES | — | — |
| 114 | PurchasingDocumentHeaderPEORevisedDate | REVISED_DATE | — | ✅ |
| 115 | PurchasingDocumentHeaderPEORevisionNum | REVISION_NUM | — | — |
| 116 | PurchasingDocumentHeaderPEOSegment1 | SEGMENT1 | — | ✅ |
| 117 | PurchasingDocumentHeaderPEOSegment2 | SEGMENT2 | — | — |
| 118 | PurchasingDocumentHeaderPEOSegment3 | SEGMENT3 | — | — |
| 119 | PurchasingDocumentHeaderPEOSegment4 | SEGMENT4 | — | — |
| 120 | PurchasingDocumentHeaderPEOSegment5 | SEGMENT5 | — | — |
| 121 | PurchasingDocumentHeaderPEOServiceLevel | SERVICE_LEVEL | — | — |
| 122 | PurchasingDocumentHeaderPEOShipToLocationId | SHIP_TO_LOCATION_ID | — | ✅ |
| 123 | PurchasingDocumentHeaderPEOShippingControl | SHIPPING_CONTROL | — | — |
| 124 | PurchasingDocumentHeaderPEOSoldtoLeId | SOLDTO_LE_ID | — | ✅ |
| 125 | PurchasingDocumentHeaderPEOStartDate | START_DATE | — | ✅ |
| 126 | PurchasingDocumentHeaderPEOStyleId | STYLE_ID | — | ✅ |
| 127 | PurchasingDocumentHeaderPEOSubmitApprovalAutomatic | SUBMIT_APPROVAL_AUTOMATIC | — | — |
| 128 | PurchasingDocumentHeaderPEOSubmitDate | SUBMIT_DATE | — | ✅ |
| 129 | PurchasingDocumentHeaderPEOSummaryFlag | SUMMARY_FLAG | — | — |
| 130 | PurchasingDocumentHeaderPEOSupplierNotifMethod | SUPPLIER_NOTIF_METHOD | — | — |
| 131 | PurchasingDocumentHeaderPEOTaxAttributeUpdateCode | TAX_ATTRIBUTE_UPDATE_CODE | — | — |
| 132 | PurchasingDocumentHeaderPEOTaxDocumentSubtype | TAX_DOCUMENT_SUBTYPE | — | — |
| 133 | PurchasingDocumentHeaderPEOTermsId | TERMS_ID | — | ✅ |
| 134 | PurchasingDocumentHeaderPEOThirdPtyRegId | THIRD_PTY_REG_ID | — | ✅ |
| 135 | PurchasingDocumentHeaderPEOTypeLookupCode | TYPE_LOOKUP_CODE | — | — |
| 136 | PurchasingDocumentHeaderPEOUpdateSourcingRulesFlag | UPDATE_SOURCING_RULES_FLAG | — | — |
| 137 | PurchasingDocumentHeaderPEOUseNeedByDate | USE_NEED_BY_DATE | — | ✅ |
| 138 | PurchasingDocumentHeaderPEOUseSalesOrderNumberFlag | USE_SALES_ORDER_NUMBER_FLAG | — | — |
| 139 | PurchasingDocumentHeaderPEOUseShipTo | USE_SHIP_TO | — | — |
| 140 | PurchasingDocumentHeaderPEOVendorContactId | VENDOR_CONTACT_ID | — | ✅ |
| 141 | PurchasingDocumentHeaderPEOVendorId | VENDOR_ID | — | ✅ |
| 142 | PurchasingDocumentHeaderPEOVendorOrderNum | VENDOR_ORDER_NUM | — | ✅ |
| 143 | PurchasingDocumentHeaderPEOVendorSiteId | VENDOR_SITE_ID | — | ✅ |
| 144 | PurchasingDocumentHeaderPEOXmlChangeSendDate | XML_CHANGE_SEND_DATE | — | ✅ |
| 145 | PurchasingDocumentHeaderPEOXmlFlag | XML_FLAG | — | — |
| 146 | PurchasingDocumentHeaderPEOXmlSendDate | XML_SEND_DATE | — | ✅ |

### [[wie_work_orders_b|WIE_WORK_ORDERS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkOrderAnalyticsPEOActualCompletionDate | ACTUAL_COMPLETION_DATE | — | ✅ |
| 2 | WorkOrderAnalyticsPEOActualStartDate | ACTUAL_START_DATE | — | ✅ |
| 3 | WorkOrderAnalyticsPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 4 | WorkOrderAnalyticsPEOBackToBackFlag | BACK_TO_BACK_FLAG | — | ✅ |
| 5 | WorkOrderAnalyticsPEOCanceledDate | CANCELED_DATE | — | ✅ |
| 6 | WorkOrderAnalyticsPEOCanceledReason | CANCELED_REASON | — | ✅ |
| 7 | WorkOrderAnalyticsPEOClosedDate | CLOSED_DATE | — | ✅ |
| 8 | WorkOrderAnalyticsPEOCmPoHeaderId | CM_PO_HEADER_ID | — | ✅ |
| 9 | WorkOrderAnalyticsPEOCmPoLineId | CM_PO_LINE_ID | — | ✅ |
| 10 | WorkOrderAnalyticsPEOCmPoLineLocId | CM_PO_LINE_LOC_ID | — | ✅ |
| 11 | WorkOrderAnalyticsPEOComplLocatorId | COMPL_LOCATOR_ID | — | ✅ |
| 12 | WorkOrderAnalyticsPEOComplSubinventoryCode | COMPL_SUBINVENTORY_CODE | — | ✅ |
| 13 | WorkOrderAnalyticsPEOCompletedQuantity | COMPLETED_QUANTITY | — | ✅ |
| 14 | WorkOrderAnalyticsPEOContractMfgFlag | CONTRACT_MFG_FLAG | — | ✅ |
| 15 | WorkOrderAnalyticsPEOCreatedBy | CREATED_BY | — | ✅ |
| 16 | WorkOrderAnalyticsPEOCreationDate | CREATION_DATE | — | ✅ |
| 17 | WorkOrderAnalyticsPEOFirmPlannedFlag | FIRM_PLANNED_FLAG | — | ✅ |
| 18 | WorkOrderAnalyticsPEOInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | — |
| 19 | WorkOrderAnalyticsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 20 | WorkOrderAnalyticsPEOItemRevision | ITEM_REVISION | — | — |
| 21 | WorkOrderAnalyticsPEOItemStructureName | ITEM_STRUCTURE_NAME | — | — |
| 22 | WorkOrderAnalyticsPEOItemVersion | ITEM_VERSION | — | — |
| 23 | WorkOrderAnalyticsPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 24 | WorkOrderAnalyticsPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 25 | WorkOrderAnalyticsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 26 | WorkOrderAnalyticsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 27 | WorkOrderAnalyticsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 28 | WorkOrderAnalyticsPEONeedByDate | NEED_BY_DATE | — | ✅ |
| 29 | WorkOrderAnalyticsPEONettableSupplyQtyOverride | NETTABLE_SUPPLY_QTY_OVERRIDE | — | — |
| 30 | WorkOrderAnalyticsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 31 | WorkOrderAnalyticsPEOOrchestrationCode | ORCHESTRATION_CODE | — | — |
| 32 | WorkOrderAnalyticsPEOOrderLessFlag | ORDER_LESS_FLAG | — | ✅ |
| 33 | WorkOrderAnalyticsPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 34 | WorkOrderAnalyticsPEOOvercomplToleranceType | OVERCOMPL_TOLERANCE_TYPE | — | — |
| 35 | WorkOrderAnalyticsPEOOvercomplToleranceValue | OVERCOMPL_TOLERANCE_VALUE | — | ✅ |
| 36 | WorkOrderAnalyticsPEOPlannedCompletionDate | PLANNED_COMPLETION_DATE | — | ✅ |
| 37 | WorkOrderAnalyticsPEOPlannedStartDate | PLANNED_START_DATE | — | ✅ |
| 38 | WorkOrderAnalyticsPEOPlannedStartQuantity | PLANNED_START_QUANTITY | — | ✅ |
| 39 | WorkOrderAnalyticsPEOPreassignLotFlag | PREASSIGN_LOT_FLAG | — | ✅ |
| 40 | WorkOrderAnalyticsPEOPrimaryProductQuantity | PRIMARY_PRODUCT_QUANTITY | — | — |
| 41 | WorkOrderAnalyticsPEOPrimaryProductUomCode | PRIMARY_PRODUCT_UOM_CODE | — | ✅ |
| 42 | WorkOrderAnalyticsPEORejectedQuantity | REJECTED_QUANTITY | — | ✅ |
| 43 | WorkOrderAnalyticsPEOReleasedDate | RELEASED_DATE | — | ✅ |
| 44 | WorkOrderAnalyticsPEORequestId | REQUEST_ID | — | ✅ |
| 45 | WorkOrderAnalyticsPEOResequenceFlag | RESEQUENCE_FLAG | — | ✅ |
| 46 | WorkOrderAnalyticsPEOSchedulingMethod | SCHEDULING_METHOD | — | — |
| 47 | WorkOrderAnalyticsPEOScoSupplyOrderId | SCO_SUPPLY_ORDER_ID | — | ✅ |
| 48 | WorkOrderAnalyticsPEOScrappedQuantity | SCRAPPED_QUANTITY | — | ✅ |
| 49 | WorkOrderAnalyticsPEOSerialTrackingFlag | SERIAL_TRACKING_FLAG | — | ✅ |
| 50 | WorkOrderAnalyticsPEOSourceHeaderRef | SOURCE_HEADER_REF | — | ✅ |
| 51 | WorkOrderAnalyticsPEOSourceHeaderRefId | SOURCE_HEADER_REF_ID | — | ✅ |
| 52 | WorkOrderAnalyticsPEOSourceLineRef | SOURCE_LINE_REF | — | ✅ |
| 53 | WorkOrderAnalyticsPEOSourceLineRefId | SOURCE_LINE_REF_ID | — | ✅ |
| 54 | WorkOrderAnalyticsPEOSourceSystemId | SOURCE_SYSTEM_ID | — | ✅ |
| 55 | WorkOrderAnalyticsPEOSourceSystemType | SOURCE_SYSTEM_TYPE | — | ✅ |
| 56 | WorkOrderAnalyticsPEOStatusChangeReason | STATUS_CHANGE_REASON | — | — |
| 57 | WorkOrderAnalyticsPEOSupplyType | SUPPLY_TYPE | — | — |
| 58 | WorkOrderAnalyticsPEOUnderCompletedFlag | UNDER_COMPLETED_FLAG | — | — |
| 59 | WorkOrderAnalyticsPEOUndercomplToleranceType | UNDERCOMPL_TOLERANCE_TYPE | — | — |
| 60 | WorkOrderAnalyticsPEOUndercomplToleranceValue | UNDERCOMPL_TOLERANCE_VALUE | — | — |
| 61 | WorkOrderAnalyticsPEOUomCode | UOM_CODE | — | ✅ |
| 62 | WorkOrderAnalyticsPEOWorkDefinitionAsOfDate | WORK_DEFINITION_AS_OF_DATE | — | — |
| 63 | WorkOrderAnalyticsPEOWorkDefinitionId | WORK_DEFINITION_ID | — | ✅ |
| 64 | WorkOrderAnalyticsPEOWorkDefinitionVersionId | WORK_DEFINITION_VERSION_ID | — | ✅ |
| 65 | WorkOrderAnalyticsPEOWorkMethodId | WORK_METHOD_ID | — | ✅ |
| 66 | WorkOrderAnalyticsPEOWorkOrderNumber | WORK_ORDER_NUMBER | — | ✅ |
| 67 | WorkOrderAnalyticsPEOWorkOrderPriority | WORK_ORDER_PRIORITY | — | ✅ |
| 68 | WorkOrderAnalyticsPEOWorkOrderStatusId | WORK_ORDER_STATUS_ID | — | ✅ |
| 69 | WorkOrderAnalyticsPEOWorkOrderSubType | WORK_ORDER_SUB_TYPE | — | ✅ |
| 70 | WorkOrderAnalyticsPEOWorkOrderType | WORK_ORDER_TYPE | — | ✅ |
| 71 | WorkOrderId | WORK_ORDER_ID | 🔑 | ✅ |

### [[wie_work_orders_tl|WIE_WORK_ORDERS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkOrderTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | WorkOrderTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | WorkOrderTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 4 | WorkOrderTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | WorkOrderTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | WorkOrderTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | WorkOrderTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | WorkOrderTranslationPEOSourceLang | SOURCE_LANG | — | — |
| 9 | WorkOrderTranslationPEOWorkOrderDescription | WORK_ORDER_DESCRIPTION | — | ✅ |
| 10 | WorkOrderTranslationPEOWorkOrderId | WORK_ORDER_ID | — | ✅ |

### [[wie_wo_assets|WIE_WO_ASSETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkOrderAssetPEOMatchToTxnCodeFlag | MATCH_TO_TXN_CODE_FLAG | — | — |
| 2 | WorkOrderAssetPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 3 | WorkOrderAssetPEOWarrantyRepairFlag | WARRANTY_REPAIR_FLAG | — | — |
| 4 | WorkOrderAssetPEOWoAssetId | WO_ASSET_ID | — | — |

### [[wie_wo_product_lots|WIE_WO_PRODUCT_LOTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkOrderProductLotPEOCreatedBy | CREATED_BY | — | — |
| 2 | WorkOrderProductLotPEOCreationDate | CREATION_DATE | — | — |
| 3 | WorkOrderProductLotPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 4 | WorkOrderProductLotPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 5 | WorkOrderProductLotPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 6 | WorkOrderProductLotPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | WorkOrderProductLotPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | WorkOrderProductLotPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | WorkOrderProductLotPEOLotNumber | LOT_NUMBER | — | — |
| 10 | WorkOrderProductLotPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | WorkOrderProductLotPEOOrganizationId | ORGANIZATION_ID | — | — |
| 12 | WorkOrderProductLotPEORequestId | REQUEST_ID | — | — |
| 13 | WorkOrderProductLotPEOWoOperationOutputId | WO_OPERATION_OUTPUT_ID | — | — |
| 14 | WorkOrderProductLotPEOWoProductLotId | WO_PRODUCT_LOT_ID | — | — |
| 15 | WorkOrderProductLotPEOWorkOrderId | WORK_ORDER_ID | — | — |

### [[wis_work_methods_vl|WIS_WORK_METHODS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkMethodPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | WorkMethodPEOWorkMethodCode | WORK_METHOD_CODE | — | — |
| 3 | WorkMethodPEOWorkMethodDescription | WORK_METHOD_DESCRIPTION | — | — |
| 4 | WorkMethodPEOWorkMethodId | WORK_METHOD_ID | — | — |
| 5 | WorkMethodPEOWorkMethodName | WORK_METHOD_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
