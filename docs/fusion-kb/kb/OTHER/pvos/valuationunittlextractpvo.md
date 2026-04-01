---
id: DOC-OTHER-PVO-ValuationUnitTLExtractPVO
doc_type: system-doc
title: "ValuationUnitTLExtractPVO — PVO Cross-Module"
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
  - ValuationUnitTLExtractPVO
  - valuationunittlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ValuationUnitTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Valuation Unit TLExtract. Acessa as tabelas: CST_VAL_UNITS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.ValuationUnitTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_val_units_tl|CST_VAL_UNITS_TL]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[cst_val_units_tl|CST_VAL_UNITS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ValuationUnitTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | ValuationUnitTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | ValuationUnitTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 4 | ValuationUnitTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ValuationUnitTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | ValuationUnitTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | ValuationUnitTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | ValuationUnitTLPEOSourceLang | SOURCE_LANG | — | ✅ |
| 9 | ValuationUnitTLPEOValUnitDesc | VAL_UNIT_DESC | — | ✅ |
| 10 | ValuationUnitTLPEOValUnitId | VAL_UNIT_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
