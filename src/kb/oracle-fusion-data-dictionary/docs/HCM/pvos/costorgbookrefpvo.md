---
id: DOC-HCM-PVO-CostOrgBookRefPVO
doc_type: system-doc
title: "CostOrgBookRefPVO — PVO Human Capital Management"
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
  - CostOrgBookRefPVO
  - costorgbookrefpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CostOrgBookRefPVO

## 📌 Visão Geral

Versao de referencia dos livros de custo por organizacao. Utilizado em lookups de configuracao contabil de custos de pessoal.

**Caminho:** `FscmTopModelAM.CostOrganizationAM.CostOrgBookRefPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 49 | 5 | 2 | 22 | 45% |

---

## 🔗 Tabelas Relacionadas

- [[cst_cost_books_b|CST_COST_BOOKS_B]] — 9 atributos (3 BICC)
- [[cst_cost_books_tl|CST_COST_BOOKS_TL]] — 10 atributos
- [[cst_cost_orgs_v|CST_COST_ORGS_V]] — 5 atributos (3 BICC)
- [[cst_cost_org_books|CST_COST_ORG_BOOKS]] — 22 atributos (2 PKs, 15 BICC)
- [[gl_ledgers|GL_LEDGERS]] — 3 atributos (1 BICC)

---

## ⚙️ Atributos

### [[cst_cost_books_b|CST_COST_BOOKS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostBookBPEOCostBookCode | COST_BOOK_CODE | — | ✅ |
| 2 | CostBookBPEOCostBookId1 | COST_BOOK_ID | — | ✅ |
| 3 | CostBookBPEOCreatedBy1 | CREATED_BY | — | — |
| 4 | CostBookBPEOCreationDate1 | CREATION_DATE | — | — |
| 5 | CostBookBPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 6 | CostBookBPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 7 | CostBookBPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 8 | CostBookBPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 9 | CostBookBPEOPeriodicAverageFlag | PERIODIC_AVERAGE_FLAG | — | — |

### [[cst_cost_books_tl|CST_COST_BOOKS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostBookTLPEOCostBookDesc | COST_BOOK_DESC | — | — |
| 2 | CostBookTLPEOCostBookId2 | COST_BOOK_ID | — | — |
| 3 | CostBookTLPEOCreatedBy2 | CREATED_BY | — | — |
| 4 | CostBookTLPEOCreationDate2 | CREATION_DATE | — | — |
| 5 | CostBookTLPEOLanguage | LANGUAGE | — | — |
| 6 | CostBookTLPEOLastUpdateDate2 | LAST_UPDATE_DATE | — | — |
| 7 | CostBookTLPEOLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 8 | CostBookTLPEOLastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 9 | CostBookTLPEOObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 10 | CostBookTLPEOSourceLang | SOURCE_LANG | — | — |

### [[cst_cost_orgs_v|CST_COST_ORGS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostOrganizationVPEOCostOrgId1 | COST_ORG_ID | — | — |
| 2 | CostOrganizationVPEOCostOrgName | COST_ORG_NAME | — | ✅ |
| 3 | CostOrganizationVPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 4 | CostOrganizationVPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 5 | CostOrganizationVPEOLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |

### [[cst_cost_org_books|CST_COST_ORG_BOOKS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostBookId | COST_BOOK_ID | 🔑 | ✅ |
| 2 | CostOrgBookPEOCalendarId | CALENDAR_ID | — | — |
| 3 | CostOrgBookPEOCdConversionType | CD_CONVERSION_TYPE | — | ✅ |
| 4 | CostOrgBookPEOConversionType | CONVERSION_TYPE | — | — |
| 5 | CostOrgBookPEOCreateAccountingFlag | CREATE_ACCOUNTING_FLAG | — | ✅ |
| 6 | CostOrgBookPEOCreatedBy | CREATED_BY | — | ✅ |
| 7 | CostOrgBookPEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | CostOrgBookPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 9 | CostOrgBookPEOFirstLedgerPeriodName | FIRST_LEDGER_PERIOD_NAME | — | — |
| 10 | CostOrgBookPEOFromDate | FROM_DATE | — | ✅ |
| 11 | CostOrgBookPEOInactiveDate | INACTIVE_DATE | — | ✅ |
| 12 | CostOrgBookPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | CostOrgBookPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | CostOrgBookPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | CostOrgBookPEOLedgerId | LEDGER_ID | — | ✅ |
| 16 | CostOrgBookPEOMaintainTransactionsFlag | MAINTAIN_TRANSACTIONS_FLAG | — | — |
| 17 | CostOrgBookPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | CostOrgBookPEOOpenPeriodsNum | OPEN_PERIODS_NUM | — | — |
| 19 | CostOrgBookPEOPrimaryBookFlag | PRIMARY_BOOK_FLAG | — | ✅ |
| 20 | CostOrgBookPEOToDate | TO_DATE | — | ✅ |
| 21 | CostOrgBookPEOUsdConversionType | USD_CONVERSION_TYPE | — | ✅ |
| 22 | CostOrgId | COST_ORG_ID | 🔑 | ✅ |

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlLedgersPEOLedgerId | LEDGER_ID | — | — |
| 2 | GlLedgersPEOName | NAME | — | ✅ |
| 3 | GlLedgersPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
