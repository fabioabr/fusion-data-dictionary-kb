---
id: DOC-AR-022
doc_type: system-doc
title: "AR_MISC_CASH_DISTRIBUTIONS_ALL — Distribuições de Recebimentos Avulsos"
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
  - distribuicoes
  - misc-cash
  - contabilidade
aliases:
  - AR_MISC_CASH_DISTRIBUTIONS_ALL
  - ar_misc_cash_distributions_all
  - distribuicoes-misc-ar
  - misc-cash-distributions
  - distribuicoes-avulsos
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_MISC_CASH_DISTRIBUTIONS_ALL

## 📌 Visão Geral

Armazena as **distribuições contábeis de recebimentos avulsos** (miscellaneous receipts) no módulo Accounts Receivable. Cada registro representa uma linha de distribuição contábil, vinculando um recebimento avulso a uma combinação de contas contábeis (CCID) com valor e percentual. Utilizada quando recebimentos não são aplicados a faturas, mas sim contabilizados diretamente em contas específicas (e.g., juros recebidos, receitas diversas).

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Contabilização de recebimentos avulsos:** Distribuição de valores recebidos sem vinculação a faturas em contas contábeis específicas.
- **Receitas diversas:** Registro contábil de juros, dividendos, reembolsos e outros recebimentos não-faturados.
- **Reconciliação GL:** Base para conciliar recebimentos avulsos com lançamentos no General Ledger.
- **Auditoria:** Rastreabilidade da alocação contábil de cada recebimento avulso.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | MISC_CASH_DISTRIBUTION_ID | NUMBER(18) | NOT NULL | PK | Identificador único da distribuição | — | 🟢 100% |
| 2 | CASH_RECEIPT_ID | NUMBER(18) | NOT NULL | FK | Recebimento avulso associado | [[ar_cash_receipts_all]] | 🟢 100% |
| 3 | CODE_COMBINATION_ID | NUMBER(18) | NOT NULL | Contabilidade | Combinação de contas contábeis (CCID) | [[gl_code_combinations]] | 🟢 100% |
| 4 | AMOUNT | NUMBER | NOT NULL | Financeiro | Valor da distribuição na moeda da transação | — | 🟢 100% |
| 5 | ACCTD_AMOUNT | NUMBER | NULL | Financeiro | Valor na moeda funcional | — | 🟢 100% |
| 6 | PERCENT | NUMBER | NULL | Financeiro | Percentual da distribuição sobre o total | — | 🟢 100% |
| 7 | GL_DATE | DATE | NOT NULL | Contabilidade | Data contábil (General Ledger) | — | 🟢 100% |
| 8 | GL_POSTED_DATE | DATE | NULL | Contabilidade | Data em que foi contabilizado no GL | — | 🟢 100% |
| 9 | POSTING_CONTROL_ID | NUMBER(18) | NULL | Contabilidade | ID do processo de posting | — | 🟢 100% |
| 10 | SET_OF_BOOKS_ID | NUMBER(18) | NULL | Contabilidade | Ledger contábil | [[gl_ledgers]] | 🟢 100% |
| 11 | ACTIVITY_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de atividade do recebimento avulso | — | 🟢 100% |
| 12 | RECEIVABLES_TRX_ID | NUMBER(18) | NULL | Classificação | Tipo de atividade de recebimento | [[ar_receivables_trx_all]] | 🟢 100% |
| 13 | COMMENTS | VARCHAR2(2000) | NULL | Texto livre | Comentários sobre a distribuição | — | 🟡 75% |
| 14 | CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Código da moeda da distribuição | — | 🟢 100% |
| 15 | EXCHANGE_RATE_TYPE | VARCHAR2(30) | NULL | Financeiro | Tipo de taxa de câmbio | — | 🟢 100% |
| 16 | EXCHANGE_RATE | NUMBER | NULL | Financeiro | Taxa de câmbio aplicada | — | 🟢 100% |
| 17 | EXCHANGE_DATE | DATE | NULL | Financeiro | Data da taxa de câmbio | — | 🟢 100% |
| 18 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 19 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 20 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 21 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 22 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 23 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 24 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 100% |
| 25 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ar_cash_receipts_all]] — via `CASH_RECEIPT_ID` (recebimento avulso)
- [[gl_code_combinations]] — via `CODE_COMBINATION_ID` (conta contábil da distribuição de recebimento avulso)
- [[gl_ledgers]] — via `SET_OF_BOOKS_ID` (ledger contábil)
- [[ar_receivables_trx_all]] — via `RECEIVABLES_TRX_ID` (tipo de atividade)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit da distribuição de recebimento avulso)

### Tabelas-filha (FK de saída)
- [[ar_distributions_all]] — via `SOURCE_ID` onde `SOURCE_TABLE = 'MCD'` (distribuições detalhadas)

---

## 📎 Uso Típico

### Distribuições de um recebimento avulso
```sql
SELECT mcd.CODE_COMBINATION_ID, mcd.AMOUNT, mcd.PERCENT,
       mcd.GL_DATE, mcd.GL_POSTED_DATE
FROM   AR_MISC_CASH_DISTRIBUTIONS_ALL mcd
WHERE  mcd.CASH_RECEIPT_ID = :p_cash_receipt_id;
```

### Recebimentos avulsos com distribuição contábil
```sql
SELECT cr.RECEIPT_NUMBER, cr.AMOUNT, mcd.CODE_COMBINATION_ID,
       mcd.AMOUNT AS dist_amount, mcd.GL_DATE
FROM   AR_MISC_CASH_DISTRIBUTIONS_ALL mcd
JOIN   AR_CASH_RECEIPTS_ALL cr ON cr.CASH_RECEIPT_ID = mcd.CASH_RECEIPT_ID
WHERE  cr.TYPE = 'MISC'
  AND  mcd.GL_DATE BETWEEN :start_date AND :end_date
  AND  mcd.ORG_ID = :p_org_id;
```

---

## 🔒 Observações

- A soma dos `PERCENT` de todas as distribuições de um recebimento deve totalizar **100%**.
- A soma dos `AMOUNT` de todas as distribuições deve igualar o `AMOUNT` do recebimento em [[ar_cash_receipts_all]].
- O campo `SET_OF_BOOKS_ID` é legado; em implementações modernas, usar `ORG_ID` para contexto contábil.
- O `POSTING_CONTROL_ID = -3` indica distribuições **ainda não contabilizadas** no GL.

---

## 🔗 PVOs Relacionados

### [[miscellaneousreceiptdistributionextractpvo|MiscellaneousReceiptDistributionExtractPVO]] (OTHER · BICC: 28/44)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT | ArMiscCashDistributionAcctdAmount | ✅ |
| AMOUNT | ArMiscCashDistributionAmount | ✅ |
| APPLY_DATE | ArMiscCashDistributionApplyDate | ✅ |
| ATTRIBUTE1 | ArMiscCashDistributionAttribute1 | — |
| ATTRIBUTE10 | ArMiscCashDistributionAttribute10 | — |
| ATTRIBUTE11 | ArMiscCashDistributionAttribute11 | — |
| ATTRIBUTE12 | ArMiscCashDistributionAttribute12 | — |
| ATTRIBUTE13 | ArMiscCashDistributionAttribute13 | — |
| ATTRIBUTE14 | ArMiscCashDistributionAttribute14 | — |
| ATTRIBUTE15 | ArMiscCashDistributionAttribute15 | — |
| ATTRIBUTE2 | ArMiscCashDistributionAttribute2 | — |
| ATTRIBUTE3 | ArMiscCashDistributionAttribute3 | — |
| ATTRIBUTE4 | ArMiscCashDistributionAttribute4 | — |
| ATTRIBUTE5 | ArMiscCashDistributionAttribute5 | — |
| ATTRIBUTE6 | ArMiscCashDistributionAttribute6 | — |
| ATTRIBUTE7 | ArMiscCashDistributionAttribute7 | — |
| ATTRIBUTE8 | ArMiscCashDistributionAttribute8 | — |
| ATTRIBUTE9 | ArMiscCashDistributionAttribute9 | — |
| ATTRIBUTE_CATEGORY | ArMiscCashDistributionAttributeCategory | — |
| CASH_RECEIPT_HISTORY_ID | ArMiscCashDistributionCashReceiptHistoryId | ✅ |
| CASH_RECEIPT_ID | ArMiscCashDistributionCashReceiptId | ✅ |
| CODE_COMBINATION_ID | ArMiscCashDistributionCodeCombinationId | ✅ |
| COMMENTS | ArMiscCashDistributionComments | ✅ |
| CREATED_BY | ArMiscCashDistributionCreatedBy | ✅ |
| CREATED_FROM | ArMiscCashDistributionCreatedFrom | ✅ |
| CREATION_DATE | ArMiscCashDistributionCreationDate | ✅ |
| EVENT_ID | ArMiscCashDistributionEventId | ✅ |
| GL_DATE | ArMiscCashDistributionGlDate | ✅ |
| GL_POSTED_DATE | ArMiscCashDistributionGlPostedDate | ✅ |
| LAST_UPDATE_DATE | ArMiscCashDistributionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ArMiscCashDistributionLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ArMiscCashDistributionLastUpdatedBy | ✅ |
| MISC_CASH_DISTRIBUTION_ID | ArMiscCashDistributionMiscCashDistributionId | ✅ |
| OBJECT_VERSION_NUMBER | ArMiscCashDistributionObjectVersionNumber | ✅ |
| ORG_ID | ArMiscCashDistributionOrgId | ✅ |
| PERCENT | ArMiscCashDistributionPercent | ✅ |
| POSTING_CONTROL_ID | ArMiscCashDistributionPostingControlId | ✅ |
| PROGRAM_APPLICATION_ID | ArMiscCashDistributionProgramApplicationId | ✅ |
| PROGRAM_ID | ArMiscCashDistributionProgramId | ✅ |
| PROGRAM_UPDATE_DATE | ArMiscCashDistributionProgramUpdateDate | ✅ |
| REQUEST_ID | ArMiscCashDistributionRequestId | ✅ |
| REVERSAL_GL_DATE | ArMiscCashDistributionReversalGlDate | ✅ |
| SET_OF_BOOKS_ID | ArMiscCashDistributionSetOfBooksId | ✅ |
| USSGL_TRANSACTION_CODE_CONTEXT | ArMiscCashDistributionUssglTransactionCodeContext | ✅ |

### [[miscreceiptdistributionpvo|MiscReceiptDistributionPVO]] (AR · BICC: 4/32)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT | MiscReceiptDistAcctdAmount | — |
| AMOUNT | MiscReceiptDistAmount | — |
| APPLY_DATE | MiscReceiptDistApplyDate | — |
| CASH_RECEIPT_HISTORY_ID | MiscReceiptDistCashReceiptHistoryId | — |
| CASH_RECEIPT_ID | MiscReceiptDistCashReceiptId | — |
| CODE_COMBINATION_ID | MiscReceiptDistCodeCombinationId | — |
| COMMENTS | MiscReceiptDistComments | — |
| CREATED_BY | MiscReceiptDistCreatedBy | — |
| CREATED_FROM | MiscReceiptDistCreatedFrom | — |
| CREATION_DATE | MiscReceiptDistCreationDate | — |
| EVENT_ID | MiscReceiptDistEventId | — |
| GL_DATE | MiscReceiptDistGlDate | ✅ |
| GL_POSTED_DATE | MiscReceiptDistGlPostedDate | — |
| LAST_UPDATE_DATE | MiscReceiptDistLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | MiscReceiptDistLastUpdateLogin | — |
| LAST_UPDATED_BY | MiscReceiptDistLastUpdatedBy | — |
| MISC_CASH_DISTRIBUTION_ID | MiscReceiptDistMiscCashDistributionId | — |
| MRC_ACCTD_AMOUNT | MiscReceiptDistMrcAcctdAmount | — |
| MRC_GL_POSTED_DATE | MiscReceiptDistMrcGlPostedDate | — |
| MRC_POSTING_CONTROL_ID | MiscReceiptDistMrcPostingControlId | — |
| OBJECT_VERSION_NUMBER | MiscReceiptDistObjectVersionNumber | — |
| ORG_ID | MiscReceiptDistOrgId | — |
| PERCENT | MiscReceiptDistPercent | ✅ |
| POSTING_CONTROL_ID | MiscReceiptDistPostingControlId | ✅ |
| PROGRAM_APPLICATION_ID | MiscReceiptDistProgramApplicationId | — |
| PROGRAM_ID | MiscReceiptDistProgramId | — |
| PROGRAM_UPDATE_DATE | MiscReceiptDistProgramUpdateDate | — |
| REQUEST_ID | MiscReceiptDistRequestId | — |
| REVERSAL_GL_DATE | MiscReceiptDistReversalGlDate | — |
| SET_OF_BOOKS_ID | MiscReceiptDistSetOfBooksId | — |
| USSGL_TRANSACTION_CODE | MiscReceiptDistUssglTransactionCode | — |
| USSGL_TRANSACTION_CODE_CONTEXT | MiscReceiptDistUssglTransactionCodeContext | — |

---

## 📚 Referências

- [Oracle Docs — AR_MISC_CASH_DISTRIBUTIONS_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/armisccashdistributionsall-10047.html)
- [[ar-module-data-dictionary]] — Dossiê do módulo AR
