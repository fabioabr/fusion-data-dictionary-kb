---
id: DOC-OTHER-PVO-ProjectAssetAssignmentExtractPVO
doc_type: system-doc
title: "ProjectAssetAssignmentExtractPVO — PVO Cross-Module"
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
  - ProjectAssetAssignmentExtractPVO
  - projectassetassignmentextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectAssetAssignmentExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Asset Assignment Extract. Acessa as tabelas: PJC_PRJ_ASSET_ASGS.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjcBiccExtractAM.ProjectAssetAssignmentExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 26 | 1 | 3 | 10 | 38% |

---

## 🔗 Tabelas Relacionadas

- [[pjc_prj_asset_asgs|PJC_PRJ_ASSET_ASGS]] — 26 atributos (3 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[pjc_prj_asset_asgs|PJC_PRJ_ASSET_ASGS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjcPrjAssetAsgsAssetAssignmentId | ASSET_ASSIGNMENT_ID | — | ✅ |
| 2 | PjcPrjAssetAsgsAttribute1 | ATTRIBUTE1 | — | — |
| 3 | PjcPrjAssetAsgsAttribute10 | ATTRIBUTE10 | — | — |
| 4 | PjcPrjAssetAsgsAttribute11 | ATTRIBUTE11 | — | — |
| 5 | PjcPrjAssetAsgsAttribute12 | ATTRIBUTE12 | — | — |
| 6 | PjcPrjAssetAsgsAttribute13 | ATTRIBUTE13 | — | — |
| 7 | PjcPrjAssetAsgsAttribute14 | ATTRIBUTE14 | — | — |
| 8 | PjcPrjAssetAsgsAttribute15 | ATTRIBUTE15 | — | — |
| 9 | PjcPrjAssetAsgsAttribute2 | ATTRIBUTE2 | — | — |
| 10 | PjcPrjAssetAsgsAttribute3 | ATTRIBUTE3 | — | — |
| 11 | PjcPrjAssetAsgsAttribute4 | ATTRIBUTE4 | — | — |
| 12 | PjcPrjAssetAsgsAttribute5 | ATTRIBUTE5 | — | — |
| 13 | PjcPrjAssetAsgsAttribute6 | ATTRIBUTE6 | — | — |
| 14 | PjcPrjAssetAsgsAttribute7 | ATTRIBUTE7 | — | — |
| 15 | PjcPrjAssetAsgsAttribute8 | ATTRIBUTE8 | — | — |
| 16 | PjcPrjAssetAsgsAttribute9 | ATTRIBUTE9 | — | — |
| 17 | PjcPrjAssetAsgsAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 18 | PjcPrjAssetAsgsCreatedBy | CREATED_BY | — | ✅ |
| 19 | PjcPrjAssetAsgsCreationDate | CREATION_DATE | — | ✅ |
| 20 | PjcPrjAssetAsgsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 21 | PjcPrjAssetAsgsLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 22 | PjcPrjAssetAsgsLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 23 | PjcPrjAssetAsgsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 24 | PjcPrjAssetAsgsProjectAssetId | PROJECT_ASSET_ID | 🔑 | ✅ |
| 25 | PjcPrjAssetAsgsProjectId | PROJECT_ID | 🔑 | ✅ |
| 26 | PjcPrjAssetAsgsTaskId | TASK_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
