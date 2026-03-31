---
id: DOC-HCM-621
doc_type: system-doc
title: "PER_ALLOCATED_TASKS — Tarefas Alocadas"
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
  - tarefas
  - checklist-tasks
aliases:
  - PER_ALLOCATED_TASKS
  - per_allocated_tasks
  - per-allocated-tasks
  - tarefas-alocadas
  - per-allocated-tasks
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_ALLOCATED_TASKS

## 📌 Visão Geral

Armazena as **tarefas individuais** alocadas dentro de um checklist. Cada registro representa uma tarefa específica que deve ser concluída como parte de um processo de checklist.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de tarefas** — rastreamento individual de cada item do checklist.
- **Atribuição de responsáveis** — cada tarefa pode ter um responsável diferente.
- **Prazos** — controle de datas-limite para cada tarefa.
- **Status granular** — acompanhamento do progresso tarefa a tarefa.
- **Compliance** — evidência de conclusão de itens obrigatórios.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ALLOCATED_TASK_ID | NUMBER(18) | NOT NULL | PK | Identificador único da tarefa alocada | — | 🟢 95% |
| 2 | ALLOCATED_CHECKLIST_ID | NUMBER(18) | NOT NULL | FK | Checklist ao qual pertence | PER_ALLOCATED_CHECKLISTS | 🟢 90% |
| 3 | TASK_STATUS | VARCHAR2(30) | NULL | Status | Status da tarefa (OPEN, IN_PROGRESS, COMPLETED) | — | 🟢 85% |
| 4 | PERFORMER_PERSON_ID | NUMBER(18) | NULL | FK | Responsável pela execução | PER_ALL_PEOPLE_F | 🟢 85% |
| 5 | TARGET_END_DATE | DATE | NULL | Período | Data limite para conclusão | — | 🟢 85% |
| 6 | ACTUAL_END_DATE | DATE | NULL | Período | Data real de conclusão | — | 🟢 85% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_allocated_checklists]] — via `ALLOCATED_CHECKLIST_ID` (checklist pai)
- [[per_all_people_f]] — via `PERFORMER_PERSON_ID` (responsável pela execução da tarefa)

### Tabelas-filha (FK de saída)
- [[per_allocated_tasks_tl]] — via `ALLOCATED_TASK_ID` (traduções da tarefa alocada)
- [[per_alloc_task_notifs]] — via `ALLOCATED_TASK_ID` (notificações da tarefa alocada)

---

## 📎 Uso Típico

### Tarefas pendentes de um checklist
```sql
SELECT pat.ALLOCATED_TASK_ID, pat.TASK_STATUS, pat.TARGET_END_DATE
FROM   PER_ALLOCATED_TASKS pat
WHERE  pat.ALLOCATED_CHECKLIST_ID = :p_checklist_id
  AND  pat.TASK_STATUS != 'COMPLETED'
ORDER BY pat.TARGET_END_DATE;
```

### Filtros comuns
- `TASK_STATUS = 'OPEN'` — Tarefas abertas
- `TARGET_END_DATE < SYSDATE` — Tarefas atrasadas
---

## 🔒 Observações

- Cada tarefa é uma instância dentro de um checklist alocado.
- O `PERFORMER_PERSON_ID` identifica quem deve executar a tarefa.
- A diferença entre `TARGET_END_DATE` e `ACTUAL_END_DATE` permite medir atrasos.
---

## 📚 Referências

- [Oracle Docs — PER_ALLOCATED_TASKS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perallocatedtasks.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
