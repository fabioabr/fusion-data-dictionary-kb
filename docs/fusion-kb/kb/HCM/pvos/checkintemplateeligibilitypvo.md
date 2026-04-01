---
id: DOC-HCM-PVO-CheckinTemplateEligibilityPVO
doc_type: system-doc
title: "CheckinTemplateEligibilityPVO — PVO Human Capital Management"
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
  - CheckinTemplateEligibilityPVO
  - checkintemplateeligibilitypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CheckinTemplateEligibilityPVO

## 📌 Visão Geral

Avalia elegibilidade de templates de check-in por colaborador com base em perfis. Controla quais templates de 1:1 sao aplicaveis a cada pessoa.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmPerformanceSetupAM.CheckinTemplateEligibilityPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 31 | 3 | 3 | 15 | 48% |

---

## 🔗 Tabelas Relacionadas

- [[ben_elig_obj_f|BEN_ELIG_OBJ_F]] — 7 atributos (1 BICC)
- [[ben_elig_rslt_f|BEN_ELIG_RSLT_F]] — 20 atributos (3 PKs, 14 BICC)
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 4 atributos

---

## ⚙️ Atributos

### [[ben_elig_obj_f|BEN_ELIG_OBJ_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EligibilityObjectPEOColumnName | COLUMN_NAME | — | — |
| 2 | EligibilityObjectPEOColumnValue | COLUMN_VALUE | — | — |
| 3 | EligibilityObjectPEOEffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 4 | EligibilityObjectPEOEffectiveStartDate1 | EFFECTIVE_START_DATE | — | ✅ |
| 5 | EligibilityObjectPEOEligObjId1 | ELIG_OBJ_ID | — | — |
| 6 | EligibilityObjectPEOEligObjType | ELIG_OBJ_TYPE | — | — |
| 7 | EligibilityObjectPEOTableName | TABLE_NAME | — | — |

### [[ben_elig_rslt_f|BEN_ELIG_RSLT_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EligibilityResultPEOAssignmentId | ASSIGNMENT_ID | — | ✅ |
| 2 | EligibilityResultPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 3 | EligibilityResultPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | EligibilityResultPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | EligibilityResultPEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 6 | EligibilityResultPEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 7 | EligibilityResultPEOEligFlag | ELIG_FLAG | — | ✅ |
| 8 | EligibilityResultPEOEligObjId | ELIG_OBJ_ID | — | — |
| 9 | EligibilityResultPEOEligRsltId | ELIG_RSLT_ID | 🔑 | ✅ |
| 10 | EligibilityResultPEOInelgRsnCd | INELG_RSN_CD | — | ✅ |
| 11 | EligibilityResultPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 12 | EligibilityResultPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 13 | EligibilityResultPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | EligibilityResultPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | EligibilityResultPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | EligibilityResultPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | EligibilityResultPEOOverrideFlag | OVERRIDE_FLAG | — | ✅ |
| 18 | EligibilityResultPEOOverrideThruDate | OVERRIDE_THRU_DATE | — | ✅ |
| 19 | EligibilityResultPEOPersonId | PERSON_ID | — | ✅ |
| 20 | EligibilityResultPEORequestId | REQUEST_ID | — | — |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | PersonId | PERSON_ID | — | — |
| 4 | PersonNumber | PERSON_NUMBER | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
