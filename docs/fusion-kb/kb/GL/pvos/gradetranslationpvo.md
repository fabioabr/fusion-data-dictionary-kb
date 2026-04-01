---
id: DOC-GL-PVO-GradeTranslationPVO
doc_type: system-doc
title: "GradeTranslationPVO — PVO General Ledger"
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
  - GradeTranslationPVO
  - gradetranslationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GradeTranslationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Grade Translation. Acessa as tabelas: PER_GRADES_F_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.GradeAM.GradeTranslationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 3 | 10 | 83% |

---

## 🔗 Tabelas Relacionadas

- [[per_grades_f_tl|PER_GRADES_F_TL]] — 12 atributos (3 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[per_grades_f_tl|PER_GRADES_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 3 | GradeId | GRADE_ID | 🔑 | ✅ |
| 4 | GradeTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | GradeTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | GradeTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | GradeTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | GradeTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | GradeTranslationPEOName | NAME | — | ✅ |
| 10 | GradeTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | GradeTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |
| 12 | Language | LANGUAGE | 🔑 | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
