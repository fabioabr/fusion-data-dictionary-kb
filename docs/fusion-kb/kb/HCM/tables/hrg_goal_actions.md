---
id: DOC-HCM-166
doc_type: system-doc
title: "HRG_GOAL_ACTIONS — Ações de Objetivos"
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
  - actions
aliases:
  - HRG_GOAL_ACTIONS
  - hrg_goal_actions
  - ações-de-objetivos
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRG_GOAL_ACTIONS

## 📌 Visão Geral

Armazena **ações** vinculadas a objetivos. Tarefas específicas para alcançar um objetivo.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Desdobramento:** Objetivos em ações menores.
- **Acompanhamento:** Conclusão de atividades.
- **Plano de ação:** Etapas necessárias.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | GOAL_ACTION_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | GOAL_ID | NUMBER(18) | NOT NULL | FK | Objetivo | [[hrg_goals]] | 🟢 90% |
| 3 | ACTION_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome da ação | — | 🟡 80% |
| 4 | STATUS_CODE | VARCHAR2(30) | NULL | Classificação | Status | — | 🟡 75% |
| 5 | DUE_DATE | DATE | NULL | Data | Data prevista | — | 🟡 75% |
| 6 | COMPLETION_DATE | DATE | NULL | Data | Data real | — | 🟡 75% |
| 7 | SEQUENCE_NUMBER | NUMBER | NULL | Ordenação | Ordem | — | 🟡 70% |
| 8 | COMMENTS | VARCHAR2(4000) | NULL | Texto livre | Comentários | — | 🟡 65% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai
- [[hrg_goals]] — via `GOAL_ID` (meta da acao planejada)

---

## 📎 Uso Típico

### Ações pendentes
```sql
SELECT a.ACTION_NAME, a.STATUS_CODE, a.DUE_DATE
FROM   HRG_GOAL_ACTIONS a
WHERE  a.GOAL_ID = :p_goal_id AND a.STATUS_CODE <> 'COMPLETED'
ORDER BY a.SEQUENCE_NUMBER;
```

---

## 🔒 Observações

- Cada objetivo pode ter múltiplas ações.
- `SEQUENCE_NUMBER` define ordem sugerida.

---

## 🔗 PVOs Relacionados

### [[goalactionextractpvo|GoalActionExtractPVO]] (HCM · BICC: 18/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_NAME | ActionName | ✅ |
| ACTION_TYPE_CODE | ActionTypeCode | ✅ |
| ACTION_URL | ActionUrl | ✅ |
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| COMMENTS | Comments | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| GOAL_ACTION_ID | GoalActionId | ✅ |
| GOAL_ID | GoalId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| PERCENT_COMPLETE_CODE | PercentCompleteCode | ✅ |
| PRIORITY_CODE | PriorityCode | ✅ |
| START_DATE | StartDate | ✅ |
| STATUS_CODE | StatusCode | ✅ |
| TARGET_COMPLETION_DATE | TargetCompletionDate | ✅ |

### [[taskpvo|TaskPVO]] (HCM · BICC: 18/24)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_NAME | GoalActionPEOActionName | ✅ |
| ACTION_TYPE_CODE | GoalActionPEOActionTypeCode | ✅ |
| ACTION_URL | GoalActionPEOActionUrl | ✅ |
| ACTUAL_COMPLETION_DATE | GoalActionPEOActualCompletionDate | — |
| BUSINESS_GROUP_ID | GoalActionPEOBusinessGroupId | ✅ |
| COMMENTS | GoalActionPEOComments | ✅ |
| COMPLETION_STATUS | GoalActionPEOCompletionStatus | — |
| CREATED_BY | GoalActionPEOCreatedBy | ✅ |
| CREATION_DATE | GoalActionPEOCreationDate | ✅ |
| DESCRIPTION | GoalActionPEODescription | — |
| GOAL_ACTION_ID | GoalActionId | ✅ |
| GOAL_ID | GoalActionPEOGoalId | ✅ |
| LAST_UPDATE_DATE | GoalActionPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalActionPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | GoalActionPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | GoalActionPEOObjectVersionNumber | ✅ |
| PERCENT_COMPLETE_CODE | GoalActionPEOPercentCompleteCode | ✅ |
| PRIORITY_CODE | GoalActionPEOPriorityCode | ✅ |
| START_DATE | GoalActionPEOStartDate | ✅ |
| STATUS_CODE | GoalActionPEOStatusCode | ✅ |
| TARGET_COMPLETION_DATE | GoalActionPEOTargetCompletionDate | ✅ |
| TARGET_TYPE | GoalActionPEOTargetType | — |
| TARGET_VALUE | GoalActionPEOTargetValue | — |
| UOM_CODE | GoalActionPEOUomCode | — |

### [[taskvaluespvo|TaskValuesPVO]] (HCM · BICC: 16/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_NAME | GoalActionPEOActionName | ✅ |
| ACTION_TYPE_CODE | GoalActionPEOActionTypeCode | ✅ |
| ACTION_URL | GoalActionPEOActionUrl | — |
| BUSINESS_GROUP_ID | GoalActionPEOBusinessGroupId | ✅ |
| COMMENTS | GoalActionPEOComments | ✅ |
| CREATED_BY | GoalActionPEOCreatedBy | ✅ |
| CREATION_DATE | GoalActionPEOCreationDate | ✅ |
| GOAL_ACTION_ID | GoalActionId | ✅ |
| GOAL_ID | GoalActionPEOGoalId | ✅ |
| LAST_UPDATE_DATE | GoalActionPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GoalActionPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | GoalActionPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | GoalActionPEOObjectVersionNumber | ✅ |
| PERCENT_COMPLETE_CODE | GoalActionPEOPercentCompleteCode | ✅ |
| PRIORITY_CODE | GoalActionPEOPriorityCode | ✅ |
| START_DATE | GoalActionPEOStartDate | ✅ |
| STATUS_CODE | GoalActionPEOStatusCode | ✅ |
| TARGET_COMPLETION_DATE | GoalActionPEOTargetCompletionDate | ✅ |

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
