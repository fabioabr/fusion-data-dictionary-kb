---
id: DOC-OTHER-PVO-GradeTranslationExtractPVO
doc_type: system-doc
title: "GradeTranslationExtractPVO — PVO Cross-Module"
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
  - GradeTranslationExtractPVO
  - gradetranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GradeTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Grade Translation Extract. Acessa as tabelas: PER_GRADES_F_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.GradeBiccExtractAM.GradeTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 4 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[per_grades_f_tl|PER_GRADES_F_TL]] — 12 atributos (4 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[per_grades_f_tl|PER_GRADES_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 4 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 5 | GradeId | GRADE_ID | 🔑 | ✅ |
| 6 | Language | LANGUAGE | 🔑 | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | Name | NAME | — | ✅ |
| 11 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
