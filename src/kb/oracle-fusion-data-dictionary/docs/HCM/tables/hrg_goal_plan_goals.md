---
id: DOC-HCM-171
doc_type: system-doc
title: "HRG_GOAL_PLAN_GOALS — Objetivos em Planos de Metas"
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
  - HRG_GOAL_PLAN_GOALS
  - hrg_goal_plan_goals
  - objetivos-em-planos-de-metas
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRG_GOAL_PLAN_GOALS

## 📌 Visão Geral

Tabela de relacionamento: **objetivos vinculados a planos de metas**.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Vínculo objetivo-plano:** Associa goals a goal plans.
- **Peso:** Importância relativa no plano.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | GOAL_PLAN_GOAL_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | GOAL_PLAN_ID | NUMBER(18) | NOT NULL | FK | Plano | [[hrg_goal_plans_b]] | 🟢 90% |
| 3 | GOAL_ID | NUMBER(18) | NOT NULL | FK | Objetivo | [[hrg_goals]] | 🟢 90% |
| 4 | WEIGHT | NUMBER | NULL | Métrica | Peso no plano | — | 🟡 75% |
| 5 | SEQUENCE_NUMBER | NUMBER | NULL | Ordenação | Ordem | — | 🟡 70% |
| 6 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai
- [[hrg_goal_plans_b]] — via `GOAL_PLAN_ID` (plano de metas do vinculo)
- [[hrg_goals]] — via `GOAL_ID` (meta vinculada ao plano de metas)

---

## 📎 Uso Típico

### Objetivos de um plano
```sql
SELECT g.GOAL_NAME, gpg.WEIGHT, g.STATUS_CODE
FROM   HRG_GOAL_PLAN_GOALS gpg
JOIN   HRG_GOALS g ON g.GOAL_ID = gpg.GOAL_ID
WHERE  gpg.GOAL_PLAN_ID = :p_id
ORDER BY gpg.SEQUENCE_NUMBER;
```

---

## 🔒 Observações

- Relacionamento N:N.
- Soma dos pesos geralmente = 100%.

---

## 🔗 PVOs Relacionados

### [[careerdevgoalpvo|CareerDevGoalPVO]] (HCM · BICC: 4/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DISPLAY_SEQUENCE | GoalPlanGoalPEODisplaySequence | — |
| EFFECTIVE_END_DATE | GoalPlanGoalPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | GoalPlanGoalPEOEffectiveStartDate | ✅ |
| GOAL_PLAN_GOAL_ID | GoalPlanGoalPEOGoalPlanGoalId | — |
| GOAL_PLAN_ID | GoalPlanGoalPEOGoalPlanId | ✅ |
| GOAL_PLAN_SET_ID | GoalPlanGoalPEOGoalPlanSetId | — |
| LAST_UPDATE_DATE | GoalPlanGoalPEOLastUpdateDate | ✅ |
| REVIEW_PERIOD_ID | GoalPlanGoalPEOReviewPeriodId | — |
| WEIGHTING | GoalPlanGoalPEOWeighting | ✅ |

### [[careerdevgoalpvoviewall|CareerDevGoalPVOViewAll]] (HCM · BICC: 4/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DISPLAY_SEQUENCE | GoalPlanGoalPEODisplaySequence | — |
| EFFECTIVE_END_DATE | GoalPlanGoalPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | GoalPlanGoalPEOEffectiveStartDate | ✅ |
| GOAL_PLAN_GOAL_ID | GoalPlanGoalPEOGoalPlanGoalId | — |
| GOAL_PLAN_ID | GoalPlanGoalPEOGoalPlanId | ✅ |
| GOAL_PLAN_SET_ID | GoalPlanGoalPEOGoalPlanSetId | — |
| LAST_UPDATE_DATE | GoalPlanGoalPEOLastUpdateDate | ✅ |
| REVIEW_PERIOD_ID | GoalPlanGoalPEOReviewPeriodId | — |
| WEIGHTING | GoalPlanGoalPEOWeighting | ✅ |

### [[careerdevgoalversionpvo|CareerDevGoalVersionPVO]] (HCM · BICC: 4/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DISPLAY_SEQUENCE | GoalPlanGoalPEODisplaySequence | — |
| EFFECTIVE_END_DATE | GoalPlanGoalPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | GoalPlanGoalPEOEffectiveStartDate | ✅ |
| GOAL_PLAN_GOAL_ID | GoalPlanGoalPEOGoalPlanGoalId | — |
| GOAL_PLAN_ID | GoalPlanGoalPEOGoalPlanId | ✅ |
| GOAL_PLAN_SET_ID | GoalPlanGoalPEOGoalPlanSetId | — |
| LAST_UPDATE_DATE | GoalPlanGoalPEOLastUpdateDate | ✅ |
| REVIEW_PERIOD_ID | GoalPlanGoalPEOReviewPeriodId | — |
| WEIGHTING | GoalPlanGoalPEOWeighting | ✅ |

### [[careerdevgoalversionpvoviewall|CareerDevGoalVersionPVOViewAll]] (HCM · BICC: 4/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DISPLAY_SEQUENCE | GoalPlanGoalPEODisplaySequence | — |
| EFFECTIVE_END_DATE | GoalPlanGoalPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | GoalPlanGoalPEOEffectiveStartDate | ✅ |
| GOAL_PLAN_GOAL_ID | GoalPlanGoalPEOGoalPlanGoalId | — |
| GOAL_PLAN_ID | GoalPlanGoalPEOGoalPlanId | ✅ |
| GOAL_PLAN_SET_ID | GoalPlanGoalPEOGoalPlanSetId | — |
| LAST_UPDATE_DATE | GoalPlanGoalPEOLastUpdateDate | ✅ |
| REVIEW_PERIOD_ID | GoalPlanGoalPEOReviewPeriodId | — |
| WEIGHTING | GoalPlanGoalPEOWeighting | ✅ |

### [[careerdevpvo|CareerDevPVO]] (HCM · BICC: 5/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | GoalPlanGoalPEOBusinessGroupId | — |
| CREATED_BY | GoalPlanGoalPEOCreatedBy | — |
| CREATION_DATE | GoalPlanGoalPEOCreationDate | — |
| DISPLAY_SEQUENCE | GoalPlanGoalPEODisplaySequence | — |
| EFFECTIVE_END_DATE | GoalPlanGoalPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | GoalPlanGoalPEOEffectiveStartDate | ✅ |
| GOAL_ID | GoalPlanGoalPEOGoalId | ✅ |
| GOAL_PLAN_GOAL_ID | GoalPlanGoalId | ✅ |
| GOAL_PLAN_ID | GoalPlanGoalPEOGoalPlanId | ✅ |
| GOAL_PLAN_SET_ID | GoalPlanGoalPEOGoalPlanSetId1 | — |
| LAST_UPDATE_DATE | GoalPlanGoalPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalPlanGoalPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | GoalPlanGoalPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | GoalPlanGoalPEOObjectVersionNumber | — |
| PRIORITY_CODE | GoalPlanGoalPEOPriorityCode | — |
| REVIEW_PERIOD_ID | GoalPlanGoalPEOReviewPeriodId | — |
| WEIGHTING | GoalPlanGoalPEOWeighting | — |

### [[careerdevversionpvo|CareerDevVersionPVO]] (HCM · BICC: 5/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | GoalPlanGoalPEOBusinessGroupId | — |
| CREATED_BY | GoalPlanGoalPEOCreatedBy | — |
| CREATION_DATE | GoalPlanGoalPEOCreationDate | — |
| DISPLAY_SEQUENCE | GoalPlanGoalPEODisplaySequence | — |
| EFFECTIVE_END_DATE | GoalPlanGoalPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | GoalPlanGoalPEOEffectiveStartDate | ✅ |
| GOAL_ID | GoalPlanGoalPEOGoalId | ✅ |
| GOAL_PLAN_GOAL_ID | GoalPlanGoalId | ✅ |
| GOAL_PLAN_ID | GoalPlanGoalPEOGoalPlanId | ✅ |
| GOAL_PLAN_SET_ID | GoalPlanGoalPEOGoalPlanSetId1 | — |
| LAST_UPDATE_DATE | GoalPlanGoalPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalPlanGoalPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | GoalPlanGoalPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | GoalPlanGoalPEOObjectVersionNumber | — |
| PRIORITY_CODE | GoalPlanGoalPEOPriorityCode | — |
| REVIEW_PERIOD_ID | GoalPlanGoalPEOReviewPeriodId | — |
| WEIGHTING | GoalPlanGoalPEOWeighting | — |

### [[developmentgoalpvo|DevelopmentGoalPVO]] (HCM · BICC: 4/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DISPLAY_SEQUENCE | GoalPlanGoalPEODisplaySequence | — |
| EFFECTIVE_END_DATE | GoalPlanGoalPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | GoalPlanGoalPEOEffectiveStartDate | ✅ |
| GOAL_PLAN_GOAL_ID | GoalPlanGoalPEOGoalPlanGoalId | — |
| GOAL_PLAN_ID | GoalPlanGoalPEOGoalPlanId | ✅ |
| GOAL_PLAN_SET_ID | GoalPlanGoalPEOGoalPlanSetId | — |
| LAST_UPDATE_DATE | GoalPlanGoalPEOLastUpdateDate | ✅ |
| REVIEW_PERIOD_ID | GoalPlanGoalPEOReviewPeriodId | — |
| WEIGHTING | GoalPlanGoalPEOWeighting | ✅ |

### [[developmentgoalpvoviewall|DevelopmentGoalPVOViewAll]] (HCM · BICC: 4/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DISPLAY_SEQUENCE | GoalPlanGoalPEODisplaySequence | — |
| EFFECTIVE_END_DATE | GoalPlanGoalPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | GoalPlanGoalPEOEffectiveStartDate | ✅ |
| GOAL_PLAN_GOAL_ID | GoalPlanGoalPEOGoalPlanGoalId | — |
| GOAL_PLAN_ID | GoalPlanGoalPEOGoalPlanId | ✅ |
| GOAL_PLAN_SET_ID | GoalPlanGoalPEOGoalPlanSetId | — |
| LAST_UPDATE_DATE | GoalPlanGoalPEOLastUpdateDate | ✅ |
| REVIEW_PERIOD_ID | GoalPlanGoalPEOReviewPeriodId | — |
| WEIGHTING | GoalPlanGoalPEOWeighting | ✅ |

### [[goalplangoalpvo|GoalPlanGoalPVO]] (HCM · BICC: 7/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | GoalPlanGoalPEOAssignmentId | — |
| BUSINESS_GROUP_ID | GoalPlanGoalPEOBusinessGroupId | — |
| CREATED_BY | GoalPlanGoalPEOCreatedBy | — |
| CREATION_DATE | GoalPlanGoalPEOCreationDate | — |
| DISPLAY_SEQUENCE | GoalPlanGoalPEODisplaySequence | — |
| EFFECTIVE_END_DATE | GoalPlanGoalPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | GoalPlanGoalPEOEffectiveStartDate | ✅ |
| GOAL_ID | GoalPlanGoalPEOGoalId | — |
| GOAL_PLAN_GOAL_ID | GoalPlanGoalId | ✅ |
| GOAL_PLAN_ID | GoalPlanGoalPEOGoalPlanId | ✅ |
| GOAL_PLAN_SET_ID | GoalPlanGoalPEOGoalPlanSetId | — |
| LAST_UPDATE_DATE | GoalPlanGoalPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalPlanGoalPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | GoalPlanGoalPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | GoalPlanGoalPEOObjectVersionNumber | — |
| PRIORITY_CODE | GoalPlanGoalPEOPriorityCode | ✅ |
| REVIEW_PERIOD_ID | GoalPlanGoalPEORevPeriodId | — |
| WEIGHTING | GoalPlanGoalPEOWeighting | ✅ |

### [[goalppvo1|GoalPPVO1]] (HCM · BICC: 2/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DISPLAY_SEQUENCE | GoalPlanGoalPEODisplaySequence | — |
| EFFECTIVE_END_DATE | GoalPlanGoalPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | GoalPlanGoalPEOEffectiveStartDate | ✅ |
| GOAL_PLAN_GOAL_ID | GoalPlanGoalPEOGoalPlanGoalId | — |
| GOAL_PLAN_ID | GoalPlanGoalPEOGoalPlanId | — |
| GOAL_PLAN_SET_ID | GoalPlanGoalPEOGoalPlanSetId | — |
| LAST_UPDATE_DATE | GoalPlanGoalPEOLastUpdateDate | ✅ |
| REVIEW_PERIOD_ID | GoalPlanGoalPEOReviewPeriodId | — |
| WEIGHTING | GoalPlanGoalPEOWeighting | — |

### [[goalpvo_copy|GoalPVO_Copy]] (HCM · BICC: 2/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DISPLAY_SEQUENCE | GoalPlanGoalPEODisplaySequence | — |
| EFFECTIVE_END_DATE | GoalPlanGoalPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | GoalPlanGoalPEOEffectiveStartDate | ✅ |
| GOAL_PLAN_GOAL_ID | GoalPlanGoalPEOGoalPlanGoalId | — |
| GOAL_PLAN_ID | GoalPlanGoalPEOGoalPlanId | — |
| GOAL_PLAN_SET_ID | GoalPlanGoalPEOGoalPlanSetId | — |
| LAST_UPDATE_DATE | GoalPlanGoalPEOLastUpdateDate | ✅ |
| WEIGHTING | GoalPlanGoalPEOWeighting | — |

### [[goalstatusoverviewpvo|GoalStatusOverviewPVO]] (HCM · BICC: 5/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | GoalPlanGoalPEOBusinessGroupId | — |
| CREATED_BY | GoalPlanGoalPEOCreatedBy | — |
| CREATION_DATE | GoalPlanGoalPEOCreationDate | — |
| DISPLAY_SEQUENCE | GoalPlanGoalPEODisplaySequence | — |
| EFFECTIVE_END_DATE | GoalPlanGoalPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | GoalPlanGoalPEOEffectiveStartDate | ✅ |
| GOAL_ID | GoalPlanGoalPEOGoalId | — |
| GOAL_PLAN_GOAL_ID | GoalPlanGoalId | ✅ |
| GOAL_PLAN_ID | GoalPlanGoalPEOGoalPlanId | ✅ |
| GOAL_PLAN_SET_ID | GoalPlanGoalPEOGoalPlanSetId1 | ✅ |
| LAST_UPDATE_DATE | GoalPlanGoalPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalPlanGoalPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | GoalPlanGoalPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | GoalPlanGoalPEOObjectVersionNumber | — |
| PRIORITY_CODE | GoalPlanGoalPEOPriorityCode | — |
| REVIEW_PERIOD_ID | GoalPlanGoalPEOReviewPeriodId | — |
| WEIGHTING | GoalPlanGoalPEOWeighting | — |

### [[goalversionstatusoverviewpvo|GoalVersionStatusOverviewPVO]] (HCM · BICC: 5/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | GoalPlanGoalPEOBusinessGroupId | — |
| CREATED_BY | GoalPlanGoalPEOCreatedBy | — |
| CREATION_DATE | GoalPlanGoalPEOCreationDate | — |
| DISPLAY_SEQUENCE | GoalPlanGoalPEODisplaySequence | — |
| EFFECTIVE_END_DATE | GoalPlanGoalPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | GoalPlanGoalPEOEffectiveStartDate | ✅ |
| GOAL_ID | GoalPlanGoalPEOGoalId | — |
| GOAL_PLAN_GOAL_ID | GoalPlanGoalId | ✅ |
| GOAL_PLAN_ID | GoalPlanGoalPEOGoalPlanId | ✅ |
| GOAL_PLAN_SET_ID | GoalPlanGoalPEOGoalPlanSetId1 | ✅ |
| LAST_UPDATE_DATE | GoalPlanGoalPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalPlanGoalPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | GoalPlanGoalPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | GoalPlanGoalPEOObjectVersionNumber | — |
| PRIORITY_CODE | GoalPlanGoalPEOPriorityCode | — |
| REVIEW_PERIOD_ID | GoalPlanGoalPEORevPeriodId | — |
| WEIGHTING | GoalPlanGoalPEOWeighting | — |

### [[organizationgoalpvo|OrganizationGoalPVO]] (HCM · BICC: 1/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DISPLAY_SEQUENCE | GoalPlanGoalPEODisplaySequence | — |
| EFFECTIVE_END_DATE | EffectiveEndDate1 | — |
| EFFECTIVE_START_DATE | EffectiveStartDate1 | — |
| GOAL_ID | GoalPlanGoalPEOGoalId | — |
| GOAL_PLAN_GOAL_ID | GoalPlanGoalId | — |
| GOAL_PLAN_ID | GoalPEOGoalPlanId | ✅ |
| GOAL_PLAN_SET_ID | GoalPlanSetId | — |
| GOAL_PLAN_SET_ID | GoalPlanSetId1 | — |
| LAST_UPDATE_DATE | LastUpdateDate | — |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PRIORITY_CODE | PriorityCode | — |
| REVIEW_PERIOD_ID | GoalPlanGoalPEORevPeriodId | — |
| WEIGHTING | GoalPEOWeighting | — |

### [[performancegoalpvo|PerformanceGoalPVO]] (HCM · BICC: 4/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DISPLAY_SEQUENCE | GoalPlanGoalPEODisplaySequence | — |
| EFFECTIVE_END_DATE | GoalPlanGoalPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | GoalPlanGoalPEOEffectiveStartDate | ✅ |
| GOAL_PLAN_GOAL_ID | GoalPlanGoalPEOGoalPlanGoalId | — |
| GOAL_PLAN_ID | GoalPlanGoalPEOGoalPlanId | ✅ |
| GOAL_PLAN_SET_ID | GoalPlanGoalPEOGoalPlanSetId | — |
| LAST_UPDATE_DATE | GoalPlanGoalPEOLastUpdateDate | ✅ |
| REVIEW_PERIOD_ID | GoalPlanGoalPEOReviewPeriodId | — |
| WEIGHTING | GoalPlanGoalPEOWeighting | ✅ |

### [[performancegoalpvoviewall|PerformanceGoalPVOViewAll]] (HCM · BICC: 4/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DISPLAY_SEQUENCE | GoalPlanGoalPEODisplaySequence | — |
| EFFECTIVE_END_DATE | GoalPlanGoalPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | GoalPlanGoalPEOEffectiveStartDate | ✅ |
| GOAL_PLAN_GOAL_ID | GoalPlanGoalPEOGoalPlanGoalId | — |
| GOAL_PLAN_ID | GoalPlanGoalPEOGoalPlanId | ✅ |
| GOAL_PLAN_SET_ID | GoalPlanGoalPEOGoalPlanSetId | — |
| LAST_UPDATE_DATE | GoalPlanGoalPEOLastUpdateDate | ✅ |
| REVIEW_PERIOD_ID | GoalPlanGoalPEOReviewPeriodId | — |
| WEIGHTING | GoalPlanGoalPEOWeighting | ✅ |

### [[performancegoalversionpvo|PerformanceGoalVersionPVO]] (HCM · BICC: 3/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DISPLAY_SEQUENCE | GoalPlanGoalPEODisplaySequence | — |
| EFFECTIVE_END_DATE | GoalPlanGoalPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | GoalPlanGoalPEOEffectiveStartDate | ✅ |
| GOAL_PLAN_GOAL_ID | GoalPlanGoalPEOGoalPlanGoalId | — |
| GOAL_PLAN_ID | GoalPlanGoalPEOGoalPlanId | — |
| GOAL_PLAN_SET_ID | GoalPlanGoalPEOGoalPlanSetId | — |
| LAST_UPDATE_DATE | GoalPlanGoalPEOLastUpdateDate | ✅ |
| REVIEW_PERIOD_ID | GoalPlanGoalPEOReviewPeriodId | — |
| WEIGHTING | GoalPlanGoalPEOWeighting | ✅ |

### [[performancegoalversionpvoviewall|PerformanceGoalVersionPVOViewAll]] (HCM · BICC: 3/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DISPLAY_SEQUENCE | GoalPlanGoalPEODisplaySequence | — |
| EFFECTIVE_END_DATE | GoalPlanGoalPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | GoalPlanGoalPEOEffectiveStartDate | ✅ |
| GOAL_PLAN_GOAL_ID | GoalPlanGoalPEOGoalPlanGoalId | — |
| GOAL_PLAN_ID | GoalPlanGoalPEOGoalPlanId | — |
| GOAL_PLAN_SET_ID | GoalPlanGoalPEOGoalPlanSetId | — |
| LAST_UPDATE_DATE | GoalPlanGoalPEOLastUpdateDate | ✅ |
| REVIEW_PERIOD_ID | GoalPlanGoalPEOReviewPeriodId | — |
| WEIGHTING | GoalPlanGoalPEOWeighting | ✅ |

### [[personalgoalpvo|PersonalGoalPVO]] (HCM · BICC: 2/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DISPLAY_SEQUENCE | GoalPlanGoalPEODisplaySequence | — |
| EFFECTIVE_END_DATE | GoalPlanGoalPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | GoalPlanGoalPEOEffectiveStartDate | ✅ |
| GOAL_PLAN_GOAL_ID | GoalPlanGoalPEOGoalPlanGoalId | — |
| GOAL_PLAN_ID | GoalPlanGoalPEOGoalPlanId | — |
| GOAL_PLAN_SET_ID | GoalPlanGoalPEOGoalPlanSetId | — |
| LAST_UPDATE_DATE | GoalPlanGoalPEOLastUpdateDate | ✅ |
| REVIEW_PERIOD_ID | GoalPlanGoalPEOReviewPeriodId | — |
| WEIGHTING | GoalPlanGoalPEOWeighting | — |

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
