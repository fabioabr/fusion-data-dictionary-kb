---
id: DOC-OTHER-PVO-FiscalYearExtractPVO
doc_type: system-doc
title: "FiscalYearExtractPVO — PVO Cross-Module"
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
  - FiscalYearExtractPVO
  - fiscalyearextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FiscalYearExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fiscal Year Extract. Acessa as tabelas: FA_FISCAL_YEAR.

**Caminho:** `FscmTopModelAM.FinExtractAM.FaBiccExtractAM.FiscalYearExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 27 | 1 | 2 | 11 | 41% |

---

## 🔗 Tabelas Relacionadas

- [[fa_fiscal_year|FA_FISCAL_YEAR]] — 27 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[fa_fiscal_year|FA_FISCAL_YEAR]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalYearAttribute1 | ATTRIBUTE1 | — | — |
| 2 | FiscalYearAttribute10 | ATTRIBUTE10 | — | — |
| 3 | FiscalYearAttribute11 | ATTRIBUTE11 | — | — |
| 4 | FiscalYearAttribute12 | ATTRIBUTE12 | — | — |
| 5 | FiscalYearAttribute13 | ATTRIBUTE13 | — | — |
| 6 | FiscalYearAttribute14 | ATTRIBUTE14 | — | — |
| 7 | FiscalYearAttribute15 | ATTRIBUTE15 | — | — |
| 8 | FiscalYearAttribute2 | ATTRIBUTE2 | — | — |
| 9 | FiscalYearAttribute3 | ATTRIBUTE3 | — | — |
| 10 | FiscalYearAttribute4 | ATTRIBUTE4 | — | — |
| 11 | FiscalYearAttribute5 | ATTRIBUTE5 | — | — |
| 12 | FiscalYearAttribute6 | ATTRIBUTE6 | — | — |
| 13 | FiscalYearAttribute7 | ATTRIBUTE7 | — | — |
| 14 | FiscalYearAttribute8 | ATTRIBUTE8 | — | — |
| 15 | FiscalYearAttribute9 | ATTRIBUTE9 | — | — |
| 16 | FiscalYearAttributeCategoryCode | ATTRIBUTE_CATEGORY_CODE | — | — |
| 17 | FiscalYearCreatedBy | CREATED_BY | — | ✅ |
| 18 | FiscalYearCreationDate | CREATION_DATE | — | ✅ |
| 19 | FiscalYearEndDate | END_DATE | — | ✅ |
| 20 | FiscalYearFiscalYear1 | FISCAL_YEAR | — | ✅ |
| 21 | FiscalYearFiscalYearName | FISCAL_YEAR_NAME | 🔑 | ✅ |
| 22 | FiscalYearLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 23 | FiscalYearLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 24 | FiscalYearLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 25 | FiscalYearMidYearDate | MID_YEAR_DATE | — | ✅ |
| 26 | FiscalYearObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 27 | FiscalYearStartDate | START_DATE | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
