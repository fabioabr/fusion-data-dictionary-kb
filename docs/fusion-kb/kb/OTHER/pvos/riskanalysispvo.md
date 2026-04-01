---
id: DOC-OTHER-PVO-RiskAnalysisPVO
doc_type: system-doc
title: "RiskAnalysisPVO — PVO Cross-Module"
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
  - RiskAnalysisPVO
  - riskanalysispvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RiskAnalysisPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Risk Analysis. Acessa as tabelas: FUSION_GRC.GTG_OTBI_RISK_DETAILS, GRC_RSK_ANALYSIS_B, GRC_RSK_ANALYSIS_TL (+19).

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.RiskAnalysisPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 324 | 22 | 1 | 80 | 25% |

---

## 🔗 Tabelas Relacionadas

- [[fusion_grc.gtg_otbi_risk_details|FUSION_GRC.GTG_OTBI_RISK_DETAILS]] — 14 atributos (3 BICC)
- [[grc_rsk_analysis_b|GRC_RSK_ANALYSIS_B]] — 27 atributos (1 PKs, 16 BICC)
- [[grc_rsk_analysis_tl|GRC_RSK_ANALYSIS_TL]] — 10 atributos (4 BICC)
- [[grc_rsk_analys_model_map_vl|GRC_RSK_ANALYS_MODEL_MAP_VL]] — 19 atributos (2 BICC)
- [[grc_rsk_anls_mdlmap_b|GRC_RSK_ANLS_MDLMAP_B]] — 15 atributos (1 BICC)
- [[grc_rsk_anls_mdl_tl|GRC_RSK_ANLS_MDL_TL]] — 10 atributos (2 BICC)
- [[grc_rsk_evaluation_b|GRC_RSK_EVALUATION_B]] — 19 atributos (2 BICC)
- [[grc_rsk_impact_model_vl|GRC_RSK_IMPACT_MODEL_VL]] — 22 atributos (1 BICC)
- [[grc_rsk_impact_param_vl|GRC_RSK_IMPACT_PARAM_VL]] — 21 atributos (2 BICC)
- [[grc_rsk_likelihood_model_vl|GRC_RSK_LIKELIHOOD_MODEL_VL]] — 22 atributos (1 BICC)
- [[grc_rsk_likelihood_param_vl|GRC_RSK_LIKELIHOOD_PARAM_VL]] — 21 atributos (2 BICC)
- [[grc_rsk_risk_b|GRC_RSK_RISK_B]] — 1 atributos
- [[grc_rsk_risk_tl|GRC_RSK_RISK_TL]] — 3 atributos (1 BICC)
- [[grc_rsk_trtmntp_b|GRC_RSK_TRTMNTP_B]] — 16 atributos (2 BICC)
- [[grc_rsk_trtmntp_tl|GRC_RSK_TRTMNTP_TL]] — 10 atributos (2 BICC)
- [[gtg_otbi_risk_details|GTG_OTBI_RISK_DETAILS]] — 5 atributos (5 BICC)
- [[gtg_otbi_rsk_analysis_dtl|GTG_OTBI_RSK_ANALYSIS_DTL]] — 13 atributos (6 BICC)
- [[gtg_otbi_rsk_evl_dtl|GTG_OTBI_RSK_EVL_DTL]] — 10 atributos (4 BICC)
- [[gtg_otbi_rsk_trtmnt_dtl|GTG_OTBI_RSK_TRTMNT_DTL]] — 43 atributos (22 BICC)
- [[gtg_sc_frc_access_v|GTG_SC_FRC_ACCESS_V]] — 3 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos (2 BICC)
- [[per_users|PER_USERS]] — 10 atributos

---

## ⚙️ Atributos

### [[fusion_grc.gtg_otbi_risk_details|FUSION_GRC.GTG_OTBI_RISK_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskAnalysisDetailsPEOCreatedBy | CREATED_BY | — | — |
| 2 | RiskAnalysisDetailsPEOCreationDate | CREATION_DATE | — | — |
| 3 | RiskAnalysisDetailsPEOEvalResult | EVALUATION_RESULT | — | ✅ |
| 4 | RiskAnalysisDetailsPEOLstUpdtDt | LAST_UPDATE_DATE | — | ✅ |
| 5 | RiskAnalysisDetailsPEOLstUpdtLgn | LAST_UPDATE_LOGIN | — | — |
| 6 | RiskAnalysisDetailsPEOLstUpdtdBy | LAST_UPDATED_BY | — | — |
| 7 | RiskAnalysisDetailsPEOResImpactParam | RESIDUAL_IMPACT_PARAM | — | — |
| 8 | RiskAnalysisDetailsPEOResImpactVal | RESIDUAL_IMPACT_VAL | — | — |
| 9 | RiskAnalysisDetailsPEOResLklhdParam | RESIDUAL_LIKELIHOOD_PARAM | — | — |
| 10 | RiskAnalysisDetailsPEOResLklhdVal | RESIDUAL_LIKELIHOOD_VAL | — | ✅ |
| 11 | RiskAnalysisDetailsPEOResRiskLevel | RESIDUAL_RISK_LEVEL | — | — |
| 12 | RiskAnalysisDetailsPEOResRiskLvlVal | RESIDUAL_RISK_LVL_VAL | — | — |
| 13 | RiskAnalysisDetailsPEORiskId | RISK_ID | — | — |
| 14 | RiskAnalysisDetailsPEOTrtmntPlanId | TREATMENT_PLAN_ID | — | — |

### [[grc_rsk_analysis_b|GRC_RSK_ANALYSIS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskAnalysisBasePEOAnalysisDate | ANALYSIS_DATE | — | ✅ |
| 2 | RiskAnalysisBasePEOAnalysisTypeCode | ANALYSIS_TYPE_CODE | — | ✅ |
| 3 | RiskAnalysisBasePEOCompletedBy | COMPLETED_BY | — | — |
| 4 | RiskAnalysisBasePEOCompletedDate | COMPLETED_DATE | — | ✅ |
| 5 | RiskAnalysisBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | RiskAnalysisBasePEOCreationDate | CREATION_DATE | — | — |
| 7 | RiskAnalysisBasePEODueDate | DUE_DATE | — | ✅ |
| 8 | RiskAnalysisBasePEOImpactModelId | IMPACT_MODEL_ID | — | — |
| 9 | RiskAnalysisBasePEOImpactParamId | IMPACT_PARAM_ID | — | ✅ |
| 10 | RiskAnalysisBasePEOImpactValue | IMPACT_VALUE | — | — |
| 11 | RiskAnalysisBasePEOLastStateCode | LAST_STATE_CODE | — | ✅ |
| 12 | RiskAnalysisBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | RiskAnalysisBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | RiskAnalysisBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | RiskAnalysisBasePEOLikelihoodModelId | LIKELIHOOD_MODEL_ID | — | — |
| 16 | RiskAnalysisBasePEOLikelihoodParamId | LIKELIHOOD_PARAM_ID | — | ✅ |
| 17 | RiskAnalysisBasePEOLikelihoodValue | LIKELIHOOD_VALUE | — | — |
| 18 | RiskAnalysisBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 19 | RiskAnalysisBasePEORiskAnalysisId | RISK_ANALYSIS_ID | 🔑 | ✅ |
| 20 | RiskAnalysisBasePEORiskAnalysisMapId | RISK_ANALYSIS_MAP_ID | — | ✅ |
| 21 | RiskAnalysisBasePEORiskId | RISK_ID | — | ✅ |
| 22 | RiskAnalysisBasePEORiskLevel | RISK_LEVEL | — | ✅ |
| 23 | RiskAnalysisBasePEOStateCode | STATE_CODE | — | ✅ |
| 24 | RiskAnalysisBasePEOStateDate | STATE_DATE | — | — |
| 25 | RiskAnalysisBasePEOStatus | STATUS | — | ✅ |
| 26 | RiskAnalysisBasePEOTargetCompletionDate | TARGET_COMPLETION_DATE | — | — |
| 27 | RiskAnalysisBasePEOTimeframeCode | TIMEFRAME_CODE | — | — |

### [[grc_rsk_analysis_tl|GRC_RSK_ANALYSIS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskAnalysisTransPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | RiskAnalysisTransPEOCreationDate | CREATION_DATE | — | — |
| 3 | RiskAnalysisTransPEODescription | DESCRIPTION | — | — |
| 4 | RiskAnalysisTransPEODetailedDescription | DETAILED_DESCRIPTION | — | ✅ |
| 5 | RiskAnalysisTransPEOLanguage | LANGUAGE | — | — |
| 6 | RiskAnalysisTransPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | RiskAnalysisTransPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | RiskAnalysisTransPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | RiskAnalysisTransPEORiskAnalysisId | RISK_ANALYSIS_ID | — | — |
| 10 | RiskAnalysisTransPEOSourceLang | SOURCE_LANG | — | — |

### [[grc_rsk_analys_model_map_vl|GRC_RSK_ANALYS_MODEL_MAP_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskAnalysisModelMapPEOBindKey | BIND_KEY | — | — |
| 2 | RiskAnalysisModelMapPEOCreatedBy | CREATED_BY | — | — |
| 3 | RiskAnalysisModelMapPEOCreationDt | CREATION_DATE | — | — |
| 4 | RiskAnalysisModelMapPEODsplyOrdr | DISPLAY_ORDER | — | — |
| 5 | RiskAnalysisModelMapPEOEffSeq | EFFECTIVE_SEQUENCE | — | — |
| 6 | RiskAnalysisModelMapPEOHighValue | HIGH_VALUE | — | — |
| 7 | RiskAnalysisModelMapPEOIsActive | IS_ACTIVE | — | — |
| 8 | RiskAnalysisModelMapPEOIsSddFlg | IS_SEEDED_FLAG | — | — |
| 9 | RiskAnalysisModelMapPEOIsSeeded | IS_SEEDED | — | — |
| 10 | RiskAnalysisModelMapPEOLabel | LABEL | — | ✅ |
| 11 | RiskAnalysisModelMapPEOLowValue | LOW_VALUE | — | — |
| 12 | RiskAnalysisModelMapPEOLstUpdtDt | LAST_UPDATE_DATE | — | — |
| 13 | RiskAnalysisModelMapPEOLstUpdtLgn | LAST_UPDATE_LOGIN | — | — |
| 14 | RiskAnalysisModelMapPEOLstUpdtdBy | LAST_UPDATED_BY | — | — |
| 15 | RiskAnalysisModelMapPEOMdlMapId | RISK_ANALYSIS_MODEL_MAP_ID | — | ✅ |
| 16 | RiskAnalysisModelMapPEOObjVerNum | OBJECT_VERSION_NUMBER | — | — |
| 17 | RiskAnalysisModelMapPEORevisionDt | REVISION_DATE | — | — |
| 18 | RiskAnalysisModelMapPEORskAnlysMdlId | RISK_ANALYSIS_MODEL_ID | — | — |
| 19 | RiskAnalysisModelMapPEOSeedDS | SEED_DATA_SOURCE | — | — |

### [[grc_rsk_anls_mdlmap_b|GRC_RSK_ANLS_MDLMAP_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskAnalysisMapBasePEOBindKey | BIND_KEY | — | — |
| 2 | RiskAnalysisMapBasePEOCreatedBy | CREATED_BY | — | — |
| 3 | RiskAnalysisMapBasePEOCreationDate | CREATION_DATE | — | — |
| 4 | RiskAnalysisMapBasePEODisplayOrder | DISPLAY_ORDER | — | — |
| 5 | RiskAnalysisMapBasePEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 6 | RiskAnalysisMapBasePEOHighValue | HIGH_VALUE | — | — |
| 7 | RiskAnalysisMapBasePEOIsSeededFlag | IS_SEEDED_FLAG | — | — |
| 8 | RiskAnalysisMapBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | RiskAnalysisMapBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | RiskAnalysisMapBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | RiskAnalysisMapBasePEOLowValue | LOW_VALUE | — | — |
| 12 | RiskAnalysisMapBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | RiskAnalysisMapBasePEORevisionDate | REVISION_DATE | — | — |
| 14 | RiskAnalysisMapBasePEORiskAnalysisModelId | RISK_ANALYSIS_MODEL_ID | — | — |
| 15 | RiskAnalysisMapBasePEORiskAnalysisModelMapId | RISK_ANALYSIS_MODEL_MAP_ID | — | — |

### [[grc_rsk_anls_mdl_tl|GRC_RSK_ANLS_MDL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskAnalysisMdlTransPEOBindKey | BIND_KEY | — | — |
| 2 | RiskAnalysisMdlTransPEOCreatedBy | CREATED_BY | — | — |
| 3 | RiskAnalysisMdlTransPEOCreationDate | CREATION_DATE | — | — |
| 4 | RiskAnalysisMdlTransPEOLanguage | LANGUAGE | — | — |
| 5 | RiskAnalysisMdlTransPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | RiskAnalysisMdlTransPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | RiskAnalysisMdlTransPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | RiskAnalysisMdlTransPEOName | NAME | — | ✅ |
| 9 | RiskAnalysisMdlTransPEORiskAnalysisModelId | RISK_ANALYSIS_MODEL_ID | — | — |
| 10 | RiskAnalysisMdlTransPEOSourceLang | SOURCE_LANG | — | — |

### [[grc_rsk_evaluation_b|GRC_RSK_EVALUATION_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskEvaluationBasePEOCatastrophic | CATASTROPHIC | — | — |
| 2 | RiskEvaluationBasePEOCompletedBy | COMPLETED_BY | — | — |
| 3 | RiskEvaluationBasePEOCompletedDate | COMPLETED_DATE | — | — |
| 4 | RiskEvaluationBasePEOCreatedBy | CREATED_BY | — | — |
| 5 | RiskEvaluationBasePEOCreationDate | CREATION_DATE | — | — |
| 6 | RiskEvaluationBasePEODueDate | DUE_DATE | — | — |
| 7 | RiskEvaluationBasePEOLastStateCode | LAST_STATE_CODE | — | — |
| 8 | RiskEvaluationBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | RiskEvaluationBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | RiskEvaluationBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | RiskEvaluationBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | RiskEvaluationBasePEORiskEvaluationDate | RISK_EVALUATION_DATE | — | — |
| 13 | RiskEvaluationBasePEORiskEvaluationId | RISK_EVALUATION_ID | — | — |
| 14 | RiskEvaluationBasePEORiskId | RISK_ID | — | — |
| 15 | RiskEvaluationBasePEORiskRating | RISK_RATING | — | ✅ |
| 16 | RiskEvaluationBasePEOStateCode | STATE_CODE | — | — |
| 17 | RiskEvaluationBasePEOStateDate | STATE_DATE | — | — |
| 18 | RiskEvaluationBasePEOStatus | STATUS | — | — |
| 19 | RiskEvaluationBasePEOTargetCompletionDate | TARGET_COMPLETION_DATE | — | — |

### [[grc_rsk_impact_model_vl|GRC_RSK_IMPACT_MODEL_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskImpactModelVLPEOAnalsTypCd | ANALYSIS_TYPE_CODE | — | — |
| 2 | RiskImpactModelVLPEOApprCompDt | APPROVE_COMPLETE_DATE | — | — |
| 3 | RiskImpactModelVLPEOAttrCat | ATTRIBUTE_CATEGORY | — | — |
| 4 | RiskImpactModelVLPEOBindKey | BIND_KEY | — | — |
| 5 | RiskImpactModelVLPEOCurrCode | CURRENCY_CODE | — | — |
| 6 | RiskImpactModelVLPEODtlDescr | DETAILED_DESCRIPTION | — | — |
| 7 | RiskImpactModelVLPEOEffSeq | EFFECTIVE_SEQUENCE | — | — |
| 8 | RiskImpactModelVLPEOImpactMdlId | IMPACT_MODEL_ID | — | — |
| 9 | RiskImpactModelVLPEOIsActive | IS_ACTIVE | — | — |
| 10 | RiskImpactModelVLPEOIsDefault | IS_DEFAULT | — | — |
| 11 | RiskImpactModelVLPEOIsSddFlg | IS_SEEDED_FLAG | — | — |
| 12 | RiskImpactModelVLPEOIsSeeded | IS_SEEDED | — | — |
| 13 | RiskImpactModelVLPEOLstStateCode | LAST_STATE_CODE | — | — |
| 14 | RiskImpactModelVLPEOName | NAME | — | ✅ |
| 15 | RiskImpactModelVLPEOObjVerNum | OBJECT_VERSION_NUMBER | — | — |
| 16 | RiskImpactModelVLPEORevDate | REVISION_DATE | — | — |
| 17 | RiskImpactModelVLPEORevStartDate1 | REVIEW_START_DATE | — | — |
| 18 | RiskImpactModelVLPEOSeedDS | SEED_DATA_SOURCE | — | — |
| 19 | RiskImpactModelVLPEOStateCode | STATE_CODE | — | — |
| 20 | RiskImpactModelVLPEOStateDate | STATE_DATE | — | — |
| 21 | RiskImpactModelVLPEOStatus | STATUS | — | — |
| 22 | RiskImpactModelVLPEOTotRevs | TOTAL_REVISIONS | — | — |

### [[grc_rsk_impact_param_vl|GRC_RSK_IMPACT_PARAM_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskImpactParamPEOAnalysTypCd | ANALYSIS_TYPE_CODE | — | — |
| 2 | RiskImpactParamPEOBindKey | BIND_KEY | — | — |
| 3 | RiskImpactParamPEOCreatedBy | CREATED_BY | — | — |
| 4 | RiskImpactParamPEOCreationDate | CREATION_DATE | — | — |
| 5 | RiskImpactParamPEOEffSeq | EFFECTIVE_SEQUENCE | — | — |
| 6 | RiskImpactParamPEOHighValue | HIGH_VALUE | — | — |
| 7 | RiskImpactParamPEOImpactMdlId | IMPACT_MODEL_ID | — | — |
| 8 | RiskImpactParamPEOImpctParamId | IMPACT_PARAM_ID | — | ✅ |
| 9 | RiskImpactParamPEOIsActive | IS_ACTIVE | — | — |
| 10 | RiskImpactParamPEOIsSeeded | IS_SEEDED | — | — |
| 11 | RiskImpactParamPEOIsSeededFlg | IS_SEEDED_FLAG | — | — |
| 12 | RiskImpactParamPEOLabel | LABEL | — | ✅ |
| 13 | RiskImpactParamPEOLowValue | LOW_VALUE | — | — |
| 14 | RiskImpactParamPEOLstUpdtDt | LAST_UPDATE_DATE | — | — |
| 15 | RiskImpactParamPEOLstUpdtLgn | LAST_UPDATE_LOGIN | — | — |
| 16 | RiskImpactParamPEOLstUpdtdBy | LAST_UPDATED_BY | — | — |
| 17 | RiskImpactParamPEOObjVerNum | OBJECT_VERSION_NUMBER | — | — |
| 18 | RiskImpactParamPEORating | RATING | — | — |
| 19 | RiskImpactParamPEORevisionDt | REVISION_DATE | — | — |
| 20 | RiskImpactParamPEOSeedDS | SEED_DATA_SOURCE | — | — |
| 21 | RiskImpactParamPEOSequence | SEQUENCE | — | — |

### [[grc_rsk_likelihood_model_vl|GRC_RSK_LIKELIHOOD_MODEL_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskLikelihoodModelVLPEOAnlsTypCd | ANALYSIS_TYPE_CODE | — | — |
| 2 | RiskLikelihoodModelVLPEOApprCmplDt | APPROVE_COMPLETE_DATE | — | — |
| 3 | RiskLikelihoodModelVLPEOAttrCat | ATTRIBUTE_CATEGORY | — | — |
| 4 | RiskLikelihoodModelVLPEOBindKey | BIND_KEY | — | — |
| 5 | RiskLikelihoodModelVLPEODtldDescr | DETAILED_DESCRIPTION | — | — |
| 6 | RiskLikelihoodModelVLPEOEffSeq | EFFECTIVE_SEQUENCE | — | — |
| 7 | RiskLikelihoodModelVLPEOIsActive | IS_ACTIVE | — | — |
| 8 | RiskLikelihoodModelVLPEOIsDefault | IS_DEFAULT | — | — |
| 9 | RiskLikelihoodModelVLPEOIsSddFlg | IS_SEEDED_FLAG | — | — |
| 10 | RiskLikelihoodModelVLPEOIsSeeded | IS_SEEDED | — | — |
| 11 | RiskLikelihoodModelVLPEOLklhdMdlId | LIKELIHOOD_MODEL_ID | — | — |
| 12 | RiskLikelihoodModelVLPEOLklhdType | LIKELIHOOD_TYPE | — | — |
| 13 | RiskLikelihoodModelVLPEOLstStateCode | LAST_STATE_CODE | — | — |
| 14 | RiskLikelihoodModelVLPEOName | NAME | — | ✅ |
| 15 | RiskLikelihoodModelVLPEOObjVerNum | OBJECT_VERSION_NUMBER | — | — |
| 16 | RiskLikelihoodModelVLPEORevStartDate | REVIEW_START_DATE | — | — |
| 17 | RiskLikelihoodModelVLPEORevnDate | REVISION_DATE | — | — |
| 18 | RiskLikelihoodModelVLPEOSeedDS | SEED_DATA_SOURCE | — | — |
| 19 | RiskLikelihoodModelVLPEOStateCode | STATE_CODE | — | — |
| 20 | RiskLikelihoodModelVLPEOStateDate | STATE_DATE | — | — |
| 21 | RiskLikelihoodModelVLPEOStatus | STATUS | — | — |
| 22 | RiskLikelihoodModelVLPEOTotRevs | TOTAL_REVISIONS | — | — |

### [[grc_rsk_likelihood_param_vl|GRC_RSK_LIKELIHOOD_PARAM_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskLikelihoodParamPEOAnlysTypCd | ANALYSIS_TYPE_CODE | — | — |
| 2 | RiskLikelihoodParamPEOBindKey | BIND_KEY | — | — |
| 3 | RiskLikelihoodParamPEOCreatedBy | CREATED_BY | — | — |
| 4 | RiskLikelihoodParamPEOCreationDt | CREATION_DATE | — | — |
| 5 | RiskLikelihoodParamPEOEffSeq | EFFECTIVE_SEQUENCE | — | — |
| 6 | RiskLikelihoodParamPEOHighValue | HIGH_VALUE | — | — |
| 7 | RiskLikelihoodParamPEOIsActive | IS_ACTIVE | — | — |
| 8 | RiskLikelihoodParamPEOIsSeeded | IS_SEEDED | — | — |
| 9 | RiskLikelihoodParamPEOIsSeededFlag | IS_SEEDED_FLAG | — | — |
| 10 | RiskLikelihoodParamPEOLabel | LABEL | — | ✅ |
| 11 | RiskLikelihoodParamPEOLastUpdtDt | LAST_UPDATE_DATE | — | — |
| 12 | RiskLikelihoodParamPEOLastUpdtLgn | LAST_UPDATE_LOGIN | — | — |
| 13 | RiskLikelihoodParamPEOLastUpdtdBy | LAST_UPDATED_BY | — | — |
| 14 | RiskLikelihoodParamPEOLklhdMdlId | LIKELIHOOD_MODEL_ID | — | — |
| 15 | RiskLikelihoodParamPEOLklhdParId | LIKELIHOOD_PARAM_ID | — | ✅ |
| 16 | RiskLikelihoodParamPEOLowValue | LOW_VALUE | — | — |
| 17 | RiskLikelihoodParamPEOObjVerNum | OBJECT_VERSION_NUMBER | — | — |
| 18 | RiskLikelihoodParamPEORating | RATING | — | — |
| 19 | RiskLikelihoodParamPEORevDate | REVISION_DATE | — | — |
| 20 | RiskLikelihoodParamPEOSeedDS | SEED_DATA_SOURCE | — | — |
| 21 | RiskLikelihoodParamPEOSequence | SEQUENCE | — | — |

### [[grc_rsk_risk_b|GRC_RSK_RISK_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskBasePEORiskId | RISK_ID | — | — |

### [[grc_rsk_risk_tl|GRC_RSK_RISK_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskTranslationPEOLanguage | LANGUAGE | — | — |
| 2 | RiskTranslationPEOName | NAME | — | ✅ |
| 3 | RiskTranslationPEORiskId | RISK_ID | — | — |

### [[grc_rsk_trtmntp_b|GRC_RSK_TRTMNTP_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskTreatmentPlanBasePEOCreatedBy | CREATED_BY | — | — |
| 2 | RiskTreatmentPlanBasePEOCreationDate | CREATION_DATE | — | — |
| 3 | RiskTreatmentPlanBasePEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 4 | RiskTreatmentPlanBasePEOInUseIndicator | IN_USE_INDICATOR | — | — |
| 5 | RiskTreatmentPlanBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 6 | RiskTreatmentPlanBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | RiskTreatmentPlanBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | RiskTreatmentPlanBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | RiskTreatmentPlanBasePEOResidualImpactParamId | RESIDUAL_IMPACT_PARAM_ID | — | — |
| 10 | RiskTreatmentPlanBasePEOResidualLikelihoodParamId | RESIDUAL_LIKELIHOOD_PARAM_ID | — | — |
| 11 | RiskTreatmentPlanBasePEOResidualRiskLevel | RESIDUAL_RISK_LEVEL | — | — |
| 12 | RiskTreatmentPlanBasePEOResidualRiskLevelMapId | RESIDUAL_RISK_LEVEL_MAP_ID | — | — |
| 13 | RiskTreatmentPlanBasePEORevisionDate | REVISION_DATE | — | — |
| 14 | RiskTreatmentPlanBasePEORiskId | RISK_ID | — | — |
| 15 | RiskTreatmentPlanBasePEOTargetPlanIndicator | TARGET_PLAN_INDICATOR | — | ✅ |
| 16 | RiskTreatmentPlanBasePEOTreatmentPlanId | TREATMENT_PLAN_ID | — | ✅ |

### [[grc_rsk_trtmntp_tl|GRC_RSK_TRTMNTP_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskTreatmentPlanTransPEOCreatedBy | CREATED_BY | — | — |
| 2 | RiskTreatmentPlanTransPEOCreationDate | CREATION_DATE | — | — |
| 3 | RiskTreatmentPlanTransPEODtlDescr | DETAILED_DESCRIPTION | — | ✅ |
| 4 | RiskTreatmentPlanTransPEOLanguage | LANGUAGE | — | — |
| 5 | RiskTreatmentPlanTransPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 6 | RiskTreatmentPlanTransPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | RiskTreatmentPlanTransPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | RiskTreatmentPlanTransPEOName | NAME | — | ✅ |
| 9 | RiskTreatmentPlanTransPEOSourceLang | SOURCE_LANG | — | — |
| 10 | RiskTreatmentPlanTransPEOTreatmentPlanId | TREATMENT_PLAN_ID | — | — |

### [[gtg_otbi_risk_details|GTG_OTBI_RISK_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskAnalysisDetailsPEORskSign | RISK_SIGNIFICANCE | — | ✅ |
| 2 | RiskAnalysisDetailsPEORskSignLbl | RISK_SIGNIFICANCE_LABEL | — | ✅ |
| 3 | RiskAnalysisDetailsPEOTrgtImpct | TARGET_IMPACT | — | ✅ |
| 4 | RiskAnalysisDetailsPEOTrgtLklhd | TARGET_LIKELIHOOD | — | ✅ |
| 5 | RiskAnalysisDetailsPEOTrgtRskLvl | TARGET_RISK_LEVEL | — | ✅ |

### [[gtg_otbi_rsk_analysis_dtl|GTG_OTBI_RSK_ANALYSIS_DTL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskAnlsDetailsPEOAnalysisId | ANALYSIS_ID | — | — |
| 2 | RiskAnlsDetailsPEOCreatedBy | CREATED_BY | — | — |
| 3 | RiskAnlsDetailsPEOCreationDate | CREATION_DATE | — | — |
| 4 | RiskAnlsDetailsPEOInhRiskImpct | INHERENT_RISK_IMPACT | — | ✅ |
| 5 | RiskAnlsDetailsPEOInhRskImpLbl | INHERENT_RISK_IMPACT_LABEL | — | ✅ |
| 6 | RiskAnlsDetailsPEOInhRskLiklhd | INHERENT_RISK_LIKELIHOOD | — | ✅ |
| 7 | RiskAnlsDetailsPEOInhRskLklhdLbl | INHERENT_RISK_LIKELIHOOD_LABEL | — | ✅ |
| 8 | RiskAnlsDetailsPEOInhRskLvl | INHERENT_RISK_LEVEL | — | ✅ |
| 9 | RiskAnlsDetailsPEOInhRskLvlLbl | INHERENT_RISK_LEVEL_LABEL | — | ✅ |
| 10 | RiskAnlsDetailsPEOLstUpdatDt | LAST_UPDATE_DATE | — | — |
| 11 | RiskAnlsDetailsPEOLstUpdtLgn | LAST_UPDATE_LOGIN | — | — |
| 12 | RiskAnlsDetailsPEOLstUpdtdBy | LAST_UPDATED_BY | — | — |
| 13 | RiskAnlsDetailsPEORiskId | RISK_ID | — | — |

### [[gtg_otbi_rsk_evl_dtl|GTG_OTBI_RSK_EVL_DTL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskEvalDetailPEOCreatedBy | CREATED_BY | — | — |
| 2 | RiskEvalDetailPEOCreationDate | CREATION_DATE | — | — |
| 3 | RiskEvalDetailPEOEvaluationId | EVALUATION_ID | — | — |
| 4 | RiskEvalDetailPEOEvaluationResult | EVALUATION_RESULT | — | ✅ |
| 5 | RiskEvalDetailPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | RiskEvalDetailPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | RiskEvalDetailPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | RiskEvalDetailPEORiskId | RISK_ID | — | — |
| 9 | RiskEvalDetailPEORiskSigLabel | RISK_SIGNIFICANCE_LABEL | — | ✅ |
| 10 | RiskEvalDetailPEORiskSignificance | RISK_SIGNIFICANCE | — | ✅ |

### [[gtg_otbi_rsk_trtmnt_dtl|GTG_OTBI_RSK_TRTMNT_DTL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskTrtmntDetailPEOAnalysisId | ANALYSIS_ID | — | — |
| 2 | RiskTrtmntDetailPEOCreatedBy | CREATED_BY | — | — |
| 3 | RiskTrtmntDetailPEOCreationDate | CREATION_DATE | — | — |
| 4 | RiskTrtmntDetailPEOInhRskLklhdLbl | INHERENT_RISK_LIKELIHOOD_LABEL | — | ✅ |
| 5 | RiskTrtmntDetailPEOInhRskLvlLbl | INHERENT_RISK_LEVEL_LABEL | — | ✅ |
| 6 | RiskTrtmntDetailPEOInhrRskImpLabel | INHERENT_RISK_IMPACT_LABEL | — | ✅ |
| 7 | RiskTrtmntDetailPEOInhrntRskImpct | INHERENT_RISK_IMPACT | — | ✅ |
| 8 | RiskTrtmntDetailPEOInhrntRskLevel | INHERENT_RISK_LEVEL | — | ✅ |
| 9 | RiskTrtmntDetailPEOInhrntRskLklhd | INHERENT_RISK_LIKELIHOOD | — | ✅ |
| 10 | RiskTrtmntDetailPEOInusTrtmntCost | INUSE_TREATMENT_COST | — | ✅ |
| 11 | RiskTrtmntDetailPEOInuseTreatmentCostOrig | INUSE_TREATMENT_COST_ORIG | — | — |
| 12 | RiskTrtmntDetailPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | RiskTrtmntDetailPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | RiskTrtmntDetailPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | RiskTrtmntDetailPEOResidualImpactLabelOrig | RESIDUAL_IMPACT_LABEL_ORIG | — | — |
| 16 | RiskTrtmntDetailPEOResidualImpactOrig | RESIDUAL_IMPACT_ORIG | — | — |
| 17 | RiskTrtmntDetailPEOResidualLikelihoodLabelOrig | RESIDUAL_LIKELIHOOD_LABEL_ORIG | — | — |
| 18 | RiskTrtmntDetailPEOResidualLikelihoodOrig | RESIDUAL_LIKELIHOOD_ORIG | — | — |
| 19 | RiskTrtmntDetailPEOResidualRiskLevelLabelOrig | RESIDUAL_RISK_LEVEL_LABEL_ORIG | — | — |
| 20 | RiskTrtmntDetailPEOResidualRiskLevelOrig | RESIDUAL_RISK_LEVEL_ORIG | — | — |
| 21 | RiskTrtmntDetailPEORiskId | RISK_ID | — | — |
| 22 | RiskTrtmntDetailPEORsdlImpctLabel | RESIDUAL_IMPACT_LABEL | — | ✅ |
| 23 | RiskTrtmntDetailPEORsdlLklhd | RESIDUAL_LIKELIHOOD | — | ✅ |
| 24 | RiskTrtmntDetailPEORsdlLklhdLabel | RESIDUAL_LIKELIHOOD_LABEL | — | ✅ |
| 25 | RiskTrtmntDetailPEORsdlRskLvlLabel | RESIDUAL_RISK_LEVEL_LABEL | — | ✅ |
| 26 | RiskTrtmntDetailPEORsdulImpct | RESIDUAL_IMPACT | — | ✅ |
| 27 | RiskTrtmntDetailPEORsdulRskLvl | RESIDUAL_RISK_LEVEL | — | ✅ |
| 28 | RiskTrtmntDetailPEOTargetImpactLabelOrig | TARGET_IMPACT_LABEL_ORIG | — | — |
| 29 | RiskTrtmntDetailPEOTargetImpactOrig | TARGET_IMPACT_ORIG | — | — |
| 30 | RiskTrtmntDetailPEOTargetLikelihoodLabelOrig | TARGET_LIKELIHOOD_LABEL_ORIG | — | — |
| 31 | RiskTrtmntDetailPEOTargetLikelihoodOrig | TARGET_LIKELIHOOD_ORIG | — | — |
| 32 | RiskTrtmntDetailPEOTargetRiskLevelLabelOrig | TARGET_RISK_LEVEL_LABEL_ORIG | — | — |
| 33 | RiskTrtmntDetailPEOTargetRiskLevelOrig | TARGET_RISK_LEVEL_ORIG | — | — |
| 34 | RiskTrtmntDetailPEOTargetTreatmentCostOrig | TARGET_TREATMENT_COST_ORIG | — | — |
| 35 | RiskTrtmntDetailPEOTotalTrtmntCost | TOTAL_TREATMENT_COST | — | ✅ |
| 36 | RiskTrtmntDetailPEOTrgtImpactLabel | TARGET_IMPACT_LABEL | — | ✅ |
| 37 | RiskTrtmntDetailPEOTrgtImpct | TARGET_IMPACT | — | ✅ |
| 38 | RiskTrtmntDetailPEOTrgtLklihd | TARGET_LIKELIHOOD | — | ✅ |
| 39 | RiskTrtmntDetailPEOTrgtLklihdlbl | TARGET_LIKELIHOOD_LABEL | — | ✅ |
| 40 | RiskTrtmntDetailPEOTrgtRskLvl | TARGET_RISK_LEVEL | — | ✅ |
| 41 | RiskTrtmntDetailPEOTrgtRsklvllbl | TARGET_RISK_LEVEL_LABEL | — | ✅ |
| 42 | RiskTrtmntDetailPEOTrgtTrtmntCost | TARGET_TREATMENT_COST | — | ✅ |
| 43 | RiskTrtmntDetailPEOTrtmntPlnId | TREATMENT_PLAN_ID | — | — |

### [[gtg_sc_frc_access_v|GTG_SC_FRC_ACCESS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FRCSecurityPEOSecurableId | SECURABLE_ID | — | — |
| 2 | FRCSecurityPEOSecurableType | SECURABLE_TYPE | — | — |
| 3 | FRCSecurityPEOUserId | USER_ID | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RskAnlPersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | RskAnlPersonCreatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | RskAnlPersonCreatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | RskAnlPersonCreatedByPersonId | PERSON_ID | — | — |
| 5 | RskAnlPersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | RskAnlPersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 7 | RskAnlPersonUpdatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | RskAnlPersonUpdatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | RskAnlPersonUpdatedByPersonId | PERSON_ID | — | — |
| 10 | RskAnlPersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RskAnlCreatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | RskAnlCreatedByPersonId | PERSON_ID | — | — |
| 3 | RskAnlCreatedByUserGuid | USER_GUID | — | — |
| 4 | RskAnlCreatedByUserId | USER_ID | — | — |
| 5 | RskAnlCreatedByUsername | USERNAME | — | — |
| 6 | RskAnlUpdatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | RskAnlUpdatedByPersonId | PERSON_ID | — | — |
| 8 | RskAnlUpdatedByUserGuid | USER_GUID | — | — |
| 9 | RskAnlUpdatedByUserId | USER_ID | — | — |
| 10 | RskAnlUpdatedByUsername | USERNAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
