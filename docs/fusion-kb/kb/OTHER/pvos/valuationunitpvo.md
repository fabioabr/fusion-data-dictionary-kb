---
id: DOC-OTHER-PVO-ValuationUnitPVO
doc_type: system-doc
title: "ValuationUnitPVO — PVO Cross-Module"
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
  - ValuationUnitPVO
  - valuationunitpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ValuationUnitPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Valuation Unit. Acessa as tabelas: CST_COST_BOOKS_TL, CST_COST_ORGS_V, CST_VAL_STRUCTURES_B (+3).

**Caminho:** `FscmTopModelAM.ValuationUnitAM.ValuationUnitPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 53 | 6 | 1 | 23 | 43% |

---

## 🔗 Tabelas Relacionadas

- [[cst_cost_books_tl|CST_COST_BOOKS_TL]] — 3 atributos (1 BICC)
- [[cst_cost_orgs_v|CST_COST_ORGS_V]] — 4 atributos (2 BICC)
- [[cst_val_structures_b|CST_VAL_STRUCTURES_B]] — 13 atributos (7 BICC)
- [[cst_val_structures_tl|CST_VAL_STRUCTURES_TL]] — 10 atributos (2 BICC)
- [[cst_val_units_b|CST_VAL_UNITS_B]] — 13 atributos (1 PKs, 9 BICC)
- [[cst_val_units_tl|CST_VAL_UNITS_TL]] — 10 atributos (2 BICC)

---

## ⚙️ Atributos

### [[cst_cost_books_tl|CST_COST_BOOKS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostBookTLPEOCostBookDesc | COST_BOOK_DESC | — | ✅ |
| 2 | CostBookTLPEOCostBookId | COST_BOOK_ID | — | — |
| 3 | CostBookTLPEOLanguage | LANGUAGE | — | — |

### [[cst_cost_orgs_v|CST_COST_ORGS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostOrganizationVPEOCostOrgId | COST_ORG_ID | — | — |
| 2 | CostOrganizationVPEOCostOrgName | COST_ORG_NAME | — | ✅ |
| 3 | CostOrganizationVPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 4 | CostOrganizationVPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |

### [[cst_val_structures_b|CST_VAL_STRUCTURES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ValuationStructureBEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 2 | ValuationStructureBEOCreatedBy | CREATED_BY | — | — |
| 3 | ValuationStructureBEOCreationDate | CREATION_DATE | — | — |
| 4 | ValuationStructureBEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ValuationStructureBEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | ValuationStructureBEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | ValuationStructureBEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | ValuationStructureBEOSetId | SET_ID | — | ✅ |
| 9 | ValuationStructureBEOStructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | ✅ |
| 10 | ValuationStructureBEOValStructureCode | VAL_STRUCTURE_CODE | — | ✅ |
| 11 | ValuationStructureBEOValStructureId | VAL_STRUCTURE_ID | — | ✅ |
| 12 | ValuationStructureBEOValStructureModeCode | VAL_STRUCTURE_MODE_CODE | — | ✅ |
| 13 | ValuationStructureBEOValStructureTypeCode | VAL_STRUCTURE_TYPE_CODE | — | ✅ |

### [[cst_val_structures_tl|CST_VAL_STRUCTURES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ValuationStructureTLEOCreatedBy | CREATED_BY | — | — |
| 2 | ValuationStructureTLEOCreationDate | CREATION_DATE | — | — |
| 3 | ValuationStructureTLEOLanguage | LANGUAGE | — | — |
| 4 | ValuationStructureTLEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ValuationStructureTLEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | ValuationStructureTLEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | ValuationStructureTLEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | ValuationStructureTLEOSourceLang | SOURCE_LANG | — | — |
| 9 | ValuationStructureTLEOValStructureDesc | VAL_STRUCTURE_DESC | — | ✅ |
| 10 | ValuationStructureTLEOValStructureId | VAL_STRUCTURE_ID | — | — |

### [[cst_val_units_b|CST_VAL_UNITS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ValUnitId | VAL_UNIT_ID | 🔑 | ✅ |
| 2 | ValuationUnitBEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 3 | ValuationUnitBEOCostBookId | COST_BOOK_ID | — | ✅ |
| 4 | ValuationUnitBEOCostOrgId | COST_ORG_ID | — | ✅ |
| 5 | ValuationUnitBEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | ValuationUnitBEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | ValuationUnitBEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ValuationUnitBEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ValuationUnitBEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ValuationUnitBEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | ValuationUnitBEOValStructureId | VAL_STRUCTURE_ID | — | ✅ |
| 12 | ValuationUnitBEOValStructureModeCode | VAL_STRUCTURE_MODE_CODE | — | — |
| 13 | ValuationUnitBEOValUnitCode | VAL_UNIT_CODE | — | ✅ |

### [[cst_val_units_tl|CST_VAL_UNITS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ValuationUnitTLEOCreatedBy | CREATED_BY | — | — |
| 2 | ValuationUnitTLEOCreationDate | CREATION_DATE | — | — |
| 3 | ValuationUnitTLEOLanguage | LANGUAGE | — | — |
| 4 | ValuationUnitTLEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ValuationUnitTLEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | ValuationUnitTLEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | ValuationUnitTLEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | ValuationUnitTLEOSourceLang | SOURCE_LANG | — | — |
| 9 | ValuationUnitTLEOValUnitDesc | VAL_UNIT_DESC | — | ✅ |
| 10 | ValuationUnitTLEOValUnitId | VAL_UNIT_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
