---
id: DOC-OTHER-PVO-CostElementExtractPVO
doc_type: system-doc
title: "CostElementExtractPVO — PVO Cross-Module"
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
  - CostElementExtractPVO
  - costelementextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CostElementExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cost Element Extract. Acessa as tabelas: CST_COST_ELEMENTS_B, CST_COST_ELEMENTS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CostElementExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 61 | 2 | 1 | 59 | 97% |

---

## 🔗 Tabelas Relacionadas

- [[cst_cost_elements_b|CST_COST_ELEMENTS_B]] — 51 atributos (1 PKs, 51 BICC)
- [[cst_cost_elements_tl|CST_COST_ELEMENTS_TL]] — 10 atributos (8 BICC)

---

## ⚙️ Atributos

### [[cst_cost_elements_b|CST_COST_ELEMENTS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostElementBPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 2 | CostElementBPEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | ✅ |
| 3 | CostElementBPEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | ✅ |
| 4 | CostElementBPEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | ✅ |
| 5 | CostElementBPEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | ✅ |
| 6 | CostElementBPEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | ✅ |
| 7 | CostElementBPEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | ✅ |
| 8 | CostElementBPEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | ✅ |
| 9 | CostElementBPEOAttributeChar16 | ATTRIBUTE_CHAR16 | — | ✅ |
| 10 | CostElementBPEOAttributeChar17 | ATTRIBUTE_CHAR17 | — | ✅ |
| 11 | CostElementBPEOAttributeChar18 | ATTRIBUTE_CHAR18 | — | ✅ |
| 12 | CostElementBPEOAttributeChar19 | ATTRIBUTE_CHAR19 | — | ✅ |
| 13 | CostElementBPEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | ✅ |
| 14 | CostElementBPEOAttributeChar20 | ATTRIBUTE_CHAR20 | — | ✅ |
| 15 | CostElementBPEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | ✅ |
| 16 | CostElementBPEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | ✅ |
| 17 | CostElementBPEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | ✅ |
| 18 | CostElementBPEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | ✅ |
| 19 | CostElementBPEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | ✅ |
| 20 | CostElementBPEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | ✅ |
| 21 | CostElementBPEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | ✅ |
| 22 | CostElementBPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 23 | CostElementBPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 24 | CostElementBPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 25 | CostElementBPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 26 | CostElementBPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 27 | CostElementBPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 28 | CostElementBPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 29 | CostElementBPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 30 | CostElementBPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 31 | CostElementBPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 32 | CostElementBPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 33 | CostElementBPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 34 | CostElementBPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 35 | CostElementBPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 36 | CostElementBPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 37 | CostElementBPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 38 | CostElementBPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 39 | CostElementBPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 40 | CostElementBPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 41 | CostElementBPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 42 | CostElementBPEOCostElementCode | COST_ELEMENT_CODE | — | ✅ |
| 43 | CostElementBPEOCostElementId | COST_ELEMENT_ID | 🔑 | ✅ |
| 44 | CostElementBPEOCostElementType | COST_ELEMENT_TYPE | — | ✅ |
| 45 | CostElementBPEOCreatedBy | CREATED_BY | — | ✅ |
| 46 | CostElementBPEOCreationDate | CREATION_DATE | — | ✅ |
| 47 | CostElementBPEOInvOrgId | INV_ORG_ID | — | ✅ |
| 48 | CostElementBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 49 | CostElementBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 50 | CostElementBPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 51 | CostElementBPEOSetId | SET_ID | — | ✅ |

### [[cst_cost_elements_tl|CST_COST_ELEMENTS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostElementTLPEOCostElementDesc | COST_ELEMENT_DESC | — | ✅ |
| 2 | CostElementTLPEOCostElementId | COST_ELEMENT_ID | — | ✅ |
| 3 | CostElementTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | CostElementTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | CostElementTLPEOLanguage | LANGUAGE | — | — |
| 6 | CostElementTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | CostElementTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | CostElementTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | CostElementTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | CostElementTLPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
