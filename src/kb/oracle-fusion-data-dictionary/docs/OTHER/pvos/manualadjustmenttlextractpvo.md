---
id: DOC-OTHER-PVO-ManualAdjustmentTLExtractPVO
doc_type: system-doc
title: "ManualAdjustmentTLExtractPVO — PVO Cross-Module"
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
  - ManualAdjustmentTLExtractPVO
  - manualadjustmenttlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ManualAdjustmentTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Manual Adjustment TLExtract. Acessa as tabelas: CJM_MANUAL_ADJUSTMENTS_ALL_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CjmBiccExtractAM.ManualAdjustmentTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 2 | 9 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cjm_manual_adjustments_all_tl|CJM_MANUAL_ADJUSTMENTS_ALL_TL]] — 9 atributos (2 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[cjm_manual_adjustments_all_tl|CJM_MANUAL_ADJUSTMENTS_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdjustmentComments | ADJUSTMENT_COMMENTS | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | Language | LANGUAGE | 🔑 | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ManualAdjustmentId | MANUAL_ADJUSTMENT_ID | 🔑 | ✅ |
| 9 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
