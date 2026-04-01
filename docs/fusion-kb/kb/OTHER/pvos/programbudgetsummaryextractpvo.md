---
id: DOC-OTHER-PVO-ProgramBudgetSummaryExtractPVO
doc_type: system-doc
title: "ProgramBudgetSummaryExtractPVO — PVO Cross-Module"
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
  - ProgramBudgetSummaryExtractPVO
  - programbudgetsummaryextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProgramBudgetSummaryExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Program Budget Summary Extract. Acessa as tabelas: CJM_PROGRAM_BUDGET_SUMMARY.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CjmBiccExtractAM.ProgramBudgetSummaryExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 1 | 1 | 22 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cjm_program_budget_summary|CJM_PROGRAM_BUDGET_SUMMARY]] — 22 atributos (1 PKs, 22 BICC)

---

## ⚙️ Atributos

### [[cjm_program_budget_summary|CJM_PROGRAM_BUDGET_SUMMARY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BuId | BU_ID | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | EarnedAcctdAmt | EARNED_ACCTD_AMT | — | ✅ |
| 5 | InProgressAcctdAmt | IN_PROGRESS_ACCTD_AMT | — | ✅ |
| 6 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | PaidAcctdAmt | PAID_ACCTD_AMT | — | ✅ |
| 12 | ProgBudgetSumId | PROG_BUDGET_SUM_ID | 🔑 | ✅ |
| 13 | ProgramCurrencyCode | PROGRAM_CURRENCY_CODE | — | ✅ |
| 14 | ProgramEarnedAmt | PROGRAM_EARNED_AMT | — | ✅ |
| 15 | ProgramHeaderId | PROGRAM_HEADER_ID | — | ✅ |
| 16 | ProgramInProgressAmt | PROGRAM_IN_PROGRESS_AMT | — | ✅ |
| 17 | ProgramPaidAmt | PROGRAM_PAID_AMT | — | ✅ |
| 18 | ProgramUtilizedAmt | PROGRAM_UTILIZED_AMT | — | ✅ |
| 19 | RequestId | REQUEST_ID | — | ✅ |
| 20 | SourceTrxAmt | SOURCE_TRX_AMT | — | ✅ |
| 21 | UtilizedAcctdAmt | UTILIZED_ACCTD_AMT | — | ✅ |
| 22 | YearId | YEAR_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
