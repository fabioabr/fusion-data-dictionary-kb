---
id: DOC-HCM-622
doc_type: system-doc
title: "PER_ALLOCATED_TASKS_TL — Tarefas Alocadas (Traduções)"
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
  - traducoes
  - tasks-tl
aliases:
  - PER_ALLOCATED_TASKS_TL
  - per_allocated_tasks_tl
  - per-allocated-tasks-tl
  - tarefas-alocadas-(traduções)
  - per-allocated-tasks-
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_ALLOCATED_TASKS_TL

## 📌 Visão Geral

Armazena as **traduções** dos nomes e descrições das tarefas alocadas em múltiplos idiomas.

> [!note] Sufixo _TL
> O sufixo `_TL` indica tabela de **traduções** — armazena textos traduzidos em múltiplos idiomas (colunas `LANGUAGE` e `SOURCE_LANG`).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Internacionalização** — exibe tarefas no idioma do responsável.
- **Self-service** — interface traduzida para execução de tarefas.
- **Consistência** — tradução centralizada dos nomes de tarefas.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ALLOCATED_TASK_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador da tarefa alocada | PER_ALLOCATED_TASKS | 🟢 95% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma da tradução | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem da tradução | — | 🟢 95% |
| 4 | TASK_NAME | VARCHAR2(240) | NOT NULL | Tradução | Nome traduzido da tarefa | — | 🟢 90% |
| 5 | DESCRIPTION | VARCHAR2(600) | NULL | Tradução | Descrição traduzida | — | 🟡 80% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_allocated_tasks]] — via `ALLOCATED_TASK_ID` (tabela base da tarefa alocada)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha — tabela terminal de tradução.

---

## 📎 Uso Típico

### Tarefas em português
```sql
SELECT tl.ALLOCATED_TASK_ID, tl.TASK_NAME
FROM   PER_ALLOCATED_TASKS_TL tl
WHERE  tl.LANGUAGE = 'PTB';
```

### Filtros comuns
- `LANGUAGE = 'PTB'` — Traduções em português brasileiro
---

## 🔒 Observações

- Tabela de traduções (_TL) — chave composta por `ALLOCATED_TASK_ID` + `LANGUAGE`.
---

## 📚 Referências

- [Oracle Docs — PER_ALLOCATED_TASKS_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perallocatedtaskstl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
