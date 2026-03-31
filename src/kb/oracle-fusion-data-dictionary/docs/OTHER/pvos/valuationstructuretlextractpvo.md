---
id: DOC-OTHER-PVO-ValuationStructureTLExtractPVO
doc_type: system-doc
title: "ValuationStructureTLExtractPVO — PVO Cross-Module"
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
  - ValuationStructureTLExtractPVO
  - valuationstructuretlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ValuationStructureTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Valuation Structure TLExtract. Acessa as tabelas: CST_VAL_STRUCTURES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.ValuationStructureTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_val_structures_tl|CST_VAL_STRUCTURES_TL]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[cst_val_structures_tl|CST_VAL_STRUCTURES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ValuationStructureTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | ValuationStructureTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | ValuationStructureTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 4 | ValuationStructureTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ValuationStructureTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | ValuationStructureTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | ValuationStructureTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | ValuationStructureTLPEOSourceLang | SOURCE_LANG | — | ✅ |
| 9 | ValuationStructureTLPEOValStructureDesc | VAL_STRUCTURE_DESC | — | ✅ |
| 10 | ValuationStructureTLPEOValStructureId | VAL_STRUCTURE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
