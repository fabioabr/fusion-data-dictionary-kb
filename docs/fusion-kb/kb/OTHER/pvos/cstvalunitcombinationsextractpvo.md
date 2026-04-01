---
id: DOC-OTHER-PVO-CstValUnitCombinationsExtractPVO
doc_type: system-doc
title: "CstValUnitCombinationsExtractPVO — PVO Cross-Module"
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
  - CstValUnitCombinationsExtractPVO
  - cstvalunitcombinationsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstValUnitCombinationsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Val Unit Combinations Extract. Acessa as tabelas: CST_VAL_UNITS_B, CST_VAL_UNIT_COMBINATIONS, CST_VAL_UNIT_DETAILS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstValUnitCombinationsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 64 | 3 | 3 | 64 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_val_units_b|CST_VAL_UNITS_B]] — 3 atributos (1 PKs, 3 BICC)
- [[cst_val_unit_combinations|CST_VAL_UNIT_COMBINATIONS]] — 60 atributos (1 PKs, 60 BICC)
- [[cst_val_unit_details|CST_VAL_UNIT_DETAILS]] — 1 atributos (1 PKs, 1 BICC)

---

## ⚙️ Atributos

### [[cst_val_units_b|CST_VAL_UNITS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ValuationUnitBPEOValStructureId | VAL_STRUCTURE_ID | — | ✅ |
| 2 | ValuationUnitBPEOValUnitCode | VAL_UNIT_CODE | — | ✅ |
| 3 | ValuationUnitBPEOValUnitId | VAL_UNIT_ID | 🔑 | ✅ |

### [[cst_val_unit_combinations|CST_VAL_UNIT_COMBINATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstValUnitCombinationsPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 2 | CstValUnitCombinationsPEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | ✅ |
| 3 | CstValUnitCombinationsPEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | ✅ |
| 4 | CstValUnitCombinationsPEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | ✅ |
| 5 | CstValUnitCombinationsPEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | ✅ |
| 6 | CstValUnitCombinationsPEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | ✅ |
| 7 | CstValUnitCombinationsPEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | ✅ |
| 8 | CstValUnitCombinationsPEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | ✅ |
| 9 | CstValUnitCombinationsPEOAttributeChar16 | ATTRIBUTE_CHAR16 | — | ✅ |
| 10 | CstValUnitCombinationsPEOAttributeChar17 | ATTRIBUTE_CHAR17 | — | ✅ |
| 11 | CstValUnitCombinationsPEOAttributeChar18 | ATTRIBUTE_CHAR18 | — | ✅ |
| 12 | CstValUnitCombinationsPEOAttributeChar19 | ATTRIBUTE_CHAR19 | — | ✅ |
| 13 | CstValUnitCombinationsPEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | ✅ |
| 14 | CstValUnitCombinationsPEOAttributeChar20 | ATTRIBUTE_CHAR20 | — | ✅ |
| 15 | CstValUnitCombinationsPEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | ✅ |
| 16 | CstValUnitCombinationsPEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | ✅ |
| 17 | CstValUnitCombinationsPEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | ✅ |
| 18 | CstValUnitCombinationsPEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | ✅ |
| 19 | CstValUnitCombinationsPEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | ✅ |
| 20 | CstValUnitCombinationsPEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | ✅ |
| 21 | CstValUnitCombinationsPEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | ✅ |
| 22 | CstValUnitCombinationsPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 23 | CstValUnitCombinationsPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 24 | CstValUnitCombinationsPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 25 | CstValUnitCombinationsPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 26 | CstValUnitCombinationsPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 27 | CstValUnitCombinationsPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 28 | CstValUnitCombinationsPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 29 | CstValUnitCombinationsPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 30 | CstValUnitCombinationsPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 31 | CstValUnitCombinationsPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 32 | CstValUnitCombinationsPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 33 | CstValUnitCombinationsPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 34 | CstValUnitCombinationsPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 35 | CstValUnitCombinationsPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 36 | CstValUnitCombinationsPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 37 | CstValUnitCombinationsPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 38 | CstValUnitCombinationsPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 39 | CstValUnitCombinationsPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 40 | CstValUnitCombinationsPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 41 | CstValUnitCombinationsPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 42 | CstValUnitCombinationsPEOCostOrgCode | COST_ORG_CODE | — | ✅ |
| 43 | CstValUnitCombinationsPEOCreatedBy | CREATED_BY | — | ✅ |
| 44 | CstValUnitCombinationsPEOCreationDate | CREATION_DATE | — | ✅ |
| 45 | CstValUnitCombinationsPEOEnabledFlag | ENABLED_FLAG | — | ✅ |
| 46 | CstValUnitCombinationsPEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 47 | CstValUnitCombinationsPEOGradeCode | GRADE_CODE | — | ✅ |
| 48 | CstValUnitCombinationsPEOInvOrgCode | INV_ORG_CODE | — | ✅ |
| 49 | CstValUnitCombinationsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 50 | CstValUnitCombinationsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 51 | CstValUnitCombinationsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 52 | CstValUnitCombinationsPEOLocatorId | LOCATOR_ID | — | ✅ |
| 53 | CstValUnitCombinationsPEOLotNumber | LOT_NUMBER | — | ✅ |
| 54 | CstValUnitCombinationsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 55 | CstValUnitCombinationsPEOSerialNumber | SERIAL_NUMBER | — | ✅ |
| 56 | CstValUnitCombinationsPEOStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 57 | CstValUnitCombinationsPEOStructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | ✅ |
| 58 | CstValUnitCombinationsPEOSubinventoryCode | SUBINVENTORY_CODE | — | ✅ |
| 59 | CstValUnitCombinationsPEOSummaryFlag | SUMMARY_FLAG | — | ✅ |
| 60 | CstValUnitCombinationsPEOValUnitCombinationId | VAL_UNIT_COMBINATION_ID | 🔑 | ✅ |

### [[cst_val_unit_details|CST_VAL_UNIT_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstValUnitDetailsPEOValUnitDetailId | VAL_UNIT_DETAIL_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
