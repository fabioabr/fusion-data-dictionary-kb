---
id: DOC-OTHER-PVO-CostOrgBooksExtractPVO
doc_type: system-doc
title: "CostOrgBooksExtractPVO — PVO Cross-Module"
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
  - CostOrgBooksExtractPVO
  - costorgbooksextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CostOrgBooksExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cost Org Books Extract. Acessa as tabelas: CST_COST_ORG_BOOKS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CostOrgBooksExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 62 | 1 | 2 | 21 | 34% |

---

## 🔗 Tabelas Relacionadas

- [[cst_cost_org_books|CST_COST_ORG_BOOKS]] — 62 atributos (2 PKs, 21 BICC)

---

## ⚙️ Atributos

### [[cst_cost_org_books|CST_COST_ORG_BOOKS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostOrgBookPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 2 | CostOrgBookPEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 3 | CostOrgBookPEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 4 | CostOrgBookPEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 5 | CostOrgBookPEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 6 | CostOrgBookPEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 7 | CostOrgBookPEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 8 | CostOrgBookPEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 9 | CostOrgBookPEOAttributeChar16 | ATTRIBUTE_CHAR16 | — | — |
| 10 | CostOrgBookPEOAttributeChar17 | ATTRIBUTE_CHAR17 | — | — |
| 11 | CostOrgBookPEOAttributeChar18 | ATTRIBUTE_CHAR18 | — | — |
| 12 | CostOrgBookPEOAttributeChar19 | ATTRIBUTE_CHAR19 | — | — |
| 13 | CostOrgBookPEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 14 | CostOrgBookPEOAttributeChar20 | ATTRIBUTE_CHAR20 | — | — |
| 15 | CostOrgBookPEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 16 | CostOrgBookPEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 17 | CostOrgBookPEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 18 | CostOrgBookPEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 19 | CostOrgBookPEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 20 | CostOrgBookPEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 21 | CostOrgBookPEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 22 | CostOrgBookPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 23 | CostOrgBookPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 24 | CostOrgBookPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 25 | CostOrgBookPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 26 | CostOrgBookPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 27 | CostOrgBookPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 28 | CostOrgBookPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 29 | CostOrgBookPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 30 | CostOrgBookPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 31 | CostOrgBookPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 32 | CostOrgBookPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 33 | CostOrgBookPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 34 | CostOrgBookPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 35 | CostOrgBookPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 36 | CostOrgBookPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 37 | CostOrgBookPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 38 | CostOrgBookPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 39 | CostOrgBookPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 40 | CostOrgBookPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 41 | CostOrgBookPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 42 | CostOrgBookPEOCalendarId | CALENDAR_ID | — | ✅ |
| 43 | CostOrgBookPEOCdConversionType | CD_CONVERSION_TYPE | — | ✅ |
| 44 | CostOrgBookPEOConversionType | CONVERSION_TYPE | — | ✅ |
| 45 | CostOrgBookPEOCostBookId | COST_BOOK_ID | 🔑 | ✅ |
| 46 | CostOrgBookPEOCostOrgId | COST_ORG_ID | 🔑 | ✅ |
| 47 | CostOrgBookPEOCreateAccountingFlag | CREATE_ACCOUNTING_FLAG | — | ✅ |
| 48 | CostOrgBookPEOCreatedBy | CREATED_BY | — | ✅ |
| 49 | CostOrgBookPEOCreationDate | CREATION_DATE | — | ✅ |
| 50 | CostOrgBookPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 51 | CostOrgBookPEOFirstLedgerPeriodName | FIRST_LEDGER_PERIOD_NAME | — | ✅ |
| 52 | CostOrgBookPEOFromDate | FROM_DATE | — | ✅ |
| 53 | CostOrgBookPEOInactiveDate | INACTIVE_DATE | — | ✅ |
| 54 | CostOrgBookPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 55 | CostOrgBookPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 56 | CostOrgBookPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 57 | CostOrgBookPEOLedgerId | LEDGER_ID | — | ✅ |
| 58 | CostOrgBookPEOMaintainTransactionsFlag | MAINTAIN_TRANSACTIONS_FLAG | — | ✅ |
| 59 | CostOrgBookPEOOpenPeriodsNum | OPEN_PERIODS_NUM | — | ✅ |
| 60 | CostOrgBookPEOPrimaryBookFlag | PRIMARY_BOOK_FLAG | — | ✅ |
| 61 | CostOrgBookPEOToDate | TO_DATE | — | ✅ |
| 62 | CostOrgBookPEOUsdConversionType | USD_CONVERSION_TYPE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
