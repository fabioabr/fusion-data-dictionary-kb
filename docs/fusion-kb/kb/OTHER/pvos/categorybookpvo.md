---
id: DOC-OTHER-PVO-CategoryBookPVO
doc_type: system-doc
title: "CategoryBookPVO — PVO Cross-Module"
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
  - CategoryBookPVO
  - categorybookpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CategoryBookPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Category Book. Acessa as tabelas: FA_BOOK_CONTROLS, FA_CATEGORY_BOOKS, PER_PERSON_NAMES_F_V (+1).

**Caminho:** `FscmTopModelAM.FinFaDeprnSetupCategoriesAM.CategoryBookPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 56 | 4 | 1 | 7 | 12% |

---

## 🔗 Tabelas Relacionadas

- [[fa_book_controls|FA_BOOK_CONTROLS]] — 5 atributos
- [[fa_category_books|FA_CATEGORY_BOOKS]] — 31 atributos (1 PKs, 5 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos (2 BICC)
- [[per_users|PER_USERS]] — 10 atributos

---

## ⚙️ Atributos

### [[fa_book_controls|FA_BOOK_CONTROLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccountingFlexStructure | ACCOUNTING_FLEX_STRUCTURE | — | — |
| 2 | BookControlId | BOOK_CONTROL_ID | — | — |
| 3 | BookTypeCode1 | BOOK_TYPE_CODE | — | — |
| 4 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 5 | SetOfBooksId | SET_OF_BOOKS_ID | — | — |

### [[fa_category_books|FA_CATEGORY_BOOKS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AltCostAccountCcid | ALT_COST_ACCOUNT_CCID | — | — |
| 2 | AssetClearingAccountCcid | ASSET_CLEARING_ACCOUNT_CCID | — | — |
| 3 | AssetCostAccountCcid | ASSET_COST_ACCOUNT_CCID | — | — |
| 4 | BonusExpenseAccountCcid | BONUS_EXPENSE_ACCOUNT_CCID | — | — |
| 5 | BonusReserveAcctCcid | BONUS_RESERVE_ACCT_CCID | — | — |
| 6 | BookTypeCode | BOOK_TYPE_CODE | — | — |
| 7 | CapitalAdjAccountCcid | CAPITAL_ADJ_ACCOUNT_CCID | — | — |
| 8 | CategoryBookId | CATEGORY_BOOK_ID | 🔑 | ✅ |
| 9 | CategoryId | CATEGORY_ID | — | — |
| 10 | CostWriteOffAccountCcid | COST_WRITE_OFF_ACCOUNT_CCID | — | — |
| 11 | CreatedBy | CREATED_BY | — | ✅ |
| 12 | CreationDate | CREATION_DATE | — | ✅ |
| 13 | DeprnExpenseAccountCcid | DEPRN_EXPENSE_ACCOUNT_CCID | — | — |
| 14 | GeneralFundAccountCcid | GENERAL_FUND_ACCOUNT_CCID | — | — |
| 15 | ImpairExpenseAccountCcid | IMPAIR_EXPENSE_ACCOUNT_CCID | — | — |
| 16 | ImpairExpenseAccountCcid1 | IMPAIR_EXPENSE_ACCOUNT_CCID | — | — |
| 17 | ImpairReserveAccountCcid | IMPAIR_RESERVE_ACCOUNT_CCID | — | — |
| 18 | ImpairReserveAccountCcid1 | IMPAIR_RESERVE_ACCOUNT_CCID | — | — |
| 19 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 20 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 21 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 22 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 23 | ReserveAccountCcid | RESERVE_ACCOUNT_CCID | — | — |
| 24 | RevalAmortAccountCcid | REVAL_AMORT_ACCOUNT_CCID | — | — |
| 25 | RevalLossAccountCcid | REVAL_LOSS_ACCOUNT_CCID | — | — |
| 26 | RevalReserveAccountCcid | REVAL_RESERVE_ACCOUNT_CCID | — | — |
| 27 | UnplanExpenseAccountCcid | UNPLAN_EXPENSE_ACCOUNT_CCID | — | — |
| 28 | WipClearingAccountCcid | WIP_CLEARING_ACCOUNT_CCID | — | — |
| 29 | WipCostAccountCcid | WIP_COST_ACCOUNT_CCID | — | — |
| 30 | WriteOffAccountCcid | WRITE_OFF_ACCOUNT_CCID | — | — |
| 31 | WriteOffAccountCcid1 | WRITE_OFF_ACCOUNT_CCID | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | PersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | PersonCreatedByPersonId | PERSON_ID | — | — |
| 5 | PersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | PersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 7 | PersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | PersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | PersonUpdatedByPersonId | PERSON_ID | — | — |
| 10 | PersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

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
