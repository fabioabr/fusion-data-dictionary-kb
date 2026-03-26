---
id: DOC-AR-042
doc_type: system-doc
title: "AR_CONS_INV_ALL — Faturamento Consolidado (Balance Forward Billing)"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-receivable, data-dictionary, faturamento-consolidado, balance-forward, cons-inv]
aliases: [AR_CONS_INV_ALL, ar_cons_inv_all, cons_inv, faturamento_consolidado, consolidated_invoice]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_CONS_INV_ALL

> [!note] Sufixo _ALL
> Tabela particionada por `ORG_ID`. O sufixo `_ALL` indica que contém dados de todas as business units. Acessos via views sem sufixo filtram automaticamente pelo contexto de segurança da sessão.

## 📌 Visão Geral

Tabela de faturamento consolidado (consolidated invoices / balance forward billing) do Accounts Receivable. Cada registro representa um extrato consolidado para um cliente, agrupando múltiplas transações em um único documento de cobrança com saldo inicial, movimentações e saldo final.

## 🧠 Propósito de Negócio

O faturamento consolidado é utilizado quando a empresa emite um único documento de cobrança periódico ao cliente, em vez de cobrar cada fatura individualmente. Esse modelo é comum em relações de alto volume transacional (ex.: cartões corporativos, serviços recorrentes). O balance forward billing permite ao cliente receber um extrato com saldo anterior, novas cobranças, pagamentos recebidos e saldo final a pagar.

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Descrição | Categoria | Confiança |
|---|--------|------|-------|-----------|-----------|-----------|
| 1 | CONS_INV_ID | NUMBER(15) | NOT NULL | Chave primária. Identificador único do faturamento consolidado. | PK | 🟢 100% |
| 2 | CONS_BILLING_NUMBER | VARCHAR2(30) | NOT NULL | Número do documento consolidado de cobrança. | Negócio | 🟢 100% |
| 3 | CUSTOMER_ID | NUMBER(15) | NOT NULL | FK para HZ_CUST_ACCOUNTS. Cliente do faturamento. | FK | 🟢 100% |
| 4 | SITE_USE_ID | NUMBER(15) | NULL | FK para HZ_CUST_SITE_USES_ALL. Site de cobrança do cliente. | FK | 🟢 100% |
| 5 | CURRENCY_CODE | VARCHAR2(15) | NOT NULL | Código da moeda do documento consolidado. | Financeiro | 🟢 100% |
| 6 | BEGINNING_BALANCE | NUMBER | NULL | Saldo inicial do período (carregado do período anterior). | Financeiro | 🟢 100% |
| 7 | ENDING_BALANCE | NUMBER | NULL | Saldo final do período (a pagar pelo cliente). | Financeiro | 🟢 100% |
| 8 | CONS_INV_TYPE | VARCHAR2(30) | NOT NULL | Tipo do documento consolidado (ex.: BALANCE_FORWARD, OPEN_ITEM). | Classificação | 🟢 100% |
| 9 | STATUS | VARCHAR2(30) | NOT NULL | Status do documento (ex.: DRAFT, FINAL, PRINTED, ACCEPTED). | Controle | 🟢 100% |
| 10 | CUT_OFF_DATE | DATE | NOT NULL | Data de corte para inclusão de transações. | Temporal | 🟢 100% |
| 11 | ISSUE_DATE | DATE | NOT NULL | Data de emissão do documento consolidado. | Temporal | 🟢 100% |
| 12 | DUE_DATE | DATE | NULL | Data de vencimento do saldo consolidado. | Temporal | 🟢 100% |
| 13 | PRINT_STATUS | VARCHAR2(30) | NULL | Status de impressão (ex.: PENDING, PRINTED, REPRINTED). | Controle | 🟢 100% |
| 14 | TERM_ID | NUMBER(15) | NULL | FK para condições de pagamento. | FK | 🟢 100% |
| 15 | TOTAL_INVOICES_AMOUNT | NUMBER | NULL | Valor total das faturas incluídas no consolidado. | Financeiro | 🟢 100% |
| 16 | TOTAL_CREDITS_AMOUNT | NUMBER | NULL | Valor total dos créditos no período. | Financeiro | 🟢 100% |
| 17 | TOTAL_PAYMENTS_AMOUNT | NUMBER | NULL | Valor total dos pagamentos recebidos no período. | Financeiro | 🟢 100% |
| 18 | TOTAL_ADJUSTMENTS_AMOUNT | NUMBER | NULL | Valor total dos ajustes no período. | Financeiro | 🟡 75% |
| 19 | ORG_ID | NUMBER(15) | NOT NULL | Identificador da business unit (Operating Unit). | Partição | 🟢 100% |
| 20 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | Contexto de flexfield descritivo. | DFF | 🟢 100% |
| 21 | REQUEST_ID | NUMBER(15) | NULL | Identificador da requisição concorrente que gerou o registro. | Técnico | 🟢 100% |
| 22 | CREATED_BY | VARCHAR2(64) | NOT NULL | Usuário que criou o registro. | WHO | 🟢 100% |
| 23 | CREATION_DATE | DATE | NOT NULL | Data de criação do registro. | WHO | 🟢 100% |
| 24 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Usuário da última atualização. | WHO | 🟢 100% |
| 25 | LAST_UPDATE_DATE | DATE | NOT NULL | Data da última atualização. | WHO | 🟢 100% |

## 🔗 Relacionamentos

- **HZ_CUST_ACCOUNTS** — Cliente do faturamento consolidado (N:1 via `CUSTOMER_ID`).
- **HZ_CUST_SITE_USES_ALL** — Site de cobrança (N:1 via `SITE_USE_ID`).
- **AR_CONS_INV_TRX_ALL** — Transações incluídas no documento consolidado (1:N via `CONS_INV_ID`).
- **[[ar_statement_cycles]]** — Ciclo de extrato que pode disparar a geração do consolidado.

## 📎 Uso Típico

```sql
-- Faturamento consolidado pendente por cliente
SELECT ci.CONS_BILLING_NUMBER,
       ci.CUSTOMER_ID,
       ci.CURRENCY_CODE,
       ci.BEGINNING_BALANCE,
       ci.ENDING_BALANCE,
       ci.ISSUE_DATE,
       ci.DUE_DATE,
       ci.STATUS
  FROM AR_CONS_INV_ALL ci
 WHERE ci.ORG_ID = :p_org_id
   AND ci.STATUS NOT IN ('ACCEPTED', 'CANCELLED')
 ORDER BY ci.DUE_DATE;
```

## 🔒 Observações

- `ENDING_BALANCE` = `BEGINNING_BALANCE` + `TOTAL_INVOICES_AMOUNT` - `TOTAL_PAYMENTS_AMOUNT` - `TOTAL_CREDITS_AMOUNT` +/- `TOTAL_ADJUSTMENTS_AMOUNT`.
- O `CUT_OFF_DATE` determina quais transações são incluídas no consolidado; transações posteriores ficam para o próximo ciclo.
- Documentos com `STATUS = 'DRAFT'` podem ser regenerados; uma vez finalizado, o número é definitivo.
- Filtrar sempre por `ORG_ID` para garantir contexto correto de business unit.

## 📚 Referências

- Oracle Fusion Cloud Financials — Accounts Receivable Tables (OEDMF Release 13).
- Oracle Fusion Cloud — Balance Forward Billing Documentation.
- Oracle Fusion Cloud ERP Schema Reference (Release 25A).
