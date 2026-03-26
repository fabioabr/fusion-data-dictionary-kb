---
id: DOC-HCM-087
doc_type: system-doc
title: "CMP_SALARY_BASES — Bases Salariais (Base)"
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
  - base-salarial
  - salary-basis
  - annualization
aliases:
  - CMP_SALARY_BASES
  - cmp_salary_bases
  - cmp-salary-bases
  - DOC-HCM-087
  - bases-salariais-(base)
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# CMP_SALARY_BASES

## 📌 Visão Geral

Armazena as **definições de bases salariais** — a periodicidade e fator de anualização usados para cálculo de salários. Ex: mensal (fator 12), horário (fator 2080), quinzenal (fator 24).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Definição de periodicidade:** Configuração de como o salário é expresso (mensal, anual, horário).
- **Fator de anualização:** Multiplicador para converter salário em base anual.
- **Padronização:** Referência para comparação de salários em bases diferentes.
- **Integração com payroll:** Define como o salário é processado na folha.
- **Base para tradução:** Complementada por `CMP_SALARY_BASES_TL`.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | SALARY_BASIS_ID | NUMBER(18) | NOT NULL | PK | Identificador único da base salarial | — | 🟢 95% |
| 2 | SALARY_BASIS_CODE | VARCHAR2(30) | NOT NULL | Identificação | Código da base salarial | — | 🟢 90% |
| 3 | PAY_BASIS | VARCHAR2(30) | NULL | Classificação | Base de pagamento (ANNUAL, MONTHLY, HOURLY) | — | 🟢 90% |
| 4 | ANNUALIZATION_FACTOR | NUMBER | NULL | Cálculo | Fator de anualização (ex: 12 para mensal) | — | 🟢 90% |
| 5 | CURRENCY_CODE | VARCHAR2(30) | NULL | Referência | Moeda padrão | — | 🟢 90% |
| 6 | GRADE_RATE_ID | NUMBER(18) | NULL | FK | Taxa de grade associada | [[per_grades_f]] | 🟡 70% |
| 7 | EFFECTIVE_START_DATE | DATE | NOT NULL | Data | Início de vigência | — | 🟢 90% |
| 8 | EFFECTIVE_END_DATE | DATE | NOT NULL | Data | Fim de vigência | — | 🟢 90% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_grades_f]] — via `GRADE_RATE_ID` (taxa de grade, se aplicável)

### Tabelas-filha (FK de saída)
- [[cmp_salary]] — via `SALARY_BASIS_ID` (salarios vinculados a base salarial)
- [[cmp_salary_bases_tl]] — via `SALARY_BASIS_ID` (traducoes multilingue do registro)

---

## 📎 Uso Típico

### Bases salariais ativas
```sql
SELECT sb.SALARY_BASIS_ID, sb.SALARY_BASIS_CODE, sb.PAY_BASIS,
       sb.ANNUALIZATION_FACTOR, sb.CURRENCY_CODE
FROM   CMP_SALARY_BASES sb
WHERE  SYSDATE BETWEEN sb.EFFECTIVE_START_DATE AND sb.EFFECTIVE_END_DATE;
```

### Fator de anualização por base
```sql
SELECT sb.SALARY_BASIS_CODE, sb.PAY_BASIS, sb.ANNUALIZATION_FACTOR
FROM   CMP_SALARY_BASES sb
ORDER BY sb.ANNUALIZATION_FACTOR;
```

---

## 🔒 Observações

- O `ANNUALIZATION_FACTOR` converte o valor para base anual: Salário Mensal × 12 = Anual.
- Bases típicas: ANNUAL (fator 1), MONTHLY (fator 12), HOURLY (fator 2080).
- Cada assignment referencia uma base salarial que define como o salário é expresso.
- Tabela _B (base) — nomes traduzidos estão em `CMP_SALARY_BASES_TL`.

---

## 📚 Referências

- [Oracle Docs — CMP_SALARY_BASES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/cmpsalarybases.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
