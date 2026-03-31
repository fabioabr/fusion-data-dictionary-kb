---
id: DOC-OTHER-PVO-StructureTypesTranslationExtractPVO
doc_type: system-doc
title: "StructureTypesTranslationExtractPVO — PVO Cross-Module"
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
  - StructureTypesTranslationExtractPVO
  - structuretypestranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# StructureTypesTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Structure Types Translation Extract. Acessa as tabelas: EGP_STRUCTURE_TYPES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.EgpBiccExtractAM.StructureTypesTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[egp_structure_types_tl|EGP_STRUCTURE_TYPES_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[egp_structure_types_tl|EGP_STRUCTURE_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | StructureTypesTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | StructureTypesTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | StructureTypesTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | StructureTypesTranslationPEODisplayName | DISPLAY_NAME | — | ✅ |
| 5 | StructureTypesTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | StructureTypesTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | StructureTypesTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | StructureTypesTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | StructureTypesTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | StructureTypesTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |
| 11 | StructureTypesTranslationPEOStructureTypeId | STRUCTURE_TYPE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
