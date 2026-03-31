---
id: DOC-PO-PVO-RequisitionPVO
doc_type: system-doc
title: "RequisitionPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - RequisitionPVO
  - requisitionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RequisitionPVO

## 📌 Visão Geral

Extrai dados de requisições de contratação para consulta, consolidando informações de candidatos, assignees e processos seletivos. Base para relatórios de recrutamento e análise de pipeline de hiring.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.RequisitionAM.RequisitionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 55 | 5 | 1 | 21 | 38% |

---

## 🔗 Tabelas Relacionadas

- [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]] — 5 atributos
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 3 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 4 atributos (2 BICC)
- [[per_requisitions_interface_b|PER_REQUISITIONS_INTERFACE_B]] — 32 atributos (1 PKs, 16 BICC)
- [[per_requisitions_interface_tl|PER_REQUISITIONS_INTERFACE_TL]] — 11 atributos (3 BICC)

---

## ⚙️ Atributos

### [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentPEOAssignmentId | ASSIGNMENT_ID | — | — |
| 2 | AssignmentPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | AssignmentPEOEffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | — |
| 4 | AssignmentPEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 5 | AssignmentPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonDetailsPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | PersonDetailsPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | PersonDetailsPEOPersonId | PERSON_ID | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | PersonNameId | PERSON_NAME_ID | — | — |
| 4 | PersonNamePEODisplayName | DISPLAY_NAME | — | ✅ |

### [[per_requisitions_interface_b|PER_REQUISITIONS_INTERFACE_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RequisitionPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | RequisitionPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | RequisitionPEOEmployeeStatus | EMPLOYEE_STATUS | — | ✅ |
| 4 | RequisitionPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 5 | RequisitionPEOInterfaceSource | INTERFACE_SOURCE | — | ✅ |
| 6 | RequisitionPEOInterfaceSourceId | INTERFACE_SOURCE_ID | — | — |
| 7 | RequisitionPEOInterfaceType | INTERFACE_TYPE | — | — |
| 8 | RequisitionPEOJobId | JOB_ID | — | — |
| 9 | RequisitionPEOJobSchedule | JOB_SCHEDULE | — | ✅ |
| 10 | RequisitionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | RequisitionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | RequisitionPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | RequisitionPEOManagerAssignmentId | MANAGER_ASSIGNMENT_ID | — | — |
| 14 | RequisitionPEOManagerId | MANAGER_ID | — | — |
| 15 | RequisitionPEOManagerType | MANAGER_TYPE | — | — |
| 16 | RequisitionPEOManagerUserName | MANAGER_USER_NAME | — | — |
| 17 | RequisitionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | RequisitionPEOOrganizationId | ORGANIZATION_ID | — | — |
| 19 | RequisitionPEOPositionId | POSITION_ID | — | — |
| 20 | RequisitionPEOPrimaryLocationId | PRIMARY_LOCATION_ID | — | — |
| 21 | RequisitionPEORequisitionInterfaceCode | REQUISITION_INTERFACE_CODE | — | — |
| 22 | RequisitionPEORequisitionInterfaceId | REQUISITION_INTERFACE_ID | 🔑 | ✅ |
| 23 | RequisitionPEORequisitionJustification | REQUISITION_JUSTIFICATION | — | ✅ |
| 24 | RequisitionPEORequisitionNumber | REQUISITION_NUMBER | — | ✅ |
| 25 | RequisitionPEORequisitionStatus | REQUISITION_STATUS | — | ✅ |
| 26 | RequisitionPEORequisitionTemplateCode | REQUISITION_TEMPLATE_CODE | — | — |
| 27 | RequisitionPEOTargetStartDate | TARGET_START_DATE | — | — |
| 28 | RequisitionPEOTotalAvailableHeadcount | TOTAL_AVAILABLE_HEADCOUNT | — | ✅ |
| 29 | RequisitionPEOTotalHiredHeadcount | TOTAL_HIRED_HEADCOUNT | — | ✅ |
| 30 | RequisitionPEOTotalOpenHeadcount | TOTAL_OPEN_HEADCOUNT | — | ✅ |
| 31 | RequisitionPEOUnlimitedHire | UNLIMITED_HIRE | — | ✅ |
| 32 | RequisitionPEOVacancyStatus | VACANCY_STATUS | — | ✅ |

### [[per_requisitions_interface_tl|PER_REQUISITIONS_INTERFACE_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RequisitionTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | RequisitionTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | RequisitionTranslationPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 4 | RequisitionTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 5 | RequisitionTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | RequisitionTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | RequisitionTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | RequisitionTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | RequisitionTranslationPEORequisitionInterfaceId | REQUISITION_INTERFACE_ID | — | — |
| 10 | RequisitionTranslationPEORequisitionTitle | REQUISITION_TITLE | — | ✅ |
| 11 | RequisitionTranslationPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
