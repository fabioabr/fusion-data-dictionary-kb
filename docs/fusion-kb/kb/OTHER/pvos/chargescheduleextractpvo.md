---
id: DOC-OTHER-PVO-ChargeScheduleExtractPVO
doc_type: system-doc
title: "ChargeScheduleExtractPVO — PVO Cross-Module"
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
  - ChargeScheduleExtractPVO
  - chargescheduleextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ChargeScheduleExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Charge Schedule Extract. Acessa as tabelas: AR_CHARGE_SCHEDULES.

**Caminho:** `FscmTopModelAM.FinExtractAM.ArBiccExtractAM.ChargeScheduleExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 25 | 1 | 1 | 9 | 36% |

---

## 🔗 Tabelas Relacionadas

- [[ar_charge_schedules|AR_CHARGE_SCHEDULES]] — 25 atributos (1 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[ar_charge_schedules|AR_CHARGE_SCHEDULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ArChargeScheduleAttribute1 | ATTRIBUTE1 | — | — |
| 2 | ArChargeScheduleAttribute10 | ATTRIBUTE10 | — | — |
| 3 | ArChargeScheduleAttribute11 | ATTRIBUTE11 | — | — |
| 4 | ArChargeScheduleAttribute12 | ATTRIBUTE12 | — | — |
| 5 | ArChargeScheduleAttribute13 | ATTRIBUTE13 | — | — |
| 6 | ArChargeScheduleAttribute14 | ATTRIBUTE14 | — | — |
| 7 | ArChargeScheduleAttribute15 | ATTRIBUTE15 | — | — |
| 8 | ArChargeScheduleAttribute2 | ATTRIBUTE2 | — | — |
| 9 | ArChargeScheduleAttribute3 | ATTRIBUTE3 | — | — |
| 10 | ArChargeScheduleAttribute4 | ATTRIBUTE4 | — | — |
| 11 | ArChargeScheduleAttribute5 | ATTRIBUTE5 | — | — |
| 12 | ArChargeScheduleAttribute6 | ATTRIBUTE6 | — | — |
| 13 | ArChargeScheduleAttribute7 | ATTRIBUTE7 | — | — |
| 14 | ArChargeScheduleAttribute8 | ATTRIBUTE8 | — | — |
| 15 | ArChargeScheduleAttribute9 | ATTRIBUTE9 | — | — |
| 16 | ArChargeScheduleAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 17 | ArChargeScheduleCreatedBy | CREATED_BY | — | ✅ |
| 18 | ArChargeScheduleCreationDate | CREATION_DATE | — | ✅ |
| 19 | ArChargeScheduleLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 20 | ArChargeScheduleLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 21 | ArChargeScheduleLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 22 | ArChargeScheduleObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 23 | ArChargeScheduleScheduleDescription | SCHEDULE_DESCRIPTION | — | ✅ |
| 24 | ArChargeScheduleScheduleId | SCHEDULE_ID | 🔑 | ✅ |
| 25 | ArChargeScheduleScheduleName | SCHEDULE_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
