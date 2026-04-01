---
id: DOC-OTHER-PVO-PaymentTermHeaderTranslationExtractPVO
doc_type: system-doc
title: "PaymentTermHeaderTranslationExtractPVO — PVO Cross-Module"
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
  - PaymentTermHeaderTranslationExtractPVO
  - paymenttermheadertranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PaymentTermHeaderTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Payment Term Header Translation Extract. Acessa as tabelas: AP_TERMS_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ApBiccExtractAM.PaymentTermHeaderTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ap_terms_tl|AP_TERMS_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[ap_terms_tl|AP_TERMS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PaymentTermHeaderTranslationCreatedBy | CREATED_BY | — | ✅ |
| 2 | PaymentTermHeaderTranslationCreationDate | CREATION_DATE | — | ✅ |
| 3 | PaymentTermHeaderTranslationDescription | DESCRIPTION | — | ✅ |
| 4 | PaymentTermHeaderTranslationLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | PaymentTermHeaderTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | PaymentTermHeaderTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | PaymentTermHeaderTranslationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | PaymentTermHeaderTranslationName | NAME | — | ✅ |
| 9 | PaymentTermHeaderTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | PaymentTermHeaderTranslationSourceLang | SOURCE_LANG | — | ✅ |
| 11 | PaymentTermHeaderTranslationTermId | TERM_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
