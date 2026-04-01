---
id: DOC-OTHER-PVO-PSCPlanReviewStatusPVO
doc_type: system-doc
title: "PSCPlanReviewStatusPVO — PVO Cross-Module"
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
  - PSCPlanReviewStatusPVO
  - pscplanreviewstatuspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PSCPlanReviewStatusPVO

## 📌 Visão Geral

View Object para extração BICC de dados de PSCPlan Review Status. Acessa as tabelas: PSC_LNP_PR_STATUS_VL.

**Caminho:** `FscmTopModelAM.PscPermitsReportingAM.PSCPlanReviewStatusPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 2 | 11 | 85% |

---

## 🔗 Tabelas Relacionadas

- [[psc_lnp_pr_status_vl|PSC_LNP_PR_STATUS_VL]] — 13 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[psc_lnp_pr_status_vl|PSC_LNP_PR_STATUS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PlanReviewStatusPEOAgencyId | AGENCY_ID | 🔑 | ✅ |
| 2 | PlanReviewStatusPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | PlanReviewStatusPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | PlanReviewStatusPEODeletedFlag | DELETED_FLAG | — | ✅ |
| 5 | PlanReviewStatusPEODescription | DESCRIPTION | — | ✅ |
| 6 | PlanReviewStatusPEOEnabledFlag | ENABLED_FLAG | — | ✅ |
| 7 | PlanReviewStatusPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | PlanReviewStatusPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | PlanReviewStatusPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | PlanReviewStatusPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | PlanReviewStatusPEOReviewStatus | REVIEW_STATUS | — | ✅ |
| 12 | PlanReviewStatusPEOSeedDataLock | SEED_DATA_LOCK | — | — |
| 13 | PlanReviewStatusPEOSystemStatus | SYSTEM_STATUS | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
