---
id: DOC-HCM-715
doc_type: system-doc
title: "PER_TASK_DEPENDENCIES — Dependências de Tarefas"
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
  - dependencias-tarefas
  - onboarding
aliases:
  - PER_TASK_DEPENDENCIES
  - per_task_dependencies
  - per-task-dependencies
  - dependencias-de-tarefas
  - task-dependencies
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_TASK_DEPENDENCIES

## Visão Geral

Armazena as **dependências entre tarefas** dentro de um checklist, definindo quais tarefas devem ser concluídas antes de outras serem iniciadas.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Fluxo sequencial** — garante que tarefas são executadas na ordem correta.
- **Pré-requisitos** — impede início de tarefas cujos pré-requisitos não foram cumpridos.
- **Onboarding estruturado** — define a sequência lógica das etapas de integração.
- **Automação** — permite bloquear tarefas pendentes automaticamente.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TASK_DEPENDENCY_ID | NUMBER(18) | NOT NULL | PK | Identificador único da dependência | — | 🟢 85% |
| 2 | TASK_IN_CHECKLIST_ID | NUMBER(18) | NOT NULL | FK | Tarefa que possui a dependência | PER_TASKS_IN_CHECKLIST_B | 🟢 85% |
| 3 | DEPENDENT_TASK_ID | NUMBER(18) | NOT NULL | FK | Tarefa da qual depende (pré-requisito) | PER_TASKS_IN_CHECKLIST_B | 🟡 80% |
| 4 | DEPENDENCY_TYPE_CD | VARCHAR2(30) | NULL | Classificação | Tipo de dependência (ex.: finish-to-start) | — | 🟡 70% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_tasks_in_checklist_b]] — via `TASK_IN_CHECKLIST_ID` (tarefa que possui a dependência)
- [[per_tasks_in_checklist_b]] — via `DEPENDENT_TASK_ID` (tarefa pré-requisito)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha identificada.

---

## Uso Típico

### Dependências entre tarefas
```sql
SELECT td.TASK_IN_CHECKLIST_ID, t1.TASK_NAME AS tarefa,
       td.DEPENDENT_TASK_ID, t2.TASK_NAME AS pre_requisito
FROM   PER_TASK_DEPENDENCIES td
JOIN   PER_TASKS_IN_CHECKLIST_B t1 ON td.TASK_IN_CHECKLIST_ID = t1.TASK_IN_CHECKLIST_ID
JOIN   PER_TASKS_IN_CHECKLIST_B t2 ON td.DEPENDENT_TASK_ID = t2.TASK_IN_CHECKLIST_ID;
```

### Filtros comuns
- `TASK_IN_CHECKLIST_ID = :p_task_id` — Dependências de uma tarefa específica

---

## Observações

- Relacionamento auto-referencial: ambas as FKs apontam para PER_TASKS_IN_CHECKLIST_B.
- Evitar dependências circulares é responsabilidade da aplicação.
- Geralmente utilizada em processos de onboarding/offboarding.

---

## Referências

- [Oracle Docs — PER_TASK_DEPENDENCIES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/pertaskdependencies.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM

---

## 🔗 PVOs Relacionados

### [[checklisttasktemplatepvo|ChecklistTaskTemplatePVO]] (HCM · BICC: 2/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | ChecklistTaskDependenciesPEOCreatedBy | — |
| CREATION_DATE | ChecklistTaskDependenciesPEOCreationDate | — |
| DEPENDENCY_TYPE | ChecklistTaskDependenciesPEODependencyType | ✅ |
| DEPENDENT_TASK_IN_CHECKLIST_ID | ChecklistTaskDependenciesPEODependentTaskInChecklistId | ✅ |
| ENTERPRISE_ID | ChecklistTaskDependenciesPEOEnterpriseId | — |
| LAST_UPDATE_DATE | ChecklistTaskDependenciesPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | ChecklistTaskDependenciesPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ChecklistTaskDependenciesPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ChecklistTaskDependenciesPEOObjectVersionNumber | — |
| SEED_DATA_SOURCE | ChecklistTaskDependenciesPEOSeedDataSource | — |
| TASK_DEPENDENCY_ID | ChecklistTaskDependenciesPEOChecklistTaskDependenciesPEOTaskDependencyId | — |
| TASK_IN_CHECKLIST_ID | ChecklistTaskDependenciesPEOTaskInChecklistId | — |
