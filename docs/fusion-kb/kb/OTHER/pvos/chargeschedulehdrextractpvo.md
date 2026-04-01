---
id: DOC-OTHER-PVO-ChargeScheduleHDRExtractPVO
doc_type: system-doc
title: "ChargeScheduleHDRExtractPVO — PVO Cross-Module"
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
  - ChargeScheduleHDRExtractPVO
  - chargeschedulehdrextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ChargeScheduleHDRExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Charge Schedule HDRExtract. Acessa as tabelas: AR_CHARGE_SCHEDULE_HDRS.

**Caminho:** `FscmTopModelAM.FinExtractAM.ArBiccExtractAM.ChargeScheduleHDRExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 29 | 1 | 2 | 13 | 45% |

---

## 🔗 Tabelas Relacionadas

- [[ar_charge_schedule_hdrs|AR_CHARGE_SCHEDULE_HDRS]] — 29 atributos (2 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[ar_charge_schedule_hdrs|AR_CHARGE_SCHEDULE_HDRS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ArChargeScheduleHDRAgingBucketId | AGING_BUCKET_ID | — | ✅ |
| 2 | ArChargeScheduleHDRAttribute1 | ATTRIBUTE1 | — | — |
| 3 | ArChargeScheduleHDRAttribute10 | ATTRIBUTE10 | — | — |
| 4 | ArChargeScheduleHDRAttribute11 | ATTRIBUTE11 | — | — |
| 5 | ArChargeScheduleHDRAttribute12 | ATTRIBUTE12 | — | — |
| 6 | ArChargeScheduleHDRAttribute13 | ATTRIBUTE13 | — | — |
| 7 | ArChargeScheduleHDRAttribute14 | ATTRIBUTE14 | — | — |
| 8 | ArChargeScheduleHDRAttribute15 | ATTRIBUTE15 | — | — |
| 9 | ArChargeScheduleHDRAttribute2 | ATTRIBUTE2 | — | — |
| 10 | ArChargeScheduleHDRAttribute3 | ATTRIBUTE3 | — | — |
| 11 | ArChargeScheduleHDRAttribute4 | ATTRIBUTE4 | — | — |
| 12 | ArChargeScheduleHDRAttribute5 | ATTRIBUTE5 | — | — |
| 13 | ArChargeScheduleHDRAttribute6 | ATTRIBUTE6 | — | — |
| 14 | ArChargeScheduleHDRAttribute7 | ATTRIBUTE7 | — | — |
| 15 | ArChargeScheduleHDRAttribute8 | ATTRIBUTE8 | — | — |
| 16 | ArChargeScheduleHDRAttribute9 | ATTRIBUTE9 | — | — |
| 17 | ArChargeScheduleHDRAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 18 | ArChargeScheduleHDRCreatedBy | CREATED_BY | — | ✅ |
| 19 | ArChargeScheduleHDRCreationDate | CREATION_DATE | — | ✅ |
| 20 | ArChargeScheduleHDREndDate | END_DATE | — | ✅ |
| 21 | ArChargeScheduleHDRLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 22 | ArChargeScheduleHDRLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 23 | ArChargeScheduleHDRLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 24 | ArChargeScheduleHDRObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 25 | ArChargeScheduleHDRScheduleHeaderId | SCHEDULE_HEADER_ID | 🔑 | ✅ |
| 26 | ArChargeScheduleHDRScheduleHeaderType | SCHEDULE_HEADER_TYPE | — | ✅ |
| 27 | ArChargeScheduleHDRScheduleId | SCHEDULE_ID | 🔑 | ✅ |
| 28 | ArChargeScheduleHDRStartDate | START_DATE | — | ✅ |
| 29 | ArChargeScheduleHDRStatus | STATUS | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
