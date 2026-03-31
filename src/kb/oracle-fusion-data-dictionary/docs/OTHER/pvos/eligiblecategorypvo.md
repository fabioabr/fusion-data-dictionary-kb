---
id: DOC-OTHER-PVO-EligibleCategoryPVO
doc_type: system-doc
title: "EligibleCategoryPVO — PVO Cross-Module"
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
  - EligibleCategoryPVO
  - eligiblecategorypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EligibleCategoryPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Eligible Category. Acessa as tabelas: CN_ELIGIBLE_CATS_ALL_B, CN_ELIGIBLE_CATS_ALL_TL, FUN_ALL_BUSINESS_UNITS_V.

**Caminho:** `FscmTopModelAM.EligibleCategoryAM.EligibleCategoryPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 31 | 3 | 1 | 8 | 26% |

---

## 🔗 Tabelas Relacionadas

- [[cn_eligible_cats_all_b|CN_ELIGIBLE_CATS_ALL_B]] — 11 atributos (1 PKs, 2 BICC)
- [[cn_eligible_cats_all_tl|CN_ELIGIBLE_CATS_ALL_TL]] — 5 atributos (3 BICC)
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 15 atributos (3 BICC)

---

## ⚙️ Atributos

### [[cn_eligible_cats_all_b|CN_ELIGIBLE_CATS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 2 | CreatedBy | CREATED_BY | — | — |
| 3 | CreationDate | CREATION_DATE | — | — |
| 4 | EligibleCatId | ELIGIBLE_CAT_ID | 🔑 | ✅ |
| 5 | ExpenseAccountId | EXPENSE_ACCOUNT_ID | — | — |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | LiabilityAccountId | LIABILITY_ACCOUNT_ID | — | — |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | OrgId | ORG_ID | — | — |

### [[cn_eligible_cats_all_tl|CN_ELIGIBLE_CATS_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Description | DESCRIPTION | — | ✅ |
| 2 | EligibleCatId1 | ELIGIBLE_CAT_ID | — | — |
| 3 | Language | LANGUAGE | — | ✅ |
| 4 | Name | NAME | — | ✅ |
| 5 | SourceLang | SOURCE_LANG | — | — |

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitId | BU_ID | — | — |
| 2 | BusinessUnitPEOName | BU_NAME | — | ✅ |
| 3 | DateFrom | DATE_FROM | — | — |
| 4 | DateTo | DATE_TO | — | — |
| 5 | DefaultCurrencyCode | DEFAULT_CURRENCY_CODE | — | — |
| 6 | DefaultSetId | DEFAULT_SET_ID | — | — |
| 7 | EnabledForHrFlag | ENABLED_FOR_HR_FLAG | — | — |
| 8 | EnterpriseId | BUSINESS_GROUP_ID | — | — |
| 9 | FinancialsBusinessUnitId | FIN_BUSINESS_UNIT_ID | — | — |
| 10 | LegalEntityId | LEGAL_ENTITY_ID | — | — |
| 11 | LocationId | LOCATION_ID | — | — |
| 12 | ManagerId | MANAGER_ID | — | — |
| 13 | PrimaryLedgerId | PRIMARY_LEDGER_ID | — | — |
| 14 | ShortCode | SHORT_CODE | — | ✅ |
| 15 | Status | STATUS | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
