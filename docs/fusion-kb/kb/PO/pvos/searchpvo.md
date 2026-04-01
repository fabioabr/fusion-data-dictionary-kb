---
id: DOC-PO-PVO-SearchPVO
doc_type: system-doc
title: "SearchPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - SearchPVO
  - searchpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SearchPVO

## 📌 Visão Geral

Extrai dados de buscas realizadas no sistema de recrutamento, incluindo termos, filtros, responsável e critérios. Permite análise de comportamento de busca e otimização de processos de seleção.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecSourcingCoreAM.SearchPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 58 | 4 | 1 | 28 | 48% |

---

## 🔗 Tabelas Relacionadas

- [[irc_searches|IRC_SEARCHES]] — 12 atributos (1 PKs, 3 BICC)
- [[irc_searches_dn|IRC_SEARCHES_DN]] — 38 atributos (23 BICC)
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 4 atributos (1 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 4 atributos (1 BICC)

---

## ⚙️ Atributos

### [[irc_searches|IRC_SEARCHES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SearchId | SEARCH_ID | 🔑 | ✅ |
| 2 | SearchPEOCandidateTrackingUpdated | CANDIDATE_TRACKING_UPDATED | — | — |
| 3 | SearchPEOCreatedBy | CREATED_BY | — | — |
| 4 | SearchPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | SearchPEODenormalizationCompleted | DENORMALIZATION_COMPLETED | — | — |
| 6 | SearchPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | SearchPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | SearchPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | SearchPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | SearchPEOOwnerPersonId | OWNER_PERSON_ID | — | ✅ |
| 11 | SearchPEOSearchQuery | SEARCH_QUERY | — | — |
| 12 | SearchPEOSearchResult | SEARCH_RESULT | — | — |

### [[irc_searches_dn|IRC_SEARCHES_DN]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SearchDNPEOCreatedBy | CREATED_BY | — | — |
| 2 | SearchDNPEOCreationDate | CREATION_DATE | — | — |
| 3 | SearchDNPEOFilterAssessmentPackage | FILTER_ASSESSMENT_PACKAGE | — | ✅ |
| 4 | SearchDNPEOFilterAssessmentPercentile | FILTER_ASSESSMENT_PERCENTILE | — | ✅ |
| 5 | SearchDNPEOFilterAssessmentResult | FILTER_ASSESSMENT_RESULT | — | ✅ |
| 6 | SearchDNPEOFilterBasicInfo | FILTER_BASIC_INFO | — | ✅ |
| 7 | SearchDNPEOFilterCandidateType | FILTER_CANDIDATE_TYPE | — | ✅ |
| 8 | SearchDNPEOFilterCompanies | FILTER_COMPANIES | — | ✅ |
| 9 | SearchDNPEOFilterDegrees | FILTER_DEGREES | — | ✅ |
| 10 | SearchDNPEOFilterEvent | FILTER_EVENT | — | — |
| 11 | SearchDNPEOFilterJob | FILTER_JOB | — | ✅ |
| 12 | SearchDNPEOFilterLanguage | FILTER_LANGUAGE | — | ✅ |
| 13 | SearchDNPEOFilterLastUpdatedDate | FILTER_LAST_UPDATED_DATE | — | ✅ |
| 14 | SearchDNPEOFilterLicense | FILTER_LICENSE | — | ✅ |
| 15 | SearchDNPEOFilterLocations | FILTER_LOCATIONS | — | ✅ |
| 16 | SearchDNPEOFilterPool | FILTER_POOL | — | ✅ |
| 17 | SearchDNPEOFilterRehireRecommendation | FILTER_REHIRE_RECOMMENDATION | — | ✅ |
| 18 | SearchDNPEOFilterRequisition | FILTER_REQUISITION | — | — |
| 19 | SearchDNPEOFilterSearchByEmailFlag | SEARCH_BY_EMAIL_FLAG | — | — |
| 20 | SearchDNPEOFilterSearchByLabel | FILTER_LABEL | — | — |
| 21 | SearchDNPEOFilterSearchByOptInMktEmailPref | FILTER_OPT_IN_MKT_EMAILS_PREF | — | — |
| 22 | SearchDNPEOFilterSearchByPhoneFlag | SEARCH_BY_PHONE_FLAG | — | — |
| 23 | SearchDNPEOFilterSkill | FILTER_SKILL | — | — |
| 24 | SearchDNPEOFilterSource | FILTER_SOURCE | — | ✅ |
| 25 | SearchDNPEOFilterSourceMedium | FILTER_SOURCE_MEDIUM | — | ✅ |
| 26 | SearchDNPEOFilterYearsOfExp | FILTER_YEARS_OF_EXP | — | ✅ |
| 27 | SearchDNPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 28 | SearchDNPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 29 | SearchDNPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 30 | SearchDNPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 31 | SearchDNPEOPrecriteriaCandDetails | PRECRITERIA_CAND_DETAILS | — | ✅ |
| 32 | SearchDNPEOPrecriteriaCompany | PRECRITERIA_COMPANY | — | ✅ |
| 33 | SearchDNPEOPrecriteriaEducation | PRECRITERIA_EDUCATION | — | ✅ |
| 34 | SearchDNPEOPrecriteriaExperience | PRECRITERIA_EXPERIENCE | — | ✅ |
| 35 | SearchDNPEOPrecriteriaLocation | PRECRITERIA_LOCATION | — | ✅ |
| 36 | SearchDNPEOSearchId | SEARCH_ID | — | — |
| 37 | SearchDNPEOSearchKeywords | SEARCH_KEYWORDS | — | ✅ |
| 38 | SearchdnId | SEARCHDN_ID | — | — |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonDetailsPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | PersonDetailsPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | PersonDetailsPEOPersonId | PERSON_ID | — | — |
| 4 | PersonDetailsPEOPersonNumber | PERSON_NUMBER | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | PersonNameId | PERSON_NAME_ID | — | — |
| 4 | PersonNamePEOFullName | FULL_NAME | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
