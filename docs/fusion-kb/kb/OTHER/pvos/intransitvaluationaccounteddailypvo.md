---
id: DOC-OTHER-PVO-IntransitValuationAccountedDailyPVO
doc_type: system-doc
title: "IntransitValuationAccountedDailyPVO — PVO Cross-Module"
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
  - IntransitValuationAccountedDailyPVO
  - intransitvaluationaccounteddailypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# IntransitValuationAccountedDailyPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Intransit Valuation Accounted Daily. Acessa as tabelas: CST_ACCT_INTRANSIT_DAILY, CST_COST_BOOKS_TL, CST_COST_ORGS_V (+6).

**Caminho:** `FscmTopModelAM.OnhandValuationAM.IntransitValuationAccountedDailyPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 57 | 9 | 1 | 27 | 47% |

---

## 🔗 Tabelas Relacionadas

- [[cst_acct_intransit_daily|CST_ACCT_INTRANSIT_DAILY]] — 28 atributos (1 PKs, 24 BICC)
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

### [[cst_acct_intransit_daily|CST_ACCT_INTRANSIT_DAILY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IntransitAccountedEOAmount | AMOUNT | — | ✅ |
| 2 | IntransitAccountedEOBusinessUnitId | BUSINESS_UNIT_ID | — | ✅ |
| 3 | IntransitAccountedEOCostBookId | COST_BOOK_ID | — | ✅ |
| 4 | IntransitAccountedEOCostOrgId | COST_ORG_ID | — | ✅ |
| 5 | IntransitAccountedEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | IntransitAccountedEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | IntransitAccountedEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 8 | IntransitAccountedEOEffToDate | EFF_TO_DATE | — | ✅ |
| 9 | IntransitAccountedEOFobPoint | FOB_POINT | — | ✅ |
| 10 | IntransitAccountedEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 11 | IntransitAccountedEOInventoryOrgId | INVENTORY_ORG_ID | — | ✅ |
| 12 | IntransitAccountedEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 13 | IntransitAccountedEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 14 | IntransitAccountedEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | IntransitAccountedEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | IntransitAccountedEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 17 | IntransitAccountedEOLocatorId | LOCATOR_ID | — | ✅ |
| 18 | IntransitAccountedEOQuantity | QUANTITY | — | ✅ |
| 19 | IntransitAccountedEORequestId | REQUEST_ID | — | — |
| 20 | IntransitAccountedEOSnapshotDate | SNAPSHOT_DATE | — | ✅ |
| 21 | IntransitAccountedEOSubinventoryCode | SUBINVENTORY_CODE | — | ✅ |
| 22 | IntransitAccountedEOTransferBookId | TRANSFER_BOOK_ID | — | ✅ |
| 23 | IntransitAccountedEOTransferCostOrgId | TRANSFER_COST_ORG_ID | — | ✅ |
| 24 | IntransitAccountedEOTransferInventoryOrgId | TRANSFER_INVENTORY_ORG_ID | — | ✅ |
| 25 | IntransitAccountedEOTransferLocatorId | TRANSFER_LOCATOR_ID | — | ✅ |
| 26 | IntransitAccountedEOTransferSubinventoryCode | TRANSFER_SUBINVENTORY_CODE | — | ✅ |
| 27 | IntransitAccountedEOUom | UOM | — | ✅ |
| 28 | PkIndex | PK_INDEX | 🔑 | ✅ |

### [[cst_cost_books_tl|CST_COST_BOOKS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransferBookPEOCostBookDesc | COST_BOOK_DESC | — | — |
| 2 | TransferBookPEOCostBookId | COST_BOOK_ID | — | — |
| 3 | TransferBookPEOLanguage | LANGUAGE | — | — |

### [[cst_cost_orgs_v|CST_COST_ORGS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransferCostOrgEOCostOrgId | COST_ORG_ID | — | — |
| 2 | TransferCostOrgEOCostOrgName | COST_ORG_NAME | — | — |
| 3 | TransferCostOrgEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 4 | TransferCostOrgEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |

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
| 3 | GlCalendarsPeriodSetId | PERIOD_SET_ID | — | — |
| 4 | GlCalendarsPeriodSetName | PERIOD_SET_NAME | — | ✅ |
| 5 | GlCalendarsPeriodType | PERIOD_TYPE | — | ✅ |
| 6 | GlCalendarsPeriodTypeId | PERIOD_TYPE_ID | — | — |

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
| 1 | TransferSubInvEODescription | DESCRIPTION | — | — |
| 2 | TransferSubInvEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 3 | TransferSubInvEOOrganizationId | ORGANIZATION_ID | — | — |
| 4 | TransferSubInvEOSecondaryInventoryName | SECONDARY_INVENTORY_NAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
