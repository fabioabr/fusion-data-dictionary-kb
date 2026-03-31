---
id: DOC-HCM-PVO-SourcesAllPVO
doc_type: system-doc
title: "SourcesAllPVO — PVO Human Capital Management"
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
  - SourcesAllPVO
  - sourcesallpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SourcesAllPVO

## 📌 Visão Geral

Disponibiliza todas as fontes cadastradas na biblioteca de conteúdo de perfil. Define origens de informação para competências e qualificações no Talent Profile.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmProfileContentLibraryAM.SourcesAllPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 2 | 2 | 7 | 44% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_sources_b|HRT_SOURCES_B]] — 10 atributos (2 PKs, 4 BICC)
- [[hrt_sources_tl|HRT_SOURCES_TL]] — 6 atributos (3 BICC)

---

## ⚙️ Atributos

### [[hrt_sources_b|HRT_SOURCES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | CreatedBy | CREATED_BY | — | — |
| 3 | CreationDate | CREATION_DATE | — | — |
| 4 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | ModuleId | MODULE_ID | — | — |
| 8 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | SourceCode | SOURCE_CODE | — | ✅ |
| 10 | SourceId | SOURCE_ID | 🔑 | ✅ |

### [[hrt_sources_tl|HRT_SOURCES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Language | LANGUAGE | — | ✅ |
| 2 | SourceDescription | SOURCE_DESCRIPTION | — | ✅ |
| 3 | SourceLang | SOURCE_LANG | — | — |
| 4 | SourcesTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 5 | SourcesTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | SourcesTranslationPEOSourceId | SOURCE_ID | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
