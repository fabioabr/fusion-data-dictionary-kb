---
id: DOC-OTHER-PVO-TaskFollowerPVO
doc_type: system-doc
title: "TaskFollowerPVO — PVO Cross-Module"
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
  - TaskFollowerPVO
  - taskfollowerpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TaskFollowerPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Task Follower. Acessa as tabelas: PJF_PROJ_ELEMENT_VERSION, PJT_PRJ_ENTERPRISE_RESOURCE_B, PJT_PRJ_ENTERPRISE_RESOURCE_TL (+1).

**Caminho:** `FscmTopModelAM.PjlTaskManagementAM.TaskFollowerPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 19 | 4 | 5 | 9 | 47% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_proj_element_version|PJF_PROJ_ELEMENT_VERSION]] — 2 atributos (1 PKs, 1 BICC)
- [[pjt_prj_enterprise_resource_b|PJT_PRJ_ENTERPRISE_RESOURCE_B]] — 3 atributos (1 BICC)
- [[pjt_prj_enterprise_resource_tl|PJT_PRJ_ENTERPRISE_RESOURCE_TL]] — 4 atributos (2 PKs, 3 BICC)
- [[pjt_task_followers|PJT_TASK_FOLLOWERS]] — 10 atributos (2 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[pjf_proj_element_version|PJF_PROJ_ELEMENT_VERSION]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ElementVersionId | ELEMENT_VERSION_ID | 🔑 | ✅ |
| 2 | PjtProjElementVersionPEOObjectType | OBJECT_TYPE | — | — |

### [[pjt_prj_enterprise_resource_b|PJT_PRJ_ENTERPRISE_RESOURCE_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PrjEnterpriseResourceBasePEOEmail | EMAIL | — | ✅ |
| 2 | PrjEnterpriseResourceBasePEOResourceClass | RESOURCE_CLASS | — | — |
| 3 | PrjEnterpriseResourceBasePEOResourceId | RESOURCE_ID | — | — |

### [[pjt_prj_enterprise_resource_tl|PJT_PRJ_ENTERPRISE_RESOURCE_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Language | LANGUAGE | 🔑 | ✅ |
| 2 | PrjEnterpriseResourceTransla1Description | DESCRIPTION | — | — |
| 3 | PrjEnterpriseResourceTransla1DisplayName | DISPLAY_NAME | — | ✅ |
| 4 | ResourceId | RESOURCE_ID | 🔑 | ✅ |

### [[pjt_task_followers|PJT_TASK_FOLLOWERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EnterpriseId | ENTERPRISE_ID | 🔑 | ✅ |
| 2 | TaskFollowerId | TASK_FOLLOWER_ID | 🔑 | ✅ |
| 3 | TaskFollowerPEOCreatedBy | CREATED_BY | — | — |
| 4 | TaskFollowerPEOCreationDate | CREATION_DATE | — | — |
| 5 | TaskFollowerPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | TaskFollowerPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | TaskFollowerPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | TaskFollowerPEOLastViewedDate | LAST_VIEWED_DATE | — | — |
| 9 | TaskFollowerPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | TaskFollowerPEOResourceId | RESOURCE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
