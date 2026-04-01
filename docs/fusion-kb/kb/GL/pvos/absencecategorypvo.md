---
id: DOC-GL-PVO-AbsenceCategoryPVO
doc_type: system-doc
title: "AbsenceCategoryPVO — PVO General Ledger"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - gl
  - data-dictionary
  - pvo
  - bicc
aliases:
  - AbsenceCategoryPVO
  - absencecategorypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AbsenceCategoryPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Absence Category. Acessa as tabelas: ANC_ABSENCE_CATEGORIES_F, ANC_ABSENCE_CATEGORIES_F_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.GlobalAbsencesAM.AbsenceCategoryPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 29 | 2 | 3 | 15 | 52% |

---

## 🔗 Tabelas Relacionadas

- [[anc_absence_categories_f|ANC_ABSENCE_CATEGORIES_F]] — 14 atributos (2 PKs, 5 BICC)
- [[anc_absence_categories_f_tl|ANC_ABSENCE_CATEGORIES_F_TL]] — 15 atributos (1 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[anc_absence_categories_f|ANC_ABSENCE_CATEGORIES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbsenceCategoryId | ABSENCE_CATEGORY_ID | 🔑 | ✅ |
| 2 | AncAbsCategoryFAltcd | ANC_ABS_CATEGORY_F_ALTCD | — | — |
| 3 | CreatedBy | CREATED_BY | — | — |
| 4 | CreationDate | CREATION_DATE | — | — |
| 5 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 6 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 7 | EnterpriseId | ENTERPRISE_ID | — | — |
| 8 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | LegislationCode | LEGISLATION_CODE | — | — |
| 12 | ModuleId | MODULE_ID | — | — |
| 13 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | Status | STATUS | — | ✅ |

### [[anc_absence_categories_f_tl|ANC_ABSENCE_CATEGORIES_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbsenceCategoryId1 | ABSENCE_CATEGORY_ID | — | ✅ |
| 2 | CreatedBy1 | CREATED_BY | — | ✅ |
| 3 | CreationDate1 | CREATION_DATE | — | ✅ |
| 4 | Description | DESCRIPTION | — | ✅ |
| 5 | EffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 6 | EffectiveStartDate1 | EFFECTIVE_START_DATE | — | ✅ |
| 7 | EnterpriseId1 | ENTERPRISE_ID | — | — |
| 8 | Language | LANGUAGE | 🔑 | ✅ |
| 9 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 10 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 11 | LastUpdatedBy1 | LAST_UPDATED_BY | — | ✅ |
| 12 | ModuleId1 | MODULE_ID | — | — |
| 13 | Name | NAME | — | ✅ |
| 14 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 15 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
