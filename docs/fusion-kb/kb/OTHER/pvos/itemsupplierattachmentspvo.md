---
id: DOC-OTHER-PVO-ItemSupplierAttachmentsPVO
doc_type: system-doc
title: "ItemSupplierAttachmentsPVO — PVO Cross-Module"
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
  - ItemSupplierAttachmentsPVO
  - itemsupplierattachmentspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ItemSupplierAttachmentsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Item Supplier Attachments. Acessa as tabelas: EGP_ITEM_ATTACHMENTS_INTF.

**Caminho:** `FscmTopModelAM.EgiBatchesPublicModelAnalyticsAM.ItemSupplierAttachmentsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 42 | 1 | 1 | 42 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[egp_item_attachments_intf|EGP_ITEM_ATTACHMENTS_INTF]] — 42 atributos (1 PKs, 42 BICC)

---

## ⚙️ Atributos

### [[egp_item_attachments_intf|EGP_ITEM_ATTACHMENTS_INTF]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemSupplierAttachmentsPEOAttachmentCategory | ATTACHMENT_CATEGORY | — | ✅ |
| 2 | ItemSupplierAttachmentsPEOBatchAttachedDocId | BATCH_ATTACHED_DOC_ID | — | ✅ |
| 3 | ItemSupplierAttachmentsPEOBatchDocCategory | BATCH_DOC_CATEGORY | — | ✅ |
| 4 | ItemSupplierAttachmentsPEOBatchDocName | BATCH_DOC_NAME | — | ✅ |
| 5 | ItemSupplierAttachmentsPEOBatchDocumentId | BATCH_DOCUMENT_ID | — | ✅ |
| 6 | ItemSupplierAttachmentsPEOBatchId | BATCH_ID | — | ✅ |
| 7 | ItemSupplierAttachmentsPEOBatchNumber | BATCH_NUMBER | — | ✅ |
| 8 | ItemSupplierAttachmentsPEOCreatedBy | CREATED_BY | — | ✅ |
| 9 | ItemSupplierAttachmentsPEOCreatedByModule | CREATED_BY_MODULE | — | ✅ |
| 10 | ItemSupplierAttachmentsPEOCreationDate | CREATION_DATE | — | ✅ |
| 11 | ItemSupplierAttachmentsPEODescription | DESCRIPTION | — | ✅ |
| 12 | ItemSupplierAttachmentsPEOFileType | FILE_TYPE | — | ✅ |
| 13 | ItemSupplierAttachmentsPEOFileTypeName | FILE_TYPE_NAME | — | ✅ |
| 14 | ItemSupplierAttachmentsPEOFileUrlText | FILE_URL_TEXT | — | ✅ |
| 15 | ItemSupplierAttachmentsPEOInterfaceDataType | INTERFACE_DATA_TYPE | — | ✅ |
| 16 | ItemSupplierAttachmentsPEOInterfaceTableUniqueId | INTERFACE_TABLE_UNIQUE_ID | 🔑 | ✅ |
| 17 | ItemSupplierAttachmentsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 18 | ItemSupplierAttachmentsPEOItemNumber | ITEM_NUMBER | — | ✅ |
| 19 | ItemSupplierAttachmentsPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 20 | ItemSupplierAttachmentsPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 21 | ItemSupplierAttachmentsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 22 | ItemSupplierAttachmentsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 23 | ItemSupplierAttachmentsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 24 | ItemSupplierAttachmentsPEOLoadRequestId | LOAD_REQUEST_ID | — | ✅ |
| 25 | ItemSupplierAttachmentsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 26 | ItemSupplierAttachmentsPEOOrganizationCode | ORGANIZATION_CODE | — | ✅ |
| 27 | ItemSupplierAttachmentsPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 28 | ItemSupplierAttachmentsPEOPhaseNumber | PHASE_NUMBER | — | ✅ |
| 29 | ItemSupplierAttachmentsPEOPrimaryCategoryFlag | PRIMARY_CATEGORY_FLAG | — | ✅ |
| 30 | ItemSupplierAttachmentsPEOProcessStatus | PROCESS_STATUS | — | ✅ |
| 31 | ItemSupplierAttachmentsPEOProgramAppName | PROGRAM_APP_NAME | — | ✅ |
| 32 | ItemSupplierAttachmentsPEOProgramName | PROGRAM_NAME | — | ✅ |
| 33 | ItemSupplierAttachmentsPEORequestId | REQUEST_ID | — | ✅ |
| 34 | ItemSupplierAttachmentsPEOSeqNum | SEQ_NUM | — | ✅ |
| 35 | ItemSupplierAttachmentsPEOShared | SHARED | — | ✅ |
| 36 | ItemSupplierAttachmentsPEOSourceSystemCode | SOURCE_SYSTEM_CODE | — | ✅ |
| 37 | ItemSupplierAttachmentsPEOSourceSystemId | SOURCE_SYSTEM_ID | — | ✅ |
| 38 | ItemSupplierAttachmentsPEOSourceSystemReference | SOURCE_SYSTEM_REFERENCE | — | ✅ |
| 39 | ItemSupplierAttachmentsPEOThreadNumber | THREAD_NUMBER | — | ✅ |
| 40 | ItemSupplierAttachmentsPEOTitle | TITLE | — | ✅ |
| 41 | ItemSupplierAttachmentsPEOTransactionId | TRANSACTION_ID | — | ✅ |
| 42 | ItemSupplierAttachmentsPEOTransactionType | TRANSACTION_TYPE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
