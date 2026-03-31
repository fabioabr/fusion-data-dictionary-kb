---
id: DOC-OTHER-PVO-FndDocumentExtractPVO
doc_type: system-doc
title: "FndDocumentExtractPVO — PVO Cross-Module"
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
  - FndDocumentExtractPVO
  - fnddocumentextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FndDocumentExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fnd Document Extract. Acessa as tabelas: FND_DOCUMENTS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.CommonBiccExtractAM.FndDocumentExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 1 | 2 | 21 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_documents|FND_DOCUMENTS]] — 21 atributos (2 PKs, 21 BICC)

---

## ⚙️ Atributos

### [[fnd_documents|FND_DOCUMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BaseDocumentId | BASE_DOCUMENT_ID | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | DatatypeCode | DATATYPE_CODE | — | ✅ |
| 5 | DocumentAttributes | DOCUMENT_ATTRIBUTES | — | ✅ |
| 6 | DocumentId | DOCUMENT_ID | 🔑 | ✅ |
| 7 | EndDateActive | END_DATE_ACTIVE | — | ✅ |
| 8 | EnterpriseId | ENTERPRISE_ID | 🔑 | ✅ |
| 9 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | PostProcessingClass | POST_PROCESSING_CLASS | — | ✅ |
| 13 | PostProcessingMessage | POST_PROCESSING_MESSAGE | — | ✅ |
| 14 | PostProcessingParameters | POST_PROCESSING_PARAMETERS | — | ✅ |
| 15 | PostProcessingStatus | POST_PROCESSING_STATUS | — | ✅ |
| 16 | ProgramApplicationId | PROGRAM_APPLICATION_ID | — | ✅ |
| 17 | ProgramId | PROGRAM_ID | — | ✅ |
| 18 | ProgramUpdateDate | PROGRAM_UPDATE_DATE | — | ✅ |
| 19 | RequestId | REQUEST_ID | — | ✅ |
| 20 | StartDateActive | START_DATE_ACTIVE | — | ✅ |
| 21 | UsageType | USAGE_TYPE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
