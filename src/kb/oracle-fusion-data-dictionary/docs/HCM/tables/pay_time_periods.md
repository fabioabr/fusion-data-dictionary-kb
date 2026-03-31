---
id: DOC-HCM-600
doc_type: system-doc
title: "PAY_TIME_PERIODS — Periodos de Tempo de Folha"
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
  - time-periods
  - periodos
  - pay-time-periods
aliases:
  - PAY_TIME_PERIODS
  - pay_time_periods
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_TIME_PERIODS

## 📌 Visão Geral

Armazena os **periodos de tempo** (time periods) associados a cada folha de pagamento. Cada registro define um periodo de pagamento (ex.: janeiro/2026, quinzena 1/2026) com suas datas de inicio, fim e pagamento.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Definicao de periodos de pagamento por folha
- Controle de datas de processamento e pagamento
- Base para calculo de proventos e descontos por periodo
- Calendario de folha de pagamento

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TIME_PERIOD_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do periodo | --- | 🟢 95% |
| 2 | PAYROLL_ID | NUMBER(18) | NOT NULL | FK | ID da folha de pagamento | PAY_ALL_PAYROLLS_F | 🟢 95% |
| 3 | PERIOD_NAME | VARCHAR2(70) | NOT NULL | Identificacao | Nome do periodo | --- | 🟢 90% |
| 4 | START_DATE | DATE | NOT NULL | Vigencia | Data de inicio do periodo | --- | 🟢 95% |
| 5 | END_DATE | DATE | NOT NULL | Vigencia | Data de fim do periodo | --- | 🟢 95% |
| 6 | REGULAR_PAYMENT_DATE | DATE | NULL | Dados | Data de pagamento regular | --- | 🟢 85% |
| 7 | PERIOD_NUM | NUMBER | NOT NULL | Dados | Numero sequencial do periodo no ano | --- | 🟢 85% |
| 8 | PERIOD_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de periodo (Calendar Month, Semi-Month, etc.) | --- | 🟢 85% |
| 9 | STATUS | VARCHAR2(30) | NULL | Classificacao | Status do periodo (Open, Closed) | --- | 🟡 80% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pay_all_payrolls_f]] --- via `PAYROLL_ID` (folha de pagamento do período)

### Tabelas-filha (FK de saída)
- [[pay_payroll_actions]] --- via `TIME_PERIOD_ID` (ações processadas no período)

---

## 📎 Uso Típico

### Periodos abertos de uma folha
```sql
SELECT tp.TIME_PERIOD_ID, tp.PERIOD_NAME, tp.START_DATE, tp.END_DATE,
       tp.REGULAR_PAYMENT_DATE, tp.STATUS
FROM   PAY_TIME_PERIODS tp
WHERE  tp.PAYROLL_ID = :p_payroll_id
  AND  tp.STATUS = 'O'
ORDER BY tp.START_DATE;
```

---

## 🔒 Observações

- Os periodos sao gerados automaticamente com base no tipo de periodo da folha.
- O campo `REGULAR_PAYMENT_DATE` define quando o pagamento sera efetivado.
- Periodos com status 'O' (Open) sao elegiveis para processamento; 'C' (Closed) ja foram processados.

---

## 📚 Referências

- [Oracle Docs — PAY_TIME_PERIODS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/paytimeperiods.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
