---
id: DOC-OTHER-PVO-InvUnitsOfMeasureTranslationPVO
doc_type: system-doc
title: "InvUnitsOfMeasureTranslationPVO — PVO Cross-Module"
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
  - InvUnitsOfMeasureTranslationPVO
  - invunitsofmeasuretranslationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InvUnitsOfMeasureTranslationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Inv Units Of Measure Translation. Acessa as tabelas: INV_UNITS_OF_MEASURE_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.ScmRcsBiccExtractAM.InvUnitsOfMeasureTranslationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[inv_units_of_measure_tl|INV_UNITS_OF_MEASURE_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[inv_units_of_measure_tl|INV_UNITS_OF_MEASURE_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | Description | DESCRIPTION | — | ✅ |
| 4 | Language | LANGUAGE | 🔑 | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | SourceLang | SOURCE_LANG | — | ✅ |
| 10 | UnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |
| 11 | UnitOfMeasureId | UNIT_OF_MEASURE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
