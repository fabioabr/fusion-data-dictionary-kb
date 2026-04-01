---
id: DOC-OTHER-PVO-CstAnalysisCodesTLExtractPVO
doc_type: system-doc
title: "CstAnalysisCodesTLExtractPVO — PVO Cross-Module"
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
  - CstAnalysisCodesTLExtractPVO
  - cstanalysiscodestlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstAnalysisCodesTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Analysis Codes TLExtract. Acessa as tabelas: CST_ANALYSIS_CODES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstAnalysisCodesTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 2 | 9 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_analysis_codes_tl|CST_ANALYSIS_CODES_TL]] — 9 atributos (2 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[cst_analysis_codes_tl|CST_ANALYSIS_CODES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AnalysisCodesTLPEOAnalysisDesc | ANALYSIS_DESC | — | ✅ |
| 2 | AnalysisCodesTLPEOAnalysisId | ANALYSIS_ID | 🔑 | ✅ |
| 3 | AnalysisCodesTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | AnalysisCodesTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | AnalysisCodesTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | AnalysisCodesTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | AnalysisCodesTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | AnalysisCodesTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | AnalysisCodesTLPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
