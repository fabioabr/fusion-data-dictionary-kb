---
id: DOC-AP-011
doc_type: system-doc
title: "AP_INVOICES_ALL — Faturas de Fornecedores (Invoices)"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - accounts-payable
  - data-dictionary
  - faturas
  - invoices
  - ap-invoices
aliases:
  - AP_INVOICES_ALL
  - ap_invoices_all
  - faturas-ap
  - invoices-ap
  - faturas-fornecedores
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AP_INVOICES_ALL

## 📌 Visão Geral

Armazena um registro para **cada fatura** (invoice) do módulo Accounts Payable. Cada linha representa uma fatura individual recebida de fornecedores, contendo número, valor, moeda, data, tipo (Standard, Credit Memo, Debit Memo, Prepayment, Mixed), status de validação e referência ao fornecedor emissor. É a tabela central do módulo AP e ponto de partida para todo o fluxo de contas a pagar — da entrada até o pagamento.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Registro de faturas:** Cada fatura de fornecedor gera um registro, seja entrada manual, importação via interface, OCR ou EDI.
- **Validação e aprovação:** Controle do status de validação (Validated, Needs Revalidation, Never Validated) e workflow de aprovação.
- **Contabilização:** Base para geração de lançamentos contábeis no General Ledger via Subledger Accounting.
- **Pagamentos:** Faturas validadas e aprovadas tornam-se elegíveis para seleção de pagamento.
- **Conciliação:** Vinculação de faturas a pedidos de compra (PO) e recebimentos para three-way matching.
- **Auditoria e compliance:** Rastreabilidade completa com sequência de documento, WHO columns e histórico de aprovação.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | INVOICE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da fatura | — | 🟢 100% |
| 2 | INVOICE_NUM | VARCHAR2(50) | NOT NULL | Identificação | Número da fatura do fornecedor | — | 🟢 100% |
| 3 | INVOICE_TYPE_LOOKUP_CODE | VARCHAR2(25) | NOT NULL | Classificação | Tipo da fatura (STANDARD/CREDIT/DEBIT/PREPAYMENT/MIXED) | [[ap_lookup_codes]] | 🟢 100% |
| 4 | INVOICE_DATE | DATE | NOT NULL | Data | Data da fatura | — | 🟢 100% |
| 5 | VENDOR_ID | NUMBER(18) | NOT NULL | Fornecedor | Identificador do fornecedor | [[poz_suppliers]] | 🟢 100% |
| 6 | VENDOR_SITE_ID | NUMBER(18) | NOT NULL | Fornecedor | Site do fornecedor | [[poz_supplier_sites_all_m]] | 🟢 100% |
| 7 | INVOICE_AMOUNT | NUMBER | NOT NULL | Financeiro | Valor total da fatura na moeda da transação | — | 🟢 100% |
| 8 | INVOICE_CURRENCY_CODE | VARCHAR2(15) | NOT NULL | Financeiro | Código da moeda da fatura (ISO 4217) | — | 🟢 100% |
| 9 | PAYMENT_CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Código da moeda de pagamento | — | 🟢 100% |
| 10 | EXCHANGE_RATE_TYPE | VARCHAR2(30) | NULL | Financeiro | Tipo de taxa de câmbio | [[gl_daily_conversion_types]] | 🟢 100% |
| 11 | EXCHANGE_RATE | NUMBER | NULL | Financeiro | Taxa de câmbio aplicada | — | 🟢 100% |
| 12 | EXCHANGE_DATE | DATE | NULL | Financeiro | Data da taxa de câmbio | — | 🟢 100% |
| 13 | TERMS_ID | NUMBER(18) | NULL | Condições | Condição de pagamento | [[ap_terms_b]] | 🟢 100% |
| 14 | TERMS_DATE | DATE | NULL | Condições | Data-base para cálculo de vencimento | — | 🟢 100% |
| 15 | DESCRIPTION | VARCHAR2(240) | NULL | Texto livre | Descrição da fatura | — | 🟢 100% |
| 16 | SOURCE | VARCHAR2(80) | NULL | Classificação | Origem da fatura (ex: Manual, ScanSnap, ERS) | — | 🟢 100% |
| 17 | PAYMENT_METHOD_CODE | VARCHAR2(30) | NULL | Pagamento | Método de pagamento (CHECK/EFT/WIRE) | [[iby_payment_methods_b]] | 🟢 100% |
| 18 | PAY_GROUP_LOOKUP_CODE | VARCHAR2(25) | NULL | Pagamento | Grupo de pagamento | [[ap_lookup_codes]] | 🟢 100% |
| 19 | GL_DATE | DATE | NULL | Contabilidade | Data contábil (General Ledger) | — | 🟢 100% |
| 20 | ACCTS_PAY_CODE_COMBINATION_ID | NUMBER(18) | NULL | Contabilidade | Conta contábil de AP (liability) | [[gl_code_combinations]] | 🟢 100% |
| 21 | PAYMENT_STATUS_FLAG | VARCHAR2(1) | NULL | Status | Status do pagamento (Y=pago/N=pendente/P=parcial) | — | 🟢 100% |
| 22 | APPROVAL_STATUS | VARCHAR2(25) | NULL | Status | Status de aprovação (APPROVED/REJECTED/INITIATED/etc.) | — | 🟢 100% |
| 23 | WFAPPROVAL_STATUS | VARCHAR2(50) | NULL | Status | Status do workflow de aprovação | — | 🟢 100% |
| 24 | CANCELLED_DATE | DATE | NULL | Status | Data de cancelamento da fatura | — | 🟢 100% |
| 25 | CANCELLED_BY | NUMBER(18) | NULL | Status | Usuário que cancelou | — | 🟢 100% |
| 26 | AMOUNT_PAID | NUMBER | NULL | Financeiro | Valor total já pago | — | 🟢 100% |
| 27 | DISCOUNT_AMOUNT_TAKEN | NUMBER | NULL | Financeiro | Desconto financeiro obtido | — | 🟢 100% |
| 28 | BASE_AMOUNT | NUMBER | NULL | Financeiro | Valor na moeda funcional (ledger) | — | 🟢 100% |
| 29 | DOC_SEQUENCE_ID | NUMBER(18) | NULL | Identificação | ID da sequência de documento | [[fnd_document_sequences]] | 🟢 100% |
| 30 | DOC_SEQUENCE_VALUE | NUMBER(15) | NULL | Identificação | Número de sequência de documento legal | — | 🟢 100% |
| 31 | PO_HEADER_ID | NUMBER(18) | NULL | Referência cruzada | Pedido de compra vinculado (quick match) | [[po_headers_all]] | 🟢 100% |
| 32 | PARTY_ID | NUMBER(18) | NULL | Fornecedor | Trading Community party do fornecedor | [[hz_parties]] | 🟢 100% |
| 33 | PARTY_SITE_ID | NUMBER(18) | NULL | Fornecedor | Party site do fornecedor | [[hz_party_sites]] | 🟢 100% |
| 34 | LEGAL_ENTITY_ID | NUMBER(18) | NULL | Multi-Org | Entidade legal | [[xle_entity_profiles]] | 🟢 100% |
| 35 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 36 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 37 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 38 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 39 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 40 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 41 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 100% |
| 42 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 100% |
| 43 | GLOBAL_ATTRIBUTE1–20 | VARCHAR2(150) | NULL | DFF | Atributos globais (localizações por país) | — | 🟢 100% |
| 44 | GLOBAL_ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Global Descriptive Flexfield | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_suppliers]] — via `VENDOR_ID` (fornecedor emissor da fatura)
- [[poz_supplier_sites_all_m]] — via `VENDOR_SITE_ID` (site do fornecedor)
- [[hz_parties]] — via `PARTY_ID` (trading community party)
- [[hz_party_sites]] — via `PARTY_SITE_ID` (endereço do fornecedor na fatura)
- [[ap_terms_b]] — via `TERMS_ID` (condição de pagamento)
- [[iby_payment_methods_b]] — via `PAYMENT_METHOD_CODE` (método de pagamento)
- [[gl_code_combinations]] — via `ACCTS_PAY_CODE_COMBINATION_ID` (conta contábil padrão de contas a pagar)
- [[gl_daily_conversion_types]] — via `EXCHANGE_RATE_TYPE` (tipo de câmbio usado na conversão da fatura)
- [[po_headers_all]] — via `PO_HEADER_ID` (pedido de compra)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit proprietária da fatura)
- [[xle_entity_profiles]] — via `LEGAL_ENTITY_ID` (entidade legal responsável pela fatura)

### Tabelas-filha (FK de saída)
- [[ap_invoice_lines_all]] — via `INVOICE_ID` (linhas da fatura)
- [[ap_invoice_distributions_all]] — via `INVOICE_ID` (distribuições contábeis)
- [[ap_invoice_payments_all]] — via `INVOICE_ID` (pagamentos da fatura)
- [[ap_payment_schedules_all]] — via `INVOICE_ID` (parcelas/vencimentos)
- [[ap_inv_aprvl_hist_all]] — via `INVOICE_ID` (histórico de aprovação)

---

## 📎 Uso Típico

### Listar faturas pendentes de pagamento
```sql
SELECT ai.INVOICE_NUM, ai.INVOICE_DATE, ai.INVOICE_AMOUNT,
       ai.INVOICE_CURRENCY_CODE, ai.PAYMENT_STATUS_FLAG
FROM   AP_INVOICES_ALL ai
WHERE  ai.PAYMENT_STATUS_FLAG = 'N'
  AND  ai.CANCELLED_DATE IS NULL
  AND  ai.ORG_ID = :p_org_id;
```

### Faturas com dados do fornecedor
```sql
SELECT ai.INVOICE_NUM, ai.INVOICE_AMOUNT, ai.INVOICE_DATE,
       ps.VENDOR_NAME, ps.SEGMENT1 AS vendor_number
FROM   AP_INVOICES_ALL ai
JOIN   POZ_SUPPLIERS ps ON ps.VENDOR_ID = ai.VENDOR_ID
WHERE  ai.INVOICE_DATE BETWEEN :start_date AND :end_date
  AND  ai.ORG_ID = :p_org_id;
```

### Filtros comuns
- `INVOICE_TYPE_LOOKUP_CODE = 'STANDARD'` — Faturas padrão
- `PAYMENT_STATUS_FLAG = 'N'` — Faturas não pagas
- `CANCELLED_DATE IS NULL` — Exclui canceladas
- `WFAPPROVAL_STATUS = 'WFAPPROVED'` — Aprovadas no workflow

---

## 🔒 Observações

- O campo `INVOICE_TYPE_LOOKUP_CODE` determina o tipo: **STANDARD** (fatura normal), **CREDIT** (nota de crédito), **DEBIT** (nota de débito), **PREPAYMENT** (adiantamento), **MIXED** (misto).
- O status de pagamento é controlado por `PAYMENT_STATUS_FLAG`: **Y** (totalmente pago), **N** (não pago), **P** (parcialmente pago).
- A validação da fatura é pré-requisito para pagamento; faturas inválidas não aparecem na seleção de pagamento.
- Campos `CANCELLED_*` são preenchidos apenas quando a fatura é cancelada; faturas canceladas não podem ser pagas.
- A tabela possui **Descriptive Flexfields (DFF)** via colunas `ATTRIBUTE1–15` para customizações por implementação.
- O campo `SOURCE` indica a origem da fatura e é importante para rastreabilidade de integrações.

---

## 📚 Referências

- [Oracle Docs — AP_INVOICES_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/apinvoicesall-25702.html)
- [[ap-module-data-dictionary]] — Dossiê do módulo AP
