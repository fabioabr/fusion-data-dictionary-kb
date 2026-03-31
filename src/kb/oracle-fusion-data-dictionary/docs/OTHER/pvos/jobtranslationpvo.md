---
id: DOC-OTHER-PVO-JobTranslationPVO
doc_type: system-doc
title: "JobTranslationPVO — PVO Cross-Module"
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
  - JobTranslationPVO
  - jobtranslationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# JobTranslationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Job Translation. Acessa as tabelas: PER_JOBS_F, PER_JOBS_F_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.JobAM.JobTranslationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 35 | 2 | 3 | 12 | 34% |

---

## 🔗 Tabelas Relacionadas

- [[per_jobs_f|PER_JOBS_F]] — 23 atributos (2 BICC)
- [[per_jobs_f_tl|PER_JOBS_F_TL]] — 12 atributos (3 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[per_jobs_f|PER_JOBS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JobPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 2 | JobPEOActiveStatus | ACTIVE_STATUS | — | — |
| 3 | JobPEOApprovalAuthority | APPROVAL_AUTHORITY | — | — |
| 4 | JobPEOBenchmarkJobFlag | BENCHMARK_JOB_FLAG | — | — |
| 5 | JobPEOBenchmarkJobId | BENCHMARK_JOB_ID | — | — |
| 6 | JobPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 7 | JobPEOCreatedBy | CREATED_BY | — | — |
| 8 | JobPEOCreationDate | CREATION_DATE | — | — |
| 9 | JobPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 10 | JobPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 11 | JobPEOFullPartTime | FULL_PART_TIME | — | — |
| 12 | JobPEOJobCode | JOB_CODE | — | — |
| 13 | JobPEOJobFamilyId | JOB_FAMILY_ID | — | — |
| 14 | JobPEOJobFunctionCode | JOB_FUNCTION_CODE | — | — |
| 15 | JobPEOJobId | JOB_ID | — | — |
| 16 | JobPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | JobPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 18 | JobPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 19 | JobPEOManagerLevel | MANAGER_LEVEL | — | — |
| 20 | JobPEOMedCheckupReq | MED_CHECKUP_REQ | — | — |
| 21 | JobPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 22 | JobPEORegularTemporary | REGULAR_TEMPORARY | — | — |
| 23 | JobPEOSetId | SET_ID | — | — |

### [[per_jobs_f_tl|PER_JOBS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 3 | JobId | JOB_ID | 🔑 | ✅ |
| 4 | JobTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | JobTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | JobTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | JobTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | JobTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | JobTranslationPEOName | NAME | — | ✅ |
| 10 | JobTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | JobTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |
| 12 | Language | LANGUAGE | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
