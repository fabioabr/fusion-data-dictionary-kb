---
id: DOC-OTHER-PVO-MatrixManagerHierarchyCFDNDPVO
doc_type: system-doc
title: "MatrixManagerHierarchyCFDNDPVO — PVO Cross-Module"
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
  - MatrixManagerHierarchyCFDNDPVO
  - matrixmanagerhierarchycfdndpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MatrixManagerHierarchyCFDNDPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Matrix Manager Hierarchy CFDND. Acessa as tabelas: PER_MANAGER_HRCHY_REPORTEES_DN.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.ManagerHierarchyAM.MatrixManagerHierarchyCFDNDPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 75 | 1 | 4 | 23 | 31% |

---

## 🔗 Tabelas Relacionadas

- [[per_manager_hrchy_reportees_dn|PER_MANAGER_HRCHY_REPORTEES_DN]] — 75 atributos (4 PKs, 23 BICC)

---

## ⚙️ Atributos

### [[per_manager_hrchy_reportees_dn|PER_MANAGER_HRCHY_REPORTEES_DN]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | CreationDate | CREATION_DATE | — | — |
| 3 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 4 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 5 | EnterpriseId | ENTERPRISE_ID | — | — |
| 6 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 7 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 8 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | Level10ReporteeAsgId | LEVEL10_REPORTEE_ASSIGNMENT_ID | — | — |
| 12 | Level10ReporteeManagerType | MANAGER_TYPE | — | ✅ |
| 13 | Level10ReporteePersonId | LEVEL10_REPORTEE_PERSON_ID | — | — |
| 14 | Level11ReporteeAsgId | LEVEL11_REPORTEE_ASSIGNMENT_ID | — | — |
| 15 | Level11ReporteeManagerType | MANAGER_TYPE | — | ✅ |
| 16 | Level11ReporteePersonId | LEVEL11_REPORTEE_PERSON_ID | — | — |
| 17 | Level12ReporteeAsgId | LEVEL12_REPORTEE_ASSIGNMENT_ID | — | — |
| 18 | Level12ReporteeManagerType | MANAGER_TYPE | — | ✅ |
| 19 | Level12ReporteePersonId | LEVEL12_REPORTEE_PERSON_ID | — | — |
| 20 | Level13ReporteeAsgId | LEVEL13_REPORTEE_ASSIGNMENT_ID | — | — |
| 21 | Level13ReporteeManagerType | MANAGER_TYPE | — | ✅ |
| 22 | Level13ReporteePersonId | LEVEL13_REPORTEE_PERSON_ID | — | — |
| 23 | Level14ReporteeAsgId | LEVEL14_REPORTEE_ASSIGNMENT_ID | — | — |
| 24 | Level14ReporteeManagerType | MANAGER_TYPE | — | ✅ |
| 25 | Level14ReporteePersonId | LEVEL14_REPORTEE_PERSON_ID | — | — |
| 26 | Level15ReporteeAsgId | LEVEL15_REPORTEE_ASSIGNMENT_ID | 🔑 | ✅ |
| 27 | Level15ReporteeManagerType | MANAGER_TYPE | — | ✅ |
| 28 | Level15ReporteePersonId | LEVEL15_REPORTEE_PERSON_ID | — | — |
| 29 | Level16ReporteeAsgId | LEVEL16_REPORTEE_ASSIGNMENT_ID | — | — |
| 30 | Level16ReporteeManagerType | MANAGER_TYPE | — | — |
| 31 | Level16ReporteePersonId | LEVEL16_REPORTEE_PERSON_ID | — | — |
| 32 | Level17ReporteeAsgId | LEVEL17_REPORTEE_ASSIGNMENT_ID | — | — |
| 33 | Level17ReporteeManagerType | MANAGER_TYPE | — | — |
| 34 | Level17ReporteePersonId | LEVEL17_REPORTEE_PERSON_ID | — | — |
| 35 | Level18ReporteeAsgId | LEVEL18_REPORTEE_ASSIGNMENT_ID | — | — |
| 36 | Level18ReporteeManagerType | MANAGER_TYPE | — | — |
| 37 | Level18ReporteePersonId | LEVEL18_REPORTEE_PERSON_ID | — | — |
| 38 | Level19ReporteeAsgId | LEVEL19_REPORTEE_ASSIGNMENT_ID | — | — |
| 39 | Level19ReporteeManagerType | MANAGER_TYPE | — | — |
| 40 | Level19ReporteePersonId | LEVEL19_REPORTEE_PERSON_ID | — | — |
| 41 | Level1ReporteeAsgId | LEVEL1_REPORTEE_ASSIGNMENT_ID | — | — |
| 42 | Level1ReporteeManagerType | MANAGER_TYPE | — | ✅ |
| 43 | Level1ReporteePersonId | LEVEL1_REPORTEE_PERSON_ID | — | — |
| 44 | Level20ReporteeAsgId | LEVEL20_REPORTEE_ASSIGNMENT_ID | — | — |
| 45 | Level20ReporteeManagerType | MANAGER_TYPE | — | — |
| 46 | Level20ReporteePersonId | LEVEL20_REPORTEE_PERSON_ID | — | — |
| 47 | Level2ReporteeAsgId | LEVEL2_REPORTEE_ASSIGNMENT_ID | — | — |
| 48 | Level2ReporteeManagerType | MANAGER_TYPE | — | ✅ |
| 49 | Level2ReporteePersonId | LEVEL2_REPORTEE_PERSON_ID | — | — |
| 50 | Level3ReporteeAsgId | LEVEL3_REPORTEE_ASSIGNMENT_ID | — | — |
| 51 | Level3ReporteeManagerType | MANAGER_TYPE | — | ✅ |
| 52 | Level3ReporteePersonId | LEVEL3_REPORTEE_PERSON_ID | — | — |
| 53 | Level4ReporteeAsgId | LEVEL4_REPORTEE_ASSIGNMENT_ID | — | — |
| 54 | Level4ReporteeManagerType | MANAGER_TYPE | — | ✅ |
| 55 | Level4ReporteePersonId | LEVEL4_REPORTEE_PERSON_ID | — | — |
| 56 | Level5ReporteeAsgId | LEVEL5_REPORTEE_ASSIGNMENT_ID | — | — |
| 57 | Level5ReporteeManagerType | MANAGER_TYPE | — | ✅ |
| 58 | Level5ReporteePersonId | LEVEL5_REPORTEE_PERSON_ID | — | — |
| 59 | Level6ReporteeAsgId | LEVEL6_REPORTEE_ASSIGNMENT_ID | — | — |
| 60 | Level6ReporteeManagerType | MANAGER_TYPE | — | ✅ |
| 61 | Level6ReporteePersonId | LEVEL6_REPORTEE_PERSON_ID | — | — |
| 62 | Level7ReporteeAsgId | LEVEL7_REPORTEE_ASSIGNMENT_ID | — | — |
| 63 | Level7ReporteeManagerType | MANAGER_TYPE | — | ✅ |
| 64 | Level7ReporteePersonId | LEVEL7_REPORTEE_PERSON_ID | — | — |
| 65 | Level8ReporteeAsgId | LEVEL8_REPORTEE_ASSIGNMENT_ID | — | — |
| 66 | Level8ReporteeManagerType | MANAGER_TYPE | — | ✅ |
| 67 | Level8ReporteePersonId | LEVEL8_REPORTEE_PERSON_ID | — | — |
| 68 | Level9ReporteeAsgId | LEVEL9_REPORTEE_ASSIGNMENT_ID | — | — |
| 69 | Level9ReporteeManagerType | MANAGER_TYPE | — | ✅ |
| 70 | Level9ReporteePersonId | LEVEL9_REPORTEE_PERSON_ID | — | — |
| 71 | ManagerAssignmentId | MANAGER_ASSIGNMENT_ID | 🔑 | ✅ |
| 72 | ManagerId | MANAGER_ID | — | ✅ |
| 73 | ManagerLevel | MANAGER_LEVEL | — | ✅ |
| 74 | ManagerType | MANAGER_TYPE | — | ✅ |
| 75 | RequestId | REQUEST_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
