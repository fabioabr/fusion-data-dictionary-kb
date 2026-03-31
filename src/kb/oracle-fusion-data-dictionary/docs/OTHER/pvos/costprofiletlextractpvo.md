---
id: DOC-OTHER-PVO-CostProfileTLExtractPVO
doc_type: system-doc
title: "CostProfileTLExtractPVO — PVO Cross-Module"
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
  - CostProfileTLExtractPVO
  - costprofiletlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CostProfileTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cost Profile TLExtract. Acessa as tabelas: CST_COST_PROFILES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CostProfileTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 2 | 9 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_cost_profiles_tl|CST_COST_PROFILES_TL]] — 9 atributos (2 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[cst_cost_profiles_tl|CST_COST_PROFILES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostProfileTLPEOCostProfileDesc | COST_PROFILE_DESC | — | ✅ |
| 2 | CostProfileTLPEOCostProfileId | COST_PROFILE_ID | 🔑 | ✅ |
| 3 | CostProfileTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | CostProfileTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | CostProfileTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | CostProfileTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | CostProfileTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | CostProfileTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | CostProfileTLPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
