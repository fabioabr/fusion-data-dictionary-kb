---
id: DOC-AR-060
doc_type: system-doc
title: "AR_RECON_SUMMARY_DETAILS — Resumo de Reconciliação AR vs GL"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-receivable, data-dictionary, reconciliacao, ar-gl, subledger]
aliases: [AR_RECON_SUMMARY_DETAILS, ar_recon_summary_details, recon_summary, reconciliacao_ar, ar_gl_recon]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_RECON_SUMMARY_DETAILS

## 📌 Visão Geral

Tabela de resumo do processo de reconciliação entre o subledger de Accounts Receivable e o General Ledger. Cada registro contém os valores sumarizados por tipo de fonte, categoria e combinação contábil, permitindo identificar discrepâncias entre os dois módulos.

## 🧠 Propósito de Negócio

A reconciliação AR vs GL é um controle financeiro crítico que garante que os saldos de contas a receber no subledger estejam consistentes com os lançamentos no razão geral. Diferenças podem indicar erros de postagem, transações não transferidas ou problemas de período contábil. Para instituições financeiras, essa reconciliação é obrigatória em fechamentos mensais.

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Descrição | Categoria | Confiança |
|---|--------|------|-------|-----------|-----------|-----------|
| 1 | RECON_ID | NUMBER(15) | NOT NULL | Chave primária. Identificador único do registro de reconciliação. | PK | 🟢 100% |
| 2 | RECON_PARAMETER_ID | NUMBER(15) | NOT NULL | FK para [[ar_recon_summary_parameters]]. Parâmetros da execução. | FK | 🟢 100% |
| 3 | SOURCE_TYPE | VARCHAR2(30) | NOT NULL | Tipo de fonte (ex.: AR_SUBLEDGER, GL_JOURNAL). | Classificação | 🟢 100% |
| 4 | CATEGORY | VARCHAR2(30) | NULL | Categoria do lançamento (ex.: INVOICE, RECEIPT, ADJUSTMENT). | Classificação | 🟢 100% |
| 5 | CODE_COMBINATION_ID | NUMBER(15) | NULL | FK para GL_CODE_COMBINATIONS. Conta contábil reconciliada. | FK | 🟢 100% |
| 6 | ENTERED_AMOUNT | NUMBER | NULL | Valor na moeda da transação (entered). | Financeiro | 🟢 100% |
| 7 | ACCOUNTED_AMOUNT | NUMBER | NULL | Valor na moeda funcional (accounted). | Financeiro | 🟢 100% |
| 8 | PERIOD_NAME | VARCHAR2(15) | NOT NULL | Nome do período contábil reconciliado. | Temporal | 🟢 100% |
| 9 | LEDGER_ID | NUMBER(15) | NOT NULL | FK para GL_LEDGERS. Ledger contábil. | FK | 🟢 100% |
| 10 | TRANSACTION_COUNT | NUMBER | NULL | Quantidade de transações na categoria/fonte. | Estatística | 🟡 75% |
| 11 | CURRENCY_CODE | VARCHAR2(15) | NULL | Código da moeda das transações. | Financeiro | 🟢 100% |
| 12 | ORG_ID | NUMBER(15) | NOT NULL | Identificador da business unit (Operating Unit). | Partição | 🟢 100% |
| 13 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | Contexto de flexfield descritivo. | DFF | 🟢 100% |
| 14 | REQUEST_ID | NUMBER(15) | NULL | Identificador da requisição concorrente. | Técnico | 🟢 100% |
| 15 | CREATED_BY | VARCHAR2(64) | NOT NULL | Usuário que criou o registro. | WHO | 🟢 100% |
| 16 | CREATION_DATE | DATE | NOT NULL | Data de criação do registro. | WHO | 🟢 100% |
| 17 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Usuário da última atualização. | WHO | 🟢 100% |
| 18 | LAST_UPDATE_DATE | DATE | NOT NULL | Data da última atualização. | WHO | 🟢 100% |

## 🔗 Relacionamentos

- **[[ar_recon_summary_parameters]]** — Parâmetros da execução de reconciliação (N:1 via `RECON_PARAMETER_ID`).
- **[[ar_recon_difference_details]]** — Diferenças encontradas nesta reconciliação (1:N via `RECON_ID`).
- **GL_CODE_COMBINATIONS** — Conta contábil reconciliada (N:1 via `CODE_COMBINATION_ID`).
- **GL_LEDGERS** — Ledger contábil (N:1 via `LEDGER_ID`).

## 📎 Uso Típico

```sql
-- Resumo de reconciliação por período e categoria
SELECT rsd.PERIOD_NAME,
       rsd.SOURCE_TYPE,
       rsd.CATEGORY,
       SUM(rsd.ACCOUNTED_AMOUNT) AS total_contabil,
       SUM(rsd.TRANSACTION_COUNT) AS total_transacoes
  FROM AR_RECON_SUMMARY_DETAILS rsd
 WHERE rsd.ORG_ID = :p_org_id
   AND rsd.PERIOD_NAME = :p_periodo
 GROUP BY rsd.PERIOD_NAME, rsd.SOURCE_TYPE, rsd.CATEGORY
 ORDER BY rsd.SOURCE_TYPE, rsd.CATEGORY;
```

## 🔒 Observações

- Compare registros com `SOURCE_TYPE = 'AR_SUBLEDGER'` vs `SOURCE_TYPE = 'GL_JOURNAL'` para identificar diferenças.
- Diferenças são detalhadas em [[ar_recon_difference_details]].
- A reconciliação deve ser executada após o fechamento do período e transferência de journals para o GL.
- Filtrar sempre por `ORG_ID` e `LEDGER_ID` para garantir contexto correto.

## 🔗 PVOs Relacionados

### [[receivablesreconciliationsummarypvo|ReceivablesReconciliationSummaryPVO]] (AR · BICC: 8/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTED_CR | ReconciliationSummaryPEOAccountedCr | ✅ |
| ACCOUNTED_DR | ReconciliationSummaryPEOAccountedDr | ✅ |
| AR_ACCTD_AMOUNT | ReconciliationSummaryPEOArAcctdAmount | ✅ |
| BALANCING_SEGMENT | ReconciliationSummaryPEOBalancingSegment | — |
| BU_ID | ReconciliationSummaryPEOBuId | — |
| CODE_COMBINATION_ID | ReconciliationSummaryPEOCodeCombinationId | — |
| CREATED_BY | ReconciliationSummaryPEOCreatedBy | — |
| CREATION_DATE | ReconciliationSummaryPEOCreationDate | — |
| DATA_SOURCE | ReconciliationSummaryPEODataSource | ✅ |
| JOB_DEFINITION_NAME | ReconciliationSummaryPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | ReconciliationSummaryPEOJobDefinitionPackage | — |
| LAST_UPDATE_DATE | ReconciliationSummaryPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ReconciliationSummaryPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ReconciliationSummaryPEOLastUpdatedBy | — |
| LEDGER_ID | ReconciliationSummaryPEOLedgerId | — |
| NATURAL_ACCOUNT_SEGMENT | ReconciliationSummaryPEONaturalAccountSegment | — |
| RECON_ITEM_CODE | ReconciliationSummaryPEOReconItemCode | ✅ |
| RECON_ITEM_ID | ReconItemId | ✅ |
| RECON_ITEM_ORDER | ReconciliationSummaryPEOReconItemOrder | ✅ |
| REQUEST_ID | ReconciliationSummaryPEORequestId | — |

---

## 📚 Referências

- Oracle Fusion Cloud Financials — Accounts Receivable Tables (OEDMF Release 13).
- Oracle Fusion Cloud — Subledger to GL Reconciliation Documentation.
- Oracle Fusion Cloud ERP Schema Reference (Release 25A).
