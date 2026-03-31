---
id: DOC-OTHER-PVO-DescriptionPVO
doc_type: system-doc
title: "DescriptionPVO — PVO Cross-Module"
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
  - DescriptionPVO
  - descriptionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DescriptionPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Description. Acessa as tabelas: IRC_DESCRIPTIONS_B, IRC_DESCRIPTIONS_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecruitingCommonAM.DescriptionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 2 | 1 | 10 | 48% |

---

## 🔗 Tabelas Relacionadas

- [[irc_descriptions_b|IRC_DESCRIPTIONS_B]] — 11 atributos (1 PKs, 8 BICC)
- [[irc_descriptions_tl|IRC_DESCRIPTIONS_TL]] — 10 atributos (2 BICC)

---

## ⚙️ Atributos

### [[irc_descriptions_b|IRC_DESCRIPTIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | DescriptionCode | DESCRIPTION_CODE | — | ✅ |
| 4 | DescriptionId | DESCRIPTION_ID | 🔑 | ✅ |
| 5 | DescriptionTypeCode | DESCRIPTION_TYPE_CODE | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | StatusCode | STATUS_CODE | — | ✅ |
| 11 | VisibilityCode | VISIBILITY_CODE | — | ✅ |

### [[irc_descriptions_tl|IRC_DESCRIPTIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy1 | CREATED_BY | — | — |
| 2 | CreationDate1 | CREATION_DATE | — | — |
| 3 | DescriptionId1 | DESCRIPTION_ID | — | — |
| 4 | Language | LANGUAGE | — | — |
| 5 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 7 | LastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 8 | Name | NAME | — | ✅ |
| 9 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 10 | SourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
