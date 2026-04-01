---
id: DOC-OTHER-PVO-CstAnalysisCodesExtractPVO
doc_type: system-doc
title: "CstAnalysisCodesExtractPVO — PVO Cross-Module"
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
  - CstAnalysisCodesExtractPVO
  - cstanalysiscodesextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstAnalysisCodesExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Analysis Codes Extract. Acessa as tabelas: CST_ANALYSIS_CODES_B, CST_ANALYSIS_CODES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstAnalysisCodesExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 59 | 2 | 1 | 15 | 25% |

---

## 🔗 Tabelas Relacionadas

- [[cst_analysis_codes_b|CST_ANALYSIS_CODES_B]] — 50 atributos (1 PKs, 9 BICC)
- [[cst_analysis_codes_tl|CST_ANALYSIS_CODES_TL]] — 9 atributos (6 BICC)

---

## ⚙️ Atributos

### [[cst_analysis_codes_b|CST_ANALYSIS_CODES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AnalysisCodesBPEOAnalysisCode | ANALYSIS_CODE | — | ✅ |
| 2 | AnalysisCodesBPEOAnalysisGroupId | ANALYSIS_GROUP_ID | — | ✅ |
| 3 | AnalysisCodesBPEOAnalysisId | ANALYSIS_ID | 🔑 | ✅ |
| 4 | AnalysisCodesBPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 5 | AnalysisCodesBPEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 6 | AnalysisCodesBPEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 7 | AnalysisCodesBPEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 8 | AnalysisCodesBPEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 9 | AnalysisCodesBPEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 10 | AnalysisCodesBPEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 11 | AnalysisCodesBPEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 12 | AnalysisCodesBPEOAttributeChar16 | ATTRIBUTE_CHAR16 | — | — |
| 13 | AnalysisCodesBPEOAttributeChar17 | ATTRIBUTE_CHAR17 | — | — |
| 14 | AnalysisCodesBPEOAttributeChar18 | ATTRIBUTE_CHAR18 | — | — |
| 15 | AnalysisCodesBPEOAttributeChar19 | ATTRIBUTE_CHAR19 | — | — |
| 16 | AnalysisCodesBPEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 17 | AnalysisCodesBPEOAttributeChar20 | ATTRIBUTE_CHAR20 | — | — |
| 18 | AnalysisCodesBPEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 19 | AnalysisCodesBPEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 20 | AnalysisCodesBPEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 21 | AnalysisCodesBPEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 22 | AnalysisCodesBPEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 23 | AnalysisCodesBPEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 24 | AnalysisCodesBPEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 25 | AnalysisCodesBPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 26 | AnalysisCodesBPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 27 | AnalysisCodesBPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 28 | AnalysisCodesBPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 29 | AnalysisCodesBPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 30 | AnalysisCodesBPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 31 | AnalysisCodesBPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 32 | AnalysisCodesBPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 33 | AnalysisCodesBPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 34 | AnalysisCodesBPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 35 | AnalysisCodesBPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 36 | AnalysisCodesBPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 37 | AnalysisCodesBPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 38 | AnalysisCodesBPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 39 | AnalysisCodesBPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 40 | AnalysisCodesBPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 41 | AnalysisCodesBPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 42 | AnalysisCodesBPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 43 | AnalysisCodesBPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 44 | AnalysisCodesBPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 45 | AnalysisCodesBPEOCreatedBy | CREATED_BY | — | ✅ |
| 46 | AnalysisCodesBPEOCreationDate | CREATION_DATE | — | ✅ |
| 47 | AnalysisCodesBPEODefaultAnalysisCodeFlag | DEFAULT_ANALYSIS_CODE_FLAG | — | ✅ |
| 48 | AnalysisCodesBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 49 | AnalysisCodesBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 50 | AnalysisCodesBPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |

### [[cst_analysis_codes_tl|CST_ANALYSIS_CODES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AnalysisCodesTLPEOAnalysisDesc | ANALYSIS_DESC | — | ✅ |
| 2 | AnalysisCodesTLPEOAnalysisId | ANALYSIS_ID | — | — |
| 3 | AnalysisCodesTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | AnalysisCodesTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | AnalysisCodesTLPEOLanguage | LANGUAGE | — | — |
| 6 | AnalysisCodesTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | AnalysisCodesTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | AnalysisCodesTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | AnalysisCodesTLPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
