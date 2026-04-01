---
id: DOC-GL-PVO-BalanceCategory
doc_type: system-doc
title: "BalanceCategory — PVO General Ledger"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - gl
  - data-dictionary
  - pvo
  - bicc
aliases:
  - BalanceCategory
  - balancecategory
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BalanceCategory

## 📌 Visão Geral

View Object para extração BICC de dados de Balance Category. Acessa as tabelas: PAY_BALANCE_CATEGORIES_F, PAY_BALANCE_CATEGORIES_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmPayBalanceAM.BalanceCategory`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 2 | 3 | 11 | 55% |

---

## 🔗 Tabelas Relacionadas

- [[pay_balance_categories_f|PAY_BALANCE_CATEGORIES_F]] — 16 atributos (2 PKs, 9 BICC)
- [[pay_balance_categories_tl|PAY_BALANCE_CATEGORIES_TL]] — 4 atributos (1 PKs, 2 BICC)

---

## ⚙️ Atributos

### [[pay_balance_categories_f|PAY_BALANCE_CATEGORIES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BalanceCategoryBaseDPEOBaseBalanceCategoryId | BASE_BALANCE_CATEGORY_ID | — | ✅ |
| 2 | BalanceCategoryBaseDPEOBaseCategoryName | BASE_CATEGORY_NAME | — | ✅ |
| 3 | BalanceCategoryBaseDPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | BalanceCategoryBaseDPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | BalanceCategoryBaseDPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | BalanceCategoryBaseDPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | BalanceCategoryBaseDPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | BalanceCategoryBaseDPEOLegislationCode | LEGISLATION_CODE | — | — |
| 9 | BalanceCategoryBaseDPEOLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | — |
| 10 | BalanceCategoryBaseDPEOModuleId | MODULE_ID | — | — |
| 11 | BalanceCategoryBaseDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | BalanceCategoryBaseDPEOPbcInformationCategory | PBC_INFORMATION_CATEGORY | — | — |
| 13 | BalanceCategoryBaseDPEOSaveRunBalanceEnabled | SAVE_RUN_BALANCE_ENABLED | — | — |
| 14 | BalanceCategoryId | BALANCE_CATEGORY_ID | 🔑 | ✅ |
| 15 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 16 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |

### [[pay_balance_categories_tl|PAY_BALANCE_CATEGORIES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BalanceCategoryBaseDPEOBalanceCategoryId | BALANCE_CATEGORY_ID | — | — |
| 2 | BalanceCategoryBaseDPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 3 | BalanceCategoryBaseDPEOSourceLang | SOURCE_LANG | — | ✅ |
| 4 | BalanceCategoryBaseDPEOUserCategoryName | USER_CATEGORY_NAME | — | — |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
