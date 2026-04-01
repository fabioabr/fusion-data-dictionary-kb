---
id: DOC-OTHER-PVO-WorkCenterPVO
doc_type: system-doc
title: "WorkCenterPVO — PVO Cross-Module"
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
  - WorkCenterPVO
  - workcenterpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WorkCenterPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Work Center. Acessa as tabelas: WIS_WORK_AREAS_VL, WIS_WORK_CENTERS_B, WIS_WORK_CENTERS_TL.

**Caminho:** `FscmTopModelAM.WorkCenterAM.WorkCenterPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 26 | 3 | 1 | 17 | 65% |

---

## 🔗 Tabelas Relacionadas

- [[wis_work_areas_vl|WIS_WORK_AREAS_VL]] — 4 atributos (4 BICC)
- [[wis_work_centers_b|WIS_WORK_CENTERS_B]] — 11 atributos (1 PKs, 7 BICC)
- [[wis_work_centers_tl|WIS_WORK_CENTERS_TL]] — 11 atributos (6 BICC)

---

## ⚙️ Atributos

### [[wis_work_areas_vl|WIS_WORK_AREAS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkAreaPEOWorkAreaCode | WORK_AREA_CODE | — | ✅ |
| 2 | WorkAreaPEOWorkAreaDescription | WORK_AREA_DESCRIPTION | — | ✅ |
| 3 | WorkAreaPEOWorkAreaId | WORK_AREA_ID | — | ✅ |
| 4 | WorkAreaPEOWorkAreaName | WORK_AREA_NAME | — | ✅ |

### [[wis_work_centers_b|WIS_WORK_CENTERS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkCenterId | WORK_CENTER_ID | 🔑 | ✅ |
| 2 | WorkCenterPEOCreatedBy | CREATED_BY | — | — |
| 3 | WorkCenterPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | WorkCenterPEOInactiveDate | INACTIVE_DATE | — | ✅ |
| 5 | WorkCenterPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | WorkCenterPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | WorkCenterPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | WorkCenterPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | WorkCenterPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 10 | WorkCenterPEOWorkAreaId | WORK_AREA_ID | — | ✅ |
| 11 | WorkCenterPEOWorkCenterCode | WORK_CENTER_CODE | — | ✅ |

### [[wis_work_centers_tl|WIS_WORK_CENTERS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkCenterTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | WorkCenterTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | WorkCenterTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 4 | WorkCenterTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | WorkCenterTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | WorkCenterTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | WorkCenterTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | WorkCenterTranslationPEOSourceLang | SOURCE_LANG | — | — |
| 9 | WorkCenterTranslationPEOWorkCenterDescription | WORK_CENTER_DESCRIPTION | — | ✅ |
| 10 | WorkCenterTranslationPEOWorkCenterId | WORK_CENTER_ID | — | ✅ |
| 11 | WorkCenterTranslationPEOWorkCenterName | WORK_CENTER_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
