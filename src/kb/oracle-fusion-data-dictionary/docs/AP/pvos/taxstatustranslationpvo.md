---
id: DOC-AP-PVO-TaxStatusTranslationPVO
doc_type: system-doc
title: "TaxStatusTranslationPVO — PVO Accounts Payable"
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
  - TaxStatusTranslationPVO
  - taxstatustranslationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TaxStatusTranslationPVO

## 📌 Visão Geral

Extrai as traduções dos nomes de status fiscais para diferentes idiomas. Necessário para conformidade tributária em operações multinacionais, garantindo clareza na classificação fiscal em cada localidade.

**Caminho:** `FscmTopModelAM.FinApInvTransactionsAM.TaxStatusTranslationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 2 | 4 | 44% |

---

## 🔗 Tabelas Relacionadas

- [[zx_status_tl|ZX_STATUS_TL]] — 9 atributos (2 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[zx_status_tl|ZX_STATUS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Language | LANGUAGE | 🔑 | ✅ |
| 2 | TaxStatusId | TAX_STATUS_ID | 🔑 | ✅ |
| 3 | TaxStatusTLPEOCreatedBy | CREATED_BY | — | — |
| 4 | TaxStatusTLPEOCreationDate | CREATION_DATE | — | — |
| 5 | TaxStatusTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | TaxStatusTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | TaxStatusTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | TaxStatusTLPEOSourceLang | SOURCE_LANG | — | — |
| 9 | TaxStatusTLPEOTaxStatusName | TAX_STATUS_NAME | — | ✅ |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
