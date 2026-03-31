---
id: DOC-GL-PVO-PersonDonationEntryDtlPVO
doc_type: system-doc
title: "PersonDonationEntryDtlPVO — PVO General Ledger"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - gl
  - data-dictionary
  - pvo
  - bicc
aliases:
  - PersonDonationEntryDtlPVO
  - persondonationentrydtlpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PersonDonationEntryDtlPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Person Donation Entry Dtl. Acessa as tabelas: ANC_PER_ACRL_ENTRY_DTLS, ANC_PER_PLAN_ENROLLMENT, PER_ALL_ASSIGNMENTS_M (+1).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.GlobalAbsencesAM.PersonDonationEntryDtlPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 61 | 4 | 1 | 22 | 36% |

---

## 🔗 Tabelas Relacionadas

- [[anc_per_acrl_entry_dtls|ANC_PER_ACRL_ENTRY_DTLS]] — 50 atributos (1 PKs, 17 BICC)
- [[anc_per_plan_enrollment|ANC_PER_PLAN_ENROLLMENT]] — 3 atributos (3 BICC)
- [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]] — 5 atributos
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 3 atributos (2 BICC)

---

## ⚙️ Atributos

### [[anc_per_acrl_entry_dtls|ANC_PER_ACRL_ENTRY_DTLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdjExpDt | ADJ_EXP_DT | — | — |
| 2 | AdjExpDtReasonCd | ADJ_EXP_DT_REASON_CD | — | — |
| 3 | AdjustmentReason | ADJUSTMENT_REASON | — | — |
| 4 | AncPerAcrlEntryDtlsAltcd | ANC_PER_ACRL_ENTRY_DTLS_ALTCD | — | — |
| 5 | AncPerBenElctdDisbId | ANC_PER_BEN_ELCTD_DISB_ID | — | — |
| 6 | ApprovalStatusCd | APPROVAL_STATUS_CD | — | ✅ |
| 7 | ApprovalSubmittedDate | APPROVAL_SUBMITTED_DATE | — | ✅ |
| 8 | AssignmentId | ASSIGNMENT_ID | — | ✅ |
| 9 | BenDisbFixed | BEN_DISB_FIXED | — | — |
| 10 | BenDisbProcError | BEN_DISB_PROC_ERROR | — | — |
| 11 | BenDisbProcessed | BEN_DISB_PROCESSED | — | — |
| 12 | CompAdjReasonCd | COMP_ADJ_REASON_CD | — | — |
| 13 | CovrEntryDtlId | COVR_ENTRY_DTL_ID | — | — |
| 14 | CreatedBy | CREATED_BY | — | ✅ |
| 15 | CreationDate | CREATION_DATE | — | ✅ |
| 16 | ElectedAmt | ELECTED_AMT | — | — |
| 17 | ElectionDt | ELECTION_DT | — | — |
| 18 | EnterpriseId | ENTERPRISE_ID | — | — |
| 19 | ExpDisbPayPush | EXP_DISB_PAY_PUSH | — | — |
| 20 | ExpDt | EXP_DT | — | — |
| 21 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 22 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 23 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 24 | LegalEmployerId | LEGAL_EMPLOYER_ID | — | — |
| 25 | LoaderRefId | LOADER_REF_ID | — | — |
| 26 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 27 | PerAbsTypeEntryId | PER_ABS_TYPE_ENTRY_ID | — | — |
| 28 | PerAbsenceEntryId | PER_ABSENCE_ENTRY_ID | — | — |
| 29 | PerAccrualEntryDtlId | PER_ACCRUAL_ENTRY_DTL_ID | 🔑 | ✅ |
| 30 | PerAccrualEntryId | PER_ACCRUAL_ENTRY_ID | — | — |
| 31 | PerEventId | PER_EVENT_ID | — | — |
| 32 | PerPlanEnrtId | PER_PLAN_ENRT_ID | — | ✅ |
| 33 | PersonId | PERSON_ID | — | ✅ |
| 34 | PlId | PL_ID | — | ✅ |
| 35 | ProcStatusCd | PROC_STATUS_CD | — | ✅ |
| 36 | ProcdDate | PROCD_DATE | — | ✅ |
| 37 | RecipientPlanEnrtId | RECIPIENT_PLAN_ENRT_ID | — | ✅ |
| 38 | RefId | REF_ID | — | — |
| 39 | ReferenceDate | REFERENCE_DATE | — | — |
| 40 | ReprocessRequired | REPROCESS_REQUIRED | — | — |
| 41 | Source | SOURCE | — | — |
| 42 | TimeCardId | TIME_CARD_ID | — | — |
| 43 | TimeCardVersion | TIME_CARD_VERSION | — | — |
| 44 | Type | TYPE | — | ✅ |
| 45 | UserMode | USER_MODE | — | — |
| 46 | Value | VALUE | — | ✅ |
| 47 | VoidedAcrl | VOIDED_ACRL | — | — |
| 48 | VoidedBy | VOIDED_BY | — | — |
| 49 | VoidedDatetime | VOIDED_DATETIME | — | — |
| 50 | WorkTermAsgId | WORK_TERM_ASG_ID | — | ✅ |

### [[anc_per_plan_enrollment|ANC_PER_PLAN_ENROLLMENT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbsPerPlanEnrollmentPEORecipientPerPlanEnrtId | PER_PLAN_ENRT_ID | — | ✅ |
| 2 | AbsPerPlanEnrollmentPEORecipientPersonID | PERSON_ID | — | ✅ |
| 3 | AbsPerPlanEnrollmentPEORecipientPlanID | PLAN_ID | — | ✅ |

### [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentPEOAssignmentId | ASSIGNMENT_ID | — | — |
| 2 | AssignmentPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | AssignmentPEOEffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | — |
| 4 | AssignmentPEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 5 | AssignmentPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonDetailsPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 2 | PersonDetailsPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | PersonDetailsPEOPersonId | PERSON_ID | — | — |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
