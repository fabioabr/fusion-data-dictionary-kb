---
id: DOC-HCM-084
doc_type: system-doc
title: "CMP_PRE_SALARY_V — Visão de Pré-Salário (CMP)"
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
  - pre-salario
  - salary-pending
  - view
aliases:
  - CMP_PRE_SALARY_V
  - cmp_pre_salary_v
  - cmp-pre-salary-v
  - DOC-HCM-084
  - visão-de-pré-salário-(cmp)
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# CMP_PRE_SALARY_V

## 📌 Visão Geral

**View** que apresenta os dados de **pré-salário** dos colaboradores, consolidando informações anteriores à efetivação salarial. Útil para análises comparativas e aprovações pendentes.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Análise pré-efetivação:** Dados salariais antes da confirmação no sistema.
- **Workflow de aprovação:** Base para telas de aprovação de salários.
- **Comparação:** Valores propostos vs. valores atuais antes da efetivação.
- **Relatórios de pendências:** Identificação de salários aguardando processamento.
- **Validação:** Conferência de dados antes do commit na tabela de salários.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Identificador da pessoa | [[per_all_people_f]] | 🟢 90% |
| 2 | ASSIGNMENT_ID | NUMBER(18) | NULL | FK | Atribuição do colaborador | [[per_all_assignments_m]] | 🟢 90% |
| 3 | SALARY_AMOUNT | NUMBER | NULL | Financeiro | Valor do salário proposto | — | 🟡 80% |
| 4 | ANNUAL_SALARY | NUMBER | NULL | Financeiro | Salário anualizado | — | 🟡 75% |
| 5 | CURRENCY_CODE | VARCHAR2(30) | NULL | Referência | Moeda do salário | — | 🟢 90% |
| 6 | SALARY_BASIS_ID | NUMBER(18) | NULL | FK | Base salarial | [[cmp_salary_bases]] | 🟡 80% |
| 7 | EFFECTIVE_DATE | DATE | NULL | Data | Data de efetividade proposta | — | 🟡 80% |
| 8 | STATUS | VARCHAR2(30) | NULL | Status | Status do pré-salário | — | 🟡 75% |
| 9 | CHANGE_AMOUNT | NUMBER | NULL | Financeiro | Diferença em relação ao salário anterior | — | 🟡 70% |
| 10 | CHANGE_PERCENT | NUMBER | NULL | Financeiro | Percentual de alteração | — | 🟡 70% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador da pre-proposta salarial)
- [[per_all_assignments_m]] — via `ASSIGNMENT_ID` (vinculo empregaticio da pre-proposta salarial)
- [[cmp_salary_bases]] — via `SALARY_BASIS_ID` (base salarial da pre-proposta)

### Tabelas-filha (FK de saída)
- Por ser uma view, não possui tabelas-filha diretas.

---

## 📎 Uso Típico

### Salários pendentes de efetivação
```sql
SELECT ps.PERSON_ID, ps.SALARY_AMOUNT, ps.ANNUAL_SALARY,
       ps.EFFECTIVE_DATE, ps.STATUS
FROM   CMP_PRE_SALARY_V ps
WHERE  ps.STATUS = 'PENDING';
```

### Variações salariais propostas
```sql
SELECT ps.PERSON_ID, ps.SALARY_AMOUNT,
       ps.CHANGE_AMOUNT, ps.CHANGE_PERCENT
FROM   CMP_PRE_SALARY_V ps
WHERE  ps.CHANGE_PERCENT > 10;
```

---

## 🔒 Observações

- Esta é uma **view** (sufixo `_V`), não uma tabela física.
- Consolida dados de pré-processamento salarial antes da efetivação.
- Após aprovação, os dados migram para `CMP_SALARY`.
- Os campos `CHANGE_AMOUNT` e `CHANGE_PERCENT` são calculados automaticamente.

---

## 📚 Referências

- [Oracle Docs — CMP_PRE_SALARY_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/cmppresalaryv.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
