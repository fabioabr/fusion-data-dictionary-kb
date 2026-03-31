---
id: DOC-OTHER-PVO-CustomerItem
doc_type: system-doc
title: "CustomerItem — PVO Cross-Module"
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
  - CustomerItem
  - customeritem
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CustomerItem

## 📌 Visão Geral

View Object para extração BICC de dados de Customer Item. Acessa as tabelas: EGO_ITEM_ASSOCIATIONS, EGP_ITEM_RELATIONSHIPS_B_V, EGP_TRADING_PARTNER_ITEMS.

**Caminho:** `FscmTopModelAM.EgpItemsPublicModelAM.CustomerItem`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 78 | 3 | 1 | 9 | 12% |

---

## 🔗 Tabelas Relacionadas

- [[ego_item_associations|EGO_ITEM_ASSOCIATIONS]] — 19 atributos (1 BICC)
- [[egp_item_relationships_b_v|EGP_ITEM_RELATIONSHIPS_B_V]] — 38 atributos (1 BICC)
- [[egp_trading_partner_items|EGP_TRADING_PARTNER_ITEMS]] — 21 atributos (1 PKs, 7 BICC)

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
| 1 | ItemRelationshipBasePEOAltItemRelationshipCode | ALT_ITEM_RELATIONSHIP_CODE | — | — |
| 2 | ItemRelationshipBasePEOApprovalStatus | APPROVAL_STATUS | — | — |
| 3 | ItemRelationshipBasePEOCreatedBy | CREATED_BY | — | — |
| 4 | ItemRelationshipBasePEOCreationDate | CREATION_DATE | — | — |
| 5 | ItemRelationshipBasePEOCrossReference | CROSS_REFERENCE | — | — |
| 6 | ItemRelationshipBasePEODerivedOrgId | MASTER_ORGANIZATION_ID | — | — |
| 7 | ItemRelationshipBasePEODescription | DESCRIPTION | — | — |
| 8 | ItemRelationshipBasePEOEndDateActive | END_DATE_ACTIVE | — | — |
| 9 | ItemRelationshipBasePEOEpcGtinSerial | EPC_GTIN_SERIAL | — | — |
| 10 | ItemRelationshipBasePEOFirstArticleStatus | FIRST_ARTICLE_STATUS | — | — |
| 11 | ItemRelationshipBasePEOInactiveFlag | INACTIVE_FLAG | — | — |
| 12 | ItemRelationshipBasePEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 13 | ItemRelationshipBasePEOItemRelationshipId | ITEM_RELATIONSHIP_ID | — | — |
| 14 | ItemRelationshipBasePEOItemRelationshipType | ITEM_RELATIONSHIP_TYPE | — | — |
| 15 | ItemRelationshipBasePEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 16 | ItemRelationshipBasePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 17 | ItemRelationshipBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 18 | ItemRelationshipBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 19 | ItemRelationshipBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 20 | ItemRelationshipBasePEOMasterOrganizationId | MASTER_ORGANIZATION_ID | — | — |
| 21 | ItemRelationshipBasePEOMrpPlanningCode | MRP_PLANNING_CODE | — | — |
| 22 | ItemRelationshipBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 23 | ItemRelationshipBasePEOOrgIndependentFlag | ORG_INDEPENDENT_FLAG | — | — |
| 24 | ItemRelationshipBasePEOOrganizationId | ORGANIZATION_ID | — | — |
| 25 | ItemRelationshipBasePEOPlanningEnabledFlag | PLANNING_ENABLED_FLAG | — | — |
| 26 | ItemRelationshipBasePEOPreferenceNumber | PREFERENCE_NUMBER | — | — |
| 27 | ItemRelationshipBasePEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 28 | ItemRelationshipBasePEOProgramName | PROGRAM_NAME | — | — |
| 29 | ItemRelationshipBasePEOReciprocalFlag | RECIPROCAL_FLAG | — | — |
| 30 | ItemRelationshipBasePEORelatedItemId | RELATED_ITEM_ID | — | — |
| 31 | ItemRelationshipBasePEORelateditemRank | RELATEDITEM_RANK | — | — |
| 32 | ItemRelationshipBasePEORequestId | REQUEST_ID | — | — |
| 33 | ItemRelationshipBasePEORevisionId | REVISION_ID | — | — |
| 34 | ItemRelationshipBasePEOSourceSystemId | SOURCE_SYSTEM_ID | — | — |
| 35 | ItemRelationshipBasePEOStartDateActive | START_DATE_ACTIVE | — | — |
| 36 | ItemRelationshipBasePEOSubType | SUB_TYPE | — | — |
| 37 | ItemRelationshipBasePEOTpItemId | TP_ITEM_ID | — | — |
| 38 | ItemRelationshipBasePEOUomCode | UOM_CODE | — | — |

### [[egp_trading_partner_items|EGP_TRADING_PARTNER_ITEMS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedFromTpItemPEOTpItemDesc | TP_ITEM_DESC | — | — |
| 2 | CreatedFromTpItemPEOTpItemId | TP_ITEM_ID | — | — |
| 3 | CreatedFromTpItemPEOTpItemNumber | TP_ITEM_NUMBER | — | — |
| 4 | CreatedFromTpItemPEOTpType | TP_TYPE | — | — |
| 5 | CustomerItemPEOCreatedBy | CREATED_BY | — | — |
| 6 | CustomerItemPEOCreatedFromTpiId | CREATED_FROM_TPI_ID | — | — |
| 7 | CustomerItemPEOCreationDate | CREATION_DATE | — | — |
| 8 | CustomerItemPEOEndDate | END_DATE | — | ✅ |
| 9 | CustomerItemPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | CustomerItemPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | CustomerItemPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | CustomerItemPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | CustomerItemPEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 14 | CustomerItemPEOProgramName | PROGRAM_NAME | — | — |
| 15 | CustomerItemPEORequestId | REQUEST_ID | — | — |
| 16 | CustomerItemPEOStartDate | START_DATE | — | ✅ |
| 17 | CustomerItemPEOTpItemDesc | TP_ITEM_DESC | — | ✅ |
| 18 | CustomerItemPEOTpItemNumber | TP_ITEM_NUMBER | — | ✅ |
| 19 | CustomerItemPEOTpType | TP_TYPE | — | ✅ |
| 20 | CustomerItemPEOTradingPartnerId | TRADING_PARTNER_ID | — | — |
| 21 | TpItemId | TP_ITEM_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
