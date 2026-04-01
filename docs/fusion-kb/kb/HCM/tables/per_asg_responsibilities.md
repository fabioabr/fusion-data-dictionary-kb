---
id: DOC-HCM-629
doc_type: system-doc
title: "PER_ASG_RESPONSIBILITIES — Responsabilidades por Assignment"
system: Oracle Fusion Cloud HCM
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
  - workforce-management
  - responsabilidades
  - assignment-responsibilities
aliases:
  - PER_ASG_RESPONSIBILITIES
  - per_asg_responsibilities
  - per-asg-responsibilities
  - responsabilidades-por-assignment
  - per-asg-responsibili
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_ASG_RESPONSIBILITIES

## 📌 Visão Geral

Armazena as **responsabilidades** atribuídas a assignments específicos. Define papéis e responsabilidades adicionais que um colaborador exerce além do cargo base.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de responsabilidades** — define papéis adicionais por assignment.
- **Delegação** — registro de responsabilidades temporárias ou permanentes.
- **Compliance** — rastreabilidade de quem é responsável por quais funções.
- **Avaliação de desempenho** — base para avaliação de competências e responsabilidades.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ASG_RESPONSIBILITY_ID | NUMBER(18) | NOT NULL | PK | Identificador único da responsabilidade | — | 🟢 90% |
| 2 | ASSIGNMENT_ID | NUMBER(18) | NOT NULL | FK | Assignment associado | PER_ALL_ASSIGNMENTS_M | 🟢 90% |
| 3 | RESPONSIBILITY_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de responsabilidade | — | 🟡 75% |
| 4 | START_DATE | DATE | NULL | Período | Data de início da responsabilidade | — | 🟢 85% |
| 5 | END_DATE | DATE | NULL | Período | Data de fim da responsabilidade | — | 🟢 85% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_assignments_m]] — via `ASSIGNMENT_ID` (vínculo ao qual a responsabilidade pertence)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha direta identificada.

---

## 📎 Uso Típico

### Responsabilidades ativas de um assignment
```sql
SELECT par.RESPONSIBILITY_TYPE, par.START_DATE, par.END_DATE
FROM   PER_ASG_RESPONSIBILITIES par
WHERE  par.ASSIGNMENT_ID = :p_assignment_id
  AND  (par.END_DATE IS NULL OR par.END_DATE >= SYSDATE);
```

### Filtros comuns
- `END_DATE IS NULL` — Responsabilidades sem data de fim (permanentes)
---

## 🔒 Observações

- Permite atribuir responsabilidades adicionais sem alterar o cargo do colaborador.
- Responsabilidades com data de fim representam atribuições temporárias.
- Utilizada para compliance em contextos regulatórios (ex.: responsável por dados, DPO).
---

## 🔗 PVOs Relacionados

### [[assignmentresponsibilitypvo|AssignmentResponsibilityPVO]] (AR · BICC: 55/55)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASG_RESPONSIBILITY_ID | AsgResponsibilityId | ✅ |
| ASSIGNMENT_CATEGORY | AssignmentCategory | ✅ |
| ASSIGNMENT_ID | AssignmentId | ✅ |
| AUTO_PROVISION_FLAG | AutoProvisionFlag | ✅ |
| BARGAINING_UNIT | BargainingUnit | ✅ |
| BENEFIT_GROUP_ID | BenefitGroupId | ✅ |
| BUSINESS_UNIT_ID | BusinessUnitId | ✅ |
| COUNTRY | Country | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DEPARTMENT_HIERARCHY_ID | DepartmentHierarchyId | ✅ |
| DEPARTMENT_TREE_CODE | DepartmentTreeCode | ✅ |
| END_DATE | EndDate | ✅ |
| ENTERPRISE_ID | EnterpriseId | ✅ |
| GRADE_ID | GradeId | ✅ |
| HIERARCHY_LEVELS | HierarchyLevels | ✅ |
| HIERARCHY_TYPE | HierarchyType | ✅ |
| INCLUDE_TOP_HIER_NODE | IncludeTopHierNode | ✅ |
| JOB_FAMILY_ID | JobFamilyId | ✅ |
| JOB_FUNCTION_CODE | JobFunctionCode | ✅ |
| JOB_ID | JobId | ✅ |
| LAST_NAME_END | LastNameEnd | ✅ |
| LAST_NAME_START | LastNameStart | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LEGAL_ENTITY_ID | LegalEntityId | ✅ |
| LEGISLATIVE_DATA_GROUP_ID | LegislativeDataGroupId | ✅ |
| LOCATION_ID | LocationId | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| ORGANIZATION_HIERARCHY_ID | OrganizationHierarchyId | ✅ |
| ORGANIZATION_ID | OrganizationId | ✅ |
| ORGANIZATION_TREE_CODE | OrganizationTreeCode | ✅ |
| PAYROLL_ID | PayrollId | ✅ |
| PAYROLL_STAT_UNIT_ID | PayrollStatUnitId | ✅ |
| PERSON_ID | PersonId | ✅ |
| POSITION_HIERARCHY_ID | PositionHierarchyId | ✅ |
| POSITION_ID | PositionId | ✅ |
| POSITION_TREE_CODE | PositionTreeCode | ✅ |
| RECRUITING_LOC_HIERARCHY_ID | RecruitingLocHierarchyId | ✅ |
| RECRUITING_ORG_HIERARCHY_ID | RecruitingOrgHierarchyId | ✅ |
| RECRUITING_ORG_TREE_CODE | RecruitingOrgTreeCode | ✅ |
| RECRUITING_ORG_TREE_VER | RecruitingOrgTreeVer | ✅ |
| RECRUITING_TYPE_CODE | RecruitingTypeCode | ✅ |
| RESPONSIBILITY_NAME | ResponsibilityName | ✅ |
| RESPONSIBILITY_TYPE | ResponsibilityType | ✅ |
| START_DATE | StartDate | ✅ |
| STATUS | Status | ✅ |
| TAX_REPORTING_UNIT_ID | TaxReportingUnitId | ✅ |
| TEMPLATE_ID | TemplateId | ✅ |
| TOP_DEPARTMENT_ID | TopDepartmentId | ✅ |
| TOP_MANAGER_ID | TopManagerId | ✅ |
| TOP_ORGANIZATION_ID | TopOrganizationId | ✅ |
| TOP_POSITION_ID | TopPositionId | ✅ |
| WORK_CONTACTS_FLAG | WorkContactsFlag | ✅ |

---

## 📚 Referências

- [Oracle Docs — PER_ASG_RESPONSIBILITIES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perasgresponsibilities.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
