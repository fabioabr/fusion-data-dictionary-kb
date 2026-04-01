---
id: DOC-OTHER-PVO-SourceSystem
doc_type: system-doc
title: "SourceSystem — PVO Cross-Module"
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
  - SourceSystem
  - sourcesystem
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SourceSystem

## 📌 Visão Geral

View Object para extração BICC de dados de Source System. Acessa as tabelas: HZ_ORIG_SYSTEMS_B, HZ_ORIG_SYSTEMS_TL.

**Caminho:** `FscmTopModelAM.EgiBatchesPublicModelAnalyticsAM.SourceSystem`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 28 | 2 | 2 | 15 | 54% |

---

## 🔗 Tabelas Relacionadas

- [[hz_orig_systems_b|HZ_ORIG_SYSTEMS_B]] — 17 atributos (1 PKs, 7 BICC)
- [[hz_orig_systems_tl|HZ_ORIG_SYSTEMS_TL]] — 11 atributos (1 PKs, 8 BICC)

---

## ⚙️ Atributos

### [[hz_orig_systems_b|HZ_ORIG_SYSTEMS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrigSystemBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | OrigSystemBasePEOCreatedByModule | CREATED_BY_MODULE | — | — |
| 3 | OrigSystemBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | OrigSystemBasePEOEnableForItemsFlag | ENABLE_FOR_ITEMS_FLAG | — | — |
| 5 | OrigSystemBasePEOEnableForPlanningFlag | ENABLE_FOR_PLANNING_FLAG | — | — |
| 6 | OrigSystemBasePEOEnableForTcaFlag | ENABLE_FOR_TCA_FLAG | — | — |
| 7 | OrigSystemBasePEOEndDateActive | END_DATE_ACTIVE | — | — |
| 8 | OrigSystemBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | OrigSystemBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | OrigSystemBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | OrigSystemBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | OrigSystemBasePEOOrigSystem | ORIG_SYSTEM | — | ✅ |
| 13 | OrigSystemBasePEOOrigSystemType | ORIG_SYSTEM_TYPE | — | ✅ |
| 14 | OrigSystemBasePEOSstFlag | SST_FLAG | — | — |
| 15 | OrigSystemBasePEOStartDateActive | START_DATE_ACTIVE | — | — |
| 16 | OrigSystemBasePEOStatus | STATUS | — | ✅ |
| 17 | OrigSystemId | ORIG_SYSTEM_ID | 🔑 | ✅ |

### [[hz_orig_systems_tl|HZ_ORIG_SYSTEMS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrigSystemTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | OrigSystemTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | OrigSystemTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | OrigSystemTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | OrigSystemTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | OrigSystemTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | OrigSystemTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | OrigSystemTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | OrigSystemTranslationPEOOrigSystemId | ORIG_SYSTEM_ID | — | — |
| 10 | OrigSystemTranslationPEOOrigSystemName | ORIG_SYSTEM_NAME | — | ✅ |
| 11 | OrigSystemTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
