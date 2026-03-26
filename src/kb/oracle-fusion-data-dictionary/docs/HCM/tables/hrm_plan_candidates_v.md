---
id: DOC-HCM-179
doc_type: system-doc
title: "HRM_PLAN_CANDIDATES_V — Candidatos a Sucessão — Visão Enriquecida"
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
  - candidates
aliases:
  - HRM_PLAN_CANDIDATES_V
  - hrm_plan_candidates_v
  - candidatos-a-sucessãovisão-enriquecida
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRM_PLAN_CANDIDATES_V

## 📌 Visão Geral

View enriquecida de **candidatos a sucessão** com dados de perfil (nome, cargo, departamento).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Relatórios:** Visão com dados de perfil.
- **Talent Review:** Contexto completo.
- **Dashboards:** Painéis de gestão.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PLAN_CANDIDATE_ID | NUMBER(18) | NOT NULL | PK | Identificador | — | 🟢 90% |
| 2 | PLAN_ID | NUMBER(18) | NOT NULL | FK | Plano | [[hrm_plans_v]] | 🟢 90% |
| 3 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Candidato | [[per_all_people_f]] | 🟢 90% |
| 4 | PERSON_NAME | VARCHAR2(360) | NULL | Descrição | Nome completo | — | 🟡 75% |
| 5 | READINESS_CODE | VARCHAR2(30) | NULL | Classificação | Prontidão | — | 🟡 80% |
| 6 | READINESS_MEANING | VARCHAR2(240) | NULL | Descrição | Prontidão traduzida | — | 🟡 70% |
| 7 | RANKING | NUMBER | NULL | Métrica | Classificação | — | 🟡 70% |
| 8 | CURRENT_JOB_NAME | VARCHAR2(240) | NULL | Descrição | Cargo atual | — | 🟡 65% |
| 9 | CURRENT_DEPARTMENT | VARCHAR2(240) | NULL | Descrição | Departamento | — | 🟡 65% |
| 10 | STATUS_CODE | VARCHAR2(30) | NULL | Classificação | Status | — | 🟡 70% |

---

## 🔗 Relacionamentos

### Tabela base

---

## 📎 Uso Típico

### Candidatos prontos
```sql
SELECT pcv.PERSON_NAME, pcv.CURRENT_JOB_NAME, pcv.READINESS_MEANING
FROM   HRM_PLAN_CANDIDATES_V pcv
WHERE  pcv.PLAN_ID = :p_id AND pcv.READINESS_CODE = 'READY_NOW'
ORDER BY pcv.RANKING;
```

---

## 🔒 Observações

- View enriquecida (sufixo `_V`).
- Inclui dados de perfil sem joins adicionais.

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
