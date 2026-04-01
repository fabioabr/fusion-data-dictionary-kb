---
id: DOC-AR-PVO-AssignmentResponsibilityPVO
doc_type: system-doc
title: "AssignmentResponsibilityPVO — PVO Accounts Receivable"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ar
  - data-dictionary
  - pvo
  - bicc
aliases:
  - AssignmentResponsibilityPVO
  - assignmentresponsibilitypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AssignmentResponsibilityPVO

## 📌 Visão Geral

Extrai as responsabilidades atribuídas a colaboradores no contexto de Contas a Receber. Mapeia quem é responsável por cobranças, aprovações e gestão de contas de clientes específicos.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.AreasOfResponsibilityAM.AssignmentResponsibilityPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 55 | 1 | 1 | 55 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[per_asg_responsibilities|PER_ASG_RESPONSIBILITIES]] — 55 atributos (1 PKs, 55 BICC)

---

## ⚙️ Atributos

### [[per_asg_responsibilities|PER_ASG_RESPONSIBILITIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AsgResponsibilityId | ASG_RESPONSIBILITY_ID | 🔑 | ✅ |
| 2 | AssignmentCategory | ASSIGNMENT_CATEGORY | — | ✅ |
| 3 | AssignmentId | ASSIGNMENT_ID | — | ✅ |
| 4 | AutoProvisionFlag | AUTO_PROVISION_FLAG | — | ✅ |
| 5 | BargainingUnit | BARGAINING_UNIT | — | ✅ |
| 6 | BenefitGroupId | BENEFIT_GROUP_ID | — | ✅ |
| 7 | BusinessUnitId | BUSINESS_UNIT_ID | — | ✅ |
| 8 | Country | COUNTRY | — | ✅ |
| 9 | CreatedBy | CREATED_BY | — | ✅ |
| 10 | CreationDate | CREATION_DATE | — | ✅ |
| 11 | DepartmentHierarchyId | DEPARTMENT_HIERARCHY_ID | — | ✅ |
| 12 | DepartmentTreeCode | DEPARTMENT_TREE_CODE | — | ✅ |
| 13 | EndDate | END_DATE | — | ✅ |
| 14 | EnterpriseId | ENTERPRISE_ID | — | ✅ |
| 15 | GradeId | GRADE_ID | — | ✅ |
| 16 | HierarchyLevels | HIERARCHY_LEVELS | — | ✅ |
| 17 | HierarchyType | HIERARCHY_TYPE | — | ✅ |
| 18 | IncludeTopHierNode | INCLUDE_TOP_HIER_NODE | — | ✅ |
| 19 | JobFamilyId | JOB_FAMILY_ID | — | ✅ |
| 20 | JobFunctionCode | JOB_FUNCTION_CODE | — | ✅ |
| 21 | JobId | JOB_ID | — | ✅ |
| 22 | LastNameEnd | LAST_NAME_END | — | ✅ |
| 23 | LastNameStart | LAST_NAME_START | — | ✅ |
| 24 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 25 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 26 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 27 | LegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 28 | LegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | ✅ |
| 29 | LocationId | LOCATION_ID | — | ✅ |
| 30 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 31 | OrganizationHierarchyId | ORGANIZATION_HIERARCHY_ID | — | ✅ |
| 32 | OrganizationId | ORGANIZATION_ID | — | ✅ |
| 33 | OrganizationTreeCode | ORGANIZATION_TREE_CODE | — | ✅ |
| 34 | PayrollId | PAYROLL_ID | — | ✅ |
| 35 | PayrollStatUnitId | PAYROLL_STAT_UNIT_ID | — | ✅ |
| 36 | PersonId | PERSON_ID | — | ✅ |
| 37 | PositionHierarchyId | POSITION_HIERARCHY_ID | — | ✅ |
| 38 | PositionId | POSITION_ID | — | ✅ |
| 39 | PositionTreeCode | POSITION_TREE_CODE | — | ✅ |
| 40 | RecruitingLocHierarchyId | RECRUITING_LOC_HIERARCHY_ID | — | ✅ |
| 41 | RecruitingOrgHierarchyId | RECRUITING_ORG_HIERARCHY_ID | — | ✅ |
| 42 | RecruitingOrgTreeCode | RECRUITING_ORG_TREE_CODE | — | ✅ |
| 43 | RecruitingOrgTreeVer | RECRUITING_ORG_TREE_VER | — | ✅ |
| 44 | RecruitingTypeCode | RECRUITING_TYPE_CODE | — | ✅ |
| 45 | ResponsibilityName | RESPONSIBILITY_NAME | — | ✅ |
| 46 | ResponsibilityType | RESPONSIBILITY_TYPE | — | ✅ |
| 47 | StartDate | START_DATE | — | ✅ |
| 48 | Status | STATUS | — | ✅ |
| 49 | TaxReportingUnitId | TAX_REPORTING_UNIT_ID | — | ✅ |
| 50 | TemplateId | TEMPLATE_ID | — | ✅ |
| 51 | TopDepartmentId | TOP_DEPARTMENT_ID | — | ✅ |
| 52 | TopManagerId | TOP_MANAGER_ID | — | ✅ |
| 53 | TopOrganizationId | TOP_ORGANIZATION_ID | — | ✅ |
| 54 | TopPositionId | TOP_POSITION_ID | — | ✅ |
| 55 | WorkContactsFlag | WORK_CONTACTS_FLAG | — | ✅ |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
