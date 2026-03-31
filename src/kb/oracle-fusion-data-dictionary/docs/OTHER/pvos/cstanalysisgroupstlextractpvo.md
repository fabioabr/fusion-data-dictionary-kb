---
id: DOC-OTHER-PVO-CstAnalysisGroupsTLExtractPVO
doc_type: system-doc
title: "CstAnalysisGroupsTLExtractPVO — PVO Cross-Module"
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
  - CstAnalysisGroupsTLExtractPVO
  - cstanalysisgroupstlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstAnalysisGroupsTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Analysis Groups TLExtract. Acessa as tabelas: CST_ANALYSIS_GROUPS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstAnalysisGroupsTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 2 | 9 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_analysis_groups_tl|CST_ANALYSIS_GROUPS_TL]] — 9 atributos (2 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[cst_analysis_groups_tl|CST_ANALYSIS_GROUPS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AnalysisGroupsTLPEOAnalysisGroupDesc | ANALYSIS_GROUP_DESC | — | ✅ |
| 2 | AnalysisGroupsTLPEOAnalysisGroupId | ANALYSIS_GROUP_ID | 🔑 | ✅ |
| 3 | AnalysisGroupsTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | AnalysisGroupsTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | AnalysisGroupsTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | AnalysisGroupsTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | AnalysisGroupsTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | AnalysisGroupsTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | AnalysisGroupsTLPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
