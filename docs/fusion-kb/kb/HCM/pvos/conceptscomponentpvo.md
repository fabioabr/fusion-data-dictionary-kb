---
id: DOC-HCM-PVO-ConceptsComponentPVO
doc_type: system-doc
title: "ConceptsComponentPVO — PVO Human Capital Management"
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
  - ConceptsComponentPVO
  - conceptscomponentpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ConceptsComponentPVO

## 📌 Visão Geral

Disponibiliza componentes de conceitos de inovacao com tamanho e estrutura. Suporta detalhamento tecnico de ideias e solucoes no ciclo de inovacao.

**Caminho:** `FscmTopModelAM.ConceptsAnalyticsAM.ConceptsComponentPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 127 | 7 | 1 | 125 | 98% |

---

## 🔗 Tabelas Relacionadas

- [[acd_component_vl|ACD_COMPONENT_VL]] — 15 atributos (1 PKs, 14 BICC)
- [[acd_concept_b|ACD_CONCEPT_B]] — 16 atributos (16 BICC)
- [[acd_concept_structure|ACD_CONCEPT_STRUCTURE]] — 61 atributos (61 BICC)
- [[acd_concept_str_components_v|ACD_CONCEPT_STR_COMPONENTS_V]] — 2 atributos (2 BICC)
- [[acd_concept_str_concepts_v|ACD_CONCEPT_STR_CONCEPTS_V]] — 2 atributos (2 BICC)
- [[acd_concept_tl|ACD_CONCEPT_TL]] — 11 atributos (10 BICC)
- [[acd_metrics|ACD_METRICS]] — 20 atributos (20 BICC)

---

## ⚙️ Atributos

### [[acd_component_vl|ACD_COMPONENT_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ComponentComponentId | COMPONENT_ID | 🔑 | ✅ |
| 2 | ComponentComponentSize | COMPONENT_SIZE | — | ✅ |
| 3 | ComponentCreatedBy | CREATED_BY | — | ✅ |
| 4 | ComponentCreationDate | CREATION_DATE | — | ✅ |
| 5 | ComponentDescription | DESCRIPTION | — | — |
| 6 | ComponentLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ComponentLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | ComponentLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ComponentMaterial | MATERIAL | — | ✅ |
| 10 | ComponentName | NAME | — | ✅ |
| 11 | ComponentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | ComponentSupplier | SUPPLIER | — | ✅ |
| 13 | ComponentTargetType | TARGET_TYPE | — | ✅ |
| 14 | ComponentTopConceptId | TOP_CONCEPT_ID | — | ✅ |
| 15 | ComponentType | TYPE | — | ✅ |

### [[acd_concept_b|ACD_CONCEPT_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConceptBaseAllowAccesstoEveryone | ALLOW_ACCESSTO_EVERYONE | — | ✅ |
| 2 | ConceptBaseConceptId | CONCEPT_ID | — | ✅ |
| 3 | ConceptBaseConceptNumber | CONCEPT_NUMBER | — | ✅ |
| 4 | ConceptBaseCreatedBy | CREATED_BY | — | ✅ |
| 5 | ConceptBaseCreationDate | CREATION_DATE | — | ✅ |
| 6 | ConceptBaseCurrencyCode | CURRENCY_CODE | — | ✅ |
| 7 | ConceptBaseDueDate | DUE_DATE | — | ✅ |
| 8 | ConceptBaseIsCurrent | IS_CURRENT | — | ✅ |
| 9 | ConceptBaseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | ConceptBaseLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | ConceptBaseLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | ConceptBaseLifecyclePhase | LIFECYCLE_PHASE | — | ✅ |
| 13 | ConceptBaseMasterId | MASTER_ID | — | ✅ |
| 14 | ConceptBaseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 15 | ConceptBaseType | TYPE | — | ✅ |
| 16 | ConceptBaseVersion | VERSION | — | ✅ |

### [[acd_concept_structure|ACD_CONCEPT_STRUCTURE]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConceptStructureActualCost | ACTUAL_COST | — | ✅ |
| 2 | ConceptStructureActualPowerConsumption | ACTUAL_POWER_CONSUMPTION | — | ✅ |
| 3 | ConceptStructureActualWeight | ACTUAL_WEIGHT | — | ✅ |
| 4 | ConceptStructureAlternate | ALTERNATE | — | ✅ |
| 5 | ConceptStructureAnalyticsDirtyFlag | ANALYTICS_DIRTY_FLAG | — | ✅ |
| 6 | ConceptStructureAvailability | AVAILABILITY | — | ✅ |
| 7 | ConceptStructureCompliance | COMPLIANCE | — | ✅ |
| 8 | ConceptStructureConceptStructureId | CONCEPT_STRUCTURE_ID | — | ✅ |
| 9 | ConceptStructureCostIncomplete | COST_INCOMPLETE | — | ✅ |
| 10 | ConceptStructureCostNotes | COST_NOTES | — | ✅ |
| 11 | ConceptStructureCostVariance | COST_VARIANCE | — | ✅ |
| 12 | ConceptStructureCountryOfOrigin | COUNTRY_OF_ORIGIN | — | ✅ |
| 13 | ConceptStructureCreatedBy | CREATED_BY | — | ✅ |
| 14 | ConceptStructureCreationDate | CREATION_DATE | — | ✅ |
| 15 | ConceptStructureFixedCost | FIXED_COST | — | ✅ |
| 16 | ConceptStructureFromId | FROM_ID | — | ✅ |
| 17 | ConceptStructureFromStrId | FROM_STR_ID | — | ✅ |
| 18 | ConceptStructureFromType | FROM_TYPE | — | ✅ |
| 19 | ConceptStructureItemNumberManifacturers | ITEM_NUMBER_MANIFACTURERS | — | ✅ |
| 20 | ConceptStructureLastCostUpdate | LAST_COST_UPDATE | — | ✅ |
| 21 | ConceptStructureLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 22 | ConceptStructureLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 23 | ConceptStructureLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 24 | ConceptStructureLeadTime | LEAD_TIME | — | ✅ |
| 25 | ConceptStructureLocation | LOCATION | — | ✅ |
| 26 | ConceptStructureMaterial | MATERIAL | — | ✅ |
| 27 | ConceptStructureMaterialCost | MATERIAL_COST | — | ✅ |
| 28 | ConceptStructureMorphedId | MORPHED_ID | — | ✅ |
| 29 | ConceptStructureNonMaterialCost | NON_MATERIAL_COST | — | ✅ |
| 30 | ConceptStructureNumberManufacturers | NUMBER_MANUFACTURERS | — | ✅ |
| 31 | ConceptStructureObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 32 | ConceptStructurePlaceholder | PLACEHOLDER | — | ✅ |
| 33 | ConceptStructurePosNo | POS_NO | — | ✅ |
| 34 | ConceptStructurePowerConsumptionVariance | POWER_CONSUMPTION_VARIANCE | — | ✅ |
| 35 | ConceptStructurePowerIncomplete | POWER_INCOMPLETE | — | ✅ |
| 36 | ConceptStructurePowerUnit | POWER_UNIT | — | ✅ |
| 37 | ConceptStructurePreferredStatus | PREFERRED_STATUS | — | ✅ |
| 38 | ConceptStructurePrice | PRICE | — | ✅ |
| 39 | ConceptStructureQuantity | QUANTITY | — | ✅ |
| 40 | ConceptStructureReferenceDesignator | REFERENCE_DESIGNATOR | — | ✅ |
| 41 | ConceptStructureReqCountFulfilled | REQ_COUNT_FULFILLED | — | ✅ |
| 42 | ConceptStructureReqCountTotal | REQ_COUNT_TOTAL | — | ✅ |
| 43 | ConceptStructureRisk | RISK | — | ✅ |
| 44 | ConceptStructureScore | SCORE | — | ✅ |
| 45 | ConceptStructureStatus | STATUS | — | ✅ |
| 46 | ConceptStructureTargetCost | TARGET_COST | — | ✅ |
| 47 | ConceptStructureTargetPowerConsumption | TARGET_POWER_CONSUMPTION | — | ✅ |
| 48 | ConceptStructureTargetWeight | TARGET_WEIGHT | — | ✅ |
| 49 | ConceptStructureToId | TO_ID | — | ✅ |
| 50 | ConceptStructureToItemId | TO_ITEM_ID | — | ✅ |
| 51 | ConceptStructureToItemStrId | TO_ITEM_STR_ID | — | ✅ |
| 52 | ConceptStructureToType | TO_TYPE | — | ✅ |
| 53 | ConceptStructureTopConceptId | TOP_CONCEPT_ID | — | ✅ |
| 54 | ConceptStructureUnitSize | UNIT_SIZE | — | ✅ |
| 55 | ConceptStructureVendor | VENDOR | — | ✅ |
| 56 | ConceptStructureVendorNotes | VENDOR_NOTES | — | ✅ |
| 57 | ConceptStructureVolume | VOLUME | — | ✅ |
| 58 | ConceptStructureWeightIncomplete | WEIGHT_INCOMPLETE | — | ✅ |
| 59 | ConceptStructureWeightQuality | WEIGHT_QUALITY | — | ✅ |
| 60 | ConceptStructureWeightUnit | WEIGHT_UNIT | — | ✅ |
| 61 | ConceptStructureWeightVariance | WEIGHT_VARIANCE | — | ✅ |

### [[acd_concept_str_components_v|ACD_CONCEPT_STR_COMPONENTS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConceptStructureComponentsComponentId | COMPONENT_ID | — | ✅ |
| 2 | ConceptStructureComponentsConceptStructureId | CONCEPT_STRUCTURE_ID | — | ✅ |

### [[acd_concept_str_concepts_v|ACD_CONCEPT_STR_CONCEPTS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConceptStructureConceptsConceptId | CONCEPT_ID | — | ✅ |
| 2 | ConceptStructureConceptsConceptStructureId | CONCEPT_STRUCTURE_ID | — | ✅ |

### [[acd_concept_tl|ACD_CONCEPT_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConceptTranslationConceptId | CONCEPT_ID | — | ✅ |
| 2 | ConceptTranslationCreatedBy | CREATED_BY | — | ✅ |
| 3 | ConceptTranslationCreationDate | CREATION_DATE | — | ✅ |
| 4 | ConceptTranslationDescription | DESCRIPTION | — | — |
| 5 | ConceptTranslationLanguage | LANGUAGE | — | ✅ |
| 6 | ConceptTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ConceptTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | ConceptTranslationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ConceptTranslationName | NAME | — | ✅ |
| 10 | ConceptTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | ConceptTranslationSourceLang | SOURCE_LANG | — | ✅ |

### [[acd_metrics|ACD_METRICS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MetricsAlternativeIndex | ALTERNATIVE_INDEX | — | ✅ |
| 2 | MetricsCompliance | COMPLIANCE | — | ✅ |
| 3 | MetricsConceptStructureId | CONCEPT_STRUCTURE_ID | — | ✅ |
| 4 | MetricsCost | COST | — | ✅ |
| 5 | MetricsCostIncomplete | COST_INCOMPLETE | — | ✅ |
| 6 | MetricsCostVariance | COST_VARIANCE | — | ✅ |
| 7 | MetricsCreatedBy | CREATED_BY | — | ✅ |
| 8 | MetricsCreationDate | CREATION_DATE | — | ✅ |
| 9 | MetricsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | MetricsLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | MetricsLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | MetricsMetricsId | METRICS_ID | — | ✅ |
| 13 | MetricsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | MetricsPowerConsumption | POWER_CONSUMPTION | — | ✅ |
| 15 | MetricsPowerConsumptionVariance | POWER_CONSUMPTION_VARIANCE | — | ✅ |
| 16 | MetricsPowerIncomplete | POWER_INCOMPLETE | — | ✅ |
| 17 | MetricsScore | SCORE | — | ✅ |
| 18 | MetricsWeight | WEIGHT | — | ✅ |
| 19 | MetricsWeightIncomplete | WEIGHT_INCOMPLETE | — | ✅ |
| 20 | MetricsWeightVariance | WEIGHT_VARIANCE | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
