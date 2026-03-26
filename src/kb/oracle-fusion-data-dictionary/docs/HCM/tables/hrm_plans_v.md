---
id: DOC-HCM-177
doc_type: system-doc
title: "HRM_PLANS_V — Planos de Sucessão — Visão"
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
  - succession
  - plans
aliases:
  - HRM_PLANS_V
  - hrm_plans_v
  - planos-de-sucessãovisão
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRM_PLANS_V

## 📌 Visão Geral

View dos **planos de sucessão** do HCM. Posições-chave e potenciais sucessores.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Planejamento de sucessão:** Visão consolidada.
- **Continuidade:** Posições-chave e candidatos.
- **Relatórios de talento:** Succession readiness.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PLAN_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | PLAN_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome do plano | — | 🟢 85% |
| 3 | PLAN_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo (POSITION, JOB, INCUMBENT) | — | 🟡 75% |
| 4 | STATUS_CODE | VARCHAR2(30) | NULL | Classificação | Status | — | 🟡 75% |
| 5 | POSITION_ID | NUMBER(18) | NULL | FK | Posição-chave | [[hr_all_positions_f]] | 🟡 75% |
| 6 | INCUMBENT_PERSON_ID | NUMBER(18) | NULL | FK | Titular atual | [[per_all_people_f]] | 🟡 75% |
| 7 | START_DATE | DATE | NULL | Data | Início | — | 🟡 75% |
| 8 | END_DATE | DATE | NULL | Data | Término | — | 🟡 75% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-filha

---

## 📎 Uso Típico

### Planos ativos
```sql
SELECT p.PLAN_ID, p.PLAN_NAME, p.PLAN_TYPE, p.STATUS_CODE
FROM   HRM_PLANS_V p
WHERE  p.STATUS_CODE = 'ACTIVE';
```

---

## 🔒 Observações

- View (sufixo `_V`).
- Utilizado em Talent Review meetings.

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
