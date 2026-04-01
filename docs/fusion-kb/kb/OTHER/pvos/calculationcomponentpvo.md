---
id: DOC-OTHER-PVO-CalculationComponentPVO
doc_type: system-doc
title: "CalculationComponentPVO — PVO Cross-Module"
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
  - CalculationComponentPVO
  - calculationcomponentpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CalculationComponentPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Calculation Component. Acessa as tabelas: PAY_DIR_CARDS_F, PAY_DIR_CARD_COMPONENTS_F, PAY_DIR_CARD_COMP_DEFS_VL (+2).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmPayDeductionSetupAM.CalculationComponentPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 78 | 5 | 6 | 27 | 35% |

---

## 🔗 Tabelas Relacionadas

- [[pay_dir_cards_f|PAY_DIR_CARDS_F]] — 16 atributos (3 PKs, 8 BICC)
- [[pay_dir_card_components_f|PAY_DIR_CARD_COMPONENTS_F]] — 20 atributos (3 PKs, 10 BICC)
- [[pay_dir_card_comp_defs_vl|PAY_DIR_CARD_COMP_DEFS_VL]] — 18 atributos (5 BICC)
- [[pay_dir_card_definitions_vl|PAY_DIR_CARD_DEFINITIONS_VL]] — 13 atributos (4 BICC)
- [[pay_pay_relationships_dn|PAY_PAY_RELATIONSHIPS_DN]] — 11 atributos

---

## ⚙️ Atributos

### [[pay_dir_cards_f|PAY_DIR_CARDS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DIRCardDPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | DIRCardDPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | DIRCardDPEOCreatorType | CREATOR_TYPE | — | — |
| 4 | DIRCardDPEODirCardDefinitionId | DIR_CARD_DEFINITION_ID | — | — |
| 5 | DIRCardDPEODirCardId | DIR_CARD_ID | 🔑 | ✅ |
| 6 | DIRCardDPEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 7 | DIRCardDPEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 8 | DIRCardDPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | DIRCardDPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | DIRCardDPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | DIRCardDPEOLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | — |
| 12 | DIRCardDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | DIRCardDPEOPayrollRelationshipId | PAYROLL_RELATIONSHIP_ID | — | — |
| 14 | DIRCardDPEOSourceId | SOURCE_ID | — | — |
| 15 | DIRCardDPEOSourceType | SOURCE_TYPE | — | — |
| 16 | DIRCardDPEOStatus | STATUS | — | — |

### [[pay_dir_card_components_f|PAY_DIR_CARD_COMPONENTS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DIRCardComponentDPEOContext1 | CONTEXT_VALUE1 | — | — |
| 2 | DIRCardComponentDPEOContext2 | CONTEXT_VALUE2 | — | — |
| 3 | DIRCardComponentDPEOContext3 | CONTEXT_VALUE3 | — | — |
| 4 | DIRCardComponentDPEOContext4 | CONTEXT_VALUE4 | — | — |
| 5 | DIRCardComponentDPEOContext5 | CONTEXT_VALUE5 | — | — |
| 6 | DIRCardComponentDPEOContext6 | CONTEXT_VALUE6 | — | — |
| 7 | DIRCardComponentDPEOCreatedBy | CREATED_BY | — | ✅ |
| 8 | DIRCardComponentDPEOCreationDate | CREATION_DATE | — | ✅ |
| 9 | DIRCardComponentDPEODeductionGroupId | DEDUCTION_GROUP_ID | — | — |
| 10 | DIRCardComponentDPEODirCardCompDefId | DIR_CARD_COMP_DEF_ID | — | — |
| 11 | DIRCardComponentDPEODirCardCompId | DIR_CARD_COMP_ID | 🔑 | ✅ |
| 12 | DIRCardComponentDPEODirCardId | DIR_CARD_ID | — | — |
| 13 | DIRCardComponentDPEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 14 | DIRCardComponentDPEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 15 | DIRCardComponentDPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | DIRCardComponentDPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 17 | DIRCardComponentDPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 18 | DIRCardComponentDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 19 | DIRCardComponentDPEOParentDirCardCompId | PARENT_DIR_CARD_COMP_ID | — | ✅ |
| 20 | DIRCardComponentDPEOSubpriority | SUBPRIORITY | — | ✅ |

### [[pay_dir_card_comp_defs_vl|PAY_DIR_CARD_COMP_DEFS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DIRCardCompDefPEOAssociableTerm | ASSOCIABLE_TERM | — | — |
| 2 | DIRCardCompDefPEOAssociableTru | ASSOCIABLE_TRU | — | — |
| 3 | DIRCardCompDefPEOBaseComponentName | BASE_COMPONENT_NAME | — | ✅ |
| 4 | DIRCardCompDefPEOBreakdownComponentFlag | BREAKDOWN_COMPONENT_FLAG | — | — |
| 5 | DIRCardCompDefPEOComponentName | COMPONENT_NAME | — | ✅ |
| 6 | DIRCardCompDefPEODeductionGroupId | DEDUCTION_GROUP_ID | — | — |
| 7 | DIRCardCompDefPEODeductionTypeId | DEDUCTION_TYPE_ID | — | — |
| 8 | DIRCardCompDefPEODefaultingTruCompFlag | DEFAULTING_TRU_COMP_FLAG | — | — |
| 9 | DIRCardCompDefPEODirCardDefinitionId | DIR_CARD_DEFINITION_ID | — | — |
| 10 | DIRCardCompDefPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 11 | DIRCardCompDefPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 12 | DIRCardCompDefPEOElementTypeId | ELEMENT_TYPE_ID | — | — |
| 13 | DIRCardCompDefPEOLegislationCode | LEGISLATION_CODE | — | — |
| 14 | DIRCardCompDefPEOLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | — |
| 15 | DIRCardCompDefPEOMultipleAllowed | MULTIPLE_ALLOWED | — | — |
| 16 | DIRCardCompDefPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | DIRCardCompDefPEORequired | REQUIRED | — | — |
| 18 | DirCardCompDefId | DIR_CARD_COMP_DEF_ID | — | ✅ |

### [[pay_dir_card_definitions_vl|PAY_DIR_CARD_DEFINITIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DIRCardDefinitionPEOAssociableTerm | ASSOCIABLE_TERM | — | — |
| 2 | DIRCardDefinitionPEOAssociableTru | ASSOCIABLE_TRU | — | — |
| 3 | DIRCardDefinitionPEOAutoGenerate | AUTO_GENERATE | — | — |
| 4 | DIRCardDefinitionPEOBaseDisplayName | BASE_DISPLAY_NAME | — | ✅ |
| 5 | DIRCardDefinitionPEOBreakdownComponentFlag | BREAKDOWN_COMPONENT_FLAG | — | — |
| 6 | DIRCardDefinitionPEODateMode | DATE_MODE | — | — |
| 7 | DIRCardDefinitionPEODefaultingTruFlag | DEFAULTING_TRU_FLAG | — | — |
| 8 | DIRCardDefinitionPEODescription | DESCRIPTION | — | ✅ |
| 9 | DIRCardDefinitionPEODirCardDefinitionId | DIR_CARD_DEFINITION_ID | — | ✅ |
| 10 | DIRCardDefinitionPEODisplayName | DISPLAY_NAME | — | ✅ |
| 11 | DIRCardDefinitionPEOLegislationCode | LEGISLATION_CODE | — | — |
| 12 | DIRCardDefinitionPEOLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | — |
| 13 | DIRCardDefinitionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[pay_pay_relationships_dn|PAY_PAY_RELATIONSHIPS_DN]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayrollRelationshipPEOCreatedBy | CREATED_BY | — | — |
| 2 | PayrollRelationshipPEOCreationDate | CREATION_DATE | — | — |
| 3 | PayrollRelationshipPEOEndDate | END_DATE | — | — |
| 4 | PayrollRelationshipPEOLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | — |
| 5 | PayrollRelationshipPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 6 | PayrollRelationshipPEOPayrollRelationshipId | PAYROLL_RELATIONSHIP_ID | — | — |
| 7 | PayrollRelationshipPEOPayrollRelationshipNumber | PAYROLL_RELATIONSHIP_NUMBER | — | — |
| 8 | PayrollRelationshipPEOPayrollStatUnitId | PAYROLL_STAT_UNIT_ID | — | — |
| 9 | PayrollRelationshipPEOPersonId | PERSON_ID | — | — |
| 10 | PayrollRelationshipPEORelationshipTypeId | RELATIONSHIP_TYPE_ID | — | — |
| 11 | PayrollRelationshipPEOStartDate | START_DATE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
