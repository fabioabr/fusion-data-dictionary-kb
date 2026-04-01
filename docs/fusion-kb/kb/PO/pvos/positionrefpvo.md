---
id: DOC-PO-PVO-PositionRefPVO
doc_type: system-doc
title: "PositionRefPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - PositionRefPVO
  - positionrefpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PositionRefPVO

## 📌 Visão Geral

Extrai referências de posições organizacionais, vinculando cargos a nomes e traduções. Suporta análise de estrutura hierárquica e identificação de posições na organização.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.PositionAM.PositionRefPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 32 | 2 | 3 | 10 | 31% |

---

## 🔗 Tabelas Relacionadas

- [[hr_all_positions_f|HR_ALL_POSITIONS_F]] — 20 atributos (3 PKs, 6 BICC)
- [[hr_all_positions_f_tl|HR_ALL_POSITIONS_F_TL]] — 12 atributos (4 BICC)

---

## ⚙️ Atributos

### [[hr_all_positions_f|HR_ALL_POSITIONS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 3 | PositionId | POSITION_ID | 🔑 | ✅ |
| 4 | PositionPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 5 | PositionPEOActiveStatus | ACTIVE_STATUS | — | ✅ |
| 6 | PositionPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 7 | PositionPEOBargainingUnitCd | BARGAINING_UNIT_CD | — | — |
| 8 | PositionPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 9 | PositionPEOBusinessUnitId | BUSINESS_UNIT_ID | — | — |
| 10 | PositionPEOCalculateFte | CALCULATE_FTE | — | — |
| 11 | PositionPEOCreatedBy | CREATED_BY | — | — |
| 12 | PositionPEOCreationDate | CREATION_DATE | — | — |
| 13 | PositionPEOJobId | JOB_ID | — | — |
| 14 | PositionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | PositionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | PositionPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 17 | PositionPEOLocationId | LOCATION_ID | — | — |
| 18 | PositionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 19 | PositionPEOOrganizationId | ORGANIZATION_ID | — | — |
| 20 | PositionPEOPositionCode | POSITION_CODE | — | ✅ |

### [[hr_all_positions_f_tl|HR_ALL_POSITIONS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PositionTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | PositionTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | PositionTranslationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 4 | PositionTranslationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 5 | PositionTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 6 | PositionTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | PositionTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | PositionTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | PositionTranslationPEOName | NAME | — | ✅ |
| 10 | PositionTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | PositionTranslationPEOPositionId | POSITION_ID | — | — |
| 12 | PositionTranslationPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
