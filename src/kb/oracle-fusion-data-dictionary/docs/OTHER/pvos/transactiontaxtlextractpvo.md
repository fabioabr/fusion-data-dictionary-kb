---
id: DOC-OTHER-PVO-TransactionTaxTLExtractPVO
doc_type: system-doc
title: "TransactionTaxTLExtractPVO — PVO Cross-Module"
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
  - TransactionTaxTLExtractPVO
  - transactiontaxtlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TransactionTaxTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Transaction Tax TLExtract. Acessa as tabelas: ZX_TAXES_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ZxBiccExtractAM.TransactionTaxTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 2 | 9 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[zx_taxes_tl|ZX_TAXES_TL]] — 9 atributos (2 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[zx_taxes_tl|ZX_TAXES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionTaxTLCreatedBy | CREATED_BY | — | ✅ |
| 2 | TransactionTaxTLCreationDate | CREATION_DATE | — | ✅ |
| 3 | TransactionTaxTLLanguage | LANGUAGE | 🔑 | ✅ |
| 4 | TransactionTaxTLLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | TransactionTaxTLLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | TransactionTaxTLLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | TransactionTaxTLSourceLang | SOURCE_LANG | — | ✅ |
| 8 | TransactionTaxTLTaxFullName | TAX_FULL_NAME | — | ✅ |
| 9 | TransactionTaxTLTaxId | TAX_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
