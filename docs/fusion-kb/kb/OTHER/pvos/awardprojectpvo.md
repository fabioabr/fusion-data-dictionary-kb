---
id: DOC-OTHER-PVO-AwardProjectPVO
doc_type: system-doc
title: "AwardProjectPVO — PVO Cross-Module"
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
  - AwardProjectPVO
  - awardprojectpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AwardProjectPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Award Project. Acessa as tabelas: GMS_AWARD_PROJECTS, PJF_IND_RATE_SCH_VL, PJF_PROJECTS_ALL_VL.

**Caminho:** `FscmTopModelAM.GmsAwardAM.AwardProjectPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 17 | 3 | 1 | 17 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gms_award_projects|GMS_AWARD_PROJECTS]] — 12 atributos (1 PKs, 12 BICC)
- [[pjf_ind_rate_sch_vl|PJF_IND_RATE_SCH_VL]] — 2 atributos (2 BICC)
- [[pjf_projects_all_vl|PJF_PROJECTS_ALL_VL]] — 3 atributos (3 BICC)

---

## ⚙️ Atributos

### [[gms_award_projects|GMS_AWARD_PROJECTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardProjectPEOAwardFundingSourceId | AWARD_FUNDING_SOURCE_ID | — | ✅ |
| 2 | AwardProjectPEOAwardId | AWARD_ID | — | ✅ |
| 3 | AwardProjectPEOCostIndSchFixedDate | COST_IND_SCH_FIXED_DATE | — | ✅ |
| 4 | AwardProjectPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | AwardProjectPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | AwardProjectPEOIdcScheduleId | IDC_SCHEDULE_ID | — | ✅ |
| 7 | AwardProjectPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | AwardProjectPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | AwardProjectPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | AwardProjectPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | AwardProjectPEOProjectId | PROJECT_ID | — | ✅ |
| 12 | Id | ID | 🔑 | ✅ |

### [[pjf_ind_rate_sch_vl|PJF_IND_RATE_SCH_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjfIndRateSchVlIndRateSchId | IND_RATE_SCH_ID | — | ✅ |
| 2 | PjfIndRateSchVlIndSchName | IND_SCH_NAME | — | ✅ |

### [[pjf_projects_all_vl|PJF_PROJECTS_ALL_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectPEOName | NAME | — | ✅ |
| 2 | ProjectPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 3 | ProjectPEOProjectId | PROJECT_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
