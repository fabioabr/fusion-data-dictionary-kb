---
id: DOC-AR-000
doc_type: system-doc
title: "Accounts Receivable (AR) — Dossiê do Módulo"
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
  - modulo-ar
  - contas-a-receber
  - financeiro
aliases:
  - AR
  - accounts-receivable
  - contas-a-receber
  - receivables
  - modulo-ar
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# Accounts Receivable (AR) — Dossiê do Módulo

## 📌 Visão Geral

O módulo **Accounts Receivable (AR)** do Oracle Fusion Cloud Financials é responsável por todo o ciclo de vida das contas a receber da organização. Abrange desde a criação de faturas (invoices), notas de débito e crédito, até o recebimento de pagamentos, aplicação de créditos, aging de saldos, cobranças e reconciliação contábil.

No contexto do Banco Patria, o AR é um dos módulos financeiros core do Oracle Fusion, processando transações de clientes e integrando-se com General Ledger ([[gl_ledgers]]), Tax ([[zx_lines]]), Payments ([[iby_ext_bank_accounts]]) e Trading Community Architecture ([[hz_parties]]).

> [!note] Fonte de dados
> As tabelas documentadas neste dossiê foram extraídas do **BICC Database Mapping (Release 13/25A)** — documentação oficial Oracle Fusion Cloud ERP.

---

## 🧠 Processos de Negócio Suportados

### Faturamento (Billing)
Criação e gestão de transações de clientes: faturas, notas de débito, notas de crédito e duplicatas a receber. Inclui agrupamento por lotes, regras de receita e atribuição de vendedores.

### Recebimentos (Cash Receipts)
Registro e aplicação de pagamentos recebidos de clientes. Suporta recebimentos manuais, automáticos (lockbox), miscelâneos e remessas eletrônicas.

### Ajustes e Distribuições
Ajustes de valores em transações existentes — write-offs, ajustes de receita, reclassificações contábeis e distribuições para o General Ledger.

### Aging e Cobranças
Classificação de saldos em aberto por faixa de vencimento (aging buckets), atribuição de cobradores, rastreamento de disputas e ciclos de extrato.

### Juros e Encargos
Cálculo e aplicação de juros sobre saldos em atraso, com schedules configuráveis por cliente/perfil.

### Reconciliação
Conciliação entre saldos do AR e lançamentos no General Ledger, com detalhamento de diferenças.

---

## ⚙️ Inventário de Tabelas — Core AR (52 tabelas)

### 1. Transações — Invoices, Memos e Linhas (16 tabelas `RA_`)

| # | Tabela | Descrição |
|---|--------|-----------|
| 001 | [[ra_customer_trx_all]] | Cabeçalho de faturas, notas de débito/crédito e duplicatas |
| 002 | [[ra_customer_trx_lines_all]] | Linhas de detalhe das transações |
| 003 | [[ra_cust_trx_line_gl_dist_all]] | Distribuições contábeis das linhas |
| 004 | [[ra_cust_trx_line_salesreps_all]] | Atribuição de vendedores às linhas |
| 005 | [[ra_cust_trx_types_all]] | Tipos de transação (invoice, credit memo, etc.) |
| 006 | [[ra_batches_all]] | Lotes de transações |
| 007 | [[ra_batch_sources_all]] | Origens/fontes de transações |
| 008 | [[ra_cm_requests_all]] | Solicitações de notas de crédito |
| 009 | [[ra_cust_receipt_methods]] | Métodos de recebimento por cliente |
| 010 | [[ra_remit_tos_all]] | Endereços de remessa (remit-to) |
| 011 | [[ra_grouping_rules]] | Regras de agrupamento de transações |
| 012 | [[ra_rules]] | Regras de reconhecimento de receita |
| 013 | [[ra_terms_b]] | Condições de pagamento (base) |
| 014 | [[ra_terms_lines]] | Linhas das condições de pagamento |
| 015 | [[ra_terms_tl]] | Condições de pagamento (traduções) |
| 016 | [[ra_terms_vl]] | Condições de pagamento (view consolidada) |

### 2. Recebimentos — Receipts (8 tabelas `AR_`)

| # | Tabela | Descrição |
|---|--------|-----------|
| 017 | [[ar_cash_receipts_all]] | Recebimentos de caixa (cash receipts) |
| 018 | [[ar_cash_receipt_history_all]] | Histórico de status dos recebimentos |
| 019 | [[ar_cash_remit_refs_all]] | Referências de remessa dos recebimentos |
| 020 | [[ar_receivable_applications_all]] | Aplicações de recebimentos a transações |
| 021 | [[ar_payment_schedules_all]] | Parcelas/schedule de pagamento das transações |
| 022 | [[ar_misc_cash_distributions_all]] | Distribuições de recebimentos miscelâneos |
| 023 | [[ar_batches_all]] | Lotes de recebimentos |
| 024 | [[ar_transmissions_all]] | Transmissões de remessas/lockbox |

### 3. Ajustes e Distribuições (6 tabelas)

| # | Tabela | Descrição |
|---|--------|-----------|
| 025 | [[ar_adjustments_all]] | Ajustes em transações AR |
| 026 | [[ar_revenue_adjustments_all]] | Ajustes de reconhecimento de receita |
| 027 | [[ar_rate_adjustments_all]] | Ajustes de taxa de câmbio |
| 028 | [[ar_distributions_all]] | Distribuições contábeis do AR |
| 029 | [[ar_distribution_sets_all]] | Conjuntos de distribuição predefinidos |
| 030 | [[ar_detailed_distributions_all]] | Distribuições detalhadas (subledger) |

### 4. Aging, Cobranças e Disputas (6 tabelas)

| # | Tabela | Descrição |
|---|--------|-----------|
| 031 | [[ar_aging_buckets]] | Definição de faixas de aging |
| 032 | [[ar_aging_bucket_lines_b]] | Linhas das faixas de aging (base) |
| 033 | [[ar_aging_bucket_lines_tl]] | Linhas das faixas de aging (traduções) |
| 034 | [[ar_collectors]] | Cadastro de cobradores |
| 035 | [[ar_dispute_history]] | Histórico de disputas de clientes |
| 036 | [[ar_statement_cycles]] | Ciclos de geração de extratos |

### 5. Juros, Diferimentos e Consolidado (7 tabelas)

| # | Tabela | Descrição |
|---|--------|-----------|
| 037 | [[ar_interest_headers_all]] | Cabeçalho de cálculo de juros |
| 038 | [[ar_interest_lines_all]] | Linhas de detalhe dos juros |
| 039 | [[ar_charge_schedules]] | Schedules de encargos |
| 040 | [[ar_charge_schedule_hdrs]] | Cabeçalhos dos schedules de encargos |
| 041 | [[ar_charge_schedule_lines]] | Linhas dos schedules de encargos |
| 042 | [[ar_cons_inv_all]] | Faturas consolidadas (consolidated billing) |
| 043 | [[ar_deferred_lines_all]] | Linhas de receita diferida |

### 6. Configuração e Parâmetros (16 tabelas)

| # | Tabela | Descrição |
|---|--------|-----------|
| 044 | [[ar_system_parameters_all]] | Parâmetros do sistema AR por org |
| 045 | [[ar_receivables_trx_all]] | Tipos de atividade de recebíveis |
| 046 | [[ar_receipt_classes]] | Classes de recebimento |
| 047 | [[ar_receipt_methods]] | Métodos de recebimento |
| 048 | [[ar_receipt_method_accounts_all]] | Contas contábeis dos métodos de recebimento |
| 049 | [[ar_autocash_hierarchies]] | Hierarquias de aplicação automática |
| 050 | [[ar_automatch_rules]] | Regras de matching automático |
| 051 | [[ar_app_rule_sets]] | Conjuntos de regras de aplicação |
| 052 | [[ar_app_exception_rules]] | Regras de exceção de aplicação |
| 053 | [[ar_approval_action_history]] | Histórico de ações de aprovação |
| 054 | [[ar_memo_lines_all_b]] | Linhas de memo (base) |
| 055 | [[ar_memo_lines_all_tl]] | Linhas de memo (traduções) |
| 056 | [[ar_lookups]] | Valores de lookup do AR |
| 057 | [[ar_sales_credit_types]] | Tipos de crédito de vendas |
| 058 | [[ar_standard_text_b]] | Textos padrão (base) |
| 059 | [[ar_standard_text_tl]] | Textos padrão (traduções) |

### 7. Reconciliação, Histórico e Referências (6 tabelas)

| # | Tabela | Descrição |
|---|--------|-----------|
| 060 | [[ar_recon_summary_details]] | Resumo da reconciliação AR×GL |
| 061 | [[ar_recon_difference_details]] | Detalhes das diferenças de reconciliação |
| 062 | [[ar_recon_summary_parameters]] | Parâmetros de execução da reconciliação |
| 063 | [[ar_transaction_history_all]] | Histórico completo de transações AR |
| 064 | [[ar_ref_accounts_all]] | Contas de referência por atividade |
| 065 | [[ar_remit_to_locs_all]] | Locais de remessa (endereços remit-to) |

> [!note] Numeração
> A numeração DOC-AR-NNN pode não ser estritamente sequencial (001–065) pois inclui a contagem final após inventário detalhado. Algumas tabelas como `AR_TRANSMISSION_FORMATS` são de configuração e foram agrupadas no grupo 6.

---

## 🔗 Integrações com Outros Módulos

### Trading Community Architecture (TCA) — `HZ_`
17 tabelas de cadastro de clientes, contatos, endereços, perfis e relacionamentos. O AR depende fortemente do TCA para identificação de clientes em todas as transações.
- Tabelas-chave: [[hz_parties]], [[hz_cust_accounts]], [[hz_cust_acct_sites_all]], [[hz_cust_site_uses_all]], [[hz_locations]], [[hz_customer_profiles_f]]

### Payments (IBY) — `IBY_`
9 tabelas de instrumentos de pagamento, autorizações de débito e contas bancárias externas.
- Tabelas-chave: [[iby_ext_bank_accounts]], [[iby_pmt_instr_uses_all]], [[iby_fndcpt_tx_extensions]]

### Tax (ZX) — `ZX_`
17 tabelas de regimes fiscais, jurisdições, taxas, registros e códigos de reporte tributário.
- Tabelas-chave: [[zx_lines]], [[zx_regimes_vl]], [[zx_registrations]], [[zx_party_tax_profile]]

### General Ledger (GL) — `GL_`
3 tabelas de combinações de contas, ledgers e taxas de conversão.
- Tabelas-chave: [[gl_code_combinations]], [[gl_ledgers]], [[gl_daily_conversion_types]]

### Cash Management (CE) — `CE_`
3 tabelas de contas bancárias internas e agências.
- Tabelas-chave: [[ce_bank_acct_uses_all]], [[ce_internal_bank_accts_v]], [[ce_bank_branches_v]]

### Items & Inventory (EGP/INV) — `EGP_`, `INV_`
6 tabelas de itens, categorias e unidades de medida.
- Tabelas-chave: [[egp_system_items_vl]], [[egp_categories_vl]], [[inv_org_parameters]]

### Human Resources (HR) — `HR_`
4 tabelas de unidades organizacionais e business units.
- Tabelas-chave: [[hr_all_organization_units_f]], [[hr_organization_information_f]]

### Subledger Accounting (XLA/XLE) — `XLA_`, `XLE_`
2 tabelas de eventos contábeis e entidades legais.
- Tabelas-chave: [[xla_events]], [[xle_entity_profiles]]

### Foundation (FND/FUN/PER) — `FND_`, `FUN_`, `PER_`
5 tabelas de infraestrutura — sequências de documentos, territórios, usuários.
- Tabelas-chave: [[fnd_document_sequences]], [[fnd_territories_vl]], [[per_users]]

### Sales (JTF) — `JTF_`
1 tabela de representantes de vendas.
- Tabela: [[jtf_rs_salesreps]]

---

## 📎 Referências

- [Oracle Fusion Cloud Financials — Receivables Tables (OEDMF)](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/receivables-tables.html)
- [Oracle Fusion Cloud — BICC Database Mapping Release 13/25A](https://docs.oracle.com/en/cloud/saas/financials/25a/)
- [RA_CUSTOMER_TRX_ALL — Table Reference](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/racustomertrxall-25138.html)
- [AR_CASH_RECEIPTS_ALL — Table Reference](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/arcashreceiptsall-10584.html)
- [AR_PAYMENT_SCHEDULES_ALL — Table Reference](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/arpaymentschedulesall-11453.html)
- [AR_RECEIVABLE_APPLICATIONS_ALL — Table Reference](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/arreceivableapplicationsall-10850.html)
- [AR_ADJUSTMENTS_ALL — Table Reference](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/aradjustmentsall-10533.html)
