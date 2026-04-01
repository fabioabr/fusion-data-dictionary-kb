---
id: DOC-AP-PVO-TransactionTaxTranslationPVO
doc_type: system-doc
title: "TransactionTaxTranslationPVO — PVO Accounts Payable"
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
  - TransactionTaxTranslationPVO
  - transactiontaxtranslationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TransactionTaxTranslationPVO

## 📌 Visão Geral

Extrai as traduções dos nomes de impostos transacionais para diferentes idiomas. Necessário para conformidade tributária internacional, garantindo que os impostos sejam identificáveis no idioma local.

**Caminho:** `FscmTopModelAM.FinApInvTransactionsAM.TransactionTaxTranslationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 2 | 4 | 44% |

---

## 🔗 Tabelas Relacionadas

- [[zx_taxes_tl|ZX_TAXES_TL]] — 9 atributos (2 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[zx_taxes_tl|ZX_TAXES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Language | LANGUAGE | 🔑 | ✅ |
| 2 | TaxId | TAX_ID | 🔑 | ✅ |
| 3 | TransactionTaxTLPEOCreatedBy | CREATED_BY | — | — |
| 4 | TransactionTaxTLPEOCreationDate | CREATION_DATE | — | — |
| 5 | TransactionTaxTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | TransactionTaxTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | TransactionTaxTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | TransactionTaxTLPEOSourceLang | SOURCE_LANG | — | — |
| 9 | TransactionTaxTLPEOTaxFullName | TAX_FULL_NAME | — | ✅ |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
