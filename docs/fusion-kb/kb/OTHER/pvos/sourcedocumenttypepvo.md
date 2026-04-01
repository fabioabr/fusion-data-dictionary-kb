---
id: DOC-OTHER-PVO-SourceDocumentTypePVO
doc_type: system-doc
title: "SourceDocumentTypePVO — PVO Cross-Module"
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
  - SourceDocumentTypePVO
  - sourcedocumenttypepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SourceDocumentTypePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Source Document Type. Acessa as tabelas: VRM_SOURCE_DOC_TYPES_B, VRM_SOURCE_DOC_TYPES_TL.

**Caminho:** `FscmTopModelAM.FinVrmShrdSetupPublicModelAM.SourceDocumentTypePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 25 | 2 | 1 | 8 | 32% |

---

## 🔗 Tabelas Relacionadas

- [[vrm_source_doc_types_b|VRM_SOURCE_DOC_TYPES_B]] — 14 atributos (1 PKs, 4 BICC)
- [[vrm_source_doc_types_tl|VRM_SOURCE_DOC_TYPES_TL]] — 11 atributos (4 BICC)

---

## ⚙️ Atributos

### [[vrm_source_doc_types_b|VRM_SOURCE_DOC_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DocumentTypeId | DOCUMENT_TYPE_ID | 🔑 | ✅ |
| 2 | VrmSourceDocTypeBaseActiveFlag | ACTIVE_FLAG | — | ✅ |
| 3 | VrmSourceDocTypeBaseApplicationId | APPLICATION_ID | — | — |
| 4 | VrmSourceDocTypeBaseCreatedBy | CREATED_BY | — | — |
| 5 | VrmSourceDocTypeBaseCreationDate | CREATION_DATE | — | — |
| 6 | VrmSourceDocTypeBaseDefaultRevisionIntentCode | DEFAULT_REVISION_INTENT_CODE | — | ✅ |
| 7 | VrmSourceDocTypeBaseDocumentTypeCode | DOCUMENT_TYPE_CODE | — | — |
| 8 | VrmSourceDocTypeBaseExtractTimeFrame | EXTRACT_TIME_FRAME | — | — |
| 9 | VrmSourceDocTypeBaseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | VrmSourceDocTypeBaseLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | VrmSourceDocTypeBaseLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | VrmSourceDocTypeBaseModuleId | MODULE_ID | — | — |
| 13 | VrmSourceDocTypeBaseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | VrmSourceDocTypeBaseValidationStatus | VALIDATION_STATUS | — | — |

### [[vrm_source_doc_types_tl|VRM_SOURCE_DOC_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | VrmSourceDocTypeTranslationCreatedBy | CREATED_BY | — | — |
| 2 | VrmSourceDocTypeTranslationCreationDate | CREATION_DATE | — | — |
| 3 | VrmSourceDocTypeTranslationDescription | DESCRIPTION | — | ✅ |
| 4 | VrmSourceDocTypeTranslationDocumentTypeId | DOCUMENT_TYPE_ID | — | — |
| 5 | VrmSourceDocTypeTranslationLanguage | LANGUAGE | — | ✅ |
| 6 | VrmSourceDocTypeTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | VrmSourceDocTypeTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | VrmSourceDocTypeTranslationLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | VrmSourceDocTypeTranslationName | NAME | — | ✅ |
| 10 | VrmSourceDocTypeTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | VrmSourceDocTypeTranslationSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
