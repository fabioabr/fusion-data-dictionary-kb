---
id: DOC-OTHER-PVO-MfgPartNumber
doc_type: system-doc
title: "MfgPartNumber — PVO Cross-Module"
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
  - MfgPartNumber
  - mfgpartnumber
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MfgPartNumber

## 📌 Visão Geral

View Object para extração BICC de dados de Mfg Part Number. Acessa as tabelas: EGO_ITEM_ASSOCIATIONS, EGP_ITEM_RELATIONSHIPS_B_V, EGP_TRADING_PARTNER_ITEMS.

**Caminho:** `FscmTopModelAM.EgpItemsPublicModelAM.MfgPartNumber`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 86 | 3 | 2 | 58 | 67% |

---

## 🔗 Tabelas Relacionadas

- [[ego_item_associations|EGO_ITEM_ASSOCIATIONS]] — 19 atributos (1 BICC)
- [[egp_item_relationships_b_v|EGP_ITEM_RELATIONSHIPS_B_V]] — 45 atributos (1 PKs, 40 BICC)
- [[egp_trading_partner_items|EGP_TRADING_PARTNER_ITEMS]] — 22 atributos (1 PKs, 17 BICC)

---

## ⚙️ Atributos

### [[ego_item_associations|EGO_ITEM_ASSOCIATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemSupplierAssociationPEOAcdType | ACD_TYPE | — | — |
| 2 | ItemSupplierAssociationPEOAssociationId | ASSOCIATION_ID | — | — |
| 3 | ItemSupplierAssociationPEOChangeBitMap | CHANGE_BIT_MAP | — | — |
| 4 | ItemSupplierAssociationPEOChangeLineId | CHANGE_LINE_ID | — | — |
| 5 | ItemSupplierAssociationPEOImplementationDate | IMPLEMENTATION_DATE | — | — |
| 6 | ItemSupplierAssociationPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 7 | ItemSupplierAssociationPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 8 | ItemSupplierAssociationPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 9 | ItemSupplierAssociationPEOOrganizationId | ORGANIZATION_ID | — | — |
| 10 | ItemSupplierAssociationPEOPartyStatus | PARTY_STATUS | — | — |
| 11 | ItemSupplierAssociationPEOPrimaryFlag | PRIMARY_FLAG | — | ✅ |
| 12 | ItemSupplierAssociationPEORequestId | REQUEST_ID | — | — |
| 13 | ItemSupplierAssociationPEOStatusCode | STATUS_CODE | — | — |
| 14 | ItemSupplierAssociationPEOStyleItemId | STYLE_ITEM_ID | — | — |
| 15 | ItemSupplierAssociationPEOSupplierId | SUPPLIER_ID | — | — |
| 16 | ItemSupplierAssociationPEOSupplierSiteId | SUPPLIER_SITE_ID | — | — |
| 17 | ItemSupplierAssociationPEOVersionEndDate | VERSION_END_DATE | — | — |
| 18 | ItemSupplierAssociationPEOVersionId | VERSION_ID | — | — |
| 19 | ItemSupplierAssociationPEOVersionStartDate | VERSION_START_DATE | — | — |

### [[egp_item_relationships_b_v|EGP_ITEM_RELATIONSHIPS_B_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemRelationshipBasePEOAcdType | ACD_TYPE | — | ✅ |
| 2 | ItemRelationshipBasePEOAltItemRelationshipCode | ALT_ITEM_RELATIONSHIP_CODE | — | ✅ |
| 3 | ItemRelationshipBasePEOApprovalStatus | APPROVAL_STATUS | — | ✅ |
| 4 | ItemRelationshipBasePEOChangeLineId | CHANGE_LINE_ID | — | ✅ |
| 5 | ItemRelationshipBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | ItemRelationshipBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | ItemRelationshipBasePEOCrossReference | CROSS_REFERENCE | — | ✅ |
| 8 | ItemRelationshipBasePEODerivedOrgId | MASTER_ORGANIZATION_ID | — | — |
| 9 | ItemRelationshipBasePEODescription | DESCRIPTION | — | ✅ |
| 10 | ItemRelationshipBasePEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 11 | ItemRelationshipBasePEOEpcGtinSerial | EPC_GTIN_SERIAL | — | ✅ |
| 12 | ItemRelationshipBasePEOFirstArticleStatus | FIRST_ARTICLE_STATUS | — | ✅ |
| 13 | ItemRelationshipBasePEOImplementationDate | IMPLEMENTATION_DATE | — | — |
| 14 | ItemRelationshipBasePEOInactiveFlag | INACTIVE_FLAG | — | ✅ |
| 15 | ItemRelationshipBasePEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 16 | ItemRelationshipBasePEOItemRelationshipId | ITEM_RELATIONSHIP_ID | 🔑 | ✅ |
| 17 | ItemRelationshipBasePEOItemRelationshipType | ITEM_RELATIONSHIP_TYPE | — | ✅ |
| 18 | ItemRelationshipBasePEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 19 | ItemRelationshipBasePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 20 | ItemRelationshipBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 21 | ItemRelationshipBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 22 | ItemRelationshipBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 23 | ItemRelationshipBasePEOMasterOrganizationId | MASTER_ORGANIZATION_ID | — | ✅ |
| 24 | ItemRelationshipBasePEOMrpPlanningCode | MRP_PLANNING_CODE | — | ✅ |
| 25 | ItemRelationshipBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 26 | ItemRelationshipBasePEOOrgIndependentFlag | ORG_INDEPENDENT_FLAG | — | ✅ |
| 27 | ItemRelationshipBasePEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 28 | ItemRelationshipBasePEOPlanningEnabledFlag | PLANNING_ENABLED_FLAG | — | ✅ |
| 29 | ItemRelationshipBasePEOPreferenceNumber | PREFERENCE_NUMBER | — | ✅ |
| 30 | ItemRelationshipBasePEOProgramAppName | PROGRAM_APP_NAME | — | ✅ |
| 31 | ItemRelationshipBasePEOProgramName | PROGRAM_NAME | — | ✅ |
| 32 | ItemRelationshipBasePEOReciprocalFlag | RECIPROCAL_FLAG | — | ✅ |
| 33 | ItemRelationshipBasePEORelatedItemId | RELATED_ITEM_ID | — | ✅ |
| 34 | ItemRelationshipBasePEORelateditemRank | RELATEDITEM_RANK | — | ✅ |
| 35 | ItemRelationshipBasePEORequestId | REQUEST_ID | — | ✅ |
| 36 | ItemRelationshipBasePEORevisionId | REVISION_ID | — | ✅ |
| 37 | ItemRelationshipBasePEOSourceSystemId | SOURCE_SYSTEM_ID | — | ✅ |
| 38 | ItemRelationshipBasePEOStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 39 | ItemRelationshipBasePEOStatusCode | STATUS_CODE | — | ✅ |
| 40 | ItemRelationshipBasePEOSubType | SUB_TYPE | — | ✅ |
| 41 | ItemRelationshipBasePEOTpItemId | TP_ITEM_ID | — | ✅ |
| 42 | ItemRelationshipBasePEOUomCode | UOM_CODE | — | ✅ |
| 43 | ItemRelationshipBasePEOVersionEndDate | VERSION_END_DATE | — | — |
| 44 | ItemRelationshipBasePEOVersionId | VERSION_ID | — | — |
| 45 | ItemRelationshipBasePEOVersionStartDate | VERSION_START_DATE | — | — |

### [[egp_trading_partner_items|EGP_TRADING_PARTNER_ITEMS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedFromTPItemPEOTpItemDesc | TP_ITEM_DESC | — | — |
| 2 | CreatedFromTPItemPEOTpItemId | TP_ITEM_ID | — | — |
| 3 | CreatedFromTPItemPEOTpItemNumber | TP_ITEM_NUMBER | — | — |
| 4 | CreatedFromTPItemPEOTpType | TP_TYPE | — | — |
| 5 | MfgPartNumberPEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | MfgPartNumberPEOCreatedFromTpiId | CREATED_FROM_TPI_ID | — | — |
| 7 | MfgPartNumberPEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | MfgPartNumberPEOEndDate | END_DATE | — | ✅ |
| 9 | MfgPartNumberPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | MfgPartNumberPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | MfgPartNumberPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | MfgPartNumberPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | MfgPartNumberPEOPartStatusCode | PART_STATUS_CODE | — | ✅ |
| 14 | MfgPartNumberPEOProgramAppName | PROGRAM_APP_NAME | — | ✅ |
| 15 | MfgPartNumberPEOProgramName | PROGRAM_NAME | — | ✅ |
| 16 | MfgPartNumberPEORequestId | REQUEST_ID | — | ✅ |
| 17 | MfgPartNumberPEOStartDate | START_DATE | — | ✅ |
| 18 | MfgPartNumberPEOTpItemDesc | TP_ITEM_DESC | — | ✅ |
| 19 | MfgPartNumberPEOTpItemNumber | TP_ITEM_NUMBER | — | ✅ |
| 20 | MfgPartNumberPEOTpType | TP_TYPE | — | ✅ |
| 21 | MfgPartNumberPEOTradingPartnerId | TRADING_PARTNER_ID | — | ✅ |
| 22 | TpItemId | TP_ITEM_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
