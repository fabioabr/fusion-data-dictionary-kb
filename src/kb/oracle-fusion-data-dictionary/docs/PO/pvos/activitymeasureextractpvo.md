---
id: DOC-PO-PVO-ActivityMeasureExtractPVO
doc_type: system-doc
title: "ActivityMeasureExtractPVO — PVO Purchasing"
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
  - ActivityMeasureExtractPVO
  - activitymeasureextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ActivityMeasureExtractPVO

## 📌 Visão Geral

Extrai medidas quantitativas (volume, peso, distância) de atividades de procurement para cálculos de sustentabilidade. Fundamental para conversão de atividades em emissões equivalentes de CO2.

**Caminho:** `FscmTopModelAM.PrcExtractAM.SusBiccExtractAM.ActivityMeasureExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 1 | 12 | 92% |

---

## 🔗 Tabelas Relacionadas

- [[sus_activity_measures|SUS_ACTIVITY_MEASURES]] — 13 atributos (1 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[sus_activity_measures|SUS_ACTIVITY_MEASURES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActivityId | ACTIVITY_ID | — | ✅ |
| 2 | ActivityMeasureId | ACTIVITY_MEASURE_ID | 🔑 | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | Measure | MEASURE | — | ✅ |
| 10 | MeasureTypeCode | MEASURE_TYPE_CODE | — | ✅ |
| 11 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | StatusCode | STATUS_CODE | — | — |
| 13 | UOMCode | UOM_CODE | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
