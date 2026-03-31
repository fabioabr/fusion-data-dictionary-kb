---
id: DOC-OTHER-PVO-PSCPropertyValuesPVO
doc_type: system-doc
title: "PSCPropertyValuesPVO — PVO Cross-Module"
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
  - PSCPropertyValuesPVO
  - pscpropertyvaluespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PSCPropertyValuesPVO

## 📌 Visão Geral

View Object para extração BICC de dados de PSCProperty Values. Acessa as tabelas: PSC_COM_PARCEL_ADDRESS, PSC_COM_PARCEL_B, PSC_COM_PARCEL_VALUE_F.

**Caminho:** `FscmTopModelAM.PscPermitsReportingAM.PSCPropertyValuesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 131 | 3 | 1 | 116 | 89% |

---

## 🔗 Tabelas Relacionadas

- [[psc_com_parcel_address|PSC_COM_PARCEL_ADDRESS]] — 51 atributos (42 BICC)
- [[psc_com_parcel_b|PSC_COM_PARCEL_B]] — 57 atributos (1 PKs, 51 BICC)
- [[psc_com_parcel_value_f|PSC_COM_PARCEL_VALUE_F]] — 23 atributos (23 BICC)

---

## ⚙️ Atributos

### [[psc_com_parcel_address|PSC_COM_PARCEL_ADDRESS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PropertyParcelAddressPEOAddress1 | ADDRESS1 | — | ✅ |
| 2 | PropertyParcelAddressPEOAddress2 | ADDRESS2 | — | ✅ |
| 3 | PropertyParcelAddressPEOAddress3 | ADDRESS3 | — | ✅ |
| 4 | PropertyParcelAddressPEOAddress4 | ADDRESS4 | — | ✅ |
| 5 | PropertyParcelAddressPEOAddressCode | ADDRESS_CODE | — | ✅ |
| 6 | PropertyParcelAddressPEOAddressField1 | ADDRESS_FIELD1 | — | ✅ |
| 7 | PropertyParcelAddressPEOAddressField2 | ADDRESS_FIELD2 | — | ✅ |
| 8 | PropertyParcelAddressPEOAddressField3 | ADDRESS_FIELD3 | — | ✅ |
| 9 | PropertyParcelAddressPEOAddressId | ADDRESS_ID | — | ✅ |
| 10 | PropertyParcelAddressPEOAddressType | ADDRESS_TYPE | — | ✅ |
| 11 | PropertyParcelAddressPEOBuildingType | BUILDING_TYPE | — | ✅ |
| 12 | PropertyParcelAddressPEOCellPhoneCountry | CELL_PHONE_COUNTRY | — | ✅ |
| 13 | PropertyParcelAddressPEOCellPhoneNum | CELL_PHONE_NUM | — | ✅ |
| 14 | PropertyParcelAddressPEOCity | CITY | — | ✅ |
| 15 | PropertyParcelAddressPEOCoordinateX | COORDINATE_X | — | — |
| 16 | PropertyParcelAddressPEOCoordinateY | COORDINATE_Y | — | — |
| 17 | PropertyParcelAddressPEOCountry | COUNTRY | — | ✅ |
| 18 | PropertyParcelAddressPEOCounty | COUNTY | — | ✅ |
| 19 | PropertyParcelAddressPEOCreatedBy | CREATED_BY | — | — |
| 20 | PropertyParcelAddressPEOCreationDate | CREATION_DATE | — | — |
| 21 | PropertyParcelAddressPEOEmailId | EMAIL_ID | — | ✅ |
| 22 | PropertyParcelAddressPEOEnabledFlag | ENABLED_FLAG | — | ✅ |
| 23 | PropertyParcelAddressPEOFaxCountry | FAX_COUNTRY | — | ✅ |
| 24 | PropertyParcelAddressPEOFaxNum | FAX_NUM | — | ✅ |
| 25 | PropertyParcelAddressPEOFloor | FLOOR | — | ✅ |
| 26 | PropertyParcelAddressPEOHomePhoneCountry | HOME_PHONE_COUNTRY | — | ✅ |
| 27 | PropertyParcelAddressPEOHomePhoneNum | HOME_PHONE_NUM | — | ✅ |
| 28 | PropertyParcelAddressPEOInputSource | INPUT_SOURCE | — | — |
| 29 | PropertyParcelAddressPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 30 | PropertyParcelAddressPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 31 | PropertyParcelAddressPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 32 | PropertyParcelAddressPEOLatitude | LATITUDE | — | ✅ |
| 33 | PropertyParcelAddressPEOLongitude | LONGITUDE | — | ✅ |
| 34 | PropertyParcelAddressPEOMunicipalityId | MUNICIPALITY_ID | — | ✅ |
| 35 | PropertyParcelAddressPEOName1 | NAME1 | — | ✅ |
| 36 | PropertyParcelAddressPEOName2 | NAME2 | — | ✅ |
| 37 | PropertyParcelAddressPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 38 | PropertyParcelAddressPEOParcelId | PARCEL_ID | — | ✅ |
| 39 | PropertyParcelAddressPEOPostalCode | POSTAL_CODE | — | ✅ |
| 40 | PropertyParcelAddressPEOPostalPlus4Code | POSTAL_PLUS4_CODE | — | ✅ |
| 41 | PropertyParcelAddressPEOPrimaryFlag | PRIMARY_FLAG | — | ✅ |
| 42 | PropertyParcelAddressPEOProvince | PROVINCE | — | ✅ |
| 43 | PropertyParcelAddressPEOSrid | SRID | — | — |
| 44 | PropertyParcelAddressPEOState | STATE | — | ✅ |
| 45 | PropertyParcelAddressPEOStreeName | STREE_NAME | — | ✅ |
| 46 | PropertyParcelAddressPEOStreetDirection | STREET_DIRECTION | — | ✅ |
| 47 | PropertyParcelAddressPEOStreetNumber | STREET_NUMBER | — | ✅ |
| 48 | PropertyParcelAddressPEOStreetType | STREET_TYPE | — | ✅ |
| 49 | PropertyParcelAddressPEOUnitNumber | UNIT_NUMBER | — | ✅ |
| 50 | PropertyParcelAddressPEOWorkPhoneCountry | WORK_PHONE_COUNTRY | — | ✅ |
| 51 | PropertyParcelAddressPEOWorkPhoneNum | WORK_PHONE_NUM | — | ✅ |

### [[psc_com_parcel_b|PSC_COM_PARCEL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PropertyParcelPEOAdditionalStructure | ADDITIONAL_STRUCTURE | — | ✅ |
| 2 | PropertyParcelPEOBathrooms | BATHROOMS | — | ✅ |
| 3 | PropertyParcelPEOBedrooms | BEDROOMS | — | ✅ |
| 4 | PropertyParcelPEOBlockNum | BLOCK_NUM | — | ✅ |
| 5 | PropertyParcelPEOBookNum | BOOK_NUM | — | ✅ |
| 6 | PropertyParcelPEOCensusBlock | CENSUS_BLOCK | — | ✅ |
| 7 | PropertyParcelPEOCensusTract | CENSUS_TRACT | — | ✅ |
| 8 | PropertyParcelPEOClimateZone | CLIMATE_ZONE | — | ✅ |
| 9 | PropertyParcelPEOCoordinateX | COORDINATE_X | — | — |
| 10 | PropertyParcelPEOCoordinateY | COORDINATE_Y | — | — |
| 11 | PropertyParcelPEOCreatedBy | CREATED_BY | — | ✅ |
| 12 | PropertyParcelPEOCreationDate | CREATION_DATE | — | ✅ |
| 13 | PropertyParcelPEODwellingUnitCount | DWELLING_UNIT_COUNT | — | ✅ |
| 14 | PropertyParcelPEOEnabledFlag | ENABLED_FLAG | — | ✅ |
| 15 | PropertyParcelPEOFireRisk | FIRE_RISK | — | ✅ |
| 16 | PropertyParcelPEOFloodInsRateMap | FLOOD_INS_RATE_MAP | — | ✅ |
| 17 | PropertyParcelPEOFloodZone | FLOOD_ZONE | — | ✅ |
| 18 | PropertyParcelPEOGeneralPlan2 | GENERAL_PLAN2 | — | ✅ |
| 19 | PropertyParcelPEOJurisdiction | JURISDICTION | — | ✅ |
| 20 | PropertyParcelPEOLandUseCode | LAND_USE_CODE | — | ✅ |
| 21 | PropertyParcelPEOLandslideRisk | LANDSLIDE_RISK | — | ✅ |
| 22 | PropertyParcelPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 23 | PropertyParcelPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 24 | PropertyParcelPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 25 | PropertyParcelPEOLatitude | LATITUDE | — | ✅ |
| 26 | PropertyParcelPEOLiquefactionRisk | LIQUEFACTION_RISK | — | ✅ |
| 27 | PropertyParcelPEOLongitude | LONGITUDE | — | ✅ |
| 28 | PropertyParcelPEOLotNum | LOT_NUM | — | ✅ |
| 29 | PropertyParcelPEOMapBookPage | MAP_BOOK_PAGE | — | ✅ |
| 30 | PropertyParcelPEOMapName | MAP_NAME | — | ✅ |
| 31 | PropertyParcelPEOModuleId | MODULE_ID | — | — |
| 32 | PropertyParcelPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 33 | PropertyParcelPEOPageNum | PAGE_NUM | — | ✅ |
| 34 | PropertyParcelPEOParcelId | PARCEL_ID | 🔑 | ✅ |
| 35 | PropertyParcelPEOParcelIdEntered | PARCEL_ID_ENTERED | — | ✅ |
| 36 | PropertyParcelPEOParcelSize1 | PARCEL_SIZE1 | — | ✅ |
| 37 | PropertyParcelPEOParcelSize1Unit | PARCEL_SIZE1_UNIT | — | ✅ |
| 38 | PropertyParcelPEOParcelSize2 | PARCEL_SIZE2 | — | ✅ |
| 39 | PropertyParcelPEOParcelSize2Unit | PARCEL_SIZE2_UNIT | — | ✅ |
| 40 | PropertyParcelPEOParcelStatus | PARCEL_STATUS | — | ✅ |
| 41 | PropertyParcelPEOParcelType | PARCEL_TYPE | — | ✅ |
| 42 | PropertyParcelPEOParentParcelId | PARENT_PARCEL_ID | — | ✅ |
| 43 | PropertyParcelPEOPatio | PATIO | — | ✅ |
| 44 | PropertyParcelPEOPool | POOL | — | ✅ |
| 45 | PropertyParcelPEOPrimaryZoningId | PRIMARY_ZONING_ID | — | ✅ |
| 46 | PropertyParcelPEOSectionNum | SECTION_NUM | — | ✅ |
| 47 | PropertyParcelPEOSoilType | SOIL_TYPE | — | ✅ |
| 48 | PropertyParcelPEOSrid | SRID | — | — |
| 49 | PropertyParcelPEOStructureSize1 | STRUCTURE_SIZE1 | — | ✅ |
| 50 | PropertyParcelPEOStructureSize1Unit | STRUCTURE_SIZE1_UNIT | — | ✅ |
| 51 | PropertyParcelPEOStructureSize2 | STRUCTURE_SIZE2 | — | ✅ |
| 52 | PropertyParcelPEOStructureSize2Unit | STRUCTURE_SIZE2_UNIT | — | ✅ |
| 53 | PropertyParcelPEOSubdivision | SUBDIVISION | — | ✅ |
| 54 | PropertyParcelPEOTaxRateArea | TAX_RATE_AREA | — | ✅ |
| 55 | PropertyParcelPEOUnitNum | UNIT_NUM | — | ✅ |
| 56 | PropertyParcelPEOYearBuilt | YEAR_BUILT | — | ✅ |
| 57 | PropertyParcelPEOZoningCode2 | ZONING_CODE2 | — | ✅ |

### [[psc_com_parcel_value_f|PSC_COM_PARCEL_VALUE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PropertyValueDPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | PropertyValueDPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | PropertyValueDPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 4 | PropertyValueDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 5 | PropertyValueDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 6 | PropertyValueDPEOFixtureExemption | FIXTURE_EXEMPTION | — | ✅ |
| 7 | PropertyValueDPEOFixtures | FIXTURES | — | ✅ |
| 8 | PropertyValueDPEOImprovementValue | IMPROVEMENT_VALUE | — | ✅ |
| 9 | PropertyValueDPEOLandValue | LAND_VALUE | — | ✅ |
| 10 | PropertyValueDPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | PropertyValueDPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | PropertyValueDPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | PropertyValueDPEONetAssessedValues | NET_ASSESSED_VALUES | — | ✅ |
| 14 | PropertyValueDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 15 | PropertyValueDPEOOtherExemption | OTHER_EXEMPTION | — | ✅ |
| 16 | PropertyValueDPEOOwnerExemption | OWNER_EXEMPTION | — | ✅ |
| 17 | PropertyValueDPEOParcelId | PARCEL_ID | — | ✅ |
| 18 | PropertyValueDPEOParcelSize | PARCEL_SIZE1 | — | ✅ |
| 19 | PropertyValueDPEOParcelSize1Uom | PARCEL_SIZE1_UOM | — | ✅ |
| 20 | PropertyValueDPEOParcelSize2 | PARCEL_SIZE2 | — | ✅ |
| 21 | PropertyValueDPEOParcelSize2Uom | PARCEL_SIZE2_UOM | — | ✅ |
| 22 | PropertyValueDPEOPersonalPropertyValue | PERSONAL_PROPERTY_VALUE | — | ✅ |
| 23 | PropertyValueDPEOPropertyUseCode | PROPERTY_USE_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
