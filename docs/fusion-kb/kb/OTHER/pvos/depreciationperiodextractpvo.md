---
id: DOC-OTHER-PVO-DepreciationPeriodExtractPVO
doc_type: system-doc
title: "DepreciationPeriodExtractPVO — PVO Cross-Module"
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
  - DepreciationPeriodExtractPVO
  - depreciationperiodextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DepreciationPeriodExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Depreciation Period Extract. Acessa as tabelas: FA_DEPRN_PERIODS.

**Caminho:** `FscmTopModelAM.FinExtractAM.FaBiccExtractAM.DepreciationPeriodExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 1 | 2 | 16 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fa_deprn_periods|FA_DEPRN_PERIODS]] — 16 atributos (2 PKs, 16 BICC)

---

## ⚙️ Atributos

### [[fa_deprn_periods|FA_DEPRN_PERIODS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DepreciationPeriodBookTypeCode | BOOK_TYPE_CODE | 🔑 | ✅ |
| 2 | DepreciationPeriodCalendarPeriodCloseDate | CALENDAR_PERIOD_CLOSE_DATE | — | ✅ |
| 3 | DepreciationPeriodCalendarPeriodOpenDate | CALENDAR_PERIOD_OPEN_DATE | — | ✅ |
| 4 | DepreciationPeriodCreatedBy | CREATED_BY | — | ✅ |
| 5 | DepreciationPeriodCreationDate | CREATION_DATE | — | ✅ |
| 6 | DepreciationPeriodDeprnRun | DEPRN_RUN | — | ✅ |
| 7 | DepreciationPeriodFiscalYear | FISCAL_YEAR | — | ✅ |
| 8 | DepreciationPeriodLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | DepreciationPeriodLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | DepreciationPeriodLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | DepreciationPeriodObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | DepreciationPeriodPeriodCloseDate | PERIOD_CLOSE_DATE | — | ✅ |
| 13 | DepreciationPeriodPeriodCounter | PERIOD_COUNTER | 🔑 | ✅ |
| 14 | DepreciationPeriodPeriodName | PERIOD_NAME | — | ✅ |
| 15 | DepreciationPeriodPeriodNum | PERIOD_NUM | — | ✅ |
| 16 | DepreciationPeriodPeriodOpenDate | PERIOD_OPEN_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
