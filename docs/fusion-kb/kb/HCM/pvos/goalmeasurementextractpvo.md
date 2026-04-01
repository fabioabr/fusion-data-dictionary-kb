---
id: DOC-HCM-PVO-GoalMeasurementExtractPVO
doc_type: system-doc
title: "GoalMeasurementExtractPVO — PVO Human Capital Management"
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
  - GoalMeasurementExtractPVO
  - goalmeasurementextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GoalMeasurementExtractPVO

## 📌 Visão Geral

Extrai medições de metas com valores reais, esperados e pesos alcançados. Utilizado para análise quantitativa de atingimento de objetivos.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.GoalBiccExtractAM.GoalMeasurementExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 23 | 1 | 1 | 23 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hrg_goal_measurements|HRG_GOAL_MEASUREMENTS]] — 23 atributos (1 PKs, 23 BICC)

---

## ⚙️ Atributos

### [[hrg_goal_measurements|HRG_GOAL_MEASUREMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AchievedWeight | ACHIEVED_WEIGHT | — | ✅ |
| 2 | ActualValue | ACTUAL_VALUE | — | ✅ |
| 3 | BusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 4 | Comments | COMMENTS | — | ✅ |
| 5 | CreatedBy | CREATED_BY | — | ✅ |
| 6 | CreationDate | CREATION_DATE | — | ✅ |
| 7 | DisplaySequence | DISPLAY_SEQUENCE | — | ✅ |
| 8 | EndDate | END_DATE | — | ✅ |
| 9 | GoalId | GOAL_ID | — | ✅ |
| 10 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | MaxTarget | MAX_TARGET | — | ✅ |
| 14 | MeasureTypeCode | MEASURE_TYPE_CODE | — | ✅ |
| 15 | MeasurementId | MEASUREMENT_ID | 🔑 | ✅ |
| 16 | MeasurementName | MEASUREMENT_NAME | — | ✅ |
| 17 | MinTarget | MIN_TARGET | — | ✅ |
| 18 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 19 | StartDate | START_DATE | — | ✅ |
| 20 | TargetPercentage | TARGET_PERCENTAGE | — | ✅ |
| 21 | TargetType | TARGET_TYPE | — | ✅ |
| 22 | TargetValue | TARGET_VALUE | — | ✅ |
| 23 | UomCode | UOM_CODE | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
