---
id: DOC-HCM-271
doc_type: system-doc
title: "HRT_TASK_OBJ_RELATIONS — Relacionamentos Tarefa-Objetivo"
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
  - task-objective
  - performance
  - goals
aliases:
  - HRT_TASK_OBJ_RELATIONS
  - hrt_task_obj_relations
  - hrt-task-obj-relations
  - task-obj-relations
  - relacionamentos-tarefa-objetivo
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_TASK_OBJ_RELATIONS

## 📌 Visao Geral

Armazena os **relacionamentos entre tarefas e objetivos** em processos de performance management. Vincula tarefas operacionais a objetivos estrategicos.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Performance Management:** Vincular tarefas a objetivos de desempenho.
- **Rastreamento:** Monitorar progresso de objetivos via conclusao de tarefas.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TASK_OBJ_RELATION_ID | NUMBER(18) | NOT NULL | PK | Identificador do relacionamento | — | 🟢 90% |
| 2 | TASK_ID | NUMBER(18) | NOT NULL | FK | Tarefa associada | — | 🟡 85% |
| 3 | OBJECTIVE_ID | NUMBER(18) | NOT NULL | FK | Objetivo associado | — | 🟡 85% |
| 4 | RELATION_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de relacao | — | 🟡 75% |
| 5 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 95% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK de entrada identificada.

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Objetivos vinculados a uma tarefa
```sql
SELECT tor.OBJECTIVE_ID, tor.RELATION_TYPE
FROM   HRT_TASK_OBJ_RELATIONS tor
WHERE  tor.TASK_ID = :p_task_id;
```

---

## 🔒 Observacoes

- Tabela de relacionamento N:N entre tarefas e objetivos.
- Permite rastrear quais tarefas contribuem para quais objetivos.

---

## 📚 Referencias

- [Oracle Docs — HRT_TASK_OBJ_RELATIONS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrttaskobjrelations.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
