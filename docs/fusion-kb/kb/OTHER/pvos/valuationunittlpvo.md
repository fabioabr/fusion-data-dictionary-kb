---
id: DOC-OTHER-PVO-ValuationUnitTLPVO
doc_type: system-doc
title: "ValuationUnitTLPVO — PVO Cross-Module"
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
  - ValuationUnitTLPVO
  - valuationunittlpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ValuationUnitTLPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Valuation Unit TL. Acessa as tabelas: CST_VAL_UNITS_B, CST_VAL_UNITS_TL.

**Caminho:** `FscmTopModelAM.ValuationUnitAM.ValuationUnitTLPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 2 | 2 | 8 | 67% |

---

## 🔗 Tabelas Relacionadas

- [[cst_val_units_b|CST_VAL_UNITS_B]] — 2 atributos
- [[cst_val_units_tl|CST_VAL_UNITS_TL]] — 10 atributos (2 PKs, 8 BICC)

---

## ⚙️ Atributos

### [[cst_val_units_b|CST_VAL_UNITS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ValuationUnitBPEOCostOrgId | COST_ORG_ID | — | — |
| 2 | ValuationUnitBPEOValUnitId | VAL_UNIT_ID | — | — |

### [[cst_val_units_tl|CST_VAL_UNITS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Language | LANGUAGE | 🔑 | ✅ |
| 2 | ValUnitId | VAL_UNIT_ID | 🔑 | ✅ |
| 3 | ValuationUnitTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | ValuationUnitTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | ValuationUnitTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ValuationUnitTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | ValuationUnitTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ValuationUnitTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | ValuationUnitTLPEOSourceLang | SOURCE_LANG | — | ✅ |
| 10 | ValuationUnitTLPEOValUnitDesc | VAL_UNIT_DESC | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
