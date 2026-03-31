---
id: DOC-HCM-PVO-LearningPlanRecordsPVO
doc_type: system-doc
title: "LearningPlanRecordsPVO — PVO Human Capital Management"
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
  - LearningPlanRecordsPVO
  - learningplanrecordspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LearningPlanRecordsPVO

## 📌 Visão Geral

Extrai registros de planos de aprendizagem com status, custo e vigência. Suporta acompanhamento de progresso e orçamento de treinamentos.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.ContentAM.LearningPlanRecordsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 1 | 3 | 7 | 35% |

---

## 🔗 Tabelas Relacionadas

- [[wlf_plan_records_f|WLF_PLAN_RECORDS_F]] — 20 atributos (3 PKs, 7 BICC)

---

## ⚙️ Atributos

### [[wlf_plan_records_f|WLF_PLAN_RECORDS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PlanRecordsDEOArecEffectiveDate | AREC_EFFECTIVE_DATE | — | — |
| 2 | PlanRecordsDEOArecStateOnExecute | AREC_STATE_ON_EXECUTE | — | — |
| 3 | PlanRecordsDEOAssignmentRecordId | ASSIGNMENT_RECORD_ID | — | — |
| 4 | PlanRecordsDEOCreatedBy | CREATED_BY | — | — |
| 5 | PlanRecordsDEOCreationDate | CREATION_DATE | — | — |
| 6 | PlanRecordsDEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 7 | PlanRecordsDEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 8 | PlanRecordsDEOEnterpriseId | ENTERPRISE_ID | — | — |
| 9 | PlanRecordsDEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | PlanRecordsDEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | PlanRecordsDEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | PlanRecordsDEOLearningPlanId | LEARNING_PLAN_ID | — | — |
| 13 | PlanRecordsDEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | PlanRecordsDEOPlanProfileId | PLAN_PROFILE_ID | — | — |
| 15 | PlanRecordsDEOPlanRecordId | PLAN_RECORD_ID | 🔑 | ✅ |
| 16 | PlanRecordsDEOPricingRuleId | PRICING_RULE_ID | — | — |
| 17 | PlanRecordsDEOPricingRuleLockDate | PRICING_RULE_LOCK_DATE | — | — |
| 18 | PlanRecordsDEOStatus | STATUS | — | ✅ |
| 19 | PlanRecordsDEOWageCost | WAGE_COST | — | ✅ |
| 20 | PlanRecordsDEOWageCostCurrency | WAGE_COST_CURRENCY | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
