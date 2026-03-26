---
id: DOC-HCM-175
doc_type: system-doc
title: "HRG_GOAL_PLN_ASSIGNMENTS — Atribuições de Planos de Metas"
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
  - assignments
aliases:
  - HRG_GOAL_PLN_ASSIGNMENTS
  - hrg_goal_pln_assignments
  - atribuições-de-planos-de-metas
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRG_GOAL_PLN_ASSIGNMENTS

## 📌 Visão Geral

Armazena **atribuições de planos de metas a colaboradores**.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Inscrição:** Atribuição de colaboradores a planos.
- **Cobertura:** Verificação de quem possui planos.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | GOAL_PLN_ASSIGNMENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | GOAL_PLAN_ID | NUMBER(18) | NOT NULL | FK | Plano | [[hrg_goal_plans_b]] | 🟢 90% |
| 3 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador | [[per_all_people_f]] | 🟢 90% |
| 4 | ASSIGNMENT_STATUS | VARCHAR2(30) | NULL | Classificação | Status (ACTIVE, INACTIVE) | — | 🟡 75% |
| 5 | ASSIGNMENT_DATE | DATE | NULL | Data | Data da atribuição | — | 🟡 75% |
| 6 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai
- [[hrg_goal_plans_b]] — via `GOAL_PLAN_ID` (plano de metas da atribuicao)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador atribuido ao plano de metas)

---

## 📎 Uso Típico

### Colaboradores em um plano
```sql
SELECT ga.PERSON_ID, ga.ASSIGNMENT_STATUS
FROM   HRG_GOAL_PLN_ASSIGNMENTS ga
WHERE  ga.GOAL_PLAN_ID = :p_id AND ga.ASSIGNMENT_STATUS = 'ACTIVE';
```

---

## 🔒 Observações

- Colaborador pode estar em múltiplos planos.

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
