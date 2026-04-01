---
id: DOC-OTHER-PVO-ContractRuleDetailsPVO
doc_type: system-doc
title: "ContractRuleDetailsPVO — PVO Cross-Module"
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
  - ContractRuleDetailsPVO
  - contractruledetailspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ContractRuleDetailsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Contract Rule Details. Acessa as tabelas: VRM_CONTRACT_RULE_DETAILS, VRM_SOURCE_COLUMNS_B, VRM_SOURCE_COLUMNS_TL (+1).

**Caminho:** `FscmTopModelAM.FinVrmRRSharedPublicModelAM.ContractRuleDetailsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 4 | 1 | 8 | 40% |

---

## 🔗 Tabelas Relacionadas

- [[vrm_contract_rule_details|VRM_CONTRACT_RULE_DETAILS]] — 11 atributos (1 PKs, 6 BICC)
- [[vrm_source_columns_b|VRM_SOURCE_COLUMNS_B]] — 3 atributos
- [[vrm_source_columns_tl|VRM_SOURCE_COLUMNS_TL]] — 3 atributos (1 BICC)
- [[vrm_source_doc_types_tl|VRM_SOURCE_DOC_TYPES_TL]] — 3 atributos (1 BICC)

---

## ⚙️ Atributos

### [[vrm_contract_rule_details|VRM_CONTRACT_RULE_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractRuleDetailsAttributeGroupId | ATTRIBUTE_GROUP_ID | — | ✅ |
| 2 | ContractRuleDetailsContractRuleDetailId | CONTRACT_RULE_DETAIL_ID | 🔑 | ✅ |
| 3 | ContractRuleDetailsContractRuleId | CONTRACT_RULE_ID | — | — |
| 4 | ContractRuleDetailsCopyReferenceFlag | COPY_REFERENCE_FLAG | — | ✅ |
| 5 | ContractRuleDetailsCreatedBy | CREATED_BY | — | — |
| 6 | ContractRuleDetailsCreationDate | CREATION_DATE | — | — |
| 7 | ContractRuleDetailsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ContractRuleDetailsLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ContractRuleDetailsLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ContractRuleDetailsReferencePrefix | REFERENCE_PREFIX | — | ✅ |
| 11 | ContractRuleDetailsUseAsGroupNumberFlag | USE_AS_GROUP_NUMBER_FLAG | — | ✅ |

### [[vrm_source_columns_b|VRM_SOURCE_COLUMNS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | VrmSourceColumnsSourceColumnId | SOURCE_COLUMN_ID | — | — |
| 2 | VrmSourceColumnsTransAttrUserLang | TRANS_ATTR_USER_LANG | — | — |
| 3 | VrmSourceColumnsUsedInContractRuleFlag | USED_IN_CONTRACT_RULE_FLAG | — | — |

### [[vrm_source_columns_tl|VRM_SOURCE_COLUMNS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | VrmSourceColumnsTLDescription | DESCRIPTION | — | ✅ |
| 2 | VrmSourceColumnsTLLanguage | LANGUAGE | — | — |
| 3 | VrmSourceColumnsTLSourceColumnId | SOURCE_COLUMN_ID | — | — |

### [[vrm_source_doc_types_tl|VRM_SOURCE_DOC_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | VrmSourceDocumentTypeDocumentTypeId | DOCUMENT_TYPE_ID | — | — |
| 2 | VrmSourceDocumentTypeLanguage | LANGUAGE | — | — |
| 3 | VrmSourceDocumentTypeName | NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
