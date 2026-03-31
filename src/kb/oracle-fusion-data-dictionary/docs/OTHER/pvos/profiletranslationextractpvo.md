---
id: DOC-OTHER-PVO-ProfileTranslationExtractPVO
doc_type: system-doc
title: "ProfileTranslationExtractPVO — PVO Cross-Module"
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
  - ProfileTranslationExtractPVO
  - profiletranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProfileTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Profile Translation Extract. Acessa as tabelas: HRT_PROFILES_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.HcmProfileCoreAM.ProfileTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 2 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_profiles_tl|HRT_PROFILES_TL]] — 12 atributos (2 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[hrt_profiles_tl|HRT_PROFILES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | Description | DESCRIPTION | — | ✅ |
| 5 | Language | LANGUAGE | 🔑 | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | ProfileId | PROFILE_ID | 🔑 | ✅ |
| 11 | SourceLang | SOURCE_LANG | — | ✅ |
| 12 | Summary | SUMMARY | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
