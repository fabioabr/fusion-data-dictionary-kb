---
id: DOC-OTHER-PVO-BalanceExtractPVO
doc_type: system-doc
title: "BalanceExtractPVO — PVO Cross-Module"
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
  - BalanceExtractPVO
  - balanceextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BalanceExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Balance Extract. Acessa as tabelas: XCC_BALANCES.

**Caminho:** `FscmTopModelAM.FinExtractAM.XccBiccExtractAM.BalanceExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 24 | 1 | 3 | 24 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[xcc_balances|XCC_BALANCES]] — 24 atributos (3 PKs, 24 BICC)

---

## ⚙️ Atributos

### [[xcc_balances|XCC_BALANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccountedPayablesAmount | ACCOUNTED_PAYABLES_AMOUNT | — | ✅ |
| 2 | AccountedProjectAmount | ACCOUNTED_PROJECT_AMOUNT | — | ✅ |
| 3 | AccountedReceiptsAmount | ACCOUNTED_RECEIPTS_AMOUNT | — | ✅ |
| 4 | ActualAmount | ACTUAL_AMOUNT | — | ✅ |
| 5 | ApprovedAuthorizationAmount | APPROVED_AUTHORIZATION_AMOUNT | — | ✅ |
| 6 | ApprovedCommitmentAmount | APPROVED_COMMITMENT_AMOUNT | — | ✅ |
| 7 | ApprovedObligationAmount | APPROVED_OBLIGATION_AMOUNT | — | ✅ |
| 8 | BudgetAdjustmentAmount | BUDGET_ADJUSTMENT_AMOUNT | — | ✅ |
| 9 | BudgetAmount | BUDGET_AMOUNT | — | ✅ |
| 10 | BudgetCcid | BUDGET_CCID | 🔑 | ✅ |
| 11 | CommitmentAmount | COMMITMENT_AMOUNT | — | ✅ |
| 12 | ControlBudgetId | CONTROL_BUDGET_ID | 🔑 | ✅ |
| 13 | CreatedBy | CREATED_BY | — | ✅ |
| 14 | CreationDate | CREATION_DATE | — | ✅ |
| 15 | DetailOtherAmount | DETAIL_OTHER_AMOUNT | — | ✅ |
| 16 | FundsAvailableAmount | FUNDS_AVAILABLE_AMOUNT | — | ✅ |
| 17 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 18 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 19 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 20 | MiscExpendituresAmount | MISC_EXPENDITURES_AMOUNT | — | ✅ |
| 21 | ObligationAmount | OBLIGATION_AMOUNT | — | ✅ |
| 22 | OtherAmount | OTHER_AMOUNT | — | ✅ |
| 23 | PeriodName | PERIOD_NAME | 🔑 | ✅ |
| 24 | UnreleasedBudgetAmount | UNRELEASED_BUDGET_AMOUNT | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
