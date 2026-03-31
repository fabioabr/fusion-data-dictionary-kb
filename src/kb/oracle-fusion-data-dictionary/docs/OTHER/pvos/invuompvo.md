---
id: DOC-OTHER-PVO-InvUomPVO
doc_type: system-doc
title: "InvUomPVO — PVO Cross-Module"
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
  - InvUomPVO
  - invuompvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InvUomPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Inv Uom. Acessa as tabelas: INV_UNITS_OF_MEASURE_B, INV_UNITS_OF_MEASURE_TL.

**Caminho:** `FscmTopModelAM.InvUomPublicViewAM.InvUomPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 26 | 2 | 2 | 11 | 42% |

---

## 🔗 Tabelas Relacionadas

- [[inv_units_of_measure_b|INV_UNITS_OF_MEASURE_B]] — 15 atributos (1 PKs, 5 BICC)
- [[inv_units_of_measure_tl|INV_UNITS_OF_MEASURE_TL]] — 11 atributos (1 PKs, 6 BICC)

---

## ⚙️ Atributos

### [[inv_units_of_measure_b|INV_UNITS_OF_MEASURE_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvUomBPEOBaseUomFlag | BASE_UOM_FLAG | — | ✅ |
| 2 | InvUomBPEOCreatedBy | CREATED_BY | — | — |
| 3 | InvUomBPEOCreationDate | CREATION_DATE | — | — |
| 4 | InvUomBPEODisableDate | DISABLE_DATE | — | — |
| 5 | InvUomBPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 6 | InvUomBPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 7 | InvUomBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | InvUomBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | InvUomBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | InvUomBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | InvUomBPEORequestId | REQUEST_ID | — | — |
| 12 | InvUomBPEOStandardPackFlag | STANDARD_PACK_FLAG | — | — |
| 13 | InvUomBPEOUomClass | UOM_CLASS | — | ✅ |
| 14 | InvUomBPEOUomCode | UOM_CODE | 🔑 | ✅ |
| 15 | UnitOfMeasureId | UNIT_OF_MEASURE_ID | — | ✅ |

### [[inv_units_of_measure_tl|INV_UNITS_OF_MEASURE_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvUomTLPEOCreatedBy | CREATED_BY | — | — |
| 2 | InvUomTLPEOCreationDate | CREATION_DATE | — | — |
| 3 | InvUomTLPEODescription | DESCRIPTION | — | ✅ |
| 4 | InvUomTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | InvUomTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | InvUomTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | InvUomTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | InvUomTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | InvUomTLPEOSourceLang | SOURCE_LANG | — | ✅ |
| 10 | InvUomTLPEOUnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |
| 11 | InvUomTLPEOUnitOfMeasureId | UNIT_OF_MEASURE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
