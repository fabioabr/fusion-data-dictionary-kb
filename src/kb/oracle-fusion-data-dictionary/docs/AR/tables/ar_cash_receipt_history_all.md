---
id: DOC-AR-018
doc_type: system-doc
title: "AR_CASH_RECEIPT_HISTORY_ALL — Histórico de Recebimentos"
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
  - historico-recebimentos
  - receipt-history
  - ciclo-vida
aliases:
  - AR_CASH_RECEIPT_HISTORY_ALL
  - ar_cash_receipt_history_all
  - historico-recebimentos-ar
  - cash-receipt-history
  - receipt-lifecycle
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_CASH_RECEIPT_HISTORY_ALL

## 📌 Visão Geral

Armazena o **histórico do ciclo de vida de cada recebimento** do módulo Accounts Receivable. Cada registro representa uma etapa na evolução do recebimento: criação, confirmação, remessa ao banco, compensação (clearing) e reversão. Permite rastrear a progressão completa de um receipt desde sua entrada até a baixa contábil.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Rastreamento de ciclo de vida:** Cada mudança de status do recebimento gera um novo registro, formando uma trilha de auditoria completa.
- **Contabilização:** Cada etapa pode gerar lançamentos contábeis — a coluna `POSTABLE_FLAG` identifica quais registros foram contabilizados.
- **Remessa bancária:** Rastreamento de quando o recebimento foi enviado ao banco e quando foi compensado.
- **Reversão:** Registro detalhado de reversões com data contábil específica.
- **Reconciliação GL:** Vinculação com combinação de contas contábeis via `ACCOUNT_CODE_COMBINATION_ID`.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CASH_RECEIPT_HISTORY_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro de histórico | — | 🟢 100% |
| 2 | CASH_RECEIPT_ID | NUMBER(18) | NOT NULL | FK | Recebimento associado | [[ar_cash_receipts_all]] | 🟢 100% |
| 3 | STATUS | VARCHAR2(30) | NOT NULL | Classificação | Status nesta etapa do ciclo (APPROVED/CONFIRMED/REMITTED/CLEARED/REVERSED) | — | 🟢 100% |
| 4 | TRX_DATE | DATE | NOT NULL | Data | Data da transação nesta etapa | — | 🟢 100% |
| 5 | AMOUNT | NUMBER | NOT NULL | Financeiro | Valor do recebimento nesta etapa | — | 🟢 100% |
| 6 | FACTOR_FLAG | VARCHAR2(1) | NULL | Classificação | Indica se o recebimento foi fatorado (Y/N) | — | 🟢 100% |
| 7 | FIRST_POSTED_RECORD_FLAG | VARCHAR2(1) | NULL | Contabilidade | Indica se é o primeiro registro contabilizado (Y/N) | — | 🟢 100% |
| 8 | POSTABLE_FLAG | VARCHAR2(1) | NULL | Contabilidade | Indica se este registro gera lançamento contábil (Y/N) | — | 🟢 100% |
| 9 | GL_DATE | DATE | NULL | Contabilidade | Data contábil (General Ledger) | — | 🟢 100% |
| 10 | GL_POSTED_DATE | DATE | NULL | Contabilidade | Data em que foi efetivamente contabilizado no GL | — | 🟢 100% |
| 11 | POSTING_CONTROL_ID | NUMBER(18) | NULL | Contabilidade | ID do processo de posting que contabilizou | — | 🟢 100% |
| 12 | BATCH_ID | NUMBER(18) | NULL | Classificação | Lote de recebimentos associado | [[ar_batches_all]] | 🟢 100% |
| 13 | ACCOUNT_CODE_COMBINATION_ID | NUMBER(18) | NULL | Contabilidade | Combinação de contas contábeis (CCID) | [[gl_code_combinations]] | 🟢 100% |
| 14 | BANK_CHARGE_ACCOUNT_CCID | NUMBER(18) | NULL | Contabilidade | CCID para despesas bancárias | [[gl_code_combinations]] | 🟢 100% |
| 15 | REVERSAL_GL_DATE | DATE | NULL | Contabilidade | Data contábil da reversão | — | 🟢 100% |
| 16 | REVERSAL_POSTING_CONTROL_ID | NUMBER(18) | NULL | Contabilidade | ID do posting de reversão | — | 🟢 100% |
| 17 | CURRENT_RECORD_FLAG | VARCHAR2(1) | NULL | Status | Indica se é o registro mais recente do recebimento (Y/N) | — | 🟢 100% |
| 18 | EXCHANGE_RATE_TYPE | VARCHAR2(30) | NULL | Financeiro | Tipo de taxa de câmbio | [[gl_daily_conversion_types]] | 🟢 100% |
| 19 | EXCHANGE_RATE | NUMBER | NULL | Financeiro | Taxa de câmbio aplicada | — | 🟢 100% |
| 20 | EXCHANGE_DATE | DATE | NULL | Financeiro | Data da taxa de câmbio | — | 🟢 100% |
| 21 | NOTE_STATUS | VARCHAR2(30) | NULL | Classificação | Status da nota promissória (bills receivable) | — | 🟡 70% |
| 22 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 23 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 24 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 25 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 26 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 27 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ar_cash_receipts_all]] — via `CASH_RECEIPT_ID` (recebimento principal)
- [[ar_batches_all]] — via `BATCH_ID` (lote de recebimentos)
- [[gl_code_combinations]] — via `ACCOUNT_CODE_COMBINATION_ID` (conta contábil do histórico de recebimento)
- [[gl_daily_conversion_types]] — via `EXCHANGE_RATE_TYPE` (tipo de câmbio do histórico de recebimento)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit do histórico de recebimento)

### Tabelas-filha (FK de saída)
- [[ar_distributions_all]] — via `SOURCE_ID` onde `SOURCE_TABLE = 'CRH'` (distribuições contábeis)

---

## 📎 Uso Típico

### Histórico completo de um recebimento
```sql
SELECT crh.STATUS, crh.TRX_DATE, crh.AMOUNT,
       crh.GL_DATE, crh.POSTABLE_FLAG, crh.CURRENT_RECORD_FLAG
FROM   AR_CASH_RECEIPT_HISTORY_ALL crh
WHERE  crh.CASH_RECEIPT_ID = :p_cash_receipt_id
ORDER BY crh.CASH_RECEIPT_HISTORY_ID;
```

### Recebimentos compensados em um período
```sql
SELECT cr.RECEIPT_NUMBER, crh.TRX_DATE AS cleared_date, crh.AMOUNT
FROM   AR_CASH_RECEIPT_HISTORY_ALL crh
JOIN   AR_CASH_RECEIPTS_ALL cr ON cr.CASH_RECEIPT_ID = crh.CASH_RECEIPT_ID
WHERE  crh.STATUS = 'CLEARED'
  AND  crh.CURRENT_RECORD_FLAG = 'Y'
  AND  crh.TRX_DATE BETWEEN :start_date AND :end_date
  AND  crh.ORG_ID = :p_org_id;
```

### Filtros comuns
- `STATUS = 'APPROVED'` — Recebimentos aprovados
- `STATUS = 'CLEARED'` — Recebimentos compensados
- `CURRENT_RECORD_FLAG = 'Y'` — Apenas o registro mais recente
- `POSTABLE_FLAG = 'Y'` — Registros contabilizáveis

---

## 🔒 Observações

- Cada mudança de status gera um **novo registro** — a tabela nunca é atualizada in-place para manter a trilha de auditoria.
- O campo `CURRENT_RECORD_FLAG = 'Y'` identifica o registro mais recente; a coluna correspondente em [[ar_cash_receipts_all]] (`CASH_RECEIPT_HISTORY_ID`) também aponta para ele.
- Os status seguem a progressão: **APPROVED → CONFIRMED → REMITTED → CLEARED**. Reversões podem ocorrer em qualquer etapa.
- O `POSTING_CONTROL_ID = -3` indica registros **ainda não contabilizados** no GL.

---

## 🔗 PVOs Relacionados

### [[receiptheaderpvo|ReceiptHeaderPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_CODE_COMBINATION_ID | ReceiptHistoryAccountCodeCombinationId | — |
| ACCTD_AMOUNT | ReceiptHistoryAcctdAmount | — |
| ACCTD_FACTOR_DISCOUNT_AMOUNT | ReceiptHistoryAcctdFactorDiscountAmount | — |
| AMOUNT | ReceiptHistoryAmount | — |
| BANK_CHARGE_ACCOUNT_CCID | ReceiptHistoryBankChargeAccountCcid | — |
| BATCH_ID | ReceiptHistoryBatchId | — |
| CASH_RECEIPT_HISTORY_ID | ReceiptHistoryCashReceiptHistoryId | — |
| CASH_RECEIPT_ID | ReceiptHistoryCashReceiptId | — |
| CREATED_BY | ReceiptHistoryCreatedBy | — |
| CREATED_FROM | ReceiptHistoryCreatedFrom | — |
| CREATION_DATE | ReceiptHistoryCreationDate | — |
| CURRENT_RECORD_FLAG | ReceiptHistoryCurrentRecordFlag | — |
| EVENT_ID | ReceiptHistoryEventId | — |
| EXCHANGE_DATE | ReceiptHistoryExchangeDate | — |
| EXCHANGE_RATE | ReceiptHistoryExchangeRate | — |
| EXCHANGE_RATE_TYPE | ReceiptHistoryExchangeRateType | — |
| FACTOR_DISCOUNT_AMOUNT | ReceiptHistoryFactorDiscountAmount | — |
| FACTOR_FLAG | ReceiptHistoryFactorFlag | — |
| FIRST_POSTED_RECORD_FLAG | ReceiptHistoryFirstPostedRecordFlag | — |
| GL_DATE | ReceiptHistoryGlDate | — |
| GL_POSTED_DATE | ReceiptHistoryGlPostedDate | — |
| NOTE_STATUS | ReceiptHistoryNoteStatus | — |
| ORG_ID | ReceiptHistoryOrgId | — |
| POSTABLE_FLAG | ReceiptHistoryPostableFlag | — |
| POSTING_CONTROL_ID | ReceiptHistoryPostingControlId | — |
| PROGRAM_APPLICATION_ID | ReceiptHistoryProgramApplicationId | — |
| PROGRAM_ID | ReceiptHistoryProgramId | — |
| PROGRAM_UPDATE_DATE | ReceiptHistoryProgramUpdateDate | — |
| PRV_STAT_CASH_RECEIPT_HIST_ID | ReceiptHistoryPrvStatCashReceiptHistId | — |
| REQUEST_ID | ReceiptHistoryRequestId | — |
| REVERSAL_CASH_RECEIPT_HIST_ID | ReceiptHistoryReversalCashReceiptHistId | — |
| REVERSAL_CREATED_FROM | ReceiptHistoryReversalCreatedFrom | — |
| REVERSAL_GL_DATE | ReceiptHistoryReversalGlDate | — |
| REVERSAL_GL_POSTED_DATE | ReceiptHistoryReversalGlPostedDate | — |
| REVERSAL_POSTING_CONTROL_ID | ReceiptHistoryReversalPostingControlId | — |
| STATUS | ReceiptHistoryStatus | — |
| TRX_DATE | ReceiptHistoryTrxDate | — |

### [[receipthistorydistributionpvo|ReceiptHistoryDistributionPVO]] (AR · BICC: 20/52)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_CODE_COMBINATION_ID | HistoryAccountCodeCombinationId | — |
| ACCTD_AMOUNT | HistoryAcctdAmount | — |
| ACCTD_FACTOR_DISCOUNT_AMOUNT | HistoryAcctdFactorDiscountAmount | — |
| AMOUNT | HistoryAmount | — |
| BANK_CHARGE_ACCOUNT_CCID | HistoryBankChargeAccountCcid | — |
| BATCH_ID | HistoryBatchId | — |
| CASH_RECEIPT_HISTORY_ID | HistoryCashReceiptHistoryId | ✅ |
| CASH_RECEIPT_HISTORY_ID | PrvStatHistoryCashReceiptHistoryId | — |
| CASH_RECEIPT_ID | HistoryCashReceiptId | — |
| CASH_RECEIPT_ID | PrvStatHistoryCashReceiptId | — |
| CREATED_BY | HistoryCreatedBy | ✅ |
| CREATED_FROM | HistoryCreatedFrom | — |
| CREATION_DATE | HistoryCreationDate | ✅ |
| CURRENT_RECORD_FLAG | HistoryCurrentRecordFlag | ✅ |
| EVENT_ID | HistoryEventId | ✅ |
| EXCHANGE_DATE | HistoryExchangeDate | ✅ |
| EXCHANGE_RATE | HistoryExchangeRate | ✅ |
| EXCHANGE_RATE_TYPE | HistoryExchangeRateType | ✅ |
| FACTOR_DISCOUNT_AMOUNT | HistoryFactorDiscountAmount | — |
| FACTOR_FLAG | HistoryFactorFlag | — |
| FIRST_POSTED_RECORD_FLAG | HistoryFirstPostedRecordFlag | ✅ |
| GL_DATE | HistoryGlDate | ✅ |
| GL_POSTED_DATE | HistoryGlPostedDate | ✅ |
| LAST_UPDATE_DATE | HistoryLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | HistoryLastUpdateLogin | — |
| LAST_UPDATED_BY | HistoryLastUpdatedBy | ✅ |
| MRC_ACCTD_AMOUNT | HistoryMrcAcctdAmount | — |
| MRC_ACCTD_FACTOR_DISC_AMOUNT | HistoryMrcAcctdFactorDiscAmount | — |
| MRC_EXCHANGE_DATE | HistoryMrcExchangeDate | — |
| MRC_EXCHANGE_RATE | HistoryMrcExchangeRate | — |
| MRC_EXCHANGE_RATE_TYPE | HistoryMrcExchangeRateType | — |
| MRC_GL_POSTED_DATE | HistoryMrcGlPostedDate | — |
| MRC_POSTING_CONTROL_ID | HistoryMrcPostingControlId | — |
| MRC_REVERSAL_GL_POSTED_DATE | HistoryMrcReversalGlPostedDate | — |
| NOTE_STATUS | HistoryNoteStatus | — |
| OBJECT_VERSION_NUMBER | HistoryObjectVersionNumber | — |
| ORG_ID | HistoryOrgId | — |
| POSTABLE_FLAG | HistoryPostableFlag | ✅ |
| POSTING_CONTROL_ID | HistoryPostingControlId | ✅ |
| PROGRAM_APPLICATION_ID | HistoryProgramApplicationId | — |
| PROGRAM_ID | HistoryProgramId | — |
| PROGRAM_UPDATE_DATE | HistoryProgramUpdateDate | — |
| PRV_STAT_CASH_RECEIPT_HIST_ID | HistoryPrvStatCashReceiptHistId | — |
| REQUEST_ID | HistoryRequestId | — |
| REVERSAL_CASH_RECEIPT_HIST_ID | HistoryReversalCashReceiptHistId | — |
| REVERSAL_CREATED_FROM | HistoryReversalCreatedFrom | — |
| REVERSAL_GL_DATE | HistoryReversalGlDate | ✅ |
| REVERSAL_GL_POSTED_DATE | HistoryReversalGlPostedDate | ✅ |
| REVERSAL_POSTING_CONTROL_ID | HistoryReversalPostingControlId | — |
| STATUS | HistoryStatus | ✅ |
| STATUS | PrvStatHistoryStatus | ✅ |
| TRX_DATE | HistoryTrxDate | ✅ |

### [[receipthistoryextractpvo|ReceiptHistoryExtractPVO]] (OTHER · BICC: 41/57)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_CODE_COMBINATION_ID | ArCashReceiptHistoryAccountCodeCombinationId | ✅ |
| ACCTD_AMOUNT | ArCashReceiptHistoryAcctdAmount | ✅ |
| ACCTD_FACTOR_DISCOUNT_AMOUNT | ArCashReceiptHistoryAcctdFactorDiscountAmount | ✅ |
| AMOUNT | ArCashReceiptHistoryAmount | ✅ |
| ATTRIBUTE1 | ArCashReceiptHistoryAttribute1 | — |
| ATTRIBUTE10 | ArCashReceiptHistoryAttribute10 | — |
| ATTRIBUTE11 | ArCashReceiptHistoryAttribute11 | — |
| ATTRIBUTE12 | ArCashReceiptHistoryAttribute12 | — |
| ATTRIBUTE13 | ArCashReceiptHistoryAttribute13 | — |
| ATTRIBUTE14 | ArCashReceiptHistoryAttribute14 | — |
| ATTRIBUTE15 | ArCashReceiptHistoryAttribute15 | — |
| ATTRIBUTE2 | ArCashReceiptHistoryAttribute2 | — |
| ATTRIBUTE3 | ArCashReceiptHistoryAttribute3 | — |
| ATTRIBUTE4 | ArCashReceiptHistoryAttribute4 | — |
| ATTRIBUTE5 | ArCashReceiptHistoryAttribute5 | — |
| ATTRIBUTE6 | ArCashReceiptHistoryAttribute6 | — |
| ATTRIBUTE7 | ArCashReceiptHistoryAttribute7 | — |
| ATTRIBUTE8 | ArCashReceiptHistoryAttribute8 | — |
| ATTRIBUTE9 | ArCashReceiptHistoryAttribute9 | — |
| ATTRIBUTE_CATEGORY | ArCashReceiptHistoryAttributeCategory | — |
| BANK_CHARGE_ACCOUNT_CCID | ArCashReceiptHistoryBankChargeAccountCcid | ✅ |
| BATCH_ID | ArCashReceiptHistoryBatchId | ✅ |
| CASH_RECEIPT_HISTORY_ID | ArCashReceiptHistoryCashReceiptHistoryId | ✅ |
| CASH_RECEIPT_ID | ArCashReceiptHistoryCashReceiptId | ✅ |
| CREATED_BY | ArCashReceiptHistoryCreatedBy | ✅ |
| CREATED_FROM | ArCashReceiptHistoryCreatedFrom | ✅ |
| CREATION_DATE | ArCashReceiptHistoryCreationDate | ✅ |
| CURRENT_RECORD_FLAG | ArCashReceiptHistoryCurrentRecordFlag | ✅ |
| EVENT_ID | ArCashReceiptHistoryEventId | ✅ |
| EXCHANGE_DATE | ArCashReceiptHistoryExchangeDate | ✅ |
| EXCHANGE_RATE | ArCashReceiptHistoryExchangeRate | ✅ |
| EXCHANGE_RATE_TYPE | ArCashReceiptHistoryExchangeRateType | ✅ |
| FACTOR_DISCOUNT_AMOUNT | ArCashReceiptHistoryFactorDiscountAmount | ✅ |
| FACTOR_FLAG | ArCashReceiptHistoryFactorFlag | ✅ |
| FIRST_POSTED_RECORD_FLAG | ArCashReceiptHistoryFirstPostedRecordFlag | ✅ |
| GL_DATE | ArCashReceiptHistoryGlDate | ✅ |
| GL_POSTED_DATE | ArCashReceiptHistoryGlPostedDate | ✅ |
| LAST_UPDATE_DATE | ArCashReceiptHistoryLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ArCashReceiptHistoryLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ArCashReceiptHistoryLastUpdatedBy | ✅ |
| NOTE_STATUS | ArCashReceiptHistoryNoteStatus | ✅ |
| OBJECT_VERSION_NUMBER | ArCashReceiptHistoryObjectVersionNumber | ✅ |
| ORG_ID | ArCashReceiptHistoryOrgId | ✅ |
| POSTABLE_FLAG | ArCashReceiptHistoryPostableFlag | ✅ |
| POSTING_CONTROL_ID | ArCashReceiptHistoryPostingControlId | ✅ |
| PROGRAM_APPLICATION_ID | ArCashReceiptHistoryProgramApplicationId | ✅ |
| PROGRAM_ID | ArCashReceiptHistoryProgramId | ✅ |
| PROGRAM_UPDATE_DATE | ArCashReceiptHistoryProgramUpdateDate | ✅ |
| PRV_STAT_CASH_RECEIPT_HIST_ID | ArCashReceiptHistoryPrvStatCashReceiptHistId | ✅ |
| REQUEST_ID | ArCashReceiptHistoryRequestId | ✅ |
| REVERSAL_CASH_RECEIPT_HIST_ID | ArCashReceiptHistoryReversalCashReceiptHistId | ✅ |
| REVERSAL_CREATED_FROM | ArCashReceiptHistoryReversalCreatedFrom | ✅ |
| REVERSAL_GL_DATE | ArCashReceiptHistoryReversalGlDate | ✅ |
| REVERSAL_GL_POSTED_DATE | ArCashReceiptHistoryReversalGlPostedDate | ✅ |
| REVERSAL_POSTING_CONTROL_ID | ArCashReceiptHistoryReversalPostingControlId | ✅ |
| STATUS | ArCashReceiptHistoryStatus | ✅ |
| TRX_DATE | ArCashReceiptHistoryTrxDate | ✅ |

### [[receipthistorypvo|ReceiptHistoryPVO]] (AR · BICC: 26/147)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_CODE_COMBINATION_ID | HistoryAccountCodeCombinationId | — |
| ACCOUNT_CODE_COMBINATION_ID | PrvStatHistoryAccountCodeCombinationId | — |
| ACCOUNT_CODE_COMBINATION_ID | RevHistoryAccountCodeCombinationId | — |
| ACCTD_AMOUNT | HistoryAcctdAmount | ✅ |
| ACCTD_AMOUNT | PrvStatHistoryAcctdAmount | — |
| ACCTD_AMOUNT | RevHistoryAcctdAmount | — |
| ACCTD_FACTOR_DISCOUNT_AMOUNT | HistoryAcctdFactorDiscountAmount | ✅ |
| ACCTD_FACTOR_DISCOUNT_AMOUNT | PrvStatHistoryAcctdFactorDiscountAmount | — |
| ACCTD_FACTOR_DISCOUNT_AMOUNT | RevHistoryAcctdFactorDiscountAmount | — |
| AMOUNT | HistoryAmount | ✅ |
| AMOUNT | PrvStatHistoryAmount | — |
| AMOUNT | RevHistoryAmount | — |
| BANK_CHARGE_ACCOUNT_CCID | HistoryBankChargeAccountCcid | — |
| BANK_CHARGE_ACCOUNT_CCID | PrvStatHistoryBankChargeAccountCcid | — |
| BANK_CHARGE_ACCOUNT_CCID | RevHistoryBankChargeAccountCcid | — |
| BATCH_ID | HistoryBatchId | — |
| BATCH_ID | PrvStatHistoryBatchId | — |
| BATCH_ID | RevHistoryBatchId | — |
| CASH_RECEIPT_HISTORY_ID | CashReceiptHistoryId | ✅ |
| CASH_RECEIPT_HISTORY_ID | PrvStatHistoryCashReceiptHistoryId | — |
| CASH_RECEIPT_HISTORY_ID | RevHistoryCashReceiptHistoryId | — |
| CASH_RECEIPT_ID | HistoryCashReceiptId | — |
| CASH_RECEIPT_ID | PrvStatHistoryCashReceiptId | — |
| CASH_RECEIPT_ID | RevHistoryCashReceiptId | — |
| CREATED_BY | HistoryCreatedBy | ✅ |
| CREATED_BY | PrvStatHistoryCreatedBy | — |
| CREATED_BY | RevHistoryCreatedBy | — |
| CREATED_FROM | HistoryCreatedFrom | — |
| CREATED_FROM | PrvStatHistoryCreatedFrom | — |
| CREATED_FROM | RevHistoryCreatedFrom | — |
| CREATION_DATE | HistoryCreationDate | ✅ |
| CREATION_DATE | PrvStatHistoryCreationDate | — |
| CREATION_DATE | RevHistoryCreationDate | — |
| CURRENT_RECORD_FLAG | HistoryCurrentRecordFlag | ✅ |
| CURRENT_RECORD_FLAG | PrvStatHistoryCurrentRecordFlag | — |
| CURRENT_RECORD_FLAG | RevHistoryCurrentRecordFlag | — |
| EVENT_ID | HistoryEventId | ✅ |
| EVENT_ID | PrvStatHistoryEventId | — |
| EVENT_ID | RevHistoryEventId | — |
| EXCHANGE_DATE | HistoryExchangeDate | ✅ |
| EXCHANGE_DATE | PrvStatHistoryExchangeDate | — |
| EXCHANGE_DATE | RevHistoryExchangeDate | — |
| EXCHANGE_RATE | HistoryExchangeRate | ✅ |
| EXCHANGE_RATE | PrvStatHistoryExchangeRate | — |
| EXCHANGE_RATE | RevHistoryExchangeRate | — |
| EXCHANGE_RATE_TYPE | HistoryExchangeRateType | ✅ |
| EXCHANGE_RATE_TYPE | PrvStatHistoryExchangeRateType | — |
| EXCHANGE_RATE_TYPE | RevHistoryExchangeRateType | — |
| FACTOR_DISCOUNT_AMOUNT | HistoryFactorDiscountAmount | ✅ |
| FACTOR_DISCOUNT_AMOUNT | PrvStatHistoryFactorDiscountAmount | — |
| FACTOR_DISCOUNT_AMOUNT | RevHistoryFactorDiscountAmount | — |
| FACTOR_FLAG | HistoryFactorFlag | — |
| FACTOR_FLAG | PrvStatHistoryFactorFlag | — |
| FACTOR_FLAG | RevHistoryFactorFlag | — |
| FIRST_POSTED_RECORD_FLAG | HistoryFirstPostedRecordFlag | ✅ |
| FIRST_POSTED_RECORD_FLAG | PrvStatHistoryFirstPostedRecordFlag | — |
| FIRST_POSTED_RECORD_FLAG | RevHistoryFirstPostedRecordFlag | — |
| GL_DATE | HistoryGlDate | ✅ |
| GL_DATE | PrvStatHistoryGlDate | — |
| GL_DATE | RevHistoryGlDate | — |
| GL_POSTED_DATE | HistoryGlPostedDate | ✅ |
| GL_POSTED_DATE | PrvStatHistoryGlPostedDate | — |
| GL_POSTED_DATE | RevHistoryGlPostedDate | — |
| LAST_UPDATE_DATE | HistoryLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | PrvStatHistoryLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | RevHistoryLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | HistoryLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | PrvStatHistoryLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | RevHistoryLastUpdateLogin | — |
| LAST_UPDATED_BY | HistoryLastUpdatedBy | ✅ |
| LAST_UPDATED_BY | PrvStatHistoryLastUpdatedBy | — |
| LAST_UPDATED_BY | RevHistoryLastUpdatedBy | — |
| MRC_ACCTD_AMOUNT | HistoryMrcAcctdAmount | — |
| MRC_ACCTD_AMOUNT | PrvStatHistoryMrcAcctdAmount | — |
| MRC_ACCTD_AMOUNT | RevHistoryMrcAcctdAmount | — |
| MRC_ACCTD_FACTOR_DISC_AMOUNT | HistoryMrcAcctdFactorDiscAmount | — |
| MRC_ACCTD_FACTOR_DISC_AMOUNT | PrvStatHistoryMrcAcctdFactorDiscAmount | — |
| MRC_ACCTD_FACTOR_DISC_AMOUNT | RevHistoryMrcAcctdFactorDiscAmount | — |
| MRC_EXCHANGE_DATE | HistoryMrcExchangeDate | — |
| MRC_EXCHANGE_DATE | PrvStatHistoryMrcExchangeDate | — |
| MRC_EXCHANGE_DATE | RevHistoryMrcExchangeDate | — |
| MRC_EXCHANGE_RATE | HistoryMrcExchangeRate | — |
| MRC_EXCHANGE_RATE | PrvStatHistoryMrcExchangeRate | — |
| MRC_EXCHANGE_RATE | RevHistoryMrcExchangeRate | — |
| MRC_EXCHANGE_RATE_TYPE | HistoryMrcExchangeRateType | — |
| MRC_EXCHANGE_RATE_TYPE | PrvStatHistoryMrcExchangeRateType | — |
| MRC_EXCHANGE_RATE_TYPE | RevHistoryMrcExchangeRateType | — |
| MRC_GL_POSTED_DATE | HistoryMrcGlPostedDate | — |
| MRC_GL_POSTED_DATE | PrvStatHistoryMrcGlPostedDate | — |
| MRC_GL_POSTED_DATE | RevHistoryMrcGlPostedDate | — |
| MRC_POSTING_CONTROL_ID | HistoryMrcPostingControlId | — |
| MRC_POSTING_CONTROL_ID | PrvStatHistoryMrcPostingControlId | — |
| MRC_POSTING_CONTROL_ID | RevHistoryMrcPostingControlId | — |
| MRC_REVERSAL_GL_POSTED_DATE | HistoryMrcReversalGlPostedDate | — |
| MRC_REVERSAL_GL_POSTED_DATE | PrvStatHistoryMrcReversalGlPostedDate | — |
| MRC_REVERSAL_GL_POSTED_DATE | RevHistoryMrcReversalGlPostedDate | — |
| NOTE_STATUS | HistoryNoteStatus | — |
| NOTE_STATUS | PrvStatHistoryNoteStatus | — |
| NOTE_STATUS | RevHistoryNoteStatus | — |
| OBJECT_VERSION_NUMBER | HistoryObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | PrvStatHistoryObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | RevHistoryObjectVersionNumber | — |
| ORG_ID | HistoryOrgId | — |
| ORG_ID | PrvStatHistoryOrgId | — |
| ORG_ID | RevHistoryOrgId | — |
| POSTABLE_FLAG | HistoryPostableFlag | ✅ |
| POSTABLE_FLAG | PrvStatHistoryPostableFlag | — |
| POSTABLE_FLAG | RevHistoryPostableFlag | — |
| POSTING_CONTROL_ID | HistoryPostingControlId | ✅ |
| POSTING_CONTROL_ID | PrvStatHistoryPostingControlId | — |
| POSTING_CONTROL_ID | RevHistoryPostingControlId | — |
| PROGRAM_APPLICATION_ID | HistoryProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | PrvStatHistoryProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | RevHistoryProgramApplicationId | — |
| PROGRAM_ID | HistoryProgramId | — |
| PROGRAM_ID | PrvStatHistoryProgramId | — |
| PROGRAM_ID | RevHistoryProgramId | — |
| PROGRAM_UPDATE_DATE | HistoryProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | PrvStatHistoryProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | RevHistoryProgramUpdateDate | — |
| PRV_STAT_CASH_RECEIPT_HIST_ID | HistoryPrvStatCashReceiptHistId | — |
| PRV_STAT_CASH_RECEIPT_HIST_ID | PrvStatHistoryPrvStatCashReceiptHistId | — |
| PRV_STAT_CASH_RECEIPT_HIST_ID | RevHistoryPrvStatCashReceiptHistId | — |
| REQUEST_ID | HistoryRequestId | — |
| REQUEST_ID | PrvStatHistoryRequestId | — |
| REQUEST_ID | RevHistoryRequestId | — |
| REVERSAL_CASH_RECEIPT_HIST_ID | HistoryReversalCashReceiptHistId | — |
| REVERSAL_CASH_RECEIPT_HIST_ID | PrvStatHistoryReversalCashReceiptHistId | — |
| REVERSAL_CASH_RECEIPT_HIST_ID | RevHistoryReversalCashReceiptHistId | — |
| REVERSAL_CREATED_FROM | HistoryReversalCreatedFrom | — |
| REVERSAL_CREATED_FROM | PrvStatHistoryReversalCreatedFrom | — |
| REVERSAL_CREATED_FROM | RevHistoryReversalCreatedFrom | — |
| REVERSAL_GL_DATE | HistoryReversalGlDate | ✅ |
| REVERSAL_GL_DATE | PrvStatHistoryReversalGlDate | — |
| REVERSAL_GL_DATE | RevHistoryReversalGlDate | — |
| REVERSAL_GL_POSTED_DATE | HistoryReversalGlPostedDate | ✅ |
| REVERSAL_GL_POSTED_DATE | PrvStatHistoryReversalGlPostedDate | — |
| REVERSAL_GL_POSTED_DATE | RevHistoryReversalGlPostedDate | — |
| REVERSAL_POSTING_CONTROL_ID | HistoryReversalPostingControlId | — |
| REVERSAL_POSTING_CONTROL_ID | PrvStatHistoryReversalPostingControlId | — |
| REVERSAL_POSTING_CONTROL_ID | RevHistoryReversalPostingControlId | — |
| STATUS | HistoryStatus | ✅ |
| STATUS | PrvStatHistoryStatus | ✅ |
| STATUS | RevHistoryStatus | — |
| TRX_DATE | HistoryTrxDate | ✅ |
| TRX_DATE | PrvStatHistoryTrxDate | — |
| TRX_DATE | RevHistoryTrxDate | — |

---

## 📚 Referências

- [Oracle Docs — AR_CASH_RECEIPT_HISTORY_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/arcashreceipthistoryall-25077.html)
- [[ar-module-data-dictionary]] — Dossiê do módulo AR
