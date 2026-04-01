---
id: DOC-HCM-PVO-CostOrgBookPVO
doc_type: system-doc
title: "CostOrgBookPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - CostOrgBookPVO
  - costorgbookpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CostOrgBookPVO

## 📌 Visão Geral

Relaciona livros de custo a organizacoes de custo com codigo e configuracoes. Suporta setup de contabilizacao de custos de workforce.

**Caminho:** `FscmTopModelAM.CostOrganizationAM.CostOrgBookPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 51 | 5 | 2 | 22 | 43% |

---

## 🔗 Tabelas Relacionadas

- [[cst_cost_books_b|CST_COST_BOOKS_B]] — 10 atributos (3 BICC)
- [[cst_cost_books_tl|CST_COST_BOOKS_TL]] — 10 atributos
- [[cst_cost_orgs_v|CST_COST_ORGS_V]] — 5 atributos (3 BICC)
- [[cst_cost_org_books|CST_COST_ORG_BOOKS]] — 23 atributos (2 PKs, 15 BICC)
- [[gl_ledgers|GL_LEDGERS]] — 3 atributos (1 BICC)

---

## ⚙️ Atributos

### [[cst_cost_books_b|CST_COST_BOOKS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostBookBPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 2 | CostBookBPEOCostBookCode | COST_BOOK_CODE | — | ✅ |
| 3 | CostBookBPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 4 | CostBookBPEOCreatedBy | CREATED_BY | — | — |
| 5 | CostBookBPEOCreationDate | CREATION_DATE | — | — |
| 6 | CostBookBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | CostBookBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | CostBookBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | CostBookBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | CostBookBPEOPeriodicAverageFlag | PERIODIC_AVERAGE_FLAG | — | — |

### [[cst_cost_books_tl|CST_COST_BOOKS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostBookTLPEOCostBookDesc | COST_BOOK_DESC | — | — |
| 2 | CostBookTLPEOCostBookId | COST_BOOK_ID | — | — |
| 3 | CostBookTLPEOCreatedBy | CREATED_BY | — | — |
| 4 | CostBookTLPEOCreationDate | CREATION_DATE | — | — |
| 5 | CostBookTLPEOLanguage | LANGUAGE | — | — |
| 6 | CostBookTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | CostBookTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | CostBookTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | CostBookTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | CostBookTLPEOSourceLang | SOURCE_LANG | — | — |

### [[cst_cost_orgs_v|CST_COST_ORGS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostOrganizationVPEOCostOrgId | COST_ORG_ID | — | — |
| 2 | CostOrganizationVPEOCostOrgName | COST_ORG_NAME | — | ✅ |
| 3 | CostOrganizationVPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 4 | CostOrganizationVPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 5 | CostOrganizationVPEOLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |

### [[cst_cost_org_books|CST_COST_ORG_BOOKS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostBookId | COST_BOOK_ID | 🔑 | ✅ |
| 2 | CostOrgBookPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 3 | CostOrgBookPEOCalendarId | CALENDAR_ID | — | — |
| 4 | CostOrgBookPEOCdConversionType | CD_CONVERSION_TYPE | — | ✅ |
| 5 | CostOrgBookPEOConversionType | CONVERSION_TYPE | — | — |
| 6 | CostOrgBookPEOCreateAccountingFlag | CREATE_ACCOUNTING_FLAG | — | ✅ |
| 7 | CostOrgBookPEOCreatedBy | CREATED_BY | — | ✅ |
| 8 | CostOrgBookPEOCreationDate | CREATION_DATE | — | ✅ |
| 9 | CostOrgBookPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 10 | CostOrgBookPEOFirstLedgerPeriodName | FIRST_LEDGER_PERIOD_NAME | — | — |
| 11 | CostOrgBookPEOFromDate | FROM_DATE | — | ✅ |
| 12 | CostOrgBookPEOInactiveDate | INACTIVE_DATE | — | ✅ |
| 13 | CostOrgBookPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | CostOrgBookPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | CostOrgBookPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | CostOrgBookPEOLedgerId | LEDGER_ID | — | ✅ |
| 17 | CostOrgBookPEOMaintainTransactionsFlag | MAINTAIN_TRANSACTIONS_FLAG | — | — |
| 18 | CostOrgBookPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 19 | CostOrgBookPEOOpenPeriodsNum | OPEN_PERIODS_NUM | — | — |
| 20 | CostOrgBookPEOPrimaryBookFlag | PRIMARY_BOOK_FLAG | — | ✅ |
| 21 | CostOrgBookPEOToDate | TO_DATE | — | ✅ |
| 22 | CostOrgBookPEOUsdConversionType | USD_CONVERSION_TYPE | — | ✅ |
| 23 | CostOrgId | COST_ORG_ID | 🔑 | ✅ |

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlLedgersPEOLedgerId | LEDGER_ID | — | — |
| 2 | GlLedgersPEOName | NAME | — | ✅ |
| 3 | GlLedgersPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
