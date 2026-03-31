---
id: DOC-HCM-559
doc_type: system-doc
title: "PAY_COSTS — Custos de Folha de Pagamento"
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
  - costs
  - custos
  - pay-costs
aliases:
  - PAY_COSTS
  - pay_costs
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_COSTS

## 📌 Visão Geral

Armazena os **custos** (cost allocations) gerados pelo processamento de folha de pagamento. Cada registro representa uma distribuicao de custo contabil associada a um resultado de calculo.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Distribuicao contabil de custos de folha
- Integracao com modulo de contabilidade (GL)
- Relatorios de custo de pessoal por centro de custo
- Reconciliacao financeira de folha de pagamento

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | COST_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do custo | --- | 🟢 90% |
| 2 | PAYROLL_REL_ACTION_ID | NUMBER(18) | NOT NULL | FK | ID da acao de folha | PAY_PAYROLL_REL_ACTIONS | 🟢 85% |
| 3 | COST_ALLOCATION_KEYFLEX_ID | NUMBER(18) | NULL | FK | ID da combinacao de segmentos contabeis | --- | 🟢 80% |
| 4 | COSTED_VALUE | NUMBER | NULL | Dados | Valor do custo | --- | 🟢 85% |
| 5 | BALANCE_TYPE_ID | NUMBER(18) | NULL | FK | ID do tipo de saldo | --- | 🟡 75% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pay_payroll_rel_actions]] --- via `PAYROLL_REL_ACTION_ID` (ação de folha que gerou o custo)

### Tabelas-filha (FK de saída)
- [[pay_payment_costs]] --- via `COST_ID` (custos de pagamento)

---

## 📎 Uso Típico

### Custos por acao de folha
```sql
SELECT c.COST_ID, c.COSTED_VALUE, c.COST_ALLOCATION_KEYFLEX_ID
FROM   PAY_COSTS c
WHERE  c.PAYROLL_REL_ACTION_ID = :p_rel_action_id;
```

---

## 🔒 Observações

- Tabela do modulo Payroll do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 🔗 PVOs Relacionados

### [[payrollruncosting|PayrollRunCosting]] (GL · BICC: 11/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BALANCE_OR_COST | PayCostBalanceOrCost | ✅ |
| COST_ALLOCATION_KEYFLEX_ID | PayCostCostAllocationKeyflexId | — |
| COST_ID | CostId | ✅ |
| COSTED_VALUE | PayCostCostedValue | ✅ |
| DEBIT_OR_CREDIT | PayCostDebitOrCredit | ✅ |
| DISTRIBUTED_INPUT_VALUE_ID | PayCostDistributedInputValueId | — |
| DISTRIBUTED_RUN_RESULT_ID | PayCostDistributedRunResultId | — |
| END_DATE | PayCostEndDate | — |
| ID_FLEX_NUM | PayCostIdFlexNum | ✅ |
| INPUT_VALUE_ID | PayCostInputValueId | — |
| PAYROLL_REL_ACTION_ID | PayCostPayrollRelationshipActionId | — |
| RUN_RESULT_ID | PayCostRunResultId | ✅ |
| SECONDARY_STATUS | PayCostSecondaryStatus | ✅ |
| SEQUENCE | PayCostSequence | ✅ |
| SOURCE_ID | PayCostSourceId | ✅ |
| START_DATE | PayCostStartDate | — |
| STATUS | PayCostStatus | ✅ |
| TRANSFER_TO_GL_FLAG | PayCostTransferToGlFlag | ✅ |

---

## 📚 Referências

- [Oracle Docs — PAY_COSTS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/paycosts.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
