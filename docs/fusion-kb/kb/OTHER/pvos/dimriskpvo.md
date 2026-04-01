---
id: DOC-OTHER-PVO-DimRiskPVO
doc_type: system-doc
title: "DimRiskPVO — PVO Cross-Module"
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
  - DimRiskPVO
  - dimriskpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DimRiskPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Dim Risk. Acessa as tabelas: FND_CURRENCIES_TL, GRC_RSK_ANLS_MDL_TL, GRC_RSK_RISK_B (+8).

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.DimRiskPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 136 | 11 | 1 | 41 | 30% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_currencies_tl|FND_CURRENCIES_TL]] — 12 atributos (3 BICC)
- [[grc_rsk_anls_mdl_tl|GRC_RSK_ANLS_MDL_TL]] — 10 atributos
- [[grc_rsk_risk_b|GRC_RSK_RISK_B]] — 28 atributos (1 PKs, 14 BICC)
- [[grc_rsk_risk_tl|GRC_RSK_RISK_TL]] — 10 atributos (3 BICC)
- [[gtg_sc_frc_access_v|GTG_SC_FRC_ACCESS_V]] — 3 atributos
- [[gtg_sc_frc_security_v|GTG_SC_FRC_SECURITY_V]] — 15 atributos (10 BICC)
- [[gtg_sc_group_vl|GTG_SC_GROUP_VL]] — 5 atributos (4 BICC)
- [[gtg_sc_securable_to_priv|GTG_SC_SECURABLE_TO_PRIV]] — 4 atributos (1 BICC)
- [[gtg_sc_user_group|GTG_SC_USER_GROUP]] — 9 atributos (2 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 20 atributos (4 BICC)
- [[per_users|PER_USERS]] — 20 atributos

---

## ⚙️ Atributos

### [[fnd_currencies_tl|FND_CURRENCIES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CurrencyPEOCreatedBy | CREATED_BY | — | — |
| 2 | CurrencyPEOCreationDate | CREATION_DATE | — | — |
| 3 | CurrencyPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 4 | CurrencyPEODescription | DESCRIPTION | — | — |
| 5 | CurrencyPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 6 | CurrencyPEOLanguage | LANGUAGE | — | — |
| 7 | CurrencyPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | CurrencyPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | CurrencyPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | CurrencyPEOName | NAME | — | ✅ |
| 11 | CurrencyPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 12 | CurrencyPEOSourceLang | SOURCE_LANG | — | — |

### [[grc_rsk_anls_mdl_tl|GRC_RSK_ANLS_MDL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskAnalysisMdlTransPEOBindKey | BIND_KEY | — | — |
| 2 | RiskAnalysisMdlTransPEOCreatedBy | CREATED_BY | — | — |
| 3 | RiskAnalysisMdlTransPEOCreationDate | CREATION_DATE | — | — |
| 4 | RiskAnalysisMdlTransPEOLanguage | LANGUAGE | — | — |
| 5 | RiskAnalysisMdlTransPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 6 | RiskAnalysisMdlTransPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | RiskAnalysisMdlTransPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | RiskAnalysisMdlTransPEOName | NAME | — | — |
| 9 | RiskAnalysisMdlTransPEORiskAnalysisModelId | RISK_ANALYSIS_MODEL_ID | — | — |
| 10 | RiskAnalysisMdlTransPEOSourceLang | SOURCE_LANG | — | — |

### [[grc_rsk_risk_b|GRC_RSK_RISK_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskBasePEOApproveCompleteDate | APPROVE_COMPLETE_DATE | — | — |
| 2 | RiskBasePEOApprovedBy | APPROVED_BY | — | ✅ |
| 3 | RiskBasePEOApprovedDate | APPROVED_DATE | — | ✅ |
| 4 | RiskBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | RiskBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | RiskBasePEOCurrencyCode | CURRENCY_CODE | — | — |
| 7 | RiskBasePEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 8 | RiskBasePEOFlexObjectTypeId | FLEX_OBJECT_TYPE_ID | — | — |
| 9 | RiskBasePEOFlxPerspItemId | FLX_PERSP_ITEM_ID | — | — |
| 10 | RiskBasePEOLastStateCode | LAST_STATE_CODE | — | — |
| 11 | RiskBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | RiskBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | RiskBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | RiskBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | RiskBasePEOProposedRiskId | PROPOSED_RISK_ID | — | — |
| 16 | RiskBasePEOReviewStartDate | REVIEW_START_DATE | — | — |
| 17 | RiskBasePEOReviewedBy | REVIEWED_BY | — | ✅ |
| 18 | RiskBasePEOReviewedDate | REVIEWED_DATE | — | ✅ |
| 19 | RiskBasePEORevisionDate | REVISION_DATE | — | ✅ |
| 20 | RiskBasePEORevisionNumber | REVISION_NUMBER | — | ✅ |
| 21 | RiskBasePEORevisionSubmittedBy | REVISION_SUBMITTED_BY | — | — |
| 22 | RiskBasePEORiskAnalysisModelId | RISK_ANALYSIS_MODEL_ID | — | — |
| 23 | RiskBasePEORiskContextModelId | RISK_CONTEXT_MODEL_ID | — | — |
| 24 | RiskBasePEORiskId | RISK_ID | 🔑 | ✅ |
| 25 | RiskBasePEOStateCode | STATE_CODE | — | ✅ |
| 26 | RiskBasePEOStateDate | STATE_DATE | — | — |
| 27 | RiskBasePEOStatus | STATUS | — | ✅ |
| 28 | RiskBasePEOType | TYPE | — | ✅ |

### [[grc_rsk_risk_tl|GRC_RSK_RISK_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | RiskTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | RiskTranslationPEODetailedDescription | DETAILED_DESCRIPTION | — | ✅ |
| 4 | RiskTranslationPEOLanguage | LANGUAGE | — | — |
| 5 | RiskTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | RiskTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | RiskTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | RiskTranslationPEOName | NAME | — | ✅ |
| 9 | RiskTranslationPEORiskId | RISK_ID | — | — |
| 10 | RiskTranslationPEOSourceLang | SOURCE_LANG | — | — |

### [[gtg_sc_frc_access_v|GTG_SC_FRC_ACCESS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FRCSecurityPEOSecurableId | SECURABLE_ID | — | — |
| 2 | FRCSecurityPEOSecurableType | SECURABLE_TYPE | — | — |
| 3 | FRCSecurityPEOUserId | USER_ID | — | — |

### [[gtg_sc_frc_security_v|GTG_SC_FRC_SECURITY_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FRCScSecurityPEOAccessorId | ACCESSOR_ID | — | ✅ |
| 2 | FRCScSecurityPEOAccessorType | ACCESSOR_TYPE | — | — |
| 3 | FRCScSecurityPEOId | ID | — | — |
| 4 | FRCScSecurityPEOIsApprover | IS_APPROVER | — | ✅ |
| 5 | FRCScSecurityPEOIsAssessor | IS_ASSESSOR | — | ✅ |
| 6 | FRCScSecurityPEOIsEditor | IS_EDITOR | — | ✅ |
| 7 | FRCScSecurityPEOIsIssueOwner | IS_ISSUE_OWNER | — | ✅ |
| 8 | FRCScSecurityPEOIsIssueValidator | IS_ISSUE_VALIDATOR | — | ✅ |
| 9 | FRCScSecurityPEOIsManager | IS_MANAGER | — | ✅ |
| 10 | FRCScSecurityPEOIsOwner | IS_OWNER | — | ✅ |
| 11 | FRCScSecurityPEOIsReviewer | IS_REVIEWER | — | ✅ |
| 12 | FRCScSecurityPEOIsViewer | IS_VIEWER | — | ✅ |
| 13 | FRCScSecurityPEORoleBitmap | ROLE_BITMAP | — | — |
| 14 | FRCScSecurityPEOSecurableId | SECURABLE_ID | — | — |
| 15 | FRCScSecurityPEOSecurableType | SECURABLE_TYPE | — | — |

### [[gtg_sc_group_vl|GTG_SC_GROUP_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SecurityGroupPEOGroupId | GROUP_ID | — | ✅ |
| 2 | SecurityGroupPEOName | NAME | — | ✅ |
| 3 | SecurityGroupPEOObjVerNum | OBJECT_VERSION_NUMBER | — | — |
| 4 | SecurityGroupPEORoleType | ROLE_TYPE | — | ✅ |
| 5 | SecurityGroupPEOSecurableType | SECURABLE_TYPE | — | ✅ |

### [[gtg_sc_securable_to_priv|GTG_SC_SECURABLE_TO_PRIV]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ScSecurityPrivPEOId | ID | — | — |
| 2 | ScSecurityPrivPEOPrivilegeCode | PRIVILEGE_CODE | — | — |
| 3 | ScSecurityPrivPEORoleType | ROLE_TYPE | — | ✅ |
| 4 | ScSecurityPrivPEOSecurableType | SECURABLE_TYPE | — | — |

### [[gtg_sc_user_group|GTG_SC_USER_GROUP]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ScSecurityUserGroupPEOCreatedBy | CREATED_BY | — | — |
| 2 | ScSecurityUserGroupPEOCrtnDt | CREATION_DATE | — | — |
| 3 | ScSecurityUserGroupPEOGroupId | GROUP_ID | — | — |
| 4 | ScSecurityUserGroupPEOId | ID | — | — |
| 5 | ScSecurityUserGroupPEOIsOrphan | IS_ORPHAN | — | ✅ |
| 6 | ScSecurityUserGroupPEOLstUpdtDt | LAST_UPDATE_DATE | — | — |
| 7 | ScSecurityUserGroupPEOLstUpdtLgn | LAST_UPDATE_LOGIN | — | — |
| 8 | ScSecurityUserGroupPEOLstUpdtdBy | LAST_UPDATED_BY | — | — |
| 9 | ScSecurityUserGroupPEOUserId | USER_ID | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskPersonApprovedByDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | RiskPersonApprovedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | RiskPersonApprovedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | RiskPersonApprovedByPersonId | PERSON_ID | — | — |
| 5 | RiskPersonApprovedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | RiskPersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 7 | RiskPersonCreatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | RiskPersonCreatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | RiskPersonCreatedByPersonId | PERSON_ID | — | — |
| 10 | RiskPersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 11 | RiskPersonReviewedByDisplayName | DISPLAY_NAME | — | ✅ |
| 12 | RiskPersonReviewedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 13 | RiskPersonReviewedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 14 | RiskPersonReviewedByPersonId | PERSON_ID | — | — |
| 15 | RiskPersonReviewedByPersonNameId | PERSON_NAME_ID | — | — |
| 16 | RiskPersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 17 | RiskPersonUpdatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 18 | RiskPersonUpdatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 19 | RiskPersonUpdatedByPersonId | PERSON_ID | — | — |
| 20 | RiskPersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RiskApprovedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | RiskApprovedByPersonId | PERSON_ID | — | — |
| 3 | RiskApprovedByUserGuid | USER_GUID | — | — |
| 4 | RiskApprovedByUserId | USER_ID | — | — |
| 5 | RiskApprovedByUsername | USERNAME | — | — |
| 6 | RiskCreatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | RiskCreatedByPersonId | PERSON_ID | — | — |
| 8 | RiskCreatedByUserGuid | USER_GUID | — | — |
| 9 | RiskCreatedByUserId | USER_ID | — | — |
| 10 | RiskCreatedByUsername | USERNAME | — | — |
| 11 | RiskReviewedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | RiskReviewedByPersonId | PERSON_ID | — | — |
| 13 | RiskReviewedByUserGuid | USER_GUID | — | — |
| 14 | RiskReviewedByUserId | USER_ID | — | — |
| 15 | RiskReviewedByUsername | USERNAME | — | — |
| 16 | RiskUpdatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | RiskUpdatedByPersonId | PERSON_ID | — | — |
| 18 | RiskUpdatedByUserGuid | USER_GUID | — | — |
| 19 | RiskUpdatedByUserId | USER_ID | — | — |
| 20 | RiskUpdatedByUsername | USERNAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
