---
id: DOC-HCM-727
doc_type: system-doc
title: "WLF_ASSIGNMENT_TASKS_F — Tarefas de Atribuição (Learning)"
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
  - learning
  - workforce-learning
  - tarefas-atribuição
aliases:
  - WLF_ASSIGNMENT_TASKS_F
  - wlf_assignment_tasks_f
  - wlf-assignment-tasks-f
  - tarefas-de-atribuição-learning
  - assignment-tasks
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# WLF_ASSIGNMENT_TASKS_F

## Visão Geral

Armazena as **tarefas individuais** geradas por atribuições de aprendizado, representando as atividades que cada colaborador deve completar como parte de um treinamento. Tabela date-effective (_F).

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Tracking granular** — acompanha cada tarefa dentro de um treinamento complexo.
- **Progresso detalhado** — mostra quais atividades foram concluídas em um treinamento.
- **Pré-requisitos** — controla a sequência de atividades dentro de um item de aprendizado.
- **Relatórios de compliance** — evidência de conclusão de cada etapa obrigatória.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ASSIGNMENT_TASK_ID | NUMBER(18) | NOT NULL | PK | Identificador único da tarefa de atribuição | — | 🟡 80% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Início da validade do registro | — | 🟢 90% |
| 3 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Fim da validade do registro | — | 🟢 90% |
| 4 | ASSIGNMENT_RECORD_ID | NUMBER(18) | NOT NULL | FK | Registro de atribuição pai | WLF_ASSIGNMENT_RECORDS_F | 🟡 80% |
| 5 | TASK_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo da tarefa (quiz, video, document, etc.) | — | 🟡 70% |
| 6 | TASK_STATUS | VARCHAR2(30) | NULL | Status | Status da tarefa (pending, completed, failed) | — | 🟡 75% |
| 7 | COMPLETION_DATE | DATE | NULL | Data | Data de conclusão da tarefa | — | 🟡 75% |
| 8 | SEQUENCE | NUMBER(9) | NULL | Controle | Ordem da tarefa no treinamento | — | 🟡 70% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[wlf_assignment_records_f]] — via `ASSIGNMENT_RECORD_ID` (registro de atribuição)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha identificada.

---

## Uso Típico

### Tarefas de uma atribuição de aprendizado
```sql
SELECT at.TASK_TYPE, at.TASK_STATUS, at.COMPLETION_DATE, at.SEQUENCE
FROM   WLF_ASSIGNMENT_TASKS_F at
WHERE  at.ASSIGNMENT_RECORD_ID = :p_record_id
  AND  SYSDATE BETWEEN at.EFFECTIVE_START_DATE AND at.EFFECTIVE_END_DATE
ORDER BY at.SEQUENCE;
```

### Filtros comuns
- `ASSIGNMENT_RECORD_ID = :p_record_id` — Tarefas de uma atribuição
- `TASK_STATUS = 'COMPLETED'` — Apenas tarefas concluídas

---

## Observações

- Tabela date-effective (_F) — registros possuem vigência temporal.
- Granularidade abaixo do registro de atribuição — cada tarefa é uma atividade atômica.
- Faz parte do módulo Workforce Learning (prefixo WLF_).

---

## Referências

- [Oracle Docs — WLF_ASSIGNMENT_TASKS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/wlfassignmenttasksf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM

---

## 🔗 PVOs Relacionados

### [[assignmenttaskspvo|AssignmentTasksPVO]] (HCM · BICC: 14/27)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_RECORD_ID | AssignmentTasksDEOAssignmentRecordId | — |
| ASSIGNMENT_TASK_ID | AssignmentTasksDEOAssignmentTaskId | ✅ |
| COMPLETION_DATE | AssignmentTasksDEOCompletionDate | ✅ |
| CREATED_BY | AssignmentTasksDEOCreatedBy | — |
| CREATION_DATE | AssignmentTasksDEOCreationDate | — |
| EFFECTIVE_END_DATE | AssignmentTasksDEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | AssignmentTasksDEOEffectiveStartDate | ✅ |
| EFFORT | AssignmentTasksDEOEffort | ✅ |
| EFFORT_UOM | AssignmentTasksDEOEffortUom | ✅ |
| ENTERPRISE_ID | AssignmentTasksDEOEnterpriseId | — |
| LAST_UPDATE_DATE | AssignmentTasksDEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AssignmentTasksDEOLastUpdateLogin | — |
| LAST_UPDATED_BY | AssignmentTasksDEOLastUpdatedBy | — |
| LEARNING_ITEM_ID | AssignmentTasksDEOLearningItemId | ✅ |
| NOTES | AssignmentTasksDEONotes | ✅ |
| OBJECT_VERSION_NUMBER | AssignmentTasksDEOObjectVersionNumber | — |
| PARENT_TASK_ID | AssignmentTasksDEOParentTaskId | — |
| REASON_CODE | AssignmentTasksDEOReasonCode | ✅ |
| SCORE | AssignmentTasksDEOScore | ✅ |
| SOURCE_OBJECT_CODE | AssignmentTasksDEOSourceObjectCode | — |
| SOURCE_OBJECT_ID | AssignmentTasksDEOSourceObjectId | — |
| SOURCE_OBJECT_TYPE | AssignmentTasksDEOSourceObjectType | — |
| TASK_OWNER_ID | AssignmentTasksDEOTaskOwnerId | — |
| TASK_OWNER_TYPE | AssignmentTasksDEOTaskOwnerType | — |
| TASK_STATUS | AssignmentTasksDEOTaskStatus | ✅ |
| TASK_SUB_STATUS | AssignmentTasksDEOTaskSubStatus | ✅ |
| TRAINING_EFFORT | AssignmentTasksDEOTrainingEffort | ✅ |
