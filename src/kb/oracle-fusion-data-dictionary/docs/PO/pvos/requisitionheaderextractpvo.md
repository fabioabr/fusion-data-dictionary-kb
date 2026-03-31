---
id: DOC-PO-PVO-RequisitionHeaderExtractPVO
doc_type: system-doc
title: "RequisitionHeaderExtractPVO — PVO Purchasing"
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
  - RequisitionHeaderExtractPVO
  - requisitionheaderextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RequisitionHeaderExtractPVO

## 📌 Visão Geral

Extrai os cabeçalhos de requisições de compra para carga BICC, incluindo solicitante, departamento, urgência, status de aprovação e justificativa. Permite análise de demanda interna e tempo de ciclo.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PorBiccExtractAM.RequisitionHeaderExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 105 | 1 | 1 | 48 | 46% |

---

## 🔗 Tabelas Relacionadas

- [[por_requisition_headers_all|POR_REQUISITION_HEADERS_ALL]] — 105 atributos (1 PKs, 48 BICC)

---

## ⚙️ Atributos

### [[por_requisition_headers_all|POR_REQUISITION_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActiveRequisitionFlag | ACTIVE_REQUISITION_FLAG | — | ✅ |
| 2 | ApprovalInstanceId | APPROVAL_INSTANCE_ID | — | ✅ |
| 3 | ApprovedDate | APPROVED_DATE | — | ✅ |
| 4 | Attribute1 | ATTRIBUTE1 | — | — |
| 5 | Attribute10 | ATTRIBUTE10 | — | — |
| 6 | Attribute11 | ATTRIBUTE11 | — | — |
| 7 | Attribute12 | ATTRIBUTE12 | — | — |
| 8 | Attribute13 | ATTRIBUTE13 | — | — |
| 9 | Attribute14 | ATTRIBUTE14 | — | — |
| 10 | Attribute15 | ATTRIBUTE15 | — | — |
| 11 | Attribute16 | ATTRIBUTE16 | — | — |
| 12 | Attribute17 | ATTRIBUTE17 | — | — |
| 13 | Attribute18 | ATTRIBUTE18 | — | — |
| 14 | Attribute19 | ATTRIBUTE19 | — | — |
| 15 | Attribute2 | ATTRIBUTE2 | — | — |
| 16 | Attribute20 | ATTRIBUTE20 | — | — |
| 17 | Attribute3 | ATTRIBUTE3 | — | — |
| 18 | Attribute4 | ATTRIBUTE4 | — | — |
| 19 | Attribute5 | ATTRIBUTE5 | — | — |
| 20 | Attribute6 | ATTRIBUTE6 | — | — |
| 21 | Attribute7 | ATTRIBUTE7 | — | — |
| 22 | Attribute8 | ATTRIBUTE8 | — | — |
| 23 | Attribute9 | ATTRIBUTE9 | — | — |
| 24 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 25 | AttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 26 | AttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 27 | AttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 28 | AttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 29 | AttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 30 | AttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 31 | AttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 32 | AttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 33 | AttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 34 | AttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 35 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 36 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 37 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 38 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 39 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 40 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 41 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 42 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 43 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 44 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 45 | AttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 46 | AttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 47 | AttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 48 | AttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 49 | AttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 50 | AttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 51 | AttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 52 | AttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 53 | AttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 54 | AttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 55 | BudgetControlEnabledFlag | BUDGET_CONTROL_ENABLED_FLAG | — | ✅ |
| 56 | ChangePendingFlag | CHANGE_PENDING_FLAG | — | ✅ |
| 57 | CreatedBy | CREATED_BY | — | ✅ |
| 58 | CreationDate | CREATION_DATE | — | ✅ |
| 59 | DefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | ✅ |
| 60 | Description | DESCRIPTION | — | ✅ |
| 61 | DocumentStatus | DOCUMENT_STATUS | — | ✅ |
| 62 | DocumentSubType | DOCUMENT_SUB_TYPE | — | ✅ |
| 63 | EmergencyPoNumber | EMERGENCY_PO_NUMBER | — | ✅ |
| 64 | EmergencyReqFlag | EMERGENCY_REQ_FLAG | — | ✅ |
| 65 | ExternallyManagedFlag | EXTERNALLY_MANAGED_FLAG | — | ✅ |
| 66 | FundsChkFailWarnFlag | FUNDS_CHK_FAIL_WARN_FLAG | — | ✅ |
| 67 | FundsOverrideApproverId | FUNDS_OVERRIDE_APPROVER_ID | — | ✅ |
| 68 | FundsStatus | FUNDS_STATUS | — | ✅ |
| 69 | HasActionRequiredLinesFlag | HAS_ACTION_REQUIRED_LINES | — | ✅ |
| 70 | HasCanceledLines | HAS_CANCELED_LINES | — | — |
| 71 | HasIncompleteLines | HAS_INCOMPLETE_LINES | — | — |
| 72 | HasPendingApprLines | HAS_PENDING_APPR_LINES | — | — |
| 73 | HasRejectedLines | HAS_REJECTED_LINES | — | — |
| 74 | HasReturnedLines | HAS_RETURNED_LINES | — | — |
| 75 | HasWithdrawnLines | HAS_WITHDRAWN_LINES | — | — |
| 76 | InsufficientFundsFlag | INSUFFICIENT_FUNDS_FLAG | — | ✅ |
| 77 | InterfaceSourceCode | INTERFACE_SOURCE_CODE | — | ✅ |
| 78 | InterfaceSourceLineId | INTERFACE_SOURCE_LINE_ID | — | ✅ |
| 79 | InternalTransferReqFlag | INTERNAL_TRANSFER_REQ_FLAG | — | ✅ |
| 80 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 81 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 82 | Justification | JUSTIFICATION | — | ✅ |
| 83 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 84 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 85 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 86 | LifecycleStatus | LIFECYCLE_STATUS | — | ✅ |
| 87 | LineGroup | LINE_GROUP | — | ✅ |
| 88 | LockedByBuyerFlag | LOCKED_BY_BUYER_FLAG | — | ✅ |
| 89 | ModifyingApproverId | MODIFYING_APPROVER_ID | — | ✅ |
| 90 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 91 | OverridingApproverId | OVERRIDING_APPROVER_ID | — | ✅ |
| 92 | PcardId | PCARD_ID | — | ✅ |
| 93 | PrcBuId | PRC_BU_ID | — | ✅ |
| 94 | PreparerId | PREPARER_ID | — | ✅ |
| 95 | ProcessStatus | PROCESS_STATUS | — | ✅ |
| 96 | RejectReason | REJECT_REASON | — | ✅ |
| 97 | RejectedByApproverId | REJECTED_BY_APPROVER_ID | — | ✅ |
| 98 | ReqBuId | REQ_BU_ID | — | ✅ |
| 99 | ReqImportApproverId | REQ_IMPORT_APPROVER_ID | — | ✅ |
| 100 | RequestId | REQUEST_ID | — | ✅ |
| 101 | RequisitionHeaderId | REQUISITION_HEADER_ID | 🔑 | ✅ |
| 102 | RequisitionNumber | REQUISITION_NUMBER | — | ✅ |
| 103 | SoldtoLeId | SOLDTO_LE_ID | — | ✅ |
| 104 | SubmissionDate | SUBMISSION_DATE | — | ✅ |
| 105 | TaxUserOverrideHdrFlag | TAX_USER_OVERRIDE_HDR_FLAG | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
