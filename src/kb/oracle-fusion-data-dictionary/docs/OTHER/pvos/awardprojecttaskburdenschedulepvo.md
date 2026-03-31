---
id: DOC-OTHER-PVO-AwardProjectTaskBurdenSchedulePVO
doc_type: system-doc
title: "AwardProjectTaskBurdenSchedulePVO — PVO Cross-Module"
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
  - AwardProjectTaskBurdenSchedulePVO
  - awardprojecttaskburdenschedulepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AwardProjectTaskBurdenSchedulePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Award Project Task Burden Schedule. Acessa as tabelas: GMS_AWD_PRJ_TSK_BRD_SCHEDULES, PJF_IND_RATE_SCH_VL.

**Caminho:** `FscmTopModelAM.GmsAwardAM.AwardProjectTaskBurdenSchedulePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 34 | 2 | 1 | 5 | 15% |

---

## 🔗 Tabelas Relacionadas

- [[gms_awd_prj_tsk_brd_schedules|GMS_AWD_PRJ_TSK_BRD_SCHEDULES]] — 13 atributos (1 PKs, 3 BICC)
- [[pjf_ind_rate_sch_vl|PJF_IND_RATE_SCH_VL]] — 21 atributos (2 BICC)

---

## ⚙️ Atributos

### [[gms_awd_prj_tsk_brd_schedules|GMS_AWD_PRJ_TSK_BRD_SCHEDULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardTaskBurdenSchedulePEOAwardId | AWARD_ID | — | — |
| 2 | AwardTaskBurdenSchedulePEOAwdProjectLnkId | AWD_PROJECT_LNK_ID | — | — |
| 3 | AwardTaskBurdenSchedulePEOCostIndSchFixedDate | COST_IND_SCH_FIXED_DATE | — | ✅ |
| 4 | AwardTaskBurdenSchedulePEOCreatedBy | CREATED_BY | — | — |
| 5 | AwardTaskBurdenSchedulePEOCreationDate | CREATION_DATE | — | — |
| 6 | AwardTaskBurdenSchedulePEOIdcScheduleId | IDC_SCHEDULE_ID | — | — |
| 7 | AwardTaskBurdenSchedulePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | AwardTaskBurdenSchedulePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | AwardTaskBurdenSchedulePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | AwardTaskBurdenSchedulePEOProjectId | PROJECT_ID | — | — |
| 11 | AwardTaskBurdenSchedulePEOTaskId | TASK_ID | — | — |
| 12 | Id | ID | 🔑 | ✅ |
| 13 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |

### [[pjf_ind_rate_sch_vl|PJF_IND_RATE_SCH_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjfIndRateSchVlCostOvrSchFlag | COST_OVR_SCH_FLAG | — | — |
| 2 | PjfIndRateSchVlCreatedBy | CREATED_BY | — | — |
| 3 | PjfIndRateSchVlCreationDate | CREATION_DATE | — | — |
| 4 | PjfIndRateSchVlDescription | DESCRIPTION | — | — |
| 5 | PjfIndRateSchVlEndDateActive | END_DATE_ACTIVE | — | — |
| 6 | PjfIndRateSchVlIndRateSchId | IND_RATE_SCH_ID | — | — |
| 7 | PjfIndRateSchVlIndRateScheduleType | IND_RATE_SCHEDULE_TYPE | — | — |
| 8 | PjfIndRateSchVlIndSchName | IND_SCH_NAME | — | ✅ |
| 9 | PjfIndRateSchVlIndStructureName | IND_STRUCTURE_NAME | — | — |
| 10 | PjfIndRateSchVlLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | PjfIndRateSchVlLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 12 | PjfIndRateSchVlLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | PjfIndRateSchVlObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | PjfIndRateSchVlProjectId | PROJECT_ID | — | — |
| 15 | PjfIndRateSchVlRecostTxnFlag | RECOST_TXN_FLAG | — | — |
| 16 | PjfIndRateSchVlStartDateActive | START_DATE_ACTIVE | — | — |
| 17 | PjfIndRateSchVlStartOrganizationId | START_ORGANIZATION_ID | — | — |
| 18 | PjfIndRateSchVlTaskId | TASK_ID | — | — |
| 19 | PjfIndRateSchVlTreeCode | TREE_CODE | — | — |
| 20 | PjfIndRateSchVlTreeStructureCode | TREE_STRUCTURE_CODE | — | — |
| 21 | PjfIndRateSchVlTreeVersionId | TREE_VERSION_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
