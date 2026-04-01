---
id: DOC-OTHER-PVO-AwardHeaderTranslationExtractPVO
doc_type: system-doc
title: "AwardHeaderTranslationExtractPVO — PVO Cross-Module"
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
  - AwardHeaderTranslationExtractPVO
  - awardheadertranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AwardHeaderTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Award Header Translation Extract. Acessa as tabelas: GMS_AWARD_HEADERS_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.GmsBiccExtractAM.AwardHeaderTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 2 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gms_award_headers_tl|GMS_AWARD_HEADERS_TL]] — 13 atributos (2 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[gms_award_headers_tl|GMS_AWARD_HEADERS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardHeaderTranslationCreatedBy | CREATED_BY | — | ✅ |
| 2 | AwardHeaderTranslationCreationDate | CREATION_DATE | — | ✅ |
| 3 | AwardHeaderTranslationDescription | DESCRIPTION | — | ✅ |
| 4 | AwardHeaderTranslationFtRefAwardName | FT_REF_AWARD_NAME | — | ✅ |
| 5 | AwardHeaderTranslationId | ID | 🔑 | ✅ |
| 6 | AwardHeaderTranslationIntellPropDesc | INTELL_PROP_DESC | — | ✅ |
| 7 | AwardHeaderTranslationLanguage | LANGUAGE | 🔑 | ✅ |
| 8 | AwardHeaderTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | AwardHeaderTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | AwardHeaderTranslationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | AwardHeaderTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | AwardHeaderTranslationPreAwardGsf | PRE_AWARD_GSF | — | ✅ |
| 13 | AwardHeaderTranslationSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
