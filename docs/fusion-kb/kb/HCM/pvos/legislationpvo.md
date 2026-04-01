---
id: DOC-HCM-PVO-LegislationPVO
doc_type: system-doc
title: "LegislationPVO — PVO Human Capital Management"
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
  - LegislationPVO
  - legislationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LegislationPVO

## 📌 Visão Geral

Disponibiliza dados de legislações/territórios com estilo de endereço e códigos. Tabela de referência para compliance e localização por país.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.PersonAM.LegislationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 28 | 2 | 1 | 22 | 79% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_territories_b|FND_TERRITORIES_B]] — 18 atributos (1 PKs, 18 BICC)
- [[fnd_territories_tl|FND_TERRITORIES_TL]] — 10 atributos (4 BICC)

---

## ⚙️ Atributos

### [[fnd_territories_b|FND_TERRITORIES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LegislationPEOAddressStyle | ADDRESS_STYLE | — | ✅ |
| 2 | LegislationPEOAddressValidation | ADDRESS_VALIDATION | — | ✅ |
| 3 | LegislationPEOAlternateTerritoryCode | ALTERNATE_TERRITORY_CODE | — | ✅ |
| 4 | LegislationPEOBankInfoStyle | BANK_INFO_STYLE | — | ✅ |
| 5 | LegislationPEOBankInfoValidation | BANK_INFO_VALIDATION | — | ✅ |
| 6 | LegislationPEOCreatedBy | CREATED_BY | — | ✅ |
| 7 | LegislationPEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | LegislationPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 9 | LegislationPEOEnabledFlag | ENABLED_FLAG | — | ✅ |
| 10 | LegislationPEOEuCode | EU_CODE | — | ✅ |
| 11 | LegislationPEOIsoNumericCode | ISO_NUMERIC_CODE | — | ✅ |
| 12 | LegislationPEOIsoTerritoryCode | ISO_TERRITORY_CODE | — | ✅ |
| 13 | LegislationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | LegislationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 15 | LegislationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | LegislationPEONlsTerritory | NLS_TERRITORY | — | ✅ |
| 17 | LegislationPEOObsoleteFlag | OBSOLETE_FLAG | — | ✅ |
| 18 | TerritoryCode | TERRITORY_CODE | 🔑 | ✅ |

### [[fnd_territories_tl|FND_TERRITORIES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LegislationTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | LegislationTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | LegislationTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | LegislationTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 5 | LegislationTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LegislationTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | LegislationTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | LegislationTranslationPEOSourceLang | SOURCE_LANG | — | — |
| 9 | LegislationTranslationPEOTerritoryCode | TERRITORY_CODE | — | — |
| 10 | LegislationTranslationPEOTerritoryShortName | TERRITORY_SHORT_NAME | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
