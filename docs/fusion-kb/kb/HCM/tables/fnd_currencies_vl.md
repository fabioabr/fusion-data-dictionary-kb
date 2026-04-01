---
id: DOC-HCM-124
doc_type: system-doc
title: "FND_CURRENCIES_VL — (título a preencher)"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - human-capital-management
  - data-dictionary
aliases:
  - FND_CURRENCIES_VL
  - fnd_currencies_vl
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# FND_CURRENCIES_VL

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CONTEXT | — | — | — | — | — | — |
| 2 | CURRENCY_CODE | — | — | — | — | — | — |
| 3 | CURRENCY_FLAG | — | — | — | — | — | — |
| 4 | DERIVE_EFFECTIVE | — | — | — | — | — | — |
| 5 | DERIVE_FACTOR | — | — | — | — | — | — |
| 6 | DERIVE_TYPE | — | — | — | — | — | — |
| 7 | DESCRIPTION | — | — | — | — | — | — |
| 8 | ENABLED_FLAG | — | — | — | — | — | — |
| 9 | END_DATE_ACTIVE | — | — | — | — | — | — |
| 10 | EXTENDED_PRECISION | — | — | — | — | — | — |
| 11 | ISO_FLAG | — | — | — | — | — | — |
| 12 | ISSUING_TERRITORY_CODE | — | — | — | — | — | — |
| 13 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 14 | MINIMUM_ACCOUNTABLE_UNIT | — | — | — | — | — | — |
| 15 | NAME | — | — | — | — | — | — |
| 16 | PRECISION | — | — | — | — | — | — |
| 17 | START_DATE_ACTIVE | — | — | — | — | — | — |
| 18 | SYMBOL | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[currencypvo|CurrencyPVO]] (HCM · BICC: 4/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONTEXT | CurrencyPEOContext | — |
| CURRENCY_CODE | CurrencyPEOCurrencyCode | ✅ |
| CURRENCY_FLAG | CurrencyPEOCurrencyFlag | — |
| DERIVE_EFFECTIVE | CurrencyPEODeriveEffective | — |
| DERIVE_FACTOR | CurrencyPEODeriveFactor | — |
| DERIVE_TYPE | CurrencyPEODeriveType | — |
| DESCRIPTION | CurrencyPEODescription | ✅ |
| ENABLED_FLAG | CurrencyPEOEnabledFlag | — |
| END_DATE_ACTIVE | CurrencyPEOEndDateActive | — |
| EXTENDED_PRECISION | CurrencyPEOExtendedPrecision | — |
| ISO_FLAG | CurrencyPEOIsoFlag | — |
| ISSUING_TERRITORY_CODE | CurrencyPEOIssuingTerritoryCode | — |
| LAST_UPDATE_DATE | CurrencyPEOLastUpdateDate | ✅ |
| MINIMUM_ACCOUNTABLE_UNIT | CurrencyPEOMinimumAccountableUnit | — |
| NAME | CurrencyPEOName | ✅ |
| PRECISION | CurrencyPEOPrecision | — |
| START_DATE_ACTIVE | CurrencyPEOStartDateActive | — |
| SYMBOL | CurrencyPEOSymbol | — |

### [[ledgerpvo|LedgerPVO]] (GL · BICC: 1/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONTEXT | CurrencyContext | — |
| CURRENCY_CODE | CurrencyCurrencyCode | ✅ |
| CURRENCY_FLAG | CurrencyCurrencyFlag | — |
| DERIVE_EFFECTIVE | CurrencyDeriveEffective | — |
| DERIVE_FACTOR | CurrencyDeriveFactor | — |
| DERIVE_TYPE | CurrencyDeriveType | — |
| DESCRIPTION | CurrencyDescription | — |
| ENABLED_FLAG | CurrencyEnabledFlag | — |
| END_DATE_ACTIVE | CurrencyEndDateActive | — |
| EXTENDED_PRECISION | CurrencyExtendedPrecision | — |
| ISO_FLAG | CurrencyIsoFlag | — |
| ISSUING_TERRITORY_CODE | CurrencyIssuingTerritoryCode | — |
| MINIMUM_ACCOUNTABLE_UNIT | CurrencyMinimumAccountableUnit | — |
| NAME | CurrencyName | — |
| PRECISION | CurrencyPrecision | — |
| START_DATE_ACTIVE | CurrencyStartDateActive | — |
| SYMBOL | CurrencySymbol | — |

### [[ledgersetpvo|LedgerSetPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONTEXT | CurrencyContext | — |
| CURRENCY_CODE | CurrencyCurrencyCode | — |
| CURRENCY_FLAG | CurrencyCurrencyFlag | — |
| DERIVE_EFFECTIVE | CurrencyDeriveEffective | — |
| DERIVE_FACTOR | CurrencyDeriveFactor | — |
| DERIVE_TYPE | CurrencyDeriveType | — |
| DESCRIPTION | CurrencyDescription | — |
| ENABLED_FLAG | CurrencyEnabledFlag | — |
| END_DATE_ACTIVE | CurrencyEndDateActive | — |
| EXTENDED_PRECISION | CurrencyExtendedPrecision | — |
| ISO_FLAG | CurrencyIsoFlag | — |
| ISSUING_TERRITORY_CODE | CurrencyIssuingTerritoryCode | — |
| MINIMUM_ACCOUNTABLE_UNIT | CurrencyMinimumAccountableUnit | — |
| NAME | CurrencyName | — |
| PRECISION | CurrencyPrecision | — |
| START_DATE_ACTIVE | CurrencyStartDateActive | — |
| SYMBOL | CurrencySymbol | — |

### [[project|Project]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CURRENCY_CODE | ProjectCurrencyCodePEOCurrencyCode | — |
| CURRENCY_CODE | ProjectFunctionalCurrencyPEOCurrencyCode | — |
| DESCRIPTION | ProjectCurrencyCodePEODescription | — |
| DESCRIPTION | ProjectFunctionalCurrencyPEODescription | — |
| NAME | ProjectCurrencyCodePEOName | — |
| NAME | ProjectFunctionalCurrencyPEOName | — |

### [[projectcommitmentpvo|ProjectCommitmentPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CURRENCY_CODE | CurrencyPEOCurrencyCode | — |
| NAME | CurrencyPEOCurrencyName | — |

### [[projectexec|ProjectExec]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CURRENCY_CODE | ProjectCurrencyCodePEOCurrencyCode | — |
| CURRENCY_CODE | ProjectFunctionalCurrencyPEOCurrencyCode | — |
| DESCRIPTION | ProjectCurrencyCodePEODescription | — |
| DESCRIPTION | ProjectFunctionalCurrencyPEODescription | — |
| NAME | ProjectCurrencyCodePEOName | — |
| NAME | ProjectFunctionalCurrencyPEOName | — |

### [[projectrefpvo|ProjectRefPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CURRENCY_CODE | ProjectCurrencyCodePEOCurrencyCode | — |
| CURRENCY_CODE | ProjectFunctionalCurrencyPEOCurrencyCode | — |
| DESCRIPTION | ProjectCurrencyCodePEODescription | — |
| DESCRIPTION | ProjectFunctionalCurrencyPEODescription | — |
| NAME | ProjectCurrencyCodePEOName | — |
| NAME | ProjectFunctionalCurrencyPEOName | — |

### [[projectview|ProjectView]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CURRENCY_CODE | ProjectCurrencyCodePEOCurrencyCode | — |
| CURRENCY_CODE | ProjectFunctionalCurrencyPEOCurrencyCode | — |
| DESCRIPTION | ProjectCurrencyCodePEODescription | — |
| DESCRIPTION | ProjectFunctionalCurrencyPEODescription | — |
| NAME | ProjectCurrencyCodePEOName | — |
| NAME | ProjectFunctionalCurrencyPEOName | — |
