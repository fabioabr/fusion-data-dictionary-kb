---
id: DOC-OTHER-PVO-VcsCollaborationPlansExtractPVO
doc_type: system-doc
title: "VcsCollaborationPlansExtractPVO — PVO Cross-Module"
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
  - VcsCollaborationPlansExtractPVO
  - vcscollaborationplansextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# VcsCollaborationPlansExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Vcs Collaboration Plans Extract. Acessa as tabelas: VCS_COLLAB_SOURCE, VCS_PLAN_SCENARIOS_B, VCS_PLAN_SCENARIOS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.VcsBiccExtractAM.VcsCollaborationPlansExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 39 | 3 | 4 | 39 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[vcs_collab_source|VCS_COLLAB_SOURCE]] — 16 atributos (1 PKs, 16 BICC)
- [[vcs_plan_scenarios_b|VCS_PLAN_SCENARIOS_B]] — 14 atributos (1 PKs, 14 BICC)
- [[vcs_plan_scenarios_tl|VCS_PLAN_SCENARIOS_TL]] — 9 atributos (2 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[vcs_collab_source|VCS_COLLAB_SOURCE]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | VcsCollaborationPlansPEOCollabName | COLLAB_NAME | — | ✅ |
| 2 | VcsCollaborationPlansPEOCollaborationSourceId | COLLAB_SOURCE_ID | 🔑 | ✅ |
| 3 | VcsCollaborationPlansPEOCollaborationTypeCode | COLLAB_TYPE_CODE | — | ✅ |
| 4 | VcsCollaborationPlansPEOCollaborationVersion | COLLAB_VERSION | — | ✅ |
| 5 | VcsCollaborationPlansPEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | VcsCollaborationPlansPEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | VcsCollaborationPlansPEODescription | DESCRIPTION | — | ✅ |
| 8 | VcsCollaborationPlansPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | VcsCollaborationPlansPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | VcsCollaborationPlansPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | VcsCollaborationPlansPEOOriginSourceCode | ORIGIN_SOURCE_CODE | — | ✅ |
| 12 | VcsCollaborationPlansPEOParentCollaborationSourceId | PARENT_COLLAB_SOURCE_ID | — | ✅ |
| 13 | VcsCollaborationPlansPEOPublishCycleEndDate | PUBLISH_CYCLE_END_DATE | — | ✅ |
| 14 | VcsCollaborationPlansPEOPublishCycleStartDate | PUBLISH_CYCLE_START_DATE | — | ✅ |
| 15 | VcsCollaborationPlansPEOScenarioId | SCENARIO_ID | — | ✅ |
| 16 | VcsCollaborationPlansPEOSourceSystemCode | SOURCE_SYSTEM_CODE | — | ✅ |

### [[vcs_plan_scenarios_b|VCS_PLAN_SCENARIOS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | VcsPlanScenariosBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | VcsPlanScenariosBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | VcsPlanScenariosBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | VcsPlanScenariosBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 5 | VcsPlanScenariosBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 6 | VcsPlanScenariosBasePEOPlanName | PLAN_NAME | — | ✅ |
| 7 | VcsPlanScenariosBasePEOPublishCycleDayCode | PUBLISH_CYCLE_DAY_CODE | — | ✅ |
| 8 | VcsPlanScenariosBasePEOPublishCycleFrequency | PUBLISH_CYCLE_FREQUENCY | — | ✅ |
| 9 | VcsPlanScenariosBasePEOPublishCycleTypeCode | PUBLISH_CYCLE_TYPE_CODE | — | ✅ |
| 10 | VcsPlanScenariosBasePEOPublishMonthlyStartDate | PUBLISH_MONTHLY_START_DATE | — | ✅ |
| 11 | VcsPlanScenariosBasePEOScenarioId | SCENARIO_ID | 🔑 | ✅ |
| 12 | VcsPlanScenariosBasePEOStartDayOrdinal | PUBLISH_START_ORDINAL_CODE | — | ✅ |
| 13 | VcsPlanScenariosBasePEOStartType | PUBLISH_START_TYPE_CODE | — | ✅ |
| 14 | VcsPlanScenariosBasePEOStatusCode | STATUS_CODE | — | ✅ |

### [[vcs_plan_scenarios_tl|VCS_PLAN_SCENARIOS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | VcsPlanScenariosTranslatePEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | VcsPlanScenariosTranslatePEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | VcsPlanScenariosTranslatePEOLanguage | LANGUAGE | 🔑 | ✅ |
| 4 | VcsPlanScenariosTranslatePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | VcsPlanScenariosTranslatePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 6 | VcsPlanScenariosTranslatePEOName | NAME | — | ✅ |
| 7 | VcsPlanScenariosTranslatePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | VcsPlanScenariosTranslatePEOScenarioId | SCENARIO_ID | 🔑 | ✅ |
| 9 | VcsPlanScenariosTranslatePEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
