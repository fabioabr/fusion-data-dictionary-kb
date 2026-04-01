---
id: DOC-OTHER-PVO-VcsHistSupplyForecastExtractPVO
doc_type: system-doc
title: "VcsHistSupplyForecastExtractPVO — PVO Cross-Module"
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
  - VcsHistSupplyForecastExtractPVO
  - vcshistsupplyforecastextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# VcsHistSupplyForecastExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Vcs Hist Supply Forecast Extract. Acessa as tabelas: VCS_COLLAB_ENT_HIST, VCS_COLLAB_SOURCE, VCS_PARTICIPANTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.VcsBiccExtractAM.VcsHistSupplyForecastExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 61 | 3 | 4 | 61 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[vcs_collab_ent_hist|VCS_COLLAB_ENT_HIST]] — 47 atributos (1 PKs, 47 BICC)
- [[vcs_collab_source|VCS_COLLAB_SOURCE]] — 3 atributos (1 PKs, 3 BICC)
- [[vcs_participants|VCS_PARTICIPANTS]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[vcs_collab_ent_hist|VCS_COLLAB_ENT_HIST]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | VcsHistSupplyForecastPEOCmOnHandPublishedByPartyCode | CM_ON_HAND_PUB_BY_PARTY | — | ✅ |
| 2 | VcsHistSupplyForecastPEOCmOnHandPublishedByPersonId | CM_ON_HAND_PUB_BY | — | ✅ |
| 3 | VcsHistSupplyForecastPEOCmOnHandPublishedDate | CM_ON_HAND_PUB_DATE | — | ✅ |
| 4 | VcsHistSupplyForecastPEOCmOnHandQuantity | CM_ON_HAND_QTY | — | ✅ |
| 5 | VcsHistSupplyForecastPEOCollaborationEntryVersion | COLLAB_ENTRY_VERSION | — | ✅ |
| 6 | VcsHistSupplyForecastPEOCollaborationIdentityId | COLLAB_IDENTITY_ID | — | ✅ |
| 7 | VcsHistSupplyForecastPEOCollaborationOrderForecastEntryId | ENTRY_ID | 🔑 | ✅ |
| 8 | VcsHistSupplyForecastPEOCollaborationOrderForecastEntryTypeId | ENTRY_TYPE_ID | — | ✅ |
| 9 | VcsHistSupplyForecastPEOCollaborationSourceId | COLLAB_SOURCE_ID | — | ✅ |
| 10 | VcsHistSupplyForecastPEOCollaborationUOMCode | COLLAB_UOM | — | ✅ |
| 11 | VcsHistSupplyForecastPEOCommitDate | COMMIT_DATE | — | ✅ |
| 12 | VcsHistSupplyForecastPEOCommitDueDate | COMMIT_DUE_DATE | — | ✅ |
| 13 | VcsHistSupplyForecastPEOCommitHorizonEndDate | COMMIT_HORIZON_END_DATE | — | ✅ |
| 14 | VcsHistSupplyForecastPEOCommitTotalQuantity | COMMIT_HORIZON_CQTY | — | ✅ |
| 15 | VcsHistSupplyForecastPEOCommittedByPartyCode | COMMITTED_BY_PARTY | — | ✅ |
| 16 | VcsHistSupplyForecastPEOCommittedByPersonId | COMMITTED_BY | — | ✅ |
| 17 | VcsHistSupplyForecastPEOCorrelationCode | ORCH_CORRELATION_CODE | — | ✅ |
| 18 | VcsHistSupplyForecastPEOCreatedBy | CREATED_BY | — | ✅ |
| 19 | VcsHistSupplyForecastPEOCreationDate | CREATION_DATE | — | ✅ |
| 20 | VcsHistSupplyForecastPEOForecastHorizonEndDate | FORECAST_HORIZON_END_DATE | — | ✅ |
| 21 | VcsHistSupplyForecastPEOForecastTotalCommitHorizonQuantity | COMMIT_HORIZON_FQTY | — | ✅ |
| 22 | VcsHistSupplyForecastPEOForecastTotalForecastHorizonQuantity | FORECAST_HORIZON_FQTY | — | ✅ |
| 23 | VcsHistSupplyForecastPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 24 | VcsHistSupplyForecastPEOInventoryItemOrganizationId | INVENTORY_ITEM_ORG_ID | — | ✅ |
| 25 | VcsHistSupplyForecastPEOLastPublishedPlanName | LAST_PUBLISHED_PLAN_NAME | — | ✅ |
| 26 | VcsHistSupplyForecastPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 27 | VcsHistSupplyForecastPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 28 | VcsHistSupplyForecastPEOMaxCommitVersion | MAX_COMMIT_VERSION | — | ✅ |
| 29 | VcsHistSupplyForecastPEOMaxForecastVersion | MAX_FORECAST_VERSION | — | ✅ |
| 30 | VcsHistSupplyForecastPEONoteToPlanner | NOTE_TO_PLANNER | — | ✅ |
| 31 | VcsHistSupplyForecastPEONoteToSupplier | NOTE_TO_SUPPLIER | — | ✅ |
| 32 | VcsHistSupplyForecastPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 33 | VcsHistSupplyForecastPEOPublishCycleEndDate | PUBLISH_CYCLE_END_DATE | — | ✅ |
| 34 | VcsHistSupplyForecastPEOPublishCycleStartDate | PUBLISH_CYCLE_START_DATE | — | ✅ |
| 35 | VcsHistSupplyForecastPEOPublishedByPartyCode | PUBLISH_BY_PARTY | — | ✅ |
| 36 | VcsHistSupplyForecastPEOPublishedByPersonId | PUBLISHED_BY | — | ✅ |
| 37 | VcsHistSupplyForecastPEOPublishedDate | PUBLISHED_DATE | — | ✅ |
| 38 | VcsHistSupplyForecastPEOPublishedOnHandQuantity | PUBLISHED_ON_HAND_QTY | — | ✅ |
| 39 | VcsHistSupplyForecastPEOShipFromId | SHIP_FROM_ID | — | ✅ |
| 40 | VcsHistSupplyForecastPEOShipToId | SHIP_TO_ID | — | ✅ |
| 41 | VcsHistSupplyForecastPEOSlaDays | SLA_DAYS | — | ✅ |
| 42 | VcsHistSupplyForecastPEOStatusCode | STATUS_CODE | — | ✅ |
| 43 | VcsHistSupplyForecastPEOSupplierOnHandPublishedByPartyCode | SUPPLIER_ON_HAND_PUB_BY_PARTY | — | ✅ |
| 44 | VcsHistSupplyForecastPEOSupplierOnHandPublishedByPersonId | SUPPLIER_ON_HAND_PUB_BY | — | ✅ |
| 45 | VcsHistSupplyForecastPEOSupplierOnHandPublishedDate | SUPPLIER_ON_HAND_PUB_DATE | — | ✅ |
| 46 | VcsHistSupplyForecastPEOSupplierOnHandQuantity | SUPPLIER_ON_HAND_QTY | — | ✅ |
| 47 | VcsHistSupplyForecastPEOUOMCode | PRIMARY_UOM_CODE | — | ✅ |

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
| 6 | VcsCollabPartShipFromPEOShipToCustomerId | CUSTOMER_ID | — | ✅ |
| 7 | VcsCollabPartShipToPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | VcsCollabPartShipToPEOPartnerCode | PARTNER_CODE | — | ✅ |
| 9 | VcsCollabPartShipToPEOShipToCustomerSiteId | CUSTOMER_SITE_ID | — | ✅ |
| 10 | VcsCollabPartShipToPEOShipToOrganizationId | ORGANIZATION_ID | — | ✅ |
| 11 | VcsCollabPartShipToPEOShipToVcsParticipantId | VCS_PARTICIPANT_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
