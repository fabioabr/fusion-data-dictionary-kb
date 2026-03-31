---
id: DOC-OTHER-PVO-EgoChangeTypesCycleTimeThresholdPVO
doc_type: system-doc
title: "EgoChangeTypesCycleTimeThresholdPVO — PVO Cross-Module"
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
  - EgoChangeTypesCycleTimeThresholdPVO
  - egochangetypescycletimethresholdpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EgoChangeTypesCycleTimeThresholdPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Ego Change Types Cycle Time Threshold. Acessa as tabelas: ACA_PC_COMMON_CONFIG_VL, EGO_CHANGE_TYPES_VL.

**Caminho:** `FscmTopModelAM.ChangeTypesAM.EgoChangeTypesCycleTimeThresholdPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 2 | 2 | 4 | 33% |

---

## 🔗 Tabelas Relacionadas

- [[aca_pc_common_config_vl|ACA_PC_COMMON_CONFIG_VL]] — 10 atributos (2 PKs, 4 BICC)
- [[ego_change_types_vl|EGO_CHANGE_TYPES_VL]] — 2 atributos

---

## ⚙️ Atributos

### [[aca_pc_common_config_vl|ACA_PC_COMMON_CONFIG_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EgoPcCommonConfigConfigCode | CONFIG_CODE | 🔑 | ✅ |
| 2 | EgoPcCommonConfigConfigLabel | CONFIG_LABEL | — | — |
| 3 | EgoPcCommonConfigConfigType | CONFIG_TYPE | 🔑 | ✅ |
| 4 | EgoPcCommonConfigConfigValue | CONFIG_VALUE | — | ✅ |
| 5 | EgoPcCommonConfigCreatedBy | CREATED_BY | — | — |
| 6 | EgoPcCommonConfigCreationDate | CREATION_DATE | — | — |
| 7 | EgoPcCommonConfigDescription | DESCRIPTION | — | — |
| 8 | EgoPcCommonConfigLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | EgoPcCommonConfigLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | EgoPcCommonConfigLastUpdatedBy | LAST_UPDATED_BY | — | — |

### [[ego_change_types_vl|EGO_CHANGE_TYPES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EgoChangeTypesChangeTypeId | CHANGE_TYPE_ID | — | — |
| 2 | EgoChangeTypesTypeName | TYPE_NAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
