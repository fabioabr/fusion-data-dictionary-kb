---
id: DOC-OTHER-PVO-ObligRuleDetailsPVO
doc_type: system-doc
title: "ObligRuleDetailsPVO — PVO Cross-Module"
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
  - ObligRuleDetailsPVO
  - obligruledetailspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ObligRuleDetailsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Oblig Rule Details. Acessa as tabelas: VRM_PERF_OBLIG_GRP_RULE_DTLS, VRM_SOURCE_COLUMNS_B, VRM_SOURCE_COLUMNS_TL (+1).

**Caminho:** `FscmTopModelAM.FinVrmRRSharedPublicModelAM.ObligRuleDetailsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 4 | 1 | 7 | 35% |

---

## 🔗 Tabelas Relacionadas

- [[vrm_perf_oblig_grp_rule_dtls|VRM_PERF_OBLIG_GRP_RULE_DTLS]] — 11 atributos (1 PKs, 5 BICC)
- [[vrm_source_columns_b|VRM_SOURCE_COLUMNS_B]] — 3 atributos
- [[vrm_source_columns_tl|VRM_SOURCE_COLUMNS_TL]] — 3 atributos (1 BICC)
- [[vrm_source_doc_types_tl|VRM_SOURCE_DOC_TYPES_TL]] — 3 atributos (1 BICC)

---

## ⚙️ Atributos

### [[vrm_perf_oblig_grp_rule_dtls|VRM_PERF_OBLIG_GRP_RULE_DTLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ObligRuleDetailsAttributeGroupId | ATTRIBUTE_GROUP_ID | — | ✅ |
| 2 | ObligRuleDetailsCopyReferenceFlag | COPY_REFERENCE_FLAG | — | ✅ |
| 3 | ObligRuleDetailsCreatedBy | CREATED_BY | — | — |
| 4 | ObligRuleDetailsCreationDate | CREATION_DATE | — | — |
| 5 | ObligRuleDetailsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ObligRuleDetailsLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | ObligRuleDetailsLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | ObligRuleDetailsPerfObligGrpRuleDtlId | PERF_OBLIG_GRP_RULE_DTL_ID | 🔑 | ✅ |
| 9 | ObligRuleDetailsPerfObligationGroupRuleId | PERF_OBLIGATION_GROUP_RULE_ID | — | — |
| 10 | ObligRuleDetailsReferencePrefix | REFERENCE_PREFIX | — | ✅ |
| 11 | ObligRuleDetailsTransAttrObligRuleFlag | TRANS_ATTR_OBLIG_RULE_FLAG | — | — |

### [[vrm_source_columns_b|VRM_SOURCE_COLUMNS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | VrmSourceColumnsSourceColumnId | SOURCE_COLUMN_ID | — | — |
| 2 | VrmSourceColumnsTransAttrUserLang | TRANS_ATTR_USER_LANG | — | — |
| 3 | VrmSourceColumnsUsedInObligRuleFlag | USED_IN_OBLIG_RULE_FLAG | — | — |

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
