---
id: DOC-OTHER-PVO-ProjectExtractPVO
doc_type: system-doc
title: "ProjectExtractPVO — PVO Cross-Module"
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
  - ProjectExtractPVO
  - projectextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Extract. Acessa as tabelas: DOO_PROJECTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DooBiccExtractAM.ProjectExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 1 | 1 | 22 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[doo_projects|DOO_PROJECTS]] — 22 atributos (1 PKs, 22 BICC)

---

## ⚙️ Atributos

### [[doo_projects|DOO_PROJECTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectCreatedBy | CREATED_BY | — | ✅ |
| 2 | ProjectCreationDate | CREATION_DATE | — | ✅ |
| 3 | ProjectDooOrderPrjId | DOO_ORDER_PRJ_ID | 🔑 | ✅ |
| 4 | ProjectLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ProjectLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | ProjectLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | ProjectModifiedFlag | MODIFIED_FLAG | — | ✅ |
| 8 | ProjectObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | ProjectPJC_BILLABLE_FLAG | PJC_BILLABLE_FLAG | — | ✅ |
| 10 | ProjectPJC_CAPITALIZABLE_FLAG | PJC_CAPITALIZABLE_FLAG | — | ✅ |
| 11 | ProjectPJC_CONTEXT_CATEGORY | PJC_CONTEXT_CATEGORY | — | ✅ |
| 12 | ProjectPJC_CONTRACT_ID | PJC_CONTRACT_ID | — | ✅ |
| 13 | ProjectPJC_EXPENDITURE_ITEM_DATE | PJC_EXPENDITURE_ITEM_DATE | — | ✅ |
| 14 | ProjectPJC_EXPENDITURE_TYPE_ID | PJC_EXPENDITURE_TYPE_ID | — | ✅ |
| 15 | ProjectPJC_FUNDING_ALLOCATION_ID | PJC_FUNDING_ALLOCATION_ID | — | ✅ |
| 16 | ProjectPJC_ORGANIZATION_ID | PJC_ORGANIZATION_ID | — | ✅ |
| 17 | ProjectPJC_PROJECT_ID | PJC_PROJECT_ID | — | ✅ |
| 18 | ProjectPJC_TASK_ID | PJC_TASK_ID | — | ✅ |
| 19 | ProjectPJC_WORK_TYPE_ID | PJC_WORK_TYPE_ID | — | ✅ |
| 20 | ProjectParentEntityCode | PARENT_ENTITY_CODE | — | ✅ |
| 21 | ProjectParentEntityId | PARENT_ENTITY_ID | — | ✅ |
| 22 | ProjectRefDooOrderPrjId | REF_DOO_ORDER_PRJ_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
