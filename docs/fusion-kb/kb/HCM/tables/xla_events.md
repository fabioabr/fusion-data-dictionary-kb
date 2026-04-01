---
id: DOC-HCM-868
doc_type: system-doc
title: "XLA_EVENTS — (título a preencher)"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - human-capital-management
  - data-dictionary
aliases:
  - XLA_EVENTS
  - xla_events
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# XLA_EVENTS

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | APPLICATION_ID | — | — | — | — | — | — |
| 2 | BUDGETARY_CONTROL_FLAG | — | — | — | — | — | — |
| 3 | CREATED_BY | — | — | — | — | — | — |
| 4 | CREATION_DATE | — | — | — | — | — | — |
| 5 | ENTITY_ID | — | — | — | — | — | — |
| 6 | EVENT_DATE | — | — | — | — | — | — |
| 7 | EVENT_ID | — | — | — | — | — | — |
| 8 | EVENT_NUMBER | — | — | — | — | — | — |
| 9 | EVENT_STATUS_CODE | — | — | — | — | — | — |
| 10 | EVENT_TYPE_CODE | — | — | — | — | — | — |
| 11 | FILE_IDENTIFIER | — | — | — | — | — | — |
| 12 | HAS_WARNINGS_FLAG | — | — | — | — | — | — |
| 13 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 14 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 15 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 16 | MERGE_EVENT_SET_ID | — | — | — | — | — | — |
| 17 | OBJECT_VERSION_NUMBER | — | — | — | — | — | — |
| 18 | ON_HOLD_FLAG | — | — | — | — | — | — |
| 19 | PROCESS_STATUS_CODE | — | — | — | — | — | — |
| 20 | REFERENCE_CHAR_1 | — | — | — | — | — | — |
| 21 | REFERENCE_CHAR_2 | — | — | — | — | — | — |
| 22 | REFERENCE_CHAR_3 | — | — | — | — | — | — |
| 23 | REFERENCE_CHAR_4 | — | — | — | — | — | — |
| 24 | REFERENCE_DATE_1 | — | — | — | — | — | — |
| 25 | REFERENCE_DATE_2 | — | — | — | — | — | — |
| 26 | REFERENCE_DATE_3 | — | — | — | — | — | — |
| 27 | REFERENCE_DATE_4 | — | — | — | — | — | — |
| 28 | REFERENCE_NUM_1 | — | — | — | — | — | — |
| 29 | REFERENCE_NUM_2 | — | — | — | — | — | — |
| 30 | REFERENCE_NUM_3 | — | — | — | — | — | — |
| 31 | REFERENCE_NUM_4 | — | — | — | — | — | — |
| 32 | REQUEST_ID | — | — | — | — | — | — |
| 33 | TRANSACTION_DATE | — | — | — | — | — | — |
| 34 | UPG_BATCH_ID | — | — | — | — | — | — |
| 35 | UPG_SOURCE_APPLICATION_ID | — | — | — | — | — | — |
| 36 | UPG_VALID_FLAG | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[adjustmentdistributionpvo|AdjustmentDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUDGETARY_CONTROL_FLAG | EventBudgetaryControlFlag | — |
| EVENT_DATE | EventEventDate | — |
| EVENT_ID | EventEventId | — |
| EVENT_NUMBER | EventEventNumber | — |
| EVENT_STATUS_CODE | EventEventStatusCode | — |
| EVENT_TYPE_CODE | EventEventTypeCode | — |
| HAS_WARNINGS_FLAG | EventHasWarningsFlag | — |
| ON_HOLD_FLAG | EventOnHoldFlag | — |
| PROCESS_STATUS_CODE | EventProcessStatusCode | — |
| TRANSACTION_DATE | EventTransactionDate | — |
| UPG_VALID_FLAG | EventUpgValidFlag | — |

### [[adjustmentpvo|AdjustmentPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUDGETARY_CONTROL_FLAG | EventBudgetaryControlFlag | — |
| EVENT_DATE | EventEventDate | — |
| EVENT_ID | EventEventId | — |
| EVENT_NUMBER | EventEventNumber | — |
| EVENT_STATUS_CODE | EventEventStatusCode | — |
| EVENT_TYPE_CODE | EventEventTypeCode | — |
| HAS_WARNINGS_FLAG | EventHasWarningsFlag | — |
| ON_HOLD_FLAG | EventOnHoldFlag | — |
| PROCESS_STATUS_CODE | EventProcessStatusCode | — |
| TRANSACTION_DATE | EventTransactionDate | — |
| UPG_VALID_FLAG | EventUpgValidFlag | — |

### [[creditmemoapplicationdistributionpvo|CreditMemoApplicationDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUDGETARY_CONTROL_FLAG | EventBudgetaryControlFlag | — |
| EVENT_DATE | EventEventDate | — |
| EVENT_ID | EventEventId | — |
| EVENT_NUMBER | EventEventNumber | — |
| EVENT_STATUS_CODE | EventEventStatusCode | — |
| EVENT_TYPE_CODE | EventEventTypeCode | — |
| HAS_WARNINGS_FLAG | EventHasWarningsFlag | — |
| ON_HOLD_FLAG | EventOnHoldFlag | — |
| PROCESS_STATUS_CODE | EventProcessStatusCode | — |
| TRANSACTION_DATE | EventTransactionDate | — |
| UPG_VALID_FLAG | EventUpgValidFlag | — |

### [[creditmemoapplicationpvo|CreditMemoApplicationPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUDGETARY_CONTROL_FLAG | EventBudgetaryControlFlag | — |
| EVENT_DATE | EventEventDate | — |
| EVENT_ID | EventEventId | — |
| EVENT_NUMBER | EventEventNumber | — |
| EVENT_STATUS_CODE | EventEventStatusCode | — |
| EVENT_TYPE_CODE | EventEventTypeCode | — |
| HAS_WARNINGS_FLAG | EventHasWarningsFlag | — |
| ON_HOLD_FLAG | EventOnHoldFlag | — |
| PROCESS_STATUS_CODE | EventProcessStatusCode | — |
| TRANSACTION_DATE | EventTransactionDate | — |
| UPG_VALID_FLAG | EventUpgValidFlag | — |

### [[depreciationeventspvo|DepreciationEventsPVO]] (OTHER · BICC: 8/70)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICATION_ID | EventApplicationId | — |
| APPLICATION_ID | RevEventApplicationId | — |
| BUDGETARY_CONTROL_FLAG | EventBudgetaryControlFlag | — |
| BUDGETARY_CONTROL_FLAG | RevEventBudgetaryControlFlag | — |
| CREATED_BY | EventCreatedBy | — |
| CREATED_BY | RevEventCreatedBy | — |
| CREATION_DATE | EventCreationDate | — |
| CREATION_DATE | RevEventCreationDate | — |
| ENTITY_ID | EventEntityId | — |
| ENTITY_ID | RevEventEntityId | — |
| EVENT_DATE | EventEventDate | ✅ |
| EVENT_DATE | RevEventEventDate | ✅ |
| EVENT_ID | EventEventId | — |
| EVENT_ID | RevEventEventId | — |
| EVENT_NUMBER | EventEventNumber | — |
| EVENT_NUMBER | RevEventEventNumber | — |
| EVENT_STATUS_CODE | EventEventStatusCode | — |
| EVENT_STATUS_CODE | RevEventEventStatusCode | — |
| EVENT_TYPE_CODE | EventEventTypeCode | ✅ |
| EVENT_TYPE_CODE | RevEventEventTypeCode | ✅ |
| HAS_WARNINGS_FLAG | EventHasWarningsFlag | — |
| HAS_WARNINGS_FLAG | RevEventHasWarningsFlag | — |
| LAST_UPDATE_DATE | EventLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | RevEventLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | EventLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | RevEventLastUpdateLogin | — |
| LAST_UPDATED_BY | EventLastUpdatedBy | — |
| LAST_UPDATED_BY | RevEventLastUpdatedBy | — |
| MERGE_EVENT_SET_ID | EventMergeEventSetId | — |
| MERGE_EVENT_SET_ID | RevEventMergeEventSetId | — |
| OBJECT_VERSION_NUMBER | EventObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | RevEventObjectVersionNumber | — |
| ON_HOLD_FLAG | EventOnHoldFlag | — |
| ON_HOLD_FLAG | RevEventOnHoldFlag | — |
| PROCESS_STATUS_CODE | EventProcessStatusCode | — |
| PROCESS_STATUS_CODE | RevEventProcessStatusCode | — |
| REFERENCE_CHAR_1 | EventReferenceChar1 | — |
| REFERENCE_CHAR_1 | RevEventReferenceChar1 | — |
| REFERENCE_CHAR_2 | EventReferenceChar2 | — |
| REFERENCE_CHAR_2 | RevEventReferenceChar2 | — |
| REFERENCE_CHAR_3 | EventReferenceChar3 | — |
| REFERENCE_CHAR_3 | RevEventReferenceChar3 | — |
| REFERENCE_CHAR_4 | EventReferenceChar4 | — |
| REFERENCE_CHAR_4 | RevEventReferenceChar4 | — |
| REFERENCE_DATE_1 | EventReferenceDate1 | — |
| REFERENCE_DATE_1 | RevEventReferenceDate1 | — |
| REFERENCE_DATE_2 | EventReferenceDate2 | — |
| REFERENCE_DATE_2 | RevEventReferenceDate2 | — |
| REFERENCE_DATE_3 | EventReferenceDate3 | — |
| REFERENCE_DATE_3 | RevEventReferenceDate3 | — |
| REFERENCE_DATE_4 | EventReferenceDate4 | — |
| REFERENCE_DATE_4 | RevEventReferenceDate4 | — |
| REFERENCE_NUM_1 | EventReferenceNum1 | — |
| REFERENCE_NUM_1 | RevEventReferenceNum1 | — |
| REFERENCE_NUM_2 | EventReferenceNum2 | — |
| REFERENCE_NUM_2 | RevEventReferenceNum2 | — |
| REFERENCE_NUM_3 | EventReferenceNum3 | — |
| REFERENCE_NUM_3 | RevEventReferenceNum3 | — |
| REFERENCE_NUM_4 | EventReferenceNum4 | — |
| REFERENCE_NUM_4 | RevEventReferenceNum4 | — |
| REQUEST_ID | EventRequestId | — |
| REQUEST_ID | RevEventRequestId | — |
| TRANSACTION_DATE | EventTransactionDate | ✅ |
| TRANSACTION_DATE | RevEventTransactionDate | ✅ |
| UPG_BATCH_ID | EventUpgBatchId | — |
| UPG_BATCH_ID | RevEventUpgBatchId | — |
| UPG_SOURCE_APPLICATION_ID | EventUpgSourceApplicationId | — |
| UPG_SOURCE_APPLICATION_ID | RevEventUpgSourceApplicationId | — |
| UPG_VALID_FLAG | EventUpgValidFlag | — |
| UPG_VALID_FLAG | RevEventUpgValidFlag | — |

### [[miscreceiptdistributionpvo|MiscReceiptDistributionPVO]] (AR · BICC: 1/35)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICATION_ID | EventApplicationId | — |
| BUDGETARY_CONTROL_FLAG | EventBudgetaryControlFlag | — |
| CREATED_BY | EventCreatedBy | — |
| CREATION_DATE | EventCreationDate | — |
| ENTITY_ID | EventEntityId | — |
| EVENT_DATE | EventEventDate | — |
| EVENT_ID | EventEventId | — |
| EVENT_NUMBER | EventEventNumber | — |
| EVENT_STATUS_CODE | EventEventStatusCode | — |
| EVENT_TYPE_CODE | EventEventTypeCode | — |
| HAS_WARNINGS_FLAG | EventHasWarningsFlag | — |
| LAST_UPDATE_DATE | EventLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | EventLastUpdateLogin | — |
| LAST_UPDATED_BY | EventLastUpdatedBy | — |
| MERGE_EVENT_SET_ID | EventMergeEventSetId | — |
| OBJECT_VERSION_NUMBER | EventObjectVersionNumber | — |
| ON_HOLD_FLAG | EventOnHoldFlag | — |
| PROCESS_STATUS_CODE | EventProcessStatusCode | — |
| REFERENCE_CHAR_1 | EventReferenceChar1 | — |
| REFERENCE_CHAR_2 | EventReferenceChar2 | — |
| REFERENCE_CHAR_3 | EventReferenceChar3 | — |
| REFERENCE_CHAR_4 | EventReferenceChar4 | — |
| REFERENCE_DATE_1 | EventReferenceDate1 | — |
| REFERENCE_DATE_2 | EventReferenceDate2 | — |
| REFERENCE_DATE_3 | EventReferenceDate3 | — |
| REFERENCE_DATE_4 | EventReferenceDate4 | — |
| REFERENCE_NUM_1 | EventReferenceNum1 | — |
| REFERENCE_NUM_2 | EventReferenceNum2 | — |
| REFERENCE_NUM_3 | EventReferenceNum3 | — |
| REFERENCE_NUM_4 | EventReferenceNum4 | — |
| REQUEST_ID | EventRequestId | — |
| TRANSACTION_DATE | EventTransactionDate | — |
| UPG_BATCH_ID | EventUpgBatchId | — |
| UPG_SOURCE_APPLICATION_ID | EventUpgSourceApplicationId | — |
| UPG_VALID_FLAG | EventUpgValidFlag | — |

### [[paymenthistorydistributionpvo|PaymentHistoryDistributionPVO]] (AP · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EVENT_ID | PayEvntEventId | — |
| EVENT_ID | PayHistDistEvntEventId | — |
| LAST_UPDATE_DATE | PayEvntLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | PayHistDistEvntLastUpdateDate | ✅ |

### [[receiptapplicationdistributionpvo|ReceiptApplicationDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUDGETARY_CONTROL_FLAG | EventBudgetaryControlFlag | — |
| EVENT_DATE | EventEventDate | — |
| EVENT_ID | EventEventId | — |
| EVENT_NUMBER | EventEventNumber | — |
| EVENT_STATUS_CODE | EventEventStatusCode | — |
| EVENT_TYPE_CODE | EventEventTypeCode | — |
| HAS_WARNINGS_FLAG | EventHasWarningsFlag | — |
| ON_HOLD_FLAG | EventOnHoldFlag | — |
| PROCESS_STATUS_CODE | EventProcessStatusCode | — |
| TRANSACTION_DATE | EventTransactionDate | — |
| UPG_VALID_FLAG | EventUpgValidFlag | — |

### [[receiptapplicationdistributionvc|ReceiptApplicationDistributionVC]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUDGETARY_CONTROL_FLAG | EventBudgetaryControlFlag | — |
| EVENT_DATE | EventEventDate | — |
| EVENT_ID | EventEventId | — |
| EVENT_NUMBER | EventEventNumber | — |
| EVENT_STATUS_CODE | EventEventStatusCode | — |
| EVENT_TYPE_CODE | EventEventTypeCode | — |
| HAS_WARNINGS_FLAG | EventHasWarningsFlag | — |
| ON_HOLD_FLAG | EventOnHoldFlag | — |
| PROCESS_STATUS_CODE | EventProcessStatusCode | — |
| TRANSACTION_DATE | EventTransactionDate | — |
| UPG_VALID_FLAG | EventUpgValidFlag | — |

### [[receiptapplicationpvo|ReceiptApplicationPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUDGETARY_CONTROL_FLAG | EventBudgetaryControlFlag | — |
| EVENT_DATE | EventEventDate | — |
| EVENT_ID | EventEventId | — |
| EVENT_NUMBER | EventEventNumber | — |
| EVENT_STATUS_CODE | EventEventStatusCode | — |
| EVENT_TYPE_CODE | EventEventTypeCode | — |
| HAS_WARNINGS_FLAG | EventHasWarningsFlag | — |
| ON_HOLD_FLAG | EventOnHoldFlag | — |
| PROCESS_STATUS_CODE | EventProcessStatusCode | — |
| TRANSACTION_DATE | EventTransactionDate | — |
| UPG_VALID_FLAG | EventUpgValidFlag | — |

### [[subledgerjournaleventextractpvo|SubledgerJournalEventExtractPVO]] (OTHER · BICC: 33/33)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICATION_ID | EventPEOApplicationId | ✅ |
| BUDGETARY_CONTROL_FLAG | EventPEOEventPEOBudgetaryControlFlag | ✅ |
| CREATED_BY | EventPEOEventPEOCreatedBy | ✅ |
| CREATION_DATE | EventPEOCreationDate | ✅ |
| ENTITY_ID | EventPEOEntityId | ✅ |
| EVENT_DATE | EventPEOEventDate | ✅ |
| EVENT_ID | EventPEOEventId | ✅ |
| EVENT_NUMBER | EventPEOEventNumber | ✅ |
| EVENT_STATUS_CODE | EventPEOEventStatusCode | ✅ |
| EVENT_TYPE_CODE | EventPEOEventTypeCode | ✅ |
| FILE_IDENTIFIER | EventPEOFileIdentifier | ✅ |
| HAS_WARNINGS_FLAG | EventPEOHasWarningsFlag | ✅ |
| LAST_UPDATE_DATE | EventPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | EventPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | EventPEOLastUpdatedBy | ✅ |
| MERGE_EVENT_SET_ID | EventPEOMergeEventSetId | ✅ |
| OBJECT_VERSION_NUMBER | EventPEOObjectVersionNumber | ✅ |
| ON_HOLD_FLAG | EventPEOOnHoldFlag | ✅ |
| PROCESS_STATUS_CODE | EventPEOProcessStatusCode | ✅ |
| REFERENCE_CHAR_1 | EventPEOReferenceChar1 | ✅ |
| REFERENCE_CHAR_2 | EventPEOReferenceChar2 | ✅ |
| REFERENCE_CHAR_3 | EventPEOReferenceChar3 | ✅ |
| REFERENCE_CHAR_4 | EventPEOReferenceChar4 | ✅ |
| REFERENCE_DATE_1 | EventPEOReferenceDate1 | ✅ |
| REFERENCE_DATE_2 | EventPEOReferenceDate2 | ✅ |
| REFERENCE_DATE_3 | EventPEOReferenceDate3 | ✅ |
| REFERENCE_DATE_4 | EventPEOReferenceDate4 | ✅ |
| REFERENCE_NUM_1 | EventPEOReferenceNum1 | ✅ |
| REFERENCE_NUM_2 | EventPEOReferenceNum2 | ✅ |
| REFERENCE_NUM_3 | EventPEOReferenceNum3 | ✅ |
| REFERENCE_NUM_4 | EventPEOReferenceNum4 | ✅ |
| REQUEST_ID | EventPEORequestId | ✅ |
| TRANSACTION_DATE | EventPEOTransactionDate | ✅ |
