---
id: DOC-GL-PVO-LegislativeDataGroupPVO
doc_type: system-doc
title: "LegislativeDataGroupPVO — PVO General Ledger"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - gl
  - data-dictionary
  - pvo
  - bicc
aliases:
  - LegislativeDataGroupPVO
  - legislativedatagrouppvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LegislativeDataGroupPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Legislative Data Group. Acessa as tabelas: PER_LEGISLATIVE_DATA_GROUPS, PER_LEGISLATIVE_DATA_GROUPS_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.LegislativeDataGroupAM.LegislativeDataGroupPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 2 | 2 | 15 | 71% |

---

## 🔗 Tabelas Relacionadas

- [[per_legislative_data_groups|PER_LEGISLATIVE_DATA_GROUPS]] — 11 atributos (1 PKs, 8 BICC)
- [[per_legislative_data_groups_tl|PER_LEGISLATIVE_DATA_GROUPS_TL]] — 10 atributos (1 PKs, 7 BICC)

---

## ⚙️ Atributos

### [[per_legislative_data_groups|PER_LEGISLATIVE_DATA_GROUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | 🔑 | ✅ |
| 2 | LegislativeDataGroupPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | LegislativeDataGroupPEOCostAllocationIdFlexNum | COST_ALLOCATION_ID_FLEX_NUM | — | ✅ |
| 4 | LegislativeDataGroupPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | LegislativeDataGroupPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | LegislativeDataGroupPEODefaultCurrencyCode | DEFAULT_CURRENCY_CODE | — | ✅ |
| 7 | LegislativeDataGroupPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LegislativeDataGroupPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | LegislativeDataGroupPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | LegislativeDataGroupPEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 11 | LegislativeDataGroupPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[per_legislative_data_groups_tl|PER_LEGISLATIVE_DATA_GROUPS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LegislativeDataGroupTLEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | LegislativeDataGroupTLEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | LegislativeDataGroupTLEOLanguage | LANGUAGE | 🔑 | ✅ |
| 4 | LegislativeDataGroupTLEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LegislativeDataGroupTLEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | LegislativeDataGroupTLEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | LegislativeDataGroupTLEOLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | — |
| 8 | LegislativeDataGroupTLEOName | NAME | — | ✅ |
| 9 | LegislativeDataGroupTLEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | LegislativeDataGroupTLEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
