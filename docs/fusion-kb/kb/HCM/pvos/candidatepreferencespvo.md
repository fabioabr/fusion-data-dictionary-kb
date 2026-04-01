---
id: DOC-HCM-PVO-CandidatePreferencesPVO
doc_type: system-doc
title: "CandidatePreferencesPVO — PVO Human Capital Management"
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
  - CandidatePreferencesPVO
  - candidatepreferencespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CandidatePreferencesPVO

## 📌 Visão Geral

Extrai preferencias de candidatos incluindo familias de cargo e localizacoes desejadas. Suporta matching entre candidatos e oportunidades disponiveis.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecCandidatesAM.CandidatePreferencesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 34 | 3 | 1 | 12 | 35% |

---

## 🔗 Tabelas Relacionadas

- [[irc_cand_preferences|IRC_CAND_PREFERENCES]] — 16 atributos (1 PKs, 8 BICC)
- [[irc_cand_pref_job_family|IRC_CAND_PREF_JOB_FAMILY]] — 9 atributos (2 BICC)
- [[irc_cand_pref_locations|IRC_CAND_PREF_LOCATIONS]] — 9 atributos (2 BICC)

---

## ⚙️ Atributos

### [[irc_cand_preferences|IRC_CAND_PREFERENCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CandPrefId | CAND_PREF_ID | 🔑 | ✅ |
| 2 | CandPrefPEOCreatedBy | CREATED_BY | — | — |
| 3 | CandPrefPEOCreationDate | CREATION_DATE | — | — |
| 4 | CandPrefPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | CandPrefPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | CandPrefPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | CandPrefPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | CandPrefPEOOptInTcEmailsDate | OPT_IN_TC_EMAILS_DATE | — | ✅ |
| 9 | CandPrefPEOOptInTcEmailsFlag | OPT_IN_TC_EMAILS_FLAG | — | ✅ |
| 10 | CandPrefPEOPersonId | PERSON_ID | — | — |
| 11 | CandPrefPEOSiteNumber | SITE_NUMBER | — | — |
| 12 | CandPrefPEOTcAfVersionId | TC_AF_VERSION_ID | — | ✅ |
| 13 | CandPrefPEOTcConfirmedByPersonId | TC_CONFIRMED_BY_PERSON_ID | — | — |
| 14 | CandPrefPEOTcConfirmedDate | TC_CONFIRMED_DATE | — | ✅ |
| 15 | CandPrefPEOTcConfirmedFlag | TC_CONFIRMED_FLAG | — | ✅ |
| 16 | CandPrefPEOTcLegalDescVersionId | TC_LEGAL_DESC_VERSION_ID | — | ✅ |

### [[irc_cand_pref_job_family|IRC_CAND_PREF_JOB_FAMILY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CandPrefJobFamilyPEOCandPrefId | CAND_PREF_ID | — | — |
| 2 | CandPrefJobFamilyPEOCreatedBy | CREATED_BY | — | — |
| 3 | CandPrefJobFamilyPEOCreationDate | CREATION_DATE | — | — |
| 4 | CandPrefJobFamilyPEOJobFamilyId | JOB_FAMILY_ID | — | ✅ |
| 5 | CandPrefJobFamilyPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | CandPrefJobFamilyPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | CandPrefJobFamilyPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | CandPrefJobFamilyPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | PrefJobFamilyId | PREF_JOB_FAMILY_ID | — | — |

### [[irc_cand_pref_locations|IRC_CAND_PREF_LOCATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CandPrefLocPEOCandPrefId | CAND_PREF_ID | — | — |
| 2 | CandPrefLocPEOCreatedBy | CREATED_BY | — | — |
| 3 | CandPrefLocPEOCreationDate | CREATION_DATE | — | — |
| 4 | CandPrefLocPEOGeographyId | GEOGRAPHY_ID | — | ✅ |
| 5 | CandPrefLocPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | CandPrefLocPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | CandPrefLocPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | CandPrefLocPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | PrefLocId | PREF_LOC_ID | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
