---
id: DOC-OTHER-PVO-DailyBalanceExtractPVO
doc_type: system-doc
title: "DailyBalanceExtractPVO — PVO Cross-Module"
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
  - DailyBalanceExtractPVO
  - dailybalanceextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DailyBalanceExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Daily Balance Extract. Acessa as tabelas: GL_DAILY_BALANCES.

**Caminho:** `FscmTopModelAM.FinExtractAM.GlBiccExtractAM.DailyBalanceExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 57 | 1 | 7 | 57 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gl_daily_balances|GL_DAILY_BALANCES]] — 57 atributos (7 PKs, 57 BICC)

---

## ⚙️ Atributos

### [[gl_daily_balances|GL_DAILY_BALANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlDailyBalancesActualFlag | ACTUAL_FLAG | 🔑 | ✅ |
| 2 | GlDailyBalancesCodeCombinationId | CODE_COMBINATION_ID | 🔑 | ✅ |
| 3 | GlDailyBalancesConvertedFromCurrency | CONVERTED_FROM_CURRENCY | 🔑 | ✅ |
| 4 | GlDailyBalancesCreatedBy | CREATED_BY | — | ✅ |
| 5 | GlDailyBalancesCreationDate | CREATION_DATE | — | ✅ |
| 6 | GlDailyBalancesCurrencyCode | CURRENCY_CODE | 🔑 | ✅ |
| 7 | GlDailyBalancesCurrencyType | CURRENCY_TYPE | 🔑 | ✅ |
| 8 | GlDailyBalancesLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | GlDailyBalancesLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | GlDailyBalancesLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | GlDailyBalancesLedgerId | LEDGER_ID | 🔑 | ✅ |
| 12 | GlDailyBalancesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | GlDailyBalancesOpeningPeriodAggregate | OPENING_PERIOD_AGGREGATE | — | ✅ |
| 14 | GlDailyBalancesOpeningQuarterAggregate | OPENING_QUARTER_AGGREGATE | — | ✅ |
| 15 | GlDailyBalancesOpeningYearAggregate | OPENING_YEAR_AGGREGATE | — | ✅ |
| 16 | GlDailyBalancesPeriodAggregate1 | PERIOD_AGGREGATE1 | — | ✅ |
| 17 | GlDailyBalancesPeriodAggregate10 | PERIOD_AGGREGATE10 | — | ✅ |
| 18 | GlDailyBalancesPeriodAggregate11 | PERIOD_AGGREGATE11 | — | ✅ |
| 19 | GlDailyBalancesPeriodAggregate12 | PERIOD_AGGREGATE12 | — | ✅ |
| 20 | GlDailyBalancesPeriodAggregate13 | PERIOD_AGGREGATE13 | — | ✅ |
| 21 | GlDailyBalancesPeriodAggregate14 | PERIOD_AGGREGATE14 | — | ✅ |
| 22 | GlDailyBalancesPeriodAggregate15 | PERIOD_AGGREGATE15 | — | ✅ |
| 23 | GlDailyBalancesPeriodAggregate16 | PERIOD_AGGREGATE16 | — | ✅ |
| 24 | GlDailyBalancesPeriodAggregate17 | PERIOD_AGGREGATE17 | — | ✅ |
| 25 | GlDailyBalancesPeriodAggregate18 | PERIOD_AGGREGATE18 | — | ✅ |
| 26 | GlDailyBalancesPeriodAggregate19 | PERIOD_AGGREGATE19 | — | ✅ |
| 27 | GlDailyBalancesPeriodAggregate2 | PERIOD_AGGREGATE2 | — | ✅ |
| 28 | GlDailyBalancesPeriodAggregate20 | PERIOD_AGGREGATE20 | — | ✅ |
| 29 | GlDailyBalancesPeriodAggregate21 | PERIOD_AGGREGATE21 | — | ✅ |
| 30 | GlDailyBalancesPeriodAggregate22 | PERIOD_AGGREGATE22 | — | ✅ |
| 31 | GlDailyBalancesPeriodAggregate23 | PERIOD_AGGREGATE23 | — | ✅ |
| 32 | GlDailyBalancesPeriodAggregate24 | PERIOD_AGGREGATE24 | — | ✅ |
| 33 | GlDailyBalancesPeriodAggregate25 | PERIOD_AGGREGATE25 | — | ✅ |
| 34 | GlDailyBalancesPeriodAggregate26 | PERIOD_AGGREGATE26 | — | ✅ |
| 35 | GlDailyBalancesPeriodAggregate27 | PERIOD_AGGREGATE27 | — | ✅ |
| 36 | GlDailyBalancesPeriodAggregate28 | PERIOD_AGGREGATE28 | — | ✅ |
| 37 | GlDailyBalancesPeriodAggregate29 | PERIOD_AGGREGATE29 | — | ✅ |
| 38 | GlDailyBalancesPeriodAggregate3 | PERIOD_AGGREGATE3 | — | ✅ |
| 39 | GlDailyBalancesPeriodAggregate30 | PERIOD_AGGREGATE30 | — | ✅ |
| 40 | GlDailyBalancesPeriodAggregate31 | PERIOD_AGGREGATE31 | — | ✅ |
| 41 | GlDailyBalancesPeriodAggregate32 | PERIOD_AGGREGATE32 | — | ✅ |
| 42 | GlDailyBalancesPeriodAggregate33 | PERIOD_AGGREGATE33 | — | ✅ |
| 43 | GlDailyBalancesPeriodAggregate34 | PERIOD_AGGREGATE34 | — | ✅ |
| 44 | GlDailyBalancesPeriodAggregate35 | PERIOD_AGGREGATE35 | — | ✅ |
| 45 | GlDailyBalancesPeriodAggregate4 | PERIOD_AGGREGATE4 | — | ✅ |
| 46 | GlDailyBalancesPeriodAggregate5 | PERIOD_AGGREGATE5 | — | ✅ |
| 47 | GlDailyBalancesPeriodAggregate6 | PERIOD_AGGREGATE6 | — | ✅ |
| 48 | GlDailyBalancesPeriodAggregate7 | PERIOD_AGGREGATE7 | — | ✅ |
| 49 | GlDailyBalancesPeriodAggregate8 | PERIOD_AGGREGATE8 | — | ✅ |
| 50 | GlDailyBalancesPeriodAggregate9 | PERIOD_AGGREGATE9 | — | ✅ |
| 51 | GlDailyBalancesPeriodEndDate | PERIOD_END_DATE | — | ✅ |
| 52 | GlDailyBalancesPeriodName | PERIOD_NAME | 🔑 | ✅ |
| 53 | GlDailyBalancesPeriodNum | PERIOD_NUM | — | ✅ |
| 54 | GlDailyBalancesPeriodStartDate | PERIOD_START_DATE | — | ✅ |
| 55 | GlDailyBalancesPeriodYear | PERIOD_YEAR | — | ✅ |
| 56 | GlDailyBalancesQuarterStartDate | QUARTER_START_DATE | — | ✅ |
| 57 | GlDailyBalancesYearStartDate | YEAR_START_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
