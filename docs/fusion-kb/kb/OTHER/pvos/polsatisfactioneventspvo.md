---
id: DOC-OTHER-PVO-PolSatisfactionEventsPVO
doc_type: system-doc
title: "PolSatisfactionEventsPVO — PVO Cross-Module"
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
  - PolSatisfactionEventsPVO
  - polsatisfactioneventspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PolSatisfactionEventsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Pol Satisfaction Events. Acessa as tabelas: VRM_POL_SATISFACTION_EVENTS, VRM_SOURCE_DOC_SUB_LINES.

**Caminho:** `FscmTopModelAM.FinVrmRRSharedPublicModelAM.PolSatisfactionEventsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 63 | 2 | 1 | 19 | 30% |

---

## 🔗 Tabelas Relacionadas

- [[vrm_pol_satisfaction_events|VRM_POL_SATISFACTION_EVENTS]] — 59 atributos (1 PKs, 16 BICC)
- [[vrm_source_doc_sub_lines|VRM_SOURCE_DOC_SUB_LINES]] — 4 atributos (3 BICC)

---

## ⚙️ Atributos

### [[vrm_pol_satisfaction_events|VRM_POL_SATISFACTION_EVENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PolSatisfactionEventId | POL_SATISFACTION_EVENT_ID | 🔑 | ✅ |
| 2 | PolSatisfactionEventsAttribute1 | ATTRIBUTE1 | — | — |
| 3 | PolSatisfactionEventsAttribute10 | ATTRIBUTE10 | — | — |
| 4 | PolSatisfactionEventsAttribute11 | ATTRIBUTE11 | — | — |
| 5 | PolSatisfactionEventsAttribute12 | ATTRIBUTE12 | — | — |
| 6 | PolSatisfactionEventsAttribute13 | ATTRIBUTE13 | — | — |
| 7 | PolSatisfactionEventsAttribute14 | ATTRIBUTE14 | — | — |
| 8 | PolSatisfactionEventsAttribute15 | ATTRIBUTE15 | — | — |
| 9 | PolSatisfactionEventsAttribute16 | ATTRIBUTE16 | — | — |
| 10 | PolSatisfactionEventsAttribute17 | ATTRIBUTE17 | — | — |
| 11 | PolSatisfactionEventsAttribute18 | ATTRIBUTE18 | — | — |
| 12 | PolSatisfactionEventsAttribute19 | ATTRIBUTE19 | — | — |
| 13 | PolSatisfactionEventsAttribute2 | ATTRIBUTE2 | — | — |
| 14 | PolSatisfactionEventsAttribute20 | ATTRIBUTE20 | — | — |
| 15 | PolSatisfactionEventsAttribute3 | ATTRIBUTE3 | — | — |
| 16 | PolSatisfactionEventsAttribute4 | ATTRIBUTE4 | — | — |
| 17 | PolSatisfactionEventsAttribute5 | ATTRIBUTE5 | — | — |
| 18 | PolSatisfactionEventsAttribute6 | ATTRIBUTE6 | — | — |
| 19 | PolSatisfactionEventsAttribute7 | ATTRIBUTE7 | — | — |
| 20 | PolSatisfactionEventsAttribute8 | ATTRIBUTE8 | — | — |
| 21 | PolSatisfactionEventsAttribute9 | ATTRIBUTE9 | — | — |
| 22 | PolSatisfactionEventsAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 23 | PolSatisfactionEventsAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 24 | PolSatisfactionEventsAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 25 | PolSatisfactionEventsAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 26 | PolSatisfactionEventsAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 27 | PolSatisfactionEventsAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 28 | PolSatisfactionEventsAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 29 | PolSatisfactionEventsAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 30 | PolSatisfactionEventsAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 31 | PolSatisfactionEventsAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 32 | PolSatisfactionEventsAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 33 | PolSatisfactionEventsComments | COMMENTS | — | — |
| 34 | PolSatisfactionEventsCreatedBy | CREATED_BY | — | — |
| 35 | PolSatisfactionEventsCreatedFrom | CREATED_FROM | — | — |
| 36 | PolSatisfactionEventsCreationDate | CREATION_DATE | — | — |
| 37 | PolSatisfactionEventsDiscardedDate | DISCARDED_DATE | — | ✅ |
| 38 | PolSatisfactionEventsDiscardedFlag | DISCARDED_FLAG | — | ✅ |
| 39 | PolSatisfactionEventsDocumentLineId | DOCUMENT_LINE_ID | — | — |
| 40 | PolSatisfactionEventsDocumentSubLineId | DOCUMENT_SUB_LINE_ID | — | — |
| 41 | PolSatisfactionEventsHoldFlag | HOLD_FLAG | — | ✅ |
| 42 | PolSatisfactionEventsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 43 | PolSatisfactionEventsLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 44 | PolSatisfactionEventsLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 45 | PolSatisfactionEventsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 46 | PolSatisfactionEventsPerfObligationLineId | PERF_OBLIGATION_LINE_ID | — | — |
| 47 | PolSatisfactionEventsProcessedAmount | PROCESSED_AMOUNT | — | ✅ |
| 48 | PolSatisfactionEventsProcessedFlag | PROCESSED_FLAG | — | ✅ |
| 49 | PolSatisfactionEventsProcessedPeriodProportion | PROCESSED_PERIOD_PROPORTION | — | ✅ |
| 50 | PolSatisfactionEventsProcessedRequestId | PROCESSED_REQUEST_ID | — | — |
| 51 | PolSatisfactionEventsRequestId | REQUEST_ID | — | — |
| 52 | PolSatisfactionEventsSatisfactionMeasurementDate | SATISFACTION_MEASUREMENT_DATE | — | ✅ |
| 53 | PolSatisfactionEventsSatisfactionMeasurementNum | SATISFACTION_MEASUREMENT_NUM | — | ✅ |
| 54 | PolSatisfactionEventsSatisfactionPercent | SATISFACTION_PERCENT | — | ✅ |
| 55 | PolSatisfactionEventsSatisfactionPeriodEndDate | SATISFACTION_PERIOD_END_DATE | — | ✅ |
| 56 | PolSatisfactionEventsSatisfactionPeriodProportion | SATISFACTION_PERIOD_PROPORTION | — | ✅ |
| 57 | PolSatisfactionEventsSatisfactionPeriodStartDate | SATISFACTION_PERIOD_START_DATE | — | ✅ |
| 58 | PolSatisfactionEventsSatisfactionQuantity | SATISFACTION_QUANTITY | — | ✅ |
| 59 | PolSatisfactionEventsSplitFlag | SPLIT_FLAG | — | ✅ |

### [[vrm_source_doc_sub_lines|VRM_SOURCE_DOC_SUB_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SourceDocSubLinesDocumentSubLineId | DOCUMENT_SUB_LINE_ID | — | — |
| 2 | SourceDocSubLinesPeriodActionCode | PERIOD_ACTION_CODE | — | ✅ |
| 3 | SourceDocSubLinesPeriodActionEventDate | PERIOD_ACTION_EVENT_DATE | — | ✅ |
| 4 | SourceDocSubLinesPrevDocumentSubLineId | PREV_DOCUMENT_SUB_LINE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
