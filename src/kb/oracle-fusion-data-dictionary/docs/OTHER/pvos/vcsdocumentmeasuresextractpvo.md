---
id: DOC-OTHER-PVO-VcsDocumentMeasuresExtractPVO
doc_type: system-doc
title: "VcsDocumentMeasuresExtractPVO — PVO Cross-Module"
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
  - VcsDocumentMeasuresExtractPVO
  - vcsdocumentmeasuresextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# VcsDocumentMeasuresExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Vcs Document Measures Extract. Acessa as tabelas: VCS_DOCUMENT_MEASURES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.VcsDemandBiccExtractAM.VcsDocumentMeasuresExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 1 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[vcs_document_measures|VCS_DOCUMENT_MEASURES]] — 12 atributos (1 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[vcs_document_measures|VCS_DOCUMENT_MEASURES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DCDocumentMeasuresPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | DCDocumentMeasuresPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | DCDocumentMeasuresPEODeletedFlag | DELETED_FLAG | — | ✅ |
| 4 | DCDocumentMeasuresPEODocumentId | DOCUMENT_ID | — | ✅ |
| 5 | DCDocumentMeasuresPEODocumentTypeCode | DOCUMENT_TYPE_CODE | — | ✅ |
| 6 | DCDocumentMeasuresPEOInstanceId | INSTANCE_ID | 🔑 | ✅ |
| 7 | DCDocumentMeasuresPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | DCDocumentMeasuresPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | DCDocumentMeasuresPEOMeasureId | MEASURE_ID | — | ✅ |
| 10 | DCDocumentMeasuresPEOMeasureTypeCode | MEASURE_CODE | — | ✅ |
| 11 | DCDocumentMeasuresPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | DCDocumentMeasuresPEOPartyOwnerCode | PARTY_OWNER_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
