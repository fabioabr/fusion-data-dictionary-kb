---
id: DOC-OTHER-PVO-QaIpEventDispositionExtractPVO
doc_type: system-doc
title: "QaIpEventDispositionExtractPVO — PVO Cross-Module"
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
  - QaIpEventDispositionExtractPVO
  - qaipeventdispositionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QaIpEventDispositionExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Qa Ip Event Disposition Extract. Acessa as tabelas: QA_IP_EVENT_DISPOSITIONS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.QaBiccExtractAM.QaIpEventDispositionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 1 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[qa_ip_event_dispositions|QA_IP_EVENT_DISPOSITIONS]] — 13 atributos (1 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[qa_ip_event_dispositions|QA_IP_EVENT_DISPOSITIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QaIpEventDispositionsPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | QaIpEventDispositionsPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | QaIpEventDispositionsPEODisposition | DISPOSITION | — | ✅ |
| 4 | QaIpEventDispositionsPEOInspectionPlanId | INSPECTION_PLAN_ID | — | ✅ |
| 5 | QaIpEventDispositionsPEOIpEventDispositionId | IP_EVENT_DISPOSITION_ID | 🔑 | ✅ |
| 6 | QaIpEventDispositionsPEOIpEventId | IP_EVENT_ID | — | ✅ |
| 7 | QaIpEventDispositionsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | QaIpEventDispositionsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | QaIpEventDispositionsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | QaIpEventDispositionsPEOQuantity | QUANTITY | — | ✅ |
| 11 | QaIpEventDispositionsPEORcvIntTxnId | RCV_INT_TXN_ID | — | ✅ |
| 12 | QaIpEventDispositionsPEORcvTransactionId | RCV_TRANSACTION_ID | — | ✅ |
| 13 | QaIpEventDispositionsPEOWoOperationTxnId | WO_OPERATION_TXN_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
