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

## 📚 Referências

- [Oracle Docs — PER_ALLOC_TASK_NOTIFS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/peralloctasknotifs.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
