---
id: DOC-OTHER-PVO-BuImplementation
doc_type: system-doc
title: "BuImplementation — PVO Cross-Module"
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
  - BuImplementation
  - buimplementation
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BuImplementation

## 📌 Visão Geral

View Object para extração BICC de dados de Bu Implementation. Acessa as tabelas: PJF_BU_IMPL_ALL_V.

**Caminho:** `FscmTopModelAM.PjfSetupSystemAM.BuImplementation`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 34 | 1 | 1 | 5 | 15% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_bu_impl_all_v|PJF_BU_IMPL_ALL_V]] — 34 atributos (1 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[pjf_bu_impl_all_v|PJF_BU_IMPL_ALL_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BookTypeCode | BOOK_TYPE_CODE | — | — |
| 2 | BuName | BU_NAME | — | — |
| 3 | BusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 4 | CcDefaultRateDateCode | CC_DEFAULT_RATE_DATE_CODE | — | — |
| 5 | CcDefaultRateType | CC_DEFAULT_RATE_TYPE | — | — |
| 6 | CcProcessIoCode | CC_PROCESS_IO_CODE | — | — |
| 7 | CcProcessIuCode | CC_PROCESS_IU_CODE | — | ✅ |
| 8 | DateFrom | DATE_FROM | — | — |
| 9 | DateTo | DATE_TO | — | — |
| 10 | DefaultRateDateCode | DEFAULT_RATE_DATE_CODE | — | — |
| 11 | DefaultRateType | DEFAULT_RATE_TYPE | — | — |
| 12 | DefaultSetId | DEFAULT_SET_ID | — | — |
| 13 | ExpCycleStartDayCode | EXP_CYCLE_START_DAY_CODE | — | — |
| 14 | ExpStartOrgId | EXP_START_ORG_ID | — | — |
| 15 | ExpTreeCode | EXP_TREE_CODE | — | — |
| 16 | ExpTreeStructureCode | EXP_TREE_STRUCTURE_CODE | — | — |
| 17 | ExpTreeVersionId | EXP_TREE_VERSION_ID | — | — |
| 18 | LegalEntityId | LEGAL_ENTITY_ID | — | — |
| 19 | LocationId | LOCATION_ID | — | — |
| 20 | ManagerId | MANAGER_ID | — | — |
| 21 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 22 | OrgId | ORG_ID | 🔑 | ✅ |
| 23 | OvertimeCalcEnabledFlag | OVERTIME_CALC_ENABLED_FLAG | — | — |
| 24 | PaPeriodType | PA_PERIOD_TYPE | — | ✅ |
| 25 | PeriodSetName | PERIOD_SET_NAME | — | ✅ |
| 26 | PrimaryLedgerId | PRIMARY_LEDGER_ID | — | — |
| 27 | ProjStartOrgId | PROJ_START_ORG_ID | — | — |
| 28 | ProjTreeCode | PROJ_TREE_CODE | — | — |
| 29 | ProjTreeStructureCode | PROJ_TREE_STRUCTURE_CODE | — | — |
| 30 | ProjTreeVersionId | PROJ_TREE_VERSION_ID | — | — |
| 31 | RetProcessFlag | RET_PROCESS_FLAG | — | — |
| 32 | SamePaGlPeriod | SAME_PA_GL_PERIOD | — | — |
| 33 | SeparationOfDutiesFlag | SEPARATION_OF_DUTIES_FLAG | — | — |
| 34 | ShortCode | SHORT_CODE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
