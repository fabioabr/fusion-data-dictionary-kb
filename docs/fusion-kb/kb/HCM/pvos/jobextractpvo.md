---
id: DOC-HCM-PVO-JobExtractPVO
doc_type: system-doc
title: "JobExtractPVO — PVO Human Capital Management"
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
  - JobExtractPVO
  - jobextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# JobExtractPVO

## 📌 Visão Geral

Extrai cadastro de cargos (jobs) com vigência, status e avaliação. Fundamental para estruturação da arquitetura de cargos do HCM.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.JobAM.JobExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 106 | 2 | 3 | 38 | 36% |

---

## 🔗 Tabelas Relacionadas

- [[per_jobs_f|PER_JOBS_F]] — 94 atributos (3 PKs, 26 BICC)
- [[per_jobs_f_tl|PER_JOBS_F_TL]] — 12 atributos (12 BICC)

---

## ⚙️ Atributos

### [[per_jobs_f|PER_JOBS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionOccurrenceId | ACTION_OCCURRENCE_ID | — | ✅ |
| 2 | ActiveStatus | ACTIVE_STATUS | — | ✅ |
| 3 | ApprovalAuthority | APPROVAL_AUTHORITY | — | ✅ |
| 4 | Attribute1 | ATTRIBUTE1 | — | — |
| 5 | Attribute10 | ATTRIBUTE10 | — | — |
| 6 | Attribute11 | ATTRIBUTE11 | — | — |
| 7 | Attribute12 | ATTRIBUTE12 | — | — |
| 8 | Attribute13 | ATTRIBUTE13 | — | — |
| 9 | Attribute14 | ATTRIBUTE14 | — | — |
| 10 | Attribute15 | ATTRIBUTE15 | — | — |
| 11 | Attribute16 | ATTRIBUTE16 | — | — |
| 12 | Attribute17 | ATTRIBUTE17 | — | — |
| 13 | Attribute18 | ATTRIBUTE18 | — | — |
| 14 | Attribute19 | ATTRIBUTE19 | — | — |
| 15 | Attribute2 | ATTRIBUTE2 | — | — |
| 16 | Attribute20 | ATTRIBUTE20 | — | — |
| 17 | Attribute21 | ATTRIBUTE21 | — | — |
| 18 | Attribute22 | ATTRIBUTE22 | — | — |
| 19 | Attribute23 | ATTRIBUTE23 | — | — |
| 20 | Attribute24 | ATTRIBUTE24 | — | — |
| 21 | Attribute25 | ATTRIBUTE25 | — | — |
| 22 | Attribute26 | ATTRIBUTE26 | — | — |
| 23 | Attribute27 | ATTRIBUTE27 | — | — |
| 24 | Attribute28 | ATTRIBUTE28 | — | — |
| 25 | Attribute29 | ATTRIBUTE29 | — | — |
| 26 | Attribute3 | ATTRIBUTE3 | — | — |
| 27 | Attribute30 | ATTRIBUTE30 | — | — |
| 28 | Attribute4 | ATTRIBUTE4 | — | — |
| 29 | Attribute5 | ATTRIBUTE5 | — | — |
| 30 | Attribute6 | ATTRIBUTE6 | — | — |
| 31 | Attribute7 | ATTRIBUTE7 | — | — |
| 32 | Attribute8 | ATTRIBUTE8 | — | — |
| 33 | Attribute9 | ATTRIBUTE9 | — | — |
| 34 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 35 | AttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 36 | AttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 37 | AttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 38 | AttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 39 | AttributeDate13 | ATTRIBUTE_DATE13 | — | — |
| 40 | AttributeDate14 | ATTRIBUTE_DATE14 | — | — |
| 41 | AttributeDate15 | ATTRIBUTE_DATE15 | — | — |
| 42 | AttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 43 | AttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 44 | AttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 45 | AttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 46 | AttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 47 | AttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 48 | AttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 49 | AttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 50 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 51 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 52 | AttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 53 | AttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 54 | AttributeNumber13 | ATTRIBUTE_NUMBER13 | — | — |
| 55 | AttributeNumber14 | ATTRIBUTE_NUMBER14 | — | — |
| 56 | AttributeNumber15 | ATTRIBUTE_NUMBER15 | — | — |
| 57 | AttributeNumber16 | ATTRIBUTE_NUMBER16 | — | — |
| 58 | AttributeNumber17 | ATTRIBUTE_NUMBER17 | — | — |
| 59 | AttributeNumber18 | ATTRIBUTE_NUMBER18 | — | — |
| 60 | AttributeNumber19 | ATTRIBUTE_NUMBER19 | — | — |
| 61 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 62 | AttributeNumber20 | ATTRIBUTE_NUMBER20 | — | — |
| 63 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 64 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 65 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 66 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 67 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 68 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 69 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 70 | BenchmarkJobFlag | BENCHMARK_JOB_FLAG | — | ✅ |
| 71 | BenchmarkJobId | BENCHMARK_JOB_ID | — | ✅ |
| 72 | BusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 73 | CategoryCode | CATEGORY_CODE | — | ✅ |
| 74 | CreatedBy | CREATED_BY | — | ✅ |
| 75 | CreationDate | CREATION_DATE | — | — |
| 76 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 77 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 78 | FullPartTime | FULL_PART_TIME | — | ✅ |
| 79 | GradeLadderId | GRADE_LADDER_ID | — | ✅ |
| 80 | JobCode | JOB_CODE | — | ✅ |
| 81 | JobFamilyId | JOB_FAMILY_ID | — | ✅ |
| 82 | JobFunctionCode | JOB_FUNCTION_CODE | — | ✅ |
| 83 | JobId | JOB_ID | 🔑 | ✅ |
| 84 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 85 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 86 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 87 | ManagerLevel | MANAGER_LEVEL | — | ✅ |
| 88 | MedCheckupReq | MED_CHECKUP_REQ | — | ✅ |
| 89 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 90 | ProgressionJobId | PROGRESSION_JOB_ID | — | ✅ |
| 91 | RegularTemporary | REGULAR_TEMPORARY | — | ✅ |
| 92 | RequisitionTemplateId | REQUISITION_TEMPLATE_ID | — | ✅ |
| 93 | SchedulingGroup | SCHEDULING_GROUP | — | — |
| 94 | SetId | SET_ID | — | ✅ |

### [[per_jobs_f_tl|PER_JOBS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JobTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | JobTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | JobTranslationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 4 | JobTranslationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 5 | JobTranslationPEOJobId | JOB_ID | — | ✅ |
| 6 | JobTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 7 | JobTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | JobTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | JobTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | JobTranslationPEOName | NAME | — | ✅ |
| 11 | JobTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | JobTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
