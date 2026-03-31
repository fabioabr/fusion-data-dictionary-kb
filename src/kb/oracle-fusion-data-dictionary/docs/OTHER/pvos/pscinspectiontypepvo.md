---
id: DOC-OTHER-PVO-PSCInspectionTypePVO
doc_type: system-doc
title: "PSCInspectionTypePVO — PVO Cross-Module"
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
  - PSCInspectionTypePVO
  - pscinspectiontypepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PSCInspectionTypePVO

## 📌 Visão Geral

View Object para extração BICC de dados de PSCInspection Type. Acessa as tabelas: PSC_BNP_BILL_TYPE_TL, PSC_INS_ASSESSMENT_TYPE_TL, PSC_INS_INSPECTION_TYPE_B (+3).

**Caminho:** `FscmTopModelAM.PscPermitsReportingAM.PSCInspectionTypePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 85 | 6 | 2 | 13 | 15% |

---

## 🔗 Tabelas Relacionadas

- [[psc_bnp_bill_type_tl|PSC_BNP_BILL_TYPE_TL]] — 11 atributos
- [[psc_ins_assessment_type_tl|PSC_INS_ASSESSMENT_TYPE_TL]] — 11 atributos (1 BICC)
- [[psc_ins_inspection_type_b|PSC_INS_INSPECTION_TYPE_B]] — 30 atributos (2 PKs, 9 BICC)
- [[psc_ins_inspection_type_tl|PSC_INS_INSPECTION_TYPE_TL]] — 11 atributos (1 BICC)
- [[psc_ins_passing_rule_tl|PSC_INS_PASSING_RULE_TL]] — 11 atributos (1 BICC)
- [[psc_ins_rating_method_tl|PSC_INS_RATING_METHOD_TL]] — 11 atributos (1 BICC)

---

## ⚙️ Atributos

### [[psc_bnp_bill_type_tl|PSC_BNP_BILL_TYPE_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BillTypeTLPEOAgencyId | AGENCY_ID | — | — |
| 2 | BillTypeTLPEOBillType | BILL_TYPE | — | — |
| 3 | BillTypeTLPEOCreatedBy | CREATED_BY | — | — |
| 4 | BillTypeTLPEOCreationDate | CREATION_DATE | — | — |
| 5 | BillTypeTLPEODescription | DESCRIPTION | — | — |
| 6 | BillTypeTLPEOLanguage | LANGUAGE | — | — |
| 7 | BillTypeTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 8 | BillTypeTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | BillTypeTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | BillTypeTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | BillTypeTLPEOSourceLang | SOURCE_LANG | — | — |

### [[psc_ins_assessment_type_tl|PSC_INS_ASSESSMENT_TYPE_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssessmentTypeTLPEOAgencyId | AGENCY_ID | — | — |
| 2 | AssessmentTypeTLPEOAssessmentType | ASSESSMENT_TYPE | — | — |
| 3 | AssessmentTypeTLPEOCreatedBy | CREATED_BY | — | — |
| 4 | AssessmentTypeTLPEOCreationDate | CREATION_DATE | — | — |
| 5 | AssessmentTypeTLPEODescription | DESCRIPTION | — | ✅ |
| 6 | AssessmentTypeTLPEOLanguage | LANGUAGE | — | — |
| 7 | AssessmentTypeTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 8 | AssessmentTypeTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | AssessmentTypeTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | AssessmentTypeTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | AssessmentTypeTLPEOSourceLang | SOURCE_LANG | — | — |

### [[psc_ins_inspection_type_b|PSC_INS_INSPECTION_TYPE_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InspectionTypePEOAgencyId | AGENCY_ID | 🔑 | ✅ |
| 2 | InspectionTypePEOAssessmentType | ASSESSMENT_TYPE | — | ✅ |
| 3 | InspectionTypePEOAutonumberRuleId | AUTONUMBER_RULE_ID | — | — |
| 4 | InspectionTypePEOBillType | BILL_TYPE | — | — |
| 5 | InspectionTypePEOBillableFlag | BILLABLE_FLAG | — | — |
| 6 | InspectionTypePEOChecklistGroup | CHECKLIST_GROUP | — | — |
| 7 | InspectionTypePEOChecklistId | CHECKLIST_ID | — | — |
| 8 | InspectionTypePEOChgSchedulePolicyHrs | CHG_SCHEDULE_POLICY_HRS | — | — |
| 9 | InspectionTypePEOContractorSignatureOpt | CONTRACTOR_SIGNATURE_OPT | — | — |
| 10 | InspectionTypePEOCreatedBy | CREATED_BY | — | — |
| 11 | InspectionTypePEOCreationDate | CREATION_DATE | — | — |
| 12 | InspectionTypePEODistrictType | DISTRICT_TYPE | — | — |
| 13 | InspectionTypePEOEnabledFlag | ENABLED_FLAG | — | — |
| 14 | InspectionTypePEOEstimatedDurationHrs | ESTIMATED_DURATION_HRS | — | ✅ |
| 15 | InspectionTypePEOHideInspectorComment | HIDE_INSPECTOR_COMMENT | — | — |
| 16 | InspectionTypePEOInspectionType | INSPECTION_TYPE | 🔑 | ✅ |
| 17 | InspectionTypePEOInspectorSignatureOpt | INSPECTOR_SIGNATURE_OPT | — | — |
| 18 | InspectionTypePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 19 | InspectionTypePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 20 | InspectionTypePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 21 | InspectionTypePEOMaxScore | MAX_SCORE | — | — |
| 22 | InspectionTypePEOModuleId | MODULE_ID | — | — |
| 23 | InspectionTypePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 24 | InspectionTypePEOOpaPolicyName | OPA_POLICY_NAME | — | — |
| 25 | InspectionTypePEOOpaPolicyVersion | OPA_POLICY_VERSION | — | — |
| 26 | InspectionTypePEOOwnerSignatureOpt | OWNER_SIGNATURE_OPT | — | — |
| 27 | InspectionTypePEOPassingRule | PASSING_RULE | — | ✅ |
| 28 | InspectionTypePEORatingMethod | RATING_METHOD | — | ✅ |
| 29 | InspectionTypePEOSchedulingMethod | SCHEDULING_METHOD | — | ✅ |
| 30 | InspectionTypePEOScoringMethod | SCORING_METHOD | — | ✅ |

### [[psc_ins_inspection_type_tl|PSC_INS_INSPECTION_TYPE_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InspectionTypeTLPEOAgencyId | AGENCY_ID | — | — |
| 2 | InspectionTypeTLPEOCreatedBy | CREATED_BY | — | — |
| 3 | InspectionTypeTLPEOCreationDate | CREATION_DATE | — | — |
| 4 | InspectionTypeTLPEODescription | DESCRIPTION | — | ✅ |
| 5 | InspectionTypeTLPEOInspectionType | INSPECTION_TYPE | — | — |
| 6 | InspectionTypeTLPEOLanguage | LANGUAGE | — | — |
| 7 | InspectionTypeTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 8 | InspectionTypeTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | InspectionTypeTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | InspectionTypeTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | InspectionTypeTLPEOSourceLang | SOURCE_LANG | — | — |

### [[psc_ins_passing_rule_tl|PSC_INS_PASSING_RULE_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PassingRuleTLPEOAgencyId | AGENCY_ID | — | — |
| 2 | PassingRuleTLPEOCreatedBy | CREATED_BY | — | — |
| 3 | PassingRuleTLPEOCreationDate | CREATION_DATE | — | — |
| 4 | PassingRuleTLPEODescription | DESCRIPTION | — | ✅ |
| 5 | PassingRuleTLPEOLanguage | LANGUAGE | — | — |
| 6 | PassingRuleTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | PassingRuleTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | PassingRuleTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | PassingRuleTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | PassingRuleTLPEOPassingRule | PASSING_RULE | — | — |
| 11 | PassingRuleTLPEOSourceLang | SOURCE_LANG | — | — |

### [[psc_ins_rating_method_tl|PSC_INS_RATING_METHOD_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RatingMethodTLPEOAgencyId | AGENCY_ID | — | — |
| 2 | RatingMethodTLPEOCreatedBy | CREATED_BY | — | — |
| 3 | RatingMethodTLPEOCreationDate | CREATION_DATE | — | — |
| 4 | RatingMethodTLPEODescription | DESCRIPTION | — | ✅ |
| 5 | RatingMethodTLPEOLanguage | LANGUAGE | — | — |
| 6 | RatingMethodTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | RatingMethodTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | RatingMethodTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | RatingMethodTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | RatingMethodTLPEORatingMethod | RATING_METHOD | — | — |
| 11 | RatingMethodTLPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
