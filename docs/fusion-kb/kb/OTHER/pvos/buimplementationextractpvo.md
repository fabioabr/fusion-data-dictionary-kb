---
id: DOC-OTHER-PVO-BUImplementationExtractPVO
doc_type: system-doc
title: "BUImplementationExtractPVO — PVO Cross-Module"
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
  - BUImplementationExtractPVO
  - buimplementationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BUImplementationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de BUImplementation Extract. Acessa as tabelas: PJF_BU_IMPL_ALL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.BUImplementationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 29 | 1 | 1 | 29 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_bu_impl_all|PJF_BU_IMPL_ALL]] — 29 atributos (1 PKs, 29 BICC)

---

## ⚙️ Atributos

### [[pjf_bu_impl_all|PJF_BU_IMPL_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjfBuImplAllBookTypeCode | BOOK_TYPE_CODE | — | ✅ |
| 2 | PjfBuImplAllCcDefaultRateDateCode | CC_DEFAULT_RATE_DATE_CODE | — | ✅ |
| 3 | PjfBuImplAllCcDefaultRateType | CC_DEFAULT_RATE_TYPE | — | ✅ |
| 4 | PjfBuImplAllCcProcessIoCode | CC_PROCESS_IO_CODE | — | ✅ |
| 5 | PjfBuImplAllCcProcessIuCode | CC_PROCESS_IU_CODE | — | ✅ |
| 6 | PjfBuImplAllCreatedBy | CREATED_BY | — | ✅ |
| 7 | PjfBuImplAllCreationDate | CREATION_DATE | — | ✅ |
| 8 | PjfBuImplAllDefaultRateDateCode | DEFAULT_RATE_DATE_CODE | — | ✅ |
| 9 | PjfBuImplAllDefaultRateType | DEFAULT_RATE_TYPE | — | ✅ |
| 10 | PjfBuImplAllExpCycleStartDayCode | EXP_CYCLE_START_DAY_CODE | — | ✅ |
| 11 | PjfBuImplAllExpStartOrgId | EXP_START_ORG_ID | — | ✅ |
| 12 | PjfBuImplAllExpTreeCode | EXP_TREE_CODE | — | ✅ |
| 13 | PjfBuImplAllExpTreeStructureCode | EXP_TREE_STRUCTURE_CODE | — | ✅ |
| 14 | PjfBuImplAllExpTreeVersionId | EXP_TREE_VERSION_ID | — | ✅ |
| 15 | PjfBuImplAllLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | PjfBuImplAllLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 17 | PjfBuImplAllLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 18 | PjfBuImplAllObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 19 | PjfBuImplAllOrgId | ORG_ID | 🔑 | ✅ |
| 20 | PjfBuImplAllOvertimeCalcEnabledFlag | OVERTIME_CALC_ENABLED_FLAG | — | ✅ |
| 21 | PjfBuImplAllPaPeriodType | PA_PERIOD_TYPE | — | ✅ |
| 22 | PjfBuImplAllPeriodSetName | PERIOD_SET_NAME | — | ✅ |
| 23 | PjfBuImplAllProjStartOrgId | PROJ_START_ORG_ID | — | ✅ |
| 24 | PjfBuImplAllProjTreeCode | PROJ_TREE_CODE | — | ✅ |
| 25 | PjfBuImplAllProjTreeStructureCode | PROJ_TREE_STRUCTURE_CODE | — | ✅ |
| 26 | PjfBuImplAllProjTreeVersionId | PROJ_TREE_VERSION_ID | — | ✅ |
| 27 | PjfBuImplAllRetProcessFlag | RET_PROCESS_FLAG | — | ✅ |
| 28 | PjfBuImplAllSamePaGlPeriod | SAME_PA_GL_PERIOD | — | ✅ |
| 29 | PjfBuImplAllSeparationOfDutiesFlag | SEPARATION_OF_DUTIES_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
