---
id: DOC-OTHER-PVO-BurdenScheduleTranslationExtractPVO
doc_type: system-doc
title: "BurdenScheduleTranslationExtractPVO — PVO Cross-Module"
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
  - BurdenScheduleTranslationExtractPVO
  - burdenscheduletranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BurdenScheduleTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Burden Schedule Translation Extract. Acessa as tabelas: PJF_IND_RATE_SCH_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.BurdenScheduleTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_ind_rate_sch_tl|PJF_IND_RATE_SCH_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[pjf_ind_rate_sch_tl|PJF_IND_RATE_SCH_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BurdenScheduleTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | BurdenScheduleTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | BurdenScheduleTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | BurdenScheduleTranslationPEOIndRateSchId | IND_RATE_SCH_ID | 🔑 | ✅ |
| 5 | BurdenScheduleTranslationPEOIndSchName | IND_SCH_NAME | — | ✅ |
| 6 | BurdenScheduleTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 7 | BurdenScheduleTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | BurdenScheduleTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | BurdenScheduleTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | BurdenScheduleTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | BurdenScheduleTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
