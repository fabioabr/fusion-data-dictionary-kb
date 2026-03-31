---
id: DOC-OTHER-PVO-SubledgerControlBalancePVO
doc_type: system-doc
title: "SubledgerControlBalancePVO — PVO Cross-Module"
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
  - SubledgerControlBalancePVO
  - subledgercontrolbalancepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SubledgerControlBalancePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Subledger Control Balance. Acessa as tabelas: GL_CODE_COMBINATIONS, GL_LEDGERS, XLA_CONTROL_BALANCES (+2).

**Caminho:** `FscmTopModelAM.FinXlaBalInqConBalPublicModelAM.SubledgerControlBalancePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 69 | 5 | 8 | 69 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gl_code_combinations|GL_CODE_COMBINATIONS]] — 12 atributos (12 BICC)
- [[gl_ledgers|GL_LEDGERS]] — 17 atributos (1 PKs, 17 BICC)
- [[xla_control_balances|XLA_CONTROL_BALANCES]] — 27 atributos (7 PKs, 27 BICC)
- [[xla_subledgers|XLA_SUBLEDGERS]] — 6 atributos (6 BICC)
- [[xla_subledgers_vl|XLA_SUBLEDGERS_VL]] — 7 atributos (7 BICC)

---

## ⚙️ Atributos

### [[gl_code_combinations|GL_CODE_COMBINATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CodeCombinationAccountType | ACCOUNT_TYPE | — | ✅ |
| 2 | CodeCombinationAllocationCreateFlag | ALLOCATION_CREATE_FLAG | — | ✅ |
| 3 | CodeCombinationAlternateCodeCombinationId | ALTERNATE_CODE_COMBINATION_ID | — | ✅ |
| 4 | CodeCombinationChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | ✅ |
| 5 | CodeCombinationCodeCombinationId | CODE_COMBINATION_ID | — | ✅ |
| 6 | CodeCombinationFinancialCategory | FINANCIAL_CATEGORY | — | ✅ |
| 7 | CodeCombinationLedgerSegment | LEDGER_SEGMENT | — | ✅ |
| 8 | CodeCombinationLedgerTypeCode | LEDGER_TYPE_CODE | — | ✅ |
| 9 | CodeCombinationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | CodeCombinationRevaluationId | REVALUATION_ID | — | ✅ |
| 11 | CodeCombinationStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 12 | CodeCombinationTemplateId | TEMPLATE_ID | — | ✅ |

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlLedgersAccountedPeriodType | ACCOUNTED_PERIOD_TYPE | — | ✅ |
| 2 | GlLedgersAlcLedgerTypeCode | ALC_LEDGER_TYPE_CODE | — | ✅ |
| 3 | GlLedgersAllowIntercompanyPostFlag | ALLOW_INTERCOMPANY_POST_FLAG | — | ✅ |
| 4 | GlLedgersApDocSequencingOptionFlag | AP_DOC_SEQUENCING_OPTION_FLAG | — | ✅ |
| 5 | GlLedgersBalSegValueSetId | BAL_SEG_VALUE_SET_ID | — | ✅ |
| 6 | GlLedgersBudgetPeriodAvgRateType | BUDGET_PERIOD_AVG_RATE_TYPE | — | ✅ |
| 7 | GlLedgersBudgetPeriodEndRateType | BUDGET_PERIOD_END_RATE_TYPE | — | ✅ |
| 8 | GlLedgersChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | ✅ |
| 9 | GlLedgersConfigurationId | CONFIGURATION_ID | — | ✅ |
| 10 | GlLedgersConsolidationLedgerFlag | CONSOLIDATION_LEDGER_FLAG | — | ✅ |
| 11 | GlLedgersCurrencyCode | CURRENCY_CODE | — | ✅ |
| 12 | GlLedgersJrnlsGroupByDateFlag | JRNLS_GROUP_BY_DATE_FLAG | — | ✅ |
| 13 | GlLedgersLedgerCategoryCode | LEDGER_CATEGORY_CODE | — | ✅ |
| 14 | GlLedgersLedgerId | LEDGER_ID | 🔑 | ✅ |
| 15 | GlLedgersNetIncomeCodeCombinationId | NET_INCOME_CODE_COMBINATION_ID | — | ✅ |
| 16 | GlLedgersObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 17 | GlLedgersPeriodSetName | PERIOD_SET_NAME | — | ✅ |

### [[xla_control_balances|XLA_CONTROL_BALANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApplicationId | APPLICATION_ID | 🔑 | ✅ |
| 2 | CodeCombinationId | CODE_COMBINATION_ID | 🔑 | ✅ |
| 3 | ControlBalancesBeginningBalanceCr | BEGINNING_BALANCE_CR | — | ✅ |
| 4 | ControlBalancesBeginningBalanceDr | BEGINNING_BALANCE_DR | — | ✅ |
| 5 | ControlBalancesCreatedBy | CREATED_BY | — | ✅ |
| 6 | ControlBalancesCreationDate | CREATION_DATE | — | ✅ |
| 7 | ControlBalancesDraftBeginningBalanceCr | DRAFT_BEGINNING_BALANCE_CR | — | ✅ |
| 8 | ControlBalancesDraftBeginningBalanceDr | DRAFT_BEGINNING_BALANCE_DR | — | ✅ |
| 9 | ControlBalancesFirstPeriodFlag | FIRST_PERIOD_FLAG | — | ✅ |
| 10 | ControlBalancesInitialBalanceFlag | INITIAL_BALANCE_FLAG | — | ✅ |
| 11 | ControlBalancesJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 12 | ControlBalancesJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 13 | ControlBalancesLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | ControlBalancesLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 15 | ControlBalancesLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | ControlBalancesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 17 | ControlBalancesPeriodBalanceCr | PERIOD_BALANCE_CR | — | ✅ |
| 18 | ControlBalancesPeriodBalanceDr | PERIOD_BALANCE_DR | — | ✅ |
| 19 | ControlBalancesPeriodDraftBalanceCr | PERIOD_DRAFT_BALANCE_CR | — | ✅ |
| 20 | ControlBalancesPeriodDraftBalanceDr | PERIOD_DRAFT_BALANCE_DR | — | ✅ |
| 21 | ControlBalancesPeriodYear | PERIOD_YEAR | — | ✅ |
| 22 | ControlBalancesRequestId | REQUEST_ID | — | ✅ |
| 23 | LedgerId | LEDGER_ID | 🔑 | ✅ |
| 24 | PartyId | PARTY_ID | 🔑 | ✅ |
| 25 | PartySiteId | PARTY_SITE_ID | 🔑 | ✅ |
| 26 | PartyTypeCode | PARTY_TYPE_CODE | 🔑 | ✅ |
| 27 | PeriodName | PERIOD_NAME | 🔑 | ✅ |

### [[xla_subledgers|XLA_SUBLEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SubledgerApplicationSetupApplicationId | APPLICATION_ID | — | ✅ |
| 2 | SubledgerApplicationSetupApplicationTypeCode | APPLICATION_TYPE_CODE | — | ✅ |
| 3 | SubledgerApplicationSetupControlAccountTypeCode | CONTROL_ACCOUNT_TYPE_CODE | — | ✅ |
| 4 | SubledgerApplicationSetupDrilldownProcedureName | DRILLDOWN_PROCEDURE_NAME | — | ✅ |
| 5 | SubledgerApplicationSetupJeSourceName | JE_SOURCE_NAME | — | ✅ |
| 6 | SubledgerApplicationSetupObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |

### [[xla_subledgers_vl|XLA_SUBLEDGERS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SubledgerApplicationApplicationId | APPLICATION_ID | — | ✅ |
| 2 | SubledgerApplicationApplicationName | APPLICATION_NAME | — | ✅ |
| 3 | SubledgerApplicationApplicationShortName | APPLICATION_SHORT_NAME | — | ✅ |
| 4 | SubledgerApplicationApplicationTypeCode | APPLICATION_TYPE_CODE | — | ✅ |
| 5 | SubledgerApplicationControlAccountTypeCode | CONTROL_ACCOUNT_TYPE_CODE | — | ✅ |
| 6 | SubledgerApplicationJeSourceName | JE_SOURCE_NAME | — | ✅ |
| 7 | SubledgerApplicationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
