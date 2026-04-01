---
id: DOC-OTHER-PVO-FosFlowInstanceExtractPVO
doc_type: system-doc
title: "FosFlowInstanceExtractPVO — PVO Cross-Module"
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
  - FosFlowInstanceExtractPVO
  - fosflowinstanceextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FosFlowInstanceExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fos Flow Instance Extract. Acessa as tabelas: FOS_FLOW_INSTANCES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.FosBiccExtractAM.FosFlowInstanceExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 35 | 1 | 1 | 35 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fos_flow_instances|FOS_FLOW_INSTANCES]] — 35 atributos (1 PKs, 35 BICC)

---

## ⚙️ Atributos

### [[fos_flow_instances|FOS_FLOW_INSTANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FlowInstancePEOAgreementFtrId | AGREEMENT_FTR_ID | — | ✅ |
| 2 | FlowInstancePEOAgreementPtrId | AGREEMENT_PTR_ID | — | ✅ |
| 3 | FlowInstancePEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | FlowInstancePEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | FlowInstancePEODocumentFlowAssignmentId | DOCUMENT_FLOW_ASSIGNMENT_ID | — | ✅ |
| 6 | FlowInstancePEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 7 | FlowInstancePEOEventDataId | EVENT_DATA_ID | — | ✅ |
| 8 | FlowInstancePEOEventDefinitionId | EVENT_DEFINITION_ID | — | ✅ |
| 9 | FlowInstancePEOFlowInstanceId | FLOW_INSTANCE_ID | 🔑 | ✅ |
| 10 | FlowInstancePEOFlowType | FLOW_TYPE | — | ✅ |
| 11 | FlowInstancePEOGroupId | GROUP_ID | — | ✅ |
| 12 | FlowInstancePEOImportDate | IMPORT_DATE | — | ✅ |
| 13 | FlowInstancePEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 14 | FlowInstancePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 15 | FlowInstancePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | FlowInstancePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 17 | FlowInstancePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 18 | FlowInstancePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 19 | FlowInstancePEOProcessBatchId | PROCESS_BATCH_ID | — | ✅ |
| 20 | FlowInstancePEORequestId | REQUEST_ID | — | ✅ |
| 21 | FlowInstancePEOStatus | STATUS | — | ✅ |
| 22 | FlowInstancePEOSystemId | SYSTEM_ID | — | ✅ |
| 23 | FlowInstancePEOTaDocumentId | TA_DOCUMENT_ID | — | ✅ |
| 24 | FlowInstancePEOTargetDocumentDetail | TARGET_DOCUMENT_DETAIL | — | ✅ |
| 25 | FlowInstancePEOTargetDocumentDetailId | TARGET_DOCUMENT_DETAIL_ID | — | ✅ |
| 26 | FlowInstancePEOTargetDocumentHeader | TARGET_DOCUMENT_HEADER | — | ✅ |
| 27 | FlowInstancePEOTargetDocumentHeaderId | TARGET_DOCUMENT_HEADER_ID | — | ✅ |
| 28 | FlowInstancePEOTargetDocumentLine | TARGET_DOCUMENT_LINE | — | ✅ |
| 29 | FlowInstancePEOTargetDocumentLineId | TARGET_DOCUMENT_LINE_ID | — | ✅ |
| 30 | FlowInstancePEOTargetSystemId | TARGET_SYSTEM_ID | — | ✅ |
| 31 | FlowInstancePEOTaskGroup | TASK_GROUP | — | ✅ |
| 32 | FlowInstancePEOTaskSequence | TASK_SEQUENCE | — | ✅ |
| 33 | FlowInstancePEOTaskType | TASK_TYPE | — | ✅ |
| 34 | FlowInstancePEOTaxCalculationStatus | TAX_CALCULATION_STATUS | — | ✅ |
| 35 | FlowInstancePEOTransactionType | TRANSACTION_TYPE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
