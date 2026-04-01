---
id: DOC-OTHER-PVO-ItemRelShipRelatedItemNonPendRev
doc_type: system-doc
title: "ItemRelShipRelatedItemNonPendRev — PVO Cross-Module"
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
  - ItemRelShipRelatedItemNonPendRev
  - itemrelshiprelateditemnonpendrev
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ItemRelShipRelatedItemNonPendRev

## 📌 Visão Geral

View Object para extração BICC de dados de Item Rel Ship Related Item Non Pend Rev. Acessa as tabelas: EGO_ITEM_ASSOCIATIONS, EGP_ITEM_RELATIONSHIPS_B_V, EGP_ITEM_RELATIONSHIPS_TL (+3).

**Caminho:** `FscmTopModelAM.EgpItemsPublicModelAM.ItemRelShipRelatedItemNonPendRev`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 102 | 6 | 1 | 72 | 71% |

---

## 🔗 Tabelas Relacionadas

- [[ego_item_associations|EGO_ITEM_ASSOCIATIONS]] — 38 atributos (9 BICC)
- [[egp_item_relationships_b_v|EGP_ITEM_RELATIONSHIPS_B_V]] — 45 atributos (1 PKs, 44 BICC)
- [[egp_item_relationships_tl|EGP_ITEM_RELATIONSHIPS_TL]] — 10 atributos (10 BICC)
- [[egp_item_revisions_vl|EGP_ITEM_REVISIONS_VL]] — 3 atributos (3 BICC)
- [[egp_system_items_vl|EGP_SYSTEM_ITEMS_VL]] — 4 atributos (4 BICC)
- [[hz_parties|HZ_PARTIES]] — 2 atributos (2 BICC)

---

## ⚙️ Atributos

### [[ego_item_associations|EGO_ITEM_ASSOCIATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemSupplierAssociationPEOAcdType | ACD_TYPE | — | ✅ |
| 2 | ItemSupplierAssociationPEOAssociationId | ASSOCIATION_ID | — | — |
| 3 | ItemSupplierAssociationPEOChangeBitMap | CHANGE_BIT_MAP | — | — |
| 4 | ItemSupplierAssociationPEOChangeLineId | CHANGE_LINE_ID | — | ✅ |
| 5 | ItemSupplierAssociationPEOImplementationDate | IMPLEMENTATION_DATE | — | — |
| 6 | ItemSupplierAssociationPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 7 | ItemSupplierAssociationPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 8 | ItemSupplierAssociationPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 9 | ItemSupplierAssociationPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 10 | ItemSupplierAssociationPEOPartyStatus | PARTY_STATUS | — | — |
| 11 | ItemSupplierAssociationPEOPrimaryFlag | PRIMARY_FLAG | — | ✅ |
| 12 | ItemSupplierAssociationPEORequestId | REQUEST_ID | — | — |
| 13 | ItemSupplierAssociationPEOStatusCode | STATUS_CODE | — | ✅ |
| 14 | ItemSupplierAssociationPEOStyleItemId | STYLE_ITEM_ID | — | — |
| 15 | ItemSupplierAssociationPEOSupplierId | SUPPLIER_ID | — | ✅ |
| 16 | ItemSupplierAssociationPEOSupplierSiteId | SUPPLIER_SITE_ID | — | ✅ |
| 17 | ItemSupplierAssociationPEOVersionEndDate | VERSION_END_DATE | — | — |
| 18 | ItemSupplierAssociationPEOVersionId | VERSION_ID | — | ✅ |
| 19 | ItemSupplierAssociationPEOVersionStartDate | VERSION_START_DATE | — | — |
| 20 | ToItemSupplierAssociationPEOAcdType | ACD_TYPE | — | — |
| 21 | ToItemSupplierAssociationPEOAssociationId | ASSOCIATION_ID | — | — |
| 22 | ToItemSupplierAssociationPEOChangeBitMap | CHANGE_BIT_MAP | — | — |
| 23 | ToItemSupplierAssociationPEOChangeLineId | CHANGE_LINE_ID | — | — |
| 24 | ToItemSupplierAssociationPEOImplementationDate | IMPLEMENTATION_DATE | — | — |
| 25 | ToItemSupplierAssociationPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 26 | ToItemSupplierAssociationPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 27 | ToItemSupplierAssociationPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 28 | ToItemSupplierAssociationPEOOrganizationId | ORGANIZATION_ID | — | — |
| 29 | ToItemSupplierAssociationPEOPartyStatus | PARTY_STATUS | — | — |
| 30 | ToItemSupplierAssociationPEOPrimaryFlag | PRIMARY_FLAG | — | — |
| 31 | ToItemSupplierAssociationPEORequestId | REQUEST_ID | — | — |
| 32 | ToItemSupplierAssociationPEOStatusCode | STATUS_CODE | — | — |
| 33 | ToItemSupplierAssociationPEOStyleItemId | STYLE_ITEM_ID | — | — |
| 34 | ToItemSupplierAssociationPEOSupplierId | SUPPLIER_ID | — | — |
| 35 | ToItemSupplierAssociationPEOSupplierSiteId | SUPPLIER_SITE_ID | — | — |
| 36 | ToItemSupplierAssociationPEOVersionEndDate | VERSION_END_DATE | — | — |
| 37 | ToItemSupplierAssociationPEOVersionId | VERSION_ID | — | — |
| 38 | ToItemSupplierAssociationPEOVersionStartDate | VERSION_START_DATE | — | — |

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
| 8 | ItemRelationshipBasePEODescription | DESCRIPTION | — | ✅ |
| 9 | ItemRelationshipBasePEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 10 | ItemRelationshipBasePEOEpcGtinSerial | EPC_GTIN_SERIAL | — | ✅ |
| 11 | ItemRelationshipBasePEOFirstArticleStatus | FIRST_ARTICLE_STATUS | — | ✅ |
| 12 | ItemRelationshipBasePEOImplementationDate | IMPLEMENTATION_DATE | — | ✅ |
| 13 | ItemRelationshipBasePEOInactiveFlag | INACTIVE_FLAG | — | ✅ |
| 14 | ItemRelationshipBasePEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 15 | ItemRelationshipBasePEOItemRelationshipType | ITEM_RELATIONSHIP_TYPE | — | ✅ |
| 16 | ItemRelationshipBasePEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 17 | ItemRelationshipBasePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 18 | ItemRelationshipBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 19 | ItemRelationshipBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 20 | ItemRelationshipBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 21 | ItemRelationshipBasePEOMasterOrganizationId | MASTER_ORGANIZATION_ID | — | ✅ |
| 22 | ItemRelationshipBasePEOMrpPlanningCode | MRP_PLANNING_CODE | — | ✅ |
| 23 | ItemRelationshipBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 24 | ItemRelationshipBasePEOOrgIndependentFlag | ORG_INDEPENDENT_FLAG | — | ✅ |
| 25 | ItemRelationshipBasePEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 26 | ItemRelationshipBasePEOPlanningEnabledFlag | PLANNING_ENABLED_FLAG | — | ✅ |
| 27 | ItemRelationshipBasePEOPreferenceNumber | PREFERENCE_NUMBER | — | ✅ |
| 28 | ItemRelationshipBasePEOProgramAppName | PROGRAM_APP_NAME | — | ✅ |
| 29 | ItemRelationshipBasePEOProgramName | PROGRAM_NAME | — | ✅ |
| 30 | ItemRelationshipBasePEOReciprocalFlag | RECIPROCAL_FLAG | — | ✅ |
| 31 | ItemRelationshipBasePEORelatedItemId | RELATED_ITEM_ID | — | ✅ |
| 32 | ItemRelationshipBasePEORelateditemRank | RELATEDITEM_RANK | — | ✅ |
| 33 | ItemRelationshipBasePEORelationshipRank | RELATIONSHIP_RANK | — | — |
| 34 | ItemRelationshipBasePEORequestId | REQUEST_ID | — | ✅ |
| 35 | ItemRelationshipBasePEORevisionId | REVISION_ID | — | ✅ |
| 36 | ItemRelationshipBasePEOSourceSystemId | SOURCE_SYSTEM_ID | — | ✅ |
| 37 | ItemRelationshipBasePEOStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 38 | ItemRelationshipBasePEOStatusCode | STATUS_CODE | — | ✅ |
| 39 | ItemRelationshipBasePEOSubType | SUB_TYPE | — | ✅ |
| 40 | ItemRelationshipBasePEOTpItemId | TP_ITEM_ID | — | ✅ |
| 41 | ItemRelationshipBasePEOUomCode | UOM_CODE | — | ✅ |
| 42 | ItemRelationshipBasePEOVersionEndDate | VERSION_END_DATE | — | ✅ |
| 43 | ItemRelationshipBasePEOVersionId | VERSION_ID | — | ✅ |
| 44 | ItemRelationshipBasePEOVersionStartDate | VERSION_START_DATE | — | ✅ |
| 45 | ItemRelationshipId | ITEM_RELATIONSHIP_ID | 🔑 | ✅ |

### [[egp_item_relationships_tl|EGP_ITEM_RELATIONSHIPS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemRelationshipTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | ItemRelationshipTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | ItemRelationshipTLPEODescription | DESCRIPTION | — | ✅ |
| 4 | ItemRelationshipTLPEOItemRelationshipId | ITEM_RELATIONSHIP_ID | — | ✅ |
| 5 | ItemRelationshipTLPEOLanguage | LANGUAGE | — | ✅ |
| 6 | ItemRelationshipTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ItemRelationshipTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | ItemRelationshipTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ItemRelationshipTLPEOSourceLang | SOURCE_LANG | — | ✅ |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |

### [[egp_item_revisions_vl|EGP_ITEM_REVISIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemRevisionPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 2 | ItemRevisionPEORevision | REVISION | — | ✅ |
| 3 | ItemRevisionPEORevisionId | REVISION_ID | — | ✅ |

### [[egp_system_items_vl|EGP_SYSTEM_ITEMS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemPEODescription | DESCRIPTION | — | ✅ |
| 2 | ItemPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 3 | ItemPEOItemNumber | ITEM_NUMBER | — | ✅ |
| 4 | ItemPEOOrganizationId | ORGANIZATION_ID | — | ✅ |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyPEOPartyId | PARTY_ID | — | ✅ |
| 2 | PartyPEOPartyName | PARTY_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
