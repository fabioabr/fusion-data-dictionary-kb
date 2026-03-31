---
id: DOC-OTHER-PVO-VcsMeasureDefinitionTranslationsExtractPVO
doc_type: system-doc
title: "VcsMeasureDefinitionTranslationsExtractPVO — PVO Cross-Module"
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
  - VcsMeasureDefinitionTranslationsExtractPVO
  - vcsmeasuredefinitiontranslationsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# VcsMeasureDefinitionTranslationsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Vcs Measure Definition Translations Extract. Acessa as tabelas: VCS_MEASURE_DEFINITIONS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.VcsDemandBiccExtractAM.VcsMeasureDefinitionTranslationsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[vcs_measure_definitions_tl|VCS_MEASURE_DEFINITIONS_TL]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[vcs_measure_definitions_tl|VCS_MEASURE_DEFINITIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DCMeasureDefinitionTranslationsPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | DCMeasureDefinitionTranslationsPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | DCMeasureDefinitionTranslationsPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 4 | DCMeasureDefinitionTranslationsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | DCMeasureDefinitionTranslationsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 6 | DCMeasureDefinitionTranslationsPEOMeasureId | MEASURE_ID | 🔑 | ✅ |
| 7 | DCMeasureDefinitionTranslationsPEOName | NAME | — | ✅ |
| 8 | DCMeasureDefinitionTranslationsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | DCMeasureDefinitionTranslationsPEOPreviousCycleName | PREVIOUS_CYCLE_NAME | — | ✅ |
| 10 | DCMeasureDefinitionTranslationsPEOSourceLanguage | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
