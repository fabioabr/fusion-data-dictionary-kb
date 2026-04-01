---
id: DOC-OTHER-PVO-RiskEvaluationPVO
doc_type: system-doc
title: "RiskEvaluationPVO — PVO Cross-Module"
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
  - RiskEvaluationPVO
  - riskevaluationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RiskEvaluationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Risk Evaluation. Acessa as tabelas: GRC_RSK_ANLS_MDL_B, GRC_RSK_CRITERIA, GRC_RSK_CRITERIA_DETAIL_VL (+9).

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.RiskEvaluationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 179 | 12 | 1 | 32 | 18% |

---

## 🔗 Tabelas Relacionadas

- [[grc_rsk_anls_mdl_b|GRC_RSK_ANLS_MDL_B]] — 21 atributos (1 BICC)
- [[grc_rsk_criteria|GRC_RSK_CRITERIA]] — 16 atributos
- [[grc_rsk_criteria_detail_vl|GRC_RSK_CRITERIA_DETAIL_VL]] — 19 atributos (1 BICC)
- [[grc_rsk_criteria_name_vl|GRC_RSK_CRITERIA_NAME_VL]] — 15 atributos (1 BICC)
- [[grc_rsk_crit_dtl_b|GRC_RSK_CRIT_DTL_B]] — 14 atributos (3 BICC)
- [[grc_rsk_evaluation_b|GRC_RSK_EVALUATION_B]] — 19 atributos (1 PKs, 13 BICC)
- [[grc_rsk_evaluation_dtl|GRC_RSK_EVALUATION_DTL]] — 9 atributos (1 BICC)
- [[grc_rsk_evaluation_tl|GRC_RSK_EVALUATION_TL]] — 10 atributos (4 BICC)
- [[grc_rsk_risk_b|GRC_RSK_RISK_B]] — 26 atributos
- [[gtg_otbi_rsk_evl_dtl|GTG_OTBI_RSK_EVL_DTL]] — 10 atributos (6 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos (2 BICC)
- [[per_users|PER_USERS]] — 10 atributos

---

## ⚙️ Atributos

### [[grc_rsk_anls_mdl_b|GRC_RSK_ANLS_MDL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IsActive | IS_ACTIVE | — | — |
| 2 | RiskAnalysisModelIdAnlsTypeCd | ANALYSIS_TYPE_CODE | — | ✅ |
| 3 | RiskAnalysisModelIdApprComplDate | APPROVE_COMPLETE_DATE | — | — |
| 4 | RiskAnalysisModelIdAttrCat | ATTRIBUTE_CATEGORY | — | — |
| 5 | RiskAnalysisModelIdBindKey | BIND_KEY | — | — |
| 6 | RiskAnalysisModelIdEffSeq | EFFECTIVE_SEQUENCE | — | — |
| 7 | RiskAnalysisModelIdFactor | FACTOR1 | — | — |
| 8 | RiskAnalysisModelIdFactor2 | FACTOR2 | — | — |
| 9 | RiskAnalysisModelIdFormulaCode | FORMULA_CODE | — | — |
| 10 | RiskAnalysisModelIdIsSeeded | IS_SEEDED | — | — |
| 11 | RiskAnalysisModelIdIsSeededFlag | IS_SEEDED_FLAG | — | — |
| 12 | RiskAnalysisModelIdLstStateCode | LAST_STATE_CODE | — | — |
| 13 | RiskAnalysisModelIdObjVerNum | OBJECT_VERSION_NUMBER | — | — |
| 14 | RiskAnalysisModelIdRevStartDate | REVIEW_START_DATE | — | — |
| 15 | RiskAnalysisModelIdRevisionDate | REVISION_DATE | — | — |
| 16 | RiskAnalysisModelIdRskAnlsMdlId | RISK_ANALYSIS_MODEL_ID | — | — |
| 17 | RiskAnalysisModelIdSeedDS | SEED_DATA_SOURCE | — | — |
| 18 | RiskAnalysisModelIdStateCode | STATE_CODE | — | — |
| 19 | RiskAnalysisModelIdStateDate | STATE_DATE | — | — |
| 20 | RiskAnalysisModelIdStatus | STATUS | — | — |
| 21 | RiskAnalysisModelIdWeight | WEIGHT | — | — |

### [[grc_rsk_criteria|GRC_RSK_CRITERIA]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskCriteriaPEOCreatdBy | CREATED_BY | — | — |
| 2 | RiskCriteriaPEOCreationDt | CREATION_DATE | — | — |
| 3 | RiskCriteriaPEOCritNameId | CRITERIA_NAME_ID | — | — |
| 4 | RiskCriteriaPEOEffSeq | EFFECTIVE_SEQUENCE | — | — |
| 5 | RiskCriteriaPEOIsActive | IS_ACTIVE | — | — |
| 6 | RiskCriteriaPEOIsSddFlg | IS_SEEDED_FLAG | — | — |
| 7 | RiskCriteriaPEOIsSeeded | IS_SEEDED | — | — |
| 8 | RiskCriteriaPEOLstUpdtDt | LAST_UPDATE_DATE | — | — |
| 9 | RiskCriteriaPEOLstUpdtLgn | LAST_UPDATE_LOGIN | — | — |
| 10 | RiskCriteriaPEOLstUpdtdBy | LAST_UPDATED_BY | — | — |
| 11 | RiskCriteriaPEOObjVerNum | OBJECT_VERSION_NUMBER | — | — |
| 12 | RiskCriteriaPEORevsnDt | REVISION_DATE | — | — |
| 13 | RiskCriteriaPEORiskCntxtMdlId | RISK_CONTEXT_MODEL_ID | — | — |
| 14 | RiskCriteriaPEORiskCritId | RISK_CRITERIA_ID | — | — |
| 15 | RiskCriteriaPEOSeedDataSrc | SEED_DATA_SOURCE | — | — |
| 16 | RiskCriteriaPEOSequence | SEQUENCE | — | — |

### [[grc_rsk_criteria_detail_vl|GRC_RSK_CRITERIA_DETAIL_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskCritDtlVLPEOBindKey | BIND_KEY | — | — |
| 2 | RiskCritDtlVLPEOCreatdBy | CREATED_BY | — | — |
| 3 | RiskCritDtlVLPEOCreatnDt | CREATION_DATE | — | — |
| 4 | RiskCritDtlVLPEOCritDtlId | CRITERIA_DETAIL_ID | — | — |
| 5 | RiskCritDtlVLPEOEffSeq | EFFECTIVE_SEQUENCE | — | — |
| 6 | RiskCritDtlVLPEOIsActive | IS_ACTIVE | — | — |
| 7 | RiskCritDtlVLPEOIsSeedFlg | IS_SEEDED_FLAG | — | — |
| 8 | RiskCritDtlVLPEOIsSeeded | IS_SEEDED | — | — |
| 9 | RiskCritDtlVLPEOLabel | LABEL | — | ✅ |
| 10 | RiskCritDtlVLPEOLstUpdtDt | LAST_UPDATE_DATE | — | — |
| 11 | RiskCritDtlVLPEOLstUpdtLgn | LAST_UPDATE_LOGIN | — | — |
| 12 | RiskCritDtlVLPEOLstUpdtdBy | LAST_UPDATED_BY | — | — |
| 13 | RiskCritDtlVLPEOObjVerNum | OBJECT_VERSION_NUMBER | — | — |
| 14 | RiskCritDtlVLPEORating | RATING | — | — |
| 15 | RiskCritDtlVLPEORowId | ROW_ID | — | — |
| 16 | RiskCritDtlVLPEORskCritId | RISK_CRITERIA_ID | — | — |
| 17 | RiskCritDtlVLPEORvsnDate | REVISION_DATE | — | — |
| 18 | RiskCritDtlVLPEOSeedDataSrc | SEED_DATA_SOURCE | — | — |
| 19 | RiskCritDtlVLPEOTlrnceCd | TOLERANCE_CODE | — | — |

### [[grc_rsk_criteria_name_vl|GRC_RSK_CRITERIA_NAME_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskCritNameVLPEOBindKey | BIND_KEY | — | — |
| 2 | RiskCritNameVLPEOCreatdBy | CREATED_BY | — | — |
| 3 | RiskCritNameVLPEOCreationDt | CREATION_DATE | — | — |
| 4 | RiskCritNameVLPEOCritNameId | CRITERIA_NAME_ID | — | — |
| 5 | RiskCritNameVLPEODtldDescr | DETAILED_DESCRIPTION | — | — |
| 6 | RiskCritNameVLPEOIsAct | IS_ACTIVE | — | — |
| 7 | RiskCritNameVLPEOIsSeed | IS_SEEDED | — | — |
| 8 | RiskCritNameVLPEOIsSeededFlg | IS_SEEDED_FLAG | — | — |
| 9 | RiskCritNameVLPEOLstUpdtDt | LAST_UPDATE_DATE | — | — |
| 10 | RiskCritNameVLPEOLstUpdtLgn | LAST_UPDATE_LOGIN | — | — |
| 11 | RiskCritNameVLPEOLstUpdtdBy | LAST_UPDATED_BY | — | — |
| 12 | RiskCritNameVLPEOName | NAME | — | ✅ |
| 13 | RiskCritNameVLPEOObjVerNum | OBJECT_VERSION_NUMBER | — | — |
| 14 | RiskCritNameVLPEORowId | ROW_ID | — | — |
| 15 | RiskCritNameVLPEOSeedDataSrc | SEED_DATA_SOURCE | — | — |

### [[grc_rsk_crit_dtl_b|GRC_RSK_CRIT_DTL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskCriteriaDetailPEOBindKey | BIND_KEY | — | — |
| 2 | RiskCriteriaDetailPEOCreatedBy | CREATED_BY | — | — |
| 3 | RiskCriteriaDetailPEOCreationDate | CREATION_DATE | — | — |
| 4 | RiskCriteriaDetailPEOCriteriaDetailId | CRITERIA_DETAIL_ID | — | — |
| 5 | RiskCriteriaDetailPEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 6 | RiskCriteriaDetailPEOIsSeededFlag | IS_SEEDED_FLAG | — | — |
| 7 | RiskCriteriaDetailPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | RiskCriteriaDetailPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | RiskCriteriaDetailPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | RiskCriteriaDetailPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | RiskCriteriaDetailPEORating | RATING | — | ✅ |
| 12 | RiskCriteriaDetailPEORevisionDate | REVISION_DATE | — | — |
| 13 | RiskCriteriaDetailPEORiskCriteriaId | RISK_CRITERIA_ID | — | — |
| 14 | RiskCriteriaDetailPEOToleranceCode | TOLERANCE_CODE | — | ✅ |

### [[grc_rsk_evaluation_b|GRC_RSK_EVALUATION_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskEvaluationBasePEOCatastrophic | CATASTROPHIC | — | ✅ |
| 2 | RiskEvaluationBasePEOCompletedBy | COMPLETED_BY | — | — |
| 3 | RiskEvaluationBasePEOCompletedDate | COMPLETED_DATE | — | ✅ |
| 4 | RiskEvaluationBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | RiskEvaluationBasePEOCreationDate | CREATION_DATE | — | — |
| 6 | RiskEvaluationBasePEODueDate | DUE_DATE | — | ✅ |
| 7 | RiskEvaluationBasePEOLastStateCode | LAST_STATE_CODE | — | ✅ |
| 8 | RiskEvaluationBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | RiskEvaluationBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | RiskEvaluationBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | RiskEvaluationBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | RiskEvaluationBasePEORiskEvaluationDate | RISK_EVALUATION_DATE | — | ✅ |
| 13 | RiskEvaluationBasePEORiskEvaluationId | RISK_EVALUATION_ID | 🔑 | ✅ |
| 14 | RiskEvaluationBasePEORiskId | RISK_ID | — | ✅ |
| 15 | RiskEvaluationBasePEORiskRating | RISK_RATING | — | ✅ |
| 16 | RiskEvaluationBasePEOStateCode | STATE_CODE | — | ✅ |
| 17 | RiskEvaluationBasePEOStateDate | STATE_DATE | — | — |
| 18 | RiskEvaluationBasePEOStatus | STATUS | — | ✅ |
| 19 | RiskEvaluationBasePEOTargetCompletionDate | TARGET_COMPLETION_DATE | — | — |

### [[grc_rsk_evaluation_dtl|GRC_RSK_EVALUATION_DTL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskEvaluationDetailPEOCreatedBy | CREATED_BY | — | — |
| 2 | RiskEvaluationDetailPEOCreationDate | CREATION_DATE | — | — |
| 3 | RiskEvaluationDetailPEOCriteriaDetailId | CRITERIA_DETAIL_ID | — | — |
| 4 | RiskEvaluationDetailPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | RiskEvaluationDetailPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | RiskEvaluationDetailPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | RiskEvaluationDetailPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | RiskEvaluationDetailPEORiskCriteriaId | RISK_CRITERIA_ID | — | — |
| 9 | RiskEvaluationDetailPEORiskEvaluationId | RISK_EVALUATION_ID | — | — |

### [[grc_rsk_evaluation_tl|GRC_RSK_EVALUATION_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskEvaluationTransPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | RiskEvaluationTransPEOCreationDate | CREATION_DATE | — | — |
| 3 | RiskEvaluationTransPEODescription | DESCRIPTION | — | — |
| 4 | RiskEvaluationTransPEODetailedDescription | DETAILED_DESCRIPTION | — | ✅ |
| 5 | RiskEvaluationTransPEOLanguage | LANGUAGE | — | — |
| 6 | RiskEvaluationTransPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | RiskEvaluationTransPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | RiskEvaluationTransPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | RiskEvaluationTransPEORiskEvaluationId | RISK_EVALUATION_ID | — | — |
| 10 | RiskEvaluationTransPEOSourceLang | SOURCE_LANG | — | — |

### [[grc_rsk_risk_b|GRC_RSK_RISK_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskBasePEOAccessType | ACCESS_TYPE | — | — |
| 2 | RiskBasePEOApprCompleteDate1 | APPROVE_COMPLETE_DATE | — | — |
| 3 | RiskBasePEOApprovedBy | APPROVED_BY | — | — |
| 4 | RiskBasePEOApprovedDate | APPROVED_DATE | — | — |
| 5 | RiskBasePEOAttrCat | ATTRIBUTE_CATEGORY | — | — |
| 6 | RiskBasePEOCategoryCode | CATEGORY_CODE | — | — |
| 7 | RiskBasePEOCurrencyCode | CURRENCY_CODE | — | — |
| 8 | RiskBasePEOEffSeq | EFFECTIVE_SEQUENCE | — | — |
| 9 | RiskBasePEOFlexObjectTypeId | FLEX_OBJECT_TYPE_ID | — | — |
| 10 | RiskBasePEOFlxPerspItemId | FLX_PERSP_ITEM_ID | — | — |
| 11 | RiskBasePEOLastStateCode | LAST_STATE_CODE | — | — |
| 12 | RiskBasePEOObjVerNum | OBJECT_VERSION_NUMBER | — | — |
| 13 | RiskBasePEOProposedRiskId | PROPOSED_RISK_ID | — | — |
| 14 | RiskBasePEORevDate | REVISION_DATE | — | — |
| 15 | RiskBasePEORevSubmittedBy | REVISION_SUBMITTED_BY | — | — |
| 16 | RiskBasePEOReviewStartDate | REVIEW_START_DATE | — | — |
| 17 | RiskBasePEOReviewedBy | REVIEWED_BY | — | — |
| 18 | RiskBasePEOReviewedDate | REVIEWED_DATE | — | — |
| 19 | RiskBasePEORevisionNumber | REVISION_NUMBER | — | — |
| 20 | RiskBasePEORiskId | RISK_ID | — | — |
| 21 | RiskBasePEORskAnlysMdlId | RISK_ANALYSIS_MODEL_ID | — | — |
| 22 | RiskBasePEORskCntxtMdlId | RISK_CONTEXT_MODEL_ID | — | — |
| 23 | RiskBasePEOStateCode | STATE_CODE | — | — |
| 24 | RiskBasePEOStateDate | STATE_DATE | — | — |
| 25 | RiskBasePEOStatus | STATUS | — | — |
| 26 | RiskBasePEOType | TYPE | — | — |

### [[gtg_otbi_rsk_evl_dtl|GTG_OTBI_RSK_EVL_DTL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskEvalDetailPEOCreatedBy | CREATED_BY | — | — |
| 2 | RiskEvalDetailPEOCreationDate | CREATION_DATE | — | — |
| 3 | RiskEvalDetailPEOEvaluationId | EVALUATION_ID | — | ✅ |
| 4 | RiskEvalDetailPEOEvaluationResult | EVALUATION_RESULT | — | ✅ |
| 5 | RiskEvalDetailPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | RiskEvalDetailPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | RiskEvalDetailPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | RiskEvalDetailPEORiskId | RISK_ID | — | — |
| 9 | RiskEvalDetailPEORiskSigLabel | RISK_SIGNIFICANCE_LABEL | — | ✅ |
| 10 | RiskEvalDetailPEORiskSignificance | RISK_SIGNIFICANCE | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RskEvlPersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | RskEvlPersonCreatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | RskEvlPersonCreatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | RskEvlPersonCreatedByPersonId | PERSON_ID | — | — |
| 5 | RskEvlPersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | RskEvlPersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 7 | RskEvlPersonUpdatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | RskEvlPersonUpdatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | RskEvlPersonUpdatedByPersonId | PERSON_ID | — | — |
| 10 | RskEvlPersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RskEvlCreatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | RskEvlCreatedByPersonId | PERSON_ID | — | — |
| 3 | RskEvlCreatedByUserGuid | USER_GUID | — | — |
| 4 | RskEvlCreatedByUserId | USER_ID | — | — |
| 5 | RskEvlCreatedByUsername | USERNAME | — | — |
| 6 | RskEvlUpdatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | RskEvlUpdatedByPersonId | PERSON_ID | — | — |
| 8 | RskEvlUpdatedByUserGuid | USER_GUID | — | — |
| 9 | RskEvlUpdatedByUserId | USER_ID | — | — |
| 10 | RskEvlUpdatedByUsername | USERNAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
