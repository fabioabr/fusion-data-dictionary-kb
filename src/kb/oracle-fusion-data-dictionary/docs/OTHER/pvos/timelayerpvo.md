---
id: DOC-OTHER-PVO-TimeLayerPVO
doc_type: system-doc
title: "TimeLayerPVO — PVO Cross-Module"
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
  - TimeLayerPVO
  - timelayerpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TimeLayerPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Time Layer. Acessa as tabelas: HWM_LAYER.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.TimeRepositoryAM.TimeLayerPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 1 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_layer|HWM_LAYER]] — 13 atributos (1 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[hwm_layer|HWM_LAYER]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Auditable | AUDITABLE | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | Description | DESCRIPTION | — | ✅ |
| 5 | EnterpriseId | ENTERPRISE_ID | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | LayerCode | LAYER_CODE | — | ✅ |
| 10 | LayerId | LAYER_ID | 🔑 | ✅ |
| 11 | ModuleId | MODULE_ID | — | ✅ |
| 12 | Name | NAME | — | ✅ |
| 13 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
