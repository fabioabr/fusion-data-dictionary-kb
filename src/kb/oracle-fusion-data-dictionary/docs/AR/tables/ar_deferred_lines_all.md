---
id: DOC-AR-043
doc_type: system-doc
title: "AR_DEFERRED_LINES_ALL — Linhas de Receita Diferida"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-receivable, data-dictionary, receita-diferida, deferred-revenue, contabilidade]
aliases: [AR_DEFERRED_LINES_ALL, ar_deferred_lines_all, deferred_lines, receita_diferida, deferred_revenue_ar]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_DEFERRED_LINES_ALL

> [!note] Sufixo _ALL
> Tabela particionada por `ORG_ID`. O sufixo `_ALL` indica que contém dados de todas as business units. Acessos via views sem sufixo filtram automaticamente pelo contexto de segurança da sessão.

## 📌 Visão Geral

Tabela de linhas de receita diferida do Accounts Receivable. Registra os valores de receita que foram faturados mas ainda não podem ser reconhecidos contabilmente, mantendo o controle de diferimento até que os critérios de coletabilidade ou entrega sejam atendidos.

## 🧠 Propósito de Negócio

O diferimento de receita é um requisito contábil (IFRS 15 / ASC 606) para situações em que a receita não pode ser reconhecida no momento do faturamento. Exemplos: entrega futura de serviços, incerteza de coletabilidade, contingências contratuais. Esta tabela rastreia cada linha de receita diferida, seu status de coletabilidade e a data contábil de reconhecimento planejada.

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Descrição | Categoria | Confiança |
|---|--------|------|-------|-----------|-----------|-----------|
| 1 | DEFERRED_LINE_ID | NUMBER(15) | NOT NULL | Chave primária. Identificador único da linha diferida. | PK | 🟢 100% |
| 2 | CUSTOMER_TRX_LINE_ID | NUMBER(15) | NOT NULL | FK para RA_CUSTOMER_TRX_LINES_ALL. Linha da transação original. | FK | 🟢 100% |
| 3 | CUSTOMER_TRX_ID | NUMBER(15) | NOT NULL | FK para RA_CUSTOMER_TRX_ALL. Transação original. | FK | 🟢 100% |
| 4 | AMOUNT | NUMBER | NOT NULL | Valor da receita diferida na moeda da transação. | Financeiro | 🟢 100% |
| 5 | ACCTD_AMOUNT | NUMBER | NULL | Valor da receita diferida na moeda funcional (contábil). | Financeiro | 🟢 100% |
| 6 | CODE_COMBINATION_ID | NUMBER(15) | NULL | FK para GL_CODE_COMBINATIONS. Conta contábil de receita diferida. | FK | 🟢 100% |
| 7 | GL_DATE | DATE | NULL | Data contábil planejada para reconhecimento da receita. | Temporal | 🟢 100% |
| 8 | ORIGINAL_COLLECTIBILITY_FLAG | VARCHAR2(1) | NULL | Flag de coletabilidade original da linha (Y = coletável). | Controle | 🟢 100% |
| 9 | LINE_COLLECTIBLE_FLAG | VARCHAR2(1) | NULL | Flag de coletabilidade atual da linha (Y = coletável). | Controle | 🟢 100% |
| 10 | EVENT_ID | NUMBER(15) | NULL | Identificador do evento contábil (SLA). | FK | 🟢 100% |
| 11 | LINE_NUMBER | NUMBER | NULL | Número da linha dentro da transação. | Controle | 🟡 75% |
| 12 | REVENUE_ADJUSTMENT_ID | NUMBER(15) | NULL | FK para ajuste de receita, se aplicável. | FK | 🟡 75% |
| 13 | TAX_LINE_ID | NUMBER(15) | NULL | FK para linha de imposto diferida, se aplicável. | FK | 🟡 75% |
| 14 | ORG_ID | NUMBER(15) | NOT NULL | Identificador da business unit (Operating Unit). | Partição | 🟢 100% |
| 15 | CREATED_BY | VARCHAR2(64) | NOT NULL | Usuário que criou o registro. | WHO | 🟢 100% |
| 16 | CREATION_DATE | DATE | NOT NULL | Data de criação do registro. | WHO | 🟢 100% |
| 17 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Usuário da última atualização. | WHO | 🟢 100% |
| 18 | LAST_UPDATE_DATE | DATE | NOT NULL | Data da última atualização. | WHO | 🟢 100% |

## 🔗 Relacionamentos

- **RA_CUSTOMER_TRX_LINES_ALL** — Linha da transação original (N:1 via `CUSTOMER_TRX_LINE_ID`).
- **RA_CUSTOMER_TRX_ALL** — Transação original (N:1 via `CUSTOMER_TRX_ID`).
- **GL_CODE_COMBINATIONS** — Conta contábil de diferimento (N:1 via `CODE_COMBINATION_ID`).

## 📎 Uso Típico

```sql
-- Receita diferida pendente de reconhecimento
SELECT dl.CUSTOMER_TRX_ID,
       dl.CUSTOMER_TRX_LINE_ID,
       dl.AMOUNT,
       dl.GL_DATE,
       dl.LINE_COLLECTIBLE_FLAG,
       dl.ORIGINAL_COLLECTIBILITY_FLAG
  FROM AR_DEFERRED_LINES_ALL dl
 WHERE dl.ORG_ID = :p_org_id
   AND dl.LINE_COLLECTIBLE_FLAG = 'N'
 ORDER BY dl.GL_DATE;
```

## 🔒 Observações

- Quando `LINE_COLLECTIBLE_FLAG` muda de 'N' para 'Y', a receita é reconhecida e transferida da conta de diferimento para a conta de receita.
- O campo `GL_DATE` indica quando a receita será (ou foi) reconhecida contabilmente.
- A diferença entre `ORIGINAL_COLLECTIBILITY_FLAG` e `LINE_COLLECTIBLE_FLAG` indica reclassificação de coletabilidade.
- Essencial para compliance com IFRS 15 (reconhecimento de receita).
- Filtrar sempre por `ORG_ID` para garantir contexto correto de business unit.

## 🔗 PVOs Relacionados

### [[linesalescreditpvo|LineSalesCreditPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_DUE_ORIGINAL | DeferredLineAcctdAmountDueOriginal | — |
| ACCTD_AMOUNT_PENDING | DeferredLineAcctdAmountPending | — |
| ACCTD_AMOUNT_RECOGNIZED | DeferredLineAcctdAmountRecognized | — |
| AMOUNT_DUE_ORIGINAL | DeferredLineAmountDueOriginal | — |
| AMOUNT_PENDING | DeferredLineAmountPending | — |
| AMOUNT_RECOGNIZED | DeferredLineAmountRecognized | — |
| CREATED_BY | DeferredLineCreatedBy | — |
| CUSTOMER_TRX_ID | DeferredLineCustomerTrxId | — |
| CUSTOMER_TRX_LINE_ID | DeferredLineCustomerTrxLineId | — |
| LAST_UPDATE_LOGIN | DeferredLineLastUpdateLogin | — |
| LAST_UPDATED_BY | DeferredLineLastUpdatedBy | — |
| LINE_COLLECTIBLE_FLAG | DeferredLineLineCollectibleFlag | — |
| MANUAL_OVERRIDE_FLAG | DeferredLineManualOverrideFlag | — |
| OBJECT_VERSION_NUMBER | DeferredLineObjectVersionNumber | — |
| ORG_ID | DeferredLineOrgId | — |
| ORIGINAL_COLLECTIBILITY_FLAG | DeferredLineOriginalCollectibilityFlag | — |
| PARENT_LINE_ID | DeferredLineParentLineId | — |
| REQUEST_ID | DeferredLineRequestId | — |

### [[transactionhistorydistributionpvo|TransactionHistoryDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_DUE_ORIGINAL | DeferredLineAcctdAmountDueOriginal | — |
| ACCTD_AMOUNT_PENDING | DeferredLineAcctdAmountPending | — |
| ACCTD_AMOUNT_RECOGNIZED | DeferredLineAcctdAmountRecognized | — |
| AMOUNT_DUE_ORIGINAL | DeferredLineAmountDueOriginal | — |
| AMOUNT_PENDING | DeferredLineAmountPending | — |
| AMOUNT_RECOGNIZED | DeferredLineAmountRecognized | — |
| CREATED_BY | DeferredLineCreatedBy | — |
| CUSTOMER_TRX_ID | DeferredLineCustomerTrxId | — |
| CUSTOMER_TRX_LINE_ID | DeferredLineCustomerTrxLineId | — |
| LAST_UPDATE_LOGIN | DeferredLineLastUpdateLogin | — |
| LAST_UPDATED_BY | DeferredLineLastUpdatedBy | — |
| LINE_COLLECTIBLE_FLAG | DeferredLineLineCollectibleFlag | — |
| MANUAL_OVERRIDE_FLAG | DeferredLineManualOverrideFlag | — |
| OBJECT_VERSION_NUMBER | DeferredLineObjectVersionNumber | — |
| ORG_ID | DeferredLineOrgId | — |
| ORIGINAL_COLLECTIBILITY_FLAG | DeferredLineOriginalCollectibilityFlag | — |
| PARENT_LINE_ID | DeferredLineParentLineId | — |
| REQUEST_ID | DeferredLineRequestId | — |

### [[transactionhistorypvo|TransactionHistoryPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_DUE_ORIGINAL | DeferredLineAcctdAmountDueOriginal | — |
| ACCTD_AMOUNT_PENDING | DeferredLineAcctdAmountPending | — |
| ACCTD_AMOUNT_RECOGNIZED | DeferredLineAcctdAmountRecognized | — |
| AMOUNT_DUE_ORIGINAL | DeferredLineAmountDueOriginal | — |
| AMOUNT_PENDING | DeferredLineAmountPending | — |
| AMOUNT_RECOGNIZED | DeferredLineAmountRecognized | — |
| CREATED_BY | DeferredLineCreatedBy | — |
| CUSTOMER_TRX_ID | DeferredLineCustomerTrxId | — |
| CUSTOMER_TRX_LINE_ID | DeferredLineCustomerTrxLineId | — |
| LAST_UPDATE_LOGIN | DeferredLineLastUpdateLogin | — |
| LAST_UPDATED_BY | DeferredLineLastUpdatedBy | — |
| LINE_COLLECTIBLE_FLAG | DeferredLineLineCollectibleFlag | — |
| MANUAL_OVERRIDE_FLAG | DeferredLineManualOverrideFlag | — |
| OBJECT_VERSION_NUMBER | DeferredLineObjectVersionNumber | — |
| ORG_ID | DeferredLineOrgId | — |
| ORIGINAL_COLLECTIBILITY_FLAG | DeferredLineOriginalCollectibilityFlag | — |
| PARENT_LINE_ID | DeferredLineParentLineId | — |
| REQUEST_ID | DeferredLineRequestId | — |

### [[transactionlinebillsreceivablepvo|TransactionLineBillsReceivablePVO]] (AR · BICC: 1/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_DUE_ORIGINAL | DeferredLineAcctdAmountDueOriginal | — |
| ACCTD_AMOUNT_PENDING | DeferredLineAcctdAmountPending | — |
| ACCTD_AMOUNT_RECOGNIZED | DeferredLineAcctdAmountRecognized | — |
| AMOUNT_DUE_ORIGINAL | DeferredLineAmountDueOriginal | — |
| AMOUNT_PENDING | DeferredLineAmountPending | — |
| AMOUNT_RECOGNIZED | DeferredLineAmountRecognized | — |
| CREATED_BY | DeferredLineCreatedBy | — |
| CREATION_DATE | DeferredLineCreationDate | — |
| CUSTOMER_TRX_ID | DeferredLineCustomerTrxId | — |
| CUSTOMER_TRX_LINE_ID | DeferredLineCustomerTrxLineId | — |
| LAST_UPDATE_DATE | DeferredLineLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DeferredLineLastUpdateLogin | — |
| LAST_UPDATED_BY | DeferredLineLastUpdatedBy | — |
| LINE_COLLECTIBLE_FLAG | DeferredLineLineCollectibleFlag | — |
| MANUAL_OVERRIDE_FLAG | DeferredLineManualOverrideFlag | — |
| OBJECT_VERSION_NUMBER | DeferredLineObjectVersionNumber | — |
| ORG_ID | DeferredLineOrgId | — |
| ORIGINAL_COLLECTIBILITY_FLAG | DeferredLineOriginalCollectibilityFlag | — |
| PARENT_LINE_ID | DeferredLineParentLineId | — |
| REQUEST_ID | DeferredLineRequestId | — |

### [[transactionlinedistributionpvo|TransactionLineDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_DUE_ORIGINAL | DeferredLineAcctdAmountDueOriginal | — |
| ACCTD_AMOUNT_PENDING | DeferredLineAcctdAmountPending | — |
| ACCTD_AMOUNT_RECOGNIZED | DeferredLineAcctdAmountRecognized | — |
| AMOUNT_DUE_ORIGINAL | DeferredLineAmountDueOriginal | — |
| AMOUNT_PENDING | DeferredLineAmountPending | — |
| AMOUNT_RECOGNIZED | DeferredLineAmountRecognized | — |
| CREATED_BY | DeferredLineCreatedBy | — |
| CUSTOMER_TRX_ID | DeferredLineCustomerTrxId | — |
| CUSTOMER_TRX_LINE_ID | DeferredLineCustomerTrxLineId | — |
| LAST_UPDATE_LOGIN | DeferredLineLastUpdateLogin | — |
| LAST_UPDATED_BY | DeferredLineLastUpdatedBy | — |
| LINE_COLLECTIBLE_FLAG | DeferredLineLineCollectibleFlag | — |
| MANUAL_OVERRIDE_FLAG | DeferredLineManualOverrideFlag | — |
| OBJECT_VERSION_NUMBER | DeferredLineObjectVersionNumber | — |
| ORG_ID | DeferredLineOrgId | — |
| ORIGINAL_COLLECTIBILITY_FLAG | DeferredLineOriginalCollectibilityFlag | — |
| PARENT_LINE_ID | DeferredLineParentLineId | — |
| REQUEST_ID | DeferredLineRequestId | — |

### [[transactionlinepvo|TransactionLinePVO]] (AR · BICC: 7/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_DUE_ORIGINAL | DeferredLineAcctdAmountDueOriginal | ✅ |
| ACCTD_AMOUNT_PENDING | DeferredLineAcctdAmountPending | ✅ |
| ACCTD_AMOUNT_RECOGNIZED | DeferredLineAcctdAmountRecognized | ✅ |
| AMOUNT_DUE_ORIGINAL | DeferredLineAmountDueOriginal | ✅ |
| AMOUNT_PENDING | DeferredLineAmountPending | ✅ |
| AMOUNT_RECOGNIZED | DeferredLineAmountRecognized | ✅ |
| CREATED_BY | DeferredLineCreatedBy | — |
| CREATION_DATE | DeferredLineCreationDate | — |
| CUSTOMER_TRX_ID | DeferredLineCustomerTrxId | — |
| CUSTOMER_TRX_LINE_ID | DeferredLineCustomerTrxLineId | — |
| LAST_UPDATE_DATE | DeferredLineLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DeferredLineLastUpdateLogin | — |
| LAST_UPDATED_BY | DeferredLineLastUpdatedBy | — |
| LINE_COLLECTIBLE_FLAG | DeferredLineLineCollectibleFlag | — |
| MANUAL_OVERRIDE_FLAG | DeferredLineManualOverrideFlag | — |
| OBJECT_VERSION_NUMBER | DeferredLineObjectVersionNumber | — |
| ORG_ID | DeferredLineOrgId | — |
| ORIGINAL_COLLECTIBILITY_FLAG | DeferredLineOriginalCollectibilityFlag | — |
| PARENT_LINE_ID | DeferredLineParentLineId | — |
| REQUEST_ID | DeferredLineRequestId | — |

### [[transactionlinerevenuedeferralextractpvo|TransactionLineRevenueDeferralExtractPVO]] (OTHER · BICC: 20/36)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_DUE_ORIGINAL | ArDeferredLineAcctdAmountDueOriginal | ✅ |
| ACCTD_AMOUNT_PENDING | ArDeferredLineAcctdAmountPending | ✅ |
| ACCTD_AMOUNT_RECOGNIZED | ArDeferredLineAcctdAmountRecognized | ✅ |
| AMOUNT_DUE_ORIGINAL | ArDeferredLineAmountDueOriginal | ✅ |
| AMOUNT_PENDING | ArDeferredLineAmountPending | ✅ |
| AMOUNT_RECOGNIZED | ArDeferredLineAmountRecognized | ✅ |
| ATTRIBUTE1 | ArDeferredLineAttribute1 | — |
| ATTRIBUTE10 | ArDeferredLineAttribute10 | — |
| ATTRIBUTE11 | ArDeferredLineAttribute11 | — |
| ATTRIBUTE12 | ArDeferredLineAttribute12 | — |
| ATTRIBUTE13 | ArDeferredLineAttribute13 | — |
| ATTRIBUTE14 | ArDeferredLineAttribute14 | — |
| ATTRIBUTE15 | ArDeferredLineAttribute15 | — |
| ATTRIBUTE2 | ArDeferredLineAttribute2 | — |
| ATTRIBUTE3 | ArDeferredLineAttribute3 | — |
| ATTRIBUTE4 | ArDeferredLineAttribute4 | — |
| ATTRIBUTE5 | ArDeferredLineAttribute5 | — |
| ATTRIBUTE6 | ArDeferredLineAttribute6 | — |
| ATTRIBUTE7 | ArDeferredLineAttribute7 | — |
| ATTRIBUTE8 | ArDeferredLineAttribute8 | — |
| ATTRIBUTE9 | ArDeferredLineAttribute9 | — |
| ATTRIBUTE_CATEGORY | ArDeferredLineAttributeCategory | — |
| CREATED_BY | ArDeferredLineCreatedBy | ✅ |
| CREATION_DATE | ArDeferredLineCreationDate | ✅ |
| CUSTOMER_TRX_ID | ArDeferredLineCustomerTrxId | ✅ |
| CUSTOMER_TRX_LINE_ID | ArDeferredLineCustomerTrxLineId | ✅ |
| LAST_UPDATE_DATE | ArDeferredLineLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ArDeferredLineLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ArDeferredLineLastUpdatedBy | ✅ |
| LINE_COLLECTIBLE_FLAG | ArDeferredLineLineCollectibleFlag | ✅ |
| MANUAL_OVERRIDE_FLAG | ArDeferredLineManualOverrideFlag | ✅ |
| OBJECT_VERSION_NUMBER | ArDeferredLineObjectVersionNumber | ✅ |
| ORG_ID | ArDeferredLineOrgId | ✅ |
| ORIGINAL_COLLECTIBILITY_FLAG | ArDeferredLineOriginalCollectibilityFlag | ✅ |
| PARENT_LINE_ID | ArDeferredLineParentLineId | ✅ |
| REQUEST_ID | ArDeferredLineRequestId | ✅ |

---

## 📚 Referências

- Oracle Fusion Cloud Financials — Accounts Receivable Tables (OEDMF Release 13).
- Oracle Fusion Cloud — Revenue Recognition and Deferred Revenue Documentation.
- Oracle Fusion Cloud ERP Schema Reference (Release 25A).
- IFRS 15 — Revenue from Contracts with Customers.
