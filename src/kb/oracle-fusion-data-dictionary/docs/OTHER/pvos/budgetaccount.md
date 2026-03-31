---
id: DOC-OTHER-PVO-BudgetAccount
doc_type: system-doc
title: "BudgetAccount — PVO Cross-Module"
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
  - BudgetAccount
  - budgetaccount
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BudgetAccount

## 📌 Visão Geral

View Object para extração BICC de dados de Budget Account. Acessa as tabelas: FND_KF_STR_INSTANCES_VL, XCC_BUDGET_ACCOUNTS.

**Caminho:** `FscmTopModelAM.FinCcBudgetAccountPublicModelAM.BudgetAccount`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 58 | 2 | 1 | 8 | 14% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_kf_str_instances_vl|FND_KF_STR_INSTANCES_VL]] — 16 atributos (4 BICC)
- [[xcc_budget_accounts|XCC_BUDGET_ACCOUNTS]] — 42 atributos (1 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[fnd_kf_str_instances_vl|FND_KF_STR_INSTANCES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FlexStructInstancApplicationId | APPLICATION_ID | — | — |
| 2 | FlexStructInstancCreatedBy | CREATED_BY | — | — |
| 3 | FlexStructInstancCreationDate | CREATION_DATE | — | ✅ |
| 4 | FlexStructInstancDescription | DESCRIPTION | — | ✅ |
| 5 | FlexStructInstancDynamicCombinationCreationAllowed | DYNAMIC_COMBO_CREATION_FLAG | — | — |
| 6 | FlexStructInstancEnabledFlag1 | ENABLED_FLAG | — | — |
| 7 | FlexStructInstancKeyFlexfieldCode | KEY_FLEXFIELD_CODE | — | — |
| 8 | FlexStructInstancLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | FlexStructInstancLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | FlexStructInstancLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 11 | FlexStructInstancName | NAME | — | ✅ |
| 12 | FlexStructInstancStructureId | STRUCTURE_ID | — | — |
| 13 | FlexStructInstancStructureInstanceCode | STRUCTURE_INSTANCE_CODE | — | — |
| 14 | FlexStructInstancStructureInstanceId | STRUCTURE_INSTANCE_ID | — | — |
| 15 | FlexStructInstancStructureInstanceIdentifier | STRUCTURE_INSTANCE_IDENTIFIER | — | — |
| 16 | FlexStructInstancStructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | — |

### [[xcc_budget_accounts|XCC_BUDGET_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BudgetAccountCreatedBy | CREATED_BY | — | — |
| 2 | BudgetAccountCreationDate | CREATION_DATE | — | — |
| 3 | BudgetAccountLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | BudgetAccountLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 5 | BudgetChartOfAccountsId | BUDGET_CHART_OF_ACCOUNTS_ID | — | — |
| 6 | BudgetCodeCombinationId | BUDGET_CODE_COMBINATION_ID | 🔑 | ✅ |
| 7 | EnabledFlag | ENABLED_FLAG | — | ✅ |
| 8 | EndDateActive | END_DATE_ACTIVE | — | — |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | SegmentValue1 | SEGMENT_VALUE1 | — | — |
| 12 | SegmentValue10 | SEGMENT_VALUE10 | — | — |
| 13 | SegmentValue11 | SEGMENT_VALUE11 | — | — |
| 14 | SegmentValue12 | SEGMENT_VALUE12 | — | — |
| 15 | SegmentValue13 | SEGMENT_VALUE13 | — | — |
| 16 | SegmentValue14 | SEGMENT_VALUE14 | — | — |
| 17 | SegmentValue15 | SEGMENT_VALUE15 | — | — |
| 18 | SegmentValue16 | SEGMENT_VALUE16 | — | — |
| 19 | SegmentValue17 | SEGMENT_VALUE17 | — | — |
| 20 | SegmentValue18 | SEGMENT_VALUE18 | — | — |
| 21 | SegmentValue19 | SEGMENT_VALUE19 | — | — |
| 22 | SegmentValue2 | SEGMENT_VALUE2 | — | — |
| 23 | SegmentValue20 | SEGMENT_VALUE20 | — | — |
| 24 | SegmentValue21 | SEGMENT_VALUE21 | — | — |
| 25 | SegmentValue22 | SEGMENT_VALUE22 | — | — |
| 26 | SegmentValue23 | SEGMENT_VALUE23 | — | — |
| 27 | SegmentValue24 | SEGMENT_VALUE24 | — | — |
| 28 | SegmentValue25 | SEGMENT_VALUE25 | — | — |
| 29 | SegmentValue26 | SEGMENT_VALUE26 | — | — |
| 30 | SegmentValue27 | SEGMENT_VALUE27 | — | — |
| 31 | SegmentValue28 | SEGMENT_VALUE28 | — | — |
| 32 | SegmentValue29 | SEGMENT_VALUE29 | — | — |
| 33 | SegmentValue3 | SEGMENT_VALUE3 | — | — |
| 34 | SegmentValue30 | SEGMENT_VALUE30 | — | — |
| 35 | SegmentValue4 | SEGMENT_VALUE4 | — | — |
| 36 | SegmentValue5 | SEGMENT_VALUE5 | — | — |
| 37 | SegmentValue6 | SEGMENT_VALUE6 | — | — |
| 38 | SegmentValue7 | SEGMENT_VALUE7 | — | — |
| 39 | SegmentValue8 | SEGMENT_VALUE8 | — | — |
| 40 | SegmentValue9 | SEGMENT_VALUE9 | — | — |
| 41 | StartDateActive | START_DATE_ACTIVE | — | — |
| 42 | SummaryFlag | SUMMARY_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
