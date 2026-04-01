---
id: DOC-OTHER-PVO-WDOperationExtractPVO
doc_type: system-doc
title: "WDOperationExtractPVO — PVO Cross-Module"
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
  - WDOperationExtractPVO
  - wdoperationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WDOperationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de WDOperation Extract. Acessa as tabelas: WIS_WD_OPERATIONS_B, WIS_WD_OPERATIONS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.WisBiccExtractAM.WDOperationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 83 | 2 | 3 | 83 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[wis_wd_operations_b|WIS_WD_OPERATIONS_B]] — 72 atributos (1 PKs, 72 BICC)
- [[wis_wd_operations_tl|WIS_WD_OPERATIONS_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[wis_wd_operations_b|WIS_WD_OPERATIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionStatusCode | ACTION_STATUS_CODE | — | ✅ |
| 2 | ApplicabilityRuleId | APPLICABILITY_RULE_ID | — | ✅ |
| 3 | AttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 4 | AttributeChar1 | ATTRIBUTE_CHAR1 | — | ✅ |
| 5 | AttributeChar10 | ATTRIBUTE_CHAR10 | — | ✅ |
| 6 | AttributeChar11 | ATTRIBUTE_CHAR11 | — | ✅ |
| 7 | AttributeChar12 | ATTRIBUTE_CHAR12 | — | ✅ |
| 8 | AttributeChar13 | ATTRIBUTE_CHAR13 | — | ✅ |
| 9 | AttributeChar14 | ATTRIBUTE_CHAR14 | — | ✅ |
| 10 | AttributeChar15 | ATTRIBUTE_CHAR15 | — | ✅ |
| 11 | AttributeChar16 | ATTRIBUTE_CHAR16 | — | ✅ |
| 12 | AttributeChar17 | ATTRIBUTE_CHAR17 | — | ✅ |
| 13 | AttributeChar18 | ATTRIBUTE_CHAR18 | — | ✅ |
| 14 | AttributeChar19 | ATTRIBUTE_CHAR19 | — | ✅ |
| 15 | AttributeChar2 | ATTRIBUTE_CHAR2 | — | ✅ |
| 16 | AttributeChar20 | ATTRIBUTE_CHAR20 | — | ✅ |
| 17 | AttributeChar3 | ATTRIBUTE_CHAR3 | — | ✅ |
| 18 | AttributeChar4 | ATTRIBUTE_CHAR4 | — | ✅ |
| 19 | AttributeChar5 | ATTRIBUTE_CHAR5 | — | ✅ |
| 20 | AttributeChar6 | ATTRIBUTE_CHAR6 | — | ✅ |
| 21 | AttributeChar7 | ATTRIBUTE_CHAR7 | — | ✅ |
| 22 | AttributeChar8 | ATTRIBUTE_CHAR8 | — | ✅ |
| 23 | AttributeChar9 | ATTRIBUTE_CHAR9 | — | ✅ |
| 24 | AttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 25 | AttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 26 | AttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 27 | AttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 28 | AttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 29 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 30 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 31 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 32 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 33 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 34 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 35 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 36 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 37 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 38 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 39 | AttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 40 | AttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 41 | AttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 42 | AttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 43 | AttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 44 | AutoTransactFlag | AUTO_TRANSACT_FLAG | — | ✅ |
| 45 | CountPointFlag | COUNT_POINT_FLAG | — | ✅ |
| 46 | CreatedBy | CREATED_BY | — | ✅ |
| 47 | CreationDate | CREATION_DATE | — | ✅ |
| 48 | EffectiveFromDate | EFFECTIVE_FROM_DATE | — | ✅ |
| 49 | EffectiveToDate | EFFECTIVE_TO_DATE | — | ✅ |
| 50 | FixedLeadTime | FIXED_LEAD_TIME | — | ✅ |
| 51 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 52 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 53 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 54 | LeadTimeUom | LEAD_TIME_UOM | — | ✅ |
| 55 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 56 | OperationSeqNumber | OPERATION_SEQ_NUMBER | — | ✅ |
| 57 | OperationType | OPERATION_TYPE | — | ✅ |
| 58 | OptionDependentFlag | OPTION_DEPENDENT_FLAG | — | ✅ |
| 59 | OspItemId | OSP_ITEM_ID | — | ✅ |
| 60 | PlanningPercent | PLANNING_PERCENT | — | ✅ |
| 61 | ReferencedFlag | REFERENCED_FLAG | — | ✅ |
| 62 | ResequenceFlag | RESEQUENCE_FLAG | — | ✅ |
| 63 | SerialTrackingFlag | SERIAL_TRACKING_FLAG | — | ✅ |
| 64 | ShippingDocumentsFlag | SHIPPING_DOCUMENTS_FLAG | — | ✅ |
| 65 | StandardOperationId | STANDARD_OPERATION_ID | — | ✅ |
| 66 | SupplierId | SUPPLIER_ID | — | ✅ |
| 67 | SupplierSiteId | SUPPLIER_SITE_ID | — | ✅ |
| 68 | VariableLeadTime | VARIABLE_LEAD_TIME | — | ✅ |
| 69 | WDOperationPEOYieldFactor | OP_YIELD_FACTOR | — | ✅ |
| 70 | WdOperationId | WD_OPERATION_ID | 🔑 | ✅ |
| 71 | WorkCenterId | WORK_CENTER_ID | — | ✅ |
| 72 | WorkDefinitionId | WORK_DEFINITION_ID | — | ✅ |

### [[wis_wd_operations_tl|WIS_WD_OPERATIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WDOperationTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | WDOperationTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | WDOperationTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 4 | WDOperationTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | WDOperationTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | WDOperationTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | WDOperationTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | WDOperationTranslationPEOOperationDescription | OPERATION_DESCRIPTION | — | ✅ |
| 9 | WDOperationTranslationPEOOperationName | OPERATION_NAME | — | ✅ |
| 10 | WDOperationTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |
| 11 | WDOperationTranslationPEOWdOperationId | WD_OPERATION_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
