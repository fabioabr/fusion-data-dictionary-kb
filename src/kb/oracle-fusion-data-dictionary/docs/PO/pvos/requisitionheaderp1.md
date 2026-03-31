---
id: DOC-PO-PVO-RequisitionHeaderP1
doc_type: system-doc
title: "RequisitionHeaderP1 — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - RequisitionHeaderP1
  - requisitionheaderp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RequisitionHeaderP1

## 📌 Visão Geral

Disponibiliza cabeçalhos de requisições de compra para consulta operacional, com dados de solicitante, status e datas. Suporta acompanhamento em tempo real do andamento das requisições.

**Caminho:** `FscmTopModelAM.PrcPorPublicViewAM.RequisitionHeaderP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 29 | 1 | 1 | 6 | 21% |

---

## 🔗 Tabelas Relacionadas

- [[por_requisition_headers_all|POR_REQUISITION_HEADERS_ALL]] — 29 atributos (1 PKs, 6 BICC)

---

## ⚙️ Atributos

### [[por_requisition_headers_all|POR_REQUISITION_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActiveRequisitionFlag | ACTIVE_REQUISITION_FLAG | — | — |
| 2 | ApprovedDate | APPROVED_DATE | — | — |
| 3 | BudgetControlEnabledFlag | BUDGET_CONTROL_ENABLED_FLAG | — | — |
| 4 | ChangePendingFlag | CHANGE_PENDING_FLAG | — | — |
| 5 | CreatedBy | CREATED_BY | — | — |
| 6 | CreationDate | CREATION_DATE | — | — |
| 7 | Description | DESCRIPTION | — | ✅ |
| 8 | DocumentStatus | DOCUMENT_STATUS | — | ✅ |
| 9 | EmergencyPoNumber | EMERGENCY_PO_NUMBER | — | — |
| 10 | EmergencyReqFlag | EMERGENCY_REQ_FLAG | — | — |
| 11 | InterfaceSourceCode | INTERFACE_SOURCE_CODE | — | ✅ |
| 12 | InterfaceSourceLineId | INTERFACE_SOURCE_LINE_ID | — | — |
| 13 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 14 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 15 | Justification | JUSTIFICATION | — | ✅ |
| 16 | LastUpdateDate | LAST_UPDATE_DATE | — | — |
| 17 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 18 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 19 | ModifyingApproverId | MODIFYING_APPROVER_ID | — | — |
| 20 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 21 | PcardId | PCARD_ID | — | — |
| 22 | PrcBuId | PRC_BU_ID | — | — |
| 23 | PreparerId | PREPARER_ID | — | — |
| 24 | ReqBuId | REQ_BU_ID | — | — |
| 25 | RequestId | REQUEST_ID | — | — |
| 26 | RequisitionHeaderId | REQUISITION_HEADER_ID | 🔑 | ✅ |
| 27 | RequisitionNumber | REQUISITION_NUMBER | — | ✅ |
| 28 | SoldtoLeId | SOLDTO_LE_ID | — | — |
| 29 | SubmissionDate | SUBMISSION_DATE | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
