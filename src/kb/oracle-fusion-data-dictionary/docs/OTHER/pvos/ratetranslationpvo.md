---
id: DOC-OTHER-PVO-RateTranslationPVO
doc_type: system-doc
title: "RateTranslationPVO — PVO Cross-Module"
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
  - RateTranslationPVO
  - ratetranslationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RateTranslationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Rate Translation. Acessa as tabelas: PER_RATES_F_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.GradeAM.RateTranslationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 4 | 5 | 42% |

---

## 🔗 Tabelas Relacionadas

- [[per_rates_f_tl|PER_RATES_F_TL]] — 12 atributos (4 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[per_rates_f_tl|PER_RATES_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 3 | Language | LANGUAGE | 🔑 | ✅ |
| 4 | RateId | RATE_ID | 🔑 | ✅ |
| 5 | RateTranslationPEOCreatedBy | CREATED_BY | — | — |
| 6 | RateTranslationPEOCreationDate | CREATION_DATE | — | — |
| 7 | RateTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | RateTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | RateTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | RateTranslationPEOName | NAME | — | — |
| 11 | RateTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | RateTranslationPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
