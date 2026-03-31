---
id: DOC-OTHER-PVO-ValuationStructureTLPVO
doc_type: system-doc
title: "ValuationStructureTLPVO — PVO Cross-Module"
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
  - ValuationStructureTLPVO
  - valuationstructuretlpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ValuationStructureTLPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Valuation Structure TL. Acessa as tabelas: CST_VAL_STRUCTURES_B, CST_VAL_STRUCTURES_TL.

**Caminho:** `FscmTopModelAM.ValuationUnitAM.ValuationStructureTLPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 2 | 2 | 8 | 67% |

---

## 🔗 Tabelas Relacionadas

- [[cst_val_structures_b|CST_VAL_STRUCTURES_B]] — 2 atributos
- [[cst_val_structures_tl|CST_VAL_STRUCTURES_TL]] — 10 atributos (2 PKs, 8 BICC)

---

## ⚙️ Atributos

### [[cst_val_structures_b|CST_VAL_STRUCTURES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ValuationStructureBPEOSetId | SET_ID | — | — |
| 2 | ValuationStructureBPEOValStructureId | VAL_STRUCTURE_ID | — | — |

### [[cst_val_structures_tl|CST_VAL_STRUCTURES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Language | LANGUAGE | 🔑 | ✅ |
| 2 | ValStructureId | VAL_STRUCTURE_ID | 🔑 | ✅ |
| 3 | ValuationStructureTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | ValuationStructureTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | ValuationStructureTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ValuationStructureTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | ValuationStructureTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ValuationStructureTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | ValuationStructureTLPEOSourceLang | SOURCE_LANG | — | ✅ |
| 10 | ValuationStructureTLPEOValStructureDesc | VAL_STRUCTURE_DESC | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
