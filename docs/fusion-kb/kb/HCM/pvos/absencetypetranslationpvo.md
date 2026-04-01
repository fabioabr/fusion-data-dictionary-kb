---
id: DOC-HCM-PVO-AbsenceTypeTranslationPVO
doc_type: system-doc
title: "AbsenceTypeTranslationPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - AbsenceTypeTranslationPVO
  - absencetypetranslationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AbsenceTypeTranslationPVO

## 📌 Visão Geral

Fornece traducoes multilingue dos tipos de ausencia cadastrados. Suporta operacoes globais com nomenclatura localizada por idioma.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.AbsenceAM.AbsenceTypeTranslationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 3 | 30% |

---

## 🔗 Tabelas Relacionadas

- [[per_abs_attendance_types_tl|PER_ABS_ATTENDANCE_TYPES_TL]] — 10 atributos (2 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[per_abs_attendance_types_tl|PER_ABS_ATTENDANCE_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbsenceAttendanceTypeId | ABSENCE_ATTENDANCE_TYPE_ID | 🔑 | ✅ |
| 2 | AbsenceTypeTranslationPEOCreatedBy | CREATED_BY | — | — |
| 3 | AbsenceTypeTranslationPEOCreationDate | CREATION_DATE | — | — |
| 4 | AbsenceTypeTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | AbsenceTypeTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | AbsenceTypeTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | AbsenceTypeTranslationPEOName | NAME | — | — |
| 8 | AbsenceTypeTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | AbsenceTypeTranslationPEOSourceLang | SOURCE_LANG | — | — |
| 10 | Language | LANGUAGE | 🔑 | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
