---
id: DOC-HCM-139
doc_type: system-doc
title: "FND_TERRITORIES_B — (título a preencher)"
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
  - FND_TERRITORIES_B
  - fnd_territories_b
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# FND_TERRITORIES_B

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ADDRESS_STYLE | — | — | — | — | — | — |
| 2 | ADDRESS_VALIDATION | — | — | — | — | — | — |
| 3 | ALTERNATE_TERRITORY_CODE | — | — | — | — | — | — |
| 4 | BANK_INFO_STYLE | — | — | — | — | — | — |
| 5 | BANK_INFO_VALIDATION | — | — | — | — | — | — |
| 6 | CREATED_BY | — | — | — | — | — | — |
| 7 | CREATION_DATE | — | — | — | — | — | — |
| 8 | CURRENCY_CODE | — | — | — | — | — | — |
| 9 | ENABLED_FLAG | — | — | — | — | — | — |
| 10 | EU_CODE | — | — | — | — | — | — |
| 11 | ISO_NUMERIC_CODE | — | — | — | — | — | — |
| 12 | ISO_TERRITORY_CODE | — | — | — | — | — | — |
| 13 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 14 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 15 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 16 | NLS_TERRITORY | — | — | — | — | — | — |
| 17 | OBSOLETE_FLAG | — | — | — | — | — | — |
| 18 | TERRITORY_CODE | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[legislationpvo|LegislationPVO]] (HCM · BICC: 18/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDRESS_STYLE | LegislationPEOAddressStyle | ✅ |
| ADDRESS_VALIDATION | LegislationPEOAddressValidation | ✅ |
| ALTERNATE_TERRITORY_CODE | LegislationPEOAlternateTerritoryCode | ✅ |
| BANK_INFO_STYLE | LegislationPEOBankInfoStyle | ✅ |
| BANK_INFO_VALIDATION | LegislationPEOBankInfoValidation | ✅ |
| CREATED_BY | LegislationPEOCreatedBy | ✅ |
| CREATION_DATE | LegislationPEOCreationDate | ✅ |
| CURRENCY_CODE | LegislationPEOCurrencyCode | ✅ |
| ENABLED_FLAG | LegislationPEOEnabledFlag | ✅ |
| EU_CODE | LegislationPEOEuCode | ✅ |
| ISO_NUMERIC_CODE | LegislationPEOIsoNumericCode | ✅ |
| ISO_TERRITORY_CODE | LegislationPEOIsoTerritoryCode | ✅ |
| LAST_UPDATE_DATE | LegislationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LegislationPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LegislationPEOLastUpdatedBy | ✅ |
| NLS_TERRITORY | LegislationPEONlsTerritory | ✅ |
| OBSOLETE_FLAG | LegislationPEOObsoleteFlag | ✅ |
| TERRITORY_CODE | TerritoryCode | ✅ |

### [[territoriespvo|TerritoriesPVO]] (HCM · BICC: 5/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDRESS_STYLE | AddressStyle | — |
| ADDRESS_VALIDATION | AddressValidation | — |
| ALTERNATE_TERRITORY_CODE | AlternateTerritoryCode | — |
| BANK_INFO_STYLE | BankInfoStyle | — |
| BANK_INFO_VALIDATION | BankInfoValidation | — |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| CURRENCY_CODE | CurrencyCode | — |
| ENABLED_FLAG | EnabledFlag | — |
| EU_CODE | EuCode | — |
| ISO_NUMERIC_CODE | IsoNumericCode | — |
| ISO_TERRITORY_CODE | IsoTerritoryCode | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| NLS_TERRITORY | NlsTerritory | — |
| OBSOLETE_FLAG | ObsoleteFlag | — |
| TERRITORY_CODE | TerritoryCode | ✅ |
