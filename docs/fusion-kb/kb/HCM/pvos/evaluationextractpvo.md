---
id: DOC-HCM-PVO-EvaluationExtractPVO
doc_type: system-doc
title: "EvaluationExtractPVO — PVO Human Capital Management"
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
  - EvaluationExtractPVO
  - evaluationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EvaluationExtractPVO

## 📌 Visão Geral

Extrai avaliações de desempenho completas, incluindo status, ações e datas. Fundamental para análise consolidada de ciclos de performance review.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.PerformanceBiccExtractAM.EvaluationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 103 | 1 | 1 | 103 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hra_evaluations|HRA_EVALUATIONS]] — 103 atributos (1 PKs, 103 BICC)

---

## ⚙️ Atributos

### [[hra_evaluations|HRA_EVALUATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionCode | ACTION_CODE | — | ✅ |
| 2 | ActionPerformedBy | ACTION_PERFORMED_BY | — | ✅ |
| 3 | ActionPerformedDate | ACTION_PERFORMED_DATE | — | ✅ |
| 4 | ActionReason | ACTION_REASON | — | ✅ |
| 5 | AssignmentId | ASSIGNMENT_ID | — | ✅ |
| 6 | Attribute1 | ATTRIBUTE1 | — | ✅ |
| 7 | Attribute10 | ATTRIBUTE10 | — | ✅ |
| 8 | Attribute11 | ATTRIBUTE11 | — | ✅ |
| 9 | Attribute12 | ATTRIBUTE12 | — | ✅ |
| 10 | Attribute13 | ATTRIBUTE13 | — | ✅ |
| 11 | Attribute14 | ATTRIBUTE14 | — | ✅ |
| 12 | Attribute15 | ATTRIBUTE15 | — | ✅ |
| 13 | Attribute16 | ATTRIBUTE16 | — | ✅ |
| 14 | Attribute17 | ATTRIBUTE17 | — | ✅ |
| 15 | Attribute18 | ATTRIBUTE18 | — | ✅ |
| 16 | Attribute19 | ATTRIBUTE19 | — | ✅ |
| 17 | Attribute2 | ATTRIBUTE2 | — | ✅ |
| 18 | Attribute20 | ATTRIBUTE20 | — | ✅ |
| 19 | Attribute21 | ATTRIBUTE21 | — | ✅ |
| 20 | Attribute22 | ATTRIBUTE22 | — | ✅ |
| 21 | Attribute23 | ATTRIBUTE23 | — | ✅ |
| 22 | Attribute24 | ATTRIBUTE24 | — | ✅ |
| 23 | Attribute25 | ATTRIBUTE25 | — | ✅ |
| 24 | Attribute26 | ATTRIBUTE26 | — | ✅ |
| 25 | Attribute27 | ATTRIBUTE27 | — | ✅ |
| 26 | Attribute28 | ATTRIBUTE28 | — | ✅ |
| 27 | Attribute29 | ATTRIBUTE29 | — | ✅ |
| 28 | Attribute3 | ATTRIBUTE3 | — | ✅ |
| 29 | Attribute30 | ATTRIBUTE30 | — | ✅ |
| 30 | Attribute4 | ATTRIBUTE4 | — | ✅ |
| 31 | Attribute5 | ATTRIBUTE5 | — | ✅ |
| 32 | Attribute6 | ATTRIBUTE6 | — | ✅ |
| 33 | Attribute7 | ATTRIBUTE7 | — | ✅ |
| 34 | Attribute8 | ATTRIBUTE8 | — | ✅ |
| 35 | Attribute9 | ATTRIBUTE9 | — | ✅ |
| 36 | AttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 37 | AttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 38 | AttributeDate10 | ATTRIBUTE_DATE10 | — | ✅ |
| 39 | AttributeDate11 | ATTRIBUTE_DATE11 | — | ✅ |
| 40 | AttributeDate12 | ATTRIBUTE_DATE12 | — | ✅ |
| 41 | AttributeDate13 | ATTRIBUTE_DATE13 | — | ✅ |
| 42 | AttributeDate14 | ATTRIBUTE_DATE14 | — | ✅ |
| 43 | AttributeDate15 | ATTRIBUTE_DATE15 | — | ✅ |
| 44 | AttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 45 | AttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 46 | AttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 47 | AttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 48 | AttributeDate6 | ATTRIBUTE_DATE6 | — | ✅ |
| 49 | AttributeDate7 | ATTRIBUTE_DATE7 | — | ✅ |
| 50 | AttributeDate8 | ATTRIBUTE_DATE8 | — | ✅ |
| 51 | AttributeDate9 | ATTRIBUTE_DATE9 | — | ✅ |
| 52 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 53 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 54 | AttributeNumber11 | ATTRIBUTE_NUMBER11 | — | ✅ |
| 55 | AttributeNumber12 | ATTRIBUTE_NUMBER12 | — | ✅ |
| 56 | AttributeNumber13 | ATTRIBUTE_NUMBER13 | — | ✅ |
| 57 | AttributeNumber14 | ATTRIBUTE_NUMBER14 | — | ✅ |
| 58 | AttributeNumber15 | ATTRIBUTE_NUMBER15 | — | ✅ |
| 59 | AttributeNumber16 | ATTRIBUTE_NUMBER16 | — | ✅ |
| 60 | AttributeNumber17 | ATTRIBUTE_NUMBER17 | — | ✅ |
| 61 | AttributeNumber18 | ATTRIBUTE_NUMBER18 | — | ✅ |
| 62 | AttributeNumber19 | ATTRIBUTE_NUMBER19 | — | ✅ |
| 63 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 64 | AttributeNumber20 | ATTRIBUTE_NUMBER20 | — | ✅ |
| 65 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 66 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 67 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 68 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 69 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 70 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 71 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 72 | BusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 73 | CalculationRatingsFlag | CALCULATION_RATINGS_FLAG | — | ✅ |
| 74 | CreatedBy | CREATED_BY | — | ✅ |
| 75 | CreationDate | CREATION_DATE | — | ✅ |
| 76 | DecimalPlaces | DECIMAL_PLACES | — | ✅ |
| 77 | EndDate | END_DATE | — | ✅ |
| 78 | EvaluationDate | EVALUATION_DATE | — | ✅ |
| 79 | EvaluationId | EVALUATION_ID | 🔑 | ✅ |
| 80 | LanguageCode | LANGUAGE_CODE | — | ✅ |
| 81 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 82 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 83 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 84 | LockedByUserId | LOCKED_BY_USER_ID | — | ✅ |
| 85 | ManagerAssignmentId | MANAGER_ASSIGNMENT_ID | — | ✅ |
| 86 | ManagerComments | MANAGER_COMMENTS | — | ✅ |
| 87 | ManagerId | MANAGER_ID | — | ✅ |
| 88 | MappingMethodCode | MAPPING_METHOD_CODE | — | ✅ |
| 89 | MeetingHeldDate | MEETING_HELD_DATE | — | ✅ |
| 90 | Name | NAME | — | ✅ |
| 91 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 92 | PrevStatusCode | PREV_STATUS_CODE | — | ✅ |
| 93 | ReviewPeriodId | REVIEW_PERIOD_ID | — | ✅ |
| 94 | RoundingRuleCode | ROUNDING_RULE_CODE | — | ✅ |
| 95 | SelectManagerAllowedFlag | SELECT_MANAGER_ALLOWED_FLAG | — | ✅ |
| 96 | StarRatingEnabledFlag | STAR_RATING_ENABLED_FLAG | — | ✅ |
| 97 | StartDate | START_DATE | — | ✅ |
| 98 | StatusCode | STATUS_CODE | — | ✅ |
| 99 | TemplateDefnId | TEMPLATE_DEFN_ID | — | ✅ |
| 100 | TemplateTypeCode | TEMPLATE_TYPE_CODE | — | ✅ |
| 101 | TmplPeriodId | TMPL_PERIOD_ID | — | ✅ |
| 102 | WorkerComments | WORKER_COMMENTS | — | ✅ |
| 103 | WorkerId | WORKER_ID | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
