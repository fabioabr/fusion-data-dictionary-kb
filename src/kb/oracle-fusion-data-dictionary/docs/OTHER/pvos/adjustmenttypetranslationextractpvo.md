---
id: DOC-OTHER-PVO-AdjustmentTypeTranslationExtractPVO
doc_type: system-doc
title: "AdjustmentTypeTranslationExtractPVO — PVO Cross-Module"
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
  - AdjustmentTypeTranslationExtractPVO
  - adjustmenttypetranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AdjustmentTypeTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Adjustment Type Translation Extract. Acessa as tabelas: CJM_ADJUSTMENT_TYPES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CjmBiccExtractAM.AdjustmentTypeTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cjm_adjustment_types_tl|CJM_ADJUSTMENT_TYPES_TL]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[cjm_adjustment_types_tl|CJM_ADJUSTMENT_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdjustmentTypeId | ADJUSTMENT_TYPE_ID | 🔑 | ✅ |
| 2 | AdjustmentTypeName | ADJUSTMENT_TYPE_NAME | — | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | Description | DESCRIPTION | — | ✅ |
| 6 | Language | LANGUAGE | 🔑 | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
