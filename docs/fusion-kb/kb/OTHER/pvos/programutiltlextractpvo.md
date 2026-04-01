---
id: DOC-OTHER-PVO-ProgramUtilTLExtractPVO
doc_type: system-doc
title: "ProgramUtilTLExtractPVO — PVO Cross-Module"
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
  - ProgramUtilTLExtractPVO
  - programutiltlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProgramUtilTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Program Util TLExtract. Acessa as tabelas: CJM_PROGRAMS_UTILIZED_ALL_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CjmBiccExtractAM.ProgramUtilTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 2 | 9 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cjm_programs_utilized_all_tl|CJM_PROGRAMS_UTILIZED_ALL_TL]] — 9 atributos (2 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[cjm_programs_utilized_all_tl|CJM_PROGRAMS_UTILIZED_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdjustmentDesc | ADJUSTMENT_DESC | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | Language | LANGUAGE | 🔑 | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | SourceLang | SOURCE_LANG | — | ✅ |
| 9 | UtilizationId | UTILIZATION_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
