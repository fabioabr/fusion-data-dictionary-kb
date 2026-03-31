---
id: DOC-OTHER-PVO-AwardCertTranslationExtractPVO
doc_type: system-doc
title: "AwardCertTranslationExtractPVO — PVO Cross-Module"
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
  - AwardCertTranslationExtractPVO
  - awardcerttranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AwardCertTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Award Cert Translation Extract. Acessa as tabelas: GMS_AWARD_CERTS_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.GmsBiccExtractAM.AwardCertTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gms_award_certs_tl|GMS_AWARD_CERTS_TL]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[gms_award_certs_tl|GMS_AWARD_CERTS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardCertTranslationComments | COMMENTS | — | ✅ |
| 2 | AwardCertTranslationCreatedBy | CREATED_BY | — | ✅ |
| 3 | AwardCertTranslationCreationDate | CREATION_DATE | — | ✅ |
| 4 | AwardCertTranslationId | ID | 🔑 | ✅ |
| 5 | AwardCertTranslationLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | AwardCertTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | AwardCertTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | AwardCertTranslationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | AwardCertTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | AwardCertTranslationSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
