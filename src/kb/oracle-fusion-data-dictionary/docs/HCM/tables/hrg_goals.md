---
id: DOC-HCM-165
doc_type: system-doc
title: "HRG_GOALS — Objetivos (Goals) de Colaboradores"
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
  - goals
  - performance
aliases:
  - HRG_GOALS
  - hrg_goals
  - objetivos-goals-de-colaboradores
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRG_GOALS

## 📌 Visão Geral

Tabela principal de **objetivos (goals)** de colaboradores no módulo de Performance.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de desempenho:** Objetivos individuais.
- **Acompanhamento:** Progresso, status e resultados.
- **Avaliação:** Base para ciclos de avaliação.
- **Alinhamento estratégico:** Vínculo com metas organizacionais.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | GOAL_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 95% |
| 2 | GOAL_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome do objetivo | — | 🟢 90% |
| 3 | GOAL_DESCRIPTION | VARCHAR2(4000) | NULL | Descrição | Descrição detalhada | — | 🟢 85% |
| 4 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador | [[per_all_people_f]] | 🟢 90% |
| 5 | GOAL_TYPE_CODE | VARCHAR2(30) | NULL | Classificação | Tipo (PERFORMANCE, DEVELOPMENT) | — | 🟡 80% |
| 6 | STATUS_CODE | VARCHAR2(30) | NOT NULL | Classificação | Status (NOT_STARTED, IN_PROGRESS, COMPLETED) | — | 🟢 85% |
| 7 | START_DATE | DATE | NULL | Data | Início | — | 🟢 85% |
| 8 | TARGET_COMPLETION_DATE | DATE | NULL | Data | Data prevista | — | 🟢 85% |
| 9 | COMPLETION_DATE | DATE | NULL | Data | Data real de conclusão | — | 🟢 85% |
| 10 | PERCENT_COMPLETE | NUMBER | NULL | Métrica | Percentual (0-100) | — | 🟢 85% |
| 11 | PRIORITY_CODE | VARCHAR2(30) | NULL | Classificação | Prioridade | — | 🟡 75% |
| 12 | WEIGHT | NUMBER | NULL | Métrica | Peso no plano | — | 🟡 75% |
| 13 | MANAGER_ID | NUMBER(18) | NULL | FK | Gestor | [[per_all_people_f]] | 🟡 75% |
| 14 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 15 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 16 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 17 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 18 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 19 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai
- [[per_all_people_f]] — via `PERSON_ID` (colaborador responsavel pela meta)

### Tabelas-filha

---

## 📎 Uso Típico

### Objetivos ativos
```sql
SELECT g.GOAL_ID, g.GOAL_NAME, g.STATUS_CODE, g.PERCENT_COMPLETE
FROM   HRG_GOALS g
WHERE  g.PERSON_ID = :p_person_id
  AND  g.STATUS_CODE NOT IN ('COMPLETED','CANCELLED')
ORDER BY g.PRIORITY_CODE;
```

---

## 🔒 Observações

- Tabela central do módulo de Goals.
- `WEIGHT` para nota ponderada.
- `PERCENT_COMPLETE` manual ou via métricas.

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
