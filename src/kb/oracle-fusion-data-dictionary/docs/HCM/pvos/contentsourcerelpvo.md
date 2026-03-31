---
id: DOC-HCM-PVO-ContentSourceRelPVO
doc_type: system-doc
title: "ContentSourceRelPVO — PVO Human Capital Management"
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
  - ContentSourceRelPVO
  - contentsourcerelpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ContentSourceRelPVO

## 📌 Visão Geral

Relaciona fontes a itens de conteudo da biblioteca de perfis com traducoes. Suporta rastreabilidade da origem de competencias e qualificacoes.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmProfileContentLibraryAM.ContentSourceRelPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 3 | 2 | 6 | 27% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_content_source_rlats|HRT_CONTENT_SOURCE_RLATS]] — 11 atributos (2 PKs, 3 BICC)
- [[hrt_sources_b|HRT_SOURCES_B]] — 5 atributos (2 BICC)
- [[hrt_sources_tl|HRT_SOURCES_TL]] — 6 atributos (1 BICC)

---

## ⚙️ Atributos

### [[hrt_content_source_rlats|HRT_CONTENT_SOURCE_RLATS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | ContentSourceRlatId | CONTENT_SOURCE_RLAT_ID | 🔑 | ✅ |
| 3 | ContentTypeId | CONTENT_TYPE_ID | — | — |
| 4 | CreatedBy | CREATED_BY | — | — |
| 5 | CreationDate | CREATION_DATE | — | — |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ModuleId | MODULE_ID | — | — |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | SourceId | SOURCE_ID | — | — |

### [[hrt_sources_b|HRT_SOURCES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SourcesBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | SourcesBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 3 | SourcesBPEOModuleId | MODULE_ID | — | — |
| 4 | SourcesBPEOSourceCode | SOURCE_CODE | — | ✅ |
| 5 | SourcesBPEOSourceId | SOURCE_ID | — | — |

### [[hrt_sources_tl|HRT_SOURCES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SourceLang | SOURCE_LANG | — | — |
| 2 | SourcesTransalationPEOSourceId | SOURCE_ID | — | — |
| 3 | SourcesTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 4 | SourcesTranslationPEOLanguage | LANGUAGE | — | — |
| 5 | SourcesTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | SourcesTranslationPEOSourceDescription | SOURCE_DESCRIPTION | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
