---
id: DOC-OTHER-PVO-LocationPVO
doc_type: system-doc
title: "LocationPVO — PVO Cross-Module"
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
  - LocationPVO
  - locationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LocationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Location. Acessa as tabelas: FND_SETID_SETS_VL, PER_LOCATIONS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.LocationAM.LocationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 2 | 1 | 16 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_setid_sets_vl|FND_SETID_SETS_VL]] — 4 atributos (4 BICC)
- [[per_locations|PER_LOCATIONS]] — 12 atributos (1 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[fnd_setid_sets_vl|FND_SETID_SETS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SetIdSetPEODescription | DESCRIPTION | — | ✅ |
| 2 | SetIdSetPEOSetCode | SET_CODE | — | ✅ |
| 3 | SetIdSetPEOSetId | SET_ID | — | ✅ |
| 4 | SetIdSetPEOSetName | SET_NAME | — | ✅ |

### [[per_locations|PER_LOCATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LocationId | LOCATION_ID | 🔑 | ✅ |
| 2 | LocationPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | ✅ |
| 3 | LocationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 4 | LocationPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | LocationPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | LocationPEOInternalLocationCode | INTERNAL_LOCATION_CODE | — | ✅ |
| 7 | LocationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LocationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LocationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | LocationPEOLocationImageUrl | LOCATION_IMAGE_URL | — | ✅ |
| 11 | LocationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | LocationPEOSetId | SET_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
