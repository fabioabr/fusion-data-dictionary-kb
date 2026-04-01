---
id: DOC-OTHER-PVO-PSCPlanReviewersPVO
doc_type: system-doc
title: "PSCPlanReviewersPVO — PVO Cross-Module"
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
  - PSCPlanReviewersPVO
  - pscplanreviewerspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PSCPlanReviewersPVO

## 📌 Visão Geral

View Object para extração BICC de dados de PSCPlan Reviewers. Acessa as tabelas: PER_PERSON_NAMES_F, PSC_LNP_PR, PSC_LNP_PR_EDR_USER (+1).

**Caminho:** `FscmTopModelAM.PscPermitsReportingAM.PSCPlanReviewersPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 78 | 4 | 1 | 50 | 64% |

---

## 🔗 Tabelas Relacionadas

- [[per_person_names_f|PER_PERSON_NAMES_F]] — 4 atributos (1 BICC)
- [[psc_lnp_pr|PSC_LNP_PR]] — 27 atributos (1 PKs, 26 BICC)
- [[psc_lnp_pr_edr_user|PSC_LNP_PR_EDR_USER]] — 21 atributos
- [[psc_lnp_pr_user|PSC_LNP_PR_USER]] — 26 atributos (23 BICC)

---

## ⚙️ Atributos

### [[per_person_names_f|PER_PERSON_NAMES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonProfileDPEODisplayName | DISPLAY_NAME | — | ✅ |
| 2 | PersonProfileDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonProfileDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | PersonProfileDPEOPersonNameId | PERSON_NAME_ID | — | — |

### [[psc_lnp_pr|PSC_LNP_PR]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PlanReviewPEOAgencyId | AGENCY_ID | — | ✅ |
| 2 | PlanReviewPEOBbSessionKey | BB_SESSION_KEY | — | ✅ |
| 3 | PlanReviewPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | PlanReviewPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | PlanReviewPEOCycleCount | CYCLE_COUNT | — | ✅ |
| 6 | PlanReviewPEOCycleDays | CYCLE_DAYS | — | ✅ |
| 7 | PlanReviewPEODecision | DECISION | — | ✅ |
| 8 | PlanReviewPEOElectronicPlanReview | ELECTRONIC_PLAN_REVIEW | — | ✅ |
| 9 | PlanReviewPEOFinalizeStatus | FINALIZE_STATUS | — | ✅ |
| 10 | PlanReviewPEOInviteUrl | INVITE_URL | — | ✅ |
| 11 | PlanReviewPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | PlanReviewPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | PlanReviewPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | PlanReviewPEOLnpRecordKey | LNP_RECORD_KEY | — | ✅ |
| 15 | PlanReviewPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | PlanReviewPEOOriginalPlanReviewKey | ORIGINAL_PLAN_REVIEW_KEY | — | ✅ |
| 17 | PlanReviewPEOPlanReviewId | PLAN_REVIEW_ID | — | ✅ |
| 18 | PlanReviewPEOPlanReviewKey | PLAN_REVIEW_KEY | 🔑 | ✅ |
| 19 | PlanReviewPEOPlanReviewName | PLAN_REVIEW_NAME | — | ✅ |
| 20 | PlanReviewPEOPlanReviewType | PLAN_REVIEW_TYPE | — | ✅ |
| 21 | PlanReviewPEOReviewClosedBy | REVIEW_CLOSED_BY | — | ✅ |
| 22 | PlanReviewPEOReviewClosedDttm | REVIEW_CLOSED_DTTM | — | ✅ |
| 23 | PlanReviewPEOReviewDueDate | REVIEW_DUE_DATE | — | ✅ |
| 24 | PlanReviewPEOReviewOpenBy | REVIEW_OPEN_BY | — | ✅ |
| 25 | PlanReviewPEOReviewOpenDttm | REVIEW_OPEN_DTTM | — | ✅ |
| 26 | PlanReviewPEOReviewStatus | REVIEW_STATUS | — | ✅ |
| 27 | PlanReviewPEOSessionId | SESSION_ID | — | ✅ |

### [[psc_lnp_pr_edr_user|PSC_LNP_PR_EDR_USER]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PlanReviewEDRUsersPEOAgencyId | AGENCY_ID | — | — |
| 2 | PlanReviewEDRUsersPEOAssignedBy | ASSIGNED_BY | — | — |
| 3 | PlanReviewEDRUsersPEOAssignedDttm | ASSIGNED_DTTM | — | — |
| 4 | PlanReviewEDRUsersPEODecision | DECISION | — | — |
| 5 | PlanReviewEDRUsersPEODecisionDttm | DECISION_DTTM | — | — |
| 6 | PlanReviewEDRUsersPEODepartmentId | DEPARTMENT_ID | — | — |
| 7 | PlanReviewEDRUsersPEODocumentFileKey | DOCUMENT_FILE_KEY | — | — |
| 8 | PlanReviewEDRUsersPEODocumentUserId | DOCUMENT_USER_ID | — | — |
| 9 | PlanReviewEDRUsersPEODocumentUserKey | DOCUMENT_USER_KEY | — | — |
| 10 | PlanReviewEDRUsersPEOEmailAddress | EMAIL_ADDRESS | — | — |
| 11 | PlanReviewEDRUsersPEOOverride | OVERRIDE | — | — |
| 12 | PlanReviewEDRUsersPEOOverrideBy | OVERRIDE_BY | — | — |
| 13 | PlanReviewEDRUsersPEOOverrideDecision | OVERRIDE_DECISION | — | — |
| 14 | PlanReviewEDRUsersPEOOverrideDttm | OVERRIDE_DTTM | — | — |
| 15 | PlanReviewEDRUsersPEOPartyId | PARTY_ID | — | — |
| 16 | PlanReviewEDRUsersPEOPlanReviewKey | PLAN_REVIEW_KEY | — | — |
| 17 | PlanReviewEDRUsersPEOReviewStatus | REVIEW_STATUS | — | — |
| 18 | PlanReviewEDRUsersPEOReviewerDueDate | REVIEWER_DUE_DATE | — | — |
| 19 | PlanReviewEDRUsersPEOReviewerId | REVIEWER_ID | — | — |
| 20 | PlanReviewEDRUsersPEOUploadStatus | UPLOAD_STATUS | — | — |
| 21 | PlanReviewEDRUsersPEOUserType | USER_TYPE | — | — |

### [[psc_lnp_pr_user|PSC_LNP_PR_USER]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PlanReviewersPEOAgencyId | AGENCY_ID | — | — |
| 2 | PlanReviewersPEOAssignedBy | ASSIGNED_BY | — | ✅ |
| 3 | PlanReviewersPEOAssignedDttm | ASSIGNED_DTTM | — | ✅ |
| 4 | PlanReviewersPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | PlanReviewersPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | PlanReviewersPEODecision | DECISION | — | ✅ |
| 7 | PlanReviewersPEODecisionDttm | DECISION_DTTM | — | ✅ |
| 8 | PlanReviewersPEODepartmentId | DEPARTMENT_ID | — | ✅ |
| 9 | PlanReviewersPEOEmailAddress | EMAIL_ADDRESS | — | ✅ |
| 10 | PlanReviewersPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | PlanReviewersPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | PlanReviewersPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | PlanReviewersPEOMigratedDataFlag | MIGRATED_DATA_FLAG | — | ✅ |
| 14 | PlanReviewersPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | PlanReviewersPEOOverride | OVERRIDE | — | ✅ |
| 16 | PlanReviewersPEOOverrideBy | OVERRIDE_BY | — | ✅ |
| 17 | PlanReviewersPEOOverrideDecision | OVERRIDE_DECISION | — | ✅ |
| 18 | PlanReviewersPEOOverrideDttm | OVERRIDE_DTTM | — | ✅ |
| 19 | PlanReviewersPEOPartyId | PARTY_ID | — | ✅ |
| 20 | PlanReviewersPEOPlanReviewKey | PLAN_REVIEW_KEY | — | ✅ |
| 21 | PlanReviewersPEOPlanReviewUserKey | PLAN_REVIEW_USER_KEY | — | ✅ |
| 22 | PlanReviewersPEOReviewStatus | REVIEW_STATUS | — | ✅ |
| 23 | PlanReviewersPEOReviewerDueDate | REVIEWER_DUE_DATE | — | ✅ |
| 24 | PlanReviewersPEOReviewerEmailId | REVIEWER_EMAIL_ID | — | — |
| 25 | PlanReviewersPEOReviewerId | REVIEWER_ID | — | ✅ |
| 26 | PlanReviewersPEOUserType | USER_TYPE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
