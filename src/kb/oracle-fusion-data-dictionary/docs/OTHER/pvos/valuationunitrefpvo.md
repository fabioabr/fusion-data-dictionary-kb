---
id: DOC-OTHER-PVO-ValuationUnitRefPVO
doc_type: system-doc
title: "ValuationUnitRefPVO — PVO Cross-Module"
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
  - ValuationUnitRefPVO
  - valuationunitrefpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ValuationUnitRefPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Valuation Unit Ref. Acessa as tabelas: CST_COST_BOOKS_TL, CST_COST_ORGS_V, CST_VAL_STRUCTURES_B (+3).

**Caminho:** `FscmTopModelAM.ValuationUnitAM.ValuationUnitRefPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 51 | 6 | 1 | 23 | 45% |

---

## 🔗 Tabelas Relacionadas

- [[cst_cost_books_tl|CST_COST_BOOKS_TL]] — 3 atributos (1 BICC)
- [[cst_cost_orgs_v|CST_COST_ORGS_V]] — 4 atributos (2 BICC)
- [[cst_val_structures_b|CST_VAL_STRUCTURES_B]] — 12 atributos (7 BICC)
- [[cst_val_structures_tl|CST_VAL_STRUCTURES_TL]] — 10 atributos (2 BICC)
- [[cst_val_units_b|CST_VAL_UNITS_B]] — 12 atributos (1 PKs, 9 BICC)
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
| 1 | ValuationStructureBPEOCreatedBy2 | CREATED_BY | — | — |
| 2 | ValuationStructureBPEOCreationDate2 | CREATION_DATE | — | — |
| 3 | ValuationStructureBPEOLastUpdateDate2 | LAST_UPDATE_DATE | — | ✅ |
| 4 | ValuationStructureBPEOLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 5 | ValuationStructureBPEOLastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 6 | ValuationStructureBPEOObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 7 | ValuationStructureBPEOSetId | SET_ID | — | ✅ |
| 8 | ValuationStructureBPEOStructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | ✅ |
| 9 | ValuationStructureBPEOValStructureCode | VAL_STRUCTURE_CODE | — | ✅ |
| 10 | ValuationStructureBPEOValStructureId1 | VAL_STRUCTURE_ID | — | ✅ |
| 11 | ValuationStructureBPEOValStructureModeCode1 | VAL_STRUCTURE_MODE_CODE | — | ✅ |
| 12 | ValuationStructureBPEOValStructureTypeCode | VAL_STRUCTURE_TYPE_CODE | — | ✅ |

### [[cst_val_structures_tl|CST_VAL_STRUCTURES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ValuationStructureTLPEOCreatedBy3 | CREATED_BY | — | — |
| 2 | ValuationStructureTLPEOCreationDate3 | CREATION_DATE | — | — |
| 3 | ValuationStructureTLPEOLanguage1 | LANGUAGE | — | — |
| 4 | ValuationStructureTLPEOLastUpdateDate3 | LAST_UPDATE_DATE | — | ✅ |
| 5 | ValuationStructureTLPEOLastUpdateLogin3 | LAST_UPDATE_LOGIN | — | — |
| 6 | ValuationStructureTLPEOLastUpdatedBy3 | LAST_UPDATED_BY | — | — |
| 7 | ValuationStructureTLPEOObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 8 | ValuationStructureTLPEOSourceLang1 | SOURCE_LANG | — | — |
| 9 | ValuationStructureTLPEOValStructureDesc | VAL_STRUCTURE_DESC | — | ✅ |
| 10 | ValuationStructureTLPEOValStructureId2 | VAL_STRUCTURE_ID | — | — |

### [[cst_val_units_b|CST_VAL_UNITS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ValUnitId | VAL_UNIT_ID | 🔑 | ✅ |
| 2 | ValuationUnitBPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 3 | ValuationUnitBPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 4 | ValuationUnitBPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | ValuationUnitBPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | ValuationUnitBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ValuationUnitBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | ValuationUnitBPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ValuationUnitBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | ValuationUnitBPEOValStructureId | VAL_STRUCTURE_ID | — | ✅ |
| 11 | ValuationUnitBPEOValStructureModeCode | VAL_STRUCTURE_MODE_CODE | — | — |
| 12 | ValuationUnitBPEOValUnitCode | VAL_UNIT_CODE | — | ✅ |

### [[cst_val_units_tl|CST_VAL_UNITS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ValuationUnitTLPEOCreatedBy1 | CREATED_BY | — | — |
| 2 | ValuationUnitTLPEOCreationDate1 | CREATION_DATE | — | — |
| 3 | ValuationUnitTLPEOLanguage | LANGUAGE | — | — |
| 4 | ValuationUnitTLPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 5 | ValuationUnitTLPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 6 | ValuationUnitTLPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 7 | ValuationUnitTLPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 8 | ValuationUnitTLPEOSourceLang | SOURCE_LANG | — | — |
| 9 | ValuationUnitTLPEOValUnitDesc | VAL_UNIT_DESC | — | ✅ |
| 10 | ValuationUnitTLPEOValUnitId1 | VAL_UNIT_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
