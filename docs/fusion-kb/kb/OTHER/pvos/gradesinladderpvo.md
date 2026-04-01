---
id: DOC-OTHER-PVO-GradesInLadderPVO
doc_type: system-doc
title: "GradesInLadderPVO — PVO Cross-Module"
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
  - GradesInLadderPVO
  - gradesinladderpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GradesInLadderPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Grades In Ladder. Acessa as tabelas: PER_GRADES_IN_LADDERS_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.GradeAM.GradesInLadderPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 3 | 6 | 43% |

---

## 🔗 Tabelas Relacionadas

- [[per_grades_in_ladders_f|PER_GRADES_IN_LADDERS_F]] — 14 atributos (3 PKs, 6 BICC)

---

## ⚙️ Atributos

### [[per_grades_in_ladders_f|PER_GRADES_IN_LADDERS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 2 | BusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | CreatedBy | CREATED_BY | — | — |
| 4 | CreationDate | CREATION_DATE | — | — |
| 5 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 6 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 7 | GradeId | GRADE_ID | — | ✅ |
| 8 | GradeLadderId | GRADE_LADDER_ID | — | — |
| 9 | GradesInLadderId | GRADES_IN_LADDER_ID | 🔑 | ✅ |
| 10 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | Sequence | SEQUENCE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
