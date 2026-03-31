---
id: DOC-PO-PVO-EmissionFactorMappingExtractPVO
doc_type: system-doc
title: "EmissionFactorMappingExtractPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - EmissionFactorMappingExtractPVO
  - emissionfactormappingextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EmissionFactorMappingExtractPVO

## 📌 Visão Geral

Extrai o mapeamento de fatores de emissão para atividades de procurement, com coeficientes de conversão por tipo de gás. Essencial para cálculo preciso da pegada de carbono nas compras.

**Caminho:** `FscmTopModelAM.PrcExtractAM.SusBiccExtractAM.EmissionFactorMappingExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 58 | 1 | 1 | 58 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[sus_emission_factor_maps|SUS_EMISSION_FACTOR_MAPS]] — 58 atributos (1 PKs, 58 BICC)

---

## ⚙️ Atributos

### [[sus_emission_factor_maps|SUS_EMISSION_FACTOR_MAPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActivityTypeCode | ACTIVITY_TYPE_CODE | — | ✅ |
| 2 | CountryCode | COUNTRY_CODE | — | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | DenominatorCurrencyCode | DENOMINATOR_CURRENCY_CODE | — | ✅ |
| 6 | DenominatorUomCode | DENOMINATOR_UOM_CODE | — | ✅ |
| 7 | Description | DESCRIPTION | — | ✅ |
| 8 | EfmAttribute1 | EFM_ATTRIBUTE1 | — | ✅ |
| 9 | EfmAttribute10 | EFM_ATTRIBUTE10 | — | ✅ |
| 10 | EfmAttribute11 | EFM_ATTRIBUTE11 | — | ✅ |
| 11 | EfmAttribute12 | EFM_ATTRIBUTE12 | — | ✅ |
| 12 | EfmAttribute13 | EFM_ATTRIBUTE13 | — | ✅ |
| 13 | EfmAttribute14 | EFM_ATTRIBUTE14 | — | ✅ |
| 14 | EfmAttribute15 | EFM_ATTRIBUTE15 | — | ✅ |
| 15 | EfmAttribute16 | EFM_ATTRIBUTE16 | — | ✅ |
| 16 | EfmAttribute17 | EFM_ATTRIBUTE17 | — | ✅ |
| 17 | EfmAttribute18 | EFM_ATTRIBUTE18 | — | ✅ |
| 18 | EfmAttribute19 | EFM_ATTRIBUTE19 | — | ✅ |
| 19 | EfmAttribute2 | EFM_ATTRIBUTE2 | — | ✅ |
| 20 | EfmAttribute20 | EFM_ATTRIBUTE20 | — | ✅ |
| 21 | EfmAttribute3 | EFM_ATTRIBUTE3 | — | ✅ |
| 22 | EfmAttribute4 | EFM_ATTRIBUTE4 | — | ✅ |
| 23 | EfmAttribute5 | EFM_ATTRIBUTE5 | — | ✅ |
| 24 | EfmAttribute6 | EFM_ATTRIBUTE6 | — | ✅ |
| 25 | EfmAttribute7 | EFM_ATTRIBUTE7 | — | ✅ |
| 26 | EfmAttribute8 | EFM_ATTRIBUTE8 | — | ✅ |
| 27 | EfmAttribute9 | EFM_ATTRIBUTE9 | — | ✅ |
| 28 | EfmAttributeDate1 | EFM_ATTRIBUTE_DATE1 | — | ✅ |
| 29 | EfmAttributeDate2 | EFM_ATTRIBUTE_DATE2 | — | ✅ |
| 30 | EfmAttributeDate3 | EFM_ATTRIBUTE_DATE3 | — | ✅ |
| 31 | EfmAttributeDate4 | EFM_ATTRIBUTE_DATE4 | — | ✅ |
| 32 | EfmAttributeDate5 | EFM_ATTRIBUTE_DATE5 | — | ✅ |
| 33 | EfmAttributeNumber1 | EFM_ATTRIBUTE_NUMBER1 | — | ✅ |
| 34 | EfmAttributeNumber10 | EFM_ATTRIBUTE_NUMBER10 | — | ✅ |
| 35 | EfmAttributeNumber2 | EFM_ATTRIBUTE_NUMBER2 | — | ✅ |
| 36 | EfmAttributeNumber3 | EFM_ATTRIBUTE_NUMBER3 | — | ✅ |
| 37 | EfmAttributeNumber4 | EFM_ATTRIBUTE_NUMBER4 | — | ✅ |
| 38 | EfmAttributeNumber5 | EFM_ATTRIBUTE_NUMBER5 | — | ✅ |
| 39 | EfmAttributeNumber6 | EFM_ATTRIBUTE_NUMBER6 | — | ✅ |
| 40 | EfmAttributeNumber7 | EFM_ATTRIBUTE_NUMBER7 | — | ✅ |
| 41 | EfmAttributeNumber8 | EFM_ATTRIBUTE_NUMBER8 | — | ✅ |
| 42 | EfmAttributeNumber9 | EFM_ATTRIBUTE_NUMBER9 | — | ✅ |
| 43 | EmissionFactor | EMISSION_FACTOR | — | ✅ |
| 44 | EmissionFactorMappingId | EMISSION_FACTOR_MAP_ID | 🔑 | ✅ |
| 45 | EmissionFactorSource | EMISSION_FACTOR_SOURCE | — | ✅ |
| 46 | EmissionTypeCode | EMISSION_TYPE_CODE | — | ✅ |
| 47 | EndDate | END_DATE | — | ✅ |
| 48 | InventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 49 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 50 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 51 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 52 | LegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 53 | MeasureTypeCode | MEASURE_TYPE_CODE | — | ✅ |
| 54 | NumeratorUomCode | NUMERATOR_UOM_CODE | — | ✅ |
| 55 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 56 | Ranking | RANKING | — | ✅ |
| 57 | StartDate | START_DATE | — | ✅ |
| 58 | SupplierId | SUPPLIER_ID | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
