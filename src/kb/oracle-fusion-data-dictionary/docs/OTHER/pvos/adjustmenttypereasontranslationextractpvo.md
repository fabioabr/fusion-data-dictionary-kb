---
id: DOC-OTHER-PVO-AdjustmentTypeReasonTranslationExtractPVO
doc_type: system-doc
title: "AdjustmentTypeReasonTranslationExtractPVO — PVO Cross-Module"
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
  - AdjustmentTypeReasonTranslationExtractPVO
  - adjustmenttypereasontranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AdjustmentTypeReasonTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Adjustment Type Reason Translation Extract. Acessa as tabelas: CJM_ADJ_TYPE_REASONS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CjmBiccExtractAM.AdjustmentTypeReasonTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cjm_adj_type_reasons_tl|CJM_ADJ_TYPE_REASONS_TL]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[cjm_adj_type_reasons_tl|CJM_ADJ_TYPE_REASONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdjustmentReasonId | ADJUSTMENT_REASON_ID | 🔑 | ✅ |
| 2 | AdjustmentReasonName | ADJUSTMENT_REASON_NAME | — | ✅ |
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
