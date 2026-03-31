---
id: DOC-OTHER-PVO-EndDemandPVO
doc_type: system-doc
title: "EndDemandPVO — PVO Cross-Module"
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
  - EndDemandPVO
  - enddemandpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EndDemandPVO

## 📌 Visão Geral

View Object para extração BICC de dados de End Demand. Acessa as tabelas: MSC_ANALYTIC_END_DEMANDS.

**Caminho:** `FscmTopModelAM.MscAnalyticsTopAM.EndDemandPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 39 | 1 | 1 | 34 | 87% |

---

## 🔗 Tabelas Relacionadas

- [[msc_analytic_end_demands|MSC_ANALYTIC_END_DEMANDS]] — 39 atributos (1 PKs, 34 BICC)

---

## ⚙️ Atributos

### [[msc_analytic_end_demands|MSC_ANALYTIC_END_DEMANDS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DemandId | DEMAND_ID | 🔑 | ✅ |
| 2 | EndDemandPEOAttributeDisplayValue13 | ATTRIBUTE_DISPLAY_VALUE13 | — | ✅ |
| 3 | EndDemandPEOAttributeDisplayValue14 | ATTRIBUTE_DISPLAY_VALUE14 | — | ✅ |
| 4 | EndDemandPEOAttributeDisplayValue15 | ATTRIBUTE_DISPLAY_VALUE15 | — | ✅ |
| 5 | EndDemandPEOAttributeDisplayValue16 | ATTRIBUTE_DISPLAY_VALUE16 | — | ✅ |
| 6 | EndDemandPEOAttributeDisplayValue17 | ATTRIBUTE_DISPLAY_VALUE17 | — | ✅ |
| 7 | EndDemandPEOAttributeDisplayValue18 | ATTRIBUTE_DISPLAY_VALUE18 | — | ✅ |
| 8 | EndDemandPEOAttributeDisplayValue19 | ATTRIBUTE_DISPLAY_VALUE19 | — | ✅ |
| 9 | EndDemandPEOAttributeDisplayValue20 | ATTRIBUTE_DISPLAY_VALUE20 | — | ✅ |
| 10 | EndDemandPEOAttributeDisplayValue21 | ATTRIBUTE_DISPLAY_VALUE21 | — | ✅ |
| 11 | EndDemandPEOAttributeDisplayValue22 | ATTRIBUTE_DISPLAY_VALUE22 | — | ✅ |
| 12 | EndDemandPEOAttributeDisplayValue23 | ATTRIBUTE_DISPLAY_VALUE23 | — | ✅ |
| 13 | EndDemandPEOAttributeDisplayValue24 | ATTRIBUTE_DISPLAY_VALUE24 | — | ✅ |
| 14 | EndDemandPEOAttributeDisplayValue25 | ATTRIBUTE_DISPLAY_VALUE25 | — | ✅ |
| 15 | EndDemandPEOCreatedBy | CREATED_BY | — | ✅ |
| 16 | EndDemandPEOCreationDate | CREATION_DATE | — | ✅ |
| 17 | EndDemandPEODemandPriority | DEMAND_PRIORITY | — | — |
| 18 | EndDemandPEOGlobalAttributeNumber11 | GLOBAL_ATTRIBUTE_NUMBER11 | — | — |
| 19 | EndDemandPEOGlobalAttributeNumber12 | GLOBAL_ATTRIBUTE_NUMBER12 | — | — |
| 20 | EndDemandPEOGlobalAttributeNumber26 | GLOBAL_ATTRIBUTE_NUMBER26 | — | — |
| 21 | EndDemandPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 22 | EndDemandPEOItemDescription | ITEM_DESCRIPTION | — | ✅ |
| 23 | EndDemandPEOItemName | ITEM_NAME | — | ✅ |
| 24 | EndDemandPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 25 | EndDemandPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 26 | EndDemandPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 27 | EndDemandPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 28 | EndDemandPEOOrderNumber | ORDER_NUMBER | — | ✅ |
| 29 | EndDemandPEOOrderType | ORDER_TYPE | — | ✅ |
| 30 | EndDemandPEOOrderTypeText | ORDER_TYPE_TEXT | — | ✅ |
| 31 | EndDemandPEOOrganizationCode | ORGANIZATION_CODE | — | ✅ |
| 32 | EndDemandPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 33 | EndDemandPEOOrganizationName | ORGANIZATION_NAME | — | ✅ |
| 34 | EndDemandPEOOverrideDemandPriority | OVERRIDE_DEMAND_PRIORITY | — | — |
| 35 | EndDemandPEOPlanId | PLAN_ID | — | ✅ |
| 36 | EndDemandPEOProject | PROJECT | — | ✅ |
| 37 | EndDemandPEOProjectGroup | PROJECT_GROUP | — | ✅ |
| 38 | EndDemandPEOSegmentName | SEGMENT_NAME | — | ✅ |
| 39 | EndDemandPEOTask | TASK | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
