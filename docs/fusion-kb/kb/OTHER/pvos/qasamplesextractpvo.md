---
id: DOC-OTHER-PVO-QaSamplesExtractPVO
doc_type: system-doc
title: "QaSamplesExtractPVO — PVO Cross-Module"
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
  - QaSamplesExtractPVO
  - qasamplesextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QaSamplesExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Qa Samples Extract. Acessa as tabelas: QA_SAMPLES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.QaBiccExtractAM.QaSamplesExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 1 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[qa_samples|QA_SAMPLES]] — 13 atributos (1 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[qa_samples|QA_SAMPLES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QaSamplesPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | QaSamplesPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | QaSamplesPEOIpEventId | IP_EVENT_ID | — | ✅ |
| 4 | QaSamplesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | QaSamplesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | QaSamplesPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | QaSamplesPEOOriginalDisposition | ORIGINAL_DISPOSITION | — | ✅ |
| 8 | QaSamplesPEOQuantity | QUANTITY | — | ✅ |
| 9 | QaSamplesPEOSampleId | SAMPLE_ID | 🔑 | ✅ |
| 10 | QaSamplesPEOSampleNumber | SAMPLE_NUMBER | — | ✅ |
| 11 | QaSamplesPEOSerialNumber | SERIAL_NUMBER | — | ✅ |
| 12 | QaSamplesPEOUomCode | UOM_CODE | — | ✅ |
| 13 | QaSamplesPEOWoOperationTxnId | WO_OPERATION_TXN_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
