---
id: DOC-OTHER-PVO-ShipmentPriority
doc_type: system-doc
title: "ShipmentPriority — PVO Cross-Module"
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
  - ShipmentPriority
  - shipmentpriority
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ShipmentPriority

## 📌 Visão Geral

View Object para extração BICC de dados de Shipment Priority. Acessa as tabelas: MSC_SR_LOOKUP_VALUES_B, MSC_SR_LOOKUP_VALUES_TL.

**Caminho:** `FscmTopModelAM.DooTopAM.ShipmentPriority`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 23 | 2 | 0 | 7 | 30% |

---

## 🔗 Tabelas Relacionadas

- [[msc_sr_lookup_values_b|MSC_SR_LOOKUP_VALUES_B]] — 11 atributos (3 BICC)
- [[msc_sr_lookup_values_tl|MSC_SR_LOOKUP_VALUES_TL]] — 12 atributos (4 BICC)

---

## ⚙️ Atributos

### [[msc_sr_lookup_values_b|MSC_SR_LOOKUP_VALUES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LookupCode | LOOKUP_CODE | — | ✅ |
| 2 | LookupType | LOOKUP_TYPE | — | ✅ |
| 3 | ShipmentPriorityCreatedBy | CREATED_BY | — | — |
| 4 | ShipmentPriorityCreationDate | CREATION_DATE | — | — |
| 5 | ShipmentPriorityEnabledFlag | ENABLED_FLAG | — | — |
| 6 | ShipmentPriorityEndDateActive | END_DATE_ACTIVE | — | — |
| 7 | ShipmentPriorityLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ShipmentPriorityLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ShipmentPriorityLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ShipmentPriorityRefreshNumber | REFRESH_NUMBER | — | — |
| 11 | ShipmentPriorityStartDateActive | START_DATE_ACTIVE | — | — |

### [[msc_sr_lookup_values_tl|MSC_SR_LOOKUP_VALUES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ShipmentPriorityTranslationCreatedBy | CREATED_BY | — | — |
| 2 | ShipmentPriorityTranslationCreationDate | CREATION_DATE | — | — |
| 3 | ShipmentPriorityTranslationDescription | DESCRIPTION | — | ✅ |
| 4 | ShipmentPriorityTranslationLanguage | LANGUAGE | — | ✅ |
| 5 | ShipmentPriorityTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ShipmentPriorityTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | ShipmentPriorityTranslationLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | ShipmentPriorityTranslationLookupCode | LOOKUP_CODE | — | — |
| 9 | ShipmentPriorityTranslationLookupType | LOOKUP_TYPE | — | — |
| 10 | ShipmentPriorityTranslationMeaning | MEANING | — | ✅ |
| 11 | ShipmentPriorityTranslationRefreshNumber | REFRESH_NUMBER | — | — |
| 12 | ShipmentPriorityTranslationSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
