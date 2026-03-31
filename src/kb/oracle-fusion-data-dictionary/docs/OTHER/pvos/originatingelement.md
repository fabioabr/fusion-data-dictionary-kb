---
id: DOC-OTHER-PVO-OriginatingElement
doc_type: system-doc
title: "OriginatingElement — PVO Cross-Module"
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
  - OriginatingElement
  - originatingelement
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# OriginatingElement

## 📌 Visão Geral

View Object para extração BICC de dados de Originating Element. Acessa as tabelas: PAY_ELEMENT_TYPES_F, PAY_ELEMENT_TYPES_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmElementSetupAM.OriginatingElement`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 58 | 2 | 3 | 16 | 28% |

---

## 🔗 Tabelas Relacionadas

- [[pay_element_types_f|PAY_ELEMENT_TYPES_F]] — 52 atributos (3 PKs, 12 BICC)
- [[pay_element_types_tl|PAY_ELEMENT_TYPES_TL]] — 6 atributos (4 BICC)

---

## ⚙️ Atributos

### [[pay_element_types_f|PAY_ELEMENT_TYPES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 3 | ElementTypeAdditionalEntryAllowedFlag | ADDITIONAL_ENTRY_ALLOWED_FLAG | — | — |
| 4 | ElementTypeAdjustmentOnlyFlag | ADJUSTMENT_ONLY_FLAG | — | — |
| 5 | ElementTypeAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 6 | ElementTypeBaseElementName | BASE_ELEMENT_NAME | — | — |
| 7 | ElementTypeCalculationFormulaId | CALCULATION_FORMULA_ID | — | — |
| 8 | ElementTypeClassificationId | CLASSIFICATION_ID | — | ✅ |
| 9 | ElementTypeClosedForEntryFlag | CLOSED_FOR_ENTRY_FLAG | — | — |
| 10 | ElementTypeCreatedBy | CREATED_BY | — | — |
| 11 | ElementTypeCreationDate | CREATION_DATE | — | — |
| 12 | ElementTypeCreatorType | CREATOR_TYPE | — | — |
| 13 | ElementTypeDeductionOrExemption | DEDUCTION_OR_EXEMPTION | — | — |
| 14 | ElementTypeDeductionTypeId | DEDUCTION_TYPE_ID | — | — |
| 15 | ElementTypeDefaultingFormulaId | DEFAULTING_FORMULA_ID | — | — |
| 16 | ElementTypeElementInformationCategory | ELEMENT_INFORMATION_CATEGORY | — | — |
| 17 | ElementTypeEndingTimeDefId | ENDING_TIME_DEF_ID | — | — |
| 18 | ElementTypeFormulaId | FORMULA_ID | — | — |
| 19 | ElementTypeGrossupFlag | GROSSUP_FLAG | — | — |
| 20 | ElementTypeId | ELEMENT_TYPE_ID | 🔑 | ✅ |
| 21 | ElementTypeIndirectOnlyFlag | INDIRECT_ONLY_FLAG | — | — |
| 22 | ElementTypeInputCurrencyCode | INPUT_CURRENCY_CODE | — | ✅ |
| 23 | ElementTypeIterativeFlag | ITERATIVE_FLAG | — | — |
| 24 | ElementTypeIterativeFormulaId | ITERATIVE_FORMULA_ID | — | — |
| 25 | ElementTypeIterativePriority | ITERATIVE_PRIORITY | — | — |
| 26 | ElementTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 27 | ElementTypeLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 28 | ElementTypeLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 29 | ElementTypeLegislationCode | LEGISLATION_CODE | — | ✅ |
| 30 | ElementTypeLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | ✅ |
| 31 | ElementTypeModuleId | MODULE_ID | — | — |
| 32 | ElementTypeMultipleEntriesAllowedFlag | MULTIPLE_ENTRIES_ALLOWED_FLAG | — | — |
| 33 | ElementTypeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 34 | ElementTypeOnceEachPeriodFlag | ONCE_EACH_PERIOD_FLAG | — | — |
| 35 | ElementTypeOutputCurrencyCode | OUTPUT_CURRENCY_CODE | — | ✅ |
| 36 | ElementTypeProcessInRunFlag | PROCESS_IN_RUN_FLAG | — | — |
| 37 | ElementTypeProcessMode | PROCESS_MODE | — | — |
| 38 | ElementTypeProcessingPriority | PROCESSING_PRIORITY | — | — |
| 39 | ElementTypeProcessingType | PROCESSING_TYPE | — | ✅ |
| 40 | ElementTypeProrationFormulaId | PRORATION_FORMULA_ID | — | — |
| 41 | ElementTypeProrationGroupId | PRORATION_GROUP_ID | — | — |
| 42 | ElementTypeRecalcEventGroupId | RECALC_EVENT_GROUP_ID | — | ✅ |
| 43 | ElementTypeSecondaryClassificationId | SECONDARY_CLASSIFICATION_ID | — | ✅ |
| 44 | ElementTypeStandardLinkFlag | STANDARD_LINK_FLAG | — | — |
| 45 | ElementTypeStartingTimeDefId | STARTING_TIME_DEF_ID | — | — |
| 46 | ElementTypeTimeDefinitionId | TIME_DEFINITION_ID | — | — |
| 47 | ElementTypeTimeDefinitionType | TIME_DEFINITION_TYPE | — | — |
| 48 | ElementTypeUseAtAsgLevel | USE_AT_ASG_LEVEL | — | — |
| 49 | ElementTypeUseAtRelLevel | USE_AT_REL_LEVEL | — | — |
| 50 | ElementTypeUseAtTermLevel | USE_AT_TERM_LEVEL | — | — |
| 51 | ElementTypeValidationFormulaId | VALIDATION_FORMULA_ID | — | — |
| 52 | ElementTypeValidationOverrideMessage | VALIDATION_OVERRIDE_MESSAGE | — | — |

### [[pay_element_types_tl|PAY_ELEMENT_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ElementTypeTranslationDescription | DESCRIPTION | — | ✅ |
| 2 | ElementTypeTranslationElementName | ELEMENT_NAME | — | ✅ |
| 3 | ElementTypeTranslationElementTypeId | ELEMENT_TYPE_ID | — | — |
| 4 | ElementTypeTranslationLanguage | LANGUAGE | — | ✅ |
| 5 | ElementTypeTranslationReportingName | REPORTING_NAME | — | ✅ |
| 6 | ElementTypeTranslationSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
