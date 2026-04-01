---
id: DOC-HCM-PVO-DocumentTypePVO
doc_type: system-doc
title: "DocumentTypePVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - DocumentTypePVO
  - documenttypepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DocumentTypePVO

## 📌 Visão Geral

Disponibiliza tipos de documentos de avaliação de desempenho, incluindo traduções. Utilizado na configuração de templates e modelos de performance review.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmPerformanceSetupAM.DocumentTypePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 19 | 2 | 3 | 16 | 84% |

---

## 🔗 Tabelas Relacionadas

- [[hra_doc_types_b|HRA_DOC_TYPES_B]] — 12 atributos (2 PKs, 11 BICC)
- [[hra_doc_types_tl|HRA_DOC_TYPES_TL]] — 7 atributos (1 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[hra_doc_types_b|HRA_DOC_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | DocTypeId | DOC_TYPE_ID | 🔑 | ✅ |
| 5 | DocumentTypeBPEODateFrom | DATE_FROM | — | ✅ |
| 6 | DocumentTypeBPEODateTo | DATE_TO | — | ✅ |
| 7 | DocumentTypeBPEOSelectMgrAllowedFlag | SELECT_MGR_ALLOWED_FLAG | — | ✅ |
| 8 | DocumentTypeBPEOStatusCode | STATUS_CODE | — | ✅ |
| 9 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[hra_doc_types_tl|HRA_DOC_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DocumentTypeTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | DocumentTypeTranslationPEODescription | DESCRIPTION | — | ✅ |
| 3 | DocumentTypeTranslationPEODocTypeId | DOC_TYPE_ID | — | — |
| 4 | DocumentTypeTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | DocumentTypeTranslationPEOName | NAME | — | ✅ |
| 6 | Language | LANGUAGE | 🔑 | ✅ |
| 7 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
