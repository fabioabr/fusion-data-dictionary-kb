---
id: DOC-GL-PVO-ElementTypeClassificationPVO
doc_type: system-doc
title: "ElementTypeClassificationPVO — PVO General Ledger"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - gl
  - data-dictionary
  - pvo
  - bicc
aliases:
  - ElementTypeClassificationPVO
  - elementtypeclassificationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ElementTypeClassificationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Element Type Classification. Acessa as tabelas: PAY_ELEMENT_TYPES_F, PAY_ELE_CLASSIFICATIONS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.AccrualAM.ElementTypeClassificationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 76 | 2 | 3 | 5 | 7% |

---

## 🔗 Tabelas Relacionadas

- [[pay_element_types_f|PAY_ELEMENT_TYPES_F]] — 50 atributos (3 PKs, 4 BICC)
- [[pay_ele_classifications|PAY_ELE_CLASSIFICATIONS]] — 26 atributos (1 BICC)

---

## ⚙️ Atributos

### [[pay_element_types_f|PAY_ELEMENT_TYPES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 3 | ElementTypeDPEOAdditionalEntryAllowedFlag | ADDITIONAL_ENTRY_ALLOWED_FLAG | — | — |
| 4 | ElementTypeDPEOAdjustmentOnlyFlag | ADJUSTMENT_ONLY_FLAG | — | — |
| 5 | ElementTypeDPEOBaseElementName | BASE_ELEMENT_NAME | — | — |
| 6 | ElementTypeDPEOCalculationFormulaId | CALCULATION_FORMULA_ID | — | — |
| 7 | ElementTypeDPEOClassificationId | CLASSIFICATION_ID | — | — |
| 8 | ElementTypeDPEOClosedForEntryFlag | CLOSED_FOR_ENTRY_FLAG | — | — |
| 9 | ElementTypeDPEOCreatedBy | CREATED_BY | — | — |
| 10 | ElementTypeDPEOCreationDate | CREATION_DATE | — | — |
| 11 | ElementTypeDPEOCreatorType | CREATOR_TYPE | — | — |
| 12 | ElementTypeDPEODeductionOrExemption | DEDUCTION_OR_EXEMPTION | — | — |
| 13 | ElementTypeDPEODeductionTypeId | DEDUCTION_TYPE_ID | — | — |
| 14 | ElementTypeDPEODefaultingFormulaId | DEFAULTING_FORMULA_ID | — | — |
| 15 | ElementTypeDPEOEndingTimeDefId | ENDING_TIME_DEF_ID | — | — |
| 16 | ElementTypeDPEOFormulaId | FORMULA_ID | — | — |
| 17 | ElementTypeDPEOGrossupFlag | GROSSUP_FLAG | — | — |
| 18 | ElementTypeDPEOIndirectOnlyFlag | INDIRECT_ONLY_FLAG | — | — |
| 19 | ElementTypeDPEOInputCurrencyCode | INPUT_CURRENCY_CODE | — | — |
| 20 | ElementTypeDPEOIterativeFlag | ITERATIVE_FLAG | — | — |
| 21 | ElementTypeDPEOIterativeFormulaId | ITERATIVE_FORMULA_ID | — | — |
| 22 | ElementTypeDPEOIterativePriority | ITERATIVE_PRIORITY | — | — |
| 23 | ElementTypeDPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 24 | ElementTypeDPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 25 | ElementTypeDPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 26 | ElementTypeDPEOLegislationCode | LEGISLATION_CODE | — | — |
| 27 | ElementTypeDPEOLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | — |
| 28 | ElementTypeDPEOModuleId | MODULE_ID | — | — |
| 29 | ElementTypeDPEOMultipleEntriesAllowedFlag | MULTIPLE_ENTRIES_ALLOWED_FLAG | — | — |
| 30 | ElementTypeDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 31 | ElementTypeDPEOOnceEachPeriodFlag | ONCE_EACH_PERIOD_FLAG | — | — |
| 32 | ElementTypeDPEOOutputCurrencyCode | OUTPUT_CURRENCY_CODE | — | — |
| 33 | ElementTypeDPEOProcessInRunFlag | PROCESS_IN_RUN_FLAG | — | — |
| 34 | ElementTypeDPEOProcessMode | PROCESS_MODE | — | — |
| 35 | ElementTypeDPEOProcessingPriority | PROCESSING_PRIORITY | — | — |
| 36 | ElementTypeDPEOProcessingType | PROCESSING_TYPE | — | — |
| 37 | ElementTypeDPEOProrationFormulaId | PRORATION_FORMULA_ID | — | — |
| 38 | ElementTypeDPEOProrationGroupId | PRORATION_GROUP_ID | — | — |
| 39 | ElementTypeDPEORecalcEventGroupId | RECALC_EVENT_GROUP_ID | — | — |
| 40 | ElementTypeDPEOSecondaryClassificationId | SECONDARY_CLASSIFICATION_ID | — | — |
| 41 | ElementTypeDPEOStandardLinkFlag | STANDARD_LINK_FLAG | — | — |
| 42 | ElementTypeDPEOStartingTimeDefId | STARTING_TIME_DEF_ID | — | — |
| 43 | ElementTypeDPEOTimeDefinitionId | TIME_DEFINITION_ID | — | — |
| 44 | ElementTypeDPEOTimeDefinitionType | TIME_DEFINITION_TYPE | — | — |
| 45 | ElementTypeDPEOUseAtAsgLevel | USE_AT_ASG_LEVEL | — | — |
| 46 | ElementTypeDPEOUseAtRelLevel | USE_AT_REL_LEVEL | — | — |
| 47 | ElementTypeDPEOUseAtTermLevel | USE_AT_TERM_LEVEL | — | — |
| 48 | ElementTypeDPEOValidationFormulaId | VALIDATION_FORMULA_ID | — | — |
| 49 | ElementTypeDPEOValidationOverrideMessage | VALIDATION_OVERRIDE_MESSAGE | — | — |
| 50 | ElementTypeId | ELEMENT_TYPE_ID | 🔑 | ✅ |

### [[pay_ele_classifications|PAY_ELE_CLASSIFICATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ElementClassificationPVOBaseClassificationId | BASE_CLASSIFICATION_ID | — | — |
| 2 | ElementClassificationPVOBaseClassificationName | BASE_CLASSIFICATION_NAME | — | — |
| 3 | ElementClassificationPVOClassificationId | CLASSIFICATION_ID | — | — |
| 4 | ElementClassificationPVOCostableFlag | COSTABLE_FLAG | — | — |
| 5 | ElementClassificationPVOCostingDebitOrCredit | COSTING_DEBIT_OR_CREDIT | — | — |
| 6 | ElementClassificationPVOCreateByDefaultFlag | CREATE_BY_DEFAULT_FLAG | — | — |
| 7 | ElementClassificationPVOCreatedBy | CREATED_BY | — | — |
| 8 | ElementClassificationPVOCreationDate | CREATION_DATE | — | — |
| 9 | ElementClassificationPVODateFrom | DATE_FROM | — | — |
| 10 | ElementClassificationPVODateTo | DATE_TO | — | — |
| 11 | ElementClassificationPVODefaultHighPriority | DEFAULT_HIGH_PRIORITY | — | — |
| 12 | ElementClassificationPVODefaultLowPriority | DEFAULT_LOW_PRIORITY | — | — |
| 13 | ElementClassificationPVODefaultPriority | DEFAULT_PRIORITY | — | — |
| 14 | ElementClassificationPVODistributableOverFlag | DISTRIBUTABLE_OVER_FLAG | — | — |
| 15 | ElementClassificationPVOFreqRuleEnabled | FREQ_RULE_ENABLED | — | — |
| 16 | ElementClassificationPVOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | ElementClassificationPVOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 18 | ElementClassificationPVOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 19 | ElementClassificationPVOLegislationCode | LEGISLATION_CODE | — | — |
| 20 | ElementClassificationPVOLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | — |
| 21 | ElementClassificationPVOModuleId | MODULE_ID | — | — |
| 22 | ElementClassificationPVONonPaymentsFlag | NON_PAYMENTS_FLAG | — | — |
| 23 | ElementClassificationPVOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 24 | ElementClassificationPVOParentClassificationId | PARENT_CLASSIFICATION_ID | — | — |
| 25 | ElementClassificationPVOProcessWhenEarning | PROCESS_WHEN_EARNING | — | — |
| 26 | ElementClassificationPVOSecondaryClassificationFlag | SECONDARY_CLASSIFICATION_FLAG | — | — |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
