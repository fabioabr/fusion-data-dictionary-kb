---
id: DOC-OTHER-PVO-FosEventDefinitionExtractPVO
doc_type: system-doc
title: "FosEventDefinitionExtractPVO — PVO Cross-Module"
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
  - FosEventDefinitionExtractPVO
  - foseventdefinitionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FosEventDefinitionExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fos Event Definition Extract. Acessa as tabelas: FOS_EVENT_DEFINITIONS_B, FOS_EVENT_DEFINITIONS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.FosBiccExtractAM.FosEventDefinitionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 58 | 2 | 1 | 56 | 97% |

---

## 🔗 Tabelas Relacionadas

- [[fos_event_definitions_b|FOS_EVENT_DEFINITIONS_B]] — 45 atributos (1 PKs, 45 BICC)
- [[fos_event_definitions_tl|FOS_EVENT_DEFINITIONS_TL]] — 13 atributos (11 BICC)

---

## ⚙️ Atributos

### [[fos_event_definitions_b|FOS_EVENT_DEFINITIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventDefinitionsBPEOAgreementType | AGREEMENT_TYPE | — | ✅ |
| 2 | EventDefinitionsBPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 3 | EventDefinitionsBPEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | ✅ |
| 4 | EventDefinitionsBPEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | ✅ |
| 5 | EventDefinitionsBPEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | ✅ |
| 6 | EventDefinitionsBPEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | ✅ |
| 7 | EventDefinitionsBPEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | ✅ |
| 8 | EventDefinitionsBPEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | ✅ |
| 9 | EventDefinitionsBPEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | ✅ |
| 10 | EventDefinitionsBPEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | ✅ |
| 11 | EventDefinitionsBPEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | ✅ |
| 12 | EventDefinitionsBPEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | ✅ |
| 13 | EventDefinitionsBPEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | ✅ |
| 14 | EventDefinitionsBPEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | ✅ |
| 15 | EventDefinitionsBPEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | ✅ |
| 16 | EventDefinitionsBPEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | ✅ |
| 17 | EventDefinitionsBPEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | ✅ |
| 18 | EventDefinitionsBPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 19 | EventDefinitionsBPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 20 | EventDefinitionsBPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 21 | EventDefinitionsBPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 22 | EventDefinitionsBPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 23 | EventDefinitionsBPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 24 | EventDefinitionsBPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 25 | EventDefinitionsBPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 26 | EventDefinitionsBPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 27 | EventDefinitionsBPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 28 | EventDefinitionsBPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 29 | EventDefinitionsBPEOCancellationEventTypeFlag | CANCELLATION_EVENT_TYPE_FLAG | — | ✅ |
| 30 | EventDefinitionsBPEOCreatedBy | CREATED_BY | — | ✅ |
| 31 | EventDefinitionsBPEOCreationDate | CREATION_DATE | — | ✅ |
| 32 | EventDefinitionsBPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 33 | EventDefinitionsBPEOEventDefinitionId | EVENT_DEFINITION_ID | 🔑 | ✅ |
| 34 | EventDefinitionsBPEOEventName | EVENT_NAME | — | ✅ |
| 35 | EventDefinitionsBPEOEventType | EVENT_TYPE | — | ✅ |
| 36 | EventDefinitionsBPEOFlowType | FLOW_TYPE | — | ✅ |
| 37 | EventDefinitionsBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 38 | EventDefinitionsBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 39 | EventDefinitionsBPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 40 | EventDefinitionsBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 41 | EventDefinitionsBPEOOriginalEventType | ORIGINAL_EVENT_TYPE | — | ✅ |
| 42 | EventDefinitionsBPEOOwnershipChgEventTypeFlag | OWNERSHIP_CHG_EVENT_TYPE_FLAG | — | ✅ |
| 43 | EventDefinitionsBPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 44 | EventDefinitionsBPEOSeededFlag | SEEDED_FLAG | — | ✅ |
| 45 | EventDefinitionsBPEOSequenceNumber | SEQUENCE_NUMBER | — | ✅ |

### [[fos_event_definitions_tl|FOS_EVENT_DEFINITIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventDefinitionsTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | EventDefinitionsTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | EventDefinitionsTLPEODescription | DESCRIPTION | — | ✅ |
| 4 | EventDefinitionsTLPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 5 | EventDefinitionsTLPEOEventDefinitionId | EVENT_DEFINITION_ID | — | ✅ |
| 6 | EventDefinitionsTLPEOEventTypeName | EVENT_TYPE_NAME | — | ✅ |
| 7 | EventDefinitionsTLPEOLanguage | LANGUAGE | — | — |
| 8 | EventDefinitionsTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | EventDefinitionsTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | EventDefinitionsTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | EventDefinitionsTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | EventDefinitionsTLPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 13 | EventDefinitionsTLPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
