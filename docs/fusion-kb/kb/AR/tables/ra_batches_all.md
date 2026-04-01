---
id: DOC-AR-006
doc_type: system-doc
title: "RA_BATCHES_ALL — Lotes de Transações AR"
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
  - lotes
  - batch
  - importacao
aliases:
  - RA_BATCHES_ALL
  - ra_batches_all
  - lotes-transacoes-ar
  - ar-batches
  - batch-ar
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# RA_BATCHES_ALL

## 📌 Visão Geral

Armazena informações sobre **lotes de transações** (batches) do módulo Accounts Receivable. Cada lote agrupa transações criadas em conjunto para processamento, permitindo controle de volume e valor esperado versus realizado. Lotes são criados tanto por entrada manual quanto por processos de importação em massa (AutoInvoice).

É a tabela de **controle de agrupamento** — usada para rastreamento de importações, validação de totais e organização de entrada de dados.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Controle de lotes de entrada:** Agrupamento de faturas criadas manualmente em lotes para conferência (contagem e valor de controle vs. real).
- **Rastreamento de importações em massa:** Lotes criados pelo AutoInvoice ou por integrações externas são registrados aqui para rastreabilidade.
- **Validação de totais:** Campos `CONTROL_COUNT`/`CONTROL_AMOUNT` vs. `ACTUAL_COUNT`/`ACTUAL_AMOUNT` permitem conferência de integridade.
- **Purge de dados:** O campo `PURGED_CHILDREN_FLAG` indica se as transações filhas foram expurgadas, mantendo o registro do lote para auditoria.
- **Organização operacional:** Usuários podem agrupar transações por critério funcional (data, origem, tipo) para facilitar revisão e aprovação.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BATCH_ID | NUMBER(18) | NOT NULL | PK | Identificador único do lote | — | 🟢 100% |
| 2 | NAME | VARCHAR2(50) | NOT NULL | Identificação | Nome do lote (visível ao usuário) | — | 🟢 100% |
| 3 | BATCH_SOURCE_ID | NUMBER(18) | NOT NULL | FK | Origem/fonte do lote (manual, AutoInvoice, etc.) | [[ra_batch_sources_all]] | 🟢 100% |
| 4 | BATCH_DATE | DATE | NOT NULL | Data | Data do lote | — | 🟢 100% |
| 5 | STATUS | VARCHAR2(20) | NULL | Classificação | Status do lote (CL=Closed, OP=Open) | — | 🟢 100% |
| 6 | CONTROL_COUNT | NUMBER | NULL | Controle | Quantidade esperada de transações no lote (informada pelo usuário) | — | 🟢 100% |
| 7 | CONTROL_AMOUNT | NUMBER | NULL | Controle | Valor total esperado do lote (informado pelo usuário) | — | 🟢 100% |
| 8 | ACTUAL_COUNT | NUMBER | NULL | Controle | Quantidade real de transações criadas no lote | — | 🟢 100% |
| 9 | ACTUAL_AMOUNT | NUMBER | NULL | Controle | Valor real total das transações no lote | — | 🟢 100% |
| 10 | TYPE | VARCHAR2(30) | NULL | Classificação | Tipo do lote (INV, CM, DM) | — | 🟢 100% |
| 11 | CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Moeda do lote (ISO 4217) | — | 🟢 100% |
| 12 | EXCHANGE_RATE_TYPE | VARCHAR2(30) | NULL | Financeiro | Tipo de taxa de câmbio padrão para o lote | [[gl_daily_conversion_types]] | 🟢 100% |
| 13 | EXCHANGE_DATE | DATE | NULL | Financeiro | Data da taxa de câmbio padrão | — | 🟢 100% |
| 14 | GL_DATE | DATE | NULL | Contabilidade | Data GL padrão para transações do lote | — | 🟢 100% |
| 15 | COMMENTS | VARCHAR2(240) | NULL | Texto livre | Comentários do lote | — | 🟢 100% |
| 16 | PURGED_CHILDREN_FLAG | VARCHAR2(1) | NULL | Controle | Y = transações filhas foram expurgadas (purge) | — | 🟢 100% |
| 17 | SOLD_TO_CUSTOMER_ID | NUMBER(18) | NULL | Cliente | Cliente padrão do lote (sold-to) | [[hz_cust_accounts]] | 🟢 100% |
| 18 | SET_OF_BOOKS_ID | NUMBER(18) | NULL | Contabilidade | Ledger contábil (legado) | [[gl_ledgers]] | 🟢 100% |
| 19 | ISSUE_DATE | DATE | NULL | Data | Data de emissão (bills receivable batches) | — | 🟢 100% |
| 20 | MATURITY_DATE | DATE | NULL | Data | Data de vencimento (bills receivable batches) | — | 🟢 100% |
| 21 | SPECIAL_INSTRUCTIONS | VARCHAR2(240) | NULL | Texto livre | Instruções especiais para o lote | — | 🟡 70% |
| 22 | BATCH_PROCESS_STATUS | VARCHAR2(30) | NULL | Controle | Status do processamento do lote | — | 🟢 100% |
| 23 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 24 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 25 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 26 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 27 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 28 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 29 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 100% |
| 30 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ra_batch_sources_all]] — via `BATCH_SOURCE_ID` (origem/fonte do lote)
- [[gl_daily_conversion_types]] — via `EXCHANGE_RATE_TYPE` (tipo de câmbio do lote de transações)
- [[hz_cust_accounts]] — via `SOLD_TO_CUSTOMER_ID` (cliente padrão de venda do lote)
- [[gl_ledgers]] — via `SET_OF_BOOKS_ID` (ledger contábil)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit do lote de transações AR)

### Tabelas-filha (FK de saída)
- [[ra_customer_trx_all]] — via `BATCH_ID` (transações pertencentes ao lote)

---

## 📎 Uso Típico

### Lotes com divergência entre controle e real
```sql
SELECT b.NAME, b.BATCH_DATE, b.STATUS,
       b.CONTROL_COUNT, b.ACTUAL_COUNT,
       b.CONTROL_AMOUNT, b.ACTUAL_AMOUNT,
       (b.CONTROL_AMOUNT - NVL(b.ACTUAL_AMOUNT, 0)) AS diferenca
FROM   RA_BATCHES_ALL b
WHERE  b.ORG_ID = :p_org_id
  AND  (b.CONTROL_COUNT != b.ACTUAL_COUNT
        OR b.CONTROL_AMOUNT != b.ACTUAL_AMOUNT);
```

### Transações por lote
```sql
SELECT b.NAME AS lote, b.BATCH_DATE,
       ct.TRX_NUMBER, ct.TRX_DATE,
       ct.INVOICE_CURRENCY_CODE
FROM   RA_BATCHES_ALL b
JOIN   RA_CUSTOMER_TRX_ALL ct
       ON ct.BATCH_ID = b.BATCH_ID
WHERE  b.ORG_ID = :p_org_id
ORDER BY b.BATCH_DATE DESC, ct.TRX_NUMBER;
```

### Filtros comuns
- `STATUS = 'OP'` — Lotes abertos (ainda recebendo transações)
- `STATUS = 'CL'` — Lotes fechados
- `PURGED_CHILDREN_FLAG = 'Y'` — Lotes cujas transações foram expurgadas
- `BATCH_SOURCE_ID = :p_source_id` — Filtrar por origem do lote
- `BATCH_DATE BETWEEN :start AND :end` — Período

---

## 🔒 Observações

- Os campos `CONTROL_COUNT` e `CONTROL_AMOUNT` são **opcionais** e preenchidos manualmente pelo usuário no momento da criação do lote. Servem como mecanismo de conferência.
- Quando `PURGED_CHILDREN_FLAG = 'Y'`, o lote existe apenas como registro histórico — suas transações foram removidas por processo de purge.
- O `BATCH_SOURCE_ID` referencia [[ra_batch_sources_all]], que define se a origem é manual, AutoInvoice, ou integração específica.
- Nem toda transação pertence a um lote; o campo `BATCH_ID` em [[ra_customer_trx_all]] pode ser NULL para transações criadas individualmente.
- Campos `ISSUE_DATE` e `MATURITY_DATE` são utilizados apenas em lotes de **Bills Receivable**.
- A tabela possui **Descriptive Flexfields (DFF)** via `ATTRIBUTE1–15` para customizações por implementação.

---

## 🔗 PVOs Relacionados

### [[adjustmentdistributionpvo|AdjustmentDistributionPVO]] (AR · BICC: 1/33)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BATCH_DATE | TransactionBatchBatchDate | — |
| BATCH_ID | TransactionBatchBatchId | — |
| BATCH_PROCESS_STATUS | TransactionBatchBatchProcessStatus | — |
| BATCH_SOURCE_ID | TransactionBatchBatchSourceId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchBatchSourceSeqId | — |
| COMMENTS | TransactionBatchComments | — |
| CONTROL_AMOUNT | TransactionBatchControlAmount | — |
| CONTROL_COUNT | TransactionBatchControlCount | — |
| CREATED_BY | TransactionBatchCreatedBy | — |
| CREATION_DATE | TransactionBatchCreationDate | — |
| CURRENCY_CODE | TransactionBatchCurrencyCode | — |
| EXCHANGE_DATE | TransactionBatchExchangeDate | — |
| EXCHANGE_RATE | TransactionBatchExchangeRate | — |
| EXCHANGE_RATE_TYPE | TransactionBatchExchangeRateType | — |
| GL_DATE | TransactionBatchGlDate | — |
| ISSUE_DATE | TransactionBatchIssueDate | — |
| LAST_UPDATE_DATE | TransactionBatchLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TransactionBatchLastUpdateLogin | — |
| LAST_UPDATED_BY | TransactionBatchLastUpdatedBy | — |
| MATURITY_DATE | TransactionBatchMaturityDate | — |
| NAME | TransactionBatchName | — |
| OBJECT_VERSION_NUMBER | TransactionBatchObjectVersionNumber | — |
| ORG_ID | TransactionBatchOrgId | — |
| PROGRAM_APPLICATION_ID | TransactionBatchProgramApplicationId | — |
| PROGRAM_ID | TransactionBatchProgramId | — |
| PROGRAM_UPDATE_DATE | TransactionBatchProgramUpdateDate | — |
| PURGED_CHILDREN_FLAG | TransactionBatchPurgedChildrenFlag | — |
| REQUEST_ID | TransactionBatchRequestId | — |
| SELECTION_CRITERIA_ID | TransactionBatchSelectionCriteriaId | — |
| SET_OF_BOOKS_ID | TransactionBatchSetOfBooksId | — |
| SPECIAL_INSTRUCTIONS | TransactionBatchSpecialInstructions | — |
| STATUS | TransactionBatchStatus | — |
| TYPE | TransactionBatchType | — |

### [[completedtrxrevadjdistributionpvo|CompletedTrxRevAdjDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BATCH_DATE | TransactionBatchBatchDate | — |
| BATCH_ID | TransactionBatchBatchId | — |
| BATCH_PROCESS_STATUS | TransactionBatchBatchProcessStatus | — |
| BATCH_SOURCE_ID | TransactionBatchBatchSourceId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchBatchSourceSeqId | — |
| COMMENTS | TransactionBatchComments | — |
| CONTROL_AMOUNT | TransactionBatchControlAmount | — |
| CONTROL_COUNT | TransactionBatchControlCount | — |
| CURRENCY_CODE | TransactionBatchCurrencyCode | — |
| EXCHANGE_DATE | TransactionBatchExchangeDate | — |
| EXCHANGE_RATE | TransactionBatchExchangeRate | — |
| EXCHANGE_RATE_TYPE | TransactionBatchExchangeRateType | — |
| GL_DATE | TransactionBatchGlDate | — |
| ISSUE_DATE | TransactionBatchIssueDate | — |
| MATURITY_DATE | TransactionBatchMaturityDate | — |
| NAME | TransactionBatchName | — |
| ORG_ID | TransactionBatchOrgId | — |
| PROGRAM_APPLICATION_ID | TransactionBatchProgramApplicationId | — |
| PROGRAM_ID | TransactionBatchProgramId | — |
| PROGRAM_UPDATE_DATE | TransactionBatchProgramUpdateDate | — |
| PURGED_CHILDREN_FLAG | TransactionBatchPurgedChildrenFlag | — |
| REQUEST_ID | TransactionBatchRequestId | — |
| SELECTION_CRITERIA_ID | TransactionBatchSelectionCriteriaId | — |
| SET_OF_BOOKS_ID | TransactionBatchSetOfBooksId | — |
| SPECIAL_INSTRUCTIONS | TransactionBatchSpecialInstructions | — |
| STATUS | TransactionBatchStatus | — |
| TYPE | TransactionBatchType | — |

### [[completedtrxrevenuedistributionpvo|CompletedTrxRevenueDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BATCH_DATE | TransactionBatchBatchDate | — |
| BATCH_ID | TransactionBatchBatchId | — |
| BATCH_PROCESS_STATUS | TransactionBatchBatchProcessStatus | — |
| BATCH_SOURCE_ID | TransactionBatchBatchSourceId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchBatchSourceSeqId | — |
| COMMENTS | TransactionBatchComments | — |
| CONTROL_AMOUNT | TransactionBatchControlAmount | — |
| CONTROL_COUNT | TransactionBatchControlCount | — |
| CURRENCY_CODE | TransactionBatchCurrencyCode | — |
| EXCHANGE_DATE | TransactionBatchExchangeDate | — |
| EXCHANGE_RATE | TransactionBatchExchangeRate | — |
| EXCHANGE_RATE_TYPE | TransactionBatchExchangeRateType | — |
| GL_DATE | TransactionBatchGlDate | — |
| ISSUE_DATE | TransactionBatchIssueDate | — |
| MATURITY_DATE | TransactionBatchMaturityDate | — |
| NAME | TransactionBatchName | — |
| ORG_ID | TransactionBatchOrgId | — |
| PROGRAM_APPLICATION_ID | TransactionBatchProgramApplicationId | — |
| PROGRAM_ID | TransactionBatchProgramId | — |
| PROGRAM_UPDATE_DATE | TransactionBatchProgramUpdateDate | — |
| PURGED_CHILDREN_FLAG | TransactionBatchPurgedChildrenFlag | — |
| REQUEST_ID | TransactionBatchRequestId | — |
| SELECTION_CRITERIA_ID | TransactionBatchSelectionCriteriaId | — |
| SET_OF_BOOKS_ID | TransactionBatchSetOfBooksId | — |
| SPECIAL_INSTRUCTIONS | TransactionBatchSpecialInstructions | — |
| STATUS | TransactionBatchStatus | — |
| TYPE | TransactionBatchType | — |

### [[creditmemoapplicationdistributionpvo|CreditMemoApplicationDistributionPVO]] (AR · BICC: 1/33)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BATCH_DATE | TransactionBatchBatchDate | — |
| BATCH_ID | TransactionBatchBatchId | — |
| BATCH_PROCESS_STATUS | TransactionBatchBatchProcessStatus | — |
| BATCH_SOURCE_ID | TransactionBatchBatchSourceId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchBatchSourceSeqId | — |
| COMMENTS | TransactionBatchComments | — |
| CONTROL_AMOUNT | TransactionBatchControlAmount | — |
| CONTROL_COUNT | TransactionBatchControlCount | — |
| CREATED_BY | TransactionBatchCreatedBy | — |
| CREATION_DATE | TransactionBatchCreationDate | — |
| CURRENCY_CODE | TransactionBatchCurrencyCode | — |
| EXCHANGE_DATE | TransactionBatchExchangeDate | — |
| EXCHANGE_RATE | TransactionBatchExchangeRate | — |
| EXCHANGE_RATE_TYPE | TransactionBatchExchangeRateType | — |
| GL_DATE | TransactionBatchGlDate | — |
| ISSUE_DATE | TransactionBatchIssueDate | — |
| LAST_UPDATE_DATE | TransactionBatchLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TransactionBatchLastUpdateLogin | — |
| LAST_UPDATED_BY | TransactionBatchLastUpdatedBy | — |
| MATURITY_DATE | TransactionBatchMaturityDate | — |
| NAME | TransactionBatchName | — |
| OBJECT_VERSION_NUMBER | TransactionBatchObjectVersionNumber | — |
| ORG_ID | TransactionBatchOrgId | — |
| PROGRAM_APPLICATION_ID | TransactionBatchProgramApplicationId | — |
| PROGRAM_ID | TransactionBatchProgramId | — |
| PROGRAM_UPDATE_DATE | TransactionBatchProgramUpdateDate | — |
| PURGED_CHILDREN_FLAG | TransactionBatchPurgedChildrenFlag | — |
| REQUEST_ID | TransactionBatchRequestId | — |
| SELECTION_CRITERIA_ID | TransactionBatchSelectionCriteriaId | — |
| SET_OF_BOOKS_ID | TransactionBatchSetOfBooksId | — |
| SPECIAL_INSTRUCTIONS | TransactionBatchSpecialInstructions | — |
| STATUS | TransactionBatchStatus | — |
| TYPE | TransactionBatchType | — |

### [[headersalescreditpvo|HeaderSalesCreditPVO]] (AR · BICC: 1/33)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BATCH_DATE | TransactionBatchBatchDate | — |
| BATCH_ID | TransactionBatchBatchId | — |
| BATCH_PROCESS_STATUS | TransactionBatchBatchProcessStatus | — |
| BATCH_SOURCE_ID | TransactionBatchBatchSourceId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchBatchSourceSeqId | — |
| COMMENTS | TransactionBatchComments | — |
| CONTROL_AMOUNT | TransactionBatchControlAmount | — |
| CONTROL_COUNT | TransactionBatchControlCount | — |
| CREATED_BY | TransactionBatchCreatedBy | — |
| CREATION_DATE | TransactionBatchCreationDate | — |
| CURRENCY_CODE | TransactionBatchCurrencyCode | — |
| EXCHANGE_DATE | TransactionBatchExchangeDate | — |
| EXCHANGE_RATE | TransactionBatchExchangeRate | — |
| EXCHANGE_RATE_TYPE | TransactionBatchExchangeRateType | — |
| GL_DATE | TransactionBatchGlDate | — |
| ISSUE_DATE | TransactionBatchIssueDate | — |
| LAST_UPDATE_DATE | TransactionBatchLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TransactionBatchLastUpdateLogin | — |
| LAST_UPDATED_BY | TransactionBatchLastUpdatedBy | — |
| MATURITY_DATE | TransactionBatchMaturityDate | — |
| NAME | TransactionBatchName | — |
| OBJECT_VERSION_NUMBER | TransactionBatchObjectVersionNumber | — |
| ORG_ID | TransactionBatchOrgId | — |
| PROGRAM_APPLICATION_ID | TransactionBatchProgramApplicationId | — |
| PROGRAM_ID | TransactionBatchProgramId | — |
| PROGRAM_UPDATE_DATE | TransactionBatchProgramUpdateDate | — |
| PURGED_CHILDREN_FLAG | TransactionBatchPurgedChildrenFlag | — |
| REQUEST_ID | TransactionBatchRequestId | — |
| SELECTION_CRITERIA_ID | TransactionBatchSelectionCriteriaId | — |
| SET_OF_BOOKS_ID | TransactionBatchSetOfBooksId | — |
| SPECIAL_INSTRUCTIONS | TransactionBatchSpecialInstructions | — |
| STATUS | TransactionBatchStatus | — |
| TYPE | TransactionBatchType | — |

### [[linesalescreditpvo|LineSalesCreditPVO]] (AR · BICC: 1/33)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BATCH_DATE | TransactionBatchBatchDate | — |
| BATCH_ID | TransactionBatchBatchId | — |
| BATCH_PROCESS_STATUS | TransactionBatchBatchProcessStatus | — |
| BATCH_SOURCE_ID | TransactionBatchBatchSourceId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchBatchSourceSeqId | — |
| COMMENTS | TransactionBatchComments | — |
| CONTROL_AMOUNT | TransactionBatchControlAmount | — |
| CONTROL_COUNT | TransactionBatchControlCount | — |
| CREATED_BY | TransactionBatchCreatedBy | — |
| CREATION_DATE | TransactionBatchCreationDate | — |
| CURRENCY_CODE | TransactionBatchCurrencyCode | — |
| EXCHANGE_DATE | TransactionBatchExchangeDate | — |
| EXCHANGE_RATE | TransactionBatchExchangeRate | — |
| EXCHANGE_RATE_TYPE | TransactionBatchExchangeRateType | — |
| GL_DATE | TransactionBatchGlDate | — |
| ISSUE_DATE | TransactionBatchIssueDate | — |
| LAST_UPDATE_DATE | TransactionBatchLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TransactionBatchLastUpdateLogin | — |
| LAST_UPDATED_BY | TransactionBatchLastUpdatedBy | — |
| MATURITY_DATE | TransactionBatchMaturityDate | — |
| NAME | TransactionBatchName | — |
| OBJECT_VERSION_NUMBER | TransactionBatchObjectVersionNumber | — |
| ORG_ID | TransactionBatchOrgId | — |
| PROGRAM_APPLICATION_ID | TransactionBatchProgramApplicationId | — |
| PROGRAM_ID | TransactionBatchProgramId | — |
| PROGRAM_UPDATE_DATE | TransactionBatchProgramUpdateDate | — |
| PURGED_CHILDREN_FLAG | TransactionBatchPurgedChildrenFlag | — |
| REQUEST_ID | TransactionBatchRequestId | — |
| SELECTION_CRITERIA_ID | TransactionBatchSelectionCriteriaId | — |
| SET_OF_BOOKS_ID | TransactionBatchSetOfBooksId | — |
| SPECIAL_INSTRUCTIONS | TransactionBatchSpecialInstructions | — |
| STATUS | TransactionBatchStatus | — |
| TYPE | TransactionBatchType | — |

### [[paymentschedulepvo|PaymentSchedulePVO]] (AR · BICC: 1/33)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BATCH_DATE | TransactionBatchBatchDate | — |
| BATCH_ID | TransactionBatchBatchId | — |
| BATCH_PROCESS_STATUS | TransactionBatchBatchProcessStatus | — |
| BATCH_SOURCE_ID | TransactionBatchBatchSourceId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchBatchSourceSeqId | — |
| COMMENTS | TransactionBatchComments | — |
| CONTROL_AMOUNT | TransactionBatchControlAmount | — |
| CONTROL_COUNT | TransactionBatchControlCount | — |
| CREATED_BY | TransactionBatchCreatedBy | — |
| CREATION_DATE | TransactionBatchCreationDate | — |
| CURRENCY_CODE | TransactionBatchCurrencyCode | — |
| EXCHANGE_DATE | TransactionBatchExchangeDate | — |
| EXCHANGE_RATE | TransactionBatchExchangeRate | — |
| EXCHANGE_RATE_TYPE | TransactionBatchExchangeRateType | — |
| GL_DATE | TransactionBatchGlDate | — |
| ISSUE_DATE | TransactionBatchIssueDate | — |
| LAST_UPDATE_DATE | TransactionBatchLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TransactionBatchLastUpdateLogin | — |
| LAST_UPDATED_BY | TransactionBatchLastUpdatedBy | — |
| MATURITY_DATE | TransactionBatchMaturityDate | — |
| NAME | TransactionBatchName | — |
| OBJECT_VERSION_NUMBER | TransactionBatchObjectVersionNumber | — |
| ORG_ID | TransactionBatchOrgId | — |
| PROGRAM_APPLICATION_ID | TransactionBatchProgramApplicationId | — |
| PROGRAM_ID | TransactionBatchProgramId | — |
| PROGRAM_UPDATE_DATE | TransactionBatchProgramUpdateDate | — |
| PURGED_CHILDREN_FLAG | TransactionBatchPurgedChildrenFlag | — |
| REQUEST_ID | TransactionBatchRequestId | — |
| SELECTION_CRITERIA_ID | TransactionBatchSelectionCriteriaId | — |
| SET_OF_BOOKS_ID | TransactionBatchSetOfBooksId | — |
| SPECIAL_INSTRUCTIONS | TransactionBatchSpecialInstructions | — |
| STATUS | TransactionBatchStatus | — |
| TYPE | TransactionBatchType | — |

### [[receiptapplicationdistributionpvo|ReceiptApplicationDistributionPVO]] (AR · BICC: 1/33)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BATCH_DATE | TransactionBatchBatchDate | — |
| BATCH_ID | TransactionBatchBatchId | — |
| BATCH_PROCESS_STATUS | TransactionBatchBatchProcessStatus | — |
| BATCH_SOURCE_ID | TransactionBatchBatchSourceId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchBatchSourceSeqId | — |
| COMMENTS | TransactionBatchComments | — |
| CONTROL_AMOUNT | TransactionBatchControlAmount | — |
| CONTROL_COUNT | TransactionBatchControlCount | — |
| CREATED_BY | TransactionBatchCreatedBy | — |
| CREATION_DATE | TransactionBatchCreationDate | — |
| CURRENCY_CODE | TransactionBatchCurrencyCode | — |
| EXCHANGE_DATE | TransactionBatchExchangeDate | — |
| EXCHANGE_RATE | TransactionBatchExchangeRate | — |
| EXCHANGE_RATE_TYPE | TransactionBatchExchangeRateType | — |
| GL_DATE | TransactionBatchGlDate | — |
| ISSUE_DATE | TransactionBatchIssueDate | — |
| LAST_UPDATE_DATE | TransactionBatchLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TransactionBatchLastUpdateLogin | — |
| LAST_UPDATED_BY | TransactionBatchLastUpdatedBy | — |
| MATURITY_DATE | TransactionBatchMaturityDate | — |
| NAME | TransactionBatchName | — |
| OBJECT_VERSION_NUMBER | TransactionBatchObjectVersionNumber | — |
| ORG_ID | TransactionBatchOrgId | — |
| PROGRAM_APPLICATION_ID | TransactionBatchProgramApplicationId | — |
| PROGRAM_ID | TransactionBatchProgramId | — |
| PROGRAM_UPDATE_DATE | TransactionBatchProgramUpdateDate | — |
| PURGED_CHILDREN_FLAG | TransactionBatchPurgedChildrenFlag | — |
| REQUEST_ID | TransactionBatchRequestId | — |
| SELECTION_CRITERIA_ID | TransactionBatchSelectionCriteriaId | — |
| SET_OF_BOOKS_ID | TransactionBatchSetOfBooksId | — |
| SPECIAL_INSTRUCTIONS | TransactionBatchSpecialInstructions | — |
| STATUS | TransactionBatchStatus | — |
| TYPE | TransactionBatchType | — |

### [[receiptapplicationdistributionvc|ReceiptApplicationDistributionVC]] (AR · BICC: 1/33)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BATCH_DATE | TransactionBatchBatchDate | — |
| BATCH_ID | TransactionBatchBatchId | — |
| BATCH_PROCESS_STATUS | TransactionBatchBatchProcessStatus | — |
| BATCH_SOURCE_ID | TransactionBatchBatchSourceId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchBatchSourceSeqId | — |
| COMMENTS | TransactionBatchComments | — |
| CONTROL_AMOUNT | TransactionBatchControlAmount | — |
| CONTROL_COUNT | TransactionBatchControlCount | — |
| CREATED_BY | TransactionBatchCreatedBy | — |
| CREATION_DATE | TransactionBatchCreationDate | — |
| CURRENCY_CODE | TransactionBatchCurrencyCode | — |
| EXCHANGE_DATE | TransactionBatchExchangeDate | — |
| EXCHANGE_RATE | TransactionBatchExchangeRate | — |
| EXCHANGE_RATE_TYPE | TransactionBatchExchangeRateType | — |
| GL_DATE | TransactionBatchGlDate | — |
| ISSUE_DATE | TransactionBatchIssueDate | — |
| LAST_UPDATE_DATE | TransactionBatchLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TransactionBatchLastUpdateLogin | — |
| LAST_UPDATED_BY | TransactionBatchLastUpdatedBy | — |
| MATURITY_DATE | TransactionBatchMaturityDate | — |
| NAME | TransactionBatchName | — |
| OBJECT_VERSION_NUMBER | TransactionBatchObjectVersionNumber | — |
| ORG_ID | TransactionBatchOrgId | — |
| PROGRAM_APPLICATION_ID | TransactionBatchProgramApplicationId | — |
| PROGRAM_ID | TransactionBatchProgramId | — |
| PROGRAM_UPDATE_DATE | TransactionBatchProgramUpdateDate | — |
| PURGED_CHILDREN_FLAG | TransactionBatchPurgedChildrenFlag | — |
| REQUEST_ID | TransactionBatchRequestId | — |
| SELECTION_CRITERIA_ID | TransactionBatchSelectionCriteriaId | — |
| SET_OF_BOOKS_ID | TransactionBatchSetOfBooksId | — |
| SPECIAL_INSTRUCTIONS | TransactionBatchSpecialInstructions | — |
| STATUS | TransactionBatchStatus | — |
| TYPE | TransactionBatchType | — |

### [[salesinvoicecustomertrxlinespvo|SalesInvoiceCustomerTrxLinesPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BATCH_DATE | TransactionBatchBatchDate | — |
| BATCH_ID | TransactionBatchBatchId | — |
| BATCH_PROCESS_STATUS | TransactionBatchBatchProcessStatus | — |
| BATCH_SOURCE_ID | TransactionBatchBatchSourceId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchBatchSourceSeqId | — |
| COMMENTS | TransactionBatchComments | — |
| CONTROL_AMOUNT | TransactionBatchControlAmount | — |
| CONTROL_COUNT | TransactionBatchControlCount | — |
| CURRENCY_CODE | TransactionBatchCurrencyCode | — |
| EXCHANGE_DATE | TransactionBatchExchangeDate | — |
| EXCHANGE_RATE | TransactionBatchExchangeRate | — |
| EXCHANGE_RATE_TYPE | TransactionBatchExchangeRateType | — |
| GL_DATE | TransactionBatchGlDate | — |
| ISSUE_DATE | TransactionBatchIssueDate | — |
| MATURITY_DATE | TransactionBatchMaturityDate | — |
| NAME | TransactionBatchName | — |
| ORG_ID | TransactionBatchOrgId | — |
| PROGRAM_APPLICATION_ID | TransactionBatchProgramApplicationId | — |
| PROGRAM_ID | TransactionBatchProgramId | — |
| PROGRAM_UPDATE_DATE | TransactionBatchProgramUpdateDate | — |
| PURGED_CHILDREN_FLAG | TransactionBatchPurgedChildrenFlag | — |
| REQUEST_ID | TransactionBatchRequestId | — |
| SELECTION_CRITERIA_ID | TransactionBatchSelectionCriteriaId | — |
| SET_OF_BOOKS_ID | TransactionBatchSetOfBooksId | — |
| SPECIAL_INSTRUCTIONS | TransactionBatchSpecialInstructions | — |
| STATUS | TransactionBatchStatus | — |
| TYPE | TransactionBatchType | — |

### [[transactionbatchextractpvo|TransactionBatchExtractPVO]] (OTHER · BICC: 33/49)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | RaBatchAttribute1 | — |
| ATTRIBUTE10 | RaBatchAttribute10 | — |
| ATTRIBUTE11 | RaBatchAttribute11 | — |
| ATTRIBUTE12 | RaBatchAttribute12 | — |
| ATTRIBUTE13 | RaBatchAttribute13 | — |
| ATTRIBUTE14 | RaBatchAttribute14 | — |
| ATTRIBUTE15 | RaBatchAttribute15 | — |
| ATTRIBUTE2 | RaBatchAttribute2 | — |
| ATTRIBUTE3 | RaBatchAttribute3 | — |
| ATTRIBUTE4 | RaBatchAttribute4 | — |
| ATTRIBUTE5 | RaBatchAttribute5 | — |
| ATTRIBUTE6 | RaBatchAttribute6 | — |
| ATTRIBUTE7 | RaBatchAttribute7 | — |
| ATTRIBUTE8 | RaBatchAttribute8 | — |
| ATTRIBUTE9 | RaBatchAttribute9 | — |
| ATTRIBUTE_CATEGORY | RaBatchAttributeCategory | — |
| BATCH_DATE | RaBatchBatchDate | ✅ |
| BATCH_ID | RaBatchBatchId | ✅ |
| BATCH_PROCESS_STATUS | RaBatchBatchProcessStatus | ✅ |
| BATCH_SOURCE_ID | RaBatchBatchSourceId | ✅ |
| BATCH_SOURCE_SEQ_ID | RaBatchBatchSourceSeqId | ✅ |
| COMMENTS | RaBatchComments | ✅ |
| CONTROL_AMOUNT | RaBatchControlAmount | ✅ |
| CONTROL_COUNT | RaBatchControlCount | ✅ |
| CREATED_BY | RaBatchCreatedBy | ✅ |
| CREATION_DATE | RaBatchCreationDate | ✅ |
| CURRENCY_CODE | RaBatchCurrencyCode | ✅ |
| EXCHANGE_DATE | RaBatchExchangeDate | ✅ |
| EXCHANGE_RATE | RaBatchExchangeRate | ✅ |
| EXCHANGE_RATE_TYPE | RaBatchExchangeRateType | ✅ |
| GL_DATE | RaBatchGlDate | ✅ |
| ISSUE_DATE | RaBatchIssueDate | ✅ |
| LAST_UPDATE_DATE | RaBatchLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RaBatchLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | RaBatchLastUpdatedBy | ✅ |
| MATURITY_DATE | RaBatchMaturityDate | ✅ |
| NAME | RaBatchName | ✅ |
| OBJECT_VERSION_NUMBER | RaBatchObjectVersionNumber | ✅ |
| ORG_ID | RaBatchOrgId | ✅ |
| PROGRAM_APPLICATION_ID | RaBatchProgramApplicationId | ✅ |
| PROGRAM_ID | RaBatchProgramId | ✅ |
| PROGRAM_UPDATE_DATE | RaBatchProgramUpdateDate | ✅ |
| PURGED_CHILDREN_FLAG | RaBatchPurgedChildrenFlag | ✅ |
| REQUEST_ID | RaBatchRequestId | ✅ |
| SELECTION_CRITERIA_ID | RaBatchSelectionCriteriaId | ✅ |
| SET_OF_BOOKS_ID | RaBatchSetOfBooksId | ✅ |
| SPECIAL_INSTRUCTIONS | RaBatchSpecialInstructions | ✅ |
| STATUS | RaBatchStatus | ✅ |
| TYPE | RaBatchType | ✅ |

### [[transactionheaderbillsreceivablepvo|TransactionHeaderBillsReceivablePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BATCH_DATE | TransactionBatchBatchDate | — |
| BATCH_ID | TransactionBatchBatchId | — |
| BATCH_PROCESS_STATUS | TransactionBatchBatchProcessStatus | — |
| BATCH_SOURCE_ID | TransactionBatchBatchSourceId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchBatchSourceSeqId | — |
| COMMENTS | TransactionBatchComments | — |
| CONTROL_AMOUNT | TransactionBatchControlAmount | — |
| CONTROL_COUNT | TransactionBatchControlCount | — |
| CURRENCY_CODE | TransactionBatchCurrencyCode | — |
| EXCHANGE_DATE | TransactionBatchExchangeDate | — |
| EXCHANGE_RATE | TransactionBatchExchangeRate | — |
| EXCHANGE_RATE_TYPE | TransactionBatchExchangeRateType | — |
| GL_DATE | TransactionBatchGlDate | — |
| ISSUE_DATE | TransactionBatchIssueDate | — |
| MATURITY_DATE | TransactionBatchMaturityDate | — |
| NAME | TransactionBatchName | — |
| ORG_ID | TransactionBatchOrgId | — |
| PROGRAM_APPLICATION_ID | TransactionBatchProgramApplicationId | — |
| PROGRAM_ID | TransactionBatchProgramId | — |
| PROGRAM_UPDATE_DATE | TransactionBatchProgramUpdateDate | — |
| PURGED_CHILDREN_FLAG | TransactionBatchPurgedChildrenFlag | — |
| REQUEST_ID | TransactionBatchRequestId | — |
| SELECTION_CRITERIA_ID | TransactionBatchSelectionCriteriaId | — |
| SET_OF_BOOKS_ID | TransactionBatchSetOfBooksId | — |
| SPECIAL_INSTRUCTIONS | TransactionBatchSpecialInstructions | — |
| STATUS | TransactionBatchStatus | — |
| TYPE | TransactionBatchType | — |

### [[transactionheadernovcpvo|TransactionHeaderNoVCPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BATCH_DATE | TransactionBatchBatchDate | — |
| BATCH_ID | TransactionBatchBatchId | — |
| BATCH_PROCESS_STATUS | TransactionBatchBatchProcessStatus | — |
| BATCH_SOURCE_ID | TransactionBatchBatchSourceId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchBatchSourceSeqId | — |
| COMMENTS | TransactionBatchComments | — |
| CONTROL_AMOUNT | TransactionBatchControlAmount | — |
| CONTROL_COUNT | TransactionBatchControlCount | — |
| CURRENCY_CODE | TransactionBatchCurrencyCode | — |
| EXCHANGE_DATE | TransactionBatchExchangeDate | — |
| EXCHANGE_RATE | TransactionBatchExchangeRate | — |
| EXCHANGE_RATE_TYPE | TransactionBatchExchangeRateType | — |
| GL_DATE | TransactionBatchGlDate | — |
| ISSUE_DATE | TransactionBatchIssueDate | — |
| MATURITY_DATE | TransactionBatchMaturityDate | — |
| NAME | TransactionBatchName | — |
| ORG_ID | TransactionBatchOrgId | — |
| PROGRAM_APPLICATION_ID | TransactionBatchProgramApplicationId | — |
| PROGRAM_ID | TransactionBatchProgramId | — |
| PROGRAM_UPDATE_DATE | TransactionBatchProgramUpdateDate | — |
| PURGED_CHILDREN_FLAG | TransactionBatchPurgedChildrenFlag | — |
| REQUEST_ID | TransactionBatchRequestId | — |
| SELECTION_CRITERIA_ID | TransactionBatchSelectionCriteriaId | — |
| SET_OF_BOOKS_ID | TransactionBatchSetOfBooksId | — |
| SPECIAL_INSTRUCTIONS | TransactionBatchSpecialInstructions | — |
| STATUS | TransactionBatchStatus | — |
| TYPE | TransactionBatchType | — |

### [[transactionheaderpvo|TransactionHeaderPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BATCH_DATE | TransactionBatchBatchDate | — |
| BATCH_ID | TransactionBatchBatchId | — |
| BATCH_PROCESS_STATUS | TransactionBatchBatchProcessStatus | — |
| BATCH_SOURCE_ID | TransactionBatchBatchSourceId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchBatchSourceSeqId | — |
| COMMENTS | TransactionBatchComments | — |
| CONTROL_AMOUNT | TransactionBatchControlAmount | — |
| CONTROL_COUNT | TransactionBatchControlCount | — |
| CURRENCY_CODE | TransactionBatchCurrencyCode | — |
| EXCHANGE_DATE | TransactionBatchExchangeDate | — |
| EXCHANGE_RATE | TransactionBatchExchangeRate | — |
| EXCHANGE_RATE_TYPE | TransactionBatchExchangeRateType | — |
| GL_DATE | TransactionBatchGlDate | — |
| ISSUE_DATE | TransactionBatchIssueDate | — |
| MATURITY_DATE | TransactionBatchMaturityDate | — |
| NAME | TransactionBatchName | — |
| ORG_ID | TransactionBatchOrgId | — |
| PROGRAM_APPLICATION_ID | TransactionBatchProgramApplicationId | — |
| PROGRAM_ID | TransactionBatchProgramId | — |
| PROGRAM_UPDATE_DATE | TransactionBatchProgramUpdateDate | — |
| PURGED_CHILDREN_FLAG | TransactionBatchPurgedChildrenFlag | — |
| REQUEST_ID | TransactionBatchRequestId | — |
| SELECTION_CRITERIA_ID | TransactionBatchSelectionCriteriaId | — |
| SET_OF_BOOKS_ID | TransactionBatchSetOfBooksId | — |
| SPECIAL_INSTRUCTIONS | TransactionBatchSpecialInstructions | — |
| STATUS | TransactionBatchStatus | — |
| TYPE | TransactionBatchType | — |

### [[transactionhistorydistributionpvo|TransactionHistoryDistributionPVO]] (AR · BICC: 4/39)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BATCH_DATE | TransactionBatchBatchDate | — |
| BATCH_ID | TransactionBatchBatchBatchId | — |
| BATCH_ID | TransactionBatchBatchId | ✅ |
| BATCH_PROCESS_STATUS | TransactionBatchBatchBatchProcessStatus | — |
| BATCH_PROCESS_STATUS | TransactionBatchBatchProcessStatus | — |
| BATCH_SOURCE_ID | TransactionBatchBatchSourceId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchBatchSourceSeqId | — |
| COMMENTS | TransactionBatchComments | — |
| CONTROL_AMOUNT | TransactionBatchControlAmount | — |
| CONTROL_COUNT | TransactionBatchControlCount | — |
| CREATED_BY | TransactionBatchCreatedBy | — |
| CREATION_DATE | TransactionBatchCreationDate | — |
| CURRENCY_CODE | TransactionBatchBatchCurrencyCode | — |
| CURRENCY_CODE | TransactionBatchCurrencyCode | — |
| EXCHANGE_DATE | TransactionBatchExchangeDate | — |
| EXCHANGE_RATE | TransactionBatchExchangeRate | — |
| EXCHANGE_RATE_TYPE | TransactionBatchExchangeRateType | — |
| GL_DATE | TransactionBatchGlDate | — |
| ISSUE_DATE | TransactionBatchIssueDate | — |
| LAST_UPDATE_DATE | TransactionBatchLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TransactionBatchLastUpdateLogin | — |
| LAST_UPDATED_BY | TransactionBatchLastUpdatedBy | — |
| MATURITY_DATE | TransactionBatchMaturityDate | — |
| NAME | TransactionBatchBatchName | — |
| NAME | TransactionBatchName | ✅ |
| OBJECT_VERSION_NUMBER | TransactionBatchObjectVersionNumber | — |
| ORG_ID | TransactionBatchOrgId | — |
| PROGRAM_APPLICATION_ID | TransactionBatchProgramApplicationId | — |
| PROGRAM_ID | TransactionBatchProgramId | — |
| PROGRAM_UPDATE_DATE | TransactionBatchProgramUpdateDate | — |
| PURGED_CHILDREN_FLAG | TransactionBatchPurgedChildrenFlag | — |
| REQUEST_ID | TransactionBatchRequestId | — |
| SELECTION_CRITERIA_ID | TransactionBatchSelectionCriteriaId | — |
| SET_OF_BOOKS_ID | TransactionBatchSetOfBooksId | — |
| SPECIAL_INSTRUCTIONS | TransactionBatchSpecialInstructions | — |
| STATUS | TransactionBatchBatchStatus | — |
| STATUS | TransactionBatchStatus | ✅ |
| TYPE | TransactionBatchBatchType | — |
| TYPE | TransactionBatchType | — |

### [[transactionhistorypvo|TransactionHistoryPVO]] (AR · BICC: 4/39)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BATCH_DATE | TransactionBatchBatchDate | — |
| BATCH_ID | TransactionBatchBatchBatchId | — |
| BATCH_ID | TransactionBatchBatchId | ✅ |
| BATCH_PROCESS_STATUS | TransactionBatchBatchBatchProcessStatus | — |
| BATCH_PROCESS_STATUS | TransactionBatchBatchProcessStatus | — |
| BATCH_SOURCE_ID | TransactionBatchBatchSourceId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchBatchSourceSeqId | — |
| COMMENTS | TransactionBatchComments | — |
| CONTROL_AMOUNT | TransactionBatchControlAmount | — |
| CONTROL_COUNT | TransactionBatchControlCount | — |
| CREATED_BY | TransactionBatchCreatedBy | — |
| CREATION_DATE | TransactionBatchCreationDate | — |
| CURRENCY_CODE | TransactionBatchBatchCurrencyCode | — |
| CURRENCY_CODE | TransactionBatchCurrencyCode | — |
| EXCHANGE_DATE | TransactionBatchExchangeDate | — |
| EXCHANGE_RATE | TransactionBatchExchangeRate | — |
| EXCHANGE_RATE_TYPE | TransactionBatchExchangeRateType | — |
| GL_DATE | TransactionBatchGlDate | — |
| ISSUE_DATE | TransactionBatchIssueDate | — |
| LAST_UPDATE_DATE | TransactionBatchLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TransactionBatchLastUpdateLogin | — |
| LAST_UPDATED_BY | TransactionBatchLastUpdatedBy | — |
| MATURITY_DATE | TransactionBatchMaturityDate | — |
| NAME | TransactionBatchBatchName | — |
| NAME | TransactionBatchName | ✅ |
| OBJECT_VERSION_NUMBER | TransactionBatchObjectVersionNumber | — |
| ORG_ID | TransactionBatchOrgId | — |
| PROGRAM_APPLICATION_ID | TransactionBatchProgramApplicationId | — |
| PROGRAM_ID | TransactionBatchProgramId | — |
| PROGRAM_UPDATE_DATE | TransactionBatchProgramUpdateDate | — |
| PURGED_CHILDREN_FLAG | TransactionBatchPurgedChildrenFlag | — |
| REQUEST_ID | TransactionBatchRequestId | — |
| SELECTION_CRITERIA_ID | TransactionBatchSelectionCriteriaId | — |
| SET_OF_BOOKS_ID | TransactionBatchSetOfBooksId | — |
| SPECIAL_INSTRUCTIONS | TransactionBatchSpecialInstructions | — |
| STATUS | TransactionBatchBatchStatus | — |
| STATUS | TransactionBatchStatus | ✅ |
| TYPE | TransactionBatchBatchType | — |
| TYPE | TransactionBatchType | — |

### [[transactionlinebillsreceivablepvo|TransactionLineBillsReceivablePVO]] (AR · BICC: 1/33)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BATCH_DATE | TransactionBatchBatchDate | — |
| BATCH_ID | TransactionBatchBatchId | — |
| BATCH_PROCESS_STATUS | TransactionBatchBatchProcessStatus | — |
| BATCH_SOURCE_ID | TransactionBatchBatchSourceId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchBatchSourceSeqId | — |
| COMMENTS | TransactionBatchComments | — |
| CONTROL_AMOUNT | TransactionBatchControlAmount | — |
| CONTROL_COUNT | TransactionBatchControlCount | — |
| CREATED_BY | TransactionBatchCreatedBy | — |
| CREATION_DATE | TransactionBatchCreationDate | — |
| CURRENCY_CODE | TransactionBatchCurrencyCode | — |
| EXCHANGE_DATE | TransactionBatchExchangeDate | — |
| EXCHANGE_RATE | TransactionBatchExchangeRate | — |
| EXCHANGE_RATE_TYPE | TransactionBatchExchangeRateType | — |
| GL_DATE | TransactionBatchGlDate | — |
| ISSUE_DATE | TransactionBatchIssueDate | — |
| LAST_UPDATE_DATE | TransactionBatchLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TransactionBatchLastUpdateLogin | — |
| LAST_UPDATED_BY | TransactionBatchLastUpdatedBy | — |
| MATURITY_DATE | TransactionBatchMaturityDate | — |
| NAME | TransactionBatchName | — |
| OBJECT_VERSION_NUMBER | TransactionBatchObjectVersionNumber | — |
| ORG_ID | TransactionBatchOrgId | — |
| PROGRAM_APPLICATION_ID | TransactionBatchProgramApplicationId | — |
| PROGRAM_ID | TransactionBatchProgramId | — |
| PROGRAM_UPDATE_DATE | TransactionBatchProgramUpdateDate | — |
| PURGED_CHILDREN_FLAG | TransactionBatchPurgedChildrenFlag | — |
| REQUEST_ID | TransactionBatchRequestId | — |
| SELECTION_CRITERIA_ID | TransactionBatchSelectionCriteriaId | — |
| SET_OF_BOOKS_ID | TransactionBatchSetOfBooksId | — |
| SPECIAL_INSTRUCTIONS | TransactionBatchSpecialInstructions | — |
| STATUS | TransactionBatchStatus | — |
| TYPE | TransactionBatchType | — |

### [[transactionlinedistributionpvo|TransactionLineDistributionPVO]] (AR · BICC: 1/33)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BATCH_DATE | TransactionBatchBatchDate | — |
| BATCH_ID | TransactionBatchBatchId | — |
| BATCH_PROCESS_STATUS | TransactionBatchBatchProcessStatus | — |
| BATCH_SOURCE_ID | TransactionBatchBatchSourceId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchBatchSourceSeqId | — |
| COMMENTS | TransactionBatchComments | — |
| CONTROL_AMOUNT | TransactionBatchControlAmount | — |
| CONTROL_COUNT | TransactionBatchControlCount | — |
| CREATED_BY | TransactionBatchCreatedBy | — |
| CREATION_DATE | TransactionBatchCreationDate | — |
| CURRENCY_CODE | TransactionBatchCurrencyCode | — |
| EXCHANGE_DATE | TransactionBatchExchangeDate | — |
| EXCHANGE_RATE | TransactionBatchExchangeRate | — |
| EXCHANGE_RATE_TYPE | TransactionBatchExchangeRateType | — |
| GL_DATE | TransactionBatchGlDate | — |
| ISSUE_DATE | TransactionBatchIssueDate | — |
| LAST_UPDATE_DATE | TransactionBatchLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TransactionBatchLastUpdateLogin | — |
| LAST_UPDATED_BY | TransactionBatchLastUpdatedBy | — |
| MATURITY_DATE | TransactionBatchMaturityDate | — |
| NAME | TransactionBatchName | — |
| OBJECT_VERSION_NUMBER | TransactionBatchObjectVersionNumber | — |
| ORG_ID | TransactionBatchOrgId | — |
| PROGRAM_APPLICATION_ID | TransactionBatchProgramApplicationId | — |
| PROGRAM_ID | TransactionBatchProgramId | — |
| PROGRAM_UPDATE_DATE | TransactionBatchProgramUpdateDate | — |
| PURGED_CHILDREN_FLAG | TransactionBatchPurgedChildrenFlag | — |
| REQUEST_ID | TransactionBatchRequestId | — |
| SELECTION_CRITERIA_ID | TransactionBatchSelectionCriteriaId | — |
| SET_OF_BOOKS_ID | TransactionBatchSetOfBooksId | — |
| SPECIAL_INSTRUCTIONS | TransactionBatchSpecialInstructions | — |
| STATUS | TransactionBatchStatus | — |
| TYPE | TransactionBatchType | — |

### [[transactionlinepvo|TransactionLinePVO]] (AR · BICC: 1/33)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BATCH_DATE | TransactionBatchBatchDate | — |
| BATCH_ID | TransactionBatchBatchId | — |
| BATCH_PROCESS_STATUS | TransactionBatchBatchProcessStatus | — |
| BATCH_SOURCE_ID | TransactionBatchBatchSourceId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchBatchSourceSeqId | — |
| COMMENTS | TransactionBatchComments | — |
| CONTROL_AMOUNT | TransactionBatchControlAmount | — |
| CONTROL_COUNT | TransactionBatchControlCount | — |
| CREATED_BY | TransactionBatchCreatedBy | — |
| CREATION_DATE | TransactionBatchCreationDate | — |
| CURRENCY_CODE | TransactionBatchCurrencyCode | — |
| EXCHANGE_DATE | TransactionBatchExchangeDate | — |
| EXCHANGE_RATE | TransactionBatchExchangeRate | — |
| EXCHANGE_RATE_TYPE | TransactionBatchExchangeRateType | — |
| GL_DATE | TransactionBatchGlDate | — |
| ISSUE_DATE | TransactionBatchIssueDate | — |
| LAST_UPDATE_DATE | TransactionBatchLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TransactionBatchLastUpdateLogin | — |
| LAST_UPDATED_BY | TransactionBatchLastUpdatedBy | — |
| MATURITY_DATE | TransactionBatchMaturityDate | — |
| NAME | TransactionBatchName | — |
| OBJECT_VERSION_NUMBER | TransactionBatchObjectVersionNumber | — |
| ORG_ID | TransactionBatchOrgId | — |
| PROGRAM_APPLICATION_ID | TransactionBatchProgramApplicationId | — |
| PROGRAM_ID | TransactionBatchProgramId | — |
| PROGRAM_UPDATE_DATE | TransactionBatchProgramUpdateDate | — |
| PURGED_CHILDREN_FLAG | TransactionBatchPurgedChildrenFlag | — |
| REQUEST_ID | TransactionBatchRequestId | — |
| SELECTION_CRITERIA_ID | TransactionBatchSelectionCriteriaId | — |
| SET_OF_BOOKS_ID | TransactionBatchSetOfBooksId | — |
| SPECIAL_INSTRUCTIONS | TransactionBatchSpecialInstructions | — |
| STATUS | TransactionBatchStatus | — |
| TYPE | TransactionBatchType | — |

---

## 📚 Referências

- [Oracle Docs — RA_BATCHES_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/rabatchesall-24880.html)
- [[ar-module-data-dictionary]] — Dossiê do módulo AR
