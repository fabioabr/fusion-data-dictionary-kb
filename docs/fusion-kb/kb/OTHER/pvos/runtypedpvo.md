---
id: DOC-OTHER-PVO-RunTypeDPVO
doc_type: system-doc
title: "RunTypeDPVO — PVO Cross-Module"
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
  - RunTypeDPVO
  - runtypedpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RunTypeDPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Run Type D. Acessa as tabelas: PAY_RUN_TYPES_F, PAY_RUN_TYPES_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmPayRunTypesAM.RunTypeDPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 2 | 3 | 15 | 71% |

---

## 🔗 Tabelas Relacionadas

- [[pay_run_types_f|PAY_RUN_TYPES_F]] — 17 atributos (2 PKs, 12 BICC)
- [[pay_run_types_tl|PAY_RUN_TYPES_TL]] — 4 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[pay_run_types_f|PAY_RUN_TYPES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 3 | RunTypeBaseDPEOBaseRunTypeName | BASE_RUN_TYPE_NAME | — | — |
| 4 | RunTypeBaseDPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | RunTypeBaseDPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | RunTypeBaseDPEOInclusionFlag | INCLUSION_FLAG | — | ✅ |
| 7 | RunTypeBaseDPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | RunTypeBaseDPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | RunTypeBaseDPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | RunTypeBaseDPEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 11 | RunTypeBaseDPEOLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | ✅ |
| 12 | RunTypeBaseDPEOModuleId | MODULE_ID | — | — |
| 13 | RunTypeBaseDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | RunTypeBaseDPEORunMethod | RUN_METHOD | — | ✅ |
| 15 | RunTypeBaseDPEOShortname | SHORTNAME | — | ✅ |
| 16 | RunTypeBaseDPEOSrsFlag | SRS_FLAG | — | — |
| 17 | RunTypeId | RUN_TYPE_ID | 🔑 | ✅ |

### [[pay_run_types_tl|PAY_RUN_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RunTypeTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 2 | RunTypeTranslationPEORunTypeId | RUN_TYPE_ID | — | — |
| 3 | RunTypeTranslationPEORunTypeName | RUN_TYPE_NAME | — | ✅ |
| 4 | RunTypeTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
