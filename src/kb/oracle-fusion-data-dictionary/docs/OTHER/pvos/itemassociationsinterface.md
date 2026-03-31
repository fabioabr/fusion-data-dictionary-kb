---
id: DOC-OTHER-PVO-ItemAssociationsInterface
doc_type: system-doc
title: "ItemAssociationsInterface — PVO Cross-Module"
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
  - ItemAssociationsInterface
  - itemassociationsinterface
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ItemAssociationsInterface

## 📌 Visão Geral

View Object para extração BICC de dados de Item Associations Interface. Acessa as tabelas: EGO_ITEM_ASSOCIATIONS_INTF.

**Caminho:** `FscmTopModelAM.EgiBatchesPublicModelAnalyticsAM.ItemAssociationsInterface`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 45 | 1 | 2 | 45 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ego_item_associations_intf|EGO_ITEM_ASSOCIATIONS_INTF]] — 45 atributos (2 PKs, 45 BICC)

---

## ⚙️ Atributos

### [[ego_item_associations_intf|EGO_ITEM_ASSOCIATIONS_INTF]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemAssociationsInterfacePEOAcdType | ACD_TYPE | 🔑 | ✅ |
| 2 | ItemAssociationsInterfacePEOAssociationId | ASSOCIATION_ID | — | ✅ |
| 3 | ItemAssociationsInterfacePEOAssociationTransactionId | ASSOCIATION_TRANSACTION_ID | 🔑 | ✅ |
| 4 | ItemAssociationsInterfacePEOBatchId | BATCH_ID | — | ✅ |
| 5 | ItemAssociationsInterfacePEOBatchNumber | BATCH_NUMBER | — | ✅ |
| 6 | ItemAssociationsInterfacePEOBundleId | BUNDLE_ID | — | ✅ |
| 7 | ItemAssociationsInterfacePEOChangeLineId | CHANGE_LINE_ID | — | ✅ |
| 8 | ItemAssociationsInterfacePEOCreatedBy | CREATED_BY | — | ✅ |
| 9 | ItemAssociationsInterfacePEOCreationDate | CREATION_DATE | — | ✅ |
| 10 | ItemAssociationsInterfacePEOGlobalLocationNumber | GLOBAL_LOCATION_NUMBER | — | ✅ |
| 11 | ItemAssociationsInterfacePEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 12 | ItemAssociationsInterfacePEOIsFakeRecord | IS_FAKE_RECORD | — | ✅ |
| 13 | ItemAssociationsInterfacePEOItemNumber | ITEM_NUMBER | — | ✅ |
| 14 | ItemAssociationsInterfacePEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 15 | ItemAssociationsInterfacePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 16 | ItemAssociationsInterfacePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | ItemAssociationsInterfacePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 18 | ItemAssociationsInterfacePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 19 | ItemAssociationsInterfacePEOLoadRequestId | LOAD_REQUEST_ID | — | ✅ |
| 20 | ItemAssociationsInterfacePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 21 | ItemAssociationsInterfacePEOOrganizationCode | ORGANIZATION_CODE | — | ✅ |
| 22 | ItemAssociationsInterfacePEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 23 | ItemAssociationsInterfacePEOPhaseNumber | PHASE_NUMBER | — | ✅ |
| 24 | ItemAssociationsInterfacePEOPrimaryFlag | PRIMARY_FLAG | — | ✅ |
| 25 | ItemAssociationsInterfacePEOProcessStatus | PROCESS_STATUS | — | ✅ |
| 26 | ItemAssociationsInterfacePEOProgramAppName | PROGRAM_APP_NAME | — | ✅ |
| 27 | ItemAssociationsInterfacePEOProgramName | PROGRAM_NAME | — | ✅ |
| 28 | ItemAssociationsInterfacePEORequestId | REQUEST_ID | — | ✅ |
| 29 | ItemAssociationsInterfacePEOSourceSystemCode | SOURCE_SYSTEM_CODE | — | ✅ |
| 30 | ItemAssociationsInterfacePEOSourceSystemId | SOURCE_SYSTEM_ID | — | ✅ |
| 31 | ItemAssociationsInterfacePEOSourceSystemReference | SOURCE_SYSTEM_REFERENCE | — | ✅ |
| 32 | ItemAssociationsInterfacePEOStatusCode | STATUS_CODE | — | ✅ |
| 33 | ItemAssociationsInterfacePEOStyleItemFlag | STYLE_ITEM_FLAG | — | ✅ |
| 34 | ItemAssociationsInterfacePEOStyleItemId | STYLE_ITEM_ID | — | ✅ |
| 35 | ItemAssociationsInterfacePEOSupplierId | SUPPLIER_ID | — | ✅ |
| 36 | ItemAssociationsInterfacePEOSupplierName | SUPPLIER_NAME | — | ✅ |
| 37 | ItemAssociationsInterfacePEOSupplierNumber | SUPPLIER_NUMBER | — | ✅ |
| 38 | ItemAssociationsInterfacePEOSupplierSiteId | SUPPLIER_SITE_ID | — | ✅ |
| 39 | ItemAssociationsInterfacePEOSupplierSiteName | SUPPLIER_SITE_NAME | — | ✅ |
| 40 | ItemAssociationsInterfacePEOThreadNumber | THREAD_NUMBER | — | ✅ |
| 41 | ItemAssociationsInterfacePEOTransactionId | TRANSACTION_ID | — | ✅ |
| 42 | ItemAssociationsInterfacePEOTransactionType | TRANSACTION_TYPE | — | ✅ |
| 43 | ItemAssociationsInterfacePEOVersionEnabledFlag | VERSION_ENABLED_FLAG | — | ✅ |
| 44 | ItemAssociationsInterfacePEOVersionRevisionCode | VERSION_REVISION_CODE | — | ✅ |
| 45 | ItemAssociationsInterfacePEOVersionStartDate | VERSION_START_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
