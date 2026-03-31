---
id: DOC-HCM-PVO-PlanCandidatesPVO
doc_type: system-doc
title: "PlanCandidatesPVO — PVO Human Capital Management"
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
  - PlanCandidatesPVO
  - plancandidatespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PlanCandidatesPVO

## 📌 Visão Geral

Extrai os candidatos a planos de sucessão, incluindo ranking e dados de avaliação. Fundamental para gestão de pipeline de talentos e planejamento sucessório de posições-chave.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmSuccessionPlansAM.PlanCandidatesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 87 | 2 | 2 | 17 | 20% |

---

## 🔗 Tabelas Relacionadas

- [[hrm_plan_candidates|HRM_PLAN_CANDIDATES]] — 1 atributos
- [[hrm_plan_candidates_v|HRM_PLAN_CANDIDATES_V]] — 86 atributos (2 PKs, 17 BICC)

---

## ⚙️ Atributos

### [[hrm_plan_candidates|HRM_PLAN_CANDIDATES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CandidateSince | CANDIDATE_SINCE | — | — |

### [[hrm_plan_candidates_v|HRM_PLAN_CANDIDATES_V]]

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
| 31 | AttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 32 | AttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 33 | AttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 34 | AttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 35 | AttributeDate13 | ATTRIBUTE_DATE13 | — | — |
| 36 | AttributeDate14 | ATTRIBUTE_DATE14 | — | — |
| 37 | AttributeDate15 | ATTRIBUTE_DATE15 | — | — |
| 38 | AttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 39 | AttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 40 | AttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 41 | AttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 42 | AttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 43 | AttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 44 | AttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 45 | AttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 46 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 47 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 48 | AttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 49 | AttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 50 | AttributeNumber13 | ATTRIBUTE_NUMBER13 | — | — |
| 51 | AttributeNumber14 | ATTRIBUTE_NUMBER14 | — | — |
| 52 | AttributeNumber15 | ATTRIBUTE_NUMBER15 | — | — |
| 53 | AttributeNumber16 | ATTRIBUTE_NUMBER16 | — | — |
| 54 | AttributeNumber17 | ATTRIBUTE_NUMBER17 | — | — |
| 55 | AttributeNumber18 | ATTRIBUTE_NUMBER18 | — | — |
| 56 | AttributeNumber19 | ATTRIBUTE_NUMBER19 | — | — |
| 57 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 58 | AttributeNumber20 | ATTRIBUTE_NUMBER20 | — | — |
| 59 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 60 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 61 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 62 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 63 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 64 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 65 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 66 | CandidateRanking | CANDIDATE_RANKING | — | ✅ |
| 67 | CreatedBy | CREATED_BY | — | ✅ |
| 68 | CreationDate | CREATION_DATE | — | ✅ |
| 69 | EmergencySuccessor | EMERGENCY_SUCCESSOR | — | ✅ |
| 70 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 71 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 72 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 73 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 74 | PlanCandPEODateFrom | DATE_FROM | — | — |
| 75 | PlanCandPEOLatestRecordFlag | LATEST_RECORD_FLAG | — | — |
| 76 | PlanCandPEOShowSuccStatusFlag | SHOW_SUCCESSION_STATUS_FLAG | — | — |
| 77 | PlanCandPEOSuccessionStatus | SUCCESSION_STATUS | — | ✅ |
| 78 | PlanCandidatesPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 79 | PlanCandidatesPEOCandidateType | CANDIDATE_TYPE | — | ✅ |
| 80 | PlanCandidatesPEOEnterpriseId | ENTERPRISE_ID | 🔑 | ✅ |
| 81 | PlanCandidatesPEOExteCandidateId | EXTERNAL_CANDIDATE_ID | — | — |
| 82 | PlanCandidatesPEOPersonId | PERSON_ID | — | ✅ |
| 83 | PlanCandidatesPEOPlanCandidateId | PLAN_CANDIDATE_ID | 🔑 | ✅ |
| 84 | PlanCandidatesPEOPlanId | PLAN_ID | — | ✅ |
| 85 | PlanCandidatesPEOReadinessCode | READINESS_CODE | — | ✅ |
| 86 | PlanCandidatesPEOStatus | STATUS | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
