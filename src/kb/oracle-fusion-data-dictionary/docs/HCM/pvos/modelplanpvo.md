---
id: DOC-HCM-PVO-ModelPlanPVO
doc_type: system-doc
title: "ModelPlanPVO — PVO Human Capital Management"
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
  - ModelPlanPVO
  - modelplanpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ModelPlanPVO

## 📌 Visão Geral

Extrai planos de modelagem de workforce com nome traduzido e controle de acesso a gestores de topo. Base para gestão de cenários de planejamento de força de trabalho.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.WorkforceModelingAM.ModelPlanPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 32 | 2 | 1 | 13 | 41% |

---

## 🔗 Tabelas Relacionadas

- [[hmo_model_plans_b|HMO_MODEL_PLANS_B]] — 20 atributos (1 PKs, 10 BICC)
- [[hmo_model_plans_tl|HMO_MODEL_PLANS_TL]] — 12 atributos (3 BICC)

---

## ⚙️ Atributos

### [[hmo_model_plans_b|HMO_MODEL_PLANS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccessToTopManager | ACCESS_TO_TOP_MANAGER | — | ✅ |
| 2 | ActionId | ACTION_ID | — | — |
| 3 | ActionReasonId | ACTION_REASON_ID | — | — |
| 4 | AuthorPersonId | AUTHOR_PERSON_ID | — | — |
| 5 | CreatedBy | CREATED_BY | — | ✅ |
| 6 | CreationDate | CREATION_DATE | — | ✅ |
| 7 | EffectiveDate | EFFECTIVE_DATE | — | ✅ |
| 8 | EnterpriseId | ENTERPRISE_ID | — | — |
| 9 | LastSyncDate | LAST_SYNC_DATE | — | ✅ |
| 10 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | ModelLoaderBatchId | MODEL_LOADER_BATCH_ID | — | — |
| 14 | ModelPlanId | MODEL_PLAN_ID | 🔑 | ✅ |
| 15 | ModelPlanStatus | MODEL_PLAN_STATUS | — | ✅ |
| 16 | ModelPlanType | MODEL_PLAN_TYPE | — | ✅ |
| 17 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | TopManagerAssignmentId | TOP_MANAGER_ASSIGNMENT_ID | — | — |
| 19 | TopManagerId | TOP_MANAGER_ID | — | — |
| 20 | TopManagerType | TOP_MANAGER_TYPE | — | — |

### [[hmo_model_plans_tl|HMO_MODEL_PLANS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ModelPlanTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | ModelPlanTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | ModelPlanTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | ModelPlanTranslationPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 5 | ModelPlanTranslationPEOLanguage | LANGUAGE | — | — |
| 6 | ModelPlanTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ModelPlanTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | ModelPlanTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ModelPlanTranslationPEOModelPlanId | MODEL_PLAN_ID | — | — |
| 10 | ModelPlanTranslationPEOModelPlanName | MODEL_PLAN_NAME | — | ✅ |
| 11 | ModelPlanTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | ModelPlanTranslationPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
