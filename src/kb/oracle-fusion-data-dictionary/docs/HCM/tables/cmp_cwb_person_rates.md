---
id: DOC-HCM-076
doc_type: system-doc
title: "CMP_CWB_PERSON_RATES — Taxas Individuais no Compensation Workbench"
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
  - cwb
  - taxas-pessoa
  - salary-rates
aliases:
  - CMP_CWB_PERSON_RATES
  - cmp_cwb_person_rates
  - cmp-cwb-person-rates
  - DOC-HCM-076
  - taxas-individuais-no-compensation-workbench
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# CMP_CWB_PERSON_RATES

## 📌 Visão Geral

Armazena as **taxas de compensação individuais** (salários, taxas horárias, comissões) de cada colaborador dentro do processo de Compensation Workbench (CWB). Cada registro representa a taxa de um funcionário em um plano CWB específico, incluindo valores atuais e propostos.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Planejamento salarial:** Registro das taxas individuais durante o ciclo CWB.
- **Aprovação de aumentos:** Comparação de taxas atuais vs. propostas.
- **Orçamento de compensação:** Base de cálculo para orçamentos por gestor.
- **Relatórios de variação:** Análise de delta entre taxa atual e nova taxa.
- **Auditoria de remuneração:** Rastreamento histórico de propostas.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PERSON_RATE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da taxa da pessoa | — | 🟢 95% |
| 2 | PLAN_ID | NUMBER(18) | NOT NULL | FK | Plano CWB associado | [[cmp_cwb_plan_definitions]] | 🟢 95% |
| 3 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Identificador da pessoa | [[per_all_people_f]] | 🟢 95% |
| 4 | ASSIGNMENT_ID | NUMBER(18) | NOT NULL | FK | Atribuição do colaborador | [[per_all_assignments_m]] | 🟢 90% |
| 5 | BASE_SALARY | NUMBER | NULL | Financeiro | Salário-base atual do colaborador | — | 🟡 80% |
| 6 | PROPOSED_SALARY | NUMBER | NULL | Financeiro | Salário proposto no ciclo CWB | — | 🟡 80% |
| 7 | CURRENCY_CODE | VARCHAR2(30) | NULL | Referência | Código da moeda | — | 🟢 90% |
| 8 | RATE_BASIS | VARCHAR2(30) | NULL | Classificação | Base da taxa (ANNUAL, HOURLY, MONTHLY) | — | 🟡 75% |
| 9 | EFFECTIVE_DATE | DATE | NULL | Data | Data de efetividade da taxa | — | 🟡 75% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[cmp_cwb_plan_definitions]] — via `PLAN_ID` (plano CWB das taxas do colaborador)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador das taxas de compensacao)
- [[per_all_assignments_m]] — via `ASSIGNMENT_ID` (vinculo empregaticio das taxas de compensacao)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado até o momento.

---

## 📎 Uso Típico

### Taxas por plano CWB
```sql
SELECT pr.PERSON_ID, pr.BASE_SALARY, pr.PROPOSED_SALARY,
       pr.CURRENCY_CODE, pr.RATE_BASIS
FROM   CMP_CWB_PERSON_RATES pr
WHERE  pr.PLAN_ID = :p_plan_id;
```

### Variação salarial por ciclo
```sql
SELECT pr.PERSON_ID, pr.BASE_SALARY, pr.PROPOSED_SALARY,
       (pr.PROPOSED_SALARY - pr.BASE_SALARY) AS variacao
FROM   CMP_CWB_PERSON_RATES pr
WHERE  pr.PLAN_ID = :p_plan_id
  AND  pr.PROPOSED_SALARY IS NOT NULL;
```

---

## 🔒 Observações

- Os campos `BASE_SALARY` e `PROPOSED_SALARY` são centrais para análise de variação salarial.
- A `RATE_BASIS` indica se a taxa é anual, horária ou mensal — fundamental para comparação correta.
- Esta tabela é populada durante o processo de abertura do ciclo CWB.
- Dados podem ser promovidos para `CMP_SALARY` após aprovação.

---

## 📚 Referências

- [Oracle Docs — CMP_CWB_PERSON_RATES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/cmpcwbpersonrates.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
