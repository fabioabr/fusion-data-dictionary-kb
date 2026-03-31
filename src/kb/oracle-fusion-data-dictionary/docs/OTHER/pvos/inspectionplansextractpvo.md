---
id: DOC-OTHER-PVO-InspectionPlansExtractPVO
doc_type: system-doc
title: "InspectionPlansExtractPVO — PVO Cross-Module"
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
  - InspectionPlansExtractPVO
  - inspectionplansextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InspectionPlansExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Inspection Plans Extract. Acessa as tabelas: QA_INSPECTION_PLANS_B, QA_INSPECTION_PLANS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.QaBiccExtractAM.InspectionPlansExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 30 | 2 | 2 | 30 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[qa_inspection_plans_b|QA_INSPECTION_PLANS_B]] — 20 atributos (20 BICC)
- [[qa_inspection_plans_tl|QA_INSPECTION_PLANS_TL]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[qa_inspection_plans_b|QA_INSPECTION_PLANS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InspectionPlansBaseRptPEOApprover | APPROVER | — | ✅ |
| 2 | InspectionPlansBaseRptPEOAssetGroupId | ASSET_GROUP_ID | — | ✅ |
| 3 | InspectionPlansBaseRptPEOAssetId | ASSET_ID | — | ✅ |
| 4 | InspectionPlansBaseRptPEOCategoryId | CATEGORY_ID | — | ✅ |
| 5 | InspectionPlansBaseRptPEOCategorySetId | CATEGORY_SET_ID | — | ✅ |
| 6 | InspectionPlansBaseRptPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 7 | InspectionPlansBaseRptPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 8 | InspectionPlansBaseRptPEOEnabledFlag | ENABLED_FLAG | — | ✅ |
| 9 | InspectionPlansBaseRptPEOInspectionLevelId | INSPECTION_LEVEL_ID | — | ✅ |
| 10 | InspectionPlansBaseRptPEOInspectionPlanId | INSPECTION_PLAN_ID | — | ✅ |
| 11 | InspectionPlansBaseRptPEOInspectionPlanStatus | INSPECTION_PLAN_STATUS | — | ✅ |
| 12 | InspectionPlansBaseRptPEOInspectionPlanType | INSPECTION_PLAN_TYPE | — | ✅ |
| 13 | InspectionPlansBaseRptPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 14 | InspectionPlansBaseRptPEOOptionalFlag | OPTIONAL_FLAG | — | ✅ |
| 15 | InspectionPlansBaseRptPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 16 | InspectionPlansBaseRptPEOOwner | OWNER | — | ✅ |
| 17 | InspectionPlansBaseRptPEOResourceId | RESOURCE_ID | — | ✅ |
| 18 | InspectionPlansBaseRptPEORevision | REVISION | — | ✅ |
| 19 | InspectionPlansBaseRptPEOVersionNumber | VERSION_NUMBER | — | ✅ |
| 20 | InspectionPlansBaseRptPEOWorkCenterId | WORK_CENTER_ID | — | ✅ |

### [[qa_inspection_plans_tl|QA_INSPECTION_PLANS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InspectionPlansTLRptPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | InspectionPlansTLRptPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | InspectionPlansTLRptPEODescription | DESCRIPTION | — | ✅ |
| 4 | InspectionPlansTLRptPEOInspectionPlanId | INSPECTION_PLAN_ID | 🔑 | ✅ |
| 5 | InspectionPlansTLRptPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | InspectionPlansTLRptPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | InspectionPlansTLRptPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | InspectionPlansTLRptPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | InspectionPlansTLRptPEOName | NAME | — | ✅ |
| 10 | InspectionPlansTLRptPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
