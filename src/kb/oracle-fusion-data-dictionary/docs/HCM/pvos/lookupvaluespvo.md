---
id: DOC-HCM-PVO-LookupValuesPVO
doc_type: system-doc
title: "LookupValuesPVO — PVO Human Capital Management"
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
  - LookupValuesPVO
  - lookupvaluespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LookupValuesPVO

## 📌 Visão Geral

Extrai valores de listas de lookup (domínios de valores) do Oracle Fusion, incluindo código, tipo e descrição. Fundamental para decodificação de campos codificados em todo o HCM.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.AnalyticsServiceAM.LookupValuesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 39 | 2 | 4 | 15 | 38% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_lookup_values_b|FND_LOOKUP_VALUES_B]] — 31 atributos (4 PKs, 13 BICC)
- [[fnd_lookup_values_tl|FND_LOOKUP_VALUES_TL]] — 8 atributos (2 BICC)

---

## ⚙️ Atributos

### [[fnd_lookup_values_b|FND_LOOKUP_VALUES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Attribute1 | ATTRIBUTE1 | — | — |
| 2 | Attribute10 | ATTRIBUTE10 | — | — |
| 3 | Attribute11 | ATTRIBUTE11 | — | — |
| 4 | Attribute12 | ATTRIBUTE12 | — | — |
| 5 | Attribute13 | ATTRIBUTE13 | — | — |
| 6 | Attribute14 | ATTRIBUTE14 | — | — |
| 7 | Attribute15 | ATTRIBUTE15 | — | — |
| 8 | Attribute2 | ATTRIBUTE2 | — | — |
| 9 | Attribute3 | ATTRIBUTE3 | — | — |
| 10 | Attribute4 | ATTRIBUTE4 | — | — |
| 11 | Attribute5 | ATTRIBUTE5 | — | — |
| 12 | Attribute6 | ATTRIBUTE6 | — | — |
| 13 | Attribute7 | ATTRIBUTE7 | — | — |
| 14 | Attribute8 | ATTRIBUTE8 | — | — |
| 15 | Attribute9 | ATTRIBUTE9 | — | — |
| 16 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 17 | CreatedBy | CREATED_BY | — | ✅ |
| 18 | CreationDate | CREATION_DATE | — | ✅ |
| 19 | DisplaySequence | DISPLAY_SEQUENCE | — | ✅ |
| 20 | EnabledFlag | ENABLED_FLAG | — | ✅ |
| 21 | EndDateActive | END_DATE_ACTIVE | — | ✅ |
| 22 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 23 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 24 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 25 | LookupCode | LOOKUP_CODE | 🔑 | ✅ |
| 26 | LookupType | LOOKUP_TYPE | 🔑 | ✅ |
| 27 | SetId | SET_ID | 🔑 | ✅ |
| 28 | StartDateActive | START_DATE_ACTIVE | — | ✅ |
| 29 | Tag | TAG | — | ✅ |
| 30 | TerritoryCode | TERRITORY_CODE | — | — |
| 31 | ViewApplicationId | VIEW_APPLICATION_ID | 🔑 | ✅ |

### [[fnd_lookup_values_tl|FND_LOOKUP_VALUES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Description | DESCRIPTION | — | ✅ |
| 2 | Language | LANGUAGE | — | — |
| 3 | LookupCode1 | LOOKUP_CODE | — | — |
| 4 | LookupType1 | LOOKUP_TYPE | — | — |
| 5 | Meaning | MEANING | — | ✅ |
| 6 | SetId1 | SET_ID | — | — |
| 7 | SourceLang | SOURCE_LANG | — | — |
| 8 | ViewApplicationId1 | VIEW_APPLICATION_ID | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
