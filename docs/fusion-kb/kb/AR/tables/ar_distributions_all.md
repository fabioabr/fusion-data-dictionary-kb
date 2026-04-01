---
id: DOC-AR-028
doc_type: system-doc
title: "AR_DISTRIBUTIONS_ALL — Distribuições Contábeis de Recebimentos"
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
  - distribuicoes-contabeis
  - accounting-distributions
  - subledger
aliases:
  - AR_DISTRIBUTIONS_ALL
  - ar_distributions_all
  - distribuicoes-contabeis-ar
  - ar-distributions
  - accounting-distributions-ar
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_DISTRIBUTIONS_ALL

## 📌 Visão Geral

Armazena as **distribuições contábeis** de recebimentos, ajustes e aplicações do módulo Accounts Receivable. Cada registro representa uma linha de débito ou crédito contábil vinculada a uma entidade-origem identificada por `SOURCE_TABLE` + `SOURCE_ID`. É a tabela central de contabilização do lado de recebimentos do AR — complementar a [[ra_cust_trx_line_gl_dist_all]] que trata das distribuições de transações (faturas).

As entidades-origem incluem:
- **RA** — Receivable Applications ([[ar_receivable_applications_all]])
- **ARR** — Adjustments (histórico legado)
- **ADJ** — Adjustments ([[ar_adjustments_all]])
- **MCD** — Misc Cash Distributions ([[ar_misc_cash_distributions_all]])
- **CRH** — Cash Receipt History ([[ar_cash_receipt_history_all]])

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Contabilização de recebimentos:** Geração de lançamentos contábeis (débito/crédito) para cada etapa do ciclo de vida do recebimento.
- **Contabilização de ajustes:** Distribuições contábeis de write-offs e reclassificações.
- **Contabilização de aplicações:** Lançamentos gerados quando recebimentos são aplicados a faturas.
- **Reconciliação AR × GL:** Base para conciliar o subledger AR com o General Ledger.
- **Subledger Accounting (XLA):** Fonte de dados para o mecanismo de contabilização do subledger.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LINE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da linha de distribuição | — | 🟢 100% |
| 2 | SOURCE_ID | NUMBER(18) | NOT NULL | FK | ID da entidade-origem (varia conforme SOURCE_TABLE) | — | 🟢 100% |
| 3 | SOURCE_TABLE | VARCHAR2(10) | NOT NULL | Classificação | Tabela de origem: RA, ARR, ADJ, MCD, CRH | — | 🟢 100% |
| 4 | SOURCE_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo da distribuição (REC/UNAPP/ACC/FACTOR/REMITTANCE/etc.) | — | 🟢 100% |
| 5 | CODE_COMBINATION_ID | NUMBER(18) | NOT NULL | Contabilidade | Combinação de contas contábeis (CCID) | [[gl_code_combinations]] | 🟢 100% |
| 6 | AMOUNT_DR | NUMBER | NULL | Financeiro | Valor a débito na moeda da transação | — | 🟢 100% |
| 7 | AMOUNT_CR | NUMBER | NULL | Financeiro | Valor a crédito na moeda da transação | — | 🟢 100% |
| 8 | ACCTD_AMOUNT_DR | NUMBER | NULL | Financeiro | Valor a débito na moeda funcional | — | 🟢 100% |
| 9 | ACCTD_AMOUNT_CR | NUMBER | NULL | Financeiro | Valor a crédito na moeda funcional | — | 🟢 100% |
| 10 | CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Código da moeda da transação | — | 🟢 100% |
| 11 | CURRENCY_CONVERSION_RATE | NUMBER | NULL | Financeiro | Taxa de conversão cambial | — | 🟢 100% |
| 12 | CURRENCY_CONVERSION_TYPE | VARCHAR2(30) | NULL | Financeiro | Tipo de conversão cambial | — | 🟢 100% |
| 13 | CURRENCY_CONVERSION_DATE | DATE | NULL | Financeiro | Data da conversão cambial | — | 🟢 100% |
| 14 | THIRD_PARTY_ID | NUMBER(18) | NULL | Cliente | ID do terceiro (cliente) | [[hz_cust_accounts]] | 🟢 100% |
| 15 | THIRD_PARTY_SUB_ID | NUMBER(18) | NULL | Cliente | ID do sub-terceiro (site do cliente) | [[hz_cust_site_uses_all]] | 🟢 100% |
| 16 | GL_DATE | DATE | NULL | Contabilidade | Data contábil | — | 🟢 100% |
| 17 | GL_POSTED_DATE | DATE | NULL | Contabilidade | Data de contabilização no GL | — | 🟡 75% |
| 18 | POSTING_CONTROL_ID | NUMBER(18) | NULL | Contabilidade | ID do processo de posting | — | 🟢 100% |
| 19 | SET_OF_BOOKS_ID | NUMBER(18) | NULL | Contabilidade | Ledger contábil | [[gl_ledgers]] | 🟢 100% |
| 20 | TAX_CODE_ID | NUMBER(18) | NULL | Fiscal | Código de imposto associado | — | 🟡 70% |
| 21 | ACTIVITY_BUCKET | VARCHAR2(30) | NULL | Classificação | Bucket de atividade (para subledger accounting) | — | 🟡 70% |
| 22 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 23 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 24 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 25 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 26 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 27 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada — via SOURCE_TABLE + SOURCE_ID)
- [[gl_code_combinations]] — via `CODE_COMBINATION_ID` (conta contábil da distribuição de recebíveis)
- [[hz_cust_accounts]] — via `THIRD_PARTY_ID` (cliente associado à distribuição contábil)
- [[hz_cust_site_uses_all]] — via `THIRD_PARTY_SUB_ID` (site do cliente na distribuição contábil)
- [[gl_ledgers]] — via `SET_OF_BOOKS_ID` (ledger contábil da distribuição de AR)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit da distribuição de recebíveis)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Distribuições de uma aplicação de recebimento
```sql
SELECT d.SOURCE_TYPE, d.CODE_COMBINATION_ID,
       d.AMOUNT_DR, d.AMOUNT_CR, d.CURRENCY_CODE
FROM   AR_DISTRIBUTIONS_ALL d
WHERE  d.SOURCE_TABLE = 'RA'
  AND  d.SOURCE_ID = :p_receivable_application_id;
```

### Distribuições de ajustes por período
```sql
SELECT d.SOURCE_ID, d.SOURCE_TYPE, d.CODE_COMBINATION_ID,
       d.AMOUNT_DR, d.AMOUNT_CR, d.GL_DATE
FROM   AR_DISTRIBUTIONS_ALL d
WHERE  d.SOURCE_TABLE = 'ADJ'
  AND  d.GL_DATE BETWEEN :start_date AND :end_date
  AND  d.ORG_ID = :p_org_id;
```

### Total de distribuições por tipo de origem
```sql
SELECT d.SOURCE_TABLE,
       SUM(NVL(d.AMOUNT_DR, 0)) AS total_dr,
       SUM(NVL(d.AMOUNT_CR, 0)) AS total_cr
FROM   AR_DISTRIBUTIONS_ALL d
WHERE  d.GL_DATE BETWEEN :start_date AND :end_date
  AND  d.ORG_ID = :p_org_id
GROUP BY d.SOURCE_TABLE;
```

---

## 🔒 Observações

- O par `SOURCE_TABLE` + `SOURCE_ID` é a **chave de vinculação polimórfica** — cada valor de `SOURCE_TABLE` direciona a um tipo diferente de tabela-origem.
- Os valores de `SOURCE_TYPE` variam conforme o `SOURCE_TABLE`: para CRH pode ser CASH, CONFIRMATION, REMITTANCE; para RA pode ser REC, UNAPP, ACC; para ADJ pode ser ADJ.
- A soma de `AMOUNT_DR` e `AMOUNT_CR` deve balancear (débito = crédito) para cada `SOURCE_ID` + `SOURCE_TABLE`.
- O campo `SET_OF_BOOKS_ID` é legado; em implementações modernas, usar `ORG_ID` para contexto contábil.
- O `POSTING_CONTROL_ID = -3` indica distribuições **ainda não contabilizadas** no GL.

---

## 🔗 PVOs Relacionados

### [[adjustmentdistributionpvo|AdjustmentDistributionPVO]] (AR · BICC: 23/103)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_CR | CashDistributionAcctdAmountCr | ✅ |
| ACCTD_AMOUNT_CR | CshDistRefLineAcctdAmountCr | — |
| ACCTD_AMOUNT_CR | CshDistRevSrcAcctdAmountCr | — |
| ACCTD_AMOUNT_DR | CashDistributionAcctdAmountDr | ✅ |
| ACCTD_AMOUNT_DR | CshDistRefLineAcctdAmountDr | — |
| ACCTD_AMOUNT_DR | CshDistRevSrcAcctdAmountDr | — |
| ACTIVITY_BUCKET | CashDistributionActivityBucket | ✅ |
| ACTIVITY_BUCKET | CshDistRefLineActivityBucket | — |
| ACTIVITY_BUCKET | CshDistRevSrcActivityBucket | — |
| AMOUNT_CR | CashDistributionAmountCr | ✅ |
| AMOUNT_CR | CshDistRefLineAmountCr | — |
| AMOUNT_CR | CshDistRevSrcAmountCr | — |
| AMOUNT_DR | CashDistributionAmountDr | ✅ |
| AMOUNT_DR | CshDistRefLineAmountDr | — |
| AMOUNT_DR | CshDistRevSrcAmountDr | — |
| CODE_COMBINATION_ID | CashDistributionCodeCombinationId | ✅ |
| CREATED_BY | CashDistributionCreatedBy | — |
| CREATION_DATE | CashDistributionCreationDate | — |
| CURRENCY_CODE | CashDistributionCurrencyCode | — |
| CURRENCY_CODE | CshDistRefLineCurrencyCode | — |
| CURRENCY_CODE | CshDistRevSrcCurrencyCode | — |
| CURRENCY_CONVERSION_DATE | CashDistributionCurrencyConversionDate | ✅ |
| CURRENCY_CONVERSION_DATE | CshDistRefLineCurrencyConversionDate | — |
| CURRENCY_CONVERSION_DATE | CshDistRevSrcCurrencyConversionDate | — |
| CURRENCY_CONVERSION_RATE | CashDistributionCurrencyConversionRate | ✅ |
| CURRENCY_CONVERSION_RATE | CshDistRefLineCurrencyConversionRate | — |
| CURRENCY_CONVERSION_RATE | CshDistRevSrcCurrencyConversionRate | — |
| CURRENCY_CONVERSION_TYPE | CashDistributionCurrencyConversionType | ✅ |
| CURRENCY_CONVERSION_TYPE | CshDistRefLineCurrencyConversionType | — |
| CURRENCY_CONVERSION_TYPE | CshDistRevSrcCurrencyConversionType | — |
| FROM_ACCTD_AMOUNT_CR | CashDistributionFromAcctdAmountCr | ✅ |
| FROM_ACCTD_AMOUNT_CR | CshDistRefLineFromAcctdAmountCr | — |
| FROM_ACCTD_AMOUNT_CR | CshDistRevSrcFromAcctdAmountCr | — |
| FROM_ACCTD_AMOUNT_DR | CashDistributionFromAcctdAmountDr | ✅ |
| FROM_ACCTD_AMOUNT_DR | CshDistRefLineFromAcctdAmountDr | — |
| FROM_ACCTD_AMOUNT_DR | CshDistRevSrcFromAcctdAmountDr | — |
| FROM_AMOUNT_CR | CashDistributionFromAmountCr | ✅ |
| FROM_AMOUNT_CR | CshDistRefLineFromAmountCr | — |
| FROM_AMOUNT_CR | CshDistRevSrcFromAmountCr | — |
| FROM_AMOUNT_DR | CashDistributionFromAmountDr | ✅ |
| FROM_AMOUNT_DR | CshDistRefLineFromAmountDr | — |
| FROM_AMOUNT_DR | CshDistRevSrcFromAmountDr | — |
| LAST_UPDATE_DATE | CashDistributionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CashDistributionLastUpdateLogin | — |
| LAST_UPDATED_BY | CashDistributionLastUpdatedBy | — |
| LINE_ID | CshDistRefLineLineId | — |
| LINE_ID | CshDistRevSrcLineId | — |
| LINE_ID | LineId | ✅ |
| LOCATION_SEGMENT_ID | CashDistributionLocationSegmentId | — |
| OBJECT_VERSION_NUMBER | CashDistributionObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber4 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber5 | — |
| ORG_ID | CashDistributionOrgId | — |
| REF_ACCOUNT_CLASS | CashDistributionRefAccountClass | ✅ |
| REF_ACCOUNT_CLASS | CshDistRefLineRefAccountClass | — |
| REF_ACCOUNT_CLASS | CshDistRevSrcRefAccountClass | — |
| REF_CUST_TRX_LINE_GL_DIST_ID | CashDistributionRefCustTrxLineGlDistId | — |
| REF_CUSTOMER_TRX_LINE_ID | CashDistributionRefCustomerTrxLineId | — |
| REF_DIST_CCID | CashDistributionRefDistCcid | — |
| REF_LINE_ID | CashDistributionRefLineId | — |
| REF_MF_DIST_FLAG | CashDistributionRefMfDistFlag | — |
| REF_MF_DIST_FLAG | CshDistRefLineRefMfDistFlag | — |
| REF_MF_DIST_FLAG | CshDistRevSrcRefMfDistFlag | — |
| REVERSAL_FLAG | CashDistributionReversalFlag | — |
| REVERSAL_FLAG | CshDistRefLineReversalFlag | — |
| REVERSAL_FLAG | CshDistRevSrcReversalFlag | — |
| REVERSED_SOURCE_ID | CashDistributionReversedSourceId | — |
| SOURCE_ID | CashDistributionSourceId | ✅ |
| SOURCE_ID | CshDistRefLineSourceId | — |
| SOURCE_ID | CshDistRevSrcSourceId | — |
| SOURCE_ID_SECONDARY | CashDistributionSourceIdSecondary | — |
| SOURCE_ID_SECONDARY | CshDistRefLineSourceIdSecondary | — |
| SOURCE_ID_SECONDARY | CshDistRevSrcSourceIdSecondary | — |
| SOURCE_TABLE | CashDistributionSourceTable | ✅ |
| SOURCE_TABLE | CshDistRefLineSourceTable | — |
| SOURCE_TABLE | CshDistRevSrcSourceTable | — |
| SOURCE_TABLE_SECONDARY | CashDistributionSourceTableSecondary | — |
| SOURCE_TABLE_SECONDARY | CshDistRefLineSourceTableSecondary | — |
| SOURCE_TABLE_SECONDARY | CshDistRevSrcSourceTableSecondary | — |
| SOURCE_TYPE | CashDistributionSourceType | ✅ |
| SOURCE_TYPE | CshDistRefLineSourceType | — |
| SOURCE_TYPE | CshDistRevSrcSourceType | — |
| SOURCE_TYPE_SECONDARY | CashDistributionSourceTypeSecondary | — |
| SOURCE_TYPE_SECONDARY | CshDistRefLineSourceTypeSecondary | — |
| SOURCE_TYPE_SECONDARY | CshDistRevSrcSourceTypeSecondary | — |
| TAX_CODE_ID | CashDistributionTaxCodeId | — |
| TAX_GROUP_CODE_ID | CashDistributionTaxGroupCodeId | — |
| TAX_ID | CashDistributionTaxId | — |
| TAX_LINK_ID | CashDistributionTaxLinkId | — |
| TAXABLE_ACCOUNTED_CR | CashDistributionTaxableAccountedCr | ✅ |
| TAXABLE_ACCOUNTED_CR | CshDistRefLineTaxableAccountedCr | — |
| TAXABLE_ACCOUNTED_CR | CshDistRevSrcTaxableAccountedCr | — |
| TAXABLE_ACCOUNTED_DR | CashDistributionTaxableAccountedDr | ✅ |
| TAXABLE_ACCOUNTED_DR | CshDistRefLineTaxableAccountedDr | — |
| TAXABLE_ACCOUNTED_DR | CshDistRevSrcTaxableAccountedDr | — |
| TAXABLE_ENTERED_CR | CashDistributionTaxableEnteredCr | ✅ |
| TAXABLE_ENTERED_CR | CshDistRefLineTaxableEnteredCr | — |
| TAXABLE_ENTERED_CR | CshDistRevSrcTaxableEnteredCr | — |
| TAXABLE_ENTERED_DR | CashDistributionTaxableEnteredDr | ✅ |
| TAXABLE_ENTERED_DR | CshDistRefLineTaxableEnteredDr | — |
| TAXABLE_ENTERED_DR | CshDistRevSrcTaxableEnteredDr | — |
| THIRD_PARTY_ID | CashDistributionThirdPartyId | — |
| THIRD_PARTY_SUB_ID | CashDistributionThirdPartySubId | — |

### [[completedtrxrevadjdistributionpvo|CompletedTrxRevAdjDistributionPVO]] (AR · BICC: 8/101)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_CR | CashDistributionAcctdAmountCr | ✅ |
| ACCTD_AMOUNT_CR | CshDistRefLineAcctdAmountCr | — |
| ACCTD_AMOUNT_CR | CshDistRevSrcAcctdAmountCr | — |
| ACCTD_AMOUNT_DR | CashDistributionAcctdAmountDr | ✅ |
| ACCTD_AMOUNT_DR | CshDistRefLineAcctdAmountDr | — |
| ACCTD_AMOUNT_DR | CshDistRevSrcAcctdAmountDr | — |
| ACTIVITY_BUCKET | CashDistributionActivityBucket | — |
| ACTIVITY_BUCKET | CshDistRefLineActivityBucket | — |
| ACTIVITY_BUCKET | CshDistRevSrcActivityBucket | — |
| AMOUNT_CR | CashDistributionAmountCr | ✅ |
| AMOUNT_CR | CshDistRefLineAmountCr | — |
| AMOUNT_CR | CshDistRevSrcAmountCr | — |
| AMOUNT_DR | CashDistributionAmountDr | ✅ |
| AMOUNT_DR | CshDistRefLineAmountDr | — |
| AMOUNT_DR | CshDistRevSrcAmountDr | — |
| CODE_COMBINATION_ID | CashDistributionCodeCombinationId | — |
| CREATED_BY | CashDistributionCreatedBy | — |
| CREATION_DATE | CashDistributionCreationDate | — |
| CURRENCY_CODE | CashDistributionCurrencyCode | — |
| CURRENCY_CODE | CshDistRefLineCurrencyCode | — |
| CURRENCY_CODE | CshDistRevSrcCurrencyCode | — |
| CURRENCY_CONVERSION_DATE | CashDistributionCurrencyConversionDate | — |
| CURRENCY_CONVERSION_DATE | CshDistRefLineCurrencyConversionDate | — |
| CURRENCY_CONVERSION_DATE | CshDistRevSrcCurrencyConversionDate | — |
| CURRENCY_CONVERSION_RATE | CashDistributionCurrencyConversionRate | — |
| CURRENCY_CONVERSION_RATE | CshDistRefLineCurrencyConversionRate | — |
| CURRENCY_CONVERSION_RATE | CshDistRevSrcCurrencyConversionRate | — |
| CURRENCY_CONVERSION_TYPE | CashDistributionCurrencyConversionType | — |
| CURRENCY_CONVERSION_TYPE | CshDistRefLineCurrencyConversionType | — |
| CURRENCY_CONVERSION_TYPE | CshDistRevSrcCurrencyConversionType | — |
| FROM_ACCTD_AMOUNT_CR | CashDistributionFromAcctdAmountCr | — |
| FROM_ACCTD_AMOUNT_CR | CshDistRefLineFromAcctdAmountCr | — |
| FROM_ACCTD_AMOUNT_CR | CshDistRevSrcFromAcctdAmountCr | — |
| FROM_ACCTD_AMOUNT_DR | CashDistributionFromAcctdAmountDr | — |
| FROM_ACCTD_AMOUNT_DR | CshDistRefLineFromAcctdAmountDr | — |
| FROM_ACCTD_AMOUNT_DR | CshDistRevSrcFromAcctdAmountDr | — |
| FROM_AMOUNT_CR | CashDistributionFromAmountCr | — |
| FROM_AMOUNT_CR | CshDistRefLineFromAmountCr | — |
| FROM_AMOUNT_CR | CshDistRevSrcFromAmountCr | — |
| FROM_AMOUNT_DR | CashDistributionFromAmountDr | — |
| FROM_AMOUNT_DR | CshDistRefLineFromAmountDr | — |
| FROM_AMOUNT_DR | CshDistRevSrcFromAmountDr | — |
| LAST_UPDATE_DATE | CashDistributionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CashDistributionLastUpdateLogin | — |
| LAST_UPDATED_BY | CashDistributionLastUpdatedBy | — |
| LINE_ID | CshDistRefLineLineId | — |
| LINE_ID | CshDistRevSrcLineId | — |
| LINE_ID | LineId | ✅ |
| LOCATION_SEGMENT_ID | CashDistributionLocationSegmentId | — |
| OBJECT_VERSION_NUMBER | CashDistributionObjectVersionNumber | — |
| ORG_ID | CashDistributionOrgId | — |
| REF_ACCOUNT_CLASS | CashDistributionRefAccountClass | — |
| REF_ACCOUNT_CLASS | CshDistRefLineRefAccountClass | — |
| REF_ACCOUNT_CLASS | CshDistRevSrcRefAccountClass | — |
| REF_CUST_TRX_LINE_GL_DIST_ID | CashDistributionRefCustTrxLineGlDistId | — |
| REF_CUSTOMER_TRX_LINE_ID | CashDistributionRefCustomerTrxLineId | — |
| REF_DIST_CCID | CashDistributionRefDistCcid | — |
| REF_LINE_ID | CashDistributionRefLineId | — |
| REF_MF_DIST_FLAG | CashDistributionRefMfDistFlag | — |
| REF_MF_DIST_FLAG | CshDistRefLineRefMfDistFlag | — |
| REF_MF_DIST_FLAG | CshDistRevSrcRefMfDistFlag | — |
| REVERSAL_FLAG | CashDistributionReversalFlag | — |
| REVERSAL_FLAG | CshDistRefLineReversalFlag | — |
| REVERSAL_FLAG | CshDistRevSrcReversalFlag | — |
| REVERSED_SOURCE_ID | CashDistributionReversedSourceId | — |
| SOURCE_ID | CashDistributionSourceId | — |
| SOURCE_ID | CshDistRefLineSourceId | — |
| SOURCE_ID | CshDistRevSrcSourceId | — |
| SOURCE_ID_SECONDARY | CashDistributionSourceIdSecondary | — |
| SOURCE_ID_SECONDARY | CshDistRefLineSourceIdSecondary | — |
| SOURCE_ID_SECONDARY | CshDistRevSrcSourceIdSecondary | — |
| SOURCE_TABLE | CashDistributionSourceTable | ✅ |
| SOURCE_TABLE | CshDistRefLineSourceTable | — |
| SOURCE_TABLE | CshDistRevSrcSourceTable | — |
| SOURCE_TABLE_SECONDARY | CashDistributionSourceTableSecondary | — |
| SOURCE_TABLE_SECONDARY | CshDistRefLineSourceTableSecondary | — |
| SOURCE_TABLE_SECONDARY | CshDistRevSrcSourceTableSecondary | — |
| SOURCE_TYPE | CashDistributionSourceType | ✅ |
| SOURCE_TYPE | CshDistRefLineSourceType | — |
| SOURCE_TYPE | CshDistRevSrcSourceType | — |
| SOURCE_TYPE_SECONDARY | CashDistributionSourceTypeSecondary | — |
| SOURCE_TYPE_SECONDARY | CshDistRefLineSourceTypeSecondary | — |
| SOURCE_TYPE_SECONDARY | CshDistRevSrcSourceTypeSecondary | — |
| TAX_CODE_ID | CashDistributionTaxCodeId | — |
| TAX_GROUP_CODE_ID | CashDistributionTaxGroupCodeId | — |
| TAX_ID | CashDistributionTaxId | — |
| TAX_LINK_ID | CashDistributionTaxLinkId | — |
| TAXABLE_ACCOUNTED_CR | CashDistributionTaxableAccountedCr | — |
| TAXABLE_ACCOUNTED_CR | CshDistRefLineTaxableAccountedCr | — |
| TAXABLE_ACCOUNTED_CR | CshDistRevSrcTaxableAccountedCr | — |
| TAXABLE_ACCOUNTED_DR | CashDistributionTaxableAccountedDr | — |
| TAXABLE_ACCOUNTED_DR | CshDistRefLineTaxableAccountedDr | — |
| TAXABLE_ACCOUNTED_DR | CshDistRevSrcTaxableAccountedDr | — |
| TAXABLE_ENTERED_CR | CashDistributionTaxableEnteredCr | — |
| TAXABLE_ENTERED_CR | CshDistRefLineTaxableEnteredCr | — |
| TAXABLE_ENTERED_CR | CshDistRevSrcTaxableEnteredCr | — |
| TAXABLE_ENTERED_DR | CashDistributionTaxableEnteredDr | — |
| TAXABLE_ENTERED_DR | CshDistRefLineTaxableEnteredDr | — |
| TAXABLE_ENTERED_DR | CshDistRevSrcTaxableEnteredDr | — |
| THIRD_PARTY_ID | CashDistributionThirdPartyId | — |
| THIRD_PARTY_SUB_ID | CashDistributionThirdPartySubId | — |

### [[creditmemoapplicationdistributionpvo|CreditMemoApplicationDistributionPVO]] (AR · BICC: 24/103)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_CR | CashDistributionAcctdAmountCr | ✅ |
| ACCTD_AMOUNT_CR | CshDistRefLineAcctdAmountCr | — |
| ACCTD_AMOUNT_CR | CshDistRevSrcAcctdAmountCr | — |
| ACCTD_AMOUNT_DR | CashDistributionAcctdAmountDr | ✅ |
| ACCTD_AMOUNT_DR | CshDistRefLineAcctdAmountDr | — |
| ACCTD_AMOUNT_DR | CshDistRevSrcAcctdAmountDr | — |
| ACTIVITY_BUCKET | CashDistributionActivityBucket | ✅ |
| ACTIVITY_BUCKET | CshDistRefLineActivityBucket | — |
| ACTIVITY_BUCKET | CshDistRevSrcActivityBucket | — |
| AMOUNT_CR | CashDistributionAmountCr | ✅ |
| AMOUNT_CR | CshDistRefLineAmountCr | — |
| AMOUNT_CR | CshDistRevSrcAmountCr | — |
| AMOUNT_DR | CashDistributionAmountDr | ✅ |
| AMOUNT_DR | CshDistRefLineAmountDr | — |
| AMOUNT_DR | CshDistRevSrcAmountDr | — |
| CODE_COMBINATION_ID | CashDistributionCodeCombinationId | ✅ |
| CREATED_BY | CashDistributionCreatedBy | — |
| CREATION_DATE | CashDistributionCreationDate | — |
| CURRENCY_CODE | CashDistributionCurrencyCode | — |
| CURRENCY_CODE | CshDistRefLineCurrencyCode | — |
| CURRENCY_CODE | CshDistRevSrcCurrencyCode | — |
| CURRENCY_CONVERSION_DATE | CashDistributionCurrencyConversionDate | ✅ |
| CURRENCY_CONVERSION_DATE | CshDistRefLineCurrencyConversionDate | — |
| CURRENCY_CONVERSION_DATE | CshDistRevSrcCurrencyConversionDate | — |
| CURRENCY_CONVERSION_RATE | CashDistributionCurrencyConversionRate | ✅ |
| CURRENCY_CONVERSION_RATE | CshDistRefLineCurrencyConversionRate | — |
| CURRENCY_CONVERSION_RATE | CshDistRevSrcCurrencyConversionRate | — |
| CURRENCY_CONVERSION_TYPE | CashDistributionCurrencyConversionType | ✅ |
| CURRENCY_CONVERSION_TYPE | CshDistRefLineCurrencyConversionType | — |
| CURRENCY_CONVERSION_TYPE | CshDistRevSrcCurrencyConversionType | — |
| FROM_ACCTD_AMOUNT_CR | CashDistributionFromAcctdAmountCr | ✅ |
| FROM_ACCTD_AMOUNT_CR | CshDistRefLineFromAcctdAmountCr | — |
| FROM_ACCTD_AMOUNT_CR | CshDistRevSrcFromAcctdAmountCr | — |
| FROM_ACCTD_AMOUNT_DR | CashDistributionFromAcctdAmountDr | ✅ |
| FROM_ACCTD_AMOUNT_DR | CshDistRefLineFromAcctdAmountDr | — |
| FROM_ACCTD_AMOUNT_DR | CshDistRevSrcFromAcctdAmountDr | — |
| FROM_AMOUNT_CR | CashDistributionFromAmountCr | ✅ |
| FROM_AMOUNT_CR | CshDistRefLineFromAmountCr | — |
| FROM_AMOUNT_CR | CshDistRevSrcFromAmountCr | — |
| FROM_AMOUNT_DR | CashDistributionFromAmountDr | ✅ |
| FROM_AMOUNT_DR | CshDistRefLineFromAmountDr | — |
| FROM_AMOUNT_DR | CshDistRevSrcFromAmountDr | — |
| LAST_UPDATE_DATE | CashDistributionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CashDistributionLastUpdateLogin | — |
| LAST_UPDATED_BY | CashDistributionLastUpdatedBy | — |
| LINE_ID | CshDistRefLineLineId | — |
| LINE_ID | CshDistRevSrcLineId | — |
| LINE_ID | LineId | ✅ |
| LOCATION_SEGMENT_ID | CashDistributionLocationSegmentId | — |
| OBJECT_VERSION_NUMBER | CashDistributionObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber2 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber3 | — |
| ORG_ID | CashDistributionOrgId | — |
| REF_ACCOUNT_CLASS | CashDistributionRefAccountClass | ✅ |
| REF_ACCOUNT_CLASS | CshDistRefLineRefAccountClass | — |
| REF_ACCOUNT_CLASS | CshDistRevSrcRefAccountClass | — |
| REF_CUST_TRX_LINE_GL_DIST_ID | CashDistributionRefCustTrxLineGlDistId | ✅ |
| REF_CUSTOMER_TRX_LINE_ID | CashDistributionRefCustomerTrxLineId | — |
| REF_DIST_CCID | CashDistributionRefDistCcid | — |
| REF_LINE_ID | CashDistributionRefLineId | — |
| REF_MF_DIST_FLAG | CashDistributionRefMfDistFlag | — |
| REF_MF_DIST_FLAG | CshDistRefLineRefMfDistFlag | — |
| REF_MF_DIST_FLAG | CshDistRevSrcRefMfDistFlag | — |
| REVERSAL_FLAG | CashDistributionReversalFlag | — |
| REVERSAL_FLAG | CshDistRefLineReversalFlag | — |
| REVERSAL_FLAG | CshDistRevSrcReversalFlag | — |
| REVERSED_SOURCE_ID | CashDistributionReversedSourceId | — |
| SOURCE_ID | CashDistributionSourceId | ✅ |
| SOURCE_ID | CshDistRefLineSourceId | — |
| SOURCE_ID | CshDistRevSrcSourceId | — |
| SOURCE_ID_SECONDARY | CashDistributionSourceIdSecondary | — |
| SOURCE_ID_SECONDARY | CshDistRefLineSourceIdSecondary | — |
| SOURCE_ID_SECONDARY | CshDistRevSrcSourceIdSecondary | — |
| SOURCE_TABLE | CashDistributionSourceTable | ✅ |
| SOURCE_TABLE | CshDistRefLineSourceTable | — |
| SOURCE_TABLE | CshDistRevSrcSourceTable | — |
| SOURCE_TABLE_SECONDARY | CashDistributionSourceTableSecondary | — |
| SOURCE_TABLE_SECONDARY | CshDistRefLineSourceTableSecondary | — |
| SOURCE_TABLE_SECONDARY | CshDistRevSrcSourceTableSecondary | — |
| SOURCE_TYPE | CashDistributionSourceType | ✅ |
| SOURCE_TYPE | CshDistRefLineSourceType | — |
| SOURCE_TYPE | CshDistRevSrcSourceType | — |
| SOURCE_TYPE_SECONDARY | CashDistributionSourceTypeSecondary | — |
| SOURCE_TYPE_SECONDARY | CshDistRefLineSourceTypeSecondary | — |
| SOURCE_TYPE_SECONDARY | CshDistRevSrcSourceTypeSecondary | — |
| TAX_CODE_ID | CashDistributionTaxCodeId | — |
| TAX_GROUP_CODE_ID | CashDistributionTaxGroupCodeId | — |
| TAX_ID | CashDistributionTaxId | — |
| TAX_LINK_ID | CashDistributionTaxLinkId | — |
| TAXABLE_ACCOUNTED_CR | CashDistributionTaxableAccountedCr | ✅ |
| TAXABLE_ACCOUNTED_CR | CshDistRefLineTaxableAccountedCr | — |
| TAXABLE_ACCOUNTED_CR | CshDistRevSrcTaxableAccountedCr | — |
| TAXABLE_ACCOUNTED_DR | CashDistributionTaxableAccountedDr | ✅ |
| TAXABLE_ACCOUNTED_DR | CshDistRefLineTaxableAccountedDr | — |
| TAXABLE_ACCOUNTED_DR | CshDistRevSrcTaxableAccountedDr | — |
| TAXABLE_ENTERED_CR | CashDistributionTaxableEnteredCr | ✅ |
| TAXABLE_ENTERED_CR | CshDistRefLineTaxableEnteredCr | — |
| TAXABLE_ENTERED_CR | CshDistRevSrcTaxableEnteredCr | — |
| TAXABLE_ENTERED_DR | CashDistributionTaxableEnteredDr | ✅ |
| TAXABLE_ENTERED_DR | CshDistRefLineTaxableEnteredDr | — |
| TAXABLE_ENTERED_DR | CshDistRevSrcTaxableEnteredDr | — |
| THIRD_PARTY_ID | CashDistributionThirdPartyId | — |
| THIRD_PARTY_SUB_ID | CashDistributionThirdPartySubId | — |

### [[distributionextractpvo|DistributionExtractPVO]] (OTHER · BICC: 48/48)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_CR | ArDistributionAcctdAmountCr | ✅ |
| ACCTD_AMOUNT_DR | ArDistributionAcctdAmountDr | ✅ |
| ACTIVITY_BUCKET | ArDistributionActivityBucket | ✅ |
| AMOUNT_CR | ArDistributionAmountCr | ✅ |
| AMOUNT_DR | ArDistributionAmountDr | ✅ |
| CODE_COMBINATION_ID | ArDistributionCodeCombinationId | ✅ |
| CREATED_BY | ArDistributionCreatedBy | ✅ |
| CREATION_DATE | ArDistributionCreationDate | ✅ |
| CURRENCY_CODE | ArDistributionCurrencyCode | ✅ |
| CURRENCY_CONVERSION_DATE | ArDistributionCurrencyConversionDate | ✅ |
| CURRENCY_CONVERSION_RATE | ArDistributionCurrencyConversionRate | ✅ |
| CURRENCY_CONVERSION_TYPE | ArDistributionCurrencyConversionType | ✅ |
| FROM_ACCTD_AMOUNT_CR | ArDistributionFromAcctdAmountCr | ✅ |
| FROM_ACCTD_AMOUNT_DR | ArDistributionFromAcctdAmountDr | ✅ |
| FROM_AMOUNT_CR | ArDistributionFromAmountCr | ✅ |
| FROM_AMOUNT_DR | ArDistributionFromAmountDr | ✅ |
| LAST_UPDATE_DATE | ArDistributionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ArDistributionLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ArDistributionLastUpdatedBy | ✅ |
| LINE_ID | ArDistributionLineId | ✅ |
| LOCATION_SEGMENT_ID | ArDistributionLocationSegmentId | ✅ |
| OBJECT_VERSION_NUMBER | ArDistributionObjectVersionNumber | ✅ |
| ORG_ID | ArDistributionOrgId | ✅ |
| REF_ACCOUNT_CLASS | ArDistributionRefAccountClass | ✅ |
| REF_CUST_TRX_LINE_GL_DIST_ID | ArDistributionRefCustTrxLineGlDistId | ✅ |
| REF_CUSTOMER_TRX_LINE_ID | ArDistributionRefCustomerTrxLineId | ✅ |
| REF_DIST_CCID | ArDistributionRefDistCcid | ✅ |
| REF_LINE_ID | ArDistributionRefLineId | ✅ |
| REF_MF_DIST_FLAG | ArDistributionRefMfDistFlag | ✅ |
| REF_PREV_CUST_TRX_LINE_ID | ArDistributionRefPrevCustTrxLineId | ✅ |
| REVERSAL_FLAG | ArDistributionReversalFlag | ✅ |
| REVERSED_SOURCE_ID | ArDistributionReversedSourceId | ✅ |
| SOURCE_ID | ArDistributionSourceId | ✅ |
| SOURCE_ID_SECONDARY | ArDistributionSourceIdSecondary | ✅ |
| SOURCE_TABLE | ArDistributionSourceTable | ✅ |
| SOURCE_TABLE_SECONDARY | ArDistributionSourceTableSecondary | ✅ |
| SOURCE_TYPE | ArDistributionSourceType | ✅ |
| SOURCE_TYPE_SECONDARY | ArDistributionSourceTypeSecondary | ✅ |
| TAX_CODE_ID | ArDistributionTaxCodeId | ✅ |
| TAX_GROUP_CODE_ID | ArDistributionTaxGroupCodeId | ✅ |
| TAX_ID | ArDistributionTaxId | ✅ |
| TAX_LINK_ID | ArDistributionTaxLinkId | ✅ |
| TAXABLE_ACCOUNTED_CR | ArDistributionTaxableAccountedCr | ✅ |
| TAXABLE_ACCOUNTED_DR | ArDistributionTaxableAccountedDr | ✅ |
| TAXABLE_ENTERED_CR | ArDistributionTaxableEnteredCr | ✅ |
| TAXABLE_ENTERED_DR | ArDistributionTaxableEnteredDr | ✅ |
| THIRD_PARTY_ID | ArDistributionThirdPartyId | ✅ |
| THIRD_PARTY_SUB_ID | ArDistributionThirdPartySubId | ✅ |

### [[miscreceiptdistributionpvo|MiscReceiptDistributionPVO]] (AR · BICC: 24/141)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_CR | AdjustmentDistributionAcctdAmountCr | — |
| ACCTD_AMOUNT_CR | CashDistributionAcctdAmountCr | ✅ |
| ACCTD_AMOUNT_CR | ReverseDistributionAcctdAmountCr | — |
| ACCTD_AMOUNT_DR | AdjustmentDistributionAcctdAmountDr | — |
| ACCTD_AMOUNT_DR | CashDistributionAcctdAmountDr | ✅ |
| ACCTD_AMOUNT_DR | ReverseDistributionAcctdAmountDr | — |
| ACTIVITY_BUCKET | AdjustmentDistributionActivityBucket | — |
| ACTIVITY_BUCKET | CashDistributionActivityBucket | ✅ |
| ACTIVITY_BUCKET | ReverseDistributionActivityBucket | — |
| AMOUNT_CR | AdjustmentDistributionAmountCr | — |
| AMOUNT_CR | CashDistributionAmountCr | ✅ |
| AMOUNT_CR | ReverseDistributionAmountCr | — |
| AMOUNT_DR | AdjustmentDistributionAmountDr | — |
| AMOUNT_DR | CashDistributionAmountDr | ✅ |
| AMOUNT_DR | ReverseDistributionAmountDr | — |
| CODE_COMBINATION_ID | AdjustmentDistributionCodeCombinationId | — |
| CODE_COMBINATION_ID | CashDistributionCodeCombinationId | — |
| CODE_COMBINATION_ID | ReverseDistributionCodeCombinationId | — |
| CREATED_BY | AdjustmentDistributionCreatedBy | — |
| CREATED_BY | CashDistributionCreatedBy | — |
| CREATED_BY | ReverseDistributionCreatedBy | — |
| CREATION_DATE | AdjustmentDistributionCreationDate | — |
| CREATION_DATE | CashDistributionCreationDate | — |
| CREATION_DATE | ReverseDistributionCreationDate | — |
| CURRENCY_CODE | AdjustmentDistributionCurrencyCode | — |
| CURRENCY_CODE | CashDistributionCurrencyCode | — |
| CURRENCY_CODE | ReverseDistributionCurrencyCode | — |
| CURRENCY_CONVERSION_DATE | AdjustmentDistributionCurrencyConversionDate | — |
| CURRENCY_CONVERSION_DATE | CashDistributionCurrencyConversionDate | ✅ |
| CURRENCY_CONVERSION_DATE | ReverseDistributionCurrencyConversionDate | — |
| CURRENCY_CONVERSION_RATE | AdjustmentDistributionCurrencyConversionRate | — |
| CURRENCY_CONVERSION_RATE | CashDistributionCurrencyConversionRate | ✅ |
| CURRENCY_CONVERSION_RATE | ReverseDistributionCurrencyConversionRate | — |
| CURRENCY_CONVERSION_TYPE | AdjustmentDistributionCurrencyConversionType | — |
| CURRENCY_CONVERSION_TYPE | CashDistributionCurrencyConversionType | ✅ |
| CURRENCY_CONVERSION_TYPE | ReverseDistributionCurrencyConversionType | — |
| FROM_ACCTD_AMOUNT_CR | AdjustmentDistributionFromAcctdAmountCr | — |
| FROM_ACCTD_AMOUNT_CR | CashDistributionFromAcctdAmountCr | ✅ |
| FROM_ACCTD_AMOUNT_CR | ReverseDistributionFromAcctdAmountCr | — |
| FROM_ACCTD_AMOUNT_DR | AdjustmentDistributionFromAcctdAmountDr | — |
| FROM_ACCTD_AMOUNT_DR | CashDistributionFromAcctdAmountDr | ✅ |
| FROM_ACCTD_AMOUNT_DR | ReverseDistributionFromAcctdAmountDr | — |
| FROM_AMOUNT_CR | AdjustmentDistributionFromAmountCr | — |
| FROM_AMOUNT_CR | CashDistributionFromAmountCr | ✅ |
| FROM_AMOUNT_CR | ReverseDistributionFromAmountCr | — |
| FROM_AMOUNT_DR | AdjustmentDistributionFromAmountDr | — |
| FROM_AMOUNT_DR | CashDistributionFromAmountDr | ✅ |
| FROM_AMOUNT_DR | ReverseDistributionFromAmountDr | — |
| LAST_UPDATE_DATE | AdjustmentDistributionLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | CashDistributionLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ReverseDistributionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AdjustmentDistributionLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | CashDistributionLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ReverseDistributionLastUpdateLogin | — |
| LAST_UPDATED_BY | AdjustmentDistributionLastUpdatedBy | — |
| LAST_UPDATED_BY | CashDistributionLastUpdatedBy | — |
| LAST_UPDATED_BY | ReverseDistributionLastUpdatedBy | — |
| LINE_ID | AdjustmentDistributionLineId | — |
| LINE_ID | LineId | ✅ |
| LINE_ID | ReverseDistributionLineId | — |
| LOCATION_SEGMENT_ID | AdjustmentDistributionLocationSegmentId | — |
| LOCATION_SEGMENT_ID | CashDistributionLocationSegmentId | — |
| LOCATION_SEGMENT_ID | ReverseDistributionLocationSegmentId | — |
| OBJECT_VERSION_NUMBER | AdjustmentDistributionObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | CashDistributionObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ReverseDistributionObjectVersionNumber | — |
| ORG_ID | AdjustmentDistributionOrgId | — |
| ORG_ID | CashDistributionOrgId | — |
| ORG_ID | ReverseDistributionOrgId | — |
| REF_ACCOUNT_CLASS | AdjustmentDistributionRefAccountClass | — |
| REF_ACCOUNT_CLASS | CashDistributionRefAccountClass | ✅ |
| REF_ACCOUNT_CLASS | ReverseDistributionRefAccountClass | — |
| REF_CUST_TRX_LINE_GL_DIST_ID | AdjustmentDistributionRefCustTrxLineGlDistId | — |
| REF_CUST_TRX_LINE_GL_DIST_ID | CashDistributionRefCustTrxLineGlDistId | — |
| REF_CUST_TRX_LINE_GL_DIST_ID | ReverseDistributionRefCustTrxLineGlDistId | — |
| REF_CUSTOMER_TRX_LINE_ID | AdjustmentDistributionRefCustomerTrxLineId | — |
| REF_CUSTOMER_TRX_LINE_ID | CashDistributionRefCustomerTrxLineId | — |
| REF_CUSTOMER_TRX_LINE_ID | ReverseDistributionRefCustomerTrxLineId | — |
| REF_DIST_CCID | AdjustmentDistributionRefDistCcid | — |
| REF_DIST_CCID | CashDistributionRefDistCcid | — |
| REF_DIST_CCID | ReverseDistributionRefDistCcid | — |
| REF_LINE_ID | AdjustmentDistributionRefLineId | — |
| REF_LINE_ID | CashDistributionRefLineId | — |
| REF_LINE_ID | ReverseDistributionRefLineId | — |
| REF_MF_DIST_FLAG | AdjustmentDistributionRefMfDistFlag | — |
| REF_MF_DIST_FLAG | CashDistributionRefMfDistFlag | — |
| REF_MF_DIST_FLAG | ReverseDistributionRefMfDistFlag | — |
| REVERSAL_FLAG | AdjustmentDistributionReversalFlag | — |
| REVERSAL_FLAG | CashDistributionReversalFlag | — |
| REVERSAL_FLAG | ReverseDistributionReversalFlag | — |
| REVERSED_SOURCE_ID | AdjustmentDistributionReversedSourceId | — |
| REVERSED_SOURCE_ID | CashDistributionReversedSourceId | — |
| REVERSED_SOURCE_ID | ReverseDistributionReversedSourceId | — |
| SOURCE_ID | AdjustmentDistributionSourceId | — |
| SOURCE_ID | CashDistributionSourceId | ✅ |
| SOURCE_ID | ReverseDistributionSourceId | — |
| SOURCE_ID_SECONDARY | AdjustmentDistributionSourceIdSecondary | — |
| SOURCE_ID_SECONDARY | CashDistributionSourceIdSecondary | — |
| SOURCE_ID_SECONDARY | ReverseDistributionSourceIdSecondary | — |
| SOURCE_TABLE | AdjustmentDistributionSourceTable | — |
| SOURCE_TABLE | CashDistributionSourceTable | ✅ |
| SOURCE_TABLE | ReverseDistributionSourceTable | — |
| SOURCE_TABLE_SECONDARY | AdjustmentDistributionSourceTableSecondary | — |
| SOURCE_TABLE_SECONDARY | CashDistributionSourceTableSecondary | — |
| SOURCE_TABLE_SECONDARY | ReverseDistributionSourceTableSecondary | — |
| SOURCE_TYPE | AdjustmentDistributionSourceType | — |
| SOURCE_TYPE | CashDistributionSourceType | ✅ |
| SOURCE_TYPE | ReverseDistributionSourceType | — |
| SOURCE_TYPE_SECONDARY | AdjustmentDistributionSourceTypeSecondary | — |
| SOURCE_TYPE_SECONDARY | CashDistributionSourceTypeSecondary | — |
| SOURCE_TYPE_SECONDARY | ReverseDistributionSourceTypeSecondary | — |
| TAX_CODE_ID | AdjustmentDistributionTaxCodeId | — |
| TAX_CODE_ID | CashDistributionTaxCodeId | — |
| TAX_CODE_ID | ReverseDistributionTaxCodeId | — |
| TAX_GROUP_CODE_ID | AdjustmentDistributionTaxGroupCodeId | — |
| TAX_GROUP_CODE_ID | CashDistributionTaxGroupCodeId | — |
| TAX_GROUP_CODE_ID | ReverseDistributionTaxGroupCodeId | — |
| TAX_ID | AdjustmentDistributionTaxId | — |
| TAX_ID | CashDistributionTaxId | — |
| TAX_ID | ReverseDistributionTaxId | — |
| TAX_LINK_ID | AdjustmentDistributionTaxLinkId | — |
| TAX_LINK_ID | CashDistributionTaxLinkId | — |
| TAX_LINK_ID | ReverseDistributionTaxLinkId | — |
| TAXABLE_ACCOUNTED_CR | AdjustmentDistributionTaxableAccountedCr | — |
| TAXABLE_ACCOUNTED_CR | CashDistributionTaxableAccountedCr | ✅ |
| TAXABLE_ACCOUNTED_CR | ReverseDistributionTaxableAccountedCr | — |
| TAXABLE_ACCOUNTED_DR | AdjustmentDistributionTaxableAccountedDr | — |
| TAXABLE_ACCOUNTED_DR | CashDistributionTaxableAccountedDr | ✅ |
| TAXABLE_ACCOUNTED_DR | ReverseDistributionTaxableAccountedDr | — |
| TAXABLE_ENTERED_CR | AdjustmentDistributionTaxableEnteredCr | — |
| TAXABLE_ENTERED_CR | CashDistributionTaxableEnteredCr | ✅ |
| TAXABLE_ENTERED_CR | ReverseDistributionTaxableEnteredCr | — |
| TAXABLE_ENTERED_DR | AdjustmentDistributionTaxableEnteredDr | — |
| TAXABLE_ENTERED_DR | CashDistributionTaxableEnteredDr | ✅ |
| TAXABLE_ENTERED_DR | ReverseDistributionTaxableEnteredDr | — |
| THIRD_PARTY_ID | AdjustmentDistributionThirdPartyId | — |
| THIRD_PARTY_ID | CashDistributionThirdPartyId | — |
| THIRD_PARTY_ID | ReverseDistributionThirdPartyId | — |
| THIRD_PARTY_SUB_ID | AdjustmentDistributionThirdPartySubId | — |
| THIRD_PARTY_SUB_ID | CashDistributionThirdPartySubId | — |
| THIRD_PARTY_SUB_ID | ReverseDistributionThirdPartySubId | — |

### [[receiptapplicationdistributionpvo|ReceiptApplicationDistributionPVO]] (AR · BICC: 11/101)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_CR | CashDistributionAcctdAmountCr | ✅ |
| ACCTD_AMOUNT_CR | CshDistRefLineAcctdAmountCr | — |
| ACCTD_AMOUNT_CR | CshDistRevSrcAcctdAmountCr | — |
| ACCTD_AMOUNT_DR | CashDistributionAcctdAmountDr | ✅ |
| ACCTD_AMOUNT_DR | CshDistRefLineAcctdAmountDr | — |
| ACCTD_AMOUNT_DR | CshDistRevSrcAcctdAmountDr | — |
| ACTIVITY_BUCKET | CashDistributionActivityBucket | ✅ |
| ACTIVITY_BUCKET | CshDistRefLineActivityBucket | — |
| ACTIVITY_BUCKET | CshDistRevSrcActivityBucket | — |
| AMOUNT_CR | CashDistributionAmountCr | ✅ |
| AMOUNT_CR | CshDistRefLineAmountCr | — |
| AMOUNT_CR | CshDistRevSrcAmountCr | — |
| AMOUNT_DR | CashDistributionAmountDr | ✅ |
| AMOUNT_DR | CshDistRefLineAmountDr | — |
| AMOUNT_DR | CshDistRevSrcAmountDr | — |
| CODE_COMBINATION_ID | CashDistributionCodeCombinationId | ✅ |
| CREATED_BY | CashDistributionCreatedBy | — |
| CREATION_DATE | CashDistributionCreationDate | ✅ |
| CURRENCY_CODE | CashDistributionCurrencyCode | ✅ |
| CURRENCY_CODE | CshDistRefLineCurrencyCode | — |
| CURRENCY_CODE | CshDistRevSrcCurrencyCode | — |
| CURRENCY_CONVERSION_DATE | CashDistributionCurrencyConversionDate | — |
| CURRENCY_CONVERSION_DATE | CshDistRefLineCurrencyConversionDate | — |
| CURRENCY_CONVERSION_DATE | CshDistRevSrcCurrencyConversionDate | — |
| CURRENCY_CONVERSION_RATE | CashDistributionCurrencyConversionRate | — |
| CURRENCY_CONVERSION_RATE | CshDistRefLineCurrencyConversionRate | — |
| CURRENCY_CONVERSION_RATE | CshDistRevSrcCurrencyConversionRate | — |
| CURRENCY_CONVERSION_TYPE | CashDistributionCurrencyConversionType | — |
| CURRENCY_CONVERSION_TYPE | CshDistRefLineCurrencyConversionType | — |
| CURRENCY_CONVERSION_TYPE | CshDistRevSrcCurrencyConversionType | — |
| FROM_ACCTD_AMOUNT_CR | CashDistributionFromAcctdAmountCr | — |
| FROM_ACCTD_AMOUNT_CR | CshDistRefLineFromAcctdAmountCr | — |
| FROM_ACCTD_AMOUNT_CR | CshDistRevSrcFromAcctdAmountCr | — |
| FROM_ACCTD_AMOUNT_DR | CashDistributionFromAcctdAmountDr | — |
| FROM_ACCTD_AMOUNT_DR | CshDistRefLineFromAcctdAmountDr | — |
| FROM_ACCTD_AMOUNT_DR | CshDistRevSrcFromAcctdAmountDr | — |
| FROM_AMOUNT_CR | CashDistributionFromAmountCr | — |
| FROM_AMOUNT_CR | CshDistRefLineFromAmountCr | — |
| FROM_AMOUNT_CR | CshDistRevSrcFromAmountCr | — |
| FROM_AMOUNT_DR | CashDistributionFromAmountDr | — |
| FROM_AMOUNT_DR | CshDistRefLineFromAmountDr | — |
| FROM_AMOUNT_DR | CshDistRevSrcFromAmountDr | — |
| LAST_UPDATE_DATE | CashDistributionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CashDistributionLastUpdateLogin | — |
| LAST_UPDATED_BY | CashDistributionLastUpdatedBy | — |
| LINE_ID | CshDistRefLineLineId | — |
| LINE_ID | CshDistRevSrcLineId | — |
| LINE_ID | LineId | ✅ |
| LOCATION_SEGMENT_ID | CashDistributionLocationSegmentId | — |
| OBJECT_VERSION_NUMBER | CashDistributionObjectVersionNumber | — |
| ORG_ID | CashDistributionOrgId | — |
| REF_ACCOUNT_CLASS | CashDistributionRefAccountClass | — |
| REF_ACCOUNT_CLASS | CshDistRefLineRefAccountClass | — |
| REF_ACCOUNT_CLASS | CshDistRevSrcRefAccountClass | — |
| REF_CUST_TRX_LINE_GL_DIST_ID | CashDistributionRefCustTrxLineGlDistId | — |
| REF_CUSTOMER_TRX_LINE_ID | CashDistributionRefCustomerTrxLineId | — |
| REF_DIST_CCID | CashDistributionRefDistCcid | — |
| REF_LINE_ID | CashDistributionRefLineId | — |
| REF_MF_DIST_FLAG | CashDistributionRefMfDistFlag | — |
| REF_MF_DIST_FLAG | CshDistRefLineRefMfDistFlag | — |
| REF_MF_DIST_FLAG | CshDistRevSrcRefMfDistFlag | — |
| REVERSAL_FLAG | CashDistributionReversalFlag | — |
| REVERSAL_FLAG | CshDistRefLineReversalFlag | — |
| REVERSAL_FLAG | CshDistRevSrcReversalFlag | — |
| REVERSED_SOURCE_ID | CashDistributionReversedSourceId | — |
| SOURCE_ID | CashDistributionSourceId | — |
| SOURCE_ID | CshDistRefLineSourceId | — |
| SOURCE_ID | CshDistRevSrcSourceId | — |
| SOURCE_ID_SECONDARY | CashDistributionSourceIdSecondary | — |
| SOURCE_ID_SECONDARY | CshDistRefLineSourceIdSecondary | — |
| SOURCE_ID_SECONDARY | CshDistRevSrcSourceIdSecondary | — |
| SOURCE_TABLE | CashDistributionSourceTable | — |
| SOURCE_TABLE | CshDistRefLineSourceTable | — |
| SOURCE_TABLE | CshDistRevSrcSourceTable | — |
| SOURCE_TABLE_SECONDARY | CashDistributionSourceTableSecondary | — |
| SOURCE_TABLE_SECONDARY | CshDistRefLineSourceTableSecondary | — |
| SOURCE_TABLE_SECONDARY | CshDistRevSrcSourceTableSecondary | — |
| SOURCE_TYPE | CashDistributionSourceType | ✅ |
| SOURCE_TYPE | CshDistRefLineSourceType | — |
| SOURCE_TYPE | CshDistRevSrcSourceType | — |
| SOURCE_TYPE_SECONDARY | CashDistributionSourceTypeSecondary | — |
| SOURCE_TYPE_SECONDARY | CshDistRefLineSourceTypeSecondary | — |
| SOURCE_TYPE_SECONDARY | CshDistRevSrcSourceTypeSecondary | — |
| TAX_CODE_ID | CashDistributionTaxCodeId | — |
| TAX_GROUP_CODE_ID | CashDistributionTaxGroupCodeId | — |
| TAX_ID | CashDistributionTaxId | — |
| TAX_LINK_ID | CashDistributionTaxLinkId | — |
| TAXABLE_ACCOUNTED_CR | CashDistributionTaxableAccountedCr | — |
| TAXABLE_ACCOUNTED_CR | CshDistRefLineTaxableAccountedCr | — |
| TAXABLE_ACCOUNTED_CR | CshDistRevSrcTaxableAccountedCr | — |
| TAXABLE_ACCOUNTED_DR | CashDistributionTaxableAccountedDr | — |
| TAXABLE_ACCOUNTED_DR | CshDistRefLineTaxableAccountedDr | — |
| TAXABLE_ACCOUNTED_DR | CshDistRevSrcTaxableAccountedDr | — |
| TAXABLE_ENTERED_CR | CashDistributionTaxableEnteredCr | — |
| TAXABLE_ENTERED_CR | CshDistRefLineTaxableEnteredCr | — |
| TAXABLE_ENTERED_CR | CshDistRevSrcTaxableEnteredCr | — |
| TAXABLE_ENTERED_DR | CashDistributionTaxableEnteredDr | — |
| TAXABLE_ENTERED_DR | CshDistRefLineTaxableEnteredDr | — |
| TAXABLE_ENTERED_DR | CshDistRevSrcTaxableEnteredDr | — |
| THIRD_PARTY_ID | CashDistributionThirdPartyId | — |
| THIRD_PARTY_SUB_ID | CashDistributionThirdPartySubId | — |

### [[receiptapplicationdistributionvc|ReceiptApplicationDistributionVC]] (AR · BICC: 22/101)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_CR | CashDistributionAcctdAmountCr | ✅ |
| ACCTD_AMOUNT_CR | CshDistRefLineAcctdAmountCr | — |
| ACCTD_AMOUNT_CR | CshDistRevSrcAcctdAmountCr | — |
| ACCTD_AMOUNT_DR | CashDistributionAcctdAmountDr | ✅ |
| ACCTD_AMOUNT_DR | CshDistRefLineAcctdAmountDr | — |
| ACCTD_AMOUNT_DR | CshDistRevSrcAcctdAmountDr | — |
| ACTIVITY_BUCKET | CashDistributionActivityBucket | ✅ |
| ACTIVITY_BUCKET | CshDistRefLineActivityBucket | — |
| ACTIVITY_BUCKET | CshDistRevSrcActivityBucket | — |
| AMOUNT_CR | CashDistributionAmountCr | ✅ |
| AMOUNT_CR | CshDistRefLineAmountCr | — |
| AMOUNT_CR | CshDistRevSrcAmountCr | — |
| AMOUNT_DR | CashDistributionAmountDr | ✅ |
| AMOUNT_DR | CshDistRefLineAmountDr | — |
| AMOUNT_DR | CshDistRevSrcAmountDr | — |
| CODE_COMBINATION_ID | CashDistributionCodeCombinationId | — |
| CREATED_BY | CashDistributionCreatedBy | — |
| CREATION_DATE | CashDistributionCreationDate | — |
| CURRENCY_CODE | CashDistributionCurrencyCode | — |
| CURRENCY_CODE | CshDistRefLineCurrencyCode | — |
| CURRENCY_CODE | CshDistRevSrcCurrencyCode | — |
| CURRENCY_CONVERSION_DATE | CashDistributionCurrencyConversionDate | ✅ |
| CURRENCY_CONVERSION_DATE | CshDistRefLineCurrencyConversionDate | — |
| CURRENCY_CONVERSION_DATE | CshDistRevSrcCurrencyConversionDate | — |
| CURRENCY_CONVERSION_RATE | CashDistributionCurrencyConversionRate | ✅ |
| CURRENCY_CONVERSION_RATE | CshDistRefLineCurrencyConversionRate | — |
| CURRENCY_CONVERSION_RATE | CshDistRevSrcCurrencyConversionRate | — |
| CURRENCY_CONVERSION_TYPE | CashDistributionCurrencyConversionType | ✅ |
| CURRENCY_CONVERSION_TYPE | CshDistRefLineCurrencyConversionType | — |
| CURRENCY_CONVERSION_TYPE | CshDistRevSrcCurrencyConversionType | — |
| FROM_ACCTD_AMOUNT_CR | CashDistributionFromAcctdAmountCr | ✅ |
| FROM_ACCTD_AMOUNT_CR | CshDistRefLineFromAcctdAmountCr | — |
| FROM_ACCTD_AMOUNT_CR | CshDistRevSrcFromAcctdAmountCr | — |
| FROM_ACCTD_AMOUNT_DR | CashDistributionFromAcctdAmountDr | ✅ |
| FROM_ACCTD_AMOUNT_DR | CshDistRefLineFromAcctdAmountDr | — |
| FROM_ACCTD_AMOUNT_DR | CshDistRevSrcFromAcctdAmountDr | — |
| FROM_AMOUNT_CR | CashDistributionFromAmountCr | ✅ |
| FROM_AMOUNT_CR | CshDistRefLineFromAmountCr | — |
| FROM_AMOUNT_CR | CshDistRevSrcFromAmountCr | — |
| FROM_AMOUNT_DR | CashDistributionFromAmountDr | ✅ |
| FROM_AMOUNT_DR | CshDistRefLineFromAmountDr | — |
| FROM_AMOUNT_DR | CshDistRevSrcFromAmountDr | — |
| LAST_UPDATE_DATE | CashDistributionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CashDistributionLastUpdateLogin | — |
| LAST_UPDATED_BY | CashDistributionLastUpdatedBy | — |
| LINE_ID | CshDistRefLineLineId | — |
| LINE_ID | CshDistRevSrcLineId | — |
| LINE_ID | LineId | ✅ |
| LOCATION_SEGMENT_ID | CashDistributionLocationSegmentId | — |
| OBJECT_VERSION_NUMBER | CashDistributionObjectVersionNumber | — |
| ORG_ID | CashDistributionOrgId | — |
| REF_ACCOUNT_CLASS | CashDistributionRefAccountClass | ✅ |
| REF_ACCOUNT_CLASS | CshDistRefLineRefAccountClass | — |
| REF_ACCOUNT_CLASS | CshDistRevSrcRefAccountClass | — |
| REF_CUST_TRX_LINE_GL_DIST_ID | CashDistributionRefCustTrxLineGlDistId | — |
| REF_CUSTOMER_TRX_LINE_ID | CashDistributionRefCustomerTrxLineId | — |
| REF_DIST_CCID | CashDistributionRefDistCcid | — |
| REF_LINE_ID | CashDistributionRefLineId | — |
| REF_MF_DIST_FLAG | CashDistributionRefMfDistFlag | — |
| REF_MF_DIST_FLAG | CshDistRefLineRefMfDistFlag | — |
| REF_MF_DIST_FLAG | CshDistRevSrcRefMfDistFlag | — |
| REVERSAL_FLAG | CashDistributionReversalFlag | — |
| REVERSAL_FLAG | CshDistRefLineReversalFlag | — |
| REVERSAL_FLAG | CshDistRevSrcReversalFlag | — |
| REVERSED_SOURCE_ID | CashDistributionReversedSourceId | — |
| SOURCE_ID | CashDistributionSourceId | ✅ |
| SOURCE_ID | CshDistRefLineSourceId | — |
| SOURCE_ID | CshDistRevSrcSourceId | — |
| SOURCE_ID_SECONDARY | CashDistributionSourceIdSecondary | — |
| SOURCE_ID_SECONDARY | CshDistRefLineSourceIdSecondary | — |
| SOURCE_ID_SECONDARY | CshDistRevSrcSourceIdSecondary | — |
| SOURCE_TABLE | CashDistributionSourceTable | ✅ |
| SOURCE_TABLE | CshDistRefLineSourceTable | — |
| SOURCE_TABLE | CshDistRevSrcSourceTable | — |
| SOURCE_TABLE_SECONDARY | CashDistributionSourceTableSecondary | — |
| SOURCE_TABLE_SECONDARY | CshDistRefLineSourceTableSecondary | — |
| SOURCE_TABLE_SECONDARY | CshDistRevSrcSourceTableSecondary | — |
| SOURCE_TYPE | CashDistributionSourceType | ✅ |
| SOURCE_TYPE | CshDistRefLineSourceType | — |
| SOURCE_TYPE | CshDistRevSrcSourceType | — |
| SOURCE_TYPE_SECONDARY | CashDistributionSourceTypeSecondary | — |
| SOURCE_TYPE_SECONDARY | CshDistRefLineSourceTypeSecondary | — |
| SOURCE_TYPE_SECONDARY | CshDistRevSrcSourceTypeSecondary | — |
| TAX_CODE_ID | CashDistributionTaxCodeId | — |
| TAX_GROUP_CODE_ID | CashDistributionTaxGroupCodeId | — |
| TAX_ID | CashDistributionTaxId | — |
| TAX_LINK_ID | CashDistributionTaxLinkId | — |
| TAXABLE_ACCOUNTED_CR | CashDistributionTaxableAccountedCr | ✅ |
| TAXABLE_ACCOUNTED_CR | CshDistRefLineTaxableAccountedCr | — |
| TAXABLE_ACCOUNTED_CR | CshDistRevSrcTaxableAccountedCr | — |
| TAXABLE_ACCOUNTED_DR | CashDistributionTaxableAccountedDr | ✅ |
| TAXABLE_ACCOUNTED_DR | CshDistRefLineTaxableAccountedDr | — |
| TAXABLE_ACCOUNTED_DR | CshDistRevSrcTaxableAccountedDr | — |
| TAXABLE_ENTERED_CR | CashDistributionTaxableEnteredCr | ✅ |
| TAXABLE_ENTERED_CR | CshDistRefLineTaxableEnteredCr | — |
| TAXABLE_ENTERED_CR | CshDistRevSrcTaxableEnteredCr | — |
| TAXABLE_ENTERED_DR | CashDistributionTaxableEnteredDr | ✅ |
| TAXABLE_ENTERED_DR | CshDistRefLineTaxableEnteredDr | — |
| TAXABLE_ENTERED_DR | CshDistRevSrcTaxableEnteredDr | — |
| THIRD_PARTY_ID | CashDistributionThirdPartyId | — |
| THIRD_PARTY_SUB_ID | CashDistributionThirdPartySubId | — |

### [[receipthistorydistributionpvo|ReceiptHistoryDistributionPVO]] (AR · BICC: 24/141)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_CR | AdjustmentDistributionAcctdAmountCr | — |
| ACCTD_AMOUNT_CR | CashDistributionAcctdAmountCr | ✅ |
| ACCTD_AMOUNT_CR | ReverseDistributionAcctdAmountCr | — |
| ACCTD_AMOUNT_DR | AdjustmentDistributionAcctdAmountDr | — |
| ACCTD_AMOUNT_DR | CashDistributionAcctdAmountDr | ✅ |
| ACCTD_AMOUNT_DR | ReverseDistributionAcctdAmountDr | — |
| ACTIVITY_BUCKET | AdjustmentDistributionActivityBucket | — |
| ACTIVITY_BUCKET | CashDistributionActivityBucket | ✅ |
| ACTIVITY_BUCKET | ReverseDistributionActivityBucket | — |
| AMOUNT_CR | AdjustmentDistributionAmountCr | — |
| AMOUNT_CR | CashDistributionAmountCr | ✅ |
| AMOUNT_CR | ReverseDistributionAmountCr | — |
| AMOUNT_DR | AdjustmentDistributionAmountDr | — |
| AMOUNT_DR | CashDistributionAmountDr | ✅ |
| AMOUNT_DR | ReverseDistributionAmountDr | — |
| CODE_COMBINATION_ID | AdjustmentDistributionCodeCombinationId | — |
| CODE_COMBINATION_ID | CashDistributionCodeCombinationId | — |
| CODE_COMBINATION_ID | ReverseDistributionCodeCombinationId | — |
| CREATED_BY | AdjustmentDistributionCreatedBy | — |
| CREATED_BY | CashDistributionCreatedBy | — |
| CREATED_BY | ReverseDistributionCreatedBy | — |
| CREATION_DATE | AdjustmentDistributionCreationDate | — |
| CREATION_DATE | CashDistributionCreationDate | — |
| CREATION_DATE | ReverseDistributionCreationDate | — |
| CURRENCY_CODE | AdjustmentDistributionCurrencyCode | — |
| CURRENCY_CODE | CashDistributionCurrencyCode | — |
| CURRENCY_CODE | ReverseDistributionCurrencyCode | — |
| CURRENCY_CONVERSION_DATE | AdjustmentDistributionCurrencyConversionDate | — |
| CURRENCY_CONVERSION_DATE | CashDistributionCurrencyConversionDate | ✅ |
| CURRENCY_CONVERSION_DATE | ReverseDistributionCurrencyConversionDate | — |
| CURRENCY_CONVERSION_RATE | AdjustmentDistributionCurrencyConversionRate | — |
| CURRENCY_CONVERSION_RATE | CashDistributionCurrencyConversionRate | ✅ |
| CURRENCY_CONVERSION_RATE | ReverseDistributionCurrencyConversionRate | — |
| CURRENCY_CONVERSION_TYPE | AdjustmentDistributionCurrencyConversionType | — |
| CURRENCY_CONVERSION_TYPE | CashDistributionCurrencyConversionType | ✅ |
| CURRENCY_CONVERSION_TYPE | ReverseDistributionCurrencyConversionType | — |
| FROM_ACCTD_AMOUNT_CR | AdjustmentDistributionFromAcctdAmountCr | — |
| FROM_ACCTD_AMOUNT_CR | CashDistributionFromAcctdAmountCr | ✅ |
| FROM_ACCTD_AMOUNT_CR | ReverseDistributionFromAcctdAmountCr | — |
| FROM_ACCTD_AMOUNT_DR | AdjustmentDistributionFromAcctdAmountDr | — |
| FROM_ACCTD_AMOUNT_DR | CashDistributionFromAcctdAmountDr | ✅ |
| FROM_ACCTD_AMOUNT_DR | ReverseDistributionFromAcctdAmountDr | — |
| FROM_AMOUNT_CR | AdjustmentDistributionFromAmountCr | — |
| FROM_AMOUNT_CR | CashDistributionFromAmountCr | ✅ |
| FROM_AMOUNT_CR | ReverseDistributionFromAmountCr | — |
| FROM_AMOUNT_DR | AdjustmentDistributionFromAmountDr | — |
| FROM_AMOUNT_DR | CashDistributionFromAmountDr | ✅ |
| FROM_AMOUNT_DR | ReverseDistributionFromAmountDr | — |
| LAST_UPDATE_DATE | AdjustmentDistributionLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | CashDistributionLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ReverseDistributionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AdjustmentDistributionLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | CashDistributionLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ReverseDistributionLastUpdateLogin | — |
| LAST_UPDATED_BY | AdjustmentDistributionLastUpdatedBy | — |
| LAST_UPDATED_BY | CashDistributionLastUpdatedBy | — |
| LAST_UPDATED_BY | ReverseDistributionLastUpdatedBy | — |
| LINE_ID | AdjustmentDistributionLineId | — |
| LINE_ID | LineId | ✅ |
| LINE_ID | ReverseDistributionLineId | — |
| LOCATION_SEGMENT_ID | AdjustmentDistributionLocationSegmentId | — |
| LOCATION_SEGMENT_ID | CashDistributionLocationSegmentId | — |
| LOCATION_SEGMENT_ID | ReverseDistributionLocationSegmentId | — |
| OBJECT_VERSION_NUMBER | AdjustmentDistributionObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | CashDistributionObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ReverseDistributionObjectVersionNumber | — |
| ORG_ID | AdjustmentDistributionOrgId | — |
| ORG_ID | CashDistributionOrgId | — |
| ORG_ID | ReverseDistributionOrgId | — |
| REF_ACCOUNT_CLASS | AdjustmentDistributionRefAccountClass | — |
| REF_ACCOUNT_CLASS | CashDistributionRefAccountClass | ✅ |
| REF_ACCOUNT_CLASS | ReverseDistributionRefAccountClass | — |
| REF_CUST_TRX_LINE_GL_DIST_ID | AdjustmentDistributionRefCustTrxLineGlDistId | — |
| REF_CUST_TRX_LINE_GL_DIST_ID | CashDistributionRefCustTrxLineGlDistId | — |
| REF_CUST_TRX_LINE_GL_DIST_ID | ReverseDistributionRefCustTrxLineGlDistId | — |
| REF_CUSTOMER_TRX_LINE_ID | AdjustmentDistributionRefCustomerTrxLineId | — |
| REF_CUSTOMER_TRX_LINE_ID | CashDistributionRefCustomerTrxLineId | — |
| REF_CUSTOMER_TRX_LINE_ID | ReverseDistributionRefCustomerTrxLineId | — |
| REF_DIST_CCID | AdjustmentDistributionRefDistCcid | — |
| REF_DIST_CCID | CashDistributionRefDistCcid | — |
| REF_DIST_CCID | ReverseDistributionRefDistCcid | — |
| REF_LINE_ID | AdjustmentDistributionRefLineId | — |
| REF_LINE_ID | CashDistributionRefLineId | — |
| REF_LINE_ID | ReverseDistributionRefLineId | — |
| REF_MF_DIST_FLAG | AdjustmentDistributionRefMfDistFlag | — |
| REF_MF_DIST_FLAG | CashDistributionRefMfDistFlag | — |
| REF_MF_DIST_FLAG | ReverseDistributionRefMfDistFlag | — |
| REVERSAL_FLAG | AdjustmentDistributionReversalFlag | — |
| REVERSAL_FLAG | CashDistributionReversalFlag | — |
| REVERSAL_FLAG | ReverseDistributionReversalFlag | — |
| REVERSED_SOURCE_ID | AdjustmentDistributionReversedSourceId | — |
| REVERSED_SOURCE_ID | CashDistributionReversedSourceId | — |
| REVERSED_SOURCE_ID | ReverseDistributionReversedSourceId | — |
| SOURCE_ID | AdjustmentDistributionSourceId | — |
| SOURCE_ID | CashDistributionSourceId | ✅ |
| SOURCE_ID | ReverseDistributionSourceId | — |
| SOURCE_ID_SECONDARY | AdjustmentDistributionSourceIdSecondary | — |
| SOURCE_ID_SECONDARY | CashDistributionSourceIdSecondary | — |
| SOURCE_ID_SECONDARY | ReverseDistributionSourceIdSecondary | — |
| SOURCE_TABLE | AdjustmentDistributionSourceTable | — |
| SOURCE_TABLE | CashDistributionSourceTable | ✅ |
| SOURCE_TABLE | ReverseDistributionSourceTable | — |
| SOURCE_TABLE_SECONDARY | AdjustmentDistributionSourceTableSecondary | — |
| SOURCE_TABLE_SECONDARY | CashDistributionSourceTableSecondary | — |
| SOURCE_TABLE_SECONDARY | ReverseDistributionSourceTableSecondary | — |
| SOURCE_TYPE | AdjustmentDistributionSourceType | — |
| SOURCE_TYPE | CashDistributionSourceType | ✅ |
| SOURCE_TYPE | ReverseDistributionSourceType | — |
| SOURCE_TYPE_SECONDARY | AdjustmentDistributionSourceTypeSecondary | — |
| SOURCE_TYPE_SECONDARY | CashDistributionSourceTypeSecondary | — |
| SOURCE_TYPE_SECONDARY | ReverseDistributionSourceTypeSecondary | — |
| TAX_CODE_ID | AdjustmentDistributionTaxCodeId | — |
| TAX_CODE_ID | CashDistributionTaxCodeId | — |
| TAX_CODE_ID | ReverseDistributionTaxCodeId | — |
| TAX_GROUP_CODE_ID | AdjustmentDistributionTaxGroupCodeId | — |
| TAX_GROUP_CODE_ID | CashDistributionTaxGroupCodeId | — |
| TAX_GROUP_CODE_ID | ReverseDistributionTaxGroupCodeId | — |
| TAX_ID | AdjustmentDistributionTaxId | — |
| TAX_ID | CashDistributionTaxId | — |
| TAX_ID | ReverseDistributionTaxId | — |
| TAX_LINK_ID | AdjustmentDistributionTaxLinkId | — |
| TAX_LINK_ID | CashDistributionTaxLinkId | — |
| TAX_LINK_ID | ReverseDistributionTaxLinkId | — |
| TAXABLE_ACCOUNTED_CR | AdjustmentDistributionTaxableAccountedCr | — |
| TAXABLE_ACCOUNTED_CR | CashDistributionTaxableAccountedCr | ✅ |
| TAXABLE_ACCOUNTED_CR | ReverseDistributionTaxableAccountedCr | — |
| TAXABLE_ACCOUNTED_DR | AdjustmentDistributionTaxableAccountedDr | — |
| TAXABLE_ACCOUNTED_DR | CashDistributionTaxableAccountedDr | ✅ |
| TAXABLE_ACCOUNTED_DR | ReverseDistributionTaxableAccountedDr | — |
| TAXABLE_ENTERED_CR | AdjustmentDistributionTaxableEnteredCr | — |
| TAXABLE_ENTERED_CR | CashDistributionTaxableEnteredCr | ✅ |
| TAXABLE_ENTERED_CR | ReverseDistributionTaxableEnteredCr | — |
| TAXABLE_ENTERED_DR | AdjustmentDistributionTaxableEnteredDr | — |
| TAXABLE_ENTERED_DR | CashDistributionTaxableEnteredDr | ✅ |
| TAXABLE_ENTERED_DR | ReverseDistributionTaxableEnteredDr | — |
| THIRD_PARTY_ID | AdjustmentDistributionThirdPartyId | — |
| THIRD_PARTY_ID | CashDistributionThirdPartyId | — |
| THIRD_PARTY_ID | ReverseDistributionThirdPartyId | — |
| THIRD_PARTY_SUB_ID | AdjustmentDistributionThirdPartySubId | — |
| THIRD_PARTY_SUB_ID | CashDistributionThirdPartySubId | — |
| THIRD_PARTY_SUB_ID | ReverseDistributionThirdPartySubId | — |

### [[transactionhistorydistributionpvo|TransactionHistoryDistributionPVO]] (AR · BICC: 7/41)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_CR | CashDistributionAcctdAmountCr | ✅ |
| ACCTD_AMOUNT_DR | CashDistributionAcctdAmountDr | ✅ |
| ACTIVITY_BUCKET | CashDistributionActivityBucket | — |
| AMOUNT_CR | CashDistributionAmountCr | ✅ |
| AMOUNT_DR | CashDistributionAmountDr | ✅ |
| CODE_COMBINATION_ID | CashDistributionCodeCombinationId | — |
| CURRENCY_CODE | CashDistributionCurrencyCode | ✅ |
| CURRENCY_CONVERSION_DATE | CashDistributionCurrencyConversionDate | — |
| CURRENCY_CONVERSION_RATE | CashDistributionCurrencyConversionRate | — |
| CURRENCY_CONVERSION_TYPE | CashDistributionCurrencyConversionType | — |
| FROM_ACCTD_AMOUNT_CR | CashDistributionFromAcctdAmountCr | — |
| FROM_ACCTD_AMOUNT_DR | CashDistributionFromAcctdAmountDr | — |
| FROM_AMOUNT_CR | CashDistributionFromAmountCr | — |
| FROM_AMOUNT_DR | CashDistributionFromAmountDr | — |
| LINE_ID | LineId | ✅ |
| LOCATION_SEGMENT_ID | CashDistributionLocationSegmentId | — |
| OBJECT_VERSION_NUMBER | CashDistributionObjectVersionNumber | — |
| REF_ACCOUNT_CLASS | CashDistributionRefAccountClass | — |
| REF_CUST_TRX_LINE_GL_DIST_ID | CashDistributionRefCustTrxLineGlDistId | — |
| REF_CUSTOMER_TRX_LINE_ID | CashDistributionRefCustomerTrxLineId | — |
| REF_DIST_CCID | CashDistributionRefDistCcid | — |
| REF_LINE_ID | CashDistributionRefLineId | — |
| REF_MF_DIST_FLAG | CashDistributionRefMfDistFlag | — |
| REVERSAL_FLAG | CashDistributionReversalFlag | — |
| REVERSED_SOURCE_ID | CashDistributionReversedSourceId | — |
| SOURCE_ID | CashDistributionSourceId | — |
| SOURCE_ID_SECONDARY | CashDistributionSourceIdSecondary | — |
| SOURCE_TABLE | CashDistributionSourceTable | — |
| SOURCE_TABLE_SECONDARY | CashDistributionSourceTableSecondary | — |
| SOURCE_TYPE | CashDistributionSourceType | — |
| SOURCE_TYPE_SECONDARY | CashDistributionSourceTypeSecondary | ✅ |
| TAX_CODE_ID | CashDistributionTaxCodeId | — |
| TAX_GROUP_CODE_ID | CashDistributionTaxGroupCodeId | — |
| TAX_ID | CashDistributionTaxId | — |
| TAX_LINK_ID | CashDistributionTaxLinkId | — |
| TAXABLE_ACCOUNTED_CR | CashDistributionTaxableAccountedCr | — |
| TAXABLE_ACCOUNTED_DR | CashDistributionTaxableAccountedDr | — |
| TAXABLE_ENTERED_CR | CashDistributionTaxableEnteredCr | — |
| TAXABLE_ENTERED_DR | CashDistributionTaxableEnteredDr | — |
| THIRD_PARTY_ID | CashDistributionThirdPartyId | — |
| THIRD_PARTY_SUB_ID | CashDistributionThirdPartySubId | — |

---

## 📚 Referências

- [Oracle Docs — AR_DISTRIBUTIONS_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/ardistributionsall-10041.html)
- [[ar-module-data-dictionary]] — Dossiê do módulo AR
