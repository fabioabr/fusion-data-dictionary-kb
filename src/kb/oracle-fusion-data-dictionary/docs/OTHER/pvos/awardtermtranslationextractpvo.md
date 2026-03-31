---
id: DOC-OTHER-PVO-AwardTermTranslationExtractPVO
doc_type: system-doc
title: "AwardTermTranslationExtractPVO — PVO Cross-Module"
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
  - AwardTermTranslationExtractPVO
  - awardtermtranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AwardTermTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Award Term Translation Extract. Acessa as tabelas: GMS_AWARD_TERMS_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.GmsBiccExtractAM.AwardTermTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gms_award_terms_tl|GMS_AWARD_TERMS_TL]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[gms_award_terms_tl|GMS_AWARD_TERMS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardTermTranslationCreatedBy | CREATED_BY | — | ✅ |
| 2 | AwardTermTranslationCreationDate | CREATION_DATE | — | ✅ |
| 3 | AwardTermTranslationDescription | DESCRIPTION | — | ✅ |
| 4 | AwardTermTranslationId | ID | 🔑 | ✅ |
| 5 | AwardTermTranslationLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | AwardTermTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | AwardTermTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | AwardTermTranslationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | AwardTermTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | AwardTermTranslationSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
