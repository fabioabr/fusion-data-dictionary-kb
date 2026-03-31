---
id: DOC-HCM-123
doc_type: system-doc
title: "FND_CURRENCIES_TL — (título a preencher)"
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
  - FND_CURRENCIES_TL
  - fnd_currencies_tl
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# FND_CURRENCIES_TL

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CREATED_BY | — | — | — | — | — | — |
| 2 | CREATION_DATE | — | — | — | — | — | — |
| 3 | CURRENCY_CODE | — | — | — | — | — | — |
| 4 | DESCRIPTION | — | — | — | — | — | — |
| 5 | ENTERPRISE_ID | — | — | — | — | — | — |
| 6 | LANGUAGE | — | — | — | — | — | — |
| 7 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 8 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 9 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 10 | NAME | — | — | — | — | — | — |
| 11 | SEED_DATA_SOURCE | — | — | — | — | — | — |
| 12 | SOURCE_LANG | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[currenciespvo|CurrenciesPVO]] (HCM · BICC: 2/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CURRENCY_CODE | CurrencyCode1 | — |
| DESCRIPTION | Description | ✅ |
| LANGUAGE | Language | — |
| NAME | Name | ✅ |
| SOURCE_LANG | SourceLang | — |

### [[currenciestlpvo|CurrenciesTLPVO]] (HCM · BICC: 10/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| CURRENCY_CODE | CurrencyCode | ✅ |
| DESCRIPTION | Description | ✅ |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| NAME | Name | ✅ |
| SOURCE_LANG | SourceLang | ✅ |

### [[dimriskpvo|DimRiskPVO]] (OTHER · BICC: 3/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CurrencyPEOCreatedBy | — |
| CREATION_DATE | CurrencyPEOCreationDate | — |
| CURRENCY_CODE | CurrencyPEOCurrencyCode | ✅ |
| DESCRIPTION | CurrencyPEODescription | — |
| ENTERPRISE_ID | CurrencyPEOEnterpriseId | — |
| LANGUAGE | CurrencyPEOLanguage | — |
| LAST_UPDATE_DATE | CurrencyPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CurrencyPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | CurrencyPEOLastUpdatedBy | — |
| NAME | CurrencyPEOName | ✅ |
| SEED_DATA_SOURCE | CurrencyPEOSeedDataSource | — |
| SOURCE_LANG | CurrencyPEOSourceLang | — |

### [[dummycurrenciespvo|DummyCurrenciesPVO]] (HCM · BICC: 2/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CURRENCY_CODE | CurrencyCode1 | — |
| DESCRIPTION | Description | ✅ |
| LANGUAGE | Language | — |
| NAME | Name | ✅ |
| SOURCE_LANG | SourceLang | — |
