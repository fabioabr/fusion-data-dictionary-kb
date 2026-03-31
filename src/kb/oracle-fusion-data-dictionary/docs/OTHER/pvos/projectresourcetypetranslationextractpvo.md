---
id: DOC-OTHER-PVO-ProjectResourceTypeTranslationExtractPVO
doc_type: system-doc
title: "ProjectResourceTypeTranslationExtractPVO — PVO Cross-Module"
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
  - ProjectResourceTypeTranslationExtractPVO
  - projectresourcetypetranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectResourceTypeTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Resource Type Translation Extract. Acessa as tabelas: PJF_RES_TYPES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.ProjectResourceTypeTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 2 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_res_types_tl|PJF_RES_TYPES_TL]] — 12 atributos (2 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[pjf_res_types_tl|PJF_RES_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectResourceTypeTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | ProjectResourceTypeTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | ProjectResourceTypeTLPEODescription | DESCRIPTION | — | ✅ |
| 4 | ProjectResourceTypeTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | ProjectResourceTypeTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ProjectResourceTypeTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | ProjectResourceTypeTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ProjectResourceTypeTLPEOName | NAME | — | ✅ |
| 9 | ProjectResourceTypeTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | ProjectResourceTypeTLPEOResTypeId | RES_TYPE_ID | 🔑 | ✅ |
| 11 | ProjectResourceTypeTLPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 12 | ProjectResourceTypeTLPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
