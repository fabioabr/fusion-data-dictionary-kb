---
id: DOC-OTHER-PVO-InvUnitsOfMeasurePVO
doc_type: system-doc
title: "InvUnitsOfMeasurePVO — PVO Cross-Module"
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
  - InvUnitsOfMeasurePVO
  - invunitsofmeasurepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InvUnitsOfMeasurePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Inv Units Of Measure. Acessa as tabelas: INV_UNITS_OF_MEASURE_B.

**Caminho:** `FscmTopModelAM.ScmExtractAM.ScmRcsBiccExtractAM.InvUnitsOfMeasurePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 30 | 1 | 1 | 14 | 47% |

---

## 🔗 Tabelas Relacionadas

- [[inv_units_of_measure_b|INV_UNITS_OF_MEASURE_B]] — 30 atributos (1 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[inv_units_of_measure_b|INV_UNITS_OF_MEASURE_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Attribute1 | ATTRIBUTE1 | — | — |
| 2 | Attribute10 | ATTRIBUTE10 | — | — |
| 3 | Attribute11 | ATTRIBUTE11 | — | — |
| 4 | Attribute12 | ATTRIBUTE12 | — | — |
| 5 | Attribute13 | ATTRIBUTE13 | — | — |
| 6 | Attribute14 | ATTRIBUTE14 | — | — |
| 7 | Attribute15 | ATTRIBUTE15 | — | — |
| 8 | Attribute2 | ATTRIBUTE2 | — | — |
| 9 | Attribute3 | ATTRIBUTE3 | — | — |
| 10 | Attribute4 | ATTRIBUTE4 | — | — |
| 11 | Attribute5 | ATTRIBUTE5 | — | — |
| 12 | Attribute6 | ATTRIBUTE6 | — | — |
| 13 | Attribute7 | ATTRIBUTE7 | — | — |
| 14 | Attribute8 | ATTRIBUTE8 | — | — |
| 15 | Attribute9 | ATTRIBUTE9 | — | — |
| 16 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 17 | BaseUomFlag | BASE_UOM_FLAG | — | ✅ |
| 18 | CreatedBy | CREATED_BY | — | ✅ |
| 19 | CreationDate | CREATION_DATE | — | ✅ |
| 20 | DisableDate | DISABLE_DATE | — | ✅ |
| 21 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 22 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 23 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 24 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 25 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 26 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 27 | RequestId | REQUEST_ID | — | ✅ |
| 28 | UnitOfMeasureId | UNIT_OF_MEASURE_ID | 🔑 | ✅ |
| 29 | UomClass | UOM_CLASS | — | ✅ |
| 30 | UomCode | UOM_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
