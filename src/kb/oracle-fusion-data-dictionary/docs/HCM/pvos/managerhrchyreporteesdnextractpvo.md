---
id: DOC-HCM-PVO-ManagerHrchyReporteesDNExtractPVO
doc_type: system-doc
title: "ManagerHrchyReporteesDNExtractPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - ManagerHrchyReporteesDNExtractPVO
  - managerhrchyreporteesdnextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ManagerHrchyReporteesDNExtractPVO

## 📌 Visão Geral

Extração BICC da hierarquia gerencial desnormalizada com subordinados por nível. Utilizado em cargas analíticas para construção de dimensão hierárquica de gestão no data warehouse.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.ManagerHierarchyBiccExtractAM.ManagerHrchyReporteesDNExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 55 | 1 | 9 | 55 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[per_manager_hrchy_reportees_dn|PER_MANAGER_HRCHY_REPORTEES_DN]] — 55 atributos (9 PKs, 55 BICC)

---

## ⚙️ Atributos

### [[per_manager_hrchy_reportees_dn|PER_MANAGER_HRCHY_REPORTEES_DN]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 4 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 5 | EnterpriseId | ENTERPRISE_ID | 🔑 | ✅ |
| 6 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 7 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 8 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | Level10ReporteeAssignmentId | LEVEL10_REPORTEE_ASSIGNMENT_ID | — | ✅ |
| 12 | Level10ReporteePersonId | LEVEL10_REPORTEE_PERSON_ID | — | ✅ |
| 13 | Level11ReporteeAssignmentId | LEVEL11_REPORTEE_ASSIGNMENT_ID | — | ✅ |
| 14 | Level11ReporteePersonId | LEVEL11_REPORTEE_PERSON_ID | — | ✅ |
| 15 | Level12ReporteeAssignmentId | LEVEL12_REPORTEE_ASSIGNMENT_ID | — | ✅ |
| 16 | Level12ReporteePersonId | LEVEL12_REPORTEE_PERSON_ID | — | ✅ |
| 17 | Level13ReporteeAssignmentId | LEVEL13_REPORTEE_ASSIGNMENT_ID | — | ✅ |
| 18 | Level13ReporteePersonId | LEVEL13_REPORTEE_PERSON_ID | — | ✅ |
| 19 | Level14ReporteeAssignmentId | LEVEL14_REPORTEE_ASSIGNMENT_ID | — | ✅ |
| 20 | Level14ReporteePersonId | LEVEL14_REPORTEE_PERSON_ID | — | ✅ |
| 21 | Level15ReporteeAssignmentId | LEVEL15_REPORTEE_ASSIGNMENT_ID | — | ✅ |
| 22 | Level15ReporteePersonId | LEVEL15_REPORTEE_PERSON_ID | — | ✅ |
| 23 | Level16ReporteeAssignmentId | LEVEL16_REPORTEE_ASSIGNMENT_ID | — | ✅ |
| 24 | Level16ReporteePersonId | LEVEL16_REPORTEE_PERSON_ID | — | ✅ |
| 25 | Level17ReporteeAssignmentId | LEVEL17_REPORTEE_ASSIGNMENT_ID | — | ✅ |
| 26 | Level17ReporteePersonId | LEVEL17_REPORTEE_PERSON_ID | — | ✅ |
| 27 | Level18ReporteeAssignmentId | LEVEL18_REPORTEE_ASSIGNMENT_ID | — | ✅ |
| 28 | Level18ReporteePersonId | LEVEL18_REPORTEE_PERSON_ID | — | ✅ |
| 29 | Level19ReporteeAssignmentId | LEVEL19_REPORTEE_ASSIGNMENT_ID | — | ✅ |
| 30 | Level19ReporteePersonId | LEVEL19_REPORTEE_PERSON_ID | — | ✅ |
| 31 | Level1ReporteeAssignmentId | LEVEL1_REPORTEE_ASSIGNMENT_ID | — | ✅ |
| 32 | Level1ReporteePersonId | LEVEL1_REPORTEE_PERSON_ID | — | ✅ |
| 33 | Level20ReporteeAssignmentId | LEVEL20_REPORTEE_ASSIGNMENT_ID | 🔑 | ✅ |
| 34 | Level20ReporteePersonId | LEVEL20_REPORTEE_PERSON_ID | 🔑 | ✅ |
| 35 | Level2ReporteeAssignmentId | LEVEL2_REPORTEE_ASSIGNMENT_ID | — | ✅ |
| 36 | Level2ReporteePersonId | LEVEL2_REPORTEE_PERSON_ID | — | ✅ |
| 37 | Level3ReporteeAssignmentId | LEVEL3_REPORTEE_ASSIGNMENT_ID | — | ✅ |
| 38 | Level3ReporteePersonId | LEVEL3_REPORTEE_PERSON_ID | — | ✅ |
| 39 | Level4ReporteeAssignmentId | LEVEL4_REPORTEE_ASSIGNMENT_ID | — | ✅ |
| 40 | Level4ReporteePersonId | LEVEL4_REPORTEE_PERSON_ID | — | ✅ |
| 41 | Level5ReporteeAssignmentId | LEVEL5_REPORTEE_ASSIGNMENT_ID | — | ✅ |
| 42 | Level5ReporteePersonId | LEVEL5_REPORTEE_PERSON_ID | — | ✅ |
| 43 | Level6ReporteeAssignmentId | LEVEL6_REPORTEE_ASSIGNMENT_ID | — | ✅ |
| 44 | Level6ReporteePersonId | LEVEL6_REPORTEE_PERSON_ID | — | ✅ |
| 45 | Level7ReporteeAssignmentId | LEVEL7_REPORTEE_ASSIGNMENT_ID | — | ✅ |
| 46 | Level7ReporteePersonId | LEVEL7_REPORTEE_PERSON_ID | — | ✅ |
| 47 | Level8ReporteeAssignmentId | LEVEL8_REPORTEE_ASSIGNMENT_ID | — | ✅ |
| 48 | Level8ReporteePersonId | LEVEL8_REPORTEE_PERSON_ID | — | ✅ |
| 49 | Level9ReporteeAssignmentId | LEVEL9_REPORTEE_ASSIGNMENT_ID | — | ✅ |
| 50 | Level9ReporteePersonId | LEVEL9_REPORTEE_PERSON_ID | — | ✅ |
| 51 | ManagerAssignmentId | MANAGER_ASSIGNMENT_ID | 🔑 | ✅ |
| 52 | ManagerId | MANAGER_ID | 🔑 | ✅ |
| 53 | ManagerLevel | MANAGER_LEVEL | 🔑 | ✅ |
| 54 | ManagerType | MANAGER_TYPE | 🔑 | ✅ |
| 55 | RequestId | REQUEST_ID | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
