---
id: DOC-AR-017
doc_type: system-doc
title: "AR_CASH_RECEIPTS_ALL — Recebimentos (Receipts)"
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
  - recebimentos
  - receipts
  - cash-receipts
aliases:
  - AR_CASH_RECEIPTS_ALL
  - ar_cash_receipts_all
  - recebimentos-ar
  - cash-receipts
  - receipts-ar
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_CASH_RECEIPTS_ALL

## 📌 Visão Geral

Armazena um registro para **cada recebimento** (receipt) do módulo Accounts Receivable. Cada linha representa um recebimento individual, contendo valor, moeda, data, status do ciclo de vida (APP, UNAPP, UNID, NSF, REV, STOP) e referência ao cliente pagador. É a tabela central para rastreamento de todos os recebimentos de caixa, sejam eles manuais, automáticos ou importados via interface.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Registro de recebimentos:** Cada pagamento recebido de clientes gera um registro nesta tabela, incluindo recebimentos manuais, automáticos e por lockbox.
- **Controle de status:** Rastreamento do ciclo de vida do recebimento — aplicado, não-aplicado, não-identificado, NSF, revertido ou parado.
- **Conciliação bancária:** Vinculação de recebimentos a contas bancárias de remessa para reconciliação.
- **Aging de recebimentos:** Base para análise de recebimentos não-aplicados por faixa de data.
- **Auditoria e compliance:** Rastreabilidade completa de cada recebimento com sequência de documento e WHO columns.
- **Câmbio:** Suporte a recebimentos em moeda estrangeira com taxa de conversão.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CASH_RECEIPT_ID | NUMBER(18) | NOT NULL | PK | Identificador único do recebimento | — | 🟢 100% |
| 2 | RECEIPT_NUMBER | VARCHAR2(30) | NOT NULL | Identificação | Número do recebimento visível ao usuário | — | 🟢 100% |
| 3 | AMOUNT | NUMBER | NOT NULL | Financeiro | Valor do recebimento na moeda da transação | — | 🟢 100% |
| 4 | CURRENCY_CODE | VARCHAR2(15) | NOT NULL | Financeiro | Código da moeda do recebimento (ISO 4217) | — | 🟢 100% |
| 5 | RECEIPT_DATE | DATE | NOT NULL | Data | Data do recebimento | — | 🟢 100% |
| 6 | STATUS | VARCHAR2(30) | NOT NULL | Classificação | Status do recebimento (APP/UNAPP/UNID/NSF/REV/STOP) | — | 🟢 100% |
| 7 | TYPE | VARCHAR2(30) | NULL | Classificação | Tipo do recebimento (CASH/MISC) | — | 🟢 100% |
| 8 | PAY_FROM_CUSTOMER | NUMBER(18) | NULL | Cliente | Conta do cliente pagador | [[hz_cust_accounts]] | 🟢 100% |
| 9 | CUSTOMER_SITE_USE_ID | NUMBER(18) | NULL | Cliente | Site de uso do cliente | [[hz_cust_site_uses_all]] | 🟢 100% |
| 10 | RECEIPT_METHOD_ID | NUMBER(18) | NOT NULL | Classificação | Método de recebimento utilizado | [[ar_receipt_methods]] | 🟢 100% |
| 11 | REMITTANCE_BANK_ACCOUNT_ID | NUMBER(18) | NULL | Bancário | Conta bancária de remessa | [[ce_bank_acct_uses_all]] | 🟢 100% |
| 12 | DOC_SEQUENCE_ID | NUMBER(18) | NULL | Identificação | ID da sequência de documento | [[fnd_document_sequences]] | 🟢 100% |
| 13 | DOC_SEQUENCE_VALUE | NUMBER(15) | NULL | Identificação | Número de sequência de documento legal | — | 🟢 100% |
| 14 | EXCHANGE_RATE_TYPE | VARCHAR2(30) | NULL | Financeiro | Tipo de taxa de câmbio | [[gl_daily_conversion_types]] | 🟢 100% |
| 15 | EXCHANGE_RATE | NUMBER | NULL | Financeiro | Taxa de câmbio aplicada | — | 🟢 100% |
| 16 | EXCHANGE_DATE | DATE | NULL | Financeiro | Data da taxa de câmbio | — | 🟢 100% |
| 17 | DEPOSIT_DATE | DATE | NULL | Data | Data do depósito bancário | — | 🟢 100% |
| 18 | GL_DATE | DATE | NULL | Contabilidade | Data contábil (General Ledger) | — | 🟢 100% |
| 19 | REVERSAL_DATE | DATE | NULL | Data | Data de reversão do recebimento | — | 🟢 100% |
| 20 | REVERSAL_REASON_CODE | VARCHAR2(30) | NULL | Classificação | Motivo da reversão | — | 🟢 100% |
| 21 | REVERSAL_CATEGORY | VARCHAR2(30) | NULL | Classificação | Categoria da reversão (NSF/DEBIT/REV) | — | 🟢 100% |
| 22 | CASH_RECEIPT_HISTORY_ID | NUMBER(18) | NULL | Referência cruzada | Registro atual do histórico | [[ar_cash_receipt_history_all]] | 🟢 100% |
| 23 | COMMENTS | VARCHAR2(2000) | NULL | Texto livre | Comentários livres sobre o recebimento | — | 🟢 100% |
| 24 | CUSTOMER_RECEIPT_REFERENCE | VARCHAR2(30) | NULL | Referência externa | Referência do cliente para o pagamento | — | 🟢 100% |
| 25 | ANTICIPATED_CLEARING_DATE | DATE | NULL | Data | Data prevista de compensação | — | 🟢 100% |
| 26 | CONFIRMED_FLAG | VARCHAR2(1) | NULL | Status | Indica se recebimento foi confirmado (Y/N) | — | 🟢 100% |
| 27 | OVERRIDE_REMIT_ACCOUNT_FLAG | VARCHAR2(1) | NULL | Controle | Conta de remessa sobrescrita manualmente (Y/N) | — | 🟡 75% |
| 28 | MISC_PAYMENT_SOURCE | VARCHAR2(30) | NULL | Classificação | Origem de recebimentos avulsos | — | 🟢 100% |
| 29 | DISTRIBUTION_SET_ID | NUMBER(18) | NULL | Contabilidade | Conjunto de distribuição para misc receipts | [[ar_distribution_sets_all]] | 🟢 100% |
| 30 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 31 | LEGAL_ENTITY_ID | NUMBER(18) | NULL | Multi-Org | Entidade legal | [[xle_entity_profiles]] | 🟢 100% |
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
- [[hz_cust_accounts]] — via `PAY_FROM_CUSTOMER` (cliente pagador)
- [[hz_cust_site_uses_all]] — via `CUSTOMER_SITE_USE_ID` (site do cliente)
- [[ar_receipt_methods]] — via `RECEIPT_METHOD_ID` (método de recebimento)
- [[ce_bank_acct_uses_all]] — via `REMITTANCE_BANK_ACCOUNT_ID` (conta bancária de depósito do recebimento)
- [[ar_distribution_sets_all]] — via `DISTRIBUTION_SET_ID` (distribuição para misc receipts)
- [[gl_daily_conversion_types]] — via `EXCHANGE_RATE_TYPE` (tipo de câmbio aplicado ao recebimento)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit do recebimento de caixa)
- [[xle_entity_profiles]] — via `LEGAL_ENTITY_ID` (entidade legal do recebimento de caixa)

### Tabelas-filha (FK de saída)
- [[ar_cash_receipt_history_all]] — via `CASH_RECEIPT_ID` (histórico do recebimento)
- [[ar_receivable_applications_all]] — via `CASH_RECEIPT_ID` (aplicações de recebimento contra faturas ou contas)
- [[ar_payment_schedules_all]] — via `CASH_RECEIPT_ID` (schedule de pagamento)
- [[ar_misc_cash_distributions_all]] — via `CASH_RECEIPT_ID` (distribuições de misc receipts)
- [[ar_cash_remit_refs_all]] — via `CASH_RECEIPT_ID` (referências de remessa)

---

## 📎 Uso Típico

### Listar recebimentos não-aplicados
```sql
SELECT cr.RECEIPT_NUMBER, cr.AMOUNT, cr.CURRENCY_CODE,
       cr.RECEIPT_DATE, cr.STATUS
FROM   AR_CASH_RECEIPTS_ALL cr
WHERE  cr.STATUS = 'UNAPP'
  AND  cr.ORG_ID = :p_org_id;
```

### Recebimentos com dados do cliente
```sql
SELECT cr.RECEIPT_NUMBER, cr.AMOUNT, cr.RECEIPT_DATE,
       hca.ACCOUNT_NUMBER, hca.ACCOUNT_NAME
FROM   AR_CASH_RECEIPTS_ALL cr
JOIN   HZ_CUST_ACCOUNTS hca ON hca.CUST_ACCOUNT_ID = cr.PAY_FROM_CUSTOMER
WHERE  cr.RECEIPT_DATE BETWEEN :start_date AND :end_date
  AND  cr.ORG_ID = :p_org_id;
```

### Filtros comuns
- `STATUS = 'APP'` — Recebimentos aplicados
- `STATUS = 'UNAPP'` — Recebimentos não-aplicados
- `TYPE = 'CASH'` — Apenas recebimentos de caixa (exclui misc)
- `RECEIPT_DATE BETWEEN :start AND :end` — Período

---

## 🔒 Observações

- O campo `STATUS` controla o ciclo de vida: **APP** (aplicado), **UNAPP** (não-aplicado), **UNID** (não-identificado), **NSF** (sem fundos), **REV** (revertido), **STOP** (parado).
- Recebimentos do tipo **MISC** (avulsos) utilizam `DISTRIBUTION_SET_ID` para contabilização direta, sem vinculação a faturas.
- A coluna `CASH_RECEIPT_HISTORY_ID` aponta para o registro **mais recente** do histórico em [[ar_cash_receipt_history_all]].
- Campos `REVERSAL_*` são preenchidos apenas quando o recebimento é revertido.
- A tabela possui **Descriptive Flexfields (DFF)** via colunas `ATTRIBUTE1–15` para customizações por implementação.

---

## 🔗 PVOs Relacionados

### [[adjustmentdistributionpvo|AdjustmentDistributionPVO]] (AR · BICC: 3/86)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTUAL_VALUE_DATE | ReceiptActualValueDate | — |
| ADDRESS_VERIFICATION_CODE | ReceiptAddressVerificationCode | — |
| AMOUNT | ReceiptAmount | — |
| ANTICIPATED_CLEARING_DATE | ReceiptAnticipatedClearingDate | — |
| APPLICATION_NOTES | ReceiptApplicationNotes | — |
| APPROVAL_CODE | ReceiptApprovalCode | — |
| AUTOAPPLY_FLAG | ReceiptAutoapplyFlag | — |
| AUTOMATCH_REQUEST_ID | ReceiptAutomatchRequestId | — |
| AX_ACCOUNTED_FLAG | ReceiptAxAccountedFlag | — |
| CASH_RECEIPT_ID | ReceiptCashReceiptId | — |
| CASH_RECEIPT_ID | ReverseReceiptCashReceiptId | — |
| CC_ERROR_CODE | ReceiptCcErrorCode | — |
| CC_ERROR_FLAG | ReceiptCcErrorFlag | — |
| CC_ERROR_TEXT | ReceiptCcErrorText | — |
| CODE_COMBINATION_ID | ReceiptCodeCombinationId | — |
| COLLECTOR_ID | ReceiptCollectorId | — |
| COMMENTS | ReceiptComments | — |
| CONFIRMED_FLAG | ReceiptConfirmedFlag | — |
| CREATED_BY | ReceiptCreatedBy | — |
| CREATION_DATE | ReceiptCreationDate | — |
| CURRENCY_CODE | ReceiptCurrencyCode | — |
| CUSTOMER_BANK_ACCOUNT_ID | ReceiptCustomerBankAccountId | — |
| CUSTOMER_BANK_BRANCH_ID | ReceiptCustomerBankBranchId | — |
| CUSTOMER_RECEIPT_REFERENCE | ReceiptCustomerReceiptReference | — |
| CUSTOMER_SITE_USE_ID | ReceiptCustomerSiteUseId | — |
| DEPOSIT_DATE | ReceiptDepositDate | — |
| DISTRIBUTION_SET_ID | ReceiptDistributionSetId | — |
| DOC_SEQUENCE_ID | ReceiptDocSequenceId | — |
| DOC_SEQUENCE_VALUE | ReceiptDocSequenceValue | — |
| EXCHANGE_DATE | ReceiptExchangeDate | — |
| EXCHANGE_RATE | ReceiptExchangeRate | — |
| EXCHANGE_RATE_TYPE | ReceiptExchangeRateType | — |
| FACTOR_DISCOUNT_AMOUNT | ReceiptFactorDiscountAmount | — |
| ISSUE_DATE | ReceiptIssueDate | — |
| ISSUER_BANK_BRANCH_ID | ReceiptIssuerBankBranchId | — |
| ISSUER_NAME | ReceiptIssuerName | — |
| LAST_UPDATE_DATE | ReceiptLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ReceiptLastUpdateLogin | — |
| LAST_UPDATED_BY | ReceiptLastUpdatedBy | — |
| LEGAL_ENTITY_ID | ReceiptLegalEntityId | — |
| LOGICAL_GROUP_REFERENCE | ReceiptLogicalGroupReference | — |
| MISC_PAYMENT_SOURCE | ReceiptMiscPaymentSource | — |
| OBJECT_VERSION_NUMBER | ReceiptObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ReverseReceiptObjectVersionNumber8 | — |
| OLD_CUSTOMER_BANK_ACCOUNT_ID | ReceiptOldCustomerBankAccountId | — |
| OLD_CUSTOMER_BANK_BRANCH_ID | ReceiptOldCustomerBankBranchId | — |
| OLD_ISSUER_BANK_BRANCH_ID | ReceiptOldIssuerBankBranchId | — |
| ORG_ID | ReceiptOrgId | — |
| OVERRIDE_REMIT_ACCOUNT_FLAG | ReceiptOverrideRemitAccountFlag | — |
| PAY_FROM_CUSTOMER | ReceiptPayFromCustomer | — |
| PAYMENT_SERVER_ORDER_NUM | ReceiptPaymentServerOrderNum | — |
| PAYMENT_TRXN_EXTENSION_ID | ReceiptPaymentTrxnExtensionId | — |
| POSTMARK_DATE | ReceiptPostmarkDate | — |
| PROGRAM_APPLICATION_ID | ReceiptProgramApplicationId | — |
| PROGRAM_ID | ReceiptProgramId | — |
| PROGRAM_UPDATE_DATE | ReceiptProgramUpdateDate | — |
| PROMISE_SOURCE | ReceiptPromiseSource | — |
| REC_VERSION_NUMBER | ReceiptRecVersionNumber | — |
| RECEIPT_BATCH_ID | ReceiptReceiptBatchId | — |
| RECEIPT_DATE | ReceiptReceiptDate | — |
| RECEIPT_METHOD_ID | ReceiptReceiptMethodId | — |
| RECEIPT_NUMBER | ReceiptReceiptNumber | ✅ |
| RECEIPT_NUMBER | ReverseReceiptReceiptNumber | ✅ |
| RECEIVABLES_TRX_ID | ReceiptReceivablesTrxId | — |
| RECON_FLAG | ReceiptReconFlag | — |
| REFERENCE_ID | ReceiptReferenceId | — |
| REFERENCE_TYPE | ReceiptReferenceType | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptRemitBankAcctUseId | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptRemittanceBankAccountId | — |
| REMITTANCE_BATCH_ID | ReceiptRemittanceBatchId | — |
| REQUEST_ID | ReceiptRequestId | — |
| RESOURCE_ID | ReceiptResourceId | — |
| REVERSAL_CATEGORY | ReceiptReversalCategory | — |
| REVERSAL_COMMENTS | ReceiptReversalComments | — |
| REVERSAL_DATE | ReceiptReversalDate | — |
| REVERSAL_REASON_CODE | ReceiptReversalReasonCode | — |
| SELECTED_FOR_FACTORING_FLAG | ReceiptSelectedForFactoringFlag | — |
| SELECTED_REMITTANCE_BATCH_ID | ReceiptSelectedRemittanceBatchId | — |
| SET_OF_BOOKS_ID | ReceiptSetOfBooksId | — |
| STATUS | ReceiptStatus | — |
| TAX_RATE | ReceiptTaxRate | — |
| TYPE | ReceiptType | — |
| UNIQUE_REFERENCE | ReceiptUniqueReference | — |
| USSGL_TRANSACTION_CODE | ReceiptUssglTransactionCode | — |
| USSGL_TRANSACTION_CODE_CONTEXT | ReceiptUssglTransactionCodeContext | — |
| VAT_TAX_ID | ReceiptVatTaxId | — |

### [[adjustmentpvo|AdjustmentPVO]] (AR · BICC: 3/86)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTUAL_VALUE_DATE | ReceiptsActualValueDate | — |
| ADDRESS_VERIFICATION_CODE | ReceiptsAddressVerificationCode | — |
| AMOUNT | ReceiptsAmount | — |
| ANTICIPATED_CLEARING_DATE | ReceiptsAnticipatedClearingDate | — |
| APPLICATION_NOTES | ReceiptsApplicationNotes | — |
| APPROVAL_CODE | ReceiptsApprovalCode | — |
| AUTOAPPLY_FLAG | ReceiptsAutoapplyFlag | — |
| AUTOMATCH_REQUEST_ID | ReceiptsAutomatchRequestId | — |
| AX_ACCOUNTED_FLAG | ReceiptsAxAccountedFlag | — |
| CASH_RECEIPT_ID | ReceiptsCashReceiptId | — |
| CASH_RECEIPT_ID | ReverseReceiptCashReceiptId | — |
| CC_ERROR_CODE | ReceiptsCcErrorCode | — |
| CC_ERROR_FLAG | ReceiptsCcErrorFlag | — |
| CC_ERROR_TEXT | ReceiptsCcErrorText | — |
| CODE_COMBINATION_ID | ReceiptsCodeCombinationId | — |
| COLLECTOR_ID | ReceiptsCollectorId | — |
| COMMENTS | ReceiptsComments | — |
| CONFIRMED_FLAG | ReceiptsConfirmedFlag | — |
| CREATED_BY | ReceiptsCreatedBy | — |
| CREATION_DATE | ReceiptsCreationDate | — |
| CURRENCY_CODE | ReceiptsCurrencyCode | — |
| CUSTOMER_BANK_ACCOUNT_ID | ReceiptsCustomerBankAccountId | — |
| CUSTOMER_BANK_BRANCH_ID | ReceiptsCustomerBankBranchId | — |
| CUSTOMER_RECEIPT_REFERENCE | ReceiptsCustomerReceiptReference | — |
| CUSTOMER_SITE_USE_ID | ReceiptsCustomerSiteUseId | — |
| DEPOSIT_DATE | ReceiptsDepositDate | — |
| DISTRIBUTION_SET_ID | ReceiptsDistributionSetId | — |
| DOC_SEQUENCE_ID | ReceiptsDocSequenceId | — |
| DOC_SEQUENCE_VALUE | ReceiptsDocSequenceValue | — |
| EXCHANGE_DATE | ReceiptsExchangeDate | — |
| EXCHANGE_RATE | ReceiptsExchangeRate | — |
| EXCHANGE_RATE_TYPE | ReceiptsExchangeRateType | — |
| FACTOR_DISCOUNT_AMOUNT | ReceiptsFactorDiscountAmount | — |
| ISSUE_DATE | ReceiptsIssueDate | — |
| ISSUER_BANK_BRANCH_ID | ReceiptsIssuerBankBranchId | — |
| ISSUER_NAME | ReceiptsIssuerName | — |
| LAST_UPDATE_DATE | ReceiptsLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ReceiptsLastUpdateLogin | — |
| LAST_UPDATED_BY | ReceiptsLastUpdatedBy | — |
| LEGAL_ENTITY_ID | ReceiptsLegalEntityId | — |
| LOGICAL_GROUP_REFERENCE | ReceiptsLogicalGroupReference | — |
| MISC_PAYMENT_SOURCE | ReceiptsMiscPaymentSource | — |
| OBJECT_VERSION_NUMBER | ReceiptsObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ReverseReceiptObjectVersionNumber5 | — |
| OLD_CUSTOMER_BANK_ACCOUNT_ID | ReceiptsOldCustomerBankAccountId | — |
| OLD_CUSTOMER_BANK_BRANCH_ID | ReceiptsOldCustomerBankBranchId | — |
| OLD_ISSUER_BANK_BRANCH_ID | ReceiptsOldIssuerBankBranchId | — |
| ORG_ID | ReceiptsOrgId | — |
| OVERRIDE_REMIT_ACCOUNT_FLAG | ReceiptsOverrideRemitAccountFlag | — |
| PAY_FROM_CUSTOMER | ReceiptsPayFromCustomer | — |
| PAYMENT_SERVER_ORDER_NUM | ReceiptsPaymentServerOrderNum | — |
| PAYMENT_TRXN_EXTENSION_ID | ReceiptsPaymentTrxnExtensionId | — |
| POSTMARK_DATE | ReceiptsPostmarkDate | — |
| PROGRAM_APPLICATION_ID | ReceiptsProgramApplicationId | — |
| PROGRAM_ID | ReceiptsProgramId | — |
| PROGRAM_UPDATE_DATE | ReceiptsProgramUpdateDate | — |
| PROMISE_SOURCE | ReceiptsPromiseSource | — |
| REC_VERSION_NUMBER | ReceiptsRecVersionNumber | — |
| RECEIPT_BATCH_ID | ReceiptsReceiptBatchId | — |
| RECEIPT_DATE | ReceiptsReceiptDate | — |
| RECEIPT_METHOD_ID | ReceiptsReceiptMethodId | — |
| RECEIPT_NUMBER | ReceiptsReceiptNumber | ✅ |
| RECEIPT_NUMBER | ReverseReceiptReceiptNumber | ✅ |
| RECEIVABLES_TRX_ID | ReceiptsReceivablesTrxId | — |
| RECON_FLAG | ReceiptsReconFlag | — |
| REFERENCE_ID | ReceiptsReferenceId | — |
| REFERENCE_TYPE | ReceiptsReferenceType | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptsRemitBankAcctUseId | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptsRemittanceBankAccountId | — |
| REMITTANCE_BATCH_ID | ReceiptsRemittanceBatchId | — |
| REQUEST_ID | ReceiptsRequestId | — |
| RESOURCE_ID | ReceiptsResourceId | — |
| REVERSAL_CATEGORY | ReceiptsReversalCategory | — |
| REVERSAL_COMMENTS | ReceiptsReversalComments | — |
| REVERSAL_DATE | ReceiptsReversalDate | — |
| REVERSAL_REASON_CODE | ReceiptsReversalReasonCode | — |
| SELECTED_FOR_FACTORING_FLAG | ReceiptsSelectedForFactoringFlag | — |
| SELECTED_REMITTANCE_BATCH_ID | ReceiptsSelectedRemittanceBatchId | — |
| SET_OF_BOOKS_ID | ReceiptsSetOfBooksId | — |
| STATUS | ReceiptsStatus | — |
| TAX_RATE | ReceiptsTaxRate | — |
| TYPE | ReceiptsType | — |
| UNIQUE_REFERENCE | ReceiptsUniqueReference | — |
| USSGL_TRANSACTION_CODE | ReceiptsUssglTransactionCode | — |
| USSGL_TRANSACTION_CODE_CONTEXT | ReceiptsUssglTransactionCodeContext | — |
| VAT_TAX_ID | ReceiptsVatTaxId | — |

### [[completedtrxrevadjdistributionpvo|CompletedTrxRevAdjDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTUAL_VALUE_DATE | ReceiptActualValueDate | — |
| ADDRESS_VERIFICATION_CODE | ReceiptAddressVerificationCode | — |
| AMOUNT | ReceiptAmount | — |
| ANTICIPATED_CLEARING_DATE | ReceiptAnticipatedClearingDate | — |
| APPLICATION_NOTES | ReceiptApplicationNotes | — |
| APPROVAL_CODE | ReceiptApprovalCode | — |
| AUTOAPPLY_FLAG | ReceiptAutoapplyFlag | — |
| AUTOMATCH_REQUEST_ID | ReceiptAutomatchRequestId | — |
| AX_ACCOUNTED_FLAG | ReceiptAxAccountedFlag | — |
| CASH_RECEIPT_ID | ReceiptCashReceiptId | — |
| CC_ERROR_CODE | ReceiptCcErrorCode | — |
| CC_ERROR_FLAG | ReceiptCcErrorFlag | — |
| CC_ERROR_TEXT | ReceiptCcErrorText | — |
| CODE_COMBINATION_ID | ReceiptCodeCombinationId | — |
| COLLECTOR_ID | ReceiptCollectorId | — |
| COMMENTS | ReceiptComments | — |
| CONFIRMED_FLAG | ReceiptConfirmedFlag | — |
| CURRENCY_CODE | ReceiptCurrencyCode | — |
| CUSTOMER_BANK_ACCOUNT_ID | ReceiptCustomerBankAccountId | — |
| CUSTOMER_BANK_BRANCH_ID | ReceiptCustomerBankBranchId | — |
| CUSTOMER_RECEIPT_REFERENCE | ReceiptCustomerReceiptReference | — |
| CUSTOMER_SITE_USE_ID | ReceiptCustomerSiteUseId | — |
| DEPOSIT_DATE | ReceiptDepositDate | — |
| DISTRIBUTION_SET_ID | ReceiptDistributionSetId | — |
| DOC_SEQUENCE_ID | ReceiptDocSequenceId | — |
| DOC_SEQUENCE_VALUE | ReceiptDocSequenceValue | — |
| EXCHANGE_DATE | ReceiptExchangeDate | — |
| EXCHANGE_RATE | ReceiptExchangeRate | — |
| EXCHANGE_RATE_TYPE | ReceiptExchangeRateType | — |
| FACTOR_DISCOUNT_AMOUNT | ReceiptFactorDiscountAmount | — |
| ISSUE_DATE | ReceiptIssueDate | — |
| ISSUER_BANK_BRANCH_ID | ReceiptIssuerBankBranchId | — |
| ISSUER_NAME | ReceiptIssuerName | — |
| LEGAL_ENTITY_ID | ReceiptLegalEntityId | — |
| LOGICAL_GROUP_REFERENCE | ReceiptLogicalGroupReference | — |
| MISC_PAYMENT_SOURCE | ReceiptMiscPaymentSource | — |
| OLD_CUSTOMER_BANK_ACCOUNT_ID | ReceiptOldCustomerBankAccountId | — |
| OLD_CUSTOMER_BANK_BRANCH_ID | ReceiptOldCustomerBankBranchId | — |
| OLD_ISSUER_BANK_BRANCH_ID | ReceiptOldIssuerBankBranchId | — |
| ORG_ID | ReceiptOrgId | — |
| OVERRIDE_REMIT_ACCOUNT_FLAG | ReceiptOverrideRemitAccountFlag | — |
| PAY_FROM_CUSTOMER | ReceiptPayFromCustomer | — |
| PAYMENT_SERVER_ORDER_NUM | ReceiptPaymentServerOrderNum | — |
| PAYMENT_TRXN_EXTENSION_ID | ReceiptPaymentTrxnExtensionId | — |
| POSTMARK_DATE | ReceiptPostmarkDate | — |
| PROGRAM_APPLICATION_ID | ReceiptProgramApplicationId | — |
| PROGRAM_ID | ReceiptProgramId | — |
| PROGRAM_UPDATE_DATE | ReceiptProgramUpdateDate | — |
| PROMISE_SOURCE | ReceiptPromiseSource | — |
| REC_VERSION_NUMBER | ReceiptRecVersionNumber | — |
| RECEIPT_BATCH_ID | ReceiptReceiptBatchId | — |
| RECEIPT_DATE | ReceiptReceiptDate | — |
| RECEIPT_METHOD_ID | ReceiptReceiptMethodId | — |
| RECEIPT_NUMBER | ReceiptReceiptNumber | — |
| RECEIVABLES_TRX_ID | ReceiptReceivablesTrxId | — |
| RECON_FLAG | ReceiptReconFlag | — |
| REFERENCE_ID | ReceiptReferenceId | — |
| REFERENCE_TYPE | ReceiptReferenceType | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptRemitBankAcctUseId | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptRemittanceBankAccountId | — |
| REMITTANCE_BATCH_ID | ReceiptRemittanceBatchId | — |
| REQUEST_ID | ReceiptRequestId | — |
| RESOURCE_ID | ReceiptResourceId | — |
| REVERSAL_CATEGORY | ReceiptReversalCategory | — |
| REVERSAL_COMMENTS | ReceiptReversalComments | — |
| REVERSAL_DATE | ReceiptReversalDate | — |
| REVERSAL_REASON_CODE | ReceiptReversalReasonCode | — |
| SELECTED_FOR_FACTORING_FLAG | ReceiptSelectedForFactoringFlag | — |
| SELECTED_REMITTANCE_BATCH_ID | ReceiptSelectedRemittanceBatchId | — |
| SET_OF_BOOKS_ID | ReceiptSetOfBooksId | — |
| STATUS | ReceiptStatus | — |
| TAX_RATE | ReceiptTaxRate | — |
| TYPE | ReceiptType | — |
| UNIQUE_REFERENCE | ReceiptUniqueReference | — |
| USSGL_TRANSACTION_CODE | ReceiptUssglTransactionCode | — |
| USSGL_TRANSACTION_CODE_CONTEXT | ReceiptUssglTransactionCodeContext | — |
| VAT_TAX_ID | ReceiptVatTaxId | — |

### [[headersalescreditpvo|HeaderSalesCreditPVO]] (AR · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CASH_RECEIPT_ID | RevCashRcptCashReceiptId | — |
| COMMENTS | RevCashRcptComments | — |
| ISSUER_NAME | RevCashRcptIssuerName | — |
| OBJECT_VERSION_NUMBER | RevCashRcptObjectVersionNumber | — |
| RECEIPT_NUMBER | RevCashRcptReceiptNumber | ✅ |

### [[linesalescreditpvo|LineSalesCreditPVO]] (AR · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CASH_RECEIPT_ID | RevCashRcptCashReceiptId | — |
| COMMENTS | RevCashRcptComments | — |
| ISSUER_NAME | RevCashRcptIssuerName | — |
| OBJECT_VERSION_NUMBER | RevCashRcptObjectVersionNumber | — |
| RECEIPT_NUMBER | RevCashRcptReceiptNumber | ✅ |

### [[miscreceiptdistributionpvo|MiscReceiptDistributionPVO]] (AR · BICC: 26/83)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTUAL_VALUE_DATE | ReceiptActualValueDate | ✅ |
| ADDRESS_VERIFICATION_CODE | ReceiptAddressVerificationCode | — |
| AMOUNT | ReceiptAmount | — |
| ANTICIPATED_CLEARING_DATE | ReceiptAnticipatedClearingDate | ✅ |
| APPLICATION_NOTES | ReceiptApplicationNotes | — |
| APPROVAL_CODE | ReceiptApprovalCode | — |
| AUTOAPPLY_FLAG | ReceiptAutoapplyFlag | — |
| AUTOMATCH_REQUEST_ID | ReceiptAutomatchRequestId | — |
| AX_ACCOUNTED_FLAG | ReceiptAxAccountedFlag | — |
| CASH_RECEIPT_ID | ReceiptCashReceiptId | ✅ |
| CC_ERROR_CODE | ReceiptCcErrorCode | — |
| CC_ERROR_FLAG | ReceiptCcErrorFlag | — |
| CC_ERROR_TEXT | ReceiptCcErrorText | — |
| CODE_COMBINATION_ID | ReceiptCodeCombinationId | — |
| COLLECTOR_ID | ReceiptCollectorId | — |
| COMMENTS | ReceiptComments | ✅ |
| CONFIRMED_FLAG | ReceiptConfirmedFlag | ✅ |
| CREATED_BY | ReceiptCreatedBy | ✅ |
| CREATION_DATE | ReceiptCreationDate | ✅ |
| CURRENCY_CODE | ReceiptCurrencyCode | — |
| CUSTOMER_BANK_ACCOUNT_ID | ReceiptCustomerBankAccountId | — |
| CUSTOMER_BANK_BRANCH_ID | ReceiptCustomerBankBranchId | — |
| CUSTOMER_RECEIPT_REFERENCE | ReceiptCustomerReceiptReference | ✅ |
| CUSTOMER_SITE_USE_ID | ReceiptCustomerSiteUseId | — |
| DEPOSIT_DATE | ReceiptDepositDate | ✅ |
| DISTRIBUTION_SET_ID | ReceiptDistributionSetId | — |
| DOC_SEQUENCE_ID | ReceiptDocSequenceId | — |
| DOC_SEQUENCE_VALUE | ReceiptDocSequenceValue | ✅ |
| EXCHANGE_DATE | ReceiptExchangeDate | ✅ |
| EXCHANGE_RATE | ReceiptExchangeRate | ✅ |
| EXCHANGE_RATE_TYPE | ReceiptExchangeRateType | ✅ |
| FACTOR_DISCOUNT_AMOUNT | ReceiptFactorDiscountAmount | — |
| ISSUE_DATE | ReceiptIssueDate | — |
| ISSUER_BANK_BRANCH_ID | ReceiptIssuerBankBranchId | — |
| ISSUER_NAME | ReceiptIssuerName | — |
| LAST_UPDATE_DATE | ReceiptLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ReceiptLastUpdateLogin | — |
| LAST_UPDATED_BY | ReceiptLastUpdatedBy | ✅ |
| LEGAL_ENTITY_ID | ReceiptLegalEntityId | — |
| LOGICAL_GROUP_REFERENCE | ReceiptLogicalGroupReference | — |
| MISC_PAYMENT_SOURCE | ReceiptMiscPaymentSource | ✅ |
| OBJECT_VERSION_NUMBER | ReceiptObjectVersionNumber | — |
| OLD_CUSTOMER_BANK_ACCOUNT_ID | ReceiptOldCustomerBankAccountId | — |
| OLD_CUSTOMER_BANK_BRANCH_ID | ReceiptOldCustomerBankBranchId | — |
| OLD_ISSUER_BANK_BRANCH_ID | ReceiptOldIssuerBankBranchId | — |
| ORG_ID | ReceiptOrgId | — |
| OVERRIDE_REMIT_ACCOUNT_FLAG | ReceiptOverrideRemitAccountFlag | — |
| PAY_FROM_CUSTOMER | ReceiptPayFromCustomer | — |
| PAYMENT_SERVER_ORDER_NUM | ReceiptPaymentServerOrderNum | — |
| PAYMENT_TRXN_EXTENSION_ID | ReceiptPaymentTrxnExtensionId | — |
| POSTMARK_DATE | ReceiptPostmarkDate | ✅ |
| PROGRAM_APPLICATION_ID | ReceiptProgramApplicationId | — |
| PROGRAM_ID | ReceiptProgramId | — |
| PROGRAM_UPDATE_DATE | ReceiptProgramUpdateDate | — |
| PROMISE_SOURCE | ReceiptPromiseSource | — |
| REC_VERSION_NUMBER | ReceiptRecVersionNumber | — |
| RECEIPT_BATCH_ID | ReceiptReceiptBatchId | — |
| RECEIPT_DATE | ReceiptReceiptDate | ✅ |
| RECEIPT_METHOD_ID | ReceiptReceiptMethodId | — |
| RECEIPT_NUMBER | ReceiptReceiptNumber | ✅ |
| RECEIVABLES_TRX_ID | ReceiptReceivablesTrxId | — |
| RECON_FLAG | ReceiptReconFlag | — |
| REFERENCE_ID | ReceiptReferenceId | — |
| REFERENCE_TYPE | ReceiptReferenceType | ✅ |
| REMIT_BANK_ACCT_USE_ID | ReceiptRemitBankAcctUseId | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptRemittanceBankAccountId | — |
| REMITTANCE_BATCH_ID | ReceiptRemittanceBatchId | — |
| REQUEST_ID | ReceiptRequestId | — |
| RESOURCE_ID | ReceiptResourceId | — |
| REVERSAL_CATEGORY | ReceiptReversalCategory | ✅ |
| REVERSAL_COMMENTS | ReceiptReversalComments | ✅ |
| REVERSAL_DATE | ReceiptReversalDate | ✅ |
| REVERSAL_REASON_CODE | ReceiptReversalReasonCode | ✅ |
| SELECTED_FOR_FACTORING_FLAG | ReceiptSelectedForFactoringFlag | — |
| SELECTED_REMITTANCE_BATCH_ID | ReceiptSelectedRemittanceBatchId | — |
| SET_OF_BOOKS_ID | ReceiptSetOfBooksId | — |
| STATUS | ReceiptStatus | — |
| TAX_RATE | ReceiptTaxRate | ✅ |
| TYPE | ReceiptType | ✅ |
| UNIQUE_REFERENCE | ReceiptUniqueReference | — |
| USSGL_TRANSACTION_CODE | ReceiptUssglTransactionCode | — |
| USSGL_TRANSACTION_CODE_CONTEXT | ReceiptUssglTransactionCodeContext | — |
| VAT_TAX_ID | ReceiptVatTaxId | — |

### [[paymentschedulepvo|PaymentSchedulePVO]] (AR · BICC: 7/332)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTUAL_VALUE_DATE | ReceiptActualValueDate | — |
| ACTUAL_VALUE_DATE | ReceiptAssociatedActualValueDate | — |
| ACTUAL_VALUE_DATE | ReceiptLastActualValueDate | — |
| ACTUAL_VALUE_DATE | ReceiptReverseActualValueDate | — |
| ADDRESS_VERIFICATION_CODE | ReceiptAddressVerificationCode | — |
| ADDRESS_VERIFICATION_CODE | ReceiptAssociatedAddressVerificationCode | — |
| ADDRESS_VERIFICATION_CODE | ReceiptLastAddressVerificationCode | — |
| ADDRESS_VERIFICATION_CODE | ReceiptReverseAddressVerificationCode | — |
| AMOUNT | ReceiptAmount | — |
| AMOUNT | ReceiptAssociatedAmount | — |
| AMOUNT | ReceiptLastAmount | — |
| AMOUNT | ReceiptReverseAmount | — |
| ANTICIPATED_CLEARING_DATE | ReceiptAnticipatedClearingDate | — |
| ANTICIPATED_CLEARING_DATE | ReceiptAssociatedAnticipatedClearingDate | — |
| ANTICIPATED_CLEARING_DATE | ReceiptLastAnticipatedClearingDate | — |
| ANTICIPATED_CLEARING_DATE | ReceiptReverseAnticipatedClearingDate | — |
| APPLICATION_NOTES | ReceiptApplicationNotes | — |
| APPLICATION_NOTES | ReceiptAssociatedApplicationNotes | — |
| APPLICATION_NOTES | ReceiptLastApplicationNotes | — |
| APPLICATION_NOTES | ReceiptReverseApplicationNotes | — |
| APPROVAL_CODE | ReceiptApprovalCode | — |
| APPROVAL_CODE | ReceiptAssociatedApprovalCode | — |
| APPROVAL_CODE | ReceiptLastApprovalCode | — |
| APPROVAL_CODE | ReceiptReverseApprovalCode | — |
| AUTOAPPLY_FLAG | ReceiptAssociatedAutoapplyFlag | — |
| AUTOAPPLY_FLAG | ReceiptAutoapplyFlag | — |
| AUTOAPPLY_FLAG | ReceiptLastAutoapplyFlag | — |
| AUTOAPPLY_FLAG | ReceiptReverseAutoapplyFlag | — |
| AUTOMATCH_REQUEST_ID | ReceiptAssociatedAutomatchRequestId | — |
| AUTOMATCH_REQUEST_ID | ReceiptAutomatchRequestId | — |
| AUTOMATCH_REQUEST_ID | ReceiptLastAutomatchRequestId | — |
| AUTOMATCH_REQUEST_ID | ReceiptReverseAutomatchRequestId | — |
| AX_ACCOUNTED_FLAG | ReceiptAssociatedAxAccountedFlag | — |
| AX_ACCOUNTED_FLAG | ReceiptAxAccountedFlag | — |
| AX_ACCOUNTED_FLAG | ReceiptLastAxAccountedFlag | — |
| AX_ACCOUNTED_FLAG | ReceiptReverseAxAccountedFlag | — |
| CASH_RECEIPT_ID | ReceiptAssociatedCashReceiptId | — |
| CASH_RECEIPT_ID | ReceiptCashReceiptId | — |
| CASH_RECEIPT_ID | ReceiptLastCashReceiptId | — |
| CASH_RECEIPT_ID | ReceiptReverseCashReceiptId | — |
| CC_ERROR_CODE | ReceiptAssociatedCcErrorCode | — |
| CC_ERROR_CODE | ReceiptCcErrorCode | — |
| CC_ERROR_CODE | ReceiptLastCcErrorCode | — |
| CC_ERROR_CODE | ReceiptReverseCcErrorCode | — |
| CC_ERROR_FLAG | ReceiptAssociatedCcErrorFlag | — |
| CC_ERROR_FLAG | ReceiptCcErrorFlag | — |
| CC_ERROR_FLAG | ReceiptLastCcErrorFlag | — |
| CC_ERROR_FLAG | ReceiptReverseCcErrorFlag | — |
| CC_ERROR_TEXT | ReceiptAssociatedCcErrorText | — |
| CC_ERROR_TEXT | ReceiptCcErrorText | — |
| CC_ERROR_TEXT | ReceiptLastCcErrorText | — |
| CC_ERROR_TEXT | ReceiptReverseCcErrorText | — |
| CODE_COMBINATION_ID | ReceiptAssociatedCodeCombinationId | — |
| CODE_COMBINATION_ID | ReceiptCodeCombinationId | — |
| CODE_COMBINATION_ID | ReceiptLastCodeCombinationId | — |
| CODE_COMBINATION_ID | ReceiptReverseCodeCombinationId | — |
| COLLECTOR_ID | ReceiptAssociatedCollectorId | — |
| COLLECTOR_ID | ReceiptCollectorId | — |
| COLLECTOR_ID | ReceiptLastCollectorId | — |
| COLLECTOR_ID | ReceiptReverseCollectorId | — |
| COMMENTS | ReceiptAssociatedComments | — |
| COMMENTS | ReceiptComments | — |
| COMMENTS | ReceiptLastComments | — |
| COMMENTS | ReceiptReverseComments | — |
| CONFIRMED_FLAG | ReceiptAssociatedConfirmedFlag | — |
| CONFIRMED_FLAG | ReceiptConfirmedFlag | — |
| CONFIRMED_FLAG | ReceiptLastConfirmedFlag | — |
| CONFIRMED_FLAG | ReceiptReverseConfirmedFlag | — |
| CREATED_BY | ReceiptAssociatedCreatedBy | — |
| CREATED_BY | ReceiptCreatedBy | — |
| CREATED_BY | ReceiptLastCreatedBy | — |
| CREATED_BY | ReceiptReverseCreatedBy | — |
| CREATION_DATE | ReceiptAssociatedCreationDate | — |
| CREATION_DATE | ReceiptCreationDate | — |
| CREATION_DATE | ReceiptLastCreationDate | — |
| CREATION_DATE | ReceiptReverseCreationDate | — |
| CURRENCY_CODE | ReceiptAssociatedCurrencyCode | — |
| CURRENCY_CODE | ReceiptCurrencyCode | — |
| CURRENCY_CODE | ReceiptLastCurrencyCode | — |
| CURRENCY_CODE | ReceiptReverseCurrencyCode | — |
| CUSTOMER_BANK_ACCOUNT_ID | ReceiptAssociatedCustomerBankAccountId | — |
| CUSTOMER_BANK_ACCOUNT_ID | ReceiptCustomerBankAccountId | — |
| CUSTOMER_BANK_ACCOUNT_ID | ReceiptLastCustomerBankAccountId | — |
| CUSTOMER_BANK_ACCOUNT_ID | ReceiptReverseCustomerBankAccountId | — |
| CUSTOMER_BANK_BRANCH_ID | ReceiptAssociatedCustomerBankBranchId | — |
| CUSTOMER_BANK_BRANCH_ID | ReceiptCustomerBankBranchId | — |
| CUSTOMER_BANK_BRANCH_ID | ReceiptLastCustomerBankBranchId | — |
| CUSTOMER_BANK_BRANCH_ID | ReceiptReverseCustomerBankBranchId | — |
| CUSTOMER_RECEIPT_REFERENCE | ReceiptAssociatedCustomerReceiptReference | — |
| CUSTOMER_RECEIPT_REFERENCE | ReceiptCustomerReceiptReference | — |
| CUSTOMER_RECEIPT_REFERENCE | ReceiptLastCustomerReceiptReference | — |
| CUSTOMER_RECEIPT_REFERENCE | ReceiptReverseCustomerReceiptReference | — |
| CUSTOMER_SITE_USE_ID | ReceiptAssociatedCustomerSiteUseId | — |
| CUSTOMER_SITE_USE_ID | ReceiptCustomerSiteUseId | — |
| CUSTOMER_SITE_USE_ID | ReceiptLastCustomerSiteUseId | — |
| CUSTOMER_SITE_USE_ID | ReceiptReverseCustomerSiteUseId | — |
| DEPOSIT_DATE | ReceiptAssociatedDepositDate | — |
| DEPOSIT_DATE | ReceiptDepositDate | — |
| DEPOSIT_DATE | ReceiptLastDepositDate | — |
| DEPOSIT_DATE | ReceiptReverseDepositDate | — |
| DISTRIBUTION_SET_ID | ReceiptAssociatedDistributionSetId | — |
| DISTRIBUTION_SET_ID | ReceiptDistributionSetId | — |
| DISTRIBUTION_SET_ID | ReceiptLastDistributionSetId | — |
| DISTRIBUTION_SET_ID | ReceiptReverseDistributionSetId | — |
| DOC_SEQUENCE_ID | ReceiptAssociatedDocSequenceId | — |
| DOC_SEQUENCE_ID | ReceiptDocSequenceId | — |
| DOC_SEQUENCE_ID | ReceiptLastDocSequenceId | — |
| DOC_SEQUENCE_ID | ReceiptReverseDocSequenceId | — |
| DOC_SEQUENCE_VALUE | ReceiptAssociatedDocSequenceValue | — |
| DOC_SEQUENCE_VALUE | ReceiptDocSequenceValue | — |
| DOC_SEQUENCE_VALUE | ReceiptLastDocSequenceValue | — |
| DOC_SEQUENCE_VALUE | ReceiptReverseDocSequenceValue | — |
| EXCHANGE_DATE | ReceiptAssociatedExchangeDate | — |
| EXCHANGE_DATE | ReceiptExchangeDate | — |
| EXCHANGE_DATE | ReceiptLastExchangeDate | — |
| EXCHANGE_DATE | ReceiptReverseExchangeDate | — |
| EXCHANGE_RATE | ReceiptAssociatedExchangeRate | — |
| EXCHANGE_RATE | ReceiptExchangeRate | — |
| EXCHANGE_RATE | ReceiptLastExchangeRate | — |
| EXCHANGE_RATE | ReceiptReverseExchangeRate | — |
| EXCHANGE_RATE_TYPE | ReceiptAssociatedExchangeRateType | — |
| EXCHANGE_RATE_TYPE | ReceiptExchangeRateType | — |
| EXCHANGE_RATE_TYPE | ReceiptLastExchangeRateType | — |
| EXCHANGE_RATE_TYPE | ReceiptReverseExchangeRateType | — |
| FACTOR_DISCOUNT_AMOUNT | ReceiptAssociatedFactorDiscountAmount | — |
| FACTOR_DISCOUNT_AMOUNT | ReceiptFactorDiscountAmount | — |
| FACTOR_DISCOUNT_AMOUNT | ReceiptLastFactorDiscountAmount | — |
| FACTOR_DISCOUNT_AMOUNT | ReceiptReverseFactorDiscountAmount | — |
| ISSUE_DATE | ReceiptAssociatedIssueDate | — |
| ISSUE_DATE | ReceiptIssueDate | — |
| ISSUE_DATE | ReceiptLastIssueDate | — |
| ISSUE_DATE | ReceiptReverseIssueDate | — |
| ISSUER_BANK_BRANCH_ID | ReceiptAssociatedIssuerBankBranchId | — |
| ISSUER_BANK_BRANCH_ID | ReceiptIssuerBankBranchId | — |
| ISSUER_BANK_BRANCH_ID | ReceiptLastIssuerBankBranchId | — |
| ISSUER_BANK_BRANCH_ID | ReceiptReverseIssuerBankBranchId | — |
| ISSUER_NAME | ReceiptAssociatedIssuerName | — |
| ISSUER_NAME | ReceiptIssuerName | — |
| ISSUER_NAME | ReceiptLastIssuerName | — |
| ISSUER_NAME | ReceiptReverseIssuerName | — |
| LAST_UPDATE_DATE | ReceiptAssociatedLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ReceiptLastLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ReceiptLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ReceiptReverseLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ReceiptAssociatedLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ReceiptLastLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ReceiptLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ReceiptReverseLastUpdateLogin | — |
| LAST_UPDATED_BY | ReceiptAssociatedLastUpdatedBy | — |
| LAST_UPDATED_BY | ReceiptLastLastUpdatedBy | — |
| LAST_UPDATED_BY | ReceiptLastUpdatedBy | — |
| LAST_UPDATED_BY | ReceiptReverseLastUpdatedBy | — |
| LEGAL_ENTITY_ID | ReceiptAssociatedLegalEntityId | — |
| LEGAL_ENTITY_ID | ReceiptLastLegalEntityId | — |
| LEGAL_ENTITY_ID | ReceiptLegalEntityId | — |
| LEGAL_ENTITY_ID | ReceiptReverseLegalEntityId | — |
| LOGICAL_GROUP_REFERENCE | ReceiptAssociatedLogicalGroupReference | — |
| LOGICAL_GROUP_REFERENCE | ReceiptLastLogicalGroupReference | — |
| LOGICAL_GROUP_REFERENCE | ReceiptLogicalGroupReference | — |
| LOGICAL_GROUP_REFERENCE | ReceiptReverseLogicalGroupReference | — |
| MISC_PAYMENT_SOURCE | ReceiptAssociatedMiscPaymentSource | — |
| MISC_PAYMENT_SOURCE | ReceiptLastMiscPaymentSource | — |
| MISC_PAYMENT_SOURCE | ReceiptMiscPaymentSource | — |
| MISC_PAYMENT_SOURCE | ReceiptReverseMiscPaymentSource | — |
| OBJECT_VERSION_NUMBER | ReceiptAssociatedObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ReceiptLastObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ReceiptObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ReceiptReverseObjectVersionNumber | — |
| OLD_CUSTOMER_BANK_ACCOUNT_ID | ReceiptAssociatedOldCustomerBankAccountId | — |
| OLD_CUSTOMER_BANK_ACCOUNT_ID | ReceiptLastOldCustomerBankAccountId | — |
| OLD_CUSTOMER_BANK_ACCOUNT_ID | ReceiptOldCustomerBankAccountId | — |
| OLD_CUSTOMER_BANK_ACCOUNT_ID | ReceiptReverseOldCustomerBankAccountId | — |
| OLD_CUSTOMER_BANK_BRANCH_ID | ReceiptAssociatedOldCustomerBankBranchId | — |
| OLD_CUSTOMER_BANK_BRANCH_ID | ReceiptLastOldCustomerBankBranchId | — |
| OLD_CUSTOMER_BANK_BRANCH_ID | ReceiptOldCustomerBankBranchId | — |
| OLD_CUSTOMER_BANK_BRANCH_ID | ReceiptReverseOldCustomerBankBranchId | — |
| OLD_ISSUER_BANK_BRANCH_ID | ReceiptAssociatedOldIssuerBankBranchId | — |
| OLD_ISSUER_BANK_BRANCH_ID | ReceiptLastOldIssuerBankBranchId | — |
| OLD_ISSUER_BANK_BRANCH_ID | ReceiptOldIssuerBankBranchId | — |
| OLD_ISSUER_BANK_BRANCH_ID | ReceiptReverseOldIssuerBankBranchId | — |
| ORG_ID | ReceiptAssociatedOrgId | — |
| ORG_ID | ReceiptLastOrgId | — |
| ORG_ID | ReceiptOrgId | — |
| ORG_ID | ReceiptReverseOrgId | — |
| OVERRIDE_REMIT_ACCOUNT_FLAG | ReceiptAssociatedOverrideRemitAccountFlag | — |
| OVERRIDE_REMIT_ACCOUNT_FLAG | ReceiptLastOverrideRemitAccountFlag | — |
| OVERRIDE_REMIT_ACCOUNT_FLAG | ReceiptOverrideRemitAccountFlag | — |
| OVERRIDE_REMIT_ACCOUNT_FLAG | ReceiptReverseOverrideRemitAccountFlag | — |
| PAY_FROM_CUSTOMER | ReceiptAssociatedPayFromCustomer | — |
| PAY_FROM_CUSTOMER | ReceiptLastPayFromCustomer | — |
| PAY_FROM_CUSTOMER | ReceiptPayFromCustomer | — |
| PAY_FROM_CUSTOMER | ReceiptReversePayFromCustomer | — |
| PAYMENT_SERVER_ORDER_NUM | ReceiptAssociatedPaymentServerOrderNum | — |
| PAYMENT_SERVER_ORDER_NUM | ReceiptLastPaymentServerOrderNum | — |
| PAYMENT_SERVER_ORDER_NUM | ReceiptPaymentServerOrderNum | — |
| PAYMENT_SERVER_ORDER_NUM | ReceiptReversePaymentServerOrderNum | — |
| PAYMENT_TRXN_EXTENSION_ID | ReceiptAssociatedPaymentTrxnExtensionId | — |
| PAYMENT_TRXN_EXTENSION_ID | ReceiptLastPaymentTrxnExtensionId | — |
| PAYMENT_TRXN_EXTENSION_ID | ReceiptPaymentTrxnExtensionId | — |
| PAYMENT_TRXN_EXTENSION_ID | ReceiptReversePaymentTrxnExtensionId | — |
| POSTMARK_DATE | ReceiptAssociatedPostmarkDate | — |
| POSTMARK_DATE | ReceiptLastPostmarkDate | — |
| POSTMARK_DATE | ReceiptPostmarkDate | — |
| POSTMARK_DATE | ReceiptReversePostmarkDate | — |
| PROGRAM_APPLICATION_ID | ReceiptAssociatedProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | ReceiptLastProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | ReceiptProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | ReceiptReverseProgramApplicationId | — |
| PROGRAM_ID | ReceiptAssociatedProgramId | — |
| PROGRAM_ID | ReceiptLastProgramId | — |
| PROGRAM_ID | ReceiptProgramId | — |
| PROGRAM_ID | ReceiptReverseProgramId | — |
| PROGRAM_UPDATE_DATE | ReceiptAssociatedProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | ReceiptLastProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | ReceiptProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | ReceiptReverseProgramUpdateDate | — |
| PROMISE_SOURCE | ReceiptAssociatedPromiseSource | — |
| PROMISE_SOURCE | ReceiptLastPromiseSource | — |
| PROMISE_SOURCE | ReceiptPromiseSource | — |
| PROMISE_SOURCE | ReceiptReversePromiseSource | — |
| REC_VERSION_NUMBER | ReceiptAssociatedRecVersionNumber | — |
| REC_VERSION_NUMBER | ReceiptLastRecVersionNumber | — |
| REC_VERSION_NUMBER | ReceiptRecVersionNumber | — |
| REC_VERSION_NUMBER | ReceiptReverseRecVersionNumber | — |
| RECEIPT_BATCH_ID | ReceiptAssociatedReceiptBatchId | — |
| RECEIPT_BATCH_ID | ReceiptLastReceiptBatchId | — |
| RECEIPT_BATCH_ID | ReceiptReceiptBatchId | — |
| RECEIPT_BATCH_ID | ReceiptReverseReceiptBatchId | — |
| RECEIPT_DATE | ReceiptAssociatedReceiptDate | — |
| RECEIPT_DATE | ReceiptLastReceiptDate | — |
| RECEIPT_DATE | ReceiptReceiptDate | — |
| RECEIPT_DATE | ReceiptReverseReceiptDate | — |
| RECEIPT_METHOD_ID | ReceiptAssociatedReceiptMethodId | — |
| RECEIPT_METHOD_ID | ReceiptLastReceiptMethodId | — |
| RECEIPT_METHOD_ID | ReceiptReceiptMethodId | — |
| RECEIPT_METHOD_ID | ReceiptReverseReceiptMethodId | — |
| RECEIPT_NUMBER | ReceiptAssociatedReceiptNumber | ✅ |
| RECEIPT_NUMBER | ReceiptLastReceiptNumber | — |
| RECEIPT_NUMBER | ReceiptReceiptNumber | ✅ |
| RECEIPT_NUMBER | ReceiptReverseReceiptNumber | ✅ |
| RECEIVABLES_TRX_ID | ReceiptAssociatedReceivablesTrxId | — |
| RECEIVABLES_TRX_ID | ReceiptLastReceivablesTrxId | — |
| RECEIVABLES_TRX_ID | ReceiptReceivablesTrxId | — |
| RECEIVABLES_TRX_ID | ReceiptReverseReceivablesTrxId | — |
| RECON_FLAG | ReceiptAssociatedReconFlag | — |
| RECON_FLAG | ReceiptLastReconFlag | — |
| RECON_FLAG | ReceiptReconFlag | — |
| RECON_FLAG | ReceiptReverseReconFlag | — |
| REFERENCE_ID | ReceiptAssociatedReferenceId | — |
| REFERENCE_ID | ReceiptLastReferenceId | — |
| REFERENCE_ID | ReceiptReferenceId | — |
| REFERENCE_ID | ReceiptReverseReferenceId | — |
| REFERENCE_TYPE | ReceiptAssociatedReferenceType | — |
| REFERENCE_TYPE | ReceiptLastReferenceType | — |
| REFERENCE_TYPE | ReceiptReferenceType | — |
| REFERENCE_TYPE | ReceiptReverseReferenceType | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptAssociatedRemitBankAcctUseId | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptLastRemitBankAcctUseId | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptRemitBankAcctUseId | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptReverseRemitBankAcctUseId | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptAssociatedRemittanceBankAccountId | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptLastRemittanceBankAccountId | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptRemittanceBankAccountId | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptReverseRemittanceBankAccountId | — |
| REMITTANCE_BATCH_ID | ReceiptAssociatedRemittanceBatchId | — |
| REMITTANCE_BATCH_ID | ReceiptLastRemittanceBatchId | — |
| REMITTANCE_BATCH_ID | ReceiptRemittanceBatchId | — |
| REMITTANCE_BATCH_ID | ReceiptReverseRemittanceBatchId | — |
| REQUEST_ID | ReceiptAssociatedRequestId | — |
| REQUEST_ID | ReceiptLastRequestId | — |
| REQUEST_ID | ReceiptRequestId | — |
| REQUEST_ID | ReceiptReverseRequestId | — |
| RESOURCE_ID | ReceiptAssociatedResourceId | — |
| RESOURCE_ID | ReceiptLastResourceId | — |
| RESOURCE_ID | ReceiptResourceId | — |
| RESOURCE_ID | ReceiptReverseResourceId | — |
| REVERSAL_CATEGORY | ReceiptAssociatedReversalCategory | — |
| REVERSAL_CATEGORY | ReceiptLastReversalCategory | — |
| REVERSAL_CATEGORY | ReceiptReversalCategory | — |
| REVERSAL_CATEGORY | ReceiptReverseReversalCategory | — |
| REVERSAL_COMMENTS | ReceiptAssociatedReversalComments | — |
| REVERSAL_COMMENTS | ReceiptLastReversalComments | — |
| REVERSAL_COMMENTS | ReceiptReversalComments | — |
| REVERSAL_COMMENTS | ReceiptReverseReversalComments | — |
| REVERSAL_DATE | ReceiptAssociatedReversalDate | — |
| REVERSAL_DATE | ReceiptLastReversalDate | — |
| REVERSAL_DATE | ReceiptReversalDate | — |
| REVERSAL_DATE | ReceiptReverseReversalDate | — |
| REVERSAL_REASON_CODE | ReceiptAssociatedReversalReasonCode | — |
| REVERSAL_REASON_CODE | ReceiptLastReversalReasonCode | — |
| REVERSAL_REASON_CODE | ReceiptReversalReasonCode | — |
| REVERSAL_REASON_CODE | ReceiptReverseReversalReasonCode | — |
| SELECTED_FOR_FACTORING_FLAG | ReceiptAssociatedSelectedForFactoringFlag | — |
| SELECTED_FOR_FACTORING_FLAG | ReceiptLastSelectedForFactoringFlag | — |
| SELECTED_FOR_FACTORING_FLAG | ReceiptReverseSelectedForFactoringFlag | — |
| SELECTED_FOR_FACTORING_FLAG | ReceiptSelectedForFactoringFlag | — |
| SELECTED_REMITTANCE_BATCH_ID | ReceiptAssociatedSelectedRemittanceBatchId | — |
| SELECTED_REMITTANCE_BATCH_ID | ReceiptLastSelectedRemittanceBatchId | — |
| SELECTED_REMITTANCE_BATCH_ID | ReceiptReverseSelectedRemittanceBatchId | — |
| SELECTED_REMITTANCE_BATCH_ID | ReceiptSelectedRemittanceBatchId | — |
| SET_OF_BOOKS_ID | ReceiptAssociatedSetOfBooksId | — |
| SET_OF_BOOKS_ID | ReceiptLastSetOfBooksId | — |
| SET_OF_BOOKS_ID | ReceiptReverseSetOfBooksId | — |
| SET_OF_BOOKS_ID | ReceiptSetOfBooksId | — |
| STATUS | ReceiptAssociatedStatus | — |
| STATUS | ReceiptLastStatus | — |
| STATUS | ReceiptReverseStatus | — |
| STATUS | ReceiptStatus | — |
| TAX_RATE | ReceiptAssociatedTaxRate | — |
| TAX_RATE | ReceiptLastTaxRate | — |
| TAX_RATE | ReceiptReverseTaxRate | — |
| TAX_RATE | ReceiptTaxRate | — |
| TYPE | ReceiptAssociatedType | — |
| TYPE | ReceiptLastType | — |
| TYPE | ReceiptReverseType | — |
| TYPE | ReceiptType | — |
| UNIQUE_REFERENCE | ReceiptAssociatedUniqueReference | — |
| UNIQUE_REFERENCE | ReceiptLastUniqueReference | — |
| UNIQUE_REFERENCE | ReceiptReverseUniqueReference | — |
| UNIQUE_REFERENCE | ReceiptUniqueReference | — |
| USSGL_TRANSACTION_CODE | ReceiptAssociatedUssglTransactionCode | — |
| USSGL_TRANSACTION_CODE | ReceiptLastUssglTransactionCode | — |
| USSGL_TRANSACTION_CODE | ReceiptReverseUssglTransactionCode | — |
| USSGL_TRANSACTION_CODE | ReceiptUssglTransactionCode | — |
| USSGL_TRANSACTION_CODE_CONTEXT | ReceiptAssociatedUssglTransactionCodeContext | — |
| USSGL_TRANSACTION_CODE_CONTEXT | ReceiptLastUssglTransactionCodeContext | — |
| USSGL_TRANSACTION_CODE_CONTEXT | ReceiptReverseUssglTransactionCodeContext | — |
| USSGL_TRANSACTION_CODE_CONTEXT | ReceiptUssglTransactionCodeContext | — |
| VAT_TAX_ID | ReceiptAssociatedVatTaxId | — |
| VAT_TAX_ID | ReceiptLastVatTaxId | — |
| VAT_TAX_ID | ReceiptReverseVatTaxId | — |
| VAT_TAX_ID | ReceiptVatTaxId | — |

### [[rateadjustmentpvo|RateAdjustmentPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CASH_RECEIPT_ID | ReceiptCashReceiptId | — |
| SET_OF_BOOKS_ID | ReceiptSetOfBooksId | — |

### [[receiptapplicationdistributionpvo|ReceiptApplicationDistributionPVO]] (AR · BICC: 13/415)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTUAL_VALUE_DATE | ReceiptActualValueDate | — |
| ACTUAL_VALUE_DATE | ReceiptAssociatedActualValueDate | — |
| ACTUAL_VALUE_DATE | ReceiptLastActualValueDate | — |
| ACTUAL_VALUE_DATE | ReceiptReverseActualValueDate | — |
| ACTUAL_VALUE_DATE | ReceiptSchedActualValueDate | — |
| ADDRESS_VERIFICATION_CODE | ReceiptAddressVerificationCode | — |
| ADDRESS_VERIFICATION_CODE | ReceiptAssociatedAddressVerificationCode | — |
| ADDRESS_VERIFICATION_CODE | ReceiptLastAddressVerificationCode | — |
| ADDRESS_VERIFICATION_CODE | ReceiptReverseAddressVerificationCode | — |
| ADDRESS_VERIFICATION_CODE | ReceiptSchedAddressVerificationCode | — |
| AMOUNT | ReceiptAmount | — |
| AMOUNT | ReceiptAssociatedAmount | — |
| AMOUNT | ReceiptLastAmount | — |
| AMOUNT | ReceiptReverseAmount | — |
| AMOUNT | ReceiptSchedAmount | — |
| ANTICIPATED_CLEARING_DATE | ReceiptAnticipatedClearingDate | — |
| ANTICIPATED_CLEARING_DATE | ReceiptAssociatedAnticipatedClearingDate | — |
| ANTICIPATED_CLEARING_DATE | ReceiptLastAnticipatedClearingDate | — |
| ANTICIPATED_CLEARING_DATE | ReceiptReverseAnticipatedClearingDate | — |
| ANTICIPATED_CLEARING_DATE | ReceiptSchedAnticipatedClearingDate | — |
| APPLICATION_NOTES | ReceiptApplicationNotes | — |
| APPLICATION_NOTES | ReceiptAssociatedApplicationNotes | — |
| APPLICATION_NOTES | ReceiptLastApplicationNotes | — |
| APPLICATION_NOTES | ReceiptReverseApplicationNotes | — |
| APPLICATION_NOTES | ReceiptSchedApplicationNotes | — |
| APPROVAL_CODE | ReceiptApprovalCode | — |
| APPROVAL_CODE | ReceiptAssociatedApprovalCode | — |
| APPROVAL_CODE | ReceiptLastApprovalCode | — |
| APPROVAL_CODE | ReceiptReverseApprovalCode | — |
| APPROVAL_CODE | ReceiptSchedApprovalCode | — |
| AUTOAPPLY_FLAG | ReceiptAssociatedAutoapplyFlag | — |
| AUTOAPPLY_FLAG | ReceiptAutoapplyFlag | — |
| AUTOAPPLY_FLAG | ReceiptLastAutoapplyFlag | — |
| AUTOAPPLY_FLAG | ReceiptReverseAutoapplyFlag | — |
| AUTOAPPLY_FLAG | ReceiptSchedAutoapplyFlag | — |
| AUTOMATCH_REQUEST_ID | ReceiptAssociatedAutomatchRequestId | — |
| AUTOMATCH_REQUEST_ID | ReceiptAutomatchRequestId | — |
| AUTOMATCH_REQUEST_ID | ReceiptLastAutomatchRequestId | — |
| AUTOMATCH_REQUEST_ID | ReceiptReverseAutomatchRequestId | — |
| AUTOMATCH_REQUEST_ID | ReceiptSchedAutomatchRequestId | — |
| AX_ACCOUNTED_FLAG | ReceiptAssociatedAxAccountedFlag | — |
| AX_ACCOUNTED_FLAG | ReceiptAxAccountedFlag | — |
| AX_ACCOUNTED_FLAG | ReceiptLastAxAccountedFlag | — |
| AX_ACCOUNTED_FLAG | ReceiptReverseAxAccountedFlag | — |
| AX_ACCOUNTED_FLAG | ReceiptSchedAxAccountedFlag | — |
| CASH_RECEIPT_ID | ReceiptAssociatedCashReceiptId | — |
| CASH_RECEIPT_ID | ReceiptCashReceiptId | — |
| CASH_RECEIPT_ID | ReceiptLastCashReceiptId | — |
| CASH_RECEIPT_ID | ReceiptReverseCashReceiptId | — |
| CASH_RECEIPT_ID | ReceiptSchedCashReceiptId | — |
| CC_ERROR_CODE | ReceiptAssociatedCcErrorCode | — |
| CC_ERROR_CODE | ReceiptCcErrorCode | — |
| CC_ERROR_CODE | ReceiptLastCcErrorCode | — |
| CC_ERROR_CODE | ReceiptReverseCcErrorCode | — |
| CC_ERROR_CODE | ReceiptSchedCcErrorCode | — |
| CC_ERROR_FLAG | ReceiptAssociatedCcErrorFlag | — |
| CC_ERROR_FLAG | ReceiptCcErrorFlag | — |
| CC_ERROR_FLAG | ReceiptLastCcErrorFlag | — |
| CC_ERROR_FLAG | ReceiptReverseCcErrorFlag | — |
| CC_ERROR_FLAG | ReceiptSchedCcErrorFlag | — |
| CC_ERROR_TEXT | ReceiptAssociatedCcErrorText | — |
| CC_ERROR_TEXT | ReceiptCcErrorText | — |
| CC_ERROR_TEXT | ReceiptLastCcErrorText | — |
| CC_ERROR_TEXT | ReceiptReverseCcErrorText | — |
| CC_ERROR_TEXT | ReceiptSchedCcErrorText | — |
| CODE_COMBINATION_ID | ReceiptAssociatedCodeCombinationId | — |
| CODE_COMBINATION_ID | ReceiptCodeCombinationId | — |
| CODE_COMBINATION_ID | ReceiptLastCodeCombinationId | — |
| CODE_COMBINATION_ID | ReceiptReverseCodeCombinationId | — |
| CODE_COMBINATION_ID | ReceiptSchedCodeCombinationId | — |
| COLLECTOR_ID | ReceiptAssociatedCollectorId | — |
| COLLECTOR_ID | ReceiptCollectorId | — |
| COLLECTOR_ID | ReceiptLastCollectorId | — |
| COLLECTOR_ID | ReceiptReverseCollectorId | — |
| COLLECTOR_ID | ReceiptSchedCollectorId | — |
| COMMENTS | ReceiptAssociatedComments | — |
| COMMENTS | ReceiptComments | — |
| COMMENTS | ReceiptLastComments | — |
| COMMENTS | ReceiptReverseComments | — |
| COMMENTS | ReceiptSchedComments | — |
| CONFIRMED_FLAG | ReceiptAssociatedConfirmedFlag | — |
| CONFIRMED_FLAG | ReceiptConfirmedFlag | — |
| CONFIRMED_FLAG | ReceiptLastConfirmedFlag | — |
| CONFIRMED_FLAG | ReceiptReverseConfirmedFlag | — |
| CONFIRMED_FLAG | ReceiptSchedConfirmedFlag | — |
| CREATED_BY | ReceiptAssociatedCreatedBy | — |
| CREATED_BY | ReceiptCreatedBy | — |
| CREATED_BY | ReceiptLastCreatedBy | — |
| CREATED_BY | ReceiptReverseCreatedBy | — |
| CREATED_BY | ReceiptSchedCreatedBy | — |
| CREATION_DATE | ReceiptAssociatedCreationDate | — |
| CREATION_DATE | ReceiptCreationDate | — |
| CREATION_DATE | ReceiptLastCreationDate | — |
| CREATION_DATE | ReceiptReverseCreationDate | — |
| CREATION_DATE | ReceiptSchedCreationDate | — |
| CURRENCY_CODE | ReceiptAssociatedCurrencyCode | — |
| CURRENCY_CODE | ReceiptCurrencyCode | ✅ |
| CURRENCY_CODE | ReceiptLastCurrencyCode | — |
| CURRENCY_CODE | ReceiptReverseCurrencyCode | — |
| CURRENCY_CODE | ReceiptSchedCurrencyCode | — |
| CUSTOMER_BANK_ACCOUNT_ID | ReceiptAssociatedCustomerBankAccountId | — |
| CUSTOMER_BANK_ACCOUNT_ID | ReceiptCustomerBankAccountId | — |
| CUSTOMER_BANK_ACCOUNT_ID | ReceiptLastCustomerBankAccountId | — |
| CUSTOMER_BANK_ACCOUNT_ID | ReceiptReverseCustomerBankAccountId | — |
| CUSTOMER_BANK_ACCOUNT_ID | ReceiptSchedCustomerBankAccountId | — |
| CUSTOMER_BANK_BRANCH_ID | ReceiptAssociatedCustomerBankBranchId | — |
| CUSTOMER_BANK_BRANCH_ID | ReceiptCustomerBankBranchId | — |
| CUSTOMER_BANK_BRANCH_ID | ReceiptLastCustomerBankBranchId | — |
| CUSTOMER_BANK_BRANCH_ID | ReceiptReverseCustomerBankBranchId | — |
| CUSTOMER_BANK_BRANCH_ID | ReceiptSchedCustomerBankBranchId | — |
| CUSTOMER_RECEIPT_REFERENCE | ReceiptAssociatedCustomerReceiptReference | — |
| CUSTOMER_RECEIPT_REFERENCE | ReceiptCustomerReceiptReference | — |
| CUSTOMER_RECEIPT_REFERENCE | ReceiptLastCustomerReceiptReference | — |
| CUSTOMER_RECEIPT_REFERENCE | ReceiptReverseCustomerReceiptReference | — |
| CUSTOMER_RECEIPT_REFERENCE | ReceiptSchedCustomerReceiptReference | — |
| CUSTOMER_SITE_USE_ID | ReceiptAssociatedCustomerSiteUseId | — |
| CUSTOMER_SITE_USE_ID | ReceiptCustomerSiteUseId | ✅ |
| CUSTOMER_SITE_USE_ID | ReceiptLastCustomerSiteUseId | — |
| CUSTOMER_SITE_USE_ID | ReceiptReverseCustomerSiteUseId | — |
| CUSTOMER_SITE_USE_ID | ReceiptSchedCustomerSiteUseId | — |
| DEPOSIT_DATE | ReceiptAssociatedDepositDate | — |
| DEPOSIT_DATE | ReceiptDepositDate | — |
| DEPOSIT_DATE | ReceiptLastDepositDate | — |
| DEPOSIT_DATE | ReceiptReverseDepositDate | — |
| DEPOSIT_DATE | ReceiptSchedDepositDate | — |
| DISTRIBUTION_SET_ID | ReceiptAssociatedDistributionSetId | — |
| DISTRIBUTION_SET_ID | ReceiptDistributionSetId | — |
| DISTRIBUTION_SET_ID | ReceiptLastDistributionSetId | — |
| DISTRIBUTION_SET_ID | ReceiptReverseDistributionSetId | — |
| DISTRIBUTION_SET_ID | ReceiptSchedDistributionSetId | — |
| DOC_SEQUENCE_ID | ReceiptAssociatedDocSequenceId | — |
| DOC_SEQUENCE_ID | ReceiptDocSequenceId | — |
| DOC_SEQUENCE_ID | ReceiptLastDocSequenceId | — |
| DOC_SEQUENCE_ID | ReceiptReverseDocSequenceId | — |
| DOC_SEQUENCE_ID | ReceiptSchedDocSequenceId | — |
| DOC_SEQUENCE_VALUE | ReceiptAssociatedDocSequenceValue | — |
| DOC_SEQUENCE_VALUE | ReceiptDocSequenceValue | — |
| DOC_SEQUENCE_VALUE | ReceiptLastDocSequenceValue | — |
| DOC_SEQUENCE_VALUE | ReceiptReverseDocSequenceValue | — |
| DOC_SEQUENCE_VALUE | ReceiptSchedDocSequenceValue | — |
| EXCHANGE_DATE | ReceiptAssociatedExchangeDate | — |
| EXCHANGE_DATE | ReceiptExchangeDate | — |
| EXCHANGE_DATE | ReceiptLastExchangeDate | — |
| EXCHANGE_DATE | ReceiptReverseExchangeDate | — |
| EXCHANGE_DATE | ReceiptSchedExchangeDate | — |
| EXCHANGE_RATE | ReceiptAssociatedExchangeRate | — |
| EXCHANGE_RATE | ReceiptExchangeRate | — |
| EXCHANGE_RATE | ReceiptLastExchangeRate | — |
| EXCHANGE_RATE | ReceiptReverseExchangeRate | — |
| EXCHANGE_RATE | ReceiptSchedExchangeRate | — |
| EXCHANGE_RATE_TYPE | ReceiptAssociatedExchangeRateType | — |
| EXCHANGE_RATE_TYPE | ReceiptExchangeRateType | — |
| EXCHANGE_RATE_TYPE | ReceiptLastExchangeRateType | — |
| EXCHANGE_RATE_TYPE | ReceiptReverseExchangeRateType | — |
| EXCHANGE_RATE_TYPE | ReceiptSchedExchangeRateType | — |
| FACTOR_DISCOUNT_AMOUNT | ReceiptAssociatedFactorDiscountAmount | — |
| FACTOR_DISCOUNT_AMOUNT | ReceiptFactorDiscountAmount | — |
| FACTOR_DISCOUNT_AMOUNT | ReceiptLastFactorDiscountAmount | — |
| FACTOR_DISCOUNT_AMOUNT | ReceiptReverseFactorDiscountAmount | — |
| FACTOR_DISCOUNT_AMOUNT | ReceiptSchedFactorDiscountAmount | — |
| ISSUE_DATE | ReceiptAssociatedIssueDate | — |
| ISSUE_DATE | ReceiptIssueDate | — |
| ISSUE_DATE | ReceiptLastIssueDate | — |
| ISSUE_DATE | ReceiptReverseIssueDate | — |
| ISSUE_DATE | ReceiptSchedIssueDate | — |
| ISSUER_BANK_BRANCH_ID | ReceiptAssociatedIssuerBankBranchId | — |
| ISSUER_BANK_BRANCH_ID | ReceiptIssuerBankBranchId | — |
| ISSUER_BANK_BRANCH_ID | ReceiptLastIssuerBankBranchId | — |
| ISSUER_BANK_BRANCH_ID | ReceiptReverseIssuerBankBranchId | — |
| ISSUER_BANK_BRANCH_ID | ReceiptSchedIssuerBankBranchId | — |
| ISSUER_NAME | ReceiptAssociatedIssuerName | — |
| ISSUER_NAME | ReceiptIssuerName | — |
| ISSUER_NAME | ReceiptLastIssuerName | — |
| ISSUER_NAME | ReceiptReverseIssuerName | — |
| ISSUER_NAME | ReceiptSchedIssuerName | — |
| LAST_UPDATE_DATE | ReceiptAssociatedLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ReceiptLastLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ReceiptLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ReceiptReverseLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ReceiptSchedLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ReceiptAssociatedLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ReceiptLastLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ReceiptLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ReceiptReverseLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ReceiptSchedLastUpdateLogin | — |
| LAST_UPDATED_BY | ReceiptAssociatedLastUpdatedBy | — |
| LAST_UPDATED_BY | ReceiptLastLastUpdatedBy | — |
| LAST_UPDATED_BY | ReceiptLastUpdatedBy | — |
| LAST_UPDATED_BY | ReceiptReverseLastUpdatedBy | — |
| LAST_UPDATED_BY | ReceiptSchedLastUpdatedBy | — |
| LEGAL_ENTITY_ID | ReceiptAssociatedLegalEntityId | — |
| LEGAL_ENTITY_ID | ReceiptLastLegalEntityId | — |
| LEGAL_ENTITY_ID | ReceiptLegalEntityId | ✅ |
| LEGAL_ENTITY_ID | ReceiptReverseLegalEntityId | — |
| LEGAL_ENTITY_ID | ReceiptSchedLegalEntityId | — |
| LOGICAL_GROUP_REFERENCE | ReceiptAssociatedLogicalGroupReference | — |
| LOGICAL_GROUP_REFERENCE | ReceiptLastLogicalGroupReference | — |
| LOGICAL_GROUP_REFERENCE | ReceiptLogicalGroupReference | — |
| LOGICAL_GROUP_REFERENCE | ReceiptReverseLogicalGroupReference | — |
| LOGICAL_GROUP_REFERENCE | ReceiptSchedLogicalGroupReference | — |
| MISC_PAYMENT_SOURCE | ReceiptAssociatedMiscPaymentSource | — |
| MISC_PAYMENT_SOURCE | ReceiptLastMiscPaymentSource | — |
| MISC_PAYMENT_SOURCE | ReceiptMiscPaymentSource | — |
| MISC_PAYMENT_SOURCE | ReceiptReverseMiscPaymentSource | — |
| MISC_PAYMENT_SOURCE | ReceiptSchedMiscPaymentSource | — |
| OBJECT_VERSION_NUMBER | ReceiptAssociatedObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ReceiptLastObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ReceiptObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ReceiptReverseObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ReceiptSchedObjectVersionNumber | — |
| OLD_CUSTOMER_BANK_ACCOUNT_ID | ReceiptAssociatedOldCustomerBankAccountId | — |
| OLD_CUSTOMER_BANK_ACCOUNT_ID | ReceiptLastOldCustomerBankAccountId | — |
| OLD_CUSTOMER_BANK_ACCOUNT_ID | ReceiptOldCustomerBankAccountId | — |
| OLD_CUSTOMER_BANK_ACCOUNT_ID | ReceiptReverseOldCustomerBankAccountId | — |
| OLD_CUSTOMER_BANK_ACCOUNT_ID | ReceiptSchedOldCustomerBankAccountId | — |
| OLD_CUSTOMER_BANK_BRANCH_ID | ReceiptAssociatedOldCustomerBankBranchId | — |
| OLD_CUSTOMER_BANK_BRANCH_ID | ReceiptLastOldCustomerBankBranchId | — |
| OLD_CUSTOMER_BANK_BRANCH_ID | ReceiptOldCustomerBankBranchId | — |
| OLD_CUSTOMER_BANK_BRANCH_ID | ReceiptReverseOldCustomerBankBranchId | — |
| OLD_CUSTOMER_BANK_BRANCH_ID | ReceiptSchedOldCustomerBankBranchId | — |
| OLD_ISSUER_BANK_BRANCH_ID | ReceiptAssociatedOldIssuerBankBranchId | — |
| OLD_ISSUER_BANK_BRANCH_ID | ReceiptLastOldIssuerBankBranchId | — |
| OLD_ISSUER_BANK_BRANCH_ID | ReceiptOldIssuerBankBranchId | — |
| OLD_ISSUER_BANK_BRANCH_ID | ReceiptReverseOldIssuerBankBranchId | — |
| OLD_ISSUER_BANK_BRANCH_ID | ReceiptSchedOldIssuerBankBranchId | — |
| ORG_ID | ReceiptAssociatedOrgId | — |
| ORG_ID | ReceiptLastOrgId | — |
| ORG_ID | ReceiptOrgId | ✅ |
| ORG_ID | ReceiptReverseOrgId | — |
| ORG_ID | ReceiptSchedOrgId | — |
| OVERRIDE_REMIT_ACCOUNT_FLAG | ReceiptAssociatedOverrideRemitAccountFlag | — |
| OVERRIDE_REMIT_ACCOUNT_FLAG | ReceiptLastOverrideRemitAccountFlag | — |
| OVERRIDE_REMIT_ACCOUNT_FLAG | ReceiptOverrideRemitAccountFlag | — |
| OVERRIDE_REMIT_ACCOUNT_FLAG | ReceiptReverseOverrideRemitAccountFlag | — |
| OVERRIDE_REMIT_ACCOUNT_FLAG | ReceiptSchedOverrideRemitAccountFlag | — |
| PAY_FROM_CUSTOMER | ReceiptAssociatedPayFromCustomer | — |
| PAY_FROM_CUSTOMER | ReceiptLastPayFromCustomer | — |
| PAY_FROM_CUSTOMER | ReceiptPayFromCustomer | ✅ |
| PAY_FROM_CUSTOMER | ReceiptReversePayFromCustomer | — |
| PAY_FROM_CUSTOMER | ReceiptSchedPayFromCustomer | — |
| PAYMENT_SERVER_ORDER_NUM | ReceiptAssociatedPaymentServerOrderNum | — |
| PAYMENT_SERVER_ORDER_NUM | ReceiptLastPaymentServerOrderNum | — |
| PAYMENT_SERVER_ORDER_NUM | ReceiptPaymentServerOrderNum | — |
| PAYMENT_SERVER_ORDER_NUM | ReceiptReversePaymentServerOrderNum | — |
| PAYMENT_SERVER_ORDER_NUM | ReceiptSchedPaymentServerOrderNum | — |
| PAYMENT_TRXN_EXTENSION_ID | ReceiptAssociatedPaymentTrxnExtensionId | — |
| PAYMENT_TRXN_EXTENSION_ID | ReceiptLastPaymentTrxnExtensionId | — |
| PAYMENT_TRXN_EXTENSION_ID | ReceiptPaymentTrxnExtensionId | — |
| PAYMENT_TRXN_EXTENSION_ID | ReceiptReversePaymentTrxnExtensionId | — |
| PAYMENT_TRXN_EXTENSION_ID | ReceiptSchedPaymentTrxnExtensionId | — |
| POSTMARK_DATE | ReceiptAssociatedPostmarkDate | — |
| POSTMARK_DATE | ReceiptLastPostmarkDate | — |
| POSTMARK_DATE | ReceiptPostmarkDate | — |
| POSTMARK_DATE | ReceiptReversePostmarkDate | — |
| POSTMARK_DATE | ReceiptSchedPostmarkDate | — |
| PROGRAM_APPLICATION_ID | ReceiptAssociatedProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | ReceiptLastProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | ReceiptProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | ReceiptReverseProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | ReceiptSchedProgramApplicationId | — |
| PROGRAM_ID | ReceiptAssociatedProgramId | — |
| PROGRAM_ID | ReceiptLastProgramId | — |
| PROGRAM_ID | ReceiptProgramId | — |
| PROGRAM_ID | ReceiptReverseProgramId | — |
| PROGRAM_ID | ReceiptSchedProgramId | — |
| PROGRAM_UPDATE_DATE | ReceiptAssociatedProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | ReceiptLastProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | ReceiptProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | ReceiptReverseProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | ReceiptSchedProgramUpdateDate | — |
| PROMISE_SOURCE | ReceiptAssociatedPromiseSource | — |
| PROMISE_SOURCE | ReceiptLastPromiseSource | — |
| PROMISE_SOURCE | ReceiptPromiseSource | — |
| PROMISE_SOURCE | ReceiptReversePromiseSource | — |
| PROMISE_SOURCE | ReceiptSchedPromiseSource | — |
| REC_VERSION_NUMBER | ReceiptAssociatedRecVersionNumber | — |
| REC_VERSION_NUMBER | ReceiptLastRecVersionNumber | — |
| REC_VERSION_NUMBER | ReceiptRecVersionNumber | — |
| REC_VERSION_NUMBER | ReceiptReverseRecVersionNumber | — |
| REC_VERSION_NUMBER | ReceiptSchedRecVersionNumber | — |
| RECEIPT_BATCH_ID | ReceiptAssociatedReceiptBatchId | — |
| RECEIPT_BATCH_ID | ReceiptLastReceiptBatchId | — |
| RECEIPT_BATCH_ID | ReceiptReceiptBatchId | — |
| RECEIPT_BATCH_ID | ReceiptReverseReceiptBatchId | — |
| RECEIPT_BATCH_ID | ReceiptSchedReceiptBatchId | — |
| RECEIPT_DATE | ReceiptAssociatedReceiptDate | — |
| RECEIPT_DATE | ReceiptLastReceiptDate | — |
| RECEIPT_DATE | ReceiptReceiptDate | ✅ |
| RECEIPT_DATE | ReceiptReverseReceiptDate | — |
| RECEIPT_DATE | ReceiptSchedReceiptDate | — |
| RECEIPT_METHOD_ID | ReceiptAssociatedReceiptMethodId | — |
| RECEIPT_METHOD_ID | ReceiptLastReceiptMethodId | — |
| RECEIPT_METHOD_ID | ReceiptReceiptMethodId | ✅ |
| RECEIPT_METHOD_ID | ReceiptReverseReceiptMethodId | — |
| RECEIPT_METHOD_ID | ReceiptSchedReceiptMethodId | — |
| RECEIPT_NUMBER | ReceiptAssociatedReceiptNumber | — |
| RECEIPT_NUMBER | ReceiptLastReceiptNumber | — |
| RECEIPT_NUMBER | ReceiptReceiptNumber | ✅ |
| RECEIPT_NUMBER | ReceiptReverseReceiptNumber | — |
| RECEIPT_NUMBER | ReceiptSchedReceiptNumber | — |
| RECEIVABLES_TRX_ID | ReceiptAssociatedReceivablesTrxId | — |
| RECEIVABLES_TRX_ID | ReceiptLastReceivablesTrxId | — |
| RECEIVABLES_TRX_ID | ReceiptReceivablesTrxId | — |
| RECEIVABLES_TRX_ID | ReceiptReverseReceivablesTrxId | — |
| RECEIVABLES_TRX_ID | ReceiptSchedReceivablesTrxId | — |
| RECON_FLAG | ReceiptAssociatedReconFlag | — |
| RECON_FLAG | ReceiptLastReconFlag | — |
| RECON_FLAG | ReceiptReconFlag | — |
| RECON_FLAG | ReceiptReverseReconFlag | — |
| RECON_FLAG | ReceiptSchedReconFlag | — |
| REFERENCE_ID | ReceiptAssociatedReferenceId | — |
| REFERENCE_ID | ReceiptLastReferenceId | — |
| REFERENCE_ID | ReceiptReferenceId | — |
| REFERENCE_ID | ReceiptReverseReferenceId | — |
| REFERENCE_ID | ReceiptSchedReferenceId | — |
| REFERENCE_TYPE | ReceiptAssociatedReferenceType | — |
| REFERENCE_TYPE | ReceiptLastReferenceType | — |
| REFERENCE_TYPE | ReceiptReferenceType | — |
| REFERENCE_TYPE | ReceiptReverseReferenceType | — |
| REFERENCE_TYPE | ReceiptSchedReferenceType | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptAssociatedRemitBankAcctUseId | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptLastRemitBankAcctUseId | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptRemitBankAcctUseId | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptReverseRemitBankAcctUseId | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptSchedRemitBankAcctUseId | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptAssociatedRemittanceBankAccountId | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptLastRemittanceBankAccountId | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptRemittanceBankAccountId | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptReverseRemittanceBankAccountId | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptSchedRemittanceBankAccountId | — |
| REMITTANCE_BATCH_ID | ReceiptAssociatedRemittanceBatchId | — |
| REMITTANCE_BATCH_ID | ReceiptLastRemittanceBatchId | — |
| REMITTANCE_BATCH_ID | ReceiptRemittanceBatchId | — |
| REMITTANCE_BATCH_ID | ReceiptReverseRemittanceBatchId | — |
| REMITTANCE_BATCH_ID | ReceiptSchedRemittanceBatchId | — |
| REQUEST_ID | ReceiptAssociatedRequestId | — |
| REQUEST_ID | ReceiptLastRequestId | — |
| REQUEST_ID | ReceiptRequestId | — |
| REQUEST_ID | ReceiptReverseRequestId | — |
| REQUEST_ID | ReceiptSchedRequestId | — |
| RESOURCE_ID | ReceiptAssociatedResourceId | — |
| RESOURCE_ID | ReceiptLastResourceId | — |
| RESOURCE_ID | ReceiptResourceId | — |
| RESOURCE_ID | ReceiptReverseResourceId | — |
| RESOURCE_ID | ReceiptSchedResourceId | — |
| REVERSAL_CATEGORY | ReceiptAssociatedReversalCategory | — |
| REVERSAL_CATEGORY | ReceiptLastReversalCategory | — |
| REVERSAL_CATEGORY | ReceiptReversalCategory | — |
| REVERSAL_CATEGORY | ReceiptReverseReversalCategory | — |
| REVERSAL_CATEGORY | ReceiptSchedReversalCategory | — |
| REVERSAL_COMMENTS | ReceiptAssociatedReversalComments | — |
| REVERSAL_COMMENTS | ReceiptLastReversalComments | — |
| REVERSAL_COMMENTS | ReceiptReversalComments | — |
| REVERSAL_COMMENTS | ReceiptReverseReversalComments | — |
| REVERSAL_COMMENTS | ReceiptSchedReversalComments | — |
| REVERSAL_DATE | ReceiptAssociatedReversalDate | — |
| REVERSAL_DATE | ReceiptLastReversalDate | — |
| REVERSAL_DATE | ReceiptReversalDate | — |
| REVERSAL_DATE | ReceiptReverseReversalDate | — |
| REVERSAL_DATE | ReceiptSchedReversalDate | — |
| REVERSAL_REASON_CODE | ReceiptAssociatedReversalReasonCode | — |
| REVERSAL_REASON_CODE | ReceiptLastReversalReasonCode | — |
| REVERSAL_REASON_CODE | ReceiptReversalReasonCode | — |
| REVERSAL_REASON_CODE | ReceiptReverseReversalReasonCode | — |
| REVERSAL_REASON_CODE | ReceiptSchedReversalReasonCode | — |
| SELECTED_FOR_FACTORING_FLAG | ReceiptAssociatedSelectedForFactoringFlag | — |
| SELECTED_FOR_FACTORING_FLAG | ReceiptLastSelectedForFactoringFlag | — |
| SELECTED_FOR_FACTORING_FLAG | ReceiptReverseSelectedForFactoringFlag | — |
| SELECTED_FOR_FACTORING_FLAG | ReceiptSchedSelectedForFactoringFlag | — |
| SELECTED_FOR_FACTORING_FLAG | ReceiptSelectedForFactoringFlag | — |
| SELECTED_REMITTANCE_BATCH_ID | ReceiptAssociatedSelectedRemittanceBatchId | — |
| SELECTED_REMITTANCE_BATCH_ID | ReceiptLastSelectedRemittanceBatchId | — |
| SELECTED_REMITTANCE_BATCH_ID | ReceiptReverseSelectedRemittanceBatchId | — |
| SELECTED_REMITTANCE_BATCH_ID | ReceiptSchedSelectedRemittanceBatchId | — |
| SELECTED_REMITTANCE_BATCH_ID | ReceiptSelectedRemittanceBatchId | — |
| SET_OF_BOOKS_ID | ReceiptAssociatedSetOfBooksId | — |
| SET_OF_BOOKS_ID | ReceiptLastSetOfBooksId | — |
| SET_OF_BOOKS_ID | ReceiptReverseSetOfBooksId | — |
| SET_OF_BOOKS_ID | ReceiptSchedSetOfBooksId | — |
| SET_OF_BOOKS_ID | ReceiptSetOfBooksId | — |
| STATUS | ReceiptAssociatedStatus | — |
| STATUS | ReceiptLastStatus | — |
| STATUS | ReceiptReverseStatus | — |
| STATUS | ReceiptSchedStatus | — |
| STATUS | ReceiptStatus | — |
| TAX_RATE | ReceiptAssociatedTaxRate | — |
| TAX_RATE | ReceiptLastTaxRate | — |
| TAX_RATE | ReceiptReverseTaxRate | — |
| TAX_RATE | ReceiptSchedTaxRate | — |
| TAX_RATE | ReceiptTaxRate | — |
| TYPE | ReceiptAssociatedType | — |
| TYPE | ReceiptLastType | — |
| TYPE | ReceiptReverseType | — |
| TYPE | ReceiptSchedType | — |
| TYPE | ReceiptType | — |
| UNIQUE_REFERENCE | ReceiptAssociatedUniqueReference | — |
| UNIQUE_REFERENCE | ReceiptLastUniqueReference | — |
| UNIQUE_REFERENCE | ReceiptReverseUniqueReference | — |
| UNIQUE_REFERENCE | ReceiptSchedUniqueReference | — |
| UNIQUE_REFERENCE | ReceiptUniqueReference | — |
| USSGL_TRANSACTION_CODE | ReceiptAssociatedUssglTransactionCode | — |
| USSGL_TRANSACTION_CODE | ReceiptLastUssglTransactionCode | — |
| USSGL_TRANSACTION_CODE | ReceiptReverseUssglTransactionCode | — |
| USSGL_TRANSACTION_CODE | ReceiptSchedUssglTransactionCode | — |
| USSGL_TRANSACTION_CODE | ReceiptUssglTransactionCode | — |
| USSGL_TRANSACTION_CODE_CONTEXT | ReceiptAssociatedUssglTransactionCodeContext | — |
| USSGL_TRANSACTION_CODE_CONTEXT | ReceiptLastUssglTransactionCodeContext | — |
| USSGL_TRANSACTION_CODE_CONTEXT | ReceiptReverseUssglTransactionCodeContext | — |
| USSGL_TRANSACTION_CODE_CONTEXT | ReceiptSchedUssglTransactionCodeContext | — |
| USSGL_TRANSACTION_CODE_CONTEXT | ReceiptUssglTransactionCodeContext | — |
| VAT_TAX_ID | ReceiptAssociatedVatTaxId | — |
| VAT_TAX_ID | ReceiptLastVatTaxId | — |
| VAT_TAX_ID | ReceiptReverseVatTaxId | — |
| VAT_TAX_ID | ReceiptSchedVatTaxId | — |
| VAT_TAX_ID | ReceiptVatTaxId | — |

### [[receiptapplicationdistributionvc|ReceiptApplicationDistributionVC]] (AR · BICC: 29/415)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTUAL_VALUE_DATE | ReceiptActualValueDate | ✅ |
| ACTUAL_VALUE_DATE | ReceiptAssociatedActualValueDate | — |
| ACTUAL_VALUE_DATE | ReceiptLastActualValueDate | — |
| ACTUAL_VALUE_DATE | ReceiptReverseActualValueDate | — |
| ACTUAL_VALUE_DATE | ReceiptSchedActualValueDate | — |
| ADDRESS_VERIFICATION_CODE | ReceiptAddressVerificationCode | ✅ |
| ADDRESS_VERIFICATION_CODE | ReceiptAssociatedAddressVerificationCode | — |
| ADDRESS_VERIFICATION_CODE | ReceiptLastAddressVerificationCode | — |
| ADDRESS_VERIFICATION_CODE | ReceiptReverseAddressVerificationCode | — |
| ADDRESS_VERIFICATION_CODE | ReceiptSchedAddressVerificationCode | — |
| AMOUNT | ReceiptAmount | — |
| AMOUNT | ReceiptAssociatedAmount | — |
| AMOUNT | ReceiptLastAmount | — |
| AMOUNT | ReceiptReverseAmount | — |
| AMOUNT | ReceiptSchedAmount | — |
| ANTICIPATED_CLEARING_DATE | ReceiptAnticipatedClearingDate | ✅ |
| ANTICIPATED_CLEARING_DATE | ReceiptAssociatedAnticipatedClearingDate | — |
| ANTICIPATED_CLEARING_DATE | ReceiptLastAnticipatedClearingDate | — |
| ANTICIPATED_CLEARING_DATE | ReceiptReverseAnticipatedClearingDate | — |
| ANTICIPATED_CLEARING_DATE | ReceiptSchedAnticipatedClearingDate | — |
| APPLICATION_NOTES | ReceiptApplicationNotes | — |
| APPLICATION_NOTES | ReceiptAssociatedApplicationNotes | — |
| APPLICATION_NOTES | ReceiptLastApplicationNotes | — |
| APPLICATION_NOTES | ReceiptReverseApplicationNotes | — |
| APPLICATION_NOTES | ReceiptSchedApplicationNotes | — |
| APPROVAL_CODE | ReceiptApprovalCode | — |
| APPROVAL_CODE | ReceiptAssociatedApprovalCode | — |
| APPROVAL_CODE | ReceiptLastApprovalCode | — |
| APPROVAL_CODE | ReceiptReverseApprovalCode | — |
| APPROVAL_CODE | ReceiptSchedApprovalCode | — |
| AUTOAPPLY_FLAG | ReceiptAssociatedAutoapplyFlag | — |
| AUTOAPPLY_FLAG | ReceiptAutoapplyFlag | — |
| AUTOAPPLY_FLAG | ReceiptLastAutoapplyFlag | — |
| AUTOAPPLY_FLAG | ReceiptReverseAutoapplyFlag | — |
| AUTOAPPLY_FLAG | ReceiptSchedAutoapplyFlag | — |
| AUTOMATCH_REQUEST_ID | ReceiptAssociatedAutomatchRequestId | — |
| AUTOMATCH_REQUEST_ID | ReceiptAutomatchRequestId | — |
| AUTOMATCH_REQUEST_ID | ReceiptLastAutomatchRequestId | — |
| AUTOMATCH_REQUEST_ID | ReceiptReverseAutomatchRequestId | — |
| AUTOMATCH_REQUEST_ID | ReceiptSchedAutomatchRequestId | — |
| AX_ACCOUNTED_FLAG | ReceiptAssociatedAxAccountedFlag | — |
| AX_ACCOUNTED_FLAG | ReceiptAxAccountedFlag | — |
| AX_ACCOUNTED_FLAG | ReceiptLastAxAccountedFlag | — |
| AX_ACCOUNTED_FLAG | ReceiptReverseAxAccountedFlag | — |
| AX_ACCOUNTED_FLAG | ReceiptSchedAxAccountedFlag | — |
| CASH_RECEIPT_ID | ReceiptAssociatedCashReceiptId | — |
| CASH_RECEIPT_ID | ReceiptCashReceiptId | — |
| CASH_RECEIPT_ID | ReceiptLastCashReceiptId | — |
| CASH_RECEIPT_ID | ReceiptReverseCashReceiptId | — |
| CASH_RECEIPT_ID | ReceiptSchedCashReceiptId | — |
| CC_ERROR_CODE | ReceiptAssociatedCcErrorCode | — |
| CC_ERROR_CODE | ReceiptCcErrorCode | — |
| CC_ERROR_CODE | ReceiptLastCcErrorCode | — |
| CC_ERROR_CODE | ReceiptReverseCcErrorCode | — |
| CC_ERROR_CODE | ReceiptSchedCcErrorCode | — |
| CC_ERROR_FLAG | ReceiptAssociatedCcErrorFlag | — |
| CC_ERROR_FLAG | ReceiptCcErrorFlag | — |
| CC_ERROR_FLAG | ReceiptLastCcErrorFlag | — |
| CC_ERROR_FLAG | ReceiptReverseCcErrorFlag | — |
| CC_ERROR_FLAG | ReceiptSchedCcErrorFlag | — |
| CC_ERROR_TEXT | ReceiptAssociatedCcErrorText | — |
| CC_ERROR_TEXT | ReceiptCcErrorText | — |
| CC_ERROR_TEXT | ReceiptLastCcErrorText | — |
| CC_ERROR_TEXT | ReceiptReverseCcErrorText | — |
| CC_ERROR_TEXT | ReceiptSchedCcErrorText | — |
| CODE_COMBINATION_ID | ReceiptAssociatedCodeCombinationId | — |
| CODE_COMBINATION_ID | ReceiptCodeCombinationId | — |
| CODE_COMBINATION_ID | ReceiptLastCodeCombinationId | — |
| CODE_COMBINATION_ID | ReceiptReverseCodeCombinationId | — |
| CODE_COMBINATION_ID | ReceiptSchedCodeCombinationId | — |
| COLLECTOR_ID | ReceiptAssociatedCollectorId | — |
| COLLECTOR_ID | ReceiptCollectorId | — |
| COLLECTOR_ID | ReceiptLastCollectorId | — |
| COLLECTOR_ID | ReceiptReverseCollectorId | — |
| COLLECTOR_ID | ReceiptSchedCollectorId | — |
| COMMENTS | ReceiptAssociatedComments | — |
| COMMENTS | ReceiptComments | ✅ |
| COMMENTS | ReceiptLastComments | — |
| COMMENTS | ReceiptReverseComments | — |
| COMMENTS | ReceiptSchedComments | — |
| CONFIRMED_FLAG | ReceiptAssociatedConfirmedFlag | — |
| CONFIRMED_FLAG | ReceiptConfirmedFlag | ✅ |
| CONFIRMED_FLAG | ReceiptLastConfirmedFlag | — |
| CONFIRMED_FLAG | ReceiptReverseConfirmedFlag | — |
| CONFIRMED_FLAG | ReceiptSchedConfirmedFlag | — |
| CREATED_BY | ReceiptAssociatedCreatedBy | — |
| CREATED_BY | ReceiptCreatedBy | ✅ |
| CREATED_BY | ReceiptLastCreatedBy | — |
| CREATED_BY | ReceiptReverseCreatedBy | — |
| CREATED_BY | ReceiptSchedCreatedBy | — |
| CREATION_DATE | ReceiptAssociatedCreationDate | — |
| CREATION_DATE | ReceiptCreationDate | ✅ |
| CREATION_DATE | ReceiptLastCreationDate | — |
| CREATION_DATE | ReceiptReverseCreationDate | — |
| CREATION_DATE | ReceiptSchedCreationDate | — |
| CURRENCY_CODE | ReceiptAssociatedCurrencyCode | — |
| CURRENCY_CODE | ReceiptCurrencyCode | — |
| CURRENCY_CODE | ReceiptLastCurrencyCode | — |
| CURRENCY_CODE | ReceiptReverseCurrencyCode | — |
| CURRENCY_CODE | ReceiptSchedCurrencyCode | — |
| CUSTOMER_BANK_ACCOUNT_ID | ReceiptAssociatedCustomerBankAccountId | — |
| CUSTOMER_BANK_ACCOUNT_ID | ReceiptCustomerBankAccountId | — |
| CUSTOMER_BANK_ACCOUNT_ID | ReceiptLastCustomerBankAccountId | — |
| CUSTOMER_BANK_ACCOUNT_ID | ReceiptReverseCustomerBankAccountId | — |
| CUSTOMER_BANK_ACCOUNT_ID | ReceiptSchedCustomerBankAccountId | — |
| CUSTOMER_BANK_BRANCH_ID | ReceiptAssociatedCustomerBankBranchId | — |
| CUSTOMER_BANK_BRANCH_ID | ReceiptCustomerBankBranchId | — |
| CUSTOMER_BANK_BRANCH_ID | ReceiptLastCustomerBankBranchId | — |
| CUSTOMER_BANK_BRANCH_ID | ReceiptReverseCustomerBankBranchId | — |
| CUSTOMER_BANK_BRANCH_ID | ReceiptSchedCustomerBankBranchId | — |
| CUSTOMER_RECEIPT_REFERENCE | ReceiptAssociatedCustomerReceiptReference | — |
| CUSTOMER_RECEIPT_REFERENCE | ReceiptCustomerReceiptReference | ✅ |
| CUSTOMER_RECEIPT_REFERENCE | ReceiptLastCustomerReceiptReference | — |
| CUSTOMER_RECEIPT_REFERENCE | ReceiptReverseCustomerReceiptReference | — |
| CUSTOMER_RECEIPT_REFERENCE | ReceiptSchedCustomerReceiptReference | — |
| CUSTOMER_SITE_USE_ID | ReceiptAssociatedCustomerSiteUseId | — |
| CUSTOMER_SITE_USE_ID | ReceiptCustomerSiteUseId | — |
| CUSTOMER_SITE_USE_ID | ReceiptLastCustomerSiteUseId | — |
| CUSTOMER_SITE_USE_ID | ReceiptReverseCustomerSiteUseId | — |
| CUSTOMER_SITE_USE_ID | ReceiptSchedCustomerSiteUseId | — |
| DEPOSIT_DATE | ReceiptAssociatedDepositDate | — |
| DEPOSIT_DATE | ReceiptDepositDate | ✅ |
| DEPOSIT_DATE | ReceiptLastDepositDate | — |
| DEPOSIT_DATE | ReceiptReverseDepositDate | — |
| DEPOSIT_DATE | ReceiptSchedDepositDate | — |
| DISTRIBUTION_SET_ID | ReceiptAssociatedDistributionSetId | — |
| DISTRIBUTION_SET_ID | ReceiptDistributionSetId | — |
| DISTRIBUTION_SET_ID | ReceiptLastDistributionSetId | — |
| DISTRIBUTION_SET_ID | ReceiptReverseDistributionSetId | — |
| DISTRIBUTION_SET_ID | ReceiptSchedDistributionSetId | — |
| DOC_SEQUENCE_ID | ReceiptAssociatedDocSequenceId | — |
| DOC_SEQUENCE_ID | ReceiptDocSequenceId | — |
| DOC_SEQUENCE_ID | ReceiptLastDocSequenceId | — |
| DOC_SEQUENCE_ID | ReceiptReverseDocSequenceId | — |
| DOC_SEQUENCE_ID | ReceiptSchedDocSequenceId | — |
| DOC_SEQUENCE_VALUE | ReceiptAssociatedDocSequenceValue | — |
| DOC_SEQUENCE_VALUE | ReceiptDocSequenceValue | ✅ |
| DOC_SEQUENCE_VALUE | ReceiptLastDocSequenceValue | — |
| DOC_SEQUENCE_VALUE | ReceiptReverseDocSequenceValue | — |
| DOC_SEQUENCE_VALUE | ReceiptSchedDocSequenceValue | — |
| EXCHANGE_DATE | ReceiptAssociatedExchangeDate | — |
| EXCHANGE_DATE | ReceiptExchangeDate | ✅ |
| EXCHANGE_DATE | ReceiptLastExchangeDate | — |
| EXCHANGE_DATE | ReceiptReverseExchangeDate | — |
| EXCHANGE_DATE | ReceiptSchedExchangeDate | — |
| EXCHANGE_RATE | ReceiptAssociatedExchangeRate | — |
| EXCHANGE_RATE | ReceiptExchangeRate | ✅ |
| EXCHANGE_RATE | ReceiptLastExchangeRate | — |
| EXCHANGE_RATE | ReceiptReverseExchangeRate | — |
| EXCHANGE_RATE | ReceiptSchedExchangeRate | — |
| EXCHANGE_RATE_TYPE | ReceiptAssociatedExchangeRateType | — |
| EXCHANGE_RATE_TYPE | ReceiptExchangeRateType | ✅ |
| EXCHANGE_RATE_TYPE | ReceiptLastExchangeRateType | — |
| EXCHANGE_RATE_TYPE | ReceiptReverseExchangeRateType | — |
| EXCHANGE_RATE_TYPE | ReceiptSchedExchangeRateType | — |
| FACTOR_DISCOUNT_AMOUNT | ReceiptAssociatedFactorDiscountAmount | — |
| FACTOR_DISCOUNT_AMOUNT | ReceiptFactorDiscountAmount | — |
| FACTOR_DISCOUNT_AMOUNT | ReceiptLastFactorDiscountAmount | — |
| FACTOR_DISCOUNT_AMOUNT | ReceiptReverseFactorDiscountAmount | — |
| FACTOR_DISCOUNT_AMOUNT | ReceiptSchedFactorDiscountAmount | — |
| ISSUE_DATE | ReceiptAssociatedIssueDate | — |
| ISSUE_DATE | ReceiptIssueDate | — |
| ISSUE_DATE | ReceiptLastIssueDate | — |
| ISSUE_DATE | ReceiptReverseIssueDate | — |
| ISSUE_DATE | ReceiptSchedIssueDate | — |
| ISSUER_BANK_BRANCH_ID | ReceiptAssociatedIssuerBankBranchId | — |
| ISSUER_BANK_BRANCH_ID | ReceiptIssuerBankBranchId | — |
| ISSUER_BANK_BRANCH_ID | ReceiptLastIssuerBankBranchId | — |
| ISSUER_BANK_BRANCH_ID | ReceiptReverseIssuerBankBranchId | — |
| ISSUER_BANK_BRANCH_ID | ReceiptSchedIssuerBankBranchId | — |
| ISSUER_NAME | ReceiptAssociatedIssuerName | — |
| ISSUER_NAME | ReceiptIssuerName | — |
| ISSUER_NAME | ReceiptLastIssuerName | — |
| ISSUER_NAME | ReceiptReverseIssuerName | — |
| ISSUER_NAME | ReceiptSchedIssuerName | — |
| LAST_UPDATE_DATE | ReceiptAssociatedLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ReceiptLastLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ReceiptLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ReceiptReverseLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ReceiptSchedLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ReceiptAssociatedLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ReceiptLastLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ReceiptLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ReceiptReverseLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ReceiptSchedLastUpdateLogin | — |
| LAST_UPDATED_BY | ReceiptAssociatedLastUpdatedBy | — |
| LAST_UPDATED_BY | ReceiptLastLastUpdatedBy | — |
| LAST_UPDATED_BY | ReceiptLastUpdatedBy | ✅ |
| LAST_UPDATED_BY | ReceiptReverseLastUpdatedBy | — |
| LAST_UPDATED_BY | ReceiptSchedLastUpdatedBy | — |
| LEGAL_ENTITY_ID | ReceiptAssociatedLegalEntityId | — |
| LEGAL_ENTITY_ID | ReceiptLastLegalEntityId | — |
| LEGAL_ENTITY_ID | ReceiptLegalEntityId | — |
| LEGAL_ENTITY_ID | ReceiptReverseLegalEntityId | — |
| LEGAL_ENTITY_ID | ReceiptSchedLegalEntityId | — |
| LOGICAL_GROUP_REFERENCE | ReceiptAssociatedLogicalGroupReference | — |
| LOGICAL_GROUP_REFERENCE | ReceiptLastLogicalGroupReference | — |
| LOGICAL_GROUP_REFERENCE | ReceiptLogicalGroupReference | — |
| LOGICAL_GROUP_REFERENCE | ReceiptReverseLogicalGroupReference | — |
| LOGICAL_GROUP_REFERENCE | ReceiptSchedLogicalGroupReference | — |
| MISC_PAYMENT_SOURCE | ReceiptAssociatedMiscPaymentSource | — |
| MISC_PAYMENT_SOURCE | ReceiptLastMiscPaymentSource | — |
| MISC_PAYMENT_SOURCE | ReceiptMiscPaymentSource | ✅ |
| MISC_PAYMENT_SOURCE | ReceiptReverseMiscPaymentSource | — |
| MISC_PAYMENT_SOURCE | ReceiptSchedMiscPaymentSource | — |
| OBJECT_VERSION_NUMBER | ReceiptAssociatedObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ReceiptLastObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ReceiptObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ReceiptReverseObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ReceiptSchedObjectVersionNumber | — |
| OLD_CUSTOMER_BANK_ACCOUNT_ID | ReceiptAssociatedOldCustomerBankAccountId | — |
| OLD_CUSTOMER_BANK_ACCOUNT_ID | ReceiptLastOldCustomerBankAccountId | — |
| OLD_CUSTOMER_BANK_ACCOUNT_ID | ReceiptOldCustomerBankAccountId | — |
| OLD_CUSTOMER_BANK_ACCOUNT_ID | ReceiptReverseOldCustomerBankAccountId | — |
| OLD_CUSTOMER_BANK_ACCOUNT_ID | ReceiptSchedOldCustomerBankAccountId | — |
| OLD_CUSTOMER_BANK_BRANCH_ID | ReceiptAssociatedOldCustomerBankBranchId | — |
| OLD_CUSTOMER_BANK_BRANCH_ID | ReceiptLastOldCustomerBankBranchId | — |
| OLD_CUSTOMER_BANK_BRANCH_ID | ReceiptOldCustomerBankBranchId | — |
| OLD_CUSTOMER_BANK_BRANCH_ID | ReceiptReverseOldCustomerBankBranchId | — |
| OLD_CUSTOMER_BANK_BRANCH_ID | ReceiptSchedOldCustomerBankBranchId | — |
| OLD_ISSUER_BANK_BRANCH_ID | ReceiptAssociatedOldIssuerBankBranchId | — |
| OLD_ISSUER_BANK_BRANCH_ID | ReceiptLastOldIssuerBankBranchId | — |
| OLD_ISSUER_BANK_BRANCH_ID | ReceiptOldIssuerBankBranchId | — |
| OLD_ISSUER_BANK_BRANCH_ID | ReceiptReverseOldIssuerBankBranchId | — |
| OLD_ISSUER_BANK_BRANCH_ID | ReceiptSchedOldIssuerBankBranchId | — |
| ORG_ID | ReceiptAssociatedOrgId | — |
| ORG_ID | ReceiptLastOrgId | — |
| ORG_ID | ReceiptOrgId | — |
| ORG_ID | ReceiptReverseOrgId | — |
| ORG_ID | ReceiptSchedOrgId | — |
| OVERRIDE_REMIT_ACCOUNT_FLAG | ReceiptAssociatedOverrideRemitAccountFlag | — |
| OVERRIDE_REMIT_ACCOUNT_FLAG | ReceiptLastOverrideRemitAccountFlag | — |
| OVERRIDE_REMIT_ACCOUNT_FLAG | ReceiptOverrideRemitAccountFlag | — |
| OVERRIDE_REMIT_ACCOUNT_FLAG | ReceiptReverseOverrideRemitAccountFlag | — |
| OVERRIDE_REMIT_ACCOUNT_FLAG | ReceiptSchedOverrideRemitAccountFlag | — |
| PAY_FROM_CUSTOMER | ReceiptAssociatedPayFromCustomer | — |
| PAY_FROM_CUSTOMER | ReceiptLastPayFromCustomer | — |
| PAY_FROM_CUSTOMER | ReceiptPayFromCustomer | — |
| PAY_FROM_CUSTOMER | ReceiptReversePayFromCustomer | — |
| PAY_FROM_CUSTOMER | ReceiptSchedPayFromCustomer | — |
| PAYMENT_SERVER_ORDER_NUM | ReceiptAssociatedPaymentServerOrderNum | — |
| PAYMENT_SERVER_ORDER_NUM | ReceiptLastPaymentServerOrderNum | — |
| PAYMENT_SERVER_ORDER_NUM | ReceiptPaymentServerOrderNum | — |
| PAYMENT_SERVER_ORDER_NUM | ReceiptReversePaymentServerOrderNum | — |
| PAYMENT_SERVER_ORDER_NUM | ReceiptSchedPaymentServerOrderNum | — |
| PAYMENT_TRXN_EXTENSION_ID | ReceiptAssociatedPaymentTrxnExtensionId | — |
| PAYMENT_TRXN_EXTENSION_ID | ReceiptLastPaymentTrxnExtensionId | — |
| PAYMENT_TRXN_EXTENSION_ID | ReceiptPaymentTrxnExtensionId | — |
| PAYMENT_TRXN_EXTENSION_ID | ReceiptReversePaymentTrxnExtensionId | — |
| PAYMENT_TRXN_EXTENSION_ID | ReceiptSchedPaymentTrxnExtensionId | — |
| POSTMARK_DATE | ReceiptAssociatedPostmarkDate | — |
| POSTMARK_DATE | ReceiptLastPostmarkDate | — |
| POSTMARK_DATE | ReceiptPostmarkDate | ✅ |
| POSTMARK_DATE | ReceiptReversePostmarkDate | — |
| POSTMARK_DATE | ReceiptSchedPostmarkDate | — |
| PROGRAM_APPLICATION_ID | ReceiptAssociatedProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | ReceiptLastProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | ReceiptProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | ReceiptReverseProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | ReceiptSchedProgramApplicationId | — |
| PROGRAM_ID | ReceiptAssociatedProgramId | — |
| PROGRAM_ID | ReceiptLastProgramId | — |
| PROGRAM_ID | ReceiptProgramId | — |
| PROGRAM_ID | ReceiptReverseProgramId | — |
| PROGRAM_ID | ReceiptSchedProgramId | — |
| PROGRAM_UPDATE_DATE | ReceiptAssociatedProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | ReceiptLastProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | ReceiptProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | ReceiptReverseProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | ReceiptSchedProgramUpdateDate | — |
| PROMISE_SOURCE | ReceiptAssociatedPromiseSource | — |
| PROMISE_SOURCE | ReceiptLastPromiseSource | — |
| PROMISE_SOURCE | ReceiptPromiseSource | — |
| PROMISE_SOURCE | ReceiptReversePromiseSource | — |
| PROMISE_SOURCE | ReceiptSchedPromiseSource | — |
| REC_VERSION_NUMBER | ReceiptAssociatedRecVersionNumber | — |
| REC_VERSION_NUMBER | ReceiptLastRecVersionNumber | — |
| REC_VERSION_NUMBER | ReceiptRecVersionNumber | — |
| REC_VERSION_NUMBER | ReceiptReverseRecVersionNumber | — |
| REC_VERSION_NUMBER | ReceiptSchedRecVersionNumber | — |
| RECEIPT_BATCH_ID | ReceiptAssociatedReceiptBatchId | — |
| RECEIPT_BATCH_ID | ReceiptLastReceiptBatchId | — |
| RECEIPT_BATCH_ID | ReceiptReceiptBatchId | — |
| RECEIPT_BATCH_ID | ReceiptReverseReceiptBatchId | — |
| RECEIPT_BATCH_ID | ReceiptSchedReceiptBatchId | — |
| RECEIPT_DATE | ReceiptAssociatedReceiptDate | — |
| RECEIPT_DATE | ReceiptLastReceiptDate | — |
| RECEIPT_DATE | ReceiptReceiptDate | ✅ |
| RECEIPT_DATE | ReceiptReverseReceiptDate | — |
| RECEIPT_DATE | ReceiptSchedReceiptDate | — |
| RECEIPT_METHOD_ID | ReceiptAssociatedReceiptMethodId | — |
| RECEIPT_METHOD_ID | ReceiptLastReceiptMethodId | — |
| RECEIPT_METHOD_ID | ReceiptReceiptMethodId | — |
| RECEIPT_METHOD_ID | ReceiptReverseReceiptMethodId | — |
| RECEIPT_METHOD_ID | ReceiptSchedReceiptMethodId | — |
| RECEIPT_NUMBER | ReceiptAssociatedReceiptNumber | — |
| RECEIPT_NUMBER | ReceiptLastReceiptNumber | — |
| RECEIPT_NUMBER | ReceiptReceiptNumber | ✅ |
| RECEIPT_NUMBER | ReceiptReverseReceiptNumber | — |
| RECEIPT_NUMBER | ReceiptSchedReceiptNumber | — |
| RECEIVABLES_TRX_ID | ReceiptAssociatedReceivablesTrxId | — |
| RECEIVABLES_TRX_ID | ReceiptLastReceivablesTrxId | — |
| RECEIVABLES_TRX_ID | ReceiptReceivablesTrxId | — |
| RECEIVABLES_TRX_ID | ReceiptReverseReceivablesTrxId | — |
| RECEIVABLES_TRX_ID | ReceiptSchedReceivablesTrxId | — |
| RECON_FLAG | ReceiptAssociatedReconFlag | — |
| RECON_FLAG | ReceiptLastReconFlag | — |
| RECON_FLAG | ReceiptReconFlag | — |
| RECON_FLAG | ReceiptReverseReconFlag | — |
| RECON_FLAG | ReceiptSchedReconFlag | — |
| REFERENCE_ID | ReceiptAssociatedReferenceId | — |
| REFERENCE_ID | ReceiptLastReferenceId | — |
| REFERENCE_ID | ReceiptReferenceId | — |
| REFERENCE_ID | ReceiptReverseReferenceId | — |
| REFERENCE_ID | ReceiptSchedReferenceId | — |
| REFERENCE_TYPE | ReceiptAssociatedReferenceType | — |
| REFERENCE_TYPE | ReceiptLastReferenceType | — |
| REFERENCE_TYPE | ReceiptReferenceType | — |
| REFERENCE_TYPE | ReceiptReverseReferenceType | — |
| REFERENCE_TYPE | ReceiptSchedReferenceType | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptAssociatedRemitBankAcctUseId | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptLastRemitBankAcctUseId | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptRemitBankAcctUseId | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptReverseRemitBankAcctUseId | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptSchedRemitBankAcctUseId | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptAssociatedRemittanceBankAccountId | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptLastRemittanceBankAccountId | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptRemittanceBankAccountId | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptReverseRemittanceBankAccountId | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptSchedRemittanceBankAccountId | — |
| REMITTANCE_BATCH_ID | ReceiptAssociatedRemittanceBatchId | — |
| REMITTANCE_BATCH_ID | ReceiptLastRemittanceBatchId | — |
| REMITTANCE_BATCH_ID | ReceiptRemittanceBatchId | — |
| REMITTANCE_BATCH_ID | ReceiptReverseRemittanceBatchId | — |
| REMITTANCE_BATCH_ID | ReceiptSchedRemittanceBatchId | — |
| REQUEST_ID | ReceiptAssociatedRequestId | — |
| REQUEST_ID | ReceiptLastRequestId | — |
| REQUEST_ID | ReceiptRequestId | — |
| REQUEST_ID | ReceiptReverseRequestId | — |
| REQUEST_ID | ReceiptSchedRequestId | — |
| RESOURCE_ID | ReceiptAssociatedResourceId | — |
| RESOURCE_ID | ReceiptLastResourceId | — |
| RESOURCE_ID | ReceiptResourceId | — |
| RESOURCE_ID | ReceiptReverseResourceId | — |
| RESOURCE_ID | ReceiptSchedResourceId | — |
| REVERSAL_CATEGORY | ReceiptAssociatedReversalCategory | — |
| REVERSAL_CATEGORY | ReceiptLastReversalCategory | — |
| REVERSAL_CATEGORY | ReceiptReversalCategory | ✅ |
| REVERSAL_CATEGORY | ReceiptReverseReversalCategory | — |
| REVERSAL_CATEGORY | ReceiptSchedReversalCategory | — |
| REVERSAL_COMMENTS | ReceiptAssociatedReversalComments | — |
| REVERSAL_COMMENTS | ReceiptLastReversalComments | — |
| REVERSAL_COMMENTS | ReceiptReversalComments | ✅ |
| REVERSAL_COMMENTS | ReceiptReverseReversalComments | — |
| REVERSAL_COMMENTS | ReceiptSchedReversalComments | — |
| REVERSAL_DATE | ReceiptAssociatedReversalDate | — |
| REVERSAL_DATE | ReceiptLastReversalDate | — |
| REVERSAL_DATE | ReceiptReversalDate | ✅ |
| REVERSAL_DATE | ReceiptReverseReversalDate | — |
| REVERSAL_DATE | ReceiptSchedReversalDate | — |
| REVERSAL_REASON_CODE | ReceiptAssociatedReversalReasonCode | — |
| REVERSAL_REASON_CODE | ReceiptLastReversalReasonCode | — |
| REVERSAL_REASON_CODE | ReceiptReversalReasonCode | ✅ |
| REVERSAL_REASON_CODE | ReceiptReverseReversalReasonCode | — |
| REVERSAL_REASON_CODE | ReceiptSchedReversalReasonCode | — |
| SELECTED_FOR_FACTORING_FLAG | ReceiptAssociatedSelectedForFactoringFlag | — |
| SELECTED_FOR_FACTORING_FLAG | ReceiptLastSelectedForFactoringFlag | — |
| SELECTED_FOR_FACTORING_FLAG | ReceiptReverseSelectedForFactoringFlag | — |
| SELECTED_FOR_FACTORING_FLAG | ReceiptSchedSelectedForFactoringFlag | — |
| SELECTED_FOR_FACTORING_FLAG | ReceiptSelectedForFactoringFlag | — |
| SELECTED_REMITTANCE_BATCH_ID | ReceiptAssociatedSelectedRemittanceBatchId | — |
| SELECTED_REMITTANCE_BATCH_ID | ReceiptLastSelectedRemittanceBatchId | — |
| SELECTED_REMITTANCE_BATCH_ID | ReceiptReverseSelectedRemittanceBatchId | — |
| SELECTED_REMITTANCE_BATCH_ID | ReceiptSchedSelectedRemittanceBatchId | — |
| SELECTED_REMITTANCE_BATCH_ID | ReceiptSelectedRemittanceBatchId | — |
| SET_OF_BOOKS_ID | ReceiptAssociatedSetOfBooksId | — |
| SET_OF_BOOKS_ID | ReceiptLastSetOfBooksId | — |
| SET_OF_BOOKS_ID | ReceiptReverseSetOfBooksId | — |
| SET_OF_BOOKS_ID | ReceiptSchedSetOfBooksId | — |
| SET_OF_BOOKS_ID | ReceiptSetOfBooksId | — |
| STATUS | ReceiptAssociatedStatus | — |
| STATUS | ReceiptLastStatus | — |
| STATUS | ReceiptReverseStatus | — |
| STATUS | ReceiptSchedStatus | — |
| STATUS | ReceiptStatus | — |
| TAX_RATE | ReceiptAssociatedTaxRate | — |
| TAX_RATE | ReceiptLastTaxRate | — |
| TAX_RATE | ReceiptReverseTaxRate | — |
| TAX_RATE | ReceiptSchedTaxRate | — |
| TAX_RATE | ReceiptTaxRate | ✅ |
| TYPE | ReceiptAssociatedType | — |
| TYPE | ReceiptLastType | — |
| TYPE | ReceiptReverseType | — |
| TYPE | ReceiptSchedType | — |
| TYPE | ReceiptType | ✅ |
| UNIQUE_REFERENCE | ReceiptAssociatedUniqueReference | — |
| UNIQUE_REFERENCE | ReceiptLastUniqueReference | — |
| UNIQUE_REFERENCE | ReceiptReverseUniqueReference | — |
| UNIQUE_REFERENCE | ReceiptSchedUniqueReference | — |
| UNIQUE_REFERENCE | ReceiptUniqueReference | — |
| USSGL_TRANSACTION_CODE | ReceiptAssociatedUssglTransactionCode | — |
| USSGL_TRANSACTION_CODE | ReceiptLastUssglTransactionCode | — |
| USSGL_TRANSACTION_CODE | ReceiptReverseUssglTransactionCode | — |
| USSGL_TRANSACTION_CODE | ReceiptSchedUssglTransactionCode | — |
| USSGL_TRANSACTION_CODE | ReceiptUssglTransactionCode | — |
| USSGL_TRANSACTION_CODE_CONTEXT | ReceiptAssociatedUssglTransactionCodeContext | — |
| USSGL_TRANSACTION_CODE_CONTEXT | ReceiptLastUssglTransactionCodeContext | — |
| USSGL_TRANSACTION_CODE_CONTEXT | ReceiptReverseUssglTransactionCodeContext | — |
| USSGL_TRANSACTION_CODE_CONTEXT | ReceiptSchedUssglTransactionCodeContext | — |
| USSGL_TRANSACTION_CODE_CONTEXT | ReceiptUssglTransactionCodeContext | — |
| VAT_TAX_ID | ReceiptAssociatedVatTaxId | — |
| VAT_TAX_ID | ReceiptLastVatTaxId | — |
| VAT_TAX_ID | ReceiptReverseVatTaxId | — |
| VAT_TAX_ID | ReceiptSchedVatTaxId | — |
| VAT_TAX_ID | ReceiptVatTaxId | — |

### [[receiptapplicationpvo|ReceiptApplicationPVO]] (AR · BICC: 26/83)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTUAL_VALUE_DATE | ReceiptActualValueDate | ✅ |
| ADDRESS_VERIFICATION_CODE | ReceiptAddressVerificationCode | ✅ |
| AMOUNT | ReceiptAmount | — |
| ANTICIPATED_CLEARING_DATE | ReceiptAnticipatedClearingDate | ✅ |
| APPLICATION_NOTES | ReceiptApplicationNotes | — |
| APPROVAL_CODE | ReceiptApprovalCode | — |
| AUTOAPPLY_FLAG | ReceiptAutoapplyFlag | — |
| AUTOMATCH_REQUEST_ID | ReceiptAutomatchRequestId | — |
| AX_ACCOUNTED_FLAG | ReceiptAxAccountedFlag | — |
| CASH_RECEIPT_ID | ReceiptCashReceiptId | — |
| CC_ERROR_CODE | ReceiptCcErrorCode | — |
| CC_ERROR_FLAG | ReceiptCcErrorFlag | — |
| CC_ERROR_TEXT | ReceiptCcErrorText | — |
| CODE_COMBINATION_ID | ReceiptCodeCombinationId | — |
| COLLECTOR_ID | ReceiptCollectorId | — |
| COMMENTS | ReceiptComments | ✅ |
| CONFIRMED_FLAG | ReceiptConfirmedFlag | ✅ |
| CREATED_BY | ReceiptCreatedBy | ✅ |
| CREATION_DATE | ReceiptCreationDate | ✅ |
| CURRENCY_CODE | ReceiptCurrencyCode | — |
| CUSTOMER_BANK_ACCOUNT_ID | ReceiptCustomerBankAccountId | — |
| CUSTOMER_BANK_BRANCH_ID | ReceiptCustomerBankBranchId | — |
| CUSTOMER_RECEIPT_REFERENCE | ReceiptCustomerReceiptReference | ✅ |
| CUSTOMER_SITE_USE_ID | ReceiptCustomerSiteUseId | — |
| DEPOSIT_DATE | ReceiptDepositDate | ✅ |
| DISTRIBUTION_SET_ID | ReceiptDistributionSetId | — |
| DOC_SEQUENCE_ID | ReceiptDocSequenceId | — |
| DOC_SEQUENCE_VALUE | ReceiptDocSequenceValue | ✅ |
| EXCHANGE_DATE | ReceiptExchangeDate | ✅ |
| EXCHANGE_RATE | ReceiptExchangeRate | ✅ |
| EXCHANGE_RATE_TYPE | ReceiptExchangeRateType | ✅ |
| FACTOR_DISCOUNT_AMOUNT | ReceiptFactorDiscountAmount | — |
| ISSUE_DATE | ReceiptIssueDate | — |
| ISSUER_BANK_BRANCH_ID | ReceiptIssuerBankBranchId | — |
| ISSUER_NAME | ReceiptIssuerName | — |
| LAST_UPDATE_DATE | ReceiptLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ReceiptLastUpdateLogin | — |
| LAST_UPDATED_BY | ReceiptLastUpdatedBy | ✅ |
| LEGAL_ENTITY_ID | ReceiptLegalEntityId | — |
| LOGICAL_GROUP_REFERENCE | ReceiptLogicalGroupReference | — |
| MISC_PAYMENT_SOURCE | ReceiptMiscPaymentSource | ✅ |
| OBJECT_VERSION_NUMBER | ReceiptObjectVersionNumber | — |
| OLD_CUSTOMER_BANK_ACCOUNT_ID | ReceiptOldCustomerBankAccountId | — |
| OLD_CUSTOMER_BANK_BRANCH_ID | ReceiptOldCustomerBankBranchId | — |
| OLD_ISSUER_BANK_BRANCH_ID | ReceiptOldIssuerBankBranchId | — |
| ORG_ID | ReceiptOrgId | — |
| OVERRIDE_REMIT_ACCOUNT_FLAG | ReceiptOverrideRemitAccountFlag | — |
| PAY_FROM_CUSTOMER | ReceiptPayFromCustomer | — |
| PAYMENT_SERVER_ORDER_NUM | ReceiptPaymentServerOrderNum | — |
| PAYMENT_TRXN_EXTENSION_ID | ReceiptPaymentTrxnExtensionId | — |
| POSTMARK_DATE | ReceiptPostmarkDate | ✅ |
| PROGRAM_APPLICATION_ID | ReceiptProgramApplicationId | — |
| PROGRAM_ID | ReceiptProgramId | — |
| PROGRAM_UPDATE_DATE | ReceiptProgramUpdateDate | — |
| PROMISE_SOURCE | ReceiptPromiseSource | — |
| REC_VERSION_NUMBER | ReceiptRecVersionNumber | — |
| RECEIPT_BATCH_ID | ReceiptReceiptBatchId | — |
| RECEIPT_DATE | ReceiptReceiptDate | ✅ |
| RECEIPT_METHOD_ID | ReceiptReceiptMethodId | — |
| RECEIPT_NUMBER | ReceiptReceiptNumber | ✅ |
| RECEIVABLES_TRX_ID | ReceiptReceivablesTrxId | — |
| RECON_FLAG | ReceiptReconFlag | — |
| REFERENCE_ID | ReceiptReferenceId | — |
| REFERENCE_TYPE | ReceiptReferenceType | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptRemitBankAcctUseId | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptRemittanceBankAccountId | — |
| REMITTANCE_BATCH_ID | ReceiptRemittanceBatchId | — |
| REQUEST_ID | ReceiptRequestId | — |
| RESOURCE_ID | ReceiptResourceId | — |
| REVERSAL_CATEGORY | ReceiptReversalCategory | ✅ |
| REVERSAL_COMMENTS | ReceiptReversalComments | ✅ |
| REVERSAL_DATE | ReceiptReversalDate | ✅ |
| REVERSAL_REASON_CODE | ReceiptReversalReasonCode | ✅ |
| SELECTED_FOR_FACTORING_FLAG | ReceiptSelectedForFactoringFlag | — |
| SELECTED_REMITTANCE_BATCH_ID | ReceiptSelectedRemittanceBatchId | — |
| SET_OF_BOOKS_ID | ReceiptSetOfBooksId | — |
| STATUS | ReceiptStatus | ✅ |
| TAX_RATE | ReceiptTaxRate | ✅ |
| TYPE | ReceiptType | ✅ |
| UNIQUE_REFERENCE | ReceiptUniqueReference | — |
| USSGL_TRANSACTION_CODE | ReceiptUssglTransactionCode | — |
| USSGL_TRANSACTION_CODE_CONTEXT | ReceiptUssglTransactionCodeContext | — |
| VAT_TAX_ID | ReceiptVatTaxId | — |

### [[receiptheaderextractpvo|ReceiptHeaderExtractPVO]] (OTHER · BICC: 88/135)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTUAL_VALUE_DATE | ArCashReceiptActualValueDate | ✅ |
| ADDRESS_VERIFICATION_CODE | ArCashReceiptAddressVerificationCode | ✅ |
| AMOUNT | ArCashReceiptAmount | ✅ |
| ANTICIPATED_CLEARING_DATE | ArCashReceiptAnticipatedClearingDate | ✅ |
| APPLICATION_NOTES | ArCashReceiptApplicationNotes | ✅ |
| APPROVAL_CODE | ArCashReceiptApprovalCode | ✅ |
| ATTRIBUTE1 | ArCashReceiptAttribute1 | — |
| ATTRIBUTE10 | ArCashReceiptAttribute10 | — |
| ATTRIBUTE11 | ArCashReceiptAttribute11 | — |
| ATTRIBUTE12 | ArCashReceiptAttribute12 | — |
| ATTRIBUTE13 | ArCashReceiptAttribute13 | — |
| ATTRIBUTE14 | ArCashReceiptAttribute14 | — |
| ATTRIBUTE15 | ArCashReceiptAttribute15 | — |
| ATTRIBUTE2 | ArCashReceiptAttribute2 | — |
| ATTRIBUTE3 | ArCashReceiptAttribute3 | — |
| ATTRIBUTE4 | ArCashReceiptAttribute4 | — |
| ATTRIBUTE5 | ArCashReceiptAttribute5 | — |
| ATTRIBUTE6 | ArCashReceiptAttribute6 | — |
| ATTRIBUTE7 | ArCashReceiptAttribute7 | — |
| ATTRIBUTE8 | ArCashReceiptAttribute8 | — |
| ATTRIBUTE9 | ArCashReceiptAttribute9 | — |
| ATTRIBUTE_CATEGORY | ArCashReceiptAttributeCategory | — |
| AUTOAPPLY_FLAG | ArCashReceiptAutoapplyFlag | ✅ |
| AUTOMATCH_REQUEST_ID | ArCashReceiptAutomatchRequestId | ✅ |
| AX_ACCOUNTED_FLAG | ArCashReceiptAxAccountedFlag | ✅ |
| CASH_RECEIPT_ID | ArCashReceiptCashReceiptId | ✅ |
| CC_ERROR_CODE | ArCashReceiptCcErrorCode | ✅ |
| CC_ERROR_FLAG | ArCashReceiptCcErrorFlag | ✅ |
| CC_ERROR_TEXT | ArCashReceiptCcErrorText | ✅ |
| CODE_COMBINATION_ID | ArCashReceiptCodeCombinationId | ✅ |
| COLLECTOR_ID | ArCashReceiptCollectorId | ✅ |
| COMMENTS | ArCashReceiptComments | ✅ |
| CONFIRMED_FLAG | ArCashReceiptConfirmedFlag | ✅ |
| CREATED_BY | ArCashReceiptCreatedBy | ✅ |
| CREATION_DATE | ArCashReceiptCreationDate | ✅ |
| CURRENCY_CODE | ArCashReceiptCurrencyCode | ✅ |
| CUSTOMER_BANK_ACCOUNT_ID | ArCashReceiptCustomerBankAccountId | ✅ |
| CUSTOMER_BANK_BRANCH_ID | ArCashReceiptCustomerBankBranchId | ✅ |
| CUSTOMER_RECEIPT_REFERENCE | ArCashReceiptCustomerReceiptReference | ✅ |
| CUSTOMER_SITE_USE_ID | ArCashReceiptCustomerSiteUseId | ✅ |
| DEPOSIT_DATE | ArCashReceiptDepositDate | ✅ |
| DISTRIBUTION_SET_ID | ArCashReceiptDistributionSetId | ✅ |
| DOC_SEQUENCE_ID | ArCashReceiptDocSequenceId | ✅ |
| DOC_SEQUENCE_VALUE | ArCashReceiptDocSequenceValue | ✅ |
| EXCHANGE_DATE | ArCashReceiptExchangeDate | ✅ |
| EXCHANGE_RATE | ArCashReceiptExchangeRate | ✅ |
| EXCHANGE_RATE_TYPE | ArCashReceiptExchangeRateType | ✅ |
| FACTOR_DISCOUNT_AMOUNT | ArCashReceiptFactorDiscountAmount | ✅ |
| GLOBAL_ATTRIBUTE1 | ArCashReceiptGlobalAttribute1 | — |
| GLOBAL_ATTRIBUTE10 | ArCashReceiptGlobalAttribute10 | — |
| GLOBAL_ATTRIBUTE11 | ArCashReceiptGlobalAttribute11 | — |
| GLOBAL_ATTRIBUTE12 | ArCashReceiptGlobalAttribute12 | — |
| GLOBAL_ATTRIBUTE13 | ArCashReceiptGlobalAttribute13 | — |
| GLOBAL_ATTRIBUTE14 | ArCashReceiptGlobalAttribute14 | — |
| GLOBAL_ATTRIBUTE15 | ArCashReceiptGlobalAttribute15 | — |
| GLOBAL_ATTRIBUTE16 | ArCashReceiptGlobalAttribute16 | — |
| GLOBAL_ATTRIBUTE17 | ArCashReceiptGlobalAttribute17 | — |
| GLOBAL_ATTRIBUTE18 | ArCashReceiptGlobalAttribute18 | — |
| GLOBAL_ATTRIBUTE19 | ArCashReceiptGlobalAttribute19 | — |
| GLOBAL_ATTRIBUTE2 | ArCashReceiptGlobalAttribute2 | — |
| GLOBAL_ATTRIBUTE20 | ArCashReceiptGlobalAttribute20 | — |
| GLOBAL_ATTRIBUTE3 | ArCashReceiptGlobalAttribute3 | — |
| GLOBAL_ATTRIBUTE4 | ArCashReceiptGlobalAttribute4 | — |
| GLOBAL_ATTRIBUTE5 | ArCashReceiptGlobalAttribute5 | — |
| GLOBAL_ATTRIBUTE6 | ArCashReceiptGlobalAttribute6 | — |
| GLOBAL_ATTRIBUTE7 | ArCashReceiptGlobalAttribute7 | — |
| GLOBAL_ATTRIBUTE8 | ArCashReceiptGlobalAttribute8 | — |
| GLOBAL_ATTRIBUTE9 | ArCashReceiptGlobalAttribute9 | — |
| GLOBAL_ATTRIBUTE_CATEGORY | ArCashReceiptGlobalAttributeCategory | — |
| GLOBAL_ATTRIBUTE_DATE1 | ArCashReceiptGlobalAttributeDate1 | — |
| GLOBAL_ATTRIBUTE_DATE2 | ArCashReceiptGlobalAttributeDate2 | — |
| GLOBAL_ATTRIBUTE_DATE3 | ArCashReceiptGlobalAttributeDate3 | — |
| GLOBAL_ATTRIBUTE_DATE4 | ArCashReceiptGlobalAttributeDate4 | — |
| GLOBAL_ATTRIBUTE_DATE5 | ArCashReceiptGlobalAttributeDate5 | — |
| GLOBAL_ATTRIBUTE_NUMBER1 | ArCashReceiptGlobalAttributeNumber1 | — |
| GLOBAL_ATTRIBUTE_NUMBER2 | ArCashReceiptGlobalAttributeNumber2 | — |
| GLOBAL_ATTRIBUTE_NUMBER3 | ArCashReceiptGlobalAttributeNumber3 | — |
| GLOBAL_ATTRIBUTE_NUMBER4 | ArCashReceiptGlobalAttributeNumber4 | — |
| GLOBAL_ATTRIBUTE_NUMBER5 | ArCashReceiptGlobalAttributeNumber5 | — |
| ISSUE_DATE | ArCashReceiptIssueDate | ✅ |
| ISSUER_BANK_BRANCH_ID | ArCashReceiptIssuerBankBranchId | ✅ |
| ISSUER_NAME | ArCashReceiptIssuerName | ✅ |
| LAST_UPDATE_DATE | ArCashReceiptLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ArCashReceiptLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ArCashReceiptLastUpdatedBy | ✅ |
| LEGAL_ENTITY_ID | ArCashReceiptLegalEntityId | ✅ |
| LOGICAL_GROUP_REFERENCE | ArCashReceiptLogicalGroupReference | ✅ |
| MISC_PAYMENT_SOURCE | ArCashReceiptMiscPaymentSource | ✅ |
| OBJECT_VERSION_NUMBER | ArCashReceiptObjectVersionNumber | ✅ |
| OLD_CUSTOMER_BANK_ACCOUNT_ID | ArCashReceiptOldCustomerBankAccountId | ✅ |
| OLD_CUSTOMER_BANK_BRANCH_ID | ArCashReceiptOldCustomerBankBranchId | ✅ |
| OLD_ISSUER_BANK_BRANCH_ID | ArCashReceiptOldIssuerBankBranchId | ✅ |
| ORG_ID | ArCashReceiptOrgId | ✅ |
| OVERRIDE_REMIT_ACCOUNT_FLAG | ArCashReceiptOverrideRemitAccountFlag | ✅ |
| PAY_FROM_CUSTOMER | ArCashReceiptPayFromCustomer | ✅ |
| PAYMENT_SERVER_ORDER_NUM | ArCashReceiptPaymentServerOrderNum | ✅ |
| PAYMENT_TRXN_EXTENSION_ID | ArCashReceiptPaymentTrxnExtensionId | ✅ |
| POSTMARK_DATE | ArCashReceiptPostmarkDate | ✅ |
| PREV_CUSTOMER_SITE_USE_ID | ArCashReceiptPrevCustomerSiteUseId | ✅ |
| PREV_PAY_FROM_CUSTOMER | ArCashReceiptPrevPayFromCustomer | ✅ |
| PROGRAM_APPLICATION_ID | ArCashReceiptProgramApplicationId | ✅ |
| PROGRAM_ID | ArCashReceiptProgramId | ✅ |
| PROGRAM_UPDATE_DATE | ArCashReceiptProgramUpdateDate | ✅ |
| PROMISE_SOURCE | ArCashReceiptPromiseSource | ✅ |
| REC_VERSION_NUMBER | ArCashReceiptRecVersionNumber | ✅ |
| RECEIPT_BATCH_ID | ArCashReceiptReceiptBatchId | ✅ |
| RECEIPT_DATE | ArCashReceiptReceiptDate | ✅ |
| RECEIPT_METHOD_ID | ArCashReceiptReceiptMethodId | ✅ |
| RECEIPT_NUMBER | ArCashReceiptReceiptNumber | ✅ |
| RECEIVABLES_TRX_ID | ArCashReceiptReceivablesTrxId | ✅ |
| RECOMMENDATION_COUNT | ArCashReceiptRecommendationCount | ✅ |
| RECON_FLAG | ArCashReceiptReconFlag | ✅ |
| REFERENCE_ID | ArCashReceiptReferenceId | ✅ |
| REFERENCE_TYPE | ArCashReceiptReferenceType | ✅ |
| REMIT_BANK_ACCT_USE_ID | ArCashReceiptRemitBankAcctUseId | ✅ |
| REMITTANCE_BANK_ACCOUNT_ID | ArCashReceiptRemittanceBankAccountId | ✅ |
| REMITTANCE_BATCH_ID | ArCashReceiptRemittanceBatchId | ✅ |
| REQUEST_ID | ArCashReceiptRequestId | ✅ |
| RESOURCE_ID | ArCashReceiptResourceId | ✅ |
| REVERSAL_CATEGORY | ArCashReceiptReversalCategory | ✅ |
| REVERSAL_COMMENTS | ArCashReceiptReversalComments | ✅ |
| REVERSAL_DATE | ArCashReceiptReversalDate | ✅ |
| REVERSAL_REASON_CODE | ArCashReceiptReversalReasonCode | ✅ |
| SELECTED_FOR_FACTORING_FLAG | ArCashReceiptSelectedForFactoringFlag | ✅ |
| SELECTED_REMITTANCE_BATCH_ID | ArCashReceiptSelectedRemittanceBatchId | ✅ |
| SET_OF_BOOKS_ID | ArCashReceiptSetOfBooksId | ✅ |
| STATUS | ArCashReceiptStatus | ✅ |
| STRUCTURED_PAYMENT_REFERENCE | ArCashReceiptStructuredPaymentReference | ✅ |
| TAX_AMOUNT | ArCashReceiptTaxAmount | ✅ |
| TAX_RATE | ArCashReceiptTaxRate | ✅ |
| TYPE | ArCashReceiptType | ✅ |
| UNIQUE_REFERENCE | ArCashReceiptUniqueReference | ✅ |
| USSGL_TRANSACTION_CODE | ArCashReceiptUssglTransactionCode | ✅ |
| USSGL_TRANSACTION_CODE_CONTEXT | ArCashReceiptUssglTransactionCodeContext | ✅ |
| VAT_TAX_ID | ArCashReceiptVatTaxId | ✅ |

### [[receiptheaderpvo|ReceiptHeaderPVO]] (AR · BICC: 29/83)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTUAL_VALUE_DATE | ReceiptActualValueDate | ✅ |
| ADDRESS_VERIFICATION_CODE | ReceiptAddressVerificationCode | ✅ |
| AMOUNT | ReceiptAmount | ✅ |
| ANTICIPATED_CLEARING_DATE | ReceiptAnticipatedClearingDate | ✅ |
| APPLICATION_NOTES | ReceiptApplicationNotes | — |
| APPROVAL_CODE | ReceiptApprovalCode | — |
| AUTOAPPLY_FLAG | ReceiptAutoapplyFlag | — |
| AUTOMATCH_REQUEST_ID | ReceiptAutomatchRequestId | — |
| AX_ACCOUNTED_FLAG | ReceiptAxAccountedFlag | — |
| CASH_RECEIPT_ID | CashReceiptId | ✅ |
| CC_ERROR_CODE | ReceiptCcErrorCode | — |
| CC_ERROR_FLAG | ReceiptCcErrorFlag | — |
| CC_ERROR_TEXT | ReceiptCcErrorText | — |
| CODE_COMBINATION_ID | ReceiptCodeCombinationId | — |
| COLLECTOR_ID | ReceiptCollectorId | — |
| COMMENTS | ReceiptComments | ✅ |
| CONFIRMED_FLAG | ReceiptConfirmedFlag | ✅ |
| CREATED_BY | ReceiptCreatedBy | ✅ |
| CREATION_DATE | ReceiptCreationDate | ✅ |
| CURRENCY_CODE | ReceiptCurrencyCode | — |
| CUSTOMER_BANK_ACCOUNT_ID | ReceiptCustomerBankAccountId | — |
| CUSTOMER_BANK_BRANCH_ID | ReceiptCustomerBankBranchId | — |
| CUSTOMER_RECEIPT_REFERENCE | ReceiptCustomerReceiptReference | ✅ |
| CUSTOMER_SITE_USE_ID | ReceiptCustomerSiteUseId | — |
| DEPOSIT_DATE | ReceiptDepositDate | ✅ |
| DISTRIBUTION_SET_ID | ReceiptDistributionSetId | — |
| DOC_SEQUENCE_ID | ReceiptDocSequenceId | — |
| DOC_SEQUENCE_VALUE | ReceiptDocSequenceValue | ✅ |
| EXCHANGE_DATE | ReceiptExchangeDate | ✅ |
| EXCHANGE_RATE | ReceiptExchangeRate | ✅ |
| EXCHANGE_RATE_TYPE | ReceiptExchangeRateType | ✅ |
| FACTOR_DISCOUNT_AMOUNT | ReceiptFactorDiscountAmount | ✅ |
| ISSUE_DATE | ReceiptIssueDate | — |
| ISSUER_BANK_BRANCH_ID | ReceiptIssuerBankBranchId | — |
| ISSUER_NAME | ReceiptIssuerName | — |
| LAST_UPDATE_DATE | ReceiptLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ReceiptLastUpdateLogin | — |
| LAST_UPDATED_BY | ReceiptLastUpdatedBy | ✅ |
| LEGAL_ENTITY_ID | ReceiptLegalEntityId | — |
| LOGICAL_GROUP_REFERENCE | ReceiptLogicalGroupReference | — |
| MISC_PAYMENT_SOURCE | ReceiptMiscPaymentSource | ✅ |
| OBJECT_VERSION_NUMBER | ReceiptObjectVersionNumber | — |
| OLD_CUSTOMER_BANK_ACCOUNT_ID | ReceiptOldCustomerBankAccountId | — |
| OLD_CUSTOMER_BANK_BRANCH_ID | ReceiptOldCustomerBankBranchId | — |
| OLD_ISSUER_BANK_BRANCH_ID | ReceiptOldIssuerBankBranchId | — |
| ORG_ID | ReceiptOrgId | — |
| OVERRIDE_REMIT_ACCOUNT_FLAG | ReceiptOverrideRemitAccountFlag | — |
| PAY_FROM_CUSTOMER | ReceiptPayFromCustomer | — |
| PAYMENT_SERVER_ORDER_NUM | ReceiptPaymentServerOrderNum | — |
| PAYMENT_TRXN_EXTENSION_ID | ReceiptPaymentTrxnExtensionId | — |
| POSTMARK_DATE | ReceiptPostmarkDate | ✅ |
| PROGRAM_APPLICATION_ID | ReceiptProgramApplicationId | — |
| PROGRAM_ID | ReceiptProgramId | — |
| PROGRAM_UPDATE_DATE | ReceiptProgramUpdateDate | — |
| PROMISE_SOURCE | ReceiptPromiseSource | — |
| REC_VERSION_NUMBER | ReceiptRecVersionNumber | — |
| RECEIPT_BATCH_ID | ReceiptReceiptBatchId | — |
| RECEIPT_DATE | ReceiptReceiptDate | ✅ |
| RECEIPT_METHOD_ID | ReceiptReceiptMethodId | — |
| RECEIPT_NUMBER | ReceiptReceiptNumber | ✅ |
| RECEIVABLES_TRX_ID | ReceiptReceivablesTrxId | — |
| RECON_FLAG | ReceiptReconFlag | — |
| REFERENCE_ID | ReceiptReferenceId | — |
| REFERENCE_TYPE | ReceiptReferenceType | ✅ |
| REMIT_BANK_ACCT_USE_ID | ReceiptRemitBankAcctUseId | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptRemittanceBankAccountId | — |
| REMITTANCE_BATCH_ID | ReceiptRemittanceBatchId | — |
| REQUEST_ID | ReceiptRequestId | — |
| RESOURCE_ID | ReceiptResourceId | — |
| REVERSAL_CATEGORY | ReceiptReversalCategory | ✅ |
| REVERSAL_COMMENTS | ReceiptReversalComments | ✅ |
| REVERSAL_DATE | ReceiptReversalDate | ✅ |
| REVERSAL_REASON_CODE | ReceiptReversalReasonCode | ✅ |
| SELECTED_FOR_FACTORING_FLAG | ReceiptSelectedForFactoringFlag | — |
| SELECTED_REMITTANCE_BATCH_ID | ReceiptSelectedRemittanceBatchId | — |
| SET_OF_BOOKS_ID | ReceiptSetOfBooksId | — |
| STATUS | ReceiptStatus | — |
| TAX_RATE | ReceiptTaxRate | ✅ |
| TYPE | ReceiptType | ✅ |
| UNIQUE_REFERENCE | ReceiptUniqueReference | — |
| USSGL_TRANSACTION_CODE | ReceiptUssglTransactionCode | — |
| USSGL_TRANSACTION_CODE_CONTEXT | ReceiptUssglTransactionCodeContext | — |
| VAT_TAX_ID | ReceiptVatTaxId | — |

### [[receipthistorydistributionpvo|ReceiptHistoryDistributionPVO]] (AR · BICC: 3/85)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTUAL_VALUE_DATE | ReceiptActualValueDate | — |
| ADDRESS_VERIFICATION_CODE | ReceiptAddressVerificationCode | — |
| AMOUNT | ReceiptAmount | — |
| ANTICIPATED_CLEARING_DATE | ReceiptAnticipatedClearingDate | — |
| APPLICATION_NOTES | ReceiptApplicationNotes | — |
| APPROVAL_CODE | ReceiptApprovalCode | — |
| ATTRIBUTE_CATEGORY | ReceiptAttributeCategory | — |
| AUTOAPPLY_FLAG | ReceiptAutoapplyFlag | — |
| AUTOMATCH_REQUEST_ID | ReceiptAutomatchRequestId | — |
| AX_ACCOUNTED_FLAG | ReceiptAxAccountedFlag | — |
| CASH_RECEIPT_ID | ReceiptCashReceiptId | — |
| CC_ERROR_CODE | ReceiptCcErrorCode | — |
| CC_ERROR_FLAG | ReceiptCcErrorFlag | — |
| CC_ERROR_TEXT | ReceiptCcErrorText | — |
| CODE_COMBINATION_ID | ReceiptReceiptCodeCombinationId | — |
| COLLECTOR_ID | ReceiptCollectorId | — |
| COMMENTS | ReceiptComments | — |
| CONFIRMED_FLAG | ReceiptConfirmedFlag | — |
| CREATED_BY | ReceiptCreatedBy | — |
| CREATION_DATE | ReceiptCreationDate | — |
| CURRENCY_CODE | ReceiptCurrencyCode | — |
| CUSTOMER_BANK_ACCOUNT_ID | ReceiptCustomerBankAccountId | — |
| CUSTOMER_BANK_BRANCH_ID | ReceiptCustomerBankBranchId | — |
| CUSTOMER_RECEIPT_REFERENCE | ReceiptCustomerReceiptReference | — |
| CUSTOMER_SITE_USE_ID | ReceiptCustomerSiteUseId | — |
| DEPOSIT_DATE | ReceiptDepositDate | — |
| DISTRIBUTION_SET_ID | ReceiptDistributionSetId | — |
| DOC_SEQUENCE_ID | ReceiptDocSequenceId | — |
| DOC_SEQUENCE_VALUE | ReceiptDocSequenceValue | — |
| EXCHANGE_DATE | ReceiptExchangeDate | — |
| EXCHANGE_RATE | ReceiptExchangeRate | — |
| EXCHANGE_RATE_TYPE | ReceiptExchangeRateType | — |
| FACTOR_DISCOUNT_AMOUNT | ReceiptFactorDiscountAmount | — |
| ISSUE_DATE | ReceiptIssueDate | — |
| ISSUER_BANK_BRANCH_ID | ReceiptIssuerBankBranchId | — |
| ISSUER_NAME | ReceiptIssuerName | — |
| LAST_UPDATE_DATE | ReceiptLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ReceiptLastUpdateLogin | — |
| LAST_UPDATED_BY | ReceiptLastUpdatedBy | — |
| LEGAL_ENTITY_ID | ReceiptLegalEntityId | — |
| LOGICAL_GROUP_REFERENCE | ReceiptLogicalGroupReference | — |
| MISC_PAYMENT_SOURCE | ReceiptMiscPaymentSource | — |
| OBJECT_VERSION_NUMBER | ReceiptObjectVersionNumber | — |
| OLD_CUSTOMER_BANK_ACCOUNT_ID | ReceiptOldCustomerBankAccountId | — |
| OLD_CUSTOMER_BANK_BRANCH_ID | ReceiptOldCustomerBankBranchId | — |
| OLD_ISSUER_BANK_BRANCH_ID | ReceiptOldIssuerBankBranchId | — |
| ORG_ID | ReceiptOrgId | — |
| OVERRIDE_REMIT_ACCOUNT_FLAG | ReceiptOverrideRemitAccountFlag | — |
| PAY_FROM_CUSTOMER | ReceiptPayFromCustomer | — |
| PAYMENT_SERVER_ORDER_NUM | ReceiptPaymentServerOrderNum | — |
| PAYMENT_TRXN_EXTENSION_ID | ReceiptPaymentTrxnExtensionId | — |
| POSTMARK_DATE | ReceiptPostmarkDate | — |
| PROGRAM_APPLICATION_ID | ReceiptProgramApplicationId | — |
| PROGRAM_ID | ReceiptProgramId | — |
| PROGRAM_UPDATE_DATE | ReceiptProgramUpdateDate | — |
| PROMISE_SOURCE | ReceiptPromiseSource | — |
| REC_VERSION_NUMBER | ReceiptRecVersionNumber | — |
| RECEIPT_BATCH_ID | ReceiptReceiptReceiptBatchId | — |
| RECEIPT_DATE | ReceiptReceiptDate | — |
| RECEIPT_METHOD_ID | ReceiptReceiptMethodId | — |
| RECEIPT_NUMBER | ReceiptReceiptNumber | ✅ |
| RECEIVABLES_TRX_ID | ReceiptReceivablesTrxId | — |
| RECON_FLAG | ReceiptReconFlag | — |
| REFERENCE_ID | ReceiptReferenceId | — |
| REFERENCE_TYPE | ReceiptReferenceType | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptRemitBankAcctUseId | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptRemittanceBankAccountId | — |
| REMITTANCE_BATCH_ID | ReceiptRemittanceBatchId | — |
| REQUEST_ID | ReceiptRequestId | — |
| RESOURCE_ID | ReceiptResourceId | — |
| REVERSAL_CATEGORY | ReceiptReversalCategory | — |
| REVERSAL_COMMENTS | ReceiptReversalComments | — |
| REVERSAL_DATE | ReceiptReversalDate | — |
| REVERSAL_REASON_CODE | ReceiptReversalReasonCode | — |
| SELECTED_FOR_FACTORING_FLAG | ReceiptSelectedForFactoringFlag | — |
| SELECTED_REMITTANCE_BATCH_ID | ReceiptSelectedRemittanceBatchId | — |
| SET_OF_BOOKS_ID | ReceiptSetOfBooksId | — |
| STATUS | ReceiptStatus | — |
| TAX_AMOUNT | ReceiptTaxAmount | — |
| TAX_RATE | ReceiptTaxRate | — |
| TYPE | ReceiptType | ✅ |
| UNIQUE_REFERENCE | ReceiptUniqueReference | — |
| USSGL_TRANSACTION_CODE | ReceiptUssglTransactionCode | — |
| USSGL_TRANSACTION_CODE_CONTEXT | ReceiptUssglTransactionCodeContext | — |
| VAT_TAX_ID | ReceiptVatTaxId | — |

### [[receipthistorypvo|ReceiptHistoryPVO]] (AR · BICC: 3/85)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTUAL_VALUE_DATE | ReceiptActualValueDate | — |
| ADDRESS_VERIFICATION_CODE | ReceiptAddressVerificationCode | — |
| AMOUNT | ReceiptAmount | — |
| ANTICIPATED_CLEARING_DATE | ReceiptAnticipatedClearingDate | — |
| APPLICATION_NOTES | ReceiptApplicationNotes | — |
| APPROVAL_CODE | ReceiptApprovalCode | — |
| ATTRIBUTE_CATEGORY | ReceiptAttributeCategory | — |
| AUTOAPPLY_FLAG | ReceiptAutoapplyFlag | — |
| AUTOMATCH_REQUEST_ID | ReceiptAutomatchRequestId | — |
| AX_ACCOUNTED_FLAG | ReceiptAxAccountedFlag | — |
| CASH_RECEIPT_ID | ReceiptCashReceiptId | — |
| CC_ERROR_CODE | ReceiptCcErrorCode | — |
| CC_ERROR_FLAG | ReceiptCcErrorFlag | — |
| CC_ERROR_TEXT | ReceiptCcErrorText | — |
| CODE_COMBINATION_ID | ReceiptReceiptCodeCombinationId | — |
| COLLECTOR_ID | ReceiptCollectorId | — |
| COMMENTS | ReceiptComments | — |
| CONFIRMED_FLAG | ReceiptConfirmedFlag | — |
| CREATED_BY | ReceiptCreatedBy | — |
| CREATION_DATE | ReceiptCreationDate | — |
| CURRENCY_CODE | ReceiptCurrencyCode | — |
| CUSTOMER_BANK_ACCOUNT_ID | ReceiptCustomerBankAccountId | — |
| CUSTOMER_BANK_BRANCH_ID | ReceiptCustomerBankBranchId | — |
| CUSTOMER_RECEIPT_REFERENCE | ReceiptCustomerReceiptReference | — |
| CUSTOMER_SITE_USE_ID | ReceiptCustomerSiteUseId | — |
| DEPOSIT_DATE | ReceiptDepositDate | — |
| DISTRIBUTION_SET_ID | ReceiptDistributionSetId | — |
| DOC_SEQUENCE_ID | ReceiptDocSequenceId | — |
| DOC_SEQUENCE_VALUE | ReceiptDocSequenceValue | — |
| EXCHANGE_DATE | ReceiptExchangeDate | — |
| EXCHANGE_RATE | ReceiptExchangeRate | — |
| EXCHANGE_RATE_TYPE | ReceiptExchangeRateType | — |
| FACTOR_DISCOUNT_AMOUNT | ReceiptFactorDiscountAmount | — |
| ISSUE_DATE | ReceiptIssueDate | — |
| ISSUER_BANK_BRANCH_ID | ReceiptIssuerBankBranchId | — |
| ISSUER_NAME | ReceiptIssuerName | — |
| LAST_UPDATE_DATE | ReceiptLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ReceiptLastUpdateLogin | — |
| LAST_UPDATED_BY | ReceiptLastUpdatedBy | — |
| LEGAL_ENTITY_ID | ReceiptLegalEntityId | — |
| LOGICAL_GROUP_REFERENCE | ReceiptLogicalGroupReference | — |
| MISC_PAYMENT_SOURCE | ReceiptMiscPaymentSource | — |
| OBJECT_VERSION_NUMBER | ReceiptObjectVersionNumber | — |
| OLD_CUSTOMER_BANK_ACCOUNT_ID | ReceiptOldCustomerBankAccountId | — |
| OLD_CUSTOMER_BANK_BRANCH_ID | ReceiptOldCustomerBankBranchId | — |
| OLD_ISSUER_BANK_BRANCH_ID | ReceiptOldIssuerBankBranchId | — |
| ORG_ID | ReceiptOrgId | — |
| OVERRIDE_REMIT_ACCOUNT_FLAG | ReceiptOverrideRemitAccountFlag | — |
| PAY_FROM_CUSTOMER | ReceiptPayFromCustomer | — |
| PAYMENT_SERVER_ORDER_NUM | ReceiptPaymentServerOrderNum | — |
| PAYMENT_TRXN_EXTENSION_ID | ReceiptPaymentTrxnExtensionId | — |
| POSTMARK_DATE | ReceiptPostmarkDate | — |
| PROGRAM_APPLICATION_ID | ReceiptProgramApplicationId | — |
| PROGRAM_ID | ReceiptProgramId | — |
| PROGRAM_UPDATE_DATE | ReceiptProgramUpdateDate | — |
| PROMISE_SOURCE | ReceiptPromiseSource | — |
| REC_VERSION_NUMBER | ReceiptRecVersionNumber | — |
| RECEIPT_BATCH_ID | ReceiptReceiptReceiptBatchId | — |
| RECEIPT_DATE | ReceiptReceiptDate | — |
| RECEIPT_METHOD_ID | ReceiptReceiptMethodId | — |
| RECEIPT_NUMBER | ReceiptReceiptNumber | ✅ |
| RECEIVABLES_TRX_ID | ReceiptReceivablesTrxId | — |
| RECON_FLAG | ReceiptReconFlag | — |
| REFERENCE_ID | ReceiptReferenceId | — |
| REFERENCE_TYPE | ReceiptReferenceType | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptRemitBankAcctUseId | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptRemittanceBankAccountId | — |
| REMITTANCE_BATCH_ID | ReceiptRemittanceBatchId | — |
| REQUEST_ID | ReceiptRequestId | — |
| RESOURCE_ID | ReceiptResourceId | — |
| REVERSAL_CATEGORY | ReceiptReversalCategory | — |
| REVERSAL_COMMENTS | ReceiptReversalComments | — |
| REVERSAL_DATE | ReceiptReversalDate | — |
| REVERSAL_REASON_CODE | ReceiptReversalReasonCode | — |
| SELECTED_FOR_FACTORING_FLAG | ReceiptSelectedForFactoringFlag | — |
| SELECTED_REMITTANCE_BATCH_ID | ReceiptSelectedRemittanceBatchId | — |
| SET_OF_BOOKS_ID | ReceiptSetOfBooksId | — |
| STATUS | ReceiptStatus | — |
| TAX_AMOUNT | ReceiptTaxAmount | — |
| TAX_RATE | ReceiptTaxRate | — |
| TYPE | ReceiptType | ✅ |
| UNIQUE_REFERENCE | ReceiptUniqueReference | — |
| USSGL_TRANSACTION_CODE | ReceiptUssglTransactionCode | — |
| USSGL_TRANSACTION_CODE_CONTEXT | ReceiptUssglTransactionCodeContext | — |
| VAT_TAX_ID | ReceiptVatTaxId | — |

### [[transactionheaderbillsreceivablepvo|TransactionHeaderBillsReceivablePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CASH_RECEIPT_ID | RevCashRcptCashReceiptId | — |
| COMMENTS | RevCashRcptComments | — |
| ISSUER_NAME | RevCashRcptIssuerName | — |
| OBJECT_VERSION_NUMBER | RevCashRcptObjectVersionNumber | — |
| RECEIPT_NUMBER | RevCashRcptReceiptNumber | — |

### [[transactionheadernovcpvo|TransactionHeaderNoVCPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CASH_RECEIPT_ID | RevCashRcptCashReceiptId | — |
| COMMENTS | RevCashRcptComments | — |
| ISSUER_NAME | RevCashRcptIssuerName | — |
| OBJECT_VERSION_NUMBER | RevCashRcptObjectVersionNumber | — |
| RECEIPT_NUMBER | RevCashRcptReceiptNumber | — |

### [[transactionheaderpvo|TransactionHeaderPVO]] (AR · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CASH_RECEIPT_ID | RevCashRcptCashReceiptId | — |
| COMMENTS | RevCashRcptComments | — |
| ISSUER_NAME | RevCashRcptIssuerName | — |
| OBJECT_VERSION_NUMBER | RevCashRcptObjectVersionNumber | — |
| RECEIPT_NUMBER | RevCashRcptReceiptNumber | ✅ |

### [[transactionhistorydistributionpvo|TransactionHistoryDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CASH_RECEIPT_ID | RevCashRcptCashReceiptId | — |
| COMMENTS | RevCashRcptComments | — |
| ISSUER_NAME | RevCashRcptIssuerName | — |
| RECEIPT_NUMBER | RevCashRcptReceiptNumber | — |

### [[transactionhistorypvo|TransactionHistoryPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CASH_RECEIPT_ID | RevCashRcptCashReceiptId | — |
| COMMENTS | RevCashRcptComments | — |
| ISSUER_NAME | RevCashRcptIssuerName | — |
| RECEIPT_NUMBER | RevCashRcptReceiptNumber | — |

### [[transactionlinebillsreceivablepvo|TransactionLineBillsReceivablePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CASH_RECEIPT_ID | RevCashRcptCashReceiptId | — |
| COMMENTS | RevCashRcptComments | — |
| ISSUER_NAME | RevCashRcptIssuerName | — |
| OBJECT_VERSION_NUMBER | RevCashRcptObjectVersionNumber4 | — |
| RECEIPT_NUMBER | RevCashRcptReceiptNumber | — |

### [[transactionlinedistributionpvo|TransactionLineDistributionPVO]] (AR · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CASH_RECEIPT_ID | RevCashRcptCashReceiptId | — |
| COMMENTS | RevCashRcptComments | — |
| ISSUER_NAME | RevCashRcptIssuerName | — |
| OBJECT_VERSION_NUMBER | RevCashRcptObjectVersionNumber | — |
| RECEIPT_NUMBER | RevCashRcptReceiptNumber | ✅ |

### [[transactionlinepvo|TransactionLinePVO]] (AR · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CASH_RECEIPT_ID | RevCashRcptCashReceiptId | — |
| COMMENTS | RevCashRcptComments | — |
| ISSUER_NAME | RevCashRcptIssuerName | — |
| OBJECT_VERSION_NUMBER | RevCashRcptObjectVersionNumber4 | — |
| RECEIPT_NUMBER | RevCashRcptReceiptNumber | ✅ |

---

## 📚 Referências

- [Oracle Docs — AR_CASH_RECEIPTS_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/arcashreceiptsall-10044.html)
- [[ar-module-data-dictionary]] — Dossiê do módulo AR
