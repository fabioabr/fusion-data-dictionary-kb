---
id: DOC-OTHER-PVO-VcsExtHistSupplyForecastExtractPVO
doc_type: system-doc
title: "VcsExtHistSupplyForecastExtractPVO — PVO Cross-Module"
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
  - VcsExtHistSupplyForecastExtractPVO
  - vcsexthistsupplyforecastextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# VcsExtHistSupplyForecastExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Vcs Ext Hist Supply Forecast Extract. Acessa as tabelas: VCS_COLLAB_ENT_HIST, VCS_COLLAB_SOURCE, VCS_PARTICIPANTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.VcsBiccExtractAM.VcsExtHistSupplyForecastExtractPVO`

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
| 1 | VcsExtHistSupplyForecastPEOCmOnHandPublishedByPartyCode | CM_ON_HAND_PUB_BY_PARTY | — | ✅ |
| 2 | VcsExtHistSupplyForecastPEOCmOnHandPublishedByPersonId | CM_ON_HAND_PUB_BY | — | ✅ |
| 3 | VcsExtHistSupplyForecastPEOCmOnHandPublishedDate | CM_ON_HAND_PUB_DATE | — | ✅ |
| 4 | VcsExtHistSupplyForecastPEOCmOnHandQuantity | CM_ON_HAND_QTY | — | ✅ |
| 5 | VcsExtHistSupplyForecastPEOCollaborationEntryVersion | COLLAB_ENTRY_VERSION | — | ✅ |
| 6 | VcsExtHistSupplyForecastPEOCollaborationOrderForecastCollabIdentityId | COLLAB_IDENTITY_ID | — | ✅ |
| 7 | VcsExtHistSupplyForecastPEOCollaborationOrderForecastEntryId | ENTRY_ID | 🔑 | ✅ |
| 8 | VcsExtHistSupplyForecastPEOCollaborationOrderForecastEntryTypeId | ENTRY_TYPE_ID | — | ✅ |
| 9 | VcsExtHistSupplyForecastPEOCollaborationSourceId | COLLAB_SOURCE_ID | — | ✅ |
| 10 | VcsExtHistSupplyForecastPEOCollaborationUOMCode | COLLAB_UOM | — | ✅ |
| 11 | VcsExtHistSupplyForecastPEOCommitDate | COMMIT_DATE | — | ✅ |
| 12 | VcsExtHistSupplyForecastPEOCommitDueDate | COMMIT_DUE_DATE | — | ✅ |
| 13 | VcsExtHistSupplyForecastPEOCommitHorizonEndDate | COMMIT_HORIZON_END_DATE | — | ✅ |
| 14 | VcsExtHistSupplyForecastPEOCommitTotalQuantity | COMMIT_HORIZON_CQTY | — | ✅ |
| 15 | VcsExtHistSupplyForecastPEOCommittedByPartyCode | COMMITTED_BY_PARTY | — | ✅ |
| 16 | VcsExtHistSupplyForecastPEOCommittedByPersonId | COMMITTED_BY | — | ✅ |
| 17 | VcsExtHistSupplyForecastPEOCorrelationCode | ORCH_CORRELATION_CODE | — | ✅ |
| 18 | VcsExtHistSupplyForecastPEOCreatedBy | CREATED_BY | — | ✅ |
| 19 | VcsExtHistSupplyForecastPEOCreationDate | CREATION_DATE | — | ✅ |
| 20 | VcsExtHistSupplyForecastPEOForecastHorizonEndDate | FORECAST_HORIZON_END_DATE | — | ✅ |
| 21 | VcsExtHistSupplyForecastPEOForecastTotalCommitHorizonQuantity | COMMIT_HORIZON_FQTY | — | ✅ |
| 22 | VcsExtHistSupplyForecastPEOForecastTotalForecastHorizonQuantity | FORECAST_HORIZON_FQTY | — | ✅ |
| 23 | VcsExtHistSupplyForecastPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 24 | VcsExtHistSupplyForecastPEOInventoryItemOrganizationId | INVENTORY_ITEM_ORG_ID | — | ✅ |
| 25 | VcsExtHistSupplyForecastPEOLastPublishedPlanName | LAST_PUBLISHED_PLAN_NAME | — | ✅ |
| 26 | VcsExtHistSupplyForecastPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 27 | VcsExtHistSupplyForecastPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 28 | VcsExtHistSupplyForecastPEOMaxCommitVersion | MAX_COMMIT_VERSION | — | ✅ |
| 29 | VcsExtHistSupplyForecastPEOMaxForecastVersion | MAX_FORECAST_VERSION | — | ✅ |
| 30 | VcsExtHistSupplyForecastPEONoteToPlanner | NOTE_TO_PLANNER | — | ✅ |
| 31 | VcsExtHistSupplyForecastPEONoteToSupplier | NOTE_TO_SUPPLIER | — | ✅ |
| 32 | VcsExtHistSupplyForecastPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 33 | VcsExtHistSupplyForecastPEOPublishCycleEndDate | PUBLISH_CYCLE_END_DATE | — | ✅ |
| 34 | VcsExtHistSupplyForecastPEOPublishCycleStartDate | PUBLISH_CYCLE_START_DATE | — | ✅ |
| 35 | VcsExtHistSupplyForecastPEOPublishedByPartyCode | PUBLISH_BY_PARTY | — | ✅ |
| 36 | VcsExtHistSupplyForecastPEOPublishedByPersonId | PUBLISHED_BY | — | ✅ |
| 37 | VcsExtHistSupplyForecastPEOPublishedDate | PUBLISHED_DATE | — | ✅ |
| 38 | VcsExtHistSupplyForecastPEOPublishedOnHandQuantity | PUBLISHED_ON_HAND_QTY | — | ✅ |
| 39 | VcsExtHistSupplyForecastPEOShipFromId | SHIP_FROM_ID | — | ✅ |
| 40 | VcsExtHistSupplyForecastPEOShipToId | SHIP_TO_ID | — | ✅ |
| 41 | VcsExtHistSupplyForecastPEOSlaDays | SLA_DAYS | — | ✅ |
| 42 | VcsExtHistSupplyForecastPEOStatusCode | STATUS_CODE | — | ✅ |
| 43 | VcsExtHistSupplyForecastPEOSupplierOnHandPublishedByPartyCode | SUPPLIER_ON_HAND_PUB_BY_PARTY | — | ✅ |
| 44 | VcsExtHistSupplyForecastPEOSupplierOnHandPublishedByPersonId | SUPPLIER_ON_HAND_PUB_BY | — | ✅ |
| 45 | VcsExtHistSupplyForecastPEOSupplierOnHandPublishedDate | SUPPLIER_ON_HAND_PUB_DATE | — | ✅ |
| 46 | VcsExtHistSupplyForecastPEOSupplierOnHandQuantity | SUPPLIER_ON_HAND_QTY | — | ✅ |
| 47 | VcsExtHistSupplyForecastPEOUOMCode | PRIMARY_UOM_CODE | — | ✅ |

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
