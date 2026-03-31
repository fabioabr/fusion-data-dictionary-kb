---
id: DOC-OTHER-PVO-SponsorAcctDetailTranslationExtractPVO
doc_type: system-doc
title: "SponsorAcctDetailTranslationExtractPVO — PVO Cross-Module"
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
  - SponsorAcctDetailTranslationExtractPVO
  - sponsoracctdetailtranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SponsorAcctDetailTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Sponsor Acct Detail Translation Extract. Acessa as tabelas: GMS_SPONSOR_ACCT_DETAILS_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.GmsBiccExtractAM.SponsorAcctDetailTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gms_sponsor_acct_details_tl|GMS_SPONSOR_ACCT_DETAILS_TL]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[gms_sponsor_acct_details_tl|GMS_SPONSOR_ACCT_DETAILS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SponsorAcctDetailTranslationComments | COMMENTS | — | ✅ |
| 2 | SponsorAcctDetailTranslationCreatedBy | CREATED_BY | — | ✅ |
| 3 | SponsorAcctDetailTranslationCreationDate | CREATION_DATE | — | ✅ |
| 4 | SponsorAcctDetailTranslationLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | SponsorAcctDetailTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | SponsorAcctDetailTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | SponsorAcctDetailTranslationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | SponsorAcctDetailTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | SponsorAcctDetailTranslationSourceLang | SOURCE_LANG | — | ✅ |
| 10 | SponsorAcctDetailTranslationSponsorAcctDetailsId | SPONSOR_ACCT_DETAILS_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
