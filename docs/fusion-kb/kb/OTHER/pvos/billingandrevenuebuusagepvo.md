---
id: DOC-OTHER-PVO-BillingAndRevenueBUUsagePVO
doc_type: system-doc
title: "BillingAndRevenueBUUsagePVO — PVO Cross-Module"
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
  - BillingAndRevenueBUUsagePVO
  - billingandrevenuebuusagepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BillingAndRevenueBUUsagePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Billing And Revenue BUUsage. Acessa as tabelas: FUN_ALL_BUSINESS_UNITS_V, FUN_BUSINESS_FUNCTIONS_B, FUN_BUSINESS_FUNCTIONS_TL (+1).

**Caminho:** `FscmTopModelAM.FinFunBusinessUnitsAM.BillingAndRevenueBUUsagePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 39 | 4 | 1 | 32 | 82% |

---

## 🔗 Tabelas Relacionadas

- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 16 atributos (15 BICC)
- [[fun_business_functions_b|FUN_BUSINESS_FUNCTIONS_B]] — 10 atributos (10 BICC)
- [[fun_business_functions_tl|FUN_BUSINESS_FUNCTIONS_TL]] — 5 atributos
- [[fun_bu_usages_v|FUN_BU_USAGES_V]] — 8 atributos (1 PKs, 7 BICC)

---

## ⚙️ Atributos

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitBusinessUnitId | BU_ID | — | ✅ |
| 2 | BusinessUnitDateFrom | DATE_FROM | — | ✅ |
| 3 | BusinessUnitDateTo | DATE_TO | — | ✅ |
| 4 | BusinessUnitDefaultCurrencyCode | DEFAULT_CURRENCY_CODE | — | ✅ |
| 5 | BusinessUnitDefaultSetId | DEFAULT_SET_ID | — | ✅ |
| 6 | BusinessUnitEnabledForHrFlag | ENABLED_FOR_HR_FLAG | — | ✅ |
| 7 | BusinessUnitEnterpriseId | BUSINESS_GROUP_ID | — | ✅ |
| 8 | BusinessUnitFinancialsBusinessUnitId | FIN_BUSINESS_UNIT_ID | — | ✅ |
| 9 | BusinessUnitLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 10 | BusinessUnitLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 11 | BusinessUnitLocationId | LOCATION_ID | — | ✅ |
| 12 | BusinessUnitManagerId | MANAGER_ID | — | ✅ |
| 13 | BusinessUnitName | BU_NAME | — | ✅ |
| 14 | BusinessUnitPrimaryLedgerId | PRIMARY_LEDGER_ID | — | ✅ |
| 15 | BusinessUnitShortCode | SHORT_CODE | — | ✅ |
| 16 | BusinessUnitStatus | STATUS | — | ✅ |

### [[fun_business_functions_b|FUN_BUSINESS_FUNCTIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessFunctionBusinessFunctionCode | BUSINESS_FUNCTION_CODE | — | ✅ |
| 2 | BusinessFunctionBusinessFunctionId | BUSINESS_FUNCTION_ID | — | ✅ |
| 3 | BusinessFunctionCreatedBy | CREATED_BY | — | ✅ |
| 4 | BusinessFunctionCreationDate | CREATION_DATE | — | ✅ |
| 5 | BusinessFunctionGenerateFinTxnFlag | GENERATE_FIN_TXN_FLAG | — | ✅ |
| 6 | BusinessFunctionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | BusinessFunctionLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | BusinessFunctionLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | BusinessFunctionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | BusinessFunctionSetupApi | SETUP_API | — | ✅ |

### [[fun_business_functions_tl|FUN_BUSINESS_FUNCTIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessFunctionTranslationBusinessFunctionId | BUSINESS_FUNCTION_ID | — | — |
| 2 | BusinessFunctionTranslationBusinessFunctionName | BUSINESS_FUNCTION_NAME | — | — |
| 3 | BusinessFunctionTranslationDescription | DESCRIPTION | — | — |
| 4 | BusinessFunctionTranslationLanguage | LANGUAGE | — | — |
| 5 | BusinessFunctionTranslationSourceLang | SOURCE_LANG | — | — |

### [[fun_bu_usages_v|FUN_BU_USAGES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitId | BUSINESS_UNIT_ID | 🔑 | ✅ |
| 2 | BusinessUnitUsageConfigurationStatus | CONFIGURATION_STATUS | — | ✅ |
| 3 | BusinessUnitUsageModuleKey | MODULE_KEY | — | ✅ |
| 4 | BusinessUnitUsageModuleName | MODULE_NAME | — | ✅ |
| 5 | BusinessUnitUsageName | BU_NAME | — | ✅ |
| 6 | BusinessUnitUsageShortCode | SHORT_CODE | — | ✅ |
| 7 | BusinessUnitUsageStatus | STATUS | — | ✅ |
| 8 | ModuleId | MODULE_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
