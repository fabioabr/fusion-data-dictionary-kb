---
id: DOC-OTHER-PVO-RiskTreatmentPVO
doc_type: system-doc
title: "RiskTreatmentPVO — PVO Cross-Module"
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
  - RiskTreatmentPVO
  - risktreatmentpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RiskTreatmentPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Risk Treatment. Acessa as tabelas: GRC_RSK_TRTMNTP_B, GRC_RSK_TRTMNTP_TL, GTG_OTBI_RSK_TRTMNT_DTL (+1).

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.RiskTreatmentPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 82 | 4 | 0 | 9 | 11% |

---

## 🔗 Tabelas Relacionadas

- [[grc_rsk_trtmntp_b|GRC_RSK_TRTMNTP_B]] — 16 atributos (7 BICC)
- [[grc_rsk_trtmntp_tl|GRC_RSK_TRTMNTP_TL]] — 10 atributos (1 BICC)
- [[gtg_otbi_rsk_trtmnt_dtl|GTG_OTBI_RSK_TRTMNT_DTL]] — 43 atributos (1 BICC)
- [[gtg_sc_frc_access_v|GTG_SC_FRC_ACCESS_V]] — 13 atributos

---

## ⚙️ Atributos

### [[grc_rsk_trtmntp_b|GRC_RSK_TRTMNTP_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskTreatmentPlanBasePEOCreatedBy | CREATED_BY | — | — |
| 2 | RiskTreatmentPlanBasePEOCreationDate | CREATION_DATE | — | — |
| 3 | RiskTreatmentPlanBasePEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 4 | RiskTreatmentPlanBasePEOInUseIndicator | IN_USE_INDICATOR | — | ✅ |
| 5 | RiskTreatmentPlanBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | RiskTreatmentPlanBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | RiskTreatmentPlanBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | RiskTreatmentPlanBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | RiskTreatmentPlanBasePEOResidualImpactParamId | RESIDUAL_IMPACT_PARAM_ID | — | ✅ |
| 10 | RiskTreatmentPlanBasePEOResidualLikelihoodParamId | RESIDUAL_LIKELIHOOD_PARAM_ID | — | ✅ |
| 11 | RiskTreatmentPlanBasePEOResidualRiskLevel | RESIDUAL_RISK_LEVEL | — | ✅ |
| 12 | RiskTreatmentPlanBasePEOResidualRiskLevelMapId | RESIDUAL_RISK_LEVEL_MAP_ID | — | ✅ |
| 13 | RiskTreatmentPlanBasePEORevisionDate | REVISION_DATE | — | — |
| 14 | RiskTreatmentPlanBasePEORiskId | RISK_ID | — | — |
| 15 | RiskTreatmentPlanBasePEOTargetPlanIndicator | TARGET_PLAN_INDICATOR | — | ✅ |
| 16 | RiskTreatmentPlanBasePEOTreatmentPlanId | TREATMENT_PLAN_ID | — | — |

### [[grc_rsk_trtmntp_tl|GRC_RSK_TRTMNTP_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskTreatmentPlanTransPEOCreatedBy | CREATED_BY | — | — |
| 2 | RiskTreatmentPlanTransPEOCreationDate | CREATION_DATE | — | — |
| 3 | RiskTreatmentPlanTransPEODetailedDescription | DETAILED_DESCRIPTION | — | — |
| 4 | RiskTreatmentPlanTransPEOLanguage | LANGUAGE | — | — |
| 5 | RiskTreatmentPlanTransPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | RiskTreatmentPlanTransPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | RiskTreatmentPlanTransPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | RiskTreatmentPlanTransPEOName | NAME | — | — |
| 9 | RiskTreatmentPlanTransPEOSourceLang | SOURCE_LANG | — | — |
| 10 | RiskTreatmentPlanTransPEOTreatmentPlanId | TREATMENT_PLAN_ID | — | — |

### [[gtg_otbi_rsk_trtmnt_dtl|GTG_OTBI_RSK_TRTMNT_DTL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskTreatmentBasePEOAnalysisId | ANALYSIS_ID | — | — |
| 2 | RiskTreatmentBasePEOCreatedBy | CREATED_BY | — | — |
| 3 | RiskTreatmentBasePEOCreationDate | CREATION_DATE | — | — |
| 4 | RiskTreatmentBasePEOInherentRiskImpact | INHERENT_RISK_IMPACT | — | — |
| 5 | RiskTreatmentBasePEOInherentRiskImpactLabel | INHERENT_RISK_IMPACT_LABEL | — | — |
| 6 | RiskTreatmentBasePEOInherentRiskLevel | INHERENT_RISK_LEVEL | — | — |
| 7 | RiskTreatmentBasePEOInherentRiskLevelLabel | INHERENT_RISK_LEVEL_LABEL | — | — |
| 8 | RiskTreatmentBasePEOInherentRiskLikelihood | INHERENT_RISK_LIKELIHOOD | — | — |
| 9 | RiskTreatmentBasePEOInherentRiskLikelihoodLabel | INHERENT_RISK_LIKELIHOOD_LABEL | — | — |
| 10 | RiskTreatmentBasePEOInuseTreatmentCost | INUSE_TREATMENT_COST | — | — |
| 11 | RiskTreatmentBasePEOInuseTreatmentCostOrig | INUSE_TREATMENT_COST_ORIG | — | — |
| 12 | RiskTreatmentBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | RiskTreatmentBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | RiskTreatmentBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | RiskTreatmentBasePEOResidualImpact | RESIDUAL_IMPACT | — | — |
| 16 | RiskTreatmentBasePEOResidualImpactLabel | RESIDUAL_IMPACT_LABEL | — | — |
| 17 | RiskTreatmentBasePEOResidualImpactLabelOrig | RESIDUAL_IMPACT_LABEL_ORIG | — | — |
| 18 | RiskTreatmentBasePEOResidualImpactOrig | RESIDUAL_IMPACT_ORIG | — | — |
| 19 | RiskTreatmentBasePEOResidualLikelihood | RESIDUAL_LIKELIHOOD | — | — |
| 20 | RiskTreatmentBasePEOResidualLikelihoodLabel | RESIDUAL_LIKELIHOOD_LABEL | — | — |
| 21 | RiskTreatmentBasePEOResidualLikelihoodLabelOrig | RESIDUAL_LIKELIHOOD_LABEL_ORIG | — | — |
| 22 | RiskTreatmentBasePEOResidualLikelihoodOrig | RESIDUAL_LIKELIHOOD_ORIG | — | — |
| 23 | RiskTreatmentBasePEOResidualRiskLevel | RESIDUAL_RISK_LEVEL | — | — |
| 24 | RiskTreatmentBasePEOResidualRiskLevelLabel | RESIDUAL_RISK_LEVEL_LABEL | — | — |
| 25 | RiskTreatmentBasePEOResidualRiskLevelLabelOrig | RESIDUAL_RISK_LEVEL_LABEL_ORIG | — | — |
| 26 | RiskTreatmentBasePEOResidualRiskLevelOrig | RESIDUAL_RISK_LEVEL_ORIG | — | — |
| 27 | RiskTreatmentBasePEORiskId | RISK_ID | — | — |
| 28 | RiskTreatmentBasePEOTargetImpact | TARGET_IMPACT | — | — |
| 29 | RiskTreatmentBasePEOTargetImpactLabel | TARGET_IMPACT_LABEL | — | — |
| 30 | RiskTreatmentBasePEOTargetImpactLabelOrig | TARGET_IMPACT_LABEL_ORIG | — | — |
| 31 | RiskTreatmentBasePEOTargetImpactOrig | TARGET_IMPACT_ORIG | — | — |
| 32 | RiskTreatmentBasePEOTargetLikelihood | TARGET_LIKELIHOOD | — | — |
| 33 | RiskTreatmentBasePEOTargetLikelihoodLabel | TARGET_LIKELIHOOD_LABEL | — | — |
| 34 | RiskTreatmentBasePEOTargetLikelihoodLabelOrig | TARGET_LIKELIHOOD_LABEL_ORIG | — | — |
| 35 | RiskTreatmentBasePEOTargetLikelihoodOrig | TARGET_LIKELIHOOD_ORIG | — | — |
| 36 | RiskTreatmentBasePEOTargetRiskLevel | TARGET_RISK_LEVEL | — | — |
| 37 | RiskTreatmentBasePEOTargetRiskLevelLabel | TARGET_RISK_LEVEL_LABEL | — | — |
| 38 | RiskTreatmentBasePEOTargetRiskLevelLabelOrig | TARGET_RISK_LEVEL_LABEL_ORIG | — | — |
| 39 | RiskTreatmentBasePEOTargetRiskLevelOrig | TARGET_RISK_LEVEL_ORIG | — | — |
| 40 | RiskTreatmentBasePEOTargetTreatmentCost | TARGET_TREATMENT_COST | — | — |
| 41 | RiskTreatmentBasePEOTargetTreatmentCostOrig | TARGET_TREATMENT_COST_ORIG | — | — |
| 42 | RiskTreatmentBasePEOTotalTreatmentCost | TOTAL_TREATMENT_COST | — | — |
| 43 | RiskTreatmentBasePEOTreatmentPlanId | TREATMENT_PLAN_ID | — | — |

### [[gtg_sc_frc_access_v|GTG_SC_FRC_ACCESS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FRCSecurityPEOHasApprove | HAS_APPROVE | — | — |
| 2 | FRCSecurityPEOHasAssign | HAS_ASSIGN | — | — |
| 3 | FRCSecurityPEOHasClose | HAS_CLOSE | — | — |
| 4 | FRCSecurityPEOHasDelete | HAS_DELETE | — | — |
| 5 | FRCSecurityPEOHasEdit | HAS_EDIT | — | — |
| 6 | FRCSecurityPEOHasInitAssessment | HAS_INIT_ASSESSMENT | — | — |
| 7 | FRCSecurityPEOHasIssueValidate | HAS_ISSUE_VALIDATE | — | — |
| 8 | FRCSecurityPEOHasReview | HAS_REVIEW | — | — |
| 9 | FRCSecurityPEOHasView | HAS_VIEW | — | — |
| 10 | FRCSecurityPEOSecurableId | SECURABLE_ID | — | — |
| 11 | FRCSecurityPEOSecurableType | SECURABLE_TYPE | — | — |
| 12 | FRCSecurityPEOStateType | STATE_TYPE | — | — |
| 13 | FRCSecurityPEOUserId | USER_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
