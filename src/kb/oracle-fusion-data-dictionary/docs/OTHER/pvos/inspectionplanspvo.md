---
id: DOC-OTHER-PVO-InspectionPlansPVO
doc_type: system-doc
title: "InspectionPlansPVO — PVO Cross-Module"
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
  - InspectionPlansPVO
  - inspectionplanspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InspectionPlansPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Inspection Plans. Acessa as tabelas: QA_INSPECTION_PLANS_B, QA_INSPECTION_PLANS_TL.

**Caminho:** `FscmTopModelAM.InspectionPlansAM.InspectionPlansPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 38 | 2 | 1 | 36 | 95% |

---

## 🔗 Tabelas Relacionadas

- [[qa_inspection_plans_b|QA_INSPECTION_PLANS_B]] — 27 atributos (1 PKs, 25 BICC)
- [[qa_inspection_plans_tl|QA_INSPECTION_PLANS_TL]] — 11 atributos (11 BICC)

---

## ⚙️ Atributos

### [[qa_inspection_plans_b|QA_INSPECTION_PLANS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InspectionPlansBasePEOApprover | APPROVER | — | ✅ |
| 2 | InspectionPlansBasePEOAssetGroupId | ASSET_GROUP_ID | — | — |
| 3 | InspectionPlansBasePEOAssetId | ASSET_ID | — | — |
| 4 | InspectionPlansBasePEOCategoryId | CATEGORY_ID | — | ✅ |
| 5 | InspectionPlansBasePEOCategorySetId | CATEGORY_SET_ID | — | ✅ |
| 6 | InspectionPlansBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 7 | InspectionPlansBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | InspectionPlansBasePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 9 | InspectionPlansBasePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 10 | InspectionPlansBasePEOEnabledFlag | ENABLED_FLAG | — | ✅ |
| 11 | InspectionPlansBasePEOInspectionLevelId | INSPECTION_LEVEL_ID | — | ✅ |
| 12 | InspectionPlansBasePEOInspectionPlanCode | INSPECTION_PLAN_CODE | — | ✅ |
| 13 | InspectionPlansBasePEOInspectionPlanId | INSPECTION_PLAN_ID | 🔑 | ✅ |
| 14 | InspectionPlansBasePEOInspectionPlanStatus | INSPECTION_PLAN_STATUS | — | ✅ |
| 15 | InspectionPlansBasePEOInspectionPlanType | INSPECTION_PLAN_TYPE | — | ✅ |
| 16 | InspectionPlansBasePEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 17 | InspectionPlansBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 18 | InspectionPlansBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 19 | InspectionPlansBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 20 | InspectionPlansBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 21 | InspectionPlansBasePEOOptionalFlag | OPTIONAL_FLAG | — | ✅ |
| 22 | InspectionPlansBasePEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 23 | InspectionPlansBasePEOOwner | OWNER | — | ✅ |
| 24 | InspectionPlansBasePEOResourceId | RESOURCE_ID | — | ✅ |
| 25 | InspectionPlansBasePEORevision | REVISION | — | ✅ |
| 26 | InspectionPlansBasePEOVersionNumber | VERSION_NUMBER | — | ✅ |
| 27 | InspectionPlansBasePEOWorkCenterId | WORK_CENTER_ID | — | ✅ |

### [[qa_inspection_plans_tl|QA_INSPECTION_PLANS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InspectionPlansTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | InspectionPlansTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | InspectionPlansTLPEODescription | DESCRIPTION | — | ✅ |
| 4 | InspectionPlansTLPEOInspectionPlanId | INSPECTION_PLAN_ID | — | ✅ |
| 5 | InspectionPlansTLPEOLanguage | LANGUAGE | — | ✅ |
| 6 | InspectionPlansTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | InspectionPlansTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | InspectionPlansTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | InspectionPlansTLPEOName | NAME | — | ✅ |
| 10 | InspectionPlansTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | InspectionPlansTLPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
