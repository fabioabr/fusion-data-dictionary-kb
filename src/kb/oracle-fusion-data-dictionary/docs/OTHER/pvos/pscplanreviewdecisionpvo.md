---
id: DOC-OTHER-PVO-PSCPlanReviewDecisionPVO
doc_type: system-doc
title: "PSCPlanReviewDecisionPVO — PVO Cross-Module"
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
  - PSCPlanReviewDecisionPVO
  - pscplanreviewdecisionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PSCPlanReviewDecisionPVO

## 📌 Visão Geral

View Object para extração BICC de dados de PSCPlan Review Decision. Acessa as tabelas: PSC_LNP_PR_DECISION_VL.

**Caminho:** `FscmTopModelAM.PscPermitsReportingAM.PSCPlanReviewDecisionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 2 | 11 | 85% |

---

## 🔗 Tabelas Relacionadas

- [[psc_lnp_pr_decision_vl|PSC_LNP_PR_DECISION_VL]] — 13 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[psc_lnp_pr_decision_vl|PSC_LNP_PR_DECISION_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PlanReviewDecisionPEOAgencyId | AGENCY_ID | 🔑 | ✅ |
| 2 | PlanReviewDecisionPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | PlanReviewDecisionPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | PlanReviewDecisionPEODecisionStatus | DECISION_STATUS | — | ✅ |
| 5 | PlanReviewDecisionPEODeletedFlag | DELETED_FLAG | — | ✅ |
| 6 | PlanReviewDecisionPEODescription | DESCRIPTION | — | ✅ |
| 7 | PlanReviewDecisionPEOEnabledFlag | ENABLED_FLAG | — | ✅ |
| 8 | PlanReviewDecisionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | PlanReviewDecisionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | PlanReviewDecisionPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | PlanReviewDecisionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | PlanReviewDecisionPEOSeedDataLock | SEED_DATA_LOCK | — | — |
| 13 | PlanReviewDecisionPEOSystemStatus | SYSTEM_STATUS | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
