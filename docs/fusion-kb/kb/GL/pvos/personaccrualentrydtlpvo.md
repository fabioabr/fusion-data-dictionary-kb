---
id: DOC-GL-PVO-PersonAccrualEntryDtlPVO
doc_type: system-doc
title: "PersonAccrualEntryDtlPVO — PVO General Ledger"
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
  - PersonAccrualEntryDtlPVO
  - personaccrualentrydtlpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PersonAccrualEntryDtlPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Person Accrual Entry Dtl. Acessa as tabelas: ANC_PER_ACCRUAL_ENTRIES, ANC_PER_ACRL_ENTRY_DTLS, PER_ALL_ASSIGNMENTS_M (+1).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.GlobalAbsencesAM.PersonAccrualEntryDtlPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 68 | 4 | 1 | 26 | 38% |

---

## 🔗 Tabelas Relacionadas

- [[anc_per_accrual_entries|ANC_PER_ACCRUAL_ENTRIES]] — 19 atributos
- [[anc_per_acrl_entry_dtls|ANC_PER_ACRL_ENTRY_DTLS]] — 41 atributos (1 PKs, 25 BICC)
- [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]] — 5 atributos
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 3 atributos (1 BICC)

---

## ⚙️ Atributos

### [[anc_per_accrual_entries|ANC_PER_ACCRUAL_ENTRIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccrualPeriod | ACCRUAL_PERIOD | — | — |
| 2 | Accrued | ACCRUED | — | — |
| 3 | BeginBal | BEGIN_BAL | — | — |
| 4 | CreatedBy2 | CREATED_BY | — | — |
| 5 | CreationDate2 | CREATION_DATE | — | — |
| 6 | EndBal | END_BAL | — | — |
| 7 | EnterpriseId1 | ENTERPRISE_ID | — | — |
| 8 | LastUpdateDate2 | LAST_UPDATE_DATE | — | — |
| 9 | LastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 10 | LastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 11 | ObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 12 | PerAccrualEntryId1 | PER_ACCRUAL_ENTRY_ID | — | — |
| 13 | PerPlanEnrtId1 | PER_PLAN_ENRT_ID | — | — |
| 14 | PersonEventId | PERSON_EVENT_ID | — | — |
| 15 | PersonId2 | PERSON_ID | — | — |
| 16 | PlanId | PLAN_ID | — | — |
| 17 | PrdOfSvcId | PRD_OF_SVC_ID | — | — |
| 18 | Used | USED | — | — |
| 19 | WorkTermAsgId1 | WORK_TERM_ASG_ID | — | — |

### [[anc_per_acrl_entry_dtls|ANC_PER_ACRL_ENTRY_DTLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdjExpDt | ADJ_EXP_DT | — | ✅ |
| 2 | AdjExpDtReasonCd | ADJ_EXP_DT_REASON_CD | — | ✅ |
| 3 | AdjustmentReason | ADJUSTMENT_REASON | — | ✅ |
| 4 | ApprovalStatusCd | APPROVAL_STATUS_CD | — | ✅ |
| 5 | AssignmentId | ASSIGNMENT_ID | — | ✅ |
| 6 | BenDisbProcError | BEN_DISB_PROC_ERROR | — | ✅ |
| 7 | CompAdjReasonCd | COMP_ADJ_REASON_CD | — | ✅ |
| 8 | CreatedBy | CREATED_BY | — | — |
| 9 | CreationDate | CREATION_DATE | — | — |
| 10 | ElectedAmt | ELECTED_AMT | — | ✅ |
| 11 | ElectionDt | ELECTION_DT | — | ✅ |
| 12 | EnterpriseId | ENTERPRISE_ID | — | — |
| 13 | ExpDisbPayPush | EXP_DISB_PAY_PUSH | — | ✅ |
| 14 | ExpDt | EXP_DT | — | ✅ |
| 15 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 17 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 18 | LegalEmployerId | LEGAL_EMPLOYER_ID | — | — |
| 19 | LoaderRefId | LOADER_REF_ID | — | — |
| 20 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 21 | PerAbsenceEntryId | PER_ABSENCE_ENTRY_ID | — | — |
| 22 | PerAccrualEntryDtlId | PER_ACCRUAL_ENTRY_DTL_ID | 🔑 | ✅ |
| 23 | PerAccrualEntryId | PER_ACCRUAL_ENTRY_ID | — | ✅ |
| 24 | PerEventId | PER_EVENT_ID | — | — |
| 25 | PerPlanEnrtId | PER_PLAN_ENRT_ID | — | ✅ |
| 26 | PersonAccrualEntryDtlPEODonPoolPlanId | DON_POOL_PLAN_ID | — | — |
| 27 | PersonAccrualEntryDtlPEODonType | DON_TYPE | — | — |
| 28 | PersonAccrualEntryDtlPEORecipientPlanEnrtId | RECIPIENT_PLAN_ENRT_ID | — | — |
| 29 | PersonId | PERSON_ID | — | ✅ |
| 30 | PlId | PL_ID | — | ✅ |
| 31 | ProcStatusCd | PROC_STATUS_CD | — | ✅ |
| 32 | ProcdDate | PROCD_DATE | — | ✅ |
| 33 | RefId | REF_ID | — | — |
| 34 | ReferenceDate | REFERENCE_DATE | — | ✅ |
| 35 | Source | SOURCE | — | ✅ |
| 36 | TimeCardId | TIME_CARD_ID | — | — |
| 37 | TimeCardVersion | TIME_CARD_VERSION | — | — |
| 38 | Type | TYPE | — | ✅ |
| 39 | Value | VALUE | — | ✅ |
| 40 | VoidedAcrl | VOIDED_ACRL | — | ✅ |
| 41 | WorkTermAsgId | WORK_TERM_ASG_ID | — | ✅ |

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
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | PersonId1 | PERSON_ID | — | — |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
