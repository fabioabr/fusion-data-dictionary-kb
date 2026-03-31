---
id: DOC-OTHER-PVO-CollectorExtractPVO
doc_type: system-doc
title: "CollectorExtractPVO — PVO Cross-Module"
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
  - CollectorExtractPVO
  - collectorextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CollectorExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Collector Extract. Acessa as tabelas: AR_COLLECTORS.

**Caminho:** `FscmTopModelAM.FinExtractAM.IexBiccExtractAM.CollectorExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 34 | 1 | 1 | 18 | 53% |

---

## 🔗 Tabelas Relacionadas

- [[ar_collectors|AR_COLLECTORS]] — 34 atributos (1 PKs, 18 BICC)

---

## ⚙️ Atributos

### [[ar_collectors|AR_COLLECTORS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ArCollectorAlias | ALIAS | — | ✅ |
| 2 | ArCollectorAttribute1 | ATTRIBUTE1 | — | — |
| 3 | ArCollectorAttribute10 | ATTRIBUTE10 | — | — |
| 4 | ArCollectorAttribute11 | ATTRIBUTE11 | — | — |
| 5 | ArCollectorAttribute12 | ATTRIBUTE12 | — | — |
| 6 | ArCollectorAttribute13 | ATTRIBUTE13 | — | — |
| 7 | ArCollectorAttribute14 | ATTRIBUTE14 | — | — |
| 8 | ArCollectorAttribute15 | ATTRIBUTE15 | — | — |
| 9 | ArCollectorAttribute2 | ATTRIBUTE2 | — | — |
| 10 | ArCollectorAttribute3 | ATTRIBUTE3 | — | — |
| 11 | ArCollectorAttribute4 | ATTRIBUTE4 | — | — |
| 12 | ArCollectorAttribute5 | ATTRIBUTE5 | — | — |
| 13 | ArCollectorAttribute6 | ATTRIBUTE6 | — | — |
| 14 | ArCollectorAttribute7 | ATTRIBUTE7 | — | — |
| 15 | ArCollectorAttribute8 | ATTRIBUTE8 | — | — |
| 16 | ArCollectorAttribute9 | ATTRIBUTE9 | — | — |
| 17 | ArCollectorAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 18 | ArCollectorCollectorId | COLLECTOR_ID | 🔑 | ✅ |
| 19 | ArCollectorCreatedBy | CREATED_BY | — | ✅ |
| 20 | ArCollectorCreationDate | CREATION_DATE | — | ✅ |
| 21 | ArCollectorDescription | DESCRIPTION | — | ✅ |
| 22 | ArCollectorEmployeeId | EMPLOYEE_ID | — | ✅ |
| 23 | ArCollectorInactiveDate | INACTIVE_DATE | — | ✅ |
| 24 | ArCollectorLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 25 | ArCollectorLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 26 | ArCollectorLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 27 | ArCollectorName | NAME | — | ✅ |
| 28 | ArCollectorObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 29 | ArCollectorResourceId | RESOURCE_ID | — | ✅ |
| 30 | ArCollectorResourceType | RESOURCE_TYPE | — | ✅ |
| 31 | ArCollectorSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 32 | ArCollectorSetId | SET_ID | — | ✅ |
| 33 | ArCollectorStatus | STATUS | — | ✅ |
| 34 | ArCollectorTelephoneNumber | TELEPHONE_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
