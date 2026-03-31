---
id: DOC-OTHER-PVO-VcsSupplyForecastExtractPVO
doc_type: system-doc
title: "VcsSupplyForecastExtractPVO — PVO Cross-Module"
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
  - VcsSupplyForecastExtractPVO
  - vcssupplyforecastextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# VcsSupplyForecastExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Vcs Supply Forecast Extract. Acessa as tabelas: VCS_COLLAB_ENT, VCS_COLLAB_SOURCE, VCS_PARTICIPANTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.VcsBiccExtractAM.VcsSupplyForecastExtractPVO`

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
| 1 | VcsSupplyForecastPEOAutoCommitPercentFactor | COMMIT_PERCENT_FACTOR | — | ✅ |
| 2 | VcsSupplyForecastPEOAutoCommitPeriodCode | AUTO_COMMIT_PERIOD_CODE | — | ✅ |
| 3 | VcsSupplyForecastPEOAutoCommitPeriodFactor | AUTO_COMMIT_PERIOD_FACTOR | — | ✅ |
| 4 | VcsSupplyForecastPEOBaseUomCode | BASE_UOM_CODE | — | ✅ |
| 5 | VcsSupplyForecastPEOCmOnHandPublishedByPartyCode | CM_ON_HAND_PUB_BY_PARTY | — | ✅ |
| 6 | VcsSupplyForecastPEOCmOnHandPublishedByPersonId | CM_ON_HAND_PUB_BY | — | ✅ |
| 7 | VcsSupplyForecastPEOCmOnHandPublishedDate | CM_ON_HAND_PUB_DATE | — | ✅ |
| 8 | VcsSupplyForecastPEOCmOnHandQuantity | CM_ON_HAND_QTY | — | ✅ |
| 9 | VcsSupplyForecastPEOCollaborationEntryVersion | COLLAB_ENTRY_VERSION | — | ✅ |
| 10 | VcsSupplyForecastPEOCollaborationIdentityId | COLLAB_IDENTITY_ID | — | ✅ |
| 11 | VcsSupplyForecastPEOCollaborationOrderForecastEntryId | ENTRY_ID | 🔑 | ✅ |
| 12 | VcsSupplyForecastPEOCollaborationOrderForecastEntryTypeId | ENTRY_TYPE_ID | — | ✅ |
| 13 | VcsSupplyForecastPEOCollaborationSourceId | COLLAB_SOURCE_ID | — | ✅ |
| 14 | VcsSupplyForecastPEOCollaborationUomSourceCode | COLLAB_UOM_SOURCE_CODE | — | ✅ |
| 15 | VcsSupplyForecastPEOCommitDate | COMMIT_DATE | — | ✅ |
| 16 | VcsSupplyForecastPEOCommitDetailLastUpdatedByEnterprise | DETAIL_LAST_UPDATE_ENT | — | ✅ |
| 17 | VcsSupplyForecastPEOCommitDetailLastUpdatedBySupplier | DETAIL_LAST_UPDATE_SUP | — | ✅ |
| 18 | VcsSupplyForecastPEOCommitDueDate | COMMIT_DUE_DATE | — | ✅ |
| 19 | VcsSupplyForecastPEOCommitHorizonEndDate | COMMIT_HORIZON_END_DATE | — | ✅ |
| 20 | VcsSupplyForecastPEOCommitQuantityPreferenceCode | COMMIT_QUANTITY_PREF_CODE | — | ✅ |
| 21 | VcsSupplyForecastPEOCommitTotalQuantity | COMMIT_HORIZON_CQTY | — | ✅ |
| 22 | VcsSupplyForecastPEOCommittedByPartyCode | COMMITTED_BY_PARTY | — | ✅ |
| 23 | VcsSupplyForecastPEOCommittedByPersonId | COMMITTED_BY | — | ✅ |
| 24 | VcsSupplyForecastPEOCorrelationCode | ORCH_CORRELATION_CODE | — | ✅ |
| 25 | VcsSupplyForecastPEOCreatedBy | CREATED_BY | — | ✅ |
| 26 | VcsSupplyForecastPEOCreationDate | CREATION_DATE | — | ✅ |
| 27 | VcsSupplyForecastPEODropShipFlag | DROP_SHIP_FLAG | — | ✅ |
| 28 | VcsSupplyForecastPEOEnterpriseDraftQtyFlag | ENT_DRAFT_QTY_FLAG | — | ✅ |
| 29 | VcsSupplyForecastPEOExternalReferenceFlag | EXTERNAL_REFERENCE_FLAG | — | ✅ |
| 30 | VcsSupplyForecastPEOForecastDetailLastUpdateEnterprise | DETAIL_LAST_UPDATE_FRCST_ENT | — | ✅ |
| 31 | VcsSupplyForecastPEOForecastDetailLastUpdateSupplier | DETAIL_LAST_UPDATE_FRCST_SUP | — | ✅ |
| 32 | VcsSupplyForecastPEOForecastHorizonEndDate | FORECAST_HORIZON_END_DATE | — | ✅ |
| 33 | VcsSupplyForecastPEOForecastTotalCommitHorizonQuantity | COMMIT_HORIZON_FQTY | — | ✅ |
| 34 | VcsSupplyForecastPEOForecastTotalForecastHorizonQuantity | FORECAST_HORIZON_FQTY | — | ✅ |
| 35 | VcsSupplyForecastPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 36 | VcsSupplyForecastPEOInventoryItemOrganizationId | INVENTORY_ITEM_ORG_ID | — | ✅ |
| 37 | VcsSupplyForecastPEOIsCurrentFlag | IS_CURRENT_FLAG | — | ✅ |
| 38 | VcsSupplyForecastPEOIsManagedFlag | IS_MANAGED_FLAG | — | ✅ |
| 39 | VcsSupplyForecastPEOLastPublishedPlanName | LAST_PUBLISHED_PLAN_NAME | — | ✅ |
| 40 | VcsSupplyForecastPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 41 | VcsSupplyForecastPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 42 | VcsSupplyForecastPEOMaxCommitVersion | MAX_COMMIT_VERSION | — | ✅ |
| 43 | VcsSupplyForecastPEOMaxForecastVersion | MAX_FORECAST_VERSION | — | ✅ |
| 44 | VcsSupplyForecastPEONoteToPlanner | NOTE_TO_PLANNER | — | ✅ |
| 45 | VcsSupplyForecastPEONoteToSupplier | NOTE_TO_SUPPLIER | — | ✅ |
| 46 | VcsSupplyForecastPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 47 | VcsSupplyForecastPEOPublishCycleEndDate | PUBLISH_CYCLE_END_DATE | — | ✅ |
| 48 | VcsSupplyForecastPEOPublishCycleStartDate | PUBLISH_CYCLE_START_DATE | — | ✅ |
| 49 | VcsSupplyForecastPEOPublishedByPartyCode | PUBLISH_BY_PARTY | — | ✅ |
| 50 | VcsSupplyForecastPEOPublishedByPersonId | PUBLISHED_BY | — | ✅ |
| 51 | VcsSupplyForecastPEOPublishedDate | PUBLISHED_DATE | — | ✅ |
| 52 | VcsSupplyForecastPEOPublishedOnHandQuantity | PUBLISHED_ON_HAND_QTY | — | ✅ |
| 53 | VcsSupplyForecastPEOPublishedUomCode | PUBLISHED_UOM_CODE | — | ✅ |
| 54 | VcsSupplyForecastPEOShipFromId | SHIP_FROM_ID | — | ✅ |
| 55 | VcsSupplyForecastPEOShipToId | SHIP_TO_ID | — | ✅ |
| 56 | VcsSupplyForecastPEOSlaDays | SLA_DAYS | — | ✅ |
| 57 | VcsSupplyForecastPEOSlaPastDueActionCode | SLA_PAST_DUE_ACTION_CODE | — | ✅ |
| 58 | VcsSupplyForecastPEOStatusCode | STATUS_CODE | — | ✅ |
| 59 | VcsSupplyForecastPEOSupplierDraftQtyFlag | SUP_DRAFT_QTY_FLAG | — | ✅ |
| 60 | VcsSupplyForecastPEOSupplierOnHandPublishedByPartyCode | SUPPLIER_ON_HAND_PUB_BY_PARTY | — | ✅ |
| 61 | VcsSupplyForecastPEOSupplierOnHandPublishedByPersonId | SUPPLIER_ON_HAND_PUB_BY | — | ✅ |
| 62 | VcsSupplyForecastPEOSupplierOnHandPublishedDate | SUPPLIER_ON_HAND_PUB_DATE | — | ✅ |
| 63 | VcsSupplyForecastPEOSupplierOnHandQuantity | SUPPLIER_ON_HAND_QTY | — | ✅ |
| 64 | VcsSupplyForecastPEOTimeLevel | TIME_LEVEL | — | ✅ |
| 65 | VcsSupplyForecastPEOUOMCode | PRIMARY_UOM_CODE | — | ✅ |

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
