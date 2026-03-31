---
id: DOC-OTHER-PVO-PatternExtractPVO
doc_type: system-doc
title: "PatternExtractPVO — PVO Cross-Module"
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
  - PatternExtractPVO
  - patternextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PatternExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Pattern Extract. Acessa as tabelas: ZMM_SR_PATTERNS_B, ZMM_SR_PATTERNS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.ScmRcsBiccExtractAM.PatternExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 43 | 2 | 1 | 42 | 98% |

---

## 🔗 Tabelas Relacionadas

- [[zmm_sr_patterns_b|ZMM_SR_PATTERNS_B]] — 40 atributos (1 PKs, 40 BICC)
- [[zmm_sr_patterns_tl|ZMM_SR_PATTERNS_TL]] — 3 atributos (2 BICC)

---

## ⚙️ Atributos

### [[zmm_sr_patterns_b|ZMM_SR_PATTERNS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PatternId | PATTERN_ID | 🔑 | ✅ |
| 2 | PatternPEOAttribute1 | ATTRIBUTE1 | — | ✅ |
| 3 | PatternPEOAttribute10 | ATTRIBUTE10 | — | ✅ |
| 4 | PatternPEOAttribute11 | ATTRIBUTE11 | — | ✅ |
| 5 | PatternPEOAttribute12 | ATTRIBUTE12 | — | ✅ |
| 6 | PatternPEOAttribute13 | ATTRIBUTE13 | — | ✅ |
| 7 | PatternPEOAttribute14 | ATTRIBUTE14 | — | ✅ |
| 8 | PatternPEOAttribute15 | ATTRIBUTE15 | — | ✅ |
| 9 | PatternPEOAttribute16 | ATTRIBUTE16 | — | ✅ |
| 10 | PatternPEOAttribute17 | ATTRIBUTE17 | — | ✅ |
| 11 | PatternPEOAttribute18 | ATTRIBUTE18 | — | ✅ |
| 12 | PatternPEOAttribute19 | ATTRIBUTE19 | — | ✅ |
| 13 | PatternPEOAttribute2 | ATTRIBUTE2 | — | ✅ |
| 14 | PatternPEOAttribute20 | ATTRIBUTE20 | — | ✅ |
| 15 | PatternPEOAttribute21 | ATTRIBUTE21 | — | ✅ |
| 16 | PatternPEOAttribute22 | ATTRIBUTE22 | — | ✅ |
| 17 | PatternPEOAttribute23 | ATTRIBUTE23 | — | ✅ |
| 18 | PatternPEOAttribute24 | ATTRIBUTE24 | — | ✅ |
| 19 | PatternPEOAttribute25 | ATTRIBUTE25 | — | ✅ |
| 20 | PatternPEOAttribute26 | ATTRIBUTE26 | — | ✅ |
| 21 | PatternPEOAttribute27 | ATTRIBUTE27 | — | ✅ |
| 22 | PatternPEOAttribute28 | ATTRIBUTE28 | — | ✅ |
| 23 | PatternPEOAttribute29 | ATTRIBUTE29 | — | ✅ |
| 24 | PatternPEOAttribute3 | ATTRIBUTE3 | — | ✅ |
| 25 | PatternPEOAttribute30 | ATTRIBUTE30 | — | ✅ |
| 26 | PatternPEOAttribute4 | ATTRIBUTE4 | — | ✅ |
| 27 | PatternPEOAttribute5 | ATTRIBUTE5 | — | ✅ |
| 28 | PatternPEOAttribute6 | ATTRIBUTE6 | — | ✅ |
| 29 | PatternPEOAttribute7 | ATTRIBUTE7 | — | ✅ |
| 30 | PatternPEOAttribute8 | ATTRIBUTE8 | — | ✅ |
| 31 | PatternPEOAttribute9 | ATTRIBUTE9 | — | ✅ |
| 32 | PatternPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 33 | PatternPEOCreatedBy | CREATED_BY | — | ✅ |
| 34 | PatternPEOCreationDate | CREATION_DATE | — | ✅ |
| 35 | PatternPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 36 | PatternPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 37 | PatternPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 38 | PatternPEOLengthDaysNum | LENGTH_DAYS_NUM | — | ✅ |
| 39 | PatternPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 40 | PatternPEOPatternTypeCode | PATTERN_TYPE_CODE | — | ✅ |

### [[zmm_sr_patterns_tl|ZMM_SR_PATTERNS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PatternTranslationPEOLanguage | LANGUAGE | — | — |
| 2 | PatternTranslationPEOPatternDesc | PATTERN_DESC | — | ✅ |
| 3 | PatternTranslationPEOPatternName | PATTERN_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
