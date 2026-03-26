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
