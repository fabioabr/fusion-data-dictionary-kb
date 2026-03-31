---
id: DOC-OTHER-PVO-VcsExtSupplyForecastExtractPVO
doc_type: system-doc
title: "VcsExtSupplyForecastExtractPVO — PVO Cross-Module"
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
  - VcsExtSupplyForecastExtractPVO
  - vcsextsupplyforecastextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# VcsExtSupplyForecastExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Vcs Ext Supply Forecast Extract. Acessa as tabelas: VCS_COLLAB_ENT, VCS_COLLAB_SOURCE, VCS_PARTICIPANTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.VcsBiccExtractAM.VcsExtSupplyForecastExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 79 | 3 | 4 | 79 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[vcs_collab_ent|VCS_COLLAB_ENT]] — 65 atributos (1 PKs, 65 BICC)
- [[vcs_collab_source|VCS_COLLAB_SOURCE]] — 3 atributos (1 PKs, 3 BICC)
- [[vcs_participants|VCS_PARTICIPANTS]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[vcs_collab_ent|VCS_COLLAB_ENT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | VcsExtSupplyForecastPEOAutoCommitPercentFactor | COMMIT_PERCENT_FACTOR | — | ✅ |
| 2 | VcsExtSupplyForecastPEOAutoCommitPeriodCode | AUTO_COMMIT_PERIOD_CODE | — | ✅ |
| 3 | VcsExtSupplyForecastPEOAutoCommitPeriodFactor | AUTO_COMMIT_PERIOD_FACTOR | — | ✅ |
| 4 | VcsExtSupplyForecastPEOBaseUomCode | BASE_UOM_CODE | — | ✅ |
| 5 | VcsExtSupplyForecastPEOCmOnHandPublishedByPartyCode | CM_ON_HAND_PUB_BY_PARTY | — | ✅ |
| 6 | VcsExtSupplyForecastPEOCmOnHandPublishedByPersonId | CM_ON_HAND_PUB_BY | — | ✅ |
| 7 | VcsExtSupplyForecastPEOCmOnHandPublishedDate | CM_ON_HAND_PUB_DATE | — | ✅ |
| 8 | VcsExtSupplyForecastPEOCmOnHandQuantity | CM_ON_HAND_QTY | — | ✅ |
| 9 | VcsExtSupplyForecastPEOCollaborationEntryVersion | COLLAB_ENTRY_VERSION | — | ✅ |
| 10 | VcsExtSupplyForecastPEOCollaborationIdentityId | COLLAB_IDENTITY_ID | — | ✅ |
| 11 | VcsExtSupplyForecastPEOCollaborationOrderForecastEntryId | ENTRY_ID | 🔑 | ✅ |
| 12 | VcsExtSupplyForecastPEOCollaborationOrderForecastEntryTypeId | ENTRY_TYPE_ID | — | ✅ |
| 13 | VcsExtSupplyForecastPEOCollaborationSourceId | COLLAB_SOURCE_ID | — | ✅ |
| 14 | VcsExtSupplyForecastPEOCollaborationUomSourceCode | COLLAB_UOM_SOURCE_CODE | — | ✅ |
| 15 | VcsExtSupplyForecastPEOCommitDate | COMMIT_DATE | — | ✅ |
| 16 | VcsExtSupplyForecastPEOCommitDetailLastUpdatedByEnterprise | DETAIL_LAST_UPDATE_ENT | — | ✅ |
| 17 | VcsExtSupplyForecastPEOCommitDetailLastUpdatedBySupplier | DETAIL_LAST_UPDATE_SUP | — | ✅ |
| 18 | VcsExtSupplyForecastPEOCommitDueDate | COMMIT_DUE_DATE | — | ✅ |
| 19 | VcsExtSupplyForecastPEOCommitHorizonEndDate | COMMIT_HORIZON_END_DATE | — | ✅ |
| 20 | VcsExtSupplyForecastPEOCommitQuantityPreferenceCode | COMMIT_QUANTITY_PREF_CODE | — | ✅ |
| 21 | VcsExtSupplyForecastPEOCommitTotalQuantity | COMMIT_HORIZON_CQTY | — | ✅ |
| 22 | VcsExtSupplyForecastPEOCommittedByPartyCode | COMMITTED_BY_PARTY | — | ✅ |
| 23 | VcsExtSupplyForecastPEOCommittedByPersonId | COMMITTED_BY | — | ✅ |
| 24 | VcsExtSupplyForecastPEOCorrelationCode | ORCH_CORRELATION_CODE | — | ✅ |
| 25 | VcsExtSupplyForecastPEOCreatedBy | CREATED_BY | — | ✅ |
| 26 | VcsExtSupplyForecastPEOCreationDate | CREATION_DATE | — | ✅ |
| 27 | VcsExtSupplyForecastPEODropShipFlag | DROP_SHIP_FLAG | — | ✅ |
| 28 | VcsExtSupplyForecastPEOEnterpriseDraftQtyFlag | ENT_DRAFT_QTY_FLAG | — | ✅ |
| 29 | VcsExtSupplyForecastPEOExternalReferenceFlag | EXTERNAL_REFERENCE_FLAG | — | ✅ |
| 30 | VcsExtSupplyForecastPEOForecastDetailLastUpdateEnterprise | DETAIL_LAST_UPDATE_FRCST_ENT | — | ✅ |
| 31 | VcsExtSupplyForecastPEOForecastDetailLastUpdateSupplier | DETAIL_LAST_UPDATE_FRCST_SUP | — | ✅ |
| 32 | VcsExtSupplyForecastPEOForecastHorizonEndDate | FORECAST_HORIZON_END_DATE | — | ✅ |
| 33 | VcsExtSupplyForecastPEOForecastTotalCommitHorizonQuantity | COMMIT_HORIZON_FQTY | — | ✅ |
| 34 | VcsExtSupplyForecastPEOForecastTotalForecastHorizonQuantity | FORECAST_HORIZON_FQTY | — | ✅ |
| 35 | VcsExtSupplyForecastPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 36 | VcsExtSupplyForecastPEOInventoryItemOrganizationId | INVENTORY_ITEM_ORG_ID | — | ✅ |
| 37 | VcsExtSupplyForecastPEOIsCurrentFlag | IS_CURRENT_FLAG | — | ✅ |
| 38 | VcsExtSupplyForecastPEOIsManagedFlag | IS_MANAGED_FLAG | — | ✅ |
| 39 | VcsExtSupplyForecastPEOLastPublishedPlanName | LAST_PUBLISHED_PLAN_NAME | — | ✅ |
| 40 | VcsExtSupplyForecastPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 41 | VcsExtSupplyForecastPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 42 | VcsExtSupplyForecastPEOMaxCommitVersion | MAX_COMMIT_VERSION | — | ✅ |
| 43 | VcsExtSupplyForecastPEOMaxForecastVersion | MAX_FORECAST_VERSION | — | ✅ |
| 44 | VcsExtSupplyForecastPEONoteToPlanner | NOTE_TO_PLANNER | — | ✅ |
| 45 | VcsExtSupplyForecastPEONoteToSupplier | NOTE_TO_SUPPLIER | — | ✅ |
| 46 | VcsExtSupplyForecastPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 47 | VcsExtSupplyForecastPEOPublishCycleEndDate | PUBLISH_CYCLE_END_DATE | — | ✅ |
| 48 | VcsExtSupplyForecastPEOPublishCycleStartDate | PUBLISH_CYCLE_START_DATE | — | ✅ |
| 49 | VcsExtSupplyForecastPEOPublishedByPartyCode | PUBLISH_BY_PARTY | — | ✅ |
| 50 | VcsExtSupplyForecastPEOPublishedByPersonId | PUBLISHED_BY | — | ✅ |
| 51 | VcsExtSupplyForecastPEOPublishedDate | PUBLISHED_DATE | — | ✅ |
| 52 | VcsExtSupplyForecastPEOPublishedOnHandQuantity | PUBLISHED_ON_HAND_QTY | — | ✅ |
| 53 | VcsExtSupplyForecastPEOPublishedUomCode | PUBLISHED_UOM_CODE | — | ✅ |
| 54 | VcsExtSupplyForecastPEOShipFromId | SHIP_FROM_ID | — | ✅ |
| 55 | VcsExtSupplyForecastPEOShipToId | SHIP_TO_ID | — | ✅ |
| 56 | VcsExtSupplyForecastPEOSlaDays | SLA_DAYS | — | ✅ |
| 57 | VcsExtSupplyForecastPEOSlaPastDueActionCode | SLA_PAST_DUE_ACTION_CODE | — | ✅ |
| 58 | VcsExtSupplyForecastPEOStatusCode | STATUS_CODE | — | ✅ |
| 59 | VcsExtSupplyForecastPEOSupplierDraftQtyFlag | SUP_DRAFT_QTY_FLAG | — | ✅ |
| 60 | VcsExtSupplyForecastPEOSupplierOnHandPublishedByPartyCode | SUPPLIER_ON_HAND_PUB_BY_PARTY | — | ✅ |
| 61 | VcsExtSupplyForecastPEOSupplierOnHandPublishedByPersonId | SUPPLIER_ON_HAND_PUB_BY | — | ✅ |
| 62 | VcsExtSupplyForecastPEOSupplierOnHandPublishedDate | SUPPLIER_ON_HAND_PUB_DATE | — | ✅ |
| 63 | VcsExtSupplyForecastPEOSupplierOnHandQuantity | SUPPLIER_ON_HAND_QTY | — | ✅ |
| 64 | VcsExtSupplyForecastPEOUOMCode | PRIMARY_UOM_CODE | — | ✅ |
| 65 | VcsSupplyForecastPEOTimeLevel | TIME_LEVEL | — | ✅ |

### [[vcs_collab_source|VCS_COLLAB_SOURCE]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | VcsCollaborationPlanPEOCollaborationSourceId | COLLAB_SOURCE_ID | 🔑 | ✅ |
| 2 | VcsCollaborationPlanPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 3 | VcsCollaborationPlanPEOScenarioId | SCENARIO_ID | — | ✅ |

### [[vcs_participants|VCS_PARTICIPANTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | VcsCollabPartShipFromPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 2 | VcsCollabPartShipFromPEOShipFromOrganizationId | ORGANIZATION_ID | — | ✅ |
| 3 | VcsCollabPartShipFromPEOShipFromSupplierId | VENDOR_ID | — | ✅ |
| 4 | VcsCollabPartShipFromPEOShipFromSupplierSiteId | VENDOR_SITE_ID | — | ✅ |
| 5 | VcsCollabPartShipFromPEOShipFromVcsParticipantId | VCS_PARTICIPANT_ID | 🔑 | ✅ |
| 6 | VcsCollabPartShipToPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 7 | VcsCollabPartShipToPEOPartnerCode | PARTNER_CODE | — | ✅ |
| 8 | VcsCollabPartShipToPEOShipToCustomerId | CUSTOMER_ID | — | ✅ |
| 9 | VcsCollabPartShipToPEOShipToCustomerSiteId | CUSTOMER_SITE_ID | — | ✅ |
| 10 | VcsCollabPartShipToPEOShipToOrganizationId | ORGANIZATION_ID | — | ✅ |
| 11 | VcsCollabPartShipToPEOShipToVcsParticipantId | VCS_PARTICIPANT_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
