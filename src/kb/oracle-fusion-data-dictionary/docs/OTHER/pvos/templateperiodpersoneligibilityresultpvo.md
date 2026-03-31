---
id: DOC-OTHER-PVO-TemplatePeriodPersonEligibilityResultPVO
doc_type: system-doc
title: "TemplatePeriodPersonEligibilityResultPVO — PVO Cross-Module"
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
  - TemplatePeriodPersonEligibilityResultPVO
  - templateperiodpersoneligibilityresultpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TemplatePeriodPersonEligibilityResultPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Template Period Person Eligibility Result. Acessa as tabelas: BEN_ELIG_OBJ_F, BEN_ELIG_RSLT_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmBenefitsAM.TemplatePeriodPersonEligibilityResultPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 33 | 2 | 4 | 6 | 18% |

---

## 🔗 Tabelas Relacionadas

- [[ben_elig_obj_f|BEN_ELIG_OBJ_F]] — 14 atributos (1 BICC)
- [[ben_elig_rslt_f|BEN_ELIG_RSLT_F]] — 19 atributos (4 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[ben_elig_obj_f|BEN_ELIG_OBJ_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ColumnName | COLUMN_NAME | — | — |
| 2 | ColumnValue | COLUMN_VALUE | — | — |
| 3 | EffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 4 | EffectiveStartDate1 | EFFECTIVE_START_DATE | — | ✅ |
| 5 | EligObjId1 | ELIG_OBJ_ID | — | — |
| 6 | EligObjId2 | ELIG_OBJ_ID | — | — |
| 7 | EligObjType | ELIG_OBJ_TYPE | — | — |
| 8 | EligibilityObjectPEOCreatedBy | CREATED_BY | — | — |
| 9 | EligibilityObjectPEOCreationDate | CREATION_DATE | — | — |
| 10 | EligibilityObjectPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 11 | EligibilityObjectPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | EligibilityObjectPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | EligibilityObjectPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | TableName | TABLE_NAME | — | — |

### [[ben_elig_rslt_f|BEN_ELIG_RSLT_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentId | ASSIGNMENT_ID | — | — |
| 2 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 3 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 4 | EligFlag | ELIG_FLAG | — | ✅ |
| 5 | EligObjId | ELIG_OBJ_ID | — | — |
| 6 | EligRsltId | ELIG_RSLT_ID | 🔑 | ✅ |
| 7 | EligRsltId1 | ELIG_RSLT_ID | 🔑 | ✅ |
| 8 | EligibilityResultPEOCreatedBy | CREATED_BY | — | — |
| 9 | EligibilityResultPEOCreationDate | CREATION_DATE | — | — |
| 10 | EligibilityResultPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 11 | EligibilityResultPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | EligibilityResultPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | EligibilityResultPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | InelgRsnCd | INELG_RSN_CD | — | — |
| 15 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 16 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 17 | OverrideFlag | OVERRIDE_FLAG | — | — |
| 18 | OverrideThruDate | OVERRIDE_THRU_DATE | — | — |
| 19 | PersonId | PERSON_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
