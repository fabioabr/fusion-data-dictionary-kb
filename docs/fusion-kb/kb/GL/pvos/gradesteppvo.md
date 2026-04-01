---
id: DOC-GL-PVO-GradeStepPVO
doc_type: system-doc
title: "GradeStepPVO — PVO General Ledger"
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
  - GradeStepPVO
  - gradesteppvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GradeStepPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Grade Step. Acessa as tabelas: PER_ACTION_OCCURRENCES, PER_ACTION_REASONS_B, PER_ACTION_REASONS_TL (+2).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.GradeAM.GradeStepPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 38 | 5 | 3 | 10 | 26% |

---

## 🔗 Tabelas Relacionadas

- [[per_action_occurrences|PER_ACTION_OCCURRENCES]] — 4 atributos
- [[per_action_reasons_b|PER_ACTION_REASONS_B]] — 5 atributos
- [[per_action_reasons_tl|PER_ACTION_REASONS_TL]] — 4 atributos
- [[per_grade_steps_f|PER_GRADE_STEPS_F]] — 13 atributos (3 PKs, 6 BICC)
- [[per_grade_steps_f_tl|PER_GRADE_STEPS_F_TL]] — 12 atributos (4 BICC)

---

## ⚙️ Atributos

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
| 3 | ActionReasonsPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 4 | ActionReasonsPEOEndDate | END_DATE | — | — |
| 5 | ActionReasonsPEOStartDate | START_DATE | — | — |

### [[per_action_reasons_tl|PER_ACTION_REASONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionReasonsTranslationPEOActionReason | ACTION_REASON | — | — |
| 2 | ActionReasonsTranslationPEOActionReasonsTranslationPEOActionReasonId | ACTION_REASON_ID | — | — |
| 3 | ActionReasonsTranslationPEOLanguage | LANGUAGE | — | — |
| 4 | ActionReasonsTranslationPEOSourceLang | SOURCE_LANG | — | — |

### [[per_grade_steps_f|PER_GRADE_STEPS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 3 | GradeStepId | GRADE_STEP_ID | 🔑 | ✅ |
| 4 | GradeStepPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 5 | GradeStepPEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | GradeStepPEOCreationDate | CREATION_DATE | — | — |
| 7 | GradeStepPEOGradeId | GRADE_ID | — | — |
| 8 | GradeStepPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | GradeStepPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | GradeStepPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | GradeStepPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | GradeStepPEOPayScalePointId | PAY_SCALE_POINT_ID | — | — |
| 13 | GradeStepPEOSequence | SEQUENCE | — | ✅ |

### [[per_grade_steps_f_tl|PER_GRADE_STEPS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GradeStepTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | GradeStepTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | GradeStepTranslationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 4 | GradeStepTranslationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 5 | GradeStepTranslationPEOGradeStepId | GRADE_STEP_ID | — | — |
| 6 | GradeStepTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 7 | GradeStepTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | GradeStepTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | GradeStepTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | GradeStepTranslationPEOName | NAME | — | ✅ |
| 11 | GradeStepTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | GradeStepTranslationPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
