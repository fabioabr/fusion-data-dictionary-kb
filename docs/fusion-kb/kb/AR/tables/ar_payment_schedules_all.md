---
id: DOC-AR-021
doc_type: system-doc
title: "AR_PAYMENT_SCHEDULES_ALL — Cronogramas de Pagamento"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - accounts-receivable
  - data-dictionary
  - cronograma-pagamento
  - payment-schedules
  - aging
aliases:
  - AR_PAYMENT_SCHEDULES_ALL
  - ar_payment_schedules_all
  - cronograma-pagamento-ar
  - payment-schedules
  - aging-ar
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_PAYMENT_SCHEDULES_ALL

## 📌 Visão Geral

Armazena os **cronogramas de pagamento de todas as transações e recebimentos** do módulo Accounts Receivable. Cada registro representa uma parcela de pagamento com data de vencimento, valor original, saldo remanescente e valores aplicados/creditados/ajustados. É a tabela fundamental para cálculo de **aging** (envelhecimento de recebíveis), controle de inadimplência e análise de saldos em aberto.

A coluna `CLASS` distingue o tipo: INV (fatura), CM (credit memo), DM (debit memo), DEP (depósito), GUAR (garantia), BR (bill receivable) e PMT (pagamento/recebimento).

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Aging de recebíveis:** Cálculo de saldos em aberto por faixa de vencimento (current, 1-30, 31-60, 61-90, 90+).
- **Controle de inadimplência:** Identificação de faturas vencidas via `DUE_DATE` × `AMOUNT_DUE_REMAINING`.
- **Cobrança:** Base para processos de dunning — seleção de faturas vencidas por cliente/site.
- **Conciliação AR:** Saldo em aberto (`AMOUNT_DUE_REMAINING`) deve bater com subledger e GL.
- **Relatórios de saldo:** Extração de posição de contas a receber por cliente, moeda, business unit.
- **Disputas:** Registro de valores em disputa via `AMOUNT_IN_DISPUTE`.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PAYMENT_SCHEDULE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do schedule de pagamento | — | 🟢 100% |
| 2 | CUSTOMER_TRX_ID | NUMBER(18) | NULL | FK | Transação associada (faturas, CMs, DMs) | [[ra_customer_trx_all]] | 🟢 100% |
| 3 | CASH_RECEIPT_ID | NUMBER(18) | NULL | FK | Recebimento associado | [[ar_cash_receipts_all]] | 🟢 100% |
| 4 | CLASS | VARCHAR2(30) | NOT NULL | Classificação | Tipo: INV/CM/DM/DEP/GUAR/BR/PMT | — | 🟢 100% |
| 5 | STATUS | VARCHAR2(30) | NOT NULL | Classificação | Status: OP (aberto) ou CL (fechado) | — | 🟢 100% |
| 6 | DUE_DATE | DATE | NOT NULL | Data | Data de vencimento da parcela | — | 🟢 100% |
| 7 | AMOUNT_DUE_ORIGINAL | NUMBER | NOT NULL | Financeiro | Valor original da parcela | — | 🟢 100% |
| 8 | AMOUNT_DUE_REMAINING | NUMBER | NOT NULL | Financeiro | Saldo remanescente (valor em aberto) | — | 🟢 100% |
| 9 | AMOUNT_APPLIED | NUMBER | NULL | Financeiro | Total aplicado (recebimentos + credit memos) | — | 🟢 100% |
| 10 | AMOUNT_CREDITED | NUMBER | NULL | Financeiro | Total creditado via credit memos | — | 🟢 100% |
| 11 | AMOUNT_ADJUSTED | NUMBER | NULL | Financeiro | Total ajustado (write-offs, reclassificações) | — | 🟢 100% |
| 12 | AMOUNT_IN_DISPUTE | NUMBER | NULL | Financeiro | Valor em disputa | — | 🟢 100% |
| 13 | AMOUNT_LINE_ITEMS_ORIGINAL | NUMBER | NULL | Financeiro | Valor original de itens de linha | — | 🟢 100% |
| 14 | TAX_ORIGINAL | NUMBER | NULL | Financeiro | Valor original de imposto | — | 🟢 100% |
| 15 | TAX_REMAINING | NUMBER | NULL | Financeiro | Saldo remanescente de imposto | — | 🟢 100% |
| 16 | FREIGHT_ORIGINAL | NUMBER | NULL | Financeiro | Valor original de frete | — | 🟢 100% |
| 17 | FREIGHT_REMAINING | NUMBER | NULL | Financeiro | Saldo remanescente de frete | — | 🟢 100% |
| 18 | NUMBER_OF_DUE_DATES | NUMBER | NULL | Financeiro | Número total de parcelas da transação | — | 🟢 100% |
| 19 | TERMS_SEQUENCE_NUMBER | NUMBER | NULL | Financeiro | Número sequencial da parcela nos termos de pagamento | — | 🟢 100% |
| 20 | CUSTOMER_ID | NUMBER(18) | NULL | Cliente | Conta do cliente | [[hz_cust_accounts]] | 🟢 100% |
| 21 | CUSTOMER_SITE_USE_ID | NUMBER(18) | NULL | Cliente | Site de uso do cliente | [[hz_cust_site_uses_all]] | 🟢 100% |
| 22 | INVOICE_CURRENCY_CODE | VARCHAR2(15) | NOT NULL | Financeiro | Código da moeda (ISO 4217) | — | 🟢 100% |
| 23 | EXCHANGE_RATE_TYPE | VARCHAR2(30) | NULL | Financeiro | Tipo de taxa de câmbio | [[gl_daily_conversion_types]] | 🟢 100% |
| 24 | EXCHANGE_RATE | NUMBER | NULL | Financeiro | Taxa de câmbio aplicada | — | 🟢 100% |
| 25 | EXCHANGE_DATE | DATE | NULL | Financeiro | Data da taxa de câmbio | — | 🟢 100% |
| 26 | GL_DATE | DATE | NULL | Contabilidade | Data contábil (General Ledger) | — | 🟢 100% |
| 27 | GL_DATE_CLOSED | DATE | NULL | Contabilidade | Data contábil de fechamento | — | 🟢 100% |
| 28 | ACTUAL_DATE_CLOSED | DATE | NULL | Data | Data real de fechamento do schedule | — | 🟢 100% |
| 29 | TRX_NUMBER | VARCHAR2(30) | NULL | Identificação | Número da transação (denormalizado) | — | 🟢 100% |
| 30 | TRX_DATE | DATE | NULL | Data | Data da transação (denormalizado) | — | 🟢 100% |
| 31 | CUST_TRX_TYPE_ID | NUMBER(18) | NULL | Classificação | Tipo de transação | [[ra_cust_trx_types_all]] | 🟢 100% |
| 32 | TERM_ID | NUMBER(18) | NULL | Financeiro | Condição de pagamento | [[ra_terms_b]] | 🟢 100% |
| 33 | DISCOUNT_DATE | DATE | NULL | Data | Data limite para desconto | — | 🟢 100% |
| 34 | DISCOUNT_ORIGINAL | NUMBER | NULL | Financeiro | Valor do desconto disponível | — | 🟢 100% |
| 35 | DISCOUNT_TAKEN_EARNED | NUMBER | NULL | Financeiro | Desconto concedido aproveitado | — | 🟢 100% |
| 36 | DISCOUNT_TAKEN_UNEARNED | NUMBER | NULL | Financeiro | Desconto não-concedido aproveitado | — | 🟢 100% |
| 37 | SELECTED_FOR_RECEIPT_BATCH_ID | NUMBER(18) | NULL | Controle | Lote de recebimento em que o schedule foi selecionado | — | 🟢 100% |
| 38 | DISPUTE_DATE | DATE | NULL | Data | Data da disputa | — | 🟢 100% |
| 39 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 40 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 41 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 42 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 43 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 44 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ra_customer_trx_all]] — via `CUSTOMER_TRX_ID` (transação de cliente associada à parcela)
- [[ar_cash_receipts_all]] — via `CASH_RECEIPT_ID` (recebimento de caixa vinculado à parcela)
- [[hz_cust_accounts]] — via `CUSTOMER_ID` (cliente devedor da parcela)
- [[hz_cust_site_uses_all]] — via `CUSTOMER_SITE_USE_ID` (site do cliente)
- [[ra_cust_trx_types_all]] — via `CUST_TRX_TYPE_ID` (tipo de transação)
- [[ra_terms_b]] — via `TERM_ID` (condição de pagamento)
- [[gl_daily_conversion_types]] — via `EXCHANGE_RATE_TYPE` (tipo de câmbio da parcela de recebimento)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit da parcela de recebimento)

### Tabelas-filha (FK de saída)
- [[ar_receivable_applications_all]] — via `APPLIED_PAYMENT_SCHEDULE_ID` e `PAYMENT_SCHEDULE_ID` (aplicações de pagamento contra esta parcela)
- [[ar_adjustments_all]] — via `PAYMENT_SCHEDULE_ID` (ajustes aplicados a esta parcela de recebimento)

---

## 📎 Uso Típico

### Saldo em aberto por cliente (aging)
```sql
SELECT ps.CUSTOMER_ID, hca.ACCOUNT_NAME,
       SUM(ps.AMOUNT_DUE_REMAINING) AS saldo_aberto,
       SUM(CASE WHEN ps.DUE_DATE < SYSDATE THEN ps.AMOUNT_DUE_REMAINING ELSE 0 END) AS vencido
FROM   AR_PAYMENT_SCHEDULES_ALL ps
JOIN   HZ_CUST_ACCOUNTS hca ON hca.CUST_ACCOUNT_ID = ps.CUSTOMER_ID
WHERE  ps.STATUS = 'OP'
  AND  ps.CLASS = 'INV'
  AND  ps.ORG_ID = :p_org_id
GROUP BY ps.CUSTOMER_ID, hca.ACCOUNT_NAME;
```

### Faturas vencidas há mais de 90 dias
```sql
SELECT ps.TRX_NUMBER, ps.DUE_DATE, ps.AMOUNT_DUE_REMAINING,
       TRUNC(SYSDATE) - ps.DUE_DATE AS dias_atraso
FROM   AR_PAYMENT_SCHEDULES_ALL ps
WHERE  ps.STATUS = 'OP'
  AND  ps.CLASS = 'INV'
  AND  ps.DUE_DATE < SYSDATE - 90
  AND  ps.ORG_ID = :p_org_id
ORDER BY dias_atraso DESC;
```

### Filtros comuns
- `STATUS = 'OP'` — Schedules em aberto
- `STATUS = 'CL'` — Schedules fechados
- `CLASS = 'INV'` — Apenas faturas
- `CLASS = 'PMT'` — Apenas recebimentos
- `AMOUNT_DUE_REMAINING > 0` — Com saldo remanescente

---

## 🔒 Observações

- A relação `AMOUNT_DUE_REMAINING = AMOUNT_DUE_ORIGINAL - AMOUNT_APPLIED - AMOUNT_CREDITED - AMOUNT_ADJUSTED` deve ser sempre consistente.
- Um registro existe para **cada parcela** — transações com condição de pagamento parcelada geram múltiplos schedules (e.g., 30/60/90 dias gera 3 registros).
- O campo `CLASS = 'PMT'` indica um schedule de recebimento (cash receipt) — o saldo remanescente negativo indica valor não-aplicado.
- Os campos `GL_DATE_CLOSED` e `ACTUAL_DATE_CLOSED` são preenchidos quando `STATUS` muda para 'CL'.
- Os campos `TAX_ORIGINAL`, `TAX_REMAINING`, `FREIGHT_ORIGINAL`, `FREIGHT_REMAINING` são **denormalizados** para performance em relatórios de aging.

---

## 🔗 PVOs Relacionados

### [[adjustmentdistributionpvo|AdjustmentDistributionPVO]] (AR · BICC: 13/93)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_DUE_REMAINING | PaymentScheduleAcctdAmountDueRemaining | — |
| ACTIVE_CLAIM_FLAG | PaymentScheduleActiveClaimFlag | — |
| ACTUAL_DATE_CLOSED | PaymentScheduleActualDateClosed | — |
| ADJUSTMENT_AMOUNT_LAST | PaymentScheduleAdjustmentAmountLast | — |
| ADJUSTMENT_DATE_LAST | PaymentScheduleAdjustmentDateLast | — |
| ADJUSTMENT_GL_DATE_LAST | PaymentScheduleAdjustmentGlDateLast | — |
| ADJUSTMENT_ID_LAST | PaymentScheduleAdjustmentIdLast | — |
| AMOUNT_ADJUSTED | PaymentScheduleAmountAdjusted | — |
| AMOUNT_ADJUSTED_PENDING | PaymentScheduleAmountAdjustedPending | — |
| AMOUNT_APPLIED | PaymentScheduleAmountApplied | — |
| AMOUNT_CREDITED | PaymentScheduleAmountCredited | — |
| AMOUNT_DUE_ORIGINAL | PaymentScheduleAmountDueOriginal | — |
| AMOUNT_DUE_REMAINING | PaymentScheduleAmountDueRemaining | — |
| AMOUNT_IN_DISPUTE | PaymentScheduleAmountInDispute | — |
| AMOUNT_LINE_ITEMS_ORIGINAL | PaymentScheduleAmountLineItemsOriginal | — |
| AMOUNT_LINE_ITEMS_REMAINING | PaymentScheduleAmountLineItemsRemaining | — |
| AMOUNT_ON_ACCOUNT | PaymentScheduleAmountOnAccount | — |
| AMOUNT_OTHER_ACCOUNT | PaymentScheduleAmountOtherAccount | — |
| ASSOCIATED_CASH_RECEIPT_ID | PaymentScheduleAssociatedCashReceiptId | — |
| BR_AMOUNT_ASSIGNED | PaymentScheduleBrAmountAssigned | — |
| CALL_DATE_LAST | PaymentScheduleCallDateLast | — |
| CASH_APPLIED_AMOUNT_LAST | PaymentScheduleCashAppliedAmountLast | — |
| CASH_APPLIED_DATE_LAST | PaymentScheduleCashAppliedDateLast | — |
| CASH_APPLIED_ID_LAST | PaymentScheduleCashAppliedIdLast | — |
| CASH_APPLIED_STATUS_LAST | PaymentScheduleCashAppliedStatusLast | — |
| CASH_GL_DATE_LAST | PaymentScheduleCashGlDateLast | — |
| CASH_RECEIPT_AMOUNT_LAST | PaymentScheduleCashReceiptAmountLast | — |
| CASH_RECEIPT_DATE_LAST | PaymentScheduleCashReceiptDateLast | — |
| CASH_RECEIPT_ID | PaymentScheduleCashReceiptId | — |
| CASH_RECEIPT_ID_LAST | PaymentScheduleCashReceiptIdLast | — |
| CASH_RECEIPT_STATUS_LAST | PaymentScheduleCashReceiptStatusLast | — |
| CLASS | PaymentSchedulePaymentScheduleClass | — |
| COLLECTOR_LAST | PaymentScheduleCollectorLast | — |
| CONS_INV_ID | PaymentScheduleConsInvId | — |
| CONS_INV_ID_REV | PaymentScheduleConsInvIdRev | — |
| CREATED_BY | PaymentScheduleCreatedBy | — |
| CREATION_DATE | PaymentScheduleCreationDate | — |
| CUST_TRX_TYPE_SEQ_ID | PaymentScheduleCustTrxTypeSeqId | — |
| CUSTOMER_ID | PaymentScheduleCustomerId | — |
| CUSTOMER_SITE_USE_ID | PaymentScheduleCustomerSiteUseId | ✅ |
| CUSTOMER_TRX_ID | PaymentScheduleCustomerTrxId | — |
| DISCOUNT_DATE | PaymentScheduleDiscountDate | — |
| DISCOUNT_ORIGINAL | PaymentScheduleDiscountOriginal | — |
| DISCOUNT_REMAINING | PaymentScheduleDiscountRemaining | — |
| DISCOUNT_TAKEN_EARNED | PaymentScheduleDiscountTakenEarned | — |
| DISCOUNT_TAKEN_UNEARNED | PaymentScheduleDiscountTakenUnearned | — |
| DISPUTE_DATE | PaymentScheduleDisputeDate | ✅ |
| DUE_DATE | PaymentScheduleDueDate | ✅ |
| DUNNING_LEVEL_OVERRIDE_DATE | PaymentScheduleDunningLevelOverrideDate | — |
| EXCHANGE_DATE | PaymentScheduleExchangeDate | ✅ |
| EXCHANGE_RATE | PaymentScheduleExchangeRate | ✅ |
| EXCHANGE_RATE_TYPE | PaymentScheduleExchangeRateType | ✅ |
| EXCLUDE_FROM_CONS_BILL_FLAG | PaymentScheduleExcludeFromConsBillFlag | — |
| EXCLUDE_FROM_DUNNING_FLAG | PaymentScheduleExcludeFromDunningFlag | — |
| FOLLOW_UP_CODE_LAST | PaymentScheduleFollowUpCodeLast | — |
| FOLLOW_UP_DATE_LAST | PaymentScheduleFollowUpDateLast | — |
| FREIGHT_ORIGINAL | PaymentScheduleFreightOriginal | — |
| FREIGHT_REMAINING | PaymentScheduleFreightRemaining | — |
| GL_DATE | PaymentScheduleGlDate | ✅ |
| GL_DATE_CLOSED | PaymentScheduleGlDateClosed | — |
| IN_COLLECTION | PaymentScheduleInCollection | — |
| INVOICE_CURRENCY_CODE | PaymentScheduleInvoiceCurrencyCode | — |
| LAST_CHARGE_DATE | PaymentScheduleLastChargeDate | — |
| LAST_UPDATE_DATE | PaymentScheduleLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PaymentScheduleLastUpdateLogin | — |
| LAST_UPDATED_BY | PaymentScheduleLastUpdatedBy | — |
| NUMBER_OF_DUE_DATES | PaymentScheduleNumberOfDueDates | — |
| OBJECT_VERSION_NUMBER | PaymentScheduleObjectVersionNumber | — |
| ORG_ID | PaymentScheduleOrgId | — |
| PAYMENT_APPROVAL | PaymentSchedulePaymentApproval | — |
| PAYMENT_SCHEDULE_ID | PaymentSchedulePaymentScheduleId | ✅ |
| PROGRAM_APPLICATION_ID | PaymentScheduleProgramApplicationId | — |
| PROGRAM_ID | PaymentScheduleProgramId | — |
| PROGRAM_UPDATE_DATE | PaymentScheduleProgramUpdateDate | — |
| PROMISE_AMOUNT_LAST | PaymentSchedulePromiseAmountLast | — |
| PROMISE_DATE_LAST | PaymentSchedulePromiseDateLast | — |
| RECEIPT_CONFIRMED_FLAG | PaymentScheduleReceiptConfirmedFlag | — |
| RECEIVABLES_CHARGES_CHARGED | PaymentScheduleReceivablesChargesCharged | — |
| RECEIVABLES_CHARGES_REMAINING | PaymentScheduleReceivablesChargesRemaining | — |
| REQUEST_ID | PaymentScheduleRequestId | — |
| RESERVED_TYPE | PaymentScheduleReservedType | — |
| RESERVED_VALUE | PaymentScheduleReservedValue | — |
| REVERSED_CASH_RECEIPT_ID | PaymentScheduleReversedCashReceiptId | — |
| SECOND_LAST_CHARGE_DATE | PaymentScheduleSecondLastChargeDate | — |
| SELECTED_FOR_RECEIPT_BATCH_ID | PaymentScheduleSelectedForReceiptBatchId | — |
| STAGED_DUNNING_LEVEL | PaymentScheduleStagedDunningLevel | — |
| STATUS | PaymentScheduleStatus | ✅ |
| TAX_ORIGINAL | PaymentScheduleTaxOriginal | — |
| TAX_REMAINING | PaymentScheduleTaxRemaining | — |
| TERM_ID | PaymentScheduleTermId | — |
| TERMS_SEQUENCE_NUMBER | PaymentScheduleTermsSequenceNumber | ✅ |
| TRX_DATE | PaymentScheduleTrxDate | ✅ |
| TRX_NUMBER | PaymentScheduleTrxNumber | ✅ |

### [[adjustmentpvo|AdjustmentPVO]] (AR · BICC: 9/72)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_DUE_REMAINING | PmtScheduleAcctdAmountDueRemaining | — |
| ACTIVE_CLAIM_FLAG | PmtScheduleActiveClaimFlag | — |
| ACTUAL_DATE_CLOSED | PmtScheduleActualDateClosed | — |
| ADJUSTMENT_AMOUNT_LAST | PmtScheduleAdjustmentAmountLast | — |
| ADJUSTMENT_DATE_LAST | PmtScheduleAdjustmentDateLast | — |
| ADJUSTMENT_GL_DATE_LAST | PmtScheduleAdjustmentGlDateLast | — |
| ADJUSTMENT_ID_LAST | PmtScheduleAdjustmentIdLast | — |
| AMOUNT_ADJUSTED | PmtScheduleAmountAdjusted | — |
| AMOUNT_ADJUSTED_PENDING | PmtScheduleAmountAdjustedPending | — |
| AMOUNT_APPLIED | PmtScheduleAmountApplied | — |
| AMOUNT_CREDITED | PmtScheduleAmountCredited | — |
| AMOUNT_DUE_ORIGINAL | PmtScheduleAmountDueOriginal | — |
| AMOUNT_DUE_REMAINING | PmtScheduleAmountDueRemaining | — |
| AMOUNT_IN_DISPUTE | PmtScheduleAmountInDispute | — |
| AMOUNT_LINE_ITEMS_ORIGINAL | PmtScheduleAmountLineItemsOriginal | — |
| AMOUNT_LINE_ITEMS_REMAINING | PmtScheduleAmountLineItemsRemaining | — |
| AMOUNT_ON_ACCOUNT | PmtScheduleAmountOnAccount | — |
| AMOUNT_OTHER_ACCOUNT | PmtScheduleAmountOtherAccount | — |
| ASSOCIATED_CASH_RECEIPT_ID | PmtScheduleAssociatedCashReceiptId | — |
| BR_AMOUNT_ASSIGNED | PmtScheduleBrAmountAssigned | — |
| CALL_DATE_LAST | PmtScheduleCallDateLast | — |
| CASH_RECEIPT_ID | PmtScheduleCashReceiptId | — |
| CLASS | PmtSchedulePaymentScheduleClass | — |
| COLLECTOR_LAST | PmtScheduleCollectorLast | — |
| CONS_INV_ID | PmtScheduleConsInvId | — |
| CONS_INV_ID_REV | PmtScheduleConsInvIdRev | — |
| CUST_TRX_TYPE_SEQ_ID | PmtScheduleCustTrxTypeSeqId | — |
| CUSTOMER_ID | PmtScheduleCustomerId | — |
| CUSTOMER_TRX_ID | PmtScheduleCustomerTrxId | — |
| DISCOUNT_DATE | PmtScheduleDiscountDate | — |
| DISCOUNT_ORIGINAL | PmtScheduleDiscountOriginal | — |
| DISCOUNT_REMAINING | PmtScheduleDiscountRemaining | — |
| DISCOUNT_TAKEN_EARNED | PmtScheduleDiscountTakenEarned | — |
| DISCOUNT_TAKEN_UNEARNED | PmtScheduleDiscountTakenUnearned | — |
| DISPUTE_DATE | PmtScheduleDisputeDate | ✅ |
| DUE_DATE | PmtScheduleDueDate | ✅ |
| EXCHANGE_DATE | PmtScheduleExchangeDate | ✅ |
| EXCHANGE_RATE | PmtScheduleExchangeRate | ✅ |
| EXCHANGE_RATE_TYPE | PmtScheduleExchangeRateType | ✅ |
| EXCLUDE_FROM_CONS_BILL_FLAG | PmtScheduleExcludeFromConsBillFlag | — |
| FOLLOW_UP_CODE_LAST | PmtScheduleFollowUpCodeLast | — |
| FOLLOW_UP_DATE_LAST | PmtScheduleFollowUpDateLast | — |
| FREIGHT_ORIGINAL | PmtScheduleFreightOriginal | — |
| FREIGHT_REMAINING | PmtScheduleFreightRemaining | — |
| GL_DATE | PmtScheduleGlDate | ✅ |
| GL_DATE_CLOSED | PmtScheduleGlDateClosed | — |
| IN_COLLECTION | PmtScheduleInCollection | — |
| INVOICE_CURRENCY_CODE | PmtScheduleInvoiceCurrencyCode | — |
| LAST_CHARGE_DATE | PmtScheduleLastChargeDate | — |
| NUMBER_OF_DUE_DATES | PmtScheduleNumberOfDueDates | — |
| OBJECT_VERSION_NUMBER | PmtScheduleObjectVersionNumber2 | — |
| ORG_ID | PmtScheduleOrgId | — |
| PAYMENT_APPROVAL | PmtSchedulePaymentApproval | — |
| PAYMENT_SCHEDULE_ID | PmtSchedulePaymentScheduleId | — |
| PROMISE_AMOUNT_LAST | PmtSchedulePromiseAmountLast | — |
| PROMISE_DATE_LAST | PmtSchedulePromiseDateLast | — |
| RECEIVABLES_CHARGES_CHARGED | PmtScheduleReceivablesChargesCharged | — |
| RECEIVABLES_CHARGES_REMAINING | PmtScheduleReceivablesChargesRemaining | — |
| REQUEST_ID | PmtScheduleRequestId | — |
| RESERVED_TYPE | PmtScheduleReservedType | — |
| RESERVED_VALUE | PmtScheduleReservedValue | — |
| REVERSED_CASH_RECEIPT_ID | PmtScheduleReversedCashReceiptId | — |
| SECOND_LAST_CHARGE_DATE | PmtScheduleSecondLastChargeDate | — |
| SELECTED_FOR_RECEIPT_BATCH_ID | PmtScheduleSelectedForReceiptBatchId | — |
| STAGED_DUNNING_LEVEL | PmtScheduleStagedDunningLevel | — |
| STATUS | PmtScheduleStatus | ✅ |
| TAX_ORIGINAL | PmtScheduleTaxOriginal | — |
| TAX_REMAINING | PmtScheduleTaxRemaining | — |
| TERM_ID | PmtScheduleTermId | — |
| TERMS_SEQUENCE_NUMBER | PmtScheduleTermsSequenceNumber | — |
| TRX_DATE | PmtScheduleTrxDate | ✅ |
| TRX_NUMBER | PmtScheduleTrxNumber | ✅ |

### [[completedtrxrevadjdistributionpvo|CompletedTrxRevAdjDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_DUE_REMAINING | PaymentScheduleAcctdAmountDueRemaining | — |
| ACCTD_AMOUNT_DUE_REMAINING | PaymentSchedulesLineAcctdAmountDueRemaining | — |
| ACTIVE_CLAIM_FLAG | PaymentScheduleActiveClaimFlag | — |
| ACTIVE_CLAIM_FLAG | PaymentSchedulesLineActiveClaimFlag | — |
| ACTUAL_DATE_CLOSED | PaymentScheduleActualDateClosed | — |
| ACTUAL_DATE_CLOSED | PaymentSchedulesLineActualDateClosed | — |
| ADJUSTMENT_AMOUNT_LAST | PaymentScheduleAdjustmentAmountLast | — |
| ADJUSTMENT_AMOUNT_LAST | PaymentSchedulesLineAdjustmentAmountLast | — |
| ADJUSTMENT_DATE_LAST | PaymentScheduleAdjustmentDateLast | — |
| ADJUSTMENT_DATE_LAST | PaymentSchedulesLineAdjustmentDateLast | — |
| ADJUSTMENT_GL_DATE_LAST | PaymentScheduleAdjustmentGlDateLast | — |
| ADJUSTMENT_GL_DATE_LAST | PaymentSchedulesLineAdjustmentGlDateLast | — |
| ADJUSTMENT_ID_LAST | PaymentScheduleAdjustmentIdLast | — |
| ADJUSTMENT_ID_LAST | PaymentSchedulesLineAdjustmentIdLast | — |
| AMOUNT_ADJUSTED | PaymentScheduleAmountAdjusted | — |
| AMOUNT_ADJUSTED | PaymentSchedulesLineAmountAdjusted | — |
| AMOUNT_ADJUSTED_PENDING | PaymentScheduleAmountAdjustedPending | — |
| AMOUNT_ADJUSTED_PENDING | PaymentSchedulesLineAmountAdjustedPending | — |
| AMOUNT_APPLIED | PaymentScheduleAmountApplied | — |
| AMOUNT_APPLIED | PaymentSchedulesLineAmountApplied | — |
| AMOUNT_CREDITED | PaymentScheduleAmountCredited | — |
| AMOUNT_CREDITED | PaymentSchedulesLineAmountCredited | — |
| AMOUNT_DUE_ORIGINAL | PaymentScheduleAmountDueOriginal | — |
| AMOUNT_DUE_ORIGINAL | PaymentSchedulesLineAmountDueOriginal | — |
| AMOUNT_DUE_REMAINING | PaymentScheduleAmountDueRemaining | — |
| AMOUNT_DUE_REMAINING | PaymentSchedulesLineAmountDueRemaining | — |
| AMOUNT_IN_DISPUTE | PaymentScheduleAmountInDispute | — |
| AMOUNT_IN_DISPUTE | PaymentSchedulesLineAmountInDispute | — |
| AMOUNT_LINE_ITEMS_ORIGINAL | PaymentScheduleAmountLineItemsOriginal | — |
| AMOUNT_LINE_ITEMS_ORIGINAL | PaymentSchedulesLineAmountLineItemsOriginal | — |
| AMOUNT_LINE_ITEMS_REMAINING | PaymentScheduleAmountLineItemsRemaining | — |
| AMOUNT_LINE_ITEMS_REMAINING | PaymentSchedulesLineAmountLineItemsRemaining | — |
| AMOUNT_ON_ACCOUNT | PaymentScheduleAmountOnAccount | — |
| AMOUNT_ON_ACCOUNT | PaymentSchedulesLineAmountOnAccount | — |
| AMOUNT_OTHER_ACCOUNT | PaymentScheduleAmountOtherAccount | — |
| AMOUNT_OTHER_ACCOUNT | PaymentSchedulesLineAmountOtherAccount | — |
| ASSOCIATED_CASH_RECEIPT_ID | PaymentScheduleAssociatedCashReceiptId | — |
| ASSOCIATED_CASH_RECEIPT_ID | PaymentSchedulesLineAssociatedCashReceiptId | — |
| BR_AMOUNT_ASSIGNED | PaymentScheduleBrAmountAssigned | — |
| BR_AMOUNT_ASSIGNED | PaymentSchedulesLineBrAmountAssigned | — |
| CALL_DATE_LAST | PaymentScheduleCallDateLast | — |
| CALL_DATE_LAST | PaymentSchedulesLineCallDateLast | — |
| CASH_APPLIED_AMOUNT_LAST | PaymentScheduleCashAppliedAmountLast | — |
| CASH_APPLIED_AMOUNT_LAST | PaymentSchedulesLineCashAppliedAmountLast | — |
| CASH_APPLIED_DATE_LAST | PaymentScheduleCashAppliedDateLast | — |
| CASH_APPLIED_DATE_LAST | PaymentSchedulesLineCashAppliedDateLast | — |
| CASH_APPLIED_ID_LAST | PaymentScheduleCashAppliedIdLast | — |
| CASH_APPLIED_ID_LAST | PaymentSchedulesLineCashAppliedIdLast | — |
| CASH_APPLIED_STATUS_LAST | PaymentScheduleCashAppliedStatusLast | — |
| CASH_APPLIED_STATUS_LAST | PaymentSchedulesLineCashAppliedStatusLast | — |
| CASH_GL_DATE_LAST | PaymentScheduleCashGlDateLast | — |
| CASH_GL_DATE_LAST | PaymentSchedulesLineCashGlDateLast | — |
| CASH_RECEIPT_AMOUNT_LAST | PaymentScheduleCashReceiptAmountLast | — |
| CASH_RECEIPT_AMOUNT_LAST | PaymentSchedulesLineCashReceiptAmountLast | — |
| CASH_RECEIPT_DATE_LAST | PaymentScheduleCashReceiptDateLast | — |
| CASH_RECEIPT_DATE_LAST | PaymentSchedulesLineCashReceiptDateLast | — |
| CASH_RECEIPT_ID | PaymentScheduleCashReceiptId | — |
| CASH_RECEIPT_ID | PaymentSchedulesLineCashReceiptId | — |
| CASH_RECEIPT_ID_LAST | PaymentScheduleCashReceiptIdLast | — |
| CASH_RECEIPT_ID_LAST | PaymentSchedulesLineCashReceiptIdLast | — |
| CASH_RECEIPT_STATUS_LAST | PaymentScheduleCashReceiptStatusLast | — |
| CASH_RECEIPT_STATUS_LAST | PaymentSchedulesLineCashReceiptStatusLast | — |
| CLASS | PaymentSchedulePaymentScheduleClass | — |
| CLASS | PaymentSchedulesLinePaymentScheduleClass | — |
| COLLECTOR_LAST | PaymentScheduleCollectorLast | — |
| COLLECTOR_LAST | PaymentSchedulesLineCollectorLast | — |
| CONS_INV_ID | PaymentScheduleConsInvId | — |
| CONS_INV_ID | PaymentSchedulesLineConsInvId | — |
| CONS_INV_ID_REV | PaymentScheduleConsInvIdRev | — |
| CONS_INV_ID_REV | PaymentSchedulesLineConsInvIdRev | — |
| CUST_TRX_TYPE_SEQ_ID | PaymentScheduleCustTrxTypeSeqId | — |
| CUST_TRX_TYPE_SEQ_ID | PaymentSchedulesLineCustTrxTypeSeqId | — |
| CUSTOMER_ID | PaymentScheduleCustomerId | — |
| CUSTOMER_ID | PaymentSchedulesLineCustomerId | — |
| CUSTOMER_SITE_USE_ID | PaymentScheduleCustomerSiteUseId | — |
| CUSTOMER_SITE_USE_ID | PaymentSchedulesLineCustomerSiteUseId | — |
| CUSTOMER_TRX_ID | PaymentScheduleCustomerTrxId | — |
| CUSTOMER_TRX_ID | PaymentSchedulesLineCustomerTrxId | — |
| DISCOUNT_DATE | PaymentScheduleDiscountDate | — |
| DISCOUNT_DATE | PaymentSchedulesLineDiscountDate | — |
| DISCOUNT_ORIGINAL | PaymentScheduleDiscountOriginal | — |
| DISCOUNT_ORIGINAL | PaymentSchedulesLineDiscountOriginal | — |
| DISCOUNT_REMAINING | PaymentScheduleDiscountRemaining | — |
| DISCOUNT_REMAINING | PaymentSchedulesLineDiscountRemaining | — |
| DISCOUNT_TAKEN_EARNED | PaymentScheduleDiscountTakenEarned | — |
| DISCOUNT_TAKEN_EARNED | PaymentSchedulesLineDiscountTakenEarned | — |
| DISCOUNT_TAKEN_UNEARNED | PaymentScheduleDiscountTakenUnearned | — |
| DISCOUNT_TAKEN_UNEARNED | PaymentSchedulesLineDiscountTakenUnearned | — |
| DISPUTE_DATE | PaymentScheduleDisputeDate | — |
| DISPUTE_DATE | PaymentSchedulesLineDisputeDate | — |
| DUE_DATE | PaymentScheduleDueDate | — |
| DUE_DATE | PaymentSchedulesLineDueDate | — |
| DUNNING_LEVEL_OVERRIDE_DATE | PaymentScheduleDunningLevelOverrideDate | — |
| DUNNING_LEVEL_OVERRIDE_DATE | PaymentSchedulesLineDunningLevelOverrideDate | — |
| EXCHANGE_DATE | PaymentScheduleExchangeDate | — |
| EXCHANGE_DATE | PaymentSchedulesLineExchangeDate | — |
| EXCHANGE_RATE | PaymentScheduleExchangeRate | — |
| EXCHANGE_RATE | PaymentSchedulesLineExchangeRate | — |
| EXCHANGE_RATE_TYPE | PaymentScheduleExchangeRateType | — |
| EXCHANGE_RATE_TYPE | PaymentSchedulesLineExchangeRateType | — |
| EXCLUDE_FROM_CONS_BILL_FLAG | PaymentScheduleExcludeFromConsBillFlag | — |
| EXCLUDE_FROM_CONS_BILL_FLAG | PaymentSchedulesLineExcludeFromConsBillFlag | — |
| EXCLUDE_FROM_DUNNING_FLAG | PaymentScheduleExcludeFromDunningFlag | — |
| EXCLUDE_FROM_DUNNING_FLAG | PaymentSchedulesLineExcludeFromDunningFlag | — |
| FOLLOW_UP_CODE_LAST | PaymentScheduleFollowUpCodeLast | — |
| FOLLOW_UP_CODE_LAST | PaymentSchedulesLineFollowUpCodeLast | — |
| FOLLOW_UP_DATE_LAST | PaymentScheduleFollowUpDateLast | — |
| FOLLOW_UP_DATE_LAST | PaymentSchedulesLineFollowUpDateLast | — |
| FREIGHT_ORIGINAL | PaymentScheduleFreightOriginal | — |
| FREIGHT_ORIGINAL | PaymentSchedulesLineFreightOriginal | — |
| FREIGHT_REMAINING | PaymentScheduleFreightRemaining | — |
| FREIGHT_REMAINING | PaymentSchedulesLineFreightRemaining | — |
| GL_DATE | PaymentScheduleGlDate | — |
| GL_DATE | PaymentSchedulesLineGlDate | — |
| GL_DATE_CLOSED | PaymentScheduleGlDateClosed | — |
| GL_DATE_CLOSED | PaymentSchedulesLineGlDateClosed | — |
| IN_COLLECTION | PaymentScheduleInCollection | — |
| IN_COLLECTION | PaymentSchedulesLineInCollection | — |
| INVOICE_CURRENCY_CODE | PaymentScheduleInvoiceCurrencyCode | — |
| INVOICE_CURRENCY_CODE | PaymentSchedulesLineInvoiceCurrencyCode | — |
| LAST_CHARGE_DATE | PaymentScheduleLastChargeDate | — |
| LAST_CHARGE_DATE | PaymentSchedulesLineLastChargeDate | — |
| NUMBER_OF_DUE_DATES | PaymentScheduleNumberOfDueDates | — |
| NUMBER_OF_DUE_DATES | PaymentSchedulesLineNumberOfDueDates | — |
| ORG_ID | PaymentScheduleOrgId | — |
| ORG_ID | PaymentSchedulesLineOrgId | — |
| PAYMENT_APPROVAL | PaymentSchedulePaymentApproval | — |
| PAYMENT_APPROVAL | PaymentSchedulesLinePaymentApproval | — |
| PAYMENT_SCHEDULE_ID | PaymentSchedulePaymentScheduleId | — |
| PAYMENT_SCHEDULE_ID | PaymentSchedulesLinePaymentScheduleId | — |
| PROGRAM_APPLICATION_ID | PaymentScheduleProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | PaymentSchedulesLineProgramApplicationId | — |
| PROGRAM_ID | PaymentScheduleProgramId | — |
| PROGRAM_ID | PaymentSchedulesLineProgramId | — |
| PROGRAM_UPDATE_DATE | PaymentScheduleProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | PaymentSchedulesLineProgramUpdateDate | — |
| PROMISE_AMOUNT_LAST | PaymentSchedulePromiseAmountLast | — |
| PROMISE_AMOUNT_LAST | PaymentSchedulesLinePromiseAmountLast | — |
| PROMISE_DATE_LAST | PaymentSchedulePromiseDateLast | — |
| PROMISE_DATE_LAST | PaymentSchedulesLinePromiseDateLast | — |
| RECEIPT_CONFIRMED_FLAG | PaymentScheduleReceiptConfirmedFlag | — |
| RECEIPT_CONFIRMED_FLAG | PaymentSchedulesLineReceiptConfirmedFlag | — |
| RECEIVABLES_CHARGES_CHARGED | PaymentScheduleReceivablesChargesCharged | — |
| RECEIVABLES_CHARGES_CHARGED | PaymentSchedulesLineReceivablesChargesCharged | — |
| RECEIVABLES_CHARGES_REMAINING | PaymentScheduleReceivablesChargesRemaining | — |
| RECEIVABLES_CHARGES_REMAINING | PaymentSchedulesLineReceivablesChargesRemaining | — |
| REQUEST_ID | PaymentScheduleRequestId | — |
| REQUEST_ID | PaymentSchedulesLineRequestId | — |
| RESERVED_TYPE | PaymentScheduleReservedType | — |
| RESERVED_TYPE | PaymentSchedulesLineReservedType | — |
| RESERVED_VALUE | PaymentScheduleReservedValue | — |
| RESERVED_VALUE | PaymentSchedulesLineReservedValue | — |
| REVERSED_CASH_RECEIPT_ID | PaymentScheduleReversedCashReceiptId | — |
| REVERSED_CASH_RECEIPT_ID | PaymentSchedulesLineReversedCashReceiptId | — |
| SECOND_LAST_CHARGE_DATE | PaymentScheduleSecondLastChargeDate | — |
| SECOND_LAST_CHARGE_DATE | PaymentSchedulesLineSecondLastChargeDate | — |
| SELECTED_FOR_RECEIPT_BATCH_ID | PaymentScheduleSelectedForReceiptBatchId | — |
| SELECTED_FOR_RECEIPT_BATCH_ID | PaymentSchedulesLineSelectedForReceiptBatchId | — |
| STAGED_DUNNING_LEVEL | PaymentScheduleStagedDunningLevel | — |
| STAGED_DUNNING_LEVEL | PaymentSchedulesLineStagedDunningLevel | — |
| STATUS | PaymentScheduleStatus | — |
| STATUS | PaymentSchedulesLineStatus | — |
| TAX_ORIGINAL | PaymentScheduleTaxOriginal | — |
| TAX_ORIGINAL | PaymentSchedulesLineTaxOriginal | — |
| TAX_REMAINING | PaymentScheduleTaxRemaining | — |
| TAX_REMAINING | PaymentSchedulesLineTaxRemaining | — |
| TERM_ID | PaymentScheduleTermId | — |
| TERM_ID | PaymentSchedulesLineTermId | — |
| TERMS_SEQUENCE_NUMBER | PaymentScheduleTermsSequenceNumber | — |
| TERMS_SEQUENCE_NUMBER | PaymentSchedulesLineTermsSequenceNumber | — |
| TRX_DATE | PaymentScheduleTrxDate | — |
| TRX_DATE | PaymentSchedulesLineTrxDate | — |
| TRX_NUMBER | PaymentScheduleTrxNumber | — |
| TRX_NUMBER | PaymentSchedulesLineTrxNumber | — |

### [[completedtrxrevenuedistributionpvo|CompletedTrxRevenueDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_DUE_REMAINING | PaymentSchedulesAcctdAmountDueRemaining | — |
| ACTIVE_CLAIM_FLAG | PaymentSchedulesActiveClaimFlag | — |
| ACTUAL_DATE_CLOSED | PaymentSchedulesActualDateClosed | — |
| ADJUSTMENT_AMOUNT_LAST | PaymentSchedulesAdjustmentAmountLast | — |
| ADJUSTMENT_DATE_LAST | PaymentSchedulesAdjustmentDateLast | — |
| ADJUSTMENT_GL_DATE_LAST | PaymentSchedulesAdjustmentGlDateLast | — |
| ADJUSTMENT_ID_LAST | PaymentSchedulesAdjustmentIdLast | — |
| AMOUNT_ADJUSTED | PaymentSchedulesAmountAdjusted | — |
| AMOUNT_ADJUSTED_PENDING | PaymentSchedulesAmountAdjustedPending | — |
| AMOUNT_APPLIED | PaymentSchedulesAmountApplied | — |
| AMOUNT_CREDITED | PaymentSchedulesAmountCredited | — |
| AMOUNT_DUE_ORIGINAL | PaymentSchedulesAmountDueOriginal | — |
| AMOUNT_DUE_REMAINING | PaymentSchedulesAmountDueRemaining | — |
| AMOUNT_IN_DISPUTE | PaymentSchedulesAmountInDispute | — |
| AMOUNT_LINE_ITEMS_ORIGINAL | PaymentSchedulesAmountLineItemsOriginal | — |
| AMOUNT_LINE_ITEMS_REMAINING | PaymentSchedulesAmountLineItemsRemaining | — |
| AMOUNT_ON_ACCOUNT | PaymentSchedulesAmountOnAccount | — |
| AMOUNT_OTHER_ACCOUNT | PaymentSchedulesAmountOtherAccount | — |
| ASSOCIATED_CASH_RECEIPT_ID | PaymentSchedulesAssociatedCashReceiptId | — |
| BR_AMOUNT_ASSIGNED | PaymentSchedulesBrAmountAssigned | — |
| CALL_DATE_LAST | PaymentSchedulesCallDateLast | — |
| CASH_APPLIED_AMOUNT_LAST | PaymentSchedulesCashAppliedAmountLast | — |
| CASH_APPLIED_DATE_LAST | PaymentSchedulesCashAppliedDateLast | — |
| CASH_APPLIED_ID_LAST | PaymentSchedulesCashAppliedIdLast | — |
| CASH_APPLIED_STATUS_LAST | PaymentSchedulesCashAppliedStatusLast | — |
| CASH_GL_DATE_LAST | PaymentSchedulesCashGlDateLast | — |
| CASH_RECEIPT_AMOUNT_LAST | PaymentSchedulesCashReceiptAmountLast | — |
| CASH_RECEIPT_DATE_LAST | PaymentSchedulesCashReceiptDateLast | — |
| CASH_RECEIPT_ID | PaymentSchedulesCashReceiptId | — |
| CASH_RECEIPT_ID_LAST | PaymentSchedulesCashReceiptIdLast | — |
| CASH_RECEIPT_STATUS_LAST | PaymentSchedulesCashReceiptStatusLast | — |
| CLASS | PaymentSchedulesPaymentScheduleClass | — |
| COLLECTOR_LAST | PaymentSchedulesCollectorLast | — |
| CONS_INV_ID | PaymentSchedulesConsInvId | — |
| CONS_INV_ID_REV | PaymentSchedulesConsInvIdRev | — |
| CUST_TRX_TYPE_SEQ_ID | PaymentSchedulesCustTrxTypeSeqId | — |
| CUSTOMER_ID | PaymentSchedulesCustomerId | — |
| CUSTOMER_SITE_USE_ID | PaymentSchedulesCustomerSiteUseId | — |
| CUSTOMER_TRX_ID | PaymentSchedulesCustomerTrxId | — |
| DISCOUNT_DATE | PaymentSchedulesDiscountDate | — |
| DISCOUNT_ORIGINAL | PaymentSchedulesDiscountOriginal | — |
| DISCOUNT_REMAINING | PaymentSchedulesDiscountRemaining | — |
| DISCOUNT_TAKEN_EARNED | PaymentSchedulesDiscountTakenEarned | — |
| DISCOUNT_TAKEN_UNEARNED | PaymentSchedulesDiscountTakenUnearned | — |
| DISPUTE_DATE | PaymentSchedulesDisputeDate | — |
| DUE_DATE | PaymentSchedulesDueDate | — |
| DUNNING_LEVEL_OVERRIDE_DATE | PaymentSchedulesDunningLevelOverrideDate | — |
| EXCHANGE_DATE | PaymentSchedulesExchangeDate | — |
| EXCHANGE_RATE | PaymentSchedulesExchangeRate | — |
| EXCHANGE_RATE_TYPE | PaymentSchedulesExchangeRateType | — |
| EXCLUDE_FROM_CONS_BILL_FLAG | PaymentSchedulesExcludeFromConsBillFlag | — |
| EXCLUDE_FROM_DUNNING_FLAG | PaymentSchedulesExcludeFromDunningFlag | — |
| FOLLOW_UP_CODE_LAST | PaymentSchedulesFollowUpCodeLast | — |
| FOLLOW_UP_DATE_LAST | PaymentSchedulesFollowUpDateLast | — |
| FREIGHT_ORIGINAL | PaymentSchedulesFreightOriginal | — |
| FREIGHT_REMAINING | PaymentSchedulesFreightRemaining | — |
| GL_DATE | PaymentSchedulesGlDate | — |
| GL_DATE_CLOSED | PaymentSchedulesGlDateClosed | — |
| IN_COLLECTION | PaymentSchedulesInCollection | — |
| INVOICE_CURRENCY_CODE | PaymentSchedulesInvoiceCurrencyCode | — |
| LAST_CHARGE_DATE | PaymentSchedulesLastChargeDate | — |
| NUMBER_OF_DUE_DATES | PaymentSchedulesNumberOfDueDates | — |
| ORG_ID | PaymentSchedulesOrgId | — |
| PAYMENT_APPROVAL | PaymentSchedulesPaymentApproval | — |
| PAYMENT_SCHEDULE_ID | PaymentSchedulesPaymentScheduleId | — |
| PROGRAM_APPLICATION_ID | PaymentSchedulesProgramApplicationId | — |
| PROGRAM_ID | PaymentSchedulesProgramId | — |
| PROGRAM_UPDATE_DATE | PaymentSchedulesProgramUpdateDate | — |
| PROMISE_AMOUNT_LAST | PaymentSchedulesPromiseAmountLast | — |
| PROMISE_DATE_LAST | PaymentSchedulesPromiseDateLast | — |
| RECEIPT_CONFIRMED_FLAG | PaymentSchedulesReceiptConfirmedFlag | — |
| RECEIVABLES_CHARGES_CHARGED | PaymentSchedulesReceivablesChargesCharged | — |
| RECEIVABLES_CHARGES_REMAINING | PaymentSchedulesReceivablesChargesRemaining | — |
| REQUEST_ID | PaymentSchedulesRequestId | — |
| RESERVED_TYPE | PaymentSchedulesReservedType | — |
| RESERVED_VALUE | PaymentSchedulesReservedValue | — |
| REVERSED_CASH_RECEIPT_ID | PaymentSchedulesReversedCashReceiptId | — |
| SECOND_LAST_CHARGE_DATE | PaymentSchedulesSecondLastChargeDate | — |
| SELECTED_FOR_RECEIPT_BATCH_ID | PaymentSchedulesSelectedForReceiptBatchId | — |
| STAGED_DUNNING_LEVEL | PaymentSchedulesStagedDunningLevel | — |
| STATUS | PaymentSchedulesStatus | — |
| TAX_ORIGINAL | PaymentSchedulesTaxOriginal | — |
| TAX_REMAINING | PaymentSchedulesTaxRemaining | — |
| TERM_ID | PaymentSchedulesTermId | — |
| TERMS_SEQUENCE_NUMBER | PaymentSchedulesTermsSequenceNumber | — |
| TRX_DATE | PaymentSchedulesTrxDate | — |
| TRX_NUMBER | PaymentSchedulesTrxNumber | — |

### [[creditmemoapplicationdistributionpvo|CreditMemoApplicationDistributionPVO]] (AR · BICC: 10/186)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_DUE_REMAINING | PaymentScheduleAcctdAmountDueRemaining | — |
| ACCTD_AMOUNT_DUE_REMAINING | PaymentScheduleAppliedAcctdAmountDueRemaining | — |
| ACTIVE_CLAIM_FLAG | PaymentScheduleActiveClaimFlag | — |
| ACTIVE_CLAIM_FLAG | PaymentScheduleAppliedActiveClaimFlag | — |
| ACTUAL_DATE_CLOSED | PaymentScheduleActualDateClosed | — |
| ACTUAL_DATE_CLOSED | PaymentScheduleAppliedActualDateClosed | — |
| ADJUSTMENT_AMOUNT_LAST | PaymentScheduleAdjustmentAmountLast | — |
| ADJUSTMENT_AMOUNT_LAST | PaymentScheduleAppliedAdjustmentAmountLast | — |
| ADJUSTMENT_DATE_LAST | PaymentScheduleAdjustmentDateLast | — |
| ADJUSTMENT_DATE_LAST | PaymentScheduleAppliedAdjustmentDateLast | — |
| ADJUSTMENT_GL_DATE_LAST | PaymentScheduleAdjustmentGlDateLast | — |
| ADJUSTMENT_GL_DATE_LAST | PaymentScheduleAppliedAdjustmentGlDateLast | — |
| ADJUSTMENT_ID_LAST | PaymentScheduleAdjustmentIdLast | — |
| ADJUSTMENT_ID_LAST | PaymentScheduleAppliedAdjustmentIdLast | — |
| AMOUNT_ADJUSTED | PaymentScheduleAmountAdjusted | — |
| AMOUNT_ADJUSTED | PaymentScheduleAppliedAmountAdjusted | — |
| AMOUNT_ADJUSTED_PENDING | PaymentScheduleAmountAdjustedPending | — |
| AMOUNT_ADJUSTED_PENDING | PaymentScheduleAppliedAmountAdjustedPending | — |
| AMOUNT_APPLIED | PaymentScheduleAmountApplied | — |
| AMOUNT_APPLIED | PaymentScheduleAppliedAmountApplied | — |
| AMOUNT_CREDITED | PaymentScheduleAmountCredited | — |
| AMOUNT_CREDITED | PaymentScheduleAppliedAmountCredited | — |
| AMOUNT_DUE_ORIGINAL | PaymentScheduleAmountDueOriginal | — |
| AMOUNT_DUE_ORIGINAL | PaymentScheduleAppliedAmountDueOriginal | — |
| AMOUNT_DUE_REMAINING | PaymentScheduleAmountDueRemaining | — |
| AMOUNT_DUE_REMAINING | PaymentScheduleAppliedAmountDueRemaining | — |
| AMOUNT_IN_DISPUTE | PaymentScheduleAmountInDispute | — |
| AMOUNT_IN_DISPUTE | PaymentScheduleAppliedAmountInDispute | — |
| AMOUNT_LINE_ITEMS_ORIGINAL | PaymentScheduleAmountLineItemsOriginal | — |
| AMOUNT_LINE_ITEMS_ORIGINAL | PaymentScheduleAppliedAmountLineItemsOriginal | — |
| AMOUNT_LINE_ITEMS_REMAINING | PaymentScheduleAmountLineItemsRemaining | — |
| AMOUNT_LINE_ITEMS_REMAINING | PaymentScheduleAppliedAmountLineItemsRemaining | — |
| AMOUNT_ON_ACCOUNT | PaymentScheduleAmountOnAccount | — |
| AMOUNT_ON_ACCOUNT | PaymentScheduleAppliedAmountOnAccount | — |
| AMOUNT_OTHER_ACCOUNT | PaymentScheduleAmountOtherAccount | — |
| AMOUNT_OTHER_ACCOUNT | PaymentScheduleAppliedAmountOtherAccount | — |
| ASSOCIATED_CASH_RECEIPT_ID | PaymentScheduleAppliedAssociatedCashReceiptId | — |
| ASSOCIATED_CASH_RECEIPT_ID | PaymentScheduleAssociatedCashReceiptId | — |
| BR_AMOUNT_ASSIGNED | PaymentScheduleAppliedBrAmountAssigned | — |
| BR_AMOUNT_ASSIGNED | PaymentScheduleBrAmountAssigned | — |
| CALL_DATE_LAST | PaymentScheduleAppliedCallDateLast | — |
| CALL_DATE_LAST | PaymentScheduleCallDateLast | — |
| CASH_APPLIED_AMOUNT_LAST | PaymentScheduleAppliedCashAppliedAmountLast | — |
| CASH_APPLIED_AMOUNT_LAST | PaymentScheduleCashAppliedAmountLast | — |
| CASH_APPLIED_DATE_LAST | PaymentScheduleAppliedCashAppliedDateLast | — |
| CASH_APPLIED_DATE_LAST | PaymentScheduleCashAppliedDateLast | — |
| CASH_APPLIED_ID_LAST | PaymentScheduleAppliedCashAppliedIdLast | — |
| CASH_APPLIED_ID_LAST | PaymentScheduleCashAppliedIdLast | — |
| CASH_APPLIED_STATUS_LAST | PaymentScheduleAppliedCashAppliedStatusLast | — |
| CASH_APPLIED_STATUS_LAST | PaymentScheduleCashAppliedStatusLast | — |
| CASH_GL_DATE_LAST | PaymentScheduleAppliedCashGlDateLast | — |
| CASH_GL_DATE_LAST | PaymentScheduleCashGlDateLast | — |
| CASH_RECEIPT_AMOUNT_LAST | PaymentScheduleAppliedCashReceiptAmountLast | — |
| CASH_RECEIPT_AMOUNT_LAST | PaymentScheduleCashReceiptAmountLast | — |
| CASH_RECEIPT_DATE_LAST | PaymentScheduleAppliedCashReceiptDateLast | — |
| CASH_RECEIPT_DATE_LAST | PaymentScheduleCashReceiptDateLast | — |
| CASH_RECEIPT_ID | PaymentScheduleAppliedCashReceiptId | — |
| CASH_RECEIPT_ID | PaymentScheduleCashReceiptId | — |
| CASH_RECEIPT_ID_LAST | PaymentScheduleAppliedCashReceiptIdLast | — |
| CASH_RECEIPT_ID_LAST | PaymentScheduleCashReceiptIdLast | — |
| CASH_RECEIPT_STATUS_LAST | PaymentScheduleAppliedCashReceiptStatusLast | — |
| CASH_RECEIPT_STATUS_LAST | PaymentScheduleCashReceiptStatusLast | — |
| CLASS | PaymentScheduleAppliedPaymentScheduleClass | — |
| CLASS | PaymentSchedulePaymentScheduleClass | — |
| COLLECTOR_LAST | PaymentScheduleAppliedCollectorLast | — |
| COLLECTOR_LAST | PaymentScheduleCollectorLast | — |
| CONS_INV_ID | PaymentScheduleAppliedConsInvId | — |
| CONS_INV_ID | PaymentScheduleConsInvId | — |
| CONS_INV_ID_REV | PaymentScheduleAppliedConsInvIdRev | — |
| CONS_INV_ID_REV | PaymentScheduleConsInvIdRev | — |
| CREATED_BY | PaymentScheduleAppliedCreatedBy | — |
| CREATED_BY | PaymentScheduleCreatedBy | — |
| CREATION_DATE | PaymentScheduleAppliedCreationDate | — |
| CREATION_DATE | PaymentScheduleCreationDate | — |
| CUST_TRX_TYPE_SEQ_ID | PaymentScheduleAppliedCustTrxTypeSeqId | — |
| CUST_TRX_TYPE_SEQ_ID | PaymentScheduleCustTrxTypeSeqId | — |
| CUSTOMER_ID | PaymentScheduleAppliedCustomerId | — |
| CUSTOMER_ID | PaymentScheduleCustomerId | — |
| CUSTOMER_SITE_USE_ID | PaymentScheduleAppliedCustomerSiteUseId | ✅ |
| CUSTOMER_SITE_USE_ID | PaymentScheduleCustomerSiteUseId | — |
| CUSTOMER_TRX_ID | PaymentScheduleAppliedCustomerTrxId | — |
| CUSTOMER_TRX_ID | PaymentScheduleCustomerTrxId | — |
| DISCOUNT_DATE | PaymentScheduleAppliedDiscountDate | — |
| DISCOUNT_DATE | PaymentScheduleDiscountDate | — |
| DISCOUNT_ORIGINAL | PaymentScheduleAppliedDiscountOriginal | — |
| DISCOUNT_ORIGINAL | PaymentScheduleDiscountOriginal | — |
| DISCOUNT_REMAINING | PaymentScheduleAppliedDiscountRemaining | — |
| DISCOUNT_REMAINING | PaymentScheduleDiscountRemaining | — |
| DISCOUNT_TAKEN_EARNED | PaymentScheduleAppliedDiscountTakenEarned | — |
| DISCOUNT_TAKEN_EARNED | PaymentScheduleDiscountTakenEarned | — |
| DISCOUNT_TAKEN_UNEARNED | PaymentScheduleAppliedDiscountTakenUnearned | — |
| DISCOUNT_TAKEN_UNEARNED | PaymentScheduleDiscountTakenUnearned | — |
| DISPUTE_DATE | PaymentScheduleAppliedDisputeDate | — |
| DISPUTE_DATE | PaymentScheduleDisputeDate | — |
| DUE_DATE | PaymentScheduleAppliedDueDate | ✅ |
| DUE_DATE | PaymentScheduleDueDate | ✅ |
| DUNNING_LEVEL_OVERRIDE_DATE | PaymentScheduleAppliedDunningLevelOverrideDate | — |
| DUNNING_LEVEL_OVERRIDE_DATE | PaymentScheduleDunningLevelOverrideDate | — |
| EXCHANGE_DATE | PaymentScheduleAppliedExchangeDate | — |
| EXCHANGE_DATE | PaymentScheduleExchangeDate | — |
| EXCHANGE_RATE | PaymentScheduleAppliedExchangeRate | — |
| EXCHANGE_RATE | PaymentScheduleExchangeRate | — |
| EXCHANGE_RATE_TYPE | PaymentScheduleAppliedExchangeRateType | — |
| EXCHANGE_RATE_TYPE | PaymentScheduleExchangeRateType | — |
| EXCLUDE_FROM_CONS_BILL_FLAG | PaymentScheduleAppliedExcludeFromConsBillFlag | — |
| EXCLUDE_FROM_CONS_BILL_FLAG | PaymentScheduleExcludeFromConsBillFlag | — |
| EXCLUDE_FROM_DUNNING_FLAG | PaymentScheduleAppliedExcludeFromDunningFlag | — |
| EXCLUDE_FROM_DUNNING_FLAG | PaymentScheduleExcludeFromDunningFlag | — |
| FOLLOW_UP_CODE_LAST | PaymentScheduleAppliedFollowUpCodeLast | — |
| FOLLOW_UP_CODE_LAST | PaymentScheduleFollowUpCodeLast | — |
| FOLLOW_UP_DATE_LAST | PaymentScheduleAppliedFollowUpDateLast | — |
| FOLLOW_UP_DATE_LAST | PaymentScheduleFollowUpDateLast | — |
| FREIGHT_ORIGINAL | PaymentScheduleAppliedFreightOriginal | — |
| FREIGHT_ORIGINAL | PaymentScheduleFreightOriginal | — |
| FREIGHT_REMAINING | PaymentScheduleAppliedFreightRemaining | — |
| FREIGHT_REMAINING | PaymentScheduleFreightRemaining | — |
| GL_DATE | PaymentScheduleAppliedGlDate | — |
| GL_DATE | PaymentScheduleGlDate | — |
| GL_DATE_CLOSED | PaymentScheduleAppliedGlDateClosed | — |
| GL_DATE_CLOSED | PaymentScheduleGlDateClosed | — |
| IN_COLLECTION | PaymentScheduleAppliedInCollection | — |
| IN_COLLECTION | PaymentScheduleInCollection | — |
| INVOICE_CURRENCY_CODE | PaymentScheduleAppliedInvoiceCurrencyCode | — |
| INVOICE_CURRENCY_CODE | PaymentScheduleInvoiceCurrencyCode | — |
| LAST_CHARGE_DATE | PaymentScheduleAppliedLastChargeDate | — |
| LAST_CHARGE_DATE | PaymentScheduleLastChargeDate | — |
| LAST_UPDATE_DATE | PaymentScheduleAppliedLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | PaymentScheduleLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PaymentScheduleAppliedLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | PaymentScheduleLastUpdateLogin | — |
| LAST_UPDATED_BY | PaymentScheduleAppliedLastUpdatedBy | — |
| LAST_UPDATED_BY | PaymentScheduleLastUpdatedBy | — |
| NUMBER_OF_DUE_DATES | PaymentScheduleAppliedNumberOfDueDates | — |
| NUMBER_OF_DUE_DATES | PaymentScheduleNumberOfDueDates | — |
| OBJECT_VERSION_NUMBER | PaymentScheduleAppliedObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | PaymentScheduleObjectVersionNumber | — |
| ORG_ID | PaymentScheduleAppliedOrgId | — |
| ORG_ID | PaymentScheduleOrgId | — |
| PAYMENT_APPROVAL | PaymentScheduleAppliedPaymentApproval | — |
| PAYMENT_APPROVAL | PaymentSchedulePaymentApproval | — |
| PAYMENT_SCHEDULE_ID | PaymentScheduleAppliedPaymentScheduleId | ✅ |
| PAYMENT_SCHEDULE_ID | PaymentSchedulePaymentScheduleId | ✅ |
| PROGRAM_APPLICATION_ID | PaymentScheduleAppliedProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | PaymentScheduleProgramApplicationId | — |
| PROGRAM_ID | PaymentScheduleAppliedProgramId | — |
| PROGRAM_ID | PaymentScheduleProgramId | — |
| PROGRAM_UPDATE_DATE | PaymentScheduleAppliedProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | PaymentScheduleProgramUpdateDate | — |
| PROMISE_AMOUNT_LAST | PaymentScheduleAppliedPromiseAmountLast | — |
| PROMISE_AMOUNT_LAST | PaymentSchedulePromiseAmountLast | — |
| PROMISE_DATE_LAST | PaymentScheduleAppliedPromiseDateLast | — |
| PROMISE_DATE_LAST | PaymentSchedulePromiseDateLast | — |
| RECEIPT_CONFIRMED_FLAG | PaymentScheduleAppliedReceiptConfirmedFlag | — |
| RECEIPT_CONFIRMED_FLAG | PaymentScheduleReceiptConfirmedFlag | — |
| RECEIVABLES_CHARGES_CHARGED | PaymentScheduleAppliedReceivablesChargesCharged | — |
| RECEIVABLES_CHARGES_CHARGED | PaymentScheduleReceivablesChargesCharged | — |
| RECEIVABLES_CHARGES_REMAINING | PaymentScheduleAppliedReceivablesChargesRemaining | — |
| RECEIVABLES_CHARGES_REMAINING | PaymentScheduleReceivablesChargesRemaining | — |
| REQUEST_ID | PaymentScheduleAppliedRequestId | — |
| REQUEST_ID | PaymentScheduleRequestId | — |
| RESERVED_TYPE | PaymentScheduleAppliedReservedType | — |
| RESERVED_TYPE | PaymentScheduleReservedType | — |
| RESERVED_VALUE | PaymentScheduleAppliedReservedValue | — |
| RESERVED_VALUE | PaymentScheduleReservedValue | — |
| REVERSED_CASH_RECEIPT_ID | PaymentScheduleAppliedReversedCashReceiptId | — |
| REVERSED_CASH_RECEIPT_ID | PaymentScheduleReversedCashReceiptId | — |
| SECOND_LAST_CHARGE_DATE | PaymentScheduleAppliedSecondLastChargeDate | — |
| SECOND_LAST_CHARGE_DATE | PaymentScheduleSecondLastChargeDate | — |
| SELECTED_FOR_RECEIPT_BATCH_ID | PaymentScheduleAppliedSelectedForReceiptBatchId | — |
| SELECTED_FOR_RECEIPT_BATCH_ID | PaymentScheduleSelectedForReceiptBatchId | — |
| STAGED_DUNNING_LEVEL | PaymentScheduleAppliedStagedDunningLevel | — |
| STAGED_DUNNING_LEVEL | PaymentScheduleStagedDunningLevel | — |
| STATUS | PaymentScheduleAppliedStatus | ✅ |
| STATUS | PaymentScheduleStatus | ✅ |
| TAX_ORIGINAL | PaymentScheduleAppliedTaxOriginal | — |
| TAX_ORIGINAL | PaymentScheduleTaxOriginal | — |
| TAX_REMAINING | PaymentScheduleAppliedTaxRemaining | — |
| TAX_REMAINING | PaymentScheduleTaxRemaining | — |
| TERM_ID | PaymentScheduleAppliedTermId | — |
| TERM_ID | PaymentScheduleTermId | — |
| TERMS_SEQUENCE_NUMBER | PaymentScheduleAppliedTermsSequenceNumber | ✅ |
| TERMS_SEQUENCE_NUMBER | PaymentScheduleTermsSequenceNumber | — |
| TRX_DATE | PaymentScheduleAppliedTrxDate | — |
| TRX_DATE | PaymentScheduleTrxDate | — |
| TRX_NUMBER | PaymentScheduleAppliedTrxNumber | — |
| TRX_NUMBER | PaymentScheduleTrxNumber | — |

### [[creditmemoapplicationpvo|CreditMemoApplicationPVO]] (AR · BICC: 2/93)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_DUE_REMAINING | PaymentScheduleAppliedAcctdAmountDueRemaining | — |
| ACTIVE_CLAIM_FLAG | PaymentScheduleAppliedActiveClaimFlag | — |
| ACTUAL_DATE_CLOSED | PaymentScheduleAppliedActualDateClosed | — |
| ADJUSTMENT_AMOUNT_LAST | PaymentScheduleAppliedAdjustmentAmountLast | — |
| ADJUSTMENT_DATE_LAST | PaymentScheduleAppliedAdjustmentDateLast | — |
| ADJUSTMENT_GL_DATE_LAST | PaymentScheduleAppliedAdjustmentGlDateLast | — |
| ADJUSTMENT_ID_LAST | PaymentScheduleAppliedAdjustmentIdLast | — |
| AMOUNT_ADJUSTED | PaymentScheduleAppliedAmountAdjusted | — |
| AMOUNT_ADJUSTED_PENDING | PaymentScheduleAppliedAmountAdjustedPending | — |
| AMOUNT_APPLIED | PaymentScheduleAppliedAmountApplied | — |
| AMOUNT_CREDITED | PaymentScheduleAppliedAmountCredited | — |
| AMOUNT_DUE_ORIGINAL | PaymentScheduleAppliedAmountDueOriginal | — |
| AMOUNT_DUE_REMAINING | PaymentScheduleAppliedAmountDueRemaining | — |
| AMOUNT_IN_DISPUTE | PaymentScheduleAppliedAmountInDispute | — |
| AMOUNT_LINE_ITEMS_ORIGINAL | PaymentScheduleAppliedAmountLineItemsOriginal | — |
| AMOUNT_LINE_ITEMS_REMAINING | PaymentScheduleAppliedAmountLineItemsRemaining | — |
| AMOUNT_ON_ACCOUNT | PaymentScheduleAppliedAmountOnAccount | — |
| AMOUNT_OTHER_ACCOUNT | PaymentScheduleAppliedAmountOtherAccount | — |
| ASSOCIATED_CASH_RECEIPT_ID | PaymentScheduleAppliedAssociatedCashReceiptId | — |
| BR_AMOUNT_ASSIGNED | PaymentScheduleAppliedBrAmountAssigned | — |
| CALL_DATE_LAST | PaymentScheduleAppliedCallDateLast | — |
| CASH_APPLIED_AMOUNT_LAST | PaymentScheduleAppliedCashAppliedAmountLast | — |
| CASH_APPLIED_DATE_LAST | PaymentScheduleAppliedCashAppliedDateLast | — |
| CASH_APPLIED_ID_LAST | PaymentScheduleAppliedCashAppliedIdLast | — |
| CASH_APPLIED_STATUS_LAST | PaymentScheduleAppliedCashAppliedStatusLast | — |
| CASH_GL_DATE_LAST | PaymentScheduleAppliedCashGlDateLast | — |
| CASH_RECEIPT_AMOUNT_LAST | PaymentScheduleAppliedCashReceiptAmountLast | — |
| CASH_RECEIPT_DATE_LAST | PaymentScheduleAppliedCashReceiptDateLast | — |
| CASH_RECEIPT_ID | PaymentScheduleAppliedCashReceiptId | — |
| CASH_RECEIPT_ID_LAST | PaymentScheduleAppliedCashReceiptIdLast | — |
| CASH_RECEIPT_STATUS_LAST | PaymentScheduleAppliedCashReceiptStatusLast | — |
| CLASS | PaymentScheduleAppliedPaymentScheduleClass | — |
| COLLECTOR_LAST | PaymentScheduleAppliedCollectorLast | — |
| CONS_INV_ID | PaymentScheduleAppliedConsInvId | — |
| CONS_INV_ID_REV | PaymentScheduleAppliedConsInvIdRev | — |
| CREATED_BY | PaymentScheduleAppliedCreatedBy | — |
| CREATION_DATE | PaymentScheduleAppliedCreationDate | — |
| CUST_TRX_TYPE_SEQ_ID | PaymentScheduleAppliedCustTrxTypeSeqId | — |
| CUSTOMER_ID | PaymentScheduleAppliedCustomerId | — |
| CUSTOMER_SITE_USE_ID | PaymentScheduleAppliedCustomerSiteUseId | — |
| CUSTOMER_TRX_ID | PaymentScheduleAppliedCustomerTrxId | — |
| DISCOUNT_DATE | PaymentScheduleAppliedDiscountDate | — |
| DISCOUNT_ORIGINAL | PaymentScheduleAppliedDiscountOriginal | — |
| DISCOUNT_REMAINING | PaymentScheduleAppliedDiscountRemaining | — |
| DISCOUNT_TAKEN_EARNED | PaymentScheduleAppliedDiscountTakenEarned | — |
| DISCOUNT_TAKEN_UNEARNED | PaymentScheduleAppliedDiscountTakenUnearned | — |
| DISPUTE_DATE | PaymentScheduleAppliedDisputeDate | — |
| DUE_DATE | PaymentScheduleAppliedDueDate | ✅ |
| DUNNING_LEVEL_OVERRIDE_DATE | PaymentScheduleAppliedDunningLevelOverrideDate | — |
| EXCHANGE_DATE | PaymentScheduleAppliedExchangeDate | — |
| EXCHANGE_RATE | PaymentScheduleAppliedExchangeRate | — |
| EXCHANGE_RATE_TYPE | PaymentScheduleAppliedExchangeRateType | — |
| EXCLUDE_FROM_CONS_BILL_FLAG | PaymentScheduleAppliedExcludeFromConsBillFlag | — |
| EXCLUDE_FROM_DUNNING_FLAG | PaymentScheduleAppliedExcludeFromDunningFlag | — |
| FOLLOW_UP_CODE_LAST | PaymentScheduleAppliedFollowUpCodeLast | — |
| FOLLOW_UP_DATE_LAST | PaymentScheduleAppliedFollowUpDateLast | — |
| FREIGHT_ORIGINAL | PaymentScheduleAppliedFreightOriginal | — |
| FREIGHT_REMAINING | PaymentScheduleAppliedFreightRemaining | — |
| GL_DATE | PaymentScheduleAppliedGlDate | — |
| GL_DATE_CLOSED | PaymentScheduleAppliedGlDateClosed | — |
| IN_COLLECTION | PaymentScheduleAppliedInCollection | — |
| INVOICE_CURRENCY_CODE | PaymentScheduleAppliedInvoiceCurrencyCode | — |
| LAST_CHARGE_DATE | PaymentScheduleAppliedLastChargeDate | — |
| LAST_UPDATE_DATE | PaymentScheduleAppliedLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PaymentScheduleAppliedLastUpdateLogin | — |
| LAST_UPDATED_BY | PaymentScheduleAppliedLastUpdatedBy | — |
| NUMBER_OF_DUE_DATES | PaymentScheduleAppliedNumberOfDueDates | — |
| OBJECT_VERSION_NUMBER | PaymentScheduleAppliedObjectVersionNumber | — |
| ORG_ID | PaymentScheduleAppliedOrgId | — |
| PAYMENT_APPROVAL | PaymentScheduleAppliedPaymentApproval | — |
| PAYMENT_SCHEDULE_ID | PaymentScheduleAppliedPaymentScheduleId | — |
| PROGRAM_APPLICATION_ID | PaymentScheduleAppliedProgramApplicationId | — |
| PROGRAM_ID | PaymentScheduleAppliedProgramId | — |
| PROGRAM_UPDATE_DATE | PaymentScheduleAppliedProgramUpdateDate | — |
| PROMISE_AMOUNT_LAST | PaymentScheduleAppliedPromiseAmountLast | — |
| PROMISE_DATE_LAST | PaymentScheduleAppliedPromiseDateLast | — |
| RECEIPT_CONFIRMED_FLAG | PaymentScheduleAppliedReceiptConfirmedFlag | — |
| RECEIVABLES_CHARGES_CHARGED | PaymentScheduleAppliedReceivablesChargesCharged | — |
| RECEIVABLES_CHARGES_REMAINING | PaymentScheduleAppliedReceivablesChargesRemaining | — |
| REQUEST_ID | PaymentScheduleAppliedRequestId | — |
| RESERVED_TYPE | PaymentScheduleAppliedReservedType | — |
| RESERVED_VALUE | PaymentScheduleAppliedReservedValue | — |
| REVERSED_CASH_RECEIPT_ID | PaymentScheduleAppliedReversedCashReceiptId | — |
| SECOND_LAST_CHARGE_DATE | PaymentScheduleAppliedSecondLastChargeDate | — |
| SELECTED_FOR_RECEIPT_BATCH_ID | PaymentScheduleAppliedSelectedForReceiptBatchId | — |
| STAGED_DUNNING_LEVEL | PaymentScheduleAppliedStagedDunningLevel | — |
| STATUS | PaymentScheduleAppliedStatus | — |
| TAX_ORIGINAL | PaymentScheduleAppliedTaxOriginal | — |
| TAX_REMAINING | PaymentScheduleAppliedTaxRemaining | — |
| TERM_ID | PaymentScheduleAppliedTermId | — |
| TERMS_SEQUENCE_NUMBER | PaymentScheduleAppliedTermsSequenceNumber | — |
| TRX_DATE | PaymentScheduleAppliedTrxDate | — |
| TRX_NUMBER | PaymentScheduleAppliedTrxNumber | — |

### [[disputehistorypvo|DisputeHistoryPVO]] (AR · BICC: 1/1)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| PAYMENT_SCHEDULE_ID | PaymentSchedulePaymentScheduleId | ✅ |

### [[linesalescreditpvo|LineSalesCreditPVO]] (AR · BICC: 1/93)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_DUE_REMAINING | PaymentSchedulesAcctdAmountDueRemaining | — |
| ACTIVE_CLAIM_FLAG | PaymentSchedulesActiveClaimFlag | — |
| ACTUAL_DATE_CLOSED | PaymentSchedulesActualDateClosed | — |
| ADJUSTMENT_AMOUNT_LAST | PaymentSchedulesAdjustmentAmountLast | — |
| ADJUSTMENT_DATE_LAST | PaymentSchedulesAdjustmentDateLast | — |
| ADJUSTMENT_GL_DATE_LAST | PaymentSchedulesAdjustmentGlDateLast | — |
| ADJUSTMENT_ID_LAST | PaymentSchedulesAdjustmentIdLast | — |
| AMOUNT_ADJUSTED | PaymentSchedulesAmountAdjusted | — |
| AMOUNT_ADJUSTED_PENDING | PaymentSchedulesAmountAdjustedPending | — |
| AMOUNT_APPLIED | PaymentSchedulesAmountApplied | — |
| AMOUNT_CREDITED | PaymentSchedulesAmountCredited | — |
| AMOUNT_DUE_ORIGINAL | PaymentSchedulesAmountDueOriginal | — |
| AMOUNT_DUE_REMAINING | PaymentSchedulesAmountDueRemaining | — |
| AMOUNT_IN_DISPUTE | PaymentSchedulesAmountInDispute | — |
| AMOUNT_LINE_ITEMS_ORIGINAL | PaymentSchedulesAmountLineItemsOriginal | — |
| AMOUNT_LINE_ITEMS_REMAINING | PaymentSchedulesAmountLineItemsRemaining | — |
| AMOUNT_ON_ACCOUNT | PaymentSchedulesAmountOnAccount | — |
| AMOUNT_OTHER_ACCOUNT | PaymentSchedulesAmountOtherAccount | — |
| ASSOCIATED_CASH_RECEIPT_ID | PaymentSchedulesAssociatedCashReceiptId | — |
| BR_AMOUNT_ASSIGNED | PaymentSchedulesBrAmountAssigned | — |
| CALL_DATE_LAST | PaymentSchedulesCallDateLast | — |
| CASH_APPLIED_AMOUNT_LAST | PaymentSchedulesCashAppliedAmountLast | — |
| CASH_APPLIED_DATE_LAST | PaymentSchedulesCashAppliedDateLast | — |
| CASH_APPLIED_ID_LAST | PaymentSchedulesCashAppliedIdLast | — |
| CASH_APPLIED_STATUS_LAST | PaymentSchedulesCashAppliedStatusLast | — |
| CASH_GL_DATE_LAST | PaymentSchedulesCashGlDateLast | — |
| CASH_RECEIPT_AMOUNT_LAST | PaymentSchedulesCashReceiptAmountLast | — |
| CASH_RECEIPT_DATE_LAST | PaymentSchedulesCashReceiptDateLast | — |
| CASH_RECEIPT_ID | PaymentSchedulesCashReceiptId | — |
| CASH_RECEIPT_ID_LAST | PaymentSchedulesCashReceiptIdLast | — |
| CASH_RECEIPT_STATUS_LAST | PaymentSchedulesCashReceiptStatusLast | — |
| CLASS | PaymentSchedulesPaymentScheduleClass | — |
| COLLECTOR_LAST | PaymentSchedulesCollectorLast | — |
| CONS_INV_ID | PaymentSchedulesConsInvId | — |
| CONS_INV_ID_REV | PaymentSchedulesConsInvIdRev | — |
| CREATED_BY | PaymentSchedulesCreatedBy | — |
| CREATION_DATE | PaymentSchedulesCreationDate | — |
| CUST_TRX_TYPE_SEQ_ID | PaymentSchedulesCustTrxTypeSeqId | — |
| CUSTOMER_ID | PaymentSchedulesCustomerId | — |
| CUSTOMER_SITE_USE_ID | PaymentSchedulesCustomerSiteUseId | — |
| CUSTOMER_TRX_ID | PaymentSchedulesCustomerTrxId | — |
| DISCOUNT_DATE | PaymentSchedulesDiscountDate | — |
| DISCOUNT_ORIGINAL | PaymentSchedulesDiscountOriginal | — |
| DISCOUNT_REMAINING | PaymentSchedulesDiscountRemaining | — |
| DISCOUNT_TAKEN_EARNED | PaymentSchedulesDiscountTakenEarned | — |
| DISCOUNT_TAKEN_UNEARNED | PaymentSchedulesDiscountTakenUnearned | — |
| DISPUTE_DATE | PaymentSchedulesDisputeDate | — |
| DUE_DATE | PaymentSchedulesDueDate | — |
| DUNNING_LEVEL_OVERRIDE_DATE | PaymentSchedulesDunningLevelOverrideDate | — |
| EXCHANGE_DATE | PaymentSchedulesExchangeDate | — |
| EXCHANGE_RATE | PaymentSchedulesExchangeRate | — |
| EXCHANGE_RATE_TYPE | PaymentSchedulesExchangeRateType | — |
| EXCLUDE_FROM_CONS_BILL_FLAG | PaymentSchedulesExcludeFromConsBillFlag | — |
| EXCLUDE_FROM_DUNNING_FLAG | PaymentSchedulesExcludeFromDunningFlag | — |
| FOLLOW_UP_CODE_LAST | PaymentSchedulesFollowUpCodeLast | — |
| FOLLOW_UP_DATE_LAST | PaymentSchedulesFollowUpDateLast | — |
| FREIGHT_ORIGINAL | PaymentSchedulesFreightOriginal | — |
| FREIGHT_REMAINING | PaymentSchedulesFreightRemaining | — |
| GL_DATE | PaymentSchedulesGlDate | — |
| GL_DATE_CLOSED | PaymentSchedulesGlDateClosed | — |
| IN_COLLECTION | PaymentSchedulesInCollection | — |
| INVOICE_CURRENCY_CODE | PaymentSchedulesInvoiceCurrencyCode | — |
| LAST_CHARGE_DATE | PaymentSchedulesLastChargeDate | — |
| LAST_UPDATE_DATE | PaymentSchedulesLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PaymentSchedulesLastUpdateLogin | — |
| LAST_UPDATED_BY | PaymentSchedulesLastUpdatedBy | — |
| NUMBER_OF_DUE_DATES | PaymentSchedulesNumberOfDueDates | — |
| OBJECT_VERSION_NUMBER | PaymentSchedulesObjectVersionNumber | — |
| ORG_ID | PaymentSchedulesOrgId | — |
| PAYMENT_APPROVAL | PaymentSchedulesPaymentApproval | — |
| PAYMENT_SCHEDULE_ID | PaymentSchedulesPaymentScheduleId | — |
| PROGRAM_APPLICATION_ID | PaymentSchedulesProgramApplicationId | — |
| PROGRAM_ID | PaymentSchedulesProgramId | — |
| PROGRAM_UPDATE_DATE | PaymentSchedulesProgramUpdateDate | — |
| PROMISE_AMOUNT_LAST | PaymentSchedulesPromiseAmountLast | — |
| PROMISE_DATE_LAST | PaymentSchedulesPromiseDateLast | — |
| RECEIPT_CONFIRMED_FLAG | PaymentSchedulesReceiptConfirmedFlag | — |
| RECEIVABLES_CHARGES_CHARGED | PaymentSchedulesReceivablesChargesCharged | — |
| RECEIVABLES_CHARGES_REMAINING | PaymentSchedulesReceivablesChargesRemaining | — |
| REQUEST_ID | PaymentSchedulesRequestId | — |
| RESERVED_TYPE | PaymentSchedulesReservedType | — |
| RESERVED_VALUE | PaymentSchedulesReservedValue | — |
| REVERSED_CASH_RECEIPT_ID | PaymentSchedulesReversedCashReceiptId | — |
| SECOND_LAST_CHARGE_DATE | PaymentSchedulesSecondLastChargeDate | — |
| SELECTED_FOR_RECEIPT_BATCH_ID | PaymentSchedulesSelectedForReceiptBatchId | — |
| STAGED_DUNNING_LEVEL | PaymentSchedulesStagedDunningLevel | — |
| STATUS | PaymentSchedulesStatus | — |
| TAX_ORIGINAL | PaymentSchedulesTaxOriginal | — |
| TAX_REMAINING | PaymentSchedulesTaxRemaining | — |
| TERM_ID | PaymentSchedulesTermId | — |
| TERMS_SEQUENCE_NUMBER | PaymentSchedulesTermsSequenceNumber | — |
| TRX_DATE | PaymentSchedulesTrxDate | — |
| TRX_NUMBER | PaymentSchedulesTrxNumber | — |

### [[paymentscheduleextractpvo|PaymentScheduleExtractPVO]] (OTHER · BICC: 80/127)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_DUE_REMAINING | ArPaymentScheduleAcctdAmountDueRemaining | ✅ |
| ACTIVE_CLAIM_FLAG | ArPaymentScheduleActiveClaimFlag | ✅ |
| ACTUAL_DATE_CLOSED | ArPaymentScheduleActualDateClosed | ✅ |
| AMOUNT_ADJUSTED | ArPaymentScheduleAmountAdjusted | ✅ |
| AMOUNT_ADJUSTED_PENDING | ArPaymentScheduleAmountAdjustedPending | ✅ |
| AMOUNT_APPLIED | ArPaymentScheduleAmountApplied | ✅ |
| AMOUNT_CREDITED | ArPaymentScheduleAmountCredited | ✅ |
| AMOUNT_DUE_ORIGINAL | ArPaymentScheduleAmountDueOriginal | ✅ |
| AMOUNT_DUE_REMAINING | ArPaymentScheduleAmountDueRemaining | ✅ |
| AMOUNT_IN_DISPUTE | ArPaymentScheduleAmountInDispute | ✅ |
| AMOUNT_LINE_ITEMS_ORIGINAL | ArPaymentScheduleAmountLineItemsOriginal | ✅ |
| AMOUNT_LINE_ITEMS_REMAINING | ArPaymentScheduleAmountLineItemsRemaining | ✅ |
| AMOUNT_ON_ACCOUNT | ArPaymentScheduleAmountOnAccount | ✅ |
| AMOUNT_OTHER_ACCOUNT | ArPaymentScheduleAmountOtherAccount | ✅ |
| ASSOCIATED_CASH_RECEIPT_ID | ArPaymentScheduleAssociatedCashReceiptId | ✅ |
| ATTRIBUTE1 | ArPaymentScheduleAttribute1 | — |
| ATTRIBUTE10 | ArPaymentScheduleAttribute10 | — |
| ATTRIBUTE11 | ArPaymentScheduleAttribute11 | — |
| ATTRIBUTE12 | ArPaymentScheduleAttribute12 | — |
| ATTRIBUTE13 | ArPaymentScheduleAttribute13 | — |
| ATTRIBUTE14 | ArPaymentScheduleAttribute14 | — |
| ATTRIBUTE15 | ArPaymentScheduleAttribute15 | — |
| ATTRIBUTE2 | ArPaymentScheduleAttribute2 | — |
| ATTRIBUTE3 | ArPaymentScheduleAttribute3 | — |
| ATTRIBUTE4 | ArPaymentScheduleAttribute4 | — |
| ATTRIBUTE5 | ArPaymentScheduleAttribute5 | — |
| ATTRIBUTE6 | ArPaymentScheduleAttribute6 | — |
| ATTRIBUTE7 | ArPaymentScheduleAttribute7 | — |
| ATTRIBUTE8 | ArPaymentScheduleAttribute8 | — |
| ATTRIBUTE9 | ArPaymentScheduleAttribute9 | — |
| ATTRIBUTE_CATEGORY | ArPaymentScheduleAttributeCategory | — |
| BR_AMOUNT_ASSIGNED | ArPaymentScheduleBrAmountAssigned | ✅ |
| CALL_DATE_LAST | ArPaymentScheduleCallDateLast | ✅ |
| CASH_RECEIPT_ID | ArPaymentScheduleCashReceiptId | ✅ |
| CLASS | ArPaymentSchedulePaymentScheduleClass1 | ✅ |
| COLLECTOR_LAST | ArPaymentScheduleCollectorLast | ✅ |
| CONS_INV_ID | ArPaymentScheduleConsInvId | ✅ |
| CONS_INV_ID_REV | ArPaymentScheduleConsInvIdRev | ✅ |
| CREATED_BY | ArPaymentScheduleCreatedBy | ✅ |
| CREATION_DATE | ArPaymentScheduleCreationDate | ✅ |
| CUST_TRX_TYPE_SEQ_ID | ArPaymentScheduleCustTrxTypeSeqId | ✅ |
| CUSTOMER_ID | ArPaymentScheduleCustomerId | ✅ |
| CUSTOMER_SITE_USE_ID | ArPaymentScheduleCustomerSiteUseId | ✅ |
| CUSTOMER_TRX_ID | ArPaymentScheduleCustomerTrxId | ✅ |
| DEL_CONTACT_EMAIL_ADDRESS | ArPaymentScheduleDelContactEmailAddress | ✅ |
| DISCOUNT_TAKEN_EARNED | ArPaymentScheduleDiscountTakenEarned | ✅ |
| DISCOUNT_TAKEN_UNEARNED | ArPaymentScheduleDiscountTakenUnearned | ✅ |
| DISPUTE_DATE | ArPaymentScheduleDisputeDate | ✅ |
| DUE_DATE | ArPaymentScheduleDueDate | ✅ |
| DUNNING_LEVEL_OVERRIDE_DATE | ArPaymentScheduleDunningLevelOverrideDate | ✅ |
| EXCHANGE_DATE | ArPaymentScheduleExchangeDate | ✅ |
| EXCHANGE_RATE | ArPaymentScheduleExchangeRate | ✅ |
| EXCHANGE_RATE_TYPE | ArPaymentScheduleExchangeRateType | ✅ |
| EXCLUDE_FROM_CONS_BILL_FLAG | ArPaymentScheduleExcludeFromConsBillFlag | ✅ |
| EXCLUDE_FROM_DUNNING_FLAG | ArPaymentScheduleExcludeFromDunningFlag | ✅ |
| FOLLOW_UP_CODE_LAST | ArPaymentScheduleFollowUpCodeLast | ✅ |
| FOLLOW_UP_DATE_LAST | ArPaymentScheduleFollowUpDateLast | ✅ |
| FREIGHT_ORIGINAL | ArPaymentScheduleFreightOriginal | ✅ |
| FREIGHT_REMAINING | ArPaymentScheduleFreightRemaining | ✅ |
| GL_DATE | ArPaymentScheduleGlDate | ✅ |
| GL_DATE_CLOSED | ArPaymentScheduleGlDateClosed | ✅ |
| GLOBAL_ATTRIBUTE1 | ArPaymentScheduleGlobalAttribute1 | — |
| GLOBAL_ATTRIBUTE10 | ArPaymentScheduleGlobalAttribute10 | — |
| GLOBAL_ATTRIBUTE11 | ArPaymentScheduleGlobalAttribute11 | — |
| GLOBAL_ATTRIBUTE12 | ArPaymentScheduleGlobalAttribute12 | — |
| GLOBAL_ATTRIBUTE13 | ArPaymentScheduleGlobalAttribute13 | — |
| GLOBAL_ATTRIBUTE14 | ArPaymentScheduleGlobalAttribute14 | — |
| GLOBAL_ATTRIBUTE15 | ArPaymentScheduleGlobalAttribute15 | — |
| GLOBAL_ATTRIBUTE16 | ArPaymentScheduleGlobalAttribute16 | — |
| GLOBAL_ATTRIBUTE17 | ArPaymentScheduleGlobalAttribute17 | — |
| GLOBAL_ATTRIBUTE18 | ArPaymentScheduleGlobalAttribute18 | — |
| GLOBAL_ATTRIBUTE19 | ArPaymentScheduleGlobalAttribute19 | — |
| GLOBAL_ATTRIBUTE2 | ArPaymentScheduleGlobalAttribute2 | — |
| GLOBAL_ATTRIBUTE20 | ArPaymentScheduleGlobalAttribute20 | — |
| GLOBAL_ATTRIBUTE3 | ArPaymentScheduleGlobalAttribute3 | — |
| GLOBAL_ATTRIBUTE4 | ArPaymentScheduleGlobalAttribute4 | — |
| GLOBAL_ATTRIBUTE5 | ArPaymentScheduleGlobalAttribute5 | — |
| GLOBAL_ATTRIBUTE6 | ArPaymentScheduleGlobalAttribute6 | — |
| GLOBAL_ATTRIBUTE7 | ArPaymentScheduleGlobalAttribute7 | — |
| GLOBAL_ATTRIBUTE8 | ArPaymentScheduleGlobalAttribute8 | — |
| GLOBAL_ATTRIBUTE9 | ArPaymentScheduleGlobalAttribute9 | — |
| GLOBAL_ATTRIBUTE_CATEGORY | ArPaymentScheduleGlobalAttributeCategory | — |
| GLOBAL_ATTRIBUTE_DATE1 | ArPaymentScheduleGlobalAttributeDate1 | — |
| GLOBAL_ATTRIBUTE_DATE2 | ArPaymentScheduleGlobalAttributeDate2 | — |
| GLOBAL_ATTRIBUTE_DATE3 | ArPaymentScheduleGlobalAttributeDate3 | — |
| GLOBAL_ATTRIBUTE_DATE4 | ArPaymentScheduleGlobalAttributeDate4 | — |
| GLOBAL_ATTRIBUTE_DATE5 | ArPaymentScheduleGlobalAttributeDate5 | — |
| GLOBAL_ATTRIBUTE_NUMBER1 | ArPaymentScheduleGlobalAttributeNumber1 | — |
| GLOBAL_ATTRIBUTE_NUMBER2 | ArPaymentScheduleGlobalAttributeNumber2 | — |
| GLOBAL_ATTRIBUTE_NUMBER3 | ArPaymentScheduleGlobalAttributeNumber3 | — |
| GLOBAL_ATTRIBUTE_NUMBER4 | ArPaymentScheduleGlobalAttributeNumber4 | — |
| GLOBAL_ATTRIBUTE_NUMBER5 | ArPaymentScheduleGlobalAttributeNumber5 | — |
| IN_COLLECTION | ArPaymentScheduleInCollection | ✅ |
| INVOICE_CURRENCY_CODE | ArPaymentScheduleInvoiceCurrencyCode | ✅ |
| LAST_CHARGE_DATE | ArPaymentScheduleLastChargeDate | ✅ |
| LAST_UPDATE_DATE | ArPaymentScheduleLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ArPaymentScheduleLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ArPaymentScheduleLastUpdatedBy | ✅ |
| MODULE_ID | ArPaymentScheduleModuleId | ✅ |
| NUMBER_OF_DUE_DATES | ArPaymentScheduleNumberOfDueDates | ✅ |
| OBJECT_VERSION_NUMBER | ArPaymentScheduleObjectVersionNumber | ✅ |
| ORG_ID | ArPaymentScheduleOrgId | ✅ |
| PAYMENT_APPROVAL | ArPaymentSchedulePaymentApproval | ✅ |
| PAYMENT_SCHEDULE_ID | ArPaymentSchedulePaymentScheduleId | ✅ |
| PRINT_REQUEST_ID | ArPaymentSchedulePrintRequestId | ✅ |
| PROGRAM_APPLICATION_ID | ArPaymentScheduleProgramApplicationId | ✅ |
| PROGRAM_ID | ArPaymentScheduleProgramId | ✅ |
| PROGRAM_UPDATE_DATE | ArPaymentScheduleProgramUpdateDate | ✅ |
| PROMISE_AMOUNT_LAST | ArPaymentSchedulePromiseAmountLast | ✅ |
| PROMISE_DATE_LAST | ArPaymentSchedulePromiseDateLast | ✅ |
| RECEIPT_CONFIRMED_FLAG | ArPaymentScheduleReceiptConfirmedFlag | ✅ |
| RECEIVABLES_CHARGES_CHARGED | ArPaymentScheduleReceivablesChargesCharged | ✅ |
| RECEIVABLES_CHARGES_REMAINING | ArPaymentScheduleReceivablesChargesRemaining | ✅ |
| REQUEST_ID | ArPaymentScheduleRequestId | ✅ |
| RESERVED_TYPE | ArPaymentScheduleReservedType | ✅ |
| RESERVED_VALUE | ArPaymentScheduleReservedValue | ✅ |
| REVERSED_CASH_RECEIPT_ID | ArPaymentScheduleReversedCashReceiptId | ✅ |
| SEED_DATA_SOURCE | ArPaymentScheduleSeedDataSource | ✅ |
| SELECTED_FOR_RECEIPT_BATCH_ID | ArPaymentScheduleSelectedForReceiptBatchId | ✅ |
| STAGED_DUNNING_LEVEL | ArPaymentScheduleStagedDunningLevel | ✅ |
| STATUS | ArPaymentScheduleStatus | ✅ |
| TAX_ORIGINAL | ArPaymentScheduleTaxOriginal | ✅ |
| TAX_REMAINING | ArPaymentScheduleTaxRemaining | ✅ |
| TERM_ID | ArPaymentScheduleTermId | ✅ |
| TERMS_SEQUENCE_NUMBER | ArPaymentScheduleTermsSequenceNumber | ✅ |
| TRX_DATE | ArPaymentScheduleTrxDate | ✅ |
| TRX_NUMBER | ArPaymentScheduleTrxNumber | ✅ |

### [[paymentschedulepvo|PaymentSchedulePVO]] (AR · BICC: 40/93)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_DUE_REMAINING | PaymentScheduleAcctdAmountDueRemaining | ✅ |
| ACTIVE_CLAIM_FLAG | PaymentScheduleActiveClaimFlag | — |
| ACTUAL_DATE_CLOSED | PaymentScheduleActualDateClosed | ✅ |
| ADJUSTMENT_AMOUNT_LAST | PaymentScheduleAdjustmentAmountLast | — |
| ADJUSTMENT_DATE_LAST | PaymentScheduleAdjustmentDateLast | — |
| ADJUSTMENT_GL_DATE_LAST | PaymentScheduleAdjustmentGlDateLast | — |
| ADJUSTMENT_ID_LAST | PaymentScheduleAdjustmentIdLast | — |
| AMOUNT_ADJUSTED | PaymentScheduleAmountAdjusted | ✅ |
| AMOUNT_ADJUSTED_PENDING | PaymentScheduleAmountAdjustedPending | ✅ |
| AMOUNT_APPLIED | PaymentScheduleAmountApplied | ✅ |
| AMOUNT_CREDITED | PaymentScheduleAmountCredited | ✅ |
| AMOUNT_DUE_ORIGINAL | PaymentScheduleAmountDueOriginal | ✅ |
| AMOUNT_DUE_REMAINING | PaymentScheduleAmountDueRemaining | ✅ |
| AMOUNT_IN_DISPUTE | PaymentScheduleAmountInDispute | ✅ |
| AMOUNT_LINE_ITEMS_ORIGINAL | PaymentScheduleAmountLineItemsOriginal | ✅ |
| AMOUNT_LINE_ITEMS_REMAINING | PaymentScheduleAmountLineItemsRemaining | ✅ |
| AMOUNT_ON_ACCOUNT | PaymentScheduleAmountOnAccount | ✅ |
| AMOUNT_OTHER_ACCOUNT | PaymentScheduleAmountOtherAccount | ✅ |
| ASSOCIATED_CASH_RECEIPT_ID | PaymentScheduleAssociatedCashReceiptId | — |
| BR_AMOUNT_ASSIGNED | PaymentScheduleBrAmountAssigned | — |
| CALL_DATE_LAST | PaymentScheduleCallDateLast | — |
| CASH_APPLIED_AMOUNT_LAST | PaymentScheduleCashAppliedAmountLast | — |
| CASH_APPLIED_DATE_LAST | PaymentScheduleCashAppliedDateLast | — |
| CASH_APPLIED_ID_LAST | PaymentScheduleCashAppliedIdLast | — |
| CASH_APPLIED_STATUS_LAST | PaymentScheduleCashAppliedStatusLast | — |
| CASH_GL_DATE_LAST | PaymentScheduleCashGlDateLast | — |
| CASH_RECEIPT_AMOUNT_LAST | PaymentScheduleCashReceiptAmountLast | — |
| CASH_RECEIPT_DATE_LAST | PaymentScheduleCashReceiptDateLast | — |
| CASH_RECEIPT_ID | PaymentScheduleCashReceiptId | — |
| CASH_RECEIPT_ID_LAST | PaymentScheduleCashReceiptIdLast | — |
| CASH_RECEIPT_STATUS_LAST | PaymentScheduleCashReceiptStatusLast | — |
| CLASS | PaymentSchedulePaymentScheduleClass | ✅ |
| COLLECTOR_LAST | PaymentScheduleCollectorLast | — |
| CONS_INV_ID | PaymentScheduleConsInvId | — |
| CONS_INV_ID_REV | PaymentScheduleConsInvIdRev | — |
| CREATED_BY | PaymentScheduleCreatedBy | ✅ |
| CREATION_DATE | PaymentScheduleCreationDate | ✅ |
| CUST_TRX_TYPE_SEQ_ID | PaymentScheduleCustTrxTypeSeqId | — |
| CUSTOMER_ID | PaymentScheduleCustomerId | — |
| CUSTOMER_SITE_USE_ID | PaymentScheduleCustomerSiteUseId | ✅ |
| CUSTOMER_TRX_ID | PaymentScheduleCustomerTrxId | — |
| DISCOUNT_DATE | PaymentScheduleDiscountDate | — |
| DISCOUNT_ORIGINAL | PaymentScheduleDiscountOriginal | — |
| DISCOUNT_REMAINING | PaymentScheduleDiscountRemaining | — |
| DISCOUNT_TAKEN_EARNED | PaymentScheduleDiscountTakenEarned | ✅ |
| DISCOUNT_TAKEN_UNEARNED | PaymentScheduleDiscountTakenUnearned | ✅ |
| DISPUTE_DATE | PaymentScheduleDisputeDate | ✅ |
| DUE_DATE | PaymentScheduleDueDate | ✅ |
| DUNNING_LEVEL_OVERRIDE_DATE | PaymentScheduleDunningLevelOverrideDate | — |
| EXCHANGE_DATE | PaymentScheduleExchangeDate | ✅ |
| EXCHANGE_RATE | PaymentScheduleExchangeRate | ✅ |
| EXCHANGE_RATE_TYPE | PaymentScheduleExchangeRateType | ✅ |
| EXCLUDE_FROM_CONS_BILL_FLAG | PaymentScheduleExcludeFromConsBillFlag | — |
| EXCLUDE_FROM_DUNNING_FLAG | PaymentScheduleExcludeFromDunningFlag | — |
| FOLLOW_UP_CODE_LAST | PaymentScheduleFollowUpCodeLast | — |
| FOLLOW_UP_DATE_LAST | PaymentScheduleFollowUpDateLast | — |
| FREIGHT_ORIGINAL | PaymentScheduleFreightOriginal | ✅ |
| FREIGHT_REMAINING | PaymentScheduleFreightRemaining | ✅ |
| GL_DATE | PaymentScheduleGlDate | ✅ |
| GL_DATE_CLOSED | PaymentScheduleGlDateClosed | ✅ |
| IN_COLLECTION | PaymentScheduleInCollection | — |
| INVOICE_CURRENCY_CODE | PaymentScheduleInvoiceCurrencyCode | — |
| LAST_CHARGE_DATE | PaymentScheduleLastChargeDate | — |
| LAST_UPDATE_DATE | PaymentScheduleLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PaymentScheduleLastUpdateLogin | — |
| LAST_UPDATED_BY | PaymentScheduleLastUpdatedBy | ✅ |
| NUMBER_OF_DUE_DATES | PaymentScheduleNumberOfDueDates | ✅ |
| OBJECT_VERSION_NUMBER | PaymentScheduleObjectVersionNumber | — |
| ORG_ID | PaymentScheduleOrgId | — |
| PAYMENT_APPROVAL | PaymentSchedulePaymentApproval | — |
| PAYMENT_SCHEDULE_ID | PaymentScheduleId | ✅ |
| PROGRAM_APPLICATION_ID | PaymentScheduleProgramApplicationId | — |
| PROGRAM_ID | PaymentScheduleProgramId | — |
| PROGRAM_UPDATE_DATE | PaymentScheduleProgramUpdateDate | — |
| PROMISE_AMOUNT_LAST | PaymentSchedulePromiseAmountLast | — |
| PROMISE_DATE_LAST | PaymentSchedulePromiseDateLast | — |
| RECEIPT_CONFIRMED_FLAG | PaymentScheduleReceiptConfirmedFlag | — |
| RECEIVABLES_CHARGES_CHARGED | PaymentScheduleReceivablesChargesCharged | ✅ |
| RECEIVABLES_CHARGES_REMAINING | PaymentScheduleReceivablesChargesRemaining | ✅ |
| REQUEST_ID | PaymentScheduleRequestId | — |
| RESERVED_TYPE | PaymentScheduleReservedType | — |
| RESERVED_VALUE | PaymentScheduleReservedValue | — |
| REVERSED_CASH_RECEIPT_ID | PaymentScheduleReversedCashReceiptId | — |
| SECOND_LAST_CHARGE_DATE | PaymentScheduleSecondLastChargeDate | — |
| SELECTED_FOR_RECEIPT_BATCH_ID | PaymentScheduleSelectedForReceiptBatchId | — |
| STAGED_DUNNING_LEVEL | PaymentScheduleStagedDunningLevel | — |
| STATUS | PaymentScheduleStatus | ✅ |
| TAX_ORIGINAL | PaymentScheduleTaxOriginal | ✅ |
| TAX_REMAINING | PaymentScheduleTaxRemaining | ✅ |
| TERM_ID | PaymentScheduleTermId | — |
| TERMS_SEQUENCE_NUMBER | PaymentScheduleTermsSequenceNumber | ✅ |
| TRX_DATE | PaymentScheduleTrxDate | ✅ |
| TRX_NUMBER | PaymentScheduleTrxNumber | ✅ |

### [[receiptapplicationdistributionpvo|ReceiptApplicationDistributionPVO]] (AR · BICC: 10/280)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_DUE_REMAINING | PaymentScheduleAcctdAmountDueRemaining | — |
| ACCTD_AMOUNT_DUE_REMAINING | PaymentScheduleAppliedAcctdAmountDueRemaining | — |
| ACCTD_AMOUNT_DUE_REMAINING | PaymentSchedulesAcctdAmountDueRemaining | — |
| ACTIVE_CLAIM_FLAG | PaymentScheduleActiveClaimFlag | — |
| ACTIVE_CLAIM_FLAG | PaymentScheduleAppliedActiveClaimFlag | — |
| ACTIVE_CLAIM_FLAG | PaymentSchedulesActiveClaimFlag | — |
| ACTUAL_DATE_CLOSED | PaymentScheduleActualDateClosed | — |
| ACTUAL_DATE_CLOSED | PaymentScheduleAppliedActualDateClosed | — |
| ACTUAL_DATE_CLOSED | PaymentSchedulesActualDateClosed | — |
| ADJUSTMENT_AMOUNT_LAST | PaymentScheduleAdjustmentAmountLast | — |
| ADJUSTMENT_AMOUNT_LAST | PaymentScheduleAppliedAdjustmentAmountLast | — |
| ADJUSTMENT_AMOUNT_LAST | PaymentSchedulesAdjustmentAmountLast | — |
| ADJUSTMENT_DATE_LAST | PaymentScheduleAdjustmentDateLast | — |
| ADJUSTMENT_DATE_LAST | PaymentScheduleAppliedAdjustmentDateLast | — |
| ADJUSTMENT_DATE_LAST | PaymentSchedulesAdjustmentDateLast | — |
| ADJUSTMENT_GL_DATE_LAST | PaymentScheduleAdjustmentGlDateLast | — |
| ADJUSTMENT_GL_DATE_LAST | PaymentScheduleAppliedAdjustmentGlDateLast | — |
| ADJUSTMENT_GL_DATE_LAST | PaymentSchedulesAdjustmentGlDateLast | — |
| ADJUSTMENT_ID_LAST | PaymentScheduleAdjustmentIdLast | — |
| ADJUSTMENT_ID_LAST | PaymentScheduleAppliedAdjustmentIdLast | — |
| ADJUSTMENT_ID_LAST | PaymentSchedulesAdjustmentIdLast | — |
| AMOUNT_ADJUSTED | PaymentScheduleAmountAdjusted | — |
| AMOUNT_ADJUSTED | PaymentScheduleAppliedAmountAdjusted | — |
| AMOUNT_ADJUSTED | PaymentSchedulesAmountAdjusted | — |
| AMOUNT_ADJUSTED_PENDING | PaymentScheduleAmountAdjustedPending | — |
| AMOUNT_ADJUSTED_PENDING | PaymentScheduleAppliedAmountAdjustedPending | — |
| AMOUNT_ADJUSTED_PENDING | PaymentSchedulesAmountAdjustedPending | — |
| AMOUNT_APPLIED | PaymentScheduleAmountApplied | — |
| AMOUNT_APPLIED | PaymentScheduleAppliedAmountApplied | — |
| AMOUNT_APPLIED | PaymentSchedulesAmountApplied | — |
| AMOUNT_CREDITED | PaymentScheduleAmountCredited | — |
| AMOUNT_CREDITED | PaymentScheduleAppliedAmountCredited | — |
| AMOUNT_CREDITED | PaymentSchedulesAmountCredited | — |
| AMOUNT_DUE_ORIGINAL | PaymentScheduleAmountDueOriginal | — |
| AMOUNT_DUE_ORIGINAL | PaymentScheduleAppliedAmountDueOriginal | — |
| AMOUNT_DUE_ORIGINAL | PaymentSchedulesAmountDueOriginal | — |
| AMOUNT_DUE_REMAINING | PaymentScheduleAmountDueRemaining | — |
| AMOUNT_DUE_REMAINING | PaymentScheduleAppliedAmountDueRemaining | — |
| AMOUNT_DUE_REMAINING | PaymentSchedulesAmountDueRemaining | — |
| AMOUNT_IN_DISPUTE | PaymentScheduleAmountInDispute | — |
| AMOUNT_IN_DISPUTE | PaymentScheduleAppliedAmountInDispute | — |
| AMOUNT_IN_DISPUTE | PaymentSchedulesAmountInDispute | — |
| AMOUNT_LINE_ITEMS_ORIGINAL | PaymentScheduleAmountLineItemsOriginal | — |
| AMOUNT_LINE_ITEMS_ORIGINAL | PaymentScheduleAppliedAmountLineItemsOriginal | — |
| AMOUNT_LINE_ITEMS_ORIGINAL | PaymentSchedulesAmountLineItemsOriginal | — |
| AMOUNT_LINE_ITEMS_REMAINING | PaymentScheduleAmountLineItemsRemaining | — |
| AMOUNT_LINE_ITEMS_REMAINING | PaymentScheduleAppliedAmountLineItemsRemaining | — |
| AMOUNT_LINE_ITEMS_REMAINING | PaymentSchedulesAmountLineItemsRemaining | — |
| AMOUNT_ON_ACCOUNT | PaymentScheduleAmountOnAccount | — |
| AMOUNT_ON_ACCOUNT | PaymentScheduleAppliedAmountOnAccount | — |
| AMOUNT_ON_ACCOUNT | PaymentSchedulesAmountOnAccount | — |
| AMOUNT_OTHER_ACCOUNT | PaymentScheduleAmountOtherAccount | — |
| AMOUNT_OTHER_ACCOUNT | PaymentScheduleAppliedAmountOtherAccount | — |
| AMOUNT_OTHER_ACCOUNT | PaymentSchedulesAmountOtherAccount | — |
| ASSOCIATED_CASH_RECEIPT_ID | PaymentScheduleAppliedAssociatedCashReceiptId | — |
| ASSOCIATED_CASH_RECEIPT_ID | PaymentScheduleAssociatedCashReceiptId | — |
| ASSOCIATED_CASH_RECEIPT_ID | PaymentSchedulesAssociatedCashReceiptId | — |
| BR_AMOUNT_ASSIGNED | PaymentScheduleAppliedBrAmountAssigned | — |
| BR_AMOUNT_ASSIGNED | PaymentScheduleBrAmountAssigned | — |
| BR_AMOUNT_ASSIGNED | PaymentSchedulesBrAmountAssigned | — |
| CALL_DATE_LAST | PaymentScheduleAppliedCallDateLast | — |
| CALL_DATE_LAST | PaymentScheduleCallDateLast | — |
| CALL_DATE_LAST | PaymentSchedulesCallDateLast | — |
| CASH_APPLIED_AMOUNT_LAST | PaymentScheduleAppliedCashAppliedAmountLast | — |
| CASH_APPLIED_AMOUNT_LAST | PaymentScheduleCashAppliedAmountLast | — |
| CASH_APPLIED_AMOUNT_LAST | PaymentSchedulesCashAppliedAmountLast | — |
| CASH_APPLIED_DATE_LAST | PaymentScheduleAppliedCashAppliedDateLast | — |
| CASH_APPLIED_DATE_LAST | PaymentScheduleCashAppliedDateLast | — |
| CASH_APPLIED_DATE_LAST | PaymentSchedulesCashAppliedDateLast | — |
| CASH_APPLIED_ID_LAST | PaymentScheduleAppliedCashAppliedIdLast | — |
| CASH_APPLIED_ID_LAST | PaymentScheduleCashAppliedIdLast | — |
| CASH_APPLIED_ID_LAST | PaymentSchedulesCashAppliedIdLast | — |
| CASH_APPLIED_STATUS_LAST | PaymentScheduleAppliedCashAppliedStatusLast | — |
| CASH_APPLIED_STATUS_LAST | PaymentScheduleCashAppliedStatusLast | — |
| CASH_APPLIED_STATUS_LAST | PaymentSchedulesCashAppliedStatusLast | — |
| CASH_GL_DATE_LAST | PaymentScheduleAppliedCashGlDateLast | — |
| CASH_GL_DATE_LAST | PaymentScheduleCashGlDateLast | — |
| CASH_GL_DATE_LAST | PaymentSchedulesCashGlDateLast | — |
| CASH_RECEIPT_AMOUNT_LAST | PaymentScheduleAppliedCashReceiptAmountLast | — |
| CASH_RECEIPT_AMOUNT_LAST | PaymentScheduleCashReceiptAmountLast | — |
| CASH_RECEIPT_AMOUNT_LAST | PaymentSchedulesCashReceiptAmountLast | — |
| CASH_RECEIPT_DATE_LAST | PaymentScheduleAppliedCashReceiptDateLast | — |
| CASH_RECEIPT_DATE_LAST | PaymentScheduleCashReceiptDateLast | — |
| CASH_RECEIPT_DATE_LAST | PaymentSchedulesCashReceiptDateLast | — |
| CASH_RECEIPT_ID | PaymentScheduleAppliedCashReceiptId | — |
| CASH_RECEIPT_ID | PaymentScheduleCashReceiptId | — |
| CASH_RECEIPT_ID | PaymentSchedulesCashReceiptId1 | — |
| CASH_RECEIPT_ID_LAST | PaymentScheduleAppliedCashReceiptIdLast | — |
| CASH_RECEIPT_ID_LAST | PaymentScheduleCashReceiptIdLast | — |
| CASH_RECEIPT_ID_LAST | PaymentSchedulesCashReceiptIdLast | — |
| CASH_RECEIPT_STATUS_LAST | PaymentScheduleAppliedCashReceiptStatusLast | — |
| CASH_RECEIPT_STATUS_LAST | PaymentScheduleCashReceiptStatusLast | — |
| CASH_RECEIPT_STATUS_LAST | PaymentSchedulesCashReceiptStatusLast | — |
| CLASS | PaymentScheduleAppliedPaymentScheduleClass | — |
| CLASS | PaymentSchedulePaymentScheduleClass | — |
| CLASS | PaymentSchedulesPaymentScheduleClass1 | — |
| COLLECTOR_LAST | PaymentScheduleAppliedCollectorLast | — |
| COLLECTOR_LAST | PaymentScheduleCollectorLast | — |
| COLLECTOR_LAST | PaymentSchedulesCollectorLast | — |
| CONS_INV_ID | PaymentScheduleAppliedConsInvId | — |
| CONS_INV_ID | PaymentScheduleConsInvId | — |
| CONS_INV_ID | PaymentSchedulesConsInvId | — |
| CONS_INV_ID_REV | PaymentScheduleAppliedConsInvIdRev | — |
| CONS_INV_ID_REV | PaymentScheduleConsInvIdRev | — |
| CONS_INV_ID_REV | PaymentSchedulesConsInvIdRev | — |
| CREATED_BY | PaymentScheduleAppliedCreatedBy | — |
| CREATED_BY | PaymentScheduleCreatedBy | — |
| CREATED_BY | PaymentSchedulesCreatedBy | — |
| CREATION_DATE | PaymentScheduleAppliedCreationDate | — |
| CREATION_DATE | PaymentScheduleCreationDate | — |
| CREATION_DATE | PaymentSchedulesCreationDate | — |
| CUST_TRX_TYPE_SEQ_ID | PaymentScheduleAppliedCustTrxTypeSeqId | — |
| CUST_TRX_TYPE_SEQ_ID | PaymentScheduleCustTrxTypeSeqId | — |
| CUST_TRX_TYPE_SEQ_ID | PaymentSchedulesCustTrxTypeSeqId | — |
| CUSTOMER_ID | PaymentScheduleAppliedCustomerId | — |
| CUSTOMER_ID | PaymentScheduleCustomerId | — |
| CUSTOMER_ID | PaymentSchedulesCustomerId | — |
| CUSTOMER_SITE_USE_ID | PaymentScheduleAppliedCustomerSiteUseId | — |
| CUSTOMER_SITE_USE_ID | PaymentScheduleCustomerSiteUseId | ✅ |
| CUSTOMER_SITE_USE_ID | PaymentSchedulesCustomerSiteUseId | — |
| CUSTOMER_TRX_ID | PaymentScheduleAppliedCustomerTrxId | — |
| CUSTOMER_TRX_ID | PaymentScheduleCustomerTrxId | — |
| CUSTOMER_TRX_ID | PaymentSchedulesCustomerTrxId | — |
| DISCOUNT_DATE | PaymentScheduleAppliedDiscountDate | — |
| DISCOUNT_DATE | PaymentScheduleDiscountDate | — |
| DISCOUNT_DATE | PaymentSchedulesDiscountDate | — |
| DISCOUNT_ORIGINAL | PaymentScheduleAppliedDiscountOriginal | — |
| DISCOUNT_ORIGINAL | PaymentScheduleDiscountOriginal | — |
| DISCOUNT_ORIGINAL | PaymentSchedulesDiscountOriginal | — |
| DISCOUNT_REMAINING | PaymentScheduleAppliedDiscountRemaining | — |
| DISCOUNT_REMAINING | PaymentScheduleDiscountRemaining | — |
| DISCOUNT_REMAINING | PaymentSchedulesDiscountRemaining | — |
| DISCOUNT_TAKEN_EARNED | PaymentScheduleAppliedDiscountTakenEarned | — |
| DISCOUNT_TAKEN_EARNED | PaymentScheduleDiscountTakenEarned | — |
| DISCOUNT_TAKEN_EARNED | PaymentSchedulesDiscountTakenEarned | — |
| DISCOUNT_TAKEN_UNEARNED | PaymentScheduleAppliedDiscountTakenUnearned | — |
| DISCOUNT_TAKEN_UNEARNED | PaymentScheduleDiscountTakenUnearned | — |
| DISCOUNT_TAKEN_UNEARNED | PaymentSchedulesDiscountTakenUnearned | — |
| DISPUTE_DATE | PaymentScheduleAppliedDisputeDate | — |
| DISPUTE_DATE | PaymentScheduleDisputeDate | — |
| DISPUTE_DATE | PaymentSchedulesDisputeDate | — |
| DUE_DATE | PaymentScheduleAppliedDueDate | ✅ |
| DUE_DATE | PaymentScheduleDueDate | ✅ |
| DUE_DATE | PaymentSchedulesDueDate | — |
| DUNNING_LEVEL_OVERRIDE_DATE | PaymentScheduleAppliedDunningLevelOverrideDate | — |
| DUNNING_LEVEL_OVERRIDE_DATE | PaymentScheduleDunningLevelOverrideDate | — |
| DUNNING_LEVEL_OVERRIDE_DATE | PaymentSchedulesDunningLevelOverrideDate | — |
| EXCHANGE_DATE | PaymentScheduleAppliedExchangeDate | — |
| EXCHANGE_DATE | PaymentScheduleExchangeDate | — |
| EXCHANGE_DATE | PaymentSchedulesExchangeDate | — |
| EXCHANGE_RATE | PaymentScheduleAppliedExchangeRate | — |
| EXCHANGE_RATE | PaymentScheduleExchangeRate | — |
| EXCHANGE_RATE | PaymentSchedulesExchangeRate | — |
| EXCHANGE_RATE_TYPE | PaymentScheduleAppliedExchangeRateType | — |
| EXCHANGE_RATE_TYPE | PaymentScheduleExchangeRateType | — |
| EXCHANGE_RATE_TYPE | PaymentSchedulesExchangeRateType | — |
| EXCLUDE_FROM_CONS_BILL_FLAG | PaymentScheduleAppliedExcludeFromConsBillFlag | — |
| EXCLUDE_FROM_CONS_BILL_FLAG | PaymentScheduleExcludeFromConsBillFlag | — |
| EXCLUDE_FROM_CONS_BILL_FLAG | PaymentSchedulesExcludeFromConsBillFlag | — |
| EXCLUDE_FROM_DUNNING_FLAG | PaymentScheduleAppliedExcludeFromDunningFlag | — |
| EXCLUDE_FROM_DUNNING_FLAG | PaymentScheduleExcludeFromDunningFlag | — |
| EXCLUDE_FROM_DUNNING_FLAG | PaymentSchedulesExcludeFromDunningFlag | — |
| FOLLOW_UP_CODE_LAST | PaymentScheduleAppliedFollowUpCodeLast | — |
| FOLLOW_UP_CODE_LAST | PaymentScheduleFollowUpCodeLast | — |
| FOLLOW_UP_CODE_LAST | PaymentSchedulesFollowUpCodeLast | — |
| FOLLOW_UP_DATE_LAST | PaymentScheduleAppliedFollowUpDateLast | — |
| FOLLOW_UP_DATE_LAST | PaymentScheduleFollowUpDateLast | — |
| FOLLOW_UP_DATE_LAST | PaymentSchedulesFollowUpDateLast | — |
| FREIGHT_ORIGINAL | PaymentScheduleAppliedFreightOriginal | — |
| FREIGHT_ORIGINAL | PaymentScheduleFreightOriginal | — |
| FREIGHT_ORIGINAL | PaymentSchedulesFreightOriginal | — |
| FREIGHT_REMAINING | PaymentScheduleAppliedFreightRemaining | — |
| FREIGHT_REMAINING | PaymentScheduleFreightRemaining | — |
| FREIGHT_REMAINING | PaymentSchedulesFreightRemaining | — |
| GL_DATE | PaymentScheduleAppliedGlDate | — |
| GL_DATE | PaymentScheduleGlDate | — |
| GL_DATE | PaymentSchedulesGlDate | — |
| GL_DATE_CLOSED | PaymentScheduleAppliedGlDateClosed | — |
| GL_DATE_CLOSED | PaymentScheduleGlDateClosed | — |
| GL_DATE_CLOSED | PaymentSchedulesGlDateClosed | — |
| IN_COLLECTION | PaymentScheduleAppliedInCollection | — |
| IN_COLLECTION | PaymentScheduleInCollection | — |
| IN_COLLECTION | PaymentSchedulesInCollection | — |
| INVOICE_CURRENCY_CODE | PaymentScheduleAppliedInvoiceCurrencyCode | — |
| INVOICE_CURRENCY_CODE | PaymentScheduleInvoiceCurrencyCode | — |
| INVOICE_CURRENCY_CODE | PaymentSchedulesInvoiceCurrencyCode | — |
| LAST_CHARGE_DATE | PaymentScheduleAppliedLastChargeDate | — |
| LAST_CHARGE_DATE | PaymentScheduleLastChargeDate | — |
| LAST_CHARGE_DATE | PaymentSchedulesLastChargeDate | — |
| LAST_UPDATE_DATE | PaymentScheduleAppliedLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | PaymentScheduleLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | PaymentSchedulesLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PaymentScheduleAppliedLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | PaymentScheduleLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | PaymentSchedulesLastUpdateLogin | — |
| LAST_UPDATED_BY | PaymentScheduleAppliedLastUpdatedBy | — |
| LAST_UPDATED_BY | PaymentScheduleLastUpdatedBy | — |
| LAST_UPDATED_BY | PaymentSchedulesLastUpdatedBy | — |
| NUMBER_OF_DUE_DATES | PaymentScheduleAppliedNumberOfDueDates | — |
| NUMBER_OF_DUE_DATES | PaymentScheduleNumberOfDueDates | — |
| NUMBER_OF_DUE_DATES | PaymentSchedulesNumberOfDueDates | — |
| OBJECT_VERSION_NUMBER | PaymentScheduleAppliedObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | PaymentScheduleObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | PaymentSchedulesObjectVersionNumber | — |
| ORG_ID | PaymentScheduleAppliedOrgId | — |
| ORG_ID | PaymentScheduleOrgId | — |
| ORG_ID | PaymentSchedulesOrgId | — |
| PAYMENT_APPROVAL | PaymentScheduleAppliedPaymentApproval | — |
| PAYMENT_APPROVAL | PaymentSchedulePaymentApproval | — |
| PAYMENT_APPROVAL | PaymentSchedulesPaymentApproval | — |
| PAYMENT_SCHEDULE_ID | PaymentScheduleAppliedPaymentScheduleId | ✅ |
| PAYMENT_SCHEDULE_ID | PaymentSchedulePaymentScheduleId | ✅ |
| PAYMENT_SCHEDULE_ID | PaymentSchedulesDebitMemoPaymentScheduleId | — |
| PAYMENT_SCHEDULE_ID | PaymentSchedulesPaymentScheduleId | — |
| PROGRAM_APPLICATION_ID | PaymentScheduleAppliedProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | PaymentScheduleProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | PaymentSchedulesProgramApplicationId | — |
| PROGRAM_ID | PaymentScheduleAppliedProgramId | — |
| PROGRAM_ID | PaymentScheduleProgramId | — |
| PROGRAM_ID | PaymentSchedulesProgramId | — |
| PROGRAM_UPDATE_DATE | PaymentScheduleAppliedProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | PaymentScheduleProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | PaymentSchedulesProgramUpdateDate | — |
| PROMISE_AMOUNT_LAST | PaymentScheduleAppliedPromiseAmountLast | — |
| PROMISE_AMOUNT_LAST | PaymentSchedulePromiseAmountLast | — |
| PROMISE_AMOUNT_LAST | PaymentSchedulesPromiseAmountLast | — |
| PROMISE_DATE_LAST | PaymentScheduleAppliedPromiseDateLast | — |
| PROMISE_DATE_LAST | PaymentSchedulePromiseDateLast | — |
| PROMISE_DATE_LAST | PaymentSchedulesPromiseDateLast | — |
| RECEIPT_CONFIRMED_FLAG | PaymentScheduleAppliedReceiptConfirmedFlag | — |
| RECEIPT_CONFIRMED_FLAG | PaymentScheduleReceiptConfirmedFlag | — |
| RECEIPT_CONFIRMED_FLAG | PaymentSchedulesReceiptConfirmedFlag1 | — |
| RECEIVABLES_CHARGES_CHARGED | PaymentScheduleAppliedReceivablesChargesCharged | — |
| RECEIVABLES_CHARGES_CHARGED | PaymentScheduleReceivablesChargesCharged | — |
| RECEIVABLES_CHARGES_CHARGED | PaymentSchedulesReceivablesChargesCharged | — |
| RECEIVABLES_CHARGES_REMAINING | PaymentScheduleAppliedReceivablesChargesRemaining | — |
| RECEIVABLES_CHARGES_REMAINING | PaymentScheduleReceivablesChargesRemaining | — |
| RECEIVABLES_CHARGES_REMAINING | PaymentSchedulesReceivablesChargesRemaining | — |
| REQUEST_ID | PaymentScheduleAppliedRequestId | — |
| REQUEST_ID | PaymentScheduleRequestId | — |
| REQUEST_ID | PaymentSchedulesRequestId | — |
| RESERVED_TYPE | PaymentScheduleAppliedReservedType | — |
| RESERVED_TYPE | PaymentScheduleReservedType | — |
| RESERVED_TYPE | PaymentSchedulesReservedType | — |
| RESERVED_VALUE | PaymentScheduleAppliedReservedValue | — |
| RESERVED_VALUE | PaymentScheduleReservedValue | — |
| RESERVED_VALUE | PaymentSchedulesReservedValue | — |
| REVERSED_CASH_RECEIPT_ID | PaymentScheduleAppliedReversedCashReceiptId | — |
| REVERSED_CASH_RECEIPT_ID | PaymentScheduleReversedCashReceiptId | — |
| REVERSED_CASH_RECEIPT_ID | PaymentSchedulesReversedCashReceiptId | — |
| SECOND_LAST_CHARGE_DATE | PaymentScheduleAppliedSecondLastChargeDate | — |
| SECOND_LAST_CHARGE_DATE | PaymentScheduleSecondLastChargeDate | — |
| SECOND_LAST_CHARGE_DATE | PaymentSchedulesSecondLastChargeDate | — |
| SELECTED_FOR_RECEIPT_BATCH_ID | PaymentScheduleAppliedSelectedForReceiptBatchId | — |
| SELECTED_FOR_RECEIPT_BATCH_ID | PaymentScheduleSelectedForReceiptBatchId | — |
| SELECTED_FOR_RECEIPT_BATCH_ID | PaymentSchedulesSelectedForReceiptBatchId | — |
| STAGED_DUNNING_LEVEL | PaymentScheduleAppliedStagedDunningLevel | — |
| STAGED_DUNNING_LEVEL | PaymentScheduleStagedDunningLevel | — |
| STAGED_DUNNING_LEVEL | PaymentSchedulesStagedDunningLevel | — |
| STATUS | PaymentScheduleAppliedStatus | ✅ |
| STATUS | PaymentScheduleStatus | ✅ |
| STATUS | PaymentSchedulesStatus | — |
| TAX_ORIGINAL | PaymentScheduleAppliedTaxOriginal | — |
| TAX_ORIGINAL | PaymentScheduleTaxOriginal | — |
| TAX_ORIGINAL | PaymentSchedulesTaxOriginal | — |
| TAX_REMAINING | PaymentScheduleAppliedTaxRemaining | — |
| TAX_REMAINING | PaymentScheduleTaxRemaining | — |
| TAX_REMAINING | PaymentSchedulesTaxRemaining | — |
| TERM_ID | PaymentScheduleAppliedTermId | — |
| TERM_ID | PaymentScheduleTermId | — |
| TERM_ID | PaymentSchedulesTermId | — |
| TERMS_SEQUENCE_NUMBER | PaymentScheduleAppliedTermsSequenceNumber | — |
| TERMS_SEQUENCE_NUMBER | PaymentScheduleTermsSequenceNumber | — |
| TERMS_SEQUENCE_NUMBER | PaymentSchedulesTermsSequenceNumber | — |
| TRX_DATE | PaymentScheduleAppliedTrxDate | — |
| TRX_DATE | PaymentScheduleTrxDate | — |
| TRX_DATE | PaymentSchedulesTrxDate | — |
| TRX_NUMBER | PaymentScheduleAppliedTrxNumber | — |
| TRX_NUMBER | PaymentScheduleTrxNumber | — |
| TRX_NUMBER | PaymentSchedulesTrxNumber | — |

### [[receiptapplicationdistributionvc|ReceiptApplicationDistributionVC]] (AR · BICC: 5/280)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_DUE_REMAINING | PaymentScheduleAcctdAmountDueRemaining | — |
| ACCTD_AMOUNT_DUE_REMAINING | PaymentScheduleAppliedAcctdAmountDueRemaining | — |
| ACCTD_AMOUNT_DUE_REMAINING | PaymentSchedulesAcctdAmountDueRemaining | — |
| ACTIVE_CLAIM_FLAG | PaymentScheduleActiveClaimFlag | — |
| ACTIVE_CLAIM_FLAG | PaymentScheduleAppliedActiveClaimFlag | — |
| ACTIVE_CLAIM_FLAG | PaymentSchedulesActiveClaimFlag | — |
| ACTUAL_DATE_CLOSED | PaymentScheduleActualDateClosed | — |
| ACTUAL_DATE_CLOSED | PaymentScheduleAppliedActualDateClosed | — |
| ACTUAL_DATE_CLOSED | PaymentSchedulesActualDateClosed | — |
| ADJUSTMENT_AMOUNT_LAST | PaymentScheduleAdjustmentAmountLast | — |
| ADJUSTMENT_AMOUNT_LAST | PaymentScheduleAppliedAdjustmentAmountLast | — |
| ADJUSTMENT_AMOUNT_LAST | PaymentSchedulesAdjustmentAmountLast | — |
| ADJUSTMENT_DATE_LAST | PaymentScheduleAdjustmentDateLast | — |
| ADJUSTMENT_DATE_LAST | PaymentScheduleAppliedAdjustmentDateLast | — |
| ADJUSTMENT_DATE_LAST | PaymentSchedulesAdjustmentDateLast | — |
| ADJUSTMENT_GL_DATE_LAST | PaymentScheduleAdjustmentGlDateLast | — |
| ADJUSTMENT_GL_DATE_LAST | PaymentScheduleAppliedAdjustmentGlDateLast | — |
| ADJUSTMENT_GL_DATE_LAST | PaymentSchedulesAdjustmentGlDateLast | — |
| ADJUSTMENT_ID_LAST | PaymentScheduleAdjustmentIdLast | — |
| ADJUSTMENT_ID_LAST | PaymentScheduleAppliedAdjustmentIdLast | — |
| ADJUSTMENT_ID_LAST | PaymentSchedulesAdjustmentIdLast | — |
| AMOUNT_ADJUSTED | PaymentScheduleAmountAdjusted | — |
| AMOUNT_ADJUSTED | PaymentScheduleAppliedAmountAdjusted | — |
| AMOUNT_ADJUSTED | PaymentSchedulesAmountAdjusted | — |
| AMOUNT_ADJUSTED_PENDING | PaymentScheduleAmountAdjustedPending | — |
| AMOUNT_ADJUSTED_PENDING | PaymentScheduleAppliedAmountAdjustedPending | — |
| AMOUNT_ADJUSTED_PENDING | PaymentSchedulesAmountAdjustedPending | — |
| AMOUNT_APPLIED | PaymentScheduleAmountApplied | — |
| AMOUNT_APPLIED | PaymentScheduleAppliedAmountApplied | — |
| AMOUNT_APPLIED | PaymentSchedulesAmountApplied | — |
| AMOUNT_CREDITED | PaymentScheduleAmountCredited | — |
| AMOUNT_CREDITED | PaymentScheduleAppliedAmountCredited | — |
| AMOUNT_CREDITED | PaymentSchedulesAmountCredited | — |
| AMOUNT_DUE_ORIGINAL | PaymentScheduleAmountDueOriginal | — |
| AMOUNT_DUE_ORIGINAL | PaymentScheduleAppliedAmountDueOriginal | — |
| AMOUNT_DUE_ORIGINAL | PaymentSchedulesAmountDueOriginal | — |
| AMOUNT_DUE_REMAINING | PaymentScheduleAmountDueRemaining | — |
| AMOUNT_DUE_REMAINING | PaymentScheduleAppliedAmountDueRemaining | — |
| AMOUNT_DUE_REMAINING | PaymentSchedulesAmountDueRemaining | — |
| AMOUNT_IN_DISPUTE | PaymentScheduleAmountInDispute | — |
| AMOUNT_IN_DISPUTE | PaymentScheduleAppliedAmountInDispute | — |
| AMOUNT_IN_DISPUTE | PaymentSchedulesAmountInDispute | — |
| AMOUNT_LINE_ITEMS_ORIGINAL | PaymentScheduleAmountLineItemsOriginal | — |
| AMOUNT_LINE_ITEMS_ORIGINAL | PaymentScheduleAppliedAmountLineItemsOriginal | — |
| AMOUNT_LINE_ITEMS_ORIGINAL | PaymentSchedulesAmountLineItemsOriginal | — |
| AMOUNT_LINE_ITEMS_REMAINING | PaymentScheduleAmountLineItemsRemaining | — |
| AMOUNT_LINE_ITEMS_REMAINING | PaymentScheduleAppliedAmountLineItemsRemaining | — |
| AMOUNT_LINE_ITEMS_REMAINING | PaymentSchedulesAmountLineItemsRemaining | — |
| AMOUNT_ON_ACCOUNT | PaymentScheduleAmountOnAccount | ✅ |
| AMOUNT_ON_ACCOUNT | PaymentScheduleAppliedAmountOnAccount | — |
| AMOUNT_ON_ACCOUNT | PaymentSchedulesAmountOnAccount | — |
| AMOUNT_OTHER_ACCOUNT | PaymentScheduleAmountOtherAccount | — |
| AMOUNT_OTHER_ACCOUNT | PaymentScheduleAppliedAmountOtherAccount | — |
| AMOUNT_OTHER_ACCOUNT | PaymentSchedulesAmountOtherAccount | — |
| ASSOCIATED_CASH_RECEIPT_ID | PaymentScheduleAppliedAssociatedCashReceiptId | — |
| ASSOCIATED_CASH_RECEIPT_ID | PaymentScheduleAssociatedCashReceiptId | — |
| ASSOCIATED_CASH_RECEIPT_ID | PaymentSchedulesAssociatedCashReceiptId | — |
| BR_AMOUNT_ASSIGNED | PaymentScheduleAppliedBrAmountAssigned | — |
| BR_AMOUNT_ASSIGNED | PaymentScheduleBrAmountAssigned | — |
| BR_AMOUNT_ASSIGNED | PaymentSchedulesBrAmountAssigned | — |
| CALL_DATE_LAST | PaymentScheduleAppliedCallDateLast | — |
| CALL_DATE_LAST | PaymentScheduleCallDateLast | — |
| CALL_DATE_LAST | PaymentSchedulesCallDateLast | — |
| CASH_APPLIED_AMOUNT_LAST | PaymentScheduleAppliedCashAppliedAmountLast | — |
| CASH_APPLIED_AMOUNT_LAST | PaymentScheduleCashAppliedAmountLast | — |
| CASH_APPLIED_AMOUNT_LAST | PaymentSchedulesCashAppliedAmountLast | — |
| CASH_APPLIED_DATE_LAST | PaymentScheduleAppliedCashAppliedDateLast | — |
| CASH_APPLIED_DATE_LAST | PaymentScheduleCashAppliedDateLast | — |
| CASH_APPLIED_DATE_LAST | PaymentSchedulesCashAppliedDateLast | — |
| CASH_APPLIED_ID_LAST | PaymentScheduleAppliedCashAppliedIdLast | — |
| CASH_APPLIED_ID_LAST | PaymentScheduleCashAppliedIdLast | — |
| CASH_APPLIED_ID_LAST | PaymentSchedulesCashAppliedIdLast | — |
| CASH_APPLIED_STATUS_LAST | PaymentScheduleAppliedCashAppliedStatusLast | — |
| CASH_APPLIED_STATUS_LAST | PaymentScheduleCashAppliedStatusLast | — |
| CASH_APPLIED_STATUS_LAST | PaymentSchedulesCashAppliedStatusLast | — |
| CASH_GL_DATE_LAST | PaymentScheduleAppliedCashGlDateLast | — |
| CASH_GL_DATE_LAST | PaymentScheduleCashGlDateLast | — |
| CASH_GL_DATE_LAST | PaymentSchedulesCashGlDateLast | — |
| CASH_RECEIPT_AMOUNT_LAST | PaymentScheduleAppliedCashReceiptAmountLast | — |
| CASH_RECEIPT_AMOUNT_LAST | PaymentScheduleCashReceiptAmountLast | — |
| CASH_RECEIPT_AMOUNT_LAST | PaymentSchedulesCashReceiptAmountLast | — |
| CASH_RECEIPT_DATE_LAST | PaymentScheduleAppliedCashReceiptDateLast | — |
| CASH_RECEIPT_DATE_LAST | PaymentScheduleCashReceiptDateLast | — |
| CASH_RECEIPT_DATE_LAST | PaymentSchedulesCashReceiptDateLast | — |
| CASH_RECEIPT_ID | PaymentScheduleAppliedCashReceiptId | — |
| CASH_RECEIPT_ID | PaymentScheduleCashReceiptId | — |
| CASH_RECEIPT_ID | PaymentSchedulesCashReceiptId1 | — |
| CASH_RECEIPT_ID_LAST | PaymentScheduleAppliedCashReceiptIdLast | — |
| CASH_RECEIPT_ID_LAST | PaymentScheduleCashReceiptIdLast | — |
| CASH_RECEIPT_ID_LAST | PaymentSchedulesCashReceiptIdLast | — |
| CASH_RECEIPT_STATUS_LAST | PaymentScheduleAppliedCashReceiptStatusLast | — |
| CASH_RECEIPT_STATUS_LAST | PaymentScheduleCashReceiptStatusLast | — |
| CASH_RECEIPT_STATUS_LAST | PaymentSchedulesCashReceiptStatusLast | — |
| CLASS | PaymentScheduleAppliedPaymentScheduleClass | — |
| CLASS | PaymentSchedulePaymentScheduleClass | — |
| CLASS | PaymentSchedulesPaymentScheduleClass1 | — |
| COLLECTOR_LAST | PaymentScheduleAppliedCollectorLast | — |
| COLLECTOR_LAST | PaymentScheduleCollectorLast | — |
| COLLECTOR_LAST | PaymentSchedulesCollectorLast | — |
| CONS_INV_ID | PaymentScheduleAppliedConsInvId | — |
| CONS_INV_ID | PaymentScheduleConsInvId | — |
| CONS_INV_ID | PaymentSchedulesConsInvId | — |
| CONS_INV_ID_REV | PaymentScheduleAppliedConsInvIdRev | — |
| CONS_INV_ID_REV | PaymentScheduleConsInvIdRev | — |
| CONS_INV_ID_REV | PaymentSchedulesConsInvIdRev | — |
| CREATED_BY | PaymentScheduleAppliedCreatedBy | — |
| CREATED_BY | PaymentScheduleCreatedBy | — |
| CREATED_BY | PaymentSchedulesCreatedBy | — |
| CREATION_DATE | PaymentScheduleAppliedCreationDate | — |
| CREATION_DATE | PaymentScheduleCreationDate | — |
| CREATION_DATE | PaymentSchedulesCreationDate | — |
| CUST_TRX_TYPE_SEQ_ID | PaymentScheduleAppliedCustTrxTypeSeqId | — |
| CUST_TRX_TYPE_SEQ_ID | PaymentScheduleCustTrxTypeSeqId | — |
| CUST_TRX_TYPE_SEQ_ID | PaymentSchedulesCustTrxTypeSeqId | — |
| CUSTOMER_ID | PaymentScheduleAppliedCustomerId | — |
| CUSTOMER_ID | PaymentScheduleCustomerId | — |
| CUSTOMER_ID | PaymentSchedulesCustomerId | — |
| CUSTOMER_SITE_USE_ID | PaymentScheduleAppliedCustomerSiteUseId | — |
| CUSTOMER_SITE_USE_ID | PaymentScheduleCustomerSiteUseId | — |
| CUSTOMER_SITE_USE_ID | PaymentSchedulesCustomerSiteUseId | — |
| CUSTOMER_TRX_ID | PaymentScheduleAppliedCustomerTrxId | — |
| CUSTOMER_TRX_ID | PaymentScheduleCustomerTrxId | — |
| CUSTOMER_TRX_ID | PaymentSchedulesCustomerTrxId | — |
| DISCOUNT_DATE | PaymentScheduleAppliedDiscountDate | — |
| DISCOUNT_DATE | PaymentScheduleDiscountDate | — |
| DISCOUNT_DATE | PaymentSchedulesDiscountDate | — |
| DISCOUNT_ORIGINAL | PaymentScheduleAppliedDiscountOriginal | — |
| DISCOUNT_ORIGINAL | PaymentScheduleDiscountOriginal | — |
| DISCOUNT_ORIGINAL | PaymentSchedulesDiscountOriginal | — |
| DISCOUNT_REMAINING | PaymentScheduleAppliedDiscountRemaining | — |
| DISCOUNT_REMAINING | PaymentScheduleDiscountRemaining | — |
| DISCOUNT_REMAINING | PaymentSchedulesDiscountRemaining | — |
| DISCOUNT_TAKEN_EARNED | PaymentScheduleAppliedDiscountTakenEarned | — |
| DISCOUNT_TAKEN_EARNED | PaymentScheduleDiscountTakenEarned | — |
| DISCOUNT_TAKEN_EARNED | PaymentSchedulesDiscountTakenEarned | — |
| DISCOUNT_TAKEN_UNEARNED | PaymentScheduleAppliedDiscountTakenUnearned | — |
| DISCOUNT_TAKEN_UNEARNED | PaymentScheduleDiscountTakenUnearned | — |
| DISCOUNT_TAKEN_UNEARNED | PaymentSchedulesDiscountTakenUnearned | — |
| DISPUTE_DATE | PaymentScheduleAppliedDisputeDate | — |
| DISPUTE_DATE | PaymentScheduleDisputeDate | — |
| DISPUTE_DATE | PaymentSchedulesDisputeDate | — |
| DUE_DATE | PaymentScheduleAppliedDueDate | — |
| DUE_DATE | PaymentScheduleDueDate | — |
| DUE_DATE | PaymentSchedulesDueDate | ✅ |
| DUNNING_LEVEL_OVERRIDE_DATE | PaymentScheduleAppliedDunningLevelOverrideDate | — |
| DUNNING_LEVEL_OVERRIDE_DATE | PaymentScheduleDunningLevelOverrideDate | — |
| DUNNING_LEVEL_OVERRIDE_DATE | PaymentSchedulesDunningLevelOverrideDate | — |
| EXCHANGE_DATE | PaymentScheduleAppliedExchangeDate | — |
| EXCHANGE_DATE | PaymentScheduleExchangeDate | — |
| EXCHANGE_DATE | PaymentSchedulesExchangeDate | — |
| EXCHANGE_RATE | PaymentScheduleAppliedExchangeRate | — |
| EXCHANGE_RATE | PaymentScheduleExchangeRate | — |
| EXCHANGE_RATE | PaymentSchedulesExchangeRate | — |
| EXCHANGE_RATE_TYPE | PaymentScheduleAppliedExchangeRateType | — |
| EXCHANGE_RATE_TYPE | PaymentScheduleExchangeRateType | — |
| EXCHANGE_RATE_TYPE | PaymentSchedulesExchangeRateType | — |
| EXCLUDE_FROM_CONS_BILL_FLAG | PaymentScheduleAppliedExcludeFromConsBillFlag | — |
| EXCLUDE_FROM_CONS_BILL_FLAG | PaymentScheduleExcludeFromConsBillFlag | — |
| EXCLUDE_FROM_CONS_BILL_FLAG | PaymentSchedulesExcludeFromConsBillFlag | — |
| EXCLUDE_FROM_DUNNING_FLAG | PaymentScheduleAppliedExcludeFromDunningFlag | — |
| EXCLUDE_FROM_DUNNING_FLAG | PaymentScheduleExcludeFromDunningFlag | — |
| EXCLUDE_FROM_DUNNING_FLAG | PaymentSchedulesExcludeFromDunningFlag | — |
| FOLLOW_UP_CODE_LAST | PaymentScheduleAppliedFollowUpCodeLast | — |
| FOLLOW_UP_CODE_LAST | PaymentScheduleFollowUpCodeLast | — |
| FOLLOW_UP_CODE_LAST | PaymentSchedulesFollowUpCodeLast | — |
| FOLLOW_UP_DATE_LAST | PaymentScheduleAppliedFollowUpDateLast | — |
| FOLLOW_UP_DATE_LAST | PaymentScheduleFollowUpDateLast | — |
| FOLLOW_UP_DATE_LAST | PaymentSchedulesFollowUpDateLast | — |
| FREIGHT_ORIGINAL | PaymentScheduleAppliedFreightOriginal | — |
| FREIGHT_ORIGINAL | PaymentScheduleFreightOriginal | — |
| FREIGHT_ORIGINAL | PaymentSchedulesFreightOriginal | — |
| FREIGHT_REMAINING | PaymentScheduleAppliedFreightRemaining | — |
| FREIGHT_REMAINING | PaymentScheduleFreightRemaining | — |
| FREIGHT_REMAINING | PaymentSchedulesFreightRemaining | — |
| GL_DATE | PaymentScheduleAppliedGlDate | — |
| GL_DATE | PaymentScheduleGlDate | — |
| GL_DATE | PaymentSchedulesGlDate | — |
| GL_DATE_CLOSED | PaymentScheduleAppliedGlDateClosed | — |
| GL_DATE_CLOSED | PaymentScheduleGlDateClosed | — |
| GL_DATE_CLOSED | PaymentSchedulesGlDateClosed | — |
| IN_COLLECTION | PaymentScheduleAppliedInCollection | — |
| IN_COLLECTION | PaymentScheduleInCollection | — |
| IN_COLLECTION | PaymentSchedulesInCollection | — |
| INVOICE_CURRENCY_CODE | PaymentScheduleAppliedInvoiceCurrencyCode | — |
| INVOICE_CURRENCY_CODE | PaymentScheduleInvoiceCurrencyCode | — |
| INVOICE_CURRENCY_CODE | PaymentSchedulesInvoiceCurrencyCode | — |
| LAST_CHARGE_DATE | PaymentScheduleAppliedLastChargeDate | — |
| LAST_CHARGE_DATE | PaymentScheduleLastChargeDate | — |
| LAST_CHARGE_DATE | PaymentSchedulesLastChargeDate | — |
| LAST_UPDATE_DATE | PaymentScheduleAppliedLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | PaymentScheduleLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | PaymentSchedulesLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PaymentScheduleAppliedLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | PaymentScheduleLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | PaymentSchedulesLastUpdateLogin | — |
| LAST_UPDATED_BY | PaymentScheduleAppliedLastUpdatedBy | — |
| LAST_UPDATED_BY | PaymentScheduleLastUpdatedBy | — |
| LAST_UPDATED_BY | PaymentSchedulesLastUpdatedBy | — |
| NUMBER_OF_DUE_DATES | PaymentScheduleAppliedNumberOfDueDates | — |
| NUMBER_OF_DUE_DATES | PaymentScheduleNumberOfDueDates | — |
| NUMBER_OF_DUE_DATES | PaymentSchedulesNumberOfDueDates | — |
| OBJECT_VERSION_NUMBER | PaymentScheduleAppliedObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | PaymentScheduleObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | PaymentSchedulesObjectVersionNumber | — |
| ORG_ID | PaymentScheduleAppliedOrgId | — |
| ORG_ID | PaymentScheduleOrgId | — |
| ORG_ID | PaymentSchedulesOrgId | — |
| PAYMENT_APPROVAL | PaymentScheduleAppliedPaymentApproval | — |
| PAYMENT_APPROVAL | PaymentSchedulePaymentApproval | — |
| PAYMENT_APPROVAL | PaymentSchedulesPaymentApproval | — |
| PAYMENT_SCHEDULE_ID | PaymentScheduleAppliedPaymentScheduleId | — |
| PAYMENT_SCHEDULE_ID | PaymentSchedulePaymentScheduleId | — |
| PAYMENT_SCHEDULE_ID | PaymentSchedulesDebitMemoPaymentScheduleId | — |
| PAYMENT_SCHEDULE_ID | PaymentSchedulesPaymentScheduleId | — |
| PROGRAM_APPLICATION_ID | PaymentScheduleAppliedProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | PaymentScheduleProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | PaymentSchedulesProgramApplicationId | — |
| PROGRAM_ID | PaymentScheduleAppliedProgramId | — |
| PROGRAM_ID | PaymentScheduleProgramId | — |
| PROGRAM_ID | PaymentSchedulesProgramId | — |
| PROGRAM_UPDATE_DATE | PaymentScheduleAppliedProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | PaymentScheduleProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | PaymentSchedulesProgramUpdateDate | — |
| PROMISE_AMOUNT_LAST | PaymentScheduleAppliedPromiseAmountLast | — |
| PROMISE_AMOUNT_LAST | PaymentSchedulePromiseAmountLast | — |
| PROMISE_AMOUNT_LAST | PaymentSchedulesPromiseAmountLast | — |
| PROMISE_DATE_LAST | PaymentScheduleAppliedPromiseDateLast | — |
| PROMISE_DATE_LAST | PaymentSchedulePromiseDateLast | — |
| PROMISE_DATE_LAST | PaymentSchedulesPromiseDateLast | — |
| RECEIPT_CONFIRMED_FLAG | PaymentScheduleAppliedReceiptConfirmedFlag | — |
| RECEIPT_CONFIRMED_FLAG | PaymentScheduleReceiptConfirmedFlag | — |
| RECEIPT_CONFIRMED_FLAG | PaymentSchedulesReceiptConfirmedFlag1 | — |
| RECEIVABLES_CHARGES_CHARGED | PaymentScheduleAppliedReceivablesChargesCharged | — |
| RECEIVABLES_CHARGES_CHARGED | PaymentScheduleReceivablesChargesCharged | — |
| RECEIVABLES_CHARGES_CHARGED | PaymentSchedulesReceivablesChargesCharged | — |
| RECEIVABLES_CHARGES_REMAINING | PaymentScheduleAppliedReceivablesChargesRemaining | — |
| RECEIVABLES_CHARGES_REMAINING | PaymentScheduleReceivablesChargesRemaining | — |
| RECEIVABLES_CHARGES_REMAINING | PaymentSchedulesReceivablesChargesRemaining | — |
| REQUEST_ID | PaymentScheduleAppliedRequestId | — |
| REQUEST_ID | PaymentScheduleRequestId | — |
| REQUEST_ID | PaymentSchedulesRequestId | — |
| RESERVED_TYPE | PaymentScheduleAppliedReservedType | — |
| RESERVED_TYPE | PaymentScheduleReservedType | — |
| RESERVED_TYPE | PaymentSchedulesReservedType | — |
| RESERVED_VALUE | PaymentScheduleAppliedReservedValue | — |
| RESERVED_VALUE | PaymentScheduleReservedValue | — |
| RESERVED_VALUE | PaymentSchedulesReservedValue | — |
| REVERSED_CASH_RECEIPT_ID | PaymentScheduleAppliedReversedCashReceiptId | — |
| REVERSED_CASH_RECEIPT_ID | PaymentScheduleReversedCashReceiptId | — |
| REVERSED_CASH_RECEIPT_ID | PaymentSchedulesReversedCashReceiptId | — |
| SECOND_LAST_CHARGE_DATE | PaymentScheduleAppliedSecondLastChargeDate | — |
| SECOND_LAST_CHARGE_DATE | PaymentScheduleSecondLastChargeDate | — |
| SECOND_LAST_CHARGE_DATE | PaymentSchedulesSecondLastChargeDate | — |
| SELECTED_FOR_RECEIPT_BATCH_ID | PaymentScheduleAppliedSelectedForReceiptBatchId | — |
| SELECTED_FOR_RECEIPT_BATCH_ID | PaymentScheduleSelectedForReceiptBatchId | — |
| SELECTED_FOR_RECEIPT_BATCH_ID | PaymentSchedulesSelectedForReceiptBatchId | — |
| STAGED_DUNNING_LEVEL | PaymentScheduleAppliedStagedDunningLevel | — |
| STAGED_DUNNING_LEVEL | PaymentScheduleStagedDunningLevel | — |
| STAGED_DUNNING_LEVEL | PaymentSchedulesStagedDunningLevel | — |
| STATUS | PaymentScheduleAppliedStatus | — |
| STATUS | PaymentScheduleStatus | — |
| STATUS | PaymentSchedulesStatus | — |
| TAX_ORIGINAL | PaymentScheduleAppliedTaxOriginal | — |
| TAX_ORIGINAL | PaymentScheduleTaxOriginal | — |
| TAX_ORIGINAL | PaymentSchedulesTaxOriginal | — |
| TAX_REMAINING | PaymentScheduleAppliedTaxRemaining | — |
| TAX_REMAINING | PaymentScheduleTaxRemaining | — |
| TAX_REMAINING | PaymentSchedulesTaxRemaining | — |
| TERM_ID | PaymentScheduleAppliedTermId | — |
| TERM_ID | PaymentScheduleTermId | — |
| TERM_ID | PaymentSchedulesTermId | — |
| TERMS_SEQUENCE_NUMBER | PaymentScheduleAppliedTermsSequenceNumber | — |
| TERMS_SEQUENCE_NUMBER | PaymentScheduleTermsSequenceNumber | — |
| TERMS_SEQUENCE_NUMBER | PaymentSchedulesTermsSequenceNumber | — |
| TRX_DATE | PaymentScheduleAppliedTrxDate | — |
| TRX_DATE | PaymentScheduleTrxDate | — |
| TRX_DATE | PaymentSchedulesTrxDate | — |
| TRX_NUMBER | PaymentScheduleAppliedTrxNumber | — |
| TRX_NUMBER | PaymentScheduleTrxNumber | — |
| TRX_NUMBER | PaymentSchedulesTrxNumber | — |

### [[receiptapplicationpvo|ReceiptApplicationPVO]] (AR · BICC: 3/187)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_DUE_REMAINING | PaymentScheduleAcctdAmountDueRemaining | — |
| ACCTD_AMOUNT_DUE_REMAINING | PaymentSchedulesAcctdAmountDueRemaining | — |
| ACTIVE_CLAIM_FLAG | PaymentScheduleActiveClaimFlag | — |
| ACTIVE_CLAIM_FLAG | PaymentSchedulesActiveClaimFlag | — |
| ACTUAL_DATE_CLOSED | PaymentScheduleActualDateClosed | — |
| ACTUAL_DATE_CLOSED | PaymentSchedulesActualDateClosed | — |
| ADJUSTMENT_AMOUNT_LAST | PaymentScheduleAdjustmentAmountLast | — |
| ADJUSTMENT_AMOUNT_LAST | PaymentSchedulesAdjustmentAmountLast | — |
| ADJUSTMENT_DATE_LAST | PaymentScheduleAdjustmentDateLast | — |
| ADJUSTMENT_DATE_LAST | PaymentSchedulesAdjustmentDateLast | — |
| ADJUSTMENT_GL_DATE_LAST | PaymentScheduleAdjustmentGlDateLast | — |
| ADJUSTMENT_GL_DATE_LAST | PaymentSchedulesAdjustmentGlDateLast | — |
| ADJUSTMENT_ID_LAST | PaymentScheduleAdjustmentIdLast | — |
| ADJUSTMENT_ID_LAST | PaymentSchedulesAdjustmentIdLast | — |
| AMOUNT_ADJUSTED | PaymentScheduleAmountAdjusted | — |
| AMOUNT_ADJUSTED | PaymentSchedulesAmountAdjusted | — |
| AMOUNT_ADJUSTED_PENDING | PaymentScheduleAmountAdjustedPending | — |
| AMOUNT_ADJUSTED_PENDING | PaymentSchedulesAmountAdjustedPending | — |
| AMOUNT_APPLIED | PaymentScheduleAmountApplied | — |
| AMOUNT_APPLIED | PaymentSchedulesAmountApplied | — |
| AMOUNT_CREDITED | PaymentScheduleAmountCredited | — |
| AMOUNT_CREDITED | PaymentSchedulesAmountCredited | — |
| AMOUNT_DUE_ORIGINAL | PaymentScheduleAmountDueOriginal | — |
| AMOUNT_DUE_ORIGINAL | PaymentSchedulesAmountDueOriginal | — |
| AMOUNT_DUE_REMAINING | PaymentScheduleAmountDueRemaining | — |
| AMOUNT_DUE_REMAINING | PaymentSchedulesAmountDueRemaining | — |
| AMOUNT_IN_DISPUTE | PaymentScheduleAmountInDispute | — |
| AMOUNT_IN_DISPUTE | PaymentSchedulesAmountInDispute | — |
| AMOUNT_LINE_ITEMS_ORIGINAL | PaymentScheduleAmountLineItemsOriginal | — |
| AMOUNT_LINE_ITEMS_ORIGINAL | PaymentSchedulesAmountLineItemsOriginal | — |
| AMOUNT_LINE_ITEMS_REMAINING | PaymentScheduleAmountLineItemsRemaining | — |
| AMOUNT_LINE_ITEMS_REMAINING | PaymentSchedulesAmountLineItemsRemaining | — |
| AMOUNT_ON_ACCOUNT | PaymentScheduleAmountOnAccount | — |
| AMOUNT_ON_ACCOUNT | PaymentSchedulesAmountOnAccount | — |
| AMOUNT_OTHER_ACCOUNT | PaymentScheduleAmountOtherAccount | — |
| AMOUNT_OTHER_ACCOUNT | PaymentSchedulesAmountOtherAccount | — |
| ASSOCIATED_CASH_RECEIPT_ID | PaymentScheduleAssociatedCashReceiptId | — |
| ASSOCIATED_CASH_RECEIPT_ID | PaymentSchedulesAssociatedCashReceiptId | — |
| BR_AMOUNT_ASSIGNED | PaymentScheduleBrAmountAssigned | — |
| BR_AMOUNT_ASSIGNED | PaymentSchedulesBrAmountAssigned | — |
| CALL_DATE_LAST | PaymentScheduleCallDateLast | — |
| CALL_DATE_LAST | PaymentSchedulesCallDateLast | — |
| CASH_APPLIED_AMOUNT_LAST | PaymentScheduleCashAppliedAmountLast | — |
| CASH_APPLIED_AMOUNT_LAST | PaymentSchedulesCashAppliedAmountLast | — |
| CASH_APPLIED_DATE_LAST | PaymentScheduleCashAppliedDateLast | — |
| CASH_APPLIED_DATE_LAST | PaymentSchedulesCashAppliedDateLast | — |
| CASH_APPLIED_ID_LAST | PaymentScheduleCashAppliedIdLast | — |
| CASH_APPLIED_ID_LAST | PaymentSchedulesCashAppliedIdLast | — |
| CASH_APPLIED_STATUS_LAST | PaymentScheduleCashAppliedStatusLast | — |
| CASH_APPLIED_STATUS_LAST | PaymentSchedulesCashAppliedStatusLast | — |
| CASH_GL_DATE_LAST | PaymentScheduleCashGlDateLast | — |
| CASH_GL_DATE_LAST | PaymentSchedulesCashGlDateLast | — |
| CASH_RECEIPT_AMOUNT_LAST | PaymentScheduleCashReceiptAmountLast | — |
| CASH_RECEIPT_AMOUNT_LAST | PaymentSchedulesCashReceiptAmountLast | — |
| CASH_RECEIPT_DATE_LAST | PaymentScheduleCashReceiptDateLast | — |
| CASH_RECEIPT_DATE_LAST | PaymentSchedulesCashReceiptDateLast | — |
| CASH_RECEIPT_ID | PaymentScheduleCashReceiptId | — |
| CASH_RECEIPT_ID | PaymentSchedulesCashReceiptId1 | — |
| CASH_RECEIPT_ID_LAST | PaymentScheduleCashReceiptIdLast | — |
| CASH_RECEIPT_ID_LAST | PaymentSchedulesCashReceiptIdLast | — |
| CASH_RECEIPT_STATUS_LAST | PaymentScheduleCashReceiptStatusLast | — |
| CASH_RECEIPT_STATUS_LAST | PaymentSchedulesCashReceiptStatusLast | — |
| CLASS | PaymentSchedulePaymentScheduleClass | — |
| CLASS | PaymentSchedulesPaymentScheduleClass1 | — |
| COLLECTOR_LAST | PaymentScheduleCollectorLast | — |
| COLLECTOR_LAST | PaymentSchedulesCollectorLast | — |
| CONS_INV_ID | PaymentScheduleConsInvId | — |
| CONS_INV_ID | PaymentSchedulesConsInvId | — |
| CONS_INV_ID_REV | PaymentScheduleConsInvIdRev | — |
| CONS_INV_ID_REV | PaymentSchedulesConsInvIdRev | — |
| CREATED_BY | PaymentScheduleCreatedBy | — |
| CREATED_BY | PaymentSchedulesCreatedBy | — |
| CREATION_DATE | PaymentScheduleCreationDate | — |
| CREATION_DATE | PaymentSchedulesCreationDate | — |
| CUST_TRX_TYPE_SEQ_ID | PaymentScheduleCustTrxTypeSeqId | — |
| CUST_TRX_TYPE_SEQ_ID | PaymentSchedulesCustTrxTypeSeqId | — |
| CUSTOMER_ID | PaymentScheduleCustomerId | — |
| CUSTOMER_ID | PaymentSchedulesCustomerId | — |
| CUSTOMER_SITE_USE_ID | PaymentScheduleCustomerSiteUseId | — |
| CUSTOMER_SITE_USE_ID | PaymentSchedulesCustomerSiteUseId | — |
| CUSTOMER_TRX_ID | PaymentScheduleCustomerTrxId | — |
| CUSTOMER_TRX_ID | PaymentSchedulesCustomerTrxId | — |
| DISCOUNT_DATE | PaymentScheduleDiscountDate | — |
| DISCOUNT_DATE | PaymentSchedulesDiscountDate | — |
| DISCOUNT_ORIGINAL | PaymentScheduleDiscountOriginal | — |
| DISCOUNT_ORIGINAL | PaymentSchedulesDiscountOriginal | — |
| DISCOUNT_REMAINING | PaymentScheduleDiscountRemaining | — |
| DISCOUNT_REMAINING | PaymentSchedulesDiscountRemaining | — |
| DISCOUNT_TAKEN_EARNED | PaymentScheduleDiscountTakenEarned | — |
| DISCOUNT_TAKEN_EARNED | PaymentSchedulesDiscountTakenEarned | — |
| DISCOUNT_TAKEN_UNEARNED | PaymentScheduleDiscountTakenUnearned | — |
| DISCOUNT_TAKEN_UNEARNED | PaymentSchedulesDiscountTakenUnearned | — |
| DISPUTE_DATE | PaymentScheduleDisputeDate | — |
| DISPUTE_DATE | PaymentSchedulesDisputeDate | — |
| DUE_DATE | PaymentScheduleDueDate | — |
| DUE_DATE | PaymentSchedulesDueDate | ✅ |
| DUNNING_LEVEL_OVERRIDE_DATE | PaymentScheduleDunningLevelOverrideDate | — |
| DUNNING_LEVEL_OVERRIDE_DATE | PaymentSchedulesDunningLevelOverrideDate | — |
| EXCHANGE_DATE | PaymentScheduleExchangeDate | — |
| EXCHANGE_DATE | PaymentSchedulesExchangeDate | — |
| EXCHANGE_RATE | PaymentScheduleExchangeRate | — |
| EXCHANGE_RATE | PaymentSchedulesExchangeRate | — |
| EXCHANGE_RATE_TYPE | PaymentScheduleExchangeRateType | — |
| EXCHANGE_RATE_TYPE | PaymentSchedulesExchangeRateType | — |
| EXCLUDE_FROM_CONS_BILL_FLAG | PaymentScheduleExcludeFromConsBillFlag | — |
| EXCLUDE_FROM_CONS_BILL_FLAG | PaymentSchedulesExcludeFromConsBillFlag | — |
| EXCLUDE_FROM_DUNNING_FLAG | PaymentScheduleExcludeFromDunningFlag | — |
| EXCLUDE_FROM_DUNNING_FLAG | PaymentSchedulesExcludeFromDunningFlag | — |
| FOLLOW_UP_CODE_LAST | PaymentScheduleFollowUpCodeLast | — |
| FOLLOW_UP_CODE_LAST | PaymentSchedulesFollowUpCodeLast | — |
| FOLLOW_UP_DATE_LAST | PaymentScheduleFollowUpDateLast | — |
| FOLLOW_UP_DATE_LAST | PaymentSchedulesFollowUpDateLast | — |
| FREIGHT_ORIGINAL | PaymentScheduleFreightOriginal | — |
| FREIGHT_ORIGINAL | PaymentSchedulesFreightOriginal | — |
| FREIGHT_REMAINING | PaymentScheduleFreightRemaining | — |
| FREIGHT_REMAINING | PaymentSchedulesFreightRemaining | — |
| GL_DATE | PaymentScheduleGlDate | — |
| GL_DATE | PaymentSchedulesGlDate | — |
| GL_DATE_CLOSED | PaymentScheduleGlDateClosed | — |
| GL_DATE_CLOSED | PaymentSchedulesGlDateClosed | — |
| IN_COLLECTION | PaymentScheduleInCollection | — |
| IN_COLLECTION | PaymentSchedulesInCollection | — |
| INVOICE_CURRENCY_CODE | PaymentScheduleInvoiceCurrencyCode | — |
| INVOICE_CURRENCY_CODE | PaymentSchedulesInvoiceCurrencyCode | — |
| LAST_CHARGE_DATE | PaymentScheduleLastChargeDate | — |
| LAST_CHARGE_DATE | PaymentSchedulesLastChargeDate | — |
| LAST_UPDATE_DATE | PaymentScheduleLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | PaymentSchedulesLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PaymentScheduleLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | PaymentSchedulesLastUpdateLogin | — |
| LAST_UPDATED_BY | PaymentScheduleLastUpdatedBy | — |
| LAST_UPDATED_BY | PaymentSchedulesLastUpdatedBy | — |
| NUMBER_OF_DUE_DATES | PaymentScheduleNumberOfDueDates | — |
| NUMBER_OF_DUE_DATES | PaymentSchedulesNumberOfDueDates | — |
| OBJECT_VERSION_NUMBER | PaymentScheduleObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | PaymentSchedulesObjectVersionNumber | — |
| ORG_ID | PaymentScheduleOrgId | — |
| ORG_ID | PaymentSchedulesOrgId | — |
| PAYMENT_APPROVAL | PaymentSchedulePaymentApproval | — |
| PAYMENT_APPROVAL | PaymentSchedulesPaymentApproval | — |
| PAYMENT_SCHEDULE_ID | PaymentSchedulePaymentScheduleId | — |
| PAYMENT_SCHEDULE_ID | PaymentSchedulesDebitMemoPaymentScheduleId | — |
| PAYMENT_SCHEDULE_ID | PaymentSchedulesPaymentScheduleId | — |
| PROGRAM_APPLICATION_ID | PaymentScheduleProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | PaymentSchedulesProgramApplicationId | — |
| PROGRAM_ID | PaymentScheduleProgramId | — |
| PROGRAM_ID | PaymentSchedulesProgramId | — |
| PROGRAM_UPDATE_DATE | PaymentScheduleProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | PaymentSchedulesProgramUpdateDate | — |
| PROMISE_AMOUNT_LAST | PaymentSchedulePromiseAmountLast | — |
| PROMISE_AMOUNT_LAST | PaymentSchedulesPromiseAmountLast | — |
| PROMISE_DATE_LAST | PaymentSchedulePromiseDateLast | — |
| PROMISE_DATE_LAST | PaymentSchedulesPromiseDateLast | — |
| RECEIPT_CONFIRMED_FLAG | PaymentScheduleReceiptConfirmedFlag | — |
| RECEIPT_CONFIRMED_FLAG | PaymentSchedulesReceiptConfirmedFlag1 | — |
| RECEIVABLES_CHARGES_CHARGED | PaymentScheduleReceivablesChargesCharged | — |
| RECEIVABLES_CHARGES_CHARGED | PaymentSchedulesReceivablesChargesCharged | — |
| RECEIVABLES_CHARGES_REMAINING | PaymentScheduleReceivablesChargesRemaining | — |
| RECEIVABLES_CHARGES_REMAINING | PaymentSchedulesReceivablesChargesRemaining | — |
| REQUEST_ID | PaymentScheduleRequestId | — |
| REQUEST_ID | PaymentSchedulesRequestId | — |
| RESERVED_TYPE | PaymentScheduleReservedType | — |
| RESERVED_TYPE | PaymentSchedulesReservedType | — |
| RESERVED_VALUE | PaymentScheduleReservedValue | — |
| RESERVED_VALUE | PaymentSchedulesReservedValue | — |
| REVERSED_CASH_RECEIPT_ID | PaymentScheduleReversedCashReceiptId | — |
| REVERSED_CASH_RECEIPT_ID | PaymentSchedulesReversedCashReceiptId | — |
| SECOND_LAST_CHARGE_DATE | PaymentScheduleSecondLastChargeDate | — |
| SECOND_LAST_CHARGE_DATE | PaymentSchedulesSecondLastChargeDate | — |
| SELECTED_FOR_RECEIPT_BATCH_ID | PaymentScheduleSelectedForReceiptBatchId | — |
| SELECTED_FOR_RECEIPT_BATCH_ID | PaymentSchedulesSelectedForReceiptBatchId | — |
| STAGED_DUNNING_LEVEL | PaymentScheduleStagedDunningLevel | — |
| STAGED_DUNNING_LEVEL | PaymentSchedulesStagedDunningLevel | — |
| STATUS | PaymentScheduleStatus | — |
| STATUS | PaymentSchedulesStatus | — |
| TAX_ORIGINAL | PaymentScheduleTaxOriginal | — |
| TAX_ORIGINAL | PaymentSchedulesTaxOriginal | — |
| TAX_REMAINING | PaymentScheduleTaxRemaining | — |
| TAX_REMAINING | PaymentSchedulesTaxRemaining | — |
| TERM_ID | PaymentScheduleTermId | — |
| TERM_ID | PaymentSchedulesTermId | — |
| TERMS_SEQUENCE_NUMBER | PaymentScheduleTermsSequenceNumber | — |
| TERMS_SEQUENCE_NUMBER | PaymentSchedulesTermsSequenceNumber | — |
| TRX_DATE | PaymentScheduleTrxDate | — |
| TRX_DATE | PaymentSchedulesTrxDate | — |
| TRX_NUMBER | PaymentScheduleTrxNumber | — |
| TRX_NUMBER | PaymentSchedulesTrxNumber | — |

### [[receiptheaderpvo|ReceiptHeaderPVO]] (AR · BICC: 6/93)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_DUE_REMAINING | PaymentScheduleAcctdAmountDueRemaining | — |
| ACTIVE_CLAIM_FLAG | PaymentScheduleActiveClaimFlag | — |
| ACTUAL_DATE_CLOSED | PaymentScheduleActualDateClosed | — |
| ADJUSTMENT_AMOUNT_LAST | PaymentScheduleAdjustmentAmountLast | — |
| ADJUSTMENT_DATE_LAST | PaymentScheduleAdjustmentDateLast | — |
| ADJUSTMENT_GL_DATE_LAST | PaymentScheduleAdjustmentGlDateLast | — |
| ADJUSTMENT_ID_LAST | PaymentScheduleAdjustmentIdLast | — |
| AMOUNT_ADJUSTED | PaymentScheduleAmountAdjusted | — |
| AMOUNT_ADJUSTED_PENDING | PaymentScheduleAmountAdjustedPending | — |
| AMOUNT_APPLIED | PaymentScheduleAmountApplied | ✅ |
| AMOUNT_CREDITED | PaymentScheduleAmountCredited | — |
| AMOUNT_DUE_ORIGINAL | PaymentScheduleAmountDueOriginal | ✅ |
| AMOUNT_DUE_REMAINING | PaymentScheduleAmountDueRemaining | ✅ |
| AMOUNT_IN_DISPUTE | PaymentScheduleAmountInDispute | — |
| AMOUNT_LINE_ITEMS_ORIGINAL | PaymentScheduleAmountLineItemsOriginal | — |
| AMOUNT_LINE_ITEMS_REMAINING | PaymentScheduleAmountLineItemsRemaining | — |
| AMOUNT_ON_ACCOUNT | PaymentScheduleAmountOnAccount | ✅ |
| AMOUNT_OTHER_ACCOUNT | PaymentScheduleAmountOtherAccount | — |
| ASSOCIATED_CASH_RECEIPT_ID | PaymentScheduleAssociatedCashReceiptId | — |
| BR_AMOUNT_ASSIGNED | PaymentScheduleBrAmountAssigned | — |
| CALL_DATE_LAST | PaymentScheduleCallDateLast | — |
| CASH_APPLIED_AMOUNT_LAST | PaymentScheduleCashAppliedAmountLast | — |
| CASH_APPLIED_DATE_LAST | PaymentScheduleCashAppliedDateLast | — |
| CASH_APPLIED_ID_LAST | PaymentScheduleCashAppliedIdLast | — |
| CASH_APPLIED_STATUS_LAST | PaymentScheduleCashAppliedStatusLast | — |
| CASH_GL_DATE_LAST | PaymentScheduleCashGlDateLast | — |
| CASH_RECEIPT_AMOUNT_LAST | PaymentScheduleCashReceiptAmountLast | — |
| CASH_RECEIPT_DATE_LAST | PaymentScheduleCashReceiptDateLast | — |
| CASH_RECEIPT_ID | PaymentScheduleCashReceiptId | — |
| CASH_RECEIPT_ID_LAST | PaymentScheduleCashReceiptIdLast | — |
| CASH_RECEIPT_STATUS_LAST | PaymentScheduleCashReceiptStatusLast | — |
| CLASS | PaymentSchedulePaymentScheduleClass | — |
| COLLECTOR_LAST | PaymentScheduleCollectorLast | — |
| CONS_INV_ID | PaymentScheduleConsInvId | — |
| CONS_INV_ID_REV | PaymentScheduleConsInvIdRev | — |
| CREATED_BY | PaymentScheduleCreatedBy | — |
| CREATION_DATE | PaymentScheduleCreationDate | — |
| CUST_TRX_TYPE_SEQ_ID | PaymentScheduleCustTrxTypeSeqId | — |
| CUSTOMER_ID | PaymentScheduleCustomerId | — |
| CUSTOMER_SITE_USE_ID | PaymentScheduleCustomerSiteUseId | — |
| CUSTOMER_TRX_ID | PaymentScheduleCustomerTrxId | — |
| DISCOUNT_DATE | PaymentScheduleDiscountDate | — |
| DISCOUNT_ORIGINAL | PaymentScheduleDiscountOriginal | — |
| DISCOUNT_REMAINING | PaymentScheduleDiscountRemaining | — |
| DISCOUNT_TAKEN_EARNED | PaymentScheduleDiscountTakenEarned | — |
| DISCOUNT_TAKEN_UNEARNED | PaymentScheduleDiscountTakenUnearned | — |
| DISPUTE_DATE | PaymentScheduleDisputeDate | — |
| DUE_DATE | PaymentScheduleDueDate | ✅ |
| DUNNING_LEVEL_OVERRIDE_DATE | PaymentScheduleDunningLevelOverrideDate | — |
| EXCHANGE_DATE | PaymentScheduleExchangeDate | — |
| EXCHANGE_RATE | PaymentScheduleExchangeRate | — |
| EXCHANGE_RATE_TYPE | PaymentScheduleExchangeRateType | — |
| EXCLUDE_FROM_CONS_BILL_FLAG | PaymentScheduleExcludeFromConsBillFlag | — |
| EXCLUDE_FROM_DUNNING_FLAG | PaymentScheduleExcludeFromDunningFlag | — |
| FOLLOW_UP_CODE_LAST | PaymentScheduleFollowUpCodeLast | — |
| FOLLOW_UP_DATE_LAST | PaymentScheduleFollowUpDateLast | — |
| FREIGHT_ORIGINAL | PaymentScheduleFreightOriginal | — |
| FREIGHT_REMAINING | PaymentScheduleFreightRemaining | — |
| GL_DATE | PaymentScheduleGlDate | — |
| GL_DATE_CLOSED | PaymentScheduleGlDateClosed | — |
| IN_COLLECTION | PaymentScheduleInCollection | — |
| INVOICE_CURRENCY_CODE | PaymentScheduleInvoiceCurrencyCode | — |
| LAST_CHARGE_DATE | PaymentScheduleLastChargeDate | — |
| LAST_UPDATE_DATE | PaymentScheduleLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PaymentScheduleLastUpdateLogin | — |
| LAST_UPDATED_BY | PaymentScheduleLastUpdatedBy | — |
| NUMBER_OF_DUE_DATES | PaymentScheduleNumberOfDueDates | — |
| OBJECT_VERSION_NUMBER | PaymentScheduleObjectVersionNumber | — |
| ORG_ID | PaymentScheduleOrgId | — |
| PAYMENT_APPROVAL | PaymentSchedulePaymentApproval | — |
| PAYMENT_SCHEDULE_ID | PaymentSchedulesPaymentScheduleId | — |
| PROGRAM_APPLICATION_ID | PaymentScheduleProgramApplicationId | — |
| PROGRAM_ID | PaymentScheduleProgramId | — |
| PROGRAM_UPDATE_DATE | PaymentScheduleProgramUpdateDate | — |
| PROMISE_AMOUNT_LAST | PaymentSchedulePromiseAmountLast | — |
| PROMISE_DATE_LAST | PaymentSchedulePromiseDateLast | — |
| RECEIPT_CONFIRMED_FLAG | PaymentScheduleReceiptConfirmedFlag | — |
| RECEIVABLES_CHARGES_CHARGED | PaymentScheduleReceivablesChargesCharged | — |
| RECEIVABLES_CHARGES_REMAINING | PaymentScheduleReceivablesChargesRemaining | — |
| REQUEST_ID | PaymentScheduleRequestId | — |
| RESERVED_TYPE | PaymentScheduleReservedType | — |
| RESERVED_VALUE | PaymentScheduleReservedValue | — |
| REVERSED_CASH_RECEIPT_ID | PaymentScheduleReversedCashReceiptId | — |
| SECOND_LAST_CHARGE_DATE | PaymentScheduleSecondLastChargeDate | — |
| SELECTED_FOR_RECEIPT_BATCH_ID | PaymentScheduleSelectedForReceiptBatchId | — |
| STAGED_DUNNING_LEVEL | PaymentScheduleStagedDunningLevel | — |
| STATUS | PaymentScheduleStatus | — |
| TAX_ORIGINAL | PaymentScheduleTaxOriginal | — |
| TAX_REMAINING | PaymentScheduleTaxRemaining | — |
| TERM_ID | PaymentScheduleTermId | — |
| TERMS_SEQUENCE_NUMBER | PaymentScheduleTermsSequenceNumber | — |
| TRX_DATE | PaymentScheduleTrxDate | — |
| TRX_NUMBER | PaymentScheduleTrxNumber | — |

### [[receipthistorydistributionpvo|ReceiptHistoryDistributionPVO]] (AR · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DUE_DATE | PaymentSchedulesDueDate | ✅ |
| PAYMENT_SCHEDULE_ID | PaymentSchedulesPaymentScheduleId | — |

### [[receipthistorypvo|ReceiptHistoryPVO]] (AR · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DUE_DATE | PaymentSchedulesDueDate | ✅ |
| PAYMENT_SCHEDULE_ID | PaymentSchedulesPaymentScheduleId | — |

### [[transactionheaderbillsreceivablepvo|TransactionHeaderBillsReceivablePVO]] (AR · BICC: 3/93)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_DUE_REMAINING | PaymentScheduleAcctdAmountDueRemaining | ✅ |
| ACTIVE_CLAIM_FLAG | PaymentScheduleActiveClaimFlag | — |
| ACTUAL_DATE_CLOSED | PaymentScheduleActualDateClosed | — |
| ADJUSTMENT_AMOUNT_LAST | PaymentScheduleAdjustmentAmountLast | — |
| ADJUSTMENT_DATE_LAST | PaymentScheduleAdjustmentDateLast | — |
| ADJUSTMENT_GL_DATE_LAST | PaymentScheduleAdjustmentGlDateLast | — |
| ADJUSTMENT_ID_LAST | PaymentScheduleAdjustmentIdLast | — |
| AMOUNT_ADJUSTED | PaymentScheduleAmountAdjusted | — |
| AMOUNT_ADJUSTED_PENDING | PaymentScheduleAmountAdjustedPending | — |
| AMOUNT_APPLIED | PaymentScheduleAmountApplied | — |
| AMOUNT_CREDITED | PaymentScheduleAmountCredited | — |
| AMOUNT_DUE_ORIGINAL | PaymentScheduleAmountDueOriginal | — |
| AMOUNT_DUE_REMAINING | PaymentScheduleAmountDueRemaining | ✅ |
| AMOUNT_IN_DISPUTE | PaymentScheduleAmountInDispute | — |
| AMOUNT_LINE_ITEMS_ORIGINAL | PaymentScheduleAmountLineItemsOriginal | — |
| AMOUNT_LINE_ITEMS_REMAINING | PaymentScheduleAmountLineItemsRemaining | — |
| AMOUNT_ON_ACCOUNT | PaymentScheduleAmountOnAccount | — |
| AMOUNT_OTHER_ACCOUNT | PaymentScheduleAmountOtherAccount | — |
| ASSOCIATED_CASH_RECEIPT_ID | PaymentScheduleAssociatedCashReceiptId | — |
| BR_AMOUNT_ASSIGNED | PaymentScheduleBrAmountAssigned | — |
| CALL_DATE_LAST | PaymentScheduleCallDateLast | — |
| CASH_APPLIED_AMOUNT_LAST | PaymentScheduleCashAppliedAmountLast | — |
| CASH_APPLIED_DATE_LAST | PaymentScheduleCashAppliedDateLast | — |
| CASH_APPLIED_ID_LAST | PaymentScheduleCashAppliedIdLast | — |
| CASH_APPLIED_STATUS_LAST | PaymentScheduleCashAppliedStatusLast | — |
| CASH_GL_DATE_LAST | PaymentScheduleCashGlDateLast | — |
| CASH_RECEIPT_AMOUNT_LAST | PaymentScheduleCashReceiptAmountLast | — |
| CASH_RECEIPT_DATE_LAST | PaymentScheduleCashReceiptDateLast | — |
| CASH_RECEIPT_ID | PaymentScheduleCashReceiptId | — |
| CASH_RECEIPT_ID_LAST | PaymentScheduleCashReceiptIdLast | — |
| CASH_RECEIPT_STATUS_LAST | PaymentScheduleCashReceiptStatusLast | — |
| CLASS | PaymentSchedulePaymentScheduleClass | — |
| COLLECTOR_LAST | PaymentScheduleCollectorLast | — |
| CONS_INV_ID | PaymentScheduleConsInvId | — |
| CONS_INV_ID_REV | PaymentScheduleConsInvIdRev | — |
| CREATED_BY | PaymentScheduleCreatedBy | — |
| CREATION_DATE | PaymentScheduleCreationDate | — |
| CUST_TRX_TYPE_SEQ_ID | PaymentScheduleCustTrxTypeSeqId | — |
| CUSTOMER_ID | PaymentScheduleCustomerId | — |
| CUSTOMER_SITE_USE_ID | PaymentScheduleCustomerSiteUseId | — |
| CUSTOMER_TRX_ID | PaymentScheduleCustomerTrxId | — |
| DISCOUNT_DATE | PaymentScheduleDiscountDate | — |
| DISCOUNT_ORIGINAL | PaymentScheduleDiscountOriginal | — |
| DISCOUNT_REMAINING | PaymentScheduleDiscountRemaining | — |
| DISCOUNT_TAKEN_EARNED | PaymentScheduleDiscountTakenEarned | — |
| DISCOUNT_TAKEN_UNEARNED | PaymentScheduleDiscountTakenUnearned | — |
| DISPUTE_DATE | PaymentScheduleDisputeDate | — |
| DUE_DATE | PaymentScheduleDueDate | — |
| DUNNING_LEVEL_OVERRIDE_DATE | PaymentScheduleDunningLevelOverrideDate | — |
| EXCHANGE_DATE | PaymentScheduleExchangeDate | — |
| EXCHANGE_RATE | PaymentScheduleExchangeRate | — |
| EXCHANGE_RATE_TYPE | PaymentScheduleExchangeRateType | — |
| EXCLUDE_FROM_CONS_BILL_FLAG | PaymentScheduleExcludeFromConsBillFlag | — |
| EXCLUDE_FROM_DUNNING_FLAG | PaymentScheduleExcludeFromDunningFlag | — |
| FOLLOW_UP_CODE_LAST | PaymentScheduleFollowUpCodeLast | — |
| FOLLOW_UP_DATE_LAST | PaymentScheduleFollowUpDateLast | — |
| FREIGHT_ORIGINAL | PaymentScheduleFreightOriginal | — |
| FREIGHT_REMAINING | PaymentScheduleFreightRemaining | — |
| GL_DATE | PaymentScheduleGlDate | — |
| GL_DATE_CLOSED | PaymentScheduleGlDateClosed | — |
| IN_COLLECTION | PaymentScheduleInCollection | — |
| INVOICE_CURRENCY_CODE | PaymentScheduleInvoiceCurrencyCode | — |
| LAST_CHARGE_DATE | PaymentScheduleLastChargeDate | — |
| LAST_UPDATE_DATE | PaymentScheduleLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PaymentScheduleLastUpdateLogin | — |
| LAST_UPDATED_BY | PaymentScheduleLastUpdatedBy | — |
| NUMBER_OF_DUE_DATES | PaymentScheduleNumberOfDueDates | — |
| OBJECT_VERSION_NUMBER | PaymentScheduleObjectVersionNumber | — |
| ORG_ID | PaymentScheduleOrgId | — |
| PAYMENT_APPROVAL | PaymentSchedulePaymentApproval | — |
| PAYMENT_SCHEDULE_ID | PaymentSchedulePaymentScheduleId | — |
| PROGRAM_APPLICATION_ID | PaymentScheduleProgramApplicationId | — |
| PROGRAM_ID | PaymentScheduleProgramId | — |
| PROGRAM_UPDATE_DATE | PaymentScheduleProgramUpdateDate | — |
| PROMISE_AMOUNT_LAST | PaymentSchedulePromiseAmountLast | — |
| PROMISE_DATE_LAST | PaymentSchedulePromiseDateLast | — |
| RECEIPT_CONFIRMED_FLAG | PaymentScheduleReceiptConfirmedFlag | — |
| RECEIVABLES_CHARGES_CHARGED | PaymentScheduleReceivablesChargesCharged | — |
| RECEIVABLES_CHARGES_REMAINING | PaymentScheduleReceivablesChargesRemaining | — |
| REQUEST_ID | PaymentScheduleRequestId | — |
| RESERVED_TYPE | PaymentScheduleReservedType | — |
| RESERVED_VALUE | PaymentScheduleReservedValue | — |
| REVERSED_CASH_RECEIPT_ID | PaymentScheduleReversedCashReceiptId | — |
| SECOND_LAST_CHARGE_DATE | PaymentScheduleSecondLastChargeDate | — |
| SELECTED_FOR_RECEIPT_BATCH_ID | PaymentScheduleSelectedForReceiptBatchId | — |
| STAGED_DUNNING_LEVEL | PaymentScheduleStagedDunningLevel | — |
| STATUS | PaymentScheduleStatus | — |
| TAX_ORIGINAL | PaymentScheduleTaxOriginal | — |
| TAX_REMAINING | PaymentScheduleTaxRemaining | — |
| TERM_ID | PaymentScheduleTermId | — |
| TERMS_SEQUENCE_NUMBER | PaymentScheduleTermsSequenceNumber | — |
| TRX_DATE | PaymentScheduleTrxDate | — |
| TRX_NUMBER | PaymentScheduleTrxNumber | — |

### [[transactionheadernovcpvo|TransactionHeaderNoVCPVO]] (AR · BICC: 1/93)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_DUE_REMAINING | PaymentScheduleAcctdAmountDueRemaining | — |
| ACTIVE_CLAIM_FLAG | PaymentScheduleActiveClaimFlag | — |
| ACTUAL_DATE_CLOSED | PaymentScheduleActualDateClosed | — |
| ADJUSTMENT_AMOUNT_LAST | PaymentScheduleAdjustmentAmountLast | — |
| ADJUSTMENT_DATE_LAST | PaymentScheduleAdjustmentDateLast | — |
| ADJUSTMENT_GL_DATE_LAST | PaymentScheduleAdjustmentGlDateLast | — |
| ADJUSTMENT_ID_LAST | PaymentScheduleAdjustmentIdLast | — |
| AMOUNT_ADJUSTED | PaymentScheduleAmountAdjusted | — |
| AMOUNT_ADJUSTED_PENDING | PaymentScheduleAmountAdjustedPending | — |
| AMOUNT_APPLIED | PaymentScheduleAmountApplied | — |
| AMOUNT_CREDITED | PaymentScheduleAmountCredited | — |
| AMOUNT_DUE_ORIGINAL | PaymentScheduleAmountDueOriginal | — |
| AMOUNT_DUE_REMAINING | PaymentScheduleAmountDueRemaining | — |
| AMOUNT_IN_DISPUTE | PaymentScheduleAmountInDispute | — |
| AMOUNT_LINE_ITEMS_ORIGINAL | PaymentScheduleAmountLineItemsOriginal | — |
| AMOUNT_LINE_ITEMS_REMAINING | PaymentScheduleAmountLineItemsRemaining | — |
| AMOUNT_ON_ACCOUNT | PaymentScheduleAmountOnAccount | — |
| AMOUNT_OTHER_ACCOUNT | PaymentScheduleAmountOtherAccount | — |
| ASSOCIATED_CASH_RECEIPT_ID | PaymentScheduleAssociatedCashReceiptId | — |
| BR_AMOUNT_ASSIGNED | PaymentScheduleBrAmountAssigned | — |
| CALL_DATE_LAST | PaymentScheduleCallDateLast | — |
| CASH_APPLIED_AMOUNT_LAST | PaymentScheduleCashAppliedAmountLast | — |
| CASH_APPLIED_DATE_LAST | PaymentScheduleCashAppliedDateLast | — |
| CASH_APPLIED_ID_LAST | PaymentScheduleCashAppliedIdLast | — |
| CASH_APPLIED_STATUS_LAST | PaymentScheduleCashAppliedStatusLast | — |
| CASH_GL_DATE_LAST | PaymentScheduleCashGlDateLast | — |
| CASH_RECEIPT_AMOUNT_LAST | PaymentScheduleCashReceiptAmountLast | — |
| CASH_RECEIPT_DATE_LAST | PaymentScheduleCashReceiptDateLast | — |
| CASH_RECEIPT_ID | PaymentScheduleCashReceiptId | — |
| CASH_RECEIPT_ID_LAST | PaymentScheduleCashReceiptIdLast | — |
| CASH_RECEIPT_STATUS_LAST | PaymentScheduleCashReceiptStatusLast | — |
| CLASS | PaymentSchedulePaymentScheduleClass | — |
| COLLECTOR_LAST | PaymentScheduleCollectorLast | — |
| CONS_INV_ID | PaymentScheduleConsInvId | — |
| CONS_INV_ID_REV | PaymentScheduleConsInvIdRev | — |
| CREATED_BY | PaymentScheduleCreatedBy | — |
| CREATION_DATE | PaymentScheduleCreationDate | — |
| CUST_TRX_TYPE_SEQ_ID | PaymentScheduleCustTrxTypeSeqId | — |
| CUSTOMER_ID | PaymentScheduleCustomerId | — |
| CUSTOMER_SITE_USE_ID | PaymentScheduleCustomerSiteUseId | — |
| CUSTOMER_TRX_ID | PaymentScheduleCustomerTrxId | — |
| DISCOUNT_DATE | PaymentScheduleDiscountDate | — |
| DISCOUNT_ORIGINAL | PaymentScheduleDiscountOriginal | — |
| DISCOUNT_REMAINING | PaymentScheduleDiscountRemaining | — |
| DISCOUNT_TAKEN_EARNED | PaymentScheduleDiscountTakenEarned | — |
| DISCOUNT_TAKEN_UNEARNED | PaymentScheduleDiscountTakenUnearned | — |
| DISPUTE_DATE | PaymentScheduleDisputeDate | — |
| DUE_DATE | PaymentScheduleDueDate | — |
| DUNNING_LEVEL_OVERRIDE_DATE | PaymentScheduleDunningLevelOverrideDate | — |
| EXCHANGE_DATE | PaymentScheduleExchangeDate | — |
| EXCHANGE_RATE | PaymentScheduleExchangeRate | — |
| EXCHANGE_RATE_TYPE | PaymentScheduleExchangeRateType | — |
| EXCLUDE_FROM_CONS_BILL_FLAG | PaymentScheduleExcludeFromConsBillFlag | — |
| EXCLUDE_FROM_DUNNING_FLAG | PaymentScheduleExcludeFromDunningFlag | — |
| FOLLOW_UP_CODE_LAST | PaymentScheduleFollowUpCodeLast | — |
| FOLLOW_UP_DATE_LAST | PaymentScheduleFollowUpDateLast | — |
| FREIGHT_ORIGINAL | PaymentScheduleFreightOriginal | — |
| FREIGHT_REMAINING | PaymentScheduleFreightRemaining | — |
| GL_DATE | PaymentScheduleGlDate | — |
| GL_DATE_CLOSED | PaymentScheduleGlDateClosed | — |
| IN_COLLECTION | PaymentScheduleInCollection | — |
| INVOICE_CURRENCY_CODE | PaymentScheduleInvoiceCurrencyCode | — |
| LAST_CHARGE_DATE | PaymentScheduleLastChargeDate | — |
| LAST_UPDATE_DATE | PaymentScheduleLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PaymentScheduleLastUpdateLogin | — |
| LAST_UPDATED_BY | PaymentScheduleLastUpdatedBy | — |
| NUMBER_OF_DUE_DATES | PaymentScheduleNumberOfDueDates | — |
| OBJECT_VERSION_NUMBER | PaymentScheduleObjectVersionNumber | — |
| ORG_ID | PaymentScheduleOrgId | — |
| PAYMENT_APPROVAL | PaymentSchedulePaymentApproval | — |
| PAYMENT_SCHEDULE_ID | PaymentSchedulePaymentScheduleId | — |
| PROGRAM_APPLICATION_ID | PaymentScheduleProgramApplicationId | — |
| PROGRAM_ID | PaymentScheduleProgramId | — |
| PROGRAM_UPDATE_DATE | PaymentScheduleProgramUpdateDate | — |
| PROMISE_AMOUNT_LAST | PaymentSchedulePromiseAmountLast | — |
| PROMISE_DATE_LAST | PaymentSchedulePromiseDateLast | — |
| RECEIPT_CONFIRMED_FLAG | PaymentScheduleReceiptConfirmedFlag | — |
| RECEIVABLES_CHARGES_CHARGED | PaymentScheduleReceivablesChargesCharged | — |
| RECEIVABLES_CHARGES_REMAINING | PaymentScheduleReceivablesChargesRemaining | — |
| REQUEST_ID | PaymentScheduleRequestId | — |
| RESERVED_TYPE | PaymentScheduleReservedType | — |
| RESERVED_VALUE | PaymentScheduleReservedValue | — |
| REVERSED_CASH_RECEIPT_ID | PaymentScheduleReversedCashReceiptId | — |
| SECOND_LAST_CHARGE_DATE | PaymentScheduleSecondLastChargeDate | — |
| SELECTED_FOR_RECEIPT_BATCH_ID | PaymentScheduleSelectedForReceiptBatchId | — |
| STAGED_DUNNING_LEVEL | PaymentScheduleStagedDunningLevel | — |
| STATUS | PaymentScheduleStatus | — |
| TAX_ORIGINAL | PaymentScheduleTaxOriginal | — |
| TAX_REMAINING | PaymentScheduleTaxRemaining | — |
| TERM_ID | PaymentScheduleTermId | — |
| TERMS_SEQUENCE_NUMBER | PaymentScheduleTermsSequenceNumber | — |
| TRX_DATE | PaymentScheduleTrxDate | — |
| TRX_NUMBER | PaymentScheduleTrxNumber | — |

### [[transactionheaderpvo|TransactionHeaderPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_DUE_REMAINING | PaymentScheduleAcctdAmountDueRemaining | — |
| ACTIVE_CLAIM_FLAG | PaymentScheduleActiveClaimFlag | — |
| ACTUAL_DATE_CLOSED | PaymentScheduleActualDateClosed | — |
| ADJUSTMENT_AMOUNT_LAST | PaymentScheduleAdjustmentAmountLast | — |
| ADJUSTMENT_DATE_LAST | PaymentScheduleAdjustmentDateLast | — |
| ADJUSTMENT_GL_DATE_LAST | PaymentScheduleAdjustmentGlDateLast | — |
| ADJUSTMENT_ID_LAST | PaymentScheduleAdjustmentIdLast | — |
| AMOUNT_ADJUSTED | PaymentScheduleAmountAdjusted | — |
| AMOUNT_ADJUSTED_PENDING | PaymentScheduleAmountAdjustedPending | — |
| AMOUNT_APPLIED | PaymentScheduleAmountApplied | — |
| AMOUNT_CREDITED | PaymentScheduleAmountCredited | — |
| AMOUNT_DUE_ORIGINAL | PaymentScheduleAmountDueOriginal | — |
| AMOUNT_DUE_REMAINING | PaymentScheduleAmountDueRemaining | — |
| AMOUNT_IN_DISPUTE | PaymentScheduleAmountInDispute | — |
| AMOUNT_LINE_ITEMS_ORIGINAL | PaymentScheduleAmountLineItemsOriginal | — |
| AMOUNT_LINE_ITEMS_REMAINING | PaymentScheduleAmountLineItemsRemaining | — |
| AMOUNT_ON_ACCOUNT | PaymentScheduleAmountOnAccount | — |
| AMOUNT_OTHER_ACCOUNT | PaymentScheduleAmountOtherAccount | — |
| ASSOCIATED_CASH_RECEIPT_ID | PaymentScheduleAssociatedCashReceiptId | — |
| BR_AMOUNT_ASSIGNED | PaymentScheduleBrAmountAssigned | — |
| CALL_DATE_LAST | PaymentScheduleCallDateLast | — |
| CASH_APPLIED_AMOUNT_LAST | PaymentScheduleCashAppliedAmountLast | — |
| CASH_APPLIED_DATE_LAST | PaymentScheduleCashAppliedDateLast | — |
| CASH_APPLIED_ID_LAST | PaymentScheduleCashAppliedIdLast | — |
| CASH_APPLIED_STATUS_LAST | PaymentScheduleCashAppliedStatusLast | — |
| CASH_GL_DATE_LAST | PaymentScheduleCashGlDateLast | — |
| CASH_RECEIPT_AMOUNT_LAST | PaymentScheduleCashReceiptAmountLast | — |
| CASH_RECEIPT_DATE_LAST | PaymentScheduleCashReceiptDateLast | — |
| CASH_RECEIPT_ID | PaymentScheduleCashReceiptId | — |
| CASH_RECEIPT_ID_LAST | PaymentScheduleCashReceiptIdLast | — |
| CASH_RECEIPT_STATUS_LAST | PaymentScheduleCashReceiptStatusLast | — |
| CLASS | PaymentSchedulePaymentScheduleClass | — |
| COLLECTOR_LAST | PaymentScheduleCollectorLast | — |
| CONS_INV_ID | PaymentScheduleConsInvId | — |
| CONS_INV_ID_REV | PaymentScheduleConsInvIdRev | — |
| CREATED_BY | PaymentScheduleCreatedBy | — |
| CREATION_DATE | PaymentScheduleCreationDate | — |
| CUST_TRX_TYPE_SEQ_ID | PaymentScheduleCustTrxTypeSeqId | — |
| CUSTOMER_ID | PaymentScheduleCustomerId | — |
| CUSTOMER_SITE_USE_ID | PaymentScheduleCustomerSiteUseId | — |
| CUSTOMER_TRX_ID | PaymentScheduleCustomerTrxId | — |
| DISCOUNT_DATE | PaymentScheduleDiscountDate | — |
| DISCOUNT_ORIGINAL | PaymentScheduleDiscountOriginal | — |
| DISCOUNT_REMAINING | PaymentScheduleDiscountRemaining | — |
| DISCOUNT_TAKEN_EARNED | PaymentScheduleDiscountTakenEarned | — |
| DISCOUNT_TAKEN_UNEARNED | PaymentScheduleDiscountTakenUnearned | — |
| DISPUTE_DATE | PaymentScheduleDisputeDate | — |
| DUE_DATE | PaymentScheduleDueDate | — |
| DUNNING_LEVEL_OVERRIDE_DATE | PaymentScheduleDunningLevelOverrideDate | — |
| EXCHANGE_DATE | PaymentScheduleExchangeDate | — |
| EXCHANGE_RATE | PaymentScheduleExchangeRate | — |
| EXCHANGE_RATE_TYPE | PaymentScheduleExchangeRateType | — |
| EXCLUDE_FROM_CONS_BILL_FLAG | PaymentScheduleExcludeFromConsBillFlag | — |
| EXCLUDE_FROM_DUNNING_FLAG | PaymentScheduleExcludeFromDunningFlag | — |
| FOLLOW_UP_CODE_LAST | PaymentScheduleFollowUpCodeLast | — |
| FOLLOW_UP_DATE_LAST | PaymentScheduleFollowUpDateLast | — |
| FREIGHT_ORIGINAL | PaymentScheduleFreightOriginal | — |
| FREIGHT_REMAINING | PaymentScheduleFreightRemaining | — |
| GL_DATE | PaymentScheduleGlDate | — |
| GL_DATE_CLOSED | PaymentScheduleGlDateClosed | — |
| IN_COLLECTION | PaymentScheduleInCollection | — |
| INVOICE_CURRENCY_CODE | PaymentScheduleInvoiceCurrencyCode | — |
| LAST_CHARGE_DATE | PaymentScheduleLastChargeDate | — |
| LAST_UPDATE_DATE | PaymentScheduleLastUpdateDate | — |
| LAST_UPDATE_LOGIN | PaymentScheduleLastUpdateLogin | — |
| LAST_UPDATED_BY | PaymentScheduleLastUpdatedBy | — |
| NUMBER_OF_DUE_DATES | PaymentScheduleNumberOfDueDates | — |
| OBJECT_VERSION_NUMBER | PaymentScheduleObjectVersionNumber | — |
| ORG_ID | PaymentScheduleOrgId | — |
| PAYMENT_APPROVAL | PaymentSchedulePaymentApproval | — |
| PAYMENT_SCHEDULE_ID | PaymentSchedulePaymentScheduleId | — |
| PROGRAM_APPLICATION_ID | PaymentScheduleProgramApplicationId | — |
| PROGRAM_ID | PaymentScheduleProgramId | — |
| PROGRAM_UPDATE_DATE | PaymentScheduleProgramUpdateDate | — |
| PROMISE_AMOUNT_LAST | PaymentSchedulePromiseAmountLast | — |
| PROMISE_DATE_LAST | PaymentSchedulePromiseDateLast | — |
| RECEIPT_CONFIRMED_FLAG | PaymentScheduleReceiptConfirmedFlag | — |
| RECEIVABLES_CHARGES_CHARGED | PaymentScheduleReceivablesChargesCharged | — |
| RECEIVABLES_CHARGES_REMAINING | PaymentScheduleReceivablesChargesRemaining | — |
| REQUEST_ID | PaymentScheduleRequestId | — |
| RESERVED_TYPE | PaymentScheduleReservedType | — |
| RESERVED_VALUE | PaymentScheduleReservedValue | — |
| REVERSED_CASH_RECEIPT_ID | PaymentScheduleReversedCashReceiptId | — |
| SECOND_LAST_CHARGE_DATE | PaymentScheduleSecondLastChargeDate | — |
| SELECTED_FOR_RECEIPT_BATCH_ID | PaymentScheduleSelectedForReceiptBatchId | — |
| STAGED_DUNNING_LEVEL | PaymentScheduleStagedDunningLevel | — |
| STATUS | PaymentScheduleStatus | — |
| TAX_ORIGINAL | PaymentScheduleTaxOriginal | — |
| TAX_REMAINING | PaymentScheduleTaxRemaining | — |
| TERM_ID | PaymentScheduleTermId | — |
| TERMS_SEQUENCE_NUMBER | PaymentScheduleTermsSequenceNumber | — |
| TRX_DATE | PaymentScheduleTrxDate | — |
| TRX_NUMBER | PaymentScheduleTrxNumber | — |

### [[transactionhistorydistributionpvo|TransactionHistoryDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_DUE_REMAINING | BrPaymentSchedulesAcctdAmountDueRemaining | — |
| AMOUNT_DUE_REMAINING | BrPaymentSchedulesAmountDueRemaining | — |
| PAYMENT_SCHEDULE_ID | BrPaymentSchedulesPaymentScheduleId | — |

### [[transactionhistorypvo|TransactionHistoryPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_DUE_REMAINING | BrPaymentSchedulesAcctdAmountDueRemaining | — |
| AMOUNT_DUE_REMAINING | BrPaymentSchedulesAmountDueRemaining | — |
| PAYMENT_SCHEDULE_ID | BrPaymentSchedulesPaymentScheduleId | — |

### [[transactionlinebillsreceivablepvo|TransactionLineBillsReceivablePVO]] (AR · BICC: 1/93)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_DUE_REMAINING | PaymentScheduleAcctdAmountDueRemaining | — |
| ACTIVE_CLAIM_FLAG | PaymentScheduleActiveClaimFlag | — |
| ACTUAL_DATE_CLOSED | PaymentScheduleActualDateClosed | — |
| ADJUSTMENT_AMOUNT_LAST | PaymentScheduleAdjustmentAmountLast | — |
| ADJUSTMENT_DATE_LAST | PaymentScheduleAdjustmentDateLast | — |
| ADJUSTMENT_GL_DATE_LAST | PaymentScheduleAdjustmentGlDateLast | — |
| ADJUSTMENT_ID_LAST | PaymentScheduleAdjustmentIdLast | — |
| AMOUNT_ADJUSTED | PaymentScheduleAmountAdjusted | — |
| AMOUNT_ADJUSTED_PENDING | PaymentScheduleAmountAdjustedPending | — |
| AMOUNT_APPLIED | PaymentScheduleAmountApplied | — |
| AMOUNT_CREDITED | PaymentScheduleAmountCredited | — |
| AMOUNT_DUE_ORIGINAL | PaymentScheduleAmountDueOriginal | — |
| AMOUNT_DUE_REMAINING | PaymentScheduleAmountDueRemaining | — |
| AMOUNT_IN_DISPUTE | PaymentScheduleAmountInDispute | — |
| AMOUNT_LINE_ITEMS_ORIGINAL | PaymentScheduleAmountLineItemsOriginal | — |
| AMOUNT_LINE_ITEMS_REMAINING | PaymentScheduleAmountLineItemsRemaining | — |
| AMOUNT_ON_ACCOUNT | PaymentScheduleAmountOnAccount | — |
| AMOUNT_OTHER_ACCOUNT | PaymentScheduleAmountOtherAccount | — |
| ASSOCIATED_CASH_RECEIPT_ID | PaymentScheduleAssociatedCashReceiptId | — |
| BR_AMOUNT_ASSIGNED | PaymentScheduleBrAmountAssigned | — |
| CALL_DATE_LAST | PaymentScheduleCallDateLast | — |
| CASH_APPLIED_AMOUNT_LAST | PaymentScheduleCashAppliedAmountLast | — |
| CASH_APPLIED_DATE_LAST | PaymentScheduleCashAppliedDateLast | — |
| CASH_APPLIED_ID_LAST | PaymentScheduleCashAppliedIdLast | — |
| CASH_APPLIED_STATUS_LAST | PaymentScheduleCashAppliedStatusLast | — |
| CASH_GL_DATE_LAST | PaymentScheduleCashGlDateLast | — |
| CASH_RECEIPT_AMOUNT_LAST | PaymentScheduleCashReceiptAmountLast | — |
| CASH_RECEIPT_DATE_LAST | PaymentScheduleCashReceiptDateLast | — |
| CASH_RECEIPT_ID | PaymentScheduleCashReceiptId | — |
| CASH_RECEIPT_ID_LAST | PaymentScheduleCashReceiptIdLast | — |
| CASH_RECEIPT_STATUS_LAST | PaymentScheduleCashReceiptStatusLast | — |
| CLASS | PaymentSchedulePaymentScheduleClass | — |
| COLLECTOR_LAST | PaymentScheduleCollectorLast | — |
| CONS_INV_ID | PaymentScheduleConsInvId | — |
| CONS_INV_ID_REV | PaymentScheduleConsInvIdRev | — |
| CREATED_BY | PaymentScheduleCreatedBy | — |
| CREATION_DATE | PaymentScheduleCreationDate | — |
| CUST_TRX_TYPE_SEQ_ID | PaymentScheduleCustTrxTypeSeqId | — |
| CUSTOMER_ID | PaymentScheduleCustomerId | — |
| CUSTOMER_SITE_USE_ID | PaymentScheduleCustomerSiteUseId | — |
| CUSTOMER_TRX_ID | PaymentScheduleCustomerTrxId | — |
| DISCOUNT_DATE | PaymentScheduleDiscountDate | — |
| DISCOUNT_ORIGINAL | PaymentScheduleDiscountOriginal | — |
| DISCOUNT_REMAINING | PaymentScheduleDiscountRemaining | — |
| DISCOUNT_TAKEN_EARNED | PaymentScheduleDiscountTakenEarned | — |
| DISCOUNT_TAKEN_UNEARNED | PaymentScheduleDiscountTakenUnearned | — |
| DISPUTE_DATE | PaymentScheduleDisputeDate | — |
| DUE_DATE | PaymentScheduleDueDate | — |
| DUNNING_LEVEL_OVERRIDE_DATE | PaymentScheduleDunningLevelOverrideDate | — |
| EXCHANGE_DATE | PaymentScheduleExchangeDate | — |
| EXCHANGE_RATE | PaymentScheduleExchangeRate | — |
| EXCHANGE_RATE_TYPE | PaymentScheduleExchangeRateType | — |
| EXCLUDE_FROM_CONS_BILL_FLAG | PaymentScheduleExcludeFromConsBillFlag | — |
| EXCLUDE_FROM_DUNNING_FLAG | PaymentScheduleExcludeFromDunningFlag | — |
| FOLLOW_UP_CODE_LAST | PaymentScheduleFollowUpCodeLast | — |
| FOLLOW_UP_DATE_LAST | PaymentScheduleFollowUpDateLast | — |
| FREIGHT_ORIGINAL | PaymentScheduleFreightOriginal | — |
| FREIGHT_REMAINING | PaymentScheduleFreightRemaining | — |
| GL_DATE | PaymentScheduleGlDate | — |
| GL_DATE_CLOSED | PaymentScheduleGlDateClosed | — |
| IN_COLLECTION | PaymentScheduleInCollection | — |
| INVOICE_CURRENCY_CODE | PaymentScheduleInvoiceCurrencyCode | — |
| LAST_CHARGE_DATE | PaymentScheduleLastChargeDate | — |
| LAST_UPDATE_DATE | PaymentScheduleLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PaymentScheduleLastUpdateLogin | — |
| LAST_UPDATED_BY | PaymentScheduleLastUpdatedBy | — |
| NUMBER_OF_DUE_DATES | PaymentScheduleNumberOfDueDates | — |
| OBJECT_VERSION_NUMBER | PaymentScheduleObjectVersionNumber | — |
| ORG_ID | PaymentScheduleOrgId | — |
| PAYMENT_APPROVAL | PaymentSchedulePaymentApproval | — |
| PAYMENT_SCHEDULE_ID | PaymentSchedulePaymentScheduleId | — |
| PROGRAM_APPLICATION_ID | PaymentScheduleProgramApplicationId | — |
| PROGRAM_ID | PaymentScheduleProgramId | — |
| PROGRAM_UPDATE_DATE | PaymentScheduleProgramUpdateDate | — |
| PROMISE_AMOUNT_LAST | PaymentSchedulePromiseAmountLast | — |
| PROMISE_DATE_LAST | PaymentSchedulePromiseDateLast | — |
| RECEIPT_CONFIRMED_FLAG | PaymentScheduleReceiptConfirmedFlag | — |
| RECEIVABLES_CHARGES_CHARGED | PaymentScheduleReceivablesChargesCharged | — |
| RECEIVABLES_CHARGES_REMAINING | PaymentScheduleReceivablesChargesRemaining | — |
| REQUEST_ID | PaymentScheduleRequestId | — |
| RESERVED_TYPE | PaymentScheduleReservedType | — |
| RESERVED_VALUE | PaymentScheduleReservedValue | — |
| REVERSED_CASH_RECEIPT_ID | PaymentScheduleReversedCashReceiptId | — |
| SECOND_LAST_CHARGE_DATE | PaymentScheduleSecondLastChargeDate | — |
| SELECTED_FOR_RECEIPT_BATCH_ID | PaymentScheduleSelectedForReceiptBatchId | — |
| STAGED_DUNNING_LEVEL | PaymentScheduleStagedDunningLevel | — |
| STATUS | PaymentScheduleStatus | — |
| TAX_ORIGINAL | PaymentScheduleTaxOriginal | — |
| TAX_REMAINING | PaymentScheduleTaxRemaining | — |
| TERM_ID | PaymentScheduleTermId | — |
| TERMS_SEQUENCE_NUMBER | PaymentScheduleTermsSequenceNumber | — |
| TRX_DATE | PaymentScheduleTrxDate | — |
| TRX_NUMBER | PaymentScheduleTrxNumber | — |

### [[transactionlinedistributionpvo|TransactionLineDistributionPVO]] (AR · BICC: 1/93)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_DUE_REMAINING | TransactionLineBRAcctdAmountDueRemaining | — |
| ACTIVE_CLAIM_FLAG | TransactionLineBRActiveClaimFlag | — |
| ACTUAL_DATE_CLOSED | TransactionLineBRActualDateClosed | — |
| ADJUSTMENT_AMOUNT_LAST | TransactionLineBRAdjustmentAmountLast | — |
| ADJUSTMENT_DATE_LAST | TransactionLineBRAdjustmentDateLast | — |
| ADJUSTMENT_GL_DATE_LAST | TransactionLineBRAdjustmentGlDateLast | — |
| ADJUSTMENT_ID_LAST | TransactionLineBRAdjustmentIdLast | — |
| AMOUNT_ADJUSTED | TransactionLineBRAmountAdjusted | — |
| AMOUNT_ADJUSTED_PENDING | TransactionLineBRAmountAdjustedPending | — |
| AMOUNT_APPLIED | TransactionLineBRAmountApplied | — |
| AMOUNT_CREDITED | TransactionLineBRAmountCredited | — |
| AMOUNT_DUE_ORIGINAL | TransactionLineBRAmountDueOriginal | — |
| AMOUNT_DUE_REMAINING | TransactionLineBRAmountDueRemaining | — |
| AMOUNT_IN_DISPUTE | TransactionLineBRAmountInDispute | — |
| AMOUNT_LINE_ITEMS_ORIGINAL | TransactionLineBRAmountLineItemsOriginal | — |
| AMOUNT_LINE_ITEMS_REMAINING | TransactionLineBRAmountLineItemsRemaining | — |
| AMOUNT_ON_ACCOUNT | TransactionLineBRAmountOnAccount | — |
| AMOUNT_OTHER_ACCOUNT | TransactionLineBRAmountOtherAccount | — |
| ASSOCIATED_CASH_RECEIPT_ID | TransactionLineBRAssociatedCashReceiptId | — |
| BR_AMOUNT_ASSIGNED | TransactionLineBRBrAmountAssigned | — |
| CALL_DATE_LAST | TransactionLineBRCallDateLast | — |
| CASH_APPLIED_AMOUNT_LAST | TransactionLineBRCashAppliedAmountLast | — |
| CASH_APPLIED_DATE_LAST | TransactionLineBRCashAppliedDateLast | — |
| CASH_APPLIED_ID_LAST | TransactionLineBRCashAppliedIdLast | — |
| CASH_APPLIED_STATUS_LAST | TransactionLineBRCashAppliedStatusLast | — |
| CASH_GL_DATE_LAST | TransactionLineBRCashGlDateLast | — |
| CASH_RECEIPT_AMOUNT_LAST | TransactionLineBRCashReceiptAmountLast | — |
| CASH_RECEIPT_DATE_LAST | TransactionLineBRCashReceiptDateLast | — |
| CASH_RECEIPT_ID | TransactionLineBRCashReceiptId | — |
| CASH_RECEIPT_ID_LAST | TransactionLineBRCashReceiptIdLast | — |
| CASH_RECEIPT_STATUS_LAST | TransactionLineBRCashReceiptStatusLast | — |
| CLASS | TransactionLineBRPaymentScheduleClass | — |
| COLLECTOR_LAST | TransactionLineBRCollectorLast | — |
| CONS_INV_ID | TransactionLineBRConsInvId | — |
| CONS_INV_ID_REV | TransactionLineBRConsInvIdRev | — |
| CREATED_BY | TransactionLineBRCreatedBy | — |
| CREATION_DATE | TransactionLineBRCreationDate | — |
| CUST_TRX_TYPE_SEQ_ID | TransactionLineBRCustTrxTypeSeqId | — |
| CUSTOMER_ID | TransactionLineBRCustomerId | — |
| CUSTOMER_SITE_USE_ID | TransactionLineBRCustomerSiteUseId | — |
| CUSTOMER_TRX_ID | TransactionLineBRCustomerTrxId | — |
| DISCOUNT_DATE | TransactionLineBRDiscountDate | — |
| DISCOUNT_ORIGINAL | TransactionLineBRDiscountOriginal | — |
| DISCOUNT_REMAINING | TransactionLineBRDiscountRemaining | — |
| DISCOUNT_TAKEN_EARNED | TransactionLineBRDiscountTakenEarned | — |
| DISCOUNT_TAKEN_UNEARNED | TransactionLineBRDiscountTakenUnearned | — |
| DISPUTE_DATE | TransactionLineBRDisputeDate | — |
| DUE_DATE | TransactionLineBRDueDate | — |
| DUNNING_LEVEL_OVERRIDE_DATE | TransactionLineBRDunningLevelOverrideDate | — |
| EXCHANGE_DATE | TransactionLineBRExchangeDate | — |
| EXCHANGE_RATE | TransactionLineBRExchangeRate | — |
| EXCHANGE_RATE_TYPE | TransactionLineBRExchangeRateType | — |
| EXCLUDE_FROM_CONS_BILL_FLAG | TransactionLineBRExcludeFromConsBillFlag | — |
| EXCLUDE_FROM_DUNNING_FLAG | TransactionLineBRExcludeFromDunningFlag | — |
| FOLLOW_UP_CODE_LAST | TransactionLineBRFollowUpCodeLast | — |
| FOLLOW_UP_DATE_LAST | TransactionLineBRFollowUpDateLast | — |
| FREIGHT_ORIGINAL | TransactionLineBRFreightOriginal | — |
| FREIGHT_REMAINING | TransactionLineBRFreightRemaining | — |
| GL_DATE | TransactionLineBRGlDate | — |
| GL_DATE_CLOSED | TransactionLineBRGlDateClosed | — |
| IN_COLLECTION | TransactionLineBRInCollection | — |
| INVOICE_CURRENCY_CODE | TransactionLineBRInvoiceCurrencyCode | — |
| LAST_CHARGE_DATE | TransactionLineBRLastChargeDate | — |
| LAST_UPDATE_DATE | TransactionLineBRLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TransactionLineBRLastUpdateLogin | — |
| LAST_UPDATED_BY | TransactionLineBRLastUpdatedBy | — |
| NUMBER_OF_DUE_DATES | TransactionLineBRNumberOfDueDates | — |
| OBJECT_VERSION_NUMBER | TransactionLineBRObjectVersionNumber | — |
| ORG_ID | TransactionLineBROrgId | — |
| PAYMENT_APPROVAL | TransactionLineBRPaymentApproval | — |
| PAYMENT_SCHEDULE_ID | TransactionLineBRPaymentScheduleId | — |
| PROGRAM_APPLICATION_ID | TransactionLineBRProgramApplicationId | — |
| PROGRAM_ID | TransactionLineBRProgramId | — |
| PROGRAM_UPDATE_DATE | TransactionLineBRProgramUpdateDate | — |
| PROMISE_AMOUNT_LAST | TransactionLineBRPromiseAmountLast | — |
| PROMISE_DATE_LAST | TransactionLineBRPromiseDateLast | — |
| RECEIPT_CONFIRMED_FLAG | TransactionLineBRReceiptConfirmedFlag | — |
| RECEIVABLES_CHARGES_CHARGED | TransactionLineBRReceivablesChargesCharged | — |
| RECEIVABLES_CHARGES_REMAINING | TransactionLineBRReceivablesChargesRemaining | — |
| REQUEST_ID | TransactionLineBRRequestId | — |
| RESERVED_TYPE | TransactionLineBRReservedType | — |
| RESERVED_VALUE | TransactionLineBRReservedValue | — |
| REVERSED_CASH_RECEIPT_ID | TransactionLineBRReversedCashReceiptId | — |
| SECOND_LAST_CHARGE_DATE | TransactionLineBRSecondLastChargeDate | — |
| SELECTED_FOR_RECEIPT_BATCH_ID | TransactionLineBRSelectedForReceiptBatchId | — |
| STAGED_DUNNING_LEVEL | TransactionLineBRStagedDunningLevel | — |
| STATUS | TransactionLineBRStatus | — |
| TAX_ORIGINAL | TransactionLineBRTaxOriginal | — |
| TAX_REMAINING | TransactionLineBRTaxRemaining | — |
| TERM_ID | TransactionLineBRTermId | — |
| TERMS_SEQUENCE_NUMBER | TransactionLineBRTermsSequenceNumber | — |
| TRX_DATE | TransactionLineBRTrxDate | — |
| TRX_NUMBER | TransactionLineBRTrxNumber | — |

### [[transactionlinepvo|TransactionLinePVO]] (AR · BICC: 1/93)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_DUE_REMAINING | PaymentScheduleAcctdAmountDueRemaining | — |
| ACTIVE_CLAIM_FLAG | PaymentScheduleActiveClaimFlag | — |
| ACTUAL_DATE_CLOSED | PaymentScheduleActualDateClosed | — |
| ADJUSTMENT_AMOUNT_LAST | PaymentScheduleAdjustmentAmountLast | — |
| ADJUSTMENT_DATE_LAST | PaymentScheduleAdjustmentDateLast | — |
| ADJUSTMENT_GL_DATE_LAST | PaymentScheduleAdjustmentGlDateLast | — |
| ADJUSTMENT_ID_LAST | PaymentScheduleAdjustmentIdLast | — |
| AMOUNT_ADJUSTED | PaymentScheduleAmountAdjusted | — |
| AMOUNT_ADJUSTED_PENDING | PaymentScheduleAmountAdjustedPending | — |
| AMOUNT_APPLIED | PaymentScheduleAmountApplied | — |
| AMOUNT_CREDITED | PaymentScheduleAmountCredited | — |
| AMOUNT_DUE_ORIGINAL | PaymentScheduleAmountDueOriginal | — |
| AMOUNT_DUE_REMAINING | PaymentScheduleAmountDueRemaining | — |
| AMOUNT_IN_DISPUTE | PaymentScheduleAmountInDispute | — |
| AMOUNT_LINE_ITEMS_ORIGINAL | PaymentScheduleAmountLineItemsOriginal | — |
| AMOUNT_LINE_ITEMS_REMAINING | PaymentScheduleAmountLineItemsRemaining | — |
| AMOUNT_ON_ACCOUNT | PaymentScheduleAmountOnAccount | — |
| AMOUNT_OTHER_ACCOUNT | PaymentScheduleAmountOtherAccount | — |
| ASSOCIATED_CASH_RECEIPT_ID | PaymentScheduleAssociatedCashReceiptId | — |
| BR_AMOUNT_ASSIGNED | PaymentScheduleBrAmountAssigned | — |
| CALL_DATE_LAST | PaymentScheduleCallDateLast | — |
| CASH_APPLIED_AMOUNT_LAST | PaymentScheduleCashAppliedAmountLast | — |
| CASH_APPLIED_DATE_LAST | PaymentScheduleCashAppliedDateLast | — |
| CASH_APPLIED_ID_LAST | PaymentScheduleCashAppliedIdLast | — |
| CASH_APPLIED_STATUS_LAST | PaymentScheduleCashAppliedStatusLast | — |
| CASH_GL_DATE_LAST | PaymentScheduleCashGlDateLast | — |
| CASH_RECEIPT_AMOUNT_LAST | PaymentScheduleCashReceiptAmountLast | — |
| CASH_RECEIPT_DATE_LAST | PaymentScheduleCashReceiptDateLast | — |
| CASH_RECEIPT_ID | PaymentScheduleCashReceiptId | — |
| CASH_RECEIPT_ID_LAST | PaymentScheduleCashReceiptIdLast | — |
| CASH_RECEIPT_STATUS_LAST | PaymentScheduleCashReceiptStatusLast | — |
| CLASS | PaymentSchedulePaymentScheduleClass | — |
| COLLECTOR_LAST | PaymentScheduleCollectorLast | — |
| CONS_INV_ID | PaymentScheduleConsInvId | — |
| CONS_INV_ID_REV | PaymentScheduleConsInvIdRev | — |
| CREATED_BY | PaymentScheduleCreatedBy | — |
| CREATION_DATE | PaymentScheduleCreationDate | — |
| CUST_TRX_TYPE_SEQ_ID | PaymentScheduleCustTrxTypeSeqId | — |
| CUSTOMER_ID | PaymentScheduleCustomerId | — |
| CUSTOMER_SITE_USE_ID | PaymentScheduleCustomerSiteUseId | — |
| CUSTOMER_TRX_ID | PaymentScheduleCustomerTrxId | — |
| DISCOUNT_DATE | PaymentScheduleDiscountDate | — |
| DISCOUNT_ORIGINAL | PaymentScheduleDiscountOriginal | — |
| DISCOUNT_REMAINING | PaymentScheduleDiscountRemaining | — |
| DISCOUNT_TAKEN_EARNED | PaymentScheduleDiscountTakenEarned | — |
| DISCOUNT_TAKEN_UNEARNED | PaymentScheduleDiscountTakenUnearned | — |
| DISPUTE_DATE | PaymentScheduleDisputeDate | — |
| DUE_DATE | PaymentScheduleDueDate | — |
| DUNNING_LEVEL_OVERRIDE_DATE | PaymentScheduleDunningLevelOverrideDate | — |
| EXCHANGE_DATE | PaymentScheduleExchangeDate | — |
| EXCHANGE_RATE | PaymentScheduleExchangeRate | — |
| EXCHANGE_RATE_TYPE | PaymentScheduleExchangeRateType | — |
| EXCLUDE_FROM_CONS_BILL_FLAG | PaymentScheduleExcludeFromConsBillFlag | — |
| EXCLUDE_FROM_DUNNING_FLAG | PaymentScheduleExcludeFromDunningFlag | — |
| FOLLOW_UP_CODE_LAST | PaymentScheduleFollowUpCodeLast | — |
| FOLLOW_UP_DATE_LAST | PaymentScheduleFollowUpDateLast | — |
| FREIGHT_ORIGINAL | PaymentScheduleFreightOriginal | — |
| FREIGHT_REMAINING | PaymentScheduleFreightRemaining | — |
| GL_DATE | PaymentScheduleGlDate | — |
| GL_DATE_CLOSED | PaymentScheduleGlDateClosed | — |
| IN_COLLECTION | PaymentScheduleInCollection | — |
| INVOICE_CURRENCY_CODE | PaymentScheduleInvoiceCurrencyCode | — |
| LAST_CHARGE_DATE | PaymentScheduleLastChargeDate | — |
| LAST_UPDATE_DATE | PaymentScheduleLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PaymentScheduleLastUpdateLogin | — |
| LAST_UPDATED_BY | PaymentScheduleLastUpdatedBy | — |
| NUMBER_OF_DUE_DATES | PaymentScheduleNumberOfDueDates | — |
| OBJECT_VERSION_NUMBER | PaymentScheduleObjectVersionNumber | — |
| ORG_ID | PaymentScheduleOrgId | — |
| PAYMENT_APPROVAL | PaymentSchedulePaymentApproval | — |
| PAYMENT_SCHEDULE_ID | PaymentSchedulePaymentScheduleId | — |
| PROGRAM_APPLICATION_ID | PaymentScheduleProgramApplicationId | — |
| PROGRAM_ID | PaymentScheduleProgramId | — |
| PROGRAM_UPDATE_DATE | PaymentScheduleProgramUpdateDate | — |
| PROMISE_AMOUNT_LAST | PaymentSchedulePromiseAmountLast | — |
| PROMISE_DATE_LAST | PaymentSchedulePromiseDateLast | — |
| RECEIPT_CONFIRMED_FLAG | PaymentScheduleReceiptConfirmedFlag | — |
| RECEIVABLES_CHARGES_CHARGED | PaymentScheduleReceivablesChargesCharged | — |
| RECEIVABLES_CHARGES_REMAINING | PaymentScheduleReceivablesChargesRemaining | — |
| REQUEST_ID | PaymentScheduleRequestId | — |
| RESERVED_TYPE | PaymentScheduleReservedType | — |
| RESERVED_VALUE | PaymentScheduleReservedValue | — |
| REVERSED_CASH_RECEIPT_ID | PaymentScheduleReversedCashReceiptId | — |
| SECOND_LAST_CHARGE_DATE | PaymentScheduleSecondLastChargeDate | — |
| SELECTED_FOR_RECEIPT_BATCH_ID | PaymentScheduleSelectedForReceiptBatchId | — |
| STAGED_DUNNING_LEVEL | PaymentScheduleStagedDunningLevel | — |
| STATUS | PaymentScheduleStatus | — |
| TAX_ORIGINAL | PaymentScheduleTaxOriginal | — |
| TAX_REMAINING | PaymentScheduleTaxRemaining | — |
| TERM_ID | PaymentScheduleTermId | — |
| TERMS_SEQUENCE_NUMBER | PaymentScheduleTermsSequenceNumber | — |
| TRX_DATE | PaymentScheduleTrxDate | — |
| TRX_NUMBER | PaymentScheduleTrxNumber | — |

---

## 📚 Referências

- [Oracle Docs — AR_PAYMENT_SCHEDULES_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/arpaymentschedulesall-10053.html)
- [[ar-module-data-dictionary]] — Dossiê do módulo AR
