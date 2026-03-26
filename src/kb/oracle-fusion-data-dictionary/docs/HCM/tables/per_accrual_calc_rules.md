---
id: DOC-HCM-607
doc_type: system-doc
title: "PER_ACCRUAL_CALC_RULES — Regras de Cálculo de Acumulação"
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
  - absence-management
  - accrual
  - regras-calculo
aliases:
  - PER_ACCRUAL_CALC_RULES
  - per_accrual_calc_rules
  - per-accrual-calc-rules
  - regras-de-cálculo-de-acumulação
  - per-accrual-calc-rul
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_ACCRUAL_CALC_RULES

## 📌 Visão Geral

Armazena as **regras de cálculo** aplicadas aos planos de acumulação de ausências. Define a fórmula, frequência e parâmetros de cálculo para accrual de saldos.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Definição de fórmulas** — especifica como o saldo de ausência é calculado.
- **Frequência de cálculo** — determina quando o accrual é processado (diário, mensal, etc.).
- **Parâmetros de carry-over** — regras para transporte de saldo entre períodos.
- **Personalização por plano** — cada plano pode ter regras de cálculo distintas.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ACCRUAL_CALC_RULE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da regra de cálculo | — | 🟢 90% |
| 2 | ACCRUAL_PLAN_ID | NUMBER(18) | NOT NULL | FK | Plano de acumulação associado | PER_ACCRUAL_PLANS_B | 🟢 90% |
| 3 | ACCRUAL_FORMULA_ID | NUMBER(18) | NULL | FK | Fórmula de cálculo (Fast Formula) | — | 🟡 75% |
| 4 | ACCRUAL_START_RULE | VARCHAR2(30) | NULL | Configuração | Regra de início do accrual | — | 🟡 75% |
| 5 | ACCRUAL_UOM | VARCHAR2(30) | NULL | Configuração | Unidade de medida do accrual (DAYS, HOURS) | — | 🟢 85% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_accrual_plans_b]] — via `ACCRUAL_PLAN_ID` (plano de acumulação pai)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha direta identificada.

---

## 📎 Uso Típico

### Regras de cálculo por plano
```sql
SELECT pcr.ACCRUAL_CALC_RULE_ID, pcr.ACCRUAL_START_RULE, pcr.ACCRUAL_UOM
FROM   PER_ACCRUAL_CALC_RULES pcr
WHERE  pcr.ACCRUAL_PLAN_ID = :p_accrual_plan_id;
```

### Filtros comuns
- `ACCRUAL_UOM = 'DAYS'` — Regras calculadas em dias
---

## 🔒 Observações

- As regras de cálculo determinam a lógica de acumulação aplicada aos colaboradores elegíveis.
- A fórmula de cálculo pode ser uma Fast Formula customizada do Oracle.
- O `ACCRUAL_START_RULE` define quando o colaborador começa a acumular (data de admissão, período probatório, etc.).
---

## 📚 Referências

- [Oracle Docs — PER_ACCRUAL_CALC_RULES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/peraccrualcalcrules.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
