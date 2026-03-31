---
id: DOC-OTHER-PVO-VcsDocumentDefinitionsExtractPVO
doc_type: system-doc
title: "VcsDocumentDefinitionsExtractPVO — PVO Cross-Module"
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
  - VcsDocumentDefinitionsExtractPVO
  - vcsdocumentdefinitionsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# VcsDocumentDefinitionsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Vcs Document Definitions Extract. Acessa as tabelas: VCS_DOCUMENT_DEFINITIONS_B.

**Caminho:** `FscmTopModelAM.ScmExtractAM.VcsDemandBiccExtractAM.VcsDocumentDefinitionsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 1 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[vcs_document_definitions_b|VCS_DOCUMENT_DEFINITIONS_B]] — 13 atributos (1 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[vcs_document_definitions_b|VCS_DOCUMENT_DEFINITIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DCDocumentDefinitionsPEOCollabObjectCode | COLLAB_OBJECT_CODE | — | ✅ |
| 2 | DCDocumentDefinitionsPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | DCDocumentDefinitionsPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | DCDocumentDefinitionsPEOCustomerLvlCode | CUSTOMER_LVL_CODE | — | ✅ |
| 5 | DCDocumentDefinitionsPEODocumentId | DOCUMENT_ID | 🔑 | ✅ |
| 6 | DCDocumentDefinitionsPEODocumentTypeCode | DOCUMENT_TYPE_CODE | — | ✅ |
| 7 | DCDocumentDefinitionsPEOItemLvlCode | ITEM_LVL_CODE | — | ✅ |
| 8 | DCDocumentDefinitionsPEOItemResolutionCode | ITEM_RESOLUTION_CODE | — | ✅ |
| 9 | DCDocumentDefinitionsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | DCDocumentDefinitionsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | DCDocumentDefinitionsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | DCDocumentDefinitionsPEOOrganizationLvlCode | ORGANIZATION_LVL_CODE | — | ✅ |
| 13 | DCDocumentDefinitionsPEOStatusCode | STATUS_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
