---
id: DOC-OTHER-PVO-ReportingBookControlExtractPVO
doc_type: system-doc
title: "ReportingBookControlExtractPVO — PVO Cross-Module"
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
  - ReportingBookControlExtractPVO
  - reportingbookcontrolextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReportingBookControlExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Reporting Book Control Extract. Acessa as tabelas: FA_MC_BOOK_CONTROLS.

**Caminho:** `FscmTopModelAM.FinExtractAM.FaBiccExtractAM.ReportingBookControlExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 1 | 2 | 21 | 95% |

---

## 🔗 Tabelas Relacionadas

- [[fa_mc_book_controls|FA_MC_BOOK_CONTROLS]] — 22 atributos (2 PKs, 21 BICC)

---

## ⚙️ Atributos

### [[fa_mc_book_controls|FA_MC_BOOK_CONTROLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReportingBookControlBookTypeCode | BOOK_TYPE_CODE | 🔑 | ✅ |
| 2 | ReportingBookControlConversionStatus | CONVERSION_STATUS | — | ✅ |
| 3 | ReportingBookControlCreatedBy | CREATED_BY | — | ✅ |
| 4 | ReportingBookControlCreationDate | CREATION_DATE | — | ✅ |
| 5 | ReportingBookControlCurrencyCode | CURRENCY_CODE | — | ✅ |
| 6 | ReportingBookControlCurrentFiscalYear | CURRENT_FISCAL_YEAR | — | ✅ |
| 7 | ReportingBookControlDeprnRequestId | DEPRN_REQUEST_ID | — | ✅ |
| 8 | ReportingBookControlDeprnStatus | DEPRN_STATUS | — | ✅ |
| 9 | ReportingBookControlEnabledFlag | ENABLED_FLAG | — | ✅ |
| 10 | ReportingBookControlGlPostingAllowedFlag | GL_POSTING_ALLOWED_FLAG | — | — |
| 11 | ReportingBookControlLastDeprnRunDate | LAST_DEPRN_RUN_DATE | — | ✅ |
| 12 | ReportingBookControlLastPeriodCounter | LAST_PERIOD_COUNTER | — | ✅ |
| 13 | ReportingBookControlLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | ReportingBookControlLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 15 | ReportingBookControlLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | ReportingBookControlMassRequestId | MASS_REQUEST_ID | — | ✅ |
| 17 | ReportingBookControlMrcConvertedFlag | MRC_CONVERTED_FLAG | — | ✅ |
| 18 | ReportingBookControlNbvAmountThreshold | NBV_AMOUNT_THRESHOLD | — | ✅ |
| 19 | ReportingBookControlObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 20 | ReportingBookControlPrimaryCurrencyCode | PRIMARY_CURRENCY_CODE | — | ✅ |
| 21 | ReportingBookControlPrimarySetOfBooksId | PRIMARY_SET_OF_BOOKS_ID | — | ✅ |
| 22 | ReportingBookControlSetOfBooksId | SET_OF_BOOKS_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
