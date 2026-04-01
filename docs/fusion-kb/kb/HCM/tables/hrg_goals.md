---
id: DOC-HCM-165
doc_type: system-doc
title: "HRG_GOALS — Objetivos (Goals) de Colaboradores"
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
  - goals
  - performance
aliases:
  - HRG_GOALS
  - hrg_goals
  - objetivos-goals-de-colaboradores
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRG_GOALS

## 📌 Visão Geral

Tabela principal de **objetivos (goals)** de colaboradores no módulo de Performance.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de desempenho:** Objetivos individuais.
- **Acompanhamento:** Progresso, status e resultados.
- **Avaliação:** Base para ciclos de avaliação.
- **Alinhamento estratégico:** Vínculo com metas organizacionais.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | GOAL_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 95% |
| 2 | GOAL_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome do objetivo | — | 🟢 90% |
| 3 | GOAL_DESCRIPTION | VARCHAR2(4000) | NULL | Descrição | Descrição detalhada | — | 🟢 85% |
| 4 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador | [[per_all_people_f]] | 🟢 90% |
| 5 | GOAL_TYPE_CODE | VARCHAR2(30) | NULL | Classificação | Tipo (PERFORMANCE, DEVELOPMENT) | — | 🟡 80% |
| 6 | STATUS_CODE | VARCHAR2(30) | NOT NULL | Classificação | Status (NOT_STARTED, IN_PROGRESS, COMPLETED) | — | 🟢 85% |
| 7 | START_DATE | DATE | NULL | Data | Início | — | 🟢 85% |
| 8 | TARGET_COMPLETION_DATE | DATE | NULL | Data | Data prevista | — | 🟢 85% |
| 9 | COMPLETION_DATE | DATE | NULL | Data | Data real de conclusão | — | 🟢 85% |
| 10 | PERCENT_COMPLETE | NUMBER | NULL | Métrica | Percentual (0-100) | — | 🟢 85% |
| 11 | PRIORITY_CODE | VARCHAR2(30) | NULL | Classificação | Prioridade | — | 🟡 75% |
| 12 | WEIGHT | NUMBER | NULL | Métrica | Peso no plano | — | 🟡 75% |
| 13 | MANAGER_ID | NUMBER(18) | NULL | FK | Gestor | [[per_all_people_f]] | 🟡 75% |
| 14 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 15 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 16 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 17 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 18 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 19 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai
- [[per_all_people_f]] — via `PERSON_ID` (colaborador responsavel pela meta)

### Tabelas-filha

---

## 📎 Uso Típico

### Objetivos ativos
```sql
SELECT g.GOAL_ID, g.GOAL_NAME, g.STATUS_CODE, g.PERCENT_COMPLETE
FROM   HRG_GOALS g
WHERE  g.PERSON_ID = :p_person_id
  AND  g.STATUS_CODE NOT IN ('COMPLETED','CANCELLED')
ORDER BY g.PRIORITY_CODE;
```

---

## 🔒 Observações

- Tabela central do módulo de Goals.
- `WEIGHT` para nota ponderada.
- `PERCENT_COMPLETE` manual ou via métricas.

---

## 🔗 PVOs Relacionados

### [[careerdevgoalpvo|CareerDevGoalPVO]] (HCM · BICC: 51/65)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_TO_HIERARCHY_FLAG | GoalPEOAccessToHierarchyFlag | ✅ |
| ACTIVE_FLAG | GoalPEOActiveFlag | ✅ |
| ACTUAL_COMPLETION_DATE | GoalPEOActualCompletionDate | ✅ |
| ACTUAL_VALUE | GoalPEOActualValue | — |
| ALLOW_DEL_GOAL_FLAG | GoalPEOAllowDelGoalFlag | — |
| ALLOW_KEY_ATTR_UPDATE_FLAG | GoalPEOAllowKeyAttrUpdateFlag | ✅ |
| APPROVAL_STATUS_CODE | GoalPEOApprovalStatusCode | ✅ |
| APPROVER_RESPONSE_CODE | GoalPEOApproverResponseCode | ✅ |
| ASSIGNED_BY_PERSON_ID | GoalPEOAssignedByPersonId | ✅ |
| ASSIGNMENT_ID | GoalPEOAssignmentId | ✅ |
| ATTRIBUTE_CATEGORY | GoalPEOAttributeCategory | ✅ |
| BUSINESS_GROUP_ID | GoalPEOBusinessGroupId | ✅ |
| CATEGORY_CODE | GoalPEOCategoryCode | ✅ |
| COMMENTS | GoalPEOComments | — |
| COMMENTS_TEXT | GoalPEOCommentsText | ✅ |
| CREATED_BY | GoalPEOCreatedBy | ✅ |
| CREATION_DATE | GoalPEOCreationDate | ✅ |
| DESCRIPTION | GoalPEODescription | ✅ |
| GOAL_ACCESS_LEVEL_CODE | GoalPEOGoalAccessLevelCode | ✅ |
| GOAL_APPROVAL_STATE | GoalPEOGoalApprovalState | ✅ |
| GOAL_EXT_ID | GoalPEOGoalExtId | ✅ |
| GOAL_ID | GoalId | ✅ |
| GOAL_NAME | GoalPEOGoalName | ✅ |
| GOAL_SOURCE_CODE | GoalPEOGoalSourceCode | ✅ |
| GOAL_SUB_TYPE_CODE | GoalPEOGoalSubTypeCode | ✅ |
| GOAL_TYPE_CODE | GoalPEOGoalTypeCode | ✅ |
| GOAL_URL | GoalPEOGoalUrl | ✅ |
| GOAL_VERSION_TYPE_CODE | GoalPEOGoalVersionTypeCode | ✅ |
| HRCHY_ACCESS_GRANT_DATE | GoalPEOHrchyAccessGrantDate | ✅ |
| INCLUDE_IN_PERFDOC_FLAG | GoalPEOIncludeInPerfdocFlag | ✅ |
| LAST_MODIFIED_BY | GoalPEOLastModifiedBy | — |
| LAST_MODIFIED_DATE | GoalPEOLastModifiedDate | ✅ |
| LAST_UPDATE_DATE | GoalPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | GoalPEOLastUpdatedBy | ✅ |
| LEVEL_CODE | GoalPEOLevelCode | ✅ |
| LEVEL_MEANING | GoalPEOLevelMeaning | ✅ |
| LONG_DESCRIPTION | GoalPEOLongDescription | — |
| MASS_REQUEST_ID | GoalPEOMassRequestId | ✅ |
| MEASURE_CALC_RULE_CODE | GoalPEOMeasureCalcRuleCode | ✅ |
| MEASURE_COMMENTS | GoalPEOMeasureComments | — |
| MEASURE_NAME | GoalPEOMeasureName | — |
| MEASURE_TYPE_CODE | GoalPEOMeasureTypeCode | — |
| OBJECT_VERSION_NUMBER | GoalPEOObjectVersionNumber | ✅ |
| ORGANIZATION_ID | OrganizationId | ✅ |
| PERCENT_COMPLETE_CODE | GoalPEOPercentCompleteCode | ✅ |
| PERSON_ID | GoalPEOPersonId | ✅ |
| PREVIOUS_STATE_GOAL_ID | GoalPEOPreviousStateGoalId | — |
| PRIORITY_CODE | GoalPEOPriorityCode | ✅ |
| PRIVATE_FLAG | GoalPEOPrivateFlag | ✅ |
| PUBLISH_DATE | GoalPEOPublishDate | ✅ |
| PUBLISHED_FLAG | GoalPEOPublishedFlag | ✅ |
| REFERENCE_CONTENT_ITEM_ID | GoalPEOReferenceContentItemId | ✅ |
| REFERENCE_GOAL_ID | GoalPEOReferenceGoalId | ✅ |
| REQUEST_CONTEXT | GoalPEORequestContext | — |
| REQUESTER_PERSON_ID | GoalPEORequesterPersonId | ✅ |
| START_DATE | GoalPEOStartDate | ✅ |
| STATUS_CODE | GoalPEOStatusCode | ✅ |
| SUCCESS_CRITERIA | GoalPEOSuccessCriteria | — |
| SUCCESS_CRITERIA_TEXT | GoalPEOSuccessCriteriaText | ✅ |
| TARGET_COMPLETION_DATE | GoalPEOTargetCompletionDate | ✅ |
| TARGET_TYPE | GoalPEOTargetType | — |
| TARGET_VALUE | GoalPEOTargetValue | — |
| UOM_CODE | GoalPEOUomCode | — |
| VERSION_DATE | GoalPEOVersionDate | ✅ |

### [[careerdevgoalpvoviewall|CareerDevGoalPVOViewAll]] (HCM · BICC: 50/65)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_TO_HIERARCHY_FLAG | GoalPEOAccessToHierarchyFlag | ✅ |
| ACTIVE_FLAG | GoalPEOActiveFlag | ✅ |
| ACTUAL_COMPLETION_DATE | GoalPEOActualCompletionDate | ✅ |
| ACTUAL_VALUE | GoalPEOActualValue | — |
| ALLOW_DEL_GOAL_FLAG | GoalPEOAllowDelGoalFlag | — |
| ALLOW_KEY_ATTR_UPDATE_FLAG | GoalPEOAllowKeyAttrUpdateFlag | ✅ |
| APPROVAL_STATUS_CODE | GoalPEOApprovalStatusCode | ✅ |
| APPROVER_RESPONSE_CODE | GoalPEOApproverResponseCode | ✅ |
| ASSIGNED_BY_PERSON_ID | GoalPEOAssignedByPersonId | ✅ |
| ASSIGNMENT_ID | GoalPEOAssignmentId | ✅ |
| ATTRIBUTE_CATEGORY | GoalPEOAttributeCategory | ✅ |
| BUSINESS_GROUP_ID | GoalPEOBusinessGroupId | ✅ |
| CATEGORY_CODE | GoalPEOCategoryCode | ✅ |
| COMMENTS | GoalPEOComments | — |
| COMMENTS_TEXT | GoalPEOCommentsText | ✅ |
| CREATED_BY | GoalPEOCreatedBy | ✅ |
| CREATION_DATE | GoalPEOCreationDate | ✅ |
| DESCRIPTION | GoalPEODescription | ✅ |
| GOAL_ACCESS_LEVEL_CODE | GoalPEOGoalAccessLevelCode | ✅ |
| GOAL_APPROVAL_STATE | GoalPEOGoalApprovalState | ✅ |
| GOAL_EXT_ID | GoalPEOGoalExtId | ✅ |
| GOAL_ID | GoalId | ✅ |
| GOAL_NAME | GoalPEOGoalName | ✅ |
| GOAL_SOURCE_CODE | GoalPEOGoalSourceCode | ✅ |
| GOAL_SUB_TYPE_CODE | GoalPEOGoalSubTypeCode | ✅ |
| GOAL_TYPE_CODE | GoalPEOGoalTypeCode | ✅ |
| GOAL_URL | GoalPEOGoalUrl | ✅ |
| GOAL_VERSION_TYPE_CODE | GoalPEOGoalVersionTypeCode | ✅ |
| HRCHY_ACCESS_GRANT_DATE | GoalPEOHrchyAccessGrantDate | ✅ |
| INCLUDE_IN_PERFDOC_FLAG | GoalPEOIncludeInPerfdocFlag | ✅ |
| LAST_MODIFIED_BY | GoalPEOLastModifiedBy | — |
| LAST_MODIFIED_DATE | GoalPEOLastModifiedDate | ✅ |
| LAST_UPDATE_DATE | GoalPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | GoalPEOLastUpdatedBy | ✅ |
| LEVEL_CODE | GoalPEOLevelCode | ✅ |
| LEVEL_MEANING | GoalPEOLevelMeaning | ✅ |
| LONG_DESCRIPTION | GoalPEOLongDescription | — |
| MASS_REQUEST_ID | GoalPEOMassRequestId | ✅ |
| MEASURE_CALC_RULE_CODE | GoalPEOMeasureCalcRuleCode | ✅ |
| MEASURE_COMMENTS | GoalPEOMeasureComments | — |
| MEASURE_NAME | GoalPEOMeasureName | — |
| MEASURE_TYPE_CODE | GoalPEOMeasureTypeCode | — |
| OBJECT_VERSION_NUMBER | GoalPEOObjectVersionNumber | ✅ |
| ORGANIZATION_ID | OrganizationId | ✅ |
| PERCENT_COMPLETE_CODE | GoalPEOPercentCompleteCode | ✅ |
| PERSON_ID | GoalPEOPersonId | ✅ |
| PREVIOUS_STATE_GOAL_ID | GoalPEOPreviousStateGoalId | — |
| PRIORITY_CODE | GoalPEOPriorityCode | ✅ |
| PRIVATE_FLAG | GoalPEOPrivateFlag | ✅ |
| PUBLISH_DATE | GoalPEOPublishDate | ✅ |
| PUBLISHED_FLAG | GoalPEOPublishedFlag | — |
| REFERENCE_CONTENT_ITEM_ID | GoalPEOReferenceContentItemId | ✅ |
| REFERENCE_GOAL_ID | GoalPEOReferenceGoalId | ✅ |
| REQUEST_CONTEXT | GoalPEORequestContext | — |
| REQUESTER_PERSON_ID | GoalPEORequesterPersonId | ✅ |
| START_DATE | GoalPEOStartDate | ✅ |
| STATUS_CODE | GoalPEOStatusCode | ✅ |
| SUCCESS_CRITERIA | GoalPEOSuccessCriteria | — |
| SUCCESS_CRITERIA_TEXT | GoalPEOSuccessCriteriaText | ✅ |
| TARGET_COMPLETION_DATE | GoalPEOTargetCompletionDate | ✅ |
| TARGET_TYPE | GoalPEOTargetType | — |
| TARGET_VALUE | GoalPEOTargetValue | — |
| UOM_CODE | GoalPEOUomCode | — |
| VERSION_DATE | GoalPEOVersionDate | ✅ |

### [[careerdevgoalversionpvo|CareerDevGoalVersionPVO]] (HCM · BICC: 51/65)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_TO_HIERARCHY_FLAG | GoalPEOAccessToHierarchyFlag | ✅ |
| ACTIVE_FLAG | GoalPEOActiveFlag | ✅ |
| ACTUAL_COMPLETION_DATE | GoalPEOActualCompletionDate | ✅ |
| ACTUAL_VALUE | GoalPEOActualValue | — |
| ALLOW_DEL_GOAL_FLAG | GoalPEOAllowDelGoalFlag | — |
| ALLOW_KEY_ATTR_UPDATE_FLAG | GoalPEOAllowKeyAttrUpdateFlag | ✅ |
| APPROVAL_STATUS_CODE | GoalPEOApprovalStatusCode | ✅ |
| APPROVER_RESPONSE_CODE | GoalPEOApproverResponseCode | ✅ |
| ASSIGNED_BY_PERSON_ID | GoalPEOAssignedByPersonId | ✅ |
| ASSIGNMENT_ID | GoalPEOAssignmentId | ✅ |
| ATTRIBUTE_CATEGORY | GoalPEOAttributeCategory | ✅ |
| BUSINESS_GROUP_ID | GoalPEOBusinessGroupId | ✅ |
| CATEGORY_CODE | GoalPEOCategoryCode | ✅ |
| COMMENTS | GoalPEOComments | — |
| COMMENTS_TEXT | GoalPEOCommentsText | ✅ |
| CREATED_BY | GoalPEOCreatedBy | ✅ |
| CREATION_DATE | GoalPEOCreationDate | ✅ |
| DESCRIPTION | GoalPEODescription | ✅ |
| GOAL_ACCESS_LEVEL_CODE | GoalPEOGoalAccessLevelCode | ✅ |
| GOAL_APPROVAL_STATE | GoalPEOGoalApprovalState | ✅ |
| GOAL_EXT_ID | GoalPEOGoalExtId | ✅ |
| GOAL_ID | GoalId | ✅ |
| GOAL_NAME | GoalPEOGoalName | ✅ |
| GOAL_SOURCE_CODE | GoalPEOGoalSourceCode | ✅ |
| GOAL_SUB_TYPE_CODE | GoalPEOGoalSubTypeCode | ✅ |
| GOAL_TYPE_CODE | GoalPEOGoalTypeCode | ✅ |
| GOAL_URL | GoalPEOGoalUrl | ✅ |
| GOAL_VERSION_TYPE_CODE | GoalPEOGoalVersionTypeCode | ✅ |
| HRCHY_ACCESS_GRANT_DATE | GoalPEOHrchyAccessGrantDate | ✅ |
| INCLUDE_IN_PERFDOC_FLAG | GoalPEOIncludeInPerfdocFlag | ✅ |
| LAST_MODIFIED_BY | GoalPEOLastModifiedBy | ✅ |
| LAST_MODIFIED_DATE | GoalPEOLastModifiedDate | ✅ |
| LAST_UPDATE_DATE | GoalPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | GoalPEOLastUpdatedBy | ✅ |
| LEVEL_CODE | GoalPEOLevelCode | ✅ |
| LEVEL_MEANING | GoalPEOLevelMeaning | ✅ |
| LONG_DESCRIPTION | GoalPEOLongDescription | — |
| MASS_REQUEST_ID | GoalPEOMassRequestId | ✅ |
| MEASURE_CALC_RULE_CODE | GoalPEOMeasureCalcRuleCode | ✅ |
| MEASURE_COMMENTS | GoalPEOMeasureComments | — |
| MEASURE_NAME | GoalPEOMeasureName | — |
| MEASURE_TYPE_CODE | GoalPEOMeasureTypeCode | — |
| OBJECT_VERSION_NUMBER | GoalPEOObjectVersionNumber | ✅ |
| ORGANIZATION_ID | OrganizationId | ✅ |
| PERCENT_COMPLETE_CODE | GoalPEOPercentCompleteCode | ✅ |
| PERSON_ID | GoalPEOPersonId | ✅ |
| PREVIOUS_STATE_GOAL_ID | GoalPEOPreviousStateGoalId | — |
| PRIORITY_CODE | GoalPEOPriorityCode | ✅ |
| PRIVATE_FLAG | GoalPEOPrivateFlag | ✅ |
| PUBLISH_DATE | GoalPEOPublishDate | ✅ |
| PUBLISHED_FLAG | GoalPEOPublishedFlag | — |
| REFERENCE_CONTENT_ITEM_ID | GoalPEOReferenceContentItemId | ✅ |
| REFERENCE_GOAL_ID | GoalPEOReferenceGoalId | ✅ |
| REQUEST_CONTEXT | GoalPEORequestContext | — |
| REQUESTER_PERSON_ID | GoalPEORequesterPersonId | ✅ |
| START_DATE | GoalPEOStartDate | ✅ |
| STATUS_CODE | GoalPEOStatusCode | ✅ |
| SUCCESS_CRITERIA | GoalPEOSuccessCriteria | — |
| SUCCESS_CRITERIA_TEXT | GoalPEOSuccessCriteriaText | ✅ |
| TARGET_COMPLETION_DATE | GoalPEOTargetCompletionDate | ✅ |
| TARGET_TYPE | GoalPEOTargetType | — |
| TARGET_VALUE | GoalPEOTargetValue | — |
| UOM_CODE | GoalPEOUomCode | — |
| VERSION_DATE | GoalPEOVersionDate | ✅ |

### [[careerdevgoalversionpvoviewall|CareerDevGoalVersionPVOViewAll]] (HCM · BICC: 50/65)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_TO_HIERARCHY_FLAG | GoalPEOAccessToHierarchyFlag | ✅ |
| ACTIVE_FLAG | GoalPEOActiveFlag | ✅ |
| ACTUAL_COMPLETION_DATE | GoalPEOActualCompletionDate | ✅ |
| ACTUAL_VALUE | GoalPEOActualValue | — |
| ALLOW_DEL_GOAL_FLAG | GoalPEOAllowDelGoalFlag | — |
| ALLOW_KEY_ATTR_UPDATE_FLAG | GoalPEOAllowKeyAttrUpdateFlag | ✅ |
| APPROVAL_STATUS_CODE | GoalPEOApprovalStatusCode | ✅ |
| APPROVER_RESPONSE_CODE | GoalPEOApproverResponseCode | ✅ |
| ASSIGNED_BY_PERSON_ID | GoalPEOAssignedByPersonId | ✅ |
| ASSIGNMENT_ID | GoalPEOAssignmentId | ✅ |
| ATTRIBUTE_CATEGORY | GoalPEOAttributeCategory | ✅ |
| BUSINESS_GROUP_ID | GoalPEOBusinessGroupId | ✅ |
| CATEGORY_CODE | GoalPEOCategoryCode | ✅ |
| COMMENTS | GoalPEOComments | — |
| COMMENTS_TEXT | GoalPEOCommentsText | ✅ |
| CREATED_BY | GoalPEOCreatedBy | ✅ |
| CREATION_DATE | GoalPEOCreationDate | ✅ |
| DESCRIPTION | GoalPEODescription | ✅ |
| GOAL_ACCESS_LEVEL_CODE | GoalPEOGoalAccessLevelCode | ✅ |
| GOAL_APPROVAL_STATE | GoalPEOGoalApprovalState | ✅ |
| GOAL_EXT_ID | GoalPEOGoalExtId | ✅ |
| GOAL_ID | GoalId | ✅ |
| GOAL_NAME | GoalPEOGoalName | ✅ |
| GOAL_SOURCE_CODE | GoalPEOGoalSourceCode | ✅ |
| GOAL_SUB_TYPE_CODE | GoalPEOGoalSubTypeCode | ✅ |
| GOAL_TYPE_CODE | GoalPEOGoalTypeCode | ✅ |
| GOAL_URL | GoalPEOGoalUrl | ✅ |
| GOAL_VERSION_TYPE_CODE | GoalPEOGoalVersionTypeCode | ✅ |
| HRCHY_ACCESS_GRANT_DATE | GoalPEOHrchyAccessGrantDate | ✅ |
| INCLUDE_IN_PERFDOC_FLAG | GoalPEOIncludeInPerfdocFlag | ✅ |
| LAST_MODIFIED_BY | GoalPEOLastModifiedBy | — |
| LAST_MODIFIED_DATE | GoalPEOLastModifiedDate | ✅ |
| LAST_UPDATE_DATE | GoalPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | GoalPEOLastUpdatedBy | ✅ |
| LEVEL_CODE | GoalPEOLevelCode | ✅ |
| LEVEL_MEANING | GoalPEOLevelMeaning | ✅ |
| LONG_DESCRIPTION | GoalPEOLongDescription | — |
| MASS_REQUEST_ID | GoalPEOMassRequestId | ✅ |
| MEASURE_CALC_RULE_CODE | GoalPEOMeasureCalcRuleCode | ✅ |
| MEASURE_COMMENTS | GoalPEOMeasureComments | — |
| MEASURE_NAME | GoalPEOMeasureName | — |
| MEASURE_TYPE_CODE | GoalPEOMeasureTypeCode | — |
| OBJECT_VERSION_NUMBER | GoalPEOObjectVersionNumber | ✅ |
| ORGANIZATION_ID | OrganizationId | ✅ |
| PERCENT_COMPLETE_CODE | GoalPEOPercentCompleteCode | ✅ |
| PERSON_ID | GoalPEOPersonId | ✅ |
| PREVIOUS_STATE_GOAL_ID | GoalPEOPreviousStateGoalId | — |
| PRIORITY_CODE | GoalPEOPriorityCode | ✅ |
| PRIVATE_FLAG | GoalPEOPrivateFlag | ✅ |
| PUBLISH_DATE | GoalPEOPublishDate | ✅ |
| PUBLISHED_FLAG | GoalPEOPublishedFlag | — |
| REFERENCE_CONTENT_ITEM_ID | GoalPEOReferenceContentItemId | ✅ |
| REFERENCE_GOAL_ID | GoalPEOReferenceGoalId | ✅ |
| REQUEST_CONTEXT | GoalPEORequestContext | — |
| REQUESTER_PERSON_ID | GoalPEORequesterPersonId | ✅ |
| START_DATE | GoalPEOStartDate | ✅ |
| STATUS_CODE | GoalPEOStatusCode | ✅ |
| SUCCESS_CRITERIA | GoalPEOSuccessCriteria | — |
| SUCCESS_CRITERIA_TEXT | GoalPEOSuccessCriteriaText | ✅ |
| TARGET_COMPLETION_DATE | GoalPEOTargetCompletionDate | ✅ |
| TARGET_TYPE | GoalPEOTargetType | — |
| TARGET_VALUE | GoalPEOTargetValue | — |
| UOM_CODE | GoalPEOUomCode | — |
| VERSION_DATE | GoalPEOVersionDate | ✅ |

### [[careerdevpvo|CareerDevPVO]] (HCM · BICC: 39/63)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_TO_HIERARCHY_FLAG | GoalPEOAccessToHierarchyFlag | ✅ |
| ACTIVE_FLAG | GoalPEOActiveFlag | — |
| ACTUAL_COMPLETION_DATE | GoalPEOActualCompletionDate | ✅ |
| ACTUAL_VALUE | GoalPEOActualValue | ✅ |
| ALLOW_KEY_ATTR_UPDATE_FLAG | GoalPEOAllowKeyAttrUpdateFlag | ✅ |
| APPROVAL_STATUS_CODE | GoalPEOApprovalStatusCode | ✅ |
| APPROVER_RESPONSE_CODE | GoalPEOApproverResponseCode | — |
| ASSIGNED_BY_PERSON_ID | GoalPEOAssignedByPersonId | — |
| ASSIGNMENT_ID | GoalPEOAssignmentId | — |
| ATTRIBUTE_CATEGORY | GoalPEOAttributeCategory | ✅ |
| BUSINESS_GROUP_ID | GoalPEOBusinessGroupId | — |
| CATEGORY_CODE | GoalPEOCategoryCode | — |
| COMMENTS | GoalPEOComments | ✅ |
| COMMENTS_TEXT | GoalPEOCommentsText | — |
| CREATED_BY | GoalPEOCreatedBy | ✅ |
| CREATION_DATE | GoalPEOCreationDate | ✅ |
| DESCRIPTION | GoalPEODescription | ✅ |
| GOAL_ACCESS_LEVEL_CODE | GoalPEOGoalAccessLevelCode | — |
| GOAL_APPROVAL_STATE | GoalPEOGoalApprovalState | — |
| GOAL_EXT_ID | GoalPEOGoalExtId | — |
| GOAL_ID | GoalId | ✅ |
| GOAL_NAME | GoalPEOGoalName | ✅ |
| GOAL_SOURCE_CODE | GoalPEOGoalSourceCode | ✅ |
| GOAL_SUB_TYPE_CODE | GoalPEOGoalSubTypeCode | — |
| GOAL_TYPE_CODE | GoalPEOGoalTypeCode | ✅ |
| GOAL_URL | GoalPEOGoalUrl | ✅ |
| GOAL_VERSION_TYPE_CODE | GoalPEOGoalVersionTypeCode | ✅ |
| HRCHY_ACCESS_GRANT_DATE | GoalPEOHrchyAccessGrantDate | ✅ |
| INCLUDE_IN_PERFDOC_FLAG | GoalPEOIncludeInPerfdocFlag | ✅ |
| LAST_MODIFIED_DATE | GoalPEOLastModifiedDate | ✅ |
| LAST_UPDATE_DATE | GoalPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | GoalPEOLastUpdatedBy | ✅ |
| LEVEL_CODE | GoalPEOLevelCode | — |
| LEVEL_MEANING | GoalPEOLevelMeaning | ✅ |
| LONG_DESCRIPTION | GoalPEOLongDescription | — |
| MASS_REQUEST_ID | GoalPEOMassRequestId | — |
| MEASURE_CALC_RULE_CODE | GoalPEOMeasureCalcRuleCode | — |
| MEASURE_COMMENTS | GoalPEOMeasureComments | ✅ |
| MEASURE_NAME | GoalPEOMeasureName | ✅ |
| MEASURE_TYPE_CODE | GoalPEOMeasureTypeCode | ✅ |
| OBJECT_VERSION_NUMBER | GoalPEOObjectVersionNumber | — |
| ORGANIZATION_ID | GoalPEOOrganizationId | — |
| PERCENT_COMPLETE_CODE | GoalPEOPercentCompleteCode | ✅ |
| PERSON_ID | GoalPEOPersonId | ✅ |
| PREVIOUS_STATE_GOAL_ID | GoalPEOPreviousStateGoalId | — |
| PRIORITY_CODE | GoalPEOPriorityCode | ✅ |
| PRIVATE_FLAG | GoalPEOPrivateFlag | ✅ |
| PUBLISH_DATE | GoalPEOPublishDate | ✅ |
| PUBLISHED_FLAG | GoalPEOPublishedFlag | ✅ |
| REFERENCE_CONTENT_ITEM_ID | GoalPEOReferenceContentItemId | — |
| REFERENCE_GOAL_ID | GoalPEOReferenceGoalId | — |
| REQUEST_CONTEXT | GoalPEORequestContext | — |
| REQUESTER_PERSON_ID | GoalPEORequesterPersonId | — |
| START_DATE | GoalPEOStartDate | ✅ |
| STATUS_CODE | GoalPEOStatusCode | ✅ |
| SUCCESS_CRITERIA | GoalPEOSuccessCriteria | ✅ |
| SUCCESS_CRITERIA_TEXT | GoalPEOSuccessCriteriaText | — |
| TARGET_COMPLETION_DATE | GoalPEOTargetCompletionDate | ✅ |
| TARGET_TYPE | GoalPEOTargetType | ✅ |
| TARGET_VALUE | GoalPEOTargetValue | ✅ |
| UOM_CODE | GoalPEOUomCode | ✅ |
| VERSION_DATE | GoalPEOVersionDate | ✅ |

### [[careerdevversionpvo|CareerDevVersionPVO]] (HCM · BICC: 6/63)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_TO_HIERARCHY_FLAG | GoalPEOAccessToHierarchyFlag | — |
| ACTIVE_FLAG | GoalPEOActiveFlag | — |
| ACTUAL_COMPLETION_DATE | GoalPEOActualCompletionDate | — |
| ACTUAL_VALUE | GoalPEOActualValue | — |
| ALLOW_KEY_ATTR_UPDATE_FLAG | GoalPEOAllowKeyAttrUpdateFlag | — |
| APPROVAL_STATUS_CODE | GoalPEOApprovalStatusCode | — |
| APPROVER_RESPONSE_CODE | GoalPEOApproverResponseCode | — |
| ASSIGNED_BY_PERSON_ID | GoalPEOAssignedByPersonId | — |
| ASSIGNMENT_ID | GoalPEOAssignmentId | — |
| ATTRIBUTE_CATEGORY | GoalPEOAttributeCategory | — |
| BUSINESS_GROUP_ID | GoalPEOBusinessGroupId | — |
| CATEGORY_CODE | GoalPEOCategoryCode | — |
| COMMENTS | GoalPEOComments | — |
| COMMENTS_TEXT | GoalPEOCommentsText | — |
| CREATED_BY | GoalPEOCreatedBy | — |
| CREATION_DATE | GoalPEOCreationDate | — |
| DESCRIPTION | GoalPEODescription | — |
| GOAL_ACCESS_LEVEL_CODE | GoalPEOGoalAccessLevelCode | — |
| GOAL_APPROVAL_STATE | GoalPEOGoalApprovalState | — |
| GOAL_EXT_ID | GoalPEOGoalExtId | — |
| GOAL_ID | GoalId | ✅ |
| GOAL_NAME | GoalPEOGoalName | — |
| GOAL_SOURCE_CODE | GoalPEOGoalSourceCode | — |
| GOAL_SUB_TYPE_CODE | GoalPEOGoalSubTypeCode | — |
| GOAL_TYPE_CODE | GoalPEOGoalTypeCode | ✅ |
| GOAL_URL | GoalPEOGoalUrl | — |
| GOAL_VERSION_TYPE_CODE | GoalPEOGoalVersionTypeCode | — |
| HRCHY_ACCESS_GRANT_DATE | GoalPEOHrchyAccessGrantDate | — |
| INCLUDE_IN_PERFDOC_FLAG | GoalPEOIncludeInPerfdocFlag | — |
| LAST_MODIFIED_DATE | GoalPEOLastModifiedDate | — |
| LAST_UPDATE_DATE | GoalPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | GoalPEOLastUpdatedBy | — |
| LEVEL_CODE | GoalPEOLevelCode | — |
| LEVEL_MEANING | GoalPEOLevelMeaning | — |
| LONG_DESCRIPTION | GoalPEOLongDescription | — |
| MASS_REQUEST_ID | GoalPEOMassRequestId | — |
| MEASURE_CALC_RULE_CODE | GoalPEOMeasureCalcRuleCode | — |
| MEASURE_COMMENTS | GoalPEOMeasureComments | — |
| MEASURE_NAME | GoalPEOMeasureName | — |
| MEASURE_TYPE_CODE | GoalPEOMeasureTypeCode | — |
| OBJECT_VERSION_NUMBER | GoalPEOObjectVersionNumber | — |
| ORGANIZATION_ID | GoalPEOOrganizationId | — |
| PERCENT_COMPLETE_CODE | GoalPEOPercentCompleteCode | — |
| PERSON_ID | GoalPEOPersonId | ✅ |
| PREVIOUS_STATE_GOAL_ID | GoalPEOPreviousStateGoalId | — |
| PRIORITY_CODE | GoalPEOPriorityCode | — |
| PRIVATE_FLAG | GoalPEOPrivateFlag | — |
| PUBLISH_DATE | GoalPEOPublishDate | — |
| PUBLISHED_FLAG | GoalPEOPublishedFlag | — |
| REFERENCE_CONTENT_ITEM_ID | GoalPEOReferenceContentItemId | — |
| REFERENCE_GOAL_ID | GoalPEOReferenceGoalId | — |
| REQUEST_CONTEXT | GoalPEORequestContext | — |
| REQUESTER_PERSON_ID | GoalPEORequesterPersonId | — |
| START_DATE | GoalPEOStartDate | — |
| STATUS_CODE | GoalPEOStatusCode | ✅ |
| SUCCESS_CRITERIA | GoalPEOSuccessCriteria | — |
| SUCCESS_CRITERIA_TEXT | GoalPEOSuccessCriteriaText | — |
| TARGET_COMPLETION_DATE | GoalPEOTargetCompletionDate | ✅ |
| TARGET_TYPE | GoalPEOTargetType | — |
| TARGET_VALUE | GoalPEOTargetValue | — |
| UOM_CODE | GoalPEOUomCode | — |
| VERSION_DATE | GoalPEOVersionDate | — |

### [[colleaguegoalpvo|ColleagueGoalPVO]] (HCM · BICC: 7/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPROVAL_STATUS_CODE | GoalPEOApprovalStatusCode | ✅ |
| CREATED_BY | GoalPEOCreatedBy | ✅ |
| CREATION_DATE | GoalPEOCreationDate | ✅ |
| GOAL_APPROVAL_STATE | GoalPEOGoalApprovalState | — |
| GOAL_ID | GoalId | ✅ |
| HRCHY_ACCESS_GRANT_DATE | GoalPEOHrchyAccessGrantDate | — |
| LAST_UPDATE_DATE | GoalPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | GoalPEOLastUpdatedBy | ✅ |

### [[contentitemvaluepvo|ContentItemValuePVO]] (HCM · BICC: 3/54)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_TO_HIERARCHY_FLAG | GoalPEOAccessToHierarchyFlag | — |
| ACTUAL_COMPLETION_DATE | GoalPEOActualCompletionDate | ✅ |
| ACTUAL_VALUE | GoalPEOActualValue | — |
| ALLOW_KEY_ATTR_UPDATE_FLAG | GoalPEOAllowKeyAttrUpdateFlag | — |
| APPROVAL_STATUS_CODE | GoalPEOApprovalStatusCode | — |
| ASSIGNED_BY_PERSON_ID | GoalPEOAssignedByPersonId | — |
| ASSIGNMENT_ID | GoalPEOAssignmentId | — |
| ATTRIBUTE_CATEGORY | GoalPEOAttributeCategory | — |
| BUSINESS_GROUP_ID | GoalPEOBusinessGroupId | — |
| CATEGORY_CODE | GoalPEOCategoryCode | — |
| COMMENTS | GoalPEOComments | — |
| COMMENTS_TEXT | GoalPEOCommentsText | — |
| CREATED_BY | GoalPEOCreatedBy | — |
| CREATION_DATE | GoalPEOCreationDate | — |
| DESCRIPTION | GoalPEODescription | — |
| GOAL_APPROVAL_STATE | GoalPEOGoalApprovalState | — |
| GOAL_ID | GoalPEOGoalId | ✅ |
| GOAL_NAME | GoalPEOGoalName | — |
| GOAL_SOURCE_CODE | GoalPEOGoalSourceCode | — |
| GOAL_TYPE_CODE | GoalPEOGoalTypeCode | — |
| GOAL_URL | GoalPEOGoalUrl | — |
| GOAL_VERSION_TYPE_CODE | GoalPEOGoalVersionTypeCode | — |
| HRCHY_ACCESS_GRANT_DATE | GoalPEOHrchyAccessGrantDate | — |
| INCLUDE_IN_PERFDOC_FLAG | GoalPEOIncludeInPerfdocFlag | — |
| LAST_UPDATE_DATE | GoalPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | GoalPEOLastUpdatedBy | — |
| LEVEL_CODE | GoalPEOLevelCode | — |
| LEVEL_MEANING | GoalPEOLevelMeaning | — |
| LONG_DESCRIPTION | GoalPEOLongDescription | — |
| MASS_REQUEST_ID | GoalPEOMassRequestId | — |
| MEASURE_COMMENTS | GoalPEOMeasureComments | — |
| MEASURE_NAME | GoalPEOMeasureName | — |
| MEASURE_TYPE_CODE | GoalPEOMeasureTypeCode | — |
| OBJECT_VERSION_NUMBER | GoalPEOObjectVersionNumber | — |
| ORGANIZATION_ID | GoalPEOOrganizationId | — |
| PERCENT_COMPLETE_CODE | GoalPEOPercentCompleteCode | — |
| PERSON_ID | GoalPEOPersonId | — |
| PRIORITY_CODE | GoalPEOPriorityCode | — |
| PRIVATE_FLAG | GoalPEOPrivateFlag | — |
| PUBLISH_DATE | GoalPEOPublishDate | — |
| PUBLISHED_FLAG | GoalPEOPublishedFlag | — |
| REFERENCE_CONTENT_ITEM_ID | GoalPEOReferenceContentItemId | — |
| REFERENCE_GOAL_ID | GoalPEOReferenceGoalId | — |
| REQUESTER_PERSON_ID | GoalPEORequesterPersonId | — |
| START_DATE | GoalPEOStartDate | — |
| STATUS_CODE | GoalPEOStatusCode | — |
| SUCCESS_CRITERIA | GoalPEOSuccessCriteria | — |
| SUCCESS_CRITERIA_TEXT | GoalPEOSuccessCriteriaText | — |
| TARGET_COMPLETION_DATE | GoalPEOTargetCompletionDate | — |
| TARGET_TYPE | GoalPEOTargetType | — |
| TARGET_VALUE | GoalPEOTargetValue | — |
| UOM_CODE | GoalPEOUomCode | — |
| VERSION_DATE | GoalPEOVersionDate | — |

### [[developmentgoalpvo|DevelopmentGoalPVO]] (HCM · BICC: 51/65)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_TO_HIERARCHY_FLAG | GoalPEOAccessToHierarchyFlag | ✅ |
| ACTIVE_FLAG | GoalPEOActiveFlag | ✅ |
| ACTUAL_COMPLETION_DATE | GoalPEOActualCompletionDate | ✅ |
| ACTUAL_VALUE | GoalPEOActualValue | — |
| ALLOW_DEL_GOAL_FLAG | GoalPEOAllowDelGoalFlag | — |
| ALLOW_KEY_ATTR_UPDATE_FLAG | GoalPEOAllowKeyAttrUpdateFlag | ✅ |
| APPROVAL_STATUS_CODE | GoalPEOApprovalStatusCode | ✅ |
| APPROVER_RESPONSE_CODE | GoalPEOApproverResponseCode | ✅ |
| ASSIGNED_BY_PERSON_ID | GoalPEOAssignedByPersonId | ✅ |
| ASSIGNMENT_ID | GoalPEOAssignmentId | ✅ |
| ATTRIBUTE_CATEGORY | GoalPEOAttributeCategory | ✅ |
| BUSINESS_GROUP_ID | GoalPEOBusinessGroupId | ✅ |
| CATEGORY_CODE | GoalPEOCategoryCode | ✅ |
| COMMENTS | GoalPEOComments | — |
| COMMENTS_TEXT | GoalPEOCommentsText | ✅ |
| CREATED_BY | GoalPEOCreatedBy | ✅ |
| CREATION_DATE | GoalPEOCreationDate | ✅ |
| DESCRIPTION | GoalPEODescription | ✅ |
| GOAL_ACCESS_LEVEL_CODE | GoalPEOGoalAccessLevelCode | ✅ |
| GOAL_APPROVAL_STATE | GoalPEOGoalApprovalState | ✅ |
| GOAL_EXT_ID | GoalPEOGoalExtId | ✅ |
| GOAL_ID | GoalId | ✅ |
| GOAL_NAME | GoalPEOGoalName | ✅ |
| GOAL_SOURCE_CODE | GoalPEOGoalSourceCode | ✅ |
| GOAL_SUB_TYPE_CODE | GoalPEOGoalSubTypeCode | ✅ |
| GOAL_TYPE_CODE | GoalPEOGoalTypeCode | ✅ |
| GOAL_URL | GoalPEOGoalUrl | ✅ |
| GOAL_VERSION_TYPE_CODE | GoalPEOGoalVersionTypeCode | ✅ |
| HRCHY_ACCESS_GRANT_DATE | GoalPEOHrchyAccessGrantDate | ✅ |
| INCLUDE_IN_PERFDOC_FLAG | GoalPEOIncludeInPerfdocFlag | ✅ |
| LAST_MODIFIED_BY | GoalPEOLastModifiedBy | — |
| LAST_MODIFIED_DATE | GoalPEOLastModifiedDate | ✅ |
| LAST_UPDATE_DATE | GoalPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | GoalPEOLastUpdatedBy | ✅ |
| LEVEL_CODE | GoalPEOLevelCode | ✅ |
| LEVEL_MEANING | GoalPEOLevelMeaning | ✅ |
| LONG_DESCRIPTION | GoalPEOLongDescription | — |
| MASS_REQUEST_ID | GoalPEOMassRequestId | ✅ |
| MEASURE_CALC_RULE_CODE | GoalPEOMeasureCalcRuleCode | ✅ |
| MEASURE_COMMENTS | GoalPEOMeasureComments | — |
| MEASURE_NAME | GoalPEOMeasureName | — |
| MEASURE_TYPE_CODE | GoalPEOMeasureTypeCode | — |
| OBJECT_VERSION_NUMBER | GoalPEOObjectVersionNumber | ✅ |
| ORGANIZATION_ID | OrganizationId | ✅ |
| PERCENT_COMPLETE_CODE | GoalPEOPercentCompleteCode | ✅ |
| PERSON_ID | GoalPEOPersonId | ✅ |
| PREVIOUS_STATE_GOAL_ID | GoalPEOPreviousStateGoalId | — |
| PRIORITY_CODE | GoalPEOPriorityCode | ✅ |
| PRIVATE_FLAG | GoalPEOPrivateFlag | ✅ |
| PUBLISH_DATE | GoalPEOPublishDate | ✅ |
| PUBLISHED_FLAG | GoalPEOPublishedFlag | ✅ |
| REFERENCE_CONTENT_ITEM_ID | GoalPEOReferenceContentItemId | ✅ |
| REFERENCE_GOAL_ID | GoalPEOReferenceGoalId | ✅ |
| REQUEST_CONTEXT | GoalPEORequestContext | — |
| REQUESTER_PERSON_ID | GoalPEORequesterPersonId | ✅ |
| START_DATE | GoalPEOStartDate | ✅ |
| STATUS_CODE | GoalPEOStatusCode | ✅ |
| SUCCESS_CRITERIA | GoalPEOSuccessCriteria | — |
| SUCCESS_CRITERIA_TEXT | GoalPEOSuccessCriteriaText | ✅ |
| TARGET_COMPLETION_DATE | GoalPEOTargetCompletionDate | ✅ |
| TARGET_TYPE | GoalPEOTargetType | — |
| TARGET_VALUE | GoalPEOTargetValue | — |
| UOM_CODE | GoalPEOUomCode | — |
| VERSION_DATE | GoalPEOVersionDate | ✅ |

### [[developmentgoalpvoviewall|DevelopmentGoalPVOViewAll]] (HCM · BICC: 51/65)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_TO_HIERARCHY_FLAG | GoalPEOAccessToHierarchyFlag | ✅ |
| ACTIVE_FLAG | GoalPEOActiveFlag | ✅ |
| ACTUAL_COMPLETION_DATE | GoalPEOActualCompletionDate | ✅ |
| ACTUAL_VALUE | GoalPEOActualValue | — |
| ALLOW_DEL_GOAL_FLAG | GoalPEOAllowDelGoalFlag | — |
| ALLOW_KEY_ATTR_UPDATE_FLAG | GoalPEOAllowKeyAttrUpdateFlag | ✅ |
| APPROVAL_STATUS_CODE | GoalPEOApprovalStatusCode | ✅ |
| APPROVER_RESPONSE_CODE | GoalPEOApproverResponseCode | ✅ |
| ASSIGNED_BY_PERSON_ID | GoalPEOAssignedByPersonId | ✅ |
| ASSIGNMENT_ID | GoalPEOAssignmentId | ✅ |
| ATTRIBUTE_CATEGORY | GoalPEOAttributeCategory | ✅ |
| BUSINESS_GROUP_ID | GoalPEOBusinessGroupId | ✅ |
| CATEGORY_CODE | GoalPEOCategoryCode | ✅ |
| COMMENTS | GoalPEOComments | — |
| COMMENTS_TEXT | GoalPEOCommentsText | ✅ |
| CREATED_BY | GoalPEOCreatedBy | ✅ |
| CREATION_DATE | GoalPEOCreationDate | ✅ |
| DESCRIPTION | GoalPEODescription | ✅ |
| GOAL_ACCESS_LEVEL_CODE | GoalPEOGoalAccessLevelCode | ✅ |
| GOAL_APPROVAL_STATE | GoalPEOGoalApprovalState | ✅ |
| GOAL_EXT_ID | GoalPEOGoalExtId | ✅ |
| GOAL_ID | GoalId | ✅ |
| GOAL_NAME | GoalPEOGoalName | ✅ |
| GOAL_SOURCE_CODE | GoalPEOGoalSourceCode | ✅ |
| GOAL_SUB_TYPE_CODE | GoalPEOGoalSubTypeCode | ✅ |
| GOAL_TYPE_CODE | GoalPEOGoalTypeCode | ✅ |
| GOAL_URL | GoalPEOGoalUrl | ✅ |
| GOAL_VERSION_TYPE_CODE | GoalPEOGoalVersionTypeCode | ✅ |
| HRCHY_ACCESS_GRANT_DATE | GoalPEOHrchyAccessGrantDate | ✅ |
| INCLUDE_IN_PERFDOC_FLAG | GoalPEOIncludeInPerfdocFlag | ✅ |
| LAST_MODIFIED_BY | GoalPEOLastModifiedBy | — |
| LAST_MODIFIED_DATE | GoalPEOLastModifiedDate | ✅ |
| LAST_UPDATE_DATE | GoalPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | GoalPEOLastUpdatedBy | ✅ |
| LEVEL_CODE | GoalPEOLevelCode | ✅ |
| LEVEL_MEANING | GoalPEOLevelMeaning | ✅ |
| LONG_DESCRIPTION | GoalPEOLongDescription | — |
| MASS_REQUEST_ID | GoalPEOMassRequestId | ✅ |
| MEASURE_CALC_RULE_CODE | GoalPEOMeasureCalcRuleCode | ✅ |
| MEASURE_COMMENTS | GoalPEOMeasureComments | — |
| MEASURE_NAME | GoalPEOMeasureName | — |
| MEASURE_TYPE_CODE | GoalPEOMeasureTypeCode | — |
| OBJECT_VERSION_NUMBER | GoalPEOObjectVersionNumber | ✅ |
| ORGANIZATION_ID | OrganizationId | ✅ |
| PERCENT_COMPLETE_CODE | GoalPEOPercentCompleteCode | ✅ |
| PERSON_ID | GoalPEOPersonId | ✅ |
| PREVIOUS_STATE_GOAL_ID | GoalPEOPreviousStateGoalId | — |
| PRIORITY_CODE | GoalPEOPriorityCode | ✅ |
| PRIVATE_FLAG | GoalPEOPrivateFlag | ✅ |
| PUBLISH_DATE | GoalPEOPublishDate | ✅ |
| PUBLISHED_FLAG | GoalPEOPublishedFlag | ✅ |
| REFERENCE_CONTENT_ITEM_ID | GoalPEOReferenceContentItemId | ✅ |
| REFERENCE_GOAL_ID | GoalPEOReferenceGoalId | ✅ |
| REQUEST_CONTEXT | GoalPEORequestContext | — |
| REQUESTER_PERSON_ID | GoalPEORequesterPersonId | ✅ |
| START_DATE | GoalPEOStartDate | ✅ |
| STATUS_CODE | GoalPEOStatusCode | ✅ |
| SUCCESS_CRITERIA | GoalPEOSuccessCriteria | — |
| SUCCESS_CRITERIA_TEXT | GoalPEOSuccessCriteriaText | ✅ |
| TARGET_COMPLETION_DATE | GoalPEOTargetCompletionDate | ✅ |
| TARGET_TYPE | GoalPEOTargetType | — |
| TARGET_VALUE | GoalPEOTargetValue | — |
| UOM_CODE | GoalPEOUomCode | — |
| VERSION_DATE | GoalPEOVersionDate | ✅ |

### [[goalalignmentpvo|GoalAlignmentPVO]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| GOAL_APPROVAL_STATE | GoalPEOGoalApprovalState | — |
| GOAL_ID | GoalpeogoalId | ✅ |
| GOAL_NAME | GoalPEOGoalName | ✅ |
| LONG_DESCRIPTION | GoalPEOLongDescription | — |

### [[goalextractpvo|GoalExtractPVO]] (HCM · BICC: 56/121)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | ActiveFlag | ✅ |
| ACTUAL_COMPLETION_DATE | ActualCompletionDate | ✅ |
| ALLOW_DEL_GOAL_FLAG | AllowDelGoalFlag | ✅ |
| ALLOW_KEY_ATTR_UPDATE_FLAG | AllowKeyAttrUpdateFlag | ✅ |
| APPROVAL_STATUS_CODE | ApprovalStatusCode | ✅ |
| APPROVER_RESPONSE_CODE | ApproverResponseCode | ✅ |
| ASSIGNED_BY_PERSON_ID | AssignedByPersonId | ✅ |
| ASSIGNMENT_ID | AssignmentId | ✅ |
| ATTRIBUTE1 | Attribute1 | — |
| ATTRIBUTE10 | Attribute10 | — |
| ATTRIBUTE11 | Attribute11 | — |
| ATTRIBUTE12 | Attribute12 | — |
| ATTRIBUTE13 | Attribute13 | — |
| ATTRIBUTE14 | Attribute14 | — |
| ATTRIBUTE15 | Attribute15 | — |
| ATTRIBUTE16 | Attribute16 | — |
| ATTRIBUTE17 | Attribute17 | — |
| ATTRIBUTE18 | Attribute18 | — |
| ATTRIBUTE19 | Attribute19 | — |
| ATTRIBUTE2 | Attribute2 | — |
| ATTRIBUTE20 | Attribute20 | — |
| ATTRIBUTE21 | Attribute21 | — |
| ATTRIBUTE22 | Attribute22 | — |
| ATTRIBUTE23 | Attribute23 | — |
| ATTRIBUTE24 | Attribute24 | — |
| ATTRIBUTE25 | Attribute25 | — |
| ATTRIBUTE26 | Attribute26 | — |
| ATTRIBUTE27 | Attribute27 | — |
| ATTRIBUTE28 | Attribute28 | — |
| ATTRIBUTE29 | Attribute29 | — |
| ATTRIBUTE3 | Attribute3 | — |
| ATTRIBUTE30 | Attribute30 | — |
| ATTRIBUTE4 | Attribute4 | — |
| ATTRIBUTE5 | Attribute5 | — |
| ATTRIBUTE6 | Attribute6 | — |
| ATTRIBUTE7 | Attribute7 | — |
| ATTRIBUTE8 | Attribute8 | — |
| ATTRIBUTE9 | Attribute9 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory | ✅ |
| ATTRIBUTE_DATE1 | AttributeDate1 | — |
| ATTRIBUTE_DATE10 | AttributeDate10 | — |
| ATTRIBUTE_DATE11 | AttributeDate11 | — |
| ATTRIBUTE_DATE12 | AttributeDate12 | — |
| ATTRIBUTE_DATE13 | AttributeDate13 | — |
| ATTRIBUTE_DATE14 | AttributeDate14 | — |
| ATTRIBUTE_DATE15 | AttributeDate15 | — |
| ATTRIBUTE_DATE2 | AttributeDate2 | — |
| ATTRIBUTE_DATE3 | AttributeDate3 | — |
| ATTRIBUTE_DATE4 | AttributeDate4 | — |
| ATTRIBUTE_DATE5 | AttributeDate5 | — |
| ATTRIBUTE_DATE6 | AttributeDate6 | — |
| ATTRIBUTE_DATE7 | AttributeDate7 | — |
| ATTRIBUTE_DATE8 | AttributeDate8 | — |
| ATTRIBUTE_DATE9 | AttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber9 | — |
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CATEGORY_CODE | CategoryCode | ✅ |
| COMMENTS | Comments | ✅ |
| COMMENTS_TEXT | CommentsText | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DESCRIPTION | Description | ✅ |
| GOAL_ACCESS_LEVEL_CODE | GoalAccessLevelCode | ✅ |
| GOAL_APPROVAL_STATE | GoalApprovalState | ✅ |
| GOAL_EXT_ID | GoalExtId | ✅ |
| GOAL_ID | GoalId | ✅ |
| GOAL_NAME | GoalName | ✅ |
| GOAL_SOURCE_CODE | GoalSourceCode | ✅ |
| GOAL_SUB_TYPE_CODE | GoalSubTypeCode | ✅ |
| GOAL_TYPE_CODE | GoalTypeCode | ✅ |
| GOAL_URL | GoalUrl | ✅ |
| GOAL_VERSION_TYPE_CODE | GoalVersionTypeCode | ✅ |
| INCLUDE_IN_PERFDOC_FLAG | IncludeInPerfdocFlag | ✅ |
| LAST_MODIFIED_BY | LastModifiedBy | ✅ |
| LAST_MODIFIED_DATE | LastModifiedDate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LEVEL_CODE | LevelCode | ✅ |
| LEVEL_MEANING | LevelMeaning | ✅ |
| LONG_DESCRIPTION | LongDescription | ✅ |
| MASS_REQUEST_ID | MassRequestId | ✅ |
| MEASURE_CALC_RULE_CODE | MeasureCalcRuleCode | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| ORGANIZATION_ID | OrganizationId | ✅ |
| PERCENT_COMPLETE_CODE | PercentCompleteCode | ✅ |
| PERSON_ID | PersonId | ✅ |
| PREVIOUS_STATE_GOAL_ID | PreviousStateGoalId | ✅ |
| PRIORITY_CODE | PriorityCode | ✅ |
| PRIVATE_FLAG | PrivateFlag | ✅ |
| PUBLISH_DATE | PublishDate | ✅ |
| PUBLISHED_FLAG | PublishedFlag | ✅ |
| REFERENCE_CONTENT_ITEM_ID | ReferenceContentItemId | ✅ |
| REFERENCE_GOAL_ID | ReferenceGoalId | ✅ |
| REQUEST_CONTEXT | RequestContext | ✅ |
| REQUESTER_PERSON_ID | RequesterPersonId | ✅ |
| START_DATE | StartDate | ✅ |
| STATUS_CODE | StatusCode | ✅ |
| SUCCESS_CRITERIA | SuccessCriteria | ✅ |
| SUCCESS_CRITERIA_TEXT | SuccessCriteriaText | ✅ |
| TARGET_COMPLETION_DATE | TargetCompletionDate | ✅ |
| VERSION_DATE | VersionDate | ✅ |

### [[goalitempvo|GoalItemPVO]] (HCM · BICC: 18/39)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_TO_HIERARCHY_FLAG | GoalPEOAccessToHierarchyFlag | — |
| ACTUAL_COMPLETION_DATE | GoalPEOActualCompletionDate | ✅ |
| ALLOW_KEY_ATTR_UPDATE_FLAG | GoalPEOAllowKeyAttrUpdateFlag | — |
| APPROVAL_STATUS_CODE | GoalPEOApprovalStatusCode | — |
| ASSIGNED_BY_PERSON_ID | GoalPEOAssignedByPersonId | — |
| ASSIGNMENT_ID | GoalPEOAssignmentId | — |
| BUSINESS_GROUP_ID | GoalPEOBusinessGroupId | — |
| CATEGORY_CODE | GoalPEOCategoryCode | ✅ |
| COMMENTS | GoalPEOComments | — |
| COMMENTS_TEXT | GoalPEOCommentsText | ✅ |
| DESCRIPTION | GoalPEODescription | ✅ |
| GOAL_ID | GoalId | ✅ |
| GOAL_NAME | GoalPEOGoalName | ✅ |
| GOAL_SOURCE_CODE | GoalPEOGoalSourceCode | ✅ |
| GOAL_TYPE_CODE | GoalPEOGoalTypeCode | ✅ |
| GOAL_URL | GoalPEOGoalUrl | ✅ |
| GOAL_VERSION_TYPE_CODE | GoalPEOGoalVersionTypeCode | — |
| HRCHY_ACCESS_GRANT_DATE | GoalPEOHrchyAccessGrantDate | — |
| INCLUDE_IN_PERFDOC_FLAG | GoalPEOIncludeInPerfdocFlag | — |
| LAST_UPDATE_DATE | GoalPEOLastUpdateDate | ✅ |
| LEVEL_CODE | GoalPEOLevelCode | ✅ |
| LEVEL_MEANING | GoalPEOLevelMeaning | ✅ |
| MASS_REQUEST_ID | GoalPEOMassRequestId | — |
| ORGANIZATION_ID | GoalPEOOrganizationId | — |
| PERCENT_COMPLETE_CODE | GoalPEOPercentCompleteCode | ✅ |
| PERSON_ID | GoalPEOPersonId | — |
| PRIORITY_CODE | GoalPEOPriorityCode | ✅ |
| PRIVATE_FLAG | GoalPEOPrivateFlag | — |
| PUBLISH_DATE | GoalPEOPublishDate | — |
| PUBLISHED_FLAG | GoalPEOPublishedFlag | — |
| REFERENCE_CONTENT_ITEM_ID | GoalPEOReferenceContentItemId | — |
| REFERENCE_GOAL_ID | GoalPEOReferenceGoalId | — |
| REQUESTER_PERSON_ID | GoalPEORequesterPersonId | — |
| START_DATE | GoalPEOStartDate | ✅ |
| STATUS_CODE | GoalPEOStatusCode | ✅ |
| SUCCESS_CRITERIA | GoalPEOSuccessCriteria | — |
| SUCCESS_CRITERIA_TEXT | GoalPEOSuccessCriteriaText | ✅ |
| TARGET_COMPLETION_DATE | GoalPEOTargetCompletionDate | ✅ |
| VERSION_DATE | GoalPEOVersionDate | — |

### [[goalppvo1|GoalPPVO1]] (HCM · BICC: 4/65)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_TO_HIERARCHY_FLAG | GoalPEOAccessToHierarchyFlag | — |
| ACTIVE_FLAG | GoalPEOActiveFlag | — |
| ACTUAL_COMPLETION_DATE | GoalPEOActualCompletionDate | — |
| ACTUAL_VALUE | GoalPEOActualValue | — |
| ALLOW_DEL_GOAL_FLAG | GoalPEOAllowDelGoalFlag | — |
| ALLOW_KEY_ATTR_UPDATE_FLAG | GoalPEOAllowKeyAttrUpdateFlag | — |
| APPROVAL_STATUS_CODE | GoalPEOApprovalStatusCode | — |
| APPROVER_RESPONSE_CODE | GoalPEOApproverResponseCode | — |
| ASSIGNED_BY_PERSON_ID | GoalPEOAssignedByPersonId | — |
| ASSIGNMENT_ID | GoalPEOAssignmentId | — |
| ATTRIBUTE_CATEGORY | GoalPEOAttributeCategory | — |
| BUSINESS_GROUP_ID | GoalPEOBusinessGroupId | — |
| CATEGORY_CODE | GoalPEOCategoryCode | — |
| COMMENTS | GoalPEOComments | — |
| COMMENTS_TEXT | GoalPEOCommentsText | ✅ |
| CREATED_BY | GoalPEOCreatedBy | — |
| CREATION_DATE | GoalPEOCreationDate | — |
| DESCRIPTION | GoalPEODescription | — |
| GOAL_ACCESS_LEVEL_CODE | GoalPEOGoalAccessLevelCode | — |
| GOAL_APPROVAL_STATE | GoalPEOGoalApprovalState | — |
| GOAL_EXT_ID | GoalPEOGoalExtId | — |
| GOAL_ID | GoalId | ✅ |
| GOAL_NAME | GoalPEOGoalName | — |
| GOAL_SOURCE_CODE | GoalPEOGoalSourceCode | — |
| GOAL_SUB_TYPE_CODE | GoalPEOGoalSubTypeCode | — |
| GOAL_TYPE_CODE | GoalPEOGoalTypeCode | — |
| GOAL_URL | GoalPEOGoalUrl | — |
| GOAL_VERSION_TYPE_CODE | GoalPEOGoalVersionTypeCode | — |
| HRCHY_ACCESS_GRANT_DATE | GoalPEOHrchyAccessGrantDate | — |
| INCLUDE_IN_PERFDOC_FLAG | GoalPEOIncludeInPerfdocFlag | — |
| LAST_MODIFIED_BY | GoalPEOLastModifiedBy | — |
| LAST_MODIFIED_DATE | GoalPEOLastModifiedDate | — |
| LAST_UPDATE_DATE | GoalPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | GoalPEOLastUpdatedBy | — |
| LEVEL_CODE | GoalPEOLevelCode | — |
| LEVEL_MEANING | GoalPEOLevelMeaning | — |
| LONG_DESCRIPTION | GoalPEOLongDescription | — |
| MASS_REQUEST_ID | GoalPEOMassRequestId | — |
| MEASURE_CALC_RULE_CODE | GoalPEOMeasureCalcRuleCode | — |
| MEASURE_COMMENTS | GoalPEOMeasureComments | — |
| MEASURE_NAME | GoalPEOMeasureName | — |
| MEASURE_TYPE_CODE | GoalPEOMeasureTypeCode | — |
| OBJECT_VERSION_NUMBER | GoalPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationId | — |
| PERCENT_COMPLETE_CODE | GoalPEOPercentCompleteCode | — |
| PERSON_ID | GoalPEOPersonId | — |
| PREVIOUS_STATE_GOAL_ID | GoalPEOPreviousStateGoalId | — |
| PRIORITY_CODE | GoalPEOPriorityCode | — |
| PRIVATE_FLAG | GoalPEOPrivateFlag | — |
| PUBLISH_DATE | GoalPEOPublishDate | — |
| PUBLISHED_FLAG | GoalPEOPublishedFlag | — |
| REFERENCE_CONTENT_ITEM_ID | GoalPEOReferenceContentItemId | — |
| REFERENCE_GOAL_ID | GoalPEOReferenceGoalId | — |
| REQUEST_CONTEXT | GoalPEORequestContext | — |
| REQUESTER_PERSON_ID | GoalPEORequesterPersonId | — |
| START_DATE | GoalPEOStartDate | — |
| STATUS_CODE | GoalPEOStatusCode | — |
| SUCCESS_CRITERIA | GoalPEOSuccessCriteria | — |
| SUCCESS_CRITERIA_TEXT | GoalPEOSuccessCriteriaText | ✅ |
| TARGET_COMPLETION_DATE | GoalPEOTargetCompletionDate | — |
| TARGET_TYPE | GoalPEOTargetType | — |
| TARGET_VALUE | GoalPEOTargetValue | — |
| UOM_CODE | GoalPEOUomCode | — |
| VERSION_DATE | GoalPEOVersionDate | — |

### [[goalpvo_copy|GoalPVO_Copy]] (HCM · BICC: 3/64)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_TO_HIERARCHY_FLAG | GoalPEOAccessToHierarchyFlag | — |
| ACTIVE_FLAG | GoalPEOActiveFlag | — |
| ACTUAL_COMPLETION_DATE | GoalPEOActualCompletionDate | — |
| ACTUAL_VALUE | GoalPEOActualValue | — |
| ALLOW_KEY_ATTR_UPDATE_FLAG | GoalPEOAllowKeyAttrUpdateFlag | — |
| APPROVAL_STATUS_CODE | GoalPEOApprovalStatusCode | — |
| APPROVER_RESPONSE_CODE | GoalPEOApproverResponseCode | — |
| ASSIGNED_BY_PERSON_ID | GoalPEOAssignedByPersonId | — |
| ASSIGNMENT_ID | GoalPEOAssignmentId | — |
| ATTRIBUTE_CATEGORY | GoalPEOAttributeCategory | — |
| BUSINESS_GROUP_ID | GoalPEOBusinessGroupId | — |
| CATEGORY_CODE | GoalPEOCategoryCode | — |
| COMMENTS | GoalPEOComments | — |
| COMMENTS_TEXT | GoalPEOCommentsText | — |
| CREATED_BY | GoalPEOCreatedBy | — |
| CREATION_DATE | GoalPEOCreationDate | — |
| DESCRIPTION | GoalPEODescription | — |
| GOAL_ACCESS_LEVEL_CODE | GoalPEOGoalAccessLevelCode | — |
| GOAL_APPROVAL_STATE | GoalPEOGoalApprovalState | — |
| GOAL_EXT_ID | GoalPEOGoalExtId | — |
| GOAL_ID | GoalId | ✅ |
| GOAL_NAME | GoalPEOGoalName | ✅ |
| GOAL_SOURCE_CODE | GoalPEOGoalSourceCode | — |
| GOAL_SUB_TYPE_CODE | GoalPEOGoalSubTypeCode | — |
| GOAL_TYPE_CODE | GoalPEOGoalTypeCode | — |
| GOAL_URL | GoalPEOGoalUrl | — |
| GOAL_VERSION_TYPE_CODE | GoalPEOGoalVersionTypeCode | — |
| HRCHY_ACCESS_GRANT_DATE | GoalPEOHrchyAccessGrantDate | — |
| INCLUDE_IN_PERFDOC_FLAG | GoalPEOIncludeInPerfdocFlag | — |
| LAST_MODIFIED_BY | GoalPEOLastModifiedBy | — |
| LAST_MODIFIED_DATE | GoalPEOLastModifiedDate | — |
| LAST_UPDATE_DATE | GoalPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | GoalPEOLastUpdatedBy | — |
| LEVEL_CODE | GoalPEOLevelCode | — |
| LEVEL_MEANING | GoalPEOLevelMeaning | — |
| LONG_DESCRIPTION | GoalPEOLongDescription | — |
| MASS_REQUEST_ID | GoalPEOMassRequestId | — |
| MEASURE_CALC_RULE_CODE | GoalPEOMeasureCalcRuleCode | — |
| MEASURE_COMMENTS | GoalPEOMeasureComments | — |
| MEASURE_NAME | GoalPEOMeasureName | — |
| MEASURE_TYPE_CODE | GoalPEOMeasureTypeCode | — |
| OBJECT_VERSION_NUMBER | GoalPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationId | — |
| PERCENT_COMPLETE_CODE | GoalPEOPercentCompleteCode | — |
| PERSON_ID | GoalPEOPersonId | — |
| PREVIOUS_STATE_GOAL_ID | GoalPEOPreviousStateGoalId | — |
| PRIORITY_CODE | GoalPEOPriorityCode | — |
| PRIVATE_FLAG | GoalPEOPrivateFlag | — |
| PUBLISH_DATE | GoalPEOPublishDate | — |
| PUBLISHED_FLAG | GoalPEOPublishedFlag | — |
| REFERENCE_CONTENT_ITEM_ID | GoalPEOReferenceContentItemId | — |
| REFERENCE_GOAL_ID | GoalPEOReferenceGoalId | — |
| REQUEST_CONTEXT | GoalPEORequestContext | — |
| REQUESTER_PERSON_ID | GoalPEORequesterPersonId | — |
| START_DATE | GoalPEOStartDate | — |
| STATUS_CODE | GoalPEOStatusCode | — |
| SUCCESS_CRITERIA | GoalPEOSuccessCriteria | — |
| SUCCESS_CRITERIA_TEXT | GoalPEOSuccessCriteriaText | — |
| TARGET_COMPLETION_DATE | GoalPEOTargetCompletionDate | — |
| TARGET_TYPE | GoalPEOTargetType | — |
| TARGET_VALUE | GoalPEOTargetValue | — |
| UOM_CODE | GoalPEOUomCode | — |
| VERSION_DATE | GoalPEOVersionDate | — |

### [[goalpvodescriptionlookup|GoalPVODescriptionLookup]] (HCM · BICC: 3/129)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_TO_HIERARCHY_FLAG | GoalPEOAccessToHierarchyFlag | — |
| ACTIVE_FLAG | ActiveFlag | — |
| ACTUAL_COMPLETION_DATE | GoalPEOActualCompletionDate | — |
| ACTUAL_VALUE | GoalPEOActualValue | — |
| ALLOW_KEY_ATTR_UPDATE_FLAG | GoalPEOAllowKeyAttrUpdateFlag | — |
| APPROVAL_STATUS_CODE | GoalPEOApprovalStatusCode | — |
| APPROVER_RESPONSE_CODE | ApproverResponseCode | — |
| ASSIGNED_BY_PERSON_ID | GoalPEOAssignedByPersonId | — |
| ASSIGNMENT_ID | GoalPEOAssignmentId | — |
| ATTRIBUTE1 | Attribute1 | — |
| ATTRIBUTE10 | Attribute10 | — |
| ATTRIBUTE11 | Attribute11 | — |
| ATTRIBUTE12 | Attribute12 | — |
| ATTRIBUTE13 | Attribute13 | — |
| ATTRIBUTE14 | Attribute14 | — |
| ATTRIBUTE15 | Attribute15 | — |
| ATTRIBUTE16 | Attribute16 | — |
| ATTRIBUTE17 | Attribute17 | — |
| ATTRIBUTE18 | Attribute18 | — |
| ATTRIBUTE19 | Attribute19 | — |
| ATTRIBUTE2 | Attribute2 | — |
| ATTRIBUTE20 | Attribute20 | — |
| ATTRIBUTE21 | Attribute21 | — |
| ATTRIBUTE22 | Attribute22 | — |
| ATTRIBUTE23 | Attribute23 | — |
| ATTRIBUTE24 | Attribute24 | — |
| ATTRIBUTE25 | Attribute25 | — |
| ATTRIBUTE26 | Attribute26 | — |
| ATTRIBUTE27 | Attribute27 | — |
| ATTRIBUTE28 | Attribute28 | — |
| ATTRIBUTE29 | Attribute29 | — |
| ATTRIBUTE3 | Attribute3 | — |
| ATTRIBUTE30 | Attribute30 | — |
| ATTRIBUTE4 | Attribute4 | — |
| ATTRIBUTE5 | Attribute5 | — |
| ATTRIBUTE6 | Attribute6 | — |
| ATTRIBUTE7 | Attribute7 | — |
| ATTRIBUTE8 | Attribute8 | — |
| ATTRIBUTE9 | Attribute9 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory | — |
| ATTRIBUTE_DATE1 | AttributeDate1 | — |
| ATTRIBUTE_DATE10 | AttributeDate10 | — |
| ATTRIBUTE_DATE11 | AttributeDate11 | — |
| ATTRIBUTE_DATE12 | AttributeDate12 | — |
| ATTRIBUTE_DATE13 | AttributeDate13 | — |
| ATTRIBUTE_DATE14 | AttributeDate14 | — |
| ATTRIBUTE_DATE15 | AttributeDate15 | — |
| ATTRIBUTE_DATE2 | AttributeDate2 | — |
| ATTRIBUTE_DATE3 | AttributeDate3 | — |
| ATTRIBUTE_DATE4 | AttributeDate4 | — |
| ATTRIBUTE_DATE5 | AttributeDate5 | — |
| ATTRIBUTE_DATE6 | AttributeDate6 | — |
| ATTRIBUTE_DATE7 | AttributeDate7 | — |
| ATTRIBUTE_DATE8 | AttributeDate8 | — |
| ATTRIBUTE_DATE9 | AttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber9 | — |
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| CATEGORY_CODE | GoalPEOCategoryCode | — |
| COMMENTS | GoalPEOComments | — |
| COMMENTS_TEXT | GoalPEOCommentsText | — |
| CREATED_BY | GoalPEOCreatedBy | — |
| CREATION_DATE | GoalPEOCreationDate | — |
| DESCRIPTION | GoalPEODescription | — |
| GOAL_ACCESS_LEVEL_CODE | GoalAccessLevelCode | — |
| GOAL_APPROVAL_STATE | GoalPEOGoalApprovalState | — |
| GOAL_EXT_ID | GoalExtId | — |
| GOAL_ID | GoalId | ✅ |
| GOAL_NAME | GoalPEOGoalName | — |
| GOAL_SOURCE_CODE | GoalPEOGoalSourceCode | — |
| GOAL_SUB_TYPE_CODE | GoalSubTypeCode | — |
| GOAL_TYPE_CODE | GoalPEOGoalTypeCode | — |
| GOAL_URL | GoalPEOGoalUrl | — |
| GOAL_VERSION_TYPE_CODE | GoalPEOGoalVersionTypeCode | — |
| HRCHY_ACCESS_GRANT_DATE | GoalPEOHrchyAccessGrantDate | — |
| INCLUDE_IN_PERFDOC_FLAG | GoalPEOIncludeInPerfdocFlag | — |
| LAST_MODIFIED_BY | LastModifiedBy | — |
| LAST_MODIFIED_DATE | LastModifiedDate | — |
| LAST_UPDATE_DATE | GoalPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | GoalPEOLastUpdatedBy | — |
| LEVEL_CODE | GoalPEOLevelCode | — |
| LEVEL_MEANING | GoalPEOLevelMeaning | — |
| LONG_DESCRIPTION | GoalPEOLongDescription | ✅ |
| MASS_REQUEST_ID | GoalPEOMassRequestId | — |
| MEASURE_CALC_RULE_CODE | MeasureCalcRuleCode | — |
| MEASURE_COMMENTS | GoalPEOMeasureComments | — |
| MEASURE_NAME | GoalPEOMeasureName | — |
| MEASURE_TYPE_CODE | GoalPEOMeasureTypeCode | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationId | — |
| PERCENT_COMPLETE_CODE | GoalPEOPercentCompleteCode | — |
| PERSON_ID | PersonId | — |
| PREVIOUS_STATE_GOAL_ID | PreviousStateGoalId | — |
| PRIORITY_CODE | GoalPEOPriorityCode | — |
| PRIVATE_FLAG | GoalPEOPrivateFlag | — |
| PUBLISH_DATE | PublishDate | — |
| PUBLISHED_FLAG | PublishedFlag | — |
| REFERENCE_CONTENT_ITEM_ID | GoalPEOReferenceContentItemId | — |
| REFERENCE_GOAL_ID | GoalPEOReferenceGoalId | — |
| REQUEST_CONTEXT | RequestContext | — |
| REQUESTER_PERSON_ID | GoalPEORequesterPersonId | — |
| START_DATE | GoalPEOStartDate | — |
| STATUS_CODE | GoalPEOStatusCode | — |
| SUCCESS_CRITERIA | GoalPEOSuccessCriteria | — |
| SUCCESS_CRITERIA_TEXT | GoalPEOSuccessCriteriaText | — |
| TARGET_COMPLETION_DATE | GoalPEOTargetCompletionDate | — |
| TARGET_TYPE | GoalPEOTargetType | — |
| TARGET_VALUE | GoalPEOTargetValue | — |
| UOM_CODE | GoalPEOUomCode | — |
| VERSION_DATE | GoalPEOVersionDate | — |

### [[goalstatusoverviewpvo|GoalStatusOverviewPVO]] (HCM · BICC: 33/63)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_TO_HIERARCHY_FLAG | GoalPEOAccessToHierarchyFlag | ✅ |
| ACTIVE_FLAG | GoalPEOActiveFlag | — |
| ACTUAL_COMPLETION_DATE | GoalPEOActualCompletionDate | ✅ |
| ACTUAL_VALUE | GoalPEOActualValue | — |
| ALLOW_KEY_ATTR_UPDATE_FLAG | GoalPEOAllowKeyAttrUpdateFlag | ✅ |
| APPROVAL_STATUS_CODE | GoalPEOApprovalStatusCode | ✅ |
| APPROVER_RESPONSE_CODE | GoalPEOApproverResponseCode | — |
| ASSIGNED_BY_PERSON_ID | GoalPEOAssignedByPersonId | — |
| ASSIGNMENT_ID | GoalPEOAssignmentId | — |
| ATTRIBUTE_CATEGORY | GoalPEOAttributeCategory | ✅ |
| BUSINESS_GROUP_ID | GoalPEOBusinessGroupId | — |
| CATEGORY_CODE | GoalPEOCategoryCode | — |
| COMMENTS | GoalPEOComments | — |
| COMMENTS_TEXT | GoalPEOCommentsText | ✅ |
| CREATED_BY | GoalPEOCreatedBy | ✅ |
| CREATION_DATE | GoalPEOCreationDate | ✅ |
| DESCRIPTION | GoalPEODescription | ✅ |
| GOAL_ACCESS_LEVEL_CODE | GoalPEOGoalAccessLevelCode | — |
| GOAL_APPROVAL_STATE | GoalPEOGoalApprovalState | — |
| GOAL_EXT_ID | GoalPEOGoalExtId | — |
| GOAL_ID | GoalId | ✅ |
| GOAL_NAME | GoalPEOGoalName | ✅ |
| GOAL_SOURCE_CODE | GoalPEOGoalSourceCode | ✅ |
| GOAL_SUB_TYPE_CODE | GoalPEOGoalSubTypeCode | — |
| GOAL_TYPE_CODE | GoalPEOGoalTypeCode | ✅ |
| GOAL_URL | GoalPEOGoalUrl | ✅ |
| GOAL_VERSION_TYPE_CODE | GoalPEOGoalVersionTypeCode | ✅ |
| HRCHY_ACCESS_GRANT_DATE | GoalPEOHrchyAccessGrantDate | ✅ |
| INCLUDE_IN_PERFDOC_FLAG | GoalPEOIncludeInPerfdocFlag | ✅ |
| LAST_MODIFIED_DATE | GoalPEOLastModifiedDate | ✅ |
| LAST_UPDATE_DATE | GoalPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | GoalPEOLastUpdatedBy | ✅ |
| LEVEL_CODE | GoalPEOLevelCode | — |
| LEVEL_MEANING | GoalPEOLevelMeaning | ✅ |
| LONG_DESCRIPTION | GoalPEOLongDescription | — |
| MASS_REQUEST_ID | GoalPEOMassRequestId | — |
| MEASURE_CALC_RULE_CODE | GoalPEOMeasureCalcRuleCode | — |
| MEASURE_COMMENTS | GoalPEOMeasureComments | — |
| MEASURE_NAME | GoalPEOMeasureName | — |
| MEASURE_TYPE_CODE | GoalPEOMeasureTypeCode | — |
| OBJECT_VERSION_NUMBER | GoalPEOObjectVersionNumber | ✅ |
| ORGANIZATION_ID | GoalPEOOrganizationId | — |
| PERCENT_COMPLETE_CODE | GoalPEOPercentCompleteCode | ✅ |
| PERSON_ID | GoalPEOPersonId | ✅ |
| PREVIOUS_STATE_GOAL_ID | GoalPEOPreviousStateGoalId | — |
| PRIORITY_CODE | GoalPEOPriorityCode | ✅ |
| PRIVATE_FLAG | GoalPEOPrivateFlag | ✅ |
| PUBLISH_DATE | GoalPEOPublishDate | ✅ |
| PUBLISHED_FLAG | GoalPEOPublishedFlag | ✅ |
| REFERENCE_CONTENT_ITEM_ID | GoalPEOReferenceContentItemId | — |
| REFERENCE_GOAL_ID | GoalPEOReferenceGoalId | — |
| REQUEST_CONTEXT | GoalPEORequestContext | — |
| REQUESTER_PERSON_ID | GoalPEORequesterPersonId | — |
| START_DATE | GoalPEOStartDate | ✅ |
| STATUS_CODE | GoalPEOStatusCode | ✅ |
| SUCCESS_CRITERIA | GoalPEOSuccessCriteria | — |
| SUCCESS_CRITERIA_TEXT | GoalPEOSuccessCriteriaText | ✅ |
| TARGET_COMPLETION_DATE | GoalPEOTargetCompletionDate | ✅ |
| TARGET_TYPE | GoalPEOTargetType | — |
| TARGET_VALUE | GoalPEOTargetValue | — |
| UOM_CODE | GoalPEOUomCode | — |
| VERSION_DATE | GoalPEOVersionDate | ✅ |

### [[goaltargetoutcomeprofilespvo|GoalTargetOutcomeProfilesPVO]] (HCM · BICC: 4/38)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | GoalPEOActiveFlag | — |
| ACTUAL_COMPLETION_DATE | GoalPEOActualCompletionDate | ✅ |
| ACTUAL_VALUE | GoalPEOActualValue | — |
| ALLOW_KEY_ATTR_UPDATE_FLAG | GoalPEOAllowKeyAttrUpdateFlag | — |
| APPROVAL_STATUS_CODE | GoalPEOApprovalStatusCode | — |
| APPROVER_RESPONSE_CODE | GoalPEOApproverResponseCode | — |
| ASSIGNED_BY_PERSON_ID | GoalPEOAssignedByPersonId | — |
| ASSIGNMENT_ID | GoalPEOAssignmentId | ✅ |
| COMMENTS | GoalPEOComments | — |
| COMMENTS_TEXT | GoalPEOCommentsText | — |
| DESCRIPTION | GoalPEODescription | — |
| GOAL_ACCESS_LEVEL_CODE | GoalPEOGoalAccessLevelCode | — |
| GOAL_APPROVAL_STATE | GoalPEOGoalApprovalState | — |
| GOAL_ID | GoalId | ✅ |
| GOAL_NAME | GoalPEOGoalName | — |
| GOAL_SOURCE_CODE | GoalPEOGoalSourceCode | — |
| GOAL_SUB_TYPE_CODE | GoalPEOGoalSubTypeCode | — |
| GOAL_TYPE_CODE | GoalPEOGoalTypeCode | — |
| GOAL_URL | GoalPEOGoalUrl | — |
| GOAL_VERSION_TYPE_CODE | GoalPEOGoalVersionTypeCode | — |
| LEVEL_CODE | GoalPEOLevelCode | — |
| LEVEL_MEANING | GoalPEOLevelMeaning | — |
| LONG_DESCRIPTION | GoalPEOLongDescription | — |
| MEASURE_CALC_RULE_CODE | GoalPEOMeasureCalcRuleCode | — |
| MEASURE_COMMENTS | GoalPEOMeasureComments | — |
| MEASURE_NAME | GoalPEOMeasureName | — |
| ORGANIZATION_ID | GoalPEOOrganizationId | — |
| PERSON_ID | PersonId | ✅ |
| PRIORITY_CODE | GoalPEOPriorityCode | — |
| PUBLISHED_FLAG | GoalPEOPublishedFlag | — |
| REQUESTER_PERSON_ID | GoalPEORequesterPersonId | — |
| START_DATE | GoalPEOStartDate | — |
| STATUS_CODE | GoalPEOStatusCode | — |
| SUCCESS_CRITERIA | GoalPEOSuccessCriteria | — |
| SUCCESS_CRITERIA_TEXT | GoalPEOSuccessCriteriaText | — |
| TARGET_COMPLETION_DATE | GoalPEOTargetCompletionDate | — |
| TARGET_TYPE | GoalPEOTargetType | — |
| TARGET_VALUE | GoalPEOTargetValue | — |

### [[goalversionstatusoverviewpvo|GoalVersionStatusOverviewPVO]] (HCM · BICC: 33/63)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_TO_HIERARCHY_FLAG | GoalPEOAccessToHierarchyFlag | ✅ |
| ACTIVE_FLAG | GoalPEOActiveFlag | — |
| ACTUAL_COMPLETION_DATE | GoalPEOActualCompletionDate | ✅ |
| ACTUAL_VALUE | GoalPEOActualValue | — |
| ALLOW_KEY_ATTR_UPDATE_FLAG | GoalPEOAllowKeyAttrUpdateFlag | ✅ |
| APPROVAL_STATUS_CODE | GoalPEOApprovalStatusCode | ✅ |
| APPROVER_RESPONSE_CODE | GoalPEOApproverResponseCode | — |
| ASSIGNED_BY_PERSON_ID | GoalPEOAssignedByPersonId | — |
| ASSIGNMENT_ID | GoalPEOAssignmentId | — |
| ATTRIBUTE_CATEGORY | GoalPEOAttributeCategory | ✅ |
| BUSINESS_GROUP_ID | GoalPEOBusinessGroupId | — |
| CATEGORY_CODE | GoalPEOCategoryCode | — |
| COMMENTS | GoalPEOComments | — |
| COMMENTS_TEXT | GoalPEOCommentsText | ✅ |
| CREATED_BY | GoalPEOCreatedBy | ✅ |
| CREATION_DATE | GoalPEOCreationDate | ✅ |
| DESCRIPTION | GoalPEODescription | ✅ |
| GOAL_ACCESS_LEVEL_CODE | GoalPEOGoalAccessLevelCode | — |
| GOAL_APPROVAL_STATE | GoalPEOGoalApprovalState | — |
| GOAL_EXT_ID | GoalPEOGoalExtId | — |
| GOAL_ID | GoalId | ✅ |
| GOAL_NAME | GoalPEOGoalName | ✅ |
| GOAL_SOURCE_CODE | GoalPEOGoalSourceCode | ✅ |
| GOAL_SUB_TYPE_CODE | GoalPEOGoalSubTypeCode | — |
| GOAL_TYPE_CODE | GoalPEOGoalTypeCode | ✅ |
| GOAL_URL | GoalPEOGoalUrl | ✅ |
| GOAL_VERSION_TYPE_CODE | GoalPEOGoalVersionTypeCode | ✅ |
| HRCHY_ACCESS_GRANT_DATE | GoalPEOHrchyAccessGrantDate | ✅ |
| INCLUDE_IN_PERFDOC_FLAG | GoalPEOIncludeInPerfdocFlag | ✅ |
| LAST_MODIFIED_DATE | GoalPEOLastModifiedDate | ✅ |
| LAST_UPDATE_DATE | GoalPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | GoalPEOLastUpdatedBy | ✅ |
| LEVEL_CODE | GoalPEOLevelCode | — |
| LEVEL_MEANING | GoalPEOLevelMeaning | ✅ |
| LONG_DESCRIPTION | GoalPEOLongDescription | — |
| MASS_REQUEST_ID | GoalPEOMassRequestId | — |
| MEASURE_CALC_RULE_CODE | GoalPEOMeasureCalcRuleCode | — |
| MEASURE_COMMENTS | GoalPEOMeasureComments | — |
| MEASURE_NAME | GoalPEOMeasureName | — |
| MEASURE_TYPE_CODE | GoalPEOMeasureTypeCode | — |
| OBJECT_VERSION_NUMBER | GoalPEOObjectVersionNumber | ✅ |
| ORGANIZATION_ID | GoalPEOOrganizationId | — |
| PERCENT_COMPLETE_CODE | GoalPEOPercentCompleteCode | ✅ |
| PERSON_ID | GoalPEOPersonId | ✅ |
| PREVIOUS_STATE_GOAL_ID | GoalPEOPreviousStateGoalId | — |
| PRIORITY_CODE | GoalPEOPriorityCode | ✅ |
| PRIVATE_FLAG | GoalPEOPrivateFlag | ✅ |
| PUBLISH_DATE | GoalPEOPublishDate | ✅ |
| PUBLISHED_FLAG | GoalPEOPublishedFlag | ✅ |
| REFERENCE_CONTENT_ITEM_ID | GoalPEOReferenceContentItemId | — |
| REFERENCE_GOAL_ID | GoalPEOReferenceGoalId | — |
| REQUEST_CONTEXT | GoalPEORequestContext | — |
| REQUESTER_PERSON_ID | GoalPEORequesterPersonId | — |
| START_DATE | GoalPEOStartDate | ✅ |
| STATUS_CODE | GoalPEOStatusCode | ✅ |
| SUCCESS_CRITERIA | GoalPEOSuccessCriteria | — |
| SUCCESS_CRITERIA_TEXT | GoalPEOSuccessCriteriaText | ✅ |
| TARGET_COMPLETION_DATE | GoalPEOTargetCompletionDate | ✅ |
| TARGET_TYPE | GoalPEOTargetType | — |
| TARGET_VALUE | GoalPEOTargetValue | — |
| UOM_CODE | GoalPEOUomCode | — |
| VERSION_DATE | GoalPEOVersionDate | ✅ |

### [[managergoalpvo|ManagerGoalPVO]] (HCM · BICC: 12/90)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPROVAL_STATUS_CODE | GoalPEOApprovalStatusCode | ✅ |
| ATTRIBUTE1 | Attribute1 | — |
| ATTRIBUTE10 | Attribute10 | — |
| ATTRIBUTE11 | Attribute11 | — |
| ATTRIBUTE12 | Attribute12 | — |
| ATTRIBUTE13 | Attribute13 | — |
| ATTRIBUTE14 | Attribute14 | — |
| ATTRIBUTE15 | Attribute15 | — |
| ATTRIBUTE16 | Attribute16 | — |
| ATTRIBUTE17 | Attribute17 | — |
| ATTRIBUTE18 | Attribute18 | — |
| ATTRIBUTE19 | Attribute19 | — |
| ATTRIBUTE2 | Attribute2 | — |
| ATTRIBUTE20 | Attribute20 | — |
| ATTRIBUTE21 | Attribute21 | — |
| ATTRIBUTE22 | Attribute22 | — |
| ATTRIBUTE23 | Attribute23 | — |
| ATTRIBUTE24 | Attribute24 | — |
| ATTRIBUTE25 | Attribute25 | — |
| ATTRIBUTE26 | Attribute26 | — |
| ATTRIBUTE27 | Attribute27 | — |
| ATTRIBUTE28 | Attribute28 | — |
| ATTRIBUTE29 | Attribute29 | — |
| ATTRIBUTE3 | Attribute3 | — |
| ATTRIBUTE30 | Attribute30 | — |
| ATTRIBUTE4 | Attribute4 | — |
| ATTRIBUTE5 | Attribute5 | — |
| ATTRIBUTE6 | Attribute6 | — |
| ATTRIBUTE7 | Attribute7 | — |
| ATTRIBUTE8 | Attribute8 | — |
| ATTRIBUTE9 | Attribute9 | — |
| ATTRIBUTE_DATE1 | AttributeDate1 | — |
| ATTRIBUTE_DATE10 | AttributeDate10 | — |
| ATTRIBUTE_DATE11 | AttributeDate11 | — |
| ATTRIBUTE_DATE12 | AttributeDate12 | — |
| ATTRIBUTE_DATE13 | AttributeDate13 | — |
| ATTRIBUTE_DATE14 | AttributeDate14 | — |
| ATTRIBUTE_DATE15 | AttributeDate15 | — |
| ATTRIBUTE_DATE2 | AttributeDate2 | — |
| ATTRIBUTE_DATE3 | AttributeDate3 | — |
| ATTRIBUTE_DATE4 | AttributeDate4 | — |
| ATTRIBUTE_DATE5 | AttributeDate5 | — |
| ATTRIBUTE_DATE6 | AttributeDate6 | — |
| ATTRIBUTE_DATE7 | AttributeDate7 | — |
| ATTRIBUTE_DATE8 | AttributeDate8 | — |
| ATTRIBUTE_DATE9 | AttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber9 | — |
| BUSINESS_GROUP_ID | GoalPEOBusinessGroupId | ✅ |
| CREATED_BY | GoalPEOCreatedBy | ✅ |
| CREATION_DATE | GoalPEOCreationDate | ✅ |
| GOAL_ACCESS_LEVEL_CODE | GoalAccessLevelCode | — |
| GOAL_APPROVAL_STATE | GoalPEOGoalApprovalState | — |
| GOAL_EXT_ID | GoalExtId | — |
| GOAL_ID | GoalId | ✅ |
| GOAL_SOURCE_CODE | GoalPEOGoalSourceCode | ✅ |
| GOAL_SUB_TYPE_CODE | GoalSubTypeCode | — |
| GOAL_VERSION_TYPE_CODE | GoalPEOGoalVersionTypeCode | ✅ |
| INCLUDE_IN_PERFDOC_FLAG | GoalPEOIncludeInPerfdocFlag | — |
| LAST_MODIFIED_BY | LastModifiedBy | — |
| LAST_MODIFIED_DATE | LastModifiedDate | — |
| LAST_UPDATE_DATE | GoalPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | GoalPEOLastUpdatedBy | ✅ |
| LONG_DESCRIPTION | GoalPEOLongDescription | — |
| MASS_REQUEST_ID | GoalPEOMassRequestId | ✅ |
| MEASURE_CALC_RULE_CODE | MeasureCalcRuleCode | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PUBLISH_DATE | PublishDate | — |
| PUBLISHED_FLAG | PublishedFlag | — |
| REFERENCE_CONTENT_ITEM_ID | GoalPEOReferenceContentItemId | ✅ |
| REQUEST_CONTEXT | RequestContext | — |

### [[organizationgoalpvo|OrganizationGoalPVO]] (HCM · BICC: 43/130)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_TO_HIERARCHY_FLAG | GoalPEOAccessToHierarchyFlag | ✅ |
| ACTIVE_FLAG | GoalPEOActiveFlag | — |
| ACTUAL_COMPLETION_DATE | GoalPEOActualCompletionDate | ✅ |
| ACTUAL_VALUE | GoalPEOActualValue | — |
| ALLOW_KEY_ATTR_UPDATE_FLAG | GoalPEOAllowKeyAttrUpdateFlag | ✅ |
| APPROVAL_STATUS_CODE | GoalPEOApprovalStatusCode | ✅ |
| APPROVER_RESPONSE_CODE | GoalPEOApproverResponseCode | — |
| ASSIGNED_BY_PERSON_ID | GoalPEOAssignedByPersonId | ✅ |
| ASSIGNMENT_ID | GoalPEOAssignmentId | ✅ |
| ATTRIBUTE1 | Attribute110 | — |
| ATTRIBUTE10 | Attribute101 | — |
| ATTRIBUTE11 | Attribute111 | — |
| ATTRIBUTE12 | Attribute121 | — |
| ATTRIBUTE13 | Attribute131 | — |
| ATTRIBUTE14 | Attribute141 | — |
| ATTRIBUTE15 | Attribute151 | — |
| ATTRIBUTE16 | Attribute161 | — |
| ATTRIBUTE17 | Attribute171 | — |
| ATTRIBUTE18 | Attribute181 | — |
| ATTRIBUTE19 | Attribute191 | — |
| ATTRIBUTE2 | Attribute210 | — |
| ATTRIBUTE20 | Attribute201 | — |
| ATTRIBUTE21 | Attribute211 | — |
| ATTRIBUTE22 | Attribute221 | — |
| ATTRIBUTE23 | Attribute231 | — |
| ATTRIBUTE24 | Attribute241 | — |
| ATTRIBUTE25 | Attribute251 | — |
| ATTRIBUTE26 | Attribute261 | — |
| ATTRIBUTE27 | Attribute271 | — |
| ATTRIBUTE28 | Attribute281 | — |
| ATTRIBUTE29 | Attribute291 | — |
| ATTRIBUTE3 | Attribute31 | — |
| ATTRIBUTE30 | Attribute301 | — |
| ATTRIBUTE4 | Attribute41 | — |
| ATTRIBUTE5 | Attribute51 | — |
| ATTRIBUTE6 | Attribute61 | — |
| ATTRIBUTE7 | Attribute71 | — |
| ATTRIBUTE8 | Attribute81 | — |
| ATTRIBUTE9 | Attribute91 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory1 | — |
| ATTRIBUTE_CATEGORY | GoalPEOAttributeCategory | ✅ |
| ATTRIBUTE_DATE1 | AttributeDate16 | — |
| ATTRIBUTE_DATE10 | AttributeDate101 | — |
| ATTRIBUTE_DATE11 | AttributeDate111 | — |
| ATTRIBUTE_DATE12 | AttributeDate121 | — |
| ATTRIBUTE_DATE13 | AttributeDate131 | — |
| ATTRIBUTE_DATE14 | AttributeDate141 | — |
| ATTRIBUTE_DATE15 | AttributeDate151 | — |
| ATTRIBUTE_DATE2 | AttributeDate21 | — |
| ATTRIBUTE_DATE3 | AttributeDate31 | — |
| ATTRIBUTE_DATE4 | AttributeDate41 | — |
| ATTRIBUTE_DATE5 | AttributeDate51 | — |
| ATTRIBUTE_DATE6 | AttributeDate61 | — |
| ATTRIBUTE_DATE7 | AttributeDate71 | — |
| ATTRIBUTE_DATE8 | AttributeDate81 | — |
| ATTRIBUTE_DATE9 | AttributeDate91 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber110 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber101 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber111 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber121 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber131 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber141 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber151 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber161 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber171 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber181 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber191 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber21 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber201 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber31 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber41 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber51 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber61 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber71 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber81 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber91 | — |
| BUSINESS_GROUP_ID | GoalPEOBusinessGroupId | ✅ |
| CATEGORY_CODE | GoalPEOCategoryCode | ✅ |
| COMMENTS | GoalPEOComments | — |
| COMMENTS_TEXT | GoalPEOCommentsText | ✅ |
| CREATED_BY | GoalPEOCreatedBy | ✅ |
| CREATION_DATE | GoalPEOCreationDate | ✅ |
| DESCRIPTION | GoalPEODescription | ✅ |
| GOAL_ACCESS_LEVEL_CODE | GoalAccessLevelCode | — |
| GOAL_APPROVAL_STATE | GoalPEOGoalApprovalState | — |
| GOAL_EXT_ID | GoalExtId | — |
| GOAL_ID | GoalId | ✅ |
| GOAL_NAME | GoalPEOGoalName | ✅ |
| GOAL_SOURCE_CODE | GoalPEOGoalSourceCode | ✅ |
| GOAL_SUB_TYPE_CODE | GoalSubTypeCode | — |
| GOAL_TYPE_CODE | GoalPEOGoalTypeCode | ✅ |
| GOAL_URL | GoalPEOGoalUrl | ✅ |
| GOAL_VERSION_TYPE_CODE | GoalPEOGoalVersionTypeCode | ✅ |
| HRCHY_ACCESS_GRANT_DATE | GoalPEOHrchyAccessGrantDate | ✅ |
| INCLUDE_IN_PERFDOC_FLAG | GoalPEOIncludeInPerfdocFlag | ✅ |
| LAST_MODIFIED_BY | LastModifiedBy | — |
| LAST_MODIFIED_DATE | LastModifiedDate | — |
| LAST_UPDATE_DATE | GoalPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | GoalPEOLastUpdatedBy | ✅ |
| LEVEL_CODE | GoalPEOLevelCode | ✅ |
| LEVEL_MEANING | GoalPEOLevelMeaning | ✅ |
| LONG_DESCRIPTION | GoalPEOLongDescription | — |
| MASS_REQUEST_ID | GoalPEOMassRequestId | ✅ |
| MEASURE_CALC_RULE_CODE | MeasureCalcRuleCode | — |
| MEASURE_COMMENTS | GoalPEOMeasureComments | — |
| MEASURE_NAME | GoalPEOMeasureName | — |
| MEASURE_TYPE_CODE | GoalPEOMeasureTypeCode | — |
| OBJECT_VERSION_NUMBER | GoalPEOObjectVersionNumber | ✅ |
| ORGANIZATION_ID | GoalPEOOrganizationId | ✅ |
| PERCENT_COMPLETE_CODE | GoalPEOPercentCompleteCode | ✅ |
| PERSON_ID | GoalPEOPersonId | ✅ |
| PREVIOUS_STATE_GOAL_ID | GoalPEOPreviousStateGoalId | — |
| PRIORITY_CODE | GoalPEOPriorityCode | ✅ |
| PRIVATE_FLAG | GoalPEOPrivateFlag | ✅ |
| PUBLISH_DATE | GoalPEOPublishDate | ✅ |
| PUBLISHED_FLAG | GoalPEOPublishedFlag | ✅ |
| REFERENCE_CONTENT_ITEM_ID | GoalPEOReferenceContentItemId | ✅ |
| REFERENCE_GOAL_ID | GoalPEOReferenceGoalId | ✅ |
| REQUEST_CONTEXT | RequestContext | — |
| REQUESTER_PERSON_ID | GoalPEORequesterPersonId | ✅ |
| START_DATE | GoalPEOStartDate | ✅ |
| STATUS_CODE | GoalPEOStatusCode | ✅ |
| SUCCESS_CRITERIA | GoalPEOSuccessCriteria | — |
| SUCCESS_CRITERIA_TEXT | GoalPEOSuccessCriteriaText | ✅ |
| TARGET_COMPLETION_DATE | GoalPEOTargetCompletionDate | ✅ |
| TARGET_TYPE | GoalPEOTargetType | — |
| TARGET_VALUE | GoalPEOTargetValue | — |
| UOM_CODE | GoalPEOUomCode | — |
| VERSION_DATE | GoalPEOVersionDate | ✅ |

### [[performancegoalpvo|PerformanceGoalPVO]] (HCM · BICC: 51/65)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_TO_HIERARCHY_FLAG | GoalPEOAccessToHierarchyFlag | ✅ |
| ACTIVE_FLAG | GoalPEOActiveFlag | — |
| ACTUAL_COMPLETION_DATE | GoalPEOActualCompletionDate | ✅ |
| ACTUAL_VALUE | GoalPEOActualValue | — |
| ALLOW_DEL_GOAL_FLAG | GoalPEOAllowDelGoalFlag | — |
| ALLOW_KEY_ATTR_UPDATE_FLAG | GoalPEOAllowKeyAttrUpdateFlag | ✅ |
| APPROVAL_STATUS_CODE | GoalPEOApprovalStatusCode | ✅ |
| APPROVER_RESPONSE_CODE | GoalPEOApproverResponseCode | ✅ |
| ASSIGNED_BY_PERSON_ID | GoalPEOAssignedByPersonId | ✅ |
| ASSIGNMENT_ID | GoalPEOAssignmentId | ✅ |
| ATTRIBUTE_CATEGORY | GoalPEOAttributeCategory | ✅ |
| BUSINESS_GROUP_ID | GoalPEOBusinessGroupId | ✅ |
| CATEGORY_CODE | GoalPEOCategoryCode | ✅ |
| COMMENTS | GoalPEOComments | — |
| COMMENTS_TEXT | GoalPEOCommentsText | ✅ |
| CREATED_BY | GoalPEOCreatedBy | ✅ |
| CREATION_DATE | GoalPEOCreationDate | ✅ |
| DESCRIPTION | GoalPEODescription | ✅ |
| GOAL_ACCESS_LEVEL_CODE | GoalPEOGoalAccessLevelCode | ✅ |
| GOAL_APPROVAL_STATE | GoalPEOGoalApprovalState | ✅ |
| GOAL_EXT_ID | GoalPEOGoalExtId | ✅ |
| GOAL_ID | GoalId | ✅ |
| GOAL_NAME | GoalPEOGoalName | ✅ |
| GOAL_SOURCE_CODE | GoalPEOGoalSourceCode | ✅ |
| GOAL_SUB_TYPE_CODE | GoalPEOGoalSubTypeCode | ✅ |
| GOAL_TYPE_CODE | GoalPEOGoalTypeCode | ✅ |
| GOAL_URL | GoalPEOGoalUrl | ✅ |
| GOAL_VERSION_TYPE_CODE | GoalPEOGoalVersionTypeCode | ✅ |
| HRCHY_ACCESS_GRANT_DATE | GoalPEOHrchyAccessGrantDate | ✅ |
| INCLUDE_IN_PERFDOC_FLAG | GoalPEOIncludeInPerfdocFlag | ✅ |
| LAST_MODIFIED_BY | GoalPEOLastModifiedBy | — |
| LAST_MODIFIED_DATE | GoalPEOLastModifiedDate | ✅ |
| LAST_UPDATE_DATE | GoalPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | GoalPEOLastUpdatedBy | ✅ |
| LEVEL_CODE | GoalPEOLevelCode | ✅ |
| LEVEL_MEANING | GoalPEOLevelMeaning | ✅ |
| LONG_DESCRIPTION | GoalPEOLongDescription | — |
| MASS_REQUEST_ID | GoalPEOMassRequestId | ✅ |
| MEASURE_CALC_RULE_CODE | GoalPEOMeasureCalcRuleCode | ✅ |
| MEASURE_COMMENTS | GoalPEOMeasureComments | — |
| MEASURE_NAME | GoalPEOMeasureName | — |
| MEASURE_TYPE_CODE | GoalPEOMeasureTypeCode | — |
| OBJECT_VERSION_NUMBER | GoalPEOObjectVersionNumber | ✅ |
| ORGANIZATION_ID | OrganizationId | ✅ |
| PERCENT_COMPLETE_CODE | GoalPEOPercentCompleteCode | ✅ |
| PERSON_ID | GoalPEOPersonId | ✅ |
| PREVIOUS_STATE_GOAL_ID | GoalPEOPreviousStateGoalId | — |
| PRIORITY_CODE | GoalPEOPriorityCode | ✅ |
| PRIVATE_FLAG | GoalPEOPrivateFlag | ✅ |
| PUBLISH_DATE | GoalPEOPublishDate | ✅ |
| PUBLISHED_FLAG | GoalPEOPublishedFlag | ✅ |
| REFERENCE_CONTENT_ITEM_ID | GoalPEOReferenceContentItemId | ✅ |
| REFERENCE_GOAL_ID | GoalPEOReferenceGoalId | ✅ |
| REQUEST_CONTEXT | GoalPEORequestContext | ✅ |
| REQUESTER_PERSON_ID | GoalPEORequesterPersonId | ✅ |
| START_DATE | GoalPEOStartDate | ✅ |
| STATUS_CODE | GoalPEOStatusCode | ✅ |
| SUCCESS_CRITERIA | GoalPEOSuccessCriteria | — |
| SUCCESS_CRITERIA_TEXT | GoalPEOSuccessCriteriaText | ✅ |
| TARGET_COMPLETION_DATE | GoalPEOTargetCompletionDate | ✅ |
| TARGET_TYPE | GoalPEOTargetType | — |
| TARGET_VALUE | GoalPEOTargetValue | — |
| UOM_CODE | GoalPEOUomCode | — |
| VERSION_DATE | GoalPEOVersionDate | ✅ |

### [[performancegoalpvoviewall|PerformanceGoalPVOViewAll]] (HCM · BICC: 51/65)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_TO_HIERARCHY_FLAG | GoalPEOAccessToHierarchyFlag | ✅ |
| ACTIVE_FLAG | GoalPEOActiveFlag | — |
| ACTUAL_COMPLETION_DATE | GoalPEOActualCompletionDate | ✅ |
| ACTUAL_VALUE | GoalPEOActualValue | — |
| ALLOW_DEL_GOAL_FLAG | GoalPEOAllowDelGoalFlag | — |
| ALLOW_KEY_ATTR_UPDATE_FLAG | GoalPEOAllowKeyAttrUpdateFlag | ✅ |
| APPROVAL_STATUS_CODE | GoalPEOApprovalStatusCode | ✅ |
| APPROVER_RESPONSE_CODE | GoalPEOApproverResponseCode | ✅ |
| ASSIGNED_BY_PERSON_ID | GoalPEOAssignedByPersonId | ✅ |
| ASSIGNMENT_ID | GoalPEOAssignmentId | ✅ |
| ATTRIBUTE_CATEGORY | GoalPEOAttributeCategory | ✅ |
| BUSINESS_GROUP_ID | GoalPEOBusinessGroupId | ✅ |
| CATEGORY_CODE | GoalPEOCategoryCode | ✅ |
| COMMENTS | GoalPEOComments | — |
| COMMENTS_TEXT | GoalPEOCommentsText | ✅ |
| CREATED_BY | GoalPEOCreatedBy | ✅ |
| CREATION_DATE | GoalPEOCreationDate | ✅ |
| DESCRIPTION | GoalPEODescription | ✅ |
| GOAL_ACCESS_LEVEL_CODE | GoalPEOGoalAccessLevelCode | ✅ |
| GOAL_APPROVAL_STATE | GoalPEOGoalApprovalState | ✅ |
| GOAL_EXT_ID | GoalPEOGoalExtId | ✅ |
| GOAL_ID | GoalId | ✅ |
| GOAL_NAME | GoalPEOGoalName | ✅ |
| GOAL_SOURCE_CODE | GoalPEOGoalSourceCode | ✅ |
| GOAL_SUB_TYPE_CODE | GoalPEOGoalSubTypeCode | ✅ |
| GOAL_TYPE_CODE | GoalPEOGoalTypeCode | ✅ |
| GOAL_URL | GoalPEOGoalUrl | ✅ |
| GOAL_VERSION_TYPE_CODE | GoalPEOGoalVersionTypeCode | ✅ |
| HRCHY_ACCESS_GRANT_DATE | GoalPEOHrchyAccessGrantDate | ✅ |
| INCLUDE_IN_PERFDOC_FLAG | GoalPEOIncludeInPerfdocFlag | ✅ |
| LAST_MODIFIED_BY | GoalPEOLastModifiedBy | — |
| LAST_MODIFIED_DATE | GoalPEOLastModifiedDate | ✅ |
| LAST_UPDATE_DATE | GoalPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | GoalPEOLastUpdatedBy | ✅ |
| LEVEL_CODE | GoalPEOLevelCode | ✅ |
| LEVEL_MEANING | GoalPEOLevelMeaning | ✅ |
| LONG_DESCRIPTION | GoalPEOLongDescription | — |
| MASS_REQUEST_ID | GoalPEOMassRequestId | ✅ |
| MEASURE_CALC_RULE_CODE | GoalPEOMeasureCalcRuleCode | ✅ |
| MEASURE_COMMENTS | GoalPEOMeasureComments | — |
| MEASURE_NAME | GoalPEOMeasureName | — |
| MEASURE_TYPE_CODE | GoalPEOMeasureTypeCode | — |
| OBJECT_VERSION_NUMBER | GoalPEOObjectVersionNumber | ✅ |
| ORGANIZATION_ID | OrganizationId | ✅ |
| PERCENT_COMPLETE_CODE | GoalPEOPercentCompleteCode | ✅ |
| PERSON_ID | GoalPEOPersonId | ✅ |
| PREVIOUS_STATE_GOAL_ID | GoalPEOPreviousStateGoalId | — |
| PRIORITY_CODE | GoalPEOPriorityCode | ✅ |
| PRIVATE_FLAG | GoalPEOPrivateFlag | ✅ |
| PUBLISH_DATE | GoalPEOPublishDate | ✅ |
| PUBLISHED_FLAG | GoalPEOPublishedFlag | ✅ |
| REFERENCE_CONTENT_ITEM_ID | GoalPEOReferenceContentItemId | ✅ |
| REFERENCE_GOAL_ID | GoalPEOReferenceGoalId | ✅ |
| REQUEST_CONTEXT | GoalPEORequestContext | ✅ |
| REQUESTER_PERSON_ID | GoalPEORequesterPersonId | ✅ |
| START_DATE | GoalPEOStartDate | ✅ |
| STATUS_CODE | GoalPEOStatusCode | ✅ |
| SUCCESS_CRITERIA | GoalPEOSuccessCriteria | — |
| SUCCESS_CRITERIA_TEXT | GoalPEOSuccessCriteriaText | ✅ |
| TARGET_COMPLETION_DATE | GoalPEOTargetCompletionDate | ✅ |
| TARGET_TYPE | GoalPEOTargetType | — |
| TARGET_VALUE | GoalPEOTargetValue | — |
| UOM_CODE | GoalPEOUomCode | — |
| VERSION_DATE | GoalPEOVersionDate | ✅ |

### [[performancegoalversionpvo|PerformanceGoalVersionPVO]] (HCM · BICC: 41/65)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_TO_HIERARCHY_FLAG | GoalPEOAccessToHierarchyFlag | ✅ |
| ACTIVE_FLAG | GoalPEOActiveFlag | — |
| ACTUAL_COMPLETION_DATE | GoalPEOActualCompletionDate | ✅ |
| ACTUAL_VALUE | GoalPEOActualValue | — |
| ALLOW_DEL_GOAL_FLAG | GoalPEOAllowDelGoalFlag | — |
| ALLOW_KEY_ATTR_UPDATE_FLAG | GoalPEOAllowKeyAttrUpdateFlag | ✅ |
| APPROVAL_STATUS_CODE | GoalPEOApprovalStatusCode | — |
| APPROVER_RESPONSE_CODE | GoalPEOApproverResponseCode | ✅ |
| ASSIGNED_BY_PERSON_ID | GoalPEOAssignedByPersonId | ✅ |
| ASSIGNMENT_ID | GoalPEOAssignmentId | ✅ |
| ATTRIBUTE_CATEGORY | GoalPEOAttributeCategory | — |
| BUSINESS_GROUP_ID | GoalPEOBusinessGroupId | ✅ |
| CATEGORY_CODE | GoalPEOCategoryCode | ✅ |
| COMMENTS | GoalPEOComments | — |
| COMMENTS_TEXT | GoalPEOCommentsText | ✅ |
| CREATED_BY | GoalPEOCreatedBy | ✅ |
| CREATION_DATE | GoalPEOCreationDate | ✅ |
| DESCRIPTION | GoalPEODescription | ✅ |
| GOAL_ACCESS_LEVEL_CODE | GoalPEOGoalAccessLevelCode | ✅ |
| GOAL_APPROVAL_STATE | GoalPEOGoalApprovalState | ✅ |
| GOAL_EXT_ID | GoalPEOGoalExtId | ✅ |
| GOAL_ID | GoalId | ✅ |
| GOAL_NAME | GoalPEOGoalName | ✅ |
| GOAL_SOURCE_CODE | GoalPEOGoalSourceCode | ✅ |
| GOAL_SUB_TYPE_CODE | GoalPEOGoalSubTypeCode | ✅ |
| GOAL_TYPE_CODE | GoalPEOGoalTypeCode | — |
| GOAL_URL | GoalPEOGoalUrl | ✅ |
| GOAL_VERSION_TYPE_CODE | GoalPEOGoalVersionTypeCode | ✅ |
| HRCHY_ACCESS_GRANT_DATE | GoalPEOHrchyAccessGrantDate | ✅ |
| INCLUDE_IN_PERFDOC_FLAG | GoalPEOIncludeInPerfdocFlag | — |
| LAST_MODIFIED_BY | GoalPEOLastModifiedBy | ✅ |
| LAST_MODIFIED_DATE | GoalPEOLastModifiedDate | ✅ |
| LAST_UPDATE_DATE | GoalPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | GoalPEOLastUpdatedBy | ✅ |
| LEVEL_CODE | GoalPEOLevelCode | ✅ |
| LEVEL_MEANING | GoalPEOLevelMeaning | ✅ |
| LONG_DESCRIPTION | GoalPEOLongDescription | — |
| MASS_REQUEST_ID | GoalPEOMassRequestId | — |
| MEASURE_CALC_RULE_CODE | GoalPEOMeasureCalcRuleCode | ✅ |
| MEASURE_COMMENTS | GoalPEOMeasureComments | — |
| MEASURE_NAME | GoalPEOMeasureName | — |
| MEASURE_TYPE_CODE | GoalPEOMeasureTypeCode | — |
| OBJECT_VERSION_NUMBER | GoalPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationId | ✅ |
| PERCENT_COMPLETE_CODE | GoalPEOPercentCompleteCode | ✅ |
| PERSON_ID | GoalPEOPersonId | ✅ |
| PREVIOUS_STATE_GOAL_ID | GoalPEOPreviousStateGoalId | — |
| PRIORITY_CODE | GoalPEOPriorityCode | ✅ |
| PRIVATE_FLAG | GoalPEOPrivateFlag | — |
| PUBLISH_DATE | GoalPEOPublishDate | — |
| PUBLISHED_FLAG | GoalPEOPublishedFlag | — |
| REFERENCE_CONTENT_ITEM_ID | GoalPEOReferenceContentItemId | ✅ |
| REFERENCE_GOAL_ID | GoalPEOReferenceGoalId | ✅ |
| REQUEST_CONTEXT | GoalPEORequestContext | — |
| REQUESTER_PERSON_ID | GoalPEORequesterPersonId | ✅ |
| START_DATE | GoalPEOStartDate | ✅ |
| STATUS_CODE | GoalPEOStatusCode | ✅ |
| SUCCESS_CRITERIA | GoalPEOSuccessCriteria | — |
| SUCCESS_CRITERIA_TEXT | GoalPEOSuccessCriteriaText | ✅ |
| TARGET_COMPLETION_DATE | GoalPEOTargetCompletionDate | ✅ |
| TARGET_TYPE | GoalPEOTargetType | — |
| TARGET_VALUE | GoalPEOTargetValue | — |
| UOM_CODE | GoalPEOUomCode | — |
| VERSION_DATE | GoalPEOVersionDate | ✅ |

### [[performancegoalversionpvoviewall|PerformanceGoalVersionPVOViewAll]] (HCM · BICC: 41/65)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_TO_HIERARCHY_FLAG | GoalPEOAccessToHierarchyFlag | ✅ |
| ACTIVE_FLAG | GoalPEOActiveFlag | — |
| ACTUAL_COMPLETION_DATE | GoalPEOActualCompletionDate | ✅ |
| ACTUAL_VALUE | GoalPEOActualValue | — |
| ALLOW_DEL_GOAL_FLAG | GoalPEOAllowDelGoalFlag | — |
| ALLOW_KEY_ATTR_UPDATE_FLAG | GoalPEOAllowKeyAttrUpdateFlag | ✅ |
| APPROVAL_STATUS_CODE | GoalPEOApprovalStatusCode | — |
| APPROVER_RESPONSE_CODE | GoalPEOApproverResponseCode | ✅ |
| ASSIGNED_BY_PERSON_ID | GoalPEOAssignedByPersonId | ✅ |
| ASSIGNMENT_ID | GoalPEOAssignmentId | ✅ |
| ATTRIBUTE_CATEGORY | GoalPEOAttributeCategory | — |
| BUSINESS_GROUP_ID | GoalPEOBusinessGroupId | ✅ |
| CATEGORY_CODE | GoalPEOCategoryCode | ✅ |
| COMMENTS | GoalPEOComments | — |
| COMMENTS_TEXT | GoalPEOCommentsText | ✅ |
| CREATED_BY | GoalPEOCreatedBy | ✅ |
| CREATION_DATE | GoalPEOCreationDate | ✅ |
| DESCRIPTION | GoalPEODescription | ✅ |
| GOAL_ACCESS_LEVEL_CODE | GoalPEOGoalAccessLevelCode | ✅ |
| GOAL_APPROVAL_STATE | GoalPEOGoalApprovalState | ✅ |
| GOAL_EXT_ID | GoalPEOGoalExtId | ✅ |
| GOAL_ID | GoalId | ✅ |
| GOAL_NAME | GoalPEOGoalName | ✅ |
| GOAL_SOURCE_CODE | GoalPEOGoalSourceCode | ✅ |
| GOAL_SUB_TYPE_CODE | GoalPEOGoalSubTypeCode | ✅ |
| GOAL_TYPE_CODE | GoalPEOGoalTypeCode | — |
| GOAL_URL | GoalPEOGoalUrl | ✅ |
| GOAL_VERSION_TYPE_CODE | GoalPEOGoalVersionTypeCode | ✅ |
| HRCHY_ACCESS_GRANT_DATE | GoalPEOHrchyAccessGrantDate | ✅ |
| INCLUDE_IN_PERFDOC_FLAG | GoalPEOIncludeInPerfdocFlag | — |
| LAST_MODIFIED_BY | GoalPEOLastModifiedBy | ✅ |
| LAST_MODIFIED_DATE | GoalPEOLastModifiedDate | ✅ |
| LAST_UPDATE_DATE | GoalPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | GoalPEOLastUpdatedBy | ✅ |
| LEVEL_CODE | GoalPEOLevelCode | ✅ |
| LEVEL_MEANING | GoalPEOLevelMeaning | ✅ |
| LONG_DESCRIPTION | GoalPEOLongDescription | — |
| MASS_REQUEST_ID | GoalPEOMassRequestId | — |
| MEASURE_CALC_RULE_CODE | GoalPEOMeasureCalcRuleCode | ✅ |
| MEASURE_COMMENTS | GoalPEOMeasureComments | — |
| MEASURE_NAME | GoalPEOMeasureName | — |
| MEASURE_TYPE_CODE | GoalPEOMeasureTypeCode | — |
| OBJECT_VERSION_NUMBER | GoalPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationId | ✅ |
| PERCENT_COMPLETE_CODE | GoalPEOPercentCompleteCode | ✅ |
| PERSON_ID | GoalPEOPersonId | ✅ |
| PREVIOUS_STATE_GOAL_ID | GoalPEOPreviousStateGoalId | — |
| PRIORITY_CODE | GoalPEOPriorityCode | ✅ |
| PRIVATE_FLAG | GoalPEOPrivateFlag | — |
| PUBLISH_DATE | GoalPEOPublishDate | — |
| PUBLISHED_FLAG | GoalPEOPublishedFlag | — |
| REFERENCE_CONTENT_ITEM_ID | GoalPEOReferenceContentItemId | ✅ |
| REFERENCE_GOAL_ID | GoalPEOReferenceGoalId | ✅ |
| REQUEST_CONTEXT | GoalPEORequestContext | — |
| REQUESTER_PERSON_ID | GoalPEORequesterPersonId | ✅ |
| START_DATE | GoalPEOStartDate | ✅ |
| STATUS_CODE | GoalPEOStatusCode | ✅ |
| SUCCESS_CRITERIA | GoalPEOSuccessCriteria | — |
| SUCCESS_CRITERIA_TEXT | GoalPEOSuccessCriteriaText | ✅ |
| TARGET_COMPLETION_DATE | GoalPEOTargetCompletionDate | ✅ |
| TARGET_TYPE | GoalPEOTargetType | — |
| TARGET_VALUE | GoalPEOTargetValue | — |
| UOM_CODE | GoalPEOUomCode | — |
| VERSION_DATE | GoalPEOVersionDate | ✅ |

### [[personalgoalpvo|PersonalGoalPVO]] (HCM · BICC: 20/65)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_TO_HIERARCHY_FLAG | GoalPEOAccessToHierarchyFlag | — |
| ACTIVE_FLAG | GoalPEOActiveFlag | — |
| ACTUAL_COMPLETION_DATE | GoalPEOActualCompletionDate | — |
| ACTUAL_VALUE | GoalPEOActualValue | ✅ |
| ALLOW_DEL_GOAL_FLAG | GoalPEOAllowDelGoalFlag | — |
| ALLOW_KEY_ATTR_UPDATE_FLAG | GoalPEOAllowKeyAttrUpdateFlag | — |
| APPROVAL_STATUS_CODE | GoalPEOApprovalStatusCode | — |
| APPROVER_RESPONSE_CODE | GoalPEOApproverResponseCode | — |
| ASSIGNED_BY_PERSON_ID | GoalPEOAssignedByPersonId | — |
| ASSIGNMENT_ID | GoalPEOAssignmentId | — |
| ATTRIBUTE_CATEGORY | GoalPEOAttributeCategory | — |
| BUSINESS_GROUP_ID | GoalPEOBusinessGroupId | — |
| CATEGORY_CODE | GoalPEOCategoryCode | ✅ |
| COMMENTS | GoalPEOComments | ✅ |
| COMMENTS_TEXT | GoalPEOCommentsText | — |
| CREATED_BY | GoalPEOCreatedBy | — |
| CREATION_DATE | GoalPEOCreationDate | — |
| DESCRIPTION | GoalPEODescription | ✅ |
| GOAL_ACCESS_LEVEL_CODE | GoalPEOGoalAccessLevelCode | — |
| GOAL_APPROVAL_STATE | GoalPEOGoalApprovalState | — |
| GOAL_EXT_ID | GoalPEOGoalExtId | — |
| GOAL_ID | GoalId | ✅ |
| GOAL_NAME | GoalPEOGoalName | ✅ |
| GOAL_SOURCE_CODE | GoalPEOGoalSourceCode | — |
| GOAL_SUB_TYPE_CODE | GoalPEOGoalSubTypeCode | — |
| GOAL_TYPE_CODE | GoalPEOGoalTypeCode | — |
| GOAL_URL | GoalPEOGoalUrl | ✅ |
| GOAL_VERSION_TYPE_CODE | GoalPEOGoalVersionTypeCode | — |
| HRCHY_ACCESS_GRANT_DATE | GoalPEOHrchyAccessGrantDate | — |
| INCLUDE_IN_PERFDOC_FLAG | GoalPEOIncludeInPerfdocFlag | — |
| LAST_MODIFIED_BY | GoalPEOLastModifiedBy | — |
| LAST_MODIFIED_DATE | GoalPEOLastModifiedDate | — |
| LAST_UPDATE_DATE | GoalPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | GoalPEOLastUpdatedBy | — |
| LEVEL_CODE | GoalPEOLevelCode | ✅ |
| LEVEL_MEANING | GoalPEOLevelMeaning | ✅ |
| LONG_DESCRIPTION | GoalPEOLongDescription | — |
| MASS_REQUEST_ID | GoalPEOMassRequestId | — |
| MEASURE_CALC_RULE_CODE | GoalPEOMeasureCalcRuleCode | — |
| MEASURE_COMMENTS | GoalPEOMeasureComments | ✅ |
| MEASURE_NAME | GoalPEOMeasureName | ✅ |
| MEASURE_TYPE_CODE | GoalPEOMeasureTypeCode | ✅ |
| OBJECT_VERSION_NUMBER | GoalPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationId | ✅ |
| PERCENT_COMPLETE_CODE | GoalPEOPercentCompleteCode | — |
| PERSON_ID | GoalPEOPersonId | — |
| PREVIOUS_STATE_GOAL_ID | GoalPEOPreviousStateGoalId | — |
| PRIORITY_CODE | GoalPEOPriorityCode | ✅ |
| PRIVATE_FLAG | GoalPEOPrivateFlag | — |
| PUBLISH_DATE | GoalPEOPublishDate | — |
| PUBLISHED_FLAG | GoalPEOPublishedFlag | — |
| REFERENCE_CONTENT_ITEM_ID | GoalPEOReferenceContentItemId | — |
| REFERENCE_GOAL_ID | GoalPEOReferenceGoalId | — |
| REQUEST_CONTEXT | GoalPEORequestContext | — |
| REQUESTER_PERSON_ID | GoalPEORequesterPersonId | — |
| START_DATE | GoalPEOStartDate | ✅ |
| STATUS_CODE | GoalPEOStatusCode | — |
| SUCCESS_CRITERIA | GoalPEOSuccessCriteria | ✅ |
| SUCCESS_CRITERIA_TEXT | GoalPEOSuccessCriteriaText | — |
| TARGET_COMPLETION_DATE | GoalPEOTargetCompletionDate | — |
| TARGET_TYPE | GoalPEOTargetType | ✅ |
| TARGET_VALUE | GoalPEOTargetValue | ✅ |
| UOM_CODE | GoalPEOUomCode | ✅ |
| VERSION_DATE | GoalPEOVersionDate | — |

### [[taskpvo|TaskPVO]] (HCM · BICC: 1/53)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_TO_HIERARCHY_FLAG | GoalPEOAccessToHierarchyFlag | — |
| ACTUAL_COMPLETION_DATE | GoalPEOActualCompletionDate | — |
| ACTUAL_VALUE | GoalPEOActualValue | — |
| ALLOW_KEY_ATTR_UPDATE_FLAG | GoalPEOAllowKeyAttrUpdateFlag | — |
| APPROVAL_STATUS_CODE | GoalPEOApprovalStatusCode | — |
| ASSIGNED_BY_PERSON_ID | GoalPEOAssignedByPersonId | — |
| ASSIGNMENT_ID | GoalPEOAssignmentId | — |
| ATTRIBUTE_CATEGORY | GoalPEOAttributeCategory | — |
| BUSINESS_GROUP_ID | GoalPEOBusinessGroupId | — |
| CATEGORY_CODE | GoalPEOCategoryCode | — |
| COMMENTS | GoalPEOComments | — |
| COMMENTS_TEXT | GoalPEOCommentsText | — |
| CREATED_BY | GoalPEOCreatedBy | — |
| CREATION_DATE | GoalPEOCreationDate | — |
| DESCRIPTION | GoalPEODescription | — |
| GOAL_APPROVAL_STATE | GoalPEOGoalApprovalState | — |
| GOAL_ID | GoalPEOGoalId | — |
| GOAL_NAME | GoalPEOGoalName | — |
| GOAL_SOURCE_CODE | GoalPEOGoalSourceCode | — |
| GOAL_TYPE_CODE | GoalPEOGoalTypeCode | — |
| GOAL_URL | GoalPEOGoalUrl | — |
| GOAL_VERSION_TYPE_CODE | GoalPEOGoalVersionTypeCode | — |
| HRCHY_ACCESS_GRANT_DATE | GoalPEOHrchyAccessGrantDate | — |
| INCLUDE_IN_PERFDOC_FLAG | GoalPEOIncludeInPerfdocFlag | — |
| LAST_UPDATE_DATE | GoalPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | GoalPEOLastUpdatedBy | — |
| LEVEL_CODE | GoalPEOLevelCode | — |
| LEVEL_MEANING | GoalPEOLevelMeaning | — |
| LONG_DESCRIPTION | GoalPEOLongDescription | — |
| MASS_REQUEST_ID | GoalPEOMassRequestId | — |
| MEASURE_COMMENTS | GoalPEOMeasureComments | — |
| MEASURE_NAME | GoalPEOMeasureName | — |
| MEASURE_TYPE_CODE | GoalPEOMeasureTypeCode | — |
| OBJECT_VERSION_NUMBER | GoalPEOObjectVersionNumber | — |
| ORGANIZATION_ID | GoalPEOOrganizationId | — |
| PERCENT_COMPLETE_CODE | GoalPEOPercentCompleteCode | — |
| PERSON_ID | GoalPEOPersonId | — |
| PRIORITY_CODE | GoalPEOPriorityCode | — |
| PRIVATE_FLAG | GoalPEOPrivateFlag | — |
| PUBLISH_DATE | GoalPEOPublishDate | — |
| REFERENCE_CONTENT_ITEM_ID | GoalPEOReferenceContentItemId | — |
| REFERENCE_GOAL_ID | GoalPEOReferenceGoalId | — |
| REQUESTER_PERSON_ID | GoalPEORequesterPersonId | — |
| START_DATE | GoalPEOStartDate | — |
| STATUS_CODE | GoalPEOStatusCode | — |
| SUCCESS_CRITERIA | GoalPEOSuccessCriteria | — |
| SUCCESS_CRITERIA_TEXT | GoalPEOSuccessCriteriaText | — |
| TARGET_COMPLETION_DATE | GoalPEOTargetCompletionDate | — |
| TARGET_TYPE | GoalPEOTargetType | — |
| TARGET_VALUE | GoalPEOTargetValue | — |
| UOM_CODE | GoalPEOUomCode | — |
| VERSION_DATE | GoalPEOVersionDate | — |

### [[taskvaluespvo|TaskValuesPVO]] (HCM · BICC: 2/53)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_TO_HIERARCHY_FLAG | GoalPEOAccessToHierarchyFlag | — |
| ACTUAL_COMPLETION_DATE | GoalPEOActualCompletionDate | — |
| ACTUAL_VALUE | GoalPEOActualValue | — |
| ALLOW_KEY_ATTR_UPDATE_FLAG | GoalPEOAllowKeyAttrUpdateFlag | — |
| APPROVAL_STATUS_CODE | GoalPEOApprovalStatusCode | — |
| ASSIGNED_BY_PERSON_ID | GoalPEOAssignedByPersonId | — |
| ASSIGNMENT_ID | GoalPEOAssignmentId | — |
| ATTRIBUTE_CATEGORY | GoalPEOAttributeCategory | — |
| BUSINESS_GROUP_ID | GoalPEOBusinessGroupId | — |
| CATEGORY_CODE | GoalPEOCategoryCode | — |
| COMMENTS | GoalPEOComments | — |
| COMMENTS_TEXT | GoalPEOCommentsText | — |
| CREATED_BY | GoalPEOCreatedBy | — |
| CREATION_DATE | GoalPEOCreationDate | — |
| DESCRIPTION | GoalPEODescription | — |
| GOAL_APPROVAL_STATE | GoalPEOGoalApprovalState | — |
| GOAL_ID | GoalPEOGoalId | — |
| GOAL_NAME | GoalPEOGoalName | — |
| GOAL_SOURCE_CODE | GoalPEOGoalSourceCode | — |
| GOAL_TYPE_CODE | GoalPEOGoalTypeCode | — |
| GOAL_URL | GoalPEOGoalUrl | — |
| GOAL_VERSION_TYPE_CODE | GoalPEOGoalVersionTypeCode | — |
| HRCHY_ACCESS_GRANT_DATE | GoalPEOHrchyAccessGrantDate | — |
| INCLUDE_IN_PERFDOC_FLAG | GoalPEOIncludeInPerfdocFlag | — |
| LAST_UPDATE_DATE | GoalPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | GoalPEOLastUpdatedBy | — |
| LEVEL_CODE | GoalPEOLevelCode | — |
| LEVEL_MEANING | GoalPEOLevelMeaning | — |
| LONG_DESCRIPTION | GoalPEOLongDescription | — |
| MASS_REQUEST_ID | GoalPEOMassRequestId | — |
| MEASURE_COMMENTS | GoalPEOMeasureComments | — |
| MEASURE_NAME | GoalPEOMeasureName | — |
| MEASURE_TYPE_CODE | GoalPEOMeasureTypeCode | — |
| OBJECT_VERSION_NUMBER | GoalPEOObjectVersionNumber | — |
| ORGANIZATION_ID | GoalPEOOrganizationId | — |
| PERCENT_COMPLETE_CODE | GoalPEOPercentCompleteCode | — |
| PERSON_ID | GoalPEOPersonId | — |
| PRIORITY_CODE | GoalPEOPriorityCode | — |
| PRIVATE_FLAG | GoalPEOPrivateFlag | — |
| PUBLISH_DATE | GoalPEOPublishDate | — |
| REFERENCE_CONTENT_ITEM_ID | GoalPEOReferenceContentItemId | — |
| REFERENCE_GOAL_ID | GoalPEOReferenceGoalId | — |
| REQUESTER_PERSON_ID | GoalPEORequesterPersonId | — |
| START_DATE | GoalPEOStartDate | — |
| STATUS_CODE | GoalPEOStatusCode | — |
| SUCCESS_CRITERIA | GoalPEOSuccessCriteria | — |
| SUCCESS_CRITERIA_TEXT | GoalPEOSuccessCriteriaText | — |
| TARGET_COMPLETION_DATE | GoalPEOTargetCompletionDate | — |
| TARGET_TYPE | GoalPEOTargetType | — |
| TARGET_VALUE | GoalPEOTargetValue | — |
| UOM_CODE | GoalPEOUomCode | — |
| VERSION_DATE | GoalPEOVersionDate | — |

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
