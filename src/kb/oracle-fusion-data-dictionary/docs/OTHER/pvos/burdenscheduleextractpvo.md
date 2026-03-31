---
id: DOC-OTHER-PVO-BurdenScheduleExtractPVO
doc_type: system-doc
title: "BurdenScheduleExtractPVO — PVO Cross-Module"
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
  - BurdenScheduleExtractPVO
  - burdenscheduleextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BurdenScheduleExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Burden Schedule Extract. Acessa as tabelas: PJF_IND_RATE_SCH_B, PJF_IND_RATE_SCH_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.BurdenScheduleExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 33 | 2 | 1 | 33 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_ind_rate_sch_b|PJF_IND_RATE_SCH_B]] — 22 atributos (1 PKs, 22 BICC)
- [[pjf_ind_rate_sch_tl|PJF_IND_RATE_SCH_TL]] — 11 atributos (11 BICC)

---

## ⚙️ Atributos

### [[pjf_ind_rate_sch_b|PJF_IND_RATE_SCH_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BurdenScheduleBasePEOAwardId | AWARD_ID | — | ✅ |
| 2 | BurdenScheduleBasePEOAwardProjectId | AWARD_PROJECT_ID | — | ✅ |
| 3 | BurdenScheduleBasePEOAwardTaskId | AWARD_TASK_ID | — | ✅ |
| 4 | BurdenScheduleBasePEOCostOvrSchFlag | COST_OVR_SCH_FLAG | — | ✅ |
| 5 | BurdenScheduleBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | BurdenScheduleBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | BurdenScheduleBasePEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 8 | BurdenScheduleBasePEOIndRateSchId | IND_RATE_SCH_ID | 🔑 | ✅ |
| 9 | BurdenScheduleBasePEOIndRateScheduleType | IND_RATE_SCHEDULE_TYPE | — | ✅ |
| 10 | BurdenScheduleBasePEOIndStructureName | IND_STRUCTURE_NAME | — | ✅ |
| 11 | BurdenScheduleBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | BurdenScheduleBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | BurdenScheduleBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | BurdenScheduleBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 15 | BurdenScheduleBasePEOProjectId | PROJECT_ID | — | ✅ |
| 16 | BurdenScheduleBasePEORecostTxnFlag | RECOST_TXN_FLAG | — | ✅ |
| 17 | BurdenScheduleBasePEOStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 18 | BurdenScheduleBasePEOStartOrganizationId | START_ORGANIZATION_ID | — | ✅ |
| 19 | BurdenScheduleBasePEOTaskId | TASK_ID | — | ✅ |
| 20 | BurdenScheduleBasePEOTreeCode | TREE_CODE | — | ✅ |
| 21 | BurdenScheduleBasePEOTreeStructureCode | TREE_STRUCTURE_CODE | — | ✅ |
| 22 | BurdenScheduleBasePEOTreeVersionId | TREE_VERSION_ID | — | ✅ |

### [[pjf_ind_rate_sch_tl|PJF_IND_RATE_SCH_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BurdenScheduleTLCreatedBy | CREATED_BY | — | ✅ |
| 2 | BurdenScheduleTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | BurdenScheduleTLPEODescription | DESCRIPTION | — | ✅ |
| 4 | BurdenScheduleTLPEOIndRateSchId | IND_RATE_SCH_ID | — | ✅ |
| 5 | BurdenScheduleTLPEOIndSchName | IND_SCH_NAME | — | ✅ |
| 6 | BurdenScheduleTLPEOLanguage | LANGUAGE | — | ✅ |
| 7 | BurdenScheduleTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | BurdenScheduleTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | BurdenScheduleTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | BurdenScheduleTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | BurdenScheduleTLPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
