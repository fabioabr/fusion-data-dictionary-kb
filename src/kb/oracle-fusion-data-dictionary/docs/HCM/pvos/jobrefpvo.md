---
id: DOC-HCM-PVO-JobRefPVO
doc_type: system-doc
title: "JobRefPVO — PVO Human Capital Management"
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
  - JobRefPVO
  - jobrefpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# JobRefPVO

## 📌 Visão Geral

Disponibiliza referência simplificada de cargos com código, status e função. Utilizado como lookup em joins com outras entidades HCM.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.JobAM.JobRefPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 26 | 2 | 3 | 12 | 46% |

---

## 🔗 Tabelas Relacionadas

- [[per_jobs_f|PER_JOBS_F]] — 14 atributos (3 PKs, 8 BICC)
- [[per_jobs_f_tl|PER_JOBS_F_TL]] — 12 atributos (4 BICC)

---

## ⚙️ Atributos

### [[per_jobs_f|PER_JOBS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 3 | JobId | JOB_ID | 🔑 | ✅ |
| 4 | JobPEOActiveStatus | ACTIVE_STATUS | — | ✅ |
| 5 | JobPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 6 | JobPEOCreatedBy | CREATED_BY | — | — |
| 7 | JobPEOCreationDate | CREATION_DATE | — | — |
| 8 | JobPEOJobCode | JOB_CODE | — | ✅ |
| 9 | JobPEOJobFunctionCode | JOB_FUNCTION_CODE | — | ✅ |
| 10 | JobPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | JobPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | JobPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | JobPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | JobPEOSetId | SET_ID | — | ✅ |

### [[per_jobs_f_tl|PER_JOBS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JobTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | JobTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | JobTranslationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 4 | JobTranslationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 5 | JobTranslationPEOJobId | JOB_ID | — | — |
| 6 | JobTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 7 | JobTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | JobTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | JobTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | JobTranslationPEOName | NAME | — | ✅ |
| 11 | JobTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | JobTranslationPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
