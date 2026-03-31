---
id: DOC-OTHER-PVO-ProspectsPVO
doc_type: system-doc
title: "ProspectsPVO — PVO Cross-Module"
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
  - ProspectsPVO
  - prospectspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProspectsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Prospects. Acessa as tabelas: IRC_CAND_PROFILE_USAGES_M, IRC_PROSPECTS, IRC_PRSPT_LAST_INTERACTION_V (+5).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecHiringProspectsAM.ProspectsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 45 | 8 | 1 | 43 | 96% |

---

## 🔗 Tabelas Relacionadas

- [[irc_cand_profile_usages_m|IRC_CAND_PROFILE_USAGES_M]] — 6 atributos (6 BICC)
- [[irc_prospects|IRC_PROSPECTS]] — 17 atributos (1 PKs, 17 BICC)
- [[irc_prspt_last_interaction_v|IRC_PRSPT_LAST_INTERACTION_V]] — 2 atributos
- [[irc_requisitions_b|IRC_REQUISITIONS_B]] — 2 atributos (2 BICC)
- [[irc_submissions|IRC_SUBMISSIONS]] — 5 atributos (5 BICC)
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 4 atributos (4 BICC)
- [[per_email_addresses|PER_EMAIL_ADDRESSES]] — 2 atributos (2 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 7 atributos (7 BICC)

---

## ⚙️ Atributos

### [[irc_cand_profile_usages_m|IRC_CAND_PROFILE_USAGES_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CProUsgPEOCandProfileId | PROFILE_ID | — | ✅ |
| 2 | CProUsgPEOCandProfileUsageId | CAND_PROFILE_USAGE_ID | — | ✅ |
| 3 | CProUsgPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 4 | CProUsgPEOEffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | ✅ |
| 5 | CProUsgPEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | ✅ |
| 6 | CProUsgPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |

### [[irc_prospects|IRC_PROSPECTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProspectId | PROSPECT_ID | 🔑 | ✅ |
| 2 | ProspectsPEOAddedByPersonId | ADDED_BY_PERSON_ID | — | ✅ |
| 3 | ProspectsPEOCandidatePersonId | CANDIDATE_PERSON_ID | — | ✅ |
| 4 | ProspectsPEOContextId | CONTEXT_ID | — | ✅ |
| 5 | ProspectsPEOContextTypeCode | CONTEXT_TYPE_CODE | — | ✅ |
| 6 | ProspectsPEOCreatedBy | CREATED_BY | — | ✅ |
| 7 | ProspectsPEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | ProspectsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | ProspectsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | ProspectsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | ProspectsPEOObjectStatus | OBJECT_STATUS | — | ✅ |
| 12 | ProspectsPEOObjectVersionNum | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | ProspectsPEOProspectStatusCode | PROSPECT_STATUS_CODE | — | ✅ |
| 14 | ProspectsPEOProspectTypeCode | PROSPECT_TYPE_CODE | — | ✅ |
| 15 | ProspectsPEOReferralId | REFERRAL_ID | — | ✅ |
| 16 | ProspectsPEORequisitionId | REQUISITION_ID | — | ✅ |
| 17 | ProspectsPEOSubmissionId | SUBMISSION_ID | — | ✅ |

### [[irc_prspt_last_interaction_v|IRC_PRSPT_LAST_INTERACTION_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProspectLastInteractionPEOInteractionDate | INTERACTION_DATE | — | — |
| 2 | ProspectLastInteractionPEOInteractionId | INTERACTION_ID | — | — |

### [[irc_requisitions_b|IRC_REQUISITIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReqBPEORequisitionId | REQUISITION_ID | — | ✅ |
| 2 | ReqBPEORequisitionTemplateId | REQUISITION_TEMPLATE_ID | — | ✅ |

### [[irc_submissions|IRC_SUBMISSIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SubmissionPEOActiveFlag | ACTIVE_FLAG | — | ✅ |
| 2 | SubmissionPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | SubmissionPEOObjectVersionNum | OBJECT_VERSION_NUMBER | — | ✅ |
| 4 | SubmissionPEOSubmissionDate | SUBMISSION_DATE | — | ✅ |
| 5 | SubmissionPEOSubmissionId | SUBMISSION_ID | — | ✅ |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PerDetailsPEOAddedByPersonNumber | PERSON_NUMBER | — | ✅ |
| 2 | PerDetailsPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 3 | PerDetailsPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | PerDetailsPEOPersonId | PERSON_ID | — | ✅ |

### [[per_email_addresses|PER_EMAIL_ADDRESSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EmailAddrPEOAddedByEmailAddress | EMAIL_ADDRESS | — | ✅ |
| 2 | EmailAddrPEOEmailAddressId | EMAIL_ADDRESS_ID | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PerNamePEOAddedByFirstName | FIRST_NAME | — | ✅ |
| 2 | PerNamePEOAddedByFullName | FULL_NAME | — | ✅ |
| 3 | PerNamePEOAddedByLastName | LAST_NAME | — | ✅ |
| 4 | PerNamePEOAddedByMiddleNames | MIDDLE_NAMES | — | ✅ |
| 5 | PerNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 6 | PerNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 7 | PerNamePEOPersonNameId | PERSON_NAME_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
