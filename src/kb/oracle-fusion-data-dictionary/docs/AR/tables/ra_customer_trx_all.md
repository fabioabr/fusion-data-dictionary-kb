---
id: DOC-AR-001
doc_type: system-doc
title: "RA_CUSTOMER_TRX_ALL — Cabeçalho de Transações AR"
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
  - transacoes
  - faturas
  - invoices
aliases:
  - RA_CUSTOMER_TRX_ALL
  - ra_customer_trx_all
  - cabecalho-transacoes-ar
  - invoices-header
  - faturas-ar
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# RA_CUSTOMER_TRX_ALL

## 📌 Visão Geral

Armazena o **cabeçalho de todas as transações** do módulo Accounts Receivable: faturas (invoices), notas de débito (debit memos), notas de crédito (credit memos) e duplicatas a receber (bills receivable). Cada registro representa uma transação completa com informações de cliente, tipo de transação, data, moeda, instruções de impressão e referências contábeis.

É a **tabela central do AR** — praticamente toda consulta ou relatório de contas a receber começa por ela.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Faturamento:** Registro de toda fatura emitida para clientes, com dados de cobrança, embarque e pagamento.
- **Notas de crédito/débito:** Ajustes comerciais vinculados a transações originais.
- **Duplicatas a receber (Bills Receivable):** Instrumentos de crédito sacados contra clientes.
- **Aging e cobrança:** Base para cálculo de saldos em aberto por faixa de vencimento.
- **Reconciliação contábil:** Ponto de partida para conciliação AR × GL via distribuições ([[ra_cust_trx_line_gl_dist_all]]).
- **Relatórios regulatórios:** Extração de transações para compliance fiscal e auditoria.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CUSTOMER_TRX_ID | NUMBER(18) | NOT NULL | PK | Identificador único da transação | — | 🟢 100% |
| 2 | TRX_NUMBER | VARCHAR2(30) | NOT NULL | Identificação | Número da transação visível ao usuário | — | 🟢 100% |
| 3 | OLD_TRX_NUMBER | VARCHAR2(30) | NULL | Identificação | Número anterior (se renumerada) | — | 🟡 70% |
| 4 | CUST_TRX_TYPE_ID | NUMBER(18) | NOT NULL | Classificação | Tipo da transação (invoice, credit memo, etc.) | [[ra_cust_trx_types_all]] | 🟢 100% |
| 5 | TRX_DATE | DATE | NOT NULL | Data | Data da transação | — | 🟢 100% |
| 6 | BATCH_SOURCE_ID | NUMBER(18) | NOT NULL | Classificação | Origem/fonte da transação | [[ra_batch_sources_all]] | 🟢 100% |
| 7 | BATCH_ID | NUMBER(18) | NULL | Classificação | Lote de entrada da transação | [[ra_batches_all]] | 🟢 100% |
| 8 | STATUS_TRX | VARCHAR2(30) | NULL | Classificação | Status da transação (OP=Open, CL=Closed, VD=Void) | — | 🟢 100% |
| 9 | COMPLETE_FLAG | VARCHAR2(1) | NULL | Classificação | Indica se a transação está completa (Y/N) | — | 🟢 100% |
| 10 | REASON_CODE | VARCHAR2(30) | NULL | Classificação | Código do motivo da transação | — | 🟢 100% |
| 11 | BILL_TO_CUSTOMER_ID | NUMBER(18) | NULL | Cliente | Conta do cliente de cobrança | [[hz_cust_accounts]] | 🟢 100% |
| 12 | BILL_TO_SITE_USE_ID | NUMBER(18) | NULL | Cliente | Site de cobrança do cliente | [[hz_cust_site_uses_all]] | 🟢 100% |
| 13 | BILL_TO_CONTACT_ID | NUMBER(18) | NULL | Cliente | Contato de cobrança | [[hz_cust_account_roles]] | 🟢 100% |
| 14 | SHIP_TO_CUSTOMER_ID | NUMBER(18) | NULL | Cliente | Conta do cliente de embarque | [[hz_cust_accounts]] | 🟢 100% |
| 15 | SHIP_TO_SITE_USE_ID | NUMBER(18) | NULL | Cliente | Site de embarque do cliente | [[hz_cust_site_uses_all]] | 🟢 100% |
| 16 | SHIP_TO_CONTACT_ID | NUMBER(18) | NULL | Cliente | Contato de embarque | [[hz_cust_account_roles]] | 🟢 100% |
| 17 | SOLD_TO_CUSTOMER_ID | NUMBER(18) | NULL | Cliente | Conta do cliente comprador (sold-to) | [[hz_cust_accounts]] | 🟢 100% |
| 18 | PAYING_CUSTOMER_ID | NUMBER(18) | NULL | Cliente | Conta do cliente pagador | [[hz_cust_accounts]] | 🟢 100% |
| 19 | PAYING_SITE_USE_ID | NUMBER(18) | NULL | Cliente | Site do cliente pagador | [[hz_cust_site_uses_all]] | 🟢 100% |
| 20 | DRAWEE_ID | NUMBER(18) | NULL | Cliente | Sacado (bills receivable) | [[hz_cust_accounts]] | 🟢 100% |
| 21 | DRAWEE_SITE_USE_ID | NUMBER(18) | NULL | Cliente | Site do sacado | [[hz_cust_site_uses_all]] | 🟢 100% |
| 22 | INVOICE_CURRENCY_CODE | VARCHAR2(15) | NOT NULL | Financeiro | Código da moeda da transação (ISO 4217) | — | 🟢 100% |
| 23 | EXCHANGE_RATE_TYPE | VARCHAR2(30) | NULL | Financeiro | Tipo de taxa de câmbio | [[gl_daily_conversion_types]] | 🟢 100% |
| 24 | EXCHANGE_RATE | NUMBER | NULL | Financeiro | Taxa de câmbio aplicada | — | 🟢 100% |
| 25 | EXCHANGE_DATE | DATE | NULL | Financeiro | Data da taxa de câmbio | — | 🟢 100% |
| 26 | TERM_ID | NUMBER(18) | NULL | Financeiro | Condição de pagamento | [[ra_terms_b]] | 🟢 100% |
| 27 | TERM_DUE_DATE | DATE | NULL | Financeiro | Data de vencimento calculada | — | 🟡 75% |
| 28 | FINANCE_CHARGES | VARCHAR2(1) | NULL | Financeiro | Sujeito a encargos financeiros (Y/N) | — | 🟡 75% |
| 29 | PRIMARY_SALESREP_ID | NUMBER(18) | NULL | Comercial | Vendedor principal | [[jtf_rs_salesreps]] | 🟢 100% |
| 30 | INVOICING_RULE_ID | NUMBER(18) | NULL | Contabilidade | Regra de faturamento (advance/arrears) | [[ra_rules]] | 🟢 100% |
| 31 | SET_OF_BOOKS_ID | NUMBER(18) | NULL | Contabilidade | Ledger contábil (legado — usar ORG_ID + LEGAL_ENTITY_ID) | [[gl_ledgers]] | 🟢 100% |
| 32 | RECEIPT_METHOD_ID | NUMBER(18) | NULL | Recebimento | Método de recebimento padrão | [[ar_receipt_methods]] | 🟢 100% |
| 33 | REMIT_TO_ADDRESS_ID | NUMBER(18) | NULL | Recebimento | Endereço remit-to | [[ra_remit_tos_all]] | 🟢 100% |
| 34 | DEFAULT_USSGL_TRX_CODE | VARCHAR2(30) | NULL | Contabilidade | Código de transação USSGL padrão | — | 🟡 65% |
| 35 | PREVIOUS_CUSTOMER_TRX_ID | NUMBER(18) | NULL | Referência cruzada | Transação original (credit memos vinculados) | self | 🟢 100% |
| 36 | RELATED_CUSTOMER_TRX_ID | NUMBER(18) | NULL | Referência cruzada | Transação relacionada (bills receivable) | self | 🟢 100% |
| 37 | DOC_SEQUENCE_ID | NUMBER(18) | NULL | Identificação | ID da sequência de documento | [[fnd_document_sequences]] | 🟢 100% |
| 38 | DOC_SEQUENCE_VALUE | NUMBER(15) | NULL | Identificação | Número de sequência de documento legal | [[fnd_document_sequences]] | 🟢 100% |
| 39 | CT_REFERENCE | VARCHAR2(150) | NULL | Identificação | Referência externa da transação | — | 🟡 70% |
| 40 | CUSTOMER_REFERENCE | VARCHAR2(100) | NULL | Referência externa | Referência do cliente (PO number, etc.) | — | 🟢 100% |
| 41 | CUSTOMER_REFERENCE_DATE | DATE | NULL | Referência externa | Data da referência do cliente | — | 🟢 100% |
| 42 | SHIP_DATE_ACTUAL | DATE | NULL | Logística | Data real de embarque | — | 🟢 100% |
| 43 | PRINTING_OPTION | VARCHAR2(30) | NULL | Impressão | Opção de impressão (PRI=Print, NOT=No Print) | — | 🟢 100% |
| 44 | PRINTING_COUNT | NUMBER | NULL | Impressão | Número de vezes impresso | — | 🟢 100% |
| 45 | PRINTING_ORIGINAL_DATE | DATE | NULL | Impressão | Data da primeira impressão | — | 🟢 100% |
| 46 | PRINTING_LAST_PRINTED | DATE | NULL | Impressão | Data da última impressão | — | 🟢 100% |
| 47 | COMMENTS | VARCHAR2(1760) | NULL | Texto livre | Comentários livres da transação | — | 🟢 100% |
| 48 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 49 | LEGAL_ENTITY_ID | NUMBER(18) | NULL | Multi-Org | Entidade legal | [[xle_entity_profiles]] | 🟢 100% |
| 50 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 51 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 52 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 53 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 54 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 55 | INTERFACE_HEADER_ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos flexíveis de interface (Descriptive Flexfield) | — | 🟢 100% |
| 56 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 100% |
| 57 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 100% |
| 58 | GLOBAL_ATTRIBUTE1–20 | VARCHAR2(150) | NULL | DFF | Atributos globais (localizações por país) | — | 🟢 100% |
| 59 | GLOBAL_ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Global Descriptive Flexfield | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ra_cust_trx_types_all]] — via `CUST_TRX_TYPE_ID` (tipo da transação)
- [[ra_batch_sources_all]] — via `BATCH_SOURCE_ID` (origem da transação)
- [[ra_batches_all]] — via `BATCH_ID` (lote de entrada)
- [[hz_cust_accounts]] — via `BILL_TO_CUSTOMER_ID`, `SHIP_TO_CUSTOMER_ID`, `SOLD_TO_CUSTOMER_ID`, `PAYING_CUSTOMER_ID`, `DRAWEE_ID` (cliente de cobrança (bill-to) da transação)
- [[hz_cust_site_uses_all]] — via `BILL_TO_SITE_USE_ID`, `SHIP_TO_SITE_USE_ID`, `PAYING_SITE_USE_ID`, `DRAWEE_SITE_USE_ID` (endereço de cobrança (bill-to) da transação)
- [[ra_terms_b]] — via `TERM_ID` (condição de pagamento)
- [[ra_rules]] — via `INVOICING_RULE_ID` (regra de faturamento)
- [[gl_ledgers]] — via `SET_OF_BOOKS_ID` (ledger contábil)
- [[gl_daily_conversion_types]] — via `EXCHANGE_RATE_TYPE` (tipo de câmbio da transação de cliente)
- [[ar_receipt_methods]] — via `RECEIPT_METHOD_ID` (método de recebimento da transação)
- [[jtf_rs_salesreps]] — via `PRIMARY_SALESREP_ID` (vendedor principal da transação de cliente)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit da transação de cliente)
- [[xle_entity_profiles]] — via `LEGAL_ENTITY_ID` (entidade legal da transação de cliente)

### Tabelas-filha (FK de saída)
- [[ra_customer_trx_lines_all]] — via `CUSTOMER_TRX_ID` (linhas da transação)
- [[ra_cust_trx_line_gl_dist_all]] — via `CUSTOMER_TRX_ID` (distribuições contábeis, indireta via lines)
- [[ra_cust_trx_line_salesreps_all]] — via `CUSTOMER_TRX_ID` (créditos de vendas)
- [[ar_payment_schedules_all]] — via `CUSTOMER_TRX_ID` (parcelas de pagamento)
- [[ar_receivable_applications_all]] — via `CUSTOMER_TRX_ID` (aplicações de recebimento)
- [[ar_adjustments_all]] — via `CUSTOMER_TRX_ID` (ajustes aplicados a esta transação de cliente)
- [[ar_transaction_history_all]] — via `CUSTOMER_TRX_ID` (histórico de status)
- [[zx_lines]] — via `TRX_ID` + `APPLICATION_ID` (linhas de imposto)

### Self-references
- `PREVIOUS_CUSTOMER_TRX_ID` — Transação original (para credit memos vinculados)
- `RELATED_CUSTOMER_TRX_ID` — Transação relacionada (bills receivable)

---

## 📎 Uso Típico

### Extração de todas as faturas abertas
```sql
SELECT ct.TRX_NUMBER, ct.TRX_DATE, ct.INVOICE_CURRENCY_CODE,
       ps.AMOUNT_DUE_REMAINING, ps.DUE_DATE
FROM   RA_CUSTOMER_TRX_ALL ct
JOIN   AR_PAYMENT_SCHEDULES_ALL ps ON ps.CUSTOMER_TRX_ID = ct.CUSTOMER_TRX_ID
WHERE  ps.STATUS = 'OP'
  AND  ct.ORG_ID = :p_org_id;
```

### Join com linhas e distribuições
```sql
SELECT ct.TRX_NUMBER, ctl.LINE_NUMBER, ctl.EXTENDED_AMOUNT,
       dist.CODE_COMBINATION_ID, dist.AMOUNT
FROM   RA_CUSTOMER_TRX_ALL ct
JOIN   RA_CUSTOMER_TRX_LINES_ALL ctl ON ctl.CUSTOMER_TRX_ID = ct.CUSTOMER_TRX_ID
JOIN   RA_CUST_TRX_LINE_GL_DIST_ALL dist ON dist.CUSTOMER_TRX_LINE_ID = ctl.CUSTOMER_TRX_LINE_ID
WHERE  ct.ORG_ID = :p_org_id;
```

### Filtros comuns
- `STATUS_TRX = 'OP'` — Transações abertas
- `COMPLETE_FLAG = 'Y'` — Apenas transações completas
- `CUST_TRX_TYPE_ID` — Filtrar por tipo (invoice, credit memo, etc.)
- `TRX_DATE BETWEEN :start AND :end` — Período

---

## 🔒 Observações

- A tabela possui **Descriptive Flexfields (DFF)** via colunas `ATTRIBUTE1–15` e `INTERFACE_HEADER_ATTRIBUTE1–15` — usados para customizações por implementação.
- O campo `SET_OF_BOOKS_ID` é legado; em implementações modernas do Fusion, usar `LEGAL_ENTITY_ID` + `ORG_ID` para contexto contábil.
- Transações do tipo **Bills Receivable** usam os campos `DRAWEE_*` em vez de `BILL_TO_*`.
- Campos `PREVIOUS_CUSTOMER_TRX_ID` e `RELATED_CUSTOMER_TRX_ID` criam uma **cadeia de transações** (fatura → credit memo → reissue).

---

## 📚 Referências

- [Oracle Docs — RA_CUSTOMER_TRX_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/racustomertrxall-25138.html)
- [[ar-module-data-dictionary]] — Dossiê do módulo AR
