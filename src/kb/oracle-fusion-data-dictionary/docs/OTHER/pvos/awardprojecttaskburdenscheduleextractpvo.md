---
id: DOC-OTHER-PVO-AwardProjectTaskBurdenScheduleExtractPVO
doc_type: system-doc
title: "AwardProjectTaskBurdenScheduleExtractPVO — PVO Cross-Module"
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
  - AwardProjectTaskBurdenScheduleExtractPVO
  - awardprojecttaskburdenscheduleextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AwardProjectTaskBurdenScheduleExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Award Project Task Burden Schedule Extract. Acessa as tabelas: GMS_AWD_PRJ_TSK_BRD_SCHEDULES.

**Caminho:** `FscmTopModelAM.PrjExtractAM.GmsBiccExtractAM.AwardProjectTaskBurdenScheduleExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 1 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gms_awd_prj_tsk_brd_schedules|GMS_AWD_PRJ_TSK_BRD_SCHEDULES]] — 13 atributos (1 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[gms_awd_prj_tsk_brd_schedules|GMS_AWD_PRJ_TSK_BRD_SCHEDULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwdTaskBrdnSchedulePEOAwardId | AWARD_ID | — | ✅ |
| 2 | AwdTaskBrdnSchedulePEOAwdProjectLnkId | AWD_PROJECT_LNK_ID | — | ✅ |
| 3 | AwdTaskBrdnSchedulePEOCostIndSchFixedDate | COST_IND_SCH_FIXED_DATE | — | ✅ |
| 4 | AwdTaskBrdnSchedulePEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | AwdTaskBrdnSchedulePEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | AwdTaskBrdnSchedulePEOId | ID | 🔑 | ✅ |
| 7 | AwdTaskBrdnSchedulePEOIdcScheduleId | IDC_SCHEDULE_ID | — | ✅ |
| 8 | AwdTaskBrdnSchedulePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | AwdTaskBrdnSchedulePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | AwdTaskBrdnSchedulePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | AwdTaskBrdnSchedulePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | AwdTaskBrdnSchedulePEOProjectId | PROJECT_ID | — | ✅ |
| 13 | AwdTaskBrdnSchedulePEOTaskId | TASK_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
