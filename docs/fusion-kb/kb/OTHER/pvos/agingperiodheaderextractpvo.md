---
id: DOC-OTHER-PVO-AgingPeriodHeaderExtractPVO
doc_type: system-doc
title: "AgingPeriodHeaderExtractPVO — PVO Cross-Module"
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
  - AgingPeriodHeaderExtractPVO
  - agingperiodheaderextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AgingPeriodHeaderExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Aging Period Header Extract. Acessa as tabelas: AP_AGING_PERIODS.

**Caminho:** `FscmTopModelAM.FinExtractAM.ApBiccExtractAM.AgingPeriodHeaderExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 26 | 1 | 1 | 11 | 42% |

---

## 🔗 Tabelas Relacionadas

- [[ap_aging_periods|AP_AGING_PERIODS]] — 26 atributos (1 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[ap_aging_periods|AP_AGING_PERIODS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApAgingPeriodsAgingPeriodId | AGING_PERIOD_ID | 🔑 | ✅ |
| 2 | ApAgingPeriodsAttribute1 | ATTRIBUTE1 | — | — |
| 3 | ApAgingPeriodsAttribute10 | ATTRIBUTE10 | — | — |
| 4 | ApAgingPeriodsAttribute11 | ATTRIBUTE11 | — | — |
| 5 | ApAgingPeriodsAttribute12 | ATTRIBUTE12 | — | — |
| 6 | ApAgingPeriodsAttribute13 | ATTRIBUTE13 | — | — |
| 7 | ApAgingPeriodsAttribute14 | ATTRIBUTE14 | — | — |
| 8 | ApAgingPeriodsAttribute15 | ATTRIBUTE15 | — | — |
| 9 | ApAgingPeriodsAttribute2 | ATTRIBUTE2 | — | — |
| 10 | ApAgingPeriodsAttribute3 | ATTRIBUTE3 | — | — |
| 11 | ApAgingPeriodsAttribute4 | ATTRIBUTE4 | — | — |
| 12 | ApAgingPeriodsAttribute5 | ATTRIBUTE5 | — | — |
| 13 | ApAgingPeriodsAttribute6 | ATTRIBUTE6 | — | — |
| 14 | ApAgingPeriodsAttribute7 | ATTRIBUTE7 | — | — |
| 15 | ApAgingPeriodsAttribute8 | ATTRIBUTE8 | — | — |
| 16 | ApAgingPeriodsAttribute9 | ATTRIBUTE9 | — | — |
| 17 | ApAgingPeriodsAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 18 | ApAgingPeriodsCreatedBy | CREATED_BY | — | ✅ |
| 19 | ApAgingPeriodsCreationDate | CREATION_DATE | — | ✅ |
| 20 | ApAgingPeriodsDescription | DESCRIPTION | — | ✅ |
| 21 | ApAgingPeriodsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 22 | ApAgingPeriodsLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 23 | ApAgingPeriodsLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 24 | ApAgingPeriodsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 25 | ApAgingPeriodsPeriodName | PERIOD_NAME | — | ✅ |
| 26 | ApAgingPeriodsStatus | STATUS | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
