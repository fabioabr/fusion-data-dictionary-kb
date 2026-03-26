---
id: DOC-HCM-174
doc_type: system-doc
title: "HRG_GOAL_PLAN_SET_PLANS — Planos em Conjuntos de Metas"
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
  - plan-sets
aliases:
  - HRG_GOAL_PLAN_SET_PLANS
  - hrg_goal_plan_set_plans
  - planos-em-conjuntos-de-metas
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRG_GOAL_PLAN_SET_PLANS

## 📌 Visão Geral

Tabela de relacionamento: **planos de metas em conjuntos**.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Vínculo conjunto-plano:** Associa planos a conjuntos.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | GOAL_PLAN_SET_PLAN_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | GOAL_PLAN_SET_ID | NUMBER(18) | NOT NULL | FK | Conjunto | [[hrg_goal_plan_sets_b]] | 🟢 90% |
| 3 | GOAL_PLAN_ID | NUMBER(18) | NOT NULL | FK | Plano | [[hrg_goal_plans_b]] | 🟢 90% |
| 4 | SEQUENCE_NUMBER | NUMBER | NULL | Ordenação | Ordem | — | 🟡 70% |
| 5 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai
- [[hrg_goal_plan_sets_b]] — via `GOAL_PLAN_SET_ID` (conjunto de planos de metas)
- [[hrg_goal_plans_b]] — via `GOAL_PLAN_ID` (plano de metas no conjunto)

---

## 📎 Uso Típico

### Planos de um conjunto
```sql
SELECT gp.GOAL_PLAN_NAME
FROM   HRG_GOAL_PLAN_SET_PLANS spp
JOIN   HRG_GOAL_PLANS_B gp ON gp.GOAL_PLAN_ID = spp.GOAL_PLAN_ID
WHERE  spp.GOAL_PLAN_SET_ID = :p_id;
```

---

## 🔒 Observações

- Relacionamento N:N.

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
