---
id: DOC-OTHER-PVO-PSCPropertyParcelPVO
doc_type: system-doc
title: "PSCPropertyParcelPVO — PVO Cross-Module"
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
  - PSCPropertyParcelPVO
  - pscpropertyparcelpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PSCPropertyParcelPVO

## 📌 Visão Geral

View Object para extração BICC de dados de PSCProperty Parcel. Acessa as tabelas: PSC_COM_PARCEL_B.

**Caminho:** `FscmTopModelAM.PscPermitsReportingAM.PSCPropertyParcelPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 57 | 1 | 1 | 51 | 89% |

---

## 🔗 Tabelas Relacionadas

- [[psc_com_parcel_b|PSC_COM_PARCEL_B]] — 57 atributos (1 PKs, 51 BICC)

---

## ⚙️ Atributos

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

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
