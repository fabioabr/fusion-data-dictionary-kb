---
id: DOC-OTHER-PVO-SubledgerJournalEventExtractPVO
doc_type: system-doc
title: "SubledgerJournalEventExtractPVO — PVO Cross-Module"
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
  - SubledgerJournalEventExtractPVO
  - subledgerjournaleventextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SubledgerJournalEventExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Subledger Journal Event Extract. Acessa as tabelas: XLA_EVENTS.

**Caminho:** `FscmTopModelAM.FinExtractAM.XlaBiccExtractAM.SubledgerJournalEventExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 33 | 1 | 2 | 33 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[xla_events|XLA_EVENTS]] — 33 atributos (2 PKs, 33 BICC)

---

## ⚙️ Atributos

### [[xla_events|XLA_EVENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventPEOApplicationId | APPLICATION_ID | 🔑 | ✅ |
| 2 | EventPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | EventPEOEntityId | ENTITY_ID | — | ✅ |
| 4 | EventPEOEventDate | EVENT_DATE | — | ✅ |
| 5 | EventPEOEventId | EVENT_ID | 🔑 | ✅ |
| 6 | EventPEOEventNumber | EVENT_NUMBER | — | ✅ |
| 7 | EventPEOEventPEOBudgetaryControlFlag | BUDGETARY_CONTROL_FLAG | — | ✅ |
| 8 | EventPEOEventPEOCreatedBy | CREATED_BY | — | ✅ |
| 9 | EventPEOEventStatusCode | EVENT_STATUS_CODE | — | ✅ |
| 10 | EventPEOEventTypeCode | EVENT_TYPE_CODE | — | ✅ |
| 11 | EventPEOFileIdentifier | FILE_IDENTIFIER | — | ✅ |
| 12 | EventPEOHasWarningsFlag | HAS_WARNINGS_FLAG | — | ✅ |
| 13 | EventPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | EventPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 15 | EventPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | EventPEOMergeEventSetId | MERGE_EVENT_SET_ID | — | ✅ |
| 17 | EventPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 18 | EventPEOOnHoldFlag | ON_HOLD_FLAG | — | ✅ |
| 19 | EventPEOProcessStatusCode | PROCESS_STATUS_CODE | — | ✅ |
| 20 | EventPEOReferenceChar1 | REFERENCE_CHAR_1 | — | ✅ |
| 21 | EventPEOReferenceChar2 | REFERENCE_CHAR_2 | — | ✅ |
| 22 | EventPEOReferenceChar3 | REFERENCE_CHAR_3 | — | ✅ |
| 23 | EventPEOReferenceChar4 | REFERENCE_CHAR_4 | — | ✅ |
| 24 | EventPEOReferenceDate1 | REFERENCE_DATE_1 | — | ✅ |
| 25 | EventPEOReferenceDate2 | REFERENCE_DATE_2 | — | ✅ |
| 26 | EventPEOReferenceDate3 | REFERENCE_DATE_3 | — | ✅ |
| 27 | EventPEOReferenceDate4 | REFERENCE_DATE_4 | — | ✅ |
| 28 | EventPEOReferenceNum1 | REFERENCE_NUM_1 | — | ✅ |
| 29 | EventPEOReferenceNum2 | REFERENCE_NUM_2 | — | ✅ |
| 30 | EventPEOReferenceNum3 | REFERENCE_NUM_3 | — | ✅ |
| 31 | EventPEOReferenceNum4 | REFERENCE_NUM_4 | — | ✅ |
| 32 | EventPEORequestId | REQUEST_ID | — | ✅ |
| 33 | EventPEOTransactionDate | TRANSACTION_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
