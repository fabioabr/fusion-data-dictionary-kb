---
id: DOC-OTHER-PVO-TransactionBatchPVO
doc_type: system-doc
title: "TransactionBatchPVO — PVO Cross-Module"
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
  - TransactionBatchPVO
  - transactionbatchpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TransactionBatchPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Transaction Batch. Acessa as tabelas: FUN_INTERCO_ORGANIZATIONS, FUN_LOOKUPS, FUN_TRX_BATCHES (+1).

**Caminho:** `FscmTopModelAM.FinFunIntercoTransactionsAM.TransactionBatchPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 122 | 4 | 1 | 18 | 15% |

---

## 🔗 Tabelas Relacionadas

- [[fun_interco_organizations|FUN_INTERCO_ORGANIZATIONS]] — 10 atributos (1 BICC)
- [[fun_lookups|FUN_LOOKUPS]] — 7 atributos (1 BICC)
- [[fun_trx_batches|FUN_TRX_BATCHES]] — 87 atributos (1 PKs, 15 BICC)
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 18 atributos (1 BICC)

---

## ⚙️ Atributos

### [[fun_interco_organizations|FUN_INTERCO_ORGANIZATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IntercoOrgContactPersonId | CONTACT_PERSON_ID | — | — |
| 2 | IntercoOrgDescription | DESCRIPTION | — | — |
| 3 | IntercoOrgEnabledFlag | ENABLED_FLAG | — | — |
| 4 | IntercoOrgIntercoOrgId | INTERCO_ORG_ID | — | — |
| 5 | IntercoOrgIntercoOrgName | INTERCO_ORG_NAME | — | ✅ |
| 6 | IntercoOrgLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 7 | IntercoOrgPayBuId | PAY_BU_ID | — | — |
| 8 | IntercoOrgRecBuId | REC_BU_ID | — | — |
| 9 | IntercoOrgRemoteInstanceFlag | REMOTE_INSTANCE_FLAG | — | — |
| 10 | IntercoOrgRemoteInstanceIdentifier | REMOTE_INSTANCE_IDENTIFIER | — | — |

### [[fun_lookups|FUN_LOOKUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BatchLookupDescription | DESCRIPTION | — | — |
| 2 | BatchLookupEnabledFlag | ENABLED_FLAG | — | — |
| 3 | BatchLookupEndDateActive | END_DATE_ACTIVE | — | — |
| 4 | BatchLookupLookupCode | LOOKUP_CODE | — | — |
| 5 | BatchLookupLookupType | LOOKUP_TYPE | — | — |
| 6 | BatchLookupMeaning | MEANING | — | ✅ |
| 7 | BatchLookupStartDateActive | START_DATE_ACTIVE | — | — |

### [[fun_trx_batches|FUN_TRX_BATCHES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BatchId | BATCH_ID | 🔑 | ✅ |
| 2 | TransactionBatchAutoProrationFlag | AUTO_PRORATION_FLAG | — | — |
| 3 | TransactionBatchBatchDate | BATCH_DATE | — | ✅ |
| 4 | TransactionBatchBatchNumber | BATCH_NUMBER | — | ✅ |
| 5 | TransactionBatchControlTotal | CONTROL_TOTAL | — | ✅ |
| 6 | TransactionBatchCreatedBy | CREATED_BY | — | — |
| 7 | TransactionBatchCreationDate | CREATION_DATE | — | — |
| 8 | TransactionBatchCurrencyCode | CURRENCY_CODE | — | ✅ |
| 9 | TransactionBatchDescription | DESCRIPTION | — | ✅ |
| 10 | TransactionBatchExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 11 | TransactionBatchFromLeId | FROM_LE_ID | — | — |
| 12 | TransactionBatchFromLedgerId | FROM_LEDGER_ID | — | — |
| 13 | TransactionBatchFromRecurringBatchId | FROM_RECURRING_BATCH_ID | — | — |
| 14 | TransactionBatchGlDate | GL_DATE | — | ✅ |
| 15 | TransactionBatchInitiatorId | INITIATOR_ID | — | — |
| 16 | TransactionBatchInitiatorSource | INITIATOR_SOURCE | — | — |
| 17 | TransactionBatchLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 18 | TransactionBatchLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 19 | TransactionBatchLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 20 | TransactionBatchNote | NOTE | — | ✅ |
| 21 | TransactionBatchObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 22 | TransactionBatchOrigAutoProrationFlag | AUTO_PRORATION_FLAG | — | — |
| 23 | TransactionBatchOrigBatchDate | BATCH_DATE | — | — |
| 24 | TransactionBatchOrigBatchId | BATCH_ID | — | — |
| 25 | TransactionBatchOrigBatchNumber | BATCH_NUMBER | — | — |
| 26 | TransactionBatchOrigControlTotal | CONTROL_TOTAL | — | — |
| 27 | TransactionBatchOrigCreatedBy | CREATED_BY | — | — |
| 28 | TransactionBatchOrigCreationDate | CREATION_DATE | — | — |
| 29 | TransactionBatchOrigCurrencyCode | CURRENCY_CODE | — | — |
| 30 | TransactionBatchOrigDescription | DESCRIPTION | — | — |
| 31 | TransactionBatchOrigExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 32 | TransactionBatchOrigFromLeId | FROM_LE_ID | — | — |
| 33 | TransactionBatchOrigFromLedgerId | FROM_LEDGER_ID | — | — |
| 34 | TransactionBatchOrigFromRecurringBatchId | FROM_RECURRING_BATCH_ID | — | — |
| 35 | TransactionBatchOrigGlDate | GL_DATE | — | — |
| 36 | TransactionBatchOrigInitiatorId | INITIATOR_ID | — | — |
| 37 | TransactionBatchOrigInitiatorSource | INITIATOR_SOURCE | — | — |
| 38 | TransactionBatchOrigLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 39 | TransactionBatchOrigLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 40 | TransactionBatchOrigLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 41 | TransactionBatchOrigNote | NOTE | — | — |
| 42 | TransactionBatchOrigObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 43 | TransactionBatchOrigOriginalBatchId | ORIGINAL_BATCH_ID | — | — |
| 44 | TransactionBatchOrigRejectAllowFlag | REJECT_ALLOW_FLAG | — | — |
| 45 | TransactionBatchOrigReversedBatchId | REVERSED_BATCH_ID | — | — |
| 46 | TransactionBatchOrigRunningTotalCr | RUNNING_TOTAL_CR | — | — |
| 47 | TransactionBatchOrigRunningTotalDr | RUNNING_TOTAL_DR | — | — |
| 48 | TransactionBatchOrigStatus | STATUS | — | — |
| 49 | TransactionBatchOrigTrxTypeCode | TRX_TYPE_CODE | — | — |
| 50 | TransactionBatchOrigTrxTypeId | TRX_TYPE_ID | — | — |
| 51 | TransactionBatchOriginalBatchId | ORIGINAL_BATCH_ID | — | — |
| 52 | TransactionBatchRejectAllowFlag | REJECT_ALLOW_FLAG | — | — |
| 53 | TransactionBatchReverseAutoProrationFlag | AUTO_PRORATION_FLAG | — | — |
| 54 | TransactionBatchReverseBatchDate | BATCH_DATE | — | — |
| 55 | TransactionBatchReverseBatchId | BATCH_ID | — | — |
| 56 | TransactionBatchReverseBatchNumber | BATCH_NUMBER | — | — |
| 57 | TransactionBatchReverseControlTotal | CONTROL_TOTAL | — | — |
| 58 | TransactionBatchReverseCreatedBy | CREATED_BY | — | — |
| 59 | TransactionBatchReverseCreationDate | CREATION_DATE | — | — |
| 60 | TransactionBatchReverseCurrencyCode | CURRENCY_CODE | — | — |
| 61 | TransactionBatchReverseDescription | DESCRIPTION | — | — |
| 62 | TransactionBatchReverseExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 63 | TransactionBatchReverseFromLeId | FROM_LE_ID | — | — |
| 64 | TransactionBatchReverseFromLedgerId | FROM_LEDGER_ID | — | — |
| 65 | TransactionBatchReverseFromRecurringBatchId | FROM_RECURRING_BATCH_ID | — | — |
| 66 | TransactionBatchReverseGlDate | GL_DATE | — | — |
| 67 | TransactionBatchReverseInitiatorId | INITIATOR_ID | — | — |
| 68 | TransactionBatchReverseInitiatorSource | INITIATOR_SOURCE | — | — |
| 69 | TransactionBatchReverseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 70 | TransactionBatchReverseLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 71 | TransactionBatchReverseLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 72 | TransactionBatchReverseNote | NOTE | — | — |
| 73 | TransactionBatchReverseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 74 | TransactionBatchReverseOriginalBatchId | ORIGINAL_BATCH_ID | — | — |
| 75 | TransactionBatchReverseRejectAllowFlag | REJECT_ALLOW_FLAG | — | — |
| 76 | TransactionBatchReverseReversedBatchId | REVERSED_BATCH_ID | — | — |
| 77 | TransactionBatchReverseRunningTotalCr | RUNNING_TOTAL_CR | — | — |
| 78 | TransactionBatchReverseRunningTotalDr | RUNNING_TOTAL_DR | — | — |
| 79 | TransactionBatchReverseStatus | STATUS | — | — |
| 80 | TransactionBatchReverseTrxTypeCode | TRX_TYPE_CODE | — | — |
| 81 | TransactionBatchReverseTrxTypeId | TRX_TYPE_ID | — | — |
| 82 | TransactionBatchReversedBatchId | REVERSED_BATCH_ID | — | — |
| 83 | TransactionBatchRunningTotalCr | RUNNING_TOTAL_CR | — | ✅ |
| 84 | TransactionBatchRunningTotalDr | RUNNING_TOTAL_DR | — | ✅ |
| 85 | TransactionBatchStatus | STATUS | — | — |
| 86 | TransactionBatchTrxTypeCode | TRX_TYPE_CODE | — | ✅ |
| 87 | TransactionBatchTrxTypeId | TRX_TYPE_ID | — | — |

### [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DailyConversionTypeConversionType | CONVERSION_TYPE | — | — |
| 2 | DailyConversionTypeCreatedBy | CREATED_BY | — | — |
| 3 | DailyConversionTypeCreationDate | CREATION_DATE | — | — |
| 4 | DailyConversionTypeDescription | DESCRIPTION | — | — |
| 5 | DailyConversionTypeEnableCrossRateFlag | ENABLE_CROSS_RATE_FLAG | — | — |
| 6 | DailyConversionTypeEnforceInverseRateFlag | ENFORCE_INVERSE_RATE_FLAG | — | — |
| 7 | DailyConversionTypeFemEnabledFlag | FEM_ENABLED_FLAG | — | — |
| 8 | DailyConversionTypeFemRateTypeCode | FEM_RATE_TYPE_CODE | — | — |
| 9 | DailyConversionTypeFemScenario | FEM_SCENARIO | — | — |
| 10 | DailyConversionTypeFemTimeframe | FEM_TIMEFRAME | — | — |
| 11 | DailyConversionTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | DailyConversionTypeLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | DailyConversionTypeLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | DailyConversionTypeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | DailyConversionTypePivotCurrencyCode | PIVOT_CURRENCY_CODE | — | — |
| 16 | DailyConversionTypeSecurityFlag | SECURITY_FLAG | — | — |
| 17 | DailyConversionTypeUserConversionType | USER_CONVERSION_TYPE | — | — |
| 18 | DailyConversionTypeUserOverrideCrossRateFlag | USER_OVERRIDE_CROSS_RATE_FLAG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
