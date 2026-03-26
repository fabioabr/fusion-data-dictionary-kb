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

## 📚 Referências

- [Oracle Docs — AR_DISTRIBUTIONS_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/ardistributionsall-10041.html)
- [[ar-module-data-dictionary]] — Dossiê do módulo AR
