---
id: DOC-HCM-714
doc_type: system-doc
title: "PER_TASKS_IN_CHECKLIST_TL — Tarefas em Checklist (Traduções)"
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
  - traduções
aliases:
  - PER_TASKS_IN_CHECKLIST_TL
  - per_tasks_in_checklist_tl
  - per-tasks-in-checklist-tl
  - tarefas-em-checklist-traduções
  - tasks-in-checklist-tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_TASKS_IN_CHECKLIST_TL

## Visão Geral

Armazena as **traduções** (nomes e descrições em múltiplos idiomas) das tarefas definidas nos checklists. Tabela de tradução (_TL) associada à PER_TASKS_IN_CHECKLIST_B.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Internacionalização** — suporta organizações multinacionais com múltiplos idiomas.
- **Interface do usuário** — exibe tarefas no idioma preferido do colaborador.
- **Relatórios localizados** — permite gerar relatórios de checklists em idiomas específicos.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TASK_IN_CHECKLIST_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador da tarefa (referência à tabela _B) | PER_TASKS_IN_CHECKLIST_B | 🟢 90% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma (ex.: PT, EN, ES) | — | 🟢 90% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem da tradução | — | 🟢 85% |
| 4 | TASK_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome traduzido da tarefa | — | 🟢 85% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Identificação | Descrição traduzida da tarefa | — | 🟡 80% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_tasks_in_checklist_b]] — via `TASK_IN_CHECKLIST_ID` (tabela base da tarefa no template de checklist)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha identificada.

---

## Uso Típico

### Traduções de uma tarefa
```sql
SELECT tl.TASK_NAME, tl.DESCRIPTION, tl.LANGUAGE
FROM   PER_TASKS_IN_CHECKLIST_TL tl
WHERE  tl.TASK_IN_CHECKLIST_ID = :p_task_id
ORDER BY tl.LANGUAGE;
```

### Filtros comuns
- `LANGUAGE = 'PT'` — Filtrar por idioma português
- `LANGUAGE = 'US'` — Filtrar por idioma inglês americano

---

## Observações

- Tabela de tradução (_TL) — sempre associada à _B correspondente.
- PK composta: TASK_IN_CHECKLIST_ID + LANGUAGE.
- SOURCE_LANG indica o idioma original de onde a tradução foi derivada.

---

## Referências

- [Oracle Docs — PER_TASKS_IN_CHECKLIST_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/pertasksinchecklisttl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
