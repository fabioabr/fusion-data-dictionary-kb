---
id: DOC-OTHER-PVO-PSCPlanReviewPVO
doc_type: system-doc
title: "PSCPlanReviewPVO — PVO Cross-Module"
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
  - PSCPlanReviewPVO
  - pscplanreviewpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PSCPlanReviewPVO

## 📌 Visão Geral

View Object para extração BICC de dados de PSCPlan Review. Acessa as tabelas: PSC_LNP_PR.

**Caminho:** `FscmTopModelAM.PscPermitsReportingAM.PSCPlanReviewPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 30 | 1 | 1 | 27 | 90% |

---

## 🔗 Tabelas Relacionadas

- [[psc_lnp_pr|PSC_LNP_PR]] — 30 atributos (1 PKs, 27 BICC)

---

## ⚙️ Atributos

### [[psc_lnp_pr|PSC_LNP_PR]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PlanReviewPEOAgencyId | AGENCY_ID | — | ✅ |
| 2 | PlanReviewPEOBbSessionId | BB_SESSION_ID | — | — |
| 3 | PlanReviewPEOBbSessionKey | BB_SESSION_KEY | — | ✅ |
| 4 | PlanReviewPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | PlanReviewPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | PlanReviewPEOCycleCount | CYCLE_COUNT | — | ✅ |
| 7 | PlanReviewPEOCycleDays | CYCLE_DAYS | — | ✅ |
| 8 | PlanReviewPEODecision | DECISION | — | ✅ |
| 9 | PlanReviewPEOEPlanReview | E_PLAN_REVIEW | — | — |
| 10 | PlanReviewPEOElectronicPlanReview | ELECTRONIC_PLAN_REVIEW | — | ✅ |
| 11 | PlanReviewPEOFinalizeStatus | FINALIZE_STATUS | — | ✅ |
| 12 | PlanReviewPEOInviteUrl | INVITE_URL | — | ✅ |
| 13 | PlanReviewPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | PlanReviewPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 15 | PlanReviewPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | PlanReviewPEOLnpRecordKey | LNP_RECORD_KEY | — | ✅ |
| 17 | PlanReviewPEOMigratedDataFlag | MIGRATED_DATA_FLAG | — | ✅ |
| 18 | PlanReviewPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 19 | PlanReviewPEOOriginalPlanReviewKey | ORIGINAL_PLAN_REVIEW_KEY | — | ✅ |
| 20 | PlanReviewPEOPlanReviewId | PLAN_REVIEW_ID | — | ✅ |
| 21 | PlanReviewPEOPlanReviewKey | PLAN_REVIEW_KEY | 🔑 | ✅ |
| 22 | PlanReviewPEOPlanReviewName | PLAN_REVIEW_NAME | — | ✅ |
| 23 | PlanReviewPEOPlanReviewType | PLAN_REVIEW_TYPE | — | ✅ |
| 24 | PlanReviewPEOReviewClosedBy | REVIEW_CLOSED_BY | — | ✅ |
| 25 | PlanReviewPEOReviewClosedDttm | REVIEW_CLOSED_DTTM | — | ✅ |
| 26 | PlanReviewPEOReviewDueDate | REVIEW_DUE_DATE | — | ✅ |
| 27 | PlanReviewPEOReviewOpenBy | REVIEW_OPEN_BY | — | ✅ |
| 28 | PlanReviewPEOReviewOpenDttm | REVIEW_OPEN_DTTM | — | ✅ |
| 29 | PlanReviewPEOReviewStatus | REVIEW_STATUS | — | ✅ |
| 30 | PlanReviewPEOSessionId | SESSION_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
