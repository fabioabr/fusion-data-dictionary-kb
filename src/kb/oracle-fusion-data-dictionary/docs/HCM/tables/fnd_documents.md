---
id: DOC-HCM-126
doc_type: system-doc
title: "FND_DOCUMENTS — (título a preencher)"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - human-capital-management
  - data-dictionary
aliases:
  - FND_DOCUMENTS
  - fnd_documents
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# FND_DOCUMENTS

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BASE_DOCUMENT_ID | — | — | — | — | — | — |
| 2 | CREATED_BY | — | — | — | — | — | — |
| 3 | CREATION_DATE | — | — | — | — | — | — |
| 4 | DATATYPE_CODE | — | — | — | — | — | — |
| 5 | DOCUMENT_ATTRIBUTES | — | — | — | — | — | — |
| 6 | DOCUMENT_ID | — | — | — | — | — | — |
| 7 | END_DATE_ACTIVE | — | — | — | — | — | — |
| 8 | ENTERPRISE_ID | — | — | — | — | — | — |
| 9 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 10 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 11 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 12 | POST_PROCESSING_CLASS | — | — | — | — | — | — |
| 13 | POST_PROCESSING_MESSAGE | — | — | — | — | — | — |
| 14 | POST_PROCESSING_PARAMETERS | — | — | — | — | — | — |
| 15 | POST_PROCESSING_STATUS | — | — | — | — | — | — |
| 16 | PROGRAM_APPLICATION_ID | — | — | — | — | — | — |
| 17 | PROGRAM_ID | — | — | — | — | — | — |
| 18 | PROGRAM_UPDATE_DATE | — | — | — | — | — | — |
| 19 | REQUEST_ID | — | — | — | — | — | — |
| 20 | START_DATE_ACTIVE | — | — | — | — | — | — |
| 21 | USAGE_TYPE | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[attacheddocumentspvo|AttachedDocumentsPVO]] (OTHER · BICC: 16/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BASE_DOCUMENT_ID | BaseDocumentId | ✅ |
| CREATED_BY | CreatedBy2 | ✅ |
| CREATION_DATE | CreationDate2 | ✅ |
| DATATYPE_CODE | DatatypeCode | ✅ |
| DOCUMENT_ATTRIBUTES | DocumentAttributes | ✅ |
| DOCUMENT_ID | DocumentId1 | ✅ |
| END_DATE_ACTIVE | EndDateActive | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate2 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin2 | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy2 | ✅ |
| PROGRAM_APPLICATION_ID | ProgramApplicationId1 | ✅ |
| PROGRAM_ID | ProgramId1 | ✅ |
| PROGRAM_UPDATE_DATE | ProgramUpdateDate1 | ✅ |
| REQUEST_ID | RequestId1 | ✅ |
| START_DATE_ACTIVE | StartDateActive | ✅ |
| USAGE_TYPE | UsageType | ✅ |

### [[fnddocumentextractpvo|FndDocumentExtractPVO]] (HCM · BICC: 21/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BASE_DOCUMENT_ID | BaseDocumentId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DATATYPE_CODE | DatatypeCode | ✅ |
| DOCUMENT_ATTRIBUTES | DocumentAttributes | ✅ |
| DOCUMENT_ID | DocumentId | ✅ |
| END_DATE_ACTIVE | EndDateActive | ✅ |
| ENTERPRISE_ID | EnterpriseId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| POST_PROCESSING_CLASS | PostProcessingClass | ✅ |
| POST_PROCESSING_MESSAGE | PostProcessingMessage | ✅ |
| POST_PROCESSING_PARAMETERS | PostProcessingParameters | ✅ |
| POST_PROCESSING_STATUS | PostProcessingStatus | ✅ |
| PROGRAM_APPLICATION_ID | ProgramApplicationId | ✅ |
| PROGRAM_ID | ProgramId | ✅ |
| PROGRAM_UPDATE_DATE | ProgramUpdateDate | ✅ |
| REQUEST_ID | RequestId | ✅ |
| START_DATE_ACTIVE | StartDateActive | ✅ |
| USAGE_TYPE | UsageType | ✅ |
