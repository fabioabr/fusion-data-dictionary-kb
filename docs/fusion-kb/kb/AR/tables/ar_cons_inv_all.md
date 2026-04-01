---
id: DOC-AR-042
doc_type: system-doc
title: "AR_CONS_INV_ALL — Faturamento Consolidado (Balance Forward Billing)"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-receivable, data-dictionary, faturamento-consolidado, balance-forward, cons-inv]
aliases: [AR_CONS_INV_ALL, ar_cons_inv_all, cons_inv, faturamento_consolidado, consolidated_invoice]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_CONS_INV_ALL

> [!note] Sufixo _ALL
> Tabela particionada por `ORG_ID`. O sufixo `_ALL` indica que contém dados de todas as business units. Acessos via views sem sufixo filtram automaticamente pelo contexto de segurança da sessão.

## 📌 Visão Geral

Tabela de faturamento consolidado (consolidated invoices / balance forward billing) do Accounts Receivable. Cada registro representa um extrato consolidado para um cliente, agrupando múltiplas transações em um único documento de cobrança com saldo inicial, movimentações e saldo final.

## 🧠 Propósito de Negócio

O faturamento consolidado é utilizado quando a empresa emite um único documento de cobrança periódico ao cliente, em vez de cobrar cada fatura individualmente. Esse modelo é comum em relações de alto volume transacional (ex.: cartões corporativos, serviços recorrentes). O balance forward billing permite ao cliente receber um extrato com saldo anterior, novas cobranças, pagamentos recebidos e saldo final a pagar.

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Descrição | Categoria | Confiança |
|---|--------|------|-------|-----------|-----------|-----------|
| 1 | CONS_INV_ID | NUMBER(15) | NOT NULL | Chave primária. Identificador único do faturamento consolidado. | PK | 🟢 100% |
| 2 | CONS_BILLING_NUMBER | VARCHAR2(30) | NOT NULL | Número do documento consolidado de cobrança. | Negócio | 🟢 100% |
| 3 | CUSTOMER_ID | NUMBER(15) | NOT NULL | FK para HZ_CUST_ACCOUNTS. Cliente do faturamento. | FK | 🟢 100% |
| 4 | SITE_USE_ID | NUMBER(15) | NULL | FK para HZ_CUST_SITE_USES_ALL. Site de cobrança do cliente. | FK | 🟢 100% |
| 5 | CURRENCY_CODE | VARCHAR2(15) | NOT NULL | Código da moeda do documento consolidado. | Financeiro | 🟢 100% |
| 6 | BEGINNING_BALANCE | NUMBER | NULL | Saldo inicial do período (carregado do período anterior). | Financeiro | 🟢 100% |
| 7 | ENDING_BALANCE | NUMBER | NULL | Saldo final do período (a pagar pelo cliente). | Financeiro | 🟢 100% |
| 8 | CONS_INV_TYPE | VARCHAR2(30) | NOT NULL | Tipo do documento consolidado (ex.: BALANCE_FORWARD, OPEN_ITEM). | Classificação | 🟢 100% |
| 9 | STATUS | VARCHAR2(30) | NOT NULL | Status do documento (ex.: DRAFT, FINAL, PRINTED, ACCEPTED). | Controle | 🟢 100% |
| 10 | CUT_OFF_DATE | DATE | NOT NULL | Data de corte para inclusão de transações. | Temporal | 🟢 100% |
| 11 | ISSUE_DATE | DATE | NOT NULL | Data de emissão do documento consolidado. | Temporal | 🟢 100% |
| 12 | DUE_DATE | DATE | NULL | Data de vencimento do saldo consolidado. | Temporal | 🟢 100% |
| 13 | PRINT_STATUS | VARCHAR2(30) | NULL | Status de impressão (ex.: PENDING, PRINTED, REPRINTED). | Controle | 🟢 100% |
| 14 | TERM_ID | NUMBER(15) | NULL | FK para condições de pagamento. | FK | 🟢 100% |
| 15 | TOTAL_INVOICES_AMOUNT | NUMBER | NULL | Valor total das faturas incluídas no consolidado. | Financeiro | 🟢 100% |
| 16 | TOTAL_CREDITS_AMOUNT | NUMBER | NULL | Valor total dos créditos no período. | Financeiro | 🟢 100% |
| 17 | TOTAL_PAYMENTS_AMOUNT | NUMBER | NULL | Valor total dos pagamentos recebidos no período. | Financeiro | 🟢 100% |
| 18 | TOTAL_ADJUSTMENTS_AMOUNT | NUMBER | NULL | Valor total dos ajustes no período. | Financeiro | 🟡 75% |
| 19 | ORG_ID | NUMBER(15) | NOT NULL | Identificador da business unit (Operating Unit). | Partição | 🟢 100% |
| 20 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | Contexto de flexfield descritivo. | DFF | 🟢 100% |
| 21 | REQUEST_ID | NUMBER(15) | NULL | Identificador da requisição concorrente que gerou o registro. | Técnico | 🟢 100% |
| 22 | CREATED_BY | VARCHAR2(64) | NOT NULL | Usuário que criou o registro. | WHO | 🟢 100% |
| 23 | CREATION_DATE | DATE | NOT NULL | Data de criação do registro. | WHO | 🟢 100% |
| 24 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Usuário da última atualização. | WHO | 🟢 100% |
| 25 | LAST_UPDATE_DATE | DATE | NOT NULL | Data da última atualização. | WHO | 🟢 100% |

## 🔗 Relacionamentos

- **HZ_CUST_ACCOUNTS** — Cliente do faturamento consolidado (N:1 via `CUSTOMER_ID`).
- **HZ_CUST_SITE_USES_ALL** — Site de cobrança (N:1 via `SITE_USE_ID`).
- **AR_CONS_INV_TRX_ALL** — Transações incluídas no documento consolidado (1:N via `CONS_INV_ID`).
- **[[ar_statement_cycles]]** — Ciclo de extrato que pode disparar a geração do consolidado.

## 📎 Uso Típico

```sql
-- Faturamento consolidado pendente por cliente
SELECT ci.CONS_BILLING_NUMBER,
       ci.CUSTOMER_ID,
       ci.CURRENCY_CODE,
       ci.BEGINNING_BALANCE,
       ci.ENDING_BALANCE,
       ci.ISSUE_DATE,
       ci.DUE_DATE,
       ci.STATUS
  FROM AR_CONS_INV_ALL ci
 WHERE ci.ORG_ID = :p_org_id
   AND ci.STATUS NOT IN ('ACCEPTED', 'CANCELLED')
 ORDER BY ci.DUE_DATE;
```

## 🔒 Observações

- `ENDING_BALANCE` = `BEGINNING_BALANCE` + `TOTAL_INVOICES_AMOUNT` - `TOTAL_PAYMENTS_AMOUNT` - `TOTAL_CREDITS_AMOUNT` +/- `TOTAL_ADJUSTMENTS_AMOUNT`.
- O `CUT_OFF_DATE` determina quais transações são incluídas no consolidado; transações posteriores ficam para o próximo ciclo.
- Documentos com `STATUS = 'DRAFT'` podem ser regenerados; uma vez finalizado, o número é definitivo.
- Filtrar sempre por `ORG_ID` para garantir contexto correto de business unit.

## 🔗 PVOs Relacionados

### [[adjustmentdistributionpvo|AdjustmentDistributionPVO]] (AR · BICC: 3/50)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGING_BUCKET1_AMT | ConsolidationBillAgingBucket1Amt | — |
| AGING_BUCKET2_AMT | ConsolidationBillAgingBucket2Amt | — |
| AGING_BUCKET3_AMT | ConsolidationBillAgingBucket3Amt | — |
| AGING_BUCKET4_AMT | ConsolidationBillAgingBucket4Amt | — |
| AGING_BUCKET5_AMT | ConsolidationBillAgingBucket5Amt | — |
| AGING_BUCKET6_AMT | ConsolidationBillAgingBucket6Amt | — |
| AGING_BUCKET7_AMT | ConsolidationBillAgingBucket7Amt | — |
| BEGINNING_BALANCE | ConsolidationBillBeginningBalance | — |
| BILL_LEVEL_FLAG | ConsolidationBillBillLevelFlag | — |
| BILLING_CYCLE_ID | ConsolidationBillBillingCycleId | — |
| BILLING_DATE | ConsolidationBillBillingDate | — |
| CONCURRENT_REQUEST_ID | ConsolidationBillConcurrentRequestId | — |
| CONS_BILLING_NUMBER | ConsBillingNumber1 | — |
| CONS_BILLING_NUMBER | ConsolidationBillConsBillingNumber | ✅ |
| CONS_BILLING_NUMBER | RevConsBillConsBillingNumber | ✅ |
| CONS_INV_ID | ConsBillConsInvId1 | — |
| CONS_INV_ID | ConsolidationBillConsInvId | — |
| CONS_INV_ID | RevConsBillConsInvId | — |
| CONS_INV_TYPE | ConsolidationBillConsInvType | — |
| CREATED_BY | ConsolidationBillCreatedBy | — |
| CREATION_DATE | ConsolidationBillCreationDate | — |
| CURRENCY_CODE | ConsolidationBillCurrencyCode | — |
| CUSTOMER_ID | ConsolidationBillCustomerId | — |
| CUT_OFF_DATE | ConsolidationBillCutOffDate | — |
| DUE_DATE | ConsolidationBillDueDate | — |
| ENDING_BALANCE | ConsolidationBillEndingBalance | — |
| ISSUE_DATE | ConsolidationBillIssueDate | — |
| LAST_BILLING_DATE | ConsolidationBillLastBillingDate | — |
| LAST_CHARGE_DATE | ConsolidationBillLastChargeDate | — |
| LAST_UPDATE_DATE | ConsolidationBillLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ConsolidationBillLastUpdateLogin | — |
| LAST_UPDATED_BY | ConsolidationBillLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ConsBillObjectVersionNumber8 | — |
| OBJECT_VERSION_NUMBER | ConsolidationBillObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | RevConsBillObjectVersionNumber7 | — |
| ORG_ID | ConsolidationBillOrgId | — |
| PRINT_STATUS | ConsolidationBillPrintStatus | — |
| REMIT_TO_ADDRESS_ID | ConsolidationBillRemitToAddressId | — |
| REMIT_TO_ADDRESS_SEQ_ID | ConsolidationBillRemitToAddressSeqId | — |
| SITE_USE_ID | ConsolidationBillSiteUseId | — |
| START_DATE | ConsolidationBillStartDate | — |
| STATUS | ConsolidationBillStatus | — |
| TERM_ID | ConsolidationBillTermId | — |
| TOTAL_ADJUSTMENTS_AMT | ConsolidationBillTotalAdjustmentsAmt | — |
| TOTAL_CREDITS_AMT | ConsolidationBillTotalCreditsAmt | — |
| TOTAL_FINANCE_CHARGES_AMT | ConsolidationBillTotalFinanceChargesAmt | — |
| TOTAL_RECEIPTS_AMT | ConsolidationBillTotalReceiptsAmt | — |
| TOTAL_TAX_AMT | ConsolidationBillTotalTaxAmt | — |
| TOTAL_TRX_AMT | ConsolidationBillTotalTrxAmt | — |
| UNPAID_REASON | ConsolidationBillUnpaidReason | — |

### [[adjustmentpvo|AdjustmentPVO]] (AR · BICC: 3/49)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGING_BUCKET1_AMT | ConsBillAgingBucket1Amt | — |
| AGING_BUCKET2_AMT | ConsBillAgingBucket2Amt | — |
| AGING_BUCKET3_AMT | ConsBillAgingBucket3Amt | — |
| AGING_BUCKET4_AMT | ConsBillAgingBucket4Amt | — |
| AGING_BUCKET5_AMT | ConsBillAgingBucket5Amt | — |
| AGING_BUCKET6_AMT | ConsBillAgingBucket6Amt | — |
| AGING_BUCKET7_AMT | ConsBillAgingBucket7Amt | — |
| BEGINNING_BALANCE | ConsBillBeginningBalance | — |
| BILL_LEVEL_FLAG | ConsBillBillLevelFlag | — |
| BILLING_CYCLE_ID | ConsBillBillingCycleId | — |
| BILLING_DATE | ConsBillBillingDate | — |
| CONCURRENT_REQUEST_ID | ConsBillConcurrentRequestId | — |
| CONS_BILLING_NUMBER | ConsBillConsBillingNumber | ✅ |
| CONS_BILLING_NUMBER | RevConsBillConsBillingNumber1 | ✅ |
| CONS_INV_ID | ConsBillConsInvId | — |
| CONS_INV_ID | ConsolidatedBillConsInvId | — |
| CONS_INV_ID | RevConsBillConsInvId1 | — |
| CONS_INV_TYPE | ConsBillConsInvType | — |
| CREATED_BY | ConsBillCreatedBy | — |
| CREATION_DATE | ConsBillCreationDate | — |
| CURRENCY_CODE | ConsBillCurrencyCode | — |
| CUSTOMER_ID | ConsBillCustomerId | — |
| CUT_OFF_DATE | ConsBillCutOffDate | — |
| DUE_DATE | ConsBillDueDate | — |
| ENDING_BALANCE | ConsBillEndingBalance | — |
| ISSUE_DATE | ConsBillIssueDate | — |
| LAST_BILLING_DATE | ConsBillLastBillingDate | — |
| LAST_CHARGE_DATE | ConsBillLastChargeDate | — |
| LAST_UPDATE_DATE | ConsBillLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ConsBillLastUpdateLogin | — |
| LAST_UPDATED_BY | ConsBillLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ConsBillObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ConsolidatedBillObjectVersionNumber3 | — |
| OBJECT_VERSION_NUMBER | RevConsBillObjectVersionNumber4 | — |
| ORG_ID | ConsBillOrgId | — |
| PRINT_STATUS | ConsBillPrintStatus | — |
| REMIT_TO_ADDRESS_ID | ConsBillRemitToAddressId | — |
| REMIT_TO_ADDRESS_SEQ_ID | ConsBillRemitToAddressSeqId | — |
| SITE_USE_ID | ConsBillSiteUseId | — |
| START_DATE | ConsBillStartDate | — |
| STATUS | ConsBillStatus | — |
| TERM_ID | ConsBillTermId | — |
| TOTAL_ADJUSTMENTS_AMT | ConsBillTotalAdjustmentsAmt | — |
| TOTAL_CREDITS_AMT | ConsBillTotalCreditsAmt | — |
| TOTAL_FINANCE_CHARGES_AMT | ConsBillTotalFinanceChargesAmt | — |
| TOTAL_RECEIPTS_AMT | ConsBillTotalReceiptsAmt | — |
| TOTAL_TAX_AMT | ConsBillTotalTaxAmt | — |
| TOTAL_TRX_AMT | ConsBillTotalTrxAmt | — |
| UNPAID_REASON | ConsBillUnpaidReason | — |

### [[completedtrxrevadjdistributionpvo|CompletedTrxRevAdjDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGING_BUCKET1_AMT | ConsolidationBillAgingBucket1Amt | — |
| AGING_BUCKET2_AMT | ConsolidationBillAgingBucket2Amt | — |
| AGING_BUCKET3_AMT | ConsolidationBillAgingBucket3Amt | — |
| AGING_BUCKET4_AMT | ConsolidationBillAgingBucket4Amt | — |
| AGING_BUCKET5_AMT | ConsolidationBillAgingBucket5Amt | — |
| AGING_BUCKET6_AMT | ConsolidationBillAgingBucket6Amt | — |
| AGING_BUCKET7_AMT | ConsolidationBillAgingBucket7Amt | — |
| BEGINNING_BALANCE | ConsolidationBillBeginningBalance | — |
| BILL_LEVEL_FLAG | ConsolidationBillBillLevelFlag | — |
| BILLING_CYCLE_ID | ConsolidationBillBillingCycleId | — |
| BILLING_DATE | ConsolidationBillBillingDate | — |
| CONCURRENT_REQUEST_ID | ConsolidationBillConcurrentRequestId | — |
| CONS_BILLING_NUMBER | ConsolidationBillConsBillingNumber | — |
| CONS_INV_ID | ConsolidationBillConsInvId | — |
| CONS_INV_TYPE | ConsolidationBillConsInvType | — |
| CURRENCY_CODE | ConsolidationBillCurrencyCode | — |
| CUSTOMER_ID | ConsolidationBillCustomerId | — |
| CUT_OFF_DATE | ConsolidationBillCutOffDate | — |
| DUE_DATE | ConsolidationBillDueDate | — |
| ENDING_BALANCE | ConsolidationBillEndingBalance | — |
| ISSUE_DATE | ConsolidationBillIssueDate | — |
| LAST_BILLING_DATE | ConsolidationBillLastBillingDate | — |
| LAST_CHARGE_DATE | ConsolidationBillLastChargeDate | — |
| ORG_ID | ConsolidationBillOrgId | — |
| PRINT_STATUS | ConsolidationBillPrintStatus | — |
| REMIT_TO_ADDRESS_ID | ConsolidationBillRemitToAddressId | — |
| REMIT_TO_ADDRESS_SEQ_ID | ConsolidationBillRemitToAddressSeqId | — |
| SITE_USE_ID | ConsolidationBillSiteUseId | — |
| START_DATE | ConsolidationBillStartDate | — |
| STATUS | ConsolidationBillStatus | — |
| TERM_ID | ConsolidationBillTermId | — |
| TOTAL_ADJUSTMENTS_AMT | ConsolidationBillTotalAdjustmentsAmt | — |
| TOTAL_CREDITS_AMT | ConsolidationBillTotalCreditsAmt | — |
| TOTAL_FINANCE_CHARGES_AMT | ConsolidationBillTotalFinanceChargesAmt | — |
| TOTAL_RECEIPTS_AMT | ConsolidationBillTotalReceiptsAmt | — |
| TOTAL_TAX_AMT | ConsolidationBillTotalTaxAmt | — |
| TOTAL_TRX_AMT | ConsolidationBillTotalTrxAmt | — |
| UNPAID_REASON | ConsolidationBillUnpaidReason | — |

### [[consolidatedbillextractpvo|ConsolidatedBillExtractPVO]] (OTHER · BICC: 45/61)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGING_BUCKET1_AMT | ArConsInvAgingBucket1Amt | ✅ |
| AGING_BUCKET2_AMT | ArConsInvAgingBucket2Amt | ✅ |
| AGING_BUCKET3_AMT | ArConsInvAgingBucket3Amt | ✅ |
| AGING_BUCKET4_AMT | ArConsInvAgingBucket4Amt | ✅ |
| AGING_BUCKET5_AMT | ArConsInvAgingBucket5Amt | ✅ |
| AGING_BUCKET6_AMT | ArConsInvAgingBucket6Amt | ✅ |
| AGING_BUCKET7_AMT | ArConsInvAgingBucket7Amt | ✅ |
| ATTRIBUTE1 | ArConsInvAttribute1 | — |
| ATTRIBUTE10 | ArConsInvAttribute10 | — |
| ATTRIBUTE11 | ArConsInvAttribute11 | — |
| ATTRIBUTE12 | ArConsInvAttribute12 | — |
| ATTRIBUTE13 | ArConsInvAttribute13 | — |
| ATTRIBUTE14 | ArConsInvAttribute14 | — |
| ATTRIBUTE15 | ArConsInvAttribute15 | — |
| ATTRIBUTE2 | ArConsInvAttribute2 | — |
| ATTRIBUTE3 | ArConsInvAttribute3 | — |
| ATTRIBUTE4 | ArConsInvAttribute4 | — |
| ATTRIBUTE5 | ArConsInvAttribute5 | — |
| ATTRIBUTE6 | ArConsInvAttribute6 | — |
| ATTRIBUTE7 | ArConsInvAttribute7 | — |
| ATTRIBUTE8 | ArConsInvAttribute8 | — |
| ATTRIBUTE9 | ArConsInvAttribute9 | — |
| ATTRIBUTE_CATEGORY | ArConsInvAttributeCategory | — |
| BEGINNING_BALANCE | ArConsInvBeginningBalance | ✅ |
| BFB_TEMPLATE_NAME | ArConsInvBfbTemplateName | ✅ |
| BILL_LEVEL_FLAG | ArConsInvBillLevelFlag | ✅ |
| BILLING_CYCLE_ID | ArConsInvBillingCycleId | ✅ |
| BILLING_DATE | ArConsInvBillingDate | ✅ |
| CONCURRENT_REQUEST_ID | ArConsInvConcurrentRequestId | ✅ |
| CONS_BILLING_NUMBER | ArConsInvConsBillingNumber | ✅ |
| CONS_INV_ID | ArConsInvConsInvId | ✅ |
| CONS_INV_TYPE | ArConsInvConsInvType | ✅ |
| CREATED_BY | ArConsInvCreatedBy | ✅ |
| CREATION_DATE | ArConsInvCreationDate | ✅ |
| CURRENCY_CODE | ArConsInvCurrencyCode | ✅ |
| CUSTOMER_ID | ArConsInvCustomerId | ✅ |
| CUT_OFF_DATE | ArConsInvCutOffDate | ✅ |
| DUE_DATE | ArConsInvDueDate | ✅ |
| ENDING_BALANCE | ArConsInvEndingBalance | ✅ |
| ISSUE_DATE | ArConsInvIssueDate | ✅ |
| LAST_BILLING_DATE | ArConsInvLastBillingDate | ✅ |
| LAST_CHARGE_DATE | ArConsInvLastChargeDate | ✅ |
| LAST_UPDATE_DATE | ArConsInvLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ArConsInvLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ArConsInvLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ArConsInvObjectVersionNumber | ✅ |
| ORG_ID | ArConsInvOrgId | ✅ |
| PRINT_STATUS | ArConsInvPrintStatus | ✅ |
| REMIT_TO_ADDRESS_ID | ArConsInvRemitToAddressId | ✅ |
| REMIT_TO_ADDRESS_SEQ_ID | ArConsInvRemitToAddressSeqId | ✅ |
| SITE_USE_ID | ArConsInvSiteUseId | ✅ |
| START_DATE | ArConsInvStartDate | ✅ |
| STATUS | ArConsInvStatus | ✅ |
| TERM_ID | ArConsInvTermId | ✅ |
| TOTAL_ADJUSTMENTS_AMT | ArConsInvTotalAdjustmentsAmt | ✅ |
| TOTAL_CREDITS_AMT | ArConsInvTotalCreditsAmt | ✅ |
| TOTAL_FINANCE_CHARGES_AMT | TotalFinanceChargesAmt | ✅ |
| TOTAL_RECEIPTS_AMT | ArConsInvTotalReceiptsAmt | ✅ |
| TOTAL_TAX_AMT | ArConsInvTotalTaxAmt | ✅ |
| TOTAL_TRX_AMT | ArConsInvTotalTrxAmt | ✅ |
| UNPAID_REASON | ArConsInvUnpaidReason | ✅ |

### [[creditmemoapplicationdistributionpvo|CreditMemoApplicationDistributionPVO]] (AR · BICC: 3/88)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGING_BUCKET1_AMT | ConsolidatedBillTo1AgingBucket1Amt | — |
| AGING_BUCKET1_AMT | ConsolidatedBillToAgingBucket1Amt | — |
| AGING_BUCKET2_AMT | ConsolidatedBillTo1AgingBucket2Amt | — |
| AGING_BUCKET2_AMT | ConsolidatedBillToAgingBucket2Amt | — |
| AGING_BUCKET3_AMT | ConsolidatedBillTo1AgingBucket3Amt | — |
| AGING_BUCKET3_AMT | ConsolidatedBillToAgingBucket3Amt | — |
| AGING_BUCKET4_AMT | ConsolidatedBillTo1AgingBucket4Amt | — |
| AGING_BUCKET4_AMT | ConsolidatedBillToAgingBucket4Amt | — |
| AGING_BUCKET5_AMT | ConsolidatedBillTo1AgingBucket5Amt | — |
| AGING_BUCKET5_AMT | ConsolidatedBillToAgingBucket5Amt | — |
| AGING_BUCKET6_AMT | ConsolidatedBillTo1AgingBucket6Amt | — |
| AGING_BUCKET6_AMT | ConsolidatedBillToAgingBucket6Amt | — |
| AGING_BUCKET7_AMT | ConsolidatedBillTo1AgingBucket7Amt | — |
| AGING_BUCKET7_AMT | ConsolidatedBillToAgingBucket7Amt | — |
| BEGINNING_BALANCE | ConsolidatedBillTo1BeginningBalance | — |
| BEGINNING_BALANCE | ConsolidatedBillToBeginningBalance | — |
| BILL_LEVEL_FLAG | ConsolidatedBillTo1BillLevelFlag | — |
| BILL_LEVEL_FLAG | ConsolidatedBillToBillLevelFlag | — |
| BILLING_CYCLE_ID | ConsolidatedBillTo1BillingCycleId | — |
| BILLING_CYCLE_ID | ConsolidatedBillToBillingCycleId | — |
| BILLING_DATE | ConsolidatedBillTo1BillingDate | — |
| BILLING_DATE | ConsolidatedBillToBillingDate | — |
| CONCURRENT_REQUEST_ID | ConsolidatedBillTo1ConcurrentRequestId | — |
| CONCURRENT_REQUEST_ID | ConsolidatedBillToConcurrentRequestId | — |
| CONS_BILLING_NUMBER | ConsolidatedBillTo1ConsBillingNumber | ✅ |
| CONS_BILLING_NUMBER | ConsolidatedBillToConsBillingNumber | — |
| CONS_INV_ID | ConsolidatedBillTo1ConsInvId | — |
| CONS_INV_ID | ConsolidatedBillToConsInvId | — |
| CONS_INV_TYPE | ConsolidatedBillTo1ConsInvType | — |
| CONS_INV_TYPE | ConsolidatedBillToConsInvType | — |
| CREATED_BY | ConsolidatedBillTo1CreatedBy | — |
| CREATED_BY | ConsolidatedBillToCreatedBy | — |
| CREATION_DATE | ConsolidatedBillTo1CreationDate | — |
| CREATION_DATE | ConsolidatedBillToCreationDate | — |
| CURRENCY_CODE | ConsolidatedBillTo1CurrencyCode | — |
| CURRENCY_CODE | ConsolidatedBillToCurrencyCode | — |
| CUSTOMER_ID | ConsolidatedBillTo1CustomerId | — |
| CUSTOMER_ID | ConsolidatedBillToCustomerId | — |
| CUT_OFF_DATE | ConsolidatedBillTo1CutOffDate | — |
| CUT_OFF_DATE | ConsolidatedBillToCutOffDate | — |
| DUE_DATE | ConsolidatedBillTo1DueDate | — |
| DUE_DATE | ConsolidatedBillToDueDate | — |
| ENDING_BALANCE | ConsolidatedBillTo1EndingBalance | — |
| ENDING_BALANCE | ConsolidatedBillToEndingBalance | — |
| ISSUE_DATE | ConsolidatedBillTo1IssueDate | — |
| ISSUE_DATE | ConsolidatedBillToIssueDate | — |
| LAST_BILLING_DATE | ConsolidatedBillTo1LastBillingDate | — |
| LAST_BILLING_DATE | ConsolidatedBillToLastBillingDate | — |
| LAST_CHARGE_DATE | ConsolidatedBillTo1LastChargeDate | — |
| LAST_CHARGE_DATE | ConsolidatedBillToLastChargeDate | — |
| LAST_UPDATE_DATE | ConsolidatedBillTo1LastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ConsolidatedBillToLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ConsolidatedBillTo1LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ConsolidatedBillToLastUpdateLogin | — |
| LAST_UPDATED_BY | ConsolidatedBillTo1LastUpdatedBy | — |
| LAST_UPDATED_BY | ConsolidatedBillToLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ConsolidatedBillTo1ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ConsolidatedBillToObjectVersionNumber | — |
| ORG_ID | ConsolidatedBillTo1OrgId | — |
| ORG_ID | ConsolidatedBillToOrgId | — |
| PRINT_STATUS | ConsolidatedBillTo1PrintStatus | — |
| PRINT_STATUS | ConsolidatedBillToPrintStatus | — |
| REMIT_TO_ADDRESS_ID | ConsolidatedBillTo1RemitToAddressId | — |
| REMIT_TO_ADDRESS_ID | ConsolidatedBillToRemitToAddressId | — |
| REMIT_TO_ADDRESS_SEQ_ID | ConsolidatedBillTo1RemitToAddressSeqId | — |
| REMIT_TO_ADDRESS_SEQ_ID | ConsolidatedBillToRemitToAddressSeqId | — |
| SITE_USE_ID | ConsolidatedBillTo1SiteUseId | — |
| SITE_USE_ID | ConsolidatedBillToSiteUseId | — |
| START_DATE | ConsolidatedBillTo1StartDate | — |
| START_DATE | ConsolidatedBillToStartDate | — |
| STATUS | ConsolidatedBillTo1Status | — |
| STATUS | ConsolidatedBillToStatus | — |
| TERM_ID | ConsolidatedBillTo1TermId | — |
| TERM_ID | ConsolidatedBillToTermId | — |
| TOTAL_ADJUSTMENTS_AMT | ConsolidatedBillTo1TotalAdjustmentsAmt | — |
| TOTAL_ADJUSTMENTS_AMT | ConsolidatedBillToTotalAdjustmentsAmt | — |
| TOTAL_CREDITS_AMT | ConsolidatedBillTo1TotalCreditsAmt | — |
| TOTAL_CREDITS_AMT | ConsolidatedBillToTotalCreditsAmt | — |
| TOTAL_FINANCE_CHARGES_AMT | ConsolidatedBillTo1TotalFinanceChargesAmt | — |
| TOTAL_FINANCE_CHARGES_AMT | ConsolidatedBillToTotalFinanceChargesAmt | — |
| TOTAL_RECEIPTS_AMT | ConsolidatedBillTo1TotalReceiptsAmt | — |
| TOTAL_RECEIPTS_AMT | ConsolidatedBillToTotalReceiptsAmt | — |
| TOTAL_TAX_AMT | ConsolidatedBillTo1TotalTaxAmt | — |
| TOTAL_TAX_AMT | ConsolidatedBillToTotalTaxAmt | — |
| TOTAL_TRX_AMT | ConsolidatedBillTo1TotalTrxAmt | — |
| TOTAL_TRX_AMT | ConsolidatedBillToTotalTrxAmt | — |
| UNPAID_REASON | ConsolidatedBillTo1UnpaidReason | — |
| UNPAID_REASON | ConsolidatedBillToUnpaidReason | — |

### [[creditmemoapplicationpvo|CreditMemoApplicationPVO]] (AR · BICC: 1/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONCURRENT_REQUEST_ID | ConsBillConcurrentRequestId | — |
| CONS_BILLING_NUMBER | ConsBillConsBillingNumber | ✅ |
| CONS_INV_ID | ConsBillConsInvId | — |
| CONS_INV_TYPE | ConsBillConsInvType | — |
| CUSTOMER_ID | ConsBillCustomerId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| SITE_USE_ID | ConsBillSiteUseId | — |
| STATUS | ConsBillStatus | — |

### [[paymentschedulepvo|PaymentSchedulePVO]] (AR · BICC: 4/88)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGING_BUCKET1_AMT | ConsolidationBillAgingBucket1Amt | — |
| AGING_BUCKET1_AMT | ConsolidationBillReverseAgingBucket1Amt | — |
| AGING_BUCKET2_AMT | ConsolidationBillAgingBucket2Amt | — |
| AGING_BUCKET2_AMT | ConsolidationBillReverseAgingBucket2Amt | — |
| AGING_BUCKET3_AMT | ConsolidationBillAgingBucket3Amt | — |
| AGING_BUCKET3_AMT | ConsolidationBillReverseAgingBucket3Amt | — |
| AGING_BUCKET4_AMT | ConsolidationBillAgingBucket4Amt | — |
| AGING_BUCKET4_AMT | ConsolidationBillReverseAgingBucket4Amt | — |
| AGING_BUCKET5_AMT | ConsolidationBillAgingBucket5Amt | — |
| AGING_BUCKET5_AMT | ConsolidationBillReverseAgingBucket5Amt | — |
| AGING_BUCKET6_AMT | ConsolidationBillAgingBucket6Amt | — |
| AGING_BUCKET6_AMT | ConsolidationBillReverseAgingBucket6Amt | — |
| AGING_BUCKET7_AMT | ConsolidationBillAgingBucket7Amt | — |
| AGING_BUCKET7_AMT | ConsolidationBillReverseAgingBucket7Amt | — |
| BEGINNING_BALANCE | ConsolidationBillBeginningBalance | — |
| BEGINNING_BALANCE | ConsolidationBillReverseBeginningBalance | — |
| BILL_LEVEL_FLAG | ConsolidationBillBillLevelFlag | — |
| BILL_LEVEL_FLAG | ConsolidationBillReverseBillLevelFlag | — |
| BILLING_CYCLE_ID | ConsolidationBillBillingCycleId | — |
| BILLING_CYCLE_ID | ConsolidationBillReverseBillingCycleId | — |
| BILLING_DATE | ConsolidationBillBillingDate | — |
| BILLING_DATE | ConsolidationBillReverseBillingDate | — |
| CONCURRENT_REQUEST_ID | ConsolidationBillConcurrentRequestId | — |
| CONCURRENT_REQUEST_ID | ConsolidationBillReverseConcurrentRequestId | — |
| CONS_BILLING_NUMBER | ConsolidationBillConsBillingNumber | ✅ |
| CONS_BILLING_NUMBER | ConsolidationBillReverseConsBillingNumber | ✅ |
| CONS_INV_ID | ConsolidationBillConsInvId | — |
| CONS_INV_ID | ConsolidationBillReverseConsInvId | — |
| CONS_INV_TYPE | ConsolidationBillConsInvType | — |
| CONS_INV_TYPE | ConsolidationBillReverseConsInvType | — |
| CREATED_BY | ConsolidationBillCreatedBy | — |
| CREATED_BY | ConsolidationBillReverseCreatedBy | — |
| CREATION_DATE | ConsolidationBillCreationDate | — |
| CREATION_DATE | ConsolidationBillReverseCreationDate | — |
| CURRENCY_CODE | ConsolidationBillCurrencyCode | — |
| CURRENCY_CODE | ConsolidationBillReverseCurrencyCode | — |
| CUSTOMER_ID | ConsolidationBillCustomerId | — |
| CUSTOMER_ID | ConsolidationBillReverseCustomerId | — |
| CUT_OFF_DATE | ConsolidationBillCutOffDate | — |
| CUT_OFF_DATE | ConsolidationBillReverseCutOffDate | — |
| DUE_DATE | ConsolidationBillDueDate | — |
| DUE_DATE | ConsolidationBillReverseDueDate | — |
| ENDING_BALANCE | ConsolidationBillEndingBalance | — |
| ENDING_BALANCE | ConsolidationBillReverseEndingBalance | — |
| ISSUE_DATE | ConsolidationBillIssueDate | — |
| ISSUE_DATE | ConsolidationBillReverseIssueDate | — |
| LAST_BILLING_DATE | ConsolidationBillLastBillingDate | — |
| LAST_BILLING_DATE | ConsolidationBillReverseLastBillingDate | — |
| LAST_CHARGE_DATE | ConsolidationBillLastChargeDate | — |
| LAST_CHARGE_DATE | ConsolidationBillReverseLastChargeDate | — |
| LAST_UPDATE_DATE | ConsolidationBillLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ConsolidationBillReverseLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ConsolidationBillLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ConsolidationBillReverseLastUpdateLogin | — |
| LAST_UPDATED_BY | ConsolidationBillLastUpdatedBy | — |
| LAST_UPDATED_BY | ConsolidationBillReverseLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ConsolidationBillObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ConsolidationBillReverseObjectVersionNumber | — |
| ORG_ID | ConsolidationBillOrgId | — |
| ORG_ID | ConsolidationBillReverseOrgId | — |
| PRINT_STATUS | ConsolidationBillPrintStatus | — |
| PRINT_STATUS | ConsolidationBillReversePrintStatus | — |
| REMIT_TO_ADDRESS_ID | ConsolidationBillRemitToAddressId | — |
| REMIT_TO_ADDRESS_ID | ConsolidationBillReverseRemitToAddressId | — |
| REMIT_TO_ADDRESS_SEQ_ID | ConsolidationBillRemitToAddressSeqId | — |
| REMIT_TO_ADDRESS_SEQ_ID | ConsolidationBillReverseRemitToAddressSeqId | — |
| SITE_USE_ID | ConsolidationBillReverseSiteUseId | — |
| SITE_USE_ID | ConsolidationBillSiteUseId | — |
| START_DATE | ConsolidationBillReverseStartDate | — |
| START_DATE | ConsolidationBillStartDate | — |
| STATUS | ConsolidationBillReverseStatus | — |
| STATUS | ConsolidationBillStatus | — |
| TERM_ID | ConsolidationBillReverseTermId | — |
| TERM_ID | ConsolidationBillTermId | — |
| TOTAL_ADJUSTMENTS_AMT | ConsolidationBillReverseTotalAdjustmentsAmt | — |
| TOTAL_ADJUSTMENTS_AMT | ConsolidationBillTotalAdjustmentsAmt | — |
| TOTAL_CREDITS_AMT | ConsolidationBillReverseTotalCreditsAmt | — |
| TOTAL_CREDITS_AMT | ConsolidationBillTotalCreditsAmt | — |
| TOTAL_FINANCE_CHARGES_AMT | ConsolidationBillReverseTotalFinanceChargesAmt | — |
| TOTAL_FINANCE_CHARGES_AMT | ConsolidationBillTotalFinanceChargesAmt | — |
| TOTAL_RECEIPTS_AMT | ConsolidationBillReverseTotalReceiptsAmt | — |
| TOTAL_RECEIPTS_AMT | ConsolidationBillTotalReceiptsAmt | — |
| TOTAL_TAX_AMT | ConsolidationBillReverseTotalTaxAmt | — |
| TOTAL_TAX_AMT | ConsolidationBillTotalTaxAmt | — |
| TOTAL_TRX_AMT | ConsolidationBillReverseTotalTrxAmt | — |
| TOTAL_TRX_AMT | ConsolidationBillTotalTrxAmt | — |
| UNPAID_REASON | ConsolidationBillReverseUnpaidReason | — |
| UNPAID_REASON | ConsolidationBillUnpaidReason | — |

### [[receiptapplicationdistributionpvo|ReceiptApplicationDistributionPVO]] (AR · BICC: 3/132)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGING_BUCKET1_AMT | ConsBillInvAgingBucket1Amt | — |
| AGING_BUCKET1_AMT | ConsolidationBillAgingBucket1Amt | — |
| AGING_BUCKET1_AMT | ConsolidationBillReverseAgingBucket1Amt | — |
| AGING_BUCKET2_AMT | ConsBillInvAgingBucket2Amt | — |
| AGING_BUCKET2_AMT | ConsolidationBillAgingBucket2Amt | — |
| AGING_BUCKET2_AMT | ConsolidationBillReverseAgingBucket2Amt | — |
| AGING_BUCKET3_AMT | ConsBillInvAgingBucket3Amt | — |
| AGING_BUCKET3_AMT | ConsolidationBillAgingBucket3Amt | — |
| AGING_BUCKET3_AMT | ConsolidationBillReverseAgingBucket3Amt | — |
| AGING_BUCKET4_AMT | ConsBillInvAgingBucket4Amt | — |
| AGING_BUCKET4_AMT | ConsolidationBillAgingBucket4Amt | — |
| AGING_BUCKET4_AMT | ConsolidationBillReverseAgingBucket4Amt | — |
| AGING_BUCKET5_AMT | ConsBillInvAgingBucket5Amt | — |
| AGING_BUCKET5_AMT | ConsolidationBillAgingBucket5Amt | — |
| AGING_BUCKET5_AMT | ConsolidationBillReverseAgingBucket5Amt | — |
| AGING_BUCKET6_AMT | ConsBillInvAgingBucket6Amt | — |
| AGING_BUCKET6_AMT | ConsolidationBillAgingBucket6Amt | — |
| AGING_BUCKET6_AMT | ConsolidationBillReverseAgingBucket6Amt | — |
| AGING_BUCKET7_AMT | ConsBillInvAgingBucket7Amt | — |
| AGING_BUCKET7_AMT | ConsolidationBillAgingBucket7Amt | — |
| AGING_BUCKET7_AMT | ConsolidationBillReverseAgingBucket7Amt | — |
| BEGINNING_BALANCE | ConsBillInvBeginningBalance | — |
| BEGINNING_BALANCE | ConsolidationBillBeginningBalance | — |
| BEGINNING_BALANCE | ConsolidationBillReverseBeginningBalance | — |
| BILL_LEVEL_FLAG | ConsBillInvBillLevelFlag | — |
| BILL_LEVEL_FLAG | ConsolidationBillBillLevelFlag | — |
| BILL_LEVEL_FLAG | ConsolidationBillReverseBillLevelFlag | — |
| BILLING_CYCLE_ID | ConsBillInvBillingCycleId | — |
| BILLING_CYCLE_ID | ConsolidationBillBillingCycleId | — |
| BILLING_CYCLE_ID | ConsolidationBillReverseBillingCycleId | — |
| BILLING_DATE | ConsBillInvBillingDate | — |
| BILLING_DATE | ConsolidationBillBillingDate | — |
| BILLING_DATE | ConsolidationBillReverseBillingDate | — |
| CONCURRENT_REQUEST_ID | ConsBillInvConcurrentRequestId | — |
| CONCURRENT_REQUEST_ID | ConsolidationBillConcurrentRequestId | — |
| CONCURRENT_REQUEST_ID | ConsolidationBillReverseConcurrentRequestId | — |
| CONS_BILLING_NUMBER | ConsBillInvConsBillingNumber | — |
| CONS_BILLING_NUMBER | ConsolidationBillConsBillingNumber | — |
| CONS_BILLING_NUMBER | ConsolidationBillReverseConsBillingNumber | — |
| CONS_INV_ID | ConsBillInvConsInvId | — |
| CONS_INV_ID | ConsolidationBillConsInvId | — |
| CONS_INV_ID | ConsolidationBillReverseConsInvId | — |
| CONS_INV_TYPE | ConsBillInvConsInvType | — |
| CONS_INV_TYPE | ConsolidationBillConsInvType | — |
| CONS_INV_TYPE | ConsolidationBillReverseConsInvType | — |
| CREATED_BY | ConsBillInvCreatedBy | — |
| CREATED_BY | ConsolidationBillCreatedBy | — |
| CREATED_BY | ConsolidationBillReverseCreatedBy | — |
| CREATION_DATE | ConsBillInvCreationDate | — |
| CREATION_DATE | ConsolidationBillCreationDate | — |
| CREATION_DATE | ConsolidationBillReverseCreationDate | — |
| CURRENCY_CODE | ConsBillInvCurrencyCode | — |
| CURRENCY_CODE | ConsolidationBillCurrencyCode | — |
| CURRENCY_CODE | ConsolidationBillReverseCurrencyCode | — |
| CUSTOMER_ID | ConsBillInvCustomerId | — |
| CUSTOMER_ID | ConsolidationBillCustomerId | — |
| CUSTOMER_ID | ConsolidationBillReverseCustomerId | — |
| CUT_OFF_DATE | ConsBillInvCutOffDate | — |
| CUT_OFF_DATE | ConsolidationBillCutOffDate | — |
| CUT_OFF_DATE | ConsolidationBillReverseCutOffDate | — |
| DUE_DATE | ConsBillInvDueDate | — |
| DUE_DATE | ConsolidationBillDueDate | — |
| DUE_DATE | ConsolidationBillReverseDueDate | — |
| ENDING_BALANCE | ConsBillInvEndingBalance | — |
| ENDING_BALANCE | ConsolidationBillEndingBalance | — |
| ENDING_BALANCE | ConsolidationBillReverseEndingBalance | — |
| ISSUE_DATE | ConsBillInvIssueDate | — |
| ISSUE_DATE | ConsolidationBillIssueDate | — |
| ISSUE_DATE | ConsolidationBillReverseIssueDate | — |
| LAST_BILLING_DATE | ConsBillInvLastBillingDate | — |
| LAST_BILLING_DATE | ConsolidationBillLastBillingDate | — |
| LAST_BILLING_DATE | ConsolidationBillReverseLastBillingDate | — |
| LAST_CHARGE_DATE | ConsBillInvLastChargeDate | — |
| LAST_CHARGE_DATE | ConsolidationBillLastChargeDate | — |
| LAST_CHARGE_DATE | ConsolidationBillReverseLastChargeDate | — |
| LAST_UPDATE_DATE | ConsBillInvLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ConsolidationBillLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ConsolidationBillReverseLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ConsBillInvLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ConsolidationBillLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ConsolidationBillReverseLastUpdateLogin | — |
| LAST_UPDATED_BY | ConsBillInvLastUpdatedBy | — |
| LAST_UPDATED_BY | ConsolidationBillLastUpdatedBy | — |
| LAST_UPDATED_BY | ConsolidationBillReverseLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ConsBillInvObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ConsolidationBillObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ConsolidationBillReverseObjectVersionNumber | — |
| ORG_ID | ConsBillInvOrgId | — |
| ORG_ID | ConsolidationBillOrgId | — |
| ORG_ID | ConsolidationBillReverseOrgId | — |
| PRINT_STATUS | ConsBillInvPrintStatus | — |
| PRINT_STATUS | ConsolidationBillPrintStatus | — |
| PRINT_STATUS | ConsolidationBillReversePrintStatus | — |
| REMIT_TO_ADDRESS_ID | ConsBillInvRemitToAddressId | — |
| REMIT_TO_ADDRESS_ID | ConsolidationBillRemitToAddressId | — |
| REMIT_TO_ADDRESS_ID | ConsolidationBillReverseRemitToAddressId | — |
| REMIT_TO_ADDRESS_SEQ_ID | ConsBillInvRemitToAddressSeqId | — |
| REMIT_TO_ADDRESS_SEQ_ID | ConsolidationBillRemitToAddressSeqId | — |
| REMIT_TO_ADDRESS_SEQ_ID | ConsolidationBillReverseRemitToAddressSeqId | — |
| SITE_USE_ID | ConsBillInvSiteUseId | — |
| SITE_USE_ID | ConsolidationBillReverseSiteUseId | — |
| SITE_USE_ID | ConsolidationBillSiteUseId | — |
| START_DATE | ConsBillInvStartDate | — |
| START_DATE | ConsolidationBillReverseStartDate | — |
| START_DATE | ConsolidationBillStartDate | — |
| STATUS | ConsBillInvStatus | — |
| STATUS | ConsolidationBillReverseStatus | — |
| STATUS | ConsolidationBillStatus | — |
| TERM_ID | ConsBillInvTermId | — |
| TERM_ID | ConsolidationBillReverseTermId | — |
| TERM_ID | ConsolidationBillTermId | — |
| TOTAL_ADJUSTMENTS_AMT | ConsBillInvTotalAdjustmentsAmt | — |
| TOTAL_ADJUSTMENTS_AMT | ConsolidationBillReverseTotalAdjustmentsAmt | — |
| TOTAL_ADJUSTMENTS_AMT | ConsolidationBillTotalAdjustmentsAmt | — |
| TOTAL_CREDITS_AMT | ConsBillInvTotalCreditsAmt | — |
| TOTAL_CREDITS_AMT | ConsolidationBillReverseTotalCreditsAmt | — |
| TOTAL_CREDITS_AMT | ConsolidationBillTotalCreditsAmt | — |
| TOTAL_FINANCE_CHARGES_AMT | ConsBillInvTotalFinanceChargesAmt | — |
| TOTAL_FINANCE_CHARGES_AMT | ConsolidationBillReverseTotalFinanceChargesAmt | — |
| TOTAL_FINANCE_CHARGES_AMT | ConsolidationBillTotalFinanceChargesAmt | — |
| TOTAL_RECEIPTS_AMT | ConsBillInvTotalReceiptsAmt | — |
| TOTAL_RECEIPTS_AMT | ConsolidationBillReverseTotalReceiptsAmt | — |
| TOTAL_RECEIPTS_AMT | ConsolidationBillTotalReceiptsAmt | — |
| TOTAL_TAX_AMT | ConsBillInvTotalTaxAmt | — |
| TOTAL_TAX_AMT | ConsolidationBillReverseTotalTaxAmt | — |
| TOTAL_TAX_AMT | ConsolidationBillTotalTaxAmt | — |
| TOTAL_TRX_AMT | ConsBillInvTotalTrxAmt | — |
| TOTAL_TRX_AMT | ConsolidationBillReverseTotalTrxAmt | — |
| TOTAL_TRX_AMT | ConsolidationBillTotalTrxAmt | — |
| UNPAID_REASON | ConsBillInvUnpaidReason | — |
| UNPAID_REASON | ConsolidationBillReverseUnpaidReason | — |
| UNPAID_REASON | ConsolidationBillUnpaidReason | — |

### [[receiptapplicationdistributionvc|ReceiptApplicationDistributionVC]] (AR · BICC: 4/132)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGING_BUCKET1_AMT | ConsBillInvAgingBucket1Amt | — |
| AGING_BUCKET1_AMT | ConsolidationBillAgingBucket1Amt | — |
| AGING_BUCKET1_AMT | ConsolidationBillReverseAgingBucket1Amt | — |
| AGING_BUCKET2_AMT | ConsBillInvAgingBucket2Amt | — |
| AGING_BUCKET2_AMT | ConsolidationBillAgingBucket2Amt | — |
| AGING_BUCKET2_AMT | ConsolidationBillReverseAgingBucket2Amt | — |
| AGING_BUCKET3_AMT | ConsBillInvAgingBucket3Amt | — |
| AGING_BUCKET3_AMT | ConsolidationBillAgingBucket3Amt | — |
| AGING_BUCKET3_AMT | ConsolidationBillReverseAgingBucket3Amt | — |
| AGING_BUCKET4_AMT | ConsBillInvAgingBucket4Amt | — |
| AGING_BUCKET4_AMT | ConsolidationBillAgingBucket4Amt | — |
| AGING_BUCKET4_AMT | ConsolidationBillReverseAgingBucket4Amt | — |
| AGING_BUCKET5_AMT | ConsBillInvAgingBucket5Amt | — |
| AGING_BUCKET5_AMT | ConsolidationBillAgingBucket5Amt | — |
| AGING_BUCKET5_AMT | ConsolidationBillReverseAgingBucket5Amt | — |
| AGING_BUCKET6_AMT | ConsBillInvAgingBucket6Amt | — |
| AGING_BUCKET6_AMT | ConsolidationBillAgingBucket6Amt | — |
| AGING_BUCKET6_AMT | ConsolidationBillReverseAgingBucket6Amt | — |
| AGING_BUCKET7_AMT | ConsBillInvAgingBucket7Amt | — |
| AGING_BUCKET7_AMT | ConsolidationBillAgingBucket7Amt | — |
| AGING_BUCKET7_AMT | ConsolidationBillReverseAgingBucket7Amt | — |
| BEGINNING_BALANCE | ConsBillInvBeginningBalance | — |
| BEGINNING_BALANCE | ConsolidationBillBeginningBalance | — |
| BEGINNING_BALANCE | ConsolidationBillReverseBeginningBalance | — |
| BILL_LEVEL_FLAG | ConsBillInvBillLevelFlag | — |
| BILL_LEVEL_FLAG | ConsolidationBillBillLevelFlag | — |
| BILL_LEVEL_FLAG | ConsolidationBillReverseBillLevelFlag | — |
| BILLING_CYCLE_ID | ConsBillInvBillingCycleId | — |
| BILLING_CYCLE_ID | ConsolidationBillBillingCycleId | — |
| BILLING_CYCLE_ID | ConsolidationBillReverseBillingCycleId | — |
| BILLING_DATE | ConsBillInvBillingDate | — |
| BILLING_DATE | ConsolidationBillBillingDate | — |
| BILLING_DATE | ConsolidationBillReverseBillingDate | — |
| CONCURRENT_REQUEST_ID | ConsBillInvConcurrentRequestId | — |
| CONCURRENT_REQUEST_ID | ConsolidationBillConcurrentRequestId | — |
| CONCURRENT_REQUEST_ID | ConsolidationBillReverseConcurrentRequestId | — |
| CONS_BILLING_NUMBER | ConsBillInvConsBillingNumber | ✅ |
| CONS_BILLING_NUMBER | ConsolidationBillConsBillingNumber | — |
| CONS_BILLING_NUMBER | ConsolidationBillReverseConsBillingNumber | — |
| CONS_INV_ID | ConsBillInvConsInvId | — |
| CONS_INV_ID | ConsolidationBillConsInvId | — |
| CONS_INV_ID | ConsolidationBillReverseConsInvId | — |
| CONS_INV_TYPE | ConsBillInvConsInvType | — |
| CONS_INV_TYPE | ConsolidationBillConsInvType | — |
| CONS_INV_TYPE | ConsolidationBillReverseConsInvType | — |
| CREATED_BY | ConsBillInvCreatedBy | — |
| CREATED_BY | ConsolidationBillCreatedBy | — |
| CREATED_BY | ConsolidationBillReverseCreatedBy | — |
| CREATION_DATE | ConsBillInvCreationDate | — |
| CREATION_DATE | ConsolidationBillCreationDate | — |
| CREATION_DATE | ConsolidationBillReverseCreationDate | — |
| CURRENCY_CODE | ConsBillInvCurrencyCode | — |
| CURRENCY_CODE | ConsolidationBillCurrencyCode | — |
| CURRENCY_CODE | ConsolidationBillReverseCurrencyCode | — |
| CUSTOMER_ID | ConsBillInvCustomerId | — |
| CUSTOMER_ID | ConsolidationBillCustomerId | — |
| CUSTOMER_ID | ConsolidationBillReverseCustomerId | — |
| CUT_OFF_DATE | ConsBillInvCutOffDate | — |
| CUT_OFF_DATE | ConsolidationBillCutOffDate | — |
| CUT_OFF_DATE | ConsolidationBillReverseCutOffDate | — |
| DUE_DATE | ConsBillInvDueDate | — |
| DUE_DATE | ConsolidationBillDueDate | — |
| DUE_DATE | ConsolidationBillReverseDueDate | — |
| ENDING_BALANCE | ConsBillInvEndingBalance | — |
| ENDING_BALANCE | ConsolidationBillEndingBalance | — |
| ENDING_BALANCE | ConsolidationBillReverseEndingBalance | — |
| ISSUE_DATE | ConsBillInvIssueDate | — |
| ISSUE_DATE | ConsolidationBillIssueDate | — |
| ISSUE_DATE | ConsolidationBillReverseIssueDate | — |
| LAST_BILLING_DATE | ConsBillInvLastBillingDate | — |
| LAST_BILLING_DATE | ConsolidationBillLastBillingDate | — |
| LAST_BILLING_DATE | ConsolidationBillReverseLastBillingDate | — |
| LAST_CHARGE_DATE | ConsBillInvLastChargeDate | — |
| LAST_CHARGE_DATE | ConsolidationBillLastChargeDate | — |
| LAST_CHARGE_DATE | ConsolidationBillReverseLastChargeDate | — |
| LAST_UPDATE_DATE | ConsBillInvLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ConsolidationBillLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ConsolidationBillReverseLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ConsBillInvLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ConsolidationBillLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ConsolidationBillReverseLastUpdateLogin | — |
| LAST_UPDATED_BY | ConsBillInvLastUpdatedBy | — |
| LAST_UPDATED_BY | ConsolidationBillLastUpdatedBy | — |
| LAST_UPDATED_BY | ConsolidationBillReverseLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ConsBillInvObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ConsolidationBillObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ConsolidationBillReverseObjectVersionNumber | — |
| ORG_ID | ConsBillInvOrgId | — |
| ORG_ID | ConsolidationBillOrgId | — |
| ORG_ID | ConsolidationBillReverseOrgId | — |
| PRINT_STATUS | ConsBillInvPrintStatus | — |
| PRINT_STATUS | ConsolidationBillPrintStatus | — |
| PRINT_STATUS | ConsolidationBillReversePrintStatus | — |
| REMIT_TO_ADDRESS_ID | ConsBillInvRemitToAddressId | — |
| REMIT_TO_ADDRESS_ID | ConsolidationBillRemitToAddressId | — |
| REMIT_TO_ADDRESS_ID | ConsolidationBillReverseRemitToAddressId | — |
| REMIT_TO_ADDRESS_SEQ_ID | ConsBillInvRemitToAddressSeqId | — |
| REMIT_TO_ADDRESS_SEQ_ID | ConsolidationBillRemitToAddressSeqId | — |
| REMIT_TO_ADDRESS_SEQ_ID | ConsolidationBillReverseRemitToAddressSeqId | — |
| SITE_USE_ID | ConsBillInvSiteUseId | — |
| SITE_USE_ID | ConsolidationBillReverseSiteUseId | — |
| SITE_USE_ID | ConsolidationBillSiteUseId | — |
| START_DATE | ConsBillInvStartDate | — |
| START_DATE | ConsolidationBillReverseStartDate | — |
| START_DATE | ConsolidationBillStartDate | — |
| STATUS | ConsBillInvStatus | — |
| STATUS | ConsolidationBillReverseStatus | — |
| STATUS | ConsolidationBillStatus | — |
| TERM_ID | ConsBillInvTermId | — |
| TERM_ID | ConsolidationBillReverseTermId | — |
| TERM_ID | ConsolidationBillTermId | — |
| TOTAL_ADJUSTMENTS_AMT | ConsBillInvTotalAdjustmentsAmt | — |
| TOTAL_ADJUSTMENTS_AMT | ConsolidationBillReverseTotalAdjustmentsAmt | — |
| TOTAL_ADJUSTMENTS_AMT | ConsolidationBillTotalAdjustmentsAmt | — |
| TOTAL_CREDITS_AMT | ConsBillInvTotalCreditsAmt | — |
| TOTAL_CREDITS_AMT | ConsolidationBillReverseTotalCreditsAmt | — |
| TOTAL_CREDITS_AMT | ConsolidationBillTotalCreditsAmt | — |
| TOTAL_FINANCE_CHARGES_AMT | ConsBillInvTotalFinanceChargesAmt | — |
| TOTAL_FINANCE_CHARGES_AMT | ConsolidationBillReverseTotalFinanceChargesAmt | — |
| TOTAL_FINANCE_CHARGES_AMT | ConsolidationBillTotalFinanceChargesAmt | — |
| TOTAL_RECEIPTS_AMT | ConsBillInvTotalReceiptsAmt | — |
| TOTAL_RECEIPTS_AMT | ConsolidationBillReverseTotalReceiptsAmt | — |
| TOTAL_RECEIPTS_AMT | ConsolidationBillTotalReceiptsAmt | — |
| TOTAL_TAX_AMT | ConsBillInvTotalTaxAmt | — |
| TOTAL_TAX_AMT | ConsolidationBillReverseTotalTaxAmt | — |
| TOTAL_TAX_AMT | ConsolidationBillTotalTaxAmt | — |
| TOTAL_TRX_AMT | ConsBillInvTotalTrxAmt | — |
| TOTAL_TRX_AMT | ConsolidationBillReverseTotalTrxAmt | — |
| TOTAL_TRX_AMT | ConsolidationBillTotalTrxAmt | — |
| UNPAID_REASON | ConsBillInvUnpaidReason | — |
| UNPAID_REASON | ConsolidationBillReverseUnpaidReason | — |
| UNPAID_REASON | ConsolidationBillUnpaidReason | — |

### [[receiptapplicationpvo|ReceiptApplicationPVO]] (AR · BICC: 3/88)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGING_BUCKET1_AMT | ConsTrxAgingBucket1Amt | — |
| AGING_BUCKET1_AMT | ToConsTrxAgingBucket1Amt | — |
| AGING_BUCKET2_AMT | ConsTrxAgingBucket2Amt | — |
| AGING_BUCKET2_AMT | ToConsTrxAgingBucket2Amt | — |
| AGING_BUCKET3_AMT | ConsTrxAgingBucket3Amt | — |
| AGING_BUCKET3_AMT | ToConsTrxAgingBucket3Amt | — |
| AGING_BUCKET4_AMT | ConsTrxAgingBucket4Amt | — |
| AGING_BUCKET4_AMT | ToConsTrxAgingBucket4Amt | — |
| AGING_BUCKET5_AMT | ConsTrxAgingBucket5Amt | — |
| AGING_BUCKET5_AMT | ToConsTrxAgingBucket5Amt | — |
| AGING_BUCKET6_AMT | ConsTrxAgingBucket6Amt | — |
| AGING_BUCKET6_AMT | ToConsTrxAgingBucket6Amt | — |
| AGING_BUCKET7_AMT | ConsTrxAgingBucket7Amt | — |
| AGING_BUCKET7_AMT | ToConsTrxAgingBucket7Amt | — |
| BEGINNING_BALANCE | ConsTrxBeginningBalance | — |
| BEGINNING_BALANCE | ToConsTrxBeginningBalance | — |
| BILL_LEVEL_FLAG | ConsTrxBillLevelFlag | — |
| BILL_LEVEL_FLAG | ToConsTrxBillLevelFlag | — |
| BILLING_CYCLE_ID | ConsTrxBillingCycleId | — |
| BILLING_CYCLE_ID | ToConsTrxBillingCycleId | — |
| BILLING_DATE | ConsTrxBillingDate | — |
| BILLING_DATE | ToConsTrxBillingDate | — |
| CONCURRENT_REQUEST_ID | ConsTrxConcurrentRequestId | — |
| CONCURRENT_REQUEST_ID | ToConsTrxConcurrentRequestId | — |
| CONS_BILLING_NUMBER | ConsTrxConsBillingNumber | ✅ |
| CONS_BILLING_NUMBER | ToConsTrxConsBillingNumber | — |
| CONS_INV_ID | ConsTrxConsInvId | — |
| CONS_INV_ID | ToConsTrxConsInvId | — |
| CONS_INV_TYPE | ConsTrxConsInvType | — |
| CONS_INV_TYPE | ToConsTrxConsInvType | — |
| CREATED_BY | ConsTrxCreatedBy | — |
| CREATED_BY | ToConsTrxCreatedBy | — |
| CREATION_DATE | ConsTrxCreationDate | — |
| CREATION_DATE | ToConsTrxCreationDate | — |
| CURRENCY_CODE | ConsTrxCurrencyCode | — |
| CURRENCY_CODE | ToConsTrxCurrencyCode | — |
| CUSTOMER_ID | ConsTrxCustomerId | — |
| CUSTOMER_ID | ToConsTrxCustomerId | — |
| CUT_OFF_DATE | ConsTrxCutOffDate | — |
| CUT_OFF_DATE | ToConsTrxCutOffDate | — |
| DUE_DATE | ConsTrxDueDate | — |
| DUE_DATE | ToConsTrxDueDate | — |
| ENDING_BALANCE | ConsTrxEndingBalance | — |
| ENDING_BALANCE | ToConsTrxEndingBalance | — |
| ISSUE_DATE | ConsTrxIssueDate | — |
| ISSUE_DATE | ToConsTrxIssueDate | — |
| LAST_BILLING_DATE | ConsTrxLastBillingDate | — |
| LAST_BILLING_DATE | ToConsTrxLastBillingDate | — |
| LAST_CHARGE_DATE | ConsTrxLastChargeDate | — |
| LAST_CHARGE_DATE | ToConsTrxLastChargeDate | — |
| LAST_UPDATE_DATE | ConsTrxLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ToConsTrxLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ConsTrxLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ToConsTrxLastUpdateLogin | — |
| LAST_UPDATED_BY | ConsTrxLastUpdatedBy | — |
| LAST_UPDATED_BY | ToConsTrxLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ConsTrxObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ToConsTrxObjectVersionNumber | — |
| ORG_ID | ConsTrxOrgId | — |
| ORG_ID | ToConsTrxOrgId | — |
| PRINT_STATUS | ConsTrxPrintStatus | — |
| PRINT_STATUS | ToConsTrxPrintStatus | — |
| REMIT_TO_ADDRESS_ID | ConsTrxRemitToAddressId | — |
| REMIT_TO_ADDRESS_ID | ToConsTrxRemitToAddressId | — |
| REMIT_TO_ADDRESS_SEQ_ID | ConsTrxRemitToAddressSeqId | — |
| REMIT_TO_ADDRESS_SEQ_ID | ToConsTrxRemitToAddressSeqId | — |
| SITE_USE_ID | ConsTrxSiteUseId | — |
| SITE_USE_ID | ToConsTrxSiteUseId | — |
| START_DATE | ConsTrxStartDate | — |
| START_DATE | ToConsTrxStartDate | — |
| STATUS | ConsTrxStatus | — |
| STATUS | ToConsTrxStatus | — |
| TERM_ID | ConsTrxTermId | — |
| TERM_ID | ToConsTrxTermId | — |
| TOTAL_ADJUSTMENTS_AMT | ConsTrxTotalAdjustmentsAmt | — |
| TOTAL_ADJUSTMENTS_AMT | ToConsTrxTotalAdjustmentsAmt | — |
| TOTAL_CREDITS_AMT | ConsTrxTotalCreditsAmt | — |
| TOTAL_CREDITS_AMT | ToConsTrxTotalCreditsAmt | — |
| TOTAL_FINANCE_CHARGES_AMT | ConsTrxTotalFinanceChargesAmt | — |
| TOTAL_FINANCE_CHARGES_AMT | ToConsTrxTotalFinanceChargesAmt | — |
| TOTAL_RECEIPTS_AMT | ConsTrxTotalReceiptsAmt | — |
| TOTAL_RECEIPTS_AMT | ToConsTrxTotalReceiptsAmt | — |
| TOTAL_TAX_AMT | ConsTrxTotalTaxAmt | — |
| TOTAL_TAX_AMT | ToConsTrxTotalTaxAmt | — |
| TOTAL_TRX_AMT | ConsTrxTotalTrxAmt | — |
| TOTAL_TRX_AMT | ToConsTrxTotalTrxAmt | — |
| UNPAID_REASON | ConsTrxUnpaidReason | — |
| UNPAID_REASON | ToConsTrxUnpaidReason | — |

---

## 📚 Referências

- Oracle Fusion Cloud Financials — Accounts Receivable Tables (OEDMF Release 13).
- Oracle Fusion Cloud — Balance Forward Billing Documentation.
- Oracle Fusion Cloud ERP Schema Reference (Release 25A).
