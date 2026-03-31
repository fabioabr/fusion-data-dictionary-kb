---
id: DOC-OTHER-PVO-IntransitValuationCostedDailyPVO
doc_type: system-doc
title: "IntransitValuationCostedDailyPVO — PVO Cross-Module"
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
  - IntransitValuationCostedDailyPVO
  - intransitvaluationcosteddailypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# IntransitValuationCostedDailyPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Intransit Valuation Costed Daily. Acessa as tabelas: CST_COSTED_INTRANSIT_DAILY, CST_COST_BOOKS_TL, CST_COST_ORGS_V (+6).

**Caminho:** `FscmTopModelAM.OnhandValuationAM.IntransitValuationCostedDailyPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 57 | 9 | 1 | 27 | 47% |

---

## 🔗 Tabelas Relacionadas

- [[cst_costed_intransit_daily|CST_COSTED_INTRANSIT_DAILY]] — 28 atributos (1 PKs, 24 BICC)
- [[cst_cost_books_tl|CST_COST_BOOKS_TL]] — 3 atributos
- [[cst_cost_orgs_v|CST_COST_ORGS_V]] — 4 atributos (1 BICC)
- [[cst_cost_org_books|CST_COST_ORG_BOOKS]] — 4 atributos
- [[egp_system_items_b_v|EGP_SYSTEM_ITEMS_B_V]] — 3 atributos
- [[gl_calendars|GL_CALENDARS]] — 6 atributos (2 BICC)
- [[inv_item_locations|INV_ITEM_LOCATIONS]] — 3 atributos
- [[inv_org_parameters_v|INV_ORG_PARAMETERS_V]] — 2 atributos
- [[inv_secondary_inventories|INV_SECONDARY_INVENTORIES]] — 4 atributos

---

## ⚙️ Atributos

### [[cst_costed_intransit_daily|CST_COSTED_INTRANSIT_DAILY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IntransitCostedEOAmount | AMOUNT | — | ✅ |
| 2 | IntransitCostedEOBusinessUnitId | BUSINESS_UNIT_ID | — | ✅ |
| 3 | IntransitCostedEOCostBookId | COST_BOOK_ID | — | ✅ |
| 4 | IntransitCostedEOCostOrgId | COST_ORG_ID | — | ✅ |
| 5 | IntransitCostedEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | IntransitCostedEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | IntransitCostedEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 8 | IntransitCostedEOEffToDate | EFF_TO_DATE | — | ✅ |
| 9 | IntransitCostedEOFobPoint | FOB_POINT | — | ✅ |
| 10 | IntransitCostedEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 11 | IntransitCostedEOInventoryOrgId | INVENTORY_ORG_ID | — | ✅ |
| 12 | IntransitCostedEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 13 | IntransitCostedEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 14 | IntransitCostedEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | IntransitCostedEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | IntransitCostedEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 17 | IntransitCostedEOLocatorId | LOCATOR_ID | — | ✅ |
| 18 | IntransitCostedEOQuantity | QUANTITY | — | ✅ |
| 19 | IntransitCostedEORequestId | REQUEST_ID | — | — |
| 20 | IntransitCostedEOSnapshotDate | SNAPSHOT_DATE | — | ✅ |
| 21 | IntransitCostedEOSubinventoryCode | SUBINVENTORY_CODE | — | ✅ |
| 22 | IntransitCostedEOTransferBookId | TRANSFER_BOOK_ID | — | ✅ |
| 23 | IntransitCostedEOTransferCostOrgId | TRANSFER_COST_ORG_ID | — | ✅ |
| 24 | IntransitCostedEOTransferInventoryOrgId | TRANSFER_INVENTORY_ORG_ID | — | ✅ |
| 25 | IntransitCostedEOTransferLocatorId | TRANSFER_LOCATOR_ID | — | ✅ |
| 26 | IntransitCostedEOTransferSubinventoryCode | TRANSFER_SUBINVENTORY_CODE | — | ✅ |
| 27 | IntransitCostedEOUom | UOM | — | ✅ |
| 28 | PkIndex | PK_INDEX | 🔑 | ✅ |

### [[cst_cost_books_tl|CST_COST_BOOKS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransferCostBookPEOCostBookDesc | COST_BOOK_DESC | — | — |
| 2 | TransferCostBookPEOCostBookId | COST_BOOK_ID | — | — |
| 3 | TransferCostBookPEOLanguage | LANGUAGE | — | — |

### [[cst_cost_orgs_v|CST_COST_ORGS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransferCostOrgPEOCostOrgId | COST_ORG_ID | — | — |
| 2 | TransferCostOrgPEOCostOrgName | COST_ORG_NAME | — | — |
| 3 | TransferCostOrgPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 4 | TransferCostOrgPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |

### [[cst_cost_org_books|CST_COST_ORG_BOOKS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostOrgBookPEOCalendarId | CALENDAR_ID | — | — |
| 2 | CostOrgBookPEOCostBookId | COST_BOOK_ID | — | — |
| 3 | CostOrgBookPEOCostOrgId | COST_ORG_ID | — | — |
| 4 | LedgerId | LEDGER_ID | — | — |

### [[egp_system_items_b_v|EGP_SYSTEM_ITEMS_B_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemBasePEOBaseItemId | BASE_ITEM_ID | — | — |
| 2 | ItemBasePEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 3 | ItemBasePEOOrganizationId | ORGANIZATION_ID | — | — |

### [[gl_calendars|GL_CALENDARS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlCalendarsCalendarId | CALENDAR_ID | — | — |
| 2 | GlCalendarsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 3 | GlCalendarsPeriodSetName | PERIOD_SET_NAME | — | ✅ |
| 4 | GlCalendarsPeriodType | PERIOD_TYPE | — | ✅ |
| 5 | GlCalendarsPeriodTypeId | PERIOD_TYPE_ID | — | — |
| 6 | PeriodSetId | PERIOD_SET_ID | — | — |

### [[inv_item_locations|INV_ITEM_LOCATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransferLocatorEODescription | DESCRIPTION | — | — |
| 2 | TransferLocatorEOInventoryLocationId | INVENTORY_LOCATION_ID | — | — |
| 3 | TransferLocatorEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[inv_org_parameters_v|INV_ORG_PARAMETERS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransferInvOrgEOOrganizationCode | ORGANIZATION_CODE | — | — |
| 2 | TransferInvOrgEOOrganizationId | ORGANIZATION_ID | — | — |

### [[inv_secondary_inventories|INV_SECONDARY_INVENTORIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransferInvOrgEODescription | DESCRIPTION | — | — |
| 2 | TransferSubInvEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 3 | TransferSubInvEOOrganizationId | ORGANIZATION_ID | — | — |
| 4 | TransferSubInvEOSecondaryInventoryName | SECONDARY_INVENTORY_NAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
