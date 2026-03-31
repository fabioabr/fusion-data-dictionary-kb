---
id: DOC-OTHER-PVO-QaSampleEventDispositionsExtractPVO
doc_type: system-doc
title: "QaSampleEventDispositionsExtractPVO — PVO Cross-Module"
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
  - QaSampleEventDispositionsExtractPVO
  - qasampleeventdispositionsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QaSampleEventDispositionsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Qa Sample Event Dispositions Extract. Acessa as tabelas: QA_SAMPLE_EVENT_DISPOSITIONS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.QaBiccExtractAM.QaSampleEventDispositionsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 1 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[qa_sample_event_dispositions|QA_SAMPLE_EVENT_DISPOSITIONS]] — 11 atributos (1 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[qa_sample_event_dispositions|QA_SAMPLE_EVENT_DISPOSITIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QaSampleEventDispositionsPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | QaSampleEventDispositionsPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | QaSampleEventDispositionsPEODisposition | DISPOSITION | — | ✅ |
| 4 | QaSampleEventDispositionsPEOIpEventDispositionId | IP_EVENT_DISPOSITION_ID | — | ✅ |
| 5 | QaSampleEventDispositionsPEOIpEventId | IP_EVENT_ID | — | ✅ |
| 6 | QaSampleEventDispositionsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | QaSampleEventDispositionsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | QaSampleEventDispositionsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | QaSampleEventDispositionsPEOSampleEventDispositionId | SAMPLE_EVENT_DISPOSITION_ID | 🔑 | ✅ |
| 10 | QaSampleEventDispositionsPEOSampleId | SAMPLE_ID | — | ✅ |
| 11 | QaSampleEventDispositionsPEOStatus | STATUS | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
