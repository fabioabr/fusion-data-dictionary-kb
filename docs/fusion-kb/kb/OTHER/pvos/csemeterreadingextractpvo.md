---
id: DOC-OTHER-PVO-CseMeterReadingExtractPVO
doc_type: system-doc
title: "CseMeterReadingExtractPVO — PVO Cross-Module"
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
  - CseMeterReadingExtractPVO
  - csemeterreadingextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CseMeterReadingExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cse Meter Reading Extract. Acessa as tabelas: CSE_METER_READINGS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CseBiccExtractAM.CseMeterReadingExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 30 | 1 | 1 | 30 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cse_meter_readings|CSE_METER_READINGS]] — 30 atributos (1 PKs, 30 BICC)

---

## ⚙️ Atributos

### [[cse_meter_readings|CSE_METER_READINGS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 2 | CanceledFlag | CANCELED_FLAG | — | ✅ |
| 3 | Comments | COMMENTS | — | ✅ |
| 4 | CorpCurrencyCode | CORP_CURRENCY_CODE | — | ✅ |
| 5 | CreatedBy | CREATED_BY | — | ✅ |
| 6 | CreationDate | CREATION_DATE | — | ✅ |
| 7 | CurcyConvRateType | CURCY_CONV_RATE_TYPE | — | ✅ |
| 8 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 9 | DisabledFlag | DISABLED_FLAG | — | ✅ |
| 10 | DisplayedValue | DISPLAYED_VALUE | — | ✅ |
| 11 | InitialFlag | INITIAL_FLAG | — | ✅ |
| 12 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 13 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 14 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 16 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 17 | MeterId | METER_ID | — | ✅ |
| 18 | MeterReadingId | METER_READING_ID | 🔑 | ✅ |
| 19 | ModifiedFlag | MODIFIED_FLAG | — | ✅ |
| 20 | NetValue | NET_VALUE | — | ✅ |
| 21 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 22 | ReadingDate | READING_DATE | — | ✅ |
| 23 | ReadingNetChange | READING_NET_CHANGE | — | ✅ |
| 24 | ReadingTypeCode | READING_TYPE_CODE | — | ✅ |
| 25 | ReadingValue | READING_VALUE | — | ✅ |
| 26 | ReferenceReadingId | REFERENCE_READING_ID | — | ✅ |
| 27 | RequestId | REQUEST_ID | — | ✅ |
| 28 | ResetFlag | RESET_FLAG | — | ✅ |
| 29 | RolloverFlag | ROLLOVER_FLAG | — | ✅ |
| 30 | WorkOrderId | WORK_ORDER_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
