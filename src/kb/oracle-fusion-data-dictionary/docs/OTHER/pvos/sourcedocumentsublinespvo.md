---
id: DOC-OTHER-PVO-SourceDocumentSubLinesPVO
doc_type: system-doc
title: "SourceDocumentSubLinesPVO — PVO Cross-Module"
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
  - SourceDocumentSubLinesPVO
  - sourcedocumentsublinespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SourceDocumentSubLinesPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Source Document Sub Lines. Acessa as tabelas: VRM_SOURCE_DOC_SUB_LINES.

**Caminho:** `FscmTopModelAM.FinVrmRCSharedPublicModelAM.SourceDocumentSubLinesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 1 | 10 | 67% |

---

## 🔗 Tabelas Relacionadas

- [[vrm_source_doc_sub_lines|VRM_SOURCE_DOC_SUB_LINES]] — 15 atributos (1 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[vrm_source_doc_sub_lines|VRM_SOURCE_DOC_SUB_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SourceDocSubLinesCreatedBy | CREATED_BY | — | — |
| 2 | SourceDocSubLinesCreationDate | CREATION_DATE | — | — |
| 3 | SourceDocSubLinesDataTransformationStatus | DATA_TRANSFORMATION_STATUS | — | ✅ |
| 4 | SourceDocSubLinesDocSubLineType | DOC_SUB_LINE_TYPE | — | ✅ |
| 5 | SourceDocSubLinesDocumentLineId | DOCUMENT_LINE_ID | — | — |
| 6 | SourceDocSubLinesDocumentSubLineId | DOCUMENT_SUB_LINE_ID | 🔑 | ✅ |
| 7 | SourceDocSubLinesLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | SourceDocSubLinesLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | SourceDocSubLinesLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | SourceDocSubLinesPeriodActionCode | PERIOD_ACTION_CODE | — | ✅ |
| 11 | SourceDocSubLinesPeriodActionEventDate | PERIOD_ACTION_EVENT_DATE | — | ✅ |
| 12 | SourceDocSubLinesPrevDocumentSubLineId | PREV_DOCUMENT_SUB_LINE_ID | — | ✅ |
| 13 | SourceDocSubLinesSatisfactionEventPercent | SATISFACTION_EVENT_PERCENT | — | ✅ |
| 14 | SourceDocSubLinesSatisfactionEventQuantity | SATISFACTION_EVENT_QUANTITY | — | ✅ |
| 15 | SourceDocSubLinesSatisfactionMeasurementDate | SATISFACTION_MEASUREMENT_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
