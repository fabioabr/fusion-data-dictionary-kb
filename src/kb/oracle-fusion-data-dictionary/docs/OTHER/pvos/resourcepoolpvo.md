---
id: DOC-OTHER-PVO-ResourcePoolPVO
doc_type: system-doc
title: "ResourcePoolPVO — PVO Cross-Module"
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
  - ResourcePoolPVO
  - resourcepoolpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ResourcePoolPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Resource Pool. Acessa as tabelas: PJR_RESOURCE_POOLS_B, PJR_RESOURCE_POOLS_TL, PJR_RESOURCE_POOLS_VL (+1).

**Caminho:** `FscmTopModelAM.PjrResourceAM.ResourcePoolPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 30 | 4 | 3 | 14 | 47% |

---

## 🔗 Tabelas Relacionadas

- [[pjr_resource_pools_b|PJR_RESOURCE_POOLS_B]] — 13 atributos (1 PKs, 5 BICC)
- [[pjr_resource_pools_tl|PJR_RESOURCE_POOLS_TL]] — 11 atributos (2 PKs, 5 BICC)
- [[pjr_resource_pools_vl|PJR_RESOURCE_POOLS_VL]] — 4 atributos (3 BICC)
- [[pjt_prj_enterprise_resource_vl|PJT_PRJ_ENTERPRISE_RESOURCE_VL]] — 2 atributos (1 BICC)

---

## ⚙️ Atributos

### [[pjr_resource_pools_b|PJR_RESOURCE_POOLS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PoolId | POOL_ID | 🔑 | ✅ |
| 2 | ResourcePoolBasePEOCreatedBy | CREATED_BY | — | — |
| 3 | ResourcePoolBasePEOCreationDate | CREATION_DATE | — | — |
| 4 | ResourcePoolBasePEOFromDate | FROM_DATE | — | — |
| 5 | ResourcePoolBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ResourcePoolBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | ResourcePoolBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | ResourcePoolBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | ResourcePoolBasePEOParentPoolId | PARENT_POOL_ID | — | ✅ |
| 10 | ResourcePoolBasePEOPoolCode | POOL_CODE | — | ✅ |
| 11 | ResourcePoolBasePEOPoolTypeCode | POOL_TYPE_CODE | — | — |
| 12 | ResourcePoolBasePEOResourceId | RESOURCE_ID | — | ✅ |
| 13 | ResourcePoolBasePEOToDate | TO_DATE | — | — |

### [[pjr_resource_pools_tl|PJR_RESOURCE_POOLS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ResourcePoolTLPEOCreatedBy | CREATED_BY | — | — |
| 2 | ResourcePoolTLPEOCreationDate | CREATION_DATE | — | — |
| 3 | ResourcePoolTLPEODescription | DESCRIPTION | — | ✅ |
| 4 | ResourcePoolTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | ResourcePoolTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ResourcePoolTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | ResourcePoolTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | ResourcePoolTLPEOName | NAME | — | ✅ |
| 9 | ResourcePoolTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | ResourcePoolTLPEOPoolId | POOL_ID | 🔑 | ✅ |
| 11 | ResourcePoolTLPEOSourceLang | SOURCE_LANG | — | — |

### [[pjr_resource_pools_vl|PJR_RESOURCE_POOLS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Description | DESCRIPTION | — | ✅ |
| 2 | ParentName | NAME | — | ✅ |
| 3 | ParentPoolId | POOL_ID | — | — |
| 4 | PoolCode | POOL_CODE | — | ✅ |

### [[pjt_prj_enterprise_resource_vl|PJT_PRJ_ENTERPRISE_RESOURCE_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EnterpriseResourcePEODisplayName | DISPLAY_NAME | — | ✅ |
| 2 | EnterpriseResourcePEOResourceId | RESOURCE_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
