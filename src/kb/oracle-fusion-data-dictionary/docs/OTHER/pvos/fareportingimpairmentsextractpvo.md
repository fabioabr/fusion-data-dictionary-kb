---
id: DOC-OTHER-PVO-FaReportingImpairmentsExtractPVO
doc_type: system-doc
title: "FaReportingImpairmentsExtractPVO — PVO Cross-Module"
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
  - FaReportingImpairmentsExtractPVO
  - fareportingimpairmentsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FaReportingImpairmentsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fa Reporting Impairments Extract. Acessa as tabelas: FA_MC_IMPAIRMENTS.

**Caminho:** `FscmTopModelAM.FinExtractAM.FaBiccExtractAM.FaReportingImpairmentsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 38 | 1 | 2 | 38 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fa_mc_impairments|FA_MC_IMPAIRMENTS]] — 38 atributos (2 PKs, 38 BICC)

---

## ⚙️ Atributos

### [[fa_mc_impairments|FA_MC_IMPAIRMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FaReportingImpairmentsAssetId | ASSET_ID | — | ✅ |
| 2 | FaReportingImpairmentsBookTypeCode | BOOK_TYPE_CODE | — | ✅ |
| 3 | FaReportingImpairmentsCashGeneratingUnitId | CASH_GENERATING_UNIT_ID | — | ✅ |
| 4 | FaReportingImpairmentsCreatedBy | CREATED_BY | — | ✅ |
| 5 | FaReportingImpairmentsCreationDate | CREATION_DATE | — | ✅ |
| 6 | FaReportingImpairmentsDateIneffective | DATE_INEFFECTIVE | — | ✅ |
| 7 | FaReportingImpairmentsDescription | DESCRIPTION | — | ✅ |
| 8 | FaReportingImpairmentsGoodwillAmount | GOODWILL_AMOUNT | — | ✅ |
| 9 | FaReportingImpairmentsGoodwillAssetId | GOODWILL_ASSET_ID | — | ✅ |
| 10 | FaReportingImpairmentsImpairClass | IMPAIR_CLASS | — | ✅ |
| 11 | FaReportingImpairmentsImpairmentAmount | IMPAIRMENT_AMOUNT | — | ✅ |
| 12 | FaReportingImpairmentsImpairmentDate | IMPAIRMENT_DATE | — | ✅ |
| 13 | FaReportingImpairmentsImpairmentId | IMPAIRMENT_ID | 🔑 | ✅ |
| 14 | FaReportingImpairmentsImpairmentName | IMPAIRMENT_NAME | — | ✅ |
| 15 | FaReportingImpairmentsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | FaReportingImpairmentsLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 17 | FaReportingImpairmentsLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 18 | FaReportingImpairmentsNetBookValue | NET_BOOK_VALUE | — | ✅ |
| 19 | FaReportingImpairmentsNetSellingPrice | NET_SELLING_PRICE | — | ✅ |
| 20 | FaReportingImpairmentsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 21 | FaReportingImpairmentsPeriodCounterImpaired | PERIOD_COUNTER_IMPAIRED | — | ✅ |
| 22 | FaReportingImpairmentsReason | REASON | — | ✅ |
| 23 | FaReportingImpairmentsRequestId | REQUEST_ID | — | ✅ |
| 24 | FaReportingImpairmentsReversalFlag | REVERSAL_FLAG | — | ✅ |
| 25 | FaReportingImpairmentsSetOfBooksId | SET_OF_BOOKS_ID | 🔑 | ✅ |
| 26 | FaReportingImpairmentsSplit1ImpairClass | SPLIT1_IMPAIR_CLASS | — | ✅ |
| 27 | FaReportingImpairmentsSplit1Percent | SPLIT1_PERCENT | — | ✅ |
| 28 | FaReportingImpairmentsSplit1Reason | SPLIT1_REASON | — | ✅ |
| 29 | FaReportingImpairmentsSplit2ImpairClass | SPLIT2_IMPAIR_CLASS | — | ✅ |
| 30 | FaReportingImpairmentsSplit2Percent | SPLIT2_PERCENT | — | ✅ |
| 31 | FaReportingImpairmentsSplit2Reason | SPLIT2_REASON | — | ✅ |
| 32 | FaReportingImpairmentsSplit3ImpairClass | SPLIT3_IMPAIR_CLASS | — | ✅ |
| 33 | FaReportingImpairmentsSplit3Percent | SPLIT3_PERCENT | — | ✅ |
| 34 | FaReportingImpairmentsSplit3Reason | SPLIT3_REASON | — | ✅ |
| 35 | FaReportingImpairmentsSplitImpairFlag | SPLIT_IMPAIR_FLAG | — | ✅ |
| 36 | FaReportingImpairmentsStatus | STATUS | — | ✅ |
| 37 | FaReportingImpairmentsUserDate | USER_DATE | — | ✅ |
| 38 | FaReportingImpairmentsValueInUse | VALUE_IN_USE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
