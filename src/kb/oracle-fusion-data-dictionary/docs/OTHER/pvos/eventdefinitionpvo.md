---
id: DOC-OTHER-PVO-EventDefinitionPVO
doc_type: system-doc
title: "EventDefinitionPVO — PVO Cross-Module"
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
  - EventDefinitionPVO
  - eventdefinitionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EventDefinitionPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Event Definition. Acessa as tabelas: FOS_EVENT_DEFINITIONS_VL.

**Caminho:** `FscmTopModelAM.FosOrchestrationProcessAM.EventDefinitionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 19 | 1 | 1 | 19 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fos_event_definitions_vl|FOS_EVENT_DEFINITIONS_VL]] — 19 atributos (1 PKs, 19 BICC)

---

## ⚙️ Atributos

### [[fos_event_definitions_vl|FOS_EVENT_DEFINITIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventDefinitionPEOAgreementType | AGREEMENT_TYPE | — | ✅ |
| 2 | EventDefinitionPEOCancellationEventTypeFlag | CANCELLATION_EVENT_TYPE_FLAG | — | ✅ |
| 3 | EventDefinitionPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | EventDefinitionPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | EventDefinitionPEODescription | DESCRIPTION | — | ✅ |
| 6 | EventDefinitionPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 7 | EventDefinitionPEOEventDefinitionId | EVENT_DEFINITION_ID | 🔑 | ✅ |
| 8 | EventDefinitionPEOEventName | EVENT_NAME | — | ✅ |
| 9 | EventDefinitionPEOEventType | EVENT_TYPE | — | ✅ |
| 10 | EventDefinitionPEOEventTypeName | EVENT_TYPE_NAME | — | ✅ |
| 11 | EventDefinitionPEOFlowType | FLOW_TYPE | — | ✅ |
| 12 | EventDefinitionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | EventDefinitionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | EventDefinitionPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | EventDefinitionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 16 | EventDefinitionPEOOriginalEventType | ORIGINAL_EVENT_TYPE | — | ✅ |
| 17 | EventDefinitionPEOOwnershipChgEventTypeFlag | OWNERSHIP_CHG_EVENT_TYPE_FLAG | — | ✅ |
| 18 | EventDefinitionPEOSeededFlag | SEEDED_FLAG | — | ✅ |
| 19 | EventDefinitionPEOSequenceNumber | SEQUENCE_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
