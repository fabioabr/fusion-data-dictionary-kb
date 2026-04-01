---
id: DOC-HCM-597
doc_type: system-doc
title: "PAY_RUN_RESULTS — Resultados de Calculo de Folha"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: "Técnico"
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - payroll
  - run-results
  - resultados-calculo
  - pay-run-results
aliases:
  - PAY_RUN_RESULTS
  - pay_run_results
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_RUN_RESULTS

## 📌 Visão Geral

Tabela central que armazena os **resultados de calculo** (run results) gerados pelo processamento de folha. Cada registro contem o valor calculado de um elemento para um colaborador em um ciclo de processamento especifico.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Armazenamento dos valores calculados de cada elemento por colaborador
- Base para contracheques e relatorios de folha
- Reconciliacao de valores brutos e liquidos
- Historico completo de calculos de folha

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | RUN_RESULT_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do resultado | --- | 🟢 95% |
| 2 | PAYROLL_REL_ACTION_ID | NUMBER(18) | NOT NULL | FK | ID da acao por relacionamento | PAY_PAYROLL_REL_ACTIONS | 🟢 95% |
| 3 | ELEMENT_TYPE_ID | NUMBER(18) | NOT NULL | FK | ID do tipo de elemento | PAY_ELEMENT_TYPES_F | 🟢 95% |
| 4 | STATUS | VARCHAR2(30) | NULL | Classificacao | Status do resultado | --- | 🟡 80% |
| 5 | RESULT_VALUE | NUMBER | NULL | Dados | Valor do resultado calculado | --- | 🟢 85% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pay_payroll_rel_actions]] --- via `PAYROLL_REL_ACTION_ID` (ação por relacionamento do resultado de cálculo)
- [[pay_element_types_f]] --- via `ELEMENT_TYPE_ID` (tipo de elemento calculado no resultado)

### Tabelas-filha (FK de saída)
- --- Tabela de resultados granulares, sem filhas conhecidas

---

## 📎 Uso Típico

### Resultados de calculo de uma acao
```sql
SELECT rr.RUN_RESULT_ID, et.ELEMENT_NAME, rr.RESULT_VALUE
FROM   PAY_RUN_RESULTS rr
JOIN   PAY_ELEMENT_TYPES_F et ON et.ELEMENT_TYPE_ID = rr.ELEMENT_TYPE_ID
WHERE  rr.PAYROLL_REL_ACTION_ID = :p_rel_action_id;
```

---

## 🔒 Observações

- Tabela de alta volumetria: cada processamento gera um resultado por elemento por colaborador.
- Para valores detalhados (por input value), consultar run result values associados.
- Essencial para geracao de contracheques e relatorios de folha.

---

## 🔗 PVOs Relacionados

### [[payrollruncosting|PayrollRunCosting]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CALC_BREAKDOWN_ID | RunResultPEOCalcBreakdownId | — |
| RUN_RESULT_ID | RunResultPEORunResultId | — |
| TAX_UNIT_ID | RunResultPEOTaxUnitId | — |

---

## 📚 Referências

- [Oracle Docs — PAY_RUN_RESULTS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/payrunresults.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
