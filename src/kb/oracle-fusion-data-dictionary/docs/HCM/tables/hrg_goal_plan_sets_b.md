---
id: DOC-HCM-172
doc_type: system-doc
title: "HRG_GOAL_PLAN_SETS_B — Conjuntos de Planos de Metas (Base)"
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
  - plan-sets
aliases:
  - HRG_GOAL_PLAN_SETS_B
  - hrg_goal_plan_sets_b
  - conjuntos-de-planos-de-metas-base
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRG_GOAL_PLAN_SETS_B

## 📌 Visão Geral

Tabela base de **conjuntos (sets) de planos de metas**. Agrupa múltiplos planos.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Agrupamento:** Múltiplos planos em conjunto lógico.
- **Administração centralizada:** Gestão de ciclos.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | GOAL_PLAN_SET_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 95% |
| 2 | PLAN_SET_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome do conjunto | — | 🟡 80% |
| 3 | STATUS_CODE | VARCHAR2(30) | NULL | Classificação | Status (ACTIVE, INACTIVE) | — | 🟡 70% |
| 4 | START_DATE | DATE | NULL | Data | Início | — | 🟡 75% |
| 5 | END_DATE | DATE | NULL | Data | Término | — | 🟡 75% |
| 6 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 11 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-filha

### Tabelas relacionadas

---

## 📎 Uso Típico

### Conjuntos ativos
```sql
SELECT gps.GOAL_PLAN_SET_ID, gps.PLAN_SET_NAME
FROM   HRG_GOAL_PLAN_SETS_B gps
WHERE  gps.STATUS_CODE = 'ACTIVE';
```

---

## 🔒 Observações

- Tabela base (sufixo `_B`) — traduções em [[hrg_goal_plan_sets_tl]].

---

## 🔗 PVOs Relacionados

### [[careerdevpvo|CareerDevPVO]] (HCM · BICC: 1/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | GoalPlanSetBPEOBusinessGroupId | — |
| CREATED_BY | GoalPlanSetBPEOCreatedBy | — |
| CREATION_DATE | GoalPlanSetBPEOCreationDate | — |
| END_DATE | GoalPlanSetBPEOEndDate | — |
| GOAL_PLAN_SET_ACTIVE_FLAG | GoalPlanSetBPEOGoalPlanSetActiveFlag | — |
| GOAL_PLAN_SET_EXT_ID | GoalPlanSetBPEOGoalPlanSetExtId | — |
| GOAL_PLAN_SET_ID | GoalPlanSetBPEOGoalPlanSetId | — |
| LAST_UPDATE_DATE | GoalPlanSetBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalPlanSetBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | GoalPlanSetBPEOLastUpdatedBy1 | — |
| MASS_REQUEST_ID | GoalPlanSetBPEOMassRequestId | — |
| OBJECT_VERSION_NUMBER | GoalPlanSetBPEOObjectVersionNumber | — |
| REQUEST_UI_CONTEXT_CODE | GoalPlanSetBPEORequestUiContextCode | — |
| REVIEW_PERIOD_ID | GoalPlanSetBPEOReviewPeriodId | — |
| START_DATE | StartDate | — |

### [[careerdevversionpvo|CareerDevVersionPVO]] (HCM · BICC: 1/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | GoalPlanSetBPEOBusinessGroupId | — |
| CREATED_BY | GoalPlanSetBPEOCreatedBy | — |
| CREATION_DATE | GoalPlanSetBPEOCreationDate | — |
| END_DATE | GoalPlanSetBPEOEndDate | — |
| GOAL_PLAN_SET_ACTIVE_FLAG | GoalPlanSetBPEOGoalPlanSetActiveFlag | — |
| GOAL_PLAN_SET_EXT_ID | GoalPlanSetBPEOGoalPlanSetExtId | — |
| GOAL_PLAN_SET_ID | GoalPlanSetBPEOGoalPlanSetId | — |
| LAST_UPDATE_DATE | GoalPlanSetBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalPlanSetBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | GoalPlanSetBPEOLastUpdatedBy1 | — |
| MASS_REQUEST_ID | GoalPlanSetBPEOMassRequestId | — |
| OBJECT_VERSION_NUMBER | GoalPlanSetBPEOObjectVersionNumber | — |
| REQUEST_UI_CONTEXT_CODE | GoalPlanSetBPEORequestUiContextCode | — |
| REVIEW_PERIOD_ID | GoalPlanSetBPEOReviewPeriodId | — |
| START_DATE | StartDate | — |

### [[goalplansetpvo|GoalPlanSetPVO]] (HCM · BICC: 13/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | GoalPlanSetBPEOBusinessGroupId | ✅ |
| CREATED_BY | GoalPlanSetBPEOCreatedBy | ✅ |
| CREATION_DATE | GoalPlanSetBPEOCreationDate | ✅ |
| END_DATE | GoalPlanSetBPEOEndDate | ✅ |
| GOAL_PLAN_SET_ACTIVE_FLAG | GoalPlanSetBPEOGoalPlanSetActiveFlag | ✅ |
| GOAL_PLAN_SET_EXT_ID | GoalPlanSetBPEOGoalPlanSetExtId | ✅ |
| GOAL_PLAN_SET_ID | GoalPlanSetId | ✅ |
| LAST_UPDATE_DATE | GoalPlanSetBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalPlanSetBPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | GoalPlanSetBPEOLastUpdatedBy | ✅ |
| MASS_REQUEST_ID | GoalPlanSetBPEOMassRequestId | ✅ |
| OBJECT_VERSION_NUMBER | GoalPlanSetBPEOObjectVersionNumber | — |
| REQUEST_UI_CONTEXT_CODE | GoalPlanSetBPEORequestUiContextCode | ✅ |
| START_DATE | GoalPlanSetBPEOStartDate | ✅ |

### [[goalstatusoverviewpvo|GoalStatusOverviewPVO]] (HCM · BICC: 1/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | GoalPlanSetBPEOBusinessGroupId | — |
| CREATED_BY | GoalPlanSetBPEOCreatedBy | — |
| CREATION_DATE | GoalPlanSetBPEOCreationDate | — |
| END_DATE | GoalPlanSetBPEOEndDate | — |
| GOAL_PLAN_SET_ACTIVE_FLAG | GoalPlanSetBPEOGoalPlanSetActiveFlag | — |
| GOAL_PLAN_SET_EXT_ID | GoalPlanSetBPEOGoalPlanSetExtId | — |
| GOAL_PLAN_SET_ID | GoalPlanSetBPEOGoalPlanSetId | — |
| LAST_UPDATE_DATE | GoalPlanSetBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalPlanSetBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | GoalPlanSetBPEOLastUpdatedBy1 | — |
| MASS_REQUEST_ID | GoalPlanSetBPEOMassRequestId | — |
| OBJECT_VERSION_NUMBER | GoalPlanSetBPEOObjectVersionNumber | — |
| REQUEST_UI_CONTEXT_CODE | GoalPlanSetBPEORequestUiContextCode | — |
| REVIEW_PERIOD_ID | GoalPlanSetBPEOReviewPeriodId | — |
| START_DATE | StartDate | — |

### [[goalversionstatusoverviewpvo|GoalVersionStatusOverviewPVO]] (HCM · BICC: 1/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | GoalPlanSetBPEOBusinessGroupId | — |
| CREATED_BY | GoalPlanSetBPEOCreatedBy | — |
| CREATION_DATE | GoalPlanSetBPEOCreationDate | — |
| END_DATE | GoalPlanSetBPEOEndDate | — |
| GOAL_PLAN_SET_ACTIVE_FLAG | GoalPlanSetBPEOGoalPlanSetActiveFlag | — |
| GOAL_PLAN_SET_EXT_ID | GoalPlanSetBPEOGoalPlanSetExtId | — |
| GOAL_PLAN_SET_ID | GoalPlanSetBPEOGoalPlanSetId | — |
| LAST_UPDATE_DATE | GoalPlanSetBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalPlanSetBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | GoalPlanSetBPEOLastUpdatedBy1 | — |
| MASS_REQUEST_ID | GoalPlanSetBPEOMassRequestId | — |
| OBJECT_VERSION_NUMBER | GoalPlanSetBPEOObjectVersionNumber | — |
| REQUEST_UI_CONTEXT_CODE | GoalPlanSetBPEORequestUiContextCode | — |
| REVIEW_PERIOD_ID | GoalPlanSetBPEOReviewPeriodId | — |
| START_DATE | StartDate | — |

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
