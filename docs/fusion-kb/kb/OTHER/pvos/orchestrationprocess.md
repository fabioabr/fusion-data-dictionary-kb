---
id: DOC-OTHER-PVO-OrchestrationProcess
doc_type: system-doc
title: "OrchestrationProcess — PVO Cross-Module"
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
  - OrchestrationProcess
  - orchestrationprocess
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# OrchestrationProcess

## 📌 Visão Geral

View Object para extração BICC de dados de Orchestration Process. Acessa as tabelas: DOO_PROCESS_CLASSES_B, DOO_PROCESS_CLASSES_TL, DOO_PROCESS_DEFINITIONS_B (+1).

**Caminho:** `FscmTopModelAM.DooTopAM.OrchestrationProcess`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 59 | 4 | 3 | 19 | 32% |

---

## 🔗 Tabelas Relacionadas

- [[doo_process_classes_b|DOO_PROCESS_CLASSES_B]] — 7 atributos (2 BICC)
- [[doo_process_classes_tl|DOO_PROCESS_CLASSES_TL]] — 11 atributos (1 PKs, 3 BICC)
- [[doo_process_definitions_b|DOO_PROCESS_DEFINITIONS_B]] — 29 atributos (1 PKs, 11 BICC)
- [[doo_process_definitions_tl|DOO_PROCESS_DEFINITIONS_TL]] — 12 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[doo_process_classes_b|DOO_PROCESS_CLASSES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrchProcClassCreationDate | CREATION_DATE | — | ✅ |
| 2 | OrchProcClassLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 3 | OrchProcClassLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 4 | OrchProcClassLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 5 | OrchProcClassObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 6 | OrchProcClassOrchProcClassCreatedBy | CREATED_BY | — | — |
| 7 | OrchProcClassProcessClassId | PROCESS_CLASS_ID | — | — |

### [[doo_process_classes_tl|DOO_PROCESS_CLASSES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrchProcClassTranslationCreatedBy | CREATED_BY | — | — |
| 2 | OrchProcClassTranslationCreationDate | CREATION_DATE | — | — |
| 3 | OrchProcClassTranslationDescription | DESCRIPTION | — | — |
| 4 | OrchProcClassTranslationLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | OrchProcClassTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | OrchProcClassTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | OrchProcClassTranslationLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | OrchProcClassTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | OrchProcClassTranslationProcessClassId | PROCESS_CLASS_ID | — | — |
| 10 | OrchProcClassTranslationProcessClassName | PROCESS_CLASS_NAME | — | ✅ |
| 11 | OrchProcClassTranslationSourceLang | SOURCE_LANG | — | — |

### [[doo_process_definitions_b|DOO_PROCESS_DEFINITIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProcessDefinitionChangeManagementMode | CHANGE_MANAGEMENT_MODE | — | — |
| 2 | ProcessDefinitionCompositeNameSpace | COMPOSITE_NAME_SPACE | — | — |
| 3 | ProcessDefinitionCostOfChangeRlsId | COST_OF_CHANGE_RLS_ID | — | — |
| 4 | ProcessDefinitionCostOfChangeRlsName | COST_OF_CHANGE_RLS_NAME | — | — |
| 5 | ProcessDefinitionCreatedBy | CREATED_BY | — | ✅ |
| 6 | ProcessDefinitionCreationDate | CREATION_DATE | — | ✅ |
| 7 | ProcessDefinitionDeployedBpelVersion | DEPLOYED_BPEL_VERSION | — | — |
| 8 | ProcessDefinitionDooProcessId | DOO_PROCESS_ID | 🔑 | ✅ |
| 9 | ProcessDefinitionDooProcessVersion | DOO_PROCESS_VERSION | — | — |
| 10 | ProcessDefinitionEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 11 | ProcessDefinitionEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 12 | ProcessDefinitionEssFlag | ESS_FLAG | — | — |
| 13 | ProcessDefinitionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | ProcessDefinitionLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | ProcessDefinitionLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | ProcessDefinitionMainProcessFlag | MAIN_PROCESS_FLAG | — | ✅ |
| 17 | ProcessDefinitionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | ProcessDefinitionOrchestrationApplicationId | ORCHESTRATION_APPLICATION_ID | — | ✅ |
| 19 | ProcessDefinitionProcessClassId | PROCESS_CLASS_ID | — | — |
| 20 | ProcessDefinitionProcessImage | PROCESS_IMAGE | — | — |
| 21 | ProcessDefinitionProcessName | PROCESS_NAME | — | ✅ |
| 22 | ProcessDefinitionProcessReleaseStatusCode | PROCESS_RELEASE_STATUS_CODE | — | ✅ |
| 23 | ProcessDefinitionProcessWsdlUri | PROCESS_WSDL_URI | — | — |
| 24 | ProcessDefinitionReplanFlag | REPLAN_FLAG | — | — |
| 25 | ProcessDefinitionRuleDictionaryId | RULE_DICTIONARY_ID | — | — |
| 26 | ProcessDefinitionSetId | SET_ID | — | — |
| 27 | ProcessDefinitionStatusCatalogId | STATUS_CATALOG_ID | — | — |
| 28 | ProcessDefinitionUseDynamicAttrInDeltaComp | USE_DYNAMIC_ATTR_IN_DELTA_COMP | — | — |
| 29 | ProcessDefinitionUseFlexAttrInDeltaComp | USE_FLEX_ATTR_IN_DELTA_COMP | — | — |

### [[doo_process_definitions_tl|DOO_PROCESS_DEFINITIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProcessDefinitionTranslationCreatedBy | CREATED_BY | — | — |
| 2 | ProcessDefinitionTranslationCreationDate | CREATION_DATE | — | — |
| 3 | ProcessDefinitionTranslationDescription | DESCRIPTION | — | ✅ |
| 4 | ProcessDefinitionTranslationDooProcessId | DOO_PROCESS_ID | — | — |
| 5 | ProcessDefinitionTranslationDooProcessVersion | DOO_PROCESS_VERSION | — | — |
| 6 | ProcessDefinitionTranslationLanguage | LANGUAGE | 🔑 | ✅ |
| 7 | ProcessDefinitionTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ProcessDefinitionTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ProcessDefinitionTranslationLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ProcessDefinitionTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | ProcessDefinitionTranslationProcessDisplayName | PROCESS_DISPLAY_NAME | — | — |
| 12 | ProcessDefinitionTranslationSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
