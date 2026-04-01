---
id: DOC-HCM-PVO-JobFamilyTranslationPVO
doc_type: system-doc
title: "JobFamilyTranslationPVO — PVO Human Capital Management"
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
  - JobFamilyTranslationPVO
  - jobfamilytranslationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# JobFamilyTranslationPVO

## 📌 Visão Geral

Disponibiliza traduções de famílias de cargos com vigência e idioma. Utilizado para exibição localizada de categorias funcionais.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.JobAM.JobFamilyTranslationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 3 | 10 | 83% |

---

## 🔗 Tabelas Relacionadas

- [[per_job_family_f_tl|PER_JOB_FAMILY_F_TL]] — 12 atributos (3 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[per_job_family_f_tl|PER_JOB_FAMILY_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 3 | JobFamilyId | JOB_FAMILY_ID | 🔑 | ✅ |
| 4 | JobFamilyTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | JobFamilyTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | JobFamilyTranslationPEOJobFamilyName | JOB_FAMILY_NAME | — | ✅ |
| 7 | JobFamilyTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | JobFamilyTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | JobFamilyTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | JobFamilyTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | JobFamilyTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |
| 12 | Language | LANGUAGE | 🔑 | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
