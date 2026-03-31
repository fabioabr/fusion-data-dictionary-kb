---
id: DOC-OTHER-PVO-AwardHeaderTranslationPVO
doc_type: system-doc
title: "AwardHeaderTranslationPVO — PVO Cross-Module"
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
  - AwardHeaderTranslationPVO
  - awardheadertranslationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AwardHeaderTranslationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Award Header Translation. Acessa as tabelas: GMS_AWARD_HEADERS_TL.

**Caminho:** `FscmTopModelAM.GmsAwardAM.AwardHeaderTranslationPVO`

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
| 1 | AwardHeaderTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | AwardHeaderTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | AwardHeaderTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | AwardHeaderTranslationPEOFtRefAwardName | FT_REF_AWARD_NAME | — | ✅ |
| 5 | AwardHeaderTranslationPEOIntellPropDesc | INTELL_PROP_DESC | — | ✅ |
| 6 | AwardHeaderTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | AwardHeaderTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | AwardHeaderTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | AwardHeaderTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | AwardHeaderTranslationPEOPreAwardGsf | PRE_AWARD_GSF | — | ✅ |
| 11 | AwardHeaderTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |
| 12 | Id | ID | 🔑 | ✅ |
| 13 | Language | LANGUAGE | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
