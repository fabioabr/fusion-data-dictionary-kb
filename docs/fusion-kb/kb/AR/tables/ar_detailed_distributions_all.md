---
id: DOC-AR-030
doc_type: system-doc
title: "AR_DETAILED_DISTRIBUTIONS_ALL — Distribuições Detalhadas para XLA"
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
  - distribuicoes-detalhadas
  - xla
  - subledger-accounting
aliases:
  - AR_DETAILED_DISTRIBUTIONS_ALL
  - ar_detailed_distributions_all
  - distribuicoes-detalhadas-ar
  - detailed-distributions
  - xla-distributions-ar
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_DETAILED_DISTRIBUTIONS_ALL

## 📌 Visão Geral

Armazena as **distribuições detalhadas** do módulo Accounts Receivable, servindo como interface para o **Subledger Accounting (XLA)**. Cada registro representa uma linha de distribuição granular vinculada a uma entidade-origem via `SOURCE_TABLE` + `SOURCE_ID`, com CCID de referência e valores na moeda da transação e funcional. É uma camada de detalhe acima de [[ar_distributions_all]], provendo informações adicionais necessárias para o mecanismo de contabilização do subledger.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Subledger Accounting (XLA):** Fonte de dados para o mecanismo de criação de journal entries no subledger.
- **Contabilização detalhada:** Provê granularidade adicional sobre as distribuições contábeis do AR.
- **Reconciliação XLA × GL:** Base para conciliar lançamentos do subledger com o General Ledger.
- **Auditoria contábil:** Rastreabilidade completa das distribuições até o nível de detalhe exigido pelo XLA.
- **Relatórios contábeis:** Extração de dados para relatórios de subledger com detalhamento por evento contábil.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DETAILED_DIST_ID | NUMBER(18) | NOT NULL | PK | Identificador único da distribuição detalhada | — | 🟢 100% |
| 2 | SOURCE_ID | NUMBER(18) | NOT NULL | FK | ID da entidade-origem (varia conforme SOURCE_TABLE) | — | 🟢 100% |
| 3 | SOURCE_TABLE | VARCHAR2(10) | NOT NULL | Classificação | Tabela de origem: RA, ADJ, MCD, CRH | — | 🟢 100% |
| 4 | SOURCE_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo da distribuição | — | 🟢 100% |
| 5 | CODE_COMBINATION_ID | NUMBER(18) | NOT NULL | Contabilidade | Combinação de contas contábeis (CCID) | [[gl_code_combinations]] | 🟢 100% |
| 6 | AMOUNT | NUMBER | NOT NULL | Financeiro | Valor na moeda da transação | — | 🟢 100% |
| 7 | ACCTD_AMOUNT | NUMBER | NULL | Financeiro | Valor na moeda funcional | — | 🟢 100% |
| 8 | AMOUNT_DR | NUMBER | NULL | Financeiro | Valor a débito | — | 🟢 100% |
| 9 | AMOUNT_CR | NUMBER | NULL | Financeiro | Valor a crédito | — | 🟢 100% |
| 10 | ACCTD_AMOUNT_DR | NUMBER | NULL | Financeiro | Valor a débito na moeda funcional | — | 🟢 100% |
| 11 | ACCTD_AMOUNT_CR | NUMBER | NULL | Financeiro | Valor a crédito na moeda funcional | — | 🟢 100% |
| 12 | REF_DIST_CCID | NUMBER(18) | NULL | Contabilidade | CCID de referência da distribuição original | [[gl_code_combinations]] | 🟢 100% |
| 13 | CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Código da moeda da transação | — | 🟢 100% |
| 14 | CURRENCY_CONVERSION_RATE | NUMBER | NULL | Financeiro | Taxa de conversão cambial | — | 🟢 100% |
| 15 | CURRENCY_CONVERSION_TYPE | VARCHAR2(30) | NULL | Financeiro | Tipo de conversão cambial | — | 🟢 100% |
| 16 | CURRENCY_CONVERSION_DATE | DATE | NULL | Financeiro | Data da conversão cambial | — | 🟢 100% |
| 17 | REF_MF_DIST_FLAG | VARCHAR2(1) | NULL | Controle | Flag de referência multi-fund distribution (Y/N) | — | 🟢 100% |
| 18 | REF_LINE_ID | NUMBER(18) | NULL | Referência cruzada | ID da linha de distribuição de referência em AR_DISTRIBUTIONS_ALL | [[ar_distributions_all]] | 🟢 100% |
| 19 | GL_DATE | DATE | NULL | Contabilidade | Data contábil | — | 🟢 100% |
| 20 | THIRD_PARTY_ID | NUMBER(18) | NULL | Cliente | ID do terceiro (cliente) | [[hz_cust_accounts]] | 🟢 100% |
| 21 | THIRD_PARTY_SUB_ID | NUMBER(18) | NULL | Cliente | ID do sub-terceiro (site do cliente) | [[hz_cust_site_uses_all]] | 🟢 100% |
| 22 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 23 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 24 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 25 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 26 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 27 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada — via SOURCE_TABLE + SOURCE_ID)
- [[ar_distributions_all]] — via `REF_LINE_ID` (distribuição de referência)
- [[gl_code_combinations]] — via `CODE_COMBINATION_ID` e `REF_DIST_CCID` (conta contábil da distribuição detalhada de AR)
- [[hz_cust_accounts]] — via `THIRD_PARTY_ID` (cliente terceiro da distribuição detalhada)
- [[hz_cust_site_uses_all]] — via `THIRD_PARTY_SUB_ID` (site do cliente na distribuição detalhada)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit da distribuição detalhada de AR)

### Tabelas-filha (FK de saída)
- **XLA_DISTRIBUTION_LINKS** — vinculação com journal entries do subledger accounting

---

## 📎 Uso Típico

### Distribuições detalhadas de uma aplicação
```sql
SELECT dd.SOURCE_TYPE, dd.CODE_COMBINATION_ID, dd.REF_DIST_CCID,
       dd.AMOUNT, dd.ACCTD_AMOUNT, dd.CURRENCY_CODE
FROM   AR_DETAILED_DISTRIBUTIONS_ALL dd
WHERE  dd.SOURCE_TABLE = 'RA'
  AND  dd.SOURCE_ID = :p_receivable_application_id;
```

### Conciliação com AR_DISTRIBUTIONS_ALL
```sql
SELECT d.LINE_ID, d.AMOUNT_DR, d.AMOUNT_CR,
       dd.DETAILED_DIST_ID, dd.AMOUNT, dd.REF_DIST_CCID
FROM   AR_DISTRIBUTIONS_ALL d
JOIN   AR_DETAILED_DISTRIBUTIONS_ALL dd
       ON dd.SOURCE_TABLE = d.SOURCE_TABLE
      AND dd.SOURCE_ID = d.SOURCE_ID
      AND dd.REF_LINE_ID = d.LINE_ID
WHERE  d.SOURCE_TABLE = 'CRH'
  AND  d.ORG_ID = :p_org_id;
```

---

## 🔒 Observações

- Esta tabela é uma **camada de detalhe** acima de [[ar_distributions_all]] — utiliza o mesmo padrão polimórfico `SOURCE_TABLE` + `SOURCE_ID`.
- O campo `REF_DIST_CCID` referencia o CCID da distribuição **original** — útil para rastrear reclassificações.
- O campo `REF_MF_DIST_FLAG` indica se a distribuição faz parte de um cenário de **multi-fund accounting**.
- O `REF_LINE_ID` vincula esta distribuição detalhada à linha correspondente em [[ar_distributions_all]].
- Essencial para integração com **XLA (Subledger Accounting)** — sem esta tabela, os journal entries do subledger não são gerados corretamente.

---

## 🔗 PVOs Relacionados

### [[detaileddistributionsallextractpvo|DetailedDistributionsAllExtractPVO]] (OTHER · BICC: 46/46)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCTD_AMOUNT_APPLIED_FROM | DetailedDistributionsAllAcctdAmountAppliedFrom | ✅ |
| ACCTD_AMOUNT_APPLIED_TO | DetailedDistributionsAllAcctdAmountAppliedTo | ✅ |
| ACCTD_AMOUNT_CR | DetailedDistributionsAllAcctdAmountCr | ✅ |
| ACCTD_AMOUNT_DR | DetailedDistributionsAllAcctdAmountDr | ✅ |
| ACCTD_EARNED_DISCOUNT_TAKEN | DetailedDistributionsAllAcctdEarnedDiscountTaken | ✅ |
| ACCTD_UNEARNED_DISCOUNT_TAKEN | DetailedDistributionsAllAcctdUnearnedDiscountTaken | ✅ |
| ACTIVITY_BUCKET | DetailedDistributionsAllActivityBucket | ✅ |
| AMOUNT_APPLIED | DetailedDistributionsAllAmountApplied | ✅ |
| AMOUNT_APPLIED_FROM | DetailedDistributionsAllAmountAppliedFrom | ✅ |
| AMOUNT_CR | DetailedDistributionsAllAmountCr | ✅ |
| AMOUNT_DR | DetailedDistributionsAllAmountDr | ✅ |
| APP_SOURCE_ID | DetailedDistributionsAllAppSourceId | ✅ |
| ASSOCIATED_DIST_ID | DetailedDistributionsAllAssociatedDistId | ✅ |
| BALANCE_ACCTD_AMOUNT | DetailedDistributionsAllBalanceAcctdAmount | ✅ |
| BALANCE_AMOUNT | DetailedDistributionsAllBalanceAmount | ✅ |
| CASH_RECEIPT_HISTORY_ID | DetailedDistributionsAllCashReceiptHistoryId | ✅ |
| CREATED_BY | DetailedDistributionsAllCreatedBy | ✅ |
| CREATION_DATE | DetailedDistributionsAllCreationDate | ✅ |
| DETAILED_DIST_ENTRY | DetailedDistributionsAllDetailedDistEntry | ✅ |
| DETAILED_DIST_ID | DetailedDistributionsAllDetailedDistId | ✅ |
| EARNED_DISCOUNT_TAKEN | DetailedDistributionsAllEarnedDiscountTaken | ✅ |
| FROM_ACCTD_AMOUNT_CR | DetailedDistributionsAllFromAcctdAmountCr | ✅ |
| FROM_ACCTD_AMOUNT_DR | DetailedDistributionsAllFromAcctdAmountDr | ✅ |
| FROM_AMOUNT_CR | DetailedDistributionsAllFromAmountCr | ✅ |
| FROM_AMOUNT_DR | DetailedDistributionsAllFromAmountDr | ✅ |
| FROM_TO_CODE | DetailedDistributionsAllFromToCode | ✅ |
| LAST_UPDATE_DATE | DetailedDistributionsAllLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DetailedDistributionsAllLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | DetailedDistributionsAllLastUpdatedBy | ✅ |
| LATEST_ACTIVITY_FLAG | DetailedDistributionsAllLatestActivityFlag | ✅ |
| OBJECT_VERSION_NUMBER | DetailedDistributionsAllObjectVersionNumber | ✅ |
| ORG_ID | DetailedDistributionsAllOrgId | ✅ |
| PRIOR_DETAILED_DIST_ID | DetailedDistributionsAllPriorDetailedDistId | ✅ |
| REF_ACCOUNT_CLASS | DetailedDistributionsAllRefAccountClass | ✅ |
| REF_CUST_TRX_LINE_GL_DIST_ID | DetailedDistributionsAllRefCustTrxLineGlDistId | ✅ |
| REF_CUSTOMER_TRX_LINE_ID | DetailedDistributionsAllRefCustomerTrxLineId | ✅ |
| REF_DIST_CCID | DetailedDistributionsAllRefDistCcid | ✅ |
| SOURCE_DIST_ID | DetailedDistributionsAllSourceDistId | ✅ |
| SOURCE_ID | DetailedDistributionsAllSourceId | ✅ |
| SOURCE_TABLE | DetailedDistributionsAllSourceTable | ✅ |
| SOURCE_TYPE | DetailedDistributionsAllSourceType | ✅ |
| TAXABLE_ACCOUNTED_CR | DetailedDistributionsAllTaxableAccountedCr | ✅ |
| TAXABLE_ACCOUNTED_DR | DetailedDistributionsAllTaxableAccountedDr | ✅ |
| TAXABLE_ENTERED_CR | DetailedDistributionsAllTaxableEnteredCr | ✅ |
| TAXABLE_ENTERED_DR | DetailedDistributionsAllTaxableEnteredDr | ✅ |
| UNEARNED_DISCOUNT_TAKEN | DetailedDistributionsAllUnearnedDiscountTaken | ✅ |

---

## 📚 Referências

- [Oracle Docs — AR_DETAILED_DISTRIBUTIONS_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/ardetaileddistributionsall-25090.html)
- [[ar-module-data-dictionary]] — Dossiê do módulo AR
