---
id: DOC-OTHER-PVO-SupportingReferenceBalancePVO
doc_type: system-doc
title: "SupportingReferenceBalancePVO — PVO Cross-Module"
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
  - SupportingReferenceBalancePVO
  - supportingreferencebalancepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupportingReferenceBalancePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Supporting Reference Balance. Acessa as tabelas: GL_LEDGERS, PER_PERSON_NAMES_F_V, PER_USERS (+5).

**Caminho:** `FscmTopModelAM.FinXlaBalInqSuppRefBalAM.SupportingReferenceBalancePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 183 | 8 | 1 | 95 | 52% |

---

## 🔗 Tabelas Relacionadas

- [[gl_ledgers|GL_LEDGERS]] — 3 atributos (2 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos (3 BICC)
- [[per_users|PER_USERS]] — 10 atributos
- [[xla_ac_balances|XLA_AC_BALANCES]] — 67 atributos (1 PKs, 64 BICC)
- [[xla_gl_ledgers|XLA_GL_LEDGERS]] — 2 atributos
- [[xla_subledgers|XLA_SUBLEDGERS]] — 18 atributos (18 BICC)
- [[xla_subledgers_vl|XLA_SUBLEDGERS_VL]] — 7 atributos (7 BICC)
- [[xla_sup_ref_combinations|XLA_SUP_REF_COMBINATIONS]] — 66 atributos (1 BICC)

---

## ⚙️ Atributos

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LedgersChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | ✅ |
| 2 | LedgersLedgerId | LEDGER_ID | — | ✅ |
| 3 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonCreatedByDisplayName | DISPLAY_NAME | — | — |
| 2 | PersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | PersonCreatedByPersonId | PERSON_ID | — | — |
| 5 | PersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | PersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 7 | PersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | PersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
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

### [[xla_ac_balances|XLA_AC_BALANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AcBalanceId | AC_BALANCE_ID | 🔑 | ✅ |
| 2 | SupportingBalRef1 | SR1 | — | ✅ |
| 3 | SupportingBalRef10 | SR10 | — | ✅ |
| 4 | SupportingBalRef11 | SR11 | — | ✅ |
| 5 | SupportingBalRef12 | SR12 | — | ✅ |
| 6 | SupportingBalRef13 | SR13 | — | ✅ |
| 7 | SupportingBalRef14 | SR14 | — | ✅ |
| 8 | SupportingBalRef15 | SR15 | — | ✅ |
| 9 | SupportingBalRef16 | SR16 | — | ✅ |
| 10 | SupportingBalRef17 | SR17 | — | ✅ |
| 11 | SupportingBalRef18 | SR18 | — | ✅ |
| 12 | SupportingBalRef19 | SR19 | — | ✅ |
| 13 | SupportingBalRef2 | SR2 | — | ✅ |
| 14 | SupportingBalRef20 | SR20 | — | ✅ |
| 15 | SupportingBalRef21 | SR21 | — | ✅ |
| 16 | SupportingBalRef22 | SR22 | — | ✅ |
| 17 | SupportingBalRef23 | SR23 | — | ✅ |
| 18 | SupportingBalRef24 | SR24 | — | ✅ |
| 19 | SupportingBalRef25 | SR25 | — | ✅ |
| 20 | SupportingBalRef26 | SR26 | — | ✅ |
| 21 | SupportingBalRef27 | SR27 | — | ✅ |
| 22 | SupportingBalRef28 | SR28 | — | ✅ |
| 23 | SupportingBalRef29 | SR29 | — | ✅ |
| 24 | SupportingBalRef3 | SR3 | — | ✅ |
| 25 | SupportingBalRef30 | SR30 | — | ✅ |
| 26 | SupportingBalRef4 | SR4 | — | ✅ |
| 27 | SupportingBalRef5 | SR5 | — | ✅ |
| 28 | SupportingBalRef6 | SR6 | — | ✅ |
| 29 | SupportingBalRef7 | SR7 | — | ✅ |
| 30 | SupportingBalRef8 | SR8 | — | ✅ |
| 31 | SupportingBalRef9 | SR9 | — | ✅ |
| 32 | SupportingRefBalAc1 | AC1 | — | ✅ |
| 33 | SupportingRefBalAc2 | AC2 | — | ✅ |
| 34 | SupportingRefBalAc3 | AC3 | — | ✅ |
| 35 | SupportingRefBalAc4 | AC4 | — | ✅ |
| 36 | SupportingRefBalAc5 | AC5 | — | ✅ |
| 37 | SupportingRefBalAmbContextCode | AMB_CONTEXT_CODE | — | — |
| 38 | SupportingRefBalAnalyticalCriterionCode | ANALYTICAL_CRITERION_CODE | — | — |
| 39 | SupportingRefBalAnalyticalCriterionTypeCode | ANALYTICAL_CRITERION_TYPE_CODE | — | — |
| 40 | SupportingRefBalApplicationId | APPLICATION_ID | — | ✅ |
| 41 | SupportingRefBalBeginningBalanceCr | BEGINNING_BALANCE_CR | — | ✅ |
| 42 | SupportingRefBalBeginningBalanceDr | BEGINNING_BALANCE_DR | — | ✅ |
| 43 | SupportingRefBalCodeCombinationId | CODE_COMBINATION_ID | — | ✅ |
| 44 | SupportingRefBalCreatedBy | CREATED_BY | — | ✅ |
| 45 | SupportingRefBalCreationDate | CREATION_DATE | — | ✅ |
| 46 | SupportingRefBalEnteredCurBeginBalCr | ENTERED_CUR_BEGIN_BAL_CR | — | ✅ |
| 47 | SupportingRefBalEnteredCurBeginBalDr | ENTERED_CUR_BEGIN_BAL_DR | — | ✅ |
| 48 | SupportingRefBalEnteredCurrencyCode | ENTERED_CURRENCY_CODE | — | ✅ |
| 49 | SupportingRefBalFirstPeriodFlag | FIRST_PERIOD_FLAG | — | ✅ |
| 50 | SupportingRefBalInitialBalanceFlag | INITIAL_BALANCE_FLAG | — | ✅ |
| 51 | SupportingRefBalJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 52 | SupportingRefBalJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 53 | SupportingRefBalLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 54 | SupportingRefBalLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 55 | SupportingRefBalLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 56 | SupportingRefBalLedgerId | LEDGER_ID | — | ✅ |
| 57 | SupportingRefBalObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 58 | SupportingRefBalPeriodBalanceCr | PERIOD_BALANCE_CR | — | ✅ |
| 59 | SupportingRefBalPeriodBalanceDr | PERIOD_BALANCE_DR | — | ✅ |
| 60 | SupportingRefBalPeriodEnteredBalanceCr | PERIOD_ENTERED_BALANCE_CR | — | ✅ |
| 61 | SupportingRefBalPeriodEnteredBalanceDr | PERIOD_ENTERED_BALANCE_DR | — | ✅ |
| 62 | SupportingRefBalPeriodName | PERIOD_NAME | — | ✅ |
| 63 | SupportingRefBalPeriodYear | PERIOD_YEAR | — | ✅ |
| 64 | SupportingRefBalRequestId | REQUEST_ID | — | ✅ |
| 65 | SupportingRefBalSuppRefCombinationId | SUPP_REF_COMBINATION_ID | — | ✅ |
| 66 | SupportingRefBalSuppRefValues | SUPP_REF_VALUES | — | ✅ |
| 67 | SupportingRefBalTransferredToEssbase | TRANSFERRED_TO_ESSBASE | — | ✅ |

### [[xla_gl_ledgers|XLA_GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | XlaGlLedgersLedgerId | LEDGER_ID | — | — |
| 2 | XlaGlLedgersObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[xla_subledgers|XLA_SUBLEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SubledgerApplnSetupAccountingEnabled | ACCOUNTING_ENABLED | — | ✅ |
| 2 | SubledgerApplnSetupAlcEnabledFlag | ALC_ENABLED_FLAG | — | ✅ |
| 3 | SubledgerApplnSetupApplicationId | APPLICATION_ID | — | ✅ |
| 4 | SubledgerApplnSetupApplicationShortName | APPLICATION_SHORT_NAME | — | ✅ |
| 5 | SubledgerApplnSetupApplicationTypeCode | APPLICATION_TYPE_CODE | — | ✅ |
| 6 | SubledgerApplnSetupControlAccountTypeCode | CONTROL_ACCOUNT_TYPE_CODE | — | ✅ |
| 7 | SubledgerApplnSetupCreatedBy | CREATED_BY | — | ✅ |
| 8 | SubledgerApplnSetupCreationDate | CREATION_DATE | — | ✅ |
| 9 | SubledgerApplnSetupDrilldownProcedureName | DRILLDOWN_PROCEDURE_NAME | — | ✅ |
| 10 | SubledgerApplnSetupJeSourceName | JE_SOURCE_NAME | — | ✅ |
| 11 | SubledgerApplnSetupLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | SubledgerApplnSetupLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | SubledgerApplnSetupLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | SubledgerApplnSetupObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 15 | SubledgerApplnSetupRemoteUrl | REMOTE_URL | — | ✅ |
| 16 | SubledgerApplnSetupRowLockingFlag | ROW_LOCKING_FLAG | — | ✅ |
| 17 | SubledgerApplnSetupSecurityFunctionName | SECURITY_FUNCTION_NAME | — | ✅ |
| 18 | SubledgerApplnSetupValuationMethodFlag | VALUATION_METHOD_FLAG | — | ✅ |

### [[xla_subledgers_vl|XLA_SUBLEDGERS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | XlaApplnVLApplicationId | APPLICATION_ID | — | ✅ |
| 2 | XlaApplnVLApplicationName | APPLICATION_NAME | — | ✅ |
| 3 | XlaApplnVLApplicationShortName | APPLICATION_SHORT_NAME | — | ✅ |
| 4 | XlaApplnVLDescription | DESCRIPTION | — | ✅ |
| 5 | XlaApplnVLDrilldownProcedureName | DRILLDOWN_PROCEDURE_NAME | — | ✅ |
| 6 | XlaApplnVLJeSourceName | JE_SOURCE_NAME | — | ✅ |
| 7 | XlaApplnVLSecurityFunctionName | SECURITY_FUNCTION_NAME | — | ✅ |

### [[xla_sup_ref_combinations|XLA_SUP_REF_COMBINATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SuppRefCombinationCreatedBy | CREATED_BY | — | — |
| 2 | SuppRefCombinationCreationDate | CREATION_DATE | — | — |
| 3 | SuppRefCombinationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | SuppRefCombinationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 5 | SuppRefCombinationLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 6 | SuppRefCombinationSupRefCode1 | SUP_REF_CODE1 | — | — |
| 7 | SuppRefCombinationSupRefCode10 | SUP_REF_CODE10 | — | — |
| 8 | SuppRefCombinationSupRefCode11 | SUP_REF_CODE11 | — | — |
| 9 | SuppRefCombinationSupRefCode12 | SUP_REF_CODE12 | — | — |
| 10 | SuppRefCombinationSupRefCode13 | SUP_REF_CODE13 | — | — |
| 11 | SuppRefCombinationSupRefCode14 | SUP_REF_CODE14 | — | — |
| 12 | SuppRefCombinationSupRefCode15 | SUP_REF_CODE15 | — | — |
| 13 | SuppRefCombinationSupRefCode16 | SUP_REF_CODE16 | — | — |
| 14 | SuppRefCombinationSupRefCode17 | SUP_REF_CODE17 | — | — |
| 15 | SuppRefCombinationSupRefCode18 | SUP_REF_CODE18 | — | — |
| 16 | SuppRefCombinationSupRefCode19 | SUP_REF_CODE19 | — | — |
| 17 | SuppRefCombinationSupRefCode2 | SUP_REF_CODE2 | — | — |
| 18 | SuppRefCombinationSupRefCode20 | SUP_REF_CODE20 | — | — |
| 19 | SuppRefCombinationSupRefCode21 | SUP_REF_CODE21 | — | — |
| 20 | SuppRefCombinationSupRefCode22 | SUP_REF_CODE22 | — | — |
| 21 | SuppRefCombinationSupRefCode23 | SUP_REF_CODE23 | — | — |
| 22 | SuppRefCombinationSupRefCode24 | SUP_REF_CODE24 | — | — |
| 23 | SuppRefCombinationSupRefCode25 | SUP_REF_CODE25 | — | — |
| 24 | SuppRefCombinationSupRefCode26 | SUP_REF_CODE26 | — | — |
| 25 | SuppRefCombinationSupRefCode27 | SUP_REF_CODE27 | — | — |
| 26 | SuppRefCombinationSupRefCode28 | SUP_REF_CODE28 | — | — |
| 27 | SuppRefCombinationSupRefCode29 | SUP_REF_CODE29 | — | — |
| 28 | SuppRefCombinationSupRefCode3 | SUP_REF_CODE3 | — | — |
| 29 | SuppRefCombinationSupRefCode30 | SUP_REF_CODE30 | — | — |
| 30 | SuppRefCombinationSupRefCode31 | SUP_REF_CODE31 | — | — |
| 31 | SuppRefCombinationSupRefCode32 | SUP_REF_CODE32 | — | — |
| 32 | SuppRefCombinationSupRefCode33 | SUP_REF_CODE33 | — | — |
| 33 | SuppRefCombinationSupRefCode34 | SUP_REF_CODE34 | — | — |
| 34 | SuppRefCombinationSupRefCode35 | SUP_REF_CODE35 | — | — |
| 35 | SuppRefCombinationSupRefCode36 | SUP_REF_CODE36 | — | — |
| 36 | SuppRefCombinationSupRefCode37 | SUP_REF_CODE37 | — | — |
| 37 | SuppRefCombinationSupRefCode38 | SUP_REF_CODE38 | — | — |
| 38 | SuppRefCombinationSupRefCode39 | SUP_REF_CODE39 | — | — |
| 39 | SuppRefCombinationSupRefCode4 | SUP_REF_CODE4 | — | — |
| 40 | SuppRefCombinationSupRefCode40 | SUP_REF_CODE40 | — | — |
| 41 | SuppRefCombinationSupRefCode41 | SUP_REF_CODE41 | — | — |
| 42 | SuppRefCombinationSupRefCode42 | SUP_REF_CODE42 | — | — |
| 43 | SuppRefCombinationSupRefCode43 | SUP_REF_CODE43 | — | — |
| 44 | SuppRefCombinationSupRefCode44 | SUP_REF_CODE44 | — | — |
| 45 | SuppRefCombinationSupRefCode45 | SUP_REF_CODE45 | — | — |
| 46 | SuppRefCombinationSupRefCode46 | SUP_REF_CODE46 | — | — |
| 47 | SuppRefCombinationSupRefCode47 | SUP_REF_CODE47 | — | — |
| 48 | SuppRefCombinationSupRefCode48 | SUP_REF_CODE48 | — | — |
| 49 | SuppRefCombinationSupRefCode49 | SUP_REF_CODE49 | — | — |
| 50 | SuppRefCombinationSupRefCode5 | SUP_REF_CODE5 | — | — |
| 51 | SuppRefCombinationSupRefCode50 | SUP_REF_CODE50 | — | — |
| 52 | SuppRefCombinationSupRefCode51 | SUP_REF_CODE51 | — | — |
| 53 | SuppRefCombinationSupRefCode52 | SUP_REF_CODE52 | — | — |
| 54 | SuppRefCombinationSupRefCode53 | SUP_REF_CODE53 | — | — |
| 55 | SuppRefCombinationSupRefCode54 | SUP_REF_CODE54 | — | — |
| 56 | SuppRefCombinationSupRefCode55 | SUP_REF_CODE55 | — | — |
| 57 | SuppRefCombinationSupRefCode56 | SUP_REF_CODE56 | — | — |
| 58 | SuppRefCombinationSupRefCode57 | SUP_REF_CODE57 | — | — |
| 59 | SuppRefCombinationSupRefCode58 | SUP_REF_CODE58 | — | — |
| 60 | SuppRefCombinationSupRefCode59 | SUP_REF_CODE59 | — | — |
| 61 | SuppRefCombinationSupRefCode6 | SUP_REF_CODE6 | — | — |
| 62 | SuppRefCombinationSupRefCode60 | SUP_REF_CODE60 | — | — |
| 63 | SuppRefCombinationSupRefCode7 | SUP_REF_CODE7 | — | — |
| 64 | SuppRefCombinationSupRefCode8 | SUP_REF_CODE8 | — | — |
| 65 | SuppRefCombinationSupRefCode9 | SUP_REF_CODE9 | — | — |
| 66 | SuppRefCombinationSuppRefCombinationId | SUPP_REF_COMBINATION_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
