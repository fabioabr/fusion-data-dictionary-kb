---
id: DOC-OTHER-PVO-ChargeScheduleLineExtractPVO
doc_type: system-doc
title: "ChargeScheduleLineExtractPVO — PVO Cross-Module"
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
  - ChargeScheduleLineExtractPVO
  - chargeschedulelineextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ChargeScheduleLineExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Charge Schedule Line Extract. Acessa as tabelas: AR_CHARGE_SCHEDULE_LINES.

**Caminho:** `FscmTopModelAM.FinExtractAM.ArBiccExtractAM.ChargeScheduleLineExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 29 | 1 | 1 | 13 | 45% |

---

## 🔗 Tabelas Relacionadas

- [[ar_charge_schedule_lines|AR_CHARGE_SCHEDULE_LINES]] — 29 atributos (1 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[ar_charge_schedule_lines|AR_CHARGE_SCHEDULE_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ArChargeScheduleLineAgingBucketId | AGING_BUCKET_ID | — | ✅ |
| 2 | ArChargeScheduleLineAgingBucketLineId | AGING_BUCKET_LINE_ID | — | ✅ |
| 3 | ArChargeScheduleLineAmount | AMOUNT | — | ✅ |
| 4 | ArChargeScheduleLineAttribute1 | ATTRIBUTE1 | — | — |
| 5 | ArChargeScheduleLineAttribute10 | ATTRIBUTE10 | — | — |
| 6 | ArChargeScheduleLineAttribute11 | ATTRIBUTE11 | — | — |
| 7 | ArChargeScheduleLineAttribute12 | ATTRIBUTE12 | — | — |
| 8 | ArChargeScheduleLineAttribute13 | ATTRIBUTE13 | — | — |
| 9 | ArChargeScheduleLineAttribute14 | ATTRIBUTE14 | — | — |
| 10 | ArChargeScheduleLineAttribute15 | ATTRIBUTE15 | — | — |
| 11 | ArChargeScheduleLineAttribute2 | ATTRIBUTE2 | — | — |
| 12 | ArChargeScheduleLineAttribute3 | ATTRIBUTE3 | — | — |
| 13 | ArChargeScheduleLineAttribute4 | ATTRIBUTE4 | — | — |
| 14 | ArChargeScheduleLineAttribute5 | ATTRIBUTE5 | — | — |
| 15 | ArChargeScheduleLineAttribute6 | ATTRIBUTE6 | — | — |
| 16 | ArChargeScheduleLineAttribute7 | ATTRIBUTE7 | — | — |
| 17 | ArChargeScheduleLineAttribute8 | ATTRIBUTE8 | — | — |
| 18 | ArChargeScheduleLineAttribute9 | ATTRIBUTE9 | — | — |
| 19 | ArChargeScheduleLineAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 20 | ArChargeScheduleLineCreatedBy | CREATED_BY | — | ✅ |
| 21 | ArChargeScheduleLineCreationDate | CREATION_DATE | — | ✅ |
| 22 | ArChargeScheduleLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 23 | ArChargeScheduleLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 24 | ArChargeScheduleLineLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 25 | ArChargeScheduleLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 26 | ArChargeScheduleLineRate | RATE | — | ✅ |
| 27 | ArChargeScheduleLineScheduleHeaderId | SCHEDULE_HEADER_ID | — | ✅ |
| 28 | ArChargeScheduleLineScheduleId | SCHEDULE_ID | — | ✅ |
| 29 | ArChargeScheduleLineScheduleLineId | SCHEDULE_LINE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
