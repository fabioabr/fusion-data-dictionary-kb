---
id: DOC-HCM-588
doc_type: system-doc
title: "PAY_PAYROLL_ACTIONS — Acoes de Folha de Pagamento"
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
  - payroll-actions
  - acoes-folha
  - pay-actions
aliases:
  - PAY_PAYROLL_ACTIONS
  - pay_payroll_actions
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_PAYROLL_ACTIONS

## 📌 Visão Geral

Armazena as **acoes de folha** (payroll actions) que representam cada execucao de processamento. Cada acao corresponde a um ciclo de calculo, retroativo, QuickPay, ou processamento especial.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Registro de cada execucao de processamento de folha
- Controle de status e parametros de processamento
- Auditoria de ciclos de calculo de folha
- Base para rastreamento de resultados de calculo

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PAYROLL_ACTION_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da acao | --- | 🟢 95% |
| 2 | PAYROLL_ID | NUMBER(18) | NOT NULL | FK | ID da folha de pagamento | PAY_ALL_PAYROLLS_F | 🟢 95% |
| 3 | ACTION_TYPE | VARCHAR2(30) | NOT NULL | Classificacao | Tipo de acao (R=Regular, Q=QuickPay, B=Balance Adj) | --- | 🟢 90% |
| 4 | ACTION_STATUS | VARCHAR2(1) | NOT NULL | Classificacao | Status (C=Complete, E=Error, U=Unprocessed) | --- | 🟢 90% |
| 5 | TIME_PERIOD_ID | NUMBER(18) | NULL | FK | ID do periodo de tempo | PAY_TIME_PERIODS | 🟢 85% |
| 6 | EFFECTIVE_DATE | DATE | NULL | Vigencia | Data efetiva da acao | --- | 🟢 90% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pay_all_payrolls_f]] --- via `PAYROLL_ID` (folha de pagamento da aÃ§Ã£o processada)
- [[pay_time_periods]] --- via `TIME_PERIOD_ID` (perÃ­odo de tempo da aÃ§Ã£o de folha)

### Tabelas-filha (FK de saída)
- [[pay_payroll_rel_actions]] --- via `PAYROLL_ACTION_ID` (aÃ§Ãµes por relacionamento da aÃ§Ã£o de folha)
- [[pay_run_results]] --- via `PAYROLL_ACTION_ID` (resultados de cÃ¡lculo da aÃ§Ã£o de folha)

---

## 📎 Uso Típico

### Acoes completadas de uma folha
```sql
SELECT pa.PAYROLL_ACTION_ID, pa.ACTION_TYPE, pa.ACTION_STATUS, pa.EFFECTIVE_DATE
FROM   PAY_PAYROLL_ACTIONS pa
WHERE  pa.PAYROLL_ID = :p_payroll_id
  AND  pa.ACTION_STATUS = 'C'
ORDER BY pa.EFFECTIVE_DATE DESC;
```

---

## 🔒 Observações

- Tabela do modulo Payroll do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 📚 Referências

- [Oracle Docs — PAY_PAYROLL_ACTIONS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/paypayrollactions.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
