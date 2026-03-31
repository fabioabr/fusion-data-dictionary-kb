---
id: DOC-OTHER-PVO-FaBalancesExtractPVO
doc_type: system-doc
title: "FaBalancesExtractPVO — PVO Cross-Module"
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
  - FaBalancesExtractPVO
  - fabalancesextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FaBalancesExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fa Balances Extract. Acessa as tabelas: FA_BALANCES_EXTRACT, FA_BOOK_CONTROLS, FA_TRANSACTION_HEADERS (+4).

**Caminho:** `FscmTopModelAM.FinFaSharedUtilAM.FaBalancesExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 84 | 7 | 1 | 29 | 35% |

---

## 🔗 Tabelas Relacionadas

- [[fa_balances_extract|FA_BALANCES_EXTRACT]] — 49 atributos (1 PKs, 26 BICC)
- [[fa_book_controls|FA_BOOK_CONTROLS]] — 4 atributos
- [[fa_transaction_headers|FA_TRANSACTION_HEADERS]] — 3 atributos (1 BICC)
- [[gl_ledgers|GL_LEDGERS]] — 3 atributos
- [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]] — 5 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos (2 BICC)
- [[per_users|PER_USERS]] — 10 atributos

---

## ⚙️ Atributos

### [[fa_balances_extract|FA_BALANCES_EXTRACT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BeginningBalance | BEGINNING_BALANCE | — | — |
| 2 | FaBalanceExtractAccountCcid | ACCOUNT_CCID | — | — |
| 3 | FaBalanceExtractAccountType | ACCOUNT_TYPE | — | ✅ |
| 4 | FaBalanceExtractAccountingClassCode | ACCOUNTING_CLASS_CODE | — | ✅ |
| 5 | FaBalanceExtractAccountingEntryStatusCode | ACCOUNTING_ENTRY_STATUS_CODE | — | ✅ |
| 6 | FaBalanceExtractAdjustmentLineId | ADJUSTMENT_LINE_ID | — | — |
| 7 | FaBalanceExtractAeHeaderId | AE_HEADER_ID | — | — |
| 8 | FaBalanceExtractAeLineNum | AE_LINE_NUM | — | ✅ |
| 9 | FaBalanceExtractAmount | AMOUNT | — | — |
| 10 | FaBalanceExtractAssetId | ASSET_ID | — | — |
| 11 | FaBalanceExtractAssetType | ASSET_TYPE | — | — |
| 12 | FaBalanceExtractBalancesExtractId | BALANCES_EXTRACT_ID | 🔑 | ✅ |
| 13 | FaBalanceExtractBookTypeCode | BOOK_TYPE_CODE | — | — |
| 14 | FaBalanceExtractCategoryBookDefaultId | CATEGORY_BOOK_DEFAULT_ID | — | — |
| 15 | FaBalanceExtractCategoryId | CATEGORY_ID | — | — |
| 16 | FaBalanceExtractCreatedBy | CREATED_BY | — | ✅ |
| 17 | FaBalanceExtractCreationDate | CREATION_DATE | — | ✅ |
| 18 | FaBalanceExtractCurrencyCode | CURRENCY_CODE | — | ✅ |
| 19 | FaBalanceExtractDeprnRunDate | DEPRN_RUN_DATE | — | ✅ |
| 20 | FaBalanceExtractDeprnRunId | DEPRN_RUN_ID | — | — |
| 21 | FaBalanceExtractDeprnSourceCode | DEPRN_SOURCE_CODE | — | ✅ |
| 22 | FaBalanceExtractDistCcid | DIST_CCID | — | — |
| 23 | FaBalanceExtractDistributionId | DISTRIBUTION_ID | — | ✅ |
| 24 | FaBalanceExtractEmployeeId | EMPLOYEE_ID | — | — |
| 25 | FaBalanceExtractEventId | EVENT_ID | — | — |
| 26 | FaBalanceExtractEventTypeCode | EVENT_TYPE_CODE | — | ✅ |
| 27 | FaBalanceExtractGlSlLinkId | GL_SL_LINK_ID | — | ✅ |
| 28 | FaBalanceExtractGlSlLinkTable | GL_SL_LINK_TABLE | — | ✅ |
| 29 | FaBalanceExtractGlTransferStatusCode | GL_TRANSFER_STATUS_CODE | — | ✅ |
| 30 | FaBalanceExtractGroupAssetId | GROUP_ASSET_ID | — | — |
| 31 | FaBalanceExtractLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 32 | FaBalanceExtractLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 33 | FaBalanceExtractLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 34 | FaBalanceExtractLedgerId | LEDGER_ID | — | — |
| 35 | FaBalanceExtractLocationId | LOCATION_ID | — | — |
| 36 | FaBalanceExtractMassTransactionId | MASS_TRANSACTION_ID | — | — |
| 37 | FaBalanceExtractPeriodCounter | PERIOD_COUNTER | — | — |
| 38 | FaBalanceExtractPeriodName | PERIOD_NAME | — | ✅ |
| 39 | FaBalanceExtractSourceDestCode | SOURCE_DEST_CODE | — | ✅ |
| 40 | FaBalanceExtractSourceDistributionType | SOURCE_DISTRIBUTION_TYPE | — | ✅ |
| 41 | FaBalanceExtractSourceLineId | SOURCE_LINE_ID | — | — |
| 42 | FaBalanceExtractSourceTable | SOURCE_TABLE | — | — |
| 43 | FaBalanceExtractSourceTypeCode | SOURCE_TYPE_CODE | — | ✅ |
| 44 | FaBalanceExtractTotalUnits | TOTAL_UNITS | — | ✅ |
| 45 | FaBalanceExtractTransactionHeaderId | TRANSACTION_HEADER_ID | — | — |
| 46 | FaBalanceExtractTransactionKey | TRANSACTION_KEY | — | ✅ |
| 47 | FaBalanceExtractTransactionTypeCode | TRANSACTION_TYPE_CODE | — | ✅ |
| 48 | FaBalanceExtractUnitRatio | UNIT_RATIO | — | ✅ |
| 49 | FaBalanceExtractUnitsAssigned | UNITS_ASSIGNED | — | ✅ |

### [[fa_book_controls|FA_BOOK_CONTROLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BookControlPEOBookControlId | BOOK_CONTROL_ID | — | — |
| 2 | BookControlPEOBookTypeCode | BOOK_TYPE_CODE | — | — |
| 3 | BookControlPEOBookTypeName | BOOK_TYPE_NAME | — | — |
| 4 | BookControlPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |

### [[fa_transaction_headers|FA_TRANSACTION_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionHeaderPEOBookTypeCode | BOOK_TYPE_CODE | — | — |
| 2 | TransactionHeaderPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 3 | TransactionHeaderPEOTransactionHeaderId | TRANSACTION_HEADER_ID | — | ✅ |

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LedgerPEOChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 2 | LedgerPEOLedgerId | LEDGER_ID | — | — |
| 3 | LedgerPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentPEOAssignmentId | ASSIGNMENT_ID | — | — |
| 2 | AssignmentPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | AssignmentPEOEffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | — |
| 4 | AssignmentPEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 5 | AssignmentPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | PersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | PersonCreatedByPersonId | PERSON_ID | — | — |
| 5 | PersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | PersonId | PERSON_ID | — | — |
| 7 | PersonNameId | PERSON_NAME_ID | — | — |
| 8 | PersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 9 | PersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 10 | PersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserCreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | UserCreatedByPersonId | PERSON_ID | — | — |
| 3 | UserCreatedByUserGuid | USER_GUID | — | — |
| 4 | UserCreatedByUserId | USER_ID | — | — |
| 5 | UserCreatedByUsername | USERNAME | — | — |
| 6 | UserUpdatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | UserUpdatedByPersonId | PERSON_ID | — | — |
| 8 | UserUpdatedByUserGuid | USER_GUID | — | — |
| 9 | UserUpdatedByUserId | USER_ID | — | — |
| 10 | UserUpdatedByUsername | USERNAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
