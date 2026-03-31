---
id: DOC-HCM-PVO-HierarchyCfDnPVO
doc_type: system-doc
title: "HierarchyCfDnPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - HierarchyCfDnPVO
  - hierarchycfdnpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# HierarchyCfDnPVO

## 📌 Visão Geral

Disponibiliza hierarquia denormalizada de compensação (CWB) com cadeia de gestores. Utilizado para orçamento e aprovação de remuneração em cascata.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.CompensationAM.HierarchyCfDnPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 41 | 1 | 1 | 39 | 95% |

---

## 🔗 Tabelas Relacionadas

- [[cmp_cwb_hrchy_cf_dn|CMP_CWB_HRCHY_CF_DN]] — 41 atributos (1 PKs, 39 BICC)

---

## ⚙️ Atributos

### [[cmp_cwb_hrchy_cf_dn|CMP_CWB_HRCHY_CF_DN]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentId | ASSIGNMENT_ID | — | — |
| 2 | HierarchyCfDnPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | HierarchyCfDnPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | HierarchyCfDnPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | HierarchyCfDnPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | HierarchyCfDnPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | HierarchyCfDnPEOLevel10MgrPersonId | LEVEL10_MGR_PERSON_ID | — | ✅ |
| 8 | HierarchyCfDnPEOLevel10PersonEventId | LEVEL10_PERSON_EVENT_ID | — | ✅ |
| 9 | HierarchyCfDnPEOLevel11MgrPersonId | LEVEL11_MGR_PERSON_ID | — | ✅ |
| 10 | HierarchyCfDnPEOLevel11PersonEventId | LEVEL11_PERSON_EVENT_ID | — | ✅ |
| 11 | HierarchyCfDnPEOLevel12MgrPersonId | LEVEL12_MGR_PERSON_ID | — | ✅ |
| 12 | HierarchyCfDnPEOLevel12PersonEventId | LEVEL12_PERSON_EVENT_ID | — | ✅ |
| 13 | HierarchyCfDnPEOLevel13MgrPersonId | LEVEL13_MGR_PERSON_ID | — | ✅ |
| 14 | HierarchyCfDnPEOLevel13PersonEventId | LEVEL13_PERSON_EVENT_ID | — | ✅ |
| 15 | HierarchyCfDnPEOLevel14MgrPersonId | LEVEL14_MGR_PERSON_ID | — | ✅ |
| 16 | HierarchyCfDnPEOLevel14PersonEventId | LEVEL14_PERSON_EVENT_ID | — | ✅ |
| 17 | HierarchyCfDnPEOLevel15MgrPersonId | LEVEL15_MGR_PERSON_ID | — | ✅ |
| 18 | HierarchyCfDnPEOLevel15PersonEventId | LEVEL15_PERSON_EVENT_ID | — | ✅ |
| 19 | HierarchyCfDnPEOLevel1MgrPersonId | LEVEL1_MGR_PERSON_ID | — | ✅ |
| 20 | HierarchyCfDnPEOLevel1PersonEventId | LEVEL1_PERSON_EVENT_ID | — | ✅ |
| 21 | HierarchyCfDnPEOLevel2MgrPersonId | LEVEL2_MGR_PERSON_ID | — | ✅ |
| 22 | HierarchyCfDnPEOLevel2PersonEventId | LEVEL2_PERSON_EVENT_ID | — | ✅ |
| 23 | HierarchyCfDnPEOLevel3MgrPersonId | LEVEL3_MGR_PERSON_ID | — | ✅ |
| 24 | HierarchyCfDnPEOLevel3PersonEventId | LEVEL3_PERSON_EVENT_ID | — | ✅ |
| 25 | HierarchyCfDnPEOLevel4MgrPersonId | LEVEL4_MGR_PERSON_ID | — | ✅ |
| 26 | HierarchyCfDnPEOLevel4PersonEventId | LEVEL4_PERSON_EVENT_ID | — | ✅ |
| 27 | HierarchyCfDnPEOLevel5MgrPersonId | LEVEL5_MGR_PERSON_ID | — | ✅ |
| 28 | HierarchyCfDnPEOLevel5PersonEventId | LEVEL5_PERSON_EVENT_ID | — | ✅ |
| 29 | HierarchyCfDnPEOLevel6MgrPersonId | LEVEL6_MGR_PERSON_ID | — | ✅ |
| 30 | HierarchyCfDnPEOLevel6PersonEventId | LEVEL6_PERSON_EVENT_ID | — | ✅ |
| 31 | HierarchyCfDnPEOLevel7MgrPersonId | LEVEL7_MGR_PERSON_ID | — | ✅ |
| 32 | HierarchyCfDnPEOLevel7PersonEventId | LEVEL7_PERSON_EVENT_ID | — | ✅ |
| 33 | HierarchyCfDnPEOLevel8MgrPersonId | LEVEL8_MGR_PERSON_ID | — | ✅ |
| 34 | HierarchyCfDnPEOLevel8PersonEventId | LEVEL8_PERSON_EVENT_ID | — | ✅ |
| 35 | HierarchyCfDnPEOLevel9MgrPersonId | LEVEL9_MGR_PERSON_ID | — | ✅ |
| 36 | HierarchyCfDnPEOLevel9PersonEventId | LEVEL9_PERSON_EVENT_ID | — | ✅ |
| 37 | HierarchyCfDnPEOPersonId | PERSON_ID | — | — |
| 38 | HierarchyCfDnPEOTopMgrPersonId | TOP_MGR_PERSON_ID | — | ✅ |
| 39 | HierarchyCfDnPEOTopPeriodId | TOP_PERIOD_ID | — | ✅ |
| 40 | HierarchyCfDnPEOTopPlanId | TOP_PLAN_ID | — | ✅ |
| 41 | TopMgrPersonEventId | TOP_MGR_PERSON_EVENT_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
