---
id: DOC-OTHER-PVO-TerritoriesPVO
doc_type: system-doc
title: "TerritoriesPVO — PVO Cross-Module"
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
  - TerritoriesPVO
  - territoriespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TerritoriesPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Territories. Acessa as tabelas: FND_TERRITORIES_B, FND_TERRITORIES_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.AnalyticsServiceAM.TerritoriesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 23 | 2 | 2 | 9 | 39% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_territories_b|FND_TERRITORIES_B]] — 18 atributos (1 PKs, 5 BICC)
- [[fnd_territories_tl|FND_TERRITORIES_TL]] — 5 atributos (1 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[fnd_territories_b|FND_TERRITORIES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AddressStyle | ADDRESS_STYLE | — | — |
| 2 | AddressValidation | ADDRESS_VALIDATION | — | — |
| 3 | AlternateTerritoryCode | ALTERNATE_TERRITORY_CODE | — | — |
| 4 | BankInfoStyle | BANK_INFO_STYLE | — | — |
| 5 | BankInfoValidation | BANK_INFO_VALIDATION | — | — |
| 6 | CreatedBy | CREATED_BY | — | ✅ |
| 7 | CreationDate | CREATION_DATE | — | ✅ |
| 8 | CurrencyCode | CURRENCY_CODE | — | — |
| 9 | EnabledFlag | ENABLED_FLAG | — | — |
| 10 | EuCode | EU_CODE | — | — |
| 11 | IsoNumericCode | ISO_NUMERIC_CODE | — | — |
| 12 | IsoTerritoryCode | ISO_TERRITORY_CODE | — | — |
| 13 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | NlsTerritory | NLS_TERRITORY | — | — |
| 17 | ObsoleteFlag | OBSOLETE_FLAG | — | — |
| 18 | TerritoryCode | TERRITORY_CODE | 🔑 | ✅ |

### [[fnd_territories_tl|FND_TERRITORIES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Description | DESCRIPTION | — | ✅ |
| 2 | Language | LANGUAGE | 🔑 | ✅ |
| 3 | SourceLang | SOURCE_LANG | — | ✅ |
| 4 | TerritoryCode1 | TERRITORY_CODE | — | — |
| 5 | TerritoryShortName | TERRITORY_SHORT_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
