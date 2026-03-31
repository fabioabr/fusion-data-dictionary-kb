---
id: DOC-OTHER-PVO-PSCPermitTypePVO
doc_type: system-doc
title: "PSCPermitTypePVO — PVO Cross-Module"
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
  - PSCPermitTypePVO
  - pscpermittypepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PSCPermitTypePVO

## 📌 Visão Geral

View Object para extração BICC de dados de PSCPermit Type. Acessa as tabelas: PSC_BNP_BILL_TYPE_TL, PSC_ERP_DEPARTMENT_TL, PSC_INS_INSPECTION_GROUP_TL (+5).

**Caminho:** `FscmTopModelAM.PscPermitsReportingAM.PSCPermitTypePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 136 | 8 | 1 | 22 | 16% |

---

## 🔗 Tabelas Relacionadas

- [[psc_bnp_bill_type_tl|PSC_BNP_BILL_TYPE_TL]] — 11 atributos (1 BICC)
- [[psc_erp_department_tl|PSC_ERP_DEPARTMENT_TL]] — 10 atributos (1 BICC)
- [[psc_ins_inspection_group_tl|PSC_INS_INSPECTION_GROUP_TL]] — 11 atributos (1 BICC)
- [[psc_lnp_appl_group_tl|PSC_LNP_APPL_GROUP_TL]] — 10 atributos (1 BICC)
- [[psc_lnp_category_tl|PSC_LNP_CATEGORY_TL]] — 10 atributos (1 BICC)
- [[psc_lnp_record_type_b|PSC_LNP_RECORD_TYPE_B]] — 64 atributos (1 PKs, 15 BICC)
- [[psc_lnp_record_type_tl|PSC_LNP_RECORD_TYPE_TL]] — 10 atributos (1 BICC)
- [[psc_lnp_subcategory_tl|PSC_LNP_SUBCATEGORY_TL]] — 10 atributos (1 BICC)

---

## ⚙️ Atributos

### [[psc_bnp_bill_type_tl|PSC_BNP_BILL_TYPE_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PermitBillTypeTLPEOAgencyId | AGENCY_ID | — | — |
| 2 | PermitBillTypeTLPEOBillType | BILL_TYPE | — | — |
| 3 | PermitBillTypeTLPEOCreatedBy | CREATED_BY | — | — |
| 4 | PermitBillTypeTLPEOCreationDate | CREATION_DATE | — | — |
| 5 | PermitBillTypeTLPEODescription | DESCRIPTION | — | ✅ |
| 6 | PermitBillTypeTLPEOLanguage | LANGUAGE | — | — |
| 7 | PermitBillTypeTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 8 | PermitBillTypeTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | PermitBillTypeTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | PermitBillTypeTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | PermitBillTypeTLPEOSourceLang | SOURCE_LANG | — | — |

### [[psc_erp_department_tl|PSC_ERP_DEPARTMENT_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PermitDepartmentTLPEOAgencyId | AGENCY_ID | — | — |
| 2 | PermitDepartmentTLPEOCreatedBy | CREATED_BY | — | — |
| 3 | PermitDepartmentTLPEOCreationDate | CREATION_DATE | — | — |
| 4 | PermitDepartmentTLPEODepartmentId | DEPARTMENT_ID | — | — |
| 5 | PermitDepartmentTLPEODescription | DESCRIPTION | — | ✅ |
| 6 | PermitDepartmentTLPEOLanguage | LANGUAGE | — | — |
| 7 | PermitDepartmentTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 8 | PermitDepartmentTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | PermitDepartmentTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | PermitDepartmentTLPEOSourceLang | SOURCE_LANG | — | — |

### [[psc_ins_inspection_group_tl|PSC_INS_INSPECTION_GROUP_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InspectionGroupTLPEOAgencyId | AGENCY_ID | — | — |
| 2 | InspectionGroupTLPEOCreatedBy | CREATED_BY | — | — |
| 3 | InspectionGroupTLPEOCreationDate | CREATION_DATE | — | — |
| 4 | InspectionGroupTLPEODescription | DESCRIPTION | — | ✅ |
| 5 | InspectionGroupTLPEOInspectionGroup | INSPECTION_GROUP | — | — |
| 6 | InspectionGroupTLPEOLanguage | LANGUAGE | — | — |
| 7 | InspectionGroupTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 8 | InspectionGroupTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | InspectionGroupTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | InspectionGroupTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | InspectionGroupTLPEOSourceLang | SOURCE_LANG | — | — |

### [[psc_lnp_appl_group_tl|PSC_LNP_APPL_GROUP_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApplicationGroupTLPEOAgencyId | AGENCY_ID | — | — |
| 2 | ApplicationGroupTLPEOApplGroup | APPL_GROUP | — | — |
| 3 | ApplicationGroupTLPEOCreatedBy | CREATED_BY | — | — |
| 4 | ApplicationGroupTLPEOCreationDate | CREATION_DATE | — | — |
| 5 | ApplicationGroupTLPEODescription | DESCRIPTION | — | ✅ |
| 6 | ApplicationGroupTLPEOLanguage | LANGUAGE | — | — |
| 7 | ApplicationGroupTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 8 | ApplicationGroupTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ApplicationGroupTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ApplicationGroupTLPEOSourceLang | SOURCE_LANG | — | — |

### [[psc_lnp_category_tl|PSC_LNP_CATEGORY_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CategoryTLPEOAgencyId | AGENCY_ID | — | — |
| 2 | CategoryTLPEOCategory | CATEGORY | — | — |
| 3 | CategoryTLPEOCreatedBy | CREATED_BY | — | — |
| 4 | CategoryTLPEOCreationDate | CREATION_DATE | — | — |
| 5 | CategoryTLPEODescription | DESCRIPTION | — | ✅ |
| 6 | CategoryTLPEOLanguage | LANGUAGE | — | — |
| 7 | CategoryTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 8 | CategoryTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | CategoryTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | CategoryTLPEOSourceLang | SOURCE_LANG | — | — |

### [[psc_lnp_record_type_b|PSC_LNP_RECORD_TYPE_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PermitTypePEOActivityGroupId | ACTIVITY_GROUP_ID | — | — |
| 2 | PermitTypePEOAgencyId | AGENCY_ID | — | — |
| 3 | PermitTypePEOAllowPublicUserView | ALLOW_PUBLIC_USER_VIEW | — | — |
| 4 | PermitTypePEOApplGroup | APPL_GROUP | — | ✅ |
| 5 | PermitTypePEOBillType | BILL_TYPE | — | ✅ |
| 6 | PermitTypePEOCategory | CATEGORY | — | ✅ |
| 7 | PermitTypePEOCitizenEnabled | CITIZEN_ENABLED | — | ✅ |
| 8 | PermitTypePEOClassification | CLASSIFICATION | — | — |
| 9 | PermitTypePEOCntrctrValidationGroupId | CNTRCTR_VALIDATION_GROUP_ID | — | — |
| 10 | PermitTypePEOCoaReportId | COA_REPORT_ID | — | — |
| 11 | PermitTypePEOCoaTemplateId | COA_TEMPLATE_ID | — | — |
| 12 | PermitTypePEOCreatedBy | CREATED_BY | — | — |
| 13 | PermitTypePEOCreationDate | CREATION_DATE | — | — |
| 14 | PermitTypePEODepartmentId | DEPARTMENT_ID | — | ✅ |
| 15 | PermitTypePEODocGroupId | DOC_GROUP_ID | — | — |
| 16 | PermitTypePEOExpirationAmend | EXPIRATION_AMEND | — | — |
| 17 | PermitTypePEOExpirationGroupId | EXPIRATION_GROUP_ID | — | — |
| 18 | PermitTypePEOExpirationRenew | EXPIRATION_RENEW | — | — |
| 19 | PermitTypePEOFeeScheduleId | FEE_SCHEDULE_ID | — | — |
| 20 | PermitTypePEOHearingOption | HEARING_OPTION | — | — |
| 21 | PermitTypePEOInspectionGroup | INSPECTION_GROUP | — | ✅ |
| 22 | PermitTypePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 23 | PermitTypePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 24 | PermitTypePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 25 | PermitTypePEOMeetTemplateId | MEET_TEMPLATE_ID | — | — |
| 26 | PermitTypePEOModuleId | MODULE_ID | — | — |
| 27 | PermitTypePEONaicsGroupCode | NAICS_GROUP_CODE | — | — |
| 28 | PermitTypePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 29 | PermitTypePEOOpaPolicyName | OPA_POLICY_NAME | — | — |
| 30 | PermitTypePEOOpaPolicyVersion | OPA_POLICY_VERSION | — | — |
| 31 | PermitTypePEOPlanReview | PLAN_REVIEW | — | — |
| 32 | PermitTypePEORecordTypeCode | RECORD_TYPE_CODE | — | ✅ |
| 33 | PermitTypePEORecordTypeId | RECORD_TYPE_ID | 🔑 | ✅ |
| 34 | PermitTypePEORecordTypeState | RECORD_TYPE_STATE | — | ✅ |
| 35 | PermitTypePEORenewalRuleId | RENEWAL_RULE_ID | — | — |
| 36 | PermitTypePEOReportControlId | REPORT_CONTROL_ID | — | — |
| 37 | PermitTypePEOReportGroup | REPORT_GROUP | — | — |
| 38 | PermitTypePEOReviewerAutoAssign | REVIEWER_AUTO_ASSIGN | — | — |
| 39 | PermitTypePEORuleId | RULE_ID | — | ✅ |
| 40 | PermitTypePEOSubcategory | SUBCATEGORY | — | ✅ |
| 41 | PermitTypePEOSubclassification | SUBCLASSIFICATION | — | — |
| 42 | PermitTypePEOTaxClassCode | TAX_CLASS_CODE | — | — |
| 43 | PermitTypePEOTermsUseId | TERMS_USE_ID | — | — |
| 44 | PermitTypePEOTransPeriodFormat | TRANS_PERIOD_FORMAT | — | — |
| 45 | PermitTypePEOUrl | URL | — | — |
| 46 | PermitTypePEOValidFromDate | VALID_FROM_DATE | — | ✅ |
| 47 | PermitTypePEOValidToDate | VALID_TO_DATE | — | ✅ |
| 48 | PermitTypePEOWfNoOrigFlag | WF_NO_ORIG_FLAG | — | — |
| 49 | PermitTypePEOWfNoRenewFlag | WF_NO_RENEW_FLAG | — | — |
| 50 | PermitTypePEOWfProcDefIdAmend | WF_PROC_DEF_ID_AMEND | — | — |
| 51 | PermitTypePEOWfProcDefIdOrig | WF_PROC_DEF_ID_ORIG | — | ✅ |
| 52 | PermitTypePEOWfProcDefIdRenew | WF_PROC_DEF_ID_RENEW | — | — |
| 53 | PermitTypePEOWfProcVersionAmend | WF_PROC_VERSION_AMEND | — | — |
| 54 | PermitTypePEOWfProcVersionOrig | WF_PROC_VERSION_ORIG | — | — |
| 55 | PermitTypePEOWfProcVersionRenew | WF_PROC_VERSION_RENEW | — | — |
| 56 | PermitTypePEOWfProjectAmend | WF_PROJECT_AMEND | — | — |
| 57 | PermitTypePEOWfProjectOrig | WF_PROJECT_ORIG | — | — |
| 58 | PermitTypePEOWfProjectRenew | WF_PROJECT_RENEW | — | — |
| 59 | PermitTypePEOWfSpaceAmend | WF_SPACE_AMEND | — | — |
| 60 | PermitTypePEOWfSpaceNameAmend | WF_SPACE_NAME_AMEND | — | — |
| 61 | PermitTypePEOWfSpaceNameOrig | WF_SPACE_NAME_ORIG | — | — |
| 62 | PermitTypePEOWfSpaceNameRenew | WF_SPACE_NAME_RENEW | — | — |
| 63 | PermitTypePEOWfSpaceOrig | WF_SPACE_ORIG | — | — |
| 64 | PermitTypePEOWfSpaceRenew | WF_SPACE_RENEW | — | — |

### [[psc_lnp_record_type_tl|PSC_LNP_RECORD_TYPE_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PermitTypeTLPEOCreatedBy | CREATED_BY | — | — |
| 2 | PermitTypeTLPEOCreationDate | CREATION_DATE | — | — |
| 3 | PermitTypeTLPEOLanguage | LANGUAGE | — | — |
| 4 | PermitTypeTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 5 | PermitTypeTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | PermitTypeTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | PermitTypeTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | PermitTypeTLPEORecordType | RECORD_TYPE | — | ✅ |
| 9 | PermitTypeTLPEORecordTypeId | RECORD_TYPE_ID | — | — |
| 10 | PermitTypeTLPEOSourceLang | SOURCE_LANG | — | — |

### [[psc_lnp_subcategory_tl|PSC_LNP_SUBCATEGORY_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SubCategoryTLPEOAgencyId | AGENCY_ID | — | — |
| 2 | SubCategoryTLPEOCreatedBy | CREATED_BY | — | — |
| 3 | SubCategoryTLPEOCreationDate | CREATION_DATE | — | — |
| 4 | SubCategoryTLPEODescription | DESCRIPTION | — | ✅ |
| 5 | SubCategoryTLPEOLanguage | LANGUAGE | — | — |
| 6 | SubCategoryTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | SubCategoryTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | SubCategoryTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | SubCategoryTLPEOSourceLang | SOURCE_LANG | — | — |
| 10 | SubCategoryTLPEOSubcategory | SUBCATEGORY | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
