---
id: DOC-OTHER-PVO-VcsDemandCollabIdentityExtractPVO
doc_type: system-doc
title: "VcsDemandCollabIdentityExtractPVO — PVO Cross-Module"
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
  - VcsDemandCollabIdentityExtractPVO
  - vcsdemandcollabidentityextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# VcsDemandCollabIdentityExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Vcs Demand Collab Identity Extract. Acessa as tabelas: VCS_DEMAND_COLLAB_IDENTITY.

**Caminho:** `FscmTopModelAM.ScmExtractAM.VcsDemandBiccExtractAM.VcsDemandCollabIdentityExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 26 | 1 | 1 | 26 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[vcs_demand_collab_identity|VCS_DEMAND_COLLAB_IDENTITY]] — 26 atributos (1 PKs, 26 BICC)

---

## ⚙️ Atributos

### [[vcs_demand_collab_identity|VCS_DEMAND_COLLAB_IDENTITY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DCDemandCollabIdentityPEOBaseItemUomCode | BASE_ITEM_UOM_CODE | — | ✅ |
| 2 | DCDemandCollabIdentityPEOCollaborationProfileId | COLLABORATION_PROFILE_ID | — | ✅ |
| 3 | DCDemandCollabIdentityPEOCollaborationUomCode | COLLABORATION_UOM_CODE | — | ✅ |
| 4 | DCDemandCollabIdentityPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | DCDemandCollabIdentityPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | DCDemandCollabIdentityPEOCustomerId | CUSTOMER_ID | — | ✅ |
| 7 | DCDemandCollabIdentityPEOCustomerLvlCode | CUSTOMER_LVL_CODE | — | ✅ |
| 8 | DCDemandCollabIdentityPEOCustomerName | CUSTOMER_NAME | — | ✅ |
| 9 | DCDemandCollabIdentityPEOCustomerNumber | CUSTOMER_NUMBER | — | ✅ |
| 10 | DCDemandCollabIdentityPEOCustomerSiteId | CUSTOMER_SITE_ID | — | ✅ |
| 11 | DCDemandCollabIdentityPEOCustomerSiteNumber | CUSTOMER_SITE_NUMBER | — | ✅ |
| 12 | DCDemandCollabIdentityPEODocumentTypeCode | DOCUMENT_TYPE_CODE | — | ✅ |
| 13 | DCDemandCollabIdentityPEOIdentityId | IDENTITY_ID | 🔑 | ✅ |
| 14 | DCDemandCollabIdentityPEOItemLvlCode | ITEM_LVL_CODE | — | ✅ |
| 15 | DCDemandCollabIdentityPEOItemLvlDescription | ITEM_LVL_DESCRIPTION | — | ✅ |
| 16 | DCDemandCollabIdentityPEOItemLvlId | ITEM_LVL_ID | — | ✅ |
| 17 | DCDemandCollabIdentityPEOItemLvlValue | ITEM_LVL_VALUE | — | ✅ |
| 18 | DCDemandCollabIdentityPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 19 | DCDemandCollabIdentityPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 20 | DCDemandCollabIdentityPEOLocationCode | LOCATION_CODE | — | ✅ |
| 21 | DCDemandCollabIdentityPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 22 | DCDemandCollabIdentityPEOOrganizationLvlCode | ORGANIZATION_LVL_CODE | — | ✅ |
| 23 | DCDemandCollabIdentityPEOOrganizationLvlId | ORGANIZATION_LVL_ID | — | ✅ |
| 24 | DCDemandCollabIdentityPEOOrganizationLvlValue | ORGANIZATION_LVL_VALUE | — | ✅ |
| 25 | DCDemandCollabIdentityPEOPublishUomCode | PUB_UOM_CODE | — | ✅ |
| 26 | DCDemandCollabIdentityPEOStatusCode | STATUS_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
