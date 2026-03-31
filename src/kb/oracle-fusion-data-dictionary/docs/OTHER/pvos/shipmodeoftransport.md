---
id: DOC-OTHER-PVO-ShipModeOfTransport
doc_type: system-doc
title: "ShipModeOfTransport — PVO Cross-Module"
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
  - ShipModeOfTransport
  - shipmodeoftransport
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ShipModeOfTransport

## 📌 Visão Geral

View Object para extração BICC de dados de Ship Mode Of Transport. Acessa as tabelas: MSC_SR_LOOKUP_VALUES_B, MSC_SR_LOOKUP_VALUES_TL.

**Caminho:** `FscmTopModelAM.DooTopAM.ShipModeOfTransport`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 23 | 2 | 0 | 6 | 26% |

---

## 🔗 Tabelas Relacionadas

- [[msc_sr_lookup_values_b|MSC_SR_LOOKUP_VALUES_B]] — 11 atributos (3 BICC)
- [[msc_sr_lookup_values_tl|MSC_SR_LOOKUP_VALUES_TL]] — 12 atributos (3 BICC)

---

## ⚙️ Atributos

### [[msc_sr_lookup_values_b|MSC_SR_LOOKUP_VALUES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LookupCode | LOOKUP_CODE | — | ✅ |
| 2 | LookupType | LOOKUP_TYPE | — | ✅ |
| 3 | ShipModeOfTransportCreatedBy | CREATED_BY | — | — |
| 4 | ShipModeOfTransportCreationDate | CREATION_DATE | — | — |
| 5 | ShipModeOfTransportEnabledFlag | ENABLED_FLAG | — | — |
| 6 | ShipModeOfTransportEndDateActive | END_DATE_ACTIVE | — | — |
| 7 | ShipModeOfTransportLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ShipModeOfTransportLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ShipModeOfTransportLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ShipModeOfTransportRefreshNumber | REFRESH_NUMBER | — | — |
| 11 | ShipModeOfTransportStartDateActive | START_DATE_ACTIVE | — | — |

### [[msc_sr_lookup_values_tl|MSC_SR_LOOKUP_VALUES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ShipModeOfTransportTransCreatedBy | CREATED_BY | — | — |
| 2 | ShipModeOfTransportTransCreationDate | CREATION_DATE | — | — |
| 3 | ShipModeOfTransportTransDescription | DESCRIPTION | — | ✅ |
| 4 | ShipModeOfTransportTransLanguage | LANGUAGE | — | ✅ |
| 5 | ShipModeOfTransportTransLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 6 | ShipModeOfTransportTransLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | ShipModeOfTransportTransLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | ShipModeOfTransportTransLookupCode | LOOKUP_CODE | — | — |
| 9 | ShipModeOfTransportTransLookupType | LOOKUP_TYPE | — | — |
| 10 | ShipModeOfTransportTransMeaning | MEANING | — | ✅ |
| 11 | ShipModeOfTransportTransRefreshNumber | REFRESH_NUMBER | — | — |
| 12 | ShipModeOfTransportTransSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
