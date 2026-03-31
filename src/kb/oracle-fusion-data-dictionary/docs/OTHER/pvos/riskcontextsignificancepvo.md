---
id: DOC-OTHER-PVO-RiskContextSignificancePVO
doc_type: system-doc
title: "RiskContextSignificancePVO — PVO Cross-Module"
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
  - RiskContextSignificancePVO
  - riskcontextsignificancepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RiskContextSignificancePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Risk Context Significance. Acessa as tabelas: GRC_RSK_CONTEXT_MDL_B, GRC_RSK_CONTEXT_MDL_TL, GRC_RSK_SIG_DETAIL_VL (+2).

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.RiskContextSignificancePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 75 | 5 | 2 | 14 | 19% |

---

## 🔗 Tabelas Relacionadas

- [[grc_rsk_context_mdl_b|GRC_RSK_CONTEXT_MDL_B]] — 19 atributos (2 PKs, 3 BICC)
- [[grc_rsk_context_mdl_tl|GRC_RSK_CONTEXT_MDL_TL]] — 11 atributos (2 BICC)
- [[grc_rsk_sig_detail_vl|GRC_RSK_SIG_DETAIL_VL]] — 18 atributos (5 BICC)
- [[grc_rsk_sig_model_b|GRC_RSK_SIG_MODEL_B]] — 17 atributos (2 BICC)
- [[grc_rsk_sig_model_tl|GRC_RSK_SIG_MODEL_TL]] — 10 atributos (2 BICC)

---

## ⚙️ Atributos

### [[grc_rsk_context_mdl_b|GRC_RSK_CONTEXT_MDL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskContextBasePEOApproveCompleteDate | APPROVE_COMPLETE_DATE | — | — |
| 2 | RiskContextBasePEOBindKey | BIND_KEY | 🔑 | ✅ |
| 3 | RiskContextBasePEOCreatedBy | CREATED_BY | — | — |
| 4 | RiskContextBasePEOCreationDate | CREATION_DATE | — | — |
| 5 | RiskContextBasePEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 6 | RiskContextBasePEOIsSeededFlag | IS_SEEDED_FLAG | — | — |
| 7 | RiskContextBasePEOLastStateCode | LAST_STATE_CODE | — | — |
| 8 | RiskContextBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | RiskContextBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | RiskContextBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | RiskContextBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | RiskContextBasePEOReviewStartDate | REVIEW_START_DATE | — | — |
| 13 | RiskContextBasePEORevisionDate | REVISION_DATE | — | — |
| 14 | RiskContextBasePEORevisionNumber | REVISION_NUMBER | — | — |
| 15 | RiskContextBasePEORiskContextModelId | RISK_CONTEXT_MODEL_ID | 🔑 | ✅ |
| 16 | RiskContextBasePEORiskSignificanceModelId | RISK_SIGNIFICANCE_MODEL_ID | — | — |
| 17 | RiskContextBasePEOStateCode | STATE_CODE | — | — |
| 18 | RiskContextBasePEOStateDate | STATE_DATE | — | — |
| 19 | RiskContextBasePEOStatus | STATUS | — | — |

### [[grc_rsk_context_mdl_tl|GRC_RSK_CONTEXT_MDL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskContextTranslationPEOBindKey | BIND_KEY | — | — |
| 2 | RiskContextTranslationPEOCreatedBy | CREATED_BY | — | — |
| 3 | RiskContextTranslationPEOCreationDate | CREATION_DATE | — | — |
| 4 | RiskContextTranslationPEOLanguage | LANGUAGE | — | — |
| 5 | RiskContextTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | RiskContextTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | RiskContextTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | RiskContextTranslationPEOName | NAME | — | ✅ |
| 9 | RiskContextTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | RiskContextTranslationPEORiskContextModelId | RISK_CONTEXT_MODEL_ID | — | — |
| 11 | RiskContextTranslationPEOSourceLang | SOURCE_LANG | — | — |

### [[grc_rsk_sig_detail_vl|GRC_RSK_SIG_DETAIL_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskSignificanceDetailPEOBindKey | BIND_KEY | — | — |
| 2 | RiskSignificanceDetailPEOCreatedBy | CREATED_BY | — | — |
| 3 | RiskSignificanceDetailPEOCreationDate | CREATION_DATE | — | — |
| 4 | RiskSignificanceDetailPEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 5 | RiskSignificanceDetailPEOIsActive | IS_ACTIVE | — | — |
| 6 | RiskSignificanceDetailPEOIsSeeded | IS_SEEDED | — | — |
| 7 | RiskSignificanceDetailPEOIsSeededFlag | IS_SEEDED_FLAG | — | — |
| 8 | RiskSignificanceDetailPEOLabel | LABEL | — | ✅ |
| 9 | RiskSignificanceDetailPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | RiskSignificanceDetailPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | RiskSignificanceDetailPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | RiskSignificanceDetailPEOMaximumNum | MAXIMUM_NUM | — | ✅ |
| 13 | RiskSignificanceDetailPEOMinimumNum | MINIMUM_NUM | — | ✅ |
| 14 | RiskSignificanceDetailPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | RiskSignificanceDetailPEORevisionDate | REVISION_DATE | — | — |
| 16 | RiskSignificanceDetailPEORiskSigDetailId | RISK_SIG_DETAIL_ID | — | ✅ |
| 17 | RiskSignificanceDetailPEORiskSignificanceModelId | RISK_SIGNIFICANCE_MODEL_ID | — | — |
| 18 | RiskSignificanceDetailPEOSeedDS | SEED_DATA_SOURCE | — | — |

### [[grc_rsk_sig_model_b|GRC_RSK_SIG_MODEL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskSignificanceBasePEOApproveCompleteDate | APPROVE_COMPLETE_DATE | — | — |
| 2 | RiskSignificanceBasePEOBindKey | BIND_KEY | — | — |
| 3 | RiskSignificanceBasePEOCreatedBy | CREATED_BY | — | — |
| 4 | RiskSignificanceBasePEOCreationDate | CREATION_DATE | — | — |
| 5 | RiskSignificanceBasePEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 6 | RiskSignificanceBasePEOIsSeededFlag | IS_SEEDED_FLAG | — | — |
| 7 | RiskSignificanceBasePEOLastStateCode | LAST_STATE_CODE | — | — |
| 8 | RiskSignificanceBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | RiskSignificanceBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | RiskSignificanceBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | RiskSignificanceBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | RiskSignificanceBasePEOReviewStartDate | REVIEW_START_DATE | — | — |
| 13 | RiskSignificanceBasePEORevisionDate | REVISION_DATE | — | — |
| 14 | RiskSignificanceBasePEORiskSignificanceModelId | RISK_SIGNIFICANCE_MODEL_ID | — | ✅ |
| 15 | RiskSignificanceBasePEOStateCode | STATE_CODE | — | — |
| 16 | RiskSignificanceBasePEOStateDate | STATE_DATE | — | — |
| 17 | RiskSignificanceBasePEOStatus | STATUS | — | — |

### [[grc_rsk_sig_model_tl|GRC_RSK_SIG_MODEL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskSignificanceTransPEOBindKey | BIND_KEY | — | — |
| 2 | RiskSignificanceTransPEOCreatedBy | CREATED_BY | — | — |
| 3 | RiskSignificanceTransPEOCreationDate | CREATION_DATE | — | — |
| 4 | RiskSignificanceTransPEOLanguage | LANGUAGE | — | — |
| 5 | RiskSignificanceTransPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | RiskSignificanceTransPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | RiskSignificanceTransPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | RiskSignificanceTransPEOName | NAME | — | ✅ |
| 9 | RiskSignificanceTransPEORiskSignificanceModelId | RISK_SIGNIFICANCE_MODEL_ID | — | — |
| 10 | RiskSignificanceTransPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
