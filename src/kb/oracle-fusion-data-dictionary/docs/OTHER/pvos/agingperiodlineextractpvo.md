---
id: DOC-OTHER-PVO-AgingPeriodLineExtractPVO
doc_type: system-doc
title: "AgingPeriodLineExtractPVO — PVO Cross-Module"
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
  - AgingPeriodLineExtractPVO
  - agingperiodlineextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AgingPeriodLineExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Aging Period Line Extract. Acessa as tabelas: AP_AGING_PERIOD_LINES.

**Caminho:** `FscmTopModelAM.FinExtractAM.ApBiccExtractAM.AgingPeriodLineExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 31 | 1 | 1 | 15 | 48% |

---

## 🔗 Tabelas Relacionadas

- [[ap_aging_period_lines|AP_AGING_PERIOD_LINES]] — 31 atributos (1 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[ap_aging_period_lines|AP_AGING_PERIOD_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApAgingPeriodLinesAgingPeriodId | AGING_PERIOD_ID | — | ✅ |
| 2 | ApAgingPeriodLinesAgingPeriodLineId | AGING_PERIOD_LINE_ID | 🔑 | ✅ |
| 3 | ApAgingPeriodLinesAttribute1 | ATTRIBUTE1 | — | — |
| 4 | ApAgingPeriodLinesAttribute10 | ATTRIBUTE10 | — | — |
| 5 | ApAgingPeriodLinesAttribute11 | ATTRIBUTE11 | — | — |
| 6 | ApAgingPeriodLinesAttribute12 | ATTRIBUTE12 | — | — |
| 7 | ApAgingPeriodLinesAttribute13 | ATTRIBUTE13 | — | — |
| 8 | ApAgingPeriodLinesAttribute14 | ATTRIBUTE14 | — | — |
| 9 | ApAgingPeriodLinesAttribute15 | ATTRIBUTE15 | — | — |
| 10 | ApAgingPeriodLinesAttribute2 | ATTRIBUTE2 | — | — |
| 11 | ApAgingPeriodLinesAttribute3 | ATTRIBUTE3 | — | — |
| 12 | ApAgingPeriodLinesAttribute4 | ATTRIBUTE4 | — | — |
| 13 | ApAgingPeriodLinesAttribute5 | ATTRIBUTE5 | — | — |
| 14 | ApAgingPeriodLinesAttribute6 | ATTRIBUTE6 | — | — |
| 15 | ApAgingPeriodLinesAttribute7 | ATTRIBUTE7 | — | — |
| 16 | ApAgingPeriodLinesAttribute8 | ATTRIBUTE8 | — | — |
| 17 | ApAgingPeriodLinesAttribute9 | ATTRIBUTE9 | — | — |
| 18 | ApAgingPeriodLinesAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 19 | ApAgingPeriodLinesCreatedBy | CREATED_BY | — | ✅ |
| 20 | ApAgingPeriodLinesCreationDate | CREATION_DATE | — | ✅ |
| 21 | ApAgingPeriodLinesDaysStart | DAYS_START | — | ✅ |
| 22 | ApAgingPeriodLinesDaysTo | DAYS_TO | — | ✅ |
| 23 | ApAgingPeriodLinesLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 24 | ApAgingPeriodLinesLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 25 | ApAgingPeriodLinesLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 26 | ApAgingPeriodLinesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 27 | ApAgingPeriodLinesPeriodSequenceNum | PERIOD_SEQUENCE_NUM | — | ✅ |
| 28 | ApAgingPeriodLinesReportHeading1 | REPORT_HEADING1 | — | ✅ |
| 29 | ApAgingPeriodLinesReportHeading2 | REPORT_HEADING2 | — | ✅ |
| 30 | ApAgingPeriodLinesReportHeading3 | REPORT_HEADING3 | — | ✅ |
| 31 | ApAgingPeriodLinesType | TYPE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
