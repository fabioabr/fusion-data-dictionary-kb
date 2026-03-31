---
id: DOC-OTHER-PVO-PlantShiftExceptionTranslationExtractPVO
doc_type: system-doc
title: "PlantShiftExceptionTranslationExtractPVO — PVO Cross-Module"
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
  - PlantShiftExceptionTranslationExtractPVO
  - plantshiftexceptiontranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PlantShiftExceptionTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Plant Shift Exception Translation Extract. Acessa as tabelas: RCS_PLANT_SHIFT_EXC_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.ScmRcsBiccExtractAM.PlantShiftExceptionTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[rcs_plant_shift_exc_tl|RCS_PLANT_SHIFT_EXC_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[rcs_plant_shift_exc_tl|RCS_PLANT_SHIFT_EXC_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | Language | LANGUAGE | 🔑 | ✅ |
| 4 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | Name | NAME | — | ✅ |
| 8 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | PlantShiftExcId | PLANT_SHIFT_EXC_ID | 🔑 | ✅ |
| 10 | Reason | REASON | — | ✅ |
| 11 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
