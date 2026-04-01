---
id: DOC-OTHER-PVO-MiscellaneousReceiptDistributionExtractPVO
doc_type: system-doc
title: "MiscellaneousReceiptDistributionExtractPVO — PVO Cross-Module"
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
  - MiscellaneousReceiptDistributionExtractPVO
  - miscellaneousreceiptdistributionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MiscellaneousReceiptDistributionExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Miscellaneous Receipt Distribution Extract. Acessa as tabelas: AR_MISC_CASH_DISTRIBUTIONS_ALL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ArBiccExtractAM.MiscellaneousReceiptDistributionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 44 | 1 | 1 | 28 | 64% |

---

## 🔗 Tabelas Relacionadas

- [[ar_misc_cash_distributions_all|AR_MISC_CASH_DISTRIBUTIONS_ALL]] — 44 atributos (1 PKs, 28 BICC)

---

## ⚙️ Atributos

### [[ar_misc_cash_distributions_all|AR_MISC_CASH_DISTRIBUTIONS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ArMiscCashDistributionAcctdAmount | ACCTD_AMOUNT | — | ✅ |
| 2 | ArMiscCashDistributionAmount | AMOUNT | — | ✅ |
| 3 | ArMiscCashDistributionApplyDate | APPLY_DATE | — | ✅ |
| 4 | ArMiscCashDistributionAttribute1 | ATTRIBUTE1 | — | — |
| 5 | ArMiscCashDistributionAttribute10 | ATTRIBUTE10 | — | — |
| 6 | ArMiscCashDistributionAttribute11 | ATTRIBUTE11 | — | — |
| 7 | ArMiscCashDistributionAttribute12 | ATTRIBUTE12 | — | — |
| 8 | ArMiscCashDistributionAttribute13 | ATTRIBUTE13 | — | — |
| 9 | ArMiscCashDistributionAttribute14 | ATTRIBUTE14 | — | — |
| 10 | ArMiscCashDistributionAttribute15 | ATTRIBUTE15 | — | — |
| 11 | ArMiscCashDistributionAttribute2 | ATTRIBUTE2 | — | — |
| 12 | ArMiscCashDistributionAttribute3 | ATTRIBUTE3 | — | — |
| 13 | ArMiscCashDistributionAttribute4 | ATTRIBUTE4 | — | — |
| 14 | ArMiscCashDistributionAttribute5 | ATTRIBUTE5 | — | — |
| 15 | ArMiscCashDistributionAttribute6 | ATTRIBUTE6 | — | — |
| 16 | ArMiscCashDistributionAttribute7 | ATTRIBUTE7 | — | — |
| 17 | ArMiscCashDistributionAttribute8 | ATTRIBUTE8 | — | — |
| 18 | ArMiscCashDistributionAttribute9 | ATTRIBUTE9 | — | — |
| 19 | ArMiscCashDistributionAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 20 | ArMiscCashDistributionCashReceiptHistoryId | CASH_RECEIPT_HISTORY_ID | — | ✅ |
| 21 | ArMiscCashDistributionCashReceiptId | CASH_RECEIPT_ID | — | ✅ |
| 22 | ArMiscCashDistributionCodeCombinationId | CODE_COMBINATION_ID | — | ✅ |
| 23 | ArMiscCashDistributionComments | COMMENTS | — | ✅ |
| 24 | ArMiscCashDistributionCreatedBy | CREATED_BY | — | ✅ |
| 25 | ArMiscCashDistributionCreatedFrom | CREATED_FROM | — | ✅ |
| 26 | ArMiscCashDistributionCreationDate | CREATION_DATE | — | ✅ |
| 27 | ArMiscCashDistributionEventId | EVENT_ID | — | ✅ |
| 28 | ArMiscCashDistributionGlDate | GL_DATE | — | ✅ |
| 29 | ArMiscCashDistributionGlPostedDate | GL_POSTED_DATE | — | ✅ |
| 30 | ArMiscCashDistributionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 31 | ArMiscCashDistributionLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 32 | ArMiscCashDistributionLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 33 | ArMiscCashDistributionMiscCashDistributionId | MISC_CASH_DISTRIBUTION_ID | 🔑 | ✅ |
| 34 | ArMiscCashDistributionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 35 | ArMiscCashDistributionOrgId | ORG_ID | — | ✅ |
| 36 | ArMiscCashDistributionPercent | PERCENT | — | ✅ |
| 37 | ArMiscCashDistributionPostingControlId | POSTING_CONTROL_ID | — | ✅ |
| 38 | ArMiscCashDistributionProgramApplicationId | PROGRAM_APPLICATION_ID | — | ✅ |
| 39 | ArMiscCashDistributionProgramId | PROGRAM_ID | — | ✅ |
| 40 | ArMiscCashDistributionProgramUpdateDate | PROGRAM_UPDATE_DATE | — | ✅ |
| 41 | ArMiscCashDistributionRequestId | REQUEST_ID | — | ✅ |
| 42 | ArMiscCashDistributionReversalGlDate | REVERSAL_GL_DATE | — | ✅ |
| 43 | ArMiscCashDistributionSetOfBooksId | SET_OF_BOOKS_ID | — | ✅ |
| 44 | ArMiscCashDistributionUssglTransactionCodeContext | USSGL_TRANSACTION_CODE_CONTEXT | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
