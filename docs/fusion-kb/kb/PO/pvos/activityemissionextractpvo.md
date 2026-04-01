---
id: DOC-PO-PVO-ActivityEmissionExtractPVO
doc_type: system-doc
title: "ActivityEmissionExtractPVO — PVO Purchasing"
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
  - ActivityEmissionExtractPVO
  - activityemissionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ActivityEmissionExtractPVO

## 📌 Visão Geral

Extrai dados de emissões de carbono associadas a atividades de procurement, incluindo tipo de emissão e quantidade. Permite cálculo da pegada de carbono da cadeia de compras e reporting ESG corporativo.

**Caminho:** `FscmTopModelAM.PrcExtractAM.SusBiccExtractAM.ActivityEmissionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 25 | 1 | 1 | 24 | 96% |

---

## 🔗 Tabelas Relacionadas

- [[sus_activity_emissions|SUS_ACTIVITY_EMISSIONS]] — 25 atributos (1 PKs, 24 BICC)

---

## ⚙️ Atributos

### [[sus_activity_emissions|SUS_ACTIVITY_EMISSIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActivityEmissionId | ACTIVITY_EMISSION_ID | 🔑 | ✅ |
| 2 | ActivityId | ACTIVITY_ID | — | ✅ |
| 3 | ActivityMeasureId | ACTIVITY_MEASURE_ID | — | ✅ |
| 4 | Co2eEmissionQty | CO2E_EMISSION_QTY | — | ✅ |
| 5 | Co2eUomCode | CO2E_UOM_CODE | — | ✅ |
| 6 | CreatedBy | CREATED_BY | — | ✅ |
| 7 | CreationDate | CREATION_DATE | — | ✅ |
| 8 | DenominatorCurrencyCode | DENOMINATOR_CURRENCY_CODE | — | ✅ |
| 9 | DenominatorUomCode | DENOMINATOR_UOM_CODE | — | ✅ |
| 10 | Description | DESCRIPTION | — | ✅ |
| 11 | EmissionFactor | EMISSION_FACTOR | — | ✅ |
| 12 | EmissionFactorMapId | EMISSION_FACTOR_MAP_ID | — | ✅ |
| 13 | EmissionFactorSource | EMISSION_FACTOR_SOURCE | — | ✅ |
| 14 | EmissionQty | EMISSION_QTY | — | ✅ |
| 15 | EmissionTypeCode | EMISSION_TYPE_CODE | — | ✅ |
| 16 | EmissionUomCode | EMISSION_UOM_CODE | — | ✅ |
| 17 | GwpFactor | GWP_FACTOR | — | ✅ |
| 18 | GwpId | GWP_ID | — | ✅ |
| 19 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 20 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 21 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 22 | MeasureTypeCode | MEASURE_TYPE_CODE | — | ✅ |
| 23 | NumeratorUomCode | NUMERATOR_UOM_CODE | — | ✅ |
| 24 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 25 | StatusCode | STATUS_CODE | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
