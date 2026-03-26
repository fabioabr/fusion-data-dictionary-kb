---
id: DOC-HCM-075
doc_type: system-doc
title: "CMP_CWB_PERSON_INFO_V — Informações de Pessoa no CWB (View)"
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
  - compensation
  - cwb-person-info-view
  - compensacao-pessoa-view
aliases:
  - CMP_CWB_PERSON_INFO_V
  - cmp_cwb_person_info_v
  - cwb-person-info-view
  - cwb-person-info-v
  - cmp-cwb-person-info-v
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# CMP_CWB_PERSON_INFO_V

## 📌 Visão Geral

View que apresenta as **informações consolidadas de compensação por pessoa** no CWB de forma simplificada, combinando dados de múltiplas tabelas (pessoa, assignment, compensação).

> [!note] Sufixo _V
> O sufixo `_V` indica **view** — consulta pré-montada que combina dados de múltiplas tabelas.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Consulta simplificada:** View pré-montada com dados de pessoa e compensação.
- **Relatórios:** Base para relatórios de compensação sem necessidade de JOINs complexos.
- **Análise:** Visão consolidada para análise de equity e compa-ratio.
- **Self-service gerencial:** Alimenta dashboards do CWB.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador | [[per_all_people_f]] | 🟢 90% |
| 2 | PERSON_NAME | VARCHAR2(360) | NULL | Identificação | Nome completo do colaborador | — | 🟡 80% |
| 3 | PLAN_ID | NUMBER(18) | NULL | FK | Plano de compensação | — | 🟡 80% |
| 4 | MANAGER_ID | NUMBER(18) | NULL | FK | Gestor | [[per_all_people_f]] | 🟢 85% |
| 5 | MANAGER_NAME | VARCHAR2(360) | NULL | Identificação | Nome do gestor | — | 🟡 80% |
| 6 | CURRENT_SALARY | NUMBER | NULL | Financeiro | Salário atual | — | 🟢 85% |
| 7 | PROPOSED_SALARY | NUMBER | NULL | Financeiro | Salário proposto | — | 🟢 85% |
| 8 | MERIT_PERCENT | NUMBER | NULL | Percentual | Percentual de merit increase | — | 🟡 80% |
| 9 | BONUS_AMOUNT | NUMBER | NULL | Financeiro | Valor de bônus | — | 🟡 80% |
| 10 | COMPA_RATIO | NUMBER | NULL | Indicador | Compa-ratio | — | 🟡 80% |
| 11 | PERFORMANCE_RATING | VARCHAR2(30) | NULL | Avaliação | Rating de performance | — | 🟡 75% |
| 12 | APPROVAL_STATUS | VARCHAR2(30) | NULL | Workflow | Status de aprovação | — | 🟡 80% |
| 13 | DEPARTMENT | VARCHAR2(240) | NULL | Organização | Departamento do colaborador | — | 🟡 75% |
| 14 | JOB_NAME | VARCHAR2(240) | NULL | Organização | Cargo do colaborador | — | 🟡 75% |
| 15 | CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Moeda | — | 🟢 85% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` e `MANAGER_ID` (colaborador na visao do workbench)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha (view somente leitura).

---

## 📎 Uso Típico

### Visão consolidada de compensação
```sql
SELECT v.PERSON_NAME, v.JOB_NAME, v.DEPARTMENT,
       v.CURRENT_SALARY, v.PROPOSED_SALARY, v.MERIT_PERCENT,
       v.COMPA_RATIO, v.PERFORMANCE_RATING, v.APPROVAL_STATUS
FROM   CMP_CWB_PERSON_INFO_V v
WHERE  v.MANAGER_ID = :p_manager_id
  AND  v.PLAN_ID = :p_plan_id
ORDER BY v.DEPARTMENT, v.PERSON_NAME;
```

### Filtros comuns
- `APPROVAL_STATUS = 'SUBMITTED'` — Propostas submetidas
- `COMPA_RATIO < 0.8` — Abaixo de 80% do midpoint
- `PERFORMANCE_RATING = '5'` — Top performers

---

## 🔒 Observações

- View somente leitura — dados derivados de `CMP_CWB_PERSON_INFO` e tabelas de pessoas.
- Inclui nomes, departamento e cargo para facilitar análise sem JOINs adicionais.
- Contém dados de compensação sensíveis — classificar como `restricted`.

---

## 📚 Referências

- [Oracle Docs — CMP_CWB_PERSON_INFO_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/cmpcwbpersoninfov.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
