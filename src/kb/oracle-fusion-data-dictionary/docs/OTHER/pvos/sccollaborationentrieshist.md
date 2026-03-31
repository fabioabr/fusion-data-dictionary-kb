---
id: DOC-OTHER-PVO-SCCollaborationEntriesHist
doc_type: system-doc
title: "SCCollaborationEntriesHist — PVO Cross-Module"
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
  - SCCollaborationEntriesHist
  - sccollaborationentrieshist
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SCCollaborationEntriesHist

## 📌 Visão Geral

View Object para extração BICC de dados de SCCollaboration Entries Hist. Acessa as tabelas: VCS_COLLAB_ENT_HIST, VCS_COLLAB_SOURCE, VCS_PLAN_SCENARIOS_B (+1).

**Caminho:** `FscmTopModelAM.SupplyCollaborationAM.SCCollaborationEntriesHist`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 92 | 4 | 2 | 16 | 17% |

---

## 🔗 Tabelas Relacionadas

- [[vcs_collab_ent_hist|VCS_COLLAB_ENT_HIST]] — 53 atributos (1 PKs, 9 BICC)
- [[vcs_collab_source|VCS_COLLAB_SOURCE]] — 17 atributos (1 PKs, 4 BICC)
- [[vcs_plan_scenarios_b|VCS_PLAN_SCENARIOS_B]] — 12 atributos (1 BICC)
- [[vcs_plan_scenarios_tl|VCS_PLAN_SCENARIOS_TL]] — 10 atributos (2 BICC)

---

## ⚙️ Atributos

### [[vcs_collab_ent_hist|VCS_COLLAB_ENT_HIST]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CollaborationEntriesHistNoteToPlanner | NOTE_TO_PLANNER | — | — |
| 2 | CollaborationEntriesHistNoteToSupplier | NOTE_TO_SUPPLIER | — | — |
| 3 | CollaborationEntriesHistPEOBucketCountCommitHorizonMonthly | BUCKET_COUNT_CH_MONTHLY | — | — |
| 4 | CollaborationEntriesHistPEOBucketCountCommitHorizonWeekly | BUCKET_COUNT_CH_WEEKLY | — | — |
| 5 | CollaborationEntriesHistPEOBucketCountForecastHorizonMonthly | BUCKET_COUNT_FH_MONTHLY | — | — |
| 6 | CollaborationEntriesHistPEOBucketCountForecastHorizonWeekly | BUCKET_COUNT_FH_WEEKLY | — | — |
| 7 | CollaborationEntriesHistPEOCollabEntryVersion | COLLAB_ENTRY_VERSION | — | — |
| 8 | CollaborationEntriesHistPEOCollabSourceId | COLLAB_SOURCE_ID | — | ✅ |
| 9 | CollaborationEntriesHistPEOCollabUom | COLLAB_UOM | — | ✅ |
| 10 | CollaborationEntriesHistPEOCommitDate | COMMIT_DATE | — | — |
| 11 | CollaborationEntriesHistPEOCommitDueDate | COMMIT_DUE_DATE | — | — |
| 12 | CollaborationEntriesHistPEOCommitHorizonCqty | COMMIT_HORIZON_CQTY | — | — |
| 13 | CollaborationEntriesHistPEOCommitHorizonEndDate | COMMIT_HORIZON_END_DATE | — | — |
| 14 | CollaborationEntriesHistPEOCommitHorizonFqty | COMMIT_HORIZON_FQTY | — | — |
| 15 | CollaborationEntriesHistPEOCommitMismatchCountMonthly | COMMIT_MISMATCH_COUNT_MONTHLY | — | — |
| 16 | CollaborationEntriesHistPEOCommitMismatchCountWeekly | COMMIT_MISMATCH_COUNT_WEEKLY | — | — |
| 17 | CollaborationEntriesHistPEOCommitToForecastMAPEMonthly | CTF_MAPE_MONTHLY | — | — |
| 18 | CollaborationEntriesHistPEOCommitToForecastMAPEWeekly | CTF_MAPE_WEEKLY | — | — |
| 19 | CollaborationEntriesHistPEOCreatedBy | CREATED_BY | — | — |
| 20 | CollaborationEntriesHistPEOCreationDate | CREATION_DATE | — | — |
| 21 | CollaborationEntriesHistPEODetailLastUpdateEnt | DETAIL_LAST_UPDATE_ENT | — | — |
| 22 | CollaborationEntriesHistPEODetailLastUpdateSup | DETAIL_LAST_UPDATE_SUP | — | — |
| 23 | CollaborationEntriesHistPEOEntDraftQtyFlag | ENT_DRAFT_QTY_FLAG | — | — |
| 24 | CollaborationEntriesHistPEOEntryId | ENTRY_ID | 🔑 | ✅ |
| 25 | CollaborationEntriesHistPEOEntryTypeId | ENTRY_TYPE_ID | — | — |
| 26 | CollaborationEntriesHistPEOForecastChangeCountMonthly | FORECAST_CHANGE_COUNT_MONTHLY | — | — |
| 27 | CollaborationEntriesHistPEOForecastChangeCountWeekly | FORECAST_CHANGE_COUNT_WEEKLY | — | — |
| 28 | CollaborationEntriesHistPEOForecastChangeMAPEMonthly | FORECAST_CHANGE_MAPE_MONTHLY | — | — |
| 29 | CollaborationEntriesHistPEOForecastChangeMAPEWeekly | FORECAST_CHANGE_MAPE_WEEKLY | — | — |
| 30 | CollaborationEntriesHistPEOForecastHorizonEndDate | FORECAST_HORIZON_END_DATE | — | — |
| 31 | CollaborationEntriesHistPEOForecastHorizonFqty | FORECAST_HORIZON_FQTY | — | — |
| 32 | CollaborationEntriesHistPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 33 | CollaborationEntriesHistPEOInventoryItemOrgId | INVENTORY_ITEM_ORG_ID | — | — |
| 34 | CollaborationEntriesHistPEOLastPublishedPlanName | LAST_PUBLISHED_PLAN_NAME | — | ✅ |
| 35 | CollaborationEntriesHistPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 36 | CollaborationEntriesHistPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 37 | CollaborationEntriesHistPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 38 | CollaborationEntriesHistPEOMaxCommitVersion | MAX_COMMIT_VERSION | — | — |
| 39 | CollaborationEntriesHistPEOMaxForecastVersion | MAX_FORECAST_VERSION | — | — |
| 40 | CollaborationEntriesHistPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 41 | CollaborationEntriesHistPEOOrchCorrelationCode | ORCH_CORRELATION_CODE | — | — |
| 42 | CollaborationEntriesHistPEOPrimaryUom | PRIMARY_UOM_CODE | — | — |
| 43 | CollaborationEntriesHistPEOPublishByParty | PUBLISH_BY_PARTY | — | ✅ |
| 44 | CollaborationEntriesHistPEOPublishCycleEndDate | PUBLISH_CYCLE_END_DATE | — | ✅ |
| 45 | CollaborationEntriesHistPEOPublishCycleStartDate | PUBLISH_CYCLE_START_DATE | — | ✅ |
| 46 | CollaborationEntriesHistPEOPublishedBy | PUBLISHED_BY | — | — |
| 47 | CollaborationEntriesHistPEOPublishedDate | PUBLISHED_DATE | — | ✅ |
| 48 | CollaborationEntriesHistPEOShipFromId | SHIP_FROM_ID | — | — |
| 49 | CollaborationEntriesHistPEOShipToId | SHIP_TO_ID | — | — |
| 50 | CollaborationEntriesHistPEOSlaDays | SLA_DAYS | — | — |
| 51 | CollaborationEntriesHistPEOStatusCode | STATUS_CODE | — | — |
| 52 | CollaborationEntriesHistPEOSupDraftQtyFlag | SUP_DRAFT_QTY_FLAG | — | — |
| 53 | CollaborationEntriesHistPEOTimeLevel | TIME_LEVEL | — | — |

### [[vcs_collab_source|VCS_COLLAB_SOURCE]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SCCollaborationPlanPEOCollabName | COLLAB_NAME | — | ✅ |
| 2 | SCCollaborationPlanPEOCollabSourceId | COLLAB_SOURCE_ID | 🔑 | ✅ |
| 3 | SCCollaborationPlanPEOCollabTypeCode | COLLAB_TYPE_CODE | — | — |
| 4 | SCCollaborationPlanPEOCollabVersion | COLLAB_VERSION | — | — |
| 5 | SCCollaborationPlanPEOCreatedBy | CREATED_BY | — | — |
| 6 | SCCollaborationPlanPEOCreationDate | CREATION_DATE | — | — |
| 7 | SCCollaborationPlanPEODescription | DESCRIPTION | — | ✅ |
| 8 | SCCollaborationPlanPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | SCCollaborationPlanPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | SCCollaborationPlanPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | SCCollaborationPlanPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | SCCollaborationPlanPEOOriginSourceCode | ORIGIN_SOURCE_CODE | — | — |
| 13 | SCCollaborationPlanPEOParentCollabSourceId | PARENT_COLLAB_SOURCE_ID | — | — |
| 14 | SCCollaborationPlanPEOPublishCycleEndDate | PUBLISH_CYCLE_END_DATE | — | — |
| 15 | SCCollaborationPlanPEOPublishCycleStartDate | PUBLISH_CYCLE_START_DATE | — | — |
| 16 | SCCollaborationPlanPEOScenarioId | SCENARIO_ID | — | — |
| 17 | SCCollaborationPlanPEOSourceSystemCode | SOURCE_SYSTEM_CODE | — | — |

### [[vcs_plan_scenarios_b|VCS_PLAN_SCENARIOS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SCPlanScenariosBasePEOCreatedBy | CREATED_BY | — | — |
| 2 | SCPlanScenariosBasePEOCreationDate | CREATION_DATE | — | — |
| 3 | SCPlanScenariosBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | SCPlanScenariosBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 5 | SCPlanScenariosBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 6 | SCPlanScenariosBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | SCPlanScenariosBasePEOPlanName | PLAN_NAME | — | — |
| 8 | SCPlanScenariosBasePEOPublishCycleDayCode | PUBLISH_CYCLE_DAY_CODE | — | — |
| 9 | SCPlanScenariosBasePEOPublishCycleFrequency | PUBLISH_CYCLE_FREQUENCY | — | — |
| 10 | SCPlanScenariosBasePEOPublishCycleTypeCode | PUBLISH_CYCLE_TYPE_CODE | — | — |
| 11 | SCPlanScenariosBasePEOScenarioId | SCENARIO_ID | — | — |
| 12 | SCPlanScenariosBasePEOStatusCode | STATUS_CODE | — | — |

### [[vcs_plan_scenarios_tl|VCS_PLAN_SCENARIOS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SCPlanScenariosTranslatePEOCreatedBy | CREATED_BY | — | — |
| 2 | SCPlanScenariosTranslatePEOCreationDate | CREATION_DATE | — | — |
| 3 | SCPlanScenariosTranslatePEOLanguage | LANGUAGE | — | — |
| 4 | SCPlanScenariosTranslatePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | SCPlanScenariosTranslatePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | SCPlanScenariosTranslatePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | SCPlanScenariosTranslatePEOName | NAME | — | ✅ |
| 8 | SCPlanScenariosTranslatePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | SCPlanScenariosTranslatePEOScenarioId | SCENARIO_ID | — | — |
| 10 | SCPlanScenariosTranslatePEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
