---
id: DOC-OTHER-PVO-DescriptionVersionPVO
doc_type: system-doc
title: "DescriptionVersionPVO — PVO Cross-Module"
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
  - DescriptionVersionPVO
  - descriptionversionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DescriptionVersionPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Description Version. Acessa as tabelas: IRC_DESC_VERSIONS_B, IRC_DESC_VERSIONS_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecruitingCommonAM.DescriptionVersionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 23 | 2 | 1 | 11 | 48% |

---

## 🔗 Tabelas Relacionadas

- [[irc_desc_versions_b|IRC_DESC_VERSIONS_B]] — 11 atributos (1 PKs, 7 BICC)
- [[irc_desc_versions_tl|IRC_DESC_VERSIONS_TL]] — 12 atributos (4 BICC)

---

## ⚙️ Atributos

### [[irc_desc_versions_b|IRC_DESC_VERSIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | DescVerBPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 4 | DescVersionId | DESC_VERSION_ID | 🔑 | ✅ |
| 5 | DescriptionId | DESCRIPTION_ID | — | — |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | StatusCode | STATUS_CODE | — | ✅ |
| 11 | VersionStartDate | VERSION_START_DATE | — | ✅ |

### [[irc_desc_versions_tl|IRC_DESC_VERSIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy1 | CREATED_BY | — | — |
| 2 | CreationDate1 | CREATION_DATE | — | — |
| 3 | DescVerTranslPEOTxtDecsription | TXT_DESCRIPTION | — | ✅ |
| 4 | DescVersionId1 | DESC_VERSION_ID | — | — |
| 5 | Description | DESCRIPTION | — | ✅ |
| 6 | Language1 | LANGUAGE | — | — |
| 7 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 9 | LastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 10 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 11 | ShortDescription | SHORT_DESCRIPTION | — | ✅ |
| 12 | SourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
