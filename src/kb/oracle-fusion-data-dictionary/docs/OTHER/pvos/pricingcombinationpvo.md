---
id: DOC-OTHER-PVO-PricingCombinationPVO
doc_type: system-doc
title: "PricingCombinationPVO — PVO Cross-Module"
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
  - PricingCombinationPVO
  - pricingcombinationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PricingCombinationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Pricing Combination. Acessa as tabelas: FND_KF_STRUCTURES_VL, FND_KF_STR_INSTANCES_VL, PER_PERSON_NAMES_F_V (+2).

**Caminho:** `FscmTopModelAM.FinVrmRCSetupDimPublicModelAM.PricingCombinationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 64 | 5 | 1 | 15 | 23% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_kf_structures_vl|FND_KF_STRUCTURES_VL]] — 2 atributos (1 BICC)
- [[fnd_kf_str_instances_vl|FND_KF_STR_INSTANCES_VL]] — 3 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 8 atributos
- [[per_users|PER_USERS]] — 4 atributos
- [[vrm_pricing_combinations|VRM_PRICING_COMBINATIONS]] — 47 atributos (1 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[fnd_kf_structures_vl|FND_KF_STRUCTURES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | KeyFlexfieldStructurePEOKeyFlexfieldStructureName | NAME | — | ✅ |
| 2 | KeyFlexfieldStructurePEOStructureId | STRUCTURE_ID | — | — |

### [[fnd_kf_str_instances_vl|FND_KF_STR_INSTANCES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | KFFStrucInstApplicationId | APPLICATION_ID | — | — |
| 2 | KFFStrucInstKeyFlexFieldCode | KEY_FLEXFIELD_CODE | — | — |
| 3 | KFFStrucInstStructInstanceId | STRUCTURE_INSTANCE_ID | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonCreatedByDisplayName | DISPLAY_NAME | — | — |
| 2 | PersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | PersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 5 | PersonUpdatedByDisplayName | DISPLAY_NAME | — | — |
| 6 | PersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 7 | PersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 8 | PersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserCreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | UserCreatedByUserId | USER_ID | — | — |
| 3 | UserUpdatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 4 | UserUpdatedByUserId | USER_ID | — | — |

### [[vrm_pricing_combinations|VRM_PRICING_COMBINATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PricingCombinationId | PRICING_COMBINATION_ID | 🔑 | ✅ |
| 2 | PricingDimensionCombinationCreatedByUserId | CREATED_BY | — | ✅ |
| 3 | PricingDimensionCombinationCreationDate | CREATION_DATE | — | ✅ |
| 4 | PricingDimensionCombinationEnabledFlag | ENABLED_FLAG | — | ✅ |
| 5 | PricingDimensionCombinationEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 6 | PricingDimensionCombinationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | PricingDimensionCombinationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | PricingDimensionCombinationLastUpdatedByUserId | LAST_UPDATED_BY | — | ✅ |
| 9 | PricingDimensionCombinationMinimumLineCount | MINIMUM_LINE_COUNT | — | ✅ |
| 10 | PricingDimensionCombinationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | PricingDimensionCombinationSegment1 | SEGMENT1 | — | — |
| 12 | PricingDimensionCombinationSegment10 | SEGMENT10 | — | — |
| 13 | PricingDimensionCombinationSegment11 | SEGMENT11 | — | — |
| 14 | PricingDimensionCombinationSegment12 | SEGMENT12 | — | — |
| 15 | PricingDimensionCombinationSegment13 | SEGMENT13 | — | — |
| 16 | PricingDimensionCombinationSegment14 | SEGMENT14 | — | — |
| 17 | PricingDimensionCombinationSegment15 | SEGMENT15 | — | — |
| 18 | PricingDimensionCombinationSegment16 | SEGMENT16 | — | — |
| 19 | PricingDimensionCombinationSegment17 | SEGMENT17 | — | — |
| 20 | PricingDimensionCombinationSegment18 | SEGMENT18 | — | — |
| 21 | PricingDimensionCombinationSegment19 | SEGMENT19 | — | — |
| 22 | PricingDimensionCombinationSegment2 | SEGMENT2 | — | — |
| 23 | PricingDimensionCombinationSegment20 | SEGMENT20 | — | — |
| 24 | PricingDimensionCombinationSegment21 | SEGMENT21 | — | — |
| 25 | PricingDimensionCombinationSegment22 | SEGMENT22 | — | — |
| 26 | PricingDimensionCombinationSegment23 | SEGMENT23 | — | — |
| 27 | PricingDimensionCombinationSegment24 | SEGMENT24 | — | — |
| 28 | PricingDimensionCombinationSegment25 | SEGMENT25 | — | — |
| 29 | PricingDimensionCombinationSegment26 | SEGMENT26 | — | — |
| 30 | PricingDimensionCombinationSegment27 | SEGMENT27 | — | — |
| 31 | PricingDimensionCombinationSegment28 | SEGMENT28 | — | — |
| 32 | PricingDimensionCombinationSegment29 | SEGMENT29 | — | — |
| 33 | PricingDimensionCombinationSegment3 | SEGMENT3 | — | — |
| 34 | PricingDimensionCombinationSegment30 | SEGMENT30 | — | — |
| 35 | PricingDimensionCombinationSegment4 | SEGMENT4 | — | — |
| 36 | PricingDimensionCombinationSegment5 | SEGMENT5 | — | — |
| 37 | PricingDimensionCombinationSegment6 | SEGMENT6 | — | — |
| 38 | PricingDimensionCombinationSegment7 | SEGMENT7 | — | — |
| 39 | PricingDimensionCombinationSegment8 | SEGMENT8 | — | — |
| 40 | PricingDimensionCombinationSegment9 | SEGMENT9 | — | — |
| 41 | PricingDimensionCombinationStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 42 | PricingDimensionCombinationStructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | ✅ |
| 43 | PricingDimensionCombinationSummaryFlag | SUMMARY_FLAG | — | — |
| 44 | PricingDimensionCombinationTolerancePctRangeHigh | TOLERANCE_PCT_RANGE_HIGH | — | ✅ |
| 45 | PricingDimensionCombinationTolerancePctRangeLow | TOLERANCE_PCT_RANGE_LOW | — | ✅ |
| 46 | PricingDimensionCombinationToleranceRangeCoverage | TOLERANCE_RANGE_COVERAGE | — | ✅ |
| 47 | PricingDimensionCombinationUseToleranceForCompliance | USE_TOLERANCE_FOR_COMPLIANCE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
