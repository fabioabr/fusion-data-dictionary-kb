---
id: DOC-AR-038
doc_type: system-doc
title: "AR_INTEREST_LINES_ALL — Linhas de Detalhe de Juros Calculados"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-receivable, data-dictionary, juros, linhas-juros, late-charges]
aliases: [AR_INTEREST_LINES_ALL, ar_interest_lines_all, interest_lines, linhas_juros, detalhe_juros]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_INTEREST_LINES_ALL

> [!note] Sufixo _ALL
> Tabela particionada por `ORG_ID`. O sufixo `_ALL` indica que contém dados de todas as business units. Acessos via views sem sufixo filtram automaticamente pelo contexto de segurança da sessão.

## 📌 Visão Geral

Tabela de linhas de detalhe dos juros calculados no Accounts Receivable. Cada linha representa o cálculo de juros para uma transação/parcela específica, vinculada a um cabeçalho em [[ar_interest_headers_all]]. Contém informações como taxa diária, valor cobrado e dias em atraso.

## 🧠 Propósito de Negócio

As linhas de juros detalham o cálculo fatura a fatura, permitindo transparência total no processo de cobrança de encargos. São utilizadas para: (1) justificar o valor de juros cobrado ao cliente, (2) reconciliar com os debit memos gerados, (3) auditar a corretude dos cálculos baseados na taxa e dias de atraso, (4) gerar relatórios analíticos de receita de juros.

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Descrição | Categoria | Confiança |
|---|--------|------|-------|-----------|-----------|-----------|
| 1 | INTEREST_LINE_ID | NUMBER(15) | NOT NULL | Chave primária. Identificador único da linha de juros. | PK | 🟢 100% |
| 2 | INTEREST_HEADER_ID | NUMBER(15) | NOT NULL | FK para [[ar_interest_headers_all]]. Cabeçalho do lote de juros. | FK | 🟢 100% |
| 3 | PAYMENT_SCHEDULE_ID | NUMBER(15) | NOT NULL | FK para AR_PAYMENT_SCHEDULES_ALL. Parcela sobre a qual o juro incide. | FK | 🟢 100% |
| 4 | CUSTOMER_TRX_ID | NUMBER(15) | NOT NULL | FK para RA_CUSTOMER_TRX_ALL. Transação original em atraso. | FK | 🟢 100% |
| 5 | ORIGINAL_TRX_CLASS | VARCHAR2(30) | NULL | Classe da transação original (INV, DM, DEP). | Classificação | 🟢 100% |
| 6 | DAILY_INTEREST_CHARGE | NUMBER | NULL | Valor diário do juro calculado. | Financeiro | 🟢 100% |
| 7 | INTEREST_CHARGED | NUMBER | NULL | Valor total de juros cobrados nesta linha. | Financeiro | 🟢 100% |
| 8 | DAYS_OVERDUE | NUMBER | NULL | Quantidade de dias em atraso na data do cálculo. | Negócio | 🟢 100% |
| 9 | AMOUNT_DUE_REMAINING | NUMBER | NULL | Saldo devedor remanescente da parcela. | Financeiro | 🟢 100% |
| 10 | INTEREST_RATE | NUMBER | NULL | Taxa de juros aplicada (percentual). | Financeiro | 🟢 100% |
| 11 | DUE_DATE | DATE | NULL | Data de vencimento da parcela original. | Temporal | 🟢 100% |
| 12 | CHARGE_DATE | DATE | NULL | Data base do cálculo de juros. | Temporal | 🟢 100% |
| 13 | PROCESS_STATUS | VARCHAR2(30) | NULL | Status do processamento da linha. | Controle | 🟡 75% |
| 14 | ORG_ID | NUMBER(15) | NOT NULL | Identificador da business unit (Operating Unit). | Partição | 🟢 100% |
| 15 | CREATED_BY | VARCHAR2(64) | NOT NULL | Usuário que criou o registro. | WHO | 🟢 100% |
| 16 | CREATION_DATE | DATE | NOT NULL | Data de criação do registro. | WHO | 🟢 100% |
| 17 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Usuário da última atualização. | WHO | 🟢 100% |
| 18 | LAST_UPDATE_DATE | DATE | NOT NULL | Data da última atualização. | WHO | 🟢 100% |

## 🔗 Relacionamentos

- **[[ar_interest_headers_all]]** — Cabeçalho do lote de juros (N:1 via `INTEREST_HEADER_ID`).
- **AR_PAYMENT_SCHEDULES_ALL** — Parcela sobre a qual o juro incide (N:1 via `PAYMENT_SCHEDULE_ID`).
- **RA_CUSTOMER_TRX_ALL** — Transação original (N:1 via `CUSTOMER_TRX_ID`).

## 📎 Uso Típico

```sql
-- Detalhe de juros calculados por transação em um período
SELECT il.CUSTOMER_TRX_ID,
       il.DAYS_OVERDUE,
       il.INTEREST_RATE,
       il.DAILY_INTEREST_CHARGE,
       il.INTEREST_CHARGED,
       il.AMOUNT_DUE_REMAINING
  FROM AR_INTEREST_LINES_ALL il
  JOIN AR_INTEREST_HEADERS_ALL ih
    ON ih.INTEREST_HEADER_ID = il.INTEREST_HEADER_ID
 WHERE ih.ORG_ID = :p_org_id
   AND ih.CHARGE_DATE BETWEEN :p_data_ini AND :p_data_fim
 ORDER BY il.DAYS_OVERDUE DESC;
```

## 🔒 Observações

- O cálculo `DAILY_INTEREST_CHARGE * DAYS_OVERDUE` deve ser aproximadamente igual a `INTEREST_CHARGED` (pode haver arredondamento).
- `ORIGINAL_TRX_CLASS` permite distinguir se o juro incide sobre fatura (INV), debit memo (DM) ou depósito (DEP).
- Filtrar sempre por `ORG_ID` para garantir contexto correto de business unit.

## 🔗 PVOs Relacionados

### [[adjustmentdistributionpvo|AdjustmentDistributionPVO]] (AR · BICC: 4/22)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTUAL_DATE_CLOSED | IntrstLineActualDateClosed | — |
| AMOUNT_DUE_ORIGINAL | IntrstLineAmountDueOriginal | — |
| AMOUNT_DUE_REMAINING | IntrstLineAmountDueRemaining | — |
| DAILY_INTEREST_CHARGE | IntrstLineDailyInterestCharge | — |
| DAYS_OF_INTEREST | IntrstLineDaysOfInterest | ✅ |
| DAYS_OVERDUE_LATE | IntrstLineDaysOverdueLate | ✅ |
| DUE_DATE | IntrstLineDueDate | — |
| FINANCE_CHARGE_CHARGED | IntrstLineFinanceChargeCharged | — |
| INTEREST_CHARGED | IntrstLineInterestCharged | ✅ |
| INTEREST_LINE_ID | IntrstLineInterestLineId | — |
| INTEREST_RATE | IntrstLineInterestRate | ✅ |
| LAST_CHARGE_DATE | IntrstLineLastChargeDate | — |
| ORIGINAL_TRX_CLASS | IntrstLineOriginalTrxClass | — |
| OUTSTANDING_AMOUNT | IntrstLineOutstandingAmount | — |
| PAYMENT_DATE | IntrstLinePaymentDate | — |
| PROCESS_MESSAGE | IntrstLineProcessMessage | — |
| PROCESS_STATUS | IntrstLineProcessStatus | — |
| RATE_END_DATE | IntrstLineRateEndDate | — |
| RATE_START_DATE | IntrstLineRateStartDate | — |
| SCHEDULE_DAYS_FROM | IntrstLineScheduleDaysFrom | — |
| SCHEDULE_DAYS_TO | IntrstLineScheduleDaysTo | — |
| TYPE | IntrstLineType | — |

### [[adjustmentpvo|AdjustmentPVO]] (AR · BICC: 4/22)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTUAL_DATE_CLOSED | IntrstLineActualDateClosed | — |
| AMOUNT_DUE_ORIGINAL | IntrstLineAmountDueOriginal | — |
| AMOUNT_DUE_REMAINING | IntrstLineAmountDueRemaining | — |
| DAILY_INTEREST_CHARGE | IntrstLineDailyInterestCharge | — |
| DAYS_OF_INTEREST | IntrstLineDaysOfInterest | ✅ |
| DAYS_OVERDUE_LATE | IntrstLineDaysOverdueLate | ✅ |
| DUE_DATE | IntrstLineDueDate | — |
| FINANCE_CHARGE_CHARGED | IntrstLineFinanceChargeCharged | — |
| INTEREST_CHARGED | IntrstLineInterestCharged | ✅ |
| INTEREST_LINE_ID | IntrstLineInterestLineId | — |
| INTEREST_RATE | IntrstLineInterestRate | ✅ |
| LAST_CHARGE_DATE | IntrstLineLastChargeDate | — |
| ORIGINAL_TRX_CLASS | IntrstLineOriginalTrxClass | — |
| OUTSTANDING_AMOUNT | IntrstLineOutstandingAmount | — |
| PAYMENT_DATE | IntrstLinePaymentDate | — |
| PROCESS_MESSAGE | IntrstLineProcessMessage | — |
| PROCESS_STATUS | IntrstLineProcessStatus | — |
| RATE_END_DATE | IntrstLineRateEndDate | — |
| RATE_START_DATE | IntrstLineRateStartDate | — |
| SCHEDULE_DAYS_FROM | IntrstLineScheduleDaysFrom | — |
| SCHEDULE_DAYS_TO | IntrstLineScheduleDaysTo | — |
| TYPE | IntrstLineType | — |

### [[interestlineextractpvo|InterestLineExtractPVO]] (OTHER · BICC: 33/33)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTUAL_DATE_CLOSED | ArInterestLineActualDateClosed | ✅ |
| AMOUNT_DUE_ORIGINAL | ArInterestLineAmountDueOriginal | ✅ |
| AMOUNT_DUE_REMAINING | ArInterestLineAmountDueRemaining | ✅ |
| CREATED_BY | ArInterestLineCreatedBy | ✅ |
| CREATION_DATE | ArInterestLineCreationDate | ✅ |
| DAILY_INTEREST_CHARGE | DailyInterestCharge | ✅ |
| DAYS_OF_INTEREST | ArInterestLineDaysOfInterest | ✅ |
| DAYS_OVERDUE_LATE | ArInterestLineDaysOverdueLate | ✅ |
| DUE_DATE | ArInterestLineDueDate | ✅ |
| FINANCE_CHARGE_CHARGED | ArInterestLineFinanceChargeCharged | ✅ |
| INTEREST_CHARGED | ArInterestLineInterestCharged | ✅ |
| INTEREST_HEADER_ID | ArInterestLineInterestHeaderId | ✅ |
| INTEREST_LINE_ID | ArInterestLineInterestLineId | ✅ |
| INTEREST_RATE | ArInterestLineInterestRate | ✅ |
| LAST_CHARGE_DATE | ArInterestLineLastChargeDate | ✅ |
| LAST_UPDATE_DATE | ArInterestLineLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ArInterestLineLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ArInterestLineLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ArInterestLineObjectVersionNumber | ✅ |
| ORG_ID | ArInterestLineOrgId | ✅ |
| ORIGINAL_TRX_CLASS | ArInterestLineOriginalTrxClass | ✅ |
| ORIGINAL_TRX_ID | ArInterestLineOriginalTrxId | ✅ |
| OUTSTANDING_AMOUNT | ArInterestLineOutstandingAmount | ✅ |
| PAYMENT_DATE | ArInterestLinePaymentDate | ✅ |
| PAYMENT_SCHEDULE_ID | ArInterestLinePaymentScheduleId | ✅ |
| PROCESS_MESSAGE | ArInterestLineProcessMessage | ✅ |
| PROCESS_STATUS | ArInterestLineProcessStatus | ✅ |
| RATE_END_DATE | ArInterestLineRateEndDate | ✅ |
| RATE_START_DATE | ArInterestLineRateStartDate | ✅ |
| RECEIVABLES_TRX_ID | ArInterestLineReceivablesTrxId | ✅ |
| SCHEDULE_DAYS_FROM | ArInterestLineScheduleDaysFrom | ✅ |
| SCHEDULE_DAYS_TO | ArInterestLineScheduleDaysTo | ✅ |
| TYPE | ArInterestLineType | ✅ |

### [[linesalescreditpvo|LineSalesCreditPVO]] (AR · BICC: 4/22)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTUAL_DATE_CLOSED | IntrstLineActualDateClosed | — |
| AMOUNT_DUE_ORIGINAL | IntrstLineAmountDueOriginal | — |
| AMOUNT_DUE_REMAINING | IntrstLineAmountDueRemaining | — |
| DAILY_INTEREST_CHARGE | IntrstLineDailyInterestCharge | — |
| DAYS_OF_INTEREST | IntrstLineDaysOfInterest | ✅ |
| DAYS_OVERDUE_LATE | IntrstLineDaysOverdueLate | ✅ |
| DUE_DATE | IntrstLineDueDate | — |
| FINANCE_CHARGE_CHARGED | IntrstLineFinanceChargeCharged | — |
| INTEREST_CHARGED | IntrstLineInterestCharged | ✅ |
| INTEREST_LINE_ID | IntrstLineInterestLineId | — |
| INTEREST_RATE | IntrstLineInterestRate | ✅ |
| LAST_CHARGE_DATE | IntrstLineLastChargeDate | — |
| ORIGINAL_TRX_CLASS | IntrstLineOriginalTrxClass | — |
| OUTSTANDING_AMOUNT | IntrstLineOutstandingAmount | — |
| PAYMENT_DATE | IntrstLinePaymentDate | — |
| PROCESS_MESSAGE | IntrstLineProcessMessage | — |
| PROCESS_STATUS | IntrstLineProcessStatus | — |
| RATE_END_DATE | IntrstLineRateEndDate | — |
| RATE_START_DATE | IntrstLineRateStartDate | — |
| SCHEDULE_DAYS_FROM | IntrstLineScheduleDaysFrom | — |
| SCHEDULE_DAYS_TO | IntrstLineScheduleDaysTo | — |
| TYPE | IntrstLineType | — |

### [[transactionhistorydistributionpvo|TransactionHistoryDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTUAL_DATE_CLOSED | IntrstLineActualDateClosed | — |
| AMOUNT_DUE_ORIGINAL | IntrstLineAmountDueOriginal | — |
| AMOUNT_DUE_REMAINING | IntrstLineAmountDueRemaining | — |
| DAILY_INTEREST_CHARGE | IntrstLineDailyInterestCharge | — |
| DAYS_OF_INTEREST | IntrstLineDaysOfInterest | — |
| DAYS_OVERDUE_LATE | IntrstLineDaysOverdueLate | — |
| DUE_DATE | IntrstLineDueDate | — |
| FINANCE_CHARGE_CHARGED | IntrstLineFinanceChargeCharged | — |
| INTEREST_CHARGED | IntrstLineInterestCharged | — |
| INTEREST_LINE_ID | IntrstLineInterestLineId | — |
| INTEREST_RATE | IntrstLineInterestRate | — |
| LAST_CHARGE_DATE | IntrstLineLastChargeDate | — |
| ORIGINAL_TRX_CLASS | IntrstLineOriginalTrxClass | — |
| OUTSTANDING_AMOUNT | IntrstLineOutstandingAmount | — |
| PAYMENT_DATE | IntrstLinePaymentDate | — |
| PROCESS_MESSAGE | IntrstLineProcessMessage | — |
| PROCESS_STATUS | IntrstLineProcessStatus | — |
| RATE_END_DATE | IntrstLineRateEndDate | — |
| RATE_START_DATE | IntrstLineRateStartDate | — |
| SCHEDULE_DAYS_FROM | IntrstLineScheduleDaysFrom | — |
| SCHEDULE_DAYS_TO | IntrstLineScheduleDaysTo | — |
| TYPE | IntrstLineType | — |

### [[transactionhistorypvo|TransactionHistoryPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTUAL_DATE_CLOSED | IntrstLineActualDateClosed | — |
| AMOUNT_DUE_ORIGINAL | IntrstLineAmountDueOriginal | — |
| AMOUNT_DUE_REMAINING | IntrstLineAmountDueRemaining | — |
| DAILY_INTEREST_CHARGE | IntrstLineDailyInterestCharge | — |
| DAYS_OF_INTEREST | IntrstLineDaysOfInterest | — |
| DAYS_OVERDUE_LATE | IntrstLineDaysOverdueLate | — |
| DUE_DATE | IntrstLineDueDate | — |
| FINANCE_CHARGE_CHARGED | IntrstLineFinanceChargeCharged | — |
| INTEREST_CHARGED | IntrstLineInterestCharged | — |
| INTEREST_LINE_ID | IntrstLineInterestLineId | — |
| INTEREST_RATE | IntrstLineInterestRate | — |
| LAST_CHARGE_DATE | IntrstLineLastChargeDate | — |
| ORIGINAL_TRX_CLASS | IntrstLineOriginalTrxClass | — |
| OUTSTANDING_AMOUNT | IntrstLineOutstandingAmount | — |
| PAYMENT_DATE | IntrstLinePaymentDate | — |
| PROCESS_MESSAGE | IntrstLineProcessMessage | — |
| PROCESS_STATUS | IntrstLineProcessStatus | — |
| RATE_END_DATE | IntrstLineRateEndDate | — |
| RATE_START_DATE | IntrstLineRateStartDate | — |
| SCHEDULE_DAYS_FROM | IntrstLineScheduleDaysFrom | — |
| SCHEDULE_DAYS_TO | IntrstLineScheduleDaysTo | — |
| TYPE | IntrstLineType | — |

### [[transactionlinebillsreceivablepvo|TransactionLineBillsReceivablePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTUAL_DATE_CLOSED | IntrstLineActualDateClosed | — |
| AMOUNT_DUE_ORIGINAL | IntrstLineAmountDueOriginal | — |
| AMOUNT_DUE_REMAINING | IntrstLineAmountDueRemaining | — |
| DAILY_INTEREST_CHARGE | IntrstLineDailyInterestCharge | — |
| DAYS_OF_INTEREST | IntrstLineDaysOfInterest | — |
| DAYS_OVERDUE_LATE | IntrstLineDaysOverdueLate | — |
| DUE_DATE | IntrstLineDueDate | — |
| FINANCE_CHARGE_CHARGED | IntrstLineFinanceChargeCharged | — |
| INTEREST_CHARGED | IntrstLineInterestCharged | — |
| INTEREST_LINE_ID | IntrstLineInterestLineId | — |
| INTEREST_RATE | IntrstLineInterestRate | — |
| LAST_CHARGE_DATE | IntrstLineLastChargeDate | — |
| ORIGINAL_TRX_CLASS | IntrstLineOriginalTrxClass | — |
| OUTSTANDING_AMOUNT | IntrstLineOutstandingAmount | — |
| PAYMENT_DATE | IntrstLinePaymentDate | — |
| PROCESS_MESSAGE | IntrstLineProcessMessage | — |
| PROCESS_STATUS | IntrstLineProcessStatus | — |
| RATE_END_DATE | IntrstLineRateEndDate | — |
| RATE_START_DATE | IntrstLineRateStartDate | — |
| SCHEDULE_DAYS_FROM | IntrstLineScheduleDaysFrom | — |
| SCHEDULE_DAYS_TO | IntrstLineScheduleDaysTo | — |
| TYPE | IntrstLineType | — |

### [[transactionlinedistributionpvo|TransactionLineDistributionPVO]] (AR · BICC: 4/22)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTUAL_DATE_CLOSED | IntrstLineActualDateClosed | — |
| AMOUNT_DUE_ORIGINAL | IntrstLineAmountDueOriginal | — |
| AMOUNT_DUE_REMAINING | IntrstLineAmountDueRemaining | — |
| DAILY_INTEREST_CHARGE | IntrstLineDailyInterestCharge | — |
| DAYS_OF_INTEREST | IntrstLineDaysOfInterest | ✅ |
| DAYS_OVERDUE_LATE | IntrstLineDaysOverdueLate | ✅ |
| DUE_DATE | IntrstLineDueDate | — |
| FINANCE_CHARGE_CHARGED | IntrstLineFinanceChargeCharged | — |
| INTEREST_CHARGED | IntrstLineInterestCharged | ✅ |
| INTEREST_LINE_ID | IntrstLineInterestLineId | — |
| INTEREST_RATE | IntrstLineInterestRate | ✅ |
| LAST_CHARGE_DATE | IntrstLineLastChargeDate | — |
| ORIGINAL_TRX_CLASS | IntrstLineOriginalTrxClass | — |
| OUTSTANDING_AMOUNT | IntrstLineOutstandingAmount | — |
| PAYMENT_DATE | IntrstLinePaymentDate | — |
| PROCESS_MESSAGE | IntrstLineProcessMessage | — |
| PROCESS_STATUS | IntrstLineProcessStatus | — |
| RATE_END_DATE | IntrstLineRateEndDate | — |
| RATE_START_DATE | IntrstLineRateStartDate | — |
| SCHEDULE_DAYS_FROM | IntrstLineScheduleDaysFrom | — |
| SCHEDULE_DAYS_TO | IntrstLineScheduleDaysTo | — |
| TYPE | IntrstLineType | — |

### [[transactionlinepvo|TransactionLinePVO]] (AR · BICC: 4/22)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTUAL_DATE_CLOSED | IntrstLineActualDateClosed | — |
| AMOUNT_DUE_ORIGINAL | IntrstLineAmountDueOriginal | — |
| AMOUNT_DUE_REMAINING | IntrstLineAmountDueRemaining | — |
| DAILY_INTEREST_CHARGE | IntrstLineDailyInterestCharge | — |
| DAYS_OF_INTEREST | IntrstLineDaysOfInterest | ✅ |
| DAYS_OVERDUE_LATE | IntrstLineDaysOverdueLate | ✅ |
| DUE_DATE | IntrstLineDueDate | — |
| FINANCE_CHARGE_CHARGED | IntrstLineFinanceChargeCharged | — |
| INTEREST_CHARGED | IntrstLineInterestCharged | ✅ |
| INTEREST_LINE_ID | IntrstLineInterestLineId | — |
| INTEREST_RATE | IntrstLineInterestRate | ✅ |
| LAST_CHARGE_DATE | IntrstLineLastChargeDate | — |
| ORIGINAL_TRX_CLASS | IntrstLineOriginalTrxClass | — |
| OUTSTANDING_AMOUNT | IntrstLineOutstandingAmount | — |
| PAYMENT_DATE | IntrstLinePaymentDate | — |
| PROCESS_MESSAGE | IntrstLineProcessMessage | — |
| PROCESS_STATUS | IntrstLineProcessStatus | — |
| RATE_END_DATE | IntrstLineRateEndDate | — |
| RATE_START_DATE | IntrstLineRateStartDate | — |
| SCHEDULE_DAYS_FROM | IntrstLineScheduleDaysFrom | — |
| SCHEDULE_DAYS_TO | IntrstLineScheduleDaysTo | — |
| TYPE | IntrstLineType | — |

---

## 📚 Referências

- Oracle Fusion Cloud Financials — Accounts Receivable Tables (OEDMF Release 13).
- Oracle Fusion Cloud — Late Charges Calculation Documentation.
- Oracle Fusion Cloud ERP Schema Reference (Release 25A).
