---
id: DOC-OTHER-PVO-QaInspectionLevelsTLExtractPVO
doc_type: system-doc
title: "QaInspectionLevelsTLExtractPVO — PVO Cross-Module"
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
  - QaInspectionLevelsTLExtractPVO
  - qainspectionlevelstlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QaInspectionLevelsTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Qa Inspection Levels TLExtract. Acessa as tabelas: QA_INSPECTION_LEVELS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.QaBiccExtractAM.QaInspectionLevelsTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[qa_inspection_levels_tl|QA_INSPECTION_LEVELS_TL]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[qa_inspection_levels_tl|QA_INSPECTION_LEVELS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InspectionLevelsTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | InspectionLevelsTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | InspectionLevelsTLPEODescription | DESCRIPTION | — | ✅ |
| 4 | InspectionLevelsTLPEOInspectionLevelId | INSPECTION_LEVEL_ID | 🔑 | ✅ |
| 5 | InspectionLevelsTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | InspectionLevelsTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | InspectionLevelsTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | InspectionLevelsTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | InspectionLevelsTLPEOName | NAME | — | ✅ |
| 10 | InspectionLevelsTLPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
