---
id: DOC-OTHER-PVO-StructureNamesTranslationExtractPVO
doc_type: system-doc
title: "StructureNamesTranslationExtractPVO — PVO Cross-Module"
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
  - StructureNamesTranslationExtractPVO
  - structurenamestranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# StructureNamesTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Structure Names Translation Extract. Acessa as tabelas: EGP_STRUCTURE_NAMES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.EgpBiccExtractAM.StructureNamesTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 2 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[egp_structure_names_tl|EGP_STRUCTURE_NAMES_TL]] — 12 atributos (2 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[egp_structure_names_tl|EGP_STRUCTURE_NAMES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | StructureNamesTranslationPEOAlternateDesignatorId | ALTERNATE_DESIGNATOR_ID | 🔑 | ✅ |
| 2 | StructureNamesTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | StructureNamesTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | StructureNamesTranslationPEODescription | DESCRIPTION | — | ✅ |
| 5 | StructureNamesTranslationPEODisplayName | DISPLAY_NAME | — | ✅ |
| 6 | StructureNamesTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 7 | StructureNamesTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | StructureNamesTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | StructureNamesTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | StructureNamesTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | StructureNamesTranslationPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 12 | StructureNamesTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
