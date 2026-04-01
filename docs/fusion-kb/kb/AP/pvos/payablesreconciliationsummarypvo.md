---
id: DOC-AP-PVO-PayablesReconciliationSummaryPVO
doc_type: system-doc
title: "PayablesReconciliationSummaryPVO — PVO Accounts Payable"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ap
  - data-dictionary
  - pvo
  - bicc
aliases:
  - PayablesReconciliationSummaryPVO
  - payablesreconciliationsummarypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PayablesReconciliationSummaryPVO

## 📌 Visão Geral

Extrai o resumo consolidado das reconciliações de contas a pagar por ledger, incluindo totais de débito, crédito e diferenças. Fundamental para fechamento contábil, identificação de divergências e validação de saldos de fornecedores.

**Caminho:** `FscmTopModelAM.FinApReportsReconciliationAM.PayablesReconciliationSummaryPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 2 | 1 | 8 | 36% |

---

## 🔗 Tabelas Relacionadas

- [[ap_recon_summary_details|AP_RECON_SUMMARY_DETAILS]] — 20 atributos (1 PKs, 8 BICC)
- [[gl_ledgers|GL_LEDGERS]] — 2 atributos

---

## ⚙️ Atributos

### [[ap_recon_summary_details|AP_RECON_SUMMARY_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReconItemId | RECON_ITEM_ID | 🔑 | ✅ |
| 2 | ReconciliationSummaryPEOAccountedCr | ACCOUNTED_CR | — | ✅ |
| 3 | ReconciliationSummaryPEOAccountedDr | ACCOUNTED_DR | — | ✅ |
| 4 | ReconciliationSummaryPEOApAcctdAmount | AP_ACCTD_AMOUNT | — | ✅ |
| 5 | ReconciliationSummaryPEOBalancingSegment | BALANCING_SEGMENT | — | — |
| 6 | ReconciliationSummaryPEOBuId | BU_ID | — | — |
| 7 | ReconciliationSummaryPEOCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 8 | ReconciliationSummaryPEOCreatedBy | CREATED_BY | — | — |
| 9 | ReconciliationSummaryPEOCreationDate | CREATION_DATE | — | — |
| 10 | ReconciliationSummaryPEODataSource | DATA_SOURCE | — | ✅ |
| 11 | ReconciliationSummaryPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 12 | ReconciliationSummaryPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 13 | ReconciliationSummaryPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | ReconciliationSummaryPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | ReconciliationSummaryPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 16 | ReconciliationSummaryPEOLedgerId | LEDGER_ID | — | — |
| 17 | ReconciliationSummaryPEONaturalAccountSegment | NATURAL_ACCOUNT_SEGMENT | — | — |
| 18 | ReconciliationSummaryPEOReconItemCode | RECON_ITEM_CODE | — | ✅ |
| 19 | ReconciliationSummaryPEOReconItemOrder | RECON_ITEM_ORDER | — | ✅ |
| 20 | ReconciliationSummaryPEORequestId | REQUEST_ID | — | — |

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LedgersChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 2 | LedgersLedgerId | LEDGER_ID | — | — |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
