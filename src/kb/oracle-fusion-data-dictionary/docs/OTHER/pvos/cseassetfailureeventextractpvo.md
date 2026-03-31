---
id: DOC-OTHER-PVO-CseAssetFailureEventExtractPVO
doc_type: system-doc
title: "CseAssetFailureEventExtractPVO — PVO Cross-Module"
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
  - CseAssetFailureEventExtractPVO
  - cseassetfailureeventextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CseAssetFailureEventExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cse Asset Failure Event Extract. Acessa as tabelas: CSE_FAILURE_EVENTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CseBiccExtractAM.CseAssetFailureEventExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 65 | 1 | 1 | 65 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cse_failure_events|CSE_FAILURE_EVENTS]] — 65 atributos (1 PKs, 65 BICC)

---

## ⚙️ Atributos

### [[cse_failure_events|CSE_FAILURE_EVENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssetDownFlag | ASSET_DOWN_FLAG | — | ✅ |
| 2 | AssetId | ASSET_ID | — | ✅ |
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
| 44 | AvailableDate | AVAILABLE_DATE | — | ✅ |
| 45 | CreatedBy | CREATED_BY | — | ✅ |
| 46 | CreationDate | CREATION_DATE | — | ✅ |
| 47 | FailureDate | FAILURE_DATE | — | ✅ |
| 48 | FailureEventId | FAILURE_EVENT_ID | 🔑 | ✅ |
| 49 | FailureFlag | FAILURE_FLAG | — | ✅ |
| 50 | FailureSetId | FAILURE_SET_ID | — | ✅ |
| 51 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 52 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 53 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 54 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 55 | RepairCost | REPAIR_COST | — | ✅ |
| 56 | SourceDocId | SOURCE_DOC_ID | — | ✅ |
| 57 | SourceDocTypeCode | SOURCE_DOC_TYPE_CODE | — | ✅ |
| 58 | SourceSystemId | SOURCE_SYSTEM_ID | — | ✅ |
| 59 | SourceSystemType | SOURCE_SYSTEM_TYPE | — | ✅ |
| 60 | TbfDays | TBF_DAYS | — | ✅ |
| 61 | TbfMeterUnits | TBF_METER_UNITS | — | ✅ |
| 62 | TbfMeterUnitsUomCode | TBF_METER_UNITS_UOM_CODE | — | ✅ |
| 63 | TrackingObjectId | TRACKING_OBJECT_ID | — | ✅ |
| 64 | TrackingObjectType | TRACKING_OBJECT_TYPE | — | ✅ |
| 65 | WoCompletionDate | WO_COMPLETION_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
