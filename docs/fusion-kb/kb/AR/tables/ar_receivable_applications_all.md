---
id: DOC-AR-020
doc_type: system-doc
title: "AR_RECEIVABLE_APPLICATIONS_ALL — Aplicações de Recebimentos e Créditos"
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
  - aplicacoes
  - receivable-applications
  - cash-application
aliases:
  - AR_RECEIVABLE_APPLICATIONS_ALL
  - ar_receivable_applications_all
  - aplicacoes-recebimentos-ar
  - receivable-applications
  - cash-application
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_RECEIVABLE_APPLICATIONS_ALL

## 📌 Visão Geral

Armazena as **aplicações de recebimentos e notas de crédito a faturas** no módulo Accounts Receivable. Cada registro representa uma aplicação individual — a alocação de um valor recebido (cash receipt) ou crédito (credit memo) contra uma fatura específica. O campo `APPLICATION_TYPE` distingue entre aplicações de caixa (CASH) e de credit memo (CM). É a tabela central para entender **como os recebimentos foram distribuídos** entre as faturas.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Aplicação de recebimentos:** Vinculação de pagamentos recebidos a faturas específicas, reduzindo o saldo em aberto.
- **Aplicação de credit memos:** Alocação de notas de crédito contra faturas para compensação.
- **Descontos:** Registro de descontos concedidos (earned) e não-concedidos (unearned) na aplicação.
- **Reconciliação AR:** Base para conciliar saldos de recebimentos × faturas × GL.
- **Relatórios de aging:** Impacto direto no cálculo de saldos em aberto em [[ar_payment_schedules_all]].
- **Auditoria:** Rastreabilidade completa de cada alocação de valor.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | RECEIVABLE_APPLICATION_ID | NUMBER(18) | NOT NULL | PK | Identificador único da aplicação | — | 🟢 100% |
| 2 | CASH_RECEIPT_ID | NUMBER(18) | NULL | FK | Recebimento de caixa aplicado (quando APPLICATION_TYPE = CASH) | [[ar_cash_receipts_all]] | 🟢 100% |
| 3 | APPLIED_CUSTOMER_TRX_ID | NUMBER(18) | NULL | FK | Transação (fatura) na qual o valor foi aplicado | [[ra_customer_trx_all]] | 🟢 100% |
| 4 | APPLIED_PAYMENT_SCHEDULE_ID | NUMBER(18) | NULL | FK | Schedule de pagamento da fatura aplicada | [[ar_payment_schedules_all]] | 🟢 100% |
| 5 | APPLICATION_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo da aplicação: CASH (recebimento) ou CM (credit memo) | — | 🟢 100% |
| 6 | STATUS | VARCHAR2(30) | NOT NULL | Classificação | Status da aplicação (APP/UNAPP/ACC/ACTIVITY/OTHER ACC) | — | 🟢 100% |
| 7 | AMOUNT_APPLIED | NUMBER | NULL | Financeiro | Valor aplicado na moeda da fatura | — | 🟢 100% |
| 8 | AMOUNT_APPLIED_FROM | NUMBER | NULL | Financeiro | Valor aplicado na moeda do recebimento (cross-currency) | — | 🟢 100% |
| 9 | ACCTD_AMOUNT_APPLIED_FROM | NUMBER | NULL | Financeiro | Valor aplicado na moeda funcional | — | 🟢 100% |
| 10 | ACCTD_AMOUNT_APPLIED_TO | NUMBER | NULL | Financeiro | Valor aplicado na moeda funcional (lado da fatura) | — | 🟢 100% |
| 11 | APPLY_DATE | DATE | NOT NULL | Data | Data da aplicação | — | 🟢 100% |
| 12 | GL_DATE | DATE | NOT NULL | Contabilidade | Data contábil (General Ledger) | — | 🟢 100% |
| 13 | GL_POSTED_DATE | DATE | NULL | Contabilidade | Data em que foi contabilizado no GL | — | 🟢 100% |
| 14 | POSTING_CONTROL_ID | NUMBER(18) | NULL | Contabilidade | ID do processo de posting | — | 🟢 100% |
| 15 | CODE_COMBINATION_ID | NUMBER(18) | NULL | Contabilidade | Combinação de contas contábeis (CCID) | [[gl_code_combinations]] | 🟢 100% |
| 16 | PAYMENT_SCHEDULE_ID | NUMBER(18) | NULL | FK | Schedule de pagamento do recebimento/credit memo | [[ar_payment_schedules_all]] | 🟢 100% |
| 17 | CUSTOMER_TRX_ID | NUMBER(18) | NULL | FK | Transação de origem do credit memo (quando APPLICATION_TYPE = CM) | [[ra_customer_trx_all]] | 🟢 100% |
| 18 | DISPLAY_FLAG | VARCHAR2(1) | NULL | Controle | Indica se a aplicação é exibida na UI (Y/N) | — | 🟢 100% |
| 19 | APPLICATION_RULE | VARCHAR2(30) | NULL | Classificação | Regra utilizada na aplicação (e.g., LINE FIRST, PRORATE) | — | 🟢 100% |
| 20 | EARNED_DISCOUNT_TAKEN | NUMBER | NULL | Financeiro | Desconto concedido (earned discount) | — | 🟢 100% |
| 21 | UNEARNED_DISCOUNT_TAKEN | NUMBER | NULL | Financeiro | Desconto não-concedido (unearned discount) | — | 🟢 100% |
| 22 | EARNED_DISCOUNT_CCID | NUMBER(18) | NULL | Contabilidade | CCID do desconto concedido | [[gl_code_combinations]] | 🟢 100% |
| 23 | UNEARNED_DISCOUNT_CCID | NUMBER(18) | NULL | Contabilidade | CCID do desconto não-concedido | [[gl_code_combinations]] | 🟢 100% |
| 24 | DAYS_LATE | NUMBER | NULL | Financeiro | Dias de atraso no pagamento | — | 🟢 100% |
| 25 | COMMENTS | VARCHAR2(2000) | NULL | Texto livre | Comentários sobre a aplicação | — | 🟢 100% |
| 26 | APPLIED_CUSTOMER_TRX_LINE_ID | NUMBER(18) | NULL | FK | Linha específica da fatura aplicada (line-level) | [[ra_customer_trx_lines_all]] | 🟢 100% |
| 27 | REVERSAL_GL_DATE | DATE | NULL | Contabilidade | Data contábil da reversão da aplicação | — | 🟢 100% |
| 28 | LINK_TO_CUSTOMER_TRX_ID | NUMBER(18) | NULL | Referência cruzada | Transação vinculada (para on-account credit) | [[ra_customer_trx_all]] | 🟢 100% |
| 29 | ON_ACCOUNT_CUSTOMER | NUMBER(18) | NULL | Cliente | Conta do cliente para crédito on-account | [[hz_cust_accounts]] | 🟢 100% |
| 30 | RECEIVABLES_TRX_ID | NUMBER(18) | NULL | Classificação | Tipo de atividade de recebimento | [[ar_receivables_trx_all]] | 🟢 100% |
| 31 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 32 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 33 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 34 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 35 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 36 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 37 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 100% |
| 38 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 100% |
| 39 | GLOBAL_ATTRIBUTE1–20 | VARCHAR2(150) | NULL | DFF | Atributos globais (localizações por país) | — | 🟢 100% |
| 40 | GLOBAL_ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Global Descriptive Flexfield | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ar_cash_receipts_all]] — via `CASH_RECEIPT_ID` (recebimento de caixa)
- [[ra_customer_trx_all]] — via `APPLIED_CUSTOMER_TRX_ID` (fatura aplicada) e `CUSTOMER_TRX_ID` (credit memo)
- [[ar_payment_schedules_all]] — via `APPLIED_PAYMENT_SCHEDULE_ID` e `PAYMENT_SCHEDULE_ID` (parcela contra a qual o pagamento foi aplicado)
- [[ra_customer_trx_lines_all]] — via `APPLIED_CUSTOMER_TRX_LINE_ID` (linha da fatura)
- [[gl_code_combinations]] — via `CODE_COMBINATION_ID`, `EARNED_DISCOUNT_CCID`, `UNEARNED_DISCOUNT_CCID` (conta contábil da aplicação de recebível)
- [[ar_receivables_trx_all]] — via `RECEIVABLES_TRX_ID` (atividade de recebimento)
- [[hz_cust_accounts]] — via `ON_ACCOUNT_CUSTOMER` (cliente on-account)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit da aplicação de recebível)

### Tabelas-filha (FK de saída)
- [[ar_distributions_all]] — via `SOURCE_ID` onde `SOURCE_TABLE = 'RA'` (distribuições contábeis)

---

## 📎 Uso Típico

### Aplicações de um recebimento
```sql
SELECT ra.STATUS, ra.APPLICATION_TYPE, ra.AMOUNT_APPLIED,
       ra.APPLY_DATE, ct.TRX_NUMBER
FROM   AR_RECEIVABLE_APPLICATIONS_ALL ra
LEFT JOIN RA_CUSTOMER_TRX_ALL ct ON ct.CUSTOMER_TRX_ID = ra.APPLIED_CUSTOMER_TRX_ID
WHERE  ra.CASH_RECEIPT_ID = :p_cash_receipt_id
  AND  ra.DISPLAY_FLAG = 'Y';
```

### Faturas com aplicações de recebimento
```sql
SELECT ct.TRX_NUMBER, cr.RECEIPT_NUMBER,
       ra.AMOUNT_APPLIED, ra.APPLY_DATE, ra.STATUS
FROM   AR_RECEIVABLE_APPLICATIONS_ALL ra
JOIN   RA_CUSTOMER_TRX_ALL ct ON ct.CUSTOMER_TRX_ID = ra.APPLIED_CUSTOMER_TRX_ID
JOIN   AR_CASH_RECEIPTS_ALL cr ON cr.CASH_RECEIPT_ID = ra.CASH_RECEIPT_ID
WHERE  ra.APPLICATION_TYPE = 'CASH'
  AND  ra.STATUS = 'APP'
  AND  ra.ORG_ID = :p_org_id;
```

### Filtros comuns
- `APPLICATION_TYPE = 'CASH'` — Aplicações de recebimento
- `APPLICATION_TYPE = 'CM'` — Aplicações de credit memo
- `STATUS = 'APP'` — Aplicações efetivadas
- `DISPLAY_FLAG = 'Y'` — Aplicações visíveis na UI

---

## 🔒 Observações

- Os campos `AMOUNT_APPLIED` e `AMOUNT_APPLIED_FROM` diferem em aplicações **cross-currency**: `AMOUNT_APPLIED` é na moeda da fatura, `AMOUNT_APPLIED_FROM` na moeda do recebimento.
- O `STATUS` pode ser: **APP** (aplicado), **UNAPP** (não-aplicado), **ACC** (on-account), **ACTIVITY** (atividade), **OTHER ACC** (outra conta).
- Registros com `DISPLAY_FLAG = 'N'` são internos ao sistema (e.g., reversões internas) — não devem aparecer em relatórios de usuário.
- O campo `APPLICATION_RULE` indica a regra de alocação: **LINE FIRST** (aplica primeiro em linhas), **PRORATE** (distribui proporcional), etc.
- Descontos (earned/unearned) são registrados junto com a aplicação e impactam contas contábeis separadas.

---

## 🔗 PVOs Relacionados

### [[adjustmentdistributionpvo|AdjustmentDistributionPVO]] (AR · BICC: 1/84)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_APPLIED_FROM | ReceivableApplication1AcctdAmountAppliedFrom | — |
| ACCTD_AMOUNT_APPLIED_TO | ReceivableApplication1AcctdAmountAppliedTo | — |
| ACCTD_EARNED_DISCOUNT_TAKEN | ReceivableApplication1AcctdEarnedDiscountTaken | — |
| ACCTD_UNEARNED_DISCOUNT_TAKEN | ReceivableApplication1AcctdUnearnedDiscountTaken | — |
| AMOUNT_APPLIED | ReceivableApplication1AmountApplied | — |
| AMOUNT_APPLIED_FROM | ReceivableApplication1AmountAppliedFrom | — |
| APPLICATION_REF_ID | ReceivableApplication1ApplicationRefId | — |
| APPLICATION_REF_NUM | ReceivableApplication1ApplicationRefNum | — |
| APPLICATION_REF_REASON | ReceivableApplication1ApplicationRefReason | — |
| APPLICATION_REF_TYPE | ReceivableApplication1ApplicationRefType | — |
| APPLICATION_RULE | ReceivableApplication1ApplicationRule | — |
| APPLICATION_TYPE | ReceivableApplication1ApplicationType | — |
| APPLIED_CUSTOMER_TRX_ID | ReceivableApplication1AppliedCustomerTrxId | — |
| APPLIED_CUSTOMER_TRX_LINE_ID | ReceivableApplication1AppliedCustomerTrxLineId | — |
| APPLIED_PAYMENT_SCHEDULE_ID | ReceivableApplication1AppliedPaymentScheduleId | — |
| APPLIED_REC_APP_ID | ReceivableApplication1AppliedRecAppId | — |
| APPLY_DATE | ReceivableApplication1ApplyDate | — |
| CASH_RECEIPT_HISTORY_ID | ReceivableApplication1CashReceiptHistoryId | — |
| CASH_RECEIPT_ID | ReceivableApplication1CashReceiptId | — |
| CHARGEBACK_CUSTOMER_TRX_ID | ReceivableApplication1ChargebackCustomerTrxId | — |
| CHARGES_EDISCOUNTED | ReceivableApplication1ChargesEdiscounted | — |
| CHARGES_UEDISCOUNTED | ReceivableApplication1ChargesUediscounted | — |
| CODE_COMBINATION_ID | ReceivableApplication1CodeCombinationId | — |
| COMMENTS | ReceivableApplication1Comments | — |
| CONFIRMED_FLAG | ReceivableApplication1ConfirmedFlag | — |
| CONS_INV_ID | ReceivableApplication1ConsInvId | — |
| CONS_INV_ID_TO | ReceivableApplication1ConsInvIdTo | — |
| CREATED_BY | ReceivableApplication1CreatedBy | — |
| CREATION_DATE | ReceivableApplication1CreationDate | — |
| CUSTOMER_REASON | ReceivableApplication1CustomerReason | — |
| CUSTOMER_REFERENCE | ReceivableApplication1CustomerReference | — |
| CUSTOMER_TRX_ID | ReceivableApplication1CustomerTrxId | — |
| DAYS_LATE | ReceivableApplication1DaysLate | — |
| DISPLAY | ReceivableApplication1Display | — |
| EARNED_DISCOUNT_CCID | ReceivableApplication1EarnedDiscountCcid | — |
| EARNED_DISCOUNT_TAKEN | ReceivableApplication1EarnedDiscountTaken | — |
| EDISC_TAX_ACCT_RULE | ReceivableApplication1EdiscTaxAcctRule | — |
| EVENT_ID | ReceivableApplication1EventId | — |
| EXCEPTION_REASON_CODE | ReceivableApplication1ExceptionReasonCode | — |
| FREIGHT_APPLIED | ReceivableApplication1FreightApplied | — |
| FREIGHT_EDISCOUNTED | ReceivableApplication1FreightEdiscounted | — |
| FREIGHT_UEDISCOUNTED | ReceivableApplication1FreightUediscounted | — |
| GL_DATE | ReceivableApplication1GlDate | — |
| GL_POSTED_DATE | ReceivableApplication1GlPostedDate | — |
| LAST_UPDATE_DATE | ReceivableApplication1LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ReceivableApplication1LastUpdateLogin | — |
| LAST_UPDATED_BY | ReceivableApplication1LastUpdatedBy | — |
| LINE_APPLIED | ReceivableApplication1LineApplied | — |
| LINE_EDISCOUNTED | ReceivableApplication1LineEdiscounted | — |
| LINE_UEDISCOUNTED | ReceivableApplication1LineUediscounted | — |
| LINK_TO_CUSTOMER_TRX_ID | ReceivableApplication1LinkToCustomerTrxId | — |
| LINK_TO_TRX_HIST_ID | ReceivableApplication1LinkToTrxHistId | — |
| OBJECT_VERSION_NUMBER | ReceivableApplication1ObjectVersionNumber | — |
| ON_ACCOUNT_CUSTOMER | ReceivableApplication1OnAccountCustomer | — |
| ORG_ID | ReceivableApplication1OrgId | — |
| PAYMENT_SCHEDULE_ID | ReceivableApplication1PaymentScheduleId | — |
| PAYMENT_SET_ID | ReceivableApplication1PaymentSetId | — |
| POSTABLE | ReceivableApplication1Postable | — |
| POSTING_CONTROL_ID | ReceivableApplication1PostingControlId | — |
| PROGRAM_APPLICATION_ID | ReceivableApplication1ProgramApplicationId | — |
| PROGRAM_ID | ReceivableApplication1ProgramId | — |
| PROGRAM_UPDATE_DATE | ReceivableApplication1ProgramUpdateDate | — |
| RECEIVABLE_APPLICATION_ID | ReceivableApplication1ReceivableApplicationId | — |
| RECEIVABLES_CHARGES_APPLIED | ReceivableApplication1ReceivablesChargesApplied | — |
| RECEIVABLES_TRX_ID | ReceivableApplication1ReceivablesTrxId | — |
| REQUEST_ID | ReceivableApplication1RequestId | — |
| REVERSAL_GL_DATE | ReceivableApplication1ReversalGlDate | — |
| RULE_SET_ID | ReceivableApplication1RuleSetId | — |
| SECONDARY_APPLICATION_REF_ID | ReceivableApplication1SecondaryApplicationRefId | — |
| SECONDARY_APPLICATION_REF_NUM | ReceivableApplication1SecondaryApplicationRefNum | — |
| SECONDARY_APPLICATION_REF_TYPE | ReceivableApplication1SecondaryApplicationRefType | — |
| SET_OF_BOOKS_ID | ReceivableApplication1SetOfBooksId | — |
| STATUS | ReceivableApplication1Status | — |
| TAX_APPLIED | ReceivableApplication1TaxApplied | — |
| TAX_CODE | ReceivableApplication1TaxCode | — |
| TAX_EDISCOUNTED | ReceivableApplication1TaxEdiscounted | — |
| TAX_UEDISCOUNTED | ReceivableApplication1TaxUediscounted | — |
| TRANS_TO_RECEIPT_RATE | ReceivableApplication1TransToReceiptRate | — |
| UNEARNED_DISCOUNT_CCID | ReceivableApplication1UnearnedDiscountCcid | — |
| UNEARNED_DISCOUNT_TAKEN | ReceivableApplication1UnearnedDiscountTaken | — |
| UNEDISC_TAX_ACCT_RULE | ReceivableApplication1UnediscTaxAcctRule | — |
| UPGRADE_METHOD | ReceivableApplication1UpgradeMethod | — |
| USSGL_TRANSACTION_CODE | ReceivableApplication1UssglTransactionCode | — |
| USSGL_TRANSACTION_CODE_CONTEXT | ReceivableApplication1UssglTransactionCodeContext | — |

### [[completedtrxrevadjdistributionpvo|CompletedTrxRevAdjDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_APPLIED_FROM | ReceivableApplicationAcctdAmountAppliedFrom | — |
| ACCTD_AMOUNT_APPLIED_FROM | ReceivableApplicationAdjAcctdAmountAppliedFrom | — |
| ACCTD_AMOUNT_APPLIED_TO | ReceivableApplicationAcctdAmountAppliedTo | — |
| ACCTD_AMOUNT_APPLIED_TO | ReceivableApplicationAdjAcctdAmountAppliedTo | — |
| ACCTD_EARNED_DISCOUNT_TAKEN | ReceivableApplicationAcctdEarnedDiscountTaken | — |
| ACCTD_EARNED_DISCOUNT_TAKEN | ReceivableApplicationAdjAcctdEarnedDiscountTaken | — |
| ACCTD_UNEARNED_DISCOUNT_TAKEN | ReceivableApplicationAcctdUnearnedDiscountTaken | — |
| ACCTD_UNEARNED_DISCOUNT_TAKEN | ReceivableApplicationAdjAcctdUnearnedDiscountTaken | — |
| AMOUNT_APPLIED | ReceivableApplicationAdjAmountApplied | — |
| AMOUNT_APPLIED | ReceivableApplicationAmountApplied | — |
| AMOUNT_APPLIED_FROM | ReceivableApplicationAdjAmountAppliedFrom | — |
| AMOUNT_APPLIED_FROM | ReceivableApplicationAmountAppliedFrom | — |
| APPLICATION_REF_ID | ReceivableApplicationAdjApplicationRefId | — |
| APPLICATION_REF_ID | ReceivableApplicationApplicationRefId | — |
| APPLICATION_REF_NUM | ReceivableApplicationAdjApplicationRefNum | — |
| APPLICATION_REF_NUM | ReceivableApplicationApplicationRefNum | — |
| APPLICATION_REF_REASON | ReceivableApplicationAdjApplicationRefReason | — |
| APPLICATION_REF_REASON | ReceivableApplicationApplicationRefReason | — |
| APPLICATION_REF_TYPE | ReceivableApplicationAdjApplicationRefType | — |
| APPLICATION_REF_TYPE | ReceivableApplicationApplicationRefType | — |
| APPLICATION_RULE | ReceivableApplicationAdjApplicationRule | — |
| APPLICATION_RULE | ReceivableApplicationApplicationRule | — |
| APPLICATION_TYPE | ReceivableApplicationAdjApplicationType | — |
| APPLICATION_TYPE | ReceivableApplicationApplicationType | — |
| APPLIED_CUSTOMER_TRX_ID | ReceivableApplicationAdjAppliedCustomerTrxId | — |
| APPLIED_CUSTOMER_TRX_ID | ReceivableApplicationAppliedCustomerTrxId | — |
| APPLIED_CUSTOMER_TRX_LINE_ID | ReceivableApplicationAdjAppliedCustomerTrxLineId | — |
| APPLIED_CUSTOMER_TRX_LINE_ID | ReceivableApplicationAppliedCustomerTrxLineId | — |
| APPLIED_PAYMENT_SCHEDULE_ID | ReceivableApplicationAdjAppliedPaymentScheduleId | — |
| APPLIED_PAYMENT_SCHEDULE_ID | ReceivableApplicationAppliedPaymentScheduleId | — |
| APPLIED_REC_APP_ID | ReceivableApplicationAdjAppliedRecAppId | — |
| APPLIED_REC_APP_ID | ReceivableApplicationAppliedRecAppId | — |
| APPLY_DATE | ReceivableApplicationAdjApplyDate | — |
| APPLY_DATE | ReceivableApplicationApplyDate | — |
| CASH_RECEIPT_HISTORY_ID | ReceivableApplicationAdjCashReceiptHistoryId | — |
| CASH_RECEIPT_HISTORY_ID | ReceivableApplicationCashReceiptHistoryId | — |
| CASH_RECEIPT_ID | ReceivableApplicationAdjCashReceiptId | — |
| CASH_RECEIPT_ID | ReceivableApplicationCashReceiptId | — |
| CHARGEBACK_CUSTOMER_TRX_ID | ReceivableApplicationAdjChargebackCustomerTrxId | — |
| CHARGEBACK_CUSTOMER_TRX_ID | ReceivableApplicationChargebackCustomerTrxId | — |
| CHARGES_EDISCOUNTED | ReceivableApplicationAdjChargesEdiscounted | — |
| CHARGES_EDISCOUNTED | ReceivableApplicationChargesEdiscounted | — |
| CHARGES_UEDISCOUNTED | ReceivableApplicationAdjChargesUediscounted | — |
| CHARGES_UEDISCOUNTED | ReceivableApplicationChargesUediscounted | — |
| CODE_COMBINATION_ID | ReceivableApplicationAdjCodeCombinationId | — |
| CODE_COMBINATION_ID | ReceivableApplicationCodeCombinationId | — |
| COMMENTS | ReceivableApplicationAdjComments | — |
| COMMENTS | ReceivableApplicationComments | — |
| CONFIRMED_FLAG | ReceivableApplicationAdjConfirmedFlag | — |
| CONFIRMED_FLAG | ReceivableApplicationConfirmedFlag | — |
| CONS_INV_ID | ReceivableApplicationAdjConsInvId | — |
| CONS_INV_ID | ReceivableApplicationConsInvId | — |
| CONS_INV_ID_TO | ReceivableApplicationAdjConsInvIdTo | — |
| CONS_INV_ID_TO | ReceivableApplicationConsInvIdTo | — |
| CUSTOMER_REASON | ReceivableApplicationAdjCustomerReason | — |
| CUSTOMER_REASON | ReceivableApplicationCustomerReason | — |
| CUSTOMER_REFERENCE | ReceivableApplicationAdjCustomerReference | — |
| CUSTOMER_REFERENCE | ReceivableApplicationCustomerReference | — |
| CUSTOMER_TRX_ID | ReceivableApplicationAdjCustomerTrxId | — |
| CUSTOMER_TRX_ID | ReceivableApplicationCustomerTrxId | — |
| DAYS_LATE | ReceivableApplicationAdjDaysLate | — |
| DAYS_LATE | ReceivableApplicationDaysLate | — |
| DISPLAY | ReceivableApplicationAdjDisplay | — |
| DISPLAY | ReceivableApplicationDisplay | — |
| EARNED_DISCOUNT_CCID | ReceivableApplicationAdjEarnedDiscountCcid | — |
| EARNED_DISCOUNT_CCID | ReceivableApplicationEarnedDiscountCcid | — |
| EARNED_DISCOUNT_TAKEN | ReceivableApplicationAdjEarnedDiscountTaken | — |
| EARNED_DISCOUNT_TAKEN | ReceivableApplicationEarnedDiscountTaken | — |
| EDISC_TAX_ACCT_RULE | ReceivableApplicationAdjEdiscTaxAcctRule | — |
| EDISC_TAX_ACCT_RULE | ReceivableApplicationEdiscTaxAcctRule | — |
| EVENT_ID | ReceivableApplicationAdjEventId | — |
| EVENT_ID | ReceivableApplicationEventId | — |
| EXCEPTION_REASON_CODE | ReceivableApplicationAdjExceptionReasonCode | — |
| EXCEPTION_REASON_CODE | ReceivableApplicationExceptionReasonCode | — |
| FREIGHT_APPLIED | ReceivableApplicationAdjFreightApplied | — |
| FREIGHT_APPLIED | ReceivableApplicationFreightApplied | — |
| FREIGHT_EDISCOUNTED | ReceivableApplicationAdjFreightEdiscounted | — |
| FREIGHT_EDISCOUNTED | ReceivableApplicationFreightEdiscounted | — |
| FREIGHT_UEDISCOUNTED | ReceivableApplicationAdjFreightUediscounted | — |
| FREIGHT_UEDISCOUNTED | ReceivableApplicationFreightUediscounted | — |
| GL_DATE | ReceivableApplicationAdjGlDate | — |
| GL_DATE | ReceivableApplicationGlDate | — |
| GL_POSTED_DATE | ReceivableApplicationAdjGlPostedDate | — |
| GL_POSTED_DATE | ReceivableApplicationGlPostedDate | — |
| LINE_APPLIED | ReceivableApplicationAdjLineApplied | — |
| LINE_APPLIED | ReceivableApplicationLineApplied | — |
| LINE_EDISCOUNTED | ReceivableApplicationAdjLineEdiscounted | — |
| LINE_EDISCOUNTED | ReceivableApplicationLineEdiscounted | — |
| LINE_UEDISCOUNTED | ReceivableApplicationAdjLineUediscounted | — |
| LINE_UEDISCOUNTED | ReceivableApplicationLineUediscounted | — |
| LINK_TO_CUSTOMER_TRX_ID | ReceivableApplicationAdjLinkToCustomerTrxId | — |
| LINK_TO_CUSTOMER_TRX_ID | ReceivableApplicationLinkToCustomerTrxId | — |
| LINK_TO_TRX_HIST_ID | ReceivableApplicationAdjLinkToTrxHistId | — |
| LINK_TO_TRX_HIST_ID | ReceivableApplicationLinkToTrxHistId | — |
| ON_ACCOUNT_CUSTOMER | ReceivableApplicationAdjOnAccountCustomer | — |
| ON_ACCOUNT_CUSTOMER | ReceivableApplicationOnAccountCustomer | — |
| ORG_ID | ReceivableApplicationAdjOrgId | — |
| ORG_ID | ReceivableApplicationOrgId | — |
| PAYMENT_SCHEDULE_ID | ReceivableApplicationAdjPaymentScheduleId | — |
| PAYMENT_SCHEDULE_ID | ReceivableApplicationPaymentScheduleId | — |
| PAYMENT_SET_ID | ReceivableApplicationAdjPaymentSetId | — |
| PAYMENT_SET_ID | ReceivableApplicationPaymentSetId | — |
| POSTABLE | ReceivableApplicationAdjPostable | — |
| POSTABLE | ReceivableApplicationPostable | — |
| POSTING_CONTROL_ID | ReceivableApplicationAdjPostingControlId | — |
| POSTING_CONTROL_ID | ReceivableApplicationPostingControlId | — |
| PROGRAM_APPLICATION_ID | ReceivableApplicationAdjProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | ReceivableApplicationProgramApplicationId | — |
| PROGRAM_ID | ReceivableApplicationAdjProgramId | — |
| PROGRAM_ID | ReceivableApplicationProgramId | — |
| PROGRAM_UPDATE_DATE | ReceivableApplicationAdjProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | ReceivableApplicationProgramUpdateDate | — |
| RECEIVABLE_APPLICATION_ID | ReceivableApplicationAdjReceivableApplicationId | — |
| RECEIVABLE_APPLICATION_ID | ReceivableApplicationReceivableApplicationId | — |
| RECEIVABLES_CHARGES_APPLIED | ReceivableApplicationAdjReceivablesChargesApplied | — |
| RECEIVABLES_CHARGES_APPLIED | ReceivableApplicationReceivablesChargesApplied | — |
| RECEIVABLES_TRX_ID | ReceivableApplicationAdjReceivablesTrxId | — |
| RECEIVABLES_TRX_ID | ReceivableApplicationReceivablesTrxId | — |
| REQUEST_ID | ReceivableApplicationAdjRequestId | — |
| REQUEST_ID | ReceivableApplicationRequestId | — |
| REVERSAL_GL_DATE | ReceivableApplicationAdjReversalGlDate | — |
| REVERSAL_GL_DATE | ReceivableApplicationReversalGlDate | — |
| RULE_SET_ID | ReceivableApplicationAdjRuleSetId | — |
| RULE_SET_ID | ReceivableApplicationRuleSetId | — |
| SECONDARY_APPLICATION_REF_ID | ReceivableApplicationAdjSecondaryApplicationRefId | — |
| SECONDARY_APPLICATION_REF_ID | ReceivableApplicationSecondaryApplicationRefId | — |
| SECONDARY_APPLICATION_REF_NUM | ReceivableApplicationAdjSecondaryApplicationRefNum | — |
| SECONDARY_APPLICATION_REF_NUM | ReceivableApplicationSecondaryApplicationRefNum | — |
| SECONDARY_APPLICATION_REF_TYPE | ReceivableApplicationAdjSecondaryApplicationRefType | — |
| SECONDARY_APPLICATION_REF_TYPE | ReceivableApplicationSecondaryApplicationRefType | — |
| SET_OF_BOOKS_ID | ReceivableApplicationAdjSetOfBooksId | — |
| SET_OF_BOOKS_ID | ReceivableApplicationSetOfBooksId | — |
| STATUS | ReceivableApplicationAdjStatus | — |
| STATUS | ReceivableApplicationStatus | — |
| TAX_APPLIED | ReceivableApplicationAdjTaxApplied | — |
| TAX_APPLIED | ReceivableApplicationTaxApplied | — |
| TAX_CODE | ReceivableApplicationAdjTaxCode | — |
| TAX_CODE | ReceivableApplicationTaxCode | — |
| TAX_EDISCOUNTED | ReceivableApplicationAdjTaxEdiscounted | — |
| TAX_EDISCOUNTED | ReceivableApplicationTaxEdiscounted | — |
| TAX_UEDISCOUNTED | ReceivableApplicationAdjTaxUediscounted | — |
| TAX_UEDISCOUNTED | ReceivableApplicationTaxUediscounted | — |
| TRANS_TO_RECEIPT_RATE | ReceivableApplicationAdjTransToReceiptRate | — |
| TRANS_TO_RECEIPT_RATE | ReceivableApplicationTransToReceiptRate | — |
| UNEARNED_DISCOUNT_CCID | ReceivableApplicationAdjUnearnedDiscountCcid | — |
| UNEARNED_DISCOUNT_CCID | ReceivableApplicationUnearnedDiscountCcid | — |
| UNEARNED_DISCOUNT_TAKEN | ReceivableApplicationAdjUnearnedDiscountTaken | — |
| UNEARNED_DISCOUNT_TAKEN | ReceivableApplicationUnearnedDiscountTaken | — |
| UNEDISC_TAX_ACCT_RULE | ReceivableApplicationAdjUnediscTaxAcctRule | — |
| UNEDISC_TAX_ACCT_RULE | ReceivableApplicationUnediscTaxAcctRule | — |
| UPGRADE_METHOD | ReceivableApplicationAdjUpgradeMethod | — |
| UPGRADE_METHOD | ReceivableApplicationUpgradeMethod | — |
| USSGL_TRANSACTION_CODE | ReceivableApplicationAdjUssglTransactionCode | — |
| USSGL_TRANSACTION_CODE | ReceivableApplicationUssglTransactionCode | — |
| USSGL_TRANSACTION_CODE_CONTEXT | ReceivableApplicationAdjUssglTransactionCodeContext | — |
| USSGL_TRANSACTION_CODE_CONTEXT | ReceivableApplicationUssglTransactionCodeContext | — |

### [[creditmemoapplicationdistributionpvo|CreditMemoApplicationDistributionPVO]] (AR · BICC: 24/168)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_APPLIED_FROM | ReceivableAppAppliedRecIdAcctdAmountAppliedFrom | — |
| ACCTD_AMOUNT_APPLIED_FROM | ReceivableApplicationAcctdAmountAppliedFrom | — |
| ACCTD_AMOUNT_APPLIED_TO | ReceivableAppAppliedRecIdAcctdAmountAppliedTo | — |
| ACCTD_AMOUNT_APPLIED_TO | ReceivableApplicationAcctdAmountAppliedTo | — |
| ACCTD_EARNED_DISCOUNT_TAKEN | ReceivableAppAppliedRecIdAcctdEarnedDiscountTaken | — |
| ACCTD_EARNED_DISCOUNT_TAKEN | ReceivableApplicationAcctdEarnedDiscountTaken | — |
| ACCTD_UNEARNED_DISCOUNT_TAKEN | ReceivableAppAppliedRecIdAcctdUnearnedDiscountTaken | — |
| ACCTD_UNEARNED_DISCOUNT_TAKEN | ReceivableApplicationAcctdUnearnedDiscountTaken | — |
| AMOUNT_APPLIED | ReceivableAppAppliedRecIdAmountApplied | — |
| AMOUNT_APPLIED | ReceivableApplicationAmountApplied | ✅ |
| AMOUNT_APPLIED_FROM | ReceivableAppAppliedRecIdAmountAppliedFrom | — |
| AMOUNT_APPLIED_FROM | ReceivableApplicationAmountAppliedFrom | — |
| APPLICATION_REF_ID | ReceivableAppAppliedRecIdApplicationRefId | — |
| APPLICATION_REF_ID | ReceivableApplicationApplicationRefId | — |
| APPLICATION_REF_NUM | ReceivableAppAppliedRecIdApplicationRefNum | — |
| APPLICATION_REF_NUM | ReceivableApplicationApplicationRefNum | — |
| APPLICATION_REF_REASON | ReceivableAppAppliedRecIdApplicationRefReason | — |
| APPLICATION_REF_REASON | ReceivableApplicationApplicationRefReason | — |
| APPLICATION_REF_TYPE | ReceivableAppAppliedRecIdApplicationRefType | — |
| APPLICATION_REF_TYPE | ReceivableApplicationApplicationRefType | — |
| APPLICATION_RULE | ReceivableAppAppliedRecIdApplicationRule | — |
| APPLICATION_RULE | ReceivableApplicationApplicationRule | — |
| APPLICATION_TYPE | ReceivableAppAppliedRecIdApplicationType | — |
| APPLICATION_TYPE | ReceivableApplicationApplicationType | ✅ |
| APPLIED_CUSTOMER_TRX_ID | ReceivableAppAppliedRecIdAppliedCustomerTrxId | — |
| APPLIED_CUSTOMER_TRX_ID | ReceivableApplicationAppliedCustomerTrxId | — |
| APPLIED_CUSTOMER_TRX_LINE_ID | ReceivableAppAppliedRecIdAppliedCustomerTrxLineId | — |
| APPLIED_CUSTOMER_TRX_LINE_ID | ReceivableApplicationAppliedCustomerTrxLineId | — |
| APPLIED_PAYMENT_SCHEDULE_ID | ReceivableAppAppliedRecIdAppliedPaymentScheduleId | — |
| APPLIED_PAYMENT_SCHEDULE_ID | ReceivableApplicationAppliedPaymentScheduleId | — |
| APPLIED_REC_APP_ID | ReceivableAppAppliedRecIdAppliedRecAppId | — |
| APPLIED_REC_APP_ID | ReceivableApplicationAppliedRecAppId | — |
| APPLY_DATE | ReceivableAppAppliedRecIdApplyDate | — |
| APPLY_DATE | ReceivableApplicationApplyDate | ✅ |
| CASH_RECEIPT_HISTORY_ID | ReceivableAppAppliedRecIdCashReceiptHistoryId | — |
| CASH_RECEIPT_HISTORY_ID | ReceivableApplicationCashReceiptHistoryId | — |
| CASH_RECEIPT_ID | ReceivableAppAppliedRecIdCashReceiptId | — |
| CASH_RECEIPT_ID | ReceivableApplicationCashReceiptId | — |
| CHARGEBACK_CUSTOMER_TRX_ID | ReceivableAppAppliedRecIdChargebackCustomerTrxId | — |
| CHARGEBACK_CUSTOMER_TRX_ID | ReceivableApplicationChargebackCustomerTrxId | — |
| CHARGES_EDISCOUNTED | ReceivableAppAppliedRecIdChargesEdiscounted | — |
| CHARGES_EDISCOUNTED | ReceivableApplicationChargesEdiscounted | — |
| CHARGES_UEDISCOUNTED | ReceivableAppAppliedRecIdChargesUediscounted | — |
| CHARGES_UEDISCOUNTED | ReceivableApplicationChargesUediscounted | — |
| CODE_COMBINATION_ID | ReceivableAppAppliedRecIdCodeCombinationId | — |
| CODE_COMBINATION_ID | ReceivableApplicationCodeCombinationId | — |
| COMMENTS | ReceivableAppAppliedRecIdComments | — |
| COMMENTS | ReceivableApplicationComments | ✅ |
| CONFIRMED_FLAG | ReceivableAppAppliedRecIdConfirmedFlag | — |
| CONFIRMED_FLAG | ReceivableApplicationConfirmedFlag | ✅ |
| CONS_INV_ID | ReceivableAppAppliedRecIdConsInvId | — |
| CONS_INV_ID | ReceivableApplicationConsInvId | — |
| CONS_INV_ID_TO | ReceivableAppAppliedRecIdConsInvIdTo | — |
| CONS_INV_ID_TO | ReceivableApplicationConsInvIdTo | — |
| CREATED_BY | ReceivableAppAppliedRecIdCreatedBy | — |
| CREATED_BY | ReceivableApplicationCreatedBy | ✅ |
| CREATION_DATE | ReceivableAppAppliedRecIdCreationDate | — |
| CREATION_DATE | ReceivableApplicationCreationDate | ✅ |
| CUSTOMER_REASON | ReceivableAppAppliedRecIdCustomerReason | — |
| CUSTOMER_REASON | ReceivableApplicationCustomerReason | ✅ |
| CUSTOMER_REFERENCE | ReceivableAppAppliedRecIdCustomerReference | — |
| CUSTOMER_REFERENCE | ReceivableApplicationCustomerReference | ✅ |
| CUSTOMER_TRX_ID | ReceivableAppAppliedRecIdCustomerTrxId | — |
| CUSTOMER_TRX_ID | ReceivableApplicationCustomerTrxId | — |
| DAYS_LATE | ReceivableAppAppliedRecIdDaysLate | — |
| DAYS_LATE | ReceivableApplicationDaysLate | — |
| DISPLAY | ReceivableAppAppliedRecIdDisplay | — |
| DISPLAY | ReceivableApplicationDisplay | ✅ |
| EARNED_DISCOUNT_CCID | ReceivableAppAppliedRecIdEarnedDiscountCcid | — |
| EARNED_DISCOUNT_CCID | ReceivableApplicationEarnedDiscountCcid | — |
| EARNED_DISCOUNT_TAKEN | ReceivableAppAppliedRecIdEarnedDiscountTaken | — |
| EARNED_DISCOUNT_TAKEN | ReceivableApplicationEarnedDiscountTaken | — |
| EDISC_TAX_ACCT_RULE | ReceivableAppAppliedRecIdEdiscTaxAcctRule | — |
| EDISC_TAX_ACCT_RULE | ReceivableApplicationEdiscTaxAcctRule | — |
| EVENT_ID | ReceivableAppAppliedRecIdEventId | — |
| EVENT_ID | ReceivableApplicationEventId | ✅ |
| EXCEPTION_REASON_CODE | ReceivableAppAppliedRecIdExceptionReasonCode | — |
| EXCEPTION_REASON_CODE | ReceivableApplicationExceptionReasonCode | — |
| FREIGHT_APPLIED | ReceivableAppAppliedRecIdFreightApplied | — |
| FREIGHT_APPLIED | ReceivableApplicationFreightApplied | — |
| FREIGHT_EDISCOUNTED | ReceivableAppAppliedRecIdFreightEdiscounted | — |
| FREIGHT_EDISCOUNTED | ReceivableApplicationFreightEdiscounted | — |
| FREIGHT_UEDISCOUNTED | ReceivableAppAppliedRecIdFreightUediscounted | — |
| FREIGHT_UEDISCOUNTED | ReceivableApplicationFreightUediscounted | — |
| GL_DATE | ReceivableAppAppliedRecIdGlDate | — |
| GL_DATE | ReceivableApplicationGlDate | ✅ |
| GL_POSTED_DATE | ReceivableAppAppliedRecIdGlPostedDate | — |
| GL_POSTED_DATE | ReceivableApplicationGlPostedDate | ✅ |
| LAST_UPDATE_DATE | ReceivableAppAppliedRecIdLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ReceivableApplicationLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ReceivableAppAppliedRecIdLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ReceivableApplicationLastUpdateLogin | — |
| LAST_UPDATED_BY | ReceivableAppAppliedRecIdLastUpdatedBy | — |
| LAST_UPDATED_BY | ReceivableApplicationLastUpdatedBy | ✅ |
| LINE_APPLIED | ReceivableAppAppliedRecIdLineApplied | — |
| LINE_APPLIED | ReceivableApplicationLineApplied | — |
| LINE_EDISCOUNTED | ReceivableAppAppliedRecIdLineEdiscounted | — |
| LINE_EDISCOUNTED | ReceivableApplicationLineEdiscounted | — |
| LINE_UEDISCOUNTED | ReceivableAppAppliedRecIdLineUediscounted | — |
| LINE_UEDISCOUNTED | ReceivableApplicationLineUediscounted | — |
| LINK_TO_CUSTOMER_TRX_ID | ReceivableAppAppliedRecIdLinkToCustomerTrxId | — |
| LINK_TO_CUSTOMER_TRX_ID | ReceivableApplicationLinkToCustomerTrxId | — |
| LINK_TO_TRX_HIST_ID | ReceivableAppAppliedRecIdLinkToTrxHistId | — |
| LINK_TO_TRX_HIST_ID | ReceivableApplicationLinkToTrxHistId | — |
| OBJECT_VERSION_NUMBER | ReceivableAppAppliedRecIdObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ReceivableApplicationObjectVersionNumber | — |
| ON_ACCOUNT_CUSTOMER | ReceivableAppAppliedRecIdOnAccountCustomer | — |
| ON_ACCOUNT_CUSTOMER | ReceivableApplicationOnAccountCustomer | — |
| ORG_ID | ReceivableAppAppliedRecIdOrgId | — |
| ORG_ID | ReceivableApplicationOrgId | ✅ |
| PAYMENT_SCHEDULE_ID | ReceivableAppAppliedRecIdPaymentScheduleId | — |
| PAYMENT_SCHEDULE_ID | ReceivableApplicationPaymentScheduleId | — |
| PAYMENT_SET_ID | ReceivableAppAppliedRecIdPaymentSetId | — |
| PAYMENT_SET_ID | ReceivableApplicationPaymentSetId | — |
| POSTABLE | ReceivableAppAppliedRecIdPostable | — |
| POSTABLE | ReceivableApplicationPostable | ✅ |
| POSTING_CONTROL_ID | ReceivableAppAppliedRecIdPostingControlId | — |
| POSTING_CONTROL_ID | ReceivableApplicationPostingControlId | ✅ |
| PROGRAM_APPLICATION_ID | ReceivableAppAppliedRecIdProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | ReceivableApplicationProgramApplicationId | — |
| PROGRAM_ID | ReceivableAppAppliedRecIdProgramId | — |
| PROGRAM_ID | ReceivableApplicationProgramId | — |
| PROGRAM_UPDATE_DATE | ReceivableAppAppliedRecIdProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | ReceivableApplicationProgramUpdateDate | — |
| RECEIVABLE_APPLICATION_ID | ReceivableAppAppliedRecIdReceivableApplicationId | — |
| RECEIVABLE_APPLICATION_ID | ReceivableApplicationReceivableApplicationId | ✅ |
| RECEIVABLES_CHARGES_APPLIED | ReceivableAppAppliedRecIdReceivablesChargesApplied | — |
| RECEIVABLES_CHARGES_APPLIED | ReceivableApplicationReceivablesChargesApplied | — |
| RECEIVABLES_TRX_ID | ReceivableAppAppliedRecIdReceivablesTrxId | — |
| RECEIVABLES_TRX_ID | ReceivableApplicationReceivablesTrxId | — |
| REQUEST_ID | ReceivableAppAppliedRecIdRequestId | — |
| REQUEST_ID | ReceivableApplicationRequestId | — |
| REVERSAL_GL_DATE | ReceivableAppAppliedRecIdReversalGlDate | — |
| REVERSAL_GL_DATE | ReceivableApplicationReversalGlDate | ✅ |
| RULE_SET_ID | ReceivableAppAppliedRecIdRuleSetId | — |
| RULE_SET_ID | ReceivableApplicationRuleSetId | — |
| SECONDARY_APPLICATION_REF_ID | ReceivableAppAppliedRecIdSecondaryApplicationRefId | — |
| SECONDARY_APPLICATION_REF_ID | ReceivableApplicationSecondaryApplicationRefId | — |
| SECONDARY_APPLICATION_REF_NUM | ReceivableAppAppliedRecIdSecondaryApplicationRefNum | — |
| SECONDARY_APPLICATION_REF_NUM | ReceivableApplicationSecondaryApplicationRefNum | — |
| SECONDARY_APPLICATION_REF_TYPE | ReceivableAppAppliedRecIdSecondaryApplicationRefType | — |
| SECONDARY_APPLICATION_REF_TYPE | ReceivableApplicationSecondaryApplicationRefType | — |
| SET_OF_BOOKS_ID | ReceivableAppAppliedRecIdSetOfBooksId | — |
| SET_OF_BOOKS_ID | ReceivableApplicationSetOfBooksId | ✅ |
| STATUS | ReceivableAppAppliedRecIdStatus | — |
| STATUS | ReceivableApplicationStatus | — |
| TAX_APPLIED | ReceivableAppAppliedRecIdTaxApplied | — |
| TAX_APPLIED | ReceivableApplicationTaxApplied | — |
| TAX_CODE | ReceivableAppAppliedRecIdTaxCode | — |
| TAX_CODE | ReceivableApplicationTaxCode | ✅ |
| TAX_EDISCOUNTED | ReceivableAppAppliedRecIdTaxEdiscounted | — |
| TAX_EDISCOUNTED | ReceivableApplicationTaxEdiscounted | — |
| TAX_UEDISCOUNTED | ReceivableAppAppliedRecIdTaxUediscounted | — |
| TAX_UEDISCOUNTED | ReceivableApplicationTaxUediscounted | — |
| TRANS_TO_RECEIPT_RATE | ReceivableAppAppliedRecIdTransToReceiptRate | — |
| TRANS_TO_RECEIPT_RATE | ReceivableApplicationTransToReceiptRate | ✅ |
| UNEARNED_DISCOUNT_CCID | ReceivableAppAppliedRecIdUnearnedDiscountCcid | — |
| UNEARNED_DISCOUNT_CCID | ReceivableApplicationUnearnedDiscountCcid | — |
| UNEARNED_DISCOUNT_TAKEN | ReceivableAppAppliedRecIdUnearnedDiscountTaken | — |
| UNEARNED_DISCOUNT_TAKEN | ReceivableApplicationUnearnedDiscountTaken | — |
| UNEDISC_TAX_ACCT_RULE | ReceivableAppAppliedRecIdUnediscTaxAcctRule | — |
| UNEDISC_TAX_ACCT_RULE | ReceivableApplicationUnediscTaxAcctRule | — |
| UPGRADE_METHOD | ReceivableAppAppliedRecIdUpgradeMethod | — |
| UPGRADE_METHOD | ReceivableApplicationUpgradeMethod | — |
| USSGL_TRANSACTION_CODE | ReceivableAppAppliedRecIdUssglTransactionCode | — |
| USSGL_TRANSACTION_CODE | ReceivableApplicationUssglTransactionCode | — |
| USSGL_TRANSACTION_CODE_CONTEXT | ReceivableAppAppliedRecIdUssglTransactionCodeContext | — |
| USSGL_TRANSACTION_CODE_CONTEXT | ReceivableApplicationUssglTransactionCodeContext | — |

### [[creditmemoapplicationpvo|CreditMemoApplicationPVO]] (AR · BICC: 26/84)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_APPLIED_FROM | ReceivableApplicationAcctdAmountAppliedFrom | ✅ |
| ACCTD_AMOUNT_APPLIED_TO | ReceivableApplicationAcctdAmountAppliedTo | ✅ |
| ACCTD_EARNED_DISCOUNT_TAKEN | ReceivableApplicationAcctdEarnedDiscountTaken | — |
| ACCTD_UNEARNED_DISCOUNT_TAKEN | ReceivableApplicationAcctdUnearnedDiscountTaken | — |
| AMOUNT_APPLIED | ReceivableApplicationAmountApplied | ✅ |
| AMOUNT_APPLIED_FROM | ReceivableApplicationAmountAppliedFrom | ✅ |
| APPLICATION_REF_ID | ReceivableApplicationApplicationRefId | — |
| APPLICATION_REF_NUM | ReceivableApplicationApplicationRefNum | — |
| APPLICATION_REF_REASON | ReceivableApplicationApplicationRefReason | — |
| APPLICATION_REF_TYPE | ReceivableApplicationApplicationRefType | — |
| APPLICATION_RULE | ReceivableApplicationApplicationRule | — |
| APPLICATION_TYPE | ReceivableApplicationApplicationType | ✅ |
| APPLIED_CUSTOMER_TRX_ID | ReceivableApplicationAppliedCustomerTrxId | — |
| APPLIED_CUSTOMER_TRX_LINE_ID | ReceivableApplicationAppliedCustomerTrxLineId | — |
| APPLIED_PAYMENT_SCHEDULE_ID | ReceivableApplicationAppliedPaymentScheduleId | — |
| APPLIED_REC_APP_ID | ReceivableApplicationAppliedRecAppId | — |
| APPLY_DATE | ReceivableApplicationApplyDate | ✅ |
| CASH_RECEIPT_HISTORY_ID | ReceivableApplicationCashReceiptHistoryId | — |
| CASH_RECEIPT_ID | ReceivableApplicationCashReceiptId | — |
| CHARGEBACK_CUSTOMER_TRX_ID | ReceivableApplicationChargebackCustomerTrxId | — |
| CHARGES_EDISCOUNTED | ReceivableApplicationChargesEdiscounted | — |
| CHARGES_UEDISCOUNTED | ReceivableApplicationChargesUediscounted | — |
| CODE_COMBINATION_ID | ReceivableApplicationCodeCombinationId | — |
| COMMENTS | ReceivableApplicationComments | ✅ |
| CONFIRMED_FLAG | ReceivableApplicationConfirmedFlag | — |
| CONS_INV_ID | ReceivableApplicationConsInvId | — |
| CONS_INV_ID_TO | ReceivableApplicationConsInvIdTo | — |
| CREATED_BY | ReceivableApplicationCreatedBy | ✅ |
| CREATION_DATE | ReceivableApplicationCreationDate | ✅ |
| CUSTOMER_REASON | ReceivableApplicationCustomerReason | ✅ |
| CUSTOMER_REFERENCE | ReceivableApplicationCustomerReference | ✅ |
| CUSTOMER_TRX_ID | ReceivableApplicationCustomerTrxId | — |
| DAYS_LATE | ReceivableApplicationDaysLate | — |
| DISPLAY | ReceivableApplicationDisplay | ✅ |
| EARNED_DISCOUNT_CCID | ReceivableApplicationEarnedDiscountCcid | — |
| EARNED_DISCOUNT_TAKEN | ReceivableApplicationEarnedDiscountTaken | — |
| EDISC_TAX_ACCT_RULE | ReceivableApplicationEdiscTaxAcctRule | — |
| EVENT_ID | ReceivableApplicationEventId | ✅ |
| EXCEPTION_REASON_CODE | ReceivableApplicationExceptionReasonCode | — |
| FREIGHT_APPLIED | ReceivableApplicationFreightApplied | ✅ |
| FREIGHT_EDISCOUNTED | ReceivableApplicationFreightEdiscounted | — |
| FREIGHT_UEDISCOUNTED | ReceivableApplicationFreightUediscounted | — |
| GL_DATE | ReceivableApplicationGlDate | ✅ |
| GL_POSTED_DATE | ReceivableApplicationGlPostedDate | ✅ |
| LAST_UPDATE_DATE | ReceivableApplicationLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ReceivableApplicationLastUpdateLogin | — |
| LAST_UPDATED_BY | ReceivableApplicationLastUpdatedBy | ✅ |
| LINE_APPLIED | ReceivableApplicationLineApplied | — |
| LINE_EDISCOUNTED | ReceivableApplicationLineEdiscounted | — |
| LINE_UEDISCOUNTED | ReceivableApplicationLineUediscounted | — |
| LINK_TO_CUSTOMER_TRX_ID | ReceivableApplicationLinkToCustomerTrxId | — |
| LINK_TO_TRX_HIST_ID | ReceivableApplicationLinkToTrxHistId | — |
| OBJECT_VERSION_NUMBER | ReceivableApplicationObjectVersionNumber | — |
| ON_ACCOUNT_CUSTOMER | ReceivableApplicationOnAccountCustomer | — |
| ORG_ID | ReceivableApplicationOrgId | — |
| PAYMENT_SCHEDULE_ID | ReceivableApplicationPaymentScheduleId | — |
| PAYMENT_SET_ID | ReceivableApplicationPaymentSetId | — |
| POSTABLE | ReceivableApplicationPostable | ✅ |
| POSTING_CONTROL_ID | ReceivableApplicationPostingControlId | ✅ |
| PROGRAM_APPLICATION_ID | ReceivableApplicationProgramApplicationId | — |
| PROGRAM_ID | ReceivableApplicationProgramId | — |
| PROGRAM_UPDATE_DATE | ReceivableApplicationProgramUpdateDate | — |
| RECEIVABLE_APPLICATION_ID | ReceivableApplicationId | ✅ |
| RECEIVABLES_CHARGES_APPLIED | ReceivableApplicationReceivablesChargesApplied | ✅ |
| RECEIVABLES_TRX_ID | ReceivableApplicationReceivablesTrxId | — |
| REQUEST_ID | ReceivableApplicationRequestId | — |
| REVERSAL_GL_DATE | ReceivableApplicationReversalGlDate | ✅ |
| RULE_SET_ID | ReceivableApplicationRuleSetId | — |
| SECONDARY_APPLICATION_REF_ID | ReceivableApplicationSecondaryApplicationRefId | — |
| SECONDARY_APPLICATION_REF_NUM | ReceivableApplicationSecondaryApplicationRefNum | — |
| SECONDARY_APPLICATION_REF_TYPE | ReceivableApplicationSecondaryApplicationRefType | — |
| SET_OF_BOOKS_ID | ReceivableApplicationSetOfBooksId | — |
| STATUS | ReceivableApplicationStatus | — |
| TAX_APPLIED | ReceivableApplicationTaxApplied | ✅ |
| TAX_CODE | ReceivableApplicationTaxCode | ✅ |
| TAX_EDISCOUNTED | ReceivableApplicationTaxEdiscounted | — |
| TAX_UEDISCOUNTED | ReceivableApplicationTaxUediscounted | — |
| TRANS_TO_RECEIPT_RATE | ReceivableApplicationTransToReceiptRate | ✅ |
| UNEARNED_DISCOUNT_CCID | ReceivableApplicationUnearnedDiscountCcid | — |
| UNEARNED_DISCOUNT_TAKEN | ReceivableApplicationUnearnedDiscountTaken | — |
| UNEDISC_TAX_ACCT_RULE | ReceivableApplicationUnediscTaxAcctRule | — |
| UPGRADE_METHOD | ReceivableApplicationUpgradeMethod | — |
| USSGL_TRANSACTION_CODE | ReceivableApplicationUssglTransactionCode | — |
| USSGL_TRANSACTION_CODE_CONTEXT | ReceivableApplicationUssglTransactionCodeContext | — |

### [[paymentschedulepvo|PaymentSchedulePVO]] (AR · BICC: 1/84)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_APPLIED_FROM | ReceivableApplicationAcctdAmountAppliedFrom | — |
| ACCTD_AMOUNT_APPLIED_TO | ReceivableApplicationAcctdAmountAppliedTo | — |
| ACCTD_EARNED_DISCOUNT_TAKEN | ReceivableApplicationAcctdEarnedDiscountTaken | — |
| ACCTD_UNEARNED_DISCOUNT_TAKEN | ReceivableApplicationAcctdUnearnedDiscountTaken | — |
| AMOUNT_APPLIED | ReceivableApplicationAmountApplied | — |
| AMOUNT_APPLIED_FROM | ReceivableApplicationAmountAppliedFrom | — |
| APPLICATION_REF_ID | ReceivableApplicationApplicationRefId | — |
| APPLICATION_REF_NUM | ReceivableApplicationApplicationRefNum | — |
| APPLICATION_REF_REASON | ReceivableApplicationApplicationRefReason | — |
| APPLICATION_REF_TYPE | ReceivableApplicationApplicationRefType | — |
| APPLICATION_RULE | ReceivableApplicationApplicationRule | — |
| APPLICATION_TYPE | ReceivableApplicationApplicationType | — |
| APPLIED_CUSTOMER_TRX_ID | ReceivableApplicationAppliedCustomerTrxId | — |
| APPLIED_CUSTOMER_TRX_LINE_ID | ReceivableApplicationAppliedCustomerTrxLineId | — |
| APPLIED_PAYMENT_SCHEDULE_ID | ReceivableApplicationAppliedPaymentScheduleId | — |
| APPLIED_REC_APP_ID | ReceivableApplicationAppliedRecAppId | — |
| APPLY_DATE | ReceivableApplicationApplyDate | — |
| CASH_RECEIPT_HISTORY_ID | ReceivableApplicationCashReceiptHistoryId | — |
| CASH_RECEIPT_ID | ReceivableApplicationCashReceiptId | — |
| CHARGEBACK_CUSTOMER_TRX_ID | ReceivableApplicationChargebackCustomerTrxId | — |
| CHARGES_EDISCOUNTED | ReceivableApplicationChargesEdiscounted | — |
| CHARGES_UEDISCOUNTED | ReceivableApplicationChargesUediscounted | — |
| CODE_COMBINATION_ID | ReceivableApplicationCodeCombinationId | — |
| COMMENTS | ReceivableApplicationComments | — |
| CONFIRMED_FLAG | ReceivableApplicationConfirmedFlag | — |
| CONS_INV_ID | ReceivableApplicationConsInvId | — |
| CONS_INV_ID_TO | ReceivableApplicationConsInvIdTo | — |
| CREATED_BY | ReceivableApplicationCreatedBy | — |
| CREATION_DATE | ReceivableApplicationCreationDate | — |
| CUSTOMER_REASON | ReceivableApplicationCustomerReason | — |
| CUSTOMER_REFERENCE | ReceivableApplicationCustomerReference | — |
| CUSTOMER_TRX_ID | ReceivableApplicationCustomerTrxId | — |
| DAYS_LATE | ReceivableApplicationDaysLate | — |
| DISPLAY | ReceivableApplicationDisplay | — |
| EARNED_DISCOUNT_CCID | ReceivableApplicationEarnedDiscountCcid | — |
| EARNED_DISCOUNT_TAKEN | ReceivableApplicationEarnedDiscountTaken | — |
| EDISC_TAX_ACCT_RULE | ReceivableApplicationEdiscTaxAcctRule | — |
| EVENT_ID | ReceivableApplicationEventId | — |
| EXCEPTION_REASON_CODE | ReceivableApplicationExceptionReasonCode | — |
| FREIGHT_APPLIED | ReceivableApplicationFreightApplied | — |
| FREIGHT_EDISCOUNTED | ReceivableApplicationFreightEdiscounted | — |
| FREIGHT_UEDISCOUNTED | ReceivableApplicationFreightUediscounted | — |
| GL_DATE | ReceivableApplicationGlDate | — |
| GL_POSTED_DATE | ReceivableApplicationGlPostedDate | — |
| LAST_UPDATE_DATE | ReceivableApplicationLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ReceivableApplicationLastUpdateLogin | — |
| LAST_UPDATED_BY | ReceivableApplicationLastUpdatedBy | — |
| LINE_APPLIED | ReceivableApplicationLineApplied | — |
| LINE_EDISCOUNTED | ReceivableApplicationLineEdiscounted | — |
| LINE_UEDISCOUNTED | ReceivableApplicationLineUediscounted | — |
| LINK_TO_CUSTOMER_TRX_ID | ReceivableApplicationLinkToCustomerTrxId | — |
| LINK_TO_TRX_HIST_ID | ReceivableApplicationLinkToTrxHistId | — |
| OBJECT_VERSION_NUMBER | ReceivableApplicationObjectVersionNumber | — |
| ON_ACCOUNT_CUSTOMER | ReceivableApplicationOnAccountCustomer | — |
| ORG_ID | ReceivableApplicationOrgId | — |
| PAYMENT_SCHEDULE_ID | ReceivableApplicationPaymentScheduleId | — |
| PAYMENT_SET_ID | ReceivableApplicationPaymentSetId | — |
| POSTABLE | ReceivableApplicationPostable | — |
| POSTING_CONTROL_ID | ReceivableApplicationPostingControlId | — |
| PROGRAM_APPLICATION_ID | ReceivableApplicationProgramApplicationId | — |
| PROGRAM_ID | ReceivableApplicationProgramId | — |
| PROGRAM_UPDATE_DATE | ReceivableApplicationProgramUpdateDate | — |
| RECEIVABLE_APPLICATION_ID | ReceivableApplicationReceivableApplicationId | — |
| RECEIVABLES_CHARGES_APPLIED | ReceivableApplicationReceivablesChargesApplied | — |
| RECEIVABLES_TRX_ID | ReceivableApplicationReceivablesTrxId | — |
| REQUEST_ID | ReceivableApplicationRequestId | — |
| REVERSAL_GL_DATE | ReceivableApplicationReversalGlDate | — |
| RULE_SET_ID | ReceivableApplicationRuleSetId | — |
| SECONDARY_APPLICATION_REF_ID | ReceivableApplicationSecondaryApplicationRefId | — |
| SECONDARY_APPLICATION_REF_NUM | ReceivableApplicationSecondaryApplicationRefNum | — |
| SECONDARY_APPLICATION_REF_TYPE | ReceivableApplicationSecondaryApplicationRefType | — |
| SET_OF_BOOKS_ID | ReceivableApplicationSetOfBooksId | — |
| STATUS | ReceivableApplicationStatus | — |
| TAX_APPLIED | ReceivableApplicationTaxApplied | — |
| TAX_CODE | ReceivableApplicationTaxCode | — |
| TAX_EDISCOUNTED | ReceivableApplicationTaxEdiscounted | — |
| TAX_UEDISCOUNTED | ReceivableApplicationTaxUediscounted | — |
| TRANS_TO_RECEIPT_RATE | ReceivableApplicationTransToReceiptRate | — |
| UNEARNED_DISCOUNT_CCID | ReceivableApplicationUnearnedDiscountCcid | — |
| UNEARNED_DISCOUNT_TAKEN | ReceivableApplicationUnearnedDiscountTaken | — |
| UNEDISC_TAX_ACCT_RULE | ReceivableApplicationUnediscTaxAcctRule | — |
| UPGRADE_METHOD | ReceivableApplicationUpgradeMethod | — |
| USSGL_TRANSACTION_CODE | ReceivableApplicationUssglTransactionCode | — |
| USSGL_TRANSACTION_CODE_CONTEXT | ReceivableApplicationUssglTransactionCodeContext | — |

### [[receiptapplicationdistributionpvo|ReceiptApplicationDistributionPVO]] (AR · BICC: 18/168)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_APPLIED_FROM | ReceiptApplicationAcctdAmountAppliedFrom | — |
| ACCTD_AMOUNT_APPLIED_FROM | ReceivableApplicationAcctdAmountAppliedFrom | — |
| ACCTD_AMOUNT_APPLIED_TO | ReceiptApplicationAcctdAmountAppliedTo | — |
| ACCTD_AMOUNT_APPLIED_TO | ReceivableApplicationAcctdAmountAppliedTo | — |
| ACCTD_EARNED_DISCOUNT_TAKEN | ReceiptApplicationAcctdEarnedDiscountTaken | — |
| ACCTD_EARNED_DISCOUNT_TAKEN | ReceivableApplicationAcctdEarnedDiscountTaken | — |
| ACCTD_UNEARNED_DISCOUNT_TAKEN | ReceiptApplicationAcctdUnearnedDiscountTaken | — |
| ACCTD_UNEARNED_DISCOUNT_TAKEN | ReceivableApplicationAcctdUnearnedDiscountTaken | — |
| AMOUNT_APPLIED | ReceiptApplicationAmountApplied | — |
| AMOUNT_APPLIED | ReceivableApplicationAmountApplied | — |
| AMOUNT_APPLIED_FROM | ReceiptApplicationAmountAppliedFrom | — |
| AMOUNT_APPLIED_FROM | ReceivableApplicationAmountAppliedFrom | — |
| APPLICATION_REF_ID | ReceiptApplicationApplicationRefId | — |
| APPLICATION_REF_ID | ReceivableApplicationApplicationRefId | — |
| APPLICATION_REF_NUM | ReceiptApplicationApplicationRefNum | — |
| APPLICATION_REF_NUM | ReceivableApplicationApplicationRefNum | — |
| APPLICATION_REF_REASON | ReceiptApplicationApplicationRefReason | — |
| APPLICATION_REF_REASON | ReceivableApplicationApplicationRefReason | — |
| APPLICATION_REF_TYPE | ReceiptApplicationApplicationRefType | — |
| APPLICATION_REF_TYPE | ReceivableApplicationApplicationRefType | — |
| APPLICATION_RULE | ReceiptApplicationApplicationRule | — |
| APPLICATION_RULE | ReceivableApplicationApplicationRule | — |
| APPLICATION_TYPE | ReceiptApplicationApplicationType | ✅ |
| APPLICATION_TYPE | ReceivableApplicationApplicationType | — |
| APPLIED_CUSTOMER_TRX_ID | ReceiptApplicationAppliedCustomerTrxId | ✅ |
| APPLIED_CUSTOMER_TRX_ID | ReceivableApplicationAppliedCustomerTrxId | — |
| APPLIED_CUSTOMER_TRX_LINE_ID | ReceiptApplicationAppliedCustomerTrxLineId | — |
| APPLIED_CUSTOMER_TRX_LINE_ID | ReceivableApplicationAppliedCustomerTrxLineId | — |
| APPLIED_PAYMENT_SCHEDULE_ID | ReceiptApplicationAppliedPaymentScheduleId | — |
| APPLIED_PAYMENT_SCHEDULE_ID | ReceivableApplicationAppliedPaymentScheduleId | — |
| APPLIED_REC_APP_ID | ReceiptApplicationAppliedRecAppId | — |
| APPLIED_REC_APP_ID | ReceivableApplicationAppliedRecAppId | — |
| APPLY_DATE | ReceiptApplicationApplyDate | ✅ |
| APPLY_DATE | ReceivableApplicationApplyDate | — |
| CASH_RECEIPT_HISTORY_ID | ReceiptApplicationCashReceiptHistoryId | — |
| CASH_RECEIPT_HISTORY_ID | ReceivableApplicationCashReceiptHistoryId | — |
| CASH_RECEIPT_ID | ReceiptApplicationCashReceiptId | ✅ |
| CASH_RECEIPT_ID | ReceivableApplicationCashReceiptId | — |
| CHARGEBACK_CUSTOMER_TRX_ID | ReceiptApplicationChargebackCustomerTrxId | — |
| CHARGEBACK_CUSTOMER_TRX_ID | ReceivableApplicationChargebackCustomerTrxId | — |
| CHARGES_EDISCOUNTED | ReceiptApplicationChargesEdiscounted | — |
| CHARGES_EDISCOUNTED | ReceivableApplicationChargesEdiscounted | — |
| CHARGES_UEDISCOUNTED | ReceiptApplicationChargesUediscounted | — |
| CHARGES_UEDISCOUNTED | ReceivableApplicationChargesUediscounted | — |
| CODE_COMBINATION_ID | ReceiptApplicationCodeCombinationId | — |
| CODE_COMBINATION_ID | ReceivableApplicationCodeCombinationId | — |
| COMMENTS | ReceiptApplicationComments | — |
| COMMENTS | ReceivableApplicationComments | — |
| CONFIRMED_FLAG | ReceiptApplicationConfirmedFlag | ✅ |
| CONFIRMED_FLAG | ReceivableApplicationConfirmedFlag | — |
| CONS_INV_ID | ReceiptApplicationConsInvId | — |
| CONS_INV_ID | ReceivableApplicationConsInvId | — |
| CONS_INV_ID_TO | ReceiptApplicationConsInvIdTo | — |
| CONS_INV_ID_TO | ReceivableApplicationConsInvIdTo | — |
| CREATED_BY | ReceiptApplicationCreatedBy | ✅ |
| CREATED_BY | ReceivableApplicationCreatedBy | — |
| CREATION_DATE | ReceiptApplicationCreationDate | ✅ |
| CREATION_DATE | ReceivableApplicationCreationDate | — |
| CUSTOMER_REASON | ReceiptApplicationCustomerReason | — |
| CUSTOMER_REASON | ReceivableApplicationCustomerReason | — |
| CUSTOMER_REFERENCE | ReceiptApplicationCustomerReference | — |
| CUSTOMER_REFERENCE | ReceivableApplicationCustomerReference | — |
| CUSTOMER_TRX_ID | ReceiptApplicationCustomerTrxId | — |
| CUSTOMER_TRX_ID | ReceivableApplicationCustomerTrxId | — |
| DAYS_LATE | ReceiptApplicationDaysLate | — |
| DAYS_LATE | ReceivableApplicationDaysLate | — |
| DISPLAY | ReceiptApplicationDisplay | — |
| DISPLAY | ReceivableApplicationDisplay | — |
| EARNED_DISCOUNT_CCID | ReceiptApplicationEarnedDiscountCcid | — |
| EARNED_DISCOUNT_CCID | ReceivableApplicationEarnedDiscountCcid | — |
| EARNED_DISCOUNT_TAKEN | ReceiptApplicationEarnedDiscountTaken | ✅ |
| EARNED_DISCOUNT_TAKEN | ReceivableApplicationEarnedDiscountTaken | — |
| EDISC_TAX_ACCT_RULE | ReceiptApplicationEdiscTaxAcctRule | — |
| EDISC_TAX_ACCT_RULE | ReceivableApplicationEdiscTaxAcctRule | — |
| EVENT_ID | ReceiptApplicationEventId | — |
| EVENT_ID | ReceivableApplicationEventId | — |
| EXCEPTION_REASON_CODE | ReceiptApplicationExceptionReasonCode | — |
| EXCEPTION_REASON_CODE | ReceivableApplicationExceptionReasonCode | — |
| FREIGHT_APPLIED | ReceiptApplicationFreightApplied | — |
| FREIGHT_APPLIED | ReceivableApplicationFreightApplied | — |
| FREIGHT_EDISCOUNTED | ReceiptApplicationFreightEdiscounted | — |
| FREIGHT_EDISCOUNTED | ReceivableApplicationFreightEdiscounted | — |
| FREIGHT_UEDISCOUNTED | ReceiptApplicationFreightUediscounted | — |
| FREIGHT_UEDISCOUNTED | ReceivableApplicationFreightUediscounted | — |
| GL_DATE | ReceiptApplicationGlDate | ✅ |
| GL_DATE | ReceivableApplicationGlDate | — |
| GL_POSTED_DATE | ReceiptApplicationGlPostedDate | ✅ |
| GL_POSTED_DATE | ReceivableApplicationGlPostedDate | — |
| LAST_UPDATE_DATE | ReceiptApplicationLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ReceivableApplicationLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ReceiptApplicationLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ReceivableApplicationLastUpdateLogin | — |
| LAST_UPDATED_BY | ReceiptApplicationLastUpdatedBy | ✅ |
| LAST_UPDATED_BY | ReceivableApplicationLastUpdatedBy | — |
| LINE_APPLIED | ReceiptApplicationLineApplied | — |
| LINE_APPLIED | ReceivableApplicationLineApplied | — |
| LINE_EDISCOUNTED | ReceiptApplicationLineEdiscounted | — |
| LINE_EDISCOUNTED | ReceivableApplicationLineEdiscounted | — |
| LINE_UEDISCOUNTED | ReceiptApplicationLineUediscounted | — |
| LINE_UEDISCOUNTED | ReceivableApplicationLineUediscounted | — |
| LINK_TO_CUSTOMER_TRX_ID | ReceiptApplicationLinkToCustomerTrxId | — |
| LINK_TO_CUSTOMER_TRX_ID | ReceivableApplicationLinkToCustomerTrxId | — |
| LINK_TO_TRX_HIST_ID | ReceiptApplicationLinkToTrxHistId | — |
| LINK_TO_TRX_HIST_ID | ReceivableApplicationLinkToTrxHistId | — |
| OBJECT_VERSION_NUMBER | ReceiptApplicationObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ReceivableApplicationObjectVersionNumber | — |
| ON_ACCOUNT_CUSTOMER | ReceiptApplicationOnAccountCustomer | — |
| ON_ACCOUNT_CUSTOMER | ReceivableApplicationOnAccountCustomer | — |
| ORG_ID | ReceiptApplicationOrgId | ✅ |
| ORG_ID | ReceivableApplicationOrgId | — |
| PAYMENT_SCHEDULE_ID | ReceiptApplicationPaymentScheduleId | — |
| PAYMENT_SCHEDULE_ID | ReceivableApplicationPaymentScheduleId | — |
| PAYMENT_SET_ID | ReceiptApplicationPaymentSetId | — |
| PAYMENT_SET_ID | ReceivableApplicationPaymentSetId | — |
| POSTABLE | ReceiptApplicationPostable | — |
| POSTABLE | ReceivableApplicationPostable | — |
| POSTING_CONTROL_ID | ReceiptApplicationPostingControlId | — |
| POSTING_CONTROL_ID | ReceivableApplicationPostingControlId | — |
| PROGRAM_APPLICATION_ID | ReceiptApplicationProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | ReceivableApplicationProgramApplicationId | — |
| PROGRAM_ID | ReceiptApplicationProgramId | — |
| PROGRAM_ID | ReceivableApplicationProgramId | — |
| PROGRAM_UPDATE_DATE | ReceiptApplicationProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | ReceivableApplicationProgramUpdateDate | — |
| RECEIVABLE_APPLICATION_ID | ReceiptApplicationReceivableApplicationId | ✅ |
| RECEIVABLE_APPLICATION_ID | ReceivableApplicationReceivableApplicationId | — |
| RECEIVABLES_CHARGES_APPLIED | ReceiptApplicationReceivablesChargesApplied | — |
| RECEIVABLES_CHARGES_APPLIED | ReceivableApplicationReceivablesChargesApplied | — |
| RECEIVABLES_TRX_ID | ReceiptApplicationReceivablesTrxId | — |
| RECEIVABLES_TRX_ID | ReceivableApplicationReceivablesTrxId | — |
| REQUEST_ID | ReceiptApplicationRequestId | — |
| REQUEST_ID | ReceivableApplicationRequestId | — |
| REVERSAL_GL_DATE | ReceiptApplicationReversalGlDate | — |
| REVERSAL_GL_DATE | ReceivableApplicationReversalGlDate | — |
| RULE_SET_ID | ReceiptApplicationRuleSetId | — |
| RULE_SET_ID | ReceivableApplicationRuleSetId | — |
| SECONDARY_APPLICATION_REF_ID | ReceiptApplicationSecondaryApplicationRefId | — |
| SECONDARY_APPLICATION_REF_ID | ReceivableApplicationSecondaryApplicationRefId | — |
| SECONDARY_APPLICATION_REF_NUM | ReceiptApplicationSecondaryApplicationRefNum | — |
| SECONDARY_APPLICATION_REF_NUM | ReceivableApplicationSecondaryApplicationRefNum | — |
| SECONDARY_APPLICATION_REF_TYPE | ReceiptApplicationSecondaryApplicationRefType | — |
| SECONDARY_APPLICATION_REF_TYPE | ReceivableApplicationSecondaryApplicationRefType | — |
| SET_OF_BOOKS_ID | ReceiptApplicationSetOfBooksId | ✅ |
| SET_OF_BOOKS_ID | ReceivableApplicationSetOfBooksId | — |
| STATUS | ReceiptApplicationStatus | ✅ |
| STATUS | ReceivableApplicationStatus | — |
| TAX_APPLIED | ReceiptApplicationTaxApplied | — |
| TAX_APPLIED | ReceivableApplicationTaxApplied | — |
| TAX_CODE | ReceiptApplicationTaxCode | — |
| TAX_CODE | ReceivableApplicationTaxCode | — |
| TAX_EDISCOUNTED | ReceiptApplicationTaxEdiscounted | — |
| TAX_EDISCOUNTED | ReceivableApplicationTaxEdiscounted | — |
| TAX_UEDISCOUNTED | ReceiptApplicationTaxUediscounted | — |
| TAX_UEDISCOUNTED | ReceivableApplicationTaxUediscounted | — |
| TRANS_TO_RECEIPT_RATE | ReceiptApplicationTransToReceiptRate | — |
| TRANS_TO_RECEIPT_RATE | ReceivableApplicationTransToReceiptRate | — |
| UNEARNED_DISCOUNT_CCID | ReceiptApplicationUnearnedDiscountCcid | — |
| UNEARNED_DISCOUNT_CCID | ReceivableApplicationUnearnedDiscountCcid | — |
| UNEARNED_DISCOUNT_TAKEN | ReceiptApplicationUnearnedDiscountTaken | ✅ |
| UNEARNED_DISCOUNT_TAKEN | ReceivableApplicationUnearnedDiscountTaken | — |
| UNEDISC_TAX_ACCT_RULE | ReceiptApplicationUnediscTaxAcctRule | — |
| UNEDISC_TAX_ACCT_RULE | ReceivableApplicationUnediscTaxAcctRule | — |
| UPGRADE_METHOD | ReceiptApplicationUpgradeMethod | — |
| UPGRADE_METHOD | ReceivableApplicationUpgradeMethod | — |
| USSGL_TRANSACTION_CODE | ReceiptApplicationUssglTransactionCode | — |
| USSGL_TRANSACTION_CODE | ReceivableApplicationUssglTransactionCode | — |
| USSGL_TRANSACTION_CODE_CONTEXT | ReceiptApplicationUssglTransactionCodeContext | — |
| USSGL_TRANSACTION_CODE_CONTEXT | ReceivableApplicationUssglTransactionCodeContext | — |

### [[receiptapplicationdistributionvc|ReceiptApplicationDistributionVC]] (AR · BICC: 27/168)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_APPLIED_FROM | ReceiptApplicationAcctdAmountAppliedFrom | — |
| ACCTD_AMOUNT_APPLIED_FROM | ReceivableApplicationAcctdAmountAppliedFrom | — |
| ACCTD_AMOUNT_APPLIED_TO | ReceiptApplicationAcctdAmountAppliedTo | — |
| ACCTD_AMOUNT_APPLIED_TO | ReceivableApplicationAcctdAmountAppliedTo | — |
| ACCTD_EARNED_DISCOUNT_TAKEN | ReceiptApplicationAcctdEarnedDiscountTaken | — |
| ACCTD_EARNED_DISCOUNT_TAKEN | ReceivableApplicationAcctdEarnedDiscountTaken | — |
| ACCTD_UNEARNED_DISCOUNT_TAKEN | ReceiptApplicationAcctdUnearnedDiscountTaken | — |
| ACCTD_UNEARNED_DISCOUNT_TAKEN | ReceivableApplicationAcctdUnearnedDiscountTaken | — |
| AMOUNT_APPLIED | ReceiptApplicationAmountApplied | — |
| AMOUNT_APPLIED | ReceivableApplicationAmountApplied | — |
| AMOUNT_APPLIED_FROM | ReceiptApplicationAmountAppliedFrom | — |
| AMOUNT_APPLIED_FROM | ReceivableApplicationAmountAppliedFrom | — |
| APPLICATION_REF_ID | ReceiptApplicationApplicationRefId | — |
| APPLICATION_REF_ID | ReceivableApplicationApplicationRefId | — |
| APPLICATION_REF_NUM | ReceiptApplicationApplicationRefNum | — |
| APPLICATION_REF_NUM | ReceivableApplicationApplicationRefNum | — |
| APPLICATION_REF_REASON | ReceiptApplicationApplicationRefReason | — |
| APPLICATION_REF_REASON | ReceivableApplicationApplicationRefReason | — |
| APPLICATION_REF_TYPE | ReceiptApplicationApplicationRefType | — |
| APPLICATION_REF_TYPE | ReceivableApplicationApplicationRefType | — |
| APPLICATION_RULE | ReceiptApplicationApplicationRule | — |
| APPLICATION_RULE | ReceivableApplicationApplicationRule | — |
| APPLICATION_TYPE | ReceiptApplicationApplicationType | ✅ |
| APPLICATION_TYPE | ReceivableApplicationApplicationType | — |
| APPLIED_CUSTOMER_TRX_ID | ReceiptApplicationAppliedCustomerTrxId | — |
| APPLIED_CUSTOMER_TRX_ID | ReceivableApplicationAppliedCustomerTrxId | — |
| APPLIED_CUSTOMER_TRX_LINE_ID | ReceiptApplicationAppliedCustomerTrxLineId | — |
| APPLIED_CUSTOMER_TRX_LINE_ID | ReceivableApplicationAppliedCustomerTrxLineId | — |
| APPLIED_PAYMENT_SCHEDULE_ID | ReceiptApplicationAppliedPaymentScheduleId | — |
| APPLIED_PAYMENT_SCHEDULE_ID | ReceivableApplicationAppliedPaymentScheduleId | ✅ |
| APPLIED_REC_APP_ID | ReceiptApplicationAppliedRecAppId | — |
| APPLIED_REC_APP_ID | ReceivableApplicationAppliedRecAppId | — |
| APPLY_DATE | ReceiptApplicationApplyDate | ✅ |
| APPLY_DATE | ReceivableApplicationApplyDate | — |
| CASH_RECEIPT_HISTORY_ID | ReceiptApplicationCashReceiptHistoryId | — |
| CASH_RECEIPT_HISTORY_ID | ReceivableApplicationCashReceiptHistoryId | — |
| CASH_RECEIPT_ID | ReceiptApplicationCashReceiptId | ✅ |
| CASH_RECEIPT_ID | ReceivableApplicationCashReceiptId | — |
| CHARGEBACK_CUSTOMER_TRX_ID | ReceiptApplicationChargebackCustomerTrxId | — |
| CHARGEBACK_CUSTOMER_TRX_ID | ReceivableApplicationChargebackCustomerTrxId | — |
| CHARGES_EDISCOUNTED | ReceiptApplicationChargesEdiscounted | — |
| CHARGES_EDISCOUNTED | ReceivableApplicationChargesEdiscounted | — |
| CHARGES_UEDISCOUNTED | ReceiptApplicationChargesUediscounted | — |
| CHARGES_UEDISCOUNTED | ReceivableApplicationChargesUediscounted | — |
| CODE_COMBINATION_ID | ReceiptApplicationCodeCombinationId | — |
| CODE_COMBINATION_ID | ReceivableApplicationCodeCombinationId | — |
| COMMENTS | ReceiptApplicationComments | ✅ |
| COMMENTS | ReceivableApplicationComments | — |
| CONFIRMED_FLAG | ReceiptApplicationConfirmedFlag | — |
| CONFIRMED_FLAG | ReceivableApplicationConfirmedFlag | — |
| CONS_INV_ID | ReceiptApplicationConsInvId | — |
| CONS_INV_ID | ReceivableApplicationConsInvId | — |
| CONS_INV_ID_TO | ReceiptApplicationConsInvIdTo | — |
| CONS_INV_ID_TO | ReceivableApplicationConsInvIdTo | — |
| CREATED_BY | ReceiptApplicationCreatedBy | ✅ |
| CREATED_BY | ReceivableApplicationCreatedBy | ✅ |
| CREATION_DATE | ReceiptApplicationCreationDate | ✅ |
| CREATION_DATE | ReceivableApplicationCreationDate | ✅ |
| CUSTOMER_REASON | ReceiptApplicationCustomerReason | ✅ |
| CUSTOMER_REASON | ReceivableApplicationCustomerReason | — |
| CUSTOMER_REFERENCE | ReceiptApplicationCustomerReference | ✅ |
| CUSTOMER_REFERENCE | ReceivableApplicationCustomerReference | — |
| CUSTOMER_TRX_ID | ReceiptApplicationCustomerTrxId | — |
| CUSTOMER_TRX_ID | ReceivableApplicationCustomerTrxId | — |
| DAYS_LATE | ReceiptApplicationDaysLate | ✅ |
| DAYS_LATE | ReceivableApplicationDaysLate | — |
| DISPLAY | ReceiptApplicationDisplay | ✅ |
| DISPLAY | ReceivableApplicationDisplay | — |
| EARNED_DISCOUNT_CCID | ReceiptApplicationEarnedDiscountCcid | — |
| EARNED_DISCOUNT_CCID | ReceivableApplicationEarnedDiscountCcid | — |
| EARNED_DISCOUNT_TAKEN | ReceiptApplicationEarnedDiscountTaken | — |
| EARNED_DISCOUNT_TAKEN | ReceivableApplicationEarnedDiscountTaken | — |
| EDISC_TAX_ACCT_RULE | ReceiptApplicationEdiscTaxAcctRule | — |
| EDISC_TAX_ACCT_RULE | ReceivableApplicationEdiscTaxAcctRule | — |
| EVENT_ID | ReceiptApplicationEventId | ✅ |
| EVENT_ID | ReceivableApplicationEventId | — |
| EXCEPTION_REASON_CODE | ReceiptApplicationExceptionReasonCode | ✅ |
| EXCEPTION_REASON_CODE | ReceivableApplicationExceptionReasonCode | — |
| FREIGHT_APPLIED | ReceiptApplicationFreightApplied | — |
| FREIGHT_APPLIED | ReceivableApplicationFreightApplied | — |
| FREIGHT_EDISCOUNTED | ReceiptApplicationFreightEdiscounted | — |
| FREIGHT_EDISCOUNTED | ReceivableApplicationFreightEdiscounted | — |
| FREIGHT_UEDISCOUNTED | ReceiptApplicationFreightUediscounted | — |
| FREIGHT_UEDISCOUNTED | ReceivableApplicationFreightUediscounted | — |
| GL_DATE | ReceiptApplicationGlDate | ✅ |
| GL_DATE | ReceivableApplicationGlDate | — |
| GL_POSTED_DATE | ReceiptApplicationGlPostedDate | ✅ |
| GL_POSTED_DATE | ReceivableApplicationGlPostedDate | — |
| LAST_UPDATE_DATE | ReceiptApplicationLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ReceivableApplicationLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ReceiptApplicationLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ReceivableApplicationLastUpdateLogin | — |
| LAST_UPDATED_BY | ReceiptApplicationLastUpdatedBy | ✅ |
| LAST_UPDATED_BY | ReceivableApplicationLastUpdatedBy | ✅ |
| LINE_APPLIED | ReceiptApplicationLineApplied | — |
| LINE_APPLIED | ReceivableApplicationLineApplied | — |
| LINE_EDISCOUNTED | ReceiptApplicationLineEdiscounted | — |
| LINE_EDISCOUNTED | ReceivableApplicationLineEdiscounted | — |
| LINE_UEDISCOUNTED | ReceiptApplicationLineUediscounted | — |
| LINE_UEDISCOUNTED | ReceivableApplicationLineUediscounted | — |
| LINK_TO_CUSTOMER_TRX_ID | ReceiptApplicationLinkToCustomerTrxId | — |
| LINK_TO_CUSTOMER_TRX_ID | ReceivableApplicationLinkToCustomerTrxId | — |
| LINK_TO_TRX_HIST_ID | ReceiptApplicationLinkToTrxHistId | — |
| LINK_TO_TRX_HIST_ID | ReceivableApplicationLinkToTrxHistId | — |
| OBJECT_VERSION_NUMBER | ReceiptApplicationObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ReceivableApplicationObjectVersionNumber | — |
| ON_ACCOUNT_CUSTOMER | ReceiptApplicationOnAccountCustomer | — |
| ON_ACCOUNT_CUSTOMER | ReceivableApplicationOnAccountCustomer | — |
| ORG_ID | ReceiptApplicationOrgId | — |
| ORG_ID | ReceivableApplicationOrgId | — |
| PAYMENT_SCHEDULE_ID | ReceiptApplicationPaymentScheduleId | — |
| PAYMENT_SCHEDULE_ID | ReceivableApplicationPaymentScheduleId | — |
| PAYMENT_SET_ID | ReceiptApplicationPaymentSetId | — |
| PAYMENT_SET_ID | ReceivableApplicationPaymentSetId | — |
| POSTABLE | ReceiptApplicationPostable | ✅ |
| POSTABLE | ReceivableApplicationPostable | — |
| POSTING_CONTROL_ID | ReceiptApplicationPostingControlId | ✅ |
| POSTING_CONTROL_ID | ReceivableApplicationPostingControlId | — |
| PROGRAM_APPLICATION_ID | ReceiptApplicationProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | ReceivableApplicationProgramApplicationId | — |
| PROGRAM_ID | ReceiptApplicationProgramId | — |
| PROGRAM_ID | ReceivableApplicationProgramId | — |
| PROGRAM_UPDATE_DATE | ReceiptApplicationProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | ReceivableApplicationProgramUpdateDate | — |
| RECEIVABLE_APPLICATION_ID | ReceiptApplicationReceivableApplicationId | ✅ |
| RECEIVABLE_APPLICATION_ID | ReceivableApplicationReceivableApplicationId | — |
| RECEIVABLES_CHARGES_APPLIED | ReceiptApplicationReceivablesChargesApplied | — |
| RECEIVABLES_CHARGES_APPLIED | ReceivableApplicationReceivablesChargesApplied | — |
| RECEIVABLES_TRX_ID | ReceiptApplicationReceivablesTrxId | — |
| RECEIVABLES_TRX_ID | ReceivableApplicationReceivablesTrxId | — |
| REQUEST_ID | ReceiptApplicationRequestId | — |
| REQUEST_ID | ReceivableApplicationRequestId | — |
| REVERSAL_GL_DATE | ReceiptApplicationReversalGlDate | ✅ |
| REVERSAL_GL_DATE | ReceivableApplicationReversalGlDate | — |
| RULE_SET_ID | ReceiptApplicationRuleSetId | — |
| RULE_SET_ID | ReceivableApplicationRuleSetId | — |
| SECONDARY_APPLICATION_REF_ID | ReceiptApplicationSecondaryApplicationRefId | — |
| SECONDARY_APPLICATION_REF_ID | ReceivableApplicationSecondaryApplicationRefId | — |
| SECONDARY_APPLICATION_REF_NUM | ReceiptApplicationSecondaryApplicationRefNum | — |
| SECONDARY_APPLICATION_REF_NUM | ReceivableApplicationSecondaryApplicationRefNum | — |
| SECONDARY_APPLICATION_REF_TYPE | ReceiptApplicationSecondaryApplicationRefType | — |
| SECONDARY_APPLICATION_REF_TYPE | ReceivableApplicationSecondaryApplicationRefType | — |
| SET_OF_BOOKS_ID | ReceiptApplicationSetOfBooksId | — |
| SET_OF_BOOKS_ID | ReceivableApplicationSetOfBooksId | — |
| STATUS | ReceiptApplicationStatus | — |
| STATUS | ReceivableApplicationStatus | — |
| TAX_APPLIED | ReceiptApplicationTaxApplied | — |
| TAX_APPLIED | ReceivableApplicationTaxApplied | — |
| TAX_CODE | ReceiptApplicationTaxCode | ✅ |
| TAX_CODE | ReceivableApplicationTaxCode | — |
| TAX_EDISCOUNTED | ReceiptApplicationTaxEdiscounted | — |
| TAX_EDISCOUNTED | ReceivableApplicationTaxEdiscounted | — |
| TAX_UEDISCOUNTED | ReceiptApplicationTaxUediscounted | — |
| TAX_UEDISCOUNTED | ReceivableApplicationTaxUediscounted | — |
| TRANS_TO_RECEIPT_RATE | ReceiptApplicationTransToReceiptRate | ✅ |
| TRANS_TO_RECEIPT_RATE | ReceivableApplicationTransToReceiptRate | — |
| UNEARNED_DISCOUNT_CCID | ReceiptApplicationUnearnedDiscountCcid | — |
| UNEARNED_DISCOUNT_CCID | ReceivableApplicationUnearnedDiscountCcid | — |
| UNEARNED_DISCOUNT_TAKEN | ReceiptApplicationUnearnedDiscountTaken | — |
| UNEARNED_DISCOUNT_TAKEN | ReceivableApplicationUnearnedDiscountTaken | — |
| UNEDISC_TAX_ACCT_RULE | ReceiptApplicationUnediscTaxAcctRule | — |
| UNEDISC_TAX_ACCT_RULE | ReceivableApplicationUnediscTaxAcctRule | — |
| UPGRADE_METHOD | ReceiptApplicationUpgradeMethod | — |
| UPGRADE_METHOD | ReceivableApplicationUpgradeMethod | — |
| USSGL_TRANSACTION_CODE | ReceiptApplicationUssglTransactionCode | — |
| USSGL_TRANSACTION_CODE | ReceivableApplicationUssglTransactionCode | — |
| USSGL_TRANSACTION_CODE_CONTEXT | ReceiptApplicationUssglTransactionCodeContext | — |
| USSGL_TRANSACTION_CODE_CONTEXT | ReceivableApplicationUssglTransactionCodeContext | — |

### [[receiptapplicationpvo|ReceiptApplicationPVO]] (AR · BICC: 45/168)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_APPLIED_FROM | AppRcvAppAcctdAmountAppliedFrom | — |
| ACCTD_AMOUNT_APPLIED_FROM | ReceivableApplicationAcctdAmountAppliedFrom | ✅ |
| ACCTD_AMOUNT_APPLIED_TO | AppRcvAppAcctdAmountAppliedTo | — |
| ACCTD_AMOUNT_APPLIED_TO | ReceivableApplicationAcctdAmountAppliedTo | ✅ |
| ACCTD_EARNED_DISCOUNT_TAKEN | AppRcvAppAcctdEarnedDiscountTaken | — |
| ACCTD_EARNED_DISCOUNT_TAKEN | ReceivableApplicationAcctdEarnedDiscountTaken | ✅ |
| ACCTD_UNEARNED_DISCOUNT_TAKEN | AppRcvAppAcctdUnearnedDiscountTaken | — |
| ACCTD_UNEARNED_DISCOUNT_TAKEN | ReceivableApplicationAcctdUnearnedDiscountTaken | ✅ |
| AMOUNT_APPLIED | AppRcvAppAmountApplied | — |
| AMOUNT_APPLIED | ReceivableApplicationAmountApplied | ✅ |
| AMOUNT_APPLIED_FROM | AppRcvAppAmountAppliedFrom | — |
| AMOUNT_APPLIED_FROM | ReceivableApplicationAmountAppliedFrom | ✅ |
| APPLICATION_REF_ID | AppRcvAppApplicationRefId | — |
| APPLICATION_REF_ID | ReceivableApplicationApplicationRefId | — |
| APPLICATION_REF_NUM | AppRcvAppApplicationRefNum | — |
| APPLICATION_REF_NUM | ReceivableApplicationApplicationRefNum | — |
| APPLICATION_REF_REASON | AppRcvAppApplicationRefReason | — |
| APPLICATION_REF_REASON | ReceivableApplicationApplicationRefReason | — |
| APPLICATION_REF_TYPE | AppRcvAppApplicationRefType | — |
| APPLICATION_REF_TYPE | ReceivableApplicationApplicationRefType | — |
| APPLICATION_RULE | AppRcvAppApplicationRule | — |
| APPLICATION_RULE | ReceivableApplicationApplicationRule | — |
| APPLICATION_TYPE | AppRcvAppApplicationType | — |
| APPLICATION_TYPE | ReceivableApplicationApplicationType | ✅ |
| APPLIED_CUSTOMER_TRX_ID | AppRcvAppAppliedCustomerTrxId | — |
| APPLIED_CUSTOMER_TRX_ID | ReceivableApplicationAppliedCustomerTrxId | — |
| APPLIED_CUSTOMER_TRX_LINE_ID | AppRcvAppAppliedCustomerTrxLineId | — |
| APPLIED_CUSTOMER_TRX_LINE_ID | ReceivableApplicationAppliedCustomerTrxLineId | — |
| APPLIED_PAYMENT_SCHEDULE_ID | AppRcvAppAppliedPaymentScheduleId | — |
| APPLIED_PAYMENT_SCHEDULE_ID | ReceivableApplicationAppliedPaymentScheduleId | ✅ |
| APPLIED_REC_APP_ID | AppRcvAppAppliedRecAppId | — |
| APPLIED_REC_APP_ID | ReceivableApplicationAppliedRecAppId | — |
| APPLY_DATE | AppRcvAppApplyDate | — |
| APPLY_DATE | ReceivableApplicationApplyDate | ✅ |
| CASH_RECEIPT_HISTORY_ID | AppRcvAppCashReceiptHistoryId | — |
| CASH_RECEIPT_HISTORY_ID | ReceivableApplicationCashReceiptHistoryId | — |
| CASH_RECEIPT_ID | AppRcvAppCashReceiptId | — |
| CASH_RECEIPT_ID | ReceivableApplicationCashReceiptId | ✅ |
| CHARGEBACK_CUSTOMER_TRX_ID | AppRcvAppChargebackCustomerTrxId | — |
| CHARGEBACK_CUSTOMER_TRX_ID | ReceivableApplicationChargebackCustomerTrxId | — |
| CHARGES_EDISCOUNTED | AppRcvAppChargesEdiscounted | — |
| CHARGES_EDISCOUNTED | ReceivableApplicationChargesEdiscounted | ✅ |
| CHARGES_UEDISCOUNTED | AppRcvAppChargesUediscounted | — |
| CHARGES_UEDISCOUNTED | ReceivableApplicationChargesUediscounted | ✅ |
| CODE_COMBINATION_ID | AppRcvAppCodeCombinationId | — |
| CODE_COMBINATION_ID | ReceivableApplicationCodeCombinationId | — |
| COMMENTS | AppRcvAppComments | — |
| COMMENTS | ReceivableApplicationComments | ✅ |
| CONFIRMED_FLAG | AppRcvAppConfirmedFlag | — |
| CONFIRMED_FLAG | ReceivableApplicationConfirmedFlag | — |
| CONS_INV_ID | AppRcvAppConsInvId | — |
| CONS_INV_ID | ReceivableApplicationConsInvId | — |
| CONS_INV_ID_TO | AppRcvAppConsInvIdTo | — |
| CONS_INV_ID_TO | ReceivableApplicationConsInvIdTo | — |
| CREATED_BY | AppRcvAppCreatedBy | — |
| CREATED_BY | ReceivableApplicationCreatedBy | ✅ |
| CREATION_DATE | AppRcvAppCreationDate | — |
| CREATION_DATE | ReceivableApplicationCreationDate | ✅ |
| CUSTOMER_REASON | AppRcvAppCustomerReason | — |
| CUSTOMER_REASON | ReceivableApplicationCustomerReason | ✅ |
| CUSTOMER_REFERENCE | AppRcvAppCustomerReference | — |
| CUSTOMER_REFERENCE | ReceivableApplicationCustomerReference | ✅ |
| CUSTOMER_TRX_ID | AppRcvAppCustomerTrxId | — |
| CUSTOMER_TRX_ID | ReceivableApplicationCustomerTrxId | — |
| DAYS_LATE | AppRcvAppDaysLate | — |
| DAYS_LATE | ReceivableApplicationDaysLate | ✅ |
| DISPLAY | AppRcvAppDisplay | — |
| DISPLAY | ReceivableApplicationDisplay | ✅ |
| EARNED_DISCOUNT_CCID | AppRcvAppEarnedDiscountCcid | — |
| EARNED_DISCOUNT_CCID | ReceivableApplicationEarnedDiscountCcid | — |
| EARNED_DISCOUNT_TAKEN | AppRcvAppEarnedDiscountTaken | — |
| EARNED_DISCOUNT_TAKEN | ReceivableApplicationEarnedDiscountTaken | ✅ |
| EDISC_TAX_ACCT_RULE | AppRcvAppEdiscTaxAcctRule | — |
| EDISC_TAX_ACCT_RULE | ReceivableApplicationEdiscTaxAcctRule | — |
| EVENT_ID | AppRcvAppEventId | — |
| EVENT_ID | ReceivableApplicationEventId | ✅ |
| EXCEPTION_REASON_CODE | AppRcvAppExceptionReasonCode | — |
| EXCEPTION_REASON_CODE | ReceivableApplicationExceptionReasonCode | ✅ |
| FREIGHT_APPLIED | AppRcvAppFreightApplied | — |
| FREIGHT_APPLIED | ReceivableApplicationFreightApplied | ✅ |
| FREIGHT_EDISCOUNTED | AppRcvAppFreightEdiscounted | — |
| FREIGHT_EDISCOUNTED | ReceivableApplicationFreightEdiscounted | ✅ |
| FREIGHT_UEDISCOUNTED | AppRcvAppFreightUediscounted | — |
| FREIGHT_UEDISCOUNTED | ReceivableApplicationFreightUediscounted | ✅ |
| GL_DATE | AppRcvAppGlDate | — |
| GL_DATE | ReceivableApplicationGlDate | ✅ |
| GL_POSTED_DATE | AppRcvAppGlPostedDate | — |
| GL_POSTED_DATE | ReceivableApplicationGlPostedDate | ✅ |
| LAST_UPDATE_DATE | AppRcvAppLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ReceivableApplicationLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AppRcvAppLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ReceivableApplicationLastUpdateLogin | — |
| LAST_UPDATED_BY | AppRcvAppLastUpdatedBy | — |
| LAST_UPDATED_BY | ReceivableApplicationLastUpdatedBy | ✅ |
| LINE_APPLIED | AppRcvAppLineApplied | — |
| LINE_APPLIED | ReceivableApplicationLineApplied | ✅ |
| LINE_EDISCOUNTED | AppRcvAppLineEdiscounted | — |
| LINE_EDISCOUNTED | ReceivableApplicationLineEdiscounted | ✅ |
| LINE_UEDISCOUNTED | AppRcvAppLineUediscounted | — |
| LINE_UEDISCOUNTED | ReceivableApplicationLineUediscounted | ✅ |
| LINK_TO_CUSTOMER_TRX_ID | AppRcvAppLinkToCustomerTrxId | — |
| LINK_TO_CUSTOMER_TRX_ID | ReceivableApplicationLinkToCustomerTrxId | — |
| LINK_TO_TRX_HIST_ID | AppRcvAppLinkToTrxHistId | — |
| LINK_TO_TRX_HIST_ID | ReceivableApplicationLinkToTrxHistId | — |
| OBJECT_VERSION_NUMBER | AppRcvAppObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ReceivableApplicationObjectVersionNumber | — |
| ON_ACCOUNT_CUSTOMER | AppRcvAppOnAccountCustomer | — |
| ON_ACCOUNT_CUSTOMER | ReceivableApplicationOnAccountCustomer | — |
| ORG_ID | AppRcvAppOrgId | — |
| ORG_ID | ReceivableApplicationOrgId | — |
| PAYMENT_SCHEDULE_ID | AppRcvAppPaymentScheduleId | — |
| PAYMENT_SCHEDULE_ID | ReceivableApplicationPaymentScheduleId | — |
| PAYMENT_SET_ID | AppRcvAppPaymentSetId | — |
| PAYMENT_SET_ID | ReceivableApplicationPaymentSetId | — |
| POSTABLE | AppRcvAppPostable | — |
| POSTABLE | ReceivableApplicationPostable | ✅ |
| POSTING_CONTROL_ID | AppRcvAppPostingControlId | — |
| POSTING_CONTROL_ID | ReceivableApplicationPostingControlId | ✅ |
| PROGRAM_APPLICATION_ID | AppRcvAppProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | ReceivableApplicationProgramApplicationId | — |
| PROGRAM_ID | AppRcvAppProgramId | — |
| PROGRAM_ID | ReceivableApplicationProgramId | — |
| PROGRAM_UPDATE_DATE | AppRcvAppProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | ReceivableApplicationProgramUpdateDate | — |
| RECEIVABLE_APPLICATION_ID | AppRcvAppReceivableApplicationId | — |
| RECEIVABLE_APPLICATION_ID | ReceivableApplicationId | ✅ |
| RECEIVABLES_CHARGES_APPLIED | AppRcvAppReceivablesChargesApplied | — |
| RECEIVABLES_CHARGES_APPLIED | ReceivableApplicationReceivablesChargesApplied | ✅ |
| RECEIVABLES_TRX_ID | AppRcvAppReceivablesTrxId | — |
| RECEIVABLES_TRX_ID | ReceivableApplicationReceivablesTrxId | — |
| REQUEST_ID | AppRcvAppRequestId | — |
| REQUEST_ID | ReceivableApplicationRequestId | — |
| REVERSAL_GL_DATE | AppRcvAppReversalGlDate | — |
| REVERSAL_GL_DATE | ReceivableApplicationReversalGlDate | ✅ |
| RULE_SET_ID | AppRcvAppRuleSetId | — |
| RULE_SET_ID | ReceivableApplicationRuleSetId | — |
| SECONDARY_APPLICATION_REF_ID | AppRcvAppSecondaryApplicationRefId | — |
| SECONDARY_APPLICATION_REF_ID | ReceivableApplicationSecondaryApplicationRefId | — |
| SECONDARY_APPLICATION_REF_NUM | AppRcvAppSecondaryApplicationRefNum | — |
| SECONDARY_APPLICATION_REF_NUM | ReceivableApplicationSecondaryApplicationRefNum | — |
| SECONDARY_APPLICATION_REF_TYPE | AppRcvAppSecondaryApplicationRefType | — |
| SECONDARY_APPLICATION_REF_TYPE | ReceivableApplicationSecondaryApplicationRefType | — |
| SET_OF_BOOKS_ID | AppRcvAppSetOfBooksId | — |
| SET_OF_BOOKS_ID | ReceivableApplicationSetOfBooksId | — |
| STATUS | AppRcvAppStatus | — |
| STATUS | ReceivableApplicationStatus | ✅ |
| TAX_APPLIED | AppRcvAppTaxApplied | — |
| TAX_APPLIED | ReceivableApplicationTaxApplied | ✅ |
| TAX_CODE | AppRcvAppTaxCode | — |
| TAX_CODE | ReceivableApplicationTaxCode | ✅ |
| TAX_EDISCOUNTED | AppRcvAppTaxEdiscounted | — |
| TAX_EDISCOUNTED | ReceivableApplicationTaxEdiscounted | ✅ |
| TAX_UEDISCOUNTED | AppRcvAppTaxUediscounted | — |
| TAX_UEDISCOUNTED | ReceivableApplicationTaxUediscounted | ✅ |
| TRANS_TO_RECEIPT_RATE | AppRcvAppTransToReceiptRate | — |
| TRANS_TO_RECEIPT_RATE | ReceivableApplicationTransToReceiptRate | ✅ |
| UNEARNED_DISCOUNT_CCID | AppRcvAppUnearnedDiscountCcid | — |
| UNEARNED_DISCOUNT_CCID | ReceivableApplicationUnearnedDiscountCcid | — |
| UNEARNED_DISCOUNT_TAKEN | AppRcvAppUnearnedDiscountTaken | — |
| UNEARNED_DISCOUNT_TAKEN | ReceivableApplicationUnearnedDiscountTaken | ✅ |
| UNEDISC_TAX_ACCT_RULE | AppRcvAppUnediscTaxAcctRule | — |
| UNEDISC_TAX_ACCT_RULE | ReceivableApplicationUnediscTaxAcctRule | — |
| UPGRADE_METHOD | AppRcvAppUpgradeMethod | — |
| UPGRADE_METHOD | ReceivableApplicationUpgradeMethod | — |
| USSGL_TRANSACTION_CODE | AppRcvAppUssglTransactionCode | — |
| USSGL_TRANSACTION_CODE | ReceivableApplicationUssglTransactionCode | — |
| USSGL_TRANSACTION_CODE_CONTEXT | AppRcvAppUssglTransactionCodeContext | — |
| USSGL_TRANSACTION_CODE_CONTEXT | ReceivableApplicationUssglTransactionCodeContext | — |

### [[receivableapplicationextractpvo|ReceivableApplicationExtractPVO]] (OTHER · BICC: 82/129)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_APPLIED_FROM | ArReceivableApplicationAcctdAmountAppliedFrom | ✅ |
| ACCTD_AMOUNT_APPLIED_TO | ArReceivableApplicationAcctdAmountAppliedTo | ✅ |
| ACCTD_EARNED_DISCOUNT_TAKEN | ArReceivableApplicationAcctdEarnedDiscountTaken | ✅ |
| ACCTD_UNEARNED_DISCOUNT_TAKEN | ArReceivableApplicationAcctdUnearnedDiscountTaken | ✅ |
| AMOUNT_APPLIED | ArReceivableApplicationAmountApplied | ✅ |
| AMOUNT_APPLIED_FROM | ArReceivableApplicationAmountAppliedFrom | ✅ |
| APPLICATION_REF_ID | ArReceivableApplicationApplicationRefId | ✅ |
| APPLICATION_REF_NUM | ArReceivableApplicationApplicationRefNum | ✅ |
| APPLICATION_REF_REASON | ArReceivableApplicationApplicationRefReason | ✅ |
| APPLICATION_REF_TYPE | ArReceivableApplicationApplicationRefType | ✅ |
| APPLICATION_RULE | ArReceivableApplicationApplicationRule | ✅ |
| APPLICATION_TYPE | ArReceivableApplicationApplicationType | ✅ |
| APPLIED_CUSTOMER_TRX_ID | ArReceivableApplicationAppliedCustomerTrxId | ✅ |
| APPLIED_CUSTOMER_TRX_LINE_ID | ArReceivableApplicationAppliedCustomerTrxLineId | ✅ |
| APPLIED_PAYMENT_SCHEDULE_ID | ArReceivableApplicationAppliedPaymentScheduleId | ✅ |
| APPLIED_REC_APP_ID | ArReceivableApplicationAppliedRecAppId | ✅ |
| APPLY_DATE | ArReceivableApplicationApplyDate | ✅ |
| ATTRIBUTE1 | ArReceivableApplicationAttribute1 | — |
| ATTRIBUTE10 | ArReceivableApplicationAttribute10 | — |
| ATTRIBUTE11 | ArReceivableApplicationAttribute11 | — |
| ATTRIBUTE12 | ArReceivableApplicationAttribute12 | — |
| ATTRIBUTE13 | ArReceivableApplicationAttribute13 | — |
| ATTRIBUTE14 | ArReceivableApplicationAttribute14 | — |
| ATTRIBUTE15 | ArReceivableApplicationAttribute15 | — |
| ATTRIBUTE2 | ArReceivableApplicationAttribute2 | — |
| ATTRIBUTE3 | ArReceivableApplicationAttribute3 | — |
| ATTRIBUTE4 | ArReceivableApplicationAttribute4 | — |
| ATTRIBUTE5 | ArReceivableApplicationAttribute5 | — |
| ATTRIBUTE6 | ArReceivableApplicationAttribute6 | — |
| ATTRIBUTE7 | ArReceivableApplicationAttribute7 | — |
| ATTRIBUTE8 | ArReceivableApplicationAttribute8 | — |
| ATTRIBUTE9 | ArReceivableApplicationAttribute9 | — |
| ATTRIBUTE_CATEGORY | ArReceivableApplicationAttributeCategory | — |
| CASH_RECEIPT_HISTORY_ID | ArReceivableApplicationCashReceiptHistoryId | ✅ |
| CASH_RECEIPT_ID | ArReceivableApplicationCashReceiptId | ✅ |
| CHARGES_EDISCOUNTED | ArReceivableApplicationChargesEdiscounted | ✅ |
| CHARGES_UEDISCOUNTED | ArReceivableApplicationChargesUediscounted | ✅ |
| CODE_COMBINATION_ID | ArReceivableApplicationCodeCombinationId | ✅ |
| COMMENTS | ArReceivableApplicationComments | ✅ |
| CONFIRMED_FLAG | ArReceivableApplicationConfirmedFlag | ✅ |
| CONS_INV_ID | ArReceivableApplicationConsInvId | ✅ |
| CONS_INV_ID_TO | ArReceivableApplicationConsInvIdTo | ✅ |
| CREATED_BY | ArReceivableApplicationCreatedBy | ✅ |
| CREATION_DATE | ArReceivableApplicationCreationDate | ✅ |
| CUSTOMER_REASON | ArReceivableApplicationCustomerReason | ✅ |
| CUSTOMER_REFERENCE | ArReceivableApplicationCustomerReference | ✅ |
| CUSTOMER_TRX_ID | ArReceivableApplicationCustomerTrxId | ✅ |
| DAYS_LATE | ArReceivableApplicationDaysLate | ✅ |
| DISPLAY | ArReceivableApplicationDisplay | ✅ |
| EARNED_DISCOUNT_CCID | ArReceivableApplicationEarnedDiscountCcid | ✅ |
| EARNED_DISCOUNT_TAKEN | ArReceivableApplicationEarnedDiscountTaken | ✅ |
| EDISC_TAX_ACCT_RULE | ArReceivableApplicationEdiscTaxAcctRule | ✅ |
| EVENT_ID | ArReceivableApplicationEventId | ✅ |
| EXCEPTION_REASON_CODE | ArReceivableApplicationExceptionReasonCode | ✅ |
| FREIGHT_APPLIED | ArReceivableApplicationFreightApplied | ✅ |
| FREIGHT_EDISCOUNTED | ArReceivableApplicationFreightEdiscounted | ✅ |
| FREIGHT_UEDISCOUNTED | ArReceivableApplicationFreightUediscounted | ✅ |
| GL_DATE | ArReceivableApplicationGlDate | ✅ |
| GL_POSTED_DATE | ArReceivableApplicationGlPostedDate | ✅ |
| GLOBAL_ATTRIBUTE1 | ArReceivableApplicationGlobalAttribute1 | — |
| GLOBAL_ATTRIBUTE10 | ArReceivableApplicationGlobalAttribute10 | — |
| GLOBAL_ATTRIBUTE11 | ArReceivableApplicationGlobalAttribute11 | — |
| GLOBAL_ATTRIBUTE12 | ArReceivableApplicationGlobalAttribute12 | — |
| GLOBAL_ATTRIBUTE13 | ArReceivableApplicationGlobalAttribute13 | — |
| GLOBAL_ATTRIBUTE14 | ArReceivableApplicationGlobalAttribute14 | — |
| GLOBAL_ATTRIBUTE15 | ArReceivableApplicationGlobalAttribute15 | — |
| GLOBAL_ATTRIBUTE16 | ArReceivableApplicationGlobalAttribute16 | — |
| GLOBAL_ATTRIBUTE17 | ArReceivableApplicationGlobalAttribute17 | — |
| GLOBAL_ATTRIBUTE18 | ArReceivableApplicationGlobalAttribute18 | — |
| GLOBAL_ATTRIBUTE19 | ArReceivableApplicationGlobalAttribute19 | — |
| GLOBAL_ATTRIBUTE2 | ArReceivableApplicationGlobalAttribute2 | — |
| GLOBAL_ATTRIBUTE20 | ArReceivableApplicationGlobalAttribute20 | — |
| GLOBAL_ATTRIBUTE3 | ArReceivableApplicationGlobalAttribute3 | — |
| GLOBAL_ATTRIBUTE4 | ArReceivableApplicationGlobalAttribute4 | — |
| GLOBAL_ATTRIBUTE5 | ArReceivableApplicationGlobalAttribute5 | — |
| GLOBAL_ATTRIBUTE6 | ArReceivableApplicationGlobalAttribute6 | — |
| GLOBAL_ATTRIBUTE7 | ArReceivableApplicationGlobalAttribute7 | — |
| GLOBAL_ATTRIBUTE8 | ArReceivableApplicationGlobalAttribute8 | — |
| GLOBAL_ATTRIBUTE9 | ArReceivableApplicationGlobalAttribute9 | — |
| GLOBAL_ATTRIBUTE_CATEGORY | ArReceivableApplicationGlobalAttributeCategory | — |
| GLOBAL_ATTRIBUTE_DATE1 | ArReceivableApplicationGlobalAttributeDate1 | — |
| GLOBAL_ATTRIBUTE_DATE2 | ArReceivableApplicationGlobalAttributeDate2 | — |
| GLOBAL_ATTRIBUTE_DATE3 | ArReceivableApplicationGlobalAttributeDate3 | — |
| GLOBAL_ATTRIBUTE_DATE4 | ArReceivableApplicationGlobalAttributeDate4 | — |
| GLOBAL_ATTRIBUTE_DATE5 | ArReceivableApplicationGlobalAttributeDate5 | — |
| GLOBAL_ATTRIBUTE_NUMBER1 | ArReceivableApplicationGlobalAttributeNumber1 | — |
| GLOBAL_ATTRIBUTE_NUMBER2 | ArReceivableApplicationGlobalAttributeNumber2 | — |
| GLOBAL_ATTRIBUTE_NUMBER3 | ArReceivableApplicationGlobalAttributeNumber3 | — |
| GLOBAL_ATTRIBUTE_NUMBER4 | ArReceivableApplicationGlobalAttributeNumber4 | — |
| GLOBAL_ATTRIBUTE_NUMBER5 | ArReceivableApplicationGlobalAttributeNumber5 | — |
| LAST_UPDATE_DATE | ArReceivableApplicationLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ArReceivableApplicationLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ArReceivableApplicationLastUpdatedBy | ✅ |
| LINE_APPLIED | ArReceivableApplicationLineApplied | ✅ |
| LINE_EDISCOUNTED | ArReceivableApplicationLineEdiscounted | ✅ |
| LINE_UEDISCOUNTED | ArReceivableApplicationLineUediscounted | ✅ |
| LINK_TO_CUSTOMER_TRX_ID | ArReceivableApplicationLinkToCustomerTrxId | ✅ |
| LINK_TO_TRX_HIST_ID | ArReceivableApplicationLinkToTrxHistId | ✅ |
| OBJECT_VERSION_NUMBER | ArReceivableApplicationObjectVersionNumber | ✅ |
| ORG_ID | ArReceivableApplicationOrgId | ✅ |
| PAYMENT_SCHEDULE_ID | ArReceivableApplicationPaymentScheduleId | ✅ |
| PAYMENT_SET_ID | ArReceivableApplicationPaymentSetId | ✅ |
| POSTABLE | ArReceivableApplicationPostable | ✅ |
| POSTING_CONTROL_ID | ArReceivableApplicationPostingControlId | ✅ |
| PROGRAM_APPLICATION_ID | ArReceivableApplicationProgramApplicationId | ✅ |
| PROGRAM_ID | ArReceivableApplicationProgramId | ✅ |
| PROGRAM_UPDATE_DATE | ArReceivableApplicationProgramUpdateDate | ✅ |
| RECEIVABLE_APPLICATION_ID | ArReceivableApplicationReceivableApplicationId | ✅ |
| RECEIVABLES_CHARGES_APPLIED | ArReceivableApplicationReceivablesChargesApplied | ✅ |
| RECEIVABLES_TRX_ID | ArReceivableApplicationReceivablesTrxId | ✅ |
| REQUEST_ID | ArReceivableApplicationRequestId | ✅ |
| REVERSAL_GL_DATE | ArReceivableApplicationReversalGlDate | ✅ |
| RULE_SET_ID | ArReceivableApplicationRuleSetId | ✅ |
| SECONDARY_APPLICATION_REF_ID | ArReceivableApplicationSecondaryApplicationRefId | ✅ |
| SECONDARY_APPLICATION_REF_NUM | ArReceivableApplicationSecondaryApplicationRefNum | ✅ |
| SECONDARY_APPLICATION_REF_TYPE | ArReceivableApplicationSecondaryApplicationRefType | ✅ |
| SET_OF_BOOKS_ID | ArReceivableApplicationSetOfBooksId | ✅ |
| STATUS | ArReceivableApplicationStatus | ✅ |
| TAX_APPLIED | ArReceivableApplicationTaxApplied | ✅ |
| TAX_CODE | ArReceivableApplicationTaxCode | ✅ |
| TAX_EDISCOUNTED | ArReceivableApplicationTaxEdiscounted | ✅ |
| TAX_UEDISCOUNTED | ArReceivableApplicationTaxUediscounted | ✅ |
| TRANS_TO_RECEIPT_RATE | ArReceivableApplicationTransToReceiptRate | ✅ |
| UNEARNED_DISCOUNT_CCID | ArReceivableApplicationUnearnedDiscountCcid | ✅ |
| UNEARNED_DISCOUNT_TAKEN | ArReceivableApplicationUnearnedDiscountTaken | ✅ |
| UNEDISC_TAX_ACCT_RULE | ArReceivableApplicationUnediscTaxAcctRule | ✅ |
| UPGRADE_METHOD | ArReceivableApplicationUpgradeMethod | ✅ |
| USSGL_TRANSACTION_CODE | ArReceivableApplicationUssglTransactionCode | ✅ |
| USSGL_TRANSACTION_CODE_CONTEXT | ArReceivableApplicationUssglTransactionCodeContext | ✅ |

---

## 📚 Referências

- [Oracle Docs — AR_RECEIVABLE_APPLICATIONS_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/arreceivableapplicationsall-10021.html)
- [[ar-module-data-dictionary]] — Dossiê do módulo AR
