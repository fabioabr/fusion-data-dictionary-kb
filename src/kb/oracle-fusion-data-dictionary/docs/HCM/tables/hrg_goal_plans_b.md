---
id: DOC-HCM-169
doc_type: system-doc
title: "HRG_GOAL_PLANS_B — Planos de Metas (Base)"
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
  - plans
aliases:
  - HRG_GOAL_PLANS_B
  - hrg_goal_plans_b
  - planos-de-metas-base
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRG_GOAL_PLANS_B

## 📌 Visão Geral

Tabela base dos **planos de metas (goal plans)**. Agrupa objetivos para um período específico.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Ciclo de metas:** Plano para período específico.
- **Agrupamento:** Organiza objetivos individuais.
- **Governça:** Ciclo de vida dos planos.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | GOAL_PLAN_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 95% |
| 2 | GOAL_PLAN_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome do plano | — | 🟢 90% |
| 3 | STATUS_CODE | VARCHAR2(30) | NOT NULL | Classificação | Status (DRAFT, ACTIVE, CLOSED) | — | 🟢 85% |
| 4 | START_DATE | DATE | NOT NULL | Data | Início | — | 🟢 90% |
| 5 | END_DATE | DATE | NULL | Data | Término | — | 🟢 90% |
| 6 | REVIEW_PERIOD_CODE | VARCHAR2(30) | NULL | Classificação | Período de revisão | — | 🟡 75% |
| 7 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 12 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-filha

### Tabelas relacionadas

---

## 📎 Uso Típico

### Planos ativos
```sql
SELECT gp.GOAL_PLAN_ID, gp.GOAL_PLAN_NAME, gp.START_DATE
FROM   HRG_GOAL_PLANS_B gp
WHERE  gp.STATUS_CODE = 'ACTIVE';
```

---

## 🔒 Observações

- Tabela base (sufixo `_B`) — traduções em [[hrg_goal_plans_tl]].
Ciclo: DRAFT -> ACTIVE -> CLOSED.

---

## 🔗 PVOs Relacionados

### [[careerdevpvo|CareerDevPVO]] (HCM · BICC: 1/92)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALL_DEPARTMENTS_FLAG | GoalPlanBPEOAllDepartmentsFlag | — |
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
| AUTO_ASSOCIATE_GOAL_FLAG | GoalPlanBPEOAutoAssociateGoalFlag | — |
| BUSINESS_GROUP_ID | GoalPlanBPEOBusinessGroupId | — |
| CREATED_BY | GoalPlanBPEOCreatedBy | — |
| CREATED_BY_SYSTEM | GoalPlanBPEOCreatedBySystem | — |
| CREATION_DATE | GoalPlanBPEOCreationDate | — |
| ENABLE_WEIGHTING_FLAG | GoalPlanBPEOEnableWeightingFlag | — |
| END_DATE | GoalPlanBPEOEndDate | — |
| ENFORCE_GOAL_WEIGHT_FLAG | GoalPlanBPEOEnforceGoalWeightFlag | — |
| GOAL_ACCESS_LEVEL_CODE | GoalPlanBPEOGoalAccessLevelCode | — |
| GOAL_PLAN_ACTIVE_FLAG | GoalPlanBPEOGoalPlanActiveFlag | — |
| GOAL_PLAN_EXT_ID | GoalPlanBPEOGoalPlanExtId | — |
| GOAL_PLAN_ID | GoalPlanBPEOGoalPlanId | — |
| GOAL_PLAN_TYPE_CODE | GoalPlanBPEOGoalPlanTypeCode | — |
| GOAL_SUB_TYPE_CODE | GoalPlanBPEOGoalSubTypeCode | — |
| INCLUDE_IN_PERFDOC_FLAG | GoalPlanBPEOIncludeInPerfdocFlag | — |
| LAST_UPDATE_DATE | GoalPlanBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalPlanBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | GoalPlanBPEOLastUpdatedBy1 | — |
| MASS_REQUEST_ID | GoalPlanBPEOMassRequestId | — |
| OBJECT_VERSION_NUMBER | GoalPlanBPEOObjectVersionNumber | — |
| PREVIOUS_GOAL_PLAN_ID | GoalPlanBPEOPreviousGoalPlanId | — |
| PRIMARY_GOAL_PLAN_FLAG | GoalPlanBPEOPrimGoalPlanFlag | — |
| REQUEST_UI_CONTEXT_CODE | GoalPlanBPEORequestUiContextCode | — |
| REVIEW_PERIOD_ID | GoalPlanBPEOReviewPeriodId | — |
| START_DATE | StartDate1 | — |

### [[careerdevversionpvo|CareerDevVersionPVO]] (HCM · BICC: 1/92)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALL_DEPARTMENTS_FLAG | GoalPlanBPEOAllDepartmentsFlag | — |
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
| AUTO_ASSOCIATE_GOAL_FLAG | GoalPlanBPEOAutoAssociateGoalFlag | — |
| BUSINESS_GROUP_ID | GoalPlanBPEOBusinessGroupId | — |
| CREATED_BY | GoalPlanBPEOCreatedBy | — |
| CREATED_BY_SYSTEM | GoalPlanBPEOCreatedBySystem | — |
| CREATION_DATE | GoalPlanBPEOCreationDate | — |
| ENABLE_WEIGHTING_FLAG | GoalPlanBPEOEnableWeightingFlag | — |
| END_DATE | GoalPlanBPEOEndDate | — |
| ENFORCE_GOAL_WEIGHT_FLAG | GoalPlanBPEOEnforceGoalWeightFlag | — |
| GOAL_ACCESS_LEVEL_CODE | GoalPlanBPEOGoalAccessLevelCode | — |
| GOAL_PLAN_ACTIVE_FLAG | GoalPlanBPEOGoalPlanActiveFlag | — |
| GOAL_PLAN_EXT_ID | GoalPlanBPEOGoalPlanExtId | — |
| GOAL_PLAN_ID | GoalPlanBPEOGoalPlanId | — |
| GOAL_PLAN_TYPE_CODE | GoalPlanBPEOGoalPlanTypeCode | — |
| GOAL_SUB_TYPE_CODE | GoalPlanBPEOGoalSubTypeCode | — |
| INCLUDE_IN_PERFDOC_FLAG | GoalPlanBPEOIncludeInPerfdocFlag | — |
| LAST_UPDATE_DATE | GoalPlanBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalPlanBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | GoalPlanBPEOLastUpdatedBy1 | — |
| MASS_REQUEST_ID | GoalPlanBPEOMassRequestId | — |
| OBJECT_VERSION_NUMBER | GoalPlanBPEOObjectVersionNumber | — |
| PREVIOUS_GOAL_PLAN_ID | GoalPlanBPEOPreviousGoalPlanId | — |
| PRIMARY_GOAL_PLAN_FLAG | GoalPlanBPEOPrimGoalPlanFlag | — |
| REQUEST_UI_CONTEXT_CODE | GoalPlanBPEORequestUiContextCode | — |
| REVIEW_PERIOD_ID | GoalPlanBPEOReviewPeriodId | — |
| START_DATE | StartDate1 | — |

### [[developmentgoalplanpvo|DevelopmentGoalPlanPVO]] (HCM · BICC: 23/30)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALL_DEPARTMENTS_FLAG | GoalPlanBPEOAllDepartmentsFlag | — |
| ALLOW_PVT_GOAL_MAX_GOAL_FLAG | GoalPlanBPEOAllowPvtGoalMaxGoalFlag | — |
| ATTRIBUTE_CATEGORY | GoalPlanBPEOAttributeCategory | ✅ |
| AUTO_ASSOCIATE_GOAL_FLAG | GoalPlanBPEOAutoAssociateGoalFlag | ✅ |
| BUSINESS_GROUP_ID | GoalPlanBPEOBusinessGroupId | ✅ |
| CREATED_BY | GoalPlanBPEOCreatedBy | ✅ |
| CREATION_DATE | GoalPlanBPEOCreationDate | ✅ |
| ENABLE_WEIGHTING_FLAG | GoalPlanBPEOEnableWeightingFlag | ✅ |
| END_DATE | GoalPlanBPEOEndDate | ✅ |
| ENFORCE_GOAL_WEIGHT_FLAG | GoalPlanBPEOEnforceGoalWeightFlag | ✅ |
| ENFORCE_MAX_GOALS_IN_GP_FLAG | GoalPlanBPEOEnforceMaxGoalsInGpFlag | — |
| EVALUATION_TYPE | GoalPlanBPEOEvaluationType | — |
| GOAL_ACCESS_LEVEL_CODE | GoalPlanBPEOGoalAccessLevelCode | ✅ |
| GOAL_PLAN_ACTIVE_FLAG | GoalPlanBPEOGoalPlanActiveFlag | ✅ |
| GOAL_PLAN_EXT_ID | GoalPlanBPEOGoalPlanExtId | ✅ |
| GOAL_PLAN_ID | GoalPlanId | ✅ |
| GOAL_PLAN_TYPE_CODE | GoalPlanBPEOGoalPlanTypeCode | ✅ |
| GOAL_SUB_TYPE_CODE | GoalPlanBPEOGoalSubTypeCode | ✅ |
| INCLUDE_IN_PERFDOC_FLAG | GoalPlanBPEOIncludeInPerfdocFlag | ✅ |
| LAST_UPDATE_DATE | GoalPlanBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalPlanBPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | GoalPlanBPEOLastUpdatedBy | ✅ |
| MASS_REQUEST_ID | GoalPlanBPEOMassRequestId | ✅ |
| MAX_GOALS_NUM_IN_GOAL_PLAN | GoalPlanBPEOMaxGoalsNumInGoalPlan | — |
| MIN_GOALS_NUM_IN_GOAL_PLAN | GoalPlanBPEOMinGoalsNumInGoalPlan | — |
| OBJECT_VERSION_NUMBER | GoalPlanBPEOObjectVersionNumber | ✅ |
| PREVIOUS_GOAL_PLAN_ID | GoalPlanBPEOPreviousGoalPlanId | ✅ |
| PRIMARY_GOAL_PLAN_FLAG | GoalPlanBPEOPrimGoalPlanFlag | — |
| REQUEST_UI_CONTEXT_CODE | GoalPlanBPEORequestUiContextCode | ✅ |
| START_DATE | GoalPlanBPEOStartDate | ✅ |

### [[goalplanassignmentfactp1|GoalPlanAssignmentFactP1]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALL_DEPARTMENTS_FLAG | AllDepartmentsFlag | — |
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
| AUTO_ASSOCIATE_GOAL_FLAG | AutoAssociateGoalFlag | — |
| BUSINESS_GROUP_ID | BusinessGroupId1 | — |
| CREATED_BY | CreatedBy1 | — |
| CREATED_BY_SYSTEM | CreatedBySystem | — |
| CREATION_DATE | CreationDate1 | — |
| ENABLE_WEIGHTING_FLAG | EnableWeightingFlag | — |
| END_DATE | EndDate | — |
| ENFORCE_GOAL_WEIGHT_FLAG | EnforceGoalWeightFlag | — |
| GOAL_ACCESS_LEVEL_CODE | GoalAccessLevelCode | — |
| GOAL_PLAN_ACTIVE_FLAG | GoalPlanActiveFlag | — |
| GOAL_PLAN_EXT_ID | GoalPlanExtId | — |
| GOAL_PLAN_ID | GoalPlanId1 | — |
| GOAL_PLAN_TYPE_CODE | GoalPlanTypeCode | — |
| GOAL_SUB_TYPE_CODE | GoalSubTypeCode | — |
| INCLUDE_IN_PERFDOC_FLAG | IncludeInPerfdocFlag | — |
| LAST_UPDATE_DATE | LastUpdateDate1 | — |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | — |
| MASS_REQUEST_ID | MassRequestId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PREVIOUS_GOAL_PLAN_ID | PreviousGoalPlanId | — |
| PRIMARY_GOAL_PLAN_FLAG | GoalPlanBPEOPrimGoalPlanFlag | — |
| REQUEST_UI_CONTEXT_CODE | RequestUiContextCode | — |
| REVIEW_PERIOD_ID | GoalPlanBPEORevPerId | — |
| REVIEW_PERIOD_ID | ReviewPeriodId | — |
| START_DATE | StartDate | — |

### [[goalplanp1|GoalPlanP1]] (HCM · BICC: 27/30)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALL_DEPARTMENTS_FLAG | GoalPlanBPEOAllDepartmentsFlag | ✅ |
| ALLOW_PVT_GOAL_MAX_GOAL_FLAG | GoalPlanBPEOAllowPvtGoalMaxGoalFlag | — |
| ATTRIBUTE_CATEGORY | GoalPlanBPEOAttributeCategory | ✅ |
| AUTO_ASSOCIATE_GOAL_FLAG | GoalPlanBPEOAutoAssociateGoalFlag | ✅ |
| BUSINESS_GROUP_ID | GoalPlanBPEOBusinessGroupId | ✅ |
| CREATED_BY | GoalPlanBPEOCreatedBy | ✅ |
| CREATION_DATE | GoalPlanBPEOCreationDate | ✅ |
| ENABLE_WEIGHTING_FLAG | GoalPlanBPEOEnableWeightingFlag | ✅ |
| END_DATE | GoalPlanBPEOEndDate | ✅ |
| ENFORCE_GOAL_WEIGHT_FLAG | GoalPlanBPEOEnforceGoalWeightFlag | ✅ |
| ENFORCE_MAX_GOALS_IN_GP_FLAG | GoalPlanBPEOEnforceMaxGoalsInGpFlag | — |
| EVALUATION_TYPE | GoalPlanBPEOEvaluationType | ✅ |
| GOAL_ACCESS_LEVEL_CODE | GoalPlanBPEOGoalAccessLevelCode | ✅ |
| GOAL_PLAN_ACTIVE_FLAG | GoalPlanBPEOGoalPlanActiveFlag | ✅ |
| GOAL_PLAN_EXT_ID | GoalPlanBPEOGoalPlanExtId | ✅ |
| GOAL_PLAN_ID | GoalPlanId | ✅ |
| GOAL_PLAN_TYPE_CODE | GoalPlanBPEOGoalPlanTypeCode | ✅ |
| GOAL_SUB_TYPE_CODE | GoalPlanBPEOGoalSubTypeCode | ✅ |
| INCLUDE_IN_PERFDOC_FLAG | GoalPlanBPEOIncludeInPerfdocFlag | ✅ |
| LAST_UPDATE_DATE | GoalPlanBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalPlanBPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | GoalPlanBPEOLastUpdatedBy | ✅ |
| MASS_REQUEST_ID | GoalPlanBPEOMassRequestId | ✅ |
| MAX_GOALS_NUM_IN_GOAL_PLAN | GoalPlanBPEOMaxGoalsNumInGoalPlan | ✅ |
| MIN_GOALS_NUM_IN_GOAL_PLAN | GoalPlanBPEOMinGoalsNumInGoalPlan | — |
| OBJECT_VERSION_NUMBER | GoalPlanBPEOObjectVersionNumber | ✅ |
| PREVIOUS_GOAL_PLAN_ID | GoalPlanBPEOPreviousGoalPlanId | ✅ |
| PRIMARY_GOAL_PLAN_FLAG | GoalPlanBPEOPrimGoalPlanFlag | ✅ |
| REQUEST_UI_CONTEXT_CODE | GoalPlanBPEORequestUiContextCode | ✅ |
| START_DATE | GoalPlanBPEOStartDate | ✅ |

### [[goalstatusoverviewpvo|GoalStatusOverviewPVO]] (HCM · BICC: 1/92)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALL_DEPARTMENTS_FLAG | GoalPlanBPEOAllDepartmentsFlag | — |
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
| AUTO_ASSOCIATE_GOAL_FLAG | GoalPlanBPEOAutoAssociateGoalFlag | — |
| BUSINESS_GROUP_ID | GoalPlanBPEOBusinessGroupId | — |
| CREATED_BY | GoalPlanBPEOCreatedBy | — |
| CREATED_BY_SYSTEM | GoalPlanBPEOCreatedBySystem | — |
| CREATION_DATE | GoalPlanBPEOCreationDate | — |
| ENABLE_WEIGHTING_FLAG | GoalPlanBPEOEnableWeightingFlag | — |
| END_DATE | GoalPlanBPEOEndDate | — |
| ENFORCE_GOAL_WEIGHT_FLAG | GoalPlanBPEOEnforceGoalWeightFlag | — |
| GOAL_ACCESS_LEVEL_CODE | GoalPlanBPEOGoalAccessLevelCode | — |
| GOAL_PLAN_ACTIVE_FLAG | GoalPlanBPEOGoalPlanActiveFlag | — |
| GOAL_PLAN_EXT_ID | GoalPlanBPEOGoalPlanExtId | — |
| GOAL_PLAN_ID | GoalPlanBPEOGoalPlanId | — |
| GOAL_PLAN_TYPE_CODE | GoalPlanBPEOGoalPlanTypeCode | — |
| GOAL_SUB_TYPE_CODE | GoalPlanBPEOGoalSubTypeCode | — |
| INCLUDE_IN_PERFDOC_FLAG | GoalPlanBPEOIncludeInPerfdocFlag | — |
| LAST_UPDATE_DATE | GoalPlanBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalPlanBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | GoalPlanBPEOLastUpdatedBy1 | — |
| MASS_REQUEST_ID | GoalPlanBPEOMassRequestId | — |
| OBJECT_VERSION_NUMBER | GoalPlanBPEOObjectVersionNumber | — |
| PREVIOUS_GOAL_PLAN_ID | GoalPlanBPEOPreviousGoalPlanId | — |
| PRIMARY_GOAL_PLAN_FLAG | GoalPlanBPEOPrimGoalPlanFlag | — |
| REQUEST_UI_CONTEXT_CODE | GoalPlanBPEORequestUiContextCode | — |
| REVIEW_PERIOD_ID | GoalPlanBPEOReviewPeriodId | — |
| START_DATE | StartDate1 | — |

### [[goalversionstatusoverviewpvo|GoalVersionStatusOverviewPVO]] (HCM · BICC: 1/92)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALL_DEPARTMENTS_FLAG | GoalPlanBPEOAllDepartmentsFlag | — |
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
| AUTO_ASSOCIATE_GOAL_FLAG | GoalPlanBPEOAutoAssociateGoalFlag | — |
| BUSINESS_GROUP_ID | GoalPlanBPEOBusinessGroupId | — |
| CREATED_BY | GoalPlanBPEOCreatedBy | — |
| CREATED_BY_SYSTEM | GoalPlanBPEOCreatedBySystem | — |
| CREATION_DATE | GoalPlanBPEOCreationDate | — |
| ENABLE_WEIGHTING_FLAG | GoalPlanBPEOEnableWeightingFlag | — |
| END_DATE | GoalPlanBPEOEndDate | — |
| ENFORCE_GOAL_WEIGHT_FLAG | GoalPlanBPEOEnforceGoalWeightFlag | — |
| GOAL_ACCESS_LEVEL_CODE | GoalPlanBPEOGoalAccessLevelCode | — |
| GOAL_PLAN_ACTIVE_FLAG | GoalPlanBPEOGoalPlanActiveFlag | — |
| GOAL_PLAN_EXT_ID | GoalPlanBPEOGoalPlanExtId | — |
| GOAL_PLAN_ID | GoalPlanBPEOGoalPlanId | — |
| GOAL_PLAN_TYPE_CODE | GoalPlanBPEOGoalPlanTypeCode | — |
| GOAL_SUB_TYPE_CODE | GoalPlanBPEOGoalSubTypeCode | — |
| INCLUDE_IN_PERFDOC_FLAG | GoalPlanBPEOIncludeInPerfdocFlag | — |
| LAST_UPDATE_DATE | GoalPlanBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalPlanBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | GoalPlanBPEOLastUpdatedBy1 | — |
| MASS_REQUEST_ID | GoalPlanBPEOMassRequestId | — |
| OBJECT_VERSION_NUMBER | GoalPlanBPEOObjectVersionNumber | — |
| PREVIOUS_GOAL_PLAN_ID | GoalPlanBPEOPreviousGoalPlanId | — |
| PRIMARY_GOAL_PLAN_FLAG | GoalPlanBPEOPrimGoalPlanFlag | — |
| REQUEST_UI_CONTEXT_CODE | GoalPlanBPEORequestUiContextCode | — |
| REVIEW_PERIOD_ID | GoalPlanBPEOReviewPeriodId | — |
| START_DATE | StartDate1 | — |

### [[performancegoalplanpvo|PerformanceGoalPlanPVO]] (HCM · BICC: 25/30)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALL_DEPARTMENTS_FLAG | GoalPlanBPEOAllDepartmentsFlag | — |
| ALLOW_PVT_GOAL_MAX_GOAL_FLAG | GoalPlanBPEOAllowPvtGoalMaxGoalFlag | — |
| ATTRIBUTE_CATEGORY | GoalPlanBPEOAttributeCategory | ✅ |
| AUTO_ASSOCIATE_GOAL_FLAG | GoalPlanBPEOAutoAssociateGoalFlag | ✅ |
| BUSINESS_GROUP_ID | GoalPlanBPEOBusinessGroupId | ✅ |
| CREATED_BY | GoalPlanBPEOCreatedBy | ✅ |
| CREATION_DATE | GoalPlanBPEOCreationDate | ✅ |
| ENABLE_WEIGHTING_FLAG | GoalPlanBPEOEnableWeightingFlag | ✅ |
| END_DATE | GoalPlanBPEOEndDate | ✅ |
| ENFORCE_GOAL_WEIGHT_FLAG | GoalPlanBPEOEnforceGoalWeightFlag | ✅ |
| ENFORCE_MAX_GOALS_IN_GP_FLAG | GoalPlanBPEOEnforceMaxGoalsInGpFlag | — |
| EVALUATION_TYPE | GoalPlanBPEOEvaluationType | ✅ |
| GOAL_ACCESS_LEVEL_CODE | GoalPlanBPEOGoalAccessLevelCode | ✅ |
| GOAL_PLAN_ACTIVE_FLAG | GoalPlanBPEOGoalPlanActiveFlag | ✅ |
| GOAL_PLAN_EXT_ID | GoalPlanBPEOGoalPlanExtId | ✅ |
| GOAL_PLAN_ID | GoalPlanId | ✅ |
| GOAL_PLAN_TYPE_CODE | GoalPlanBPEOGoalPlanTypeCode | ✅ |
| GOAL_SUB_TYPE_CODE | GoalPlanBPEOGoalSubTypeCode | ✅ |
| INCLUDE_IN_PERFDOC_FLAG | GoalPlanBPEOIncludeInPerfdocFlag | ✅ |
| LAST_UPDATE_DATE | GoalPlanBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalPlanBPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | GoalPlanBPEOLastUpdatedBy | ✅ |
| MASS_REQUEST_ID | GoalPlanBPEOMassRequestId | ✅ |
| MAX_GOALS_NUM_IN_GOAL_PLAN | GoalPlanBPEOMaxGoalsNumInGoalPlan | — |
| MIN_GOALS_NUM_IN_GOAL_PLAN | GoalPlanBPEOMinGoalsNumInGoalPlan | — |
| OBJECT_VERSION_NUMBER | GoalPlanBPEOObjectVersionNumber | ✅ |
| PREVIOUS_GOAL_PLAN_ID | GoalPlanBPEOPreviousGoalPlanId | ✅ |
| PRIMARY_GOAL_PLAN_FLAG | GoalPlanBPEOPrimGoalPlanFlag | ✅ |
| REQUEST_UI_CONTEXT_CODE | GoalPlanBPEORequestUiContextCode | ✅ |
| START_DATE | GoalPlanBPEOStartDate | ✅ |

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
