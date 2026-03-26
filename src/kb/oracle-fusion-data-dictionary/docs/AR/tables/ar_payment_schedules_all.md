---
id: DOC-AR-021
doc_type: system-doc
title: "AR_PAYMENT_SCHEDULES_ALL — Cronogramas de Pagamento"
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
  - cronograma-pagamento
  - payment-schedules
  - aging
aliases:
  - AR_PAYMENT_SCHEDULES_ALL
  - ar_payment_schedules_all
  - cronograma-pagamento-ar
  - payment-schedules
  - aging-ar
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_PAYMENT_SCHEDULES_ALL

## 📌 Visão Geral

Armazena os **cronogramas de pagamento de todas as transações e recebimentos** do módulo Accounts Receivable. Cada registro representa uma parcela de pagamento com data de vencimento, valor original, saldo remanescente e valores aplicados/creditados/ajustados. É a tabela fundamental para cálculo de **aging** (envelhecimento de recebíveis), controle de inadimplência e análise de saldos em aberto.

A coluna `CLASS` distingue o tipo: INV (fatura), CM (credit memo), DM (debit memo), DEP (depósito), GUAR (garantia), BR (bill receivable) e PMT (pagamento/recebimento).

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Aging de recebíveis:** Cálculo de saldos em aberto por faixa de vencimento (current, 1-30, 31-60, 61-90, 90+).
- **Controle de inadimplência:** Identificação de faturas vencidas via `DUE_DATE` × `AMOUNT_DUE_REMAINING`.
- **Cobrança:** Base para processos de dunning — seleção de faturas vencidas por cliente/site.
- **Conciliação AR:** Saldo em aberto (`AMOUNT_DUE_REMAINING`) deve bater com subledger e GL.
- **Relatórios de saldo:** Extração de posição de contas a receber por cliente, moeda, business unit.
- **Disputas:** Registro de valores em disputa via `AMOUNT_IN_DISPUTE`.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PAYMENT_SCHEDULE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do schedule de pagamento | — | 🟢 100% |
| 2 | CUSTOMER_TRX_ID | NUMBER(18) | NULL | FK | Transação associada (faturas, CMs, DMs) | [[ra_customer_trx_all]] | 🟢 100% |
| 3 | CASH_RECEIPT_ID | NUMBER(18) | NULL | FK | Recebimento associado | [[ar_cash_receipts_all]] | 🟢 100% |
| 4 | CLASS | VARCHAR2(30) | NOT NULL | Classificação | Tipo: INV/CM/DM/DEP/GUAR/BR/PMT | — | 🟢 100% |
| 5 | STATUS | VARCHAR2(30) | NOT NULL | Classificação | Status: OP (aberto) ou CL (fechado) | — | 🟢 100% |
| 6 | DUE_DATE | DATE | NOT NULL | Data | Data de vencimento da parcela | — | 🟢 100% |
| 7 | AMOUNT_DUE_ORIGINAL | NUMBER | NOT NULL | Financeiro | Valor original da parcela | — | 🟢 100% |
| 8 | AMOUNT_DUE_REMAINING | NUMBER | NOT NULL | Financeiro | Saldo remanescente (valor em aberto) | — | 🟢 100% |
| 9 | AMOUNT_APPLIED | NUMBER | NULL | Financeiro | Total aplicado (recebimentos + credit memos) | — | 🟢 100% |
| 10 | AMOUNT_CREDITED | NUMBER | NULL | Financeiro | Total creditado via credit memos | — | 🟢 100% |
| 11 | AMOUNT_ADJUSTED | NUMBER | NULL | Financeiro | Total ajustado (write-offs, reclassificações) | — | 🟢 100% |
| 12 | AMOUNT_IN_DISPUTE | NUMBER | NULL | Financeiro | Valor em disputa | — | 🟢 100% |
| 13 | AMOUNT_LINE_ITEMS_ORIGINAL | NUMBER | NULL | Financeiro | Valor original de itens de linha | — | 🟢 100% |
| 14 | TAX_ORIGINAL | NUMBER | NULL | Financeiro | Valor original de imposto | — | 🟢 100% |
| 15 | TAX_REMAINING | NUMBER | NULL | Financeiro | Saldo remanescente de imposto | — | 🟢 100% |
| 16 | FREIGHT_ORIGINAL | NUMBER | NULL | Financeiro | Valor original de frete | — | 🟢 100% |
| 17 | FREIGHT_REMAINING | NUMBER | NULL | Financeiro | Saldo remanescente de frete | — | 🟢 100% |
| 18 | NUMBER_OF_DUE_DATES | NUMBER | NULL | Financeiro | Número total de parcelas da transação | — | 🟢 100% |
| 19 | TERMS_SEQUENCE_NUMBER | NUMBER | NULL | Financeiro | Número sequencial da parcela nos termos de pagamento | — | 🟢 100% |
| 20 | CUSTOMER_ID | NUMBER(18) | NULL | Cliente | Conta do cliente | [[hz_cust_accounts]] | 🟢 100% |
| 21 | CUSTOMER_SITE_USE_ID | NUMBER(18) | NULL | Cliente | Site de uso do cliente | [[hz_cust_site_uses_all]] | 🟢 100% |
| 22 | INVOICE_CURRENCY_CODE | VARCHAR2(15) | NOT NULL | Financeiro | Código da moeda (ISO 4217) | — | 🟢 100% |
| 23 | EXCHANGE_RATE_TYPE | VARCHAR2(30) | NULL | Financeiro | Tipo de taxa de câmbio | [[gl_daily_conversion_types]] | 🟢 100% |
| 24 | EXCHANGE_RATE | NUMBER | NULL | Financeiro | Taxa de câmbio aplicada | — | 🟢 100% |
| 25 | EXCHANGE_DATE | DATE | NULL | Financeiro | Data da taxa de câmbio | — | 🟢 100% |
| 26 | GL_DATE | DATE | NULL | Contabilidade | Data contábil (General Ledger) | — | 🟢 100% |
| 27 | GL_DATE_CLOSED | DATE | NULL | Contabilidade | Data contábil de fechamento | — | 🟢 100% |
| 28 | ACTUAL_DATE_CLOSED | DATE | NULL | Data | Data real de fechamento do schedule | — | 🟢 100% |
| 29 | TRX_NUMBER | VARCHAR2(30) | NULL | Identificação | Número da transação (denormalizado) | — | 🟢 100% |
| 30 | TRX_DATE | DATE | NULL | Data | Data da transação (denormalizado) | — | 🟢 100% |
| 31 | CUST_TRX_TYPE_ID | NUMBER(18) | NULL | Classificação | Tipo de transação | [[ra_cust_trx_types_all]] | 🟢 100% |
| 32 | TERM_ID | NUMBER(18) | NULL | Financeiro | Condição de pagamento | [[ra_terms_b]] | 🟢 100% |
| 33 | DISCOUNT_DATE | DATE | NULL | Data | Data limite para desconto | — | 🟢 100% |
| 34 | DISCOUNT_ORIGINAL | NUMBER | NULL | Financeiro | Valor do desconto disponível | — | 🟢 100% |
| 35 | DISCOUNT_TAKEN_EARNED | NUMBER | NULL | Financeiro | Desconto concedido aproveitado | — | 🟢 100% |
| 36 | DISCOUNT_TAKEN_UNEARNED | NUMBER | NULL | Financeiro | Desconto não-concedido aproveitado | — | 🟢 100% |
| 37 | SELECTED_FOR_RECEIPT_BATCH_ID | NUMBER(18) | NULL | Controle | Lote de recebimento em que o schedule foi selecionado | — | 🟢 100% |
| 38 | DISPUTE_DATE | DATE | NULL | Data | Data da disputa | — | 🟢 100% |
| 39 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 40 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 41 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 42 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 43 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 44 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ra_customer_trx_all]] — via `CUSTOMER_TRX_ID` (transação de cliente associada à parcela)
- [[ar_cash_receipts_all]] — via `CASH_RECEIPT_ID` (recebimento de caixa vinculado à parcela)
- [[hz_cust_accounts]] — via `CUSTOMER_ID` (cliente devedor da parcela)
- [[hz_cust_site_uses_all]] — via `CUSTOMER_SITE_USE_ID` (site do cliente)
- [[ra_cust_trx_types_all]] — via `CUST_TRX_TYPE_ID` (tipo de transação)
- [[ra_terms_b]] — via `TERM_ID` (condição de pagamento)
- [[gl_daily_conversion_types]] — via `EXCHANGE_RATE_TYPE` (tipo de câmbio da parcela de recebimento)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit da parcela de recebimento)

### Tabelas-filha (FK de saída)
- [[ar_receivable_applications_all]] — via `APPLIED_PAYMENT_SCHEDULE_ID` e `PAYMENT_SCHEDULE_ID` (aplicações de pagamento contra esta parcela)
- [[ar_adjustments_all]] — via `PAYMENT_SCHEDULE_ID` (ajustes aplicados a esta parcela de recebimento)

---

## 📎 Uso Típico

### Saldo em aberto por cliente (aging)
```sql
SELECT ps.CUSTOMER_ID, hca.ACCOUNT_NAME,
       SUM(ps.AMOUNT_DUE_REMAINING) AS saldo_aberto,
       SUM(CASE WHEN ps.DUE_DATE < SYSDATE THEN ps.AMOUNT_DUE_REMAINING ELSE 0 END) AS vencido
FROM   AR_PAYMENT_SCHEDULES_ALL ps
JOIN   HZ_CUST_ACCOUNTS hca ON hca.CUST_ACCOUNT_ID = ps.CUSTOMER_ID
WHERE  ps.STATUS = 'OP'
  AND  ps.CLASS = 'INV'
  AND  ps.ORG_ID = :p_org_id
GROUP BY ps.CUSTOMER_ID, hca.ACCOUNT_NAME;
```

### Faturas vencidas há mais de 90 dias
```sql
SELECT ps.TRX_NUMBER, ps.DUE_DATE, ps.AMOUNT_DUE_REMAINING,
       TRUNC(SYSDATE) - ps.DUE_DATE AS dias_atraso
FROM   AR_PAYMENT_SCHEDULES_ALL ps
WHERE  ps.STATUS = 'OP'
  AND  ps.CLASS = 'INV'
  AND  ps.DUE_DATE < SYSDATE - 90
  AND  ps.ORG_ID = :p_org_id
ORDER BY dias_atraso DESC;
```

### Filtros comuns
- `STATUS = 'OP'` — Schedules em aberto
- `STATUS = 'CL'` — Schedules fechados
- `CLASS = 'INV'` — Apenas faturas
- `CLASS = 'PMT'` — Apenas recebimentos
- `AMOUNT_DUE_REMAINING > 0` — Com saldo remanescente

---

## 🔒 Observações

- A relação `AMOUNT_DUE_REMAINING = AMOUNT_DUE_ORIGINAL - AMOUNT_APPLIED - AMOUNT_CREDITED - AMOUNT_ADJUSTED` deve ser sempre consistente.
- Um registro existe para **cada parcela** — transações com condição de pagamento parcelada geram múltiplos schedules (e.g., 30/60/90 dias gera 3 registros).
- O campo `CLASS = 'PMT'` indica um schedule de recebimento (cash receipt) — o saldo remanescente negativo indica valor não-aplicado.
- Os campos `GL_DATE_CLOSED` e `ACTUAL_DATE_CLOSED` são preenchidos quando `STATUS` muda para 'CL'.
- Os campos `TAX_ORIGINAL`, `TAX_REMAINING`, `FREIGHT_ORIGINAL`, `FREIGHT_REMAINING` são **denormalizados** para performance em relatórios de aging.

---

## 📚 Referências

- [Oracle Docs — AR_PAYMENT_SCHEDULES_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/arpaymentschedulesall-10053.html)
- [[ar-module-data-dictionary]] — Dossiê do módulo AR
