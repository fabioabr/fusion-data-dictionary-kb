---
id: DOC-HCM-713
doc_type: system-doc
title: "PER_TASKS_IN_CHECKLIST_B — Tarefas em Checklist (Base)"
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
  - tarefas-checklist
  - onboarding
aliases:
  - PER_TASKS_IN_CHECKLIST_B
  - per_tasks_in_checklist_b
  - per-tasks-in-checklist-b
  - tarefas-em-checklist-base
  - tasks-in-checklist-b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_TASKS_IN_CHECKLIST_B

## Visão Geral

Armazena as **tarefas base** que compõem um checklist de onboarding, offboarding ou qualquer outro processo de RH estruturado em etapas. Tabela base (_B), independente de idioma.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Onboarding/Offboarding** — define as tarefas obrigatórias que o colaborador ou gestor deve completar.
- **Checklists operacionais** — cada item do checklist é uma tarefa rastreável.
- **Compliance** — garante que todas as etapas foram cumpridas antes da conclusão do processo.
- **Automação de processos** — tarefas podem disparar notificações e dependências.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TASK_IN_CHECKLIST_ID | NUMBER(18) | NOT NULL | PK | Identificador único da tarefa no checklist | — | 🟢 90% |
| 2 | CHECKLIST_ID | NUMBER(18) | NOT NULL | FK | Checklist ao qual a tarefa pertence | PER_CHECKLISTS_B | 🟢 85% |
| 3 | TASK_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome interno da tarefa | — | 🟡 80% |
| 4 | TASK_TYPE_CD | VARCHAR2(30) | NULL | Classificação | Tipo/categoria da tarefa | — | 🟡 75% |
| 5 | SEQUENCE | NUMBER(9) | NULL | Controle | Ordem de exibição da tarefa no checklist | — | 🟡 80% |
| 6 | MANDATORY_FLAG | VARCHAR2(1) | NULL | Regra | Indica se a tarefa é obrigatória (Y/N) | — | 🟡 75% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_checklists_b]] — via `CHECKLIST_ID` (checklist pai)

### Tabelas-filha (FK de saída)
- [[per_tasks_in_checklist_tl]] — via `TASK_IN_CHECKLIST_ID` (traduções da tarefa)
- [[per_task_dependencies]] — via `TASK_IN_CHECKLIST_ID` (dependências entre tarefas)
- [[per_task_notifications]] — via `TASK_IN_CHECKLIST_ID` (notificações associadas)

---

## Uso Típico

### Tarefas de um checklist
```sql
SELECT tcb.TASK_NAME, tcb.SEQUENCE, tcb.MANDATORY_FLAG
FROM   PER_TASKS_IN_CHECKLIST_B tcb
JOIN   PER_CHECKLISTS_B cb ON tcb.CHECKLIST_ID = cb.CHECKLIST_ID
WHERE  cb.CHECKLIST_ID = :p_checklist_id
ORDER BY tcb.SEQUENCE;
```

### Filtros comuns
- `CHECKLIST_ID = :p_checklist_id` — Tarefas de um checklist específico
- `MANDATORY_FLAG = 'Y'` — Apenas tarefas obrigatórias

---

## Observações

- Tabela base (_B) — contém dados independentes de idioma.
- Cada tarefa pode ter dependências definidas em PER_TASK_DEPENDENCIES.
- Traduções disponíveis na tabela PER_TASKS_IN_CHECKLIST_TL.
- O campo SEQUENCE determina a ordem de apresentação ao usuário.

---

## Referências

- [Oracle Docs — PER_TASKS_IN_CHECKLIST_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/pertasksinchecklist.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
