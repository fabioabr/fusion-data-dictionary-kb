---
id: DOC-OTHER-PVO-CmrExpenseClrAmtsExtractPVO
doc_type: system-doc
title: "CmrExpenseClrAmtsExtractPVO — PVO Cross-Module"
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
  - CmrExpenseClrAmtsExtractPVO
  - cmrexpenseclramtsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CmrExpenseClrAmtsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cmr Expense Clr Amts Extract. Acessa as tabelas: CMR_EXPENSE_CLR_AMTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CmrBiccExtractAM.CmrExpenseClrAmtsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 1 | 15 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cmr_expense_clr_amts|CMR_EXPENSE_CLR_AMTS]] — 15 atributos (1 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[cmr_expense_clr_amts|CMR_EXPENSE_CLR_AMTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CmrExpenseClrAmtsPEOAccrualClrGroupId | ACCRUAL_CLR_GROUP_ID | — | ✅ |
| 2 | CmrExpenseClrAmtsPEOApInvoiceDistributionType | AP_INVOICE_DISTRIBUTION_TYPE | — | ✅ |
| 3 | CmrExpenseClrAmtsPEOCmrExpenseClrAmtsId | CMR_EXPENSE_CLR_AMTS_ID | 🔑 | ✅ |
| 4 | CmrExpenseClrAmtsPEOCmrPoDistributionId | CMR_PO_DISTRIBUTION_ID | — | ✅ |
| 5 | CmrExpenseClrAmtsPEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | CmrExpenseClrAmtsPEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | CmrExpenseClrAmtsPEOExpPoDistCostId | EXP_PO_DIST_COST_ID | — | ✅ |
| 8 | CmrExpenseClrAmtsPEOInclusiveFlag | INCLUSIVE_FLAG | — | ✅ |
| 9 | CmrExpenseClrAmtsPEOInvoiceAmt | INVOICE_AMT | — | ✅ |
| 10 | CmrExpenseClrAmtsPEOInvoiceAmtEnteredCurr | INVOICE_AMT_ENTERED_CURR | — | ✅ |
| 11 | CmrExpenseClrAmtsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | CmrExpenseClrAmtsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | CmrExpenseClrAmtsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | CmrExpenseClrAmtsPEONetExpAdjAmtRounded | NET_EXP_ADJ_AMT_ROUNDED | — | ✅ |
| 15 | CmrExpenseClrAmtsPEONetExpAdjAmtRoundedEc | NET_EXP_ADJ_AMT_ROUNDED_EC | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
