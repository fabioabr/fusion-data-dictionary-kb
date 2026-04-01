---
id: DOC-OTHER-PVO-BudgetBalanceExtractPVO
doc_type: system-doc
title: "BudgetBalanceExtractPVO — PVO Cross-Module"
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
  - BudgetBalanceExtractPVO
  - budgetbalanceextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BudgetBalanceExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Budget Balance Extract. Acessa as tabelas: GL_BUDGET_BALANCES.

**Caminho:** `FscmTopModelAM.FinExtractAM.GlBiccExtractAM.BudgetBalanceExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 44 | 1 | 6 | 43 | 98% |

---

## 🔗 Tabelas Relacionadas

- [[gl_budget_balances|GL_BUDGET_BALANCES]] — 44 atributos (6 PKs, 43 BICC)

---

## ⚙️ Atributos

### [[gl_budget_balances|GL_BUDGET_BALANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BudgetName | BUDGET_NAME | 🔑 | ✅ |
| 2 | ConcatAccount | CONCAT_ACCOUNT | 🔑 | — |
| 3 | CurrencyCode | CURRENCY_CODE | 🔑 | ✅ |
| 4 | CurrencyType | CURRENCY_TYPE | 🔑 | ✅ |
| 5 | GlBudBalCreatedBy | CREATED_BY | — | ✅ |
| 6 | GlBudBalCreationDate | CREATION_DATE | — | ✅ |
| 7 | GlBudBalLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | GlBudBalLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | GlBudBalLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | GlBudBalObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | GlBudBalPeriodNetCr | PERIOD_NET_CR | — | ✅ |
| 12 | GlBudBalPeriodNetDr | PERIOD_NET_DR | — | ✅ |
| 13 | GlBudBalSegment1 | SEGMENT1 | — | ✅ |
| 14 | GlBudBalSegment10 | SEGMENT10 | — | ✅ |
| 15 | GlBudBalSegment11 | SEGMENT11 | — | ✅ |
| 16 | GlBudBalSegment12 | SEGMENT12 | — | ✅ |
| 17 | GlBudBalSegment13 | SEGMENT13 | — | ✅ |
| 18 | GlBudBalSegment14 | SEGMENT14 | — | ✅ |
| 19 | GlBudBalSegment15 | SEGMENT15 | — | ✅ |
| 20 | GlBudBalSegment16 | SEGMENT16 | — | ✅ |
| 21 | GlBudBalSegment17 | SEGMENT17 | — | ✅ |
| 22 | GlBudBalSegment18 | SEGMENT18 | — | ✅ |
| 23 | GlBudBalSegment19 | SEGMENT19 | — | ✅ |
| 24 | GlBudBalSegment2 | SEGMENT2 | — | ✅ |
| 25 | GlBudBalSegment20 | SEGMENT20 | — | ✅ |
| 26 | GlBudBalSegment21 | SEGMENT21 | — | ✅ |
| 27 | GlBudBalSegment22 | SEGMENT22 | — | ✅ |
| 28 | GlBudBalSegment23 | SEGMENT23 | — | ✅ |
| 29 | GlBudBalSegment24 | SEGMENT24 | — | ✅ |
| 30 | GlBudBalSegment25 | SEGMENT25 | — | ✅ |
| 31 | GlBudBalSegment26 | SEGMENT26 | — | ✅ |
| 32 | GlBudBalSegment27 | SEGMENT27 | — | ✅ |
| 33 | GlBudBalSegment28 | SEGMENT28 | — | ✅ |
| 34 | GlBudBalSegment29 | SEGMENT29 | — | ✅ |
| 35 | GlBudBalSegment3 | SEGMENT3 | — | ✅ |
| 36 | GlBudBalSegment30 | SEGMENT30 | — | ✅ |
| 37 | GlBudBalSegment4 | SEGMENT4 | — | ✅ |
| 38 | GlBudBalSegment5 | SEGMENT5 | — | ✅ |
| 39 | GlBudBalSegment6 | SEGMENT6 | — | ✅ |
| 40 | GlBudBalSegment7 | SEGMENT7 | — | ✅ |
| 41 | GlBudBalSegment8 | SEGMENT8 | — | ✅ |
| 42 | GlBudBalSegment9 | SEGMENT9 | — | ✅ |
| 43 | LedgerId | LEDGER_ID | 🔑 | ✅ |
| 44 | PeriodName | PERIOD_NAME | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
