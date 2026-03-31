---
id: DOC-AP-PVO-TaxRegimeTranslationPVO
doc_type: system-doc
title: "TaxRegimeTranslationPVO — PVO Accounts Payable"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ap
  - data-dictionary
  - pvo
  - bicc
aliases:
  - TaxRegimeTranslationPVO
  - taxregimetranslationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TaxRegimeTranslationPVO

## 📌 Visão Geral

Extrai as traduções dos nomes de regimes fiscais para diferentes idiomas. Necessário para operações internacionais onde os regimes tributários precisam ser apresentados no idioma local do usuário.

**Caminho:** `FscmTopModelAM.FinApInvTransactionsAM.TaxRegimeTranslationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 2 | 4 | 44% |

---

## 🔗 Tabelas Relacionadas

- [[zx_regimes_tl|ZX_REGIMES_TL]] — 9 atributos (2 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[zx_regimes_tl|ZX_REGIMES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Language | LANGUAGE | 🔑 | ✅ |
| 2 | TaxRegimeId | TAX_REGIME_ID | 🔑 | ✅ |
| 3 | TaxRegimeTLPEOCreatedBy | CREATED_BY | — | — |
| 4 | TaxRegimeTLPEOCreationDate | CREATION_DATE | — | — |
| 5 | TaxRegimeTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | TaxRegimeTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | TaxRegimeTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | TaxRegimeTLPEOSourceLang | SOURCE_LANG | — | — |
| 9 | TaxRegimeTLPEOTaxRegimeName | TAX_REGIME_NAME | — | ✅ |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
