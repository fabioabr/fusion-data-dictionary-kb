---
id: DOC-OTHER-PVO-WOOperationStartStopExtractPVO
doc_type: system-doc
title: "WOOperationStartStopExtractPVO — PVO Cross-Module"
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
  - WOOperationStartStopExtractPVO
  - wooperationstartstopextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WOOperationStartStopExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de WOOperation Start Stop Extract. Acessa as tabelas: WIE_WO_OPERATION_START_STOP.

**Caminho:** `FscmTopModelAM.ScmExtractAM.WieBiccExtractAM.WOOperationStartStopExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 3 | 15 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[wie_wo_operation_start_stop|WIE_WO_OPERATION_START_STOP]] — 15 atributos (3 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[wie_wo_operation_start_stop|WIE_WO_OPERATION_START_STOP]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WOOpStartStopPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | WOOpStartStopPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | WOOpStartStopPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 4 | WOOpStartStopPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 5 | WOOpStartStopPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | WOOpStartStopPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | WOOpStartStopPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | WOOpStartStopPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | WOOpStartStopPEOOperationStartTime | OPERATION_START_TIME | 🔑 | ✅ |
| 10 | WOOpStartStopPEOOperationStopTime | OPERATION_STOP_TIME | — | ✅ |
| 11 | WOOpStartStopPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 12 | WOOpStartStopPEORequestId | REQUEST_ID | — | ✅ |
| 13 | WOOpStartStopPEOWoOpStartStopId | WO_OP_START_STOP_ID | — | ✅ |
| 14 | WOOpStartStopPEOWoOperationId | WO_OPERATION_ID | 🔑 | ✅ |
| 15 | WOOpStartStopPEOWoProductSerialId | WO_PRODUCT_SERIAL_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
