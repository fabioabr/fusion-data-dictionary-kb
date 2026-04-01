---
id: DOC-OTHER-PVO-CostAnalysisGroupPVO
doc_type: system-doc
title: "CostAnalysisGroupPVO — PVO Cross-Module"
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
  - CostAnalysisGroupPVO
  - costanalysisgrouppvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CostAnalysisGroupPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cost Analysis Group. Acessa as tabelas: CST_ANALYSIS_CODES_B, CST_ANALYSIS_CODES_TL, CST_ANALYSIS_GROUPS_B (+4).

**Caminho:** `FscmTopModelAM.CostAnalysisGroupAM.CostAnalysisGroupPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 73 | 7 | 1 | 8 | 11% |

---

## 🔗 Tabelas Relacionadas

- [[cst_analysis_codes_b|CST_ANALYSIS_CODES_B]] — 11 atributos (2 BICC)
- [[cst_analysis_codes_tl|CST_ANALYSIS_CODES_TL]] — 10 atributos (1 BICC)
- [[cst_analysis_groups_b|CST_ANALYSIS_GROUPS_B]] — 9 atributos (1 BICC)
- [[cst_analysis_groups_tl|CST_ANALYSIS_GROUPS_TL]] — 10 atributos (1 BICC)
- [[cst_cost_elements_b|CST_COST_ELEMENTS_B]] — 12 atributos (1 PKs, 2 BICC)
- [[cst_cost_elements_tl|CST_COST_ELEMENTS_TL]] — 10 atributos (1 BICC)
- [[cst_element_analysis_groups|CST_ELEMENT_ANALYSIS_GROUPS]] — 11 atributos

---

## ⚙️ Atributos

### [[cst_analysis_codes_b|CST_ANALYSIS_CODES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AnalysisCodeBEOAnalysisCode | ANALYSIS_CODE | — | ✅ |
| 2 | AnalysisCodeBEOAnalysisGroupId | ANALYSIS_GROUP_ID | — | — |
| 3 | AnalysisCodeBEOAnalysisId | ANALYSIS_ID | — | ✅ |
| 4 | AnalysisCodeBEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 5 | AnalysisCodeBEOCreatedBy | CREATED_BY | — | — |
| 6 | AnalysisCodeBEOCreationDate | CREATION_DATE | — | — |
| 7 | AnalysisCodeBEODefaultAnalysisCodeFlag | DEFAULT_ANALYSIS_CODE_FLAG | — | — |
| 8 | AnalysisCodeBEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 9 | AnalysisCodeBEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | AnalysisCodeBEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | AnalysisCodeBEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[cst_analysis_codes_tl|CST_ANALYSIS_CODES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AnalysisCodeTLEOAnalysisDesc | ANALYSIS_DESC | — | ✅ |
| 2 | AnalysisCodeTLEOAnalysisId | ANALYSIS_ID | — | — |
| 3 | AnalysisCodeTLEOCreatedBy | CREATED_BY | — | — |
| 4 | AnalysisCodeTLEOCreationDate | CREATION_DATE | — | — |
| 5 | AnalysisCodeTLEOLanguage | LANGUAGE | — | — |
| 6 | AnalysisCodeTLEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | AnalysisCodeTLEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | AnalysisCodeTLEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | AnalysisCodeTLEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | AnalysisCodeTLEOSourceLang | SOURCE_LANG | — | — |

### [[cst_analysis_groups_b|CST_ANALYSIS_GROUPS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AnalysisGroupBEOAnalysisGroupCode | ANALYSIS_GROUP_CODE | — | — |
| 2 | AnalysisGroupBEOAnalysisGroupId | ANALYSIS_GROUP_ID | — | ✅ |
| 3 | AnalysisGroupBEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 4 | AnalysisGroupBEOCreatedBy | CREATED_BY | — | — |
| 5 | AnalysisGroupBEOCreationDate | CREATION_DATE | — | — |
| 6 | AnalysisGroupBEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | AnalysisGroupBEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | AnalysisGroupBEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | AnalysisGroupBEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[cst_analysis_groups_tl|CST_ANALYSIS_GROUPS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AnalysisGroupTLEOAnalysisGroupDesc | ANALYSIS_GROUP_DESC | — | ✅ |
| 2 | AnalysisGroupTLEOAnalysisGroupId | ANALYSIS_GROUP_ID | — | — |
| 3 | AnalysisGroupTLEOCreatedBy | CREATED_BY | — | — |
| 4 | AnalysisGroupTLEOCreationDate | CREATION_DATE | — | — |
| 5 | AnalysisGroupTLEOLanguage | LANGUAGE | — | — |
| 6 | AnalysisGroupTLEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | AnalysisGroupTLEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | AnalysisGroupTLEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | AnalysisGroupTLEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | AnalysisGroupTLEOSourceLang | SOURCE_LANG | — | — |

### [[cst_cost_elements_b|CST_COST_ELEMENTS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostElementBEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 2 | CostElementBEOCostElementCode | COST_ELEMENT_CODE | — | — |
| 3 | CostElementBEOCostElementType | COST_ELEMENT_TYPE | — | — |
| 4 | CostElementBEOCreatedBy | CREATED_BY | — | — |
| 5 | CostElementBEOCreationDate | CREATION_DATE | — | — |
| 6 | CostElementBEOInvOrgId | INV_ORG_ID | — | — |
| 7 | CostElementBEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | CostElementBEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | CostElementBEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | CostElementBEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | CostElementBEOSetId | SET_ID | — | — |
| 12 | CostElementId | COST_ELEMENT_ID | 🔑 | ✅ |

### [[cst_cost_elements_tl|CST_COST_ELEMENTS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostElementTLCostElementDesc | COST_ELEMENT_DESC | — | ✅ |
| 2 | CostElementTLCostElementId | COST_ELEMENT_ID | — | — |
| 3 | CostElementTLCreatedBy | CREATED_BY | — | — |
| 4 | CostElementTLCreationDate | CREATION_DATE | — | — |
| 5 | CostElementTLLanguage | LANGUAGE | — | — |
| 6 | CostElementTLLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | CostElementTLLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | CostElementTLLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | CostElementTLObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | CostElementTLSourceLang | SOURCE_LANG | — | — |

### [[cst_element_analysis_groups|CST_ELEMENT_ANALYSIS_GROUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ElementAnalysisGroupEOAnalysisGroupId | ANALYSIS_GROUP_ID | — | — |
| 2 | ElementAnalysisGroupEOAnalysisId | ANALYSIS_ID | — | — |
| 3 | ElementAnalysisGroupEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 4 | ElementAnalysisGroupEOCostElementId | COST_ELEMENT_ID | — | — |
| 5 | ElementAnalysisGroupEOCreatedBy | CREATED_BY | — | — |
| 6 | ElementAnalysisGroupEOCreationDate | CREATION_DATE | — | — |
| 7 | ElementAnalysisGroupEOElementAnalysisGroupId | ELEMENT_ANALYSIS_GROUP_ID | — | — |
| 8 | ElementAnalysisGroupEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 9 | ElementAnalysisGroupEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | ElementAnalysisGroupEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | ElementAnalysisGroupEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
