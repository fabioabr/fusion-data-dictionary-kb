---
id: DOC-HCM-169
doc_type: system-doc
title: "HRG_GOAL_PLANS_B — Planos de Metas (Base)"
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
  - plans
aliases:
  - HRG_GOAL_PLANS_B
  - hrg_goal_plans_b
  - planos-de-metas-base
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRG_GOAL_PLANS_B

## 📌 Visão Geral

Tabela base dos **planos de metas (goal plans)**. Agrupa objetivos para um período específico.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Ciclo de metas:** Plano para período específico.
- **Agrupamento:** Organiza objetivos individuais.
- **Governça:** Ciclo de vida dos planos.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | GOAL_PLAN_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 95% |
| 2 | GOAL_PLAN_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome do plano | — | 🟢 90% |
| 3 | STATUS_CODE | VARCHAR2(30) | NOT NULL | Classificação | Status (DRAFT, ACTIVE, CLOSED) | — | 🟢 85% |
| 4 | START_DATE | DATE | NOT NULL | Data | Início | — | 🟢 90% |
| 5 | END_DATE | DATE | NULL | Data | Término | — | 🟢 90% |
| 6 | REVIEW_PERIOD_CODE | VARCHAR2(30) | NULL | Classificação | Período de revisão | — | 🟡 75% |
| 7 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 12 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-filha

### Tabelas relacionadas

---

## 📎 Uso Típico

### Planos ativos
```sql
SELECT gp.GOAL_PLAN_ID, gp.GOAL_PLAN_NAME, gp.START_DATE
FROM   HRG_GOAL_PLANS_B gp
WHERE  gp.STATUS_CODE = 'ACTIVE';
```

---

## 🔒 Observações

- Tabela base (sufixo `_B`) — traduções em [[hrg_goal_plans_tl]].
Ciclo: DRAFT -> ACTIVE -> CLOSED.

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
