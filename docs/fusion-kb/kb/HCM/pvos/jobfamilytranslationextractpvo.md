---
id: DOC-HCM-PVO-JobFamilyTranslationExtractPVO
doc_type: system-doc
title: "JobFamilyTranslationExtractPVO — PVO Human Capital Management"
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
  - JobFamilyTranslationExtractPVO
  - jobfamilytranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# JobFamilyTranslationExtractPVO

## 📌 Visão Geral

Extrai traduções de nomes de famílias de cargos por idioma. Suporta relatórios multilíngues de estrutura de carreiras.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.JobBiccExtractAM.JobFamilyTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 4 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[per_job_family_f_tl|PER_JOB_FAMILY_F_TL]] — 12 atributos (4 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[per_job_family_f_tl|PER_JOB_FAMILY_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 4 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 5 | JobFamilyId | JOB_FAMILY_ID | 🔑 | ✅ |
| 6 | JobFamilyName | JOB_FAMILY_NAME | — | ✅ |
| 7 | Language | LANGUAGE | 🔑 | ✅ |
| 8 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
