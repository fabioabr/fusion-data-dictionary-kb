---
id: DOC-AR-PVO-RateAdjustmentPVO
doc_type: system-doc
title: "RateAdjustmentPVO — PVO Accounts Receivable"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ar
  - data-dictionary
  - pvo
  - bicc
aliases:
  - RateAdjustmentPVO
  - rateadjustmentpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RateAdjustmentPVO

## 📌 Visão Geral

Extrai os ajustes de taxa de câmbio aplicados a recebimentos em moeda estrangeira, com taxas original e ajustada, ganho/perda cambial e data. Essencial para gestão de exposição cambial e contabilização de variações de câmbio em operações internacionais.

**Caminho:** `FscmTopModelAM.FinArTopPublicModelAM.RateAdjustmentPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 81 | 6 | 1 | 19 | 23% |

---

## 🔗 Tabelas Relacionadas

- [[ar_cash_receipts_all|AR_CASH_RECEIPTS_ALL]] — 2 atributos
- [[ar_rate_adjustments_all|AR_RATE_ADJUSTMENTS_ALL]] — 24 atributos (1 PKs, 15 BICC)
- [[fun_bu_perf_v|FUN_BU_PERF_V]] — 1 atributos
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 36 atributos (4 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos
- [[per_users|PER_USERS]] — 8 atributos

---

## ⚙️ Atributos

### [[ar_cash_receipts_all|AR_CASH_RECEIPTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReceiptCashReceiptId | CASH_RECEIPT_ID | — | — |
| 2 | ReceiptSetOfBooksId | SET_OF_BOOKS_ID | — | — |

### [[ar_rate_adjustments_all|AR_RATE_ADJUSTMENTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RateAdjustmentId | RATE_ADJUSTMENT_ID | 🔑 | ✅ |
| 2 | ReceiptRateAdjustmentCashReceiptId | CASH_RECEIPT_ID | — | — |
| 3 | ReceiptRateAdjustmentCreatedBy | CREATED_BY | — | ✅ |
| 4 | ReceiptRateAdjustmentCreatedFrom | CREATED_FROM | — | — |
| 5 | ReceiptRateAdjustmentCreationDate | CREATION_DATE | — | ✅ |
| 6 | ReceiptRateAdjustmentGainLoss | GAIN_LOSS | — | ✅ |
| 7 | ReceiptRateAdjustmentGlDate | GL_DATE | — | ✅ |
| 8 | ReceiptRateAdjustmentGlPostedDate | GL_POSTED_DATE | — | ✅ |
| 9 | ReceiptRateAdjustmentLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | ReceiptRateAdjustmentLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | ReceiptRateAdjustmentLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | ReceiptRateAdjustmentNewExchangeDate | NEW_EXCHANGE_DATE | — | ✅ |
| 13 | ReceiptRateAdjustmentNewExchangeRate | NEW_EXCHANGE_RATE | — | ✅ |
| 14 | ReceiptRateAdjustmentNewExchangeRateType | NEW_EXCHANGE_RATE_TYPE | — | ✅ |
| 15 | ReceiptRateAdjustmentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | ReceiptRateAdjustmentOldExchangeDate | OLD_EXCHANGE_DATE | — | ✅ |
| 17 | ReceiptRateAdjustmentOldExchangeRate | OLD_EXCHANGE_RATE | — | ✅ |
| 18 | ReceiptRateAdjustmentOldExchangeRateType | OLD_EXCHANGE_RATE_TYPE | — | ✅ |
| 19 | ReceiptRateAdjustmentOrgId | ORG_ID | — | — |
| 20 | ReceiptRateAdjustmentPostingControlId | POSTING_CONTROL_ID | — | ✅ |
| 21 | ReceiptRateAdjustmentProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 22 | ReceiptRateAdjustmentProgramId | PROGRAM_ID | — | — |
| 23 | ReceiptRateAdjustmentProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 24 | ReceiptRateAdjustmentRequestId | REQUEST_ID | — | — |

### [[fun_bu_perf_v|FUN_BU_PERF_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitBusinessUnitId | BU_ID | — | — |

### [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NewExcRateConversionType | CONVERSION_TYPE | — | — |
| 2 | NewExcRateCreatedBy | CREATED_BY | — | — |
| 3 | NewExcRateCreationDate | CREATION_DATE | — | — |
| 4 | NewExcRateDescription | DESCRIPTION | — | — |
| 5 | NewExcRateEnableCrossRateFlag | ENABLE_CROSS_RATE_FLAG | — | — |
| 6 | NewExcRateEnforceInverseRateFlag | ENFORCE_INVERSE_RATE_FLAG | — | — |
| 7 | NewExcRateFemEnabledFlag | FEM_ENABLED_FLAG | — | — |
| 8 | NewExcRateFemRateTypeCode | FEM_RATE_TYPE_CODE | — | — |
| 9 | NewExcRateFemScenario | FEM_SCENARIO | — | — |
| 10 | NewExcRateFemTimeframe | FEM_TIMEFRAME | — | — |
| 11 | NewExcRateLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | NewExcRateLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | NewExcRateLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | NewExcRateObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | NewExcRatePivotCurrencyCode | PIVOT_CURRENCY_CODE | — | — |
| 16 | NewExcRateSecurityFlag | SECURITY_FLAG | — | — |
| 17 | NewExcRateUserConversionType | USER_CONVERSION_TYPE | — | ✅ |
| 18 | NewExcRateUserOverrideCrossRateFlag | USER_OVERRIDE_CROSS_RATE_FLAG | — | — |
| 19 | OldExcRateConversionType | CONVERSION_TYPE | — | — |
| 20 | OldExcRateCreatedBy | CREATED_BY | — | — |
| 21 | OldExcRateCreationDate | CREATION_DATE | — | — |
| 22 | OldExcRateDescription | DESCRIPTION | — | — |
| 23 | OldExcRateEnableCrossRateFlag | ENABLE_CROSS_RATE_FLAG | — | — |
| 24 | OldExcRateEnforceInverseRateFlag | ENFORCE_INVERSE_RATE_FLAG | — | — |
| 25 | OldExcRateFemEnabledFlag | FEM_ENABLED_FLAG | — | — |
| 26 | OldExcRateFemRateTypeCode | FEM_RATE_TYPE_CODE | — | — |
| 27 | OldExcRateFemScenario | FEM_SCENARIO | — | — |
| 28 | OldExcRateFemTimeframe | FEM_TIMEFRAME | — | — |
| 29 | OldExcRateLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 30 | OldExcRateLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 31 | OldExcRateLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 32 | OldExcRateObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 33 | OldExcRatePivotCurrencyCode | PIVOT_CURRENCY_CODE | — | — |
| 34 | OldExcRateSecurityFlag | SECURITY_FLAG | — | — |
| 35 | OldExcRateUserConversionType | USER_CONVERSION_TYPE | — | ✅ |
| 36 | OldExcRateUserOverrideCrossRateFlag | USER_OVERRIDE_CROSS_RATE_FLAG | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonCreatedByDisplayName | DISPLAY_NAME | — | — |
| 2 | PersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | PersonCreatedByPersonId | PERSON_ID | — | — |
| 5 | PersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | PersonUpdatedByDisplayName | DISPLAY_NAME | — | — |
| 7 | PersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | PersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | PersonUpdatedByPersonId | PERSON_ID | — | — |
| 10 | PersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserCreatedByPersonId | PERSON_ID | — | — |
| 2 | UserCreatedByUserGuid | USER_GUID | — | — |
| 3 | UserCreatedByUserId | USER_ID | — | — |
| 4 | UserCreatedByUsername | USERNAME | — | — |
| 5 | UserUpdatedByPersonId | PERSON_ID | — | — |
| 6 | UserUpdatedByUserGuid | USER_GUID | — | — |
| 7 | UserUpdatedByUserId | USER_ID | — | — |
| 8 | UserUpdatedByUsername | USERNAME | — | — |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
