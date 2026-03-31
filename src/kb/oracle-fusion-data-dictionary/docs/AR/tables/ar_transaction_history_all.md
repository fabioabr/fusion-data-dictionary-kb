---
id: DOC-AR-063
doc_type: system-doc
title: "AR_TRANSACTION_HISTORY_ALL — Histórico de Bills Receivable"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-receivable, data-dictionary, historico, bills-receivable, ciclo-vida]
aliases: [AR_TRANSACTION_HISTORY_ALL, ar_transaction_history_all, transaction_history, historico_transacoes, bills_receivable_hist]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_TRANSACTION_HISTORY_ALL

> [!note] Sufixo _ALL
> Tabela particionada por `ORG_ID`. O sufixo `_ALL` indica que contém dados de todas as business units. Acessos via views sem sufixo filtram automaticamente pelo contexto de segurança da sessão.

## 📌 Visão Geral

Tabela de histórico de bills receivable (títulos a receber / duplicatas) do Accounts Receivable. Registra todas as atividades e eventos do ciclo de vida de um bill receivable, desde a criação até a liquidação, incluindo endossos, protestos, descontos e remessas a bancos.

## 🧠 Propósito de Negócio

Bills receivable são instrumentos financeiros negociáveis que representam a promessa de pagamento de um cliente. No Brasil, correspondem a duplicatas e boletos bancários. O histórico rastreia cada evento do ciclo de vida: criação, aceitação, remessa ao banco, desconto, protesto, liquidação. Essencial para: (1) auditoria de operações de desconto bancário, (2) controle de custódia de títulos, (3) contabilização correta em cada etapa do ciclo.

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Descrição | Categoria | Confiança |
|---|--------|------|-------|-----------|-----------|-----------|
| 1 | TRANSACTION_HISTORY_ID | NUMBER(15) | NOT NULL | Chave primária. Identificador único do registro histórico. | PK | 🟢 100% |
| 2 | CUSTOMER_TRX_ID | NUMBER(15) | NOT NULL | FK para RA_CUSTOMER_TRX_ALL. Bill receivable associado. | FK | 🟢 100% |
| 3 | TRX_DATE | DATE | NOT NULL | Data da transação/evento registrado. | Temporal | 🟢 100% |
| 4 | EVENT | VARCHAR2(30) | NOT NULL | Tipo de evento (ex.: CREATED, ACCEPTED, REMITTED, CLOSED). | Classificação | 🟢 100% |
| 5 | STATUS | VARCHAR2(30) | NOT NULL | Status do bill receivable após o evento. | Controle | 🟢 100% |
| 6 | BATCH_ID | NUMBER(15) | NULL | FK para batch de processamento, se aplicável. | FK | 🟢 100% |
| 7 | MATURITY_DATE | DATE | NULL | Data de vencimento do bill receivable. | Temporal | 🟢 100% |
| 8 | CURRENT_ACCOUNTED_FLAG | VARCHAR2(1) | NULL | Indica se este é o registro contábil corrente (Y/N). | Controle | 🟢 100% |
| 9 | POSTABLE_FLAG | VARCHAR2(1) | NULL | Indica se o evento gera lançamento contábil (Y/N). | Controle | 🟢 100% |
| 10 | GL_DATE | DATE | NULL | Data contábil do evento. | Temporal | 🟢 100% |
| 11 | GL_POSTED_DATE | DATE | NULL | Data em que o lançamento foi efetivamente postado no GL. | Temporal | 🟢 100% |
| 12 | FIRST_POSTED_RECORD_FLAG | VARCHAR2(1) | NULL | Indica se é o primeiro registro postado do bill (Y/N). | Controle | 🟢 100% |
| 13 | POSTING_CONTROL_ID | NUMBER(15) | NULL | FK para controle de postagem no GL. | FK | 🟢 100% |
| 14 | COMMENTS | VARCHAR2(240) | NULL | Comentários sobre o evento. | Negócio | 🟢 100% |
| 15 | PROMISOR_ID | NUMBER(15) | NULL | FK para o promitente (drawee) do bill receivable. | FK | 🟢 100% |
| 16 | DRAWEE_ID | NUMBER(15) | NULL | FK para o sacado do bill receivable. | FK | 🟡 75% |
| 17 | EVENT_ID | NUMBER(15) | NULL | Identificador do evento contábil (SLA). | FK | 🟢 100% |
| 18 | CREATED_FROM_PROGRAM | VARCHAR2(30) | NULL | Programa que originou o registro. | Técnico | 🟡 75% |
| 19 | ORG_ID | NUMBER(15) | NOT NULL | Identificador da business unit (Operating Unit). | Partição | 🟢 100% |
| 20 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | Contexto de flexfield descritivo. | DFF | 🟢 100% |
| 21 | REQUEST_ID | NUMBER(15) | NULL | Identificador da requisição concorrente. | Técnico | 🟢 100% |
| 22 | CREATED_BY | VARCHAR2(64) | NOT NULL | Usuário que criou o registro. | WHO | 🟢 100% |
| 23 | CREATION_DATE | DATE | NOT NULL | Data de criação do registro. | WHO | 🟢 100% |
| 24 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Usuário da última atualização. | WHO | 🟢 100% |
| 25 | LAST_UPDATE_DATE | DATE | NOT NULL | Data da última atualização. | WHO | 🟢 100% |

## 🔗 Relacionamentos

- **RA_CUSTOMER_TRX_ALL** — Bill receivable associado (N:1 via `CUSTOMER_TRX_ID`).
- **AR_BATCHES_ALL** — Batch de processamento (N:1 via `BATCH_ID`).
- **HZ_CUST_ACCOUNTS** — Promitente/Sacado (via `PROMISOR_ID`, `DRAWEE_ID`).

## 📎 Uso Típico

```sql
-- Ciclo de vida de um bill receivable específico
SELECT th.TRANSACTION_HISTORY_ID,
       th.TRX_DATE,
       th.EVENT,
       th.STATUS,
       th.MATURITY_DATE,
       th.GL_DATE,
       th.POSTABLE_FLAG
  FROM AR_TRANSACTION_HISTORY_ALL th
 WHERE th.CUSTOMER_TRX_ID = :p_customer_trx_id
 ORDER BY th.TRX_DATE, th.TRANSACTION_HISTORY_ID;
```

## 🔒 Observações

- `CURRENT_ACCOUNTED_FLAG = 'Y'` identifica o registro contábil corrente do bill receivable.
- Eventos típicos incluem: CREATED, ACCEPTED, REMITTED, FACTORED, MATURED, CLOSED, PROTESTED, UNPAID.
- No contexto brasileiro, esta tabela é relevante para controle de duplicatas e operações de desconto bancário.
- `POSTABLE_FLAG = 'Y'` indica que o evento gerou (ou deve gerar) lançamento contábil no GL.
- Filtrar sempre por `ORG_ID` para garantir contexto correto de business unit.

## 🔗 PVOs Relacionados

### [[transactionhistoryallextractpvo|TransactionHistoryAllExtractPVO]] (OTHER · BICC: 42/42)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | TransactionHistoryAllAttribute1 | ✅ |
| ATTRIBUTE10 | TransactionHistoryAllAttribute10 | ✅ |
| ATTRIBUTE11 | TransactionHistoryAllAttribute11 | ✅ |
| ATTRIBUTE12 | TransactionHistoryAllAttribute12 | ✅ |
| ATTRIBUTE13 | TransactionHistoryAllAttribute13 | ✅ |
| ATTRIBUTE14 | TransactionHistoryAllAttribute14 | ✅ |
| ATTRIBUTE15 | TransactionHistoryAllAttribute15 | ✅ |
| ATTRIBUTE2 | TransactionHistoryAllAttribute2 | ✅ |
| ATTRIBUTE3 | TransactionHistoryAllAttribute3 | ✅ |
| ATTRIBUTE4 | TransactionHistoryAllAttribute4 | ✅ |
| ATTRIBUTE5 | TransactionHistoryAllAttribute5 | ✅ |
| ATTRIBUTE6 | TransactionHistoryAllAttribute6 | ✅ |
| ATTRIBUTE7 | TransactionHistoryAllAttribute7 | ✅ |
| ATTRIBUTE8 | TransactionHistoryAllAttribute8 | ✅ |
| ATTRIBUTE9 | TransactionHistoryAllAttribute9 | ✅ |
| ATTRIBUTE_CATEGORY | TransactionHistoryAllAttributeCategory | ✅ |
| BATCH_ID | TransactionHistoryAllBatchId | ✅ |
| COMMENTS | TransactionHistoryAllComments | ✅ |
| CREATED_BY | TransactionHistoryAllCreatedBy | ✅ |
| CREATED_FROM | TransactionHistoryAllCreatedFrom | ✅ |
| CREATION_DATE | TransactionHistoryAllCreationDate | ✅ |
| CURRENT_ACCOUNTED_FLAG | TransactionHistoryAllCurrentAccountedFlag | ✅ |
| CURRENT_RECORD_FLAG | TransactionHistoryAllCurrentRecordFlag | ✅ |
| CUSTOMER_TRX_ID | TransactionHistoryAllCustomerTrxId | ✅ |
| EVENT | TransactionHistoryAllEvent | ✅ |
| EVENT_ID | TransactionHistoryAllEventId | ✅ |
| FIRST_POSTED_RECORD_FLAG | TransactionHistoryAllFirstPostedRecordFlag | ✅ |
| GL_DATE | TransactionHistoryAllGlDate | ✅ |
| GL_POSTED_DATE | TransactionHistoryAllGlPostedDate | ✅ |
| LAST_UPDATE_DATE | TransactionHistoryAllLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TransactionHistoryAllLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | TransactionHistoryAllLastUpdatedBy | ✅ |
| MATURITY_DATE | TransactionHistoryAllMaturityDate | ✅ |
| OBJECT_VERSION_NUMBER | TransactionHistoryAllObjectVersionNumber | ✅ |
| ORG_ID | TransactionHistoryAllOrgId | ✅ |
| POSTABLE_FLAG | TransactionHistoryAllPostableFlag | ✅ |
| POSTING_CONTROL_ID | TransactionHistoryAllPostingControlId | ✅ |
| PRV_TRX_HISTORY_ID | TransactionHistoryAllPrvTrxHistoryId | ✅ |
| REQUEST_ID | TransactionHistoryAllRequestId | ✅ |
| STATUS | TransactionHistoryAllStatus | ✅ |
| TRANSACTION_HISTORY_ID | TransactionHistoryAllTransactionHistoryId | ✅ |
| TRX_DATE | TransactionHistoryAllTrxDate | ✅ |

### [[transactionhistorydistributionpvo|TransactionHistoryDistributionPVO]] (AR · BICC: 15/33)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE_CATEGORY | TransactionHistoryAttributeCategory | — |
| BATCH_ID | TransactionHistoryBatchId | — |
| COMMENTS | TransactionHistoryComments | ✅ |
| CREATED_BY | TransactionHistoryCreatedBy | ✅ |
| CREATED_FROM | TransactionHistoryCreatedFrom | — |
| CREATION_DATE | TransactionHistoryCreationDate | ✅ |
| CURRENT_ACCOUNTED_FLAG | TransactionHistoryCurrentAccountedFlag | ✅ |
| CURRENT_RECORD_FLAG | TransactionHistoryCurrentRecordFlag | ✅ |
| CUSTOMER_TRX_ID | TransactionHistoryCustomerTrxId | — |
| EVENT | TransactionHistoryEvent | ✅ |
| EVENT_ID | TransactionHistoryEventId | — |
| FIRST_POSTED_RECORD_FLAG | TransactionHistoryFirstPostedRecordFlag | — |
| GL_DATE | TransactionHistoryGlDate | ✅ |
| GL_POSTED_DATE | TransactionHistoryGlPostedDate | ✅ |
| LAST_UPDATE_DATE | TransactionHistoryLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TransactionHistoryLastUpdateLogin | — |
| LAST_UPDATED_BY | TransactionHistoryLastUpdatedBy | ✅ |
| MATURITY_DATE | TransactionHistoryMaturityDate | ✅ |
| MRC_CREATED_FROM | TransactionHistoryMrcCreatedFrom | — |
| MRC_GL_POSTED_DATE | TransactionHistoryMrcGlPostedDate | — |
| MRC_POSTING_CONTROL_ID | TransactionHistoryMrcPostingControlId | — |
| OBJECT_VERSION_NUMBER | TransactionHistoryObjectVersionNumber | — |
| ORG_ID | OrgId | — |
| POSTABLE_FLAG | TransactionHistoryPostableFlag | ✅ |
| POSTING_CONTROL_ID | TransactionHistoryPostingControlId | ✅ |
| PROGRAM_APPLICATION_ID | TransactionHistoryProgramApplicationId | — |
| PROGRAM_ID | TransactionHistoryProgramId | — |
| PROGRAM_UPDATE_DATE | TransactionHistoryProgramUpdateDate | — |
| PRV_TRX_HISTORY_ID | TransactionHistoryPrvTrxHistoryId | — |
| REQUEST_ID | TransactionHistoryRequestId | — |
| STATUS | TransactionHistoryStatus | ✅ |
| TRANSACTION_HISTORY_ID | TransactionHistoryTransactionHistoryId | — |
| TRX_DATE | TransactionHistoryTrxDate | ✅ |

### [[transactionhistorypvo|TransactionHistoryPVO]] (AR · BICC: 15/33)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE_CATEGORY | TransactionHistoryAttributeCategory | — |
| BATCH_ID | TransactionHistoryBatchId | — |
| COMMENTS | TransactionHistoryComments | — |
| CREATED_BY | TransactionHistoryCreatedBy | ✅ |
| CREATED_FROM | TransactionHistoryCreatedFrom | — |
| CREATION_DATE | TransactionHistoryCreationDate | ✅ |
| CURRENT_ACCOUNTED_FLAG | TransactionHistoryCurrentAccountedFlag | ✅ |
| CURRENT_RECORD_FLAG | TransactionHistoryCurrentRecordFlag | ✅ |
| CUSTOMER_TRX_ID | TransactionHistoryCustomerTrxId | — |
| EVENT | TransactionHistoryEvent | ✅ |
| EVENT_ID | TransactionHistoryEventId | — |
| FIRST_POSTED_RECORD_FLAG | TransactionHistoryFirstPostedRecordFlag | — |
| GL_DATE | TransactionHistoryGlDate | ✅ |
| GL_POSTED_DATE | TransactionHistoryGlPostedDate | ✅ |
| LAST_UPDATE_DATE | TransactionHistoryLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TransactionHistoryLastUpdateLogin | — |
| LAST_UPDATED_BY | TransactionHistoryLastUpdatedBy | ✅ |
| MATURITY_DATE | TransactionHistoryMaturityDate | ✅ |
| MRC_CREATED_FROM | TransactionHistoryMrcCreatedFrom | — |
| MRC_GL_POSTED_DATE | TransactionHistoryMrcGlPostedDate | — |
| MRC_POSTING_CONTROL_ID | TransactionHistoryMrcPostingControlId | — |
| OBJECT_VERSION_NUMBER | TransactionHistoryObjectVersionNumber | — |
| ORG_ID | TransactionHistoryOrgId | — |
| POSTABLE_FLAG | TransactionHistoryPostableFlag | ✅ |
| POSTING_CONTROL_ID | TransactionHistoryPostingControlId | ✅ |
| PROGRAM_APPLICATION_ID | TransactionHistoryProgramApplicationId | — |
| PROGRAM_ID | TransactionHistoryProgramId | — |
| PROGRAM_UPDATE_DATE | TransactionHistoryProgramUpdateDate | — |
| PRV_TRX_HISTORY_ID | TransactionHistoryPrvTrxHistoryId | — |
| REQUEST_ID | TransactionHistoryRequestId | — |
| STATUS | TransactionHistoryStatus | ✅ |
| TRANSACTION_HISTORY_ID | TransactionHistoryId | ✅ |
| TRX_DATE | TransactionHistoryTrxDate | ✅ |

---

## 📚 Referências

- Oracle Fusion Cloud Financials — Accounts Receivable Tables (OEDMF Release 13).
- Oracle Fusion Cloud — Bills Receivable Lifecycle Documentation.
- Oracle Fusion Cloud ERP Schema Reference (Release 25A).
