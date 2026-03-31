---
id: DOC-OTHER-PVO-ContentTypePVO
doc_type: system-doc
title: "ContentTypePVO — PVO Cross-Module"
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
  - ContentTypePVO
  - contenttypepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ContentTypePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Content Type. Acessa as tabelas: HRT_CONTENT_TYPES_B, HRT_CONTENT_TYPES_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmProfileContentLibraryAM.ContentTypePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 19 | 2 | 3 | 16 | 84% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_content_types_b|HRT_CONTENT_TYPES_B]] — 12 atributos (2 PKs, 10 BICC)
- [[hrt_content_types_tl|HRT_CONTENT_TYPES_TL]] — 7 atributos (1 PKs, 6 BICC)

---

## ⚙️ Atributos

### [[hrt_content_types_b|HRT_CONTENT_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ContentTypeBPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 3 | ContentTypeBPEOContentTypeId | CONTENT_TYPE_ID | 🔑 | ✅ |
| 4 | ContentTypeBPEOContextName | CONTEXT_NAME | — | ✅ |
| 5 | ContentTypeBPEOModuleId | MODULE_ID | — | — |
| 6 | CreatedBy | CREATED_BY | — | ✅ |
| 7 | CreationDate | CREATION_DATE | — | ✅ |
| 8 | FreeFormFlag | FREE_FORM_FLAG | — | ✅ |
| 9 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |

### [[hrt_content_types_tl|HRT_CONTENT_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContentTypeTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ContentTypeTranslationPEOContentDescription | CONTENT_DESCRIPTION | — | ✅ |
| 3 | ContentTypeTranslationPEOContentTypeId | CONTENT_TYPE_ID | — | ✅ |
| 4 | ContentTypeTranslationPEOContentTypeName | CONTENT_TYPE_NAME | — | ✅ |
| 5 | ContentTypeTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | Language | LANGUAGE | 🔑 | ✅ |
| 7 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
