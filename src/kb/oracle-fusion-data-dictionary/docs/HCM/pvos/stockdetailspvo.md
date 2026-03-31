---
id: DOC-HCM-PVO-StockDetailsPVO
doc_type: system-doc
title: "StockDetailsPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - StockDetailsPVO
  - stockdetailspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# StockDetailsPVO

## 📌 Visão Geral

Extrai detalhes de ações (stock) vinculados a perfis de compensação. Suporta gestão de remuneração em ações e análise de equity compensation.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.CompensationAM.StockDetailsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 77 | 2 | 1 | 44 | 57% |

---

## 🔗 Tabelas Relacionadas

- [[cmp_profile_values|CMP_PROFILE_VALUES]] — 30 atributos (2 BICC)
- [[cmp_stock_details|CMP_STOCK_DETAILS]] — 47 atributos (1 PKs, 42 BICC)

---

## ⚙️ Atributos

### [[cmp_profile_values|CMP_PROFILE_VALUES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CompProfileEOBusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 2 | CompProfileEOCreatedBy1 | CREATED_BY | — | — |
| 3 | CompProfileEOCreationDate1 | CREATION_DATE | — | — |
| 4 | CompProfileEOEnableModelingFlag | ENABLE_MODELING_FLAG | — | — |
| 5 | CompProfileEOEstStockPrice | EST_STOCK_PRICE | — | ✅ |
| 6 | CompProfileEOEstStockPriceCurrencyCd | EST_STOCK_PRICE_CURRENCY_CD | — | — |
| 7 | CompProfileEOLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 8 | CompProfileEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 9 | CompProfileEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 10 | CompProfileEOMaxStatementPeriods | MAX_STATEMENT_PERIODS | — | — |
| 11 | CompProfileEOMaxSwitchManagers | MAX_SWITCH_MANAGERS | — | — |
| 12 | CompProfileEONotifyBudgetPublish | NOTIFY_BUDGET_PUBLISH | — | — |
| 13 | CompProfileEONotifyChangeAccess | NOTIFY_CHANGE_ACCESS | — | — |
| 14 | CompProfileEONotifyChangeElig | NOTIFY_CHANGE_ELIG | — | — |
| 15 | CompProfileEONotifyFinalApproval | NOTIFY_FINAL_APPROVAL | — | — |
| 16 | CompProfileEONotifyManagerApproval | NOTIFY_MANAGER_APPROVAL | — | — |
| 17 | CompProfileEONotifyManagerOverride | NOTIFY_MANAGER_OVERRIDE | — | — |
| 18 | CompProfileEONotifyReassign | NOTIFY_REASSIGN | — | — |
| 19 | CompProfileEONotifyWorkRecall | NOTIFY_WORK_RECALL | — | — |
| 20 | CompProfileEONotifyWorkReject | NOTIFY_WORK_REJECT | — | — |
| 21 | CompProfileEONotifyWorkSubmit | NOTIFY_WORK_SUBMIT | — | — |
| 22 | CompProfileEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 23 | CompProfileEOWatchBudgetPublishDays | WATCH_BUDGET_PUBLISH_DAYS | — | — |
| 24 | CompProfileEOWatchBudgetPublishFlag | WATCH_BUDGET_PUBLISH_FLAG | — | — |
| 25 | CompProfileEOWatchNewPlansDays | WATCH_NEW_PLANS_DAYS | — | — |
| 26 | CompProfileEOWatchNewPlansFlag | WATCH_NEW_PLANS_FLAG | — | — |
| 27 | CompProfileEOWatchNumPlansFlag | WATCH_NUM_PLANS_FLAG | — | — |
| 28 | CompProfileEOWatchNumPoolsFlag | WATCH_NUM_POOLS_FLAG | — | — |
| 29 | CompProfileEOWatchStatementDays | WATCH_STATEMENT_DAYS | — | — |
| 30 | CompProfileEOWatchStatementFlag | WATCH_STATEMENT_FLAG | — | — |

### [[cmp_stock_details|CMP_STOCK_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | StockDetailsId | STOCK_DETAILS_ID | 🔑 | ✅ |
| 2 | StockEOAssignmentId | ASSIGNMENT_ID | — | ✅ |
| 3 | StockEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 4 | StockEOCancellationDate | CANCELLATION_DATE | — | ✅ |
| 5 | StockEOCancelledShares | CANCELLED_SHARES | — | ✅ |
| 6 | StockEOClassType | CLASS_TYPE | — | ✅ |
| 7 | StockEOCreatedBy | CREATED_BY | — | ✅ |
| 8 | StockEOCreationDate | CREATION_DATE | — | ✅ |
| 9 | StockEOElementEntryId | ELEMENT_ENTRY_ID | — | — |
| 10 | StockEOExercisableShares | EXERCISABLE_SHARES | — | ✅ |
| 11 | StockEOExerciseDate | EXERCISE_DATE | — | ✅ |
| 12 | StockEOExercisePrice | EXERCISE_PRICE | — | ✅ |
| 13 | StockEOExercisedShares | EXERCISED_SHARES | — | ✅ |
| 14 | StockEOExpirationDate | EXPIRATION_DATE | — | ✅ |
| 15 | StockEOGrantId | GRANT_ID | — | ✅ |
| 16 | StockEOGrantName | GRANT_NAME | — | ✅ |
| 17 | StockEOGrantNumber | GRANT_NUMBER | — | ✅ |
| 18 | StockEOGrantType | GRANT_TYPE | — | ✅ |
| 19 | StockEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 20 | StockEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 21 | StockEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 22 | StockEOLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 23 | StockEOMisc | MISC | — | ✅ |
| 24 | StockEOMisc1Char | MISC1_CHAR | — | ✅ |
| 25 | StockEOMisc1Val | MISC1_VAL | — | ✅ |
| 26 | StockEOMisc2Char | MISC2_CHAR | — | ✅ |
| 27 | StockEOMisc2Val | MISC2_VAL | — | ✅ |
| 28 | StockEOMisc3Char | MISC3_CHAR | — | ✅ |
| 29 | StockEOMisc3Val | MISC3_VAL | — | ✅ |
| 30 | StockEOMisc4Char | MISC4_CHAR | — | ✅ |
| 31 | StockEOMisc4Val | MISC4_VAL | — | ✅ |
| 32 | StockEOMisc5Char | MISC5_CHAR | — | ✅ |
| 33 | StockEOMisc5Val | MISC5_VAL | — | ✅ |
| 34 | StockEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 35 | StockEOOriginalGrantDate | ORIGINAL_GRANT_DATE | — | ✅ |
| 36 | StockEOOriginalGrantPrice | ORIGINAL_GRANT_PRICE | — | ✅ |
| 37 | StockEOOriginalSharesGranted | ORIGINAL_SHARES_GRANTED | — | ✅ |
| 38 | StockEOOriginalValueAtGrant | ORIGINAL_VALUE_AT_GRANT | — | ✅ |
| 39 | StockEOPersonEventId | PERSON_EVENT_ID | — | — |
| 40 | StockEOPersonId | PERSON_ID | — | — |
| 41 | StockEOReasonCode | REASON_CODE | — | ✅ |
| 42 | StockEOTotalShares | TOTAL_SHARES | — | ✅ |
| 43 | StockEOTradingSymbol | TRADING_SYMBOL | — | ✅ |
| 44 | StockEOUnvestedShares | UNVESTED_SHARES | — | ✅ |
| 45 | StockEOVestDate | VEST_DATE | — | ✅ |
| 46 | StockEOVestedShares | VESTED_SHARES | — | ✅ |
| 47 | StockEOWorkerNumber | WORKER_NUMBER | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
