---
id: DOC-AR-023
doc_type: system-doc
title: "AR_BATCHES_ALL — Lotes de Recebimentos"
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
  - lotes-recebimentos
  - receipt-batches
  - batches
aliases:
  - AR_BATCHES_ALL
  - ar_batches_all
  - lotes-recebimentos-ar
  - receipt-batches
  - ar-batches
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_BATCHES_ALL

## 📌 Visão Geral

Armazena os **lotes de recebimentos** (receipt batches) do módulo Accounts Receivable. Cada registro representa um lote que agrupa múltiplos recebimentos para processamento conjunto — entrada manual em lote, importação via lockbox ou remessa bancária. Contém totais de controle (contagem e valor esperados vs. reais) para validação de integridade.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

**Nota:** Esta tabela é diferente de [[ra_batches_all]], que armazena lotes de *transações* (faturas). AR_BATCHES_ALL armazena lotes de *recebimentos*.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Entrada em lote:** Agrupamento de múltiplos recebimentos para digitação simultânea.
- **Lockbox:** Cada arquivo de lockbox importado gera um lote de recebimentos.
- **Controle de qualidade:** Validação de contagem e valor total do lote (controle vs. real).
- **Remessa bancária:** Lotes de recebimentos vinculados a um método e conta bancária.
- **Auditoria:** Rastreabilidade de quando e como os recebimentos foram registrados no sistema.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BATCH_ID | NUMBER(18) | NOT NULL | PK | Identificador único do lote de recebimentos | — | 🟢 100% |
| 2 | NAME | VARCHAR2(30) | NOT NULL | Identificação | Nome do lote | — | 🟢 100% |
| 3 | BATCH_DATE | DATE | NOT NULL | Data | Data do lote | — | 🟢 100% |
| 4 | STATUS | VARCHAR2(30) | NOT NULL | Classificação | Status do lote (e.g., OP, CL) | — | 🟢 100% |
| 5 | TYPE | VARCHAR2(30) | NULL | Classificação | Tipo do lote (MANUAL/LOCKBOX/REMITTANCE) | — | 🟢 100% |
| 6 | CONTROL_COUNT | NUMBER | NULL | Controle | Contagem esperada de recebimentos no lote | — | 🟢 100% |
| 7 | CONTROL_AMOUNT | NUMBER | NULL | Controle | Valor total esperado do lote | — | 🟢 100% |
| 8 | ACTUAL_COUNT | NUMBER | NULL | Controle | Contagem real de recebimentos no lote | — | 🟢 100% |
| 9 | ACTUAL_AMOUNT | NUMBER | NULL | Controle | Valor total real do lote | — | 🟢 100% |
| 10 | BATCH_SOURCE_ID | NUMBER(18) | NULL | Classificação | Fonte do lote | [[ra_batch_sources_all]] | 🟢 100% |
| 11 | RECEIPT_CLASS_ID | NUMBER(18) | NULL | Classificação | Classe do recebimento | — | 🟢 100% |
| 12 | RECEIPT_METHOD_ID | NUMBER(18) | NULL | Classificação | Método de recebimento | [[ar_receipt_methods]] | 🟢 100% |
| 13 | REMITTANCE_BANK_ACCOUNT_ID | NUMBER(18) | NULL | Bancário | Conta bancária de remessa | [[ce_bank_acct_uses_all]] | 🟢 100% |
| 14 | CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Código da moeda do lote | — | 🟢 100% |
| 15 | EXCHANGE_RATE_TYPE | VARCHAR2(30) | NULL | Financeiro | Tipo de taxa de câmbio | — | 🟢 100% |
| 16 | EXCHANGE_RATE | NUMBER | NULL | Financeiro | Taxa de câmbio | — | 🟢 100% |
| 17 | EXCHANGE_DATE | DATE | NULL | Financeiro | Data da taxa de câmbio | — | 🟢 100% |
| 18 | GL_DATE | DATE | NULL | Contabilidade | Data contábil padrão para recebimentos do lote | — | 🟢 100% |
| 19 | COMMENTS | VARCHAR2(2000) | NULL | Texto livre | Comentários sobre o lote | — | 🟢 100% |
| 20 | LOCKBOX_ID | NUMBER(18) | NULL | Classificação | Identificador do lockbox de origem | — | 🟢 100% |
| 21 | LOCKBOX_BATCH_NAME | VARCHAR2(30) | NULL | Identificação | Nome do lote no lockbox | — | 🟡 75% |
| 22 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 23 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 24 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 25 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 26 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 27 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 28 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 100% |
| 29 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ra_batch_sources_all]] — via `BATCH_SOURCE_ID` (fonte de transação que originou o lote)
- [[ar_receipt_methods]] — via `RECEIPT_METHOD_ID` (método de recebimento)
- [[ce_bank_acct_uses_all]] — via `REMITTANCE_BANK_ACCOUNT_ID` (conta bancária de remessa do lote)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit do lote de transações AR)

### Tabelas-filha (FK de saída)
- [[ar_cash_receipts_all]] — via `BATCH_ID` (recebimentos do lote, indireto via history)
- [[ar_cash_receipt_history_all]] — via `BATCH_ID` (histórico de recebimentos do lote)

---

## 📎 Uso Típico

### Lotes de recebimento com diferença de controle
```sql
SELECT b.NAME, b.BATCH_DATE, b.STATUS,
       b.CONTROL_COUNT, b.ACTUAL_COUNT,
       b.CONTROL_AMOUNT, b.ACTUAL_AMOUNT,
       b.CONTROL_AMOUNT - b.ACTUAL_AMOUNT AS diferenca
FROM   AR_BATCHES_ALL b
WHERE  b.CONTROL_AMOUNT <> b.ACTUAL_AMOUNT
  AND  b.ORG_ID = :p_org_id;
```

### Recebimentos de um lote
```sql
SELECT cr.RECEIPT_NUMBER, cr.AMOUNT, cr.RECEIPT_DATE, cr.STATUS
FROM   AR_CASH_RECEIPT_HISTORY_ALL crh
JOIN   AR_CASH_RECEIPTS_ALL cr ON cr.CASH_RECEIPT_ID = crh.CASH_RECEIPT_ID
WHERE  crh.BATCH_ID = :p_batch_id
  AND  crh.CURRENT_RECORD_FLAG = 'Y';
```

---

## 🔒 Observações

- **Não confundir** com [[ra_batches_all]], que armazena lotes de *transações* (faturas). Esta tabela (`AR_BATCHES_ALL`) armazena lotes de *recebimentos*.
- Os totais de controle (`CONTROL_COUNT`/`CONTROL_AMOUNT`) são inseridos pelo usuário; os reais (`ACTUAL_COUNT`/`ACTUAL_AMOUNT`) são calculados pelo sistema.
- Lotes de **lockbox** possuem `LOCKBOX_ID` preenchido, permitindo rastrear a origem da importação.
- O campo `RECEIPT_CLASS_ID` identifica a classe do recebimento (e.g., cheque, transferência, boleto).

---

## 🔗 PVOs Relacionados

### [[adjustmentdistributionpvo|AdjustmentDistributionPVO]] (AR · BICC: 2/92)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUTO_PRINT_PROGRAM_ID | ReceiptBatch1AutoPrintProgramId | — |
| AUTO_PRINT_PROGRAM_ID | ReceiptBatchAutoPrintProgramId | — |
| AUTO_TRANS_PROGRAM_ID | ReceiptBatch1AutoTransProgramId | — |
| AUTO_TRANS_PROGRAM_ID | ReceiptBatchAutoTransProgramId | — |
| BANK_DEPOSIT_NUMBER | ReceiptBatch1BankDepositNumber | — |
| BANK_DEPOSIT_NUMBER | ReceiptBatchBankDepositNumber | — |
| BATCH_APPLIED_STATUS | ReceiptBatch1BatchAppliedStatus | — |
| BATCH_APPLIED_STATUS | ReceiptBatchBatchAppliedStatus | — |
| BATCH_DATE | ReceiptBatch1BatchDate | — |
| BATCH_DATE | ReceiptBatchBatchDate | — |
| BATCH_ID | ReceiptBatch1BatchId | — |
| BATCH_ID | ReceiptBatchBatchId | — |
| BATCH_SOURCE_SEQ_ID | ReceiptBatch1BatchSourceSeqId | — |
| BATCH_SOURCE_SEQ_ID | ReceiptBatchBatchSourceSeqId | — |
| CLOSED_DATE | ReceiptBatch1ClosedDate | — |
| CLOSED_DATE | ReceiptBatchClosedDate | — |
| CONTROL_AMOUNT | ReceiptBatch1ControlAmount | — |
| CONTROL_AMOUNT | ReceiptBatchControlAmount | — |
| CONTROL_COUNT | ReceiptBatch1ControlCount | — |
| CONTROL_COUNT | ReceiptBatchControlCount | — |
| CREATED_BY | ReceiptBatch1CreatedBy | — |
| CREATED_BY | ReceiptBatchCreatedBy | — |
| CREATION_DATE | ReceiptBatch1CreationDate | — |
| CREATION_DATE | ReceiptBatchCreationDate | — |
| CURRENCY_CODE | ReceiptBatch1CurrencyCode | — |
| CURRENCY_CODE | ReceiptBatchCurrencyCode | — |
| DEPOSIT_DATE | ReceiptBatch1DepositDate | — |
| DEPOSIT_DATE | ReceiptBatchDepositDate | — |
| EXCHANGE_DATE | ReceiptBatch1ExchangeDate | — |
| EXCHANGE_DATE | ReceiptBatchExchangeDate | — |
| EXCHANGE_RATE | ReceiptBatch1ExchangeRate | — |
| EXCHANGE_RATE | ReceiptBatchExchangeRate | — |
| EXCHANGE_RATE_TYPE | ReceiptBatch1ExchangeRateType | — |
| EXCHANGE_RATE_TYPE | ReceiptBatchExchangeRateType | — |
| GL_DATE | ReceiptBatch1GlDate | — |
| GL_DATE | ReceiptBatchGlDate | — |
| LAST_UPDATE_DATE | ReceiptBatch1LastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ReceiptBatchLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ReceiptBatch1LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ReceiptBatchLastUpdateLogin | — |
| LAST_UPDATED_BY | ReceiptBatch1LastUpdatedBy | — |
| LAST_UPDATED_BY | ReceiptBatchLastUpdatedBy | — |
| LOCKBOX_BATCH_NAME | ReceiptBatch1LockboxBatchName | — |
| LOCKBOX_BATCH_NAME | ReceiptBatchLockboxBatchName | — |
| LOCKBOX_ID | ReceiptBatch1LockboxId | — |
| LOCKBOX_ID | ReceiptBatchLockboxId | — |
| MEDIA_REFERENCE | ReceiptBatch1MediaReference | — |
| MEDIA_REFERENCE | ReceiptBatchMediaReference | — |
| NAME | ReceiptBatch1Name | — |
| NAME | ReceiptBatchName | — |
| OBJECT_VERSION_NUMBER | ReceiptBatch1ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ReceiptBatchObjectVersionNumber | — |
| OLD_REMITTANCE_BANK_BRANCH_ID | ReceiptBatch1OldRemittanceBankBranchId | — |
| OLD_REMITTANCE_BANK_BRANCH_ID | ReceiptBatchOldRemittanceBankBranchId | — |
| OPERATION_REQUEST_ID | ReceiptBatch1OperationRequestId | — |
| OPERATION_REQUEST_ID | ReceiptBatchOperationRequestId | — |
| ORG_ID | ReceiptBatch1OrgId | — |
| ORG_ID | ReceiptBatchOrgId | — |
| PROGRAM_APPLICATION_ID | ReceiptBatch1ProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | ReceiptBatchProgramApplicationId | — |
| PROGRAM_ID | ReceiptBatch1ProgramId | — |
| PROGRAM_ID | ReceiptBatchProgramId | — |
| PROGRAM_UPDATE_DATE | ReceiptBatch1ProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | ReceiptBatchProgramUpdateDate | — |
| PURGED_CHILDREN_FLAG | ReceiptBatch1PurgedChildrenFlag | — |
| PURGED_CHILDREN_FLAG | ReceiptBatchPurgedChildrenFlag | — |
| RECEIPT_CLASS_ID | ReceiptBatch1ReceiptClassId | — |
| RECEIPT_CLASS_ID | ReceiptBatchReceiptClassId | — |
| RECEIPT_METHOD_ID | ReceiptBatch1ReceiptMethodId | — |
| RECEIPT_METHOD_ID | ReceiptBatchReceiptMethodId | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptBatch1RemitBankAcctUseId | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptBatchRemitBankAcctUseId | — |
| REMIT_METHOD_CODE | ReceiptBatch1RemitMethodCode | — |
| REMIT_METHOD_CODE | ReceiptBatchRemitMethodCode | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptBatch1RemittanceBankAccountId | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptBatchRemittanceBankAccountId | — |
| REMITTANCE_BANK_BRANCH_ID | ReceiptBatch1RemittanceBankBranchId | — |
| REMITTANCE_BANK_BRANCH_ID | ReceiptBatchRemittanceBankBranchId | — |
| REQUEST_ID | ReceiptBatch1RequestId | — |
| REQUEST_ID | ReceiptBatchRequestId | — |
| SET_OF_BOOKS_ID | ReceiptBatch1SetOfBooksId | — |
| SET_OF_BOOKS_ID | ReceiptBatchSetOfBooksId | — |
| STATUS | ReceiptBatch1Status | — |
| STATUS | ReceiptBatchStatus | — |
| TRANSMISSION_ID | ReceiptBatch1TransmissionId | — |
| TRANSMISSION_ID | ReceiptBatchTransmissionId | — |
| TRANSMISSION_REQUEST_ID | ReceiptBatch1TransmissionRequestId | — |
| TRANSMISSION_REQUEST_ID | ReceiptBatchTransmissionRequestId | — |
| TYPE | ReceiptBatch1Type | — |
| TYPE | ReceiptBatchType | — |
| WITH_RECOURSE_FLAG | ReceiptBatch1WithRecourseFlag | — |
| WITH_RECOURSE_FLAG | ReceiptBatchWithRecourseFlag | — |

### [[completedtrxrevadjdistributionpvo|CompletedTrxRevAdjDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUTO_PRINT_PROGRAM_ID | ReceiptBatch1AutoPrintProgramId | — |
| AUTO_PRINT_PROGRAM_ID | ReceiptBatchAutoPrintProgramId | — |
| AUTO_TRANS_PROGRAM_ID | ReceiptBatch1AutoTransProgramId | — |
| AUTO_TRANS_PROGRAM_ID | ReceiptBatchAutoTransProgramId | — |
| BANK_DEPOSIT_NUMBER | ReceiptBatch1BankDepositNumber | — |
| BANK_DEPOSIT_NUMBER | ReceiptBatchBankDepositNumber | — |
| BATCH_APPLIED_STATUS | ReceiptBatch1BatchAppliedStatus | — |
| BATCH_APPLIED_STATUS | ReceiptBatchBatchAppliedStatus | — |
| BATCH_DATE | ReceiptBatch1BatchDate | — |
| BATCH_DATE | ReceiptBatchBatchDate | — |
| BATCH_ID | ReceiptBatch1BatchId | — |
| BATCH_ID | ReceiptBatchBatchId | — |
| BATCH_SOURCE_SEQ_ID | ReceiptBatch1BatchSourceSeqId | — |
| BATCH_SOURCE_SEQ_ID | ReceiptBatchBatchSourceSeqId | — |
| CLOSED_DATE | ReceiptBatch1ClosedDate | — |
| CLOSED_DATE | ReceiptBatchClosedDate | — |
| CONTROL_AMOUNT | ReceiptBatch1ControlAmount | — |
| CONTROL_AMOUNT | ReceiptBatchControlAmount | — |
| CONTROL_COUNT | ReceiptBatch1ControlCount | — |
| CONTROL_COUNT | ReceiptBatchControlCount | — |
| CURRENCY_CODE | ReceiptBatch1CurrencyCode | — |
| CURRENCY_CODE | ReceiptBatchCurrencyCode | — |
| DEPOSIT_DATE | ReceiptBatch1DepositDate | — |
| DEPOSIT_DATE | ReceiptBatchDepositDate | — |
| EXCHANGE_DATE | ReceiptBatch1ExchangeDate | — |
| EXCHANGE_DATE | ReceiptBatchExchangeDate | — |
| EXCHANGE_RATE | ReceiptBatch1ExchangeRate | — |
| EXCHANGE_RATE | ReceiptBatchExchangeRate | — |
| EXCHANGE_RATE_TYPE | ReceiptBatch1ExchangeRateType | — |
| EXCHANGE_RATE_TYPE | ReceiptBatchExchangeRateType | — |
| GL_DATE | ReceiptBatch1GlDate | — |
| GL_DATE | ReceiptBatchGlDate | — |
| LOCKBOX_BATCH_NAME | ReceiptBatch1LockboxBatchName | — |
| LOCKBOX_BATCH_NAME | ReceiptBatchLockboxBatchName | — |
| LOCKBOX_ID | ReceiptBatch1LockboxId | — |
| LOCKBOX_ID | ReceiptBatchLockboxId | — |
| MEDIA_REFERENCE | ReceiptBatch1MediaReference | — |
| MEDIA_REFERENCE | ReceiptBatchMediaReference | — |
| NAME | ReceiptBatch1Name | — |
| NAME | ReceiptBatchName | — |
| OLD_REMITTANCE_BANK_BRANCH_ID | ReceiptBatch1OldRemittanceBankBranchId | — |
| OLD_REMITTANCE_BANK_BRANCH_ID | ReceiptBatchOldRemittanceBankBranchId | — |
| OPERATION_REQUEST_ID | ReceiptBatch1OperationRequestId | — |
| OPERATION_REQUEST_ID | ReceiptBatchOperationRequestId | — |
| ORG_ID | ReceiptBatch1OrgId | — |
| ORG_ID | ReceiptBatchOrgId | — |
| PROGRAM_APPLICATION_ID | ReceiptBatch1ProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | ReceiptBatchProgramApplicationId | — |
| PROGRAM_ID | ReceiptBatch1ProgramId | — |
| PROGRAM_ID | ReceiptBatchProgramId | — |
| PROGRAM_UPDATE_DATE | ReceiptBatch1ProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | ReceiptBatchProgramUpdateDate | — |
| PURGED_CHILDREN_FLAG | ReceiptBatch1PurgedChildrenFlag | — |
| PURGED_CHILDREN_FLAG | ReceiptBatchPurgedChildrenFlag | — |
| RECEIPT_CLASS_ID | ReceiptBatch1ReceiptClassId | — |
| RECEIPT_CLASS_ID | ReceiptBatchReceiptClassId | — |
| RECEIPT_METHOD_ID | ReceiptBatch1ReceiptMethodId | — |
| RECEIPT_METHOD_ID | ReceiptBatchReceiptMethodId | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptBatch1RemitBankAcctUseId | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptBatchRemitBankAcctUseId | — |
| REMIT_METHOD_CODE | ReceiptBatch1RemitMethodCode | — |
| REMIT_METHOD_CODE | ReceiptBatchRemitMethodCode | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptBatch1RemittanceBankAccountId | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptBatchRemittanceBankAccountId | — |
| REMITTANCE_BANK_BRANCH_ID | ReceiptBatch1RemittanceBankBranchId | — |
| REMITTANCE_BANK_BRANCH_ID | ReceiptBatchRemittanceBankBranchId | — |
| REQUEST_ID | ReceiptBatch1RequestId | — |
| REQUEST_ID | ReceiptBatchRequestId | — |
| SET_OF_BOOKS_ID | ReceiptBatch1SetOfBooksId | — |
| SET_OF_BOOKS_ID | ReceiptBatchSetOfBooksId | — |
| STATUS | ReceiptBatch1Status | — |
| STATUS | ReceiptBatchStatus | — |
| TRANSMISSION_ID | ReceiptBatch1TransmissionId | — |
| TRANSMISSION_ID | ReceiptBatchTransmissionId | — |
| TRANSMISSION_REQUEST_ID | ReceiptBatch1TransmissionRequestId | — |
| TRANSMISSION_REQUEST_ID | ReceiptBatchTransmissionRequestId | — |
| TYPE | ReceiptBatch1Type | — |
| TYPE | ReceiptBatchType | — |
| WITH_RECOURSE_FLAG | ReceiptBatch1WithRecourseFlag | — |
| WITH_RECOURSE_FLAG | ReceiptBatchWithRecourseFlag | — |

### [[completedtrxrevenuedistributionpvo|CompletedTrxRevenueDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUTO_PRINT_PROGRAM_ID | ReceiptBatchAutoPrintProgramId | — |
| AUTO_TRANS_PROGRAM_ID | ReceiptBatchAutoTransProgramId | — |
| BANK_DEPOSIT_NUMBER | ReceiptBatchBankDepositNumber | — |
| BATCH_APPLIED_STATUS | ReceiptBatchBatchAppliedStatus | — |
| BATCH_DATE | ReceiptBatchBatchDate | — |
| BATCH_ID | ReceiptBatchBatchId | — |
| BATCH_SOURCE_SEQ_ID | ReceiptBatchBatchSourceSeqId | — |
| CLOSED_DATE | ReceiptBatchClosedDate | — |
| CONTROL_AMOUNT | ReceiptBatchControlAmount | — |
| CONTROL_COUNT | ReceiptBatchControlCount | — |
| CURRENCY_CODE | ReceiptBatchCurrencyCode | — |
| DEPOSIT_DATE | ReceiptBatchDepositDate | — |
| EXCHANGE_DATE | ReceiptBatchExchangeDate | — |
| EXCHANGE_RATE | ReceiptBatchExchangeRate | — |
| EXCHANGE_RATE_TYPE | ReceiptBatchExchangeRateType | — |
| GL_DATE | ReceiptBatchGlDate | — |
| LOCKBOX_BATCH_NAME | ReceiptBatchLockboxBatchName | — |
| LOCKBOX_ID | ReceiptBatchLockboxId | — |
| MEDIA_REFERENCE | ReceiptBatchMediaReference | — |
| NAME | ReceiptBatchName | — |
| OLD_REMITTANCE_BANK_BRANCH_ID | ReceiptBatchOldRemittanceBankBranchId | — |
| OPERATION_REQUEST_ID | ReceiptBatchOperationRequestId | — |
| ORG_ID | ReceiptBatchOrgId | — |
| PROGRAM_APPLICATION_ID | ReceiptBatchProgramApplicationId | — |
| PROGRAM_ID | ReceiptBatchProgramId | — |
| PROGRAM_UPDATE_DATE | ReceiptBatchProgramUpdateDate | — |
| PURGED_CHILDREN_FLAG | ReceiptBatchPurgedChildrenFlag | — |
| RECEIPT_CLASS_ID | ReceiptBatchReceiptClassId | — |
| RECEIPT_METHOD_ID | ReceiptBatchReceiptMethodId | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptBatchRemitBankAcctUseId | — |
| REMIT_METHOD_CODE | ReceiptBatchRemitMethodCode | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptBatchRemittanceBankAccountId | — |
| REMITTANCE_BANK_BRANCH_ID | ReceiptBatchRemittanceBankBranchId | — |
| REQUEST_ID | ReceiptBatchRequestId | — |
| SET_OF_BOOKS_ID | ReceiptBatchSetOfBooksId | — |
| STATUS | ReceiptBatchStatus | — |
| TRANSMISSION_ID | ReceiptBatchTransmissionId | — |
| TRANSMISSION_REQUEST_ID | ReceiptBatchTransmissionRequestId | — |
| TYPE | ReceiptBatchType | — |
| WITH_RECOURSE_FLAG | ReceiptBatchWithRecourseFlag | — |

### [[creditmemoapplicationdistributionpvo|CreditMemoApplicationDistributionPVO]] (AR · BICC: 1/46)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUTO_PRINT_PROGRAM_ID | ReceiptBatchAutoPrintProgramId | — |
| AUTO_TRANS_PROGRAM_ID | ReceiptBatchAutoTransProgramId | — |
| BANK_DEPOSIT_NUMBER | ReceiptBatchBankDepositNumber | — |
| BATCH_APPLIED_STATUS | ReceiptBatchBatchAppliedStatus | — |
| BATCH_DATE | ReceiptBatchBatchDate | — |
| BATCH_ID | ReceiptBatchBatchId | — |
| BATCH_SOURCE_SEQ_ID | ReceiptBatchBatchSourceSeqId | — |
| CLOSED_DATE | ReceiptBatchClosedDate | — |
| CONTROL_AMOUNT | ReceiptBatchControlAmount | — |
| CONTROL_COUNT | ReceiptBatchControlCount | — |
| CREATED_BY | ReceiptBatchCreatedBy | — |
| CREATION_DATE | ReceiptBatchCreationDate | — |
| CURRENCY_CODE | ReceiptBatchCurrencyCode | — |
| DEPOSIT_DATE | ReceiptBatchDepositDate | — |
| EXCHANGE_DATE | ReceiptBatchExchangeDate | — |
| EXCHANGE_RATE | ReceiptBatchExchangeRate | — |
| EXCHANGE_RATE_TYPE | ReceiptBatchExchangeRateType | — |
| GL_DATE | ReceiptBatchGlDate | — |
| LAST_UPDATE_DATE | ReceiptBatchLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ReceiptBatchLastUpdateLogin | — |
| LAST_UPDATED_BY | ReceiptBatchLastUpdatedBy | — |
| LOCKBOX_BATCH_NAME | ReceiptBatchLockboxBatchName | — |
| LOCKBOX_ID | ReceiptBatchLockboxId | — |
| MEDIA_REFERENCE | ReceiptBatchMediaReference | — |
| NAME | ReceiptBatchName | — |
| OBJECT_VERSION_NUMBER | ReceiptBatchObjectVersionNumber | — |
| OLD_REMITTANCE_BANK_BRANCH_ID | ReceiptBatchOldRemittanceBankBranchId | — |
| OPERATION_REQUEST_ID | ReceiptBatchOperationRequestId | — |
| ORG_ID | ReceiptBatchOrgId | — |
| PROGRAM_APPLICATION_ID | ReceiptBatchProgramApplicationId | — |
| PROGRAM_ID | ReceiptBatchProgramId | — |
| PROGRAM_UPDATE_DATE | ReceiptBatchProgramUpdateDate | — |
| PURGED_CHILDREN_FLAG | ReceiptBatchPurgedChildrenFlag | — |
| RECEIPT_CLASS_ID | ReceiptBatchReceiptClassId | — |
| RECEIPT_METHOD_ID | ReceiptBatchReceiptMethodId | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptBatchRemitBankAcctUseId | — |
| REMIT_METHOD_CODE | ReceiptBatchRemitMethodCode | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptBatchRemittanceBankAccountId | — |
| REMITTANCE_BANK_BRANCH_ID | ReceiptBatchRemittanceBankBranchId | — |
| REQUEST_ID | ReceiptBatchRequestId | — |
| SET_OF_BOOKS_ID | ReceiptBatchSetOfBooksId | — |
| STATUS | ReceiptBatchStatus | — |
| TRANSMISSION_ID | ReceiptBatchTransmissionId | — |
| TRANSMISSION_REQUEST_ID | ReceiptBatchTransmissionRequestId | — |
| TYPE | ReceiptBatchType | — |
| WITH_RECOURSE_FLAG | ReceiptBatchWithRecourseFlag | — |

### [[headersalescreditpvo|HeaderSalesCreditPVO]] (AR · BICC: 1/46)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUTO_PRINT_PROGRAM_ID | ReceiptBatchAutoPrintProgramId | — |
| AUTO_TRANS_PROGRAM_ID | ReceiptBatchAutoTransProgramId | — |
| BANK_DEPOSIT_NUMBER | ReceiptBatchBankDepositNumber | — |
| BATCH_APPLIED_STATUS | ReceiptBatchBatchAppliedStatus | — |
| BATCH_DATE | ReceiptBatchBatchDate | — |
| BATCH_ID | ReceiptBatchBatchId | — |
| BATCH_SOURCE_SEQ_ID | ReceiptBatchBatchSourceSeqId | — |
| CLOSED_DATE | ReceiptBatchClosedDate | — |
| CONTROL_AMOUNT | ReceiptBatchControlAmount | — |
| CONTROL_COUNT | ReceiptBatchControlCount | — |
| CREATED_BY | ReceiptBatchCreatedBy | — |
| CREATION_DATE | ReceiptBatchCreationDate | — |
| CURRENCY_CODE | ReceiptBatchCurrencyCode | — |
| DEPOSIT_DATE | ReceiptBatchDepositDate | — |
| EXCHANGE_DATE | ReceiptBatchExchangeDate | — |
| EXCHANGE_RATE | ReceiptBatchExchangeRate | — |
| EXCHANGE_RATE_TYPE | ReceiptBatchExchangeRateType | — |
| GL_DATE | ReceiptBatchGlDate | — |
| LAST_UPDATE_DATE | ReceiptBatchLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ReceiptBatchLastUpdateLogin | — |
| LAST_UPDATED_BY | ReceiptBatchLastUpdatedBy | — |
| LOCKBOX_BATCH_NAME | ReceiptBatchLockboxBatchName | — |
| LOCKBOX_ID | ReceiptBatchLockboxId | — |
| MEDIA_REFERENCE | ReceiptBatchMediaReference | — |
| NAME | ReceiptBatchName | — |
| OBJECT_VERSION_NUMBER | ReceiptBatchObjectVersionNumber | — |
| OLD_REMITTANCE_BANK_BRANCH_ID | ReceiptBatchOldRemittanceBankBranchId | — |
| OPERATION_REQUEST_ID | ReceiptBatchOperationRequestId | — |
| ORG_ID | ReceiptBatchOrgId | — |
| PROGRAM_APPLICATION_ID | ReceiptBatchProgramApplicationId | — |
| PROGRAM_ID | ReceiptBatchProgramId | — |
| PROGRAM_UPDATE_DATE | ReceiptBatchProgramUpdateDate | — |
| PURGED_CHILDREN_FLAG | ReceiptBatchPurgedChildrenFlag | — |
| RECEIPT_CLASS_ID | ReceiptBatchReceiptClassId | — |
| RECEIPT_METHOD_ID | ReceiptBatchReceiptMethodId | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptBatchRemitBankAcctUseId | — |
| REMIT_METHOD_CODE | ReceiptBatchRemitMethodCode | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptBatchRemittanceBankAccountId | — |
| REMITTANCE_BANK_BRANCH_ID | ReceiptBatchRemittanceBankBranchId | — |
| REQUEST_ID | ReceiptBatchRequestId | — |
| SET_OF_BOOKS_ID | ReceiptBatchSetOfBooksId | — |
| STATUS | ReceiptBatchStatus | — |
| TRANSMISSION_ID | ReceiptBatchTransmissionId | — |
| TRANSMISSION_REQUEST_ID | ReceiptBatchTransmissionRequestId | — |
| TYPE | ReceiptBatchType | — |
| WITH_RECOURSE_FLAG | ReceiptBatchWithRecourseFlag | — |

### [[linesalescreditpvo|LineSalesCreditPVO]] (AR · BICC: 1/46)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUTO_PRINT_PROGRAM_ID | ReceiptBatchAutoPrintProgramId | — |
| AUTO_TRANS_PROGRAM_ID | ReceiptBatchAutoTransProgramId | — |
| BANK_DEPOSIT_NUMBER | ReceiptBatchBankDepositNumber | — |
| BATCH_APPLIED_STATUS | ReceiptBatchBatchAppliedStatus | — |
| BATCH_DATE | ReceiptBatchBatchDate | — |
| BATCH_ID | ReceiptBatchBatchId | — |
| BATCH_SOURCE_SEQ_ID | ReceiptBatchBatchSourceSeqId | — |
| CLOSED_DATE | ReceiptBatchClosedDate | — |
| CONTROL_AMOUNT | ReceiptBatchControlAmount | — |
| CONTROL_COUNT | ReceiptBatchControlCount | — |
| CREATED_BY | ReceiptBatchCreatedBy | — |
| CREATION_DATE | ReceiptBatchCreationDate | — |
| CURRENCY_CODE | ReceiptBatchCurrencyCode | — |
| DEPOSIT_DATE | ReceiptBatchDepositDate | — |
| EXCHANGE_DATE | ReceiptBatchExchangeDate | — |
| EXCHANGE_RATE | ReceiptBatchExchangeRate | — |
| EXCHANGE_RATE_TYPE | ReceiptBatchExchangeRateType | — |
| GL_DATE | ReceiptBatchGlDate | — |
| LAST_UPDATE_DATE | ReceiptBatchLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ReceiptBatchLastUpdateLogin | — |
| LAST_UPDATED_BY | ReceiptBatchLastUpdatedBy | — |
| LOCKBOX_BATCH_NAME | ReceiptBatchLockboxBatchName | — |
| LOCKBOX_ID | ReceiptBatchLockboxId | — |
| MEDIA_REFERENCE | ReceiptBatchMediaReference | — |
| NAME | ReceiptBatchName | — |
| OBJECT_VERSION_NUMBER | ReceiptBatchObjectVersionNumber | — |
| OLD_REMITTANCE_BANK_BRANCH_ID | ReceiptBatchOldRemittanceBankBranchId | — |
| OPERATION_REQUEST_ID | ReceiptBatchOperationRequestId | — |
| ORG_ID | ReceiptBatchOrgId | — |
| PROGRAM_APPLICATION_ID | ReceiptBatchProgramApplicationId | — |
| PROGRAM_ID | ReceiptBatchProgramId | — |
| PROGRAM_UPDATE_DATE | ReceiptBatchProgramUpdateDate | — |
| PURGED_CHILDREN_FLAG | ReceiptBatchPurgedChildrenFlag | — |
| RECEIPT_CLASS_ID | ReceiptBatchReceiptClassId | — |
| RECEIPT_METHOD_ID | ReceiptBatchReceiptMethodId | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptBatchRemitBankAcctUseId | — |
| REMIT_METHOD_CODE | ReceiptBatchRemitMethodCode | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptBatchRemittanceBankAccountId | — |
| REMITTANCE_BANK_BRANCH_ID | ReceiptBatchRemittanceBankBranchId | — |
| REQUEST_ID | ReceiptBatchRequestId | — |
| SET_OF_BOOKS_ID | ReceiptBatchSetOfBooksId | — |
| STATUS | ReceiptBatchStatus | — |
| TRANSMISSION_ID | ReceiptBatchTransmissionId | — |
| TRANSMISSION_REQUEST_ID | ReceiptBatchTransmissionRequestId | — |
| TYPE | ReceiptBatchType | — |
| WITH_RECOURSE_FLAG | ReceiptBatchWithRecourseFlag | — |

### [[miscreceiptdistributionpvo|MiscReceiptDistributionPVO]] (AR · BICC: 7/184)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUTO_PRINT_PROGRAM_ID | RcptRcptRefIdAutoPrintProgramId | — |
| AUTO_PRINT_PROGRAM_ID | RcptRcptRmitBatchAutoPrintProgramId | — |
| AUTO_PRINT_PROGRAM_ID | ReceiptBatchAutoPrintProgramId | — |
| AUTO_PRINT_PROGRAM_ID | RemittanceBatchAutoPrintProgramId | — |
| AUTO_TRANS_PROGRAM_ID | RcptRcptRefIdAutoTransProgramId | — |
| AUTO_TRANS_PROGRAM_ID | RcptRcptRmitBatchAutoTransProgramId | — |
| AUTO_TRANS_PROGRAM_ID | ReceiptBatchAutoTransProgramId | — |
| AUTO_TRANS_PROGRAM_ID | RemittanceBatchAutoTransProgramId | — |
| BANK_DEPOSIT_NUMBER | RcptRcptRefIdBankDepositNumber | — |
| BANK_DEPOSIT_NUMBER | RcptRcptRmitBatchBankDepositNumber | — |
| BANK_DEPOSIT_NUMBER | ReceiptBatchBankDepositNumber | — |
| BANK_DEPOSIT_NUMBER | RemittanceBatchBankDepositNumber | — |
| BATCH_APPLIED_STATUS | RcptRcptRefIdBatchAppliedStatus | — |
| BATCH_APPLIED_STATUS | RcptRcptRmitBatchBatchAppliedStatus | — |
| BATCH_APPLIED_STATUS | ReceiptBatchBatchAppliedStatus | — |
| BATCH_APPLIED_STATUS | RemittanceBatchBatchAppliedStatus | — |
| BATCH_DATE | RcptRcptRefIdBatchDate | — |
| BATCH_DATE | RcptRcptRmitBatchBatchDate | — |
| BATCH_DATE | ReceiptBatchBatchDate | — |
| BATCH_DATE | RemittanceBatchBatchDate | — |
| BATCH_ID | RcptRcptRefIdBatchId | — |
| BATCH_ID | RcptRcptRmitBatchBatchId | — |
| BATCH_ID | ReceiptBatchBatchId | ✅ |
| BATCH_ID | RemittanceBatchBatchId | — |
| BATCH_SOURCE_SEQ_ID | RcptRcptRefIdBatchSourceSeqId | — |
| BATCH_SOURCE_SEQ_ID | RcptRcptRmitBatchBatchSourceSeqId | — |
| BATCH_SOURCE_SEQ_ID | ReceiptBatchBatchSourceSeqId | — |
| BATCH_SOURCE_SEQ_ID | RemittanceBatchBatchSourceSeqId | — |
| CLOSED_DATE | RcptRcptRefIdClosedDate | — |
| CLOSED_DATE | RcptRcptRmitBatchClosedDate | — |
| CLOSED_DATE | ReceiptBatchClosedDate | — |
| CLOSED_DATE | RemittanceBatchClosedDate | — |
| CONTROL_AMOUNT | RcptRcptRefIdControlAmount | — |
| CONTROL_AMOUNT | RcptRcptRmitBatchControlAmount | — |
| CONTROL_AMOUNT | ReceiptBatchControlAmount | — |
| CONTROL_AMOUNT | RemittanceBatchControlAmount | — |
| CONTROL_COUNT | RcptRcptRefIdControlCount | — |
| CONTROL_COUNT | RcptRcptRmitBatchControlCount | — |
| CONTROL_COUNT | ReceiptBatchControlCount | — |
| CONTROL_COUNT | RemittanceBatchControlCount | — |
| CREATED_BY | RcptRcptRefIdCreatedBy | — |
| CREATED_BY | RcptRcptRmitBatchCreatedBy | — |
| CREATED_BY | ReceiptBatchCreatedBy | — |
| CREATED_BY | RemittanceBatchCreatedBy | — |
| CREATION_DATE | RcptRcptRefIdCreationDate | — |
| CREATION_DATE | RcptRcptRmitBatchCreationDate | — |
| CREATION_DATE | ReceiptBatchCreationDate | — |
| CREATION_DATE | RemittanceBatchCreationDate | — |
| CURRENCY_CODE | RcptRcptRefIdCurrencyCode | — |
| CURRENCY_CODE | RcptRcptRmitBatchCurrencyCode | — |
| CURRENCY_CODE | ReceiptBatchCurrencyCode | — |
| CURRENCY_CODE | RemittanceBatchCurrencyCode | — |
| DEPOSIT_DATE | RcptRcptRefIdDepositDate | — |
| DEPOSIT_DATE | RcptRcptRmitBatchDepositDate | — |
| DEPOSIT_DATE | ReceiptBatchDepositDate | — |
| DEPOSIT_DATE | RemittanceBatchDepositDate | — |
| EXCHANGE_DATE | RcptRcptRefIdExchangeDate | — |
| EXCHANGE_DATE | RcptRcptRmitBatchExchangeDate | — |
| EXCHANGE_DATE | ReceiptBatchExchangeDate | — |
| EXCHANGE_DATE | RemittanceBatchExchangeDate | — |
| EXCHANGE_RATE | RcptRcptRefIdExchangeRate | — |
| EXCHANGE_RATE | RcptRcptRmitBatchExchangeRate | — |
| EXCHANGE_RATE | ReceiptBatchExchangeRate | — |
| EXCHANGE_RATE | RemittanceBatchExchangeRate | — |
| EXCHANGE_RATE_TYPE | RcptRcptRefIdExchangeRateType | — |
| EXCHANGE_RATE_TYPE | RcptRcptRmitBatchExchangeRateType | — |
| EXCHANGE_RATE_TYPE | ReceiptBatchExchangeRateType | — |
| EXCHANGE_RATE_TYPE | RemittanceBatchExchangeRateType | — |
| GL_DATE | RcptRcptRefIdGlDate | — |
| GL_DATE | RcptRcptRmitBatchGlDate | — |
| GL_DATE | ReceiptBatchGlDate | — |
| GL_DATE | RemittanceBatchGlDate | — |
| LAST_UPDATE_DATE | RcptRcptRefIdLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | RcptRcptRmitBatchLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ReceiptBatchLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | RemittanceBatchLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RcptRcptRefIdLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | RcptRcptRmitBatchLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ReceiptBatchLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | RemittanceBatchLastUpdateLogin | — |
| LAST_UPDATED_BY | RcptRcptRefIdLastUpdatedBy | — |
| LAST_UPDATED_BY | RcptRcptRmitBatchLastUpdatedBy | — |
| LAST_UPDATED_BY | ReceiptBatchLastUpdatedBy | — |
| LAST_UPDATED_BY | RemittanceBatchLastUpdatedBy | — |
| LOCKBOX_BATCH_NAME | RcptRcptRefIdLockboxBatchName | — |
| LOCKBOX_BATCH_NAME | RcptRcptRmitBatchLockboxBatchName | — |
| LOCKBOX_BATCH_NAME | ReceiptBatchLockboxBatchName | — |
| LOCKBOX_BATCH_NAME | RemittanceBatchLockboxBatchName | — |
| LOCKBOX_ID | RcptRcptRefIdLockboxId | — |
| LOCKBOX_ID | RcptRcptRmitBatchLockboxId | — |
| LOCKBOX_ID | ReceiptBatchLockboxId | — |
| LOCKBOX_ID | RemittanceBatchLockboxId | — |
| MEDIA_REFERENCE | RcptRcptRefIdMediaReference | — |
| MEDIA_REFERENCE | RcptRcptRmitBatchMediaReference | — |
| MEDIA_REFERENCE | ReceiptBatchMediaReference | — |
| MEDIA_REFERENCE | RemittanceBatchMediaReference | — |
| NAME | RcptRcptRefIdName | — |
| NAME | RcptRcptRmitBatchName | — |
| NAME | ReceiptBatchName | ✅ |
| NAME | RemittanceBatchName | — |
| OBJECT_VERSION_NUMBER | RcptRcptRefIdObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | RcptRcptRmitBatchObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ReceiptBatchObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | RemittanceBatchObjectVersionNumber | — |
| OLD_REMITTANCE_BANK_BRANCH_ID | RcptRcptRefIdOldRemittanceBankBranchId | — |
| OLD_REMITTANCE_BANK_BRANCH_ID | RcptRcptRmitBatchOldRemittanceBankBranchId | — |
| OLD_REMITTANCE_BANK_BRANCH_ID | ReceiptBatchOldRemittanceBankBranchId | — |
| OLD_REMITTANCE_BANK_BRANCH_ID | RemittanceBatchOldRemittanceBankBranchId | — |
| OPERATION_REQUEST_ID | RcptRcptRefIdOperationRequestId | — |
| OPERATION_REQUEST_ID | RcptRcptRmitBatchOperationRequestId | — |
| OPERATION_REQUEST_ID | ReceiptBatchOperationRequestId | — |
| OPERATION_REQUEST_ID | RemittanceBatchOperationRequestId | — |
| ORG_ID | RcptRcptRefIdOrgId | — |
| ORG_ID | RcptRcptRmitBatchOrgId | — |
| ORG_ID | ReceiptBatchOrgId | — |
| ORG_ID | RemittanceBatchOrgId | — |
| PROGRAM_APPLICATION_ID | RcptRcptRefIdProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | RcptRcptRmitBatchProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | ReceiptBatchProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | RemittanceBatchProgramApplicationId | — |
| PROGRAM_ID | RcptRcptRefIdProgramId | — |
| PROGRAM_ID | RcptRcptRmitBatchProgramId | — |
| PROGRAM_ID | ReceiptBatchProgramId | — |
| PROGRAM_ID | RemittanceBatchProgramId | — |
| PROGRAM_UPDATE_DATE | RcptRcptRefIdProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | RcptRcptRmitBatchProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | ReceiptBatchProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | RemittanceBatchProgramUpdateDate | — |
| PURGED_CHILDREN_FLAG | RcptRcptRefIdPurgedChildrenFlag | — |
| PURGED_CHILDREN_FLAG | RcptRcptRmitBatchPurgedChildrenFlag | — |
| PURGED_CHILDREN_FLAG | ReceiptBatchPurgedChildrenFlag | — |
| PURGED_CHILDREN_FLAG | RemittanceBatchPurgedChildrenFlag | — |
| RECEIPT_CLASS_ID | RcptRcptRefIdReceiptClassId | — |
| RECEIPT_CLASS_ID | RcptRcptRmitBatchReceiptClassId | — |
| RECEIPT_CLASS_ID | ReceiptBatchReceiptClassId | — |
| RECEIPT_CLASS_ID | RemittanceBatchReceiptClassId | — |
| RECEIPT_METHOD_ID | RcptRcptRefIdReceiptMethodId | — |
| RECEIPT_METHOD_ID | RcptRcptRmitBatchReceiptMethodId | — |
| RECEIPT_METHOD_ID | ReceiptBatchReceiptMethodId | — |
| RECEIPT_METHOD_ID | RemittanceBatchReceiptMethodId | — |
| REMIT_BANK_ACCT_USE_ID | RcptRcptRefIdRemitBankAcctUseId | — |
| REMIT_BANK_ACCT_USE_ID | RcptRcptRmitBatchRemitBankAcctUseId | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptBatchRemitBankAcctUseId | — |
| REMIT_BANK_ACCT_USE_ID | RemittanceBatchRemitBankAcctUseId | — |
| REMIT_METHOD_CODE | RcptRcptRefIdRemitMethodCode | — |
| REMIT_METHOD_CODE | RcptRcptRmitBatchRemitMethodCode | — |
| REMIT_METHOD_CODE | ReceiptBatchRemitMethodCode | — |
| REMIT_METHOD_CODE | RemittanceBatchRemitMethodCode | — |
| REMITTANCE_BANK_ACCOUNT_ID | RcptRcptRefIdRemittanceBankAccountId | — |
| REMITTANCE_BANK_ACCOUNT_ID | RcptRcptRmitBatchRemittanceBankAccountId | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptBatchRemittanceBankAccountId | — |
| REMITTANCE_BANK_ACCOUNT_ID | RemittanceBatchRemittanceBankAccountId | — |
| REMITTANCE_BANK_BRANCH_ID | RcptRcptRefIdRemittanceBankBranchId | — |
| REMITTANCE_BANK_BRANCH_ID | RcptRcptRmitBatchRemittanceBankBranchId | — |
| REMITTANCE_BANK_BRANCH_ID | ReceiptBatchRemittanceBankBranchId | — |
| REMITTANCE_BANK_BRANCH_ID | RemittanceBatchRemittanceBankBranchId | — |
| REQUEST_ID | RcptRcptRefIdRequestId | — |
| REQUEST_ID | RcptRcptRmitBatchRequestId | — |
| REQUEST_ID | ReceiptBatchRequestId | — |
| REQUEST_ID | RemittanceBatchRequestId | — |
| SET_OF_BOOKS_ID | RcptRcptRefIdSetOfBooksId | — |
| SET_OF_BOOKS_ID | RcptRcptRmitBatchSetOfBooksId | — |
| SET_OF_BOOKS_ID | ReceiptBatchSetOfBooksId | — |
| SET_OF_BOOKS_ID | RemittanceBatchSetOfBooksId | — |
| STATUS | RcptRcptRefIdStatus | — |
| STATUS | RcptRcptRmitBatchStatus | — |
| STATUS | ReceiptBatchStatus | ✅ |
| STATUS | RemittanceBatchStatus | — |
| TRANSMISSION_ID | RcptRcptRefIdTransmissionId | — |
| TRANSMISSION_ID | RcptRcptRmitBatchTransmissionId | — |
| TRANSMISSION_ID | ReceiptBatchTransmissionId | — |
| TRANSMISSION_ID | RemittanceBatchTransmissionId | — |
| TRANSMISSION_REQUEST_ID | RcptRcptRefIdTransmissionRequestId | — |
| TRANSMISSION_REQUEST_ID | RcptRcptRmitBatchTransmissionRequestId | — |
| TRANSMISSION_REQUEST_ID | ReceiptBatchTransmissionRequestId | — |
| TRANSMISSION_REQUEST_ID | RemittanceBatchTransmissionRequestId | — |
| TYPE | RcptRcptRefIdType | — |
| TYPE | RcptRcptRmitBatchType | — |
| TYPE | ReceiptBatchType | — |
| TYPE | RemittanceBatchType | — |
| WITH_RECOURSE_FLAG | RcptRcptRefIdWithRecourseFlag | — |
| WITH_RECOURSE_FLAG | RcptRcptRmitBatchWithRecourseFlag | — |
| WITH_RECOURSE_FLAG | ReceiptBatchWithRecourseFlag | — |
| WITH_RECOURSE_FLAG | RemittanceBatchWithRecourseFlag | — |

### [[paymentschedulepvo|PaymentSchedulePVO]] (AR · BICC: 2/92)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUTO_PRINT_PROGRAM_ID | ReceiptBatchAutoPrintProgramId | — |
| AUTO_PRINT_PROGRAM_ID | ReceiptBatchSchedAutoPrintProgramId | — |
| AUTO_TRANS_PROGRAM_ID | ReceiptBatchAutoTransProgramId | — |
| AUTO_TRANS_PROGRAM_ID | ReceiptBatchSchedAutoTransProgramId | — |
| BANK_DEPOSIT_NUMBER | ReceiptBatchBankDepositNumber | — |
| BANK_DEPOSIT_NUMBER | ReceiptBatchSchedBankDepositNumber | — |
| BATCH_APPLIED_STATUS | ReceiptBatchBatchAppliedStatus | — |
| BATCH_APPLIED_STATUS | ReceiptBatchSchedBatchAppliedStatus | — |
| BATCH_DATE | ReceiptBatchBatchDate | — |
| BATCH_DATE | ReceiptBatchSchedBatchDate | — |
| BATCH_ID | ReceiptBatchBatchId | — |
| BATCH_ID | ReceiptBatchSchedBatchId | — |
| BATCH_SOURCE_SEQ_ID | ReceiptBatchBatchSourceSeqId | — |
| BATCH_SOURCE_SEQ_ID | ReceiptBatchSchedBatchSourceSeqId | — |
| CLOSED_DATE | ReceiptBatchClosedDate | — |
| CLOSED_DATE | ReceiptBatchSchedClosedDate | — |
| CONTROL_AMOUNT | ReceiptBatchControlAmount | — |
| CONTROL_AMOUNT | ReceiptBatchSchedControlAmount | — |
| CONTROL_COUNT | ReceiptBatchControlCount | — |
| CONTROL_COUNT | ReceiptBatchSchedControlCount | — |
| CREATED_BY | ReceiptBatchCreatedBy | — |
| CREATED_BY | ReceiptBatchSchedCreatedBy | — |
| CREATION_DATE | ReceiptBatchCreationDate | — |
| CREATION_DATE | ReceiptBatchSchedCreationDate | — |
| CURRENCY_CODE | ReceiptBatchCurrencyCode | — |
| CURRENCY_CODE | ReceiptBatchSchedCurrencyCode | — |
| DEPOSIT_DATE | ReceiptBatchDepositDate | — |
| DEPOSIT_DATE | ReceiptBatchSchedDepositDate | — |
| EXCHANGE_DATE | ReceiptBatchExchangeDate | — |
| EXCHANGE_DATE | ReceiptBatchSchedExchangeDate | — |
| EXCHANGE_RATE | ReceiptBatchExchangeRate | — |
| EXCHANGE_RATE | ReceiptBatchSchedExchangeRate | — |
| EXCHANGE_RATE_TYPE | ReceiptBatchExchangeRateType | — |
| EXCHANGE_RATE_TYPE | ReceiptBatchSchedExchangeRateType | — |
| GL_DATE | ReceiptBatchGlDate | — |
| GL_DATE | ReceiptBatchSchedGlDate | — |
| LAST_UPDATE_DATE | ReceiptBatchLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ReceiptBatchSchedLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ReceiptBatchLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ReceiptBatchSchedLastUpdateLogin | — |
| LAST_UPDATED_BY | ReceiptBatchLastUpdatedBy | — |
| LAST_UPDATED_BY | ReceiptBatchSchedLastUpdatedBy | — |
| LOCKBOX_BATCH_NAME | ReceiptBatchLockboxBatchName | — |
| LOCKBOX_BATCH_NAME | ReceiptBatchSchedLockboxBatchName | — |
| LOCKBOX_ID | ReceiptBatchLockboxId | — |
| LOCKBOX_ID | ReceiptBatchSchedLockboxId | — |
| MEDIA_REFERENCE | ReceiptBatchMediaReference | — |
| MEDIA_REFERENCE | ReceiptBatchSchedMediaReference | — |
| NAME | ReceiptBatchName | — |
| NAME | ReceiptBatchSchedName | — |
| OBJECT_VERSION_NUMBER | ReceiptBatchObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ReceiptBatchSchedObjectVersionNumber | — |
| OLD_REMITTANCE_BANK_BRANCH_ID | ReceiptBatchOldRemittanceBankBranchId | — |
| OLD_REMITTANCE_BANK_BRANCH_ID | ReceiptBatchSchedOldRemittanceBankBranchId | — |
| OPERATION_REQUEST_ID | ReceiptBatchOperationRequestId | — |
| OPERATION_REQUEST_ID | ReceiptBatchSchedOperationRequestId | — |
| ORG_ID | ReceiptBatchOrgId | — |
| ORG_ID | ReceiptBatchSchedOrgId | — |
| PROGRAM_APPLICATION_ID | ReceiptBatchProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | ReceiptBatchSchedProgramApplicationId | — |
| PROGRAM_ID | ReceiptBatchProgramId | — |
| PROGRAM_ID | ReceiptBatchSchedProgramId | — |
| PROGRAM_UPDATE_DATE | ReceiptBatchProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | ReceiptBatchSchedProgramUpdateDate | — |
| PURGED_CHILDREN_FLAG | ReceiptBatchPurgedChildrenFlag | — |
| PURGED_CHILDREN_FLAG | ReceiptBatchSchedPurgedChildrenFlag | — |
| RECEIPT_CLASS_ID | ReceiptBatchReceiptClassId | — |
| RECEIPT_CLASS_ID | ReceiptBatchSchedReceiptClassId | — |
| RECEIPT_METHOD_ID | ReceiptBatchReceiptMethodId | — |
| RECEIPT_METHOD_ID | ReceiptBatchSchedReceiptMethodId | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptBatchRemitBankAcctUseId | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptBatchSchedRemitBankAcctUseId | — |
| REMIT_METHOD_CODE | ReceiptBatchRemitMethodCode | — |
| REMIT_METHOD_CODE | ReceiptBatchSchedRemitMethodCode | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptBatchRemittanceBankAccountId | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptBatchSchedRemittanceBankAccountId | — |
| REMITTANCE_BANK_BRANCH_ID | ReceiptBatchRemittanceBankBranchId | — |
| REMITTANCE_BANK_BRANCH_ID | ReceiptBatchSchedRemittanceBankBranchId | — |
| REQUEST_ID | ReceiptBatchRequestId | — |
| REQUEST_ID | ReceiptBatchSchedRequestId | — |
| SET_OF_BOOKS_ID | ReceiptBatchSchedSetOfBooksId | — |
| SET_OF_BOOKS_ID | ReceiptBatchSetOfBooksId | — |
| STATUS | ReceiptBatchSchedStatus | — |
| STATUS | ReceiptBatchStatus | — |
| TRANSMISSION_ID | ReceiptBatchSchedTransmissionId | — |
| TRANSMISSION_ID | ReceiptBatchTransmissionId | — |
| TRANSMISSION_REQUEST_ID | ReceiptBatchSchedTransmissionRequestId | — |
| TRANSMISSION_REQUEST_ID | ReceiptBatchTransmissionRequestId | — |
| TYPE | ReceiptBatchSchedType | — |
| TYPE | ReceiptBatchType | — |
| WITH_RECOURSE_FLAG | ReceiptBatchSchedWithRecourseFlag | — |
| WITH_RECOURSE_FLAG | ReceiptBatchWithRecourseFlag | — |

### [[receiptapplicationdistributionpvo|ReceiptApplicationDistributionPVO]] (AR · BICC: 4/184)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUTO_PRINT_PROGRAM_ID | ReceiptBatchAutoPrintProgramId | — |
| AUTO_PRINT_PROGRAM_ID | ReceiptBatchHeaderAutoPrintProgramId | — |
| AUTO_PRINT_PROGRAM_ID | ReceiptBatchSchedAutoPrintProgramId | — |
| AUTO_PRINT_PROGRAM_ID | RemittanceBatchAutoPrintProgramId | — |
| AUTO_TRANS_PROGRAM_ID | ReceiptBatchAutoTransProgramId | — |
| AUTO_TRANS_PROGRAM_ID | ReceiptBatchHeaderAutoTransProgramId | — |
| AUTO_TRANS_PROGRAM_ID | ReceiptBatchSchedAutoTransProgramId | — |
| AUTO_TRANS_PROGRAM_ID | RemittanceBatchAutoTransProgramId | — |
| BANK_DEPOSIT_NUMBER | ReceiptBatchBankDepositNumber | — |
| BANK_DEPOSIT_NUMBER | ReceiptBatchHeaderBankDepositNumber | — |
| BANK_DEPOSIT_NUMBER | ReceiptBatchSchedBankDepositNumber | — |
| BANK_DEPOSIT_NUMBER | RemittanceBatchBankDepositNumber | — |
| BATCH_APPLIED_STATUS | ReceiptBatchBatchAppliedStatus | — |
| BATCH_APPLIED_STATUS | ReceiptBatchHeaderBatchAppliedStatus | — |
| BATCH_APPLIED_STATUS | ReceiptBatchSchedBatchAppliedStatus | — |
| BATCH_APPLIED_STATUS | RemittanceBatchBatchAppliedStatus | — |
| BATCH_DATE | ReceiptBatchBatchDate | — |
| BATCH_DATE | ReceiptBatchHeaderBatchDate | — |
| BATCH_DATE | ReceiptBatchSchedBatchDate | — |
| BATCH_DATE | RemittanceBatchBatchDate | — |
| BATCH_ID | ReceiptBatchBatchId | — |
| BATCH_ID | ReceiptBatchHeaderBatchId | — |
| BATCH_ID | ReceiptBatchSchedBatchId | — |
| BATCH_ID | RemittanceBatchBatchId | — |
| BATCH_SOURCE_SEQ_ID | ReceiptBatchBatchSourceSeqId | — |
| BATCH_SOURCE_SEQ_ID | ReceiptBatchHeaderBatchSourceSeqId | — |
| BATCH_SOURCE_SEQ_ID | ReceiptBatchSchedBatchSourceSeqId | — |
| BATCH_SOURCE_SEQ_ID | RemittanceBatchBatchSourceSeqId | — |
| CLOSED_DATE | ReceiptBatchClosedDate | — |
| CLOSED_DATE | ReceiptBatchHeaderClosedDate | — |
| CLOSED_DATE | ReceiptBatchSchedClosedDate | — |
| CLOSED_DATE | RemittanceBatchClosedDate | — |
| CONTROL_AMOUNT | ReceiptBatchControlAmount | — |
| CONTROL_AMOUNT | ReceiptBatchHeaderControlAmount | — |
| CONTROL_AMOUNT | ReceiptBatchSchedControlAmount | — |
| CONTROL_AMOUNT | RemittanceBatchControlAmount | — |
| CONTROL_COUNT | ReceiptBatchControlCount | — |
| CONTROL_COUNT | ReceiptBatchHeaderControlCount | — |
| CONTROL_COUNT | ReceiptBatchSchedControlCount | — |
| CONTROL_COUNT | RemittanceBatchControlCount | — |
| CREATED_BY | ReceiptBatchCreatedBy | — |
| CREATED_BY | ReceiptBatchHeaderCreatedBy | — |
| CREATED_BY | ReceiptBatchSchedCreatedBy | — |
| CREATED_BY | RemittanceBatchCreatedBy | — |
| CREATION_DATE | ReceiptBatchCreationDate | — |
| CREATION_DATE | ReceiptBatchHeaderCreationDate | — |
| CREATION_DATE | ReceiptBatchSchedCreationDate | — |
| CREATION_DATE | RemittanceBatchCreationDate | — |
| CURRENCY_CODE | ReceiptBatchCurrencyCode | — |
| CURRENCY_CODE | ReceiptBatchHeaderCurrencyCode | — |
| CURRENCY_CODE | ReceiptBatchSchedCurrencyCode | — |
| CURRENCY_CODE | RemittanceBatchCurrencyCode | — |
| DEPOSIT_DATE | ReceiptBatchDepositDate | — |
| DEPOSIT_DATE | ReceiptBatchHeaderDepositDate | — |
| DEPOSIT_DATE | ReceiptBatchSchedDepositDate | — |
| DEPOSIT_DATE | RemittanceBatchDepositDate | — |
| EXCHANGE_DATE | ReceiptBatchExchangeDate | — |
| EXCHANGE_DATE | ReceiptBatchHeaderExchangeDate | — |
| EXCHANGE_DATE | ReceiptBatchSchedExchangeDate | — |
| EXCHANGE_DATE | RemittanceBatchExchangeDate | — |
| EXCHANGE_RATE | ReceiptBatchExchangeRate | — |
| EXCHANGE_RATE | ReceiptBatchHeaderExchangeRate | — |
| EXCHANGE_RATE | ReceiptBatchSchedExchangeRate | — |
| EXCHANGE_RATE | RemittanceBatchExchangeRate | — |
| EXCHANGE_RATE_TYPE | ReceiptBatchExchangeRateType | — |
| EXCHANGE_RATE_TYPE | ReceiptBatchHeaderExchangeRateType | — |
| EXCHANGE_RATE_TYPE | ReceiptBatchSchedExchangeRateType | — |
| EXCHANGE_RATE_TYPE | RemittanceBatchExchangeRateType | — |
| GL_DATE | ReceiptBatchGlDate | — |
| GL_DATE | ReceiptBatchHeaderGlDate | — |
| GL_DATE | ReceiptBatchSchedGlDate | — |
| GL_DATE | RemittanceBatchGlDate | — |
| LAST_UPDATE_DATE | ReceiptBatchHeaderLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ReceiptBatchLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ReceiptBatchSchedLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | RemittanceBatchLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ReceiptBatchHeaderLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ReceiptBatchLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ReceiptBatchSchedLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | RemittanceBatchLastUpdateLogin | — |
| LAST_UPDATED_BY | ReceiptBatchHeaderLastUpdatedBy | — |
| LAST_UPDATED_BY | ReceiptBatchLastUpdatedBy | — |
| LAST_UPDATED_BY | ReceiptBatchSchedLastUpdatedBy | — |
| LAST_UPDATED_BY | RemittanceBatchLastUpdatedBy | — |
| LOCKBOX_BATCH_NAME | ReceiptBatchHeaderLockboxBatchName | — |
| LOCKBOX_BATCH_NAME | ReceiptBatchLockboxBatchName | — |
| LOCKBOX_BATCH_NAME | ReceiptBatchSchedLockboxBatchName | — |
| LOCKBOX_BATCH_NAME | RemittanceBatchLockboxBatchName | — |
| LOCKBOX_ID | ReceiptBatchHeaderLockboxId | — |
| LOCKBOX_ID | ReceiptBatchLockboxId | — |
| LOCKBOX_ID | ReceiptBatchSchedLockboxId | — |
| LOCKBOX_ID | RemittanceBatchLockboxId | — |
| MEDIA_REFERENCE | ReceiptBatchHeaderMediaReference | — |
| MEDIA_REFERENCE | ReceiptBatchMediaReference | — |
| MEDIA_REFERENCE | ReceiptBatchSchedMediaReference | — |
| MEDIA_REFERENCE | RemittanceBatchMediaReference | — |
| NAME | ReceiptBatchHeaderName | — |
| NAME | ReceiptBatchName | — |
| NAME | ReceiptBatchSchedName | — |
| NAME | RemittanceBatchName | — |
| OBJECT_VERSION_NUMBER | ReceiptBatchHeaderObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ReceiptBatchObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ReceiptBatchSchedObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | RemittanceBatchObjectVersionNumber | — |
| OLD_REMITTANCE_BANK_BRANCH_ID | ReceiptBatchHeaderOldRemittanceBankBranchId | — |
| OLD_REMITTANCE_BANK_BRANCH_ID | ReceiptBatchOldRemittanceBankBranchId | — |
| OLD_REMITTANCE_BANK_BRANCH_ID | ReceiptBatchSchedOldRemittanceBankBranchId | — |
| OLD_REMITTANCE_BANK_BRANCH_ID | RemittanceBatchOldRemittanceBankBranchId | — |
| OPERATION_REQUEST_ID | ReceiptBatchHeaderOperationRequestId | — |
| OPERATION_REQUEST_ID | ReceiptBatchOperationRequestId | — |
| OPERATION_REQUEST_ID | ReceiptBatchSchedOperationRequestId | — |
| OPERATION_REQUEST_ID | RemittanceBatchOperationRequestId | — |
| ORG_ID | ReceiptBatchHeaderOrgId | — |
| ORG_ID | ReceiptBatchOrgId | — |
| ORG_ID | ReceiptBatchSchedOrgId | — |
| ORG_ID | RemittanceBatchOrgId | — |
| PROGRAM_APPLICATION_ID | ReceiptBatchHeaderProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | ReceiptBatchProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | ReceiptBatchSchedProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | RemittanceBatchProgramApplicationId | — |
| PROGRAM_ID | ReceiptBatchHeaderProgramId | — |
| PROGRAM_ID | ReceiptBatchProgramId | — |
| PROGRAM_ID | ReceiptBatchSchedProgramId | — |
| PROGRAM_ID | RemittanceBatchProgramId | — |
| PROGRAM_UPDATE_DATE | ReceiptBatchHeaderProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | ReceiptBatchProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | ReceiptBatchSchedProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | RemittanceBatchProgramUpdateDate | — |
| PURGED_CHILDREN_FLAG | ReceiptBatchHeaderPurgedChildrenFlag | — |
| PURGED_CHILDREN_FLAG | ReceiptBatchPurgedChildrenFlag | — |
| PURGED_CHILDREN_FLAG | ReceiptBatchSchedPurgedChildrenFlag | — |
| PURGED_CHILDREN_FLAG | RemittanceBatchPurgedChildrenFlag | — |
| RECEIPT_CLASS_ID | ReceiptBatchHeaderReceiptClassId | — |
| RECEIPT_CLASS_ID | ReceiptBatchReceiptClassId | — |
| RECEIPT_CLASS_ID | ReceiptBatchSchedReceiptClassId | — |
| RECEIPT_CLASS_ID | RemittanceBatchReceiptClassId | — |
| RECEIPT_METHOD_ID | ReceiptBatchHeaderReceiptMethodId | — |
| RECEIPT_METHOD_ID | ReceiptBatchReceiptMethodId | — |
| RECEIPT_METHOD_ID | ReceiptBatchSchedReceiptMethodId | — |
| RECEIPT_METHOD_ID | RemittanceBatchReceiptMethodId | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptBatchHeaderRemitBankAcctUseId | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptBatchRemitBankAcctUseId | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptBatchSchedRemitBankAcctUseId | — |
| REMIT_BANK_ACCT_USE_ID | RemittanceBatchRemitBankAcctUseId | — |
| REMIT_METHOD_CODE | ReceiptBatchHeaderRemitMethodCode | — |
| REMIT_METHOD_CODE | ReceiptBatchRemitMethodCode | — |
| REMIT_METHOD_CODE | ReceiptBatchSchedRemitMethodCode | — |
| REMIT_METHOD_CODE | RemittanceBatchRemitMethodCode | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptBatchHeaderRemittanceBankAccountId | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptBatchRemittanceBankAccountId | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptBatchSchedRemittanceBankAccountId | — |
| REMITTANCE_BANK_ACCOUNT_ID | RemittanceBatchRemittanceBankAccountId | — |
| REMITTANCE_BANK_BRANCH_ID | ReceiptBatchHeaderRemittanceBankBranchId | — |
| REMITTANCE_BANK_BRANCH_ID | ReceiptBatchRemittanceBankBranchId | — |
| REMITTANCE_BANK_BRANCH_ID | ReceiptBatchSchedRemittanceBankBranchId | — |
| REMITTANCE_BANK_BRANCH_ID | RemittanceBatchRemittanceBankBranchId | — |
| REQUEST_ID | ReceiptBatchHeaderRequestId | — |
| REQUEST_ID | ReceiptBatchRequestId | — |
| REQUEST_ID | ReceiptBatchSchedRequestId | — |
| REQUEST_ID | RemittanceBatchRequestId | — |
| SET_OF_BOOKS_ID | ReceiptBatchHeaderSetOfBooksId | — |
| SET_OF_BOOKS_ID | ReceiptBatchSchedSetOfBooksId | — |
| SET_OF_BOOKS_ID | ReceiptBatchSetOfBooksId | — |
| SET_OF_BOOKS_ID | RemittanceBatchSetOfBooksId | — |
| STATUS | ReceiptBatchHeaderStatus | — |
| STATUS | ReceiptBatchSchedStatus | — |
| STATUS | ReceiptBatchStatus | — |
| STATUS | RemittanceBatchStatus | — |
| TRANSMISSION_ID | ReceiptBatchHeaderTransmissionId | — |
| TRANSMISSION_ID | ReceiptBatchSchedTransmissionId | — |
| TRANSMISSION_ID | ReceiptBatchTransmissionId | — |
| TRANSMISSION_ID | RemittanceBatchTransmissionId | — |
| TRANSMISSION_REQUEST_ID | ReceiptBatchHeaderTransmissionRequestId | — |
| TRANSMISSION_REQUEST_ID | ReceiptBatchSchedTransmissionRequestId | — |
| TRANSMISSION_REQUEST_ID | ReceiptBatchTransmissionRequestId | — |
| TRANSMISSION_REQUEST_ID | RemittanceBatchTransmissionRequestId | — |
| TYPE | ReceiptBatchHeaderType | — |
| TYPE | ReceiptBatchSchedType | — |
| TYPE | ReceiptBatchType | — |
| TYPE | RemittanceBatchType | — |
| WITH_RECOURSE_FLAG | ReceiptBatchHeaderWithRecourseFlag | — |
| WITH_RECOURSE_FLAG | ReceiptBatchSchedWithRecourseFlag | — |
| WITH_RECOURSE_FLAG | ReceiptBatchWithRecourseFlag | — |
| WITH_RECOURSE_FLAG | RemittanceBatchWithRecourseFlag | — |

### [[receiptapplicationdistributionvc|ReceiptApplicationDistributionVC]] (AR · BICC: 7/184)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUTO_PRINT_PROGRAM_ID | ReceiptBatchAutoPrintProgramId | — |
| AUTO_PRINT_PROGRAM_ID | ReceiptBatchHeaderAutoPrintProgramId | — |
| AUTO_PRINT_PROGRAM_ID | ReceiptBatchSchedAutoPrintProgramId | — |
| AUTO_PRINT_PROGRAM_ID | RemittanceBatchAutoPrintProgramId | — |
| AUTO_TRANS_PROGRAM_ID | ReceiptBatchAutoTransProgramId | — |
| AUTO_TRANS_PROGRAM_ID | ReceiptBatchHeaderAutoTransProgramId | — |
| AUTO_TRANS_PROGRAM_ID | ReceiptBatchSchedAutoTransProgramId | — |
| AUTO_TRANS_PROGRAM_ID | RemittanceBatchAutoTransProgramId | — |
| BANK_DEPOSIT_NUMBER | ReceiptBatchBankDepositNumber | — |
| BANK_DEPOSIT_NUMBER | ReceiptBatchHeaderBankDepositNumber | — |
| BANK_DEPOSIT_NUMBER | ReceiptBatchSchedBankDepositNumber | — |
| BANK_DEPOSIT_NUMBER | RemittanceBatchBankDepositNumber | — |
| BATCH_APPLIED_STATUS | ReceiptBatchBatchAppliedStatus | — |
| BATCH_APPLIED_STATUS | ReceiptBatchHeaderBatchAppliedStatus | — |
| BATCH_APPLIED_STATUS | ReceiptBatchSchedBatchAppliedStatus | — |
| BATCH_APPLIED_STATUS | RemittanceBatchBatchAppliedStatus | — |
| BATCH_DATE | ReceiptBatchBatchDate | — |
| BATCH_DATE | ReceiptBatchHeaderBatchDate | — |
| BATCH_DATE | ReceiptBatchSchedBatchDate | — |
| BATCH_DATE | RemittanceBatchBatchDate | — |
| BATCH_ID | ReceiptBatchBatchId | ✅ |
| BATCH_ID | ReceiptBatchHeaderBatchId | — |
| BATCH_ID | ReceiptBatchSchedBatchId | — |
| BATCH_ID | RemittanceBatchBatchId | — |
| BATCH_SOURCE_SEQ_ID | ReceiptBatchBatchSourceSeqId | — |
| BATCH_SOURCE_SEQ_ID | ReceiptBatchHeaderBatchSourceSeqId | — |
| BATCH_SOURCE_SEQ_ID | ReceiptBatchSchedBatchSourceSeqId | — |
| BATCH_SOURCE_SEQ_ID | RemittanceBatchBatchSourceSeqId | — |
| CLOSED_DATE | ReceiptBatchClosedDate | — |
| CLOSED_DATE | ReceiptBatchHeaderClosedDate | — |
| CLOSED_DATE | ReceiptBatchSchedClosedDate | — |
| CLOSED_DATE | RemittanceBatchClosedDate | — |
| CONTROL_AMOUNT | ReceiptBatchControlAmount | — |
| CONTROL_AMOUNT | ReceiptBatchHeaderControlAmount | — |
| CONTROL_AMOUNT | ReceiptBatchSchedControlAmount | — |
| CONTROL_AMOUNT | RemittanceBatchControlAmount | — |
| CONTROL_COUNT | ReceiptBatchControlCount | — |
| CONTROL_COUNT | ReceiptBatchHeaderControlCount | — |
| CONTROL_COUNT | ReceiptBatchSchedControlCount | — |
| CONTROL_COUNT | RemittanceBatchControlCount | — |
| CREATED_BY | ReceiptBatchCreatedBy | — |
| CREATED_BY | ReceiptBatchHeaderCreatedBy | — |
| CREATED_BY | ReceiptBatchSchedCreatedBy | — |
| CREATED_BY | RemittanceBatchCreatedBy | — |
| CREATION_DATE | ReceiptBatchCreationDate | — |
| CREATION_DATE | ReceiptBatchHeaderCreationDate | — |
| CREATION_DATE | ReceiptBatchSchedCreationDate | — |
| CREATION_DATE | RemittanceBatchCreationDate | — |
| CURRENCY_CODE | ReceiptBatchCurrencyCode | — |
| CURRENCY_CODE | ReceiptBatchHeaderCurrencyCode | — |
| CURRENCY_CODE | ReceiptBatchSchedCurrencyCode | — |
| CURRENCY_CODE | RemittanceBatchCurrencyCode | — |
| DEPOSIT_DATE | ReceiptBatchDepositDate | — |
| DEPOSIT_DATE | ReceiptBatchHeaderDepositDate | — |
| DEPOSIT_DATE | ReceiptBatchSchedDepositDate | — |
| DEPOSIT_DATE | RemittanceBatchDepositDate | — |
| EXCHANGE_DATE | ReceiptBatchExchangeDate | — |
| EXCHANGE_DATE | ReceiptBatchHeaderExchangeDate | — |
| EXCHANGE_DATE | ReceiptBatchSchedExchangeDate | — |
| EXCHANGE_DATE | RemittanceBatchExchangeDate | — |
| EXCHANGE_RATE | ReceiptBatchExchangeRate | — |
| EXCHANGE_RATE | ReceiptBatchHeaderExchangeRate | — |
| EXCHANGE_RATE | ReceiptBatchSchedExchangeRate | — |
| EXCHANGE_RATE | RemittanceBatchExchangeRate | — |
| EXCHANGE_RATE_TYPE | ReceiptBatchExchangeRateType | — |
| EXCHANGE_RATE_TYPE | ReceiptBatchHeaderExchangeRateType | — |
| EXCHANGE_RATE_TYPE | ReceiptBatchSchedExchangeRateType | — |
| EXCHANGE_RATE_TYPE | RemittanceBatchExchangeRateType | — |
| GL_DATE | ReceiptBatchGlDate | — |
| GL_DATE | ReceiptBatchHeaderGlDate | — |
| GL_DATE | ReceiptBatchSchedGlDate | — |
| GL_DATE | RemittanceBatchGlDate | — |
| LAST_UPDATE_DATE | ReceiptBatchHeaderLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ReceiptBatchLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ReceiptBatchSchedLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | RemittanceBatchLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ReceiptBatchHeaderLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ReceiptBatchLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ReceiptBatchSchedLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | RemittanceBatchLastUpdateLogin | — |
| LAST_UPDATED_BY | ReceiptBatchHeaderLastUpdatedBy | — |
| LAST_UPDATED_BY | ReceiptBatchLastUpdatedBy | — |
| LAST_UPDATED_BY | ReceiptBatchSchedLastUpdatedBy | — |
| LAST_UPDATED_BY | RemittanceBatchLastUpdatedBy | — |
| LOCKBOX_BATCH_NAME | ReceiptBatchHeaderLockboxBatchName | — |
| LOCKBOX_BATCH_NAME | ReceiptBatchLockboxBatchName | — |
| LOCKBOX_BATCH_NAME | ReceiptBatchSchedLockboxBatchName | — |
| LOCKBOX_BATCH_NAME | RemittanceBatchLockboxBatchName | — |
| LOCKBOX_ID | ReceiptBatchHeaderLockboxId | — |
| LOCKBOX_ID | ReceiptBatchLockboxId | — |
| LOCKBOX_ID | ReceiptBatchSchedLockboxId | — |
| LOCKBOX_ID | RemittanceBatchLockboxId | — |
| MEDIA_REFERENCE | ReceiptBatchHeaderMediaReference | — |
| MEDIA_REFERENCE | ReceiptBatchMediaReference | — |
| MEDIA_REFERENCE | ReceiptBatchSchedMediaReference | — |
| MEDIA_REFERENCE | RemittanceBatchMediaReference | — |
| NAME | ReceiptBatchHeaderName | — |
| NAME | ReceiptBatchName | ✅ |
| NAME | ReceiptBatchSchedName | — |
| NAME | RemittanceBatchName | — |
| OBJECT_VERSION_NUMBER | ReceiptBatchHeaderObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ReceiptBatchObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ReceiptBatchSchedObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | RemittanceBatchObjectVersionNumber | — |
| OLD_REMITTANCE_BANK_BRANCH_ID | ReceiptBatchHeaderOldRemittanceBankBranchId | — |
| OLD_REMITTANCE_BANK_BRANCH_ID | ReceiptBatchOldRemittanceBankBranchId | — |
| OLD_REMITTANCE_BANK_BRANCH_ID | ReceiptBatchSchedOldRemittanceBankBranchId | — |
| OLD_REMITTANCE_BANK_BRANCH_ID | RemittanceBatchOldRemittanceBankBranchId | — |
| OPERATION_REQUEST_ID | ReceiptBatchHeaderOperationRequestId | — |
| OPERATION_REQUEST_ID | ReceiptBatchOperationRequestId | — |
| OPERATION_REQUEST_ID | ReceiptBatchSchedOperationRequestId | — |
| OPERATION_REQUEST_ID | RemittanceBatchOperationRequestId | — |
| ORG_ID | ReceiptBatchHeaderOrgId | — |
| ORG_ID | ReceiptBatchOrgId | — |
| ORG_ID | ReceiptBatchSchedOrgId | — |
| ORG_ID | RemittanceBatchOrgId | — |
| PROGRAM_APPLICATION_ID | ReceiptBatchHeaderProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | ReceiptBatchProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | ReceiptBatchSchedProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | RemittanceBatchProgramApplicationId | — |
| PROGRAM_ID | ReceiptBatchHeaderProgramId | — |
| PROGRAM_ID | ReceiptBatchProgramId | — |
| PROGRAM_ID | ReceiptBatchSchedProgramId | — |
| PROGRAM_ID | RemittanceBatchProgramId | — |
| PROGRAM_UPDATE_DATE | ReceiptBatchHeaderProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | ReceiptBatchProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | ReceiptBatchSchedProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | RemittanceBatchProgramUpdateDate | — |
| PURGED_CHILDREN_FLAG | ReceiptBatchHeaderPurgedChildrenFlag | — |
| PURGED_CHILDREN_FLAG | ReceiptBatchPurgedChildrenFlag | — |
| PURGED_CHILDREN_FLAG | ReceiptBatchSchedPurgedChildrenFlag | — |
| PURGED_CHILDREN_FLAG | RemittanceBatchPurgedChildrenFlag | — |
| RECEIPT_CLASS_ID | ReceiptBatchHeaderReceiptClassId | — |
| RECEIPT_CLASS_ID | ReceiptBatchReceiptClassId | — |
| RECEIPT_CLASS_ID | ReceiptBatchSchedReceiptClassId | — |
| RECEIPT_CLASS_ID | RemittanceBatchReceiptClassId | — |
| RECEIPT_METHOD_ID | ReceiptBatchHeaderReceiptMethodId | — |
| RECEIPT_METHOD_ID | ReceiptBatchReceiptMethodId | — |
| RECEIPT_METHOD_ID | ReceiptBatchSchedReceiptMethodId | — |
| RECEIPT_METHOD_ID | RemittanceBatchReceiptMethodId | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptBatchHeaderRemitBankAcctUseId | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptBatchRemitBankAcctUseId | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptBatchSchedRemitBankAcctUseId | — |
| REMIT_BANK_ACCT_USE_ID | RemittanceBatchRemitBankAcctUseId | — |
| REMIT_METHOD_CODE | ReceiptBatchHeaderRemitMethodCode | — |
| REMIT_METHOD_CODE | ReceiptBatchRemitMethodCode | — |
| REMIT_METHOD_CODE | ReceiptBatchSchedRemitMethodCode | — |
| REMIT_METHOD_CODE | RemittanceBatchRemitMethodCode | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptBatchHeaderRemittanceBankAccountId | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptBatchRemittanceBankAccountId | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptBatchSchedRemittanceBankAccountId | — |
| REMITTANCE_BANK_ACCOUNT_ID | RemittanceBatchRemittanceBankAccountId | — |
| REMITTANCE_BANK_BRANCH_ID | ReceiptBatchHeaderRemittanceBankBranchId | — |
| REMITTANCE_BANK_BRANCH_ID | ReceiptBatchRemittanceBankBranchId | — |
| REMITTANCE_BANK_BRANCH_ID | ReceiptBatchSchedRemittanceBankBranchId | — |
| REMITTANCE_BANK_BRANCH_ID | RemittanceBatchRemittanceBankBranchId | — |
| REQUEST_ID | ReceiptBatchHeaderRequestId | — |
| REQUEST_ID | ReceiptBatchRequestId | — |
| REQUEST_ID | ReceiptBatchSchedRequestId | — |
| REQUEST_ID | RemittanceBatchRequestId | — |
| SET_OF_BOOKS_ID | ReceiptBatchHeaderSetOfBooksId | — |
| SET_OF_BOOKS_ID | ReceiptBatchSchedSetOfBooksId | — |
| SET_OF_BOOKS_ID | ReceiptBatchSetOfBooksId | — |
| SET_OF_BOOKS_ID | RemittanceBatchSetOfBooksId | — |
| STATUS | ReceiptBatchHeaderStatus | — |
| STATUS | ReceiptBatchSchedStatus | — |
| STATUS | ReceiptBatchStatus | ✅ |
| STATUS | RemittanceBatchStatus | — |
| TRANSMISSION_ID | ReceiptBatchHeaderTransmissionId | — |
| TRANSMISSION_ID | ReceiptBatchSchedTransmissionId | — |
| TRANSMISSION_ID | ReceiptBatchTransmissionId | — |
| TRANSMISSION_ID | RemittanceBatchTransmissionId | — |
| TRANSMISSION_REQUEST_ID | ReceiptBatchHeaderTransmissionRequestId | — |
| TRANSMISSION_REQUEST_ID | ReceiptBatchSchedTransmissionRequestId | — |
| TRANSMISSION_REQUEST_ID | ReceiptBatchTransmissionRequestId | — |
| TRANSMISSION_REQUEST_ID | RemittanceBatchTransmissionRequestId | — |
| TYPE | ReceiptBatchHeaderType | — |
| TYPE | ReceiptBatchSchedType | — |
| TYPE | ReceiptBatchType | — |
| TYPE | RemittanceBatchType | — |
| WITH_RECOURSE_FLAG | ReceiptBatchHeaderWithRecourseFlag | — |
| WITH_RECOURSE_FLAG | ReceiptBatchSchedWithRecourseFlag | — |
| WITH_RECOURSE_FLAG | ReceiptBatchWithRecourseFlag | — |
| WITH_RECOURSE_FLAG | RemittanceBatchWithRecourseFlag | — |

### [[receiptapplicationpvo|ReceiptApplicationPVO]] (AR · BICC: 3/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BATCH_ID | ReceiptBatchBatchId | ✅ |
| CURRENCY_CODE | ReceiptBatchCurrencyCode | — |
| NAME | ReceiptBatchName | ✅ |
| STATUS | ReceiptBatchStatus | ✅ |
| TYPE | ReceiptBatchType | — |

### [[receiptbatchextractpvo|ReceiptBatchExtractPVO]] (OTHER · BICC: 50/66)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTUAL_AMOUNT | ArBatchActualAmount | ✅ |
| ACTUAL_COUNT | ArBatchActualCount | ✅ |
| ATTRIBUTE1 | ArBatchAttribute1 | — |
| ATTRIBUTE10 | ArBatchAttribute10 | — |
| ATTRIBUTE11 | ArBatchAttribute11 | — |
| ATTRIBUTE12 | ArBatchAttribute12 | — |
| ATTRIBUTE13 | ArBatchAttribute13 | — |
| ATTRIBUTE14 | ArBatchAttribute14 | — |
| ATTRIBUTE15 | ArBatchAttribute15 | — |
| ATTRIBUTE2 | ArBatchAttribute2 | — |
| ATTRIBUTE3 | ArBatchAttribute3 | — |
| ATTRIBUTE4 | ArBatchAttribute4 | — |
| ATTRIBUTE5 | ArBatchAttribute5 | — |
| ATTRIBUTE6 | ArBatchAttribute6 | — |
| ATTRIBUTE7 | ArBatchAttribute7 | — |
| ATTRIBUTE8 | ArBatchAttribute8 | — |
| ATTRIBUTE9 | ArBatchAttribute9 | — |
| ATTRIBUTE_CATEGORY | ArBatchAttributeCategory | — |
| AUTO_PRINT_PROGRAM_ID | ArBatchAutoPrintProgramId | ✅ |
| AUTO_TRANS_PROGRAM_ID | ArBatchAutoTransProgramId | ✅ |
| AUTOMATCH_REQUEST_ID | ArBatchAutomatchRequestId | ✅ |
| BANK_DEPOSIT_NUMBER | ArBatchBankDepositNumber | ✅ |
| BATCH_APPLIED_STATUS | ArBatchBatchAppliedStatus | ✅ |
| BATCH_DATE | ArBatchBatchDate | ✅ |
| BATCH_ID | ArBatchBatchId | ✅ |
| BATCH_SOURCE_SEQ_ID | ArBatchBatchSourceSeqId | ✅ |
| CLOSED_DATE | ArBatchClosedDate | ✅ |
| COMMENTS | ArBatchComments | ✅ |
| CONTROL_AMOUNT | ArBatchControlAmount | ✅ |
| CONTROL_COUNT | ArBatchControlCount | ✅ |
| CREATED_BY | ArBatchCreatedBy | ✅ |
| CREATION_DATE | ArBatchCreationDate | ✅ |
| CURRENCY_CODE | ArBatchCurrencyCode | ✅ |
| DEPOSIT_DATE | ArBatchDepositDate | ✅ |
| EXCHANGE_DATE | ArBatchExchangeDate | ✅ |
| EXCHANGE_RATE | ArBatchExchangeRate | ✅ |
| EXCHANGE_RATE_TYPE | ArBatchExchangeRateType | ✅ |
| GL_DATE | ArBatchGlDate | ✅ |
| LAST_UPDATE_DATE | ArBatchLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ArBatchLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ArBatchLastUpdatedBy | ✅ |
| LOCKBOX_BATCH_NAME | ArBatchLockboxBatchName | ✅ |
| LOCKBOX_ID | ArBatchLockboxId | ✅ |
| MEDIA_REFERENCE | ArBatchMediaReference | ✅ |
| NAME | ArBatchName | ✅ |
| OBJECT_VERSION_NUMBER | ArBatchObjectVersionNumber | ✅ |
| OLD_REMITTANCE_BANK_BRANCH_ID | ArBatchOldRemittanceBankBranchId | ✅ |
| OPERATION_REQUEST_ID | ArBatchOperationRequestId | ✅ |
| ORG_ID | ArBatchOrgId | ✅ |
| PROGRAM_APPLICATION_ID | ArBatchProgramApplicationId | ✅ |
| PROGRAM_ID | ArBatchProgramId | ✅ |
| PROGRAM_UPDATE_DATE | ArBatchProgramUpdateDate | ✅ |
| PURGED_CHILDREN_FLAG | ArBatchPurgedChildrenFlag | ✅ |
| RECEIPT_CLASS_ID | ArBatchReceiptClassId | ✅ |
| RECEIPT_METHOD_ID | ArBatchReceiptMethodId | ✅ |
| REMIT_BANK_ACCT_USE_ID | ArBatchRemitBankAcctUseId | ✅ |
| REMIT_METHOD_CODE | ArBatchRemitMethodCode | ✅ |
| REMITTANCE_BANK_ACCOUNT_ID | ArBatchRemittanceBankAccountId | ✅ |
| REMITTANCE_BANK_BRANCH_ID | ArBatchRemittanceBankBranchId | ✅ |
| REQUEST_ID | ArBatchRequestId | ✅ |
| SET_OF_BOOKS_ID | ArBatchSetOfBooksId | ✅ |
| STATUS | ArBatchStatus | ✅ |
| TRANSMISSION_ID | ArBatchTransmissionId | ✅ |
| TRANSMISSION_REQUEST_ID | ArBatchTransmissionRequestId | ✅ |
| TYPE | ArBatchType | ✅ |
| WITH_RECOURSE_FLAG | ArBatchWithRecourseFlag | ✅ |

### [[receiptheaderpvo|ReceiptHeaderPVO]] (AR · BICC: 5/92)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUTO_PRINT_PROGRAM_ID | ReceiptBatchAutoPrintProgramId | — |
| AUTO_PRINT_PROGRAM_ID | RemittanceBatchAutoPrintProgramId | — |
| AUTO_TRANS_PROGRAM_ID | ReceiptBatchAutoTransProgramId | — |
| AUTO_TRANS_PROGRAM_ID | RemittanceBatchAutoTransProgramId | — |
| BANK_DEPOSIT_NUMBER | ReceiptBatchBankDepositNumber | — |
| BANK_DEPOSIT_NUMBER | RemittanceBatchBankDepositNumber | — |
| BATCH_APPLIED_STATUS | ReceiptBatchBatchAppliedStatus | — |
| BATCH_APPLIED_STATUS | RemittanceBatchBatchAppliedStatus | — |
| BATCH_DATE | ReceiptBatchBatchDate | — |
| BATCH_DATE | RemittanceBatchBatchDate | — |
| BATCH_ID | ReceiptBatchBatchId | ✅ |
| BATCH_ID | RemittanceBatchBatchId | — |
| BATCH_SOURCE_SEQ_ID | ReceiptBatchBatchSourceSeqId | — |
| BATCH_SOURCE_SEQ_ID | RemittanceBatchBatchSourceSeqId | — |
| CLOSED_DATE | ReceiptBatchClosedDate | — |
| CLOSED_DATE | RemittanceBatchClosedDate | — |
| CONTROL_AMOUNT | ReceiptBatchControlAmount | — |
| CONTROL_AMOUNT | RemittanceBatchControlAmount | — |
| CONTROL_COUNT | ReceiptBatchControlCount | — |
| CONTROL_COUNT | RemittanceBatchControlCount | — |
| CREATED_BY | ReceiptBatchCreatedBy | — |
| CREATED_BY | RemittanceBatchCreatedBy | — |
| CREATION_DATE | ReceiptBatchCreationDate | — |
| CREATION_DATE | RemittanceBatchCreationDate | — |
| CURRENCY_CODE | ReceiptBatchCurrencyCode | — |
| CURRENCY_CODE | RemittanceBatchCurrencyCode | — |
| DEPOSIT_DATE | ReceiptBatchDepositDate | — |
| DEPOSIT_DATE | RemittanceBatchDepositDate | — |
| EXCHANGE_DATE | ReceiptBatchExchangeDate | — |
| EXCHANGE_DATE | RemittanceBatchExchangeDate | — |
| EXCHANGE_RATE | ReceiptBatchExchangeRate | — |
| EXCHANGE_RATE | RemittanceBatchExchangeRate | — |
| EXCHANGE_RATE_TYPE | ReceiptBatchExchangeRateType | — |
| EXCHANGE_RATE_TYPE | RemittanceBatchExchangeRateType | — |
| GL_DATE | ReceiptBatchGlDate | — |
| GL_DATE | RemittanceBatchGlDate | — |
| LAST_UPDATE_DATE | ReceiptBatchLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | RemittanceBatchLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ReceiptBatchLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | RemittanceBatchLastUpdateLogin | — |
| LAST_UPDATED_BY | ReceiptBatchLastUpdatedBy | — |
| LAST_UPDATED_BY | RemittanceBatchLastUpdatedBy | — |
| LOCKBOX_BATCH_NAME | ReceiptBatchLockboxBatchName | — |
| LOCKBOX_BATCH_NAME | RemittanceBatchLockboxBatchName | — |
| LOCKBOX_ID | ReceiptBatchLockboxId | — |
| LOCKBOX_ID | RemittanceBatchLockboxId | — |
| MEDIA_REFERENCE | ReceiptBatchMediaReference | — |
| MEDIA_REFERENCE | RemittanceBatchMediaReference | — |
| NAME | ReceiptBatchName | ✅ |
| NAME | RemittanceBatchName | — |
| OBJECT_VERSION_NUMBER | ReceiptBatchObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | RemittanceBatchObjectVersionNumber | — |
| OLD_REMITTANCE_BANK_BRANCH_ID | ReceiptBatchOldRemittanceBankBranchId | — |
| OLD_REMITTANCE_BANK_BRANCH_ID | RemittanceBatchOldRemittanceBankBranchId | — |
| OPERATION_REQUEST_ID | ReceiptBatchOperationRequestId | — |
| OPERATION_REQUEST_ID | RemittanceBatchOperationRequestId | — |
| ORG_ID | ReceiptBatchOrgId | — |
| ORG_ID | RemittanceBatchOrgId | — |
| PROGRAM_APPLICATION_ID | ReceiptBatchProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | RemittanceBatchProgramApplicationId | — |
| PROGRAM_ID | ReceiptBatchProgramId | — |
| PROGRAM_ID | RemittanceBatchProgramId | — |
| PROGRAM_UPDATE_DATE | ReceiptBatchProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | RemittanceBatchProgramUpdateDate | — |
| PURGED_CHILDREN_FLAG | ReceiptBatchPurgedChildrenFlag | — |
| PURGED_CHILDREN_FLAG | RemittanceBatchPurgedChildrenFlag | — |
| RECEIPT_CLASS_ID | ReceiptBatchReceiptClassId | — |
| RECEIPT_CLASS_ID | RemittanceBatchReceiptClassId | — |
| RECEIPT_METHOD_ID | ReceiptBatchReceiptMethodId | — |
| RECEIPT_METHOD_ID | RemittanceBatchReceiptMethodId | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptBatchRemitBankAcctUseId | — |
| REMIT_BANK_ACCT_USE_ID | RemittanceBatchRemitBankAcctUseId | — |
| REMIT_METHOD_CODE | ReceiptBatchRemitMethodCode | — |
| REMIT_METHOD_CODE | RemittanceBatchRemitMethodCode | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptBatchRemittanceBankAccountId | — |
| REMITTANCE_BANK_ACCOUNT_ID | RemittanceBatchRemittanceBankAccountId | — |
| REMITTANCE_BANK_BRANCH_ID | ReceiptBatchRemittanceBankBranchId | — |
| REMITTANCE_BANK_BRANCH_ID | RemittanceBatchRemittanceBankBranchId | — |
| REQUEST_ID | ReceiptBatchRequestId | — |
| REQUEST_ID | RemittanceBatchRequestId | — |
| SET_OF_BOOKS_ID | ReceiptBatchSetOfBooksId | — |
| SET_OF_BOOKS_ID | RemittanceBatchSetOfBooksId | — |
| STATUS | ReceiptBatchStatus | ✅ |
| STATUS | RemittanceBatchStatus | — |
| TRANSMISSION_ID | ReceiptBatchTransmissionId | — |
| TRANSMISSION_ID | RemittanceBatchTransmissionId | — |
| TRANSMISSION_REQUEST_ID | ReceiptBatchTransmissionRequestId | — |
| TRANSMISSION_REQUEST_ID | RemittanceBatchTransmissionRequestId | — |
| TYPE | ReceiptBatchType | — |
| TYPE | RemittanceBatchType | — |
| WITH_RECOURSE_FLAG | ReceiptBatchWithRecourseFlag | — |
| WITH_RECOURSE_FLAG | RemittanceBatchWithRecourseFlag | — |

### [[receipthistorydistributionpvo|ReceiptHistoryDistributionPVO]] (AR · BICC: 1/46)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUTO_PRINT_PROGRAM_ID | BatchAutoPrintProgramId | — |
| AUTO_TRANS_PROGRAM_ID | BatchAutoTransProgramId | — |
| BANK_DEPOSIT_NUMBER | BatchBankDepositNumber | — |
| BATCH_APPLIED_STATUS | BatchBatchAppliedStatus | — |
| BATCH_DATE | BatchBatchDate | — |
| BATCH_ID | BatchBatchId | — |
| BATCH_SOURCE_SEQ_ID | BatchBatchSourceSeqId | — |
| CLOSED_DATE | BatchClosedDate | — |
| CONTROL_AMOUNT | BatchControlAmount | — |
| CONTROL_COUNT | BatchControlCount | — |
| CREATED_BY | BatchCreatedBy | — |
| CREATION_DATE | BatchCreationDate | — |
| CURRENCY_CODE | BatchCurrencyCode | — |
| DEPOSIT_DATE | BatchDepositDate | — |
| EXCHANGE_DATE | BatchExchangeDate | — |
| EXCHANGE_RATE | BatchExchangeRate | — |
| EXCHANGE_RATE_TYPE | BatchExchangeRateType | — |
| GL_DATE | BatchGlDate | — |
| LAST_UPDATE_DATE | BatchLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BatchLastUpdateLogin | — |
| LAST_UPDATED_BY | BatchLastUpdatedBy | — |
| LOCKBOX_BATCH_NAME | BatchLockboxBatchName | — |
| LOCKBOX_ID | BatchLockboxId | — |
| MEDIA_REFERENCE | BatchMediaReference | — |
| NAME | BatchName | — |
| OBJECT_VERSION_NUMBER | BatchObjectVersionNumber | — |
| OLD_REMITTANCE_BANK_BRANCH_ID | BatchOldRemittanceBankBranchId | — |
| OPERATION_REQUEST_ID | BatchOperationRequestId | — |
| ORG_ID | BatchOrgId | — |
| PROGRAM_APPLICATION_ID | BatchProgramApplicationId | — |
| PROGRAM_ID | BatchProgramId | — |
| PROGRAM_UPDATE_DATE | BatchProgramUpdateDate | — |
| PURGED_CHILDREN_FLAG | BatchPurgedChildrenFlag | — |
| RECEIPT_CLASS_ID | BatchReceiptClassId | — |
| RECEIPT_METHOD_ID | BatchReceiptMethodId | — |
| REMIT_BANK_ACCT_USE_ID | BatchRemitBankAcctUseId | — |
| REMIT_METHOD_CODE | BatchRemitMethodCode | — |
| REMITTANCE_BANK_ACCOUNT_ID | BatchRemittanceBankAccountId | — |
| REMITTANCE_BANK_BRANCH_ID | BatchRemittanceBankBranchId | — |
| REQUEST_ID | BatchRequestId | — |
| SET_OF_BOOKS_ID | BatchSetOfBooksId | — |
| STATUS | BatchStatus | — |
| TRANSMISSION_ID | BatchTransmissionId | — |
| TRANSMISSION_REQUEST_ID | BatchTransmissionRequestId | — |
| TYPE | BatchType | — |
| WITH_RECOURSE_FLAG | BatchWithRecourseFlag | — |

### [[receipthistorypvo|ReceiptHistoryPVO]] (AR · BICC: 1/46)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUTO_PRINT_PROGRAM_ID | BatchAutoPrintProgramId | — |
| AUTO_TRANS_PROGRAM_ID | BatchAutoTransProgramId | — |
| BANK_DEPOSIT_NUMBER | BatchBankDepositNumber | — |
| BATCH_APPLIED_STATUS | BatchBatchAppliedStatus | — |
| BATCH_DATE | BatchBatchDate | — |
| BATCH_ID | BatchBatchId | — |
| BATCH_SOURCE_SEQ_ID | BatchBatchSourceSeqId | — |
| CLOSED_DATE | BatchClosedDate | — |
| CONTROL_AMOUNT | BatchControlAmount | — |
| CONTROL_COUNT | BatchControlCount | — |
| CREATED_BY | BatchCreatedBy | — |
| CREATION_DATE | BatchCreationDate | — |
| CURRENCY_CODE | BatchCurrencyCode | — |
| DEPOSIT_DATE | BatchDepositDate | — |
| EXCHANGE_DATE | BatchExchangeDate | — |
| EXCHANGE_RATE | BatchExchangeRate | — |
| EXCHANGE_RATE_TYPE | BatchExchangeRateType | — |
| GL_DATE | BatchGlDate | — |
| LAST_UPDATE_DATE | BatchLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BatchLastUpdateLogin | — |
| LAST_UPDATED_BY | BatchLastUpdatedBy | — |
| LOCKBOX_BATCH_NAME | BatchLockboxBatchName | — |
| LOCKBOX_ID | BatchLockboxId | — |
| MEDIA_REFERENCE | BatchMediaReference | — |
| NAME | BatchName | — |
| OBJECT_VERSION_NUMBER | BatchObjectVersionNumber | — |
| OLD_REMITTANCE_BANK_BRANCH_ID | BatchOldRemittanceBankBranchId | — |
| OPERATION_REQUEST_ID | BatchOperationRequestId | — |
| ORG_ID | BatchOrgId | — |
| PROGRAM_APPLICATION_ID | BatchProgramApplicationId | — |
| PROGRAM_ID | BatchProgramId | — |
| PROGRAM_UPDATE_DATE | BatchProgramUpdateDate | — |
| PURGED_CHILDREN_FLAG | BatchPurgedChildrenFlag | — |
| RECEIPT_CLASS_ID | BatchReceiptClassId | — |
| RECEIPT_METHOD_ID | BatchReceiptMethodId | — |
| REMIT_BANK_ACCT_USE_ID | BatchRemitBankAcctUseId | — |
| REMIT_METHOD_CODE | BatchRemitMethodCode | — |
| REMITTANCE_BANK_ACCOUNT_ID | BatchRemittanceBankAccountId | — |
| REMITTANCE_BANK_BRANCH_ID | BatchRemittanceBankBranchId | — |
| REQUEST_ID | BatchRequestId | — |
| SET_OF_BOOKS_ID | BatchSetOfBooksId | — |
| STATUS | BatchStatus | — |
| TRANSMISSION_ID | BatchTransmissionId | — |
| TRANSMISSION_REQUEST_ID | BatchTransmissionRequestId | — |
| TYPE | BatchType | — |
| WITH_RECOURSE_FLAG | BatchWithRecourseFlag | — |

### [[salesinvoicecustomertrxlinespvo|SalesInvoiceCustomerTrxLinesPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUTO_PRINT_PROGRAM_ID | ReceiptBatchAutoPrintProgramId | — |
| AUTO_TRANS_PROGRAM_ID | ReceiptBatchAutoTransProgramId | — |
| BANK_DEPOSIT_NUMBER | ReceiptBatchBankDepositNumber | — |
| BATCH_APPLIED_STATUS | ReceiptBatchBatchAppliedStatus | — |
| BATCH_DATE | ReceiptBatchBatchDate | — |
| BATCH_ID | ReceiptBatchBatchId | — |
| BATCH_SOURCE_SEQ_ID | ReceiptBatchBatchSourceSeqId | — |
| CLOSED_DATE | ReceiptBatchClosedDate | — |
| CONTROL_AMOUNT | ReceiptBatchControlAmount | — |
| CONTROL_COUNT | ReceiptBatchControlCount | — |
| CURRENCY_CODE | ReceiptBatchCurrencyCode | — |
| DEPOSIT_DATE | ReceiptBatchDepositDate | — |
| EXCHANGE_DATE | ReceiptBatchExchangeDate | — |
| EXCHANGE_RATE | ReceiptBatchExchangeRate | — |
| EXCHANGE_RATE_TYPE | ReceiptBatchExchangeRateType | — |
| GL_DATE | ReceiptBatchGlDate | — |
| LOCKBOX_BATCH_NAME | ReceiptBatchLockboxBatchName | — |
| LOCKBOX_ID | ReceiptBatchLockboxId | — |
| MEDIA_REFERENCE | ReceiptBatchMediaReference | — |
| NAME | ReceiptBatchName | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OLD_REMITTANCE_BANK_BRANCH_ID | ReceiptBatchOldRemittanceBankBranchId | — |
| OPERATION_REQUEST_ID | ReceiptBatchOperationRequestId | — |
| ORG_ID | ReceiptBatchOrgId | — |
| PROGRAM_APPLICATION_ID | ReceiptBatchProgramApplicationId | — |
| PROGRAM_ID | ReceiptBatchProgramId | — |
| PROGRAM_UPDATE_DATE | ReceiptBatchProgramUpdateDate | — |
| PURGED_CHILDREN_FLAG | ReceiptBatchPurgedChildrenFlag | — |
| RECEIPT_CLASS_ID | ReceiptBatchReceiptClassId | — |
| RECEIPT_METHOD_ID | ReceiptBatchReceiptMethodId | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptBatchRemitBankAcctUseId | — |
| REMIT_METHOD_CODE | ReceiptBatchRemitMethodCode | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptBatchRemittanceBankAccountId | — |
| REMITTANCE_BANK_BRANCH_ID | ReceiptBatchRemittanceBankBranchId | — |
| REQUEST_ID | ReceiptBatchRequestId | — |
| SET_OF_BOOKS_ID | ReceiptBatchSetOfBooksId | — |
| STATUS | ReceiptBatchStatus | — |
| TRANSMISSION_ID | ReceiptBatchTransmissionId | — |
| TRANSMISSION_REQUEST_ID | ReceiptBatchTransmissionRequestId | — |
| TYPE | ReceiptBatchType | — |
| WITH_RECOURSE_FLAG | ReceiptBatchWithRecourseFlag | — |

### [[transactionheaderbillsreceivablepvo|TransactionHeaderBillsReceivablePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUTO_PRINT_PROGRAM_ID | ReceiptBatchAutoPrintProgramId | — |
| AUTO_TRANS_PROGRAM_ID | ReceiptBatchAutoTransProgramId | — |
| BANK_DEPOSIT_NUMBER | ReceiptBatchBankDepositNumber | — |
| BATCH_APPLIED_STATUS | ReceiptBatchBatchAppliedStatus | — |
| BATCH_DATE | ReceiptBatchBatchDate | — |
| BATCH_ID | ReceiptBatchBatchId | — |
| BATCH_SOURCE_SEQ_ID | ReceiptBatchBatchSourceSeqId | — |
| CLOSED_DATE | ReceiptBatchClosedDate | — |
| CONTROL_AMOUNT | ReceiptBatchControlAmount | — |
| CONTROL_COUNT | ReceiptBatchControlCount | — |
| CURRENCY_CODE | ReceiptBatchCurrencyCode | — |
| DEPOSIT_DATE | ReceiptBatchDepositDate | — |
| EXCHANGE_DATE | ReceiptBatchExchangeDate | — |
| EXCHANGE_RATE | ReceiptBatchExchangeRate | — |
| EXCHANGE_RATE_TYPE | ReceiptBatchExchangeRateType | — |
| GL_DATE | ReceiptBatchGlDate | — |
| LOCKBOX_BATCH_NAME | ReceiptBatchLockboxBatchName | — |
| LOCKBOX_ID | ReceiptBatchLockboxId | — |
| MEDIA_REFERENCE | ReceiptBatchMediaReference | — |
| NAME | ReceiptBatchName | — |
| OBJECT_VERSION_NUMBER | ReceiptBatchObjectVersionNumber | — |
| OLD_REMITTANCE_BANK_BRANCH_ID | ReceiptBatchOldRemittanceBankBranchId | — |
| OPERATION_REQUEST_ID | ReceiptBatchOperationRequestId | — |
| ORG_ID | ReceiptBatchOrgId | — |
| PROGRAM_APPLICATION_ID | ReceiptBatchProgramApplicationId | — |
| PROGRAM_ID | ReceiptBatchProgramId | — |
| PROGRAM_UPDATE_DATE | ReceiptBatchProgramUpdateDate | — |
| PURGED_CHILDREN_FLAG | ReceiptBatchPurgedChildrenFlag | — |
| RECEIPT_CLASS_ID | ReceiptBatchReceiptClassId | — |
| RECEIPT_METHOD_ID | ReceiptBatchReceiptMethodId | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptBatchRemitBankAcctUseId | — |
| REMIT_METHOD_CODE | ReceiptBatchRemitMethodCode | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptBatchRemittanceBankAccountId | — |
| REMITTANCE_BANK_BRANCH_ID | ReceiptBatchRemittanceBankBranchId | — |
| REQUEST_ID | ReceiptBatchRequestId | — |
| SET_OF_BOOKS_ID | ReceiptBatchSetOfBooksId | — |
| STATUS | ReceiptBatchStatus | — |
| TRANSMISSION_ID | ReceiptBatchTransmissionId | — |
| TRANSMISSION_REQUEST_ID | ReceiptBatchTransmissionRequestId | — |
| TYPE | ReceiptBatchType | — |
| WITH_RECOURSE_FLAG | ReceiptBatchWithRecourseFlag | — |

### [[transactionheadernovcpvo|TransactionHeaderNoVCPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUTO_PRINT_PROGRAM_ID | ReceiptBatchAutoPrintProgramId | — |
| AUTO_TRANS_PROGRAM_ID | ReceiptBatchAutoTransProgramId | — |
| BANK_DEPOSIT_NUMBER | ReceiptBatchBankDepositNumber | — |
| BATCH_APPLIED_STATUS | ReceiptBatchBatchAppliedStatus | — |
| BATCH_DATE | ReceiptBatchBatchDate | — |
| BATCH_ID | ReceiptBatchBatchId | — |
| BATCH_SOURCE_SEQ_ID | ReceiptBatchBatchSourceSeqId | — |
| CLOSED_DATE | ReceiptBatchClosedDate | — |
| CONTROL_AMOUNT | ReceiptBatchControlAmount | — |
| CONTROL_COUNT | ReceiptBatchControlCount | — |
| CURRENCY_CODE | ReceiptBatchCurrencyCode | — |
| DEPOSIT_DATE | ReceiptBatchDepositDate | — |
| EXCHANGE_DATE | ReceiptBatchExchangeDate | — |
| EXCHANGE_RATE | ReceiptBatchExchangeRate | — |
| EXCHANGE_RATE_TYPE | ReceiptBatchExchangeRateType | — |
| GL_DATE | ReceiptBatchGlDate | — |
| LOCKBOX_BATCH_NAME | ReceiptBatchLockboxBatchName | — |
| LOCKBOX_ID | ReceiptBatchLockboxId | — |
| MEDIA_REFERENCE | ReceiptBatchMediaReference | — |
| NAME | ReceiptBatchName | — |
| OBJECT_VERSION_NUMBER | ReceiptBatchObjectVersionNumber | — |
| OLD_REMITTANCE_BANK_BRANCH_ID | ReceiptBatchOldRemittanceBankBranchId | — |
| OPERATION_REQUEST_ID | ReceiptBatchOperationRequestId | — |
| ORG_ID | ReceiptBatchOrgId | — |
| PROGRAM_APPLICATION_ID | ReceiptBatchProgramApplicationId | — |
| PROGRAM_ID | ReceiptBatchProgramId | — |
| PROGRAM_UPDATE_DATE | ReceiptBatchProgramUpdateDate | — |
| PURGED_CHILDREN_FLAG | ReceiptBatchPurgedChildrenFlag | — |
| RECEIPT_CLASS_ID | ReceiptBatchReceiptClassId | — |
| RECEIPT_METHOD_ID | ReceiptBatchReceiptMethodId | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptBatchRemitBankAcctUseId | — |
| REMIT_METHOD_CODE | ReceiptBatchRemitMethodCode | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptBatchRemittanceBankAccountId | — |
| REMITTANCE_BANK_BRANCH_ID | ReceiptBatchRemittanceBankBranchId | — |
| REQUEST_ID | ReceiptBatchRequestId | — |
| SET_OF_BOOKS_ID | ReceiptBatchSetOfBooksId | — |
| STATUS | ReceiptBatchStatus | — |
| TRANSMISSION_ID | ReceiptBatchTransmissionId | — |
| TRANSMISSION_REQUEST_ID | ReceiptBatchTransmissionRequestId | — |
| TYPE | ReceiptBatchType | — |
| WITH_RECOURSE_FLAG | ReceiptBatchWithRecourseFlag | — |

### [[transactionheaderpvo|TransactionHeaderPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUTO_PRINT_PROGRAM_ID | ReceiptBatchAutoPrintProgramId | — |
| AUTO_TRANS_PROGRAM_ID | ReceiptBatchAutoTransProgramId | — |
| BANK_DEPOSIT_NUMBER | ReceiptBatchBankDepositNumber | — |
| BATCH_APPLIED_STATUS | ReceiptBatchBatchAppliedStatus | — |
| BATCH_DATE | ReceiptBatchBatchDate | — |
| BATCH_ID | ReceiptBatchBatchId | — |
| BATCH_SOURCE_SEQ_ID | ReceiptBatchBatchSourceSeqId | — |
| CLOSED_DATE | ReceiptBatchClosedDate | — |
| CONTROL_AMOUNT | ReceiptBatchControlAmount | — |
| CONTROL_COUNT | ReceiptBatchControlCount | — |
| CURRENCY_CODE | ReceiptBatchCurrencyCode | — |
| DEPOSIT_DATE | ReceiptBatchDepositDate | — |
| EXCHANGE_DATE | ReceiptBatchExchangeDate | — |
| EXCHANGE_RATE | ReceiptBatchExchangeRate | — |
| EXCHANGE_RATE_TYPE | ReceiptBatchExchangeRateType | — |
| GL_DATE | ReceiptBatchGlDate | — |
| LOCKBOX_BATCH_NAME | ReceiptBatchLockboxBatchName | — |
| LOCKBOX_ID | ReceiptBatchLockboxId | — |
| MEDIA_REFERENCE | ReceiptBatchMediaReference | — |
| NAME | ReceiptBatchName | — |
| OBJECT_VERSION_NUMBER | ReceiptBatchObjectVersionNumber | — |
| OLD_REMITTANCE_BANK_BRANCH_ID | ReceiptBatchOldRemittanceBankBranchId | — |
| OPERATION_REQUEST_ID | ReceiptBatchOperationRequestId | — |
| ORG_ID | ReceiptBatchOrgId | — |
| PROGRAM_APPLICATION_ID | ReceiptBatchProgramApplicationId | — |
| PROGRAM_ID | ReceiptBatchProgramId | — |
| PROGRAM_UPDATE_DATE | ReceiptBatchProgramUpdateDate | — |
| PURGED_CHILDREN_FLAG | ReceiptBatchPurgedChildrenFlag | — |
| RECEIPT_CLASS_ID | ReceiptBatchReceiptClassId | — |
| RECEIPT_METHOD_ID | ReceiptBatchReceiptMethodId | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptBatchRemitBankAcctUseId | — |
| REMIT_METHOD_CODE | ReceiptBatchRemitMethodCode | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptBatchRemittanceBankAccountId | — |
| REMITTANCE_BANK_BRANCH_ID | ReceiptBatchRemittanceBankBranchId | — |
| REQUEST_ID | ReceiptBatchRequestId | — |
| SET_OF_BOOKS_ID | ReceiptBatchSetOfBooksId | — |
| STATUS | ReceiptBatchStatus | — |
| TRANSMISSION_ID | ReceiptBatchTransmissionId | — |
| TRANSMISSION_REQUEST_ID | ReceiptBatchTransmissionRequestId | — |
| TYPE | ReceiptBatchType | — |
| WITH_RECOURSE_FLAG | ReceiptBatchWithRecourseFlag | — |

### [[transactionhistorydistributionpvo|TransactionHistoryDistributionPVO]] (AR · BICC: 5/46)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUTO_PRINT_PROGRAM_ID | ReceiptBatchAutoPrintProgramId | — |
| AUTO_TRANS_PROGRAM_ID | ReceiptBatchAutoTransProgramId | — |
| BANK_DEPOSIT_NUMBER | ReceiptBatchBankDepositNumber | — |
| BATCH_APPLIED_STATUS | ReceiptBatchBatchAppliedStatus | — |
| BATCH_DATE | ReceiptBatchBatchDate | ✅ |
| BATCH_ID | ReceiptBatchBatchId | ✅ |
| BATCH_SOURCE_SEQ_ID | ReceiptBatchBatchSourceSeqId | — |
| CLOSED_DATE | ReceiptBatchClosedDate | — |
| CONTROL_AMOUNT | ReceiptBatchControlAmount | — |
| CONTROL_COUNT | ReceiptBatchControlCount | — |
| CREATED_BY | ReceiptBatchCreatedBy | — |
| CREATION_DATE | ReceiptBatchCreationDate | — |
| CURRENCY_CODE | ReceiptBatchCurrencyCode | — |
| DEPOSIT_DATE | ReceiptBatchDepositDate | — |
| EXCHANGE_DATE | ReceiptBatchExchangeDate | — |
| EXCHANGE_RATE | ReceiptBatchExchangeRate | — |
| EXCHANGE_RATE_TYPE | ReceiptBatchExchangeRateType | — |
| GL_DATE | ReceiptBatchGlDate | — |
| LAST_UPDATE_DATE | ReceiptBatchLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ReceiptBatchLastUpdateLogin | — |
| LAST_UPDATED_BY | ReceiptBatchLastUpdatedBy | — |
| LOCKBOX_BATCH_NAME | ReceiptBatchLockboxBatchName | — |
| LOCKBOX_ID | ReceiptBatchLockboxId | — |
| MEDIA_REFERENCE | ReceiptBatchMediaReference | — |
| NAME | ReceiptBatchName | ✅ |
| OBJECT_VERSION_NUMBER | ReceiptBatchObjectVersionNumber | — |
| OLD_REMITTANCE_BANK_BRANCH_ID | ReceiptBatchOldRemittanceBankBranchId | — |
| OPERATION_REQUEST_ID | ReceiptBatchOperationRequestId | — |
| ORG_ID | ReceiptBatchOrgId | — |
| PROGRAM_APPLICATION_ID | ReceiptBatchProgramApplicationId | — |
| PROGRAM_ID | ReceiptBatchProgramId | — |
| PROGRAM_UPDATE_DATE | ReceiptBatchProgramUpdateDate | — |
| PURGED_CHILDREN_FLAG | ReceiptBatchPurgedChildrenFlag | — |
| RECEIPT_CLASS_ID | ReceiptBatchReceiptClassId | — |
| RECEIPT_METHOD_ID | ReceiptBatchReceiptMethodId | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptBatchRemitBankAcctUseId | — |
| REMIT_METHOD_CODE | ReceiptBatchRemitMethodCode | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptBatchRemittanceBankAccountId | — |
| REMITTANCE_BANK_BRANCH_ID | ReceiptBatchRemittanceBankBranchId | — |
| REQUEST_ID | ReceiptBatchRequestId | — |
| SET_OF_BOOKS_ID | ReceiptBatchSetOfBooksId | — |
| STATUS | ReceiptBatchStatus | ✅ |
| TRANSMISSION_ID | ReceiptBatchTransmissionId | — |
| TRANSMISSION_REQUEST_ID | ReceiptBatchTransmissionRequestId | — |
| TYPE | ReceiptBatchType | — |
| WITH_RECOURSE_FLAG | ReceiptBatchWithRecourseFlag | — |

### [[transactionhistorypvo|TransactionHistoryPVO]] (AR · BICC: 5/46)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUTO_PRINT_PROGRAM_ID | ReceiptBatchAutoPrintProgramId | — |
| AUTO_TRANS_PROGRAM_ID | ReceiptBatchAutoTransProgramId | — |
| BANK_DEPOSIT_NUMBER | ReceiptBatchBankDepositNumber | — |
| BATCH_APPLIED_STATUS | ReceiptBatchBatchAppliedStatus | — |
| BATCH_DATE | ReceiptBatchBatchDate | ✅ |
| BATCH_ID | ReceiptBatchBatchId | ✅ |
| BATCH_SOURCE_SEQ_ID | ReceiptBatchBatchSourceSeqId | — |
| CLOSED_DATE | ReceiptBatchClosedDate | — |
| CONTROL_AMOUNT | ReceiptBatchControlAmount | — |
| CONTROL_COUNT | ReceiptBatchControlCount | — |
| CREATED_BY | ReceiptBatchCreatedBy | — |
| CREATION_DATE | ReceiptBatchCreationDate | — |
| CURRENCY_CODE | ReceiptBatchCurrencyCode | — |
| DEPOSIT_DATE | ReceiptBatchDepositDate | — |
| EXCHANGE_DATE | ReceiptBatchExchangeDate | — |
| EXCHANGE_RATE | ReceiptBatchExchangeRate | — |
| EXCHANGE_RATE_TYPE | ReceiptBatchExchangeRateType | — |
| GL_DATE | ReceiptBatchGlDate | — |
| LAST_UPDATE_DATE | ReceiptBatchLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ReceiptBatchLastUpdateLogin | — |
| LAST_UPDATED_BY | ReceiptBatchLastUpdatedBy | — |
| LOCKBOX_BATCH_NAME | ReceiptBatchLockboxBatchName | — |
| LOCKBOX_ID | ReceiptBatchLockboxId | — |
| MEDIA_REFERENCE | ReceiptBatchMediaReference | — |
| NAME | ReceiptBatchName | ✅ |
| OBJECT_VERSION_NUMBER | ReceiptBatchObjectVersionNumber | — |
| OLD_REMITTANCE_BANK_BRANCH_ID | ReceiptBatchOldRemittanceBankBranchId | — |
| OPERATION_REQUEST_ID | ReceiptBatchOperationRequestId | — |
| ORG_ID | ReceiptBatchOrgId | — |
| PROGRAM_APPLICATION_ID | ReceiptBatchProgramApplicationId | — |
| PROGRAM_ID | ReceiptBatchProgramId | — |
| PROGRAM_UPDATE_DATE | ReceiptBatchProgramUpdateDate | — |
| PURGED_CHILDREN_FLAG | ReceiptBatchPurgedChildrenFlag | — |
| RECEIPT_CLASS_ID | ReceiptBatchReceiptClassId | — |
| RECEIPT_METHOD_ID | ReceiptBatchReceiptMethodId | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptBatchRemitBankAcctUseId | — |
| REMIT_METHOD_CODE | ReceiptBatchRemitMethodCode | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptBatchRemittanceBankAccountId | — |
| REMITTANCE_BANK_BRANCH_ID | ReceiptBatchRemittanceBankBranchId | — |
| REQUEST_ID | ReceiptBatchRequestId | — |
| SET_OF_BOOKS_ID | ReceiptBatchSetOfBooksId | — |
| STATUS | ReceiptBatchStatus | ✅ |
| TRANSMISSION_ID | ReceiptBatchTransmissionId | — |
| TRANSMISSION_REQUEST_ID | ReceiptBatchTransmissionRequestId | — |
| TYPE | ReceiptBatchType | — |
| WITH_RECOURSE_FLAG | ReceiptBatchWithRecourseFlag | — |

### [[transactionlinebillsreceivablepvo|TransactionLineBillsReceivablePVO]] (AR · BICC: 1/46)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUTO_PRINT_PROGRAM_ID | ReceiptBatchAutoPrintProgramId | — |
| AUTO_TRANS_PROGRAM_ID | ReceiptBatchAutoTransProgramId | — |
| BANK_DEPOSIT_NUMBER | ReceiptBatchBankDepositNumber | — |
| BATCH_APPLIED_STATUS | ReceiptBatchBatchAppliedStatus | — |
| BATCH_DATE | ReceiptBatchBatchDate | — |
| BATCH_ID | ReceiptBatchBatchId | — |
| BATCH_SOURCE_SEQ_ID | ReceiptBatchBatchSourceSeqId | — |
| CLOSED_DATE | ReceiptBatchClosedDate | — |
| CONTROL_AMOUNT | ReceiptBatchControlAmount | — |
| CONTROL_COUNT | ReceiptBatchControlCount | — |
| CREATED_BY | ReceiptBatchCreatedBy | — |
| CREATION_DATE | ReceiptBatchCreationDate | — |
| CURRENCY_CODE | ReceiptBatchCurrencyCode | — |
| DEPOSIT_DATE | ReceiptBatchDepositDate | — |
| EXCHANGE_DATE | ReceiptBatchExchangeDate | — |
| EXCHANGE_RATE | ReceiptBatchExchangeRate | — |
| EXCHANGE_RATE_TYPE | ReceiptBatchExchangeRateType | — |
| GL_DATE | ReceiptBatchGlDate | — |
| LAST_UPDATE_DATE | ReceiptBatchLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ReceiptBatchLastUpdateLogin | — |
| LAST_UPDATED_BY | ReceiptBatchLastUpdatedBy | — |
| LOCKBOX_BATCH_NAME | ReceiptBatchLockboxBatchName | — |
| LOCKBOX_ID | ReceiptBatchLockboxId | — |
| MEDIA_REFERENCE | ReceiptBatchMediaReference | — |
| NAME | ReceiptBatchName | — |
| OBJECT_VERSION_NUMBER | ReceiptBatchObjectVersionNumber | — |
| OLD_REMITTANCE_BANK_BRANCH_ID | ReceiptBatchOldRemittanceBankBranchId | — |
| OPERATION_REQUEST_ID | ReceiptBatchOperationRequestId | — |
| ORG_ID | ReceiptBatchOrgId | — |
| PROGRAM_APPLICATION_ID | ReceiptBatchProgramApplicationId | — |
| PROGRAM_ID | ReceiptBatchProgramId | — |
| PROGRAM_UPDATE_DATE | ReceiptBatchProgramUpdateDate | — |
| PURGED_CHILDREN_FLAG | ReceiptBatchPurgedChildrenFlag | — |
| RECEIPT_CLASS_ID | ReceiptBatchReceiptClassId | — |
| RECEIPT_METHOD_ID | ReceiptBatchReceiptMethodId | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptBatchRemitBankAcctUseId | — |
| REMIT_METHOD_CODE | ReceiptBatchRemitMethodCode | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptBatchRemittanceBankAccountId | — |
| REMITTANCE_BANK_BRANCH_ID | ReceiptBatchRemittanceBankBranchId | — |
| REQUEST_ID | ReceiptBatchRequestId | — |
| SET_OF_BOOKS_ID | ReceiptBatchSetOfBooksId | — |
| STATUS | ReceiptBatchStatus | — |
| TRANSMISSION_ID | ReceiptBatchTransmissionId | — |
| TRANSMISSION_REQUEST_ID | ReceiptBatchTransmissionRequestId | — |
| TYPE | ReceiptBatchType | — |
| WITH_RECOURSE_FLAG | ReceiptBatchWithRecourseFlag | — |

### [[transactionlinedistributionpvo|TransactionLineDistributionPVO]] (AR · BICC: 1/46)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUTO_PRINT_PROGRAM_ID | ReceiptBatchAutoPrintProgramId | — |
| AUTO_TRANS_PROGRAM_ID | ReceiptBatchAutoTransProgramId | — |
| BANK_DEPOSIT_NUMBER | ReceiptBatchBankDepositNumber | — |
| BATCH_APPLIED_STATUS | ReceiptBatchBatchAppliedStatus | — |
| BATCH_DATE | ReceiptBatchBatchDate | — |
| BATCH_ID | ReceiptBatchBatchId | — |
| BATCH_SOURCE_SEQ_ID | ReceiptBatchBatchSourceSeqId | — |
| CLOSED_DATE | ReceiptBatchClosedDate | — |
| CONTROL_AMOUNT | ReceiptBatchControlAmount | — |
| CONTROL_COUNT | ReceiptBatchControlCount | — |
| CREATED_BY | ReceiptBatchCreatedBy | — |
| CREATION_DATE | ReceiptBatchCreationDate | — |
| CURRENCY_CODE | ReceiptBatchCurrencyCode | — |
| DEPOSIT_DATE | ReceiptBatchDepositDate | — |
| EXCHANGE_DATE | ReceiptBatchExchangeDate | — |
| EXCHANGE_RATE | ReceiptBatchExchangeRate | — |
| EXCHANGE_RATE_TYPE | ReceiptBatchExchangeRateType | — |
| GL_DATE | ReceiptBatchGlDate | — |
| LAST_UPDATE_DATE | ReceiptBatchLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ReceiptBatchLastUpdateLogin | — |
| LAST_UPDATED_BY | ReceiptBatchLastUpdatedBy | — |
| LOCKBOX_BATCH_NAME | ReceiptBatchLockboxBatchName | — |
| LOCKBOX_ID | ReceiptBatchLockboxId | — |
| MEDIA_REFERENCE | ReceiptBatchMediaReference | — |
| NAME | ReceiptBatchName | — |
| OBJECT_VERSION_NUMBER | ReceiptBatchObjectVersionNumber | — |
| OLD_REMITTANCE_BANK_BRANCH_ID | ReceiptBatchOldRemittanceBankBranchId | — |
| OPERATION_REQUEST_ID | ReceiptBatchOperationRequestId | — |
| ORG_ID | ReceiptBatchOrgId | — |
| PROGRAM_APPLICATION_ID | ReceiptBatchProgramApplicationId | — |
| PROGRAM_ID | ReceiptBatchProgramId | — |
| PROGRAM_UPDATE_DATE | ReceiptBatchProgramUpdateDate | — |
| PURGED_CHILDREN_FLAG | ReceiptBatchPurgedChildrenFlag | — |
| RECEIPT_CLASS_ID | ReceiptBatchReceiptClassId | — |
| RECEIPT_METHOD_ID | ReceiptBatchReceiptMethodId | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptBatchRemitBankAcctUseId | — |
| REMIT_METHOD_CODE | ReceiptBatchRemitMethodCode | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptBatchRemittanceBankAccountId | — |
| REMITTANCE_BANK_BRANCH_ID | ReceiptBatchRemittanceBankBranchId | — |
| REQUEST_ID | ReceiptBatchRequestId | — |
| SET_OF_BOOKS_ID | ReceiptBatchSetOfBooksId | — |
| STATUS | ReceiptBatchStatus | — |
| TRANSMISSION_ID | ReceiptBatchTransmissionId | — |
| TRANSMISSION_REQUEST_ID | ReceiptBatchTransmissionRequestId | — |
| TYPE | ReceiptBatchType | — |
| WITH_RECOURSE_FLAG | ReceiptBatchWithRecourseFlag | — |

### [[transactionlinepvo|TransactionLinePVO]] (AR · BICC: 1/46)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUTO_PRINT_PROGRAM_ID | ReceiptBatchAutoPrintProgramId | — |
| AUTO_TRANS_PROGRAM_ID | ReceiptBatchAutoTransProgramId | — |
| BANK_DEPOSIT_NUMBER | ReceiptBatchBankDepositNumber | — |
| BATCH_APPLIED_STATUS | ReceiptBatchBatchAppliedStatus | — |
| BATCH_DATE | ReceiptBatchBatchDate | — |
| BATCH_ID | ReceiptBatchBatchId | — |
| BATCH_SOURCE_SEQ_ID | ReceiptBatchBatchSourceSeqId | — |
| CLOSED_DATE | ReceiptBatchClosedDate | — |
| CONTROL_AMOUNT | ReceiptBatchControlAmount | — |
| CONTROL_COUNT | ReceiptBatchControlCount | — |
| CREATED_BY | ReceiptBatchCreatedBy | — |
| CREATION_DATE | ReceiptBatchCreationDate | — |
| CURRENCY_CODE | ReceiptBatchCurrencyCode | — |
| DEPOSIT_DATE | ReceiptBatchDepositDate | — |
| EXCHANGE_DATE | ReceiptBatchExchangeDate | — |
| EXCHANGE_RATE | ReceiptBatchExchangeRate | — |
| EXCHANGE_RATE_TYPE | ReceiptBatchExchangeRateType | — |
| GL_DATE | ReceiptBatchGlDate | — |
| LAST_UPDATE_DATE | ReceiptBatchLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ReceiptBatchLastUpdateLogin | — |
| LAST_UPDATED_BY | ReceiptBatchLastUpdatedBy | — |
| LOCKBOX_BATCH_NAME | ReceiptBatchLockboxBatchName | — |
| LOCKBOX_ID | ReceiptBatchLockboxId | — |
| MEDIA_REFERENCE | ReceiptBatchMediaReference | — |
| NAME | ReceiptBatchName | — |
| OBJECT_VERSION_NUMBER | ReceiptBatchObjectVersionNumber | — |
| OLD_REMITTANCE_BANK_BRANCH_ID | ReceiptBatchOldRemittanceBankBranchId | — |
| OPERATION_REQUEST_ID | ReceiptBatchOperationRequestId | — |
| ORG_ID | ReceiptBatchOrgId | — |
| PROGRAM_APPLICATION_ID | ReceiptBatchProgramApplicationId | — |
| PROGRAM_ID | ReceiptBatchProgramId | — |
| PROGRAM_UPDATE_DATE | ReceiptBatchProgramUpdateDate | — |
| PURGED_CHILDREN_FLAG | ReceiptBatchPurgedChildrenFlag | — |
| RECEIPT_CLASS_ID | ReceiptBatchReceiptClassId | — |
| RECEIPT_METHOD_ID | ReceiptBatchReceiptMethodId | — |
| REMIT_BANK_ACCT_USE_ID | ReceiptBatchRemitBankAcctUseId | — |
| REMIT_METHOD_CODE | ReceiptBatchRemitMethodCode | — |
| REMITTANCE_BANK_ACCOUNT_ID | ReceiptBatchRemittanceBankAccountId | — |
| REMITTANCE_BANK_BRANCH_ID | ReceiptBatchRemittanceBankBranchId | — |
| REQUEST_ID | ReceiptBatchRequestId | — |
| SET_OF_BOOKS_ID | ReceiptBatchSetOfBooksId | — |
| STATUS | ReceiptBatchStatus | — |
| TRANSMISSION_ID | ReceiptBatchTransmissionId | — |
| TRANSMISSION_REQUEST_ID | ReceiptBatchTransmissionRequestId | — |
| TYPE | ReceiptBatchType | — |
| WITH_RECOURSE_FLAG | ReceiptBatchWithRecourseFlag | — |

---

## 📚 Referências

- [Oracle Docs — AR_BATCHES_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/arbatchesall-25065.html)
- [[ar-module-data-dictionary]] — Dossiê do módulo AR
