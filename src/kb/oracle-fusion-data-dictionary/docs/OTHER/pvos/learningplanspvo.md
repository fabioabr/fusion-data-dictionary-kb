---
id: DOC-OTHER-PVO-LearningPlansPVO
doc_type: system-doc
title: "LearningPlansPVO — PVO Cross-Module"
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
  - LearningPlansPVO
  - learningplanspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LearningPlansPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Learning Plans. Acessa as tabelas: WLF_LEARNING_PLANS_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.ContentAM.LearningPlansPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 81 | 1 | 3 | 7 | 9% |

---

## 🔗 Tabelas Relacionadas

- [[wlf_learning_plans_f|WLF_LEARNING_PLANS_F]] — 81 atributos (3 PKs, 7 BICC)

---

## ⚙️ Atributos

### [[wlf_learning_plans_f|WLF_LEARNING_PLANS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LearningPlanDEOCreatedBy | CREATED_BY | — | — |
| 2 | LearningPlanDEOCreationDate | CREATION_DATE | — | — |
| 3 | LearningPlanDEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 4 | LearningPlanDEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 5 | LearningPlanDEOEnterpriseId | ENTERPRISE_ID | — | — |
| 6 | LearningPlanDEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LearningPlanDEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | LearningPlanDEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | LearningPlanDEOLearningItemId | LEARNING_ITEM_ID | — | — |
| 10 | LearningPlanDEOLearningPlanId | LEARNING_PLAN_ID | 🔑 | ✅ |
| 11 | LearningPlanDEOMonetaryBudget | MONETARY_BUDGET | — | ✅ |
| 12 | LearningPlanDEOMonetaryCurrencyCode | MONETARY_CURRENCY_CODE | — | ✅ |
| 13 | LearningPlanDEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | LearningPlanDEOPlnAttribute1 | PLN_ATTRIBUTE1 | — | — |
| 15 | LearningPlanDEOPlnAttribute10 | PLN_ATTRIBUTE10 | — | — |
| 16 | LearningPlanDEOPlnAttribute11 | PLN_ATTRIBUTE11 | — | — |
| 17 | LearningPlanDEOPlnAttribute12 | PLN_ATTRIBUTE12 | — | — |
| 18 | LearningPlanDEOPlnAttribute13 | PLN_ATTRIBUTE13 | — | — |
| 19 | LearningPlanDEOPlnAttribute14 | PLN_ATTRIBUTE14 | — | — |
| 20 | LearningPlanDEOPlnAttribute15 | PLN_ATTRIBUTE15 | — | — |
| 21 | LearningPlanDEOPlnAttribute16 | PLN_ATTRIBUTE16 | — | — |
| 22 | LearningPlanDEOPlnAttribute17 | PLN_ATTRIBUTE17 | — | — |
| 23 | LearningPlanDEOPlnAttribute18 | PLN_ATTRIBUTE18 | — | — |
| 24 | LearningPlanDEOPlnAttribute19 | PLN_ATTRIBUTE19 | — | — |
| 25 | LearningPlanDEOPlnAttribute2 | PLN_ATTRIBUTE2 | — | — |
| 26 | LearningPlanDEOPlnAttribute20 | PLN_ATTRIBUTE20 | — | — |
| 27 | LearningPlanDEOPlnAttribute21 | PLN_ATTRIBUTE21 | — | — |
| 28 | LearningPlanDEOPlnAttribute22 | PLN_ATTRIBUTE22 | — | — |
| 29 | LearningPlanDEOPlnAttribute23 | PLN_ATTRIBUTE23 | — | — |
| 30 | LearningPlanDEOPlnAttribute24 | PLN_ATTRIBUTE24 | — | — |
| 31 | LearningPlanDEOPlnAttribute25 | PLN_ATTRIBUTE25 | — | — |
| 32 | LearningPlanDEOPlnAttribute26 | PLN_ATTRIBUTE26 | — | — |
| 33 | LearningPlanDEOPlnAttribute27 | PLN_ATTRIBUTE27 | — | — |
| 34 | LearningPlanDEOPlnAttribute28 | PLN_ATTRIBUTE28 | — | — |
| 35 | LearningPlanDEOPlnAttribute29 | PLN_ATTRIBUTE29 | — | — |
| 36 | LearningPlanDEOPlnAttribute3 | PLN_ATTRIBUTE3 | — | — |
| 37 | LearningPlanDEOPlnAttribute30 | PLN_ATTRIBUTE30 | — | — |
| 38 | LearningPlanDEOPlnAttribute4 | PLN_ATTRIBUTE4 | — | — |
| 39 | LearningPlanDEOPlnAttribute5 | PLN_ATTRIBUTE5 | — | — |
| 40 | LearningPlanDEOPlnAttribute6 | PLN_ATTRIBUTE6 | — | — |
| 41 | LearningPlanDEOPlnAttribute7 | PLN_ATTRIBUTE7 | — | — |
| 42 | LearningPlanDEOPlnAttribute8 | PLN_ATTRIBUTE8 | — | — |
| 43 | LearningPlanDEOPlnAttribute9 | PLN_ATTRIBUTE9 | — | — |
| 44 | LearningPlanDEOPlnAttributeCategory | PLN_ATTRIBUTE_CATEGORY | — | — |
| 45 | LearningPlanDEOPlnAttributeDate1 | PLN_ATTRIBUTE_DATE1 | — | — |
| 46 | LearningPlanDEOPlnAttributeDate10 | PLN_ATTRIBUTE_DATE10 | — | — |
| 47 | LearningPlanDEOPlnAttributeDate11 | PLN_ATTRIBUTE_DATE11 | — | — |
| 48 | LearningPlanDEOPlnAttributeDate12 | PLN_ATTRIBUTE_DATE12 | — | — |
| 49 | LearningPlanDEOPlnAttributeDate13 | PLN_ATTRIBUTE_DATE13 | — | — |
| 50 | LearningPlanDEOPlnAttributeDate14 | PLN_ATTRIBUTE_DATE14 | — | — |
| 51 | LearningPlanDEOPlnAttributeDate15 | PLN_ATTRIBUTE_DATE15 | — | — |
| 52 | LearningPlanDEOPlnAttributeDate2 | PLN_ATTRIBUTE_DATE2 | — | — |
| 53 | LearningPlanDEOPlnAttributeDate3 | PLN_ATTRIBUTE_DATE3 | — | — |
| 54 | LearningPlanDEOPlnAttributeDate4 | PLN_ATTRIBUTE_DATE4 | — | — |
| 55 | LearningPlanDEOPlnAttributeDate5 | PLN_ATTRIBUTE_DATE5 | — | — |
| 56 | LearningPlanDEOPlnAttributeDate6 | PLN_ATTRIBUTE_DATE6 | — | — |
| 57 | LearningPlanDEOPlnAttributeDate7 | PLN_ATTRIBUTE_DATE7 | — | — |
| 58 | LearningPlanDEOPlnAttributeDate8 | PLN_ATTRIBUTE_DATE8 | — | — |
| 59 | LearningPlanDEOPlnAttributeDate9 | PLN_ATTRIBUTE_DATE9 | — | — |
| 60 | LearningPlanDEOPlnAttributeNumber1 | PLN_ATTRIBUTE_NUMBER1 | — | — |
| 61 | LearningPlanDEOPlnAttributeNumber10 | PLN_ATTRIBUTE_NUMBER10 | — | — |
| 62 | LearningPlanDEOPlnAttributeNumber11 | PLN_ATTRIBUTE_NUMBER11 | — | — |
| 63 | LearningPlanDEOPlnAttributeNumber12 | PLN_ATTRIBUTE_NUMBER12 | — | — |
| 64 | LearningPlanDEOPlnAttributeNumber13 | PLN_ATTRIBUTE_NUMBER13 | — | — |
| 65 | LearningPlanDEOPlnAttributeNumber14 | PLN_ATTRIBUTE_NUMBER14 | — | — |
| 66 | LearningPlanDEOPlnAttributeNumber15 | PLN_ATTRIBUTE_NUMBER15 | — | — |
| 67 | LearningPlanDEOPlnAttributeNumber16 | PLN_ATTRIBUTE_NUMBER16 | — | — |
| 68 | LearningPlanDEOPlnAttributeNumber17 | PLN_ATTRIBUTE_NUMBER17 | — | — |
| 69 | LearningPlanDEOPlnAttributeNumber18 | PLN_ATTRIBUTE_NUMBER18 | — | — |
| 70 | LearningPlanDEOPlnAttributeNumber19 | PLN_ATTRIBUTE_NUMBER19 | — | — |
| 71 | LearningPlanDEOPlnAttributeNumber2 | PLN_ATTRIBUTE_NUMBER2 | — | — |
| 72 | LearningPlanDEOPlnAttributeNumber20 | PLN_ATTRIBUTE_NUMBER20 | — | — |
| 73 | LearningPlanDEOPlnAttributeNumber3 | PLN_ATTRIBUTE_NUMBER3 | — | — |
| 74 | LearningPlanDEOPlnAttributeNumber4 | PLN_ATTRIBUTE_NUMBER4 | — | — |
| 75 | LearningPlanDEOPlnAttributeNumber5 | PLN_ATTRIBUTE_NUMBER5 | — | — |
| 76 | LearningPlanDEOPlnAttributeNumber6 | PLN_ATTRIBUTE_NUMBER6 | — | — |
| 77 | LearningPlanDEOPlnAttributeNumber7 | PLN_ATTRIBUTE_NUMBER7 | — | — |
| 78 | LearningPlanDEOPlnAttributeNumber8 | PLN_ATTRIBUTE_NUMBER8 | — | — |
| 79 | LearningPlanDEOPlnAttributeNumber9 | PLN_ATTRIBUTE_NUMBER9 | — | — |
| 80 | LearningPlanDEOTimeBudget | TIME_BUDGET | — | ✅ |
| 81 | LearningPlanDEOWageRateFf | WAGE_RATE_FF | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
