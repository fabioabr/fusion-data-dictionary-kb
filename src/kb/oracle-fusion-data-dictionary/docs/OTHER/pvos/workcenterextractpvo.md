---
id: DOC-OTHER-PVO-WorkCenterExtractPVO
doc_type: system-doc
title: "WorkCenterExtractPVO — PVO Cross-Module"
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
  - WorkCenterExtractPVO
  - workcenterextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WorkCenterExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Work Center Extract. Acessa as tabelas: WIS_WORK_CENTERS_B, WIS_WORK_CENTERS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.WisBiccExtractAM.WorkCenterExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 64 | 2 | 3 | 64 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[wis_work_centers_b|WIS_WORK_CENTERS_B]] — 53 atributos (1 PKs, 53 BICC)
- [[wis_work_centers_tl|WIS_WORK_CENTERS_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[wis_work_centers_b|WIS_WORK_CENTERS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 2 | AttributeChar1 | ATTRIBUTE_CHAR1 | — | ✅ |
| 3 | AttributeChar10 | ATTRIBUTE_CHAR10 | — | ✅ |
| 4 | AttributeChar11 | ATTRIBUTE_CHAR11 | — | ✅ |
| 5 | AttributeChar12 | ATTRIBUTE_CHAR12 | — | ✅ |
| 6 | AttributeChar13 | ATTRIBUTE_CHAR13 | — | ✅ |
| 7 | AttributeChar14 | ATTRIBUTE_CHAR14 | — | ✅ |
| 8 | AttributeChar15 | ATTRIBUTE_CHAR15 | — | ✅ |
| 9 | AttributeChar16 | ATTRIBUTE_CHAR16 | — | ✅ |
| 10 | AttributeChar17 | ATTRIBUTE_CHAR17 | — | ✅ |
| 11 | AttributeChar18 | ATTRIBUTE_CHAR18 | — | ✅ |
| 12 | AttributeChar19 | ATTRIBUTE_CHAR19 | — | ✅ |
| 13 | AttributeChar2 | ATTRIBUTE_CHAR2 | — | ✅ |
| 14 | AttributeChar20 | ATTRIBUTE_CHAR20 | — | ✅ |
| 15 | AttributeChar3 | ATTRIBUTE_CHAR3 | — | ✅ |
| 16 | AttributeChar4 | ATTRIBUTE_CHAR4 | — | ✅ |
| 17 | AttributeChar5 | ATTRIBUTE_CHAR5 | — | ✅ |
| 18 | AttributeChar6 | ATTRIBUTE_CHAR6 | — | ✅ |
| 19 | AttributeChar7 | ATTRIBUTE_CHAR7 | — | ✅ |
| 20 | AttributeChar8 | ATTRIBUTE_CHAR8 | — | ✅ |
| 21 | AttributeChar9 | ATTRIBUTE_CHAR9 | — | ✅ |
| 22 | AttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 23 | AttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 24 | AttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 25 | AttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 26 | AttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 27 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 28 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 29 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 30 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 31 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 32 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 33 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 34 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 35 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 36 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 37 | AttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 38 | AttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 39 | AttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 40 | AttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 41 | AttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 42 | CreatedBy | CREATED_BY | — | ✅ |
| 43 | CreationDate | CREATION_DATE | — | ✅ |
| 44 | InactiveDate | INACTIVE_DATE | — | ✅ |
| 45 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 46 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 47 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 48 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 49 | OrganizationId | ORGANIZATION_ID | — | ✅ |
| 50 | OverrideCalendarFlag | OVERRIDE_CALENDAR_FLAG | — | ✅ |
| 51 | WorkAreaId | WORK_AREA_ID | — | ✅ |
| 52 | WorkCenterCode | WORK_CENTER_CODE | — | ✅ |
| 53 | WorkCenterId | WORK_CENTER_ID | 🔑 | ✅ |

### [[wis_work_centers_tl|WIS_WORK_CENTERS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkCenterTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | WorkCenterTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | WorkCenterTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 4 | WorkCenterTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | WorkCenterTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | WorkCenterTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | WorkCenterTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | WorkCenterTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |
| 9 | WorkCenterTranslationPEOWorkCenterDescription | WORK_CENTER_DESCRIPTION | — | ✅ |
| 10 | WorkCenterTranslationPEOWorkCenterId | WORK_CENTER_ID | 🔑 | ✅ |
| 11 | WorkCenterTranslationPEOWorkCenterName | WORK_CENTER_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
