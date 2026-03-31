---
id: DOC-HCM-PVO-PlanPVO
doc_type: system-doc
title: "PlanPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - PlanPVO
  - planpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PlanPVO

## 📌 Visão Geral

Extrai os planos de sucessão organizacional, com status, tipo e configurações detalhadas. Central para gestão de talent pipeline e continuidade de posições estratégicas.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmSuccessionPlansAM.PlanPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 103 | 2 | 2 | 33 | 32% |

---

## 🔗 Tabelas Relacionadas

- [[hcm_lookups|HCM_LOOKUPS]] — 9 atributos (9 BICC)
- [[hrm_plans_v|HRM_PLANS_V]] — 94 atributos (2 PKs, 24 BICC)

---

## ⚙️ Atributos

### [[hcm_lookups|HCM_LOOKUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LookUpPEOForAccessCodeLookupCode | LOOKUP_CODE | — | ✅ |
| 2 | LookUpPEOForAccessCodeLookupType | LOOKUP_TYPE | — | ✅ |
| 3 | LookUpPEOForPlanTypeLookupCode | LOOKUP_CODE | — | ✅ |
| 4 | LookUpPEOForPlanTypeLookupType | LOOKUP_TYPE | — | ✅ |
| 5 | LookupPEOForPlanStatusLookupCode | LOOKUP_CODE | — | ✅ |
| 6 | LookupPEOForPlanStatusLookupType | LOOKUP_TYPE | — | ✅ |
| 7 | PlanPEOAccessTypeCode | MEANING | — | ✅ |
| 8 | PlanPEOPlanType | MEANING | — | ✅ |
| 9 | PlanPEOStatus | MEANING | — | ✅ |

### [[hrm_plans_v|HRM_PLANS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Attribute1 | ATTRIBUTE1 | — | — |
| 2 | Attribute10 | ATTRIBUTE10 | — | — |
| 3 | Attribute11 | ATTRIBUTE11 | — | — |
| 4 | Attribute12 | ATTRIBUTE12 | — | — |
| 5 | Attribute13 | ATTRIBUTE13 | — | — |
| 6 | Attribute14 | ATTRIBUTE14 | — | — |
| 7 | Attribute15 | ATTRIBUTE15 | — | — |
| 8 | Attribute16 | ATTRIBUTE16 | — | — |
| 9 | Attribute17 | ATTRIBUTE17 | — | — |
| 10 | Attribute18 | ATTRIBUTE18 | — | — |
| 11 | Attribute19 | ATTRIBUTE19 | — | — |
| 12 | Attribute2 | ATTRIBUTE2 | — | — |
| 13 | Attribute20 | ATTRIBUTE20 | — | — |
| 14 | Attribute21 | ATTRIBUTE21 | — | — |
| 15 | Attribute22 | ATTRIBUTE22 | — | — |
| 16 | Attribute23 | ATTRIBUTE23 | — | — |
| 17 | Attribute24 | ATTRIBUTE24 | — | — |
| 18 | Attribute25 | ATTRIBUTE25 | — | — |
| 19 | Attribute26 | ATTRIBUTE26 | — | — |
| 20 | Attribute27 | ATTRIBUTE27 | — | — |
| 21 | Attribute28 | ATTRIBUTE28 | — | — |
| 22 | Attribute29 | ATTRIBUTE29 | — | — |
| 23 | Attribute3 | ATTRIBUTE3 | — | — |
| 24 | Attribute30 | ATTRIBUTE30 | — | — |
| 25 | Attribute4 | ATTRIBUTE4 | — | — |
| 26 | Attribute5 | ATTRIBUTE5 | — | — |
| 27 | Attribute6 | ATTRIBUTE6 | — | — |
| 28 | Attribute7 | ATTRIBUTE7 | — | — |
| 29 | Attribute8 | ATTRIBUTE8 | — | — |
| 30 | Attribute9 | ATTRIBUTE9 | — | — |
| 31 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 32 | AttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 33 | AttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 34 | AttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 35 | AttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 36 | AttributeDate13 | ATTRIBUTE_DATE13 | — | — |
| 37 | AttributeDate14 | ATTRIBUTE_DATE14 | — | — |
| 38 | AttributeDate15 | ATTRIBUTE_DATE15 | — | — |
| 39 | AttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 40 | AttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 41 | AttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 42 | AttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 43 | AttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 44 | AttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 45 | AttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 46 | AttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 47 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 48 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 49 | AttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 50 | AttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 51 | AttributeNumber13 | ATTRIBUTE_NUMBER13 | — | — |
| 52 | AttributeNumber14 | ATTRIBUTE_NUMBER14 | — | — |
| 53 | AttributeNumber15 | ATTRIBUTE_NUMBER15 | — | — |
| 54 | AttributeNumber16 | ATTRIBUTE_NUMBER16 | — | — |
| 55 | AttributeNumber17 | ATTRIBUTE_NUMBER17 | — | — |
| 56 | AttributeNumber18 | ATTRIBUTE_NUMBER18 | — | — |
| 57 | AttributeNumber19 | ATTRIBUTE_NUMBER19 | — | — |
| 58 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 59 | AttributeNumber20 | ATTRIBUTE_NUMBER20 | — | — |
| 60 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 61 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 62 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 63 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 64 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 65 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 66 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 67 | CreatedBy | CREATED_BY | — | ✅ |
| 68 | CreationDate | CREATION_DATE | — | ✅ |
| 69 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 70 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 71 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 72 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 73 | PlanPEOAccessTypeCodeLookupCd | ACCESS_TYPE_CODE | — | ✅ |
| 74 | PlanPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 75 | PlanPEOBusinessUnitId | BUSINESS_UNIT_ID | — | ✅ |
| 76 | PlanPEODateFrom | DATE_FROM | — | — |
| 77 | PlanPEODepartmentId | DEPARTMENT_ID | — | ✅ |
| 78 | PlanPEODescription | DESCRIPTION | — | ✅ |
| 79 | PlanPEOEnableAlerts | ENABLE_ALERTS | — | — |
| 80 | PlanPEOEnterpriseId | ENTERPRISE_ID | 🔑 | ✅ |
| 81 | PlanPEOGradeId | GRADE_ID | — | ✅ |
| 82 | PlanPEOIncumbentPersonId | INCUMBENT_PERSON_ID | — | ✅ |
| 83 | PlanPEOIncumbentRoleChangeFlag | INCUMBENT_ROLE_CHANGE_FLAG | — | — |
| 84 | PlanPEOJobFamilyId | JOB_FAMILY_ID | — | ✅ |
| 85 | PlanPEOJobId | JOB_ID | — | ✅ |
| 86 | PlanPEOJobProfileId | JOB_PROFILE_ID | — | ✅ |
| 87 | PlanPEOLatestRecordFlag | LATEST_RECORD_FLAG | — | — |
| 88 | PlanPEOOwnerEditOnly | OWNER_EDIT_ONLY | — | ✅ |
| 89 | PlanPEOPlanId | PLAN_ID | 🔑 | ✅ |
| 90 | PlanPEOPlanName | PLAN_NAME | — | ✅ |
| 91 | PlanPEOPlanTypeCode | PLAN_TYPE | — | ✅ |
| 92 | PlanPEOPositionId | POSITION_ID | — | ✅ |
| 93 | PlanPEOStatusLookUpCode | STATUS | — | ✅ |
| 94 | PlanPEOStatusReason | STATUS_REASON | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
