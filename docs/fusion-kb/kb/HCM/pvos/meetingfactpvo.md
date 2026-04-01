---
id: DOC-HCM-PVO-MeetingFactPVO
doc_type: system-doc
title: "MeetingFactPVO — PVO Human Capital Management"
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
  - MeetingFactPVO
  - meetingfactpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MeetingFactPVO

## 📌 Visão Geral

Consolida fatos de reuniões de calibração incluindo facilitadores, participantes, avaliados e perfis associados. Visão central para análise do processo de Talent Review e calibração.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmTalentCalibMeetingsAM.MeetingFactPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 85 | 6 | 3 | 13 | 15% |

---

## 🔗 Tabelas Relacionadas

- [[hrr_meetings|HRR_MEETINGS]] — 22 atributos (2 PKs, 3 BICC)
- [[hrr_meeting_facilitators|HRR_MEETING_FACILITATORS]] — 10 atributos (2 BICC)
- [[hrr_meeting_participants|HRR_MEETING_PARTICIPANTS]] — 12 atributos (2 BICC)
- [[hrr_meeting_reviewees|HRR_MEETING_REVIEWEES]] — 12 atributos (3 BICC)
- [[hrt_profiles_b|HRT_PROFILES_B]] — 14 atributos (1 PKs, 2 BICC)
- [[hrt_profile_types_b|HRT_PROFILE_TYPES_B]] — 15 atributos (1 BICC)

---

## ⚙️ Atributos

### [[hrr_meetings|HRR_MEETINGS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | CreatedBy | CREATED_BY | — | — |
| 3 | CreationDate | CREATION_DATE | — | — |
| 4 | DashboardTmplId | DASHBOARD_TMPL_ID | — | — |
| 5 | DataSubmitDate | DATA_SUBMIT_DATE | — | — |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | MeetingDate | MEETING_DATE | — | — |
| 10 | MeetingFacilitatorNotes | MEETING_FACILITATOR_NOTES | — | — |
| 11 | MeetingId | MEETING_ID | 🔑 | ✅ |
| 12 | MeetingInstructions | MEETING_INSTRUCTIONS | — | — |
| 13 | MeetingLeaderId | MEETING_LEADER_ID | — | — |
| 14 | MeetingOrganizationId | MEETING_ORGANIZATION_ID | — | — |
| 15 | MeetingPurpose | MEETING_PURPOSE | — | — |
| 16 | MeetingStatusCode | MEETING_STATUS_CODE | — | — |
| 17 | MeetingSubmissionDate | MEETING_SUBMISSION_DATE | — | — |
| 18 | MeetingSubmitStatusCode | MEETING_SUBMIT_STATUS_CODE | — | — |
| 19 | MeetingTitle | MEETING_TITLE | — | — |
| 20 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 21 | PrefReviewQualifierId | PREF_REVIEW_QUALIFIER_ID | — | — |
| 22 | QuestionnaireId | QUESTIONNAIRE_ID | — | — |

### [[hrr_meeting_facilitators|HRR_MEETING_FACILITATORS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MeetingFacilitatorPEOCreatedBy | CREATED_BY | — | — |
| 2 | MeetingFacilitatorPEOCreationDate | CREATION_DATE | — | — |
| 3 | MeetingFacilitatorPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 4 | MeetingFacilitatorPEOFacilitatorPersonId | FACILITATOR_PERSON_ID | — | ✅ |
| 5 | MeetingFacilitatorPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | MeetingFacilitatorPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | MeetingFacilitatorPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | MeetingFacilitatorPEOMeetingId | MEETING_ID | — | — |
| 9 | MeetingFacilitatorPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | MeetingFacilitorPEOMeetingFacilitatorId | MEETING_FACILITATOR_ID | — | — |

### [[hrr_meeting_participants|HRR_MEETING_PARTICIPANTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DataSubmissionStatusCode | DATA_SUBMISSION_STATUS_CODE | — | — |
| 2 | MeetingParticipantPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | MeetingParticipantPEOCreatedBy | CREATED_BY | — | — |
| 4 | MeetingParticipantPEOCreationDate | CREATION_DATE | — | — |
| 5 | MeetingParticipantPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | MeetingParticipantPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | MeetingParticipantPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | MeetingParticipantPEOMeetingId | MEETING_ID | — | — |
| 9 | MeetingParticipantPEOMeetingParticipantId | MEETING_PARTICIPANT_ID | — | — |
| 10 | MeetingParticipantPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | MeetingParticipantPEOParticipantPersonId | PARTICIPANT_PERSON_ID | — | ✅ |
| 12 | MeetingParticipantPEOParticipantTypeCode | PARTICIPANT_TYPE_CODE | — | — |

### [[hrr_meeting_reviewees|HRR_MEETING_REVIEWEES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MeetingRevieweeId | MEETING_REVIEWEE_ID | — | — |
| 2 | MeetingRevieweePEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | MeetingRevieweePEOCreatedBy | CREATED_BY | — | — |
| 4 | MeetingRevieweePEOCreationDate | CREATION_DATE | — | — |
| 5 | MeetingRevieweePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | MeetingRevieweePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | MeetingRevieweePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | MeetingRevieweePEOMeetingId | MEETING_ID | — | — |
| 9 | MeetingRevieweePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | RevieweeAssignmentId | REVIEWEE_ASSIGNMENT_ID | — | ✅ |
| 11 | RevieweePersonId | REVIEWEE_PERSON_ID | — | ✅ |
| 12 | ReviewerPersonId | REVIEWER_PERSON_ID | — | — |

### [[hrt_profiles_b|HRT_PROFILES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OwnerPersonId | OWNER_PERSON_ID | — | — |
| 2 | PartyId | PARTY_ID | — | — |
| 3 | PersonId | PERSON_ID | — | — |
| 4 | ProfileBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 5 | ProfileBPEOCreatedBy | CREATED_BY | — | — |
| 6 | ProfileBPEOCreationDate | CREATION_DATE | — | — |
| 7 | ProfileBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ProfileBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ProfileBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ProfileBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | ProfileCode | PROFILE_CODE | — | — |
| 12 | ProfileId | PROFILE_ID | 🔑 | ✅ |
| 13 | ProfileTypeId | PROFILE_TYPE_ID | — | — |
| 14 | ProfileUsageCode | PROFILE_USAGE_CODE | — | — |

### [[hrt_profile_types_b|HRT_PROFILE_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DateFrom | DATE_FROM | — | — |
| 2 | DateTo | DATE_TO | — | — |
| 3 | ModuleId | MODULE_ID | — | — |
| 4 | PidApprovalFlag | PID_APPROVAL_FLAG | — | — |
| 5 | ProfileTypeBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 6 | ProfileTypeBPEOCreatedBy | CREATED_BY | — | — |
| 7 | ProfileTypeBPEOCreationDate | CREATION_DATE | — | — |
| 8 | ProfileTypeBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | ProfileTypeBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | ProfileTypeBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | ProfileTypeBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | ProfileTypeBPEOProfileStatusCode | PROFILE_STATUS_CODE | — | — |
| 13 | ProfileTypeBPEOProfileTypeId | PROFILE_TYPE_ID | — | — |
| 14 | ProfileTypeBPEOProfileUsageCode | PROFILE_USAGE_CODE | — | — |
| 15 | ProfileTypeCode | PROFILE_TYPE_CODE | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
