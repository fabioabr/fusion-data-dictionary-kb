---
id: DOC-OTHER-PVO-JobFamilyPVO
doc_type: system-doc
title: "JobFamilyPVO — PVO Cross-Module"
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
  - JobFamilyPVO
  - jobfamilypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# JobFamilyPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Job Family. Acessa as tabelas: PER_JOB_FAMILY_F, PER_JOB_FAMILY_F_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.JobAM.JobFamilyPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 25 | 2 | 3 | 10 | 40% |

---

## 🔗 Tabelas Relacionadas

- [[per_job_family_f|PER_JOB_FAMILY_F]] — 13 atributos (3 PKs, 5 BICC)
- [[per_job_family_f_tl|PER_JOB_FAMILY_F_TL]] — 12 atributos (5 BICC)

---

## ⚙️ Atributos

### [[per_job_family_f|PER_JOB_FAMILY_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 3 | JobFamilyCode | JOB_FAMILY_CODE | — | ✅ |
| 4 | JobFamilyId | JOB_FAMILY_ID | 🔑 | ✅ |
| 5 | JobFamilyPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 6 | JobFamilyPEOActiveStatus | ACTIVE_STATUS | — | — |
| 7 | JobFamilyPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 8 | JobFamilyPEOCreatedBy | CREATED_BY | — | — |
| 9 | JobFamilyPEOCreationDate | CREATION_DATE | — | — |
| 10 | JobFamilyPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | JobFamilyPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | JobFamilyPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | JobFamilyPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[per_job_family_f_tl|PER_JOB_FAMILY_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JobFamilyTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | JobFamilyTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | JobFamilyTranslationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 4 | JobFamilyTranslationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 5 | JobFamilyTranslationPEOJobFamilyId | JOB_FAMILY_ID | — | ✅ |
| 6 | JobFamilyTranslationPEOJobFamilyName | JOB_FAMILY_NAME | — | ✅ |
| 7 | JobFamilyTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 8 | JobFamilyTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | JobFamilyTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | JobFamilyTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | JobFamilyTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | JobFamilyTranslationPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
