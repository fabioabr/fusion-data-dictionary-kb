---
id: DOC-HCM-086
doc_type: system-doc
title: "CMP_SALARY — Salários de Compensação"
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
  - salario
  - salary
  - remuneracao
aliases:
  - CMP_SALARY
  - cmp_salary
  - cmp-salary
  - DOC-HCM-086
  - salários-de-compensação
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# CMP_SALARY

## 📌 Visão Geral

Armazena os **registros de salário** dos colaboradores no módulo de Compensação. Cada registro representa uma proposta ou efetivação salarial, com valor, moeda, base salarial, data de efetividade e status de aprovação.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão salarial:** Registro central de todos os salários do colaborador.
- **Histórico salarial:** Manutenção do histórico completo de alterações.
- **Aprovação de salários:** Workflow de aprovação de propostas salariais.
- **Integração com payroll:** Dados salariais enviados para processamento de folha.
- **Relatórios de compensação:** Base para análises de equidade e competitividade.
- **Auditoria:** Rastreamento completo de alterações salariais.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | SALARY_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro de salário | — | 🟢 95% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Identificador da pessoa | [[per_all_people_f]] | 🟢 95% |
| 3 | ASSIGNMENT_ID | NUMBER(18) | NOT NULL | FK | Atribuição do colaborador | [[per_all_assignments_m]] | 🟢 95% |
| 4 | SALARY_AMOUNT | NUMBER | NOT NULL | Financeiro | Valor do salário | — | 🟢 95% |
| 5 | ANNUAL_SALARY | NUMBER | NULL | Financeiro | Salário anualizado | — | 🟢 90% |
| 6 | SALARY_BASIS_ID | NUMBER(18) | NULL | FK | Base salarial | [[cmp_salary_bases]] | 🟢 90% |
| 7 | CURRENCY_CODE | VARCHAR2(30) | NOT NULL | Referência | Moeda do salário | — | 🟢 95% |
| 8 | DATE_FROM | DATE | NOT NULL | Data | Data de início de vigência | — | 🟢 95% |
| 9 | DATE_TO | DATE | NULL | Data | Data de fim de vigência | — | 🟢 90% |
| 10 | ACTION_CODE | VARCHAR2(30) | NULL | Classificação | Código da ação (HIRE, PROMOTION, MERIT) | — | 🟡 80% |
| 11 | ACTION_REASON_CODE | VARCHAR2(30) | NULL | Classificação | Motivo da ação | — | 🟡 80% |
| 12 | STATUS | VARCHAR2(30) | NULL | Status | Status do salário (APPROVED, PENDING, REJECTED) | — | 🟡 80% |
| 13 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 14 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 15 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 16 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador do registro salarial)
- [[per_all_assignments_m]] — via `ASSIGNMENT_ID` (vinculo empregaticio do salario)
- [[cmp_salary_bases]] — via `SALARY_BASIS_ID` (base salarial do registro de salario)

### Tabelas-filha (FK de saída)
- [[cmp_salary_components]] — via `SALARY_ID` (componentes do salário)

---

## 📎 Uso Típico

### Salário atual do colaborador
```sql
SELECT s.SALARY_ID, s.SALARY_AMOUNT, s.ANNUAL_SALARY,
       s.CURRENCY_CODE, s.DATE_FROM
FROM   CMP_SALARY s
WHERE  s.PERSON_ID = :p_person_id
  AND  SYSDATE BETWEEN s.DATE_FROM AND NVL(s.DATE_TO, TO_DATE('4712-12-31','YYYY-MM-DD'));
```

### Histórico de salários por assignment
```sql
SELECT s.SALARY_AMOUNT, s.DATE_FROM, s.DATE_TO,
       s.ACTION_CODE, s.STATUS
FROM   CMP_SALARY s
WHERE  s.ASSIGNMENT_ID = :p_assignment_id
ORDER BY s.DATE_FROM DESC;
```

---

## 🔒 Observações

- Tabela principal de salários no módulo Compensation — cada alteração gera um novo registro.
- O `ACTION_CODE` indica o motivo: HIRE (admissão), PROMOTION (promoção), MERIT (mérito), etc.
- O `ANNUAL_SALARY` é calculado com base no `SALARY_AMOUNT` e na periodicidade da `SALARY_BASIS`.
- Salários com `DATE_TO` nulo são os registros vigentes.
- Integra com payroll para cálculo de folha de pagamento.

---

## 📚 Referências

- [Oracle Docs — CMP_SALARY](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/cmpsalary.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
