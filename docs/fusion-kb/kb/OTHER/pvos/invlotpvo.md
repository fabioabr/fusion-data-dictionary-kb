---
id: DOC-OTHER-PVO-InvLotPVO
doc_type: system-doc
title: "InvLotPVO — PVO Cross-Module"
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
  - InvLotPVO
  - invlotpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InvLotPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Inv Lot. Acessa as tabelas: INV_GRADES_B, INV_GRADES_TL, INV_LOT_NUMBERS.

**Caminho:** `FscmTopModelAM.InventoryAM.InvLotPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 82 | 3 | 4 | 15 | 18% |

---

## 🔗 Tabelas Relacionadas

- [[inv_grades_b|INV_GRADES_B]] — 8 atributos (2 BICC)
- [[inv_grades_tl|INV_GRADES_TL]] — 10 atributos (1 PKs, 3 BICC)
- [[inv_lot_numbers|INV_LOT_NUMBERS]] — 64 atributos (3 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[inv_grades_b|INV_GRADES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvGradeBPEOCreatedBy | CREATED_BY | — | — |
| 2 | InvGradeBPEOCreationDate | CREATION_DATE | — | — |
| 3 | InvGradeBPEODisableFlag | DISABLE_FLAG | — | — |
| 4 | InvGradeBPEOGradeCode | GRADE_CODE | — | ✅ |
| 5 | InvGradeBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | InvGradeBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | InvGradeBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | InvGradeBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[inv_grades_tl|INV_GRADES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvGradeTLPEOCreatedBy | CREATED_BY | — | — |
| 2 | InvGradeTLPEOCreationDate | CREATION_DATE | — | — |
| 3 | InvGradeTLPEODescription | DESCRIPTION | — | ✅ |
| 4 | InvGradeTLPEOGradeCode | GRADE_CODE | — | — |
| 5 | InvGradeTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | InvGradeTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | InvGradeTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | InvGradeTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | InvGradeTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | InvGradeTLPEOSourceLang | SOURCE_LANG | — | — |

### [[inv_lot_numbers|INV_LOT_NUMBERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpirationDateBI | EXPIRATION_DATE | — | — |
| 2 | InvLotPEOAge | AGE | — | — |
| 3 | InvLotPEOAvailabilityType | AVAILABILITY_TYPE | — | — |
| 4 | InvLotPEOBestByDate | BEST_BY_DATE | — | — |
| 5 | InvLotPEOChangeDate | CHANGE_DATE | — | — |
| 6 | InvLotPEOColor | COLOR | — | — |
| 7 | InvLotPEOCreatedBy | CREATED_BY | — | — |
| 8 | InvLotPEOCreationDate | CREATION_DATE | — | ✅ |
| 9 | InvLotPEOCurlWrinkleFold | CURL_WRINKLE_FOLD | — | — |
| 10 | InvLotPEOCyclesSinceMark | CYCLES_SINCE_MARK | — | — |
| 11 | InvLotPEOCyclesSinceNew | CYCLES_SINCE_NEW | — | — |
| 12 | InvLotPEOCyclesSinceOverhaul | CYCLES_SINCE_OVERHAUL | — | — |
| 13 | InvLotPEOCyclesSinceRepair | CYCLES_SINCE_REPAIR | — | — |
| 14 | InvLotPEOCyclesSinceVisit | CYCLES_SINCE_VISIT | — | — |
| 15 | InvLotPEODateCode | DATE_CODE | — | — |
| 16 | InvLotPEODescription | DESCRIPTION | — | — |
| 17 | InvLotPEODisableFlag | DISABLE_FLAG | — | — |
| 18 | InvLotPEOExpirationActionCode | EXPIRATION_ACTION_CODE | — | — |
| 19 | InvLotPEOExpirationActionDate | EXPIRATION_ACTION_DATE | — | — |
| 20 | InvLotPEOExpirationDate | EXPIRATION_DATE | — | ✅ |
| 21 | InvLotPEOGenObjectId | GEN_OBJECT_ID | — | — |
| 22 | InvLotPEOGradeCode | GRADE_CODE | — | — |
| 23 | InvLotPEOHoldDate | HOLD_DATE | — | — |
| 24 | InvLotPEOInventoryAtpCode | INVENTORY_ATP_CODE | — | — |
| 25 | InvLotPEOItemSize | ITEM_SIZE | — | — |
| 26 | InvLotPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 27 | InvLotPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 28 | InvLotPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 29 | InvLotPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 30 | InvLotPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 31 | InvLotPEOLengthUom | LENGTH_UOM | — | — |
| 32 | InvLotPEOLotAttributeCategory | LOT_ATTRIBUTE_CATEGORY | — | — |
| 33 | InvLotPEOLotItemDisableFlag | LOT_ITEM_DISABLE_FLAG | — | ✅ |
| 34 | InvLotPEOLotLength | LOT_LENGTH | — | — |
| 35 | InvLotPEOLotThickness | LOT_THICKNESS | — | — |
| 36 | InvLotPEOLotVolume | LOT_VOLUME | — | — |
| 37 | InvLotPEOLotWidth | LOT_WIDTH | — | — |
| 38 | InvLotPEOMaturityDate | MATURITY_DATE | — | — |
| 39 | InvLotPEONumberOfRepairs | NUMBER_OF_REPAIRS | — | — |
| 40 | InvLotPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 41 | InvLotPEOOriginationDate | ORIGINATION_DATE | — | ✅ |
| 42 | InvLotPEOOriginationType | ORIGINATION_TYPE | — | — |
| 43 | InvLotPEOParentLotNumber | PARENT_LOT_NUMBER | — | ✅ |
| 44 | InvLotPEOPlaceOfOrigin | PLACE_OF_ORIGIN | — | — |
| 45 | InvLotPEORecycledContent | RECYCLED_CONTENT | — | — |
| 46 | InvLotPEORequestId | REQUEST_ID | — | — |
| 47 | InvLotPEOReservableType | RESERVABLE_TYPE | — | — |
| 48 | InvLotPEORetestDate | RETEST_DATE | — | — |
| 49 | InvLotPEOSamplingEventId | SAMPLING_EVENT_ID | — | — |
| 50 | InvLotPEOStatusId | STATUS_ID | — | ✅ |
| 51 | InvLotPEOSupplierLotNumber | SUPPLIER_LOT_NUMBER | — | — |
| 52 | InvLotPEOTerritoryCode | TERRITORY_CODE | — | — |
| 53 | InvLotPEOThicknessUom | THICKNESS_UOM | — | — |
| 54 | InvLotPEOTimeSinceMark | TIME_SINCE_MARK | — | — |
| 55 | InvLotPEOTimeSinceRepair | TIME_SINCE_REPAIR | — | — |
| 56 | InvLotPEOTimeSinceVisit | TIME_SINCE_VISIT | — | — |
| 57 | InvLotPEOVendorId | VENDOR_ID | — | — |
| 58 | InvLotPEOVendorName | VENDOR_NAME | — | — |
| 59 | InvLotPEOVolumeUom | VOLUME_UOM | — | — |
| 60 | InvLotPEOWidthUom | WIDTH_UOM | — | — |
| 61 | InventoryItemId | INVENTORY_ITEM_ID | 🔑 | ✅ |
| 62 | LotNumber | LOT_NUMBER | 🔑 | ✅ |
| 63 | OrganizationId | ORGANIZATION_ID | 🔑 | ✅ |
| 64 | UniqueDeviceIdentifier | UNIQUE_DEVICE_IDENTIFIER | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
