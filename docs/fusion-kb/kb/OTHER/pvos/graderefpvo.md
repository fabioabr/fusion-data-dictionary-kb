---
id: DOC-OTHER-PVO-GradeRefPVO
doc_type: system-doc
title: "GradeRefPVO — PVO Cross-Module"
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
  - GradeRefPVO
  - graderefpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GradeRefPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Grade Ref. Acessa as tabelas: PER_GRADES_F, PER_GRADES_F_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.GradeAM.GradeRefPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 25 | 2 | 3 | 11 | 44% |

---

## 🔗 Tabelas Relacionadas

- [[per_grades_f|PER_GRADES_F]] — 13 atributos (3 PKs, 7 BICC)
- [[per_grades_f_tl|PER_GRADES_F_TL]] — 12 atributos (4 BICC)

---

## ⚙️ Atributos

### [[per_grades_f|PER_GRADES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 3 | GradeId | GRADE_ID | 🔑 | ✅ |
| 4 | GradePEOActiveStatus | ACTIVE_STATUS | — | ✅ |
| 5 | GradePEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 6 | GradePEOCreatedBy | CREATED_BY | — | — |
| 7 | GradePEOCreationDate | CREATION_DATE | — | — |
| 8 | GradePEOGradeCode | GRADE_CODE | — | ✅ |
| 9 | GradePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | GradePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | GradePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | GradePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | GradePEOSetId | SET_ID | — | ✅ |

### [[per_grades_f_tl|PER_GRADES_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GradeTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | GradeTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | GradeTranslationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 4 | GradeTranslationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 5 | GradeTranslationPEOGradeId | GRADE_ID | — | — |
| 6 | GradeTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 7 | GradeTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | GradeTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | GradeTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | GradeTranslationPEOName | NAME | — | ✅ |
| 11 | GradeTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | GradeTranslationPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
