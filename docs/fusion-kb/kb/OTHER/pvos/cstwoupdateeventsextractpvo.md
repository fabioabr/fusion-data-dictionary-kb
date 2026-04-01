---
id: DOC-OTHER-PVO-CstWOUpdateEventsExtractPVO
doc_type: system-doc
title: "CstWOUpdateEventsExtractPVO — PVO Cross-Module"
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
  - CstWOUpdateEventsExtractPVO
  - cstwoupdateeventsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstWOUpdateEventsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst WOUpdate Events Extract. Acessa as tabelas: CST_WO_UPDATE_EVENTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstWOUpdateEventsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 1 | 1 | 16 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_wo_update_events|CST_WO_UPDATE_EVENTS]] — 16 atributos (1 PKs, 16 BICC)

---

## ⚙️ Atributos

### [[cst_wo_update_events|CST_WO_UPDATE_EVENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstWOUpdateEventsPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | CstWOUpdateEventsPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | CstWOUpdateEventsPEOCstWoUpdateEventId | CST_WO_UPDATE_EVENT_ID | 🔑 | ✅ |
| 4 | CstWOUpdateEventsPEOCstWorkOrderId | CST_WORK_ORDER_ID | — | ✅ |
| 5 | CstWOUpdateEventsPEOEventDate | EVENT_DATE | — | ✅ |
| 6 | CstWOUpdateEventsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | CstWOUpdateEventsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | CstWOUpdateEventsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | CstWOUpdateEventsPEOLatestStatusFlag | LATEST_STATUS_FLAG | — | ✅ |
| 10 | CstWOUpdateEventsPEOPriorWoSystemStatusCode | PRIOR_WO_SYSTEM_STATUS_CODE | — | ✅ |
| 11 | CstWOUpdateEventsPEOPriorWorkOrderStatusId | PRIOR_WORK_ORDER_STATUS_ID | — | ✅ |
| 12 | CstWOUpdateEventsPEOProcessedByCaFlag | PROCESSED_BY_CA_FLAG | — | ✅ |
| 13 | CstWOUpdateEventsPEOReason | REASON | — | ✅ |
| 14 | CstWOUpdateEventsPEOTransactionDate | TRANSACTION_DATE | — | ✅ |
| 15 | CstWOUpdateEventsPEOWoSystemStatusCode | WO_SYSTEM_STATUS_CODE | — | ✅ |
| 16 | CstWOUpdateEventsPEOWorkOrderStatusId | WORK_ORDER_STATUS_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
