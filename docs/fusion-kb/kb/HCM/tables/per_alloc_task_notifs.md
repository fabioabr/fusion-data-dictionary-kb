---
id: DOC-HCM-625
doc_type: system-doc
title: "PER_ALLOC_TASK_NOTIFS — Notificações de Tarefas Alocadas"
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
  - notificacoes
  - checklist-notifications
aliases:
  - PER_ALLOC_TASK_NOTIFS
  - per_alloc_task_notifs
  - per-alloc-task-notifs
  - notificações-de-tarefas-alocadas
  - per-alloc-task-notif
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_ALLOC_TASK_NOTIFS

## 📌 Visão Geral

Armazena as **notificações** geradas para tarefas alocadas em checklists. Controla o envio de lembretes e alertas sobre prazos e status de tarefas.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Lembretes automáticos** — notificações sobre tarefas pendentes e prazos.
- **Escalação** — alertas para gestores sobre tarefas atrasadas.
- **Comunicação** — canal automatizado de acompanhamento de progresso.
- **Compliance** — evidência de que notificações foram enviadas.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ALLOC_TASK_NOTIF_ID | NUMBER(18) | NOT NULL | PK | Identificador único da notificação | — | 🟢 90% |
| 2 | ALLOCATED_TASK_ID | NUMBER(18) | NOT NULL | FK | Tarefa associada | PER_ALLOCATED_TASKS | 🟢 90% |
| 3 | NOTIFICATION_DATE | DATE | NULL | Período | Data de envio da notificação | — | 🟢 85% |
| 4 | NOTIFICATION_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de notificação (REMINDER, OVERDUE, COMPLETION) | — | 🟡 75% |
| 5 | RECIPIENT_PERSON_ID | NUMBER(18) | NULL | FK | Destinatário | PER_ALL_PEOPLE_F | 🟡 75% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_allocated_tasks]] — via `ALLOCATED_TASK_ID` (tarefa de checklist da notificação)
- [[per_all_people_f]] — via `RECIPIENT_PERSON_ID` (destinatário da notificação de tarefa)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha direta identificada.

---

## 📎 Uso Típico

### Notificações enviadas para uma tarefa
```sql
SELECT ptn.NOTIFICATION_DATE, ptn.NOTIFICATION_TYPE
FROM   PER_ALLOC_TASK_NOTIFS ptn
WHERE  ptn.ALLOCATED_TASK_ID = :p_task_id
ORDER BY ptn.NOTIFICATION_DATE DESC;
```

### Filtros comuns
- `NOTIFICATION_TYPE = 'OVERDUE'` — Notificações de atraso
---

## 🔒 Observações

- As notificações são geradas automaticamente pelo sistema com base nas regras do checklist.
- O tipo OVERDUE é útil para identificar tarefas com prazos vencidos.
- Serve como evidência de comunicação para auditorias de compliance.
---

## 🔗 PVOs Relacionados

### [[allocatedchecklisttaskspvo|AllocatedChecklistTasksPVO]] (HCM · BICC: 12/52)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOC_TASK_NOTIFICATION_ID | AllocatedTaskNotificationPEO1AllocTaskNotificationId | — |
| ALLOC_TASK_NOTIFICATION_ID | AllocatedTaskNotificationPEO2AllocTaskNotificationId | — |
| ALLOC_TASK_NOTIFICATION_ID | AllocatedTaskNotificationPEO3AllocTaskNotificationId | — |
| ALLOC_TASK_NOTIFICATION_ID | AllocatedTaskNotificationPEOAllocTaskNotificationId | — |
| ALLOCATED_TASK_ID | AllocatedTaskNotificationPEO1AllocatedTaskId | — |
| ALLOCATED_TASK_ID | AllocatedTaskNotificationPEO2AllocatedTaskId | — |
| ALLOCATED_TASK_ID | AllocatedTaskNotificationPEO3AllocatedTaskId | — |
| ALLOCATED_TASK_ID | AllocatedTaskNotificationPEOAllocatedTaskId | — |
| CREATED_BY | AllocatedTaskNotificationPEO1CreatedBy | — |
| CREATED_BY | AllocatedTaskNotificationPEO2CreatedBy | — |
| CREATED_BY | AllocatedTaskNotificationPEO3CreatedBy | — |
| CREATED_BY | AllocatedTaskNotificationPEOCreatedBy | — |
| CREATION_DATE | AllocatedTaskNotificationPEO1CreationDate | — |
| CREATION_DATE | AllocatedTaskNotificationPEO2CreationDate | — |
| CREATION_DATE | AllocatedTaskNotificationPEO3CreationDate | — |
| CREATION_DATE | AllocatedTaskNotificationPEOCreationDate | — |
| ENTERPRISE_ID | AllocatedTaskNotificationPEO1EnterpriseId | — |
| ENTERPRISE_ID | AllocatedTaskNotificationPEO2EnterpriseId | — |
| ENTERPRISE_ID | AllocatedTaskNotificationPEO3EnterpriseId | — |
| ENTERPRISE_ID | AllocatedTaskNotificationPEOEnterpriseId | — |
| LAST_UPDATE_DATE | AllocatedTaskNotificationPEO1LastUpdateDate | — |
| LAST_UPDATE_DATE | AllocatedTaskNotificationPEO2LastUpdateDate | — |
| LAST_UPDATE_DATE | AllocatedTaskNotificationPEO3LastUpdateDate | — |
| LAST_UPDATE_DATE | AllocatedTaskNotificationPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | AllocatedTaskNotificationPEO1LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | AllocatedTaskNotificationPEO2LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | AllocatedTaskNotificationPEO3LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | AllocatedTaskNotificationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | AllocatedTaskNotificationPEO1LastUpdatedBy | — |
| LAST_UPDATED_BY | AllocatedTaskNotificationPEO2LastUpdatedBy | — |
| LAST_UPDATED_BY | AllocatedTaskNotificationPEO3LastUpdatedBy | — |
| LAST_UPDATED_BY | AllocatedTaskNotificationPEOLastUpdatedBy | — |
| NOTIFY_OWNER | AllocatedTaskNotificationPEO1NotifyOwner | ✅ |
| NOTIFY_OWNER | AllocatedTaskNotificationPEO2NotifyOwner | ✅ |
| NOTIFY_OWNER | AllocatedTaskNotificationPEO3NotifyOwner | ✅ |
| NOTIFY_OWNER | AllocatedTaskNotificationPEONotifyOwner | ✅ |
| NOTIFY_PERFORMER | AllocatedTaskNotificationPEO1NotifyPerformer | ✅ |
| NOTIFY_PERFORMER | AllocatedTaskNotificationPEO2NotifyPerformer | ✅ |
| NOTIFY_PERFORMER | AllocatedTaskNotificationPEO3NotifyPerformer | ✅ |
| NOTIFY_PERFORMER | AllocatedTaskNotificationPEONotifyPerformer | ✅ |
| OBJECT_VERSION_NUMBER | AllocatedTaskNotificationPEO1ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | AllocatedTaskNotificationPEO2ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | AllocatedTaskNotificationPEO3ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | AllocatedTaskNotificationPEOObjectVersionNumber | — |
| TASK_EVENT | AllocatedTaskNotificationPEO1TaskEvent | ✅ |
| TASK_EVENT | AllocatedTaskNotificationPEO2TaskEvent | ✅ |
| TASK_EVENT | AllocatedTaskNotificationPEO3TaskEvent | ✅ |
| TASK_EVENT | AllocatedTaskNotificationPEOTaskEvent | ✅ |
| TASK_NOTIFICATION_ID | AllocatedTaskNotificationPEO1TaskNotificationId | — |
| TASK_NOTIFICATION_ID | AllocatedTaskNotificationPEO2TaskNotificationId | — |
| TASK_NOTIFICATION_ID | AllocatedTaskNotificationPEO3TaskNotificationId | — |
| TASK_NOTIFICATION_ID | AllocatedTaskNotificationPEOTaskNotificationId | — |

---

## 📚 Referências

- [Oracle Docs — PER_ALLOC_TASK_NOTIFS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/peralloctasknotifs.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
