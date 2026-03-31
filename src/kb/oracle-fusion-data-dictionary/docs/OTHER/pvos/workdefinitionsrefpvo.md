---
id: DOC-OTHER-PVO-WorkDefinitionsRefPVO
doc_type: system-doc
title: "WorkDefinitionsRefPVO — PVO Cross-Module"
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
  - WorkDefinitionsRefPVO
  - workdefinitionsrefpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WorkDefinitionsRefPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Work Definitions Ref. Acessa as tabelas: WIS_WD_VERSIONS, WIS_WORK_DEFINITIONS, WIS_WORK_DEFINITION_NAMES_VL (+1).

**Caminho:** `FscmTopModelAM.WorkOrderAM.WorkDefinitionsRefPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 226 | 4 | 1 | 30 | 13% |

---

## 🔗 Tabelas Relacionadas

- [[wis_wd_versions|WIS_WD_VERSIONS]] — 57 atributos (2 BICC)
- [[wis_work_definitions|WIS_WORK_DEFINITIONS]] — 65 atributos (1 PKs, 23 BICC)
- [[wis_work_definition_names_vl|WIS_WORK_DEFINITION_NAMES_VL]] — 54 atributos (4 BICC)
- [[wis_work_methods_vl|WIS_WORK_METHODS_VL]] — 50 atributos (1 BICC)

---

## ⚙️ Atributos

### [[wis_wd_versions|WIS_WD_VERSIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WDVersionPEOApprovalStatusCode | APPROVAL_STATUS_CODE | — | — |
| 2 | WDVersionPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 3 | WDVersionPEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 4 | WDVersionPEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 5 | WDVersionPEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 6 | WDVersionPEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 7 | WDVersionPEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 8 | WDVersionPEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 9 | WDVersionPEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 10 | WDVersionPEOAttributeChar16 | ATTRIBUTE_CHAR16 | — | — |
| 11 | WDVersionPEOAttributeChar17 | ATTRIBUTE_CHAR17 | — | — |
| 12 | WDVersionPEOAttributeChar18 | ATTRIBUTE_CHAR18 | — | — |
| 13 | WDVersionPEOAttributeChar19 | ATTRIBUTE_CHAR19 | — | — |
| 14 | WDVersionPEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 15 | WDVersionPEOAttributeChar20 | ATTRIBUTE_CHAR20 | — | — |
| 16 | WDVersionPEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 17 | WDVersionPEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 18 | WDVersionPEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 19 | WDVersionPEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 20 | WDVersionPEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 21 | WDVersionPEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 22 | WDVersionPEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 23 | WDVersionPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 24 | WDVersionPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 25 | WDVersionPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 26 | WDVersionPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 27 | WDVersionPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 28 | WDVersionPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 29 | WDVersionPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 30 | WDVersionPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 31 | WDVersionPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 32 | WDVersionPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 33 | WDVersionPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 34 | WDVersionPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 35 | WDVersionPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 36 | WDVersionPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 37 | WDVersionPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 38 | WDVersionPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 39 | WDVersionPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 40 | WDVersionPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 41 | WDVersionPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 42 | WDVersionPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 43 | WDVersionPEOCompletionLocatorId | COMPLETION_LOCATOR_ID | — | — |
| 44 | WDVersionPEOCompletionSubinventoryName | COMPLETION_SUBINVENTORY_NAME | — | — |
| 45 | WDVersionPEOCostingBatchOutputSize | COSTING_BATCH_OUTPUT_SIZE | — | — |
| 46 | WDVersionPEOCreatedBy | CREATED_BY | — | — |
| 47 | WDVersionPEOCreationDate | CREATION_DATE | — | — |
| 48 | WDVersionPEOEffectiveFromDate | EFFECTIVE_FROM_DATE | — | — |
| 49 | WDVersionPEOEffectiveToDate | EFFECTIVE_TO_DATE | — | — |
| 50 | WDVersionPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 51 | WDVersionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 52 | WDVersionPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 53 | WDVersionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 54 | WDVersionPEOOrganizationId | ORGANIZATION_ID | — | — |
| 55 | WDVersionPEOVersionNumber | VERSION_NUMBER | — | ✅ |
| 56 | WDVersionPEOWorkDefinitionId | WORK_DEFINITION_ID | — | — |
| 57 | WDVersionPEOWorkDefinitionVersionId | WORK_DEFINITION_VERSION_ID | — | ✅ |

### [[wis_work_definitions|WIS_WORK_DEFINITIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkDefinitionPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 2 | WorkDefinitionPEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 3 | WorkDefinitionPEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 4 | WorkDefinitionPEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 5 | WorkDefinitionPEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 6 | WorkDefinitionPEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 7 | WorkDefinitionPEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 8 | WorkDefinitionPEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 9 | WorkDefinitionPEOAttributeChar16 | ATTRIBUTE_CHAR16 | — | — |
| 10 | WorkDefinitionPEOAttributeChar17 | ATTRIBUTE_CHAR17 | — | — |
| 11 | WorkDefinitionPEOAttributeChar18 | ATTRIBUTE_CHAR18 | — | — |
| 12 | WorkDefinitionPEOAttributeChar19 | ATTRIBUTE_CHAR19 | — | — |
| 13 | WorkDefinitionPEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 14 | WorkDefinitionPEOAttributeChar20 | ATTRIBUTE_CHAR20 | — | — |
| 15 | WorkDefinitionPEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 16 | WorkDefinitionPEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 17 | WorkDefinitionPEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 18 | WorkDefinitionPEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 19 | WorkDefinitionPEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 20 | WorkDefinitionPEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 21 | WorkDefinitionPEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 22 | WorkDefinitionPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 23 | WorkDefinitionPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 24 | WorkDefinitionPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 25 | WorkDefinitionPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 26 | WorkDefinitionPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 27 | WorkDefinitionPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 28 | WorkDefinitionPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 29 | WorkDefinitionPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 30 | WorkDefinitionPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 31 | WorkDefinitionPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 32 | WorkDefinitionPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 33 | WorkDefinitionPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 34 | WorkDefinitionPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 35 | WorkDefinitionPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 36 | WorkDefinitionPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 37 | WorkDefinitionPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 38 | WorkDefinitionPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 39 | WorkDefinitionPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 40 | WorkDefinitionPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 41 | WorkDefinitionPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 42 | WorkDefinitionPEOBillSequenceId | BILL_SEQUENCE_ID | — | ✅ |
| 43 | WorkDefinitionPEOCostingPriority | COSTING_PRIORITY | — | ✅ |
| 44 | WorkDefinitionPEOCreatedBy | CREATED_BY | — | ✅ |
| 45 | WorkDefinitionPEOCreationDate | CREATION_DATE | — | ✅ |
| 46 | WorkDefinitionPEOInactiveDate | INACTIVE_DATE | — | ✅ |
| 47 | WorkDefinitionPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 48 | WorkDefinitionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 49 | WorkDefinitionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 50 | WorkDefinitionPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 51 | WorkDefinitionPEOMinimumTransferQuantity | MINIMUM_TRANSFER_QUANTITY | — | — |
| 52 | WorkDefinitionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 53 | WorkDefinitionPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 54 | WorkDefinitionPEOProductionPriority | PRODUCTION_PRIORITY | — | ✅ |
| 55 | WorkDefinitionPEOQuantity | QUANTITY | — | ✅ |
| 56 | WorkDefinitionPEOSerialTrackingFlag | SERIAL_TRACKING_FLAG | — | ✅ |
| 57 | WorkDefinitionPEOStatusCode | STATUS_CODE | — | ✅ |
| 58 | WorkDefinitionPEOSystemGeneratedFlag | SYSTEM_GENERATED_FLAG | — | ✅ |
| 59 | WorkDefinitionPEOUomCode | UOM_CODE | — | ✅ |
| 60 | WorkDefinitionPEOWdMntNameId | WD_MNT_NAME_ID | — | ✅ |
| 61 | WorkDefinitionPEOWorkDefinitionHeaderName | WORK_DEFINITION_HEADER_NAME | — | ✅ |
| 62 | WorkDefinitionPEOWorkDefinitionId | WORK_DEFINITION_ID | 🔑 | ✅ |
| 63 | WorkDefinitionPEOWorkDefinitionNameId | WORK_DEFINITION_NAME_ID | — | ✅ |
| 64 | WorkDefinitionPEOWorkDefinitionType | WORK_DEFINITION_TYPE | — | ✅ |
| 65 | WorkDefinitionPEOWorkMethodId | WORK_METHOD_ID | — | ✅ |

### [[wis_work_definition_names_vl|WIS_WORK_DEFINITION_NAMES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkDefinitionNamePEOAttributeCategory1 | ATTRIBUTE_CATEGORY | — | — |
| 2 | WorkDefinitionNamePEOAttributeChar101 | ATTRIBUTE_CHAR10 | — | — |
| 3 | WorkDefinitionNamePEOAttributeChar111 | ATTRIBUTE_CHAR11 | — | — |
| 4 | WorkDefinitionNamePEOAttributeChar121 | ATTRIBUTE_CHAR12 | — | — |
| 5 | WorkDefinitionNamePEOAttributeChar131 | ATTRIBUTE_CHAR13 | — | — |
| 6 | WorkDefinitionNamePEOAttributeChar141 | ATTRIBUTE_CHAR14 | — | — |
| 7 | WorkDefinitionNamePEOAttributeChar151 | ATTRIBUTE_CHAR15 | — | — |
| 8 | WorkDefinitionNamePEOAttributeChar161 | ATTRIBUTE_CHAR16 | — | — |
| 9 | WorkDefinitionNamePEOAttributeChar171 | ATTRIBUTE_CHAR17 | — | — |
| 10 | WorkDefinitionNamePEOAttributeChar181 | ATTRIBUTE_CHAR18 | — | — |
| 11 | WorkDefinitionNamePEOAttributeChar191 | ATTRIBUTE_CHAR19 | — | — |
| 12 | WorkDefinitionNamePEOAttributeChar201 | ATTRIBUTE_CHAR20 | — | — |
| 13 | WorkDefinitionNamePEOAttributeChar31 | ATTRIBUTE_CHAR3 | — | — |
| 14 | WorkDefinitionNamePEOAttributeChar41 | ATTRIBUTE_CHAR4 | — | — |
| 15 | WorkDefinitionNamePEOAttributeChar51 | ATTRIBUTE_CHAR5 | — | — |
| 16 | WorkDefinitionNamePEOAttributeChar61 | ATTRIBUTE_CHAR6 | — | — |
| 17 | WorkDefinitionNamePEOAttributeChar71 | ATTRIBUTE_CHAR7 | — | — |
| 18 | WorkDefinitionNamePEOAttributeChar81 | ATTRIBUTE_CHAR8 | — | — |
| 19 | WorkDefinitionNamePEOAttributeChar91 | ATTRIBUTE_CHAR9 | — | — |
| 20 | WorkDefinitionNamePEOAttributeDate11 | ATTRIBUTE_DATE1 | — | — |
| 21 | WorkDefinitionNamePEOAttributeDate21 | ATTRIBUTE_DATE2 | — | — |
| 22 | WorkDefinitionNamePEOAttributeDate31 | ATTRIBUTE_DATE3 | — | — |
| 23 | WorkDefinitionNamePEOAttributeDate41 | ATTRIBUTE_DATE4 | — | — |
| 24 | WorkDefinitionNamePEOAttributeDate51 | ATTRIBUTE_DATE5 | — | — |
| 25 | WorkDefinitionNamePEOAttributeNumber101 | ATTRIBUTE_NUMBER10 | — | — |
| 26 | WorkDefinitionNamePEOAttributeNumber11 | ATTRIBUTE_NUMBER1 | — | — |
| 27 | WorkDefinitionNamePEOAttributeNumber21 | ATTRIBUTE_NUMBER2 | — | — |
| 28 | WorkDefinitionNamePEOAttributeNumber31 | ATTRIBUTE_NUMBER3 | — | — |
| 29 | WorkDefinitionNamePEOAttributeNumber41 | ATTRIBUTE_NUMBER4 | — | — |
| 30 | WorkDefinitionNamePEOAttributeNumber51 | ATTRIBUTE_NUMBER5 | — | — |
| 31 | WorkDefinitionNamePEOAttributeNumber61 | ATTRIBUTE_NUMBER6 | — | — |
| 32 | WorkDefinitionNamePEOAttributeNumber71 | ATTRIBUTE_NUMBER7 | — | — |
| 33 | WorkDefinitionNamePEOAttributeNumber81 | ATTRIBUTE_NUMBER8 | — | — |
| 34 | WorkDefinitionNamePEOAttributeNumber91 | ATTRIBUTE_NUMBER9 | — | — |
| 35 | WorkDefinitionNamePEOAttributeTimestamp11 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 36 | WorkDefinitionNamePEOAttributeTimestamp21 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 37 | WorkDefinitionNamePEOAttributeTimestamp31 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 38 | WorkDefinitionNamePEOAttributeTimestamp41 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 39 | WorkDefinitionNamePEOAttributeTimestamp51 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 40 | WorkDefinitionNamePEOCreatedBy1 | CREATED_BY | — | — |
| 41 | WorkDefinitionNamePEOCreationDate1 | CREATION_DATE | — | — |
| 42 | WorkDefinitionNamePEOEffectiveFromDate | EFFECTIVE_FROM_DATE | — | — |
| 43 | WorkDefinitionNamePEOEffectiveToDate | EFFECTIVE_TO_DATE | — | — |
| 44 | WorkDefinitionNamePEOLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 45 | WorkDefinitionNamePEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 46 | WorkDefinitionNamePEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 47 | WorkDefinitionNamePEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 48 | WorkDefinitionNamePEOSeededFlag | SEEDED_FLAG | — | — |
| 49 | WorkDefinitionNamePEOUsedInPlanningFlag | USED_IN_PLANNING_FLAG | — | — |
| 50 | WorkDefinitionNamePEOWorkDefName | WORK_DEF_NAME | — | ✅ |
| 51 | WorkDefinitionNamePEOWorkDefNameDescription | WORK_DEF_NAME_DESCRIPTION | — | ✅ |
| 52 | WorkDefinitionNamePEOWorkDefinitionCode | WORK_DEFINITION_CODE | — | ✅ |
| 53 | WorkDefinitionNamePEOWorkDefinitionNameId1 | WORK_DEFINITION_NAME_ID | — | — |
| 54 | WorkDefinitionNamePEOWorkDefinitionType1 | WORK_DEFINITION_TYPE | — | — |

### [[wis_work_methods_vl|WIS_WORK_METHODS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkMethodPEOAttributeCategory2 | ATTRIBUTE_CATEGORY | — | — |
| 2 | WorkMethodPEOAttributeChar102 | ATTRIBUTE_CHAR10 | — | — |
| 3 | WorkMethodPEOAttributeChar113 | ATTRIBUTE_CHAR11 | — | — |
| 4 | WorkMethodPEOAttributeChar122 | ATTRIBUTE_CHAR12 | — | — |
| 5 | WorkMethodPEOAttributeChar132 | ATTRIBUTE_CHAR13 | — | — |
| 6 | WorkMethodPEOAttributeChar142 | ATTRIBUTE_CHAR14 | — | — |
| 7 | WorkMethodPEOAttributeChar152 | ATTRIBUTE_CHAR15 | — | — |
| 8 | WorkMethodPEOAttributeChar162 | ATTRIBUTE_CHAR16 | — | — |
| 9 | WorkMethodPEOAttributeChar172 | ATTRIBUTE_CHAR17 | — | — |
| 10 | WorkMethodPEOAttributeChar182 | ATTRIBUTE_CHAR18 | — | — |
| 11 | WorkMethodPEOAttributeChar192 | ATTRIBUTE_CHAR19 | — | — |
| 12 | WorkMethodPEOAttributeChar202 | ATTRIBUTE_CHAR20 | — | — |
| 13 | WorkMethodPEOAttributeChar22 | ATTRIBUTE_CHAR2 | — | — |
| 14 | WorkMethodPEOAttributeChar32 | ATTRIBUTE_CHAR3 | — | — |
| 15 | WorkMethodPEOAttributeChar42 | ATTRIBUTE_CHAR4 | — | — |
| 16 | WorkMethodPEOAttributeChar52 | ATTRIBUTE_CHAR5 | — | — |
| 17 | WorkMethodPEOAttributeChar62 | ATTRIBUTE_CHAR6 | — | — |
| 18 | WorkMethodPEOAttributeChar72 | ATTRIBUTE_CHAR7 | — | — |
| 19 | WorkMethodPEOAttributeChar82 | ATTRIBUTE_CHAR8 | — | — |
| 20 | WorkMethodPEOAttributeChar92 | ATTRIBUTE_CHAR9 | — | — |
| 21 | WorkMethodPEOAttributeDate12 | ATTRIBUTE_DATE1 | — | — |
| 22 | WorkMethodPEOAttributeDate22 | ATTRIBUTE_DATE2 | — | — |
| 23 | WorkMethodPEOAttributeDate32 | ATTRIBUTE_DATE3 | — | — |
| 24 | WorkMethodPEOAttributeDate42 | ATTRIBUTE_DATE4 | — | — |
| 25 | WorkMethodPEOAttributeDate52 | ATTRIBUTE_DATE5 | — | — |
| 26 | WorkMethodPEOAttributeNumber102 | ATTRIBUTE_NUMBER10 | — | — |
| 27 | WorkMethodPEOAttributeNumber12 | ATTRIBUTE_NUMBER1 | — | — |
| 28 | WorkMethodPEOAttributeNumber22 | ATTRIBUTE_NUMBER2 | — | — |
| 29 | WorkMethodPEOAttributeNumber32 | ATTRIBUTE_NUMBER3 | — | — |
| 30 | WorkMethodPEOAttributeNumber42 | ATTRIBUTE_NUMBER4 | — | — |
| 31 | WorkMethodPEOAttributeNumber52 | ATTRIBUTE_NUMBER5 | — | — |
| 32 | WorkMethodPEOAttributeNumber62 | ATTRIBUTE_NUMBER6 | — | — |
| 33 | WorkMethodPEOAttributeNumber72 | ATTRIBUTE_NUMBER7 | — | — |
| 34 | WorkMethodPEOAttributeNumber82 | ATTRIBUTE_NUMBER8 | — | — |
| 35 | WorkMethodPEOAttributeNumber92 | ATTRIBUTE_NUMBER9 | — | — |
| 36 | WorkMethodPEOAttributeTimestamp12 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 37 | WorkMethodPEOAttributeTimestamp22 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 38 | WorkMethodPEOAttributeTimestamp32 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 39 | WorkMethodPEOAttributeTimestamp42 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 40 | WorkMethodPEOAttributeTimestamp52 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 41 | WorkMethodPEOCreatedBy2 | CREATED_BY | — | — |
| 42 | WorkMethodPEOCreationDate2 | CREATION_DATE | — | — |
| 43 | WorkMethodPEOLastUpdateDate2 | LAST_UPDATE_DATE | — | ✅ |
| 44 | WorkMethodPEOLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 45 | WorkMethodPEOLastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 46 | WorkMethodPEOObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 47 | WorkMethodPEOWorkMethodCode | WORK_METHOD_CODE | — | — |
| 48 | WorkMethodPEOWorkMethodDescription | WORK_METHOD_DESCRIPTION | — | — |
| 49 | WorkMethodPEOWorkMethodId1 | WORK_METHOD_ID | — | — |
| 50 | WorkMethodPEOWorkMethodName | WORK_METHOD_NAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
