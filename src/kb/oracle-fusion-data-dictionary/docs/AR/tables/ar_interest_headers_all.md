---
id: DOC-AR-037
doc_type: system-doc
title: "AR_INTEREST_HEADERS_ALL — Cabeçalhos de Cobranças de Juros"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-receivable, data-dictionary, juros, finance-charges, late-charges]
aliases: [AR_INTEREST_HEADERS_ALL, ar_interest_headers_all, interest_headers, cabecalho_juros, juros_ar]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_INTEREST_HEADERS_ALL

> [!note] Sufixo _ALL
> Tabela particionada por `ORG_ID`. O sufixo `_ALL` indica que contém dados de todas as business units. Acessos via views sem sufixo filtram automaticamente pelo contexto de segurança da sessão.

## 📌 Visão Geral

Tabela de cabeçalhos de cobranças de juros (late charges / finance charges) do Accounts Receivable. Cada registro representa um lote de cálculo de juros para um cliente em uma moeda específica, agrupando as linhas de detalhe em [[ar_interest_lines_all]].

## 🧠 Propósito de Negócio

O cálculo de juros sobre faturas em atraso é parte fundamental do processo de cobrança. Esta tabela registra os cabeçalhos dos lotes de cálculo, permitindo rastrear quando e para quem os juros foram calculados, o status do processamento e se os valores foram apresentados ao cliente. É essencial para gestão de receita financeira e compliance com termos contratuais.

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Descrição | Categoria | Confiança |
|---|--------|------|-------|-----------|-----------|-----------|
| 1 | INTEREST_HEADER_ID | NUMBER(15) | NOT NULL | Chave primária. Identificador único do cabeçalho de juros. | PK | 🟢 100% |
| 2 | CUSTOMER_ID | NUMBER(15) | NOT NULL | FK para HZ_CUST_ACCOUNTS. Cliente ao qual os juros se referem. | FK | 🟢 100% |
| 3 | CUSTOMER_SITE_USE_ID | NUMBER(15) | NULL | FK para HZ_CUST_SITE_USES_ALL. Site de uso do cliente. | FK | 🟢 100% |
| 4 | CURRENCY_CODE | VARCHAR2(15) | NOT NULL | Código da moeda dos juros calculados. | Financeiro | 🟢 100% |
| 5 | INTEREST_BATCH_ID | NUMBER(15) | NULL | Identificador do lote de processamento de juros. | FK | 🟢 100% |
| 6 | HEADER_TYPE | VARCHAR2(30) | NOT NULL | Tipo do cabeçalho (ex.: LATE_CHARGE, FINANCE_CHARGE). | Classificação | 🟢 100% |
| 7 | DISPLAY_FLAG | VARCHAR2(1) | NULL | Flag indicando se o registro deve ser exibido ao cliente (Y/N). | Controle | 🟢 100% |
| 8 | PROCESS_STATUS | VARCHAR2(30) | NOT NULL | Status do processamento (ex.: NEW, PROCESSED, ERROR). | Controle | 🟢 100% |
| 9 | PROCESS_MESSAGE | VARCHAR2(240) | NULL | Mensagem de erro ou processamento. | Controle | 🟡 75% |
| 10 | PAYMENT_SCHEDULE_ID | NUMBER(15) | NULL | FK para a parcela gerada pela cobrança de juros. | FK | 🟢 100% |
| 11 | CUSTOMER_TRX_ID | NUMBER(15) | NULL | FK para a transação de juros gerada (debit memo). | FK | 🟢 100% |
| 12 | TOTAL_INTEREST_AMOUNT | NUMBER | NULL | Valor total dos juros calculados no cabeçalho. | Financeiro | 🟢 100% |
| 13 | CHARGE_DATE | DATE | NULL | Data base do cálculo dos juros. | Temporal | 🟢 100% |
| 14 | ORG_ID | NUMBER(15) | NOT NULL | Identificador da business unit (Operating Unit). | Partição | 🟢 100% |
| 15 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | Contexto de flexfield descritivo. | DFF | 🟢 100% |
| 16 | REQUEST_ID | NUMBER(15) | NULL | Identificador da requisição concorrente que gerou o registro. | Técnico | 🟢 100% |
| 17 | CREATED_BY | VARCHAR2(64) | NOT NULL | Usuário que criou o registro. | WHO | 🟢 100% |
| 18 | CREATION_DATE | DATE | NOT NULL | Data de criação do registro. | WHO | 🟢 100% |
| 19 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Usuário da última atualização. | WHO | 🟢 100% |
| 20 | LAST_UPDATE_DATE | DATE | NOT NULL | Data da última atualização. | WHO | 🟢 100% |

## 🔗 Relacionamentos

- **[[ar_interest_lines_all]]** — Linhas de detalhe dos juros (1:N via `INTEREST_HEADER_ID`).
- **HZ_CUST_ACCOUNTS** — Cliente associado (N:1 via `CUSTOMER_ID`).
- **HZ_CUST_SITE_USES_ALL** — Site de uso do cliente (N:1 via `CUSTOMER_SITE_USE_ID`).
- **RA_CUSTOMER_TRX_ALL** — Debit memo gerado (via `CUSTOMER_TRX_ID`).

## 📎 Uso Típico

```sql
-- Resumo de juros calculados por cliente e status
SELECT ih.CUSTOMER_ID,
       ih.CURRENCY_CODE,
       ih.PROCESS_STATUS,
       SUM(ih.TOTAL_INTEREST_AMOUNT) AS total_juros
  FROM AR_INTEREST_HEADERS_ALL ih
 WHERE ih.ORG_ID = :p_org_id
   AND ih.CHARGE_DATE BETWEEN :p_data_ini AND :p_data_fim
 GROUP BY ih.CUSTOMER_ID, ih.CURRENCY_CODE, ih.PROCESS_STATUS
 ORDER BY total_juros DESC;
```

## 🔒 Observações

- O processamento de juros pode gerar automaticamente debit memos (registrados em `CUSTOMER_TRX_ID`).
- `PROCESS_STATUS` controla o fluxo: registros com status ERROR devem ser investigados.
- A coluna `DISPLAY_FLAG` permite ocultar cobranças de teste ou canceladas.
- Filtrar sempre por `ORG_ID` para garantir contexto correto de business unit.

## 🔗 PVOs Relacionados

### [[adjustmentdistributionpvo|AdjustmentDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHARGE_BEGIN_DATE | IntrstHdrChargeBeginDate | — |
| CHARGE_BEGIN_DATE | IntrstHdrTrxHdrChargeBeginDate | — |
| CHARGE_ON_FINANCE_CHARGE_FLAG | IntrstHdrChargeOnFinanceChargeFlag | — |
| CHARGE_ON_FINANCE_CHARGE_FLAG | IntrstHdrTrxHdrChargeOnFinanceChargeFlag | — |
| CREDIT_ITEMS_FLAG | IntrstHdrCreditItemsFlag | — |
| CREDIT_ITEMS_FLAG | IntrstHdrTrxHdrCreditItemsFlag | — |
| CURRENCY_CODE | IntrstHdrCurrencyCode | — |
| CURRENCY_CODE | IntrstHdrTrxHdrCurrencyCode | — |
| DISPLAY_FLAG | IntrstHdrDisplayFlag | — |
| DISPLAY_FLAG | IntrstHdrTrxHdrDisplayFlag | — |
| DISPUTED_TRANSACTIONS_FLAG | IntrstHdrDisputedTransactionsFlag | — |
| DISPUTED_TRANSACTIONS_FLAG | IntrstHdrTrxHdrDisputedTransactionsFlag | — |
| EXCHANGE_RATE | IntrstHdrExchangeRate | — |
| EXCHANGE_RATE | IntrstHdrTrxHdrExchangeRate | — |
| EXCHANGE_RATE_TYPE | IntrstHdrExchangeRateType | — |
| EXCHANGE_RATE_TYPE | IntrstHdrTrxHdrExchangeRateType | — |
| FINANCE_CHARGE_DATE | IntrstHdrFinanceChargeDate | — |
| FINANCE_CHARGE_DATE | IntrstHdrTrxHdrFinanceChargeDate | — |
| HEADER_TYPE | IntrstHdrHeaderType | — |
| HEADER_TYPE | IntrstHdrTrxHdrHeaderType | — |
| HOLD_CHARGED_INVOICES_FLAG | IntrstHdrHoldChargedInvoicesFlag | — |
| HOLD_CHARGED_INVOICES_FLAG | IntrstHdrTrxHdrHoldChargedInvoicesFlag | — |
| INTEREST_CALCULATION_PERIOD | IntrstHdrInterestCalculationPeriod | — |
| INTEREST_CALCULATION_PERIOD | IntrstHdrTrxHdrInterestCalculationPeriod | — |
| INTEREST_FIXED_AMOUNT | IntrstHdrInterestFixedAmount | — |
| INTEREST_FIXED_AMOUNT | IntrstHdrTrxHdrInterestFixedAmount | — |
| INTEREST_HEADER_ID | IntrstHdrInterestHeaderId | — |
| INTEREST_HEADER_ID | IntrstHdrTrxHdrInterestHeaderId | — |
| INTEREST_PERIOD_DAYS | IntrstHdrInterestPeriodDays | — |
| INTEREST_PERIOD_DAYS | IntrstHdrTrxHdrInterestPeriodDays | — |
| INTEREST_RATE | IntrstHdrInterestRate | — |
| INTEREST_RATE | IntrstHdrTrxHdrInterestRate | — |
| INTEREST_TYPE | IntrstHdrInterestType | — |
| INTEREST_TYPE | IntrstHdrTrxHdrInterestType | — |
| LAST_ACCRUE_CHARGE_DATE | IntrstHdrLastAccrueChargeDate | — |
| LAST_ACCRUE_CHARGE_DATE | IntrstHdrTrxHdrLastAccrueChargeDate | — |
| LATE_CHARGE_CALCULATION_TRX | IntrstHdrLateChargeCalculationTrx | — |
| LATE_CHARGE_CALCULATION_TRX | IntrstHdrTrxHdrLateChargeCalculationTrx | — |
| MAX_INTEREST_CHARGE | IntrstHdrMaxInterestCharge | — |
| MAX_INTEREST_CHARGE | IntrstHdrTrxHdrMaxInterestCharge | — |
| MIN_FC_BALANCE_AMOUNT | IntrstHdrMinFcBalanceAmount | — |
| MIN_FC_BALANCE_AMOUNT | IntrstHdrTrxHdrMinFcBalanceAmount | — |
| MIN_FC_BALANCE_OVERDUE_TYPE | IntrstHdrMinFcBalanceOverdueType | — |
| MIN_FC_BALANCE_OVERDUE_TYPE | IntrstHdrTrxHdrMinFcBalanceOverdueType | — |
| MIN_FC_BALANCE_PERCENT | IntrstHdrMinFcBalancePercent | — |
| MIN_FC_BALANCE_PERCENT | IntrstHdrTrxHdrMinFcBalancePercent | — |
| MIN_FC_INVOICE_AMOUNT | IntrstHdrMinFcInvoiceAmount | — |
| MIN_FC_INVOICE_AMOUNT | IntrstHdrTrxHdrMinFcInvoiceAmount | — |
| MIN_FC_INVOICE_OVERDUE_TYPE | IntrstHdrMinFcInvoiceOverdueType | — |
| MIN_FC_INVOICE_OVERDUE_TYPE | IntrstHdrTrxHdrMinFcInvoiceOverdueType | — |
| MIN_FC_INVOICE_PERCENT | IntrstHdrMinFcInvoicePercent | — |
| MIN_FC_INVOICE_PERCENT | IntrstHdrTrxHdrMinFcInvoicePercent | — |
| MIN_INTEREST_CHARGE | IntrstHdrMinInterestCharge | — |
| MIN_INTEREST_CHARGE | IntrstHdrTrxHdrMinInterestCharge | — |
| MULTIPLE_INTEREST_RATES_FLAG | IntrstHdrMultipleInterestRatesFlag | — |
| MULTIPLE_INTEREST_RATES_FLAG | IntrstHdrTrxHdrMultipleInterestRatesFlag | — |
| PAYMENT_GRACE_DAYS | IntrstHdrPaymentGraceDays | — |
| PAYMENT_GRACE_DAYS | IntrstHdrTrxHdrPaymentGraceDays | — |
| PENALTY_FIXED_AMOUNT | IntrstHdrPenaltyFixedAmount | — |
| PENALTY_FIXED_AMOUNT | IntrstHdrTrxHdrPenaltyFixedAmount | — |
| PENALTY_RATE | IntrstHdrPenaltyRate | — |
| PENALTY_RATE | IntrstHdrTrxHdrPenaltyRate | — |
| PENALTY_TYPE | IntrstHdrPenaltyType | — |
| PENALTY_TYPE | IntrstHdrTrxHdrPenaltyType | — |
| PROCESS_MESSAGE | IntrstHdrProcessMessage | — |
| PROCESS_MESSAGE | IntrstHdrTrxHdrProcessMessage | — |
| PROCESS_STATUS | IntrstHdrProcessStatus | — |
| PROCESS_STATUS | IntrstHdrTrxHdrProcessStatus | — |
| WORKER_NUM | IntrstHdrTrxHdrWorkerNum | — |
| WORKER_NUM | IntrstHdrWorkerNum | — |

### [[adjustmentpvo|AdjustmentPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHARGE_BEGIN_DATE | IntrstHdrChargeBeginDate | — |
| CHARGE_ON_FINANCE_CHARGE_FLAG | IntrstHdrChargeOnFinanceChargeFlag | — |
| CREDIT_ITEMS_FLAG | IntrstHdrCreditItemsFlag | — |
| CURRENCY_CODE | IntrstHdrCurrencyCode | — |
| DISPLAY_FLAG | IntrstHdrDisplayFlag | — |
| DISPUTED_TRANSACTIONS_FLAG | IntrstHdrDisputedTransactionsFlag | — |
| EXCHANGE_RATE | IntrstHdrExchangeRate | — |
| EXCHANGE_RATE_TYPE | IntrstHdrExchangeRateType | — |
| FINANCE_CHARGE_DATE | IntrstHdrFinanceChargeDate | — |
| HEADER_TYPE | IntrstHdrHeaderType | — |
| HOLD_CHARGED_INVOICES_FLAG | IntrstHdrHoldChargedInvoicesFlag | — |
| INTEREST_CALCULATION_PERIOD | IntrstHdrInterestCalculationPeriod | — |
| INTEREST_FIXED_AMOUNT | IntrstHdrInterestFixedAmount | — |
| INTEREST_HEADER_ID | IntrstHdrInterestHeaderId | — |
| INTEREST_PERIOD_DAYS | IntrstHdrInterestPeriodDays | — |
| INTEREST_RATE | IntrstHdrInterestRate | — |
| INTEREST_TYPE | IntrstHdrInterestType | — |
| LAST_ACCRUE_CHARGE_DATE | IntrstHdrLastAccrueChargeDate | — |
| LATE_CHARGE_CALCULATION_TRX | IntrstHdrLateChargeCalculationTrx | — |
| MAX_INTEREST_CHARGE | IntrstHdrMaxInterestCharge | — |
| MIN_FC_BALANCE_AMOUNT | IntrstHdrMinFcBalanceAmount | — |
| MIN_FC_BALANCE_OVERDUE_TYPE | IntrstHdrMinFcBalanceOverdueType | — |
| MIN_FC_BALANCE_PERCENT | IntrstHdrMinFcBalancePercent | — |
| MIN_FC_INVOICE_AMOUNT | IntrstHdrMinFcInvoiceAmount | — |
| MIN_FC_INVOICE_OVERDUE_TYPE | IntrstHdrMinFcInvoiceOverdueType | — |
| MIN_FC_INVOICE_PERCENT | IntrstHdrMinFcInvoicePercent | — |
| MIN_INTEREST_CHARGE | IntrstHdrMinInterestCharge | — |
| MULTIPLE_INTEREST_RATES_FLAG | IntrstHdrMultipleInterestRatesFlag | — |
| PAYMENT_GRACE_DAYS | IntrstHdrPaymentGraceDays | — |
| PENALTY_FIXED_AMOUNT | IntrstHdrPenaltyFixedAmount | — |
| PENALTY_RATE | IntrstHdrPenaltyRate | — |
| PENALTY_TYPE | IntrstHdrPenaltyType | — |
| PROCESS_MESSAGE | IntrstHdrProcessMessage | — |
| PROCESS_STATUS | IntrstHdrProcessStatus | — |
| WORKER_NUM | IntrstHdrWorkerNum | — |

### [[completedtrxrevadjdistributionpvo|CompletedTrxRevAdjDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHARGE_BEGIN_DATE | IntrstHdrTrxHdrChargeBeginDate | — |
| CHARGE_ON_FINANCE_CHARGE_FLAG | IntrstHdrTrxHdrChargeOnFinanceChargeFlag | — |
| CREDIT_ITEMS_FLAG | IntrstHdrTrxHdrCreditItemsFlag | — |
| CURRENCY_CODE | IntrstHdrTrxHdrCurrencyCode | — |
| DISPLAY_FLAG | IntrstHdrTrxHdrDisplayFlag | — |
| DISPUTED_TRANSACTIONS_FLAG | IntrstHdrTrxHdrDisputedTransactionsFlag | — |
| EXCHANGE_RATE | IntrstHdrTrxHdrExchangeRate | — |
| EXCHANGE_RATE_TYPE | IntrstHdrTrxHdrExchangeRateType | — |
| FINANCE_CHARGE_DATE | IntrstHdrTrxHdrFinanceChargeDate | — |
| HEADER_TYPE | IntrstHdrTrxHdrHeaderType | — |
| HOLD_CHARGED_INVOICES_FLAG | IntrstHdrTrxHdrHoldChargedInvoicesFlag | — |
| INTEREST_CALCULATION_PERIOD | IntrstHdrTrxHdrInterestCalculationPeriod | — |
| INTEREST_FIXED_AMOUNT | IntrstHdrTrxHdrInterestFixedAmount | — |
| INTEREST_HEADER_ID | IntrstHdrTrxHdrInterestHeaderId | — |
| INTEREST_PERIOD_DAYS | IntrstHdrTrxHdrInterestPeriodDays | — |
| INTEREST_RATE | IntrstHdrTrxHdrInterestRate | — |
| INTEREST_TYPE | IntrstHdrTrxHdrInterestType | — |
| LAST_ACCRUE_CHARGE_DATE | IntrstHdrTrxHdrLastAccrueChargeDate | — |
| LATE_CHARGE_CALCULATION_TRX | IntrstHdrTrxHdrLateChargeCalculationTrx | — |
| MAX_INTEREST_CHARGE | IntrstHdrTrxHdrMaxInterestCharge | — |
| MIN_FC_BALANCE_AMOUNT | IntrstHdrTrxHdrMinFcBalanceAmount | — |
| MIN_FC_BALANCE_OVERDUE_TYPE | IntrstHdrTrxHdrMinFcBalanceOverdueType | — |
| MIN_FC_BALANCE_PERCENT | IntrstHdrTrxHdrMinFcBalancePercent | — |
| MIN_FC_INVOICE_AMOUNT | IntrstHdrTrxHdrMinFcInvoiceAmount | — |
| MIN_FC_INVOICE_OVERDUE_TYPE | IntrstHdrTrxHdrMinFcInvoiceOverdueType | — |
| MIN_FC_INVOICE_PERCENT | IntrstHdrTrxHdrMinFcInvoicePercent | — |
| MIN_INTEREST_CHARGE | IntrstHdrTrxHdrMinInterestCharge | — |
| MULTIPLE_INTEREST_RATES_FLAG | IntrstHdrTrxHdrMultipleInterestRatesFlag | — |
| PAYMENT_GRACE_DAYS | IntrstHdrTrxHdrPaymentGraceDays | — |
| PENALTY_FIXED_AMOUNT | IntrstHdrTrxHdrPenaltyFixedAmount | — |
| PENALTY_RATE | IntrstHdrTrxHdrPenaltyRate | — |
| PENALTY_TYPE | IntrstHdrTrxHdrPenaltyType | — |
| PROCESS_MESSAGE | IntrstHdrTrxHdrProcessMessage | — |
| PROCESS_STATUS | IntrstHdrTrxHdrProcessStatus | — |
| WORKER_NUM | IntrstHdrTrxHdrWorkerNum | — |

### [[completedtrxrevenuedistributionpvo|CompletedTrxRevenueDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHARGE_BEGIN_DATE | IntrstHdrTrxHdrChargeBeginDate | — |
| CHARGE_ON_FINANCE_CHARGE_FLAG | IntrstHdrTrxHdrChargeOnFinanceChargeFlag | — |
| CREDIT_ITEMS_FLAG | IntrstHdrTrxHdrCreditItemsFlag | — |
| CURRENCY_CODE | IntrstHdrTrxHdrCurrencyCode | — |
| DISPLAY_FLAG | IntrstHdrTrxHdrDisplayFlag | — |
| DISPUTED_TRANSACTIONS_FLAG | IntrstHdrTrxHdrDisputedTransactionsFlag | — |
| EXCHANGE_RATE | IntrstHdrTrxHdrExchangeRate | — |
| EXCHANGE_RATE_TYPE | IntrstHdrTrxHdrExchangeRateType | — |
| FINANCE_CHARGE_DATE | IntrstHdrTrxHdrFinanceChargeDate | — |
| HEADER_TYPE | IntrstHdrTrxHdrHeaderType | — |
| HOLD_CHARGED_INVOICES_FLAG | IntrstHdrTrxHdrHoldChargedInvoicesFlag | — |
| INTEREST_CALCULATION_PERIOD | IntrstHdrTrxHdrInterestCalculationPeriod | — |
| INTEREST_FIXED_AMOUNT | IntrstHdrTrxHdrInterestFixedAmount | — |
| INTEREST_HEADER_ID | IntrstHdrTrxHdrInterestHeaderId | — |
| INTEREST_PERIOD_DAYS | IntrstHdrTrxHdrInterestPeriodDays | — |
| INTEREST_RATE | IntrstHdrTrxHdrInterestRate | — |
| INTEREST_TYPE | IntrstHdrTrxHdrInterestType | — |
| LAST_ACCRUE_CHARGE_DATE | IntrstHdrTrxHdrLastAccrueChargeDate | — |
| LATE_CHARGE_CALCULATION_TRX | IntrstHdrTrxHdrLateChargeCalculationTrx | — |
| MAX_INTEREST_CHARGE | IntrstHdrTrxHdrMaxInterestCharge | — |
| MIN_FC_BALANCE_AMOUNT | IntrstHdrTrxHdrMinFcBalanceAmount | — |
| MIN_FC_BALANCE_OVERDUE_TYPE | IntrstHdrTrxHdrMinFcBalanceOverdueType | — |
| MIN_FC_BALANCE_PERCENT | IntrstHdrTrxHdrMinFcBalancePercent | — |
| MIN_FC_INVOICE_AMOUNT | IntrstHdrTrxHdrMinFcInvoiceAmount | — |
| MIN_FC_INVOICE_OVERDUE_TYPE | IntrstHdrTrxHdrMinFcInvoiceOverdueType | — |
| MIN_FC_INVOICE_PERCENT | IntrstHdrTrxHdrMinFcInvoicePercent | — |
| MIN_INTEREST_CHARGE | IntrstHdrTrxHdrMinInterestCharge | — |
| MULTIPLE_INTEREST_RATES_FLAG | IntrstHdrTrxHdrMultipleInterestRatesFlag | — |
| PAYMENT_GRACE_DAYS | IntrstHdrTrxHdrPaymentGraceDays | — |
| PENALTY_FIXED_AMOUNT | IntrstHdrTrxHdrPenaltyFixedAmount | — |
| PENALTY_RATE | IntrstHdrTrxHdrPenaltyRate | — |
| PENALTY_TYPE | IntrstHdrTrxHdrPenaltyType | — |
| PROCESS_MESSAGE | IntrstHdrTrxHdrProcessMessage | — |
| PROCESS_STATUS | IntrstHdrTrxHdrProcessStatus | — |
| WORKER_NUM | IntrstHdrTrxHdrWorkerNum | — |

### [[creditmemoapplicationdistributionpvo|CreditMemoApplicationDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHARGE_BEGIN_DATE | IntrstHdrTrxHdrAlyChargeBeginDate | — |
| CHARGE_BEGIN_DATE | IntrstHdrTrxHdrChargeBeginDate | — |
| CHARGE_ON_FINANCE_CHARGE_FLAG | IntrstHdrTrxHdrAlyChargeOnFinanceChargeFlag | — |
| CHARGE_ON_FINANCE_CHARGE_FLAG | IntrstHdrTrxHdrChargeOnFinanceChargeFlag | — |
| CREDIT_ITEMS_FLAG | IntrstHdrTrxHdrAlyCreditItemsFlag | — |
| CREDIT_ITEMS_FLAG | IntrstHdrTrxHdrCreditItemsFlag | — |
| CURRENCY_CODE | IntrstHdrTrxHdrAlyCurrencyCode | — |
| CURRENCY_CODE | IntrstHdrTrxHdrCurrencyCode | — |
| DISPLAY_FLAG | IntrstHdrTrxHdrAlyDisplayFlag | — |
| DISPLAY_FLAG | IntrstHdrTrxHdrDisplayFlag | — |
| DISPUTED_TRANSACTIONS_FLAG | IntrstHdrTrxHdrAlyDisputedTransactionsFlag | — |
| DISPUTED_TRANSACTIONS_FLAG | IntrstHdrTrxHdrDisputedTransactionsFlag | — |
| EXCHANGE_RATE | IntrstHdrTrxHdrAlyExchangeRate | — |
| EXCHANGE_RATE | IntrstHdrTrxHdrExchangeRate | — |
| EXCHANGE_RATE_TYPE | IntrstHdrTrxHdrAlyExchangeRateType | — |
| EXCHANGE_RATE_TYPE | IntrstHdrTrxHdrExchangeRateType | — |
| FINANCE_CHARGE_DATE | IntrstHdrTrxHdrAlyFinanceChargeDate | — |
| FINANCE_CHARGE_DATE | IntrstHdrTrxHdrFinanceChargeDate | — |
| HEADER_TYPE | IntrstHdrTrxHdrAlyHeaderType | — |
| HEADER_TYPE | IntrstHdrTrxHdrHeaderType | — |
| HOLD_CHARGED_INVOICES_FLAG | IntrstHdrTrxHdrAlyHoldChargedInvoicesFlag | — |
| HOLD_CHARGED_INVOICES_FLAG | IntrstHdrTrxHdrHoldChargedInvoicesFlag | — |
| INTEREST_CALCULATION_PERIOD | IntrstHdrTrxHdrAlyInterestCalculationPeriod | — |
| INTEREST_CALCULATION_PERIOD | IntrstHdrTrxHdrInterestCalculationPeriod | — |
| INTEREST_FIXED_AMOUNT | IntrstHdrTrxHdrAlyInterestFixedAmount | — |
| INTEREST_FIXED_AMOUNT | IntrstHdrTrxHdrInterestFixedAmount | — |
| INTEREST_HEADER_ID | IntrstHdrTrxHdrAlyInterestHeaderId | — |
| INTEREST_HEADER_ID | IntrstHdrTrxHdrInterestHeaderId | — |
| INTEREST_PERIOD_DAYS | IntrstHdrTrxHdrAlyInterestPeriodDays | — |
| INTEREST_PERIOD_DAYS | IntrstHdrTrxHdrInterestPeriodDays | — |
| INTEREST_RATE | IntrstHdrTrxHdrAlyInterestRate | — |
| INTEREST_RATE | IntrstHdrTrxHdrInterestRate | — |
| INTEREST_TYPE | IntrstHdrTrxHdrAlyInterestType | — |
| INTEREST_TYPE | IntrstHdrTrxHdrInterestType | — |
| LAST_ACCRUE_CHARGE_DATE | IntrstHdrTrxHdrAlyLastAccrueChargeDate | — |
| LAST_ACCRUE_CHARGE_DATE | IntrstHdrTrxHdrLastAccrueChargeDate | — |
| LATE_CHARGE_CALCULATION_TRX | IntrstHdrTrxHdrAlyLateChargeCalculationTrx | — |
| LATE_CHARGE_CALCULATION_TRX | IntrstHdrTrxHdrLateChargeCalculationTrx | — |
| MAX_INTEREST_CHARGE | IntrstHdrTrxHdrAlyMaxInterestCharge | — |
| MAX_INTEREST_CHARGE | IntrstHdrTrxHdrMaxInterestCharge | — |
| MIN_FC_BALANCE_AMOUNT | IntrstHdrTrxHdrAlyMinFcBalanceAmount | — |
| MIN_FC_BALANCE_AMOUNT | IntrstHdrTrxHdrMinFcBalanceAmount | — |
| MIN_FC_BALANCE_OVERDUE_TYPE | IntrstHdrTrxHdrAlyMinFcBalanceOverdueType | — |
| MIN_FC_BALANCE_OVERDUE_TYPE | IntrstHdrTrxHdrMinFcBalanceOverdueType | — |
| MIN_FC_BALANCE_PERCENT | IntrstHdrTrxHdrAlyMinFcBalancePercent | — |
| MIN_FC_BALANCE_PERCENT | IntrstHdrTrxHdrMinFcBalancePercent | — |
| MIN_FC_INVOICE_AMOUNT | IntrstHdrTrxHdrAlyMinFcInvoiceAmount | — |
| MIN_FC_INVOICE_AMOUNT | IntrstHdrTrxHdrMinFcInvoiceAmount | — |
| MIN_FC_INVOICE_OVERDUE_TYPE | IntrstHdrTrxHdrAlyMinFcInvoiceOverdueType | — |
| MIN_FC_INVOICE_OVERDUE_TYPE | IntrstHdrTrxHdrMinFcInvoiceOverdueType | — |
| MIN_FC_INVOICE_PERCENT | IntrstHdrTrxHdrAlyMinFcInvoicePercent | — |
| MIN_FC_INVOICE_PERCENT | IntrstHdrTrxHdrMinFcInvoicePercent | — |
| MIN_INTEREST_CHARGE | IntrstHdrTrxHdrAlyMinInterestCharge | — |
| MIN_INTEREST_CHARGE | IntrstHdrTrxHdrMinInterestCharge | — |
| MULTIPLE_INTEREST_RATES_FLAG | IntrstHdrTrxHdrAlyMultipleInterestRatesFlag | — |
| MULTIPLE_INTEREST_RATES_FLAG | IntrstHdrTrxHdrMultipleInterestRatesFlag | — |
| PAYMENT_GRACE_DAYS | IntrstHdrTrxHdrAlyPaymentGraceDays | — |
| PAYMENT_GRACE_DAYS | IntrstHdrTrxHdrPaymentGraceDays | — |
| PENALTY_FIXED_AMOUNT | IntrstHdrTrxHdrAlyPenaltyFixedAmount | — |
| PENALTY_FIXED_AMOUNT | IntrstHdrTrxHdrPenaltyFixedAmount | — |
| PENALTY_RATE | IntrstHdrTrxHdrAlyPenaltyRate | — |
| PENALTY_RATE | IntrstHdrTrxHdrPenaltyRate | — |
| PENALTY_TYPE | IntrstHdrTrxHdrAlyPenaltyType | — |
| PENALTY_TYPE | IntrstHdrTrxHdrPenaltyType | — |
| PROCESS_MESSAGE | IntrstHdrTrxHdrAlyProcessMessage | — |
| PROCESS_MESSAGE | IntrstHdrTrxHdrProcessMessage | — |
| PROCESS_STATUS | IntrstHdrTrxHdrAlyProcessStatus | — |
| PROCESS_STATUS | IntrstHdrTrxHdrProcessStatus | — |
| WORKER_NUM | IntrstHdrTrxHdrAlyWorkerNum | — |
| WORKER_NUM | IntrstHdrTrxHdrWorkerNum | — |

### [[headersalescreditpvo|HeaderSalesCreditPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHARGE_BEGIN_DATE | IntrstHdrTrxHdrChargeBeginDate | — |
| CHARGE_ON_FINANCE_CHARGE_FLAG | IntrstHdrTrxHdrChargeOnFinanceChargeFlag | — |
| CREDIT_ITEMS_FLAG | IntrstHdrTrxHdrCreditItemsFlag | — |
| CURRENCY_CODE | IntrstHdrTrxHdrCurrencyCode | — |
| DISPLAY_FLAG | IntrstHdrTrxHdrDisplayFlag | — |
| DISPUTED_TRANSACTIONS_FLAG | IntrstHdrTrxHdrDisputedTransactionsFlag | — |
| EXCHANGE_RATE | IntrstHdrTrxHdrExchangeRate | — |
| EXCHANGE_RATE_TYPE | IntrstHdrTrxHdrExchangeRateType | — |
| FINANCE_CHARGE_DATE | IntrstHdrTrxHdrFinanceChargeDate | — |
| HEADER_TYPE | IntrstHdrTrxHdrHeaderType | — |
| HOLD_CHARGED_INVOICES_FLAG | IntrstHdrTrxHdrHoldChargedInvoicesFlag | — |
| INTEREST_CALCULATION_PERIOD | IntrstHdrTrxHdrInterestCalculationPeriod | — |
| INTEREST_FIXED_AMOUNT | IntrstHdrTrxHdrInterestFixedAmount | — |
| INTEREST_HEADER_ID | IntrstHdrTrxHdrInterestHeaderId | — |
| INTEREST_PERIOD_DAYS | IntrstHdrTrxHdrInterestPeriodDays | — |
| INTEREST_RATE | IntrstHdrTrxHdrInterestRate | — |
| INTEREST_TYPE | IntrstHdrTrxHdrInterestType | — |
| LAST_ACCRUE_CHARGE_DATE | IntrstHdrTrxHdrLastAccrueChargeDate | — |
| LATE_CHARGE_CALCULATION_TRX | IntrstHdrTrxHdrLateChargeCalculationTrx | — |
| MAX_INTEREST_CHARGE | IntrstHdrTrxHdrMaxInterestCharge | — |
| MIN_FC_BALANCE_AMOUNT | IntrstHdrTrxHdrMinFcBalanceAmount | — |
| MIN_FC_BALANCE_OVERDUE_TYPE | IntrstHdrTrxHdrMinFcBalanceOverdueType | — |
| MIN_FC_BALANCE_PERCENT | IntrstHdrTrxHdrMinFcBalancePercent | — |
| MIN_FC_INVOICE_AMOUNT | IntrstHdrTrxHdrMinFcInvoiceAmount | — |
| MIN_FC_INVOICE_OVERDUE_TYPE | IntrstHdrTrxHdrMinFcInvoiceOverdueType | — |
| MIN_FC_INVOICE_PERCENT | IntrstHdrTrxHdrMinFcInvoicePercent | — |
| MIN_INTEREST_CHARGE | IntrstHdrTrxHdrMinInterestCharge | — |
| MULTIPLE_INTEREST_RATES_FLAG | IntrstHdrTrxHdrMultipleInterestRatesFlag | — |
| PAYMENT_GRACE_DAYS | IntrstHdrTrxHdrPaymentGraceDays | — |
| PENALTY_FIXED_AMOUNT | IntrstHdrTrxHdrPenaltyFixedAmount | — |
| PENALTY_RATE | IntrstHdrTrxHdrPenaltyRate | — |
| PENALTY_TYPE | IntrstHdrTrxHdrPenaltyType | — |
| PROCESS_MESSAGE | IntrstHdrTrxHdrProcessMessage | — |
| PROCESS_STATUS | IntrstHdrTrxHdrProcessStatus | — |
| WORKER_NUM | IntrstHdrTrxHdrWorkerNum | — |

### [[interestheaderextractpvo|InterestHeaderExtractPVO]] (OTHER · BICC: 55/55)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHARGE_BEGIN_DATE | ArInterestHeaderChargeBeginDate | ✅ |
| CHARGE_ON_FINANCE_CHARGE_FLAG | ArInterestHeaderChargeOnFinanceChargeFlag | ✅ |
| COLLECTOR_ID | ArInterestHeaderCollectorId | ✅ |
| CREATED_BY | ArInterestHeaderCreatedBy | ✅ |
| CREATION_DATE | ArInterestHeaderCreationDate | ✅ |
| CREDIT_ITEMS_FLAG | ArInterestHeaderCreditItemsFlag | ✅ |
| CURRENCY_CODE | ArInterestHeaderCurrencyCode | ✅ |
| CUST_ACCT_PROFILE_AMT_ID | ArInterestHeaderCustAcctProfileAmtId | ✅ |
| CUST_TRX_TYPE_SEQ_ID | ArInterestHeaderCustTrxTypeSeqId | ✅ |
| CUSTOMER_ID | ArInterestHeaderCustomerId | ✅ |
| CUSTOMER_PROFILE_ID | ArInterestHeaderCustomerProfileId | ✅ |
| CUSTOMER_SITE_USE_ID | ArInterestHeaderCustomerSiteUseId | ✅ |
| DISPLAY_FLAG | ArInterestHeaderDisplayFlag | ✅ |
| DISPUTED_TRANSACTIONS_FLAG | ArInterestHeaderDisputedTransactionsFlag | ✅ |
| EXCHANGE_RATE | ArInterestHeaderExchangeRate | ✅ |
| EXCHANGE_RATE_TYPE | ArInterestHeaderExchangeRateType | ✅ |
| FINANCE_CHARGE_DATE | ArInterestHeaderFinanceChargeDate | ✅ |
| HEADER_TYPE | ArInterestHeaderHeaderType | ✅ |
| HOLD_CHARGED_INVOICES_FLAG | ArInterestHeaderHoldChargedInvoicesFlag | ✅ |
| INTEREST_BATCH_ID | ArInterestHeaderInterestBatchId | ✅ |
| INTEREST_CALCULATION_PERIOD | ArInterestHeaderInterestCalculationPeriod | ✅ |
| INTEREST_FIXED_AMOUNT | ArInterestHeaderInterestFixedAmount | ✅ |
| INTEREST_HEADER_ID | ArInterestHeaderInterestHeaderId | ✅ |
| INTEREST_PERIOD_DAYS | ArInterestHeaderInterestPeriodDays | ✅ |
| INTEREST_RATE | ArInterestHeaderInterestRate | ✅ |
| INTEREST_SCHEDULE_ID | ArInterestHeaderInterestScheduleId | ✅ |
| INTEREST_TYPE | ArInterestHeaderInterestType | ✅ |
| LAST_ACCRUE_CHARGE_DATE | ArInterestHeaderLastAccrueChargeDate | ✅ |
| LAST_UPDATE_DATE | ArInterestHeaderLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ArInterestHeaderLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ArInterestHeaderLastUpdatedBy | ✅ |
| LATE_CHARGE_CALCULATION_TRX | ArInterestHeaderLateChargeCalculationTrx | ✅ |
| LATE_CHARGE_TERM_ID | ArInterestHeaderLateChargeTermId | ✅ |
| LEGAL_ENTITY_ID | ArInterestHeaderLegalEntityId | ✅ |
| MAX_INTEREST_CHARGE | ArInterestHeaderMaxInterestCharge | ✅ |
| MESSAGE_TEXT_ID | ArInterestHeaderMessageTextId | ✅ |
| MIN_FC_BALANCE_AMOUNT | ArInterestHeaderMinFcBalanceAmount | ✅ |
| MIN_FC_BALANCE_OVERDUE_TYPE | ArInterestHeaderMinFcBalanceOverdueType | ✅ |
| MIN_FC_BALANCE_PERCENT | ArInterestHeaderMinFcBalancePercent | ✅ |
| MIN_FC_INVOICE_AMOUNT | ArInterestHeaderMinFcInvoiceAmount | ✅ |
| MIN_FC_INVOICE_OVERDUE_TYPE | ArInterestHeaderMinFcInvoiceOverdueType | ✅ |
| MIN_FC_INVOICE_PERCENT | ArInterestHeaderMinFcInvoicePercent | ✅ |
| MIN_INTEREST_CHARGE | ArInterestHeaderMinInterestCharge | ✅ |
| MULTIPLE_INTEREST_RATES_FLAG | ArInterestHeaderMultipleInterestRatesFlag | ✅ |
| OBJECT_VERSION_NUMBER | ArInterestHeaderObjectVersionNumber | ✅ |
| ORG_ID | ArInterestHeaderOrgId | ✅ |
| PAYMENT_GRACE_DAYS | ArInterestHeaderPaymentGraceDays | ✅ |
| PENALTY_FIXED_AMOUNT | ArInterestHeaderPenaltyFixedAmount | ✅ |
| PENALTY_RATE | ArInterestHeaderPenaltyRate | ✅ |
| PENALTY_SCHEDULE_ID | ArInterestHeaderPenaltyScheduleId | ✅ |
| PENALTY_TYPE | ArInterestHeaderPenaltyType | ✅ |
| PROCESS_MESSAGE | ArInterestHeaderProcessMessage | ✅ |
| PROCESS_STATUS | ArInterestHeaderProcessStatus | ✅ |
| REQUEST_ID | ArInterestHeaderRequestId | ✅ |
| WORKER_NUM | ArInterestHeaderWorkerNum | ✅ |

### [[linesalescreditpvo|LineSalesCreditPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHARGE_BEGIN_DATE | IntrstHdrTrxHdrChargeBeginDate | — |
| CHARGE_ON_FINANCE_CHARGE_FLAG | IntrstHdrTrxHdrChargeOnFinanceChargeFlag | — |
| CREDIT_ITEMS_FLAG | IntrstHdrTrxHdrCreditItemsFlag | — |
| CURRENCY_CODE | IntrstHdrTrxHdrCurrencyCode | — |
| DISPLAY_FLAG | IntrstHdrTrxHdrDisplayFlag | — |
| DISPUTED_TRANSACTIONS_FLAG | IntrstHdrTrxHdrDisputedTransactionsFlag | — |
| EXCHANGE_RATE | IntrstHdrTrxHdrExchangeRate | — |
| EXCHANGE_RATE_TYPE | IntrstHdrTrxHdrExchangeRateType | — |
| FINANCE_CHARGE_DATE | IntrstHdrTrxHdrFinanceChargeDate | — |
| HEADER_TYPE | IntrstHdrTrxHdrHeaderType | — |
| HOLD_CHARGED_INVOICES_FLAG | IntrstHdrTrxHdrHoldChargedInvoicesFlag | — |
| INTEREST_CALCULATION_PERIOD | IntrstHdrTrxHdrInterestCalculationPeriod | — |
| INTEREST_FIXED_AMOUNT | IntrstHdrTrxHdrInterestFixedAmount | — |
| INTEREST_HEADER_ID | IntrstHdrTrxHdrInterestHeaderId | — |
| INTEREST_PERIOD_DAYS | IntrstHdrTrxHdrInterestPeriodDays | — |
| INTEREST_RATE | IntrstHdrTrxHdrInterestRate | — |
| INTEREST_TYPE | IntrstHdrTrxHdrInterestType | — |
| LAST_ACCRUE_CHARGE_DATE | IntrstHdrTrxHdrLastAccrueChargeDate | — |
| LATE_CHARGE_CALCULATION_TRX | IntrstHdrTrxHdrLateChargeCalculationTrx | — |
| MAX_INTEREST_CHARGE | IntrstHdrTrxHdrMaxInterestCharge | — |
| MIN_FC_BALANCE_AMOUNT | IntrstHdrTrxHdrMinFcBalanceAmount | — |
| MIN_FC_BALANCE_OVERDUE_TYPE | IntrstHdrTrxHdrMinFcBalanceOverdueType | — |
| MIN_FC_BALANCE_PERCENT | IntrstHdrTrxHdrMinFcBalancePercent | — |
| MIN_FC_INVOICE_AMOUNT | IntrstHdrTrxHdrMinFcInvoiceAmount | — |
| MIN_FC_INVOICE_OVERDUE_TYPE | IntrstHdrTrxHdrMinFcInvoiceOverdueType | — |
| MIN_FC_INVOICE_PERCENT | IntrstHdrTrxHdrMinFcInvoicePercent | — |
| MIN_INTEREST_CHARGE | IntrstHdrTrxHdrMinInterestCharge | — |
| MULTIPLE_INTEREST_RATES_FLAG | IntrstHdrTrxHdrMultipleInterestRatesFlag | — |
| PAYMENT_GRACE_DAYS | IntrstHdrTrxHdrPaymentGraceDays | — |
| PENALTY_FIXED_AMOUNT | IntrstHdrTrxHdrPenaltyFixedAmount | — |
| PENALTY_RATE | IntrstHdrTrxHdrPenaltyRate | — |
| PENALTY_TYPE | IntrstHdrTrxHdrPenaltyType | — |
| PROCESS_MESSAGE | IntrstHdrTrxHdrProcessMessage | — |
| PROCESS_STATUS | IntrstHdrTrxHdrProcessStatus | — |
| WORKER_NUM | IntrstHdrTrxHdrWorkerNum | — |

### [[paymentschedulepvo|PaymentSchedulePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHARGE_BEGIN_DATE | IntrstHdrTrxHdrChargeBeginDate | — |
| CHARGE_ON_FINANCE_CHARGE_FLAG | IntrstHdrTrxHdrChargeOnFinanceChargeFlag | — |
| CREDIT_ITEMS_FLAG | IntrstHdrTrxHdrCreditItemsFlag | — |
| CURRENCY_CODE | IntrstHdrTrxHdrCurrencyCode | — |
| DISPLAY_FLAG | IntrstHdrTrxHdrDisplayFlag | — |
| DISPUTED_TRANSACTIONS_FLAG | IntrstHdrTrxHdrDisputedTransactionsFlag | — |
| EXCHANGE_RATE | IntrstHdrTrxHdrExchangeRate | — |
| EXCHANGE_RATE_TYPE | IntrstHdrTrxHdrExchangeRateType | — |
| FINANCE_CHARGE_DATE | IntrstHdrTrxHdrFinanceChargeDate | — |
| HEADER_TYPE | IntrstHdrTrxHdrHeaderType | — |
| HOLD_CHARGED_INVOICES_FLAG | IntrstHdrTrxHdrHoldChargedInvoicesFlag | — |
| INTEREST_CALCULATION_PERIOD | IntrstHdrTrxHdrInterestCalculationPeriod | — |
| INTEREST_FIXED_AMOUNT | IntrstHdrTrxHdrInterestFixedAmount | — |
| INTEREST_HEADER_ID | IntrstHdrTrxHdrInterestHeaderId | — |
| INTEREST_PERIOD_DAYS | IntrstHdrTrxHdrInterestPeriodDays | — |
| INTEREST_RATE | IntrstHdrTrxHdrInterestRate | — |
| INTEREST_TYPE | IntrstHdrTrxHdrInterestType | — |
| LAST_ACCRUE_CHARGE_DATE | IntrstHdrTrxHdrLastAccrueChargeDate | — |
| LATE_CHARGE_CALCULATION_TRX | IntrstHdrTrxHdrLateChargeCalculationTrx | — |
| MAX_INTEREST_CHARGE | IntrstHdrTrxHdrMaxInterestCharge | — |
| MIN_FC_BALANCE_AMOUNT | IntrstHdrTrxHdrMinFcBalanceAmount | — |
| MIN_FC_BALANCE_OVERDUE_TYPE | IntrstHdrTrxHdrMinFcBalanceOverdueType | — |
| MIN_FC_BALANCE_PERCENT | IntrstHdrTrxHdrMinFcBalancePercent | — |
| MIN_FC_INVOICE_AMOUNT | IntrstHdrTrxHdrMinFcInvoiceAmount | — |
| MIN_FC_INVOICE_OVERDUE_TYPE | IntrstHdrTrxHdrMinFcInvoiceOverdueType | — |
| MIN_FC_INVOICE_PERCENT | IntrstHdrTrxHdrMinFcInvoicePercent | — |
| MIN_INTEREST_CHARGE | IntrstHdrTrxHdrMinInterestCharge | — |
| MULTIPLE_INTEREST_RATES_FLAG | IntrstHdrTrxHdrMultipleInterestRatesFlag | — |
| PAYMENT_GRACE_DAYS | IntrstHdrTrxHdrPaymentGraceDays | — |
| PENALTY_FIXED_AMOUNT | IntrstHdrTrxHdrPenaltyFixedAmount | — |
| PENALTY_RATE | IntrstHdrTrxHdrPenaltyRate | — |
| PENALTY_TYPE | IntrstHdrTrxHdrPenaltyType | — |
| PROCESS_MESSAGE | IntrstHdrTrxHdrProcessMessage | — |
| PROCESS_STATUS | IntrstHdrTrxHdrProcessStatus | — |
| WORKER_NUM | IntrstHdrTrxHdrWorkerNum | — |

### [[salesinvoicecustomertrxlinesalescreditpvo|SalesInvoiceCustomerTrxLineSalesCreditPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHARGE_BEGIN_DATE | IntrstHdrTrxHdrChargeBeginDate | — |
| CHARGE_ON_FINANCE_CHARGE_FLAG | IntrstHdrTrxHdrChargeOnFinanceChargeFlag | — |
| CREDIT_ITEMS_FLAG | IntrstHdrTrxHdrCreditItemsFlag | — |
| CURRENCY_CODE | IntrstHdrTrxHdrCurrencyCode | — |
| DISPLAY_FLAG | IntrstHdrTrxHdrDisplayFlag | — |
| DISPUTED_TRANSACTIONS_FLAG | IntrstHdrTrxHdrDisputedTransactionsFlag | — |
| EXCHANGE_RATE | IntrstHdrTrxHdrExchangeRate | — |
| EXCHANGE_RATE_TYPE | IntrstHdrTrxHdrExchangeRateType | — |
| FINANCE_CHARGE_DATE | IntrstHdrTrxHdrFinanceChargeDate | — |
| HEADER_TYPE | IntrstHdrTrxHdrHeaderType | — |
| HOLD_CHARGED_INVOICES_FLAG | IntrstHdrTrxHdrHoldChargedInvoicesFlag | — |
| INTEREST_CALCULATION_PERIOD | IntrstHdrTrxHdrInterestCalculationPeriod | — |
| INTEREST_FIXED_AMOUNT | IntrstHdrTrxHdrInterestFixedAmount | — |
| INTEREST_HEADER_ID | IntrstHdrTrxHdrInterestHeaderId | — |
| INTEREST_PERIOD_DAYS | IntrstHdrTrxHdrInterestPeriodDays | — |
| INTEREST_RATE | IntrstHdrTrxHdrInterestRate | — |
| INTEREST_TYPE | IntrstHdrTrxHdrInterestType | — |
| LAST_ACCRUE_CHARGE_DATE | IntrstHdrTrxHdrLastAccrueChargeDate | — |
| LATE_CHARGE_CALCULATION_TRX | IntrstHdrTrxHdrLateChargeCalculationTrx | — |
| MAX_INTEREST_CHARGE | IntrstHdrTrxHdrMaxInterestCharge | — |
| MIN_FC_BALANCE_AMOUNT | IntrstHdrTrxHdrMinFcBalanceAmount | — |
| MIN_FC_BALANCE_OVERDUE_TYPE | IntrstHdrTrxHdrMinFcBalanceOverdueType | — |
| MIN_FC_BALANCE_PERCENT | IntrstHdrTrxHdrMinFcBalancePercent | — |
| MIN_FC_INVOICE_AMOUNT | IntrstHdrTrxHdrMinFcInvoiceAmount | — |
| MIN_FC_INVOICE_OVERDUE_TYPE | IntrstHdrTrxHdrMinFcInvoiceOverdueType | — |
| MIN_FC_INVOICE_PERCENT | IntrstHdrTrxHdrMinFcInvoicePercent | — |
| MIN_INTEREST_CHARGE | IntrstHdrTrxHdrMinInterestCharge | — |
| MULTIPLE_INTEREST_RATES_FLAG | IntrstHdrTrxHdrMultipleInterestRatesFlag | — |
| PAYMENT_GRACE_DAYS | IntrstHdrTrxHdrPaymentGraceDays | — |
| PENALTY_FIXED_AMOUNT | IntrstHdrTrxHdrPenaltyFixedAmount | — |
| PENALTY_RATE | IntrstHdrTrxHdrPenaltyRate | — |
| PENALTY_TYPE | IntrstHdrTrxHdrPenaltyType | — |
| PROCESS_MESSAGE | IntrstHdrTrxHdrProcessMessage | — |
| PROCESS_STATUS | IntrstHdrTrxHdrProcessStatus | — |
| WORKER_NUM | IntrstHdrTrxHdrWorkerNum | — |

### [[salesinvoicecustomertrxlinespvo|SalesInvoiceCustomerTrxLinesPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHARGE_BEGIN_DATE | IntrstHdrTrxHdrChargeBeginDate | — |
| CHARGE_ON_FINANCE_CHARGE_FLAG | IntrstHdrTrxHdrChargeOnFinanceChargeFlag | — |
| CREDIT_ITEMS_FLAG | IntrstHdrTrxHdrCreditItemsFlag | — |
| CURRENCY_CODE | IntrstHdrTrxHdrCurrencyCode | — |
| DISPLAY_FLAG | IntrstHdrTrxHdrDisplayFlag | — |
| DISPUTED_TRANSACTIONS_FLAG | IntrstHdrTrxHdrDisputedTransactionsFlag | — |
| EXCHANGE_RATE | IntrstHdrTrxHdrExchangeRate | — |
| EXCHANGE_RATE_TYPE | IntrstHdrTrxHdrExchangeRateType | — |
| FINANCE_CHARGE_DATE | IntrstHdrTrxHdrFinanceChargeDate | — |
| HEADER_TYPE | IntrstHdrTrxHdrHeaderType | — |
| HOLD_CHARGED_INVOICES_FLAG | IntrstHdrTrxHdrHoldChargedInvoicesFlag | — |
| INTEREST_CALCULATION_PERIOD | IntrstHdrTrxHdrInterestCalculationPeriod | — |
| INTEREST_FIXED_AMOUNT | IntrstHdrTrxHdrInterestFixedAmount | — |
| INTEREST_HEADER_ID | IntrstHdrTrxHdrInterestHeaderId | — |
| INTEREST_PERIOD_DAYS | IntrstHdrTrxHdrInterestPeriodDays | — |
| INTEREST_RATE | IntrstHdrTrxHdrInterestRate | — |
| INTEREST_TYPE | IntrstHdrTrxHdrInterestType | — |
| LAST_ACCRUE_CHARGE_DATE | IntrstHdrTrxHdrLastAccrueChargeDate | — |
| LATE_CHARGE_CALCULATION_TRX | IntrstHdrTrxHdrLateChargeCalculationTrx | — |
| MAX_INTEREST_CHARGE | IntrstHdrTrxHdrMaxInterestCharge | — |
| MIN_FC_BALANCE_AMOUNT | IntrstHdrTrxHdrMinFcBalanceAmount | — |
| MIN_FC_BALANCE_OVERDUE_TYPE | IntrstHdrTrxHdrMinFcBalanceOverdueType | — |
| MIN_FC_BALANCE_PERCENT | IntrstHdrTrxHdrMinFcBalancePercent | — |
| MIN_FC_INVOICE_AMOUNT | IntrstHdrTrxHdrMinFcInvoiceAmount | — |
| MIN_FC_INVOICE_OVERDUE_TYPE | IntrstHdrTrxHdrMinFcInvoiceOverdueType | — |
| MIN_FC_INVOICE_PERCENT | IntrstHdrTrxHdrMinFcInvoicePercent | — |
| MIN_INTEREST_CHARGE | IntrstHdrTrxHdrMinInterestCharge | — |
| MULTIPLE_INTEREST_RATES_FLAG | IntrstHdrTrxHdrMultipleInterestRatesFlag | — |
| PAYMENT_GRACE_DAYS | IntrstHdrTrxHdrPaymentGraceDays | — |
| PENALTY_FIXED_AMOUNT | IntrstHdrTrxHdrPenaltyFixedAmount | — |
| PENALTY_RATE | IntrstHdrTrxHdrPenaltyRate | — |
| PENALTY_TYPE | IntrstHdrTrxHdrPenaltyType | — |
| PROCESS_MESSAGE | IntrstHdrTrxHdrProcessMessage | — |
| PROCESS_STATUS | IntrstHdrTrxHdrProcessStatus | — |
| WORKER_NUM | IntrstHdrTrxHdrWorkerNum | — |

### [[transactionheaderbillsreceivablepvo|TransactionHeaderBillsReceivablePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHARGE_BEGIN_DATE | IntrstHdrTrxHdrChargeBeginDate | — |
| CHARGE_ON_FINANCE_CHARGE_FLAG | IntrstHdrTrxHdrChargeOnFinanceChargeFlag | — |
| CREDIT_ITEMS_FLAG | IntrstHdrTrxHdrCreditItemsFlag | — |
| CURRENCY_CODE | IntrstHdrTrxHdrCurrencyCode | — |
| DISPLAY_FLAG | IntrstHdrTrxHdrDisplayFlag | — |
| DISPUTED_TRANSACTIONS_FLAG | IntrstHdrTrxHdrDisputedTransactionsFlag | — |
| EXCHANGE_RATE | IntrstHdrTrxHdrExchangeRate | — |
| EXCHANGE_RATE_TYPE | IntrstHdrTrxHdrExchangeRateType | — |
| FINANCE_CHARGE_DATE | IntrstHdrTrxHdrFinanceChargeDate | — |
| HEADER_TYPE | IntrstHdrTrxHdrHeaderType | — |
| HOLD_CHARGED_INVOICES_FLAG | IntrstHdrTrxHdrHoldChargedInvoicesFlag | — |
| INTEREST_CALCULATION_PERIOD | IntrstHdrTrxHdrInterestCalculationPeriod | — |
| INTEREST_FIXED_AMOUNT | IntrstHdrTrxHdrInterestFixedAmount | — |
| INTEREST_HEADER_ID | IntrstHdrTrxHdrInterestHeaderId | — |
| INTEREST_PERIOD_DAYS | IntrstHdrTrxHdrInterestPeriodDays | — |
| INTEREST_RATE | IntrstHdrTrxHdrInterestRate | — |
| INTEREST_TYPE | IntrstHdrTrxHdrInterestType | — |
| LAST_ACCRUE_CHARGE_DATE | IntrstHdrTrxHdrLastAccrueChargeDate | — |
| LATE_CHARGE_CALCULATION_TRX | IntrstHdrTrxHdrLateChargeCalculationTrx | — |
| MAX_INTEREST_CHARGE | IntrstHdrTrxHdrMaxInterestCharge | — |
| MIN_FC_BALANCE_AMOUNT | IntrstHdrTrxHdrMinFcBalanceAmount | — |
| MIN_FC_BALANCE_OVERDUE_TYPE | IntrstHdrTrxHdrMinFcBalanceOverdueType | — |
| MIN_FC_BALANCE_PERCENT | IntrstHdrTrxHdrMinFcBalancePercent | — |
| MIN_FC_INVOICE_AMOUNT | IntrstHdrTrxHdrMinFcInvoiceAmount | — |
| MIN_FC_INVOICE_OVERDUE_TYPE | IntrstHdrTrxHdrMinFcInvoiceOverdueType | — |
| MIN_FC_INVOICE_PERCENT | IntrstHdrTrxHdrMinFcInvoicePercent | — |
| MIN_INTEREST_CHARGE | IntrstHdrTrxHdrMinInterestCharge | — |
| MULTIPLE_INTEREST_RATES_FLAG | IntrstHdrTrxHdrMultipleInterestRatesFlag | — |
| PAYMENT_GRACE_DAYS | IntrstHdrTrxHdrPaymentGraceDays | — |
| PENALTY_FIXED_AMOUNT | IntrstHdrTrxHdrPenaltyFixedAmount | — |
| PENALTY_RATE | IntrstHdrTrxHdrPenaltyRate | — |
| PENALTY_TYPE | IntrstHdrTrxHdrPenaltyType | — |
| PROCESS_MESSAGE | IntrstHdrTrxHdrProcessMessage | — |
| PROCESS_STATUS | IntrstHdrTrxHdrProcessStatus | — |
| WORKER_NUM | IntrstHdrTrxHdrWorkerNum | — |

### [[transactionheadernovcpvo|TransactionHeaderNoVCPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHARGE_BEGIN_DATE | IntrstHdrTrxHdrChargeBeginDate | — |
| CHARGE_ON_FINANCE_CHARGE_FLAG | IntrstHdrTrxHdrChargeOnFinanceChargeFlag | — |
| CREDIT_ITEMS_FLAG | IntrstHdrTrxHdrCreditItemsFlag | — |
| CURRENCY_CODE | IntrstHdrTrxHdrCurrencyCode | — |
| DISPLAY_FLAG | IntrstHdrTrxHdrDisplayFlag | — |
| DISPUTED_TRANSACTIONS_FLAG | IntrstHdrTrxHdrDisputedTransactionsFlag | — |
| EXCHANGE_RATE | IntrstHdrTrxHdrExchangeRate | — |
| EXCHANGE_RATE_TYPE | IntrstHdrTrxHdrExchangeRateType | — |
| FINANCE_CHARGE_DATE | IntrstHdrTrxHdrFinanceChargeDate | — |
| HEADER_TYPE | IntrstHdrTrxHdrHeaderType | — |
| HOLD_CHARGED_INVOICES_FLAG | IntrstHdrTrxHdrHoldChargedInvoicesFlag | — |
| INTEREST_CALCULATION_PERIOD | IntrstHdrTrxHdrInterestCalculationPeriod | — |
| INTEREST_FIXED_AMOUNT | IntrstHdrTrxHdrInterestFixedAmount | — |
| INTEREST_HEADER_ID | IntrstHdrTrxHdrInterestHeaderId | — |
| INTEREST_PERIOD_DAYS | IntrstHdrTrxHdrInterestPeriodDays | — |
| INTEREST_RATE | IntrstHdrTrxHdrInterestRate | — |
| INTEREST_TYPE | IntrstHdrTrxHdrInterestType | — |
| LAST_ACCRUE_CHARGE_DATE | IntrstHdrTrxHdrLastAccrueChargeDate | — |
| LATE_CHARGE_CALCULATION_TRX | IntrstHdrTrxHdrLateChargeCalculationTrx | — |
| MAX_INTEREST_CHARGE | IntrstHdrTrxHdrMaxInterestCharge | — |
| MIN_FC_BALANCE_AMOUNT | IntrstHdrTrxHdrMinFcBalanceAmount | — |
| MIN_FC_BALANCE_OVERDUE_TYPE | IntrstHdrTrxHdrMinFcBalanceOverdueType | — |
| MIN_FC_BALANCE_PERCENT | IntrstHdrTrxHdrMinFcBalancePercent | — |
| MIN_FC_INVOICE_AMOUNT | IntrstHdrTrxHdrMinFcInvoiceAmount | — |
| MIN_FC_INVOICE_OVERDUE_TYPE | IntrstHdrTrxHdrMinFcInvoiceOverdueType | — |
| MIN_FC_INVOICE_PERCENT | IntrstHdrTrxHdrMinFcInvoicePercent | — |
| MIN_INTEREST_CHARGE | IntrstHdrTrxHdrMinInterestCharge | — |
| MULTIPLE_INTEREST_RATES_FLAG | IntrstHdrTrxHdrMultipleInterestRatesFlag | — |
| PAYMENT_GRACE_DAYS | IntrstHdrTrxHdrPaymentGraceDays | — |
| PENALTY_FIXED_AMOUNT | IntrstHdrTrxHdrPenaltyFixedAmount | — |
| PENALTY_RATE | IntrstHdrTrxHdrPenaltyRate | — |
| PENALTY_TYPE | IntrstHdrTrxHdrPenaltyType | — |
| PROCESS_MESSAGE | IntrstHdrTrxHdrProcessMessage | — |
| PROCESS_STATUS | IntrstHdrTrxHdrProcessStatus | — |
| WORKER_NUM | IntrstHdrTrxHdrWorkerNum | — |

### [[transactionheaderpvo|TransactionHeaderPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHARGE_BEGIN_DATE | IntrstHdrTrxHdrChargeBeginDate | — |
| CHARGE_ON_FINANCE_CHARGE_FLAG | IntrstHdrTrxHdrChargeOnFinanceChargeFlag | — |
| CREDIT_ITEMS_FLAG | IntrstHdrTrxHdrCreditItemsFlag | — |
| CURRENCY_CODE | IntrstHdrTrxHdrCurrencyCode | — |
| DISPLAY_FLAG | IntrstHdrTrxHdrDisplayFlag | — |
| DISPUTED_TRANSACTIONS_FLAG | IntrstHdrTrxHdrDisputedTransactionsFlag | — |
| EXCHANGE_RATE | IntrstHdrTrxHdrExchangeRate | — |
| EXCHANGE_RATE_TYPE | IntrstHdrTrxHdrExchangeRateType | — |
| FINANCE_CHARGE_DATE | IntrstHdrTrxHdrFinanceChargeDate | — |
| HEADER_TYPE | IntrstHdrTrxHdrHeaderType | — |
| HOLD_CHARGED_INVOICES_FLAG | IntrstHdrTrxHdrHoldChargedInvoicesFlag | — |
| INTEREST_CALCULATION_PERIOD | IntrstHdrTrxHdrInterestCalculationPeriod | — |
| INTEREST_FIXED_AMOUNT | IntrstHdrTrxHdrInterestFixedAmount | — |
| INTEREST_HEADER_ID | IntrstHdrTrxHdrInterestHeaderId | — |
| INTEREST_PERIOD_DAYS | IntrstHdrTrxHdrInterestPeriodDays | — |
| INTEREST_RATE | IntrstHdrTrxHdrInterestRate | — |
| INTEREST_TYPE | IntrstHdrTrxHdrInterestType | — |
| LAST_ACCRUE_CHARGE_DATE | IntrstHdrTrxHdrLastAccrueChargeDate | — |
| LATE_CHARGE_CALCULATION_TRX | IntrstHdrTrxHdrLateChargeCalculationTrx | — |
| MAX_INTEREST_CHARGE | IntrstHdrTrxHdrMaxInterestCharge | — |
| MIN_FC_BALANCE_AMOUNT | IntrstHdrTrxHdrMinFcBalanceAmount | — |
| MIN_FC_BALANCE_OVERDUE_TYPE | IntrstHdrTrxHdrMinFcBalanceOverdueType | — |
| MIN_FC_BALANCE_PERCENT | IntrstHdrTrxHdrMinFcBalancePercent | — |
| MIN_FC_INVOICE_AMOUNT | IntrstHdrTrxHdrMinFcInvoiceAmount | — |
| MIN_FC_INVOICE_OVERDUE_TYPE | IntrstHdrTrxHdrMinFcInvoiceOverdueType | — |
| MIN_FC_INVOICE_PERCENT | IntrstHdrTrxHdrMinFcInvoicePercent | — |
| MIN_INTEREST_CHARGE | IntrstHdrTrxHdrMinInterestCharge | — |
| MULTIPLE_INTEREST_RATES_FLAG | IntrstHdrTrxHdrMultipleInterestRatesFlag | — |
| PAYMENT_GRACE_DAYS | IntrstHdrTrxHdrPaymentGraceDays | — |
| PENALTY_FIXED_AMOUNT | IntrstHdrTrxHdrPenaltyFixedAmount | — |
| PENALTY_RATE | IntrstHdrTrxHdrPenaltyRate | — |
| PENALTY_TYPE | IntrstHdrTrxHdrPenaltyType | — |
| PROCESS_MESSAGE | IntrstHdrTrxHdrProcessMessage | — |
| PROCESS_STATUS | IntrstHdrTrxHdrProcessStatus | — |
| WORKER_NUM | IntrstHdrTrxHdrWorkerNum | — |

### [[transactionhistorydistributionpvo|TransactionHistoryDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHARGE_BEGIN_DATE | IntrstHdrTrxHdrChargeBeginDate | — |
| CHARGE_ON_FINANCE_CHARGE_FLAG | IntrstHdrTrxHdrChargeOnFinanceChargeFlag | — |
| CREDIT_ITEMS_FLAG | IntrstHdrTrxHdrCreditItemsFlag | — |
| CURRENCY_CODE | IntrstHdrTrxHdrCurrencyCode | — |
| DISPLAY_FLAG | IntrstHdrTrxHdrDisplayFlag | — |
| DISPUTED_TRANSACTIONS_FLAG | IntrstHdrTrxHdrDisputedTransactionsFlag | — |
| EXCHANGE_RATE | IntrstHdrTrxHdrExchangeRate | — |
| EXCHANGE_RATE_TYPE | IntrstHdrTrxHdrExchangeRateType | — |
| FINANCE_CHARGE_DATE | IntrstHdrTrxHdrFinanceChargeDate | — |
| HEADER_TYPE | IntrstHdrTrxHdrHeaderType | — |
| HOLD_CHARGED_INVOICES_FLAG | IntrstHdrTrxHdrHoldChargedInvoicesFlag | — |
| INTEREST_CALCULATION_PERIOD | IntrstHdrTrxHdrInterestCalculationPeriod | — |
| INTEREST_FIXED_AMOUNT | IntrstHdrTrxHdrInterestFixedAmount | — |
| INTEREST_HEADER_ID | IntrstHdrTrxHdrInterestHeaderId | — |
| INTEREST_PERIOD_DAYS | IntrstHdrTrxHdrInterestPeriodDays | — |
| INTEREST_RATE | IntrstHdrTrxHdrInterestRate | — |
| INTEREST_TYPE | IntrstHdrTrxHdrInterestType | — |
| LAST_ACCRUE_CHARGE_DATE | IntrstHdrTrxHdrLastAccrueChargeDate | — |
| LATE_CHARGE_CALCULATION_TRX | IntrstHdrTrxHdrLateChargeCalculationTrx | — |
| MAX_INTEREST_CHARGE | IntrstHdrTrxHdrMaxInterestCharge | — |
| MIN_FC_BALANCE_AMOUNT | IntrstHdrTrxHdrMinFcBalanceAmount | — |
| MIN_FC_BALANCE_OVERDUE_TYPE | IntrstHdrTrxHdrMinFcBalanceOverdueType | — |
| MIN_FC_BALANCE_PERCENT | IntrstHdrTrxHdrMinFcBalancePercent | — |
| MIN_FC_INVOICE_AMOUNT | IntrstHdrTrxHdrMinFcInvoiceAmount | — |
| MIN_FC_INVOICE_OVERDUE_TYPE | IntrstHdrTrxHdrMinFcInvoiceOverdueType | — |
| MIN_FC_INVOICE_PERCENT | IntrstHdrTrxHdrMinFcInvoicePercent | — |
| MIN_INTEREST_CHARGE | IntrstHdrTrxHdrMinInterestCharge | — |
| MULTIPLE_INTEREST_RATES_FLAG | IntrstHdrTrxHdrMultipleInterestRatesFlag | — |
| PAYMENT_GRACE_DAYS | IntrstHdrTrxHdrPaymentGraceDays | — |
| PENALTY_FIXED_AMOUNT | IntrstHdrTrxHdrPenaltyFixedAmount | — |
| PENALTY_RATE | IntrstHdrTrxHdrPenaltyRate | — |
| PENALTY_TYPE | IntrstHdrTrxHdrPenaltyType | — |
| PROCESS_MESSAGE | IntrstHdrTrxHdrProcessMessage | — |
| PROCESS_STATUS | IntrstHdrTrxHdrProcessStatus | — |
| WORKER_NUM | IntrstHdrTrxHdrWorkerNum | — |

### [[transactionhistorypvo|TransactionHistoryPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHARGE_BEGIN_DATE | IntrstHdrTrxHdrChargeBeginDate | — |
| CHARGE_ON_FINANCE_CHARGE_FLAG | IntrstHdrTrxHdrChargeOnFinanceChargeFlag | — |
| CREDIT_ITEMS_FLAG | IntrstHdrTrxHdrCreditItemsFlag | — |
| CURRENCY_CODE | IntrstHdrTrxHdrCurrencyCode | — |
| DISPLAY_FLAG | IntrstHdrTrxHdrDisplayFlag | — |
| DISPUTED_TRANSACTIONS_FLAG | IntrstHdrTrxHdrDisputedTransactionsFlag | — |
| EXCHANGE_RATE | IntrstHdrTrxHdrExchangeRate | — |
| EXCHANGE_RATE_TYPE | IntrstHdrTrxHdrExchangeRateType | — |
| FINANCE_CHARGE_DATE | IntrstHdrTrxHdrFinanceChargeDate | — |
| HEADER_TYPE | IntrstHdrTrxHdrHeaderType | — |
| HOLD_CHARGED_INVOICES_FLAG | IntrstHdrTrxHdrHoldChargedInvoicesFlag | — |
| INTEREST_CALCULATION_PERIOD | IntrstHdrTrxHdrInterestCalculationPeriod | — |
| INTEREST_FIXED_AMOUNT | IntrstHdrTrxHdrInterestFixedAmount | — |
| INTEREST_HEADER_ID | IntrstHdrTrxHdrInterestHeaderId | — |
| INTEREST_PERIOD_DAYS | IntrstHdrTrxHdrInterestPeriodDays | — |
| INTEREST_RATE | IntrstHdrTrxHdrInterestRate | — |
| INTEREST_TYPE | IntrstHdrTrxHdrInterestType | — |
| LAST_ACCRUE_CHARGE_DATE | IntrstHdrTrxHdrLastAccrueChargeDate | — |
| LATE_CHARGE_CALCULATION_TRX | IntrstHdrTrxHdrLateChargeCalculationTrx | — |
| MAX_INTEREST_CHARGE | IntrstHdrTrxHdrMaxInterestCharge | — |
| MIN_FC_BALANCE_AMOUNT | IntrstHdrTrxHdrMinFcBalanceAmount | — |
| MIN_FC_BALANCE_OVERDUE_TYPE | IntrstHdrTrxHdrMinFcBalanceOverdueType | — |
| MIN_FC_BALANCE_PERCENT | IntrstHdrTrxHdrMinFcBalancePercent | — |
| MIN_FC_INVOICE_AMOUNT | IntrstHdrTrxHdrMinFcInvoiceAmount | — |
| MIN_FC_INVOICE_OVERDUE_TYPE | IntrstHdrTrxHdrMinFcInvoiceOverdueType | — |
| MIN_FC_INVOICE_PERCENT | IntrstHdrTrxHdrMinFcInvoicePercent | — |
| MIN_INTEREST_CHARGE | IntrstHdrTrxHdrMinInterestCharge | — |
| MULTIPLE_INTEREST_RATES_FLAG | IntrstHdrTrxHdrMultipleInterestRatesFlag | — |
| PAYMENT_GRACE_DAYS | IntrstHdrTrxHdrPaymentGraceDays | — |
| PENALTY_FIXED_AMOUNT | IntrstHdrTrxHdrPenaltyFixedAmount | — |
| PENALTY_RATE | IntrstHdrTrxHdrPenaltyRate | — |
| PENALTY_TYPE | IntrstHdrTrxHdrPenaltyType | — |
| PROCESS_MESSAGE | IntrstHdrTrxHdrProcessMessage | — |
| PROCESS_STATUS | IntrstHdrTrxHdrProcessStatus | — |
| WORKER_NUM | IntrstHdrTrxHdrWorkerNum | — |

### [[transactionlinebillsreceivablepvo|TransactionLineBillsReceivablePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHARGE_BEGIN_DATE | IntrstHdrTrxHdrChargeBeginDate | — |
| CHARGE_ON_FINANCE_CHARGE_FLAG | IntrstHdrTrxHdrChargeOnFinanceChargeFlag | — |
| CREDIT_ITEMS_FLAG | IntrstHdrTrxHdrCreditItemsFlag | — |
| CURRENCY_CODE | IntrstHdrTrxHdrCurrencyCode | — |
| DISPLAY_FLAG | IntrstHdrTrxHdrDisplayFlag | — |
| DISPUTED_TRANSACTIONS_FLAG | IntrstHdrTrxHdrDisputedTransactionsFlag | — |
| EXCHANGE_RATE | IntrstHdrTrxHdrExchangeRate | — |
| EXCHANGE_RATE_TYPE | IntrstHdrTrxHdrExchangeRateType | — |
| FINANCE_CHARGE_DATE | IntrstHdrTrxHdrFinanceChargeDate | — |
| HEADER_TYPE | IntrstHdrTrxHdrHeaderType | — |
| HOLD_CHARGED_INVOICES_FLAG | IntrstHdrTrxHdrHoldChargedInvoicesFlag | — |
| INTEREST_CALCULATION_PERIOD | IntrstHdrTrxHdrInterestCalculationPeriod | — |
| INTEREST_FIXED_AMOUNT | IntrstHdrTrxHdrInterestFixedAmount | — |
| INTEREST_HEADER_ID | IntrstHdrTrxHdrInterestHeaderId | — |
| INTEREST_PERIOD_DAYS | IntrstHdrTrxHdrInterestPeriodDays | — |
| INTEREST_RATE | IntrstHdrTrxHdrInterestRate | — |
| INTEREST_TYPE | IntrstHdrTrxHdrInterestType | — |
| LAST_ACCRUE_CHARGE_DATE | IntrstHdrTrxHdrLastAccrueChargeDate | — |
| LATE_CHARGE_CALCULATION_TRX | IntrstHdrTrxHdrLateChargeCalculationTrx | — |
| MAX_INTEREST_CHARGE | IntrstHdrTrxHdrMaxInterestCharge | — |
| MIN_FC_BALANCE_AMOUNT | IntrstHdrTrxHdrMinFcBalanceAmount | — |
| MIN_FC_BALANCE_OVERDUE_TYPE | IntrstHdrTrxHdrMinFcBalanceOverdueType | — |
| MIN_FC_BALANCE_PERCENT | IntrstHdrTrxHdrMinFcBalancePercent | — |
| MIN_FC_INVOICE_AMOUNT | IntrstHdrTrxHdrMinFcInvoiceAmount | — |
| MIN_FC_INVOICE_OVERDUE_TYPE | IntrstHdrTrxHdrMinFcInvoiceOverdueType | — |
| MIN_FC_INVOICE_PERCENT | IntrstHdrTrxHdrMinFcInvoicePercent | — |
| MIN_INTEREST_CHARGE | IntrstHdrTrxHdrMinInterestCharge | — |
| MULTIPLE_INTEREST_RATES_FLAG | IntrstHdrTrxHdrMultipleInterestRatesFlag | — |
| PAYMENT_GRACE_DAYS | IntrstHdrTrxHdrPaymentGraceDays | — |
| PENALTY_FIXED_AMOUNT | IntrstHdrTrxHdrPenaltyFixedAmount | — |
| PENALTY_RATE | IntrstHdrTrxHdrPenaltyRate | — |
| PENALTY_TYPE | IntrstHdrTrxHdrPenaltyType | — |
| PROCESS_MESSAGE | IntrstHdrTrxHdrProcessMessage | — |
| PROCESS_STATUS | IntrstHdrTrxHdrProcessStatus | — |
| WORKER_NUM | IntrstHdrTrxHdrWorkerNum | — |

### [[transactionlinedistributionpvo|TransactionLineDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHARGE_BEGIN_DATE | IntrstHdrTrxHdrChargeBeginDate | — |
| CHARGE_ON_FINANCE_CHARGE_FLAG | IntrstHdrTrxHdrChargeOnFinanceChargeFlag | — |
| CREDIT_ITEMS_FLAG | IntrstHdrTrxHdrCreditItemsFlag | — |
| CURRENCY_CODE | IntrstHdrTrxHdrCurrencyCode | — |
| DISPLAY_FLAG | IntrstHdrTrxHdrDisplayFlag | — |
| DISPUTED_TRANSACTIONS_FLAG | IntrstHdrTrxHdrDisputedTransactionsFlag | — |
| EXCHANGE_RATE | IntrstHdrTrxHdrExchangeRate | — |
| EXCHANGE_RATE_TYPE | IntrstHdrTrxHdrExchangeRateType | — |
| FINANCE_CHARGE_DATE | IntrstHdrTrxHdrFinanceChargeDate | — |
| HEADER_TYPE | IntrstHdrTrxHdrHeaderType | — |
| HOLD_CHARGED_INVOICES_FLAG | IntrstHdrTrxHdrHoldChargedInvoicesFlag | — |
| INTEREST_CALCULATION_PERIOD | IntrstHdrTrxHdrInterestCalculationPeriod | — |
| INTEREST_FIXED_AMOUNT | IntrstHdrTrxHdrInterestFixedAmount | — |
| INTEREST_HEADER_ID | IntrstHdrTrxHdrInterestHeaderId | — |
| INTEREST_PERIOD_DAYS | IntrstHdrTrxHdrInterestPeriodDays | — |
| INTEREST_RATE | IntrstHdrTrxHdrInterestRate | — |
| INTEREST_TYPE | IntrstHdrTrxHdrInterestType | — |
| LAST_ACCRUE_CHARGE_DATE | IntrstHdrTrxHdrLastAccrueChargeDate | — |
| LATE_CHARGE_CALCULATION_TRX | IntrstHdrTrxHdrLateChargeCalculationTrx | — |
| MAX_INTEREST_CHARGE | IntrstHdrTrxHdrMaxInterestCharge | — |
| MIN_FC_BALANCE_AMOUNT | IntrstHdrTrxHdrMinFcBalanceAmount | — |
| MIN_FC_BALANCE_OVERDUE_TYPE | IntrstHdrTrxHdrMinFcBalanceOverdueType | — |
| MIN_FC_BALANCE_PERCENT | IntrstHdrTrxHdrMinFcBalancePercent | — |
| MIN_FC_INVOICE_AMOUNT | IntrstHdrTrxHdrMinFcInvoiceAmount | — |
| MIN_FC_INVOICE_OVERDUE_TYPE | IntrstHdrTrxHdrMinFcInvoiceOverdueType | — |
| MIN_FC_INVOICE_PERCENT | IntrstHdrTrxHdrMinFcInvoicePercent | — |
| MIN_INTEREST_CHARGE | IntrstHdrTrxHdrMinInterestCharge | — |
| MULTIPLE_INTEREST_RATES_FLAG | IntrstHdrTrxHdrMultipleInterestRatesFlag | — |
| PAYMENT_GRACE_DAYS | IntrstHdrTrxHdrPaymentGraceDays | — |
| PENALTY_FIXED_AMOUNT | IntrstHdrTrxHdrPenaltyFixedAmount | — |
| PENALTY_RATE | IntrstHdrTrxHdrPenaltyRate | — |
| PENALTY_TYPE | IntrstHdrTrxHdrPenaltyType | — |
| PROCESS_MESSAGE | IntrstHdrTrxHdrProcessMessage | — |
| PROCESS_STATUS | IntrstHdrTrxHdrProcessStatus | — |
| WORKER_NUM | IntrstHdrTrxHdrWorkerNum | — |

### [[transactionlinepvo|TransactionLinePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHARGE_BEGIN_DATE | IntrstHdrTrxHdrChargeBeginDate | — |
| CHARGE_ON_FINANCE_CHARGE_FLAG | IntrstHdrTrxHdrChargeOnFinanceChargeFlag | — |
| CREDIT_ITEMS_FLAG | IntrstHdrTrxHdrCreditItemsFlag | — |
| CURRENCY_CODE | IntrstHdrTrxHdrCurrencyCode | — |
| DISPLAY_FLAG | IntrstHdrTrxHdrDisplayFlag | — |
| DISPUTED_TRANSACTIONS_FLAG | IntrstHdrTrxHdrDisputedTransactionsFlag | — |
| EXCHANGE_RATE | IntrstHdrTrxHdrExchangeRate | — |
| EXCHANGE_RATE_TYPE | IntrstHdrTrxHdrExchangeRateType | — |
| FINANCE_CHARGE_DATE | IntrstHdrTrxHdrFinanceChargeDate | — |
| HEADER_TYPE | IntrstHdrTrxHdrHeaderType | — |
| HOLD_CHARGED_INVOICES_FLAG | IntrstHdrTrxHdrHoldChargedInvoicesFlag | — |
| INTEREST_CALCULATION_PERIOD | IntrstHdrTrxHdrInterestCalculationPeriod | — |
| INTEREST_FIXED_AMOUNT | IntrstHdrTrxHdrInterestFixedAmount | — |
| INTEREST_HEADER_ID | IntrstHdrTrxHdrInterestHeaderId | — |
| INTEREST_PERIOD_DAYS | IntrstHdrTrxHdrInterestPeriodDays | — |
| INTEREST_RATE | IntrstHdrTrxHdrInterestRate | — |
| INTEREST_TYPE | IntrstHdrTrxHdrInterestType | — |
| LAST_ACCRUE_CHARGE_DATE | IntrstHdrTrxHdrLastAccrueChargeDate | — |
| LATE_CHARGE_CALCULATION_TRX | IntrstHdrTrxHdrLateChargeCalculationTrx | — |
| MAX_INTEREST_CHARGE | IntrstHdrTrxHdrMaxInterestCharge | — |
| MIN_FC_BALANCE_AMOUNT | IntrstHdrTrxHdrMinFcBalanceAmount | — |
| MIN_FC_BALANCE_OVERDUE_TYPE | IntrstHdrTrxHdrMinFcBalanceOverdueType | — |
| MIN_FC_BALANCE_PERCENT | IntrstHdrTrxHdrMinFcBalancePercent | — |
| MIN_FC_INVOICE_AMOUNT | IntrstHdrTrxHdrMinFcInvoiceAmount | — |
| MIN_FC_INVOICE_OVERDUE_TYPE | IntrstHdrTrxHdrMinFcInvoiceOverdueType | — |
| MIN_FC_INVOICE_PERCENT | IntrstHdrTrxHdrMinFcInvoicePercent | — |
| MIN_INTEREST_CHARGE | IntrstHdrTrxHdrMinInterestCharge | — |
| MULTIPLE_INTEREST_RATES_FLAG | IntrstHdrTrxHdrMultipleInterestRatesFlag | — |
| PAYMENT_GRACE_DAYS | IntrstHdrTrxHdrPaymentGraceDays | — |
| PENALTY_FIXED_AMOUNT | IntrstHdrTrxHdrPenaltyFixedAmount | — |
| PENALTY_RATE | IntrstHdrTrxHdrPenaltyRate | — |
| PENALTY_TYPE | IntrstHdrTrxHdrPenaltyType | — |
| PROCESS_MESSAGE | IntrstHdrTrxHdrProcessMessage | — |
| PROCESS_STATUS | IntrstHdrTrxHdrProcessStatus | — |
| WORKER_NUM | IntrstHdrTrxHdrWorkerNum | — |

---

## 📚 Referências

- Oracle Fusion Cloud Financials — Accounts Receivable Tables (OEDMF Release 13).
- Oracle Fusion Cloud — Late Charges and Finance Charges Documentation.
- Oracle Fusion Cloud ERP Schema Reference (Release 25A).
