---
id: DOC-HCM-PVO-PersonAccrualEntryDtlExtractPVO
doc_type: system-doc
title: "PersonAccrualEntryDtlExtractPVO — PVO Human Capital Management"
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
  - PersonAccrualEntryDtlExtractPVO
  - personaccrualentrydtlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PersonAccrualEntryDtlExtractPVO

## 📌 Visão Geral

Extrai os detalhes de lançamentos de accrual (provisão) de ausências, incluindo ajustes, expiração e motivos. Essencial para conciliação de saldos de férias e licenças remuneradas.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.HcmGblAbsencesBiccExtractAM.PersonAccrualEntryDtlExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 40 | 1 | 1 | 38 | 95% |

---

## 🔗 Tabelas Relacionadas

- [[anc_per_acrl_entry_dtls|ANC_PER_ACRL_ENTRY_DTLS]] — 40 atributos (1 PKs, 38 BICC)

---

## ⚙️ Atributos

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
| 8 | CovrEntryDtlId | COVR_ENTRY_DTL_ID | — | — |
| 9 | CreatedBy | CREATED_BY | — | ✅ |
| 10 | CreationDate | CREATION_DATE | — | ✅ |
| 11 | ElectedAmt | ELECTED_AMT | — | ✅ |
| 12 | ElectionDt | ELECTION_DT | — | ✅ |
| 13 | EnterpriseId | ENTERPRISE_ID | — | ✅ |
| 14 | ExpDisbPayPush | EXP_DISB_PAY_PUSH | — | ✅ |
| 15 | ExpDt | EXP_DT | — | ✅ |
| 16 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 18 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 19 | LegalEmployerId | LEGAL_EMPLOYER_ID | — | ✅ |
| 20 | LoaderRefId | LOADER_REF_ID | — | ✅ |
| 21 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 22 | PerAbsTypeEntryId | PER_ABS_TYPE_ENTRY_ID | — | — |
| 23 | PerAbsenceEntryId | PER_ABSENCE_ENTRY_ID | — | ✅ |
| 24 | PerAccrualEntryDtlId | PER_ACCRUAL_ENTRY_DTL_ID | 🔑 | ✅ |
| 25 | PerAccrualEntryId | PER_ACCRUAL_ENTRY_ID | — | ✅ |
| 26 | PerEventId | PER_EVENT_ID | — | ✅ |
| 27 | PerPlanEnrtId | PER_PLAN_ENRT_ID | — | ✅ |
| 28 | PersonId | PERSON_ID | — | ✅ |
| 29 | PlId | PL_ID | — | ✅ |
| 30 | ProcStatusCd | PROC_STATUS_CD | — | ✅ |
| 31 | ProcdDate | PROCD_DATE | — | ✅ |
| 32 | RefId | REF_ID | — | ✅ |
| 33 | ReferenceDate | REFERENCE_DATE | — | ✅ |
| 34 | Source | SOURCE | — | ✅ |
| 35 | TimeCardId | TIME_CARD_ID | — | ✅ |
| 36 | TimeCardVersion | TIME_CARD_VERSION | — | ✅ |
| 37 | Type | TYPE | — | ✅ |
| 38 | Value | VALUE | — | ✅ |
| 39 | VoidedAcrl | VOIDED_ACRL | — | ✅ |
| 40 | WorkTermAsgId | WORK_TERM_ASG_ID | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
