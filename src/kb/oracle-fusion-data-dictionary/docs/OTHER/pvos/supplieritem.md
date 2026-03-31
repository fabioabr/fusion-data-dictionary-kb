---
id: DOC-OTHER-PVO-SupplierItem
doc_type: system-doc
title: "SupplierItem — PVO Cross-Module"
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
  - SupplierItem
  - supplieritem
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplierItem

## 📌 Visão Geral

View Object para extração BICC de dados de Supplier Item. Acessa as tabelas: EGO_ITEM_ASSOCIATIONS, EGP_ITEM_RELATIONSHIPS_B_V, EGP_TRADING_PARTNER_ITEMS.

**Caminho:** `FscmTopModelAM.EgpItemsPublicModelAM.SupplierItem`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 114 | 3 | 1 | 9 | 8% |

---

## 🔗 Tabelas Relacionadas

- [[ego_item_associations|EGO_ITEM_ASSOCIATIONS]] — 19 atributos (1 BICC)
- [[egp_item_relationships_b_v|EGP_ITEM_RELATIONSHIPS_B_V]] — 38 atributos (1 BICC)
- [[egp_trading_partner_items|EGP_TRADING_PARTNER_ITEMS]] — 57 atributos (1 PKs, 7 BICC)

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
| 5 | SupplierItemPEOAttribute1 | ATTRIBUTE1 | — | — |
| 6 | SupplierItemPEOAttribute10 | ATTRIBUTE10 | — | — |
| 7 | SupplierItemPEOAttribute11 | ATTRIBUTE11 | — | — |
| 8 | SupplierItemPEOAttribute12 | ATTRIBUTE12 | — | — |
| 9 | SupplierItemPEOAttribute13 | ATTRIBUTE13 | — | — |
| 10 | SupplierItemPEOAttribute14 | ATTRIBUTE14 | — | — |
| 11 | SupplierItemPEOAttribute15 | ATTRIBUTE15 | — | — |
| 12 | SupplierItemPEOAttribute2 | ATTRIBUTE2 | — | — |
| 13 | SupplierItemPEOAttribute3 | ATTRIBUTE3 | — | — |
| 14 | SupplierItemPEOAttribute4 | ATTRIBUTE4 | — | — |
| 15 | SupplierItemPEOAttribute5 | ATTRIBUTE5 | — | — |
| 16 | SupplierItemPEOAttribute6 | ATTRIBUTE6 | — | — |
| 17 | SupplierItemPEOAttribute7 | ATTRIBUTE7 | — | — |
| 18 | SupplierItemPEOAttribute8 | ATTRIBUTE8 | — | — |
| 19 | SupplierItemPEOAttribute9 | ATTRIBUTE9 | — | — |
| 20 | SupplierItemPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 21 | SupplierItemPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 22 | SupplierItemPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 23 | SupplierItemPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 24 | SupplierItemPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 25 | SupplierItemPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 26 | SupplierItemPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 27 | SupplierItemPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 28 | SupplierItemPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 29 | SupplierItemPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 30 | SupplierItemPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 31 | SupplierItemPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 32 | SupplierItemPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 33 | SupplierItemPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 34 | SupplierItemPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 35 | SupplierItemPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 36 | SupplierItemPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 37 | SupplierItemPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 38 | SupplierItemPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 39 | SupplierItemPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 40 | SupplierItemPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 41 | SupplierItemPEOCreatedBy | CREATED_BY | — | — |
| 42 | SupplierItemPEOCreatedFromTpiId | CREATED_FROM_TPI_ID | — | — |
| 43 | SupplierItemPEOCreationDate | CREATION_DATE | — | — |
| 44 | SupplierItemPEOEndDate | END_DATE | — | ✅ |
| 45 | SupplierItemPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 46 | SupplierItemPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 47 | SupplierItemPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 48 | SupplierItemPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 49 | SupplierItemPEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 50 | SupplierItemPEOProgramName | PROGRAM_NAME | — | — |
| 51 | SupplierItemPEORequestId | REQUEST_ID | — | — |
| 52 | SupplierItemPEOStartDate | START_DATE | — | ✅ |
| 53 | SupplierItemPEOTpItemDesc | TP_ITEM_DESC | — | ✅ |
| 54 | SupplierItemPEOTpItemId | TP_ITEM_ID | 🔑 | ✅ |
| 55 | SupplierItemPEOTpItemNumber | TP_ITEM_NUMBER | — | ✅ |
| 56 | SupplierItemPEOTpType | TP_TYPE | — | ✅ |
| 57 | SupplierItemPEOTradingPartnerId | TRADING_PARTNER_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
