---
id: DOC-OTHER-PVO-ProjectExpenditureGroupExtractPVO
doc_type: system-doc
title: "ProjectExpenditureGroupExtractPVO — PVO Cross-Module"
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
  - ProjectExpenditureGroupExtractPVO
  - projectexpendituregroupextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectExpenditureGroupExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Expenditure Group Extract. Acessa as tabelas: PJC_EXP_GROUPS_ALL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjcBiccExtractAM.ProjectExpenditureGroupExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 18 | 1 | 1 | 18 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjc_exp_groups_all|PJC_EXP_GROUPS_ALL]] — 18 atributos (1 PKs, 18 BICC)

---

## ⚙️ Atributos

### [[pjc_exp_groups_all|PJC_EXP_GROUPS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjcExpGroupsAllBatchEndingDate | BATCH_ENDING_DATE | — | ✅ |
| 2 | PjcExpGroupsAllCreatedBy | CREATED_BY | — | ✅ |
| 3 | PjcExpGroupsAllCreationDate | CREATION_DATE | — | ✅ |
| 4 | PjcExpGroupsAllDescription | DESCRIPTION | — | ✅ |
| 5 | PjcExpGroupsAllDocumentId | DOCUMENT_ID | — | ✅ |
| 6 | PjcExpGroupsAllExpGroupId | EXP_GROUP_ID | 🔑 | ✅ |
| 7 | PjcExpGroupsAllExpenditureGroup | EXPENDITURE_GROUP | — | ✅ |
| 8 | PjcExpGroupsAllJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 9 | PjcExpGroupsAllJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 10 | PjcExpGroupsAllLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | PjcExpGroupsAllLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | PjcExpGroupsAllLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | PjcExpGroupsAllObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | PjcExpGroupsAllOrgId | ORG_ID | — | ✅ |
| 15 | PjcExpGroupsAllPeriodAccrualFlag | PERIOD_ACCRUAL_FLAG | — | ✅ |
| 16 | PjcExpGroupsAllRequestId | REQUEST_ID | — | ✅ |
| 17 | PjcExpGroupsAllTransactionSourceId | TRANSACTION_SOURCE_ID | — | ✅ |
| 18 | PjcExpGroupsAllUserBatchName | USER_BATCH_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
