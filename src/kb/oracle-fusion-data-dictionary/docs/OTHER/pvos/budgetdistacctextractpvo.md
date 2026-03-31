---
id: DOC-OTHER-PVO-BudgetDistAcctExtractPVO
doc_type: system-doc
title: "BudgetDistAcctExtractPVO — PVO Cross-Module"
system: Oracle Fusion Cloud ERP
module: Cross-Module
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - other
  - data-dictionary
  - pvo
  - bicc
aliases:
  - BudgetDistAcctExtractPVO
  - budgetdistacctextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BudgetDistAcctExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Budget Dist Acct Extract. Acessa as tabelas: XCC_BUDGET_DIST_ACCTS.

**Caminho:** `FscmTopModelAM.FinExtractAM.XccBiccExtractAM.BudgetDistAcctExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 18 | 1 | 7 | 18 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[xcc_budget_dist_accts|XCC_BUDGET_DIST_ACCTS]] — 18 atributos (7 PKs, 18 BICC)

---

## ⚙️ Atributos

### [[xcc_budget_dist_accts|XCC_BUDGET_DIST_ACCTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Amount | AMOUNT | — | ✅ |
| 2 | BudgetAction | BUDGET_ACTION | 🔑 | ✅ |
| 3 | BudgetCcid | BUDGET_CCID | 🔑 | ✅ |
| 4 | ControlBudgetId | CONTROL_BUDGET_ID | 🔑 | ✅ |
| 5 | CreatedBy | CREATED_BY | — | ✅ |
| 6 | CreationDate | CREATION_DATE | — | ✅ |
| 7 | DataSetId | DATA_SET_ID | — | ✅ |
| 8 | FundsReleasedDate | FUNDS_RELEASED_DATE | — | ✅ |
| 9 | HeaderId | HEADER_ID | 🔑 | ✅ |
| 10 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | LineNumber | LINE_NUMBER | 🔑 | ✅ |
| 14 | MasterPeriodName | MASTER_PERIOD_NAME | 🔑 | ✅ |
| 15 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 16 | OriginalAmount | ORIGINAL_AMOUNT | — | ✅ |
| 17 | PeriodName | PERIOD_NAME | 🔑 | ✅ |
| 18 | ProcessedForEssbaseFlag | PROCESSED_FOR_ESSBASE_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
