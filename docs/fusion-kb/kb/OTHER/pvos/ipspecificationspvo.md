---
id: DOC-OTHER-PVO-IpSpecificationsPVO
doc_type: system-doc
title: "IpSpecificationsPVO — PVO Cross-Module"
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
  - IpSpecificationsPVO
  - ipspecificationspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# IpSpecificationsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Ip Specifications. Acessa as tabelas: QA_CHARACTERISTICS_B, QA_CHARACTERISTICS_TL, QA_INSPECTION_PLANS_B (+1).

**Caminho:** `FscmTopModelAM.InspectionPlansAM.IpSpecificationsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 79 | 4 | 1 | 76 | 96% |

---

## 🔗 Tabelas Relacionadas

- [[qa_characteristics_b|QA_CHARACTERISTICS_B]] — 25 atributos (25 BICC)
- [[qa_characteristics_tl|QA_CHARACTERISTICS_TL]] — 11 atributos (11 BICC)
- [[qa_inspection_plans_b|QA_INSPECTION_PLANS_B]] — 25 atributos (25 BICC)
- [[qa_ip_specifications|QA_IP_SPECIFICATIONS]] — 18 atributos (1 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[qa_characteristics_b|QA_CHARACTERISTICS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CharacteristicBasePEOAttributeGroupMaximum | ATTRIBUTE_GROUP_MAXIMUM | — | ✅ |
| 2 | CharacteristicBasePEOAttributeGroupMinimum | ATTRIBUTE_GROUP_MINIMUM | — | ✅ |
| 3 | CharacteristicBasePEOAttributeGroupTarget | ATTRIBUTE_GROUP_TARGET | — | ✅ |
| 4 | CharacteristicBasePEOAttributeMaximum | ATTRIBUTE_MAXIMUM | — | ✅ |
| 5 | CharacteristicBasePEOAttributeMinimum | ATTRIBUTE_MINIMUM | — | ✅ |
| 6 | CharacteristicBasePEOAttributeTarget | ATTRIBUTE_TARGET | — | ✅ |
| 7 | CharacteristicBasePEOCharacteristicCode | CHARACTERISTIC_CODE | — | ✅ |
| 8 | CharacteristicBasePEOCharacteristicId | CHARACTERISTIC_ID | — | ✅ |
| 9 | CharacteristicBasePEOCharacteristicType | CHARACTERISTIC_TYPE | — | ✅ |
| 10 | CharacteristicBasePEOContextType | CONTEXT_TYPE | — | ✅ |
| 11 | CharacteristicBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 12 | CharacteristicBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 13 | CharacteristicBasePEODataType | DATA_TYPE | — | ✅ |
| 14 | CharacteristicBasePEODecimalPrecision | DECIMAL_PRECISION | — | ✅ |
| 15 | CharacteristicBasePEODefaultValue | DEFAULT_VALUE | — | ✅ |
| 16 | CharacteristicBasePEOEnabledFlag | ENABLED_FLAG | — | ✅ |
| 17 | CharacteristicBasePEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 18 | CharacteristicBasePEOItemClassId | ITEM_CLASS_ID | — | ✅ |
| 19 | CharacteristicBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 20 | CharacteristicBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 21 | CharacteristicBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 22 | CharacteristicBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 23 | CharacteristicBasePEOStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 24 | CharacteristicBasePEOUomCode | UOM_CODE | — | ✅ |
| 25 | CharacteristicBasePEOValueSetId | VALUE_SET_ID | — | ✅ |

### [[qa_characteristics_tl|QA_CHARACTERISTICS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CharacteristicTLPEOCharacteristicId | CHARACTERISTIC_ID | — | ✅ |
| 2 | CharacteristicTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | CharacteristicTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | CharacteristicTLPEODescription | DESCRIPTION | — | ✅ |
| 5 | CharacteristicTLPEOLanguage | LANGUAGE | — | ✅ |
| 6 | CharacteristicTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | CharacteristicTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | CharacteristicTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | CharacteristicTLPEOName | NAME | — | ✅ |
| 10 | CharacteristicTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | CharacteristicTLPEOSourceLang | SOURCE_LANG | — | ✅ |

### [[qa_inspection_plans_b|QA_INSPECTION_PLANS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InspectionPlansBasePEOApprover | APPROVER | — | ✅ |
| 2 | InspectionPlansBasePEOCategoryId | CATEGORY_ID | — | ✅ |
| 3 | InspectionPlansBasePEOCategorySetId | CATEGORY_SET_ID | — | ✅ |
| 4 | InspectionPlansBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | InspectionPlansBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | InspectionPlansBasePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 7 | InspectionPlansBasePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 8 | InspectionPlansBasePEOEnabledFlag | ENABLED_FLAG | — | ✅ |
| 9 | InspectionPlansBasePEOInspectionLevelId | INSPECTION_LEVEL_ID | — | ✅ |
| 10 | InspectionPlansBasePEOInspectionPlanCode | INSPECTION_PLAN_CODE | — | ✅ |
| 11 | InspectionPlansBasePEOInspectionPlanId | INSPECTION_PLAN_ID | — | ✅ |
| 12 | InspectionPlansBasePEOInspectionPlanStatus | INSPECTION_PLAN_STATUS | — | ✅ |
| 13 | InspectionPlansBasePEOInspectionPlanType | INSPECTION_PLAN_TYPE | — | ✅ |
| 14 | InspectionPlansBasePEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 15 | InspectionPlansBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | InspectionPlansBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 17 | InspectionPlansBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 18 | InspectionPlansBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 19 | InspectionPlansBasePEOOptionalFlag | OPTIONAL_FLAG | — | ✅ |
| 20 | InspectionPlansBasePEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 21 | InspectionPlansBasePEOOwner | OWNER | — | ✅ |
| 22 | InspectionPlansBasePEOResourceId | RESOURCE_ID | — | ✅ |
| 23 | InspectionPlansBasePEORevision | REVISION | — | ✅ |
| 24 | InspectionPlansBasePEOVersionNumber | VERSION_NUMBER | — | ✅ |
| 25 | InspectionPlansBasePEOWorkCenterId | WORK_CENTER_ID | — | ✅ |

### [[qa_ip_specifications|QA_IP_SPECIFICATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IpSpecificationPEOCharacteristicId | CHARACTERISTIC_ID | — | ✅ |
| 2 | IpSpecificationPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | IpSpecificationPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | IpSpecificationPEOEnabledFlag | ENABLED_FLAG | — | ✅ |
| 5 | IpSpecificationPEOInspectionPlanId | INSPECTION_PLAN_ID | — | ✅ |
| 6 | IpSpecificationPEOIpSpecificationId | IP_SPECIFICATION_ID | 🔑 | ✅ |
| 7 | IpSpecificationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | IpSpecificationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | IpSpecificationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | IpSpecificationPEOMaximumValue | MAXIMUM_VALUE | — | ✅ |
| 11 | IpSpecificationPEOMaximumValueDate | MAXIMUM_VALUE_DATE | — | — |
| 12 | IpSpecificationPEOMinimumValue | MINIMUM_VALUE | — | ✅ |
| 13 | IpSpecificationPEOMinimumValueDate | MINIMUM_VALUE_DATE | — | — |
| 14 | IpSpecificationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 15 | IpSpecificationPEOTargetValue | TARGET_VALUE | — | ✅ |
| 16 | IpSpecificationPEOTargetValueDate | TARGET_VALUE_DATE | — | — |
| 17 | IpSpecificationPEOUomCode | UOM_CODE | — | ✅ |
| 18 | IpSpecificationPEOUserSequence | USER_SEQUENCE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
