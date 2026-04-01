---
id: DOC-OTHER-PVO-AdjustmentTypeExtractPVO
doc_type: system-doc
title: "AdjustmentTypeExtractPVO — PVO Cross-Module"
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
  - AdjustmentTypeExtractPVO
  - adjustmenttypeextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AdjustmentTypeExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Adjustment Type Extract. Acessa as tabelas: CJM_ADJUSTMENT_TYPES_B.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CjmBiccExtractAM.AdjustmentTypeExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 1 | 14 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cjm_adjustment_types_b|CJM_ADJUSTMENT_TYPES_B]] — 14 atributos (1 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[cjm_adjustment_types_b|CJM_ADJUSTMENT_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdjustmentNumberPrefix | ADJUSTMENT_NUMBER_PREFIX | — | ✅ |
| 2 | AdjustmentTypeCode | ADJUSTMENT_TYPE_CODE | — | ✅ |
| 3 | AdjustmentTypeId | ADJUSTMENT_TYPE_ID | 🔑 | ✅ |
| 4 | AdjustmentTypeUniqueCode | ADJUSTMENT_TYPE_UNIQUE_CODE | — | ✅ |
| 5 | BuySideFlag | BUY_SIDE_FLAG | — | ✅ |
| 6 | CreatedBy | CREATED_BY | — | ✅ |
| 7 | CreationDate | CREATION_DATE | — | ✅ |
| 8 | EndDate | END_DATE | — | ✅ |
| 9 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | SetId | SET_ID | — | ✅ |
| 14 | StartDate | START_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
