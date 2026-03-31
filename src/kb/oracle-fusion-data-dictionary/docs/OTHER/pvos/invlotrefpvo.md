---
id: DOC-OTHER-PVO-InvLotRefPVO
doc_type: system-doc
title: "InvLotRefPVO — PVO Cross-Module"
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
  - InvLotRefPVO
  - invlotrefpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InvLotRefPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Inv Lot Ref. Acessa as tabelas: INV_GRADES_B, INV_GRADES_TL, INV_LOT_NUMBERS.

**Caminho:** `FscmTopModelAM.InventoryAM.InvLotRefPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 82 | 3 | 4 | 17 | 21% |

---

## 🔗 Tabelas Relacionadas

- [[inv_grades_b|INV_GRADES_B]] — 8 atributos (1 PKs, 2 BICC)
- [[inv_grades_tl|INV_GRADES_TL]] — 10 atributos (3 BICC)
- [[inv_lot_numbers|INV_LOT_NUMBERS]] — 64 atributos (3 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[inv_grades_b|INV_GRADES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy1 | CREATED_BY | — | — |
| 2 | CreationDate1 | CREATION_DATE | — | — |
| 3 | DisableFlag1 | DISABLE_FLAG | — | — |
| 4 | GradeCode1 | GRADE_CODE | 🔑 | ✅ |
| 5 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 7 | LastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 8 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |

### [[inv_grades_tl|INV_GRADES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy2 | CREATED_BY | — | — |
| 2 | CreationDate2 | CREATION_DATE | — | — |
| 3 | Description1 | DESCRIPTION | — | ✅ |
| 4 | GradeCode2 | GRADE_CODE | — | — |
| 5 | Language | LANGUAGE | — | ✅ |
| 6 | LastUpdateDate2 | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 8 | LastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 9 | ObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 10 | SourceLang | SOURCE_LANG | — | — |

### [[inv_lot_numbers|INV_LOT_NUMBERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Age | AGE | — | — |
| 2 | AvailabilityType | AVAILABILITY_TYPE | — | — |
| 3 | BestByDate | BEST_BY_DATE | — | — |
| 4 | ChangeDate | CHANGE_DATE | — | — |
| 5 | Color | COLOR | — | — |
| 6 | CreatedBy | CREATED_BY | — | — |
| 7 | CreationDate | CREATION_DATE | — | ✅ |
| 8 | CurlWrinkleFold | CURL_WRINKLE_FOLD | — | — |
| 9 | CyclesSinceMark | CYCLES_SINCE_MARK | — | — |
| 10 | CyclesSinceNew | CYCLES_SINCE_NEW | — | — |
| 11 | CyclesSinceOverhaul | CYCLES_SINCE_OVERHAUL | — | — |
| 12 | CyclesSinceRepair | CYCLES_SINCE_REPAIR | — | — |
| 13 | CyclesSinceVisit | CYCLES_SINCE_VISIT | — | — |
| 14 | DateCode | DATE_CODE | — | — |
| 15 | Description | DESCRIPTION | — | ✅ |
| 16 | DisableFlag | DISABLE_FLAG | — | — |
| 17 | ExpirationActionCode | EXPIRATION_ACTION_CODE | — | — |
| 18 | ExpirationActionDate | EXPIRATION_ACTION_DATE | — | — |
| 19 | ExpirationDate | EXPIRATION_DATE | — | ✅ |
| 20 | ExpirationDateBI | EXPIRATION_DATE | — | — |
| 21 | GenObjectId | GEN_OBJECT_ID | — | — |
| 22 | GradeCode | GRADE_CODE | — | ✅ |
| 23 | HoldDate | HOLD_DATE | — | — |
| 24 | InventoryAtpCode | INVENTORY_ATP_CODE | — | — |
| 25 | InventoryItemId | INVENTORY_ITEM_ID | 🔑 | ✅ |
| 26 | ItemSize | ITEM_SIZE | — | — |
| 27 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 28 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 29 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 30 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 31 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 32 | LengthUom | LENGTH_UOM | — | — |
| 33 | LotAttributeCategory | LOT_ATTRIBUTE_CATEGORY | — | — |
| 34 | LotItemDisableFlag | LOT_ITEM_DISABLE_FLAG | — | ✅ |
| 35 | LotLength | LOT_LENGTH | — | — |
| 36 | LotNumber | LOT_NUMBER | 🔑 | ✅ |
| 37 | LotThickness | LOT_THICKNESS | — | — |
| 38 | LotVolume | LOT_VOLUME | — | — |
| 39 | LotWidth | LOT_WIDTH | — | — |
| 40 | MaturityDate | MATURITY_DATE | — | — |
| 41 | NumberOfRepairs | NUMBER_OF_REPAIRS | — | — |
| 42 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 43 | OrganizationId | ORGANIZATION_ID | 🔑 | ✅ |
| 44 | OriginationDate | ORIGINATION_DATE | — | ✅ |
| 45 | OriginationType | ORIGINATION_TYPE | — | — |
| 46 | ParentLotNumber | PARENT_LOT_NUMBER | — | ✅ |
| 47 | PlaceOfOrigin | PLACE_OF_ORIGIN | — | — |
| 48 | RecycledContent | RECYCLED_CONTENT | — | — |
| 49 | RequestId | REQUEST_ID | — | — |
| 50 | ReservableType | RESERVABLE_TYPE | — | — |
| 51 | RetestDate | RETEST_DATE | — | — |
| 52 | SamplingEventId | SAMPLING_EVENT_ID | — | — |
| 53 | StatusId | STATUS_ID | — | ✅ |
| 54 | SupplierLotNumber | SUPPLIER_LOT_NUMBER | — | — |
| 55 | TerritoryCode | TERRITORY_CODE | — | — |
| 56 | ThicknessUom | THICKNESS_UOM | — | — |
| 57 | TimeSinceMark | TIME_SINCE_MARK | — | — |
| 58 | TimeSinceRepair | TIME_SINCE_REPAIR | — | — |
| 59 | TimeSinceVisit | TIME_SINCE_VISIT | — | — |
| 60 | UniqueDeviceIdentifier | UNIQUE_DEVICE_IDENTIFIER | — | — |
| 61 | VendorId | VENDOR_ID | — | — |
| 62 | VendorName | VENDOR_NAME | — | — |
| 63 | VolumeUom | VOLUME_UOM | — | — |
| 64 | WidthUom | WIDTH_UOM | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
