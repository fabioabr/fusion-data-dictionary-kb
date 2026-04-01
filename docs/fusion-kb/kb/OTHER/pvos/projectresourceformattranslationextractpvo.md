---
id: DOC-OTHER-PVO-ProjectResourceFormatTranslationExtractPVO
doc_type: system-doc
title: "ProjectResourceFormatTranslationExtractPVO — PVO Cross-Module"
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
  - ProjectResourceFormatTranslationExtractPVO
  - projectresourceformattranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectResourceFormatTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Resource Format Translation Extract. Acessa as tabelas: PJF_RES_FORMATS_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.ProjectResourceFormatTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 2 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_res_formats_tl|PJF_RES_FORMATS_TL]] — 12 atributos (2 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[pjf_res_formats_tl|PJF_RES_FORMATS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectResourceFormatTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | ProjectResourceFormatTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | ProjectResourceFormatTLPEODescription | DESCRIPTION | — | ✅ |
| 4 | ProjectResourceFormatTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | ProjectResourceFormatTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ProjectResourceFormatTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | ProjectResourceFormatTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ProjectResourceFormatTLPEOName | NAME | — | ✅ |
| 9 | ProjectResourceFormatTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | ProjectResourceFormatTLPEOResFormatId | RES_FORMAT_ID | 🔑 | ✅ |
| 11 | ProjectResourceFormatTLPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 12 | ProjectResourceFormatTLPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
