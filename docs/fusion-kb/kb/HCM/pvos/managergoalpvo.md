---
id: DOC-HCM-PVO-ManagerGoalPVO
doc_type: system-doc
title: "ManagerGoalPVO — PVO Human Capital Management"
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
  - ManagerGoalPVO
  - managergoalpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ManagerGoalPVO

## 📌 Visão Geral

Extrai metas de desempenho atribuídas a gestores, incluindo status de aprovação e grupo empresarial. Suporta o processo de gestão de objetivos e cascateamento de metas organizacionais.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmGoalCoreAM.ManagerGoalPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 90 | 1 | 1 | 12 | 13% |

---

## 🔗 Tabelas Relacionadas

- [[hrg_goals|HRG_GOALS]] — 90 atributos (1 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[hrg_goals|HRG_GOALS]]

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
| 66 | GoalAccessLevelCode | GOAL_ACCESS_LEVEL_CODE | — | — |
| 67 | GoalExtId | GOAL_EXT_ID | — | — |
| 68 | GoalId | GOAL_ID | 🔑 | ✅ |
| 69 | GoalPEOApprovalStatusCode | APPROVAL_STATUS_CODE | — | ✅ |
| 70 | GoalPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 71 | GoalPEOCreatedBy | CREATED_BY | — | ✅ |
| 72 | GoalPEOCreationDate | CREATION_DATE | — | ✅ |
| 73 | GoalPEOGoalApprovalState | GOAL_APPROVAL_STATE | — | — |
| 74 | GoalPEOGoalSourceCode | GOAL_SOURCE_CODE | — | ✅ |
| 75 | GoalPEOGoalVersionTypeCode | GOAL_VERSION_TYPE_CODE | — | ✅ |
| 76 | GoalPEOIncludeInPerfdocFlag | INCLUDE_IN_PERFDOC_FLAG | — | — |
| 77 | GoalPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 78 | GoalPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 79 | GoalPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 80 | GoalPEOLongDescription | LONG_DESCRIPTION | — | — |
| 81 | GoalPEOMassRequestId | MASS_REQUEST_ID | — | ✅ |
| 82 | GoalPEOReferenceContentItemId | REFERENCE_CONTENT_ITEM_ID | — | ✅ |
| 83 | GoalSubTypeCode | GOAL_SUB_TYPE_CODE | — | — |
| 84 | LastModifiedBy | LAST_MODIFIED_BY | — | — |
| 85 | LastModifiedDate | LAST_MODIFIED_DATE | — | — |
| 86 | MeasureCalcRuleCode | MEASURE_CALC_RULE_CODE | — | — |
| 87 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 88 | PublishDate | PUBLISH_DATE | — | — |
| 89 | PublishedFlag | PUBLISHED_FLAG | — | — |
| 90 | RequestContext | REQUEST_CONTEXT | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
