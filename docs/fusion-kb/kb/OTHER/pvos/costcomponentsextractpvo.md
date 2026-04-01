---
id: DOC-OTHER-PVO-CostComponentsExtractPVO
doc_type: system-doc
title: "CostComponentsExtractPVO — PVO Cross-Module"
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
  - CostComponentsExtractPVO
  - costcomponentsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CostComponentsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cost Components Extract. Acessa as tabelas: CST_COST_COMPONENTS_B, CST_COST_COMPONENTS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CostComponentsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 66 | 2 | 1 | 20 | 30% |

---

## 🔗 Tabelas Relacionadas

- [[cst_cost_components_b|CST_COST_COMPONENTS_B]] — 55 atributos (1 PKs, 13 BICC)
- [[cst_cost_components_tl|CST_COST_COMPONENTS_TL]] — 11 atributos (7 BICC)

---

## ⚙️ Atributos

### [[cst_cost_components_b|CST_COST_COMPONENTS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostComponentsBPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 2 | CostComponentsBPEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 3 | CostComponentsBPEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 4 | CostComponentsBPEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 5 | CostComponentsBPEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 6 | CostComponentsBPEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 7 | CostComponentsBPEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 8 | CostComponentsBPEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 9 | CostComponentsBPEOAttributeChar16 | ATTRIBUTE_CHAR16 | — | — |
| 10 | CostComponentsBPEOAttributeChar17 | ATTRIBUTE_CHAR17 | — | — |
| 11 | CostComponentsBPEOAttributeChar18 | ATTRIBUTE_CHAR18 | — | — |
| 12 | CostComponentsBPEOAttributeChar19 | ATTRIBUTE_CHAR19 | — | — |
| 13 | CostComponentsBPEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 14 | CostComponentsBPEOAttributeChar20 | ATTRIBUTE_CHAR20 | — | — |
| 15 | CostComponentsBPEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 16 | CostComponentsBPEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 17 | CostComponentsBPEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 18 | CostComponentsBPEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 19 | CostComponentsBPEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 20 | CostComponentsBPEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 21 | CostComponentsBPEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 22 | CostComponentsBPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 23 | CostComponentsBPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 24 | CostComponentsBPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 25 | CostComponentsBPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 26 | CostComponentsBPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 27 | CostComponentsBPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 28 | CostComponentsBPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 29 | CostComponentsBPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 30 | CostComponentsBPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 31 | CostComponentsBPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 32 | CostComponentsBPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 33 | CostComponentsBPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 34 | CostComponentsBPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 35 | CostComponentsBPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 36 | CostComponentsBPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 37 | CostComponentsBPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 38 | CostComponentsBPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 39 | CostComponentsBPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 40 | CostComponentsBPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 41 | CostComponentsBPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 42 | CostComponentsBPEOCostComponentCode | COST_COMPONENT_CODE | — | ✅ |
| 43 | CostComponentsBPEOCostComponentId | COST_COMPONENT_ID | 🔑 | ✅ |
| 44 | CostComponentsBPEOCostComponentType | COST_COMPONENT_TYPE | — | ✅ |
| 45 | CostComponentsBPEOCreatedBy | CREATED_BY | — | ✅ |
| 46 | CostComponentsBPEOCreationDate | CREATION_DATE | — | ✅ |
| 47 | CostComponentsBPEOExpensePoolId | EXPENSE_POOL_ID | — | ✅ |
| 48 | CostComponentsBPEOInactiveFlag | INACTIVE_FLAG | — | ✅ |
| 49 | CostComponentsBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 50 | CostComponentsBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 51 | CostComponentsBPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 52 | CostComponentsBPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 53 | CostComponentsBPEOSetId | SET_ID | — | ✅ |
| 54 | CostComponentsBPEOSourceCode | SOURCE_CODE | — | ✅ |
| 55 | CostComponentsBPEOSourceRefId | SOURCE_REF_ID | — | ✅ |

### [[cst_cost_components_tl|CST_COST_COMPONENTS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostComponentTLPEOCostComponentId | COST_COMPONENT_ID | — | — |
| 2 | CostComponentTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | CostComponentTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | CostComponentTLPEODescription | DESCRIPTION | — | ✅ |
| 5 | CostComponentTLPEOLanguage | LANGUAGE | — | — |
| 6 | CostComponentTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | CostComponentTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | CostComponentTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | CostComponentTLPEOName | NAME | — | ✅ |
| 10 | CostComponentTLPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 11 | CostComponentTLPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
