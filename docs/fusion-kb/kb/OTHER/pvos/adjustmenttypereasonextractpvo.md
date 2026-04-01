---
id: DOC-OTHER-PVO-AdjustmentTypeReasonExtractPVO
doc_type: system-doc
title: "AdjustmentTypeReasonExtractPVO — PVO Cross-Module"
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
  - AdjustmentTypeReasonExtractPVO
  - adjustmenttypereasonextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AdjustmentTypeReasonExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Adjustment Type Reason Extract. Acessa as tabelas: CJM_ADJ_TYPE_REASONS_B.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CjmBiccExtractAM.AdjustmentTypeReasonExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 1 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cjm_adj_type_reasons_b|CJM_ADJ_TYPE_REASONS_B]] — 11 atributos (1 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[cjm_adj_type_reasons_b|CJM_ADJ_TYPE_REASONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdjustmentReasonId | ADJUSTMENT_REASON_ID | 🔑 | ✅ |
| 2 | AdjustmentTypeId | ADJUSTMENT_TYPE_ID | — | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | DefaultFlag | DEFAULT_FLAG | — | ✅ |
| 6 | EnabledFlag | ENABLED_FLAG | — | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | ReasonCode | REASON_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
