---
id: DOC-HCM-PVO-LearningPlanProfilesPVO
doc_type: system-doc
title: "LearningPlanProfilesPVO — PVO Human Capital Management"
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
  - LearningPlanProfilesPVO
  - learningplanprofilespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LearningPlanProfilesPVO

## 📌 Visão Geral

Extrai perfis vinculados a planos de aprendizagem com tipo e vigência. Suporta segmentação de treinamentos por perfil de público.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.ContentAM.LearningPlanProfilesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 3 | 5 | 33% |

---

## 🔗 Tabelas Relacionadas

- [[wlf_plan_profiles_f|WLF_PLAN_PROFILES_F]] — 15 atributos (3 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[wlf_plan_profiles_f|WLF_PLAN_PROFILES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PlanProfileDEOCreatedBy | CREATED_BY | — | — |
| 2 | PlanProfileDEOCreationDate | CREATION_DATE | — | — |
| 3 | PlanProfileDEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 4 | PlanProfileDEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 5 | PlanProfileDEOEnterpriseId | ENTERPRISE_ID | — | — |
| 6 | PlanProfileDEOEventAssignmentId | EVENT_ASSIGNMENT_ID | — | — |
| 7 | PlanProfileDEOEventId | EVENT_ID | — | — |
| 8 | PlanProfileDEOInitialPlanRecordStatus | INITIAL_PLAN_RECORD_STATUS | — | — |
| 9 | PlanProfileDEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | PlanProfileDEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | PlanProfileDEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | PlanProfileDEOLearningPlanId | LEARNING_PLAN_ID | — | — |
| 13 | PlanProfileDEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | PlanProfileDEOPlanProfileId | PLAN_PROFILE_ID | 🔑 | ✅ |
| 15 | PlanProfileDEOPlanProfileType | PLAN_PROFILE_TYPE | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
