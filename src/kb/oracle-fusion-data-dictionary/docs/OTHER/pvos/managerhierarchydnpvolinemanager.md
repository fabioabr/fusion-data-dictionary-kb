---
id: DOC-OTHER-PVO-ManagerHierarchyDNPVOLineManager
doc_type: system-doc
title: "ManagerHierarchyDNPVOLineManager — PVO Cross-Module"
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
  - ManagerHierarchyDNPVOLineManager
  - managerhierarchydnpvolinemanager
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ManagerHierarchyDNPVOLineManager

## 📌 Visão Geral

View Object para extração BICC de dados de Manager Hierarchy DNLine Manager. Acessa as tabelas: PER_MANAGER_HRCHY_DN.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.ManagerHierarchyAM.ManagerHierarchyDNPVOLineManager`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 1 | 5 | 9 | 45% |

---

## 🔗 Tabelas Relacionadas

- [[per_manager_hrchy_dn|PER_MANAGER_HRCHY_DN]] — 20 atributos (5 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[per_manager_hrchy_dn|PER_MANAGER_HRCHY_DN]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentId | ASSIGNMENT_ID | 🔑 | ✅ |
| 2 | BusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | CreatedBy | CREATED_BY | — | — |
| 4 | CreationDate | CREATION_DATE | — | — |
| 5 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 6 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 7 | ImmediateReporteeAsgId | IMMEDIATE_REPORTEE_ASG_ID | — | — |
| 8 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 9 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 10 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | ManagerAssignmentId | MANAGER_ASSIGNMENT_ID | 🔑 | ✅ |
| 14 | ManagerId | MANAGER_ID | — | ✅ |
| 15 | ManagerLevel | MANAGER_LEVEL | — | ✅ |
| 16 | ManagerType | MANAGER_TYPE | 🔑 | ✅ |
| 17 | PersonId | PERSON_ID | — | ✅ |
| 18 | PrimaryAssignmentFlag | PRIMARY_ASSIGNMENT_FLAG | — | — |
| 19 | PrimaryManagerFlag | PRIMARY_MANAGER_FLAG | — | — |
| 20 | RequestId | REQUEST_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
