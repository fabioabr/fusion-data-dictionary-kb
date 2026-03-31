---
id: DOC-HCM-716
doc_type: system-doc
title: "PER_TASK_NOTIFICATIONS — Notificações de Tarefas"
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
  - checklist
  - notificações-tarefas
  - onboarding
aliases:
  - PER_TASK_NOTIFICATIONS
  - per_task_notifications
  - per-task-notifications
  - notificações-de-tarefas
  - task-notifications
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_TASK_NOTIFICATIONS

## Visão Geral

Armazena as **configurações de notificações** associadas às tarefas de checklists, definindo quando e para quem alertas devem ser enviados.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Alertas de prazo** — notifica responsáveis sobre tarefas próximas do vencimento.
- **Escalation** — dispara notificações quando tarefas estão atrasadas.
- **Comunicação automatizada** — envia lembretes aos participantes do processo.
- **Rastreabilidade** — registra as configurações de notificação para auditoria.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TASK_NOTIFICATION_ID | NUMBER(18) | NOT NULL | PK | Identificador único da notificação | — | 🟢 85% |
| 2 | TASK_IN_CHECKLIST_ID | NUMBER(18) | NOT NULL | FK | Tarefa associada à notificação | PER_TASKS_IN_CHECKLIST_B | 🟢 85% |
| 3 | NOTIFICATION_TYPE_CD | VARCHAR2(30) | NULL | Classificação | Tipo de notificação (ex.: reminder, escalation) | — | 🟡 75% |
| 4 | RECIPIENT_TYPE_CD | VARCHAR2(30) | NULL | Classificação | Tipo de destinatário (ex.: assignee, manager) | — | 🟡 70% |
| 5 | DAYS_BEFORE_DUE | NUMBER(5) | NULL | Regra | Dias antes do vencimento para disparar | — | 🟡 70% |
| 6 | ENABLED_FLAG | VARCHAR2(1) | NULL | Controle | Indica se a notificação está ativa (Y/N) | — | 🟡 70% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_tasks_in_checklist_b]] — via `TASK_IN_CHECKLIST_ID` (tarefa associada)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha identificada.

---

## Uso Típico

### Notificações ativas de um checklist
```sql
SELECT tn.NOTIFICATION_TYPE_CD, tn.RECIPIENT_TYPE_CD, tn.DAYS_BEFORE_DUE,
       tcb.TASK_NAME
FROM   PER_TASK_NOTIFICATIONS tn
JOIN   PER_TASKS_IN_CHECKLIST_B tcb ON tn.TASK_IN_CHECKLIST_ID = tcb.TASK_IN_CHECKLIST_ID
WHERE  tn.ENABLED_FLAG = 'Y'
ORDER BY tcb.SEQUENCE;
```

### Filtros comuns
- `ENABLED_FLAG = 'Y'` — Apenas notificações ativas
- `NOTIFICATION_TYPE_CD = 'REMINDER'` — Apenas lembretes

---

## Observações

- Cada tarefa pode ter múltiplas notificações configuradas.
- O campo DAYS_BEFORE_DUE permite antecipar alertas.
- Notificações desabilitadas (ENABLED_FLAG = 'N') não são disparadas.

---

## Referências

- [Oracle Docs — PER_TASK_NOTIFICATIONS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/pertasknotifications.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM

---

## 🔗 PVOs Relacionados

### [[checklisttasktemplatepvo|ChecklistTaskTemplatePVO]] (HCM · BICC: 12/52)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | ChecklistTaskNotificationPEO1CreatedBy | — |
| CREATED_BY | ChecklistTaskNotificationPEO2CreatedBy | — |
| CREATED_BY | ChecklistTaskNotificationPEO3CreatedBy | — |
| CREATED_BY | ChecklistTaskNotificationPEOCreatedBy | — |
| CREATION_DATE | ChecklistTaskNotificationPEO1CreationDate | — |
| CREATION_DATE | ChecklistTaskNotificationPEO2CreationDate | — |
| CREATION_DATE | ChecklistTaskNotificationPEO3CreationDate | — |
| CREATION_DATE | ChecklistTaskNotificationPEOCreationDate | — |
| ENTERPRISE_ID | ChecklistTaskNotificationPEO1EnterpriseId | — |
| ENTERPRISE_ID | ChecklistTaskNotificationPEO2EnterpriseId | — |
| ENTERPRISE_ID | ChecklistTaskNotificationPEO3EnterpriseId | — |
| ENTERPRISE_ID | ChecklistTaskNotificationPEOEnterpriseId | — |
| LAST_UPDATE_DATE | ChecklistTaskNotificationPEO1LastUpdateDate | — |
| LAST_UPDATE_DATE | ChecklistTaskNotificationPEO2LastUpdateDate | — |
| LAST_UPDATE_DATE | ChecklistTaskNotificationPEO3LastUpdateDate | — |
| LAST_UPDATE_DATE | ChecklistTaskNotificationPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | ChecklistTaskNotificationPEO1LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ChecklistTaskNotificationPEO2LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ChecklistTaskNotificationPEO3LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ChecklistTaskNotificationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ChecklistTaskNotificationPEO1LastUpdatedBy | — |
| LAST_UPDATED_BY | ChecklistTaskNotificationPEO2LastUpdatedBy | — |
| LAST_UPDATED_BY | ChecklistTaskNotificationPEO3LastUpdatedBy | — |
| LAST_UPDATED_BY | ChecklistTaskNotificationPEOLastUpdatedBy | — |
| NOTIFY_OWNER | ChecklistTaskNotificationPEO1NotifyOwner | ✅ |
| NOTIFY_OWNER | ChecklistTaskNotificationPEO2NotifyOwner | ✅ |
| NOTIFY_OWNER | ChecklistTaskNotificationPEO3NotifyOwner | ✅ |
| NOTIFY_OWNER | ChecklistTaskNotificationPEONotifyOwner | ✅ |
| NOTIFY_PERFORMER | ChecklistTaskNotificationPEO1NotifyPerformer | ✅ |
| NOTIFY_PERFORMER | ChecklistTaskNotificationPEO2NotifyPerformer | ✅ |
| NOTIFY_PERFORMER | ChecklistTaskNotificationPEO3NotifyPerformer | ✅ |
| NOTIFY_PERFORMER | ChecklistTaskNotificationPEONotifyPerformer | ✅ |
| OBJECT_VERSION_NUMBER | ChecklistTaskNotificationPEO1ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ChecklistTaskNotificationPEO2ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ChecklistTaskNotificationPEO3ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ChecklistTaskNotificationPEOObjectVersionNumber | — |
| SEED_DATA_SOURCE | ChecklistTaskNotificationPEO1SeedDataSource | — |
| SEED_DATA_SOURCE | ChecklistTaskNotificationPEO2SeedDataSource | — |
| SEED_DATA_SOURCE | ChecklistTaskNotificationPEO3SeedDataSource | — |
| SEED_DATA_SOURCE | ChecklistTaskNotificationPEOSeedDataSource | — |
| TASK_EVENT | ChecklistTaskNotificationPEO1TaskEvent | ✅ |
| TASK_EVENT | ChecklistTaskNotificationPEO2TaskEvent | ✅ |
| TASK_EVENT | ChecklistTaskNotificationPEO3TaskEvent | ✅ |
| TASK_EVENT | ChecklistTaskNotificationPEOTaskEvent | ✅ |
| TASK_IN_CHECKLIST_ID | ChecklistTaskNotificationPEO1TaskInChecklistId | — |
| TASK_IN_CHECKLIST_ID | ChecklistTaskNotificationPEO2TaskInChecklistId | — |
| TASK_IN_CHECKLIST_ID | ChecklistTaskNotificationPEO3TaskInChecklistId | — |
| TASK_IN_CHECKLIST_ID | ChecklistTaskNotificationPEOTaskInChecklistId | — |
| TASK_NOTIFICATION_ID | ChecklistTaskNotificationPEO1TaskNotificationId | — |
| TASK_NOTIFICATION_ID | ChecklistTaskNotificationPEO2TaskNotificationId | — |
| TASK_NOTIFICATION_ID | ChecklistTaskNotificationPEO3TaskNotificationId | — |
| TASK_NOTIFICATION_ID | ChecklistTaskNotificationPEOTaskNotificationId | — |
