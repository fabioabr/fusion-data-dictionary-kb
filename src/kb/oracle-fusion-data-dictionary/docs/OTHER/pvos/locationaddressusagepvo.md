---
id: DOC-OTHER-PVO-LocationAddressUsagePVO
doc_type: system-doc
title: "LocationAddressUsagePVO — PVO Cross-Module"
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
  - LocationAddressUsagePVO
  - locationaddressusagepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LocationAddressUsagePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Location Address Usage. Acessa as tabelas: PER_LOC_ADDRESS_USAGES_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.LocationAM.LocationAddressUsagePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 3 | 14 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[per_loc_address_usages_f|PER_LOC_ADDRESS_USAGES_F]] — 14 atributos (3 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[per_loc_address_usages_f|PER_LOC_ADDRESS_USAGES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 3 | LocAddressUsageId | LOC_ADDRESS_USAGE_ID | 🔑 | ✅ |
| 4 | LocationAddressUsagePEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | ✅ |
| 5 | LocationAddressUsagePEOAddressId | ADDRESS_ID | — | ✅ |
| 6 | LocationAddressUsagePEOAddressUsageType | ADDRESS_USAGE_TYPE | — | ✅ |
| 7 | LocationAddressUsagePEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 8 | LocationAddressUsagePEOCreatedBy | CREATED_BY | — | ✅ |
| 9 | LocationAddressUsagePEOCreationDate | CREATION_DATE | — | ✅ |
| 10 | LocationAddressUsagePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | LocationAddressUsagePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | LocationAddressUsagePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | LocationAddressUsagePEOLocationId | LOCATION_ID | — | ✅ |
| 14 | LocationAddressUsagePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
