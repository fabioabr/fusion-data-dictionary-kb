---
id: DOC-OTHER-PVO-BudgetAccountExtractPVO
doc_type: system-doc
title: "BudgetAccountExtractPVO — PVO Cross-Module"
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
  - BudgetAccountExtractPVO
  - budgetaccountextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BudgetAccountExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Budget Account Extract. Acessa as tabelas: XCC_BUDGET_ACCOUNTS.

**Caminho:** `FscmTopModelAM.FinExtractAM.XccBiccExtractAM.BudgetAccountExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 40 | 1 | 1 | 39 | 98% |

---

## 🔗 Tabelas Relacionadas

- [[xcc_budget_accounts|XCC_BUDGET_ACCOUNTS]] — 40 atributos (1 PKs, 39 BICC)

---

## ⚙️ Atributos

### [[xcc_budget_accounts|XCC_BUDGET_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BudgetChartOfAccountsId | BUDGET_CHART_OF_ACCOUNTS_ID | — | ✅ |
| 2 | BudgetCodeCombinationId | BUDGET_CODE_COMBINATION_ID | 🔑 | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | EnabledFlag | ENABLED_FLAG | — | — |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | SegmentValue1 | SEGMENT_VALUE1 | — | ✅ |
| 11 | SegmentValue10 | SEGMENT_VALUE10 | — | ✅ |
| 12 | SegmentValue11 | SEGMENT_VALUE11 | — | ✅ |
| 13 | SegmentValue12 | SEGMENT_VALUE12 | — | ✅ |
| 14 | SegmentValue13 | SEGMENT_VALUE13 | — | ✅ |
| 15 | SegmentValue14 | SEGMENT_VALUE14 | — | ✅ |
| 16 | SegmentValue15 | SEGMENT_VALUE15 | — | ✅ |
| 17 | SegmentValue16 | SEGMENT_VALUE16 | — | ✅ |
| 18 | SegmentValue17 | SEGMENT_VALUE17 | — | ✅ |
| 19 | SegmentValue18 | SEGMENT_VALUE18 | — | ✅ |
| 20 | SegmentValue19 | SEGMENT_VALUE19 | — | ✅ |
| 21 | SegmentValue2 | SEGMENT_VALUE2 | — | ✅ |
| 22 | SegmentValue20 | SEGMENT_VALUE20 | — | ✅ |
| 23 | SegmentValue21 | SEGMENT_VALUE21 | — | ✅ |
| 24 | SegmentValue22 | SEGMENT_VALUE22 | — | ✅ |
| 25 | SegmentValue23 | SEGMENT_VALUE23 | — | ✅ |
| 26 | SegmentValue24 | SEGMENT_VALUE24 | — | ✅ |
| 27 | SegmentValue25 | SEGMENT_VALUE25 | — | ✅ |
| 28 | SegmentValue26 | SEGMENT_VALUE26 | — | ✅ |
| 29 | SegmentValue27 | SEGMENT_VALUE27 | — | ✅ |
| 30 | SegmentValue28 | SEGMENT_VALUE28 | — | ✅ |
| 31 | SegmentValue29 | SEGMENT_VALUE29 | — | ✅ |
| 32 | SegmentValue3 | SEGMENT_VALUE3 | — | ✅ |
| 33 | SegmentValue30 | SEGMENT_VALUE30 | — | ✅ |
| 34 | SegmentValue4 | SEGMENT_VALUE4 | — | ✅ |
| 35 | SegmentValue5 | SEGMENT_VALUE5 | — | ✅ |
| 36 | SegmentValue6 | SEGMENT_VALUE6 | — | ✅ |
| 37 | SegmentValue7 | SEGMENT_VALUE7 | — | ✅ |
| 38 | SegmentValue8 | SEGMENT_VALUE8 | — | ✅ |
| 39 | SegmentValue9 | SEGMENT_VALUE9 | — | ✅ |
| 40 | SummaryFlag | SUMMARY_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
