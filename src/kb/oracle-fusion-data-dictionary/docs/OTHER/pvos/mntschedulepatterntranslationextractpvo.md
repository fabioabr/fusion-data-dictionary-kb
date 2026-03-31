---
id: DOC-OTHER-PVO-MntSchedulePatternTranslationExtractPVO
doc_type: system-doc
title: "MntSchedulePatternTranslationExtractPVO — PVO Cross-Module"
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
  - MntSchedulePatternTranslationExtractPVO
  - mntschedulepatterntranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MntSchedulePatternTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Mnt Schedule Pattern Translation Extract. Acessa as tabelas: MNT_SCHEDULE_PATTERNS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.MntBiccExtractAM.MntSchedulePatternTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[mnt_schedule_patterns_tl|MNT_SCHEDULE_PATTERNS_TL]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[mnt_schedule_patterns_tl|MNT_SCHEDULE_PATTERNS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | Language | LANGUAGE | 🔑 | ✅ |
| 4 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | SchedulePatternDesc | SCHEDULE_PATTERN_DESC | — | ✅ |
| 9 | SchedulePatternId | SCHEDULE_PATTERN_ID | 🔑 | ✅ |
| 10 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
