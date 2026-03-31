---
id: DOC-OTHER-PVO-FaImpairmentsExtractPVO
doc_type: system-doc
title: "FaImpairmentsExtractPVO — PVO Cross-Module"
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
  - FaImpairmentsExtractPVO
  - faimpairmentsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FaImpairmentsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fa Impairments Extract. Acessa as tabelas: FA_IMPAIRMENTS.

**Caminho:** `FscmTopModelAM.FinExtractAM.FaBiccExtractAM.FaImpairmentsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 37 | 1 | 1 | 37 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fa_impairments|FA_IMPAIRMENTS]] — 37 atributos (1 PKs, 37 BICC)

---

## ⚙️ Atributos

### [[fa_impairments|FA_IMPAIRMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FaImpairmentsAssetId | ASSET_ID | — | ✅ |
| 2 | FaImpairmentsBookTypeCode | BOOK_TYPE_CODE | — | ✅ |
| 3 | FaImpairmentsCashGeneratingUnitId | CASH_GENERATING_UNIT_ID | — | ✅ |
| 4 | FaImpairmentsCreatedBy | CREATED_BY | — | ✅ |
| 5 | FaImpairmentsCreationDate | CREATION_DATE | — | ✅ |
| 6 | FaImpairmentsDateIneffective | DATE_INEFFECTIVE | — | ✅ |
| 7 | FaImpairmentsDescription | DESCRIPTION | — | ✅ |
| 8 | FaImpairmentsGoodwillAmount | GOODWILL_AMOUNT | — | ✅ |
| 9 | FaImpairmentsGoodwillAssetId | GOODWILL_ASSET_ID | — | ✅ |
| 10 | FaImpairmentsImpairClass | IMPAIR_CLASS | — | ✅ |
| 11 | FaImpairmentsImpairmentAmount | IMPAIRMENT_AMOUNT | — | ✅ |
| 12 | FaImpairmentsImpairmentDate | IMPAIRMENT_DATE | — | ✅ |
| 13 | FaImpairmentsImpairmentId | IMPAIRMENT_ID | 🔑 | ✅ |
| 14 | FaImpairmentsImpairmentName | IMPAIRMENT_NAME | — | ✅ |
| 15 | FaImpairmentsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | FaImpairmentsLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 17 | FaImpairmentsLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 18 | FaImpairmentsNetBookValue | NET_BOOK_VALUE | — | ✅ |
| 19 | FaImpairmentsNetSellingPrice | NET_SELLING_PRICE | — | ✅ |
| 20 | FaImpairmentsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 21 | FaImpairmentsPeriodCounterImpaired | PERIOD_COUNTER_IMPAIRED | — | ✅ |
| 22 | FaImpairmentsReason | REASON | — | ✅ |
| 23 | FaImpairmentsRequestId | REQUEST_ID | — | ✅ |
| 24 | FaImpairmentsReversalFlag | REVERSAL_FLAG | — | ✅ |
| 25 | FaImpairmentsSplit1ImpairClass | SPLIT1_IMPAIR_CLASS | — | ✅ |
| 26 | FaImpairmentsSplit1Percent | SPLIT1_PERCENT | — | ✅ |
| 27 | FaImpairmentsSplit1Reason | SPLIT1_REASON | — | ✅ |
| 28 | FaImpairmentsSplit2ImpairClass | SPLIT2_IMPAIR_CLASS | — | ✅ |
| 29 | FaImpairmentsSplit2Percent | SPLIT2_PERCENT | — | ✅ |
| 30 | FaImpairmentsSplit2Reason | SPLIT2_REASON | — | ✅ |
| 31 | FaImpairmentsSplit3ImpairClass | SPLIT3_IMPAIR_CLASS | — | ✅ |
| 32 | FaImpairmentsSplit3Percent | SPLIT3_PERCENT | — | ✅ |
| 33 | FaImpairmentsSplit3Reason | SPLIT3_REASON | — | ✅ |
| 34 | FaImpairmentsSplitImpairFlag | SPLIT_IMPAIR_FLAG | — | ✅ |
| 35 | FaImpairmentsStatus | STATUS | — | ✅ |
| 36 | FaImpairmentsUserDate | USER_DATE | — | ✅ |
| 37 | FaImpairmentsValueInUse | VALUE_IN_USE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
