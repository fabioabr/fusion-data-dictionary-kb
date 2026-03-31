---
id: DOC-OTHER-PVO-CostElementPVO
doc_type: system-doc
title: "CostElementPVO — PVO Cross-Module"
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
  - CostElementPVO
  - costelementpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CostElementPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cost Element. Acessa as tabelas: CST_COST_ELEMENTS_B, CST_COST_ELEMENTS_TL, FND_SETID_SETS_VL (+1).

**Caminho:** `FscmTopModelAM.CostElementAM.CostElementPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 27 | 4 | 1 | 12 | 44% |

---

## 🔗 Tabelas Relacionadas

- [[cst_cost_elements_b|CST_COST_ELEMENTS_B]] — 12 atributos (1 PKs, 7 BICC)
- [[cst_cost_elements_tl|CST_COST_ELEMENTS_TL]] — 10 atributos (2 BICC)
- [[fnd_setid_sets_vl|FND_SETID_SETS_VL]] — 3 atributos (2 BICC)
- [[inv_org_parameters_v|INV_ORG_PARAMETERS_V]] — 2 atributos (1 BICC)

---

## ⚙️ Atributos

### [[cst_cost_elements_b|CST_COST_ELEMENTS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostElementBEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 2 | CostElementBEOCostElementCode | COST_ELEMENT_CODE | — | ✅ |
| 3 | CostElementBEOCostElementType | COST_ELEMENT_TYPE | — | ✅ |
| 4 | CostElementBEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | CostElementBEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | CostElementBEOInvOrgId | INV_ORG_ID | — | — |
| 7 | CostElementBEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | CostElementBEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | CostElementBEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | CostElementBEOSetId | SET_ID | — | — |
| 11 | CostElementId | COST_ELEMENT_ID | 🔑 | ✅ |
| 12 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |

### [[cst_cost_elements_tl|CST_COST_ELEMENTS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostElementTLEOCostElementDesc | COST_ELEMENT_DESC | — | ✅ |
| 2 | CostElementTLEOCostElementId | COST_ELEMENT_ID | — | — |
| 3 | CostElementTLEOCreatedBy | CREATED_BY | — | — |
| 4 | CostElementTLEOCreationDate | CREATION_DATE | — | — |
| 5 | CostElementTLEOLanguage | LANGUAGE | — | ✅ |
| 6 | CostElementTLEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | CostElementTLEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | CostElementTLEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | CostElementTLEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | CostElementTLEOSourceLang | SOURCE_LANG | — | — |

### [[fnd_setid_sets_vl|FND_SETID_SETS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SetIdSetPEOSetCode | SET_CODE | — | — |
| 2 | SetIdSetPEOSetId | SET_ID | — | ✅ |
| 3 | SetIdSetPEOSetName | SET_NAME | — | ✅ |

### [[inv_org_parameters_v|INV_ORG_PARAMETERS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MtlParametersAllOrganizationCode | ORGANIZATION_CODE | — | — |
| 2 | MtlParametersAllOrganizationId | ORGANIZATION_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
