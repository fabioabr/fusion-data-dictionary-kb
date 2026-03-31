---
id: DOC-OTHER-PVO-EligibilityResultsExtractPVO
doc_type: system-doc
title: "EligibilityResultsExtractPVO — PVO Cross-Module"
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
  - EligibilityResultsExtractPVO
  - eligibilityresultsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EligibilityResultsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Eligibility Results Extract. Acessa as tabelas: BEN_ELIG_RSLT_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.BenefitsBiccExtractAM.EligibilityResultsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 1 | 3 | 21 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ben_elig_rslt_f|BEN_ELIG_RSLT_F]] — 21 atributos (3 PKs, 21 BICC)

---

## ⚙️ Atributos

### [[ben_elig_rslt_f|BEN_ELIG_RSLT_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentId | ASSIGNMENT_ID | — | ✅ |
| 2 | BusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 6 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 7 | EligFlag | ELIG_FLAG | — | ✅ |
| 8 | EligObjId | ELIG_OBJ_ID | — | ✅ |
| 9 | EligObjType | ELIG_OBJ_TYPE | — | ✅ |
| 10 | EligRsltId | ELIG_RSLT_ID | 🔑 | ✅ |
| 11 | InelgRsnCd | INELG_RSN_CD | — | ✅ |
| 12 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 13 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 14 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 16 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 17 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 18 | OverrideFlag | OVERRIDE_FLAG | — | ✅ |
| 19 | OverrideThruDate | OVERRIDE_THRU_DATE | — | ✅ |
| 20 | PersonId | PERSON_ID | — | ✅ |
| 21 | RequestId | REQUEST_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
