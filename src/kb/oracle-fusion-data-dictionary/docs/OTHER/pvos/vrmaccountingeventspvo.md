---
id: DOC-OTHER-PVO-VrmAccountingEventsPVO
doc_type: system-doc
title: "VrmAccountingEventsPVO — PVO Cross-Module"
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
  - VrmAccountingEventsPVO
  - vrmaccountingeventspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# VrmAccountingEventsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Vrm Accounting Events. Acessa as tabelas: VRM_ACCOUNTING_EVENTS.

**Caminho:** `FscmTopModelAM.FinVrmRRSharedPublicModelAM.VrmAccountingEventsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 55 | 1 | 1 | 8 | 15% |

---

## 🔗 Tabelas Relacionadas

- [[vrm_accounting_events|VRM_ACCOUNTING_EVENTS]] — 55 atributos (1 PKs, 8 BICC)

---

## ⚙️ Atributos

### [[vrm_accounting_events|VRM_ACCOUNTING_EVENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccountingEventId | ACCOUNTING_EVENT_ID | 🔑 | ✅ |
| 2 | VrmAccountingEventsAccountingDate | ACCOUNTING_DATE | — | ✅ |
| 3 | VrmAccountingEventsAccountingEventSeqNumber | ACCOUNTING_EVENT_SEQ_NUMBER | — | — |
| 4 | VrmAccountingEventsAccountingEventTypeCode | ACCOUNTING_EVENT_TYPE_CODE | — | ✅ |
| 5 | VrmAccountingEventsAcctdAmount | ACCTD_AMOUNT | — | — |
| 6 | VrmAccountingEventsAmount | AMOUNT | — | — |
| 7 | VrmAccountingEventsAttribute1 | ATTRIBUTE1 | — | — |
| 8 | VrmAccountingEventsAttribute10 | ATTRIBUTE10 | — | — |
| 9 | VrmAccountingEventsAttribute11 | ATTRIBUTE11 | — | — |
| 10 | VrmAccountingEventsAttribute12 | ATTRIBUTE12 | — | — |
| 11 | VrmAccountingEventsAttribute13 | ATTRIBUTE13 | — | — |
| 12 | VrmAccountingEventsAttribute14 | ATTRIBUTE14 | — | — |
| 13 | VrmAccountingEventsAttribute15 | ATTRIBUTE15 | — | — |
| 14 | VrmAccountingEventsAttribute16 | ATTRIBUTE16 | — | — |
| 15 | VrmAccountingEventsAttribute17 | ATTRIBUTE17 | — | — |
| 16 | VrmAccountingEventsAttribute18 | ATTRIBUTE18 | — | — |
| 17 | VrmAccountingEventsAttribute19 | ATTRIBUTE19 | — | — |
| 18 | VrmAccountingEventsAttribute2 | ATTRIBUTE2 | — | — |
| 19 | VrmAccountingEventsAttribute20 | ATTRIBUTE20 | — | — |
| 20 | VrmAccountingEventsAttribute3 | ATTRIBUTE3 | — | — |
| 21 | VrmAccountingEventsAttribute4 | ATTRIBUTE4 | — | — |
| 22 | VrmAccountingEventsAttribute5 | ATTRIBUTE5 | — | — |
| 23 | VrmAccountingEventsAttribute6 | ATTRIBUTE6 | — | — |
| 24 | VrmAccountingEventsAttribute7 | ATTRIBUTE7 | — | — |
| 25 | VrmAccountingEventsAttribute8 | ATTRIBUTE8 | — | — |
| 26 | VrmAccountingEventsAttribute9 | ATTRIBUTE9 | — | — |
| 27 | VrmAccountingEventsAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 28 | VrmAccountingEventsAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 29 | VrmAccountingEventsAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 30 | VrmAccountingEventsAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 31 | VrmAccountingEventsAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 32 | VrmAccountingEventsAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 33 | VrmAccountingEventsAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 34 | VrmAccountingEventsAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 35 | VrmAccountingEventsAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 36 | VrmAccountingEventsAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 37 | VrmAccountingEventsAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 38 | VrmAccountingEventsContractActivityGroupId | CONTRACT_ACTIVITY_GROUP_ID | — | — |
| 39 | VrmAccountingEventsCreatedBy | CREATED_BY | — | — |
| 40 | VrmAccountingEventsCreatedFrom | CREATED_FROM | — | — |
| 41 | VrmAccountingEventsCreationDate | CREATION_DATE | — | — |
| 42 | VrmAccountingEventsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 43 | VrmAccountingEventsLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 44 | VrmAccountingEventsLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 45 | VrmAccountingEventsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 46 | VrmAccountingEventsPerfObligationId | PERF_OBLIGATION_ID | — | — |
| 47 | VrmAccountingEventsPerfObligationLineId | PERF_OBLIGATION_LINE_ID | — | — |
| 48 | VrmAccountingEventsPobFirstBeFlag | POB_FIRST_BE_FLAG | — | ✅ |
| 49 | VrmAccountingEventsPobLastSeFlag | POB_LAST_SE_FLAG | — | ✅ |
| 50 | VrmAccountingEventsProcessStatusCode | PROCESS_STATUS_CODE | — | ✅ |
| 51 | VrmAccountingEventsProcessedRequestId | PROCESSED_REQUEST_ID | — | — |
| 52 | VrmAccountingEventsReferenceEventId | REFERENCE_EVENT_ID | — | — |
| 53 | VrmAccountingEventsRequestId | REQUEST_ID | — | — |
| 54 | VrmAccountingEventsReversedFlag | REVERSED_FLAG | — | ✅ |
| 55 | VrmAccountingEventsReversedRequestId | REVERSED_REQUEST_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
