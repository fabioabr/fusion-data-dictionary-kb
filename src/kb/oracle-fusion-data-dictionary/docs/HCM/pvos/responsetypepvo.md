---
id: DOC-HCM-PVO-ResponseTypePVO
doc_type: system-doc
title: "ResponseTypePVO — PVO Human Capital Management"
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
  - ResponseTypePVO
  - responsetypepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ResponseTypePVO

## 📌 Visão Geral

Extrai tipos de resposta configurados para questionários, com códigos e traduções. Define formatos de resposta (múltipla escolha, texto) em pesquisas e avaliações.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.QuestionnaireLibraryAM.ResponseTypePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 28 | 2 | 2 | 6 | 21% |

---

## 🔗 Tabelas Relacionadas

- [[hrq_response_types_b|HRQ_RESPONSE_TYPES_B]] — 16 atributos (2 PKs, 4 BICC)
- [[hrq_response_types_tl|HRQ_RESPONSE_TYPES_TL]] — 12 atributos (2 BICC)

---

## ⚙️ Atributos

### [[hrq_response_types_b|HRQ_RESPONSE_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ResponseTypeBPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | ResponseTypeBPEOCreatedBy | CREATED_BY | — | — |
| 3 | ResponseTypeBPEOCreationDate | CREATION_DATE | — | — |
| 4 | ResponseTypeBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ResponseTypeBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | ResponseTypeBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | ResponseTypeBPEOModuleId | MODULE_ID | — | — |
| 8 | ResponseTypeBPEONumRows | NUM_ROWS | — | — |
| 9 | ResponseTypeBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | ResponseTypeBPEOQstnWidthPct | QSTN_WIDTH_PCT | — | — |
| 11 | ResponseTypeBPEOQuestionType | QUESTION_TYPE | — | — |
| 12 | ResponseTypeBPEOResponseTypeCode | RESPONSE_TYPE_CODE | — | ✅ |
| 13 | ResponseTypeBPEOResponseTypeId | RESPONSE_TYPE_ID | 🔑 | ✅ |
| 14 | ResponseTypeBPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 15 | ResponseTypeBPEOUseAsDefault | USE_AS_DEFAULT | — | — |
| 16 | ResponseTypeBPEOViewId | VIEW_ID | — | — |

### [[hrq_response_types_tl|HRQ_RESPONSE_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ResponseTypeTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ResponseTypeTranslationPEOCreatedBy | CREATED_BY | — | — |
| 3 | ResponseTypeTranslationPEOCreationDate | CREATION_DATE | — | — |
| 4 | ResponseTypeTranslationPEOLanguage | LANGUAGE | — | — |
| 5 | ResponseTypeTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ResponseTypeTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | ResponseTypeTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | ResponseTypeTranslationPEOName | NAME | — | ✅ |
| 9 | ResponseTypeTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | ResponseTypeTranslationPEOResponseTypeId | RESPONSE_TYPE_ID | — | — |
| 11 | ResponseTypeTranslationPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 12 | ResponseTypeTranslationPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
