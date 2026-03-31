---
id: DOC-OTHER-PVO-AwardTermExtractPVO
doc_type: system-doc
title: "AwardTermExtractPVO — PVO Cross-Module"
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
  - AwardTermExtractPVO
  - awardtermextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AwardTermExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Award Term Extract. Acessa as tabelas: GMS_AWARD_TERMS_B, GMS_AWARD_TERMS_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.GmsBiccExtractAM.AwardTermExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 2 | 1 | 22 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gms_award_terms_b|GMS_AWARD_TERMS_B]] — 12 atributos (1 PKs, 12 BICC)
- [[gms_award_terms_tl|GMS_AWARD_TERMS_TL]] — 10 atributos (10 BICC)

---

## ⚙️ Atributos

### [[gms_award_terms_b|GMS_AWARD_TERMS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardTermBaseAwardId | AWARD_ID | — | ✅ |
| 2 | AwardTermBaseCreatedBy | CREATED_BY | — | ✅ |
| 3 | AwardTermBaseCreationDate | CREATION_DATE | — | ✅ |
| 4 | AwardTermBaseId | ID | 🔑 | ✅ |
| 5 | AwardTermBaseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | AwardTermBaseLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | AwardTermBaseLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | AwardTermBaseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | AwardTermBaseTermCategoryId | TERM_CATEGORY_ID | — | ✅ |
| 10 | AwardTermBaseTermId | TERM_ID | — | ✅ |
| 11 | AwardTermBaseTermOperand | TERM_OPERAND | — | ✅ |
| 12 | AwardTermBaseTermValue | TERM_VALUE | — | ✅ |

### [[gms_award_terms_tl|GMS_AWARD_TERMS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardTermTransLangCreatedBy | CREATED_BY | — | ✅ |
| 2 | AwardTermTransLangCreationDate | CREATION_DATE | — | ✅ |
| 3 | AwardTermTransLangDescription | DESCRIPTION | — | ✅ |
| 4 | AwardTermTransLangId | ID | — | ✅ |
| 5 | AwardTermTransLangLanguage | LANGUAGE | — | ✅ |
| 6 | AwardTermTransLangLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | AwardTermTransLangLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | AwardTermTransLangLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | AwardTermTransLangObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | AwardTermTransLangSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
