---
id: DOC-OTHER-PVO-GradePVO
doc_type: system-doc
title: "GradePVO — PVO Cross-Module"
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
  - GradePVO
  - gradepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GradePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Grade. Acessa as tabelas: FND_SETID_SETS_VL, PER_ACTION_OCCURRENCES, PER_ACTION_REASONS_B (+3).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.GradeAM.GradePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 44 | 6 | 2 | 25 | 57% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_setid_sets_vl|FND_SETID_SETS_VL]] — 5 atributos (2 BICC)
- [[per_action_occurrences|PER_ACTION_OCCURRENCES]] — 4 atributos
- [[per_action_reasons_b|PER_ACTION_REASONS_B]] — 2 atributos
- [[per_action_reasons_tl|PER_ACTION_REASONS_TL]] — 3 atributos (1 BICC)
- [[per_grades_f|PER_GRADES_F]] — 18 atributos (2 PKs, 18 BICC)
- [[per_grades_f_tl|PER_GRADES_F_TL]] — 12 atributos (4 BICC)

---

## ⚙️ Atributos

### [[fnd_setid_sets_vl|FND_SETID_SETS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SetIdSetPEODescription | DESCRIPTION | — | — |
| 2 | SetIdSetPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 3 | SetIdSetPEOSetCode | SET_CODE | — | — |
| 4 | SetIdSetPEOSetId | SET_ID | — | — |
| 5 | SetIdSetPEOSetName | SET_NAME | — | ✅ |

### [[per_action_occurrences|PER_ACTION_OCCURRENCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionOccurrencesPEOActionDate | ACTION_DATE | — | — |
| 2 | ActionOccurrencesPEOActionId | ACTION_ID | — | — |
| 3 | ActionOccurrencesPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 4 | ActionOccurrencesPEOActionReasonId | ACTION_REASON_ID | — | — |

### [[per_action_reasons_b|PER_ACTION_REASONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionReasonsPEOActionReasonCode | ACTION_REASON_CODE | — | — |
| 2 | ActionReasonsPEOActionReasonId | ACTION_REASON_ID | — | — |

### [[per_action_reasons_tl|PER_ACTION_REASONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionReasonsTLPEOActionReason | ACTION_REASON | — | ✅ |
| 2 | ActionReasonsTLPEOActionReasonId | ACTION_REASON_ID | — | — |
| 3 | ActionReasonsTLPEOLanguage | LANGUAGE | — | — |

### [[per_grades_f|PER_GRADES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 3 | GradeId | GRADE_ID | 🔑 | ✅ |
| 4 | GradePEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | ✅ |
| 5 | GradePEOActiveStatus | ACTIVE_STATUS | — | ✅ |
| 6 | GradePEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 7 | GradePEOCeilingStepId | CEILING_STEP_ID | — | ✅ |
| 8 | GradePEOCreatedBy | CREATED_BY | — | ✅ |
| 9 | GradePEOCreationDate | CREATION_DATE | — | ✅ |
| 10 | GradePEOGradeCode | GRADE_CODE | — | ✅ |
| 11 | GradePEOGradeType | GRADE_TYPE | — | ✅ |
| 12 | GradePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | GradePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | GradePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | GradePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 16 | GradePEOPayScaleId | PAY_SCALE_ID | — | ✅ |
| 17 | GradePEOSetId | SET_ID | — | ✅ |
| 18 | GradePEOStartingStep | STARTING_STEP | — | ✅ |

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
