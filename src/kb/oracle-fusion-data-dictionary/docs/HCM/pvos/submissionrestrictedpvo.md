---
id: DOC-HCM-PVO-SubmissionRestrictedPVO
doc_type: system-doc
title: "SubmissionRestrictedPVO — PVO Human Capital Management"
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
  - SubmissionRestrictedPVO
  - submissionrestrictedpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SubmissionRestrictedPVO

## 📌 Visão Geral

Disponibiliza submissões (candidaturas) com visão restrita por segurança, incluindo ofertas e requisições. Suporta análise controlada do pipeline de candidatos.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecSubmissionsAM.SubmissionRestrictedPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 59 | 6 | 1 | 35 | 59% |

---

## 🔗 Tabelas Relacionadas

- [[irc_ja_last_interaction_v|IRC_JA_LAST_INTERACTION_V]] — 2 atributos
- [[irc_offers|IRC_OFFERS]] — 1 atributos
- [[irc_requisitions_b|IRC_REQUISITIONS_B]] — 12 atributos (4 BICC)
- [[irc_submissions|IRC_SUBMISSIONS]] — 36 atributos (1 PKs, 27 BICC)
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 4 atributos (2 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 4 atributos (2 BICC)

---

## ⚙️ Atributos

### [[irc_ja_last_interaction_v|IRC_JA_LAST_INTERACTION_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JobAppLastInteractionPEOInteractionDate | INTERACTION_DATE | — | — |
| 2 | JobAppLastInteractionPEOInteractionId | INTERACTION_ID | — | — |

### [[irc_offers|IRC_OFFERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OfferId | OFFER_ID | — | — |

### [[irc_requisitions_b|IRC_REQUISITIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReqUsageCode | REQ_USAGE_CODE | — | — |
| 2 | RequisitionBPEOOpenDate | OPEN_DATE | — | — |
| 3 | RequisitionPEOCreatedBy | CREATED_BY | — | — |
| 4 | RequisitionPEOCreationDate | CREATION_DATE | — | — |
| 5 | RequisitionPEOHiringManagerId | HIRING_MANAGER_ID | — | ✅ |
| 6 | RequisitionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | RequisitionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | RequisitionPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | RequisitionPEOManagerAssignmentId | MANAGER_ASSIGNMENT_ID | — | ✅ |
| 10 | RequisitionPEORecruiterAssignmentId | RECRUITER_ASSIGNMENT_ID | — | ✅ |
| 11 | RequisitionPEORecruiterId | RECRUITER_ID | — | — |
| 12 | RequisitionPEORequisitionId | REQUISITION_ID | — | — |

### [[irc_submissions|IRC_SUBMISSIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActiveFlag | ACTIVE_FLAG | — | ✅ |
| 2 | ConfirmedByPersonId | CONFIRMED_BY_PERSON_ID | — | ✅ |
| 3 | ConfirmedFlag | CONFIRMED_FLAG | — | ✅ |
| 4 | CreatedBy | CREATED_BY | — | ✅ |
| 5 | CreationDate | CREATION_DATE | — | ✅ |
| 6 | CurrentPhaseId | CURRENT_PHASE_ID | — | ✅ |
| 7 | CurrentStateId | CURRENT_STATE_ID | — | ✅ |
| 8 | DisqualifiedFlag | DISQUALIFIED_FLAG | — | ✅ |
| 9 | EsignDescVersionId | ESIGN_DESC_VERSION_ID | — | — |
| 10 | InternalFlag | INTERNAL_FLAG | — | ✅ |
| 11 | IsCompletedFlag | IS_COMPLETED_FLAG | — | ✅ |
| 12 | IsRestrictedFlag | IS_RESTRICTED_FLAG | — | ✅ |
| 13 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 16 | LegalDescVersionId | LEGAL_DESC_VERSION_ID | — | — |
| 17 | ObjectStatus | OBJECT_STATUS | — | ✅ |
| 18 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 19 | PersonId | PERSON_ID | — | ✅ |
| 20 | ProcessId | PROCESS_ID | — | — |
| 21 | ProfileId | PROFILE_ID | — | ✅ |
| 22 | PublicStateId | PUBLIC_STATE_ID | — | ✅ |
| 23 | RequisitionId | REQUISITION_ID | — | — |
| 24 | SiteNumber | SITE_NUMBER | — | ✅ |
| 25 | SubmLastModifiedDate | SUBM_LAST_MODIFIED_DATE | — | ✅ |
| 26 | SubmissionConfirmedDate | SUBMISSION_CONFIRMED_DATE | — | ✅ |
| 27 | SubmissionDate | SUBMISSION_DATE | — | ✅ |
| 28 | SubmissionId | SUBMISSION_ID | 🔑 | ✅ |
| 29 | SubmissionLanguageCode | SUBMISSION_LANGUAGE_CODE | — | ✅ |
| 30 | SubmissionPEOAddedByContextCode | ADDED_BY_CONTEXT_CODE | — | ✅ |
| 31 | SubmissionPEOAddedByPersonId | ADDED_BY_PERSON_ID | — | ✅ |
| 32 | SubmissionPEOAfVersionId | AF_VERSION_ID | — | — |
| 33 | SubmissionPEODiscardedFlag | DISCARDED_FLAG | — | — |
| 34 | SubmissionPEOMergedFlag | MERGED_FLAG | — | ✅ |
| 35 | SubmissionPEOPipelineSubmissionId | PIPELINE_SUBMISSION_ID | — | ✅ |
| 36 | SubmissionPEOSystemPersonType | SYSTEM_PERSON_TYPE | — | ✅ |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AddedByPersonDetailsPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | AddedByPersonDetailsPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | AddedByPersonDetailsPEOPersonId | PERSON_ID | — | — |
| 4 | AddedByPersonDetailsPEOPersonNumber | PERSON_NUMBER | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AddedByPersonNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | AddedByPersonNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | AddedByPersonNamePEOFullName | FULL_NAME | — | ✅ |
| 4 | AddedByPersonNamePEOPersonNameId | PERSON_NAME_ID | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
