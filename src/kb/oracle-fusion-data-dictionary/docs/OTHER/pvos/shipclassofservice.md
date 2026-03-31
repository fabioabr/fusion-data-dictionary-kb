---
id: DOC-OTHER-PVO-ShipClassOfService
doc_type: system-doc
title: "ShipClassOfService — PVO Cross-Module"
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
  - ShipClassOfService
  - shipclassofservice
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ShipClassOfService

## 📌 Visão Geral

View Object para extração BICC de dados de Ship Class Of Service. Acessa as tabelas: MSC_SR_LOOKUP_VALUES_B, MSC_SR_LOOKUP_VALUES_TL.

**Caminho:** `FscmTopModelAM.DooTopAM.ShipClassOfService`

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
| 3 | ShipClassOfServiceCreatedBy | CREATED_BY | — | — |
| 4 | ShipClassOfServiceCreationDate | CREATION_DATE | — | — |
| 5 | ShipClassOfServiceEnabledFlag | ENABLED_FLAG | — | — |
| 6 | ShipClassOfServiceEndDateActive | END_DATE_ACTIVE | — | — |
| 7 | ShipClassOfServiceLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ShipClassOfServiceLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ShipClassOfServiceLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ShipClassOfServiceRefreshNumber | REFRESH_NUMBER | — | — |
| 11 | ShipClassOfServiceStartDateActive | START_DATE_ACTIVE | — | — |

### [[msc_sr_lookup_values_tl|MSC_SR_LOOKUP_VALUES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ShipClassOfServiceTransCreatedBy | CREATED_BY | — | — |
| 2 | ShipClassOfServiceTransCreationDate | CREATION_DATE | — | — |
| 3 | ShipClassOfServiceTransDescription | DESCRIPTION | — | ✅ |
| 4 | ShipClassOfServiceTransLanguage | LANGUAGE | — | ✅ |
| 5 | ShipClassOfServiceTransLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 6 | ShipClassOfServiceTransLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | ShipClassOfServiceTransLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | ShipClassOfServiceTransLookupCode | LOOKUP_CODE | — | — |
| 9 | ShipClassOfServiceTransLookupType | LOOKUP_TYPE | — | — |
| 10 | ShipClassOfServiceTransMeaning | MEANING | — | ✅ |
| 11 | ShipClassOfServiceTransRefreshNumber | REFRESH_NUMBER | — | — |
| 12 | ShipClassOfServiceTransSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
