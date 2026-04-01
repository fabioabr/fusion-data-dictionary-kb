---
id: DOC-OTHER-PVO-AwardFundingTranslationExtractPVO
doc_type: system-doc
title: "AwardFundingTranslationExtractPVO — PVO Cross-Module"
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
  - AwardFundingTranslationExtractPVO
  - awardfundingtranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AwardFundingTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Award Funding Translation Extract. Acessa as tabelas: GMS_AWARD_FUNDINGS_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.GmsBiccExtractAM.AwardFundingTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gms_award_fundings_tl|GMS_AWARD_FUNDINGS_TL]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[gms_award_fundings_tl|GMS_AWARD_FUNDINGS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardFundingTranslationCreatedBy | CREATED_BY | — | ✅ |
| 2 | AwardFundingTranslationCreationDate | CREATION_DATE | — | ✅ |
| 3 | AwardFundingTranslationId | ID | 🔑 | ✅ |
| 4 | AwardFundingTranslationIssueDescription | ISSUE_DESCRIPTION | — | ✅ |
| 5 | AwardFundingTranslationLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | AwardFundingTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | AwardFundingTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | AwardFundingTranslationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | AwardFundingTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | AwardFundingTranslationSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
